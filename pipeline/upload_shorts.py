"""Upload finished shorts to dhivehivaahaka.com via the shorts integration API.

Finds output/<Series>/episode-<N>/<Series>_Episode<N>_TikTok.mp4 and uploads each
one as the short for episode id N (chunked upload, see shorts-integration.md).

Credentials: SHORTS_CLIENT_ID / SHORTS_CLIENT_SECRET from the environment or env.txt
(an API client with the `shorts.upload` ability).

Usage:
  python pipeline/upload_shorts.py --check            # read-only: list episode/book + existing shorts
  python pipeline/upload_shorts.py                    # upload everything not already on the site
  python pipeline/upload_shorts.py --only 341 358     # restrict to some episode ids
  python pipeline/upload_shorts.py --replace          # also replace episodes that already have a short
  python pipeline/upload_shorts.py --poll             # poll status of shorts recorded in the log
"""
import argparse
import json
import os
import re
import sys
import time
import warnings
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

warnings.filterwarnings("ignore")
import requests  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
LOG = ROOT / "output" / "shorts_upload_log.json"
VIDEO_RE = re.compile(r"^(?P<series>.+)_Episode(?P<ep>\d+)_TikTok\.mp4$")


def load_env():
    env = {}
    p = ROOT / "env.txt"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    env.update({k: v for k, v in os.environ.items() if k.startswith(("SHORTS_", "SITE_URL"))})
    return env


ENV = load_env()
BASE = ENV.get("SITE_URL", "https://dhivehivaahaka.com").rstrip("/") + "/api/v1/integrations"
CLIENT_ID = ENV.get("SHORTS_CLIENT_ID")
CLIENT_SECRET = ENV.get("SHORTS_CLIENT_SECRET")


def session():
    s = requests.Session()
    s.headers.update({"X-Client-Id": CLIENT_ID, "X-Client-Secret": CLIENT_SECRET,
                      "Accept": "application/json"})
    return s


def call(s, method, path, retries=6, **kw):
    """HTTP call with retry on 429 / 5xx / network errors. Returns the response."""
    url = path if path.startswith("http") else BASE + path
    for attempt in range(retries):
        try:
            r = s.request(method, url, timeout=300, **kw)
        except requests.RequestException as e:
            wait = 5 * (attempt + 1)
            print(f"    network error {e!r}; retry in {wait}s")
            time.sleep(wait)
            continue
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After", 30))
            print(f"    rate limited; waiting {wait}s")
            time.sleep(wait)
            continue
        if r.status_code >= 500:
            wait = 5 * (attempt + 1)
            print(f"    HTTP {r.status_code}; retry in {wait}s")
            time.sleep(wait)
            continue
        return r
    raise RuntimeError(f"{method} {url} failed after {retries} attempts")


def find_videos(only=None):
    vids = []
    for f in sorted(OUTPUT.glob("*/episode-*/*_TikTok.mp4")):
        m = VIDEO_RE.match(f.name)
        if not m:
            continue
        ep = int(m["ep"])
        if only and ep not in only:
            continue
        vids.append({"episode_id": ep, "series": m["series"], "path": f, "size": f.stat().st_size})
    return vids


def load_log():
    return json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else {}


def save_log(log):
    LOG.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")


def check_episode(s, ep):
    r = call(s, "GET", f"/episodes/{ep}/shorts")
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def upload(s, v, replace, workers):
    ep, path, size = v["episode_id"], v["path"], v["size"]
    data = {"episode_id": ep, "filename": path.name, "size": size}
    if replace:
        data["replace"] = 1
    r = call(s, "POST", "/shorts/uploads", json=data)
    if r.status_code == 409:
        return {"status": "skipped", "reason": "already has a short (409)"}
    if r.status_code != 201:
        return {"status": "error", "reason": f"start HTTP {r.status_code}: {r.text[:500]}"}
    up = r.json()["upload"]
    uid, chunk, total = up["id"], up["chunk_size"], up["total_chunks"]
    print(f"    upload {uid}: {total} chunks of {chunk // 1048576} MB")

    def send(i):
        with open(path, "rb") as fh:
            fh.seek(i * chunk)
            body = fh.read(chunk)
        rr = call(s, "PUT", f"/shorts/uploads/{uid}/chunks/{i}", data=body,
                  headers={"Content-Type": "application/octet-stream"})
        if rr.status_code != 200:
            raise RuntimeError(f"chunk {i}: HTTP {rr.status_code} {rr.text[:300]}")
        return i

    todo = list(range(total))
    for _ in range(3):
        failed = []
        with ThreadPoolExecutor(workers) as pool:
            futs = {i: pool.submit(send, i) for i in todo}
            for i, f in futs.items():
                try:
                    f.result()
                except Exception as e:  # noqa: BLE001
                    print(f"    {e}")
                    failed.append(i)
        if not failed:
            break
        todo = failed

    for _ in range(3):
        r = call(s, "POST", f"/shorts/uploads/{uid}/complete")
        if r.status_code == 202:
            short = r.json()["short"]
            return {"status": short["status"], "short_id": short["id"], "upload_id": uid}
        if r.status_code == 422 and r.json().get("missing_chunks"):
            for i in r.json()["missing_chunks"]:
                send(i)
            continue
        return {"status": "error", "upload_id": uid,
                "reason": f"complete HTTP {r.status_code}: {r.text[:500]}"}
    return {"status": "error", "upload_id": uid, "reason": "chunks still missing after retries"}


def poll(s, log, until_done=True, interval=20):
    pending = {ep: e for ep, e in log.items()
               if e.get("short_id") and e.get("status") not in ("ready", "failed")}
    while pending:
        for ep, e in list(pending.items()):
            r = call(s, "GET", f"/shorts/{e['short_id']}")
            if r.status_code != 200:
                print(f"  ep {ep}: HTTP {r.status_code}")
                continue
            sh = r.json()["short"]
            e["status"] = sh["status"]
            e["error"] = sh.get("error")
            print(f"  ep {ep}: {sh['status']} {sh.get('encode_progress') or ''} {sh.get('error') or ''}")
            if sh["status"] in ("ready", "failed"):
                pending.pop(ep)
            time.sleep(1.1)  # stay under 60 req/min
        save_log(log)
        if not until_done or not pending:
            break
        time.sleep(interval)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="read-only listing, no uploads")
    ap.add_argument("--replace", action="store_true")
    ap.add_argument("--only", type=int, nargs="*")
    ap.add_argument("--poll", action="store_true", help="only poll shorts from the log")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    if not CLIENT_ID or not CLIENT_SECRET:
        sys.exit("Missing SHORTS_CLIENT_ID / SHORTS_CLIENT_SECRET (env or env.txt).")

    s = session()
    log = load_log()
    if args.poll:
        poll(s, log)
        return

    vids = find_videos(set(args.only) if args.only else None)
    print(f"{len(vids)} videos found")
    for v in vids:
        ep = v["episode_id"]
        key = str(ep)
        info = check_episode(s, ep)
        time.sleep(1.1)
        if info is None:
            print(f"[{ep}] {v['series']}: episode not found on site (404) - skipped")
            log[key] = {"series": v["series"], "status": "error", "reason": "episode 404"}
            save_log(log)
            continue
        e, b = info["episode"], info["episode"]["book"]
        print(f"[{ep}] {v['series']} -> book '{b['title']}' ({b['slug']}), ep order {e['order']}, "
              f"has_short={info['has_short']} ready={info['has_ready_short']}, "
              f"{v['size'] / 1048576:.0f} MB")
        if args.check:
            continue
        if info["has_short"] and not args.replace:
            print("    already has a short - skipped")
            log.setdefault(key, {"series": v["series"], "status": "skipped",
                                 "reason": "already has a short"})
            save_log(log)
            continue
        res = upload(s, v, args.replace, args.workers)
        res.update(series=v["series"], file=str(v["path"].relative_to(ROOT)), book=b["slug"])
        print(f"    -> {res['status']} {res.get('short_id') or res.get('reason', '')}")
        log[key] = res
        save_log(log)

    if not args.check:
        print("\nPolling processing status...")
        poll(s, log)
        done = sum(1 for e in log.values() if e.get("status") == "ready")
        print(f"\n{done} ready; see {LOG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

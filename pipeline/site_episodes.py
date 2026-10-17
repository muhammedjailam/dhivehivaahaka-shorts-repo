"""Story-ID mode helpers (main prompt section 13): fetch a book's episodes + shorts, download audio bundles,
delete leftover old shorts after a replacement is live.

Credentials and HTTP retry come from upload_shorts.py (SHORTS_CLIENT_ID / SHORTS_CLIENT_SECRET in env.txt).
Rate limit 60 req/min: every call is followed by a 1.1 s pause.

Usage:
  python pipeline/site_episodes.py <book_id>                        # read-only: table + output/<series>/site_episodes.json
  python pipeline/site_episodes.py <book_id> --download new         # bundles for episodes with audio and no short
  python pipeline/site_episodes.py <book_id> --download new --orders 10-14
  python pipeline/site_episodes.py <book_id> --download replace --only 520 521   (or --all)
  python pipeline/site_episodes.py <book_id> --delete-old --only 520 521         # dry run: shows what would go
  python pipeline/site_episodes.py <book_id> --delete-old --only 520 521 --yes   # delete them

--delete-old keeps the short recorded for the episode in output/shorts_upload_log.json (the replacement) once it
is `ready`, and deletes every other short of that episode created before it. Nothing is deleted while the
replacement is not ready. 409 (old short still uploading) is retried after a minute.
"""
import argparse
import json
import re
import shutil
import sys
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_shorts import CLIENT_ID, CLIENT_SECRET, OUTPUT, ROOT, call, load_log, session  # noqa: E402

PAUSE = 1.1


def get(s, path):
    r = call(s, "GET", path)
    time.sleep(PAUSE)
    return r


# ---------------------------------------------------------------- local folders
def find_series(ids, slug):
    """Series = output/<series> whose episode-<id> folders (incl. _archive_v*) use this book's episode ids."""
    best, hits = None, 0
    for d in OUTPUT.iterdir():
        if not d.is_dir():
            continue
        have = {int(m[1]) for p in d.glob("**/episode-*") if p.is_dir() and (m := re.fullmatch(r"episode-(\d+)", p.name))}
        h = len(have & ids)
        if h > hits:
            best, hits = d.name, h
    return best or re.sub(r"[^A-Za-z0-9]+", "", slug.title()) or "Book"


def find_input(series, ids):
    """Input folder = root dir holding episode-<id>-audio.zip for this book (or this series' episodes)."""
    series_ids = {int(m[1]) for p in (OUTPUT / series).glob("**/episode-*")
                  if (m := re.fullmatch(r"episode-(\d+)", p.name))} if (OUTPUT / series).exists() else set()
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and d.name not in ("output", "pipeline", "sfx", "docs", "fonts") and not d.name.startswith("."):
            zips = {int(m[1]) for z in d.glob("episode-*-audio.zip") if (m := re.fullmatch(r"episode-(\d+)-audio\.zip", z.name))}
            if zips & (ids | series_ids):
                return d
    return ROOT / series


# ---------------------------------------------------------------- fetch
def fetch(s, book_id):
    r = get(s, f"/books/{book_id}/episodes")
    if r.status_code == 404:
        sys.exit(f"book {book_id}: not found (404)")
    r.raise_for_status()
    data = r.json()
    for e in data["episodes"]:
        e["shorts"] = []
        if e.get("shorts_count"):
            rr = get(s, f"/episodes/{e['id']}/shorts")
            if rr.status_code == 200:
                e["shorts"] = [{k: sh.get(k) for k in ("id", "status", "source", "is_active", "created_at",
                                                       "processed_at", "error", "uploaded_by_client")}
                               for sh in rr.json()["shorts"]]
    return data


def print_table(data, series, inp):
    b = data["book"]
    print(f"book {b['id']} '{b['title']}' ({b['slug']}, {b['status']}) -> series {series}, input {inp.relative_to(ROOT)}")
    print(f"{'ord':>4} {'ep id':>6}  {'status':10} {'bundle':6} {'dur':>6}  shorts (id/status/source)  title")
    for e in data["episodes"]:
        dur = f"{e['audio_duration'] / 60000:.1f}m" if e.get("audio_duration") else "-"
        sh = ", ".join(f"{x['id']}/{x['status']}/{x['source']}" for x in e["shorts"]) or "-"
        print(f"{e['order']:>4} {e['id']:>6}  {e['status']:10} {'yes' if e['has_audio_bundle'] else 'no':6} "
              f"{dur:>6}  {sh:26} {e['title']}")
    n = len(data["episodes"])
    new = sum(1 for e in data["episodes"] if e["has_audio_bundle"] and not e["has_short"])
    print(f"{n} episodes; {sum(e['has_short'] for e in data['episodes'])} with a short; {new} ready for a new short")


# ---------------------------------------------------------------- download
def pick(data, mode, only, orders, all_):
    eps = data["episodes"]
    if only:
        eps = [e for e in eps if e["id"] in only]
    if orders:
        eps = [e for e in eps if orders[0] <= e["order"] <= orders[1]]
    targets, skipped = [], []
    for e in eps:
        if not e["has_audio_bundle"]:
            skipped.append((e, "no audio bundle yet"))
        elif mode == "new" and e["has_short"]:
            skipped.append((e, "already has a short"))
        elif mode == "replace" and not e["has_short"] and not (only or orders):
            skipped.append((e, "no short to replace"))
        else:
            targets.append(e)
    if mode == "replace" and not (only or orders or all_):
        sys.exit("--download replace needs --only <ids>, --orders a-b or --all")
    return targets, skipped


def download(s, e, inp):
    """Fresh bundle -> <inp>/episode-<id>-audio.zip (an existing zip is moved to <inp>/_archive/ first)."""
    ep = e["id"]
    r = call(s, "GET", f"/episodes/{ep}/audio-bundle", stream=True)
    time.sleep(PAUSE)
    if r.status_code == 404:
        return f"skipped: 404 {r.json().get('message', '') if 'json' in r.headers.get('Content-Type', '') else ''}"
    if r.status_code != 200:
        return f"error: HTTP {r.status_code} {r.text[:200]}"
    inp.mkdir(parents=True, exist_ok=True)
    dest = inp / f"episode-{ep}-audio.zip"
    tmp = dest.with_suffix(".zip.part")
    with open(tmp, "wb") as fh:
        for chunk in r.iter_content(1 << 20):
            fh.write(chunk)
    if not zipfile.is_zipfile(tmp):
        tmp.unlink()
        return "error: response is not a zip"
    note = ""
    if dest.exists():
        arch = inp / "_archive"
        arch.mkdir(exist_ok=True)
        old = arch / f"episode-{ep}-audio.{datetime.now():%Y%m%d-%H%M%S}.zip"
        shutil.move(dest, old)
        note = f" (old zip -> {old.relative_to(ROOT)})"
    tmp.replace(dest)
    with zipfile.ZipFile(dest) as z:
        names = z.namelist()
    return f"ok {dest.stat().st_size / 1048576:.1f} MB, {len(names)} files{note}"


# ---------------------------------------------------------------- delete leftovers
def delete_old(s, ids, yes):
    log = load_log()
    for ep in ids:
        new_id = (log.get(str(ep)) or {}).get("short_id")
        r = get(s, f"/episodes/{ep}/shorts")
        if r.status_code != 200:
            print(f"[{ep}] HTTP {r.status_code} - skipped")
            continue
        shorts = r.json()["shorts"]
        new = next((x for x in shorts if x["id"] == new_id), None)
        if not new:
            print(f"[{ep}] replacement short {new_id} (upload log) not on the site - nothing deleted")
            continue
        if new["status"] != "ready":
            print(f"[{ep}] replacement short {new_id} is {new['status']} - nothing deleted yet")
            continue
        old = [x for x in shorts if x["id"] != new_id and x["created_at"] <= new["created_at"]]
        later = [x["id"] for x in shorts if x["id"] != new_id and x not in old]
        print(f"[{ep}] keep {new_id} (ready); old: "
              + (", ".join(f"{x['id']}/{x['status']}/{x['source']}" for x in old) or "none")
              + (f"; newer shorts left alone: {later}" if later else ""))
        if not yes:
            continue
        for x in old:
            for attempt in range(4):
                rr = call(s, "DELETE", f"/shorts/{x['id']}")
                time.sleep(PAUSE)
                if rr.status_code == 409 and attempt < 3:
                    print(f"    {x['id']}: still uploading (409); retry in 60s")
                    time.sleep(60)
                    continue
                print(f"    delete {x['id']}: HTTP {rr.status_code}"
                      + (" (already gone)" if rr.status_code == 404 else ""))
                break
    if not yes:
        print("dry run - add --yes to delete")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book_id", type=int)
    ap.add_argument("--series", help="override the output/<series> folder name")
    ap.add_argument("--input", help="override the input folder for audio zips")
    ap.add_argument("--download", choices=["new", "replace"])
    ap.add_argument("--only", type=int, nargs="+", help="episode ids")
    ap.add_argument("--orders", help="episode order range, e.g. 10-14")
    ap.add_argument("--all", action="store_true", help="with --download replace: every episode with a short")
    ap.add_argument("--delete-old", action="store_true", help="delete leftover old shorts of --only episodes")
    ap.add_argument("--yes", action="store_true", help="actually delete (with --delete-old)")
    args = ap.parse_args()
    if not CLIENT_ID or not CLIENT_SECRET:
        sys.exit("Missing SHORTS_CLIENT_ID / SHORTS_CLIENT_SECRET (env or env.txt).")
    orders = tuple(int(x) for x in args.orders.split("-", 1)) if args.orders else None
    if orders and len(orders) == 1:
        orders = (orders[0], orders[0])

    s = session()
    if args.delete_old:
        if not args.only:
            sys.exit("--delete-old needs --only <episode ids>")
        delete_old(s, args.only, args.yes)
        return

    data = fetch(s, args.book_id)
    ids = {e["id"] for e in data["episodes"]}
    series = args.series or find_series(ids, data["book"]["slug"])
    inp = Path(args.input).resolve() if args.input else find_input(series, ids)
    data["series"] = series
    data["input_folder"] = inp.relative_to(ROOT).as_posix() if inp.is_relative_to(ROOT) else str(inp)
    data["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (OUTPUT / series).mkdir(parents=True, exist_ok=True)
    out = OUTPUT / series / "site_episodes.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print_table(data, series, inp)
    print(f"saved {out.relative_to(ROOT)}")

    if args.download:
        targets, skipped = pick(data, args.download, set(args.only or []), orders, args.all)
        print(f"\n{args.download}: {len(targets)} targets " + " ".join(str(e["id"]) for e in targets))
        for e, why in skipped:
            print(f"  skip {e['id']} (order {e['order']}): {why}")
        for e in targets:
            old = [x["id"] for x in e["shorts"] if x["status"] != "failed"]
            print(f"  [{e['id']}] order {e['order']}: {download(s, e, inp)}"
                  + (f"; existing shorts {old}" if old else ""))


if __name__ == "__main__":
    main()

"""ElevenLabs text-to-sound generation + the shared sound library (main prompt sections 8.1-8.2).

Library: sfx/elevenlabs/<category>/<key>.mp3 plus one JSON line per sound in sfx/elevenlabs/index.jsonl
(key, category, prompt, duration_seconds, loop, prompt_influence, model_id, file, created, used_in).
Existing keys are reused, never regenerated (unless --force). Key: ElevenLabs_API_key in env.txt or
ELEVENLABS_API_KEY in the environment; it is never printed or written anywhere.

Usage:
  python pipeline/sfx_elevenlabs.py gen ambience rain_tin_roof_night "steady tropical rain on a tin roof..." \
         --duration 25 --loop
  python pipeline/sfx_elevenlabs.py gen sfx door_knock_wooden "three knocks on a wooden door, close" --duration 3
  python pipeline/sfx_elevenlabs.py batch specs.json      # [{"category","key","prompt","duration","loop","influence"}]
  python pipeline/sfx_elevenlabs.py list [--category ambience]
  python pipeline/sfx_elevenlabs.py find rain roof         # search keys + prompts
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import warnings
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "sfx" / "elevenlabs"
INDEX = LIB / "index.jsonl"
API = "https://api.elevenlabs.io/v1/sound-generation"
MODEL = "eleven_text_to_sound_v2"
NO_MUSIC = "no music, no melody, no singing, no speech, no voices"
CROWD_RE = re.compile(r"\b(crowd|market|murmur|chatter|people|cafe|bazaar|street)\b", re.I)
CROWD = "indistinct murmur, no intelligible words"
# never generate religious audio with AI (section 8.1)
RELIGIOUS_RE = re.compile(r"\b(adhan|azan|athan|call to prayer|quran|qur'an|recitation|dua|du'a|takbir|nasheed)\b", re.I)
KEY_RE = re.compile(r"^[a-z0-9_]+$")


# ---------------------------------------------------------------- library index
def load_index():
    """key -> entry (last line for a key wins)."""
    idx = {}
    if INDEX.exists():
        for line in INDEX.read_text(encoding="utf-8").splitlines():
            if line.strip():
                e = json.loads(line)
                idx[e["key"]] = e
    return idx


def save_index(idx):
    LIB.mkdir(parents=True, exist_ok=True)
    tmp = INDEX.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in idx.values()), encoding="utf-8")
    tmp.replace(INDEX)


def lookup(key, category=None):
    """Library entry for `key` (or "category/key") whose file exists, else None."""
    if "/" in key:
        category, key = key.split("/", 1)
    e = load_index().get(key)
    if not e or (category and e["category"] != category) or not (ROOT / e["file"]).exists():
        return None
    return e


def variants(key):
    """The entry for `key` plus its variations `<key>_v2`, `<key>_v3`... (for long beds)."""
    idx = load_index()
    base = key.split("/", 1)[-1]
    out = [idx[base]] if base in idx else []
    out += [idx[k] for k in sorted(idx) if re.fullmatch(re.escape(base) + r"_v\d+", k)]
    return [e for e in out if (ROOT / e["file"]).exists()]


def mark_used(keys, label):
    """Add `label` (e.g. "Karuna/episode-335") to used_in of each key."""
    idx = load_index()
    changed = False
    for k in keys:
        e = idx.get(k.split("/", 1)[-1])
        if e is not None and label not in e.setdefault("used_in", []):
            e["used_in"].append(label)
            changed = True
    if changed:
        save_index(idx)


# ---------------------------------------------------------------- generation
def api_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    p = ROOT / "env.txt"
    if not k and p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                name, v = line.split("=", 1)
                if name.strip() in ("ElevenLabs_API_key", "ELEVENLABS_API_KEY") and v.strip():
                    k = v.strip()
    return k


def full_prompt(prompt):
    p = prompt.strip().rstrip(".")
    if CROWD_RE.search(p) and CROWD not in p:
        p += ", " + CROWD
    if NO_MUSIC not in p:
        p += ", " + NO_MUSIC
    return p


def probe_duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True)
    try:
        return round(float(r.stdout.strip()), 3)
    except ValueError:
        return None


def generate(category, key, prompt, duration=None, loop=False, influence=0.4, force=False, key_=None):
    """Generate one sound into the library (or return the existing entry). Returns the index entry."""
    if not KEY_RE.match(key) or not KEY_RE.match(category):
        raise ValueError(f"key/category must be [a-z0-9_]+: {category}/{key}")
    if RELIGIOUS_RE.search(prompt):
        raise ValueError(f"{key}: religious audio is never generated with AI (section 8.1)")
    if duration is not None and not 0.5 <= duration <= 30:
        raise ValueError(f"{key}: duration_seconds must be 0.5-30")
    existing = load_index().get(key)
    if existing and not force and (ROOT / existing["file"]).exists():
        print(f"  reuse {category}/{key} ({existing.get('actual_seconds')} s)")
        return existing
    k = key_ or api_key()
    if not k:
        raise RuntimeError("no ElevenLabs key (ElevenLabs_API_key in env.txt) - use procedural fallback (8.4)")

    import requests
    text = full_prompt(prompt)
    body = {"text": text, "model_id": MODEL, "duration_seconds": duration,
            "prompt_influence": influence, "loop": bool(loop)}
    out = LIB / category / f"{key}.mp3"
    out.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(5):
        try:
            r = requests.post(API, params={"output_format": "mp3_44100_128"}, json=body, timeout=180,
                              headers={"xi-api-key": k, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        except requests.RequestException as e:
            wait = 2 ** attempt * 3
            print(f"  {key}: network error {type(e).__name__}; retry in {wait}s")
            time.sleep(wait)
            continue
        if r.status_code == 429 or r.status_code >= 500:
            wait = int(r.headers.get("Retry-After") or 2 ** attempt * 3)
            print(f"  {key}: HTTP {r.status_code}; retry in {wait}s")
            time.sleep(wait)
            continue
        if r.status_code != 200:
            try:
                detail = r.json().get("detail")
            except ValueError:
                detail = r.text[:300]
            raise RuntimeError(f"{key}: HTTP {r.status_code}: {detail}")
        if not r.content or "json" in r.headers.get("Content-Type", ""):
            raise RuntimeError(f"{key}: no audio in response")
        tmp = out.with_suffix(".part")
        tmp.write_bytes(r.content)
        tmp.replace(out)
        cost = {h: v for h, v in r.headers.items() if re.search(r"cost|character|credit", h, re.I)}
        entry = {"key": key, "category": category, "prompt": text, "duration_seconds": duration, "loop": bool(loop),
                 "prompt_influence": influence, "model_id": MODEL, "file": out.relative_to(ROOT).as_posix(),
                 "actual_seconds": probe_duration(out), "bytes": len(r.content),
                 "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "used_in": (existing or {}).get("used_in", [])}
        if cost:
            entry["api_cost_headers"] = cost
        idx = load_index()
        idx[key] = entry
        save_index(idx)
        print(f"  new   {category}/{key}: {entry['actual_seconds']} s, {len(r.content) // 1024} KB"
              + (f", {cost}" if cost else ""))
        return entry
    raise RuntimeError(f"{key}: failed after 5 tries")


# ---------------------------------------------------------------- CLI
def main():
    warnings.filterwarnings("ignore")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gen", help="generate one sound (reuses an existing key)")
    g.add_argument("category", help="ambience | sfx | ...")
    g.add_argument("key", help="library key, [a-z0-9_]+")
    g.add_argument("prompt")
    g.add_argument("--duration", type=float, help="0.5-30 s (omit = model picks)")
    g.add_argument("--loop", action="store_true", help="seamless loop (beds)")
    g.add_argument("--influence", type=float, default=0.4, help="prompt_influence 0.3-0.6")
    g.add_argument("--force", action="store_true", help="regenerate even if the key exists")
    b = sub.add_parser("batch", help="generate a JSON list of specs, 3 in parallel")
    b.add_argument("specs")
    b.add_argument("--workers", type=int, default=3)
    l_ = sub.add_parser("list", help="list the library")
    l_.add_argument("--category")
    f = sub.add_parser("find", help="search keys and prompts")
    f.add_argument("words", nargs="+")
    args = ap.parse_args()

    if args.cmd == "gen":
        generate(args.category, args.key, args.prompt, args.duration, args.loop, args.influence, args.force)
    elif args.cmd == "batch":
        specs = json.loads(Path(args.specs).read_text(encoding="utf-8"))
        k = api_key()

        def one(s):
            try:
                return generate(s["category"], s["key"], s["prompt"], s.get("duration"), s.get("loop", False),
                                s.get("influence", 0.4), s.get("force", False), key_=k)
            except Exception as e:  # noqa: BLE001
                print(f"  FAILED {s.get('key')}: {e}")
                return None
        with ThreadPoolExecutor(min(3, args.workers)) as pool:
            res = list(pool.map(one, specs))
        print(f"{sum(r is not None for r in res)}/{len(specs)} ok")
        if not all(res):
            sys.exit(1)
    else:
        idx = load_index()
        rows = [e for e in idx.values() if args.cmd == "list" and (not args.category or e["category"] == args.category)
                or args.cmd == "find" and all(w.lower() in (e["key"] + " " + e["prompt"]).lower() for w in args.words)]
        for e in sorted(rows, key=lambda e: (e["category"], e["key"])):
            print(f"{e['category'] + '/' + e['key']:45s} {str(e.get('actual_seconds')):>7s}s "
                  f"{'loop ' if e.get('loop') else '     '}{len(e.get('used_in', []))} uses  {e['prompt'][:70]}")
        print(f"{len(rows)} sounds")


if __name__ == "__main__":
    main()

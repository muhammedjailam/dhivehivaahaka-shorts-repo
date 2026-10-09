"""Generate character references and shot images with the OpenAI Images API.
Usage: python gen_images.py <series_dir> <episode_dir> [refs|shots|all] [shot_id ...]
Resumable: existing images are skipped. Every call is logged to <episode_dir>/generation_log.jsonl.
"""
import base64, json, os, re, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

MODEL = "gpt-image-2.5-flare"
QUALITY = "low"
SIZE = "1024x1536"
REF_SIZE = "1536x1024"
PARALLEL = 3
EST_COST_PER_IMAGE = 0.02  # USD, rough estimate for low quality portrait

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for line in open(os.path.join(PROJECT, "env.txt"), encoding="utf-8"):
    if "=" in line:
        k, v = line.strip().split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())
from openai import OpenAI, BadRequestError, RateLimitError, APIStatusError, APIConnectionError, APITimeoutError
client = OpenAI(timeout=300)

series_dir, ep_dir = sys.argv[1], sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else "all"
only = set(sys.argv[4:])
STYLE = open(os.path.join(series_dir, "style.txt"), encoding="utf-8").read().strip()
TAIL = "Modest Maldivian clothing, culturally respectful, no violence shown, no text, no letters, no writing, no watermark."
if os.path.exists(os.path.join(series_dir, "tail.txt")):   # per-series override (e.g. stories set outside the Maldives)
    TAIL = open(os.path.join(series_dir, "tail.txt"), encoding="utf-8").read().strip()
LOG = os.path.join(ep_dir, "generation_log.jsonl")
lock = threading.Lock()
stats = {"ok": 0, "refused": 0, "error": 0, "calls": 0}

MOOD = {
    "bedroom": "night, dim warm lamp light, deep shadows, melancholic",
    "living": "night, warm indoor light, tense domestic atmosphere",
    "street": "night, warm sodium streetlights, blue shadows, lonely",
    "road": "night, harsh white headlights and streetlights, tense",
    "memory": "hazy, desaturated, dreamlike memory, soft vignette",
    "beach": "night, silver moonlight, deep blue sea, gentle wind, melancholic and tender",
    "house_other": "dim, low-key lighting, cold atmosphere",
}
TRIGGERS = r"\b(violence|violent|injur\w*|blood\w*|death|dead|die|dying|crying|cry|cries|sobbing|sobs?|tears?|tearful|teary|body|bed|bathroom|slap\w*|fight\w*|abuse\w*|kill\w*|accident|terror|scream\w*|hit|knocked|harsh|angry|cruel|wounded|grave\w*|cemetery|burn\w*|disgust\w*|frozen|shadow of a man|pointing|kiss\w*|hug\w*|lap|touch\w*)\b"


def log(entry):
    with lock:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def is_refusal(e):
    msg = (getattr(e, "message", "") or str(e)).lower()
    code = ""
    try:
        code = (e.body or {}).get("code") or (e.body or {}).get("error", {}).get("code") or ""
    except Exception:
        pass
    return code in ("moderation_blocked", "content_policy_violation") or any(
        k in msg for k in ("safety", "moderation", "content policy", "content_policy"))


def call(prompt, refs, size):
    """One API call with retry/backoff on 429/5xx/network. Returns png bytes or raises."""
    delay = 4
    for t in range(5):
        try:
            if refs:
                files = [open(r, "rb") for r in refs]
                try:
                    r = client.images.edit(model=MODEL, image=files, prompt=prompt, size=size, quality=QUALITY, n=1)
                finally:
                    for f in files: f.close()
            else:
                r = client.images.generate(model=MODEL, prompt=prompt, size=size, quality=QUALITY, n=1)
            usage = getattr(r, "usage", None)
            return base64.b64decode(r.data[0].b64_json), (usage.model_dump() if usage else None)
        except (RateLimitError, APIConnectionError, APITimeoutError) as e:
            err = e
        except APIStatusError as e:
            if e.status_code < 500 and e.status_code != 429:
                raise
            err = e
        if t == 4:
            raise err
        time.sleep(delay); delay *= 2


def generate(item_id, attempts, out_path, size):
    """attempts: list of (prompt, refs, rewrite_reason). Tries in order on refusal."""
    if os.path.exists(out_path):
        return {"id": item_id, "status": "exists"}
    history = []
    for n, (prompt, refs, reason) in enumerate(attempts, 1):
        entry = {"beat": item_id, "attempt": n, "model": MODEL, "endpoint": "edit" if refs else "generate",
                 "refs": [os.path.relpath(r, ep_dir).replace("\\", "/") for r in refs], "prompt": prompt,
                 "rewrite_reason": reason, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
        try:
            with lock: stats["calls"] += 1
            png, usage = call(prompt, refs, size)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            open(out_path, "wb").write(png)
            entry.update(result="ok", usage=usage)
            log(entry); history.append(entry)
            with lock: stats["ok"] += 1
            print(f"[ok] {item_id} attempt {n}  (calls {stats['calls']})", flush=True)
            return {"id": item_id, "status": "ok", "attempt": n, "history": history}
        except BadRequestError as e:
            refused = is_refusal(e)
            entry.update(result="refused" if refused else "error", error=str(e)[:400])
            log(entry); history.append(entry)
            with lock: stats["refused" if refused else "error"] += 1
            print(f"[{'refused' if refused else 'error'}] {item_id} attempt {n}: {str(e)[:160]}", flush=True)
            if not refused and n >= 2:
                break
        except Exception as e:
            entry.update(result="error", error=f"{type(e).__name__}: {str(e)[:400]}")
            log(entry); history.append(entry)
            with lock: stats["error"] += 1
            print(f"[error] {item_id} attempt {n}: {type(e).__name__} {str(e)[:160]}", flush=True)
            break
    return {"id": item_id, "status": "failed", "history": history}


# ---------------------------------------------------------------- references
def ref_jobs():
    jobs = []
    cover = os.path.join(ep_dir, "work", f"episode-{os.path.basename(ep_dir).split('-')[-1]}-cover.png")
    for cid in sorted(os.listdir(os.path.join(series_dir, "characters"))):
        d = os.path.join(series_dir, "characters", cid)
        card = json.load(open(os.path.join(d, "card.json"), encoding="utf-8"))
        out = os.path.join(d, "reference.png")
        pose = card.get("ref_pose") or (
            "left: head-and-shoulders portrait; right: full-body view seated in her black manual wheelchair"
            if cid == "dhooma" else "left: head-and-shoulders portrait; right: full-body standing view")
        body = (f"{STYLE.split(', vertical')[0]}. Character reference sheet of {card['visual_prompt']} "
                f"Two views side by side — {pose}. Front-facing, neutral calm expression, default outfit, "
                f"plain soft warm-grey studio background, even soft lighting. {TAIL}")
        refs, lead = [], ""
        if card.get("reference_from_cover"):
            who = "woman" if card["gender"] == "female" else "man"
            refs = [cover]
            if card.get("cover_crop"):   # [x0, y0, x1, y1] fractions of the cover: isolate one person
                from PIL import Image
                im = Image.open(cover); x0, y0, x1, y1 = card["cover_crop"]
                crop = os.path.join(d, "cover_crop.png")
                im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height))).save(crop)
                refs = [crop]
            lead = (f"Use the {who} in the reference image only as the likeness for this character's face; "
                    f"ignore the pose, any other person, the background and any lettering. ")
        attempts = [(lead + body, refs, None),
                    (body, [], "attempt 1 refused: dropped cover reference")]
        jobs.append((f"ref:{cid}", attempts, out, REF_SIZE))
    return jobs


# ---------------------------------------------------------------- shots
def beat_jobs():
    scenes = json.load(open(os.path.join(ep_dir, "scenes.json"), encoding="utf-8"))["beats"]
    cards = {}
    jobs = []
    for s in scenes:
        if s["reuse_of"] or (only and s["id"] not in only):
            continue
        refs, vps, names = [], [], []
        for cid in s["characters"][:4]:
            d = os.path.join(series_dir, "characters", cid)
            if cid not in cards:
                cards[cid] = json.load(open(os.path.join(d, "card.json"), encoding="utf-8"))
            refs.append(os.path.join(d, "reference.png"))
            vps.append(cards[cid]["visual_prompt"])
            names.append(cards[cid]["name"].split(" (")[0])
        mood = s.get("mood") or MOOD[s["location_key"]]
        core = (f"Scene: {s['visual']}. Location: {s['location']}. Camera: {s['camera']}.\n"
                + (f"Characters: {' '.join(vps)}\n" if vps else "")
                + f"Mood/lighting: {mood}.\n{TAIL}")
        if refs:
            mapping = "; ".join(f"reference image {i + 1} is {n}" for i, n in enumerate(names))
            p1 = (f"Using the reference images for the characters' faces and clothing ({mapping}), "
                  f"create a new scene: {STYLE}\n{core}")
        else:
            p1 = f"{STYLE}\n{core}"
        # attempt 2: neutral wording
        neutral_visual = re.sub(TRIGGERS, "", s["visual"], flags=re.I)
        neutral_visual = re.sub(r"\s{2,}", " ", neutral_visual).strip(" ,;")
        core2 = (f"Scene: {neutral_visual}, calm and emotional. Location: {s['location']}. Camera: {s['camera']}.\n"
                 + (f"Characters: {' '.join(vps)}\n" if vps else "") + f"Mood/lighting: {mood}.\n{TAIL}")
        p2 = (f"Using the reference images for the characters' faces and clothing, create a new scene: {STYLE}\n{core2}"
              if refs else f"{STYLE}\n{core2}")
        # attempt 3: symbolism
        p3 = (f"{STYLE}\nScene: a symbolic, quiet image for this moment — a lone figure in modest clothing seen "
              f"from behind as a soft silhouette, in {s['location']}. Mood/lighting: {mood}.\n{TAIL}")
        # attempt 4: establishing shot
        p4 = f"{STYLE}\nScene: establishing shot of {s['location']}, no people. Mood/lighting: {mood}.\n{TAIL}"
        attempts = [(p1, refs, None),
                    (p2, refs, "refused: removed trigger words, neutral emotion/setting wording"),
                    (p3, [], "refused again: symbolic silhouette, no references"),
                    (p4, [], "refused again: generic establishing shot, no people")]
        jobs.append((s["id"], attempts, os.path.join(ep_dir, "images", f"{s['id']}.png"), SIZE))
    return jobs


def run(jobs):
    results = []
    with ThreadPoolExecutor(PARALLEL) as ex:
        for r in ex.map(lambda j: generate(*j), jobs):
            results.append(r)
    return results


if __name__ == "__main__":
    results = []
    if mode in ("refs", "all"):
        results += run(ref_jobs())
    if mode in ("beats", "shots", "all"):
        results += run(beat_jobs())
        # record attempts in scenes.json
        sp = os.path.join(ep_dir, "scenes.json")
        doc = json.load(open(sp, encoding="utf-8")); scenes = doc["beats"]
        by = {r["id"]: r for r in results if r.get("history")}
        for s in scenes:
            if s["id"] in by:
                s["prompt_attempts"] = [{"attempt": h["attempt"], "result": h["result"], "rewrite_reason": h["rewrite_reason"]}
                                        for h in by[s["id"]]["history"]]
                s["final_prompt"] = by[s["id"]]["history"][-1]["prompt"]
        json.dump(doc, open(sp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    failed = [r["id"] for r in results if r["status"] == "failed"]
    print(f"\nAPI calls this run: {stats['calls']}  ok {stats['ok']}  refused {stats['refused']}  error {stats['error']}")
    print(f"Estimated cost this run: ~${stats['ok'] * EST_COST_PER_IMAGE:.2f} (at ~${EST_COST_PER_IMAGE}/image)")
    if failed:
        print("FAILED:", failed)

"""Build scenes.json (visual BEATS -> SHOTS) from work/segments.json and an episode plan module.
Usage: python plan_beats.py <episode_dir> <plan_module.py>

The plan module defines:
  LOC   = {key: location description}
  MOOD  = {key: mood/lighting text}
  BEATS = [dict(to=<last shot number>, reason=..., chars=[...], loc=key, visual=..., camera=...,
                amb=<ambience key>, sens=None, safe=None, reuse=None | "beat_007" | "ep272:shot_091",
                transition="xfade" | "black" | "dissolve")]
  SHOTS = {n: (english, [(sfx_name, dhivehi_word_substring, gainDb)], {optional: hum, crop, motion})}
A beat covers the shots after the previous beat's `to` up to its own `to`.
"""
import importlib.util, json, os, shutil, sys

ep_dir, plan_path = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("plan", plan_path)
P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
n = os.path.basename(ep_dir.rstrip("/\\")).split("-")[-1]
series_dir = os.path.dirname(ep_dir.rstrip("/\\"))
segs = json.load(open(f"{ep_dir}/work/segments.json", encoding="utf-8"))
words = [w for blk in json.load(open(f"{ep_dir}/work/episode-{n}-captions.json", encoding="utf-8"))
         for w in blk["words"] if w["word"].strip()]
assert sorted(P.SHOTS) == list(range(1, len(segs) + 1)), "SHOTS must cover every segment"
assert P.BEATS[-1]["to"] == len(segs)

MOTIONS = ["slow push-in", "pan left", "slow pull-out", "pan right", "slow push-in", "pan up", "slow pull-out",
           "pan down", "static drift"]
CROPS = ["full", "tight", "full", "medium", "tight"]
os.makedirs(f"{ep_dir}/images", exist_ok=True)

beats, first, mi = [], 1, 0
for bi, b in enumerate(P.BEATS, 1):
    bid = f"beat_{bi:03d}"
    rng = range(first, b["to"] + 1); first = b["to"] + 1
    reuse = b.get("reuse")
    if reuse and reuse.startswith("ep"):          # image from an earlier episode of the series (no API call)
        ep, shot = reuse[2:].split(":")
        src = os.path.join(series_dir, f"episode-{ep}", "images", f"{shot}.png")
        dst = f"{ep_dir}/images/{bid}.png"
        if not os.path.exists(dst): shutil.copyfile(src, dst)
        image = f"images/{bid}.png"
    elif reuse:
        image = next(x["image"] for x in beats if x["id"] == reuse)
    else:
        image = f"images/{bid}.png"
    shots = []
    for k, si in enumerate(rng):
        seg = segs[si - 1]
        en, sfx, *opt = P.SHOTS[si]
        opt = opt[0] if opt else {}
        sfx_out = []
        for name, key, g in sfx:
            hit = next((w for w in words[seg["w0"]:seg["w1"] + 1] if key in w["word"]), None)
            assert hit, (seg["id"], key)
            sfx_out.append({"name": name, "atMs": hit["startMs"], "gainDb": g, "word": hit["word"]})
        crop = opt.get("crop") or (("medium" if reuse else "full") if len(rng) == 1 else
                                   CROPS[(k + (1 if reuse else 0)) % len(CROPS)])
        shots.append({"id": seg["id"], "startMs": seg["startMs"], "endMs": seg["endMs"],
                      "narration_dhivehi": seg["narration_dhivehi"], "narration_english": en,
                      "crop": crop, "motion": opt.get("motion") or MOTIONS[mi % len(MOTIONS)],
                      "sfx": sfx_out, "hum": bool(opt.get("hum"))})
        mi += 1
    beats.append({
        "id": bid, "startMs": shots[0]["startMs"], "endMs": shots[-1]["endMs"],
        "new_image_reason": b["reason"], "characters": b.get("chars", []),
        "location": P.LOC[b["loc"]], "location_key": b["loc"], "mood": P.MOOD[b["loc"]],
        "visual": b["visual"], "camera": b.get("camera", "medium shot, eye level"),
        "image": image, "reuse_of": reuse, "transition_in": b.get("transition", "xfade"),
        "sensitive": b.get("sens"), "safe_substitution": b.get("safe"),
        "ambience": b["amb"], "shots": shots, "prompt_attempts": [],
    })

old = f"{ep_dir}/scenes.json"
if os.path.exists(old):   # keep the logged prompt attempts of images already generated
    prev = {b["id"]: b for b in json.load(open(old, encoding="utf-8")).get("beats", [])}
    for b in beats:
        if b["id"] in prev and prev[b["id"]].get("prompt_attempts") and prev[b["id"]]["visual"] == b["visual"]:
            b["prompt_attempts"] = prev[b["id"]]["prompt_attempts"]; b["final_prompt"] = prev[b["id"]].get("final_prompt")
out = {"series": os.path.basename(series_dir), "episode": int(n), "beats": beats}
json.dump(out, open(f"{ep_dir}/scenes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
new = [b for b in beats if not b["reuse_of"]]
nshots = sum(len(b["shots"]) for b in beats)
dur = beats[-1]["endMs"] / 1000
print(f"{len(beats)} beats, {nshots} shots, {len(new)} new images, {len(beats) - len(new)} reused; "
      f"{dur / len(new):.1f} s audio per new image")
for b in beats:
    print(f'{b["id"]} {b["startMs"]/1000:7.1f}-{b["endMs"]/1000:7.1f} ({(b["endMs"]-b["startMs"])/1000:5.1f}s, '
          f'{len(b["shots"])} shots) {b["reuse_of"] or "NEW"}  {b["visual"][:70]}')

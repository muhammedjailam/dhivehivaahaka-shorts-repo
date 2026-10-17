"""Re-cut helper: map the NEW narration segments of an episode onto the OLD (v1) beats.
Aligns the new caption words with the v1 caption words (difflib on punctuation-stripped words), then writes
  <ep>/work/v1_map.txt   every new segment -> old beat(s) covering those words (share of words) + old English of the
                         overlapping old shots
  <ep>/work/v1_beats.txt every old beat (image file, chars, loc, amb, transition, visual, camera, sens/safe, focus)
Usage: python mkmap_v1.py <series_dir> <episode_number>
Expects <series>/v1/episode-<N>/ (scenes.json + work/episode-<N>-captions.json) and <series>/episode-<N>/work/.
"""
import difflib, json, os, re, sys
from collections import Counter

series_dir, n = sys.argv[1], sys.argv[2]
old_ep = os.path.join(series_dir, "v1", f"episode-{n}")
new_ep = os.path.join(series_dir, f"episode-{n}")


def words(path):
    return [w for blk in json.load(open(path, encoding="utf-8")) for w in blk["words"] if w["word"].strip()]


def norm(w):
    return re.sub(r"[\s.,،؟?!\"'“”…:;()\-]", "", w)


ow = words(os.path.join(old_ep, "work", f"episode-{n}-captions.json"))
nw = words(os.path.join(new_ep, "work", f"episode-{n}-captions.json"))
beats = json.load(open(os.path.join(old_ep, "scenes.json"), encoding="utf-8"))["beats"]
segs = json.load(open(os.path.join(new_ep, "work", "segments.json"), encoding="utf-8"))

# old word -> (beat id, shot id)
shots = [(b["id"], s) for b in beats for s in b["shots"]]
def locate(t):
    for bid, s in shots:
        if s["startMs"] <= t < s["endMs"]:
            return bid, s
    return shots[-1][0], shots[-1][1]
oloc = [locate(w["startMs"]) for w in ow]

sm = difflib.SequenceMatcher(None, [norm(w["word"]) for w in ow], [norm(w["word"]) for w in nw], autojunk=False)
m = [None] * len(nw)
for a, b, size in sm.get_matching_blocks():
    for k in range(size):
        m[b + k] = a + k
matched = sum(x is not None for x in m)
# unmatched new words: take the previous matched old word (or the next one at the start)
last = None
for i in range(len(m)):
    if m[i] is None: m[i] = last
    else: last = m[i]
nxt = None
for i in range(len(m) - 1, -1, -1):
    if m[i] is None: m[i] = nxt
    else: nxt = m[i]

out = [f"# Episode {n}: NEW segments (work/segments.json) mapped onto the OLD v1 plan ({os.path.relpath(old_ep, os.path.dirname(series_dir))}/scenes.json).",
       f"# Word alignment: {matched}/{len(nw)} new words matched an old word ({100 * matched / max(1, len(nw)):.0f}%), old words {len(ow)}.",
       "# For each new segment: the old beat(s) whose image covered those words (share of words), and the old English",
       "# translation of the overlapping old shots (the new narration is a re-recording: same story, possibly different",
       "# wording — re-check the translation against the new Dhivehi).", ""]
for k, s in enumerate(segs, 1):
    idx = [m[i] for i in range(s["w0"], s["w1"] + 1) if m[i] is not None]
    cnt = Counter(oloc[i][0] for i in idx)
    tot = sum(cnt.values()) or 1
    ob = "  ".join(f"{b} {100 * c // tot}%" for b, c in sorted(cnt.items()))
    sids, ens = [], []
    for i in idx:
        sh = oloc[i][1]
        if sh["id"] not in sids:
            sids.append(sh["id"]); ens.append(sh.get("narration_english") or "")
    out.append(f"{k:3d} {s['id']}  {s['startMs'] / 1000:6.1f}-{s['endMs'] / 1000:7.1f}  OLD BEATS: {ob}   old shots: "
               + ", ".join(x.replace("shot_", "") for x in sids))
    out.append(f"    DV: {s['narration_dhivehi']}")
    out.append(f"    EN(old): {' '.join(ens)}")
open(os.path.join(new_ep, "work", "v1_map.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")

bl = [f"# Old v1 beats of episode {n}: image file {os.path.relpath(old_ep, os.path.dirname(series_dir))}/<image>; 'reuse_of' = the old beat reused an earlier old image", ""]
for b in beats:
    f = b.get("focus") or {}
    bl.append(f"{b['id']} image={b['image']} reuse_of={b.get('reuse_of')} chars={b['characters']} loc={b.get('location_key')} "
              f"amb={b['ambience']} trans={b.get('transition_in')} speaker={b.get('speaker')} "
              f"{b['startMs'] / 1000:.1f}-{b['endMs'] / 1000:.1f}s")
    bl.append(f"    reason: {b.get('new_image_reason')}")
    bl.append(f"    visual: {b['visual']}")
    bl.append(f"    camera: {b['camera']}")
    if b.get("sensitive"): bl.append(f"    sens: {b['sensitive']} / safe: {b.get('safe_substitution')}")
    if f: bl.append(f"    face focus (auto): x {f.get('x_pct')}%, y {f.get('y_pct')}%")
    shs = [f"{s['id'].replace('shot_', '')}:{s.get('crop')}" + (f"/spk={s['speaker']}" if s.get('speaker') else "") for s in b["shots"]]
    bl.append(f"    old shots: {' '.join(shs)}")
open(os.path.join(new_ep, "work", "v1_beats.txt"), "w", encoding="utf-8").write("\n".join(bl) + "\n")
print(f"episode {n}: {matched}/{len(nw)} new words matched ({100 * matched / max(1, len(nw)):.0f}%), {len(segs)} new segments, {len(beats)} old beats")

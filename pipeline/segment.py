"""Segment narration into shots using word timings. Writes segments.json (draft)."""
import json, sys, subprocess
ep_dir = sys.argv[1]; n = sys.argv[2]
words = [w for blk in json.load(open(f"{ep_dir}/work/episode-{n}-captions.json", encoding="utf-8")) for w in blk["words"] if w["word"].strip()]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "csv=p=0", f"{ep_dir}/work/episode-{n}.wav"]).decode())
END = int(round(dur * 1000))

def is_end(i):
    t = words[i]["word"].rstrip('"\'”“')
    return t.endswith((".", "؟", "?", "!")) or (i + 1 < len(words) and words[i + 1]["startMs"] - words[i]["endMs"] > 600)

def is_soft(i):  # comma / long-ish pause for splitting overlong sentences
    t = words[i]["word"].rstrip('"\'”“')
    return t.endswith(("،", ",")) or (i + 1 < len(words) and words[i + 1]["startMs"] - words[i]["endMs"] > 350)

# sentence units [i0, i1]
units, s = [], 0
for i in range(len(words)):
    if is_end(i) or i == len(words) - 1:
        units.append([s, i]); s = i + 1

def udur(a, b): return words[b]["endMs"] - words[a]["startMs"]

# split units longer than 13 s at soft points
split = []
for a, b in units:
    while udur(a, b) > 13000:
        best = None
        for k in range(a, b):
            if is_soft(k) and 4000 <= udur(a, k) <= 11000 and udur(k + 1, b) >= 3000:
                score = abs(udur(a, k) - 8000)
                if best is None or score < best[0]: best = (score, k)
        if not best:
            # fallback: split at largest gap near middle
            ks = [k for k in range(a, b) if 4000 <= udur(a, k) <= 11000]
            if not ks: break
            k = max(ks, key=lambda k: words[k + 1]["startMs"] - words[k]["endMs"])
        else:
            k = best[1]
        split.append([a, k]); a = k + 1
    split.append([a, b])
units = split

# greedy grouping into shots of 6-10 s
shots, cur = [], None
for a, b in units:
    if cur is None: cur = [a, b]; continue
    d_cur = udur(*cur); d_new = udur(cur[0], b)
    if d_cur >= 6000 and d_new > 10000:
        shots.append(cur); cur = [a, b]
    elif d_new > 15000 and d_cur >= 3000:
        shots.append(cur); cur = [a, b]
    else:
        cur[1] = b
shots.append(cur)
# merge tiny tail
if len(shots) > 1 and udur(*shots[-1]) < 3000: shots[-2][1] = shots[-1][1]; shots.pop()

out = []
for i, (a, b) in enumerate(shots):
    start = 0 if i == 0 else out[-1]["endMs"]
    if i == len(shots) - 1: end = END
    else: end = int((words[b]["endMs"] + words[shots[i + 1][0]]["startMs"]) / 2)
    out.append({"id": f"shot_{i+1:03d}", "startMs": start, "endMs": end,
                "w0": a, "w1": b,
                "narration_dhivehi": " ".join(w["word"] for w in words[a:b + 1])})
json.dump(out, open(f"{ep_dir}/work/segments.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ds = [(s["endMs"] - s["startMs"]) / 1000 for s in out]
print(len(out), "shots; min %.1f max %.1f mean %.1f; end %d" % (min(ds), max(ds), sum(ds) / len(ds), END))
for s in out:
    print(f'{s["id"]} {s["startMs"]/1000:7.2f}-{s["endMs"]/1000:7.2f} ({(s["endMs"]-s["startMs"])/1000:4.1f}) {s["narration_dhivehi"]}')

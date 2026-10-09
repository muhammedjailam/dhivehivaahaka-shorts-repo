"""Write <episode_dir>/characters.json: the series cards of every character on screen this episode.
Usage: python episode_characters.py <episode_dir>
"""
import json, os, sys

ep_dir = sys.argv[1].rstrip("/\\")
series_dir = os.path.dirname(ep_dir)
n = int(os.path.basename(ep_dir).split("-")[-1])
beats = json.load(open(os.path.join(ep_dir, "scenes.json"), encoding="utf-8"))["beats"]
used = {}
for b in beats:
    for cid in b["characters"]:
        used.setdefault(cid, []).append(b["id"])
out = []
for cid in sorted(used):
    card = json.load(open(os.path.join(series_dir, "characters", cid, "card.json"), encoding="utf-8"))
    card["reference"] = f"../characters/{cid}/reference.png"
    card["status_this_episode"] = "new this episode" if card.get("first_seen_episode") == n else "reused from series"
    card["beats"] = used[cid]
    out.append(card)
json.dump(out, open(os.path.join(ep_dir, "characters.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(out), "characters:", ", ".join(f"{c['id']} ({c['status_this_episode']})" for c in out))

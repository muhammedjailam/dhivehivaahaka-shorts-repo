"""Contact sheet of an episode's beat images (new + reused) with beat ids. Usage: python beats_sheet.py <episode_dir> [cols]"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
ep = sys.argv[1]; cols = int(sys.argv[2]) if len(sys.argv) > 2 else 8
beats = json.load(open(os.path.join(ep, "scenes.json"), encoding="utf-8"))["beats"]
seen, items = set(), []
for b in beats:
    if b["image"] in seen: continue
    seen.add(b["image"]); items.append((b["id"], b["image"], b["reuse_of"]))
w, h = 256, 384
sheet = Image.new("RGB", (cols * w, -(-len(items) // cols) * h), "black")
f = ImageFont.truetype("arial.ttf", 22)
for i, (bid, img, r) in enumerate(items):
    im = Image.open(os.path.join(ep, img)).convert("RGB").resize((w, h))
    d = ImageDraw.Draw(im); d.rectangle((0, 0, w, 28), fill="black")
    d.text((4, 2), bid[-3:] + (f" <{r}" if r else ""), fill="yellow", font=f)
    sheet.paste(im, ((i % cols) * w, (i // cols) * h))
sheet.save(os.path.join(ep, "work", "beats_sheet.jpg"), quality=85)
print(len(items), "images")

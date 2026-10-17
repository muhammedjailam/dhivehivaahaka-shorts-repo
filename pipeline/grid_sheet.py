"""Grid sheets for picking per-shot focus points (spec 5.4): each image gets 10% grid lines labelled in % of the image,
so a speaker's face position can be read off as [x%, y%]. Four images per sheet.
Usage: python grid_sheet.py <images_dir> <out_prefix> [beat_id ...]     (e.g. beat_003 beat_007; default: all)
Writes <out_prefix>_01.jpg, <out_prefix>_02.jpg, ...
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

src, prefix = sys.argv[1], sys.argv[2]
ids = sys.argv[3:]
files = sorted(f for f in os.listdir(src) if f.endswith(".png") and (not ids or f[:-4] in ids))
w, h = 512, 768
font = ImageFont.truetype("arial.ttf", 18); big = ImageFont.truetype("arial.ttf", 26)
for k in range(0, len(files), 4):
    sheet = Image.new("RGB", (4 * w, h), "black")
    for j, f in enumerate(files[k:k + 4]):
        im = Image.open(os.path.join(src, f)).convert("RGB").resize((w, h))
        d = ImageDraw.Draw(im)
        for p in range(10, 100, 10):
            x, y = w * p // 100, h * p // 100
            d.line((x, 0, x, h), fill=(255, 255, 0), width=1)
            d.line((0, y, w, y), fill=(0, 255, 255), width=1)
            d.text((x + 2, 2), str(p), fill=(255, 255, 0), font=font)
            d.text((2, y + 2), str(p), fill=(0, 255, 255), font=font)
        d.rectangle((0, h - 34, w, h), fill="black"); d.text((6, h - 32), f[:-4], fill="white", font=big)
        sheet.paste(im, (j * w, 0))
    out = f"{prefix}_{k // 4 + 1:02d}.jpg"
    sheet.save(out, quality=85)
    print(out)

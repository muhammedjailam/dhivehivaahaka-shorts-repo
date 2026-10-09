"""QC for a finished episode: spec probe, loudness, one-frame-per-shot contact sheet, caption sample sheet.
Usage: python qc.py <episode_dir> <series> <episode_number>
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw

ep_dir, series, n = sys.argv[1], sys.argv[2], sys.argv[3]
mp4 = os.path.join(ep_dir, f"{series}_Episode{n}_TikTok.mp4")
Q = os.path.join(ep_dir, "work", "qc"); os.makedirs(Q, exist_ok=True)
pr = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", mp4]))
v = next(s for s in pr["streams"] if s["codec_type"] == "video"); a = next(s for s in pr["streams"] if s["codec_type"] == "audio")
nar = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     os.path.join(ep_dir, "work", f"episode-{n}.wav")]).decode())
print(f"video {v['codec_name']} {v.get('profile')} {v['width']}x{v['height']} {v['r_frame_rate']} {v['pix_fmt']}")
print(f"audio {a['codec_name']} {a['sample_rate']} Hz ch={a['channels']} {int(a.get('bit_rate', 0)) // 1000} kbps")
print(f"duration {float(pr['format']['duration']):.3f}s vs narration {nar:.3f}s  size {int(pr['format']['size']) / 1e6:.0f} MB")
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", mp4, "-map", "0:a", "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True)
summ = r.stderr[r.stderr.rfind("Summary:"):]
print(" ".join(l.strip() for l in summ.splitlines() if l.strip().startswith(("I:", "Peak:"))))

beats = json.load(open(os.path.join(ep_dir, "scenes.json"), encoding="utf-8"))["beats"]
shots = [(b["id"], s) for b in beats for s in b["shots"]]


def grab(t, path, w=270):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-vf", f"scale={w}:-1", path], check=True)
    return Image.open(path).convert("RGB")


# one frame per shot
cols = 10; w, h = 216, 384
sheet = Image.new("RGB", (cols * w, ((len(shots) + cols - 1) // cols) * h), "black")
for i, (bid, s) in enumerate(shots):
    im = grab((s["startMs"] + s["endMs"]) / 2000, os.path.join(Q, "f.png"), w)
    ImageDraw.Draw(im).text((4, 4), f"{bid[-3:]}/{s['id'][-3:]} {s['crop']}", fill="yellow")
    sheet.paste(im, ((i % cols) * w, (i // cols) * h))
sheet.save(os.path.join(ep_dir, "contact_sheet.jpg"), quality=85)

# caption samples: first page, last page and 8 spread across, full-size bottom half crops
words = [x for blk in json.load(open(os.path.join(ep_dir, "work", f"episode-{n}-captions.json"), encoding="utf-8"))
         for x in blk["words"] if x["word"].strip()]
idx = [3] + [int(len(words) * k / 9) for k in range(1, 9)] + [len(words) - 2]
tiles = []
for i in idx:
    wd = words[i]; t = (wd["startMs"] + min(wd["endMs"], wd["startMs"] + 250)) / 2000
    im = grab(t, os.path.join(Q, "c.png"), 1080).crop((0, 1150, 1080, 1800)).resize((540, 325))
    ImageDraw.Draw(im).text((6, 6), f"{t:.2f}s idx {i}", fill="yellow")
    tiles.append((im, i))
cs = Image.new("RGB", (1080, 325 * 5), "black")
for k, (im, i) in enumerate(tiles):
    cs.paste(im, ((k % 2) * 540, (k // 2) * 325))
cs.save(os.path.join(ep_dir, "contact_sheet_captions.jpg"), quality=88)
with open(os.path.join(Q, "caption_samples.txt"), "w", encoding="utf-8") as f:
    for im, i in tiles:
        f.write(f"{i}\t{words[i]['startMs']}\t{words[i]['word']}\n")
print("contact sheets written")

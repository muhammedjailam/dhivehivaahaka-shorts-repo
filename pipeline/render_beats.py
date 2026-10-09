"""Render the vertical video from a BEAT/SHOT plan (scenes.json with "beats").
One segment per beat (resumable); inside a beat each shot is a crop + slow Ken Burns move on the same image,
changed with a clean cut at the sentence boundary; beats are joined by a crossfade / dissolve / dip to black.
Captions (word highlight) and the per-beat logo are composited on top; fade from/to black 1 s.
Usage: python render_beats.py <episode_dir> <series> <episode_number> [--force beat_id ...]
"""
import json, math, os, subprocess, sys
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageFilter

W, H, FPS = 1080, 1920, 30
XF = {"xfade": 0.6, "dissolve": 1.0, "black": 1.0}
COVER_SEC = 2.5
LOGO_W, LOGO_BOTTOM, LOGO_OPACITY = 360, 140, 0.88
CRF = 19
CROP_ZOOM = {"full": 1.0, "medium": 1.18, "tight": 1.42}

ep_dir, series, n = sys.argv[1], sys.argv[2], sys.argv[3]
force = set(a for a in sys.argv[sys.argv.index("--force") + 1:] if not a.startswith("--")) if "--force" in sys.argv else set()
SEG = os.path.join(ep_dir, "work", "segments_beats"); os.makedirs(SEG, exist_ok=True)
SP = os.path.join(ep_dir, "scenes.json")
doc = json.load(open(SP, encoding="utf-8")); beats = doc["beats"]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     os.path.join(ep_dir, "audio", "final_mix.wav")]).decode())
B = [b["startMs"] / 1000 for b in beats] + [dur]
XFI = [0] + [XF[beats[k]["transition_in"]] for k in range(1, len(beats))]   # transition length INTO beat k
LOGO_DIR = os.path.join(ep_dir, "work", "logo")
PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_cap = None


def captions():
    global _cap
    if _cap is None:
        from captions import Captions
        _cap = Captions(os.path.join(ep_dir, "work", f"episode-{n}-captions.json"), os.path.join(PROJECT, "MVWaheed.otf"), dur)
    return _cap


# ---------------------------------------------------------------- image sources, focus points, crops
def load_src(path):
    """Original image upscaled 2x (lanczos) for clean sub-pixel sampling; returns (img, cover scale)."""
    im = Image.open(os.path.join(ep_dir, path)).convert("RGB")
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    return im, max(W / im.width, H / im.height)


def focus_point(im):
    """Centre of the most prominent face (OpenCV Haar), else upper-centre. In source pixel coords."""
    import cv2
    g = cv2.cvtColor(np.asarray(im.resize((im.width // 4, im.height // 4))), cv2.COLOR_RGB2GRAY)
    cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cas.detectMultiScale(g, 1.1, 5, minSize=(24, 24))
    if len(faces):
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
        return (x + w / 2) * 4, (y + h * 0.7) * 4, True   # a little below the eyes keeps chin + hijab
    return im.width / 2, im.height * 0.40, False


def motion_params(motion, u):
    """(zoom multiplier, dx, dy) in output pixels for progress u in [0,1]."""
    if motion == "slow push-in":  return 1.0 + 0.08 * u, 0, 0
    if motion == "slow pull-out": return 1.08 - 0.08 * u, 0, 0
    if motion == "pan left":      return 1.05, 50 - 100 * u, 0
    if motion == "pan right":     return 1.05, -50 + 100 * u, 0
    if motion == "pan up":        return 1.06, 0, 50 - 100 * u
    if motion == "pan down":      return 1.06, 0, -50 + 100 * u
    return 1.02 + 0.03 * u, -15 + 30 * u, 0


def frame(src, s0, crop, focus, motion, u):
    """Render one 1080x1920 frame: crop zoom z0 centred on `focus` (or image centre for full), plus motion."""
    zm, dx, dy = motion_params(motion, u)
    z0 = CROP_ZOOM[crop]; s = s0 * z0 * zm
    if crop == "full": cx, cy = src.width / 2, src.height / 2
    else: cx, cy = focus
    cx += dx / s; cy += dy / s
    hw, hh = W / 2 / s, H / 2 / s                       # half window in source pixels
    cx = min(max(cx, hw), src.width - hw); cy = min(max(cy, hh), src.height - hh)
    a = 1 / s; c = cx - (W / 2) / s; f = cy - (H / 2) / s
    return np.asarray(src.transform((W, H), Image.AFFINE, (a, 0, c, 0, a, f), resample=Image.BICUBIC), dtype=np.float32)


def crop_rect(src, s0, crop, focus):
    """Crop window (mid-motion ignored) as x,y,w,h in % of the image, for scenes.json."""
    s = s0 * CROP_ZOOM[crop]
    cx, cy = (src.width / 2, src.height / 2) if crop == "full" else focus
    hw, hh = W / 2 / s, H / 2 / s
    cx = min(max(cx, hw), src.width - hw); cy = min(max(cy, hh), src.height - hh)
    return [round(100 * (cx - hw) / src.width, 1), round(100 * (cy - hh) / src.height, 1),
            round(100 * 2 * hw / src.width, 1), round(100 * 2 * hh / src.height, 1)]


# ---------------------------------------------------------------- logo
LX = (W - LOGO_W) // 2


def load_logo(color):
    im = Image.open(os.path.join(LOGO_DIR, f"logo_{color}.png")).convert("RGBA")
    a = np.asarray(im, dtype=np.float32) / 255
    rgb, alpha = a[..., :3], a[..., 3:] * LOGO_OPACITY
    shadow = np.asarray(Image.fromarray((a[..., 3] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)),
                        dtype=np.float32)[..., None] / 255
    return rgb * 255, alpha, shadow


def region_lum(fr):
    lh = 112; y0 = H - LOGO_BOTTOM - lh
    reg = fr[y0:y0 + lh, LX:LX + LOGO_W] / 255
    return float((0.2126 * reg[..., 0] + 0.7152 * reg[..., 1] + 0.0722 * reg[..., 2]).mean())


def logo_from_lum(lum):
    color = "w" if lum < 0.55 else "b"
    weak = (0.40 < lum < 0.55) if color == "w" else (lum < 0.70)
    return color, weak


def apply_logo(fr, logo, weak):
    rgb, alpha, shadow = logo
    lh = rgb.shape[0]; y0 = H - LOGO_BOTTOM - lh
    reg = fr[y0:y0 + lh, LX:LX + LOGO_W]
    if weak:
        halo = 0 if rgb.mean() > 128 else 255
        reg[:] = reg * (1 - shadow * 0.35) + halo * shadow * 0.35
    reg[:] = reg * (1 - alpha) + rgb * alpha


def smooth(x): return x * x * (3 - 2 * x)


# ---------------------------------------------------------------- per-beat preparation (cached in-process)
_prep = {}


def prep(k):
    if k in _prep: return _prep[k]
    b = beats[k]
    src, s0 = load_src(b["image"])
    fx, fy, found = focus_point(src)
    lums = []
    for sh in b["shots"]:
        lums.append(region_lum(frame(src, s0, sh["crop"], (fx, fy), sh["motion"], 0.5)))
    lum = float(np.mean(lums)); color, weak = logo_from_lum(lum)
    shots = []
    for j, sh in enumerate(b["shots"]):
        a = sh["startMs"] / 1000 - (XFI[k] / 2 if j == 0 else 0)
        e = sh["endMs"] / 1000 + (XFI[k + 1] / 2 if j == len(b["shots"]) - 1 and k + 1 < len(beats) else 0)
        shots.append((a, e, sh["crop"], sh["motion"]))
    _prep[k] = dict(src=src, s0=s0, focus=(fx, fy), face=found, shots=shots,
                    logo=(load_logo(color), weak), color=color, weak=weak, lum=lum)
    return _prep[k]


def render_beat(k, t):
    p = prep(k)
    sh = next((s for s in p["shots"] if t < s[1]), p["shots"][-1])
    if t < p["shots"][0][0]: sh = p["shots"][0]
    a, e, crop, motion = sh
    u = min(1, max(0, (t - a) / (e - a)))
    fr = frame(p["src"], p["s0"], crop, p["focus"], motion, u)
    apply_logo(fr, *p["logo"])
    return fr


def T(k):
    return 0.0 if k == 0 else (dur if k == len(beats) else B[k] + XFI[k] / 2)


def render_segment(i):
    out = os.path.join(SEG, f"seg_{i:03d}.mp4")
    bid = beats[i]["id"]
    if os.path.exists(out) and bid not in force:
        return out
    f0, f1 = round(T(i) * FPS), round(T(i + 1) * FPS)
    cover = None
    if i == 0:
        im = Image.open(os.path.join(ep_dir, "work", f"episode-{n}-cover.png")).convert("RGB")
        sc = max(W / im.width, H / im.height)
        bg = im.resize((math.ceil(im.width * sc), math.ceil(im.height * sc)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(40))
        bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
        bg = Image.blend(bg, Image.new("RGB", (W, H), (0, 0, 0)), 0.35)
        fg = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
        bg.paste(fg, (0, (H - fg.height) // 2))
        c, wk = logo_from_lum(region_lum(np.asarray(bg, np.float32)))
        cover = (bg, load_logo(c), wk)
    from captions import composite
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                          "-crf", str(CRF), "-preset", "medium", "-threads", "3", "-r", str(FPS), out + ".tmp.mp4"],
                         stdin=subprocess.PIPE)
    for fi in range(f0, f1):
        t = fi / FPS
        fr = render_beat(i, t)
        if i + 1 < len(beats):
            x = XFI[i + 1]; ts = B[i + 1] - x / 2
            if t >= ts:
                al = min(1, (t - ts) / x); kind = beats[i + 1]["transition_in"]
                nxt = render_beat(i + 1, t)
                if kind == "black":
                    fr = fr * (1 - smooth(min(1, al * 2))) if al < 0.5 else nxt * smooth(min(1, (al - 0.5) * 2))
                else:
                    w_ = smooth(al) if kind == "xfade" else al
                    fr = fr * (1 - w_) + nxt * w_
        if cover is not None and t < COVER_SEC + XF["xfade"]:
            cim, clogo, cweak = cover
            cf = frame(cim, 1.0, "full", None, "slow push-in", min(1, t / (COVER_SEC + XF["xfade"])) * 0.3)
            apply_logo(cf, clogo, cweak)
            al = 0 if t < COVER_SEC else smooth((t - COVER_SEC) / XF["xfade"])
            fr = cf * (1 - al) + fr * al
        ck = 1.0 if t >= COVER_SEC + XF["xfade"] else max(0.0, (t - COVER_SEC) / XF["xfade"])
        composite(fr, captions(), t, smooth(ck))
        g = min(1, t / 1.0, (dur - t) / 1.0)
        if g < 1: fr = fr * max(0, g)
        p.stdin.write(np.clip(fr + 0.5, 0, 255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise RuntimeError(f"ffmpeg failed for segment {i}")
    os.replace(out + ".tmp.mp4", out)
    pr = prep(i)
    print(f"[seg] {bid} frames {f0}-{f1} logo={'white' if pr['color'] == 'w' else 'black'} face={pr['face']}", flush=True)
    return out


def report():
    rep = []
    for k, b in enumerate(beats):
        pr = prep(k)
        rep.append(dict(logo={"color": "white" if pr["color"] == "w" else "black", "bg_luminance": round(pr["lum"], 3),
                              "halo": pr["weak"]},
                        focus={"x_pct": round(100 * pr["focus"][0] / pr["src"].width, 1),
                               "y_pct": round(100 * pr["focus"][1] / pr["src"].height, 1), "face_detected": pr["face"]},
                        crops=[crop_rect(pr["src"], pr["s0"], sh["crop"], pr["focus"]) for sh in b["shots"]]))
    return rep


if __name__ == "__main__":
    only = [int(x) for x in os.environ.get("ONLY", "").split(",") if x]
    if only:
        with Pool(len(only)) as pool: pool.map(render_segment, only)
        sys.exit(0)
    if "--report-only" not in sys.argv:
        workers = int(os.environ.get("RENDER_WORKERS", "4"))
        with Pool(workers) as pool:
            segs = pool.map(render_segment, range(len(beats)), chunksize=1)
        lst = os.path.join(SEG, "list.txt")
        open(lst, "w").write("".join(f"file '{os.path.basename(s)}'\n" for s in segs))
        video_only = os.path.join(ep_dir, "work", "video_only.mp4")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video_only], check=True)
        final = os.path.join(ep_dir, f"{series}_Episode{n}_TikTok.mp4")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video_only, "-i", os.path.join(ep_dir, "audio", "final_mix.wav"),
                        "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "volume=-0.3dB", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", final], check=True)
        print("done:", final)
    rep = report()
    doc = json.load(open(SP, encoding="utf-8"))
    for b, r in zip(doc["beats"], rep):
        b["logo"] = r["logo"]; b["focus"] = r["focus"]
        for sh, c in zip(b["shots"], r["crops"]): sh["crop_rect_pct"] = c
    json.dump(doc, open(SP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

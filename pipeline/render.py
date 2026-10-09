"""Render the vertical video: Ken Burns per shot (sub-pixel affine, no jitter), 0.5 s crossfades,
cover intro, per-shot logo colour, fade from/to black. Segments are rendered individually (resumable)
and concatenated, then muxed with audio/final_mix.wav.
Usage: python render.py <episode_dir> <series> <episode_number> [--force shot_id ...]
"""
import json, math, os, subprocess, sys
from multiprocessing import Pool
import numpy as np
from PIL import Image, ImageFilter

W, H, FPS = 1080, 1920, 30
XF = 0.5            # crossfade seconds
COVER_SEC = 2.5     # cover hold before crossfading into shot 1
LOGO_W, LOGO_BOTTOM = 360, 140
LOGO_OPACITY = 0.88
CRF = 19

ep_dir, series, n = sys.argv[1], sys.argv[2], sys.argv[3]
CAPTIONS = "--captions" in sys.argv
force = set(a for a in sys.argv[sys.argv.index("--force") + 1:] if not a.startswith("--")) if "--force" in sys.argv else set()
SEG = os.path.join(ep_dir, "work", "segments_video_captions" if CAPTIONS else "segments_video"); os.makedirs(SEG, exist_ok=True)
scenes = json.load(open(os.path.join(ep_dir, "scenes.json"), encoding="utf-8"))
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     os.path.join(ep_dir, "audio", "final_mix.wav")]).decode())
TOTAL_F = round(dur * FPS)
B = [s["startMs"] / 1000 for s in scenes] + [dur]       # shot boundaries
LOGO_DIR = os.path.join(ep_dir, "work", "logo")
PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_cap = None


def captions():
    """Word-highlighted Thaana captions (lazy, per worker process)."""
    global _cap
    if _cap is None:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from captions import Captions
        _cap = Captions(os.path.join(ep_dir, "work", f"episode-{n}-captions.json"), os.path.join(PROJECT, "MVWaheed.otf"), dur)
    return _cap


def cover_fit(im):
    """Scale-to-cover 1080x1920 at zoom 1 (lanczos)."""
    sc = max(W / im.width, H / im.height)
    return im.resize((math.ceil(im.width * sc), math.ceil(im.height * sc)), Image.LANCZOS)


def cover_with_blur(im):
    """Fit the whole cover into 9:16 over a blurred fill."""
    bg = cover_fit(im).filter(ImageFilter.GaussianBlur(40))
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = Image.blend(bg, Image.new("RGB", (W, H), (0, 0, 0)), 0.35)
    fg = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    bg.paste(fg, (0, (H - fg.height) // 2))
    return bg


def motion_params(motion, u):
    """Return (zoom, dx, dy) in output pixels for progress u in [0,1]."""
    if motion == "slow push-in":  return 1.0 + 0.08 * u, 0, 0
    if motion == "slow pull-out": return 1.08 - 0.08 * u, 0, 0
    if motion == "pan left":      return 1.05, 60 - 120 * u, 0
    if motion == "pan right":     return 1.05, -60 + 120 * u, 0
    if motion == "pan up":        return 1.07, 0, 55 - 110 * u
    if motion == "pan down":      return 1.07, 0, -55 + 110 * u
    return 1.02 + 0.03 * u, -15 + 30 * u, 0   # static drift


def frame(src, motion, u):
    z, dx, dy = motion_params(motion, u)
    cx, cy = src.width / 2 + dx, src.height / 2 + dy
    # output pixel (x,y) -> source (cx + (x - W/2)/z, cy + (y - H/2)/z)
    a = 1 / z; e = 1 / z
    c = cx - (W / 2) / z; f = cy - (H / 2) / z
    return np.asarray(src.transform((W, H), Image.AFFINE, (a, 0, c, 0, e, f), resample=Image.BICUBIC), dtype=np.float32)


def load_logo(color):
    im = Image.open(os.path.join(LOGO_DIR, f"logo_{color}.png")).convert("RGBA")
    a = np.asarray(im, dtype=np.float32) / 255
    rgb, alpha = a[..., :3], a[..., 3:] * LOGO_OPACITY
    shadow = np.asarray(Image.fromarray((a[..., 3] * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)),
                        dtype=np.float32)[..., None] / 255
    return rgb * 255, alpha, shadow


LX = (W - LOGO_W) // 2


def logo_choice(img_rgb):
    """Average luminance behind the logo -> 'w' or 'b', plus whether to add shadow/glow."""
    lh = 112; y0 = H - LOGO_BOTTOM - lh
    reg = img_rgb[y0:y0 + lh, LX:LX + LOGO_W] / 255
    lum = float((0.2126 * reg[..., 0] + 0.7152 * reg[..., 1] + 0.0722 * reg[..., 2]).mean())
    color = "w" if lum < 0.55 else "b"
    weak = (0.40 < lum < 0.55) if color == "w" else (lum < 0.70)
    return color, weak, lum


def apply_logo(fr, logo, weak):
    rgb, alpha, shadow = logo
    lh = rgb.shape[0]; y0 = H - LOGO_BOTTOM - lh
    reg = fr[y0:y0 + lh, LX:LX + LOGO_W]
    if weak:  # subtle shadow (white logo) or glow (black logo)
        halo = 0 if rgb.mean() > 128 else 255
        reg[:] = reg * (1 - shadow * 0.35) + halo * shadow * 0.35
    reg[:] = reg * (1 - alpha) + rgb * alpha


def smooth(x): return x * x * (3 - 2 * x)


def seg_range(i):
    """Segment i covers [T_i, T_{i+1}) and contains the crossfade to shot i+1 at its end."""
    T = lambda k: 0.0 if k == 0 else (dur if k == len(scenes) else B[k] + XF / 2)
    return round(T(i) * FPS), round(T(i + 1) * FPS)


def render_segment(i):
    out = os.path.join(SEG, f"seg_{i:03d}.mp4")
    sid = scenes[i]["id"]
    if os.path.exists(out) and sid not in force:
        return out
    f0, f1 = seg_range(i)
    srcs, logos = {}, {}

    def shot(k):
        if k not in srcs:
            s = scenes[k]
            im = Image.open(os.path.join(ep_dir, s["image"])).convert("RGB")
            src = cover_fit(im)
            base = np.asarray(src.crop(((src.width - W) // 2, (src.height - H) // 2,
                                        (src.width - W) // 2 + W, (src.height - H) // 2 + H)), dtype=np.float32)
            color, weak, lum = logo_choice(base)
            srcs[k] = (src, s["motion"], B[k] - XF / 2, B[k + 1] + XF / 2)
            logos[k] = (load_logo(color), weak)
        return srcs[k]

    def render_shot(k, t):
        src, motion, a, b = shot(k)
        u = min(1, max(0, (t - a) / (b - a)))
        fr = frame(src, motion, u)
        lg, weak = logos[k]
        apply_logo(fr, lg, weak)
        return fr

    cover = None
    if i == 0:
        cim = cover_with_blur(Image.open(os.path.join(ep_dir, "work", f"episode-{n}-cover.png")).convert("RGB"))
        cbase = np.asarray(cim, dtype=np.float32)
        ccol, cweak, _ = logo_choice(cbase)
        cover = (cim, load_logo(ccol), cweak)

    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                          "-crf", str(CRF), "-preset", "medium", "-threads", "3", "-r", str(FPS), out + ".tmp.mp4"],
                         stdin=subprocess.PIPE)
    for fi in range(f0, f1):
        t = fi / FPS
        fr = render_shot(i, t)
        # crossfade into next shot at the end of this segment
        if i + 1 < len(scenes) and t >= B[i + 1] - XF / 2:
            al = smooth(min(1, (t - (B[i + 1] - XF / 2)) / XF))
            fr = fr * (1 - al) + render_shot(i + 1, t) * al
        # cover intro
        if cover is not None and t < COVER_SEC + XF:
            cim, clogo, cweak = cover
            cf = frame(cim, "slow push-in", min(1, t / (COVER_SEC + XF)) * 0.3)
            apply_logo(cf, clogo, cweak)
            al = 0 if t < COVER_SEC else smooth((t - COVER_SEC) / XF)
            fr = cf * (1 - al) + fr * al
        if CAPTIONS:
            from captions import composite
            ck = 1.0 if t >= COVER_SEC + XF else max(0.0, (t - COVER_SEC) / XF)  # not over the cover title
            composite(fr, captions(), t, smooth(ck))
        # fade from / to black (1 s)
        g = min(1, t / 1.0, (dur - t) / 1.0)
        if g < 1: fr = fr * max(0, g)
        p.stdin.write(np.clip(fr + 0.5, 0, 255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise RuntimeError(f"ffmpeg failed for segment {i}")
    os.replace(out + ".tmp.mp4", out)
    print(f"[seg] {sid} frames {f0}-{f1} logo={'white' if logos[i][0][0].mean() > 128 else 'black'}", flush=True)
    return out


def logo_report():
    rep = []
    for s in scenes:
        im = cover_fit(Image.open(os.path.join(ep_dir, s["image"])).convert("RGB"))
        base = np.asarray(im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W,
                                   (im.height - H) // 2 + H)), dtype=np.float32)
        c, weak, lum = logo_choice(base)
        rep.append({"id": s["id"], "logo": "white" if c == "w" else "black", "bg_luminance": round(lum, 3), "halo": weak})
    return rep


if __name__ == "__main__":
    workers = int(os.environ.get("RENDER_WORKERS", "4"))
    with Pool(workers) as pool:
        segs = pool.map(render_segment, range(len(scenes)), chunksize=1)
    lst = os.path.join(SEG, "list.txt")
    open(lst, "w").write("".join(f"file '{os.path.basename(s)}'\n" for s in segs))
    video_only = os.path.join(ep_dir, "work", "video_only.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", video_only], check=True)
    final = os.path.join(ep_dir, f"{series}_Episode{n}_TikTok.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", video_only, "-i", os.path.join(ep_dir, "audio", "final_mix.wav"),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                    "-movflags", "+faststart", final], check=True)
    rep = logo_report()
    sp = os.path.join(ep_dir, "scenes.json")
    sc = json.load(open(sp, encoding="utf-8"))
    for s, r in zip(sc, rep): s["logo"] = r
    json.dump(sc, open(sp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("done:", final)

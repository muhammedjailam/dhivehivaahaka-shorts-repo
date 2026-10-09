"""Word-level highlighted Thaana captions (RTL), rendered with Pillow cluster-by-cluster.
MV Waheed has no GPOS: each base letter is drawn at its pen origin and its fili (zero-advance marks)
at the same origin; clusters advance right-to-left. Digit runs keep LTR order.

Captions(...).layer(t) -> (x0, y0, premultiplied rgb float32 HxWx3, alpha float32 HxWx1) or None
"""
import json, os, re, subprocess, tempfile
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

FONT_SIZE = 82
MAX_W = 820            # text block width (x 140..940): clear of TikTok/Shorts right-side buttons
CENTER_X = 540
BLOCK_BOTTOM = 1500    # bottom of the caption block (logo top is at 1668)
LINE_H = 112
MAX_WORDS = 7
SPACE = 0.42           # x font size
TEXT = (255, 255, 255)
STROKE = (12, 12, 16)
PILL = (217, 58, 74)   # cover-title red
PILL_ALPHA = 0.94
PILL_PAD_X, PILL_SLIDE = 14, 0.10
FADE = 0.12
PAD = 40               # canvas padding around text for stroke/shadow


def series_pill(captions_json):
    """Per-series highlight colour from <series>/caption_style.json ({"pill": [r, g, b]}), else the default PILL."""
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(captions_json)))), "caption_style.json")
    return tuple(json.load(open(p, encoding="utf-8"))["pill"]) if os.path.exists(p) else PILL


# Words with glyphs MV Waheed lacks (Arabic Quran quotes) are shaped by libass (HarfBuzz) with an Arabic font into
# white-on-black masks, then placed like any other word (Pillow here has no RAQM, so it can't shape Arabic).
# This libass build does not apply bidi to neutral characters, so leading/trailing brackets are split off and placed
# by hand: a logically-first bracket sits on the RIGHT of the RTL word, mirrored; a last bracket on the LEFT, mirrored.
FALLBACK_FONT = ("C:/Windows/Fonts/majallab.ttf", "Sakkal Majalla")
FALLBACK_SCALE = 1.25       # Majalla has a small x-height next to MV Waheed
FALLBACK_MID = 0.30         # vertical centre of the fallback word, in font sizes above the Thaana baseline
MIRROR = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "[", '"': '"', "'": "'", "“": "“", "”": "”"}


def _libass(texts, size):
    """Render each text centred on its own canvas; returns [(fill, stroke)] full-canvas L images and the canvas H."""
    W, H = int(size * 0.9 * max(4, max(len(t) for t in texts)) + 200), int(size * 3)
    font_file, font_name = FALLBACK_FONT
    res = []
    with tempfile.TemporaryDirectory() as d:
        import shutil; shutil.copy(font_file, d)
        for text in texts:
            pair = []
            for bord in (0, 6):
                ass = "\n".join([
                    "[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 2", "",
                    "[V4+ Styles]",
                    "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
                    "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, "
                    "MarginL, MarginR, MarginV, Encoding",
                    f"Style: A,{font_name},{size},&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,{bord},0,5,0,0,0,1",
                    "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
                    "Dialogue: 0,0:00:00.00,0:00:01.00,A,,0,0,0,,{\\an5\\pos(%d,%d)}%s" % (W // 2, H // 2, text), ""])
                open(os.path.join(d, "w.ass"), "w", encoding="utf-8").write(ass)
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:d=0.1",
                                "-vf", "ass=w.ass:fontsdir=.", "-frames:v", "1", "m.png"], cwd=d, check=True)
                pair.append(Image.open(os.path.join(d, "m.png")).convert("L").copy())
            res.append(tuple(pair))
    return res, H


def shaped_masks(word, size):
    """Render `word` via ffmpeg/libass. Returns (fill L-image, stroke L-image, top offset from the centre line)."""
    lead = len(word) - len(word.lstrip("({[\"'“”"))
    trail = len(word) - len(word.rstrip(")}]\"'“”"))
    core = word[lead:len(word) - trail]
    # visual order, left -> right: mirrored trailing brackets, core, mirrored leading brackets
    pieces = ["".join(MIRROR[c] for c in reversed(word[len(word) - trail:]))] if trail else []
    pieces.append(core)
    if lead: pieces.append("".join(MIRROR[c] for c in reversed(word[:lead])))
    rendered, H = _libass(pieces, size)
    gap = int(size * 0.04)
    cols = []
    for fill, stroke in rendered:
        x0, _, x1, _ = stroke.getbbox()
        cols.append((fill.crop((x0, 0, x1, H)), stroke.crop((x0, 0, x1, H))))
    Wt = sum(c[1].width for c in cols) + gap * (len(cols) - 1)
    fill, stroke = Image.new("L", (Wt, H)), Image.new("L", (Wt, H))
    x = 0
    for f, s in cols:
        fill.paste(ImageChops.lighter(fill.crop((x, 0, x + s.width, H)), f), (x, 0))
        stroke.paste(ImageChops.lighter(stroke.crop((x, 0, x + s.width, H)), s), (x, 0))
        x += s.width + gap
    x0, y0, x1, y1 = stroke.getbbox()
    return fill.crop((x0, y0, x1, y1)), stroke.crop((x0, y0, x1, y1)), y0 - H // 2


def is_mark(c): return 0x07A6 <= ord(c) <= 0x07B0


def clusters(word):
    out = []
    for p in re.findall(r"[0-9]+(?:[.,][0-9]+)*|.", word, flags=re.S):
        if out and len(p) == 1 and is_mark(p) and not out[-1][0].isdigit():
            out[-1] += p
        else:
            out.append(p)
    return out


class Captions:
    def __init__(self, captions_json, font_path, end_s):
        self.font = ImageFont.truetype(font_path, FONT_SIZE)
        from fontTools.ttLib import TTFont
        self.cmap = set(TTFont(font_path).getBestCmap())
        self._shaped = {}
        self.pill = series_pill(captions_json)
        self.words = [w for blk in json.load(open(captions_json, encoding="utf-8")) for w in blk["words"] if w["word"].strip()]
        for w in self.words:
            w["s"], w["e"] = w["startMs"] / 1000, w["endMs"] / 1000
            w["w"] = self.width(w["word"])
        self.space = FONT_SIZE * SPACE
        self.phrases = self.group()
        # display windows: from first word (-0.15 s) until next phrase starts if close, else last word end + 0.35 s
        for i, p in enumerate(self.phrases):
            ws = p["words"]
            p["t0"] = max(ws[0]["s"] - 0.15, self.phrases[i - 1]["t1"] if i else 0)
            nxt = self.phrases[i + 1]["words"][0]["s"] - 0.15 if i + 1 < len(self.phrases) else end_s
            p["t1"] = nxt if nxt - ws[-1]["e"] < 1.2 else ws[-1]["e"] + 0.35
            p["t1"] = min(p["t1"], end_s)
        self._cache = (None, None)

    # ---------------------------------------------------------------- layout
    def needs_fallback(self, word):
        return any(ord(c) not in self.cmap for c in word if not c.isspace())

    def shaped(self, word):
        if word not in self._shaped:
            self._shaped[word] = shaped_masks(word, int(FONT_SIZE * FALLBACK_SCALE))
        return self._shaped[word]

    def width(self, word):
        if self.needs_fallback(word):
            return self.shaped(word)[1].width - 12   # stroke mask includes the outline on both sides
        return sum(self.font.getlength(c if c[0].isdigit() else c[0]) for c in clusters(word))

    def lines_for(self, ws):
        """Split into 1-2 lines, balanced; returns list of word lists or None if it doesn't fit."""
        def lw(seq): return sum(w["w"] for w in seq) + self.space * (len(seq) - 1)
        if lw(ws) <= MAX_W and len(ws) <= 4:
            return [ws]
        best = None
        for k in range(1, len(ws)):
            a, b = ws[:k], ws[k:]
            if lw(a) <= MAX_W and lw(b) <= MAX_W:
                score = max(lw(a), lw(b)) + (30 if len(a) < len(b) else 0)  # prefer longer top line
                if best is None or score < best[0]: best = (score, [a, b])
        return best[1] if best else ([ws] if lw(ws) <= MAX_W else None)

    def group(self):
        phrases, cur = [], []
        for i, w in enumerate(self.words):
            if cur and (len(cur) >= MAX_WORDS or self.lines_for(cur + [w]) is None):
                phrases.append(cur); cur = []
            cur.append(w)
            t = w["word"].rstrip('"\'”“')
            gap = self.words[i + 1]["s"] - w["e"] if i + 1 < len(self.words) else 9
            hard = t.endswith((".", "؟", "?", "!")) or w["word"].endswith('"') or gap > 0.6
            soft = t.endswith(("،", ",")) and len(cur) >= 3
            if hard or soft:
                phrases.append(cur); cur = []
        if cur: phrases.append(cur)
        # merge lone words into the previous phrase when it still fits and timing is tight
        out = []
        for p in phrases:
            if out and len(p) == 1 and len(out[-1]) < MAX_WORDS and p[0]["s"] - out[-1][-1]["e"] < 0.35 \
                    and self.lines_for(out[-1] + p) is not None and not out[-1][-1]["word"].rstrip('"').endswith((".", "؟")):
                out[-1] = out[-1] + p
            else:
                out.append(p)
        return [{"words": p} for p in out]

    # ---------------------------------------------------------------- rendering
    def build(self, p):
        lines = self.lines_for(p["words"])
        asc, desc = self.font.getmetrics()
        h = LINE_H * len(lines) + 2 * PAD
        w = MAX_W + 2 * PAD
        boxes = []
        stroke = Image.new("L", (w, h), 0); fill = Image.new("L", (w, h), 0)
        ds, df = ImageDraw.Draw(stroke), ImageDraw.Draw(fill)
        for li, ln in enumerate(lines):
            lw = sum(x["w"] for x in ln) + self.space * (len(ln) - 1)
            x = PAD + (MAX_W + lw) / 2          # start at the right edge (RTL)
            base = PAD + li * LINE_H + LINE_H * 0.66
            for word in ln:
                right = x
                if self.needs_fallback(word["word"]):
                    mf, mst, top = self.shaped(word["word"])
                    xl = int(round(x - mst.width + 6)); yt = int(round(base - FALLBACK_MID * FONT_SIZE + top))
                    for img, m in ((stroke, mst), (fill, mf)):
                        box = (xl, yt, xl + m.width, yt + m.height)
                        img.paste(ImageChops.lighter(img.crop(box), m), box)
                    x -= word["w"]
                    boxes.append((x - PILL_PAD_X, base - LINE_H * 0.62, right + PILL_PAD_X, base + LINE_H * 0.30, li))
                    x -= self.space
                    continue
                for c in clusters(word["word"]):
                    if c[0].isdigit():
                        x -= self.font.getlength(c)
                        glyphs = [(c, x)]
                    else:
                        x -= self.font.getlength(c[0])
                        glyphs = [(ch, x) for ch in c]
                    for ch, gx in glyphs:
                        ds.text((gx, base), ch, font=self.font, fill=255, anchor="ls", stroke_width=6, stroke_fill=255)
                        df.text((gx, base), ch, font=self.font, fill=255, anchor="ls")
                boxes.append((x - PILL_PAD_X, base - LINE_H * 0.62, right + PILL_PAD_X, base + LINE_H * 0.30, li))
                x -= self.space
        st = np.asarray(stroke, np.float32)[..., None] / 255
        fi = np.asarray(fill, np.float32)[..., None] / 255
        sh = np.asarray(stroke.filter(ImageFilter.GaussianBlur(7)), np.float32)[..., None] / 255
        sh = np.roll(sh, 5, axis=0) * 0.55
        x0 = int(CENTER_X - w / 2); y0 = int(BLOCK_BOTTOM - h + PAD)
        return dict(x0=x0, y0=y0, w=w, h=h, st=st, fi=fi, sh=sh, boxes=boxes)

    def get(self, i):
        if self._cache[0] != i:
            self._cache = (i, self.build(self.phrases[i]))
        return self._cache[1]

    def phrase_at(self, t):
        lo, hi = 0, len(self.phrases) - 1
        while lo <= hi:
            m = (lo + hi) // 2; p = self.phrases[m]
            if t < p["t0"]: hi = m - 1
            elif t >= p["t1"]: lo = m + 1
            else: return m
        return None

    def layer(self, t):
        i = self.phrase_at(t)
        if i is None: return None
        p = self.phrases[i]; L = self.get(i)
        a = min(1.0, (t - p["t0"]) / FADE, (p["t1"] - t) / FADE)
        rgb = np.zeros((L["h"], L["w"], 3), np.float32); alpha = np.zeros((L["h"], L["w"], 1), np.float32)
        # pill under the active word (slides from the previous word on the same line)
        ws = p["words"]; k = max((j for j, w in enumerate(ws) if w["s"] <= t), default=None)
        if k is not None:
            box = np.array(L["boxes"][k][:4], np.float32)
            if k > 0 and L["boxes"][k - 1][4] == L["boxes"][k][4] and t - ws[k]["s"] < PILL_SLIDE:
                u = (t - ws[k]["s"]) / PILL_SLIDE; u = u * u * (3 - 2 * u)
                box = np.array(L["boxes"][k - 1][:4], np.float32) * (1 - u) + box * u
            pill = Image.new("L", (L["w"], L["h"]), 0)
            ImageDraw.Draw(pill).rounded_rectangle([float(v) for v in box], radius=22, fill=255)
            pa = np.asarray(pill, np.float32)[..., None] / 255 * PILL_ALPHA
            pop = 1.0 if k == 0 and t - ws[0]["s"] > 0.08 or k > 0 else (t - ws[0]["s"]) / 0.08
            pa *= pop
            rgb = rgb * (1 - pa) + np.array(self.pill, np.float32) * pa; alpha = alpha * (1 - pa) + pa
        # shadow, stroke, fill
        for lay, col in ((L["sh"], (0, 0, 0)), (L["st"], STROKE), (L["fi"], TEXT)):
            rgb = rgb * (1 - lay) + np.array(col, np.float32) * lay
            alpha = alpha * (1 - lay) + lay
        return L["x0"], L["y0"], rgb * a, alpha * a   # premultiplied colour


def composite(frame, cap, t, k=1.0):
    """k scales caption opacity (used to keep captions off the cover intro)."""
    r = cap.layer(t)
    if r is None or k <= 0: return frame
    x0, y0, rgb, alpha = r
    rgb, alpha = rgb * k, alpha * k
    h, w = alpha.shape[:2]
    reg = frame[y0:y0 + h, x0:x0 + w]
    reg[:] = reg * (1 - alpha) + rgb
    return frame

"""Export the caption pages (same grouping as the burned-in captions) as an ASS sidecar file:
one Dialogue event per word window with a colour/scale override on the active word.
Usage: python export_ass.py <episode_dir> <episode_number>
"""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from captions import Captions

ep_dir, n = sys.argv[1], sys.argv[2]
PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     os.path.join(ep_dir, "work", f"episode-{n}.wav")]).decode())
cap = Captions(os.path.join(ep_dir, "work", f"episode-{n}-captions.json"), os.path.join(PROJECT, "MVWaheed.otf"), dur)


def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


r_, g_, b_ = cap.pill   # series highlight (default #D93A4A cover-title red) in &HBBGGRR&
HI = f"&H{b_:02X}{g_:02X}{r_:02X}&"
lines = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
         "[V4+ Styles]",
         "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
         "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
         "MarginR, MarginV, Encoding",
         "Style: Thaana,MV Waheed,82,&H00FFFFFF,&H00FFFFFF,&H00100C0C,&H80000000,0,0,0,0,100,100,0,0,1,5,2,2,130,130,420,1",
         "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for p in cap.phrases:
    ws = p["words"]
    for k, w in enumerate(ws):
        a = p["t0"] if k == 0 else w["s"]
        b = ws[k + 1]["s"] if k + 1 < len(ws) else p["t1"]
        if b <= a: continue
        rows = cap.lines_for(ws)
        txt = []
        for row in rows:
            txt.append(" ".join((f"{{\\c{HI}\\fscx108\\fscy108}}{x['word']}{{\\r}}" if x is w else x["word"]) for x in row))
        lines.append(f"Dialogue: 0,{ts(a)},{ts(b)},Thaana,,0,0,0,,{'\\N'.join(txt)}")
open(os.path.join(ep_dir, "captions.ass"), "w", encoding="utf-8-sig").write("\n".join(lines) + "\n")
print(len(cap.phrases), "pages,", len(lines) - 12, "events")

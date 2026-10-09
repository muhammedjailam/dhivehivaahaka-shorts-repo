"""Minimal Thaana RTL shaping for fonts without GPOS (e.g. MV Waheed): Thaana letters don't join,
fili (U+07A6-U+07B0) are zero-advance marks drawn over the following glyph in visual order.
visual(word) returns the string in left-to-right drawing order for Pillow's basic layout."""
import re

def is_mark(c): return 0x07A6 <= ord(c) <= 0x07B0

def clusters(s):
    out = []
    for c in s:
        if out and is_mark(c): out[-1] += c
        else: out.append(c)
    return out

def visual(word):
    # digit runs keep LTR order inside the RTL word
    parts = re.findall(r"[0-9]+(?:[.,][0-9]+)*|.", word, flags=re.S)
    cl = []
    for p in parts:
        if is_mark(p) and cl: cl[-1] += p
        else: cl.append(p)
    vis = []
    for c in reversed(cl):
        if len(c) > 1 and not c[0].isdigit():
            base, marks = c[0], c[1:]
            vis.append(marks + base)       # marks first (zero advance), then the base glyph
        else:
            vis.append(c)
    s = "".join(vis)
    return s.translate(str.maketrans("()[]{}«»", ")(][}{»«"))

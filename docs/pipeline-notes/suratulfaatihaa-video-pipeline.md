---
name: suratulfaatihaa-video-pipeline
description: "Suratul Faatihaa series (eps 422–427, started 2026-10-09): non-fiction tafsir book, symbolic visuals, never-depict sacred figures, emerald captions, all 5 uploaded after manual review"
metadata:
  node_type: memory
  type: project
  originSessionId: 33d25483-669c-4bbb-a1ec-7c62671f2f76
  modified: 2026-10-09T10:22:38.449Z
---

Suratul Faatihaa (ސޫރަތުލް ފާތިޙާ; input `suratul-faatihaa/`, output `output/SuratulFaatihaa/`, video prefix `SuratulFaatihaa_`) eps 422, 423, 424, 426, 427 (no 425) — started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]] and the two-stage reader→planner agents of [[nindheveethimeymathee-video-pipeline]].

NON-FICTION: a reflective book on Al-Fatiha (by Ali Fikry Mohamed), no plot. Visuals follow the narration's metaphors/examples; many beats have no people. Cards are anonymous everyman figures: listener ("you", also sinner/traveller/worshipper), mother, son, powerful_man, elder (`pipeline/characters_suratulfaatihaa.py`). Covers: identical emerald/gold arch + mosque + open Quran, no people → refs text-only.

Binding rules in `series_bible.md`: never depict Allah, prophets, companions, Ahl al-Bayt, angels, Iblis/jinn (not even silhouettes/hands) — places, light, objects instead; hereafter/war/death symbolic; no Arabic calligraphy or letters on mushaf pages.

Series files: `series_bible.md`, `agent_brief.md`, `style.txt` (emerald + gold, golden hour), `tail.txt`, `caption_style.json` (pill [22,122,84] emerald), `refs_sheet.jpg`. Added to shared `pipeline/sound.py`: ambiences cosmos, vast_plain, old_madinah_day, library_night, mosque_dawn, exam_hall, ruins_dust, battlefield_far.

Fixed in shared `pipeline/captions.py` (2026-10-09): straight/curly quotes around Arabic-fallback words now split off like brackets (before, both quotes of `"ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ"` landed in the middle).

Status 2026-10-09: all 5 rendered (~10 min each), QC passed; the user reviewed them manually, then asked for upload → uploaded, site book 'ސޫރަތުލްފާތިޙާގައި ފޮރުވިފައިވާ ސިއްރުތައް' (-Y9wbL), ep order 1–5 = ids 422, 423, 424, 426, 427, all ready.

**Why/How to apply:** the user first wanted a manual check before upload — for new episodes of this series, render and wait for their go-ahead before uploading.

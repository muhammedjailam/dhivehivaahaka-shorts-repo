---
name: taubaa-video-pipeline
description: "Taubaa series (anthology of repentance stories; eps 287, 298, 299 made 2026-10-07): per-episode casts, Saudi settings, Arabic-verse caption fallback"
metadata:
  node_type: memory
  type: project
  originSessionId: 3096ec5f-7708-4036-b17e-91e43961e068
  modified: 2026-10-07T07:28:46.172Z
---

Taubaa (ތައުބާ) is an ANTHOLOGY: every episode is a standalone repentance story with its own cast, so cards are per-episode (`pipeline/characters_taubaa.py`, ids like tv_son/devout_mother (287), jawad/jawad_wife (298), riyadh_boy/riyadh_man/pious_father/... (299)). Same beat pipeline + parallel agents + render queue as [[tedhuveriloabi-video-pipeline]].

Series files in `output/Taubaa/`: `series_bible.md` (synopses + series content rules: no drugs/alcohol/nightclub imagery even as props, crash shown as fog/headlights → ICU cast, wudu = hands at a tap, Makkah at a distance, real sheikhs never depicted), `agent_brief.md`, `style.txt` (teal/steel-blue + amber), `tail.txt` (per-series prompt tail read by gen_images.py, replaces "Modest Maldivian clothing"), `caption_style.json` (amber pill #A8661A).

Decision: stories explicitly set in Saudi Arabia use Saudi characters/dress (thobe, shemagh, abaya) instead of the master prompt's "all characters look Maldivian"; unstated settings stay Maldivian. Flagged to the user; revisit if they object.

**Why:** narration names Riyadh/Makkah/"back to Saudi"; Maldivian dress there would contradict the story.

**How to apply:** for new Taubaa episodes, add that episode's cast to characters_taubaa.py, check whether the setting is stated.

Gotchas:
- Episodes quote Quran verses in Arabic; MV Waheed has no Arabic glyphs (rendered as empty pills). captions.py now shapes any word with glyphs missing from MV Waheed via ffmpeg/libass with Sakkal Majalla (no RAQM in Pillow); this libass build ignores bidi for brackets, so leading/trailing ({[ are split off and placed mirrored by hand. Applies to all series.
- When eyeballing RTL test renders, verify word order with box coordinates — visual reading of Thaana/Arabic tiles is unreliable.
- Ihram: drop the friend's ghutra reference for Makkah beats (model put headdress over ihram).

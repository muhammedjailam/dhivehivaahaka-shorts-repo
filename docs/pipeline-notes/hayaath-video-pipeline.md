---
name: hayaath-video-pipeline
description: "How Hayaath episode videos are produced (beat pipeline scripts, series conventions, Fazaal identity) — reuse for new episodes"
metadata:
  node_type: memory
  type: project
  originSessionId: 6fa95656-bf0f-47f1-9fa6-09db970b0e9c
  modified: 2026-10-07T00:06:42.443Z
---

Episodes 272–275, 319 and 415 of Hayaath were rendered from `main prompt.txt` (272 on 2026-10-07 with the older per-shot render.py; the rest with the beat pipeline, 275/319/415 also on 2026-10-07).

Beat pipeline (use for new episodes): `pipeline/segment.py` → write `pipeline/plan_hayaath_<N>.py` (LOC/MOOD/BEATS/SHOTS) → `plan_beats.py` → `gen_images.py <series_dir> <ep_dir> beats` → `sound.py` → `render_beats.py` (copy work/logo from a previous episode first) → `export_ass.py` → `episode_characters.py` → `qc.py`. `beats_sheet.py <ep_dir>` makes an image contact sheet for review before rendering.
- Planning several episodes at once works well with one subagent per episode writing plan + story_notes + `work/new_characters.json`; then merge new cards yourself (two agents invented the same character under different ids, yaasir/yasir).
- Render ONE episode at a time: two concurrent render_beats.py runs (5 workers each) ran out of RAM; it is resumable, finished segments are kept.
- Ambience keys added: `car_night`, `beach_dusk`. render_beats mux applies volume=-0.3dB (peak now ~-1.8 dBTP).

Series conventions:
- Caption highlight is a cover-title-red pill (#D93A4A) behind the active word, Pillow renderer (MV Waheed has no GPOS), not the prompt's default yellow — kept for series consistency.
- Captions are hidden over the 2.5 s cover intro (red title).
- Character card `young_driver` IS Fazaal (driver ep 272, rescuer ep 273, name revealed ep 274). Cards also exist for hassan, asad, nurse, yasir (Fazaal's friend/go-between, glasses + light-blue checked shirt, from ep 275), shafeena (the sisters' paternal aunt, plum dress, from ep 415).
- Dhooma's reference includes her wheelchair: when she is lying in bed/on sand, describe her in text and drop her reference, or the model draws her twice.
- QC catches the model drawing engaged couples too close and wet clothing see-through: specify a clear arm's length gap and opaque/buttoned clothing in the visual text.
- Caption JSON can contain several transcript blocks (ep 274 had 2): always flatten all blocks.
- OpenCV must be 4.x (5.x dropped Haar cascades) for face-centred crops.
- AAC encode can push the peak over −1.5 dBTP; apply ~−0.3 dB at mux if QC shows it.

---
name: tedhuveriloabi-video-pipeline
description: "Tedhuveriloabi series setup (11 episodes 432–525 rendered 2026-10-07): bible, cards, plum captions, parallel-agent + render-queue workflow"
metadata:
  node_type: memory
  type: project
  originSessionId: 2e8921cc-ab50-4fe6-9c5e-8a984f18b88b
  modified: 2026-10-07T02:46:16.911Z
---

Tedhuveriloabi episodes 432, 434, 455, 456, 479–483, 496, 525 were all rendered on 2026-10-07 with the same beat pipeline as [[hayaath-video-pipeline]]. Ep 525 is the series finale ("ނިމުނީ").

Series files in `output/Tedhuveriloabi/`: `series_bible.md` (synopsis of every episode, character ids, continuity/modesty rules), `agent_brief.md` (per-episode agent instructions), `style.txt`, `caption_style.json` (plum pill #9E2F6A — captions.py/export_ass.py read it per series; Hayaath keeps its red default), `render_queue.txt`. Character script: `pipeline/characters_tedhuveriloabi.py` (16 cards; layaali/rafhaan/ahna references come from crops of the cover via card field `cover_crop`; `ref_pose` overrides the sheet pose).

Workflow that worked: one background agent per episode (plan → images → review → sound → ASS, no render), coordinator reviews `work/beats_sheet.jpg` then appends the episode to `render_queue.txt`; `pipeline/render_queue.py` renders + QCs sequentially (~9–10 min per 10-min episode, RENDER_WORKERS=6).

**Why:** renders in parallel would saturate the 16-core machine; agents editing shared scripts concurrently would conflict.
**How to apply:** for new episodes, reuse the bible/brief, add new cards only for genuinely new recurring characters, and keep cover zips' `.jpg` covers converted to `episode-<N>-cover.png`.

Gotchas: covers ship as .jpg; Rafhaan & Layaali marry in ep 480 (no touching before; side-by-side / hand on arm after); Ahna wears plain dark-grey abaya + black hijab only on her prison-release day; face detection often misses hijab faces, so "tight" crops can land on torsos.

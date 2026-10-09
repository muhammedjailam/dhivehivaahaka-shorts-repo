---
name: milahanduvaru-video-pipeline
description: "Milahanduvaru series (eps 252–261, 2026-10-07): moonlit jinn-wife story; bible/brief/cards, blue captions, island ambience keys"
metadata:
  node_type: memory
  type: project
  originSessionId: 981470a3-8dca-4192-a0c6-2c4de5ae97cc
  modified: 2026-10-07T07:31:57.577Z
---

Milahanduvaru (input folder `milahanduvaru/`, lowercase; output `output/Milahanduvaru/`) episodes 252–261 were produced on 2026-10-07 with the same beat pipeline as [[hayaath-video-pipeline]] and the parallel-agent workflow of [[tedhuveriloabi-video-pipeline]]. Ep 261 is the finale.

Series files: `series_bible.md` (synopses of all 10 episodes, 11 card ids, binding content rules: jinn only as modest humans/silhouettes, no touching before the nikah in 256, no weapons/violence), `agent_brief.md`, `style.txt` (moonlit indigo/silver-blue), `tail.txt`, `caption_style.json` (pill #2A5FC4 = cover-title blue). Cards: `pipeline/characters_milahanduvaru.py`.

Added to shared `pipeline/sound.py`: ambience keys island_day/night, island_house_day/night, jungle_night, beach_day, jetty_day, sea_boat, rain_night/day, storm_night, village_day/night; SFX thunder, rain_start, wind_howl, dhoni_engine, leaves_rustle.

All 10 rendered + QC-passed (314 new images, 6 refusals all auto-rewritten, ~$7 API). Renders took 8–20 min each via `render_queue.py` (ep 260, 24 min audio, took 20 min).

Gotcha: subagents can't create `.md` files with the Write tool ("subagents should return findings as text") — tell them to write story_notes.md via python from Bash, or save their returned text yourself.

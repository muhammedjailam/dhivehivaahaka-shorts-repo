---
name: emmefahumessage-video-pipeline
description: "Emme Fahu Message series (eps 326–329, 2026-10-09): married-couple grief drama, accident never shown, vermilion captions, rainy-apartment ambience keys, Bash tool lacks python"
metadata:
  node_type: memory
  type: project
  originSessionId: 6ee41925-f59e-4f39-bac9-b0e46c8ea895
  modified: 2026-10-09T00:33:40.537Z
---

Emme Fahu Message (އެންމެ ފަހު މެސެޖް, "The Last Message"; input `emme-fahu-message/`, output `output/EmmeFahuMessage/`, video prefix `EmmeFahuMessage_`) eps 326→327→328→329 are one complete arc (329 = ending). Started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]]; upload per [[shorts-site-upload]].

Story: Amaan (wife, 32) + Eethan (husband) after 5 years of failed fertility treatment; fight → he drives off in the rain, dies in an accident, leaves one voice message; she later finds she is pregnant. All 4 covers are the same red payphone image (no people → refs generated from text only).

Series files: `series_bible.md` (setting moved to monsoon Hulhumalé; 10 binding rules), `agent_brief.md`, `style.txt`, `tail.txt`, `caption_style.json` (pill [222,68,40] vermilion), `refs_sheet.jpg`. Cards: `pipeline/characters_emmefahumessage.py` — amaan, eethan, luha (elder sister), dr_mathews, officer_raain, officer_young.

Content decisions: accident never shown (police at door); married couple only side by side / hands held, no hug/kiss; officer never catches Amaan; Amaan always in hijab incl. in bed (sitting up); pregnancy test never near a toilet.

Added to shared `pipeline/sound.py`: ambience apartment_morning, apartment_rain_day, apartment_rain_night, apartment_quiet_night, car_rain, clinic_waiting, nursery_evening; SFX kettle_whistle, pan_sizzle, wipers, clock_tick, keys_jingle.

Status 2026-10-09: all 4 rendered, QC'd and uploaded (site book "އެންމެ ފަހު މެސެޖު", ep order 1–4 = ids 326–329, all ready).

**Gotcha (2026-10-09):** ep 329's first render crashed (ffmpeg pipe `OSError: [Errno 22]`) when another session started a render of a different series at the same time; re-running render_beats.py with RENDER_WORKERS=3 resumed cleanly (partial segments are .tmp files). Also: the Bash tool in this environment had no coreutils/python on PATH — run everything via PowerShell (`C:\Python314\python.exe`). Other sessions were rendering BappageGatulu + Marufas at the same time, so renders were queued until they finished.

---
name: nindheveethimeymathee-video-pipeline
description: "Nindheveethimeymathee series (14 eps 269–552, started 2026-10-09): three-timeline romance, age-split cards, blue captions, two-stage reader→planner agents"
metadata:
  node_type: memory
  type: project
  originSessionId: 1c1faad4-65e8-4b3e-9b79-b031215aa0ab
  modified: 2026-10-09T04:05:40.070Z
---

Nindheveethimeymathee (ނިންދެވޭތީ މޭމަތީ; input `nindheveethimeymathee/`, output `output/Nindheveethimeymathee/`, video prefix `Nindheveethimeymathee_`) eps 269, 271, 276, 295, 296, 339, 400, 401, 419, 420, 437, 442, 445, 552 — started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]]; upload per [[shorts-site-upload]].

Story on three timelines: PRESENT (269/271/276: writer Lail ~29 returns, TV host Saba ~28 in an abusive marriage to Zuhuruf, her balcony fall), SCHOOL (A-level teens Lail/Saba/Asil/Sadhee(girl)/Shahid; Lail's parents Haizum + Sana, Sana dies in 401), PAST (442/445/552: Haizum's affair with Shifa in Vietnam, Sana's lost baby, 552 marital assault + wrist-cut attempt → symbols only). All covers identical (couple on rainy blue balcony, uncovered hair → refs text-only).

Series files: `series_bible.md` (10 binding rules: hijab always, no touching unmarried incl. teen Lail/Saba, no bruise/blood), `agent_brief.md`, `style.txt`, `tail.txt`, `caption_style.json` (pill [56,128,240] = cover-title blue), `refs_sheet.jpg` (kept outside characters/). Cards: `pipeline/characters_nindheveethimeymathee.py` — 21 cards, age splits lail/lail_young/lail_child, saba/saba_young, asil(_young), sadhee(_young), shahid(_young), laira/laira_child; haizum one card for ~38 and ~48.

Added to shared `pipeline/sound.py`: ambiences tv_studio, classroom, hotel_hall, hotel_room, rooftop_day, rooftop_night, seawall_dusk, cemetery_dawn; SFX lift_ding.

**Done 2026-10-09:** all 14 rendered + QC-passed and uploaded (site book 'ނިންދެވީ ތި މޭމަތީ', ep order 1–14, all ready). ~436 beat images + 21 refs, ~$9 API, renders 11–24 min each. 271's first render died with `OSError: [Errno 22]` on the ffmpeg stdin pipe while 14 agents were generating images — a plain re-run of render_beats.py fixed it (render_queue keeps going, so check rc in render_queue.log).

**Gotcha:** the user has a separate "Cleanup completed episodes" session that deletes `work/` and `audio/` of finished episodes project-wide (only the mp4 + scenes/images/notes remain), so qc.py can't be re-run afterwards — verify with ffprobe/ebur128 on the mp4 instead.

**Workflow tweak that worked:** stage 1 = one agent per episode only reads the transcript and writes `work/synopsis.txt`; coordinator merges into bible + cards; stage 2 = SendMessage the SAME agents to plan (they keep the transcript in context). Readers disagreed on genders (Sadhee) — resolve in the bible.

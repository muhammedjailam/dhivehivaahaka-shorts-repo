---
name: sector7-video-pipeline
description: "Sector 7 series (eps 365, 385, 389, 406, 454; 2026-10-07): dystopian bunker sci-fi; no-weapons rule, amber captions, bunker ambience keys"
metadata:
  node_type: memory
  type: project
  originSessionId: 18b04aaf-b5a9-4515-a16d-161857950bdf
  modified: 2026-10-07T11:42:43.678Z
---

Sector 7 (input folder `sector7/`, lowercase; output `output/Sector7/`, video prefix `Sector7_`) episodes 365→385→389→406→454 form one continuous arc (365 = prologue). They were produced on 2026-10-07 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]].

Series files: `series_bible.md` (world, synopses, binding content rules), `agent_brief.md`, `style.txt` (dark rusted bunker, amber vs steel-blue; upper level white/gold), `tail.txt` (no weapons/blood/text/numbers), `caption_style.json` (amber pill [196,104,28] from the cover's "THE SURFACE CALLS"). Cards: `pipeline/characters_sector7.py` (aira, zail, bashir, malik, brent, kyle, marcus). All five covers are the same series poster with no characters.

Decisions: all characters keep South Asian/Maldivian looks even though the bunker is in Germany and some names are Western (Brent, Kyle, Marcus); no weapons ever visible (soldiers have empty hands, shields or flashlights); no touching between Aira and any man.

Added to shared `pipeline/sound.py`: ambience beds wasteland, bunker_machinery, engine_room, corridor_drip, alarm_corridor, workshop, warehouse_crowd, rebel_workshop, vent_shaft, storage_hall, chaos_hall, command_center, detention_room, upper_balcony, surface_green, plus 20 SFX (siren, alarm_beep, computer_beep, metal_clang, steam_hiss, drone_pass, boots_march, electric_spark, weld_hiss, power_down/up, metal_door, vent_knock, engine_rev, distant_boom, energy_zaps, crowd_roar/panic, cuffs_click, box_unlock).

All 5 rendered + QC-passed on 2026-10-07 (123 new beat images + 7 refs, 2 refusals auto-rewritten, ~$3 API, renders 9–10 min each). Model tends to add extra bystanders and to put red stains on Brent's head bandage; ask for 'perfectly clean white bandage' and 'nobody else'.

Gotcha: a bash heredoc containing a Python `'''` block failed to parse; write long code blocks to a scratch file with Write and splice them in with Python.

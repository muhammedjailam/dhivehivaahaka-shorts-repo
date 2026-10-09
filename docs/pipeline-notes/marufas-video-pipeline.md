---
name: marufas-video-pipeline
description: "Marufas series (eps 430–545 on 2026-10-07, ep 570 on 2026-10-09): horror — possessed minor, fake raqi, revenge killing; strict substitution rules, crimson captions, horror sound keys"
metadata:
  node_type: memory
  type: project
  originSessionId: d80ff85d-808c-4845-8ec3-c025def97b27
  modified: 2026-10-07T18:06:11.681Z
---

Marufas (މަރުފަސް; input folder `marufas/` — user typed "marufasall"; output `output/Marufas/`, video prefix `Marufas_`) eps 430→453→461→510→514→544→545 form one arc. Produced 2026-10-07 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]].

Series files: `series_bible.md` (full synopses + 14 binding content rules), `agent_brief.md`, `style.txt` (dark misty charcoal horror), `tail.txt` (no blood/wounds/ropes/knives/monster faces), `caption_style.json` (crimson pill [150,30,40]), `refs_sheet.jpg`. Cards: `pipeline/characters_marufas.py` (yamna, saahidha, khalid, faarish, adheel, ghassan, saeed, aadhanbe) — text-only refs (poster shows a woman from behind).

Content decisions: Yamna is ~15 → never shown hurt/contorted/uncovered/eating raw food; possession = environment, shadows, parents' reactions; Ghassan's implied abuse never visualised (locked door from outside); Aadhanbe's abduction, torture, tongue-cutting and death never shown (empty chair, closed door, police torches).

Added to shared `pipeline/sound.py`: ambience haunted_room, haunted_living, abandoned_house, icu_room, night_lane; SFX bulb_flicker, door_slam, low_growl, whisper_recite, creak, monitor_alarm, flashlight_click, crash_clatter.

All 7 rendered + QC-passed on 2026-10-08 (169 new beat images + 8 refs, 16 refusals all rewritten, ~$4 API; renders 8–14 min each via render_queue.py). Model tends to add extra people to "empty room" aftermath shots — say "EMPTY, still-life of objects only, no people, no figures". Possession/minor-in-bed prompts are refused more often; dropping Yamna's reference or saying "awake, a quiet faraway look" instead of "lifeless stare" got them through.

Ep 570 (2026-10-09, single episode, done solo without subagents): police investigation, Ghassan flees, Faarish learns from Jaleel that Aadhanbe was innocent, Saeed (now island imam) exposes Ghassan. No new cards; Jaleel/police described in text. 22 images (1 refusal, auto-rewritten), rendered + QC passed, uploaded (site episode order 8 of book -CKOif). Setup for a new ep: unzip into `work/`, ffmpeg the .jpg cover to `-cover.png`, copy `work/logo/` from a prior ep, `segment.py <ep> <N>`, then plan → plan_beats → episode_characters → gen_images → beats_sheet → sound → export_ass → render_beats → qc → upload_shorts --only N.

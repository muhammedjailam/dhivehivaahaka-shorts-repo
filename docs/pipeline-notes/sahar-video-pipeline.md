---
name: sahar-video-pipeline
description: "Sahar series (eps 359, 367, 421, 477, 574; 2026-10-09): Palestine 1948 Deir Yassin war drama, Palestinian (not Maldivian) cards, massacre/torture never shown, coral-red captions, 1948 ambience keys"
metadata:
  node_type: memory
  type: project
  originSessionId: 5279801f-9af9-45c2-b568-0e0514af7663
  modified: 2026-10-09T11:43:27.918Z
---

Sahar (ސަހަރް; input `sahar/`, output `output/Sahar/`, video prefix `Sahar_`) — story order 359 → 367 → 421 → 477 → 574 (site ids, one continuous arc). Started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]], two-stage reader→planner agents of [[nindheveethimeymathee-video-pipeline]] and the render queue of [[tedhuveriloabi-video-pipeline]]; upload per [[shorts-site-upload]].

Story: newlyweds Sahar (18) and Yazan (20) torn apart in the Deir Yassin massacre (April 1948); Yazan captured, paraded/tortured, shipped Haifa → France (crew woman Claire); Sahar's family hides in a cave, shelters in Ein Karem with Hashim & Safoora, flees by truck to Jordan. All covers identical (couple embracing before a burning city) → sahar/yazan refs via `cover_crop`, others text-only.

Series files: `series_bible.md` (12 binding rules: no violence/weapons/bodies/flags/insignia; Noor's assault+murder and Yazan's torture fully symbolic; hijab always; Sahar's LEFT arm in a sling from 367 on; Claire always far from Yazan with door open), `agent_brief.md`, `style.txt` (ember/amber 1948 Levant), `tail.txt` (Palestinian clothing, no weapons/flags), `caption_style.json` (pill [232,66,66] = cover-title coral red), `refs_sheet.jpg`. Cards: `pipeline/characters_sahar.py` — 13 (sahar, yazan, laila, mahmood, noor, hamza, fathimaa, ameen, safiyya, sama, hashim, safoora, claire).

Reader-synopsis conflicts resolved in the bible: Noor is Yazan's SISTER (421 says "son"); Fathimaa = Sahar's mother, Safoora = Hashim's wife (477 mixes them).

Added to shared `pipeline/sound.py`: ambiences village_spring_day, village_evening, wedding_crowd, stone_house_day/dawn/night, village_burning, hillside_smoke, olive_hill_day, forest_night, cave, cave_night, truck_back, truck_night, army_camp_night/dawn, old_city_crowd, port_day, ship_cabin, ship_deck, ship_storm, checkpoint_night, desert_dawn, border_post_day, dream_glow; SFX distant_shots, chain_rattle, ship_horn, truck_start, metal_gate, water_splash_small, stone_scrape.

Gotcha: the ref prompt includes the series style, so Claire's sheet came out with village landscape panels and a visible hairline → fixed with card `ref_pose` ("exactly two panels… plain studio background") and "no hair visible" in her visual_prompt.
Images: 120 beat images + 13 refs, 7 refusals (all in 367/421 distress beats; dropping Sama's reference fixed them).

Status 2026-10-09: all 5 rendered (8-9 min each, RENDER_WORKERS=6), QC-passed (-14.3 LUFS, <=-1.6 dBTP, 272-346 MB) and uploaded — site book 'ސަހަރް' (-YkQAs), ep order 1-5 = ids 359, 367, 421, 477, 574, all ready.

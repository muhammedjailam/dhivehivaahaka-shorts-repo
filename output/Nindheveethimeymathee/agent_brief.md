# Brief for an episode agent — Nindheveethimeymathee episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Nindheveethimeymathee" (ނިންދެވޭތީ މޭމަތީ) up to (but
NOT including) the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell
tool** to run commands (the Bash tool here has no python on PATH). Python is `python` (C:\Python314). Always set
`$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and `Set-Location 'D:\Projects\dhivehivaahaka-shorts'`
in the same command. Thirteen other agents are doing the other episodes at the same time, so stay inside your own episode
folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Nindheveethimeymathee/series_bible.md` (timelines, all episode synopses, character ids, and the series content
   rules — BINDING; they override the literal narration). You already wrote `episode-<N>/work/synopsis.txt`; re-read it.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_emmefahumessage_328.py`.
4. The shot segmentation already made for you: `output/Nindheveethimeymathee/episode-<N>/work/segments.json` (shot ids,
   times, Dhivehi text; `work/segment.log` is the same as a readable list). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 21
character cards and their `reference.png` in `output/Nindheveethimeymathee/characters/` (look at
`output/Nindheveethimeymathee/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series cards used; no new cards),
   locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool may refuse
   `.md` files for subagents — then write the text to a `.txt` scratch file with the Write tool and copy it with
   `Copy-Item`.
2. **Plan** `pipeline/plan_nindheveethimeymathee_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via
   the `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Hold images through reflective passages.
   - `chars` = card ids only (see the bible; max 4 per beat, most important first). Pick the card for the right
     TIMELINE (e.g. `lail` = 29-year-old writer, `lail_young` = 17, `lail_child` = 10; `saba` vs `saba_young`; `asil` vs
     `asil_young`…). People without cards are described in `visual` only. Don't put a character in `chars` who isn't
     visible (a phone voice is not visible). When a character wears something other than the card's default outfit
     (school uniform, Haizum in a casual shirt at home, Lail in a dark jacket at night), keep the id in chars and state
     the outfit in `visual`. For Haizum in PAST scenes say "younger, about 38, beard fully black".
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: hijab on
     every woman/girl in every shot; NO touching between unmarried men and women (no handshakes, no hand-holding, no
     hugs, arm's-length distance); Haizum+Sana only side by side / hand on shoulder / hands held; no bruises, bandages,
     blood, wounds, falling people, knives; no lying down; no woman in Haizum's hotel room; no readable text on phones,
     TV screens, cards, notebooks, letters; no alcohol, no smoking, no swimmers. Mark `sens=` / `safe=` for every
     substituted moment. Keep faces in the upper two-thirds and a calm lower third. Always state time of day/light and
     weather in `MOOD`. Memories/flashbacks inside an episode: MOOD "soft hazy dreamlike memory glow".
   - `amb` must be one of: tv_studio, classroom, hotel_hall, hotel_room, rooftop_day, rooftop_night, seawall_dusk,
     cemetery_dawn, apartment_morning, apartment_rain_day, apartment_rain_night, apartment_quiet_night, home_day,
     home_night, room_day, room_night, living_night, balcony_night, upper_balcony, kitchen_busy, office_day, office_quiet,
     office_night, cafe, city_day, road_busy, street_night, night_lane, car_interior, car_night, car_rain,
     hospital_corridor, hospital_room, hospital_night, hospital_day, icu_room, clinic_waiting, beach_day, beach_dusk,
     beach_evening, beach_night, dawn_exterior, rain_night, rain_day, storm_night, memory, memory_rain, hall_crowd,
     mansion_day, mansion_night, courtyard_dinner, garden_day, airport, plane_cabin, city_night_far, resort_evening.
   - SFX names (only these): phone_buzz, door_open, door_close, door_slam, knock, lock_click, creak, footsteps_pavement,
     footsteps_sand, cup_clatter, pour, page_turn, paper_shuffle, pen_scribble, cloth_rustle, car_pass, car_approach,
     car_door, car_drive_off, motorbike_pass, engine_rev, rain_start, thunder, wind_gust, wave_crash, splash,
     leaves_rustle, gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud, glass_break, crash_clatter,
     camera_shutter, applause, crowd_gasp, keyboard_typing, phone_game_taps, kettle_whistle, pan_sizzle, wipers,
     clock_tick, keys_jingle, doorbell_buzz, lift_ding, plane_pass. Gain −12…−24 dB. The Dhivehi substring must occur in
     a word of that shot (plan_beats asserts it). Place SFX only where the narration mentions the action. `hum=True` on
     emotional peaks only. No music of any kind (also no singing sound for Sana's recording — silence/room tone).
   - `transition="dissolve"` into AND out of memories/flashbacks, `transition="black"` for time jumps ("next morning",
     "a week later", "two months later", "years ago"), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Nindheveethimeymathee/episode-<N> pipeline/plan_nindheveethimeymathee_<N>.py`,
   then `python pipeline/episode_characters.py output/Nindheveethimeymathee/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Nindheveethimeymathee output/Nindheveethimeymathee/episode-<N> beats`
   (resumable; run it with a long timeout — up to 600000 ms — or in the background and wait for it). Fourteen agents share
   the API: if it ends with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten
   automatically and logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/Nindheveethimeymathee/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible
   rules (hijab fully covering hair on every woman and girl — check hairlines; no touching between Lail and Saba or
   Haizum and Shifa; no hug/kiss; no lying people; no bruises/blood; no letters/numbers on phones, screens, banners,
   notebooks, clothes, cans), characters match their cards AND their timeline age (17-year-olds must look like teens, not
   adults; 10/12-year-olds as children), the image fits its beat, no duplicated people. To fix one: adjust that beat's
   `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then
   `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Nindheveethimeymathee/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Nindheveethimeymathee/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_nindheveethimeymathee_<N>.py`, and do not touch
   other episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Emme Fahu Message episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Emme Fahu Message" (The Last Message) up to (but NOT
including) the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell
tool** to run commands (the Bash tool in this session has no python/coreutils on PATH). Python is `python`
(C:\Python314). Always set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and
`Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Three other agents are doing the other episodes
at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/EmmeFahuMessage/series_bible.md` (setting, synopses of all 4 episodes, character ids, and the series content
   rules — BINDING; they override the literal narration. This is a married-couple grief drama: a fatal car accident that
   is never shown, a fertility clinic, a pregnancy test, intimate married moments that must stay modest).
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_bappagegatulu_522.py`.
4. Your transcript: `output/EmmeFahuMessage/episode-<N>/work/transcript.txt` (timestamped shots) and the shot
   segmentation already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 6
character cards and their `reference.png` in `output/EmmeFahuMessage/characters/` (look at
`output/EmmeFahuMessage/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line, sensitive-moments
   table (timestamp → safe visual). NOTE: the Write tool refuses `.md` files for subagents — write the text to a `.txt`
   scratch file with the Write tool, then copy/rename it with python (`open(..., "w", encoding="utf-8")`) or
   `Copy-Item`.
2. **Plan** `pipeline/plan_emmefahumessage_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Hold images through reflective passages.
   - `chars` = card ids only (amaan, eethan, luha, dr_mathews, officer_raain, officer_young; max 4 per beat, most
     important first). People without cards (nurse, waiting-room couples, passers-by) are described in `visual` only.
     Don't put a character in `chars` who isn't visible (Eethan's voice on the phone is not visible; a framed photo of
     him is a small object — describe it in `visual` and you MAY add `eethan` to chars so the photo looks like him).
     When Eethan should not wear his default navy t-shirt + joggers (clinic, car, tie memory), keep `eethan` in chars but
     state the outfit in `visual` ("a dark-olive zip-up rain jacket over the navy t-shirt and dark jeans" / "a navy suit,
     white shirt and a tie"). Amaan may wear "a loose long grey cardigan over her cream dress" at night/at home after the
     accident — still the dusty-rose hijab.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: no crash
     or accident imagery, no injury, no needles; no kissing/embracing between Amaan and Eethan (side by side, hand on
     forearm, hands held on a table/in the car are fine); no man touches Amaan except Eethan; hijab fully covering hair
     on every woman in every shot, also at home and in bed; Amaan in bed is SITTING UP against the headboard; no toilet/
     shower; no readable text/numbers on phones, clocks, books, signs, clothes. Mark `sens=` / `safe=` for every
     substituted moment. Keep faces in the upper two-thirds and a calm lower third. Always state time of day/light and
     weather in `MOOD` (morning gold / rainy grey afternoon / rainy night / memory glow). Memories: MOOD "soft hazy
     golden dreamlike memory glow".
   - `amb` must be one of: apartment_morning, apartment_rain_day, apartment_rain_night, apartment_quiet_night, car_rain,
     clinic_waiting, clinic_room, nursery_evening, home_day, home_night, room_day, room_night, living_night,
     balcony_night, city_day, road_busy, street_night, rain_night, rain_day, storm_night, car_interior, car_night,
     hospital_corridor, memory, memory_rain, beach_dusk, beach_evening, dawn_exterior.
   - SFX names (only these): kettle_whistle, pan_sizzle, wipers, clock_tick, keys_jingle, phone_buzz, door_open,
     door_close, door_slam, knock, lock_click, creak, footsteps_pavement, cup_clatter, pour, page_turn, paper_shuffle,
     cloth_rustle, car_pass, car_approach, car_door, car_drive_off, motorbike_pass, rain_start, thunder, wind_gust,
     gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud, camera_shutter, glass_break, leaves_rustle.
     Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only
     where the narration mentions the action (kettle shrieking, phone vibrating, knocking, door closing, wipers, rain
     starting, thunder, keys, the clock ticking, sobbing breath). NEVER a crash/brake/skid sound (no brake_screech,
     glass_break or soft_thud for the accident). `hum=True` on emotional peaks only. No music of any kind.
   - `transition="dissolve"` into AND out of memories/imagined scenes (the tie memory in 328, the voice-message car
     scene in 329), `transition="black"` for time jumps ("that afternoon", "one week later", "weeks passed", "months
     later"), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/EmmeFahuMessage/episode-<N> pipeline/plan_emmefahumessage_<N>.py`, then
   `python pipeline/episode_characters.py output/EmmeFahuMessage/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/EmmeFahuMessage output/EmmeFahuMessage/episode-<N> beats`
   (resumable; run it in the background or with a long timeout — up to 600000 ms — and wait for it). Four agents share
   the API: if it ends with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten
   automatically and logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/EmmeFahuMessage/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible
   rules (hijab fully covering hair on every woman — check hairlines; no kissing/embracing; Amaan + Eethan never in a
   romantic clinch; no man touching Amaan except Eethan; no lying people; no needles, no crash imagery; no letters/
   numbers on phones, clocks, screens, books, signs, t-shirts), characters match their cards (Amaan dusty-rose hijab +
   cream dress; Eethan short beard + navy t-shirt unless the visual says otherwise; Luha black hijab + deep-teal dress;
   Dr. Mathews white coat, grey beard, rimless glasses; officers dark-navy uniform), the image fits its beat, no
   duplicated people. To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete
   `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat;
   log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/EmmeFahuMessage/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/EmmeFahuMessage/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_emmefahumessage_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

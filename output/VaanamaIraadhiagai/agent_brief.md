# Brief for an episode agent — Vaanama Iraadhiagai episode <N> (stage 2: PLAN + IMAGES + SOUND)

You already read your transcript and wrote `work/synopsis.txt` (stage 1). Now produce everything for ONE episode of the
Dhivehi audio drama "Vaanama Iraadhiagai" up to (but NOT including) the final video render. Project root:
`D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands (Python is `python`). Always
set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and `Set-Location
'D:\Projects\dhivehivaahaka-shorts'` in the same command. Four other agents are doing the other episodes at the same
time, so stay inside your own episode folder and your own plan file.

**THE USER WANTS THIS SERIES TO LOOK LIKE AN ANIME.** The series `style.txt` already makes every prompt an anime-film
frame; write your `visual` texts like an anime storyboard (expressive faces, anime tears, glowing skies, sparkling
sea, cherry-pink sunset clouds, lens glow, dramatic close-ups on eyes, sweeping wide establishing shots of the island)
— but keep it a Maldivian island (coconut palms, coral-sand lanes, turquoise lagoon), never Japan (no cherry trees,
torii, kimono, Japanese signs, school sailor uniforms).

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/VaanamaIraadhiagai/series_bible.md` — setting, the merged synopsis of all 5 episodes, character ids (note:
   the little brother is ALWAYS `nawfal`, even when the transcript says Kyle or Zen; Zaina's nickname is also Zen),
   and the **12 BINDING content rules** (they override the literal narration and your own synopsis where they differ).
   Luyoon and Maaniu are NOT married: arm's length apart, never touching, never on the motorbike together.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_sahar_359.py`.
4. Your `work/segments.json` / `work/transcript.txt` (shot numbers, times, Dhivehi text) — you already know them.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, series `style.txt`, `tail.txt`, `caption_style.json`, and all 8 character cards + their anime
`reference.png` in `output/VaanamaIraadhiagai/characters/` (look at `output/VaanamaIraadhiagai/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards are
   created), locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool
   refuses `.md` files for subagents — write the text to a `.txt` scratch file with the Write tool, then copy it with
   `Copy-Item` (or python) to `story_notes.md`.
2. **Plan** `pipeline/plan_vaanamairaadhiagai_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via
   the `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the
   helper pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful
   English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 22–30 s of audio per new image (budget = your
     duration / 26 ± 20%, i.e. about 14–19 images for a 7-minute episode); justify anything above that in
     story_notes. Hold images through the narrator's reflective passages.
   - `chars` = card ids only (luyoon, maaniu, aishath, zaina, nawfal, naaifaa, hawwa_manike, zahuriyya; max 4 per
     beat, most important first). People without cards (fishermen, sweeping women, classmates, harbour crowd, doctor,
     nurse, waiter, schoolchildren) are described in `visual` only as small background figures in modest clothing.
     Don't put a character in `chars` who isn't visible. When a character's look differs from the card, keep the id
     and state it in `visual` (e.g. Luyoon in a white prayer cover while praying; Luyoon in a plain pastel office
     abaya + black hijab with a lanyard with a blank card at work; Maaniu in a plain light-blue work shirt).
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman/girl's hijab fully covers hair and neck in every image (also at home, waking, in hospital). No touching
     between Luyoon and Maaniu (state "an arm's length apart" in every beat that shows both). No readable text,
     letters, numbers or screen content anywhere. Mark `sens=` / `safe=` for every substituted moment. Keep faces in
     the upper two-thirds and a calm lower third. Always state time of day/light in `MOOD` (bright morning / golden
     afternoon / orange-pink sunset / blue dusk / moonlit night with warm lamp light / soft pastel memory glow).
   - `amb` must be one of: island_day, island_night, island_house_day, island_house_night, village_day, village_night,
     night_lane, beach_day, beach_evening, beach_dusk, beach_night, seawall_dusk, jetty_day, harbour_cafe, sea_boat,
     home_day, home_night, room_day, room_night, living_night, kitchen_busy, garden_day, dawn_exterior, night_exterior,
     mosque_dawn, office_day, office_quiet, cafe, shop_day, classroom, exam_hall, hospital_room, hospital_day,
     hospital_corridor, clinic_waiting, street_night, road_busy, rain_day, rain_night, memory, dream_glow.
   - SFX names (only these): door_open, door_close, door_slam, knock, lock_click, creak, footsteps_pavement,
     footsteps_sand, cup_clatter, pour, kettle_whistle, pan_sizzle, cloth_rustle, page_turn, paper_shuffle,
     pen_scribble, leaves_rustle, wind_gust, wave_crash, splash, water_splash_small, dhoni_engine, boat_engine,
     motorbike_pass, engine_rev, phone_buzz, keyboard_typing, keys_jingle, clock_tick, gasp, sigh, sob_breath,
     breath, breath_heavy, heartbeat, soft_thud, crowd_gasp, monitor_alarm, doorbell_buzz, thunder, rain_start.
     Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only
     where the narration mentions the action. `hum=True` on emotional peaks only. No music of any kind; no adhan,
     no voices.
   - `transition="dissolve"` into AND out of memories (school days, the late father), `transition="black"` for time
     jumps ("a few days later", "weeks passed", "the next morning", "that night"), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/VaanamaIraadhiagai/episode-<N> pipeline/plan_vaanamairaadhiagai_<N>.py`,
   then `python pipeline/episode_characters.py output/VaanamaIraadhiagai/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/VaanamaIraadhiagai output/VaanamaIraadhiagai/episode-<N> beats`
   (resumable; run it with a long timeout — up to 600000 ms — and wait for it). Five agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically
   and logged. If a beat keeps being refused, rewrite its `visual` toward symbolism yourself (an empty place, objects,
   a figure from behind, a landscape).
5. **Review images**: run `python pipeline/beats_sheet.py output/VaanamaIraadhiagai/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; zoom into single images when unsure). Check: ANIME style (no
   photoreal frames), section-6 + bible rules (hijab fully covering hair on every woman — check hairlines; Luyoon and
   Maaniu never touching and clearly apart; nobody on a motorbike behind Maaniu; no letters/numbers/screen text
   anywhere), characters match their cards (Luyoon cream-white dress + black hijab; Maaniu curly hair + charcoal
   jacket; Aishath maroon + beige; Zaina sky-blue + white hijab; Nawfal yellow t-shirt; Naaifaa plum + lilac), the
   image fits its beat, Maldivian island setting (not Japan), no duplicated people. To fix one: adjust that beat's
   `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then
   `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/VaanamaIraadhiagai/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/VaanamaIraadhiagai/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_vaanamairaadhiagai_<N>.py`, and do not touch
   other episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

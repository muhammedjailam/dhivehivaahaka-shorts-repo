# Brief for an episode agent — Marufas episode <N>

You produce everything for ONE episode of the Dhivehi audio horror drama "Marufas" up to (but NOT including) the final
video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, ALWAYS
use absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command, and always
`export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Six other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Marufas/series_bible.md` (synopses of all 7 episodes, character ids, places, and the 14 BINDING content
   rules — they override the literal narration. This series is extremely dark: a possessed 15-year-old girl, implied
   sexual abuse by the raqi, self-harm, torture and the killing of an old man. NONE of that is ever shown — only the
   safe substitutes the bible lists).
3. `pipeline/plan_noorin_495.py` as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read;
   check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/Marufas/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 8
character cards and their `reference.png` in `output/Marufas/characters/` (look at `output/Marufas/refs_sheet.jpg`:
aadhanbe, adheel, faarish, ghassan / khalid, saahidha, saeed, yamna).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line,
   sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md` files for subagents — write
   the file with python from Bash (put the text in a `.txt` scratch file first with the Write tool, then copy it with
   python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_marufas_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from the example plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Long reflective/inner passages: hold the image
     and use shots (crops on faces, hands, the door, a dark window).
   - Use the places from the bible consistently (yamna_room, parents_room, living, kitchen, veranda, island_lane,
     beach_night, abandoned_house, faarish_room, hospital) — copy those descriptions into your `LOC`.
   - `chars` = card ids only (yamna, saahidha, khalid, faarish, adheel, ghassan, saeed, aadhanbe), max 4 per beat, most
     important first. People without cards (doctors, nurses, police, school friends, islanders) are described in
     `visual` only. Don't put a character in `chars` who isn't visible (a phone voice is not visible; a distant
     back/silhouette is better described in text without the reference).
   - Write the outfit into `visual` whenever it differs from the card default (Yamna's school uniform in 430 morning,
     hospital gown in 544–545; Khalid's white skullcap for prayer). Yamna's haggard look from 453 on = "pale, tired,
     dark circles under her eyes" — never wounds.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Never
     use words like blood, wound, scratch, bite, knife, stick, rope, tied, gag, corpse, dead body, vomit, guts, raw fish,
     cockroach, demon face, possessed body arching, levitating, red eyes in a `visual`. Mark `sens=` / `safe=` for every
     substituted moment. Keep faces in the upper two-thirds and a calm dark lower third. Always state time/light in
     `MOOD` (night scenes: dim, cold blue haze with one warm lamp; the possessed room: flickering or dead bulbs).
     Possessed moments: show the room/shadow/reactions (bible rule 1); the smoky shadow with long fingers (like the
     cover) at most twice per episode, never with a face. Yamna in bed: under a blanket up to her chest, hijab on.
   - `amb` must be one of: haunted_room, haunted_living, abandoned_house, icu_room, night_lane, room_night, room_day,
     home_day, home_night, living_night, mansion_day, mansion_night, island_day, island_night, island_house_day,
     island_house_night, village_day, village_night, beach_night, beach_dusk, dawn_exterior, night_exterior,
     street_night, garden_day, hospital_corridor, hospital_room, hospital_night, hospital_day, clinic_room, jetty_day,
     sea_boat, rain_night, storm_night, jungle_night, memory.
   - SFX names (only these): door_open, door_close, door_slam, creak, knock, lock_click, footsteps_pavement,
     footsteps_sand, phone_buzz, cup_clatter, glass_break, crash_clatter, bulb_flicker, low_growl, whisper_recite,
     monitor_alarm, flashlight_click, wind_gust, wind_howl, leaves_rustle, wave_crash, splash, pour, soft_thud,
     cloth_rustle, page_turn, gasp, crowd_gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, thunder,
     boat_engine, car_approach, siren. Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot
     (plan_beats asserts it). Place SFX only where the narration mentions the action (bulbs go out → bulb_flicker;
     recitation starts → whisper_recite at −22…−24; door bang → door_slam; things smashed → glass_break /
     crash_clatter; demonic voice/laugh → low_growl at −18…−22, sparingly; ambulance → siren; ICU monitor change →
     monitor_alarm; police torch → flashlight_click; heartbeat for dread, sparingly). The violence in 514/544/545 gets
     at most a muffled soft_thud offscreen — no scream SFX. `hum=True` on emotional peaks/dread only. No music of
     any kind.
   - `transition="black"` for time jumps (night → morning, → next day, "two days later"), `transition="dissolve"` for
     memories (e.g. 545 opening flash of Yamna in the kitchen) and for cutting between the hospital and the abandoned
     house, default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Marufas/episode-<N> pipeline/plan_marufas_<N>.py`, then
   `python pipeline/episode_characters.py output/Marufas/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Marufas output/Marufas/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Seven agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/Marufas/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (no blood/red
   stains/scratches anywhere — especially on Yamna's face, hands and on Aadhanbe; no ropes; no knives/sticks; no monster
   face; hijab fully covering hair on every woman and girl — check hairlines; Yamna's arms covered; no couple lying
   together; no letters/numbers on clocks, walls, phones, TV, monitors), characters match their cards (Yamna petite
   15-year-old, lilac dress, white hijab; Saahidha bottle-green + beige hijab; Khalid cream shirt, grey-streaked beard;
   Faarish black tee + jeans, faded haircut; Adheel olive shirt, curly hair, goatee; Ghassan white shirt + black
   trousers + black bag; Saeed grey kurta + white cap; Aadhanbe checked sarong + white cap), the image fits its beat, no
   duplicated people, no extra copies of a lead. To fix one: adjust that beat's `visual` in the plan (or drop a
   confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`.
   At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Marufas/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Marufas/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_marufas_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

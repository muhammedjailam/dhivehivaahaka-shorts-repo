# Brief for an episode agent — Suratul Faatihaa episode <N>

You produce everything for ONE episode of the Dhivehi narrated book "Suratul Faatihaa" (ސޫރަތުލް ފާތިޙާ — a reflective
tafsir of Surah Al-Fatiha) up to (but NOT including) the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts`
(Windows). Use the Bash tool (python and ffmpeg are on PATH; `export PYTHONIOENCODING=utf-8` before running python that
prints Thaana; `cd /d/Projects/dhivehivaahaka-shorts` in the same command). If Bash fails to find python, use the
PowerShell tool (`python` = C:\Python314). Four other agents are doing the other episodes at the same time, so stay inside
your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/SuratulFaatihaa/series_bible.md` (all episode synopses, the series cards, the recurring LOC wording and the 12
   series content rules — BINDING; they override the literal narration). Re-read your own `episode-<N>/work/synopsis.txt`.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_16february_284.py`.
4. The shot segmentation already made for you: `output/SuratulFaatihaa/episode-<N>/work/segments.json` (shot ids, times,
   Dhivehi text; `work/segment.log` is the same as a readable list). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, the 5
series cards and their `reference.png` in `output/SuratulFaatihaa/characters/` (look at `output/SuratulFaatihaa/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series cards used; no new cards are
   created), locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool
   refuses `.md` files for subagents — write the text to `work/story_notes.txt` with the Write tool, then copy it with
   `cp work/story_notes.txt story_notes.md`.
2. **Plan** `pipeline/plan_suratulfaatihaa_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - This is a reflective book, not a drama: a new image when the narration moves to a NEW concrete image, example,
     story or topic (spec 5.1 "scene change" = the illustration changes); hold images through explanation and rhetorical
     questions; `reuse="beat_00X"` when the narration returns to an earlier image of THIS episode (e.g. the listener at
     prayer, the cosmos, the balance scale). Target ≈ 22–30 s of audio per new image (budget = your duration / 25 ±
     20%; ~24–33 images for a 12-min episode); justify anything above that in story_notes.
   - Use the bible's recurring LOC descriptions (mosque_hall, home_room, beach_dawn, cosmos, plain, old_madinah, study,
     island_lane) word for word in `LOC` when you use those places, so episodes look alike.
   - `chars` = card ids only (listener, mother, son, powerful_man, elder; max 3 per beat, most important first). Many
     beats have NO characters (landscapes, cosmos, objects, symbols) — that is expected and good. Other people are
     described in `visual` only, preferably from behind / silhouetted / at a distance. When a card character wears
     something other than the card outfit, keep the id and state the outfit in `visual` (e.g. listener at prayer: "a white
     crocheted prayer cap"; listener at home at night: "a plain grey t-shirt").
   - NEVER depict Allah, prophets, companions, Ahl al-Bayt, angels, Jibreel, Iblis/Shaytan/jinn as figures — not even as
     silhouettes, hands or distant blurred figures (bible rules 1–4). Hereafter, death, war: rules 5–7. Mushaf pages never
     show letters; no Arabic calligraphy anywhere; no readable text/numbers (rule 9). Prayer shown correctly (rule 10).
     Women: hijab fully covering hair and neck in every shot. Mark `sens=` / `safe=` for every substituted moment
     ("sacred_figure", "hereafter", "death", "violence", "other"). Keep faces in the upper two-thirds and a calm lower
     third. Always state time of day/light in `MOOD`. Historical stories (early Islam, Pharaoh) and memories: MOOD with
     "hazy, slightly desaturated, soft vignette".
   - Make the visuals concrete and beautiful (composition, light, colour, a clear focal subject) — the narration is
     abstract, so pick the strongest concrete image the narration itself offers (the reader's synopsis lists them).
     Prefer variety across the episode: wide landscapes, intimate close-ups (hands raised in dua, a lamp, a key in a palm,
     a drop of water), human moments with the cards.
   - `amb` must be one of: mosque_interior, mosque_dawn, cosmos, vast_plain, old_madinah_day, desert_night, library_night,
     exam_hall, ruins_dust, battlefield_far, beach_day, beach_dusk, beach_evening, dawn_exterior, island_day,
     island_night, island_house_day, island_house_night, home_day, home_night, room_day, room_night, garden_day,
     office_day, city_day, city_night_far, rain_day, rain_night, storm_night, hospital_room, cemetery_dawn, sea_boat,
     jetty_day, village_day, village_night, memory, gallery, classroom.
   - SFX names (only these): door_open, door_close, knock, creak, footsteps_pavement, footsteps_sand, page_turn,
     paper_shuffle, pen_scribble, cloth_rustle, leaves_rustle, pour, cup_clatter, wind_gust, wind_howl, thunder,
     rain_start, wave_crash, splash, heartbeat, breath, sigh, gasp, sob_breath, clock_tick, keys_jingle, box_unlock,
     metal_door, soft_thud, distant_boom, crowd_roar, bulb_flicker, fire_crackle, whisper_recite, camera_shutter,
     phone_buzz, applause. Gain −14…−26 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts
     it). Use SFX sparingly (this is a calm, reflective book): only where the narration names a concrete sound/action
     (a door opening, a key turning = box_unlock, an iron door = metal_door, thunder/storm, rain, waves, heartbeat, pages
     of a book, footsteps on a path, a clock for "time", a sigh). `whisper_recite` only very low (−26) under prayer
     scenes, never as a melody. `distant_boom` at most once, very low, for 423's bombing passage (or not at all).
     `hum=True` on emotional/spiritual peaks only. No music of any kind; the call to prayer is NOT synthesised.
   - `transition="dissolve"` into AND out of historical stories / hadith scenes / memories / the hereafter,
     `transition="black"` for a new chapter or big topic jump, default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/SuratulFaatihaa/episode-<N> pipeline/plan_suratulfaatihaa_<N>.py`, then
   `python pipeline/episode_characters.py output/SuratulFaatihaa/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/SuratulFaatihaa output/SuratulFaatihaa/episode-<N> beats` (resumable;
   run it in the background or with a long timeout — up to 600000 ms — and wait for it). Five agents share the API: if
   it ends with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten
   automatically and logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/SuratulFaatihaa/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; zoom into single images when unsure — crop with PIL into your
   episode's `work/` folder). Check: series rules (no sacred figure drawn — e.g. a robed man in an early-Madinah scene
   must be regenerated; no letters/calligraphy on mushaf pages, walls, lamps; hijab fully covering hair on every woman;
   no bodies/blood/weapons/fire with people; prayer rows facing the same way), characters match their cards (listener
   off-white kurta + short beard; mother sage-green dress + cream hijab; son light-blue t-shirt; powerful_man charcoal
   suit; elder white cap + checked sarong), the image fits its beat, no duplicated people. To fix one: adjust that beat's
   `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then
   `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/SuratulFaatihaa/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/SuratulFaatihaa/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_suratulfaatihaa_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these files
exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav, captions.ass,
work/beats_sheet.jpg.

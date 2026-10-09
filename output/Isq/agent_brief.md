# Brief for an episode agent — Isq episode <N>

You produce everything for ONE episode of the Dhivehi audio romance "Isq" up to (but NOT including) the final video
render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, ALWAYS use
absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command, and always
`export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Five other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Isq/series_bible.md` (synopses of all 6 episodes, character ids, places, outfit continuity and the series
   content rules — BINDING; they override the literal narration: no shirtless/towel Jaleel, no smoking, no touching
   between Jaleel and Maura, no married-couple bed scene, hijab in every shot, etc.).
3. `pipeline/plan_noorin_495.py` as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read;
   check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/Isq/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 10
character cards and their `reference.png` in `output/Isq/characters/` (look at `output/Isq/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line,
   sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md` files for subagents — write
   the file with python from Bash (put the text in a `.txt` scratch file first with the Write tool, then copy it with
   python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_isq_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from the example plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. The narration has long reflective passages about
     feelings — hold images and use shots (crops on faces, hands, the balcony, the moon).
   - Use the places from the bible consistently (Maura's pale-pink house with bougainvillea and white-curtained balcony,
     the white guest house across the sandy street, Nafeesa's courtyard/kitchen, Jaleel's dark Malé home) — copy those
     descriptions into your `LOC` so they match the other episodes.
   - `chars` = card ids only (jaleel, maura, shaaliya, fauziyya, reema, assad, zulfa, salaam, nafeesa, lamha), max 4 per
     beat, most important first. People without cards (bodyguards, officials, neighbours, guests, helper girls, boys,
     children) are described in `visual` only. Don't put a character in `chars` who isn't visible (a phone voice is not
     visible; a person seen only as a distant back/silhouette is better described in text without the reference).
   - Write the outfit into `visual` whenever it differs from the card default (see the bible's continuity section —
     Jaleel's outfit changes per scene; Maura wears orange from 358's sunset through 366, a lilac home dress at night in
     her room).
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: no
     touching between Jaleel and Maura (write "a clear arm's-length gap between them" into every man+woman two-shot),
     hijab fully covering hair and neck on every woman in every shot, Jaleel always fully dressed (never shirtless /
     towel), no cigarettes or smoke, nobody lying down, no readable text/numbers on phones, signs, papers or the
     plane. Never use words like towel, shirtless, naked, bare, cigarette, smoke, kiss, embrace, bed (for a couple) in
     a `visual`. Mark `sens=` / `safe=` for every substituted moment. Keep faces in the upper two-thirds and a calm lower
     third. Always state time/light in `MOOD`.
   - `amb` must be one of: island_day, island_night, island_house_day, island_house_night, village_day, village_night,
     beach_day, beach_evening, beach_dusk, beach_night, jetty_day, sea_boat, airport, plane_cabin, car_night,
     car_interior, street_night, dawn_exterior, night_exterior, garden_day, room_day, room_night, home_day, home_night,
     living_night, balcony_night, mansion_day, mansion_night, city_night_far, hospital_day, hospital_corridor,
     clinic_room, kitchen_busy, courtyard_dinner, eid_street, cafe, hall_crowd, memory.
   - SFX names (only these): door_open, door_close, knock, lock_click, footsteps_pavement, footsteps_sand, car_pass,
     car_approach, car_door, car_drive_off, motorbike_pass, plane_pass, boat_engine, dhoni_engine, wave_crash, splash,
     splat, pour, cup_clatter, glass_break, phone_buzz, camera_shutter, page_turn, paper_shuffle, cloth_rustle,
     leaves_rustle, wind_gust, gasp, crowd_gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud.
     Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only
     where the narration mentions the action (phone photo → camera_shutter; juice → pour; colour bag hit → splat;
     dropped medicine bag → soft_thud; heartbeat for her racing heart, sparingly). `hum=True` on emotional peaks only.
     No music of any kind.
   - `transition="black"` for time jumps (night → dawn, → next day), `transition="dissolve"` for a jump between the
     island and Malé storylines and for memories, default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Isq/episode-<N> pipeline/plan_isq_<N>.py`, then
   `python pipeline/episode_characters.py output/Isq/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Isq output/Isq/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Six agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/Isq/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (hijab fully
   covering hair on every woman — check hairlines; Jaleel fully dressed; no cigarettes; no touching or closeness between
   Jaleel and Maura; nobody lying down; no letters/numbers on phones, signs, the plane, papers), characters match their
   cards (Jaleel collar-length swept-back hair + trimmed beard; Maura petite in white lace or orange with white hijab and
   frangipani; Shaaliya black velvet + maroon hijab; Reema pregnant in sage green + pink hijab; Zulfa blue floral +
   maroon headscarf; Nafeesa lavender + white headscarf; Lamha mint green + coral-pink hijab), the image fits its beat,
   no duplicated people, no extra copies of the lead. To fix one: adjust that beat's `visual` in the plan (or drop a
   confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`.
   At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Isq/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Isq/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_isq_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

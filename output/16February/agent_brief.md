# Brief for an episode agent — 16 February episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "16 February" (16 ފެބްރުއަރީ) up to (but NOT including)
the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). Use the Bash tool (python and ffmpeg
are on PATH; `export PYTHONIOENCODING=utf-8` before running python that prints Thaana; `cd /d/Projects/dhivehivaahaka-shorts`
in the same command). If Bash fails to find python, use the PowerShell tool (`python` = C:\Python314). Four other agents are
doing the other episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/16February/series_bible.md` (setting, the night of 16 February, all episode synopses, character ids, and the
   12 series content rules — BINDING; they override the literal narration). You already wrote
   `episode-<N>/work/synopsis.txt`; re-read it.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_emmefahumessage_328.py`.
4. The shot segmentation already made for you: `output/16February/episode-<N>/work/segments.json` (shot ids, times,
   Dhivehi text; `work/segment.log` is the same as a readable list). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 10
character cards and their `reference.png` in `output/16February/characters/` (look at `output/16February/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series cards used; no new cards are
   created), locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool
   refuses `.md` files for subagents — write the text to `work/story_notes.txt` with the Write tool, then copy it with
   `cp work/story_notes.txt story_notes.md`.
2. **Plan** `pipeline/plan_16february_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Hold images through reflective passages.
   - Use the bible's recurring location descriptions (family_house, night_road, building_site, jetty, resort_office,
     canteen, souvenir_shop) word for word in `LOC` when you use those places, so episodes look alike.
   - `chars` = card ids only (malak, ahlam, kaif, vimla, aanis, zain, mizoo, ali, ubey, zuhoo; max 4 per beat, most
     important first). People without cards (Babu, Rishwan, young officer, police team, taxi driver, ferry passengers,
     staff) are described in `visual` only. Don't put a character in `chars` who isn't visible (voices behind a door,
     an email sender, someone on the phone). The stranger of 16 February is a faceless dark silhouette in 246 and in the
     night-of-16-Feb flashbacks of 250/356 — do NOT put `ahlam` in chars there; in 356's flashback told from Ahlam's side
     you MAY show Ahlam (his face, in rain at night, alone or at a distance from her). When a character wears something
     other than the card outfit, keep the id and state the outfit in `visual` (e.g. Kaif off duty: "a plain dark-grey
     t-shirt and track trousers instead of the uniform"; Malak on 16 Feb night: "her maroon kurta and black hijab soaked
     dark with rain").
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's 12 rules: no
     falling man, no body, no body outline, no blood (also not on the handkerchief), no injuries/bruises on Malak, no
     weapons; no touch between Malak and any man (Kaif, Ahlam, Zain, the stranger, Rishwan); hijab fully covering hair on
     every woman in every shot; no person lying down (sitting up instead); no readable text/numbers on phones, screens,
     emails, folders, watches, clocks, signs, boats. Mark `sens=` / `safe=` for every substituted moment. Keep faces in
     the upper two-thirds and a calm lower third. Always state time of day/light and weather in `MOOD` (dusk / rainy
     night with lightning / bright tropical morning / office after midnight in a storm / memory). Memories/flashbacks:
     MOOD with "hazy, slightly desaturated memory with soft vignette" (16-Feb night flashbacks: "dark rainy night,
     lightning flashes, hazy desaturated memory, soft vignette").
   - `amb` must be one of: island_day, island_night, island_house_day, island_house_night, jungle_night, night_lane,
     beach_day, beach_dusk, beach_evening, jetty_day, sea_boat, rain_night, rain_day, storm_night, village_day,
     village_night, building_site_rain, office_day, office_night, office_storm_night, resort_day, resort_evening,
     shop_day, staff_room, clinic_room, home_day, home_night, room_day, room_night, living_night, apartment_rain_night,
     road_busy, street_night, memory, memory_rain, dawn_exterior, garden_day, cafe.
   - SFX names (only these): door_open, door_close, door_slam, knock, lock_click, creak, footsteps_pavement,
     footsteps_sand, motorbike_pass, engine_rev, car_pass, car_door, siren, phone_buzz, keyboard_typing, paper_shuffle,
     page_turn, cup_clatter, pour, cloth_rustle, leaves_rustle, rain_start, thunder, wind_gust, wind_howl, dhoni_engine,
     boat_engine, wave_crash, splash, gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud, glass_break,
     camera_shutter, clock_tick, keys_jingle, box_unlock, flashlight_click, bulb_flicker, whisper_recite. Gain −12…−24
     dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only where the
     narration mentions the action (ferry engine, thunder, rain starting, siren, footsteps, door, phone, motorbike, the
     file falling = soft_thud, gasp/scream = gasp). NEVER a body-impact sound for the fall (no soft_thud/crash there —
     use thunder or heartbeat). `hum=True` on emotional peaks only. No music of any kind; the call to prayer is NOT
     synthesised (just mention it in the visual via a distant lit minaret if you like).
   - `transition="dissolve"` into AND out of memories/flashbacks/dreams, `transition="black"` for time jumps ("the next
     morning", "a week later", "after midnight"), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/16February/episode-<N> pipeline/plan_16february_<N>.py`, then
   `python pipeline/episode_characters.py output/16February/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/16February output/16February/episode-<N> beats` (resumable; run it
   in the background or with a long timeout — up to 600000 ms — and wait for it). Five agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/16February/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (hijab fully covering
   hair on every woman — check hairlines; no man touching Malak; no body/blood/injury/weapon; no lying people; no
   letters/numbers anywhere), characters match their cards (Malak wine-maroon kurta + black hijab; Ahlam full beard +
   black shirt; Kaif navy police uniform; Vimla mustard libaas + brown floral scarf; Aanis white skullcap + checked
   sarong; Ali glasses + tie; Mizoo teal hijab; Zuhoo white hijab + scrubs), the image fits its beat, no duplicated
   people. To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete
   `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per
   beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/16February/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/16February/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_16february_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these files
exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav, captions.ass,
work/beats_sheet.jpg.

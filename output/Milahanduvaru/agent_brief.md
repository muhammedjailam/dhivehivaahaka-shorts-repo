# Brief for an episode agent — Milahanduvaru episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Milahanduvaru" up to (but NOT including) the final
video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, and
always `export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Nine other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Milahanduvaru/series_bible.md` (story synopses, character ids, continuity and series-specific content rules —
   binding; they override the literal narration).
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read).
4. Your transcript: `output/Milahanduvaru/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot
   segmentation already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, series `style.txt`, `tail.txt`, `caption_style.json`, all 11 character cards and
their `reference.png` in `output/Milahanduvaru/characters/` (look at `characters/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line, sensitive-moments
   table (timestamp → safe visual). NOTE: the Write tool may refuse `.md` files for subagents — if it does, write the file
   with python from Bash (e.g. a small script that writes the text with `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_milahanduvaru_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when the
     story returns to an earlier image. Target ≈ 25–35 s of audio per new image (budget = your duration / 30 ± 20%);
     justify anything above that in story_notes. Much of the narration is inner thought — hold images and use shots.
   - `chars` = ids from the series cards only (max 4 per beat; most important first). People without cards are described
     in `visual` only. Don't put a character in `chars` who isn't visible. For a hazy memory of Zihuna use `zihuna`;
     never put Zumra's card on the distant red-eyed jinn silhouette or an apparition (describe it in text only).
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules (no
     touching before the nikah in 256, no weapons, no violence/injury/blood, jinn only as beautiful modest humans or
     silhouettes, no readable text/Arabic script). Mark `sens=` / `safe=` for every substituted moment. Keep faces in the
     upper two-thirds and a calm lower third. Always say the time of day/light in `MOOD`.
   - `amb` must be one of: island_day, island_night, island_house_day, island_house_night, jungle_night, beach_day,
     beach_night, beach_dusk, beach_evening, jetty_day, sea_boat, rain_night, rain_day, storm_night, village_day,
     village_night, office_day, office_quiet, room_day, room_night, living_night, home_day, home_night, garden_day,
     dawn_exterior, night_exterior, street_night, hall_crowd, mosque_interior, memory, memory_rain.
   - SFX names (only these): door_open, door_close, knock, lock_click, footsteps_pavement, footsteps_sand, motorbike_pass,
     phone_buzz, keyboard_typing, page_turn, cup_clatter, glass_break, soft_thud, cloth_rustle, gasp, crowd_gasp, sigh,
     sob_breath, breath, breath_heavy, heartbeat, wind_gust, wind_howl, wave_crash, splash, thunder, rain_start,
     dhoni_engine, leaves_rustle, fire_crackle, applause. Gain −12…−24 dB. The Dhivehi substring must occur in a word of
     that shot (plan_beats asserts it). Place SFX only where the narration mentions the action. `hum=True` on emotional
     peaks only. No music/drums of any kind.
   - `transition="black"` for time jumps, `"dissolve"` for memories/flashbacks, default xfade.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Milahanduvaru/episode-<N> pipeline/plan_milahanduvaru_<N>.py`, then
   `python pipeline/episode_characters.py output/Milahanduvaru/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Milahanduvaru output/Milahanduvaru/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Ten agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: make a contact sheet of `images/beat_*.png` with Pillow (label each tile with its beat id) and
   LOOK at it (Read the jpg). Check: section-6 + bible rules (modesty — hijab fully covering hair on every woman and girl;
   no touching between Shamaan and Zumra before the nikah; no weapons, blood, wounds, monsters or scary faces; no
   text/letters/logos/Arabic script), characters match their cards (Zumra midnight-blue + silver-grey hijab, Sakeena
   maroon + beige, Shamaan light-blue shirt, Yameen a toddler in yellow), the image fits its beat, no duplicated people.
   To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`,
   rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in
   story_notes. Keep the contact sheet as `episode-<N>/work/beats_sheet.jpg`.
6. **Sound**: `python pipeline/sound.py output/Milahanduvaru/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Milahanduvaru/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_milahanduvaru_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Taubaa episode <N>

You produce everything for ONE episode of the Dhivehi audio story "Taubaa" up to (but NOT including) the final
video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, and
always `export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Two other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Taubaa/series_bible.md` (story synopses, cast per episode, setting decision and series-specific content rules — binding).
3. `pipeline/plan_hayaath_274.py` as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read).
4. Your transcript: `output/Taubaa/episode-<N>/work/episode-<N>-captions.json` (flatten ALL blocks) and the
   shot segmentation already made for you: `work/segments.json` (shot numbers, times, Dhivehi text).

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, series `style.txt`, `tail.txt`, `caption_style.json`, all 11 character cards and their
`reference.png` in `output/Taubaa/characters/` (use only the cards of YOUR episode, see the bible's table).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md` in the same
   shape as `output/Hayaath/episode-274/story_notes.md`: synopsis, characters table (cards created for this episode by the coordinator),
   locations, tone, image budget line, sensitive-moments table (timestamp → safe visual).
2. **Plan** `pipeline/plan_taubaa_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, `SHOTS` (use the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper). Every segment number 1..last must
   have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image. Targets (≈20–35 s of audio per new image): ep 287 (2:55) 7–9 images,
     ep 298 (6:27) 12–17 images, ep 299 (11:58) 22–30 images; justify anything above the range in story_notes.
     This is a reflective, mostly-narrated series: many sentences are reflection — hold images and use shots.
   - `chars` = ids from the series cards only (max 4 per beat; put the most important first). People without cards are
     described in `visual` only. Don't put a character in `chars` who isn't visible.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Mark
     `sens=` / `safe=` for every substituted moment. Keep faces in the upper two-thirds, a calm lower third.
   - `amb` must be one of: mosque_interior, plane_cabin, desert_night, city_night_far, makkah_crowd, clinic_room,
     home_day, home_night, room_day, room_night, living_night, night_exterior, street_night, road_busy, city_day,
     car_interior, car_night, hospital_corridor, hospital_room, hospital_night, hospital_day, dawn_exterior, memory,
     memory_rain, balcony_night, office_day, cafe, garden_day, hall_crowd.
   - SFX names (only these): door_open, door_close, knock, doorbell_buzz, lock_click, footsteps_pavement,
     footsteps_sand, car_pass, car_approach, car_door, car_drive_off, brake_screech, motorbike_pass, phone_buzz,
     keyboard_typing, page_turn, paper_shuffle, pen_scribble, cup_clatter, glass_break, soft_thud, cloth_rustle, gasp,
     crowd_gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, wind_gust, wave_crash, plane_pass, splash.
     Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only
     where the narration mentions the action. `hum=True` on emotional peaks only.
   - `transition="black"` for time jumps, `"dissolve"` for memories/flashbacks, default xfade.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Taubaa/episode-<N> pipeline/plan_taubaa_<N>.py`, then
   `python pipeline/episode_characters.py output/Taubaa/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Taubaa output/Taubaa/episode-<N> beats`
   (resumable, ~1–3 min per few images; run it with a long timeout or in the background and wait for it). If it ends
   with FAILED beats from rate limits/network, just run it again. Refusals are rewritten automatically and logged.
5. **Review images**: make a contact sheet of `images/beat_*.png` with Pillow (label each tile with its beat id) and
   LOOK at it (Read the jpg). Check: section-6 rules (modesty, no violence/blood, no intimacy, no text/letters/logos
   rendered in the image), characters match their cards (hijab colours!; NO alcohol/drugs/pills/smoke/nightclub imagery anywhere; no Arabic script), the image fits its beat, no duplicated people.
   To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`,
   rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in
   story_notes. Keep the contact sheet as `episode-<N>/work/beats_sheet.jpg`.
6. **Sound**: `python pipeline/sound.py output/Taubaa/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Taubaa/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_taubaa_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Noorin episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Noorin" up to (but NOT including) the final video
render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, ALWAYS use
absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command, and always
`export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Three other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Noorin/series_bible.md` (two timelines, synopses of all 4 episodes, character ids, and the series content
   rules — BINDING; they override the literal narration. This series has very sensitive material: child abuse, self-harm,
   marital violence, miscarriage, suicidal thoughts. None of it is ever depicted; follow the rules exactly).
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/Noorin/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 10
character cards and their `reference.png` in `output/Noorin/characters/` (look at `characters/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, timeline (present / flashback per
   section), image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md`
   files for subagents — write the file with python from Bash (put the text in a `.py` or `.txt` scratch file first with
   the Write tool if quoting is awkward, then copy/rename it with python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_noorin_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. The narration has long reflective passages — hold
     images and use shots.
   - Use the RIGHT card for the timeline: present = `noorin`, `uvaish`, `aakif`; twelve years ago = `noorin_young`,
     `uvaish_young`, `aakif_young`, `naahidh`. `zee`, `reem`, `uvaish_lawyer` as needed (Reem: say her age in the
     visual). `chars` = card ids only (max 4 per beat; most important first). People without cards are described in
     `visual` only. Don't put a character in `chars` who isn't visible (a phone voice is not visible).
   - Off-duty present-day Noorin (home, festival, apartment): keep `noorin` in chars but state the outfit in `visual`
     ("not in uniform: wearing a loose deep-plum long abaya-style dress and a black hijab, no cap"). On duty: uniform.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: no
     violence/injury/blood, no lying people, no touching between non-mahram men and women (keep "a clear arm's-length
     gap" written into every man+woman two-shot), hijab fully covering hair on every woman in every shot, no firearms,
     no readable text/numbers on screens, papers, signs or awards. Never use words like abuse, assault, rape, suicide,
     blood, slap, hit, kill, dead, body in a `visual`. Mark `sens=` / `safe=` for every substituted moment. Keep faces in
     the upper two-thirds and a calm lower third. Always state time/light in `MOOD`; flashback MOODs say "twelve years
     earlier, warm soft golden haze".
   - `amb` must be one of: rain_night, storm_night, rain_day, street_night, road_busy, city_day, city_night_far,
     home_day, home_night, room_day, room_night, living_night, balcony_night, office_day, office_quiet, office_night,
     cafe, hall_crowd, mansion_day, mansion_night, resort_evening, beach_day, beach_evening, beach_dusk, beach_night,
     island_day, island_night, island_house_day, island_house_night, village_day, village_night, jetty_day, garden_day,
     hospital_corridor, hospital_night, hospital_room, clinic_room, detention_room, prison_exterior, car_interior,
     car_night, memory, memory_rain, dawn_exterior, night_exterior.
   - SFX names (only these): thunder, rain_start, wind_gust, wind_howl, door_open, door_close, knock, doorbell_buzz,
     lock_click, footsteps_pavement, footsteps_sand, motorbike_pass, car_pass, car_approach, car_door, car_drive_off,
     brake_screech, siren, phone_buzz, keyboard_typing, page_turn, paper_shuffle, pen_scribble, cup_clatter, glass_break,
     soft_thud, cloth_rustle, gasp, crowd_gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, applause, wave_crash,
     splash, leaves_rustle, metal_door (never cuffs_click — no handcuffs; camera flashes get no sfx). Gain
     −12…−24 dB (soft_thud for any strike: −20…−24, muffled and offscreen). The Dhivehi substring must occur in a word of
     that shot (plan_beats asserts it). Place SFX only where the narration mentions the action. `hum=True` on emotional
     peaks only. No music of any kind.
   - `transition="dissolve"` into AND out of flashbacks (and for memories), `transition="black"` for time jumps,
     default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Noorin/episode-<N> pipeline/plan_noorin_<N>.py`, then
   `python pipeline/episode_characters.py output/Noorin/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Noorin output/Noorin/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Four agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/Noorin/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (hijab fully
   covering hair on every woman — check hairlines; no touching or closeness between men and women; no blood, wounds,
   lying people, guns; no letters/numbers on screens, papers, awards, signs), characters match their cards (present
   Noorin navy uniform + black hijab + black cap; young Noorin dusty-rose dress + cream hijab; Uvaish charcoal suit +
   greying beard; young Uvaish white linen shirt, clean-shaven; Aakif all black; young Aakif glasses + light-blue shirt;
   Zee red glasses + mustard hijab; Reem teal dress + beige hijab), the image fits its beat, no duplicated people. To fix
   one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun
   plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Noorin/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Noorin/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_noorin_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

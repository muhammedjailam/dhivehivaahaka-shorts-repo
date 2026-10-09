# Brief for an episode agent — Bappage Gatulu episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Bappage Gatulu" (Father's Killers) up to (but NOT
including) the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with
Git Bash syntax, ALWAYS use absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command, and
always `export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Five other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/BappageGatulu/series_bible.md` (two timelines, synopses of all 6 episodes, character ids, and the series
   content rules — BINDING; they override the literal narration. This series has a murder witnessed by a child, weapons,
   smoking and a break-in. None of the violence is ever depicted; follow the rules exactly).
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/BappageGatulu/episode-<N>/work/transcript.txt` (timestamped shots) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 9
character cards and their `reference.png` in `output/BappageGatulu/characters/` (look at
`output/BappageGatulu/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, timeline (2011 / present per
   section), image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md`
   files for subagents — write the file with python from Bash (put the text in a `.py` or `.txt` scratch file first with
   the Write tool if quoting is awkward, then copy/rename it with python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_bappagegatulu_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Hold images through reflective passages.
   - Use the RIGHT card for the timeline: 2011 = `iyaan_young`, `zahir`, `aminath_young`; present = `iyaan`, `aminath`,
     `asim`, `raaya`, `sameer`, `fareed`. `chars` = card ids only (max 4 per beat; most important first). People without
     cards are described in `visual` only. Don't put a character in `chars` who isn't visible (a phone/audio voice is not
     visible). When Iyaan should NOT wear his default black t-shirt (gallery/café/Raaya's house, break-in), keep `iyaan`
     in chars but state the outfit in `visual` with "NOT the plain black t-shirt of the reference".
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: no
     violence/injury/blood, no weapons, no lying people, no smoking, no touching between Iyaan and Raaya (keep "a clear
     arm's-length gap" written into every Iyaan+Raaya two-shot), hijab fully covering hair on every woman in every shot,
     no readable text/numbers on screens, papers, signs, plates. Never use words like knife, stab, blood, kill, dead,
     body, corpse, murder, gun, cigarette in a `visual`. Mark `sens=` / `safe=` for every substituted moment. Keep faces
     in the upper two-thirds and a calm lower third. Always state time/light in `MOOD`; 2011 MOODs say "2011, stormy
     night, cold desaturated blue-grey haze".
   - `amb` must be one of: rain_night, storm_night, rain_day, street_night, road_busy, city_day, city_night_far,
     home_day, home_night, room_day, room_night, living_night, balcony_night, office_day, office_quiet, office_night,
     cafe, hall_crowd, mansion_day, mansion_night, resort_evening, beach_day, beach_evening, beach_dusk, beach_night,
     garden_day, hospital_corridor, car_interior, car_night, memory, memory_rain, dawn_exterior, night_exterior,
     night_lane, and the new keys for this series: hacker_room (Iyaan's room with computers), server_room, gallery,
     storeroom, lounge_private, harbour_cafe.
   - SFX names (only these): thunder, rain_start, wind_gust, wind_howl, door_open, door_close, door_slam, knock,
     doorbell_buzz, lock_click, box_unlock, creak, footsteps_pavement, motorbike_pass, car_pass, car_approach, car_door,
     car_drive_off, brake_screech, siren, phone_buzz, keyboard_typing, computer_beep, alarm_beep, power_down, power_up,
     flashlight_click, page_turn, paper_shuffle, pen_scribble, cup_clatter, glass_break, soft_thud, cloth_rustle, gasp,
     sigh, sob_breath, breath, breath_heavy, heartbeat, wave_crash, leaves_rustle, metal_door, camera_shutter. Gain
     −12…−24 dB (a muffled offscreen soft_thud for any strike: −22…−24). The Dhivehi substring must occur in a word of
     that shot (plan_beats asserts it). Place SFX only where the narration mentions the action. `hum=True` on emotional
     peaks only. No music of any kind.
   - `transition="dissolve"` into AND out of the 2011 flashback and memories, `transition="black"` for time jumps,
     default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/BappageGatulu/episode-<N> pipeline/plan_bappagegatulu_<N>.py`, then
   `python pipeline/episode_characters.py output/BappageGatulu/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/BappageGatulu output/BappageGatulu/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Six agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/BappageGatulu/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible
   rules (hijab fully covering hair on every woman — check hairlines; no touching or closeness between Iyaan and Raaya;
   no blood, red liquid, wounds, lying people, weapons, cigarettes; no letters/numbers on screens, papers, signs),
   characters match their cards (Iyaan swept-back black hair, black t-shirt unless the visual says otherwise; Raaya
   white dress + light-grey hijab; Asim white shirt + grey moustache; Aminath white hijab + prayer beads; Sameer round
   glasses + maroon tie; Fareed pinstripe suit + thin moustache), the image fits its beat, no duplicated people. To fix
   one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun
   plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/BappageGatulu/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/BappageGatulu/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_bappagegatulu_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

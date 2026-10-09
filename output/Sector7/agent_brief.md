# Brief for an episode agent — Sector 7 episode <N>

You produce everything for ONE episode of the Dhivehi audio drama "Sector 7" up to (but NOT including) the final video
render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax, and always
`export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Four other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Sector7/series_bible.md` (world, synopses of all 5 episodes, character ids, and the series content rules —
   binding; they override the literal narration).
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read).
4. Your transcript: `output/Sector7/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 7
character cards and their `reference.png` in `output/Sector7/characters/` (look at `characters/refs_sheet.jpg`).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line, sensitive-moments
   table (timestamp → safe visual). NOTE: the Write tool may refuse `.md` files for subagents — if it does, write the
   file with python from Bash (a small script writing the text with `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_sector7_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Narration has long descriptive/inner-thought
     passages — hold images and use shots.
   - `chars` = ids from the series cards only (max 4 per beat; most important first). People without cards (overseer,
     workers, rebels, staff, commandos, young Aira) are described in `visual` only. Don't put a character in `chars`
     who isn't visible. Marcus on a screen/hologram may use `marcus` in chars.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules: NO
     weapons of any kind visible, no violence/injury/blood/bodies, no touching between Aira and any man, Aira always
     in her ankle-length coat and hijab, no readable text/numbers/symbols on screens or signs. Mark `sens=` / `safe=`
     for every substituted moment. Keep faces in the upper two-thirds and a calm lower third (floor, grating, table).
     Always state time/light in `MOOD` (underground: "amber work lights", "red alarm light", "cold white light"...).
   - `amb` must be one of: wasteland, bunker_machinery, engine_room, corridor_drip, alarm_corridor, workshop,
     warehouse_crowd, rebel_workshop, vent_shaft, storage_hall, chaos_hall, command_center, detention_room,
     upper_balcony, surface_green, memory, room_night, night_exterior.
   - SFX names (only these): siren, alarm_beep, computer_beep, metal_clang, steam_hiss, drone_pass, boots_march,
     electric_spark, weld_hiss, power_down, power_up, metal_door, vent_knock, engine_rev, distant_boom, energy_zaps,
     crowd_roar, crowd_panic, cuffs_click, box_unlock, door_open, door_close, knock, lock_click, footsteps_pavement,
     keyboard_typing, cup_clatter, glass_break, soft_thud, cloth_rustle, gasp, crowd_gasp, sigh, sob_breath, breath,
     breath_heavy, heartbeat, wind_gust, wind_howl, thunder, splash, fire_crackle, applause. Gain −12…−24 dB (violent
     sounds like distant_boom / energy_zaps / soft_thud: −18…−24, they stay muffled and offscreen). The Dhivehi
     substring must occur in a word of that shot (plan_beats asserts it). Place SFX only where the narration mentions
     the action. `hum=True` on emotional peaks only. No music/drums of any kind.
   - `transition="black"` for time jumps, `"dissolve"` for memories/flashbacks, default xfade.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Sector7/episode-<N> pipeline/plan_sector7_<N>.py`, then
   `python pipeline/episode_characters.py output/Sector7/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Sector7 output/Sector7/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Five agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/Sector7/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (no weapons at
   all — look carefully at soldiers' hands; no blood/wounds; hijab fully covering hair on every woman; no touching
   between Aira and men; no letters/numbers/symbols on screens, signs, boxes), characters match their cards (Aira
   olive-brown coat + charcoal hijab + pendant; Zail grey beard + round glasses; Brent rust-red jacket; Kyle black
   uniform + silver medals; Marcus cream-white coat), the image fits its beat, no duplicated people. To fix one: adjust
   that beat's `visual` in the plan (or drop a confusing reference), delete `images/beat_XXX.png`, rerun
   plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Sector7/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Sector7/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_sector7_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

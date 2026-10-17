# Brief for an episode agent — Gaathil episode <N> (PLAN + IMAGES + SOUND, no render)

Produce everything for ONE episode of the Dhivehi audio thriller "Gaathil" up to (but NOT including) the final video
render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands
(Python is `python`; the Bash tool has no python). Always set `$env:PYTHONIOENCODING='utf-8'` before running python
that prints Thaana, and `Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Two other agents are
doing the other episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Gaathil/series_bible.md` — setting, synopsis of all three episodes, character ids and the **12 BINDING
   content rules** (they override the literal narration). Key points: hijab always; the 20-year-old murder is never
   shown (no body/blood/weapon); no weapons/handcuffs/fighting anywhere; the silicone mask is a theatrical prop, never
   body horror; Adam–Mariyam side by side only; no readable screens, phones, notes or marks; Ibrahim in the photo is a
   real man, never a ghost; no child shown.
3. `pipeline/plan_yaraa_573.py` as the format example of a plan file (LOC / MOOD / BEATS / the `sh()` helper /
   `SHOTS = S` at the end), and `pipeline/plan_beats.py` (how it is read; check which keys `BEATS` entries and `sh()`
   support, e.g. `reuse`, `transition`, `speaker`, crops).
4. Your `work/transcript.txt` (shot id, start–end seconds, Dhivehi text per segment) and `work/segments.json`. Read
   the whole transcript yourself and translate every segment faithfully.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, transcript, series `style.txt` (gritty desaturated painted thriller-cover look matching the
cover), `tail.txt`, `caption_style.json`, and all 9 character cards + `reference.png` in `output/Gaathil/characters/`
(shahid, shahid_mother, amjad, amjad_young, ibrahim, ibrahim_young, adam, mariyam, masked_stranger — look at
`output/Gaathil/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards),
   locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses
   `.md` files for subagents — write the text to a `.txt` scratch file inside your episode's `work/` with the Write
   tool, then copy it with `Copy-Item` to `story_notes.md`.
2. **Plan** `pipeline/plan_gaathil_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (shot / reverse-shot dialogue, e.g. Shahid ↔ Amjad in the
     police room, Adam ↔ Mariyam, the computer screen with the photo). Target ≈ 20–28 s of audio per new image
     (606 ≈ 21–27 images, 607 ≈ 12–16, 608 ≈ 22–28); justify anything above in story_notes. Hold images through
     reflective narration and rhetorical questions.
   - `chars` = card ids only (max 4 per beat, most important first). Don't put a character in `chars` who isn't
     visible. When a character's look differs from the card (rain-soaked Shahid, Ibrahim's imagined disguises in 608,
     Adam/Ibrahim in the bunker), keep/choose the id and state the difference in `visual`. Drop a reference when it
     would make the model draw a person who should be hidden. Wet clothing stays opaque and loose.
   - Use `amjad_young` / `ibrahim_young` only for the "20 years ago" flashback in 608 (seg ~19–23); `adam` for Ibrahim's
     masked life with Mariyam; `ibrahim` for his real face (606 photo, 608 reveal). The masked figure of 607's
     warehouses is `masked_stranger`.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman's hijab fully covers hair and neck. Mark `sens=` / `safe=` for every substituted moment. Keep faces in the
     upper two-thirds and a calm lower third. Images shown on the computer monitor: describe the monitor showing a
     dark rainy photo of a man in a heavy coat among trees (no interface text), or simply cut to a full-frame image of
     the photo itself (`transition="dissolve"`), which reads better on a phone.
   - State time of day/light in `MOOD` (storm night: near-black blue-grey, silver rain, white lightning / room at night:
     single warm bulb + cold monitor glow / pale gold morning / cold grey police room / overcast afternoon warehouses /
     warm lamp evening / sepia memory of 20 years ago / bright sea-blue days on the far island / pitch-black sea night /
     green-black jungle night with a torch / dim yellow bunker bulb).
   - Suspense is built with atmosphere: lightning on the lighthouse, rain on glass, the flickering bulb, a door handle,
     shadows of trees, the empty warehouse lanes, footprints in wet sand, a hand gripping a pen, eyes narrowing.
   - `amb` must be one of: storm_night, rain_night, apartment_rain_night, home_night, island_house_night,
     island_house_day, home_day, island_day, island_night, village_day, village_night, office_day, office_quiet,
     detention_room, jetty_day, abandoned_house, night_lane, beach_day, beach_dusk, sea_boat, jungle_night, storeroom,
     haunted_room, memory.
   - SFX names (only these): camera_shutter, thunder, rain_start, wind_gust, wind_howl, knock, door_open, door_close,
     lock_click, cup_clatter, footsteps_sand, footsteps_pavement, keyboard_typing, phone_buzz, gasp, sigh, heartbeat,
     breath_heavy, bulb_flicker, creak, metal_door, paper_shuffle, wave_crash, boat_engine, dhoni_engine,
     leaves_rustle, cloth_rustle, soft_thud, splash. Gain −12…−24 dB. The Dhivehi substring must occur in a word of
     that shot (plan_beats asserts it). Place SFX only where the narration mentions the action (shutter + thunder,
     the mug falling, the knock, the window banging, the lock, the phone ringing/message, the hatch opening). `hum=True`
     on emotional/fear peaks only. No music of any kind; no voices; no adhan.
   - `transition="dissolve"` into AND out of memories/imagination (606's 20-years-ago memory; 608's imagined disguises
     and the whole Ibrahim/Adam flashback), `transition="black"` for time jumps (the next morning, "two years later").
   - Do NOT reuse images from the other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Gaathil/episode-<N> pipeline/plan_gaathil_<N>.py`, then
   `python pipeline/episode_characters.py output/Gaathil/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Gaathil output/Gaathil/episode-<N> beats` (resumable; run it with
   a long timeout — up to 600000 ms — and wait for it). Three agents share the API: if it ends with FAILED beats from
   rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged. If a beat keeps
   being refused, rewrite its `visual` toward symbolism yourself (an empty place, objects, a figure from behind, a
   landscape).
5. **Review images**: run `python pipeline/beats_sheet.py output/Gaathil/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; Read single `images/beat_XXX.png` when unsure). Check: section-6 + bible rules (hijab
   fully covering hair on every woman; no gun/holster/baton/handcuffs on police; no blood, no body, no gore — the mask
   must look like a soft prop, not skin; no ghostly or supernatural look on Ibrahim; no embrace; no letters/numbers on
   screens, phones, papers, uniforms, boats or walls), characters match their cards (Shahid olive-green shirt + stubble;
   Amjad navy uniform + salt-and-pepper moustache; Ibrahim gaunt + grey stubble + brown coat; Adam sky-blue shirt +
   neat beard; Mariyam dusty-rose + cream hijab; mother maroon + beige scarf), the image fits its beat, no duplicated
   people, the painted gritty thriller style (not flat cartoon). To fix one: adjust that beat's `visual` in the plan
   (or drop a confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then
   `gen_images.py ... beats beat_XXX`. At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Gaathil/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Gaathil/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders the episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_gaathil_<N>.py`, and do not touch the other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Karuna episode <N> (PLAN + IMAGES + SOUND, no render)

Produce everything for ONE episode of the Dhivehi audio family drama "Karuna" up to (but NOT including) the final
video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands
(Python is `python`; the Bash tool has no python). Always set `$env:PYTHONIOENCODING='utf-8'` before running python
that prints Thaana, and `Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Two other agents are
doing the other episodes at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Karuna/series_bible.md` — setting, synopsis of all three episodes, character ids and the **12 BINDING
   content rules** (they override the literal narration). Key points: hijab always on every woman and girl; Shima and
   Yazan never touch and are never shown together in an apartment/bedroom; the night of the sin is never depicted
   (closed door, empty room, rain on a window); no toilet/bathroom interior for the pregnancy test; Qasim's violence is
   never shown as contact (begging on knees, pointing at the door, the gate, the puddle afterwards); childbirth only
   face/upper body + nurse's hand; embraces only between mahram family in 337's ending; no readable text anywhere.
3. `pipeline/plan_yaraa_573.py` as the format example of a plan file (LOC / MOOD / BEATS / the `sh()` helper /
   `SHOTS = S` at the end), and `pipeline/plan_beats.py` (how it is read; check which keys `BEATS` entries and `sh()`
   support, e.g. `reuse`, `transition`, `speaker`, crops).
4. Your `work/transcript.txt` (shot id, start–end seconds, Dhivehi text per segment) and `work/segments.json`. Read
   the whole transcript yourself and translate every segment faithfully.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, transcript, series `style.txt` (lifelike painterly family-drama look matching the cover),
`tail.txt`, `caption_style.json`, and all 9 character cards + `reference.png` in `output/Karuna/characters/`
(shima, shima_older, qasim, qasim_old, naseema, yazan, aisamanike, zeeva, nurse — look at
`output/Karuna/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards),
   locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses
   `.md` files for subagents — write the text to a `.txt` scratch file inside your episode's `work/` with the Write
   tool, then copy it with `Copy-Item` to `story_notes.md`.
2. **Plan** `pipeline/plan_karuna_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (shot / reverse-shot dialogue: Shima ↔ Yazan at dusk in
     335, Shima ↔ Qasim in 336's opening, Aisamanike ↔ Shima on the park bench, Qasim ↔ Shima on the beach in 337).
     Target ≈ 22–30 s of audio per new image (335 ≈ 24–30 images, 336 ≈ 25–32, 337 ≈ 32–40); justify anything above
     in story_notes. Hold images through reflective narration.
   - `chars` = card ids only (max 4 per beat, most important first). Don't put a character in `chars` who isn't
     visible. When a character's look differs from the card (Shima pregnant, soaked, thin, in a hospital gown, older
     but tired), keep the id and state the difference in `visual`. The newborn/baby Zeeva has NO card — describe her
     in `visual`; the `zeeva` card is only the 7-year-old. Use `shima_older` + `qasim_old` only for 337's "seven years
     later" part. Wet clothing stays opaque and loose.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman's and girl's hijab fully covers hair and neck. Mark `sens=` / `safe=` for every substituted moment. Keep
     faces in the upper two-thirds and a calm lower third. Phones: only a soft glow on the face, never a readable
     screen.
   - State time of day/light in `MOOD` (wealthy house by day: soft bright marble interior / Shima's room at night:
     warm bedside lamp + cold phone glow / college library: bright airy daylight / dusk meeting: bruised violet-orange
     dusk / storm night: near-black blue, silver rain, white lightning / rainy lanes: sodium street lights on wet
     asphalt / hot hazy afternoon by the sea / mosque at night: soft warm lamps / Aisamanike's house: warm golden
     morning, cosy lamp evening / hospital: cold white ceiling light / rented room: dim single bulb / office: neutral
     daylight / apartment: bright warm daylight / beach: golden sunset turning to blue dusk).
   - `amb` must be one of: mansion_day, mansion_night, home_day, home_night, room_day, room_night, living_night,
     rain_night, storm_night, apartment_rain_night, apartment_morning, apartment_quiet_night, street_night,
     city_lanes_night, city_day, road_busy, library_day, classroom, cafe, beach_day, beach_dusk, beach_evening,
     seashore_day, mosque_interior, mosque_dawn, garden_day, stone_house_dawn, stone_house_day, stone_house_night,
     abandoned_house, hospital_room, hospital_corridor, delivery_room, office_day, office_quiet, office_night,
     nursery_evening, shop_day, memory, memory_rain.
   - SFX names (only these): door_open, door_close, door_slam, knock, lock_click, metal_gate, footsteps_pavement,
     footsteps_sand, phone_buzz, glass_break, crash_clatter, soft_thud, water_splash_small, thunder, rain_start,
     wind_gust, gasp, sigh, sob_breath, breath_heavy, heartbeat, heart_monitor, cloth_rustle, page_turn, pour,
     cup_clatter, keyboard_typing, paper_shuffle, motorbike_pass, wave_crash, clock_tick, keys_jingle, kettle_whistle,
     creak. Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX
     only where the narration mentions the action (the phone smash, the gate slamming and locking, thunder, the fall
     into the puddle, the cane dropping, the monitor in the delivery room). `hum=True` on emotional peaks only. No
     music of any kind; no voices (no baby-cry sound, no adhan).
   - `transition="dissolve"` into AND out of memories (337's memories of the gate during labour and on the beach),
     `transition="black"` for time jumps ("months passed", "the next morning", "weeks passed", "seven years later").
   - Do NOT reuse images from the other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Karuna/episode-<N> pipeline/plan_karuna_<N>.py`, then
   `python pipeline/episode_characters.py output/Karuna/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Karuna output/Karuna/episode-<N> beats` (resumable; run it with
   a long timeout — up to 600000 ms — and wait for it). Three agents share the API: if it ends with FAILED beats from
   rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged. If a beat keeps
   being refused, rewrite its `visual` toward symbolism yourself (an empty room, objects, a figure from behind, rain
   on a window, a landscape).
5. **Review images**: run `python pipeline/beats_sheet.py output/Karuna/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; Read single `images/beat_XXX.png` when unsure). Check: section-6 + bible rules (hijab
   fully covering hair on every woman and girl; Shima and Yazan clearly apart and not touching; no bed scene, no
   bathroom/toilet; no grabbing/pushing/hitting; no blood; childbirth decent; no exposed pregnant belly; no readable
   text on phones, papers, signs, drawings), characters match their cards (Shima lavender + cream hijab; older Shima
   camel coat + ivory hijab; Qasim white shirt + salt-and-pepper moustache; old Qasim white hair + cane + grey shirt;
   Naseema navy hijab; Yazan light-grey overshirt; Aisamanike sage-green libaas + white scarf; Zeeva pale yellow + white
   headscarf; nurse light-blue scrubs), the image fits its beat, no duplicated people, the lifelike painterly style
   (not flat cartoon). To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete
   `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per
   beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Karuna/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Karuna/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders the episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_karuna_<N>.py`, and do not touch the other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Sahar episode <N> (stage 2: PLAN + IMAGES + SOUND)

You already read your transcript and wrote `work/synopsis.txt` (stage 1). Now produce everything for ONE episode of the
Dhivehi audio drama "Sahar" up to (but NOT including) the final video render. Project root:
`D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands (Python is `python`). Always
set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and `Set-Location
'D:\Projects\dhivehivaahaka-shorts'` in the same command. Four other agents are doing the other episodes at the same
time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Sahar/series_bible.md` — setting (Palestine, spring 1948), the merged synopsis of all 5 episodes, character
   ids, and the **12 BINDING content rules** (they override the literal narration and your own synopsis where they
   differ, e.g. Noor is a girl; Safoora is Hashim's wife; Fathimaa is Sahar's mother). This is a war/massacre story:
   killings, a sexual assault, torture — NONE of it may be shown; follow rules 1–4 and 9 exactly.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example:
   `pipeline/plan_emmefahumessage_327.py`.
4. Your `work/segments.json` / `work/transcript.txt` (shot numbers, times, Dhivehi text) — you already know them.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, series `style.txt`, `tail.txt`, `caption_style.json`, and all 13 character cards + their
`reference.png` in `output/Sahar/characters/` (look at `output/Sahar/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards are
   created), locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool
   refuses `.md` files for subagents — write the text to a `.txt` scratch file with the Write tool, then copy it with
   `Copy-Item` (or python) to `story_notes.md`.
2. **Plan** `pipeline/plan_sahar_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Hold images through reflective passages and the
     narrator's historical explanations.
   - `chars` = card ids only (sahar, yazan, laila, mahmood, noor, hamza, fathimaa, ameen, safiyya, sama, hashim, safoora,
     claire; max 4 per beat, most important first). People without cards (guests, villagers, soldiers, crew, prisoners)
     are described in `visual` only — soldiers ONLY as faceless distant dark silhouettes, never weapons/insignia/flags.
     Don't put a character in `chars` who isn't visible. When a character's look differs from the card, keep the id in
     chars and state it in `visual`: Sahar's bridal outfit (359 wedding: cream-white thobe with gold-and-red embroidery +
     white hijab); **Sahar's LEFT forearm in a plain cloth sling from her injury in 367 onward**; Yazan as a prisoner
     (same clothes dusty and creased, hands loosely wrapped in clean white cloth, no wounds); Safiyya's forehead wrapped in
     a clean cloth strip after 367.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman/girl's hijab fully covers hair and neck in every image (also sleeping — sitting against a wall or a covered
     shape under a blanket seen from a distance; never lying in a bed). No embrace/kiss between Sahar and Yazan (hands held
     / side by side only). No man except her father and brother touches Sahar. Claire always ≥ two arm's lengths from
     Yazan, open door/deck. No blood, wounds, grime or cuts on faces, weapons, bodies, fire on people, chains, cages around
     a person, handcuffs. No readable text/letters/numbers/flags anywhere. Mark `sens=` / `safe=` for every substituted
     moment. Keep faces in the upper two-thirds and a calm lower third. Always state time of day/light in `MOOD`
     (spring morning gold / dawn blue-gold / smoke-darkened ember day / night oil-lamp glow / moonlit night / storm at
     sea). Dreams & memories: MOOD "soft hazy golden dreamlike memory glow".
   - `amb` must be one of: village_spring_day, village_evening, wedding_crowd, stone_house_day, stone_house_dawn,
     stone_house_night, village_burning, hillside_smoke, olive_hill_day, forest_night, cave, cave_night, truck_back,
     truck_night, army_camp_night, army_camp_dawn, old_city_crowd, port_day, ship_cabin, ship_deck, ship_storm,
     checkpoint_night, desert_dawn, desert_night, border_post_day, dream_glow, memory, night_exterior, storm_night,
     rain_night, garden_day, mosque_dawn, ruins_dust, battlefield_far, vast_plain.
   - SFX names (only these): door_open, door_close, door_slam, knock, lock_click, creak, footsteps_pavement,
     footsteps_sand, cup_clatter, pour, water_splash_small, cloth_rustle, page_turn, paper_shuffle, leaves_rustle,
     stone_scrape, wind_gust, gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud, crash_clatter,
     glass_break, thunder, rain_start, wave_crash, fire_crackle, distant_boom, distant_shots, crowd_gasp, crowd_panic,
     boots_march, chain_rattle, cuffs_click, metal_gate, metal_door, ship_horn, truck_start, engine_rev, car_door.
     Gain −12…−24 dB (distant_shots / distant_boom / crowd_panic: −20…−26, they are far away and muffled). The Dhivehi
     substring must occur in a word of that shot (plan_beats asserts it). Place SFX only where the narration mentions
     the action. Violence is at most a muffled offscreen distant_shots / soft_thud — never anything graphic. `hum=True`
     on emotional peaks only. No music of any kind; no adhan/voice sounds.
   - `transition="dissolve"` into AND out of dreams/memories (e.g. 477's Al-Azhar graduation dream),
     `transition="black"` for time jumps ("a month passed", "at midnight", "that evening", cuts between the Sahar and
     Yazan storylines when time also jumps), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Sahar/episode-<N> pipeline/plan_sahar_<N>.py`, then
   `python pipeline/episode_characters.py output/Sahar/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Sahar output/Sahar/episode-<N> beats` (resumable; run it in the
   background or with a long timeout — up to 600000 ms — and wait for it). Five agents share the API: if it ends with
   FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged. If a beat keeps being refused, rewrite its `visual` toward rule-1/4 symbolism yourself (an empty place,
   objects, a figure from behind, a landscape) and drop child references (sama, noor, ameen) for distressed moments.
5. **Review images**: run `python pipeline/beats_sheet.py output/Sahar/episode-<N>` (writes `work/beats_sheet.jpg`) and
   LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (hijab fully covering
   hair on every woman — check hairlines; no embrace; no weapons/guns/rifles (also not slung on silhouettes); no blood,
   wounds, grime, bodies, people lying on the ground, fire on people, chains, cages, flags, insignia, Stars of David,
   crosses; no letters/numbers anywhere), characters match their cards (Sahar black hijab + black thobe with red
   embroidery, sling from 367; Yazan curly hair + keffiyeh; Laila white headscarf + indigo thobe; Hamza red-white
   keffiyeh; Hashim round glasses; Claire navy uniform + navy headscarf), the image fits its beat, period-correct (1948 —
   no modern objects), no duplicated people. To fix one: adjust that beat's `visual` in the plan (or drop a confusing
   reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2
   regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Sahar/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Sahar/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_sahar_<N>.py`, and do not touch other episodes
   or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

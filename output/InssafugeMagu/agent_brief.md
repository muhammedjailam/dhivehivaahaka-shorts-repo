# Brief for an episode agent — Inssafuge Magu episode <N> (PLAN + IMAGES + SOUND, no render)

Produce everything for ONE episode of the Dhivehi audio crime thriller "Inssafuge Magu" up to (but NOT including) the
final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run
commands (Python is `python`). Always set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana,
and `Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Another agent is doing the other episode at
the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/InssafugeMagu/series_bible.md` — setting (New York / Boston, American characters), synopsis of both
   episodes, character ids and the **12 BINDING content rules** (they override the literal narration). Key points:
   hijab always on every woman; the dead men (Victor Vance, Professor Harris) are NEVER shown — no body, no hand of a
   corpse, no blood; no guns/holsters/shooting/fighting shown at all; no touching between Alex and Sarah; the coin's
   inscription and all papers/screens unreadable; no alcohol (whisky glass → overturned teacup); Richard is never
   shown hurt.
3. `pipeline/plan_gaathil_606.py` as the format example of a plan file (LOC / MOOD / BEATS / the `sh()` helper /
   `SHOTS = S` at the end), and `pipeline/plan_beats.py` (how it is read; check which keys `BEATS` entries and `sh()`
   support, e.g. `reuse`, `transition`, `speaker`, `sens`, `safe`, crops).
4. Your `work/transcript.txt` (shot id, start–end seconds, Dhivehi text per segment) and `work/segments.json`. Read
   the whole transcript yourself and translate every segment faithfully.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, transcript, series `style.txt` (dark neo-noir rain thriller with crimson/amber reflections,
matching the cover), `tail.txt`, `caption_style.json`, and all 5 character cards + `reference.png` in
`output/InssafugeMagu/characters/` (alex, rogers, richard, sarah, masked_killer — look at
`output/InssafugeMagu/refs_sheet.jpg`). No new cards.

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids), locations, tone,
   image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool may refuse `.md` files
   for subagents — then write the text to `work/story_notes.txt` with the Write tool and `Copy-Item` it to
   `story_notes.md`.
2. **Plan** `pipeline/plan_inssafugemagu_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via
   the `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every
   segment number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (shot / reverse-shot dialogue: Alex ↔ Rogers in 591, Alex on
     the phone ↔ Richard in his study, Alex ↔ Sarah in 615; the coin close-up; the fax sheet). Target ≈ 22–30 s of
     audio per new image (591 ≈ 23–30 images, 615 ≈ 25–32); justify anything above in story_notes. Hold images
     through reflective narration and rhetorical questions.
   - `chars` = card ids only (max 4 per beat, most important first). Don't put a character in `chars` who isn't
     visible. People without cards (the 1998 photo's young men and Emily, a uniformed officer, forensic staff) are
     described in `visual` only.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Keep
     faces in the upper two-thirds and a calm lower third. Mark `sens=` / `safe=` for every substituted moment (dead
     body, blood, pistol, staged suicide, forced trigger, poison, whisky, Richard's glass/gasp, the smoke bomb, the
     gunshot, the fight, the handshake, pulling Sarah down).
   - The dead-man moments: describe the office/library WITHOUT any person at the desk (empty chair turned away, papers,
     a lamp, rain on glass), and keep Alex/Rogers/Sarah standing or crouching beside it looking down at something below
     frame. Coin moments: Alex's pale-blue latex-gloved hand holding the coin up to the light, or the coin on wet dark
     wood (cover-like), or in a clear plastic evidence bag on the train table. Always "worn illegible inscription".
   - State time of day/light in `MOOD` (Manhattan storm night: near-black, crimson/amber reflections, silver rain /
     office: dim desk lamp, cold blue city glow through the glass / judge's study: warm lamp, rain on window / dawn
     train: misty pale gold / Cambridge morning: grey overcast, wet golden leaves / library: dim grey daylight + warm
     lamp / smoke: grey-black haze, cold window light / 1998 photo: faded black-and-white).
   - `amb` must be one of: city_rain_night, office_storm_night, office_night, office_quiet, mansion_night, home_night,
     train_dawn, city_day, street_night, rain_day, rain_night, car_rain, library_rain_day, library_night, smoke_room,
     memory.
   - SFX names (only these): thunder, rain_start, wind_gust, knock, door_open, door_close, door_slam, lock_click,
     footsteps_pavement, phone_buzz, dial_tone, fax_print, coin_clink, paper_shuffle, page_turn, glass_break, gasp,
     sigh, heartbeat, breath_heavy, bulb_flicker, creak, cloth_rustle, keyboard_typing, smoke_whoosh, steam_hiss,
     crash_clatter, soft_thud, siren, car_pass, leaves_rustle. Gain −12…−24 dB. The Dhivehi substring must occur in a
     word of that shot (plan_beats asserts it). Place SFX only where the narration mentions the action (heavy door
     opening, phone vibrating, glass shattering on the line, the dead tone, the fax starting, thunder + lights, the
     window smashing, the smoke, the shot = a muffled soft_thud + crash_clatter of the bookshelf, the jump out of the
     window). No gunshot sounds. `hum=True` on emotional/fear peaks only. No music of any kind; no voices.
   - `transition="black"` for time jumps; `transition="dissolve"` into AND out of the 1998 photo if you show it full
     frame, and for imagined/remembered moments.
   - Do NOT reuse images from the other episode (it is being made in parallel).
3. Run `python pipeline/plan_beats.py output/InssafugeMagu/episode-<N> pipeline/plan_inssafugemagu_<N>.py`, then
   `python pipeline/episode_characters.py output/InssafugeMagu/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/InssafugeMagu output/InssafugeMagu/episode-<N> beats` (resumable;
   run it with a long timeout — up to 600000 ms — and wait for it). Two agents share the API: if it ends with FAILED
   beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged.
   If a beat keeps being refused, rewrite its `visual` toward symbolism yourself (an empty office, rain on glass,
   objects, a figure from behind, the skyline).
5. **Review images**: run `python pipeline/beats_sheet.py output/InssafugeMagu/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; Read single `images/beat_XXX.png` when unsure). Check: section
   6 + bible rules (hijab fully covering hair on every woman; NO body or slumped person at any desk, no corpse hand, no
   blood or red liquid, no gun/holster anywhere, no whisky/alcohol, no fighting contact, no Alex–Sarah touching; no
   letters/numbers on the coin, fax, papers, phone screens, yearbook, tape or badges), characters match their cards
   (Alex long black overcoat + loosened slim tie, dark-brown combed hair, grey eyes; Rogers brown leather jacket + grey
   moustache; Richard silver hair + charcoal waistcoat + burgundy tie; Sarah ash-grey ankle-length coat + black hijab;
   killer hooded black + mask below the eyes), the image fits its beat, no duplicated people, the dark painterly noir
   style. To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference), delete
   `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations per
   beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/InssafugeMagu/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/InssafugeMagu/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders the episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_inssafugemagu_<N>.py`, and do not touch the
   other episode or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

# Brief for an episode agent — Yaraa episode <N> (PLAN + IMAGES + SOUND, no render)

Produce everything for ONE episode of the Dhivehi audio drama "Yaraa" up to (but NOT including) the final video
render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands
(Python is `python`; the Bash tool has no python). Always set `$env:PYTHONIOENCODING='utf-8'` before running python
that prints Thaana, and `Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Another agent is doing
the other episode at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Yaraa/series_bible.md` — setting, synopsis of both episodes, character ids and the **12 BINDING content
   rules** (they override the literal narration). Key points: hijab always; no swimwear/body emphasis; married couples
   only side by side / holding hands (no embrace, carrying, lying down, kiss, blown kiss); the hoarse voice is NEVER a
   person (no ghost, no figure, no face, no eyes — only the black cloud, empty jungle, Mifzaal's fear); Yaraa and
   Shifza are never shown in the present after they leave; no child/baby anywhere; no readable phone screens.
3. `pipeline/plan_vaanamairaadhiagai_549.py` as the format example of a plan file (LOC / MOOD / BEATS / the `sh()`
   helper / `SHOTS = S` at the end), and `pipeline/plan_beats.py` (how it is read; check which keys `BEATS` entries and
   `sh()` support).
4. Your `work/transcript.txt` (shot id, start–end seconds, Dhivehi text per segment) and `work/segments.json`. Read
   the whole transcript yourself and translate every segment faithfully.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, transcript, series `style.txt` (cinematic semi-realistic painted book-cover look, matching the
cover), `tail.txt`, `caption_style.json`, and all 5 character cards + `reference.png` in `output/Yaraa/characters/`
(yaraa, mifzaal, naveen, shifza, faisal — look at `output/Yaraa/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards),
   locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses
   `.md` files for subagents — write the text to a `.txt` scratch file inside your episode's `work/` with the Write
   tool, then copy it with `Copy-Item` to `story_notes.md`.
2. **Plan** `pipeline/plan_yaraa_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (shot / reverse-shot dialogue, e.g. Mifzaal ↔ Faisal on the
     phone, Mifzaal ↔ Naveen). Target ≈ 20–28 s of audio per new image (≈ 21–29 new images for a 9.5-minute
     episode); justify anything above 30 in story_notes. Hold images through reflective narration.
   - `chars` = card ids only (max 4 per beat, most important first). Don't put a character in `chars` who isn't
     visible. When a character's look differs from the card (e.g. rain-soaked, Naveen's motorbike helmet), keep the
     id and state it in `visual`. Wet clothing must stay opaque and loose.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman's hijab fully covers hair and neck in every image. Married couples: when Mifzaal and Yaraa are together say
     explicitly "sitting/standing side by side" and what their hands do (holding hands is fine, nothing more). Mark
     `sens=` / `safe=` for every substituted moment. Keep faces in the upper two-thirds and a calm lower third. State
     time of day/light in `MOOD` (calm sunny morning / golden noon / green jungle shade / slate-grey storm / blue dusk
     with amber lamps / foggy teal night like the cover / warm hazy memory glow).
   - Horror is built with atmosphere only: the enormous black cloud rising over the jungle canopy, empty sand paths
     disappearing into the trees, leaves stirred by wind, long palm shadows, spider webs in tall grass, a frightened
     face looking back over the shoulder. Never draw the source of the voice.
   - `amb` must be one of: sea_boat, sea_rough, beach_day, island_wild, island_day, jungle_day, jungle_eerie,
     pond_jungle, island_storm_day, rain_day, storm_night, jetty_day, male_jetty_dusk, harbour_cafe, office_day,
     cafe, home_day, street_night, night_lane, city_lanes_night, city_night_far, memory, dream_glow.
   - SFX names (only these): footsteps_sand, footsteps_pavement, wave_crash, splash, water_splash_small, boat_engine,
     dhoni_engine, wind_gust, wind_howl, leaves_rustle, thunder, rain_start, phone_buzz, cloth_rustle, gasp, sigh,
     sob_breath, breath, breath_heavy, heartbeat, soft_thud, motorbike_pass, engine_rev, keys_jingle, low_growl
     (only as a deep distant rumble under the voice moments, very low), creak. Gain −12…−24 dB. The Dhivehi substring
     must occur in a word of that shot (plan_beats asserts it). Place SFX only where the narration mentions the action
     (the phone ringing, the message tone, the thunderclap, the rain, footsteps, the dinghy engine). `hum=True` on
     emotional/fear peaks only (the voice, the empty jungle, Naveen's grief, the message, the final call). No music of
     any kind; no voices; no adhan.
   - `transition="dissolve"` into AND out of memories (582's message: Yaraa remembered on the beach/in the boat with a
     warm hazy memory glow), `transition="black"` for time jumps (arrival in Malé at 7 pm), default xfade otherwise.
   - Do NOT reuse images from the other episode (it is being made in parallel).
3. Run `python pipeline/plan_beats.py output/Yaraa/episode-<N> pipeline/plan_yaraa_<N>.py`, then
   `python pipeline/episode_characters.py output/Yaraa/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Yaraa output/Yaraa/episode-<N> beats` (resumable; run it with a
   long timeout — up to 600000 ms — and wait for it). Two agents share the API: if it ends with FAILED beats from rate
   limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged. If a beat keeps
   being refused, rewrite its `visual` toward symbolism yourself (an empty place, objects, a figure from behind, a
   landscape).
5. **Review images**: run `python pipeline/beats_sheet.py output/Yaraa/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; Read single `images/beat_XXX.png` when unsure). Check: section-6 + bible rules (hijab
   fully covering hair on every woman — check hairlines and wind-blown scarves; no embrace / no lying down / no
   carrying; no swimwear; no ghostly figure or face hidden in the jungle or clouds — look carefully; no
   letters/numbers/screen text anywhere, incl. boat hulls), characters match their cards (Yaraa crimson dress + black
   hijab; Mifzaal white linen shirt + beige chinos + trimmed beard; Naveen navy polo + full beard; Shifza mint-green +
   white hijab; Faisal glasses + grey shirt), the image fits its beat, no duplicated people, the painted cinematic
   style (not flat cartoon). To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference),
   delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations
   per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Yaraa/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Yaraa/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders the episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_yaraa_<N>.py`, and do not touch the other
   episode or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

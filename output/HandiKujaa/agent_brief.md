# Brief for an episode agent — Handi Kujaa episode <N> (PLAN + IMAGES + SOUND, no render)

Produce everything for ONE episode of the Dhivehi audio horror story "Handi Kujaa" up to (but NOT including) the final
video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands
(Python is `python`). Always set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and
`Set-Location 'D:\Projects\dhivehivaahaka-shorts'` in the same command. Four other agents are doing the other episodes
at the same time, so stay inside your own episode folder and your own plan file.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/HandiKujaa/series_bible.md` — setting, synopsis of all five episodes, character ids and the **12 BINDING
   content rules** (they override the literal narration). Key points: hijab always; the spirit (handi) always in an
   opaque white gown + white veil covering hair and neck, her "long hair" drawn as dark smoky ribbons; no blood, gore,
   wounds or bodies anywhere (seabird, Sameer, red sea/sand = eerie red light only); possession without body horror;
   no violence as contact (throat-grip, stick strike, crows, Naazim's shoulder); the iron knife only held up or stuck
   in the sand; Naazim never shirtless; children small and in the background; no readable text.
3. `pipeline/plan_gaathil_606.py` as the format example of a plan file (LOC / MOOD / BEATS / the `sh()` helper /
   `SHOTS = S` at the end), and `pipeline/plan_beats.py` (how it is read; check which keys `BEATS` entries and `sh()`
   support, e.g. `reuse`, `transition`, `speaker`, crops). Crops must be `full`, `medium` or `tight` only
   (render_beats has no `face_<id>` crop) — centre a speaker with `speaker=` / `focus=[x%, y%]`.
4. Your `work/transcript.txt` (shot id, start–end seconds, Dhivehi text per segment) and `work/segments.json`. Read
   the whole transcript yourself and translate every segment faithfully. Your episode opens by repeating the last
   lines of the previous episode — plan it as a continuation (same place, same lighting), not as a fresh opening.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, transcript, series `style.txt` (dark fantasy-horror painted book-cover look), `tail.txt`,
`caption_style.json`, and all 9 character cards + `reference.png` in `output/HandiKujaa/characters/` (aadhambe,
zaahid, shareefa, aslam, aisha, naazim, raaidhu, sameer, handi — look at `output/HandiKujaa/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards),
   locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses
   `.md` files for subagents — write the text to a `.txt` scratch file inside your episode's `work/` with the Write
   tool, then copy it with `Copy-Item` to `story_notes.md`.
2. **Plan** `pipeline/plan_handikujaa_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S`. Every segment
   number 1..last must have a `sh()` entry with a faithful English translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (shot / reverse-shot dialogue, e.g. Aadhambe ↔ possessed
     Aslam, Naazim at the tent flap ↔ the handi by the waves, the family in the roots ↔ the figures outside the tree).
     Target ≈ 22–28 s of audio per new image (≈ 24–30 new images for your ~11-minute episode); justify anything above
     30 in story_notes. Hold images through reflective narration and rhetorical questions.
   - `chars` = card ids only (max 4 per beat, most important first). Don't put a character in `chars` who isn't
     visible (e.g. Sameer's death scene has NO `sameer`). Crowd/family shots: pick the 3–4 most important faces, and
     describe the rest (other family members, the three small children) in text. When a character's look differs
     from the card (rain-soaked, possessed Aslam, the fake grandfather = `aadhambe` + backward feet and sly smile, the
     handi's horror form), keep the id and state the difference in `visual`. Wet clothing stays opaque and loose.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Every
     woman's hijab fully covers hair and neck; the handi always in opaque white gown + white veil. Mark `sens=` /
     `safe=` for every substituted moment. Keep faces in the upper two-thirds and a calm lower third. Supernatural
     horror is built with atmosphere: lightning, sea-green glow, glowing eyes in the dark, the stretched shadow on the
     canvas, torches dying, tree shadows, the lantern flame shrinking, rain through the torn roof, backward feet on
     unmarked sand, red-eyed crows in the canopy.
   - State time of day/light in `MOOD` (sunny holiday sea: bright turquoise and white / hot afternoon / bruised
     violet storm afternoon / dreadful orange-violet sunset / storm night: near-black indigo, silver rain, white
     lightning, sea-green spectral glow / tent at night: single warm oil-lantern light, canvas walls / torchlit jungle /
     ember glow in darkness / wine-red glowing sea (629)).
   - `amb` must be one of: island_day, beach_day, sea_boat, island_storm_day, beach_dusk, beach_storm_night,
     jungle_storm_night, jungle_eerie, tent_storm, sea_rough, storm_night, rain_night, jungle_night.
   - SFX names (only these): thunder, rain_start, wind_gust, wind_howl, leaves_rustle, footsteps_sand, wave_crash,
     splash, dhoni_engine, boat_engine, creak, low_growl, gasp, heartbeat, breath_heavy, sigh, soft_thud,
     cloth_rustle, fabric_tear, wings_flap, flashlight_click, bulb_flicker, fire_crackle, cup_clatter, metal_clang,
     knock. Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX
     only where the narration mentions the action (thunder, the engine dying, the growl, the torches going out, the
     tent flap, the canvas tearing, the scraping fingers, the lantern dying, the thud on the roof, the crows taking
     off, the dive into the sea). `hum=True` on fear/emotional peaks only. No music of any kind; no voices; no adhan.
   - `transition="dissolve"` into AND out of anything imagined or remembered (e.g. 629's hundred-years-ago story — show
     it only symbolically: an old empty jungle clearing in faded sepia, a tiny abandoned cradle-like woven basket,
     never a child or a killing), `transition="black"` for time jumps.
   - Do NOT reuse images from the other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/HandiKujaa/episode-<N> pipeline/plan_handikujaa_<N>.py`, then
   `python pipeline/episode_characters.py output/HandiKujaa/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/HandiKujaa output/HandiKujaa/episode-<N> beats` (resumable; run it
   with a long timeout — up to 600000 ms — and wait for it). Five agents share the API: if it ends with FAILED beats
   from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged. If a beat
   keeps being refused, rewrite its `visual` toward symbolism yourself (an empty place, objects, a figure from behind,
   a landscape, a shadow on canvas).
5. **Review images**: run `python pipeline/beats_sheet.py output/HandiKujaa/episode-<N>` (writes
   `work/beats_sheet.jpg`) and LOOK at it (Read the jpg; Read single `images/beat_XXX.png` when unsure). Check:
   section-6 + bible rules (hijab fully covering hair on every woman and girl; the handi's gown and veil opaque and her
   hair never visible; no blood, wounds, gore, bodies, black liquid, contorted limbs; no knife touching anyone; nobody
   shirtless; no letters on boats/bags/phones/shrine), characters match their cards (Aadhambe white skullcap + white
   beard + stick; Zaahid sky-blue shirt + grey moustache; Shareefa maroon + black hijab; Aslam mustard tee + grey
   checked shirt; Aisha lavender + white hijab; Naazim huge, dark-green tee, full beard; Raaidhu red tee, lanky;
   Sameer navy work shirt + checked sarong), the image fits its beat, no duplicated people, the painted dark-fantasy
   style (not flat cartoon, not photo). To fix one: adjust that beat's `visual` in the plan (or drop a confusing
   reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2
   regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/HandiKujaa/episode-<N> <N>` (writes audio/final_mix.wav, prints
   loudness; −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/HandiKujaa/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders the episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_handikujaa_<N>.py`, and do not touch the other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

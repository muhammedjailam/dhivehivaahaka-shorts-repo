# Brief for an episode agent — Aliflaila episode <N> (stage 2: PLAN + IMAGES + SOUND)

You already read your transcript and wrote `work/synopsis.txt` (stage 1). Now produce everything for ONE episode of the
Dhivehi audio drama "Aliflaila" (One Thousand and One Nights) up to (but NOT including) the final video render.
Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows). **Use the PowerShell tool** to run commands (Python is
`python`). Always set `$env:PYTHONIOENCODING='utf-8'` before running python that prints Thaana, and `Set-Location
'D:\Projects\dhivehivaahaka-shorts'` in the same command. Nine other agents are doing the other episodes at the same
time, so stay inside your own episode folder and your own plan file.

**THE USER WANTS THIS SERIES TO LOOK LIKE A CLASSIC HAND-DRAWN ANIMATED PRINCESS FILM** (they said "like Disney
Princess animations"). The series `style.txt` already makes every prompt such a frame; write your `visual` texts like
a storyboard for a 1990s hand-drawn animated fairy-tale musical: expressive faces and big eyes, graceful poses, flowing
silks, magical sparkles and swirling glittering smoke, glowing lanterns, a huge moon over domes, sweeping desert and sea
vistas, dramatic low angles on the towering jinn. NEVER write "Disney", "Aladdin", "Jasmine", "Genie", "Jafar" or any
film/character name in prompts.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Aliflaila/series_bible.md` — story levels (frame / tale / tale-within-the-tale), merged synopses of all 10
   episodes, character ids, and the **12 BINDING content rules** (they override the literal narration and your own
   synopsis where they differ). Above all: NO swords or weapons drawn ever, nothing of the adultery shown, executions
   and deaths only as symbols, Prophet Sulaiman never depicted, every woman's hair fully covered.
3. `pipeline/plan_taubaa_287.py` (short) as the format example of a plan file, and `pipeline/plan_beats.py` (how it is
   read; check which keys `BEATS` entries and `sh()` support). A longer recent example: `pipeline/plan_sahar_359.py`.
4. Your `work/segments.json` / `work/transcript.txt` (shot numbers, times, Dhivehi text) — you already know them.

Already done for you (do not redo): zip unpacked into `work/`, cover `work/episode-<N>-cover.png`, logo PNGs in
`work/logo/`, segments, series `style.txt`, `tail.txt`, `caption_style.json`, and all 33 character cards + their
`reference.png` in `output/Aliflaila/characters/` (look at `output/Aliflaila/refs_sheet.jpg`).

## Steps
1. **Story notes**: write `episode-<N>/story_notes.md`: synopsis, characters table (series card ids; no new cards are
   created), locations, tone, image-budget line, sensitive-moments table (timestamp → safe visual). NOTE: the Write tool
   refuses `.md` files for subagents — write the text to a `.txt` scratch file with the Write tool, then copy it with
   `Copy-Item` (or python) to `story_notes.md`.
2. **Plan** `pipeline/plan_aliflaila_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from an existing plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode (the frame chamber at the end may reuse the opening chamber
     image only if the light is the same — the dawn ending usually needs its own dawn image). Target ≈ 24–30 s of audio
     per new image (budget = your duration / 27 ± 20%: about 25 images for an 11-minute episode, about 42 for 452).
     Justify anything above that in story_notes. Hold images through reflective passages.
   - `chars` = card ids only (max 4 per beat, most important first; jinn count). People without cards are described
     in `visual` only as small background figures in modest clothing. Don't put a character in `chars` who isn't
     visible. Use `old_man_dogs_young` / `old_man_mule_young` while those men are young inside their own tales, the old
     versions when they stand before the jinni. If a character's look differs from the card, keep the id and state it in
     `visual` (e.g. the merchant in a plain white travelling robe carrying a folded white cloth; the elder brothers in
     ragged patched robes; the jinniyya at first in a patched plain brown gown and plain brown headscarf; King Yunan
     hunched under a heavy hooded grey cloak).
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. No
     sword/dagger/knife ANYWHERE (also not hanging on walls or belts) — write "empty-handed" for the jinn and the kings.
     Every woman/girl's headscarf fully covers hair and neck. No readable text, letters, numbers or script anywhere (a
     book is shown closed or with blank pages; seals are abstract rosettes). Mark `sens=` / `safe=` for every
     substituted moment. Keep faces in the upper two-thirds and a calm lower third. Always state time of day/light in
     `MOOD`. Animals that are enchanted people are drawn as normal animals (gazelle, two black dogs on leashes sitting
     at a distance, grey mule, cow, calf, fish); transformations = sparkle swirls between two separate states.
   - Frame chamber: Shahrazad on a cushion telling the story with expressive hands, Dunyazad on the carpet beside her,
     the king on the divan an arm's length or more away, fully dressed; lattice window with the moonlit city of domes.
   - 486 only: the son's wedding to the herdsman's daughter = symbolic only (her henna-patterned hands holding a small
     lantern, or two cups on a brass tray); never show the boy as a groom.
   - `amb` must be one of: palace_night, palace_dawn, palace_day, throne_hall, palace_garden_day, palace_garden_night,
     palace_kitchen, bazaar_day, desert_day, desert_night, desert_dawn, sandstorm, oasis_day, seashore_dawn,
     seashore_day, lake_mountains, mountain_night, empty_castle, caravan_road, polo_field, island_wild,
     city_lanes_night, ship_deck, ship_storm, port_day, stone_house_day, stone_house_night, stone_house_dawn,
     village_day, village_night, mosque_dawn, memory, dream_glow.
   - SFX names (only these): door_open, door_close, door_slam, knock, lock_click, creak, footsteps_pavement,
     footsteps_sand, horse_hooves, cup_clatter, pour, cloth_rustle, page_turn, paper_shuffle, leaves_rustle, wind_gust,
     wind_howl, sandstorm_gust, wave_crash, splash, net_cast, water_splash_small, smoke_whoosh, magic_shimmer,
     metal_lid, fire_crackle, thunder, gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud, crowd_gasp,
     crash_clatter, glass_break, stone_scrape, clock_tick. Gain −12…−24 dB. The Dhivehi substring must occur in a word of
     that shot (plan_beats asserts it). Place SFX only where the narration mentions the action. `hum=True` on emotional
     peaks only. No music of any kind; no adhan, no voices, no animal calls.
   - `transition="dissolve"` into AND out of each tale / tale-within-the-tale level, `transition="black"` for time
     jumps ("a year passed", "the next morning", "that night"), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Aliflaila/episode-<N> pipeline/plan_aliflaila_<N>.py`, then
   `python pipeline/episode_characters.py output/Aliflaila/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Aliflaila output/Aliflaila/episode-<N> beats` (resumable; run it
   with a long timeout — up to 600000 ms — and wait for it; if it times out just run it again). Ten agents share the API:
   if it ends with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten
   automatically and logged. If a beat keeps being refused, rewrite its `visual` toward symbolism yourself (an empty
   place, objects, a figure from behind, a landscape).
5. **Review images**: run `python pipeline/beats_sheet.py output/Aliflaila/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: hand-drawn animated princess-film style
   (no photoreal, no 3D, no anime), section-6 + bible rules (NO swords/knives/weapons anywhere — check every hand, belt
   and wall; headscarf fully covering hair on every woman — check hairlines; nothing of the betrayal scenes; no
   bodies/heads/blood; no letters/script anywhere), characters match their cards (Shahrazad saffron-gold + ivory
   headscarf; Dunyazad lavender + pink; Shahryar crimson plumed turban + bronze coat; jinn colours), the image fits its
   beat, no duplicated people. To fix one: adjust that beat's `visual` in the plan (or drop a confusing reference),
   delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`. At most 2 regenerations
   per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Aliflaila/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Aliflaila/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_aliflaila_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

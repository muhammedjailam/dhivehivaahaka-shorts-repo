# Brief for an episode agent — Project Phenix episode <N>

You produce everything for ONE episode of the Dhivehi audio crime thriller "Project Phenix" (ޕްރޮޖެކްޓް ފީނިކްސް) up to
(but NOT including) the final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash
tool with Git Bash syntax, ALWAYS use absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command,
and always `export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Six other agents are doing the
other episodes at the same time, so stay inside your own episode folder and your own plan file.

Series folder: `output/ProjectPhenix` (series name for scripts: `ProjectPhenix`). Your episode: `output/ProjectPhenix/episode-<N>`.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/ProjectPhenix/series_bible.md` (synopses of all 7 episodes, character ids, places, and the 14 BINDING content
   rules — they override the literal narration. This is a violent thriller: gunfights, a tortured and murdered young
   man, human experiments, knives, syringes, explosions. NONE of the violence, weapons, bodies or injuries is ever shown
   — only the safe substitutes the bible lists).
3. `pipeline/plan_noorin_495.py` as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read;
   check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/ProjectPhenix/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot
   segmentation already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 12
character cards and their `reference.png` in `output/ProjectPhenix/characters/` (look at
`output/ProjectPhenix/refs_sheet.jpg`: row 1 ashham, faahid, fairooz, habeeb; row 2 kalhe, moosa, naail, naasir; row 3
raniya, raniya_father, saleem, vance).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line,
   sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md` files for subagents — write
   the file with python from Bash (put the text in a `.txt` scratch file first with the Write tool, then copy it with
   python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_phenix_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from the example plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Long reflective/inner passages: hold the image
     and use shots (crops on faces, hands, the door, a dark window).
   - Use the places from the bible consistently (dhoni_sea, kandu_island, bunker_corridor, bunker_lab, isolation_ward,
     vent_shaft, police_office, moosa_mansion, sea_launch, male_alley, gang_den, car_rain, safehouse, cargo_boat,
     villingili_harbour, atoll_hospital, old_jetty, storm_sea, kandu_beach_night, launch_cabin, fairooz_office,
     hulhumale_shore, faahid_flat, police_hq, minister_office, warehouse, dhoonidhoo_cell, coastguard_launch, cargo_ship,
     commissioner_office, hulhumale_beach) — copy those descriptions into your `LOC` (you may split one place into
     several keys, e.g. police_hq_hall / police_hq_server).
   - `chars` = card ids only (ashham, habeeb, moosa, naail, kalhe, raniya, raniya_father, fairooz, faahid, naasir,
     saleem, vance), max 4 per beat, most important first. "Zayaan" in the narration = `habeeb`. People without cards
     (fishermen, guards, soldiers, journalists, launch captains, police officers) are described in `visual` only. Don't
     put a character in `chars` who isn't visible (a phone/recorded voice is not visible; a distant back/silhouette is
     better described in text without the reference).
   - Write the outfit into `visual` whenever it differs from the card default (see the bible's character table:
     Ashham's black raincoat in 318, civilian clothes 320–322, police-cap-and-sunglasses disguise 322–323, black
     tactical jacket 324, dress uniform + medal in the epilogue; Raniya without the white coat after the hospital
     escape; Faahid's black tactical jacket in field operations). After the explosions people look "dusty and
     exhausted" — never wounded, never blood.
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Never
     use words like blood, wound, injury, gun, rifle, pistol, bullet, shoot, fire at, knife, syringe, needle, grenade,
     bomb (say "a small black case with a blinking red light"), kill, dead, body, corpse, torture, tied, chains, rope,
     handcuffs, punch, kick, slap, vomit, cigarette, tattoo (say "a black phoenix emblem drawn on a tablet screen") in a
     `visual`. Mark `sens=` / `safe=` for every substituted moment. Keep faces in the upper two-thirds and a calm dark
     lower third. Always state time/light in `MOOD` (night: cold navy-blue darkness with one warm or fluorescent light
     source; bunker: flat cold fluorescent white, red emergency light during the alarm; storm: black sea, white spray,
     lightning). Explosions only as distant spectacle (orange glow, smoke, fireball on the sea) with nobody in it.
     Remember "no person lying" — show people sitting up, kneeling or crouched instead.
   - `amb` must be one of: sea_boat, sea_search, storm_night, rain_night, rain_day, beach_night, beach_dusk,
     beach_day, beach_evening, dawn_exterior, island_day, island_night, jungle_night, jetty_day, night_exterior,
     office_day, office_quiet, office_night, mansion_day, mansion_night, street_night, road_busy, city_day,
     city_night_far, car_night, car_interior, room_night, room_day, home_night, home_day, living_night, hospital_night,
     hospital_corridor, hospital_room, icu_room, bunker_machinery, corridor_drip, alarm_corridor, vent_shaft,
     command_center, detention_room, storage_hall, chaos_hall, engine_room, warehouse_crowd, hall_crowd,
     prison_exterior, memory. (Bunker corridor → corridor_drip / bunker_machinery; lab alarm → alarm_corridor; server
     room → command_center; warehouse → storage_hall; Dhoonidhoo cell → detention_room; press hall → hall_crowd;
     ship deck in the storm → storm_night or sea_search.)
   - SFX names (only these): door_open, door_close, door_slam, creak, knock, lock_click, metal_door, footsteps_pavement,
     footsteps_sand, boots_march, phone_buzz, cup_clatter, glass_break, crash_clatter, metal_clang, flashlight_click,
     keyboard_typing, computer_beep, alarm_beep, siren, power_down, power_up, electric_spark, steam_hiss, engine_rev,
     boat_engine, dhoni_engine, car_approach, car_pass, brake_screech, car_door, distant_boom, fire_crackle, thunder,
     rain_start, wind_gust, wind_howl, wave_crash, splash, leaves_rustle, cloth_rustle, page_turn, paper_shuffle,
     camera_shutter, crowd_gasp, crowd_panic, gasp, sigh, sob_breath, breath, breath_heavy, heartbeat, soft_thud.
     Gain −12…−24 dB. The Dhivehi substring must occur in a word of that shot (plan_beats asserts it). Place SFX only
     where the narration mentions the action (engine → boat_engine/dhoni_engine; lights go out → power_down; alarm/
     self-destruct → alarm_beep or siren; keypad beep → computer_beep; steel door → metal_door; bullets hitting metal →
     metal_clang; offscreen gunshots/blows → at most soft_thud at −22…−24, sparingly; explosion → distant_boom;
     searchlight shattered → glass_break; camera flashes → camera_shutter; journalists' shock → crowd_gasp; thunder;
     splash for someone going into the sea; heartbeat for dread, sparingly). NO literal gunshot, scream or pain SFX.
     `hum=True` on emotional peaks/dread only. No music of any kind.
   - `transition="black"` for time jumps (night → morning, → next day, "an hour later", "three weeks later"),
     `transition="dissolve"` for memories (318's Naail call flashback), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/ProjectPhenix/episode-<N> pipeline/plan_phenix_<N>.py`, then
   `python pipeline/episode_characters.py output/ProjectPhenix/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/ProjectPhenix output/ProjectPhenix/episode-<N> beats`
   (resumable; run it in the background or with a long timeout and wait for it). Seven agents share the API: if it ends
   with FAILED beats from rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and
   logged.
5. **Review images**: run `python pipeline/beats_sheet.py output/ProjectPhenix/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (NO guns or gun-shaped objects in anyone's hands — the model likes to add rifles to
   soldiers and pistols to police: regenerate if you see one; no knives, syringes, handcuffs; no blood/red stains,
   bruises or wounds — especially on Ashham, Habeeb and Faahid after fights/explosions; nobody lying lifeless; no
   cigarettes; no tattoos; Raniya's hijab fully covering hair and neck — check hairlines — and her clothes opaque; no
   man touching Raniya; no letters/numbers on screens, timers, keypads, ID cards, containers, ship hulls, launches),
   characters match their cards (Ashham tall, stubble, navy field shirt by default; Habeeb glasses + grey zip jacket;
   Moosa white beard + gold glasses + navy suit/red tie; Naail styled hair + black bomber; Kalhe shaved head + cheek scar
   + black henley; Raniya white coat/dusty-blue dress + navy hijab; her father thin, white stubble, pale-grey clothes;
   Fairooz greying thick moustache + senior navy uniform; Faahid grey hair + white moustache + olive shirt; Naasir bald +
   goatee + black suit; Saleem silver hair + rimless glasses + black three-piece suit; Vance elderly European, silver
   slicked hair, black overcoat), the image fits its beat, no duplicated people, no extra copies of a lead, Ashham and
   Fairooz not confused (both wear navy). To fix one: adjust that beat's `visual` in the plan (or drop a
   confusing reference), delete `images/beat_XXX.png`, rerun plan_beats.py, then `gen_images.py ... beats beat_XXX`.
   At most 2 regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/ProjectPhenix/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/ProjectPhenix/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_phenix_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

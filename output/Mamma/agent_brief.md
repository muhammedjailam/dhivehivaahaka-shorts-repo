# Brief for an episode agent — Mamma episode <N>

You produce everything for ONE episode of the Dhivehi audio family drama "Mamma" (މަންމަ) up to (but NOT including) the
final video render. Project root: `D:\Projects\dhivehivaahaka-shorts` (Windows; use the Bash tool with Git Bash syntax,
ALWAYS use absolute paths or `cd 'D:/Projects/dhivehivaahaka-shorts'` inside the same command, and always
`export PYTHONIOENCODING=utf-8` before running python that prints Thaana). Five other agents are doing the other
episodes at the same time, so stay inside your own episode folder and your own plan file.

Series folder: `output/Mamma` (series name for scripts: `Mamma`). Your episode: `output/Mamma/episode-<N>`.

Read first:
1. `main prompt.txt` (the master spec — sections 3–8 and 12 matter most for you).
2. `output/Mamma/series_bible.md` (two timelines, synopses of all 6 episodes, character ids, places, outfit continuity
   and the 14 BINDING content rules — they override the literal narration. This is a domestic-abuse drama with a
   mother's death and burial, the loss of a newborn, childbirth by C-section, nursing, a husband's affair and a grieving
   12-year-old. NONE of the violence, injuries, blood, bodies, medical procedures, nursing or marital intimacy is ever
   shown — only the safe substitutes the bible lists).
3. `pipeline/plan_isq_484.py` as the format example of a plan file, and `pipeline/plan_beats.py` (how it is read;
   check which keys `BEATS` entries and `sh()` support).
4. Your transcript: `output/Mamma/episode-<N>/work/transcript.txt` (timestamped sentences) and the shot segmentation
   already made for you: `work/segments.json` (shot numbers, times, Dhivehi text). Read ALL of it.

Already done for you (do not redo): zip unpacked into `work/`, cover converted to `work/episode-<N>-cover.png`, logo PNGs
in `work/logo/`, `work/segments.json`, `work/transcript.txt`, series `style.txt`, `tail.txt`, `caption_style.json`, all 17
character cards and their `reference.png` in `output/Mamma/characters/` (look at `output/Mamma/refs_sheet.jpg`:
row 1 aamir, aamir_teen, ayya, azeeza; row 2 faathanikey, fiyaza, khadheeja, moosafulhu; row 3 naya, raamee, reysham,
shahula; row 4 shahula_child, shahula_young, suneetha, tholaal; row 5 zubair).

## Steps
1. **Understand** the episode (you read Thaana; translate for yourself). Write `episode-<N>/story_notes.md`: synopsis,
   characters table (series cards used; no new cards are created), locations, tone, image-budget line,
   sensitive-moments table (timestamp → safe visual). NOTE: the Write tool refuses `.md` files for subagents — write
   the file with python from Bash (put the text in a `.txt` scratch file first with the Write tool, then copy it with
   python, `open(..., "w", encoding="utf-8")`).
2. **Plan** `pipeline/plan_mamma_<N>.py` with `LOC`, `MOOD` (same keys as LOC), `BEATS`, and the shots via the
   `sh(i, english, [(sfx, dhivehi_substring, gainDb)], hum=True/False)` helper ending with `SHOTS = S` (copy the helper
   pattern from the example plan file). Every segment number 1..last must have a `sh()` entry with a faithful English
   translation. Rules:
   - New image only on scene/time/character/action change (spec 5.1); hold images with shots; `reuse="beat_00X"` when
     the story returns to an earlier image of THIS episode. Target ≈ 25–35 s of audio per new image (budget = your
     duration / 30 ± 20%); justify anything above that in story_notes. Long reflective/inner passages: hold the image
     and use shots (crops on faces, hands, the rain on a window, a lamp, the baby asleep).
   - Use the places from the bible consistently — write full descriptions into your `LOC` (you may split one place
     into several keys, e.g. azeeza_house_porch_night / azeeza_kitchen / marital_bedroom_night).
   - `chars` = card ids only (shahula, shahula_young, shahula_child, khadheeja, zubair, faathanikey, moosafulhu,
     azeeza, aamir_teen, aamir, ayya, raamee, tholaal, naya, reysham, suneetha, fiyaza), max 4 per beat, most important
     first. Use the right AGE card for Shahula/Aamir (bible: shahula_child at 12, shahula_young ~16–19 until the
     marriage, shahula from the marriage on and in 308's present-day opening; aamir_teen only in 350's island night).
     People without cards (baby Zidhaan, Bodudhaitha, Thahmeena, Leeza, Haneef, Fathumaththa, mourners, villagers,
     schoolboys, nurses, the canteen boy) are described in `visual` only. Don't put a character in `chars` who isn't
     visible (a phone voice or a voice in memory is not visible).
   - Write the outfit into `visual` whenever it differs from the card default (see the bible's continuity section;
     e.g. Shahula's black abaya + black hijab with white under-scarf in 308's present and 463's flight, lavender home
     dress, navy office abaya, peach restaurant dress; Aamir's light-blue office shirt / dark-grey home t-shirt / black
     restaurant shirt; Azeeza's cream house dress when ill). The model sticks to the reference outfit: when the outfit
     differs write "reference used for her/his face only; wearing <outfit>, NOT the <card outfit>".
   - `visual` must be concrete (composition, action, expression, light) and obey section 6 + the bible's rules. Never
     use words like blood, bleeding, wound, injury, bruise, slap, hit, punch, kick, grab, choke, throat, dead, body,
     corpse, funeral body, grave digging, labour, surgery, C-section, operation, breast, nursing, kiss, embrace, hug,
     bed together, knife in a `visual`. Mark `sens=` / `safe=` for every substituted moment. Keep faces in the upper
     two-thirds and a calm lower third. Always state time/light in `MOOD` (storm night: black sky, lightning, heavy
     rain, warm amber lamps; island day: soft hazy tropical light; Malé home happy: warm homely light; Malé home after
     the marriage: dim, cold, shadowy, a single lamp; memories of Khadheeja: soft warm hazy glow). Whenever a man and a
     woman who are not married share a beat, write "a clear arm's-length gap between them, not touching". Married
     Aamir & Shahula: never touching, never in bed together (bible rule 5).
   - `amb` must be one of: storm_night, rain_night, rain_day, sea_boat, jetty_day, beach_night, beach_dusk, island_day,
     island_night, island_house_day, island_house_night, village_day, village_night, night_lane, night_exterior,
     dawn_exterior, mosque_interior, street_night, road_busy, city_day, city_night_far, car_night, car_interior,
     home_day, home_night, living_night, room_day, room_night, kitchen_busy, cafe, courtyard_dinner, office_day,
     office_quiet, hospital_night, hospital_corridor, hospital_room, hospital_day, clinic_room, memory, memory_rain,
     balcony_night, garden_day. (Mosque porch in the storm → storm_night or rain_night; cemetery in rain → memory_rain
     or rain_day; Zubair's yard → island_house_day; Malé school street → city_day; restaurant → cafe; taxi → car_night;
     maternity ward → hospital_room.)
   - SFX names (only these): door_open, door_close, door_slam, creak, knock, lock_click, footsteps_pavement,
     footsteps_sand, phone_buzz, cup_clatter, glass_break, crash_clatter, page_turn, paper_shuffle, pen_scribble,
     cloth_rustle, motorbike_pass, car_pass, car_approach, car_door, car_drive_off, brake_screech, boat_engine,
     dhoni_engine, thunder, rain_start, wind_gust, wind_howl, wave_crash, splash, leaves_rustle, pour, gasp, sigh,
     sob_breath, breath, breath_heavy, heartbeat, soft_thud, doorbell_buzz, monitor_alarm. Gain −12…−24 dB. The Dhivehi
     substring must occur in a word of that shot (plan_beats asserts it). Place SFX only where the narration mentions
     the action (thunder/lightning → thunder; rain starts → rain_start; dhoni → dhoni_engine; knock → knock; door →
     door_open/door_close; slammed door → door_slam; phone rings → phone_buzz; motorbike → motorbike_pass; taxi →
     car_approach/car_door; water poured → pour; sobbing → sob_breath sparingly; gasp of shock → gasp; Aamir kicking
     the sofa / a blow → at most soft_thud at −22…−24, never more). NO scream, no baby-cry SFX, no music of any kind.
     `hum=True` only on emotional peaks (grief, the first blow, the lost baby).
   - `transition="black"` for time jumps ("the next morning", "a week later", "years passed", "after the wedding"),
     `transition="dissolve"` into and out of memories (308's flashback to age 12, Khadheeja's voice, 457's Raamee
     memory, 460's memories, 463's hospital flashbacks), default xfade otherwise.
   - Do NOT reuse images from other episodes (they are being made in parallel).
3. Run `python pipeline/plan_beats.py output/Mamma/episode-<N> pipeline/plan_mamma_<N>.py`, then
   `python pipeline/episode_characters.py output/Mamma/episode-<N>`.
4. **Images**: `python pipeline/gen_images.py output/Mamma output/Mamma/episode-<N> beats`
   (resumable; run it with a long timeout and wait for it). Six agents share the API: if it ends with FAILED beats from
   rate limits/network, wait a minute and run it again. Refusals are rewritten automatically and logged. If the API
   reports `credit_balance_exhausted` / billing errors, STOP and report — do not loop.
5. **Review images**: run `python pipeline/beats_sheet.py output/Mamma/episode-<N>` (writes `work/beats_sheet.jpg`)
   and LOOK at it (Read the jpg; zoom into single images when unsure). Check: section-6 + bible rules (no hand raised,
   no grabbing, nobody touching — especially Aamir and Shahula, Aamir and Reysham, Tholaal and Naya, Raamee and teen
   Shahula; no red marks, bruises, blood or a split lip on Shahula's face; no knife at Zubair's fish; no body/face of the
   dead, only the white-shrouded bier from a distance; no baby being nursed; no couple in bed; every woman's and girl's
   hijab fully covering hair and neck — check hairlines — and clothes opaque and loose; no letters/numbers on papers,
   forms, phones, signs, headstones), characters match their cards and the right age card is used (Shahula soft oval
   face and big dark eyes; Aamir handsome, styled hair, light stubble; Azeeza emerald abaya + gold glasses; Zubair
   greying beard + checked shirt + sarong; Faathanikey plump in maroon), outfits match the bible's continuity, the image
   fits its beat, no duplicated people, no extra copies of a lead, the baby looks like a healthy few-months-old baby
   (newborn in 463's birth flashback). To fix one: adjust that beat's `visual` in the plan (or drop a confusing
   reference), rerun plan_beats.py, then regenerate INTO PLACE: rename the old image to `images/beat_XXX.old.png`
   (keep it until the new one exists), run `gen_images.py ... beats beat_XXX`, then delete the .old file. At most 2
   regenerations per beat; log why in story_notes.
6. **Sound**: `python pipeline/sound.py output/Mamma/episode-<N> <N>` (writes audio/final_mix.wav, prints loudness;
   −14 LUFS / ≤ −1.5 dBTP expected).
7. **Captions sidecar**: `python pipeline/export_ass.py output/Mamma/episode-<N> <N>`.
8. Do NOT run `render_beats.py` or `qc.py` — the coordinator renders all episodes one after another.
9. Do NOT edit any shared file in `pipeline/` other than your own `plan_mamma_<N>.py`, and do not touch other
   episodes or the character cards/references. If a shared script blocks you, stop and report the error.
10. Never print or write the OpenAI key (it is read from env.txt by gen_images.py).

## Final report (your last message, concise)
beats / shots / new images / in-episode reuses / seconds of audio per new image; refusals and how they were rewritten;
regenerations and why; loudness from sound.py; anything a human should double-check (with beat ids). Confirm these
files exist: story_notes.md, scenes.json, characters.json, images/, generation_log.jsonl, audio/final_mix.wav,
captions.ass, work/beats_sheet.jpg.

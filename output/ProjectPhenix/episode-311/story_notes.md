# Project Phenix — episode 311 (part 1 of 7) — story notes (v2 re-cut on the new audio)

## Synopsis
Sunset off Kandu-huttaa, a deserted island in the north of Huvadhu (GA) atoll. On the fishing dhoni "Kalaminja", Hassan spots
a big black thing floating; Sameeru the cook slows the engine; Ibrahim and Ali come to the bow ("resort rubbish, leave it").
Hassan sees strange fish around it and smells something; he hooks it with a pole. It is unnaturally heavy; four men haul the
black, tape-wrapped plastic bundle aboard. Hassan cuts the tape; the stench; Ali retches over the side; Ibrahim asks if it is
an animal's meat. Inside: the tortured remains of a man. Sameeru: "Ya Rabbi! Call the police, switch on the set!" Night falls.

MALÉ, Iskandhar Building: Ashham (tall, strong, the Serious Crimes Department's best investigator) at his cluttered desk; traffic
on Ameenee Magu. Habeeb (data analysis / digital forensics) brings a message from the southern command: a man found dead near a
deserted island in GA, brutally tortured — clearly a "message" killing. The remains are being taken to Villingili; HQ wants
Ashham on it because of a tattoo on the back: a black phoenix. Ashham recognises it: Naail Moosa, younger son of tycoon Moosa
Thaahir — nightlife, car races, suspected drugs — missing a week. Habeeb: "This is no gang fight; there's a big secret behind
it." Ashham: prepare the trip, gather Naail's medical and criminal records, we leave tonight.

MOOSA'S MANSION: luxury, and a broken father on the sofa (once called "Qaasim" by the narrator — same man). DNA pending, but the
tattoo matches. Naail always had bad friends; two weeks ago he was frightened, said he had found out a big secret and that
"those people are in Malé too". Moosa weeps: find my son's killers, any sacrifice. Ashham puts a hand on his shoulder. The
killing was a warning: say nothing, touch nothing, reveal nothing.

2:30 AM: the police fast launch "Sea Hawk" leaves Kooddoo (the team flew in to Kooddoo airport) for Kandu-huttaa on a rough sea.
Ashham and Habeeb sit silent by the forensic cases; backup police and soldiers stand by. Habeeb (laptop): Naail's phone died in
Malé a week ago; before that he often called the atoll hospital's number — but that island's systems are blocked. Ashham stares
into the dark: the most dangerous case of his life. Captain: half an hour to go. Ashham: the island first.

DAWN: Sea Hawk enters the lagoon of a beautiful, eerily silent jungle island: white beach, screwpine and magoo, no path, no
people. Ashham and Habeeb land with forensic kits, extra police and two soldiers. East side: boot prints and bare footprints out
of the bushes, a black launch-engine oil stain (Habeeb rubs the sand between two fingers), dried blood on branches — Ashham bags
a twig: "He was killed here; this is the crime scene." In the jungle: trees bent and tied, Ashham cuts the cord; a heap of dry
fronds ("a rubbish pit?" — "On a deserted island? Clear it!"). Under the sand: a heavy steel door of a concrete underground
bunker with a big padlock. "A bunker on a deserted island?" — "This is where a huge crime is run; Naail's secret." Then the roar
of a fast launch approaching; they hide in the bushes; someone knows the police came and is coming after them. (To be continued.)

## Characters (series cards only; no new cards created)
| id | role in 311 | beats (v2) |
|---|---|---|
| ashham | lead investigator; default navy field shirt throughout | 011–016, 018–023, 025, 027–029, 031–038 |
| habeeb | data/forensics analyst (narrator's "Zayaan"); default grey zip jacket, glasses | 012–016, 019, 027, 031–033, 035–038 |
| moosa | grieving tycoon ("Qaasim" in shot 40) | 021–025 |
| naail | the victim — shown ONLY alive, in Ashham's memory (dissolve) | 017 |
No-card people described in `visual` only (speaker ids in scenes.json in brackets): fishermen Hassan [hassan], Sameeru
[sameeru], Ibrahim [ibrahim], Ali (beats 001–010); the launch captain [captain] (029); police officers and two soldiers with
empty hands (030, 031, 035, 038).

## Locations (LOC keys)
dhoni_sunset / dhoni_dusk (the dhoni off Kandu-huttaa), police_office (Iskandhar Building), naail_memory (Malé seafront at
night, memory), moosa_mansion, sea_launch (exterior, 2:30 am), launch_cabin (interior), kandu_lagoon (dawn), kandu_beach (east
beach, morning), kandu_jungle (jungle, nothing man-made), kandu_bunker (the hatch spot).

## Tone
Slow-burn dread: a red sunset turning to night over the sea, a weary office at dusk, a dim golden mansion of grief, a cold navy
launch at night, and a beautiful but deadly silent island at dawn. No music; sea, wind, engine, office and jungle ambiences;
hums only on the discovery, Sameeru's cry, the phoenix photo, Moosa's tears, Ashham's foreboding and the bunker reveal/launch.

## Image budget
New audio 830 s (13.8 min; v1 was 746 s). 38 beats, 86 shots. 32 distinct images = 26 v1 images reused (copied, no API call) +
6 new images; 6 in-episode reuses (shot / reverse-shot returns: beat_005 = beat_002 Hassan; beats 015, 019 = beat_013 Habeeb;
beats 018, 020 = beat_014 Ashham; beat_024 = beat_022 Moosa) → 25.9 s of audio per image, well inside the soft max (≈44).
v1 beat_015 (Ashham and Moosa talking side by side) is no longer used: both faces sit at the frame edges (x≈22 / x≈79) and every
shot of that conversation is dialogue, so it was replaced by the over-the-shoulder pair beat_022 / beat_023. v1 beat_021
(reuse of the launch exterior after the captain) is dropped: shot 64 now goes straight to the dawn lagoon.
Longest hold: beat_027 (67 s, the cabin conversation about Naail's phone — 7 shots alternating tight crops on Habeeb x≈31 and
Ashham x≈68 per speaker); beat_024 (51 s, Moosa's lines, 5 shots of alternating tight/medium crops).

## Dialogue focus (spec 5.4)
46 shots carry a `speaker`: ashham 18, habeeb 11, moosa 8, hassan 3, ibrahim 3, sameeru 2, captain 1. 19 are centred on a
NEW image framed on the speaker, 27 by a tight/medium crop with `focus` on a v1 image (face positions read off the 10 % grids).
Mixed shots (two voices in one segment) take the speaker with most of the words: 25 and 35 (Habeeb), 36 (Ashham — "Ashham
stood up. Habeeb, prepare the trip"), 40 and 45 (Moosa), 54 (Ashham's question), 82 (Ashham's reply to Habeeb's "a bunker?").
Shot 57 is Ashham's thought (speaker ashham). Shot 33 ends with Ashham's first word ("This is…") over the Naail memory — left
without a speaker. Shot 61's captain line starts after a narration question; the shot is cropped on the captain (x≈59).

## v2 re-cut — new images
| beat | shots | reason |
|---|---|---|
| beat_002 | 3, 7 (reuse beat_005) | 5.4: Hassan calls out / says the fish are circling — in v1 he is a profile (beat_002) or at the left edge x≈22 (beat_003); new medium close-up, Hassan three-quarter at x≈40 |
| beat_008 | 12–13 | 5.4: Ibrahim asks "is this some animal's meat?" — in v1 beat_005 he is at x≈14; new close-up, Ibrahim x≈47, Sameeru soft at the side, Ali from behind at the rail |
| beat_013 | 24–26, 29, 35 (reuses 015, 019) | 5.4: Habeeb's report — in v1 beat_009 he is at x≈20 and in beat_010 at x≈83; new over-the-shoulder image, Habeeb x≈43, Ashham soft at the right edge |
| beat_022 | 40, 43–47 (reuse 024) | 5.4: Moosa's lines — v1 beat_015 has him at x≈22; new over-the-shoulder image, Moosa x≈56, Ashham soft at the left edge |
| beat_023 | 41–42 | 5.4 reverse shot: Ashham answers/questions Moosa — v1 beat_015 has him at x≈79 in profile; new over-the-shoulder, Ashham x≈34 |
| beat_033 | 73–74 | 5.4: Habeeb names the launch engine oil — v1 beat_024 has him at x≈74 looking down; new medium close-up, Habeeb x≈46 holding up the oily sand |
No fixes of v1 images were needed (no bible-rule breaks found on the v1 sheet). All 6 new images passed on the first call:
0 refusals, 0 regenerations (~$0.12).

## Sensitive moments (new timestamps)
| time | narration | safe visual |
|---|---|---|
| 64.6–96.4 s (beat_006) | hauling the heavy bundle aboard | closed black tape-wrapped plastic bundle only; men straining, disgust |
| 96.4–122.2 s (beats 007–008) | Hassan cuts the tape; stench; Ali retches; "animal's meat?" | bundle stays closed / out of frame; hands over noses; Ali seen only from behind at the far rail |
| 122.2–152.1 s (beat_009, shot 16 on beat_010) | the bag opened: a leg, a tortured man, neck wounds | ONLY Hassan's horrified face, then Sameeru shouting at the radio set; nothing of the remains |
| 216.5–267.7 s (beats 013–014) | "brutal torture murder, limbs cut off", a message killing | grave faces of Habeeb and Ashham in the office |
| 275.0–294.5 s (beat_016) | the phoenix tattoo on the back of the deceased | a black phoenix emblem drawn on a tablet screen held by Habeeb |
| 294.5–313.6 s (beat_017) | Naail: nightlife, car races, suspected drugs | Naail alive, leaning on a sports car on a seafront road (memory, dissolve); no club, no drugs |
| 455.9–478.0 s (beat_025) | Ashham's hand on Moosa's shoulder | men — allowed |
| 659.3–670.1 s, 810.0–817.8 s (beats 031, 038) | soldiers "with weapons" | soldiers and police with empty hands |
| 708.0–735.8 s (beats 033–034) | dried blood on branches | Habeeb with oily sand, then Ashham placing a plain broken twig into a clear evidence bag |
| 735.8–753.7 s (beat_035) | trees bent and tied, Ashham cuts the cord | bent palms held by frayed palm-fibre twine; Ashham pulling them apart; no blade |

## Sound notes
amb: sea_boat (dhoni + launch), office_day, memory, mansion_night, dawn_exterior, island_day. SFX on narrated actions only
(substrings re-checked against the new wording): wind_gust, dhoni_engine, footsteps, splash/soft_thud (bundle against the hull /
onto the deck), cloth_rustle (tape), gasp + heartbeat (the discovery), flashlight_click (the set switched on, "ހުޅުވާ"),
car_pass, door_open, creak, computer_beep, sob_breath, boat_engine, wave_crash, keyboard_typing, footsteps_sand, leaves_rustle,
metal_clang (padlock), heartbeat (closing dread). No retching sound, no scream. Loudness: −14.0 LUFS integrated, −1.5 dBTP.

## Notes for a human check
- v1 beats now 031 and 038 (old 023/029) still include one female police officer in navy uniform and hijab among the extra
  police (modest, accepted in v1 too); v1 beat_004 (now 006) shows five men hauling the bundle (story: four).
- beat_008: Ibrahim's hand is at his mouth/chin while he asks — face visible, three-quarter.
- beat_022: Ashham's foreground shoulder is large and dark (left third); the tight crops at x 56 keep Moosa centred.

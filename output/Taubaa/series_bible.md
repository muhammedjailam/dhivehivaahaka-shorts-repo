# Taubaa (ތައުބާ, "Repentance") — series bible

An ANTHOLOGY: every episode is a separate, true-style story of a person who returns to Allah (narrated in Dhivehi,
mostly translated from Arabic/Saudi sources). Each episode has its OWN cast; characters do not recur across episodes.
Episodes end with "(ނިމުނީ)" ("the end"); many end with a Quran verse or a dua.

Series look: `style.txt` (reflective, spiritual; deep teal / smoky steel-blue with warm amber lamplight and dawn-gold
accents — matches the cover: a silhouetted man with his head in his hand against blue haze). Caption highlight pill =
deep amber #A8661A (`caption_style.json`). The per-series prompt tail is in `tail.txt` (gen_images.py reads it).
Cover = `work/episode-<N>-cover.png` (same for every episode).

## Setting / look decision (binding)
The master prompt says "all characters look Maldivian". That rule is applied where the story's setting is unstated
(ep 287 → a simple Maldivian home). Where the narration explicitly places the story in Saudi Arabia (ep 298 Jawad,
"go back to Saudi"; ep 299 Riyadh, Makkah) we stay faithful to the narration: Saudi Arab characters in modest Saudi
dress (men: thobe, ghutra/shemagh; women: black abaya + hijab). All modesty rules still apply in full.

## Characters (ids = folders in `characters/`)
| id | episode | who |
|---|---|---|
| tv_son | 287 | the only son, early 20s, charcoal long-sleeved t-shirt, navy track trousers |
| devout_mother | 287 | his frail elderly mother, sea-green libaas, white headscarf |
| jawad | 298 | Saudi man, early 30s, trimmed beard; abroad: navy zip jacket + grey shirt; in Saudi: white thobe (say so in `visual`) |
| jawad_wife | 298 | his pious wife, black abaya, dusty-rose hijab |
| riyadh_boy | 299 | the narrator aged ~14–17, white thobe, no headdress |
| riyadh_man | 299 | the same narrator aged ~18–22, gaunt, patchy beard, rumpled off-white thobe |
| pious_father | 299 | his very religious father, long white beard, red shemagh, brown bisht |
| elder_brother | 299 | eldest brother, early 40s, full black beard, white ghutra |
| nephew | 299 | elder brother's son ~19, light-grey thobe |
| clinic_doctor | 299 | private-clinic doctor ~50, white coat, rimless glasses |
| righteous_friend | 299 | pious young man who takes him to umrah, white thobe + ghutra |

No cards (describe in text only): bad friends (always as shadowy figures from behind / silhouettes, faces not shown),
religious friends of Jawad (men in white thobes, seen at a respectful medium distance), the elder brother's family at
dinner (only men/boys in view, or women fully in abaya + hijab seen from behind), lorry driver, taxi driver, police,
crowds of pilgrims, the narrator who meets the man of ep 299 in a Riyadh mosque.

## Episode synopses
- **287** (~3 min) A young man lives with his old mother in a small house; spends his nights watching films and dramas
  on TV, never goes to the mosque, mocks his mother whenever she reminds him to pray. She has nothing but dua: every
  night in the last third of the night she raises her hands and prays, weeping, for his guidance. One silent night a
  loud crash; she runs crying "my beloved son!" to his room — he is smashing the TV with a tool, saying it kept him
  from Allah, his mother and his prayers. He goes to her, kisses her head and hugs her; she weeps tears of joy. Allah
  answered her dua. Ends with Al-Baqarah 2:186 ("I am near; I answer the call of the caller when he calls").
- **298** (~6.5 min) Jawad (Saudi) tells his own story: deep in haram (alcohol, zina, dancing) which he loved. Travelled
  Greece → France → Holland → Canada → America; ~3 years in America, only one Friday prayer in a mosque. His pure
  fitrah and upbringing called him to Allah, but Shaytan made him forget. Religious friends visited him; he admired
  them, yet went to discos and nightclubs every weekend; at first did not drink, then fell into it. Returned home,
  married a kind, religious woman from a pious family, took her to America, secretly went back to his old ways;
  married bad friends advised him to rent an apartment for sin; he refused, told his wife "we must go back to Saudi as
  soon as possible, I can't bear it any more". Friends tried to change his mind; he said no, graduated, came home —
  yet continued the same life, travelling for tourism to nightclubs. About a year later, by Allah's decree, he found
  in his car an audio tape of Sheikh Ali Jaber: Quran verses and the qunut dua. Morning, on the way to work, he broke
  down crying like a child, pulled over at the roadside, sobbed; felt as if hearing Allah's verses for the first time;
  his whole being cried "Kill Shaytan and desire, O Jawad! Repent! Don't miss the chance!" He repented, resolved never
  to return; slowly his life, appearance and character changed; he guards his prayers. Asks Allah to accept his
  repentance and grant everyone a good ending.
- **299** (~12 min) Told to the narrator in a Riyadh mosque by a young man. Grew up in a very religious home in a
  Riyadh district; father allowed no entertainment devices. At 14 a group of bad friends trapped him during exam time:
  "white pills" to stay awake; he stayed up night after night studying, passed with high marks, kept taking them,
  became exhausted; then "red pills" to sleep — ~10 a day for 3+ years; failed school, moved school to school. Decided
  to move to his eldest brother's town to finish school; on a cold winter night took his father's new car without
  asking, stopped with friends, took a huge dose; before dawn drove off and crashed under a big lorry. Woke in hospital,
  right leg broken, many wounds, 48 hours in ICU — still didn't wake up spiritually; at his father's house in Riyadh
  friends kept bringing pills. Later, on crutches, after Asr, tried to stop cars, then hired a taxi at a taxi stand to
  the brother's town; enrolled in middle school, got his certificate; switched to alcohol, sold the pills at double
  price for money, then hashish (smoked like tobacco); went to school like a fool; lived alone in an isolated house at
  the edge of town. One day two friends took him driving around town for hours after Asr; dropped back at his car, he
  was too intoxicated to find his house for 2+ hours; found it, felt a violent pain in his chest; remembered death for
  the first time in years — death seemed to stand before him. Ran to do wudu twice, prayed two rakaat (al-Fatiha +
  al-Ikhlas), lay on his left side then turned to his right side awaiting death; his body shaking, his sinful life
  flashing by. Suddenly his foot moved — hope. Drove to his elder brother's house, family gathered for dinner; he
  collapsed among them; brother: "What happened?!" — "My heart hurts badly." Nephew drove him to a private clinic;
  alcohol 94%; the doctor refused, wanted the police, finally agreed after pleading and money; ECG, treatment. His
  father, in town, came, stood at his bedside, smelled him, chest tightened, left without a word. Doctor warned him.
  He left feeling a new life. Afterwards: every whiff of hashish reminded him of death and he put out the cigarette;
  at night felt someone calling "Wake up!"; trembling, remembered death, paradise, hell, the grave, and two bad friends
  who had died; began night prayer and guarding fard prayers, ~4 months. Finally Allah sent a righteous young man who
  rescued him from the bad people and took him to Makkah for umrah; he wept, begged forgiveness at the Kaaba. Advice to
  Muslim youth: beware of bad friends. Dua for all sinners; Allah is Oft-Returning, Most Merciful.

## Content rules specific to this series (on top of `main prompt.txt` section 6 — binding)
- **Drugs, pills, alcohol, hashish, cigarettes, nightclubs, discos, dancing, zina**: NEVER shown, not even bottles,
  glasses, pills, blister packs, smoke, neon club signs or dancers. Use: the person alone at night by a window with
  city lights far away; a dark street with blurred distant lights seen from a parked car; a closed fist; shadowy
  friends from behind; an empty unmade room in grey dawn light; a clock; a mirror reflection of a hollow-eyed face
  (fully clothed); airport departure gate / plane wing / skyline for travel; a lone figure walking away down a wet
  street. Never depict women in any nightlife context.
- **The crash (299)**: no wreck, no lorry impact, no injuries/blood. Show: headlights in winter fog on an empty highway
  before dawn → (black transition) → hospital ICU monitor glow with the young man lying covered by a blanket up to the
  chest, leg in a clean white cast, no wounds; or just the empty road at dawn.
- **TV smash (287)**: show the moment with the son standing over a cracked, dark TV screen, tool lowered at his side, or
  the aftermath (broken screen on the floor). No person is harmed. The mother may be shown in the doorway.
- **Mother–son hug (287)**: mahram, allowed: son kissing his mother's forehead/head, gentle embrace, both fully clothed.
- **Near-death (299)**: no gore; show him lying on his right side on a prayer rug in a dim room, eyes closed, sweat on
  the brow; then praying; then the foot moving shown as a close-up of a bare foot on a rug in a shaft of light.
- **Wudu in a bathroom (299)**: show only hands under a running tap at a simple washbasin, or a closed bathroom door.
- **Prayer**: respectful, correct posture (standing with hands folded, ruku, sujood on a prayer mat facing a plain wall).
  Never render Arabic/Quranic text, never show a Quran page with readable script (closed Quran on a stand is fine).
- **Sheikh Ali Jaber** (real person): never depicted. Show the audio cassette in the car's tape deck, a car dashboard,
  morning light through the windscreen.
- **Quran verses / dua passages**: symbolic imagery — raised hands at dawn, a minaret against the sky, light rays, a
  prayer mat, the sky over the desert.
- **Makkah / umrah (299)**: Masjid al-Haram and the Kaaba may be shown at a respectful distance with crowds of pilgrims;
  men in white ihram covering BOTH shoulders; no close-ups of strangers' faces. Never depict prophets or sacred figures.
- **Couples (298)**: Jawad and his wife only side by side, fully clothed, no touching beyond walking side by side; she is
  always in abaya + hijab.
- Bad friends: silhouettes / from behind / faces in shadow, never glamorised.

# Aliflaila - episode 532 (Night 6) - story notes

## Synopsis
Night Six of the Thousand and One Nights. Story levels: FRAME (Shahryar's chamber, night then dawn) and TALE
(Shahrazad's tale of the Fisherman and the Jinni, opening part). There is no tale-within-the-tale in this episode.

- FRAME, night (0-90 s, shots 1-9): night six falls over the palace. The king is impatient for the tale promised on
  Night Five. Dunyazad asks her sister for it, Shahrazad bows and asks permission, and the king says "Begin at once!"
- TALE (90-667 s, shots 10-72):
  - A very poor old fisherman with a wife and three children keeps a strict rule: four casts of his net a day.
  - One morning before sunrise he walks to the shore and wades in.
  - Cast 1: a rotting dead donkey. Cast 2: a clay pot full of mud (he weeps and recites a lament). Cast 3, in deeper
    water: broken glass, bones and shells.
  - He kneels and prays tearfully for his hungry family. Cast 4 snags on the seabed, so he dives to free it.
  - The net holds a heavy, polished brass jar with a lead stopper stamped with Prophet Sulaiman's seal. He dreams of ten
    dinars, then grows curious and prises the stopper off.
  - Black smoke darkens the sky and forms a colossal jinni (long description, shots 63-66). The fisherman falls back,
    speechless.
  - The jinni roars the Shahada, bows to the ground and begs "Sulaiman" not to kill him.
- FRAME, dawn (667-758 s, shots 72-82): golden dawn and the Fajr call, so Shahrazad stops. The king demands to know why
  the jinni called on Sulaiman. She promises the jinni's secret and the fisherman's cleverness for tomorrow night. He
  spares her again, dresses and goes to the court. The executioner's sword is put off one more day; the seventh night
  is next. Cliffhanger.

## Characters (series card ids; no new cards)
| id | who | beats | notes |
|---|---|---|---|
| shahrazad | storyteller | 002, 003, 029, 030 | saffron-gold gown, ivory headscarf |
| dunyazad | her little sister | 002, 003, 029, 030 | on the carpet beside her |
| shahryar | the king | 002, 003, 029, 030, 031 | on the divan an arm's length away; empty-handed in the throne hall |
| fisherman | poor old fisherman | 004-027 | patched blue tunic; wades IN his tunic |
| jar_jinni | jinni of the brass jar | 024, 026, 027 | indigo smoke tail, midnight-purple robe, golden eyes, empty hands |
| (no card) | fisherman's wife + 3 children | 004 | small figures; wife in a plain brown gown and a brown headscarf covering hair and neck |
| (no card) | courtiers | 031 | small background figures |
| (never shown) | Prophet Sulaiman, the executioner | - | seal = abstract rosette; sword never drawn |

## Locations
- Palace exterior at night (beat 001, reused for the closing beat 032)
- Chamber at night (beats 002-003); chamber at dawn (029-030)
- The poor hut by the beach (004-005)
- The shore: before sunrise (006), sunrise (007-012), morning (013-022), underwater (018)
- The shore darkened by the smoke (023-027)
- The city of domes at dawn with a minaret silhouette (028)
- The throne hall in the morning (031)

## Tone
Opening: hushed storytelling. Middle: patient struggle, sorrow and devout hope. Then wonder at the jar, then awe and
terror as the jinni appears. Ending: suspense and relief at dawn.

## Image budget
758 s / 27 = 28 images (allowed range 22-34). Plan: 32 beats, 28 new images, 4 in-episode reuses:
- beat_010 reuses beat_007 (second cast)
- beat_017 reuses beat_008 (hauling)
- beat_026 reuses beat_024 (the jinni roars)
- beat_032 reuses beat_001 (night palace, "the seventh night is next")
That gives 27.1 s of audio per new image.

## Sensitive moments
| time | narration | safe visual |
|---|---|---|
| 157-166 s (shot 17) | takes off his outer garment to wade in | wades in his full tunic; the beige outer wrap lies folded on the sand (rule 12) |
| 207-241 s (shots 22-25) | a dead, rotting donkey in the net | net heavily tangled and its contents hidden by mesh, seaweed and foam; he recoils pinching his nose (rule 8) |
| 322-341 s (shots 35-36) | broken glass bottles, bones | shells, seaweed, pebbles and driftwood in the net (rule 8) |
| 342-385 s (shots 37-41) | tearful kneeling prayer | kneeling on the sand facing the sea horizon, palms raised, golden light (rule 9) |
| 436-470 s (shots 48-50) | the seal of Prophet Sulaiman | abstract glowing eight-petalled rosette on the lead stopper, no letters, no star; Sulaiman never depicted (rule 9) |
| 520-547 s (shots 57-58) | prises the lid with a small knife | bare hands and a flat beach stone; no knife anywhere (rule 1) |
| 547-667 s (shots 60-72) | black smoke, terrifying giant jinni, "do not kill me" | fairy-tale glittering indigo smoke; colossal jinni with empty hands; fisherman's reaction shot; the jinni bows toward empty sand (rule 7) |
| 667-678 s (shot 73) | Fajr call to prayer | distant minaret silhouette at dawn; no adhan sound (rule 9) |
| 733-754 s (shot 81) | the executioner's sword postponed | the king calmly climbing to his throne, empty-handed; no executioner, no sword (rules 1, 3) |
| frame beats | chamber scenes | all three fully dressed; the king on the divan an arm's length away; headscarves cover hair and neck (rules 4, 5) |

## Sound
Ambiences:
- palace_night: beats 001-003 and 032
- village_day: the hut
- seashore_dawn: until the second haul
- seashore_day: from the third cast to the end of the tale
- mosque_dawn: beat 028 (birds only, no adhan)
- palace_dawn: beats 029-030
- throne_hall: beat 031

SFX are placed only on the matching words: net_cast, splash, breath_heavy, sob_breath, smoke_whoosh, magic_shimmer,
thunder (the jinni's roar), and others. hum=True is set only on the lament, the prayer, the jinni's appearance, the
fall and the plea.

## Image review log
- First pass: 28 images, 28 API calls, 0 refusals, all accepted on attempt 1.
- Contact sheet checked:
  - no knife, sword or weapon anywhere (beat_022 uses a flat stone and bare hands);
  - the donkey is hidden in the tangled net (beat_009);
  - the seal is an abstract petalled rosette with no letters (019, 021, 022);
  - Sulaiman is never shown; the jinni is empty-handed in 024 and 027;
  - the hand-drawn princess-film style is consistent; the characters match their cards.
- Regenerations (1 each):
  - beat_004: the two little daughters showed some hair at the forehead under their scarves. The children were changed
    to three small sons in white skullcaps (the narration does not give their sex). Fixed.
  - beat_031: rows of women were standing in the throne hall, some with hairlines visible. Changed to male courtiers in
    turbans only, nobody holding anything. Fixed.
  - beat_030: tried to fix Dunyazad's hairline by asking for her scarf pulled low over the forehead. A thin dark strip
    of hair still shows at her forehead. It comes from her series reference card, which shows the same strip, and it
    also appears in beats 002, 003 and 029. This is left for the coordinator, because the card and references are
    off-limits to episode agents.
- Sound: sound.py measures -14.0 LUFS integrated and -1.5 dBTP true peak, with 40 SFX cues.


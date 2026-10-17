# Aliflaila (އަލިފުލައިލާ — One Thousand and One Nights) — series bible

Dhivehi audio drama retelling the Arabian Nights, drawn in the **classic hand-drawn 2D animated princess-film style**
(the user's explicit request: "make the animation style like Disney Princess animations"). Every image must look like a
frame from a late-1980s/1990s hand-drawn animated fairy-tale musical: clean ink lines, soft cel shading, big expressive
eyes, flowing silks, painterly backgrounds, magical sparkles and glows (see `style.txt`). Never photoreal, never 3D CGI,
never anime. Do NOT write the words "Disney", "Aladdin", "Jasmine", "Genie", "Jafar" or any film/character names in
prompts — describe the look instead (the jinn must not look like any famous film genie).

Story order (site episode ids = consecutive nights; one continuous arc):
**452 → 470 → 486 → 498 → 509 → 532 → 551 → 569 → 585 → 599**.
Every cover (`work/episode-<N>-cover.png`) is identical: Shahrazad kneeling on a carpet telling a story, Dunyazad
behind her, King Shahryar brooding on a divan, a moonlit city of domes through an arched window, brass lanterns.
That midnight-blue + amber-lantern palace bedchamber is the series' signature FRAME setting.

## Story levels (make them visually distinct)
- **FRAME** (start and end of every episode): Shahryar's palace chamber at night → dawn. Midnight-blue night with warm
  amber lanterns; the episode ends with golden dawn light through the arched lattice window (the Fajr call to prayer =
  a distant minaret silhouette against the dawn sky; the adhan is NOT synthesised).
- **TALE** (Shahrazad's story): full-colour fairy-tale world (desert, oasis, seashore, cities, palaces). Enter and leave
  the tale with `transition="dissolve"`.
- **TALE-WITHIN-THE-TALE** (an old man's or the fisherman's own story; King Yunan's tale): same look but with a softer,
  warmer "storybook glow" (state "soft golden storybook glow" in `visual`). Dissolve in and out.

## Episode synopses
- **452 (Night 1, 18.9 min):** Just King Shahryar of the Sasanian lands invites his brother Shah Zaman (King of
  Samarkand). Shah Zaman discovers his wife's betrayal and kills her and her lover; travels in silent grief; at his
  brother's palace he sees Shahryar's queen betray him in the garden; tells Shahryar, who sees it too. Shahryar has the
  queen and her servants executed and decrees a new bride every night, beheaded each morning by the Grand Vizier; three
  years of grief, families flee. The Vizier's elder daughter Shahrazad (learned, 1000 books) insists on marrying the
  king; her weeping father gives in; she coaches little Dunyazad. Wedding night: Dunyazad is brought in, asks for a
  story; the tale of **the Merchant and the Jinni** begins (merchant eats dates under a tree by a spring, throws the
  stones, a giant jinni rises from smoke: a stone killed his invisible son). Dawn cuts it off; the king spares her for
  one day; the Vizier rejoices.
- **470 (Night 2):** The merchant begs a year's grace, swears by God to return; the jinni sinks away as smoke. Home: joy,
  then mourning; a year settling debts, charity, freeing slaves, his will. He returns to the tree with his shroud, recites
  Quran. The First Old Man arrives with a gazelle, then the Second Old Man with two black dogs. Sandstorm; the jinni
  appears; dawn cliffhanger.
- **486 (Night 3):** The First Old Man stops the jinni and offers his tale for a third of the merchant's life. The
  gazelle is his wife (his cousin): childless 30 years, he took a young second wife who bore a son; the jealous wife
  learned sorcery while he travelled, turned mother and son into a cow and a calf. At Eid al-Adha the cow is sacrificed;
  the calf weeps at his feet, he spares it. The herdsman's daughter breaks the spell (water + words), marries the son,
  turns the wife into the gazelle. The jinni grants a third; the Second Old Man steps up; dawn.
- **498 (Night 4):** The Second Old Man's tale: the two black dogs are his elder brothers, who twice lost their
  inheritance at sea and were helped by him; on a voyage together he married a poor woman on an island (a good Muslim
  jinniyya); the jealous brothers threw the couple overboard at night; she flew him to safety, wanted to kill them, he
  begged mercy, she sank their ship (everyone else saved) and turned them into dogs for ten years. The jinni grants the
  second third; the Third Old Man (with a mule) steps up; dawn.
- **509 (Night 5):** The Third Old Man's tale: the mule is his wife, a secret sorceress; returning home secretly he
  found her with another man; she turned him into a dog with spelled water; he hid in the streets; a kind old
  fish-seller took him in; the fish-seller's veiled daughter restored him and gave him water to turn his wife into a
  mule. The jinni frees the merchant entirely and vanishes; the merchant hugs the old men and goes home. Shahrazad teases
  the Fisherman and the Jinni; dawn.
- **532 (Night 6):** The poor old fisherman (wife, three children) casts four times a day: a dead donkey, a mud pot,
  broken glass and bones, then a sealed brass jar with Prophet Sulaiman's seal. He opens it; black smoke forms a colossal
  jinni who cries the Shahada and begs "Sulaiman" not to kill him. Dawn.
- **551 (Night 7):** The jinni (Sakhr) learns Sulaiman died ages ago and vows to kill his rescuer — his backstory:
  defied Sulaiman, captured by the vizier Asif ibn Barkhiya, sealed in the jar, thrown into the sea; his vows changed
  over four centuries. The fisherman pleads, then tricks him: "you never fit in that jar" — the jinni turns to smoke,
  flows back in, the fisherman slams the lid. Dawn.
- **569 (Night 7–8):** The trapped jinni begs; the fisherman refuses, comparing them to **King Yunan and Sage Duban** and
  tells that tale: King Yunan has leprosy; the old sage Duban cures him with a hollow polo mallet filled with medicine
  (play, sweat, bathe, sleep, cured); the king honours him; a jealous vizier plots. Dawn.
- **585 (Night 8):** The vizier convinces Yunan that Duban is a spy; Yunan orders his death; Duban offers a wondrous
  book that his head will read after his death; he is executed; the king turns the stuck pages with a licked finger;
  the pages are poisoned and the king dies. Back to the fisherman: the jinni swears an oath, is freed, kicks the jar into
  the sea, leads him over mountains to a lake with white, red, blue and yellow fish. The Sultan pays 400 dinars for
  them; in the palace kitchen the wall splits, a beautiful woman with a wand asks the frying fish about their covenant;
  they burn black. Dawn.
- **599 (Night 9):** The cook faints; the Vizier, then the Sultan himself see the wonder again (now a towering dark
  figure steps out of the wall). The Sultan marches to the hidden lake, goes alone into the mountains at night, finds a
  black-stone castle, empty and splendid; a weeping young prince on a throne shows he is black marble from the waist
  down — his sorceress wife's curse. Dawn cliffhanger.

## Characters (cards in `output/Aliflaila/characters/`; see `refs_sheet.jpg`)
Frame: `shahrazad` (saffron-gold gown, ivory headscarf, ruby forehead jewel), `dunyazad` (~12, lavender gown, pink
headscarf), `shahryar` (crimson-gold plumed turban, bronze brocade coat, black beard), `grand_vizier` (Shahrazad's
father, white beard, deep-blue robe; 452 mainly), `shah_zaman` (452; emerald green).
Merchant tale: `merchant`, `merchant_jinni` (charcoal-smoke giant, dark-red robe/turban, ember eyes),
`old_man_gazelle` (snow-white beard, sage-green robe, staff), `old_man_dogs` / `old_man_dogs_young` (brown robe),
`old_man_mule` / `old_man_mule_young` (maroon robe, blue cap). 486: `gazelle_wife`, `young_mother`, `gazelle_son`,
`herdsman`, `herdsman_daughter`. 498: `elder_brother`, `middle_brother`, `jinniyya_wife`. 509: `sorceress_wife`,
`fish_seller`, `fishseller_daughter` (face-veiled).
Fisherman tale: `fisherman` (patched blue tunic, net), `jar_jinni` (indigo-smoke giant, midnight-purple robe, golden
eyes, forked beard). Yunan tale: `king_yunan` (purple, crown on turban), `sage_duban` (long white beard, ochre robe,
green turban), `yunan_vizier` (grey turban, olive robe). Fish tale: `fish_sultan` (sapphire blue), `sultan_vizier`
(rust-orange), `palace_cook`, `wall_woman` (emerald, green wand), `marble_prince` (white-and-gold, black marble feet).
Characters without cards (Shah Zaman's wife, the queen, servants, executioner, Asif, soldiers, crowds, the
merchant's family, the fisherman's family, physicians, courtiers) appear only as described in `visual`, small or from
behind, modestly dressed.
Animals: the gazelle (golden cord), two black dogs (enchanted brothers, on leashes, sitting calmly at a distance — never
petted or cuddled), the grey mule, the cow and calf (486), the four fish (white, red, blue, yellow), horses, camels.

## BINDING content rules (override the literal narration)
1. **No weapons, no violence on screen.** The narration often mentions swords (the jinni's sword, the executioner's
   sword, Shah Zaman's sword, the Sultan's sword): NEVER draw a sword, dagger, knife or any weapon; jinn have empty
   hands. A "raised sword" moment = the jinni towering with a raised empty fist / pointing finger against a storm sky,
   the merchant kneeling with eyes shut, and then cut away. Killing / execution / beheading = symbols only: a lantern
   blown out, an empty cushion, a dropped scroll, a shadow-less empty courtyard at grey dawn, storm clouds over domes,
   a closed door, a row of extinguished lamps. No blood, wounds, bodies, severed heads, covered trays, coffins.
2. **The betrayals (452 Shah Zaman's wife, the queen in the garden; 509 the third old man's wife): NOTHING of the
   adultery is shown** — no lovers, no couples, no beds. Show only the husband's shocked face at a doorway / behind a
   lattice screen, the empty moonlit garden with a fountain, a dropped gift box, a lantern swinging. The "black slave"
   lovers are NEVER depicted (no figure at all — this also avoids a racist image). The executed queen and her servants:
   not shown; use an empty garden pavilion at grey dawn.
3. **Shahryar's law (452):** the nightly brides and executions = symbols: a lone lantern going out each night across a
   row of windows, mourning families leaving the city by moonlight with camels, the Grand Vizier sitting alone with his
   head in his hands. The executioner = never shown, or a faceless distant silhouette standing at a gate at dawn with
   empty hands.
4. **Shahrazad and Shahryar are married** (from 452's wedding). Frame scenes: Shahrazad sits on a cushion on the carpet
   telling the story, the king sits or reclines fully dressed on a divan an arm's length or more away, Dunyazad sits on
   the carpet by her sister. No bed scenes, no lying together, no touching beyond a hand on her hand.
   The wedding = a modest ceremony image (henna hands, a lantern-lit hall), never a bedroom. Shahrazad's tears to fetch
   Dunyazad = her sitting with lowered eyes.
5. **Hijab always:** every woman and girl (Shahrazad, Dunyazad, the wives, the jinniyya, the herdsman's daughter, the
   fish-seller's daughter, the woman from the wall, mourners) wears a headscarf fully covering hair and neck in every
   shot, indoors too. No woman ever lies in a bed on screen (sleeping = seen from afar as a covered shape, or omit).
   The cover's uncovered hair is NOT reproduced. Gowns long-sleeved, ankle-length, opaque.
6. **No touching between unrelated men and women.** Married couples (the merchant and his wife, the jinniyya wife and
   the young merchant after their marriage) may stand side by side; the jinniyya carrying her husband through the air =
   both flying side by side wrapped in a glowing silver light, her hand holding his wrist only. The 498 "thrown
   overboard while asleep" = a dark ship at night from a distance and a splash in moonlit water.
7. **Magic and transformations:** swirls of glittering light, smoke and sparkles — fairy-tale, never horror, never body
   horror, no occult symbols, no spell books with writing. People turned into animals: show the before (person) and
   after (animal) as separate images with a sparkle swirl, never a half-transformed body.
8. **Animal deaths:** the Eid sacrifice of the cow (486) = the herdsman leading the cow away by a rope at dawn, the old
   man turning his face away; no knife, no slaughter, no carcass, no bones. The dead donkey in the net (532) = the
   fisherman recoiling with a pinched nose from a heavy tangled net, its content hidden by the net/water. Bones and
   broken glass = shells and seaweed tangled in the net.
9. **Prophet Sulaiman and sacred:** NEVER depict Prophet Sulaiman, nor any prophet, nor Asif ibn Barkhiya's face (Asif
   only as a distant figure from behind in white, if needed). Sulaiman's seal = a glowing abstract eight-petalled
   geometric rosette on the lead stopper (NOT a six-pointed star, no letters). God's Name = only golden light. Prayer is
   shown respectfully (a man on a simple mat facing a dawn horizon, palms raised). Quran recitation = the merchant
   seated under the tree with palms raised; no book with script. Mosques/minarets only as distant silhouettes. No Arabic
   script anywhere.
10. **Sickness and death (569/585):** King Yunan's leprosy = the king hunched under a heavy hooded cloak, physicians
    shaking their heads; no skin lesions. Bathing = steam in a marble bathhouse with the king wrapped in a robe, seen
    from the shoulders up. Duban's execution, the "speaking head", the poisoned book and Yunan's death = Duban standing
    calmly before the court with a large old book; then the closed old book on a stand in a beam of light; the fallen
    gold crown on the marble floor beside the closed book; an empty throne; a candle snuffed. Never a head, tray or body.
11. **The marble prince (599):** he stays seated on his throne in his long robe; only his black marble feet/shins below
    the hem are visible; the Sultan's shocked face. The "very black slave" from the kitchen wall (599) = a towering
    faceless figure of dark swirling shadow-smoke with glowing eyes, NOT a human of any race; the woman from the wall
    (585) = the `wall_woman` card.
12. **Excluded always:** wine/alcohol (the merchant's table has dates, bread, water), smoking, idols/statues of gods,
    fire temples, crosses, dogs as pets, nudity, the fisherman without his tunic (he wades in his tunic), text/letters.

## Sound
No music. Ambience keys (sound.py): palace_night, palace_dawn, palace_day, throne_hall, palace_garden_day,
palace_garden_night, palace_kitchen, bazaar_day, desert_day, desert_night, desert_dawn, sandstorm, oasis_day,
seashore_dawn, seashore_day, lake_mountains, mountain_night, empty_castle, caravan_road, polo_field, island_wild,
city_lanes_night, ship_deck, ship_storm, port_day, stone_house_day, stone_house_night, stone_house_dawn, village_day,
village_night, mosque_dawn, memory, dream_glow.

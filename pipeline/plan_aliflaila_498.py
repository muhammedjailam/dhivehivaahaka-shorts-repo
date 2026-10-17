"""Beat/shot plan for Aliflaila episode 498 — Night 4: the Second Old Man and the two black dogs (used by plan_beats.py)."""

GLOW = "soft golden storybook glow around the edges of the frame, warm dreamy light (a tale within the tale)"

LOC = {
    "palace_ext": "King Shahryar's great white palace with onion domes and slender towers above a sleeping Arabian Nights city of domes and minarets, deep midnight-blue night, a huge silver moon",
    "chamber": "King Shahryar's palace bedchamber: Persian carpets, embroidered floor cushions, a low cushioned divan, brass lanterns, silk curtains, a tall arched window with a carved lattice screen looking out over a city of domes",
    "desert": "a vast golden desert of rolling dunes around a lone spreading tree beside a small clear spring, the merchant's resting place",
    "bazaar": "a lively covered bazaar of a medieval Arabian city in the old days: rows of small wooden shop stalls under striped awnings, rolls of silk, brass pots, baskets of spices, arched stone passages",
    "port": "a busy old Arabian harbour: a stone quay, big wooden sailing ships with tall white sails, bales and crates of trade goods, turquoise water",
    "home": "the young merchant's modest whitewashed stone house: a simple room with a woven carpet, floor cushions, a small arched window, a brass water jug",
    "courtyard": "the small inner courtyard of the young merchant's stone house at night, a single date palm, a lantern on the paving stones",
    "island_port": "a rich and beautiful island seen from the sea: lush palm groves, a white town of domes and arches climbing a green hill, a harbour with a busy bazaar by the water",
    "island_bazaar": "the colourful waterfront bazaar of a rich island town, stalls of fruit, silk and pearls under palm trees, the sea and ships behind",
    "deck": "the deck of an old wooden sailing ship at sea, coiled ropes, a tall mast with billowing white sails, the open sea to the horizon",
    "sea_night": "the dark open sea at night, a lone wooden sailing ship in the distance under a huge moon, silver moonlight on the black waves",
    "night_sky": "the night sky high above the moonlit sea, a big moon, stars, and a small dark island far below",
    "isle": "a small deserted island at night: an empty pale beach, a few wild palms, black rocks, the moonlit sea all around",
    "shop": "the young merchant's small wooden shop in the bazaar, early morning, shelves of rolled cloth and brass goods, a wooden post in the middle",
    "chamber_dawn": "King Shahryar's palace bedchamber at dawn: Persian carpets, cushions, a low divan, brass lanterns burnt low, a tall arched lattice window opening onto a city of domes with a distant slender minaret silhouette against the dawn sky",
}
MOOD = {
    "palace_ext": "deep night, midnight-blue sky, huge silver moon, one single window glowing warm amber, total stillness and silence",
    "chamber": "late night near its end, deep midnight blue with warm amber lantern light, hushed and intimate, quiet anticipation",
    "desert": "late afternoon, warm golden sunlight with long shadows on the dunes, a turquoise sky, tense suspense",
    "bazaar": "bright daytime, warm golden sunlight through the awnings, busy and hopeful, soft golden storybook glow",
    "port": "bright morning, golden sunlight on turquoise water, bustling and adventurous, soft golden storybook glow",
    "home": "daytime, soft warm light from the window, tender brotherly warmth, soft golden storybook glow",
    "courtyard": "evening into night, deep blue sky with stars, warm amber lantern glow on the stones, secretive and hopeful, soft golden storybook glow",
    "island_port": "bright midday, dazzling golden sunlight, turquoise sea, wonder and wealth, soft golden storybook glow",
    "island_bazaar": "bright afternoon, warm golden light, colourful and lively, then a tender quiet moment, soft golden storybook glow",
    "deck": "golden sunset, rose and amber sky over the sea, warm and loving but with gathering shadows, soft golden storybook glow",
    "sea_night": "dead of night, deep midnight blue, cold silver moonlight, ominous and lonely",
    "night_sky": "deep midnight blue night, a huge moon and stars, a magical glowing silver light, wonder and rescue",
    "isle": "night, cold silver moonlight, the soft silver glow of the jinniyya lighting the sand, awe then anger then mercy",
    "shop": "early morning, soft pale golden light through the open door, dust motes in the air, astonishment",
    "chamber_dawn": "dawn, soft golden sunrise light pouring through the lattice window into the room, lanterns burnt low, rose and gold sky, relief",
}

BEATS = [
    dict(to=4, reason="episode opening: the fourth night falls over the silent kingdom and palace", loc="palace_ext",
         visual="a wide view of the great white palace with onion domes and slender towers rising above a silent sleeping city of domes under a huge silver moon and a sky of stars; only one high arched lattice window of the palace glows warm amber; no people visible",
         camera="wide establishing shot, slightly low angle, the palace and moon in the upper two-thirds, the dark still rooftops forming a calm lower third",
         amb="palace_night"),
    dict(to=9, reason="scene change: inside the chamber, Dunyazad asks for the rest of the tale and the king allows it",
         chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber",
         visual="Shahrazad sitting upright on a floor cushion on the carpet, turning her large expressive eyes towards the king with a gracious questioning look, one hand lifted gently; little Dunyazad sitting on the carpet beside her, leaning in eagerly and whispering with a hopeful smile; King Shahryar, fully dressed, sitting on the low divan an arm's length away, wide awake and leaning forward impatiently, one hand gesturing 'go on'; the moonlit city of domes visible through the arched lattice window",
         camera="medium wide shot, eye level, all three faces in the upper two-thirds, the patterned carpet as a calm lower third",
         amb="palace_night"),
    dict(to=13, reason="scene change into the tale: the desert, the Second Old Man steps forward with his two black dogs",
         chars=["merchant_jinni", "old_man_dogs", "merchant", "old_man_gazelle"], loc="desert",
         visual="the towering giant jinni of charcoal smoke and dark-red robe looming over the dunes beside the lone tree, arms folded, empty-handed, looking down with glowing ember eyes; in front of him the sturdy Second Old Man in his chocolate-brown robe has stepped forward, one hand raised as he speaks up boldly to the jinni; behind him two black dogs on leashes sit calmly at a little distance; the merchant in a plain white travelling robe kneels by the spring holding a folded white cloth, looking up anxiously; the snow-white-bearded First Old Man with his staff and a golden-brown gazelle on a golden cord stands a little to the side",
         camera="dramatic low-angle wide shot, the jinni's head and shoulders filling the upper sky, the people in the middle, smooth sand as a calm lower third",
         amb="desert_day", transition="dissolve", sens="other",
         safe="the jinni is shown empty-handed; the dogs are ordinary black dogs sitting calmly on leashes at a distance"),
    dict(to=15, reason="flashback into the Second Old Man's own tale: the three brothers share their inheritance and open shops",
         chars=["old_man_dogs_young", "elder_brother", "middle_brother"], loc="bazaar",
         visual=f"three brothers standing proudly in front of three neighbouring wooden shop stalls in the bazaar, each holding up a small leather coin pouch: the heavy-set eldest brother in grey-green before a big stall of silks, the lanky middle brother in mustard-yellow before a stall of brass pots, and the kind young man of about 30 in chocolate-brown before the smallest stall of cloth, smiling modestly; small background shoppers in modest robes; {GLOW}",
         camera="medium wide shot, eye level, the three brothers' faces in the upper half, the stone floor of the bazaar as a calm lower third",
         amb="bazaar_day", transition="dissolve"),
    dict(to=17, reason="action and place change: the eldest brother sells everything and sails abroad", chars=["elder_brother", "old_man_dogs_young"], loc="port",
         visual=f"the heavy-set eldest brother in his grey-green robe and turban striding up a wooden gangplank onto a big wooden sailing ship with tall white sails, waving back confidently, bales of goods being carried aboard by small background porters; on the quay the young man in chocolate-brown watches with a slightly worried smile; {GLOW}",
         camera="wide shot, slightly low angle, the ship's sails in the upper half, the stone quay as a calm lower third",
         amb="port_day"),
    dict(to=19, reason="time jump (a year later) and action change: a ragged beggar at the shop door is the eldest brother",
         chars=["elder_brother", "old_man_dogs_young"], loc="bazaar",
         visual=f"the young man in chocolate-brown rising from behind the counter of his small shop stall in shock and recognition, eyes wide; at the shop's doorway stands the eldest brother, gaunt and hungry, in a ragged, torn and patched faded grey-green robe and a frayed turban, his hand held out humbly like a beggar, eyes lowered in shame; {GLOW}",
         camera="medium shot, eye level, from beside the counter, both faces in the upper two-thirds, the wooden counter as a calm lower third",
         amb="bazaar_day", transition="black", sens="other",
         safe="poverty shown with dignity: patched clothes and a humble pose, no suffering body"),
    dict(to=23, reason="scene change: at home he bathes and clothes his brother and gives him a thousand dinars",
         chars=["old_man_dogs_young", "elder_brother"], loc="home",
         visual=f"in the modest room of the young man's house, the eldest brother, washed and now dressed in a fresh clean grey-green robe and turban, receives a heavy leather pouch of gold coins in both hands with tearful grateful eyes; the young man in chocolate-brown stands before him with a warm encouraging smile, one hand on his brother's shoulder; a brass water jug and folded towel on a low table; {GLOW}",
         camera="medium two-shot, eye level, faces in the upper half, the woven carpet as a calm lower third",
         amb="stone_house_day", hum=True),
    dict(to=26, reason="time jump and character change: the middle brother also fails at sea and returns a beggar; he is helped too",
         chars=["middle_brother", "old_man_dogs_young"], loc="bazaar",
         visual=f"the lanky middle brother, thin and weary, in a ragged, torn and patched faded mustard-yellow robe and frayed turban, standing at the young man's shop counter with his head bowed; the young man in chocolate-brown leans across the counter kindly holding out a leather pouch of gold coins to him; {GLOW}",
         camera="medium two-shot, eye level, faces in the upper half, the counter as a calm lower third",
         amb="bazaar_day", transition="black"),
    dict(to=31, reason="time jump (two or three years later): the brothers plead for a joint voyage; half the money is buried as a reserve",
         chars=["old_man_dogs_young", "elder_brother", "middle_brother"], loc="courtyard",
         visual=f"in the small courtyard at night beside a date palm, the young man in chocolate-brown kneels and carefully lowers a small iron-bound wooden chest of gold coins into a shallow hole in the earth, a lantern beside him casting warm light; the eldest brother in grey-green and the middle brother in mustard-yellow, both in clean robes, stand behind him nodding eagerly with hopeful smiles, rubbing their hands; {GLOW}",
         camera="medium wide shot, slightly high angle, the three faces in the upper half, the paving stones as a calm lower third",
         amb="stone_house_night", transition="black"),
    dict(to=33, reason="scene change: the three brothers sail and arrive at a rich, beautiful island", loc="island_port",
         visual=f"an old wooden sailing ship with billowing white sails gliding into the turquoise harbour of a rich, beautiful island, a white town of domes and arches climbing a green palm-covered hill, a busy bazaar along the waterfront; three tiny figures of the brothers at the bow pointing excitedly; {GLOW}",
         camera="wide establishing shot, the island town and sky in the upper two-thirds, calm turquoise water as the lower third",
         amb="port_day"),
    dict(to=35, reason="character change: a poor woman in torn clothes asks the young man to marry her",
         chars=["jinniyya_wife", "old_man_dogs_young"], loc="island_bazaar",
         visual=f"in the island's waterfront bazaar, a young woman in a patched plain brown gown, long-sleeved and ankle-length, and a plain brown headscarf fully covering her hair and neck (no silver glow yet) stands humbly at a respectful distance before the young man in chocolate-brown, her hands clasped at her chest, asking with sincere hopeful eyes; he listens with a surprised, compassionate look; stalls of fruit and silk behind; {GLOW}",
         camera="medium two-shot, eye level, faces in the upper half, the sandy paving as a calm lower third",
         amb="bazaar_day", sens="other",
         safe="the proposal is shown at a respectful distance with no touching; she is fully covered"),
    dict(to=37, reason="action change: married, she is dressed in fine clothes and boards the ship as his wife; her beauty revealed",
         chars=["jinniyya_wife", "old_man_dogs_young"], loc="deck",
         visual=f"on the ship's deck at golden sunset, the young man in chocolate-brown and his new wife standing side by side at the wooden rail, not touching, smiling shyly at each other; she is now radiant in a long-sleeved ankle-length pearl-white silk gown with silver embroidery and a pearl-white headscarf fully covering her hair and neck, a faint soft silver glow around her; white sails glowing rose and gold above; {GLOW}",
         camera="medium shot, eye level, faces in the upper half, the wooden deck planks as a calm lower third",
         amb="ship_deck", sens="intimacy",
         safe="the married couple only stand side by side at the rail, fully clothed, no touching"),
    dict(to=39, reason="focus change: the two elder brothers grow envious", chars=["elder_brother", "middle_brother", "old_man_dogs_young", "jinniyya_wife"], loc="deck",
         visual=f"in the long shadow of the mast, the eldest brother in grey-green and the middle brother in mustard-yellow stand close together whispering, their narrowed resentful eyes glaring sideways; far behind them, small in the sunset light at the other end of the deck, the young man and his wife in pearl-white stand side by side at the rail, unaware; {GLOW}",
         camera="medium close shot on the two brothers in the foreground, the couple small and soft-focused in the background, the deck as a calm lower third",
         amb="ship_deck"),
    dict(to=41, reason="time jump to one night at sea: the brothers throw the sleeping couple overboard (shown only from afar)", loc="sea_night",
         visual="a lone dark wooden sailing ship far away on the black sea at night under a huge pale moon, its sails dark; beside its hull a single bright white splash rises in the moonlit water, silver ripples spreading; no people visible",
         camera="extreme wide shot, the moon and sky in the upper half, the ship small in the middle, dark rippling water as the calm lower third",
         amb="ship_deck", transition="black", sens="violence",
         safe="the attempted drowning is never shown: only a distant dark ship and a splash in moonlit water (bible rule 6)"),
    dict(to=43, reason="action change: the wife lifts him from the sea and flies him through the air to a deserted island",
         chars=["jinniyya_wife", "old_man_dogs_young"], loc="night_sky",
         visual="high in the night sky above the moonlit sea, the jinniyya in her pearl-white gown and headscarf and the young man in his chocolate-brown robe fly side by side a little apart, NOT holding hands and not touching, both carried inside one large glowing oval of silver light like a comet; her hands are open at her sides, his arms spread for balance; her headscarf fully covers her hair and forehead; a trail of silver sparkles streams behind them towards a small dark island far below; his face amazed, hers calm and determined",
         camera="wide shot, the two figures and the moon in the upper two-thirds, the dark sea below as a calm lower third",
         amb="dream_glow", sens="other",
         safe="the rescue flight as a glowing silver light, side by side without touching (bible rule 6; first image showed hand-holding and was regenerated)"),
    dict(to=46, reason="scene change: on the deserted island she reveals she is a good Muslim jinniyya",
         chars=["jinniyya_wife", "old_man_dogs_young"], loc="isle",
         visual="on the pale moonlit beach of a deserted island, the jinniyya stands glowing softly silver-white in her pearl-white gown and headscarf, one hand on her heart, speaking gently but seriously with luminous silver-grey eyes, tiny silver sparkles drifting around her; a few steps away the young man in a wet chocolate-brown robe sits up on the sand staring at her in astonishment",
         camera="medium wide shot, eye level, both faces in the upper half, the smooth pale sand as a calm lower third",
         amb="island_wild", transition="xfade", sens="other",
         safe="a jinn shown as a gentle glowing woman, fully covered, fairy-tale sparkles only"),
    dict(to=50, reason="action change: she vows to sink the brothers' ship; he begs her for mercy until her anger cools",
         chars=["old_man_dogs_young", "jinniyya_wife"], loc="isle",
         visual="the young man kneeling on the moonlit sand with his palms pressed together, pleading up at his wife with desperate tearful eyes; she stands tall over him, her silver glow flaring, eyes flashing with anger, one open hand raised towards the far sea where storm clouds are gathering under the moon; her expression on the edge of softening",
         camera="medium wide, slightly low angle on her, both faces in the upper two-thirds, the sand as a calm lower third",
         amb="island_wild", sens="violence",
         safe="the threat to kill is shown only as her anger and storm clouds far over the sea; no harm shown", hum=True),
    dict(to=51, reason="return to the flight image: she flies him home through the night", reuse="beat_015",
         loc="night_sky", visual="reuse of the silver-light flight", amb="dream_glow"),
    dict(to=52, reason="time jump (next morning) and scene change: he digs up the gold, opens his shop and finds two black dogs tied inside",
         chars=["old_man_dogs_young"], loc="shop",
         visual=f"the young man in chocolate-brown standing in the open doorway of his small shop in soft morning light, a small iron-bound wooden chest of gold coins under one arm, frozen in astonishment with wide eyes; inside the shop two black dogs sit calmly side by side on leashes tied to a wooden post, looking at him; dust motes floating in the light; {GLOW}",
         camera="medium wide shot from inside the shop, the man's face in the upper third, the wooden floor as a calm lower third",
         amb="bazaar_day", transition="black", sens="other",
         safe="the enchanted brothers are drawn as ordinary black dogs sitting calmly on leashes at a distance"),
    dict(to=55, reason="character change: the wife appears and explains the spell — the dogs are his brothers, for ten years",
         chars=["jinniyya_wife", "old_man_dogs_young"], loc="shop",
         visual=f"inside the small shop a swirl of glittering silver sparkles and light has formed, and from it the jinniyya in her pearl-white gown and headscarf appears, calm and stern, one hand gesturing towards the two black dogs sitting quietly tied to the wooden post; the young man stands by the door in amazement; through a small window a tiny distant ship is seen sinking into a stormy sea far away while small lifeboats row safely away; {GLOW}",
         camera="medium wide shot, eye level, faces in the upper half, the wooden floor as a calm lower third",
         amb="bazaar_day", sens="other",
         safe="sorcery shown as fairy-tale silver sparkles; the ship's sinking only as a tiny distant image with everyone rowing to safety"),
    dict(to=57, reason="back to the desert: the Second Old Man ends his tale before the jinni", reuse="beat_003",
         loc="desert", visual="reuse of the desert image: the Second Old Man before the jinni with his two dogs",
         amb="desert_day", transition="dissolve"),
    dict(to=60, reason="action change: the jinni claps in amazement and forgives the second third of the merchant's life",
         chars=["merchant_jinni", "merchant", "old_man_dogs"], loc="desert",
         visual="the towering giant jinni of charcoal smoke and dark-red robe clapping his huge empty hands together in delighted amazement, a broad astonished grin in his black beard, ember eyes wide, swirls of smoke around him; below him the merchant in a plain white travelling robe kneels with his hands raised in relief, and the Second Old Man in chocolate-brown bows his head respectfully, his two black dogs sitting calmly on leashes behind him",
         camera="dramatic low-angle wide shot, the jinni's face high in the frame, the people in the middle, the sand as a calm lower third",
         amb="desert_day"),
    dict(to=62, reason="character change: the Third Old Man with his mule steps forward and offers his tale",
         chars=["old_man_mule", "merchant_jinni", "merchant"], loc="desert",
         visual="the thin wiry Third Old Man in his maroon robe and small dark-blue cap steps forward on the sand leading a grey mule by a rope, one finger raised as he calls up boldly to the towering jinni; the giant jinni leans down curiously with folded empty hands; the merchant in a plain white travelling robe kneels nearby looking up with new hope",
         camera="low-angle medium wide shot, the old man's and the jinni's faces in the upper two-thirds, the sand as a calm lower third",
         amb="desert_day"),
    dict(to=63, reason="back to the frame at dawn: the Fajr call is heard and Shahrazad falls silent",
         chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber_dawn",
         visual="golden dawn light pours through the arched lattice window, a distant slender minaret silhouetted against a rose-gold sky; Shahrazad sits on her floor cushion with her hands folded in her lap and her eyes politely lowered, silent; Dunyazad sits on the carpet beside her; King Shahryar sits on the divan an arm's length away, still lost in the story",
         camera="medium wide shot, eye level, the window and faces in the upper two-thirds, the carpet as a calm lower third",
         amb="palace_dawn", transition="dissolve", sens="other",
         safe="the call to prayer only as a distant minaret silhouette in the dawn sky (no adhan audio)"),
    dict(to=65, reason="action change: the king suddenly sits up demanding to know what happened next",
         chars=["shahryar", "shahrazad"], loc="chamber_dawn",
         visual="King Shahryar, fully dressed, sitting bolt upright on the edge of the divan, leaning forward with wide eager eyes and one open hand raised in a questioning gesture; in the foreground Shahrazad, seen from the side, sits calmly on her cushion with a faint knowing smile; golden dawn light across the room",
         camera="medium shot, eye level, the king's face in the upper third, the carpet as a calm lower third",
         amb="palace_dawn", hum=True),
    dict(to=69, reason="return to the dawn group image: Shahrazad gently promises the next tale", reuse="beat_024",
         loc="chamber_dawn", visual="reuse of the dawn chamber image", amb="palace_dawn"),
    dict(to=72, reason="action change: the king spares her again and leaves for his court; the executioner's sword waits another day",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="King Shahryar in his crimson plumed turban and bronze brocade coat, empty-handed, striding towards a tall open carved doorway that leads into a sunlit palace hall, glancing back over his shoulder; behind him on the carpet Shahrazad and Dunyazad exchange a quiet relieved smile, Dunyazad's hand on her sister's hand; bright golden morning sunlight floods the room",
         camera="medium wide shot, eye level, faces in the upper two-thirds, the carpet as a calm lower third",
         amb="palace_dawn", sens="violence",
         safe="the executioner and his sword are never shown; the reprieve is shown as the king leaving and the sisters' relief", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Night Four: the tale of the Second Old Man and the two black dogs. The black darkness of the fourth night spread over the world,")
sh(2, "and a deep silence settled over the whole kingdom. Inside King Shahryar's palace not a single sound could be heard.")
sh(3, "Yet the king's mind was wide awake. He lay there,")
sh(4, "impatient beyond measure, longing to know how the events between the jinni and the old men in that terrifying desert would end.")
sh(5, "As the last part of the night drew near, Dunyazad called to her elder sister as usual.",
   [("cloth_rustle", "ގޮވައިލިއެވެ", -24)])
sh(6, "\"Dear sister,\" Dunyazad whispered, \"if you are not asleep, please finish that beautiful story you broke off yesterday.")
sh(7, "Tell us the story of the second old man who had the two black dogs.\" Shahrazad looked towards the king.")
sh(8, "\"O noble king, will you give me permission to continue the story?\" \"Tell it!\"")
sh(9, "said King Shahryar. \"I very much want to know the secret of those two dogs.\" Shahrazad began the story.")
sh(10, "\"O mighty and wise king! When the First Old Man had finished telling his tale,")
sh(11, "the giant jinni forgave one third of the merchant's blood. Then the second old man, who had the two black dogs, stepped forward",
   [("footsteps_sand", "ޖެހިލައި", -22)])
sh(12, "and began to speak to that terrifying jinni: 'O mighty jinni! These two black dogs here behind me and beside me are not ordinary animals.")
sh(13, "They are in truth my own two elder brothers, and I am their youngest brother. When our father died, he left the three of us three thousand dinars as our inheritance.")
sh(14, "We divided the money equally; each of us got a thousand dinars. My two elder brothers opened shops in the bazaar with that money and began to trade.")
sh(15, "I too opened a small shop with my money and began to trade. A short while later,")
sh(16, "my eldest brother made a big decision: he sold all the goods in his shop to travel and trade in foreign lands.")
sh(17, "He bought a thousand dinars' worth of goods and set sail on a big ship. One year after he left,",
   [("wave_crash", "ނަވެއްގައި", -22)])
sh(18, "one day as I sat in my shop, a beggar in very poor, torn clothes came and stopped at the door of my shop.",
   [("footsteps_pavement", "ހުއްޓުނެވެ", -22)])
sh(19, "When I looked at him — it was my eldest brother! He was hungry, reduced to begging.",
   [("gasp", "ބޭބެއެވެ", -20)])
sh(20, "I ran to him, embraced him and treated him kindly. He had gone bankrupt in his trade and lost everything.",
   [("footsteps_pavement", "ދުވެފައި", -22), ("cloth_rustle", "ބައްދައިލައި", -22)], hum=True)
sh(21, "I took him home, had him bathed and dressed him in fine new clothes. When I checked my shop's accounts, I had two thousand dinars of profit.",
   [("water_splash_small", "ފެންވަރުވައި", -24)])
sh(22, "I gave a thousand dinars of it to my brother and said: 'O brother! Do not grieve. Here is another thousand dinars for you.")
sh(23, "Open a shop again with it and start trading.' He was overjoyed and started trading again. A short while after that,")
sh(24, "my middle brother did exactly the same. He too bought goods and set out on a voyage. And just one year later he came back with nothing at all,",
   [("wave_crash", "ދަތުރަށް", -22)])
sh(25, "returning as a poor beggar. Just as I had done for my eldest brother, I did for him too:",
   [("sigh", "ނިކަމެތި", -22)])
sh(26, "I gave him a thousand dinars from my profit and helped him start trading again. After that two or three years went by.")
sh(27, "My two brothers came to me together and proposed that the three of us make a great voyage together and do great business.")
sh(28, "At first I opposed it, because their past experiences had gone so badly. But they pleaded so much that in the end I agreed.")
sh(29, "At that time I had three thousand dinars of profit. I said: 'We will divide this money in two.")
sh(30, "Fifteen hundred dinars we will bury and hide. That is money to come back and use if misfortune befalls us. The remaining fifteen hundred dinars',",
   [("stone_scrape", "ވަޅުލައި", -22)])
sh(31, "we will share out, five hundred dinars each, buy goods and set sail.' My brothers agreed to this with great joy.")
sh(32, "We bought goods, boarded a ship and began the voyage. After a journey of many days we reached a very beautiful, rich island.",
   [("wave_crash", "ނަވަކަށް", -22)])
sh(33, "We traded in that island's bazaar and made a very great profit. While I was on that island, one day a very poor")
sh(34, "woman in torn clothes came up to me, greeted me and asked me to marry her. She said:")
sh(35, "'O good man! Marry me. Though I am a poor woman, I will be utterly faithful to you.'")
sh(36, "Compassion for her arose in my heart, and for the sake of God I married her. I bought her beautiful clothes and took her aboard the ship with me as my wife.",
   [("cloth_rustle", "ހެދުން", -24)])
sh(37, "After the marriage I discovered that this poor woman was in truth extraordinarily beautiful. She loved me deeply.")
sh(38, "But seeing this, a great envy arose in the hearts of my two brothers.")
sh(39, "They envied my success in trade and my wife's beauty.")
sh(40, "When we had finished our trading and were sailing back home over the sea, one night while my wife and I were asleep,")
sh(41, "my two brothers came secretly, lifted us both up and threw us into the dark sea! I woke only when I fell into the sea and began to drown.",
   [("splash", "އެއްލައިލިއެވެ", -16), ("breath_heavy", "ޣަރަޤުވާން", -20)], hum=True)
sh(42, "But at that moment my wife suddenly took hold of me with an unnatural strength and lifted me up above the water.",
   [("magic_shimmer", "ނެގިއެވެ", -20)])
sh(43, "And she flew through the air and carried me to a deserted island nearby! As I stood there amazed, she said:",
   [("wind_gust", "އުދުހިފައި", -20)])
sh(44, "'O my husband! Do not be afraid. I am not a human being. I am a good Muslim jinniyya.")
sh(45, "When I saw you, I saw your goodness and kindness and fell in love with you. So I came in the form of a poor human woman and married you.")
sh(46, "You treated me with great kindness. But those wicked, envious brothers of yours tried to kill us.")
sh(47, "So tonight I will go, sink their ship and kill them!' Hearing this I was terrified; I took hold of her feet and begged her:",
   [("thunder", "ފައްތައިލައި", -22), ("gasp", "ބިރުންގޮސް", -22)])
sh(48, "'O my beloved wife! For the sake of God, do not kill them! However badly they have treated me,", hum=True)
sh(49, "they are my own brothers. I could not bear to have their blood shed.' I pleaded with her for a long time,",
   [("sob_breath", "އާދޭސްކުރުމުން", -24)])
sh(50, "and at last her anger cooled a little. 'Very well. Since you ask so earnestly, I will not kill them. But I will give them the punishment they deserve.'",
   [("sigh", "ރަނގަޅެވެ", -24)])
sh(51, "After that the jinniyya flew through the air with me and, that very night, carried me to my own house.",
   [("wind_gust", "އުދުހިފައި", -22)])
sh(52, "In the morning I went and dug up the fifteen hundred dinars we had buried earlier. And when I went to my shop and opened it, I saw these two black dogs tied up inside the shop!",
   [("stone_scrape", "ކޮނެގެން", -22), ("door_open", "ހުޅުވައިލި", -18), ("gasp", "ކުއްތާއެވެ", -20)])
sh(53, "As I stood amazed, my wife appeared there and said: 'O husband! These are your two brothers.",
   [("magic_shimmer", "ފާޅުވެފައި", -18)])
sh(54, "I sank their ship in the sea, and after saving everyone else, I cast a spell on these two",
   [("wave_crash", "ފައްތާލައި", -22), ("magic_shimmer", "ސިހުރު", -20)])
sh(55, "and turned them into two black dogs for a period of ten years. This is the punishment for their treachery and envy.'")
sh(56, "O mighty jinni! Today it is exactly ten years. I am travelling with these two dogs to find my wife and ask her to break the spell and turn them back into human beings.")
sh(57, "This is the story of what happened between me and these two black dogs. Is it not even more wondrous than the First Old Man's story?'")
sh(58, "The giant jinni clapped his hands in amazement. 'Yes! That is truly a perfect and just as wondrous a story.",
   [("soft_thud", "އަތްޖަހައިލިއެވެ", -18)])
sh(59, "For the excellence of your story, I forgive another third of this merchant's blood for your sake.")
sh(60, "Now two thirds of his life are saved.' As he said this, the third old man, who had a mule with him there, stepped forward.",
   [("footsteps_sand", "ޖެހިލިއެވެ", -22)])
sh(61, "He called out to the jinni and said: 'O mighty jinni! The story of what happened between me and this mule is far more wondrous than the two stories before.")
sh(62, "If I tell that story, will you forgive the rest of his blood for my sake and set him completely free?'\"")
sh(63, "Just as Shahrazad brought the story to this point, the beautiful golden light of dawn appeared on the horizon. As the sweet sound of the Fajr call to prayer began, Shahrazad at once broke off the story and fell politely silent.")
sh(64, "King Shahryar had been completely lost in the story. He suddenly rose and said: \"What happened next?",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(65, "What is the third old man's story? Was the merchant saved completely?\" Shahrazad smiled gently.")
sh(66, "\"O noble king, it is dawn. My time is up. But if I am still in this world tomorrow night,")
sh(67, "I will tell the story of the third old man, and what happened to the merchant next. It is an even more beautiful and exciting story than this one.")
sh(68, "But that will only be known if you let me remain in this world.\" Curiosity had grown beyond measure in King Shahryar's heart.")
sh(69, "He was certain he could not bear it without knowing the third old man's secret and the merchant's fate.")
sh(70, "So today too the king decided to let Shahrazad go without having her killed. And he rose, put on his royal robes,",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(71, "and went to his court to govern. The fourth night was over. By the power of her wise stories, Shahrazad's life went on being saved.",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -22)])
sh(72, "The executioner's sword was put off yet again for another day.", hum=True)
SHOTS = S

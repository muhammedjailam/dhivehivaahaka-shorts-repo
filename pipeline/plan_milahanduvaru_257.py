"""Beat/shot plan for Milahanduvaru episode 257 (used by plan_beats.py)."""

HOUSE = ("Shamaan's family home: an old single-storey whitewashed coral-stone house with a corrugated tin roof on a small "
         "Maldivian island")
LOC = {
    "yard_morning": f"the sandy yard of {HOUSE}, a woven joali rope seat under a big shady tree, a low coral-stone boundary wall with a wooden gate, coconut palms and potted plants",
    "memory_lane": "a sandy lane of the same island village many years ago, old coral-stone walls, thatched roofs and coconut palms",
    "memory_beach": "a dark remote beach of a neighbouring island many years ago, low bushes and leaning coconut palms",
    "gate_dusk": f"the wooden gate and the sandy yard of {HOUSE}, the joali under the big tree, the house door with warm light inside",
    "bedroom": "Shamaan's simple bedroom in the old coral-stone house, whitewashed walls, a neatly made wooden double bed with a plain white sheet, a small bedside table with a brass oil lamp, a wooden window with open shutters, a few faded jasmine garlands still hanging from the wedding decoration",
    "bedroom_predawn": "Shamaan's simple bedroom in the old coral-stone house, whitewashed walls, a neatly made wooden double bed, a wooden door open to a dim corridor, a window with open shutters",
    "bedroom_morning": "Shamaan's simple bedroom in the old coral-stone house, whitewashed walls, a wooden double bed with a rumpled white sheet, a window with open shutters",
    "memory_shop": "a sandy village lane beside a small island corner shop with a wooden bench outside, coral-stone walls and palms",
    "moon_lagoon": "a calm moonlit island lagoon with a small wooden fishing dhoni moored near the shore",
    "alibe_yard": "the crowded sandy yard and the front doorway of Alibe's small coral-stone house in the island village, a few palms",
    "living_dusk": "the plain sitting room of Shamaan's family house, whitewashed walls, a cushioned wooden sofa, a woven mat on a tiled floor, the front door open to the yard",
    "lane_dusk": "a narrow sandy village lane lined with coral-stone walls, closed wooden doors and shuttered windows, coconut palms",
    "mosque_night": "a small white island mosque with a short minaret and the empty sandy lane in front of it",
    "veranda_night": "the front veranda of Alibe's family house in the island village, a low wooden bench and woven mats",
    "lane_day": "a sandy lane corner of the island village with coral-stone walls, wooden gates and a few palms",
    "lane_golden": "a sandy village lane opening towards the island harbour and jetty",
    "jetty": "the island's long coral-stone and wooden jetty reaching into a calm wide lagoon",
    "fenda": "the outer veranda (fenda) of Mudhimbe's house: a wide shaded veranda with woven mats and cushions, a low wooden table with a small clay incense burner, bougainvillea at the edge",
    "thundi_dusk": "the island's thundi — a long white sandbank tip reaching into the sea, a big old kaani tree near its base, waves breaking at the very tip",
    "thundi_storm": "the island's thundi — a long white sandbank tip reaching into the sea, a big old kaani tree near its base bending in the wind",
    "thundi_after": "the island's thundi at night just after a storm, wet sand, the big kaani tree dripping",
    "lane_storm": "a dark sandy village lane between coral-stone walls and palms",
    "eaves_rain": "the narrow eaves of a small coral-stone house at the edge of a dark sandy lane",
}
MOOD = {
    "yard_morning": "morning, soft natural tropical daylight filtered through the leaves, gentle shadows, uneasy and anxious",
    "memory_lane": "a soft hazy faded-sepia memory of many years ago, warm daylight, soft vignette, nostalgic and uneasy",
    "memory_beach": "a hazy dark memory of many years ago at night, small orange firelight and drifting smoke against deep indigo, soft vignette, sinister",
    "gate_dusk": "dusk at the time of the Maghrib prayer call, violet and indigo sky after sunset, first warm amber lamplight from the house, anxious",
    "bedroom": "night, warm amber glow of the small oil lamp against deep indigo shadows, silver moonlight through the window, intimate but tense",
    "bedroom_predawn": "pre-dawn just before the Fajr call, cold dim blue light, one faint lamp, sleepy and quiet",
    "bedroom_morning": "early morning, soft golden sunlight through the window shutters, tender and a little guilty",
    "memory_shop": "a hazy daytime memory, slightly desaturated warm light, soft vignette, uneasy",
    "moon_lagoon": "night, full moon over the sea, silver moonlight on still water, dark storm clouds gathering far on the horizon, calm but threatened",
    "alibe_yard": "morning under a pale overcast sky, flat grey light, grief and shock",
    "living_dusk": "just after sunset, a single warm lamp inside, deep blue dusk through the open door, tense",
    "lane_dusk": "dusk turning to night, deep blue light, thin pale mist drifting low between the palms, eerie silence, fear",
    "mosque_night": "night after the Isha prayer, the mosque's soft white light, deep indigo sky, empty and fearful",
    "veranda_night": "night, warm amber light of a hurricane lantern, deep shadows, grief and grave decision",
    "lane_day": "overcast daytime, flat grey-blue light, uneasy waiting",
    "lane_golden": "late afternoon golden hour, warm golden sunlight and long shadows, excitement and hope",
    "jetty": "late afternoon golden hour, sun rays on the waves turning the whole lagoon gold, hopeful awe",
    "fenda": "afternoon, soft shade with warm sunlight at the edges, wisps of incense smoke, calm and serious",
    "thundi_dusk": "dusk after sunset, last orange glow on the horizon fading into indigo, calm before a storm",
    "thundi_storm": "night storm, driving rain, strong wind, a flash of lightning lighting everything silver-white, dark clouds",
    "thundi_after": "night, rain thinning, the warm glow of one hurricane lantern, wet glistening sand, fearful hush",
    "lane_storm": "night storm, pouring rain, a flash of lightning in the sky, almost total darkness",
    "eaves_rain": "night, pouring rain, very dark, a faint distant lamp glow, cold and lonely, ominous",
}

BEATS = [
    dict(to=2, reason="episode opening: Shamaan shaken after the rumours and last night's memories", chars=["shamaan"], loc="yard_morning",
         visual="Shamaan standing alone beside the joali in the sandy yard, one hand on the joali's frame, staring into the distance with a shaken, frightened expression, as if the ground had slipped from under him",
         camera="medium shot, eye level, his face in the upper third, the sandy ground as a calm lower third", amb="island_house_day"),
    dict(to=6, reason="characters change: his worried mother; he tries to reassure her", chars=["sakeena", "shamaan"], loc="yard_morning",
         visual="Sakeena sitting on the joali under the big tree with a deeply worried face, hands clasped in her lap; Shamaan sitting at the other end of the joali turned towards her, explaining earnestly with an open reassuring hand",
         camera="medium wide two-shot, eye level", amb="island_house_day"),
    dict(to=9, reason="flashback: Sakeena remembers the gossip before her own marriage many years ago", loc="memory_lane",
         visual="a young Maldivian couple of many years ago walking along a sandy lane at a respectful distance from each other — a young woman in a maroon dress and beige headscarf and a young man in a white shirt and sarong — while two older women at a coral-stone gate whisper to each other behind their hands and glance at them",
         camera="wide shot, eye level, figures in the upper two-thirds", amb="memory", transition="dissolve"),
    dict(to=11, reason="flashback: the sorcerers brought from other islands to separate them", loc="memory_beach",
         visual="far away on a dark beach, three dark silhouettes of men sitting around a small fire with smoke curling up into the night sky, faces not visible, seen from a distance through palm trunks",
         camera="wide shot from a distance, the fire and smoke in the upper half", amb="memory", transition="dissolve",
         sens="other", safe="sorcery shown only as distant faceless silhouettes by a small fire; no rituals, objects or amulets"),
    dict(to=14, reason="back to the present: the mother's tears turn to a smile; she calls him for tea", chars=["sakeena", "shamaan"], loc="yard_morning",
         visual="Sakeena rising from the joali, wiping a tear from her cheek with the edge of her beige headscarf and smiling softly, beckoning with her other hand towards the house; Shamaan still sitting, watching her with relief in his eyes",
         camera="medium shot, eye level", amb="island_house_day", transition="dissolve"),
    dict(to=16, reason="return to the earlier two-shot: he consoles her and resolves to put his family first", reuse="beat_002",
         loc="yard_morning", amb="island_house_day", chars=["sakeena", "shamaan"],
         visual="Sakeena sitting on the joali under the big tree with a deeply worried face, hands clasped in her lap; Shamaan sitting at the other end of the joali turned towards her, explaining earnestly with an open reassuring hand"),
    dict(to=17, reason="time and scene change: Zumra arrives at the Maghrib call", chars=["zumra"], loc="gate_dusk",
         visual="Zumra stepping through the wooden gate into the sandy yard at dusk, a small bag over her shoulder, her beautiful face tense and anxious, glancing aside",
         camera="medium wide, eye level, her face in the upper third", amb="island_house_night", transition="black"),
    dict(to=22, reason="scene change: the bedroom at night; Zumra upset, Shamaan pretends not to know", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Zumra sitting on the edge of the bed with her fingertips at her temple, troubled and upset; Shamaan sitting on a wooden chair beside the bed, leaning forward and watching her with concern; both fully dressed",
         camera="medium wide two-shot, eye level", amb="room_night", sens="intimacy",
         safe="she 'bathed and lay down' and he 'lay on the bed too': shown sitting, fully dressed, bathing only mentioned"),
    dict(to=26, reason="action change: he comforts her and she looks him straight in the eye", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Shamaan and Zumra sitting side by side on the edge of the bed, his hand resting gently on her shoulder; Zumra turned towards him, looking him straight in the eyes with an intense serious expression, a silvery sparkle in her eyes",
         camera="medium close two-shot, eye level", amb="room_night", sens="intimacy",
         safe="married couple: only his hand on her shoulder, fully dressed, sitting"),
    dict(to=29, reason="memory: what his friends and relatives told him about Zumra", chars=["shamaan"], loc="memory_shop",
         visual="Shamaan standing in a sandy lane by a small corner shop, two young men and an older man in a skullcap talking to him earnestly with warning faces, one of them shaking his head; Shamaan frowning, unconvinced",
         camera="medium wide, eye level", amb="memory", transition="dissolve"),
    dict(to=32, reason="back in the bedroom: his firm promise, her fear; she sits up upset", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Zumra sitting upright on the bed, hurt and close to tears, looking down; Shamaan sitting facing her with one hand on his own chest, speaking with firm certainty",
         camera="medium two-shot, slightly from Shamaan's side", amb="room_night", transition="dissolve"),
    dict(to=37, reason="action change: he holds her hand; tears in her eyes, he nods", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Shamaan holding Zumra's hands firmly in both of his, both sitting on the edge of the bed facing each other; a tear rolling down Zumra's cheek, Shamaan nodding with a tender determined face",
         camera="medium close-up, eye level", amb="room_night", sens="intimacy",
         safe="married couple holding hands, fully dressed, sitting"),
    dict(to=39, reason="symbolic image for their promise: no storm will rock the boat of their marriage", loc="moon_lagoon",
         visual="a small wooden fishing dhoni resting calmly on a moonlit lagoon under a full moon, while dark storm clouds gather far away on the horizon; no people",
         camera="wide shot, the moon and the boat in the upper two-thirds, still water as a calm lower third", amb="island_night",
         transition="dissolve"),
    dict(to=41, reason="action change: Zumra rushes out of the room", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Zumra striding quickly out through the bedroom door into the dark corridor, glancing back over her shoulder with a tense uneasy face; Shamaan sitting on the edge of the bed behind, watching her go without moving",
         camera="medium wide, eye level", amb="room_night"),
    dict(to=43, reason="action change: she returns with a strange faint smile", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Zumra back in the room, sitting by the moonlit window with a faint mysterious smile and a silvery sparkle in her eyes; Shamaan in the soft-focus background sitting on the bed and looking away, deciding not to ask",
         camera="medium shot, Zumra in the foreground, eye level", amb="room_night"),
    dict(to=46, reason="time jump: before dawn Zumra wakes him and leaves for work", chars=["zumra", "shamaan"], loc="bedroom_predawn",
         visual="Zumra standing in the bedroom doorway ready to leave, her bag on her shoulder, speaking softly; Shamaan sitting up on the bed, drowsy, fully dressed, a light blanket over his legs, looking at her surprised",
         camera="medium wide, eye level", amb="room_night", transition="black"),
    dict(to=49, reason="time jump and character change: morning, Yameen climbs onto the bed", chars=["yameen", "shamaan"], loc="bedroom_morning",
         visual="little Yameen climbing onto the bed and tugging Shamaan's sleeve, wanting to go outside; Shamaan just waking, propped on one elbow, looking at his son with a tender, guilty face",
         camera="medium shot, eye level", amb="room_day", transition="black"),
    dict(to=53, reason="scene and character change: in the yard, the mother and Shafeena with news about Alibe", chars=["sakeena", "shamaan", "yameen"], loc="yard_morning",
         visual="Shamaan carrying little Yameen on his hip in the sandy yard; Sakeena and a neighbour woman, Shafeena (middle-aged, in a loose teal long-sleeved dress and a dark grey headscarf fully covering her hair), standing by the gate talking urgently with shocked worried faces; Shamaan listening, alarmed",
         camera="medium wide, eye level", amb="island_house_day"),
    dict(to=55, reason="scene change: Alibe's house, the yard packed with people", chars=["shamaan", "sakeena"], loc="alibe_yard",
         visual="Shamaan and Sakeena pushing through the gate into a sandy yard packed with anxious islanders, men in skullcaps and women in headscarves crowding towards the front doorway of the small house, everyone's back half-turned to the viewer",
         camera="wide shot from behind the crowd, eye level", amb="village_day", sens="violence",
         safe="Alibe and his injuries are never shown; only the crowd at the doorway"),
    dict(to=57, reason="emotional turning point: Shamaan heartbroken at the sight; the funeral", chars=["shamaan"], loc="alibe_yard",
         visual="Shamaan standing at the doorway with tears in his eyes and a hand over his mouth, heartbroken; behind him in the distance men in white carry a covered bier on their shoulders out of the yard towards the palms",
         camera="medium close-up on Shamaan, the procession small and soft in the background", amb="village_day",
         sens="violence", safe="the murdered man is never shown: Shamaan's grieving face and a covered bier at a distance"),
    dict(to=60, reason="time and scene change: home at sunset, Zumra already there smiling", chars=["zumra", "shamaan"], loc="living_dusk",
         visual="Zumra standing in the sitting room smiling broadly, bright and cheerful; Shamaan coming in through the front door, tired and sorrowful, looking at her puzzled",
         camera="medium wide two-shot, eye level", amb="home_night", transition="black"),
    dict(to=63, reason="action change: her callous words, his anger", chars=["zumra", "shamaan"], loc="living_dusk",
         visual="a tense standoff at arm's length in the sitting room: Zumra with arms folded, chin raised, a cold indifferent half-smile and contempt in her eyes; Shamaan facing her, shocked and angry, one open palm raised as if to say stop",
         camera="medium two-shot, eye level", amb="home_night", sens="other",
         safe="the argument shown only as faces and gestures at arm's length"),
    dict(to=65, reason="scene and time change: fear settles over the island; doors shut at sunset", loc="lane_dusk",
         visual="an empty sandy village lane at dusk, every wooden door and window shut, thin pale mist drifting low between the palms, no one in sight",
         camera="wide shot down the lane, eye level, the sandy lane as a calm lower third", amb="village_night", transition="black",
         sens="other", safe="the 'frightening sights' are never shown: only an empty misty lane"),
    dict(to=68, reason="scene change: after Isha only a few men hurry home; empty roads", loc="mosque_night",
         visual="three men in white skullcaps and sarongs hurrying away from the small white mosque into the empty dark lane, glancing over their shoulders nervously, seen from behind at a distance",
         camera="wide shot, eye level", amb="village_night"),
    dict(to=72, reason="scene and character change: Alibe's family decide to bring a fanditha-man", loc="veranda_night",
         visual="a group of grave Maldivian men of Alibe's family sitting close together on a lantern-lit veranda at night, an older bearded man in a skullcap speaking while the others listen and nod; women in headscarves watching sadly from the dark doorway behind",
         camera="medium wide, eye level", amb="island_night"),
    dict(to=76, reason="scene and time change: a week of waiting; Mudhimbe sprinkles recited water", loc="lane_day",
         visual="Mudhimbe, an elderly mosque caretaker with a grey beard in a white skullcap, a plain white shirt and a dark sarong, sprinkling water with his fingers from a small brass bowl at a lane corner, while a few islanders watch hopefully from behind their gates",
         camera="medium wide, eye level", amb="village_day", sens="other",
         safe="recitation shown only as sprinkling water; no script, books or amulets"),
    dict(to=79, reason="time jump: the long-awaited day; the island bustles towards the jetty", loc="lane_golden",
         visual="islanders young and old hurrying excitedly along a sandy lane towards the harbour, men in skullcaps, women in long dresses and headscarves holding children's hands, faces bright with hope, seen in warm golden light",
         camera="wide shot, eye level", amb="village_day", transition="black"),
    dict(to=81, reason="scene change: the big dhoni crossing the golden lagoon; the crowd on the jetty", loc="jetty",
         visual="a big traditional Maldivian dhoni approaching across a lagoon turned gold by the sun, a crowd of islanders waiting on the jetty in the foreground seen from behind",
         camera="wide shot over the crowd's shoulders, the dhoni and the golden sea in the upper half", amb="jetty_day"),
    dict(to=84, reason="character introduction: the famous Hassanfulhu", chars=["hassanfulhu"], loc="jetty",
         visual="Hassanfulhu standing upright at the bow of the dhoni as it nears the jetty, his white clothes glowing in the golden light, his long white beard stirring in the breeze, a calm stern steady gaze towards the island",
         camera="medium low-angle shot, eye level with the bow", amb="sea_boat"),
    dict(to=86, reason="action change: he steps ashore in silence and is welcomed", chars=["hassanfulhu"], loc="jetty",
         visual="Hassanfulhu stepping onto the jetty, an island elder in a skullcap greeting him respectfully with both hands; the hushed crowd of men behind watching in silence",
         camera="medium wide, eye level", amb="jetty_day"),
    dict(to=90, reason="scene change: Mudhimbe's veranda; the 40 strong men prepare", chars=["hassanfulhu"], loc="fenda",
         visual="Hassanfulhu sitting cross-legged on a woven mat on the veranda, calmly instructing a group of broad-shouldered young men seated on mats before him, a thin line of incense smoke rising from a small clay burner",
         camera="medium wide, eye level", amb="island_house_day"),
    dict(to=92, reason="time and scene change: dusk at the thundi; the 40 men wait, Hassanfulhu sits where the waves break", chars=["hassanfulhu"], loc="thundi_dusk",
         visual="ONLY MEN, no women anywhere: rows of young men in shirts and sarongs, some in white skullcaps, sitting cross-legged on the white sand of the sandbank tip under the big kaani tree; in front of them at the water's edge where the waves break, Hassanfulhu in white sitting cross-legged facing the sea, open palms on his knees",
         camera="wide shot from behind the rows of men, the horizon and Hassanfulhu in the upper half", amb="beach_dusk", transition="black",
         sens="other", safe="recitation shown respectfully: men seated, open palms, no books or script"),
    dict(to=97, reason="action change: as he recites, a sudden storm; he urges them to stand firm", chars=["hassanfulhu"], loc="thundi_storm",
         visual="a sudden storm over the sandbank: rain lashing down, the kaani tree bending in the wind, a flash of lightning over the sea; ONLY MEN, no women anywhere: soaked young men in shirts and sarongs shielding their faces, some leaning back in fear; Hassanfulhu standing firm at the front in his drenched white clothes, one open palm raised, calling out to them",
         camera="wide shot, eye level", amb="storm_night"),
    dict(to=100, reason="action change: after the recitation Sattar names Shamaan's wife", chars=["sattar", "hassanfulhu"], loc="thundi_after",
         visual="Sattar, soaked to the skin, speaking fearfully to Hassanfulhu by the light of a hurricane lantern; Hassanfulhu listening with a very serious face; other wet young men standing behind in the dark",
         camera="medium two-shot, eye level", amb="rain_night"),
    dict(to=102, reason="scene change: the youths walk home; the storm returns and the island sinks into darkness", loc="lane_storm",
         visual="ONLY MEN, no women anywhere: a group of five young men in shirts and sarongs hurrying along a dark sandy lane with shoulders hunched against pouring rain, a lightning flash splitting the black sky above the palms, the island plunged into darkness",
         camera="wide shot from behind the group, eye level", amb="storm_night"),
    dict(to=104, reason="character focus: Sattar alone, sheltering under the eaves", chars=["sattar"], loc="eaves_rain",
         visual="Sattar alone, pressed against a coral-stone wall under the narrow eaves of a house, soaked, arms folded against the cold, peering uneasily into the pouring rain and the dark lane",
         camera="medium shot, eye level", amb="rain_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "To Shamaan it felt as if the ground had slipped from under his feet. Remembering what Zumra had said last night, her unusual strength,")
sh(2, "and the way the room had been decorated, a powerful fear rose in Shamaan's heart.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -20)], hum=True)
sh(3, "Whenever someone is given a happy life, the envy of others is aimed at that person. With the new beginning in Shamaan's life,")
sh(4, "his mother was deeply worried because of the different stories spreading around the island. \"They are doing it out of envy.")
sh(5, "Now that I've found a good wife, they want to ruin it,\" Shamaan said, trying to make his mother understand.")
sh(6, "While many people praised his wife Zumra's character and her hard work, Shamaan knew well that hatred and envy had grown in some hearts.")
sh(7, "As she listened to Shamaan, his mother remembered something from many years ago. It was true.")
sh(8, "When Shamaan's parents were about to marry, strange stories had been told around the island too. They paid no attention to them.")
sh(9, "Had they believed such stories back then, their family would be broken today. More than the lies people told that day, they are now enjoying the sweetness of putting their trust in each other first.")
sh(10, "His mother accepted what Shamaan said. Exactly the same thing had happened to Shamaan's parents.")
sh(11, "People had even brought fanditha-men from other islands to separate them. But they were saved from those evil schemes.",
   [("fire_crackle", "ފަންޑިތަހަދާ", -24)])
sh(12, "Tears fell from his mother's eyes at those bitter memories of the past. But seeing her son's steadfastness, her heart was soothed.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(13, "\"Now come, let's have tea,\" his mother said, calling Shamaan, and walked towards the kitchen. Seeing the smile on her face, Shamaan felt a great relief.",
   [("footsteps_sand", "ހިނގައިގަތީ", -24)])
sh(14, "He was certain that a family's unity is the strongest shield against any storm.")
sh(15, "\"Now don't think about such things, all right?\" Shamaan tried to comfort his mother.")
sh(16, "He made up his mind to move forward, holding his own family's happiness far more important than other people's doubts and envy.")
sh(17, "After sunset, as the call to the Maghrib prayer sounded, Zumra arrived. Her face showed that she was somewhat anxious.",
   [("footsteps_sand", "އަތުވެއްޖެއެވެ", -22)])
sh(18, "She came straight in, bathed, went into the room and lay down. \"How tired you look,\" said Shamaan, lying down on the bed too. \"It's not tiredness.",
   [("door_close", "ވަދެ", -22)])
sh(19, "It's the things going on in this island that worry me.\" Zumra was very upset. \"What happened?\" Shamaan pretended not to know.",
   [("sigh", "ހިތްހަމަ", -22)])
sh(20, "\"Please don't play games with me. We may have to face a very big loss,\" Zumra said. Shamaan sat there frightened.")
sh(21, "He had never once seen Zumra so angry. Could Zumra have heard the stories going around the island?")
sh(22, "Surely she could not have heard them, because Zumra works away from the island.")
sh(23, "Shamaan lay there anxious. \"What's wrong? Now don't be angry, just tell me,\" Shamaan said, lovingly stroking Zumra's head.")
sh(24, "\"What has happened, and what is about to happen, is that some people are plotting to separate the two of us,\" Zumra told him. \"Who are they?\" Shamaan was alarmed.")
sh(25, "\"Shamaan, even though I am away from the island, I know everything that happens here. People who call themselves your own want to set fire to our happy life.")
sh(26, "They keep giving you bad advice and working to bring down my worth.\" Zumra let out a deep breath and looked Shamaan straight in the eyes.",
   [("breath_heavy", "ނޭވާއެއް", -22)], hum=True)
sh(27, "Shamaan's heart jolted. He remembered what his friends and some of his relatives had said recently.",
   [("heartbeat", "ތެޅިގަތެވެ", -20)])
sh(28, "They kept saying that Zumra lived far too freely away from the island, and that he should not trust her.")
sh(29, "But Shamaan did not believe those stories. Yet he had never thought they could reach Zumra.")
sh(30, "\"Zumra, I don't believe anyone's lies. However much they plot, our bond will not be shaken,\" Shamaan said with great certainty.")
sh(31, "\"I'm not afraid of what they say. But I fear that because of their evil schemes, the love for me in Shamaan's heart may grow less.")
sh(32, "Today, on the road I came by, what Siththidaitha said upset me. They say the work I do is useless, and that Shamaan is now trying to take up with another woman.\" Zumra got up and sat on the bed.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(33, "\"No, Zumra! That's a complete lie. In my heart there is no room for anyone but Zumra.", hum=True)
sh(34, "They are trying to stir up trouble between us and to separate us, ignoring the hard work Zumra does away from the island.")
sh(35, "I trust you.\" Shamaan held Zumra's hand firmly. \"Shamaan, all the work I do, I do for our future.",
   [("cloth_rustle", "ހިފާލިއެވެ", -24)])
sh(36, "If we pay attention to every story the islanders tell, they will have got what they wanted.")
sh(37, "So what I want is that whatever we hear, we tell each other.\" Tears fell from Zumra's eyes. Shamaan nodded.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(38, "Now he understood. He accepted that their love and trust had to be stronger than the schemes of envious people.")
sh(39, "In the stillness of that night, the two of them promised each other never to let any storm from outside rock the boat of their marriage.", hum=True)
sh(40, "Zumra's anxiety faded; Shamaan's sincere words brought peace to her heart. Then Zumra went out of the room very quickly.",
   [("door_open", "ނިކުތީ", -18)])
sh(41, "Her movements made it seem as if she were extremely anxious and uneasy about something. Shamaan did not follow Zumra then.")
sh(42, "He wanted to give Zumra a little time for her anger to cool and to settle down. Before long Zumra came back and lay down on the bed.",
   [("footsteps_pavement", "އެނބުރި", -24)])
sh(43, "By then a faint smile of some kind could be seen on her face. But Shamaan did not want to ask her anything about it.")
sh(44, "And so Shamaan fell asleep. He woke when Zumra came and called him. She called Shamaan before leaving for work.")
sh(45, "\"I've made food, I'm going now,\" Zumra said gently. \"So early?\" Shamaan asked in surprise.")
sh(46, "After Zumra left, Shamaan lay down again to sleep a little longer. It was almost time for the call to the Fajr prayer.",
   [("door_close", "ދިއުމުން", -22)])
sh(47, "Shamaan woke next when his son Yameen came and climbed onto the bed. Shamaan realised that, busy with the marriage, he had not paid his son much attention lately.",
   [("cloth_rustle", "އެރީމައެވެ", -24)])
sh(48, "Perhaps that is how it is when one marries after so many days alone. Yameen wanted Shamaan to take him outside.")
sh(49, "When Shamaan ignored him at first, Yameen started to cry. In the end Shamaan picked Yameen up and went outside. \"Oh, my son.",
   [("sob_breath", "ރޯށެވެ", -24)])
sh(50, "Someone has badly hurt poor Alibe,\" said Shamaan's mother, who was talking with someone else in the yard, as soon as she saw Shamaan.")
sh(51, "\"It's true! Some say they can't believe anyone from this island would dare to do such a thing,\" said Shafeena, standing beside his mother. \"Then who else would do it?",
   [("gasp", "ތެދެއް", -22)])
sh(52, "No outsiders would dare come to this island and do something like that.\" Fear rose in Shamaan's heart.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -20)])
sh(53, "\"They're even trying to find a fanditha-man now, to find out who did it,\" Shafeena added. \"Come, let's go and see Alibe,\" Shafeena said, and Shamaan and the others set off with her.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(54, "It did not take long to reach Alibe's house. The yard was packed with people.")
sh(55, "\"Alibe has just passed away,\" someone there suddenly said. Shamaan and the others moved closer to where Alibe lay.",
   [("crowd_gasp", "ނިޔާވީ", -22)], hum=True)
sh(56, "The sight broke Shamaan's heart. It was not something anyone should do to a human being. Alibe had been terribly hurt.",
   [("heartbeat", "ކުދިކުދިވިއެވެ", -20)], hum=True)
sh(57, "Shamaan truly wept. He took a leading part in everything for Alibe's funeral.",
   [("sob_breath", "ރޮވުނެވެ", -22)])
sh(58, "By the time the funeral was over and Shamaan got home, the sun had set. When he went into the house, Zumra was there.",
   [("door_open", "ވަތްއިރު", -20)])
sh(59, "Today she had come home much earlier than usual. Zumra was smiling broadly. \"You're back so early?")
sh(60, "Did work finish early today?\" Shamaan asked when he saw Zumra. \"You've come from burying Alibe, haven't you?\" Zumra began on something quite different. \"Yes,")
sh(61, "he was killed in a very cruel way,\" Shamaan replied in despair. \"Good! It was too late for him to die, even,\" Zumra said with total indifference.",
   [("gasp", "ރަނގަޅު", -22)])
sh(62, "\"Hey! Don't talk like that!\" Shamaan became very angry. \"He was a very wicked man.",
   [("breath_heavy", "ރުޅިއައެވެ", -22)])
sh(63, "A man who harmed people with sorcery,\" Zumra explained, letting out the hatred in her heart. With the news of Alibe's sudden death,", hum=True)
sh(64, "unease and fear took over that small island that had always been at peace. As frightening sights never seen before began to appear in different parts of the island,")
sh(65, "the whole island's life changed. By sunset the doors of every house were shut.",
   [("door_close", "ލައްޕާފައެވެ", -20)])
sh(66, "Apart from a few people leaving the mosque after the Isha prayer to go home, not a soul stirred on the roads.",
   [("footsteps_sand", "ނިކުންނަ", -24)])
sh(67, "Once it was afternoon, no one on the island dared even go out to the beach any more. Everyone had only one story on their lips:",
   [("wind_gust", "އަތިރިމައްޗަށް", -22)])
sh(68, "that it was the work of a jinn. And what else could one say? Nothing so evil had ever happened on that island.", hum=True)
sh(69, "With this fear added to the grief Alibe's family already bore, they decided to find a quick solution.")
sh(70, "Before the family suffered any further loss, they discussed bringing a fanditha-man from outside the island.")
sh(71, "Many on the island encouraged the decision. Everyone wanted to be freed from this evil.")
sh(72, "The family began the work of bringing the fanditha-man whose name was famous as the best in the atoll.")
sh(73, "However big the fee they had to pay him, everyone's hope was to be saved from this terrifying plague. But")
sh(74, "the earliest the fanditha-man could come to the island was a week later, and waiting that long was very hard for the islanders.")
sh(75, "Until the fanditha-man came, the island's Mudhimbe recited kiyevelli every day and sprinkled recited water over different parts of the island. But",
   [("splash", "ޖަހަމުންނެވެ", -24)])
sh(76, "nothing changed the island's fear. Everyone was waiting for the day the fanditha-man would arrive.")
sh(77, "The days passed, and today was a historic day on which joy could be seen on the islanders' faces.")
sh(78, "The bustle and excitement on the island were beyond anything usual. After a long wait, the islanders' hopes rested on him:")
sh(79, "the fanditha-man everyone had longed for was coming. As the sun's rays fell on the waves and covered the whole lagoon in gold,",
   [("wave_crash", "ރާޅުތަކުގެ", -24)])
sh(80, "a big dhoni, visible far away, drew closer to the island. On the jetty, young and old waited impatiently.",
   [("dhoni_engine", "ދޯނި", -18)])
sh(81, "The whole island seemed to have come out to welcome him; it was not just respect for one man, but trust in his skill and experience.")
sh(82, "It was the famous Hassanfulhu, known throughout the atoll. Hassanfulhu, it was said, had travelled to many atolls in the north and south of the Maldives,")
sh(83, "an experienced man who had achieved great successes in fanditha. The strength of his fanditha and")
sh(84, "the results of his treatment of the sick were famous stories told in every corner of the Maldives. As the dhoni came alongside the jetty,",
   [("dhoni_engine", "ދޯނި", -20)])
sh(85, "the sight of Hassanfulhu in a white mundu and shirt brought a hush over the whole place. His face showed patience and firmness.", hum=True)
sh(86, "As he stepped ashore, the island's leaders and people welcomed him. Hassanfulhu was to stay at Mudhimbe's house, the most trusted on the island.",
   [("footsteps_pavement", "ފޭބުމާއެކު", -22)])
sh(87, "The outer veranda of Mudhimbe's house had been prepared perfectly for Hassanfulhu. The islanders hoped that with his coming the island's troubles would be solved,")
sh(88, "and peace would return to the island. It was now the second day since Hassanfulhu came to the island. His work was set to begin today.")
sh(89, "His aim was to cut off the evil forces at work on the island and bring it peace. Hassanfulhu wanted to begin the work first at the island's thundi.")
sh(90, "So forty of the island's strongest men had prepared for it — with recitation, burning incense and other preparations.",
   [("fire_crackle", "ދުންއެޅުމާއި", -24)])
sh(91, "As sunset drew near, the forty men were at the thundi, ready for Hassanfulhu's command.")
sh(92, "Hassanfulhu had forbidden any woman to come there. After praying Maghrib, Hassanfulhu came and sat at the tip of the thundi where the waves broke.",
   [("wave_crash", "ރާޅުޖަހާ", -20)])
sh(93, "Softly he began to recite. As Hassanfulhu began reciting, the whole atmosphere changed. It was as if a great storm had come. Suddenly the wind rose,",
   [("wind_gust", "ވައިގަދަވެ", -16)], hum=True)
sh(94, "heavy rain poured down, and lightning and thunder began. Everyone there was soaked through. Though some stepped back in fear,",
   [("rain_start", "ވާރޭވެހި", -16), ("thunder", "ގުގުރަން", -14)])
sh(95, "Hassanfulhu kept urging them on. \"Be brave! Not one of you step back!\" Hassanfulhu shouted.")
sh(96, "Even in the heavy rain they obeyed Hassanfulhu and stood firm. Hassanfulhu ended the recitation when the call to the Isha prayer sounded. \"Let's go.")
sh(97, "Don't any of you be afraid,\" Hassanfulhu encouraged the young men. \"What will happen now?\" one of them asked Hassanfulhu anxiously.")
sh(98, "\"It seems some jinn girl is living on this island,\" Hassanfulhu said very seriously. \"There's no such jinn on this island.")
sh(99, "But a young man called Shamaan is married to a very strange girl. Some people say she's a jinn,\" Sattar said, very frightened.",
   [("heartbeat", "ޖިންނިއެކޭވެސް", -20)], hum=True)
sh(100, "He let out the suspicions that had grown in his heart. \"I will go to that house. But tomorrow,\" Hassanfulhu answered briefly.")
sh(101, "After taking Hassanfulhu home, the young men set off for their own homes. But they did not get far. Again there was thunder, and heavy rain began to pour.",
   [("thunder", "ގުގުރާފައި", -14), ("rain_start", "ވާރޭ", -18)])
sh(102, "The sky closed in, and the whole island sank into darkness in a terrifying way.",
   [("wind_howl", "އަނދިރިކަމުގެ", -20)], hum=True)
sh(103, "Everyone ran in different directions looking for shelter. Sattar too ran and ended up under the eaves of a house.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(104, "Since his own house was at the other end of the island, he waited there for the rain to ease.",
   [("breath", "މަޑުކޮށްލީއެވެ", -24)])
SHOTS = S

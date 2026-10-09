"""Beat/shot plan for Milahanduvaru episode 255 (used by plan_beats.py).
Shamaan and Zumra are NOT married yet: no touching of any kind between them in any image."""

LOC = {
    "show": "an open sandy ground near the beach of a small Maldivian island at night set up for a music show: a brightly lit stage with coloured lights far in the background, rows of plastic chairs, a large seated crowd on chairs and on the sand, coconut palms, strings of warm bulbs",
    "show_edge": "the dim edge of the island music-show ground at night, open sandy ground under tall coconut palms, the bright stage and the crowd far behind and small, a few low stone benches, deep shadows between the palms",
    "lane": "a narrow sandy lane on a small Maldivian island at night, low whitewashed coral-stone walls, coconut palms and a big leafy tree, the small iron gate of an old coral-stone house",
    "mother_room": "a small bedroom in an old coral-stone island house at night, a simple wooden bed with a plain cotton sheet, a small table lamp turned very low, whitewashed walls",
    "sh_room": "a simple bedroom in an old coral-stone island house at night, a wooden bed with plain sheets, a wooden-shuttered window standing open with moonlight pouring in, palm fronds outside",
    "yard": "the sandy front yard of an old coral-stone Maldivian island house at night, a traditional joali (a rope-mesh lounging seat on a wooden frame) under a big leafy tree, a low coral-stone boundary wall and a sandy lane beyond, coconut palms",
    "yard_dawn": "the sandy front yard of an old coral-stone Maldivian island house at the break of dawn, a traditional joali (rope-mesh lounging seat on a wooden frame) under a big leafy tree, a low coral-stone wall, a simple white mosque minaret far away over the rooftops",
    "room_morning": "a simple bedroom in an old coral-stone island house in the late morning, a wooden bed with plain sheets, an open doorway, bright sunlight through the wooden shutters, a plain round wall clock without numbers",
    "house_day": "the simple main room and kitchen corner of an old Maldivian island house in the morning, whitewashed walls, a small wooden table with a teapot and glass cups, an open doorway to the sunny sandy yard",
    "room_dusk": "a simple bedroom in an old coral-stone island house at sunset, a small wall mirror above a wooden chest of drawers, an open window with orange evening light",
    "yard_dusk": "the sandy front yard of an old coral-stone Maldivian island house at sunset, a traditional joali (rope-mesh lounging seat on a wooden frame) under a big leafy tree, coconut palms against an orange and violet sky",
    "beach_path": "a sandy open stretch near the beach of a small Maldivian island at night, low scaevola bushes and leaning coconut palms, the far glow of a lit music-show stage on the horizon",
    "thundi": "the sandbank tip (thundi) of a small Maldivian island at night, a huge old kaani tree with wide spreading branches, a fallen coconut trunk lying on the white sand under it, the open moonlit sea and gentle waves beyond",
    "tree_night": "a big lone leafy tree on a dark sandy stretch near the beach of a small Maldivian island at night, bushes and palms around, a faint glow of distant lights",
    "yard_wind": "the sandy front yard of an old coral-stone Maldivian island house at night as a storm arrives, palms bending in a sudden wind, the first heavy raindrops, a warm lit doorway",
    "eaves": "under the deep sloping roof eaves at the front of an old coral-stone island house at night in heavy rain, a silver curtain of rain falling from the eaves edge, puddles on the sandy yard, a warm lit doorway",
    "sitting_room": "the plain sitting room of an old coral-stone Maldivian island house at night, whitewashed walls, simple wooden chairs and a cushioned sofa, a doorway to a bedroom, a window streaked with rain",
}
MOOD = {
    "show": "night, bright coloured stage lights far away, warm bulb strings, the crowd in deep indigo shadow, busy and noisy",
    "show_edge": "night, cold silver moonlight under the palms, the warm glow of the distant stage behind, mysterious and charged",
    "lane": "late night, silver-blue moonlight on the white walls and sand, deep indigo shadows, quiet wonder",
    "mother_room": "late night, deep teal shadows and a tiny warm amber glow from the low lamp, peaceful silence",
    "sh_room": "late night, silver moonlight from the open window across the room, deep blue shadows, restless longing",
    "yard": "late night, bright full-moon silver-blue light, deep indigo shadows under the tree, still and mysterious",
    "yard_dawn": "the break of dawn, pale blue light with a first soft pink glow on the horizon, quiet and confused",
    "room_morning": "late morning, bright warm sunlight through the shutters, soft and homely",
    "house_day": "morning, soft warm tropical daylight from the doorway, homely",
    "room_dusk": "sunset, warm orange evening light from the window, restless excitement",
    "yard_dusk": "sunset turning to dusk, orange and violet sky, warm last light, dreamy anticipation",
    "beach_path": "night, cool moonlight on the sand, the far warm glow of the stage, breathless excitement",
    "thundi": "night, a bright full moon, silver moonlight on the sand and the sea, deep blue shadows under the tree, romantic and mysterious",
    "tree_night": "night, cold silver moonlight, deep shadows, uneasy and strange",
    "yard_wind": "night, sudden wind and rain, dark storm clouds, warm amber light from the doorway",
    "eaves": "night, heavy rain lit silver by the lamplight from the doorway, warm amber glow on faces, joyful surprise",
    "sitting_room": "night, warm amber lamplight indoors, the dark rainy night outside the window, tense and surprised",
}

BEATS = [
    dict(to=2, reason="episode opening: the end of the music show, Shamaan searching the crowd for Akram", chars=["shamaan"], loc="show",
         visual="Shamaan standing among the dense seated crowd at the night music show, turning his head and looking around searchingly, a little lost; the bright stage small and far behind him, a few bodu beru drummers tiny on the stage, many people seen from behind",
         camera="medium wide, eye level, Shamaan in the upper half, the sand and chair backs forming the lower third", amb="hall_crowd",
         sens="other", safe="music show shown only as a distant lit stage with small drummers and a seated crowd; no dancing"),
    dict(to=6, reason="character enters: Zumra appears behind him as he turns", chars=["zumra", "shamaan"], loc="show_edge",
         visual="at the dim edge of the show ground under the palms, Shamaan has just turned around, startled and surprised; Zumra stands about two metres away facing him with an enigmatic, indescribable faint smile and a silvery sparkle in her eyes; a clear gap between them, the bright stage far behind",
         camera="medium wide two-shot, eye level", amb="village_night"),
    dict(to=10, reason="action change: Zumra reaches for his hand, he steps back laughing", chars=["zumra", "shamaan"], loc="show_edge",
         visual="Zumra holding one hand out towards Shamaan in an inviting 'come along' gesture, her hand stopping in the air well short of him; Shamaan a step back, laughing awkwardly with one palm raised; her eyes have an unusual silvery glow and he looks at her, unsettled and fascinated; no contact, an arm's length gap",
         camera="medium two-shot, slightly low angle, faces in the upper half", amb="village_night", sens="intimacy",
         safe="the narrated hand-holding is replaced by her open inviting gesture that does not touch him; they are not married"),
    dict(to=12, reason="scene change: they walk to his house; she turns away into the night", chars=["zumra", "shamaan"], loc="lane",
         visual="at the small iron gate of Shamaan's house on the moonlit sandy lane, Zumra has already turned and is walking away down the lane, glancing back over her shoulder with a faint smile; Shamaan stands at the gate watching her go alone into the night with a puzzled, admiring look; several metres between them",
         camera="wide shot, eye level, the lane receding into the moonlit distance", amb="village_night"),
    dict(to=14, reason="scene and character change: inside the silent house, mother and son asleep", chars=["shamaan", "sakeena", "yameen"], loc="mother_room",
         visual="Shamaan peeking quietly through a half-open bedroom door; inside, his mother Sakeena lies asleep on her side on a simple bed, fully dressed in her maroon dress and beige headscarf, and little toddler Yameen in his yellow t-shirt sleeps peacefully beside her under a plain sheet; Shamaan's face soft and careful in the thin light from the doorway",
         camera="medium wide, from just behind Shamaan at the doorway", amb="island_house_night"),
    dict(to=18, reason="scene change: alone in his room, sleepless, he opens the window to the moonlight", chars=["shamaan"], loc="sh_room",
         visual="Shamaan sitting on the edge of his bed beside the open wooden-shuttered window, fully dressed, looking out at the bright moon with a restless, dreamy, troubled face, the cool night breeze stirring the curtain, silver moonlight across his face and the floor; the yard outside empty",
         camera="medium shot, eye level, from inside the room", amb="room_night"),
    dict(to=19, reason="action and location change: he lies on the joali in the moonlit yard", chars=["shamaan"], loc="yard",
         visual="Shamaan lying on his back on the joali under the big tree in the moonlit yard with his eyes closed, one arm resting on his chest, fully dressed, the empty sandy yard around him and moon-shadows of the leaves on the sand",
         camera="medium wide, slightly high angle", amb="island_night", sens="intimacy",
         safe="Zumra covering his eyes from behind is not shown; only his startle (sound) — the next image shows her standing in front of him at a distance"),
    dict(to=23, reason="character enters: Zumra stands before him with a bag and a book", chars=["zumra", "shamaan"], loc="yard",
         visual="Zumra standing on the moonlit sand a couple of metres in front of the joali, a small cloth bag over her shoulder and a closed plain book held against her chest, her face glowing softly in the moonlight with a gentle smile; Shamaan has just sat up on the joali, startled and staring at her; a clear distance between them",
         camera="medium wide two-shot, eye level", amb="island_night"),
    dict(to=24, reason="time jump: he wakes on the joali at the dawn call to prayer", chars=["shamaan"], loc="yard_dawn",
         visual="Shamaan sitting up slowly on the joali at dawn, rubbing his eyes, looking around the empty yard in confusion as if unsure whether last night was real or a dream; a faint mosque minaret far away against the pale sky",
         camera="medium shot, eye level", amb="dawn_exterior", transition="black"),
    dict(to=26, reason="time jump and character change: late morning, his mother wakes him", chars=["shamaan", "sakeena"], loc="room_morning",
         visual="Sakeena standing in the open doorway of Shamaan's sunny bedroom calling him with a hand raised; Shamaan just waking in bed under a plain sheet, fully dressed, squinting at the bright light, surprised at how late it is",
         camera="medium wide, eye level, from the foot of the bed", amb="island_house_day", transition="black"),
    dict(to=28, reason="action and character change: he takes crying Yameen from his mother", chars=["shamaan", "yameen", "sakeena"], loc="house_day",
         visual="in the main room in morning light, Shamaan, freshly washed with damp combed hair and fully dressed, lifting little Yameen from Sakeena's arms; the toddler's teary face turning towards his father and calming; Shamaan's face full of tender love; Sakeena smiling softly, the teapot on the table behind",
         camera="medium shot, eye level", amb="island_house_day"),
    dict(to=30, reason="time jump: sunset, he gets ready for the show in front of the mirror", chars=["shamaan"], loc="room_dusk",
         visual="Shamaan standing in front of a small wall mirror combing his hair in the orange sunset light, his eager impatient face seen in profile, fully dressed in his light-blue shirt; the mirror shows only a soft blurred reflection",
         camera="medium close-up, eye level, from the side", amb="island_house_day", transition="black"),
    dict(to=32, reason="action and location change: he lies on the joali at dusk dreaming of Zumra", chars=["shamaan"], loc="yard_dusk",
         visual="Shamaan lying on the joali under the big tree at dusk with his hands behind his head, gazing up at the orange and violet sky with a dreamy hopeful smile, restless and excited",
         camera="medium wide, slightly high angle", amb="island_day"),
    dict(to=38, reason="scene change: alone at the show ground before the show; the crowd fills in", chars=["shamaan"], loc="show",
         visual="Shamaan sitting on a plastic chair near the edge of the show crowd, glancing at his wristwatch impatiently and then towards the dark palms; on the distant stage people are setting up lights; more and more people are taking the seats around him, which makes him uneasy",
         camera="medium shot, eye level, the empty chairs in front forming the lower third", amb="hall_crowd"),
    dict(to=43, reason="character enters: Akram suddenly sits down beside him", chars=["akram", "shamaan"], loc="show",
         visual="Akram dropping into the chair next to Shamaan with a sly teasing grin, leaning towards him; Shamaan startled and visibly annoyed, forcing a smile and pointing away as if sending him off; the lit stage far behind",
         camera="medium two-shot, eye level", amb="hall_crowd"),
    dict(to=46, reason="action change: Akram gone, Shamaan waits alone; Zumra does not come", chars=["shamaan"], loc="show",
         visual="Shamaan sitting alone with an empty chair beside him as the show is in full swing on the distant stage, his face worried and impatient, looking over his shoulder towards the dark palms at the edge of the ground",
         camera="medium shot, from slightly behind and to the side", amb="hall_crowd"),
    dict(to=49, reason="location and character change: he joins Akram and three girls near the stage", chars=["akram", "shamaan"], loc="show",
         visual="near the brightly lit stage, Akram laughing loudly and clapping with three modestly dressed young women in long dresses and hijabs standing a little apart from the men; Shamaan beside Akram clapping half-heartedly while his eyes drift away towards the dark edge of the ground",
         camera="medium wide, eye level, the stage glow behind", amb="hall_crowd", sens="other",
         safe="the girls are modestly dressed in hijab and stand apart from the men; no dancing"),
    dict(to=50, reason="focus change: his eyes catch Zumra arriving at the edge of the crowd", chars=["zumra"], loc="show_edge",
         visual="Zumra standing alone at the dim edge of the show ground beneath tall palms, half lit by silver moonlight, looking straight towards the viewer with a soft smile and a silvery sparkle in her eyes, the crowd and stage lights blurred far behind",
         camera="medium shot, eye level, shallow depth of field", amb="village_night"),
    dict(to=53, reason="action change: Shamaan runs to her, Akram runs after him", chars=["shamaan", "akram"], loc="beach_path",
         visual="Shamaan running across the moonlit sand away from the distant lit stage with an eager face; Akram running a few steps behind him, puzzled, one hand raised calling after him",
         camera="wide shot, eye level, the figures in the upper half, open sand as the lower third", amb="beach_night"),
    dict(to=56, reason="action change: Shamaan points at someone Akram cannot see", chars=["shamaan", "akram"], loc="beach_path",
         visual="Shamaan, out of breath and beaming with joy, pointing into the dark distance between the palms; Akram beside him peering in the same direction with a confused, slightly frightened face; nobody visible where Shamaan points",
         camera="medium two-shot, eye level", amb="beach_night"),
    dict(to=60, reason="action and character change: he sits on a stone bench, Zumra sits down with him", chars=["zumra", "shamaan"], loc="show_edge",
         visual="Shamaan and Zumra sitting at opposite ends of a long low stone bench under the palms, turned towards each other and talking, Zumra smiling lovingly, Shamaan smiling back shyly; a wide empty space on the bench between them; the bright stage small and far behind",
         camera="medium wide two-shot, eye level", amb="village_night", sens="intimacy",
         safe="her head on his shoulder, him drawing her close and her taking his hand are replaced by the two sitting at opposite ends of the bench (not married)"),
    dict(to=65, reason="location change: the sandbank tip under the big tree in moonlight", chars=["zumra", "shamaan"], loc="thundi",
         visual="Shamaan and Zumra sitting at opposite ends of a fallen coconut trunk under the huge kaani tree at the moonlit sandbank tip, a clear gap between them, both turned towards each other talking softly, the full moon and the shining sea behind them",
         camera="wide shot, eye level, the tree and moon in the upper two-thirds, the white sand as a calm lower third", amb="beach_night",
         sens="intimacy", safe="walking hand in hand is not shown; they sit apart under the tree (not married)"),
    dict(to=68, reason="action change: Zumra sees Akram's group coming and jumps up in fear", chars=["zumra", "shamaan"], loc="thundi",
         visual="Zumra springing to her feet beside the fallen trunk, startled and frightened, looking towards the distance where small torch lights approach along the beach, one hand raised urgently towards Shamaan without touching him; Shamaan still seated, calm, raising a hand to tell her to wait",
         camera="medium two-shot, eye level", amb="beach_night", sens="intimacy",
         safe="her pulling his hand is shown as an urgent gesture without touching (not married)"),
    dict(to=69, reason="action change: Zumra vanishes into the darkness, Shamaan left alone", chars=["shamaan"], loc="thundi",
         visual="Shamaan sitting alone on the fallen trunk under the kaani tree, looking over his shoulder towards the dark bushes, where the slender silhouette of a young woman in a long dress and hijab, seen from behind, is dissolving into mist and shadow",
         camera="wide shot, eye level", amb="beach_night"),
    dict(to=75, reason="characters enter: Akram and his friends find Shamaan alone and tease him", chars=["akram", "shamaan"], loc="thundi",
         visual="Akram and two modestly dressed young women in hijabs standing a few metres away holding up phone torches, grinning and teasing; Shamaan sitting alone on the fallen trunk under the kaani tree, looking at them with a calm, serious face; the empty moonlit sand all around him; Akram's grin beginning to turn into unease",
         camera="medium wide, eye level", amb="beach_night",
         sens="other", safe="Akram's joke about dying alone is not visualised; the girls are modestly dressed in hijab"),
    dict(to=81, reason="action change: Akram pulls him up and the group walks away; Shamaan looks back", chars=["akram", "shamaan"], loc="beach_path",
         visual="Akram, worried and suspicious, holding Shamaan by the forearm and leading him away along the moonlit sand, two girls in hijabs walking ahead; Shamaan looking back over his shoulder towards the dark palms with a half smile, as if seeing someone the others cannot",
         camera="medium wide, eye level", amb="beach_night"),
    dict(to=83, reason="character enters and action change: Zumra draws him towards a tree", chars=["shamaan", "zumra"], loc="tree_night",
         visual="Zumra walking a few steps ahead of Shamaan towards a big lone tree in the moonlight, glancing back at him; Shamaan following reluctantly, leaning back as if pulled forward by an invisible force, a thin trail of silver mist drifting between them; no contact, a clear gap",
         camera="wide shot, eye level", amb="island_night", sens="intimacy",
         safe="her taking his hand is replaced by an unseen pull shown as a trail of silver mist; no touching (not married)"),
    dict(to=86, reason="action change: under the tree, the 'jinni?' question", chars=["zumra", "shamaan"], loc="tree_night",
         visual="Zumra and Shamaan standing face to face under the big tree at arm's length; Shamaan upset, half laughing as if joking; Zumra's face calm and serious with a cold silvery glint in her eyes; deep moon-shadows of leaves on them",
         camera="medium two-shot, eye level", amb="island_night", sens="other",
         safe="her possible jinn nature is only hinted by moonlight and a silvery glint in the eyes; she looks fully human and modest"),
    dict(to=91, reason="location change: back in his yard, they sit on the joali", chars=["zumra", "shamaan"], loc="yard",
         visual="Shamaan and Zumra sitting at opposite ends of the joali under the big tree in bright moonlight, a wide space between them; Shamaan leaning slightly towards her with an eager, enchanted face; Zumra smiling a light, patient smile, her eyes shining unusually",
         camera="medium wide two-shot, eye level", amb="island_night", sens="intimacy",
         safe="holding her hand and her cold skin are not shown; they sit apart on the joali (not married)"),
    dict(to=93, reason="action change: Zumra has vanished; Shamaan alone with his question", chars=["shamaan"], loc="yard",
         visual="Shamaan sitting alone on the joali in the moonlight staring at the empty other end of the seat where a faint wisp of silver mist is fading, his face full of questions",
         camera="medium shot, eye level", amb="island_night"),
    dict(to=95, reason="time jump: next morning, Yameen crying, he picks him up", chars=["shamaan", "yameen", "sakeena"], loc="house_day",
         visual="Shamaan just out of bed holding little Yameen against his shoulder and comforting him in the morning light; behind them Sakeena at the kitchen corner pouring tea into glass cups",
         camera="medium shot, eye level", amb="island_house_day", transition="black"),
    dict(to=99, reason="action change: at the tea table his mother scolds him; he announces a mother for Yameen", chars=["sakeena", "shamaan", "yameen"], loc="house_day",
         visual="Shamaan sitting at the small wooden tea table with Yameen on his lap, smiling happily and talking with an open hand; Sakeena standing beside the table, displeased and disbelieving, frowning, a glass of tea in her hand",
         camera="medium two-shot, eye level, the table top as the lower third", amb="island_house_day"),
    dict(to=101, reason="time jump: evening, he waits in the yard; wind and rain arrive", chars=["shamaan"], loc="yard_wind",
         visual="Shamaan, dressed neatly, standing in the dark yard glancing at his wristwatch as a sudden wind bends the palms and the first heavy raindrops fall, turning to hurry back to the lit doorway",
         camera="medium wide, eye level", amb="rain_night", transition="black"),
    dict(to=103, reason="character enters and action change: Zumra waiting under the eaves in the rain", chars=["zumra", "shamaan"], loc="eaves",
         visual="under the dripping eaves of the house, Zumra standing calm and perfectly dry in her midnight-blue dress, her face lit warmly by the doorway light; Shamaan facing her at arm's length, beaming with childlike joy, rain falling all around in a silver curtain",
         camera="medium two-shot, eye level", amb="storm_night", sens="intimacy",
         safe="his hug is replaced by the two standing face to face at arm's length, his joy shown in his face (not married)"),
    dict(to=105, reason="location and character change: inside, he calls his mother; she comes with Yameen", chars=["shamaan", "zumra", "sakeena", "yameen"], loc="sitting_room",
         visual="in the lamplit sitting room, Shamaan standing just inside the front door calling out excitedly towards the bedroom with one hand cupped beside his mouth and his other arm down at his side; Zumra standing alone more than an arm's length away from him near the door with both hands clasped in front of her and her head modestly bowed, a clear empty space between them, nobody touching; Sakeena coming out of a bedroom doorway carrying little Yameen, her face surprised and wary",
         camera="medium wide, eye level", amb="island_house_night"),
    dict(to=107, reason="character and action change: the father turns away; Sakeena leads Zumra to a chair", chars=["sakeena", "zumra", "shamaan_father", "shamaan"], loc="sitting_room",
         visual="Sakeena gently guiding Zumra by the hand to a wooden chair, Zumra sitting down with her head modestly bowed; Shamaan standing nearby smiling hopefully; in the background Shamaan's father in a bedroom doorway, turning away with a stern, doubtful glance over his shoulder",
         camera="medium wide, eye level", amb="island_house_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "As the last item of the show was being presented, it was extremely crowded near the stage.")
sh(2, "Shamaan looked in every direction, trying to spot Akram. But among the hundreds of people, Akram was nowhere to be seen.")
sh(3, "Disappointed, Shamaan decided to go home alone. \"Looking for Akram, aren't you?\" Startled by the voice behind him, Shamaan turned around.",
   [("gasp", "ސިހިފައި", -20)])
sh(4, "Standing in front of him, once again, was Zumra. On her face was a smile that could not be described. \"Do you know Akram?\"")
sh(5, "Shamaan asked in surprise. \"Oh... what a fright you got. He's here on the beach with a group of girls.\" Zumra stepped a little closer.")
sh(6, "\"I'll find them. Now go.\" Shamaan wanted to get away from Zumra as quickly as he could.")
sh(7, "His heart kept telling him that what was happening now was not good. \"No. I told them and came. Because Shamaan is going alone.")
sh(8, "Let's go. You mustn't go alone,\" Zumra said, reaching for Shamaan's hand. Shamaan laughed, freeing his hand. \"Heh-heh...")
sh(9, "You're still just a girl. I'm a man. I can get home alone,\" Shamaan said. But the unusual glow in Zumra's eyes and")
sh(10, "her movements made Shamaan's heart beat ever harder. Was tonight's meeting a coincidence?",
   [("heartbeat", "ތެޅުން", -20)], hum=True)
sh(11, "Or was it the beginning of something big to come? A faint smile came to Shamaan's lips. The two walked along talking, and when they reached Shamaan's house, Zumra turned and walked away.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(12, "At that moment Shamaan marvelled at the courage of that girl, out all alone so late at night.")
sh(13, "It was something an ordinary girl would not dare. When Shamaan went inside, complete silence had settled over everything. When he opened his mother's room,",
   [("door_open", "ހުޅުވާލިއިރު", -22)])
sh(14, "mother and child were in a deep sleep. So as not to disturb them, Shamaan went quietly to his own room.",
   [("door_close", "ވަނެވެ", -24)])
sh(15, "Tired, he wanted to fall asleep quickly, but the moment he lay down on the bed, sleep fled from his eyes.")
sh(16, "His mind was filled with thoughts of Zumra. Never having thought so deeply about a girl before, his longing to find out who she was kept growing.")
sh(17, "To calm himself, Shamaan opened the window. Outside, beautiful moonlight was shining, but as far as he could see there was no sign of life.")
sh(18, "The cool breeze blowing in brought comfort to his body, but nothing changed the unease in his heart.",
   [("wind_gust", "ރޯޅިތަކުން", -22)])
sh(19, "Finally he went out and lay down on the joali in the yard and closed his eyes. Suddenly someone came from behind and put their hands over his eyes, and Shamaan jumped.",
   [("gasp", "ސިއްސައިގެން", -18)], hum=True)
sh(20, "When he looked up with a start, there in front of him stood Zumra. A bag slung over her shoulder, a book held in her hand,")
sh(21, "her beauty shone all the more in the moonlight. \"I'm leaving on a trip. On the way I thought I'd see if Shamaan was around before I go,\" came Zumra's soft, gentle voice.")
sh(22, "\"I couldn't sleep either, so I came outside,\" Shamaan replied. \"I'm going, okay? Tomorrow night we'll meet at the very same place.\" With that, Zumra walked away.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(23, "While Shamaan was watching, she vanished from sight. Shamaan came to his senses at the sound of the call to the dawn prayer.", hum=True)
sh(24, "He was lying asleep on the joali. Was it real? Or was it a dream he had seen? With those questions he went into the house,")
sh(25, "where his mother was getting ready for prayer. Shamaan too prayed, then lay down on the bed and fell asleep. \"Son,")
sh(26, "aren't you going to play sports today?\" When Shamaan woke to his mother's call, it was already past nine o'clock.")
sh(27, "Going to make tea, his mother handed little Yameen to Shamaan. Shamaan quickly got up and washed, and when he came back, Yameen was crying in his mother's arms.",
   [("sob_breath", "ރޯށެވެ", -24)])
sh(28, "He went and picked up his child. All the joy in Shamaan's life was little Yameen. As sunset drew near, Shamaan bathed and got himself ready.")
sh(29, "To Shamaan, tonight's show seemed slow to start. His heart was pounding so hard that every minute felt like a day.",
   [("heartbeat", "ތަޅެމުންދާއިރު", -22)])
sh(30, "After combing his hair in front of the mirror, Shamaan went and lay down on the joali outside the house.")
sh(31, "His whole body was filled with a mixture of unease and joy. It wasn't just about watching the show.")
sh(32, "It was the sweet hope of meeting Zumra, the queen of his heart. As the clock struck eight, Shamaan set off with quick steps towards the music-show ground.",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -22)])
sh(33, "Because his best friend Akram was late, Shamaan didn't want to wait any longer. So he set off there, even if alone.")
sh(34, "It didn't take long to get there. Shamaan settled down and sat in the same spot where he had sat the night before.")
sh(35, "Meanwhile on the stage, the last preparations for the show were going on busily. Shamaan looked at his watch. There was still a little while before the show began.")
sh(36, "People kept arriving until the whole area was full. When people started sitting down near Shamaan too, he began to feel uneasy.")
sh(37, "Shamaan didn't want anyone there when Zumra came. He wanted to spend that enchanting moment alone with Zumra.")
sh(38, "And if he went somewhere else, he worried that Zumra wouldn't be able to find him among all the people gathered there.")
sh(39, "As he was lost in such thoughts, Akram suddenly came and sat down beside him. Shamaan jumped with a start.",
   [("gasp", "ސިހިފައި", -22)])
sh(40, "He wanted to get Akram away from there somehow. He didn't want anyone else there when Zumra came, least of all loud-mouthed Akram.")
sh(41, "\"Ran off on me again tonight, didn't you?\" Akram said with a sly grin. \"No, I came because I hadn't heard from you. Where's the girl you found last night?")
sh(42, "Go and see if those girls are there,\" Shamaan said, trying to get Akram away from there quickly. \"You have to come too tonight, Shamaan.")
sh(43, "Sitting alone like that you won't get a single girl,\" Akram said. As the show began and Shamaan wouldn't agree to go anywhere else, Akram left, fed up.",
   [("footsteps_sand", "ދިޔައީ", -24)])
sh(44, "Shamaan let out a breath of relief and began waiting for Zumra to arrive. But even as the show got going in full swing, there was no sign of Zumra.",
   [("sigh", "ނޭވާއެއްލައި", -20)])
sh(45, "Shamaan grew uneasy and felt like leaving. Had Zumra not been able to come tonight? Or had she fallen ill?")
sh(46, "His heart kept telling him that unless something had happened, Zumra would come. With that thought, his patience running out, Shamaan walked towards the stage.")
sh(47, "\"Had to give up, didn't you, mate! Didn't I tell you, sitting there you won't get a girl,\" Akram called in a mocking tone. \"I'm not looking for a girl.")
sh(48, "I got bored sitting there, so I'm going,\" Shamaan said, hiding his real purpose. Shamaan went and stopped beside Akram.")
sh(49, "They were roaring with laughter, and with Akram were three girls. Shamaan too joined in with them, clapping along.",
   [("applause", "އަތްޖަހަމުން", -24)])
sh(50, "But his eyes stayed fixed on the spot where he had met Zumra. Suddenly Shamaan's eyes caught Zumra arriving and stopping there.",
   [("heartbeat", "އަޅައިގަތީ", -22)], hum=True)
sh(51, "Without meaning to, Shamaan broke into a run towards her. Behind him, Akram, bewildered, ran too, not knowing what had happened to Shamaan.",
   [("footsteps_sand", "ދުއްވައި", -18)])
sh(52, "\"Hey, wait! Where are you running to?\" Akram shouted, running after Shamaan. When he reached a certain spot, Shamaan stopped.")
sh(53, "By then both of them were exhausted and out of breath. \"What did you run here for?\" Akram asked.",
   [("breath_heavy", "މާނޭވާ", -18)])
sh(54, "\"Because my girl came,\" Shamaan answered, bursting with joy. \"Where? Show me! There isn't a single girl here.\"")
sh(55, "Akram asked in bewilderment, looking all around. \"There, standing far off, smiling and watching,\" Shamaan said, pointing with his finger.")
sh(56, "\"You're trying to scare me! It won't work. I'm going,\" said Akram, frightened but hiding it, and walked off quickly.",
   [("footsteps_sand", "ހިނގައިގެންފިއެވެ", -22)])
sh(57, "Akram went straight off and stopped near the brightly lit stage. Shamaan sat down on a stone bench there.")
sh(58, "Within moments Zumra came and quietly sat down beside him. \"Hey, here I am,\" Zumra said in a voice full of love, laying her head on Shamaan's shoulder.",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(59, "\"I thought you weren't coming tonight,\" Shamaan said, drawing Zumra close to him. \"I was watching from afar, seeing what Shamaan would do.")
sh(60, "Even if you don't say it, I know Shamaan loves me.\" Zumra gave a light smile. When she took Shamaan's hand and set off towards the shore, Shamaan did not object either.")
sh(61, "They stopped in the shade of a big tree at the tip of the sandbank. Beautiful silver moonlight adorned the whole place. As a gentle breeze blew,",
   [("leaves_rustle", "ވައިރޯޅިއެއް", -22)])
sh(62, "apart from the music of the sea's waves, no other sound could be heard there. \"Now tell me. Which island are you from?\"",
   [("wave_crash", "ރާޅުތަކުގެ", -22)])
sh(63, "Shamaan asked eagerly. \"I'm from Malé. These days I'm staying on the farming island nearby,\" Zumra said with a smile.")
sh(64, "\"Why's that?\" Shamaan wanted to understand more. \"I come to that island very often. In the daytime I stay on that island.")
sh(65, "It's my father's island,\" Zumra answered. As they were lost in tender, loving talk,")
sh(66, "seeing Akram's group coming their way in the distance, Zumra was startled. With fear showing on her face, she hurried to leave.",
   [("gasp", "ސިހިގެން", -20)])
sh(67, "\"Let's go! There come Akram and the others,\" Zumra said, suddenly standing up and tugging at Shamaan's hand. \"Never mind.",
   [("cloth_rustle", "ތެދުވެ", -22)])
sh(68, "Wait, we'll go along with them,\" Shamaan said, quite calmly. But even though Shamaan said so, Zumra did not wait.")
sh(69, "With quick steps she slipped into the darkness nearby and vanished. When Akram and the others arrived, Shamaan was sitting there all alone.",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -22)], hum=True)
sh(70, "\"What are you doing here alone?\" Akram asked in surprise. \"Bet he's just been dumped by his girl,\" said a girl beside Akram with a sly smile.")
sh(71, "\"Sitting alone in a dark place like this, are you trying to die all by yourself?\" Akram joined in on the girl's joke, teasingly.")
sh(72, "\"No, I was sitting here with my sweetheart. When she saw you all coming, she just left,\" Shamaan said, after looking at them,")
sh(73, "quite seriously. At Shamaan's answer, Akram and his friends looked at one another, startled.",
   [("gasp", "ސިހިފައެވެ", -22)])
sh(74, "As far as they could see, Shamaan had been sitting completely alone. There was no trace of any human being anywhere around.")
sh(75, "A wave of fear rose in Akram's heart. Who was Shamaan talking about? Or had something happened to Shamaan's mind?",
   [("heartbeat", "ބިރުވެރިކަމުގެ", -20)], hum=True)
sh(76, "Or was it not a human at all? With many such questions, Akram hurriedly took Shamaan by the hand and pulled him to his feet.")
sh(77, "He realised that tonight's events were not going in the ordinary way. When Shamaan tried to introduce Zumra to his closest friends,")
sh(78, "it turned out harder than he had imagined. \"Where, show us,\" Akram looked all around. His face showed boredom and suspicion.")
sh(79, "\"She's over there, far off, watching,\" Shamaan said with a smile. He could see Zumra very clearly. But Akram and the others did not seem to see anyone at all.")
sh(80, "\"Okay, there's no need to try to fool us. We're going,\" and Akram and the others set off. Shamaan too walked after them, leaving Zumra behind.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(81, "Shamaan was very upset at the way Zumra had behaved. In front of his friends he had become a liar.")
sh(82, "Before he had gone far, Zumra came, took Shamaan's hand and led him towards a tree there. Shamaan tried not to go.")
sh(83, "But somehow, without using his own strength, he found himself beside that tree. He felt as if an unusual force was pulling him along.",
   [("wind_gust", "ދަމަމުން", -20)], hum=True)
sh(84, "\"I'm dying of shame tonight,\" Shamaan said, upset. \"So what? They won't be able to see me,\" Zumra said very confidently.")
sh(85, "That sentence raised questions in Shamaan's heart. \"You're a jinni, aren't you?\" Shamaan laughed. He said it as a joke.")
sh(86, "But at the seriousness on Zumra's face, he hesitated a little. \"Maybe, yes. Stop that talk now, let's go home.", hum=True)
sh(87, "It's nearly time for me to leave too.\" Zumra took Shamaan's hand, went and sat on the joali in the yard. Shamaan sat holding Zumra's hand.")
sh(88, "It seemed he didn't want to let Zumra go any more. The coolness of Zumra's skin and the unusual beauty in her eyes had conquered Shamaan's heart.")
sh(89, "\"So when will you meet my mother and family?\" Shamaan was impatient. He wanted to tell everyone as soon as possible that Zumra was his life partner.")
sh(90, "\"Be patient. You men are so impatient, aren't you,\" Zumra said with a light smile.")
sh(91, "The fear and doubts in Shamaan's heart faded away at Zumra's tender words.")
sh(92, "Zumra set off to leave, having agreed to meet Shamaan's mother and family tomorrow night. But the way Zumra vanished once again put a big question mark in Shamaan's heart.",
   hum=True)
sh(93, "Was he in love with a human? Or with some other creature? After Zumra left, Shamaan went into his room, changed his clothes and lay down to sleep.")
sh(94, "He was so tired that not long after lying down he fell asleep. Shamaan woke in the morning to the sound of his child crying.",
   [("sob_breath", "ރޯއަޑަށެވެ", -22)])
sh(95, "He got up and went and picked up little Yameen. At that moment Shamaan's mother was busy making tea.")
sh(96, "\"Why do you come home so late these days? You can't even spend a moment with Yameen.\" When Shamaan went and sat down at the tea table,",
   [("cup_clatter", "ސައިމޭޒު", -22)])
sh(97, "his mother said it with displeasure. \"Mum, don't be so angry. I'm trying to bring a mother for Yameen,\" Shamaan said, very happily.")
sh(98, "Finding it hard to believe, his mother asked who she was. \"She's a girl from another island. Tonight at ten o'clock she'll come to this house to meet you,\" Shamaan answered.")
sh(99, "His mother walked off without saying anything more. At seven o'clock after sunset, Shamaan was bathed and dressed.")
sh(100, "Impatiently he kept looking at the clock. Every second felt like a year.")
sh(101, "Shamaan went out into the yard and was pacing back and forth when suddenly the wind picked up and it began to rain. He quickly ran into the house.",
   [("wind_gust", "ވައިގަދަވެ", -16), ("rain_start", "ވާރޭ", -16), ("footsteps_pavement", "ދުވެފައި", -22)])
sh(102, "\"Zumra probably won't be able to come tonight,\" Shamaan said to himself. But a while later, when he looked out of the window,")
sh(103, "seeing Zumra standing under the eaves, he ran out with joy. Like a little child Shamaan threw his arms around Zumra, for he had not expected her to come.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -22)], hum=True)
sh(104, "Holding Zumra's hand, he went into the house. \"Mum! Mum!\" Shamaan called loudly.",
   [("door_close", "ވަނެވެ", -22)])
sh(105, "His mother, who was getting Yameen ready, came out of her room and asked what had happened. \"Zumra has come,\" Shamaan said. As his mother came out carrying Yameen, his father came out behind her too.",
   [("door_open", "ނުކުމެ", -22)])
sh(106, "Shamaan stood holding Zumra's hand. His father looked at them, then turned back into his room, but")
sh(107, "his mother came, took Zumra by the hand, led her to a chair and sat her down.")
SHOTS = S

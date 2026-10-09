"""Beat/shot plan for Sahar episode 477 (used by plan_beats.py).
~Two days after Deir Yassin, spring 1948: Yazan is shipped from Haifa port as a prisoner; the family shelters in
Hashim's house in Ein Karem and plans the flight to Jordan; Yazan's dream of Sahar at Al-Azhar; Claire at the door."""

LOC = {
    "haifa_road": "a dusty coastal road leading into Haifa port in spring 1948, low stone warehouses and cranes in the distance, the blue sea glimpsed beyond, pale dry ground",
    "haifa_dock": "the stone quay of Haifa port in 1948, a large old black-hulled steamship with a tall funnel and white upper decks moored alongside, a wooden gangway, coiled ropes and wooden crates on the quay, the bright Mediterranean beyond",
    "ship_stairs": "inside an elegant old 1940s passenger steamship, a polished wooden staircase with brass handrails rising between white-painted decks, round portholes, warm varnished wood panelling",
    "cabin": "a surprisingly luxurious first-class cabin on the top deck of an old 1940s steamship, a large wooden bed with a cream cover, a tall wooden wardrobe, a small old-fashioned cabinet ice-box beside the bed, a woven rug on a wooden floor, glass doors open onto a small balcony with a wide view of the open sea",
    "cabin_wash": "the small tiled washroom of an old 1940s steamship cabin, a white enamel basin, a small brass water jug, a folded white towel, soft light from a round porthole",
    "guest_room": "a simple guest room in Hashim's golden limestone house in Ein Karem, thick stone walls, an arched window with wooden shutters open onto green hills, a woven rug, a low cushioned bench along the wall, a folded blanket",
    "hall": "the living hall of Hashim's comfortable old stone house in Ein Karem, arched windows, a carved wooden sofa with embroidered cushions, woven rugs, a brass tray with coffee cups on a low table, a few books on a shelf",
    "courtyard": "the walled stone courtyard of Hashim's house in Ein Karem, a stone well with a wooden pulley and a rope bucket, potted geraniums, an almond tree, an old 1940s truck with a wooden cargo bed parked by the gate, green terraced hills beyond",
    "kitchen": "the large, well-equipped kitchen of Hashim's stone house in Ein Karem, arched stone walls, copper pots and pans hanging, clay jars, a wood-fired stone oven, a long wooden worktable with bowls of vegetables, bread and herbs, an arched window with daylight",
    "dream": "a dreamlike courtyard of an old Cairo university like Al-Azhar, rows of pale stone arches and slender columns around a sunlit courtyard, a low stone stage with a simple wooden lectern, palm fronds, no signs or writing anywhere",
}
MOOD = {
    "haifa_road": "late morning, harsh white spring sun and heat haze, oppressive and fearful",
    "haifa_dock": "late morning, hard bright sunlight, deep shadows, cold dread and humiliation",
    "ship_stairs": "late morning, warm polished light from portholes contrasting with fear, eerie elegance",
    "cabin": "midday to afternoon, soft sea light through the balcony doors, deep loneliness and grief inside beauty",
    "cabin_wash": "midday, soft pale porthole light, quiet, painful devotion",
    "guest_room": "around midday, warm spring gold daylight through the shutters, quiet and prayerful",
    "hall": "around midday, warm spring gold light through arched windows, calm but anxious",
    "courtyard": "midday, warm spring gold sunlight, green hills, a fragile calm",
    "kitchen": "midday, warm spring gold light from the window and the oven glow, tender sorrow among the women",
    "dream": "soft hazy golden dreamlike memory glow, luminous and joyful, light bloom and gentle haze",
}

BEATS = [
    # ---- Yazan: Haifa port ----
    dict(to=2, reason="episode opening: the closed iron box on the pickup arriving at Haifa port", loc="haifa_road",
         visual="an old 1940s pickup truck with a wooden cargo bed driving along the dusty road toward the port, a closed dark iron crate strapped in the back of the truck under the harsh sun, heat shimmer rising from its metal lid, cranes and a ship's funnel in the hazy distance; no people visible",
         camera="wide shot, low angle from the roadside, the truck and crate in the upper two-thirds, the dusty road as a calm lower third",
         amb="port_day", sens="violence",
         safe="Yazan locked in a hot iron box: shown only as a closed dark iron crate on a truck under harsh sun, from outside (rule 4)"),
    dict(to=7, reason="scene/action change: Yazan taken out and led along the quay to the big ship", chars=["yazan"], loc="haifa_dock",
         visual="Yazan seen from behind and slightly to the side walking slowly along the sunlit stone quay toward the gangway of a huge old steamship, head bowed, his hands together in front of him loosely wrapped in clean white cloth, his clothes dusty and creased, keffiyeh around his neck, limping slightly; a few steps behind him a tall faceless dark figure stands back-lit against the glare, only a silhouette",
         camera="medium wide shot from behind, the towering ship filling the upper two-thirds, the stone quay as a calm lower third",
         amb="port_day", sens="violence",
         safe="the handcuffing is only heard (offscreen cuffs_click); his hands are shown loosely wrapped in clean white cloth; the captor is a faceless back-lit silhouette (rule 4/9)"),
    dict(to=12, reason="emotional turning point: the captor's taunt that his family is dead", chars=["yazan"], loc="haifa_dock",
         visual="close-up of Yazan's face on the quay in hard sunlight, his curly black hair, keffiyeh around his neck, eyes wide and wet with tears, lips trembling in shock and disbelief; the long dark shadow of a man falls across his shoulder from out of frame; the ship's dark hull blurred behind him",
         camera="close-up, slightly low angle, face in the upper third, blurred dark hull below",
         amb="port_day", sens="violence",
         safe="the taunt (family dead, mother and wife left in the desert) is carried only by Yazan's stricken face; the captor appears only as a shadow"),
    dict(to=16, reason="scene change: inside the ship, taken up the stairs to the top deck", chars=["yazan"], loc="ship_stairs",
         visual="Yazan seen from below climbing a polished wooden staircase with brass handrails inside the elegant old steamship, looking around in bewildered fear at the rich wood panelling and round portholes, his hands loosely wrapped in clean white cloth, clothes dusty; above him at the top of the stairs a faceless dark back-lit silhouette of a man waits",
         camera="medium wide, low angle up the staircase, Yazan in the upper two-thirds, the lower steps as a calm lower third",
         amb="ship_deck"),
    dict(to=19, reason="scene/action change: pushed into the cabin, the door slammed", chars=["yazan"], loc="cabin",
         visual="Yazan sitting on the wooden cabin floor with his back against the side of the large bed, knees drawn up, head bowed, his hands resting loosely wrapped in clean white cloth, clothes dusty and creased; across the room the cabin door stands in shadow with only a thin line of light around it; the bright balcony doors to one side",
         camera="medium wide, eye level from the balcony side, Yazan in the upper half, the bare wooden floor as a calm lower third",
         amb="ship_cabin", sens="violence",
         safe="the push and fall are not shown: only the aftermath, Yazan sitting on the floor against the bed; the slam is an offscreen door_slam"),
    # ---- Sahar: Hashim's house ----
    dict(to=20, reason="storyline cut: Sahar wakes at the Dhuhr adhan in Hashim's house and prays", chars=["sahar"], loc="guest_room",
         visual="Sahar sitting on a simple prayer mat on the woven rug facing the bright arched window, in her black thobe with deep-red embroidery and black hijab fully covering her hair and neck, her LEFT forearm resting in a sling made from a strip of plain cloth, her right palm raised, eyes lowered in prayer, the midday light falling softly on her",
         camera="medium shot from the side and slightly behind, the window and her face in the upper two-thirds, the rug as a calm lower third",
         amb="stone_house_day", transition="black"),
    dict(to=23, reason="scene/character change: the living hall with her father Hamza and the host Hashim", chars=["sahar", "hamza", "hashim"], loc="hall",
         visual="Hamza in his red-and-white keffiyeh and Hashim with his round glasses, white beard and tweed jacket sitting on the carved wooden sofa; Hamza turned warmly toward his daughter with a gentle smile; Sahar standing a little apart in the doorway of the hall in her black thobe with red embroidery and black hijab, her LEFT forearm in a plain cloth sling, asking a question with a soft worried look",
         camera="medium wide, eye level, the three figures in the upper two-thirds, the rug as a calm lower third",
         amb="stone_house_day"),
    dict(to=27, reason="action change: Hashim urges them to leave quickly, Hamza agrees", chars=["hashim", "hamza"], loc="hall",
         visual="Hashim leaning forward on the sofa with an earnest, worried face behind his round glasses, one hand raised as he speaks; Hamza beside him in his red-and-white keffiyeh listening gravely and nodding; afternoon light through the arched window behind them, coffee cups untouched on the brass tray",
         camera="medium two-shot, eye level, faces in the upper half, the low table and rug as a calm lower third",
         amb="stone_house_day"),
    dict(to=29, reason="action change: the decision to flee to Jordan in the household truck", chars=["hashim"], loc="courtyard",
         visual="the old 1940s truck with its wooden cargo bed parked by the courtyard gate under the almond tree, Hashim standing beside it with one hand resting on the wooden side of the cargo bed, gazing toward the green hills with a deep, resolved look",
         camera="medium wide, eye level, the truck and Hashim in the upper two-thirds, the paved courtyard as a calm lower third",
         amb="garden_day"),
    # ---- Yazan: the ship at sea ----
    dict(to=32, reason="storyline cut: locked in the cabin as the ship sails into the open sea", chars=["yazan"], loc="cabin",
         visual="the luxurious cabin seen in full: the large wooden bed, tall wardrobe, small old ice-box cabinet beside the bed; Yazan standing small and alone before the open glass balcony doors, seen from behind, staring out at the endless open sea, his dusty clothes and keffiyeh, his wrapped hands hanging at his sides",
         camera="wide shot from inside the cabin, the bright balcony and sea in the upper two-thirds, the wooden floor and rug as a calm lower third",
         amb="ship_cabin", transition="black"),
    dict(to=36, reason="emotional turning point: he blames himself and weeps for his wife and mother", chars=["yazan"], loc="cabin",
         visual="Yazan sitting on the edge of the large bed bent forward, his face buried in his hands loosely wrapped in clean white cloth, shoulders shaking as he weeps, his curly black hair and keffiyeh, soft sea light from the balcony on one side and deep shadow on the other",
         camera="medium close-up, eye level, his bowed head in the upper half, the cream bed cover as a calm lower third",
         amb="ship_cabin"),
    dict(to=39, reason="action change: painful wudu in the washroom", chars=["yazan"], loc="cabin_wash",
         visual="close-up of Yazan's two hands held over a white enamel basin, loosely wrapped around the palms in clean white cloth, as clear water is poured over them from a small brass jug; the hands tremble slightly; soft pale porthole light gleams on the water drops",
         camera="close-up of the hands and jug in the upper two-thirds, the white basin as a calm lower third",
         amb="ship_cabin", sens="violence",
         safe="painful wounds during wudu: shown only as trembling hands loosely wrapped in clean white cloth under poured water, no wounds (rule 4)"),
    dict(to=41, reason="action change: he prays two rak'ahs and reminds himself of God's help", chars=["yazan"], loc="cabin",
         visual="Yazan sitting on a folded cloth on the cabin floor facing the bright open balcony doors and the sea, both palms raised in dua, his hands loosely wrapped in clean white cloth, his face in soft shadow, eyes closed, lips moving in prayer, a calm strength in his posture",
         camera="medium shot from the side, his face and raised hands in the upper two-thirds, the wooden floor as a calm lower third",
         amb="ship_cabin"),
    # ---- the kitchen in Hashim's house ----
    dict(to=43, reason="storyline cut: the women cook lunch in the big kitchen", chars=["safoora", "laila", "fathimaa"], loc="kitchen",
         visual="the spacious stone kitchen with copper pots and clay jars; Safoora in her olive-green thobe with orange embroidery and white headscarf stirring a copper pot at the oven, Laila in her indigo thobe and long white headscarf kneading dough at the long worktable, Fathimaa in her forest-green thobe and cream headscarf chopping herbs, all headscarves fully covering hair and neck, quiet sorrow on their faces as they work",
         camera="wide shot, eye level, the three women in the upper two-thirds, the long worktable top as a calm lower third",
         amb="stone_house_day"),
    dict(to=44, reason="character/location change: Sahar talks with her brother Ameen at the well", chars=["sahar", "ameen"], loc="courtyard",
         visual="Ameen in his grey shirt pulling the rope of the stone well with a wooden bucket of water, smiling shyly at his sister; Sahar standing beside the well in her black thobe with red embroidery and black hijab, her LEFT forearm in a plain cloth sling, with a faint sad smile; potted geraniums and the almond tree in sunlight",
         camera="medium shot, eye level, the two faces in the upper half, the paved courtyard as a calm lower third",
         amb="garden_day"),
    dict(to=48, reason="character focus: Laila grieves over Sahar and Yazan's short marriage", chars=["laila", "safoora"], loc="kitchen",
         visual="Laila standing at the worktable with her hands resting still on the dough, in her indigo thobe and long white headscarf, her eyes full of tears as she speaks in a trembling voice; Safoora beside her in her olive-green thobe and white headscarf, listening with deep compassion; warm window light on their faces",
         camera="medium two-shot, eye level, faces in the upper half, the floured worktable as a calm lower third",
         amb="stone_house_day"),
    dict(to=51, reason="action change: Safoora consoles Laila - Yazan is alive", chars=["safoora", "laila", "fathimaa"], loc="kitchen",
         visual="Safoora holding both of Laila's hands in hers and looking into her eyes with a firm, hopeful expression; Laila's tearful face lifting a little; behind them Fathimaa in her forest-green thobe and cream headscarf wiping her eyes with the end of her headscarf; all headscarves fully covering hair and neck; soft window light",
         camera="medium shot, eye level, the faces in the upper two-thirds, the worktable as a calm lower third",
         amb="stone_house_day"),
    dict(to=54, reason="character enters: Sahar comes into the kitchen; the mothers hide their tears", chars=["sahar", "safoora", "fathimaa", "laila"], loc="kitchen",
         visual="Sahar standing in the arched kitchen doorway in her black thobe with red embroidery and black hijab, her LEFT forearm in a plain cloth sling, her face composed but her eyes sad, pretending not to notice; inside, Safoora turns toward her with a warm smile while Fathimaa and Laila quickly wipe their eyes, turned half away",
         camera="medium wide from inside the kitchen toward the doorway, faces in the upper two-thirds, the stone floor as a calm lower third",
         amb="stone_house_day"),
    # ---- Yazan's dream ----
    dict(to=56, reason="flashforward dream: Sahar graduates first as a doctor at Al-Azhar", chars=["sahar"], loc="dream",
         visual="Sahar healthy and radiant, both arms free, wearing a black graduation gown over her black thobe with red embroidery and her black hijab fully covering hair and neck, holding a rolled paper scroll tied with a red ribbon, stepping down from the low stone stage and running joyfully across the sunlit arched courtyard toward the viewer, her face shining with happiness",
         camera="medium wide, slightly low angle, Sahar in the upper two-thirds, the sunlit courtyard flagstones as a calm lower third",
         amb="dream_glow", transition="dissolve", sens="intimacy",
         safe="the narration's 'houri on her wedding night' comparison is not depicted; Sahar is shown fully covered in a graduation gown"),
    dict(to=57, reason="action change in the dream: they meet - hands held at arm's length", chars=["sahar", "yazan"], loc="dream",
         visual="in the glowing arched courtyard, seen from the side: Sahar in a loose black graduation gown over her black thobe and her black hijab fully covering hair and neck, and Yazan in his clean shirt and keffiyeh, standing a full arm's length apart with their arms stretched out straight between them, only their hands joined, a clear open gap of golden light between their bodies, both smiling with tears of joy, the rolled scroll with a red ribbon in her other hand",
         camera="medium wide two-shot, eye level, their faces in the upper half, the flagstones as a calm lower third",
         amb="dream_glow", sens="intimacy",
         safe="the narration's tight embrace is replaced by the married couple holding hands at arm's length (rule 6)"),
    dict(to=58, reason="return to the earlier image: he wakes during his dua and weeps", chars=["yazan"], loc="cabin",
         reuse="beat_013", transition="dissolve", amb="ship_cabin", visual="(reuse of beat_013)"),
    # ---- Claire at the door ----
    dict(to=61, reason="character enters: the knocking, a tall young crew woman at the open door", chars=["claire", "yazan"], loc="cabin",
         visual="seen from deep inside the cabin toward its wooden entrance door, which stands wide open onto a narrow wood-panelled ship corridor with brass wall lamps: Claire, a tall young French crew woman in a navy ankle-length uniform with brass buttons and a navy headscarf fully covering her hair and neck, stands outside in the corridor beyond the threshold with her arms folded; Yazan stands well inside the cabin near the bed, his hand still raised from opening the door, at least two arm's lengths away from her, his eyes reddened, looking at her warily; clear empty space between them; the balcony and sea are behind the viewer, not visible",
         camera="medium wide from inside the cabin toward the open door, both in the upper two-thirds, the wooden floor as a calm lower third",
         amb="ship_cabin"),
    dict(to=65, reason="action change: Yazan answers with head bowed; she offers to explain on the balcony", chars=["claire", "yazan"], loc="cabin",
         visual="Yazan standing near the bed with his head bowed and his wrapped hands hanging at his sides; Claire in her navy uniform and navy headscarf standing on the threshold of the wide-open cabin door, far from him, one hand gesturing calmly toward the bright open balcony with a chair and the sea; her face serious and composed",
         camera="wide shot, eye level, the open door, the two figures far apart and the balcony in the upper two-thirds, the floor and rug as a calm lower third",
         amb="ship_cabin", sens="other",
         safe="Claire and Yazan never close: she stays by the open door, well over two arm's lengths away, no romantic framing (rule 8)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "After about five hours of driving, the pickup carrying Yazan reached the area of Haifa Port. It was eleven in the morning.",
   [("engine_rev", "ދުއްވުމަށްފަހު", -22)])
sh(2, "Because he had been put inside an iron box, Yazan could feel the heat on his body. The fear that had taken hold of his heart kept growing.",
   [("heartbeat", "ބިރުވެރިކަން", -22)])
sh(3, "\"For what purpose have they brought me here?\" Yazan kept asking himself. A little later a soldier came and took Yazan out of the box.",
   [("metal_door", "ނެރުނެވެ", -18)])
sh(4, "He put cuffs on both of his hands, then began leading Yazan towards a big ship lying at the port. \"Where are you taking me?",
   [("cuffs_click", "ބިޑި", -18), ("footsteps_pavement", "ގެންދަންފެށިއެވެ", -22)])
sh(5, "Where are you sending me on that ship? Let me go to my family.\" Yazan was close to tears. Because Yazan spoke in English,",
   [("sob_breath", "ރޮވޭ", -24)])
sh(6, "the man too began to answer him. \"You're very ungrateful, aren't you? Be glad that you are being let go without being killed.")
sh(7, "We don't want you anywhere within smelling distance of this region.\" The man spoke loudly. \"Why didn't you kill me?\"")
sh(8, "Yazan said in a trembling voice. \"You people are rich and generous. We wanted to loot the wealth of the rich living in Deir Yassin and make the poor there even poorer.",
   [("breath_heavy", "ތުރުތުރު", -22)])
sh(9, "That is how our power will last. We hate you people. Your whole family is dead.",
   [("heartbeat", "މަރުވެއްޖެ", -20)], hum=True)
sh(10, "When you were arrested, your mother and your woman were left in the desert because we knew the two of them would die there.",
   hum=True)
sh(11, "And I'll tell you: we kept you in this world so that you would feel the grief and pain of it. We want to make you people suffer,\" the tyrant went on arrogantly.")
sh(12, "His words revealed that the soldiers had taken over the area where Yazan's family lived in a carefully planned way.")
sh(13, "However crushed he was, Yazan kept up his courage. The man put Yazan on board and began climbing a staircase.",
   [("footsteps_pavement", "ސިޑިއަކުން", -22)])
sh(14, "Beautifully designed, the ship seemed to Yazan like the kind of ship very cultured people travel on.")
sh(15, "Although he had lived a comfortable life, this was the first time Yazan had seen such a ship. The man took Yazan up to the third deck of the ship.")
sh(16, "Yazan sensed that this was the very top of the ship. \"Please, where are you taking me?\" Yazan asked in a pleading voice.")
sh(17, "But the hard-hearted man said nothing; he opened the door of a cabin on the ship, pushed Yazan into the cabin and knocked him down.",
   [("door_open", "ހުޅުވާ", -20), ("soft_thud", "ވައްޓާލިއެވެ", -18)])
sh(18, "\"Off to the place you'll live. Don't even think of coming back to this region,\" the soldier said in a heavy, warning voice.")
sh(19, "Then he slammed the cabin door hard and went back down. Sahar woke to the sound of the midday call to prayer.",
   [("door_slam", "ލެއްޕުމަށްފަހު", -14)])
sh(20, "As soon as she woke, Sahar got up and looked for her mother and the others. Seeing no one, she went into the washroom, made wudu and prayed.",
   [("cloth_rustle", "ތެދުވެ", -24), ("pour", "ވުޟޫކޮށްގެން", -24)])
sh(21, "Then she left the room and came out to the living hall of the house. On a sofa in the hall sat Sahar's father Hamza and Hashim, the owner of the house.",
   [("footsteps_pavement", "ނިކުމެލިއެވެ", -24)])
sh(22, "\"Your mother and the others are in the kitchen. They were worried because you didn't wake up. Go and let them see you,\" Hamza said tenderly. \"Where's my little brother?\"")
sh(23, "Sahar asked, since Ameen was nowhere to be seen. \"He's drawing water for the mothers. Drawing water from that well is no easy job either,\" Hashim explained.",
   [("water_splash_small", "ފެންނެގުމަކީ", -24)])
sh(24, "Hashim was told what had happened to Hamza and his family. Hashim sat listening closely. After spending a while like that, Hashim spoke.")
sh(25, "\"I think we should leave this area quickly. Very soon they will start trying to take over this area too. This moment is like the wind")
sh(26, "blowing between two clouds. If we don't make use of this moment, we'll be caught again.\" Hashim was an aware man who had been to many countries of the world.")
sh(27, "His thoughts were already on the danger that would come next. \"What you say is right. I too think we should leave this area as soon as we can.")
sh(28, "Almighty Allah will never let a servant be lost who emigrates seeking His noble face,\" Hamza said, agreeing with Hashim. \"Safoora and I were given two children.")
sh(29, "Both of them are studying in Jordan. Let's set off in this house's truck. There's room for everyone in it,\" Hashim said, letting out a deep breath.",
   [("sigh", "ނޭވާއެއް", -22)])
sh(30, "The man had left after locking Yazan in a cabin. Which way the ship was sailing, or to what country, he did not know.",
   [("lock_click", "ތަޅުލާފައެވެ", -20)])
sh(31, "In Yazan's cabin there was a big bed and a wardrobe. And beside the bed stood a small refrigerator too.")
sh(32, "With a washroom with a shower and a balcony looking out to sea, the cabin was lovely. But however lovely it was,")
sh(33, "Yazan's life now lay in pieces. His beloved wife and his mother were lost in the desert. If wild dogs didn't kill them,")
sh(34, "the two of them might still die of hunger and heat. \"What happened to the two of them happened because of me. What a coward I am. Into the hands of cruel people,",
   hum=True)
sh(35, "people worse than wild beasts, mother and Sahar were left because of me. Because of me alone.\" Blaming himself,",
   hum=True)
sh(36, "Yazan began to weep. But however distressed and restless he was, what else could he do? To entrust everything to Almighty Allah,",
   [("sob_breath", "ރޮވެން", -22)])
sh(37, "and to pray more and more for His good mercy - Yazan had no other way. So he went into the washroom, made wudu and prayed two rak'ahs.",
   [("pour", "ވުޟޫކޮށް", -18)])
sh(38, "Because of what the soldiers had done to him, even making wudu was something that sent pain through all four of Yazan's limbs.")
sh(39, "The places where he had been scraped were still raw. Even when a drop of water touched them, the sting made his body shake.",
   [("water_splash_small", "ފެންފޮދެއް", -22)])
sh(40, "But Yazan was a strong-hearted young man, and he kept proving it. In these two days Yazan had seen so much that would make a person despair.")
sh(41, "Yet that there is One more powerful than all, and that from Him would come the full reward for this hardship, Yazan kept repeating")
sh(42, "and reminding himself. With Safoora, everyone was busy in the kitchen getting lunch ready.",
   [("cup_clatter", "ހަރަކާތްތެރިވަމުން", -22)])
sh(43, "That spacious kitchen was so lovely that anyone who liked to cook could keep at it without growing tired. As befitted the times,")
sh(44, "every utensil a kitchen could need was there. After stopping to talk with Ameen, who was at the well, Sahar went towards the kitchen.",
   [("water_splash_small", "ވަޅުދޮށުގައި", -24)])
sh(45, "\"I keep thinking about Sahar. Even if she doesn't speak of it, how much the poor girl's heart must hurt. Their marriage lasted only a few days, but")
sh(46, "they lived so lovingly. At night too they would stay up on the terrace until very late, talking about their hopes for the future,")
sh(47, "talking about the work they would do to make the dreams they saw come true. What a beautiful, happy life we were living.")
sh(48, "Today everything has fallen apart. I've grown weary of life,\" Laila said in a voice full of sorrow and pain. \"Be patient, Laila!",
   [("sob_breath", "ފޫހިވެއްޖެ", -24)], hum=True)
sh(49, "I know I may not be able to truly feel the pain in your heart and how it weighs on you. Your husband and one child were martyred.")
sh(50, "You don't even know whether Yazan is alive or not. But my heart tells me that, God willing, Yazan is alive.")
sh(51, "That boy will come to us. And we will meet him again. Yazan is a brave boy, strong in his faith.\"")
sh(52, "Fathimaa too was close to tears. Their talk came to an end when they saw Sahar coming into the kitchen. \"Sahar, habeeba.",
   [("sob_breath", "ރޮވޭ", -24), ("footsteps_pavement", "ވަދެގެން", -24)])
sh(53, "Tell the fathers to come and eat,\" Safoora said kindly. Sahar acted as if she hadn't heard what they had been saying.")
sh(54, "And acting as if she didn't see the mothers wiping their eyes, she left the kitchen. Yazan is seeing Sahar.",
   [("footsteps_pavement", "ނިކުމެގެންދިޔައެވެ", -24)])
sh(55, "Among the doctors graduating from Al-Azhar University, it was Sahar who graduated first. In her ceremonial gown, Sahar looked like a heavenly maiden ready for her wedding night.",
   hum=True)
sh(56, "Holding her doctor's certificate, Sahar came down from the stage and ran towards Yazan. When Sahar reached him,",
   [("footsteps_pavement", "ދުވެފައި", -26)], hum=True)
sh(57, "he held Sahar tightly. And with that Yazan woke, as someone began knocking on the door.",
   [("knock", "ޖަހާ", -16)])
sh(58, "Yazan realised he had fallen asleep while making dua after his prayer. \"O Allah, decree a way for this servant and this servant's wife to live together.\" Yazan burst into heavy tears.",
   [("sob_breath", "ރޮއެ", -22)], hum=True)
sh(59, "Again the loud knocking began on the door. He sat up straight, wiped his eyes, and fearfully opened the cabin door.",
   [("knock", "ޖަހާ", -14), ("door_open", "ހުޅުވާލީ", -20)])
sh(60, "Outside stood a tall, young, beautiful woman. From the clothes she wore, Yazan knew she was one of the ship's crew. \"What's happened?\"")
sh(61, "Yazan asked fearfully. \"I've come to tell you how the voyage will go. You're the prisoner brought from the Deir Yassin area of Palestine, aren't you?\"")
sh(62, "the woman said, standing facing Yazan with her arms folded. \"Yes. But I don't know what my crime is,")
sh(63, "or the reason I had to be put on this ship as a prisoner,\" Yazan said, standing with his head bowed. \"I didn't ask why you were brought as a prisoner, did I?")
sh(64, "I know how things are going. Let's sit on the chairs out on the balcony. How things have happened,")
sh(65, "and how things will happen next, I'll tell you,\" the woman said as she walked into the cabin.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -24)])
SHOTS = S

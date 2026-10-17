"""Beat/shot plan for Vaanama Iraadhiagai episode 549 (series opener; used by plan_beats.py)."""

LOC = {
    "island_morning": "a small inhabited Maldivian island in the morning: wide white coral-sand lanes lined with coconut palms and low coral-stone garden walls, small single-storey houses with tin roofs, a little harbour with wooden dhonis at the end of the lane, a turquoise lagoon sparkling beyond",
    "house_front": "the front of the family's small single-storey island house: whitewashed coral-stone walls, a tin roof, a shady veranda with a wooden bench, a low coral-stone garden wall with a gate, a coconut palm and a big leafy tree with a rope joali swing-seat beneath it, a clean swept white-sand yard",
    "memory_veranda": "the same small island house veranda remembered long ago: a simple empty wooden chair, an old faded fisherman's cap hanging on a nail on the whitewashed wall, an old fishing rod leaning in the corner",
    "bedroom": "Luyoon's small tidy bedroom in the island house: whitewashed walls, a wooden window with pale curtains, a single neatly made bed with a light cover, a small wooden wardrobe, a wooden door open onto the corridor",
    "living": "the simple bright main room of the island house: whitewashed walls, a small wooden dining table with a woven mat, a tray of glass tea cups and a teapot, a short-eats plate, a cabinet, a ceiling fan, an open door to the veranda showing palms",
    "lane_afternoon": "a long white coral-sand lane of the island leading between coconut palms and coral-stone walls towards the shore, the turquoise sea glimpsed at the end",
    "sandbank": "the island's sandbank point (finolhu): a long tongue of white sand curving into a shallow turquoise lagoon, gentle waves washing over the sand, a few coconut palms at its base, the open sea and a wide sky",
    "dusk_lane": "a quiet coral-sand island lane at dusk, coconut palms in silhouette, house windows beginning to glow, a small island mosque with a white minaret and a lit doorway at the end of the lane",
    "living_night": "the same simple main room of the island house in the evening: whitewashed walls, a wooden cabinet, a small table, a basket of folded laundry, warm lamp light, the window dark blue",
    "prayer_room": "the sisters' small bedroom at night: whitewashed walls, two prayer mats laid side by side on the tiled floor facing a plain wall, a small warm lamp on a shelf",
    "gate_dusk": "the family house gate and coral-sand lane at blue dusk, the veranda lamp glowing amber, palm fronds dark against a fading sky",
    "joali_night": "the swept sandy yard in front of the family house at night: a rope joali swing-seat under a big leafy tree, the house veranda lamp glowing warm amber behind, coconut palms, a vast starry sky with the Milky Way above the island",
}
MOOD = {
    "island_morning": "bright morning, clear sky-blue sky with soft white clouds, sparkling turquoise sea light, fresh and peaceful, everyday island life",
    "house_front": "bright morning sunlight, soft lens glow, warm and proud, gentle breeze in the palms",
    "memory_veranda": "soft hazy pastel memory glow, faded warm light, quiet longing and loss",
    "bedroom": "bright morning sunlight streaming through the window, dust motes glowing, playful and lively",
    "living": "bright morning light, warm cosy family atmosphere, playful and teasing",
    "lane_afternoon": "golden afternoon, long warm shadows, glowing sky, joyful sibling laughter",
    "sandbank": "orange-pink sunset, cherry-pink and gold clouds, the sun glowing on the horizon, sparkling sea, peaceful and dreamy",
    "dusk_lane": "blue dusk after sunset, the last pink glow on the horizon, the first stars, warm lamp lights, a hurried but gentle mood",
    "living_night": "evening, warm amber lamp light against blue night at the window, cosy and comic",
    "prayer_room": "night, soft warm lamp light, calm, devout and peaceful",
    "gate_dusk": "blue dusk, warm amber lamp light from the veranda, tired but content",
    "joali_night": "moonlit night, deep blue sky full of glittering stars, warm amber lamp light from the veranda, perfect stillness, tender and intimate between mother and daughter",
}

BEATS = [
    dict(to=2, reason="episode opening: establishing the island on a calm clear morning", loc="island_morning",
         visual="a sweeping wide anime establishing shot of the island lane in the morning: in the middle distance small background figures of women in modest long dresses and headscarves fully covering hair sweeping the white sand with long palm-rib brooms; further away at the little harbour tiny fishermen in t-shirts and long trousers loading a wooden dhoni; coconut palms swaying, a dazzling turquoise lagoon, soft white clouds and lens glow",
         camera="wide establishing shot, slightly high angle, the lane leading the eye into the picture, the sky and harbour in the upper two-thirds, the smooth white sand lane as a calm lower third",
         amb="village_day"),
    dict(to=4, reason="character introduction: Luyoon, the brave eldest daughter; her mother proud of her", chars=["luyoon", "aishath"], loc="house_front",
         visual="Luyoon (about 20) standing confidently at the open gate of the family house in her cream-white abaya-style dress and black hijab fully covering her hair and neck, chin raised, a brave bright smile, the morning breeze lifting the edge of her hijab, anime sparkle in her eyes; behind her on the shady veranda her mother Aishath in maroon libaas and beige headscarf watches her with a proud gentle smile",
         camera="medium full shot, low angle on Luyoon, Aishath smaller in the background", amb="island_house_day"),
    dict(to=5, reason="characters change: introducing the three siblings, Luyoon the eldest", chars=["luyoon", "zaina", "nawfal"], loc="house_front",
         visual="the three siblings standing side by side in the sunny yard in front of the house like a family portrait: Luyoon the tallest in her cream-white dress and black hijab, her younger sister Zaina (about 13) in a sky-blue dress and white hijab fully covering her hair, grinning, and their little brother Nawfal (about 10) in a yellow t-shirt and navy shorts making a cheeky peace sign; all smiling warmly",
         camera="medium wide, eye level, the three in the upper two-thirds, the white sand yard as the lower third", amb="island_house_day"),
    dict(to=7, reason="flashback: the father passed away when Luyoon was 12; the mother raised the three alone", loc="memory_veranda",
         visual="a soft hazy pastel memory: an empty simple wooden chair on the old veranda, an old faded fisherman's cap hanging on a nail on the whitewashed wall above it, an old fishing rod leaning in the corner, afternoon light falling gently across the empty seat, a few fallen leaves; nobody present",
         camera="medium shot, eye level, the chair and cap in the upper two-thirds, the worn veranda floor as a calm lower third",
         amb="memory", transition="dissolve", sens="other",
         safe="the late father is never shown as a person; his absence is shown with an empty chair, his old cap and fishing rod"),
    dict(to=13, reason="time/scene change: back to the present morning — Zaina shouts at Luyoon's door to wake her", chars=["zaina", "luyoon"], loc="bedroom",
         visual="Zaina in her sky-blue dress and white hijab standing in the open bedroom doorway, hands cupped round her mouth calling loudly with a mischievous grin; Luyoon sitting up on the edge of her neatly made bed, fully dressed in her cream-white dress and black hijab fully covering her hair and neck, rubbing one sleepy eye with a comically grumpy anime pout, no bag; morning sunbeams through the window showing only coconut palms and the turquoise lagoon, no city buildings",
         camera="medium wide, eye level, from inside the room towards the doorway", amb="room_day", transition="dissolve",
         sens="clothing", safe="waking scene: Luyoon is shown sitting up on the bed edge fully dressed in her hijab, never lying in bed or in bedtime clothes"),
    dict(to=15, reason="action change: Luyoon comes out to the main room and the younger siblings tease her as 'the queen of the house'", chars=["luyoon", "zaina", "nawfal"], loc="living",
         visual="Luyoon walking into the bright main room, neatly straightening the edge of her black hijab with one hand, fully covered, rolling her eyes with a small embarrassed smile; at the dining table Zaina and Nawfal giggle and bow towards her in a playful mock royal greeting; a tray of glass tea cups and a teapot on the table",
         camera="medium wide, eye level", amb="home_day", sens="clothing",
         safe="the bathroom and the hair-combing are not shown; she is seen afterwards, adjusting her hijab"),
    dict(to=17, reason="character enters: Aishath scolds the bickering children while Luyoon drinks her tea", chars=["aishath", "luyoon", "zaina", "nawfal"], loc="living",
         visual="Aishath in maroon libaas and beige headscarf standing by the table with hands on her hips, half-stern half-smiling as she scolds; Zaina and Nawfal shrinking sheepishly in their chairs with anime sweat drops; Luyoon calmly seated sipping tea from a glass cup with an innocent face; breakfast short eats on the table",
         camera="medium wide, eye level, faces in the upper two-thirds, the table top as the lower third", amb="kitchen_busy"),
    dict(to=22, reason="time and scene change: in the afternoon the three siblings walk to the sandbank", chars=["luyoon", "zaina", "nawfal"], loc="lane_afternoon",
         visual="the three siblings walking down the long white coral-sand lane towards the shore in golden afternoon light, seen from slightly behind and to the side: Nawfal skipping ahead looking back laughing, Zaina telling a story with lively hand gestures, Luyoon laughing beside them; long warm shadows on the sand, palm fronds glowing, the turquoise sea shimmering at the end of the lane",
         camera="wide tracking shot, eye level, the figures in the middle third, the sunlit sand lane as the lower third", amb="village_day"),
    dict(to=24, reason="scene change: at the sandbank at sunset — Zaina meets classmates; the waves at their feet", chars=["luyoon", "nawfal", "zaina"], loc="sandbank",
         visual="the sandbank at sunset: in the foreground Luyoon in her cream-white dress and black hijab and Nawfal stand at the water's edge, small waves washing over their bare feet, gazing at a huge glowing sun sinking into the sea; a little further up the sand Zaina chats and laughs with two background classmate girls in plain long dresses and white hijabs; cherry-pink and gold clouds, the sea sparkling",
         camera="wide shot from behind and to the side, the sun and sky in the upper two-thirds, the wet shining sand and foam as a calm lower third", amb="beach_evening"),
    dict(to=27, reason="time change: dusk falls; they hurry home and Nawfal turns off to the mosque", chars=["nawfal", "luyoon", "zaina"], loc="dusk_lane",
         visual="the coral-sand lane at blue dusk: Nawfal running towards the small white-minaret mosque at the end of the lane where a warm light glows in the doorway; Luyoon and Zaina walking quickly the other way on the near side of the lane, glancing back at him; the first stars appearing, house windows glowing amber",
         camera="wide shot, eye level, the minaret against the dusk sky in the upper third, the pale sand lane as the lower third",
         amb="night_lane", sens="other", safe="mosque shown only as a respectful exterior; no adhan sound"),
    dict(to=29, reason="scene change: at home Zaina complains to their mother about Luyoon", chars=["zaina", "aishath", "luyoon"], loc="living_night",
         visual="Zaina, her face fresh and damp from washing, wearing her white hijab and sky-blue dress, pointing at Luyoon and complaining with an exaggerated anime pout; Aishath sitting on a low bench calmly folding laundry, unbothered, not even looking up; Luyoon standing behind with arms folded and an amused smirk",
         camera="medium wide, eye level", amb="home_night"),
    dict(to=30, reason="action change: the two sisters go to their room to pray", chars=["luyoon", "zaina"], loc="prayer_room",
         visual="the two sisters seen from behind, small and respectful, standing side by side on two prayer mats, BOTH wrapped in identical long plain pure-white prayer covers (loose white robes draping from the top of the head down to the feet, no coloured clothing visible), no bags or other items on them, the warm lamp glowing softly on the wall before them",
         camera="medium wide, from behind at eye level, the figures in the upper two-thirds, the patterned prayer mats and tiled floor as the lower third",
         amb="room_night", sens="other", safe="prayer shown from behind on prayer mats in full prayer dress; no text"),
    dict(to=31, reason="time jump: days pass; Luyoon comes home from work at dusk, exhausted", chars=["luyoon"], loc="gate_dusk",
         visual="Luyoon pushing open the garden gate at blue dusk, coming home from work in a plain pastel office abaya and black hijab fully covering her hair, a lanyard with a blank card around her neck, her brown shoulder bag hanging heavy, shoulders drooping, tired half-closed eyes and a weary small smile at the glowing veranda lamp",
         camera="medium shot, eye level, slightly low", amb="village_night", transition="black"),
    dict(to=32, reason="return: however tired, she prays before resting (story returns to the prayer image)", loc="prayer_room",
         reuse="beat_012", amb="room_night", sens="other", safe="reused respectful prayer image from behind",
         visual="(reuse of beat_012)"),
    dict(to=34, reason="time and scene change: one silent night — Aishath lost in thought on the joali; Luyoon comes to sit beside her", chars=["aishath", "luyoon"], loc="joali_night",
         visual="Aishath in maroon libaas and beige headscarf reclining on the rope joali under the big tree, gazing up thoughtfully at the night sky; Luyoon walking up slowly and sitting down at the other end of the joali, turning towards her mother with gentle concern; warm veranda light behind, a sky full of stars",
         camera="medium wide, eye level, the two and the tree in the upper two-thirds, the moonlit sand as the lower third", amb="island_house_night", transition="black"),
    dict(to=37, reason="emotional turning point: missing the late father; mother and daughter gaze at the stars", chars=["aishath", "luyoon"], loc="joali_night",
         visual="close two-shot from slightly below: Aishath and Luyoon sitting on the joali looking up at the glittering starry sky, a single anime tear shining on Aishath's cheek, Luyoon smiling softly with comforting eyes; one shooting star streaking over the palms; the Milky Way glowing",
         camera="medium close-up, low angle, their faces in the middle, the vast starry sky above", amb="island_house_night", sens="other",
         safe="the late father is evoked only through the starry sky; never shown"),
    dict(to=41, reason="emotional turning point: Luyoon shyly asks for her mother's consent and confesses she likes a boy", chars=["luyoon", "aishath"], loc="joali_night",
         visual="Luyoon sitting on the joali with her head lowered, cheeks blushing deep pink in anime style, fingers fidgeting with the end of her black hijab, eyes glancing sideways shyly; Aishath turned towards her, eyebrows raised in gentle surprise with the beginning of a knowing smile; warm lamp light on their faces, stars above",
         camera="medium close-up, eye level, favouring Luyoon", amb="island_house_night", sens="intimacy",
         safe="the romance is only spoken about; the boy (Maaniu) is not shown; mother and daughter only"),
    dict(to=44, reason="action change: Luyoon openly tells her mother who he is; Aishath gently promises to consider it", chars=["aishath", "luyoon"], loc="joali_night",
         visual="Aishath smiling warmly and nodding, her hand resting on Luyoon's hand on the joali rope; Luyoon looking up at her mother now, honest and hopeful, a small relieved smile, eyes sparkling; the veranda lamp glowing behind them and the starry sky above",
         camera="medium shot, eye level, faces in the upper two-thirds", amb="island_house_night"),
    dict(to=45, reason="action change: they rise from the joali and walk back into the house to wake early for Fajr", chars=["aishath", "luyoon"], loc="joali_night",
         visual="mother and daughter seen from behind walking side by side across the moonlit sand yard towards the glowing veranda and open door of the house, the empty joali still gently swaying under the tree, the starry sky above",
         camera="wide shot from behind, the house and sky in the upper two-thirds, the moonlit sand as the lower third", amb="island_house_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The day was one with a clear, beautiful sky. There was not the slightest sign of wind or storm. Those who go out fishing were busy getting ready to go to sea.",
   [("dhoni_engine", "މަހަށް", -24)])
sh(2, "The women who sweep the neighbourhood lanes were carrying on with their work. This is a sight commonly seen on the islands of the Maldives.")
sh(3, "Luyoon is a young girl going on 20. The island speaks of her bravery and courage like no one else's.")
sh(4, "She is a girl loved for a courage quite different from other girls. And Aishath is proud of it.")
sh(5, "Luyoon has two siblings, and Luyoon is the eldest in that house. After her come a younger sister and a younger brother.")
sh(6, "Luyoon's father bade farewell to this passing world when Luyoon was only 12. At that time her younger sister was 5,",
   hum=True)
sh(7, "and her younger brother was 2. But Luyoon's mother raised the three children with boundless love and care.",
   hum=True)
sh(8, "She never let them feel their father's absence. \"Dhonthaa! Get up quickly...\" Zaina, the younger sister, kept shouting, standing by the bedroom door.")
sh(9, "\"There goes Zaina shouting again, right? I'm up,\" she said in a sleepy voice. But Zaina showed no sign of leaving the spot.")
sh(10, "She kept on calling until Luyoon got up, however much it annoyed Luyoon.")
sh(11, "The three children live in a fun, teasing atmosphere, with happiness and togetherness. Knowing that Zaina would not go away,")
sh(12, "she opened the bedroom door: \"What happened? Why are you shouting so much?\" \"Dhonthi is awake, I'll go and say so... Mum is looking for you.",
   [("door_open", "ހުޅުވުމަށް", -20)])
sh(13, "Mum said to get up quickly,\" said Zaina, laughing. \"You make such a fuss just to say that... I'm coming out.\"")
sh(14, "Having said that, Luyoon hurried into the bathroom. After washing up she combed her hair. \"Here comes the queen of this house...",
   [("door_close", "ވަދުނީ", -22)])
sh(15, "and she got up so late, didn't she,\" the two kids began to tease. Saying nothing to that, Luyoon took a cup from the tray and sat down to drink tea.",
   [("cup_clatter", "ތަށި", -20)])
sh(16, "\"You kids are always fighting... All Mum ever hears is 'big sister did this, little sister did that'...")
sh(17, "Learn to listen,\" said Aishath. Since today was Luyoon's day off, after breakfast she busied herself with the housework.")
sh(18, "And teasing her two siblings. It was afternoon. Luyoon, her sister Zaina and her little brother Nawfal went out for an afternoon walk.",
   [("footsteps_sand", "ހިގާލާ", -22)])
sh(19, "Rather than staying at home all the time, all three went together to the sandbank side of the island, because the sandbank side is where many people go.")
sh(20, "It is a place with a big point of land. Along the way many stories were told, with laughter and teasing.")
sh(21, "How noble a bond is the bond between siblings! Just look. Today those three seemed like three children of the same age.")
sh(22, "That is how it looks at a glance. But Luyoon is the eldest in that house. As the three went along joking and having fun,")
sh(23, "they didn't even notice the time passing, so much were they enjoying themselves. Zaina ran into her classmates and went on laughing and joking with them.")
sh(24, "Going to watch the sunset is something those children commonly do. The moment the waves wash over their feet is, you could say, the moment their hearts find peace.",
   [("wave_crash", "ރާޅު", -20)])
sh(25, "The sun had set and darkness was beginning to fall on the land. Zaina, Luyoon and Nawfal walked off towards home, because they always listen to what their mother says.")
sh(26, "The time between Maghrib and Isha is not a good time to be out on the road. So the three walked off at a quick pace.",
   [("footsteps_sand", "ހިގައިގަތ", -22)])
sh(27, "Nawfal went into the mosque to pray. Luyoon and her sister walked on home. As soon as they entered the house, Zaina poured out her complaints about Luyoon.",
   [("door_open", "ވަދެވުމާއެކު", -22)])
sh(28, "\"Mum, she fought with me today,\" she said after washing her face. But Aishath paid no attention to it,",
   [("water_splash_small", "ހަދާލުމަށް", -22)])
sh(29, "because it is something Zaina always does. \"Don't act so big. Go and pray,\" said Luyoon.")
sh(30, "The two went into their room together, jostling each other, to pray. The little family never noticed how the days went by.",
   [("cloth_rustle", "ނަމާދު", -24)])
sh(31, "The days felt short. By the time Luyoon came home after work, the day was over. She was exhausted.",
   [("sigh", "ވަރުބަލިވެފައެވެ", -22)])
sh(32, "However tired she was, Luyoon would not rest before she had prayed. It was the night-time of one night, an atmosphere of perfect silence.")
sh(33, "Luyoon's mother Aishath was lying on the outdoor joali. Luyoon too walked over slowly and sat down beside her mother.",
   [("creak", "ޖައްސާލާފައެވެ", -22)])
sh(34, "\"Mum, you're so deep in thought. What's wrong?\" she said gently. \"Nothing, my dear... I'm just thinking about the future.")
sh(35, "How good it would have been if your father were in this world. But today there is no father,\" said Aishath. \"Mum, if God wills, we will meet Dad too.",
   [("sigh", "އައިޝަތު", -24)], hum=True)
sh(36, "All we have is to pray,\" said Luyoon. In everything, Luyoon keeps helping her mother.", hum=True)
sh(37, "The two younger ones also help as much as they can. Mother and daughter sat in the perfect silence, watching the stars twinkle in the sky.")
sh(38, "\"Mum, I'm thinking about something... I need your consent,\" Luyoon said with her head lowered. \"My dear, what is it now?")
sh(39, "If it's something I can do, I'll see if I can do it,\" said Aishath. But Luyoon felt her mother might worry about this again.")
sh(40, "The one Luyoon always looks after is her mother. \"Mum, I've found a boy I like, but I haven't had the courage to tell him, maybe he...",
   [("breath", "ބުނަން", -24)])
sh(41, "\" That was as far as Luyoon could say. Luyoon became shy. \"My dear... that's a very big matter. But the two of you must behave properly.",
   hum=True)
sh(42, "Whose son is he?\" said Aishath. \"It's Maaniu, from Hawwa-tha's family house. He's someone who was in the same class as me.")
sh(43, "He talks properly... he prays... but I said this because I didn't want to do it without your consent,\" Luyoon told her straight and honestly.")
sh(44, "Without any deception. \"I'll think about it. And I'll talk to them...")
sh(45, "\" After saying that, mother and daughter got up from the joali and walked towards the house, so as to wake early again tonight and pray Fajr.",
   [("creak", "ތެދުވެ", -22), ("footsteps_sand", "ހިގައި", -24)])
SHOTS = S

"""Beat/shot plan for Isq episode 484 (used by plan_beats.py)."""

LOC = {
    "lane_night": "a moonlit white sandy lane on a small Maldivian local island, low coral-stone walls, palms and breadfruit trees, magenta bougainvillea over the walls, a few streetlamps casting warm pools of amber light on the sand, a full moon in a clear starry sky",
    "gate_night": "the front of Maura's family house at night: a two-storey house with pale onion-pink walls, a white gate (dhoraashi) in a coral-stone wall with magenta bougainvillea spilling over it, a sandy front yard with potted plants and a wooden joali seat behind the gate, the sandy street lit by a streetlamp, the modern white guest house with dark-wood balconies directly across the street",
    "sunrise": "the small Maldivian local island at sunrise, seen from slightly above: white sandy lanes between coral-stone walls and pale painted houses, tall coconut palms and breadfruit trees, a small white mosque, the turquoise lagoon and the open sea beyond",
    "eid_lanes": "the island's white sandy lanes on Eid morning, coral-stone walls with magenta bougainvillea, pale painted houses, palms and breadfruit trees, a small corner shop with an open wooden shutter and no signboard, the sand dark and wet in patches from water play",
    "nafeesa_court": "Nafeesa's house two doors down from Maura's: a white gate in a coral-stone wall opening onto an open sandy courtyard with a long wooden table and plastic chairs under a breadfruit tree, the house's open kitchen door at the side",
    "kitchen": "Nafeesa's simple island kitchen: a long work table crowded with bowls and trays, a gas stove with big steaming aluminium pots, a sink, a small fridge, a little door looking out to the gate and the sunny courtyard, plain pale-yellow walls",
    "tree_lane": "the side of a sunny white sandy lane under a big fithuroanu (Alexandrian laurel) tree with a thick trunk and a wide shady canopy of glossy leaves, coral-stone walls, palms, the lane stretching away into the distance",
    "quiet_lane": "a narrow, quiet, empty white sandy lane between high coral-stone walls with bougainvillea and palm fronds overhead, opening at its far end onto a sunlit four-way junction",
    "junction": "a sunny four-way junction of white sandy lanes on the island, coral-stone walls on all four corners, palms and bougainvillea, bright Eid-morning sunshine",
}
MOOD = {
    "lane_night": "late night after Isha, cool silver moonlight with warm amber streetlamp pools, deep blue shadows, quiet, shy and tender, unspoken feelings",
    "gate_night": "late night, silver full-moon light, a warm amber streetlamp glow on the pink wall and the bougainvillea, soft deep-blue shadows, a charmed, reluctant goodbye",
    "sunrise": "early morning of Eid al-Adha, a glorious golden sunrise, long warm rays spreading over the island, soft morning mist, fresh, joyful and new",
    "eid_lanes": "Eid morning, bright warm golden sunshine and crisp shadows, sparkling droplets of water in the air, festive, joyful and lively",
    "nafeesa_court": "Eid morning, bright warm sunshine, dappled shade under the tree, cheerful and busy",
    "kitchen": "late morning, warm sunlight through the little door and window, rising steam from the pots lit gold, busy, homely and cheerful",
    "tree_lane": "Eid late morning, bright sunshine and cool dappled shade under the tree, playful, mischievous excitement",
    "quiet_lane": "Eid late morning, bright sun on the far junction, the lane in calm soft shade, sneaky and playful suspense",
    "junction": "Eid late morning, bright warm sunshine and crisp shadows, a frozen surprised moment",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear arm's-length gap between them, not touching"
J_NIGHT = "Jaleel NOT in a suit: wearing a black long-sleeved shirt with the sleeves rolled to the elbows and dark trousers, no jacket, no tie"
J_NIGHT_X = ("Jaleel dressed casually, NOT in a suit and NOT in a tie: only a plain black long-sleeved button shirt, collar open, "
             "the sleeves rolled up to his elbows showing his forearms and gold watch, and dark trousers; no blazer, no jacket, no tie, no white shirt")
J_EID = "Jaleel NOT in a suit: wearing a plain white long-sleeved shirt and dark trousers, no jacket, no tie, no sunglasses"
J_EID_X = ("Jaleel dressed casually, NOT in a suit and NOT in a tie: only a plain white long-sleeved button shirt with an open collar "
           "and dark trousers; no blazer, no jacket, no black jacket, no tie, no sunglasses")
MA = "Maura in her white long-sleeved lace ankle-length dress and white hijab fully covering her hair and neck with a small white frangipani"
PLAY = ("small plastic juice-pack bags filled with brightly coloured water and buckets of water, splashes of coloured water, "
        "no powder clouds")

BEATS = [
    # ---------------- NIGHT WALK HOME (eve of Eid al-Adha)
    dict(to=4, reason="episode opening: she accepts his invitation and they walk home together in silence under the moon",
         chars=["jaleel", "maura"], loc="lane_night",
         visual=f"{J_NIGHT} and {MA} walking slowly side by side along the moonlit sandy lane towards the camera, {GAP}, "
                f"his hands in his pockets, eyes ahead, a stern but softened face; she glances down with a small shy smile she "
                f"is trying to hide; the full moon above the palms",
         camera=f"medium wide shot, eye level, {LOW} (moonlit sand of the lane)", amb="island_night",
         sens="intimacy", safe="a quiet walk side by side with a clear arm's-length gap; no touching, no couple pose"),
    dict(to=5, reason="scene change: they stop at her gate; she looks at him, the moment of parting",
         chars=["maura", "jaleel"], loc="gate_night",
         visual=f"{MA} standing in front of the white gate of her pale-pink house under the bougainvillea, turned towards "
                f"{J_NIGHT} who stands in the sandy street facing her, {GAP} and more, both quiet, she looks up at him shyly, "
                f"he looks back at her; seen from the side",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (sandy street in moonlight)", amb="island_night",
         sens="intimacy", safe="two people at a respectful distance at her gate; no touching"),
    dict(to=12, reason="framing change: Jaleel's meaningful look and his long inner questioning (why does his hard heart break its principles?)",
         chars=["jaleel"], loc="gate_night",
         visual=f"close-up of {J_NIGHT_X}, standing in the moonlit street looking off-frame towards someone with a deep, "
                f"meaningful, troubled gaze, jaw set, brows slightly drawn, the first trace of tenderness in his hard eyes; "
                f"the blurred bougainvillea and the pink wall glowing amber behind him; his black open-collar shirt with no jacket and no tie",
         camera=f"close-up, eye level, {LOW} (dark soft-focus background)", amb="island_night"),
    dict(to=13, reason="back to the two-shot at the gate: 'Good night'", reuse="beat_002", chars=["maura", "jaleel"],
         loc="gate_night", visual="reuse of beat_002", amb="island_night"),
    dict(to=16, reason="focus change: Maura's shy smile and her heart leaning towards him",
         chars=["maura"], loc="gate_night",
         visual=f"medium close-up of {MA} standing at her white gate under the magenta bougainvillea, looking up at someone "
                f"off-frame with a soft shy smile and warm shining eyes, one hand resting lightly on the gate",
         camera=f"medium close-up, eye level, {LOW} (the white gate bars and soft shadow)", amb="island_night"),
    dict(to=17, reason="action change: she walks in through the gate, then stops and turns back at his voice",
         chars=["maura"], loc="gate_night",
         visual=f"{MA} in the open white gateway, her back half to the camera as if she was walking into the sandy front yard, "
                f"stopped mid-step and looking back over her shoulder with surprise, the moonlit yard and the pink house behind her",
         camera=f"medium shot, eye level, {LOW} (moonlit sand of the front yard)", amb="island_night"),
    dict(to=18, reason="character change: Jaleel in the street calls her name and says 'Eid Mubarak'",
         chars=["jaleel"], loc="gate_night",
         visual=f"{J_NIGHT_X}, standing alone in the moonlit sandy street under a streetlamp, hands in his pockets, sleeves rolled up, speaking "
                f"quietly towards the gate, no smile but a warm closeness in his eyes; the white guest house across the street behind him; he wears the black open-collar shirt only, no jacket, no tie",
         camera=f"medium shot, eye level, {LOW} (the lamp-lit sand of the street)", amb="island_night", hum=True),
    dict(to=20, reason="back to Maura's shy smile: the first Eid wish she received", reuse="beat_005", chars=["maura"],
         loc="gate_night", visual="reuse of beat_005", amb="island_night"),
    # ---------------- EID MORNING
    dict(to=23, reason="time jump: Eid al-Adha morning, golden sunrise over the island", loc="sunrise",
         visual="a glorious golden sunrise over the small island: the sun rising out of the sea, warm rays spreading over "
                "the palms, the white mosque and the sandy lanes, a few birds in the sky; no people",
         camera="wide establishing shot from slightly above, the sky and the island in the upper two-thirds, a calm sandy lane in soft shadow as the lower third",
         amb="dawn_exterior", transition="black"),
    dict(to=25, reason="scene change: the busy Eid streets, young people's water-and-colour play, women shopping",
         loc="eid_lanes",
         visual=f"a lively Eid morning in the sandy lanes: at one corner a group of laughing teenage girls in long modest "
                f"dresses and hijabs fully covering their hair splashing one another with {PLAY}; farther down the lane a "
                f"separate group of boys in T-shirts and long trousers doing the same; a few small children running with "
                f"little water bags; island women in long dresses and headscarves walking past with full shopping bags; "
                f"everyone happy, no one hurt",
         camera=f"wide shot down the lane, eye level, the people in the upper two-thirds, {LOW} (wet sand)", amb="eid_street",
         sens="other", safe="Maldivian Eid water-and-colour game only: girls with girls, boys with boys; no Holi powder, no temples or other-faith symbols, no animal sacrifice"),
    dict(to=30, reason="character/scene change: Maura and Zulfa go to Nafeesa's house and enter through the gate",
         chars=["zulfa", "maura"], loc="nafeesa_court",
         visual=f"Zulfa stepping in through the white gate into Nafeesa's sunny sandy courtyard, calling out cheerfully with "
                f"one hand raised; {MA} following just behind her with a light smile; the long wooden table under the "
                f"breadfruit tree and the open kitchen door at the side",
         camera=f"medium wide shot, eye level, {LOW} (sunny sand of the courtyard)", amb="eid_street"),
    dict(to=33, reason="scene change: the busy kitchen, three or four women cooking the delegation's Eid lunch",
         chars=["nafeesa", "zulfa", "maura"], loc="kitchen",
         visual=f"Nafeesa's busy kitchen full of steam and golden light: three helper women at the stove and table, each "
                f"different from the main characters — one in a mustard-yellow dress with a black headscarf stirring a big pot, "
                f"one in a dark-green dress with a grey headscarf frying, one young woman in a peach dress with a beige hijab "
                f"chopping onions; Nafeesa (lavender dress, white headscarf) at the work table turning to greet the newcomers "
                f"with a wide smile; Zulfa (the only woman in a blue floral dress and maroon headscarf) just stepping in through "
                f"the doorway at the back, sniffing the delicious smell with delight; {MA} just behind her in the doorway; "
                f"every person appears only once",
         camera=f"medium wide shot, eye level, {LOW} (the work table top with bowls)", amb="kitchen_busy"),
    dict(to=36, reason="action change: Nafeesa kneads the fish paste for fish balls and lists the dishes",
         chars=["nafeesa"], loc="kitchen",
         visual="Nafeesa sitting at the kitchen table kneading a bowl of fish paste and rolling small round fish balls "
                "with her hands, talking excitedly with a wide smile; around her on the table trays of fried fish balls, "
                "pots of chicken curry and fish curry, a stack of flat roshi breads and a tray of golden bondibai rice pudding",
         camera=f"medium shot, eye level, {LOW} (the table top with the dishes)", amb="kitchen_busy"),
    dict(to=39, reason="focus change: Maura smiles at her mother's cooking enthusiasm",
         chars=["maura", "zulfa"], loc="kitchen",
         visual=f"Zulfa at the stove eagerly stirring a big steaming pot with a ladle, rolling up her sleeves with a "
                f"determined, excited grin; {MA} standing beside the work table watching her mother and covering a little "
                f"amused laugh with her fingers",
         camera=f"medium shot, eye level, {LOW} (the work table top)", amb="kitchen_busy"),
    dict(to=42, reason="character enters: Lamha bursts in splashed with colour, out of breath, and pulls Maura to play",
         chars=["lamha", "maura"], loc="kitchen",
         visual="Lamha at the kitchen door, her mint-green dress and coral-pink hijab splashed all over with bright pink, "
                "green and yellow coloured water, bent forward with her hands on her knees, panting and laughing; Maura "
                "beside her in her white dress and white hijab looking at her wide-eyed with delight; Lamha's hijab still "
                "fully covers her hair",
         camera=f"medium shot, eye level, {LOW} (the floor near the door in soft light)", amb="kitchen_busy",
         sens="other", safe="colour play shown only as bright coloured-water stains on her clothes"),
    dict(to=47, reason="action change: Maura silently asks her mother's permission; Nafeesa pleads for her; Zulfa smiles",
         chars=["maura", "zulfa", "nafeesa", "lamha"], loc="kitchen",
         visual="Maura looking hopefully and impatiently at her mother Zulfa, hands clasped; Zulfa at the stove with a ladle, "
                "turning towards her with a fond smile; Nafeesa seated at the table with her hands in the fish-paste bowl, "
                "leaning in and speaking up for Maura; colour-splashed Lamha at the door grinning; warm and funny",
         camera=f"medium wide shot, eye level, {LOW} (the table top)", amb="kitchen_busy"),
    dict(to=50, reason="scene change: Maura and Lamha run out into the lanes full of colour play",
         chars=["maura", "lamha"], loc="eid_lanes",
         visual=f"Maura (white dress, white hijab) and colour-splashed Lamha (mint-green dress, coral-pink hijab) running "
                f"out into the sunny sandy lane hand in hand, laughing; in the background groups of girls splashing each "
                f"other with {PLAY}, a separate group of boys farther away, a few small children; bright droplets glitter in the sun",
         camera=f"medium wide shot, eye level, {LOW} (wet sand)", amb="eid_street",
         sens="other", safe="Maldivian Eid water-and-colour game only; girls with girls, boys with boys; no Holi or other-faith imagery"),
    dict(to=55, reason="scene change: under the fithuroanu tree, the hidden bag of colour-filled juice-pack bags; Ibbe's boys in the distance",
         chars=["lamha", "maura"], loc="tree_lane",
         visual="Lamha crouching at the trunk of the big fithuroanu tree pulling small colour-filled juice-pack bags out of "
                "a cloth bag hidden there, laughing mischievously; Maura standing beside her holding one small bag of bright "
                "pink coloured water in both hands, looking at Lamha with excitement; far away down the sunny lane three "
                "boys walking towards them",
         camera=f"medium shot, eye level, {LOW} (sand and the cloth bag at the tree's roots)", amb="eid_street"),
    dict(to=58, reason="scene change: Maura ducks into a quiet lane and sneaks up on a young man standing with his back to her",
         chars=["maura"], loc="quiet_lane",
         visual="Maura seen from behind and slightly to the side, tiptoeing down the empty shaded lane with a playful "
                "grin, holding the small colour bag ready in one hand, glancing back over her shoulder; far ahead at the "
                "sunlit junction a young man in a T-shirt stands with his back to her",
         camera=f"medium wide shot, eye level, {LOW} (shaded sand of the lane)", amb="village_day"),
    dict(to=60, reason="character change: Jaleel walking along the road on his phone, ending a stern business call",
         chars=["jaleel"], loc="junction",
         visual=f"{J_EID_X}, walking briskly along the sunny sandy lane towards the junction holding a phone to his ear with "
                f"a stern, commanding face; the phone's screen is not visible; his white shirt has no jacket over it and no tie",
         camera=f"medium shot, eye level, {LOW} (sunny sand)", amb="village_day"),
    dict(to=62, reason="action change: at the junction the colour bag bursts on him (shown the moment after)",
         chars=["jaleel"], loc="junction",
         visual=f"{J_EID}, standing frozen in the middle of the four-way junction the moment after a small colour bag burst "
                f"on him: big bright pink and green splashes of coloured water spreading across the front of his white "
                f"shirt, which stays fully opaque, a few colour drops on his cheek, the burst empty plastic bag on the sand "
                f"at his feet; he looks down at his shirt in shock, phone back in his pocket",
         camera=f"medium shot, eye level, {LOW} (sunny sand with the burst bag)", amb="village_day",
         sens="other", safe="the bag is never shown mid-impact: only the colourful splash on his opaque shirt the moment after; no injury"),
    dict(to=64, reason="framing change: his white shirt completely covered in colour",
         chars=["jaleel"], loc="junction",
         visual=f"medium close-up of {J_EID}: his white shirt drenched with bright pink and green coloured water but fully "
                f"opaque, a few small pink and green drops on his cheek and beard, holding his arms slightly away from his "
                f"body and staring down at the ruined shirt in disbelief",
         camera=f"medium close-up, eye level, {LOW} (sunny sand behind)", amb="village_day",
         sens="other", safe="colour splash only on the opaque shirt and a few drops on his cheek, nothing like an injury"),
    dict(to=66, reason="character change: Maura frozen and pale at a distance on realising the victim is Jaleel",
         chars=["maura"], loc="quiet_lane",
         visual="Maura frozen at the mouth of the shaded lane a clear distance away, both hands pressed to her mouth, "
                "eyes wide with horror, her face gone pale; her hands empty; behind her the empty lane",
         camera=f"medium shot, eye level, {LOW} (shaded sand of the lane)", amb="village_day", hum=True),
    dict(to=67, reason="emotional turning point: he turns furious toward the thrower and his anger melts at the sight of her (cliffhanger)",
         chars=["jaleel"], loc="junction",
         visual=f"close-up of {J_EID}, his white shirt splashed with bright pink and green colour, a few colour drops on "
                f"his cheek; he has turned towards someone off-frame, his frown of anger dissolving into soft stunned "
                f"wonder, his eyes gentle as if he has seen a fairy; he is alone in the frame, nobody else near him, the empty sunny lane behind him",
         camera=f"close-up, eye level, {LOW} (sunlit soft-focus background)", amb="village_day", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Won't you come...? Do come... the house is close too...\" What girl would dare say no to Jaleel's invitation?")
sh(2, "Though her heart felt it might fly away with joy, trying not to let it show on her face, Maura came over to Jaleel with a light smile.",
   [("footsteps_sand", "އައެވެ", -22)])
sh(3, "In the few moments it took to walk home, though they spoke no more words between them,",
   [("footsteps_sand", "ހިނގާލާފައި", -22)])
sh(4, "unknown feelings were being born between them. Even for that short while, both hearts were happy in each other's nearness.")
sh(5, "Stopping near the gate of the house, Maura looked at Jaleel. From that look, Jaleel knew the time to part on that charming night had come.")
sh(6, "Jaleel looked at Maura with a meaningful gaze. What kind of magic was this short, fair girl working on Jaleel?")
sh(7, "Why was his heart growing uneasy because of these entirely new feelings that had started without his knowing?")
sh(8, "Why should Jaleel's heart, which had spent its whole life as a slave among wealth and money, now call out for something entirely different?")
sh(9, "Why should Jaleel's hard heart suddenly long to form a bond with that girl?")
sh(10, "Why was Jaleel's heart calling him to begin a relationship that did not even fit his personality and his principles?")
sh(11, "Why was Jaleel, who had held fast to his principles in everything, for the first time finding it hard to hold to them?",
   hum=True)
sh(12, "And why did his heart call on him to break those principles? Why did it seem that the strength and certainty he had over his heart were slipping away?")
sh(13, "Was he about to give his own heart away? \"Good night...\" Jaleel was the first to say farewell for the night. \"Good night...\"")
sh(14, "With a light smile Maura too wished him good night. In those few moments, seeing Jaleel's steadiness and the respect for women in his heart, Maura's young heart leaned even more towards Jaleel.")
sh(15, "Though at first sight he seemed an angry, hard man, Maura became certain that inside that hard shell was a heart as soft as a flower.")
sh(16, "Perhaps that is why Maura's heart was filling with entirely new feelings she could not explain.")
sh(17, "As Maura started walking to go inside, what made her stop and turn back was Jaleel's voice reaching her ears once more.",
   [("footsteps_sand", "ހިނގައިގަތް", -22)])
sh(18, "\"Maura...\" Jaleel called. \"Eid Mubarak...\" Jaleel said when Maura turned round.")
sh(19, "Though there was no smile on Jaleel's face, there was truly a closeness in his voice. A shy smile spread over Maura's lips because the first person to wish her a happy Eid was Jaleel.",
   hum=True)
sh(20, "In the time she spent with Jaleel she had forgotten, even for a little while, that tomorrow was Eid. \"Eid Mubarak...\"")
sh(21, "Maura too wished Jaleel a happy Eid. The sun rose on an entirely new day. The coolness of dawn was easing with the warmth of the sun's rays.",
   [("leaves_rustle", "ދޯދިތަކުން", -24)])
sh(22, "Spreading a beautiful golden glow over the whole world, the sight was an example of natural beauty one could never tire of.")
sh(23, "The whole day was filled with all kinds of joyful feelings. The whole place rang with the sounds of laughter and fun.")
sh(24, "Because it was the joyful day of Eid al-Adha, the streets looked busier than on ordinary days.")
sh(25, "At every corner young people, boys and girls, were playing the Eid water game, and women going from shop to shop buying things to cook for lunch",
   [("splash", "ފެންކުޅި", -20)])
sh(26, "could be seen out and about. Maura too, after quickly finishing the morning tea, set off with Zulfa to Nafeesa's house to cook lunch.",
   [("footsteps_sand", "މިސްރާބުޖެހީ", -24)])
sh(27, "Since Nafeesa's family had been entrusted with preparing the lunch feast for the delegation from Malé, they went to join them")
sh(28, "and help them. With no friends yet and no one to invite her to play the water game, Maura too wanted to go along with Zulfa.")
sh(29, "\"Nafeesa...\" Zulfa called as she came in through the gate. Behind Zulfa, Maura too came in through the gate. \"Oi...",
   [("door_open", "ވަދެގެން", -22)])
sh(30, "We're in the kitchen... come, come...\" came Nafeesa's voice from the kitchen. At that, Zulfa walked towards the kitchen.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(31, "As they entered the kitchen, the delicious smell of the cooking made them feel full already. Three or four women were already busy cooking with Nafeesa in the kitchen.",
   [("cup_clatter", "ކެއްކުމުގައި", -22)])
sh(32, "\"Oh my... what a lovely smell... Did you start already, before I came?\" Zulfa said as she came in. \"Yes... Vadheefa is here today too...")
sh(33, "and the two girls Vadheefa brought are here too... With so much to cook we have to hurry, don't we... so we started early...\"")
sh(34, "Nafeesa said as she kneaded the fish paste to fry fish balls. \"Yes, that's how it should be... What are you making...?\" Zulfa asked.")
sh(35, "\"Chicken curry, fish curry, fish balls, rice, roshi, bondibai, and lots more besides...\"")
sh(36, "Nafeesa said eagerly. \"Oh my... today we must put on a great show... we must show them we're people who know how to cook...\"")
sh(37, "Zulfa joined in with great enthusiasm. Maura felt a little like laughing at the way her mother was carrying on.")
sh(38, "For when it came to cooking, her mother was always full of great excitement. And her mother was famous on the island for cooking delicious food.")
sh(39, "Maura knew from Reema that her mother had never yet met anyone who would say her cooking was bad.")
sh(40, "It was just then that Maura saw Lamha come running towards the kitchen. She was covered in colour from head to toe and gasping for breath from exhaustion.",
   [("footsteps_sand", "ދުވަމުން", -20), ("breath_heavy", "މާނޭވާ", -20)])
sh(41, "Lamha came and stopped beside Maura, bent forward and took two or three deep breaths to steady her breathing. \"Come and play colours...")
sh(42, "It'll be so much fun... Ibbe and the others are there too...\" Lamha said, straightening up and tugging at Maura's hand.")
sh(43, "Though she badly wanted to go, she did not dare go without Zulfa's permission, so Maura looked at Zulfa's face for her word.")
sh(44, "The first to notice this was Nafeesa, sitting kneading the fish paste. \"Oh, Zulfa... you should let the girl go...")
sh(45, "She's lived in Malé so long and come back to the island, she doesn't even have a friend yet... send her with Lamha... I'm sure Maura wants to go...\"")
sh(46, "Nafeesa said before Zulfa could say a word. Maura looked at Zulfa impatiently. \"Oh, I wasn't going to say no...")
sh(47, "If my girl wants to, go...\" Zulfa said with a smile. \"But be careful, all right... Lamha, look after Maura, all right...\"")
sh(48, "Zulfa said in a tone of advice. Laughing, Maura ran off with Lamha.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(49, "As soon as they came out onto the road, Maura saw young people, boys and girls, running about throwing colour at every corner.",
   [("splash", "ކުލަޖަހަމުން", -22)])
sh(50, "Here and there among them small children were busy too. \"Come on, Maoo...\" Lamha called to Maura as she started to run.")
sh(51, "Smiling with joy and having fun, Maura too ran after Lamha. After running some way, Lamha stopped under a fithuroanu tree at the side of the road.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -22)])
sh(52, "Holding the colour-filled juice-pack bag that Lamha had taken from a bag left at the foot of the fithuroanu tree, Maura looked at Lamha.",
   [("cloth_rustle", "ނެގި", -24)])
sh(53, "\"Try to hit someone who hasn't got any colour on them yet, all right... Mareem and her friends still haven't got a speck of colour on them... Hey, run, run...")
sh(54, "Ibbe and the boys are coming this way...\" Lamha called, giving Maura instructions on what to do, laughing and running off.",
   [("footsteps_sand", "ދުއްވައިގަންނަމުން", -22)])
sh(55, "Just then Maura saw a group of three boys coming from a little way off. So as not to be caught by them, Maura too slipped into the first lane she came to.",
   [("footsteps_sand", "އެޅިއެވެ", -22)])
sh(56, "It was a fairly quiet lane, so there was no one on it. After running a little way, Maura saw a young man standing some distance away with his back turned.")
sh(57, "Stopping, Maura looked back to see whether Ibbe and the boys were coming after her. Seeing no one, Maura crept towards the young man with slow steps.",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -24)])
sh(58, "Stopping a little way off, Maura got a good grip on the colour-water bag in her hand and carefully sent it flying towards him.")
sh(59, "\"Within a short while my assistant will send you all the details... Then look it over at your end, make a decision and let me know....")
sh(60, "If you don't give me an answer within the given time, I'll decide for myself...\" Jaleel, who was walking along the road, ended the call and shoved the phone into his pocket.",
   [("cloth_rustle", "ކޮށްޕައިލިއެވެ", -24)])
sh(61, "Walking quickly, just as he reached the middle of a four-way junction, something came from who knows where and struck Jaleel's body.",
   [("splat", "ޖެހުނެވެ", -14)])
sh(62, "At that moment he felt the wetness of it on his body right through the white shirt he was wearing, and drops splashed onto his face too.",
   [("gasp", "ބުރައިގެން", -22)])
sh(63, "Whether it was Maura's bad luck or good luck, no one knows. The colour-water bag struck Jaleel as he came out of the lane.")
sh(64, "As the colour bag hit, it burst, and in an instant the white shirt Jaleel was wearing was covered with colour.",
   [("splash", "ފަޅައިގެން", -22)])
sh(65, "The whole shirt was ruined, and some of the colour marked Jaleel's face too. Maura's face went pale when she realised the colour bag's victim was Jaleel.",
   [("gasp", "ހުދުވެގެން", -20)])
sh(66, "The young man standing a little way down the road turned at the sound and quickly ran off to hide in safety.",
   [("footsteps_sand", "ދުވެފައި", -22)])
sh(67, "Seeing the colour bag that had hit him, Jaleel turned in anger towards where it had come from. But in an instant the displeasure on his face vanished at the sight of the beautiful fairy before him. To be continued.",
   [("heartbeat", "ފެނުމުންނެވެ", -22)], hum=True)
SHOTS = S

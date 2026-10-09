"""Beat/shot plan for Marufas episode 570 (used by plan_beats.py)."""

ABANDONED = ("a long-abandoned coral-stone house in a lonely overgrown corner of the island: broken wooden shutters, "
             "peeling walls, dust, cobwebs, a dark back room with a single old wooden chair; reached through scrub")
HOSPITAL = ("the island hospital: a long corridor with pale walls, plastic chairs along the wall, cold fluorescent "
            "ceiling lights, a polished floor")
WARD = ("the island hospital: Yamna's hospital room, a single hospital bed with white sheets and a white pillow, "
        "monitors showing abstract green lines with NO numbers, a plastic chair beside the bed, a window with blinds, "
        "pale walls")
LANE = ("white sandy lanes between coral-stone walls, palms and breadfruit trees, a few dim street lamps, small "
        "single-storey houses with corrugated roofs")
TEASHOP = ("a small island teashop (hotaa) on a white sandy lane: a few plastic tables and chairs under a corrugated "
           "awning, glasses of tea, a glass counter with short-eats, palms and coral-stone walls around")
SHOP = ("a small island shop (fihaara) on a white sandy lane: a plain shop front with open wooden shutters and shelves "
        "of goods inside (no signs, no labels), a long wooden bench outside under a breadfruit tree")
GUEST = ("the guest bedroom in the family's large modern island house: white walls, polished white marble floor, a "
         "single bed with plain white sheets, a tall dark-wood wardrobe, a glass window with a sheer curtain")
MOSQUE = ("a small white island mosque: its shaded front veranda with white pillars, a long wooden bench along the wall, "
          "a sandy yard with palms")

LOC = {
    "gossip": TEASHOP,
    "ward": WARD,
    "forensic": ABANDONED + "; inside the dark back room",
    "jetty_dawn": ("the island harbour at dawn: a long concrete jetty, a small white launch with a cabin moored "
                   "alongside, a calm grey-blue lagoon, palms along the shore"),
    "police_station": ("the small island police station: a plain office with pale walls, a desk with plain folders and "
                       "a closed laptop, a ceiling fan, a window with blinds, a wooden bench along the wall"),
    "corridor": HOSPITAL,
    "guest_room": GUEST,
    "jetty_night": ("the island harbour late at night: a long concrete jetty lit by a single dim yellow lamp, a small "
                    "launch moored at the end, black still water, mist"),
    "shop": SHOP,
    "lane_day": LANE,
    "memory": ("the island in years past: a sandy yard beside an old coral-stone house near the lagoon, a fishing "
               "dhoni pulled up on the white beach behind, palms"),
    "teashop_noon": TEASHOP,
    "guest_room_noon": GUEST,
    "mosque": MOSQUE,
    "ward_afternoon": WARD,
    "veranda": ("the island hospital's open-air side veranda: a long empty walkway with white pillars and a low wall, "
                "overlooking palms and a sandy yard, nobody else around"),
}
MOOD = {
    "gossip": "morning, flat overcast grey light, muted colours, a heavy uneasy mood, hushed whispers",
    "ward": "daytime, soft muted daylight through the blinds, pale blue-grey tones, silent and sorrowful",
    "forensic": "daytime outside but near-darkness inside: thin dusty blades of daylight through the broken shutters and white flashlight beams, cold grey-blue shadows, grim and clinical",
    "jetty_dawn": "dawn, a pale cold grey sky with a faint pink edge, mist over the lagoon, still and mournful",
    "police_station": "daytime, cool flat light through the blinds, grey-blue tones, serious and tense",
    "corridor": "midday, cold white fluorescent light, pale green-grey tones, sterile and tense",
    "guest_room": "late afternoon, dim grey light through the sheer curtain, long cold shadows, creeping fear",
    "jetty_night": "late at night, one dim yellow lamp, deep charcoal and blue-black shadows, mist drifting over black water, secretive",
    "shop": "midday, harsh white sunlight, short dark shadows, dusty heat, an uneasy stillness",
    "lane_day": "midday, harsh white sunlight bleached to cold grey, deep shadow along the coral wall, dizzying dread",
    "memory": "a remembered past, soft warm golden late-afternoon haze, gentle dreamlike glow, faded colours, peaceful",
    "teashop_noon": "noon, bright hot daylight under the shade of the awning, warm dusty tones, uneasy",
    "guest_room_noon": "noon, flat cold daylight through the sheer curtain, empty and hollow, unsettling",
    "mosque": "afternoon, soft warm light in the shaded veranda, cool white pillars, calm but grave",
    "ward_afternoon": "late afternoon, warm soft light through the blinds mixing with cool fluorescent light, heavy sorrow",
    "veranda": "late afternoon, low golden-grey light, long pillar shadows across the floor, the palms still, crushing silence",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
GOWN = ("wearing a modest long-sleeved pale-blue hospital gown instead of her lilac dress, her white hijab fully covering "
        "her hair and neck, a white blanket up to her chest")
HAG = "pale, tired, with dark circles under her eyes and hollow cheeks, no marks on her face"
POLICE = ("Maldivian police officers in plain dark-navy uniforms and plain caps (no patches, no emblems, no badges, a plain "
          "belt with no holster and no pouches, nothing on the belt)")

BEATS = [
    # ---------------- THE ISLAND TALKS
    dict(to=5, reason="scene change: the whole island whispers about Aadhanbe's death and Yamna", loc="gossip",
         visual="a small island teashop in the morning: four Maldivian men in shirts and sarongs sitting close together at a plastic table with glasses of tea, leaning in and talking in hushed tones with worried, suspicious faces; in the background on the sandy lane two women in long dresses and hijabs fully covering their hair whisper to each other beside a coral-stone wall",
         camera=f"medium wide shot, eye level, {LOW} (sandy ground and table legs in soft shadow)", amb="village_day"),
    dict(to=7, reason="scene change: in the hospital room Yamna lies silent, staring at the ceiling", chars=["yamna"], loc="ward",
         visual=f"Yamna lying in the hospital bed, propped on a white pillow, {GOWN}, {HAG}; she stares silently up at the ceiling, her lips closed, a single tear running from the corner of her eye down her cheek",
         camera=f"medium close-up from slightly above, {LOW} (the white blanket in soft shadow)", amb="hospital_room", hum=True,
         sens="other", safe="her muteness and inner torment shown only as a silent stare and a single tear"),
    # ---------------- POLICE INVESTIGATION
    dict(to=10, reason="scene change: the police forensic team examines the abandoned house", loc="forensic",
         visual=f"inside the dark back room of the abandoned house: two {POLICE}, wearing white gloves, crouch beside an EMPTY old wooden chair, one brushing it carefully with a small brush, the other shining a flashlight on the dusty floor; a small plain clear evidence bag in a gloved hand, nothing inside it visible; thin shafts of daylight through the broken shutters; no other people",
         camera=f"medium wide shot, eye level, {LOW} (dusty floor in shadow)", amb="abandoned_house", transition="black",
         sens="violence", safe="the knife and the scene of death are never shown; only officers examining an empty chair (bible rules 3, 11)"),
    dict(to=12, reason="symbolic scene change: the body is sent to Malé for the post-mortem", loc="jetty_dawn",
         visual="a small white launch slowly pulling away from the island's long concrete jetty at dawn, leaving a soft wake on the calm grey lagoon; two small silhouettes of men in dark-navy uniforms standing on its deck seen from far away; mist over the water, palms on the shore; no coffin and no stretcher visible",
         camera="wide shot, eye level, the launch and jetty in the upper two-thirds, the calm grey water as the lower third",
         amb="jetty_day", hum=True, sens="violence",
         safe="the body and the post-mortem findings (blood loss, injuries) are never shown; only a launch leaving at dawn (spec 6.1)"),
    dict(to=15, reason="scene change: police take witness statements and gather records at the station", loc="police_station",
         visual=f"in the small island police station a grim senior officer sits at a desk with plain closed folders, listening to an elderly Maldivian islander in a shirt and sarong who sits across from him, pointing vaguely towards the window as he gives his statement; a second officer stands by the window with arms folded; {POLICE}; no text on anything, no screens visible",
         camera=f"medium wide shot, eye level, {LOW} (the desk front and floor in shadow)", amb="room_day"),
    dict(to=17, reason="scene change and new characters: police come to the hospital and question Faarish and Adheel", chars=["faarish", "adheel"], loc="corridor",
         visual=f"in the hospital corridor three {POLICE} stand facing Faarish and Adheel; the senior officer in front asks a question with a stern, searching look; Faarish and Adheel stand side by side by the plastic chairs, stiff and uneasy",
         camera=f"medium wide shot, eye level, from the side, {LOW} (polished corridor floor)", amb="hospital_corridor"),
    dict(to=18, reason="focus change: Faarish forces a calm face while his heart pounds", chars=["faarish"], loc="corridor",
         visual="close-up of Faarish in the cold fluorescent light of the corridor, trying to keep a calm, steady face while answering, but a drop of sweat on his temple, his eyes flicking aside, his jaw tight with fear",
         camera=f"close-up, eye level, {LOW}", amb="hospital_corridor", hum=True),
    dict(to=20, reason="focus change: Adheel's face betrays his anxiety", chars=["adheel"], loc="corridor",
         visual="close-up of Adheel standing in the hospital corridor, his face pale and anxious, swallowing hard, his eyes darting towards the officers off-frame, one hand nervously rubbing the back of his neck",
         camera=f"close-up, eye level, slightly from the side, {LOW}", amb="hospital_corridor"),
    dict(to=22, reason="the officers finish, warn them not to leave the island and go (return to the questioning image)", reuse="beat_006",
         chars=["faarish", "adheel"], loc="corridor", visual="reuse of beat_006", amb="hospital_corridor"),
    # ---------------- GHASSAN FLEES
    dict(to=24, reason="scene and character change: Ghassan hears of the death and is gripped by fear", chars=["ghassan"], loc="guest_room",
         visual="Ghassan standing alone by the window of the guest bedroom, a phone with a dark blank screen lowered in his hand, his face frozen with fear and calculation, eyes narrowed, a cold sweat on his forehead; his big black leather bag on the bed behind him",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)", amb="room_day", hum=True),
    dict(to=26, reason="action and time change: Ghassan secretly flees the island at night", chars=["ghassan"], loc="jetty_night",
         visual="Ghassan hurrying alone down the long dark jetty late at night towards a small moored launch, his big black leather bag on his shoulder and a suitcase in his hand, glancing back over his shoulder with a furtive, frightened look, lit by a single dim yellow lamp, mist over black water",
         camera="wide shot, eye level, the figure and the launch in the upper two-thirds, the dark jetty planks and water as the calm lower third",
         amb="sea_boat", transition="black"),
    # ---------------- JALEEL'S WORDS
    dict(to=29, reason="scene change: Faarish stops by a shop and overhears Jaleel talking loudly", chars=["faarish"], loc="shop",
         visual="Faarish standing a little apart beside the breadfruit tree outside a small island shop, uneasy and pale, half turned towards a group of island men gathered on the bench; among them Jaleel, a weathered Maldivian fisherman in his fifties with a short grey stubble, a faded blue t-shirt and a checked sarong, talks loudly with open hands to the others",
         camera=f"medium wide shot, eye level, Faarish in the foreground on one side, {LOW} (white sand in shadow)", amb="village_day"),
    dict(to=31, reason="emotional turning point: Jaleel's words strike Faarish like a thunderbolt", chars=["faarish"], loc="lane_day",
         visual="close-up of Faarish's face as the truth hits him: eyes wide with shock, lips parted, the colour draining from his face, the white lane and coral wall tilting and blurring behind him as if the world is spinning",
         camera="close-up, slightly dutch angle, the face in the upper two-thirds, the blurred bright sand as the calm lower third",
         amb="village_day", hum=True),
    dict(to=35, reason="memory: Aadhanbe as the island knew him for years, a gentle old man", chars=["aadhanbe"], loc="memory",
         visual="a warm remembered scene: Aadhanbe, kindly and smiling, sitting on a low wooden bench in a sandy yard beside his old coral-stone house, a few small island children standing around him listening (boys in t-shirts and long shorts, a little girl in a long dress and a white hijab); a fishing dhoni pulled up on the beach behind them, palms",
         camera=f"medium wide shot, eye level, {LOW} (white sand in soft shadow)", amb="memory", transition="dissolve",
         sens="other", safe="the old practices (water, amulets) are not depicted as ritual; only a gentle memory of the old man with children"),
    dict(to=37, reason="back to Faarish: his mind goes blank, he trembles (return to his shocked face)", reuse="beat_013",
         chars=["faarish"], loc="lane_day", visual="reuse of beat_013", amb="village_day", transition="dissolve"),
    dict(to=40, reason="symbolic detail: his clean hands feel stained with an innocent man's blood", chars=["faarish"], loc="lane_day",
         visual="Faarish leaning his back against a sunlit coral-stone wall in the empty lane, staring down in horror at his own two open hands held in front of him, palms up, perfectly clean; his face above them stricken with guilt and nausea, trembling, frozen on the spot",
         camera=f"medium close-up, slightly high angle, the face and hands in the upper two-thirds, {LOW} (sand in shadow)",
         amb="village_day", hum=True, sens="violence",
         safe="'hands stained with blood' shown as clean hands he stares at in horror; his vomiting is not shown (spec 6.1)"),
    # ---------------- KHALID FINDS GHASSAN GONE
    dict(to=42, reason="scene and character change: at noon Khalid buys food and phones Ghassan", chars=["khalid"], loc="teashop_noon",
         visual="Khalid standing at the glass counter of the island teashop at noon holding a plastic bag of food parcels, his phone pressed to his ear, waiting for an answer, his brow creased with tiredness and growing worry",
         camera=f"medium shot, eye level, {LOW} (counter front in shadow)", amb="village_day"),
    dict(to=48, reason="scene change: Khalid opens Ghassan's room and finds it empty", chars=["khalid"], loc="guest_room_noon",
         visual="Khalid standing in the open doorway of the guest bedroom, one hand still on the door handle, staring in shock: the room is completely empty, the single bed stripped bare, the tall wardrobe standing open and empty, nothing left anywhere, no bag, no belongings",
         camera=f"medium wide shot from inside the room towards the door, eye level, {LOW} (bare marble floor)", amb="home_day"),
    # ---------------- SAEED
    dict(to=53, reason="scene and character change: Khalid rushes to Saeed, the imam, at the mosque", chars=["saeed", "khalid"], loc="mosque",
         visual="on the shaded front veranda of the small white island mosque Saeed, the young imam, stands facing Khalid, his eyebrows raised in surprise and concern as he asks a question; Khalid, breathless and dishevelled, stands before him with an anxious, pleading face",
         camera=f"medium two-shot, eye level, {LOW} (veranda floor in shadow)", amb="village_day"),
    dict(to=58, reason="focus change: Saeed listens gravely and grows certain it is sorcery", chars=["saeed"], loc="mosque",
         visual="close-up of Saeed on the mosque veranda listening in deep, grave silence, his eyes narrowed in serious thought, one hand slowly stroking his short beard, his face darkening with certainty and concern",
         camera=f"close-up, eye level, {LOW}", amb="village_day", hum=True),
    dict(to=62, reason="action change: Saeed sits with Khalid and explains how sorcerers deceive", chars=["saeed", "khalid"], loc="mosque",
         visual="Saeed and Khalid sitting side by side on the long wooden bench along the mosque veranda wall; Saeed turned towards Khalid explaining earnestly with one open hand; Khalid listening with his head slowly sinking, his face falling as he understands",
         camera=f"medium shot, eye level, {LOW} (veranda floor in shadow)", amb="village_day"),
    dict(to=65, reason="emotional turning point: Khalid realises he handed his daughter to a sorcerer and breaks down", chars=["khalid"], loc="mosque",
         visual="close-up of Khalid sitting on the bench, bent forward, his hand pressed over his mouth, tears streaming down his face, his eyes wide with guilt and horror, his grey-streaked beard wet with tears",
         camera=f"close-up, eye level, {LOW}", amb="village_day", hum=True),
    # ---------------- HOSPITAL
    dict(to=66, reason="scene change: Khalid reaches the hospital; Faarish and Saahidha by Yamna's bed", chars=["khalid", "faarish", "saahidha", "yamna"], loc="ward_afternoon",
         visual=f"seen from beside the door of the hospital room: Saahidha sits on the plastic chair beside the bed and Faarish stands at the bedside; Yamna lies asleep in the bed, {GOWN}; in the foreground Khalid stands in the doorway, his face stricken and torn, unable to speak",
         camera=f"medium wide shot, eye level, Khalid in the foreground, {LOW} (room floor in soft shadow)", amb="hospital_room",
         transition="dissolve"),
    dict(to=70, reason="scene change: on the empty veranda Khalid tells Faarish the truth; Faarish freezes in guilt", chars=["faarish", "khalid"], loc="veranda",
         visual="on the empty hospital veranda Khalid stands close to Faarish holding his forearm, speaking in a low broken voice, his eyes red with tears; Faarish stands rigid, frozen, his face drained white, eyes wide and unfocused with horror and guilt, breathing hard",
         camera=f"medium two-shot, eye level, {LOW} (pillar shadows across the floor)", amb="hospital_day", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With the news of Aadhanbe's terrifying death, what was talked about most loudly across the whole island was the extraordinary,")
sh(2, "dangerous incident that befell Yamna. The story of the terrible things she did in the kitchen, and of her fighting with death in hospital after food poisoning from eating raw fish guts, had spread fast.")
sh(3, "From every street corner and every teashop, all one heard was talk of the calamity that had struck that family.")
sh(4, "While some said it was the result of sorcery Aadhanbe had done, others believed there was some unknown link between Aadhanbe's death and Yamna's condition.",
   hum=True)
sh(5, "The whole island lay in fear, amid a mass of questions. Those voices reached even inside the hospital walls.")
sh(6, "Yet Yamna, lying on the bed, did not seem to hear any of it. She just lay staring at the ceiling of the room.")
sh(7, "Unable to say a single word, she lay imprisoned in silence, and the tears flowing from her eyes said that something far deeper than the island's talk,",
   [("sob_breath", "ކަރުނަތަކުން", -24)], hum=True)
sh(8, "a terrifying secret, lay hidden in her heart. A special police investigation team began to look into the case of Aadhanbe's terrifying death seriously.")
sh(9, "The police's attention first settled on the evidence found inside the abandoned house where Aadhanbe lay dead.")
sh(10, "The forensic team took fingerprints from the floor of that room and from the chair Aadhanbe had been tied to, and took the sharp blade found there for investigation.",
   [("flashlight_click", "ފޮރެންސިކް", -22)])
sh(11, "When Aadhanbe's body was sent to Malé for a post-mortem,",
   [("boat_engine", "ފޮނުވައިލެވުނުއިރު", -22)], hum=True)
sh(12, "the doctors' report showed that he died from heavy blood loss after his tongue was cut off, and because he could not survive the severe injuries to his body.")
sh(13, "As the investigation went on, the police's compass began to turn towards Yamna's family.")
sh(14, "With the help of the stories spread around the island, the police took statements from witnesses who had seen Faarish and Adheel near the abandoned house where he lay killed, on the night Aadhanbe went missing.")
sh(15, "Besides that, matching the time Aadhanbe went missing and the times Yamna was taken to hospital, Faarish's and Adheel's phone call records, and")
sh(16, "CCTV footage of their movements, the police began to gather. While Faarish and Adheel were at the hospital, a police team came there and began questioning the two young men.",
   [("footsteps_pavement", "އައިސް", -22)])
sh(17, "\"The night Aadhanbe went missing, and this morning, where were you two young men?\" the senior police officer asked.")
sh(18, "Faarish tried to give a false statement while showing a calm face, but his heart pounded harder and his tongue stumbled.",
   [("heartbeat", "ތެޅުން", -22)], hum=True)
sh(19, "Anxiety began to show on Adheel's face too. As the police saw through the truth and lies of their story,")
sh(20, "the suspicion on the two grew stronger. The two young men began to realise that they were close to being caught in the net of the investigation.",
   [("heartbeat", "ޝައްކުތައް", -24)])
sh(21, "After questioning Faarish and Adheel at the hospital, the police did not arrest them at that moment.")
sh(22, "But since the investigation was ongoing, the police warned them not to leave the island and to cooperate fully with the investigation, and then left.",
   [("footsteps_pavement", "ދިޔައެވެ", -22)])
sh(23, "In the midst of all this chaos, when Ghassan got the news of Aadhanbe's death, a great fear entered his heart.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -22)], hum=True)
sh(24, "Ghassan was one hundred percent sure that it was Faarish and the others who had given Aadhanbe such a merciless, bloody punishment.")
sh(25, "Realising that if the truth about Ghassan came out to them, the danger would then be to his own life,",
   hum=True)
sh(26, "Ghassan, without anyone knowing, packed his bags and secretly fled the island and hid. Faarish went out of the hospital,",
   [("cloth_rustle", "ފޮށިތަންމަތި", -20)])
sh(27, "and stood by a shop with a troubled heart. At that moment, something the people gathered there were saying struck his ears.")
sh(28, "Jaleel, who was there, was saying loudly to the others: \"I had even asked Aadhanbe to recite so that bait fish would come to this island.")
sh(29, "Since the night Aadhanbe said he would start reciting, I haven't seen him. After he said he'd recite that night, whenever I went by his house he was never home.\"")
sh(30, "That sentence of Jaleel's went into Faarish's ears like a thunderclap. He felt as if the whole world had started to spin.",
   [("thunder", "ގުގުރިއެއް", -24)], hum=True)
sh(31, "Aadhanbe was not reciting over water on the beach that night to do sorcery on Yamna! What he did was to improve the fishing for the island.")
sh(32, "That is something counted among the Maldivians' customs since old times. Because many people still don't know the evil of such things, they seek help from those who know them.")
sh(33, "Aadhanbe had been, since old times, the man who poured water over children's heads and tied amulets for them in their difficult times.")
sh(34, "There would hardly be a child on that whole island he had not given blown-on water to drink or tied an amulet on. Nor would there be a dhoni launched without Aadhanbe being taken to recite over it.")
sh(35, "Now that many people have come to know that such things too are acts of shirk, those practices have dwindled.")
sh(36, "How hard Aadhanbe tried to tell them these things! But it was Faarish who did not want to look at the other side of the matter.")
sh(37, "With this truth, Faarish's mind went completely blank. His whole body began to tremble and his breath grew frantic.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
sh(38, "Though he had washed himself and put on clean clothes, his two hands were defiled with the blood of an innocent old man.",
   hum=True)
sh(39, "An indescribable feeling of guilt, of grief and of fear surrounded him. His stomach churned and suddenly he began to retch.",
   [("breath_heavy", "ހޮޑުވެސް", -22)])
sh(40, "From the enormity of the ignorant deed he had done, he did not even know how to lift his feet from where he stood, and froze.",
   [("heartbeat", "ގަނޑުވިއެވެ", -22)])
sh(41, "Because of being busy without a moment's rest in worry and unease at the hospital, no one had remembered Ghassan.")
sh(42, "When lunchtime came, Khalid, who had gone out to buy food, called Ghassan to ask what he should bring for him.",
   [("phone_buzz", "ގުޅައިލީ", -22)])
sh(43, "When there was no answer to his phone, Khalid went home and opened the door of Ghassan's room, and he got a sudden shock.",
   [("door_open", "ހުޅުވައިލި", -20)])
sh(44, "Ghassan's room was empty. Not a single thing of his could be seen; not even a hair of his was there.",
   hum=True)
sh(45, "Realising that he had left without even telling them, some kind of unease came over Khalid's heart.")
sh(46, "But he hoped that something had happened and he had suddenly had to leave. Yet even by that afternoon, when Ghassan answered none of his calls, Khalid became sure he had fled.",
   [("phone_buzz", "ފޯނު", -24)])
sh(47, "With Ghassan suddenly fleeing the island without a word, Khalid's heart filled with unease and fear.")
sh(48, "Unable to think of any way out, big questions kept rising in his heart. Fearing that any kind of change might come over Yamna's condition,",
   hum=True)
sh(49, "the anxious Khalid went almost running and met Saeed, the imam of the island's mosque.",
   [("footsteps_sand", "ދުވެފައި", -22)])
sh(50, "His only hope was that, should a sudden danger arise, in order to reach a shore of safety,")
sh(51, "he would get Saeed's help in finding someone else to perform ruqyah. \"Where is Ghassan?\" Saeed asked in surprise, raising his eyebrows.")
sh(52, "When Khalid told him how Ghassan had fled without anyone knowing, a great storm of questions arose in Saeed's mind.")
sh(53, "Sinking into thought, he asked: \"When he treated Yamna, which verses of the Holy Quran did he usually recite?\"")
sh(54, "Saeed asked this question intending to confirm a great suspicion that had formed in his heart long before.")
sh(55, "\"We don't know at all what he recites and what he doesn't. We never hear the sound of the words of Allah.",
   hum=True)
sh(56, "What we hear are all kinds of strange, frightening, unknown sounds we have never heard before!\" Khalid explained in despair.")
sh(57, "As he listened to each of Khalid's sentences, deep seriousness and unease showed on Saeed's face. Ghassan's extraordinary,")
sh(58, "dark practices made it clear and certain to Saeed that what he was doing was evil sorcery, against the religion of Islam.",
   hum=True)
sh(59, "Before starting a treatment, finding out personal details such as the patient's mother's name and date of birth, muttering meaningless foul words,")
sh(60, "obtaining things that contain DNA such as the patient's hair and clothes, and, in the name of treatment, spending time alone with the patient in a locked room — none of these are part of shar'i ruqyah.")
sh(61, "So it was not hard for Saeed to recognise that Ghassan was a deceitful sorcerer. Showing religious evidence and various cultural examples,")
sh(62, "Saeed explained to Khalid in great detail the ways sorcerers throw dust in people's eyes and deceive them. With Saeed's strong evidence,")
sh(63, "Khalid became certain that all these days, with his own hands, he had handed his dearly loved child, dear as his own soul, to a sorcerer like a merciless executioner.",
   hum=True)
sh(64, "With that, he felt an extreme sense of guilt towards himself; the whole world turned upside down,")
sh(65, "his heart broke into pieces and he burst into tears. With the sudden shock and fear, as Khalid went almost running to the hospital,",
   [("sob_breath", "ރޮއިގަނެވުނެވެ", -24), ("footsteps_pavement", "ދުވެފައި", -22)])
sh(66, "Faarish and Saahidha were by Yamna's bed. Khalid had no courage in him at all to tell Saahidha the painful truth burning in his heart.",
   hum=True)
sh(67, "So he quietly took Faarish by the hand, led him outside, and stopped on the empty veranda of the hospital.",
   [("footsteps_pavement", "ނިކުމެ", -22)])
sh(68, "Every word that left his father's tongue pierced Faarish's heart as if stabbed with a sharp dagger. Having trusted Ghassan,",
   [("heartbeat", "ތޮރުފަމުން", -22)], hum=True)
sh(69, "the bitter truth that with his own hands his little sister had been handed over to that evil sorcerer spread through his whole body like a bitter poison.",
   hum=True)
sh(70, "From the feeling of guilt Faarish's breath grew frantic, and his whole body froze. (To be continued)",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
SHOTS = S

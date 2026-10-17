"""Beat/shot plan for Vaanama Iraadhiagai episode 565 (used by plan_beats.py).
Unnamed small Maldivian island. Recap (father died when Luyoon was 12), Aishath proposes Maaniu as a match, the couple
grow close, Zaina is sad, evening walk to the harbour (coffee + juice), Nawfal ("Kyle" in the narration) sneaks up and
taps Luyoon's shoulder, red sunset walk home, Aishath content; school-holiday morning: Luyoon phones Maaniu to invite his
family on a reef-side beach trip; shopping with the siblings.
Rules (series bible): ANIME style; hijab fully covering hair and neck on every woman/girl; Luyoon and Maaniu NOT married
-> always an arm's length apart, never touching; the shoulder tap is by Nawfal only; the late father never shown as a
person; no readable text, letters, numbers or screen content anywhere; Maldivian island, never Japan."""

NOTEXT = "no readable text, letters or numbers anywhere"
GAP = "Luyoon and Maaniu stand an arm's length apart with a clear gap between them, not touching"

LOC = {
    "house": "the family's small single-storey Maldivian island house with a corrugated tin roof and a shady veranda, "
             "a low whitewashed coral-stone garden wall, a wooden joali (rope swing-seat) hanging under a big breadfruit "
             "tree in the white coral-sand yard, red hibiscus bushes and coconut palms",
    "memory_sea": "the veranda of the same small island house in a remembered past, a simple empty wooden chair, beyond "
                  "the palms a wide grey-blue sea with big rolling waves under heavy clouds",
    "living": "the simple bright living room of the island house: whitewashed walls, a cushioned wooden sofa, a woven mat "
              "on a tiled floor, a low wooden table, an open window with a pale curtain and palm fronds outside",
    "lane": "a white coral-sand island lane between low coral-stone garden walls, red hibiscus and pink bougainvillea "
            "spilling over the walls, coconut palms overhead, small tin-roofed houses",
    "harbour": "the island harbour: a long white concrete quay with moored wooden dhonis, sparkling turquoise water, "
               "coconut palms along the waterfront, a small blank take-away kiosk with a plain awning and no signs",
    "shore_sunset": "the island's shore road along the lagoon: a white sand path beside the water, a row of coconut palms, "
                    "the small village roofs ahead, the open sea to the horizon",
    "gate": "the low coral-stone garden wall and small wooden gate of the family's island house on the sandy lane, the "
            "veranda behind with a lamp glowing, coconut palms",
    "yard_night": "the white-sand yard of the family's island house at night: the wooden joali under the breadfruit tree, "
                  "the veranda and windows glowing with warm lamplight, hibiscus bushes",
    "maaniu_house": "the veranda of Maaniu's family house, another small island house: a pale-blue painted wooden door, "
                    "potted plants, a coral-stone wall and palms, the turquoise lagoon glimpsed between the trees",
    "shop": "a small island general shop: wooden shelves of colourful unlabelled snack packets, juice cartons and "
            "bottles of water with plain blank labels, a wooden counter, an open doorway onto a sunny sand lane",
}
MOOD = {
    "house": "golden late afternoon, warm sunlight through the breadfruit leaves, glowing sky with soft drifting clouds, "
             "peaceful and loving",
    "memory_sea": "soft hazy pastel memory glow, muted blue-grey storm light with one ray of sun breaking through the "
                  "clouds, quiet grief and endurance",
    "living": "bright morning, soft sunlight from the window, airy and warm, gentle joy",
    "lane": "bright sunny morning, turquoise and sky-blue, flower petals drifting in a light breeze, spring-like happiness",
    "harbour": "golden late afternoon turning to early evening, cool breeze, sparkling sea light, lively and happy",
    "shore_sunset": "orange-pink sunset, cherry-pink and red clouds glowing across the sky, the sun low over the sea, "
                    "a golden path of light on the water, tender and happy",
    "gate": "blue dusk just after sunset, the last pink glow on the horizon, warm amber lamp light from the veranda",
    "yard_night": "moonlit night with warm amber lamp light, deep blue sky full of stars, calm and content",
    "maaniu_house": "bright morning sunshine, sky-blue and turquoise, cheerful",
    "shop": "bright daytime, sunlight pouring through the open doorway, cheerful and busy",
}

BEATS = [
    dict(to=3, reason="episode opening: the small, happy family of four at their island house", loc="house",
         chars=["luyoon", "aishath", "zaina", "nawfal"],
         visual="sweeping establishing view of the small island house in golden afternoon light; in the sandy yard under "
                "the breadfruit tree Aishath sits on the wooden joali smiling warmly, Luyoon stands beside her with a "
                "gentle smile, Zaina laughs beside Luyoon and little Nawfal grins playing with a coconut husk; a close "
                "loving family, glowing sky above the palms; " + NOTEXT,
         camera="wide establishing shot, slightly low angle, the family in the upper half, white sand as a calm lower third",
         amb="island_house_day"),
    dict(to=5, reason="flashback: the father's death when Luyoon was 12 and Aishath carrying the family alone",
         loc="memory_sea", chars=["aishath"], transition="dissolve",
         visual="soft pastel memory: Aishath, a few years younger, sitting alone on the veranda beside a simple empty "
                "wooden chair with a man's old fishing cap resting on its seat, her hands folded, looking out with "
                "quiet strength at a grey-blue sea with big rolling waves where one small wooden dhoni rides the swell; "
                "a single ray of sunlight breaks through the heavy clouds; " + NOTEXT,
         camera="medium wide shot from the side, eye level, the sea and sky in the upper two-thirds", amb="memory",
         sens="death",
         safe="the father's death is shown only as an empty chair with his old cap and a rough sea (bible rule 7); no person, no funeral"),
    dict(to=9, reason="scene change out of the memory: Aishath tells Luyoon about Maaniu; Luyoon's shy joy",
         loc="living", chars=["aishath", "luyoon"], transition="dissolve",
         visual="Aishath and Luyoon sitting side by side on the cushioned sofa; Aishath turned towards her daughter, "
                "speaking softly with a kind knowing smile, one hand resting gently on Luyoon's hand; Luyoon looks down "
                "with a shy happy blush on her cheeks, anime sparkles in her eyes, a small delighted smile; morning "
                "light from the window; " + NOTEXT,
         camera="medium two-shot, eye level", amb="home_day"),
    dict(to=12, reason="time jump and new characters: Luyoon and Maaniu growing close, laughing about school days",
         loc="lane", chars=["luyoon", "maaniu"], transition="black",
         visual="Luyoon and Maaniu walking side by side along the white coral-sand lane, both laughing, turning their "
                "heads towards each other; " + GAP + "; red hibiscus and pink bougainvillea in full bloom over the walls, "
                "flower petals drifting in the breeze like the arrival of spring, bright sunlight and a glowing blue sky; "
                + NOTEXT,
         camera="medium wide shot, eye level, the two in the upper half, the sand lane as a calm lower third",
         amb="village_day", sens="intimacy",
         safe="unmarried couple: walking side by side in public an arm's length apart, smiles and laughter only, no touching"),
    dict(to=15, reason="character change: Luyoon tells her younger siblings; Zaina is sad", loc="living",
         chars=["luyoon", "zaina", "nawfal"],
         visual="Zaina sitting on the woven mat with a sad pout and a small anime tear in the corner of her eye, Nawfal "
                "sitting close beside her looking up with big worried eyes; Luyoon kneeling in front of them, smiling "
                "warmly and reassuringly, one hand gently on Zaina's shoulder; soft daylight from the window; " + NOTEXT,
         camera="medium shot, slightly high angle, faces in the upper two-thirds", amb="home_day"),
    dict(to=17, reason="scene and time change: evening at the island harbour, the whole island out in the breeze",
         loc="harbour", transition="black",
         visual="sweeping wide view of the island harbour in the golden late afternoon: wooden dhonis moored along the "
                "white quay, sparkling turquoise water, palms swaying in the cool breeze, many small background islanders "
                "strolling — families with small children, elderly men, women in modest dresses and headscarves; a glowing "
                "sky with drifting clouds; no main characters; " + NOTEXT,
         camera="wide establishing shot, high angle, the sky and harbour in the upper two-thirds, calm water as the lower third",
         amb="harbour_cafe"),
    dict(to=20, reason="characters enter: Luyoon and Maaniu at the take-away kiosk with coffee and juice", loc="harbour",
         chars=["luyoon", "maaniu"],
         visual="Luyoon and Maaniu standing beside the small blank take-away kiosk on the harbour quay; Maaniu holds a "
                "paper cup of coffee, Luyoon holds a tall cup of orange juice with a straw; " + GAP + "; they smile and "
                "talk happily, dhonis and sparkling water behind them, golden evening light; " + NOTEXT,
         camera="medium two-shot, eye level", amb="harbour_cafe", sens="intimacy",
         safe="unmarried couple in a public place, each holding their own drink, an arm's length apart"),
    dict(to=24, reason="new character and action: Nawfal sneaks up and taps Luyoon's shoulder to scare her",
         loc="harbour", chars=["nawfal", "luyoon", "maaniu", "zaina"],
         visual="on the harbour quay little Nawfal with a big mischievous grin, having just tapped his sister Luyoon on "
                "the shoulder from behind with one finger; Luyoon turned around with wide startled anime eyes and her "
                "juice cup in hand; Maaniu standing an arm's length away on her other side laughing, holding his coffee; "
                "Zaina giggling a few steps behind Nawfal; golden-orange evening light; nobody touches Maaniu; " + NOTEXT,
         camera="medium wide shot, eye level", amb="harbour_cafe", sens="other",
         safe="the shoulder tap is by the little brother only (sibling); Luyoon and Maaniu stay an arm's length apart"),
    dict(to=27, reason="time and scene change: red sunset, the two walk home", loc="shore_sunset",
         chars=["luyoon", "maaniu"],
         visual="sweeping wide view of a blazing orange-pink sunset over the lagoon, cherry-pink and red clouds rising "
                "across the sky; on the white sand path along the shore two small figures, Luyoon and Maaniu, seen from "
                "behind walking side by side towards the village with a clear gap between them, not touching, long "
                "shadows on the sand, palms in silhouette; " + NOTEXT,
         camera="wide shot from behind, the sky filling the upper two-thirds, the sand path as a calm lower third",
         amb="beach_evening", sens="intimacy", safe="figures small and from behind, clearly apart"),
    dict(to=30, reason="scene change: arriving at the house gate at dusk; Aishath waiting", loc="gate",
         chars=["luyoon", "maaniu", "aishath"],
         visual="at blue dusk Luyoon stands at the open wooden gate of her house, turning back with a smile; Maaniu "
                "stands out in the sandy lane well over an arm's length away, raising one hand in a friendly goodbye "
                "wave and smiling; on the lamp-lit veranda behind, Aishath stands in the doorway with her hands folded, "
                "waiting with a gentle questioning look; " + NOTEXT,
         camera="medium wide shot, eye level", amb="island_house_night", sens="intimacy",
         safe="goodbye shown only as a wave across the gate, no touching; the mother is present"),
    dict(to=32, reason="action and mood change: Aishath alone, content with her children and her new 'son'",
         loc="yard_night", chars=["aishath"],
         visual="Aishath sitting alone on the wooden joali under the breadfruit tree at night, hands resting in her lap, "
                "a deeply contented gentle smile and shining grateful eyes, looking towards the warmly lit windows of "
                "her house; a moonlit starry sky, hibiscus flowers glowing in the lamp light; " + NOTEXT,
         camera="medium shot from the side, eye level, the sky and lit windows in the upper half", amb="island_house_night"),
    dict(to=34, reason="return to the couple's growing bond (reuse of beat_004)", loc="lane",
         chars=["luyoon", "maaniu"], reuse="beat_004", visual="(reuse of beat_004)", amb="village_day",
         sens="intimacy", safe="reused image: walking an arm's length apart"),
    dict(to=36, reason="time jump: a school-holiday morning, the family packing for a trip", loc="living",
         chars=["luyoon", "aishath", "zaina", "nawfal"], transition="black",
         visual="busy happy morning in the living room: Aishath packing a woven basket with wrapped snacks and a thermos, "
                "Zaina folding beach mats, Nawfal excitedly stuffing towels into a bag, Luyoon in the middle with a "
                "bright smile closing a cooler box; bright morning light, everyone cheerful; " + NOTEXT,
         camera="medium wide shot, slightly high angle", amb="home_day"),
    dict(to=40, reason="action change: Luyoon phones Maaniu to invite his family", loc="house", chars=["luyoon"],
         visual="Luyoon standing on the shady veranda of her house in bright morning light, holding a phone to her ear "
                "(the phone's back facing the viewer, no screen visible), beaming with excitement, her free hand raised "
                "lightly as she talks, hibiscus and palms behind her; " + NOTEXT,
         camera="medium close-up, eye level", amb="island_house_day"),
    dict(to=43, reason="character change: Maaniu calls back - his family agreed", loc="maaniu_house", chars=["maaniu"],
         visual="Maaniu standing on the veranda of his family's house in bright morning sun, holding a phone to his ear "
                "(no screen visible), smiling eagerly as he speaks, his other hand in his jacket pocket, the turquoise "
                "lagoon sparkling between the palms behind him; " + NOTEXT,
         camera="medium close-up, eye level", amb="island_house_day"),
    dict(to=44, reason="scene change: shopping with the siblings for the trip", loc="shop",
         chars=["luyoon", "zaina", "nawfal"],
         visual="inside the small island shop Luyoon smiles as she picks juice cartons with plain blank labels from a "
                "shelf, Zaina holds a woven shopping basket already full of colourful unlabelled snack packets, and "
                "Nawfal proudly holds up a big bag of crisps with no writing on it; sunny lane outside the doorway; "
                + NOTEXT,
         camera="medium wide shot, eye level", amb="shop_day"),
    dict(to=46, reason="emotional close: Maaniu glowing with joy before their first trip together", loc="maaniu_house",
         chars=["maaniu"],
         visual="close-up of Maaniu at the gate of his house in bright morning sun, a packed bag over his shoulder, his "
                "face glowing with pure happiness, eyes sparkling, a wide warm smile, soft lens glow and sparkling "
                "turquoise sea light behind him; " + NOTEXT,
         camera="close-up, slightly low angle, face in the upper two-thirds", amb="island_house_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Even when one has to face many hardships and troubles, not everything in life is hardship. One may also live with happiness.")
sh(2, "People who have lived together in love may have to part from each other. Only very few get to live happily as a small family.")
sh(3, "With tenderness. Luyoon, her two younger siblings and Luyoon's mother are living very happily.")
sh(4, "Even when they had to travel through rough seas, Luyoon, her mother Aishath and the two little ones faced those seas. When Luyoon was 12, her father left this world.",
   [("wave_crash", "ކަނޑެއްގައި", -22)])
sh(5, "After that, it was Aishath (Luyoon's mother) who carried every single thing that had to be done. At that time Luyoon and the two little ones were studying.")
sh(6, "\"My daughter Luyoon, you have now taken care of things on your own. And now, Maaniu... he is a boy of good character, so...\" This was after going to that house.")
sh(7, "Aishath said. Luyoon was overjoyed - because she had heard her mother's new words. But...",
   hum=True)
sh(8, "What was in Maaniu's heart was not known at all: how he saw the matters of life, or whether he could build a life with Luyoon.")
sh(9, "\"Shall Mamma see if it can be arranged with that boy?\" Aishath said. \"Whatever Mamma wants,\" Luyoon said with a smile. Minutes and seconds...")
sh(10, "...the seconds turned into hours. Now the bond between Luyoon and Maaniu is growing stronger day after day.")
sh(11, "It turned into a friendship. Remembering their school days, the two of them laugh and joke. A few days later...")
sh(12, "it was as if spring had come into Luyoon's life. It turned into happiness - as if a new flower had bloomed in her life.",
   hum=True)
sh(13, "She shared the news with her two younger siblings. \"So we won't see Donthi any more, right...\" Zaina said, sounding sad.",
   [("sigh", "ދެރަވެފައި", -22)])
sh(14, "\"Donthi will always stay close to the little ones and Mamma... I won't go anywhere else,\" Luyoon said with a smile.")
sh(15, "However much one tries to hide things... destiny cannot be changed. But Luyoon wants to be with her family.")
sh(16, "With their joys - their happiness. The cool evening breezes filled the whole air.",
   [("leaves_rustle", "ވައިރޯޅި", -22)])
sh(17, "Young and old, everyone on the island was out at the island harbour - couples, and parents with their little children.")
sh(18, "As evening came, Luyoon and Maaniu also went out, meaning to take a walk, meaning to talk about many things,")
sh(19, "meaning to make many promises and vows. At a take-away coffee place near the harbour Maaniu got a coffee and Luyoon a juice.",
   [("cup_clatter", "ކޮފީ", -22)])
sh(20, "In a moment the two reached the place they wanted to go: the harbour - to spend some truly happy moments.")
sh(21, "\"Hey Donthi, what's going on?\" Kyle said after tapping Luyoon on the shoulder. \"Kyle, what is this...",
   [("gasp", "ކޮއްޓާލުމަށް", -20)])
sh(22, "you were at home when Donthi left the house - when did you get here?\" Luyoon said, her eyes wide. She didn't know what to say. \"Did Donthi know...")
sh(23, "Mamma brought us because we were bored... and when we came here we saw Donthi and them. So we wanted to give you a scare...\"")
sh(24, "Kyle said, laughing. Kyle is a very naughty kid anyway - a playful one. The two of them have just the same nature.")
sh(25, "Having done its duty, the sun was close to setting. Red clouds began to rise across the sky.")
sh(26, "\"Maaniu, let's head home - the sun is setting,\" Luyoon said. Then the two of them walked off towards home.",
   [("footsteps_sand", "ހިގައިގަތީ", -22)])
sh(27, "In a happy moment the two went towards home. They didn't want to part. But right now the two had to go home.")
sh(28, "Luyoon reached home. \"See you later,\" Maaniu said with a smile. Aishath had been waiting for Luyoon to come. \"Where have you been...",
   [("footsteps_sand", "އާދެވިއްޖެއެވެ", -24)])
sh(29, "...\" Aishath said. \"I was at the harbour with Maaniu,\" she said with a smile.")
sh(30, "Whenever Luyoon went somewhere and was late, Aishath always asked her - it was something she did every single time she was late.")
sh(31, "Today it was as if spring had come to that house too. Aishath had gained another child who would call her 'Mamma'.")
sh(32, "Every mother dreams many dreams about all of this. The children she raised with love are devout, well-mannered and get along with others - and Aishath is overjoyed.",
   hum=True)
sh(33, "The bond between Maaniu and Luyoon, too, grows stronger day after day. Even if a problem sometimes arises between the two,")
sh(34, "they settle those things - as something resolved between Maaniu and Luyoon themselves.")
sh(35, "Many things have happened in life, and not only for that small family. It was one morning, during the school holidays.")
sh(36, "Luyoon and her family had decided to go on a trip. They are getting ready the things they need for it.",
   [("cloth_rustle", "ތައްޔާރު", -24)])
sh(37, "Luyoon picked up her phone and called Maaniu's number. \"Labbaik...\" Maaniu said. \"We're going on a trip - come, let's take Mamma and them on a trip,")
sh(38, "Luyoon said. By now both sides had agreed to Luyoon and Maaniu's match. \"I'll just ask Mamma and them, okay...")
sh(39, "give me a few minutes,\" Maaniu said and hung up. Luyoon did this so that both families would know each other,")
sh(40, "to strengthen the friendship, and so that both families could come to trust Luyoon and Maaniu.")
sh(41, "Luyoon's phone began to vibrate - it was Maaniu calling. She quickly picked up. \"Mamma and them said okay...",
   [("phone_buzz", "ވައިބްރޭޓް", -18)])
sh(42, "Which way are we going?\" Maaniu said. \"We're going to the beach on the reef side of the island. Is there anything special your Mamma and them eat?\" Luyoon said.")
sh(43, "\"Nothing special like that,\" Maaniu said. After that, Luyoon hurried off to get the things they would need for the trip.")
sh(44, "With her two little siblings she went to different shops and bought all sorts of things. Maaniu, too, kept asking Luyoon what things to bring.")
sh(45, "This is the first trip since Maaniu and Luyoon were matched. It is sure to be a happy journey.")
sh(46, "Since it was a trip for Maaniu after so many days, his face was glowing with happiness.", hum=True)
SHOTS = S

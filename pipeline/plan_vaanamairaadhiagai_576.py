"""Beat/shot plan for Vaanama Iraadhiagai episode 576 (used by plan_beats.py). Anime look (series style.txt)."""

LOC = {
    "island_morning": "a small inhabited Maldivian island seen in a sweeping high wide view at morning: a small harbour with wooden dhonis heading out through a turquoise lagoon, white coral-sand lanes between small single-storey houses with tin roofs and coral-stone walls, tall coconut palms, a white minaret far in the background, open ocean to the horizon",
    "beach": "a reef-side beach of a small Maldivian island: powdery white sand, leaning coconut palms, a glassy turquoise lagoon with sparkling light, a reef line far out, small houses half hidden behind the palms",
    "takeaway": "the harbour front of a small Maldivian island: a small take-away juice kiosk with a plain wooden counter and a tin awning with no sign, a few plastic stools, moored dhonis on the calm harbour water, coconut palms and a white coral-sand lane leading home",
    "lane": "a quiet palm-shaded white coral-sand lane of a Maldivian island between low coral-stone garden walls with bougainvillea, small houses with tin roofs, dappled light under breadfruit and coconut trees",
    "maaniu_veranda": "the open veranda of a small Maldivian island house: a wooden bench, a low coral-stone wall, potted plants, coconut palms beyond and the sea at the end of the lane",
    "naaifaa_room": "a girl's small bedroom in a Maldivian island house at night: a window with a plum curtain looking out on dark palms, a small dressing table, plain painted walls",
    "shore_sunset": "the empty white sand shore of the island at sunset, gentle foaming wavelets, coconut palm silhouettes, the sun low over the lagoon",
    "living": "the modest living room of the family's small Maldivian island house at night: a cushioned sofa, a low wooden table, a woven mat on tiled floor, a ceiling fan, a short hallway leading to a bedroom door",
    "luyoon_room_day": "Luyoon's small tidy bedroom in the island house: a single bed with a plain cream bedspread, a wooden wardrobe, a window with light curtains looking out on coconut palms and a sliver of turquoise sea",
    "luyoon_room_dusk": "a small wooden table beside the bedroom window in Luyoon's room, the window open to palms and the sea",
    "luyoon_room_night": "Luyoon's small bedroom in the island house at night: a single bed with a plain cream bedspread, a wooden wardrobe, a wooden door, a window looking out on palms and a moonlit lagoon",
    "memory": "the family's yard of the island house at night: the outdoor wooden joali (rope swing-seat) under a big tree, coconut palms, the sea beyond the low coral-stone wall",
}
MOOD = {
    "island_morning": "bright clear morning, cloudless glowing sky-blue, sparkling sea light, soft lens glow, peaceful and alive",
    "beach": "bright morning sun, cloudless sky, glittering turquoise lagoon, light breeze in the palms, joyful and carefree",
    "takeaway": "warm golden late-morning light, sparkling harbour water, light-hearted family warmth",
    "lane": "golden afternoon light in dappled shadow, a few days later, uneasy undertone",
    "maaniu_veranda": "blue dusk, the sky fading from orange-pink to deep blue, the cold glow of a phone screen on his face, conflicted and heavy",
    "naaifaa_room": "moonlit night with warm amber lamp light, her face lit from below by a phone glow, sly triumph",
    "shore_sunset": "orange-pink sunset with cherry-pink clouds fading into dusk, melancholy, something ending",
    "living": "moonlit night with warm amber lamp light, quiet concern",
    "luyoon_room_day": "pale washed-out grey afternoon light through the curtains, weeks passing, lonely and numb",
    "luyoon_room_dusk": "blue dusk light with a single warm lamp, still and wistful, a dream left unfinished",
    "luyoon_room_night": "moonlit night with warm amber lamp light, deep blue shadows, intimate, tearful and tender",
    "memory": "soft hazy pastel memory glow over a deep starry night sky, a gentle shimmer of stars over the sea, longing",
}

APART = "an arm's length apart, not touching"

BEATS = [
    dict(to=4, reason="episode opening: establishing the calm island morning (fishermen, sweepers, calm sea)", loc="island_morning",
         visual="sweeping anime establishing shot of the island at morning seen from high above the lagoon: two small wooden dhonis with fishermen leaving the harbour leaving white wakes on mirror-calm turquoise water, tiny background figures of women in long dresses and headscarves sweeping the white sand lanes with long brooms, crows on a palm frond, a cloudless glowing sky, sparkling sea; no readable text",
         camera="extreme wide high-angle establishing shot, the island and sky in the upper two-thirds, calm lagoon water as the lower third", amb="island_day"),
    dict(to=8, reason="character change: Luyoon playing on the beach with her younger siblings", chars=["luyoon", "zaina", "nawfal"], loc="beach",
         visual="Luyoon laughing brightly as she plays with her little brother Nawfal and younger sister Zaina at the water's edge, Nawfal kicking up a small sparkle of splashing water, Zaina in her sky-blue dress and white hijab clapping and giggling, Luyoon in her cream-white dress and black hijab fully covering hair and neck, the hem dry above the wavelets, anime sparkles of sunlight around them, pure happiness",
         camera="medium wide shot, eye level, the three in the upper two-thirds, wet sand and wavelets as the lower third", amb="beach_day"),
    dict(to=12, reason="character entrance: Maaniu startles Luyoon and they tease each other", chars=["luyoon", "maaniu"], loc="beach",
         visual=f"Maaniu (curly black hair, charcoal jacket over white shirt) standing on the sand with a mischievous grin and one hand raised in greeting, Luyoon turned towards him with a startled then laughing expression, a hand at her own chest, playful anime sweat-drop, the two {APART} with clear open sand between them; behind them only the empty sparkling lagoon and palms, no other people in the scene",
         camera="medium two-shot, eye level, both faces in the upper half, open sand as the lower third", amb="beach_day"),
    dict(to=15, reason="character change: Naaifaa secretly watching the couple with jealousy", chars=["naaifaa", "luyoon", "maaniu"], loc="beach",
         visual=f"Naaifaa in her plum abaya and lilac hijab half hidden behind the trunk of a leaning coconut palm in the foreground, peering out with narrowed jealous eyes and pressed lips, a dark anime shadow across her upper face; far in the background on the bright beach Luyoon and Maaniu as small figures laughing, {APART}",
         camera="over-the-shoulder medium shot from behind the palm, Naaifaa's face in the upper third foreground, the bright beach behind, sand as the lower third", amb="beach_day",
         sens="other", safe="her scheming is shown only as a look from behind a palm (bible rule 10)"),
    dict(to=19, reason="scene change: juice at the harbour take-away and walking home", chars=["maaniu", "luyoon", "zaina", "nawfal"], loc="takeaway",
         visual=f"Maaniu at a small harbour take-away kiosk handing a plastic cup of orange juice to little Nawfal, who reaches up beaming; Zaina already sipping her juice through a straw with a happy face; Luyoon a step away holding her own cup and smiling warmly at the scene, Maaniu and Luyoon {APART}; the kiosk has a plain wooden counter and no sign; dhonis moored on the sparkling water behind",
         camera="medium wide shot, eye level, the group and kiosk in the upper two-thirds, the white sand lane as the lower third", amb="harbour_cafe"),
    dict(to=24, reason="time jump ('a few days later') and character change: Naaifaa slanders Luyoon to Maaniu", chars=["naaifaa", "maaniu"], loc="lane",
         visual="Naaifaa and Maaniu standing in a palm-shaded sand lane about two arm's lengths apart, Naaifaa leaning slightly towards him with a falsely concerned face, one hand lifted as she speaks; Maaniu with his brow knitted in doubt and disbelief, eyes cast aside, troubled; a dark cloud shadow sliding over the dappled light",
         camera="medium two-shot, eye level, faces in the upper half, the sandy lane and shadows as the lower third", amb="village_day", transition="black",
         sens="other", safe="slander shown only as talk at a distance and Maaniu's troubled face"),
    dict(to=26, reason="action and place change: Maaniu rejects Luyoon's calls", chars=["maaniu"], loc="maaniu_veranda",
         visual="Maaniu sitting alone on the veranda bench at blue dusk, a mobile phone glowing in his hand with a plain blank bright screen (no text, no icons), his thumb hovering over it, his face half in shadow, jaw clenched, eyes pained and conflicted",
         camera="medium close-up, slightly low angle, his face in the upper third, the bench and veranda floor as the lower third", amb="island_house_night"),
    dict(to=28, reason="character change: Naaifaa's evil smile of triumph", chars=["naaifaa"], loc="naaifaa_room",
         visual="close-up of Naaifaa by her bedroom window at night, plum abaya and lilac hijab fully covering hair and neck, her face lit from below by the blank glow of the phone in her hand, a sly satisfied anime smile, one eye glinting, a few faint sparkles in the dark air; she is the only person in the image, no visions, no second figure",
         camera="close-up, slightly low angle, her face in the upper half, the dark window sill as the lower third", amb="room_night",
         sens="other", safe="her scheme is shown only as a smug smile lit by a blank phone glow (bible rules 9-10)"),
    dict(to=30, reason="symbolic turning point: the engaged couple is forced apart", loc="shore_sunset",
         visual="two lines of footprints in the white sand that walked side by side and then split apart in opposite directions, a gentle wave washing over where they part, cherry-pink sunset clouds glowing above the lagoon, coconut palm silhouettes, no people",
         camera="low angle wide shot along the sand, the sky and parting footprints in the upper two-thirds, smooth wet sand as the lower third", amb="beach_dusk",
         sens="other", safe="the break-up is shown symbolically with parting footprints, no people"),
    dict(to=31, reason="scene and character change: Mother asks Luyoon at home", chars=["aishath", "luyoon"], loc="living",
         visual="Aishath in her maroon libaas and beige headscarf standing in the lamp-lit living room looking after her daughter with worried eyes; Luyoon in her cream dress and black hijab turning away towards the hallway and her bedroom door, a forced small smile that does not reach her sad eyes",
         camera="medium wide shot, eye level, both figures in the upper two-thirds, the woven mat floor as the lower third", amb="living_night"),
    dict(to=35, reason="time jump ('days turned into weeks'): Luyoon alone, trying to reach Maaniu", chars=["luyoon"], loc="luyoon_room_day",
         visual="Luyoon sitting on the edge of her bed by the window, fully dressed in her cream dress and black hijab covering hair and neck, holding her phone to her ear with a blank screen, staring out of the window with dull tired eyes and a faint tear trail, the room drained of colour, dust motes floating in pale light",
         camera="medium shot from the side, her face in the upper third, the bedspread and floor as the lower third", amb="room_day", transition="black"),
    dict(to=38, reason="narrator's reflection on the abandoned wedding plans: symbolic detail image", loc="luyoon_room_dusk",
         visual="still life on the small wooden table by the window at dusk: a closed small velvet ring box, neatly folded new cream wedding fabric tied with a ribbon, a little jar of jasmine flowers wilting, a blank card with nothing written on it, the window glowing blue with palms beyond, no people",
         camera="close-up still life, the objects and window in the upper two-thirds, the plain table top as the lower third", amb="room_day",
         sens="other", safe="the cancelled wedding is shown through symbolic objects only"),
    dict(to=41, reason="character entrance: Zaina at the locked door, comes into Luyoon's room", chars=["zaina", "luyoon"], loc="luyoon_room_night",
         visual="Zaina in her sky-blue dress and white hijab peeking in through the half-opened bedroom door at night with big worried anime eyes; Luyoon fully dressed in her cream dress and black hijab covering hair and neck, standing just inside holding the door handle, her eyes red and downcast; warm amber lamp light and moonlight through the window",
         camera="medium shot, eye level, both faces in the upper half, the tiled floor as the lower third", amb="room_night"),
    dict(to=42, reason="action change / emotional peak: the sisters hug and Luyoon breaks down sobbing", chars=["luyoon", "zaina"], loc="luyoon_room_night",
         visual="the two sisters sitting side by side on the edge of the bed in a tender sideways embrace, Luyoon (cream dress, black hijab fully covering hair and neck) holding her little sister Zaina (sky-blue dress, white hijab) tightly, eyes squeezed shut with sparkling anime tears streaming down her cheeks; Zaina's eyes wide with worry; moonlight and warm lamp glow",
         camera="medium close-up, eye level, faces in the upper half, the bedspread as the lower third", amb="room_night",
         sens="other", safe="two sisters, both in hijab and fully clothed, a tender sideways embrace on the bed edge (bible rule 6)"),
    dict(to=43, reason="memory: Luyoon wishes their late father were alive (symbolic, father never shown)", loc="memory",
         visual="the empty wooden joali swing-seat under the big tree in the yard at night, an old faded fisherman's cap resting on the empty seat, a vast starry sky shimmering over the sea beyond the low coral-stone wall, soft hazy pastel glow, no people",
         camera="wide shot, the joali and starry sky in the upper two-thirds, the sandy yard as the lower third", amb="memory", transition="dissolve",
         sens="other", safe="the late father is never shown: only his empty joali seat, his old cap and the stars (bible rule 7)"),
    dict(to=46, reason="action change: Luyoon pulls back, wipes her tears and confides the break-up", chars=["luyoon", "zaina"], loc="luyoon_room_night",
         visual="the sisters sitting facing each other on the bed edge, Luyoon wiping her tears with the back of her hand, lips trembling as she speaks, Zaina leaning in and holding her big sister's hands in both of hers with a determined, trusting face; both in hijab fully covering hair and neck; a single lamp glows warm amber",
         camera="medium two-shot, eye level, faces in the upper half, the bedspread as the lower third", amb="room_night", transition="dissolve"),
    dict(to=48, reason="emotional turning point: Zaina's shock at the news (reaction close-up)", chars=["zaina", "luyoon"], loc="luyoon_room_night",
         visual="dramatic anime close-up of Zaina's face, eyes wide open in shock, mouth slightly open, white hijab fully covering hair and neck; behind her, softly out of focus, Luyoon looking down sadly at a phone with a blank dark screen in her lap",
         camera="close-up on Zaina, eyes in the upper third, soft blurred bedspread as the lower third", amb="room_night"),
    dict(to=50, reason="closing: the sisters at the window hoping for better days", chars=["luyoon", "zaina"], loc="luyoon_room_night",
         visual="the two sisters seen from behind and slightly to the side, sitting together at the open bedroom window looking out at the moonlit lagoon and a starry sky, Zaina's head resting gently on Luyoon's shoulder, a faint first glow of hope on the horizon, palm silhouettes, quiet and tender",
         camera="wide shot from behind, the window, moon and sky in the upper two-thirds, the dark window sill and floor as the lower third", amb="room_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "It was a day with a clear, beautiful sky. The fishermen were busy setting out to fish in their dhonis.",
   [("dhoni_engine", "ދޯނީގައި", -22)])
sh(2, "The women who sweep the neighbourhood went on with their work tirelessly. There was not even a single wisp of cloud in the sky.")
sh(3, "The sea lay flat as oil. Not a wave to be seen; it was that calm. From inside the island came the calls of crows and koels.")
sh(4, "With the voices of people joined to them, a heart-pleasing music had formed. As it was the school holidays, not a single schoolchild was to be seen on the roads.")
sh(5, "Luyoon was playing on the beach with her two younger siblings. These days Luyoon had taken family-responsibility leave, so she did not have to go to the office.",
   [("water_splash_small", "ކުޅުމުގައި", -24)])
sh(6, "A happy spring season had come to Luyoon. She felt as if she were flying above the clouds.")
sh(7, "It was as if Luyoon had found a joy she had never had before. Maaniu too had found a happy life.")
sh(8, "For the two lovers it was a happiness they had never known. Luyoon and Maaniu believed that nothing sad would ever come their way again.")
sh(9, "This is the world. In the world there will be many hardships and many joys. Sometimes there will even be times when one must cry alone.")
sh(10, "But today Luyoon and Maaniu found that hard to accept, and just as hard to understand. \"Hi Luyoon.")
sh(11, "You're up so early today! What happened this time?\" Maaniu asked. \"You startled me! Don't do things like that...\"",
   [("gasp", "ސިއްސައިގެން", -20)])
sh(12, "Luyoon said. Maaniu and Luyoon were always joking and teasing each other. That was the nature of the two of them.")
sh(13, "But Naaifaa could only watch it with great jealousy. Naaifaa was going to great lengths to separate the two lovers.")
sh(14, "Maaniu and Luyoon did not know it. Maaniu always said that no one could ever come between the two of them, that theirs was true love.")
sh(15, "And yet it could not be told to Luyoon. Maaniu did not know what was in Luyoon's heart.")
sh(16, "Maaniu, Luyoon, Zainaa (Luyoon's younger sister) and Naufal (her younger brother) set off towards home. \"Luyoon, Zainaa and Naufal, come here...",
   [("footsteps_sand", "ހިގައިގަތީ", -22)])
sh(17, "let's have a juice!\" Maaniu called to Luyoon, stopping near a take-away by the way. Luyoon and her two siblings walked over.")
sh(18, "Maaniu always loved Luyoon's little family immensely. Because of that, Luyoon was always happy.")
sh(19, "A man with such good manners is found only rarely. Luyoon, her two siblings and Maaniu took their juices and walked towards home.",
   [("footsteps_sand", "ހިގައިގަތެއެވެ", -24)])
sh(20, "They went on teasing and joking. A few days later, the flames of Naaifaa's jealousy burst out.")
sh(21, "And many things were said to Maaniu. \"Do you know, Maaniu, that Luyoon is a bad girl...")
sh(22, "However good she pretends to be, she is a very bad girl,\" Naaifaa said. Maaniu found it hard to believe, but he wanted to look into the matter.")
sh(23, "Maaniu always looked at things from both sides. \"No, it isn't like that. All these days I have been with Luyoon. She is not such a bad person.")
sh(24, "But I will look into it,\" Maaniu said. From that day on, Maaniu's days turned dark, and a weakness came into Maaniu and Luyoon's bond.",
   hum=True)
sh(25, "Maaniu's phone began to ring. He glanced at the display: it was Luyoon calling. He rejected the call.",
   [("phone_buzz", "ރިންގ", -16)])
sh(26, "She called about three times, but Maaniu did not answer, for many reasons. Naaifaa sensed that her wicked plan had succeeded that day.",
   [("phone_buzz", "ގުޅިއެވެ", -20)])
sh(27, "And so a wicked smile spread across Naaifaa's face. The hope of many days had been fulfilled today, and it brought Naaifaa joy.")
sh(28, "Naaifaa felt that the sweet dreams of many days had finally taken on colour.")
sh(29, "But that turned into many obstacles in the life of Maaniu and Luyoon.")
sh(30, "Even though their wedding lay ahead, they had to drift apart; it could not happen, and the two had to separate. \"Luyoon, my dear...",
   hum=True)
sh(31, "what happened, did something go wrong again?\" Mother asked. After a small smile, Luyoon walked towards her room. She said nothing at all.",
   [("footsteps_pavement", "ހިގައި", -24)])
sh(32, "Luyoon wanted to keep all of this secret, and not let anyone know. The world kept turning. Days turned into weeks.")
sh(33, "One day after another. Luyoon seemed unaware of anything happening in the world, as if she had grown weary of it.")
sh(34, "Luyoon kept trying to reveal to Maaniu how all of this had really happened.")
sh(35, "But Maaniu, believing Naaifaa's words, had grown tired of Luyoon. This is the way the world goes.")
sh(36, "Loved ones and the closest friends will leave. While the two of them were preparing for their new marriage...")
sh(37, "and while each suited the other's nature so well, no one knows how today things came to be like this.")
sh(38, "Though love and care had always been given, Luyoon could not accept that Maaniu had believed what someone else said.")
sh(39, "\"Big sister... open the room door,\" Zainaa said. Slowly the locked door was opened, and as soon as it opened Zainaa came into Luyoon's room.",
   [("knock", "ހުޅުވަބަލަ", -18), ("lock_click", "ހުޅުވާލި", -20), ("door_open", "ވަދެގަތެއެވެ", -20)])
sh(40, "\"Big sister... what really happened? These past days your face has looked so sad,\" Zainaa asked.")
sh(41, "Zainaa is Luyoon's one and only younger sister. Luyoon shares everything with Zainaa; she knows of nothing she has not told her.")
sh(42, "Luyoon hugged Zainaa tightly and started to sob and cry. \"These days your big sister has no happiness at all... always heartache...",
   [("cloth_rustle", "ބައްދާލި", -22), ("sob_breath", "ރޮވެން", -22)], hum=True)
sh(43, "If Dad were alive today, we wouldn't have to live like this. Dad always kept us happy,\" Luyoon said, crying. \"Big sister, stop it.",
   [("sob_breath", "ރޮމުން", -24)], hum=True)
sh(44, "Tell me what's going on, won't you?\" Zainaa said after pulling away from Luyoon. Wiping her tears, Luyoon said not to tell this to anyone.",
   [("breath", "ފޮހެލަމުން", -26)])
sh(45, "No one else must know of this. \"Big sister... trust me,\" Zainaa's little heart could not wait. \"Your big sister and Maaniu Bebe...")
sh(46, "have separated. Maaniu Bebe won't come anymore.\" Luyoon began to cry again. Today the only one supporting Luyoon was little Zainaa.",
   [("sob_breath", "ރޮވުނެއެވެ", -24)], hum=True)
sh(47, "\"What. Are you serious... when did this happen?\" Zainaa said, her eyes wide open.",
   [("gasp", "ބޮޑު", -20)])
sh(48, "For no one knew the reason why two people who had loved so much had come apart. \"For two weeks now, whenever your big sister calls, he rejects the call,\"")
sh(49, "Luyoon said. The world is a house of tests, a journey filled with joy and heartache.")
sh(50, "Luyoon and Zainaa keep hoping, always, for the day when the heartache Luyoon is going through today will come to an end.",
   hum=True)
SHOTS = S

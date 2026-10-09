"""Beat/shot plan for Nindheveethimeymathee episode 339 (used by plan_beats.py).
SCHOOL timeline. Asil's family apartment (study session, gaming, the hidden poem), then night at Maama Shafeeqa's house.
Lail and Saba are unmarried 17-year-olds: they never touch; the under-table foot moment is never shown.
Sadhee is a GIRL (Saba's friend) gaming on her own bean bag well apart from Asil."""

APT = "Asil's family's modern ninth-floor apartment in Malé, Maldives"
MAAMA = "Maama Shafeeqa's comfortable two-storey family house in Malé, Maldives"
LOC = {
    "asil_living": f"the bright sitting and dining area of {APT}: a light wooden dining table with school textbooks, exercise books, pens and pencils spread on it, cushioned dining chairs, a cream sofa and a low coffee table behind, a glass balcony door with sheer curtains showing a hazy view of Malé rooftops and the blue lagoon, potted green plants, tiled floor",
    "asil_room": f"a teenage boy's bedroom in {APT}: a wall-mounted TV with a game console below it (the screen turned away from the viewer, only its coloured glow visible), two big soft bean bags on a grey rug, a single bed made neatly against the far wall with a navy cover, a study desk with a lamp, a window with blinds, tiled floor",
    "asil_door": f"the open front door of {APT} seen from inside the sitting area, looking out onto a clean bright apartment-building corridor with a pale tiled floor and the closed steel doors of a lift a few steps away, a shoe rack by the door",
    "maama_porch": f"the open front veranda of {MAAMA}: a round rattan hanging swing chair on a tiled veranda, potted bougainvillea and a frangipani tree, a carved wooden main door standing open into a warm lamp-lit hall with a large round wall clock with a plain face and no numerals",
    "maama_dining": f"the warm family dining room of {MAAMA} at night: a long wooden dining table laid with home-cooked Maldivian dishes (fish curry, rice, roshi, mas huni, a bowl of fruit, glasses of water), wooden chairs, a cream wall with framed blurred landscape pictures, a pendant lamp over the table",
    "maama_lounge": f"the cosy family lounge of {MAAMA} at night: a wide soft maroon sofa with embroidered cushions, a low wooden coffee table with a plate of short-eats and teacups, a standing lamp, carved wooden cabinets, an arched doorway to the hall",
}
MOOD = {
    "asil_living": "late afternoon, warm golden sunlight slanting through the sheer curtains of the balcony door, clear tropical weather, soft shy playful warmth",
    "asil_room": "late afternoon, blinds half-drawn, the room in cool dim blue with the colourful flicker of the game screen glow on faces and warm stripes of sunlight on the wall, clear weather, teasing teenage mischief",
    "asil_door": "late afternoon turning to early evening, clear weather, warm golden light inside the apartment, soft white corridor light, a shy lingering farewell",
    "maama_porch": "early night, clear warm tropical night with a dark indigo sky, warm amber veranda lamps and lamp light spilling from the open door, gentle anticipation and family warmth",
    "maama_dining": "night, clear weather, warm amber pendant lamp light over the table, deep soft shadows in the corners, family warmth tinged with quiet worry",
    "maama_lounge": "late night, clear weather, warm amber standing-lamp glow, a moonlit indigo window, tender bittersweet stillness",
}

LAIL = "Lail in his light-grey t-shirt and dark jeans"
SABA = "Saba in her loose long-sleeved powder-blue dress and white hijab fully covering her hair and neck"
HAIZUM_HOME = "Haizum at home in a casual short-sleeved light-beige shirt and dark trousers instead of his suit"

BEATS = [
    # ---------------- Asil's apartment: the study session ----------------
    dict(to=3, reason="episode opening: Saba and Lail at the study table; she catches his foot under the table and he hides a shy smile", chars=["saba_young", "lail_young"], loc="asil_living",
         visual=f"two teenagers of 17 sitting on opposite sides of the corner of the dining table, an arm's length apart, books open between them: {SABA}, glancing down towards the floor beside the table with raised eyebrows and a suppressed amused smile, pen in hand; {LAIL}, his elbow on the table, biting lightly on his knuckle, looking down, blushing with a sheepish shy smile; nobody touches, their feet are not visible under the tabletop",
         camera="medium two-shot, eye level, the faces in the upper half, the table top with books and pencils as a calm lower third", amb="home_day",
         sens="intimacy", safe="the under-table foot contact is never shown: only Saba's amused downward glance and Lail's blushing face, the two seated an arm's length apart"),
    dict(to=7, reason="action change: Saba looks up and questions him about kicking at Asil; Lail shrugs innocently", chars=["saba_young", "lail_young"], loc="asil_living",
         visual=f"{SABA} lifting her head from her exercise book and looking straight at Lail across the table with a playful questioning frown, one hand open in a 'why?' gesture; {LAIL} sitting back in his chair raising both shoulders in an innocent shrug, eyebrows lifted, trying not to smile; textbooks and an open exercise book with only soft illegible scribble lines between them",
         camera="medium shot over Saba's shoulder side, eye level", amb="home_day"),
    dict(to=11, reason="action change: Lail's phone rings, he calls his mother while Saba watches him closely", chars=["lail_young", "saba_young"], loc="asil_living",
         visual=f"{LAIL} sitting at the table holding his phone to his ear, a slightly flustered face as if he just remembered something; across the table {SABA} has put down her pen, chin resting on her hand, watching him closely with curious eyes; the phone screen not visible",
         camera="medium two-shot, eye level, Lail in the foreground, Saba in soft focus behind", amb="home_day"),
    dict(to=15, reason="action change: Saba teases him about needing a driver; Lail earnestly explains his parents' rules", chars=["lail_young", "saba_young"], loc="asil_living",
         visual=f"{LAIL} leaning forward on the table, phone lying face down beside his book, explaining earnestly with an open hand, a slightly embarrassed half smile; {SABA} listening across the table with a teasing sideways smile and an amused tilt of the head",
         camera="medium shot, eye level, slightly favouring Lail", amb="home_day"),
    dict(to=19, reason="emotional turn: 'you are a silver spoon' — Saba's playful teasing, Lail's quiet smile", chars=["saba_young", "lail_young"], loc="asil_living",
         visual=f"the two teenagers facing each other from OPPOSITE sides of the wide dining table, the whole width of the table and its books between them, a clear gap of more than an arm's length: on the left side {SABA} laughing softly, pointing her pencil playfully across the table towards Lail, her large eyes sparkling with mischief; on the right side, across the table, {LAIL} looking down at his book with a quiet bashful smile, not answering; warm golden light on both faces",
         camera="medium two-shot in profile across the table, eye level, faces in the upper half, the table top as the lower third", amb="home_day"),
    dict(to=22, reason="action change: Lail borrows a notebook and writes something, then tears out the page", chars=["lail_young", "saba_young"], loc="asil_living",
         visual=f"{LAIL} bent over a small spiral notebook, writing with a pen, shielding the page with his other hand, a thoughtful dreamy look; beside him at an arm's length {SABA} writing in her own exercise book, head down; the notebook pages show only soft illegible grey lines, no readable letters",
         camera="medium shot from slightly above, the table and notebooks as the lower third", amb="home_day"),
    # ---------------- Asil's room: the friends ----------------
    dict(to=26, reason="location and character change: Lail opens Asil's door; Asil and Sadhee lost in a video game", chars=["lail_young", "asil_young", "sadhee_young"], loc="asil_room",
         visual=f"{LAIL} standing in the bedroom doorway with a knowing smirk, looking down at the two gamers; young Asil in his maroon t-shirt and grey track trousers sinking into one bean bag with a game controller, eyes wide and guilty; young Sadhee in her rust-orange dress and cream hijab fully covering her hair and neck on a second bean bag well apart from him, biting her lower lip, fumbling with her controller; the TV is turned away from the viewer, only its colourful glow on their faces",
         camera="medium wide from inside the room towards the doorway, eye level, the rug as a calm lower third", amb="room_day"),
    dict(to=29, reason="action change: Lail folds his arms and threatens to tell Shahid; the two shout 'Shut up Lail!'", chars=["lail_young", "asil_young", "sadhee_young"], loc="asil_room",
         visual=f"{LAIL} standing with his arms folded and a teasing raised eyebrow; young Asil and young Sadhee on their separate bean bags an arm's length apart, both leaning towards him at once with open mouths and pointing fingers, laughing protest on their faces, controllers in their laps",
         camera="medium wide, eye level, slightly low from the bean bags", amb="room_day"),
    dict(to=32, reason="action change: Asil gets up from the bean bag and gives away Lail's crush on Saba", chars=["asil_young", "lail_young", "sadhee_young"], loc="asil_room",
         visual=f"young Asil standing up from his bean bag, grinning broadly and gesturing towards the door to the sitting room with his thumb, teasing; {LAIL} facing him a step away, hands raised palms out in a 'please stop' gesture, blushing, shaking his head; young Sadhee still sitting on her bean bag looking up at Lail with delighted surprise, a hand over her smiling mouth",
         camera="medium shot, eye level", amb="room_day"),
    dict(to=35, reason="action change: Sadhee stands and steps between the two boys, speaking gently", chars=["sadhee_young", "lail_young", "asil_young"], loc="asil_room",
         visual=f"young Sadhee in her rust-orange dress and cream hijab now standing between the two boys with a kind reassuring smile, one hand raised calmly towards Asil as if to settle him; {LAIL} on one side looking down shyly, Asil on the other side with his hands in his pockets; everyone an arm's length apart",
         camera="medium three-shot, eye level", amb="room_day"),
    dict(to=38, reason="emotional turn: Lail pleads with Sadhee and cannot say whether he truly loves Saba", chars=["lail_young", "sadhee_young"], loc="asil_room",
         visual=f"close shot of {LAIL} lifting both hands with a helpless shrug, his face uncertain and vulnerable, eyes searching; young Sadhee a step away in soft focus, looking intently at his face with a gentle questioning look",
         camera="close-up on Lail, eye level, Sadhee's shoulder and cream hijab blurred in the foreground", amb="room_day"),
    dict(to=42, reason="action change: the driver calls; Lail hurries out through the sitting room saying bye to Saba", chars=["lail_young", "saba_young"], loc="asil_living",
         visual=f"{LAIL} walking quickly across the sitting room towards the front door, phone in hand, glancing back over his shoulder with a shy smile; {SABA} still at the dining table with her books, looking up at him and saying goodbye, several steps away",
         camera="medium wide, eye level, the tiled floor as the lower third", amb="home_day"),
    dict(to=44, reason="location change: at the open door he looks back; she waves from the table; he calls the lift", chars=["lail_young", "saba_young"], loc="asil_door",
         visual=f"view from beside the dining table towards the open front door: in the background {LAIL} stands in the bright corridor beside the closed lift doors, turned back towards the apartment with a soft shy smile; in the foreground, seen from the side, {SABA} sits at the table smiling gently and raising one hand in a small wave; a long distance between them",
         camera="deep two-plane composition, Saba in the near foreground, Lail far back in the doorway, eye level", amb="home_day"),
    # ---------------- Saba discovers the poem ----------------
    dict(to=46, reason="action change: alone, Saba grabs the notebook Lail used and flips through the pages", chars=["saba_young"], loc="asil_living",
         visual=f"{SABA} alone at the dining table, leaning over the small spiral notebook, flipping its pages quickly with a curious, slightly guilty excited face, glancing once towards the front door; the pages blank except for faint pressed indentations",
         camera="medium close-up from slightly above, the notebook on the table as the lower third", amb="home_day"),
    dict(to=49, reason="emotional turning point: she shades the page with a pencil and the hidden poem appears", chars=["saba_young"], loc="asil_living",
         visual=f"close-up of {SABA} gently rubbing the side of a pencil lead across the notebook page; pale wavy lines of an illegible handwritten verse appearing in white out of the grey graphite shading (soft abstract strokes, no readable letters); her face above lit by golden light, lips parted in a whispering read, eyes softening with a dawning tender smile",
         camera="close-up, her face in the upper half, her hand and the shaded page in the lower half", amb="home_day",
         sens="other", safe="the poem is shown only as illegible white strokes in graphite shading, no readable text"),
    dict(to=52, reason="character enters: Sadhee comes out and sits by Saba, who has hidden the notebook", chars=["sadhee_young", "saba_young"], loc="asil_living",
         visual=f"young Sadhee sitting down next to {SABA} at the dining table, leaning in with a curious teasing smile; Saba bent over her exercise book pretending to study with a composed innocent face, the small notebook closed and half hidden under her textbook",
         camera="medium two-shot, eye level", amb="home_day"),
    # ---------------- Night at Maama Shafeeqa's house ----------------
    dict(to=55, reason="scene and time change: night at Maama Shafeeqa's house; she watches the door, Haizum waits on the swing", chars=["shafeeqa", "haizum"], loc="maama_porch",
         visual=f"Maama Shafeeqa standing in the lamp-lit veranda near the open carved main door, hands clasped, gazing expectantly towards the gate, glancing at the big round wall clock inside the hall (plain face, no numerals); behind her {HAIZUM_HOME} sitting in the round rattan hanging swing chair with a phone in his hand, looking up at his mother; the phone screen not visible",
         camera="medium wide, eye level, the tiled veranda floor as the lower third", amb="home_night", transition="black"),
    dict(to=57, reason="characters enter: Lail and his sister Laira arrive, laughing together", chars=["lail_young", "laira"], loc="maama_porch",
         visual=f"{LAIL} walking in through the open gate onto the veranda beside his elder sister Laira, gesturing animatedly with both hands as he tells her a funny story, his face fresh and happy; Laira in her dusty-pink dress and dove-grey hijab fully covering her hair and neck, laughing with delighted interest",
         camera="medium shot, eye level, warm lamp light", amb="home_night"),
    dict(to=61, reason="action change: the grandchildren run to Maama and hold her from both sides", chars=["shafeeqa", "lail_young", "laira"], loc="maama_porch",
         visual=f"Maama Shafeeqa beaming with joy, her arms around the shoulders of her two grandchildren pressed close at either side of her, {LAIL} on one side grinning and Laira on the other side smiling with her cheek against her grandmother's white headscarf; a warm happy family reunion",
         camera="medium shot, eye level, faces in the upper half", amb="home_night",
         sens="other", safe="grandmother and grandchildren (family): a modest affectionate family greeting, everyone fully clothed"),
    dict(to=64, reason="character focus change: Haizum rises from the swing and draws his children close", chars=["haizum", "laira", "lail_young"], loc="maama_porch",
         visual=f"{HAIZUM_HOME} standing on the veranda with one arm around his daughter Laira's shoulders, his eyes closed in tenderness, his cheek resting against the top of her dove-grey hijab, and his other hand on the shoulder of his son {LAIL}, drawing him close; the round swing chair still gently moving behind them",
         camera="medium shot, eye level", amb="home_night",
         sens="other", safe="father with his own children (family): a modest affectionate greeting, no other contact"),
    dict(to=67, reason="action change: Laira steps back and tells them their mother is ill; Lail frowns at her", chars=["laira", "haizum", "lail_young"], loc="maama_porch",
         visual=f"Laira having stepped back a little from her father, speaking softly with a worried face; {HAIZUM_HOME} looking at her with sudden concern; {LAIL} beside them frowning at his sister with knitted brows, puzzled and hurt that he did not know",
         camera="medium three-shot, eye level", amb="home_night"),
    dict(to=70, reason="emotional turning point: Haizum cannot hide his anxiety and steps away", chars=["haizum", "shafeeqa"], loc="maama_porch",
         visual=f"{HAIZUM_HOME} standing a little apart near the swing chair, his face troubled and anxious, jaw tight, staring at the floor; in the background Maama Shafeeqa watching her son with knowing, sorrowful eyes",
         camera="medium close-up on Haizum, Shafeeqa soft in the background, eye level", amb="home_night"),
    dict(to=73, reason="action change: Maama leads the children to the dining room, Haizum follows", chars=["shafeeqa", "laira", "lail_young", "haizum"], loc="maama_porch",
         visual=f"Maama Shafeeqa walking through the open carved door into the lamp-lit hall, holding Laira's hand, {LAIL} just behind them; {HAIZUM_HOME} following a few steps behind, slower, head slightly bowed; seen from behind and the side",
         camera="medium wide from the veranda, eye level", amb="home_night"),
    dict(to=76, reason="location change: dinner — Maama jokes with the children, Haizum sits silent", chars=["haizum", "shafeeqa", "laira", "lail_young"], loc="maama_dining",
         visual=f"the family around the dining table: Maama Shafeeqa at the head laughing and serving food to {LAIL} and Laira, who laugh with her; Haizum sitting at the side wearing a casual short-sleeved light-beige shirt (NOT a suit, no jacket), his plate untouched, gazing into the distance, lost in silent worried thought; clear night outside the window, no rain",
         camera="medium wide, eye level, the table top with dishes as the lower third", amb="home_night"),
    dict(to=80, reason="action change: Maama asks about the client meeting; Laira teases her father", chars=["laira", "haizum", "shafeeqa"], loc="maama_dining",
         visual=f"Laira at the table looking at her father with an affectionate mock-pouting face, one hand raised in a playful complaint; {HAIZUM_HOME} turning towards her with a gentle apologetic smile, hand on his chest; Maama Shafeeqa watching them fondly",
         camera="medium shot across the table, eye level", amb="home_night"),
    dict(to=83, reason="action change: the children agree he can go; Maama pats Lail's back; Haizum rises", chars=["lail_young", "laira", "shafeeqa"], loc="maama_dining",
         visual=f"{LAIL} eating with a contented easy smile, nodding; Laira beside him looking at him with a pleased smile; Maama Shafeeqa leaning over affectionately patting Lail's back, beaming with pride; an empty chair pushed back where Haizum sat",
         camera="medium shot, eye level, dishes as the lower third", amb="home_night"),
    dict(to=85, reason="location and action change: Haizum, changed into his suit, watches the children sitting with Maama", chars=["shafeeqa", "laira", "lail_young", "haizum"], loc="maama_lounge",
         visual="Maama Shafeeqa sitting in the middle of the wide maroon sofa telling a story with animated hands, her two grandchildren — young Lail in his light-grey t-shirt and Laira in her dusty-pink dress and dove-grey hijab — sitting close on either side of her, listening eagerly like small children; in the arched doorway Haizum, now in his dark-navy suit and white open-collar shirt, stands watching them with a soft tender smile",
         camera="wide shot, eye level, the sofa group in the middle, Haizum at the side in the doorway, the rug as the lower third", amb="living_night"),
    dict(to=87, reason="reflective emotional peak: close on Haizum — his children are his whole world, lost by his one mistake", chars=["haizum"], loc="maama_lounge",
         visual="close-up of Haizum in his dark-navy suit and white open-collar shirt, leaning against the arched doorframe, his tired dark eyes glistening with unshed tears, a faint sad smile, the warm lamp-lit blur of the family on the sofa behind him",
         camera="close-up, eye level, his face in the upper half", amb="living_night"),
    dict(to=89, reason="return to the earlier image: his reflection on Sana and the children continues over the family scene", reuse="beat_027", loc="maama_lounge",
         chars=["shafeeqa", "laira", "lail_young", "haizum"],
         visual="reuse of beat_027: Maama with the two grandchildren on the sofa, Haizum watching from the doorway",
         camera="wide shot, slow pull-out", amb="living_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Lail! I am still in my conscious.\" Saying this, Saba looked down at Lail's foot.")
sh(2, "Lail nodded, rested his elbow on the table and slowly bit on his knuckle.")
sh(3, "Even then a shy little smile showed on his lips. Saba too swallowed her laughter and turned back to her book.")
sh(4, "\"Then why did you hit Asil?\" Lail asked, still sitting the same way. \"Since you're a guest, I wouldn't dare hit Lail, right?")
sh(5, "That's why I hit Asil. But what I didn't get is why kick at the foot? Why were you trying to kick Asil's foot?\"")
sh(6, "Saba asked, raising her head and looking at Lail's face. Her tone carried her unfamiliarity with Dhivehi.")
sh(7, "Lail kept looking at Saba and shrugged both shoulders to show he didn't know. Saba smiled and carried on writing her lesson.")
sh(8, "\"If you need help, let me know,\" Lail said quietly. Saba nodded in agreement. Just then Lail's phone began to ring.",
   [("phone_buzz", "ރިންގުވާން", -18)])
sh(9, "He took the phone out of his jeans pocket and looked: it was his mother calling. His face changed as if he'd suddenly remembered something, and he answered.")
sh(10, "Saba sat watching his every move closely. \"Mum, send the driver to pick Lail up.")
sh(11, "Yes, and tell big sister to get ready to go to Maama's.\" Lail said this hurriedly and hung up. \"Send someone to pick you up?")
sh(12, "Can't you go on your own?\" Saba asked teasingly. \"No, it's not that I can't go.")
sh(13, "But my parents have a lot of rules. They're always worried I'll fall in with bad people and lose my way.")
sh(14, "They always say: play with a crow and you'll turn into a crow. Aseel and Shahid are my two close friends,")
sh(15, "so my parents trust those two a lot,\" Lail explained. \"Then who's coming to get you? Your dad?")
sh(16, "Or your big brother?\" Saba asked. \"The driver,\" Lail answered. \"Hmm, you're a silver spoon, aren't you?\"")
sh(17, "Saba asked teasingly. \"When Sadhee said that, I didn't believe it at first.")
sh(18, "It was because Lail gets along with everyone else. And rich kids act very arrogant.\" Saba's words made Lail smile.")
sh(19, "Still, he gave no reply and sat quietly. Saba didn't carry the conversation further either and turned her attention to her lesson.")
sh(20, "Lail picked up another book lying there, looked at it, then took the pen beside it and asked: \"Is this a notebook? Is it okay if I use it?\"",
   [("page_turn", "ފޮތެއް", -22)])
sh(21, "\"Yep,\" Saba answered, looking at her book. Once again Saba started writing.")
sh(22, "Lail too kept writing something in his book. After a while he tore the written page out of the book, folded it and put it in his pocket.",
   [("pen_scribble", "ލިޔަމުން", -22), ("paper_shuffle", "ވީދާލުމަށްފަހު", -20)])
sh(23, "Then he left the book and pen on the table, got up from the chair and walked towards Asil's room.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(24, "When he opened the door, Sadhee and Asil were lost in their game. Lail entered the room and looked hard at the TV screen and at the two of them.",
   [("door_open", "ހުޅުވާލިއިރު", -20), ("phone_game_taps", "ގޭމު", -24)])
sh(25, "\"What a low score! Sadhee, what kind of way is that to hold the joystick?\" Lail asked.")
sh(26, "At that, Sadhee bit her lip, and Asil's eyes went wide as if something had blown up. And Sadhee quickly fixed her grip on the joystick.")
sh(27, "\"I don't know what you two talked about or did. I don't even want to look. But I'm reporting this to Shahid,\" Lail said, folding his arms.")
sh(28, "\"Shut up Lail!\" Sadhee and Asil shouted together. \"So what are you two hiding?\" Lail asked eagerly.")
sh(29, "\"We gave you two a chance. Okay?\" Asil said quickly. \"A chance for what?\" Lail asked in surprise.")
sh(30, "\"To talk, to tell her how you feel. I know Lail likes her,\" Asil said, getting up from the bean bag. \"Asil, please!\"",
   [("cloth_rustle", "ތެދުވަމުން", -22)])
sh(31, "Lail said, shaking his head. \"Okay, I won't say any more. Does Sadhee know? He even got Saba's number from me!\"")
sh(32, "Asil calmly told Sadhee. Asil's words made Lail a little embarrassed. Just then Sadhee too got up from her bean bag.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(33, "\"So what if someone likes somebody, that's no problem! This is that kind of age, isn't it? Liking each other is how it turns into love.")
sh(34, "It's completely okay,\" Sadhee said gently, stepping in between Asil and Lail.")
sh(35, "\"Please Sadhee, don't say anything like that in front of Saba! I still don't know what she thinks of me.")
sh(36, "If she turned down my proposal, I'd be so embarrassed,\" Lail told Sadhee, letting out a deep breath. \"I won't tell.",
   [("sigh", "ނޭވާއެއް", -22)])
sh(37, "Asil won't say anything either. But do you really love Saba?\" Sadhee asked, looking deep into Lail's face.")
sh(38, "Lail didn't answer; he shrugged and raised both hands. In truth, even the state of his own heart wasn't clear to him at that moment.",
   hum=True)
sh(39, "As he was about to answer, Lail's phone began to ring. Taking it from his pocket, he saw it was the driver. \"Coming out now.\" Lail hung up.",
   [("phone_buzz", "ރިންގުވާން", -18)])
sh(40, "\"My ride is here and waiting. We'll talk later, I'm off.\" Afraid he'd have to face more questions from his friends,")
sh(41, "Lail hurried to get out of there. Crossing the sitting room on his way out, he told Saba he was leaving. \"Bye.\"",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -24)])
sh(42, "Saba said softly. \"Bye,\" Lail said, putting on his shoes. Then he opened the door, stepped out, and turned back to look.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -20)])
sh(43, "Saba was sitting looking his way. A faint smile came to Lail's lips. Saba too smiled and waved. \"I'm going, okay.\"")
sh(44, "Lail said softly. \"Take care,\" Saba said. Lail walked on and pressed the button to bring the lift up.",
   [("lift_ding", "ލިފްޓު", -20)])
sh(45, "As soon as she was sure Lail had gone, Saba quickly picked up the notebook Lail had used, and leafed through its pages.",
   [("page_turn", "އެއްލަމުން", -20)])
sh(46, "No writing could be seen. Flipping the pages one by one again, she noticed on the next page the marks pressed in by the pen.",
   [("page_turn", "އުކަމުން", -22)])
sh(47, "Saba took a pencil and slowly began rubbing it over those marks. With that,",
   [("pen_scribble", "ކާއްތަން", -20)])
sh(48, "the letters of the verse Lail had written began to show clearly. \"Pausing to gaze at the invitation your eyes offer mine...",
   hum=True)
sh(49, "...what slipped onto my tongue, trembling, fled in deepest secret...\" Saba whispered the words as they slowly appeared. Just then Sadhee came out of the room.",
   hum=True)
sh(50, "Saba quickly shut the book and started on her lesson. Sadhee came and sat down beside her. \"Done playing the game?\"",
   [("paper_shuffle", "ލައްޕައިލުމަށްފަހު", -22)])
sh(51, "Saba asked, her eyes fixed on her book. \"Yes. What did you and Lail talk about?\" Sadhee asked eagerly.")
sh(52, "\"Do we need to talk?\" Saba asked back. Seeing Saba lost in her lesson, Sadhee also stopped talking and went quiet.")
sh(53, "Shafeeqa's eyes were fixed on the main door of the house. Every time she took her eyes off the door, she looked at the big clock on the wall.",
   [("clock_tick", "ގަޑިއަށް", -22)])
sh(54, "Haizum, sitting in the round swing on the open veranda playing with his phone, glanced every now and then at what his mother was doing.",
   [("creak", "އުނދޯލީގައި", -24)])
sh(55, "Shafeeqa was waiting for the moment Haizum's two children would arrive. Her wait ended with the sound of the door opening.",
   [("door_open", "ހުޅުވުނު", -18)])
sh(56, "Lail came in chatting with his big sister Laira about something funny, telling the story with his hands.")
sh(57, "Lail's face looked fresh and happy, a light smile on his lips. How interested Laira was in her little brother's story was clear from her smiling face.")
sh(58, "Seeing the two children's happy faces, a joyful smile spread over Shafeeqa's face too. \"Here come Maama's darling two kids,\" Shafeeqa said happily.")
sh(59, "\"Maama!\" The two ran to her and held their grandmother from both sides. \"Come inside, quickly.",
   [("footsteps_pavement", "ދުވެފައި", -22), ("cloth_rustle", "ބައްދައިގަތެވެ", -22)])
sh(60, "Maama has made the food you love most,\" Shafeeqa said lovingly. \"Maama, you're the best!\"")
sh(61, "Lail said, holding his grandmother again. \"If I'm that good, you should come and see Maama! You act as if you can't find your way to this house.\"")
sh(62, "Shafeeqa took Lail's hand and gave him an affectionate scolding. Haizum too got up from the swing and came towards the children.",
   [("creak", "އުނދޯލިން", -22)])
sh(63, "Laira went straight to her father and held him. Haizum drew Laira close and lovingly kissed the top of her head.",
   hum=True)
sh(64, "Then, stretching out his other arm, he drew Lail close too and kissed his head as well. \"Where's your mum?\" Haizum asked. \"At home.")
sh(65, "Mum's a bit unwell,\" Laira said, stepping back a little from her father. \"What happened? Has she got a fever?\"")
sh(66, "Worry crept into Haizum's voice. \"Yes, and she threw up late last night,\" Laira said.")
sh(67, "Lail immediately frowned and looked at Laira. \"Why didn't I know?\" he asked in a hurt tone. \"You were fast asleep, weren't you?")
sh(68, "And Mum didn't want to wake you at that hour,\" Laira said, explaining to her brother. \"Has she been to the doctor?\"")
sh(69, "Worry showed in Shafeeqa's voice too. In reply, Laira shook her head.")
sh(70, "At that moment Haizum couldn't hide the anxiety and unease on his face. Silently he stepped a little away from the children.",
   hum=True)
sh(71, "It wasn't hard for Shafeeqa to sense how deeply her son was affected. Letting out a deep sigh of sorrow, Shafeeqa began talking to the children.",
   [("sigh", "އާހެއް", -22)])
sh(72, "\"Come on, let's go and eat quickly, it's getting late,\" Shafeeqa said lovingly, taking Laira's hand.")
sh(73, "Laira and Lail walked behind their grandmother towards the dining room. And Haizum too followed them.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(74, "He didn't want to spoil the joy of this happy moment with his children, whom he was seeing after so many days.")
sh(75, "Even so, he couldn't control the ache that rose in his heart on hearing that Sana was ill.",
   hum=True)
sh(76, "Even as Shafeeqa joked and chatted with the children at the dining table, Haizum sat silent, sunk deep in thought.",
   [("cup_clatter", "ކާމޭޒުދޮށުގައި", -24)])
sh(77, "Shafeeqa could feel very well the storm going on in her son's mind. \"Didn't you say you had a meeting with a client tonight?")
sh(78, "What time is that meeting?\" Shafeeqa asked, breaking the silence. \"You brought us to this house when you have a meeting, Dad?\"")
sh(79, "Laira asked with an affectionate complaint. \"That's no problem, my dear. Dad will cancel that meeting,\" Haizum said, putting the children first. \"No,")
sh(80, "you can't do that. Will the meeting finish soon?\" Laira asked. \"Hmm... it might run a little late,\" Haizum said.")
sh(81, "\"If it ends before twelve, Dad, go and come back. We can wait till twelve, right, little brother?\" Laira said, looking at Lail sitting beside her.")
sh(82, "\"Fine by me. I don't have to go to school tomorrow,\" Lail said, carrying on eating. \"Maama's obedient darling!\"")
sh(83, "Shafeeqa said, lovingly patting Lail's back. With the children's consent, Haizum got up from the table, went and changed his clothes, and came out.",
   [("cloth_rustle", "ބަދަލުކޮށްލައިގެން", -24)])
sh(84, "By then Laira and Lail were sitting on either side of their grandmother, listening eagerly to her stories.")
sh(85, "Seeing that scene, it seemed they were still little five-year-olds. A faint smile came to Haizum's lips as he stood watching that innocent scene.")
sh(86, "Those two children were his whole world. Yet fate had taken them away from him. In his whole life he had made only one mistake.",
   hum=True)
sh(87, "But the punishment for that mistake was the pain of being separated from his beloved children. Even this chance to talk to them and see them had come only through great effort.",
   hum=True)
sh(88, "Though he belonged to an honoured, respected and wealthy family, he knew that using his own power and influence to take the children was not something he could do.")
sh(89, "A mother's love and the worth of her tears are far higher than that. To wound Sana's heart further and watch tears flow from her eyes was something Haizum's conscience would not allow. It would be a pain to his own heart too.",
   hum=True)
SHOTS = S

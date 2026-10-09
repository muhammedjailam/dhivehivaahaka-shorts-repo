"""Beat/shot plan for Nindheveethimeymathee episode 296 (used by plan_beats.py).
SCHOOL timeline (A-level years, Lail/Saba/Asil/Sadhee at 17). One afternoon at Asil's family apartment in Male':
homework help, gaming, whipped coffee, Lail's under-table kick hits Saba's foot, the ice pack, Asil and Sadhee spying.
Rules: hijab on every girl; NO touching between Lail and Saba (no foot on his lap -> foot on a cushion on a low stool,
Lail a step away); no readable text on phones/notebooks/game screen; the kick and the smack are never shown."""

APT = "the bright modern ninth-floor family apartment of Asil's family in Male', Maldives"
LOC = {
    "door": f"the entrance of {APT}: an open plain wooden front door, a low wooden shoe cabinet beside it with a few pairs of sandals, a tiled floor, a glimpse of the bright sitting room behind",
    "sitting": f"the open sitting room of {APT}: a grey sofa with cushions, a dining table at one side heaped messily with open schoolbooks, exercise books and pens, wooden dining chairs, sheer white curtains at a wide window with the sunny Male' skyline and a strip of blue lagoon beyond, potted plant, tiled floor",
    "asil_room": f"Asil's teenage bedroom in {APT}: two big soft beanbags on a rug in front of a low TV cabinet with a games console, a flat TV screen showing only blurred abstract coloured light, a study desk with a lamp and a stack of blank A4 paper, posters with only abstract shapes, a window with sunlight, a wooden door",
    "kitchen": f"the bright family kitchen of {APT}: white cabinets, a counter with a tall jug, glass mugs and a tin of coffee, a fridge, a window with afternoon sunlight",
    "dining": f"the dining table in the sitting room of {APT}: a wooden table heaped with open schoolbooks and exercise books showing only soft illegible lines, glass mugs of whipped iced coffee, a glass of water, wooden chairs, sheer curtains and the sunny Male' skyline behind",
    "classroom": "an A-level classroom in a Male' secondary school: rows of wooden desks, a whiteboard with only faint smudged marks, tall windows with louvres and bright tropical sunlight, students in white school uniforms",
    "door_gap": f"the doorway of Asil's bedroom in {APT}, the wooden door held open a narrow gap, the bright sitting room visible beyond it",
}
MOOD = {
    "door": "bright tropical afternoon, warm sunlight spilling through the apartment, shy warmth, sunny clear weather",
    "sitting": "bright sunny afternoon, warm golden light through sheer curtains, quiet curiosity and a shy crush, clear weather outside",
    "asil_room": "sunny afternoon, warm daylight from the window mixed with the soft coloured glow of the game screen, playful teenage energy and shy tension",
    "kitchen": "bright sunny afternoon, warm light on white cabinets, cheerful and lively",
    "dining": "sunny afternoon, warm golden window light over the table, teasing banter turning tense and tender, clear weather outside",
    "classroom": "soft hazy dreamlike memory glow, bright tropical late-morning sunlight through louvred windows, shy longing",
    "door_gap": "sunny afternoon, warm light from the sitting room falling through the door gap into the shaded bedroom, mischievous curiosity",
}

LAIL = "Lail in his light-grey t-shirt and dark jeans"
SABA = "Saba in her loose long-sleeved ankle-length powder-blue dress and white hijab fully covering her hair and neck"
SADHEE = "Sadhee in her loose long-sleeved rust-orange dress and cream hijab fully covering her hair and neck"
ASIL = "Asil in his maroon t-shirt and grey track trousers"

BEATS = [
    dict(to=2, reason="episode opening: Saba opens the door to Lail at Asil's apartment", chars=["saba_young", "lail_young"], loc="door",
         visual=f"{SABA} standing just inside the open front door with a small polite smile, gesturing towards the inside of the apartment; a few steps away on the threshold {LAIL} smiles faintly back, bending to slip off his sneakers; the two at a clear distance from each other, both teenagers about 17",
         camera="medium wide, eye level from inside the apartment, faces in the upper half, the tiled floor as the calm lower third", amb="home_day"),
    dict(to=5, reason="action change: Lail notices the dining table heaped with books where Saba sits down to study", chars=["lail_young", "saba_young"], loc="sitting",
         visual=f"{LAIL} in the foreground, seen from behind his shoulder, pausing in the sitting room and looking across at the dining table heaped messily with open books; at the table {SABA} has just sat down, one foot pulled up onto her chair under her long dress, writing in an exercise book with a pen, absorbed; the pages show only soft illegible lines",
         camera="over-the-shoulder medium wide, the dining table and Saba in the upper half, the tiled floor as the calm lower third", amb="home_day"),
    dict(to=8, reason="scene change: Asil's bedroom, fist bump and gaming on beanbags", chars=["asil_young", "lail_young"], loc="asil_room",
         visual=f"two teenage best friends: {ASIL} sitting in a beanbag holding a game controller, grinning and holding out his fist; {LAIL} dropping into the beanbag next to him and bumping his fist, a second controller in his other hand; the TV in front of them shows only blurred colourful abstract light, no text",
         camera="medium shot from beside the TV, both faces lit by the screen glow in the upper half, the rug as the calm lower third", amb="room_day"),
    dict(to=11, reason="character enters: Saba comes in with her exercise book and a question", chars=["saba_young", "asil_young", "lail_young"], loc="asil_room",
         visual=f"{SABA} standing in the bedroom doorway clicking a pen in one hand, her eyes on the open exercise book in the other hand, a puzzled frown; {ASIL} on his beanbag with the controller lowered, leaning to look at her book; {LAIL} on the other beanbag glancing up at her; the TV glows softly with abstract blurred light",
         camera="medium wide from behind the beanbags towards the doorway, faces in the upper two-thirds", amb="room_day"),
    dict(to=15, reason="action change: Lail takes the book, asks for a pen and paper; Saba brings A4 paper", chars=["lail_young", "saba_young", "asil_young"], loc="asil_room",
         visual=f"{LAIL} sitting on the beanbag with her open exercise book on his knee and a pen in his hand, his controller put aside; {SABA} standing a careful arm's length away holding out a single blank sheet of A4 paper towards him by its far corner, their hands not touching; {ASIL} on the next beanbag watching with interest; pages show only soft illegible lines",
         camera="medium shot, eye level, faces in the upper half, the rug as the calm lower third", amb="room_day"),
    dict(to=17, reason="action change: Saba kneels nearby while Lail explains the problem", chars=["lail_young", "saba_young", "asil_young"], loc="asil_room",
         visual=f"{LAIL} on the beanbag writing on the A4 sheet resting on the book, explaining with the pen; {SABA} kneeling on the rug a clear arm's length away, leaning to look at the paper, attentive; behind them {ASIL} lounges on his beanbag watching the two of them with a knowing interested smile; the paper shows only soft illegible lines and simple shapes",
         camera="medium shot, slightly high angle, faces in the upper two-thirds", amb="room_day"),
    dict(to=20, reason="emotional turning point: their eyes meet and lock in silence", chars=["lail_young", "saba_young"], loc="asil_room",
         visual=f"{LAIL} sitting on the beanbag with the book on his knee and {SABA} kneeling on the rug a full arm's length away from him, a clear gap of empty rug between them, both turned and looking straight into each other's eyes for a frozen silent moment, his lips slightly parted, her large dark eyes wide and shy, a faint blush on both faces; the paper lowered on the book",
         camera="medium two-shot in profile at their seated eye level, faces in the upper half, soft bokeh of the room behind", amb="room_day"),
    dict(to=23, reason="action change: Saba leaves the room; Lail gazes after her; Asil grins at Lail", chars=["lail_young", "asil_young", "saba_young"], loc="asil_room",
         visual=f"in the background {SABA} at the bedroom door holding her book and pen, quietly pulling the door closed behind her as she leaves; in the foreground {LAIL} sitting on the beanbag with his forearms resting on his knees, gazing after her with a deep dreamy look; beside him {ASIL} turned towards Lail with a sly mischievous grin",
         camera="medium wide, eye level, the two boys in the foreground, the door in the upper background", amb="room_day"),
    dict(to=27, reason="action change: Asil demands Lail's phone and types something", chars=["asil_young", "lail_young"], loc="asil_room",
         visual=f"{ASIL} lounging back in his beanbag with his legs stretched out, holding Lail's phone and typing quickly with his thumbs, a sly grin; {LAIL} sitting up on the other beanbag watching him with a puzzled half-smile; the phone screen only a soft glow seen from the side, no text",
         camera="medium shot, eye level, faces in the upper half, the rug as the calm lower third", amb="room_day"),
    dict(to=29, reason="action change: Lail finds Saba's name saved in his phone", chars=["lail_young", "asil_young"], loc="asil_room",
         visual=f"close shot of {LAIL} holding his phone, its screen only a soft blank glow turned away from the viewer, his eyebrows raised in surprise, a shy smile tugging at his lips; out of focus beside him {ASIL} laughing mischievously",
         camera="close-up, slightly low angle, his face in the upper half", amb="room_day"),
    dict(to=31, reason="action change: Asil crosses his arms and teases; Lail protests, embarrassed", chars=["asil_young", "lail_young"], loc="asil_room",
         visual=f"{ASIL} sitting on his beanbag with his arms crossed over his chest, eyeing Lail with a teasing knowing look; {LAIL} on the other beanbag turned towards him, one palm raised in protest, laughing in embarrassment, his cheeks flushed",
         camera="medium two-shot, eye level, faces in the upper half", amb="room_day"),
    dict(to=33, reason="insert: what Asil describes, Lail turning round in class to look at Saba (illustrative memory)", chars=["lail_young", "saba_young"], loc="classroom",
         visual="a sunny classroom: young Lail, in a white short-sleeved school shirt and dark-navy long trousers, sitting at a wooden desk in a front row and turning round in his seat to glance back shyly; several rows behind him young Saba, in a white long-sleeved school tunic, navy ankle-length skirt and white hijab fully covering her hair and neck, bent over her notebook, unaware; other students in white uniforms softly blurred",
         camera="medium wide from the side of the classroom, faces in the upper two-thirds, desks as the calm lower third", amb="classroom",
         transition="dissolve", sens="other", safe="illustrative classroom glance only, the two far apart; no text on the whiteboard or notebooks"),
    dict(to=35, reason="return from the insert to the bedroom teasing", reuse="beat_011", chars=["asil_young", "lail_young"], loc="asil_room",
         visual="reuse of beat_011", amb="room_day", transition="dissolve"),
    dict(to=39, reason="action change: Asil laughs about Lail's excuses and his cousin; Lail just smiles", chars=["asil_young", "lail_young"], loc="asil_room",
         visual=f"{ASIL} leaning back in the beanbag laughing loudly, one hand on his belly, the other gesturing at Lail; {LAIL} sitting quietly beside him, the phone tucked in his jeans pocket, looking down at the rug with a small shy smile he can't hide",
         camera="medium wide, eye level, faces in the upper half, the rug as the calm lower third", amb="room_day"),
    dict(to=42, reason="scene change: the kitchen, Saba and Sadhee whipping coffee; the boys arrive", chars=["saba_young", "sadhee_young", "asil_young", "lail_young"], loc="kitchen",
         visual=f"{SABA} and {SADHEE} standing side by side at the kitchen counter laughing together, Sadhee whisking coffee in a tall jug with a spoon, foam rising; in the kitchen doorway {ASIL} leaning in curiously and {LAIL} just behind him, a polite smile",
         camera="medium wide, eye level, the girls in the upper half, the counter top as the calm lower third", amb="kitchen_busy"),
    dict(to=46, reason="action change: Asil gets mugs; Lail declines coffee; Asil pours him water", chars=["asil_young", "lail_young", "sadhee_young", "saba_young"], loc="kitchen",
         visual=f"{ASIL} at the counter pouring water from a jug into a tall glass for Lail, two empty glass mugs beside him; {LAIL} leaning against the fridge, raising a hand with a grin as if saying 'liar'; in the background {SADHEE} and {SABA} still whisking coffee in the jug",
         camera="medium shot, eye level, faces in the upper half", amb="kitchen_busy"),
    dict(to=50, reason="scene change: all four at the dining table with coffee; Sadhee annoyed about Shahid", chars=["sadhee_young", "saba_young", "asil_young", "lail_young"], loc="dining",
         visual=f"four teenage friends around the book-heaped dining table: {SADHEE} with her arms folded and an irritated pout, looking away; {SABA} beside her, frowning at Asil over her open exercise book; {ASIL} holding a glass mug of whipped coffee to his lips; {LAIL} across the table with his glass of water; the girls on one side, the boys on the other",
         camera="medium wide, slightly high angle, faces in the upper two-thirds, the table top as the calm lower third", amb="home_day"),
    dict(to=54, reason="action change: Asil tests Saba with the 'gave your number to a boy' tease; Lail shoots him a look", chars=["asil_young", "saba_young", "lail_young"], loc="dining",
         visual=f"{SABA} at the dining table, eyes still on her open exercise book, pen in hand, an indifferent careless expression; {ASIL} beside her leaning back with a sly mischievous smile; across the table {LAIL} glaring at Asil in alarm",
         camera="medium shot, eye level, faces in the upper half, the table top as the calm lower third", amb="home_day"),
    dict(to=56, reason="action change: the misdirected kick under the table; Saba yelps and glares at Asil", chars=["saba_young", "asil_young", "lail_young"], loc="dining",
         visual=f"{SABA} at the dining table jolting upright with a startled wince, her mouth open in an 'ouch', glaring furiously at {ASIL} beside her, who looks back bewildered; across the table {LAIL} frozen in guilty shock; the space under the table hidden in soft shadow",
         camera="medium shot, eye level, faces in the upper half, the table edge as the calm lower third", amb="home_day",
         sens="violence", safe="the kick itself is never shown; only the startled faces above the table"),
    dict(to=58, reason="action change: Saba stands and scolds Asil; Asil rubs his arm and pouts at Lail", chars=["saba_young", "asil_young", "lail_young"], loc="dining",
         visual=f"{SABA} standing at the table, angrily pointing a scolding finger at {ASIL}, who sits rubbing his own upper arm with an exaggerated pout, glancing sideways at Lail; {LAIL} across the table looking worried",
         camera="medium wide, eye level, faces in the upper two-thirds", amb="home_day",
         sens="violence", safe="Saba's smack on Asil's arm is not shown; she scolds with a pointed finger and he rubs his arm"),
    dict(to=62, reason="action change: Lail gulps his water; Sadhee shakes her head; Asil blames Lail", chars=["lail_young", "sadhee_young", "asil_young"], loc="dining",
         visual=f"{LAIL} nervously gulping down his whole glass of water in one go; {SADHEE} shaking her head at Asil in disappointment; {ASIL} pointing a thumb towards Lail with a pleading 'ask him' expression",
         camera="medium shot, eye level, faces in the upper half, the table top as the calm lower third", amb="home_day"),
    dict(to=65, reason="emotional turning point: Saba in real pain, eyes filling with tears", chars=["saba_young", "sadhee_young"], loc="dining",
         visual=f"close shot of {SABA} sitting at the table with one foot drawn up onto her chair under her long dress, both hands rubbing over her socked foot, her brows knitted in pain, forehead creased, large eyes brimming with tears that have not yet fallen; out of focus beside her {SADHEE} watching her with concern",
         camera="close-up, eye level, her face in the upper half", amb="home_day", sens="other",
         safe="pain shown only through her face and tears; no visible injury"),
    dict(to=67, reason="action change: Lail fetches an ice pack from the fridge; Asil signals Sadhee to move", chars=["lail_young", "asil_young", "sadhee_young"], loc="kitchen",
         visual=f"{LAIL} at the open fridge taking out a blue gel ice pack, a determined worried face lit by the fridge light; through the kitchen doorway in the background {ASIL} at the dining table making a small hand gesture to {SADHEE} to get up, she looking puzzled",
         camera="medium shot, eye level, faces in the upper half", amb="kitchen_busy"),
    dict(to=70, reason="action change: the ice pack on Saba's foot; Asil leads Sadhee away", chars=["saba_young", "lail_young", "asil_young", "sadhee_young"], loc="sitting",
         visual=f"{SABA} sitting on a dining chair with her socked foot raised on a soft cushion on a low wooden stool, a blue ice pack wrapped in a small towel resting on top of her foot; {LAIL} sitting on a chair a full step away from her, leaning forward with his hands on his own knees, looking at her foot with an apologetic worried face; Saba looking at his face through teary eyes; far in the background {ASIL} leading {SADHEE} towards a bedroom door; no touching",
         camera="medium wide, eye level, faces in the upper half, the tiled floor and stool as the calm lower third", amb="home_day",
         sens="intimacy", safe="narration: her foot on his lap while he holds the ice pack -> her foot on a cushion on a low stool with the ice pack resting on it, Lail a step away, no touching"),
    dict(to=72, reason="scene change: Asil peeks through the cracked bedroom door; Sadhee puzzled", chars=["asil_young", "sadhee_young"], loc="door_gap",
         visual=f"{ASIL} standing at the bedroom door holding it open a narrow gap, peeking out with one eye and a mischievous grin; {SADHEE} standing just inside the open doorway beside him, arms folded, frowning at him with an annoyed 'what are you doing' look; the door stays wide enough that both are clearly in view",
         camera="medium shot from inside the bedroom, faces in the upper half", amb="room_day"),
    dict(to=75, reason="action change: Asil lays out his theory; Sadhee settles on a beanbag, sceptical", chars=["sadhee_young", "asil_young"], loc="asil_room",
         visual=f"{SADHEE} sitting on a beanbag near the open bedroom door, one eyebrow raised sceptically; {ASIL} standing by the door, counting reasons on his fingers with a confident grin, then reaching for the door handle to peek again",
         camera="medium wide, eye level, faces in the upper two-thirds, the rug as the calm lower third", amb="room_day"),
    dict(to=77, reason="back to the sitting room: Lail still tending the ice pack, asks if it hurts less", reuse="beat_024", chars=["saba_young", "lail_young"], loc="sitting",
         visual="reuse of beat_024", amb="home_day"),
    dict(to=81, reason="action change: a tear falls; Saba wipes her eyes and smiles; Lail reassures her", chars=["saba_young", "lail_young"], loc="sitting",
         visual=f"{SABA} sitting with her foot still raised on the cushion on the low stool, wiping a tear from her cheek with her fingertips and giving a small embarrassed smile; {LAIL} sitting a step away on his chair, looking at her with a calm gentle reassuring face; no touching",
         camera="medium two-shot, eye level, faces in the upper half, the stool and floor as the calm lower third", amb="home_day"),
    dict(to=83, reason="emotional turning point: Lail confesses it was his kick, head bowed", chars=["lail_young", "saba_young"], loc="sitting",
         visual=f"{LAIL} sitting on a dining chair with his head bowed low like a guilty schoolboy, wincing; {SABA} sitting on another dining chair a full step away, her socked foot still raised on the cushion on the low wooden stool with the ice pack, staring at him with wide surprised eyes; a clear gap of empty floor between the two chairs",
         camera="medium shot, eye level, faces in the upper half", amb="home_day"),
    dict(to=86, reason="action change: Saba bursts out laughing; Asil and Sadhee peer from the doorway, baffled", chars=["saba_young", "lail_young", "asil_young", "sadhee_young"], loc="sitting",
         visual=f"{SABA} sitting on a dining chair, her socked foot still raised on the cushion on the low wooden stool, laughing hard, wiping tears of laughter from her eyes with both hands; {LAIL} sitting on another chair a full step away with his head still bowed, sheepish, a clear gap of empty floor between them; far in the background {ASIL} and {SADHEE} peering out of a half-open bedroom door, baffled",
         camera="medium wide, eye level, faces in the upper two-thirds, the floor as the calm lower third", amb="home_day"),
    dict(to=88, reason="emotional turning point: 'I know' — Lail looks up and smiles too", chars=["saba_young", "lail_young"], loc="sitting",
         visual=f"{SABA} sitting on a dining chair with her foot still resting on the cushion on the low stool, a soft knowing smile, looking at {LAIL}, who sits on another chair a full step away and has just lifted his head, surprised, a smile spreading across his face; a clear gap of empty space between them, warm golden window light",
         camera="medium two-shot, eye level, faces in the upper half, soft bokeh behind", amb="home_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Saying that Asil was in his room, she brought a smile to her lips. A faint smile came to Lail's lips too.")
sh(2, "He stepped forward, took off his shoes and came inside. At that very moment Saba bent down, picked up Lail's shoes,")
sh(3, "put them in the shoe cabinet to one side and quietly closed the door. Lail headed towards Asil's room.",
   [("door_close", "ލައްޕައިލިއެވެ", -20)])
sh(4, "Just then his gaze came to rest on the dining table at one side of the sitting room, because of the books scattered over it in no order.")
sh(5, "After locking the door, Saba went and sat down at that table. She pulled one foot up onto the chair, settled and began to write in her book.",
   [("lock_click", "ތަޅުލުމަށްފަހު", -20), ("pen_scribble", "ލިޔަން", -24)])
sh(6, "Lail watched Saba's movements as he went into Asil's room. \"Hey bro!\" Asil, who was playing a game, made a fist and held it out to Lail.")
sh(7, "Lail made a fist the same way and bumped Asil's hand in greeting, and settled into the beanbag next to the one Asil sat in.")
sh(8, "When Asil held out the second joystick, Lail took it and joined the game. The two friends played on with great excitement. At that moment,",
   [("phone_game_taps", "ޖޮއިސްޓިކް", -22)])
sh(9, "clicking a pen in one hand, her eyes fixed on the book in the other, Saba came into Asil's room. \"Asil,",
   [("door_open", "ވަދެގެން", -22)])
sh(10, "I still can't get this answer right,\" Saba said, looking at her book. \"Show me.\"")
sh(11, "Asil paused the game and took the book from Saba's hand. Lail looked at Saba too. \"Lail, a tough one.\"",
   [("page_turn", "ފޮތް", -24)])
sh(12, "Asil said, holding the book out. Lail put down the joystick he was playing with and took the book from Asil.")
sh(13, "When he held out his hand towards Saba, she looked at Lail's face. \"Pen,\" Lail said.")
sh(14, "\"Oh,\" Saba said, and gave Lail the pen. \"Isn't there some blank paper?\" Lail asked. Saba hurried over to Asil's study desk")
sh(15, "and took a sheet of A4 paper and held it out to Lail. Lail took the sheet from her and began to write as he explained the question.",
   [("paper_shuffle", "ކަރުދާސް", -22), ("pen_scribble", "ލިޔަން", -24)])
sh(16, "Saba, glancing over the book, knelt down near Lail. Asil sat watching the scene with great interest.")
sh(17, "\"Do you get it now?\" Lail asked, looking at Saba's face. \"Maybe... again, explain.\"")
sh(18, "Saba asked, looking at Lail's face. At that moment their eyes met. For a little while a silence fell over the room.",
   [("heartbeat", "ސީދާވިއެވެ", -22)], hum=True)
sh(19, "Neither of them knew whether to look down or to speak. \"Saba should take tuition from Lail. Lail would be really good.\"")
sh(20, "It was Asil who broke the silence. At Asil's voice Saba lowered her head. Lail fixed his eyes on the book too.")
sh(21, "Lail began explaining the question again. Saba kept listening. \"Thank you, I get it now,\" Saba said, taking the book and pen from Lail. Then")
sh(22, "she got up and walked out of the room. Lail sat with his arms resting on his knees, looking at Saba with a deep gaze.")
sh(23, "Just then Asil looked at Lail with a sly smile. Saba left the room and quietly closed the door behind her. \"What are you looking at?",
   [("door_close", "ލައްޕައިލިއެވެ", -20)])
sh(24, "Give me that phone,\" Asil said, stretching his legs out on the beanbag and lounging back comfortably. \"The phone? What for?\" Sitting as he was,")
sh(25, "Lail asked in surprise. \"Give it, I want to check something. I'm not going to log into your bank account and make a transfer,\" Asil said jokingly.")
sh(26, "\"Swear you mean it,\" Lail said with a light smile, and took the phone from his pocket and handed it to Asil.")
sh(27, "Taking the phone, Asil quickly typed something, and gave the phone back into Lail's hand.",
   [("phone_game_taps", "ޓައިޕްކޮށްލިއެވެ", -22)])
sh(28, "When Lail looked at the phone, what showed on the screen was Saba's name. \"What's this?\" Lail asked in surprise. \"Don't want it?")
sh(29, "Then give it here and I'll delete it,\" Asil said with a sly laugh. \"No, I want it,\" he said, a light smile coming to his lips.")
sh(30, "Asil folded his arms and kept watching Lail slyly. \"How sad, Asil! Every time I so much as look at a girl,")
sh(31, "why do you try to link that girl with me?\" Lail asked with an embarrassed smile. \"Just looked, you say? Who were you looking at?")
sh(32, "I never noticed anything like this before! But since Saba joined our class last week, the number of times you come to this house has gone up too.")
sh(33, "And turning round in class to look at Saba has become unusually frequent for you lately.")
sh(34, "Shahid noticed it too and brought it up last night.\" Asil said with a laugh. \"What nonsense!")
sh(35, "I always come to this house,\" Lail said, slipping the phone into his pocket. \"Is that so? I don't remember that.",
   [("cloth_rustle", "ކޮށްޕައިލަމުން", -24)])
sh(36, "Before, if I asked you to come and play games, your excuses outnumbered the grains of sand on the ground. But now, to play games, to teach me lessons,")
sh(37, "or to do lessons together, there's no shortage of excuses to come to this house. And sometimes you even come to eat the delicious food Mum cooks!\"")
sh(38, "Asil said jokingly. \"Hmm, anyway it's good for me too! My closest friend has now fallen for my little cousin, so what's the problem?\"")
sh(39, "Asil added, laughing and laughing. Instead of answering what Asil was saying, Lail just sat there smiling.")
sh(40, "The two of them left the room together on the excuse of getting something to drink. Saba was nowhere to be seen in the sitting room. But,")
sh(41, "along with the sound of something being whisked in the kitchen, Sadhee's and Saba's cheerful laughter could be heard. \"Sadhee's here too,\" Asil said, heading forward.",
   [("cup_clatter", "ގިރާ", -24)])
sh(42, "Lail followed behind. \"What are you whisking? Coffee?\" Asil asked. \"Sadhee. How are you?\" Lail called to Sadhee. \"OK.\"")
sh(43, "Sadhee said, whisking the coffee jug in her hand. Asil took two mugs, getting ready to whisk coffee. \"Asil, I don't feel like coffee right now.",
   [("cup_clatter", "ޖޯޑުނަގައި", -22)])
sh(44, "I just had coffee with my dad before coming,\" Lail said. \"Then how about a glass of juice?\" Asil asked. \"A glass of water is fine.\"")
sh(45, "Lail said. Sadhee and Saba were still whisking the coffee. \"When I try to make it, right, it's 'no problem, no problem' — Saba, make Lail a glass of juice.\"")
sh(46, "Asil said. \"Liar,\" Lail said quickly. Asil poured a glass of water and handed it to Lail.",
   [("pour", "އަޅައިފައި", -20)])
sh(47, "Saba and Sadhee came with their whipped coffee and sat at the table. Asil came too, holding his mug of coffee. \"Hassan's two legs all over the room.\"",
   [("cup_clatter", "ކޮފީތަށި", -22)])
sh(48, "Asil said, sitting down at the table. \"There is not enough space in my room,\" Saba shot back at Asil with a frown.")
sh(49, "\"Sadhee, still not forgiving Shahid?\" Asil said, touching the coffee mug to his lips. \"Did he ask for forgiveness?")
sh(50, "Even last night Vadhee and the others saw him sitting in a café with that girl. I don't want to talk to him,\" Sadhee said in a fed-up tone.")
sh(51, "\"Come on, calm down...\" Asil said. \"Saba,\" Asil said gently. \"Hmm,\" Saba only made a sound, without taking her eyes off her book.")
sh(52, "\"I gave your number to a boy, okay?\" Asil asked, to see what Saba thought about it.")
sh(53, "Just then Lail suddenly looked at Asil. Asil was sitting there with a sly smile. \"Who did you give it to? A handsome one?\"")
sh(54, "Saba asked in a careless tone, like a stranger. \"Yes, very handsome,\" Asil replied.")
sh(55, "Unable to stand the way Asil was talking, Lail kicked at Asil's foot under the table. \"Ouch!\" Suddenly lifting her foot and crying out in pain, Saba",
   [("soft_thud", "ޖަހައިލިއެވެ", -18), ("gasp", "އައްދޯއި", -18)])
sh(56, "rubbed her foot. And she glared angrily at Asil. \"Are you crazy, Asil? What did I do that you kicked me just now?")
sh(57, "We're not little kids who go around teasing each other any more, are we?\" Saba said, standing up and angrily hitting Asil's arm.",
   [("soft_thud", "ޖަހައިލަމުން", -22)])
sh(58, "Seeing this, Lail got worried. Asil, rubbing the spot where Saba had hit him and pouting, looked at Lail.")
sh(59, "Lail, flustered, picked up the glass of water beside him and drank it in one breath. Even a mouse squeak would have been loud. Then Saba sat back down on the chair,")
sh(60, "and with her foot lifted, began rubbing it gently. Sadhee too looked at Asil in disappointment and shook her head.",
   [("sigh", "ހޫރައިލިއެވެ", -22)])
sh(61, "\"Asil, when will you ever grow up?\" Sadhee said too. \"Hey, it wasn't me... ask Lail.\" Asil said, looking at Lail. \"I don't know.\"")
sh(62, "Lail said in a worried tone. \"Are you my best friend, or my enemy?\" Asil asked, looking at Lail. \"I could say the same to you.\"")
sh(63, "Lail said. Sadhee gave Saba a long look. Saba sat rubbing and rubbing her foot in pain.")
sh(64, "From the severity of the pain her brows drew together and her forehead was creased. And her eyes were close to brimming over with tears of pain.",
   [("sob_breath", "ކަރުނުން", -26)], hum=True)
sh(65, "In truth Saba had been hurt quite badly. Seeing Saba's watery eyes, Lail couldn't bear it.")
sh(66, "So he got up from the table and walked towards the kitchen. He opened the fridge, took an ice pack, and came and stopped beside Saba.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -24)])
sh(67, "With a gesture Asil asked Sadhee to get up from there. Though she didn't know what was going on, Sadhee obeyed Asil's signal, got up and went")
sh(68, "and sat in the chair Lail had been sitting in. With that, Lail sat in the chair Sadhee had left, took Saba's foot and rested it on his lap.",
   [("cloth_rustle", "އިށީނދެ", -24)])
sh(69, "Though she had been crying, Saba found herself looking at Lail's face. At that moment Lail was gently pressing the ice pack to Saba's foot.",
   hum=True)
sh(70, "As Asil, saying he had something to talk about, took Sadhee and left, a deep, complete silence fell over the whole sitting room.",
   [("footsteps_pavement", "ދިޔުމާއެކު", -26)])
sh(71, "Just then Asil opened the bedroom door a little and peeked out. \"What are you doing, Asil?\" Sadhee asked, annoyed.",
   [("creak", "ހުޅުވާލުމަށްފަހު", -22)])
sh(72, "\"I think Lail likes Saba,\" Asil said slyly. \"Did Lail say so?\" Sadhee asked, to make sure. \"No,")
sh(73, "but the way he looks at her is different. Haven't you noticed? These days he comes to this house a bit more often, and in class he keeps looking back every now and then,")
sh(74, "and he's definitely not looking at Sadhee,\" Asil said, laughing. \"Maybe some other girl caught Lail's fancy. Who knows?\"")
sh(75, "Sadhee said, settling into the beanbag. \"Just wait, then Sadhee will be sure too.\" Asil slowly opened the door and looked out.",
   [("creak", "ހުޅުވާލުމަށްފަހު", -22)])
sh(76, "Lail was still carefully pressing the ice pack to the sole of Saba's foot. \"How is it now? Is the pain any better?\"")
sh(77, "Lail asked tenderly. \"Fine, thank you,\" Saba said softly. \"Sorry, okay?\" Lail said, looking at Saba's face.")
sh(78, "\"For what?\" Saba asked, rubbing her foot. At that moment a teardrop fell from her eye onto her foot. Lail's gaze stopped on Saba's foot.",
   [("sob_breath", "ކަރުނަތިކި", -26)])
sh(79, "Saba wiped her tears, looked at Lail and smiled. \"I'm too much of a softie, right?\" Saba asked with a light smile.")
sh(80, "\"When it hurts, tears come to anyone's eyes. That's not being soft,\" Lail said calmly.")
sh(81, "Keeping her eyes on Lail's face, Saba asked again what he had apologised for. \"Actually...\"")
sh(82, "Lail grimaced and nodded. \"It wasn't Asil who kicked your foot. I was trying to kick Asil's foot and hit yours by mistake. I'm really, really sorry.\"",
   hum=True)
sh(83, "Lail said, lowering his head. Saba sat looking at Lail for a while, then suddenly burst out laughing loudly.")
sh(84, "Sadhee and Asil in the room watched without knowing what was happening, but neither of them tried to come out.")
sh(85, "As Saba began to laugh, a kind of hesitation rose in Lail's heart. She laughed and laughed until tears began to fall from her eyes, and she wiped them with both hands.")
sh(86, "Lail still sat with his head bowed like a culprit. At last Saba calmed her laughter and settled down. \"I know.\"")
sh(87, "A light smile was still showing on Saba's face. At her words, Lail turned his eyes towards Saba.", hum=True)
sh(88, "With that, a smile spread over Lail's lips too. \"What did you say?\" Lail asked in surprise.")
SHOTS = S

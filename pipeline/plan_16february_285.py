"""Beat/shot plan for 16 February episode 285 (used by plan_beats.py).
Ahlam's nightmare and the scream in the storm; the next morning at the resort; Malak's emails; the watch showcase.
No touch between Malak and any man; hijab on every woman; no readable text (emails = blurred glowing screens)."""

OFFICE = ("an open-plan back-office of the resort, rows of wooden desks with monitors, glass-walled cabins, large windows "
          "to palms and sea; the boss's cabin with a dark wooden desk and a leather chair")
SHOP = "a small resort souvenir shop with a lit glass watch showcase, shells and sarongs on shelves"
LOC = {
    "dream_cabin": OFFICE,
    "cabin": OFFICE,
    "office_dark": OFFICE,
    "sunrise": "a lush tropical resort garden on a small Maldivian island just after sunrise, broad green leaves, hibiscus and frangipani flowers heavy with dew drops, coconut palms, a glimpse of a calm turquoise lagoon",
    "garden_path": "a white-sand garden path of a Maldivian resort lined on both sides with neatly watered tropical plants, hibiscus bushes and young palms, low wooden staff buildings behind",
    "walkway": "a shaded wooden walkway in front of a row of resort guest rooms with dark wooden doors, potted palms and frangipani trees, a white-sand path and the lagoon glinting beyond",
    "canteen": "the staff canteen terrace, wooden tables, sea view, palms",
    "quiet_path": "a narrow empty back path behind the resort staff buildings, white sand between dense bushes and tall coconut palms, sharp black shadows, a low whitewashed wall",
    "souvenir_shop": SHOP,
    "watch_trance": SHOP,
}
MOOD = {
    "dream_cabin": "office after midnight in a storm, a dream: darkness of the cabin suddenly torn by a blinding cold white flash from behind, hazy, slightly desaturated with soft vignette, uncanny",
    "cabin": "office after midnight in a storm, a single warm amber desk lamp against deep blue-black shadows, cold blue-white lightning flickering through the window behind, rain streaking the glass, tense",
    "office_dark": "office after midnight in a storm, the open office almost dark, only faint monitor glow and the blue-white flash of lightning through the large rain-streaked windows, deep blue-black shadows, fear and loneliness",
    "sunrise": "bright tropical morning just after sunrise after a night of rain, soft golden rays breaking through thinning clouds, fresh, sparkling, peaceful",
    "garden_path": "bright tropical morning after rain, soft golden sunlight, wet sand, slightly desaturated turquoise-and-sand palette, gentle",
    "walkway": "bright tropical morning, dappled sunlight through palms, slightly desaturated turquoise-and-sand palette, light and calm",
    "canteen": "bright tropical late morning, sunlight on the sea, soft shade under the terrace roof, slightly desaturated turquoise-and-sand palette, quiet sadness under a light surface",
    "quiet_path": "harsh midday sun, glaring white sand and deep black shadows, oppressive heat haze, slightly desaturated, uneasy and fearful",
    "souvenir_shop": "midday, bright sun outside reflecting on the shop glass, cool lit showcase inside, still and tense",
    "watch_trance": "midday light dissolving into a blur, hazy, slightly desaturated memory-like dream with soft dark vignette, time seeming to stop",
}

BEATS = [
    dict(to=2, reason="episode opening: Ahlam's nightmare in his cabin — warm breath behind him, a blinding flash", chars=["ahlam"], loc="dream_cabin",
         visual="Ahlam sitting alone at his dark wooden desk in the dark office cabin, half turned in his leather chair to look over his shoulder, startled wide eyes, his face and shoulders lit by a sudden blinding cold white flash coming from behind him; nobody else visible, only empty darkness and white glare behind him",
         camera="medium shot, eye level, slightly from the side", amb="office_storm_night", transition="dissolve", sens="other",
         safe="the breath on his shoulder is shown only as a white flash from behind; no figure visible (bible rule 12)"),
    dict(to=5, reason="time/state change: he wakes from the dream, sweating, drinks water", chars=["ahlam"], loc="cabin",
         visual="Ahlam sitting up at his dark wooden desk in the office cabin just woken, beads of sweat on his forehead, breathing hard, gulping from a glass of water held in one hand, the other hand pushing back his thick wavy hair; papers and a closed laptop on the desk, a warm desk lamp beside him",
         camera="medium close-up, eye level", amb="office_storm_night", transition="dissolve"),
    dict(to=9, reason="action change: he stands, checks his watch; lightning, thunder and a scream", chars=["ahlam"], loc="cabin",
         visual="Ahlam standing beside his desk in the cabin, frozen mid-motion with one hand at his trouser pocket, head turned sharply toward the glass door of the cabin, listening intently, his other wrist raised with his dark leather wristwatch (plain dial, no numbers); a bright blue-white lightning flash through the rain-streaked window behind him",
         camera="medium wide, low angle", amb="office_storm_night", sens="other",
         safe="the scream is carried only by his listening face and the gasp sound; the clock time 1:57 is not shown"),
    dict(to=12, reason="location change: he hurries into the dark open office and sees a girl at a distant desk", chars=["ahlam", "malak"], loc="office_dark",
         visual="seen from behind Ahlam's shoulder at the doorway of his glass cabin: the long dark open-plan office with rows of desks, and far away at a desk under a window, small in the dim light, a young woman in a black hijab and maroon kurta seen from behind, sitting hunched over the desk with her head bowed low and both hands pressed to her ears; lightning flickering in the windows; a large empty distance between them",
         camera="wide shot over the shoulder, deep perspective down the office", amb="office_storm_night", sens="other",
         safe="Malak is seen only from far behind, sitting; Ahlam stays at the cabin doorway, no approach, no touch"),
    dict(to=14, reason="focus moves to Malak: her fear at the thunder, tears", chars=["malak"], loc="office_dark",
         visual="Malak sitting hunched forward at her desk in the dark office, elbows on the desk, both hands pressed over her ears over her black hijab, eyes squeezed shut, a tear on her cheek, her face pale and frightened in the faint cold monitor glow; rain streaming on the window behind her lit by a lightning flash; her hijab fully covering her hair and neck",
         camera="medium close-up, slightly high angle", amb="office_storm_night", sens="other",
         safe="her trauma shown only as fear and a tear; she sits upright at the desk (nobody lying), no injury shown"),
    dict(to=18, reason="time jump: the next morning, sunrise after the night's rain, dew on the garden", loc="sunrise",
         visual="close view of the resort garden at sunrise: broad wet green leaves and open hibiscus and frangipani flowers covered with sparkling dew drops shining like jewels, golden sun rays slanting through palms, a soft blur of the turquoise lagoon behind; no people",
         camera="close-up of leaves and flowers in the upper two-thirds, soft green blur below", amb="dawn_exterior", transition="black"),
    dict(to=21, reason="character change: Malak walks to the canteen and greets Babu the gardener", chars=["malak"], loc="garden_path",
         visual="Malak walking along the white-sand garden path holding her laptop against her side, turning her head with a small polite smile that does not reach her tired eyes; a few steps away beside the bushes a thin older South-Asian gardener in a green staff shirt and dark trousers watering the plants with a hose, smiling back at her",
         camera="medium wide, eye level, the path leading into the frame", amb="garden_day", sens="other",
         safe="Babu has no card; described only; no touch"),
    dict(to=24, reason="character change: Ahlam steps out of his room on a phone call and watches her; Ali joins him", chars=["ahlam", "ali", "malak"], loc="walkway",
         visual="Ahlam standing on the wooden walkway in front of his guest-room door holding a phone to his ear, his gaze following a young woman in a black hijab and maroon kurta walking away along a sand path in the far background, seen from behind; Ali in his white shirt, navy tie and glasses stopping beside Ahlam with his tablet, leaning in to speak softly with a knowing smile",
         camera="medium wide, eye level, Ahlam and Ali in the foreground, Malak small in the distance", amb="resort_day"),
    dict(to=30, reason="action change: Ahlam and Ali face each other talking about Malak's overtime and a room for her", chars=["ahlam", "ali"], loc="walkway",
         visual="Ahlam and Ali standing face to face on the shaded wooden walkway, Ahlam serious and thoughtful with his arms folded, phone now in his hand, asking a question; Ali holding his tablet in both hands, explaining earnestly with a kind expression; dappled morning light",
         camera="medium two-shot, eye level", amb="resort_day"),
    dict(to=32, reason="focus change: Ahlam's gaze — Malak greeting staff on her way to the canteen", chars=["malak"], loc="garden_path",
         visual="seen from a distance along the sunny garden path: Malak in her black hijab and maroon kurta walking toward the canteen with her laptop, seen from the side and slightly behind so her face is hard to make out, nodding with a warm smile to a female staff member in a sand-beige uniform and white hijab who passes her; palms and the lagoon beyond",
         camera="long shot, telephoto compression, eye level", amb="garden_day"),
    dict(to=34, reason="return to the two-shot: Ahlam snaps at Ali's teasing", reuse="beat_009", loc="walkway",
         visual="reuse of Ahlam and Ali talking on the walkway", amb="resort_day"),
    dict(to=38, reason="action change: they walk on together, talking about the watch", chars=["ahlam", "ali"], loc="walkway",
         visual="Ahlam and Ali walking side by side along a palm-shaded sand path, Ahlam slightly ahead with a frown of concentration, looking straight ahead; Ali keeping pace beside him, glancing at his tablet and then curiously at Ahlam; long morning shadows on the white sand",
         camera="medium wide tracking shot from the front, eye level", amb="resort_day"),
    dict(to=42, reason="emotional change: Ahlam threatens Ali, who panics", chars=["ali", "ahlam"], loc="walkway",
         visual="Ali stopping on the path, flustered, eyes wide behind his glasses, one hand raised in a quick 'no, no' gesture, clutching his tablet to his chest; Ahlam already walking away a step ahead, half turned back with a stern, unsmiling face",
         camera="medium shot, eye level, Ali in the foreground", amb="resort_day"),
    dict(to=45, reason="location and character change: Malak at a canteen table with juice and her laptop", chars=["malak"], loc="canteen",
         visual="Malak sitting alone at a wooden table on the canteen terrace, a glass of orange juice beside her open laptop, looking at the screen with a weary, closed expression, the sea and palms bright behind her",
         camera="medium shot, eye level, the table top as a calm lower third", amb="cafe"),
    dict(to=49, reason="detail change: the email from Kiyaara on her screen", chars=["malak"], loc="canteen",
         visual="over Malak's shoulder: her black hijab and maroon sleeve in the foreground, the open laptop screen showing only a blurred glowing white rectangle with soft grey bars (nothing readable), her slim silver watch on the wrist at the keyboard; the bright sea out of focus beyond",
         camera="over-the-shoulder close-up", amb="cafe", sens="other",
         safe="emails are blurred glowing screens with no readable text; Kiyaara is never shown"),
    dict(to=51, reason="emotional turning point: Malak squeezes her eyes shut, a tear falls", chars=["malak"], loc="canteen",
         visual="close-up of Malak at the canteen table, eyes squeezed shut, a single tear running down her cheek, quickly lifting her fingertips to wipe it away, her black hijab fully covering hair and neck, sunlit sea blurred behind",
         camera="close-up, eye level", amb="cafe"),
    dict(to=54, reason="return to Malak at her table: Naaif's email, she frowns and sips juice", reuse="beat_014", loc="canteen",
         visual="reuse of Malak at the canteen table", amb="cafe", sens="other",
         safe="Naaif's email is not shown; only Malak's reaction"),
    dict(to=59, reason="character change: Ahlam and Ali sit down in the canteen; Ahlam sees Malak", chars=["ahlam", "ali"], loc="canteen",
         visual="Ahlam and Ali seated together at a wooden table on the canteen terrace, Ahlam leaning slightly forward, looking intently across the terrace past the camera with a careful searching look; Ali beside him leaning in, grinning and talking out of the side of his mouth, his tablet on the table",
         camera="medium two-shot, eye level", amb="cafe"),
    dict(to=62, reason="viewpoint change: over Ahlam's shoulder toward Malak far across the terrace", chars=["ahlam", "malak"], loc="canteen",
         visual="over Ahlam's shoulder (the back of his head and black shirt blurred in the foreground): across the sunny canteen terrace, several tables away, Malak sitting alone at her laptop in her black hijab and maroon kurta, small in the frame, the sea behind her; a wide empty space between them",
         camera="over-the-shoulder long shot", amb="cafe", sens="intimacy",
         safe="attraction shown only as a distant gaze across the canteen (rule 11)"),
    dict(to=67, reason="emotional change: Ahlam glares at Ali's teasing, Ali apologises", chars=["ahlam", "ali"], loc="canteen",
         visual="at the canteen table: Ahlam frowning with drawn brows, fixing Ali with a hard sideways glare; Ali leaning back with both palms raised in apology, a guilty sheepish grin behind his glasses",
         camera="medium two-shot, eye level", amb="cafe"),
    dict(to=69, reason="action change: the waiter takes the order; Ahlam settles back and gazes at Malak", chars=["ahlam", "ali"], loc="canteen",
         visual="a young male waiter in a sand-beige resort uniform walking away from the table with a notepad; Ahlam leaning back in his chair, his face softened, quietly gazing across the terrace with clear interest; Ali beside him watching Ahlam with a sly smirk",
         camera="medium wide, eye level", amb="cafe", sens="intimacy",
         safe="only a look from a distance, no contact"),
    dict(to=72, reason="return to Malak at her table: bitter thoughts about Naaif, then Zain's email", reuse="beat_014", loc="canteen",
         visual="reuse of Malak at the canteen table", amb="cafe"),
    dict(to=73, reason="action change: Malak looks up at the sky to hold back tears", chars=["malak"], loc="canteen",
         visual="Malak at the canteen table tilting her face up toward the bright sky, eyes glistening with held-back tears, lips pressed together, sunlight on her face, her black hijab fully covering hair and neck, palm fronds against the sky above her",
         camera="medium close-up, slightly low angle", amb="cafe"),
    dict(to=75, reason="character change (comic beat): Ahlam and then Ali look up at the sky too", chars=["ahlam", "ali"], loc="canteen",
         visual="at their canteen table Ahlam and Ali both tilting their heads back to look up at the empty blue sky, Ahlam serious and absorbed, Ali squinting upward in comic confusion behind his glasses, one hand shading his eyes",
         camera="medium two-shot, slightly low angle", amb="cafe"),
    dict(to=76, reason="return to Malak looking up, holding back tears before opening the mail", reuse="beat_023", loc="canteen",
         visual="reuse of Malak looking up at the sky", amb="cafe"),
    dict(to=78, reason="return to the laptop screen: Zain's email", reuse="beat_015", loc="canteen",
         visual="reuse of the over-the-shoulder laptop glow", amb="cafe", sens="other",
         safe="Zain's email is a blurred glowing screen; Zain is not shown"),
    dict(to=79, reason="action change: Malak bows her head, shuts the laptop and gets up to leave", chars=["malak"], loc="canteen",
         visual="Malak rising from the canteen table with her head bowed low, closing the laptop with one hand, her face turned down and away, a tear glinting, the half-finished juice glass left on the table",
         camera="medium shot, eye level", amb="cafe"),
    dict(to=80, reason="return to Ahlam wondering where he has seen her", reuse="beat_018", loc="canteen",
         visual="reuse of Ahlam seated, looking across", amb="cafe"),
    dict(to=84, reason="location change: Malak walks back alone by a quiet path in the midday heat", chars=["malak"], loc="quiet_path",
         visual="Malak walking alone along the empty sunlit back path, hugging her laptop tightly to her chest with both arms, wiping her cheek with the back of one hand, shoulders hunched as if cold despite the blazing sun, her eyes red and downcast",
         camera="medium wide, from the front, eye level", amb="resort_day"),
    dict(to=87, reason="action change: fear — she glances behind her, holding her breath", chars=["malak"], loc="quiet_path",
         visual="Malak on the empty path glancing back over her shoulder with frightened wide eyes, holding her breath, her own long dark shadow stretching across the glaring white sand; the path behind her empty between dark bushes and palm shadows",
         camera="medium shot from slightly behind and to the side", amb="resort_day", sens="other",
         safe="the terrifying night is only implied by her fear; nobody follows her; no flashback content"),
    dict(to=90, reason="location change: she stops at the souvenir shop window and stares at the watch showcase", chars=["malak"], loc="souvenir_shop",
         visual="Malak standing outside the souvenir shop's glass front, her faint reflection in the glass, staring through it at a lit glass showcase of elegant wristwatches with plain unmarked dials inside; shells and folded sarongs on shelves; she slowly lifts her wrist",
         camera="medium shot, from inside the shop looking out through the glass at her face", amb="shop_day", sens="other",
         safe="watches have plain dials with no brand, no numbers"),
    dict(to=94, reason="emotional turning point: her watch hands seem to turn backward; time stops, the past rushes in", chars=["malak"], loc="watch_trance",
         visual="extreme close-up of Malak's raised wrist with her slim silver watch, its plain dial with no numerals and two thin hands blurred as if spinning backward, the maroon sleeve at the edge; behind it, out of focus, her pale stunned face in black hijab reflected in the shop glass, the showcase lights smearing into streaks",
         camera="extreme close-up, the watch in the upper half, soft dark vignette", amb="memory", transition="dissolve", sens="other",
         safe="plain unmarked watch dial; the flashback of that night is not shown"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Before he could sink into the deep sea of his thoughts, he started at the feel of a hot breath falling on his shoulder from behind.",
   [("breath", "ނޭވާގެ", -20), ("gasp", "ސިހުނީ", -20)])
sh(2, "Startled, he turned around. At that moment a light flooded his eyes so that he could make out nothing. Suddenly he opened his eyes in panic.",
   [("breath_heavy", "ހުޅުވާލީ", -20)])
sh(3, "Beads of sweat stood out on his face. He quickly took the glass of water beside him and drank it in one breath. He calmed down.",
   [("cup_clatter", "ފެންތަށިގެ", -22)])
sh(4, "Even then his breath was short. Sure now that what he had just seen was a dream, he tried to calm himself.",
   [("breath_heavy", "ނޭވާވަނީ", -22)])
sh(5, "With his right hand he ran his fingers up through his thick, jet-black hair. Then he took a tissue and wiped the sweat from his face.")
sh(6, "Glancing at the watch on his wrist, he got up from the desk. It was now three minutes to two in the night.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24), ("clock_tick", "ގަޑިއަށް", -22)])
sh(7, "Lightning still flashed through the window into the office. With the flash came a crack of thunder so loud the whole place seemed to shake.",
   [("thunder", "ގުގުރީގެ", -14)])
sh(8, "With that sound came the scream of a girl. \"Mamma!\" Ahlam, who was slipping the room card from the desk into his pocket, froze at the sound.",
   [("gasp", "ހަޅޭކުގެ", -16)], hum=True)
sh(9, "Unsure, he looked at his watch once more. That sound was one he had heard a week before.",
   [("heartbeat", "ހަފުތާއެއް", -22)])
sh(10, "Quickly picking up his phone and pocketing it, he came out of the cabin almost at a run.",
   [("footsteps_pavement", "ދުވެފައި", -20), ("door_open", "ނިކުތީ", -20)])
sh(11, "He searched the office anxiously, determined to find whoever had screamed. His steps stopped.",
   [("footsteps_pavement", "ހޯދާ", -22)])
sh(12, "He had seen a girl with her head down on a desk in the dim light, her hands on her temples and her eyes squeezed shut.",
   [("heartbeat", "ފެނުމުންނެވެ", -22)], hum=True)
sh(13, "Malak had started at the loud crash of thunder. Even after three breaths her heart would not settle. However hard the cold drops of rain fell,",
   [("thunder", "ގުގުރީގެ", -14), ("heartbeat", "ހިތް", -20)])
sh(14, "her heart only raced faster. Not sensing that anyone was watching her, she wiped the tears coming from under her lashes.",
   [("sob_breath", "ކަރުން", -24)], hum=True)
sh(15, "The sun spread its golden rays over the world, bidding farewell to the stillness of the night.")
sh(16, "After the rain that had fallen all night without stopping, with the cool breezes of dawn the whole world wore a cloak of freshness.",
   [("leaves_rustle", "ވައިރޯޅިތަކާއެކު", -24)])
sh(17, "In the soft light breaking through the clouds, the dew drops shining on the deep green leaves and the blooming flowers looked like jewels.")
sh(18, "The small beauty of a dew drop is a precious gift of nature that brings life to the human soul. \"Babu.\"")
sh(19, "Calling out to Babu, who was watering the plants growing along both sides of the path, Malak walked on toward the canteen. Her laptop was in her hand.",
   [("footsteps_sand", "ގޮވާލަމުން", -24), ("pour", "ފެންދޭން", -24)])
sh(20, "\"Aan. Madam. Not going to the island at night either?\" Babu asked in broken Dhivehi. \"Busy. Very busy.\"")
sh(21, "She put a smile on her lips and hid the anxiety on her face. Malak kept walking on.",
   [("footsteps_sand", "ފިޔަވަޅު", -24)])
sh(22, "Babu went on watering the plants, smiling. Just then Ahlam came out of his room. He was on a phone call.",
   [("pour", "ފެން", -24), ("door_open", "ކޮޓަރިންނިކުތެވެ", -20)])
sh(23, "When he saw Malak pass by, he stood watching. \"That's Malak. Didn't I mention her?")
sh(24, "A very hardworking, well-mannered girl,\" Ali said softly, stopping beside Ahlam. Ahlam took a deep breath and looked at Ali. \"Hmm...",
   [("sigh", "ފުންނޭވާއެއް", -22)])
sh(25, "I said, until what time does office work go on?\" Ahlam asked thoughtfully. \"Seven o'clock at the latest,")
sh(26, "but Malak does overtime. Sometimes she even takes on other staff's unfinished work. A hardworking girl,\" Ali said warmly.")
sh(27, "\"Is that so? Doesn't the resort give her a room?\" Ahlam asked. \"Actually every night after office Malak goes home to her island.")
sh(28, "But lately she hasn't gone to the island; she spends a lot of time at the office. It's been a week now that Malak has been like this.")
sh(29, "The other day she was very ill too; that day I put her in a guest room for the time being. But...\" Ali broke off.")
sh(30, "\"Arrange a room for her from the staff rooms. I don't want to lose hardworking people,\" Ahlam said.")
sh(31, "His eyes were still on Malak, walking toward the canteen. As she went, she could be seen chatting kindly and smiling with everyone she met.")
sh(32, "But Ahlam had still not seen Malak's face properly. Seeing Ahlam watching Malak, Ali cleared his throat mischievously.")
sh(33, "\"Have you noted down everything I told you just now?\" Knowing Ali was teasing him, he asked in a stern tone. \"Yes.")
sh(34, "Noted,\" Ali said. There was a mischievous smile on his lips. \"And — have you found the truth about the watch I gave you?\"")
sh(35, "Ahlam asked, slowly starting to walk. \"Not yet. But I'm looking.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -22)])
sh(36, "I've checked pretty much all the shops on most of the islands around here. But there's no watch of that brand,\" Ali said, keeping pace with Ahlam.",
   [("footsteps_pavement", "ހިނގަމުން", -24)])
sh(37, "\"Don't check only the islands around here. Check every area. It's very important to find the truth about that watch,\" Ahlam said, thinking.")
sh(38, "He wanted to find the truth of something that had become a headache for him. \"Where did the boss find that watch?\"")
sh(39, "Ali asked, his curiosity showing. \"Don't talk so much. Do the work given to Ali.")
sh(40, "Within seven days you must bring me every detail about the watch. Otherwise I'll give the job to someone who works with fewer words.\"")
sh(41, "Ahlam said, walking ahead. He wanted to scare Ali. \"No, no, boss. I'm doing it,\" Ali said quickly.",
   [("gasp", "އަވަސް", -22)])
sh(42, "It felt as if his breath had caught in his throat. That job was one he dearly loved. He had spent his life in that job at that resort.",
   [("breath", "ނޭވާ", -22)])
sh(43, "He was a man as kind-hearted as he was hardworking. Malak took a sip from her glass of juice and set it down.",
   [("cup_clatter", "ބެހެއްޓިއެވެ", -22)])
sh(44, "Then she looked at something on the laptop in front of her. She went through the emails that had come in. It had been a week since she last checked them.",
   [("keyboard_typing", "ޗެކް", -24)])
sh(45, "There was an email from Kiyaara. Malak closed her eyes. She did not really want to read that email.")
sh(46, "Weariness showed plainly on her face. Even so, she wanted to see what sweet nothings Kiyaara had written. \"Hi Malak. Still not done with work?")
sh(47, "No holiday? I called you so many times. Your phone's switched off. What are you doing with your phone? Please call.")
sh(48, "Miss you so much. Why didn't you come to Zain's birthday party? Zain is really upset. Are you angry with Zain?")
sh(49, "Zain says you don't pick up when he calls. At least send Zain a message even if you're busy. OK? Love you, miss you lots, bestie.\"")
sh(50, "After reading the mail Malak shut her eyes even tighter than before. At that very moment a big tear dropped from her eye.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(51, "Afraid people would see, she quickly wiped the tears from her eyes. Then she opened the next mail. It was from Naaif. \"Don, where are you?",
   [("keyboard_typing", "ހުޅުވާލިއެވެ", -24)])
sh(52, "I called your number so many times. I called the office a lot too. Don, I urgently need 1000 dollars. Please get it for me.")
sh(53, "I promise I'll give it back within two months. I don't dare tell big brother — the way he asks questions. Please get it for me, Don. Mamma said to ask you.")
sh(54, "Please, Don.\" Malak frowned and drank a little more juice. Just then Ahlam and Ali came into the restaurant.",
   [("footsteps_pavement", "ވަދެގެން", -24)])
sh(55, "Sitting down at a table, they looked around. When Ahlam saw Malak, he took off the glasses he was wearing and looked at her carefully.",
   [("cloth_rustle", "އިށީންނަމުން", -24)])
sh(56, "In the office at night he hadn't seen her face properly. Just now too he had only seen Malak from behind. \"That's Malak.")
sh(57, "The secretary to the boss of the resort now being built,\" Ali said jokingly. \"When was that arranged without my knowing?")
sh(58, "Can you change my secretary just like that?\" Ahlam asked carelessly. \"I'll be there too, but Malak is the one who knows most about that resort's affairs.")
sh(59, "And Malak is very hardworking — didn't I just tell you that?\" Ali said.")
sh(60, "\"Will a girl suit a site where work is going on? Only men work there. She's a girl,\" Ahlam said, looking at Malak.")
sh(61, "\"Girls work there too. Besides, Malak would go from Admin to that project's office, as the boss's secretary.")
sh(62, "She won't have to go out on site. She'll do whatever work the boss gives her.\" A mischievous smile showed on Ali's lips.")
sh(63, "Ahlam thought for a moment. \"Are you teasing me?\" Ahlam asked, drawing his brows together, because he knew Ali was a mischievous man. \"No.")
sh(64, "Boss. Who am I to tease you? Besides, a chance like this comes only rarely. Think of it as luck.")
sh(65, "Malak is a girl famous for her beauty even on her island. And she's single; she's not that close any more with the boy she was going around with.\"")
sh(66, "There was a joking tone in Ali's voice. Ahlam glared at Ali. \"Did you come here to work? Or...\" Ahlam narrowed his eyes. \"Sorry, boss.")
sh(67, "I won't say it again. Since the boss is single, I was just trying to find you a good girl. Sorry,\" Ali said quickly.")
sh(68, "When the waiter came and stood by them, Ahlam gave the order. After the waiter took the order away, Ahlam settled in his chair and looked at Malak.",
   [("footsteps_pavement", "ވެއިޓަރު", -24)])
sh(69, "Seeing that, a mischievous smile appeared on Ali's lips once again. That Ahlam liked Malak was showing on Ahlam's face.")
sh(70, "\"It's 'Don' when they need something. Otherwise nobody even remembers I exist. Nobody even asked why I don't come home.")
sh(71, "When they need money, it's 'Don' all the way.\" Grumbling to herself, she closed Naaif's mail and opened the next one. The next was from Zain.",
   [("keyboard_typing", "ހުޅުވާލިއެވެ", -24)])
sh(72, "Malak sat hesitating whether to open it or not. \"Should I open this mail? Should I see what Zain is saying?\"")
sh(73, "More despair than before showed on her face. As tears began to gather in her eyes, she looked up at the sky so they would not fall.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(74, "Ahlam too looked up at the sky at the same moment as Malak. Ali, who had been looking at Ahlam, looked up at the sky. \"Is there something up there?\"")
sh(75, "Ali asked, still looking up. Ahlam said nothing; he narrowed his eyes at Ali. Then he looked at Malak.")
sh(76, "Malak widened her eyes, trying to stop the tears. After sitting like that for a while, Malak opened the mail. Once she had calmed down.",
   [("keyboard_typing", "ހުޅުވާލިއެވެ", -24)])
sh(77, "\"Malak, where are you? What happened to your phone? Call me. Mamma has now confirmed the wedding date. There's so much to talk about.")
sh(78, "Love you, miss you.\" Tears came from Malak's eyes. She managed to hold them back for only a few seconds.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(79, "Malak bowed her head and shut the laptop. She hurried to leave, afraid someone would see her crying.",
   [("soft_thud", "ލައްޕާލިއެވެ", -22)])
sh(80, "\"She looks so much like a girl I've seen somewhere... where was it?\" Ahlam said to himself.")
sh(81, "Holding the laptop to her chest and wiping her tears, Malak set off toward the office. She chose a quiet path, not the way she had come to the restaurant.",
   [("footsteps_pavement", "ހިނގައިގަތީ", -22)])
sh(82, "Though it had rained in the night, the fierce heat of the sun now hung over everything.")
sh(83, "Yet a cold shiver had run through her body. Because she had read Zain's mail.",
   [("breath", "ތުރުތުރެއް", -22)])
sh(84, "As Zain's unfaithfulness came back to her, so did that terrifying night. With the unease in her heart she walked on.",
   [("heartbeat", "ބިރުވެރި", -20)], hum=True)
sh(85, "Every step Malak took along that silent path showed her unease and her fear.",
   [("footsteps_pavement", "ފިޔަވަޅަކުން", -22)])
sh(86, "Quickly glancing around her, checking whether someone was following behind, she walked on holding her breath.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
sh(87, "Though it was broad daylight, an indescribable darkness and terror surrounded her.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -22)])
sh(88, "Malak's steps stopped beside the glass front of the souvenir shop that stood where the two paths met.",
   [("footsteps_pavement", "ހިނގުން", -22)])
sh(89, "Her gaze went straight to the big glass showcase inside. It stopped on the modern branded watches in that showcase.")
sh(90, "Echoing in her ears was the sound of those watches' hands going round. Slowly raising her arm, Malak looked at the watch on her own wrist.",
   [("clock_tick", "ކަށިތައް", -16)])
sh(91, "At that very moment, she felt as if the hands of her wristwatch had begun to turn backward.",
   [("clock_tick", "ކަށިތައް", -16)], hum=True)
sh(92, "Right then the whole scene before her eyes blurred, as though time had stopped. What she began to see in the souvenir shop's glass was not the reality of now.",
   [("heartbeat", "ހުއްޓުނު", -20)], hum=True)
sh(93, "It was the reality of a week ago. Her mind sank into those memories of the past, with the sound of that watch's second hand,",
   [("clock_tick", "ކަށީގެ", -16)], hum=True)
sh(94, "dragging her back once again into that terrifying moment.",
   [("heartbeat", "ބިރުވެރި", -20)], hum=True)
SHOTS = S

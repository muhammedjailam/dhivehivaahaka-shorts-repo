"""Beat/shot plan for Aliflaila episode 569 (Night 7-8: the trapped jinni, King Yunan and the Sage Duban).
Used by plan_beats.py."""

LOC = {
    "chamber_night": "King Shahryar's palace bedchamber late at night, Persian carpets, silk cushions, a low cushioned divan, glowing brass lanterns, an arched carved lattice window showing a huge moon over a city of white onion domes and slender towers",
    "shore": "a wide empty golden beach on a turquoise sea in old Arabian lands, low rocks, gentle surf, a few date palms far behind, an open old brass jar lying on the sand",
    "water_edge": "the very edge of the sea where small waves wash over wet golden sand and smooth pebbles, wide turquoise sea to the horizon",
    "yunan_city": "the fairy-tale Persian capital of King Yunan: a huge palace of gold and silver domes and slender towers above a sea of rooftops, banners on the walls, rows of small cavalry on the plain before it, distant hills",
    "sick_room": "a vast, dim royal chamber in King Yunan's palace, tall carved arches, heavy purple curtains half drawn, a gilded divan, low brass tables with bowls and small jars of medicine",
    "duban_study": "the old sage's cosy study: shelves of closed leather-bound books and rolled scrolls, bunches of drying herbs hanging from the beams, a brass astrolabe, clay jars and a mortar and pestle on a wooden table, an arched window open to a starry sky",
    "darbar": "King Yunan's grand throne hall: a golden throne on a dais under a silk canopy, rows of marble columns, rich carpets, courtiers in modest robes standing in rows at the sides, sunlight in long shafts from high arched windows",
    "workshop": "the old sage's workshop corner by lamplight: a wooden workbench with carving tools for wood, small bowls of glowing green and gold medicine, a funnel, a polished wooden polo mallet with a hollow handle and a round leather polo ball",
    "polo": "a vast green royal polo field outside the palace walls, white tents and fluttering pennants at the edges, distant domes and palms, a clear turquoise sky",
    "bath": "a royal marble bathhouse: white marble arches, a domed ceiling with small star-shaped skylights letting in beams of light, thick clouds of warm steam, a round pool, brass basins",
    "royal_bedroom": "King Yunan's royal bedroom in the early morning, tall arched window with sheer curtains, golden morning sunbeams, a carved cedar chest, silk drapes",
    "chamber_dawn": "King Shahryar's palace bedchamber at dawn, Persian carpets, silk cushions, a low cushioned divan, brass lanterns burning low, an arched carved lattice window showing a pink-gold dawn sky over the city of domes with a distant slender minaret silhouette",
    "palace_hall_dawn": "a long marble palace corridor of Shahryar's palace at dawn, arched windows with lattice screens throwing patterned golden light on the floor, distant open double doors leading to the court",
}
MOOD = {
    "chamber_night": "late night just before dawn, deep midnight blue with warm amber lantern glow, the stars of dawn beginning to show, hushed and expectant",
    "shore": "bright morning sun, turquoise sky, sparkling sea, tense and magical",
    "water_edge": "bright late-morning sun glittering on the waves, breezy, tense then curious",
    "yunan_city": "golden afternoon, soft golden storybook glow, splendid and rich",
    "sick_room": "dim daylight through half-drawn curtains, cool grey-violet shadows inside a soft golden storybook glow, heavy sorrow and despair",
    "duban_study": "night, warm candle and lamplight, deep blue starry window, soft golden storybook glow, wise and calm",
    "darbar": "bright daylight shafts through high windows, soft golden storybook glow, grand and formal",
    "workshop": "night, warm oil-lamp light, magical green-gold glimmer of medicine, soft golden storybook glow, hopeful",
    "polo": "bright sunny day, turquoise sky, warm golden light, soft golden storybook glow, energetic and joyful",
    "bath": "warm evening, beams of light through the steam, soft golden storybook glow, peaceful",
    "royal_bedroom": "early morning, soft golden sunbeams, soft golden storybook glow, wonder and joy",
    "chamber_dawn": "dawn, golden-pink first sunlight streaming through the lattice window, lanterns burning low, suspense with a gentle smile",
    "palace_hall_dawn": "early dawn, warm golden light patterns on marble, calm and resolute",
}

BEATS = [
    # ---------------- FRAME: night, the bedchamber ----------------
    dict(to=3, reason="episode opening: the frame chamber at the end of the night, Dunyazad asks for the story", chars=["dunyazad", "shahrazad", "shahryar"], loc="chamber_night",
         visual="Dunyazad sitting on the carpet leaning eagerly towards her elder sister with clasped hands and big pleading eyes; Shahrazad sitting upright on a silk cushion beside her, turning to her with a gentle smile; King Shahryar sitting on the divan an arm's length or more away, fully dressed, empty-handed, listening; the lattice window behind them shows the moonlit city of domes and the first faint stars of dawn",
         camera="wide shot, eye level, the three figures in the upper two-thirds, the carpet forming a calm lower third", amb="palace_night"),
    dict(to=6, reason="action change: the king grants permission and Shahrazad begins with expressive hands", chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_night",
         visual="Shahrazad on her cushion raising one hand gracefully as she begins to tell the story, her other hand open in her lap, eyes bright; King Shahryar on the divan an arm's length or more away gives a slow approving nod, leaning forward with keen interest; Dunyazad sits on the carpet beside her sister hugging her knees, listening; faint golden sparkles drift up from Shahrazad's raised hand towards the lantern light",
         camera="medium wide shot, slightly low angle, eye level with Shahrazad", amb="palace_night"),
    # ---------------- TALE 1: the fisherman and the jinni ----------------
    dict(to=10, reason="scene change into the tale: on the beach the jinni trembles at God's Name and the fisherman challenges him about the jar", chars=["jar_jinni", "fisherman"], loc="shore",
         visual="the colossal jinni of the jar towering over the beach, his indigo-violet smoke tail rising from the open old brass jar on the sand, recoiling and trembling with wide golden eyes and empty raised hands as a soft beam of pure golden light shines down between him and the fisherman; the thin old fisherman standing small and bold on the sand, pointing at the narrow jar with a sceptical squint and a clever half-smile",
         camera="dramatic low angle, the jinni filling the upper two-thirds, the fisherman small at the lower left, wet sand as a calm lower third",
         amb="seashore_day", transition="dissolve", sens="other",
         safe="God's Name is shown only as a soft beam of golden light; the jinni is empty-handed"),
    dict(to=12, reason="action change: the proud jinni turns to smoke and pours back into the jar", chars=["jar_jinni", "fisherman"], loc="shore",
         visual="the jinni's huge body dissolving into a spiralling column of glittering indigo-violet smoke that pours down into the narrow mouth of the old brass jar on the sand, only his proud gloating face and forked beard still visible at the top of the swirl; the old fisherman crouching beside the jar, quietly holding the round lead stopper behind his back, watching with a sly smile",
         camera="medium wide shot, low angle, the smoke spiral rising into the upper two-thirds", amb="seashore_day", sens="other",
         safe="magic shown as swirling glittering smoke and sparkles, fairy-tale, never horror"),
    dict(to=14, reason="action change: the fisherman slams the sealed lid onto the jar", chars=["fisherman"], loc="shore",
         visual="close-up of the old fisherman's weathered hands pressing a round grey lead stopper down onto the mouth of the old brass jar; the stopper bears a softly glowing abstract eight-petalled geometric rosette, no letters; the last wisps of indigo smoke are cut off with a flash of golden sparks; the fisherman's determined face above, eyes narrowed",
         camera="close-up from slightly above, the hands and stopper in the upper half, the sand below", amb="seashore_day", sens="other",
         safe="Prophet Sulaiman's seal is only an abstract eight-petalled rosette, no letters, no star; the Prophet is never depicted"),
    dict(to=17, reason="action change: the jinni is trapped, struggles and weeps inside the jar", loc="shore",
         visual="the sealed old brass jar standing alone on the wet sand, rattling and tilting, small motion lines around it, the abstract golden rosette on the lead stopper glowing steadily, a faint indigo glow pulsing through the metal and two small sad glowing golden eyes reflected in its polished surface; foam of a wave creeping close",
         camera="close low angle on the jar, the sea and sky behind, wet sand in the lower third", amb="seashore_day", sens="other",
         safe="the jinni's struggle is shown only through the rattling sealed jar"),
    dict(to=22, reason="action change: the fisherman carries the jar towards the sea", chars=["fisherman"], loc="shore",
         visual="the old fisherman walking resolutely across the sand towards the surf, the heavy sealed brass jar hugged in both arms, his cast net slung over his shoulder, his face stern and determined; a thin wisp of indigo smoke curls anxiously from the seam of the jar's stopper; waves rolling in ahead of him",
         camera="medium wide shot, from the side, the sea horizon high in the frame", amb="seashore_day"),
    dict(to=26, reason="emotional turning point: at the water's edge the jinni weeps and begs for mercy", chars=["fisherman"], loc="water_edge",
         visual="the old fisherman standing ankle-deep in the surf in his tunic, holding the sealed brass jar raised over the waves with both hands, unmoved and stern; the jar is tightly sealed and trembling, only a thin wisp of indigo smoke and a few tear-like violet sparkles leak from the seam of the stopper; NO giant and no jinni figure anywhere in the picture, the sky above is empty",
         camera="medium shot, low angle, the jar and the fisherman's face in the upper half, waves in the lower third", amb="seashore_day"),
    dict(to=31, reason="action change: the fisherman refuses, sits down at the water's edge and begins the tale", chars=["fisherman"], loc="water_edge",
         visual="the old fisherman sitting cross-legged on the wet sand at the water's edge, the sealed brass jar standing upright in front of him, one finger raised as he begins to tell a story with a knowing smile; the jar is tightly sealed with its lead stopper, a small curious curl of indigo smoke and two tiny glowing golden eye-sparks peeking from the seam as if listening; NO giant and no jinni figure anywhere in the picture; a faint golden storybook shimmer rising in the air above them",
         camera="medium shot, eye level, the fisherman and jar in the upper two-thirds, wet sand and foam in the lower third", amb="seashore_day"),
    # ---------------- TALE-WITHIN-THE-TALE: King Yunan and the Sage Duban ----------------
    dict(to=34, reason="scene change into the tale-within-the-tale: King Yunan's splendid kingdom", chars=["king_yunan"], loc="yunan_city",
         visual="soft golden storybook glow: King Yunan standing on a high palace balcony, empty-handed, looking out over his vast realm; behind and below him the palace of gold and silver domes, a sea of rooftops and rows of small cavalry banners on the plain; he looks rich and powerful but his eyes carry a hidden sadness",
         camera="wide shot from behind and beside the king, the city filling the frame, the balcony parapet as the lower third", amb="palace_day", transition="dissolve"),
    dict(to=38, reason="emotional turning point: the king's terrible sickness and the physicians' failure", chars=["king_yunan"], loc="sick_room",
         visual="soft golden storybook glow: King Yunan sitting hunched alone on a gilded divan, completely wrapped in a heavy hooded grey cloak drawn over his crown and turban, only his sad tired eyes and grey-streaked beard visible, his hands hidden in the cloak; at a distance across the chamber three small background physicians in modest long robes and turbans stand holding bowls and jars, shaking their heads; courtiers keep far back by the curtains",
         camera="wide shot, eye level, the hooded king in the upper half, the marble floor as a calm lower third",
         amb="palace_day", sens="other",
         safe="leprosy shown only as the king hidden under a hooded cloak and physicians shaking their heads; no skin lesions"),
    dict(to=40, reason="character change: the learned old Sage Duban is introduced", chars=["sage_duban"], loc="duban_study",
         visual="soft golden storybook glow: the old sage Duban sitting at his wooden table surrounded by towering stacks of closed leather-bound books and rolled scrolls, a brass astrolabe and bunches of herbs, gazing up at the starry window with calm knowing eyes, one hand resting on a closed book; tiny golden sparkles of wisdom drift in the lamplight",
         camera="medium wide shot, eye level, the sage in the upper half, the table and floor below", amb="memory"),
    dict(to=46, reason="scene change: Duban comes before the king at court and promises a cure", chars=["sage_duban", "king_yunan"], loc="darbar",
         visual="soft golden storybook glow: the old sage Duban bowing respectfully with one hand on his chest before the golden throne; King Yunan on the throne completely wrapped in a heavy hooded grey wool cloak, the grey hood pulled up over his crown and turban and the cloak closed over his purple robe so no purple shows, his hands hidden in the cloak, leaning forward in astonishment with wide hopeful eyes and an open hand; small background courtiers in modest robes watching from between the columns",
         camera="wide shot, slightly low angle from behind Duban towards the throne", amb="throne_hall"),
    dict(to=49, reason="scene change: Duban prepares the hollow polo mallet and the medicine", chars=["sage_duban"], loc="workshop",
         visual="soft golden storybook glow: the old sage Duban at his workbench by lamplight carefully pouring a glowing green-gold medicine through a small funnel into the hollow handle of a polished wooden polo mallet, a round leather polo ball beside it, sparkles rising from the medicine, his face focused and kind",
         camera="medium close shot, eye level, his face and hands in the upper two-thirds, the workbench in the lower third", amb="memory"),
    dict(to=53, reason="time jump: the next day Duban presents the mallet and ball to the king", chars=["sage_duban", "king_yunan"], loc="darbar",
         visual="soft golden storybook glow: the old sage Duban offering the polished polo mallet and the round leather ball with both hands to King Yunan, who stands before his throne completely wrapped in a heavy hooded grey wool cloak, the grey hood pulled up over his crown and turban and the cloak closed over his purple robe, one hand reaching out of the cloak curiously; Duban explaining with a gentle raised finger; sunlight shafts between the columns",
         camera="medium wide two-shot, eye level", amb="throne_hall", transition="black"),
    dict(to=56, reason="scene and action change: the king plays polo on horseback", chars=["king_yunan"], loc="polo",
         visual="soft golden storybook glow: King Yunan, cloak thrown back, in his purple robe and crowned turban, galloping on a splendid white horse across the green polo field, swinging the polo mallet towards the leather ball, his face flushed with excitement and sweat; a faint shimmer of green-gold sparkles flows from the mallet handle into his gripping hand; small background riders and pennants",
         camera="dynamic wide action shot, low angle, horse and king in the upper two-thirds, the grass in the lower third", amb="polo_field"),
    dict(to=57, reason="scene change: after the game the king bathes in hot water", chars=["king_yunan"], loc="bath",
         visual="soft golden storybook glow: in the royal marble bathhouse full of thick warm steam, King Yunan seen only from the shoulders up, wrapped in a thick white bath robe with a towel over his head instead of the turban, eyes closed in relief; beams of light through the steam; small background attendant holding folded towels",
         camera="medium close-up, shoulders up only, the steam filling the lower third", amb="memory", sens="clothing",
         safe="bathing shown as steam with the king robed, seen from the shoulders up only (bible rule 10)"),
    dict(to=60, reason="time jump: the next morning the king wakes completely cured", chars=["king_yunan"], loc="royal_bedroom",
         visual="soft golden storybook glow: King Yunan standing by the sunlit window in the morning in his purple robe, the grey cloak fallen at his feet, staring in wonder at his own clean, smooth hands held up in the golden sunbeams, tears of joy shining in his eyes and a trembling smile; tiny golden sparkles dancing in the light",
         camera="medium shot, eye level, his face and raised hands in the upper half", amb="memory", transition="black"),
    dict(to=62, reason="action change: the king honours Duban with robes, gold and a seat beside him", chars=["king_yunan", "sage_duban"], loc="darbar",
         visual="soft golden storybook glow: the healthy, beaming King Yunan on his golden throne gesturing warmly to the old sage Duban, who now sits on a cushioned seat of honour beside the throne wearing a splendid new robe of shimmering silk over his ochre robe; servants in modest robes bring a brass tray heaped with gold coins and folded silks; courtiers bowing",
         camera="wide shot, eye level, the throne dais in the upper two-thirds, the carpeted floor below", amb="throne_hall"),
    dict(to=65, reason="character change: the jealous vizier watches and plots", chars=["yunan_vizier", "sage_duban", "king_yunan"], loc="darbar",
         visual="soft golden storybook glow darkening at one side: in the foreground the thin jealous vizier half in shadow behind a marble column, empty-handed, glaring sideways with narrowed envious eyes and a tight scheming frown; in the bright background, small and far away, King Yunan laughing with the old sage Duban seated beside the throne",
         camera="medium shot, the vizier's face in the upper third at one side, deep focus to the throne", amb="throne_hall", sens="other",
         safe="the vizier's malice is only a look of envy; no violence"),
    # ---------------- FRAME: dawn ----------------
    dict(to=67, reason="scene change out of the tales: dawn light enters the chamber, Shahrazad stops and Dunyazad asks", chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber_dawn",
         visual="golden-pink dawn sunlight streams through the lattice window; Shahrazad on her cushion glancing towards the window and lowering her storytelling hand; Dunyazad on the carpet beside her tugging gently at her sister's sleeve with wide astonished eyes, asking for more; King Shahryar on the divan an arm's length or more away, fully dressed, leaning forward impatiently",
         camera="wide shot, eye level, the window light from behind", amb="palace_dawn", transition="dissolve"),
    dict(to=70, reason="emotional turning point: Shahrazad smiles and promises the rest tomorrow night", chars=["shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="close on Shahrazad smiling a calm mysterious smile, one finger raised gently as if to say 'tomorrow', her face lit by the warm golden dawn light from the lattice window; Dunyazad beside her looking up at her hopefully; behind them through the window the pink-gold sky and a distant minaret silhouette",
         camera="medium close-up, eye level, faces in the upper half", amb="palace_dawn"),
    dict(to=72, reason="character and scene change: the king spares her another day and goes to his court", chars=["shahryar"], loc="palace_hall_dawn",
         visual="King Shahryar, fully dressed, empty-handed, striding thoughtfully down the long marble corridor towards the open doors of his court, glancing back over his shoulder with a faint intrigued half-smile; golden dawn light through the lattice windows throws patterns across the floor",
         camera="medium wide shot from behind and to the side, the king in the upper two-thirds, the patterned floor as the lower third",
         amb="palace_dawn", sens="other",
         safe="the threat of execution is implied only by the king's thoughtful glance; no executioner or weapon"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The fisherman's trick and the tale of King Yunan. When the stillness of night had settled over the whole palace and the stars of dawn began to appear in the sky,")
sh(2, "Dunyazad called to her elder sister Shahrazad: \"Dear sister! If you are not asleep, please go on with the story of that poor fisherman and that terrifying great jinni.")
sh(3, "I am so impatient to hear whether that jinni killed the fisherman or whether he was saved.\"")
sh(4, "King Shahryar was also very eager to hear the rest of the story, and gave permission to continue it.")
sh(5, "Shahrazad began most politely: \"O noble and mighty king! I will begin from where the story was broken off last night.")
sh(6, "Last night I told some of how it happened. What happened was that, on hearing the exalted Name of God,")
sh(7, "the jinni started in fear and his huge body began to tremble. The jinni said: 'Yes! You have called upon a most exalted Name.",
   [("magic_shimmer", "ތުރުތުރު", -20)])
sh(8, "I will show you how this all happened.' 'I want to see how you lay inside this jar for many hundreds of years.")
sh(9, "I want to see it with my own eyes and make sure of it. I still say you are certainly lying.")
sh(10, "You did not come out of that jar. You came from the bottom of the sea.' That a human doubted the jinni's power this much was more than he could bear.")
sh(11, "So: 'Now I have shown your eyes the sight of me entering this jar. Now you will know my power!' Then the jinni spoke again:",
   [("smoke_whoosh", "ވަންނަ", -16)])
sh(12, "'O foolish fisherman! Do you believe it now? Just look. Here I am, inside this jar!")
sh(13, "Have you seen my power now?' Without wasting a single second, the fisherman quickly set the lead lid stamped with the seal of Sulaiman on the mouth of the jar and pressed it down hard.",
   [("metal_lid", "ބާރުކޮށްލިއެވެ", -14)])
sh(14, "The jar closed at once and the jinni was stuck inside it. The jinni struggled hard to get out of it.",
   [("soft_thud", "މަސައްކަތްކުރިއެވެ", -18)])
sh(15, "He knocked from inside the jar and tried to open the lid. But by the power of Sulaiman's holy seal he could not get out of it in any way.",
   [("knock", "ތަޅުވައި", -18), ("magic_shimmer", "ސިއްކައިގެ", -22)])
sh(16, "The lid was shut with such strength that no force could open it. The jinni realised his own foolishness and")
sh(17, "the fisherman's cunning, and lying inside the jar he began to weep loudly. His pride and arrogance were shattered at once.",
   [("sob_breath", "ރޯން", -20)], hum=True)
sh(18, "The fisherman picked up the jar and walked towards the sea behind him. From inside the jar the jinni called out: 'O kind fisherman!",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -18)])
sh(19, "What are you doing? Where are you going with that jar?'")
sh(20, "The fisherman answered: 'I am going to throw you back into the deepest part of the sea! Lie there until the Day of Judgement!",
   [("wave_crash", "އެއްލާލާށެވެ", -20)])
sh(21, "And I will warn everyone who comes to this shore that at the bottom of this sea lies an evil jinni full of the spirit of revenge,")
sh(22, "who will kill without mercy anyone who sets him free.")
sh(23, "It is my duty to save the world from your evil.' Weeping, the jinni began to plead: 'O my master! Forgive me!",
   [("sob_breath", "ރޮމުން", -20)], hum=True)
sh(24, "I only said those things to you as a joke. Forgive my foolishness!")
sh(25, "If you save me, I will make you rich for the rest of your life. I will bring happiness to your children!")
sh(26, "I will fulfil every wish you have.' The fisherman laughed and said: 'You are certainly lying. You are faithless.")
sh(27, "I will never trust a word of yours. Our case is like that of King Yunan and the Sage Duban. If I let you go,")
sh(28, "you will do to me what King Yunan did to the Sage Duban. You would surely kill me.'")
sh(29, "The jinni asked in surprise: 'What story is that? Who is King Yunan? And who is the Sage Duban?")
sh(30, "What happened between them? O fisherman, tell me that story before you throw me into the sea.")
sh(31, "I long to hear that story.' The fisherman sat down at the edge of the sea, set the jar in front of him,",
   [("wave_crash", "ކަނޑުގެ", -22)])
sh(32, "and began to tell the jinni the story. 'Listen! In olden times, in a great Persian kingdom, there lived a king named Yunan.",
   [("magic_shimmer", "ކުރީ", -22)])
sh(33, "He was immensely rich and powerful, and the lord of a great army. The king's power spread over many hundreds of islands.")
sh(34, "His palaces were built of the most precious gold and silver. But a very great sorrow and misfortune had come into his life.")
sh(35, "On the king's body had appeared the most dangerous of diseases, leprosy.")
sh(36, "White patches appeared all over his body and his skin decayed, until nobody even dared to come near him.")
sh(37, "Even after bringing the finest physicians and sages from every corner of the world and using many medicines and ointments, no cure was found for this disease.")
sh(38, "When the king, in utter despair, was on the verge of giving up his life, a very learned old sage came to that land.",
   hum=True)
sh(39, "His name was the Sage Duban. The Sage Duban was no ordinary man. He had mastered the Greek, Persian, Latin and Arabic languages perfectly.")
sh(40, "Besides that, he had read thousands of books on herbal medicine, the science of the stars, how the organs of the body work, and how to treat all kinds of disease, and had plunged to the depths of them all.")
sh(41, "When Duban heard of King Yunan's illness, he went to the palace to treat him. Presenting himself at the king's court,")
sh(42, "Duban said most politely: \"O noble king! I have heard of Your Majesty's illness.")
sh(43, "And I know the other physicians could not cure it. But, God willing, I will treat Your Majesty and cure you completely.")
sh(44, "And I will do it without giving you any bitter medicine to drink and without rubbing any medicine on your body.\"")
sh(45, "The king was utterly astonished to hear this. It was hard for him even to believe. \"How can that be?",
   [("gasp", "ޙައިރާން", -20)])
sh(46, "If you cure this terrible disease of mine without my eating or rubbing on any medicine, I will give you a great deal of wealth and money.")
sh(47, "And I will make you my closest friend.\" The Sage Duban went home and took out his books and medicines.",
   [("page_turn", "ފޮތްތަކާއި", -20)])
sh(48, "Most skilfully, he made a polo mallet. The inside of that mallet was empty and hollowed out. Then he prepared a very special,")
sh(49, "powerful medicine, poured it into the mallet and sealed the top. He also made a polo ball.",
   [("pour", "އަޅައި", -18)])
sh(50, "The next day Duban went to the king and presented the mallet and the ball. \"O king,\" Duban said.")
sh(51, "\"Mount your horse, go to the polo field, strike this ball with this mallet and play polo.")
sh(52, "When you play and your body begins to sweat, the medicine inside this mallet will pass through the skin of your hand into your body.")
sh(53, "When you finish playing, bathe at once and sleep to rest. Then all will be well.\"")
sh(54, "The king did just as Duban advised. Mounting his horse, he gripped the polo mallet and played with great excitement.",
   [("horse_hooves", "ސަވާރުވެވަޑައިގެން", -16)])
sh(55, "Holding the mallet, he galloped on his horse chasing the ball. His body began to sweat heavily.",
   [("horse_hooves", "ދުވެވަޑައިގަތެވެ", -16)])
sh(56, "Just as Duban had said, as his hand began to sweat, the power of the medicine inside the mallet")
sh(57, "spread through his skin into the blood of his body. After finishing the game, the king came to the palace, and after bathing in hot water,",
   [("water_splash_small", "ފެންވަރާ", -20)])
sh(58, "he lay down to rest. The next morning, when the king woke and looked at his body, a miracle he could hardly believe with his own eyes had happened.",
   [("magic_shimmer", "މުޢުޖިޒާތެއް", -20)], hum=True)
sh(59, "Every patch and every trace of the disease on his body had completely vanished. His skin was clean and fair like pure silver.",
   hum=True)
sh(60, "Not a single sign of the disease could be seen. The king wept for joy. At once he summoned the Sage Duban to the palace,",
   [("sob_breath", "ރޮވުނެވެ", -22)], hum=True)
sh(61, "gave him costly silk robes and made him rich with gold dinars. And he appointed Duban as his closest companion,",
   [("cloth_rustle", "ހެދުންތައް", -20)])
sh(62, "and gave him the honour of sitting beside the king at court. Every day he went on giving Duban new gifts. But,")
sh(63, "the king's happiness lasted only a short while. At the king's court there was a very wicked, jealous vizier.")
sh(64, "His heart had turned black. Seeing the esteem and respect the king was giving the Sage Duban, a great envy of Duban arose in that vizier's heart.",
   [("heartbeat", "ޙަސަދައެއް", -20)], hum=True)
sh(65, "He plotted by any means to ruin the Sage Duban and to bring him down in the king's eyes...'", hum=True)
sh(66, "When the fisherman's story had reached this point, Shahrazad noticed the light of the sun coming into the room, and she broke off the story at once.")
sh(67, "Dunyazad said in amazement: 'O sister! What a beautiful and exciting story! What did the jealous vizier do to the Sage Duban?'",
   [("gasp", "ޙައިރާން", -22)])
sh(68, "Shahrazad replied with a smile: 'The rest of that story is far more complete and wondrous. But dawn has come.")
sh(69, "Tomorrow night, if I am still in this world, I will tell you how that wicked vizier poisoned the king's mind,",
   hum=True)
sh(70, "the tragic fate that befell the Sage Duban because of it, and whether or not the fisherman threw that jinni into the sea.' King Shahryar,",
   hum=True)
sh(71, "being extremely eager to know what happened to the Sage Duban, decided to spare Shahrazad's life for one more day.")
sh(72, "And he went to the court of the palace to conduct the affairs of state for that day.\"",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -20)])
SHOTS = S

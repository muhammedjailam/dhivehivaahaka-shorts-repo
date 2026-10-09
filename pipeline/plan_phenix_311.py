"""Beat/shot plan for Project Phenix episode 311 (part 1; used by plan_beats.py)."""

KANDU = ("Kandu-huttaa, a deserted uninhabited island in Huvadhu (Gaafu Alifu) atoll: white sand beach, dense dark jungle "
         "of screwpine, magoo bushes and coconut palms, mangrove-like tangles reaching the water; no path, no people")
DHONI = ("a traditional Maldivian wooden fishing dhoni with a high curved bow, a small open wooden wheelhouse and a low engine "
         "housing, plain painted wooden hull with no writing, on the open sea off " + KANDU + " (the island a dark jungle "
         "silhouette in the distance)")

LOC = {
    "dhoni_sunset": DHONI,
    "dhoni_dusk": DHONI,
    "police_office": "the Serious Crimes Department office in Iskandhar Building, Malé: a cluttered desk with empty coffee cups "
                     "and stacks of unfinished case files with blank covers, a desktop computer, a window onto a busy street "
                     "(Ameenee Magu) with passing traffic",
    "naail_memory": "a seafront road in Malé at night, a sleek black sports car parked by the sea wall, coloured city lights "
                    "and building lights reflecting on the wet tarmac",
    "moosa_mansion": "Moosa's luxurious living room in Malé: polished marble floor, big cream leather sofas, dark wood panelling "
                     "and furniture, warm table lamps, heavy curtains",
    "sea_launch": "a police fast launch at speed on a rough dark sea at night: a sleek modern grey-and-navy patrol launch with a "
                  "raised cabin with windows, plain hull with no writing, numbers or name, white spray and a long white wake",
    "launch_cabin": "inside the cabin of the police fast launch at night: narrow padded seats, small square windows onto the "
                    "black sea, hard-shell forensic equipment cases stacked on the floor, a steering wheel and a navigation "
                    "screen at the front glowing with blurred shapes only, no readable digits",
    "kandu_lagoon": KANDU + "; a calm turquoise lagoon inside the reef",
    "kandu_beach": KANDU + "; the island's east-side beach where the sand meets the bushes",
    "kandu_jungle": KANDU + "; deep inside the dense untouched jungle, thick undergrowth and leaf litter on sandy ground, "
                    "nothing man-made in sight",
    "kandu_bunker": KANDU + "; deep inside the dense jungle a hidden spot of bent palms, piles of dry palm fronds and, half "
                    "buried in sand, a heavy rusted steel hatch-door set in a low concrete block in the ground among the bushes",
}
MOOD = {
    "dhoni_sunset": "sunset over the open sea, the sky streaked with blood-orange and crimson clouds, warm red-gold light on the "
                    "men's faces, long shadows, deep navy water, the first chill of dread",
    "dhoni_dusk": "the last red glow of dusk dying on the horizon, cold navy-blue darkness spreading over the sea, a single "
                  "warm lantern light on the dhoni, horror and shock",
    "police_office": "early evening in Malé, the last grey-blue daylight through the window with city lights coming on, a "
                     "flat fluorescent ceiling light and a warm desk lamp, tired and serious",
    "naail_memory": "a memory: night, soft dreamlike haze, neon-coloured city reflections, cool blue and magenta glow, slightly "
                    "blurred edges",
    "moosa_mansion": "night, warm amber table lamps in a dim luxurious room, deep shadows, heavy grief and silence",
    "sea_launch": "2 am, cold navy-blue darkness over a rough sea, faint moonlight, the launch's own small white navigation "
                  "lights, white spray glistening, tense",
    "launch_cabin": "2 am, a dark cabin lit only by the cold blue glow of a laptop and the faint green glow of the navigation "
                    "screen, black windows, sea spray on the glass, tense silence",
    "kandu_lagoon": "dawn, golden rays of the rising sun on the calm lagoon, pale gold sky, beautiful but eerily silent",
    "kandu_beach": "early morning, clear low golden sunlight, long shadows on white sand, eerie silence",
    "kandu_jungle": "early morning inside the jungle, shafts of golden light through dense leaves, green-brown shade, tense and "
                    "eerie",
    "kandu_bunker": "early morning inside the jungle, shafts of golden light through dense leaves, green-brown shade, tense and "
                    "eerie",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
HASSAN = "Hassan (an older weathered Maldivian fisherman with grey stubble, in a faded blue long-sleeved shirt and a checked sarong)"
SAMEERU = "Sameeru (a stocky middle-aged Maldivian fisherman-cook in a long-sleeved brown shirt and dark trousers)"
IBRAHIM = "Ibrahim (a lean Maldivian fisherman in his forties in a long-sleeved grey shirt and a sarong)"
ALI = "Ali (a young wiry Maldivian fisherman in his twenties in a long-sleeved green shirt and dark trousers)"
BUNDLE = "a large shapeless bundle made of thick black plastic bags wrapped round and round with wide black tape, closed"
PHOENIX = "a black phoenix emblem drawn on the tablet screen as a simple bird-of-fire line drawing, nothing else on the screen"
SOLDIERS = ("two Maldivian police officers in plain navy uniforms and two soldiers in plain black combat gear and helmets with "
            "no insignia, all with empty hands")

BEATS = [
    # ---------------- THE DHONI AT SUNSET
    dict(to=2, reason="episode opening: sunset, the dhoni Kalaminja rocking off the deserted island Kandu-huttaa", loc="dhoni_sunset",
         visual="a wide view of a lone traditional Maldivian fishing dhoni rocking gently on the open sea at sunset, the sky "
                "ablaze with red and orange clouds, the dark jungle silhouette of a deserted island on the horizon, four tiny "
                "fishermen figures aboard, the wind rising and ruffling the water",
         camera="wide establishing shot, slightly high angle, the sky and dhoni in the upper two-thirds, dark rippling water as the calm lower third",
         amb="sea_boat"),
    dict(to=4, reason="action change: Hassan at the bow spots a big black thing floating; Sameeru slows the engine", loc="dhoni_sunset",
         visual=f"{HASSAN} standing at the high curved bow of the dhoni, one arm stretched out pointing at the sea, squinting into "
                f"the sunset; far out on the water a black shapeless floating thing; behind him in the small wheelhouse {SAMEERU} "
                "leaning to look, one hand on the engine lever",
         camera=f"medium wide shot from the deck behind the men, eye level, {LOW} (the wooden deck in shadow)", amb="sea_boat"),
    dict(to=7, reason="characters enter: Ibrahim and Ali come to the bow; they argue whether to leave it", loc="dhoni_sunset",
         visual=f"four fishermen crowded at the bow of the dhoni at sunset looking down at the water: {HASSAN} pointing insistently "
                f"at a black floating bundle a few metres away with small fish circling it; {IBRAHIM} waving a dismissive hand; "
                f"{ALI} wrinkling his nose; {SAMEERU} frowning; red sunset light on their faces",
         camera=f"medium shot, eye level, the four faces in the upper two-thirds, {LOW} (dark water beside the hull)", amb="sea_boat"),
    dict(to=10, reason="action change: Hassan hooks it with a pole; four men haul the unnaturally heavy bundle aboard", loc="dhoni_sunset",
         visual=f"four Maldivian fishermen straining together to haul {BUNDLE} over the dhoni's wooden side onto the deck, faces "
                "grimacing with effort and disgust, Sameeru turning his face away, a long wooden boat pole with a hooked end lying "
                "on the deck, water streaming off the black plastic, red sunset behind them",
         camera=f"medium wide shot, eye level, {LOW} (wet wooden deck)", amb="sea_boat", sens="death",
         safe="the bundle is only a closed black taped plastic shape; nothing inside is ever suggested"),
    dict(to=12, reason="action change: Hassan works at the tape; the smell overwhelms them; Ali turns away at the rail", loc="dhoni_sunset",
         visual=f"on the dhoni deck {HASSAN} kneeling beside {BUNDLE}, his hands on the black tape; {IBRAHIM} and {SAMEERU} standing "
                f"back with their hands clamped over their noses and mouths; {ALI} turned completely away, bent over the far rail "
                "looking out to sea, his back to the viewer; the sun sinking low and red",
         camera=f"medium wide shot, slightly high angle, {LOW} (wooden deck in shadow)", amb="sea_boat", sens="death",
         safe="opening the bundle and Ali being sick are not shown: the bundle stays closed, Ali is seen only from behind at the rail"),
    # ---------------- THE DISCOVERY
    dict(to=15, reason="emotional turning point: Hassan sees what is inside — shown only as his face", loc="dhoni_dusk",
         visual=f"close-up of {HASSAN} recoiling backwards on his knees on the deck, eyes wide with horror, mouth open, one trembling "
                "hand raised in front of his mouth, his face lit red by the dying sunset; the bundle is completely out of frame "
                "below; behind him Ibrahim turning his head away in shock",
         camera=f"close-up, slightly low angle, his face in the upper two-thirds, {LOW} (dark deck shadow)", amb="sea_boat",
         sens="death", safe="the remains (leg, wounds) are never shown; only Hassan's horrified face lit by the sunset; the bundle is out of frame"),
    dict(to=17, reason="action change: Sameeru cries out and grabs the radio set; darkness falls over the sea", loc="dhoni_dusk",
         visual=f"{SAMEERU} in the small open wooden wheelhouse of the dhoni, gripping the handset of an old marine radio set and "
                "shouting into it with a panicked face, a lantern swinging above him; behind him the other fishermen as dark "
                "shapes on the deck (only four fishermen aboard in all, all men, no women anywhere on the dhoni); the last red glow on the horizon and night falling over the sea",
         camera=f"medium shot, eye level, {LOW} (dark water and deck)", amb="sea_boat"),
    # ---------------- MALÉ, ISKANDHAR BUILDING
    dict(to=21, reason="scene change: Malé, Ashham at his desk in the Serious Crimes office", chars=["ashham"], loc="police_office",
         visual="Ashham sitting at his cluttered office desk, leaning back with a tired but sharp gaze at his computer, empty "
                "coffee cups and stacks of unfinished case files with blank covers around him, a window behind him onto a busy "
                "Malé street with traffic lights blurring past",
         camera=f"medium shot, eye level, {LOW} (desk top with files and cups)", amb="office_day", transition="black"),
    dict(to=25, reason="character enters: Habeeb comes in with a message from the southern command", chars=["habeeb", "ashham"], loc="police_office",
         visual="Habeeb stepping in through the office door holding a tablet, his face serious behind his glasses; Ashham at his "
                "desk turning his chair towards him with a questioning look; the computer screen glowing with blurred shapes only",
         camera=f"medium wide shot, eye level, {LOW} (office floor and desk edge)", amb="office_day"),
    dict(to=29, reason="action change: Ashham frowns, understands it is a 'message' killing, and stands up", chars=["ashham", "habeeb"], loc="police_office",
         visual="Ashham rising from his chair behind the desk, both hands on the desk top, his brows knotted in grim concentration; "
                "Habeeb standing opposite holding the tablet to his chest, grave",
         camera=f"medium shot, eye level, {LOW} (desk top with files)", amb="office_day",
         sens="violence", safe="the described torture is only spoken; the image shows the two men's grave faces"),
    dict(to=31, reason="detail: the photo on Habeeb's tablet — the phoenix mark", chars=["habeeb"], loc="police_office",
         visual=f"close-up of Habeeb's hands holding a tablet towards the viewer: on its screen {PHOENIX}; Habeeb's serious face "
                "softly out of focus above it",
         camera=f"close-up over the desk, eye level, the tablet in the upper two-thirds, {LOW} (desk top)", amb="office_day",
         sens="death", safe="the tattoo on the back of the deceased is never shown; only a black phoenix emblem drawn on a tablet screen"),
    dict(to=33, reason="memory: Ashham recalls who Naail Moosa was — a young man of Malé's night life and car races", chars=["naail"], loc="naail_memory",
         visual="Naail as Ashham remembers him, alive and cocky: leaning against a sleek black sports car on a Malé seafront road "
                "at night, arms folded, a restless half smile, city lights glowing behind him",
         camera=f"medium shot, eye level, {LOW} (wet tarmac reflections)", amb="memory", transition="dissolve"),
    dict(to=37, reason="back to the office: Ashham names Naail and gives orders", reuse="beat_010", chars=["ashham", "habeeb"],
         loc="police_office", visual="reuse of beat_010", amb="office_day", transition="dissolve"),
    # ---------------- MOOSA'S MANSION
    dict(to=39, reason="scene change: Moosa's mansion — a broken father on the sofa", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="a wide luxurious living room at night: Moosa sitting alone on a big cream leather sofa with his head bowed and his "
                "hands hanging between his knees, shattered; Ashham standing a few steps away near the door, looking at him gravely",
         camera=f"wide shot, eye level, {LOW} (polished marble floor)", amb="mansion_night", transition="black"),
    dict(to=44, reason="action change: Ashham sits down opposite Moosa and questions him about Naail", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="Ashham sitting forward in an armchair opposite Moosa, elbows on his knees, listening intently; Moosa on the sofa "
                "speaking with a trembling voice, eyes red behind his gold glasses, one hand raised helplessly; on the side table "
                "beside Moosa a small framed photograph of a smiling young man",
         camera=f"medium shot from the side, eye level, {LOW} (low coffee table and marble floor)", amb="mansion_night"),
    dict(to=47, reason="emotional turning point: Moosa weeps and begs; Ashham stands and puts a hand on his shoulder", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="Moosa weeping on the sofa, his face crumpled with grief, a hand pressed to his eyes under his gold glasses; Ashham "
                "standing beside him with one hand resting on Moosa's shoulder, looking down with a hard, determined face",
         camera=f"medium close shot, eye level, {LOW} (sofa and floor in shadow)", amb="mansion_night"),
    # ---------------- THE SEA HAWK, 2 AM
    dict(to=49, reason="time and scene change: 2 am, the fast launch leaves Kooddoo towards Kandu-huttaa", loc="sea_launch",
         visual="a sleek police fast launch racing across a rough black sea at night, its bow lifting over a wave, white spray "
                "flying, a long white wake behind it, small white navigation lights, the dark horizon",
         camera="wide shot, low angle near the water, the launch in the upper two-thirds, dark churning water as the calm lower third",
         amb="sea_boat", transition="black"),
    dict(to=55, reason="scene change: inside the cabin — Ashham and Habeeb silent beside the forensic cases; Habeeb opens his laptop",
         chars=["habeeb", "ashham"], loc="launch_cabin",
         visual="inside the dark launch cabin, Habeeb sitting with an open laptop on his knees, its cold blue glow on his glasses "
                "and face (the screen angled away from the viewer), turning to speak; Ashham sitting beside him, arms folded, "
                "listening hard; hard-shell forensic cases stacked at their feet; black windows with sea spray",
         camera=f"medium shot, eye level, {LOW} (cabin floor with the cases in shadow)", amb="sea_boat"),
    dict(to=58, reason="action change: Ashham looks out of the window into the darkness — the most dangerous case of his life", chars=["ashham"], loc="launch_cabin",
         visual="Ashham's profile close to a small square cabin window, staring out into the pitch-black sea, his face faintly lit "
                "by the blue glow from inside, sea spray streaking the glass, his own dim reflection in it, deep in thought",
         camera=f"close-up profile, eye level, {LOW} (dark window sill)", amb="sea_boat"),
    dict(to=60, reason="character change: the launch captain reports half an hour to Kandu-huttaa; Ashham gives orders", chars=["ashham"], loc="launch_cabin",
         visual="a middle-aged Maldivian launch captain in a light-grey long-sleeved shirt at the wheel, glancing back over his "
                "shoulder; Ashham standing behind him with one hand on the cabin roof rail, pointing ahead through the windscreen "
                "into the dark, giving orders; the navigation screen glowing with blurred shapes",
         camera=f"medium shot from the back of the cabin, eye level, {LOW} (dark cabin floor)", amb="sea_boat"),
    dict(to=61, reason="back to the launch cutting through the big waves", reuse="beat_017", loc="sea_launch",
         visual="reuse of beat_017", amb="sea_boat"),
    # ---------------- KANDU-HUTTAA AT DAWN
    dict(to=64, reason="time and scene change: dawn, the launch enters the lagoon of the beautiful, silent island", loc="kandu_lagoon",
         visual="the police fast launch gliding slowly into a calm turquoise lagoon at dawn, golden sunrays across the water, ahead "
                "a beautiful deserted island with a pure white sand beach and a wall of dense dark jungle, screwpine and coconut "
                "palms, tangled bushes reaching down into the water; no path, no people on the island, eerie stillness; aboard the launch only a few men seen from behind (Maldivian policemen in navy field uniforms and two soldiers in plain black combat gear and helmets), all men, no women",
         camera="wide shot from behind the launch, eye level, the island and sky in the upper two-thirds, smooth lagoon water as the calm lower third",
         amb="dawn_exterior", transition="black"),
    dict(to=66, reason="action change: Ashham and Habeeb step ashore with forensic kits, police and two soldiers behind them",
         chars=["ashham", "habeeb"], loc="kandu_beach",
         visual=f"Ashham and Habeeb wading the last steps from the shallows onto the white sand beach carrying hard-shell forensic "
                f"cases, Ashham scanning the jungle edge; behind them, further back near the launch, {SOLDIERS}",
         camera=f"medium wide shot, eye level, {LOW} (wet white sand)", amb="island_day"),
    dict(to=70, reason="action change: on the east side Ashham finds boot prints and bare footprints; Habeeb rubs oily sand between two fingers",
         chars=["ashham", "habeeb"], loc="kandu_beach",
         visual="Ashham crouching on the sand studying a trail of large boot prints and a few bare footprints coming out of the "
                "bushes; beside him Habeeb crouching over a dark oily stain in the sand, rubbing a pinch of sand between two "
                "fingers with a sharp look",
         camera=f"medium shot, slightly high angle, {LOW} (the footprints in the sand)", amb="island_day"),
    dict(to=72, reason="action change: Ashham takes a broken twig as evidence — this is the crime scene", chars=["ashham"], loc="kandu_beach",
         visual="close-up of Ashham at the edge of the bushes carefully placing a small broken dry twig into a clear plastic "
                "evidence bag, his jaw set, eyes hard; the dark jungle behind him",
         camera=f"close-up, eye level, his face and hands in the upper two-thirds, {LOW} (sand in soft shadow)", amb="island_day",
         sens="violence", safe="the dried blood on the branches is not shown; only Ashham bagging a plain twig as evidence"),
    dict(to=74, reason="scene change: into the jungle; a hidden spot with palms bent and bound together", chars=["ashham", "habeeb"], loc="kandu_jungle",
         visual="Ashham pushing his way through dense jungle leaves with Habeeb close behind, a police officer further back; ahead "
                "of them two young palm trunks unnaturally bent low and held together with frayed palm-fibre twine; Ashham "
                "reaching out to pull them apart; nothing else on the ground but leaf litter and sand, no door, no hatch, no concrete",
         camera=f"medium shot, eye level, {LOW} (leaf litter on the ground)", amb="island_day"),
    dict(to=77, reason="action change: a pile of dry fronds — 'a rubbish pit?' — Ashham orders it cleared", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="in a small clearing a big heap of dry brown palm fronds and dead branches; Ashham dragging a large dry frond off "
                "the heap with both hands, determined; Habeeb beside him bending to pull another branch away, sand showing beneath",
         camera=f"medium wide shot, eye level, {LOW} (sand and dry fronds)", amb="island_day"),
    dict(to=80, reason="emotional turning point: under the sand a heavy steel bunker door with a big padlock", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="a heavy rusted steel hatch-door set in a low concrete block in the ground, half uncovered from the sand among the "
                "bushes, a big old padlock on it; Ashham crouching beside it with one palm flat on the cold steel, staring at it; "
                "Habeeb standing behind him, wide-eyed with astonishment, pushing his glasses up",
         camera=f"medium shot, slightly high angle, faces in the upper two-thirds, the door in the middle, {LOW} (sand)", amb="island_day"),
    dict(to=82, reason="action change: the roar of an approaching launch — they hide in the bushes", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="Ashham and Habeeb crouched low among thick jungle leaves, peering out tensely towards the bright lagoon beyond the "
                "trees, where a fast dark launch with a white bow wave is speeding towards the island; behind them a police officer "
                "and a soldier in black combat gear crouched behind big tree trunks with empty hands",
         camera=f"medium shot from behind the leaves, eye level, {LOW} (dark leaf litter)", amb="island_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The sun is setting. Outside the deserted island called 'Kandu-huttaa' in the north of Huvadhu atoll, the dhoni 'Kalaminja' rocks gently from side to side.")
sh(2, "The sky is spread with the fading colours of the red clouds. The wind grows stronger and the swell slowly rises.",
   [("wind_gust", "ވައިރޯޅި", -20)])
sh(3, "It was then that Hassan, standing at the bow of the dhoni, noticed a big black thing floating far away. \"Hey! What is that thing floating there?\"")
sh(4, "Hassan called out. Sameeru the cook slowed the dhoni's engine and looked where Hassan pointed. It was a big black bag.",
   [("dhoni_engine", "އިންޖީނު", -18)])
sh(5, "Or something made of two or three big bags tied together. The other two fishermen on the dhoni, Ibrahim and Ali, also came to the bow.",
   [("footsteps_pavement", "ދިރުނބާކޮޅަށް", -24)])
sh(6, "\"That must be a rubbish bag thrown out from some resort,\" said Ibrahim. \"Leave it and let's go.\"")
sh(7, "\"No, look, there are strange fish around it. And it seems to give off a strange smell,\" said Hassan.")
sh(8, "He picked up a hooked pole lying on the dhoni and pulled the bag close to the dhoni. As the bag hit the dhoni's hull,",
   [("splash", "ދަމާލިއެވެ", -18), ("soft_thud", "ޖެހުމާއެކު", -18)])
sh(9, "everyone could tell it was unnaturally heavy. With it rose a foul stench hard to bear. Sameeru, shaking his head,")
sh(10, "helped to lift it onto the dhoni. Four men together hauled the heavy bag over the side. It was sealed with thick plastic bags and wound round with wide black tape.",
   [("soft_thud", "އެތެރެކުރިއެވެ", -18)])
sh(11, "Hassan took a cutter and began cutting the tape. As the first bag was cut open, the stench grew far stronger.",
   [("cloth_rustle", "ޓޭޕްތައް", -20)])
sh(12, "Everyone involuntarily put their hands to their noses. Ali leaned over the side and began retching into the sea. \"Is this... is this the meat of some animal?\"")
sh(13, "Ibrahim asked. Hassan cut the second layer of the bag. At the sight that appeared from inside, he almost lost his senses.",
   [("gasp", "ފެނުނު", -18)], hum=True)
sh(14, "It was part of a human leg, swollen and white from the salt. With trembling hands Hassan cut the whole bag open.",
   [("heartbeat", "ތުރުތުރު", -20)], hum=True)
sh(15, "It was the body of a man killed mercilessly. He had been tortured badly. There were deep wounds on the neck. \"Ya Rabbi!",
   hum=True)
sh(16, "What kind of cruelty is this!\" Sameeru cried out. \"Quick, call the police! Switch on the set!\" As this terror spread through the dhoni,",
   [("flashlight_click", "ސެޓުހުޅުވާ", -20)])
sh(17, "the pitch darkness of night was taking over the whole sea. The capital Malé, Iskandhar Building:",
   [("wind_gust", "އަނދިރިކަން", -22)])
sh(18, "In the office of the police Serious Crimes Department in Iskandhar Building in Malé, Ashham sat at his desk.")
sh(19, "Ashham is a tall, strong, sharp man. He is one of the police's most capable investigators.")
sh(20, "He is a policeman famous for solving the most dangerous crimes in Malé. On his desk were empty coffee cups and")
sh(21, "the files of several unfinished cases. From outside came the sound of vehicles racing along Ameenee Magu.",
   [("car_pass", "ވެހިކަލްތަކުގެ", -22)])
sh(22, "Ashham sat staring at the computer screen. The office door opened and in came Habeeb.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(23, "Habeeb is one of the best in the Maldives at data analysis and digital forensics. \"Sir, a message just came from the southern command,\"")
sh(24, "Habeeb's face showed seriousness. \"This is not an ordinary case.\" \"What is it?\" Ashham asked, settling in his chair. \"GA.",
   [("creak", "ހަމަޖެހިލަމުން", -22)])
sh(25, "A man has been found dead near a deserted island. With big wounds — a straight torture, brutal murder; some limbs even cut off...\"")
sh(26, "Habeeb read out the report. Ashham's brows knotted. Murders do happen in the Maldives.")
sh(27, "But killing people this cruelly, as Habeeb described, mercilessly cutting off parts of the body, is not common.")
sh(28, "Ashham realised this was done as a direct message. \"Where is the body now?\" Ashham stood up.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(29, "\"They're bringing it to Villingili in that atoll. Headquarters wants you to handle this case directly, sir.")
sh(30, "The reason is a tattoo on the back of that body,\" said Habeeb, showing a photo on his tablet.",
   [("computer_beep", "ދައްކާލިއެވެ", -24)])
sh(31, "The photo was taken by the fishermen of the dhoni that found the dead man. On the back of the dead, swollen body was a tattoo of a black phoenix bird.",
   hum=True)
sh(32, "On seeing that tattoo Ashham remembered Naail Moosa, the younger son of Moosa Thaahir, one of Malé's most influential businessmen.")
sh(33, "Naail was a young man of Malé's youth nightlife and big car races, and was suspected of drugs.",
   [("car_pass", "ކާރު", -20)])
sh(34, "\"This is Naail,\" Ashham said slowly. \"He's been missing for a week now. His father poured money in every direction in Malé trying to find him.\"")
sh(35, "\"Yes, sir. If this is Naail, this is not just a gang fight. There is a big secret behind it,\" said Habeeb.")
sh(36, "Ashham stood up. \"Habeeb, prepare the trip. And gather Naail's medical records and the records of the crimes he was suspected of.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(37, "We have to leave tonight.\" The wealthy father's tears: before leaving for the south, Ashham wanted to meet Moosa Thaahir.")
sh(38, "Moosa sat in the great hall of his wealthy house, where all one could see was luxury and plenty. In the middle of that wealth sat a despairing,")
sh(39, "broken father. Moosa sat on the sofa with his head bowed. \"Ashham, my son... is it really him?\"")
sh(40, "Qaasim's voice was trembling. \"Until the DNA is done it is hard to say anything for certain.")
sh(41, "But the tattoo on the back matches,\" Ashham said, sitting down. \"Moosa, was Naail involved in anything dangerous lately?")
sh(42, "Who in Malé did he get into trouble with?\" Moosa shook his head. \"He was always a boy who went around with bad friends.")
sh(43, "But two weeks ago I noticed he was very frightened. He said he had found out a big secret. But... he didn't give much detail.\"")
sh(44, "\"What secret?\" Ashham asked at once. \"That... that he didn't say. But he said those people are in Malé too.")
sh(45, "Ashham, find the people who killed my son. I will make any sacrifice,\" Moosa said, weeping.",
   [("sob_breath", "ރޮމުން", -20)], hum=True)
sh(46, "Ashham stood and put his hand on Moosa's shoulder. As far as he understood, Naail was not killed only for revenge.",
   [("cloth_rustle", "އަތްޖަހާލިއެވެ", -22)])
sh(47, "The meaning of what was done to him was: \"Say nothing.\" And \"Touch nothing.\" Or \"Reveal nothing.\"")
sh(48, "That was it. This was a warning. Straight onto the sea: it is two in the morning. The police's fastest modern launch, 'Sea Hawk', left Kooddoo harbour at speed.",
   [("boat_engine", "ދުއްވާލިއެވެ", -14)])
sh(49, "Carrying Ashham's team, who had flown into Kooddoo airport, the launch heads for the area of Kandu-huttaa. The sea is rough.",
   [("wave_crash", "ގަދައެވެ", -18)])
sh(50, "As the launch sped over the waves, Ashham and Habeeb sat in silence. Beside them were the forensic cases.")
sh(51, "Some members of the investigation team and extra police were already in that area. A backup team and a team of soldiers ready to help were also standing by for a signal.")
sh(52, "\"Habeeb, did you check the last locations of Naail's phone?\" Ashham asked. Opening his laptop, Zayaan said, \"Yes, sir.",
   [("keyboard_typing", "ލެޕްޓޮޕް", -22)])
sh(53, "His phone went dead in Malé a week ago. But before that he had called numbers on various islands in the south.")
sh(54, "He called one number especially often. It's a number of that atoll's hospital.\" \"A hospital!\" Ashham thought.")
sh(55, "\"Naail wasn't a sick man. Why would he need to call a hospital?\" \"I'm working on finding out who uses that number.")
sh(56, "But that island's systems are blocked,\" said Habeeb. Ashham looked out of the launch's small window.")
sh(57, "Nothing could be seen in the darkness of the sea. He felt that this would be the most dangerous and unusual case he would ever face in his life.",
   hum=True)
sh(58, "What could this secret be, hidden between Malé's wealth and the emptiness of the islands?")
sh(59, "\"Sir, it'll take about another half hour to reach Kandu-huttaa,\" said the launch captain. \"Good. We go to that island first.")
sh(60, "We must check the area where the fishermen picked up the body. We must see whether anything else is there,\" Ashham ordered. With the sound of the launch's engine,",
   [("boat_engine", "އިންޖީނުގެ", -16)])
sh(61, "they went on cutting through the great waves of the sea. That was the beginning. The truth of Kandu-huttaa: the light of dawn spread and the sun's golden rays began to fall on the sea's surface.",
   [("wave_crash", "ރާޅުތައް", -18)])
sh(62, "The 'Sea Hawk' entered Kandu-huttaa's lagoon. It is a naturally beautiful, charming island. Yet a deserted island ruled by a frightening silence.",
   [("boat_engine", "ފަޅަށް", -22)])
sh(63, "Around the island is a clean white sand beach. At the edge of the vegetation are dense screwpine and magoo bushes.")
sh(64, "In some places the bushes have grown thick and run from the beach down to the water's edge. As seen from the shore, the island's vegetation is very dense.")
sh(65, "It is a jungle island. There is no trace of a human being. No path into the island can be seen. Ashham and Habeeb stepped ashore with forensic kits.",
   [("footsteps_sand", "ފޭބިއެވެ", -18)])
sh(66, "Extra police and two soldiers with weapons were with them to help. According to the fishermen, the bag they found had floated outside the reef on the east side of the island.")
sh(67, "Ashham began walking, looking at the island's sand. \"Habeeb, come this way,\" Ashham called.",
   [("footsteps_sand", "ހިނގަން", -20)])
sh(68, "From among the bushes there were big footprints in the sand. They were the marks of boots. There were also some prints of bare feet.")
sh(69, "Not far from the footprints, there were signs of black oil dripped onto the ground. \"This is a launch's engine oil,\"")
sh(70, "Habeeb said, picking up sand from where the oil was and rubbing it between two fingers. \"Sir, what is this on these bushes?\"")
sh(71, "On some branches there were bloodstains. They had dried. Ashham took a twig from there and put it in a bag.",
   [("cloth_rustle", "ކޮތަޅަކަށްލިއެވެ", -20)])
sh(72, "\"It looks like Naail wasn't killed at sea. He was killed on this island. This is the crime scene.\" Ashham went into the bushes.",
   [("leaves_rustle", "ވަދެގެން", -18)], hum=True)
sh(73, "The team members came with him too. After going some way, they found a place that seemed to be hidden among the thick bushes.")
sh(74, "Two or three trees had been bent down and tied. Ashham cut the cord that bound them. There was nothing.",
   [("leaves_rustle", "ބުރިކޮށްލިއެވެ", -18)])
sh(75, "Dry palm fronds and dried branches lay piled in a heap. \"Sir, a rubbish pit,\" said Habeeb. \"No! ...")
sh(76, "Why would there be such a big rubbish pit on a deserted island? Who, which people... Clear these branches, dig this place up.\"")
sh(77, "Ashham said, pulling away a dried branch. His thinking was right. From the dug-up sand appeared a steel door.",
   [("leaves_rustle", "ދުރަށްލަމުން", -16)], hum=True)
sh(78, "A heavy door. It was the door of a concrete bunker built to go deep into the ground. A big padlock was on the door. \"A bunker on a deserted island?\"",
   [("metal_clang", "ތަޅެއް", -22)], hum=True)
sh(79, "Habeeb said in amazement. \"This is no ordinary deserted island,\" Ashham said, touching the bunker door.")
sh(80, "\"This is a place where a huge crime is run. This is the secret Naail found.\" At that moment came the sound of a launch approaching at high speed.",
   [("boat_engine", "ލޯންޗެއް", -14)], hum=True)
sh(81, "Ashham and Zayaan instantly hid among the bushes. The other police also took cover carefully behind big trees.",
   [("leaves_rustle", "ނިވާވިވެ", -18)])
sh(82, "The soldiers, weapons ready, stood alert. Someone knew the police had come to this island. And those people were now coming after them. — To be continued in part 2 —",
   [("heartbeat", "ސަމާލުވެލިއެވެ", -20)], hum=True)
SHOTS = S

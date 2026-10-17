"""Beat/shot plan for Project Phenix episode 311 v2 (re-cut on the new audio; v1 plan in output/ProjectPhenix/v1/plans/).
v1="beat_###" = image copied from the v1 render; NEW beats = spec 5.4 speaker framing."""

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
    dict(to=2, v1="beat_001", reason="episode opening: sunset, the dhoni Kalaminja rocking off the deserted island Kandu-huttaa", loc="dhoni_sunset",
         visual="a wide view of a lone traditional Maldivian fishing dhoni rocking gently on the open sea at sunset, the sky "
                "ablaze with red and orange clouds, the dark jungle silhouette of a deserted island on the horizon, four tiny "
                "fishermen figures aboard, the wind rising and ruffling the water",
         camera="wide establishing shot, slightly high angle, the sky and dhoni in the upper two-thirds, dark rippling water as the calm lower third",
         amb="sea_boat"),
    dict(to=3, speaker="hassan", reason="5.4 dialogue: Hassan calls out 'Hey! What is that floating?' — in the v1 bow image his face is a profile at the "
         "edge; new image framed on Hassan speaking", loc="dhoni_sunset",
         visual=f"{HASSAN} at the high curved bow of the dhoni, half-turned back towards the deck and the viewer so his face is "
                "seen in three-quarter view, mouth open calling out urgently, eyebrows raised in alarm, one arm stretched out "
                "behind him pointing over the water where, far out on the red-gold sea, a small black shapeless thing is floating; "
                "the other fishermen are out of frame",
         camera=f"medium close-up from the deck, eye level, Hassan centred in the upper half, his face sharp, the sunset sky and sea "
                f"softly blurred behind him, {LOW} (dark water)", amb="sea_boat"),
    dict(to=4, v1="beat_002", reason="action change: Hassan at the bow points out the black thing; Sameeru slows the engine", loc="dhoni_sunset",
         visual=f"{HASSAN} standing at the high curved bow of the dhoni, one arm stretched out pointing at the sea, squinting into "
                f"the sunset; far out on the water a black shapeless floating thing; behind him in the small wheelhouse {SAMEERU} "
                "leaning to look, one hand on the engine lever",
         camera=f"medium wide shot from the deck behind the men, eye level, {LOW} (the wooden deck in shadow)", amb="sea_boat"),
    dict(to=6, v1="beat_003", reason="characters enter: Ibrahim and Ali come to the bow; Ibrahim says to leave it", loc="dhoni_sunset",
         visual=f"four fishermen crowded at the bow of the dhoni at sunset looking down at the water: {HASSAN} pointing insistently "
                f"at a black floating bundle a few metres away with small fish circling it; {IBRAHIM} waving a dismissive hand; "
                f"{ALI} wrinkling his nose; {SAMEERU} frowning; red sunset light on their faces",
         camera=f"medium shot, eye level, the four faces in the upper two-thirds, {LOW} (dark water beside the hull)", amb="sea_boat"),
    dict(to=7, reuse="beat_002", reason="5.4 reverse shot: back to Hassan speaking (fish circling it, a strange smell)", loc="dhoni_sunset",
         visual="reuse of beat_002", amb="sea_boat", transition="cut"),
    dict(to=10, v1="beat_004", reason="action change: Hassan hooks it with a pole; four men haul the unnaturally heavy bundle aboard", loc="dhoni_sunset",
         visual=f"four Maldivian fishermen straining together to haul {BUNDLE} over the dhoni's wooden side onto the deck, faces "
                "grimacing with effort and disgust, Sameeru turning his face away, a long wooden boat pole with a hooked end lying "
                "on the deck, water streaming off the black plastic, red sunset behind them",
         camera=f"medium wide shot, eye level, {LOW} (wet wooden deck)", amb="sea_boat", sens="death",
         safe="the bundle is only a closed black taped plastic shape; nothing inside is ever suggested"),
    dict(to=11, v1="beat_005", reason="action change: Hassan works at the tape; the smell overwhelms them; Ali turns away at the rail", loc="dhoni_sunset",
         visual=f"on the dhoni deck {HASSAN} kneeling beside {BUNDLE}, his hands on the black tape; {IBRAHIM} and {SAMEERU} standing "
                f"back with their hands clamped over their noses and mouths; {ALI} turned completely away, bent over the far rail "
                "looking out to sea, his back to the viewer; the sun sinking low and red",
         camera=f"medium wide shot, slightly high angle, {LOW} (wooden deck in shadow)", amb="sea_boat", sens="death",
         safe="opening the bundle and Ali being sick are not shown: the bundle stays closed, Ali is seen only from behind at the rail"),
    dict(to=13, speaker="ibrahim", reason="5.4 dialogue: Ibrahim asks 'is this some animal's meat?' — in the v1 image he is at the far left edge; "
         "new image framed on Ibrahim", loc="dhoni_sunset",
         visual=f"{IBRAHIM} standing on the dhoni deck, the back of one hand held just under his nose, grimacing with disgust and "
                "unease, looking down at something out of frame below and asking a question, his face in three-quarter view and "
                f"clearly visible; beside him, softer and at the side, {SAMEERU} with a hand over his mouth; in the soft background "
                f"{ALI} bent over the far rail seen only from behind; nothing on the deck is visible, the low red sun behind them",
         camera=f"medium close-up, eye level, Ibrahim centred in the upper half and sharp, the others soft at the side, {LOW} "
                "(wooden deck in shadow)", amb="sea_boat", sens="death",
         safe="nothing of the bundle or its contents is shown; Ali being sick is shown only as his back at the rail"),
    # ---------------- THE DISCOVERY
    dict(to=15, v1="beat_006", reason="emotional turning point: Hassan sees what is inside — shown only as his face", loc="dhoni_dusk",
         visual=f"close-up of {HASSAN} recoiling backwards on his knees on the deck, eyes wide with horror, mouth open, one trembling "
                "hand raised in front of his mouth, his face lit red by the dying sunset; the bundle is completely out of frame "
                "below; behind him Ibrahim turning his head away in shock",
         camera=f"close-up, slightly low angle, his face in the upper two-thirds, {LOW} (dark deck shadow)", amb="sea_boat",
         sens="death", safe="the remains (leg, wounds) are never shown; only Hassan's horrified face lit by the sunset; the bundle is out of frame"),
    dict(to=17, v1="beat_007", reason="action change: Sameeru cries out and grabs the radio set; darkness falls over the sea", loc="dhoni_dusk",
         visual=f"{SAMEERU} in the small open wooden wheelhouse of the dhoni, gripping the handset of an old marine radio set and "
                "shouting into it with a panicked face, a lantern swinging above him; behind him the other fishermen as dark "
                "shapes on the deck (only four fishermen aboard in all, all men, no women anywhere on the dhoni); the last red glow on the horizon and night falling over the sea",
         camera=f"medium shot, eye level, {LOW} (dark water and deck)", amb="sea_boat"),
    # ---------------- MALÉ, ISKANDHAR BUILDING
    dict(to=22, v1="beat_008", reason="scene change: Malé, Ashham at his desk in the Serious Crimes office", chars=["ashham"], loc="police_office",
         visual="Ashham sitting at his cluttered office desk, leaning back with a tired but sharp gaze at his computer, empty "
                "coffee cups and stacks of unfinished case files with blank covers around him, a window behind him onto a busy "
                "Malé street with traffic lights blurring past",
         camera=f"medium shot, eye level, {LOW} (desk top with files and cups)", amb="office_day", transition="black"),
    dict(to=23, v1="beat_009", reason="character enters: Habeeb comes in with a message from the southern command", chars=["habeeb", "ashham"], loc="police_office",
         visual="Habeeb stepping in through the office door holding a tablet, his face serious behind his glasses; Ashham at his "
                "desk turning his chair towards him with a questioning look; the computer screen glowing with blurred shapes only",
         camera=f"medium wide shot, eye level, {LOW} (office floor and desk edge)", amb="office_day"),
    dict(to=26, speaker="habeeb", reason="5.4 dialogue: Habeeb reports the message from the south — in the v1 images he is at the frame edge; "
         "new over-the-shoulder image framed on Habeeb (used again for his later lines)", chars=["habeeb", "ashham"], loc="police_office",
         visual="seen over Ashham's shoulder: Habeeb standing across the cluttered desk holding his tablet against his chest, "
                "speaking urgently with a grave, serious face behind his glasses, his face in three-quarter view and sharp; in the "
                "soft out-of-focus foreground at the right edge only the back of Ashham's head and his navy shoulder; the tablet "
                "screen faces Habeeb and is not visible; the window behind Habeeb with blurred city lights",
         camera=f"over-the-shoulder medium close-up, eye level, Habeeb centred in the upper half and sharp, Ashham soft at the "
                f"foreground edge, {LOW} (desk top with files and cups)", amb="office_day", sens="violence",
         safe="the described torture is only spoken; the image shows Habeeb's grave face"),
    dict(to=28, v1="beat_010", reason="action change: Ashham frowns, understands it is a 'message' killing, and stands up", chars=["ashham", "habeeb"], loc="police_office",
         visual="Ashham rising from his chair behind the desk, both hands on the desk top, his brows knotted in grim concentration; "
                "Habeeb standing opposite holding the tablet to his chest, grave",
         camera=f"medium shot, eye level, {LOW} (desk top with files)", amb="office_day", transition="cut",
         sens="violence", safe="the described torture is only spoken; the image shows the two men's grave faces"),
    dict(to=29, reuse="beat_013", reason="5.4 reverse shot: Habeeb answers (the body is being taken to Villingili)", chars=["habeeb", "ashham"],
         loc="police_office", visual="reuse of beat_013", amb="office_day", transition="cut"),
    dict(to=31, v1="beat_011", reason="detail: the photo on Habeeb's tablet — the phoenix mark", chars=["habeeb"], loc="police_office",
         visual=f"close-up of Habeeb's hands holding a tablet towards the viewer: on its screen {PHOENIX}; Habeeb's serious face "
                "softly out of focus above it",
         camera=f"close-up over the desk, eye level, the tablet in the upper two-thirds, {LOW} (desk top)", amb="office_day",
         sens="death", safe="the tattoo on the back of the deceased is never shown; only a black phoenix emblem drawn on a tablet screen"),
    dict(to=33, v1="beat_012", reason="memory: Ashham recalls who Naail Moosa was — a young man of Malé's night life and car races", chars=["naail"], loc="naail_memory",
         visual="Naail as Ashham remembers him, alive and cocky: leaning against a sleek black sports car on a Malé seafront road "
                "at night, arms folded, a restless half smile, city lights glowing behind him",
         camera=f"medium shot, eye level, {LOW} (wet tarmac reflections)", amb="memory", transition="dissolve"),
    dict(to=34, reuse="beat_014", reason="back to the office: Ashham names Naail (5.4: crop on Ashham)", chars=["ashham", "habeeb"],
         loc="police_office", visual="reuse of beat_014", amb="office_day", transition="dissolve"),
    dict(to=35, reuse="beat_013", reason="5.4 reverse shot: Habeeb — not just a gang fight", chars=["habeeb", "ashham"],
         loc="police_office", visual="reuse of beat_013", amb="office_day", transition="cut"),
    dict(to=37, reuse="beat_014", reason="5.4 reverse shot: Ashham stands up and gives orders", chars=["ashham", "habeeb"],
         loc="police_office", visual="reuse of beat_014", amb="office_day", transition="cut"),
    # ---------------- MOOSA'S MANSION
    dict(to=39, v1="beat_014", reason="scene change: Moosa's mansion — a broken father on the sofa", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="a wide luxurious living room at night: Moosa sitting alone on a big cream leather sofa with his head bowed and his "
                "hands hanging between his knees, shattered; Ashham standing a few steps away near the door, looking at him gravely",
         camera=f"wide shot, eye level, {LOW} (polished marble floor)", amb="mansion_night", transition="black"),
    dict(to=40, speaker="moosa", reason="5.4 dialogue: Moosa asks 'is it really him?' — in the v1 conversation image both faces are at the "
         "edges; new over-the-shoulder image framed on Moosa (used for all his lines)", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="seen over Ashham's shoulder: Moosa sitting on the big cream leather sofa, leaning forward, speaking with a trembling "
                "voice, eyes red and wet behind his gold glasses, one hand raised helplessly, his face in three-quarter view "
                "towards the viewer and sharp; in the soft out-of-focus foreground at the left edge only the navy shoulder and the "
                "back of the head of Ashham, seated in an armchair opposite; a warm table lamp glowing behind Moosa",
         camera=f"over-the-shoulder medium close-up, eye level, Moosa centred in the upper half and sharp, Ashham soft at the "
                f"foreground edge, {LOW} (low coffee table in shadow)", amb="mansion_night"),
    dict(to=42, speaker="ashham", reason="5.4 reverse shot: Ashham answers and questions Moosa — new image framed on Ashham", chars=["ashham", "moosa"],
         loc="moosa_mansion",
         visual="seen over Moosa's shoulder: Ashham sitting forward in a dark leather armchair, elbows on his knees, hands clasped, "
                "speaking calmly but firmly, his face grave and sharp in three-quarter view; in the soft out-of-focus foreground at "
                "the right edge only the grey hair and dark suit shoulder of Moosa on the sofa, seen from behind; warm lamps and "
                "dark wood panelling behind Ashham",
         camera=f"over-the-shoulder medium close-up, eye level, Ashham centred in the upper half and sharp, Moosa soft at the "
                f"foreground edge, {LOW} (marble floor in shadow)", amb="mansion_night", transition="cut"),
    dict(to=47, reuse="beat_022", reason="5.4 reverse shot: Moosa tells of Naail's fear and the big secret, and begs Ashham", chars=["moosa", "ashham"],
         loc="moosa_mansion", visual="reuse of beat_022", amb="mansion_night", transition="cut"),
    dict(to=49, v1="beat_016", reason="emotional turning point: Moosa weeps; Ashham stands and puts a hand on his shoulder", chars=["moosa", "ashham"], loc="moosa_mansion",
         visual="Moosa weeping on the sofa, his face crumpled with grief, a hand pressed to his eyes under his gold glasses; Ashham "
                "standing beside him with one hand resting on Moosa's shoulder, looking down with a hard, determined face",
         camera=f"medium close shot, eye level, {LOW} (sofa and floor in shadow)", amb="mansion_night"),
    # ---------------- THE SEA HAWK, 2:30 AM
    dict(to=51, v1="beat_017", reason="time and scene change: 2:30 am, the fast launch leaves Kooddoo towards Kandu-huttaa", loc="sea_launch",
         visual="a sleek police fast launch racing across a rough black sea at night, its bow lifting over a wave, white spray "
                "flying, a long white wake behind it, small white navigation lights, the dark horizon",
         camera="wide shot, low angle near the water, the launch in the upper two-thirds, dark churning water as the calm lower third",
         amb="sea_boat", transition="black"),
    dict(to=58, v1="beat_018", reason="scene change: inside the cabin — Ashham and Habeeb silent beside the forensic cases; Habeeb opens his laptop",
         chars=["habeeb", "ashham"], loc="launch_cabin",
         visual="inside the dark launch cabin, Habeeb sitting with an open laptop on his knees, its cold blue glow on his glasses "
                "and face (the screen angled away from the viewer), turning to speak; Ashham sitting beside him, arms folded, "
                "listening hard; hard-shell forensic cases stacked at their feet; black windows with sea spray",
         camera=f"medium shot, eye level, {LOW} (cabin floor with the cases in shadow)", amb="sea_boat"),
    dict(to=60, v1="beat_019", reason="action change: Ashham looks out of the window into the darkness — the most dangerous case of his life", chars=["ashham"], loc="launch_cabin",
         visual="Ashham's profile close to a small square cabin window, staring out into the pitch-black sea, his face faintly lit "
                "by the blue glow from inside, sea spray streaking the glass, his own dim reflection in it, deep in thought",
         camera=f"close-up profile, eye level, {LOW} (dark window sill)", amb="sea_boat"),
    dict(to=63, v1="beat_020", reason="character change: the launch captain reports half an hour to Kandu-huttaa; Ashham gives orders", chars=["ashham"], loc="launch_cabin",
         visual="a middle-aged Maldivian launch captain in a light-grey long-sleeved shirt at the wheel, glancing back over his "
                "shoulder; Ashham standing behind him with one hand on the cabin roof rail, pointing ahead through the windscreen "
                "into the dark, giving orders; the navigation screen glowing with blurred shapes",
         camera=f"medium shot from the back of the cabin, eye level, {LOW} (dark cabin floor)", amb="sea_boat"),
    # ---------------- KANDU-HUTTAA AT DAWN
    dict(to=67, v1="beat_022", reason="time and scene change: dawn, the launch enters the lagoon of the beautiful, silent island", loc="kandu_lagoon",
         visual="the police fast launch gliding slowly into a calm turquoise lagoon at dawn, golden sunrays across the water, ahead "
                "a beautiful deserted island with a pure white sand beach and a wall of dense dark jungle, screwpine and coconut "
                "palms, tangled bushes reaching down into the water; no path, no people on the island, eerie stillness; aboard the launch only a few men seen from behind (Maldivian policemen in navy field uniforms and two soldiers in plain black combat gear and helmets), all men, no women",
         camera="wide shot from behind the launch, eye level, the island and sky in the upper two-thirds, smooth lagoon water as the calm lower third",
         amb="dawn_exterior", transition="black"),
    dict(to=70, v1="beat_023", reason="action change: Ashham and Habeeb step ashore with forensic kits, police and two soldiers behind them",
         chars=["ashham", "habeeb"], loc="kandu_beach",
         visual=f"Ashham and Habeeb wading the last steps from the shallows onto the white sand beach carrying hard-shell forensic "
                f"cases, Ashham scanning the jungle edge; behind them, further back near the launch, {SOLDIERS}",
         camera=f"medium wide shot, eye level, {LOW} (wet white sand)", amb="island_day"),
    dict(to=72, v1="beat_024", reason="action change: on the east side Ashham finds boot prints and bare footprints",
         chars=["ashham", "habeeb"], loc="kandu_beach",
         visual="Ashham crouching on the sand studying a trail of large boot prints and a few bare footprints coming out of the "
                "bushes; beside him Habeeb crouching over a dark oily stain in the sand, rubbing a pinch of sand between two "
                "fingers with a sharp look",
         camera=f"medium shot, slightly high angle, {LOW} (the footprints in the sand)", amb="island_day"),
    dict(to=74, speaker="habeeb", reason="5.4 dialogue: Habeeb names the launch engine oil — in the v1 image he is at the right edge looking "
         "down; new image framed on Habeeb", chars=["habeeb", "ashham"], loc="kandu_beach",
         visual="Habeeb crouching on the white sand beside a dark oily patch in the sand, holding up a pinch of oily sand between "
                "his thumb and two fingers near his face, looking up and speaking with a sharp, focused look behind his glasses, "
                "his face in three-quarter view and sharp; in the soft out-of-focus foreground at the edge only the navy shoulder "
                "of Ashham crouched beside him; the green jungle edge and bushes behind Habeeb",
         camera=f"medium close-up, slightly high angle, Habeeb centred in the upper half and sharp, Ashham soft at the foreground "
                f"edge, {LOW} (white sand)", amb="island_day"),
    dict(to=76, v1="beat_025", reason="action change: Ashham takes a broken twig as evidence — this is the crime scene", chars=["ashham"], loc="kandu_beach",
         visual="close-up of Ashham at the edge of the bushes carefully placing a small broken dry twig into a clear plastic "
                "evidence bag, his jaw set, eyes hard; the dark jungle behind him",
         camera=f"close-up, eye level, his face and hands in the upper two-thirds, {LOW} (sand in soft shadow)", amb="island_day",
         sens="violence", safe="the dried blood on the branches is not shown; only Ashham bagging a plain twig as evidence"),
    dict(to=78, v1="beat_026", reason="scene change: into the jungle; a hidden spot with palms bent and bound together", chars=["ashham", "habeeb"], loc="kandu_jungle",
         visual="Ashham pushing his way through dense jungle leaves with Habeeb close behind, a police officer further back; ahead "
                "of them two young palm trunks unnaturally bent low and held together with frayed palm-fibre twine; Ashham "
                "reaching out to pull them apart; nothing else on the ground but leaf litter and sand, no door, no hatch, no concrete",
         camera=f"medium shot, eye level, {LOW} (leaf litter on the ground)", amb="island_day"),
    dict(to=80, v1="beat_027", reason="action change: a pile of dry fronds — 'a rubbish pit?' — Ashham orders it cleared", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="in a small clearing a big heap of dry brown palm fronds and dead branches; Ashham dragging a large dry frond off "
                "the heap with both hands, determined; Habeeb beside him bending to pull another branch away, sand showing beneath",
         camera=f"medium wide shot, eye level, {LOW} (sand and dry fronds)", amb="island_day"),
    dict(to=83, v1="beat_028", reason="emotional turning point: under the sand a heavy steel bunker door with a big padlock", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="a heavy rusted steel hatch-door set in a low concrete block in the ground, half uncovered from the sand among the "
                "bushes, a big old padlock on it; Ashham crouching beside it with one palm flat on the cold steel, staring at it; "
                "Habeeb standing behind him, wide-eyed with astonishment, pushing his glasses up",
         camera=f"medium shot, slightly high angle, faces in the upper two-thirds, the door in the middle, {LOW} (sand)", amb="island_day"),
    dict(to=86, v1="beat_029", reason="action change: the roar of an approaching launch — they hide in the bushes", chars=["ashham", "habeeb"], loc="kandu_bunker",
         visual="Ashham and Habeeb crouched low among thick jungle leaves, peering out tensely towards the bright lagoon beyond the "
                "trees, where a fast dark launch with a white bow wave is speeding towards the island; behind them a police officer "
                "and a soldier in black combat gear crouched behind big tree trunks with empty hands",
         camera=f"medium shot from behind the leaves, eye level, {LOW} (dark leaf litter)", amb="island_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)
T = "tight"

sh(1, "The sun is going down. Outside the deserted island called Kandu-huttaa in the north of Huvadhu atoll, the dhoni Kalaminja rocks gently from side to side.")
sh(2, "The sky is spread with the fading colours of the red clouds. The wind grew stronger, and slowly the swell rose.",
   [("wind_gust", "ވައިރޯޅި", -20)])
sh(3, "It was then that Hassan, standing at the bow of the dhoni, noticed a big black thing floating far off. Hey! What's that thing floating over there?",
   speaker="hassan", crop=T, focus=[40, 35])
sh(4, "Hassan called out. Sameeru the cook slowed the dhoni's engine and looked where Hassan pointed. It was a big black bag.",
   [("dhoni_engine", "އިންޖީނު", -18)], speaker="hassan", crop=T, focus=[44, 35])
sh(5, "Or something made of two or three big bags tied together. The other two fishermen on the dhoni, Ibrahim and Ali, also came to the bow.",
   [("footsteps_pavement", "ދިރުނބާކޮޅަށް", -24)])
sh(6, "That must be a rubbish bag thrown out from some resort. Leave it and let's go. No, look,",
   speaker="ibrahim", crop=T, focus=[38, 35])
sh(7, "there are some strange fish around it. And there's a strange kind of smell coming off it too. Hassan said.",
   speaker="hassan", crop="medium", focus=[40, 42])
sh(8, "He took a hooked pole lying on the dhoni and dragged the bag towards the dhoni. As the bag hit the dhoni's hull, everyone could tell it was unnaturally heavy.",
   [("splash", "ދަމާލި", -18), ("soft_thud", "ޖެހުމާއެކު", -18)])
sh(9, "With it rose a foul stench hard to bear. Sameeru, shaking his head, helped lift it onto the dhoni.")
sh(10, "Four of them together hauled the heavy bag in over the side. The bag was sealed with thick plastic bags, and wide black tape was wound round it on the outside.",
   [("soft_thud", "އެތެރެކުރި", -18)])
sh(11, "Hassan took a cutter and started cutting the tape. As the first bag was cut open, the stench suddenly grew much stronger.",
   [("cloth_rustle", "ޓޭޕްތައް", -20)])
sh(12, "Everyone instinctively put their hands to their noses. Ali leaned over the side towards the sea and began retching. Is this... is this some",
   speaker="ibrahim", crop="medium", focus=[47, 42])
sh(13, "animal's meat? Ibrahim asked. Hassan cut the second layer of the bag.",
   speaker="ibrahim", crop=T, focus=[47, 35])
sh(14, "At that moment the sight that appeared from inside the bag almost made him lose his senses. It was part of a human leg, swollen and white from the salt.",
   [("gasp", "ފެނުނު", -18)], hum=True)
sh(15, "With trembling hands Hassan cut the whole bag open. It was the body of a man killed mercilessly. He had been brutally tortured.",
   [("heartbeat", "ތުރުތުރު", -20)], hum=True)
sh(16, "There were deep wounds on the neck. Ya Rabbi! What kind of cruelty is this! Quick, call the police! Switch on the set!",
   [("flashlight_click", "ހުޅުވާ", -20)], hum=True, speaker="sameeru", crop=T, focus=[49, 35])
sh(17, "Sameeru shouted. As this terror spread through the dhoni, the pitch darkness of night was taking over the whole sea.",
   [("wind_gust", "އަނދިރިކަން", -22)], speaker="sameeru", crop="medium", focus=[49, 42])
sh(18, "The capital Malé, Iskandhar Building. In the office of the police Serious Crimes Department in Iskandhar Building in Malé, Ashham sat at his desk.")
sh(19, "Ashham is a tall, strong, sharp man. He is one of the police's most capable investigators.")
sh(20, "He is a policeman famous for solving the most dangerous crimes in Malé.")
sh(21, "On his desk were empty coffee mugs and the files of some unfinished cases.")
sh(22, "From outside came the sound of vehicles racing at speed along Ameenee Magu. Ashham sat staring at the computer screen.",
   [("car_pass", "ވެހިކަލްތަކުގެ", -22)])
sh(23, "The office door opened and in came Habeeb. Habeeb is one of the best in the Maldives at data analysis and digital forensics.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(24, "Sir, a message just came in from the southern command. This isn't an ordinary case. Habeeb's face showed how serious it was. What is it?",
   speaker="habeeb", crop="medium", focus=[43, 42])
sh(25, "Ashham asked, settling into his chair. GA. A man has been found dead near a deserted island.",
   [("creak", "ހަމަޖެހިލަމުން", -22)], speaker="habeeb", crop=T, focus=[43, 35])
sh(26, "With big wounds — straight torture, a brutal murder, some limbs even cut off... Habeeb read out the report. Ashham's brows knotted.",
   speaker="habeeb", crop="medium", focus=[43, 42])
sh(27, "Killings do happen in the Maldives. But killing people this cruelly, as Habeeb described, mercilessly cutting off parts of the body, is not common.")
sh(28, "Ashham realised this had been done to send a direct message. Where's the body now? Ashham stood up.",
   [("cloth_rustle", "ތެދުވި", -22)], speaker="ashham", crop=T, focus=[32, 35])
sh(29, "They're bringing it to Villingili in that atoll. Headquarters wants you to handle this case directly, sir.",
   speaker="habeeb", crop=T, focus=[43, 35])
sh(30, "The reason is a tattoo on the back of that body. Habeeb showed a photo on his tablet.",
   [("computer_beep", "ދައްކާލި", -24)], speaker="habeeb", crop=T, focus=[45, 35])
sh(31, "The photo was taken by the fishermen of the dhoni that found the dead man. Drawn on the back of the dead, swollen body was a tattoo of a black phoenix bird.",
   hum=True)
sh(32, "On seeing that tattoo, Ashham remembered Naail Moosa, the younger son of Moosa Thaahir, one of Malé's most influential businessmen.")
sh(33, "Naail was a young man of Malé's youth nightlife and big car races, and suspected of drugs. This is",
   [("car_pass", "ކާރު", -20)])
sh(34, "Naail. He's been missing for a week now. His father has been throwing money in every direction in Malé",
   speaker="ashham", crop=T, focus=[32, 35])
sh(35, "trying to find him. Yes, sir. If this is Naail, this isn't just a gang fight.",
   speaker="habeeb", crop="medium", focus=[43, 42])
sh(36, "There's a big secret behind this. Habeeb said. Ashham stood up. Habeeb, prepare the trip.",
   [("cloth_rustle", "ތެދުވި", -22)], speaker="ashham", crop=T, focus=[32, 35])
sh(37, "And gather Naail's medical records and the records of the crimes he was suspected of. We have to leave tonight. The wealthy father's tears.",
   speaker="ashham", crop="medium", focus=[36, 42])
sh(38, "Before leaving for the south, Ashham wanted to meet Moosa Thaahir. Moosa sat in the great hall of his wealthy house, where all one could see was luxury and plenty.")
sh(39, "In the middle of that wealth sat a despairing, broken father. Moosa sat on the sofa with his head bowed. Ashham, my son...",
   speaker="moosa", crop=T, focus=[37, 42])
sh(40, "is it really him? Qaasim's voice was trembling. Until the DNA is actually done,",
   speaker="moosa", crop=T, focus=[56, 35])
sh(41, "it's hard to say anything for certain. But the tattoo on the back matches. Ashham said, sitting down.",
   speaker="ashham", crop=T, focus=[34, 35])
sh(42, "Moosa, was Naail... mixed up in anything dangerous lately? Who in Malé did he get into trouble with?",
   speaker="ashham", crop="medium", focus=[36, 42])
sh(43, "Moosa shook his head. He was always a boy who went around with bad friends. But",
   speaker="moosa", crop="medium", focus=[56, 42])
sh(44, "two weeks ago I noticed he was very frightened. He said",
   speaker="moosa", crop=T, focus=[56, 35])
sh(45, "he'd found out a big secret. But... he didn't give much detail. What secret? Ashham asked at once.",
   speaker="moosa", crop="medium", focus=[56, 42])
sh(46, "That... that he didn't say. But he said those people are in Malé too.",
   speaker="moosa", crop=T, focus=[56, 35])
sh(47, "Ashham, find the people who killed my son. I will make any sacrifice.",
   hum=True, speaker="moosa", crop=T, focus=[56, 35])
sh(48, "Moosa said, weeping. Ashham stood and put his hand on Moosa's shoulder. As he understood it, Naail had not been killed only for revenge.",
   [("sob_breath", "ރޮމުން", -20), ("cloth_rustle", "އަތްޖަހާލި", -22)], hum=True, speaker="moosa", crop="medium", focus=[40, 48])
sh(49, "The meaning of what was done to him was: don't say a word. And don't touch anything, or don't reveal anything.")
sh(50, "This is a warning. Straight onto the sea: it is half past two in the morning.")
sh(51, "The police's fastest modern launch, Sea Hawk, sped out of Kooddoo harbour. Carrying Ashham's team, who had flown into Kooddoo airport, the launch is heading for the Kandu-huttaa area.",
   [("boat_engine", "ދުއްވާލި", -14)])
sh(52, "The sea is rough. As the launch sped over the waves, Ashham and Habeeb sat in silence. Beside them were the forensic cases.",
   [("wave_crash", "ގަދަ", -18)])
sh(53, "Some members of the investigation team and extra police are already in that area. A backup team and a team of soldiers ready to help are also standing by for a signal.")
sh(54, "Habeeb, did you check the last locations of Naail's phone? Ashham asked. Opening his laptop, Habeeb said: Yes, sir.",
   [("keyboard_typing", "ލެޕްޓޮޕް", -22)], speaker="ashham", crop=T, focus=[68, 35])
sh(55, "His phone went dead in Malé a week ago. But before that he had called numbers on various islands in the south.",
   speaker="habeeb", crop=T, focus=[31, 35])
sh(56, "He called one number especially often. It's a number of that atoll's hospital. A hospital!",
   speaker="habeeb", crop=T, focus=[31, 38])
sh(57, "Ashham thought. Naail isn't a sick man. Why would he need to call a hospital?",
   speaker="ashham", crop=T, focus=[68, 35])
sh(58, "I'm working on finding out who uses that number. But that island's systems are blocked. Habeeb said.",
   speaker="habeeb", crop=T, focus=[31, 35])
sh(59, "Ashham looked out of the launch's small window. Nothing could be seen in the darkness of the sea.")
sh(60, "He felt that this would be the most dangerous and unusual case he would ever face in his life.",
   hum=True)
sh(61, "What could this secret be, hidden between Malé's wealth and the emptiness of the islands? Sir, to reach Kandu-huttaa it'll still take us",
   speaker="captain", crop=T, focus=[59, 37])
sh(62, "about half an hour. The launch captain said. Good. We go to that island first. We have to check the area where the fishermen picked up the body.",
   speaker="ashham", crop=T, focus=[42, 35])
sh(63, "We have to see whether anything else is going on there. Ashham ordered. With the sound of the launch's engine, they went on cutting through the great waves of the sea.",
   [("boat_engine", "އިންޖީނުގެ", -16), ("wave_crash", "ރާޅުތައް", -18)], speaker="ashham", crop="medium", focus=[42, 42])
sh(64, "That was the beginning. The truth of Kandu-huttaa. The light of dawn spread, and the sun's golden rays began to fall on the sea's surface.")
sh(65, "Sea Hawk entered Kandu-huttaa's lagoon. It's a naturally beautiful, charming island. Yet a deserted island ruled by a frightening silence.",
   [("boat_engine", "ފަޅަށް", -22)])
sh(66, "All around the island is a clean white sand beach. At the edge of the vegetation grow dense screwpine and magoo bushes.")
sh(67, "In some places the bushes have grown thick and run from the beach down to the water's edge. Seen from the shore, the island's vegetation is very dense.")
sh(68, "A jungle island. No trace of a human being anywhere. No path into the island can be seen.")
sh(69, "Ashham and Habeeb stepped ashore with forensic kits. Extra police and two soldiers with weapons were with them to help.",
   [("footsteps_sand", "ފޭބި", -18)])
sh(70, "According to the fishermen, the bag they found had floated outside the reef on the island's east side. Ashham started walking, looking at the island's sand. Habeeb,",
   [("footsteps_sand", "ހިނގަން", -20)], speaker="ashham", crop=T, focus=[70, 35])
sh(71, "come this way. Ashham called. Among the bushes there were big footprints in the sand. They were the marks of boots.",
   speaker="ashham", crop=T, focus=[34, 35])
sh(72, "There were also some prints of bare feet. Not far from the footprints were signs of black oil dripped onto the ground.")
sh(73, "This is a launch's engine oil. Sir, what's this on these bushes?",
   speaker="habeeb", crop=T, focus=[46, 35])
sh(74, "Habeeb said, picking up sand where the oil was and rubbing it between two fingers. On some branches there were traces of blood. They had dried.",
   speaker="habeeb", crop="medium", focus=[46, 42])
sh(75, "Ashham took a twig from there and put it in a bag. It looks like Naail wasn't killed at sea. He was killed on this island.",
   [("cloth_rustle", "ކޮތަޅަކަށްލި", -20)], speaker="ashham", crop="medium", focus=[45, 42])
sh(76, "This is the crime scene. Ashham went into the bushes. The team members went with him too.",
   [("leaves_rustle", "ވަދެގެން", -18)], hum=True, speaker="ashham", crop=T, focus=[45, 35])
sh(77, "After going quite a way, they found a place that seemed to be hidden among the thick bushes. Two or three trees had been bent down and tied.")
sh(78, "Ashham cut the cord tying the trees. There was nothing. Dry palm fronds and dried branches lay piled in a heap.",
   [("leaves_rustle", "ބުރިކޮށްލި", -18)])
sh(79, "Sir, a rubbish pit. No! Why would there be such a big rubbish pit on a deserted island? Who, which people...",
   speaker="ashham", crop=T, focus=[35, 35])
sh(80, "Clear these branches, dig this place up. Ashham said, pulling away a dried branch. His thinking was right.",
   [("leaves_rustle", "ދުރަށްލަމުން", -16)], hum=True, speaker="ashham", crop=T, focus=[35, 38])
sh(81, "From the dug-up sand appeared a steel door. A heavy door. It was the door of a concrete bunker built to go deep into the ground.",
   hum=True)
sh(82, "A big padlock was on the door. A bunker on a deserted island? This isn't just an ordinary deserted island.",
   [("metal_clang", "ތަޅެއް", -22)], hum=True, speaker="ashham", crop=T, focus=[49, 35])
sh(83, "This is a place where a huge crime is run. This is the secret Naail found. Ashham said, touching the bunker door.",
   hum=True, speaker="ashham", crop="medium", focus=[49, 42])
sh(84, "At that moment came the sound of a launch approaching at high speed. Ashham and Habeeb instantly hid among the bushes.",
   [("boat_engine", "ލޯންޗެއް", -14), ("leaves_rustle", "ނިވާވި", -18)], hum=True)
sh(85, "The other police too took cover carefully behind big trees. The soldiers, weapons ready, stayed alert.",
   [("heartbeat", "ސަމާލުވެލި", -20)])
sh(86, "Someone knew the police had come to this island. And those people are now coming after them. To be continued in part two.",
   hum=True)
SHOTS = S

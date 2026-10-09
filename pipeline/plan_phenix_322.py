"""Beat/shot plan for Project Phenix episode 322 (used by plan_beats.py)."""

LOC = {
    "kandu_beach_day": "Kandu-huttaa, a deserted uninhabited island in Huvadhu (Gaafu Alifu) atoll: a white sand beach, dense dark jungle of screwpine, magoo bushes and coconut palms behind it, no path, no people, black smoke rising from the island's interior after the bunker blast",
    "kandu_reef": "the edge of Kandu-huttaa's white beach where it meets the dark coral reef, waves washing over the reef rocks, dense jungle behind",
    "kandu_beach_night": "Kandu-huttaa beach at night after the explosion: big old trees at the shore, a small driftwood and dry-frond fire on the sand under them, embers glowing far behind the trees, the dark lagoon and sea beyond",
    "launch_cabin": "the cabin of a big captured twin-engine launch at night: a steering wheel, a glowing navigation and radar screen with no readable digits, dark windows onto the black sea, a cushioned bench",
    "launch_sea": "the pitch-black open sea of the Huvadhu channel at night, no land in sight",
    "fairooz_office": "a top-floor office in Malé police headquarters: a big polished desk, a high-backed leather chair, a large wall screen, a tall window over the city lights",
    "hulhumale_shore": "a quiet dark stretch of Hulhumalé's shore at 3 am: sand and large boulders, a few far-apart street lights, modern apartment blocks dark in the distance",
    "hulhumale_street": "an empty street of Hulhumalé at night between tall modern apartment blocks, sparse street lights, damp pavement",
    "faahid_corridor": "the dim fourth-floor corridor of a modest Hulhumalé apartment building at night, plain walls, a wooden front door",
    "faahid_flat": "Faahid's modest fourth-floor Hulhumalé flat: a simple living room with a sofa, a wooden table and a desk with a computer, a window onto the dark city",
    "car_morning": "inside a car crossing the long sea bridge from Hulhumalé to Malé at sunrise, the sea and the city skyline outside",
    "police_hq_ext": "the front of the large modern police headquarters building in Malé (the Shaheed Hussain Adam Building) in the morning, wide steps and glass entrance, no writing on the building",
    "police_hq_lobby": "the busy entrance lobby of Malé police headquarters: a polished stone floor, glass doors, corridors leading off in two directions",
}
MOOD = {
    "kandu_beach_day": "late afternoon under a heavy grey overcast sky, hazy diffused light, drifting black smoke and ash, an orange glow behind the trees, stunned and desolate",
    "kandu_reef": "late afternoon under a heavy grey overcast sky, cold grey-green sea, white spray, hopeless",
    "kandu_beach_night": "night: cold navy-blue darkness and silver moonlight, the single warm orange light source of the small fire (or of flashlight beams once the fire is out), tense and fragile",
    "launch_cabin": "night: deep navy darkness outside, warm dim amber cabin light and the cold green-blue glow of the navigation screen, quiet relief mixed with resolve",
    "launch_sea": "night: pitch-black navy sea under faint stars, the only brightness is the boat's white foaming wake, lonely and determined",
    "fairooz_office": "night: dark office lit by a warm desk lamp and the cold blue glow of the wall screen, city lights through the window, smug and sinister",
    "hulhumale_shore": "3 am: cold navy-blue darkness, a few distant sodium street lights, calm black water, secretive",
    "hulhumale_street": "3 am: cold navy-blue darkness, pools of warm sodium street light on the damp pavement, quiet and tense",
    "faahid_corridor": "night: dim corridor in cold navy shadow, warm lamp light spilling from the opened door, shock",
    "faahid_flat": "night: a dim room in navy shadow with one warm table lamp and the cold glow of the computer monitor, grave and angry",
    "car_morning": "sunrise: low golden-orange sunlight, long shadows, cool blue sea, tense calm",
    "police_hq_ext": "bright tropical morning sun, crisp shadows, a busy anxious crowd",
    "police_hq_lobby": "morning: cool white indoor light and daylight through the glass doors, tense and secretive",
}

LOW = "faces in the upper two-thirds, a calm uncluttered dark lower third"
ASH = "Ashham in plain civilian clothes (a dark-grey long-sleeved shirt and dark trousers, no police uniform), dusty and damp, unmarked"
RAN = "Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque"
FAT = "her thin elderly father in loose pale-grey clothes"
ASHC = "Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp)"
RANC = "Raniya (her reference image is used only for her face: NO white coat, no doctor's coat; she wears only a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck)"
HABU = "Habeeb (his reference image is used only for his face and glasses: he is NOT wearing his grey jacket or white t-shirt; he wears a dark-navy police uniform shirt buttoned up, navy trousers, a navy police cap and dark sunglasses)"
DIS = "dark-navy police uniform with a navy police cap pulled low and dark sunglasses (plain epaulettes, no badges, no lettering)"

BEATS = [
    # ---------------- KANDU-HUTTAA, AFTERMATH (afternoon)
    dict(to=2, reason="episode opening: the second underground blast shakes the island; trees torn apart, red flames", loc="kandu_beach_day",
         visual="a distant view across the white beach of Kandu-huttaa toward the jungle: a huge orange fireball and a column of black smoke and red glow rising high above the treetops in the island's interior, palm trees bending, leaves and sand blown through the air; far in the foreground on the sand, small and far from the blast, four tiny dark silhouettes crouched low with their arms over their heads, seen from behind; nobody hurt",
         camera=f"wide shot, eye level, the explosion and sky in the upper two-thirds, the white sand as the calm lower third",
         amb="beach_day", sens="violence", safe="the blast is shown only as distant spectacle; the four people are tiny crouched silhouettes seen from behind, nobody thrown or hurt"),
    dict(to=5, reason="time jump: an hour later Ashham opens his eyes and sits up", chars=["ashham"], loc="kandu_beach_day",
         visual=f"{ASH}, sitting up on the white sand, one hand propping him up, the other at his temple, shaking his head, dazed; his face only dusty with sand and grey ash; black smoke rising above the jungle behind him",
         camera=f"medium shot, eye level, {LOW} (white sand)", amb="beach_day", transition="black",
         sens="violence", safe="his small wounds and the blood at his mouth and nose are not shown: only a dusty, dazed face"),
    dict(to=7, reason="character change: Ashham reaches Habeeb, who coughs and opens his eyes", chars=["habeeb", "ashham"], loc="kandu_beach_day",
         visual="Habeeb half sitting up on the sand, propped on one elbow, coughing into his fist, his glasses askew, his grey zip jacket dusty; Ashham (civilian dark-grey long-sleeved shirt, dusty) kneeling beside him with one hand on his shoulder, letting out a breath of relief; smoke haze over the jungle behind",
         camera=f"medium shot, slightly high angle, {LOW} (sand)", amb="beach_day",
         sens="other", safe="Habeeb 'lying on the sand' is shown already half sitting up, unhurt"),
    dict(to=8, reason="character change: Raniya with her unconscious father", chars=["raniya", "raniya_father"], loc="kandu_beach_day",
         visual=f"{RAN}, kneeling on the sand in the shade of a leaning palm, teary-eyed, holding her father's hand in both of hers; {FAT} sits slumped back against the palm trunk, eyes closed, unconscious but breathing; both dusty; smoke haze far behind",
         camera=f"medium shot, eye level, {LOW} (sand)", amb="beach_day",
         sens="other", safe="the father's head 'in her lap' is shown as him sitting slumped against a palm trunk beside her (no person lying)"),
    dict(to=9, reason="return: Ashham checks his pocket for the hard drive", reuse="beat_003", chars=["habeeb", "ashham"],
         loc="kandu_beach_day", visual="reuse of beat_003", amb="beach_day"),
    dict(to=12, reason="new location/action: the dinghy smashed on the reef; Habeeb's tablet is dead", chars=["habeeb"], loc="kandu_reef",
         visual="the small white fibreglass dinghy smashed and broken on the dark reef rocks at the waterline, its outboard engine split apart in pieces beside it, waves washing over it; in the foreground on the sand Habeeb (glasses askew, dusty grey zip jacket) crouching and holding a dark lifeless tablet whose screen is completely black, a despairing look",
         camera=f"medium wide shot, eye level, {LOW} (wet sand)", amb="beach_day"),
    dict(to=15, reason="action change: Ashham stands and looks at the rough sea; nobody will come", chars=["ashham"], loc="kandu_beach_day",
         visual=f"{ASHC}, standing alone at the water's edge seen from behind at a three-quarter angle, looking out at a grey rough sea with big white-capped waves breaking, under a heavy overcast sky; black smoke drifting overhead",
         camera=f"medium wide shot from behind, eye level, the sea and sky in the upper two-thirds, wet sand as the calm lower third", amb="beach_dusk"),
    dict(to=19, reason="character change: Raniya pleads for her father; Ashham gives orders", chars=["raniya", "raniya_father", "ashham", "habeeb"], loc="kandu_beach_day",
         visual=f"under the shade of tall palms at the jungle's edge in fading light: {RAN}, kneeling beside {FAT} who sits slumped against a palm trunk with his eyes closed; she looks up, pleading and distraught; several steps away Ashham (civilian dark-grey shirt) stands firm, pointing along the beach and giving instructions, Habeeb (glasses, grey zip jacket) nodding beside him; a clear distance between Raniya and the men",
         camera=f"medium wide shot, eye level, {LOW} (sand)", amb="beach_dusk"),
    # ---------------- NIGHT ON THE ISLAND
    dict(to=21, reason="time jump: night; Habeeb has lit a fire of dry fronds under the big trees", chars=["habeeb", "raniya", "raniya_father"], loc="kandu_beach_night",
         visual=f"night under huge old trees at the shore: a small fire of dry palm fronds and driftwood burning on the sand; Habeeb crouched feeding a dry frond into the flames, firelight on his glasses; a few steps away {RAN} sits beside {FAT}, who rests sitting against a tree trunk with his eyes closed; the dark sea beyond",
         camera=f"medium wide shot, eye level, {LOW} (dark sand)", amb="beach_night", transition="black"),
    dict(to=23, reason="action change: the father wakes asking for water; Ashham brings young coconuts", chars=["ashham", "raniya", "raniya_father"], loc="kandu_beach_night",
         visual=f"by the small fire at night: Ashham (civilian dark-grey shirt) bending to set an opened young green coconut on a driftwood log in front of {RAN}, at arm's length, not touching her; {FAT}, sitting against the tree trunk, has weakly opened his eyes; two more green coconuts on the sand; warm firelight on their faces",
         camera=f"medium shot, eye level, {LOW} (sand and the log)", amb="beach_night"),
    dict(to=27, reason="framing change: Ashham and Habeeb by the fire; the hard drive is their weapon", chars=["ashham", "habeeb"], loc="kandu_beach_night",
         visual="Ashham (civilian dark-grey shirt) and Habeeb sitting on the sand on opposite sides of the small fire at night; Ashham holds up a small black external hard drive between his fingers, looking at it with fierce determination; Habeeb, worried, watches him over the flames, firelight on his glasses",
         camera=f"medium shot, eye level, {LOW} (sand)", amb="beach_night"),
    dict(to=29, reason="turning point: a searchlight far out at sea; Ashham smothers the fire", chars=["ashham", "habeeb", "raniya"], loc="kandu_beach_night",
         visual=f"{ASHC} on one knee pushing sand with both hands over the fire, smothering it, a curl of grey smoke rising; behind him Habeeb and {RANC}, a step apart from him, ducking low and staring out to sea, where far away on the black water a powerful white searchlight beam sweeps toward the island",
         camera=f"medium wide shot, low angle, {LOW} (dark sand)", amb="beach_night", hum=True),
    dict(to=33, reason="new characters: the guards' launch arrives; three men with flashlights find the smoke", loc="kandu_beach_night",
         visual="night on the beach: a dark launch nosing into the shallow lagoon with its searchlight on; three dark figures in black clothes and black face masks wading onto the beach, each holding only a bright flashlight, beams criss-crossing the sand and falling on a small mound of sand with a thin wisp of smoke rising from it; their hands hold nothing but flashlights; no lettering on the launch",
         camera="wide shot from the tree line, eye level, the launch and figures in the upper two-thirds, the dark beach as the calm lower third",
         amb="beach_night", sens="violence", safe="the armed guards are shown with flashlights only, no weapons visible"),
    dict(to=35, reason="action change: Ashham crawls through the dark behind the guards", chars=["ashham"], loc="kandu_beach_night",
         visual="Ashham (civilian dark-grey shirt) crouched low in the dark bushes at the jungle's edge, seen in profile, intense focused eyes, his hands empty and resting on the sand, watching three flashlight beams moving on the beach beyond the leaves",
         camera=f"medium close-up, low angle, {LOW} (dark sand and leaves)", amb="jungle_night",
         sens="violence", safe="loading his gun is not shown; his hands are empty"),
    dict(to=37, reason="action change: the short fight in the dark (shown only as a dropped flashlight)", loc="kandu_beach_night",
         visual="the empty dark beach at night: a single flashlight lying dropped on the sand, still switched on, its beam lighting a long cone of empty sand and scattered footprints; in the background two more flashlight beams spinning wildly through the darkness between the palm trunks; no person visible",
         camera="low ground-level shot, the spinning beams in the upper two-thirds, the lit sand as the calm lower third",
         amb="beach_night", sens="violence", safe="the takedown and the gunfight are never shown: only a dropped flashlight on the empty beach and spinning beams"),
    dict(to=39, reason="action change: the captain fires from the launch; bark splinters fly beside Ashham", chars=["ashham"], loc="kandu_beach_night",
         visual=f"night, the campfire already put out (no fire anywhere): chips of bark and splinters bursting off a palm trunk in the glare of the launch's searchlight; {ASHC} pressed with his back against the far side of the trunk, empty hands, his tense face turned away; the launch's light glaring from the water behind",
         camera=f"medium shot, eye level, {LOW} (dark sand)", amb="beach_night",
         sens="violence", safe="gunfire shown only as bark splinters off a tree; Ashham's hands empty, no gun"),
    dict(to=41, reason="character/action change: the captain reverses; Habeeb dives into the sea", chars=["habeeb"], loc="kandu_beach_night",
         visual="night: Habeeb (glasses, grey zip jacket) diving headfirst from the shallows into the black sea toward a dark launch that is backing away from the beach, its engine churning white foam; moonlight and the launch's light on the spray; no lettering on the launch",
         camera="medium wide shot, eye level, the launch and the diving figure in the upper two-thirds, dark water as the calm lower third", amb="beach_night"),
    dict(to=44, reason="action change: Ashham leaps aboard and throws the captain into the sea; the launch is theirs", chars=["ashham", "habeeb"], loc="kandu_beach_night",
         visual="night in the lagoon: the big dark twin-engine launch; Ashham (civilian dark-grey shirt) standing firm on its rear deck in silhouette against the cabin light, one hand gripping the rail; beside the launch a big white splash in the black water where someone has just gone overboard (no person visible in the splash); Habeeb in the water at the stern, holding the stern rail, looking up",
         camera="medium wide shot, slightly low angle, the launch in the upper two-thirds, black water as the calm lower third",
         amb="sea_boat", sens="violence", safe="the captain's pistol, the struggle and the throw are not shown: only Ashham standing on the deck and a splash beside the launch"),
    # ---------------- THE VOYAGE
    dict(to=47, reason="new location: inside the cabin; lights on, radar shows the course to Malé", chars=["ashham", "habeeb"], loc="launch_cabin",
         visual="inside the launch cabin at night: Ashham (civilian dark-grey shirt, damp) at the wheel looking ahead through the dark windscreen; beside him Habeeb, wet hair, glasses on, smiling at a glowing navigation and radar screen showing only soft green sweeps and blurred shapes, no numbers",
         camera=f"medium shot, eye level, {LOW} (dark console)", amb="sea_boat"),
    dict(to=50, reason="scene change: the launch cuts across the dark sea, only its white wake visible", loc="launch_sea",
         visual="a wide high view of a big twin-engine launch speeding across the pitch-black open sea at night, only its long white foaming wake visible behind it, faint stars, no land in sight; no lettering on the hull",
         camera="wide aerial shot, the launch and its wake in the upper two-thirds, black water as the calm lower third", amb="sea_boat"),
    dict(to=51, reason="character change: Raniya with her father in the cabin, relieved", chars=["raniya", "raniya_father"], loc="launch_cabin",
         visual=f"in a corner of the launch cabin at night: {RAN}, sitting on a cushioned bench; {FAT} sits beside her wrapped in a grey blanket, his head resting on her shoulder, eyes closed, breathing peacefully; Raniya looking down at him with quiet relief",
         camera=f"medium shot, eye level, {LOW} (bench and cabin floor)", amb="sea_boat",
         sens="other", safe="the father's head 'in her lap' is shown as him sitting beside her, head on her shoulder (mahram)"),
    dict(to=54, reason="return: Habeeb at the navigation screen, Ashham at the wheel", reuse="beat_019", chars=["ashham", "habeeb"],
         loc="launch_cabin", visual="reuse of beat_019", amb="sea_boat"),
    dict(to=57, reason="framing change: Ashham looks at the small hard drive, their only weapon", chars=["ashham"], loc="launch_cabin",
         visual="close-up of Ashham (civilian dark-grey shirt) at the wheel in the dark cabin, holding up a small black hard drive in the glow of the navigation screen, examining it, his eyes hard and determined; the black sea beyond the windscreen",
         camera=f"close-up, eye level, {LOW} (dark console)", amb="sea_boat"),
    # ---------------- MALÉ HQ
    dict(to=60, reason="scene change: Fairooz in his top-floor HQ office, satellite photos of the destroyed bunker", chars=["fairooz"], loc="fairooz_office",
         visual="Fairooz leaning back in a big leather chair behind his broad desk with a satisfied, victorious smile, facing a large wall screen that shows a blurred grey aerial image of a smoking crater in green jungle; city lights through the window; no text on the screen",
         camera=f"medium wide shot, eye level, {LOW} (the dark desk top)", amb="office_night",
         sens="other", safe="the destroyed bunker appears only as a blurred aerial photo on a screen"),
    dict(to=64, reason="character enters: Moosa Thaahir, exhausted and anxious", chars=["fairooz", "moosa"], loc="fairooz_office",
         visual="Moosa standing tired and anxious in front of the desk, shoulders slumped, hands clasped; Fairooz seated behind the desk holding a coffee cup to his lips with a cold smile; the wall screen glowing behind",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="office_night", hum=False),
    dict(to=67, reason="action change: Fairooz shows the prepared official report", chars=["fairooz", "moosa"], loc="fairooz_office",
         visual="close on the desk: Fairooz's hand pushing a closed plain dark folder with a blank cover across the polished desk, Fairooz smirking above it; Moosa in the background, uneasy, looking at the folder",
         camera=f"medium close-up, slightly high angle, {LOW} (polished desk)", amb="office_night"),
    dict(to=68, reason="return: Moosa sighs, trapped in Fairooz's plan", reuse="beat_025", chars=["fairooz", "moosa"],
         loc="fairooz_office", visual="reuse of beat_025", amb="office_night"),
    # ---------------- HULHUMALÉ
    dict(to=71, reason="time and scene change: 3 am, the launch reaches a lonely spot of Hulhumalé", chars=["ashham", "habeeb"], loc="hulhumale_shore",
         visual=f"3 am: the dark launch drifting against a quiet stretch of Hulhumalé shore with sand and large boulders; {ASHC} stepping off the bow onto the sand first, Habeeb behind him on the deck; a few far-off street lights and dark apartment blocks; no lettering on the launch",
         camera=f"medium wide shot, eye level, {LOW} (dark sand)", amb="beach_night", transition="black"),
    dict(to=75, reason="action change: they walk through Hulhumalé's dark streets to Faahid's building", chars=["ashham", "habeeb", "raniya", "raniya_father"], loc="hulhumale_street",
         visual=f"four people walking along an empty dark Hulhumalé street at night past tall apartment blocks under sparse street lights: {ASHC} and Habeeb in front, Habeeb talking and gesturing; a few steps behind them {RANC}, supporting {FAT} by his arm; damp clothes, damp pavement",
         camera=f"medium wide shot, eye level, {LOW} (damp pavement)", amb="street_night"),
    dict(to=78, reason="character enters: Faahid opens his door, stunned", chars=["faahid", "ashham", "habeeb"], loc="faahid_corridor",
         visual=f"the dim fourth-floor apartment corridor at night: the front door open, Faahid (dark-olive shirt) standing in the doorway in the warm light from inside, eyes wide with shock; {ASHC} and Habeeb, damp and dusty, standing in the corridor before him",
         camera=f"medium shot, eye level, {LOW} (corridor floor)", amb="home_night"),
    dict(to=80, reason="scene change: the hard drive in Faahid's computer; his face fills with fury", chars=["faahid", "ashham", "habeeb"], loc="faahid_flat",
         visual="in Faahid's living room at night: Faahid seated at the desk, Ashham (civilian dark-grey shirt) and Habeeb standing behind him, all three faces lit by the cold glow of the computer monitor (screen seen from the side, unreadable); a small black hard drive plugged into the computer; Faahid's face hardening into fury",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="living_night",
         sens="violence", safe="the killing video and experiment documents are never shown: only faces lit by a screen seen from the side"),
    dict(to=86, reason="action change: Faahid strikes the table and lays out the press-conference plan", chars=["faahid", "ashham", "habeeb"], loc="faahid_flat",
         visual="Faahid (dark-olive shirt) standing at the wooden table, his palm pressed down hard on the tabletop, leaning forward and speaking fiercely; Ashham (civilian dark-grey shirt) and Habeeb listening intently across the table; the computer glowing behind",
         camera=f"medium shot, eye level, {LOW} (table top)", amb="living_night"),
    # ---------------- INTO THE TRAP
    dict(to=88, reason="time jump: sunrise; disguised in police uniforms, they drive to Malé in Faahid's car", chars=["ashham", "habeeb"], loc="car_morning",
         visual=f"inside a car crossing the long sea bridge toward Malé at sunrise: Ashham driving, in {DIS}, and in the passenger seat {HABU}; tense faces, golden low sunlight through the windscreen",
         camera=f"medium shot through the windscreen, eye level, {LOW} (dashboard in shadow)", amb="car_interior", transition="black"),
    dict(to=89, reason="scene change: the car stops at police HQ, crowded with journalists", loc="police_hq_ext",
         visual="morning: the front of the large modern police headquarters building in Malé, a big crowd of journalists with TV cameras on tripods and microphones gathered at the entrance, a white car pulling up at the kerb; no writing anywhere",
         camera="wide shot, eye level, the building and crowd in the upper two-thirds, the paved forecourt as the calm lower third", amb="city_day"),
    dict(to=92, reason="action change: they slip inside among a group of police and split up", chars=["ashham", "habeeb"], loc="police_hq_lobby",
         visual=f"inside the busy entrance lobby of police headquarters: a group of uniformed police officers walking in; among them Ashham in {DIS} and {HABU}, faces tense; Ashham glancing sideways at Habeeb as the corridor splits in two directions ahead",
         camera=f"medium wide shot, eye level, {LOW} (polished floor)", amb="office_day", hum=False),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With a second powerful blast from deep under Kandu-huttaa's ground, the whole deserted island shook. The bushes and trees over the bunker were torn apart,",
   [("distant_boom", "ގޮވުމާއެކު", -12)])
sh(2, "and the red of the flames spread upward. With the force of the blast, Ashham, Habeeb, Raniya and Raniya's father were flung onto the white sand of the beach.",
   [("fire_crackle", "އަލިފާނުގެ", -20), ("soft_thud", "ވިއްސައިގެން", -22)], hum=True)
sh(3, "A deafening, ear-ringing roar. About an hour later, Ashham slowly opened his eyes. He shook his head.",
   [("breath", "ހުޅުވާލިއެވެ", -22)])
sh(4, "His whole body was covered in small wounds; traces of blood showed at his mouth and nose. He got up and looked around.")
sh(5, "Black smoke was still rising from where the bunker had been. Of that terrifying laboratory not a trace was left. 'Habeeb… Raniya…'",
   hum=True)
sh(6, "Ashham called out in a hoarse voice. Half crawling, he went to Habeeb lying on the sand, took him by the shoulder and shook him.",
   [("cloth_rustle", "ފިރުކެމުން", -22)])
sh(7, "Habeeb suddenly coughed and opened his eyes. Knowing he was safe, Ashham let out a breath of relief.",
   [("gasp", "ހޮޑުލަމުން", -22), ("sigh", "ނޭވާއެއްލިއެވެ", -20)])
sh(8, "Not far away Raniya sat crying, her father's head in her lap. Her father was breathing, but he lay unconscious. 'The hard drive…'",
   [("sob_breath", "ރޯށެވެ", -24)], hum=True)
sh(9, "Habeeb's first concern was whether the vital evidence was safe. Ashham quickly reached into his pocket. The small hard drive with the forensic data was safe.")
sh(10, "'We're stranded on this deserted island now.' Cut off from the outside world: the small dinghy they came in had been flung onto the reef by the blast and smashed to pieces.",
   [("wave_crash", "ފަރުމައްޗަށް", -20)])
sh(11, "The engine was in fragments. Habeeb tried to open his tablet, but it wouldn't. 'Sir, it's completely gone. It won't even turn on.'")
sh(12, "'Our satellite modem fell and broke too,' Habeeb said in despair. 'We can't reach Malé, or even a nearby island.'")
sh(13, "'We're cut off.' Ashham stood up and looked toward the shore. In the distance lay a rough sea; big waves were breaking.",
   [("wave_crash", "ރާޅުތައް", -18)])
sh(14, "Fairooz would believe they had died in the blast inside the bunker. So no police from Malé would ever come looking for them.")
sh(15, "Fairooz was sure to have their names marked 'dead' in the police records. 'We'll die of hunger on this island,'",
   hum=True)
sh(16, "Raniya said, crying. 'Father needs medical help. The effects of the chemicals in his body have to be cleared.'",
   [("sob_breath", "ރޮމުން", -24)])
sh(17, "Ashham's mind began to work hard. As an investigator he knew that the moment you give up hope, you are beaten.")
sh(18, "'Habeeb, walk around the island. We might spot a fishing dhoni. We have to find a way. Raniya,'")
sh(19, "'take your father somewhere with shade.' Night on the deserted island: the sun set and pitch darkness took over.")
sh(20, "After the bunker blast the island seemed even more silent. They stayed in the shade of some huge trees on the shore.")
sh(21, "Habeeb had gathered dry fronds and lit a fire — not only for warmth, but in the hope that a vessel passing at sea would see its light.",
   [("fire_crackle", "އަލިފާންގަނޑެއް", -18)])
sh(22, "Raniya's father opened his eyes. In a trembling voice he said, 'Daughter… water…' There wasn't a drop. Finding clean drinking water was no easy thing.")
sh(23, "Ashham climbed a nearby palm and picked two or three young coconuts. He cut one open and passed it to Raniya. 'Sir,'",
   [("leaves_rustle", "ރުކަކަށް", -20), ("soft_thud", "ކަނޑާލުމަށްފަހު", -22)])
sh(24, "'by now Fairooz will have brought everything under his control,' Habeeb said, watching the fire.")
sh(25, "'With Moosa Thaahir's money and Fairooz's power joined together, how can we stop them?' 'Money and power,'")
sh(26, "'are like a scrap of paper before the truth.' Ashham looked at the hard drive. 'In here is the video of Fairooz himself ordering Naail's killing,'")
sh(27, "'and the dealings with the international company. The moment we reach Malé, their ruin begins.'")
sh(28, "'But how will we get to Malé?' Raniya asked. At that moment a powerful light appeared far out at sea. It was no ordinary boat's light.")
sh(29, "It was a searchlight. The trap: Ashham at once threw sand over the fire and put it out. 'Everyone down!' he ordered.",
   [("leaves_rustle", "ތިރިވޭ", -20)])
sh(30, "The light was heading for the island's lagoon. It was Fairooz's guards' launch. They had come back to check the blast site,",
   [("boat_engine", "ލޯންޗެވެ", -18)])
sh(31, "to make sure no sign of Ashham's group could be seen. The launch slowly came in toward the beach. Three armed men got off.",
   [("footsteps_sand", "ފޭބިއެވެ", -18)])
sh(32, "Powerful flashlights were in their hands. 'Look over here!' one of them shouted.",
   [("flashlight_click", "ފްލޭޝްލައިޓްތައް", -18)])
sh(33, "What he saw was the smoke of the fire Ashham's group had just put out. 'They're alive! Find them!' another ordered.",
   hum=True)
sh(34, "Ashham told Habeeb and the others to wait among the trees, loaded the last rounds he had, and slipped around behind the guards.",
   [("leaves_rustle", "ޖެހިލިއެވެ", -22)])
sh(35, "This was the only chance they would get to seize the launch. With it, the way to Malé would open. Crawling through the darkness, Ashham",
   [("footsteps_sand", "ފިރުކެމުން", -22)])
sh(36, "grabbed the last man and brought him down. He took the man's weapon and turned on the other two.",
   [("soft_thud", "ވައްޓާލިއެވެ", -23)])
sh(37, "After a short clash in the pitch dark, through Ashham's skill all three men were put out of action.",
   [("soft_thud", "ކުރިމަތިލުމަކަށްފަހު", -24)], hum=True)
sh(38, "But then someone began firing from inside the launch. One man was still aboard — their captain. The hope of escape:")
sh(39, "The rounds struck the tree beside Ashham. The weapon in Ashham's hand was empty.",
   [("soft_thud", "ރުކަށް", -22)])
sh(40, "The captain started the launch's engine and tried to back away. 'No! That's our only way out!' Habeeb burst out from the trees,",
   [("engine_rev", "ސްޓާޓުކޮށްލަމުން", -16)])
sh(41, "ran and plunged into the sea. He swam and grabbed hold of the rail at the launch's stern.",
   [("splash", "ފުންމާލިއެވެ", -14)])
sh(42, "As the captain spotted Habeeb and reached for his pistol, Ashham sprinted, leapt, and landed right inside the launch.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(43, "He seized the captain's arm, took the weapon and threw him into the sea. The launch was now under Ashham's control — a big twin-engine launch.",
   [("splash", "ކޮއްޕާލިއެވެ", -14)])
sh(44, "It had a full load of fuel and communication equipment. 'Habeeb! Quickly, bring Raniya and her father!'")
sh(45, "Ashham shouted, gripping the wheel. Habeeb brought Raniya and her father aboard the launch.")
sh(46, "As the cabin lights came on, the radar showed the course to Malé. 'Sir, this launch has full satellite navigation,' Habeeb said with a smile.",
   [("power_up", "ދިއްލާލުމާއެކު", -18), ("computer_beep", "ރާޑަރުން", -20)])
sh(47, "'Fairooz will think we're dead. But we're going to Malé.' The launch left Kandu-huttaa's lagoon,",
   [("boat_engine", "ލޯންޗު", -16)])
sh(48, "cutting through the waves and setting course out into the Huvadhu channel. The destination was Malé. They were now on a journey of revenge. Shadow on the sea:")
sh(49, "Saved from Kandu-huttaa's horrors, the launch 'Eagle Speed' carrying Ashham's group pushed on, cutting through the swell.")
sh(50, "In the pitch darkness of the night nothing could be seen but the white wake forming behind the launch.")
sh(51, "Silence filled the launch. Raniya sat with her father's head in her lap, at peace that his breathing was steadying. 'Sir, we're now entering Malé's regional radio signal range,'")
sh(52, "Habeeb said, watching the launch's navigation screen. 'But I'm still not contacting the police on any official channel,'")
sh(53, "'because ACP Fairooz controls the whole communications network.' 'Good,' Ashham said, gripping the wheel hard.")
sh(54, "'Fairooz thinks we turned to ash inside that bunker. We won't come in to Malé's main harbour — his guards will be there.'")
sh(55, "'We have to slip in secretly at a lonely spot in Hulhumalé.' Ashham took the small hard drive from his pocket and looked at it.")
sh(56, "It was their only weapon. The evidence in it was dangerous enough to cut Fairooz's power down completely. But before revealing it,")
sh(57, "they had to find out what trap Fairooz was preparing in Malé.")
sh(58, "Malé's nerve centre: at that moment, in the top-floor office of Malé police headquarters, Assistant Commissioner Fairooz sat in his comfortable chair.")
sh(59, "On the big TV screen in front of him were satellite photos of the island's bunker blown up and completely destroyed.")
sh(60, "A smile of victory showed on his face. The office door opened and in walked the tycoon Moosa Thaahir.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(61, "His face showed exhaustion and unease. 'Fairooz, is it all finished?' Moosa asked. 'Yes, Moosa.'")
sh(62, "'The bunker has been completely destroyed. Ashham, his helper and that doctor are buried beneath it now,' Fairooz said, sipping from his coffee cup.",
   [("cup_clatter", "ތަށީގައި", -20)], hum=True)
sh(63, "'Every problem your son Naail created is now solved. Not a single trace of Project Phenix will remain.'")
sh(64, "'The medicines in the Malé warehouse are ready to ship abroad.' 'But won't questions about Ashham's death come up inside the police?' Moosa worried.")
sh(65, "'I've already prepared the official report,' Fairooz said, showing a file on the desk.",
   [("paper_shuffle", "ފައިލެއް", -18)])
sh(66, "'It says Ashham and Habeeb took bribes in the Naail murder case and were trying to flee the country with criminals.'")
sh(67, "'The report will conclude that the launch they were on sank at sea. Tomorrow morning I'll release the news to the media.'")
sh(68, "Moosa let out a deep breath. Even after his own son's death, to save his business and influence, he had to take part in Fairooz's ruthless plan.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -18)], hum=True)
sh(69, "The Hulhumalé shore: at three in the early morning, Ashham's launch drew close to an area of Hulhumalé's second phase.",
   [("boat_engine", "ކައިރިކުރިއެވެ", -18)])
sh(70, "It was a place with few street lights where people don't usually go. After the engine was cut, Ashham stepped off first.",
   [("footsteps_sand", "ފޭބިއެވެ", -18)])
sh(71, "Behind him Habeeb, Raniya and her father got off. 'Habeeb, is there anyone in Malé we can trust?'")
sh(72, "Ashham asked. 'Our former senior officer, retired Commissioner Faahid,' Habeeb said, thinking.")
sh(73, "'He was removed from his post for opposing Fairooz's influence and crimes. He lives in a flat in Hulhumalé.'")
sh(74, "'We can trust him.' 'Right, we'll go to him,' Ashham said. Still damp from the sea,")
sh(75, "they walked through Hulhumalé's dark streets and entered the building where Faahid's flat was. They took the lift up,",
   [("footsteps_pavement", "ހިނގާފައި", -20)])
sh(76, "and at a door on the fourth floor Ashham knocked softly. Faahid opened the door. Seeing who stood before him, his eyes went wide. 'Ashham?'",
   [("knock", "ޓަކިޖަހާލިއެވެ", -14), ("door_open", "ހުޅުވާލީ", -18)])
sh(77, "'Habeeb? You… they're saying you're dead!' 'We're alive, sir,' Ashham said, stepping inside.",
   [("door_close", "ވަންނަމުން", -22)])
sh(78, "'And we've come with evidence that will shake the entire police institution.' The truth revealed:")
sh(79, "On the table in the main room of Faahid's home Ashham set down his hard drive. It was connected to Faahid's computer. Fairooz",
   [("keyboard_typing", "ކޮމްޕިއުޓަރަށް", -20)])
sh(80, "ordering Naail's killing on video, and the documents of the experiments done on humans on Kandu-huttaa — seeing them, Faahid's face filled with extreme fury.",
   hum=True)
sh(81, "'This is a huge betrayal!' Faahid struck the table with his hand. 'Fairooz has disgraced the name of the whole institution.'",
   [("soft_thud", "ޖެހިއެވެ", -16)])
sh(82, "'He's working to put out a statement tomorrow morning presenting you as criminals.' 'We have to show this evidence to the whole country before he does,'")
sh(83, "Ashham said. 'But how do we do that?' 'Tomorrow at nine there's a big press conference at police headquarters,' Faahid said thoughtfully.")
sh(84, "'Fairooz will speak at it himself. We have to break into that conference's live broadcast'")
sh(85, "'and release this video to every TV channel.' 'I can do that,' Habeeb said keenly.")
sh(86, "'But for that I'll have to get near the main server room of the headquarters building.' Into another trap:")
sh(87, "As the sun rose and Malé's bustle began, Ashham and Habeeb, with Faahid's help, were dressed in official police uniforms.")
sh(88, "With caps and dark glasses to hide their faces, they went to Malé in Faahid's own car.",
   [("car_door", "ކާރުގައި", -18)])
sh(89, "Raniya and her father stayed safe at Faahid's home. When the car stopped in front of headquarters, a large crowd of journalists had gathered there.",
   [("camera_shutter", "ނޫސްވެރިން", -20)])
sh(90, "All of them were impatient for the details of Ashham and Habeeb's 'death'. Ashham and Habeeb slipped into a group of police and secretly entered the building.",
   [("boots_march", "ގްރޫޕެއްގެ", -20)])
sh(91, "Their hearts pounded harder, because they knew they were walking into a trap. 'Habeeb,'",
   [("heartbeat", "ތެޅުން", -18)], hum=True)
sh(92, "'you go toward the server room,' Ashham said quietly. 'I'm going to the press hall — face to face with Fairooz.' The two set off in different directions. — To be continued —",
   [("footsteps_pavement", "މިސްރާބު", -20)])

SHOTS = S

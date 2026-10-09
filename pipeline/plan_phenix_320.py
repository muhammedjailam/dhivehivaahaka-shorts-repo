"""Beat/shot plan for Project Phenix episode 320 (used by plan_beats.py)."""

LOC = {
    "cargo_boat": "a weathered wooden-and-steel cargo supply boat travelling south across the open Maldivian sea, an open deck stacked with lashed wooden crates and sacks, a small wheelhouse, the low skyline of Malé's north harbour fading behind",
    "cargo_cabin": "the small cramped cabin of a cargo supply boat at sea, a narrow bench, a fold-down table, a small round window looking out on the grey sea",
    "villingili_harbour": "Villingili island harbour in Gaafu Alifu atoll at 9 pm, a concrete quay under a few dim yellow lamps, dark narrow sandy island lanes lined with coral-stone walls and breadfruit trees leading inland",
    "hospital_lane": "a dark sandy island lane at night leading to a quiet two-storey atoll hospital building with a few lit windows and a small lit emergency entrance",
    "hospital_corridor": "the empty upstairs corridor of a two-storey island hospital at night, pale green walls, a few dim ceiling lights, closed wooden office doors with plain blank nameplates, a polished floor",
    "raniya_office": "Dr. Raniya's small office in the island hospital: a wooden desk with stacked files and a desk lamp, a plain chair behind it, a window with dark rain outside, a filing cabinet, a heavy metal file holder on the desk",
    "office_dark": "Dr. Raniya's small hospital office plunged into total darkness, the desk with files and a heavy metal file holder, a rain-streaked window giving a faint cold glow, the wooden door to the corridor",
    "corridor_dark": "the long hospital corridor in total darkness, pale walls, closed doors, a faint emergency glow at the far end, rain-streaked windows",
    "hospital_garden": "the back garden of the island hospital at night in the rain: a lit back door, wet hibiscus and breadfruit trees, a sandy path disappearing into dark island lanes",
    "old_jetty": "an abandoned old wooden jetty on the island's west shore at night in rain, broken planks and leaning posts, black water, dense dark bushes and screwpine at the shoreline",
    "storm_sea": "the open sea between islands in a violent storm at night, huge black waves with white foaming crests, salt spray, black clouds, lightning",
    "kandu_beach": "the white sand beach of Kandu-huttaa, a deserted jungle-covered island, at night: a narrow channel through the reef behind, dense black jungle of screwpine, magoo bushes and coconut palms right behind the beach",
    "kandu_jungle": "inside the dense dark jungle of Kandu-huttaa at night: screwpine, magoo bushes and coconut palms; in a small clearing a low concrete block set into the ground with a heavy rusted steel hatch-door and a small electronic keypad panel beside it",
    "kandu_lagoon": "the lagoon of Kandu-huttaa at night seen from the edge of the jungle: black calm water inside the reef, the dark jungle-covered island, a stormy sky",
}
MOOD = {
    "cargo_boat": "dim grey-blue dawn light, a pale pink glow low on the horizon, calm sea, quiet secrecy and tension",
    "cargo_cabin": "cool grey daylight from the small window, the blue glow of a laptop, darkening storm clouds gathering outside, uneasy silence",
    "villingili_harbour": "night, cold navy-blue darkness, a few warm dim yellow lamps, damp air, watchful and quiet",
    "hospital_lane": "night, cold navy-blue darkness, the warm glow of the hospital's lit windows, deep shadows, silent and eerie",
    "hospital_corridor": "night, flat dim fluorescent light, long shadows, deserted and tense",
    "raniya_office": "night, the warm amber desk lamp against cold navy-blue shadows, rain on the window, fear and tension",
    "office_dark": "night, sudden total blackout: cold navy-blue darkness, only faint moonlight from the rain-streaked window and thin white flashlight beams, terror",
    "corridor_dark": "night, blackout, cold navy-blue darkness, a faint red emergency glow at the far end, bursts of grey dust in torchlight, panic",
    "hospital_garden": "night, heavy rain, cold navy-blue darkness, the warm light of the open back door behind, urgent escape",
    "old_jetty": "night, heavy rain, cold navy-blue darkness, faint moonlight through black clouds, wet glistening planks, exhaustion and fear",
    "storm_sea": "storm at night: black sea, white spray, flashes of lightning, a blinding white searchlight beam, deadly danger",
    "kandu_beach": "night, cold navy-blue darkness after the storm, faint moonlight breaking through clouds, white sand glowing softly, exhausted and ominous",
    "kandu_jungle": "night, cold navy-blue darkness, faint moonlight through the leaves, the small green glow of the keypad and white flashlight beams, silent dread",
    "kandu_lagoon": "night, cold navy-blue darkness, a powerful white searchlight sweeping across the black lagoon, menacing",
}

A = ("Ashham in plain civilian clothes (not a uniform): a dark-grey long-sleeved button shirt and dark trousers, "
     "short dark stubble")
AD = A + ", damp and dusty"
H = "Habeeb in his dark-grey zip-up jacket and black-rimmed glasses"
R = "Dr. Raniya in her white doctor's coat over a dusty-blue dress, navy hijab fully covering her hair and neck"
RW = ("Dr. Raniya WITHOUT her white coat: a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully "
      "covering her hair and neck, soaked dark by rain and spray but fully opaque")
LOW = "faces in the upper two-thirds, a calm dark lower third"

BEATS = [
    # ---------------- CARGO BOAT SOUTH
    dict(to=3, reason="episode opening: dawn, a cargo boat leaving Malé's north harbour with Ashham and Habeeb as secret passengers",
         chars=["ashham", "habeeb"], loc="cargo_boat",
         visual=f"{A} and {H} sitting quietly among lashed wooden crates on the open deck of the cargo boat as it pulls away from Malé's north harbour at dawn, Habeeb with a laptop bag on his knees, Ashham looking back at the fading city skyline with a grave face; plain unmarked crates",
         camera=f"medium wide shot from the deck, eye level, {LOW} (the wet wooden deck)", amb="sea_boat"),
    dict(to=7, reason="action change: in the cabin Habeeb tracks Raniya on the satellite modem; Ashham watches the storm brewing through the window",
         chars=["habeeb", "ashham"], loc="cargo_cabin",
         visual=f"{H} hunched at the fold-down table over his open laptop and a small satellite modem with a blinking light, the screen angled away from the viewer, its blue glow on his glasses; {A} standing by the small round window looking out at dark storm clouds gathering over the grey sea, arms folded, serious",
         camera=f"medium shot, eye level, {LOW} (table top)", amb="sea_boat"),
    # ---------------- VILLINGILI
    dict(to=10, reason="time and scene change: next night at 9 pm they land at Villingili and walk the dark lanes to the quiet two-storey hospital",
         chars=["ashham", "habeeb"], loc="hospital_lane",
         visual=f"{A} and {H} (with a backpack) walking side by side up a dark sandy island lane between coral-stone walls, seen slightly from behind, glancing around warily; ahead at the end of the lane the quiet two-storey island hospital with a few lit windows and a small lit emergency door; far behind them a dim yellow harbour lamp",
         camera=f"medium wide shot, eye level, slightly from behind, the hospital and figures in the upper two-thirds, {LOW} (dark sandy lane)",
         amb="island_night", transition="black"),
    dict(to=11, reason="location change: inside the corridor Habeeb keeps watch while Ashham knocks on Dr. Raniya's door",
         chars=["ashham", "habeeb"], loc="hospital_corridor",
         visual=f"{A} knocking softly with his knuckles on a closed wooden office door with a blank nameplate in the empty dim corridor; a few steps behind him {H} keeping watch, glancing back down the corridor",
         camera=f"medium wide shot down the corridor, eye level, {LOW} (polished floor)", amb="hospital_corridor"),
    # ---------------- RANIYA'S OFFICE
    dict(to=14, reason="character enters: Dr. Raniya at her desk, frightened by the two strangers; Ashham shows his police card",
         chars=["raniya", "ashham", "habeeb"], loc="raniya_office",
         visual=f"{R} standing up behind her desk with stacked files, startled and frightened, one hand raised in front of her; across the room near the closed door {A} holding up a small blank police ID card with no writing, calm and firm; {H} just behind him by the door; a wide gap between her and the men",
         camera=f"medium wide shot, eye level, {LOW} (desk top and floor)", amb="hospital_room"),
    dict(to=18, reason="emotional turning point: hearing Naail's and her father's names she breaks down into her chair",
         chars=["raniya", "ashham", "habeeb"], loc="raniya_office",
         visual=f"{R} sunk into the chair behind her desk, her face in her hands, crying, shoulders shaking; {A} and {H} standing on the other side of the desk at a respectful distance, looking at her with grave sympathy",
         camera=f"medium shot, eye level, {LOW} (desk top with files)", amb="hospital_room", hum=True),
    dict(to=22, reason="framing change: calmer now, Raniya reveals the secret lab on Kandu-huttaa; Ashham leans in to ask who is behind it",
         chars=["raniya", "ashham"], loc="raniya_office",
         visual=f"close-up of {R} sitting at her desk, eyes red from crying, speaking urgently in a low voice, one hand pressed flat on a closed file; the shoulder of {A} soft and out of focus in the foreground as he leans forward across the desk",
         camera=f"close-up over Ashham's shoulder, eye level, {LOW} (desk top)", amb="hospital_room",
         sens="other", safe="the human experiments and trafficking are only described in her words; nothing of the lab is shown"),
    # ---------------- BLACKOUT AND ATTACK
    dict(to=25, reason="emotional turning point: every light in the hospital goes out; boots in the corridor; Ashham holds the door",
         chars=["ashham", "raniya", "habeeb"], loc="office_dark",
         visual=f"the office in sudden darkness: {A} braced with his shoulder against the closed wooden door, holding the handle, tense; {H} at the window pushing it open; {R} pressed back against the filing cabinet, hands clasped at her own chest, eyes wide with terror; thin white lines of flashlight light under the door",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="hospital_night", hum=True),
    dict(to=27, reason="action change: the door bursts open and three masked men stand in the doorway (no weapons shown)", loc="office_dark",
         visual="the office door flung open: three tall dark silhouettes of men in black clothes and black face masks standing in the doorway, their empty hands holding only bright white flashlights whose beams cut through the dark room toward the viewer; nothing else in their hands",
         camera=f"medium wide shot from inside the room, low angle, the silhouettes in the upper two-thirds, {LOW} (dark floor)",
         amb="hospital_night", sens="violence",
         safe="armed attackers shown as masked silhouettes with flashlights only; the rifle-butt blow to Ashham's forehead is never shown (muffled thud only)"),
    dict(to=30, reason="character focus change: in the dark, Raniya and Habeeb pressed against the wall as flashlight beams sweep",
         chars=["raniya", "habeeb"], loc="office_dark",
         visual=f"{H} and {R} pressed against the wall side by side in the dark office, not touching, a small gap between them, Raniya's hands clasped tightly at her own chest, both staring in fear toward the door; a white flashlight beam sweeping across the wall above their heads",
         camera=f"medium shot, eye level, {LOW} (dark floor)", amb="hospital_night", sens="violence",
         safe="Ashham falling and being held by the collar are never shown; Raniya 'gripping Habeeb's arm' is shown as her standing close beside him with her hands at her own chest (bible rule 8)"),
    dict(to=33, reason="action change: Ashham's eyes adjust to the dark and fix on the heavy metal file holder", chars=["ashham"], loc="office_dark",
         visual=f"close-up of {A} crouched low beside the desk in the dark, his intense eyes fixed on a heavy metal file holder standing on the desk edge, a flashlight beam glancing across his tense face; his hands empty",
         camera=f"close-up, low angle, {LOW} (dark desk side)", amb="hospital_night", sens="violence",
         safe="the strike with the file holder, the dropped gun and the tackle are never shown; only Ashham's focused face before he moves, muffled thuds offscreen"),
    dict(to=35, reason="scene change: Habeeb and Raniya flee down the dark corridor; dust bursts from the wall behind them",
         chars=["habeeb", "raniya"], loc="corridor_dark",
         visual=f"{H} and {R} running side by side down the dark hospital corridor toward the viewer, not touching, faces full of fear; behind them small bursts of grey cement dust and sparks puff from the corridor wall in a flashlight beam; nobody is hit",
         camera=f"medium wide shot, eye level, down the corridor, {LOW} (polished floor)", amb="hospital_corridor", hum=True,
         sens="violence", safe="gunfire shown only as dust and sparks bursting from the wall far behind them; Habeeb 'pulling Raniya by the hand' shown as running side by side"),
    dict(to=38, reason="action change: Ashham follows out the back door; the three vanish into the rainy island lanes",
         loc="hospital_garden",
         visual="seen from behind: three running figures slipping through the rainy back garden of the hospital away from the lit back door toward the dark island lanes - a tall man in a dark-grey shirt, a slim young man in a grey jacket with glasses, and a slim woman in a white coat and navy hijab - side by side with gaps between them, not touching; rain glittering in the light",
         camera=f"wide shot from behind, eye level, {LOW} (wet sandy path)", amb="rain_night",
         sens="violence", safe="Ashham overpowering the attackers and taking their ammunition is never shown; only the escape from behind"),
    # ---------------- OLD JETTY
    dict(to=40, reason="scene change: at the abandoned jetty on the west shore they stop, breathless; Raniya soaked and trembling",
         chars=["raniya", "ashham", "habeeb"], loc="old_jetty",
         visual=f"{RW}, standing on the old wet jetty planks trembling, arms wrapped around herself, frightened; {AD} a few steps away scanning the dark shoreline; {H} bent over catching his breath, hands on his knees; clear gaps between them, rain falling",
         camera=f"medium wide shot, eye level, {LOW} (dark wet planks and black water)", amb="rain_night"),
    dict(to=43, reason="action change: they pull the hidden fibreglass dinghy out of the bushes; Habeeb climbs in with his laptop",
         chars=["ashham", "habeeb", "raniya"], loc="old_jetty",
         visual=f"{AD} dragging a small white fibreglass dinghy with a small outboard engine out of the dark bushes into the shallow black water; {H} stepping into it clutching his laptop bag; {RW} standing a few steps away on the shore pointing toward the bushes; rain",
         camera=f"medium wide shot, eye level, {LOW} (black shallow water)", amb="rain_night"),
    dict(to=48, reason="action change: under black clouds Ashham starts the outboard; Raniya grips the side as they head out into big waves",
         chars=["ashham", "raniya", "habeeb"], loc="old_jetty",
         visual=f"the small white fibreglass dinghy beside the old jetty in rough black water. At the bow: {RW} - she wears NO white coat and NO lab coat at all, only the dark wet dusty-blue dress - gripping the dinghy's side with both hands, determined but afraid. In the middle {H} looking up anxiously at huge black storm clouds. At the stern {AD} pulling the outboard engine's starter cord. Gaps between them",
         camera=f"medium wide shot, eye level, {LOW} (choppy black water)", amb="rain_night"),
    # ---------------- STORM CROSSING
    dict(to=51, reason="scene change: the storm at full force; huge waves over the dinghy, Habeeb bailing water",
         chars=["habeeb", "ashham", "raniya"], loc="storm_sea",
         visual=f"the tiny dinghy climbing a towering black wave, white spray exploding over it; {H} bailing water with a plastic scoop, a waterproof bag strapped to his chest; {AD} at the outboard tiller squinting into the spray; {RW} crouched low gripping the side; lightning in the black clouds",
         camera=f"medium wide shot, slightly low angle, {LOW} (dark foaming water)", amb="storm_night", hum=True),
    dict(to=54, reason="action change: a powerful searchlight sweeps toward them; Ashham looks back at two fast launches",
         chars=["ashham"], loc="storm_sea",
         visual=f"{AD} sitting low inside the small white fibreglass dinghy, the dinghy's white hull and gunwale clearly visible around him, one hand resting on the long arm of the small outboard engine mounted on the stern beside him, twisting to look back over his shoulder, drenched, his face lit hard white by a powerful searchlight beam coming across the black waves from two dark fast launches in the distance behind; spray in the air",
         camera=f"medium close-up, eye level, {LOW} (black water)", amb="storm_night"),
    dict(to=57, reason="action change: the criminals' launches close in; spray bursts around the little dinghy (no gunfire shown)",
         loc="storm_sea",
         visual="wide view of the stormy black sea at night: two large dark fast launches with no markings racing through the waves, a blinding white searchlight beam pinning a tiny dinghy ahead of them, small white plumes of spray bursting from the water around the dinghy; lightning",
         camera=f"wide shot, high angle, the launches and searchlight in the upper two-thirds, {LOW} (black foaming sea)",
         amb="storm_night", hum=True, sens="violence", safe="gunfire shown only as spray plumes on the water; no weapons, nobody hit"),
    dict(to=61, reason="emotional turning point: Ashham targets the searchlight; it bursts and the sea goes dark",
         loc="storm_sea",
         visual="seen from behind: the dark silhouette of a broad-shouldered man in a dark shirt standing braced in the stern of a small dinghy, one arm raised toward the launch behind, his hand not visible against the glare; the big searchlight on the launch's bow bursting in a shower of white-orange sparks and glass fragments, the beam dying; a huge wave rising between the boats",
         camera=f"medium wide shot from behind the man, low angle, {LOW} (black water)", amb="storm_night",
         sens="violence", safe="Ashham's shot is shown only as his raised arm in silhouette from behind and the searchlight bursting into sparks; no gun visible"),
    # ---------------- KANDU-HUTTAA
    dict(to=65, reason="scene change: through the reef channel; the engine smokes and dies; they climb onto Kandu-huttaa's beach exhausted",
         chars=["raniya", "ashham", "habeeb"], loc="kandu_beach",
         visual=f"the small dinghy beached on white sand, thin grey smoke rising from its stalled outboard engine; {AD} stepping onto the sand, exhausted; {H} climbing out with his bag; {RW} standing on the beach a few steps apart, staring with dread at the pitch-black jungle; clear gaps between them",
         camera=f"medium wide shot, eye level, the jungle and figures in the upper two-thirds, {LOW} (white sand)", amb="beach_night"),
    dict(to=68, reason="action change: Habeeb checks his laptop - a jammer from the bunker blocks all messages",
         chars=["habeeb", "ashham", "raniya"], loc="kandu_beach",
         visual=f"{H} kneeling on the sand with his open laptop on his knees, the screen angled away from the viewer, its faint blue glow lighting his worried face and glasses; {AD} standing beside him looking toward the jungle, decisive; {RW} a little behind Ashham, hands at her chest",
         camera=f"medium shot, eye level, {LOW} (white sand)", amb="beach_night"),
    dict(to=72, reason="scene change: through the jungle they find the bunker's steel door, guarded by two men",
         chars=["ashham"], loc="kandu_jungle",
         visual=f"{AD} crouched in the dark bushes in the foreground, seen from behind and to the side, watching; beyond the leaves the heavy rusted steel hatch-door in its low concrete block, two guards in black clothes and black face masks standing before it holding only flashlights, beams sweeping the ground",
         camera=f"medium wide shot over Ashham's shoulder, eye level, {LOW} (dark undergrowth)", amb="jungle_night",
         sens="violence", safe="armed guards shown with flashlights only"),
    dict(to=75, reason="action change: the guards are gone; Ashham calls the others to the door", chars=["ashham"], loc="kandu_jungle",
         visual=f"the bunker's steel hatch-door with nobody guarding it; a dropped flashlight lying in the grass casting its beam across the ground; {AD} standing at the door alone, breathing hard, beckoning urgently with one empty hand toward the bushes",
         camera=f"medium wide shot, eye level, {LOW} (dark grass)", amb="jungle_night",
         sens="violence", safe="Ashham taking down both guards is never shown; only the empty doorway and the dropped flashlight afterwards; nobody on the ground"),
    dict(to=76, reason="detail: Raniya's trembling finger types the code on the keypad", chars=["raniya"], loc="kandu_jungle",
         visual=f"close-up of {RW}, her face tense in profile, her trembling finger reaching toward a small electronic keypad panel beside the steel door, its blank keys glowing soft green with no numbers or symbols",
         camera=f"close-up, eye level, {LOW} (concrete surface)", amb="jungle_night"),
    dict(to=77, reason="action change: the steel door groans open; cold chemical air pours out",
         chars=["ashham", "raniya", "habeeb"], loc="kandu_jungle",
         visual=f"the heavy steel hatch-door swinging open, cold pale mist spilling out from a dark stairway leading down under a faint cold fluorescent glow; {AD} at the edge peering down, alert; {H} and {RW} behind him at a distance, frightened faces lit by the cold light",
         camera=f"medium wide shot, eye level, {LOW} (dark ground)", amb="jungle_night", hum=True),
    dict(to=79, reason="scene change: they shut themselves in as the criminals' big launch roars into the lagoon",
         loc="kandu_lagoon",
         visual="a large dark launch with no markings roaring into the black lagoon of the deserted island, a powerful white searchlight sweeping across the water toward the dark jungle; no people visible",
         camera=f"wide shot from the jungle edge, eye level, the launch and searchlight in the upper two-thirds, {LOW} (black water)",
         amb="beach_night", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "In the dim light of dawn, Ashham and Habeeb were aboard a cargo boat that had left Malé's north harbour.",
   [("boat_engine", "ބޯޓެއްގެ", -20)])
sh(2, "This boat carries goods to the southern atolls. Because the boat's captain was an old friend of Ashham's,")
sh(3, "they boarded the boat as secret passengers. Habeeb sat using his satellite modem to follow Dr. Raniya's movements. \"Sir,",
   [("keyboard_typing", "މޮޑެމް", -24)])
sh(4, "Raniya is on duty at the hospital now. Her phone's location shows it's there. But there are many calls from unknown numbers around her too.\"",
   [("phone_buzz", "ކޯލްތަކެއް", -24)])
sh(5, "\"Those are their guards,\" Ashham said, looking out of the window. \"Raniya is inside a locked cage.")
sh(6, "Unless she's saved, we won't learn the truth.\" The rest of the voyage passed in silence.")
sh(7, "Yet both of them knew that behind that silence lay the secret of a great storm. Reaching the island: the next night at nine,",
   [("thunder", "ތޫފާނެއްގެ", -22)], hum=True)
sh(8, "the boat came alongside GA. Villingili harbour. The harbour lay under a few dim lamps. Dressed like ordinary people, Ashham and Habeeb",
   [("boat_engine", "ކައިރިކުރިއެވެ", -22)])
sh(9, "got off the boat and walked through the dark lanes toward the hospital. The island's hospital is a two-storey building.",
   [("footsteps_sand", "ހިނގާފައި", -22)])
sh(10, "At that hour the hospital was very quiet. Entering through the emergency door, Ashham headed toward where the doctors' rooms were.",
   [("door_open", "ވަދެ", -22)])
sh(11, "While Habeeb kept watch, Ashham went and knocked on the door of the room bearing Dr. Raniya's name. \"Come in,\" came a woman's voice from inside.",
   [("knock", "ޓަކިޖަހާލިއެވެ", -16)])
sh(12, "Ashham went in, closed the door and locked it. Raniya sat at her desk looking through files. As she raised her head,",
   [("door_close", "ލައްޕާ", -20), ("lock_click", "ތަޅުލިއެވެ", -20)])
sh(13, "seeing two strangers before her she took fright. \"Who are you? Get out of here!\" Raniya stood up. \"Dr. Raniya, stay calm,\" Ashham said, showing his police card.",
   [("gasp", "ބިރުގަތެވެ", -22)])
sh(14, "\"I'm Ashham, police Serious Crimes. We came about Naail's death. And to save your father.\"")
sh(15, "At the names of Naail and her father, tears spilled from Raniya's eyes. Her legs gave way and she sank onto the chair. \"You...",
   [("sob_breath", "ކަރުނަ", -24), ("cloth_rustle", "ތިރިވެވުނެވެ", -24)], hum=True)
sh(16, "you know everything?\" \"Yes, we have the recording of Naail's phone call,\" said Habeeb.")
sh(17, "Raniya put her hands over her face and began to cry. \"They killed Naail. I told him not to get involved in this.",
   [("sob_breath", "ރޯން", -22)], hum=True)
sh(18, "They are not people with any mercy.\" Locked in: once she had calmed down, Raniya began to talk.")
sh(19, "\"On Kandu-huttaa there is a secret lab of a foreign pharmaceutical company. They are developing a new master drug there.")
sh(20, "To test that drug they use foreigners smuggled into the Maldives in secret. There is a great deal of human trafficking in this.")
sh(21, "Naail found out because their shipments came in through his father's company.\" \"Who is the mastermind in Malé?\"")
sh(22, "Ashham asked, leaning forward. Just as Raniya opened her mouth to say something, suddenly every light in the hospital went out.",
   [("power_down", "ނިވުނެވެ", -16)], hum=True)
sh(23, "The whole place sank into darkness. \"Sir! The backup power has been cut too!\" Habeeb said in alarm.",
   [("breath_heavy", "ހާސްވެފައި", -24)])
sh(24, "At that moment, from the corridor came the sound of heavy boots and of guns being loaded. They were coming into the hospital. \"They're here!\"",
   [("boots_march", "ބޫޓުތަކެއްގެ", -18), ("lock_click", "ލޯޑްކުރާ", -22)], hum=True)
sh(25, "Raniya cried out in fear. \"Habeeb, open the window! We have to get out of here!\" Ashham said, grabbing the door and holding it shut.",
   [("gasp", "ހަޅޭއްލަވައިގަތެވެ", -18)])
sh(26, "At that moment the door was flung open with a loud bang, and three armed men in black masks came in.",
   [("door_slam", "ހުޅުވާލާފައި", -14)], hum=True)
sh(27, "The butt of one man's gun struck Ashham on the forehead. Escape from the hospital:",
   [("soft_thud", "ޖެހިއެވެ", -23)])
sh(28, "In the pitch darkness that filled the room, Ashham fell. One of the men in black masks held him by the collar.",
   [("cloth_rustle", "ހިފެހެއްޓިއެވެ", -22)])
sh(29, "The man's breathing could be heard close by. Raniya was beside Habeeb; in fear she gripped Habeeb's arm tightly. \"Move, forward, without a sound!\"",
   [("breath_heavy", "ނޭވާގެ", -20)])
sh(30, "the man in front ordered Ashham in a heavy voice. Ashham is an experienced officer who has faced many dangerous situations like this.")
sh(31, "As his eyes got used to the dark, he noticed the heavy metal file holder lying on the desk. Suddenly,",
   [("heartbeat", "ފާހަގަކުރިއެވެ", -20)], hum=True)
sh(32, "without any warning, Ashham ducked down and swung the holder at the head of the man in front.",
   [("soft_thud", "ވީއްލާލިއެވެ", -22)])
sh(33, "With that, the gun fell from his hand to the floor. \"Habeeb! Out the door!\" Ashham shouted, and grabbing the second man hard, brought him to the floor.",
   [("metal_clang", "ވެއްޓުނެވެ", -22), ("soft_thud", "ވައްޓާލިއެވެ", -24)])
sh(34, "Habeeb took Raniya by the hand and ran out of the room's door. At that moment the third man began firing after them. \"Tishun..",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)], hum=True)
sh(35, "tishun\" - the bullets struck the corridor wall. Cement flew off the hospital wall. From all around, the sound of people screaming and crying echoed.",
   [("crash_clatter", "ބުރައިގެން", -22)])
sh(36, "Lying on the floor, Ashham attacked them with their own guns and brought two of them down. The third man lay unconscious from the hard blow to his head.")
sh(37, "Taking the rounds left in their guns, Ashham ran after Habeeb and the others and came out through the hospital's back door.",
   [("door_open", "ދޮރުން", -20)])
sh(38, "They came out through the hospital's back garden and vanished into the island's dark lanes. It was still raining.",
   [("rain_start", "ވާރޭ", -18)])
sh(39, "When they reached the abandoned old jetty on the island's west shore, they were all out of breath. Raniya's clothes were soaked.",
   [("breath_heavy", "މާނޭވާލެވިފައެވެ", -18)])
sh(40, "She was trembling with fear. \"What do we do now? They'll search the whole island for us,\" Raniya said in a voice full of panic.",
   [("breath", "ތުރުތުރު", -22)])
sh(41, "\"There should be a small dinghy I hid here,\" Raniya said slowly. \"It's something I prepared to escape from the island.")
sh(42, "I tried to escape so many times. But with my father in their hands, and afraid of what they'd do, I never dared.\" They pulled out a small fibreglass dinghy hidden among the bushes and put it in the sea.",
   [("leaves_rustle", "ގަސްތަކުގެ", -18), ("splash", "މޫދަށް", -18)])
sh(43, "It had a small outboard engine. Habeeb got into it at once, trying to keep his laptop safe. \"Sir,")
sh(44, "this will be a very dangerous trip. The sea is very rough,\" Zayaan said, looking up at the sky. Black clouds covered the whole sky.",
   [("wind_gust", "ކަޅުވިލާތަކުން", -18)])
sh(45, "\"The only option we have is to go to another island near here.\" \"No, there's no time. We have to go to Kandu-huttaa.")
sh(46, "If we can get there and into that bunker, we'll learn all their secrets,\" Ashham said, starting the dinghy's engine.",
   [("boat_engine", "ސްޓާޓްކޮށްލަމުން", -16)])
sh(47, "\"Raniya, do you have the bunker code?\" \"Yes, it's on my phone. But there'll be armed guards inside,\"")
sh(48, "Raniya said, gripping the side of the dinghy. The dinghy left the island's lagoon and headed into the sea's huge waves.",
   [("wave_crash", "ރާޅުތަކުގެ", -18)])
sh(49, "Storm at sea: as soon as they were out on the open sea, the storm showed its true strength. Waves like mountains crashed down on the dinghy.",
   [("wind_howl", "ތޫފާނުގެ", -18), ("wave_crash", "ރާޅުތައް", -14)], hum=True)
sh(50, "The salt spray made it hard even to open their eyes. Habeeb sat bailing water out of the dinghy. His laptop was in its waterproof bag,",
   [("splash", "ދިޔަހިއްކާށެވެ", -20)])
sh(51, "wrapped in another plastic bag, slung round his neck and tied to his body with a strap. \"Sir! A big launch is coming from the other side!\"",
   [("engine_rev", "ލޯންޗެއް", -18)])
sh(52, "Habeeb shouted. Ashham looked back. In the distance, the light of a powerful searchlight was coming toward them over the sea spray.")
sh(53, "It was two powerful launches of the criminals. Their speed was far greater. \"They've seen us!\"",
   [("engine_rev", "ލޯންޗެވެ", -16)])
sh(54, "Raniya cried out in fear. \"Zayaan! Hold on!\" Ashham swung the dinghy's helm and drove it into the waves.",
   [("wave_crash", "ރާޅުތަކުގެ", -16)])
sh(55, "From the launch behind they began to fire. The bullets hit the sea spray with a \"pop, pop\".",
   [("splash", "ޕޮޕް", -22)], hum=True)
sh(56, "Because the waves were so strong, they kept losing their aim. Even so, they kept coming closer.")
sh(57, "It was as if the big launch would come and ram the dinghy's side and crush it. \"Sir, we're going to die!\" Habeeb shouted.",
   [("engine_rev", "ލޯންޗު", -14)], hum=True)
sh(58, "Ashham took the gun he had seized at the hospital and aimed behind. But taking aim on such a heavy wave was impossible.",
   [("heartbeat", "އަމާޒުކުރިއެވެ", -20)])
sh(59, "After a moment's thought he changed his aim to the big searchlight on the front of the launch. \"Bang!\"",
   [("soft_thud", "ބޭންގް", -22)], hum=True)
sh(60, "With a single round the searchlight burst, and the whole area was dark again. At that moment a huge wave came and crashed between the two launches.",
   [("glass_break", "ގޮވައި", -14), ("wave_crash", "ރާޅެއް", -14)])
sh(61, "With that, the criminals' launch was pushed far away. By then they were nearly at Kandu-huttaa. Seizing the chance, Ashham",
   [("engine_rev", "ލޯންޗު", -22)])
sh(62, "steered the dinghy in through a narrow channel near the island's reef. A small hope settled as they entered Kandu-huttaa's lagoon.",
   [("wave_crash", "ފަރުކައިރީގައި", -20)])
sh(63, "But smoke began to rise from the dinghy's engine. Water got into the engine and it stopped completely. The dinghy drifted slowly onto the island's white sand.",
   [("steam_hiss", "ދުން", -20), ("power_down", "ހުއްޓުނީއެވެ", -22)])
sh(64, "The three got off the dinghy and climbed onto the island's beach. They were utterly exhausted and spent. \"We've only reached the field of death,\"",
   [("footsteps_sand", "އެރިއެވެ", -18)])
sh(65, "Raniya said, looking at the pitch-dark trees around them. \"Under this island's ground is hell.\" \"Habeeb, does your equipment work?\"",
   [("leaves_rustle", "ގަސްތަކަށް", -22)], hum=True)
sh(66, "Ashham asked. Zayaan took out his laptop and opened it. The battery was at fifteen percent. \"Sir, there's a satellite signal.",
   [("computer_beep", "ހުޅުވާލިއެވެ", -22)])
sh(67, "But because of a jammer coming from this island's bunker, no message can be sent to Malé. We have to get inside the bunker and switch off the main power.\"")
sh(68, "\"Let's go,\" Ashham said. \"Raniya, stay behind me. Walk without making a sound.\"")
sh(69, "They moved forward through the trees to find the big concrete bunker door Ashham had seen before. At the bunker's door:",
   [("leaves_rustle", "ގަސްތަކުގެ", -20)])
sh(70, "Searching through the thick trees, they found that heavy steel door. This time two guards with weapons stood beside the door.",
   [("leaves_rustle", "ގަސްތަކުގެ", -22)])
sh(71, "They were very alert. \"They're guarding the bunker,\" Ashham said quietly. \"I have to take those two out.", hum=True)
sh(72, "Habeeb, wait here with Raniya.\" Ashham picked up a big stone from the ground and threw it far off. \"Thud!\"",
   [("soft_thud", "ތްލަޑް", -18)])
sh(73, "At the sound of the stone one guard went to look. Ashham came up behind him, clamped one hand over his mouth and nose, gripped him with the other arm and brought him down unconscious.",
   [("footsteps_sand", "ދިޔައެވެ", -22), ("soft_thud", "ވައްޓާލައި", -24)])
sh(74, "Just as the other guard, startled, raised his gun, Ashham ran at him, struck him in the chest and brought him to the ground.")
sh(75, "After a short struggle both guards lay on the ground. \"Come quickly!\" Ashham called. Raniya and Zayaan ran to the door.",
   [("footsteps_sand", "ދުވެފައި", -18)])
sh(76, "With her trembling hand, Raniya began typing the secret code into the bunker's electronic keypad. \"4... 8... 9... 1... 0...\"",
   [("computer_beep", "ކީޕޭޑްގައި", -20)], hum=True)
sh(77, "\"Beep!\" With a loud noise the steel door began to open. Out came cold air carrying a chemical smell. \"This is only the beginning; be careful,\" Ashham said.",
   [("computer_beep", "ބީޕް", -14), ("metal_door", "ހުޅުވެން", -14), ("wind_gust", "ވައިރޯޅިއެކެވެ", -22)])
sh(78, "\"Let's go in.\" As they went into the bunker and shut the door, the sound of a big launch entering the island's lagoon was heard outside.",
   [("metal_door", "ލެއްޕުމާއެކު", -14), ("engine_rev", "ލޯންޗެއް", -16)])
sh(79, "The criminals' main group had come to the island. Ashham and the others were now locked inside the bunker. - To be continued -",
   [("heartbeat", "ބަންދުވެފައެވެ", -18)], hum=True)
SHOTS = S

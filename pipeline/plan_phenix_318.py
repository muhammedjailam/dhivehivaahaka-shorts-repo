"""Beat/shot plan for Project Phenix episode 318 (used by plan_beats.py)."""

LOC = {
    "sea_launch": "the police fast launch at speed on the open sea, leaving a deserted jungle-covered island far behind; a plain white-and-navy launch hull with no lettering, cabin with windows, a long white wake",
    "police_office": "Serious Crimes Department office in Iskandhar Building, Malé: a desk with empty coffee cups and file stacks, a computer, a window to a busy street (Ameenee Magu)",
    "male_alley": "a narrow rain-soaked Malé alley off Majeedhee Magu, tall narrow concrete buildings close on both sides, puddles, tangled overhead wires, an old two-storey building with a dark doorway further in",
    "alley_door": "the dark doorway of an old weathered two-storey building in a narrow rain-soaked Malé alley, a peeling wooden door half open on darkness, wet concrete step",
    "gang_den": "a dark room inside the old building: a big scarred wooden table covered with papers, one bare hanging light bulb, peeling walls, closed doors behind",
    "male_port": "Malé commercial harbour at night: a concrete quay with stacked plain steel shipping containers without any markings, tall harbour lamps, wet ground, a plain dark van waiting",
    "moosa_mansion": "Moosa's luxurious living room: marble floor, big sofas, dark wood, warm lamps, a tall window streaked with rain",
    "car_rain_in": "inside a dark saloon car driving on a rainy Malé road at dusk, rain streaming down the windscreen, wipers, dashboard glow, the rear-view mirror",
    "car_rain_bridge": "Sinamalé bridge (the long modern sea bridge from Malé to Hulhumalé) in heavy rain at dusk, wet shining road, rows of bridge lamps, a steel side railing, the dark sea below",
    "hulhumale_spot": "a lonely dark stretch of Hulhumalé's seafront road, one street light, a low sea wall, empty wet road, the dark lagoon beyond",
    "safehouse": "secret police safe-house room in Hulhumalé: a bare dark room with a plain table and a few chairs, a window with rain and lightning outside, lit only by the blue glow of a laptop",
    "dhoni_night": "a traditional Maldivian fishing dhoni on a dark open sea at night near a black jungle-covered deserted island, wooden deck, a small cabin",
    "raniya_office": "Dr. Raniya's office in a two-storey island hospital at night: a desk with files, a closed door, a dark window",
}
MOOD = {
    "sea_launch": "grey overcast morning after dawn, steel-blue sea, low heavy clouds, urgent and uneasy",
    "police_office": "midday under heavy monsoon rain: dim grey daylight from the rain-streaked window, a warm desk lamp, the cold glow of the monitor, tense and focused",
    "male_alley": "midday in a heavy monsoon downpour, dim grey daylight between tall buildings, silver rain streaks, glistening wet concrete, tense",
    "alley_door": "midday in heavy rain, deep shadows in the doorway, grey light, wary and tense",
    "gang_den": "dim dark interior with clear air, a single warm bare bulb over the table against deep navy-black shadows, menacing and tense",
    "male_port": "night, cold navy-blue darkness with warm sodium-orange harbour lamps, light drizzle, secretive",
    "moosa_mansion": "rainy afternoon, grey light through the tall window, warm amber lamps in a dim luxurious room, heavy guilt and grief",
    "car_rain_in": "dusk turning to night in a storm, cold navy-blue darkness, the green-white glow of the dashboard, streaks of light through the wet windscreen, uneasy",
    "car_rain_bridge": "dusk turning to night in heavy rain, cold navy-blue darkness, amber bridge lamps reflecting on the wet road, dangerous and fast",
    "hulhumale_spot": "night, cold navy-blue darkness, one warm orange street light, fine rain, quiet after the danger",
    "safehouse": "night, near-total darkness, the cold blue glow of a laptop on faces, white lightning flashes at the rain-streaked window, secretive and tense",
    "dhoni_night": "a dim memory at night: cold navy-blue darkness, faint moonlight on black water, soft hazy dreamlike edges, fear",
    "raniya_office": "a dim memory at night: one small desk lamp against deep navy shadows, soft hazy dreamlike edges, fear",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
ASH = "Ashham wearing a long black knee-length raincoat open over his dark-navy field shirt"
NOWEAP = "both his hands empty or holding only the plain card"

BEATS = [
    dict(to=3, reason="episode opening: the team races back from Kandu-huttaa to Malé", loc="sea_launch",
         visual="the police fast launch racing away across a grey choppy sea, throwing white spray, its long white wake curving back toward a small dark jungle-covered island on the horizon; two tiny figures visible through the cabin windows; no lettering anywhere on the hull",
         camera="wide aerial three-quarter view, the launch and island in the upper two-thirds, dark grey water as the calm lower third",
         amb="sea_boat"),
    dict(to=5, reason="new information: the forensic report confirms the dead man is Naail (shown only as his photo, alive)",
         loc="police_office",
         visual="an empty office with nobody in it: close view of an open forensic folder lying on the desk with blank pages, a small printed photograph paper-clipped to the page showing a smiling young Maldivian man of about 25 with styled black hair, a thin trimmed beard and a black bomber jacket; behind the folder the window is streaked with heavy rain over Malé's grey rooftops; no person present in the room",
         camera=f"close-up from slightly above, the photo and window in the upper two-thirds, the plain dark desk top as the calm lower third",
         amb="rain_day", sens="other", safe="Naail's death is shown only as a paper-clipped photo of him alive on a blank folder"),
    dict(to=9, reason="scene and time change: noon, heavy rain, Ashham and Habeeb in the alley off Majeedhee Magu",
         chars=["ashham", "habeeb"], loc="male_alley",
         visual=f"{ASH}, standing in the narrow rain-soaked alley, rain running off his shoulders, looking ahead with narrowed eyes; Habeeb in his grey zip jacket, hood up, just behind him at his shoulder, speaking quietly while shielding a dark tablet under his jacket",
         camera=f"medium shot, eye level, {LOW} (puddles on wet concrete)", amb="rain_day", transition="black"),
    dict(to=12, reason="action/character change: two young gang members at the old building's door; Ashham shows his card",
         chars=["ashham"], loc="alley_door",
         visual=f"{ASH}, seen from the side, holding up a plain dark police ID card with no writing toward two wary young Maldivian men in dark long-sleeved hooded tops and jeans standing in the dark doorway of the old building; the young men have stopped mid-step, glancing at each other, their faces tense and pale; their hands are empty and at their sides; long sleeves, nothing in their mouths",
         camera=f"medium wide shot, eye level, {LOW} (wet doorstep and puddles)", amb="rain_day",
         sens="other", safe="the two youths' cigarettes and tattoos are not shown: they wear long sleeves and hold nothing; the ID card is blank"),
    dict(to=15, reason="scene change: inside the gang den, Kalhe at the big table reading papers",
         chars=["kalhe", "ashham"], loc="gang_den",
         visual=f"Kalhe, with a clearly visible long pale scar running across his left cheek, seated at the big table under the single bare bulb, a sheaf of papers in his hands, looking up with a slow knowing smile; in the background, {ASH}, stepping in through a dark doorway, rain glistening on his coat",
         camera=f"medium shot, eye level from Kalhe's side of the table, {LOW} (table top with scattered blank papers)", amb="room_day"),
    dict(to=17, reason="action change: Ashham plants both hands on the table and confronts Kalhe",
         chars=["ashham", "kalhe"], loc="gang_den",
         visual=f"{ASH}, leaning forward over the big table on both flat palms, staring hard at Kalhe; Kalhe leaning back in his chair across the table, arms folded, hands empty, a cool unbothered half-smile; the bare bulb swinging slightly between them",
         camera=f"medium two-shot from the side, eye level, {LOW} (table top)", amb="room_day",
         sens="other", safe="Kalhe lighting a cigarette is not shown: his hands are folded and empty, no smoke"),
    dict(to=20, reason="illustration of Kalhe's account: the shipment taken out of a container at Malé port", loc="male_port",
         visual="at night on the harbour quay, the doors of a plain unmarked steel shipping container stand open; three young men in dark hooded tops, faces in shadow, carry plain brown cardboard boxes with no labels from the container to a waiting dark van; a harbour lamp throws long shadows on the wet concrete",
         camera="wide shot, slightly high angle, the container and men in the upper two-thirds, the wet empty quay as the calm lower third",
         amb="night_exterior", transition="dissolve", sens="other",
         safe="the 'drugs?' question is answered visually by plain unlabelled cardboard boxes of medical supplies; no drugs, no markings"),
    dict(to=23, reason="character/framing change: Habeeb speaks from behind; Kalhe grave — Naail got scared, 'we don't kill people'",
         chars=["kalhe", "ashham", "habeeb"], loc="gang_den",
         visual=f"Kalhe sitting forward at the table, serious now, both open palms raised slightly in denial, his scarred face grave; {ASH}, standing across the table listening; Habeeb in his grey zip jacket and glasses standing back by the doorway, watching tensely",
         camera=f"medium wide shot, eye level, {LOW} (table top)", amb="room_day",
         sens="violence", safe="the merciless killing Kalhe mentions is only spoken; on screen only his grave face"),
    dict(to=26, reason="scene change: back at the office, Habeeb hacks the port and customs records",
         chars=["habeeb", "ashham"], loc="police_office",
         visual=f"Habeeb at the office desk typing fast at the computer, glasses reflecting rows of glowing blurred bars on the monitor with no readable text, empty coffee cups beside him; {ASH}, standing behind his chair leaning in to look; rain on the window",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="office_day"),
    dict(to=29, reason="emotional turning point: the container in Moosa Thaahir's company name, signed by Naail",
         chars=["ashham", "habeeb"], loc="police_office",
         visual=f"close on {ASH}, straightening up with a startled, hard look, eyes fixed on the monitor; the monitor shows a blurred photo of a large plain shipping container with no markings; Habeeb turned in his chair looking up at him",
         camera=f"medium close-up, eye level, {LOW} (dark desk edge)", amb="office_day"),
    dict(to=30, reason="character change: Ashham thinks of Moosa Thaahir, grieving but hiding a secret",
         chars=["moosa"], loc="moosa_mansion",
         visual="Moosa Thaahir standing alone at the tall rain-streaked window of his luxurious living room, half turned toward us, his phone held loosely at his side with its screen dark, his face heavy with grief and hidden guilt, warm lamps glowing behind him",
         camera=f"medium shot, eye level, {LOW} (polished marble floor)", amb="mansion_day"),
    dict(to=34, reason="character change: Habeeb shows Dr. Raniya's photo on the screen",
         chars=["habeeb", "ashham", "raniya"], loc="police_office",
         visual=f"Habeeb turning the computer monitor toward {ASH}; on the monitor a head-and-shoulders portrait photograph of Dr. Raniya in her white doctor's coat and navy hijab, serious expression, no text on the screen; Ashham studying the photo intently; she appears ONLY as the photo on the screen, not in the room",
         camera=f"over-the-shoulder medium shot, the monitor and faces in the upper two-thirds, {LOW} (desk top)", amb="office_day"),
    dict(to=36, reason="scene change: driving to the Hulhumalé warehouse in the rain; a black van follows without lights",
         chars=["ashham", "habeeb"], loc="car_rain_in",
         visual=f"inside the car, {ASH}, driving with both hands on the wheel, eyes flicking to the rear-view mirror where a dark boxy van shape with no lights follows; Habeeb in the passenger seat with his tablet, glancing back over his shoulder; rain streaming down the windscreen",
         camera=f"medium shot from the back seat between them, {LOW} (dark dashboard and seats)", amb="car_night", transition="black"),
    dict(to=38, reason="action change: the chase on Sinamalé bridge, the dark van right on their tail",
         loc="car_rain_bridge",
         visual="a dark saloon car speeding along the wet Sinamalé bridge in heavy rain, spray flying from its wheels, and right behind it, almost touching, a big black van with its headlights off swerving in, its dark shape looming; amber bridge lamps streaking past; nobody visible",
         camera="dramatic low wide angle from behind the van, the two vehicles in the upper two-thirds, the glistening wet road as the calm lower third",
         amb="rain_night", sens="violence", safe="the ramming is shown only as the van looming close behind; no impact, no damage, no people"),
    dict(to=39, reason="action change: Ashham swerves and saves the car",
         chars=["ashham", "habeeb"], loc="car_rain_in",
         visual=f"inside the car, {ASH}, wrenching the steering wheel hard with intense concentration; Habeeb bracing one hand against the dashboard, eyes wide behind his glasses; harsh white glare flaring in the rear-view mirror and through the rain-streaked rear window",
         camera=f"tight medium shot from the passenger side, {LOW} (dark dashboard)", amb="car_night", hum=True),
    dict(to=41, reason="action change: the van stopped askew against the bridge railing as police backup arrives",
         loc="car_rain_bridge",
         visual="behind on the rainy bridge, the black van standing still askew against the steel side railing, intact, its engine steaming slightly in the rain; a police car with flashing blue lights pulling up beside it; far in the foreground the red tail lights of the saloon car driving away toward Hulhumalé; no people visible",
         camera="wide shot looking back along the bridge, slightly high angle, the vehicles in the upper two-thirds, the wet road as the calm lower third",
         amb="rain_night", sens="violence", safe="the crash is shown only as the van stopped against the railing afterwards; no damage to people, nobody shown"),
    dict(to=42, reason="back to the two inside the car: 'they have people inside the police'", reuse="beat_013",
         chars=["ashham", "habeeb"], loc="car_rain_in", visual="(reuse of beat_013)", amb="car_night"),
    dict(to=47, reason="scene change: the car stops at a lonely spot in Hulhumalé; Habeeb trembling but determined",
         chars=["habeeb", "ashham"], loc="hulhumale_spot",
         visual=f"beside the parked car under the single street light by the sea wall, Habeeb in his grey zip jacket standing with arms wrapped around himself, shaking, but his jaw set with resolve behind his rain-speckled glasses; {ASH}, facing him at arm's length, studying him with quiet respect",
         camera=f"medium two-shot, eye level, {LOW} (wet empty road)", amb="rain_night"),
    dict(to=48, reason="action change: Ashham texts Moosa Thaahir from his phone",
         chars=["ashham"], loc="hulhumale_spot",
         visual=f"close on {ASH}, his face lit from below by the soft glow of the phone in his hand, thumb on the screen, rain drops on the glass, eyes cold and determined; the phone screen shows only a blank glow",
         camera=f"close-up, eye level, his face in the upper two-thirds, {LOW} (dark coat and shadow)", amb="rain_night"),
    dict(to=50, reason="back to Moosa: no reply comes", reuse="beat_011", chars=["moosa"], loc="moosa_mansion",
         visual="(reuse of beat_011)", amb="mansion_day"),
    dict(to=53, reason="scene and time change: the secret safe house in Hulhumalé's second phase at night, storm outside",
         chars=["habeeb", "ashham"], loc="safehouse",
         visual=f"a dark bare room: Habeeb sitting at the plain table with his face lit cold blue by his open laptop; {ASH}, his raincoat dripping, standing by the window as a white flash of lightning outlines him; everything else in deep darkness",
         camera=f"wide shot, eye level, {LOW} (dark floor)", amb="rain_night", transition="black"),
    dict(to=56, reason="action change: Habeeb reveals the encrypted recording; Ashham hangs his wet coat on a chair",
         chars=["ashham", "habeeb"], loc="safehouse",
         visual="Ashham in his dark-navy field shirt hanging his wet long black raincoat over the back of a chair, looking toward Habeeb; Habeeb at the laptop, hands on the keyboard, looking up at him; the cold blue laptop glow on both faces, rain on the dark window",
         camera=f"medium shot, eye level, {LOW} (table top in shadow)", amb="room_night"),
    dict(to=59, reason="memory: the recorded satellite-phone call — Naail alive on a dhoni at night near Kandu-huttaa",
         chars=["naail"], loc="dhoni_night",
         visual="Naail crouching at the side of a dark dhoni deck at night, a chunky satellite phone pressed to his ear, his face frightened and pale in the faint moonlight, glancing back toward the black jungle island; waves slapping the hull",
         camera=f"medium shot, slightly low angle, {LOW} (dark wooden deck)", amb="sea_boat", transition="dissolve", hum=True),
    dict(to=63, reason="memory: Raniya's frightened voice on the call — she is forced because her father is a hostage",
         chars=["raniya"], loc="raniya_office",
         visual="Dr. Raniya in her white doctor's coat over her dusty-blue dress and navy hijab fully covering her hair and neck, standing in the dim office, a phone pressed to her ear, her other hand clasped at her chest, eyes wide with fear and tears, glancing toward the closed door",
         camera=f"medium close-up, eye level, {LOW} (desk top in shadow)", amb="memory", transition="dissolve", hum=True),
    dict(to=65, reason="memory, turning point: a door bursts open on the dhoni and the call cuts off (shown only symbolically)",
         loc="dhoni_night",
         visual="the dark empty dhoni deck at night: a satellite phone lying abandoned on the wet wooden planks, its small screen still glowing; a harsh beam of white flashlight light spilling across the deck from a cabin doorway that has just been flung open; nobody visible",
         camera="low close angle along the deck, the phone and the light beam in the upper two-thirds, the dark planks as the calm lower third",
         amb="sea_boat", transition="dissolve", hum=True, sens="violence",
         safe="the intruders, the gunshot and Naail's capture are never shown; only the abandoned phone and a flashlight beam; sound is a soft thud only"),
    dict(to=68, reason="back to the present: silence in the safe house; Ashham works out Raniya's situation",
         chars=["ashham", "habeeb"], loc="safehouse",
         visual="Ashham sitting at the table with his eyes closed, jaw clenched, deep in thought, his fist resting against his lips; Habeeb beside him staring at the laptop in shock; the cold blue glow on their faces, rain on the dark window",
         camera=f"medium close two-shot, eye level, {LOW} (table top)", amb="room_night", transition="dissolve", hum=True,
         sens="violence", safe="what was done to Naail is only spoken; on screen only the two men's grave faces"),
    dict(to=72, reason="action change: Ashham stands up decisively — they leave for the atoll secretly tonight",
         chars=["ashham", "habeeb"], loc="safehouse",
         visual="Ashham standing up from the table, pulling his long black raincoat back on, his face set with determination, looking toward the door; Habeeb snapping his laptop shut and slipping it into a black backpack, getting up to follow",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="room_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With the frightening evidence found on Kandu-huttaa, Ashham's team was forced to return to Malé at once.")
sh(2, "Once it was certain that the sound of the launch heard from that deserted island belonged to people keeping watch on the police, the investigation's plans had to change.",
   [("boat_engine", "ލޯންޗުގެ", -22)])
sh(3, "There were still many things to find before entering the secret bunker. The police are secretly monitoring the Kandu-huttaa area.")
sh(4, "The forensic report confirmed that the dead man found was Naail, son of Moosa Thaahir, one of Malé's most influential tycoons.")
sh(5, "Unease had settled over all of Malé's political and business circles. It is twelve noon. Heavy rain is pouring over Malé.",
   [("rain_start", "ވާރޭ", -20)])
sh(6, "Ashham is wearing a black raincoat. It is a narrow alley joined to Majeedhee Magu. Habeeb stands behind him. \"Sir,")
sh(7, "large sums of money have recently been taken out of Naail's bank accounts. The money went to the people of the Maafannu 'Black Wolf' gang,\" Habeeb said quietly.")
sh(8, "\"What did he give them money for? Blackmail? Or drugs?\" Ashham asked. \"I think it's the second reason.")
sh(9, "But that gang's leader, 'Kalhe', is not someone who will talk easily,\" Habeeb said. After nodding, Ashham")
sh(10, "went into a dark alley. At the door of an old building there, two young men were standing smoking. They had various tattoos on their bodies.",
   [("footsteps_pavement", "ވަނެވެ", -22)])
sh(11, "As soon as they saw Ashham they slowly began to walk away. Ashham took out his card and showed it. \"Wait. I've come to meet Kalhe.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(12, "About Naail's death.\" At Naail's name, the colour drained from the two young men's faces. After glancing at each other,")
sh(13, "they showed him the way inside. In the gang's den: inside the building it is dark. It is a lair of criminals.",
   [("door_open", "ވަނުމަށް", -22)])
sh(14, "Through two or three doors, in the middle of the room where they stopped, at a big table sat Kalhe, about forty years old. There was a big scar on his face.",
   [("creak", "ދޮރަކުން", -22)])
sh(15, "He sat looking through some papers. \"Ashham... the famous investigator,\" Kalhe said with a smile. \"Why have you come to me?\" \"Kalhe,",
   [("paper_shuffle", "ކަރުދާސްތަކެއް", -22)])
sh(16, "you know Naail was found murdered. Before he died he gave you large sums of money,\" Ashham said, planting his hands on the table.",
   [("soft_thud", "އަތްވިއްދާލަމުން", -20)])
sh(17, "\"What money would that be?\" Kalhe lit a cigarette. \"Naail is a tycoon's son. He wanted protection for a secret shipment coming from abroad.")
sh(18, "He gave us money to get those goods out of Malé port.\" \"What goods? Drugs?\" Ashham asked in a mocking tone. \"No!\"")
sh(19, "Kalhe shook his head. \"It isn't drugs. It's medical supplies. But the label on the outside says something else.")
sh(20, "As Naail told it, those goods had to go to GA. Kandu-huttaa. All we did was take the goods out of the container at Malé port.\"",
   [("metal_door", "ކޮންޓޭނަރުން", -22)])
sh(21, "\"So Naail was part of that secret laboratory,\" Habeeb said quietly from behind. \"Yes, but later Naail got scared.")
sh(22, "He said what they were doing was against humanity. He wanted to stop it. Two days later he disappeared,\" Kalhe explained.")
sh(23, "\"Ashham, we don't kill people. Especially not in such a merciless way. That is the work of a far more powerful group.\" The hidden file:",
   hum=True)
sh(24, "With the information Kalhe gave, Ashham realised that the root of Naail's death was an illegal medicine trade running in Malé's black market.")
sh(25, "They came back to the office. Habeeb was hacking the records of Malé commercial harbour and customs. \"Sir!",
   [("keyboard_typing", "ހެކްކުރަމުންނެވެ", -20)])
sh(26, "Found it,\" Habeeb exclaimed. \"Three weeks ago a big container was imported in the name of Moosa Thaahir's company.",
   [("computer_beep", "ފެނިއްޖެ", -22)])
sh(27, "It says it contained medical equipment.\" \"In the name of Moosa's company?\" Ashham was startled. \"So Naail's father knows about this?\"",
   [("gasp", "ސިއްސައިގެން", -22)])
sh(28, "\"No, sir. The one who signed these documents is Naail, using Moosa's name,\" Habeeb explained in detail.")
sh(29, "\"And after these goods were unloaded at Malé port, they were taken to an area of Hulhumalé.\" Ashham thought it over.")
sh(30, "When Moosa Thaahir met him, he truly was grief-stricken. Yet he is hiding some secret. \"Habeeb,", hum=True)
sh(31, "among Naail's calls there were calls to that atoll hospital's number, weren't there? Have you found that person?\" Ashham asked. \"Yes,")
sh(32, "it's Doctor Raniya. She is that hospital's chief surgeon. Before Naail died, she was the one he talked to most,\" Habeeb said, showing Raniya's photo on the screen.")
sh(33, "Raniya is a fair, beautiful woman of about twenty-eight. She is serious by nature. A well-known doctor.")
sh(34, "\"All these waves are breaking toward that atoll,\" Ashham said. \"People in Malé are planning this. But in practice it is run inside that atoll.\"")
sh(35, "The danger of being watched: Ashham and Habeeb left the office and got into the car to go to that warehouse in Hulhumalé. It was still raining heavily.",
   [("car_door", "އެރިއެވެ", -20)])
sh(36, "As the car drove on, Ashham noticed a black van coming behind them. The van was coming without any light.",
   [("car_approach", "ވޭނެއް", -22), ("heartbeat", "ނެތިއެވެ", -22)])
sh(37, "Its lights were switched off. \"Habeeb, hold on,\" Ashham sped the car up. The van behind sped up too.",
   [("engine_rev", "ބާރުކޮށްލިއެވެ", -18), ("engine_rev", "ބާރުކުރިއެވެ", -20)])
sh(38, "As they reached Sinamalé bridge, the van came straight at them and struck the car. \"Sir!\" Habeeb shouted.",
   [("crash_clatter", "ޖެއްސިއެވެ", -18), ("gasp", "ހަޅޭއްލަވައިގަތެވެ", -20)], hum=True)
sh(39, "Ashham skilfully turned the car. It was only his alertness that saved the car from overturning.",
   [("brake_screech", "އަނބުރާލިއެވެ", -18)])
sh(40, "At that moment Habeeb had already signalled the station for backup. The van lost control and hit the steel railing at the edge of the bridge.",
   [("computer_beep", "ސިގްނަލް", -22), ("crash_clatter", "ޖެހުނެވެ", -20)])
sh(41, "Without stopping, Ashham drove on to Hulhumalé. Just then a police backup vehicle was reaching the crashed van.",
   [("car_pass", "ދުއްވާލިއެވެ", -20), ("siren", "ވެހިކަލް", -22)])
sh(42, "\"They want to stop us. They have their people inside Malé's police too. They know our every move.\"")
sh(43, "Ashham said. A dangerous decision: after stopping the car at a lonely spot in Hulhumalé, Ashham looked at Habeeb.")
sh(44, "Habeeb was trembling with fear. \"Habeeb, are you scared?\" Ashham asked. \"Yes, sir.",
   [("breath_heavy", "ތުރުތުރު", -22)])
sh(45, "When it comes to that point, of course one gets scared. But I don't want to give up. I will find the truth about Naail's death.")
sh(46, "We must get justice,\" Habeeb said with courage. \"Good. Staying in Malé, there's no safety for us.")
sh(47, "Tonight we should go to GA, to meet Dr. Raniya,\" Ashham decided. \"The link between that bunker and that hospital can only be found over there.\"")
sh(48, "Ashham sent Moosa Thaahir a message from his phone: \"Naail's secrets begin with your company. Reveal the truth.\"",
   [("phone_buzz", "މެސެޖެއް", -22)])
sh(49, "But no reply came from Moosa. Gathering evidence from Malé's secret places, Ashham realised this was not just the work of criminals inside the Maldives.")
sh(50, "Behind it was also the hand of a large international network. The secret room in Hulhumalé:", hum=True)
sh(51, "After the danger they met on the way onto the bridge, Ashham and Habeeb headed for a secret police safe house in Hulhumalé's second phase.")
sh(52, "It was not a place anyone would know. Outside heavy rain was falling, and loud thunder rumbled across the whole area.",
   [("thunder", "ގުގުރީގެ", -16)])
sh(53, "The only light inside the room was the blue light coming from Habeeb's laptop screen.")
sh(54, "\"Sir, they are monitoring all our official communication channels,\" Habeeb said, running his hands over the keyboard.",
   [("keyboard_typing", "ކީބޯޑުގައި", -20)])
sh(55, "\"But inside Naail's iCloud backup I found an encrypted secret audio file.")
sh(56, "This is the recording of a satellite-phone call made twenty-four hours before he died.\" \"Play it, quickly,\" Ashham said, hanging his wet coat on the arm of a chair.",
   [("cloth_rustle", "އަޅުވަމުން", -20)])
sh(57, "As Zayaan clicked, the sound of sea waves and a phone call began to play. \"Naail! Where are you?\" It was a woman's young",
   [("computer_beep", "ކްލިކްކޮށްލުމާއެކު", -22), ("wave_crash", "ރާޅުތަކުގެ", -20)])
sh(58, "but frightened voice. \"I'm on a dhoni not far from Kandu-huttaa. Raniya, I didn't believe what you told me before.")
sh(59, "But tonight I went in and looked. What kind of horrifying thing are they doing inside that bunker?\"", hum=True)
sh(60, "Naail's voice was trembling. \"Naail, get out of there right now! If they find out you went in, they won't let you live.",
   [("breath_heavy", "ތުރުތުރު", -22)])
sh(61, "It isn't just a place for testing medicine. There they are... using human beings...\"", hum=True)
sh(62, "Raniya's words broke off. \"Using human beings for what?\" Naail shouted. \"My father...")
sh(63, "they are holding my father hostage. I'm only doing this because I'm forced to. Naail,", hum=True)
sh(64, "do you know who is behind this among Malé's powerful men? It's...\" At that moment, through the call, came the loud sound of a door bursting open,",
   [("door_slam", "ހުޅުވުނު", -16)], hum=True)
sh(65, "and the sound of a gunshot. With Naail's cry the call cut off. The doctor's secret: silence fell over the room once again.",
   [("soft_thud", "ބަޑިއެއްގެ", -22), ("gasp", "ހަޅޭކުގެ", -22)], hum=True)
sh(66, "Ashham closed his eyes and thought hard. \"Dr. Raniya,\" Ashham said slowly. \"She is the senior surgeon of that atoll hospital. By holding her father hostage",
   [("sigh", "ތަގުޅިކޮށްލިއެވެ", -22)])
sh(67, "they force her to help with the terrifying experiments run on that deserted island.\" \"Sir, testing drugs on human beings is an international crime.")
sh(68, "This is a huge crime,\" Habeeb said. \"When Naail found out, they cut out his tongue and killed him to keep that secret.\"", hum=True)
sh(69, "\"We have to go to that atoll right now. To meet Raniya,\" Ashham said, standing up.",
   [("cloth_rustle", "ތެދުވިއެވެ", -20)])
sh(70, "\"She will have the secret information and evidence for getting into the Kandu-huttaa bunker.\" \"But sir, if we go officially, they'll know.")
sh(71, "Even at Malé headquarters someone is working to cover up this case,\" Habeeb reminded him. \"We'll go on an ordinary sea boat.")
sh(72, "Secretly,\" Ashham said. \"Habeeb, take your gear and come. There's no time.\" - To be continued -",
   [("footsteps_pavement", "ހިނގާ", -22)])
SHOTS = S

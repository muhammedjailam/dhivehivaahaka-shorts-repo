"""Beat/shot plan for Project Phenix episode 318 — v2 re-cut on the new (slower, colloquial) audio (used by plan_beats.py).
v1 images are reused with v1="beat_###" (the old image file); NEW beats are mainly shot / reverse-shot images for spec 5.4
(the speaker centred and sharp). The v1 port illustration (old beat_007) is dropped: all of it plays under Kalhe's lines."""

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
    # 001 ---------------------------------------------------------------- launch back to Malé
    dict(to=3, v1="beat_001", reason="episode opening: the team races back from Kandu-huttaa to Malé", loc="sea_launch",
         visual="the police fast launch racing away across a grey choppy sea, throwing white spray, its long white wake curving back toward a small dark jungle-covered island on the horizon; two tiny figures visible through the cabin windows; no lettering anywhere on the hull",
         camera="wide aerial three-quarter view, the launch and island in the upper two-thirds, dark grey water as the calm lower third",
         amb="sea_boat"),
    # 002 ---------------------------------------------------------------- forensic report
    dict(to=5, v1="beat_002", reason="new information: the forensic report confirms the dead man is Naail (shown only as his photo, alive)",
         loc="police_office",
         visual="an empty office with nobody in it: close view of an open forensic folder lying on the desk with blank pages, a small printed photograph paper-clipped to the page showing a smiling young Maldivian man of about 25 with styled black hair, a thin trimmed beard and a black bomber jacket; behind the folder the window is streaked with heavy rain over Malé's grey rooftops; no person present in the room",
         camera="close-up from slightly above, the photo and window in the upper two-thirds, the plain dark desk top as the calm lower third",
         amb="rain_day", sens="other", safe="Naail's death is shown only as a paper-clipped photo of him alive on a blank folder"),
    # 003 ---------------------------------------------------------------- the alley: Habeeb / Ashham (both centrable by crop)
    dict(to=10, v1="beat_003", reason="scene and time change: noon, heavy rain, Ashham and Habeeb in the alley off Majeedhee Magu",
         chars=["ashham", "habeeb"], loc="male_alley",
         visual=f"{ASH}, standing in the narrow rain-soaked alley, rain running off his shoulders, looking ahead with narrowed eyes; Habeeb in his grey zip jacket, hood up, just behind him at his shoulder, speaking quietly while shielding a dark tablet under his jacket",
         camera=f"medium shot, eye level, {LOW} (puddles on wet concrete)", amb="rain_day", transition="black"),
    # 004 ---------------------------------------------------------------- youths at the door (narration)
    dict(to=11, v1="beat_004", reason="action/character change: two young gang members at the old building's door; Ashham shows his card",
         chars=["ashham"], loc="alley_door",
         visual=f"{ASH}, seen from the side, holding up a plain dark police ID card with no writing toward two wary young Maldivian men in dark long-sleeved hooded tops and jeans standing in the dark doorway of the old building; the young men have stopped mid-step, glancing at each other, their faces tense and pale; their hands are empty and at their sides; long sleeves, nothing in their mouths",
         camera=f"medium wide shot, eye level, {LOW} (wet doorstep and puddles)", amb="rain_day",
         sens="other", safe="the two youths' cigarettes and tattoos are not shown: they wear long sleeves and hold nothing; the ID card is blank"),
    # 005 NEW ------------------------------------------------------------ 5.4: Ashham speaks to the youths
    dict(to=13, reason="5.4 dialogue: Ashham speaks ('Wait. I've come to meet Kalhe') — in the v1 image he is in profile at the left edge",
         chars=["ashham"], speaker="ashham", loc="alley_door",
         visual=f"{ASH}, standing at the wet doorstep of the old building, turned three-quarters toward the camera and centred in the frame, holding up a plain dark police ID card with no writing at chest height in one hand, speaking firmly with a cool hard stare; at the left and right edges of the soft blurred foreground, the backs and hooded heads of two young men in dark long-sleeved hooded tops, out of focus; rain falling in the grey light",
         camera=f"medium close-up over the young men's shoulders, Ashham centred and sharp in the upper half, {LOW} (wet doorstep)",
         amb="rain_day", transition="cut",
         sens="other", safe="the youths are seen only from behind in long sleeves (no cigarettes, no tattoos); the ID card is blank"),
    # 006 ---------------------------------------------------------------- inside the den: Kalhe at the table
    dict(to=17, v1="beat_005", reason="scene change: inside the gang den, Kalhe at the big table reading papers",
         chars=["kalhe", "ashham"], loc="gang_den",
         visual=f"Kalhe, with a clearly visible long pale scar running across his left cheek, seated at the big table under the single bare bulb, a sheaf of papers in his hands, looking up with a slow knowing smile; in the background, {ASH}, stepping in through a dark doorway, rain glistening on his coat",
         camera=f"medium shot, eye level from Kalhe's side of the table, {LOW} (table top with scattered blank papers)", amb="room_day"),
    # 007 ---------------------------------------------------------------- Ashham plants his hands on the table
    dict(to=18, v1="beat_006", reason="action change: Ashham plants both hands on the table and confronts Kalhe",
         chars=["ashham", "kalhe"], loc="gang_den",
         visual=f"{ASH}, leaning forward over the big table on both flat palms, staring hard at Kalhe; Kalhe leaning back in his chair across the table, arms folded, hands empty, a cool unbothered half-smile; the bare bulb swinging slightly between them",
         camera=f"medium two-shot from the side, eye level, {LOW} (table top)", amb="room_day", transition="cut",
         sens="other", safe="Kalhe lighting a cigarette is not shown: his hands are folded and empty, no smoke"),
    # 008 NEW ------------------------------------------------------------ 5.4: Kalhe's reverse shot
    dict(to=23, reason="5.4 dialogue: Kalhe explains the secret shipment — his reverse shot (in the v1 two-shot he is in profile at the right edge)",
         chars=["kalhe"], speaker="kalhe", loc="gang_den",
         visual="Kalhe, with a clearly visible long pale scar across his left cheek, seated at the big scarred table under the single bare bulb, leaning forward on his forearms, speaking earnestly and gravely, one open empty palm raised, his face centred and sharp in the upper half; at the right edge of the frame the blurred dark shoulder and back of a tall man in a long black raincoat standing across the table, out of focus; scattered blank papers on the table",
         camera=f"medium close-up over the shoulder of the man in the raincoat, Kalhe centred in the upper half, {LOW} (table top with blank papers)",
         amb="room_day", transition="cut",
         sens="other", safe="Kalhe's cigarette is not shown: empty hands, no smoke; the shipment is only spoken about"),
    # 009 NEW ------------------------------------------------------------ 5.4: Habeeb speaks from the doorway
    dict(to=24, reason="5.4 dialogue: Habeeb speaks quietly from behind ('So Naail was part of that secret lab') — tiny in the v1 three-shot",
         chars=["habeeb"], speaker="habeeb", loc="gang_den",
         visual="Habeeb in his grey zip jacket and glasses standing just inside the dark doorway at the back of the room, speaking quietly with a tense, thoughtful look, his face centred and sharp in the upper half, lit by the warm bare bulb; in the blurred foreground at the lower left, the out-of-focus shaved head and broad shoulder of a man in a black henley seated at the table, seen from behind",
         camera=f"medium close-up across the table, Habeeb centred in the upper half, {LOW} (table edge in shadow)",
         amb="room_day", transition="cut"),
    # 010 ---------------------------------------------------------------- back to Kalhe: Naail got scared, 'we don't kill people'
    dict(to=27, reuse="beat_008", reason="5.4 reverse shot: Kalhe answers — Naail got scared; 'we don't kill people'",
         chars=["kalhe"], speaker="kalhe", loc="gang_den", visual="(reuse of beat_008)", amb="room_day", transition="cut",
         sens="violence", safe="the merciless killing Kalhe mentions is only spoken; on screen only his grave face"),
    # 011 ---------------------------------------------------------------- the three in the den: Ashham realises
    dict(to=28, v1="beat_008", reason="framing change: the three in the den as Ashham grasps the black-market medicine trade (narration)",
         chars=["kalhe", "ashham", "habeeb"], loc="gang_den",
         visual=f"Kalhe sitting forward at the table, serious now, both open palms raised slightly in denial, his scarred face grave; {ASH}, standing across the table listening; Habeeb in his grey zip jacket and glasses standing back by the doorway, watching tensely",
         camera=f"medium wide shot, eye level, {LOW} (table top)", amb="room_day"),
    # 012 ---------------------------------------------------------------- office: Habeeb hacks the records
    dict(to=30, v1="beat_009", reason="scene change: back at the office, Habeeb hacks the port and customs records",
         chars=["habeeb", "ashham"], loc="police_office",
         visual=f"Habeeb at the office desk typing fast at the computer, glasses reflecting rows of glowing blurred bars on the monitor with no readable text, empty coffee cups beside him; {ASH}, standing behind his chair leaning in to look; rain on the window",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="office_day"),
    # 013 ---------------------------------------------------------------- Ashham startled
    dict(to=31, v1="beat_010", reason="emotional turning point: the container in Moosa Thaahir's company name — Ashham startled",
         chars=["ashham", "habeeb"], loc="police_office",
         visual=f"close on {ASH}, straightening up with a startled, hard look, eyes fixed on the monitor; the monitor shows a blurred photo of a large plain shipping container with no markings; Habeeb turned in his chair looking up at him",
         camera=f"medium close-up, eye level, {LOW} (dark desk edge)", amb="office_day", transition="cut"),
    # 014 ---------------------------------------------------------------- Habeeb explains (reverse shot)
    dict(to=33, reuse="beat_012", reason="5.4 reverse shot: Habeeb explains Naail signed with Moosa's name",
         chars=["habeeb", "ashham"], loc="police_office", visual="(reuse of beat_012)", amb="office_day", transition="cut"),
    # 015 ---------------------------------------------------------------- Moosa
    dict(to=34, v1="beat_011", reason="character change: Ashham thinks of Moosa Thaahir, grieving but hiding a secret",
         chars=["moosa"], loc="moosa_mansion",
         visual="Moosa Thaahir standing alone at the tall rain-streaked window of his luxurious living room, half turned toward us, his phone held loosely at his side with its screen dark, his face heavy with grief and hidden guilt, warm lamps glowing behind him",
         camera=f"medium shot, eye level, {LOW} (polished marble floor)", amb="mansion_day"),
    # 016 ---------------------------------------------------------------- Raniya's photo; Ashham asks
    dict(to=35, v1="beat_012", reason="character change: Habeeb shows Dr. Raniya's photo on the screen; Ashham asks about the hospital calls",
         chars=["habeeb", "ashham", "raniya"], loc="police_office",
         visual=f"Habeeb turning the computer monitor toward {ASH}; on the monitor a head-and-shoulders portrait photograph of Dr. Raniya in her white doctor's coat and navy hijab, serious expression, no text on the screen; Ashham studying the photo intently; she appears ONLY as the photo on the screen, not in the room",
         camera=f"over-the-shoulder medium shot, the monitor and faces in the upper two-thirds, {LOW} (desk top)", amb="office_day"),
    # 017 ---------------------------------------------------------------- Habeeb answers (reverse shot)
    dict(to=36, reuse="beat_012", reason="5.4 reverse shot: Habeeb answers — it's Dr. Raniya",
         chars=["habeeb", "ashham"], loc="police_office", visual="(reuse of beat_012)", amb="office_day", transition="cut"),
    # 018 ---------------------------------------------------------------- the photo; Ashham: 'all waves break toward that atoll'
    dict(to=39, reuse="beat_016", reason="back to the photo and Ashham's conclusion",
         chars=["habeeb", "ashham", "raniya"], loc="police_office", visual="(reuse of beat_016)", amb="office_day", transition="cut"),
    # 019 ---------------------------------------------------------------- the car; black van behind
    dict(to=41, v1="beat_013", reason="scene change: driving to the Hulhumalé warehouse in the rain; a black van follows without lights",
         chars=["ashham", "habeeb"], loc="car_rain_in",
         visual=f"inside the car, {ASH}, driving with both hands on the wheel, eyes flicking to the rear-view mirror where a dark boxy van shape with no lights follows; Habeeb in the passenger seat with his tablet, glancing back over his shoulder; rain streaming down the windscreen",
         camera=f"medium shot from the back seat between them, {LOW} (dark dashboard and seats)", amb="car_night", transition="black"),
    # 020 ---------------------------------------------------------------- 'Habeeb, hold on' — Ashham speeds up
    dict(to=42, v1="beat_015", reason="action change + 5.4: Ashham ('Habeeb, hold on') speeds up — his face is centrable in this image",
         chars=["ashham", "habeeb"], loc="car_rain_in",
         visual=f"inside the car, {ASH}, wrenching the steering wheel hard with intense concentration; Habeeb bracing one hand against the dashboard, eyes wide behind his glasses; harsh white glare flaring in the rear-view mirror and through the rain-streaked rear window",
         camera=f"tight medium shot from the passenger side, {LOW} (dark dashboard)", amb="car_night"),
    # 021 ---------------------------------------------------------------- the van rams them on the bridge
    dict(to=43, v1="beat_014", reason="action change: the chase on Sinamalé bridge, the dark van right on their tail",
         loc="car_rain_bridge",
         visual="a dark saloon car speeding along the wet Sinamalé bridge in heavy rain, spray flying from its wheels, and right behind it, almost touching, a big black van with its headlights off swerving in, its dark shape looming; amber bridge lamps streaking past; nobody visible",
         camera="dramatic low wide angle from behind the van, the two vehicles in the upper two-thirds, the glistening wet road as the calm lower third",
         amb="rain_night", sens="violence", safe="the ramming is shown only as the van looming close behind; no impact, no damage, no people"),
    # 022 ---------------------------------------------------------------- Ashham swerves
    dict(to=44, reuse="beat_020", reason="action change: Ashham swerves and saves the car",
         chars=["ashham", "habeeb"], loc="car_rain_in", visual="(reuse of beat_020)", amb="car_night"),
    # 023 ---------------------------------------------------------------- the van against the railing
    dict(to=45, v1="beat_016", reason="action change: the van stopped askew against the bridge railing as police backup arrives",
         loc="car_rain_bridge",
         visual="behind on the rainy bridge, the black van standing still askew against the steel side railing, intact, its engine steaming slightly in the rain; a police car with flashing blue lights pulling up beside it; far in the foreground the red tail lights of the saloon car driving away toward Hulhumalé; no people visible",
         camera="wide shot looking back along the bridge, slightly high angle, the vehicles in the upper two-thirds, the wet road as the calm lower third",
         amb="rain_night", sens="violence", safe="the crash is shown only as the van stopped against the railing afterwards; no damage to people, nobody shown"),
    # 024 ---------------------------------------------------------------- 'they have people inside the police'
    dict(to=47, reuse="beat_020", reason="5.4: back inside the car, Ashham speaks — 'they have people inside the police'",
         chars=["ashham", "habeeb"], loc="car_rain_in", visual="(reuse of beat_020)", amb="car_night"),
    # 025 ---------------------------------------------------------------- lonely Hulhumalé spot (two-shot, narration)
    dict(to=48, v1="beat_018", reason="scene change: the car stops at a lonely spot in Hulhumalé; Habeeb trembling",
         chars=["habeeb", "ashham"], loc="hulhumale_spot",
         visual=f"beside the parked car under the single street light by the sea wall, Habeeb in his grey zip jacket standing with arms wrapped around himself, shaking, but his jaw set with resolve behind his rain-speckled glasses; {ASH}, facing him at arm's length, studying him with quiet respect",
         camera=f"medium two-shot, eye level, {LOW} (wet empty road)", amb="rain_night"),
    # 026 NEW ------------------------------------------------------------ 5.4: Ashham asks 'are you scared?'
    dict(to=49, reason="5.4 dialogue: Ashham asks Habeeb if he is scared — in the v1 two-shot both faces sit at the edges",
         chars=["ashham"], speaker="ashham", loc="hulhumale_spot",
         visual=f"{ASH}, standing by the parked car under the single street light by the sea wall at night, facing the camera three-quarters, centred, speaking with quiet concern and a firm steady gaze, fine rain glittering in the orange light around him; at the left edge, the blurred out-of-focus shoulder and dark curly hair of a young man in a grey zip jacket seen from behind",
         camera=f"medium close-up over the young man's shoulder, Ashham centred and sharp in the upper half, {LOW} (dark wet road)",
         amb="rain_night", transition="cut"),
    # 027 NEW ------------------------------------------------------------ 5.4: Habeeb answers — scared but won't give up
    dict(to=50, reason="5.4 dialogue: Habeeb answers — scared, but he won't give up (reverse shot)",
         chars=["habeeb"], speaker="habeeb", loc="hulhumale_spot",
         visual="Habeeb in his grey zip jacket over a white T-shirt, rain-speckled glasses, standing by the sea wall under the street light at night, arms wrapped tightly around himself, trembling, but speaking with his jaw set in resolve; Habeeb stands exactly in the middle of the picture, his face at the horizontal centre of the frame and sharp in the upper half; only a thin dark blurred sliver of another man's black raincoat shoulder at the very right edge of the picture; the dark lagoon and distant city lights behind him",
         camera=f"medium close-up, frontal, Habeeb exactly centred left-to-right, his face in the upper half, {LOW} (dark wet road)",
         amb="rain_night", transition="cut"),
    # 028 ---------------------------------------------------------------- Ashham decides: GA tonight
    dict(to=52, reuse="beat_026", reason="5.4 reverse shot: Ashham decides they go to GA tonight to meet Dr. Raniya",
         chars=["ashham"], speaker="ashham", loc="hulhumale_spot", visual="(reuse of beat_026)", amb="rain_night", transition="cut"),
    # 029 ---------------------------------------------------------------- message to Moosa
    dict(to=53, v1="beat_019", reason="action change: Ashham texts Moosa Thaahir from his phone",
         chars=["ashham"], loc="hulhumale_spot",
         visual=f"close on {ASH}, his face lit from below by the soft glow of the phone in his hand, thumb on the screen, rain drops on the glass, eyes cold and determined; the phone screen shows only a blank glow",
         camera=f"close-up, eye level, his face in the upper two-thirds, {LOW} (dark coat and shadow)", amb="rain_night"),
    # 030 ---------------------------------------------------------------- Moosa: no reply
    dict(to=55, reuse="beat_015", reason="back to Moosa: no reply comes", chars=["moosa"], loc="moosa_mansion",
         visual="(reuse of beat_015)", amb="mansion_day"),
    # 031 ---------------------------------------------------------------- safe house
    dict(to=57, v1="beat_021", reason="scene and time change: the secret safe house in Hulhumalé's second phase at night, storm outside",
         chars=["habeeb", "ashham"], loc="safehouse",
         visual=f"a dark bare room: Habeeb sitting at the plain table with his face lit cold blue by his open laptop; {ASH}, his raincoat dripping, standing by the window as a white flash of lightning outlines him; everything else in deep darkness",
         camera=f"wide shot, eye level, {LOW} (dark floor)", amb="rain_night", transition="black"),
    # 032 NEW ------------------------------------------------------------ 5.4: Habeeb at the laptop
    dict(to=60, reason="5.4 dialogue: Habeeb at the laptop explains the monitoring and the encrypted recording — at the edge in both v1 safe-house images",
         chars=["habeeb"], speaker="habeeb", loc="safehouse",
         visual="Habeeb in his grey zip jacket and glasses sitting at the plain table, his face lit cold blue by the open laptop in front of him, hands on the keyboard, looking up from the screen and speaking urgently, his face centred and sharp in the upper half; at the left edge, the soft out-of-focus dark silhouette of a tall man in a long black raincoat standing; rain and a white lightning flash on the dark window behind",
         camera=f"medium close-up from across the table, Habeeb centred in the upper half, only the back of the laptop lid low in frame, {LOW} (dark table top)",
         amb="room_night"),
    # 033 NEW ------------------------------------------------------------ 5.4: Ashham 'play it' hanging his coat
    dict(to=61, reason="5.4 dialogue: Ashham says 'play it, quickly' while hanging his wet coat on a chair (reverse shot)",
         chars=["ashham"], speaker="ashham", loc="safehouse",
         visual="Ashham in his dark-navy long-sleeved field shirt, standing beside a chair, hanging his wet long black raincoat over the back of the chair with one hand, turned three-quarters toward the camera and speaking firmly and urgently, his face centred and sharp in the upper half, lit by cold blue laptop glow; at the right edge, the blurred out-of-focus shoulder of a young man with glasses seated at a laptop; rain on the dark window behind",
         camera=f"medium close-up, Ashham centred in the upper half, {LOW} (dark floor and chair)",
         amb="room_night", transition="cut"),
    # 034 ---------------------------------------------------------------- memory: Raniya's voice
    dict(to=62, v1="beat_024", reason="memory: the recorded satellite-phone call — Raniya's frightened voice ('Naail! Where are you?')",
         chars=["raniya"], loc="raniya_office",
         visual="Dr. Raniya in her white doctor's coat over her dusty-blue dress and navy hijab fully covering her hair and neck, standing in the dim office, a phone pressed to her ear, her other hand clasped at her chest, eyes wide with fear and tears, glancing toward the closed door",
         camera=f"medium close-up, eye level, {LOW} (desk top in shadow)", amb="memory", transition="dissolve", hum=True),
    # 035 ---------------------------------------------------------------- memory: Naail on the dhoni
    dict(to=65, v1="beat_023", reason="memory: Naail alive on a dhoni at night near Kandu-huttaa answers on the satellite phone",
         chars=["naail"], loc="dhoni_night",
         visual="Naail crouching at the side of a dark dhoni deck at night, a chunky satellite phone pressed to his ear, his face frightened and pale in the faint moonlight, glancing back toward the black jungle island; waves slapping the hull",
         camera=f"medium shot, slightly low angle, {LOW} (dark wooden deck)", amb="sea_boat", transition="cut", hum=True),
    # 036 ---------------------------------------------------------------- Raniya: get out now
    dict(to=67, reuse="beat_034", reason="5.4 reverse shot (memory): Raniya — 'get out of there now… they're using human beings'",
         chars=["raniya"], loc="raniya_office", visual="(reuse of beat_034)", amb="memory", transition="cut", hum=True),
    # 037 ---------------------------------------------------------------- Naail: using humans for what?
    dict(to=68, reuse="beat_035", reason="5.4 reverse shot (memory): Naail shouts 'using human beings for what?'",
         chars=["naail"], loc="dhoni_night", visual="(reuse of beat_035)", amb="sea_boat", transition="cut", hum=True),
    # 038 ---------------------------------------------------------------- Raniya: my father is a hostage
    dict(to=70, reuse="beat_034", reason="5.4 reverse shot (memory): Raniya — her father is held hostage; 'who is behind this… it's…'",
         chars=["raniya"], loc="raniya_office", visual="(reuse of beat_034)", amb="memory", transition="cut", hum=True),
    # 039 ---------------------------------------------------------------- the call cuts off
    dict(to=71, v1="beat_025", reason="memory, turning point: a door bursts open on the dhoni and the call cuts off (shown only symbolically)",
         loc="dhoni_night",
         visual="the dark empty dhoni deck at night: a satellite phone lying abandoned on the wet wooden planks, its small screen still glowing; a harsh beam of white flashlight light spilling across the deck from a cabin doorway that has just been flung open; nobody visible",
         camera="low close angle along the deck, the phone and the light beam in the upper two-thirds, the dark planks as the calm lower third",
         amb="sea_boat", transition="dissolve", hum=True, sens="violence",
         safe="the intruders, the gunshot and Naail's capture are never shown; only the abandoned phone and a flashlight beam; sound is a soft thud only"),
    # 040 ---------------------------------------------------------------- back in the safe house: Ashham thinks it through
    dict(to=73, v1="beat_026", reason="back to the present: silence in the safe house; Ashham works out Raniya's situation",
         chars=["ashham", "habeeb"], loc="safehouse",
         visual="Ashham sitting at the table with his eyes closed, jaw clenched, deep in thought, his fist resting against his lips; Habeeb beside him staring at the laptop in shock; the cold blue glow on their faces, rain on the dark window",
         camera=f"medium close two-shot, eye level, {LOW} (table top)", amb="room_night", transition="dissolve", hum=True,
         sens="violence", safe="what was done to Naail is only spoken; on screen only the two men's grave faces"),
    # 041 ---------------------------------------------------------------- Habeeb: an international crime
    dict(to=75, reuse="beat_032", reason="5.4 reverse shot: Habeeb — human drug testing is an international crime",
         chars=["habeeb"], speaker="habeeb", loc="safehouse", visual="(reuse of beat_032)", amb="room_night", transition="cut",
         sens="violence", safe="what was done to Naail's tongue is only spoken; on screen only Habeeb's shocked face"),
    # 042 ---------------------------------------------------------------- Ashham stands: to the atoll tonight
    dict(to=79, v1="beat_027", reason="action change: Ashham stands up decisively — they leave for the atoll secretly tonight",
         chars=["ashham", "habeeb"], loc="safehouse",
         visual="Ashham standing up from the table, pulling his long black raincoat back on, his face set with determination, looking toward the door; Habeeb snapping his laptop shut and slipping it into a black backpack, getting up to follow",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="room_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# focus points read off work/grid (v1 images) and work/grid/new (new images); y = face centre + ~8, clamped to the crop range
T = dict(crop="tight")
# v1 beat_003 (alley): Ashham face x30 y20, Habeeb face x64 y25
A3, H3 = dict(T, focus=[31, 35]), dict(T, focus=[64, 35])
# v1 beat_005: Kalhe face x30 y36 | v1 beat_006: Ashham face x36 y19 | v1 beat_009: Habeeb x40 y32 | v1 beat_010: Ashham x38 y17
K5, A6, H9, A10 = dict(T, focus=[31, 44]), dict(T, focus=[37, 35]), dict(T, focus=[40, 40]), dict(T, focus=[38, 35])
# v1 beat_012: Ashham x50 y15 | v1 beat_015 (car): Ashham x68 y26 | v1 beat_019: Ashham x48 y18
A12, A15, A19 = dict(T, focus=[50, 35]), dict(T, focus=[68, 35]), dict(T, focus=[48, 35])
# v1 beat_023: Naail x35 y18 | v1 beat_024: Raniya x47 y18 | v1 beat_026: Ashham x37 y22 | v1 beat_027: Ashham x34 y10, Habeeb x68 y16
N23, R24, A26 = dict(T, focus=[35, 35]), dict(T, focus=[47, 35]), dict(T, focus=[37, 35])
A27, H27 = dict(T, focus=[34, 35]), dict(T, focus=[68, 35])
# NEW images (set after looking at work/grid/new)
E5 = dict(T, focus=[48, 35])     # beat_005 Ashham at the door (face x48 y12)
K8 = dict(T, focus=[42, 35])     # beat_008 Kalhe close-up (face x42 y22)
H9n = dict(T, focus=[57, 35])    # beat_009 Habeeb in the den (face x57 y20)
A26n = dict(T, focus=[66, 35])   # beat_026 Ashham at the sea wall (face x66 y16)
H27n = dict(T, focus=[43, 35])   # beat_027 Habeeb at the sea wall (face x43 y20, regenerated once)
H32 = dict(T, focus=[55, 35])    # beat_032 Habeeb at the laptop (face x55 y25)
A33 = dict(T, focus=[48, 35])    # beat_033 Ashham hanging his coat (face x48 y15)

sh(1, "With the frightening evidence found on Kandu-huttaa, Ashham's team was forced to head straight back to Malé.")
sh(2, "Once it was certain that the launch heard from that deserted island belonged to people keeping watch on the police, the investigation's plans had to change.",
   [("boat_engine", "ލޯންޗުގެ", -22)])
sh(3, "There were still plenty of things to find before going into the secret bunker. The police are secretly monitoring the Kandu-huttaa area.")
sh(4, "The forensic report confirmed that Naail, who was found dead, was the son of Moosa Thaahir, one of Malé's most influential tycoons.")
sh(5, "Unease has settled over all of Malé's political and business circles. It's twelve noon. Heavy rain is pouring down on Malé.",
   [("rain_start", "ވާރޭ", -20)])
sh(6, "Ashham is wearing a black raincoat. It's a narrow alley off Majeedhee Magu. Habeeb is standing behind him. Sir,",
   speaker="habeeb", crop="medium", focus=[63, 42])
sh(7, "large sums of money have recently been taken out of Naail's bank accounts. The money went to people of the Maafannu Black Wolf gang,",
   speaker="habeeb", **H3)
sh(8, "Habeeb said quietly. What did he give them the money for? Blackmail? Or drugs?", speaker="ashham", **A3)
sh(9, "Ashham asked. I think it's the second reason. But that gang's leader, Kalhe,", speaker="habeeb", **H3)
sh(10, "isn't someone who'll talk easily, Habeeb said. Ashham nodded and went into a dark alley.",
   [("footsteps_pavement", "ވަން", -22)], speaker="habeeb", crop="medium", focus=[63, 42])
sh(11, "At the door of an old building there, two young men stood smoking. They had all kinds of tattoos on their bodies.",
   crop="medium", focus=[60, 45])
sh(12, "As soon as they saw Ashham they slowly started walking off. Ashham took out his card and showed it. Wait.",
   [("footsteps_pavement", "ހިނގައިގަތް", -22)], speaker="ashham", **E5)
sh(13, "I've come to meet Kalhe. About Naail's death. At Naail's name, the colour drained from the two young men's faces.",
   speaker="ashham", **E5)
sh(14, "After glancing at each other, they showed him the way inside. In a gang's lair.",
   [("door_open", "ވަނުމަށް", -22)])
sh(15, "Inside the building it's dark. It's a den of criminals. Through two or three doors, in the middle of the room where they stopped, at a big table sat Kalhe, about forty years old.",
   [("creak", "ދޮރަކުން", -22)])
sh(16, "There was a big scar on his face. He sat looking through some papers. Ashham... the famous investigator,",
   [("paper_shuffle", "ކަރުދާސްތަކެއް", -22)], speaker="kalhe", **K5)
sh(17, "Kalhe said with a smile. Why have you come to me? Kalhe, you'll know Naail was found murdered.",
   speaker="kalhe", **K5)
sh(18, "Before he died he gave you large sums of money, Ashham said, planting his hands on the table. What money would that be?",
   [("soft_thud", "އަތްވިއްދާލަމުން", -20)], speaker="ashham", **A6)
sh(19, "Kalhe lit a cigarette. Naail's a tycoon's son. He wanted protection for a secret shipment coming from abroad.",
   speaker="kalhe", **K8)
sh(20, "He gave us money to get those goods out of Malé port. What goods? Drugs?", speaker="kalhe", **K8)
sh(21, "Ashham asked in a mocking tone. No! Kalhe shook his head. It's not drugs.", speaker="kalhe", **K8)
sh(22, "It's medical supplies. But the label stuck on the outside says something else.", speaker="kalhe", **K8)
sh(23, "The way Naail told it, those goods had to go to Gaafu Alifu, Kandu-huttaa. All we did was get the goods out of the container at Malé port.",
   [("metal_door", "ކޮންޓޭނަރުން", -22)], speaker="kalhe", **K8)
sh(24, "So Naail was part of that secret laboratory, Habeeb said quietly from behind. Yes,", speaker="habeeb", **H9n)
sh(25, "but later Naail got scared. He said what they were doing was against humanity.", speaker="kalhe", **K8)
sh(26, "He wanted to stop it. Two days after that he disappeared, Kalhe explained.", speaker="kalhe", **K8)
sh(27, "Ashham, we don't kill people. Especially not in such a merciless way. That's the work of a far more powerful group.",
   speaker="kalhe", hum=True, **K8)
sh(28, "The hidden file. With the information Kalhe gave, Ashham realised that the root of Naail's death was an illegal medicine trade running in Malé's black market.")
sh(29, "They came back to the office. Habeeb was hacking the records of Malé's commercial harbour and customs. Sir! Here, found it,",
   [("keyboard_typing", "ހެކްކުރަމުން", -20), ("computer_beep", "ފެނިއްޖެ", -22)], speaker="habeeb", **H9)
sh(30, "Habeeb exclaimed. Three weeks ago a big container was imported in the name of Moosa Thaahir's company.",
   speaker="habeeb", **H9)
sh(31, "It's written that it held medical equipment. In the name of Moosa's company? Ashham was startled.",
   [("gasp", "ސިއްސައިގެން", -22)], speaker="ashham", **A10)
sh(32, "So Naail's father knows about this? No, sir. The one who signed these documents is Naail, using Moosa's name,",
   speaker="habeeb", **H9)
sh(33, "Habeeb explained in detail. And after these goods were unloaded at Malé port, they were taken to an area of Hulhumalé. Ashham thought it over.",
   speaker="habeeb", **H9)
sh(34, "When Moosa Thaahir met him, he really was grief-stricken. Yet he is hiding some secret. Habeeb,", hum=True)
sh(35, "among Naail's phone calls there were calls to that atoll hospital's number, right? Have you found that person? Ashham asked.",
   speaker="ashham", **A12)
sh(36, "Yes, it's Doctor Raniya. She's that hospital's chief surgeon. Before Naail died, she was the one he talked to most,",
   speaker="habeeb", **H9)
sh(37, "Habeeb showed Raniya's photo on the screen. Raniya is a fair, beautiful woman of about twenty-eight. She's serious by nature.",
   crop="full", focus=[58, 50], motion="pan right")
sh(38, "A well-known doctor. All these waves are breaking toward that atoll, Ashham said.", speaker="ashham", **A12)
sh(39, "People in Malé are planning this. But in practice it's run inside that atoll. The danger of being watched.",
   speaker="ashham", **A12)
sh(40, "Ashham and Habeeb left the office and got into the car to go to that warehouse in Hulhumalé. It was still raining heavily.",
   [("car_door", "އެރި", -20)])
sh(41, "As they drove on, Ashham noticed a black van coming behind them. The van was coming without any lights at all.",
   [("car_approach", "ވޭނެއް", -22), ("heartbeat", "ނެތި", -22)])
sh(42, "Its lights were switched off. Habeeb, hold on, Ashham sped the car up. The van behind sped up too.",
   [("engine_rev", "ބާރުކޮށްލި", -18), ("engine_rev", "ބާރުކުރި", -20)], speaker="ashham", **A15)
sh(43, "Near Sinamalé bridge, the van came straight at them and rammed the car. Sir! Habeeb shouted.",
   [("crash_clatter", "ޖެއްސި", -18), ("gasp", "ހަޅޭއްލަވައިގަތް", -20)], hum=True)
sh(44, "Ashham skilfully swung the car round. It was his alertness alone that kept the car from overturning. By then Habeeb had already signalled the station for backup.",
   [("brake_screech", "އަނބުރާލި", -18), ("computer_beep", "ސިގްނަލް", -22)], crop="medium")
sh(45, "The van lost control and hit the steel railing at the side of the bridge. Without stopping, Ashham drove on to Hulhumalé.",
   [("crash_clatter", "ޖެހުނު", -20), ("car_pass", "ދުއްވާލި", -20)])
sh(46, "Just then a police backup vehicle was reaching the crashed van. They want to stop us.",
   [("siren", "ވެހިކަލް", -22)], speaker="ashham", **A15)
sh(47, "Even inside Malé's police they have their people. They know our every move.", speaker="ashham", **A15)
sh(48, "Ashham said. A dangerous decision. After stopping the car at a lonely spot in Hulhumalé, Ashham looked at Habeeb.")
sh(49, "Habeeb was trembling with fear. Habeeb, are you scared? Ashham asked. Yes, sir.",
   [("breath_heavy", "ތުރުތުރު", -22)], speaker="ashham", **A26n)
sh(50, "When it gets to that point, of course you get scared. But I don't want to give up. I'll find the truth about Naail's death.",
   speaker="habeeb", **H27n)
sh(51, "We have to get justice, Habeeb said bravely. Good. Staying in Malé, there's no safety for us.",
   speaker="ashham", **A26n)
sh(52, "Tonight itself we should go to Gaafu Alifu, to meet Dr. Raniya, Ashham decided. The link between that bunker and that hospital can only be found over there.",
   speaker="ashham", **A26n)
sh(53, "Ashham sent Moosa Thaahir a message from his phone. Naail's secrets begin with your company. Reveal the truth.",
   [("phone_buzz", "މެސެޖެއް", -22)], **A19)
sh(54, "But no reply came from Moosa. Gathering evidence from Malé's secret places, Ashham realised this wasn't just the work of criminals inside the Maldives.")
sh(55, "Behind it was also the hand of a big international network. The secret room in Hulhumalé.", hum=True)
sh(56, "After the danger they met on the way onto the bridge, Ashham and Habeeb headed for a secret police safe house in Hulhumalé's second phase.")
sh(57, "It wasn't a place anyone would know. Outside, heavy rain was falling, and loud thunder rumbled across the whole area.",
   [("thunder", "ގުގުރީގެ", -16)])
sh(58, "The only light inside the room was the blue light coming from Habeeb's laptop screen. Sir,", speaker="habeeb", **H32)
sh(59, "they're monitoring all our official communication channels, Habeeb said, running his hands over the keyboard.",
   [("keyboard_typing", "ކީބޯޑުގައި", -20)], speaker="habeeb", **H32)
sh(60, "But inside Naail's iCloud backup I found an encrypted secret audio file. This is the recording of a satellite-phone call made twenty-four hours before he died.",
   speaker="habeeb", **H32)
sh(61, "Play it, quickly, Ashham said, hanging his wet coat on the arm of a chair.",
   [("cloth_rustle", "އަޅުވަމުން", -20)], speaker="ashham", **A33)
sh(62, "As Zayaan clicked, the sound of sea waves and a phone call began to play. Naail! Where are you?",
   [("computer_beep", "ކްލިކްކޮށްލުމާއެކު", -22), ("wave_crash", "ރާޅުތަކުގެ", -20)], speaker="raniya", **R24)
sh(63, "It was a woman's young but frightened voice. I'm", speaker="naail", **N23)
sh(64, "on a dhoni not far from Kandu-huttaa. Raniya, I didn't believe what you told me before.", speaker="naail", **N23)
sh(65, "But tonight I went in and looked. What kind of horrifying thing are they doing inside that bunker?",
   speaker="naail", hum=True, **N23)
sh(66, "Naail's voice was trembling. Naail, get out of there right now! If they find out you went in, they won't let you live.",
   [("breath_heavy", "ތުރުތުރު", -22)], speaker="raniya", **R24)
sh(67, "It isn't just a place for testing medicine. There they are... using human beings... Raniya's words broke off.",
   speaker="raniya", hum=True, **R24)
sh(68, "Using human beings for what? Naail shouted. My father...", speaker="naail", **N23)
sh(69, "They're holding my father hostage. I'm only doing this because I'm forced to.", speaker="raniya", hum=True, **R24)
sh(70, "Naail, do you know who is behind this among Malé's powerful men? It's... At that moment, through the call, came the loud sound of a door bursting open and the sound of a gunshot.",
   [("door_slam", "ހުޅުވުނު", -16), ("soft_thud", "ބަޑިއެއްގެ", -22)], speaker="raniya", hum=True, **R24)
sh(71, "With Naail's cry the call cut off. The doctor's secret. Silence fell over the room once again.",
   [("gasp", "ހަޅޭކުގެ", -22)], hum=True)
sh(72, "Ashham closed his eyes and sighed. Dr. Raniya, Ashham said slowly. She is",
   [("sigh", "ތަގުޅިކޮށްލި", -22)], speaker="ashham", **A26)
sh(73, "the senior surgeon of that atoll hospital. By holding her father hostage, they force her to help with the",
   speaker="ashham", **A26)
sh(74, "terrifying experiments run on that deserted island. Sir, testing drugs on human beings is an international crime.",
   speaker="habeeb", **H32)
sh(75, "This is a huge crime, Habeeb said. When Naail found out, they cut out his tongue and killed him",
   speaker="habeeb", hum=True, **H32)
sh(76, "to keep that secret. We have to go to that atoll right now. To meet Raniya, Ashham said, standing up.",
   [("cloth_rustle", "ތެދުވި", -20)], speaker="ashham", **A27)
sh(77, "She'll have the secret information and evidence for getting into the Kandu-huttaa bunker. But sir, if we go officially, they'll know.",
   speaker="ashham", **A27)
sh(78, "Even at Malé headquarters someone is working to cover up this case, Habeeb reminded him. We'll go on an ordinary sea boat.",
   speaker="habeeb", **H27)
sh(79, "Secretly, Ashham said. Habeeb, take your gear and come. There's no time. To be continued.",
   [("footsteps_pavement", "ހިނގާ", -22)], speaker="ashham", **A27)
SHOTS = S

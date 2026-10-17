"""Beat/shot plan for Project Phenix episode 322 — v2 RE-CUT on the new (slower, colloquial) audio.
v1 images are reused via v1="beat_###" (file in output/ProjectPhenix/v1/episode-322/images/); the v1 plan is kept in
output/ProjectPhenix/v1/plans/plan_phenix_322.py. New images: dialogue focus (spec 5.4) and the beat_029 outfit fix."""

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
    # beat_001  (v1 1)
    dict(to=2,
         reason='episode opening: the second underground blast shakes the island; trees torn apart, red flames',
         v1='beat_001',
         loc='kandu_beach_day',
         visual="a distant view across the white beach of Kandu-huttaa toward the jungle: a huge orange fireball and a column of black smoke and red glow rising high above the treetops in the island's interior, palm trees bending, leaves and sand blown through the air; far in the foreground on the sand, small and far from the blast, four tiny dark silhouettes crouched low with their arms over their heads, seen from behind; nobody hurt",
         camera='wide shot, eye level, the explosion and sky in the upper two-thirds, the white sand as the calm lower third',
         amb='beach_day',
         sens='violence',
         safe='the blast is shown only as distant spectacle; the four people are tiny crouched silhouettes seen from behind, nobody thrown or hurt'),
    # beat_002  (v1 2)
    dict(to=5,
         reason='time jump: an hour later Ashham opens his eyes and sits up',
         v1='beat_002',
         chars=['ashham'],
         loc='kandu_beach_day',
         visual='Ashham in plain civilian clothes (a dark-grey long-sleeved shirt and dark trousers, no police uniform), dusty and damp, unmarked, sitting up on the white sand, one hand propping him up, the other at his temple, shaking his head, dazed; his face only dusty with sand and grey ash; black smoke rising above the jungle behind him',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (white sand)',
         amb='beach_day',
         transition='black',
         sens='violence',
         safe='his small wounds and the blood at his mouth and nose are not shown: only a dusty, dazed face'),
    # beat_003  (v1 3)
    dict(to=7,
         reason='character change: Ashham reaches Habeeb, who coughs and opens his eyes',
         v1='beat_003',
         chars=['habeeb', 'ashham'],
         loc='kandu_beach_day',
         visual='Habeeb half sitting up on the sand, propped on one elbow, coughing into his fist, his glasses askew, his grey zip jacket dusty; Ashham (civilian dark-grey long-sleeved shirt, dusty) kneeling beside him with one hand on his shoulder, letting out a breath of relief; smoke haze over the jungle behind',
         camera='medium shot, slightly high angle, faces in the upper two-thirds, a calm uncluttered dark lower third (sand)',
         amb='beach_day',
         sens='other',
         safe="Habeeb 'lying on the sand' is shown already half sitting up, unhurt"),
    # beat_004  (v1 4)
    dict(to=8,
         reason='character change: Raniya with her unconscious father',
         v1='beat_004',
         chars=['raniya', 'raniya_father'],
         loc='kandu_beach_day',
         visual="Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque, kneeling on the sand in the shade of a leaning palm, teary-eyed, holding her father's hand in both of hers; her thin elderly father in loose pale-grey clothes sits slumped back against the palm trunk, eyes closed, unconscious but breathing; both dusty; smoke haze far behind",
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (sand)',
         amb='beach_day',
         sens='other',
         safe="the father's head 'in her lap' is shown as him sitting slumped against a palm trunk beside her (no person lying)"),
    # beat_005  (reuse 3)
    dict(to=10,
         reason='return: Ashham checks his pocket for the hard drive (v1 beat_005 was the same reuse)',
         reuse='beat_003',
         chars=['habeeb', 'ashham'],
         loc='kandu_beach_day',
         visual='reuse of beat_003',
         amb='beach_day'),
    # beat_006  (v1 6)
    dict(to=14,
         reason="new location/action: the dinghy smashed on the reef; Habeeb's tablet is dead",
         v1='beat_006',
         chars=['habeeb'],
         loc='kandu_reef',
         visual='the small white fibreglass dinghy smashed and broken on the dark reef rocks at the waterline, its outboard engine split apart in pieces beside it, waves washing over it; in the foreground on the sand Habeeb (glasses askew, dusty grey zip jacket) crouching and holding a dark lifeless tablet whose screen is completely black, a despairing look',
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (wet sand)',
         amb='beach_day'),
    # beat_007  (v1 7)
    dict(to=16,
         reason='action change: Ashham stands and looks at the rough sea; nobody will come',
         v1='beat_007',
         chars=['ashham'],
         loc='kandu_beach_day',
         visual="Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp), standing alone at the water's edge seen from behind at a three-quarter angle, looking out at a grey rough sea with big white-capped waves breaking, under a heavy overcast sky; black smoke drifting overhead",
         camera='medium wide shot from behind, eye level, the sea and sky in the upper two-thirds, wet sand as the calm lower third',
         amb='beach_dusk'),
    # beat_008  (v1 8)
    dict(to=18,
         reason='character change: Raniya pleads for her father; Ashham gives orders',
         v1='beat_008',
         chars=['raniya', 'raniya_father', 'ashham', 'habeeb'],
         loc='kandu_beach_day',
         visual="under the shade of tall palms at the jungle's edge in fading light: Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque, kneeling beside her thin elderly father in loose pale-grey clothes who sits slumped against a palm trunk with his eyes closed; she looks up, pleading and distraught; several steps away Ashham (civilian dark-grey shirt) stands firm, pointing along the beach and giving instructions, Habeeb (glasses, grey zip jacket) nodding beside him; a clear distance between Raniya and the men",
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (sand)',
         amb='beach_dusk'),
    # beat_009  (newN1)
    dict(to=20,
         reason='dialogue focus (5.4): Ashham takes charge and gives orders; he is too small in the v1 group image to be centred',
         speaker='ashham',
         chars=['ashham', 'habeeb'],
         loc='kandu_beach_day',
         visual="Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp), standing on the beach at the jungle's edge in fading light, turned three-quarters toward the camera, face clearly visible, determined and in command, one arm raised pointing along the shoreline as he speaks; Habeeb (glasses, dusty grey zip jacket) at the right edge of the frame, softer and out of focus, seen half from behind, listening; palms and drifting smoke haze behind",
         camera="medium close-up, eye level, Ashham's face centred in the upper half, Habeeb soft at the side, a calm uncluttered lower third (sand)",
         amb='beach_dusk'),
    # beat_010  (v1 9)
    dict(to=23,
         reason='time jump: night; Habeeb has lit a fire of dry fronds under the big trees',
         v1='beat_009',
         chars=['habeeb', 'raniya', 'raniya_father'],
         loc='kandu_beach_night',
         visual='night under huge old trees at the shore: a small fire of dry palm fronds and driftwood burning on the sand; Habeeb crouched feeding a dry frond into the flames, firelight on his glasses; a few steps away Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque sits beside her thin elderly father in loose pale-grey clothes, who rests sitting against a tree trunk with his eyes closed; the dark sea beyond',
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dark sand)',
         amb='beach_night',
         transition='black'),
    # beat_011  (v1 10)
    dict(to=25,
         reason='action change: the father wakes asking for water; Ashham brings young coconuts',
         v1='beat_010',
         chars=['ashham', 'raniya', 'raniya_father'],
         loc='kandu_beach_night',
         visual="by the small fire at night: Ashham (civilian dark-grey shirt) bending to set an opened young green coconut on a driftwood log in front of Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque, at arm's length, not touching her; her thin elderly father in loose pale-grey clothes, sitting against the tree trunk, has weakly opened his eyes; two more green coconuts on the sand; warm firelight on their faces",
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (sand and the log)',
         amb='beach_night'),
    # beat_012  (newN2)
    dict(to=27,
         reason='dialogue focus (5.4): Habeeb speaks by the fire; in the v1 fire image his face is at the far edge (shot / reverse shot with v1 beat_011)',
         speaker='habeeb',
         chars=['habeeb', 'ashham'],
         loc='kandu_beach_night',
         visual="night by the small campfire under the big trees: Habeeb (glasses, dusty grey zip jacket over a white t-shirt) sitting on the sand facing the camera across the low flames, worried and earnest, speaking, warm firelight on his face and glasses; in the left foreground the back of Ashham's head and his dark-grey civilian shirt shoulder, out of focus (over-the-shoulder); dark sea and moonlight behind",
         camera="medium close-up over Ashham's shoulder, eye level, Habeeb's face centred in the upper half and sharp, a calm uncluttered dark lower third (sand and low embers)",
         amb='beach_night'),
    # beat_013  (v1 11)
    dict(to=30,
         reason='framing change: Ashham and Habeeb by the fire; the hard drive is their weapon',
         v1='beat_011',
         chars=['ashham', 'habeeb'],
         loc='kandu_beach_night',
         visual='Ashham (civilian dark-grey shirt) and Habeeb sitting on the sand on opposite sides of the small fire at night; Ashham holds up a small black external hard drive between his fingers, looking at it with fierce determination; Habeeb, worried, watches him over the flames, firelight on his glasses',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (sand)',
         amb='beach_night',
         transition='cut'),
    # beat_014  (v1 12)
    dict(to=33,
         reason='turning point: a searchlight far out at sea; Ashham smothers the fire',
         v1='beat_012',
         chars=['ashham', 'habeeb', 'raniya'],
         loc='kandu_beach_night',
         visual="Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp) on one knee pushing sand with both hands over the fire, smothering it, a curl of grey smoke rising; behind him Habeeb and Raniya (her reference image is used only for her face: NO white coat, no doctor's coat; she wears only a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck), a step apart from him, ducking low and staring out to sea, where far away on the black water a powerful white searchlight beam sweeps toward the island",
         camera='medium wide shot, low angle, faces in the upper two-thirds, a calm uncluttered dark lower third (dark sand)',
         amb='beach_night'),
    # beat_015  (v1 13)
    dict(to=37,
         reason="new characters: the guards' launch arrives; three men with flashlights find the smoke",
         v1='beat_013',
         loc='kandu_beach_night',
         visual='night on the beach: a dark launch nosing into the shallow lagoon with its searchlight on; three dark figures in black clothes and black face masks wading onto the beach, each holding only a bright flashlight, beams criss-crossing the sand and falling on a small mound of sand with a thin wisp of smoke rising from it; their hands hold nothing but flashlights; no lettering on the launch',
         camera='wide shot from the tree line, eye level, the launch and figures in the upper two-thirds, the dark beach as the calm lower third',
         amb='beach_night',
         sens='violence',
         safe='the armed guards are shown with flashlights only, no weapons visible'),
    # beat_016  (v1 14)
    dict(to=38,
         reason='action change: Ashham crawls through the dark behind the guards',
         v1='beat_014',
         chars=['ashham'],
         loc='kandu_beach_night',
         visual="Ashham (civilian dark-grey shirt) crouched low in the dark bushes at the jungle's edge, seen in profile, intense focused eyes, his hands empty and resting on the sand, watching three flashlight beams moving on the beach beyond the leaves",
         camera='medium close-up, low angle, faces in the upper two-thirds, a calm uncluttered dark lower third (dark sand and leaves)',
         amb='jungle_night',
         sens='violence',
         safe='loading his gun is not shown; his hands are empty'),
    # beat_017  (v1 15)
    dict(to=40,
         reason='action change: the short fight in the dark (shown only as a dropped flashlight)',
         v1='beat_015',
         loc='kandu_beach_night',
         visual='the empty dark beach at night: a single flashlight lying dropped on the sand, still switched on, its beam lighting a long cone of empty sand and scattered footprints; in the background two more flashlight beams spinning wildly through the darkness between the palm trunks; no person visible',
         camera='low ground-level shot, the spinning beams in the upper two-thirds, the lit sand as the calm lower third',
         amb='beach_night',
         sens='violence',
         safe='the takedown and the gunfight are never shown: only a dropped flashlight on the empty beach and spinning beams'),
    # beat_018  (v1 16)
    dict(to=42,
         reason='action change: the captain fires from the launch; bark splinters fly beside Ashham',
         v1='beat_016',
         chars=['ashham'],
         loc='kandu_beach_night',
         visual="night, the campfire already put out (no fire anywhere): chips of bark and splinters bursting off a palm trunk in the glare of the launch's searchlight; Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp) pressed with his back against the far side of the trunk, empty hands, his tense face turned away; the launch's light glaring from the water behind",
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dark sand)',
         amb='beach_night',
         sens='violence',
         safe="gunfire shown only as bark splinters off a tree; Ashham's hands empty, no gun"),
    # beat_019  (v1 17)
    dict(to=44,
         reason='character/action change: the captain reverses; Habeeb dives into the sea',
         v1='beat_017',
         chars=['habeeb'],
         loc='kandu_beach_night',
         visual="night: Habeeb (glasses, grey zip jacket) diving headfirst from the shallows into the black sea toward a dark launch that is backing away from the beach, its engine churning white foam; moonlight and the launch's light on the spray; no lettering on the launch",
         camera='medium wide shot, eye level, the launch and the diving figure in the upper two-thirds, dark water as the calm lower third',
         amb='beach_night'),
    # beat_020  (v1 18)
    dict(to=46,
         reason='action change: Ashham leaps aboard and throws the captain into the sea; the launch is theirs',
         v1='beat_018',
         chars=['ashham', 'habeeb'],
         loc='kandu_beach_night',
         visual='night in the lagoon: the big dark twin-engine launch; Ashham (civilian dark-grey shirt) standing firm on its rear deck in silhouette against the cabin light, one hand gripping the rail; beside the launch a big white splash in the black water where someone has just gone overboard (no person visible in the splash); Habeeb in the water at the stern, holding the stern rail, looking up',
         camera='medium wide shot, slightly low angle, the launch in the upper two-thirds, black water as the calm lower third',
         amb='sea_boat',
         sens='violence',
         safe="the captain's pistol, the struggle and the throw are not shown: only Ashham standing on the deck and a splash beside the launch"),
    # beat_021  (newN4)
    dict(to=48,
         reason='new framing for dialogue (5.4): Ashham at the wheel shouts orders and later lays out the plan; in the v1 cabin two-shot his face sits at the edge',
         speaker='ashham',
         chars=['ashham'],
         loc='launch_cabin',
         visual='inside the dark launch cabin at night, Ashham ALONE in the frame (exactly one person, nobody else in the cabin, no second man, no other figure behind him): Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp), standing at the round steering wheel gripping it hard with both hands, his face turned three-quarters toward the camera, clearly visible, fierce and determined, speaking; warm amber cabin light on his face, the glow of the navigation screen at the edge, the black sea through the windscreen behind him',
         camera="medium close-up, eye level, Ashham's face centred in the upper half and sharp, a calm uncluttered dark lower third (the dark console)",
         amb='sea_boat'),
    # beat_022  (newN3)
    dict(to=50,
         reason='dialogue focus (5.4): Habeeb reports from the navigation screen; in the v1 cabin two-shot his face sits at the edge (shot / reverse shot with the Ashham-at-the-wheel image)',
         speaker='habeeb',
         chars=['habeeb', 'ashham'],
         loc='launch_cabin',
         visual='inside the dark launch cabin at night: Habeeb (glasses, damp hair, grey zip jacket over a white t-shirt) seated at the glowing navigation and radar screen, turned toward the camera, speaking with a faint relieved smile, the cold green-blue glow of the screen on his face and glasses; the screen shows only soft green sweeps and blurred shapes, no numbers; Ashham (dark-grey civilian shirt) at the wheel at the left edge of the frame, out of focus',
         camera="medium close-up, eye level, Habeeb's face centred in the upper half and sharp, a calm uncluttered dark lower third (the dark console)",
         amb='sea_boat',
         transition='cut'),
    # beat_023  (v1 19)
    dict(to=52,
         reason='new location: inside the cabin; lights on, radar shows the course to Malé',
         v1='beat_019',
         chars=['ashham', 'habeeb'],
         loc='launch_cabin',
         visual='inside the launch cabin at night: Ashham (civilian dark-grey shirt, damp) at the wheel looking ahead through the dark windscreen; beside him Habeeb, wet hair, glasses on, smiling at a glowing navigation and radar screen showing only soft green sweeps and blurred shapes, no numbers',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dark console)',
         amb='sea_boat'),
    # beat_024  (v1 20)
    dict(to=54,
         reason='scene change: the launch cuts across the dark sea, only its white wake visible',
         v1='beat_020',
         loc='launch_sea',
         visual='a wide high view of a big twin-engine launch speeding across the pitch-black open sea at night, only its long white foaming wake visible behind it, faint stars, no land in sight; no lettering on the hull',
         camera='wide aerial shot, the launch and its wake in the upper two-thirds, black water as the calm lower third',
         amb='sea_boat'),
    # beat_025  (v1 21)
    dict(to=55,
         reason='character change: Raniya with her father in the cabin, relieved',
         v1='beat_021',
         chars=['raniya', 'raniya_father'],
         loc='launch_cabin',
         visual='in a corner of the launch cabin at night: Raniya without any white coat, in a loose long-sleeved ankle-length dusty-blue dress and a navy hijab fully covering her hair and neck, damp but fully opaque, sitting on a cushioned bench; her thin elderly father in loose pale-grey clothes sits beside her wrapped in a grey blanket, his head resting on her shoulder, eyes closed, breathing peacefully; Raniya looking down at him with quiet relief',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (bench and cabin floor)',
         amb='sea_boat',
         sens='other',
         safe="the father's head 'in her lap' is shown as him sitting beside her, head on her shoulder (mahram)"),
    # beat_026  (reuse 22)
    dict(to=58,
         reason='return (shot / reverse shot): Habeeb at the navigation screen',
         reuse='beat_022',
         speaker='habeeb',
         chars=['habeeb', 'ashham'],
         loc='launch_cabin',
         visual='reuse of beat_022',
         amb='sea_boat',
         transition='cut'),
    # beat_027  (reuse 21)
    dict(to=60,
         reason='return (shot / reverse shot): Ashham at the wheel answers',
         reuse='beat_021',
         speaker='ashham',
         chars=['ashham'],
         loc='launch_cabin',
         visual='reuse of beat_021',
         amb='sea_boat',
         transition='cut'),
    # beat_028  (v1 23)
    dict(to=63,
         reason='framing change: Ashham looks at the small hard drive, their only weapon',
         v1='beat_023',
         chars=['ashham'],
         loc='launch_cabin',
         visual='close-up of Ashham (civilian dark-grey shirt) at the wheel in the dark cabin, holding up a small black hard drive in the glow of the navigation screen, examining it, his eyes hard and determined; the black sea beyond the windscreen',
         camera='close-up, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dark console)',
         amb='sea_boat'),
    # beat_029  (v1 24)
    dict(to=66,
         reason='scene change: Fairooz in his top-floor HQ office, satellite photos of the destroyed bunker',
         v1='beat_024',
         chars=['fairooz'],
         loc='fairooz_office',
         visual='Fairooz leaning back in a big leather chair behind his broad desk with a satisfied, victorious smile, facing a large wall screen that shows a blurred grey aerial image of a smoking crater in green jungle; city lights through the window; no text on the screen',
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (the dark desk top)',
         amb='office_night',
         sens='other',
         safe='the destroyed bunker appears only as a blurred aerial photo on a screen'),
    # beat_030  (newN5)
    dict(to=67,
         reason='dialogue focus (5.4): Moosa asks if it is finished; in the v1 office images he stands at the edge looking down (shot / reverse shot with Fairooz)',
         speaker='moosa',
         chars=['moosa', 'fairooz'],
         loc='fairooz_office',
         visual="Moosa standing in front of the big desk, facing the camera, exhausted and anxious, heavy-lidded eyes behind gold-rimmed glasses, hands clasped, asking a worried question; in the near foreground at the side the back of Fairooz's head and the shoulder of his dark-navy uniform as he sits in the high-backed leather chair, out of focus (over-the-shoulder); city lights through the tall window behind Moosa",
         camera="medium close-up over Fairooz's shoulder, eye level, Moosa's face centred in the upper half and sharp, a calm uncluttered dark lower third (the desk edge in shadow)",
         amb='office_night'),
    # beat_031  (newN6)
    dict(to=72,
         reason='dialogue focus (5.4): Fairooz answers over his coffee; in the v1 coffee image his face is at the far left edge (shot / reverse shot with Moosa)',
         speaker='fairooz',
         chars=['fairooz', 'moosa'],
         loc='fairooz_office',
         visual="Fairooz seated in his high-backed leather chair behind the polished desk, facing the camera, a white coffee cup raised near his chin, a cold victorious smile as he speaks; the wall screen glowing blue behind him with a blurred aerial image, no text; at the right edge in the foreground the shoulder of Moosa's dark suit, out of focus, seen from behind",
         camera="medium close-up, eye level, Fairooz's face centred in the upper half and sharp, a calm uncluttered dark lower third (the polished desk top)",
         amb='office_night',
         transition='cut'),
    # beat_032  (reuse 30)
    dict(to=73,
         reason='return (shot / reverse shot): Moosa worries about questions in the police',
         reuse='beat_030',
         speaker='moosa',
         chars=['moosa', 'fairooz'],
         loc='fairooz_office',
         visual='reuse of beat_030',
         amb='office_night',
         transition='cut'),
    # beat_033  (v1 26)
    dict(to=76,
         reason='action change: Fairooz shows the prepared official report',
         v1='beat_026',
         chars=['fairooz', 'moosa'],
         loc='fairooz_office',
         visual="close on the desk: Fairooz's hand pushing a closed plain dark folder with a blank cover across the polished desk, Fairooz smirking above it; Moosa in the background, uneasy, looking at the folder",
         camera='medium close-up, slightly high angle, faces in the upper two-thirds, a calm uncluttered dark lower third (polished desk)',
         amb='office_night',
         transition='cut'),
    # beat_034  (v1 25)
    dict(to=77,
         reason="return to the v1 two-shot: Moosa sighs, trapped in Fairooz's plan (v1 beat_027 reused this image too)",
         v1='beat_025',
         chars=['fairooz', 'moosa'],
         loc='fairooz_office',
         visual='Moosa standing tired and anxious in front of the desk, shoulders slumped, hands clasped; Fairooz seated behind the desk holding a coffee cup to his lips with a cold smile; the wall screen glowing behind',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (desk top)',
         amb='office_night'),
    # beat_035  (v1 28)
    dict(to=80,
         reason='time and scene change: 3 am, the launch reaches a lonely spot of Hulhumalé',
         v1='beat_028',
         chars=['ashham', 'habeeb'],
         loc='hulhumale_shore',
         visual='3 am: the dark launch drifting against a quiet stretch of Hulhumalé shore with sand and large boulders; Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp) stepping off the bow onto the sand first, Habeeb behind him on the deck; a few far-off street lights and dark apartment blocks; no lettering on the launch',
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dark sand)',
         amb='beach_night',
         transition='black'),
    # beat_036  (newN7)
    dict(to=84,
         reason="fix (v1 beat_029 showed Raniya in her white doctor's coat) + dialogue focus (5.4): Habeeb and Ashham talk as they walk",
         speaker='habeeb',
         chars=['habeeb', 'ashham', 'raniya_father'],
         loc='hulhumale_street',
         visual='two men walking side by side toward the camera along an empty dark Hulhumalé street at night: Habeeb (glasses, dusty grey zip jacket over a white t-shirt) just left of centre, turned slightly toward his companion, talking and gesturing with one hand, and Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp) just right of centre, listening, both faces clearly visible and sharp; several steps behind them, small and softly out of focus, a young woman in a navy hijab fully covering her hair and neck and a loose long-sleeved ankle-length dusty-blue dress (no coat of any kind, nothing white) walks beside her thin elderly father in loose pale-grey clothes, holding his arm; tall apartment blocks, sparse sodium street lights, damp pavement',
         camera="medium two-shot, eye level, the two men's faces in the upper half, a calm uncluttered dark lower third (damp pavement)",
         amb='street_night'),
    # beat_037  (v1 30)
    dict(to=85,
         reason='character enters: Faahid opens his door, stunned',
         v1='beat_030',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_corridor',
         visual='the dim fourth-floor apartment corridor at night: the front door open, Faahid (dark-olive shirt) standing in the doorway in the warm light from inside, eyes wide with shock; Ashham (his reference image is used only for his face: he is NOT in police uniform; he wears a plain charcoal-grey civilian long-sleeved shirt with no epaulettes, no badges and no belt, worn untucked over dark trousers, dusty and damp) and Habeeb, damp and dusty, standing in the corridor before him',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (corridor floor)',
         amb='home_night'),
    # beat_038  (newN8)
    dict(to=86,
         reason='dialogue focus (5.4): Faahid, stunned, speaks at his door; in the v1 corridor image he is at the far left edge',
         speaker='faahid',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_corridor',
         visual='Faahid (dark-olive shirt) standing in his open front doorway facing the camera, warm lamp light from inside behind him, eyes wide with shock and disbelief, speaking; in the dim corridor foreground, out of focus and seen from behind at the left and right edges of the frame, the shoulders and backs of the heads of Ashham (charcoal-grey civilian shirt, NOT police uniform) and Habeeb (grey zip jacket)',
         camera="medium close-up between the two men's shoulders, eye level, Faahid's face centred in the upper half and sharp, a calm uncluttered dark lower third (corridor floor in shadow)",
         amb='home_night',
         transition='cut'),
    # beat_039  (reuse 37)
    dict(to=87,
         reason='return (shot / reverse shot): Ashham answers Faahid at the door',
         reuse='beat_037',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_corridor',
         visual='reuse of beat_037',
         amb='home_night',
         transition='cut'),
    # beat_040  (v1 31)
    dict(to=89,
         reason="scene change: the hard drive in Faahid's computer; his face fills with fury",
         v1='beat_031',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_flat',
         visual="in Faahid's living room at night: Faahid seated at the desk, Ashham (civilian dark-grey shirt) and Habeeb standing behind him, all three faces lit by the cold glow of the computer monitor (screen seen from the side, unreadable); a small black hard drive plugged into the computer; Faahid's face hardening into fury",
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (desk top)',
         amb='living_night',
         sens='violence',
         safe='the killing video and experiment documents are never shown: only faces lit by a screen seen from the side'),
    # beat_041  (v1 32)
    dict(to=91,
         reason='action change: Faahid strikes the table and lays out the press-conference plan',
         v1='beat_032',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_flat',
         visual='Faahid (dark-olive shirt) standing at the wooden table, his palm pressed down hard on the tabletop, leaning forward and speaking fiercely; Ashham (civilian dark-grey shirt) and Habeeb listening intently across the table; the computer glowing behind',
         camera='medium shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (table top)',
         amb='living_night'),
    # beat_042  (reuse 40)
    dict(to=92,
         reason="return (shot / reverse shot): Ashham, standing at Faahid's desk, answers",
         reuse='beat_040',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_flat',
         visual='reuse of beat_040',
         amb='living_night',
         transition='cut'),
    # beat_043  (reuse 41)
    dict(to=94,
         reason='return (shot / reverse shot): Faahid lays out the press-conference plan',
         reuse='beat_041',
         chars=['faahid', 'ashham', 'habeeb'],
         loc='faahid_flat',
         visual='reuse of beat_041',
         amb='living_night',
         transition='cut'),
    # beat_044  (newN9)
    dict(to=96,
         reason='dialogue focus (5.4): Habeeb offers to hack the broadcast; in the v1 flat images his face is turned away or at the edge',
         speaker='habeeb',
         chars=['habeeb', 'faahid', 'ashham'],
         loc='faahid_flat',
         visual="in Faahid's living room at night: Habeeb (glasses, dusty grey zip jacket over a white t-shirt) sitting at the wooden table facing the camera, leaning forward keenly with a confident look, speaking, one hand resting on a closed laptop, lamp light and the cold computer glow on his face; Faahid (dark-olive shirt) and Ashham (charcoal-grey civilian shirt) at the two edges of the frame, out of focus, seen half from behind",
         camera="medium close-up, eye level, Habeeb's face centred in the upper half and sharp, a calm uncluttered dark lower third (the table top)",
         amb='living_night',
         transition='cut'),
    # beat_045  (v1 33)
    dict(to=98,
         reason="time jump: sunrise; disguised in police uniforms, they drive to Malé in Faahid's car",
         v1='beat_033',
         chars=['ashham', 'habeeb'],
         loc='car_morning',
         visual='inside a car crossing the long sea bridge toward Malé at sunrise: Ashham driving, in dark-navy police uniform with a navy police cap pulled low and dark sunglasses (plain epaulettes, no badges, no lettering), and in the passenger seat Habeeb (his reference image is used only for his face and glasses: he is NOT wearing his grey jacket or white t-shirt; he wears a dark-navy police uniform shirt buttoned up, navy trousers, a navy police cap and dark sunglasses); tense faces, golden low sunlight through the windscreen',
         camera='medium shot through the windscreen, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (dashboard in shadow)',
         amb='car_interior',
         transition='black'),
    # beat_046  (v1 34)
    dict(to=99,
         reason='scene change: the car stops at police HQ, crowded with journalists',
         v1='beat_034',
         loc='police_hq_ext',
         visual='morning: the front of the large modern police headquarters building in Malé, a big crowd of journalists with TV cameras on tripods and microphones gathered at the entrance, a white car pulling up at the kerb; no writing anywhere',
         camera='wide shot, eye level, the building and crowd in the upper two-thirds, the paved forecourt as the calm lower third',
         amb='city_day'),
    # beat_047  (v1 35)
    dict(to=103,
         reason='action change: they slip inside among a group of police and split up',
         v1='beat_035',
         chars=['ashham', 'habeeb'],
         loc='police_hq_lobby',
         visual='inside the busy entrance lobby of police headquarters: a group of uniformed police officers walking in; among them Ashham in dark-navy police uniform with a navy police cap pulled low and dark sunglasses (plain epaulettes, no badges, no lettering) and Habeeb (his reference image is used only for his face and glasses: he is NOT wearing his grey jacket or white t-shirt; he wears a dark-navy police uniform shirt buttoned up, navy trousers, a navy police cap and dark sunglasses), faces tense; Ashham glancing sideways at Habeeb as the corridor splits in two directions ahead',
         camera='medium wide shot, eye level, faces in the upper two-thirds, a calm uncluttered dark lower third (polished floor)',
         amb='office_day'),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# speaker / crop / focus (spec 5.4): focus = [x%, y%] of the image, read off the grid sheets
T = "tight"

sh(1, "With a second powerful blast from deep under Kandu-huttaa's ground, the whole deserted island shook. The bushes and trees over the bunker were torn apart, and the red of the flames spread upward.",
   [("distant_boom", "ގޮވުމާއެކު", -12), ("fire_crackle", "އަލިފާނުގެ", -20)])
sh(2, "With the force of the blast, Ashham, Habeeb, Raniya and Raniya's father were flung onto the white sand of the beach.",
   [("soft_thud", "ވިއްސައިގެން", -22)], hum=True)
sh(3, "A deafening, ear-ringing roar. About an hour later. Ashham slowly opened his eyes. He shook his head.",
   [("breath", "ހުޅުވާލި", -22)])
sh(4, "His whole body was covered in small wounds; traces of blood showed at his mouth and nose. He got up and looked around.")
sh(5, "Black smoke was still rising from where the bunker had been. Of that terrifying laboratory not a trace was left. Habeeb…",
   hum=True, speaker="ashham", crop=T, focus=[44, 35])
sh(6, "Raniya… Ashham called out in a hoarse voice. Half crawling, he went to Habeeb lying on the sand, took him by the shoulder and shook him.",
   [("cloth_rustle", "ފިރުކެމުން", -22)], speaker="ashham", crop=T, focus=[68, 35])
sh(7, "Habeeb suddenly coughed and opened his eyes. Knowing he was safe, Ashham let out a breath of relief.",
   [("gasp", "ހޮޑުލަމުން", -22), ("sigh", "ނޭވާއެއްލި", -20)])
sh(8, "Not far away Raniya sat crying, her father's head in her lap. Her father was breathing, but he lay unconscious. The hard drive…",
   [("sob_breath", "ރޯން", -24)], hum=True)
sh(9, "Habeeb's very first concern was whether the vital evidence was safe. Ashham quickly reached into his pocket.")
sh(10, "The small hard drive with the forensic data was safe. We're stranded on this deserted island now.",
   speaker="ashham", crop=T, focus=[68, 35])
sh(11, "Cut off from the outside world: the small dinghy they came in had been flung onto the reef by the blast and smashed to pieces.",
   [("wave_crash", "ފަރުމައްޗަށް", -20)])
sh(12, "The engine was in fragments. Habeeb tried to switch on his tablet, but it wouldn't work. Sir,",
   speaker="habeeb", crop=T, focus=[34, 35])
sh(13, "it's completely gone. It won't even turn on. Our satellite modem fell and broke too,",
   speaker="habeeb", crop=T, focus=[34, 40])
sh(14, "Habeeb said in despair. We can't reach Malé, or even a nearby island. We're cut off.",
   speaker="habeeb", crop=T, focus=[34, 35])
sh(15, "Ashham stood up and looked toward the shore. In the distance lay a rough sea; big waves were breaking.",
   [("wave_crash", "ރާޅުތައް", -18)])
sh(16, "Fairooz would believe they had died in the blast inside the bunker. So no police from Malé would ever come looking for them.")
sh(17, "Fairooz was sure to have their names marked as dead in the police records. We'll starve to death on this island,",
   hum=True, speaker="raniya", crop=T, focus=[32, 47])
sh(18, "Raniya said, crying. Father needs medical help. The effects of the chemicals in his body have to be cleared.",
   [("sob_breath", "ރޮމުން", -24)], speaker="raniya", crop=T, focus=[32, 47])
sh(19, "Ashham's mind began to work hard. As an investigator he knew that the moment you give up hope, you are beaten.")
sh(20, "Habeeb, walk around the island. We might spot a fishing dhoni. We have to find a way. Raniya, take your father somewhere with shade.",
   speaker="ashham", crop=T, focus=[40, 35])
sh(21, "Night on the deserted island: the sun set and pitch darkness took over. After the bunker blast the island seemed even more silent.")
sh(22, "They stayed in the shade of some huge trees on the shore. Habeeb had found some dry fronds and lit a fire.",
   [("fire_crackle", "އަލިފާންގަނޑެއް", -18)])
sh(23, "Not only for warmth, but also in the hope that a vessel passing at sea would see its light. Raniya's father opened his eyes.")
sh(24, "In a trembling voice he said: Daughter… water… There wasn't a drop of water.",
   speaker="raniya_father", crop=T, focus=[53, 42])
sh(25, "Finding clean drinking water is no easy thing. Ashham climbed a nearby palm and picked two or three young coconuts. He cut one open and handed it to Raniya.",
   [("leaves_rustle", "ރުކަކަށް", -20), ("soft_thud", "ކަނޑާލުމަށްފަހު", -22)])
sh(26, "Sir, by now Fairooz will have brought everything under his control, Habeeb said, sitting and watching the fire.",
   speaker="habeeb", crop=T, focus=[62, 35])
sh(27, "With the money of Naail's father Moosa Thaahir and Fairooz's power joined together, how can we stop them?",
   speaker="habeeb", crop="medium", focus=[62, 42])
sh(28, "Money and power are like a scrap of paper before the truth. Ashham looked at the hard drive.",
   speaker="ashham", crop=T, focus=[30, 35])
sh(29, "In here is the video of Fairooz himself ordering Naail's killing. And the dealings with the international company.",
   speaker="ashham", crop=T, focus=[30, 35])
sh(30, "The moment we reach Malé, their ruin will begin. But how will we get to Malé?",
   speaker="ashham", crop=T, focus=[30, 35])
sh(31, "Raniya asked. At that moment a powerful light appeared far out at sea. It wasn't a boat's light. It was a searchlight.",
   hum=True, speaker="raniya", crop=T, focus=[69, 35])
sh(32, "The trap: Ashham at once threw sand over the fire and put it out. Everyone get down!",
   [("leaves_rustle", "ތިރިވޭ", -20)], speaker="ashham", crop=T, focus=[46, 35])
sh(33, "he ordered. That light is heading for the island's lagoon. It is the launch of Fairooz's guards.",
   [("boat_engine", "ލޯންޗު", -18)], speaker="ashham", crop="medium", focus=[46, 42])
sh(34, "They had come back to check the blast site of the bunker and make sure no trace of Ashham's group could be seen.")
sh(35, "The launch slowly came in toward the beach. Three armed men got off. They had powerful flashlights in their hands. Look over here!",
   [("footsteps_sand", "ފޭބި", -18), ("flashlight_click", "ފްލޭޝްލައިޓްތައް", -18)], speaker="guard", crop=T, focus=[51, 44])
sh(36, "one of them shouted. What he saw was the smoke of the fire Ashham's group had just put out. They're alive!",
   hum=True, speaker="guard", crop="medium", focus=[51, 44])
sh(37, "Find them! another ordered. Ashham told Habeeb and the others to wait among the trees, loaded the last rounds he had, and slipped around behind the guards.",
   [("leaves_rustle", "ޖެހިލި", -22)], speaker="guard", crop=T, focus=[51, 44])
sh(38, "This was the only chance they would get to seize their launch. If they got that launch, the way to Malé would open.")
sh(39, "Crawling through the darkness, Ashham grabbed the man at the very back by the neck and brought him to the ground.",
   [("footsteps_sand", "ފިރުކެމުން", -22), ("soft_thud", "ވައްޓާލި", -23)])
sh(40, "He took the man's weapon and turned on the other two. After a short clash in the pitch dark, through Ashham's skill all three men were put out of action.",
   [("soft_thud", "ކުރިމަތިލުމަކަށްފަހު", -24)], hum=True)
sh(41, "But then someone began firing from inside the launch. One man was still aboard — their captain. The hope of escape:")
sh(42, "The rounds struck the tree beside Ashham. The weapon in Ashham's hand was out of ammunition.",
   [("soft_thud", "ރުކަށް", -22)])
sh(43, "The captain started the launch's engine and tried to back away. No! That's our only way out!",
   [("engine_rev", "ސްޓާޓުކޮށްލަމުން", -16)], speaker="habeeb", crop=T, focus=[46, 35])
sh(44, "Habeeb burst out from the trees, ran and plunged into the sea. He swam and grabbed hold of the steel rail at the launch's stern.",
   [("splash", "ފުންމާލި", -14)])
sh(45, "As the captain spotted Habeeb and drew his pistol to fire, Ashham sprinted, leapt, and landed right inside the launch.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(46, "He seized the captain's arm, took the weapon and threw him into the sea. The launch was now under Ashham's control — a big twin-engine launch.",
   [("splash", "ކޮއްޕާލި", -14)])
sh(47, "It had a full load of fuel and communication equipment. Habeeb! Quickly, bring Raniya and her father!",
   speaker="ashham", crop=T, focus=[47, 35])
sh(48, "Ashham shouted, gripping the wheel. Habeeb brought Raniya and her father aboard the launch.",
   speaker="ashham", crop="medium", focus=[47, 42])
sh(49, "As the lights inside the launch came on, the radar showed the course to Malé. Sir, this launch has full satellite navigation,",
   [("power_up", "ދިއްލާލުމާއެކު", -18), ("computer_beep", "ރާޑަރުން", -20)], speaker="habeeb", crop=T, focus=[56, 35])
sh(50, "Habeeb said with a smile. Fairooz will think we're dead. But we're going to Malé.",
   speaker="habeeb", crop="medium", focus=[56, 42])
sh(51, "The launch left Kandu-huttaa's lagoon, cutting through the waves and setting course out into the Huvadhu channel. The destination: Malé.",
   [("boat_engine", "ލޯންޗު", -16)])
sh(52, "They were now on a journey of revenge. Shadow on the sea:")
sh(53, "Saved from Kandu-huttaa's horrors, the launch Eagle Speed carrying Ashham's group pushed on, cutting through the swell.")
sh(54, "In the pitch darkness of the night nothing could be seen but the white wake forming behind the launch. Silence filled the launch.")
sh(55, "Raniya sat with her father's head in her lap, at peace that his breathing was steadying.")
sh(56, "Sir, we're now entering Malé's regional radio signal range, Habeeb said, watching the launch's navigation screen.",
   speaker="habeeb", crop=T, focus=[56, 35])
sh(57, "But I'm still not contacting the police on any official channel.",
   speaker="habeeb", crop="medium", focus=[56, 42])
sh(58, "Because the whole communications network is under ACP Fairooz's control. Good,",
   speaker="habeeb", crop=T, focus=[56, 35])
sh(59, "Ashham said, gripping the wheel hard. Fairooz thinks we turned to ash inside that bunker.",
   speaker="ashham", crop=T, focus=[47, 35])
sh(60, "We won't come in to Malé's main harbour. His guards will be there.",
   speaker="ashham", crop="medium", focus=[47, 42])
sh(61, "We have to slip in secretly at a lonely spot in Hulhumalé. Ashham took the small hard drive from his pocket and looked at it.",
   speaker="ashham", crop=T, focus=[39, 35])
sh(62, "It was their only weapon. The evidence in it was dangerous enough to cut Fairooz's power down completely.")
sh(63, "But before revealing it, they had to find out what trap Fairooz was preparing in Malé.")
sh(64, "Malé's nerve centre: at that moment, in the top-floor office of Malé police headquarters, Assistant Commissioner Fairooz sat in his comfortable chair.")
sh(65, "On the big TV screen in front of him were satellite photos of the island's bunker blown up and completely destroyed.")
sh(66, "A smile of victory showed on his face. The office door opened and in walked the tycoon Moosa Thaahir.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(67, "His face showed exhaustion and unease. Fairooz, is it all finished?",
   speaker="moosa", crop=T, focus=[37, 35])
sh(68, "Moosa asked. Yes, Moosa. The bunker has been completely destroyed.",
   speaker="fairooz", crop="medium", focus=[38, 42])
sh(69, "Ashham, his helper and that doctor too are now buried beneath it,",
   hum=True, speaker="fairooz", crop=T, focus=[38, 35])
sh(70, "Fairooz said, sipping from his coffee cup. Every problem your son Naail created",
   [("cup_clatter", "ތަށީގައި", -20)], speaker="fairooz", crop="medium", focus=[38, 42])
sh(71, "is now solved. Not a single trace of Project Phenix will remain.",
   speaker="fairooz", crop=T, focus=[38, 35])
sh(72, "The medicines in the Malé warehouse are now ready to ship abroad. But",
   speaker="fairooz", crop="medium", focus=[38, 42])
sh(73, "won't questions about Ashham's death come up inside the police? Moosa worried. I've already prepared the official report,",
   speaker="moosa", crop=T, focus=[37, 35])
sh(74, "Fairooz said, showing a file on the desk. It says that Ashham and Habeeb",
   [("paper_shuffle", "ފައިލެއް", -18)], speaker="fairooz", crop=T, focus=[36, 40])
sh(75, "took bribes in the Naail murder case and were trying to flee the country together with criminals.",
   speaker="fairooz", crop=T, focus=[36, 35])
sh(76, "The report will conclude that the launch they were on sank at sea. Tomorrow morning I'll release the news to the media.",
   speaker="fairooz", crop=T, focus=[36, 35])
sh(77, "Moosa let out a deep breath. Even after his own son's death, to save his business and influence he had to take part in Fairooz's ruthless plan.",
   [("sigh", "ނޭވާއެއްލި", -18)], hum=True)
sh(78, "The Hulhumalé shore: at three in the early morning, Ashham's launch drew close to an area of Hulhumalé's second phase.",
   [("boat_engine", "ކައިރިކުރި", -18)])
sh(79, "It was a place with few street lights where people don't usually go. After the launch's engine was cut, Ashham stepped off first.",
   [("footsteps_sand", "ފޭބި", -18)])
sh(80, "Behind him Habeeb got off, bringing Raniya and her father. Habeeb, is there anyone in Malé we can trust?",
   speaker="ashham", crop=T, focus=[51, 35])
sh(81, "Ashham asked. Our former senior officer, retired Commissioner Faahid, Habeeb said, thinking.",
   speaker="habeeb", crop=T, focus=[40, 35])
sh(82, "He was removed from his post for opposing Fairooz's influence and crimes. He lives in a flat in Hulhumalé.",
   speaker="habeeb", crop=T, focus=[40, 40])
sh(83, "We can trust him. Right, we'll go to him, Ashham said.",
   speaker="ashham", crop=T, focus=[68, 35])
sh(84, "Still damp from the sea, they walked through Hulhumalé's dark streets and entered the building where Faahid's flat was.",
   [("footsteps_pavement", "ހިނގާފައި", -20)])
sh(85, "They took the lift up, and at a door on the fourth floor Ashham knocked softly. Faahid opened the door. Seeing who stood before him, his eyes went wide.",
   [("knock", "ޓަކިޖަހާލި", -14), ("door_open", "ހުޅުވާލީ", -18)])
sh(86, "Ashham? Habeeb? You… they're saying you're dead! We're alive, sir, Ashham said, stepping inside.",
   [("door_close", "ވަންނަމުން", -22)], speaker="faahid", crop=T, focus=[41, 35])
sh(87, "And we've come with evidence that will shake the entire police institution. The truth revealed:",
   speaker="ashham", crop=T, focus=[54, 35])
sh(88, "On the table in the main room of Faahid's home Ashham set down his hard drive and connected it to Faahid's computer.",
   [("keyboard_typing", "ކޮމްޕިއުޓަރަށް", -20)])
sh(89, "Seeing the video of Fairooz ordering Naail's killing, and the documents of the experiments done on humans on Kandu-huttaa, Faahid's face filled with extreme fury.",
   hum=True)
sh(90, "This is a huge betrayal! Faahid struck the table with his hand. Fairooz has disgraced the name of the whole institution.",
   [("soft_thud", "ޖެހި", -16)], speaker="faahid", crop=T, focus=[48, 35])
sh(91, "He's working to put out a statement tomorrow morning presenting you as criminals.",
   speaker="faahid", crop="medium", focus=[48, 42])
sh(92, "We have to show this evidence to the whole country before he does, Ashham said. But how do we do that?",
   speaker="ashham", crop=T, focus=[31, 35])
sh(93, "Tomorrow at nine there's a big press conference at police headquarters, Faahid said thoughtfully.",
   speaker="faahid", crop=T, focus=[48, 35])
sh(94, "Fairooz will speak at that conference himself. We have to break into the conference's live broadcast and release this video to every TV channel.",
   speaker="faahid", crop="medium", focus=[48, 42])
sh(95, "I can do that, Habeeb said keenly. But to do it I'll have to get near the headquarters building's",
   speaker="habeeb", crop=T, focus=[48, 35])
sh(96, "main server room. Into another trap:",
   speaker="habeeb", crop="medium", focus=[48, 42])
sh(97, "As the sun rose and Malé's bustle began, Ashham and Habeeb, with Faahid's help, were dressed in official police uniforms.")
sh(98, "With caps and dark glasses to hide their faces, they went to Malé in Faahid's own car.",
   [("car_door", "ކާރުގައި", -18)])
sh(99, "Raniya and her father stayed safe at Faahid's home. When the car stopped in front of headquarters, a large crowd of journalists had gathered there.",
   [("camera_shutter", "ނޫސްވެރިން", -20)])
sh(100, "All of them were impatient for the details of the news of Ashham's group's death. Ashham and Habeeb slipped into a group of police and secretly entered the building.",
    [("boots_march", "ގްރޫޕެއްގެ", -20)])
sh(101, "Their hearts pounded harder, because they knew they were walking into a trap. Habeeb,",
    [("heartbeat", "ތެޅުން", -18)], hum=True, speaker="ashham", crop=T, focus=[34, 40])
sh(102, "you go toward the server room, Ashham said quietly. I'm going to the press hall. Face to face with Fairooz.",
    speaker="ashham", crop=T, focus=[34, 35])
sh(103, "The two set off in different directions. To be continued.",
    [("footsteps_pavement", "މިސްރާބު", -20)])

SHOTS = S

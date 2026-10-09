"""Beat/shot plan for Suratul Faatihaa episode 423 (used by plan_beats.py).
Verses 2-4: majesty -> mercy (mother and sick child; hadith of the woman who finds her lost child; rahma <- rahim),
Maaliki yawmid-deen (the powerful alone on that Day, angels in rows = light pillars), the bombing passage (symbols only,
rule 7), small daily wrongs, khawf & rajaa', the sinner who wakes up (= listener), Maalik/Malik, Pharaoh & Nimrod (empty
throne), the world as an exam hall. Bible rules: no sacred figure in any form, hereafter symbolic, no text anywhere,
hijab on every woman, no bodies/blood/weapons/explosions."""

HOME_ROOM = ("a simple tidy room of a Maldivian island home, whitewashed coral-stone walls, a wooden window with shutters "
             "open to coconut palms, a woven mat on a tiled floor, a low wooden table")
BEACH_DAWN = "a quiet palm-lined Maldivian beach with a calm turquoise lagoon at dawn"
COSMOS = "deep space with luminous spiral galaxies, nebulae and countless stars"
PLAIN = "a vast empty plain under a blinding white-gold sky, fine dust drifting"
OLD_MADINAH = ("early seventh-century Madinah: a simple mosque of palm-trunk pillars with a palm-frond roof and a sandy "
               "floor, mud-brick houses, date palms")
MOSQUE_HALL = ("the prayer hall of a white coral-stone Maldivian mosque with carved dark wooden pillars, a lacquered "
               "wooden ceiling, a plain mihrab niche in the qibla wall, soft woven prayer rugs in rows, warm light through "
               "arched windows")
OFFICE = ("the top-floor executive office of a glass skyscraper in a large modern city, floor-to-ceiling windows, a "
          "polished dark wooden desk, a leather chair")

LOC = {
    "cosmos_beach": f"a quiet palm-lined Maldivian beach at night beneath {COSMOS}",
    "beach_dawn": BEACH_DAWN,
    "home_night": HOME_ROOM,
    "ocean": "the open Indian Ocean beside a Maldivian atoll, endless calm water stretching to the horizon",
    "old_madinah": OLD_MADINAH,
    "jetty_night": "a long wooden jetty reaching out into a dark Maldivian lagoon at night, a few distant island lights",
    "mosque_hall": MOSQUE_HALL,
    "scale_room": HOME_ROOM,
    "sick_room": HOME_ROOM,
    "sick_room_light": HOME_ROOM,
    "home_door": "the open wooden front door of a Maldivian island home, whitewashed coral-stone walls, a sandy yard with coconut palms and a hibiscus bush beyond",
    "window_seat": HOME_ROOM,
    "palm_sprout": "the sandy edge of a Maldivian island garden by the lagoon, a few coconut palms",
    "plain": PLAIN,
    "office": OFFICE,
    "desk_night": OFFICE,
    "ruins": "a bombed-out neighbourhood of collapsed grey concrete buildings, broken slabs and twisted rebar, dust hanging in the air",
    "home_afternoon": HOME_ROOM,
    "bedroom_predawn": HOME_ROOM,
    "beach_swing": "a palm-shaded Maldivian beach with a traditional rope-and-wood swing seat (undhoali) hanging from a wooden frame between coconut palms",
    "mosque_door": "the entrance of a white coral-stone Maldivian mosque with a carved dark wooden door, a sandy courtyard and coconut palms",
    "earth_space": f"the Earth seen from {COSMOS}",
    "pharaoh_hall": "an ancient Egyptian palace hall of massive plain sandstone columns without any carvings or inscriptions, opening onto pyramids in the desert",
    "penthouse": "the terrace of a luxury penthouse atop a skyscraper, a vast modern city and coastline spread far below",
    "exam_hall": "a large quiet examination hall of a Maldivian school, rows of single wooden desks set far apart, tall open windows with palms outside",
}
MOOD = {
    "cosmos_beach": "deep blue night, the sky ablaze with galaxies and starlight, silver light on the still lagoon, overwhelming majesty and awe",
    "beach_dawn": "dawn, soft gold light breaking through blue haze, the last grey clouds retreating, peaceful, hopeful, merciful warmth",
    "home_night": "late night, a single small oil lamp with a warm amber glow against deep teal shadows, hushed, tender and loving",
    "ocean": "golden hour, warm gold sunlight glittering on an endless ocean, vast and serene",
    "old_madinah": "bright desert morning, hazy, slightly desaturated, soft vignette, warm sand tones, an old memory, relief and love",
    "jetty_night": "cold rainy night, steel-blue and grey tones, rain streaks in the dim light, deep loneliness",
    "mosque_hall": "evening, warm brass lamps and soft gold light, emerald shadows, reverent stillness",
    "scale_room": "night, a single amber oil lamp, warm gold light and cool teal shadow perfectly balanced, contemplative",
    "sick_room": "grey overcast afternoon, muted cool light through the window, quiet loneliness and weariness",
    "sick_room_light": "afternoon, golden sunlight breaking through grey clouds and pouring in through the window, sudden hope",
    "home_door": "warm golden late afternoon, soft gold light and long gentle shadows, tender and safe",
    "window_seat": "soft early-morning light through the open shutters, a gentle golden glow, protective, peaceful",
    "palm_sprout": "a gentle sun-shower in the morning, fine sparkling raindrops lit by warm gold sunlight, nurturing and hopeful",
    "plain": "blinding white-gold light from above, absolute silence, awe, solemn but not hopeless",
    "office": "late afternoon, cold steel-blue city light with a hard gold sun glare on the glass, power and pride",
    "desk_night": "night, a single cold desk lamp, hard shadows, a chilling detachment",
    "ruins": "hazy grey-amber dust-filled daylight, muted desaturated colours, grief and silence",
    "home_afternoon": "late afternoon, warm slanting sunlight and lazy stillness, a quiet heaviness",
    "bedroom_predawn": "pre-dawn darkness, cold blue-grey light, one dim lamp, heavy regret and despair",
    "beach_swing": "bright lazy midday, glittering sea, warm careless ease",
    "mosque_door": "first light of dawn, deep blue sky turning gold, warm lamplight spilling from the open door, hope and return",
    "earth_space": "luminous white-gold light from above, majestic, vast, awe-inspiring",
    "pharaoh_hall": "dusk, hazy, slightly desaturated, soft vignette, cold arrogance and emptiness",
    "penthouse": "sunset, hard gold light and long shadows over the city, pride and possession",
    "exam_hall": "bright still morning, soft daylight through the windows, hushed concentration",
}

NOFIG = "no human figure, no silhouette"

BEATS = [
    dict(to=3, reason="episode opening: the majesty of the Lord of the worlds; a human feels his smallness", chars=["listener"], loc="cosmos_beach",
         visual="a single small man in an off-white kurta standing barefoot at the water's edge, seen from far behind, tiny beneath an immense night sky filled with luminous spiral galaxies, nebulae and countless stars reflected in the still lagoon; coconut palms in dark silhouette at the sides",
         camera="extreme wide shot, low angle, the galaxies filling the upper two-thirds, the still mirror-like lagoon as the calm lower third", amb="cosmos"),
    dict(to=6, reason="new image: after majesty comes mercy (Ar-Rahmanir-Raheem) — warm dawn breaking", loc="beach_dawn",
         visual=f"soft golden dawn light breaking through the last retreating grey clouds over a calm turquoise lagoon, warm rays fanning across the sky and touching the empty white sand, coconut palms leaning gently; nothing placed on the sand, no books, no prayer mat, no lantern; {NOFIG}",
         camera="wide shot, the glowing sky and rays in the upper two-thirds, the still lagoon and wet sand as the calm lower third", amb="dawn_exterior"),
    dict(to=9, reason="new example: the exhausted mother wakes at night to touch her sick child's forehead", chars=["mother", "son"], loc="home_night",
         visual="the mother, still wearing her cream hijab fully covering hair and neck, kneeling beside a low mattress on the woven mat, sleepy and tired yet tender, gently laying the back of her hand on the forehead of her small son, who rests under a light cotton sheet with flushed cheeks and half-closed eyes; a small oil lamp on the low wooden table beside them",
         camera="medium close-up, eye level, their faces in the upper half, the woven mat and lamp light as the lower third", amb="home_night",
         sens="other", safe="rule 6: the child's illness is shown only as flushed cheeks and resting under a sheet, no medical details or distress"),
    dict(to=12, reason="new image: all mothers' tenderness together is not even a drop compared with Allah's mercy", loc="ocean",
         visual=f"close-up of a woman's two cupped hands, with sage-green long sleeves, holding a little glistening water in front of the endless golden ocean, a single bright drop falling from her fingertips toward the vast sea below; {NOFIG} beyond the hands",
         camera="close-up of the cupped hands in the upper half, the immense glittering ocean behind and below as the calm lower third", amb="beach_dusk"),
    dict(to=16, reason="hadith story (flashback): the woman finds her lost child and clutches him to her chest", loc="old_madinah",
         visual="in a sandy lane between mud-brick houses and date palms, a young Arab mother in loose dark ankle-length robes and a black headscarf fully covering her hair and neck, kneeling in the sand and holding her small son tightly against her chest, her eyes closed in overwhelming relief; the boy in a simple pale tunic clinging to her; no other people anywhere in the scene, only low flat-roofed mud-brick houses and a low palm-frond-roofed shelter in the hazy background, no minarets, no towers, no domes",
         camera="medium shot, eye level, mother and child in the upper half, the sunlit sand as the calm lower third", amb="old_madinah_day",
         transition="dissolve", sens="sacred_figure",
         safe="rule 2: the Prophet ﷺ and the companions who witnessed it are never shown — only the mother and her child, alone in the lane"),
    dict(to=18, reason="topic change: why a heart grows hard — feeling alone in a merciless world", chars=["listener"], loc="jetty_night",
         visual="the man in his off-white kurta sitting alone at the far end of a long wooden jetty in the rain at night, shoulders hunched, seen from the side and slightly behind, staring out over the dark lagoon, his face weary and closed",
         camera="wide shot, the hunched figure in the upper half, the wet planks of the jetty as the calm lower third", amb="rain_night",
         transition="dissolve"),
    dict(to=20, reason="topic change: mercy is recalled twice at the opening of Al-Fatiha (Bismillah and verse 3)", loc="mosque_hall",
         visual=f"a closed mushaf with a deep green and gold ornamented cover resting on a carved wooden rehal on a prayer rug, a warm brass lamp glowing beside it, soft light falling from an arched window above; {NOFIG}, no letters and no calligraphy anywhere",
         camera="medium close-up, the mushaf and lamp in the upper half, the soft prayer rug as the calm lower third", amb="mosque_interior"),
    dict(to=22, reason="new image: majesty balanced by mercy — the perfect balance of hope and fear", loc="scale_room",
         visual=f"an antique brass two-pan balance scale standing perfectly level on the low wooden table, one pan softly glowing with warm golden light, the other filled with cool deep-teal shadow, the oil lamp behind it; {NOFIG}",
         camera="medium close-up, the scale centred in the upper two-thirds, the smooth table top as the calm lower third", amb="room_night"),
    dict(to=24, reason="new focus: your own life — hardship, illness, loneliness", chars=["listener"], loc="sick_room",
         visual="the man in a plain grey long-sleeved t-shirt sitting up on a simple bed against the wall, resting, pale and tired, a glass of water on the low table beside him, looking out of the open window at grey clouds, alone in the quiet room",
         camera="medium shot, eye level, his face in the upper half, the woven mat and table as the lower third", amb="room_day",
         sens="other", safe="rule 6: illness shown only as a person sitting up resting by a window; no medical equipment or suffering"),
    dict(to=26, reason="emotional turning point: the hardship itself may be a mercy — light breaks in", chars=["listener"], loc="sick_room_light",
         visual="the same man in a plain grey long-sleeved t-shirt sitting up on the simple bed, lifting his face toward the open window as a shaft of warm golden sunlight breaks through the clouds and falls across him, a faint peaceful smile beginning",
         camera="medium close-up, slightly low angle, his face and the window light in the upper two-thirds", amb="room_day"),
    dict(to=29, reason="new example: the Quran begins with mercy, as a mother first embraces her child, then advises", chars=["mother", "son"], loc="home_door",
         visual="the mother kneeling in the open doorway and warmly embracing her little son, her cheek against his hair, eyes closed in love; the boy with his arms around her neck; golden light from the sandy yard behind them",
         camera="medium shot, eye level, faces in the upper half, the doorstep and sand as the calm lower third", amb="island_house_day"),
    dict(to=31, reason="new image: rahma comes from rahim, the womb that shelters the child", chars=["mother"], loc="window_seat",
         visual="the mother, visibly expecting a baby, sitting peacefully on a cushion by the open window in a loose sage-green dress and cream hijab, both hands resting gently on her rounded belly, eyes lowered with a serene protective smile, a soft golden glow surrounding her",
         camera="medium shot, eye level, her face and hands in the upper two-thirds, the woven mat as the calm lower third", amb="room_day",
         sens="other", safe="the womb is shown only as a modestly dressed expectant mother resting her hands on her belly"),
    dict(to=34, reason="new image: mercy builds, shapes and prepares; it is sprinkled into hearts twice", loc="palm_sprout",
         visual=f"a sprouting coconut lying in the white sand with a fresh green palm shoot rising from it, fine raindrops falling and sparkling in warm morning sunlight, the turquoise lagoon blurred behind; {NOFIG}",
         camera="close-up at sand level, the shoot and raindrops in the upper two-thirds, the smooth sand as the calm lower third", amb="rain_day"),
    dict(to=37, reason="new verse: Maaliki yawmid-deen — the Day of Reckoning, awe but not despair", loc="plain",
         visual=f"a vast empty plain stretching to the horizon under a blinding white-gold sky, fine dust drifting in soft shafts of light, a faint golden horizon glow suggesting hope; {NOFIG}",
         camera="extreme wide shot, the radiant sky in the upper two-thirds, the smooth dusty ground as the calm lower third", amb="vast_plain",
         transition="dissolve", sens="hereafter", safe="rule 5: the Day of Judgement shown only as an empty radiant plain"),
    dict(to=39, reason="new parable: the powerful, the rich and the famous of this world", chars=["powerful_man"], loc="office",
         visual="the powerful man standing tall behind his polished desk in the glass-walled office, chin raised with a proud, self-satisfied look, two assistants in dark suits seen only from behind bowing slightly as they hand him folders, the city skyline glittering behind",
         camera="medium wide, slightly low angle, his face in the upper third, the polished desk top as the lower third", amb="office_day",
         transition="dissolve"),
    dict(to=42, reason="scene change: on that Day he stands utterly alone; money and fame blown away", chars=["powerful_man"], loc="plain",
         visual="the powerful man in his charcoal suit seen from far behind, very small and utterly alone in the middle of the vast empty plain under the blinding white-gold sky, a few blank paper sheets and plain blank paper slips blowing away from him in the wind and dissolving into dust",
         camera="extreme wide shot from behind, the tiny lone figure and the radiant sky in the upper two-thirds, the dusty ground as the calm lower third", amb="vast_plain",
         transition="dissolve", sens="hereafter", safe="rule 5: only one small figure from far behind on an empty plain; no resurrected crowds, no faces"),
    dict(to=46, reason="new image: angels standing in rows (Surat an-Naba') — none may speak without permission", loc="plain",
         visual=f"endless straight rows of tall soft pillars of pure white-gold light standing in perfect order across the vast plain, fading into the blinding horizon, absolute stillness; {NOFIG}, no wings, no faces",
         camera="wide shot at a low angle, the rows of light converging into the upper two-thirds, the smooth plain as the calm lower third", amb="vast_plain",
         sens="sacred_figure", safe="rule 2/5: the angels and Jibreel are shown only as rows of soft light pillars"),
    dict(to=48, reason="big topic jump: today's bombed Muslim lands — mothers searching the rubble", loc="ruins",
         visual="a woman in a dark long abaya and a dark headscarf fully covering her hair and neck kneeling on broken concrete seen entirely from behind, her hands resting on a slab of rubble; further away the silhouette of a father standing against dusty light with his hand cupped to his mouth calling out; a small child's sandal lying on the concrete in the foreground; distant smoke rising into a hazy sky",
         camera="wide shot, the figures and ruins in the upper two-thirds, the flat dusty concrete with the sandal as the calm lower third", amb="ruins_dust",
         transition="black", sens="violence",
         safe="rule 7: only ruins, dust, a mother from behind, a father's silhouette and a small sandal; no bodies, no injuries, no explosions, no weapons, no flags, no real place"),
    dict(to=49, reason="new image: those who ordered and signed for the bombing", loc="desk_night",
         visual=f"close-up of a man's hand in a dark suit sleeve and white shirt cuff signing a sheet of blank paper with a heavy fountain pen on a polished dark desk under a cold lamp; {NOFIG} beyond the hand, no face, nothing written on the paper",
         camera="close-up, the hand and pen in the upper half, the polished desk top as the calm lower third", amb="city_night_far",
         sens="violence", safe="rule 7: 'signing the order' shown only as a hand and pen on a desk; blank paper, no face"),
    dict(to=51, reason="return to Maaliki yawmid-deen: on that Day power and money avail nothing", loc="plain", reuse="beat_014",
         visual="reuse of the empty radiant plain", amb="vast_plain", transition="dissolve", sens="hereafter",
         safe="rule 5: the empty plain only"),
    dict(to=54, reason="focus change: not only oppressors — our own small daily wrongs, like delaying prayer", chars=["listener"], loc="home_afternoon",
         visual="the man in a plain grey long-sleeved t-shirt slouched on a low cushioned bench, absorbed in his phone (screen facing away from the viewer), while beside him on the woven mat a rolled-up prayer mat and a white crocheted prayer cap lie untouched; through the window a white mosque minaret glows in the late-afternoon sun",
         camera="medium wide, eye level, his face and the window in the upper half, the woven mat with the rolled prayer mat as the lower third", amb="home_day",
         transition="dissolve"),
    dict(to=57, reason="return to the balance: mercy and reckoning, khawf and rajaa' — two pans of one scale", loc="scale_room", reuse="beat_008",
         visual="reuse of the level brass balance scale", amb="room_night"),
    dict(to=60, reason="new image: fear alone brings despair, hope alone carelessness — balanced, a believer flies", loc="beach_dawn",
         visual=f"a single white seabird gliding low and steady over the calm turquoise lagoon at dawn, both wings spread wide and perfectly even, its reflection on the still water, soft gold sky; {NOFIG}",
         camera="wide shot, the bird and glowing sky in the upper two-thirds, the still lagoon as the calm lower third", amb="dawn_exterior"),
    dict(to=62, reason="new story: the long-time sinner wakes up — the first feeling, despair", chars=["listener"], loc="bedroom_predawn",
         visual="the man in a plain grey long-sleeved t-shirt sitting on the edge of a simple bed in the dark before dawn, elbows on his knees and his face buried in his hands, shoulders heavy with regret, the dim lamp casting long cold shadows",
         camera="medium shot, eye level, the hunched figure in the upper half, the tiled floor as the calm lower third", amb="room_night",
         sens="other", safe="the sins are never shown; Shaytan is not depicted — only the man's despair"),
    dict(to=64, reason="action change: the second feeling — careless overconfidence", chars=["listener"], loc="beach_swing",
         visual="the same man in a plain grey long-sleeved t-shirt lounging back carelessly on a traditional wooden swing seat under the palms, eyes half-closed, a lazy self-satisfied smile, one foot dangling, unconcerned",
         camera="medium wide, eye level, his face in the upper half, the white sand as the calm lower third", amb="beach_day"),
    dict(to=66, reason="emotional turning point: the middle path — the door of repentance is open, he returns", chars=["listener"], loc="mosque_door",
         visual="the man in his off-white kurta and a white crocheted prayer cap, barefoot, stepping toward the open carved wooden door of the white mosque at dawn, warm golden lamplight pouring out over him, his face humble and hopeful; his sandals left neatly on the step",
         camera="medium wide, eye level from slightly behind and to the side, his face and the glowing door in the upper two-thirds, the sandy courtyard as the calm lower third", amb="mosque_dawn"),
    dict(to=68, reason="new topic: Maalik (Owner) and Malik (King) — the Owner of everything", loc="earth_space",
         visual=f"the small blue-and-white Earth floating in deep space among luminous galaxies and nebulae, bathed in a soft white-gold radiance from above; {NOFIG}",
         camera="wide shot, the Earth and the radiance in the upper two-thirds, deep dark space as the calm lower third", amb="cosmos",
         transition="black"),
    dict(to=69, reason="historical example: Pharaoh and Nimrod who claimed ownership and divinity", loc="pharaoh_hall",
         visual=f"an empty gilded ancient Egyptian throne on a high stone dais in a vast columned hall, dust floating in the dusky light, pyramids silhouetted through the opening beyond; {NOFIG}, no faces, no inscriptions",
         camera="wide shot, low angle, the empty throne and pyramids in the upper two-thirds, the stone floor as the calm lower third", amb="memory",
         transition="dissolve", sens="other", safe="rule 4: Pharaoh and Nimrod never shown — only an empty throne and pyramids at dusk"),
    dict(to=71, reason="scene change: today's proud claimants — 'my land, my decision, my world'", chars=["powerful_man"], loc="penthouse",
         visual="the powerful man standing at the glass railing of the penthouse terrace, one arm sweeping out possessively over the vast city and coastline below, chin raised, a proud possessive look",
         camera="medium wide, slightly low angle, his face and the skyline in the upper two-thirds, the terrace floor as the calm lower third", amb="city_day",
         transition="dissolve"),
    dict(to=74, reason="new metaphor: this world is an exam hall — when it ends every paper is collected", loc="exam_hall",
         visual="rows of single wooden desks set far apart in the quiet hall, students in white school uniforms seen from behind with heads bowed over their blank papers, a male invigilator in a white shirt standing silently at the front holding a neat stack of collected blank papers; nothing written anywhere, no clock face",
         camera="wide shot from the back of the hall, the rows and invigilator in the upper two-thirds, the tiled floor as the calm lower third", amb="exam_hall"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The first verse of Surat al-Fatiha proclaims majesty: the Lord of the worlds. This phrase alone is enough to make hearts tremble with awe.")
sh(2, "The Lord of endless worlds, of everything that can be seen and of all that is unseen.")
sh(3, "Before such majesty, a human being feels his own smallness. At times he may even feel fear.")
sh(4, "At that very moment, the second verse changes this. \"Ar-Rahmanir-Raheem\" — after majesty, now comes mercy.")
sh(5, "This did not happen by chance. It is an order founded on great wisdom. For Allah nurtures His servants by drawing them near to Him.")
sh(6, "When you say \"Rabb\", what you feel is power. But when you say \"Rahman\", what you feel is tenderness.")
sh(7, "Think of a mother's tenderness. However exhausted she is, she wakes from deep sleep,",
   [("cloth_rustle", "ހޭލައި", -24)])
sh(8, "and lays her hand on the forehead of her sick child. Perhaps the child falls asleep. Perhaps not.")
sh(9, "But that mother will not leave her child. If you have felt this tenderness, you will understand what is being said. Now,",
   hum=True)
sh(10, "gather together the tenderness in the hearts of all the mothers in every corner of the world, every tear those mothers shed,")
sh(11, "every night that robbed them of sleep, every sacrifice they make. Even that mountain of sublime tenderness,")
sh(12, "compared with Allah's mercy, is not even the measure of a single drop of water. One day, as the Messenger of Allah ﷺ was walking with his companions, he saw a woman among a large crowd searching for her lost child.")
sh(13, "When at last she found her child, she hugged him very tightly and pressed him to her breast.",
   [("cloth_rustle", "ބައްދާލައި", -24)])
sh(14, "The Messenger of Allah ﷺ turned to his companions and asked: \"Would this woman throw her child into the fire?\"")
sh(15, "They replied: \"No, O Messenger of Allah! As long as she has the power to prevent it, she would never do such a thing.\"")
sh(16, "He said: \"Truly, Allah is more merciful to His servants than this woman is to her child.\"", hum=True)
sh(17, "Reflect on this. Why does a human heart grow hard? Because he feels that he is alone.")
sh(18, "Because he thinks he lives in a world without mercy. Because he sees what befalls him in life as nothing but torment.")
sh(19, "Yet at the very start of Surat al-Fatiha, mercy is recalled twice. First in \"Bismillah\". And then again, after the first verse.")
sh(20, "There is a secret in this repetition. Right after revealing that Allah is the Lord of the worlds, it at once reminds us that He is Ar-Rahmanir-Raheem.")
sh(21, "Majesty and power are balanced here by mercy. Had there been only majesty, man would have despaired. Had there been only mercy,")
sh(22, "man would have grown careless and lost all seriousness. Surat al-Fatiha builds a perfect balance: hope and fear, tenderness and responsibility, nearness and awe.")
sh(23, "Now look at your own life. Think about the hardships you have faced. Perhaps it was losing something.")
sh(24, "Or an illness, or loneliness. In those moments, how did you see Allah?")
sh(25, "Only as a God who tests? Or as a God who shows mercy? Surat al-Fatiha teaches")
sh(26, "that even that hardship may itself be a mercy. For Allah, the Rahman, encompasses everything, and Allah, the Raheem, will not let the believing servant be lost in this world.",
   hum=True)
sh(27, "Let us reflect more deeply still. When mercy is mentioned twice, why is power not mentioned twice?")
sh(28, "Because what man needs most of all is mercy. People make mistakes. They grow weak. They forget. That is why,")
sh(29, "when the Quran begins, there is mercy instead of a warning. This is how a mother speaks to her child: first she embraces him with tenderness, then she advises and warns.")
sh(30, "Beyond this, there is a great secret here. The word \"rahma\" is derived from \"rahim\". It is also the name for a mother's womb.")
sh(31, "Just as the womb keeps the child within it safe, cares for it and shields it from the dangers of the outside world, Allah's mercy surrounds His servants.",
   hum=True)
sh(32, "But this mercy is not only tenderness; it is also a reality. It is what builds a human being, shapes him and prepares him.")
sh(33, "For, as the next verse will show, behind this mercy lies accountability. But before accountability,")
sh(34, "mercy is sprinkled into hearts twice. This is a very deliberate preparation. Because right after it comes the fourth verse.",
   [("rain_start", "ބީހިލައެވެ", -26)])
sh(35, "The Day of Resurrection: \"Maaliki yawmid-deen\" means the Master of the Day of Reckoning, the Day of Recompense.", hum=True)
sh(36, "It is a day of awe, yet a day on which hope is not cut off. A day of accountability, yet not a day of panic and despair.")
sh(37, "Do not forget that there will be a reckoning. But do not forget Allah's mercy either.")
sh(38, "Picture a scene from this world. In the world there are the powerful, the wealthy, people with influence and fame.")
sh(39, "They do whatever they wish. Every word they say is carried out. As the years pass, the feeling 'I can do anything I want' settles in their souls.")
sh(40, "Arrogance grows in the heart. But for all that power and influence, on the Day of Resurrection that person will stand utterly alone.")
sh(41, "On that Day there will be no lawyer. Money will be worth nothing. Connections and power will be of no use.")
sh(42, "Fame and rank will be wiped away. Allah knows everything they did and everything they said, even the deeds they did in secret where no one could see.",
   [("wind_gust", "ފޮހެވިގެންދާނެއެވެ", -22)])
sh(43, "In Surat an-Naba', Allah describes the awe of that Day. The angels will stand in rows. Jibreel, too, will be there.", hum=True)
sh(44, "No one will have the power to speak a single word without Allah's permission. And in Surat al-Infitar it is said")
sh(45, "that it is the Day on which no soul will have the power to do anything at all for another soul.")
sh(46, "On that Day, all command belongs to Allah alone. Consider the situation today. In Muslim lands there are the powerful.")
sh(47, "Innocent people and small children are dying. Mothers search for their children beneath the rubble of buildings.", hum=True)
sh(48, "A father's voice has gone hoarse from calling out to his little child. But those who ordered the bombing,",
   [("distant_boom", "ބޮން", -26)])
sh(49, "and those who signed for it, live as though it were their right. They think there will never be a Day when they are called to account.",
   [("pen_scribble", "ސޮއިކުރި", -22)])
sh(50, "However powerful they may appear, \"Maaliki yawmid-deen\" is there. The Master of the Day of Recompense is there. On that Day, power,")
sh(51, "influence, money and friendship will be of no benefit at all. Even the smallest injustice will be called to account.")
sh(52, "But this is not a warning for oppressors alone. It concerns all of us. How many small wrongs do we commit every day?")
sh(53, "A word that wounds someone's heart, something we see and simply ignore, a right we delay, a trust we betray,")
sh(54, "or delaying the prayer. All of these will be weighed on the scale on that Day.")
sh(55, "That is why, in Surat al-Fatiha, Allah placed these verses one right after the other: \"Ar-Rahmanir-Raheem\" and \"Maaliki yawmid-deen\".")
sh(56, "Mercy and reckoning. Hope and fear. These are the two pans of one scale, each bound to the other.")
sh(57, "Scholars call this the balance of \"khawf\" (fear) and \"rajaa'\" (hope). A believer must live between the two.")
sh(58, "If there is only fear in a person's heart, despair may arise. Despair is dangerous.")
sh(59, "And if there is only hope, carelessness may arise. Carelessness is dangerous too. But if the two are in balance,")
sh(60, "a person will neither grow weak nor lose hope. Imagine someone who committed great sins for years.")
sh(61, "On the day he wakes up, two feelings will battle in his heart. The first: \"I am ruined, I have sinned far too much, Allah will not forgive me,",
   [("sigh", "ހޭލެވޭ", -22)])
sh(62, "there is no way back.\" This is the feeling Shaytan loves. For despair drowns a person ever deeper in sin.")
sh(63, "The second: \"Allah is the Most Merciful, He will forgive every sin, I will enter Paradise however I live.\"")
sh(64, "This too is a dangerous feeling, because it makes a person forget that there will be a reckoning. The right way is to stand between the two:")
sh(65, "\"I have done many wrongs, but Allah is the Most Merciful, the Most Compassionate. The door of repentance is open.",
   [("door_open", "ދޮރުވަނީ", -22)], hum=True)
sh(66, "At the same time, He is Maaliki yawmid-deen. That Day will come. So while there is still time, I will turn back to Him.\"",
   [("footsteps_sand", "ރުޖޫޢަވާނަމެވެ", -24)], hum=True)
sh(67, "This is the lesson these two verses of Surat al-Fatiha teach. As for the word \"Maalik\": in some readings it is recited \"Malik\". Both are correct.")
sh(68, "And both words carry a deep meaning. \"Maalik\" is the Owner. \"Malik\" is the King. On that Day, Allah is the Owner of everything and the only King.")
sh(69, "In this world, human beings are a people who lay claim to ownership. Pharaoh said he was the supreme god. Nimrod disputed with Allah.")
sh(70, "In today's world too there are people full of pride and arrogance who lay claim to ownership: 'This is my land,")
sh(71, "this is my decision, this is my world' — claims that carry on as though they were the truth.")
sh(72, "But that is only in this world. For this world is an examination hall. In an examination hall the desks are set apart.")
sh(73, "Each person looks only at his own paper. The invigilator does not keep stepping in.",
   [("pen_scribble", "ކަރުދާހަށެވެ", -24)])
sh(74, "But when the exam ends, every paper will be collected.",
   [("paper_shuffle", "އަތުލެވޭނެއެވެ", -20)])
SHOTS = S

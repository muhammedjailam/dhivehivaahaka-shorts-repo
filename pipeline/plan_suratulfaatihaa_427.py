"""Beat/shot plan for Suratul Faatihaa episode 427 (used by plan_beats.py).
Part A (0-287 s): seven verses, seven waves that rebuild a life; salah and the divided prayer; the small key and the open
door. Part B (287-745 s): new chapter, the secret of Bismillah: the void before creation, the first movement, the Day and
Paradise's gates begin with Bismillah; Ism, Allah (hidden by the intensity of His light, like the sun), ar-Rahman vs
ar-Rahim; a young believer of the first generation cries "Bismillah" before two armies (companion: NEVER shown - only the
distant dust and banners and footprints, bible rules 2 and 7); Bismillah as the door to "the constitution of the universe".
Bible rules: Allah = light/sky/cosmos only; no prophet/companion figures; hereafter symbolic; no calligraphy, no text."""

COSMOS = "deep space with luminous spiral galaxies, nebulae and countless stars"
MOSQUE_HALL = ("the prayer hall of a white coral-stone Maldivian mosque with carved dark wooden pillars, a lacquered "
               "wooden ceiling, a plain mihrab niche in the qibla wall, soft woven prayer rugs in rows, warm light through "
               "arched windows")
HOME_ROOM = ("a simple tidy room of a Maldivian island home, whitewashed coral-stone walls, a wooden window with shutters "
             "open to coconut palms, a woven mat on a tiled floor, a low wooden table")
BEACH_DAWN = "a quiet palm-lined Maldivian beach with a calm turquoise lagoon at dawn"
PLAIN = "a vast empty plain under a blinding white-gold sky, fine dust drifting"
OLD_MADINAH = ("early seventh-century Madinah: a simple mosque of palm-trunk pillars with a palm-frond roof and a sandy "
               "floor, mud-brick houses, date palms")
STUDY = "a lamp-lit scholar's study with arched windows, wooden shelves of old leather-bound books and manuscripts"
ISLAND_LANE = "a sandy Maldivian island lane between coral-stone walls and coconut palms"

LOC = {
    "beach_dawn": BEACH_DAWN,
    "office": "a bright modern office in Male' with a plain wooden desk and a tall window overlooking the turquoise sea and the harbour",
    "island_wind": "the edge of a small Maldivian island facing the open lagoon, white sand, young coconut palms and a grey sky",
    "plain": PLAIN,
    "crossroads": "a sandy island path that splits into two: one way leads to a small white coral-stone mosque with a lamp-lit doorway, the other to a busy harbour-front town glittering with shop lights",
    "reef_path": "a narrow path of wet, mossy black coral stones along the edge of a reef on a Maldivian island, the sea washing in below",
    "penthouse": "a grand, cold, luxurious top-floor office of polished black marble and glass high above a city at night, a huge empty desk",
    "home_night": HOME_ROOM,
    "old_madinah": OLD_MADINAH,
    "mosque_hall": MOSQUE_HALL,
    "home_prayer": HOME_ROOM,
    "compass": "a woven prayer mat on a tiled floor beside a window of a Maldivian island home",
    "mosque_doors": "the tall, carved dark-wood double doors of a white coral-stone Maldivian mosque, on a sandy forecourt among coconut palms",
    "void": "an absolute, endless void before creation: nothing at all, no stars, no light, no objects",
    "cosmos_birth": COSMOS,
    "paradise_gates": PLAIN,
    "beach_night": "a quiet palm-lined Maldivian beach at night, the calm lagoon reflecting the sky",
    "reef_shore": "a rocky reef shore of a Maldivian island: black coral rocks, foaming surf and tall coconut palms",
    "names_light": "the open sky above a calm endless ocean, no land in sight",
    "beach_noon": "a white-sand Maldivian beach at midday with a dazzling turquoise lagoon and coconut palms",
    "study": STUDY,
    "cosmos_order": COSMOS,
    "island_sunrise": "a whole small Maldivian island seen from above the lagoon: a cluster of tin-roofed coral-stone houses, a white mosque, a little harbour with dhonis, coconut palms and a ring of turquoise reef",
    "island_rain": ISLAND_LANE,
    "mosque_night": MOSQUE_HALL,
    "ocean_night": "the open Indian Ocean at night, far from any land, a small wooden Maldivian dhoni alone on the dark water",
    "lane_dawn": ISLAND_LANE,
    "desert_plain": "a wide Arabian desert plain with low rocky hills on the horizon",
    "desert_tracks": "a wide Arabian desert plain of soft wind-rippled sand",
    "jetty": "a wooden jetty on a Maldivian island where a small dhoni is moored, the open sea beyond",
    "door_cosmos": f"a vast doorway of pure light standing in the open, through which can be seen {COSMOS}",
}
MOOD = {
    "beach_dawn": "dawn, soft pink and gold sunrise light, long gentle waves catching the gold, peaceful new beginning",
    "office": "bright late morning, warm sunlight streaming through the window, humble gratitude",
    "island_wind": "stormy afternoon clearing, dark storm-grey clouds breaking open, a single strong golden sunbeam falling through, hope after hardship",
    "plain": "blinding white-gold light from above, silent, vast, awe and accountability, no shadows of people",
    "crossroads": "dusk, deep violet sky, warm amber lamplight from the mosque doorway versus cold glittering lights of the town, a moment of decision",
    "reef_path": "dusk, cool storm-grey and teal light, wet stones glistening, sudden unease",
    "penthouse": "night, cold blue city lights through the glass, harsh pools of light on gold, hollow loneliness",
    "home_night": "night, deep blue sky full of stars through the open window, one warm amber oil lamp, quiet reflection",
    "old_madinah": "early dawn, soft pale-gold light, hazy, slightly desaturated, soft vignette, reverent stillness",
    "mosque_hall": "early morning, a soft shaft of golden light through an arched window, warm amber and emerald tones, deep calm and presence",
    "home_prayer": "late night, a single warm oil lamp, deep blue shadows, honest and tender self-reflection",
    "compass": "early morning, fresh golden sunlight across the mat, clear and calm",
    "mosque_doors": "dawn, warm golden sunrise light, emerald shadows under the palms, quiet invitation",
    "void": "total darkness, the faintest deep-teal haze at the very edges, absolute silence and stillness",
    "cosmos_birth": "the first instant of creation: a blinding golden-white burst of light at the centre radiating outward, warm gold and soft rose, awe, love and mercy",
    "paradise_gates": "radiant white-gold and soft emerald light, serene, welcoming, otherworldly peace",
    "beach_night": "night, the Milky Way blazing across a deep blue sky, cool silver starlight on the sand, wonder and contemplation",
    "reef_shore": "late golden afternoon, strong wind, spray glowing in the low sun, power and majesty",
    "names_light": "dawn twilight, deep blue fading to gold, luminous threads of light, majestic and serene",
    "beach_noon": "midday, an overwhelmingly bright white sun high in the sky, glare washing out the edges of the scene, awe",
    "study": "night, warm amber lamplight, hazy, slightly desaturated, soft vignette, silver moonlight beyond the window, devotion",
    "cosmos_order": "deep blue and gold, calm cosmic order and harmony",
    "island_sunrise": "sunrise, warm golden light spilling over the whole island, every rooftop touched by the light, generous and peaceful",
    "island_rain": "soft daytime monsoon rain with sunshine breaking through, glistening wet sand, fresh green palms, gentle joy",
    "mosque_night": "late night, the hall almost dark, a single soft beam of warm golden light falling from a high arched window onto one worshipper, intimate nearness",
    "ocean_night": "night, an immense starry sky over black water, cold blue tones, smallness and humility",
    "lane_dawn": "early dawn, warm golden light glowing from the far end of the lane, blue shadows lifting, longing and welcome",
    "desert_plain": "early dawn, pale gold sky, hazy, slightly desaturated, soft vignette, tense stillness before a great moment",
    "desert_tracks": "sunrise, low golden sun ahead, long soft shadows, hazy, slightly desaturated, soft vignette, courage and release",
    "jetty": "early morning, grey sea and a clearing sky, first sunlight on the water, quiet resolve",
    "door_cosmos": "brilliant golden-white light pouring through the doorway, deep emerald-blue night around it, majestic, hopeful, infinite",
}

BEATS = [
    # ---------------- Part A: seven verses, seven waves ----------------
    dict(to=1, reason="episode opening: seven verses as seven waves that rebuild a whole life", chars=["listener"], loc="beach_dawn",
         visual="seven long gentle waves rolling one after another across the calm lagoon towards the shore, catching the gold of the sunrise; the listener stands barefoot at the water's edge in the distance, seen from behind and slightly to the side, his trousers rolled at the ankle, watching the waves come in",
         camera="wide shot, the sunrise and waves in the upper two-thirds, smooth wet sand as a calm lower third", amb="beach_day"),
    dict(to=4, reason="topic change: al-hamdu lillah - you are not the centre; success, beauty and power are not yours", chars=["listener"], loc="office",
         visual="the listener, wearing a light-blue long-sleeved office shirt, gently setting down a plain clear glass award with no engraving on his desk, turning his face up towards the warm sunlight pouring through the window with a humble, grateful expression, his free hand resting on his chest",
         camera="medium shot, eye level, his face in the upper third, the clean desk top as the calm lower third", amb="office_day"),
    dict(to=6, reason="new image: ar-Rahman ar-Rahim - hardship is training, purification and raising of rank, not punishment", loc="island_wind",
         visual="a young coconut palm bending hard in a strong wind but firmly rooted in the white sand, the storm clouds above it tearing open and a single strong golden sunbeam falling on it; no people",
         camera="wide shot, low angle, the palm and the sunbeam in the upper two-thirds, the white sand as the lower third", amb="island_day"),
    dict(to=9, reason="new image: maliki yawmid-din - the Day of Reckoning; nothing is lost, intentions are recorded", loc="plain",
         visual="a great empty two-pan balance scale made entirely of soft light standing alone in the middle of the vast plain, its two pans perfectly still and level; no people at all",
         camera="wide shot, the scale in the upper half, the dusty ground as the calm lower third", amb="vast_plain",
         transition="dissolve", sens="hereafter",
         safe="rule 5: the Day of Reckoning shown only as an empty plain and a scale of light; no crowds, no judgement scene"),
    dict(to=11, reason="new image: iyyaka na'budu - you are a servant either of Allah or of something else, no middle ground", chars=["listener"], loc="crossroads",
         visual="the listener standing exactly at the fork of the sandy path, seen from behind, pausing between the two ways: on the left the small white mosque with its warm lamp-lit doorway, on the right the glittering harbour-front town with bright shop lights (lights only, no signs)",
         camera="wide shot from behind him at eye level, the two destinations in the upper two-thirds, the sandy fork as the lower third", amb="village_night",
         transition="dissolve"),
    dict(to=12, reason="new image: ihdina - the veil of self-trust torn; even one who knows the way can slip at any moment", loc="reef_path",
         visual="close-up of a man's foot in a simple brown leather sandal and the hem of dark-grey trousers slipping on a wet mossy coral stone of the narrow path, a little spray rising from the surf below; no face visible",
         camera="close-up, low angle, the foot and stone in the upper half, dark water as the lower third", amb="beach_dusk"),
    dict(to=14, reason="new image: the true blessing is guidance, not money, rank or fame; those who knew and grew proud", chars=["powerful_man"], loc="penthouse",
         visual="the powerful man standing alone behind his huge empty desk, small neat stacks of gold coins and plain blank golden trophies around him, cold city lights behind the glass; his chin raised in pride but his eyes empty and lonely",
         camera="medium wide, eye level, his face in the upper third, the polished desk as the lower third", amb="city_night_far"),
    dict(to=18, reason="topic change: the listener asks himself what would change - complaint to praise, fear to trust, pride to humility", chars=["listener"], loc="home_night",
         visual="the listener, in a plain grey long-sleeved t-shirt, sitting cross-legged on the woven mat by the open window at night, his open palms resting on his knees, looking out at the stars with a calm, thoughtful, softly hopeful face; a small oil lamp on the low table beside him",
         camera="medium shot, eye level, his face and the starry window in the upper two-thirds, the mat as the lower third", amb="home_night"),
    dict(to=19, reason="new image: the Prophet's hadith - no prayer is valid without al-Fatiha", loc="old_madinah",
         visual="the empty early mosque of palm-trunk pillars at dawn, soft light falling through the gaps in the palm-frond roof onto the sandy floor, a single plain woven mat lying empty; no people at all",
         camera="wide shot, eye level, the pillars and light in the upper two-thirds, the sandy floor as the lower third", amb="old_madinah_day",
         transition="dissolve", sens="sacred_figure",
         safe="rule 2: the Prophet (peace be upon him) is never shown; only the empty early Madinah mosque in dawn light"),
    dict(to=22, reason="new image: al-Fatiha is the soul of the prayer - a conversation between Allah and His servant", chars=["listener"], loc="mosque_hall",
         visual="seen from directly behind, the listener standing alone in prayer on a prayer rug, his body squarely facing the plain mihrab niche straight ahead in the centre of the qibla wall, wearing his off-white kurta and a white crocheted prayer cap, right hand over left on his chest, eyes lowered, barefoot; a soft shaft of golden light from an arched window falling over him",
         camera="medium wide, from slightly behind and to the side, the mihrab and light in the upper two-thirds, the rug as the lower third", amb="mosque_interior",
         transition="dissolve"),
    dict(to=26, reason="new image: honest self-audit - did you really mean the words, or only repeat them?", chars=["listener"], loc="home_prayer",
         visual="the listener, in a plain grey long-sleeved t-shirt and a white crocheted prayer cap, sitting on a prayer mat on the floor after prayer, looking down into his own open palms with a searching, moved expression, eyes glistening; the oil lamp beside him",
         camera="medium close-up, eye level, his face in the upper third, the prayer mat as the lower third", amb="home_night"),
    dict(to=28, reason="new image: prayer resets the self five times a day; al-Fatiha straightens your compass", loc="compass",
         visual="an old brass pocket compass with a blank face (no letters, no numbers) lying open on the woven prayer mat, its needle settling steady, morning sunlight falling across it",
         camera="close-up, slightly high angle, the compass in the upper half, the mat as the lower third", amb="room_day"),
    dict(to=30, reason="new image: a key, however small, opens great doors; seven verses are the summary of the Quran", chars=["listener"], loc="mosque_doors",
         visual="close-up of the listener's open palm holding a small, simple antique brass key, the towering closed carved wooden doors of the mosque rising behind it, golden dawn light glinting on the key",
         camera="close-up, the key in the upper half against the tall doors, the sandy forecourt as the lower third", amb="mosque_dawn"),
    dict(to=31, reason="action change: the door is now open - will you only listen, or pray it truly?", chars=["listener"], loc="mosque_doors",
         visual="the great carved doors standing wide open, warm golden light pouring out across the sand; the listener stands at the threshold seen from behind, in his off-white kurta, about to step inside",
         camera="wide shot from behind him, the glowing doorway in the upper two-thirds, the sandy forecourt as the lower third", amb="mosque_dawn"),
    # ---------------- Part B: the secret of Bismillah ----------------
    dict(to=34, reason="new chapter: imagine an endless darkness before creation - no light, sound, time or space", loc="void",
         visual="a vast dark empty void before creation: deep indigo-black space filled with slow drifting veils of faint deep-teal and violet mist, a barely perceptible soft pale glow far away in the centre as if something is about to begin, perfectly still and silent; no stars, no planets, no shapes, no figures",
         camera="static, centred", amb="cosmos", transition="black"),
    dict(to=38, reason="action change: by the divine will the first movement of creation begins; mercy behind it", loc="cosmos_birth",
         visual="a single point of brilliant golden-white light bursting open in the darkness and spreading outward in soft luminous waves of gold and rose gas, the first glowing clouds and stars forming at the edges; only space and light - absolutely no people, no figures, no buildings, no books, no ground",
         camera="wide shot, the burst of light in the upper half, deep darkness easing into soft glow in the lower third", amb="cosmos",
         sens="sacred_figure", safe="rule 1: the divine will is shown only as light and the birth of the cosmos"),
    dict(to=40, reason="new image: the Day begins and the gates of Paradise open with Bismillah; the believers welcomed with mercy", loc="paradise_gates",
         visual="immense gates of pure light opening at the far end of the vast plain, beyond them glimpses of luminous green gardens, flowing rivers and palms bathed in white-gold light; no people",
         camera="wide shot, the gates and gardens in the upper two-thirds, the plain as the lower third", amb="garden_day",
         transition="dissolve", sens="hereafter",
         safe="rule 5: the Day and Paradise shown only as gates of light and distant gardens; no resurrected crowds, no figures"),
    dict(to=43, reason="new image: three words, each hiding a universe; seeing the universe as His dominion", chars=["listener"], loc="beach_night",
         visual="the listener standing small on the empty beach at night, seen from behind and slightly to the side, his head tilted back looking up in wonder at the blazing Milky Way arching over the lagoon",
         camera="wide shot, the Milky Way filling the upper two-thirds, the dark sand as the lower third", amb="beach_evening",
         transition="dissolve"),
    dict(to=45, reason="new image: behind every stone, flowing water and strong wind are His will, names and manifestations", loc="reef_shore",
         visual="foaming waves rushing and pouring over black coral rocks while tall coconut palms bend in a strong wind, spray glowing gold in the low sun; no people",
         camera="wide shot, the palms and spray in the upper two-thirds, the wet rocks as the lower third", amb="beach_day"),
    dict(to=50, reason="new image: 'Allah' - the Name in which all names gather; it cannot be translated", loc="names_light",
         visual="countless thin threads of golden light streaming in from every direction of the twilight sky and converging into a single radiant point of soft light high above the calm ocean, the sea reflecting it; no figure, no shape, no letters",
         camera="wide shot, the radiant point in the upper third, the still ocean as the lower third", amb="cosmos",
         sens="sacred_figure", safe="rule 1 and 9: the Name is never written; Allah is never depicted - only converging light"),
    dict(to=52, reason="new image: He is hidden by the very intensity of His manifestation - as we cannot look at the sun", chars=["listener"], loc="beach_noon",
         visual="the listener standing on the bright beach, raising one hand to shield his eyes as he tries to look up at the blazing white midday sun, the glare so strong it washes the sky and the edges of the scene into white light",
         camera="medium wide, low angle, the sun and his raised hand in the upper third, the bright sand as the lower third", amb="beach_day",
         sens="sacred_figure", safe="rule 1: the sun's overwhelming light as the narration's own metaphor; Allah is not depicted"),
    dict(to=55, reason="new image: the gnostics' age-old prayer - 'O You hidden by the intensity of Your appearing'", loc="study",
         visual="an old man in a long plain robe and turban seen only from behind, sitting at the arched window of the lamp-lit study, prayer beads hanging from his hand, looking out at the bright full moon; his face is not visible",
         camera="medium wide, from behind, the window and moonlight in the upper two-thirds, the wooden floor as the lower third", amb="library_night",
         transition="dissolve", sens="other", safe="rule 4: the anonymous gnostics of old are shown only from behind, no face"),
    dict(to=57, reason="new image: saying 'Allah' puts everything in its true place - the sun in its place, the stars in theirs", loc="cosmos_order",
         visual="a radiant golden sun with its planets moving on faint, perfect golden orbital arcs, a calm field of stars beyond, everything in serene order",
         camera="wide shot, the sun in the upper third, the orbits sweeping down into a calm dark lower third", amb="cosmos",
         transition="dissolve"),
    dict(to=58, reason="return: man in his place, your own self in yours - back to the listener under the stars", reuse="beat_018",
         chars=["listener"], loc="beach_night", visual="reuse of beat_018", amb="beach_evening"),
    dict(to=61, reason="new image: ar-Rahman - an all-embracing mercy flowing to everyone, in this very breath", loc="island_sunrise",
         visual="the sun rising over the whole small island, its golden light spreading over every tin roof, the white mosque, the harbour and the dhonis alike, the reef glowing turquoise around it; no close figures",
         camera="wide aerial shot, the sunrise and island in the upper two-thirds, the calm lagoon as the lower third", amb="island_day"),
    dict(to=64, reason="new image: the rain falls for everyone, the wind fills every lung - unearned, undeserved mercy", loc="island_rain",
         visual="soft sunlit rain falling on the island lane; small anonymous figures in the distance, seen from behind - an old fisherman walking calmly, a woman in a long dress and hijab fully covering her hair under an umbrella, two boys laughing with their faces turned up to the rain; palms swaying in the breeze",
         camera="wide shot, eye level, the lane and rain in the upper two-thirds, wet glistening sand as the lower third", amb="rain_day"),
    dict(to=67, reason="new image: ar-Rahim - a special, near mercy that flows deep into hearts that open to it", chars=["listener"], loc="mosque_night",
         visual="the listener, in his off-white kurta and a white crocheted prayer cap, sitting alone on a prayer rug in the dim hall, both palms raised at chest height in dua, face lifted, tears on his cheeks, a single soft beam of warm golden light falling on him alone",
         camera="medium close-up, eye level, his face and hands in the upper half, the rug as the lower third", amb="mosque_interior"),
    dict(to=69, reason="return: ar-Rahim perfected in the hereafter and in Paradise - back to the gates of light", reuse="beat_017",
         loc="paradise_gates", visual="reuse of beat_017", amb="garden_day", transition="dissolve", sens="hereafter",
         safe="rule 5: Paradise shown only as gates of light and gardens; no figures"),
    dict(to=71, reason="new image: before the Lord of infinite power you are limited, sinful, weak - yet He chose mercy", chars=["listener"], loc="ocean_night",
         visual="a tiny lone figure, the listener, sitting in the small wooden dhoni in the middle of the vast dark ocean, head bowed, under an immense sky of countless stars",
         camera="extreme wide shot, the starry sky filling the upper two-thirds, the black water as the lower third", amb="sea_boat",
         transition="dissolve"),
    dict(to=73, reason="new image: the message - come to Me with love, do not stay far, come even if you feel small", chars=["listener"], loc="lane_dawn",
         visual="the listener walking along the sandy lane towards a warm golden light glowing at its far end where a small white mosque stands, seen from behind, his steps unhurried and hopeful",
         camera="wide shot from behind, the glowing end of the lane in the upper two-thirds, the sandy lane as the lower third", amb="dawn_exterior"),
    dict(to=76, reason="historical story: a young believer of the first generation before the great power of his age; two armies face each other", loc="desert_plain",
         visual="the empty desert plain at dawn seen from a low rise: far away on the horizon two great clouds of dust with tiny indistinct banners (plain cloth, no symbols) facing each other across the sand; no people visible in the foreground, no weapons",
         camera="extreme wide shot, the two dust clouds on the horizon in the upper third, wind-rippled sand as the lower two-thirds", amb="battlefield_far",
         transition="dissolve", sens="sacred_figure",
         safe="rules 2 and 7: the companion and the man beside him are never shown, not even as silhouettes; the armies only as distant dust and plain banners; no weapons, no fighting"),
    dict(to=78, reason="action change: his fear vanishes - only the step forward remains", loc="desert_tracks",
         visual="a single line of fresh footprints in the soft wind-rippled sand leading forward towards the low rising sun, fine dust settling in golden light; no people, no figures, no shadows of people",
         camera="low angle, the footprints leading up into the sun in the upper half, the rippled sand as the lower third", amb="battlefield_far",
         sens="sacred_figure", safe="rule 2: the companion's step forward is shown only as footprints in the sand"),
    dict(to=80, reason="new image: Bismillah removes fear - 'what can I do alone?' - you are no longer alone", chars=["listener"], loc="jetty",
         visual="the listener standing at the end of the wooden jetty beside the moored dhoni, facing the grey open sea, one hand on his chest, lips softly moving, his face calm and resolved as the first sunlight breaks on the water",
         camera="medium wide, eye level, slightly from the side, his face in the upper third, the jetty planks as the lower third", amb="jetty_day",
         transition="dissolve"),
    dict(to=82, reason="closing image: Bismillah, the door to the eternal world - before you, the constitution of the universe", chars=["listener"], loc="door_cosmos",
         visual="the listener seen from behind, standing small at the threshold of the vast doorway of light, looking through it at the boundless ordered universe of galaxies and stars",
         camera="wide shot from behind, the doorway and galaxies in the upper two-thirds, a soft dark ground as the lower third", amb="cosmos"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "It is only seven verses. Yet they are seven waves that can rebuild a person's whole life. Let us return to a new beginning.",
   [("wave_crash", "އޮޅިއެވެ", -22)])
sh(2, "The very first thing Surah al-Fatiha did was to point you to Allah: \"Al-hamdu lillahi rabbil-'alamin\" (all praise belongs to the Lord of the worlds).")
sh(3, "This means you are not the centre of everything. Success is not your own. Beauty and power are not yours either.")
sh(4, "Allah is the origin of everything. These words shatter the arrogance in a person. Then the surah shows His mercy.")
sh(5, "\"Ar-Rahmanir-Rahim.\" So turn to Him not only with fear, but with hope and mercy.")
sh(6, "Not everything you face in life is a punishment. Sometimes it is training. Sometimes it is purification. Or it is a raising of rank.",
   [("wind_gust", "ތަރުބިއްޔަތެކެވެ", -24)])
sh(7, "These words wipe away despair. After that it brings a sense of responsibility: \"Maliki yawmid-din.\" There is a Day on which the reckoning will be taken.")
sh(8, "And that Day has an Owner. Nothing you did will be lost. No word you said will be forgotten.")
sh(9, "Your intentions are recorded. These words destroy heedlessness. Then it makes your tongue declare servitude and need.")
sh(10, "\"Iyyaka na'budu wa iyyaka nasta'in.\" These words wipe away the traces of shirk. Because if one is human,")
sh(11, "he becomes a servant either of Allah or of something else. There is no middle ground. Then it makes you supplicate.")
sh(12, "This tears away the veil of self-reliance. Because even when a person thinks he knows the way, his foot may slip at any moment.",
   [("gasp", "ކަހާލަފާނެތީއެވެ", -24)])
sh(13, "Then it gives an example: the true blessing is to be given the straight path. Not money. Not rank or fame. It is guidance. And finally,")
sh(14, "it warns us not to be among those who knew and became arrogant, or those who went astray in ignorance. It urges us to keep the balance.")
sh(15, "This is Surah al-Fatiha. Now let us ask ourselves: if someone truly understood this surah, what would change?")
sh(16, "Complaints would lessen and praise would increase. Fear would shrink and trust in Him would grow.",
   [("sigh", "ޝަކުވާތައް", -24)])
sh(17, "Carelessness would end and responsibility would be born. Arrogance would vanish and humility would come.")
sh(18, "Straying would stop and steadfastness would be gained. Al-Fatiha is not just something to recite. It is a foundation that builds awareness. Think about it.")
sh(19, "The validity of the prayer rests on Surah al-Fatiha. The Messenger of Allah (peace be upon him) said: \"There is no valid prayer for one who does not recite al-Fatiha.\"")
sh(20, "Why is that? Because al-Fatiha is the soul of the prayer. Prayer is not just movements. It is awareness.")
sh(21, "A prayer without al-Fatiha is like a body without a soul. A hadith qudsi says: \"I have divided the prayer (al-Fatiha) between Myself and My servant into two halves.\"")
sh(22, "That means al-Fatiha is a conversation between Allah and His servant. In every rak'ah, forty times a day.",
   [("whisper_recite", "ރަކުޢަތެއްގައި", -26)])
sh(23, "Today, ask yourself honestly: until now, have you been speaking these words with real meaning?")
sh(24, "Or have you only been repeating words? From now on, if in every rak'ah you recite with this awareness - I am praising Him, I am remembering His mercy,")
sh(25, "I am thinking about the Day of Reckoning, I am declaring my servitude, I am asking for help, I am asking for guidance,")
sh(26, "I am asking to be saved from going astray - then the prayer will change. And if the prayer changes, life will change.",
   hum=True)
sh(27, "Because the prayer is something that 'resets' your self five times a day. Through al-Fatiha, your compass is straightened forty times a day.",
   [("clock_tick", "ދުވާލަކު", -24)])
sh(28, "It reminds you of \"as-siratal-mustaqim\" forty times a day. The final truth is this.")
sh(29, "The shortness of al-Fatiha does not make it small. A key, however small, opens great doors.",
   [("box_unlock", "ހުޅުވައިދެއެވެ", -20)])
sh(30, "Though seven verses are short, they are the essence of the whole Quran. That is why it is called \"Umm al-Qur'an\" (the Mother of the Quran).")
sh(31, "Now the door is open. The question is: will you just listen and let it go? Or in your next prayer, will you recite al-Fatiha with real meaning for the first time?",
   [("door_open", "ހުޅުވިފައެވެ", -20)])
sh(32, "The Names of Allah and the secret of divine mercy: imagine yourself inside an endless darkness. There is nothing there.")
sh(33, "No light, no sound, no movement, no time, not even space. There is only perfect silence.")
sh(34, "This is the moment before the creatures were created. A moment when existence had not yet begun, when even non-existence had not been given a name. Then,")
sh(35, "with the divine will to create the universe, its first movement began. Although physicists call this the \"Big Bang\",")
sh(36, "that name only describes the reality seen from outside. Not what is within it.")
sh(37, "Because behind that decree are divine will, endless love and boundless mercy.",
   hum=True)
sh(38, "And the echo of that mercy is heard in this verse: \"Bismillahir-Rahmanir-Rahim.\" The universe began with Bismillah.")
sh(39, "The Day of Resurrection too will begin with Bismillah. The gates of Paradise too will open with Bismillah. When the believers enter Paradise, the very first they will meet,")
sh(40, "through the meaning of this verse, is Allah, glorified and exalted, with the attributes of ar-Rahman and ar-Rahim, welcoming them with endless mercy.",
   hum=True)
sh(41, "But to understand this, we must study the three words within it one by one.")
sh(42, "Because behind each of those words a separate universe lies hidden. Bismillah is the door that opens onto this reflection.")
sh(43, "To say Bismillah means to see this universe as the dominion of the Lord who owns all the Names.")
sh(44, "It means that behind everything - be it a stone, a flowing stream of water, or a strong wind -",
   [("wave_crash", "ފެންގަނޑެއް", -24), ("wind_gust", "ވަޔެއް", -22)])
sh(45, "you recognise the will, the Name and the manifestations behind it. Next comes the Name that is the root of all names, the Name in which all names gather and are completed.")
sh(46, "That is \"Allah\". This word cannot be perfectly translated from one language into another.")
sh(47, "Every time one tries, something feels missing. Even if you say \"God\" in English, that is not \"Allah\".")
sh(48, "Because other words convey only a general idea of divinity. But \"Allah\" is far above all such concepts,")
sh(49, "a proper Name belonging to Him alone. What is within this Name? Everything.")
sh(50, "The One free of every imperfection, with no opposite, no equal and no partner, described by perfect attributes.")
sh(51, "The centre to which the meaning of every creature is connected. At the same time, by the perfection and intensity of His existence, He is hidden from all things.")
sh(52, "Just as we cannot look at the sun because of its brightness, our eyes have not been given the strength to bear His light, so He cannot be seen with ordinary eyes.")
sh(53, "There is a prayer the gnostics have recited for ages: \"O You who are hidden by the intensity of Your appearing!")
sh(54, "O You who are veiled by the perfection of Your light!\" We cannot see Him because He is so very clearly manifest.")
sh(55, "We cannot fully know Him because He is far above our understanding. And this inability to know is not a weakness.")
sh(56, "For one who speaks this Name sincerely, that very inability to know is itself knowledge. With saying \"Allah\", the whole universe changes.",
   hum=True)
sh(57, "Because to say that Name means to put everything in its true place. The sun in its place. The stars in their place.")
sh(58, "Man in his place. And your own self in its place. After that come two Names, one joined to the other,")
sh(59, "each completing the other: \"ar-Rahman\" and \"ar-Rahim\". Both of these Names come from the root meaning \"mercy\" (rahmah).")
sh(60, "But between these two Names there is a very deep and important difference. Ar-Rahman is an endless mercy that embraces everything. It is the mercy that, in this world,")
sh(61, "at this moment, in this very breath, flows to believers and disbelievers, to those who do good,")
sh(62, "and to those who do evil alike. The sun rises for everyone. The rain falls for everyone.",
   [("rain_start", "ވާރޭ", -22)])
sh(63, "And the wind fills the lungs of every person. This is the manifestation of the attribute of ar-Rahman.",
   [("breath", "ފުއްޕާމޭވެސް", -24)])
sh(64, "It is not something anyone earns by himself. Nor is it something anyone deserves.")
sh(65, "It is a mercy that flows purely from endless generosity. \"Ar-Rahim\" is a special mercy. It is far more focused,")
sh(66, "a much nearer mercy. It is not something found only in the ordinary sense. Rather, that mercy flows deeply upon those who open their hearts longing for it.",
   hum=True)
sh(67, "It is a special nearness for those who believe, those who strive, and those who devote themselves to Him.")
sh(68, "It is a mercy that will appear in the hereafter after this world, and be perfected in Paradise. And so,")
sh(69, "while everyone is included in \"ar-Rahman\", \"ar-Rahim\" is a deeper, more personal and nearer attribute. Now reflect.")
sh(70, "Before the Lord of infinite power, the Creator of everything, the Owner of everything, you are in a very limited state - as one who sins,")
sh(71, "who is imperfect and weak. Yet the first two attributes that the Lord of such infinite power chose to introduce Himself to you with were mercy,")
sh(72, "and again mercy. This is no coincidence. This is a message: when you draw near to Me, come with love. Do not stay far away.",
   [("footsteps_sand", "އަންނާށެވެ", -24)], hum=True)
sh(73, "Come even if you feel your own smallness. My mercy will raise your rank. The nearer you come, the more your spirit will grow.",
   hum=True)
sh(74, "A day from history. A young man of the first generation of Islam stood before the great power of his age. Two armies, two worlds,",
   [("wind_gust", "ލަޝްކަރާއި", -24)])
sh(75, "two ways of thinking faced each other. As he mounted, he cried out loud: \"Bismillah!\"")
sh(76, "A man standing beside him might perhaps have smiled. He might have wondered what difference a single word could make.")
sh(77, "But that young man knew it was not just a battle cry. It was a declaration of accepting his own helplessness and leaning on the Lord of infinite power.")
sh(78, "With that declaration his fear left him. His hesitation vanished. All that remained was movement - a step taken forward.",
   [("footsteps_sand", "ފިޔަވަޅެވެ", -22)], hum=True)
sh(79, "Saying Bismillah removes fear. Because fear is born of the question: \"What can I do alone?\"",
   [("heartbeat", "ބިރުވެރިކަން", -22)])
sh(80, "Saying Bismillah cancels that question. You are no longer alone. And so it is no longer a problem.")
sh(81, "And Surah al-Fatiha begins with this powerful opening. With Bismillah. With a declaration of mercy. With the door to the eternal world.",
   [("door_open", "ދޮރުކޮޅާއެކުގައެވެ", -22)])
sh(82, "And once you enter through this door, what lies before you is not just the text of an ordinary prayer. What lies before you is the constitution of the entire universe.",
   hum=True)
SHOTS = S

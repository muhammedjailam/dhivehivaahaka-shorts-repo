"""Beat/shot plan for Suratul Faatihaa episode 422 (used by plan_beats.py).
Opening episode: Al-Fatiha as a key to the secrets of the universe; the veil of habit; virtues of the surah (Hadith
Qudsi of the divided prayer, Iblis wailing, the key and the iron door, Abu Sa'id ibn al-Mu'alla); Verse 1 in depth
(hamd, Rabb, 'alamin); the Prophet's night prayer; counting blessings; cliffhanger on Ar-Rahman ar-Rahim.
Bible rules: no prophet/companion/angel/Iblis figure (empty places, light, smoke only), Ibn Arabi only from behind, no
letters on any mushaf or anywhere, hijab fully covering hair and neck, prayer shown correctly."""

MOSQUE_HALL = ("the prayer hall of a white coral-stone Maldivian mosque with carved dark wooden pillars, a lacquered "
               "wooden ceiling, a plain mihrab niche in the qibla wall, soft woven prayer rugs in rows, warm light "
               "through arched windows")
HOME_ROOM = ("a simple tidy room of a Maldivian island home, whitewashed coral-stone walls, a wooden window with shutters "
             "open to coconut palms, a woven mat on a tiled floor, a low wooden table")
STUDY = ("a lamp-lit scholar's study with arched windows, wooden shelves of old leather-bound books and manuscripts")
OLD_MADINAH = ("early seventh-century Madinah: a simple mosque of palm-trunk pillars with a palm-frond roof and a sandy "
               "floor, mud-brick houses, date palms")
GARDEN = ("a small walled garden of a Maldivian island home, hibiscus and frangipani bushes beneath tall coconut palms, "
          "a low whitewashed coral-stone wall")
HIST = "hazy, slightly desaturated, soft vignette"

LOC = {
    "cosmos": "deep space with luminous spiral galaxies, nebulae and countless stars",
    "mosque_hall": MOSQUE_HALL,
    "mosque_hall_night": MOSQUE_HALL,
    "mosque_hall_dawn": MOSQUE_HALL,
    "study": STUDY,
    "study_candle": STUDY,
    "home_room": HOME_ROOM,
    "home_room_night": HOME_ROOM,
    "home_curtain": HOME_ROOM,
    "beach_dawn": "a quiet palm-lined Maldivian beach with a calm turquoise lagoon at dawn",
    "garden": GARDEN,
    "garden_dusk": GARDEN,
    "mosque_ext_night": ("a small white coral-stone Maldivian mosque with a simple white dome and a short minaret on a "
                         "quiet island, coconut palms around it, a sandy courtyard"),
    "storm_dawn": "a wide sky of dark storm clouds above a calm Maldivian lagoon and a line of palm islands",
    "vault": "the threshold of a vast dim stone hall with a huge heavy riveted iron door set in a massive stone arch",
    "old_madinah": OLD_MADINAH,
    "old_madinah_night": OLD_MADINAH,
    "sea_boat": "a small traditional wooden Maldivian dhoni fishing boat drawn up on a white-sand island shore, fishing nets",
    "jetty": "a long weathered wooden jetty stretching out over a calm Maldivian lagoon",
    "atoll": ("a Maldivian atoll seen from high above: a ring of small palm-covered islands in a vast turquoise lagoon "
              "edged by deep blue ocean"),
    "gallery": "a quiet airy art gallery with whitewashed walls, pointed-arch windows and a few large framed landscape paintings",
    "sand_palms": "a sunlit patch of white sand beneath tall coconut palms on a Maldivian island",
    "worlds": ("a layered vision of creation: a still Maldivian lagoon at the very bottom, a soft veil of drifting mist "
               "above it, and beyond the mist a vast luminous horizon"),
    "island_lane": "a sandy Maldivian island lane between coral-stone walls and coconut palms",
    "lagoon_rain": "a Maldivian island lagoon fringed with coconut palms and a white-sand beach",
}
MOOD = {
    "cosmos": "timeless night of space, deep indigo and emerald nebulae, warm gold starlight, awe and wonder",
    "mosque_hall": "late afternoon, warm golden light through the arched windows, soft emerald shadows, quiet devotion",
    "mosque_hall_night": "night, warm amber lamps, deep teal shadows, a soft beam of white-gold light from above, intimate and sacred",
    "mosque_hall_dawn": "dawn, the first soft gold light through the arched windows, emerald shadows, serene and hopeful",
    "study": f"night, a single warm oil lamp, amber glow against deep teal shadows, {HIST}",
    "study_candle": f"night, warm candlelight and gold reflections, deep emerald shadows, {HIST}, reverent",
    "home_room": "early morning, soft golden sunlight through the open shutters, gentle teal shadows, tender and peaceful",
    "home_room_night": "late night, the room dark blue, only a cold faint glow from below on a face, empty and restless",
    "home_curtain": "dim interior in daytime, heavy shadow, a thin bright blade of golden light at the edge of a curtain, quiet anticipation",
    "beach_dawn": "dawn, the sun just breaking the horizon, gold and rose light over the turquoise water, overwhelming awe",
    "garden": "fresh early morning, soft gold light, dew drops sparkling, tender wonder",
    "garden_dusk": "dusk, violet and gold sky, the first bright star, calm wonder",
    "mosque_ext_night": "deep blue night with countless stars, warm lamplight in the arched windows, a faint luminous column of soft white-gold light rising from the mosque to the stars, sacred stillness",
    "storm_dawn": "storm-grey and charcoal clouds torn apart by a burst of golden dawn light, dramatic and symbolic",
    "vault": "dim cool stone darkness, a flood of golden light and starlight pouring through the opening door, revelation",
    "old_madinah": f"bright morning, soft shafts of sunlight through the palm-frond roof, {HIST}, peaceful and anticipatory",
    "old_madinah_night": f"night, silver moonlight through a small window, one small oil lamp, {HIST}, deep devotion",
    "sea_boat": "golden hour, warm low sun, long soft shadows on the sand, contentment and gratitude",
    "jetty": "overcast dusk, cool storm-grey sky with one thin break of gold on the horizon, quiet heaviness",
    "atoll": "golden hour, sun rays slanting through scattered clouds, glittering turquoise water, majestic beauty",
    "gallery": "soft bright daylight through the arched windows, calm and contemplative",
    "sand_palms": "morning sun with a light shower of sparkling rain drops, gold and green, nurturing care",
    "worlds": "twilight blue below rising into a blinding white-gold glow above, mysterious and vast, reverent",
    "island_lane": "late-afternoon golden hour, warm light and soft palm shadows on the sand, contentment",
    "lagoon_rain": "golden late afternoon with a gentle sun-shower, a soft double rainbow, mercy and hope",
}

BEATS = [
    dict(to=1, reason="opening image: Al-Fatiha as the key that opens the secrets of the universe", loc="cosmos",
         visual="a small ornate antique golden key with subtle Islamic geometric filigree floating and glowing in the "
                "foreground; behind it a vast pointed-arch doorway of light opening onto spiral galaxies and nebulae",
         camera="medium close-up on the key in the upper half, the cosmos receding behind, dark calm space as the lower third",
         amb="cosmos", hum=True),
    dict(to=3, reason="scene change: the surah in daily life - every prayer begins with it", chars=["listener"],
         loc="mosque_hall",
         visual="the listener standing alone in prayer on a woven prayer rug, wearing a white crocheted prayer cap, "
                "hands folded on his chest, eyes lowered, facing the plain mihrab niche; seen from the side and slightly behind",
         camera="medium wide, eye level, from the side and slightly behind", amb="mosque_interior"),
    dict(to=7, reason="new figure: Ibn Arabi's testimony and the book's method (hadith and tafsir)", loc="study",
         visual="an old scholar in a loose dark robe and white turban seen only from behind, seated at a low wooden desk "
                "by an arched window, a single oil lamp, stacks of closed leather-bound books and rolled manuscripts "
                "around him; his face is never visible",
         camera="medium wide, from behind the scholar's shoulder, the lamp and window in the upper half",
         amb="library_night", transition="dissolve", sens="other",
         safe="bible rule 4: a revered scholar is shown only from behind, no face"),
    dict(to=10, reason="topic change: the darkness of hearts - reciting 40 times a day without reflecting",
         chars=["listener"], loc="home_room_night",
         visual="the listener in a plain grey t-shirt sitting on the woven mat in his dark room late at night, slumped "
                "against the wall, his face lit faintly cold blue from a phone held low in his hand (the screen faces "
                "away from the viewer), eyes empty and tired, the dark window behind him",
         camera="medium shot, eye level, slightly from the side", amb="room_night", transition="black"),
    dict(to=11, reason="new metaphor: habit is the thickest curtain hiding reality", loc="home_curtain",
         visual="a heavy floor-length emerald-green curtain drawn across a tall window in a dim whitewashed room, a thin "
                "blade of brilliant golden light escaping at its edge and falling across the tiled floor; no people",
         camera="medium wide, eye level, the curtain filling the upper two-thirds", amb="room_day"),
    dict(to=12, reason="new example: a man seeing the sunrise for the first time falls to the ground in awe",
         chars=["listener"], loc="beach_dawn",
         visual="the listener seen from behind and slightly to the side, sinking to his knees on the white sand at the "
                "water's edge, one hand pressed to his chest, gazing at the sun breaking over the horizon, golden rays "
                "spreading across the sky and the lagoon",
         camera="wide shot, low angle from behind, sun and sky in the upper half, wet sand as calm lower third",
         amb="dawn_exterior", hum=True),
    dict(to=13, reason="new example: smelling a flower for the first time - tears of joy", chars=["listener"], loc="garden",
         visual="close-up of the listener's face in profile as he holds a fresh white-and-yellow frangipani flower to "
                "his nose with both hands, eyes closed, a single tear of joy on his cheek, dew on the petals",
         camera="close-up, profile, face in the upper half, soft blurred garden below", amb="garden_day"),
    dict(to=14, reason="return: the surah read every day out of habit (reuse the listener at prayer)", loc="mosque_hall",
         chars=["listener"], reuse="beat_002", visual="(reuse) the listener at prayer", amb="mosque_interior"),
    dict(to=16, reason="new section: virtues - no surah like it in the Torah or Injil; Umm al-Qur'an", loc="study_candle",
         visual="a closed mushaf with a deep emerald and gold ornamented cover resting on a carved wooden rehal, softly "
                "glowing; behind it on a dark wooden shelf, ancient rolled scrolls and old codices in candlelight; no "
                "letters or writing anywhere",
         camera="medium close-up, slightly low angle, the mushaf in the upper half", amb="library_night",
         transition="black", sens="other", safe="rule 9: mushaf closed, no letters; earlier scriptures only as plain scrolls"),
    dict(to=19, reason="new image: Hadith Qudsi - the prayer divided between Allah and His servant; you are not alone",
         chars=["listener"], loc="mosque_hall_night",
         visual="the listener alone in the dim mosque at night, wearing a white crocheted prayer cap, standing in prayer "
                "on a woven rug, while a soft column of white-gold light descends from high above and gently surrounds "
                "him; only light, no figure in the light",
         camera="wide shot from behind and above, the beam of light in the upper half, the rows of empty rugs below",
         amb="mosque_interior", sens="sacred_figure", safe="rule 1: Allah's answer shown only as light from above",
         hum=True),
    dict(to=23, reason="new image: the dialogue between heaven and earth as each verse is recited", loc="mosque_ext_night",
         visual="a small white coral-stone island mosque at night seen from the sandy courtyard, warm light in its "
                "arched windows, a faint luminous column of soft light rising from its dome into a sky full of stars and "
                "the Milky Way; no people",
         camera="wide establishing shot, low angle, mosque and sky in the upper two-thirds, sand as calm lower third",
         amb="island_night", hum=True),
    dict(to=26, reason="new story: Iblis wailed four times - the last when Al-Fatiha was revealed", loc="storm_dawn",
         visual="a mass of dark swirling smoke and storm clouds recoiling and shrinking away from a powerful burst of "
                "golden dawn light breaking through the sky over the lagoon; no creature, no face, no figure",
         camera="wide shot, the clash of smoke and light in the upper two-thirds, dark still water below",
         amb="storm_night", transition="dissolve", sens="sacred_figure",
         safe="rule 3: Iblis never shown - only smoke and storm clouds fleeing the dawn light"),
    dict(to=28, reason="new metaphor: a 20-gram key opens a 200-kilo iron door", loc="vault",
         visual="in the foreground a man's open palm (off-white kurta sleeve) holding a small brass key; behind, a huge "
                "heavy riveted iron door in a massive stone arch swinging open, golden light and stars pouring through",
         camera="over-the-hand shot, the key and the door's bright opening in the upper half, dark stone floor below",
         amb="memory", transition="dissolve"),
    dict(to=30, reason="new topic: no prayer without Al-Fatiha - the pillar of religion", loc="mosque_hall",
         visual="rows of men in white and pale kurtas and prayer caps standing shoulder to shoulder in straight rows "
                "facing the plain mihrab, seen from behind, beside a massive carved dark wooden pillar glowing in "
                "golden light",
         camera="wide shot from the back of the hall, the pillar in the upper left, the rows in the middle, rugs below",
         amb="mosque_interior"),
    dict(to=32, reason="historical story: the Prophet promises Abu Sa'id ibn al-Mu'alla the greatest surah", loc="old_madinah",
         visual="the empty interior of the early mosque of Madinah: rough palm-trunk pillars, a palm-frond roof letting "
                "shafts of morning sunlight fall onto the sandy floor, a simple woven mat, a doorway glowing with light; "
                "no people, no figures, no silhouettes",
         camera="wide shot, eye level, the light shafts in the upper half, the sandy floor as calm lower third",
         amb="old_madinah_day", transition="dissolve", sens="sacred_figure",
         safe="rule 2: the Prophet and the companion are never shown - only the empty early mosque"),
    dict(to=34, reason="action change: the companion hurries after the Prophet - 'It is Al-Fatiha'", loc="old_madinah",
         visual="close-up of a pair of simple worn leather sandals left at the threshold of the palm-trunk mosque, fresh "
                "footprints in the sand leading through a sunlit doorway glowing with soft light; no people",
         camera="low close-up at ground level, the bright doorway in the upper half, sand in the lower third",
         amb="old_madinah_day", sens="sacred_figure", safe="rule 2: only sandals, footprints and a doorway of light",
         hum=True),
    dict(to=36, reason="new chapter: the secret of hamd - the Qur'an opens with praise, not a warning",
         loc="mosque_hall_dawn",
         visual="a closed mushaf with an emerald and gold cover on a carved wooden rehal on a prayer rug beneath an "
                "arched window, the first golden rays of dawn falling across it; no letters anywhere",
         camera="medium shot, slightly low, the mushaf and window light in the upper half", amb="mosque_dawn",
         transition="dissolve", sens="other", safe="rule 9: the mushaf is closed, no letters"),
    dict(to=40, reason="new image: Alhamdulillah - the declaration that sets the direction of the whole universe",
         loc="cosmos",
         visual="countless spiral galaxies and streams of stars all turning and flowing towards one radiant soft "
                "golden light at the centre of the sky, like a vast cosmic compass rose with faint golden geometric "
                "lines filling the entire frame from top to bottom; pure deep space only - no people, no human figures, no ground, no buildings, no figure in the light",
         camera="wide shot, the central light in the upper third", amb="cosmos", sens="sacred_figure",
         safe="rule 1: only light, no form"),
    dict(to=42, reason="new example: praise in wealth and poverty, health and sickness - the poor but grateful",
         chars=["elder"], loc="sea_boat",
         visual="the old fisherman sitting on the edge of his small worn wooden dhoni on the sand, a mended fishing net "
                "across his knees, palms lifted at chest height in quiet gratitude, eyes closed with a peaceful smile",
         camera="medium wide, eye level, him and the boat in the upper two-thirds, sand below", amb="beach_dusk"),
    dict(to=45, reason="new image: 'O my Lord, in every state I accept Your decisions' - contentment in dua",
         chars=["listener"], loc="home_room",
         visual="the listener sitting on a prayer mat by the open wooden window at dawn, wearing a white crocheted "
                "prayer cap, both palms raised at chest height in dua, eyes closed, a calm surrendered expression, "
                "golden light on his face",
         camera="medium shot, eye level, slightly from the side, window light in the upper half", amb="home_day"),
    dict(to=47, reason="new example: losing a job, a loved one, falling ill - the hard test of saying Alhamdulillah",
         chars=["listener"], loc="jetty",
         visual="the listener in a pale office shirt and dark trousers sitting alone at the end of a long wooden jetty "
                "at dusk, a cardboard box of office things beside him, shoulders low, looking out over the grey water "
                "towards a thin break of gold on the horizon",
         camera="wide shot from behind and to the side, sky and horizon in the upper half, still water below",
         amb="jetty_day", hum=True),
    dict(to=49, reason="return: praise before you ask (reuse the dua at dawn)", chars=["listener"], loc="home_room",
         reuse="beat_020", visual="(reuse) the listener in dua at dawn", amb="home_day"),
    dict(to=50, reason="new image: 'Al-' - all praise, all beauty and every perfection belong to Allah", loc="atoll",
         visual="a breathtaking aerial view of a Maldivian atoll at golden hour, a ring of small palm islands in a vast "
                "glittering turquoise lagoon, golden sun rays slanting through clouds, a flock of white birds",
         camera="high aerial wide shot, the sky and rays in the upper third", amb="island_day"),
    dict(to=52, reason="new example: praising a painting is really praising the painter", loc="gallery",
         visual="a man in a modest long-sleeved shirt seen from behind, standing quietly before a large framed painting "
                "of a golden Maldivian lagoon at sunset; beside it a wooden easel with brushes and a paint palette, the "
                "painter nowhere in sight",
         camera="medium wide from behind, the painting in the upper half, the plain floor below", amb="gallery"),
    dict(to=54, reason="new image: the universe as a masterpiece - from the atom to galaxies, the eye, the heart, cells",
         loc="cosmos",
         visual="a luminous human eye's iris seen in extreme close-up seamlessly becoming a spiral galaxy, with tiny "
                "glowing atom orbitals and soft translucent cells drifting around it like stars, filling the entire frame; pure abstract cosmic macro image - no people, no human figures, no ground, no buildings",
         camera="extreme close-up morphing into a wide cosmic view, the iris-galaxy in the upper half", amb="cosmos",
         hum=True),
    dict(to=57, reason="new image: Rabb - the One who creates, sustains, raises and nurtures", loc="sand_palms",
         visual="a young coconut palm seedling sprouting from a brown coconut in the white sand, its fresh green leaves "
                "catching a ray of golden sunlight and a few sparkling drops of light rain, tall palms behind; nature only - no people, no hands, no human figures",
         camera="low close-up at ground level, the seedling and light in the upper two-thirds", amb="garden_day"),
    dict(to=58, reason="characters change: shaped in the mother's womb, raised as a child, given every breath",
         chars=["mother", "son"], loc="home_room",
         visual="the mother kneeling on the woven mat by the sunlit window, gently holding her little son close, the "
                "boy smiling up at her, her face full of tender love, morning light on them both",
         camera="medium shot, eye level, faces in the upper half", amb="home_day", hum=True),
    dict(to=59, reason="new image: 'alam = a sign pointing beyond itself - a flower, a star", loc="garden_dusk",
         visual="a single red hibiscus flower in full bloom in the foreground at dusk, and high above the coconut palms "
                "one brilliant star shining in a violet-gold sky",
         camera="close-up of the flower in the lower-middle, the star in the upper third", amb="beach_dusk"),
    dict(to=60, reason="return: a human face and a little child's smile as signs (reuse mother and son)",
         chars=["mother", "son"], loc="home_room", reuse="beat_027", visual="(reuse) mother and son", amb="home_day"),
    dict(to=63, reason="new image: the seen and unseen worlds - angels, jinn, the grave and barzakh, the hereafter",
         loc="worlds",
         visual="a layered vision: a still turquoise lagoon and palm island at the bottom, above it a drifting veil of "
                "mist, beyond it rows of tall soft pillars of light, and at the top an immense blinding white-gold "
                "horizon; no beings, no figures, no faces",
         camera="vertical wide shot rising from the lagoon to the glowing horizon", amb="vast_plain",
         transition="dissolve", sens="hereafter",
         safe="rules 2, 3, 5: angels as pillars of light, the unseen and hereafter as mist and a white-gold horizon; no beings"),
    dict(to=64, reason="return: you recite it forty times a day - have you asked why? (reuse the listener at prayer)",
         chars=["listener"], loc="mosque_hall", reuse="beat_002", visual="(reuse) the listener at prayer",
         amb="mosque_interior", transition="dissolve"),
    dict(to=68, reason="historical: the Prophet stood in night prayer until his feet swelled - 'Shall I not be a grateful servant?'",
         loc="old_madinah_night",
         visual="a simple mud-brick room in early Madinah at night, an empty woven prayer mat on the sandy floor lit by "
                "silver moonlight from a small window, a small clay oil lamp burning low beside it, date palms against "
                "the starry sky outside; nobody present",
         camera="medium wide, low angle, the moonlit window in the upper half, the mat below", amb="desert_night",
         transition="dissolve", sens="sacred_figure", safe="rule 2: the Prophet is never shown - only an empty mat in moonlight",
         hum=True),
    dict(to=70, reason="new image: the forgotten miracles - sight, hearing, every heartbeat", chars=["listener"],
         loc="home_room",
         visual="close-up of the listener's face in soft morning light, eyes just opening in wonder, one hand resting "
                "over his heart, the light catching his eyes",
         camera="close-up, face in the upper half, the hand at mid-frame", amb="room_day", transition="dissolve"),
    dict(to=72, reason="return: the veil of habituation that hamd tears away (reuse the curtain)", loc="home_curtain",
         reuse="beat_005", visual="(reuse) the curtain with golden light", amb="room_day"),
    dict(to=74, reason="new image: count today's blessings - breath, water, mind, faith, family, food, shelter, time",
         loc="home_room",
         visual="a still life on a low wooden table by the open window: a clear glass of water, a plate of rice with "
                "fish curry, a few ripe bananas, a closed small mushaf with a plain cover, a small wooden hourglass and "
                "a family's teacups, palm shade and golden morning light falling across them; no people",
         camera="medium close-up, table top in the middle, window and palms in the upper third", amb="home_day"),
    dict(to=76, reason="new image: begin with praise instead of complaint - a grateful heart", chars=["listener"],
         loc="island_lane",
         visual="the listener walking calmly down the sandy island lane in golden late-afternoon light, a gentle "
                "content smile, one hand resting on his chest, palm shadows across the path",
         camera="medium wide, eye level, slightly in front of him, the lane receding behind", amb="island_day"),
    dict(to=78, reason="cliffhanger: Ar-Rahman ar-Rahim - why is mercy repeated, twice, in the middle?", loc="lagoon_rain",
         visual="a gentle golden sun-shower falling over a calm turquoise lagoon and a palm island, two soft rainbows "
                "arching one above the other across the sky, raindrops sparkling on the water; no people",
         camera="wide shot, the double rainbow in the upper half, still water below", amb="rain_day",
         transition="dissolve", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "This is not merely a commentary on Surat al-Fatiha; it is a key that opens the secrets of the whole universe. The Noble Qur'an begins with Surat al-Fatiha.")
sh(2, "The prayer begins with Surat al-Fatiha. And many supplications are concluded with this surah. It is recited beside the sick.",
   [("whisper_recite", "ނަމާދު", -26)])
sh(3, "And when someone passes away, this surah is recited too. This may sometimes seem surprising.")
sh(4, "But the reason behind it is truly astonishing. Ibn Arabi said:")
sh(5, "\"For every other thing I ask of Allah, I recite only Surat al-Fatiha, and my request is answered.\" But why is that?")
sh(6, "Why is this surah, which we recite so many times every day, so special? In this book,")
sh(7, "in the light of the hadiths of the Messenger (peace be upon him) and trusted books of tafsir, we will look at what Surat al-Fatiha truly tells us.",
   [("page_turn", "ފޮތްތަކުގެ", -24)])
sh(8, "Why is Surat al-Fatiha so powerful? We may not be living in a dark age. But the darkness within hearts")
sh(9, "may be greater than the darkest eras of history. Can a person live on reciting, many times a day, a text whose meaning he does not know?")
sh(10, "Reciting this surah forty times a day, can one spend a whole lifetime without reflecting in the least on the secrets hidden within it?")
sh(11, "This is exactly the state we are in now. Doing things out of habit is the thickest curtain hiding the truth. If a person saw the sunrise for the first time,",
   [("cloth_rustle", "ފަރުދާއެވެ", -24)])
sh(12, "he would fall to the ground at its greatness and wonder. And if he smelled a flower for the first time, tears of joy would fall from his eyes. But,")
sh(13, "because we see these miracles every day, they seem ordinary to us. Surat al-Fatiha is just the same.")
sh(14, "Because we recite it every day, the surah no longer stirs our hearts. The hadiths of Surat al-Fatiha,")
sh(15, "its virtues and its wonders: this surah is not made of ordinary words. As the Messenger of Allah (peace be upon him) said,")
sh(16, "Allah revealed no surah like Surat al-Fatiha in the Torah or the Injil either. This is Umm al-Qur'an, the Mother of the Qur'an.")
sh(17, "Allah revealed: \"I have divided this surah into two halves between Myself and My servant.")
sh(18, "And My servant shall have whatever he asks.\" What does this mean?")
sh(19, "It means that when you recite Surat al-Fatiha, you are not alone. When you speak, Allah answers those words. Reflect on this deeply.", hum=True)
sh(20, "When you say \"Al-hamdu lillahi Rabbil-'alamin\", Allah says: \"My servant has praised Me.\"")
sh(21, "When you say \"Ar-Rahman ar-Rahim\", He says: \"My servant has extolled Me.\" When you say \"Maliki yawmid-din\", He says:")
sh(22, "\"My servant has glorified Me.\" This is not merely a recitation. It is an exchange that takes place in the prayer.")
sh(23, "As your lips move, what is truly happening in that moment is an exchange between the heavens and the earth.", hum=True)
sh(24, "But most of the time we do not feel this. It is narrated that Iblis cried out with a wail of pain four times:",
   [("wind_howl", "ހޭރިގަތެވެ", -24)])
sh(25, "when he was cursed, when he was cast out of Paradise, when a Messenger was sent, and when Surat al-Fatiha was revealed.")
sh(26, "Why was he so troubled when Surat al-Fatiha was revealed? Think about a key.")
sh(27, "It may weigh perhaps 20 grams. Yet it opens a heavy iron door of 200 kilos. Surat al-Fatiha is just like that.",
   [("box_unlock", "ހުޅުވައިދެނީ", -20), ("metal_door", "ދޮރެކެވެ", -20)])
sh(28, "Though it is a short surah, it opens the doors of the universe. There are countless narrations about the virtue of this surah.")
sh(29, "The Messenger of Allah (peace be upon him) said: \"There is no valid prayer for one who does not recite Surat al-Fatiha.\" It is the soul of the prayer.")
sh(30, "The prayer is the pillar of the religion. So the foundation of that pillar of the religion is Surat al-Fatiha. One day the Messenger of Allah (peace be upon him) said to a companion: \"Before you leave this mosque,")
sh(31, "I will teach you the greatest surah of the Qur'an.\" Abu Sa'id ibn al-Mu'alla (may Allah be pleased with him) heard these words,")
sh(32, "and waited with great eagerness. The call to prayer was given, the prayer ended, and as the Messenger of Allah (peace be upon him) was about to leave the mosque, the companion hurried to him and said: \"O Messenger of Allah!",
   [("footsteps_sand", "އަވަސްއަވަހަށް", -24)])
sh(33, "Did you not announce that you would teach me the greatest surah of the Qur'an? I am waiting.\"")
sh(34, "The Messenger of Allah (peace be upon him) turned and said: \"It is Surat al-Fatiha.\" Then he recited the surah.", hum=True)
sh(35, "The companions would have been amazed, because the Qur'an does not begin with a command, nor with a prohibition. The secret of hamd:")
sh(36, "the Noble Qur'an does not open with a fearsome warning. He began His Book with words of praise and glorification.")
sh(37, "\"Al-hamdu lillahi Rabbil-'alamin\" (All praise belongs to Allah, Lord of the worlds). This is not just ordinary thanks.")
sh(38, "It is a declaration that sets the direction of the entire universe. The word \"hamd\" does not simply mean being thankful.")
sh(39, "\"Shukr\" is what one gives for a blessing one has received. But the meaning of \"hamd\" is far wider than this.")
sh(40, "Hamd is complete praise of Allah's essence, His attributes, His actions and every one of His decrees.")
sh(41, "If Allah gives you wealth, praise belongs to Him. And if poverty comes upon you, praise still belongs to Him.")
sh(42, "Whether health or sickness comes to you in life, praise belongs to Him.")
sh(43, "Because hamd is not given only for blessings. It is given for His exalted wisdom.")
sh(44, "So when you say \"Al-hamdu lillah\", what you are saying is: \"O my Lord! In every situation I accept Your decisions with contentment.")
sh(45, "Everything You do is worthy of praise\" - in this way. These are no ordinary words. It is being content with the decree Allah has measured out,")
sh(46, "and choosing peace. Think about it! When you lose your job, or when a loved one departs, or when illness strikes,")
sh(47, "how hard is it to say \"Al-hamdu lillah\" from the depth of your heart? Though it is easy to say with the tongue, accepting it from the depth of the heart is a great test.",
   [("sigh", "ދަތި", -24)], hum=True)
sh(48, "The very first verse of Surat al-Fatiha teaches an important lesson: praise before you ask.")
sh(49, "Before presenting your needs, remember the majesty of your Lord. This is the beautiful etiquette of servitude.")
sh(50, "The \"Al-\" at the beginning of the word \"al-hamd\" is a letter that gives the meaning of inclusion in Arabic. It means that all praise, all beauty and all perfect attributes belong to Allah.")
sh(51, "There is no deficiency in it, nor any limit. Reflect on the depth of this. A person praises something from his own point of view.")
sh(52, "When you praise a painting, in truth the one you are praising is the artist who painted it.")
sh(53, "Is not this whole universe, from the tiniest atom to the vast galaxies, a work of art designed in perfect order?")
sh(54, "The balance within an atom, the system of sight in the eye, the rhythm of the heart, the intricate systems within cells - this is incomparable artistry.")
sh(55, "So then, is not all this praise due to \"Rabbil-'alamin\"? The word \"Rabb\" does not simply mean an owner.")
sh(56, "\"Rabb\" is the One who creates, looks after, raises, nurtures and brings to perfection.")
sh(57, "Allah did not create man and then leave him. At every moment He watches over and nurtures him.")
sh(58, "It is He who arranged your affairs before you were born, who shaped you in your mother's womb, who raised you as a little child, and who today gives you the chance to breathe.",
   hum=True)
sh(59, "Now let us look at the word \"'alamin\". The root meaning of the word \"'alam\" is a 'mark' or a 'signal' - something that points to something else.")
sh(60, "Everything in the universe is evidence that Allah exists. A flower, a star, a human face, the smile of a little child - these are signs pointing to His power.")
sh(61, "When you say \"Rabbil-'alamin\", you are saying: \"O Lord of the visible world and of the unseen spiritual worlds!\" The world of the angels,")
sh(62, "the world of the jinn, the world of the grave and the barzakh, and the world of the hereafter. All of this is not confined to this visible world alone.")
sh(63, "In the prayer, the One you address is the Lord of all these endless worlds. Forty times a day you")
sh(64, "recite \"Al-hamdu lillahi Rabbil-'alamin\". But have you ever asked yourself why you praise Allah?")
sh(65, "Is it an ordinary thing to worship until one's feet swell? The Messenger of Allah (peace be upon him) stood so long in worship at night that his blessed feet swelled.")
sh(66, "When he was asked why he worshipped so much, when his past sins and any future ones had been forgiven, he said:")
sh(67, "\"Should I not be a grateful servant?\" This is the secret of hamd.", hum=True)
sh(68, "For him worship was not a burden; it was a feeling of gratitude. But we often consider blessings to be ordinary things.")
sh(69, "Though we have been given eyes, we forget that seeing is a miracle. Though we have been given ears, we never reflect on the true meaning of hearing.")
sh(70, "As the heart keeps beating, we do not remember that every beat is a beat made by His permission.",
   [("heartbeat", "ޖަހަމުންދާއިރު", -22)])
sh(71, "\"The veil of habituation\": if we saw someone speaking for the first time, we would be amazed. But because everyone speaks,")
sh(72, "we think of it as an ordinary thing. Hamd tears this veil apart. Hamd tells us that this is not ordinary. Think for a moment.",
   [("cloth_rustle", "ވީދާލައެވެ", -24)])
sh(73, "If you had to list the blessings you have been given today, how many things would it include?")
sh(74, "Breath, water, intellect, faith, family, food, shelter, time, and countless more things.",
   [("breath", "ނޭވާލުމާއި", -24), ("pour", "ފެނާއި", -24), ("clock_tick", "ވަގުތާއި", -24)])
sh(75, "When you say \"Al-hamdu lillah\", you are accepting and acknowledging all of those blessings. The first verse of Surat al-Fatiha teaches us to begin with hamd instead of beginning with complaint.")
sh(76, "Because a heart that praises is not a heart that will fall into grumbling and rebellion. In the next verse,")
sh(77, "the attribute of mercy will once again be strongly emphasised: \"Ar-Rahman ar-Rahim\". Why is this attribute repeated? Why does it come twice?",
   [("rain_start", "ރަޙްމަތުގެ", -24)])
sh(78, "What is the purpose of placing the attribute of mercy in the middle like this? In the next part we will reveal the secret of this repetition.",
   hum=True)
SHOTS = S

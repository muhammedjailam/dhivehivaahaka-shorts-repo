"""Beat/shot plan for Taubaa episode 298 — Jawad (used by plan_beats.py)."""

THOBE = ("Jawad here wears a plain white Saudi thobe instead of his navy jacket, same face and trimmed beard as the reference")

LOC = {
    "hotel_window": "a dark, sparse hotel room high up in a big foreign city at night, a tall window with sheer curtains, the city's lights far away and blurred below",
    "dawn_sky": "an open desert landscape at dawn under a vast sky, soft clouds, a slender minaret silhouetted far away on the horizon",
    "saudi_room": "a quiet, simple room in a Saudi home in the late afternoon, plain cream walls, a patterned prayer mat on the floor, a closed Quran resting on a small wooden stand, a tall window with warm light",
    "airport": "a large international airport departure hall with floor-to-ceiling glass windows, a passenger plane waiting outside at dusk",
    "us_street": "a rain-wet street in an American city at dusk, brick buildings, wet reflective pavement, warm streetlights; across the road a small modest mosque with a warmly lit doorway and a small dome",
    "us_living": "a modest student apartment living room in an American city in the evening, a plain sofa and armchairs, a low table with small cups of tea, a lamp, a window showing city lights",
    "night_street": "a dark empty city street abroad at night, wet asphalt, blurred distant city lights glowing at the end of the street",
    "grey_room": "a bare, untidy rented room abroad in cold grey dawn light, an unmade bed in the background, a plain wall mirror, curtains half drawn",
    "cafe": "a dim corner booth of a quiet café abroad in the evening, a dark wooden table, low amber lamp light, deep shadows",
    "us_window": "the same modest American apartment by a large window in the evening, a city skyline outside at dusk",
    "car_deck": "the dashboard of a car in Saudi Arabia in the morning, an old-fashioned car cassette tape deck, warm morning sunlight through the windscreen, a blurred empty road ahead",
    "car_roadside": "inside a car pulled over on the shoulder of a road in Saudi Arabia in the morning, sunlight through the windscreen",
    "desert_road": "an empty straight desert highway in Saudi Arabia at sunrise, a gravel shoulder, low dunes",
    "mosque": "the prayer hall of a simple Saudi mosque, a plain wall, soft carpet in rows, warm light from high windows",
    "mosque_path": "a quiet paved path leading to a Saudi neighbourhood mosque with a minaret at golden dusk, palm trees",
}
MOOD = {
    "hotel_window": "night, cold blue city glow on one side, deep shadows, lonely and empty",
    "dawn_sky": "dawn, soft gold light rays breaking through clouds, merciful, vast and calm",
    "saudi_room": "late afternoon, warm amber window light, quiet, reflective and humble",
    "airport": "dusk, cool teal light through the glass, amber lamps, restless travel",
    "us_street": "dusk, steel-blue rain light, warm glow from the mosque doorway, longing and regret",
    "us_living": "evening, warm amber lamp light, peaceful, admiring",
    "night_street": "night, smoky steel-blue, blurred distant lights, uneasy, nothing glamorous",
    "grey_room": "grey cold dawn light, hollow, empty and ashamed",
    "cafe": "evening, low amber light, heavy shadows, conspiratorial and uneasy",
    "us_window": "dusk, teal sky and warm lamp, tense resolve and quiet relief",
    "car_deck": "morning, warm golden sunlight, still and intimate",
    "car_roadside": "morning, soft golden light, overwhelming emotion, tears",
    "desert_road": "sunrise, golden light rays bursting through clouds, awe, a turning point",
    "mosque": "soft warm light, peace and devotion",
    "mosque_path": "golden dusk, hopeful, peaceful, a good ending",
}

BEATS = [
    dict(to=2, reason="episode opening: Jawad's former life abroad, shown only as a lone man at a night window", chars=["jawad"], loc="hotel_window",
         visual="Jawad standing alone at a tall dark hotel window at night, one hand resting on the glass, looking out at far-away blurred city lights, his face half in shadow, empty and restless; nobody else in the room",
         camera="medium shot from slightly behind and to the side", amb="city_night_far",
         sens="alcohol, zina, dancing", safe="none of it shown: a lone fully clothed man at a night window with distant city lights"),
    dict(to=6, reason="scene change: reflection on Allah's mercy and a Quran verse (symbolic imagery)", loc="dawn_sky",
         visual="a pure landscape: a vast empty desert of sand dunes at dawn, soft golden light rays breaking through ordinary clouds and falling across the sand, a tiny slender minaret far away on the horizon; absolutely no people, no human figures, no faces or shapes in the clouds or sky",
         camera="wide shot, low horizon", amb="dawn_exterior", sens="Quran verse 36:82",
         safe="symbolic dawn sky and minaret; no script rendered"),
    dict(to=8, reason="character change: Jawad today, reflecting on his ending and his prayers", chars=["jawad"], loc="saudi_room",
         visual=f"{THOBE}. Jawad sitting cross-legged on a prayer mat in a quiet room, hands resting on his knees, looking down thoughtfully with a humble, worried expression; a closed Quran on a small wooden stand beside him",
         camera="medium shot, eye level", amb="room_day"),
    dict(to=10, reason="flashback / scene change: travelling from country to country", chars=["jawad"], loc="airport",
         visual="Jawad in his navy zip jacket with a backpack on one shoulder, standing alone at the floor-to-ceiling window of an airport departure hall, looking out at a waiting passenger plane at dusk, restless and distant",
         camera="medium wide, from the side", amb="hall_crowd", transition="dissolve"),
    dict(to=13, reason="scene change: years in America, only one Friday prayer; walking away from the mosque", chars=["jawad"], loc="us_street",
         visual="Jawad in his navy zip jacket, hands in his pockets, walking away along a rain-wet city street at dusk and glancing back over his shoulder at a small mosque with a warmly lit doorway across the road; his face torn and guilty",
         camera="medium wide, eye level", amb="street_night"),
    dict(to=16, reason="characters change: religious friends visit him", chars=["jawad"], loc="us_living",
         visual="in a modest apartment living room two kind bearded young men in white thobes and white ghutras sit on a sofa at a respectful distance, talking gently, small cups of tea on the low table; Jawad in his navy zip jacket sits in an armchair opposite, listening to them with admiring, longing eyes",
         camera="medium wide, eye level", amb="living_night"),
    dict(to=18, reason="action change: weekends going out with bad company (symbolic)", chars=["jawad"], loc="night_street",
         visual="seen from behind: Jawad in his navy zip jacket walking down a dark empty wet street at night between two shadowy male figures seen only from behind as dark silhouettes, heading toward blurred distant city lights; no signs, no crowds, nothing glamorous",
         camera="wide shot from behind, low angle", amb="street_night",
         sens="discos, nightclubs", safe="no club, no neon, no dancing: three figures from behind walking toward distant blurred lights"),
    dict(to=20, reason="action change: he falls into the trap — the hollow aftermath", chars=["jawad"], loc="grey_room",
         visual="Jawad, fully clothed in his grey crew-neck shirt, standing in front of a plain wall mirror in a bare untidy room in cold grey dawn light, his reflection hollow-eyed and ashamed, his hand clenched into a fist at his side; the room otherwise empty",
         camera="medium close-up over his shoulder into the mirror", amb="room_night",
         sens="alcohol, zina", safe="never shown: a hollow-eyed reflection in a mirror in grey dawn light, a closed fist"),
    dict(to=22, reason="time jump and new character: married, he takes his wife back to America", chars=["jawad", "jawad_wife"], loc="airport",
         visual="Jawad in his navy zip jacket and his wife in her black abaya and dusty-rose hijab standing side by side, not touching, at the glass wall of an airport departure hall, each with a rolling suitcase, a plane outside at dusk; she looks ahead hopefully, his eyes are evasive",
         camera="medium wide two-shot, eye level", amb="hall_crowd", transition="black",
         sens="couple; secret sins", safe="married couple only side by side, no touching; the secret sins are not shown"),
    dict(to=24, reason="characters change: the married bad friends advise him to rent an apartment", chars=["jawad"], loc="cafe",
         visual="in a dim café booth two men seen from behind and in deep shadow, faces not visible, one of them sliding a single plain door key across the dark wooden table toward Jawad; Jawad in his navy zip jacket sits opposite looking down at the key, uneasy and troubled",
         camera="medium shot over the shadowy men's shoulders", amb="cafe",
         sens="zina", safe="symbolised only by a plain apartment key slid across a table; bad friends faceless in shadow"),
    dict(to=26, reason="action change: he goes to his wife — 'we must go back to Saudi'", chars=["jawad", "jawad_wife"], loc="us_window",
         visual="Jawad and his wife standing side by side, not touching, by a large apartment window with a city skyline at dusk; Jawad turned toward her, speaking urgently with a resolved, exhausted face; she in her black abaya and dusty-rose hijab listens with relieved, hopeful eyes",
         camera="medium two-shot, eye level", amb="living_night",
         sens="couple", safe="side by side, fully clothed, no touching"),
    dict(to=28, reason="the bad friends return to change his mind (reuse)", reuse="beat_010", chars=["jawad"], loc="cafe",
         visual="(reuse) the faceless friends in the café booth", amb="cafe"),
    dict(to=31, reason="back home, yet the same life and tourism trips (reuse of the lone night window)", reuse="beat_001", chars=["jawad"], loc="hotel_window",
         visual="(reuse) Jawad alone at a night window with distant city lights", amb="city_night_far", transition="black",
         sens="alcohol, nightclubs", safe="lone man at a night window, nothing else shown"),
    dict(to=34, reason="time jump (a year later) and new object: the cassette in his car", loc="car_deck",
         visual="close-up of a man's hand in a white thobe sleeve pushing a plain unlabelled audio cassette into a car's old cassette tape deck on the dashboard, warm morning sunlight through the windscreen, a blurred empty road ahead",
         camera="close-up", amb="car_interior", transition="black",
         sens="real person (Sheikh Ali Jaber)", safe="the sheikh is never depicted: only the plain cassette in the tape deck and the morning road"),
    dict(to=36, reason="action change: he breaks down weeping and pulls over", chars=["jawad"], loc="car_roadside",
         visual=f"{THOBE}. Jawad sitting in the driver's seat of a car pulled over at the roadside in the morning, his forehead bowed onto his hands on the steering wheel, eyes shut, tears on his cheeks, shoulders heaving; warm morning light through the windscreen",
         camera="medium close-up from the passenger seat", amb="car_interior", hum_note="emotional peak"),
    dict(to=39, reason="scene change: the inner call to repent — the car alone at the roadside under breaking light", loc="desert_road",
         visual="a single white car parked on the gravel shoulder of an empty straight desert highway at sunrise, golden light rays bursting through clouds above it, long soft shadows, no people visible",
         camera="wide shot, low angle", amb="dawn_exterior"),
    dict(to=41, reason="action change: he raises his hands asking forgiveness and steadfastness", chars=["jawad"], loc="desert_road",
         visual=f"{THOBE}. Jawad standing beside his parked white car at the roadside, both hands raised in dua, eyes closed, tears on his cheeks, dawn-gold light on his face, the empty desert highway behind him",
         camera="medium shot, eye level", amb="dawn_exterior", sens="dua", safe="raised hands at dawn, no script"),
    dict(to=43, reason="time jump: his life changes, he guards his prayers", chars=["jawad"], loc="mosque",
         visual=f"{THOBE}. Jawad standing in prayer in a row with other men in white thobes seen from behind, hands folded on his chest, eyes lowered, facing a plain mosque wall, peaceful soft light from high windows",
         camera="medium shot from the side and slightly behind", amb="mosque_interior", transition="black"),
    dict(to=44, reason="closing dua for a good ending: Jawad and his wife walk to the mosque", chars=["jawad", "jawad_wife"], loc="mosque_path",
         visual=f"{THOBE}. Seen from behind: Jawad in his white thobe and his wife in her black abaya and dusty-rose hijab walking side by side, not touching, along a quiet path toward a mosque with a minaret glowing in golden dusk light",
         camera="wide shot from behind", amb="dawn_exterior", sens="couple", safe="side by side from behind, no touching"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "He had fallen into many haram things: drinking, zina, dancing — countless things like these.")
sh(2, "He loved every one of them intensely. Dear reader! As repentant Jawad tells, in his own words, what he went through,")
sh(3, "let us look over his story. He said: Allah the Exalted is a kind and generous God to His servants. He")
sh(4, "gives them time, but He does not abandon them. And His mercy surpasses His wrath. Otherwise,")
sh(5, "what would stop Him from sending down punishment and penalty upon His servants whenever He wills?")
sh(6, "\"His command, when He wills a thing, is only to say to it 'Be', and it is.\"", hum=True)
sh(7, "Perhaps Allah willed good for me. I always think about it, afraid of ending badly.")
sh(8, "And I question myself: for example, what is it that stops me from praying?")
sh(9, "But my nafs and Shaytan were against me. I travelled from one country to another — from Greece to France,",
   [("plane_pass", "ދަތުރުކުރީމެވެ", -20)])
sh(10, "to Holland, to Canada, to America and other countries. In America I spent about three years.")
sh(11, "I don't remember praying a single prayer in a mosque except one Friday prayer.")
sh(12, "My sound fitrah and the environment I grew up in kept calling me to Allah's path. But Shaytan overpowered me and wiped the remembrance of Allah from my heart.", hum=True)
sh(13, "I kept sinking deeper into sins and every shameful thing, like a man without any fear.")
sh(14, "In America I spent those years standing at a crossroads. Wishing for my guidance,")
sh(15, "religious friends kept visiting me. My heart was drawn to them. Their dealings, their character,")
sh(16, "and the obedience they showed the Creator — seeing it, I hoped to become like them.")
sh(17, "Yet on the other side, I was always ready to answer the calls of Shaytan.")
sh(18, "Every weekend I went to discos and famous nightclubs. At first I didn't drink.",
   [("footsteps_pavement", "ދަމެވެ", -24)])
sh(19, "But in an environment full of corruption, fighting the nafs became hard. I fell into that trap.", hum=True)
sh(20, "And I started drinking — all kinds of it. And with the drinking I began taking part in obscene deeds like zina.")
sh(21, "I stayed in this state until I came back from America to my own country. I married a kind-hearted, righteous girl from a religious family.")
sh(22, "After the wedding I took my wife back to America. And secretly from her, I started living again the way I had lived before marriage.",
   [("plane_pass", "ދިޔައީމެވެ", -22)])
sh(23, "Bad friends played a big part in this. Sadly, they too were men who had married before me.")
sh(24, "They too lived that way secretly from their wives, behind their backs. They advised me to rent an apartment for haram things.")
sh(25, "From the start my soul refused this shameful, filthy state. At once I went to my beloved wife and said:",
   [("footsteps_pavement", "ގޮސް", -24)])
sh(26, "\"At the earliest chance we must go back to Saudi... I can't bear it any more...\"", hum=True)
sh(27, "Some friends came to change my decision to go back home. They tried very hard.")
sh(28, "They tried every way to make me agree. But to every deviation I said no.")
sh(29, "I finished my studies with good results and came back to my country. Yet I stayed in the very same life as before.")
sh(30, "Because Allah had not yet decreed guidance for me. I went on doing haram things.")
sh(31, "And I travelled to different countries as a tourist, and in those countries I drank and went to nightclubs.")
sh(32, "After about a year in this state, by Allah's decree, I found in my car an audio tape of Sheikh Ali Jaber.")
sh(33, "On it were verses of the Noble Quran and the qunut dua. I sat listening to the sheikh's recitation. It was a deeply moving recitation.",
   hum=True)
sh(34, "When the recitation ended, the sheikh began the dua. I was on the road, going to work. It was morning.",
   [("car_pass", "މަގުމަތީގައެވެ", -22)])
sh(35, "Then I began to cry hard, like a little child. I couldn't even drive the car.",
   [("sob_breath", "ރޮވެން", -22)], hum=True)
sh(36, "So I stopped the car at the side of the road and sat listening to the recitation and the dua. I wept and sobbed.",
   [("sob_breath", "ގިސްލަގިސްލާފައި", -22)], hum=True)
sh(37, "It was as if I were hearing Allah's verses for the first time, hearing such a dua for the first time. My mind began to think, and my heart began to tremble.",
   [("heartbeat", "ތެޅެން", -18)])
sh(38, "And my whole being kept calling out to me: \"Kill Shaytan and desire... O Jawad!", hum=True)
sh(39, "The time has come to leave those filthy, shameful things and reform. Repent! Don't let the chance slip away!\" I repented.", hum=True)
sh(40, "Sobbing, I begged for my sins to be forgiven, and I resolved never to return to those sins again.",
   [("sob_breath", "ގިސްލަގިސްލާފައި", -22)], hum=True)
sh(41, "I pleaded before Allah for steadfastness in the religion. That day I cried a great deal — as I had never cried on any day.")
sh(42, "Then slowly my life began to change. My appearance and my character began to change, and I began walking on the path of good.")
sh(43, "I began guarding my prayers and grew strong in worship. I ask Allah to accept my repentance,")
sh(44, "and to make my ending and the ending of all of you good, and to grant me and you steadfastness in the religion. (The end)")
SHOTS = S

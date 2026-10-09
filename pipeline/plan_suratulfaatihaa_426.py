"""Beat/shot plan for Suratul Faatihaa episode 426 (used by plan_beats.py).
Verses 6-7: not knowing you are lost; the straight path as the middle way; the path of those Allah blessed (prophets,
truthful, martyrs, righteous - symbols only: footprints, an empty early-Madinah mosque, four lamps); the real blessing is
guidance; 'maghdub' (knowledge without action) and 'dallin' (sincerity without knowledge); recap; cliffhanger.
Bible rules: no sacred figure in any form, no calligraphy/text, mushaf closed, prayer rows correct, hijab on every woman."""

MOSQUE_HALL = ("the prayer hall of a white coral-stone Maldivian mosque with carved dark wooden pillars, a lacquered "
               "wooden ceiling, a plain mihrab niche in the qibla wall, soft woven prayer rugs in rows, warm light through "
               "arched windows")
HOME_ROOM = ("a simple tidy room of a Maldivian island home, whitewashed coral-stone walls, a wooden window with shutters "
             "open to coconut palms, a woven mat on a tiled floor, a low wooden table")
BEACH_DAWN = "a quiet palm-lined Maldivian beach with a calm turquoise lagoon at dawn"
OLD_MADINAH = ("early seventh-century Madinah: a simple mosque of palm-trunk pillars with a palm-frond roof and a sandy "
               "floor, mud-brick houses, date palms")
STUDY = "a lamp-lit scholar's study with arched windows, wooden shelves of old leather-bound books and manuscripts"
ISLAND_LANE = "a sandy Maldivian island lane between coral-stone walls and coconut palms"
CAUSEWAY = ("a narrow, perfectly straight raised path of white coral stone running across a Maldivian lagoon toward a "
            "distant green island")

LOC = {
    "sand_path": "a long white-sand footpath through low coastal scrub and coconut palms on a Maldivian island, the open lagoon beside it",
    "fog_coast": "a coastal footpath on a Maldivian island swallowed by thick grey sea mist, the low coral-rock shore and the water's edge barely visible",
    "home_evening": HOME_ROOM,
    "causeway": CAUSEWAY,
    "mosque_hall": MOSQUE_HALL,
    "mosque_night": MOSQUE_HALL,
    "lane_day": ISLAND_LANE,
    "home_dawn": HOME_ROOM,
    "ridge_dawn": "a low sandy ridge on a Maldivian island above a long straight sandy track that runs across the island toward the horizon, a few faint side trails branching off into the scrub and shadow",
    "beach_night": "a quiet palm-lined Maldivian beach at night, a calm dark lagoon reflecting the stars",
    "desert_path": "a wide empty desert of soft golden sand dunes crossed by a single straight trail of footprints",
    "old_madinah": OLD_MADINAH,
    "lane_dusk": ISLAND_LANE,
    "hill_path": "a narrow steep rocky footpath climbing a windswept grassy headland high above the sea",
    "city_road": "a wide busy paved avenue of Male city between modern white buildings, with a narrow sandy side path branching off it toward a quiet palm-lined shore",
    "summit": "the grassy top of a high headland above the ocean with a wide view over the islands and turquoise lagoons of a Maldivian atoll",
    "home_night": HOME_ROOM,
    "city_night": "the wide polished marble steps of a luxurious modern glass building in Male city at night",
    "lane_dawn": ISLAND_LANE,
    "reef": "the outer reef edge of a Maldivian atoll, a small plain white lighthouse on a coral outcrop, white surf breaking on the reef and a calm deep-blue safe channel beside it",
    "crossroads": "a crossroads of sandy paths among coconut palms on a Maldivian island at night",
    "study": STUDY,
    "storm_path": "a dark jagged rocky path branching away to the left from a straight white coral-stone path, leading toward black cliffs",
    "sea_fog": "the open water inside a Maldivian atoll covered in thick white fog, no land visible",
    "mosque_court": "the sandy courtyard of a white coral-stone Maldivian mosque with an arched veranda, a low wall and coconut palms",
    "fork_plain": "a wide open plain where one sandy path splits into three ways",
    "ruins": "the ruins of an ancient city of crumbling mud-brick walls and broken stone columns half-buried in desert sand",
    "beach_dawn": BEACH_DAWN,
    "door_dawn": "a simple arched wooden doorway in a white coral-stone wall opening onto a sunrise lagoon, a sandy path leading up to it",
}
MOOD = {
    "sand_path": "late golden-hour dusk, long soft shadows, warm gold fading into teal, quietly uneasy",
    "fog_coast": "twilight, cool grey-blue mist, muted colours, one faint warm glow high in the sky above the fog, uneasy and searching",
    "home_evening": "evening, a single warm table lamp, deep teal dusk beyond the open shutters, thoughtful and weighing",
    "causeway": "golden hour, warm gold light along the white path, the left side of the lagoon dark storm-grey, the right side glittering hazy gold, balanced and calm in the middle",
    "mosque_hall": "late afternoon, warm amber light through the arched windows, emerald shadows, quiet and reverent",
    "mosque_night": "night, warm glowing amber lamps, deep blue night in the arched windows, emerald shadows, intimate and prayerful",
    "lane_day": "bright late morning, dappled palm shade, warm tropical sunlight, slightly uneasy",
    "home_dawn": "first light of dawn, soft blue-grey light turning gold through the open shutters, a small oil lamp still glowing, quiet and alert",
    "ridge_dawn": "dawn, gold light on the horizon at the end of the straight track, blue shadow over the side trails, hopeful and earnest",
    "beach_night": "deep blue night, a sky full of stars and the Milky Way, faint silver moonlight, reflective and searching",
    "desert_path": "first light of dawn, hazy, slightly desaturated, soft vignette, a warm gold glow on the horizon, sacred stillness",
    "old_madinah": "early morning, hazy, slightly desaturated, soft vignette, shafts of gold light through the palm-frond roof, drifting dust motes, sacred stillness",
    "lane_dusk": "dusk, deep violet-blue sky, warm golden lamp glow, emerald shadows, serene and reverent",
    "hill_path": "storm-grey late afternoon, strong wind bending the grass, a thin break of gold light far above, lonely and determined",
    "city_road": "bright hazy midday, harsh white light on the busy avenue, soft warm light on the quiet side path",
    "summit": "sunrise, brilliant warm gold light, a vast clear sky, triumphant and peaceful",
    "home_night": "night, a single warm oil-lamp glow on the low table, deep teal and emerald shadows, still and contemplative",
    "city_night": "night, harsh white camera flashes and cold blue city light, hollow and lonely",
    "lane_dawn": "early dawn, soft pink-gold light, long gentle shadows, peaceful and blessed",
    "reef": "twilight, deep blue sea, the lighthouse beam glowing warm gold, white surf on the reef, watchful and safe",
    "crossroads": "night, deep blue darkness, the warm circle of a hand-held lantern, one path ahead faintly lit gold, the side paths swallowed in darkness, uncertain",
    "study": "night, warm lamp light on the books but cold blue shadow around the man, a bright doorway of light behind him, proud and cold",
    "storm_path": "stormy night, cool storm-grey and deep blue, heavy black clouds and distant lightning over the dark side path, a faint warm light still on the straight path, grave warning",
    "sea_fog": "dim grey-white daylight in the fog, cold and directionless, muted colours",
    "mosque_court": "bright morning, white walls, soft shadows under the arches, calm",
    "fork_plain": "dusk, a storm-grey sky on the left, cold white fog on the right, a thin warm gold light straight ahead, a moment of warning",
    "ruins": "dusk, hazy, slightly desaturated, soft vignette, dust drifting in the low orange light, silent and ancient",
    "beach_dawn": "sunrise, golden light spreading over the lagoon, soft pink and gold sky, grateful and complete",
    "door_dawn": "dawn, brilliant warm gold light pouring through the doorway, emerald and teal shadows around it, hopeful anticipation",
}

BEATS = [
    # --- 1. are you really on the straight path? ---
    dict(to=3, reason="episode opening: the traveller whose course slowly drifts without his noticing", chars=["listener"], loc="sand_path",
         visual="the listener walking calmly along a long white-sand path, seen from behind and slightly above; a perfectly straight faint golden line of light runs ahead to the horizon, while his own footprints in the sand bend gently away from that line in a slow curve without him noticing; he walks on, relaxed and unaware",
         camera="high wide shot from behind, the man and the curving footprints in the upper two-thirds, smooth sand as the lower third", amb="beach_dusk"),
    dict(to=5, reason="new image: the greatest danger is not knowing you are lost — walking confidently into the mist", chars=["listener"], loc="fog_coast",
         visual="the listener striding confidently along a coastal path into thick grey sea mist, his head held high and a calm unaware expression, while just ahead of him the path fades into the fog near the edge of the low rocky shore; far above the mist a faint warm glow of light",
         camera="medium wide, eye level, slightly from the side, his face in the upper third, misty ground as the lower third", amb="beach_evening"),
    dict(to=7, reason="new example: guidance in every area of life — decisions, a job, a life partner, words", chars=["listener"], loc="home_evening",
         visual="the listener sitting cross-legged on the woven mat at the low wooden table in the evening, two closed plain envelopes and a folded blank letter in front of him, his chin resting on his hand, pausing thoughtfully before a decision; the warm lamp lights his face",
         camera="medium shot, eye level, his face in the upper third, the table top as the calm lower third", amb="island_house_night"),
    dict(to=8, reason="new symbol: the straight path is the middle way between two extremes", loc="causeway",
         visual="a narrow, perfectly straight white coral-stone path crossing a lagoon toward a distant green island; on its left the water is dark, choppy and storm-grey, on its right the water glitters with a heavy hazy gold shimmer; the path itself lies calm and bright in the middle, no people",
         camera="wide shot from slightly above along the path, the path leading into the upper third, still water as the lower third", amb="beach_dusk"),
    # --- worship without steadfastness ---
    dict(to=9, reason="new example: a man prays but his heart is not there", chars=["listener"], loc="mosque_hall",
         visual="the listener wearing a white crocheted prayer cap, standing in a straight row of worshippers seen from the side, every man in the row including him facing the same direction toward the plain mihrab niche at the left edge of the frame, hands folded on their chests; no other mihrab or arch niche anywhere else in the hall; the listener's eyes are unfocused and far away, distracted, and in the soft light of the arched window beside him a faint dreamlike double exposure of a busy shop counter and a ringing phone hangs in the air, showing where his thoughts have gone",
         camera="medium shot, eye level, slightly from the side, his face in the upper third, the woven rugs as the lower third", amb="mosque_interior"),
    dict(to=11, reason="new example: charity given for show", chars=["listener"], loc="lane_day",
         visual="the listener in the sandy lane holding out a plain white envelope to a humble old man in a faded shirt seen from behind, but the listener is turned half away, smiling proudly toward a young man who is holding up a phone to film him; the giving looks like a performance",
         camera="medium wide, eye level, faces in the upper third, the sandy lane as the lower third", amb="village_day"),
    dict(to=13, reason="new image: the prayer repeated about forty times a day is an alarm that checks the self", chars=["listener"], loc="home_dawn",
         visual="the listener sitting upright on a prayer mat at dawn wearing a white crocheted prayer cap, one hand resting on his chest, eyes lowered in honest self-examination; beside him on the windowsill an old brass alarm clock with a plain blank face and no numbers, its bell catching the first light",
         camera="medium shot, eye level, his face in the upper third, the prayer mat as the lower third", amb="room_day"),
    # --- 2. the path of those Allah blessed ---
    dict(to=16, reason="new topic: the next verse describes the path further", chars=["listener"], loc="ridge_dawn",
         visual="the listener standing on a low sandy ridge, seen from behind, looking down at a long straight sandy track that runs across the island to a horizon glowing with dawn; several faint side trails branch off it into shadowy scrub",
         camera="wide shot from behind, the man small in the upper-middle, the straight track leading to the horizon, sand as the lower third", amb="dawn_exterior",
         transition="black"),
    dict(to=18, reason="action change: the dua itself — 'Guide us to the straight path!'", chars=["listener"], loc="mosque_night",
         visual="the listener wearing a white crocheted prayer cap, sitting alone on a prayer rug in the quiet mosque at night, both palms raised at chest height in dua, eyes softly closed, his face lit warm by a glowing lamp, the plain mihrab niche softly lit behind him",
         camera="medium close-up, eye level, slightly from the side, his face and hands in the upper two-thirds, the rug as the lower third", amb="mosque_interior"),
    dict(to=20, reason="new image: a person cannot hold on to an abstract idea; he needs a living example", chars=["listener"], loc="beach_night",
         visual="the listener standing alone on the beach at night, looking up at the vast sky full of stars, searching, his kurta stirred by a light breeze; the starlight reflects on the still lagoon",
         camera="wide shot from slightly behind and to the side, the man and the sky in the upper two-thirds, the dark still lagoon as the lower third", amb="beach_evening"),
    dict(to=22, reason="new symbol: the straight path is not empty — real people walked it and their footprints remain", loc="desert_path",
         visual="a single straight trail of footprints pressed into soft golden sand, leading over the dunes toward a glowing dawn horizon; the footprints are clear in the foreground and fade into the light ahead; no people anywhere, no figures, no shadows of people",
         camera="low wide shot along the footprints, the glowing horizon in the upper third, sand as the lower third", amb="desert_night",
         transition="dissolve", sens="sacred_figure",
         safe="the prophets and righteous who walked the path are shown only as footprints in the sand leading to light; no figure, no silhouette (rule 2)"),
    dict(to=25, reason="new image: Q4:69 — the prophets, the truthful, the martyrs and the righteous", loc="old_madinah",
         visual="the empty early mosque of palm-trunk pillars and palm-frond roof at early morning, shafts of gold light falling through the roof onto the sandy floor, a few plain woven mats on the sand, no people at all; date palms and mud-brick houses beyond the open side",
         camera="wide shot, eye level, the light shafts in the upper two-thirds, the sandy floor as the lower third", amb="old_madinah_day",
         transition="dissolve", sens="sacred_figure",
         safe="the prophets, truthful and martyrs are evoked by the empty early-Madinah mosque in light, with no people (rule 2)"),
    dict(to=27, reason="new symbol: four qualities — obedience to revelation, truthfulness, sacrifice, steadfastness", loc="lane_dusk",
         visual="four plain undecorated brass oil lamps set on the sand in a row along the lane at dusk, each burning with a warm steady flame, leading toward a soft glow at the end of the lane; no people",
         camera="low medium-wide shot along the row of lamps, the flames in the upper two-thirds, smooth sand as the lower third", amb="island_night",
         transition="dissolve", sens="sacred_figure",
         safe="the prophets, the truthful, the martyrs and the righteous are symbolised by four burning lamps; martyrdom is shown only as a steady flame, no war (rules 2 and 7)"),
    dict(to=29, reason="new image: a huge request — a path of sacrifice, patience and loneliness", chars=["listener"], loc="hill_path",
         visual="the listener alone, climbing a narrow steep rocky path up a windswept headland, leaning into the strong wind, his kurta blown back, a determined patient face, a thin break of gold light in the clouds high above the summit",
         camera="wide shot from slightly below and to the side, the man in the upper half, rocky ground as the lower third", amb="vast_plain",
         sfx_note="wind"),
    dict(to=31, reason="new image: the path of the blessed is not the crowded road of the majority", chars=["listener"], loc="city_road",
         visual="a large crowd of men and women in modest clothing, the women in hijabs, all seen from behind, streaming down the wide busy avenue in one direction; the listener alone turning off onto the narrow sandy side path toward the quiet shore, a few of the crowd glancing back at him",
         camera="wide shot from slightly above, the listener and the fork in the upper half, the paved road as the lower third", amb="city_day"),
    dict(to=33, reason="emotional turning point: at the end lies true success", chars=["listener"], loc="summit",
         visual="the listener standing at the top of the headland at sunrise, seen from behind and slightly to the side, his arms relaxed at his sides, looking out over a vast view of islands and turquoise lagoons bathed in gold light, peaceful and fulfilled",
         camera="wide shot, the man and the sunrise in the upper two-thirds, the grassy slope as the lower third", amb="dawn_exterior"),
    # --- the real blessing is guidance ---
    dict(to=35, reason="new symbol: the real blessing is not money, health or rank, but guidance", chars=["listener"], loc="home_night",
         visual="a close-up of the listener's open hand resting on the low wooden table, cradling a small glowing light like a tiny flame of warm gold; beside it, pushed aside, a careless heap of gold coins and an expensive gold wristwatch lying in shadow",
         camera="close-up, slightly from above, the glowing palm in the upper-middle, the table top as the lower third", amb="room_night"),
    dict(to=37, reason="new example: rich yet lost, powerful yet a tyrant, famous yet in falsehood", chars=["powerful_man"], loc="city_night",
         visual="the powerful man standing on the marble steps of the luxurious building at night, a crowd of photographers' silhouettes below him raising cameras with bright white flashes, two security men in dark suits seen from behind; his face proud but hollow, his eyes empty and lost",
         camera="medium wide, slightly low angle, his face in the upper third, the marble steps as the lower third", amb="city_night_far"),
    dict(to=38, reason="character change: the poor but guided man stands on the straight path", chars=["elder"], loc="lane_dawn",
         visual="the old fisherman walking slowly but contentedly down the sandy lane toward a small white mosque at dawn, a calm gentle smile on his weathered face, soft pink-gold light around him; his worn sandals leave light prints in the sand",
         camera="medium wide, eye level, slightly from the front, his face in the upper third, the sandy lane as the lower third", amb="dawn_exterior"),
    # --- 3. not the path of those who earned anger, nor of those who went astray ---
    dict(to=40, reason="new topic: safety also comes from recognising the dangers", loc="reef",
         visual="a small wooden Maldivian dhoni with a glowing lantern sailing safely through the calm deep-blue channel beside the reef, white surf breaking on the coral on both sides, a small plain white lighthouse on the coral outcrop shining a warm gold beam over the danger; tiny figures of the crew seen from far behind",
         camera="wide shot from slightly above, the lighthouse and dhoni in the upper two-thirds, deep water as the lower third", amb="sea_boat",
         transition="black"),
    dict(to=43, reason="new image: who are these two groups, and why is the straight path between them?", chars=["listener"], loc="crossroads",
         visual="the listener standing at a crossroads at night holding up a lantern, seen from behind and slightly to the side; the path straight ahead is faintly lit gold, while on the left a path leads into cold black rocks and on the right a path disappears into thick white fog; he studies both side paths carefully",
         camera="medium wide from behind, the man and the three paths in the upper two-thirds, sand as the lower third", amb="island_night"),
    dict(to=46, reason="the narration returns to recognising the dangers, not only the ideal model", loc="reef", reuse="beat_020",
         visual="(reuse of the reef and lighthouse image)", amb="sea_boat"),
    dict(to=48, reason="the narration returns to the straight path lying between two boundaries", loc="causeway", reuse="beat_004",
         visual="(reuse of the straight white path between the dark and the gold water)", amb="beach_dusk"),
    # --- al-maghdub: knowledge without action ---
    dict(to=51, reason="new figure: those who know but do not act — knowledge without submission", loc="study",
         visual="a proud middle-aged man in a dark waistcoat over a white long-sleeved shirt and round glasses standing in the study among tall stacks of closed old books, arms crossed, chin raised, deliberately turning his back on a bright doorway of warm light behind him; his face cold and stubborn",
         camera="medium wide, eye level, his face in the upper third, the floor with stacked books as the lower third", amb="library_night"),
    dict(to=54, reason="new symbol: deliberately turning away from the truth brings divine anger, by justice", loc="storm_path",
         visual="a dark jagged rocky path branching away to the left from a straight white path, leading toward black cliffs under heavy black storm clouds with distant lightning; the straight white path on the right still holds a faint warm light; no people",
         camera="wide shot, eye level, the storm and the fork in the upper two-thirds, the white path as a calm lower third", amb="storm_night",
         sens="other", safe="Allah's anger is never personified: only a distant storm over the dark side path; no fire, no punishment (rules 1 and 5)"),
    dict(to=55, reason="the narration returns to the man of dry knowledge with no heart", loc="study", reuse="beat_024",
         visual="(reuse of the proud man among his books)", amb="library_night"),
    # --- ad-dallin: sincerity without knowledge ---
    dict(to=59, reason="new example: those who strive sincerely but stray in ignorance", chars=["listener"], loc="sea_fog",
         visual="the listener, his kurta sleeves rolled up, rowing a small wooden boat hard and earnestly into thick white fog, sincere and eager, but with no compass, map or lantern in the boat, unaware that the dark shape of a reef rises out of the mist ahead",
         camera="medium wide, eye level, slightly from the side, his face in the upper third, the grey water as the lower third", amb="sea_boat"),
    dict(to=62, reason="new symbol: the straight path is the balance of knowledge and obedience, reason and revelation", loc="home_night",
         visual="an old brass two-pan balance scale standing level on the low wooden table at night; on one pan a closed leather-bound book, on the other a small glowing oil lamp, perfectly balanced; a closed mushaf with a plain gold-ornamented cover rests on a small wooden rehal behind it",
         camera="medium close-up, eye level, the scale in the upper two-thirds, the table top as the lower third", amb="room_night"),
    dict(to=64, reason="new example: one memorised the Quran but his character is low; another is all emotion without knowledge", chars=["elder"], loc="mosque_court",
         visual="in the mosque courtyard a young man in a white robe with a closed mushaf held under his arm walks past haughtily with his chin raised, ignoring the old fisherman who is stooping to pick up a dropped rolled prayer mat; in the background under the arches another young man waves his arms passionately and excitedly at a few friends",
         camera="medium wide, eye level, faces in the upper third, the sandy courtyard as the lower third", amb="island_day"),
    dict(to=66, reason="the narration returns to the dua in every rak'ah", loc="mosque_night", chars=["listener"], reuse="beat_009",
         visual="(reuse of the listener in dua in the mosque at night)", amb="mosque_interior"),
    dict(to=69, reason="new image: over time a person can drift toward pride or toward straying", chars=["listener"], loc="fork_plain",
         visual="the listener standing at a fork in a sandy path at dusk, seen from behind; on the left a towering staircase of huge stacked closed old books climbs up toward storm-grey clouds, on the right the path slopes down into thick cold white fog, and straight ahead a narrow path glows with a thin warm gold light; he hesitates",
         camera="wide shot from behind, the three ways in the upper two-thirds, the sandy path as the lower third", amb="vast_plain"),
    dict(to=70, reason="the narration returns to slipping toward one of the two boundaries", loc="causeway", reuse="beat_004",
         visual="(reuse of the straight white path between the dark and the gold water)", amb="beach_dusk"),
    # --- it is about you; recap ---
    dict(to=71, reason="new image: not only the stories of nations of old", loc="ruins",
         visual="the silent ruins of an ancient city of crumbling mud-brick walls and broken stone columns half-buried in sand at dusk, dust drifting in low orange light; no people",
         camera="wide shot, eye level, the ruins in the upper two-thirds, sand as the lower third", amb="ruins_dust",
         transition="dissolve", sens="other", safe="the nations of old are shown only as empty ruins, no people"),
    dict(to=73, reason="new image: the straight path is an inner balance", chars=["listener"], loc="home_night",
         visual="the listener sitting peacefully on the woven mat at night, wearing a white crocheted prayer cap, eyes gently closed, one hand on his heart, a calm deep peace on his face, the warm oil lamp glowing beside him",
         camera="medium shot, eye level, his face in the upper third, the mat as the lower third", amb="room_night",
         transition="dissolve"),
    dict(to=74, reason="new chapter: recap of the whole surah — from praise to warning", loc="beach_dawn",
         visual="the sun rising over the calm turquoise lagoon, a small white domed coral-stone mosque among palms on the shore, golden light spreading across the water and sky; no people",
         camera="wide shot, the sun, sky and mosque in the upper two-thirds, the calm lagoon as the lower third", amb="dawn_exterior",
         transition="black", sens="hereafter",
         safe="the Day of Judgement named in the recap is not shown; only the sunrise over the lagoon (rule 5)"),
    dict(to=75, reason="the narration returns to the daily recitation in prayer", loc="mosque_night", chars=["listener"], reuse="beat_009",
         visual="(reuse of the listener in dua in the mosque at night)", amb="mosque_interior"),
    dict(to=77, reason="new image: cliffhanger — can seven verses change your life?", chars=["listener"], loc="door_dawn",
         visual="seven small plain undecorated brass oil lamps burning in a row along a sandy path that leads to an open arched wooden doorway full of brilliant dawn light; the listener stands at the threshold, seen from behind, about to step through",
         camera="wide shot from behind, the doorway and the man in the upper two-thirds, the row of lamps leading in from the lower third", amb="dawn_exterior"),
]
for b in BEATS:
    b.pop("sfx_note", None)

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Ask yourself: how do you know that you are truly on the straight path?")
sh(2, "Sometimes a person may not even sense that he is travelling down a bad road. Through a habit, a surrounding, an idea or a worldly goal, his course can slowly change without him noticing.",
   [("footsteps_sand", "ދަތުރުކުރާކަން", -24)])
sh(3, "Even then he may believe he is on the right road. That is why Surat al-Fatiha has us say again and again, 'Guide us.'")
sh(4, "It is a sign of relying on Allah more than on oneself. This verse teaches that the greatest danger is not getting lost;")
sh(5, "the greatest danger is not realising that you are lost. This prayer is not only about creed.")
sh(6, "It touches every area of life: in making a decision, in choosing a job,")
sh(7, "in finding a life partner, and even in speaking a word. 'As-sirat al-mustaqim' is not only prayer. It is the path of moderation.")
sh(8, "A path with no going beyond the limits and no negligence. A path with no abandoning the world entirely, and no drowning in the world either.")
sh(9, "This is the path of the prophets. A person may pray, yet his heart may not be there. He may fast,")
sh(10, "yet he may be an arrogant man. He may give charity, yet it may be for show. Is such a person on the straight path?")
sh(11, "There is worship, but there is no steadfastness in it. Surat al-Fatiha does not only teach us to worship.")
sh(12, "What then? To stand firm in it. We must repeat this prayer some forty times a day, because a person can stumble forty times, lose his way forty times, and be defeated by his own ego forty times.")
sh(13, "This prayer is an alarm set to check your self, your direction and your intention without a break.",
   [("clock_tick", "އެލާމެކެވެ", -22)])
sh(14, "The next verse explains this path further. It describes it as 'the path of those whom God has blessed.'")
sh(15, "Who these blessed ones are, and why their path is emphasised, will be explained in the next part.")
sh(16, "It will make clear whose path it is, and from whom we must keep away.")
sh(17, "The path of the prophets, the martyrs and the righteous servants: we ask to be guided to the straight path.")
sh(18, "'Guide us to the straight path!' But Surat al-Fatiha does not end there.",
   [("whisper_recite", "މަގުދައްކަވާނދޭވެ", -26)], hum=True)
sh(19, "That path has not been left as a merely imaginary or abstract idea, because it is hard for a person to hold on to such an imaginary idea for long.")
sh(20, "What a person needs is a model — examples that show it in practice. So the prayer continues:")
sh(21, "'Sirat alladhina an'amta 'alayhim' — that is, the path of those upon whom You, our Lord, have bestowed Your blessing.")
sh(22, "So 'as-sirat al-mustaqim' is not an empty road. It is a road that real people have walked, a road where the marks of their footsteps can still be seen.",
   [("footsteps_sand", "ހިނގާފައިވާ", -24)], hum=True)
sh(23, "The question that arises here is: who are those blessed ones? Another verse of the Holy Quran explains it.")
sh(24, "Those who obey Allah and His Messenger will be with those whom Allah has blessed:")
sh(25, "the prophets, the truthful (siddiqin), the martyrs and the righteous servants. This is not just a list of names.")
sh(26, "These are qualities given form. The path of the prophets is complete obedience to revelation. The path of the truthful is loyalty and truthfulness.")
sh(27, "The path of the martyrs is sacrifice. The path of the righteous is steadfastness. In every rak'ah you say: 'O my Lord!")
sh(28, "Place me on the path they walked!' This is a very great request, because that path is not a comfortable one. It is a path of sacrifice, of patience,")
sh(29, "and sometimes of enduring loneliness. Ask yourself: do you truly want that path?",
   [("wind_gust", "އެކަނިވެރިކަންވެސް", -22)])
sh(30, "Or is it just a sentence spoken by the tongue? The path of the blessed is not the path the majority accept, nor the crowded road.")
sh(31, "Sometimes it is a road where you may face others' bad opinions of you, being shut out, and worldly losses.")
sh(32, "But at the end lies true success. Surat al-Fatiha teaches that the straight path is not the road where the majority stand,",
   hum=True)
sh(33, "but the path of the few whom Allah has blessed. There is an important point to note here.")
sh(34, "Pay attention to the words 'an'amta 'alayhim' — upon whom You have bestowed Your blessing. What is the true meaning of the word 'blessing' (ni'mah)?")
sh(35, "Is it money, good health, a high position? No. The true blessing is guidance.")
sh(36, "A man may be rich, yet lost. He may be powerful, yet a tyrant.")
sh(37, "He may be famous, yet living in falsehood. But a person given the blessing of guidance, even if he is poor or an ordinary man,",
   [("camera_shutter", "މަޝްހޫރު", -22)])
sh(38, "stands on the straight path. That is the greatest blessing. Now comes the most important point: in Surat al-Fatiha we do not ask only for the right path.",
   hum=True)
sh(39, "We also ask to be protected from the bad paths, because a person's safety does not come only from knowing his destination.",
   [("wave_crash", "ރައްކާތެރިކޮށްދެއްވުމަށްވެސް", -24)])
sh(40, "It also comes from recognising the dangers. The next verse says: 'ghayril maghdubi 'alayhim wa lad-dallin' — that is,")
sh(41, "not the path of those who have earned anger, nor the path of those who have gone astray. Who are these two groups?")
sh(42, "Why are they mentioned specifically? And why is the straight path placed between these two paths?")
sh(43, "In the next part we will look in detail at these two dangers. The qualities of the path have now been described.")
sh(44, "Those who earned anger and those who went astray: the straight path is the path of those whom Allah has blessed.")
sh(45, "But Surat al-Fatiha does not end by describing only the ideal model.")
sh(46, "Because a person gains no safety just by learning what is good. He must also recognise what is bad. Therefore,")
sh(47, "this prayer ends like this: 'ghayril maghdubi 'alayhim wa lad-dallin' — not the path of those who earned anger, nor of those who went astray.")
sh(48, "These are two groups, two boundaries and two great dangers. As-sirat al-mustaqim, the straight path, lies between these two boundaries.")
sh(49, "Let us look at the meaning of these two expressions one by one. 'Ghayril maghdubi 'alayhim' — those who earned anger — describes those who know but do not act.")
sh(50, "They are those who know the truth and deny it, and who know the right way yet stubbornly oppose it. They have knowledge,",
   [("page_turn", "ޢިލްމު", -24)])
sh(51, "but no submission. They have intellect, but no obedience. This is the most dangerous wrong path.")
sh(52, "Because it does not come from ignorance; it is a deliberate turning of one's back on the truth.")
sh(53, "Whoever knowingly goes against the truth for the sake of his own desires deserves the anger of Allah.",
   [("thunder", "ކޯފާ", -20)])
sh(54, "Here 'ghadab', anger, is not merely an emotion; it is a consequence that comes through divine justice, from going astray despite having knowledge.")
sh(55, "It is a straying from the boundary built on dry knowledge alone. There is no heart there, no obedience, no gentleness — only claims.")
sh(56, "'Ad-dallin' — those who went astray — are those who strayed in ignorance. Even if they strove to seek the truth,")
sh(57, "they have no guidance. They may be sincere, but they have no knowledge.")
sh(58, "They follow their feelings, but their foundation is not revelation. On this side there may be emotion, but no knowledge.")
sh(59, "There may be sincerity, but no standard. This too is dangerous, because good intention alone does not save a person.")
sh(60, "As-sirat al-mustaqim is the standard between these two boundaries: knowledge and obedience; thought and God-consciousness; reason and revelation.")
sh(61, "Surat al-Fatiha teaches that knowing alone is not enough, and feeling alone is not enough.")
sh(62, "One must know the truth, and one must also submit to it. Now ask yourself: which danger are you closer to?")
sh(63, "The danger of knowing and not acting? Or the danger of believing without knowledge? A person may memorise the Quran, yet his character may be low.")
sh(64, "Another may be a very emotional person, yet far from the knowledge of revelation. Neither of these two is 'the sirat'.")
sh(65, "Each time you recite Surat al-Fatiha in a rak'ah, it pushes you to build this standard: 'O my Lord! Do not place me among those made arrogant by their knowledge,")
sh(66, "nor among those who think ignorance is no fault.' This verse is also a warning.",
   [("whisper_recite", "ނުލައްވާނދޭވެ", -26)], hum=True)
sh(67, "Because as time passes, a person's course can change. At first he may be on the straight path.",
   [("clock_tick", "ވަގުތު", -24)])
sh(68, "But if his arrogance grows as his knowledge grows, he is steering his course toward 'ghadab', anger.")
sh(69, "Or if he begins religious life with zeal but makes no effort to seek knowledge, he is heading toward going astray.")
sh(70, "That is why this prayer is repeated some forty times every day: because on any day a person can slip toward one of these two boundaries.")
sh(71, "Surat al-Fatiha is not only a surah telling the stories of nations of old. It is the story of two traits inside you: the arrogance within you,")
sh(72, "your ignorance, your stubbornness and your lack of steadfastness. As-sirat al-mustaqim is not only a road seen from outside; it is inner balance.",
   [("breath", "ހަމަޖެހުމެވެ", -24)], hum=True)
sh(73, "This prayer teaches that the straight path is the path far from both these boundaries. With this, Surat al-Fatiha is complete.")
sh(74, "The surah began with praise. Then mercy brought gentleness. The remembrance of the Day of Judgement brought seriousness. Servitude was declared.")
sh(75, "Guidance was asked for. Examples made it clear. And the warning fixed it as a standard. You recite this surah forty times a day.")
sh(76, "Now the question that arises is this: can these seven verses truly change your life? In the final part we will look at the whole of Surat al-Fatiha together,")
sh(77, "and find the answer to this question: if a person understands Surat al-Fatiha in its true meaning, what change will come to his life?",
   hum=True)
SHOTS = S

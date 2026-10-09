"""Beat/shot plan for Suratul Faatihaa episode 424 (used by plan_beats.py)."""

_MOSQUE = ("the prayer hall of a white coral-stone Maldivian mosque with carved dark wooden pillars, a lacquered wooden "
           "ceiling, a plain mihrab niche in the qibla wall, soft woven prayer rugs in rows, warm light through arched windows")
_PLAIN = "a vast empty plain under a blinding white-gold sky, fine dust drifting"
_LANE = "a sandy Maldivian island lane between coral-stone walls and coconut palms"

LOC = {
    "veil_world": "a small Maldivian island seen from its calm lagoon, coconut palms, a white coral-stone mosque, the open sea and sky",
    "plain": _PLAIN,
    "veranda": "the shaded veranda of a spacious, well-kept Maldivian island home with a wooden swing chair (undhoali), a low table set with dishes of food and fruit, potted plants, coconut palms beyond",
    "beach_dawn": "a quiet palm-lined Maldivian beach with a calm turquoise lagoon at dawn",
    "island_lane_night": _LANE,
    "old_madinah": "early seventh-century Madinah: a simple mosque of palm-trunk pillars with a palm-frond roof and a sandy floor, mud-brick houses, date palms",
    "mosque_night": _MOSQUE,
    "mosque_dawn": _MOSQUE,
    "mosque_soft": _MOSQUE,
    "lagoon_bridge": "a very long, narrow wooden footbridge stretching far across a calm open lagoon between two distant horizons",
    "night_beach": "a quiet palm-lined Maldivian beach at night beside a calm lagoon",
    "minaret": "a small white coral-stone Maldivian island mosque with a single slender white minaret beside a mirror-still lagoon, coconut palms",
    "office_night": "a luxurious high-rise office at night with a large polished dark desk and floor-to-ceiling windows over distant city lights",
    "home_room": "a simple tidy room of a Maldivian island home, whitewashed coral-stone walls, a wooden window with shutters open to coconut palms, a woven mat on a tiled floor, a low wooden table",
    "atoll_night": "an aerial view of a Maldivian atoll at night: many small islands ringed by pale reefs in a dark moonlit lagoon, a small white mosque on every island",
    "open_sea": "the vast open Indian Ocean far from any island, a small wooden fishing dhoni",
    "storm_house": "a small coral-stone Maldivian island house with a corrugated roof among tall coconut palms",
    "island_lane_dawn": _LANE,
    "night_road": "a long narrow road across the wild, overgrown interior of an island at night, wet with rain, side tracks branching off into darkness",
    "dawn_road": "a broad, clear, straight road of pale sand running through green open land towards the horizon",
    "sirat": "a thin glowing bridge of light spanning a vast dark misty abyss",
}
MOOD = {
    "veil_world": "sunrise, soft gold light diffused through a shimmering veil, hazy and dreamlike, a sense of something hidden",
    "plain": "the hereafter: timeless blinding white-gold light, vast silence, awe and quiet dread, fine dust in the air",
    "veranda": "late golden afternoon, warm dappled light through the palms, contented and happy",
    "beach_dawn": "dawn, soft gold light rays breaking through blue haze, peaceful, hopeful, merciful",
    "island_lane_night": "deep blue night with stars, the only light a warm golden glow streaming from an open door, hope in darkness",
    "old_madinah": "first light of dawn, pale gold and grey, hazy, slightly desaturated, soft vignette, hushed and reverent",
    "mosque_night": "night, warm amber lamplight, deep emerald and teal shadows, hushed, prayerful awe",
    "mosque_dawn": "dawn, soft gold light through the arched windows, calm, serene, steadfast",
    "mosque_soft": "warm golden light from above, hazy, slightly desaturated, soft vignette, reverent and timeless",
    "lagoon_bridge": "dusk, the sky divided between warm gold on the left and cool silver moonlight on the right, still water, delicate balance",
    "night_beach": "deep blue night, countless stars and a luminous Milky Way, faint starlight on the sand and water, quiet wonder",
    "minaret": "pre-dawn, deep blue sky, one brilliant star directly above the minaret, mirror-still water, solemn and pure",
    "office_night": "late night, cold blue city light and the hard white glow of a desk lamp, tense, lonely, driven",
    "home_room": "early morning, warm golden sunlight bursting into a dim room, glowing dust motes, searching and reflective",
    "atoll_night": "night, moonlight on the lagoon, every mosque glowing with warm lamplight, unity and peace",
    "open_sea": "dusk, an immense sky of fading gold and deep blue, humbling and solitary",
    "storm_house": "stormy night, cool storm-grey and deep blue, the warm steady glow of a single window, protection amid danger",
    "island_lane_dawn": "dawn, soft white morning mist, the first golden light ahead, a hopeful beginning",
    "night_road": "dark rainy night, cool blue mist, the small warm glow of a lantern, uncertainty and steadfastness",
    "dawn_road": "sunrise, bright clear golden light, open and hopeful, walking together",
    "sirat": "the hereafter: dark misty depths, a brilliant white-gold light at the far end, awe and warning, only a faint far red glow below",
}

BEATS = [
    dict(to=2, reason="opening: in this world Allah's dominion is seen only behind the veil of natural laws", loc="veil_world",
         visual="a small Maldivian island at sunrise seen from the lagoon through an immense translucent veil of fine golden gauze that hangs across the whole sky like a curtain; behind it the sun rising, rain falling from a distant cloud over the sea, palms swaying, everything softened and half-hidden by the shimmering veil; no people",
         camera="wide shot, the veil and the rising sun in the upper two-thirds, the still lagoon as a calm lower third", amb="dawn_exterior"),
    dict(to=3, reason="new image: on that Day the veils are torn away (the hereafter)", loc="plain",
         visual="the immense translucent golden veil torn wide open down the middle, blinding white-gold light pouring through the opening onto a vast empty plain beyond, torn shreds of the gauze lifting in the wind; no people",
         camera="wide shot, the opening in the upper two-thirds, the empty plain as the lower third", amb="vast_plain",
         transition="dissolve", sens="hereafter", safe="the Day of Judgement shown only as a torn veil and blinding light over an empty plain"),
    dict(to=5, reason="new example: what people wish for in life - happiness, wealth, long life", chars=["elder", "son", "mother"], loc="veranda",
         visual="a happy, prosperous family afternoon on the veranda: the old grandfather sitting content on a wooden swing chair, smiling, his small grandson laughing and leaning against his knee; the young mother standing a little apart, setting a dish of food on the low table full of dishes and fruit, smiling at them",
         camera="medium wide shot, eye level, faces in the upper half, the tiled veranda floor as the lower third", amb="island_house_day",
         transition="dissolve"),
    dict(to=6, reason="new image: some will wish to be dust - the terror of that Day", loc="plain",
         visual="fine pale dust lifting off the ground of the vast empty plain in long drifting streams, carried by the wind into the blinding white-gold sky, a lone small mound of dust slowly scattering; no people",
         camera="low wide shot, the dust streams rising into the upper two-thirds", amb="vast_plain",
         transition="dissolve", sens="hereafter", safe="'would that I were dust' shown only as dust blown across an empty plain; no crowds or faces"),
    dict(to=7, reason="topic turn: not despair - ar-Rahman ar-Rahim, mercy comes first", loc="beach_dawn",
         visual="the first golden rays of the sun breaking over the calm turquoise lagoon, warm light flooding across the water and the palm-lined beach, a small white mosque among the palms glowing softly; no people",
         camera="wide shot, the sunrise and palms in the upper two-thirds, the still shallow water as a calm lower third", amb="beach_day",
         transition="dissolve"),
    dict(to=8, reason="new image: the door of repentance is still open", loc="island_lane_night",
         visual="a tall arched wooden door standing wide open at the far end of the dark sandy lane, warm golden light streaming out of it and spreading across the sand towards the viewer; everything else in deep blue night under the stars; no people",
         camera="eye-level shot down the lane, the glowing doorway in the upper half, the lit sand as the lower third", amb="island_night"),
    dict(to=10, reason="new image: the scales of the reckoning are not yet set up (the hereafter)", loc="plain",
         visual="a great empty two-pan balance scale made of soft white-gold light standing still and unused on the vast empty plain, both pans level and empty, waiting; fine dust drifting; no people",
         camera="wide shot, the scale centred in the upper two-thirds", amb="vast_plain",
         transition="dissolve", sens="hereafter", safe="the reckoning shown only as an empty balance scale of light; no judgement scene"),
    dict(to=13, reason="new story: Zainul Abidin turning pale at wudu (Ahl al-Bayt - objects only)", loc="old_madinah",
         visual="in a quiet courtyard beside the palm-trunk mosque at first light, an old brass ewer standing on the rim of a rough stone wudu basin, clear water drops falling from its spout into the basin, the wet stones glistening, a pair of plain leather sandals left at the mosque threshold behind; no people anywhere, no hands",
         camera="close-up at low height, the ewer and falling drops in the upper two-thirds, the wet stone ground as the lower third", amb="old_madinah_day",
         transition="dissolve", sens="sacred_figure",
         safe="Zainul Abidin (of the Prophet's family) is never shown: only his ewer, the wudu basin and sandals at the threshold"),
    dict(to=15, reason="new image: prayer as the meeting with Allah - the place of the prayer, empty", loc="old_madinah",
         visual="inside the simple mosque of palm-trunk pillars, an empty woven palm-fibre prayer mat on the sandy floor facing a plain qibla wall, a pale shaft of dawn light falling through the palm-frond roof onto the empty mat, a small clay oil lamp glowing beside it; no people anywhere",
         camera="medium wide shot, slightly elevated, the light shaft in the upper two-thirds, the sandy floor as the lower third", amb="old_madinah_day",
         sens="sacred_figure", safe="the one who stands in prayer is not shown; only the empty mat in a shaft of light"),
    dict(to=17, reason="new image: the listener's heart trembling in prayer", chars=["listener"], loc="mosque_night",
         visual="the listener wearing a white crocheted prayer cap standing alone in prayer on a prayer rug, right hand over left on his chest, eyes lowered, his face solemn and moved, seen three-quarters from behind and to the side, facing the plain mihrab niche; barefoot on the rug",
         camera="medium shot, eye level, his head and shoulders in the upper half, the rugs as the lower third", amb="mosque_interior",
         transition="dissolve"),
    dict(to=19, reason="new metaphor: every step on a narrow bridge between mercy and justice", chars=["listener"], loc="lagoon_bridge",
         visual="the listener seen from behind walking carefully along the very narrow wooden footbridge stretching far across the calm open lagoon; the sky to the left glows warm gold, the sky to the right glows cool silver-blue moonlight; his figure small in the centre of the frame",
         camera="wide shot from behind, the bridge leading into the distance, the still water as the lower third", amb="beach_dusk"),
    dict(to=21, reason="new image: the strongest station - steady, grateful, awake", loc="mosque_dawn",
         visual="a single brass oil lamp burning with a perfectly steady upright flame inside the plain mihrab niche, rows of empty prayer rugs leading towards it, soft dawn light from the arched windows; no people",
         camera="eye-level shot along the rugs towards the mihrab, the lamp in the upper half", amb="mosque_dawn"),
    dict(to=23, reason="return: you now stand before Allah in prayer", reuse="beat_010", loc="mosque_night",
         visual="the listener standing in prayer (reuse)", amb="mosque_interior"),
    dict(to=27, reason="new chapter: worship and divine help - from speaking about Him to speaking to Him", chars=["listener"], loc="night_beach",
         visual="the listener sitting alone on the cool sand of the beach at night, seen from behind, gazing up at an immense sky full of stars and a luminous Milky Way, the calm lagoon reflecting the starlight",
         camera="wide shot from behind and slightly below, the sky filling the upper two-thirds, the sand as the lower third", amb="beach_evening",
         transition="black"),
    dict(to=29, reason="new image: 'Iyyaka na'budu wa iyyaka nasta'in' - addressing Him directly", chars=["listener"], loc="mosque_night",
         visual="close-up of the listener seated on a prayer rug, wearing a white crocheted prayer cap, both palms raised together at chest height in dua, eyes lowered, warm lamplight on his face and hands, a soft beam of light falling from a high window above",
         camera="medium close-up, eye level, face and hands in the upper two-thirds", amb="mosque_interior"),
    dict(to=32, reason="new image: 'You alone' - the peak of tawhid", loc="minaret",
         visual="a solitary slender white minaret rising against the deep blue pre-dawn sky, one brilliant star shining directly above it, its reflection perfectly still in the lagoon below; no people",
         camera="low wide shot, the minaret and star in the upper two-thirds, the mirror-like water as the lower third", amb="island_night"),
    dict(to=34, reason="new example: servitude to money, approval and desire", chars=["powerful_man"], loc="office_night",
         visual="the powerful man alone at night hunched over his large polished desk, only neat stacks of plain blank banknotes and a glowing phone in front of him (no books, no boxes, nothing else on the desk), his face tense and hungry, his huge shadow cast on the wall behind him; the cold city lights beyond the glass",
         camera="medium shot, slightly high angle, his face in the upper half, the polished desk as the lower third", amb="city_night_far"),
    dict(to=38, reason="new example: ask yourself on waking - whom do you serve? (and the cleansing of the inner idols)", chars=["listener"], loc="home_room",
         visual="the listener at dawn in a plain grey long-sleeved t-shirt and dark trousers, just risen, pushing open the wooden shutters of his room; warm sunlight bursts into the dim room and a cloud of old dust motes swirls and dissolves in the bright beam; his face thoughtful and questioning",
         camera="medium shot, eye level, his face and the window in the upper half, the woven mat on the floor as the lower third", amb="room_day",
         sens="other", safe="'idols inside the heart' shown as old dust dissolving in sunlight; no idols"),
    dict(to=40, reason="new image: 'we' not 'I' - the whole ummah, never alone", loc="atoll_night",
         visual="a high aerial view of the atoll at night, many small islands scattered across the dark moonlit lagoon, each with a small white mosque glowing with warm lamplight, all the lights together forming a gentle constellation on the water; no people visible",
         camera="high aerial wide shot, the islands in the upper two-thirds, open dark water as the lower third", amb="island_night"),
    dict(to=42, reason="new image: man is a needy creature - worship sets the direction, help reveals weakness", chars=["listener"], loc="open_sea",
         visual="the listener alone in a small wooden dhoni far out on the vast open ocean, seen from a distance and slightly behind, sitting still and looking up at the enormous sky; a tiny boat on endless water",
         camera="extreme wide shot, the sky in the upper two-thirds, open water as the lower third", amb="sea_boat"),
    dict(to=43, reason="return: 'I can manage on my own' - the self-reliant man is ruined", reuse="beat_017", loc="office_night",
         visual="the powerful man at his desk (reuse)", amb="city_night_far"),
    dict(to=45, reason="new image: seeking help shatters arrogance - prostration", chars=["listener"], loc="mosque_night",
         visual="the listener in prostration on a prayer rug, seen from the side at a modest distance, forehead and palms on the rug, wearing a white crocheted prayer cap, a single brass lamp glowing nearby, the dark quiet mosque hall around him",
         camera="medium wide shot from the side, low angle, the lamp and pillars rising into the upper half", amb="mosque_interior"),
    dict(to=46, reason="return: is your asking for help real? hands raised in dua", reuse="beat_015", loc="mosque_night",
         visual="the listener in dua (reuse)", amb="mosque_interior"),
    dict(to=48, reason="new image: help against the self, Shaytan and the trials of the world", loc="storm_house",
         visual="a small island house at night in a fierce storm, tall coconut palms bending in the wind, rain slanting; one window glows with a warm, perfectly steady lamp; dark smoky storm clouds press low over the roof but curl back and recoil from the window's light; no people",
         camera="wide shot, eye level, the lit window and the recoiling clouds in the upper two-thirds, the wet sand as the lower third", amb="storm_night",
         sens="other", safe="Shaytan is never a figure: only dark smoky clouds recoiling from the light (rule 3)"),
    dict(to=51, reason="new image: worship before help - turning your face towards Allah first", chars=["listener"], loc="beach_dawn",
         visual="the listener at dawn standing on a small prayer mat on the sand, seen from behind, both hands raised beside his ears in the opening takbir, wearing a white crocheted prayer cap, facing the glowing horizon across the calm lagoon; his sandals left on the sand beside the mat",
         camera="medium wide shot from behind, his figure and the sunrise in the upper two-thirds, the sand as the lower third", amb="beach_day",
         transition="black"),
    dict(to=53, reason="new image: the verse at the exact centre of the seven verses", loc="mosque_night",
         visual="seven small brass oil lamps standing in a straight row on a carved dark wooden ledge below the plain mihrab, the central fourth lamp burning brightest and tallest, its golden light reaching the three lamps on either side; no people",
         camera="eye-level medium shot, the row of lamps in the upper half, the dark wood ledge and rugs as the lower third", amb="mosque_interior"),
    dict(to=55, reason="new image: the Hadith Qudsi - the prayer divided into two halves", loc="mosque_soft",
         visual="an open mushaf on a carved wooden rehal resting on a prayer rug, seen at an angle, its two pages showing only soft blurred golden ornament with no letters; a warm beam of light from above divides the two pages, the right page bathed in gold, the left in gentle silver-blue",
         camera="close-up, slightly high angle, the mushaf in the upper half, the rug as the lower third", amb="mosque_interior",
         transition="dissolve", sens="sacred_figure",
         safe="the words of Allah in the hadith are illustrated only by an open mushaf with blurred ornament, no letters"),
    dict(to=58, reason="new topic: the dua begins - 'guide us to the straight path' while already in prayer", loc="mosque_dawn",
         visual="a dawn congregation seen from behind: rows of men in white kurtas and white caps standing shoulder to shoulder in perfectly straight rows, all facing the plain mihrab, soft dawn light through the arched windows",
         camera="wide shot from the back of the hall, slightly elevated, the rows in the upper two-thirds, the rugs as the lower third", amb="mosque_dawn",
         transition="dissolve"),
    dict(to=61, reason="new section: the straight path - humanity's greatest need", chars=["listener"], loc="island_lane_dawn",
         visual="the listener standing at the beginning of a long straight sandy lane at dawn, seen from behind, the lane stretching ahead into soft white morning mist between coral-stone walls and palms, the first golden light glowing ahead",
         camera="wide shot from behind at eye level, the lane vanishing into the light in the upper half, the sand as the lower third", amb="dawn_exterior",
         transition="black"),
    dict(to=63, reason="new image: guidance is a long journey on a road that may be slippery and dark", chars=["listener"], loc="night_road",
         visual="the listener walking alone at night along the long narrow road, seen from behind, holding a small glowing lantern; the road is wet and slippery after rain, mist drifts, dark side tracks branch off on either side",
         camera="medium wide shot from behind, the lantern light in the upper half, the wet road as the lower third", amb="rain_night"),
    dict(to=65, reason="new image: 'guide us' - the whole ummah together on the wide, clear road", chars=["listener"], loc="dawn_road",
         visual="many travellers walking together along the broad clear straight road towards the bright sunrise, seen from behind and at a distance: men, elders and women in loose dresses with hijabs; the listener in his off-white kurta walking among them in the foreground",
         camera="wide shot from behind, the road and the sunrise in the upper two-thirds, the pale sand road as the lower third", amb="island_day"),
    dict(to=68, reason="new image: the Sirat of the hereafter - a thin bridge over Hell", loc="sirat",
         visual="a thin bridge of light, narrow as a thread, stretching across a vast dark misty abyss towards a distant brilliant white-gold light; far below in the mist only a faint distant red glow; no people",
         camera="wide shot, the bridge rising from the lower left into the light in the upper right, dark mist as the lower third", amb="vast_plain",
         transition="dissolve", sens="hereafter",
         safe="the Sirat over Hell shown only as a thin glowing bridge over a misty abyss with a faint far red glow; no people, no fire"),
    dict(to=70, reason="new image: 'mustaqim' - no leaning; ask for the straight path in every rak'ah", chars=["listener"], loc="mosque_dawn",
         visual="the listener bowing in ruku' on a prayer rug, seen from the side, his back perfectly flat and horizontal like a table top, parallel to the floor, his head level with his back (not drooping), arms straight with palms on his knees, legs straight, wearing a white crocheted prayer cap; a beam of soft dawn light from an arched window falling along his straight back",
         camera="medium shot from the side, eye level, the figure in the upper half, the rugs as the lower third", amb="mosque_dawn",
         transition="dissolve"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "On that Day, Allah's kingship and ownership will not be seen indirectly. It will be seen with a perfectly clear, direct sight.")
sh(2, "In this world we see His dominion only from behind a veil. The laws of nature, causes and their effects, are like veils.")
sh(3, "But on that Day those veils will be torn away, and everyone will see the truth. On that Day there will be people who say, 'Would that I were dust!'",
   [("wind_gust", "ކަހައިލެވޭނެއެވެ", -22)])
sh(4, "The Qur'an uses this very expression. Reflect on it deeply. What does a person wish for while alive? Happiness,")
sh(5, "wealth and a long life. But on that Day some people will wish to become dust. Because, in the terror of that Day,")
sh(6, "being nothing at all will feel so much lighter. Does this not bring fear into your hearts? It should frighten you.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -24)])
sh(7, "But it is not despair. Because before this verse come two verses: 'Ar-Rahman ar-Rahim.' Allah is the Most Merciful, the Most Compassionate.",
   hum=True)
sh(8, "And you have not yet met that Day. You are still in this world. The door of repentance is still open.",
   [("door_open", "ދޮރު", -22)])
sh(9, "The scales that will weigh your account have not yet been set up. The verse 'Maliki yawmid-din' reminds us that that Day will come,")
sh(10, "that the true Owner will be known, that the reckoning will be taken. But this verse did not come to destroy you.")
sh(11, "It came to wake you up. There was a man whose face turned white and pale whenever he made wudu: Zainul Abidin, may Allah be pleased with him.",
   [("pour", "ވުޟޫކުރައްވާއިރު", -22)])
sh(12, "People asked him: 'Why does your face change so much?' He answered: 'Do you know")
sh(13, "before Whom I am preparing to stand?' It was only wudu - only getting ready for prayer.")
sh(14, "But to him it was the preparation for the greatest meeting there could ever be, because he knew that prayer is meeting Allah,",
   hum=True)
sh(15, "and that the One before Whom he was about to stand was the Most Merciful, the Most Compassionate, the Master of the Day of Judgement.")
sh(16, "Whoever truly knows these three attributes will feel his heart tremble with awe in prayer. At first, perhaps, that awe may not arise.",
   [("heartbeat", "ތެޅޭނެއެވެ", -24)])
sh(17, "You may see no change at all. But once you begin to accept the meaning of this surah from the depths of your heart, changes will begin to come with every prayer.")
sh(18, "Because Allah is the Lord of endless mercy, and He is the Lord of perfect justice.")
sh(19, "Every day, every step you take is on a narrow bridge between these two truths. 'Al-hamdu lillahi Rabbil-'alamin, ar-Rahmanir-Rahim,")
sh(20, "Maliki yawmid-din' - praise, mercy and the reckoning: together these three describe the strongest station a human being can stand in:")
sh(21, "a station without despair and without heedlessness - grateful, secure and awake. Now,")
sh(22, "as a servant who has learnt these three attributes, you stand before Allah. We have felt His majesty.")
sh(23, "We have come to know His mercy. We have remembered that there will be a reckoning. Now is the time to speak to Him - the time for true, intimate supplication.")
sh(24, "Worship and divine help. In the first three verses of the surah we spoke about Allah, Glorified and Exalted is He.")
sh(25, "All praise belongs to Him. Mercy comes from His presence. And the reckoning belongs to Him alone.")
sh(26, "At this point a change has come. Now it is no longer speaking about Him in the third person.")
sh(27, "Instead of saying 'He is such-and-such a Lord', we now address Him directly.")
sh(28, "'Iyyaka na'budu wa iyyaka nasta'in' - 'You alone we worship, and from You alone we seek help.' This verse is the heart of Surah al-Fatiha.",
   [("whisper_recite", "އަޅުކަންކުރަނީ", -26)], hum=True)
sh(29, "By now you have come to know Allah. What remains is to define your own place. In the usual word order of an Arabic sentence,")
sh(30, "one could say 'na'buduka' - 'we worship You'. But changing the order in this verse and saying 'Iyyaka na'budu' puts all the emphasis on the One addressed.")
sh(31, "That is: no one else - You alone. This is a declaration. It is a word of faith. And it is a word of separation.")
sh(32, "With this verse, tawhid reaches its highest level. Because the greatest error a human being can fall into is dividing his worship.")
sh(33, "Living to chase money, toiling for people's approval, blindly obeying the desires of the self - these too are forms of servitude.")
sh(34, "Surah al-Fatiha tells you that you will be a servant either of Allah or of something else. There is no middle ground between the two.")
sh(35, "Now ask yourself: when you wake in the morning, whom do you really serve? What is the root of everything you do?")
sh(36, "Whom do you fear most? Whom do you most want to please? If a person fears people more than Allah,")
sh(37, "trusts money more than Allah, or blindly follows his own desires, then his tawhid has been damaged.")
sh(38, "'Iyyaka na'budu' is a purification. This sentence wipes away the idols inside a person's heart. And notice: here it says 'na'budu' - 'we worship',")
sh(39, "not 'I worship'. This is the feeling of the ummah. Even if you stand alone in prayer, you speak together with all the believers.")
sh(40, "It reminds you that you are not alone. Then comes 'wa iyyaka nasta'in' - 'and from You alone we seek help.' Worship and seeking help are brought together.")
sh(41, "Why is that? Because a human being is not only a creature that worships; he is also a creature full of needs.")
sh(42, "Worship sets your direction, and seeking help reveals your weakness. This verse teaches you to pledge yourself to worship Allah,")
sh(43, "and at the same time to admit that you cannot do it alone. This is humility of the highest degree. When a person says 'I can manage on my own', he is ruined.")
sh(44, "But when he says 'I seek Your help', he is protected. This verse shatters arrogance,")
sh(45, "because seeking help is admitting one's weakness. When you recite this verse in prayer, reflect deeply. Are you truly asking for help?")
sh(46, "Or are you just saying words? When you say 'wa iyyaka nasta'in', what you are really saying is: 'O my Lord!")
sh(47, "Help me against my own self. Help me to be safe from Shaytan.",
   [("wind_gust", "ޝައިޠާނާގެ", -22)])
sh(48, "Help me to come safely through the trials of this world. And help me to worship You in the most perfect way.'",
   [("thunder", "އިމްތިޙާނުތަކުން", -24)])
sh(49, "This is the most honest confession between the servant and Allah: 'I want to worship You, but without Your help I cannot.'",
   hum=True)
sh(50, "There is another secret here. Why does worship come before seeking help? Because a direction must be chosen before help is sought.")
sh(51, "You cannot ask for help without first turning your face towards Allah. First you say, 'I worship You alone'; then you say, 'I seek help from You alone.'")
sh(52, "This is a covenant. This verse stands exactly in the middle of Surah al-Fatiha - the middle of its seven verses. The whole surah seems to flow towards this point.")
sh(53, "The outcome of praise, mercy and the reckoning is servitude. Did you notice? The first part of Surah al-Fatiha describes Allah.")
sh(54, "The second part is the servant's dua. This verse stands between the two. That is why a Hadith Qudsi says: 'I have divided the prayer (Surah al-Fatiha) between Myself and My servant into two halves.",
   hum=True)
sh(55, "The first half is for Allah, and the second half is for the servant.' This verse is the turning point from one side to the other.")
sh(56, "Now the dua begins. Having declared our servitude and asked for help, we now ask for the straight path.")
sh(57, "'Ihdinas-siratal-mustaqim' - 'Guide us to the straight path!' What guidance are we asking for?",
   [("whisper_recite", "މަގުދައްކަވާނދޭވެ", -26)])
sh(58, "Are we not Muslims already? Are we not already standing in prayer? The depth of this dua will become clear in what follows.")
sh(59, "Servitude has been declared, weakness has been admitted, and now the dua has begun. The straight path:")
sh(60, "this verse reveals the greatest need of a human being. Think about it carefully. We are asking to be shown the straight path.")
sh(61, "Yet we are already in Islam, already reciting al-Hamd in our prayer. So why do we still say, 'Guide us to the straight path'?")
sh(62, "Because guidance is not a certificate you receive once and for all. It is a long journey without a break. Even when a person is on the straight path,",
   [("footsteps_sand", "ދަތުރެކެވެ", -24)])
sh(63, "he needs help at every moment to stay firm on it. The road may be slippery, or dark and full of confusion.")
sh(64, "When we say 'Ihdina' - 'guide us' - the plural is used. Saying 'guide us' instead of 'guide me' makes it a collective prayer in the name of the whole ummah.")
sh(65, "Now let us look at the word 'as-Sirat'. A sirat is not just a straight road. It is a wide, clear,")
sh(66, "open road that does not make you slip or lose your way. Elsewhere in the Noble Qur'an, the Sirat is described as a thin bridge stretched over Hell.",
   [("wind_howl", "ނަރަކައިގެ", -26)], hum=True)
sh(67, "This means that the sirat of this world is the preparation for the Sirat of the hereafter. The way you walk in this world")
sh(68, "will decide how you cross that bridge in the hereafter. Then comes 'al-mustaqim'. It means a road with no crookedness of any kind,")
sh(69, "with no leaning to the right or to the left - a perfectly straight road. But human nature sometimes leans towards excess or heedlessness,")
sh(70, "towards fear or towards arrogance. That is why we must pray for the straight path in every rak'ah.", hum=True)
SHOTS = S

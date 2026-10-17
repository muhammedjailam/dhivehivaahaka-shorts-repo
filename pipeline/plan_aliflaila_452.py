"""Beat/shot plan for Aliflaila episode 452 (Night 1) - used by plan_beats.py.
Frame story from the beginning: King Shahryar and his brother Shah Zaman, the two betrayals (NOTHING of the adultery
shown, the lovers never depicted - bible rule 2), Shah Zaman's killing and the executions only as symbols (rule 1),
Shahryar's law as symbols (rule 3), Shahrazad volunteers, coaches Dunyazad; the wedding night as a modest frame scene
with Dunyazad present (rule 4); the tale of the Merchant and the Jinni begins (jinni empty-handed, never a sword);
dawn cliffhanger, the king spares her for one day.
Rules: no swords/daggers/knives anywhere; every woman and girl in a headscarf fully covering hair and neck; no bed
shown; no text anywhere."""

NOSWORD = "no sword, no dagger, no weapon anywhere, empty hands"
SHAH = "Shahrazad in her saffron-gold gown and ivory headscarf fully covering her hair and neck"
DUNYA = "little Dunyazad in her lavender gown and pale pink headscarf fully covering her hair and neck"
KING = "King Shahryar in his crimson-and-gold plumed turban and bronze brocade coat"
SZ = "Shah Zaman in his emerald-green turban and emerald brocade coat"
JINN = ("the giant jinni with a swirling charcoal-smoke lower body, dark-red robe and turban, glowing ember-orange eyes "
        "and two short tusk-like teeth jutting from his black beard, both enormous hands completely empty")
NOBODY = "no other people visible"

LOC = {
    "empire": "the vast Sasanian empire seen from a high palace balcony of white and sand-coloured stone with onion domes: "
              "endless golden desert dunes, a green river valley with palm groves, snowy mountains on the horizon",
    "samarkand": "the sunlit throne hall of the palace of Samarkand: turquoise-tiled arches, emerald silk hangings, a "
                 "carved throne on a dais, a large arched window over the blue domes of Samarkand",
    "courtyard": "the great sunlit courtyard of King Shahryar's palace seen from an upper arched gallery: a long caravan "
                 "of camels and fine horses laden with chests, rolls of silk and incense, palms and fountains",
    "pavilion": "a grand striped royal pavilion tent outside the walled city gate of Samarkand, rows of smaller army "
                "tents, tethered horses and banners without any emblems",
    "sz_corridor": "a moonlit marble corridor inside the palace of Samarkand at midnight, tall arches, carved lattice "
                   "windows letting in silver moonlight stripes, a carved wooden door at the end",
    "sz_doorway": "the threshold of a royal chamber in the palace of Samarkand at night, a heavy silk curtain drawn across "
                  "the doorway hiding the room entirely",
    "sz_floor": "a white marble floor and a closed carved wooden door inside the dark palace of Samarkand at midnight",
    "capital": "the festive capital of King Shahryar: a broad avenue of white houses decorated with silk banners, garlands "
               "and lanterns leading to the golden palace gate, rose petals in the air",
    "guest_room": "a richly furnished guest chamber in King Shahryar's palace by day: cushioned divan, Persian carpets, "
                  "silk curtains, a low brass table",
    "guest_window": "a carved wooden lattice window screen in the guest wing of the palace, overlooking a lush palace "
                    "garden with date palms, cypresses and a marble fountain far below",
    "throne_hall": "King Shahryar's vast throne hall: marble columns, a golden throne on a dais, tall arched windows, "
                   "brass lanterns",
    "garden_dawn": "an empty marble pavilion in the palace garden at grey dawn, a still fountain, dark cypresses",
    "city_square": "a city square below the palace walls in the capital, white houses with arched doors, a broad stone "
                   "stair, a crowd of townspeople",
    "palace_ext": "the long facade of King Shahryar's palace at night with a row of many arched windows",
    "city_gate": "the great arched city gate of the capital at night, the desert road leading away into moonlit dunes",
    "vizier_room": "a dim private study in the Grand Vizier's house at night, a single candle on a low table",
    "library": "Shahrazad's private library in the Grand Vizier's house: tall carved wooden shelves full of closed "
               "leather-bound books and rolled scrolls, a reading cushion, an arched window",
    "hearth": "the main room of the Grand Vizier's house at night: a glowing hearth fire, cushions and carpets, brass "
              "lantern",
    "alcove": "a quiet window alcove in the Grand Vizier's house, a lattice window with moonlight, silk cushions",
    "wedding": "King Shahryar's throne hall at night lit for a quiet wedding: hundreds of brass lanterns, rose petals on "
               "the carpet, silk drapes",
    "chamber": "King Shahryar's royal bedchamber (the series' frame setting): an arched lattice window showing a moonlit "
               "city of domes under a huge moon, brass lanterns, Persian carpets, a long cushioned divan, silk curtains; "
               "no bed visible",
    "chamber_dawn": "King Shahryar's royal chamber at dawn: the arched lattice window shows the city of domes and distant "
                    "slender minaret silhouettes against a golden sunrise sky, brass lanterns going pale, Persian "
                    "carpets, a cushioned divan",
    "desert_road": "a city gate opening onto a long desert road between dunes, palm trees at the edge of the city",
    "spring": "a clear spring of water in the desert under a huge old shade tree, grass and bushes around it, dunes "
              "shimmering in the heat",
    "sandstorm": "the desert around the shade tree and spring, now in a sudden violent swirl of sand and icy wind, the "
                 "ground cracked open",
    "court_day": "King Shahryar's throne hall by morning, courtiers waiting",
    "vizier_door": "an arched doorway of the palace opening onto a sunlit courtyard in the morning",
}
MOOD = {
    "empire": "bright morning, golden sunlight and turquoise sky, majestic and peaceful",
    "samarkand": "warm golden afternoon light, serene and dignified",
    "courtyard": "bright midday sun, glittering silks and gold, hopeful anticipation",
    "pavilion": "rose and amber evening sky, joyful bustle of departure",
    "sz_corridor": "midnight, cold silver moonlight and deep blue shadows, hushed and secretive",
    "sz_doorway": "midnight, faint moonlight and deep shadows, sudden shock and heartbreak",
    "sz_floor": "midnight, cold moonlight on marble, deep shadows, tragic stillness",
    "capital": "bright festive daylight, colourful banners, but a sad heavy note on one face",
    "guest_room": "pale afternoon light, melancholy and worry",
    "guest_window": "bright daylight outside, the viewer in shadow, shock",
    "throne_hall": "late afternoon, dark storm clouds gathering outside the windows, harsh shadows, fury",
    "garden_dawn": "grey overcast dawn, mist, cold and mournful",
    "city_square": "harsh grey daylight, dread and disbelief",
    "palace_ext": "deep midnight blue, a pale moon, grief and dread",
    "city_gate": "moonlit night, silver light and long shadows, sorrow and flight",
    "vizier_room": "night, the single candle's warm small glow against deep shadow, despair",
    "library": "warm late-afternoon sunbeams with floating dust sparkles, wonder and intelligence",
    "hearth": "night, warm orange firelight against deep blue shadows, tense family drama",
    "alcove": "night, cool silver moonlight and one small lantern, tender secrecy",
    "wedding": "night, warm amber lantern glow, solemn and quietly fateful",
    "chamber": "deep midnight blue night with warm amber lantern light and a huge moon, tense intimacy of storytelling",
    "chamber_dawn": "dawn, soft golden rays streaming through the lattice window, hope and suspense",
    "desert_road": "early morning, golden light, long shadows, adventure",
    "spring": "blazing midday sun, shimmering heat haze, the cool green shade under the tree",
    "sandstorm": "the sky suddenly darkened, swirling ochre sand, cold blue-grey storm light, magical dread",
    "court_day": "bright morning sunlight through tall windows, ordinary daily business",
    "vizier_door": "fresh bright morning light, relief and joy",
}

BEATS = [
    # ---------------- FRAME PROLOGUE: the two kings ----------------
    dict(to=4, reason="episode opening: King Shahryar and his vast just kingdom", chars=["shahryar"], loc="empire",
         visual=f"{KING} standing tall on a high palace balcony with one open hand resting on the stone balustrade, "
                f"calm wise face gazing over his sweeping kingdom of dunes, valleys and mountains, a gentle confident "
                f"smile, silk banners rippling; {NOSWORD}",
         camera="wide shot from slightly behind and to the side, the king in the upper half, the vista beyond",
         amb="palace_day"),
    dict(to=7, reason="new character and location: Shah Zaman, King of Samarkand", chars=["shah_zaman"], loc="samarkand",
         visual=f"{SZ} seated on his carved throne in the turquoise-tiled hall of Samarkand, kind thoughtful expression, "
                f"one hand raised in a gentle gesture of justice, small respectful courtiers bowing far below; {NOSWORD}",
         camera="medium wide, low angle on the throne", amb="throne_hall"),
    dict(to=10, reason="action change: Shahryar longs for his brother and sends the Grand Vizier with a gift caravan",
         chars=["shahryar", "grand_vizier"], loc="courtyard",
         visual=f"{KING} on an upper gallery with a warm longing smile, gesturing towards the courtyard below where the "
                f"Grand Vizier in his deep-blue robe bows, ready to lead a long caravan of camels and fine horses laden "
                f"with chests, rolls of shimmering silk and incense burners trailing sweet smoke",
         camera="high wide shot, the two men in the upper third, the glittering caravan stretching below",
         amb="palace_day"),
    dict(to=12, reason="scene change: Shah Zaman accepts and camps outside Samarkand ready to travel",
         chars=["shah_zaman", "grand_vizier"], loc="pavilion",
         visual=f"{SZ} smiling joyfully, holding a small invitation scroll rolled closed with a ribbon, standing before "
                f"his grand striped royal pavilion; the Grand Vizier bowing beside him; army tents, horses and camels "
                f"ready for the journey behind them in the evening glow; {NOSWORD}",
         camera="medium wide, eye level", amb="caravan_road"),
    dict(to=16, reason="time jump to midnight: Shah Zaman secretly returns alone to the palace for the forgotten gift",
         chars=["shah_zaman"], loc="sz_corridor", transition="black",
         visual=f"{SZ} walking alone and quietly down the moonlit marble corridor, holding a small ornate jewelled gift "
                f"box against his chest with both hands, a soft private smile, moonlight stripes from the lattice "
                f"windows across his face; {NOBODY}",
         camera="medium wide, from slightly ahead of him, the corridor receding behind", amb="palace_night"),
    dict(to=19, reason="emotional turning point: Shah Zaman discovers his wife's betrayal (nothing of it shown)",
         chars=["shah_zaman"], loc="sz_doorway",
         visual=f"close-up of {SZ} frozen at a doorway that is completely covered by a heavy drawn silk curtain, his eyes "
                f"wide with shock and heartbreak, lips parted, the jewelled gift box slipping from his loosening "
                f"fingers; nothing of the room beyond is visible; {NOBODY}",
         camera="close-up on his face, slightly low angle", amb="palace_night", sens="other",
         safe="the wife's betrayal is never shown: only Shah Zaman's shocked face at a curtained doorway; the lover is "
              "never depicted"),
    dict(to=22, reason="symbol for Shah Zaman's killing of the two (bible rule 1) and his silent departure", loc="sz_floor",
         visual="the small jewelled gift box lying fallen on the cold white marble floor, its lid open, a few jewels "
                "spilled and glinting in a shaft of moonlight; beside it a brass lantern tipped over and blown out, a "
                "thin curl of smoke rising; behind, the heavy carved door firmly closed; no people at all, nothing red; "
                "painted as a flat hand-drawn animated-film background with visible gouache brush strokes, clean ink "
                "outlines and simple cel-shaded shapes, not photographic, not 3D-rendered",
         camera="low close shot along the marble floor, the closed door in the upper half", amb="palace_night",
         sens="violence", safe="the double killing and the blood on the marble are replaced by a dropped gift box, an "
                               "extinguished lantern and a closed door; no sword, no bodies, no blood"),
    dict(to=24, reason="scene change: arrival and festive welcome at Shahryar's capital",
         chars=["shahryar", "shah_zaman"], loc="capital",
         visual=f"{KING} stepping forward at the golden palace gate with both arms open in a joyful welcome, while "
                f"{SZ} dismounts from his horse with a pale, hollow, heartbroken face that cannot smile; colourful "
                f"banners, garlands and rose petals swirl around them, small cheering townspeople in modest clothes "
                f"in the background",
         camera="medium wide, eye level", amb="palace_day"),
    dict(to=28, reason="action change: Shah Zaman wastes away; Shahryar worries and plans a hunt",
         chars=["shah_zaman", "shahryar"], loc="guest_room",
         visual=f"{SZ}, thin and pale with dark circles under his eyes, sitting slumped on a divan staring at nothing, "
                f"a full tray of food untouched on the low brass table; {KING} standing a step away, leaning towards "
                f"him with a concerned brotherly face, gesturing towards the window and the hunting grounds beyond",
         camera="medium two-shot, eye level", amb="palace_day"),
    dict(to=32, reason="scene change: from the guest-wing window Shah Zaman sees the queen's betrayal (nothing shown)",
         chars=["shah_zaman"], loc="guest_window", sens="other",
         visual=f"{SZ} seen over his shoulder and from the side, standing in shadow behind a carved wooden lattice "
                f"window screen, one hand pressed to the lattice, his face frozen in astonishment; far below through "
                f"the lattice the palace garden is only a soft blur of palms, cypresses and a fountain, and NO people "
                f"are visible in the garden at all",
         camera="over-the-shoulder medium shot, his face in profile in the upper third",
         amb="palace_garden_day",
         safe="the queen, the servants and the lover in the garden are never shown: only Shah Zaman's astonished face "
              "behind a lattice screen and an empty, blurred garden"),
    dict(to=36, reason="emotional turning point: his grief lifts; he eats again and recovers",
         chars=["shah_zaman"], loc="guest_room",
         visual=f"{SZ} sitting by a sunlit window with colour back in his face, a calm, bitter-wise half smile, eating "
                f"bread and dates from the brass tray, his posture upright again; {NOBODY}",
         camera="medium shot, eye level", amb="palace_day"),
    dict(to=38, reason="characters change: Shahryar returns and his brother finally tells him the truth",
         chars=["shahryar", "shah_zaman"], loc="guest_room",
         visual=f"the two royal brothers seated facing each other on cushions in the evening lamplight, {KING} leaning "
                f"forward with a searching, puzzled frown, {SZ} with lowered eyes and one hand on his heart, reluctantly "
                f"confessing",
         camera="medium two-shot in profile, eye level", amb="palace_night"),
    dict(to=40, reason="action change: Shahryar secretly watches the garden and sees it himself (nothing shown)",
         chars=["shahryar"], loc="guest_window", sens="other",
         visual=f"{KING} half hidden behind the carved lattice window screen, his eyes widening in disbelief, his jaw "
                f"tightening; the garden below only a blurred green haze with a fountain, NO people visible in it",
         camera="close medium shot through the edge of the lattice, his face in the upper half",
         amb="palace_garden_day",
         safe="the queen's betrayal is never shown: only the king's face behind the lattice and an empty garden"),
    dict(to=42, reason="emotional turning point: love turns to hatred; the king orders the executions",
         chars=["shahryar"], loc="throne_hall",
         visual=f"{KING} standing before his golden throne, his face hardened like stone, eyes dark with fury, one arm "
                f"thrust out pointing in a cold command; dark storm clouds and a flash of lightning through the tall "
                f"windows; small courtiers bowing low far away; {NOSWORD}",
         camera="low angle medium wide, the king towering", amb="throne_hall", sens="violence",
         safe="the execution order is shown only as the king's commanding gesture and a storm; nobody is harmed"),
    dict(to=44, reason="symbol for the executed queen and servants (bible rule 2) and the king's madness",
         loc="garden_dawn",
         visual="the empty marble pavilion in the palace garden at grey misty dawn, abandoned silk cushions, a row of "
                "brass lanterns all extinguished with thin wisps of smoke, fallen rose petals on the marble steps, dark "
                "storm clouds over the domes; no people at all",
         camera="wide shot, the pavilion in the upper two-thirds, the still fountain basin as a calm lower third",
         amb="palace_dawn", sens="violence",
         safe="the executions are replaced by an empty pavilion with extinguished lanterns at grey dawn"),
    # ---------------- the law ----------------
    dict(to=46, reason="scene change: the cruel law is proclaimed to the city", loc="city_square",
         visual="a royal herald in a plain grey robe standing on the broad stone stair below the palace walls, holding "
                "up an unrolled blank parchment with no writing; below him a crowd of townspeople in modest clothes "
                "seen mostly from behind, recoiling in horror, fathers with hands raised to their heads, mothers in "
                "long dark cloaks with headscarves pulled low over the forehead, holding their young daughters close; "
                "every woman's and girl's headscarf wraps snugly over the whole forehead, hair and neck with not a "
                "single strand of hair showing",
         camera="wide shot from behind the crowd, the herald and palace walls in the upper half", amb="bazaar_day",
         sens="other", safe="the nightly marriage and beheading law is shown only as a proclamation and the crowd's "
                            "horror; no bride, no executioner, no weapon"),
    dict(to=48, reason="time jump: three years of the law, shown as lanterns going out night after night",
         loc="palace_ext", transition="black",
         visual="the long palace facade at night with a row of many arched windows; most windows are dark, and one "
                "single lantern in the nearest window is going out, a thin curl of smoke rising from it under the pale "
                "moon; no people visible",
         camera="wide shot, the row of windows in the upper two-thirds, dark palace steps as a calm lower third",
         amb="palace_night", sens="violence",
         safe="the brides and their executions = a row of extinguished lanterns, one going out (bible rule 3)"),
    dict(to=51, reason="scene change: the city in grief; families flee by night", loc="city_gate",
         visual="families leaving the capital through the great arched gate by moonlight with a few laden camels: "
                "fathers leading the camels, mothers in dark headscarves fully covering their hair and neck holding "
                "their daughters' hands, all looking back sadly at the city of domes; a huge pale moon",
         camera="wide shot, the gate and moon in the upper half, the moonlit sand road below", amb="city_lanes_night"),
    dict(to=53, reason="character focus: the Grand Vizier bears the burden of the killings", chars=["grand_vizier"],
         loc="vizier_room",
         visual="the Grand Vizier in his deep-blue robe sitting alone on a low cushion, elbows on his knees, his head "
                "buried in his empty hands, shoulders bowed in grief, a single candle beside him; nothing in his "
                "hands; no other people",
         camera="medium shot, eye level", amb="palace_night"),
    # ---------------- Shahrazad ----------------
    dict(to=58, reason="new characters: Shahrazad, the learned elder daughter, and Dunyazad",
         chars=["shahrazad", "dunyazad"], loc="library",
         visual=f"{SHAH} sitting gracefully on a reading cushion among towering shelves of closed books and rolled "
                f"scrolls, a closed leather book in her lap, gazing thoughtfully out of the arched window towards the "
                f"grieving city; {DUNYA} sitting on the carpet beside her looking up at her with admiring eyes; floating "
                f"golden dust sparkles in the sunbeam; every book closed, no writing anywhere",
         camera="medium wide, eye level", amb="palace_day"),
    dict(to=61, reason="time jump to one night: Shahrazad asks her weeping father to take her to the king",
         chars=["grand_vizier", "shahrazad"], loc="hearth", transition="black",
         visual=f"the Grand Vizier sitting beside the glowing hearth, tears on his cheeks; {SHAH} kneeling on the carpet "
                f"before him with one hand on her heart and the other gently raised, her face calm and resolute, her "
                f"large dark eyes steady; warm firelight on both faces",
         camera="medium two-shot, eye level, the fire glowing at the side", amb="palace_night"),
    dict(to=66, reason="action change: the Vizier recoils in horror; Shahrazad answers without fear",
         chars=["grand_vizier", "shahrazad"], loc="hearth",
         visual=f"the Grand Vizier half rising and recoiling backwards, both palms raised in horror, eyes wide; "
                f"{SHAH} still kneeling upright, unshaken, her chin raised, fearless dark eyes fixed on him, one hand "
                f"open in a calm argument; long firelit shadows on the wall",
         camera="medium wide, slightly low angle", amb="palace_night"),
    dict(to=68, reason="emotional turning point: the Vizier gives in, weeping, and prays for his daughter",
         chars=["grand_vizier", "shahrazad"], loc="hearth",
         visual=f"the Grand Vizier sitting exhausted by the dying embers, tears streaming into his white beard, both "
                f"palms raised upward in prayer, eyes lifted; {SHAH} sitting quietly beside him with her head bowed",
         camera="medium shot, eye level", amb="palace_night"),
    dict(to=72, reason="scene and character change: Shahrazad secretly coaches Dunyazad",
         chars=["shahrazad", "dunyazad"], loc="alcove",
         visual=f"{SHAH} kneeling close to {DUNYA} in a moonlit window alcove, holding the little girl's trembling hands "
                f"in both of hers and whispering earnestly; Dunyazad's big eyes wide with fear and attention",
         camera="medium close two-shot, eye level", amb="palace_night"),
    dict(to=75, reason="emotional turning point: Dunyazad, in tears, nods bravely",
         chars=["dunyazad", "shahrazad"], loc="alcove",
         visual=f"close-up of {DUNYA}, tears glistening in her big eyes, nodding bravely with a trembling determined "
                f"mouth; {SHAH}'s hand gently resting on her shoulder at the edge of the frame",
         camera="close-up, slightly high angle", amb="palace_night"),
    # ---------------- the wedding night (frame) ----------------
    dict(to=77, reason="time jump to that night: the Vizier hands Shahrazad over to the king (modest wedding)",
         chars=["shahryar", "shahrazad", "grand_vizier"], loc="wedding", transition="black",
         visual=f"{KING} seated on his golden throne in the lantern-lit hall, his stern face softening for one moment "
                f"as he looks at {SHAH} who stands a few steps below the dais with lowered eyes and hennaed hands "
                f"folded; the Grand Vizier stands beside her with a heavy grieving face, one hand presenting her; rose "
                f"petals on the carpet; a respectful distance between the king and her; {NOSWORD}",
         camera="wide shot, eye level, the throne in the upper half", amb="throne_hall", sens="intimacy",
         safe="the wedding shown as a modest lantern-lit presentation in the throne hall, never a bedroom"),
    dict(to=81, reason="scene change: in the royal chamber Shahrazad weeps for her sister",
         chars=["shahrazad", "shahryar"], loc="chamber",
         visual=f"{SHAH} sitting on a cushion on the carpet with lowered eyes, a single tear on her cheek, hands "
                f"clasped in a plea; {KING} seated on the long divan more than an arm's length away, turning towards her "
                f"with an irritated, puzzled frown; both fully dressed; no bed visible",
         camera="medium wide, eye level, the moonlit lattice window between them", amb="palace_night",
         sens="intimacy", safe="wedding night = a frame scene of the two sitting apart, fully dressed; no bed"),
    dict(to=83, reason="character enters: Dunyazad is brought in and sits on a rug",
         chars=["dunyazad", "shahrazad", "shahryar"], loc="chamber",
         visual=f"ONE single girl, {DUNYA}, just stepping shyly through the arched doorway on the left, escorted by a "
                f"small elderly maidservant in a dark headscarf seen from behind; {SHAH} sitting on a cushion on the "
                f"carpet, turning and reaching out a welcoming hand towards her little sister, an empty small rug "
                f"waiting beside her; {KING} watching from his divan at a distance; exactly three main characters, "
                f"Dunyazad appears only once",
         camera="wide shot, eye level", amb="palace_night"),
    dict(to=86, reason="action change: the silent, tense night; the king awake, brooding on the morning",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber",
         visual=f"the dim chamber deep in the night, lanterns burning low: {KING} reclining propped on cushions on the "
                f"divan, fully dressed, staring up at the painted ceiling with cold brooding eyes; across the carpet, "
                f"well apart from him, {SHAH} and {DUNYA} sitting quietly side by side, waiting; the huge moon in the "
                f"lattice window",
         camera="wide shot, eye level", amb="palace_night"),
    dict(to=88, reason="action change: Dunyazad whispers her request for a story",
         chars=["dunyazad", "shahrazad"], loc="chamber",
         visual=f"{DUNYA} leaning towards her sister and whispering with a trembling voice and pleading big eyes; {SHAH} "
                f"turning her head to her with a tiny knowing look; lantern glow on both faces",
         camera="close two-shot, eye level", amb="palace_night"),
    dict(to=91, reason="action change: Shahrazad asks the king's leave and begins",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber",
         visual=f"{SHAH} sitting upright on her cushion, turned gracefully towards the king with one hand open in an "
                f"elegant storytelling gesture; {KING} on the divan an arm's length away, propped on one elbow, giving a "
                f"bored but curious nod; {DUNYA} sitting on the carpet beside her sister, eager; the moonlit city of "
                f"domes through the arched window",
         camera="wide shot, eye level, faces in the upper two-thirds", amb="palace_night"),
    # ---------------- TALE: the Merchant and the Jinni ----------------
    dict(to=94, reason="enter the tale: the rich merchant sets out on a long journey", chars=["merchant"],
         loc="desert_road", transition="dissolve",
         visual="the wealthy merchant riding a fine chestnut horse with richly laden saddlebags out of a city gate onto "
                "the long desert road, a determined travelling look, his dusty cloak flowing, golden dunes ahead",
         camera="wide shot, low angle, the rider in the upper half", amb="caravan_road"),
    dict(to=96, reason="action change: on the third day he stops at a spring under a great tree", chars=["merchant"],
         loc="spring",
         visual="the merchant kneeling at the edge of a clear spring in the cool shade of a huge old tree, splashing "
                "water on his tired, sweaty face from cupped hands; his horse drinking beside him; the desert outside "
                "the shade shimmering in blazing heat",
         camera="medium wide, eye level", amb="oasis_day"),
    dict(to=99, reason="action change: he eats dates and tosses the stones behind him", chars=["merchant"], loc="spring",
         visual="the merchant sitting relaxed with his back near the tree trunk, a small cloth with bread and dates "
                "spread beside him, carelessly flicking a date stone over his shoulder into the grass behind him, "
                "a contented chewing smile",
         camera="medium shot, eye level", amb="oasis_day"),
    dict(to=101, reason="emotional turning point: icy wind, the ground splits, smoke becomes a jinni",
         chars=["merchant", "merchant_jinni"], loc="sandstorm",
         visual="a sudden swirling wind of sand; in front of the startled merchant, who leans back on his hands with "
                "wide eyes, the ground cracks open and a huge spiralling column of black glittering smoke rises, "
                "already shaping into the vague outline of an enormous figure with two glowing ember-orange eyes",
         camera="low angle wide shot, the smoke column filling the upper two-thirds", amb="sandstorm", sens="other",
         safe="the jinni's appearance as fairy-tale smoke and sparkles, not horror"),
    dict(to=104, reason="the jinni revealed in full, roaring his threat", chars=["merchant_jinni", "merchant"],
         loc="sandstorm",
         visual=f"dramatic low angle of {JINN}, towering against the dark swirling sky, eyes blazing like fire, roaring "
                f"with one huge empty fist raised high; the ground trembling; the tiny merchant at the bottom of the "
                f"frame shrinking back; {NOSWORD}",
         camera="extreme low angle wide shot", amb="sandstorm", sens="violence",
         safe="the jinni's sword is never drawn: he raises an empty fist (bible rule 1)"),
    dict(to=107, reason="focus change: the merchant on his knees begging for his life",
         chars=["merchant", "merchant_jinni"], loc="sandstorm",
         visual=f"the merchant fallen to his knees in the sand, hands clasped in desperate pleading, tears on his "
                f"cheeks, looking up in terror; behind him the dark looming shape of the giant jinni with glowing eyes, "
                f"slightly out of focus; {NOSWORD}",
         camera="medium shot, high angle over the jinni's shoulder", amb="desert_day"),
    dict(to=111, reason="action change: the jinni accuses him: a date stone killed his invisible son",
         chars=["merchant_jinni", "merchant"], loc="sandstorm",
         visual=f"{JINN} bending down over the kneeling merchant and pointing one huge accusing finger at him, his "
                f"eyes burning like furnace fire; in the foreground on the sand lies a single small date stone catching "
                f"a glint of light; the merchant shaking his head and pleading; {NOSWORD}",
         camera="medium wide, low angle, the jinni's face and finger in the upper half", amb="desert_day"),
    dict(to=113, reason="climax: the jinni prepares to strike (cut away before anything happens)",
         chars=["merchant_jinni", "merchant"], loc="sandstorm",
         visual=f"{JINN} rearing up to his full height against a dark storm sky with his huge empty fist raised high "
                f"above; below, the merchant kneeling upright in the sand with his eyes squeezed shut and head bowed, "
                f"waiting; swirling sand all around; nobody is touched; {NOSWORD}",
         camera="low angle wide shot, the jinni filling the upper two-thirds", amb="sandstorm", sens="violence",
         safe="the seizing by the throat and the raised sword are replaced by a raised empty fist and the merchant "
              "kneeling with eyes shut; the scene cuts away to dawn"),
    # ---------------- FRAME: dawn ----------------
    dict(to=118, reason="leave the tale: dawn breaks, Shahrazad falls silent, the king demands more",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn", transition="dissolve",
         visual=f"golden dawn rays streaming through the lattice window with distant minaret silhouettes against the "
                f"sunrise; {KING} sitting bolt upright on his divan, eyes wide, leaning forward eagerly with one hand "
                f"raised in question; {SHAH} sitting on her cushion an arm's length away with a gentle, modest, knowing "
                f"smile, hands resting in her lap; {DUNYA} beside her, holding her breath",
         camera="wide shot, eye level, the window in the upper half", amb="palace_dawn"),
    dict(to=121, reason="action change: the king glances down at the executioner waiting in the courtyard",
         chars=["shahryar"], loc="chamber_dawn", sens="violence",
         visual=f"{KING} standing at the lattice window, seen from behind and the side, looking down into the palace "
                f"courtyard far below where a single small faceless dark silhouette stands waiting by a gate in the "
                f"grey-gold dawn light, its hands empty; the king's face torn and thoughtful",
         camera="over-the-shoulder high angle, the courtyard far below", amb="palace_dawn",
         safe="the executioner is only a tiny faceless silhouette with empty hands (bible rule 3)"),
    dict(to=123, reason="scene change: the king spares her for one day and goes to his court", chars=["shahryar"],
         loc="court_day",
         visual=f"{KING} striding along the marble hall towards his golden throne in the bright morning, settling his "
                f"robe with a decided expression; small courtiers bowing on both sides; {NOSWORD}",
         camera="wide shot, low angle", amb="throne_hall"),
    dict(to=124, reason="emotional turning point: the Vizier finds his daughter alive", chars=["grand_vizier", "shahrazad"],
         loc="vizier_door",
         visual=f"the Grand Vizier, tears of joy in his eyes and a trembling smile, holding his daughter's hands in "
                f"both of his at a sunlit palace doorway; {SHAH} smiling calmly back at her father",
         camera="medium two-shot, eye level", amb="palace_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Very long ago, in the wide and spacious realm of the Sasanian dynasty, one of the greatest powers in the world,")
sh(2, "there reigned an exceedingly mighty and just king named Shahryar. His power and his commands spread over the wide "
      "sands, the lush great valleys and the high mountains.")
sh(3, "His people loved him dearly, because he was a kind king, good to his subjects, who ruled with justice.")
sh(4, "He drew his sword from its sheath only to protect the rights of his people and to defend the land.")
sh(5, "In another part of this great kingdom, in Samarkand, reigned Shahryar's younger brother, Shah Zaman.")
sh(6, "Like his elder brother, Shah Zaman too had won his people's love and ruled with fairness.")
sh(7, "For ten years the two brothers lived apart in two lands. Because of the long road and the great deserts between "
      "them, they had had no chance to meet.")
sh(8, "But when ten years had passed, a strong longing to see his younger brother arose in Shahryar's heart,")
sh(9, "until he could bear it no longer. So the king sent his most trusted Grand Vizier,")
sh(10, "with a great caravan carrying precious silks, fragrant incense, valuable jewels and the finest horses, to Shah Zaman.",
   [("horse_hooves", "ޤާފިލާއަކާއެކު", -22)])
sh(11, "The purpose was to invite the younger brother to the elder brother's palace. Shah Zaman accepted the invitation with "
       "great joy.")
sh(12, "And to begin the journey he pitched his royal pavilion outside the palace, outside the city gate. The whole army "
       "was ready to travel.", [("cloth_rustle", "ފޭލިގޭ", -24)])
sh(13, "But in the silence of midnight, Shah Zaman remembered that a very precious and important gift he had prepared "
       "for his brother")
sh(14, "had been left behind in his chamber inside the palace.")
sh(15, "So, without telling anyone, he secretly went back to the palace all alone.",
   [("horse_hooves", "އެނބުރި", -22)])
sh(16, "When he entered the palace in the faint moonlight and came to his own chamber,",
   [("footsteps_pavement", "ވަދެވަޑައިގެން", -22)])
sh(17, "Shah Zaman saw a sight so terrible and so sorrowful that no human heart could bear it.",
   [("gasp", "ބިރުވެރި", -18)], hum=True)
sh(18, "The beautiful wife he loved most, for whom he was ready to give up the whole world, had betrayed the king with a "
       "slave.", [("heartbeat", "ބޭވަފާތެރި", -20)], hum=True)
sh(19, "This great betrayal shattered Shah Zaman's heart; he felt as if the whole world had turned upside down. Without "
       "saying a word,", hum=True)
sh(20, "in his fury he drew his sharp sword from its sheath, struck the two of them and killed them both on the spot.",
   [("breath_heavy", "ރުޅިވެރިކަމާއެކު", -20)], hum=True)
sh(21, "Blood flowed over the clean white marble floor. Then, acting as if nothing had happened, he returned to the "
       "pavilion,", [("door_close", "ފޭލިގެއަށް", -22)])
sh(22, "and ordered the journey to begin at once. As he travelled towards his brother's kingdom,",
   [("horse_hooves", "ދަތުރުކުރައްވަމުން", -22)])
sh(23, "Shah Zaman's heart was full of an indescribable deep grief and unease. When he reached Shahryar's capital, Shah "
       "Zaman was given a very warm and colourful welcome.")
sh(24, "Great celebrations and games were held throughout the city. But Shah Zaman's face showed nothing but utter "
       "despair.")
sh(25, "His body grew pale; he stopped eating and drinking and began to waste away. He could not bring himself to tell "
       "his brother about his own wife's betrayal.", [("sigh", "ބަލިކަށިވާން", -22)])
sh(26, "Shahryar thought his younger brother was homesick for his own land and family, and was sad because of it.")
sh(27, "So, to lift his brother's spirits, he arranged a great hunt.")
sh(28, "But because Shah Zaman was very weak, he excused himself from the hunt and stayed in the palace.")
sh(29, "When the king had gone hunting, while Shah Zaman stood looking out of a window in the guests' wing of the "
       "palace, he saw a sight that changed his whole outlook on life.",
   [("horse_hooves", "ޝިކާރައަށް", -24)])
sh(30, "Through a secret door opening into the beautiful palace garden came King Shahryar's wife, the chief queen of the "
       "whole realm.", [("creak", "ދޮރަކުން", -22)])
sh(31, "With her were twenty maidservants and twenty male slaves. Among the trees of the garden they all began to make "
       "merry.", [("leaves_rustle", "ގަސްތަކުގެ", -24)])
sh(32, "When the queen called out, a big slave came out from among the trees and began to embrace her. The wife of the "
       "mightiest king in the world was in the very same kind of betrayal.",
   [("gasp", "ބޭވަފާތެރި", -20)], hum=True)
sh(33, "Seeing this, Shah Zaman felt a strange, indescribable relief. He said to himself: \"If my brother, a far mightier",
   [("sigh", "ހަމަޖެހުމެއް", -22)])
sh(34, "and nobler king than I, has had to face such humiliation and betrayal,")
sh(35, "then this is not only my problem. It is an evil in the nature of all the women of the world.\" With this thought "
       "his sorrows faded away,")
sh(36, "and his former happiness and health returned. He began to eat and drink well. When Shahryar came back from the "
       "hunt and saw the good change in his brother,")
sh(37, "he wanted to understand the reason. At first Shah Zaman tried to keep it secret, but")
sh(38, "out of love and loyalty to his brother he finally revealed the whole truth. Shahryar's mind could hardly accept "
       "the story.")
sh(39, "He wanted to see it with his own eyes. So he announced that he was going hunting again, secretly came back to "
       "the palace and kept watch where he could see the garden.",
   [("footsteps_pavement", "ސިއްރުން", -24)])
sh(40, "Just as his brother had said, the king saw the queen and the slaves come out and begin that wicked deed.",
   hum=True)
sh(41, "At that moment Shahryar's world shattered into pieces. His heart became harder than stone. Love turned into "
       "hatred.", [("heartbeat", "ފުނޑުފުނޑުވެގެން", -18)], hum=True)
sh(42, "At once he ordered the queen, her maidservants and those slaves all to be killed.",
   [("thunder", "އަމުރުކުރެއްވީ", -20)])
sh(43, "But killing them did not put out the fire of hatred blazing in the king's heart.")
sh(44, "A terrible madness gripped his mind. He decided never to trust any woman.",
   [("wind_gust", "ވަށާލިއެވެ", -22)])
sh(45, "And he passed a merciless law that made the whole country weep: every night he would marry some new young girl "
       "of the land, and after spending the night with her,", [("crowd_gasp", "ރޮއްވާލި", -22)])
sh(46, "the next morning he would order the Grand Vizier to cut off the girl's head.")
sh(47, "The king believed that in this way no woman would ever have the chance to betray him. Three years passed in this "
       "tyranny.")
sh(48, "Every day a girl trembling with fear was brought to the palace. And every morning she became the prey of the "
       "executioner's sword.", [("heartbeat", "ތުރުތުރުއަޅާ", -22)], hum=True)
sh(49, "The joyful capital became a city of grief and weeping. The sound of parents crying echoed in the streets.",
   [("sob_breath", "ރުއިމުގެ", -24)], hum=True)
sh(50, "Many families fled the country in the darkness of night. Very soon there were few girls left in the city,",
   [("footsteps_sand", "ފާބައިގެން", -22)])
sh(51, "until things reached the point where there were none left except the daughters of the great viziers and emirs.")
sh(52, "The great and heart-breaking burden of finding all these girls and carrying out the order to kill them fell on "
       "the Grand Vizier's head.")
sh(53, "The Grand Vizier was a good and righteous man. Because of the innocent blood drying on his hands every day, his "
       "soul suffered great pain.", [("sigh", "ވޭނެއް", -22)], hum=True)
sh(54, "The Grand Vizier had two daughters of his own: the elder, Shahrazad, and the younger, Dunyazad.")
sh(55, "Shahrazad was a woman so special that there was no second like her in the whole kingdom. Her beauty was a "
       "beauty that could stop even a galloping horse.")
sh(56, "But her greatest power was her sharp mind. She had read and learned books of history, tales of the kings of old, "
       "poetry and the books of medicine.", [("page_turn", "ފޮތްތައް", -22)])
sh(57, "In her own library there were a thousand books. And ten thousand stories were stored in her memory.")
sh(58, "She saw the cruelty her people were suffering and the king's ruined soul. One night,")
sh(59, "as the Grand Vizier sat weeping by the fire, thinking of the innocent girl who had to be killed the next day, "
       "Shahrazad came and sat down before her father.",
   [("fire_crackle", "އަލިފާންގަނޑު", -20), ("sob_breath", "ރޯން", -24)])
sh(60, "\"Dear father,\" Shahrazad said very firmly, in a voice as clear as a silver bell, \"I ask something of you.")
sh(61, "Tomorrow, take me to the king. I will become his new wife.\"")
sh(62, "The Grand Vizier felt as if a venomous snake had bitten him. Drawing back, he said: \"Have you gone mad, my "
       "child?", [("gasp", "ޖެހިލަމުން", -18)], hum=True)
sh(63, "Do you know what you are asking for? You are asking me to lead my own flesh and blood to the slaughterhouse!\"")
sh(64, "\"I know very well what I am asking for,\" Shahrazad answered. There was no fear at all in her dark eyes.")
sh(65, "\"I will succeed in this and save the daughters of this land. Otherwise I too may die like the other girls.")
sh(66, "But I cannot stand by doing nothing while our people's blood is being spilled.\" The Grand Vizier pleaded.")
sh(67, "He shouted in anger and even threatened her. But Shahrazad did not change her decision. To every excuse her "
       "father raised she answered with strong arguments.", [("breath_heavy", "ހަޅޭއްލަވައި", -20)])
sh(68, "In the end, worn out and helpless, weeping and weeping, the Grand Vizier agreed. And he prayed to Almighty God "
       "to keep his daughter safe.", [("sob_breath", "ރޮމުންރޮމުން", -22)], hum=True)
sh(69, "Before going to the king's palace, Shahrazad took her younger sister Dunyazad aside and spoke to her.")
sh(70, "\"My dear little sister, listen carefully,\" Shahrazad whispered, holding Dunyazad's trembling hand.",
   [("breath", "ސިއްރުން", -24)])
sh(71, "\"Tonight, after I go to the king's chamber, I will ask the king to bring you to me to say a last farewell.")
sh(72, "Go there and sit beside the bed. Wait until the king and I have finished talking. And when the very last part "
       "of the night draws near,")
sh(73, "say this to me: 'Dear sister, if you are not asleep, to pass the hours of this long night,")
sh(74, "tell us one of your beautiful, wonderful stories.' Do you understand, little sister?")
sh(75, "The lives of everyone in this land hang on those words of yours.\" With eyes full of tears, Dunyazad nodded. "
       "That night,", [("sob_breath", "ކަރުނައިން", -24)], hum=True)
sh(76, "the Grand Vizier handed over the most precious jewel of his life to the tyrant king on the throne. When Shahryar "
       "saw Shahrazad,")
sh(77, "even in his heart of stone something stirred for a brief moment at her beauty. But as soon as the two of them "
       "entered the royal chamber,", [("door_close", "ވަނުމާއެކު", -22)])
sh(78, "Shahrazad suddenly began to weep very bitterly. \"What is the matter with you?\" asked Shahryar, disturbed by the "
       "sound of her crying.", [("sob_breath", "ރޯން", -22)])
sh(79, "\"O noble king,\" she said, sobbing, \"I have a little sister. Her name is Dunyazad.",
   [("sob_breath", "ގިސްލަމުން", -24)])
sh(80, "I love her dearly. Knowing that I will die when dawn comes, my heart breaks because I cannot see my sister one "
       "last time.")
sh(81, "I beg you to grant my sister leave to sit with us in the last hours of my life.\"")
sh(82, "Seeing no harm in granting the last wish of a woman ready to die, Shahryar ordered Dunyazad to be brought.")
sh(83, "The little girl was brought in and sat down on a soft, beautiful rug at the foot of the great bed.",
   [("door_open", "ގެނެސް", -22), ("cloth_rustle", "އިށީނދެއްޖެއެވެ", -24)])
sh(84, "The hours of the night passed in silence and unease. The king lay awake.")
sh(85, "As he lay staring at the ceiling, his mind was already set on the bloodshed he had to carry out the next "
       "morning.")
sh(86, "The darkest and deepest hour of the night came and settled over the palace. A short moment before the first "
       "light of dawn appeared on the horizon,", hum=True)
sh(87, "Dunyazad began to speak. Her voice trembled in that great silent room. \"Dear sister,\" she whispered.",
   [("breath", "ސިއްރުން", -24)])
sh(88, "\"If you are not asleep, to pass the last hours of this long night, tell us one of your beautiful, wonderful "
       "stories.\"")
sh(89, "Shahrazad sat up. Her long black hair had fallen over her shoulders. She looked towards the king.",
   [("cloth_rustle", "ތެދުވެ", -22)])
sh(90, "\"Will the king grant me leave to tell a story?\" Shahryar, bored from having to wait until morning, nodded.")
sh(91, "\"Tell it.\" Shahrazad took a slow, deep breath and began: \"O mighty and wise king!",
   [("breath", "ނޭވާއެއް", -22)])
sh(92, "As I have heard, in times of old there lived a very rich merchant. He had a great deal of goods and money.")
sh(93, "He travelled to distant lands to trade. One day, to collect a large sum of money that was owed to him,")
sh(94, "he mounted his horse and set out for a distant land. It was a long and exhausting journey.",
   [("horse_hooves", "ސަވާރުވެގެން", -20)])
sh(95, "Because of the hot sun overhead, the ground was as hot as an oven. On the third day of the journey, when he was "
       "so tired and hot that he could bear it no longer,")
sh(96, "he stopped in the shade of a big tall tree beside a clear spring he saw by the road. He got off his horse, washed "
       "his face and hands with the cool water, and sat down to rest.",
   [("water_splash_small", "ދޮވެލުމަށްފަހު", -20)])
sh(97, "From his bag he took out a small piece of bread and a handful of dates. He ate the dates one after another.")
sh(98, "And without any care he kept tossing the date stones into the bushes behind him. When he had eaten the last "
       "date,", [("leaves_rustle", "އުކަމުން", -24)])
sh(99, "and threw the last stone into the grass behind him, suddenly the wind all around turned bitterly cold.",
   [("wind_gust", "ވައިރޯޅި", -18)])
sh(100, "With a violent wind the sand whirled up. The ground in front of him split open, and a thick black smoke rose "
        "from it. Swirling round and round, that smoke",
    [("sandstorm_gust", "ވަޔާއެކު", -18), ("stone_scrape", "ފަޅައިގެން", -18), ("smoke_whoosh", "ދުންގަނޑެއް", -16)])
sh(101, "turned into the shape of a terrifying, enormous jinni. That jinni was a thing more frightening than anything "
        "seen even in dreams.", [("magic_shimmer", "ޖިންނިއެއްގެ", -20)], hum=True)
sh(102, "Its two eyes were like blazing fire. Its teeth were long and stuck out like the tusks of a wild boar. In its "
        "huge,")
sh(103, "segmented hand was a huge sharp sword. As the jinni took a step forward, the ground trembled.",
    [("soft_thud", "ފިޔަވަޅެއް", -14)])
sh(104, "And it roared in a voice as loud as thunder: 'Get up! Just as you killed my son, I will cut off your head!'",
    [("thunder", "ގުގުރީގެ", -16)], hum=True)
sh(105, "Frozen with terror, the merchant fell to his knees. 'O mighty spirit!' he said, weeping.",
    [("soft_thud", "ކަކޫމައްޗަށް", -20), ("sob_breath", "ރޮމުން", -24)])
sh(106, "'How could I have killed your son? I do not know him, and I have never even seen him!")
sh(107, "I am only an ordinary poor merchant who sat down to rest in the shade of this tree!' The jinni raised its huge "
        "sword.", [("wind_gust", "ނެގިއެވެ", -20)])
sh(108, "The gleam of that blade spoke of the terror of death. 'When you sat here eating dates,")
sh(109, "and tossed the date stones behind you,' the jinni said furiously, 'a stone you threw struck my son on the chest "
        "as he was walking past there, and from the force of that stone he died instantly.")
sh(110, "By the law of the unseen world, the price of blood is blood!' The merchant wept and pleaded. 'I swear it! It "
        "happened without intention!", [("sob_breath", "ރޮއި", -24)])
sh(111, "I could not see him! Have mercy on me!' 'No mercy,' cried the jinni. The fire of hell could be seen in its "
        "eyes.", [("fire_crackle", "އަލިފާން", -20)])
sh(112, "'You must die.' Having said this, the jinni seized the merchant by the throat, threw him to the ground, and "
        "raising its heavy sword,", [("soft_thud", "ވައްޓާލިއެވެ", -18)], hum=True)
sh(113, "made ready to bring it down to cut off the poor man's head...\" At that very moment the first rays of the "
        "beautiful golden light of dawn came in through the thick silk curtains of the king's chamber.",
    [("heartbeat", "ތައްޔާރުކޮށްލިއެވެ", -16)], hum=True)
sh(114, "The beautiful sound of the call to the dawn prayer from the mosques of the capital spread through the air. "
        "Shahrazad at once broke off the story and fell silent.")
sh(115, "King Shahryar lay staring at Shahrazad with wide eyes, then suddenly sat up. \"Then what happened?",
    [("cloth_rustle", "ތެދުވެވަޑައިގަތެވެ", -22)])
sh(116, "Tell me what happened next! Did the jinni cut off his head?\" A very gentle, polite smile settled on "
        "Shahrazad's lips.")
sh(117, "\"O noble king. It is dawn. And the part I have told you is nothing compared with the great events still to "
        "come.")
sh(118, "But sadly my time is up. So I must take the rest of this story with me to the grave.\"")
sh(119, "Shahryar's mind began to work hard. He longed to know whether that merchant had been saved.")
sh(120, "He wanted to know how an ordinary human being could escape from a mighty jinni of the desert.")
sh(121, "The king glanced at the executioner waiting in the courtyard below, then looked back at Shahrazad.")
sh(122, "\"Only for today I will let her go,\" the king said to himself. \"After hearing the end of this story tonight, "
        "I will kill her tomorrow morning.\"")
sh(123, "So King Shahryar rose, put on his royal robe and went to the court to govern for the day.",
    [("cloth_rustle", "ތުރުކުރައްވައިގެން", -22), ("footsteps_pavement", "ދަރުބާރަށް", -22)])
sh(124, "That day the Grand Vizier saw his daughter still alive in the world. He was utterly astonished and overjoyed. "
        "The first night was over. But the real great game had only just begun.",
    [("sigh", "ޙައިރާންވެ", -22)], hum=True)
SHOTS = S

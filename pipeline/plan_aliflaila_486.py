"""Beat/shot plan for Aliflaila episode 486 (Night Three) — used by plan_beats.py.
FRAME: Shahryar's bedchamber (night -> dawn). TALE: the Merchant and the Jinni in the desert (the First Old Man stops
the jinni). TALE-WITHIN-THE-TALE: the First Old Man's own story of the gazelle (his jealous wife), the young mother and
the son turned into a cow and a calf, the Eid sacrifice, the herdsman's daughter breaking the spell.
Bible rules: the jinni never has a sword (empty hands); the Eid sacrifice = the herdsman leading the cow away by a rope,
the old man turning his face away (no knife, no slaughter, no carcass, no bones); the son's wedding is symbolic only
(henna hands + small lantern + two cups on a brass tray, no boy groom); transformations = sparkle swirls between two
separate states; every woman's headscarf fully covers hair and neck; no text anywhere."""

STORYBOOK = "soft golden storybook glow over the whole picture"
JINNI = ("the towering charcoal-smoke jinni in his dark-red robe and dark-red turban, ember-orange eyes, both hands "
         "completely empty")
MERCHANT = ("the merchant in a plain white travelling robe and white turban, a folded white cloth (his shroud) lying beside "
            "him on the sand")
OLDMAN_TALE = ("the First Old Man as he was some years earlier: the same gentle face, white turban and pale sage-green robe "
               "but his beard grey rather than snow-white, no staff")
GAZELLE = "a slender golden-brown gazelle with big dark gentle eyes on a golden cord"
DOGS = "two calm black dogs on leashes sitting quietly on the sand at a little distance behind him"

LOC = {
    "palace_ext": "King Shahryar's great white palace with onion domes, slender towers and arched lattice windows rising "
                  "above dark cypress gardens and a long still reflecting pool",
    "chamber": "the king's palace chamber: a carved arched lattice window looking out on a moonlit city of domes and "
               "minarets, brass lanterns hanging from chains, a rich Persian carpet with silk cushions, a low cushioned "
               "divan with brocade bolsters, silk curtains",
    "chamber_dawn": "the king's palace chamber: a carved arched lattice window looking out on the city of domes and a "
                    "distant slender minaret silhouette against the sky, brass lanterns, a rich Persian carpet with silk "
                    "cushions, a low cushioned divan with brocade bolsters, silk curtains",
    "desert_tree": "a lonely desert oasis: a great old shade tree with a spreading crown beside a small clear spring, "
                   "rolling golden sand dunes all around, wind-blown sand ripples",
    "house_court": "the tiled inner courtyard of a prosperous merchant's sand-coloured house in an old island town by the "
                   "sea: arched colonnades, a small fountain, potted lemon trees, date palms, a blue-tiled doorway",
    "house_room": "a sitting room in the prosperous sand-coloured house: arched windows with carved lattice shutters, "
                  "Persian carpets, low cushions along the walls, a brass lamp on a low table",
    "bazaar": "a busy old bazaar street of the island town: striped awnings, stalls of silks, carpets, copper pots and "
              "baskets of spices, small modestly dressed background figures",
    "gate": "the arched wooden street gate of the sand-coloured house, a small caravan of laden camels waiting in the lane, "
            "the sea and sailing ships glimpsed between the houses",
    "sorcery_room": "a dim, cluttered back room of an old stone house: a low brass brazier, shelves of plain clay jars and "
                    "bundles of dried herbs, heavy dark curtains",
    "pasture": "the cattle pen and green pasture behind the house: a rough wooden fence, a thatched shelter, date palms, a "
               "few ordinary cows grazing in the distance",
    "eid_court": "the inner courtyard of the sand-coloured house decorated for Eid: strings of small brass lanterns and "
                 "festive cloth garlands between the arches, a small fountain, potted lemon trees",
    "herdsman_house": "the humble mud-brick house of the herdsman at the edge of the pasture: a low wooden door, a clay "
                      "water jar, a woven mat, simple shelves, a small window",
    "wedding": "a small lantern-lit room in the herdsman's humble house decorated with fresh jasmine garlands",
    "palace_hall": "a long sunlit marble colonnade of the palace leading to the arched doors of the royal court hall",
}
MOOD = {
    "palace_ext": "deep midnight-blue night, a huge silver moon and twinkling stars, the domes catching faint moonlight, "
                  "a few amber lantern-lit windows, hushed and still",
    "chamber": "late night, deep midnight blue with warm amber lantern light, moonlight through the lattice, intimate, "
               "hushed, full of anticipation",
    "chamber_dawn": "first light of dawn, rose-gold and pale gold light streaming through the lattice window across the "
                    "carpet, the lanterns burning low, gentle and suspenseful",
    "desert_tree": "late afternoon after a sandstorm, a dusty amber-gold sky with dark storm clouds drifting away, long "
                   "dramatic shadows, tense and awe-filled",
    "house_court": "warm golden daylight with a soft golden storybook glow, tender and nostalgic",
    "house_room": "warm afternoon light through the lattice with a soft golden storybook glow, emotional",
    "bazaar": "bright golden morning sunlight with a soft golden storybook glow, lively",
    "gate": "early morning, soft rose and gold light with a soft golden storybook glow, bittersweet farewell",
    "sorcery_room": "night, the only light a swirl of glittering green smoke from the brazier, deep violet shadows, a "
                    "soft storybook glow at the edges, sinister fairy-tale mood (never horror)",
    "pasture": "golden late-afternoon light with a soft golden storybook glow, quiet and melancholy",
    "eid_court": "early morning of Eid, soft pale-gold dawn light, festive lanterns still glowing, a soft golden storybook "
                 "glow, emotional",
    "herdsman_house": "warm daylight through a small window with a soft golden storybook glow, hopeful and magical",
    "wedding": "evening, warm lantern light and a soft golden storybook glow, gentle, joyful and modest",
    "palace_hall": "bright fresh morning sunlight striping the marble through the arches, calm and resolute",
}

BEATS = [
    # ---------------- FRAME: night ----------------
    dict(to=3, reason="episode opening: Night Three falls over Shahryar's palace", loc="palace_ext",
         visual="the great white palace seen from across the moonlit gardens, its onion domes and slender towers against a "
                "deep blue sky full of twinkling stars and a huge silver moon, one high arched window glowing warm amber; "
                "the long still reflecting pool mirrors the moon; no people",
         camera="wide establishing shot, slightly low, domes in the upper two-thirds, the still pool as the calm lower third",
         amb="palace_night"),
    dict(to=7, reason="character change: inside the chamber Dunyazad asks her sister to finish the story",
         chars=["dunyazad", "shahrazad", "shahryar"], loc="chamber",
         visual="Dunyazad sitting on the carpet beside her sister, leaning eagerly towards her and whispering with a hand "
                "cupped beside her mouth and big shining eyes; Shahrazad sitting upright on a silk cushion listening with a "
                "calm knowing smile; King Shahryar sitting fully dressed on the low divan an arm's length away, leaning "
                "forward on his knee, impatient and curious; brass lanterns glowing, the moonlit domes through the lattice",
         camera="medium wide, eye level, the three figures in the upper two-thirds, the carpet as a calm lower third",
         amb="palace_night"),
    dict(to=12, reason="action change: Shahrazad asks the king's leave and he urges her on",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber",
         visual="Shahrazad on her cushion turning her large expressive eyes towards the king and bowing her head politely, "
                "one hand on her heart, the other gently adjusting the edge of her ivory headscarf; King Shahryar on the "
                "divan an arm's length away gesturing eagerly with an open palm for her to begin, his eyes wide with "
                "impatience; Dunyazad on the carpet behind her sister, hugging a cushion",
         camera="medium two-shot, slightly low, faces in the upper half", amb="palace_night"),
    # ---------------- TALE: the desert ----------------
    dict(to=14, reason="scene change into the tale: the jinni towers over the merchant",
         chars=["merchant_jinni", "merchant"], loc="desert_tree", transition="dissolve",
         visual=f"{JINNI} towering over the dunes beside the great tree, one huge empty fist raised high against the "
                f"storm-dark amber sky, glaring down in fury; far below {MERCHANT}, kneeling small on the sand with his "
                "eyes squeezed shut and his hands clasped, trembling and waiting for the end",
         camera="dramatic low angle, the jinni filling the upper frame, the kneeling merchant small at the bottom centre "
                "above calm sand",
         amb="desert_day", sens="violence",
         safe="the narration's raised sword is replaced by an empty raised fist; no weapon, nothing harms the merchant"),
    dict(to=16, reason="character enters: the First Old Man steps forward and shouts 'Stop!'",
         chars=["old_man_gazelle", "merchant_jinni", "merchant"], loc="desert_tree",
         visual=f"the First Old Man with his snow-white beard striding boldly forward across the sand, his staff in one "
                f"hand and his other hand raised high with open palm commanding the giant to stop, his mouth open in a "
                f"shout, robe and beard swept by the wind, {GAZELLE} beside him; the huge jinni above freezing in surprise "
                "with his empty fist still raised; the kneeling merchant opening one eye",
         camera="wide shot, low angle from behind the merchant, the old man and the jinni facing each other",
         amb="desert_day"),
    dict(to=18, reason="emotional turn: the jinni glares at the old man in rage",
         chars=["merchant_jinni"], loc="desert_tree",
         visual=f"close view of {JINNI} bending down out of the swirling smoke, his blazing ember-orange eyes narrowed, "
                "thick eyebrows drawn together, pointing one huge empty finger downward in outrage, sparks of ember "
                "drifting around his turban against the storm sky",
         camera="close-up from a low angle, the face in the upper half, smoke billowing below", amb="desert_day"),
    dict(to=23, reason="action change: the old man calmly makes his bargain with the jinni",
         chars=["old_man_gazelle", "merchant_jinni"], loc="desert_tree",
         visual=f"the First Old Man standing calm and fearless on the sand, leaning on his staff, looking up at the jinni "
                f"and holding up one finger as he proposes his bargain, {GAZELLE} pressed gently against his side; the "
                "towering jinni above with arms folded, listening with a suspicious scowl; the great tree behind them",
         camera="medium wide, low angle over the old man's shoulder up to the jinni", amb="desert_day"),
    dict(to=26, reason="action change: the jinni ponders, lowers his raised arm and agrees",
         chars=["merchant_jinni", "old_man_gazelle"], loc="desert_tree",
         visual="the giant jinni stroking his thick black beard with one empty hand, eyes lifted in curious thought, a "
                "faint intrigued smile appearing, his other arm lowered and resting; little curls of smoke drifting from "
                "his shoulders; the small figure of the old man waiting below",
         camera="medium shot from a low angle, the jinni's face in the upper half", amb="desert_day"),
    dict(to=29, reason="action change: the old man strokes the gazelle and begins his story to everyone",
         chars=["old_man_gazelle", "merchant", "merchant_jinni", "old_man_dogs"], loc="desert_tree",
         visual=f"the First Old Man tenderly stroking the head of {GAZELLE}, which looks up at him with sad gentle eyes; "
                f"he begins to speak, one hand open as storytellers do; {MERCHANT}, still kneeling and trembling, looking "
                "up at him with hope; the Second Old Man standing a little further back listening, two black dogs on "
                "leashes sitting calmly beside him; the jinni's huge smoky form looming in the background listening",
         camera="medium wide, eye level, the old man and the gazelle in the centre", amb="desert_day"),
    # ---------------- TALE-WITHIN-THE-TALE: the gazelle ----------------
    dict(to=33, reason="scene change into the old man's own tale: thirty childless years with his wife",
         chars=["old_man_gazelle", "gazelle_wife"], loc="house_court", transition="dissolve",
         visual=f"{OLDMAN_TALE} and his wife in her dark forest-green gown and black headscarf sitting side by side on a "
                "stone bench in their sunlit courtyard; between them a small empty carved wooden cradle draped with a "
                "folded white cloth; he looks at the empty cradle with sad longing eyes, she looks away with a tight proud "
                f"mouth; {STORYBOOK}",
         camera="medium wide, eye level, the couple in the upper two-thirds, the tiled floor as calm lower third",
         amb="stone_house_day"),
    dict(to=35, reason="scene change: at the bazaar he takes a young girl into his house",
         chars=["old_man_gazelle", "young_mother"], loc="bazaar",
         visual=f"{OLDMAN_TALE} walking through the bustling sunlit bazaar; a few steps behind him, at a modest distance, "
                "the shy young woman in her loose pale butter-yellow gown and cream headscarf fully covering her hair and "
                "neck, eyes lowered, holding a small cloth bundle; striped awnings and colourful stalls around them; "
                f"{STORYBOOK}",
         camera="medium wide, eye level, the two figures in the upper half, the cobbled street as the lower third",
         amb="bazaar_day", sens="other",
         safe="the slave purchase is not shown as a transaction: only the man walking ahead and the modest young woman "
              "following at a respectful distance"),
    dict(to=39, reason="time and action change: the son is born; joy for the father, jealousy for the wife",
         chars=["young_mother", "old_man_gazelle", "gazelle_wife"], loc="house_court",
         visual="in the sunlit courtyard the young mother in her butter-yellow gown and cream headscarf (wrapped snugly "
                "down to her eyebrows and under her chin, completely hiding all of her hair, not a single strand "
                "visible on her forehead) sits by the "
                "fountain cradling a baby boy wrapped in a soft white swaddling blanket, smiling down at him; "
                f"{OLDMAN_TALE} stands beside them beaming with joy, hands clasped at his heart; in the shadowed archway "
                "behind them the wife in dark forest-green and black headscarf watches with narrow cold jealous eyes, one "
                f"hand gripping the pillar; {STORYBOOK}",
         camera="medium wide, eye level, the mother and father in front, the jealous wife small in the background archway",
         amb="stone_house_day"),
    dict(to=42, reason="time jump and scene change: the son is ten; the father leaves on a long trading voyage",
         chars=["old_man_gazelle", "gazelle_son", "young_mother", "gazelle_wife"], loc="gate",
         visual=f"at the arched street gate {OLDMAN_TALE}, now in a dusty travelling cloak, rests his hand on the "
                "shoulder of his ten-year-old son in a sky-blue tunic and small white cap, who looks up at him sadly; the "
                "young mother in butter-yellow and cream headscarf stands just behind the boy; the wife in dark green and "
                "black headscarf stands to one side with a thin false smile, her hand on her heart as if promising; laden "
                f"camels wait in the lane; {STORYBOOK}",
         camera="wide shot, eye level, the family under the arch, the dusty lane as the calm lower third",
         amb="caravan_road", transition="black"),
    dict(to=44, reason="scene change: while he is away the wife learns sorcery and casts her spell",
         chars=["gazelle_wife"], loc="sorcery_room", transition="black",
         visual="the wife in her dark forest-green gown and black headscarf standing over a low brass brazier in a dim "
                "back room, her hands spread above it, her face lit from below by a swirl of glittering green smoke and "
                "sparkles rising into the dark; two hooded figures in dark cloaks seen only from behind in the shadows; "
                f"plain clay jars and dried herbs on the shelves; {STORYBOOK}",
         camera="medium shot, slightly low, her face in the upper third", amb="stone_house_night", sens="other",
         safe="sorcery shown as fairy-tale green sparkling smoke; no symbols, no writing, no ritual details, the sorcerers "
              "only as hooded figures from behind"),
    dict(to=46, reason="scene and action change: the cow and the calf are handed to the herdsman",
         chars=["gazelle_wife", "herdsman"], loc="pasture",
         visual="at the wooden cattle pen the wife in dark green and black headscarf hands two ropes to the herdsman in "
                "his rough brown tunic and striped head-wrap: on the ropes stand a gentle honey-coloured cow and a small "
                "brown-and-white calf, ordinary animals with big sad eyes, a few last glittering green sparkles fading "
                "in the air around them; the herdsman takes the ropes with a puzzled but obedient look; she points "
                f"towards the herd; {STORYBOOK}",
         camera="medium wide, eye level, the people in the upper half, the grass as the calm lower third",
         amb="village_day", sens="other",
         safe="the transformation is shown only as fading sparkles around normal animals, never a half-transformed body"),
    dict(to=50, reason="time jump: a year later he returns home and the wife lies to him in false tears",
         chars=["old_man_gazelle", "gazelle_wife"], loc="house_room", transition="black",
         visual=f"{OLDMAN_TALE} in his dusty travelling cloak, just come through the door with a travel bag still on his "
                "shoulder, looking around anxiously and holding out an open hand in question; before him the wife in "
                "dark green and black headscarf hides her face behind her sleeve as if weeping, but one cold dry eye "
                f"peeks out; {STORYBOOK}",
         camera="medium two-shot, eye level", amb="stone_house_day"),
    dict(to=52, reason="emotional turning point: his heartbreak and months of mourning",
         chars=["old_man_gazelle"], loc="house_room",
         visual=f"{OLDMAN_TALE} sitting alone on a cushion by the lattice window, bent over, his face buried in his hands, "
                "shoulders shaking with grief; beside him a small sky-blue child's cap lying on the carpet; long "
                f"shadows across the room; {STORYBOOK}",
         camera="medium wide, eye level, the lonely figure in the upper half, the carpet as the lower third",
         amb="stone_house_day", sens="other", safe="grief shown as a lonely figure and the son's small cap"),
    # ---------------- Eid ----------------
    dict(to=54, reason="time jump and scene change: Eid comes; the herdsman brings the fattest cow",
         chars=["herdsman", "old_man_gazelle"], loc="eid_court", transition="black",
         visual=f"the herdsman in his brown tunic and striped head-wrap leading a plump honey-coloured cow with a festive "
                f"flower garland round its neck into the lantern-decorated courtyard on a rope; {OLDMAN_TALE}, in a clean "
                f"festive white robe, waits empty-handed and nods; {STORYBOOK}",
         camera="wide shot, eye level, the cow and men in the upper two-thirds, the tiles as the calm lower third",
         amb="stone_house_dawn"),
    dict(to=57, reason="emotional turning point: the cow weeps at his feet and he cannot go on",
         chars=["old_man_gazelle"], loc="eid_court",
         visual="the honey-coloured cow lowering its head and pressing it gently against the old man's feet, big shining "
                f"tears running from its large gentle eyes; {OLDMAN_TALE} stepping back with both hands open and empty, "
                f"his face shocked and deeply moved, eyes glistening; {STORYBOOK}",
         camera="medium shot, slightly high angle, his face in the upper third, the cow's head below",
         amb="stone_house_dawn", sens="violence",
         safe="no knife is ever shown: his hands are empty and open; the narration's dropped knife is only a sound"),
    dict(to=60, reason="character enters: the wife storms in demanding the sacrifice",
         chars=["gazelle_wife", "old_man_gazelle", "herdsman"], loc="eid_court",
         visual="the wife in dark forest-green and black headscarf storming into the courtyard, pointing furiously at the "
                f"cow, her face twisted with anger; {OLDMAN_TALE} turning towards her, torn and pleading with open "
                "hands; the herdsman holding the cow's rope in the background, uneasy; festive lanterns overhead; "
                f"{STORYBOOK}",
         camera="medium wide, eye level", amb="stone_house_dawn"),
    dict(to=61, reason="action change: the cow is led away for the sacrifice (bible rule 8)",
         chars=["herdsman", "old_man_gazelle"], loc="eid_court",
         visual="the herdsman, seen from behind, slowly leading the honey-coloured cow away on a rope through a far "
                "archway into the pale dawn light; the cow glancing back with a tear on its cheek; in the foreground "
                f"{OLDMAN_TALE} turns his face away, eyes shut, one hand pressed over his heart; {STORYBOOK}",
         camera="medium wide, the old man in the foreground on one side, the departing cow small in the archway",
         amb="stone_house_dawn", sens="violence",
         safe="no knife, no slaughter, no carcass: only the cow led away by a rope and the old man turning his face away"),
    dict(to=65, reason="emotional turn: the sorcery revealed; he turns on his wife and asks for a calf",
         chars=["old_man_gazelle", "gazelle_wife"], loc="eid_court",
         visual=f"{OLDMAN_TALE} standing with an empty loose rope hanging from his hand, his face full of sorrow and "
                "anger, pointing a reproachful finger at his wife; the wife in dark green and black headscarf folding "
                "her arms and lifting her chin coldly; a few faint green sparkles dissolving in the air between them; "
                f"{STORYBOOK}",
         camera="medium two-shot, eye level", amb="stone_house_dawn", sens="violence",
         safe="the narration's bones and carcass are never shown; only an empty rope and fading sparkles"),
    dict(to=68, reason="character enters: the calf breaks free and clings to him weeping",
         chars=["old_man_gazelle"], loc="eid_court",
         visual="a small brown-and-white calf with a broken rope trailing from its neck pressing itself against the "
                "old man's legs, big tears shining in its large dark eyes; "
                f"{OLDMAN_TALE} kneeling down, gently laying his hand on the calf's head, his own eyes filling with "
                f"tears of tender recognition; {STORYBOOK}",
         camera="medium close shot, slightly low, his face in the upper third", amb="stone_house_dawn"),
    dict(to=73, reason="action change: he protects the calf against his wife's screaming",
         chars=["old_man_gazelle", "gazelle_wife", "herdsman"], loc="eid_court",
         visual=f"{OLDMAN_TALE} standing firm with one arm stretched out protectively, refusing; behind his arm the "
                "herdsman gently leads the small brown-and-white calf away to safety; the wife in dark green and black "
                "headscarf screaming and pointing at the calf, her face red with rage; festive lanterns swaying "
                f"overhead; {STORYBOOK}",
         camera="medium wide, eye level", amb="stone_house_dawn"),
    dict(to=77, reason="time jump: the next day the herdsman secretly brings the news",
         chars=["herdsman", "old_man_gazelle"], loc="house_court", transition="black",
         visual="in a quiet shaded corner of the courtyard colonnade the herdsman leans close, one hand raised beside his "
                f"mouth, whispering secretly with excited eyes; {OLDMAN_TALE} listening with eyes widening in astonishment "
                f"and dawning hope; {STORYBOOK}",
         camera="medium two-shot, eye level", amb="stone_house_day"),
    dict(to=79, reason="emotional turning point: the terrible truth about the cow",
         chars=["old_man_gazelle"], loc="house_court",
         visual=f"{OLDMAN_TALE} sinking to his knees on the tiles, both hands clutching his turban, face lifted in "
                "anguish with tears streaming; behind him the sky over the courtyard darkens with heavy clouds as if "
                f"falling on him; {STORYBOOK}",
         camera="medium shot, slightly high angle", amb="stone_house_day", sens="other",
         safe="grief shown on his face and the darkening sky; nothing of the slaughter"),
    dict(to=84, reason="scene change: at the herdsman's house he begs the daughter; she sets two conditions",
         chars=["old_man_gazelle", "herdsman_daughter", "herdsman"], loc="herdsman_house",
         visual=f"inside the humble mud-brick house {OLDMAN_TALE} stands with hands pressed together, pleading; across "
                "the room at a respectful distance the herdsman's daughter in her burnt-orange gown and saffron-yellow "
                "headscarf fully covering her hair and neck stands confidently, holding up two fingers as she states her "
                "conditions, a clever determined look in her large eyes; the herdsman stands near the door; the small "
                f"calf rests on a straw mat in the corner; {STORYBOOK}",
         camera="medium wide, eye level, the faces in the upper two-thirds", amb="stone_house_day"),
    dict(to=86, reason="action change: the spell-breaking water is splashed on the calf",
         chars=["herdsman_daughter"], loc="herdsman_house",
         visual="the herdsman's daughter in burnt-orange and saffron headscarf holding a simple clay bowl of water in one "
                "hand and flicking it towards the little brown-and-white calf with the other; the water droplets turn "
                "into a swirl of glittering golden sparkles and soft light that wraps around the calf, which trembles "
                f"with wide eyes; {STORYBOOK}",
         camera="medium shot, eye level", amb="stone_house_day", sens="other",
         safe="counter-magic shown as plain water turning into golden sparkles; no words, no symbols"),
    dict(to=87, reason="emotional turning point: the son stands restored and the father embraces him",
         chars=["gazelle_son", "old_man_gazelle"], loc="herdsman_house",
         visual="in a fading swirl of golden sparkles the ten-year-old son stands restored in his sky-blue tunic and "
                f"small white cap, arms open; {OLDMAN_TALE} rushes to embrace him, kneeling and holding the boy close, "
                f"both weeping with joy; {STORYBOOK}",
         camera="medium shot, eye level, faces in the upper half", amb="stone_house_day",
         sens="intimacy", safe="a father and his young son embracing (mahram)"),
    dict(to=88, reason="symbolic image: the son's marriage to the herdsman's daughter (symbolic only)",
         loc="wedding",
         visual="close-up of two young hands decorated with delicate red-brown henna patterns, the sleeves of a "
                "burnt-orange gown at the wrists, holding a small glowing brass lantern; beside it a brass tray with two "
                f"small cups and fresh jasmine flowers; warm lantern light; no faces, no people visible; {STORYBOOK}",
         camera="close-up, the lantern and hands in the upper two-thirds, the tray as the lower third",
         amb="stone_house_night", sens="intimacy",
         safe="the wedding is shown only as henna hands, a lantern and two cups; the boy is never shown as a groom"),
    dict(to=89, reason="action change: the wife is turned into the gazelle",
         loc="house_court",
         visual="in the empty sunlit courtyard a swirl of glittering golden sparkles settles around a slender "
                "golden-brown gazelle standing alone where the jealous wife used to stand, a black headscarf lying "
                f"folded on the tiles nearby; the gazelle looks up with big startled eyes; {STORYBOOK}",
         camera="medium wide, eye level", amb="stone_house_day", sens="other",
         safe="transformation shown only as a normal gazelle inside a sparkle swirl"),
    # ---------------- back to the TALE ----------------
    dict(to=91, reason="scene change back to the desert: the amazed jinni grants a third of the merchant's blood",
         chars=["merchant_jinni", "old_man_gazelle", "merchant"], loc="desert_tree", transition="dissolve",
         visual=f"{JINNI} leaning back with both empty hands spread wide in amazement, his ember eyes wide and a big "
                f"astonished grin under his beard; the First Old Man with his snow-white beard standing with {GAZELLE} "
                f"and bowing slightly; {MERCHANT} looking up with a first gleam of relief",
         camera="wide shot, low angle, the jinni in the upper frame", amb="desert_day"),
    dict(to=94, reason="character change: the Second Old Man steps forward with his two black dogs",
         chars=["old_man_dogs", "merchant_jinni"], loc="desert_tree",
         visual=f"the Second Old Man in his brown turban and dark chocolate-brown robe stepping forward on the sand, one "
                f"hand raised to call the jinni, a confident glint in his eye; {DOGS}; the towering jinni turning his "
                "head down towards him with one eyebrow raised in interest",
         camera="medium wide, low angle, the old man in the centre, the jinni filling the upper background",
         amb="desert_day"),
    # ---------------- FRAME: dawn ----------------
    dict(to=95, reason="scene change back to the frame: dawn breaks and the call to prayer begins",
         loc="chamber_dawn", transition="dissolve",
         visual="the carved arched lattice window of the chamber seen from inside: beyond it the rose-gold dawn breaks "
                "over the city of domes, a slender minaret silhouetted against the brightening sky, a brass lantern "
                "burning low on the sill; no people",
         camera="medium shot of the window, the sky and minaret in the upper two-thirds, the sill as calm lower third",
         amb="palace_dawn"),
    dict(to=100, reason="characters return: Shahrazad falls silent; the king sits up begging for more",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_dawn",
         visual="golden dawn light falling across the carpet: Shahrazad on her cushion with hands folded in her lap, "
                "smiling gently and bowing her head in silence; King Shahryar, fully dressed, sitting bolt upright on the "
                "divan an arm's length away, reaching out an open hand as if to beg for more, eyebrows raised; Dunyazad "
                "beside her sister hiding a delighted smile behind her hand",
         camera="medium wide, eye level, faces in the upper two-thirds", amb="palace_dawn"),
    dict(to=104, reason="scene change: the king spares her again and walks to his court",
         chars=["shahryar"], loc="palace_hall",
         visual="King Shahryar in his crimson-and-gold plumed turban and bronze brocade coat striding down the sunlit "
                "marble colonnade towards the tall arched doors of the court hall, empty-handed, glancing back over his "
                "shoulder with a thoughtful, softened expression; bands of morning light and shadow across the floor",
         camera="wide shot, eye level, the king in the upper half, the marble floor as the calm lower third",
         amb="palace_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Night Three: the story of the First Old Man and his wife. As the black darkness of the third night spread over the world,")
sh(2, "and the stars began to twinkle in the sky, a deep silence settled over King Shahryar's great palace.")
sh(3, "An immense curiosity had grown in the king's heart. He was very impatient to learn how the affair between that "
      "terrifying jinni and the helpless merchant in the desert would end.")
sh(4, "Dunyazad, Shahrazad's younger sister, who was sitting on the beautiful costly rug spread beside the bed,")
sh(5, "as the last and darkest hour of the night drew near, softly called her sister as usual.")
sh(6, "\"Dear sister,\" Dunyazad whispered. \"If you are not asleep, please finish that beautiful,")
sh(7, "wondrous story you broke off yesterday. Tell us what happened when that giant jinni brought down his sword.\"")
sh(8, "Shahrazad looked towards King Shahryar with her lovely eyes and, with great courtesy, asked for permission.")
sh(9, "\"O noble king, will you give me leave to go on with the story?\" \"Yes, tell it quickly!\"")
sh(10, "King Shahryar said hurriedly. \"Did that terrifying jinni kill the merchant?")
sh(11, "What did the old men who had come there do?\" Shahrazad adjusted her hair and, in a lovely,",
   [("cloth_rustle", "ރަނގަޅުކޮށްލުމަށްފަހު", -24)])
sh(12, "gentle voice, began the story. \"O mighty, wise king! Where I left off yesterday,")
sh(13, "that terrifying giant jinni had lifted his great sword up high and was ready to bring it down hard on the merchant's neck.",
   [("wind_gust", "ނަގައި", -20)])
sh(14, "At that moment the merchant shut his eyes and prepared to breathe his last. His heart almost stopped with fear. \"But,",
   [("heartbeat", "ހިތް", -16)], hum=True)
sh(15, "before the blade reached the merchant's neck, suddenly the First Old Man, who was there leading a gazelle, stepped "
       "forward, raised his hand and shouted in a voice like thunder:",
   [("footsteps_sand", "ޖެހިލައި", -20)])
sh(16, "\"'O mighty jinni! Stop! Do not bring that sword down!' the old man cried. The jinni stopped suddenly",
   [("smoke_whoosh", "ހުއްޓި", -20)])
sh(17, "and glared at the old man in anger with his blazing fiery eyes. 'Who are you?",
   [("fire_crackle", "އަލިފާން", -22)])
sh(18, "How dare you get in the way of my work? This man has killed my most beloved son. Spilling his blood is my right.'")
sh(19, "\"The old man with the gazelle looked straight at the jinni without any fear and said: 'O mighty jinni! I know")
sh(20, "that your son died at this man's hand, though he did not mean it, and that you want his life in return is understandable.")
sh(21, "But I have one very small request to ask of you. There is a most wondrous story that happened between me and this gazelle in my hand.")
sh(22, "I will tell you that story. If, after hearing it, you find my story far more wondrous than what happened between this man and your son,")
sh(23, "will you forgive one third of this man's blood for my sake and spare one third of his life?'")
sh(24, "\"The jinni sank into deep thought. Jinn and devils always love strange and wondrous stories very much.")
sh(25, "So the jinni lowered his great sword and said: 'Very well. Tell me your story.",
   [("smoke_whoosh", "ތިރިކޮށްލުމަށްފަހު", -22)])
sh(26, "If that story truly amazes me and is wondrous, I will forgive one third of this man's blood for your sake.'")
sh(27, "\"At that, the old man with the gazelle stroked the head of the gazelle in his hand and, to the jinni,")
sh(28, "to the merchant shaking with fear, and to the others there, began to tell his story. \"'O mighty jinni!",
   [("breath_heavy", "ތުރުތުރުއަޅަމުންދިޔަ", -22)])
sh(29, "Listen well. This gazelle I lead here on a chain is in truth no ordinary animal. She is my elder brother's daughter.")
sh(30, "And she is also my own wife. \"'She and I married when we were both very young.")
sh(31, "We lived a happy life together. But even when thirty years of our marriage had passed,")
sh(32, "God had not granted us the blessing of a child. The sorrow of having no child was always in my heart.", hum=True)
sh(33, "To have a child born of one's own flesh and blood is one of the things every human being longs for most. And so,")
sh(34, "after thirty years, I thought of another way. I went to the market, bought a very beautiful young slave girl, brought her home",
   [("footsteps_pavement", "ބާޒާރަށް", -24)])
sh(35, "and made her my own. \"'Not many days later, by God's mercy, that slave girl conceived and bore me a very beautiful baby boy.")
sh(36, "That child's beauty was like the moon. With him, my whole world was filled with joy.")
sh(37, "I loved that child and his mother beyond measure. But when my wife, that is, this gazelle, saw this happiness,")
sh(38, "a great fire of jealousy was kindled in her heart. She began to hate my slave girl and my innocent child intensely.")
sh(39, "She hid it from me, but her heart was full of evil. \"'That boy grew up,")
sh(40, "and when he reached ten years of age, I had to make a long journey to a very distant country for trade.")
sh(41, "Before setting off, I entrusted my son and his mother to my wife,")
sh(42, "and charged her to look after them well. Then I set off. \"'My journey took one whole year.",
   [("footsteps_sand", "ފުރައިގެން", -22)])
sh(43, "During that one year, to quench her jealousy, my wife went to wicked sorcerers and learned the evil art of magic and sorcery.",
   [("magic_shimmer", "ސިހުރު", -20)])
sh(44, "Once she had mastered that art, she cast a spell on my beautiful slave girl and turned that poor woman into a cow.",
   [("magic_shimmer", "ބަދަލުކޮށްލިއެވެ", -18)])
sh(45, "And she cast a spell on my beloved ten-year-old son and turned the boy into a little calf. After that,",
   [("magic_shimmer", "ބަދަލުކޮށްލިއެވެ", -18)], hum=True)
sh(46, "she called the man who kept my cattle and handed the two animals over to him. She told him they were two newly "
       "bought animals and ordered him to keep them with the others.")
sh(47, "\"'When I finished my journey, came back to the island and entered the house, the very first thing I asked was "
       "where my beloved son and his mother were.",
   [("door_open", "ވަނުމާއެކު", -20)])
sh(48, "My wife, pretending to be in great sorrow, said through her tears: 'O my husband!",
   [("sob_breath", "ރޮމުންރޮމުން", -24)])
sh(49, "A little while after you left, that slave girl of yours fell gravely ill and died suddenly.")
sh(50, "And in his grief your son went out of his mind, left the house and ran away. Though we searched the whole island, no one could find where he went.'")
sh(51, "\"'When I heard this news it was as if my heart burst. I began to sob and weep. All the joy of my life was lost.",
   [("sob_breath", "ގިސްލާފައި", -18)], hum=True)
sh(52, "For many months I mourned, remembering my son. \"'In this way a year went by.", hum=True)
sh(53, "Then came the happy days of the great Eid. I ordered my cattle-keeper to bring me the fattest, most beautiful cow "
       "to sacrifice for the Eid.")
sh(54, "What he brought me was my slave girl, whom my wife had turned into a cow by sorcery. But I knew nothing of it.")
sh(55, "\"'When I went up to the cow to sacrifice it and took up the knife, the cow looked at me and began to weep loudly.")
sh(56, "Big teardrops rolled from its eyes. It began to rub its head against my feet as if it were pleading.",
   [("breath", "ކަރުނަތިކިތައް", -22)], hum=True)
sh(57, "This sight moved my heart deeply. The knife slipped from my hand and fell. I could not bring myself to sacrifice that cow.",
   [("soft_thud", "ވެއްޓުނެވެ", -20)], hum=True)
sh(58, "I called the cattle-keeper and said: 'Take this cow away! Bring another, better cow than this!'")
sh(59, "\"'But my wife came there, very angry, and began to shout: 'No! Sacrifice that cow! It is the fattest,")
sh(60, "the best cow we have. For the Eid only the best must be sacrificed.' As she went on and on like this,")
sh(61, "I was forced to have the cattle-keeper sacrifice the cow. That poor creature was sacrificed with tears pouring from its eyes.",
   hum=True)
sh(62, "\"'But the wonder was that when the cow was sacrificed and skinned, there was not a scrap of meat on it, not even "
       "a bit of fat. It was nothing but a skeleton.")
sh(63, "It had looked fat only because of the sorcery. I was very upset and said angrily to my wife:")
sh(64, "'Look what a wrong I have done by giving in to your words! Now it has been sacrificed. Throw its bones to the dogs!")
sh(65, "And call the cattle-keeper and tell him to bring a fat young calf instead.' \"'The cattle-keeper next brought a small young calf.")
sh(66, "It was my own beloved son! As soon as the little one saw me, it broke its rope, came running and wrapped itself round my feet.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(67, "It wept loudly, rubbing its head against my face and hands. Seeing the tears streaming from its eyes broke my heart to pieces.",
   hum=True)
sh(68, "I understood that it was no ordinary animal. I felt that in its own language it was pleading with me for mercy.")
sh(69, "\"'At once I ordered the cattle-keeper: 'Take this calf away! Do it no harm at all. Bring something else and sacrifice that instead!'")
sh(70, "\"'Once again my wife came there and began to shout louder than before: 'No! Sacrifice that one!")
sh(71, "There is nothing better than it!' For a long time she shouted, trying to make me have the calf sacrificed.")
sh(72, "But this time I did not listen to her. Because of the pity and love that had arisen in my heart for that little calf, I would not agree.")
sh(73, "I ordered the cattle-keeper to take the calf away and look after it safely. \"'The next day,")
sh(74, "the cattle-keeper came to me secretly and said: 'O master! I want to give you happy news.",
   [("footsteps_pavement", "ކައިރިއަށް", -24)])
sh(75, "My daughter is a very gifted girl who knows how to undo the evil arts of magic and sorcery.")
sh(76, "Yesterday, as soon as I took home the young calf you saved, my daughter knew what it was.")
sh(77, "She said it is your own son! Your wife turned him into a calf by sorcery.")
sh(78, "And the cow you sacrificed yesterday was your slave girl!' \"'When I heard this, I felt as if the sky had fallen on my head.",
   [("heartbeat", "ވެއްޓުނު", -16)], hum=True)
sh(79, "I burst into tears. I grieved beyond measure that my beloved slave girl had been sacrificed by my own hand.",
   [("sob_breath", "ރޮއިގަތީމެވެ", -18)], hum=True)
sh(80, "I hurried to the cattle-keeper's house and met his daughter.",
   [("footsteps_sand", "ގޮސް", -22)])
sh(81, "I begged that girl to save my son. \"'The girl said: 'O master!")
sh(82, "I can save your son. But I can do it only on two conditions. The first condition is")
sh(83, "that once your son has become human again, he marries me. The second condition is")
sh(84, "that, as a just punishment for your wife, you give me permission to cast a spell on her and turn her into an animal.'")
sh(85, "\"'Without any hesitation I agreed to both conditions. Then the girl put some things into a bowl of water",
   [("pour", "ފެންތައްޓަކަށް", -20)])
sh(86, "and recited words in an unknown tongue and blew on it, then splashed that water on the calf. At once the young calf began to tremble",
   [("water_splash_small", "ޖެހިއެވެ", -18), ("magic_shimmer", "ތުރުތުރުއަޅައިގަނެ", -18)])
sh(87, "and changed into the shape of my beloved, beautiful son! I ran to my son, threw my arms around him and wept, sobbing with joy.",
   [("magic_shimmer", "ބަދަލުވިއެވެ", -20), ("sob_breath", "ގިސްލަގިސްލާފައި", -22)], hum=True)
sh(88, "\"'After that I married my son to that girl. And the girl went to my wife,")
sh(89, "cast a spell on her and turned her into this gazelle here. O mighty jinni! This is the story that happened between me and this gazelle.",
   [("magic_shimmer", "ސިހުރު", -18)])
sh(90, "Is it not a wondrous story?' \"The jinni lowered his great sword to the ground and, in great astonishment, said: 'Yes!",
   [("smoke_whoosh", "ތިރިކޮށްލުމަށްފަހު", -22)])
sh(91, "That is truly a most wondrous story. For the excellence of your story, I forgive you one third of this merchant's blood.'",
   hum=True)
sh(92, "\"At these words, the Second Old Man, who was there with two black dogs, stepped forward. He called to the jinni and said:",
   [("footsteps_sand", "ޖެހިލިއެވެ", -22)])
sh(93, "'O mighty jinni! The story that happened between me and these two black dogs is even more wondrous than this.")
sh(94, "If I tell you that story and it proves even better, will you forgive another third of this man's blood for my sake?'\"")
sh(95, "Just as Shahrazad brought the story to this point, the lovely golden light of dawn appeared on the horizon and the "
       "call to the dawn prayer began to be heard.")
sh(96, "Shahrazad at once broke off the story and fell politely silent. King Shahryar was lost inside the story.")
sh(97, "Suddenly he sat up and said: \"Then what happened? What is the story of those two black dogs? Did the jinni agree?\"",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(98, "Shahrazad smiled gently. \"O noble king, it is dawn. My time is over.")
sh(99, "But if I am still in this world tomorrow night, I will tell you the Second Old Man's story.")
sh(100, "It is many times more beautiful and more wondrous than the First Old Man's story.\"")
sh(101, "The fire of curiosity in King Shahryar's heart grew even greater. He was certain he could not bear it without "
        "knowing the secret of those two black dogs.", hum=True)
sh(102, "So today too the king decided to let Shahrazad go without killing her. And he rose, put on his royal robes,",
    [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(103, "and went to the court to govern. The third night was over. By Shahrazad's wisdom",
    [("footsteps_pavement", "ވަޑައިގަތެވެ", -24)])
sh(104, "and the magic of her stories, King Shahryar was slowly being bound. To be continued.")
SHOTS = S

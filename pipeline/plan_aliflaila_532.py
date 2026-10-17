"""Beat/shot plan for Aliflaila episode 532 (Night 6) - used by plan_beats.py.
FRAME: Shahryar's palace chamber, night -> dawn. TALE (Shahrazad): the poor old fisherman's four casts, the brass jar with
Sulaiman's seal, the colossal jinni rising from the smoke (cliffhanger). No tale-within-the-tale in this episode.
Bible rules applied: the dead donkey stays hidden inside the tangled net (rule 8); bones / broken glass = shells, seaweed
and driftwood (rule 8); the seal = an abstract glowing eight-petalled rosette, no letters (rule 9); Prophet Sulaiman never
depicted; the fisherman wades in his tunic (rule 12) and prises the stopper off with his bare hands and a flat stone,
never a knife (rule 1); the executioner's sword is never drawn; every woman's headscarf fully covers hair and neck."""

FISHER = ("the old fisherman in his faded patched blue long-sleeved tunic, rough beige cloth wrapped as a long skirt to "
          "his shins with a rope belt, white skullcap, scruffy grey beard, bare feet")
NOWEAPON = "nobody holds anything sharp, no knife, no sword, no weapon anywhere"
JINNI = ("the colossal jinni: a huge upper body in a long-sleeved midnight-purple robe with gold bands, a tall gold-banded "
         "dark turban, a long black forked beard, blazing golden eyes, his lower body a swirling tail of glittering "
         "indigo-violet smoke rising out of the brass jar, both hands empty")
JAR = ("a large gleaming round-bellied brass jar with a narrow neck, its mouth closed by a thick dull-grey lead stopper "
       "stamped with a softly glowing abstract eight-petalled geometric rosette (no letters, no star)")

LOC = {
    "palace_ext": "the vast palace of King Shahryar seen from outside at night: white and sand-coloured walls, onion domes "
                  "and slender towers, a city of domes around it, a huge pale moon and a sky full of twinkling stars",
    "chamber_night": "King Shahryar's palace bedchamber at night: a deep Persian carpet with silk cushions, a low cushioned "
                     "divan with silk curtains, brass lanterns with warm amber light, an arched carved lattice window "
                     "showing the moonlit city of domes",
    "chamber_dawn": "King Shahryar's palace chamber at dawn: a deep Persian carpet with silk cushions, a low cushioned divan, "
                    "brass lanterns burning low, golden dawn light streaming through the arched carved lattice window "
                    "with the city of domes outside",
    "hut": "a tiny poor palm-thatched hut of driftwood and mud beside a sandy beach at the edge of an old Arabian seaside "
           "town, a patched cloth hanging in the doorway, an old net drying on poles, palms and a calm sea beyond",
    "shore_predawn": "a long empty sandy beach before sunrise, gentle waves, palm trees along the shore, the white domes of "
                     "a small seaside town far behind",
    "shore_dawn": "the shallows of a long sandy beach at sunrise, gentle turquoise waves, rocks and palms along the shore",
    "shore_morning": "the sandy shore and rocky point of an Arabian seaside at bright morning, clear turquoise sea, white "
                     "foam, palms and dunes",
    "underwater": "the clear turquoise water just off the beach, a sandy seabed with rocks and swaying seaweed, beams of "
                  "sunlight slanting down through the surface",
    "shore_dark": "the same sandy beach suddenly dark at midday: a towering column of glittering black-indigo smoke "
                  "blotting out the sun, the sea and sand dim beneath it",
    "city_dawn": "the capital city of domes at the first light of dawn seen from the palace terrace, a slender minaret in "
                 "silhouette against a rose-and-gold eastern sky, the last stars fading",
    "durbar": "King Shahryar's grand throne hall in the morning: tall marble columns, a raised golden throne under a silk "
              "canopy, sunlight pouring through high arched windows, courtiers in turbans standing in rows",
}
MOOD = {
    "palace_ext": "deep midnight blue night, silver moonlight, a few warm amber lit windows, hushed, expectant",
    "chamber_night": "the last quiet hour of the night, deep midnight blue shadows with warm amber lantern glow, intimate "
                     "storytelling hush, eager anticipation",
    "chamber_dawn": "dawn, warm golden light through the lattice mixing with the last amber lantern glow, suspense turning "
                    "to gentle relief",
    "hut": "late afternoon, soft warm light, poor but tender, a quiet sadness",
    "shore_predawn": "before sunrise, cool blue-violet sky brightening to pale rose at the horizon, hopeful stillness",
    "shore_dawn": "sunrise, rose and gold light on the water, long soft shadows, hope and effort",
    "shore_morning": "bright morning, golden sunlight and turquoise sky, sparkling sea",
    "underwater": "bright daylight filtered through turquoise water, shimmering light rays, effort and wonder",
    "shore_dark": "sudden eerie darkness at midday, the sun hidden, cold violet gloom lit by glittering sparkles in the "
                  "smoke and the jinni's blazing golden eyes, awe and terror",
    "city_dawn": "dawn, golden light rising over the domes, peaceful and holy",
    "durbar": "full morning, bright golden sunlight, grand and orderly",
}

BEATS = [
    # ---------------- FRAME: night ----------------
    dict(to=2, reason="episode opening: night six falls over Shahryar's palace", loc="palace_ext",
         visual="the great palace of domes and slender towers at night under a huge pale moon and a sky full of "
                "twinkling stars, a single warm amber glow in a high arched window of the royal chamber, the quiet city "
                "of domes spreading below; no people visible",
         camera="wide establishing shot, low angle, moon and domes in the upper two-thirds, dark garden wall and "
                "still reflecting pool as a calm lower third", amb="palace_night"),
    dict(to=6, reason="scene change: inside the chamber, Dunyazad softly asks her sister for the promised tale",
         chars=["dunyazad", "shahrazad", "shahryar"], loc="chamber_night",
         visual="Dunyazad sitting on the carpet beside her sister, leaning toward her and whispering eagerly with big "
                "bright curious eyes and clasped hands; Shahrazad sitting on a silk cushion on the carpet, turning to "
                "her with a calm clever smile; King Shahryar sitting upright fully dressed on the divan an arm's length "
                "away, leaning forward impatiently; lattice window with the moonlit domes behind; every headscarf fully "
                "covers hair and neck; the king empty-handed",
         camera="medium wide three-shot, eye level, faces in the upper two-thirds, carpet as the calm lower third",
         amb="palace_night"),
    dict(to=9, reason="action change: Shahrazad bows her head to ask the king's permission; he orders her to begin",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_night",
         visual="Shahrazad seated on her cushion, lowering her head respectfully with one hand on her heart, her large "
                "dark eyes lifted toward the king; King Shahryar on the divan an arm's length away gesturing with an "
                "open empty hand 'begin!', his brooding eyes eager; Dunyazad small on the carpet beside her sister "
                "smiling; amber lanterns glowing",
         camera="medium shot over Dunyazad's shoulder, eye level", amb="palace_night"),
    # ---------------- TALE ----------------
    dict(to=12, reason="scene change: Shahrazad's tale begins - the poor old fisherman and his hungry family",
         chars=["fisherman"], loc="hut", transition="dissolve",
         visual=f"{FISHER}, sitting on a mat in front of his tiny palm-thatched hut, sadly breaking one dry piece of "
                "bread into small pieces; his wife (a thin woman in a plain long brown gown and a plain brown headscarf "
                "fully covering her hair and neck) and their three small sons in simple patched white tunics and white skullcaps sit around a "
                "single clay water jug as small figures; the calm sea beyond",
         camera="medium wide, eye level, the family in the upper two-thirds, sand as the calm lower third",
         amb="village_day"),
    dict(to=15, reason="focus change: the fisherman alone with his net and his rule of four casts a day",
         chars=["fisherman"], loc="hut",
         visual=f"{FISHER}, standing alone in the doorway of the hut, carefully folding his big cast net over his "
                "shoulder, a determined, dignified look, holding up four fingers of his free hand as if reminding "
                "himself of his rule; old net drying on poles beside him",
         camera="medium shot, slightly low angle", amb="village_day"),
    dict(to=16, reason="time jump: one morning before sunrise he walks to the shore", chars=["fisherman"],
         loc="shore_predawn", transition="black",
         visual=f"{FISHER}, walking barefoot along the empty beach before sunrise with the heavy folded net over his "
                "shoulder, his footprints trailing behind him in the cool sand, the first rose glow on the horizon, "
                "hope on his tired face",
         camera="wide shot, from the side, the figure and sky in the upper two-thirds, sand as calm lower third",
         amb="seashore_dawn"),
    dict(to=18, reason="action change: he wades in and throws the first cast", chars=["fisherman"], loc="shore_dawn",
         visual=f"{FISHER}, standing knee-deep in the shallows still wearing his tunic (his beige outer wrap folded on "
                "the sand behind him), whirling the cast net out of his hands so it opens into a wide glittering circle "
                "in the rose-gold sunrise air, his lips moving in a quiet prayer",
         camera="medium wide, low angle from the water, the opening net in the upper half", amb="seashore_dawn"),
    dict(to=21, reason="action change: the net grows heavy - joy, then hauling with all his strength",
         chars=["fisherman"], loc="shore_dawn",
         visual=f"{FISHER}, leaning back hard on the taut rope at the water's edge with both hands, heels dug into the "
                "wet sand, sweat on his brow, chest heaving, a hopeful excited grin through the strain; the rope "
                "disappearing into the sunlit waves",
         camera="medium shot, three-quarter view, eye level", amb="seashore_dawn"),
    dict(to=25, reason="emotional turning point: the first catch is a disgusting load, not fish", chars=["fisherman"],
         loc="shore_dawn", sens="other",
         safe="the dead donkey is never shown: only a big heavy tangled net, its contents hidden by the knotted mesh, "
              "seaweed and foam; the fisherman recoils pinching his nose",
         visual=f"{FISHER}, recoiling from a big lumpy heavily tangled net lying at the waterline, pinching his nose "
                "with one hand and turning his face away in dismay, his shoulders sagging; the contents of the net "
                "completely hidden by thick knotted mesh, dark seaweed and sea foam; nothing inside is visible",
         camera="medium shot, eye level, his face in the upper third, the hidden net low in frame",
         amb="seashore_dawn"),
    dict(to=27, reason="the second cast at another spot - same action as the first cast", reuse="beat_007",
         chars=["fisherman"], loc="shore_dawn", visual="(reuse of beat_007: casting the net)", amb="seashore_dawn"),
    dict(to=29, reason="action change: he plunges into the water and hauls the second heavy net",
         chars=["fisherman"], loc="shore_dawn",
         visual=f"{FISHER}, waist-deep in the sunrise sea in his wet tunic, gripping the rope with both fists and "
                "pulling with all his might, feet braced, spray flying, eager hope in his eyes",
         camera="medium wide, from the shore, eye level", amb="seashore_dawn"),
    dict(to=32, reason="emotional turning point: only a pot of mud - he weeps and laments", chars=["fisherman"],
         loc="shore_dawn",
         visual=f"{FISHER}, sitting slumped on the wet sand beside a big cracked clay pot overflowing with grey mud, "
                "sand and seaweed tangled in his net, tears running down his lined cheeks, one hand raised in a "
                "mournful lament, exhausted",
         camera="medium shot, eye level", amb="seashore_dawn", hum=True),
    dict(to=34, reason="location/action change: the third cast into deeper water with a sad prayer",
         chars=["fisherman"], loc="shore_morning",
         visual=f"{FISHER}, standing on a low flat rock at the end of a rocky point, throwing his net in a wide arc "
                "into deeper sapphire water, his face sad and prayerful, the sun now risen over the sea",
         camera="wide shot, low angle from the rocks, the figure and net against the sky", amb="seashore_day"),
    dict(to=36, reason="action change: the third net is full of rubbish from the seabed", chars=["fisherman"],
         loc="shore_morning", sens="other",
         safe="bones and broken glass shown as shells, seaweed and grey driftwood tangled in the net (bible rule 8)",
         visual=f"{FISHER}, kneeling over his opened net on the sand, staring blankly at a tangle of empty shells, "
                "dark seaweed, pebbles and grey driftwood, his hands hanging loose, his patience broken",
         camera="medium high angle looking down past his shoulder", amb="seashore_day"),
    dict(to=41, reason="emotional turning point: he kneels and prays tearfully for his family", chars=["fisherman"],
         loc="shore_morning",
         visual=f"{FISHER}, kneeling on the sand facing the bright sea horizon, both palms raised before his chest in "
                "humble supplication, eyes lifted, tears shining on his cheeks, soft golden light falling on him from "
                "the sky",
         camera="medium shot from the side, slightly low angle, the sky filling the upper two-thirds",
         amb="seashore_day", hum=True),
    dict(to=43, reason="action change: the fourth and final cast, thrown with all his courage", chars=["fisherman"],
         loc="shore_morning",
         visual=f"{FISHER}, standing in the shallows and flinging the net high with both arms, the net spreading into "
                "a huge perfect circle against the sun with glints of sparkling light, a determined face full of hope",
         camera="dramatic low angle from behind and to the side, the spreading net and sun in the upper half",
         amb="seashore_day"),
    dict(to=44, reason="the net won't budge - same hauling action as before", reuse="beat_008",
         chars=["fisherman"], loc="shore_dawn", visual="(reuse of beat_008: hauling the heavy rope)",
         amb="seashore_day"),
    dict(to=46, reason="location change: he dives under the water to free the snagged net", chars=["fisherman"],
         loc="underwater",
         visual=f"{FISHER}, swimming underwater in his tunic with puffed cheeks and determined eyes, tugging his net "
                "free from where it is snagged around a large round shape half-buried in the sandy seabed among rocks "
                "and swaying seaweed, sunbeams slanting down, small fish darting away",
         camera="medium wide underwater view, light from the surface at the top", amb="seashore_day"),
    dict(to=50, reason="emotional turning point: the reveal of the sealed brass jar in the net", chars=["fisherman"],
         loc="shore_morning", sens="other",
         safe="Prophet Sulaiman is not depicted; his seal = an abstract glowing eight-petalled rosette with no letters",
         visual=f"close on {JAR}, lying in the wet net on the sand, gleaming richly in the sunlight with a soft "
                "magical glow; behind it the panting old fisherman sitting on the sand, leaning in with wide amazed "
                "eyes",
         camera="close-up of the jar in the lower-middle, the fisherman's face in the upper third", amb="seashore_day"),
    dict(to=53, reason="action change: he lifts the heavy jar with a joyful smile", chars=["fisherman"],
         loc="shore_morning",
         visual=f"{FISHER}, lifting {JAR} up in both arms with effort, beaming with joy, eyes shining, already "
                "dreaming of the bazaar; sparkling sea behind him",
         camera="medium shot, slightly low angle", amb="seashore_day"),
    dict(to=56, reason="action change: he shakes it, listens and grows curious", chars=["fisherman"],
         loc="shore_morning",
         visual=f"{FISHER}, sitting on the sand holding the heavy brass jar to his ear, one eyebrow raised, eyes "
                "narrowed in curious suspicion, listening; the glowing rosette on the lead stopper close to his face",
         camera="medium close-up, eye level", amb="seashore_day"),
    dict(to=59, reason="action change: he prises the lead stopper off", chars=["fisherman"], loc="shore_morning",
         sens="other",
         safe="the narration's knife is replaced: he prises the stopper loose with his bare hands and a flat stone "
              "(bible rule 1); " + NOWEAPON,
         visual="close-up of the old fisherman's weathered bare hands gripping the brass jar between his knees and "
                "tapping and levering the thick lead stopper with the rosette loose using a flat grey beach stone; the "
                "stopper just lifting off, a thin wisp of dark sparkling smoke beginning to curl from the gap; his "
                "straining face above; " + NOWEAPON,
         camera="close-up on the hands and jar, face in the upper third", amb="seashore_day"),
    dict(to=61, reason="action change: thick black smoke pours out and darkens the sky", chars=["fisherman"],
         loc="shore_dark", sens="other", safe="magic shown as fairy-tale glittering smoke, never horror",
         visual=f"a towering column of thick glittering black-indigo smoke pouring out of the open brass jar on the "
                "sand and billowing up into the sky, hiding the sun and darkening the sea and beach; "
                f"{FISHER}, small at its base, stepping back with his arm raised against the swirling smoke",
         camera="wide shot, low angle, the smoke column filling the upper two-thirds", amb="seashore_day"),
    dict(to=66, reason="emotional turning point: the smoke forms a colossal jinni", chars=["jar_jinni", "fisherman"],
         loc="shore_dark", sens="other",
         safe="the jinni is a fairy-tale giant with empty hands, awe-inspiring but not gory",
         visual=f"{JINNI}, towering up into the dark clouds above the beach, his head among the clouds like a great "
                "dome, arms crossed, huge golden eyes blazing down like two lanterns; far below at the bottom of the "
                f"frame the tiny figure of {FISHER}, staring up; " + NOWEAPON,
         camera="extreme low angle from the sand, the jinni's face high in the upper third, the tiny fisherman near "
                "the bottom", amb="seashore_day", hum=True),
    dict(to=68, reason="reaction shot: the fisherman falls back in terror, speechless", chars=["fisherman"],
         loc="shore_dark",
         visual=f"{FISHER}, fallen backward onto the sand, propped on his elbows, mouth open but silent, teeth "
                "chattering, eyes huge with terror, lit by a golden glow from above; the open brass jar beside him "
                "trailing indigo smoke",
         camera="medium close-up, high angle as if from the jinni's view", amb="seashore_day", hum=True),
    dict(to=69, reason="the jinni roars - back to the towering jinni image", reuse="beat_024",
         chars=["jar_jinni", "fisherman"], loc="shore_dark", visual="(reuse of beat_024: the towering jinni)",
         amb="seashore_day"),
    dict(to=72, reason="action change: the jinni bows down to the ground begging for mercy",
         chars=["jar_jinni", "fisherman"], loc="shore_dark", sens="other",
         safe="Prophet Sulaiman is not depicted: the jinni bows toward empty sand and golden light, the bewildered "
              "fisherman is the only person present",
         visual=f"{JINNI}, now bent low over the beach with his huge turbaned head bowed to the sand and his empty "
                "hands clasped in pleading, his golden eyes wide with fear; the bewildered old fisherman sitting "
                "small on the sand before him, staring in confusion; glittering smoke swirling around",
         camera="wide shot, eye level from the side", amb="seashore_day", hum=True),
    # ---------------- FRAME: dawn ----------------
    dict(to=73, reason="scene change out of the tale: dawn breaks over the capital (Fajr)", loc="city_dawn",
         transition="dissolve", sens="other",
         safe="the call to prayer = a distant minaret silhouette against the dawn sky; the adhan is not synthesised",
         visual="the city of domes at first light seen over a palace balustrade, a slender minaret in dark silhouette "
                "against a rose-and-gold eastern sky, the last stars fading, birds rising; no people",
         camera="wide shot, the sky and minaret in the upper two-thirds, rooftops as calm lower third",
         amb="mosque_dawn"),
    dict(to=75, reason="scene and focus change: the king sits up, wide-eyed, demanding more",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="King Shahryar sitting bolt upright on the divan fully dressed, eyes wide, one empty hand stretched "
                "out in urgent demand; Shahrazad seated on her cushion on the carpet an arm's length away, calm and "
                "silent with lowered eyes; Dunyazad beside her on the carpet; golden dawn light through the lattice",
         camera="medium wide, eye level, the king in focus", amb="palace_dawn"),
    dict(to=79, reason="focus change: Shahrazad smiles and promises the rest for tomorrow night",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_dawn",
         visual="Shahrazad seated on her cushion smiling gently and gesturing gracefully with an open hand toward the "
                "golden dawn light at the lattice window; the king on the divan an arm's length away, leaning forward, "
                "spellbound with burning curiosity; Dunyazad smiling beside her sister, her pale pink headscarf pulled low over her forehead so that no hair at all shows at the hairline",
         camera="medium shot centred on Shahrazad, eye level", amb="palace_dawn"),
    dict(to=81, reason="scene change: the king spares her again and goes to his court", chars=["shahryar"],
         loc="durbar", sens="violence",
         safe="the executioner and his sword are never shown; the postponed execution = the king calmly taking his "
              "throne in the morning light; " + NOWEAPON,
         visual="King Shahryar in his crimson plumed turban and bronze brocade coat walking up the steps to his golden "
                "throne, empty-handed, with a thoughtful hint of a smile; only small bearded male courtiers in turbans and long robes bowing in rows, no women in the hall, nobody carrying anything; bright "
                "morning sunbeams through high windows; " + NOWEAPON,
         camera="wide shot, low angle down the hall", amb="throne_hall"),
    dict(to=82, reason="closing: the seventh night lies ahead - return to the night palace image", reuse="beat_001",
         loc="palace_ext", transition="black", visual="(reuse of beat_001: the palace at night)", amb="palace_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Night Six: the tale of the poor fisherman and the brass jar. As the deep darkness of the sixth night spread over the world and the stars began to twinkle in the sky, into King Shahryar's great,")
sh(2, "awe-inspiring palace a deep silence descended. The king's mind was filled with eagerness, longing for a new story.")
sh(3, "On the fifth night Shahrazad had promised the tale of the poor fisherman and the terrifying jinni, and he lay impatient to hear it. As the last,")
sh(4, "stillest moment of the night drew near, Dunyazad, sitting by the bed as usual, softly called her sister.")
sh(5, "\"Dear sister,\" said Dunyazad, her voice full of eagerness and expectation, \"if you are not asleep, the new story you promised yesterday,")
sh(6, "the tale of the poor fisherman and the wondrous jar he found in the sea - please tell it to us.\" Shahrazad, with her beautiful,")
sh(7, "deep-black eyes, looked toward King Shahryar, and bowing her head with great respect, asked his permission.")
sh(8, "\"O noble and mighty king, will you grant me permission to begin this new story?\" \"Begin at once!\"")
sh(9, "King Shahryar said quickly. \"My heart longs to know what the fisherman found in the sea and what terrible creature came out of it.\"")
sh(10, "Shahrazad began the tale in her soft, lovely voice. \"O mighty and wise king! Long ago, on the shore of an inhabited land,")
sh(11, "there lived a very poor fisherman, advanced in age. He had a wife and three children.")
sh(12, "Their condition was extremely low. The family lived in poverty and hunger.",
   [("sigh", "ދަށެވެ", -22)])
sh(13, "On many days all they had to eat was a piece of dry bread and a sip of water. But this fisherman was very diligent in his work, and he followed a strict rule he had made for himself.")
sh(14, "His rule was that every day he would go to the sea and cast his net only four times.")
sh(15, "Under no circumstances would he cast more than that; he would come home with whatever he got. One day at dawn, long before sunrise,")
sh(16, "the old fisherman put his big net over his shoulder and set out for the shore, hoping to find provision for his family.",
   [("footsteps_sand", "ނުކުމެއްޖެއެވެ", -20)])
sh(17, "Walking on, he stopped at the water's edge, took off his outer garment, stepped down into the water, said the name of God,",
   [("water_splash_small", "ފައިބައި", -20)])
sh(18, "whirled his net at arm's length and threw it into the sea. Then he began to wait. After a little while the rope grew taut,",
   [("net_cast", "ހޫރާލައި", -16)])
sh(19, "and he felt the net become extremely heavy. He was overjoyed. 'Today God has granted me a huge fish, or many fish!'")
sh(20, "he said to himself. To drag the net onto land he began to pull the rope with all the strength of his body.",
   [("breath_heavy", "ދަމަން", -20)])
sh(21, "The net was so heavy that he could barely pull it. His chest heaved, his breath grew short, and his whole body poured with sweat. At last,",
   [("breath_heavy", "ނޭވާ", -20)])
sh(22, "with enormous effort, he brought the net ashore and looked to see what was inside. But his joy at once turned to grief and despair.",
   [("sigh", "މާޔޫސްކަމަށް", -20)])
sh(23, "There was not a single fish in the net. Instead there lay a big dead donkey, already rotting.")
sh(24, "Saddened, the fisherman said 'Inna lillahi wa inna ilayhi raji'un' and grieved over his bad luck.",
   [("sigh", "ދެރަވެފައި", -20)])
sh(25, "He removed the rotten donkey from the net, threw it away, washed the net well, cleaned it and spread it out again.",
   [("water_splash_small", "ދޮވެ", -22)])
sh(26, "Then he went to another part of the sea, said 'Bismillah' again, and cast his net a second time.",
   [("net_cast", "އެއްލިއެވެ", -16)])
sh(27, "This time too, after a little while, the net became extremely heavy - even heavier than the first time.")
sh(28, "'This time it must surely be a huge fish!' the fisherman thought hopefully. He plunged into the water, grabbed the rope of the net,",
   [("splash", "ފީނައިގަނެ", -18)])
sh(29, "planted his feet on the ground and began to pull with all his strength. After a long hard struggle he brought the net ashore and opened it.",
   [("breath_heavy", "ދަމަން", -20)])
sh(30, "But this time too he got nothing worth having. In the net, instead of fish, lay a big clay pot full of mud, sand and muck.")
sh(31, "The fisherman's heart was utterly broken. His old body was exhausted. Saddened, complaining to himself of the world's misfortune and his poverty, he recited a lament in verse,",
   [("sob_breath", "ދެރަވެފައި", -22)], hum=True)
sh(32, "and weeping, he took the clay pot out of the net and threw it away. Again he washed the net, cleaned it and cleared away the mud.",
   [("sob_breath", "ރޮމުންރޮމުން", -22), ("soft_thud", "އެއްލާލިއެވެ", -18)])
sh(33, "To make his third cast he went to a somewhat deeper part of the sea, and praying to God in his sorrow, he cast the net.",
   [("net_cast", "އެއްލިއެވެ", -16)])
sh(34, "This time, as the net reached the bottom, it again became very heavy. With great difficulty,")
sh(35, "spending a long time, he brought the net ashore. But when he opened it, there were only broken glass bottles,")
sh(36, "bones, shells and all sorts of rubbish from the seabed. At this sight the fisherman's patience came to an end.",
   [("sigh", "ކޮޅުންލައިފިއެވެ", -20)])
sh(37, "He fell to his knees, raised both hands toward the sky, and with tearful eyes began to plead before God.",
   [("cloth_rustle", "ތިރިވެ", -22), ("sob_breath", "ކަރުނަވީ", -22)])
sh(38, "'O Lord who decrees all things and grants provision! As You know well,", hum=True)
sh(39, "this servant of Yours casts his net only four times a day. This is my fourth and last time.")
sh(40, "At home my wife and three children are waiting in hunger. O God! Put Your blessing in my net this time,")
sh(41, "and grant my family good provision so that they may eat!' After this prayer the fisherman gathered all his courage,", hum=True)
sh(42, "said 'Bismillahir-Rahmanir-Rahim' and hurled his fourth and final net into the sea. The net spread out in the air",
   [("net_cast", "ހޫރާލިއެވެ", -16)])
sh(43, "and sank into the salt water. After waiting a little while the fisherman pulled the rope, but it would not move at all.",
   [("splash", "ޣަރަޤުވެގެން", -20)])
sh(44, "The net was stuck on something extremely heavy and large at the bottom of the sea. Though the fisherman pulled with all the strength of his body,",
   [("breath_heavy", "ދެމި", -20)])
sh(45, "the net did not come up even a little. In the end he was forced to dive into the water to free the net from where it was stuck.")
sh(46, "He dived, freed the net with hard work, and with great difficulty dragged it ashore. Exhausted and gasping for breath,",
   [("splash", "ފީނައިގެން", -18), ("breath_heavy", "މާނޭވާ", -20)])
sh(47, "the fisherman sat down beside the net and looked to see what was inside. This time too there was not a single fish! But instead,")
sh(48, "in the net lay an extremely heavy, large jar of brass, of a wondrous shape.",
   [("magic_shimmer", "ރަތުރަނުގެ", -20)])
sh(49, "The jar was beautifully polished, and its mouth was sealed with a thick lid of lead,")
sh(50, "and on the lead was stamped a large, special seal. It was the noble seal of God's Prophet Sulaiman! When he saw this brass jar,",
   [("magic_shimmer", "ސިއްކަފުޅެވެ", -20)])
sh(51, "a smile of joy spread across the old fisherman's face. He took the jar in his hands and looked at it. It was very heavy.")
sh(52, "'Praise be to God!' he cried out in joy. 'This is a very valuable brass jar.")
sh(53, "If I take this jar to the bazaar and sell it to the metal sellers, I will get at least ten gold dinars.")
sh(54, "Then my family will have food for many days.' He shook the jar. He felt that it was full inside.",
   [("metal_lid", "ތަޅުވާލިއެވެ", -22)])
sh(55, "But no sound came from inside. Curiosity rose in his heart. 'What can be inside, so heavy?")
sh(56, "There may be precious jewels in it. Before I sell this jar, I want to see what is inside.' With this thought,")
sh(57, "the fisherman took the small knife tucked into his waistband, and pushed its tip under the jar's lead lid,")
sh(58, "and with great force tried to prise the lid loose. After a long struggle, at last the thick lead lid came loose and fell to the ground.",
   [("stone_scrape", "މަސައްކަތްކުރިއެވެ", -20), ("soft_thud", "ވެއްޓިއްޖެއެވެ", -16)])
sh(59, "He set the jar on the ground and watched to see whether anything would come out. At first nothing at all came out of the jar.")
sh(60, "But after a short moment, a very thick, pitch-black smoke began to pour out of the jar. The smoke kept rising,",
   [("smoke_whoosh", "ދުންގަނޑެއް", -16)])
sh(61, "spread across the sky, hid the light of the sun and darkened the whole area. The smoke spread over the salt sea and the land.",
   [("wind_gust", "އަނދިރިކޮށްލިއެވެ", -18)])
sh(62, "Then suddenly the thick smoke gathered, solidified, and from it took shape an extremely terrifying, colossal, enormous jinni!",
   [("magic_shimmer", "ގަނޑުވެ", -18)], hum=True)
sh(63, "O noble king! The height of that jinni was such that while the soles of its feet touched the ground, its head reached the clouds.")
sh(64, "Its head looked like a great dome. Its two arms looked like huge, long palm trunks. Its legs looked like the trunks of great trees.")
sh(65, "Its mouth looked like a deep dark cave. Its teeth looked like great boulders of the mountains. Its nose looked like a vast pool.")
sh(66, "Its two eyes looked like two great blazing torches. It was a form more terrifying than a human heart could imagine. At this terrifying sight,",
   [("heartbeat", "ފެނުމާއެކު", -18)])
sh(67, "all the strength drained from the old fisherman's body, his teeth chattered, and he fell backward in fright.",
   [("gasp", "ބިރުންގޮސް", -18), ("soft_thud", "ވެއްޓުނެވެ", -18)], hum=True)
sh(68, "Not a single word came out of his mouth. The giant jinni looked at the fisherman with its blazing eyes,")
sh(69, "and roared with a voice as loud as thunder, enough to shake the whole earth: 'La ilaha illallah! There is no god but God!",
   [("thunder", "ގުގުރިއެއްހާ", -14)])
sh(70, "And Sulaiman is His prophet!' the jinni cried. Then the jinni bowed down to the ground and spoke in a pleading tone.",
   [("soft_thud", "ތިރިވެ", -18)])
sh(71, "'O Sulaiman, Prophet of God! Do not kill me! Never again will I disobey your command!", hum=True)
sh(72, "I will obey you completely!'\" As Shahrazad brought the story to this point, the beautiful golden light of dawn appeared in the east.")
sh(73, "The sweet sound of the Fajr call to prayer spread through the air of the whole capital. At that, Shahrazad at once broke off the story and fell respectfully silent.")
sh(74, "King Shahryar was completely lost in the story. His eyes were wide open. Suddenly the king sat up and said,",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(75, "\"Then what happened? Why did the jinni call out the name of Sulaiman? Tell me quickly what happened to that fisherman!\"")
sh(76, "Shahrazad smiled gently. \"O noble king, it is dawn. My time is over.")
sh(77, "But if I am still in this world tomorrow night, I will tell you the secret of that jinni, and how the poor fisherman faced the giant jinni with his cleverness.")
sh(78, "That is an even more thrilling and frightening story.\" The curiosity in King Shahryar's heart had grown beyond measure.")
sh(79, "He was certain he could not bear not knowing what would happen next between the fisherman and the jinni. And so,")
sh(80, "today too the king decided to spare Shahrazad and let her live. And rising, he put on his royal robes,",
   [("cloth_rustle", "ތުރުކުރައްވައިގެން", -22)])
sh(81, "and went to the court to govern. The sixth night ended. Thanks to Shahrazad's great skill in storytelling, the executioner's sword was put off once again for another day.",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -20)])
sh(82, "Next comes the seventh night, when the fisherman's cleverness will be revealed.")
SHOTS = S

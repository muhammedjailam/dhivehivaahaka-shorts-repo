"""Beat/shot plan for Aliflaila episode 599 (Night 9; used by plan_beats.py).
FRAME: Shahryar's chamber in the last hour of night -> dawn. TALE (Shahrazad): the four-coloured fish -> the cook
faints, the Vizier and then the Sultan see the wonder (a towering shadow-smoke figure from the kitchen wall), the
march to the hidden lake, the Sultan alone in the mountains, the empty black-stone castle, the weeping young prince
who is black marble from the waist down (his sorceress wife's curse). Dawn cliffhanger.
Bible rules: no sword or weapon anywhere (the Sultan walks into the mountains empty-handed; soldiers carry banners
only); the "very black slave" of the narration = a towering faceless figure of dark swirling shadow-smoke with glowing
eyes, NOT a human of any race (rule 11); the marble prince stays seated in his long robe, only his black marble
feet/shins below the hem are visible (rule 11); every woman's headscarf fully covers hair and neck; no text."""

SHADOW = ("a towering faceless figure made entirely of dark swirling charcoal-grey shadow-smoke with two glowing amber "
          "eyes and no human features at all, wisps of smoke curling off its edges, its head brushing the ceiling, a "
          "leafy green tree branch held in one smoky hand")
PRINCE = ("the marble prince seated upright on a golden throne in his long white-and-gold silk robe falling to his "
          "ankles and his white turban with a ruby jewel")
FRAME_PEOPLE = ("Shahrazad sitting on a cushion on the carpet in her saffron-gold gown and ivory headscarf fully covering "
                "her hair and neck; little Dunyazad on the carpet beside her in her lavender gown and pink headscarf fully "
                "covering her hair and neck; King Shahryar in his crimson plumed turban and bronze brocade coat sitting "
                "fully dressed on a cushioned divan more than an arm's length away")

LOC = {
    "chamber_predawn": "King Shahryar's palace bedchamber: Persian carpets, silk cushions, a long cushioned divan, brass "
                       "lanterns, an arched carved lattice window looking out over a city of white onion domes and slender "
                       "towers",
    "kitchen": "the Sultan's grand palace kitchen: thick whitewashed stone walls with arched niches, copper pots and pans "
               "hanging on hooks, a long brick cooking hearth with a glowing charcoal fire and a wide iron frying pan, "
               "baskets of onions and herbs, a tiled floor",
    "vizier_room": "the Grand Vizier's richly furnished office chamber in the Sultan's palace: a low carved writing desk "
                   "with closed scrolls tied with ribbon, cushions, arched window with turquoise sky",
    "lake": "a hidden crystal-clear turquoise mountain lake in a hollow ringed by four tall rocky mountains, smooth stones "
            "at the shore, a few wild palms",
    "throne_hall": "the Sultan's sunlit throne hall: tall marble columns, a raised golden throne under a sapphire-blue "
                   "canopy, Persian carpets, arched windows with light streaming in",
    "mountain_march": "a rocky mountain track winding up between four tall sandstone mountains under a turquoise sky",
    "lake_camp": "the crystal-clear lake between four mountains with a royal camp of striped silk pavilions and pennants "
                 "being set up along the shore",
    "tent_night": "inside the Sultan's large royal silk pavilion at night: hanging brass lanterns, carpets and cushions, the "
                  "tent flap open to a starry sky over dark mountains",
    "mountains_night": "a desolate rocky mountain pass at night, jagged dark peaks, a huge full moon, deep silence",
    "castle_ext": "a vast lonely castle built entirely of polished black stone with black domes and towers, standing on a "
                  "barren plateau among the mountains, its huge arched gate standing wide open",
    "castle_inside": "the splendid empty interior of the black-stone castle: an open courtyard garden with fragrant "
                     "flowering trees, marble fountains spraying pearl-like water, silk carpets and hangings, walls inlaid "
                     "with gold, silver and glittering jewels in floral patterns",
    "castle_corridor": "a long silent gold-inlaid corridor inside the black-stone castle with tall arches, silk curtains, "
                       "and at the far end a huge carved doorway with soft light spilling out",
    "castle_hall": "the innermost great audience hall of the black-stone castle: a gleaming floor, black-stone columns "
                   "inlaid with gold, silk hangings, a raised golden throne in the centre",
    "vision": "the crystal-clear lake between four mountains seen as a dreamlike vision",
    "chamber_dawn": "King Shahryar's palace bedchamber at sunrise: Persian carpets, silk cushions, a long cushioned divan, "
                    "brass lanterns now dimmed, an arched carved lattice window with a distant minaret silhouette against "
                    "the dawn sky over a city of domes",
    "darbar": "King Shahryar's grand royal court hall in the morning: tall arched windows, marble columns, a raised throne, "
              "courtiers in turbans standing in rows",
}
MOOD = {
    "chamber_predawn": "the last hour of night, deep midnight blue with warm amber lantern light, a first faint pale glow "
                       "on the horizon beyond the domes, a cool breeze stirring the curtains, hushed and eager",
    "kitchen": "daytime, warm firelight from the hearth mixed with golden sunlight from a high window, then eerie green "
               "and grey magical light, wonder and dread",
    "vizier_room": "daytime, golden sunlight, tense and disbelieving",
    "lake": "bright morning, golden sunlight sparkling on turquoise water, mysterious and magical",
    "throne_hall": "daytime, golden sunlight in shafts between the columns, grave and curious",
    "mountain_march": "bright midday, golden sunlight, purposeful and adventurous",
    "lake_camp": "late afternoon, warm golden light glittering on the clear water, wondrous",
    "tent_night": "night, warm amber lanterns inside, deep midnight blue outside, restless and secretive",
    "mountains_night": "night, deep midnight blue, silver moonlight, lonely, silent and brave",
    "castle_ext": "sunrise after a long night, pale rose-gold dawn light against the black stone, awe and foreboding",
    "castle_inside": "morning, soft golden light falling into an utterly empty splendour, eerie silence, wonder",
    "castle_corridor": "morning, long shadows and a warm glow from the far doorway, urgency and suspense",
    "castle_hall": "morning, soft golden light from high windows on the golden throne, sorrowful and tender",
    "vision": "soft dreamy storybook glow, misty silver-blue light, melancholy and mysterious",
    "chamber_dawn": "sunrise, warm golden dawn light pouring through the lattice window, rose and gold sky, the night's "
                    "tale cut short, gentle relief",
    "darbar": "bright morning, golden sunlight in shafts, calm and dignified",
}

BEATS = [
    dict(to=5, reason="episode opening: the frame chamber in the last hour of night; Dunyazad asks for the tale",
         chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber_predawn",
         visual=f"{FRAME_PEOPLE}; Dunyazad leaning eagerly towards her sister with clasped hands and big pleading eyes, "
                "Shahrazad turning to her with a calm smile and one graceful hand raised as she begins the story, the king "
                "leaning forward on the divan with a curious intent gaze; a curtain stirring in the breeze at the window",
         camera="wide three-shot, eye level, the window and domes in the upper part, the carpet as a calm lower third",
         amb="palace_night"),
    dict(to=8, reason="scene change: into the tale - the palace kitchen after the woman vanished; the cook has fainted",
         chars=["palace_cook"], loc="kitchen",
         visual="the plump palace cook sitting dazed on the tiled floor leaning back against the hearth, one hand on his "
                "forehead, eyes wide with fright, staring up at the iron frying pan where four fish have turned to black "
                "charcoal with thin smoke curling up; on the whitewashed wall behind, a faint fading green glow where a "
                "crack is closing; soft golden storybook glow",
         camera="medium wide, slightly low angle", amb="palace_kitchen", transition="dissolve", sens="other",
         safe="the fainting is shown only as the cook sitting dazed afterwards; nobody lies on the floor"),
    dict(to=10, reason="scene and character change: the weeping cook reports to the Grand Vizier",
         chars=["sultan_vizier", "palace_cook"], loc="vizier_room",
         visual="the plump cook standing before the Sultan's round rust-robed vizier, wiping tears with his apron and "
                "gesturing wildly as he tells his tale; the vizier sitting at his desk with raised eyebrows and a "
                "sceptical, astonished frown, one finger lifted",
         camera="medium two-shot, eye level", amb="palace_day"),
    dict(to=12, reason="scene change: the fisherman goes back to the hidden lake and casts his net",
         chars=["fisherman"], loc="lake",
         visual="the thin old fisherman in his patched blue tunic standing at the edge of the turquoise lake, casting his "
                "round net in a wide graceful arc over the water; in the clear water below, four fish - one white, one "
                "red, one blue and one yellow - glinting; the four mountains towering behind",
         camera="wide shot, low angle, the mountains and net in the upper two-thirds, still water as the lower third",
         amb="lake_mountains"),
    dict(to=13, reason="scene and action change: the vizier himself fries the four fish in the kitchen",
         chars=["sultan_vizier"], loc="kitchen",
         visual="the round vizier in his rust-orange robe and orange turban standing at the hearth with his sleeves "
                "rolled to the wrist, carefully turning four colourful fish (white, red, blue, yellow) in the sizzling "
                "iron pan with a wooden spatula, glancing nervously over his shoulder at the whitewashed wall",
         camera="medium shot, eye level, from beside the hearth", amb="palace_kitchen"),
    dict(to=16, reason="strong turning point: the wall splits and a towering shadow figure steps out",
         chars=["sultan_vizier"], loc="kitchen",
         visual=f"the whitewashed kitchen wall split open in a jagged glowing crack, and out of it rises {SHADOW}, "
                "looming over the frying pan and roaring; the small round vizier stumbling back against the hearth with "
                "his hands raised and his mouth open in terror; grey-green magical light and swirling smoke",
         camera="dramatic low angle, the shadow figure filling the upper two-thirds, the vizier small in the lower left",
         amb="palace_kitchen", sens="other",
         safe="bible rule 11: the 'very black slave' is drawn as a faceless shadow-smoke figure, not a human of any race"),
    dict(to=18, reason="action change: the fish in the pan raise their heads and answer",
         loc="kitchen",
         visual="close-up of the wide iron frying pan on the hearth: four fish - white, red, blue and yellow - lifting "
                "their heads out of the pan and answering, little glittering sparkles around them; the huge dark "
                "smoky shadow of the towering figure falling across the pan from above",
         camera="close-up, high angle looking into the pan", amb="palace_kitchen", sens="other",
         safe="magic shown as fairy-tale sparkles; the figure only as a cast shadow"),
    dict(to=21, reason="action change: the pan is overturned, the figure vanishes, the vizier trembles",
         chars=["sultan_vizier"], loc="kitchen",
         visual="the iron frying pan lying overturned on the hearth with blackened ash and a puff of grey smoke, the "
                "last wisps of dark smoke being sucked back into a closing crack in the wall; the round vizier pressed "
                "against a side wall, trembling all over, eyes huge, clutching his turban with both hands",
         camera="medium wide, eye level", amb="palace_kitchen"),
    dict(to=23, reason="scene change: the throne hall - the Sultan hears the report and summons the fisherman",
         chars=["fish_sultan", "sultan_vizier", "fisherman"], loc="throne_hall",
         visual="the Sultan in his sapphire-blue robe and white turban seated on his golden throne, leaning forward with "
                "a determined, curious expression and one hand raised in command; the round vizier bowing beside the "
                "throne; the old fisherman kneeling on the carpet below holding up a woven basket with four colourful "
                "fish",
         camera="wide shot, slight low angle towards the throne", amb="throne_hall"),
    dict(to=25, reason="scene and action change: the Sultan and the vizier alone in the locked kitchen frying the fish",
         chars=["fish_sultan", "sultan_vizier"], loc="kitchen",
         visual="the Sultan in his sapphire-blue robe standing at the hearth himself, turning the four colourful fish in "
                "the iron pan with a wooden spatula, the vizier at his side holding up a lantern; the heavy wooden "
                "kitchen door behind them shut and barred; on the wall a dark crack beginning to split open with "
                "smoke seeping out; both turning towards it",
         camera="medium two-shot, eye level", amb="palace_kitchen"),
    dict(to=27, reason="strong turning point: the Sultan witnesses the shadow figure and the burned fish himself",
         chars=["fish_sultan", "sultan_vizier"], loc="kitchen",
         visual=f"{SHADOW}, already sinking back into the cracked wall in swirling smoke; the iron pan overturned on the "
                "hearth with blackened fish; the Sultan standing firm with a stern, astonished face and narrowed "
                "knowing eyes, the vizier cowering behind him; grey-green magical light",
         camera="medium wide, low angle from the hearth", amb="palace_kitchen", sens="other",
         safe="bible rule 11: the figure is faceless shadow-smoke, not a human"),
    dict(to=31, reason="scene and action change: the Sultan questions the fisherman about the lake",
         chars=["fish_sultan", "fisherman"], loc="throne_hall",
         visual="the Sultan standing down from his throne, bending towards the old fisherman with an intent questioning "
                "look; the fisherman, holding his folded net, pointing out through a tall arched window towards distant "
                "mountains on the horizon; the Sultan's eyebrows raised in amazement",
         camera="medium two-shot, eye level, the window and mountains in the background", amb="throne_hall"),
    dict(to=33, reason="scene change: the Sultan's army marches to the mountains guided by the fisherman",
         chars=["fish_sultan", "fisherman", "sultan_vizier"], loc="mountain_march",
         visual="a royal procession winding up the mountain track: the old fisherman walking ahead pointing the way, the "
                "Sultan riding a white horse in his sapphire robe, the vizier on a brown mule behind, and a long column "
                "of soldiers in turbans carrying only tall coloured banners and pennants, no weapons",
         camera="wide shot, high angle along the winding track", amb="caravan_road"),
    dict(to=34, reason="scene change: arrival at the crystal lake between four mountains; the camp is pitched",
         chars=["fish_sultan"], loc="lake_camp",
         visual="the Sultan standing on the shore of the crystal-clear lake, looking down in wonder at the white, red, "
                "blue and yellow fish swimming in the clear water; behind him servants raising striped silk pavilions "
                "and pennants; the four mountains all around",
         camera="wide shot, the lake and mountains in the upper two-thirds, the clear shallows as the lower third",
         amb="lake_mountains"),
    dict(to=36, reason="time jump to night: in the royal tent the Sultan confides his plan to the vizier",
         chars=["fish_sultan", "sultan_vizier"], loc="tent_night",
         visual="the Sultan standing inside the lantern-lit pavilion, his hand on his chest, speaking quietly and "
                "resolutely to the anxious vizier, who wrings his hands; through the open tent flap the dark mountains "
                "and a huge moon",
         camera="medium two-shot, eye level", amb="mountain_night", transition="black"),
    dict(to=38, reason="scene change: the Sultan walks alone into the dark mountains",
         chars=["fish_sultan"], loc="mountains_night",
         visual="the Sultan seen from behind and a little to the side, walking alone and empty-handed up a moonlit rocky "
                "path between dark jagged peaks, his sapphire robe and white turban silvered by the huge full moon, the "
                "tiny glowing pavilions of the camp far below",
         camera="wide shot, the moon and peaks in the upper two-thirds, the rocky path as the lower third",
         amb="mountain_night", sens="violence",
         safe="the narration's sharp sword is not shown: the Sultan walks empty-handed"),
    dict(to=41, reason="time jump to the next morning: the black-stone castle appears",
         chars=["fish_sultan"], loc="castle_ext",
         visual="a small figure of the Sultan seen from behind on a rocky ridge at sunrise, gazing at the vast castle of "
                "polished black stone with black domes and towers rising from the plateau, its enormous arched gate "
                "standing open; rose-gold dawn light glinting on the black stone",
         camera="extreme wide shot, low angle, the castle in the upper two-thirds", amb="desert_dawn",
         transition="black"),
    dict(to=45, reason="scene change: inside the splendid, utterly empty castle",
         chars=["fish_sultan"], loc="castle_inside",
         visual="the Sultan, small in the frame, stepping in wonder through a vast empty courtyard garden of the black "
                "castle: flowering trees, marble fountains spraying pearl-like water, silk carpets, walls glittering "
                "with gold, silver and jewel-inlaid floral patterns; not another soul anywhere",
         camera="wide shot, eye level, symmetrical", amb="empty_castle"),
    dict(to=48, reason="action change: he hears weeping and hurries towards the sound",
         chars=["fish_sultan"], loc="castle_corridor",
         visual="the Sultan hurrying down the long gold-inlaid corridor towards the huge carved doorway at the far end, "
                "one hand raised to his ear, his face full of compassion and alarm, his robe swirling; soft light "
                "spilling from the doorway",
         camera="medium wide, from behind and to the side", amb="empty_castle", sens=None),
    dict(to=53, reason="character enters: the weeping young prince on the golden throne",
         chars=["marble_prince", "fish_sultan"], loc="castle_hall",
         visual=f"{PRINCE}, a handsome young man with tears running down his cheeks and a sorrowful noble face, one hand "
                "on his heart in apology; the Sultan standing at a respectful distance before the throne, his right "
                "hand on his chest in greeting, his face kind and puzzled; the prince's long robe falls in heavy folds "
                "to the floor and completely hides his feet - no feet visible at all (the reveal comes later)",
         camera="medium wide two-shot, slight low angle towards the throne", amb="empty_castle"),
    dict(to=57, reason="strong turning point: the reveal - the prince is black marble below the robe",
         chars=["marble_prince", "fish_sultan"], loc="castle_hall",
         visual=f"{PRINCE}, still seated, lifting the hem of his robe only a few inches above his ankles to show that his "
                "feet and lower shins are polished black marble merged into the base of the throne, a faint cold sheen "
                "on the stone; the Sultan in the foreground with a shocked face, eyes wide, one hand pressed to his "
                "chest; the prince's tearful eyes lowered",
         camera="medium shot, eye level, the prince's face and the Sultan's face in the upper two-thirds, the marble "
                "feet in the middle",
         amb="empty_castle", sens="other",
         safe="bible rule 11: the prince stays seated in his long robe; only the black marble feet/shins below the hem "
                "are visible; no body horror"),
    dict(to=60, reason="emotional change: the Sultan's compassionate question; the prince wipes his tears",
         chars=["fish_sultan", "marble_prince"], loc="castle_hall",
         visual="close two-shot: the Sultan leaning towards the seated prince with deep sympathy, one open hand extended "
                "in a gentle questioning gesture; the prince, still on his throne in his long robe, wiping his tears with "
                "the back of his hand and drawing a deep breath",
         camera="medium close-up two-shot, eye level", amb="empty_castle"),
    dict(to=62, reason="symbolic image: the fish were once people; the wife's sorcery cursed the land",
         loc="vision",
         visual="the crystal lake seen from above in a dreamy vision: four fish - white, red, blue and yellow - swimming "
                "in circles, and in the rippling water faint glowing reflections of crowds of townspeople in turbans and "
                "headscarves; above the lake a dark swirl of violet-green magical smoke curling over the distant "
                "black-stone castle; soft golden storybook glow",
         camera="wide shot, high angle", amb="dream_glow", transition="dissolve", sens="other",
         safe="the sorceress wife is not shown; her curse only as magical smoke; people as faint reflections"),
    dict(to=65, reason="scene and time change: back to the frame chamber at dawn; Shahrazad falls silent",
         chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber_dawn",
         visual=f"{FRAME_PEOPLE}; golden dawn light pouring through the lattice window across the carpet; Shahrazad "
                "falling silent with lowered hands and a small knowing smile, Dunyazad looking up at her with wide "
                "astonished eyes and both hands raised in a pleading question; the king sitting up attentively",
         camera="wide three-shot, eye level, the dawn window and minaret silhouette in the upper part",
         amb="palace_dawn", transition="dissolve"),
    dict(to=69, reason="emotional turning point: Shahrazad's promise; the king decides to spare her another day",
         chars=["shahryar", "shahrazad"], loc="chamber_dawn",
         visual="King Shahryar on the divan in the golden dawn light, his chin resting on his hand, his stern face "
                "softening into thoughtful curiosity; in the soft-focus background Shahrazad sitting on her cushion, "
                "smiling gently with her hands folded",
         camera="medium close-up on the king, eye level, Shahrazad blurred behind", amb="palace_dawn", sens="other",
         safe="the threat to Shahrazad's life is shown only as the king's thoughtful face; no executioner"),
    dict(to=70, reason="scene change: the king goes to his court for the day's affairs",
         chars=["shahryar"], loc="darbar",
         visual="King Shahryar seen from behind walking down the middle of his sunlit court hall towards the raised "
                "throne, courtiers in turbans bowing on both sides",
         camera="wide shot, eye level, symmetrical", amb="throne_hall"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "As the darkness of the night slowly faded and light began to appear over the world with the cool breezes of dawn, Dunyazad called out to her elder sister Shahrazad.",
   [("wind_gust", "ރޯޅިތަކާއެކު", -24)])
sh(2, "\"Dear sister! If you are not asleep, please continue the tale of those wondrous many-coloured fish and the mysterious woman who broke through the kitchen wall.")
sh(3, "I am terribly impatient to know what happened after those fish burned to ash.\"")
sh(4, "In King Shahryar's heart, too, a strong eagerness had arisen to discover this secret.")
sh(5, "So the king gave permission to continue the tale. Shahrazad began most courteously: \"O noble and mighty King!",
   [("cloth_rustle", "ފެށިއެވެ", -24)])
sh(6, "As that beautiful woman went back into the kitchen wall and vanished, the fish in the frying pan turned into black charcoal and burned.",
   [("magic_shimmer", "ގެއްލުމާއެކު", -20)])
sh(7, "The cook in the kitchen, seeing this sight, fainted from fright and fell to the floor. When he came to a while later and looked,",
   [("gasp", "ބިރުންގޮސް", -22), ("soft_thud", "ވެއްޓުނެވެ", -18)])
sh(8, "the fish were burned to coal, not fit to eat. Weeping, he went and presented himself before the Grand Vizier,",
   [("sob_breath", "ރޮމުންރޮމުން", -24)])
sh(9, "and told him every terrifying thing that had happened, word for word. The Grand Vizier, astonished, said: 'That is truly a most wondrous thing.")
sh(10, "But I will not believe it until I see it with my own eyes.' The vizier at once ordered the fisherman to be brought.")
sh(11, "When the fisherman came the vizier said: 'O fisherman! Bring me today too four fish of four colours, like the ones you brought yesterday.'")
sh(12, "The fisherman hurried off, cast his net into that mysterious lake among the mountains, caught four fish of four colours once again, and brought them to the vizier.",
   [("net_cast", "ދާގަނޑު", -18)])
sh(13, "The vizier himself cleaned the fish, poured oil into the pan and began to fry them. When one side of the fish was cooked and he turned them over,",
   [("pour", "ތެޔޮ", -22), ("fire_crackle", "ތެއްލަން", -22)])
sh(14, "suddenly the kitchen wall split in two. But this time it was not the beautiful woman who came out. Instead there came out an extremely terrifying, huge,",
   [("stone_scrape", "ދެފަޅިވެގެން", -14), ("smoke_whoosh", "ބިރުވެރި", -18)])
sh(15, "very dark slave. His head reached the kitchen ceiling. In his hand was a branch of a big green tree. That terrifying slave",
   hum=True)
sh(16, "shouted at the fish in a voice as loud as thunder: 'O fish! Are you keeping your covenant?'",
   [("thunder", "ގުގުރިއެއް", -18)])
sh(17, "At that the fish in the pan raised their heads and answered in clear human speech: 'Yes! Yes!",
   [("magic_shimmer", "ހިއްލާލައި", -22)])
sh(18, "If you come back, we will come back too. If you depart, we will depart too.' As soon as they said this,")
sh(19, "the huge slave struck the pan with the branch in his hand, the pan overturned and the fish burned to ash.",
   [("crash_clatter", "ބަންޑުންވެ", -16), ("smoke_whoosh", "އަޅިއަށް", -20)])
sh(20, "And he went back into the wall and vanished. The vizier began to tremble with fear. He was certain that this was no ordinary matter,",
   [("stone_scrape", "ގެއްލުނެވެ", -20), ("breath_heavy", "ތުރުތުރުއަޅަން", -20)])
sh(21, "and that behind it lay a great sorcerous secret. He went at once to the king and told him of this frightening and wondrous event.")
sh(22, "The king said: 'This is something I want to see with my own eyes. This is the most extraordinary thing that has ever happened in my kingdom.'")
sh(23, "The king summoned the fisherman and ordered him to bring four fish again. When the fisherman went for the third time and brought the fish,")
sh(24, "the king went to the kitchen himself, had the doors locked, and alone with the vizier began to fry the fish.",
   [("door_close", "ދޮރުތައް", -18), ("lock_click", "ލައްޕަވައި", -18)])
sh(25, "Everything happened just as before. When the fish were turned over the wall burst open, and a terrifying giant came out and questioned the fish.",
   [("stone_scrape", "ފަޅައިގެންގޮސް", -14)])
sh(26, "And when the fish answered, he overturned the pan and vanished. The fish lay burned and black.",
   [("crash_clatter", "ބަންޑުންކޮށްލާފައި", -16)])
sh(27, "The king became certain that these were no ordinary fish. They were people who had fallen victim to some sorcery.")
sh(28, "He questioned the fisherman: 'O fisherman! Where do you catch these fish?' The fisherman replied: 'O noble King!")
sh(29, "I catch these fish in a lake that lies between four mountains outside this town.'")
sh(30, "The king asked: 'How far from this town is that place?' The fisherman said: 'It is half an hour's walk.'")
sh(31, "The king was utterly astonished, for neither he nor any of his viziers had ever known that such a lake lay so close to his kingdom, so short a way off.")
sh(32, "The king at once ordered an army to be made ready and to travel to that lake under the fisherman's guidance.")
sh(33, "The king, the viziers and the army of soldiers set off towards the mountains. Just as the fisherman had said, between the four mountains lay a very beautiful,",
   [("horse_hooves", "މިސްރާބުޖެހިއެވެ", -22)])
sh(34, "crystal-clear lake. And in it those fish of four colours were swimming. The king ordered the tents to be pitched there.",
   [("water_splash_small", "ފަތަމުން", -24)])
sh(35, "And when night came he called the vizier and said: 'My heart has no rest until I discover the great secret behind this.")
sh(36, "Tonight I will go into these mountains all alone and find out the secret. Until I return, let no one come out of the tent.")
sh(37, "And if anyone asks, say that the king is unwell and is resting in private.' The king took up his sharp sword,")
sh(38, "and began to walk into the mountains through the darkness of the night. There was nothing there but desolation and silence.",
   [("footsteps_sand", "ހިންގަވަން", -22), ("wind_howl", "ހިމޭންކަން", -24)])
sh(39, "He walked the whole night through, and at sunrise the next morning he saw, far in the distance, a huge, very dark building.")
sh(40, "When he came close to it and looked, it was no ordinary place. It was built entirely of smooth black stone,")
sh(41, "a vast and perfect castle with the strength of iron. The castle's great gate stood open.")
sh(42, "The king entered the castle. Inside lay the finest silk carpets. The splendour of gold and silver spread throughout the whole place.",
   [("footsteps_pavement", "ވެދެވަޑައިގަތެވެ", -24)])
sh(43, "In the great gardens stood fragrant flowering trees and fountains gushing like pearls.")
sh(44, "The walls were decorated with costly jewels. Yet there was no life in that place - not even the trace of a human being to speak to.")
sh(45, "The whole place lay in a deep and frightening silence. The king went into the different rooms of the castle, calling out,",
   [("footsteps_pavement", "ވެދެވަޑައިގެން", -24)])
sh(46, "looking to see if he could find anyone. Suddenly, out of that deep silence, there reached his ears the sound of a most heartbreaking, moving weeping.",
   [("sob_breath", "ރުއިމެއްގެ", -22)])
sh(47, "Someone was weeping and describing his sorrows and helplessness in verses that would break one's heart.", hum=True)
sh(48, "The king hurried towards where the sound was coming from. It came from the great audience hall in the innermost part of the castle.",
   [("footsteps_pavement", "އަވަސްއަވަހަށް", -20)])
sh(49, "When the king entered that room and looked, on a golden throne in the middle of it sat a very handsome young prince.",
   [("door_open", "ވެދެވަޑައިގެން", -22)])
sh(50, "Royalty and nobility shone from his face. He was wearing a silk robe of the very finest quality.")
sh(51, "But his eyes were full of tears of sorrow. The king went to him and greeted him kindly. After returning the greeting, the young man")
sh(52, "said, weeping: 'O noble sir! Forgive me for not rising to my feet to show you respect.", hum=True)
sh(53, "It is not out of pride that I cannot rise. When you see the reason, you will understand.'")
sh(54, "Having said this, the young prince lifted the lower part of the silk robe he wore.",
   [("cloth_rustle", "ހިއްލާލިއެވެ", -20)])
sh(55, "The sight the king saw then almost stopped his heart. What he saw was hard even to believe.",
   [("heartbeat", "ހުއްޓޭވަރު", -18)], hum=True)
sh(56, "From the young man's waist down to his feet, he had turned completely into black marble!",
   [("gasp", "ބަދަލުވެފައެވެ", -22)], hum=True)
sh(57, "He was half a living man, and the other half a lifeless statue of stone! He could not even move from that spot.")
sh(58, "With astonishment and deep sympathy the king said: 'O young man! What great calamity has befallen you?")
sh(59, "What secret links this desolate black-stone castle, the fish of four colours in that lake, and your condition? Come then,")
sh(60, "tell me your sad story!' The young prince drew a deep breath and, wiping away his tears, said: 'O noble sir!",
   [("sigh", "ނޭވާއެއްލައި", -20)])
sh(61, "My story is one that would soften even hearts of stone and make them shed tears. The fish in that lake were not fish before.")
sh(62, "They were living people. And this castle and this land were struck by such great wrath because of the wickedness and sorcery of my own wife.'",
   hum=True)
sh(63, "Just as the prince was ready to begin his story...\" - when the tale had reached this point, the lovely light of dawn came into the room, and the sun rose.")
sh(64, "Shahrazad broke off her story at once and fell silent. Dunyazad said in astonishment: \"O sister!")
sh(65, "What a wondrous and heartbreaking tale this is! Why did that young prince's wife do him such great harm?")
sh(66, "And who are those fish of four colours?\" Shahrazad answered with a smile: \"That young man's story is even more thrilling and frightening than this.")
sh(67, "But dawn has come. If I am still in this world tomorrow night, I will tell you the truth about that wicked sorceress wife,")
sh(68, "how that young man turned to stone, and the efforts the noble king made to save him.\" King Shahryar,")
sh(69, "longing intensely to learn the secret of the prince turned to stone and the truth of those four-coloured fish, decided to spare Shahrazad's life for one more day.",
   hum=True)
sh(70, "And he went to the palace court to conduct the affairs of state for that day. (To be continued)",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -24)])
SHOTS = S

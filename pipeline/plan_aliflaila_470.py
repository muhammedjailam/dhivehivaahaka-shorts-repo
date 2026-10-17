"""Beat/shot plan for Aliflaila episode 470 (Night 2) (used by plan_beats.py).
FRAME: Shahryar's palace chamber at night -> golden dawn.  TALE: the Merchant and the Jinni, continued (the merchant's
year of grace, his return to the tree, the old man with the gazelle, the old man with the two black dogs, the sandstorm,
the jinni's return; cliffhanger).
Bible rules: the jinni NEVER holds a sword (empty raised fist / pointing finger, then cut away); the shroud is a folded
white cloth; the two black dogs sit calmly on leashes at a distance, never petted; every woman/girl's headscarf fully
covers hair and neck; Quran recitation = palms raised, no book with script; no text anywhere; minaret only as a distant
silhouette, the adhan is not synthesised."""

JINNI = ("the giant jinni (card merchant_jinni): lower body a swirling column of charcoal-grey smoke, dark ash-grey skin, "
         "smoky dark-red robe and turban, black beard, glowing ember-orange eyes, BOTH HANDS EMPTY, no weapon")
MERCHANT_RETURN = ("the merchant NOT in his striped robe but in a plain white travelling robe and white turban, a neatly "
                   "folded plain white cloth held in his hands")
FAMILY = ("two women of his household in long loose dark-blue and plum gowns with headscarves fully covering their hair "
          "and neck, a small boy in a cream tunic and a little girl in a long rose gown with a headscarf fully covering "
          "her hair")
DOGS = ("two big calm black dogs (ordinary dogs) sitting quietly on long leashes a few paces away from the men, "
        "not touched by anyone")
GAZELLE = "a very beautiful slender golden gazelle with a soft golden cord around its neck"

LOC = {
    "palace_ext": "King Shahryar's great white-and-sand palace of onion domes and slender towers above a sleeping city, "
                  "a huge full moon in a deep midnight-blue sky, every window dark except one high arched window glowing amber",
    "chamber": "King Shahryar's royal bedchamber: a cushioned divan with silk bolsters, a large Persian carpet with "
               "floor cushions, hanging brass lanterns, silk curtains, a tall arched window with a carved lattice screen "
               "looking out over a city of domes and minarets",
    "tree": "a lonely desert oasis: one huge old spreading shade tree beside a small spring among golden dunes, a few "
            "rocks, wide empty desert to the horizon",
    "road": "a wide desert road through rolling golden dunes, a distant walled town of sand-coloured houses and a dome on "
            "the horizon",
    "house": "the merchant's big comfortable house in his town: an arched courtyard with a small fountain, potted date "
             "palms, carpets and cushions under carved wooden arches, brass lamps",
    "storm": "the lonely desert tree by the spring in the middle of a violent sandstorm: whirling walls of orange sand "
             "rising to the sky, the tree bending in the wind",
}
MOOD = {
    "palace_ext": "deep night, midnight blue and silver moonlight, one warm amber window, hushed and still",
    "chamber": "deep night, midnight-blue shadows and warm amber lantern light, moonlight through the lattice, "
               "intimate storytelling suspense",
    "tree": "bright desert daylight, golden sun and turquoise sky, heat shimmer, tense and fateful",
    "road": "golden late-afternoon light, long shadows on the dunes, mixed grief and relief",
    "house": "warm daylight in the courtyard, soft amber lamps, family warmth turning into grief",
    "storm": "dark orange-brown storm light, swirling dust and sparks of ember light, terror and suspense",
    "chamber_dawn": "first light of dawn: rose and golden rays pouring through the lattice window, lanterns paling, "
                    "a distant minaret silhouette against the dawn sky, breathless suspense",
}
LOC["chamber_dawn"] = LOC["chamber"]

BEATS = [
    # ---------------- FRAME: night ----------------
    dict(to=1, reason="episode opening: the second night falls over the sleeping palace", loc="palace_ext",
         visual="a sweeping view of the great palace of domes and towers under a huge full moon at midnight, the whole "
                "city asleep and dark, a single high arched window glowing warm amber; no people visible",
         camera="wide establishing shot, slightly low angle, domes and moon in the upper two-thirds, dark palace "
                "gardens as a calm lower third", amb="palace_night"),
    dict(to=4, reason="scene change: inside the chamber, the king awake and Dunyazad whispering to her sister",
         chars=["shahryar", "dunyazad", "shahrazad"], loc="chamber",
         visual="King Shahryar reclining fully dressed on his cushioned divan, wide awake, propped on one elbow, "
                "impatient eyes turned towards the storytellers; an arm's length away on the carpet Shahrazad sits on a "
                "floor cushion and little Dunyazad sits beside her, leaning close and whispering eagerly to her sister "
                "with a hand beside her mouth; brass lanterns glowing, moonlit domes through the lattice window",
         camera="medium wide, eye level, the king on the left, the sisters on the right", amb="palace_night"),
    dict(to=7, reason="action change: Shahrazad asks the king's permission and begins with a smile",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber",
         visual="Shahrazad on her floor cushion turning gracefully towards the king with a gentle respectful bow of the "
                "head and a clever smile, one hand open in a storytelling gesture; King Shahryar on the divan an arm's "
                "length away leaning forward eagerly, waving a hand for her to begin; Dunyazad on the carpet beside her "
                "sister hugging her knees, big excited eyes; lantern glow and moonlight",
         camera="medium shot, eye level, Shahrazad in the foreground", amb="palace_night"),
    # ---------------- TALE ----------------
    dict(to=9, reason="story level change: into the tale - the jinni towering over the merchant under the tree",
         chars=["merchant_jinni", "merchant"], loc="tree", transition="dissolve",
         visual=f"{JINNI}, towering enormous over the shade tree with one huge EMPTY fist raised high against the sky, "
                "glaring down with blazing ember eyes; far below, the merchant kneels on the sand beside the spring with "
                "his eyes shut tight and his hands clasped, a single tear on his cheek",
         camera="dramatic low angle from behind the kneeling merchant, the jinni filling the upper two-thirds, sand as "
                "a calm lower third", amb="desert_day", sens="violence",
         safe="the narrated raised sword is never drawn: the jinni is empty-handed with a raised fist; no blow is shown"),
    dict(to=14, reason="action change: the merchant cries out and begs; the jinni answers in anger about its son",
         chars=["merchant", "merchant_jinni"], loc="tree",
         visual=f"the merchant on his knees on the sand reaching both open hands up in desperate pleading, tears "
                f"streaming, mouth open in a cry; {JINNI} bending down over him with a furious grieving face, one huge "
                "empty hand pointing an accusing finger at him; the shade tree and spring behind",
         camera="medium wide two-shot, slight low angle", amb="desert_day", sens="other",
         safe="the jinni's son's death is only spoken of, never shown; the jinni's grief and anger carry it"),
    dict(to=20, reason="action change: the merchant explains his trusts, his family and asks for one year",
         chars=["merchant", "merchant_jinni"], loc="tree",
         visual="close on the merchant kneeling, earnest and tearful, one hand pressed to his heart and the other "
                "gesturing towards the far horizon where his home lies; behind him a soft golden storybook glow in the "
                "sky shows a faint dreamy vision of a distant town of domes; the jinni's huge smoky dark-red shape "
                "looming out of focus at the edge of the frame",
         camera="medium close-up on the merchant, slightly high angle", amb="desert_day"),
    dict(to=25, reason="action change: the jinni demands a guarantee; the merchant raises his hand and swears by God",
         chars=["merchant", "merchant_jinni"], loc="tree",
         visual=f"the merchant standing now, his right hand raised solemnly to swear an oath, his face sincere and "
                f"brave, a soft golden ray of light falling on him from the sky; {JINNI} looming above with his arms "
                "folded across his chest and narrowed suspicious ember eyes, weighing the promise",
         camera="low angle two-shot, the jinni above, the merchant in the middle third", amb="desert_day",
         sens="other", safe="God's Name only as golden light from the sky; no script"),
    dict(to=27, reason="action change: the jinni turns to smoke and sinks into the ground; the merchant is alone",
         chars=["merchant_jinni", "merchant"], loc="tree",
         visual="the giant jinni dissolving into a great swirling spiral of charcoal smoke and glittering ember "
                "sparkles that pours down into the sand beside the tree; the merchant standing alone with one hand on "
                "his chest, eyes wide, breathing out in relief; his brown horse waiting nearby",
         camera="wide shot, the smoke spiral in the upper half", amb="desert_day", sens="other",
         safe="fairy-tale smoke and sparkles only, never horror"),
    dict(to=28, reason="scene change: the long ride home across the desert", chars=["merchant"], loc="road",
         visual="the merchant riding his brown horse across golden dunes towards a distant walled town on the horizon, "
                "his dusty travelling cloak flowing, his face torn between sorrow and relief",
         camera="wide shot, the rider in the upper half against the sky, dune slopes as the lower third",
         amb="caravan_road"),
    dict(to=30, reason="scene change: the family embraces him at home but he bursts into tears", chars=["merchant"],
         loc="house",
         visual=f"in the courtyard of his house the merchant has sunk onto a cushion weeping into one hand, while his "
                f"two small children cling joyfully to his robe and {FAMILY.split(', a small boy')[0]} stand close beside "
                "him, their happy faces turning to worry",
         camera="medium wide, eye level", amb="stone_house_day"),
    dict(to=34, reason="action change: he tells them the story; the whole house fills with grief", chars=["merchant"],
         loc="house",
         visual=f"the merchant sitting heavily on the carpet with his head bowed, speaking; around him {FAMILY}, the "
                "women seen from the side with their hands pressed to their chests and their faces lowered in sorrow, "
                "the children crying into their sleeves; the courtyard lamps dim, a dark cloud shadow across the arches",
         camera="medium wide, slightly high angle", amb="stone_house_day", sens="other",
         safe="mourning shown modestly: women fully covered, seen from the side, hands at their chests"),
    dict(to=39, reason="action change: a year of settling his affairs - returning trusts, charity, freeing servants, his will",
         chars=["merchant"], loc="house",
         visual="the merchant standing at the arched gate of his courtyard handing a small cloth purse of coins to a "
                "grateful poor old man in a patched robe; behind him two household servants in plain cream tunics bow "
                "with their hands on their hearts, set free; on a low table beside him a scroll of plain blank parchment "
                "with a quill and an inkpot, a small sealed wooden chest",
         camera="medium wide, eye level", amb="stone_house_day"),
    dict(to=40, reason="time jump: the promised day dawns; he has bathed and takes up his shroud", chars=["merchant"],
         loc="house", transition="black",
         visual=f"at dawn in a quiet room of his house, {MERCHANT_RETURN}, standing by an arched window in the first "
                "pale light, holding the folded white cloth against his chest with both hands, eyes closed, calm and "
                "resolved; a brass water ewer and basin on a low stool beside him",
         camera="medium shot, eye level, window light from the side", amb="stone_house_dawn", sens="other",
         safe="the burial shroud is only a neatly folded white cloth; bathing implied by the ewer and basin"),
    dict(to=42, reason="action change: the heartbreaking farewell at the door", chars=["merchant"], loc="house",
         visual=f"at the open arched door of the house in early morning light, {MERCHANT_RETURN}, "
                "tears in his eyes, gently stepping away while his small boy and little girl cling to the hem of his "
                "robe and the two women of the house in long gowns and headscarves fully covering hair and neck stand "
                "weeping in the doorway; his saddled horse waits outside",
         camera="medium wide from outside the door, eye level", amb="stone_house_dawn"),
    dict(to=45, reason="time jump: after days of travel he sits under the tree praying and waiting",
         chars=["merchant"], loc="tree", transition="black",
         visual=f"{MERCHANT_RETURN}, sitting cross-legged in the deep shade of the huge old tree by the spring, the "
                "folded white cloth on his knees, both palms raised in prayer, lips moving, tears on his cheeks, glancing "
                "fearfully at the empty sky; his horse tethered nearby",
         camera="medium wide, eye level, the tree canopy in the upper half", amb="desert_day", sens="other",
         safe="Quran recitation shown as palms raised in prayer; no book, no script"),
    dict(to=47, reason="character enters: a very old man approaches leading a gazelle",
         chars=["merchant", "old_man_gazelle"], loc="tree",
         visual=f"seen past the seated merchant's shoulder under the tree, the old man with the snow-white beard and "
                f"sage-green robe walking towards him over the dunes with his staff, leading {GAZELLE}; the merchant "
                "looking up in surprise through his tears",
         camera="over-the-shoulder wide shot, the approaching figure in the upper half", amb="desert_day"),
    dict(to=51, reason="action change: the old man stands before him asking; the merchant tells his story",
         chars=["old_man_gazelle", "merchant"], loc="tree",
         visual=f"the white-bearded old man in sage green standing before the seated merchant, leaning on his staff with "
                f"a puzzled concerned face, {GAZELLE} beside him; {MERCHANT_RETURN}, wiping tears with one hand while "
                "explaining; later the old man's eyebrows lift in astonishment",
         camera="medium two-shot, eye level", amb="desert_day"),
    dict(to=55, reason="action change: the old man praises his faithfulness and sits down beside him",
         chars=["old_man_gazelle", "merchant"], loc="tree",
         visual=f"the white-bearded old man now sitting beside the merchant in the shade of the tree, one kindly hand on "
                f"the merchant's shoulder, speaking warm words of admiration; the merchant in his plain white robe with "
                f"the folded white cloth on his knees, comforted; {GAZELLE} lying peacefully at their feet",
         camera="medium shot, eye level", amb="desert_day"),
    dict(to=58, reason="character enters: a second old man approaches with two black dogs",
         chars=["old_man_dogs", "old_man_gazelle", "merchant"], loc="tree",
         visual=f"a sturdy grey-bearded old man in a brown turban and chocolate-brown robe approaching over the dunes "
                f"holding the ends of two long leashes, two big calm black dogs walking at the leashes' length; the "
                "white-bearded old man and the merchant sitting under the tree turning to look at him, the gazelle "
                "resting beside them",
         camera="wide shot, the newcomer in the upper half against the sky", amb="desert_day"),
    dict(to=61, reason="action change: all three sit together under the tree waiting; the wind begins to rise",
         chars=["merchant", "old_man_gazelle", "old_man_dogs"], loc="tree",
         visual=f"the three men sitting side by side in the shade of the great tree, the merchant in his plain white "
                f"robe in the middle, the two old men on either side giving him courage; the gazelle lying in front; "
                f"{DOGS}; the first gusts of wind tugging at robes and leaves, a dark haze rising on the horizon",
         camera="medium wide, eye level", amb="desert_day"),
    dict(to=63, reason="scene change: the violent sandstorm sweeps over them",
         chars=["merchant", "old_man_gazelle", "old_man_dogs"], loc="storm",
         visual="a towering wall of whirling orange sand rising to the sky and rushing towards the lonely tree, the "
                "three small figures of the men huddled together beneath it shielding their faces with their sleeves, "
                "robes whipping in the wind, the animals crouching low",
         camera="extreme wide shot, low angle, the storm filling the upper two-thirds", amb="sandstorm"),
    dict(to=65, reason="character enters: the jinni appears out of the dust and seizes the merchant's hand",
         chars=["merchant_jinni", "merchant", "old_man_gazelle", "old_man_dogs"], loc="storm",
         visual=f"{JINNI}, towering out of the clearing dust with eyes blazing like fire, one gigantic empty hand "
                "gripping the merchant by the wrist and pulling him to his feet, the other huge empty fist raised "
                "high; the merchant in his plain white robe stumbling up in terror; the two old men shrinking back in "
                "fear beneath the tree",
         camera="dramatic low angle, the jinni in the upper two-thirds", amb="sandstorm", sens="violence",
         safe="the narrated raised sword is replaced by an empty raised fist; no weapon anywhere"),
    dict(to=67, reason="emotional turning point: the cliffhanger - the merchant weeping, the jinni's fist raised",
         chars=["merchant", "merchant_jinni", "old_man_gazelle", "old_man_dogs"], loc="storm",
         visual="close on the merchant kneeling in the swirling sand with his eyes shut tight and tears streaming, "
                "hands clasped; behind and far above him the jinni's enormous silhouette with a raised empty fist "
                "against a storm sky lit by ember light; at the edge of the frame the two old men weeping with their "
                "hands over their faces",
         camera="close-up on the merchant, low angle, the jinni silhouette above", amb="sandstorm", sens="violence",
         safe="the downward blow is never shown: cut away on the raised empty fist to the dawn window"),
    # ---------------- FRAME: dawn ----------------
    dict(to=70, reason="story level change: back to the chamber at dawn; Shahrazad falls silent, the king wide-eyed",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn", transition="dissolve",
         visual="the first golden rays of dawn streaming through the carved lattice window across the carpet, a "
                "distant minaret silhouette against the rose-gold sky; Shahrazad on her cushion fallen silent with her "
                "hands resting in her lap; King Shahryar on the divan an arm's length away sitting bolt upright, "
                "wide-eyed and holding his breath; Dunyazad beside her sister with both hands over her mouth",
         camera="medium wide, eye level, the window in the upper half", amb="palace_dawn"),
    dict(to=73, reason="action change: Shahrazad bows her head and promises a more wondrous tale tomorrow",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_dawn",
         visual="close on Shahrazad lowering her head respectfully with a calm knowing smile, dawn light glowing on her "
                "ivory headscarf; behind her, out of focus, King Shahryar leaning forward on the divan with a hungry "
                "curious frown; Dunyazad peeking at the king",
         camera="medium close-up on Shahrazad, eye level", amb="palace_dawn"),
    dict(to=75, reason="action change: the king spares her again and rises to go to his court",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="King Shahryar risen from the divan and striding towards the tall arched doorway of the chamber in the "
                "golden dawn light, his bronze coat swirling, glancing back over his shoulder with a thoughtful "
                "half-smile; Shahrazad and Dunyazad sitting together on the carpet watching him go, relieved, Shahrazad "
                "with a quiet wise smile",
         camera="wide shot, eye level, golden light from the window", amb="palace_dawn"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The Second Night: the merchant's promise and his return. As the darkness of the second night covered the world "
      "and the deep silence of midnight settled over King Shahryar's great palace, everyone was drowned in a deep sea of sleep.")
sh(2, "But in the king's chamber there was no trace of sleep. Shahryar lay impatient, longing to know the end of the "
      "wondrous tale Shahrazad had begun.")
sh(3, "Dunyazad, sitting on the big carpet beside the bed, softly called to her sister as the last part of the night drew near.")
sh(4, "'Dear sister,' Dunyazad whispered, 'if you are not asleep, continue the beautiful story you began yesterday.")
sh(5, "Tell us what happened next to that merchant.' Shahrazad looked towards the king and with great courtesy asked his permission.")
sh(6, "'Will the king grant me permission to continue the story?' 'Tell it,' Shahryar said quickly.")
sh(7, "'Did that terrible jinni cut off his head? Or was he saved?' Smiling, Shahrazad began the story.")
sh(8, "'O noble and mighty king! Where I stopped yesterday, that terrible giant jinni had raised its huge sharp sword, "
      "ready to bring it down on the poor merchant's neck.")
sh(9, "Lying at the brink of death, the merchant shut his eyes. But into his mind came his beloved wives, his little "
      "children and the heavy responsibilities upon his shoulders.", [("heartbeat", "މަރާލިއެވެ", -20)])
sh(10, "Suddenly, weeping, he cried out loudly: 'O mighty jinni! Wait! Do not kill me!",
   [("sob_breath", "ރޮމުން", -20)], hum=True)
sh(11, "Give me a little time!' he begged. The jinni, still holding its sword raised, said in an angry voice:")
sh(12, "'Why should I give you time? You have killed my most beloved son.")
sh(13, "I will accept nothing in exchange but your life.' With tearful eyes the merchant said, 'I accept that.",
   [("sob_breath", "ކަރުނަވީ", -22)])
sh(14, "Your son died by my hand, though without intent. And in exchange for it I stand ready to give my life.")
sh(15, "But O jinni! I am a man entrusted with the goods and money of many people.")
sh(16, "In my hands are other people's trusts. In my home are wives and little children who depend on me.")
sh(17, "If I die here suddenly, their goods will be lost, and my family will be ruined and go hungry.")
sh(18, "So give me just one year's grace. I will go back to my town,")
sh(19, "pay people's debts, return their trusts, divide my wealth among my children, and after bidding my family a last "
       "farewell, I will come right back here,")
sh(20, "to this very tree, before you. Then do with me as you wish.' The jinni sank into deep thought.")
sh(21, "Looking at the merchant with its fiery eyes, it said: 'What is the guarantee that you will come back?")
sh(22, "If you go home and flee, how will I find you?' The merchant raised his hand and spoke with great fear and sincerity.")
sh(23, "'I swear by God who created the heavens and the earth: on the day exactly one year from today, I will come right here.",
   hum=True)
sh(24, "I am a Muslim, and a Muslim's promise is more important than his life.' The jinni accepted his oath. 'Very well.")
sh(25, "I grant you one year's grace. But remember: if you do not come, I will find you and destroy your whole family.'")
sh(26, "Having said this, the giant jinni turned once more into a great cloud of smoke, sank into the ground and vanished.",
   [("smoke_whoosh", "ދުންގަނޑަކަށް", -16), ("magic_shimmer", "ގެއްލިއްޖެއެވެ", -20)])
sh(27, "It felt to the merchant as if his soul had come back into his body. He quickly got up, mounted his horse,",
   [("sigh", "ހީވީ", -20), ("horse_hooves", "ސަވާރުވެގެން", -20)])
sh(28, "and in a state of mixed grief and joy set off towards his town. After a long journey he reached his town, and as "
       "he entered his big house,", [("horse_hooves", "ދަތުރު", -20), ("door_open", "ވަނުމާއެކު", -20)])
sh(29, "his wives and children came joyfully and embraced him. But instead of rejoicing, the merchant began to weep loudly.",
   [("cloth_rustle", "އޮޅުލައިގަތެވެ", -22), ("sob_breath", "ރޮވެން", -20)])
sh(30, "The sound of his sorrowful weeping echoed through the whole house. 'What has happened? What are you grieving "
       "over so?' his wives asked anxiously.", [("gasp", "ހާސްވެފައި", -22)])
sh(31, "The merchant gathered them together and told them, word for word, the terrible thing that had befallen him in the desert.")
sh(32, "And he told them that only one single year of his life remained, and that after it he would go to the brink of death.")
sh(33, "Hearing this, a black cloud of grief covered the whole house. His wives beat their chests and began to weep.",
   [("sob_breath", "ރޯން", -22)], hum=True)
sh(34, "The loud crying of the little children was heard across the whole neighbourhood. What had come to that house was "
       "the grief of death.")
sh(35, "From that day on, the merchant's life changed completely. He began to set his last affairs in order.")
sh(36, "He returned the trusts he held to their owners. He paid off every debt he owed, leaving nothing outstanding.")
sh(37, "Much of the wealth in his hands he gave in charity to the poor and needy. He set his slaves free.")
sh(38, "And dividing fairly the wealth due to his wives and children, he finished writing his last will.",
   [("paper_shuffle", "ލިޔެ", -22)])
sh(39, "So the days went by, and when the last month of the year arrived, the weeping and grief in his house grew. At last,")
sh(40, "the day he had promised the jinni arrived. That morning the merchant bathed and purified himself, and took his "
       "own burial shroud in his hand.", [("pour", "ފެންވަރައި", -22), ("cloth_rustle", "ފޮތިގަނޑު", -22)])
sh(41, "The moment he bade his beloved family the final farewell was so painful it could break even a heart of stone.",
   hum=True)
sh(42, "His children clung to his feet, begging him not to go. But to keep his promise, with eyes full of tears, he left "
       "his house and set off towards that terrible desert.",
   [("sob_breath", "ކަރުނުން", -22), ("door_close", "ނުކުމެގެން", -22)])
sh(43, "After a journey of many days, on that very day and at that very hour, he reached the fearful tree. He got down "
       "from his horse,", [("horse_hooves", "ދަތުރަކަށްފަހު", -20), ("footsteps_sand", "ފައިބައި", -22)])
sh(44, "sat in the shade of the tree, recited the Holy Quran, prayed to God, and began to wait for his death.")
sh(45, "His heart was full of fear. At any moment the giant jinni might come and cut off his head.",
   [("heartbeat", "ބިރުވެރިކަމުން", -20)])
sh(46, "As he sat weeping, suddenly he saw someone coming from afar. It was a very old man.",
   [("footsteps_sand", "އަންނަ", -22)])
sh(47, "In his hand was an exceedingly beautiful gazelle on a chain. The old man came up to the merchant and greeted him: 'O brother!'")
sh(48, "The old man asked in astonishment: 'This is a terrible, desolate place where jinn and devils dwell. Why does a "
       "man like you, dressed in fine clothes,")
sh(49, "sit here alone, so sorrowful, holding your own shroud?' Wiping away his tears, the merchant")
sh(50, "told the old man everything that had passed between him and the jinni, and why he had come here to die.")
sh(51, "Hearing this story, the old man was utterly amazed. 'Glory be to God! This is a most wondrous thing.")
sh(52, "Your truthfulness and your faithfulness to your promise are very great. Only the truthful come to face their "
       "own death so bravely.")
sh(53, "O brother! I will halt my journey for now and stay here with you.")
sh(54, "I want to see what that terrible jinni will do with you. And if it harms you,")
sh(55, "I will do whatever I can for you.' Having said this, the old man who had come with the gazelle sat down beside "
       "the merchant.", [("cloth_rustle", "އިށީނދެއްޖެއެވެ", -24)])
sh(56, "As the two of them sat talking, once again they saw another man coming from afar. He too was a very old man.",
   [("footsteps_sand", "އަންނަތަން", -22)])
sh(57, "But in his hands were two big black dogs. He came, met the two men, and asked why they were sitting in this "
       "terrible place like this.")
sh(58, "The old man with the gazelle told him the merchant's sorrowful story.")
sh(59, "To the second old man too it was a most wondrous story. 'This is a man so truthful it is hard to believe!' said "
       "the second old man.")
sh(60, "'I too will stay here with you. I very much want to see how this story ends.' And so,")
sh(61, "the two old men sat beside the merchant to give him courage. As they sat talking, suddenly a violent storm came "
       "over the whole area.", [("wind_gust", "ތޫފާނެއް", -16)])
sh(62, "The winds grew strong, and a great dust storm began coming towards them. The sand whirled up to the sky.",
   [("sandstorm_gust", "ހިރަފުހުގެ", -14), ("wind_howl", "އެނބުރެމުން", -18)])
sh(63, "Everyone began to tremble with fear. When the smoke cleared, there before them stood the terrible giant jinni.",
   [("gasp", "ތުރުތުރުއަޅަން", -20), ("smoke_whoosh", "ދުންގަނޑު", -16)])
sh(64, "Its two eyes were blazing like fire. The great sword in its hand was raised high. The jinni came, seized the "
       "merchant by the hand and dragged him up.", [("fire_crackle", "އަނދައަނދާ", -22)])
sh(65, "'Stand up!' the jinni roared in a voice like thunder. 'Just as you killed my son, today I will cut off your head!",
   [("thunder", "ގުގުރިއެއް", -16)], hum=True)
sh(66, "Your time has come!' The merchant began to weep loudly. The two old men who had come to help him could do nothing,",
   [("sob_breath", "ރޯން", -20)])
sh(67, "and they too began to weep in fear. The jinni raised its sword to the very top and brought it down hard to "
       "strike the merchant's neck...' At that exact moment,",
   [("heartbeat", "މައްޗަށް", -16), ("gasp", "ތިރިކޮށް", -18)], hum=True)
sh(68, "the first beautiful golden rays of dawn came in through the window of the king's chamber.")
sh(69, "And as the call to the dawn prayer began to be heard, Shahrazad broke off the story and fell silent. King "
       "Shahryar, holding his breath,", [("breath", "ހިފަހައްޓައިގެން", -22)])
sh(70, "lay wide-eyed. 'Then what happened? Did the jinni kill him? What happened to those two old men?'")
sh(71, "Shahrazad respectfully lowered her head. 'O noble king. Dawn has come. My time is over. But,",
   [("cloth_rustle", "ޖަހާލިއެވެ", -24)])
sh(72, "if I am still in this world tomorrow night, and if the king permits, I will tell what happened next. That is a "
       "far more wondrous,")
sh(73, "far more beautiful story.' Eagerness kept rising in Shahryar's heart. He knew he could not bear not knowing "
       "what had happened to the jinni and the merchant.")
sh(74, "So today too the king decided to spare Shahrazad and let her live. And rising, he set off to go to his court.",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -24), ("footsteps_pavement", "ހިންގަވައިގަތެވެ", -22)])
sh(75, "The second night has ended. But Shahrazad's wise plan goes on.", hum=True)
SHOTS = S

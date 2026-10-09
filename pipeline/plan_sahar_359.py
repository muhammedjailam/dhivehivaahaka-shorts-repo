"""Beat/shot plan for Sahar episode 359 (used by plan_beats.py).
Deir Yassin, Palestine, 9 March 1948 -> one month later (evening, then the dawn of the attack, ~9 April 1948).
Wedding of Sahar and Yazan, life in Mahmood's house, the evening on the terrace with Noor, the dawn attack: Mahmood
killed (bible rule 2), Noor assaulted and killed (bible rule 3 - NOTHING of it shown), the escape through the door.
Rules: no embrace between Sahar and Yazan (side by side / hands held only); hijab fully covering hair and neck on every
woman and girl; no soldiers' faces, weapons, flags or insignia; no blood, wounds, bodies, people lying on the ground;
Yazan's blows only as an offscreen soft_thud; no readable text anywhere."""

BRIDE = ("Sahar as a bride: NOT her black everyday outfit but a loose long-sleeved ankle-length cream-white Palestinian "
         "wedding thobe with rich gold-and-red cross-stitch embroidery on the chest panel, sleeves and hem, and a white "
         "hijab fully covering her hair and neck")
GROOM = ("Yazan as the groom in a clean festive version of his outfit: earth-brown collarless shirt, dark trousers and his "
         "black-and-white keffiyeh around his shoulders, curly black hair")
SAHAR = ("Sahar in her everyday loose long-sleeved ankle-length black thobe with deep-red embroidery and black hijab fully "
         "covering her hair and neck")
NOOR = ("Noor in her cream thobe with rose-pink embroidery and rose-pink hijab fully covering her hair and neck")
LAILA = "Laila in her indigo thobe and long white headscarf fully covering her hair, neck and shoulders"
NOPEOPLE_SOLDIERS = "no soldiers, no attackers, no weapons, nobody lying on the floor"

LOC = {
    "wedding": "the wide stone-paved courtyard of a golden limestone house in Deir Yassin decorated for a wedding: plain "
               "white cloth bunting and lanterns, woven rugs, low tables with copper trays of food and clay jugs, olive and "
               "almond trees in blossom, arched windows and flat roofs of the village behind",
    "garden": "the flowering courtyard garden of Mahmood's spacious two-storey golden limestone house in Deir Yassin: "
              "arched windows with green wooden shutters, an outer stone stair to the flat roof, roses, jasmine, lemon and "
              "almond trees, a stone bench, a stone well",
    "hills": "the terraced hills of Deir Yassin west of Jerusalem: olive terraces and pine slopes, the small golden stone "
             "village on its ridge, and far on the horizon the faint silhouette of the old walled city of Al-Quds with "
             "distant domes",
    "terrace": "the flat limestone rooftop terrace of the two-storey house: a low stone parapet, potted red geraniums and a "
               "climbing jasmine, a simple wooden chair, the village rooftops and olive hills beyond",
    "yard": "the courtyard of the house at dusk: a wooden chair under a lemon tree, flowering plants, the outer stone stairs "
            "coming down from the roof, the arched wooden front door of the house with warm lamplight inside",
    "room_dawn": "an upstairs sitting room of the stone house: an arched window with open wooden shutters, a wooden chest "
                 "with its lid open and two old brown leather suitcases on a woven rug, neatly folded clothes, a low "
                 "cushion seat along the wall",
    "kitchen": "the traditional stone kitchen of the house: a clay bread oven, copper pots hanging on the wall, shelves of "
               "clay jars, a low wooden table, a round copper breakfast tray with flatbread, olives, a bowl of olive oil, "
               "white cheese and small tea glasses, a small window and an arched doorway",
    "stairs": "the inner stone staircase of the house leading down to the ground-floor hall, an arched opening, an oil "
              "lamp in a wall niche",
    "sky_window": "an arched stone window of the house looking out at the sky over the hills",
    "hall": "the ground-floor hall of the stone house: a limestone floor, a woven red rug, cushions along the walls, an "
            "arched front door standing open to the courtyard",
    "steps": "the worn limestone steps outside the arched front door of the house, a potted geranium beside them",
    "village_smoke": "the golden stone rooftops and olive trees of Deir Yassin seen from the courtyard of the house",
    "kitchen_door": "the arched doorway of the stone kitchen seen from the dim hall",
    "kitchen_empty": "the traditional stone kitchen seen from its arched doorway: clay oven, shelves of clay jars, copper "
                     "pots on the wall, a low wooden table, a small window",
    "rose_floor": "the bare limestone floor of the stone kitchen close to the ground",
    "gate": "the arched wooden front door of the stone house opening onto a narrow dirt lane between golden limestone "
            "walls in Deir Yassin",
}
MOOD = {
    "wedding": "spring afternoon gold, warm festive sunlight, blossom petals in the air, joyful and celebratory",
    "garden": "spring morning gold, soft warm sunlight through blossoms, peaceful, hopeful, newly-wed contentment",
    "hills": "dusk, heavy dark storm clouds gathering over a still-golden landscape, long shadows, ominous and foreboding",
    "terrace": "spring evening, warm low golden-orange sunset light, playful, tender and loving",
    "yard": "spring dusk turning to blue evening, warm oil-lamp glow from the doorway, gentle family warmth with a hint of "
            "farewell",
    "room_dawn": "dawn blue-gold, soft first light through the window, quiet anticipation of a journey",
    "kitchen": "dawn blue-gold, warm lamplight mixing with the first daylight, homely, the last peaceful morning",
    "stairs": "dawn, cold blue light with pale smoky haze drifting in, sudden shock and fear",
    "sky_window": "dawn, pale blue-gold sky streaked with thin smoke, sacred stillness, faith in the face of death",
    "hall": "smoke-darkened ember dawn, pale orange light through haze from the open door, grief and shock",
    "steps": "smoke-darkened ember dawn, ember-tinged haze, silent grief",
    "village_smoke": "smoke-darkened ember dawn, columns of dark smoke against an orange sky, fear and chaos far off",
    "kitchen_door": "cold dawn light falling on a face from the kitchen window, deep shadows in the hall, horror",
    "kitchen_empty": "pale smoky dawn light from the small window, still air, silence, devastating loss",
    "rose_floor": "a single soft shaft of dawn light on the floor, everything else in shadow, still and mournful",
    "gate": "smoke-darkened ember dawn, orange haze over the lane, urgent flight",
}

BEATS = [
    dict(to=5, reason="episode opening: the wedding of Sahar and Yazan in Deir Yassin, 9 March 1948",
         chars=["sahar", "yazan", "hamza", "mahmood"], loc="wedding",
         visual=f"{BRIDE}, standing side by side with {GROOM}, both smiling shyly, their hands lightly held between "
                f"them; a little behind them on either side the two proud fathers, Hamza in his red-and-white keffiyeh and "
                f"Mahmood in his white keffiyeh, beaming; many wedding guests at a distance in the background - men in "
                f"keffiyehs, women in embroidered thobes with headscarves fully covering their hair, children - blurred",
         camera="medium wide, eye level, the couple in the upper-middle of the frame, the stone paving and a rug forming "
                "a calm lower third", amb="wedding_crowd", sens="intimacy",
         safe="married couple shown only side by side with hands held; guests at a distance"),
    dict(to=9, reason="framing change: the narrator portrays Yazan and Sahar and Yazan's long love for her",
         chars=["sahar", "yazan"], loc="wedding",
         visual=f"a closer two-shot at the wedding: {BRIDE}, eyes lowered with a soft modest smile; {GROOM} beside her "
                f"turning his head to look at her with deep tender devotion; only their hands touch, fingers lightly "
                f"linked; festive lanterns and blossom bokeh behind them",
         camera="medium close-up two-shot, eye level, faces in the upper half", amb="wedding_crowd", sens="intimacy",
         safe="tender glance and held hands only, no embrace"),
    dict(to=13, reason="scene change: after the wedding Sahar lives in Yazan's two-storey house; their plan for Al-Azhar",
         chars=["sahar", "yazan"], loc="garden",
         visual=f"{SAHAR}, sitting side by side with Yazan on a stone bench in the flowering garden of the two-storey house, "
                f"a small stack of old leather-bound books with blank covers between them, Sahar holding one closed book "
                f"against her chest and gazing upward with a hopeful dreamy smile, Yazan looking at her encouragingly; the "
                f"golden two-storey house with arched windows behind them",
         camera="wide-medium shot, eye level, the house and couple in the upper two-thirds, the garden path as a calm "
                "lower third", amb="garden_day"),
    dict(to=16, reason="historical context passage (Zionist movement, the planned state): symbolic landscape",
         loc="hills",
         visual="the peaceful terraced olive hills of Deir Yassin and the small golden stone village on its ridge, while "
                "enormous dark storm clouds roll in from the horizon and swallow the last golden light; a few birds fly "
                "away; no people, no flags, no maps, no symbols",
         camera="very wide landscape, the storm sky in the upper half, the olive terraces as a calm lower third",
         amb="olive_hill_day", sens="other",
         safe="politics shown only as a symbolic gathering storm over the hills; no flags, insignia or maps"),
    dict(to=18, reason="time jump (one month later, evening) and scene change: Yazan asleep on the terrace, the girls tease him",
         chars=["yazan", "sahar", "noor"], loc="terrace", transition="black",
         visual=f"Yazan slumped asleep on a simple wooden chair on the rooftop terrace, head tilted back, mouth slightly "
                f"open, just blinking awake and rubbing his eyes; a few steps away {SAHAR} and {NOOR} stand together "
                f"laughing at him, Noor pointing with a mischievous grin and holding a single red rose",
         camera="medium wide, eye level, sunset sky behind, the stone terrace floor as a calm lower third",
         amb="village_evening"),
    dict(to=21, reason="action change: Sahar sits beside Yazan, they gaze at each other; Noor teases",
         chars=["sahar", "yazan", "noor"], loc="terrace",
         visual=f"{SAHAR} sitting on a low stone ledge beside Yazan's chair, the two smiling into each other's eyes with a "
                f"clear little space between them; {NOOR} standing a step behind with her hands on her hips and an "
                f"exaggerated teasing face, a red rose in one hand",
         camera="medium shot, eye level, faces in the upper half", amb="village_evening", sens="intimacy",
         safe="married couple only exchange a smiling glance, sitting apart; no touch"),
    dict(to=24, reason="action change: Noor tosses the rose at Yazan and runs downstairs laughing",
         chars=["noor", "yazan", "sahar"], loc="terrace",
         visual=f"{NOOR} laughing as she turns to run toward the stone stairs at the edge of the terrace, having just "
                f"tossed a red rose that tumbles through the air toward Yazan; Yazan half rising from his chair with a "
                f"broad grin, reaching out to catch it; {SAHAR} behind him laughing with a hand over her mouth",
         camera="medium wide, slightly low angle, the sunset sky behind, the terrace floor as a calm lower third",
         amb="village_evening"),
    dict(to=27, reason="scene change: downstairs in the yard, Mahmood asks if they are ready to leave",
         chars=["mahmood", "yazan", "sahar", "noor"], loc="yard",
         visual=f"Mahmood rising from a wooden chair under the lemon tree with a warm fatherly smile, one hand raised; "
                f"Yazan standing in front of him grinning, Noor beside Yazan, and {SAHAR} just coming down the last outer "
                f"stone steps behind them; lamplight glowing in the open arched doorway",
         camera="medium wide, eye level, the stone yard floor as a calm lower third", amb="village_evening"),
    dict(to=31, reason="action change: Noor is sad they are leaving, Sahar comforts her, then they go inside",
         chars=["sahar", "noor", "yazan"], loc="yard",
         visual=f"{SAHAR} holding both of Noor's hands and smiling to comfort her; {NOOR} pouting sadly with downcast "
                f"eyes; Yazan standing just behind his little sister with one hand on Noor's shoulder, smiling at both; "
                f"the open arched front door glowing with lamplight behind them under a deep-blue evening sky",
         camera="medium shot, eye level, faces in the upper half", amb="village_evening"),
    dict(to=32, reason="time jump (the next dawn) and scene change: the couple pack for Egypt",
         chars=["sahar", "yazan"], loc="room_dawn", transition="black",
         visual=f"{SAHAR} kneeling on the rug folding clothes into an open wooden chest, Yazan beside her fastening the "
                f"straps of an old leather suitcase, both calm and quietly happy, the first dawn light through the "
                f"arched window",
         camera="medium wide, eye level, the woven rug as a calm lower third", amb="stone_house_dawn"),
    dict(to=33, reason="scene and character change: Laila and Noor prepare the farewell breakfast in the kitchen",
         chars=["laila", "noor"], loc="kitchen",
         visual=f"{LAILA} at the low table arranging flatbread and olives on a round copper breakfast tray with a gentle "
                f"smile, and {NOOR} beside her pouring tea into small glasses from a copper pot, both chatting happily; "
                f"a copper pot simmering on the clay oven",
         camera="medium shot, eye level, the table top as a calm lower third", amb="stone_house_dawn"),
    dict(to=34, reason="turning point: gunfire and Laila's cry - the couple freeze on the stairs",
         chars=["yazan", "sahar"], loc="stairs",
         visual=f"Yazan and {SAHAR} frozen halfway down the stone staircase, faces turned toward the hall below in sudden "
                f"shock and fear, Yazan's arm thrown out protectively in front of her without touching her, pale smoky "
                f"haze drifting up the stairs; nothing of the hall below is visible",
         camera="medium shot from below, looking up the stairs, faces in the upper half", amb="stone_house_dawn",
         sens="violence", safe="gunfire shown only as the couple's shocked faces; the attack itself is not shown"),
    dict(to=36, reason="sensitive moment: Mahmood is shot and tries to say the Shahada (bible rule 2)", loc="sky_window",
         visual="a single man's hand raised from the lower edge of the frame with only the index finger pointing upward, "
                "in dark silhouette against the pale dawn sky seen through an arched stone window, thin smoke drifting "
                "across the sky; no face, no body, no wound",
         camera="close-up, the hand and sky in the upper two-thirds, the dark window sill as a calm lower third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 2: Mahmood is never shown hit or dying; the Shahada is a raised index finger silhouetted against "
              "the dawn sky"),
    dict(to=40, reason="character change: Laila's grief; Yazan and Sahar rush in and she begs them to save Noor",
         chars=["laila", "yazan", "sahar"], loc="hall",
         visual=f"{LAILA} kneeling on the rug seen from behind, head bowed, clutching a white keffiyeh to her chest; beyond "
                f"her in the arched opening at the foot of the stairs Yazan and {SAHAR} stand frozen, faces stricken with "
                f"disbelief; the floor around Laila is bare, {NOPEOPLE_SOLDIERS}",
         camera="medium wide from behind Laila, the couple in the upper half, the rug as a calm lower third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 2: Mahmood's body is never shown - only Laila kneeling from behind holding his white keffiyeh"),
    dict(to=44, reason="emotional turning point: Mahmood breathes his last (bible rule 2)", loc="steps",
         visual="a plain solid-white keffiyeh head cloth (pure white, no checked pattern) with a black agal cord and a "
                "string of amber prayer beads lying fallen on the worn "
                "limestone steps by the front door, touched by ember-tinged dawn light, smoke haze beyond; no people",
         camera="close-up still life, low angle, the objects in the upper-middle, the step as a calm lower third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 2: his death is shown only as his fallen keffiyeh and prayer beads"),
    dict(to=45, reason="scene change: gunfire across the whole village", loc="village_smoke",
         visual="columns of dark smoke rising behind the golden stone rooftops of Deir Yassin against an orange dawn sky, "
                "a flock of birds bursting out of an olive tree in the foreground; no people, no fire on anyone",
         camera="wide shot, the smoke and sky in the upper two-thirds, the courtyard wall as a calm lower third",
         amb="village_burning", sens="violence", safe="rule 1: gunfire = smoke over rooftops and birds bursting from a tree"),
    dict(to=48, reason="character/action change: Yazan runs to the kitchen and sees the horror (bible rule 3)",
         chars=["yazan"], loc="kitchen_door",
         visual="Yazan standing in the arched kitchen doorway gripping the stone frame with one hand, his face lit by "
                "cold dawn light, eyes wide and mouth open in horror and anguish, frozen; the inside of the kitchen is "
                "not visible, only light falling on his face",
         camera="medium close-up, eye level, his face in the upper half, the dark hall floor as a calm lower third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 3: nothing of the assault is shown - only Yazan's horrified face in the doorway"),
    dict(to=51, reason="rule-3 substitution: the empty kitchen, overturned pot and fallen breakfast tray", loc="kitchen_empty",
         visual="the kitchen seen from the doorway, completely empty of people: a copper pot overturned on the stone floor, "
                "the round copper breakfast tray fallen on its side with flatbread and olives scattered and a broken "
                "tea glass, a low stool knocked over, pale smoky dawn light through the small window; no people, no "
                "blood, no weapons",
         camera="wide shot from the doorway, eye level, the scattered tray on the floor in the middle third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 3: the assault and murder of Noor are never shown or implied visually; only the empty kitchen"),
    dict(to=55, reason="rule-3 substitution: Noor's red rose on the stone floor (her loss)", loc="rose_floor",
         visual="a single red rose with a green stem lying alone on the bare limestone floor, a few loose red petals "
                "beside it, in a soft shaft of dawn light; no people",
         camera="close-up at floor level, the rose in the upper-middle, soft dark floor as a calm lower third",
         amb="stone_house_dawn", sens="violence",
         safe="rule 3: Noor's death is shown only as the red rose from the terrace scene lying on the floor"),
    dict(to=58, reason="scene/character change: Sahar and Laila cling together; Yazan bursts out of the kitchen",
         chars=["sahar", "laila", "yazan"], loc="hall",
         visual=f"{SAHAR} and {LAILA} holding each other tightly and weeping, kneeling together on the rug; Yazan rushing "
                f"toward them from the dim arched kitchen doorway, his face wet with tears and desperate, reaching out "
                f"for their hands; {NOPEOPLE_SOLDIERS}",
         camera="medium wide, eye level, faces in the upper half, the rug as a calm lower third",
         amb="stone_house_dawn"),
    dict(to=60, reason="return to Laila's farewell to her husband (same moment as beat_014)", reuse="beat_014",
         loc="hall", chars=["laila", "yazan", "sahar"], visual="(reuse of beat_014)", amb="stone_house_dawn",
         sens="violence", safe="rule 2: Laila's farewell shown only as the earlier image of her kneeling from behind"),
    dict(to=63, reason="action change: Laila longs to see Noor; Yazan pleads with her and she stands up",
         chars=["laila", "yazan", "sahar"], loc="hall",
         visual=f"{LAILA} rising to her feet with tears on her cheeks and a trembling resolute face, Yazan in front of "
                f"her holding both her hands and pleading with tear-filled eyes, {SAHAR} at Laila's side supporting her "
                f"arm; smoke haze in the light from the open doorway",
         camera="medium shot, eye level, faces in the upper half", amb="stone_house_dawn"),
    dict(to=66, reason="scene and action change: the escape through the front door into the lane",
         chars=["yazan", "laila", "sahar"], loc="gate",
         visual=f"Yazan running out through the arched wooden doorway into the dawn lane, pulling his mother {LAILA} by "
                f"one hand and his wife {SAHAR} by the other, all three running toward the camera with frightened "
                f"determined faces, the door swinging shut behind them, orange smoke haze over the rooftops; "
                f"{NOPEOPLE_SOLDIERS}",
         camera="medium wide, eye level, the three in the upper two-thirds, the dirt lane as a calm lower third",
         amb="village_burning", sens="violence",
         safe="Yazan's blow with the stone is offscreen (soft_thud only); only the flight is shown"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The 9th of March 1948 was a day of a very joyful wedding celebration in Deir Yassin, a village of Palestine.")
sh(2, "It was the day Sahar, the eldest daughter of Hamza and Fathimaa, and Yazan, the eldest child of Hamza's close friend Mahmood and Laila, were joined in marriage.")
sh(3, "A large number of the roughly seven hundred and fifty people living in the area attended the wedding celebration.")
sh(4, "Since Hamza and Mahmood were both well-off, everything about the wedding went perfectly.")
sh(5, "Twenty-year-old Yazan and eighteen-year-old Sahar were both delighted and content with the wedding arrangements.")
sh(6, "Yazan was tall, with a handsome build. Ever since his youth he had been capturing girls' hearts.")
sh(7, "In the same way, Sahar was a well-mannered young woman blessed with modest qualities. Sahar's smile was a perfect smile")
sh(8, "that had won the hearts of many boys in the area. Out of the love that grew from the families' closeness, Yazan never even wished to look at any girl other than Sahar.")
sh(9, "Since he was fifteen, Yazan's heart had longed for Sahar. Having married Sahar with the blessing of both families, Yazan was content.")
sh(10, "After the wedding Sahar moved to Yazan's house. It was a spacious two-storey house, its yard filled with flowering plants.")
sh(11, "Yazan was a young man pursuing religious studies while helping in his father's business. Of all Yazan's qualities, the ones Sahar liked most were his bravery")
sh(12, "and generosity. The days passed. Sahar and Yazan had decided to go to Al-Azhar University in Egypt to continue their studies.")
sh(13, "Becoming a doctor and helping the people of Palestine was Sahar's great hope.")
sh(14, "Those were the days when work was under way on Palestinian land to establish a terrorist state called Israel.")
sh(15, "The effort to establish that state in the Middle East, through the Zionist Movement that began in the 1800s,")
sh(16, "was carried out through deceit and wicked, cunning schemes. Sahar and Yazan, who had no idea of such evil plots, completed one month of marriage.")
sh(17, "Sahar was the queen of Yazan's heart, the light of his life. Yazan, asleep on a chair on the terrace, woke to the sound of Sahar and Noor laughing.")
sh(18, "\"Wow... you startled me...\" Yazan said, rubbing his eyes. \"Big brother falls asleep wherever he lands, doesn't he?\" Noor said, bursting into laughter.")
sh(19, "Sahar, still giggling, came and sat beside Yazan. \"Yazan... Dad is looking for you... When I came up to see where you were,",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(20, "you were asleep with your mouth open, so I laughed,\" Sahar said with a smile. \"Smile once more - how lovely...\"")
sh(21, "Yazan said, gazing into Sahar's eyes. \"Excuse me... I'm here too, you know... you two are flirting...\"")
sh(22, "Noor said in a teasing tone, tossing the rose in her hand at Yazan. Then she dashed downstairs as fast as she could.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)])
sh(23, "Yazan and Noor had a very loving bond. From the day Sahar joined the family, Noor had also been very close to Sahar.")
sh(24, "Because of that bond, Sahar missed her little brother Ameen less. When Yazan and Noor came running downstairs,",
   [("footsteps_pavement", "ދުވަމުން", -22)])
sh(25, "Mahmood was sitting on a chair in the yard. Sahar came down after them. \"So, children, are you ready to leave?\"")
sh(26, "Mahmood asked, getting up from the chair. \"Yes, Dad... say the word and we're ready to climb onto the truck right now...\" Yazan said with a laugh.",
   [("cloth_rustle", "ތެދުވަމުން", -24)])
sh(27, "\"Then go to sleep early... you have to get up very early, don't you... Noor, you too, off to bed...\" Mahmood said, going into the house.",
   [("door_open", "ވަންނަމުން", -22)])
sh(28, "\"It will be so boring when big brother and sister are gone,\" Noor said, sulking. \"Don't worry, Noor... we'll come back now and then...")
sh(29, "or Noor can come to us too... but it's a very long journey, you know,\" Sahar said, taking Noor's hand.")
sh(30, "Yazan came up behind them and put his arms around the two of them. \"Come on, let's go to sleep now... we have to get up early and pack a few things...\"",
   [("cloth_rustle", "ބައްދާލިއެވެ", -24)])
sh(31, "Sahar said, looking up at Yazan's face. Then the three of them went into the house together and shut the door.",
   [("door_close", "ލައްޕާލިއެވެ", -18)])
sh(32, "Praising Allah, the two rose early and got their boxes ready for Egypt. Before leaving for Egypt, Sahar and Yazan",
   [("creak", "ފޮށި", -22)])
sh(33, "had planned to have breakfast with both families. Laila and Yazan's little sister Noor were busy in the kitchen preparing the breakfast.",
   [("cup_clatter", "ބަދިގެ", -22)])
sh(34, "The two were startled by a burst of gunfire and the sound of Yazan's mother Laila beginning to cry. When they came down, the scene before them was one they never imagined they would see.",
   [("distant_shots", "ބަޑީގެ", -20), ("sob_breath", "ރޯންފެށި", -24)], hum=True)
sh(35, "Fighters of the Irgun and Lehi terrorist groups had entered the house and shot Yazan's beloved father,", hum=True)
sh(36, "and he lay on the floor soaked in blood. Father was struggling to recite the two testimonies of faith, the Shahada.", hum=True)
sh(37, "Laila, beside herself, held her beloved husband and kept weeping and crying out. Meanwhile Noor's anguished crying could be heard from the kitchen.",
   [("sob_breath", "ރޮއެ", -24)])
sh(38, "Yazan and Sahar stood frozen in shock. What was happening before them was no scene from a film. Nor was it a dream.",
   [("heartbeat", "ހުއްޓުން", -20)])
sh(39, "The two ran over and asked what had happened. \"My son! Save my Noor from those evil men!",
   [("footsteps_pavement", "ދުވެފައިގޮސް", -22)])
sh(40, "I am begging you,\" Laila said, sobbing. The wounded Mahmood was taking quick, deep breaths. It did not last long.",
   [("breath_heavy", "ނޭވާތަކެއް", -24)])
sh(41, "After a farewell look at Laila's face, Mahmood released his last breath from this cruel world.", hum=True)
sh(42, "His heart stopped beating forever. It was as if everything around them went dark. Laila broke into a scream.", hum=True)
sh(43, "Laila struggled to be patient over losing the husband she had hoped to live with all her life, parted from her by the cruelty of others.")
sh(44, "But Yazan and Sahar, who loved their father beyond measure, could not hold back. Crying out \"Father!\" loudly, both of them burst into tears.",
   [("sob_breath", "ރޮއެ", -24)], hum=True)
sh(45, "At that moment gunfire began to ring out across the whole area. Heartbroken, Yazan realised he could not just stand there helpless.",
   [("distant_shots", "ބަޑީގެ", -22)])
sh(46, "He ran into the kitchen to save his beloved little sister. The scene Yazan saw made his whole body shudder.",
   [("footsteps_pavement", "ދުވެފައިގޮސް", -20), ("gasp", "ރޫރޫ", -20)], hum=True)
sh(47, "Three Israeli terrorist fighters had thrown his own full sister to the floor and were forcibly committing an immoral act against her.", hum=True)
sh(48, "And two more men stood at a distance watching. When they saw Yazan, the two began laughing mockingly.", hum=True)
sh(49, "Yazan could not bear to look. Screaming, he struck the three men forcibly assaulting Noor on the head with a heavy kitchen pan lying there, knocked them down, and tried to rescue Noor.",
   [("soft_thud", "ވައްޓާލިއެވެ", -18)], hum=True)
sh(50, "But the two men standing at a distance ran over and seized Yazan. And one of them cut Noor's throat with the dagger in his hand.", hum=True)
sh(51, "Right in front of Yazan, the life of the little sister he saw as a part of his own body was torn from her body. A part of his own body was gone.", hum=True)
sh(52, "His beloved little sister, with whom he had spent so many moments. Yazan's \"lovely, lovely Noor\". Those cruel, evil murderers had \"killed\" Yazan's beloved little sister.", hum=True)
sh(53, "Yazan kept weeping and screaming, and struggling to break free. Just then one of the three who had assaulted Noor began shouting,")
sh(54, "\"You killed that girl far too soon - she was a pretty girl we should have taken away as a captive,\" he kept yelling.")
sh(55, "And the five men began to argue. Seizing the moment, Yazan wrenched himself free from the man holding him and ran.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)])
sh(56, "Meanwhile, not knowing what was happening because of the sounds from the kitchen, Sahar and Laila were holding each other and weeping. \"Mother! Sahar!",
   [("sob_breath", "ރޮނީއެވެ", -24)])
sh(57, "They've killed Noor. They are coming to kill me too,\" Yazan said, running out of the kitchen.",
   [("footsteps_pavement", "ދުވަމުން", -20)])
sh(58, "Laila and Sahar, already helpless, were struck by yet another shock. Yazan ran to them and took Laila's and Sahar's hands.",
   [("gasp", "ޝޮކެކެވެ", -20)])
sh(59, "And before running, Yazan gave his father's blood-soaked body a farewell look.", hum=True)
sh(60, "Laila touched the face of her martyred husband in a farewell caress, and kissed his blood-covered face.", hum=True)
sh(61, "\"A mother cannot leave without seeing Noor. She too is a child I carried and bore,\" Laila said in a trembling voice. \"Mother!",
   [("sob_breath", "ކުރެކިވެފައިވާ", -24)], hum=True)
sh(62, "They won't leave even Noor's lifeless body alone. They are doing every evil thing. What we need now is courage.")
sh(63, "Let's go, Mother,\" Yazan said, weeping. Laila too gathered her courage and stood up. And the three of them ran together.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24), ("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)])
sh(64, "Just then one of the men came out of the kitchen and ran toward the front door. But Yazan, alert and ready,",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(65, "struck the man on the head with a single blow from a stone lying by the doorway. As the man fell to the floor, Yazan slammed the door shut,",
   [("soft_thud", "ޖެހިއެވެ", -18), ("door_slam", "ލައްޕާ", -16)])
sh(66, "and, holding his beloved mother's and his wife's hands, began to run.",
   [("footsteps_sand", "ދުވަންފެށިއެވެ", -20)])
SHOTS = S

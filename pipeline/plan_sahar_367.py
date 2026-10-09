"""Beat/shot plan for Sahar episode 367 (used by plan_beats.py).
Same morning as 359's attack on Deir Yassin, spring 1948. Most violent episode: bible rules 1, 4, 9 applied throughout."""

LOC = {
    "lane": "a dirt lane between golden limestone two-storey houses with arched windows and flat roofs in the Palestinian hill village of Deir Yassin, spring 1948, olive and almond trees in courtyards, house doors standing open and empty, thick columns of dark smoke rising over the rooftops",
    "lane_wall": "the same dirt lane in Deir Yassin beside the rough golden limestone wall of a house, an arched wooden doorway, drifting smoke and ash in the air, dust on the ground",
    "hill_path": "a stony footpath climbing out of the village of Deir Yassin toward a wooded hill, terraced olive groves, low dry-stone walls, pine trees above, smoke drifting from the village below",
    "parents_house": "a golden limestone two-storey house with arched windows and a small courtyard garden at the edge of the village where the wooded hill begins, pine and olive trees behind it",
    "hill_trees": "the slope of a thickly wooded pine and olive hill above Deir Yassin, rocks and dry grass among the trunks, the village of golden stone houses far below in the valley",
    "hill_climb": "a steep rocky slope near the top of the wooded hill above Deir Yassin, pine trees, boulders, dry spring grass",
    "cave_mouth": "the inside of a natural limestone cave on the wooded hill, rough rock walls in deep shadow, the bright irregular cave mouth among rocks and pine branches",
    "truck_road": "a dusty country road through terraced hills toward Jerusalem, spring 1948, the old stone city with distant domes on the far horizon, smoke rising from the hills behind",
    "old_city": "a narrow lane of old Jerusalem, worn honey-coloured stone walls, arches and small balconies, stone paving, distant domes far beyond the rooftops, 1948, no signs",
    "truck_close": "the wooden cargo bed of an old 1940s army truck with plank sides, moving along a dusty road",
    "camp": "a temporary camp of dark canvas tents on a bare hillside, a small fire far off, 1948, no flags, no vehicles with markings",
}
MOOD = {
    "lane": "smoke-darkened ember day, morning sun turned dull orange by smoke, ash in the air, panic and dread",
    "lane_wall": "smoke-darkened ember day, dim orange light through drifting smoke, shock and heartbreak",
    "hill_path": "smoke-darkened ember day, hazy amber sunlight, grief and silent horror",
    "parents_house": "smoke-darkened ember day, fierce orange firelight against dark smoke, sudden shock",
    "hill_trees": "smoke-darkened ember day, late-morning amber light filtering through pine branches, deep grief and tender comfort",
    "hill_climb": "late morning close to noon, hazy smoky amber sunlight, exhaustion and determination",
    "cave_mouth": "near noon, harsh bright daylight at the cave mouth against deep cool shadow inside, astonishment and suspense",
    "truck_road": "smoke-darkened ember day, dusty amber haze, loneliness and dread",
    "old_city": "smoke-darkened ember day, dull amber light falling into the narrow lane, a heavy fearful silence",
    "truck_close": "smoke-darkened ember day, harsh dusty light and deep shadow, endurance and prayer",
    "camp": "smoke-darkened ember dusk turning to night, deep charcoal-blue sky, a small distant orange fire, exhaustion",
}

BEATS = [
    # ---------------- the flight through the burning village ----------------
    dict(to=3, reason="episode opening: Sahar, Yazan and Laila flee through the burning village", chars=["sahar", "yazan", "laila"], loc="lane",
         visual="seen from behind, Sahar, Yazan and Laila hurrying down the dirt lane away from the camera between golden stone houses, Yazan in the middle holding his mother's hand, Sahar close at his side glancing back over her shoulder with a frightened face; empty open doorways, an abandoned bundle on a doorstep, thick columns of dark smoke and an ember sky over the rooftops; no other people, nobody in the smoke",
         camera="wide shot from behind at eye level, the smoky sky and rooftops in the upper half, the empty dirt lane as a calm lower third",
         amb="village_burning", sens="violence",
         safe="the hanged families and bodies the narration describes are never shown: only empty doorways, an abandoned bundle and smoke over the rooftops (rule 1)"),
    dict(to=6, reason="action change: the gunshot that drops Yazan and the soldier's attack on the women (symbolic)", loc="lane",
         visual="a flock of small birds bursting up out of an old olive tree beside the lane into the smoky ember sky, dark smoke drifting between the stone houses, a dropped clay water jar lying broken on the dirt lane; no people",
         camera="medium wide, low angle up into the olive tree, the dusty lane with the broken jar as the lower third",
         amb="village_burning", sens="violence",
         safe="Yazan being shot and the women being choked are not shown: birds bursting from an olive tree and a dropped jar mark the gunfire (rules 1, 4)"),
    dict(to=9, reason="character focus change: Sahar and Laila against the wall as Yazan is seized", chars=["sahar", "laila"], loc="lane_wall",
         visual="Sahar and Laila pressed back against the rough stone wall of a house, both breathless and terrified, Sahar leaning forward with one hand reaching out toward something off-frame, crying out with tears on her cheeks, Laila beside her with a hand at her own chest, staring in horror; far behind them in the smoke only blurred faceless dark silhouettes; nobody touches them",
         camera="medium shot, eye level, the two women in the upper two-thirds, the dusty ground as the lower third",
         amb="village_burning", sens="violence",
         safe="the choking, the beating of Yazan and the soldier are not shown: only the women's horrified faces and distant faceless silhouettes in smoke (rules 1, 4, 9)"),
    dict(to=14, reason="action change: Sahar has collapsed holding her arm; Laila cries out for help", chars=["laila", "sahar"], loc="lane_wall",
         visual="Laila standing in the smoky lane with both hands raised, crying out for help with an anguished face, her white headscarf and indigo thobe lit dull orange; behind her Sahar sits slumped against the stone wall with her eyes closed, holding her left forearm against her body with her right hand, no visible injury; empty doorways and smoke beyond",
         camera="medium wide, eye level, Laila in the upper half, Sahar seated behind her, the dirt lane as a calm lower third",
         amb="village_burning", sens="violence",
         safe="Sahar's arm being broken is not shown, only her sitting dazed against the wall holding her left forearm with no visible injury; the looting and shootings of residents are left to the narration (rule 1)"),
    dict(to=19, reason="character focus change: Yazan's farewell as he is taken to the truck", chars=["yazan"], loc="lane",
         visual="close-up of Yazan looking back over his shoulder through drifting smoke, his face half in shadow, tears in his eyes, lips parted as he calls out his farewell to his mother and wife, keffiyeh around his neck, clothes dusty and creased; the dark shape of an old truck blurred far behind in the smoke; no hands on him, no wounds",
         camera="close-up, slightly low angle, his face in the upper third, smoke and the blurred lane as a calm lower third",
         amb="village_burning", sens="violence",
         safe="Yazan being dragged by the hair along the ground is not shown: only his tearful face looking back (rule 4)"),
    dict(to=23, reason="action change: the truck drives away with Yazan; Laila left kneeling in the lane", chars=["laila"], loc="lane",
         visual="seen from behind, Laila kneeling alone in the dusty lane with her head bowed, her long white headscarf and indigo thobe, watching an old 1940s army truck with a wooden cargo bed drive away from her down the lane into thick smoke; empty stone houses on both sides",
         camera="wide shot from behind Laila, low angle, the truck small in the smoke in the upper half, the dusty lane as the lower third",
         amb="village_burning", sens="violence",
         safe="Laila being dragged, spat on and thrown down is not shown: only her kneeling with head bowed as the truck leaves (rules 1, 4)"),
    dict(to=26, reason="action change: Sahar wakes and searches for Yazan", chars=["sahar", "laila"], loc="lane_wall",
         visual="Sahar sitting against the stone wall, just come to, her eyes wide and searching the lane, holding her left forearm against her body with her right hand, no visible injury; Laila kneeling close beside her, dazed; far behind in the smoke blurred villagers running away, seen from behind",
         camera="medium shot, eye level, Sahar's face in the upper third, the dusty ground as the lower third",
         amb="village_burning", sens="violence",
         safe="people being thrown down and beaten are not shown; only distant blurred villagers fleeing (rule 1)"),
    dict(to=28, reason="emotional turning point: the two women break down and Laila hugs Sahar", chars=["laila", "sahar"], loc="lane_wall",
         visual="Laila holding Sahar in a tight comforting hug as they sit against the stone wall, both weeping, Laila's eyes shut, Sahar's face pressed to her mother-in-law's shoulder, Sahar's left forearm held close to her body; smoke drifting behind",
         camera="medium close-up, eye level, faces in the upper half, the dusty ground as the lower third",
         amb="village_burning"),
    # ---------------- Safiyya and Sama ----------------
    dict(to=31, reason="characters enter: Safiyya and her daughter Sama come running", chars=["safiyya", "sama"], loc="lane",
         visual="Safiyya hurrying up the smoky lane toward the camera with one hand pressed to her forehead under her black headscarf, her face worried, her young daughter Sama clinging to her other hand and her skirt with a quiet frightened face; empty stone houses and smoke behind them; no blood",
         camera="medium wide, eye level, the two figures in the upper two-thirds, the dirt lane as the lower third",
         amb="village_burning", sens="violence",
         safe="Safiyya's bleeding forehead is not shown: only her hand pressed to her forehead under the headscarf; Sama is only a quiet frightened child clinging to her mother"),
    dict(to=35, reason="action change: Laila's despair and Safiyya's words of faith", chars=["laila", "safiyya"], loc="lane_wall",
         visual="Laila and Safiyya kneeling face to face beside the stone wall, Laila weeping with her head bowed, Safiyya holding both of Laila's hands in hers and speaking softly with tears in her eyes, one hand later at her own forehead under her black headscarf; smoke drifting behind",
         camera="medium two-shot, eye level, faces in the upper half, the dusty ground as the lower third",
         amb="village_burning"),
    dict(to=38, reason="action change: Safiyya helps Laila up; the four women gather their resolve", chars=["safiyya", "laila", "sahar", "sama"], loc="lane_wall",
         visual="Safiyya wiping her own tears with one hand while helping Laila to her feet with the other; Laila looking up with a calmer, resolved face; Sahar sitting against the wall holding her left forearm against her body; Sama standing close at her mother's side clinging to her, a quiet frightened face",
         camera="medium wide, eye level, the four women in the upper two-thirds, the dusty ground as the lower third",
         amb="village_burning"),
    dict(to=41, reason="action change: Laila bandages Sahar's arm and Safiyya's head", chars=["laila", "sahar", "safiyya"], loc="lane_wall",
         visual="Laila tying a plain strip of cloth into a sling around Sahar's left forearm as they sit by the stone wall, Sahar wincing quietly; Safiyya sitting beside them with a clean pale cloth strip now tied around her forehead over her black headscarf; all headscarves fully covering hair and neck; no wounds, no blood",
         camera="medium close-up on the women and their hands, eye level, faces in the upper half",
         amb="village_burning", sens="violence",
         safe="the broken arm and head wound are not shown: only a clean cloth sling and a clean cloth strip"),
    # ---------------- to the hill ----------------
    dict(to=43, reason="scene change: the four women set off up toward the wooded hill", chars=["sahar", "laila", "safiyya"], loc="hill_path",
         visual="seen from behind, three women walking calmly side by side up a stony footpath toward the pine-covered hill on a hazy spring morning: on the left Sahar in her black hijab and black thobe with her left forearm resting in a pale cloth sling; in the middle Laila in her white headscarf and indigo thobe, glancing back over her shoulder; on the right Safiyya in black with a pale cloth band tied around her forehead over her headscarf; terraced olive groves and light haze over the village in the valley below",
         camera="wide shot from behind and below, the hill and pines in the upper half, the stony path as the lower third",
         amb="hillside_smoke"),
    dict(to=46, reason="action change: what they pass on the way (symbolic objects)", loc="hill_path",
         visual="an abandoned scene on the stony path: a single lost child's sandal and a fallen woven basket of round bread spilled on the dust beside a dry-stone wall, an empty open doorway of a stone house beyond, smoke drifting across; no people",
         camera="low close-up of the objects on the path, the doorway and smoke in the upper half",
         amb="hillside_smoke", sens="violence",
         safe="the murdered family and the burned elderly people are never shown: only a lost sandal, a fallen bread basket and an empty doorway (rule 1)"),
    dict(to=48, reason="scene change: Sahar's parents' house goes up in flames", chars=["sahar", "laila", "safiyya"], loc="parents_house",
         visual="the golden stone house of Sahar's parents with orange flames bursting from its arched windows and thick dark smoke rising, nobody inside visible; in the foreground the women seen from behind turning to run toward the wooded hill, Sahar's left forearm in a cloth sling; far off only blurred faceless dark silhouettes in the smoke",
         camera="wide shot, the burning house in the upper half, the women small in the foreground, the dusty ground as the lower third",
         amb="village_burning", sens="violence",
         safe="fire on the empty house only, never on people; soldiers only as distant faceless silhouettes (rules 1, 9)"),
    dict(to=50, reason="character focus and place change: from the trees Sahar watches her childhood home burn", chars=["sahar"], loc="hill_trees",
         visual="Sahar standing among pine trunks on the hillside, seen in profile from the side, her left forearm in a plain cloth sling, tears running down her cheeks as she looks down at a column of dark smoke rising from a single house far below in the valley",
         camera="medium shot from the side, her face in the upper third, the slope and dry grass as the lower third",
         amb="hillside_smoke"),
    dict(to=55, reason="action change: Sahar breaks down in Laila's arms and Safiyya comforts her", chars=["sahar", "laila", "safiyya"], loc="hill_trees",
         visual="under the pine trees on the hillside, Sahar sitting on the ground beside Laila, her head resting on Laila's shoulder, eyes closed with tears on her cheeks, Laila's arm around her, Sahar's left forearm resting in a pale cloth sling; Safiyya kneeling in front of them with one gentle hand on Sahar's arm, speaking softly with a kind face, a pale cloth band tied around her forehead over her black headscarf; the village of stone houses far below in the valley",
         camera="medium wide, eye level, faces in the upper half, the needle-covered ground as the lower third",
         amb="hillside_smoke"),
    dict(to=58, reason="action change: Sahar leads them up toward the cave she knew as a child", chars=["sahar", "laila", "safiyya", "sama"], loc="hill_climb",
         visual="Sahar in front pointing up the steep rocky slope with her right hand, her left forearm in a cloth sling, a determined face; behind her Laila, Safiyya with a clean cloth strip around her forehead, and Sama holding her mother's hand climb between boulders and pine trees, tired; faint smoke rising from the valley far below",
         camera="medium wide from slightly above and behind, faces in the upper two-thirds, the rocks as the lower third",
         amb="hillside_smoke"),
    dict(to=59, reason="emotional turning point: the cliffhanger at the cave mouth", chars=["sahar", "laila", "safiyya", "sama"], loc="cave_mouth",
         visual="seen from deep inside the dark cave looking out, Sahar, Laila and Safiyya with young Sama clinging to her mother, standing at the bright cave mouth among rocks and pine branches, silhouetted against the daylight, their faces caught in astonishment, eyes wide, Sahar's hand over her mouth, her left forearm in a sling; whoever is inside the cave is not shown, only dark rock in the foreground",
         camera="from inside the cave, the bright mouth in the upper half, dark rock floor as the lower third",
         amb="cave"),
    # ---------------- Yazan ----------------
    dict(to=62, reason="storyline cut: Yazan in the truck on the road to Al-Quds", chars=["yazan"], loc="truck_road",
         visual="seen from behind, Yazan sitting in the wooden cargo bed of an old 1940s army truck with his head bowed, keffiyeh around his neck, his clothes dusty and creased, the truck driving down a dusty road toward the distant old city of Jerusalem with domes on the horizon; no other faces, no wounds",
         camera="wide shot from behind the truck, the road and distant city in the upper half, the dusty road as the lower third",
         amb="truck_back", transition="black", sens="violence",
         safe="his bleeding leg wound is not shown: only Yazan from behind with his head bowed (rule 4)"),
    dict(to=65, reason="scene change: the truck paraded through a lane of old Jerusalem", loc="old_city",
         visual="a narrow old stone lane of Jerusalem, a silent crowd of men in keffiyehs and women in headscarves seen from behind, standing still and looking toward an old army truck passing slowly at the far end of the lane; the truck seen only from behind, small and dark; nobody on it visible clearly",
         camera="wide shot from behind the crowd, the lane and truck in the upper half, the stone paving as the lower third",
         amb="old_city_crowd", sens="violence",
         safe="the nailing to the iron pole and the public display are never shown: only a silent crowd from behind watching a passing truck (rule 4)"),
    dict(to=68, reason="character focus change: Yazan enduring, praying silently", chars=["yazan"], loc="truck_close",
         visual="close-up of Yazan's face half in deep shadow, his eyes closed, his lips moving in silent dua, curly black hair dusty, keffiyeh around his neck; harsh light on one side of his face; no wounds, no blood, no restraints",
         camera="close-up, his face in the upper half, dark wooden planks as the lower third",
         amb="truck_back", sens="violence",
         safe="the torture, pain and water splashed on his face are not shown: only his face in shadow in prayer (rule 4)"),
    dict(to=70, reason="scene and time change: the truck reaches the soldiers' camp at dusk", loc="camp",
         visual="a dark camp of canvas tents on a bare hillside at dusk, a small orange fire far off, the dark shape of an old truck stopped among the tents, only tiny faceless dark silhouettes in the distance; no flags, no weapons, no insignia",
         camera="wide establishing shot, the tents and dusk sky in the upper two-thirds, bare dark ground as the lower third",
         amb="army_camp_night", transition="black", sens="violence",
         safe="soldiers only as tiny faceless silhouettes; no weapons or insignia (rule 9)"),
    dict(to=73, reason="action change: Yazan's hands bound in cloth; he faints", chars=["yazan"], loc="camp",
         visual="close-up of Yazan's two hands resting palms-up on his knees, loosely wrapped in clean white cloth around the palms and wrists, the edge of his dusty keffiyeh and creased trousers visible, his head bowed in shadow above; faint orange firelight from far off; no blood, no wounds",
         camera="close-up on the hands from slightly above, the hands in the middle of the frame, dark ground as the lower third",
         amb="army_camp_night", sens="violence",
         safe="the nail wounds and the burning rags are not shown: only his hands palms-up in clean white cloth (rule 4)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Fear was creeping into Sahar's heart. She did not know what had become of her mother, father and younger sibling. Where could she even go to look for them?")
sh(2, "From every house came the sound of weeping and wailing. Outside some houses whole families had been lined up and their bodies left hanging.",
   [("crowd_panic", "ރުއިމާ", -24)])
sh(3, "Many houses had been set on fire and were burning to ash. With what tongue could that terror ever be described?",
   [("fire_crackle", "އަލިފާން", -22)])
sh(4, "When they reached a certain point of the road, a shot from far away struck Yazan in the leg, and Yazan fell.",
   [("distant_shots", "ވަޒަނެއް", -22), ("soft_thud", "ވެއްޓުނެވެ", -20)])
sh(5, "While they were trying to lift Yazan up from where he had fallen, a soldier who came from behind seized Sahar and Laila by the throat",
   [("gasp", "ކަރުގައި", -20)])
sh(6, "and pinned them against the wall of a house nearby. When the two women's breath failed and it seemed they were about to die, the soldier let Sahar and Laila go.",
   [("breath_heavy", "ނޭވާ", -20)])
sh(7, "Both of them were doubled over. As they struggled to catch their breath, another of the soldiers came from a distance shouting, \"Arrest the man who attacked us!\"",
   [("breath_heavy", "ނޭވާ", -22)])
sh(8, "He grabbed Yazan by the hair, hauled him upright, struck him in the face and split his mouth. Sahar could not bear to watch.",
   [("soft_thud", "ޖަހައި", -22)])
sh(9, "Crying and screaming \"Let my husband go!\", Sahar grabbed the attacker's arm and began to pull at it.",
   [("sob_breath", "ރޮމުން", -22)])
sh(10, "At that he flew into a rage and, shouting, seized Sahar's left arm with great force and broke it. Unable to bear the pain, Sahar doubled over and collapsed.",
   [("gasp", "އަނބުރައިގަނެގެން", -20)], hum=True)
sh(11, "Watching this, Laila felt as if her whole body were on fire. Those oppressors had already martyred her beloved husband and her daughter.",
   hum=True)
sh(12, "They had driven her out of the house she had built to live in. And as if that were not enough, they were now arresting her son Yazan and taking him away. Not knowing what to do,")
sh(13, "Laila began to cry and scream, begging for help. But who would even hear her cries? Those evil soldiers went on showing cruelty of the most extreme degree.",
   [("sob_breath", "ރޮއެ", -22)])
sh(14, "They were looting the houses of the neighbourhood, lining up the people of some houses in a row and shooting them dead, emptying them out.",
   [("distant_shots", "ބަޑިޖަހައި", -24)])
sh(15, "Everyone was running in every direction trying to save themselves. Laila stood holding on to Yazan's arm.",
   [("crowd_panic", "ދުވަނީއެވެ", -24)])
sh(16, "The man holding Yazan by the hair began dragging him along the ground toward their truck.")
sh(17, "Looking with eyes full of pain at the face of his beloved wife lying unconscious, Yazan struggled to break free. \"Sahar... Sahar... be strong...",
   hum=True)
sh(18, "I will come back... Mother! Be strong for my sake... Look after Sahar... Mother! I love you so much, Mother...")
sh(19, "Tell Sahar I love her very much...\" Yazan said, weeping, his eyes fixed on Laila's face.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(20, "When Laila would not let go of Yazan's hand, the soldier behind came, grabbed Laila by the head and dragged her away,",
   [("cloth_rustle", "ދަމާ", -24)])
sh(21, "separated her from Yazan, spat in her face and threw her down on top of the unconscious Sahar.")
sh(22, "Then the two soldiers dragged Yazan along the ground, loaded him onto the truck and drove off.",
   [("truck_start", "ނައްޓާލިއެވެ", -18)])
sh(23, "Laila sat there, dazed, watching until the truck reached the end of the road and disappeared. It was then that Sahar came to.",
   [("engine_rev", "ޓްރަކް", -24)])
sh(24, "As soon as her eyes opened she looked all around her, hoping to see Yazan. People leading their elderly parents, their wives and children,")
sh(25, "running in every direction along the road in a daze, and people being thrown to the ground and beaten - that is what she saw.",
   [("crowd_panic", "ދުވާތަނާއި", -24)])
sh(26, "But there was no trace of Yazan anywhere. \"Mother! Where is Yazan? Where is my husband, Mother?\" Sahar asked in anguish.")
sh(27, "It was as if she could not even feel the pain in her broken arm. \"They went away taking Yazan with them... Mother tried so hard, my child...\"")
sh(28, "Sahar began to cry very hard. Holding Sahar tight, Laila too began to sob.",
   [("sob_breath", "ރޯން", -22)], hum=True)
sh(29, "While the two of them were in that state, Laila's relative Safiyya and her daughter Sama were seen running toward them.",
   [("footsteps_sand", "ދުވަމުން", -22)])
sh(30, "The two came running up and stopped beside Laila and Sahar. Safiyya's forehead was split and bleeding badly. \"Get up, little sister... be strong...")
sh(31, "Let's get away from here...\" Safiyya said to Laila in a trembling voice. \"I can't be strong any more, elder sister... my Mahmood,")
sh(32, "my Noor - they killed them... They have taken Yazan away under arrest, and now here is this child... her arm is broken...")
sh(33, "If they catch us again I don't know what we'll do... Isn't death better than living...\" Laila said, sobbing.",
   [("sob_breath", "ގިސްލާ", -22)], hum=True)
sh(34, "Hearing this news, Safiyya too began to weep. \"Brother-in-law has been killed too... the two of us, mother and daughter, only just escaped... little sister...",
   [("sob_breath", "ރޮވޭ", -24)])
sh(35, "You must be strong for Sahar's sake... Be patient with the decree of Allah the Exalted and make good dua... You two will not be alone...")
sh(36, "Allah has granted us the blessing of finding each other... Get up quickly... let's go and find a safe place.\" Wiping the tears running from her eyes, Safiyya tried to give Laila courage.",
   [("cloth_rustle", "ފޮހެމުން", -24)])
sh(37, "Sama too kept talking to Sahar, comforting her. Laila accepted what Safiyya said.")
sh(38, "Never giving up hope in the mercy of Allah, she resolved to be patient - for Yazan's last wish as well - in the hope of meeting her beloved son again.")
sh(39, "Laila tore a strip from the lower part of her dress and began to bandage Sahar's broken arm.",
   [("cloth_rustle", "ވީދާލުމަށްފަހު", -20)])
sh(40, "Then she tore a small piece of the hijab on her head, placed it over the split on Safiyya's head and tied it.",
   [("cloth_rustle", "އައްސާލިއެވެ", -22)])
sh(41, "So eager was Safiyya to reach some shelter of safety that she seemed not to feel the pain.")
sh(42, "Together with Laila, Safiyya helped Sahar along. Standing upright, alert and looking behind them, the four set off to climb the hill.",
   [("footsteps_sand", "މިސްރާބުޖެހިއެވެ", -22)])
sh(43, "Sahar's parents' house was also in that area. Since it was surrounded by many trees, all four believed it would be easy to escape that way.")
sh(44, "Along the road they saw scene after heart-rending scene, too painful to describe: a mother and father shot dead together with their little child.",
   hum=True)
sh(45, "Elderly people tied up inside their homes and burned together with the house.")
sh(46, "From fear, and from the pain in her arm, Sahar was trembling violently. In that heart-stopping terror,",
   [("heartbeat", "ތުރުތުރު", -20)])
sh(47, "just as the four women came near Sahar's parents' house, there was a loud blast and the house burst into flames.",
   [("distant_boom", "ގޮވުމަކާއެކު", -20), ("fire_crackle", "އަލިފާން", -22)])
sh(48, "With that they realised soldiers were near the house. Without a moment's hesitation the four of them ran together toward the hill.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(49, "Sahar herself did not know where her strength came from. Even her broken arm seemed not to hurt. Sheltered by the trees on the hill, Sahar looked back toward the house where she had grown up since childhood.",
   [("leaves_rustle", "ގަސްތަކުން", -24)])
sh(50, "Burning to ash were so many memories, so many joys - so many memories of her mother, her father and the beloved younger sibling she had grown up with.",
   [("fire_crackle", "ރޯވެ", -26)], hum=True)
sh(51, "Sahar began to sob. \"If only we had been martyred with them,\" Sahar wept, holding Laila tightly.",
   [("sob_breath", "ގިސްލާ", -22)], hum=True)
sh(52, "Her numbed mind told her that, like Yazan's father and Noor, her mother, her father and her beloved younger sibling had also been martyred.")
sh(53, "Wondering whether her beloved husband would survive in the hands of those merciless oppressors, her poor heart felt as if it would be crushed.")
sh(54, "\"Be strong, little sister! Don't think ill of Allah. Never stop putting your trust in Him. He will not abandon us...")
sh(55, "In sha Allah,\" Safiyya said. Her words brought some measure of calm to Sahar's heart.",
   [("sigh", "ހަމަޖެހުމެއް", -24)])
sh(56, "\"When I was little I used to come with Dad and the others to play in a cave on this hill... I think it would be wise to hide there until it is dark at night...\"")
sh(57, "Sahar said, gathering her courage. Everyone agreed. Even then the sound of gunfire went on without stopping.",
   [("distant_shots", "ބަޑީގެ", -24)])
sh(58, "Sheltering under the trees on the hill, stopping here and there to rest, they reached the cave only when it was close to noon.",
   [("leaves_rustle", "ނިވާވަމުން", -24)])
sh(59, "The four were utterly exhausted, their throats parched. When they climbed up to the mouth of the cave, what they saw was a scene hard even to believe.",
   [("gasp", "ފެނުނީ", -18)], hum=True)
sh(60, "Blood was pouring from where Yazan had been shot in the leg. But those merciless oppressors paid it not the slightest attention.")
sh(61, "The truck was heading toward \"Al-Quds\". The aim of those oppressors was to take Yazan and make an example of him,",
   [("engine_rev", "ދަތުރުކުރަމުން", -22)])
sh(62, "to strike fear into the hearts of the people living in that area. In about ten minutes they entered that area.")
sh(63, "Then, through the loudspeaker they carried, they began to shout: \"Come and see what happens to those who disobey!\"")
sh(64, "Then they seized Yazan by his hands and feet, hauled him upright, took off the cuffs binding his hands behind him, and with four big nails pierced his two hands and two feet",
   hum=True)
sh(65, "and hung Yazan on an iron pole. Unable to bear the pain, Yazan kept screaming. Blood dripped into the truck from where the nails had pierced his hands and feet.",
   hum=True)
sh(66, "From the searing, the pain, Yazan kept on the edge of fainting. Each time, they splashed water on Yazan's face",
   [("water_splash_small", "ފެންޖަހައި", -22)])
sh(67, "and brought him back to his senses. It was as if they would not allow him even the smallest relief from that pain.")
sh(68, "In that state they drove the truck around for about an hour with Yazan on display. But because of the pain racking his body,")
sh(69, "that hour felt to Yazan like many hours. Driving the truck at high speed,",
   [("engine_rev", "ސްޕީޑެއްގައި", -20)])
sh(70, "they stopped in the camp area where those soldiers stayed. Then they took out the nails from Yazan's hands and feet,")
sh(71, "and began to bind with strips of cloth the places where his hands and feet had been pierced and where the bullet had struck his leg.")
sh(72, "Those strips of cloth were soaked in something with a foul smell. And when they began to wrap them around his hands and feet, they burned terribly.")
sh(73, "Unable to bear the pain, Yazan once again slipped into unconsciousness.",
   [("breath", "ހޭނެތޭ", -22)], hum=True)
SHOTS = S

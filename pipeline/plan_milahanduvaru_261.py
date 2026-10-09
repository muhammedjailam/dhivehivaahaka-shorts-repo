"""Beat/shot plan for Milahanduvaru episode 261 — the series finale (used by plan_beats.py)."""

LOC = {
    "room_dusk": "Shamaan's small bedroom in an old coral-stone Maldivian island house at dusk, whitewashed walls, a plain wooden wardrobe, a simple wooden chair, a small window with a wooden frame open onto the sandy yard, a closed plain wooden door",
    "yard_fires": "the sandy yard of an old coral-stone Maldivian island house at night, a big tree, a joali rope seat, woven mats spread on the sand, small fires burning in the corners of the yard, coconut palms and a low coral-stone boundary wall, the house with a lit doorway behind",
    "room_night": "Shamaan's small bedroom in an old coral-stone Maldivian island house at night, whitewashed walls, a plain wooden wardrobe, a woven mat on the floor, a low wooden bench against the wall, a small oil lamp on a shelf, a plain wooden door",
    "sky_smoke": "the night sky above the sandy yard of a Maldivian island house, the tops of coconut palms and a big tree in silhouette, the glow of small yard fires at the very bottom edge",
    "kitchen_morning": "the simple kitchen-dining corner of an old Maldivian island house in the morning, a plain wooden table with a teapot and small cups, wooden chairs, a whitewashed wall, an open window with sunlight and palm fronds outside",
    "yard_dusk": "the sandy yard of an old coral-stone Maldivian island house just after sunset, a joali rope seat under a big tree, coconut palms, a low coral-stone boundary wall, the house doorway glowing with lamplight",
    "yard_moon": "the sandy yard of an old coral-stone Maldivian island house in the early night, a joali rope seat under a big tree, coconut palms, the open house doorway with warm lamplight, a full moon rising above the palms",
    "sitting_night": "the simple sitting room of an old coral-stone Maldivian island house at night, whitewashed walls, a worn cushioned wooden sofa, a woven mat on a tiled floor, a low wooden table, a single warm wall lamp, an open front door onto the dark yard",
    "inner_room": "a small inner room of an old coral-stone Maldivian island house late at night, whitewashed walls, a woven mat and floor cushions, a small oil lamp on a low shelf, a wooden window open to the night with thin white curtains",
    "window_dawn": "a small inner room of an old coral-stone Maldivian island house in the last hour before dawn, a wooden window open to the night with thin white curtains, beyond it coconut palms and the dark sea under a pale setting full moon",
    "moon_sea": "the view through an open old wooden window frame of a Maldivian island house: a big full moon low over a dark calm sea, a shimmering silver moon-path on the water, gentle white surf on a dark beach",
}
MOOD = {
    "room_dusk": "dusk, the last orange-violet light fading through the small window, the room sinking into blue shadow, tense, restless anger",
    "yard_fires": "night, deep indigo sky, warm flickering amber firelight from the small fires and haze of incense smoke, solemn, tense and uneasy",
    "room_night": "night, a single small oil lamp giving warm amber light against deep blue shadows, cold silvery moonlight from the doorway, shock, pleading and fear",
    "sky_smoke": "night, a deep indigo moonlit sky with a few stars, silver moonlight, a single thin pale wisp of smoke curling upward and fading, sorrowful and final",
    "kitchen_morning": "morning, soft warm tropical daylight through the window, quiet, weary, tender",
    "yard_dusk": "just after sunset, a deep blue-violet sky with a faint pink glow on the horizon, the first stars, silvery haze, melancholic and tender",
    "yard_moon": "early night, a full moon rising, cool silver-blue moonlight on the sand, warm amber lamplight spilling from the doorway, tense then softening",
    "sitting_night": "night, warm amber lamplight in the room, the dark yard outside the open door, gentle wonder mixed with fear",
    "inner_room": "late night, warm amber oil-lamp glow, silver moonlight through the thin curtains, intimate, tender and warm",
    "window_dawn": "the last hour before dawn, the room dim, a pale setting moon and a faint first blue glow over the sea, cool silver light, bittersweet and hopeful",
    "moon_sea": "night turning towards dawn, a luminous full moon over a deep indigo sea, silver-blue light, peaceful, bittersweet and hopeful, like a calm ending",
}

BEATS = [
    dict(to=4, reason="episode opening: Shamaan storms into his room at dusk, restless and angry, while his parents prepare the kiyevelli", chars=["shamaan"], loc="room_dusk",
         visual="Shamaan standing in the middle of his dim bedroom with his back half turned to the closed wooden door, jaw clenched, one hand rubbing the back of his neck, frowning with restless anger; through the small open window behind him, two tiny distant figures of an older couple are spreading woven mats in the sandy yard at dusk",
         camera="medium shot, eye level, his face in the upper third, the bare tiled floor as a calm lower third", amb="room_night"),
    dict(to=6, reason="time jump and scene change: after Isha, the night kiyevelli in the yard with fires; Shamaan's parents join, Shamaan stays inside", chars=["hassanfulhu", "sakeena", "shamaan_father"], loc="yard_fires",
         visual="night recitation in the sandy yard: Hassanfulhu in white sits cross-legged at the head of two rows of men dressed in white, all with open upturned palms or closed books on their laps, reciting; small fires burn in the corners of the yard and incense smoke drifts; Shamaan's father sits at the end of a row and Sakeena stands near the house doorway watching; one small window of the house stays shut and dark",
         camera="wide shot, slightly high angle, the rows of men and fires in the upper two-thirds, smooth sand as a calm lower third", amb="island_house_night",
         transition="black", sens="other",
         safe="kiyevelli shown respectfully: men in rows with open palms or closed books, no readable or Arabic script, no amulets"),
    dict(to=12, reason="scene and character change: Sakeena opens Shamaan's door and finds Zumra sitting with him; Zumra pleads and reveals the truth", chars=["zumra", "shamaan", "sakeena"], loc="room_night",
         visual="seen from inside the lamp-lit bedroom: Sakeena standing frozen in the open doorway, one hand on the door edge, eyes wide with shock and anger; in the foreground Zumra and Shamaan sit side by side on a low wooden bench, Zumra turned towards Sakeena with tear-filled silvery eyes and hands pressed together, pleading; Shamaan sits stiffly beside her looking up at his mother",
         camera="medium wide, eye level, three faces in the upper half, the woven floor mat as a calm lower third", amb="room_night", sens="other",
         safe="the threats ('tonight I'll destroy you') shown only as a tense standoff at arm's length; Zumra as a normal, beautiful, fully modest woman, no supernatural horror"),
    dict(to=14, reason="action change: Zumra says she carries Shamaan's child; Sakeena pulls Shamaan by the arm while Zumra clings to him", chars=["zumra", "shamaan", "sakeena"], loc="room_night",
         visual="the three now standing in the lamp-lit bedroom: Sakeena on the left gripping her son Shamaan's wrist and leaning towards the door with a fierce determined face; Shamaan torn between them, anguished; Zumra on the right standing close at his side, both her hands holding his forearm, her face pleading with tears and a faint silvery sparkle in her eyes",
         camera="medium shot, eye level, faces in the upper half", amb="room_night", sens="intimacy",
         safe="'Zumra hugged Shamaan tightly' shown as the married couple standing close side by side with her hands on his forearm; no embrace"),
    dict(to=16, reason="action change: Hassanfulhu runs in at Sakeena's cry and finds Shamaan collapsed on the floor; the men carry him out", chars=["shamaan", "hassanfulhu", "sakeena"], loc="room_night",
         visual="Shamaan lying unconscious on the woven mat of the bedroom floor, fully clothed, eyes closed, face calm and pale, no marks; Hassanfulhu in white kneeling beside him with one palm raised, stern and focused; Sakeena in the doorway with both hands over her mouth; Zumra is gone, only a faint silvery haze lingers in the corner",
         camera="medium wide, slightly high angle, Hassanfulhu's and Sakeena's faces in the upper half", amb="room_night", sens="violence",
         safe="'wounds visible on his body' not shown: he lies fully clothed with eyes closed, no marks, no blood"),
    dict(to=20, reason="scene change: Shamaan laid on the joali in the yard; Hassanfulhu recites loudly and questions him while men hold him back", chars=["shamaan", "hassanfulhu"], loc="yard_fires",
         visual="Shamaan lying fully clothed on a joali rope seat in the firelit yard, eyes half open, weak, lifting his head slightly; Hassanfulhu in white stands over him reciting with one open palm raised and a stern face; several young men in white kneel around the joali with their hands resting on Shamaan's shoulders to keep him lying down; small fires and incense smoke behind",
         camera="medium wide, eye level, Hassanfulhu's face in the upper third, sand as a calm lower third", amb="island_house_night", sens="violence",
         safe="'held him down' shown as men kneeling with hands resting on his shoulders; Shamaan unharmed, no struggle"),
    dict(to=21, reason="symbolic detail: 'she is burning to ash' — Zumra's end shown only as a thin wisp of smoke rising into the moonlit sky", loc="sky_smoke",
         visual="a single thin pale wisp of smoke curling upward from behind the dark palm silhouettes into a deep indigo moonlit sky and fading among the stars, the full moon soft and silver to one side, a warm glow of yard fires along the lowest edge; no people",
         camera="low angle looking up, the smoke and moon in the upper two-thirds, dark palm silhouettes as a calm lower third", amb="night_exterior", sens="violence",
         safe="Zumra burning to ash is never shown: only a thin wisp of smoke rising into the moonlit sky (series rule)"),
    dict(to=24, reason="action change: Shamaan gets up from the joali weak; Hassanfulhu steadies him and says it is over", chars=["shamaan", "hassanfulhu"], loc="yard_fires",
         visual="Shamaan standing beside the joali, drained and unsteady, head lowered, eyes distant and unconvinced; Hassanfulhu in white beside him with a firm hand on his shoulder, steadying him and speaking reassuringly; the fires in the yard burning low, the reciters' empty mats behind",
         camera="medium shot, eye level, both faces in the upper third", amb="island_house_night"),
    dict(to=26, reason="time jump: the next morning, Shamaan aching sits for tea and Sakeena strokes his head", chars=["shamaan", "sakeena"], loc="kitchen_morning",
         visual="Shamaan sitting tired and silent at the wooden table with a cup of tea in front of him, eyes lowered, freshly dressed, hair damp; Sakeena standing beside him with a tender relieved smile, gently resting her hand on his head",
         camera="medium shot, eye level, faces in the upper half, the table top as a calm lower third", amb="home_day", transition="black", sens="other",
         safe="his bath is only mentioned; he is shown already dressed at the table"),
    dict(to=29, reason="time jump and new character: after sunset Shamaan lies on the joali and his jinn daughter Nazaaha comes and sits beside him, crying for her mother", chars=["nazaaha", "shamaan"], loc="yard_dusk",
         visual="Shamaan half reclining on the joali rope seat under the big tree just after sunset, propped on one elbow, looking at his small daughter Nazaaha who sits at the edge of the joali beside him, her small face wet with tears and lips pouting in grief and anger; a faint silvery glow around her",
         camera="medium shot, eye level, both faces in the upper half, smooth sand as a calm lower third", amb="island_house_night", transition="black"),
    dict(to=31, reason="character change: Sakeena calls from the doorway and takes Shamaan's arm to pull him inside; Nazaaha cries 'don't take Bappa!'", chars=["sakeena", "shamaan", "nazaaha"], loc="yard_dusk",
         visual="Sakeena at the lit house doorway holding her son Shamaan's wrist and drawing him towards the door, scolding; Shamaan half turned, looking back over his shoulder towards the joali; in the foreground, small Nazaaha seen from behind standing by the joali with one small hand reaching out towards her father",
         camera="medium wide, eye level, from behind Nazaaha, faces of Sakeena and Shamaan in the upper half", amb="island_house_night"),
    dict(to=36, reason="action change and reveal: Sakeena turns, sees the little girl and is frightened and angry; Nazaaha says Zumra was her mother and Shamaan her father", chars=["sakeena", "nazaaha", "shamaan"], loc="yard_moon",
         visual="in the moonlit yard, Sakeena stands startled with one hand at her chest, staring down at small Nazaaha who stands a few steps away with tears on her cheeks, chin raised; Shamaan stands just behind his daughter with a sad, protective face, one hand on her small shoulder",
         camera="medium wide, eye level, faces in the upper half, moonlit sand as a calm lower third", amb="island_house_night", sens="violence",
         safe="Sakeena's angry threat is shown only as her startled, tense face at a distance; empty hands, no weapon"),
    dict(to=38, reason="emotional turning point: mercy enters Sakeena's heart and she gently hugs Nazaaha, feeling an unusual coldness", chars=["sakeena", "nazaaha"], loc="yard_moon",
         visual="Sakeena kneeling on the moonlit sand gently embracing small Nazaaha, her eyes closed, a tender tearful softening on her face; Nazaaha in her arms, surprised, her small face resting on her grandmother's shoulder; a faint cool silvery mist around the girl",
         camera="medium close-up, eye level, both faces in the upper half", amb="island_house_night", sens="other",
         safe="grandmother and granddaughter, a modest gentle embrace, fully clothed"),
    dict(to=40, reason="scene and character change: inside the house, Shamaan's father learns the truth and treats Nazaaha kindly", chars=["shamaan_father", "nazaaha", "sakeena", "shamaan"], loc="sitting_night",
         visual="in the lamp-lit sitting room, Shamaan's father bends down with a gentle wondering smile, holding out his open palm towards small Nazaaha who stands shyly in front of him; Sakeena and Shamaan stand behind her watching with soft faces",
         camera="medium wide, eye level, faces in the upper half, the woven mat as a calm lower third", amb="living_night"),
    dict(to=43, reason="character change: Sakeena introduces Nazaaha to her brother Yameen — his 'imaginary friend'", chars=["nazaaha", "yameen", "sakeena"], loc="sitting_night",
         visual="on the woven mat of the sitting room, small Nazaaha crouches smiling warmly at toddler Yameen, who stands holding his grandmother Sakeena's hand and stares at Nazaaha in wide-eyed wonder; Sakeena smiles in quiet amazement",
         camera="medium shot, low eye level at child height, faces in the upper half", amb="living_night"),
    dict(to=47, reason="action change: Nazaaha suddenly grows afraid and, at the sound of Hassanfulhu coming, hides behind Shamaan", chars=["nazaaha", "shamaan"], loc="sitting_night",
         visual="Shamaan standing in the sitting room facing the open front door, and small Nazaaha hiding behind his legs, peeking out fearfully towards the dark doorway, her big silvery eyes full of fright; Shamaan's face serious and protective",
         camera="medium shot, eye level, faces in the upper half", amb="living_night"),
    dict(to=50, reason="new framing on an emotional peak: Nazaaha trembles gripping Shamaan's shirt; Sakeena lays her hand on her head and comforts her", chars=["nazaaha", "sakeena", "shamaan"], loc="sitting_night",
         visual="in the warm lamp-lit sitting room, small Nazaaha stands pressed close beside her father Shamaan, holding a fold of his light-blue shirt in one small hand, looking up with a worried face; her grandmother Sakeena stands on her other side, bending slightly with a kind reassuring smile and resting one hand softly on top of the girl's headscarf; a calm, protective family moment",
         camera="medium shot, eye level, faces in the upper half, the woven mat as a calm lower third", amb="living_night"),
    dict(to=52, reason="character change: Hassanfulhu enters with a displeased face; Shamaan's father steps up and distracts him", chars=["hassanfulhu", "shamaan_father"], loc="sitting_night",
         visual="Hassanfulhu in white standing just inside the front door of the sitting room, frowning and looking around suspiciously; Shamaan's father steps in front of him with an open welcoming gesture, talking to him and drawing his attention away from the inner doorway",
         camera="medium shot, eye level, both faces in the upper third", amb="living_night"),
    dict(to=57, reason="scene change: in the inner room through the rest of the night Nazaaha tells stories of her mother and the family's hearts fill with tenderness", chars=["nazaaha", "sakeena", "shamaan", "yameen"], loc="inner_room",
         visual="in the small lamp-lit inner room, the family sits together on a woven mat: small Nazaaha in the middle talking with a gentle smile, Sakeena beside her listening with moist tender eyes, Shamaan sitting close with a soft sad smile, toddler Yameen asleep on a floor cushion; moonlight glows through the thin curtains",
         camera="medium wide, eye level, faces in the upper half, the mat as a calm lower third", amb="room_night"),
    dict(to=59, reason="action change: near dawn a cold breeze enters and Nazaaha fades away into the moonlight", chars=["nazaaha"], loc="inner_room",
         visual="small Nazaaha standing by the open window in a shaft of silver moonlight, turned back towards the room with an innocent gentle smile, her figure becoming soft and translucent as she dissolves into glittering silver moonlight and mist, the thin white curtains blowing inward in a cold breeze",
         camera="medium shot, eye level, her face in the upper third, the moonlit floor as a calm lower third", amb="room_night", sens="other",
         safe="her vanishing shown only as a gentle translucent fading into moonlight and mist; no horror"),
    dict(to=61, reason="character change: Shamaan looks out of the window at the fading moon with new hope while Sakeena weeps", chars=["shamaan", "sakeena"], loc="window_dawn",
         visual="Shamaan standing at the open wooden window seen from slightly behind and to the side, looking out at the pale setting moon over the sea, a quiet hopeful look on his face in the silver light; behind him in the dim room Sakeena sits on the mat with her face in her hands, weeping softly",
         camera="medium shot, from behind his shoulder, his profile in the upper third", amb="room_night"),
    dict(to=62, reason="finale: the moonlit window — the moon over the dark sea, echoing the cover; everyone waits for the next moonlit night", loc="moon_sea",
         visual="through an open old wooden window frame with thin white curtains stirring, a big luminous full moon hangs low over a dark calm sea, a shimmering silver moon-path on the water, gentle white surf on a dark beach; no people; peaceful and bittersweet",
         camera="wide view through the window, the moon in the upper third, the dark sea and beach as a calm lower third", amb="beach_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"No! Mother, don't talk like that about Zumra ever again.\" Saying this angrily, Shamaan strode into his room and locked the door.",
   [("door_close", "ތަޅުލިއެވެ", -16)])
sh(2, "His heart was utterly troubled and full of anger. It was the time when sunset was drawing near.")
sh(3, "Shamaan paced back and forth inside the house, restless. His parents were preparing the house and the yard for the kiyevelli set for that night.",
   [("footsteps_pavement", "ހިނގާލަ", -22)])
sh(4, "In Shamaan's heart there was great displeasure and anxiety about it. After coming back from the Isha prayer,")
sh(5, "just as on other nights, Hassanfulhu and his men spread out in the yard, and before long they began to recite.",
   [("cloth_rustle", "އަތުރާލައި", -24)])
sh(6, "That night fires were lit all around the yard. At one point in the kiyevelli Shamaan's mother and father joined in too, but Shamaan kept away and did not come out of the house.",
   [("fire_crackle", "ރޯކޮށްފައެވެ", -18)])
sh(7, "\"Go and bring Shamaan,\" Hassanfulhu told Sakeena. At that Sakeena went into the house, walked quickly and opened the door of Shamaan's room.",
   [("footsteps_pavement", "ހިނގުމެއްގައި", -20), ("door_open", "ހުޅުވާލިއެވެ", -16)])
sh(8, "Sakeena was stunned by what she saw. Zumra was sitting in the room with Shamaan. \"Mother, don't kill me!\" Zumra began to plead, crying.",
   [("gasp", "އަންތަރީސްވިއެވެ", -18), ("sob_breath", "ރޮމުން", -22)], hum=True)
sh(9, "\"What pleading? Tonight I will finish you,\" Sakeena said harshly. \"No, mother, I came to this house for your safety,\" Zumra said.")
sh(10, "\"What could you possibly do?\" Sakeena asked mockingly. \"Mother, listen,")
sh(11, "it was I who saved you from the sorcery someone had done to separate you and father. The effect of that sorcery reached Shamaan too.")
sh(12, "Even his wife died because of it,\" Zumra went on, revealing the truth. \"That's a lie — jinn never tell the truth,\" Sakeena would not believe it.")
sh(13, "\"Mother, please believe me. I am carrying Shamaan's child,\" Zumra pleaded. \"I don't want jinn children.")
sh(14, "Tonight I will wipe even your scent from this earth,\" Sakeena said, and seized Shamaan by the arm and pulled him. \"Tonight you cannot take Shamaan,\" Zumra clung to Shamaan tightly.",
   [("cloth_rustle", "ދަމައިގަތެވެ", -20)], hum=True)
sh(15, "At Sakeena's cry Hassanfulhu came running, and when he entered the room, Shamaan was lying fallen on the floor.",
   [("footsteps_pavement", "ދުވެފައި", -18), ("soft_thud", "ވެއްޓިފައެވެ", -18)])
sh(16, "Some wounds could be seen on his body. The men who came with Hassanfulhu lifted Shamaan, carried him out and laid him on the joali in the yard.",
   [("footsteps_sand", "ނަގައިގެން", -22)])
sh(17, "Hassanfulhu kept on reciting without a pause. \"Where is the jinn Zumra?\" Hassanfulhu asked Shamaan.")
sh(18, "\"Zumra's body has caught fire,\" Shamaan answered with difficulty. \"I will not stop until she turns to ash,\" Hassanfulhu said.",
   [("fire_crackle", "އަލިފާން", -20)])
sh(19, "\"You can never kill Zumra,\" Shamaan said again. \"Is that so? Just watch,\" Hassanfulhu said, and began to recite loudly. Though Shamaan tried to get up,",
   [("breath_heavy", "ތެދުވަން", -22)])
sh(20, "at Hassanfulhu's command the men there held him back. \"Now where is Zumra?\" Hassanfulhu asked once more.")
sh(21, "\"She is burning to ash,\" Shamaan said. A little while later Shamaan got up from the joali. It was as if there was no strength left in his body.",
   [("fire_crackle", "އަނދާ", -18)], hum=True)
sh(22, "Hassanfulhu went and steadied Shamaan. \"Now it is over,\" Hassanfulhu said, encouraging him.")
sh(23, "Shamaan nodded, but he knew it was not over yet. Still, he did not want to talk about it.")
sh(24, "After Hassanfulhu took Shamaan to his room and laid him down, he told Sakeena to look after him and went home. Shamaan fell asleep just as he lay.",
   [("footsteps_sand", "ދިޔައެވެ", -24)])
sh(25, "The next day, when Shamaan woke at Sakeena's call, his whole body ached. He forced himself up, bathed, and came and sat down to drink tea.",
   [("cup_clatter", "ސައިބޯން", -20)])
sh(26, "\"My son, now you are saved from that great calamity,\" Sakeena said lovingly, stroking Shamaan's head. Shamaan nodded without a word, then went and lay down again.")
sh(27, "He woke only after the sun had set. After bathing he came out into the yard, and just as he lay down on the joali,")
sh(28, "his jinn daughter Nazaaha came and sat down beside him. Nazaaha sat sobbing in grief at losing her mother. \"Grandma is such a cruel person, isn't she?\"",
   [("sob_breath", "ރޮއެރޮއެއެވެ", -22)])
sh(29, "Nazaaha was very angry with her grandmother Sakeena. \"No, my child, grandma will love Nazaaha very much,\" Shamaan said, trying to calm his daughter.")
sh(30, "\"Shamaan! Who are you talking to? Didn't I tell you not to stay outside at sunset!\" Shamaan flinched at Sakeena's voice.",
   [("gasp", "ސިއްސައިގެން", -20)])
sh(31, "As Shamaan was about to go inside, Sakeena caught hold of his arm. At that moment: \"Grandma, don't take Bappa away!\"")
sh(32, "Hearing Nazaaha's voice, Sakeena started and looked back. Seeing a small girl standing in front of her, Sakeena was frightened. \"What jinn are you?",
   [("gasp", "ސިހިފައި", -20)])
sh(33, "Why call me grandma? Shall I kill you too!\" Sakeena said angrily. \"Grandma killed my mother so cruelly,\" Nazaaha said, crying.",
   [("sob_breath", "ރޮމުން", -22)])
sh(34, "\"Your mother? Who is that?\" Sakeena asked. \"That's Zumra. Shamaan is my father.\" At Nazaaha's answer Sakeena sank into a sea of astonishment.")
sh(35, "\"Shamaan! You even have a jinn child?\" Sakeena blurted out. \"Yes, this is my child.")
sh(36, "Now if you want, hurt this child too and kill her,\" Shamaan said sorrowfully. \"No — grandma will never hurt Nazaaha. Come, let's go inside.",
   hum=True)
sh(37, "But don't tell anyone you are a jinn child.\" Mercy entered Sakeena's heart, and slowly she took Nazaaha into her arms.",
   [("cloth_rustle", "ބައްދާލިއެވެ", -22)], hum=True)
sh(38, "Though she felt an unusual coldness from that tiny body, the tenderness born in Sakeena's heart was far greater.")
sh(39, "When they went inside, Shamaan's father was there too. When he too learned the truth, he began to treat Nazaaha kindly.")
sh(40, "Beyond the veil between humans and jinn, to this little family Nazaaha was simply a little child.")
sh(41, "Sakeena introduced Nazaaha to her big brother Yameen. On seeing Yameen, a smile spread over Nazaaha's face. \"I already know big brother.")
sh(42, "Some days I play with big brother too,\" Nazaaha said. Yameen stood staring at her in wonder.")
sh(43, "Learning that the 'imaginary friend' he used to play with was her, they felt something words cannot describe. But then,")
sh(44, "suddenly fear began to show on Nazaaha's face. \"I'm scared. I'm so sad about the way my mother died.",
   [("heartbeat", "ބިރުވެރިކަން", -20)])
sh(45, "But every moonlit night I will come to see Bappa,\" Nazaaha said, and just then,")
sh(46, "at the sound of Hassanfulhu coming from outside, she slipped behind Shamaan in fear. What that tiny soul feared was the wickedness of people and the dark side of the world.",
   [("footsteps_sand", "އަންނަ", -20)])
sh(47, "Yet it was certain that within that family's kindness Nazaaha had found safety.")
sh(48, "As the sound of Hassanfulhu's footsteps came closer, Nazaaha's whole body began to tremble.",
   [("footsteps_sand", "ފިޔަވަޅުތަކުގެ", -18), ("heartbeat", "ތުރުތުރުލާން", -22)])
sh(49, "She stood gripping Shamaan's shirt tightly, as if it were her only protection. \"Don't be afraid, my child, grandma is right here.",
   [("cloth_rustle", "ހިފަހައްޓާލައިގެން", -24)])
sh(50, "Hassanfulhu can't hurt Nazaaha,\" Sakeena said in a soft, gentle voice, quickly laying her hand on Nazaaha's head.")
sh(51, "Hassanfulhu came into the house with a displeased face. It was as if he sensed that something had changed.",
   [("door_open", "ވަދެގެން", -18)])
sh(52, "But when Shamaan's father stepped up to Hassanfulhu and began to talk, Hassanfulhu's attention turned elsewhere.")
sh(53, "Seizing that chance, Sakeena took Nazaaha into the inner room. \"Mother always used to say there are good people among humans too.",
   [("door_close", "ވަނެވެ", -22)])
sh(54, "Today I know it is true.\" Through the rest of that night, the stories Nazaaha told filled everyone's hearts with tenderness.")
sh(55, "Even though her mother was a jinn, her love and kindness were no less than any human's, Nazaaha said.")
sh(56, "\"It's time for me to go now. I will come again on a moonlit night. Take care of Bappa,\" Nazaaha begged.")
sh(57, "Sakeena nodded, giving Nazaaha that promise. As dawn drew near, Nazaaha got ready to leave.")
sh(58, "Suddenly a cold breeze came into the room. Standing before them all, Nazaaha vanished as if slowly melting into the moonlight.",
   [("wind_gust", "ރޯޅިއެއް", -18)], hum=True)
sh(59, "All that remained was the memory of the innocent smile on her face. Even though she was a jinn child,", hum=True)
sh(60, "the love for Nazaaha born in that family's hearts would never fade away. Shamaan looked out of the window.")
sh(61, "Though the moon in the sky was slowly fading, a new light of hope spread through his heart. Sakeena wept bitterly.",
   [("sob_breath", "ރޮވުނެވެ", -22)], hum=True)
sh(62, "But there was nothing more to be done. With Nazaaha's promise, they all began to wait once more for a moonlit night. — The End —", hum=True)
SHOTS = S

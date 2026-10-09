"""Beat/shot plan for Nindheveethimeymathee episode 400 (used by plan_beats.py).
SCHOOL timeline. Night at Sana's home: Haizum comes to his sick, estranged wife; the kitchen outburst; Laira and Lail
come home; Lail and Saba's verse slip; late-night grief over the lost child; the cliffhanger.
Bible rules: Sana always in hijab; Haizum + Sana only side by side / hand on shoulder / hands held (no embrace, no kiss,
never both in a bed: sitting apart on a sofa); the smashing shown only as a broken cup on the floor; no blood, no
vomiting: the cliffhanger is Haizum's terrified face at a half-open door."""

HOME = "a spacious modern apartment in Malé, Maldives, Sana's home"
LOC = {
    "living": f"the sitting room of {HOME} late at night: a long cream sofa and a matching armchair, a low wooden coffee table with a glass of water, a wall-mounted TV whose screen faces away from the viewer, sheer curtains over a tall dark window with distant city lights, most lamps switched off",
    "entry": f"the entrance of {HOME} at night: a plain dark-wood front door with a small digital keypad lock and a peephole, a narrow console table, a low shoe rack, tiled floor",
    "kitchen": f"the modern kitchen of {HOME} at night: pale wooden wall cupboards, a white stone counter, a steel sink, a small window with a dark night sky, tiled floor",
    "memory_room": "a dim, half-empty sitting room in a Malé apartment years ago, a sofa, a tall window streaked with rain, a low table",
    "memory_door": "the open front door of a Malé apartment at night years ago, seen from inside, a dim corridor beyond, warm light from the room behind",
    "hallway": f"the inner hallway of {HOME} at night: closed white bedroom doors, framed blurry family photos on the wall, a low shoe rack near the front door, soft tiled floor",
    "lail_room": f"the bedroom of a 17-year-old boy in {HOME} at night: a single cot with a light-blue sheet and plain wooden headboard, two white pillows, a wicker laundry basket, a study desk with a closed laptop and stacked school books, a window with dark night sky",
    "nook": f"a small private sitting room off the master bedroom of {HOME} late at night: a compact two-seat grey sofa by a tall window, a small side table with a glass of water, a floor lamp, sheer curtains",
    "door": f"a short dim inner corridor of {HOME} late at night, a plain white door standing half open with cold white light spilling out of the small tiled room beyond, nothing visible inside",
}
MOOD = {
    "living": "late night, a calm dry night, most lights off, cold blue TV glow and one warm amber side lamp, distant city lights through the sheer curtains, lonely, tense and sorrowful",
    "entry": "late night, calm dry night, dim warm hallway light, the keypad's tiny blue glow, hesitant tension",
    "kitchen": "late night, calm dry night, harsh white under-cabinet light against deep blue shadows, raw anger and pain",
    "memory_room": "soft hazy dreamlike memory glow, grey rainy evening light, heavy loneliness and despair",
    "memory_door": "soft hazy dreamlike memory glow, night, warm light behind and cold shadow ahead, quiet heartbreak",
    "hallway": "late night, calm dry night, a single dim warm wall light, deep blue shadows, hushed and uneasy",
    "lail_room": "late night, calm dry night, soft warm desk-lamp glow and cool moonlight from the window, dreamy, shy first love",
    "nook": "deep night, calm dry night, a single dim warm floor lamp against deep indigo shadows, moonlight through sheer curtains, grief and longing",
    "door": "deep night, calm dry night, cold white light spilling from the half-open door into the dark corridor, sudden fear and shock",
}

SANA_SICK = "Sana pale and feverish with tired red-rimmed eyes, in her loose long-sleeved sage-green dress with a soft cream shawl around her shoulders and her ivory hijab fully covering her hair and neck"
HAIZUM_SUIT = "Haizum in his dark-navy suit and white open-collar shirt"
HAIZUM_LATE = "Haizum with his suit jacket off, in a white long-sleeved shirt and navy trousers"

BEATS = [
    dict(to=3, reason="episode opening: Sana alone and sick in the dim, empty sitting room", chars=["sana"], loc="living",
         visual=f"{SANA_SICK}, sitting alone at one end of the long sofa holding a glass of water in both hands, coughing lightly into her shoulder, eyes heavy with exhaustion; the room dim and empty around her, cold light on one side of her face",
         camera="medium wide, eye level, the coffee table and floor as a calm lower third", amb="living_night"),
    dict(to=5, reason="action and location change: the doorbell rings and she looks through the peephole", chars=["sana"], loc="entry",
         visual=f"{SANA_SICK}, standing close to the front door, leaning in to look through the peephole, one hand on the door, the other pressed to her chest, her face uneasy and hesitant; the small keypad glowing softly blue beside the handle",
         camera="medium shot from the side, her face in the upper third", amb="home_night"),
    dict(to=8, reason="character enters: Haizum at the door", chars=["haizum", "sana"], loc="entry",
         visual=f"the front door half open: {HAIZUM_SUIT} standing on the threshold, gentle and worried, looking at Sana; Sana holding the edge of the door, her face cold and guarded, turning away to let him in; a pair of polished black men's shoes being slipped off on the doormat",
         camera="medium two-shot, eye level, from inside the apartment", amb="home_night"),
    dict(to=10, reason="location change: they sit in the sitting room; he asks if she has seen a doctor", chars=["haizum", "sana"], loc="living",
         visual=f"{HAIZUM_SUIT} sitting forward on the sofa, elbows on his knees, asking with concern; {SANA_SICK}, sitting in the armchair across the coffee table, coughing behind her hand and waving the question away, not meeting his eyes",
         camera="medium wide two-shot across the coffee table, eye level", amb="living_night"),
    dict(to=14, reason="action change: he goes to her and reaches to check her fever; she pushes his hand away; he pleads", chars=["haizum", "sana"], loc="living",
         visual=f"{HAIZUM_SUIT} standing beside Sana's armchair, bending towards her with one hand lifted near her forehead, his face pleading; {SANA_SICK}, turning her face away and pushing his hand aside, eyes downcast",
         camera="medium two-shot, slightly low angle", amb="living_night", sens="intimacy",
         safe="married couple; only a hand near her forehead that she pushes aside — no closer contact"),
    dict(to=18, reason="emotional turning point: tears in her eyes; he holds her hand and she lets him", chars=["sana", "haizum"], loc="living",
         visual=f"{SANA_SICK}, sitting with her head bowed, tears welling in her eyes; {HAIZUM_SUIT} crouching beside the armchair holding her hand gently in both of his, looking up at her with worry; she does not pull her hand away",
         camera="medium close two-shot, eye level, their faces in the upper half", amb="living_night", sens="intimacy",
         safe="married couple: hands held only"),
    dict(to=22, reason="flashback/backstory: the separation and Sana's depression and rage", chars=["sana"], loc="memory_room",
         visual="Sana in her sage-green dress and ivory hijab sitting hunched on the edge of a sofa in a dim room, her face buried in her hands, a toppled vase and scattered flowers on the floor a few steps away, rain on the window behind her",
         camera="medium wide, eye level, the floor as the lower third", amb="memory", transition="dissolve", sens="other",
         safe="depression and risk of self-harm shown only as a woman with her face in her hands and a toppled vase; no harm shown"),
    dict(to=24, reason="backstory continues: Haizum keeps coming and leaving with his head bowed", chars=["haizum", "sana"], loc="memory_door",
         visual=f"{HAIZUM_SUIT} stepping out through an open apartment door into a dim corridor, head bowed, glancing back over his shoulder with sorrow; far behind him in the warm room Sana stands with her back turned, arms folded",
         camera="medium wide from inside the apartment, Haizum in the doorway in the upper half", amb="memory"),
    dict(to=28, reason="return to the present: he pleads for the children; she coughs and he hands her water", chars=["haizum", "sana"], loc="living",
         visual=f"{HAIZUM_SUIT} sitting on the edge of the sofa close to the armchair, holding out a glass of water to Sana; {SANA_SICK}, coughing into her hand, reaching for the glass, her face lifted towards him, hopeless and tired",
         camera="medium two-shot, eye level", amb="living_night", transition="dissolve"),
    dict(to=31, reason="emotional turning point: bitter memories return; both pull back; silence", chars=["sana", "haizum"], loc="living",
         visual=f"{SANA_SICK}, leaning back into the armchair with her eyes squeezed shut and her face turned away in pain; in the soft-focus background {HAIZUM_SUIT} leaning back on the sofa, watching her helplessly; the TV glow flickering cold blue across the room",
         camera="close-up on Sana in the foreground, Haizum soft-focus behind", amb="living_night"),
    dict(to=34, reason="action change: he switches off the TV and stays; she walks to the kitchen; he sits with his face in his hands", chars=["haizum", "sana"], loc="living",
         visual=f"{HAIZUM_SUIT} sitting alone on the sofa, elbows on his knees and his face in his hands, exhausted, the TV remote on the coffee table; in the far background Sana's figure walking away through the kitchen doorway carrying a glass",
         camera="medium wide, eye level, Haizum in the upper half", amb="living_night"),
    dict(to=36, reason="location change: the crashes in the kitchen", chars=["sana"], loc="kitchen",
         visual=f"{SANA_SICK}, standing at the counter with her back half turned, both fists clenched at her sides, shoulders shaking; a cupboard door swung open, a broken white cup in pieces on the tiled floor and a few plastic containers scattered around it",
         camera="medium wide, eye level, the floor with the broken cup in the lower part away from her face", amb="home_night", sens="violence",
         safe="anger shown only as clenched fists and a broken cup on the floor; nothing is thrown, nobody is hurt"),
    dict(to=38, reason="character enters/action: Haizum takes the glass dish from her hand and puts it back", chars=["haizum", "sana"], loc="kitchen",
         visual=f"{HAIZUM_SUIT} standing beside Sana at the open cupboard, one hand gently holding her wrist and the other taking a clear glass bowl from her hand to put it back on the shelf; Sana looking at him with angry, tear-filled eyes",
         camera="medium two-shot, eye level", amb="home_night", sens="violence",
         safe="he stops her calmly by the wrist (married couple); nothing is thrown"),
    dict(to=42, reason="action change: the bitter argument face-off", chars=["haizum", "sana"], loc="kitchen",
         visual=f"a tense face-off across the kitchen at arm's length: {HAIZUM_SUIT} speaking firmly then closing his eyes in shame; {SANA_SICK}, glaring back at him with tears and fury, her fists clenched at her sides",
         camera="medium wide two-shot in profile, eye level", amb="home_night", sens="violence",
         safe="the quarrel shown as a tense face-off at a distance; no hitting, nothing thrown"),
    dict(to=46, reason="emotional turning point: he asks how much more he must apologise; she breaks down crying", chars=["haizum", "sana"], loc="kitchen",
         visual=f"{HAIZUM_SUIT} and {SANA_SICK} standing side by side close together, he holds both her hands in his and looks down at her with remorse; Sana weeping with her head bowed, her shoulders trembling",
         camera="medium close two-shot, eye level", amb="home_night", sens="intimacy",
         safe="the narrated embrace is replaced by the married couple standing side by side holding hands"),
    dict(to=51, reason="reflective passage (> 40 s): detail image of their held hands and wedding rings while the narration recalls his loyalty", chars=["haizum", "sana"], loc="kitchen",
         visual="close-up of a man's hand in a navy suit sleeve with a plain gold wedding band gently holding a woman's hand in a sage-green sleeve with a matching thin gold ring, her fingers trembling, a tear drop falling past them; soft focus kitchen light behind",
         camera="extreme close-up on the hands in the upper half, soft blurred counter below", amb="home_night", sens="intimacy",
         safe="married couple: hands held only"),
    dict(to=55, reason="action change: he steps back and looks at her tear-reddened face; tears in his own eyes", chars=["haizum", "sana"], loc="kitchen",
         visual=f"{HAIZUM_SUIT} standing facing Sana with his hands resting on her shoulders, tears running down his own cheeks, looking into her face with deep sorrow; {SANA_SICK}, eyes red and swollen from crying, looking up at him",
         camera="medium close two-shot, eye level, faces in the upper half", amb="home_night", sens="intimacy",
         safe="the narrated face-holding, wiping of tears and kiss on the head replaced by his hands on her shoulders (married couple)"),
    dict(to=59, reason="action change: she tries to push him away; he says he will not leave and threatens to send the children abroad", chars=["haizum", "sana"], loc="kitchen",
         visual=f"{HAIZUM_SUIT} standing firm and determined a step away from Sana, his jaw set, tears still on his face; {SANA_SICK}, crying in anger, both fists clenched at her sides, glaring at him",
         camera="medium two-shot, slightly low angle", amb="home_night", sens="violence",
         safe="her beating on his chest is never shown: clenched fists at her sides, a tense face-off"),
    dict(to=62, reason="action change: exhausted, she gives up struggling", chars=["sana", "haizum"], loc="kitchen",
         visual=f"{SANA_SICK}, sitting slumped on a kitchen stool, head bowed, utterly exhausted, tears on her cheeks; {HAIZUM_SUIT} standing beside her with one hand resting on her shoulder, his eyes closed",
         camera="medium shot, eye level, the counter as the lower third", amb="home_night", sens="intimacy",
         safe="the narrated tight embrace replaced by his hand on her shoulder (married couple)"),
    dict(to=64, reason="characters change: Laira and Lail come home", chars=["laira", "lail_young"], loc="entry",
         visual="Laira in her dusty-pink dress and dove-grey hijab stepping in through the front door first, looking ahead towards the inner hallway with worry; young Lail in his light-grey t-shirt and dark jeans behind her, closing the door; the house silent and dark",
         camera="medium wide, eye level, from inside the apartment", amb="home_night"),
    dict(to=68, reason="action change: Mum's door is locked; Lail points at Dad's shoes", chars=["laira", "lail_young"], loc="hallway",
         visual="Laira standing at a closed white bedroom door with her hand on the handle, turning to look at young Lail; Lail standing beside her at arm's length pointing back down the hallway towards a pair of polished black men's shoes on the shoe rack by the front door, whispering",
         camera="medium wide two-shot, eye level", amb="home_night"),
    dict(to=72, reason="action change: the siblings argue in whispers; Lail shrugs", chars=["lail_young", "laira"], loc="hallway",
         visual="young Lail in the hallway spreading both hands and shrugging with a cheeky indignant grimace; Laira facing him, worried and dejected, speaking softly with a tired older-sister look",
         camera="medium two-shot, eye level", amb="home_night"),
    dict(to=78, reason="location change: Lail in his room, smiling about someone", chars=["lail_young"], loc="lail_room",
         visual="young Lail in a plain grey t-shirt and dark-grey track pants, sitting up against the wooden headboard of his single cot on the light-blue sheet, hugging a white pillow to his chest, eyes half closed, a shy dreamy smile, his right hand pressed over his heart",
         camera="medium shot, eye level, the light-blue sheet as a calm lower third", amb="room_night"),
    dict(to=81, reason="action change: he jumps up and takes the folded slip from his jeans pocket and reads the verse", chars=["lail_young"], loc="lail_room",
         visual="young Lail in a plain grey t-shirt and dark-grey track pants standing beside the wicker laundry basket, a pair of jeans in one hand, carefully unfolding a small torn notebook slip with the other and gazing at it with a tender smile; the paper shows only faint illegible pencil scribbles",
         camera="medium shot, eye level", amb="room_night"),
    dict(to=84, reason="action change: back on his cot, he gazes at the slip, tucks it under the pillow and hugs another pillow", chars=["lail_young"], loc="lail_room",
         visual="young Lail sitting up against the headboard of his cot in a grey t-shirt, holding the small slip of paper up before his eyes, his dark chocolate-brown eyes shining, a happy shy smile, a white pillow hugged under his other arm; the paper shows only faint illegible scribble lines",
         camera="close-up, slightly from the side, his face in the upper half", amb="room_night"),
    dict(to=88, reason="scene change: later, Sana and Haizum in her private sitting room; she cries turned away from him", chars=["sana", "haizum"], loc="nook",
         visual=f"{SANA_SICK}, sitting at one end of the small grey sofa turned away towards the window, silent tears on her cheeks; {HAIZUM_LATE}, sitting apart at the other end with his hand pressed to his forehead, then turning to look at her with concern",
         camera="medium wide two-shot, eye level, the sofa in the middle, the rug as a calm lower third", amb="apartment_quiet_night", sens="intimacy",
         safe="the narrated scene on the bed is moved to a sofa; the couple sits apart"),
    dict(to=92, reason="action change: he leans closer asking her to see a doctor; she pulls away: 'don't touch me'", chars=["haizum", "sana"], loc="nook",
         visual=f"{HAIZUM_LATE}, leaning towards Sana on the small sofa with one hand resting on her shoulder, pleading tenderly; {SANA_SICK}, pulling away from him, crying angrily, eyes squeezed shut",
         camera="medium close two-shot, eye level", amb="apartment_quiet_night", sens="intimacy",
         safe="the narrated kiss on the cheek and caress replaced by his hand on her shoulder (married couple)"),
    dict(to=95, reason="emotional turning point: he refuses to leave again; she cries out about the child they lost", chars=["sana", "haizum"], loc="nook",
         visual=f"{SANA_SICK}, sitting upright and facing Haizum, crying out in anguish with one hand pressed to her chest, tears streaming; {HAIZUM_LATE}, sitting a little apart, frozen, stricken by her words",
         camera="medium two-shot, slightly over Haizum's shoulder onto Sana's face", amb="apartment_quiet_night", sens="other",
         safe="the lost baby is only spoken about, never shown"),
    dict(to=100, reason="emotional turning point: his confession of shared grief; both weep", chars=["haizum", "sana"], loc="nook",
         visual=f"{HAIZUM_LATE} and {SANA_SICK}, sitting side by side on the small sofa with a small gap between them, each sitting upright with their own head bowed (her head NOT resting on him), both weeping, his hand holding her hand on the seat between them; warm lamp light on their wet cheeks",
         camera="medium close two-shot, eye level", amb="apartment_quiet_night", sens="intimacy",
         safe="the narrated forehead-to-forehead and holding her in his arms replaced by sitting side by side holding hands"),
    dict(to=102, reason="action change: violent coughing; he brings her water", chars=["haizum", "sana"], loc="nook",
         visual=f"{SANA_SICK}, bent forward on the sofa coughing hard into her hand, her other hand on her chest; {HAIZUM_LATE}, hurrying back into the room holding out a glass of water, his face anxious",
         camera="medium wide two-shot, eye level", amb="apartment_quiet_night"),
    dict(to=106, reason="scene/action change and cliffhanger: she rushes off; Haizum's terrified face at the half-open door", chars=["haizum"], loc="door",
         visual=f"{HAIZUM_LATE}, standing at a half-open white door in the dark corridor, one hand gripping the door frame, his eyes wide and his face frozen in terror, calling out her name, cold white light from the doorway falling on his face; nothing visible beyond the door",
         camera="close-up on his face in the upper half, the dark corridor floor below", amb="home_night", sens="other",
         safe="her vomiting blood is never shown: only Haizum's terrified face at a half-open door; no washroom fixtures visible"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Sana came out to the sitting room carrying a glass of water and switched off the lights. The whole sitting room was left in a dim light.")
sh(2, "With the two children not at home, the whole house felt empty tonight. On any other night you would hear Layl playing games in his room,")
sh(3, "and Laira's sweet singing would echo through the house. Coughing, Sana carried the glass of water to the sofa and settled down.")
sh(4, "And to pass the time she turned on the TV. Just then the doorbell rang. Since the front door opens with a password,",
   [("doorbell_buzz", "ބެލް", -18)])
sh(5, "she was sure it was not the children. Coughing, Sana went and looked out through the peephole. She hesitated for a moment. The bell rang again.",
   [("doorbell_buzz", "ބެލް", -18)])
sh(6, "Torn in two, Sana opened the door, and standing at the door was Haizum. \"The children are at your house?\" Sana said softly. \"Yes.",
   [("door_open", "ހުޅުވައިލިއިރު", -18)])
sh(7, "Laira told me you were ill.\" Haizum answered in a gentle tone. Sana said nothing and stayed silent. \"Won't you tell me to come in?\"")
sh(8, "Haizum asked, looking at Sana's face. \"It's your own house, isn't it? Come in.\" Sana said, walking inside. Haizum stepped in and took off his shoes.",
   [("cloth_rustle", "ބޭލިއެވެ", -24)])
sh(9, "From the exhaustion on Sana's face and the sound of her coughing, it was clear how ill she was.")
sh(10, "Sitting down on the sofa, Haizum began to talk. \"Did you see a doctor?\" \"No, this is just an ordinary cold.\" Sana said carelessly.")
sh(11, "Haizum got up from the sofa and went close to Sana. And lovingly he touched Sana's forehead. But,")
sh(12, "at that very moment Sana pushed his hand away. \"Please, Sana, don't do this. If something happens to you, what will become of the children?\"",
   [("cloth_rustle", "ޖައްސައިލިއެވެ", -24)])
sh(13, "Haizum asked in a pleading tone. Sana gave no answer and stood with her head bowed. \"Sana, let it go now. Is seven years a short time?")
sh(14, "What happiness did the two of us get by staying this far apart? Our lives are passing in nothing but waiting.\" There was deep pain in Haizum's voice.",
   [("sigh", "ރިހުމެކެވެ", -22)])
sh(15, "At those words Sana's eyes filled with tears too. Pain was gripping her heart as well. Haizum gently took Sana's hand and turned her towards him.",
   [("sob_breath", "ކަރުނުން", -24)], hum=True)
sh(16, "Sana folded her arms and bowed her head because she could not meet Haizum's eyes. \"Come, let's go to the doctor.")
sh(17, "I don't think this is an ordinary cold. Your whole body is so hot.\" Not wanting to upset Sana any further, Haizum changed the course of the conversation.")
sh(18, "This time Sana did not pull her hand free from Haizum's. However far apart they lived, he was still her husband.")
sh(19, "Even when she went to the courts, Haizum never agreed to divorce her. Later Sana stopped trying too. And Haizum gave Sana time to come round.")
sh(20, "But he never thought that chance would drag on this long. The more the children grew up, the further Sana drifted away from Haizum.")
sh(21, "The two of them had to live in two houses because of the depression Sana was suffering. Whenever she saw Haizum, Sana's anger would spiral out of control,")
sh(22, "and with the fear that she might harm things and herself, Haizum made that decision only because he was forced to.")
sh(23, "Yet living apart from Sana was a very great hardship for Haizum. He would come to that house with all kinds of excuses.")
sh(24, "But when he saw Sana's displeasure and anger, he would bow his head and leave. Because he did not want such painful scenes repeated in front of the children.")
sh(25, "Because the harm of it might reach those children's young minds. \"Sana... I'm begging you, think of our children.\"")
sh(26, "There was pleading in Haizum's voice. When Sana raised her head and looked at Haizum, there was only hopelessness on her face. \"Please...\"")
sh(27, "Haizum said, even more softly than before. Just then Sana started coughing, and Haizum quickly picked up the glass of water from the small table and held it out to her.",
   [("cup_clatter", "ފެންތަށި", -22)])
sh(28, "Sana took the glass too and drank a sip of water. When the coughing eased a little, Sana looked at Haizum again.")
sh(29, "Sana knew that the worry showing on Haizum's face was the look that face always had for her. But,")
sh(30, "every time she saw Haizum, the bitter memories of the past welled up in Sana's heart, and the events of that day began to play before her. Sana closed her eyes and pulled back.",
   [("breath", "މަރައިލަމުން", -24)], hum=True)
sh(31, "Realising what had happened, Haizum pulled back too. Silence took over the whole room. Though the TV's sound was turned down,")
sh(32, "you could tell the TV was on only from the light falling across the sitting room. Haizum picked up the remote, switched off the TV and sat down on the sofa.")
sh(33, "His movements showed he had no intention of leaving. Holding the glass in her hand, Sana walked towards the kitchen.",
   [("footsteps_pavement", "ހިނގައިގަތީ", -24)])
sh(34, "Haizum rested his elbows on his knees and covered his face with both hands. Trying to make Sana understand had left him completely exhausted.",
   [("sigh", "ވަރުބަލިވެފައެވެ", -22)])
sh(35, "Just then came the sound of a glass being slammed into the sink. It was a sign of the resentment in Sana's heart.",
   [("cup_clatter", "ބެހެއްޓި", -14)])
sh(36, "As Haizum looked that way, there was the bang of a cupboard door and the clatter of things falling to the floor.",
   [("door_slam", "ޖެހި", -16), ("crash_clatter", "ވެއްޓި", -14)])
sh(37, "Haizum closed his eyes as if at his wits' end. Even so, at that very moment he got up from the sofa and strode quickly towards the kitchen.",
   [("footsteps_pavement", "ހިނގުމެއްގައި", -22)])
sh(38, "And he caught hold of Sana's hand as she was reaching for a glass dish in the cupboard, took the dish from her hand and put it back in the cupboard.",
   [("cup_clatter", "ބެހެއްޓިއެވެ", -20)])
sh(39, "\"That's enough, Sana! Even a sentence has to have a term, doesn't it? Seven years... Sana, seven years is not a short time. Our children have grown up.")
sh(40, "Tomorrow Laira might get married too. What are we teaching those children? I don't want to see this anger of yours in those children.\"")
sh(41, "Haizum said, gathering his courage. \"And I don't want this unfaithfulness of yours passed on to those children either!\"")
sh(42, "Sana shot back in a harsh tone. Haizum closed his eyes. Every time she got the chance, the words Sana threw at him filled him with shame.")
sh(43, "He himself accepted that he was the guilty one. \"Sana... how much more must I beg for forgiveness?\" Haizum said, taking hold of Sana's hand.")
sh(44, "Though Sana tried to pull her hand free, Haizum did not give her the chance. And he pulled Sana close to him by force.",
   [("cloth_rustle", "ދަމައިގަތެވެ", -22)])
sh(45, "Being ill, Sana could not put up much of a fight. Haizum drew Sana to his chest and held her.")
sh(46, "It was the first time he had held her like this since the trouble began. Sana began to cry. After a long stretch of seven years,",
   [("sob_breath", "ރޯން", -22)], hum=True)
sh(47, "resting her head on that chest, she remembered her own stubbornness. Sana knew too that Haizum had kept her without divorcing her because he loved her.")
sh(48, "If he had wanted, Haizum had every chance to take another wife without divorcing Sana. There was nobody who would have stopped him. But Haizum never did such a thing.")
sh(49, "Every single day he worked at making Sana understand. Even knowing all of that, seven years had passed in stubbornness. \"Forgive me...")
sh(50, "I beg your forgiveness with all my heart. It was a mistake I made, and I accept it.\" Haizum said gently.")
sh(51, "Sana went on sobbing. She did not know where Haizum had found such courage tonight.",
   [("sob_breath", "ގިސްލަމުންނެވެ", -22)])
sh(52, "Usually, whenever Sana got angry, Haizum would try to get away from the place. After a while of silence, Haizum drew back a little from Sana.")
sh(53, "And holding Sana's face in both hands, he looked at her. Sana's eyes were red from crying.")
sh(54, "Tears were falling from Haizum's eyes too. After wiping the tears from Sana's face, he pressed her to his chest once more.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(55, "\"Don't punish me this much. I know you are burning in this pain too. If you didn't love me, you wouldn't be this angry.\"")
sh(56, "Haizum said, kissing the top of Sana's head. Sana broke down crying again. And she struck at Haizum's chest. Though she didn't say a word,",
   [("soft_thud", "ތަޅައިގަތެވެ", -22)])
sh(57, "her movements showed she was trying to get away. \"Whatever you do, Sana, I am not leaving this place tonight.")
sh(58, "I came here to settle this one way or another. If you keep acting like this, I won't bring the children to this house any more.")
sh(59, "I'll send those children abroad, out of the Maldives.\" At these words of Haizum's, Sana's anger seemed to grow even stronger.")
sh(60, "Crying, she began hitting Haizum even harder than before. But Haizum held Sana even tighter than before and hid his face in her hair.",
   [("soft_thud", "ތަޅަން", -22)])
sh(61, "Haizum could feel the heat pouring off Sana's body. In the end, after struggling and struggling, Sana stopped, exhausted.",
   [("breath_heavy", "ވަރުބަލިވެގެން", -22)])
sh(62, "It seemed Sana understood that whatever she did, Haizum would not let go tonight. With the password entered, the front door of the house opened.",
   [("lock_click", "ޕާސްވޯޑް", -20), ("door_open", "ހުޅުވިއްޖެއެވެ", -18)])
sh(63, "In came Laira and Layl. A deep silence had taken over the whole house. Laira hurried to go to that room to check on her mum.",
   [("footsteps_pavement", "ވަދެގެން", -24)])
sh(64, "Last night too Mum had been very ill. Tonight they had left Mum alone and gone out only because Maama had asked them to.")
sh(65, "Laira went to Mum's bedroom door, took hold of the handle and turned it. But the door was locked from the inside. Just then Layl came and stopped beside her.",
   [("lock_click", "އަނބުރައިލިއެވެ", -20)])
sh(66, "\"Mamma, Mamma.\" Laira called softly. \"Big sister.\" Layl whispered, tapping Laira on the arm. \"Hmm.\"")
sh(67, "Laira looked over at Layl. \"Looks like Dad is here.\" Layl said very quietly. And he pointed at the shoes by the door.")
sh(68, "When Laira stepped forward and looked at the shoes, she was sure they were Dad's shoes. \"Dad came home after finishing his meeting.")
sh(69, "Maybe because I let slip that Mum was ill. I'm done for tomorrow. Mum will be so angry that I told Dad.\"")
sh(70, "Facing Mum's anger, Laira said in a dejected tone. \"If Mum is ill, of course you have to tell Dad!")
sh(71, "What are you even saying, sister!\" Layl said. \"You wouldn't understand, little brother. You're still a little kid.\" Laira said softly.")
sh(72, "Layl spread both hands and shrugged. And he pulled a face as if to say, when exactly am I going to be grown up.")
sh(73, "Laira didn't call Mum any more and walked towards her own room. Layl too quietly went into his room.",
   [("door_close", "ވަނެވެ", -22)])
sh(74, "He took off the clothes he had on and put them in the laundry basket, changed into his sleep clothes and lay down. Layl settled onto the light-blue sheet.",
   [("cloth_rustle", "ބާލައި", -24)])
sh(75, "And he pulled the pillow he was hugging even closer to his chest. Not long after he closed his eyes, a smile spread across his lips.")
sh(76, "After lying like that for a while, he slowly fluttered his lashes and opened his eyes. \"You've stolen my sleep.\"")
sh(77, "Layl whispered, as if speaking to someone. A faint smile showed on his lips.")
sh(78, "As he slowly rolled onto his back, he rubbed his chest with his right palm. It was as if the heart inside his chest had started beating to a new rhythm.",
   [("heartbeat", "ވިންދެއް", -20)], hum=True)
sh(79, "Suddenly remembering something, he sprang up from the bed. And almost running, he went and picked up the jeans lying in the laundry basket.",
   [("cloth_rustle", "ޖިންސު", -22)])
sh(80, "Slipping his hand into the jeans pocket, he took out the slip of paper torn from Saba's notebook, slowly unfolded it and looked at it.",
   [("paper_shuffle", "ކަރުދާސްކޮޅު", -20)])
sh(81, "\"While your eyes keep glancing my way, inviting my eyes to look, a smile slips onto your lips, then secretly runs away.\"")
sh(82, "After reading out the verse, Layl came back and lay down on the bed. And lying there gazing at it, he answered with a faint smile.")
sh(83, "It was as if a sparkle like lightning had flashed in those pretty, soft chocolate-coloured eyes. He slipped that slip of paper under the pillow he rested his head on,",
   [("paper_shuffle", "ކަރުދާސްކޮޅު", -22)])
sh(84, "then picked up the pillow lying beside him, laid it on his chest and hugged it with both arms. And with a happy smile he closed his eyes.")
sh(85, "Sana lay on the bed with her back to Haizum. Even then, tears kept falling from her eyes without stopping.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(86, "Haizum, sitting with his back against the headboard, had his right hand on his forehead. Hearing Sana sob, he took his hand from his forehead and looked towards Sana.",
   [("sob_breath", "ގިސްލުމުގެ", -22)])
sh(87, "And settling himself, he took Sana by the shoulder and turned her towards him. \"Stop it now, Sana.\" Haizum said gently.")
sh(88, "And he touched the side of Sana's neck. \"You're still so hot, Sana. Stop being stubborn and let's go to the doctor.\"")
sh(89, "Haizum said, moving a little closer to Sana. And after brushing aside the hair that had fallen over Sana's face,")
sh(90, "he kissed her cheek with great love. \"I don't want to go anywhere with you! Didn't I tell you not to touch me!\" Sana said, crying.",
   [("sob_breath", "ރޮމުން", -22)])
sh(91, "\"Sana, please, it's time to stop this now.\" Haizum said, lovingly stroking Sana's cheek. \"Leave me. Why did you even come here?\"")
sh(92, "Sana said, squeezing her eyes shut and pushing him away. It was as if the wounds in her heart were being torn open again. \"Sana, please!")
sh(93, "How long must I stay away? I can't bear it any more. Even if you're angry, even if you smash this whole house to pieces, this time I'm not leaving this house.")
sh(94, "I want to live with my family. Even if my life is to end, I want it to end beside you and the children.\"", hum=True)
sh(95, "There was resolve and emotion in Haizum's voice. \"Go and make that family with her! Will the child of ours that slipped from my hands because of your one mistake ever come back?\"",
   hum=True)
sh(96, "Sana began sobbing harder than before. Those words of Sana's struck Haizum's heart like a powerful dagger.",
   [("sob_breath", "ގިސްލެވެން", -20), ("heartbeat", "ޚަންޖަރެއް", -20)], hum=True)
sh(97, "Haizum pressed his forehead to Sana's forehead. \"Forgive me... I accept my fault.")
sh(98, "But the one who slipped away was not only your child. That was the light of my eyes too. The pain in your heart is in this heart too.")
sh(99, "You weren't the only one who was punished, I was too.\" Tears began to fall from Haizum's eyes too.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(100, "The tears running down Sana's cheeks and Haizum's tears mingled together. And Haizum drew Sana to his chest and hid her in his arms.")
sh(101, "Just then Sana again began to cough violently. Haizum got up at once, hurried out of the room and came back with a glass of water.",
   [("footsteps_pavement", "ނިކުމެގެން", -22), ("cup_clatter", "ފެންތައްޓެއް", -22)])
sh(102, "Even then Sana's coughing would not stop. After giving Sana a sip of water to drink, he set the glass aside.",
   [("cup_clatter", "ބެހެއްޓިއެވެ", -22)])
sh(103, "Suddenly Sana got up and ran towards the washroom. Haizum went after her. After retching, Sana threw up.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)], hum=True)
sh(104, "The sip of water she had just drunk came up, and she retched again. This time the washbasin filled with a deep red. Haizum's eyes went wide,",
   [("heartbeat", "ބޮޑުވެ", -18)], hum=True)
sh(105, "shock and fear showing on his face. Sana threw up again. This time too, it was only blood. \"Sana!\"",
   [("gasp", "ހައިރާންކަމާއި", -18)], hum=True)
sh(106, "Haizum cried out in a voice of pain that shattered the heart.", hum=True)
SHOTS = S

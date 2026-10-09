"""Beat/shot plan for Emme Fahu Message episode 326 (used by plan_beats.py).
A warm golden morning in the small third-floor Hulhumale apartment (Eethan's burnt pancakes, banter, breakfast), the
glowing reminder on the phone, then the rainy afternoon at the fertility clinic and Dr. Mathews' "I'm very sorry".
Rules: no embracing/kissing (the back-hug at the stove = side by side, her hand on his forearm), hijab fully covering
hair in every shot also at home and sitting up against the headboard, no readable text on phones/TV/books, the clinic
couples never touch, Dr. Mathews only across the desk."""

AMAAN = ("Amaan in her loose long-sleeved ankle-length cream dress and dusty-rose hijab fully covering her hair and neck, "
         "a thin silver wedding ring")
EETHAN_HOME = "Eethan in his faded plain navy t-shirt with a blank chest (no logo, no print) and grey jogger trousers"
EETHAN_OUT = ("Eethan in a dark-olive zip-up rain jacket over the navy t-shirt and dark jeans "
              "(NOT the grey joggers of the reference)")
SIDE = "standing side by side, NOT embracing, only her hand resting on his forearm"

LOC = {
    "bedroom": "the small bedroom of a modest third-floor apartment in Hulhumale, a simple wooden headboard against a "
               "pale wall, cream sheets, a small bedside table, thin cream curtains over a window, a half-open door to "
               "the sitting room",
    "sitting": "the small sitting room of a modest, slightly old third-floor apartment in Hulhumale, warm wooden floor, "
               "a worn grey sofa with one vermilion-red cushion, a slow ceiling fan, thin cream curtains, many small "
               "framed photos on the pale walls, an open doorway to a tiny kitchen",
    "building": "a modest new six-storey apartment block on a quiet street in Hulhumale, pale concrete facade with small "
                "balconies and potted plants, a third-floor window glowing warm, young trees along a wet pavement",
    "kitchen": "the tiny kitchen of a modest third-floor apartment in Hulhumale, a narrow counter, a small gas stove with a "
               "frying pan, a white kettle, wooden cupboards, a small open window over the counter, a vermilion-red mug "
               "on the counter",
    "dining": "a small round wooden dining table by the sitting-room window of a modest Hulhumale apartment, two cups of "
              "tea, a plate with a lopsided tower of pancakes, a bowl of strawberries and a bottle of syrup",
    "street": "a Hulhumale street seen from a third-floor window in the morning, wet shining roads after rain, cars and "
              "motorbikes, people walking under umbrellas in light raincoats, young trees, apartment blocks",
    "clinic_wait": "the waiting room of a quiet private fertility clinic in Male, plain pale cream walls, neat rows of "
                   "grey upholstered chairs, a small TV high on the wall, a reception counter with a coffee machine, a "
                   "large window with rain on the glass",
    "clinic_office": "a doctor's consultation room in a fertility clinic, a wooden desk with a closed laptop, a small "
                     "plant and a few blank folders, two chairs facing the desk, pale cream walls, a window with rain "
                     "streaks and grey light",
}
MOOD = {
    "bedroom": "early morning gold, warm golden sunlight glowing through thin cream curtains, soft and peaceful, tender",
    "sitting": "warm golden morning light through the curtains, slow dust motes floating in the sunbeams, steam and a "
               "cosy, tender, ordinary happiness; a few grey monsoon clouds far outside",
    "building": "fresh early morning gold after night rain, low warm sun breaking through grey monsoon clouds, the street "
                "still wet and shining, calm",
    "kitchen": "warm golden morning light through the small kitchen window mixed with a little pancake smoke, playful, "
               "tender and intimate in a modest way, cool morning air from the window",
    "dining": "8 o'clock morning, soft golden light from the window mixed with cool grey monsoon daylight, cosy and "
              "playful at first, then a quiet tension",
    "street": "morning, grey monsoon sky with a little golden light breaking through, wet reflective streets, busy "
              "ordinary city life",
    "clinic_wait": "rainy grey afternoon, flat cool fluorescent light mixed with grey-blue window light, rain on the "
                   "glass, sterile, quiet and heavy with waiting",
    "clinic_office": "rainy grey afternoon, cool grey window light and one warm desk lamp, hushed, heavy, a sense of "
                     "bad news coming",
}

BEATS = [
    dict(to=5, reason="episode opening: Amaan waking to the everyday sounds of Eethan", chars=["amaan"], loc="bedroom",
         visual=f"{AMAAN} (also a loose long grey cardigan over the dress), sitting up against the wooden headboard with "
                "the cream sheet over her knees, eyes still closed, a slow soft smile spreading on her face as she listens "
                "to sounds from the kitchen; golden sunlight through the thin curtains falls across her face; the "
                "half-open door to the bright sitting room beside her",
         camera="medium shot, eye level, her face in the upper third, the folded sheet as a calm lower third",
         amb="apartment_morning", sens="clothing",
         safe="she is in her modest outfit with hijab, sitting up against the headboard (never lying down)"),
    dict(to=7, reason="scene change: the apartment itself in the golden morning light", loc="sitting",
         visual="the empty little sitting room bathed in golden morning light: sunbeams slanting through thin cream "
                "curtains with dust motes floating slowly in them, a slow white ceiling fan, a worn sofa with a "
                "vermilion-red cushion, through the doorway the tiny kitchen where a white kettle steams softly on the "
                "stove; no people",
         camera="wide shot, eye level, the sunbeams and fan in the upper half, the warm wooden floor as a calm lower third",
         amb="apartment_morning"),
    dict(to=10, reason="scene change: the third-floor apartment in its year-old building", loc="building",
         visual="the modest pale apartment block seen from the wet pavement across the quiet street, one third-floor "
                "window with thin cream curtains glowing warm gold, small balconies with potted plants, young trees, "
                "puddles reflecting the morning sky; no people in focus",
         camera="wide establishing shot, low angle, the building in the upper two-thirds, the wet shining pavement as a "
                "calm lower third", amb="city_day"),
    dict(to=15, reason="detail change: the wall of framed photos of ten years together",
         loc="sitting",
         visual="a close view of an empty pale wall above a low wooden shelf, crowded with many small wooden picture "
                "frames in warm sunlight; inside the frames only tiny soft blurry snapshots: a car on a coastal road, a "
                "beach sunset, a canal city with gondola-like boats and pigeons, a birthday cake with candles, a tiny "
                "distant couple where the woman wears a dusty-rose hijab; the room is empty, NO people in the room, "
                "nobody on a sofa, only the wall of frames, a small plant and a vermilion-red vase on the shelf",
         camera="medium close-up of the wall, straight on, the frames in the upper two-thirds, a low wooden shelf as a "
                "calm lower third", amb="apartment_morning", sens="intimacy",
         safe="honeymoon/road-trip photos kept tiny and blurry, Amaan in hijab; no character references so no couple "
              "appears in the room (first try showed them in a close pose on the sofa)"),
    dict(to=17, reason="action change: Amaan reaches for her phone and frowns at another cold rainy day",
         chars=["amaan"], loc="bedroom",
         visual=f"{AMAAN} with a loose long grey cardigan over the dress, sitting up against the headboard and leaning "
                "across to pick up a phone from the far side of the mattress, its screen a soft blank glow; she glances "
                "toward the window where grey monsoon clouds are rolling in over the golden light, her face scrunched "
                "in sleepy displeasure",
         camera="medium shot, slightly high angle, her face in the upper third", amb="apartment_morning",
         sens="clothing",
         safe="narration's messy hair, his big hoodie and bare feet are not shown: she wears her cream dress, grey "
              "cardigan and hijab"),
    dict(to=20, reason="character change: Eethan at the stove burning the pancakes", chars=["eethan"], loc="kitchen",
         visual=f"{EETHAN_HOME}, standing at the small stove in the tiny kitchen, holding a frying pan with a slightly "
                "burnt pancake in one hand and a phone to his ear in the other, a wisp of smoke rising from the pan, "
                "grinning to himself without looking up; golden light from the small window",
         camera="medium shot from the kitchen doorway, eye level, his face in the upper third, the counter as a calm "
                "lower third", amb="apartment_morning", sens="clothing",
         safe="the 'university T-shirt' is a blank faded navy t-shirt with no logo or text"),
    dict(to=23, reason="characters change: Amaan leans in the doorway and the banter begins",
         chars=["amaan", "eethan"], loc="kitchen",
         visual=f"{AMAAN} with a loose long grey cardigan, leaning against the kitchen door frame with folded arms, "
                f"smiling with one corner of her lips and narrowing her eyes teasingly; {EETHAN_HOME} at the stove a few "
                "steps away, turning his head to look up at her, amused, the frying pan in his hand",
         camera="medium wide two-shot, eye level", amb="apartment_morning"),
    dict(to=28, reason="action change: Amaan comes close beside him at the stove", chars=["amaan", "eethan"],
         loc="kitchen",
         visual=f"{AMAAN} and {EETHAN_HOME} {SIDE} at the small stove, both smiling down at the frying pan as he flips a "
                "pancake with a spatula, her shoulder close beside his arm, his phone set down on the counter; cool "
                "morning air through the small open window lifts the edge of a curtain; quiet, content",
         camera="medium shot from the side of the counter, eye level, faces in the upper third, the counter top as a calm "
                "lower third", amb="apartment_morning", sens="intimacy",
         safe="the back-hug around his waist becomes standing side by side, her hand resting on his forearm"),
    dict(to=31, reason="action change: playful teasing, she pretends to be angry", chars=["amaan", "eethan"],
         loc="kitchen",
         visual=f"{AMAAN} and {EETHAN_HOME} standing side by side at the stove turned toward each other, NOT touching; "
                "Eethan laughing softly with crinkled eyes, the spatula in his hand; Amaan with a mock-offended pout, "
                "eyebrows raised, trying not to smile; golden kitchen light",
         camera="medium close two-shot, eye level", amb="apartment_morning"),
    dict(to=36, reason="emotional turning point: 'I love you' - they look into each other's eyes",
         chars=["amaan", "eethan"], loc="kitchen",
         visual=f"close two-shot of {AMAAN} and {EETHAN_HOME} standing side by side at the stove, faces turned to each "
                "other at a modest distance, gazing into each other's eyes with deep quiet tender smiles, her hand "
                "resting on his forearm; warm golden morning light glowing behind them, steam softly rising",
         camera="close two-shot in profile, eye level, faces in the upper half", amb="apartment_morning",
         sens="intimacy",
         safe="his thumb on her temple and 'in each other's arms' become a shared loving look, side by side, hand on "
              "forearm only"),
    dict(to=38, reason="action change: the kettle shrieks and Amaan steps away laughing", chars=["amaan", "eethan"],
         loc="kitchen",
         visual=f"the white kettle on the stove whistling with a burst of steam; {AMAAN} stepping back from the stove "
                f"laughing with a hand raised; {EETHAN_HOME} reaching for the kettle handle, grinning",
         camera="medium wide shot, eye level", amb="apartment_morning"),
    dict(to=42, reason="time and scene change: breakfast at 8 o'clock, the syrup banter",
         chars=["amaan", "eethan"], loc="dining",
         visual=f"{AMAAN} and {EETHAN_HOME} sitting across the small round table from each other; Amaan pouring far too "
                "much golden syrup over her pancakes, making a playful face; Eethan holding a fork, eyebrows raised, "
                "laughing at the syrup; two cups of tea, a lopsided tower of pancakes, a bowl of red strawberries",
         camera="medium wide shot from the side of the table, eye level, faces in the upper third, the table top as a calm "
                "lower third", amb="apartment_morning"),
    dict(to=45, reason="scene change: the city waking up outside the window", loc="street",
         visual="view down from a third-floor window onto a Hulhumale street waking up: cars driving on wet shining "
                "roads, motorbikes and a cyclist hurrying to work, people in light raincoats with headphones walking "
                "under umbrellas, puddles reflecting a grey sky with a little golden light; the window frame edge "
                "visible; no readable signs",
         camera="high angle view through a window, the street in the upper two-thirds, the wet window sill as a calm "
                "lower third", amb="city_day"),
    dict(to=48, reason="action change: the phone vibrates with the doctor reminder; Amaan freezes",
         chars=["amaan", "eethan"], loc="dining",
         visual=f"{AMAAN} frozen at the breakfast table holding her tea cup halfway up, her eyes fixed on her phone lying "
                "face up on the table glowing with a soft blank light (no text, no numbers); "
                f"{EETHAN_HOME} across the table, fork paused, quietly noticing her face",
         camera="medium shot, eye level, faces in the upper third, the glowing phone on the table top in the lower third",
         amb="apartment_morning", sens="other",
         safe="the '10:30 Dr. Mathews' reminder is shown only as a blank glowing phone screen"),
    dict(to=51, reason="action change: Eethan reaches across and holds her hand, a silent promise",
         chars=["amaan", "eethan"], loc="dining",
         visual=f"across the breakfast table {EETHAN_HOME} reaches over and holds Amaan's hand on the table top, both "
                "hands with simple wedding rings in the middle of the frame between the tea cups; above, Eethan's calm "
                f"steady smile and {AMAAN} returning a small smile that does not quite reach her eyes; the phone now "
                "turned face down",
         camera="medium close-up, eye level, faces in the upper part, joined hands at the centre", amb="apartment_morning"),
    dict(to=54, reason="time and scene change: that afternoon, the fertility clinic waiting room", loc="clinic_wait",
         visual="the quiet clinic waiting room: neat rows of grey chairs, pale cream walls, a small TV high on the wall "
                "showing only a soft blur of kitchen colours, a reception counter with a coffee machine and paper cups, "
                "rain streaking down the big window, a few anonymous patients sitting far apart in soft focus",
         camera="wide shot, eye level, the room in the upper two-thirds, the shiny floor as a calm lower third",
         amb="clinic_waiting", transition="black"),
    dict(to=57, reason="character change: Amaan beside Eethan, turning her wedding ring", chars=["amaan", "eethan"],
         loc="clinic_wait",
         visual=f"{AMAAN} sitting on a grey waiting-room chair beside {EETHAN_OUT}, her eyes lowered, nervously turning "
                "the thin silver wedding ring on her finger; Eethan sitting calmly beside her, glancing at her with "
                "quiet concern; rain on the window behind them",
         camera="medium shot, eye level, faces in the upper third, her hands with the ring in the middle", amb="clinic_waiting",
         sens="other", safe="the blood tests, ultrasounds and hormone treatments are only mentioned, never shown"),
    dict(to=60, reason="character change: the other couples in the waiting room", loc="clinic_wait",
         visual="in the waiting room, opposite: a young woman in a soft green hijab and loose long dress turning the "
                "blank pages of a baby-names book, her husband beside her, both smiling, a small gap between them, not "
                "touching; further back by the rainy window a pregnant woman in a lilac hijab and loose long dress "
                "resting one hand on her belly and laughing while her husband sits beside her, leaning slightly to say "
                "something, not touching her",
         camera="medium wide shot, eye level", amb="clinic_waiting", sens="intimacy",
         safe="the couples sit modestly side by side and never touch; the book has blank pages"),
    dict(to=62, reason="return to Amaan: she looks away, ashamed of her envy", chars=["amaan", "eethan"],
         loc="clinic_wait", reuse="beat_017", visual="(reuse of beat_017)", amb="clinic_waiting"),
    dict(to=64, reason="action change: the nurse calls; Eethan stands and offers his hand",
         chars=["eethan", "amaan"], loc="clinic_wait",
         visual=f"{EETHAN_OUT} standing up first beside the row of grey chairs and holding his hand out to Amaan; "
                f"{AMAAN} taking his hand and rising from her chair; in the background a young nurse in light-blue scrubs "
                "and a white hijab fully covering her hair stands at an open corridor doorway holding a blank clipboard",
         camera="medium wide shot, eye level", amb="clinic_waiting"),
    dict(to=67, reason="scene and character change: Dr. Mathews' office, his smile looks sadder today",
         chars=["dr_mathews", "amaan", "eethan"], loc="clinic_office",
         visual="Dr. Mathews standing behind his desk with a kind but noticeably sad smile, one hand gesturing to the two "
                f"chairs; {AMAAN} and {EETHAN_OUT} just sitting down in the chairs across the desk, seen in three-quarter "
                "view from behind and to the side, Amaan's face tense; rain streaks on the window behind the doctor",
         camera="medium wide shot, eye level, faces in the upper half, the desk top as a calm lower third",
         amb="clinic_room", sens="other", safe="Dr. Mathews stays across the desk; no contact with Amaan"),
    dict(to=70, reason="strong emotional turning point: 'I'm very sorry' - tight framing on the news",
         chars=["dr_mathews", "amaan", "eethan"], loc="clinic_office",
         visual="tight dramatic framing: Dr. Mathews seated across the desk leaning slightly forward, one hand resting "
                "flat on the desk, sad gentle eyes behind rimless glasses as he speaks softly; in the near foreground at "
                f"the right edge, {AMAAN} in three-quarter profile, frozen, eyes wide and glistening; at the left edge "
                f"{EETHAN_OUT}, his jaw tight, turning toward her; grey rainy light, the room feels small",
         camera="close-up over the desk, eye level, faces in the upper two-thirds, the desk top as a dark calm lower third",
         amb="clinic_room", sens="other", safe="bad news shown only through faces and a hand on the desk"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The first sound Amaan heard every morning was not her alarm clock. It was the sound of her husband, Eethan.")
sh(2, "Not always his voice. Sometimes it was the soft sound of Eethan's slippers moving across the wooden floor. Or else,",
   [("footsteps_pavement", "ފައިވާނުގެ", -24)])
sh(3, "the sound of the kitchen cupboards opening because he was hungry. Or the sound of him humming around the apartment while making tea.",
   [("creak", "ހުޅުވާ", -22)])
sh(4, "It was never the same tune. Nor was it a very beautiful one. But after nine years together, it had become an ordinary sound.")
sh(5, "Every day it was a sound that brought a smile to Amaan's face before she even opened her eyes. Sunlight came in between the curtains,")
sh(6, "and spread its light through the apartment. In the golden light of an ordinary fresh morning, dust motes drifted slowly in the air.")
sh(7, "The ceiling fan turned to a slow, pleasant rhythm. The fresh smell of brewing tea had travelled from the sitting room all the way to the bedroom.")
sh(8, "It was not a big apartment. It was on the third floor of a building that surely wasn't more than a year old.")
sh(9, "The building's lift had been 'temporarily' broken for more than a year. In the cold season you could hear the floors of the whole building,")
sh(10, "and with every change of season the bathroom tap dripped more. The kitchen was so small that when the two of them cooked together they always bumped into each other.")
sh(11, "But they never minded. The walls were covered with photos of nearly ten years spent together.")
sh(12, "Road trips on holidays. Sunsets on the beach. The honeymoon in Italy.")
sh(13, "In Venice, when Eethan pretended to be scared of the pigeons, Amaan laughed so hard she nearly dropped the camera.")
sh(14, "Birthday dinners, and photos taken in all sorts of places because one of them insisted it would be a shame not to take one.")
sh(15, "Every frame showed one thing. The two of them. Not perfect. But happy. Stretching,")
sh(16, "Amaan reached across to the other side of the bed for the phone lying there. Having to welcome yet another cold day, displeasure showed on her face.",
   [("cloth_rustle", "ދިއްކޮށްލިއެވެ", -24), ("sigh", "ނުރުހުންވުމުގެ", -22)])
sh(17, "She got up, pushed back her hair, pulled on one of Eethan's big hoodies and walked barefoot into the sitting room.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(18, "She found Eethan just as she expected: in grey sweatpants and a university T-shirt whose logo had faded from years of washing.")
sh(19, "He held a frying pan in one hand and was saying something into the phone in the other. The smell of butter filled the whole apartment. 'My queen.",
   [("pan_sizzle", "ތަވާ", -20)])
sh(20, "You're awake?' Eethan said without looking at Amaan, and smiled. 'Burnt the pancakes again, didn't you?'")
sh(21, "Amaan said, leaning against the door frame. 'I prioritise crispiness,' Eethan replied.")
sh(22, "'Then how come the smoke alarm goes off every single day?' Amaan said, smiling with one corner of her mouth. 'I disabled it.'")
sh(23, "Eethan looked up, amused. 'What?' Amaan narrowed her eyes. 'Just joking,' Eethan said at once. Amaan stepped forward,")
sh(24, "and wrapped her arms around Eethan's waist from behind. Though the cold morning air from the opened kitchen window was on his skin,",
   [("wind_gust", "ހުޅުވާލުމުން", -24)])
sh(25, "Amaan felt Eethan's warmth. Eethan put the phone down and, holding Amaan's hand with one hand, kept flipping the pancakes.",
   [("pan_sizzle", "ޕޭންކޭކު", -22)])
sh(26, "Neither of them spoke. Some silences are conversations in themselves.")
sh(27, "'If you keep holding on like that, the morning tea will be late,' Eethan said after a while. 'I have no complaints.'")
sh(28, "Amaan said, holding on tighter than before. 'You'll complain when you're hungry,' Eethan went on. 'I'm already hungry,' Amaan said.")
sh(29, "'For pancakes?' 'No. For your attention.' He laughed softly, in his usual way. 'You're a thirty-two-year-old woman.'")
sh(30, "When Eethan said that, Amaan wanted to hide how much she liked it. 'What's the problem?' Amaan pretended to be angry.")
sh(31, "And so for a while the two of them kept joking with each other, the same as every day. 'I love you so much, Amaan.'")
sh(32, "The joke ended as ordinarily as it had begun. Eethan touched Amaan's temple with his thumb.")
sh(33, "With their four eyes meeting, anyone who looked at them could see the love between them.", hum=True)
sh(34, "Just like the day they first met, there was still love between that husband and wife. 'I love you too, Eethan.'", hum=True)
sh(35, "For a short moment, it was as if everything else in the world was far away. No work to do. No responsibilities.")
sh(36, "Only the smell of tea, the warmth of the morning light, and the ordinary happiness of being in each other's arms.")
sh(37, "Suddenly the kettle began to shriek. Amaan let out a deep, dramatic sigh. 'The kettle is so jealous.'",
   [("kettle_whistle", "ކެކޭ", -16), ("sigh", "ނޭވާއެއް", -22)])
sh(38, "Saying that, Amaan laughed and stepped back, giving Eethan room to rescue the morning tea before it burnt.")
sh(39, "By eight o'clock the dining table was full. Besides two cups of tea,",
   [("cup_clatter", "ތަށީގެ", -22)])
sh(40, "there was a lopsided tower of pancakes leaning to one side, strawberries that according to Eethan complete the meal, and the maple syrup Amaan always pours far too much of.",
   [("pour", "ސިރަޕް", -22)])
sh(41, "'I think it would be fair to call the syrup you pour soup,' Eethan said after a bite. 'That's called eating sweetly.'")
sh(42, "Amaan said without stopping. 'That's called diabetes,' Eethan said without the slightest hesitation. Amaan made a face at him.")
sh(43, "Eethan surrendered at once. Outside the window people had begun to wake up. Cars drove along roads wet from the rain.",
   [("car_pass", "ކާރުތައް", -22)])
sh(44, "As cyclists hurried to get to work, people walked along the street with headphones tucked inside their coats.",
   [("motorbike_pass", "ބައިސިކަލް", -22)])
sh(45, "Each of them carried the story of their own hidden life. Inside the apartment, time moved much more slowly.")
sh(46, "Unhurried. Slowly. Carefully. When Amaan's phone vibrated on the table, she froze, holding her tea cup.",
   [("phone_buzz", "ވައިބްރޭޓްވުމާއެކު", -16)])
sh(47, "The phone screen lit up. It was a reminder Amaan had set for herself. '10:30 a.m. Dr.")
sh(48, "Mathews.' She looked at it only for a moment before turning the phone over. Eethan noticed. He always noticed.")
sh(49, "But he asked no question. Instead, he slowly reached across the table and held Amaan's hand. A silent promise.")
sh(50, "Whatever happened today, they would face it together. Amaan held Eethan's hand too and returned a smile.", hum=True)
sh(51, "But that smile was not complete. Still, Eethan smiled, as if he believed that one day her smile would be complete again.",
   hum=True)
sh(52, "It was that afternoon. Nothing ever changes at the fertility clinic. The same pale cream walls.")
sh(53, "Rows of chairs neatly lined up. The TV fixed high on the wall, every day quietly showing a cooking programme nobody watches.")
sh(54, "The smell of fresh coffee from the reception counter mixed with the smell of medicine. It was a place built to renew hope.")
sh(55, "But for Amaan it had slowly become a place where hopes die. In the waiting room, Amaan sat beside Eethan.", hum=True)
sh(56, "She sat turning the silver wedding ring that had been on her finger for about seven years.")
sh(57, "It was a habit she had picked up between the blood tests, ultrasounds, hormone injections and treatments. Opposite them,")
sh(58, "a woman was turning the pages of a baby-names book, and every time they found a name they liked, the couple smiled.",
   [("page_turn", "އުކަމުން", -22)])
sh(59, "By the window a woman sat gently resting her hand on her growing belly.")
sh(60, "When her husband leaned close and said something, the woman laughed. Amaan looked away.")
sh(61, "She was disgusted with herself for it. Not because she wasn't happy for them. She truly was happy for them.", hum=True)
sh(62, "She only wished she could feel what it was like to sit in their place. 'Eethan and Amaan?'")
sh(63, "The nurse's gentle voice broke the silence. Without a word, Eethan stood up first and held out his hand to Amaan.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(64, "Amaan took his hand and stood, as she always did. Dr. Mathews greeted them with the same kind smile he had given them for the past five years.")
sh(65, "It was a familiar smile. A smile that celebrated even the smallest successes. A smile that softened even")
sh(66, "the most painful, heart-breaking news. But today that smile seemed sadder than on other days. 'Please, sit down.'")
sh(67, "Amaan already knew. Before disappointing news, doctors' voices grow softer. The room suddenly felt smaller.", hum=True)
sh(68, "'I know how patiently you have both waited for this cycle of treatment.' Dr. Mathews rested his hand on the desk.")
sh(69, "Amaan's heart began to race. 'We received the test results this morning.' Silence. 'I'm very sorry.'",
   [("heartbeat", "ހިންގުން", -18)], hum=True)
sh(70, "Those words were spoken with a practised gentleness.", hum=True)
SHOTS = S

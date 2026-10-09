"""Beat/shot plan for Tedhuveriloabi episode 456 (used by plan_beats.py)."""

LOC = {
    "house": "the small plain sitting room of an old house in a narrow Malé lane in the morning, whitewashed walls with faded paint, a simple narrow bed with a thin mattress and a cotton blanket against the wall, a small wooden table, a louvered wooden window letting in daylight, two plastic chairs",
    "lane": "a narrow Malé lane outside a small old house in the morning, low whitewashed walls, potted plants, a sleek black car parked at the doorstep with its rear door open",
    "car": "inside a sleek black car driving through the streets of Malé in daylight, dark leather seats, city buildings passing by in a soft blur outside the windows",
    "er": "the emergency wing of ADK Hospital in Malé, a cool white corridor in front of closed frosted-glass double doors, pale grey floor, fluorescent ceiling light, no signs",
    "counter": "the payment counter in the cool white lobby of ADK Hospital in Malé, a glass partition with a clerk behind it, a card terminal on the counter, a corridor leading away behind, no signs",
    "corridor": "a long cool-white corridor of ADK Hospital in Malé, pale grey polished floor, a row of plastic waiting chairs along the wall, frosted glass doors, fluorescent ceiling lights and a window at the far end, no signs",
    "sunset": "outside ADK Hospital in Malé at sunset, a quiet paved forecourt with a low wall and potted palms, a golden sky over the city rooftops with a glimpse of the sea in the distance",
    "zaahir": "Ahmed Zaahir's dark luxurious private study at night, a heavy wooden desk, a leather chair, a tall window looking out over the lights of Malé",
}
MOOD = {
    "house": "morning daylight through the louvers, muted warm tones, anxious and fragile",
    "lane": "bright morning light, urgent, frightened",
    "car": "daylight flickering through the windows, urgent and tearful, tender",
    "er": "cold white fluorescent light, helpless, anxious",
    "counter": "cool white light, quiet resolve",
    "corridor": "cool white hospital light with warm amber accents from the far window, emotionally charged",
    "sunset": "golden sunset light, warm amber and plum sky, peaceful, tender and hopeful",
    "zaahir": "night, low cold blue light and deep shadows, menacing",
}

BEATS = [
    dict(to=4, reason="new episode opening: Rafhaan examines the envelope in Layaali's house", chars=["rafhaan", "layaali", "qaasim"], loc="house",
         visual="Rafhaan standing beside a small wooden table holding an opened brown paper envelope with a bundle of banknotes inside, frowning thoughtfully at a small folded white note in his other hand (blank paper, nothing readable); Layaali standing by the wall behind him with her hands clasped, anxious; in the background frail Qaasim lying on a simple narrow bed under a cotton blanket",
         camera="medium shot, eye level", amb="home_day"),
    dict(to=8, reason="action change: Qaasim tries to rise, pleads and collapses coughing; Layaali and Aminath rush to him", chars=["qaasim", "layaali", "aminath", "rafhaan"], loc="house",
         visual="Qaasim half-risen on his simple narrow bed, coughing into a folded clean white cloth held to his mouth, his eyes squeezed shut, weak; Layaali kneeling at the bedside holding his shoulders and Aminath beside her supporting his back, both frightened; Rafhaan standing a step behind them, alarmed, the brown envelope lowered in his hand",
         camera="medium shot, slightly high angle", amb="home_day", sens="injury",
         safe="Qaasim coughing blood is never shown: he coughs into a clean white cloth, only the family's frightened faces"),
    dict(to=9, reason="scene and action change: Rafhaan carries Qaasim out to his car", chars=["rafhaan", "qaasim", "layaali", "aminath"], loc="lane",
         visual="Rafhaan carrying frail Qaasim in his arms out of the doorway of the small old house towards a black car with its rear door open; Layaali hurrying beside them with a worried face, Aminath following behind with her hand at her chest",
         camera="medium wide, eye level", amb="city_day"),
    dict(to=12, reason="scene change: the drive to the hospital", chars=["layaali", "qaasim", "rafhaan"], loc="car",
         visual="the back seat of the car: Layaali sitting with tears on her cheeks, cradling her father's head on her lap, Qaasim lying across the seat with his eyes closed; in the front Rafhaan at the steering wheel, his worried eyes glancing at her in the rear-view mirror",
         camera="medium shot from the front passenger side looking back", amb="car_interior"),
    dict(to=14, reason="scene change: hospital emergency, the doctor's verdict", chars=["doctor", "layaali", "aminath"], loc="er",
         visual="the doctor in his white coat speaking gravely to Layaali and Aminath outside closed frosted emergency-room doors; Layaali standing stunned with her hands pressed to her mouth, Aminath holding her arm, both lost and helpless",
         camera="medium shot, eye level", amb="hospital_corridor"),
    dict(to=15, reason="action and place change: Rafhaan pays at the counter", chars=["rafhaan", "layaali"], loc="counter",
         visual="Rafhaan at the hospital payment counter handing a plain bank card (nothing printed visible) to a clerk behind the glass, his face calm and determined; in the background Layaali walking towards him from the corridor, surprised",
         camera="medium shot, three-quarter angle", amb="hospital_corridor"),
    dict(to=18, reason="action change: Layaali questions him in the corridor", chars=["layaali", "rafhaan"], loc="corridor",
         visual="Layaali facing Rafhaan in the hospital corridor at a respectful distance, her hands clasped at her chest, eyes wet, asking him why; Rafhaan looking straight into her eyes with a calm, sincere, reassuring face",
         camera="medium two-shot in profile", amb="hospital_corridor"),
    dict(to=21, reason="emotional turning point: his unfinished words stir Layaali's heart", chars=["layaali"], loc="corridor",
         visual="close-up of Layaali in the hospital corridor, her eyes wide and shining, one hand resting on her chest over her heart, lips slightly parted, moved and startled; soft bokeh of the corridor behind her",
         camera="close-up", amb="hospital_corridor", sens="romance",
         safe="feelings shown only through her face and hand on her own heart; Rafhaan out of frame"),
    dict(to=24, reason="characters change: Ahna and Zoya arrive", chars=["ahna", "zoya"], loc="corridor",
         visual="Ahna striding down the hospital corridor in high heels with a smug, triumphant sneer, chin raised, her small gold handbag on her arm; Zoya one step behind her with a sly smile",
         camera="medium wide, low angle down the corridor", amb="hospital_corridor"),
    dict(to=27, reason="action change: Rafhaan shows the evidence on his phone", chars=["rafhaan", "ahna", "zoya"], loc="corridor",
         visual="Rafhaan with a cold faint smile holding up his smartphone towards Ahna, the screen facing her and away from the viewer; Ahna in front of him, her smugness beginning to falter; Zoya just behind her shoulder",
         camera="medium over-the-shoulder shot", amb="hospital_corridor"),
    dict(to=31, reason="emotional turning point: Ahna exposed, Zoya steps back", chars=["ahna", "zoya"], loc="corridor",
         visual="close shot of Ahna, her face drained pale, eyes wide in shock, lips parted; behind her Zoya stepping backwards in fear, one hand raised near her mouth",
         camera="medium close-up", amb="hospital_corridor", hum_note="exposure"),
    dict(to=34, reason="framing change: Rafhaan's cold accusing gaze", chars=["rafhaan"], loc="corridor",
         visual="close-up of Rafhaan's face in the cool corridor light, a sharp, piercing, contemptuous gaze, jaw set, cold and controlled",
         camera="close-up, slightly low angle", amb="hospital_corridor"),
    dict(to=37, reason="the confrontation continues: Ahna denies, Rafhaan says the police have the evidence (reuse)", reuse="beat_010",
         chars=["rafhaan", "ahna", "zoya"], loc="corridor", visual="(reuse) Rafhaan showing the phone to Ahna", amb="hospital_corridor"),
    dict(to=39, reason="action change: Zoya abandons Ahna and flees", chars=["zoya", "ahna"], loc="corridor",
         visual="Zoya turning away and hurrying off down the corridor in panic, glancing back over her shoulder; Ahna left standing alone in the foreground, stunned and trembling",
         camera="medium wide", amb="hospital_corridor"),
    dict(to=41, reason="focus moves to Layaali and Aminath: tears of gratitude", chars=["layaali", "aminath"], loc="corridor",
         visual="Layaali and her mother Aminath standing together by the corridor wall, amazed and speechless; tears of gratitude running down Layaali's cheeks, her eyes lifted upward, her hands softly cupped in front of her in thanks to God",
         camera="medium shot", amb="hospital_corridor"),
    dict(to=46, reason="characters change: the doctor comes out of the operation theatre", chars=["doctor", "layaali", "aminath"], loc="corridor",
         visual="the senior doctor in a surgical cap and white coat just stepping out of the operation theatre double doors, pulling his surgical mask down from his face with a worried look; Layaali has run up and stopped about two steps in front of him, not touching him, her hands clasped together at her chest, pleading, Aminath anxious just behind her with her hand on her daughter's shoulder",
         camera="medium shot, eye level", amb="hospital_corridor"),
    dict(to=48, reason="emotional turning point: Ahna steps forward in tears", chars=["ahna", "layaali", "rafhaan"], loc="corridor",
         visual="in the corridor Ahna stepping forward with tears streaming down her face, all her pride gone, one hand on her chest; in the foreground Layaali and Rafhaan turned towards her in surprise, seen partly from behind",
         camera="medium shot over their shoulders", amb="hospital_corridor"),
    dict(to=50, reason="action change: Ahna kneels before Layaali", chars=["ahna", "layaali"], loc="corridor",
         visual="Ahna kneeling on the corridor floor in front of Layaali, weeping, head bowed, her hands clasped in plea; Layaali standing before her, stunned, with tears in her eyes",
         camera="medium wide, eye level", amb="hospital_corridor"),
    dict(to=52, reason="action change: Layaali forgives Ahna and lifts her up", chars=["layaali", "ahna"], loc="corridor",
         visual="Layaali bending to take Ahna's hands and raising her up from her knees, both women in tears, Layaali's face full of forgiveness; in the background two female nurses in white waiting by an open door",
         camera="medium two-shot", amb="hospital_corridor"),
    dict(to=54, reason="focus moves to Rafhaan watching Layaali", chars=["rafhaan"], loc="corridor",
         visual="Rafhaan standing alone by the corridor wall, gazing into the distance with deep, tender admiration and a faint smile, warm light from the far window on his face; far down the corridor, small and softly out of focus, a young woman in a black abaya and black hijab walking away",
         camera="medium close-up", amb="hospital_corridor"),
    dict(to=55, reason="time jump and action change: good news, mother and daughter embrace", chars=["layaali", "aminath", "doctor"], loc="corridor",
         visual="Layaali and her mother Aminath hugging each other tightly and weeping with relief and joy, the smiling doctor standing beside them having just given good news",
         camera="medium shot", amb="hospital_corridor"),
    dict(to=60, reason="characters change: Ahna comes out and the police arrive to take her", chars=["ahna", "rafhaan", "layaali"], loc="corridor",
         visual="Ahna, pale and exhausted yet calm, head slightly bowed, walking down the hospital corridor between two Maldivian police officers in plain dark-blue uniforms with no insignia or text, her hands hidden in her long sleeves; she glances back over her shoulder towards Rafhaan and Layaali, who watch from the foreground at a distance",
         camera="medium wide from behind Rafhaan and Layaali", amb="hospital_corridor", sens="other",
         safe="arrest shown as officers walking beside her; handcuffs not shown"),
    dict(to=63, reason="time and place change: sunset outside the hospital", chars=["rafhaan", "layaali"], loc="sunset",
         visual="Rafhaan and Layaali standing outside the hospital facing each other at a respectful distance under a golden sunset sky, Rafhaan speaking warmly, Layaali listening in surprise",
         camera="medium wide two-shot", amb="city_day", transition="black"),
    dict(to=66, reason="emotional turning point: she calls him by his name, shy smile", chars=["layaali", "rafhaan"], loc="sunset",
         visual="close-up of Layaali lowering her head shyly with a soft smile, eyes looking down, golden sunset light on her face; Rafhaan softly out of focus at a respectful distance behind her, smiling",
         camera="close-up", amb="city_day", sens="romance",
         safe="he takes her hand in the narration (not married yet): no touch shown, only her shy smile at a distance"),
    dict(to=69, reason="scene and character change: Zaahir plots revenge", chars=["zaahir"], loc="zaahir",
         visual="Ahmed Zaahir alone in his dark study at night, standing by the tall window, a smartphone lowered in his hand, his face hard and vengeful, half lit by cold blue light",
         camera="medium shot, low angle", amb="office_night", transition="black"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Rafhaan went and picked up the envelope. There was money inside it. And he read the note that lay with it.",
   [("paper_shuffle", "ނެގިއެވެ", -20)])
sh(2, "As soon as he read the note, a knot began to turn in Rafhaan's mind. Those letters were very familiar to him. It was not Layaali's handwriting.")
sh(3, "The note had been typed on a computer, but from the way the address on the outside of the envelope was written, Rafhaan realised something.")
sh(4, "It was writing almost identical to the handwriting of Ahna's secretary. At that moment Qaasim, lying on his sick bed, tried to get up. 'Sir...'",
   [("cloth_rustle", "ތެދުވަން", -22)])
sh(5, "'Don't make my daughter a criminal. She would never steal, ever. Even if I die, so be it... don't destroy my daughter's honour.' Weeping, Qaasim began to cough hard.",
   [("breath_heavy", "ކެއްސާން", -20)], hum=True)
sh(6, "Through the coughing, blood began to come from his mouth. 'Qaasim! Dad!' Layaali and Aminath cried out and rushed to Qaasim's side.",
   [("gasp", "ހަޅޭއްލަވައިގަންނަމުން", -18)], hum=True)
sh(7, "Qaasim's condition became very bad. His eyes closed. Rafhaan was alarmed. Every doubt that had formed in his heart vanished at once.",
   [("heartbeat", "ހާސްވިއެވެ", -18)], hum=True)
sh(8, "Seeing the state of this poor family, his heart softened. 'Layaali! Hurry! We have to take your father to hospital. Get him into my car!'")
sh(9, "Rafhaan at once stepped forward and lifted Qaasim in his own arms. They all got into the car and set off towards ADK Hospital.",
   [("car_door", "ކާރަށް", -18), ("car_drive_off", "މިސްރާބު", -20)])
sh(10, "On the way Layaali sat crying with her father's head resting on her lap. Rafhaan, in the front seat, kept watching Layaali in the mirror.",
   [("sob_breath", "ރޮވިފައެވެ", -24)], hum=True)
sh(11, "In this sorrowful moment the love in his heart for Layaali grew stronger. 'I will never let anyone hurt you, Layaali.")
sh(12, "I will prove that Ahna is behind all of this,' Rafhaan kept saying to himself.")
sh(13, "As soon as they reached the hospital Qaasim was taken straight into the emergency room for treatment. The doctors said his lung disease had become very serious and that an operation had to be done right away.",
   [("door_open", "ރޫމަށް", -20)])
sh(14, "And that it would need a large sum of money. Layaali and Aminath stood outside, at a loss.")
sh(15, "At that moment Rafhaan went to the counter and paid all the costs of the operation with his own card. When Layaali learned of it, she came over to Rafhaan.",
   [("footsteps_pavement", "ކައިރިއަށް", -24)])
sh(16, "'Sir... why did you do this? I'm someone accused of stealing the company's money.")
sh(17, "Why did you give me such great help, sir?' Layaali said. Rafhaan looked straight into Layaali's eyes. 'Layaali...")
sh(18, "I know you are not a thief. I will find out who set that money trap.")
sh(19, "Saving your father's life is the most important thing right now. What I did, I didn't do as a boss...")
sh(20, "I did it out of humanity. And for something else too...' Rafhaan deliberately left the rest unsaid. Layaali's heart began to pound.",
   [("heartbeat", "ތެޅިގަތެވެ", -18)], hum=True)
sh(21, "Rafhaan's words woke the feelings hidden in her heart. But just then, at the sound of high heels in the hospital corridor, they both looked round.",
   [("footsteps_pavement", "ބޫޓެއްގެ", -14)])
sh(22, "It was Ahna. Behind her was her 'devil' friend Zoya too. Ahna's face showed displeasure and a look of victory. 'Rafhaan!")
sh(23, "What are you doing at the hospital, leaving the office at a time like this, chasing after this thieving girl?' Ahna demanded harshly.")
sh(24, "'The police are at Layaali's house right now. They found the money in her house. Now all the evidence is complete!'")
sh(25, "Rafhaan looked at Ahna with a cold smile. 'Ahna... your plan was very perfect. But you forgot one thing.")
sh(26, "That behind everything there is evidence no one can see.' Rafhaan took out his phone and showed it to Ahna.")
sh(27, "On the phone's screen were the office's secret logs, and a message sent by Aasim: IP-address evidence that the letters sent to the bank were prepared on Ahna's own laptop.")
sh(28, "The colour instantly drained from Ahna's face. Zoya too stepped back in fear. The waves raised in the sea of jealousy were now heading straight for Ahna.",
   [("gasp", "ޖެހިލިއެވެ", -20)], hum=True)
sh(29, "These were things Ahna had never imagined. When you do something you have to think of every side — Ahna and her friends had forgotten that.")
sh(30, "The unease in the cold hospital corridor doubled with the evidence showing on Rafhaan's phone screen.")
sh(31, "Ahna's eyes widened and her face went completely pale. Zoya, standing behind her, took a step back in fear.",
   [("footsteps_pavement", "ފިޔަވަޅެއް", -24)])
sh(32, "Rafhaan's sharp gaze was fixed straight on Ahna's face. In that look was reproach and disgust. 'What happened, Ahna? Lost for words?'")
sh(33, "There was coldness in Rafhaan's voice. 'Did you think that by altering documents through the computer systems you could hide the real IP address?")
sh(34, "It is now proven that you forged Layaali's signature and sent letters to the bank from your own laptop.")
sh(35, "And I have found out that you sent the money to Layaali's house through your secretary.' 'Rafhaan... this... this is all lies!")
sh(36, "These are stories you are making up to save that poor girl!' Ahna shouted defiantly.")
sh(37, "But she could not hide the tremble in her voice. 'Don't try to deceive anyone any more, Ahna. All this evidence has already been sent to the police.")
sh(38, "The police team that went to Layaali's house is on its way here now to arrest you,' Rafhaan said firmly. Zoya shrieked in fear. 'Ahna!",
   [("gasp", "ހަޅޭއްލަވައިގަތެވެ", -18)])
sh(39, "I told you not to do this! Don't drag me into this!' Zoya instantly let go of Ahna and fled from there almost at a run.",
   [("footsteps_pavement", "ދުވެފައި", -18)])
sh(40, "Layaali and her mother Aminath stood amazed and speechless. Layaali had been saved from the dark pit of injustice.")
sh(41, "Tears of gratitude to Allah flowed from her eyes. At that moment the operation theatre door opened. The senior doctor came out and took the mask off his face.",
   [("door_open", "ހުޅުވުނެވެ", -16)], hum=True)
sh(42, "His face showed worry. 'Doctor! How is my father?' Layaali ran up and stopped in front of the doctor.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(43, "'The operation was successful. But... the patient's condition is still very critical.' The doctor took a deep breath.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -18)])
sh(44, "'The patient needs a special blood group. O-negative blood. Right now the hospital blood bank has none of that group.")
sh(45, "We must find blood as soon as possible. Otherwise his life may be in danger.' 'O-negative?' Layaali's and Aminath's throats tightened.",
   [("gasp", "ކަރުއެލުނެވެ", -20)])
sh(46, "It is a very rare blood group. No one in their family has that blood. 'My blood is O-negative.'")
sh(47, "At the voice suddenly behind them, everyone looked that way. It was Ahna. Tears were flowing from her eyes.", hum=True)
sh(48, "Her pride and anger seemed to have vanished at once. 'I... I'll give the blood. Rafhaan, Layaali... forgive me.",
   [("sob_breath", "މާފުކުރޭ", -24)], hum=True)
sh(49, "I changed so much in my jealousy.' Weeping, Ahna sank to her knees in front of Layaali.",
   [("cloth_rustle", "ތިރިވިއެވެ", -20)], hum=True)
sh(50, "The enemy who had tried to destroy Layaali's life had today become the only hope of saving her father's life.")
sh(51, "Layaali at once stepped forward, took Ahna by the hand and lifted her up. 'Ahna... come quickly, let's give the blood. There is no grudge in my heart.")
sh(52, "Save my father,' Layaali said, crying. The two nurses there took Ahna into the blood-collection room.",
   [("sob_breath", "ރޮމުން", -24), ("door_close", "ވަނެވެ", -22)])
sh(53, "Rafhaan stood watching Layaali. Seeing her goodness of heart and the noble grace of forgiveness, the love in Rafhaan's heart for her grew many times over.", hum=True)
sh(54, "She was not just a beautiful girl. She had a heart as pure as an angel's. About an hour later the doctor came out and gave the happy news.")
sh(55, "With the blood, Qaasim's condition had begun to improve. Aminath and Layaali held each other tightly and wept.",
   [("sob_breath", "ރޮއިގަތެވެ", -24)], hum=True)
sh(56, "When Ahna came out, her face showed exhaustion. But her heart had found a great peace.",
   [("door_open", "ނިކުތްއިރު", -22)])
sh(57, "Just then two police officers were seen coming down the hospital corridor. They had come to arrest Ahna.",
   [("footsteps_pavement", "އަންނާތީ", -18)])
sh(58, "'Ahna, you are now under arrest on charges of forgery with company money and trying to frame someone,' the officer said. Ahna bowed her head.",
   [("sigh", "ބޯޖަހާލިއެވެ", -22)])
sh(59, "She did not try to run. She looked towards Rafhaan and Layaali. 'Rafhaan... I will accept the punishment for the wrong I did.")
sh(60, "Layaali, I pray your father recovers quickly.' With handcuffs on her hands, Ahna walked away with the police.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(61, "Outside the hospital, as the sun was setting, the sky was a beautiful gold. Rafhaan moved closer to Layaali. 'Layaali...")
sh(62, "After all these storms, what I want is to give you peace. Your job has now been given back to you. And...")
sh(63, "I want to hand Ahna's post — head of the finance department — to you, Layaali.' 'Sir... I...' Layaali was astonished.")
sh(64, "'Not sir. Layaali.' Rafhaan gently took Layaali's hand. 'Call me by my name.")
sh(65, "A special place in my heart has also been given to you now.' 'Rafhaan,' Layaali called softly, shyly.", hum=True)
sh(66, "Layaali lowered her head shyly. But her smile gave Rafhaan his answer.")
sh(67, "But they did not know that another danger lay behind this happy moment.",
   [("heartbeat", "ނުރައްކަލެއް", -18)], hum=True)
sh(68, "Ahna's father Ahmed Zaahir, on hearing the news of his daughter's arrest, has already begun planning to bankrupt Rafhaan's entire company.", hum=True)
sh(69, "Rafhaan does not yet know how dangerous Ahmed Zaahir is.",
   [("heartbeat", "ނުރައްކާތެރިކަން", -18)], hum=True)
SHOTS = S

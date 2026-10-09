"""Beat/shot plan for Tedhuveriloabi episode 434 (used by plan_beats.py)."""

HOUSE = ("the tiny plain sitting room of Layaali's family's old small house in a narrow Malé lane, a simple single bed "
         "against a pale painted wall, a plastic chair, a small wooden table with a steel water jug, a wooden louvered "
         "window, a slow ceiling fan")
FLOOR = ("the open-plan finance floor of a modern glass high-rise office in Malé, rows of white desks with computer "
         "monitors turned away from the viewer, glass walls, a wide window view of the city and the sea")
CABIN = ("Rafhaan's luxurious glass-walled CEO cabin high in a modern glass office tower in Malé, a large dark walnut "
         "desk with a closed laptop and a few folders, a high-backed black leather chair, floor-to-ceiling windows "
         "with a view over the city rooftops and the sea")

LOC = {
    "home_evening": HOUSE + ", in the evening, lit by one warm bulb",
    "home_day": HOUSE + ", in the afternoon, daylight through the louvers",
    "mansion": ("the spacious living room of a large modern mansion in Malé at night, cream marble floor, a sweeping "
                "staircase with a glass railing, plush beige sofas, tall glass windows with the city lights outside"),
    "rafhaan_room": ("a large modern room in a mansion at night, a tall glass balcony door with sheer curtains "
                     "looking out over the night lights of Malé and the dark sea, a leather armchair, soft lamp light"),
    "office_morning": FLOOR + ", in the morning",
    "desk_detail": "a close view of a white office desk top on a finance floor, a thick grey file folder",
    "office_afternoon": FLOOR + ", in the late afternoon",
    "cabin": CABIN + ", by day",
    "corridor": ("a quiet glass-walled office corridor outside a CEO cabin in a modern high-rise, polished grey floor, "
                 "potted plants, city view through the glass"),
    "cafe": ("a posh modern café in Malé, deep velvet armchairs, a white marble table with two cups of coffee and a "
             "small dessert plate, warm brass pendant lights, a large window"),
    "office_night": CABIN + ", at night, the city lights glittering through the dark windows",
}
MOOD = {
    "home_evening": "evening, warm low tungsten light, soft shadows, tender but worried",
    "home_day": "afternoon, pale dusty daylight through the louvers, heavy and sorrowful",
    "mansion": "night, cool blue window light mixed with warm lamp glow, tense and serious",
    "rafhaan_room": "night, deep dusk-blue city glow and one warm lamp, lonely and torn",
    "office_morning": "morning, flat cool light, an unusual gloomy hush",
    "desk_detail": "secretive, low side light, ominous",
    "office_afternoon": "late afternoon, golden amber light through the glass, rising tension",
    "cabin": "daylight, cool glass reflections, formal and tense",
    "corridor": "daylight, cool glass reflections, sly triumph",
    "cafe": "warm amber pendant light, plum and gold tones, gloating",
    "office_night": "night, a single warm desk lamp against dark-blue city lights, solitary and searching",
}

BEATS = [
    dict(to=1, reason="new episode opening (recap): Layaali's parents at home, worried about her", chars=["aminath", "qaasim"], loc="home_evening",
         visual="Aminath sitting on a plastic chair beside the simple bed where frail Qaasim lies propped up on a pillow, both looking towards the front door with uneasy, worried faces",
         camera="medium shot, eye level", amb="home_night"),
    dict(to=6, reason="characters change: Layaali comes home tired and sits beside her father", chars=["layaali", "qaasim", "aminath"], loc="home_evening",
         visual="Layaali, tired but smiling softly, sitting on the edge of the simple bed beside her frail father Qaasim who lies propped up on a pillow; Aminath standing beside them with a kind face, holding a small steel plate of rice; Layaali's eyes are faraway and thoughtful",
         camera="medium wide, eye level", amb="home_night"),
    dict(to=9, reason="scene change: the mansion, Khadeeja waiting for Rafhaan", chars=["khadeeja", "rafhaan"], loc="mansion",
         visual="Khadeeja sitting upright on a plush sofa, speaking with a serious face and one hand raised; Rafhaan standing a few steps away just home from work, his face showing quiet annoyance",
         camera="medium wide two-shot", amb="mansion_night", transition="black"),
    dict(to=13, reason="emotional turning point: Rafhaan refuses the marriage, Khadeeja hardens", chars=["rafhaan", "khadeeja"], loc="mansion",
         visual="exactly two people: Rafhaan alone in the foreground, standing, turned towards the viewer with a firm, resolute expression; a few steps behind him the single figure of Khadeeja standing by the sofa, her face hard and uneasy; nobody else in the room",
         camera="medium close-up, slightly low angle", amb="mansion_night"),
    dict(to=15, reason="scene change: Rafhaan alone in his room, torn between company and love", chars=["rafhaan"], loc="rafhaan_room",
         visual="Rafhaan standing alone at the tall glass balcony door, seen in three-quarter profile, one hand resting on the glass, looking out over the night city lights, tie loosened, thoughtful and torn",
         camera="medium shot from inside the room", amb="room_night"),
    dict(to=18, reason="time jump and scene change: next day, Ahna hands Layaali the budget file", chars=["ahna", "layaali"], loc="office_morning",
         visual="Ahna standing beside Layaali's desk, holding out a thick grey file folder towards her with a sweet fake smile and a dangerous glint in her eyes; Layaali seated at the desk, reaching up to take it, polite and unsuspecting",
         camera="medium two-shot, eye level", amb="office_day", transition="black"),
    dict(to=19, reason="detail image: the secret theft of the cheques from the file", loc="desk_detail",
         visual="close-up of a woman's hands in black sleeves with ornate gold-embroidered cuffs secretly sliding a few blank cheque slips out of a thick grey file folder, the papers completely blank, no people's faces, low side light",
         camera="extreme close-up", amb="office_quiet"),
    dict(to=20, reason="time change: late afternoon, Layaali absorbed in her work", chars=["layaali"], loc="office_afternoon",
         visual="Layaali sitting alone at her desk, absorbed in work, leaning over open blank budget sheets with a pen, a calculator beside her, the golden late-afternoon light falling across her desk",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=23, reason="characters/action change: Ahna rushes to stop Rafhaan with the news", chars=["ahna", "rafhaan"], loc="office_afternoon",
         visual="in the open-plan office Ahna standing an arm's length in front of Rafhaan blocking his way, a clear gap between them, no touching, her face put on as anxious and alarmed, holding a grey file folder against her chest with both hands; Rafhaan stopped mid-step, serious, his eyes turning past her towards a desk in the background",
         camera="medium two-shot", amb="office_day"),
    dict(to=25, reason="focus moves to Layaali: she looks up in fear", chars=["layaali"], loc="office_afternoon",
         visual="Layaali at her desk raising her head, frightened, eyes wide, hands frozen on the papers, her shoulders tense; soft amber light, the office blurred behind her",
         camera="close-up", amb="office_quiet", sens="other",
         safe="the narration's metaphor of a 'noose of envy around her neck' is shown only as her frightened face"),
    dict(to=28, reason="framing change: the whole office falls silent and stares", chars=["rafhaan", "ahna", "layaali"], loc="office_afternoon",
         visual="wide view of the open-plan office frozen in silence: background office staff standing still at their desks staring; in the middle Rafhaan and Ahna standing facing each other, and Layaali sitting at her desk to one side, all eyes on them",
         camera="wide shot, slightly high angle", amb="office_quiet"),
    dict(to=30, reason="emotional turning point: Rafhaan demands proof", chars=["rafhaan"], loc="office_afternoon",
         visual="Rafhaan standing in the office with a hard, stern face, looking straight at someone off-frame, jaw set, eyes questioning, golden light on one side of his face",
         camera="medium close-up", amb="office_quiet"),
    dict(to=33, reason="focus moves to Ahna presenting her 'proof'", chars=["ahna"], loc="office_afternoon",
         visual="Ahna standing in the office holding up an open grey file folder, turning towards someone off-frame with a cold, thin smile and accusing eyes",
         camera="medium close-up", amb="office_quiet"),
    dict(to=36, reason="action change: Layaali stands up trembling, in tears", chars=["layaali"], loc="office_afternoon",
         visual="Layaali standing up behind her desk, her chair pushed back, trembling, both hands pressed together at her chest, tears running down her cheeks, stammering in shock",
         camera="medium shot", amb="office_quiet"),
    dict(to=38, reason="back to Ahna's accusation (reuse)", reuse="beat_013", chars=["ahna"], loc="office_afternoon",
         visual="(reuse) Ahna accusing with the open file", amb="office_quiet"),
    dict(to=39, reason="back to Rafhaan as he takes control (reuse)", reuse="beat_012", chars=["rafhaan"], loc="office_afternoon",
         visual="(reuse) Rafhaan's stern face", amb="office_quiet"),
    dict(to=42, reason="scene change: inside Rafhaan's cabin", chars=["rafhaan", "layaali", "ahna"], loc="cabin",
         visual="Rafhaan seated in his high-backed chair behind the large desk, hands folded, looking up gravely; Layaali and Ahna standing apart in front of the desk, Layaali with her head bowed, Ahna with arms folded",
         camera="wide shot from the side of the desk", amb="office_quiet"),
    dict(to=46, reason="emotional turning point: Layaali swears her innocence in tears", chars=["layaali", "rafhaan"], loc="cabin",
         visual="Layaali in the foreground in tears, hands clasped, pleading; behind her at a respectful distance Rafhaan seated at his desk, his face pained and gentle, out of focus",
         camera="close-up over the desk", amb="office_quiet"),
    dict(to=48, reason="action change: Layaali leaves, Ahna smiles in victory", chars=["ahna", "layaali"], loc="cabin",
         visual="Ahna in the foreground inside the cabin with a smug victorious smile; behind her, through the glass wall, Layaali walking away with her head down, one hand at her face",
         camera="medium close-up", amb="office_quiet"),
    dict(to=50, reason="scene change: Ahna outside the cabin phones her friends", chars=["ahna"], loc="corridor",
         visual="Ahna walking along the glass corridor holding a phone to her ear, a triumphant sly smile, one eyebrow raised",
         camera="medium shot", amb="office_quiet"),
    dict(to=51, reason="characters change: Zoya and Raaya on the other end", chars=["zoya", "raaya"], loc="cafe",
         visual="Zoya and Raaya sitting together in velvet armchairs at a marble café table, Zoya laughing with a phone held to her ear, Raaya beside her with a cold satisfied smirk",
         camera="medium two-shot", amb="cafe"),
    dict(to=53, reason="back to Ahna on the phone (reuse)", reuse="beat_020", chars=["ahna"], loc="corridor",
         visual="(reuse) Ahna on the phone in the corridor", amb="office_quiet"),
    dict(to=55, reason="scene change: Layaali home, breaks down in front of her parents", chars=["layaali", "aminath", "qaasim"], loc="home_day",
         visual="Layaali sitting on the plastic chair weeping into her hands; Aminath standing beside her with one arm around her shoulders, alarmed; Qaasim sitting up on the bed, leaning towards them, worried",
         camera="medium wide", amb="home_day"),
    dict(to=59, reason="focus change: Qaasim weeps and coughs, Layaali holds his hand", chars=["qaasim", "layaali", "aminath"], loc="home_day",
         visual="frail Qaasim sitting up on the bed, tears on his cheeks, coughing into his fist; Layaali sitting on the edge of the bed holding his other hand in both of hers with a brave but sad face; Aminath behind them, worried",
         camera="medium close-up", amb="home_day", sens="other",
         safe="his illness shown only as coughing into a fist, nothing else"),
    dict(to=61, reason="time jump and scene change: that night Rafhaan alone checks the bank reports", chars=["rafhaan"], loc="office_night",
         visual="Rafhaan sitting alone at his desk late at night under a single warm desk lamp, studying blank printed bank report pages spread out before him, a pen in hand, his face suspicious and focused",
         camera="medium shot, eye level", amb="office_night", transition="black"),
    dict(to=65, reason="time jump and characters change: next day Zaahir arrives with Khadeeja", chars=["zaahir", "khadeeja", "rafhaan"], loc="cabin",
         visual="Ahmed Zaahir standing in Rafhaan's cabin, pointing a finger with a harsh cold face; Khadeeja beside him with a stern face; Rafhaan standing behind his desk facing them, tense",
         camera="medium wide, eye level", amb="office_day", transition="black"),
    dict(to=69, reason="emotional turning point: cornered, Rafhaan lowers his head", chars=["rafhaan", "khadeeja", "zaahir"], loc="cabin",
         visual="Rafhaan in the foreground with his head lowered, eyes downcast, trapped and troubled; behind him slightly out of focus Khadeeja and Zaahir watching him expectantly",
         camera="close-up, slightly high angle", amb="office_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "'But lately there's some kind of unease on her face. I wonder whether there's some problem at the office.'")
sh(2, "Just then Layaali came into the house. Tiredness showed on her face. 'Mum... Dad...' Layaali said with a smile.",
   [("door_open", "ވަނީ", -20)])
sh(3, "'There was a lot of work at the office today, so I'm late.' 'Daughter, have you eaten? I've cooked rice,' Aminath said.")
sh(4, "Layaali nodded and sat down beside her father. In her heart the events at the office kept turning over.")
sh(5, "Rafhaan's words and Ahna's resentful looks kept appearing before her eyes.")
sh(6, "Her heart told her the days ahead would not be ordinary days. Meanwhile, at Rafhaan's house, his mother Khadeeja was waiting for him.")
sh(7, "As soon as Rafhaan came in, Khadeeja began to talk to him. 'Rafhaan, Ahna's mother called me today,' Khadeeja said in a serious tone.",
   [("door_open", "ވަނުމާއެކު", -20)])
sh(8, "'They want to settle your marriage as soon as possible. You know Ahna's father is the company's biggest shareholder, don't you?")
sh(9, "Delaying this marriage is not good for business.' Annoyance showed on Rafhaan's face.")
sh(10, "'Mum, I don't want to build a life for the sake of business profit. Ahna is not a good girl.")
sh(11, "Her heart is full of arrogance and pride. I want a humble, kind partner,' Rafhaan said firmly.")
sh(12, "Even then, Layaali's simple face kept turning in his mind. 'Rafhaan! Don't ruin the business by being carried away by feelings,' Khadeeja said, hardening.")
sh(13, "'If we turn against Ahna's family, our company could go bankrupt.' Unease showed on Khadeeja's face.")
sh(14, "Without a word Rafhaan went into his room. A great challenge lay before him. On one side, the company he had built with his hard work.",
   [("door_close", "ކޮޓަރިއަށް", -18)])
sh(15, "On the other, the pure love blossoming in his heart. The next day, when the office opened, an unusual gloom hung in the air.", hum=True)
sh(16, "Ahna came to the office with a new plan. She went to Layaali's desk and held out a big file. 'Layaali, these are the budget papers for the new project.",
   [("paper_shuffle", "ދިއްކޮށްލިއެވެ", -18)])
sh(17, "All the calculations in it must be finished before this afternoon. And the cheques for the money set aside for the budget are in it too.")
sh(18, "Be very careful,' Ahna said. A dangerous glint showed in her eyes. Layaali took the file.")
sh(19, "What she did not know was that Ahna had secretly taken some important documents and cheques out of that file.",
   [("paper_shuffle", "ސިއްރުން", -22)])
sh(20, "It was the first step of the plan Ahna and her friends had made to frame Layaali. As the afternoon wore on, Layaali sat lost in her work.",
   [("keyboard_typing", "މަސައްކަތުގެ", -24)])
sh(21, "Just then Rafhaan came out of his cabin and walked towards Layaali. But he had to stop when Ahna came almost running and stood in front of him.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22), ("footsteps_pavement", "ދުވެފައި", -20)])
sh(22, "'Rafhaan! There's a big problem. A large sum of money is missing from the new project's budget.")
sh(23, "And that file was given to Layaali,' Ahna said with a worried face. Seriousness filled Rafhaan's eyes. He looked towards Layaali.")
sh(24, "When Layaali raised her head and looked, her heart was trembling with fear. The noose of envy had been placed around her neck.",
   [("heartbeat", "ތެޅެމުންދިޔައެވެ", -16)], hum=True)
sh(25, "The fire of envy first burns to ashes the heart of the one who lit it. The success of deceit is only a passing shadow.", hum=True)
sh(26, "Rafhaan made no reply to what Ahna said. A frightening silence fell over the office's big hall.")
sh(27, "The staff stopped moving and talking at once. Every gaze was fixed on Rafhaan and Ahna, and on Layaali sitting at her desk.")
sh(28, "What came out of Ahna's mouth was not something anyone in the office could easily believe.")
sh(29, "Everyone knew Layaali was not a girl who would steal. But Ahna had come very well prepared. 'Ahna! That's a very serious claim.")
sh(30, "Where is your proof?' Rafhaan's voice was hard. His heart told him Layaali was not guilty.")
sh(31, "But as the boss he had to decide things fairly. 'Rafhaan, I won't say anything without proof,' Ahna said with a cold smile.")
sh(32, "'The file with the large sum withdrawn from the bank specially for the new project's budget — I handed it to Layaali this morning.")
sh(33, "Of the cheques in that file, two have now been cashed. And that money hasn't gone into any company account. Layaali, where is that money?'")
sh(34, "Ahna turned to Layaali and questioned her harshly. Layaali suddenly rose from her chair. Her whole body was trembling with fear.",
   [("cloth_rustle", "ތެދުވިއެވެ", -20), ("heartbeat", "ތެޅެމުންނެވެ", -18)], hum=True)
sh(35, "A girl who had never wrongfully laid a hand on anyone's belongings — faced with such a huge accusation, her tongue was tied. 'I... I...")
sh(36, "I don't know. There were no cheques in the file madam gave me. Only budget sheets.' Tears rolled from Layaali's eyes.",
   [("sob_breath", "ހިލިލިއެވެ", -24)], hum=True)
sh(37, "'Don't lie, Layaali!' Ahna shouted. 'My secretary was there too when I handed you that file.")
sh(38, "And the bank's signature verification shows a signature almost exactly like yours.' Rafhaan took a deep breath.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -18)])
sh(39, "'Layaali and Ahna, both of you come to my cabin,' Rafhaan said. He did not want to shame Layaali any further by discussing this in front of the whole office.")
sh(40, "After they entered the cabin, Rafhaan sat in his chair and looked at the two of them. 'Layaali, I trust you.",
   [("door_close", "ވަނުމަށްފަހު", -20)])
sh(41, "But we have to look into this matter. I will get the details of what Ahna says from the bank.")
sh(42, "Until then, Layaali, you will have to be on suspension.' 'Suspension?' Layaali's heart broke into pieces.",
   [("heartbeat", "ފުނޑުފުނޑުވިއެވެ", -16)], hum=True)
sh(43, "At a time when her father's treatment needs money, losing her job would be the greatest sorrow for her family. 'Sir...")
sh(44, "I swear I didn't do such a thing,' Layaali said, crying. Rafhaan was deeply moved.",
   [("sob_breath", "ރޮމުން", -24)], hum=True)
sh(45, "He wanted to dry Layaali's tears and stand up in her defence. But the company's rules and his mother's pressure left him no choice.")
sh(46, "'Layaali. Go home and rest. I will investigate this myself,' Rafhaan said gently.")
sh(47, "Layaali walked out of the cabin crying. A smile of victory appeared on Ahna's face. She looked at Rafhaan and said,",
   [("door_close", "ނިކުމެގެން", -20), ("sob_breath", "ރޮމުން", -24)])
sh(48, "'Rafhaan, didn't I tell you it's not wise to trust poor people like that too much? When they see money they forget all their morals.'")
sh(49, "'Ahna! Not another word — get out,' Rafhaan said angrily. Ahna left the cabin and immediately called her friends Zoya and Raaya.",
   [("door_close", "ނިކުމެ", -18), ("phone_buzz", "ގުޅިއެވެ", -20)])
sh(50, "'The first part of our plan has worked,' Ahna said on the phone. 'That goody-goody is suspended now. Next is getting her thrown out of the office for good.'")
sh(51, "'What a great act, Ahna. Otherwise it would never have gone this easily,' Zoya laughed.")
sh(52, "'Next we have to change the bank records and show Rafhaan documents with Layaali's signature on them.")
sh(53, "I'll get help from inside the bank.' Layaali went home crying all the way along the street.",
   [("footsteps_pavement", "މަގުމަތިން", -24)])
sh(54, "As soon as she entered the house she burst into tears. Aminath and Qaasim came to her anxiously. 'Daughter! What happened? Why are you crying?'",
   [("door_open", "ވަދެވުމާއެކު", -18), ("sob_breath", "ރޮއިގަނެވުނެވެ", -22)], hum=True)
sh(55, "Aminath asked worriedly. Layaali told her mother and father everything that had happened at the office.")
sh(56, "Hearing it, tears began to fall from Qaasim's eyes. 'My daughter would never lay a hand on anything forbidden. What a terrible slander!",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(57, "O Allah, they are taking advantage of our helplessness,' Qaasim kept saying, weeping. Then he began to cough. 'Dad.",
   [("breath_heavy", "ކެއްސަން", -20)])
sh(58, "Don't worry any more. If I've done nothing wrong, Allah will show us a way,' Layaali said, holding her father's hand.")
sh(59, "But inside, her heart was weeping. If she lost her job, how would she pay for her father's medicine?", hum=True)
sh(60, "That night Rafhaan sat alone in the office going through the bank reports. He noticed the cheques had been cashed during office hours, at a time when Layaali never left the office.",
   [("page_turn", "ރިޕޯޓްތައް", -20)])
sh(61, "The suspicion that this was Ahna's plan grew in Rafhaan's heart. He decided to get the bank's CCTV footage himself.")
sh(62, "But the next day things took a completely different turn. Ahna's father, Ahmed Zaahir, came to Rafhaan's office.",
   [("door_open", "އައެވެ", -20)])
sh(63, "He came bringing Rafhaan's mother Khadeeja with him. 'Rafhaan!' Zaahir said harshly. 'Ahna told me about an ordinary girl in your office stealing the company's money.")
sh(64, "Why are you still delaying sending her case to the police? I don't want to keep my investments in a place like this.")
sh(65, "I want the two of you married as soon as possible and my shares transferred to Ahna's name.'")
sh(66, "Khadeeja pressed him too. 'Rafhaan, agree to the marriage. Otherwise this company can't be saved.' Rafhaan lowered his head.",
   [("sigh", "އިސްދަށަށް", -20)])
sh(67, "Traps had closed in around him. And how would he save Layaali? Caught between two families, how would he win his own heart's freedom?",
   [("heartbeat", "މަޅިތައް", -18)], hum=True)
sh(68, "Everyone was trying to save the business, and to bring Ahna into his life to keep it that way.", hum=True)
sh(69, "Ahna, with all her beauty and pride, was not Rafhaan's ideal.")
SHOTS = S

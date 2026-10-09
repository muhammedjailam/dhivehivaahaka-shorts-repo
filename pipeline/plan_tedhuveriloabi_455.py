"""Beat/shot plan for Tedhuveriloabi episode 455 (used by plan_beats.py)."""

LOC = {
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin high in a modern glass office tower in Malé, a large dark walnut desk with a glass top, a black leather chair, floor-to-ceiling windows over the city rooftops and the turquoise sea, late afternoon",
    "ahna_cabin": "Ahna's elegant glass-walled office on the finance floor of a modern Malé office tower, a white lacquered desk, a burgundy velvet chair, a vase of dark red roses, glass walls with the open-plan floor blurred behind, late afternoon",
    "layaali_room": "Layaali's small plain bedroom in an old house in a narrow Malé lane in the evening, a simple single bed with a plain cotton sheet, a small wooden window with faded curtains, a worn wooden door, a woven prayer mat on the tiled floor, one small warm lamp",
    "cabin_morning": "Rafhaan's glass-walled CEO cabin in a modern Malé office tower in the morning, a large dark walnut desk with a glass top, floor-to-ceiling windows with bright morning light over the city and the sea",
    "office_floor": "the bright open-plan finance floor of a modern Malé office tower in the morning, glass walls, a long corridor beside the windows, city and sea view, blurred empty desks behind",
    "car": "the back seat of a sleek black luxury car moving slowly through a narrow Malé lane in the late morning, cream leather seats, tinted windows showing old low houses, motorbikes and coconut palms passing outside",
    "lane": "a narrow sunny Malé lane in the late morning, old low houses with weathered pale-coloured coral-stone walls, a small plain old house with a worn green wooden door, a sleek black luxury car parked close to the wall, a potted plant by the step",
    "sitting_room": "the tiny plain sitting room of a small old Malé house, whitewashed walls with peeling paint, a simple single bed against the wall with a faded blanket, a plastic chair, a small wooden table in the corner, a faded floral curtain hanging over an inner doorway, daylight through a small window",
}
MOOD = {
    "cabin": "late-afternoon golden light through the glass, long shadows, tense and oppressive",
    "ahna_cabin": "warm late-afternoon light, burgundy and gold tones, smug and scheming",
    "layaali_room": "evening, a single warm lamp, deep plum shadows, sorrowful and devout",
    "cabin_morning": "cool bright morning light, crisp blue tones, shock and disbelief",
    "office_floor": "cool morning light, glossy reflections, sly and conspiratorial",
    "car": "late-morning light flickering through the tinted windows, restless and anxious",
    "lane": "bright late-morning sun, soft shadows of palm fronds on the walls, humble and tense",
    "sitting_room": "soft daylight from a small window, muted faded colours, heavy and sorrowful",
}

BEATS = [
    dict(to=2, reason="new episode opening: Rafhaan in his cabin under pressure", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan standing beside his desk in front of the floor-to-ceiling window, one hand on the back of his leather chair, jaw tight, gazing out at the city with a troubled, burdened expression; the glass desk top calm and empty in the lower part of the frame",
         camera="medium shot, slightly low angle", amb="office_day"),
    dict(to=7, reason="characters change: Zaahir and Khadeeja confront Rafhaan", chars=["rafhaan", "zaahir", "khadeeja"], loc="cabin",
         visual="Zaahir and Khadeeja standing side by side in front of Rafhaan's desk, Zaahir stern and domineering with his hands on his hips, Khadeeja with a pleading, insistent face; Rafhaan standing behind the desk facing them, calm but firm, the city window glowing behind them",
         camera="medium wide three-shot, eye level", amb="office_day"),
    dict(to=9, reason="focus change: Khadeeja's outburst", chars=["khadeeja", "rafhaan"], loc="cabin",
         visual="Khadeeja in the foreground, one hand raised in an angry, displeased gesture, her face flushed and indignant; Rafhaan behind the desk out of focus, looking at his mother",
         camera="medium close-up on Khadeeja, shallow depth of field", amb="office_day"),
    dict(to=11, reason="Rafhaan answers his mother (reuse of the confrontation)", reuse="beat_002", chars=["rafhaan", "zaahir", "khadeeja"], loc="cabin",
         visual="(reuse) the three-shot confrontation in the cabin", amb="office_day"),
    dict(to=13, reason="action change: Zaahir's ultimatum, finger pointed at Rafhaan", chars=["zaahir", "rafhaan"], loc="cabin",
         visual="Zaahir leaning forward over the desk, pointing his index finger towards Rafhaan's face from an arm's length away (not touching), a cold mocking smile; Rafhaan standing upright, unflinching, his eyes hard",
         camera="medium two-shot from the side", amb="office_day", sens="other",
         safe="Zaahir's hand almost touching Rafhaan's chin shown as a pointing finger at a distance, no contact"),
    dict(to=15, reason="action change: alone, Rafhaan slams the desk", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan alone, leaning over his glass desk with both palms pressed flat on it, head bowed, shoulders tense with frustration, his smartphone lying beside his hand; the cabin's glass door closed behind him",
         camera="medium shot, slightly high angle", amb="office_day"),
    dict(to=21, reason="characters change: Aasim comes in and gets his instructions", chars=["rafhaan", "aasim"], loc="cabin",
         visual="Aasim standing at the side of Rafhaan's desk holding an open laptop (screen facing away from the viewer), looking at Rafhaan with concern; Rafhaan seated, leaning forward, explaining seriously with one hand open on the desk",
         camera="medium two-shot, eye level", amb="office_day"),
    dict(to=25, reason="scene change: Ahna plotting by phone in her cabin", chars=["ahna"], loc="ahna_cabin",
         visual="Ahna sitting at her white desk, typing on her smartphone held in both hands (screen facing away from the viewer, soft glow on her face), a sly self-satisfied smile, eyes narrowed with ambition",
         camera="medium close-up", amb="office_quiet"),
    dict(to=27, reason="scene change: Layaali praying at home", chars=["layaali"], loc="layaali_room",
         visual="Layaali sitting on a woven prayer mat on the floor of her small room, both hands raised in supplication (dua), eyes closed, tears on her cheeks, lit by a single warm lamp",
         camera="medium shot, eye level", amb="home_night", hum_note="emotional"),
    dict(to=29, reason="characters change: Aminath brings the envelope", chars=["aminath", "layaali"], loc="layaali_room",
         visual="Aminath standing in the open doorway holding out a small plain white envelope; Layaali still sitting on the prayer mat, turning towards her mother and wiping her tears with her fingers, puzzled",
         camera="medium wide, eye level", amb="home_night"),
    dict(to=31, reason="action change: the envelope is opened — money and a note", chars=["layaali"], loc="layaali_room",
         visual="Layaali sitting on the edge of her bed, holding an opened plain white envelope from which a thick bundle of banknotes shows, a small folded blank note in her other hand, her eyes wide with shock",
         camera="medium close-up", amb="home_night"),
    dict(to=34, reason="action change: Layaali refuses, Aminath pleads about the medicine", chars=["layaali", "aminath"], loc="layaali_room",
         visual="Layaali standing, having put the envelope down on the bed, one hand raised in refusal, frightened; Aminath beside her crying, holding an empty small medicine bottle, pleading",
         camera="medium two-shot", amb="home_night"),
    dict(to=36, reason="emotional turning point: torn between honour and her father's life", chars=["layaali"], loc="layaali_room",
         visual="Layaali standing alone by the window, looking down at the plain white envelope lying on a small wooden side table, her hands pressed together at her chest, torn and anguished, lamp light on one side of her face",
         camera="medium shot over the envelope", amb="home_night", hum_note="emotional peak"),
    dict(to=39, reason="time jump: next morning, the bank letter on Rafhaan's desk", chars=["rafhaan"], loc="cabin_morning",
         visual="Rafhaan seated at his desk holding blank document pages from an opened envelope, staring at them in disbelief, one hand at his temple as if his head is spinning",
         camera="medium close-up", amb="office_day", transition="black"),
    dict(to=42, reason="characters change: Ahna comes in with her accusations", chars=["ahna", "rafhaan"], loc="cabin_morning",
         visual="Ahna standing in front of the desk with a triumphant smug smile, one hand gesturing towards the papers lying on the desk; Rafhaan rising abruptly from his chair, his face hard and determined",
         camera="medium two-shot", amb="office_day"),
    dict(to=45, reason="action change: Ahna phones Zoya after Rafhaan leaves", chars=["ahna"], loc="office_floor",
         visual="Ahna standing by the glass wall of the office floor, smartphone held to her ear, watching something below with a cold scheming smile",
         camera="medium shot, from the side", amb="office_day"),
    dict(to=48, reason="scene change: Rafhaan driven through Malé's lanes", chars=["rafhaan"], loc="car",
         visual="Rafhaan sitting in the back seat of the car, a closed bank report folder on his lap, looking out of the window with a pained, conflicted face",
         camera="medium close-up from the opposite seat", amb="car_interior"),
    dict(to=51, reason="scene change: arrival at Baageechaage, Aminath opens the door", chars=["rafhaan", "aminath"], loc="lane",
         visual="Rafhaan standing at the worn green wooden door of the small old house; Aminath has just opened it and stands in the doorway, startled and frightened, her hand at her chest; the black car parked behind him",
         camera="medium wide, eye level", amb="city_day"),
    dict(to=53, reason="scene change: inside, Qaasim on his sickbed", chars=["qaasim", "rafhaan", "aminath"], loc="sitting_room",
         visual="Qaasim lying frail on the simple bed against the wall, propped on a pillow, a faded blanket over him, his face gaunt and ill; Rafhaan standing just inside the door looking at him with quiet compassion; Aminath beside the bed with trembling hands clasped",
         camera="medium wide, eye level", amb="home_day"),
    dict(to=56, reason="characters change: Layaali comes out and faces Rafhaan", chars=["layaali", "rafhaan"], loc="sitting_room",
         visual="Layaali standing at the inner doorway beside the faded floral curtain, stopped in surprise, her eyes red from crying; Rafhaan standing a respectful distance away across the room, serious, asking a question",
         camera="medium wide two-shot, eye level", amb="home_day", sens="intimacy",
         safe="unmarried pair kept at a respectful distance, no touch"),
    dict(to=58, reason="emotional turning point: Layaali admits the money came", chars=["layaali", "rafhaan"], loc="sitting_room",
         visual="Layaali with her head bowed, tears running down her cheeks, hands clasped in front of her; Rafhaan in the background, at a distance, his face stricken and hurt",
         camera="close-up on Layaali, Rafhaan soft in the background", amb="home_day", hum_note="emotional peak"),
    dict(to=61, reason="action change: Layaali pleads and points to the envelope", chars=["layaali", "rafhaan"], loc="sitting_room",
         visual="Layaali pleading with tearful eyes, pointing towards a small wooden table in the corner where a plain white envelope lies; Rafhaan standing at a respectful distance, his face sorrowful, turning to look at the table",
         camera="medium wide two-shot", amb="home_day", sens="intimacy",
         safe="no touch between the unmarried pair; distance and gaze only"),
    dict(to=62, reason="action change: Rafhaan picks up the envelope (cliffhanger)", chars=["rafhaan"], loc="sitting_room",
         visual="Rafhaan standing by the small wooden table in the corner, holding the plain white envelope with banknotes visible inside and a small folded blank note in his other hand, reading it with a frown",
         camera="medium close-up", amb="home_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Everyone is trying to save the business — and to bring Ahna into his life to keep it going.")
sh(2, "Ahna, with all her beauty and pride, is not Rafhaan's ideal. The smoke of unease that had formed in the office had completely poisoned Rafhaan's cabin.")
sh(3, "The harsh words and commanding tone of Ahna's father, Ahmed Zaahir, rang in Rafhaan's ears like a warning bell.")
sh(4, "The firmness and pleading on his mother Khadeeja's face were breaking Rafhaan's defensive shield to pieces.")
sh(5, "This is not just a business matter. It is a dangerous trap that could force him to sacrifice his whole life and the pure love his heart longs for.", hum=True)
sh(6, "'Zaahirbe... I will not do anything against company law,' Rafhaan said, his voice soft but firm.")
sh(7, "'I am looking into Layaali's case. When the bank's official reports come, if she is guilty, I will inform the proper authorities and have it investigated.")
sh(8, "Until then I don't want to talk about any marriage.' 'Rafhaan!' Khadeeja shouted, displeased.")
sh(9, "'Rafhaan knows very well this company can't go forward without Zaahir's help. Why are you talking so much in defence of that ordinary poor girl?'")
sh(10, "'Mum. I'm not defending anyone. When someone in a top position sees an employee's rights being harmed, they must act only after looking into it properly.")
sh(11, "That is what I am doing.' This time there was hardness in Rafhaan's voice too. Zaahir gave a strange laugh. 'Fine.")
sh(12, "I'll give you a three-day deadline, Rafhaan. If within those three days you don't agree to hand that girl to the police and marry Ahna, I will pull all my money out of this company.", hum=True)
sh(13, "Then you'll be out on the street.' Zaahir's hand came so close it almost touched Rafhaan's chin.", hum=True)
sh(14, "Having said that, Zaahir took Khadeeja and walked out of the cabin. Rafhaan struck the desk hard with both hands.",
   [("door_close", "ނިކުމެގެން", -18), ("soft_thud", "ޖެހިއެވެ", -14)])
sh(15, "His heart was full of unease. At once he picked up the phone and called Aasim, his most trusted friend and the company's IT head.")
sh(16, "'Aasim. Come to my cabin, quickly,' Rafhaan said. Within a minute Aasim walked into the cabin.",
   [("door_open", "ވަނެވެ", -18)])
sh(17, "Seeing the distress on Rafhaan's face, Aasim grew worried. 'What happened, boss?'")
sh(18, "'Aasim, I want the hidden camera footage from Ahna's cabin, and the logs of every change made through the office's main server in the last two days.")
sh(19, "Especially the time the files given to Layaali were uploaded to the system, and what was in them before that,' Rafhaan instructed.",
   [("keyboard_typing", "އަޕްލޯޑް", -22)])
sh(20, "'I'll look into it right now. I also think someone did this to frame Layaali. Layaali isn't that kind of girl,' Aasim said.")
sh(21, "'I know, Aasim. But what we need is solid proof,' Rafhaan said. Meanwhile Ahna sat in her cabin, messaging Zoya and Raaya.",
   [("phone_buzz", "މެސެޖް", -20)])
sh(22, "'My father has given Rafhaan a three-day deadline. Within these three days we must finish off Layaali's case completely.")
sh(23, "Zoya, arrange for those records to be sent from the bank,' Ahna wrote. 'Don't worry, Ahna. Tomorrow morning, with an official bank letter, the records bearing Layaali's signature will reach Rafhaan's hands.")
sh(24, "Then he'll have to hand Layaali to the police,' Zoya replied at once. Ahna put the phone down on the table and smiled.",
   [("phone_buzz", "ޖަވާބުދިނެވެ", -20)])
sh(25, "The dream she had been dreaming was coming true. The day she would become Rafhaan's wife was very near.")
sh(26, "At that moment Layaali was sitting on her prayer mat in the small room of her house. Tears flowed from her eyes without stopping.", hum=True)
sh(27, "Before Allah she prayed for her innocence to be proven, and for healing for her father lying on his sickbed. 'Layaali, my child...'")
sh(28, "Aminath opened the door of the room and came in. In her hand was a small envelope. 'What is this, Mum?' Layaali asked, wiping away her tears.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -18)])
sh(29, "'My child, someone just came from outside and gave me this envelope. They said to give it to Layaali.' Aminath handed the envelope to Layaali.")
sh(30, "Puzzled, Layaali opened the envelope. Inside was a lot of money — fifty thousand rufiyaa. And with it a small note.",
   [("paper_shuffle", "ހުޅުވާލިއެވެ", -20)])
sh(31, "On it was written: 'Layaali, this is help for your father's medical treatment. It is the reward for Layaali's honesty.'")
sh(32, "But there was no sender's name on it. 'Who sent this money?' Layaali was frightened. 'Mum, I won't lay a hand on this money.")
sh(33, "Someone may have done this to disgrace me even more.' 'But my child, your father's medicines ran out today.")
sh(34, "I don't have any money to buy medicine. Aasandha doesn't cover every medicine. There are some we have to buy,' Aminath said, weeping.",
   [("sob_breath", "ރޮމުން", -24)])
sh(35, "Layaali's heart shattered. On one side was her honour; on the other, her father's life. She stood at a crossroads, staring at the money.", hum=True)
sh(36, "That this was money secretly sent by Ahna and her friends to tighten the accusation of theft around her — Layaali")
sh(37, "did not know. The next morning, when Rafhaan came to the office, an official envelope from the bank lay on his desk. He tore it open.",
   [("paper_shuffle", "ހުޅުވައިލިއެވެ", -20)])
sh(38, "The documents inside showed that the signature on the cheques used to withdraw the money was Layaali's.", [("page_turn", "ލިޔެކިޔުންތަކުން", -22)])
sh(39, "The graphology report also said it was Layaali's signature. Rafhaan's head spun. 'No... this cannot be.",
   [("heartbeat", "އެނބުރުން", -18)], hum=True)
sh(40, "Layaali would never deceive me,' Rafhaan told himself. Just then Ahna walked into the cabin. 'You've seen it, Rafhaan? The proof is right there,' Ahna said.",
   [("door_open", "ވަނެވެ", -20)])
sh(41, "'Now the police should be sent to Layaali's house. From what I've heard, a large sum has just been spent on her father's treatment.")
sh(42, "Where did that money come from?' Rafhaan suddenly rose from his chair. 'I will go to Layaali's house myself.",
   [("cloth_rustle", "ތެދުވިއެވެ", -20)])
sh(43, "I want to hear the truth from her own mouth,' Rafhaan said firmly. As soon as Rafhaan left the office, Ahna called Zoya.",
   [("door_close", "ނުކުމެގެން", -20)])
sh(44, "'Zoya, Rafhaan is going to Layaali's house. Did the money get into that house like you said?' 'Yes. It was delivered last night.")
sh(45, "Rafhaan will find that money in that house. Then Layaali becomes a thief for good.' Zoya laughed menacingly.")
sh(46, "As Rafhaan drove into this great storm, there was no road in sight that could prove Layaali innocent.")
sh(47, "What will he decide when he enters Layaali's house and sees the truth? In the expensive car winding through Malé's narrow lanes, Rafhaan's heart was pounding.",
   [("heartbeat", "ތެޅެމުންދެއެވެ", -18)])
sh(48, "In his hand was the bank's official report. However many times he looked, the signature was Layaali's. Yet his heart would not believe it.",
   [("page_turn", "ބެލިޔަސް", -24)])
sh(49, "He could not see the evil of theft in Layaali's clear, innocent eyes. The car came to a stop at the door of Baageechaage, where Layaali's family lives.",
   [("car_approach", "މަޑުކޮށްލީ", -18)])
sh(50, "It was an ordinary little house. Rafhaan got out of the car and knocked on the front door. The door was opened by Layaali's mother, Aminath.",
   [("car_door", "ފައިބައިގެން", -16), ("knock", "ޓަކިޖަހާލިއެވެ", -12), ("door_open", "ހުޅުވާލީ", -18)])
sh(51, "When she saw Rafhaan, fear and worry crossed Aminath's face, for she knew he was the boss of the office. 'Sir... please come in.'")
sh(52, "Aminath's hands began to tremble with fear. When Rafhaan went inside, Layaali's father Qaasim was lying on a bed in the house's tiny sitting room.",
   [("footsteps_pavement", "ވަންއިރު", -26)])
sh(53, "Nothing but illness showed on his face. Layaali, coming out of her room, froze when she saw Rafhaan.")
sh(54, "Her eyes were red; they bore witness that she had been crying. 'Sir? Why have you come here...' Layaali's voice trembled. 'Layaali.")
sh(55, "I've only come to ask one question.' Rafhaan stepped forward. 'The bank reports show that it was Layaali who took that money.",
   [("footsteps_pavement", "ޖެހިލިއެވެ", -26)])
sh(56, "And according to what Ahna has learned, a large amount of money was brought to this house last night. Is that true?' Layaali lowered her head.")
sh(57, "Tears rolled from her eyes. She did not want to lie. 'Yes, sir... last night someone sent fifty thousand rufiyaa to this house. But that was...'",
   [("sob_breath", "އޮހޮރިގެން", -24)])
sh(58, "'Fifty thousand rufiyaa?' Rafhaan's heart ached terribly. With Layaali admitting it herself, it was as if all his hopes had shattered.",
   [("heartbeat", "ތަދުވިއެވެ", -18)], hum=True)
sh(59, "'Layaali... why did you do this? I trusted you so much. Will treating your father with money stolen from the company ever be blessed?'")
sh(60, "There was grief in Rafhaan's voice. 'No, sir! Please listen!' Layaali pleaded before him. 'I don't know who sent that money.", hum=True)
sh(61, "It was left in an envelope. I haven't even touched it. It's right there on the table!' Layaali pointed to the table in the corner.")
sh(62, "Rafhaan went over and picked up the envelope. The money was inside. And he read the note that came with it.",
   [("paper_shuffle", "ނެގިއެވެ", -20)])
SHOTS = S

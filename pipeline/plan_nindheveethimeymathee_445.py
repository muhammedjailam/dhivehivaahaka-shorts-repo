"""Beat/shot plan for Nindheveethimeymathee episode 445 (used by plan_beats.py).
PAST timeline (~7 years before SCHOOL). Vietnam hotel morning after Haizum's "one mistake" (no woman ever in the room,
only a closed inner door); two months later in Male: pregnant Sana reads Shifa's message, collapses (shown as slumped
sitting against the sofa), loses the baby (never shown) and turns away from Haizum in hospital.
Haizum always fully dressed; no forehead kisses or embraces between Haizum and Sana."""

HZ = "Haizum, younger, about 38, beard fully black"
HZ_HOTEL = f"{HZ}, dressed casually for the morning in a plain charcoal-grey crew-neck short-sleeved t-shirt and long dark trousers (no suit, no jacket, no white shirt), hair a little messy from sleep"
HZ_HOME = f"{HZ}, in his white office shirt with sleeves rolled to the forearm and dark-navy trousers, no jacket"
SANA_P = "Sana, seven months pregnant, in a loose long-sleeved ankle-length sage-green dress and her ivory hijab fully covering her hair and neck"
SANA_H = "Sana in a loose long-sleeved pale hospital gown with a soft ivory hijab fully covering her hair and neck"
KIDS = "little Laira (12) in her pink dress and dove-grey hijab and little Lail (10) in his striped blue-and-white t-shirt"

HOTEL = ("a modern high-rise hotel room in Ho Chi Minh City, Vietnam: cream walls, a beige carpet, a grey two-seat sofa "
         "with a low glass coffee table, a writing desk with a lamp, a tall window and a glass sliding door to a small "
         "balcony with the dense city skyline beyond, a plain white closed inner door near the entrance")
HOME = ("the open-plan living and dining area of the family's spacious modern apartment in Male, Maldives: a wooden dining "
        "table with school exercise books and pencil cases, a cream sofa with cushions on a soft grey carpet, a corridor "
        "leading to the inner rooms, warm pendant lamps, a large window with the night lights of Male beyond")
HOSP_ROOM = ("a private hospital room in Male: an adjustable hospital cot with crisp white sheets and the backrest raised high, "
             "a padded visitor chair beside it, a small bedside cabinet with a glass of water, an IV stand on wheels in the "
             "background, a window with half-closed blinds")

LOC = {
    "hotel": HOTEL,
    "office": "Haizum's company office in Male: a large dark wooden desk with a closed laptop, a leather chair, a floor-to-ceiling window overlooking the lit buildings of Male and the harbour",
    "home": HOME,
    "home_shock": HOME,
    "landing": "the bright corridor of the apartment building in Male just outside the family's front door: the apartment door standing wide open spilling warm light, a lift with brushed-steel doors and a small call panel with plain round buttons, a tiled floor",
    "ot_corridor": "a hospital corridor in Male outside the operating theatre: closed double doors with frosted round windows, a row of blue plastic waiting chairs against pale green walls, a polished floor",
    "ward_corridor": "a quiet hospital ward corridor in Male at night: the open door of a private room, pale walls, a handrail, a polished floor reflecting the lights",
    "hosp_night": HOSP_ROOM,
    "hosp_day": HOSP_ROOM,
}
MOOD = {
    "hotel": "early morning, bright soft daylight through sheer curtains, pale gold and cool blue tones, clear sky over the city, a tense guilty hush",
    "office": "evening dusk, deep indigo sky and city lights through the window, a single warm desk lamp, lonely restless guilt",
    "home": "early evening after sunset, clear night, warm amber pendant lamplight against deep blue dusk at the window, cosy family tenderness",
    "home_shock": "evening, clear night, the warm amber lamps turned cold by a dizzying blue tint, soft blur at the edges, sudden dread",
    "landing": "night, harsh white corridor light against the warm glow from the open door, urgent panic",
    "ot_corridor": "late night, cold fluorescent light, hushed and still, deep grief",
    "ward_corridor": "late night, dim quiet corridor lights, deep blue shadows, exhausted sorrow",
    "hosp_night": "late night, a single dim warm night lamp, deep blue shadows, rain-free dark window, heavy silent grief",
    "hosp_day": "daytime over the following week, flat pale daylight through the half-closed blinds, cool grey tones, weary cold distance",
}

BEATS = [
    dict(to=2, reason="episode opening: morning in the Vietnam hotel room, the doorbell wakes Haizum", chars=["haizum"], loc="hotel",
         visual=f"{HZ_HOTEL}, standing at the hotel room's entrance door in his socks, leaning close to peer through the small round peephole, one hand on the door handle, his face sleepy and wary; morning light from the window behind him; the white inner door closed beside him; he is the only person in the room, the room behind him empty",
         camera="medium shot from the side, eye level, his face in the upper third, the beige carpet as a calm lower third", amb="hotel_room"),
    dict(to=7, reason="character change: Daniyal walks in holding out his phone — Sana is calling; Haizum lies to her", chars=["haizum", "daniyal"], loc="hotel",
         visual=f"{HZ_HOTEL}, his bare forearms showing below the short t-shirt sleeves, holding a phone to his ear just inside the doorway, forcing a calm voice while his eyes are full of guilty fear; Daniyal, stout with a moustache, in his light-blue shirt and khaki trousers, walking past him into the room, looking around casually; morning light",
         camera="medium two-shot, eye level, faces in the upper half, the carpet as the lower third", amb="hotel_room"),
    dict(to=11, reason="action change: Daniyal sits on the sofa talking about last night's party while Haizum stands anxious", chars=["daniyal", "haizum"], loc="hotel",
         visual=f"Daniyal in his light-blue shirt sitting comfortably on the grey sofa, leaning back and gesturing as he chats, puzzled and amused; {HZ_HOTEL}, standing stiffly a few steps away by the desk, arms folded tight, face tense with extreme worry, glancing towards the closed white inner door",
         camera="medium wide, eye level, faces in the upper half, the coffee table and carpet as the lower third", amb="hotel_room",
         sens="other", safe="last night's party (implied affair) is never shown; only Haizum's anxious face"),
    dict(to=13, reason="action change: Daniyal steps onto the balcony for a call; Haizum hurries to the closed inner door", chars=["haizum", "daniyal"], loc="hotel",
         visual=f"{HZ_HOTEL}, standing with one hand on the handle of the closed white inner door, looking back over his shoulder towards the balcony with fearful eyes; in the background, beyond the glass sliding door, Daniyal on the small balcony with his back turned, a phone at his ear, the city skyline behind him",
         camera="medium shot, eye level, Haizum's face in the upper third, the carpet as the lower third", amb="hotel_room",
         sens="intimacy", safe="the hint of a woman in his room is only a closed inner door and his guilty face; no woman is shown"),
    dict(to=16, reason="emotional turning point: Daniyal comes back in frowning; Haizum, trembling, starts to confess", chars=["daniyal", "haizum"], loc="hotel",
         visual=f"Daniyal standing in the balcony doorway with his eyebrows knitted in a stern frown, staring hard at Haizum; {HZ_HOTEL}, his bare forearms showing below the short t-shirt sleeves, seen in three-quarter view facing Daniyal across the room, pale, lips parted, one hand half-raised as if about to explain, trembling",
         camera="medium wide over Haizum's shoulder, Daniyal's frowning face in the upper third, the carpet as the lower third", amb="hotel_room"),
    dict(to=18, reason="emotional reversal: 'We got the contract!' — Daniyal grabs Haizum's shoulders, beaming", chars=["daniyal", "haizum"], loc="hotel",
         visual=f"Daniyal beaming with joy, gripping both of Haizum's shoulders and shaking them happily; {HZ_HOTEL}, stunned with his mouth open, a confused half-relieved face; bright morning light flooding in from the balcony",
         camera="medium close two-shot, eye level, faces in the upper half", amb="hotel_room"),
    dict(to=22, reason="character/action change: alone, Haizum sits on the sofa watching Sana's scan video on his phone", chars=["haizum"], loc="hotel",
         visual=f"{HZ_HOTEL}, sitting alone on the edge of the grey sofa, holding his phone in both hands, the screen's soft grey glow lighting his face, his eyes glistening with despair and sorrow; the screen faces him, only a pale grey blur visible to us; the city bright beyond the window",
         camera="medium close-up, slightly low eye level, his face in the upper third, the glass coffee table as the lower third", amb="hotel_room",
         sens="other", safe="the ultrasound video is never shown; only the phone's soft grey glow on his face"),
    dict(to=27, reason="scene and time change: back in Male, weeks later — he keeps calling Shifa's old number, no answer", chars=["haizum"], loc="office",
         visual=f"{HZ}, in a white shirt and dark-navy trousers, standing alone at his office window in the evening, a phone held to his ear, his other hand pressed flat against the glass, eyes closed in restless guilt; the lit city and harbour beyond",
         camera="medium shot from the side, his face in the upper third, the dark desk top as the lower third", amb="office_night",
         transition="black"),
    dict(to=31, reason="time jump (two months later) and scene change: Haizum comes home; pregnant Sana tutoring the children", chars=["haizum", "sana", "laira_child", "lail_child"], loc="home",
         visual=f"{SANA_P}, sitting at the wooden dining table with exercise books open in front of {KIDS}; {HZ_HOME}, just arrived, standing behind her chair with one hand resting gently on her shoulder, smiling tenderly down at her and the children; the children look up and smile",
         camera="medium wide, eye level, faces in the upper half, the table top with books as the lower third", amb="home_night",
         transition="black", sens="intimacy",
         safe="the forehead kisses are not shown: married couple shown only with his hand on her shoulder"),
    dict(to=34, reason="framing change: the baby kicks — Haizum and Sana share a smile", chars=["haizum", "sana"], loc="home",
         visual=f"{SANA_P}, sitting at the dining table, both her hands resting on her rounded belly, looking up with a warm delighted smile; {HZ_HOME}, crouched beside her chair, his hand hovering near her belly, a surprised happy smile on his face; warm lamplight",
         camera="medium close two-shot, eye level, faces in the upper half, the table edge and her loose dress softly below", amb="home_night"),
    dict(to=37, reason="characters change: the children come to feel the baby; a warm family moment", chars=["sana", "lail_child", "laira_child", "haizum"], loc="home",
         visual=f"{SANA_P}, sitting on the cream sofa smiling; {KIDS} kneeling on either side of her, each with a small hand resting on her rounded belly, faces full of wonder; {HZ_HOME}, sitting on the sofa arm beside them, his hand resting on little Lail's head, smiling; warm lamplight",
         camera="medium wide, eye level, faces in the upper half, the soft grey carpet as the lower third", amb="home_night",
         sens="intimacy", safe="the family hug and forehead kiss are shown as the family gathered side by side; no kiss, no embrace"),
    dict(to=40, reason="action change: Haizum goes to change; his phone stays on the table in front of Sana", chars=["sana", "haizum"], loc="home",
         visual=f"{SANA_P}, sitting at the dining table smiling after him; in the background {HZ_HOME}, walking away down the corridor towards the inner rooms, glancing back with a smile; in the foreground on the table top, next to the exercise books, his black phone lying face down",
         camera="medium wide, eye level, Sana's face in the upper third, the table top with the phone as the lower third", amb="home_night"),
    dict(to=42, reason="action change: the children leave with their books; alone, Sana tidies the table as his phone lights up", chars=["sana"], loc="home",
         visual=f"{SANA_P}, standing at the dining table stacking exercise books, turning her head as Haizum's phone on the table lights up with a soft white glow; in the far background the children walking away down the corridor carrying their books",
         camera="medium shot, eye level, her face in the upper third, the table top with the glowing phone as the lower third", amb="home_night",
         sens="other", safe="the phone screen is only a soft glow; no readable text"),
    dict(to=45, reason="emotional turning point: Sana reads Shifa's message", chars=["sana"], loc="home",
         visual=f"close-up of {SANA_P}, holding Haizum's phone in both hands, its cold white glow on her face, her eyes widening in disbelief, lips parted, the colour draining from her face; the screen faces her, only its glow visible",
         camera="close-up, eye level, her face in the upper half, her hands and the phone in the middle, her dress soft below", amb="home_night",
         sens="other", safe="the message is never readable; only the glow and her face"),
    dict(to=48, reason="action change: dizziness — the world spins, she searches the phone frantically", chars=["sana"], loc="home_shock",
         visual=f"{SANA_P}, swaying on her feet, one hand gripping the edge of the dining table for support, the other clutching the glowing phone, her face pale and frightened, eyes unfocused; the room around her blurred and tilting with soft doubled edges as if spinning",
         camera="medium shot, slightly tilted dutch angle, her face in the upper third, the table top as the lower third", amb="home_night"),
    dict(to=51, reason="action change: Sana collapses; the children scream; Haizum rushes out of the bedroom", chars=["sana", "laira_child", "lail_child", "haizum"], loc="home_shock",
         visual=f"{SANA_P}, sitting on the soft carpet with her back resting against the cream sofa, her head leaning on the sofa cushion, eyes closed as if fainted, a phone on the carpet beside her hand; a few steps behind her {KIDS} standing still with worried faces; in the corridor behind them, {HZ_HOME}, fully dressed, hurrying towards her with wide alarmed eyes",
         camera="medium wide, slightly high angle, faces in the upper two-thirds, the carpet as the lower third", amb="home_night",
         sens="other", safe="the fall is not shown: she is sitting slumped against the sofa; Haizum (who in the narration holds a T-shirt) is fully dressed; no injury"),
    dict(to=54, reason="location change: rushing out — Laira holds the door open, Lail calls the lift", chars=["haizum", "lail_child", "laira_child"], loc="landing",
         visual=f"the building corridor: little Lail (10) in his striped t-shirt pressing the lift button with a frightened face; little Laira (12) in her pink dress and dove-grey hijab holding the apartment door wide open; {HZ_HOME}, hurrying out of the doorway, his face desperate and tearful",
         camera="medium wide, eye level, faces in the upper half, the tiled floor as the lower third", amb="home_night",
         sens="other", safe="Haizum carrying his unconscious wife is not shown; only his urgent face and the children"),
    dict(to=57, reason="location and time change: the hospital — the doctor says the baby could not be saved", chars=["haizum", "laira_child", "lail_child"], loc="ot_corridor",
         visual=f"a doctor in green theatre scrubs and a cap standing at the closed operating-theatre doors, his head lowered in sorrow; facing him {HZ_HOME}, his shirt rumpled, standing speechless with his arms around the shoulders of {KIDS} who press against his sides crying, tears on their cheeks",
         camera="medium wide, eye level, faces in the upper half, the polished floor as the lower third", amb="hospital_corridor",
         sens="other", safe="the loss of the baby is only spoken; the baby and the operation are never shown"),
    dict(to=59, reason="character change: that night Grandma Shafeeqa takes the children home", chars=["shafeeqa", "laira_child", "lail_child", "haizum"], loc="ward_corridor",
         visual=f"Maama Shafeeqa in her dark-maroon libaas, white headscarf and gold glasses walking away down the corridor holding the hands of {KIDS}, who glance back sadly; in the foreground {HZ_HOME}, standing alone in the open doorway of a private room, shoulders slumped, watching them go",
         camera="medium wide, eye level, faces in the upper half, the polished floor as the lower third", amb="hospital_night"),
    dict(to=63, reason="location and action change: in the private room Sana pulls her hand from Haizum's; her face swollen from crying", chars=["sana", "haizum"], loc="hosp_night",
         visual=f"{SANA_H}, propped up high against white pillows on the hospital cot, her eyes red and swollen, tears on her cheeks, her hand pulled back against her chest, staring away; {HZ_HOME}, his shirt rumpled, half-risen from the visitor chair beside her, leaning towards her with deep worry; IV stand in the dim background",
         camera="medium shot, eye level, faces in the upper half, the white sheet as a calm lower third", amb="hospital_night",
         sens="other", safe="patient propped up, no needle, no wound; married couple not touching"),
    dict(to=68, reason="action change: she turns away from him, sobbing; he stands bewildered — 'Love, what happened?'", chars=["sana", "haizum"], loc="hosp_night",
         visual=f"{SANA_H}, propped up on the pillows but turned away to the far side, her face towards the dark window, shoulders shaking as she weeps; {HZ_HOME}, standing at the side of the cot a step away, one hand half-raised and frozen in the air, his face full of confusion and hurt",
         camera="medium wide, eye level, faces in the upper two-thirds, the white sheet as the lower third", amb="hospital_night"),
    dict(to=70, reason="time change: the following seven days — he tries to feed her, she will not look at him", chars=["sana", "haizum"], loc="hosp_day",
         visual=f"{SANA_H}, sitting propped up, thin and pale, her face turned away with empty eyes; {HZ}, in a pale-grey shirt, sitting on the visitor chair holding out a small bowl and spoon towards her, tired and patient; an IV stand beside the cot in the background, no needle visible",
         camera="medium shot, eye level, faces in the upper half, the white sheet and a tray table as the lower third", amb="hospital_day",
         transition="black", sens="other", safe="IV stand only in the background, no needle"),
    dict(to=72, reason="action change: he pleads with her; she turns her back on him", chars=["haizum", "sana"], loc="hosp_day",
         visual=f"{HZ}, in a pale-grey shirt, sitting on the visitor chair pulled close to the cot, hands clasped, leaning forward and pleading with pained eyes; {SANA_H}, propped up but turned fully away from him, her back to him, a tear on her cheek in profile",
         camera="medium shot, eye level, faces in the upper half, the white sheet as the lower third", amb="hospital_room"),
    dict(to=74, reason="action change and episode ending: helpless, Haizum walks out of the room", chars=["haizum", "sana"], loc="hosp_day",
         visual=f"{HZ}, in a pale-grey shirt, standing in the open doorway of the hospital room, one hand on the door frame, looking back over his shoulder with a defeated, heartbroken face; in the foreground, soft and out of focus, {SANA_H}, propped up and turned away towards the window, crying silently",
         camera="medium wide from inside the room, his face in the upper third, the floor as the lower third", amb="hospital_room"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "In the morning, Haizum was woken by the sound of the doorbell. Pushing the blanket off him and yawning, he got up.",
   [("doorbell_buzz", "ބެލް", -16), ("cloth_rustle", "ރަޖާގަނޑު", -24)])
sh(2, "He went with quick steps and looked through the peephole; outside stood his close friend Daniyal. As soon as Haizum opened the door,",
   [("door_open", "ހުޅުވައިލުމާއެކު", -20)])
sh(3, "Daniyal held out the phone in his hand. \"Sana's been calling. Where's your phone, Haizum?\" Daniyal asked as he walked into the room.")
sh(4, "Haizum's heart jolted with fear. \"Hello,\" Haizum answered the phone, hiding his unease. \"Where's your phone? Do you know how worried I've been!\"",
   [("heartbeat", "ތެޅިގަތެވެ", -20)])
sh(5, "From the other end came Sana's anxious voice. \"Sana... I was just going to call. Last night I fell asleep a little early, so I didn't even hear the phone ring.")
sh(6, "I'm really, really sorry.\" Haizum lied. \"You didn't even send so much as a message, that's why I was so worried,\" Sana said in a complaining tone.")
sh(7, "\"Hold on, I'll call you in a little while.\" Haizum quickly ended the call and handed the phone back to Daniyal.")
sh(8, "\"You left last night's party without even saying a word. I've been standing here not knowing what happened. I saw you go into the hall, but after that I had no idea.\"")
sh(9, "Talking as if he had no wish to leave, Daniyal went and sat down on the sofa. At that moment Haizum's face showed the utmost worry.")
sh(10, "\"Go on, Daniyal, I'll get ready and come down,\" Haizum said. \"No, we'll go together.")
sh(11, "There's a small matter I need to discuss with you,\" Daniyal replied. Not daring to push any harder to send Daniyal away,")
sh(12, "as luck would have it, Daniyal got a phone call and stepped out onto the balcony. Seizing the chance, Haizum quickly grabbed the bathroom handle and opened the door.",
   [("phone_buzz", "ފޯނެއް", -20), ("door_open", "ހުޅުވާލިއެވެ", -22)])
sh(13, "Haizum looked anxiously towards the balcony. And he shut his eyes, thinking of what would happen next.",
   [("breath", "މަރައިލެވުނީ", -22)])
sh(14, "He concluded that his secret had been exposed. At that moment Daniyal came back into the room, his brows knitted, staring at Haizum.")
sh(15, "\"Daniyal, I'll tell you what happened,\" Haizum said in a trembling voice. \"What is there to tell?\"")
sh(16, "Daniyal asked in a somewhat stern tone. The fear in Haizum's heart grew. \"We got the contract!\"",
   [("heartbeat", "ބިރުވެރިކަން", -18)])
sh(17, "Daniyal announced with a sudden joyful smile. Haizum was astonished, his mouth fell open. Daniyal happily went and threw his arms around Haizum.",
   [("cloth_rustle", "ބައްދައިލިއެވެ", -22)])
sh(18, "\"This is all the result of your hard work,\" Daniyal said, smiling. \"I'm off to tell Jimmy and the others. Get ready quickly and come.\"")
sh(19, "When Haizum picked up the phone lying on the table and looked, there were about twenty missed calls and many messages from Sana.")
sh(20, "Looking through the messages one by one, he opened a video message Sana had sent. It was a scan video of the beloved baby in Sana's womb.")
sh(21, "Haizum took the phone, went and sat on the sofa. Sana's face appeared in the video. \"This is our little baby.\"")
sh(22, "Sana's voice could be heard, full of joy. At that moment Haizum's face showed despair and sorrow.", hum=True)
sh(23, "Feeling that he had been unfaithful to Sana, he closed his eyes. Even after returning from Vietnam, Haizum found no way to reach Shifa.",
   [("sigh", "މަރައިލެވުނެވެ", -22)], hum=True)
sh(24, "Not having Shifa's current number, he tried calling her old number many times. Because Shifa had left without saying anything, an unease he couldn't describe had grown in Haizum's heart.")
sh(25, "Even when Haizum left for Vietnam, an uneasy distance had grown between him and Sana because of her condition. But,")
sh(26, "after coming back from Vietnam, Haizum had failed to give Sana the attention she needed. Only one question kept turning in his mind.")
sh(27, "Why had Shifa left so suddenly without a single word? Two months went by. As the days passed,")
sh(28, "those memories slowly faded from Haizum's heart. When Haizum came home after finishing at the office,",
   [("door_open", "ވަންއިރު", -22)])
sh(29, "Sana, seven months pregnant, was sitting teaching Lail and Naira their lessons. Coming inside, Haizum lovingly stroked the two children's cheeks.")
sh(30, "And bending towards Sana, he lovingly kissed her forehead and gently touched her belly. \"How was today?")
sh(31, "Did you feel very sick and throw up a lot?\" Haizum asked in a soft voice full of tenderness.")
sh(32, "Sana gently shook her head to say no. \"Is the baby okay?\" Haizum asked again. Just then the baby in her womb kicked.")
sh(33, "It was as if it were answering its father's question. A smile spread over Haizum's lips. Sana too looked at Haizum with eyes full of love.")
sh(34, "\"Look, the baby answered too,\" Sana said with a joyful smile. \"Mamma, is little one kicking?\"")
sh(35, "Lail got up from where he sat, came and stood beside Sana, and touched his mother's belly. Haizum lovingly stroked Lail's head.")
sh(36, "Then Naira too came and stroked Sana's belly. \"Little one, this is your big sister,\" Naira said, bending down lovingly.")
sh(37, "Sana smiled and stroked the two children's heads. Haizum drew Sana close to his chest together with the children, and once more kissed Sana's forehead.",
   hum=True)
sh(38, "\"Go on, quickly change your clothes and come and eat. The children's lessons are finished now too,\" Sana said lovingly, taking Haizum's hand.")
sh(39, "\"Coming, okay.\" Kissing Sana's forehead once more, Haizum walked off towards the bedroom.")
sh(40, "The two children were still stroking Sana's belly. But Haizum had gone leaving his phone on the table in front of Sana.")
sh(41, "\"Go on, you two, put your books away now. Mamma's getting dinner,\" Sana said, getting up from the table. Ten-year-old Lail and twelve-year-old Naira took their books and went inside.",
   [("paper_shuffle", "ފޮތްތައް", -22)])
sh(42, "While Sana was tidying the table, a message suddenly arrived on Haizum's phone. As the screen lit up, the start of the message caught Sana's eye.",
   [("phone_buzz", "މެސެޖެއް", -16)])
sh(43, "\"Hi Haizum.\" Sana picked up the phone, opened it and began reading the message. \"Hi Haizum. I'm sorry for leaving so suddenly without saying anything.")
sh(44, "I thought a lot about what you said. But I felt it's far too late now. I'm not sending this message to upset you.",
   hum=True)
sh(45, "But because it's something important that you also need to know, I'm sharing it.\" When she finished reading the message, Sana's head began to spin.",
   [("heartbeat", "އެނބުރުން", -18)], hum=True)
sh(46, "The things before her eyes blurred, and she began to feel as if the whole world were lurching from side to side.", hum=True)
sh(47, "Some of the words on the phone screen blurred until they were hard to read. While Sana was straining her eyes wide to make out who had sent the message,")
sh(48, "her hand slipped and the number was deleted. Panicking, she began searching like a madwoman to find the message again. By then her whole body was trembling,",
   [("breath_heavy", "ތުރުތުރުއަޅައި", -20)], hum=True)
sh(49, "and she felt as though the world were spinning. In the end Sana fell unconscious to the floor, phone and all. \"Mamma!\"",
   [("soft_thud", "ވެއްޓުނެވެ", -16), ("gasp", "މަންމާ", -18)], hum=True)
sh(50, "Unable to hold back, the cry burst out at the top of their voices. At the sound of the scream Haizum came out of the room, a T-shirt in his hand that he'd taken to put on.",
   [("door_open", "ނުކުތްއިރު", -22)])
sh(51, "Seeing Sana collapsed on the floor, Haizum's eyes went wide with shock. \"Sana.\" Haizum ran over and lifted Sana in his arms.",
   [("gasp", "ސިހުން", -20), ("footsteps_pavement", "ދުވެފައި", -22)], hum=True)
sh(52, "There was no strength left in Sana's body. Calling to Laira, who had come out of her room, Haizum told her to open the door quickly. As soon as Laira opened the door,",
   [("door_open", "ހުޅުވައިލުމާއެކު", -20)])
sh(53, "Lail ran ahead and got the lift ready. From the state Sana was in, Haizum realised they had to get to the hospital without delay. \"What happened to Mamma?\"",
   [("lift_ding", "ލިފްޓު", -18)])
sh(54, "Lail asked anxiously. \"Come quickly with Bappa, children,\" Haizum said in a tearful voice.",
   [("sob_breath", "ކަރުނަވީ", -24)])
sh(55, "Picking up Haizum's T-shirt from where it had fallen on the carpet, Laira too hurried out after them. \"I'm very sorry, we couldn't save the baby.",
   [("footsteps_pavement", "ނުކުތެވެ", -24)])
sh(56, "But Sana is fine now.\" At these words from the doctor who came out of the operating theatre, tears streamed uncontrollably from the eyes of Laira and Lail on either side of their father.",
   [("sob_breath", "ކަރުނަ", -22)], hum=True)
sh(57, "Because their beloved little sibling had gone before ever seeing the light of the world. Haizum held the two children close, standing speechless.",
   hum=True)
sh(58, "That night, after Sana was moved to a private room, Haizum's mother Shafeeqa came to see the children, and he sent the children home with her.")
sh(59, "Haizum sat beside Sana in deep grief and unease. All the hopes the couple had built for that tiny baby who would never be born lay shattered.",
   hum=True)
sh(60, "Even as he sat in the chair with his head bowed in despair, Haizum's left hand held Sana's hand tightly.")
sh(61, "Haizum opened his eyes when Sana twisted her hand free and pulled it away. Haizum quickly got up and, coming close to Sana,",
   [("cloth_rustle", "ދަމައިގަތުމުންނެވެ", -22)])
sh(62, "tenderly stroked her head. By then Sana's face and nose were red and swollen from crying and crying.")
sh(63, "Sana's eyes were swollen and full of tears. More than the pain of the operation, her heart was breaking from distress and grief.",
   hum=True)
sh(64, "Unwillingly, Sana pushed away Haizum's hand from her forehead as one pushes away the touch of a stranger.", hum=True)
sh(65, "Sobbing without stopping, Sana turned to the other side so as not to show Haizum her face. Haizum's face showed bewilderment.",
   [("sob_breath", "ގިސްލެވެމުން", -22)])
sh(66, "Because the partner who in every such sorrow would always seek his help and love had pushed him away today. \"Love, what happened?\"")
sh(67, "Haizum asked in a voice full of worry. But Sana gave no answer. No sound but sobbing could be heard in that room.",
   [("sob_breath", "ގިސްލުމުގެ", -24)])
sh(68, "She would not even let Haizum touch her. Not eating anything and crying without stopping, Sana's condition went down,")
sh(69, "and she had to spend seven days in hospital on an IV drip. During that time Haizum worked tirelessly to feed her and care for her. But,")
sh(70, "besides not saying a single word, Sana didn't even want to look at Haizum. However hard Haizum thought, he couldn't work out what wrong he had done.")
sh(71, "\"Please, Sana... tell me what happened. If I don't know what's going on, how can we find a way to fix it?\"")
sh(72, "Haizum pleaded, sitting down by the bedside. Without saying anything, Sana turned her back on Haizum and turned to the other side.",
   [("cloth_rustle", "އެނބުރުނެވެ", -24)])
sh(73, "The more Haizum tried to talk, the more tears flowed from Sana's eyes. In the end,",
   [("sob_breath", "ކަރުނަތައް", -24)], hum=True)
sh(74, "not wanting to make Sana cry any more, Haizum, at a loss, walked out of that room.",
   [("door_close", "ނުކުމެގެން", -22)], hum=True)
SHOTS = S

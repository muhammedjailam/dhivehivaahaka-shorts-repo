"""Beat/shot plan for Tedhuveriloabi episode 482 (used by plan_beats.py)."""

LOC = {
    "office": "the open-plan finance floor of the Rafhaan Group glass high-rise in Malé, modern white desks, glass walls with a city and sea view, golden late-afternoon light",
    "corridor": "a cool white corridor of ADK Hospital in Malé, a row of pale waiting chairs against the wall, polished floor, soft daylight",
    "doctor_room": "a bright consultation room at ADK Hospital in Malé, a white desk, a window with soft daylight, a few medical folders, a potted plant",
    "car": "the back seat of a dark luxury car driving through Malé in the afternoon, sunlit city buildings passing outside the window",
    "mansion": "the spacious living room of a large modern mansion in Malé, a curved staircase, cream sofas, tall windows with sheer curtains, a garden view",
    "dining": "the large dining room of a modern Malé mansion at night, a long wooden dining table laid with many dishes of Maldivian food, warm chandelier light",
    "balcony": "a wide balcony of a modern mansion at night overlooking the lights of Malé city and the dark sea, a glass railing, potted palms",
    "jail_room": "a plain bare room with pale walls, a small high window letting in a pale beam of light, a simple wooden table and chair",
    "sky": "the sky above Malé and the Indian Ocean, heavy dark clouds breaking apart over the city skyline and the sea",
    "marquee": "a large white marquee on the white-sand beach of a new luxury Maldivian resort at dusk, colourful balloons and big flower bouquets, round tables with white cloths, fairy lights, turquoise lagoon and palms behind",
    "stage": "inside a large white beach marquee at a luxury Maldivian resort opening at night, a wooden podium with a microphone on a small stage decorated with white and blush flowers, rows of guests at round tables",
    "beach_bench": "a wooden bench on the white-sand beach of a Maldivian resort at night, gentle waves, palm trees, a full moon and stars over the sea",
    "moon_sea": "the calm Indian Ocean off a Maldivian resort beach at the very end of the night, a full moon low over the water and a first golden glow on the horizon",
    "mansion_day": "the bright living room of a large modern Malé mansion on a sunny morning, a soft rug, scattered colourful toys, tall windows with a garden view",
    "prison_gate": "the tall plain grey outer gate and high wall of Maafushi prison on a Maldivian island in the morning, a sandy road outside, a few palm trees, a vast sky with dark clouds gathering",
}
MOOD = {
    "office": "late afternoon, warm golden light through the glass, quiet, a sudden tension",
    "corridor": "cool white hospital light, anxious waiting, hopeful",
    "doctor_room": "soft bright daylight, gentle, joyful surprise",
    "car": "afternoon sunlight through the car window, tender, happy and calm",
    "mansion": "warm afternoon light, joyful family celebration",
    "dining": "night, warm golden chandelier light, happy, united families",
    "balcony": "night, cool blue city glow and warm light from the house, reflective, peaceful",
    "jail_room": "muted cool grey light, a single pale beam from the high window, remorseful and quiet",
    "sky": "dramatic clouds parting, golden rays of hope breaking through, uplifting",
    "marquee": "dusk turning to evening, warm golden fairy lights and soft pink sky, festive and elegant",
    "stage": "evening, warm spotlight on the podium, glowing fairy lights, proud and emotional",
    "beach_bench": "night, silver full moonlight, deep blue sea, tender and peaceful",
    "moon_sea": "moonlight fading into the first golden dawn light, serene and hopeful",
    "mansion_day": "bright warm morning light, playful, cheerful family happiness",
    "prison_gate": "morning, flat grey light under gathering dark clouds, ominous calm",
}

BEATS = [
    dict(to=2, reason="new episode opening: Layaali dizzy at her desk", chars=["layaali"], loc="office",
         visual="Layaali sitting at her office desk, one hand pressed to her forehead, eyes half closed, her face pale and unwell, leaning forward over a blank financial report; the desk top and floor calm in the lower third",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=6, reason="character change: Rafhaan rushes over from his cabin", chars=["rafhaan", "layaali"], loc="office",
         visual="Rafhaan standing beside Layaali's desk, leaning down towards her with a deeply worried face, one hand on the desk edge; Layaali seated, looking up at him with a weak brave smile, a respectful small distance between them; his glass cabin in the background",
         camera="medium two-shot, eye level", amb="office_day"),
    dict(to=8, reason="scene change: waiting in the hospital corridor", chars=["rafhaan", "layaali"], loc="corridor",
         visual="Rafhaan and Layaali sitting side by side on waiting chairs in a white hospital corridor, her hand resting on his forearm, Rafhaan looking at her with quiet hopeful concern, Layaali gazing ahead calmly",
         camera="medium wide, eye level", amb="hospital_corridor", sens="other",
         safe="him gripping her hand shown as her hand resting on his forearm (married couple, minimal touch)"),
    dict(to=11, reason="scene change: the doctor's room and the result", chars=["doctor", "rafhaan", "layaali"], loc="doctor_room",
         visual="the doctor seated behind a white desk smiling warmly while holding a blank report sheet, Rafhaan and Layaali seated across the desk side by side, Rafhaan leaning forward in surprise; the wall behind is plain and bare with no signs, no symbols, no posters and no icons",
         camera="medium wide over the desk", amb="hospital_day"),
    dict(to=13, reason="emotional turning point: the joy of the pregnancy news", chars=["rafhaan", "layaali"], loc="doctor_room",
         visual="close two-shot: Rafhaan turning to Layaali with a radiant overjoyed smile and shining eyes; Layaali beside him with happy tears glistening, both hands pressed over her heart",
         camera="close two-shot, eye level", amb="hospital_day", sens="intimacy",
         safe="Rafhaan pressing her hand to his lips is not shown; joyful faces, her hands over her heart"),
    dict(to=16, reason="scene change: on the way home in the car", chars=["rafhaan", "layaali"], loc="car",
         visual="Rafhaan and Layaali sitting side by side in the back seat of a car, her hand resting on his arm, both smiling softly and talking, sunlight and city buildings through the window",
         camera="medium two-shot from the front seat", amb="car_interior", sens="other",
         safe="holding hands shown as her hand resting on his arm"),
    dict(to=19, reason="scene and character change: telling Rafhaan's parents at the mansion", chars=["khadeeja", "layaali", "ibrahim", "rafhaan"], loc="mansion",
         visual="in the mansion living room Khadeeja joyfully embracing Layaali with a beaming smile, Layaali smiling shyly; Ibrahim laughing happily beside them and Rafhaan standing proudly a step behind",
         camera="medium wide, eye level", amb="mansion_day"),
    dict(to=23, reason="time jump: that night, both families dine together", chars=["qaasim", "ibrahim", "aminath", "khadeeja"], loc="dining",
         visual="the two families' elders at one end of a long dining table full of Maldivian dishes: frail Qaasim beaming with joy as he speaks to Ibrahim, Ibrahim smiling warmly back, Aminath and Khadeeja seated beside them smiling",
         camera="medium wide, eye level", amb="mansion_night", transition="black"),
    dict(to=25, reason="scene change: Rafhaan steps out to the balcony with the message", chars=["rafhaan"], loc="balcony",
         visual="Rafhaan standing alone at the glass railing of the balcony at night, looking down at his phone in his hand, the screen glow facing away from the viewer lighting his serious thoughtful face, city lights behind him",
         camera="medium shot, eye level", amb="balcony_night", sens="other",
         safe="the letter and phone screen are never readable; the screen faces away"),
    dict(to=28, reason="character change: Ahna in jail writing the letter (imagined as it is read)", chars=["ahna"], loc="jail_room",
         visual="Ahna, wearing NOT her usual outfit but a plain dark-grey abaya and a plain black hijab, no makeup, sitting alone at a simple wooden table writing on a blank sheet of paper with a pen, her eyes lowered, remorseful and humble",
         camera="medium shot, slightly high angle", amb="room_night", transition="dissolve", sens="other",
         safe="jail shown only as a plain bare room; no bars, uniform or guards; the letter is blank, no text"),
    dict(to=29, reason="back to Rafhaan on the balcony (reuse)", reuse="beat_009", chars=["rafhaan"], loc="balcony",
         visual="(reuse) Rafhaan on the balcony with his phone", amb="balcony_night", transition="dissolve"),
    dict(to=33, reason="character change: Layaali joins him on the balcony", chars=["layaali", "rafhaan"], loc="balcony",
         visual="Layaali and Rafhaan standing side by side at the balcony railing at night, the warm city lights on their faces, Layaali smiling gently with one hand resting on her belly, Rafhaan looking down at her tenderly with a soft smile, a light breeze in her hijab",
         camera="medium two-shot, eye level", amb="balcony_night", sens="other",
         safe="Rafhaan placing his hand on her belly shown as her own hand resting on her belly while he looks on tenderly"),
    dict(to=35, reason="time jump: months pass, clouds clear", loc="sky",
         visual="heavy dark clouds breaking apart over the Malé skyline and the sea, golden rays of sunlight streaming through the gaps onto the water, no people",
         camera="wide establishing shot", amb="dawn_exterior", transition="black"),
    dict(to=39, reason="scene change: opening ceremony of the Seaview Resort", loc="marquee",
         visual="a grand white marquee on white sand at dusk, decorated with colourful balloons and large flower bouquets, many guests in elegant modest formal clothes gathering around round tables, the turquoise lagoon and palms behind",
         camera="wide shot", amb="resort_evening"),
    dict(to=42, reason="character change: Rafhaan and pregnant Layaali arrive", chars=["rafhaan", "layaali"], loc="marquee",
         visual="Rafhaan in his black suit walking with a happy confident smile, Layaali beside him with her hand resting on his arm; Layaali wears NOT her black abaya but a loose ankle-length long-sleeved gown in a pale onion-pink blush colour with a matching pale blush hijab fully covering her hair and neck, eight months pregnant with a softly rounded figure under the loose gown, her face glowing and gentle",
         camera="medium wide, eye level, slightly low", amb="resort_evening", sens="other",
         safe="pregnancy shown only through a loose modest gown, no belly focus"),
    dict(to=45, reason="action change: Rafhaan's speech at the podium", chars=["rafhaan"], loc="stage",
         visual="Rafhaan standing at a wooden podium with a microphone, speaking with heartfelt sincerity, one hand on the podium, warm spotlight on him, guests listening in hushed silence in the soft-focus foreground",
         camera="medium shot, slightly low angle", amb="hall_crowd"),
    dict(to=46, reason="emotional turning point: applause, Layaali's tears of joy", chars=["layaali"], loc="stage",
         visual="close-up of Layaali in her pale blush gown and matching pale blush hijab, tears of joy on her cheeks and a trembling smile, one hand resting gently on her belly, applauding guests blurred behind her in warm fairy lights",
         camera="close-up", amb="hall_crowd"),
    dict(to=48, reason="character change: the proud parents at their table", chars=["layaali", "khadeeja", "aminath", "qaasim"], loc="stage",
         visual="Layaali, dressed tonight entirely in a loose pale onion-pink blush gown with a matching pale blush hijab (no black clothing on her at all, the same blush outfit as at her arrival), seated at a round table with a white cloth; Khadeeja beside her holding Layaali's hand warmly and smiling at her; Aminath and frail Qaasim seated beside them glowing with pride",
         camera="medium wide, eye level", amb="hall_crowd"),
    dict(to=52, reason="scene change: after the party, the bench by the sea", chars=["rafhaan", "layaali"], loc="beach_bench",
         visual="Rafhaan and Layaali sitting side by side on a wooden bench on the moonlit beach, seen from a three-quarter angle, gentle waves before them, a full moon and stars, Rafhaan speaking softly and Layaali, in her pale blush gown and matching hijab, listening with a peaceful smile; calm sand in the lower third",
         camera="wide shot, eye level", amb="beach_night", sens="other",
         safe="his hand on her shoulder shown as the couple sitting side by side"),
    dict(to=57, reason="action change: closer moment, they feel the baby move", chars=["layaali", "rafhaan"], loc="beach_bench",
         visual="closer two-shot on the bench: Layaali in her pale blush gown and matching hijab with her own hands resting gently on her belly, smiling with delighted surprise; Rafhaan sitting upright beside her with a small gap between them, his own hands resting on his knees, not touching her, laughing joyfully and looking at her face; moonlight on their faces",
         camera="medium close two-shot", amb="beach_night", sens="intimacy",
         safe="head on his shoulder and his hand on her belly shown as her own hands on her belly, side by side"),
    dict(to=60, reason="symbolic image: two hearts as one, darkness turning to golden light", loc="moon_sea",
         visual="gentle waves rolling onto white sand under a fading full moon, two pairs of footprints side by side in the wet sand, the first golden glow of dawn on the horizon, no people",
         camera="wide shot, low angle", amb="beach_night"),
    dict(to=63, reason="time jump: three years later, daughter Raina", chars=["raina", "layaali", "rafhaan"], loc="mansion_day",
         visual="a happy family scene in the bright living room: little Raina laughing as she toddles towards Layaali, who kneels on the rug with open arms and a joyful smile in her black abaya and black hijab; Rafhaan sitting on the sofa behind them smiling; colourful toys on the floor",
         camera="medium wide, eye level", amb="home_day", transition="black"),
    dict(to=65, reason="scene change: the gate of Maafushi prison opens", loc="prison_gate",
         visual="the tall plain grey prison gate standing open, a lone woman in a plain dark-grey abaya and black hijab seen from behind stepping out onto the sandy road, a long shadow stretching from her, dark clouds gathering in the sky",
         camera="wide shot from behind", amb="prison_exterior", transition="black", sens="other",
         safe="prison shown only as a plain gate and wall from outside; no bars, guards or signs"),
    dict(to=67, reason="character reveal: Ahna's face, free and smiling", chars=["ahna"], loc="prison_gate",
         visual="Ahna standing outside the prison gate, wearing NOT her usual outfit but a plain dark-grey abaya and a plain black hijab, no makeup, lifting her face to the sky with an ambiguous calm smile that hints at something hidden, dark clouds behind her",
         camera="medium close-up, slightly low angle", amb="prison_exterior"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Layaali was sitting at her desk looking over a financial report when suddenly she felt so dizzy she had to lay her head down on the desk.",
   [("soft_thud", "ބޯޖައްސާލަން", -24)])
sh(2, "The colour drained from her face and she began to sweat. This was not something that normally happened. 'Layaali! What's wrong?'")
sh(3, "Rafhaan, coming out of his cabin, saw it and came almost running. 'It's nothing, Rafhaan...",
   [("door_open", "ކެބިންއިން", -20), ("footsteps_pavement", "ދުވެފައި", -22)])
sh(4, "just a little dizzy.' Layaali tried hard to smile. 'No, this isn't just tiredness.")
sh(5, "It happened two or three times last week too.' Worry showed in Rafhaan's eyes. 'Let's go to the doctor right now.")
sh(6, "I'm really worried.' Layaali tried to protest, but with Rafhaan's tender insistence the two of them went to the hospital together.")
sh(7, "Waiting in the cold hospital corridor, Rafhaan sat holding Layaali's hand tightly.")
sh(8, "His heart kept telling him that some new change was coming into their lives. They went into the doctor's room, did some tests and waited for the results.",
   [("door_open", "ވަދެ", -22)])
sh(9, "A little later the doctor looked at the report with a smile. 'There's nothing to worry about, Rafhaan,' the doctor said.",
   [("paper_shuffle", "ރިޕޯޓަށް", -22)])
sh(10, "'This is very happy news. Layaali is now expecting to become a mother. She is five weeks pregnant.")
sh(11, "The tiredness on her face is normal at this stage.' 'Pregnant?' Rafhaan said the word with extraordinary emotion.",
   [("gasp", "ބަނޑުބޮޑު", -20)])
sh(12, "Joy shone in his eyes. He turned at once to Layaali. In Layaali's eyes were tears overflowing with happiness.", hum=True)
sh(13, "A new flower was blooming in the garden of their love. 'Thank you, doctor! Thank you so much!' Rafhaan said, pressing Layaali's hand to his lips.", hum=True)
sh(14, "All the way home Rafhaan never let go of Layaali's hand. 'Layaali... my life is complete today.")
sh(15, "I can never repay the happiness you have brought into my life.' 'Rafhaan... this is a great blessing God has given us.")
sh(16, "Now we must build a world full of love for this child,' Layaali said.")
sh(17, "As soon as they got home, Rafhaan gave the happy news to his mother Khadeeja and his father Ibrahim.",
   [("door_open", "ދެވުމާއެކު", -22)])
sh(18, "Hearing it, Khadeeja rushed with joy and hugged Layaali. 'My dear child! What great happiness! I'm going to be a grandmother.'",
   [("cloth_rustle", "ބައްދާލިއެވެ", -22)])
sh(19, "Overjoyed, Khadeeja kissed Layaali's forehead. 'From today Layaali must not go to the office and work hard. She must rest at home.")
sh(20, "Rafhaan will look after the company.' That night Layaali's mother and father were brought to the house too. The two families ate together at one table.",
   [("cup_clatter", "ކެއުން", -22)])
sh(21, "Layaali's father Qaasim was glowing with happiness. 'Ibrahim. For our lives to see such a happy day")
sh(22, "is a great mercy from God,' Qaasim said. 'Yes, Qaasimbe. Today we are not two families. We are one family.'")
sh(23, "Ibrahim Faahim said with a smile. But while this happy atmosphere went on, a message arrived on Rafhaan's phone.",
   [("phone_buzz", "މެސެޖެއް", -16)])
sh(24, "It was a message from Ahna, who was in jail: a photo of a letter she had sent through her father Zaahir.")
sh(25, "Rafhaan quietly stepped out onto the balcony and opened the message. The letter said: 'Rafhaan and Layaali...",
   [("door_open", "ބެލްކަންޏަށް", -22)])
sh(26, "Today the court sentenced me for all the wrongs I did. I have to serve a three-year prison sentence.")
sh(27, "Today I stand changed from the depths of my heart. I heard from my father the news of the new child coming into your lives.", hum=True)
sh(28, "From the depths of my heart I ask your forgiveness, and I will always wish you a happy life.' Rafhaan took a deep breath.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -20)])
sh(29, "With that letter, even the last resentment towards Ahna in his heart faded away. True justice is not only punishment.")
sh(30, "It is the change in the wrongdoer's heart. Layaali came out onto the balcony and stood beside Rafhaan. 'Rafhaan... what message?'",
   [("footsteps_pavement", "ނިކުމެ", -24)])
sh(31, "Rafhaan showed Layaali the phone. After reading it, Layaali smiled. 'God has given Ahna good sense.")
sh(32, "There was never hatred for anyone in my heart, even before.' Rafhaan gently placed his hand on Layaali's belly. 'Yes, Layaali.")
sh(33, "Our child will come into a safe world full of love, without hatred.' Just then a cool breeze brushed over them, and instead of moonlight the lights of the neighbourhood fell on their faces.",
   [("wind_gust", "ފިނިރޯޅިއެއް", -22)])
sh(34, "Days and months passed at their own pace; the heavy dark clouds in the sky cleared completely and golden rays of hope filled their lives.")
sh(35, "With Layaali eight months pregnant, the whole family lived in extraordinary happiness, awaiting a new life.")
sh(36, "The resort project started by Rafhaan's company, 'Rafhaan Group', was finished, and today was the day of the ceremony to officially open it.")
sh(37, "The big marquee set up on the resort's white sand was decorated with colourful balloons and bouquets of flowers.")
sh(38, "All the company's staff and the Maldives' big businessmen had gathered to congratulate Rafhaan and Layaali on their success.")
sh(39, "Today everyone was talking about one thing: the noble qualities of Layaali, who came from a poor, humble family and won the heart of the whole company through her honesty and courage.")
sh(40, "Rafhaan wore a black suit. His manly stride and the happy smile on his face showed the joy of a life that felt complete today.")
sh(41, "Layaali, holding his arm, wore a beautiful gown of a pale onion-skin colour.")
sh(42, "Her pregnancy gave her face an innocent glow. Following the ceremony's agenda, Rafhaan stepped up to the podium.",
   [("footsteps_pavement", "ޖެހިލިއެވެ", -24)])
sh(43, "A deep silence fell over the whole marquee. 'Tonight is the happiest night of my business life,' Rafhaan began into the microphone.")
sh(44, "'But the true owner of this success is not me.")
sh(45, "It is my partner, who never left the path of honesty and justice even when great challenges came to the company and her own honour and life were put at risk.", hum=True)
sh(46, "My wife, Layaali.' The whole hall rang with thunderous applause. Tears of joy rolled from Layaali's eyes.",
   [("applause", "ގުގުމާލީ", -14)], hum=True)
sh(47, "At the table, the faces of Layaali's mother Aminath and of Qaasim shone with pride.")
sh(48, "Rafhaan's mother Khadeeja held Layaali's hand tightly and smiled. Today in that family there was no difference at all between wealth and poverty.")
sh(49, "There was only family love. After the party, Rafhaan and Layaali sat together on a bench on the resort's beach.")
sh(50, "There was no sound but the waves breaking on the shore and the breeze. The moon was full in the sky and the stars were twinkling.",
   [("wave_crash", "ރާޅުތައް", -22)])
sh(51, "'Layaali... today our life has sailed into a safe harbour,' Rafhaan said, resting his hand on Layaali's shoulder.")
sh(52, "'From Ahna's jealousy and Shiyaz's deceit we learned one thing: an honest heart will never come to harm.'")
sh(53, "'Yes, Rafhaan.' Layaali rested her head on Rafhaan's shoulder. 'I never imagined even in a dream that an ordinary girl like me would find such great happiness.")
sh(54, "Rafhaan, you are the greatest fortune God has sent into my life.' Rafhaan gently placed his hand on Layaali's belly.")
sh(55, "At that moment they both felt the baby kick. Smiles spread over both their faces.",
   [("heartbeat", "ތޮޅުމުގެ", -20)], hum=True)
sh(56, "'Look, our child agrees too,' Rafhaan laughed. 'I promise this child will grow up brave, kind and loving justice.")
sh(57, "Just like her mother.' 'And like her father, an honest and just leader,' Layaali added.")
sh(58, "With the music of the waves, their two hearts beat as one. Over the great storms of jealousy and scheming, pure true love had won a lofty victory.",
   [("wave_crash", "ރާޅުތަކުގެ", -22), ("heartbeat", "ވިންދު", -20)], hum=True)
sh(59, "The new chapter of their life began with a peace and happiness born in the very depths of their hearts.")
sh(60, "The darkness of hatred faded and the golden light of love lit up their whole life. After the happy days of the marriage, a long three years went by.")
sh(61, "'Rafhaan Group' is now one of the biggest businesses in the Maldives. Rafhaan and Layaali's little family has grown even more complete.")
sh(62, "They now have a lovely two-year-old girl, the light of their eyes. Her name is 'Raina'.")
sh(63, "Raina's mischief and laughter have brightened the whole house. Layaali now spends most of her time at home looking after her daughter.")
sh(64, "In these very days, the big gate of Maafushi prison opened, and with the footsteps of a woman who walked out, an unseen dark shadow over this family",
   [("lock_click", "ހުޅުވި", -18), ("footsteps_pavement", "ފިޔަވަޅުތަކާއެކު", -20)])
sh(65, "began to circle overhead once again. It was Ahna. Having completed her three-year sentence, today she stood free.",
   [("heartbeat", "އަހްނާއެވެ", -18)], hum=True)
sh(66, "Anyone who saw the plain clothes she wore and the scarf covering her head would think her heart had been completely cleansed and repentant.")
sh(67, "Stepping out of the prison, she lifted her head and looked up at the sky. An ordinary smile spread across her lips.",
   [("wind_gust", "އުޑުމައްޗަށް", -22)])
SHOTS = S

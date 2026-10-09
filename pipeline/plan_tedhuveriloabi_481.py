"""Beat/shot plan for Tedhuveriloabi episode 481 (used by plan_beats.py)."""

LOC = {
    "wedding_terrace": "an open terrace of an elegant wedding hall in Malé at night, decorated with white and gold flower garlands and soft fairy lights, a stone balustrade, the lights of Malé and a sky full of stars beyond",
    "mansion_living": "the spacious sitting room of a large modern Malé mansion, cream sofas, a low glass coffee table, a wide staircase in the background, tall windows with sheer curtains",
    "finance_floor": "the open-plan finance floor of a modern glass high-rise office in Malé, rows of clean white desks with computer monitors, glass partitions, a city and sea view through floor-to-ceiling windows",
    "sea_horizon": "the calm open sea off Malé seen from the shore, a flat glassy lagoon, a single rising wave, and a heavy dark storm cloud gathering on the horizon",
    "cabin": "the CEO's luxurious glass-walled cabin on a high floor of a modern Malé office tower, a large dark wooden desk, a leather chair, a laptop and a desktop monitor, floor-to-ceiling windows over the city and the sea",
    "mansion_room": "a quiet private study room in a large modern Malé mansion, a wooden desk with a closed laptop, bookshelves, a tall window with sheer curtains",
    "server_corner": "a corner of the open-plan finance floor of a modern Malé office tower beside a tall black server rack with small blinking lights, desks with monitors, glass partitions",
    "balcony": "the wide balcony of a large modern mansion in Malé at night, a glass railing, potted palms, the city lights of Malé below and the open sea beyond",
}
MOOD = {
    "wedding_terrace": "night, warm golden fairy lights, starlit deep-blue sky, tender and joyful",
    "mansion_living": "warm daylight through sheer curtains, soft amber tones, peaceful and harmonious",
    "finance_floor": "bright golden late-morning light through the glass, busy, confident and successful",
    "sea_horizon": "early morning, pale light on the water under a looming dark plum-grey cloud, an ominous calm before the storm",
    "cabin": "morning, cool daylight through the glass with warm amber accents, tense and serious",
    "mansion_room": "late afternoon, warm low light through the curtains, private, tense and determined",
    "server_corner": "midday light, quiet and empty office, suspenseful",
    "balcony": "night, a bright full moon, silvery moonlight and soft city glow, a gentle breeze, peaceful and loving",
}

BEATS = [
    dict(to=3, reason="new episode opening: the newly married couple on the wedding night (continues ep 480)", chars=["rafhaan", "layaali"], loc="wedding_terrace",
         visual="Rafhaan and Layaali standing side by side at the flower-decked balustrade, looking out at the stars over Malé; Layaali wears her modest white lace wedding gown with long sleeves, ankle length, and a white hijab fully covering her hair and neck (not her black abaya); she smiles softly with her hand resting lightly on his arm; Rafhaan looks at her with a calm, happy smile",
         camera="medium two-shot from slightly behind and to the side, faces in the upper third", amb="balcony_night", sens="intimacy",
         safe="'she rested her head on his shoulder' shown as the married couple standing side by side, her hand resting on his arm"),
    dict(to=6, reason="time jump: three happy months later at the mansion, Khadeeja now loves Layaali", chars=["khadeeja", "layaali"], loc="mansion_living",
         visual="Khadeeja and Layaali sitting together on a cream sofa, Khadeeja smiling warmly and offering Layaali a cup of tea, Layaali smiling back gratefully, a tea tray on the glass coffee table",
         camera="medium two-shot, eye level", amb="mansion_day", transition="black"),
    dict(to=8, reason="scene change: Layaali as head of finance at the office, the company prospers", chars=["layaali"], loc="finance_floor",
         visual="Layaali standing confidently beside a desk on the finance floor holding a closed folder, smiling and guiding her team; blurred office staff in modest clothes working at monitors in the background",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=9, reason="symbolic detail: a wave rising on a calm sea, a dark cloud on the horizon", loc="sea_horizon",
         visual="a calm glassy lagoon at early morning with a single wave rising and a heavy dark storm cloud building on the horizon over the sea, no people",
         camera="wide shot, low over the water", amb="dawn_exterior"),
    dict(to=12, reason="scene change: morning in Rafhaan's cabin, Layaali enters with a worrying file", chars=["rafhaan", "layaali"], loc="cabin",
         visual="Rafhaan sitting at his large desk studying large architectural sketches of a resort spread before him; Layaali entering through the glass door carrying a thick closed file, her face uneasy and worried",
         camera="medium wide, eye level", amb="office_day"),
    dict(to=17, reason="action change: Layaali sits and explains the leak, Rafhaan reacts", chars=["layaali", "rafhaan"], loc="cabin",
         visual="Layaali sitting in a chair across the desk from Rafhaan, leaning forward, explaining earnestly with an anxious face, the closed file on the desk between them; Rafhaan leaning back in shock, frowning in disbelief",
         camera="medium two-shot across the desk", amb="office_day"),
    dict(to=19, reason="emotional turning point: fear of being framed again", chars=["layaali"], loc="cabin",
         visual="close-up of Layaali, her large eyes glistening with worry and fear, her hands clasped tightly against her chin, the soft city light behind her",
         camera="close-up, faces in the upper half", amb="office_day"),
    dict(to=21, reason="action change: Rafhaan stands beside her and reassures her", chars=["rafhaan", "layaali"], loc="cabin",
         visual="Rafhaan standing beside Layaali's chair, looking down at her with a firm, reassuring and protective expression; Layaali looking up at him with relief, her hand resting on his forearm",
         camera="medium shot, slightly low angle", amb="office_day", sens="other",
         safe="'he held her hand firmly' shown as him standing beside her chair, her hand resting on his forearm (married)"),
    dict(to=26, reason="character change: Aasim checks the server logs", chars=["aasim", "rafhaan", "layaali"], loc="cabin",
         visual="Aasim sitting at the desk in front of an open laptop, scratching his head with a troubled frown, the laptop screen glowing softly and facing away from the viewer; Rafhaan standing behind him with folded arms and Layaali beside, alarmed",
         camera="medium wide, eye level, from in front of the desk", amb="office_day"),
    dict(to=29, reason="action change: Rafhaan alone in thought, remembering the guests", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan standing alone at the floor-to-ceiling window of his cabin, one hand on his chin, deep in thought, looking out at the city and the sea",
         camera="medium close-up in profile", amb="office_quiet"),
    dict(to=32, reason="scene and time change: that afternoon at the mansion, Khadeeja introduces Shiyaz", chars=["khadeeja", "shiyaz", "rafhaan"], loc="mansion_living",
         visual="Khadeeja sitting on the cream sofa gesturing with a pleased smile towards a young man sitting beside her, Shiyaz, who has a polite, humble expression; Rafhaan standing in the doorway, just arrived home, briefcase in hand",
         camera="medium wide, eye level", amb="mansion_day", transition="black"),
    dict(to=35, reason="action change: Shiyaz greets Rafhaan; Rafhaan notices his sly smile", chars=["shiyaz", "rafhaan"], loc="mansion_living",
         visual="Shiyaz standing and shaking hands with Rafhaan, smiling with a sly, cunning glint in his narrow eyes; Rafhaan returning a polite smile but with sharp, watchful eyes",
         camera="medium close two-shot, eye level", amb="mansion_day"),
    dict(to=41, reason="scene change: in private, Rafhaan and Layaali plan the trap", chars=["rafhaan", "layaali"], loc="mansion_room",
         visual="Rafhaan and Layaali standing face to face at a respectful distance beside the desk, Rafhaan explaining with a determined, confident face, one hand raised slightly as he speaks; Layaali listening anxiously with her hands clasped",
         camera="medium two-shot, eye level", amb="room_day"),
    dict(to=43, reason="time jump: next day at the office, the false file is placed", chars=["layaali", "shiyaz"], loc="finance_floor",
         visual="Layaali deliberately placing a thick closed plum-coloured file with a blank cover on her desk; in the background near the server rack Shiyaz stands with an innocent, polite face, watching the file from the corner of his eye",
         camera="medium shot, eye level", amb="office_day", transition="black"),
    dict(to=45, reason="action change: at lunch break Shiyaz secretly copies the data", chars=["shiyaz"], loc="server_corner",
         visual="in the empty office at lunchtime Shiyaz bending over Layaali's desk, photographing the open file with his phone (pages blank from this angle), a small black hard drive in his other hand connected by a cable to the server rack, glancing over his shoulder furtively",
         camera="medium shot from the side, slightly high angle", amb="office_quiet"),
    dict(to=47, reason="character change: Rafhaan, Layaali and Aasim watch on the hidden camera", chars=["aasim", "rafhaan", "layaali"], loc="cabin",
         visual="Aasim typing fast on his laptop while Rafhaan and Layaali lean in behind him, all three watching a large monitor whose screen faces away from the viewer and glows softly; tense, focused faces",
         camera="medium shot from behind the monitor, faces lit by the screen glow", amb="office_quiet"),
    dict(to=50, reason="action change: Rafhaan and Layaali walk in with security; Shiyaz caught", chars=["shiyaz", "rafhaan", "layaali"], loc="server_corner",
         visual="Shiyaz in the foreground, startled and pale, hiding a small black hard drive behind his back beside the server rack; Rafhaan and Layaali striding in through the glass door towards him, followed by two office security guards in plain dark uniforms with no text",
         camera="medium wide, eye level", amb="office_day"),
    dict(to=53, reason="action change: the confrontation; Layaali steps forward", chars=["layaali", "rafhaan", "shiyaz"], loc="server_corner",
         visual="Layaali taking a step forward towards Shiyaz and speaking with calm dignity, Rafhaan beside her with a stern, firm face; Shiyaz cornered against the server rack, eyes darting, guilty",
         camera="medium two-shot over Shiyaz's shoulder", amb="office_day"),
    dict(to=54, reason="action change: Shiyaz drops the hard drive and is taken by police", chars=["shiyaz"], loc="server_corner",
         visual="Shiyaz with his head bowed in defeat, a small black hard drive lying on the floor at his feet, two Maldivian police officers in plain dark-blue uniforms with no visible insignia or text escorting him away by the elbows",
         camera="medium wide, eye level", amb="office_day", hum_note="arrest", sens="other",
         safe="arrest shown as officers calmly escorting him; no weapons, no handcuffs emphasised"),
    dict(to=55, reason="back to the cabin: the evidence is sent to the investors (reuse)", reuse="beat_016", chars=["aasim", "rafhaan", "layaali"], loc="cabin",
         visual="(reuse) the three at the monitor in the cabin", amb="office_day"),
    dict(to=59, reason="scene and time change: that night on the moonlit balcony", chars=["rafhaan", "layaali"], loc="balcony",
         visual="Rafhaan and Layaali (in her black abaya and black hijab) standing upright side by side at the glass railing of the balcony with a small space between them, under a bright full moon over Malé, a gentle breeze moving her hijab; both looking out at the moonlit sea with calm, content smiles",
         camera="medium two-shot from slightly behind, the moon high in the frame", amb="balcony_night", transition="black", sens="intimacy",
         safe="'he put his hand on her shoulder / she held his hand' shown as the married couple side by side, her hand on his arm"),
    dict(to=62, reason="time jump: two months later, the office thrives (reuse of the office success image)", reuse="beat_003", chars=["layaali"], loc="finance_floor",
         visual="(reuse) Layaali leading the finance floor", amb="office_day", transition="black"),
    dict(to=64, reason="action change: Layaali looks tired and unwell at work", chars=["layaali"], loc="finance_floor",
         visual="Layaali sitting at her desk with a weary, pale face, one hand pressed to her forehead, eyes half closed, a closed report folder in front of her, soft morning light",
         camera="medium close-up, eye level", amb="office_day"),
    dict(to=65, reason="action change: dizzy, she lays her head on the desk (cliffhanger)", chars=["layaali"], loc="finance_floor",
         visual="Layaali resting her head on her folded arms on her desk, eyes closed, dizzy and faint, a pen fallen from her hand onto the closed folder, the monitor beside her glowing and facing away, the busy office softly blurred behind",
         camera="medium shot, slightly high angle", amb="office_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Layaali... a new chapter of our life has begun. Never again will any storm be able to part us,\" Rafhaan said softly.")
sh(2, "Smiling, Layaali rested her head on Rafhaan's shoulder. Truth and humility had won a lofty victory over envy, power and wealth.")
sh(3, "Their love story did not end here. This was the beginning of an entirely new, happy life.")
sh(4, "The three months that passed after the joyful wedding were the happiest, most peaceful days of Layaali's life.")
sh(5, "In Rafhaan's big, wealthy household she now found nothing but love and care.")
sh(6, "The displeasure once in Khadeeja's heart had vanished completely, and Layaali had become one of the most important pillars of the house.")
sh(7, "Through the responsible work Layaali did as head of the office's finance department, the company's profits had grown beyond what they were before.")
sh(8, "A sweet fragrance had spread through the garden of Rafhaan and Layaali's love. But life does not always travel calmly in the same way.")
sh(9, "Like a wave that suddenly rises while the sea lies calm, a new dark cloud began to appear on the horizon of their life. It was morning.",
   [("wave_crash", "ބާނީއެއް", -22)])
sh(10, "Rafhaan was sitting in his cabin looking at drawings for the new resort project. Layaali came into the cabin holding a big file, unease showing on her face.",
   [("door_open", "ކެބިންއަށް", -20)])
sh(11, "\"Rafhaan... look at these reports,\" Layaali said, setting the file on the desk. \"A big payment due from our new investors has been delayed.",
   [("paper_shuffle", "ބާއްވަމުން", -20)])
sh(12, "And a letter sent from their head office says they have doubts about the company's internal management.\"")
sh(13, "Rafhaan looked at Layaali in surprise. \"Doubts? What kind of doubts? Everything we do is completely clean.\" \"They say...")
sh(14, "that the company's secret information is leaking to another, competing company outside. Especially the financial accounts and the bid prices —")
sh(15, "such important documents,\" Layaali said, sitting down. \"And the worst part... the outside auditors say the information was taken from the system using my user ID.\"",
   [("cloth_rustle", "އިށީންނަމުން", -24)])
sh(16, "Rafhaan was startled. Could that be? \"Layaali! That can't be. Does anyone else know your ID?\"",
   [("gasp", "ސިހުން", -22)])
sh(17, "\"No, Rafhaan. Nobody knows my password. I have never shared it with anyone.\"")
sh(18, "Worry began to show in Layaali's eyes. The old frightening memories took over her mind. Was someone once again plotting to trap her in a pit of disgrace?",
   [("heartbeat", "ބިރުވެރި", -18)], hum=True)
sh(19, "\"Is it someone's hand again this time?\" was all Layaali could say. \"Don't be upset, Layaali.\"")
sh(20, "Rafhaan got up, went to her and held Layaali's hand firmly. \"I will always trust you completely.",
   [("cloth_rustle", "ތެދުވެގެން", -24)])
sh(21, "This is someone trying to bring us down after our marriage. I'll have Aasim look into it.\" Rafhaan immediately called Aasim to the cabin.",
   [("knock", "ގެނުވިއެވެ", -20)])
sh(22, "Aasim began going through the system's main logs. But this time the plot was far cleverer than before.",
   [("keyboard_typing", "ލޮގްތައް", -22)])
sh(23, "The IP address showed it came straight from the internet connection at Layaali's home, from her own laptop. \"Boss... this is a very difficult one,\" Aasim said, scratching his head.",
   [("sigh", "ބޯކަހާލިއެވެ", -22)])
sh(24, "\"According to these logs the information was sent late at night from the computer at Layaali's home. This may be the work of hackers.")
sh(25, "But it's hard to detect from the system.\" Layaali's heart pounded hard. \"Late at night? At twelve last night I was asleep.",
   [("heartbeat", "ތެޅެމުންދިޔައެވެ", -18)], hum=True)
sh(26, "Rafhaan would know that too, wouldn't he?\" \"Yes, Layaali. We were together. So I am one hundred percent sure you wouldn't do this.\"")
sh(27, "Rafhaan was lost in thought. \"But who can get onto our home network? Who knows the house Wi-Fi password?\"")
sh(28, "At that moment something came to Rafhaan's mind. He remembered some guests who had come to stay at their house over the past weeks.")
sh(29, "In particular, although Ahna had gone to jail, some of her distant relatives still kept in touch with Rafhaan's mother Khadeeja.")
sh(30, "That afternoon, when Rafhaan went home, Khadeeja was sitting in the sitting room talking with the son of a close friend of hers. That was Shiyaz.",
   [("door_open", "ގެއަށް", -20)])
sh(31, "Shiyaz was a young man who had studied IT abroad but had no job. He was Ahna's cousin. \"Rafhaan!")
sh(32, "This is Shiyaz. He studied abroad and can't find a job, so I told him we'd arrange a job for him in the company's IT section.\"")
sh(33, "Khadeeja said with a smile. Shiyaz stood up and greeted Rafhaan. The cunning smile in his eyes did not escape Rafhaan's sharp gaze.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(34, "Rafhaan's heart told him at once: behind this new storm stood this Shiyaz in his simple guise. He had come to take revenge for Ahna. \"Shiyaz...", hum=True)
sh(35, "very glad to meet you. A big IT project is running in our office right now. Come to the office tomorrow.\"")
sh(36, "Rafhaan said, with a secret plan in mind. After Shiyaz left, Rafhaan took Layaali into the room. \"Layaali... the culprit is standing right before our eyes.",
   [("door_close", "ކޮޓަރިއަށް", -20)])
sh(37, "Shiyaz is Ahna's cousin. Last week he came and stayed at this house. He did this secretly, using the details on your laptop and the house Wi-Fi.\"")
sh(38, "Rafhaan said. \"But Rafhaan... how will we prove this is true? The investors are running out of time.\" Layaali was anxious.")
sh(39, "\"We have to trap him in his own pit. Otherwise cunning people like this can never be caught.\"")
sh(40, "Determination showed in Rafhaan's eyes. \"Tomorrow when he comes to the office we'll give him a file full of false information.")
sh(41, "When he tries to take it out in his greed for money, we'll have Aasim catch him red-handed.\"")
sh(42, "Layaali agreed with Rafhaan's plan. The next day Shiyaz came to the office looking perfectly innocent.")
sh(43, "Rafhaan put him in temporary charge of maintaining the finance department's servers. And Layaali deliberately left a file marked 'New resort secret budget' on her desk.",
   [("paper_shuffle", "ބޭއްވިއެވެ", -20)])
sh(44, "Inside it were entirely false figures. At lunch break, when everyone had gone out, Shiyaz crept up to Layaali's desk.",
   [("footsteps_pavement", "ޖެހިލިއެވެ", -26)])
sh(45, "He began photographing the file with his phone. And he connected the hard drive in his hand to the server and began copying the data.",
   [("keyboard_typing", "ކޮޕީކުރަން", -24)])
sh(46, "What he didn't know was that Rafhaan, Layaali and Aasim were watching the whole scene through the cabin's secret camera.")
sh(47, "Aasim at once got into Shiyaz's phone and hard drive and was making a live recording of every transaction he carried out.",
   [("keyboard_typing", "ވަދެ", -22)])
sh(48, "Just as Shiyaz finished and pulled the hard drive out of the server, the cabin door opened and Rafhaan and Layaali walked in.",
   [("door_open", "ހުޅުވާލާފައި", -16), ("footsteps_pavement", "ވަނެވެ", -24)])
sh(49, "Behind them came the office security too. The colour drained from Shiyaz's face. \"Boss... I...",
   [("gasp", "ބަދަލުވިއެވެ", -22)])
sh(50, "I was only checking the system.\" Seeing the two of them come in together, Shiyaz panicked. He tried to hide the hard drive.",
   [("cloth_rustle", "ފޮރުވަން", -24)])
sh(51, "\"Don't try to fool us any more, Shiyaz,\" Rafhaan said firmly. \"Video and digital evidence of everything you did has been recorded.")
sh(52, "You used my wife's name to take revenge for Ahna. But none of your plots will ever succeed against Layaali's honesty.\"")
sh(53, "Layaali stepped forward. \"Shiyaz... didn't even Ahna's life teach you that a heart full of envy and evil gains nothing?\"")
sh(54, "Shiyaz bowed his head. The hard drive fell from his hand to the floor. The police came, arrested Shiyaz and took him away.",
   [("soft_thud", "ވެއްޓުނެވެ", -18), ("footsteps_pavement", "ގެންދިޔައެވެ", -24)], hum=True)
sh(55, "Rafhaan immediately sent all this evidence to the foreign investors. Seeing the company's security and Layaali's honesty, they judged it the act of a hacker and transferred the delayed money at once.",
   [("keyboard_typing", "ފޮނުވިއެވެ", -24)])
sh(56, "That night Rafhaan and Layaali were on the balcony of Rafhaan's house. A full moon hung in the sky over Malé, and cool breezes brushed against them.",
   [("wind_gust", "ރޯޅިތައް", -24)])
sh(57, "\"Layaali... with every storm that comes, our bond only grows stronger.\" Rafhaan put his hand on Layaali's shoulder. \"Yes,")
sh(58, "Rafhaan. I believe that no evil can ever stand again before true love.\"", hum=True)
sh(59, "Smiling, Layaali held Rafhaan's hand tightly. The first shadows of a new page in their life had now begun to appear.")
sh(60, "Two months have now passed since Shiyaz's cunning plot was exposed and the company's staff were defended before the foreign investors.")
sh(61, "The business of 'Rafhaan Group' now runs in the front rank of the most advanced companies in the Maldives.")
sh(62, "Thanks to Layaali's hard work and honesty, the whole atmosphere of the office has come to life again.")
sh(63, "But in recent days quite different changes had begun to show in Layaali. Tiredness was often visible on her face.")
sh(64, "And amid the heavy office work she sometimes began to suffer dizziness and nausea. It was morning.")
sh(65, "Sitting at her desk going through a financial report, Layaali suddenly felt so dizzy that she had to lay her head down on the desk.",
   [("heartbeat", "ބޯއެނބުރޭވަރުން", -18), ("soft_thud", "ބޯޖައްސާލަން", -22)], hum=True)
SHOTS = S

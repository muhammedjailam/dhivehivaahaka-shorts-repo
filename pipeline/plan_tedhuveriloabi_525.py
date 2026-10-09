"""Beat/shot plan for Tedhuveriloabi episode 525 (final episode; used by plan_beats.py)."""

LOC = {
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin high in a modern glass office tower in Malé, a large glass desk with a black leather executive chair and two guest chairs, a closed plain document folder and a silver pen on the desk, floor-to-ceiling glass walls with a view of the dense city and the turquoise sea, a glass door to the open-plan office",
    "office": "the open-plan finance floor of a modern glass office tower in Malé, rows of white desks with computer monitors facing away, glass partitions, potted plants, big windows with a city view",
    "tower": "the entrance plaza of a modern glass office high-rise in Malé, wide glass doors, young palm trees, a busy city street",
    "court": "a quiet Maldivian courtroom, a polished dark-wood judge's bench on a raised platform, tall windows with soft daylight, rows of empty wooden benches, no emblems",
    "mansion": "the elegant living room of a large modern mansion in Malé, cream sofas, a low glass coffee table, a curved staircase, tall windows onto a green garden",
    "house": "the tiny plain sitting room of an old small house in a narrow Malé lane, a simple wooden bed with a faded cotton sheet against a pale wall, a faded curtain, an old wooden window letting in afternoon light",
    "memory": "a hazy remembered office of thirty years ago in Malé, old wooden desks, slatted window blinds, old filing cabinets",
    "office_later": "a bright modern open-plan office in Malé decorated with fresh plants, white desks with monitors facing away, glass walls with sea view",
    "balcony": "the wide wooden-deck balcony of a new luxury resort on a Maldivian island, a white railing, overlooking a turquoise lagoon, a white-sand beach and coconut palms, the sun low over the sea",
    "terrace": "a shaded resort terrace near the balcony with cushioned rattan chairs and a low table with cups of tea, coconut palms and a turquoise lagoon behind",
}
MOOD = {
    "cabin": "early afternoon, bright cool daylight through the glass walls, tense, heavy atmosphere",
    "office": "early afternoon, cool office light, stunned silence",
    "tower": "morning, bright tropical daylight, busy and charged",
    "court": "soft daylight, solemn, still and just",
    "mansion": "late afternoon, warm soft light through tall windows, reflective and quiet",
    "house": "late afternoon, warm golden light through the old window, tender and emotional",
    "memory": "hazy, desaturated sepia memory, soft vignette, sad and lonely",
    "office_later": "bright morning light, warm, friendly and hopeful",
    "balcony": "golden hour, warm amber sunlight, soft glowing sea, joyful and peaceful",
    "terrace": "golden hour, warm amber sunlight, gentle breeze, content and peaceful",
}

BEATS = [
    dict(to=2, reason="new episode opening: Zaahir's ultimatum in Rafhaan's cabin", chars=["zaahir", "layaali", "naasif"], loc="cabin",
         visual="Ahmed Zaahir seated in a guest chair across the glass desk, leaning back with an arrogant mocking smile and pushing a closed plain document folder towards Layaali; Layaali (black hijab) seated at the side of the desk, pale and frightened; Naasif standing behind Zaahir holding his leather briefcase with a sly look",
         camera="medium wide, eye level", amb="office_day"),
    dict(to=5, reason="character focus change: Ahna presses Layaali to sign", chars=["ahna", "layaali"], loc="cabin",
         visual="Ahna (deep burgundy hijab) standing beside the seated Layaali and leaning over her with a cold triumphant smile, one finger tapping the closed folder on the glass desk; Layaali (black hijab) looking down at the desk, lips pressed together, holding back tears",
         camera="medium close two-shot, slightly high angle", amb="office_day"),
    dict(to=10, reason="emotional turning point: Layaali's silent tears and prayer, then she takes the pen", chars=["layaali"], loc="cabin",
         visual="close-up of Layaali (black hijab) seated at the glass desk, a single tear on her cheek, eyes lifted upward in silent prayer, her hand holding a silver pen above blank white pages",
         camera="close-up, eye level", amb="office_day", hum_note="emotional peak"),
    dict(to=11, reason="character focus change: Rafhaan bows his head", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan seated behind his glass desk with his head bowed and his hands clasped tightly in front of his face, eyes closed in helpless pain, the city and sea blurred through the glass wall behind him",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=14, reason="character enters: Aasim bursts through the cabin door", chars=["aasim", "layaali"], loc="cabin",
         visual="Aasim pushing the glass door wide open and striding into the cabin holding an open laptop, his face alive with urgent excitement, one hand raised to say stop; in the foreground Layaali (black hijab) turning towards him with the pen halted above the paper, her tear-filled eyes full of hope",
         camera="medium wide, from behind Layaali's shoulder", amb="office_day"),
    dict(to=18, reason="action change: Zaahir rises in anger, Aasim sets down the laptop and confronts Ahna", chars=["zaahir", "aasim", "ahna"], loc="cabin",
         visual="Zaahir half-risen from his chair with a furious red face, calling out towards the door; Aasim calmly setting his open laptop down on the glass desk, looking straight at Ahna with quiet confidence; Ahna (deep burgundy hijab) standing by the desk, her smug smile starting to falter",
         camera="medium wide, eye level", amb="office_day"),
    dict(to=21, reason="emotional turning point: the faces of Ahna, Zaahir and Naasif drain of colour", chars=["ahna", "zaahir", "naasif"], loc="cabin",
         visual="Ahna (deep burgundy hijab) and Zaahir frozen side by side with pale shocked faces and wide eyes; Naasif stepping back behind them, clutching his briefcase to his chest, nervous and afraid",
         camera="medium close group shot, eye level", amb="office_day"),
    dict(to=24, reason="action change: Aasim shows the evidence on the laptop to Rafhaan and Zaahir", chars=["aasim", "rafhaan", "zaahir"], loc="cabin",
         visual="Aasim turning the open laptop on the glass desk towards Rafhaan and Zaahir, the screen glow facing away from the viewer; Rafhaan leaning in with a focused, steady look; Zaahir staring at the screen, beads of sweat on his forehead",
         camera="medium shot over the desk", amb="office_day"),
    dict(to=25, reason="Ahna's triumph turns into a nightmare (reuse of the shocked faces)", reuse="beat_007", chars=["ahna", "zaahir", "naasif"], loc="cabin",
         visual="(reuse) the shocked faces of Ahna, Zaahir and Naasif", amb="office_day"),
    dict(to=27, reason="action change: Rafhaan rises from his chair", chars=["rafhaan", "aasim"], loc="cabin",
         visual="Rafhaan standing up tall behind his glass desk, shoulders squared, a calm firm determination in his eyes as he speaks; Aasim standing beside the desk with the laptop, nodding with quiet satisfaction",
         camera="medium shot, slightly low angle", amb="office_day"),
    dict(to=29, reason="characters change: a police team enters with an arrest warrant", chars=["zaahir", "ahna", "naasif"], loc="cabin",
         visual="several Maldivian police officers in plain dark-blue uniforms with no visible insignia or text entering through the open glass door, the senior officer in front holding a folded plain paper; Zaahir, Ahna (deep burgundy hijab) and Naasif turning towards them in alarm",
         camera="wide shot from inside the cabin", amb="office_day", sens="other",
         safe="arrest shown as officers entering with a folded plain paper; no weapons"),
    dict(to=30, reason="action change: Zaahir collapses into a chair, Ahna cries out", chars=["zaahir", "ahna"], loc="cabin",
         visual="Zaahir slumped back in a leather chair, dazed and stunned, one hand on his forehead; beside him Ahna (deep burgundy hijab) standing with a desperate, disbelieving face, mouth open in protest",
         camera="medium two-shot", amb="office_day", sens="other",
         safe="Zaahir's dizziness shown as him sitting dazed in a chair, no fall or injury"),
    dict(to=31, reason="scene change: the three are escorted out past the staff", chars=["ahna", "zaahir", "naasif"], loc="office",
         visual="Maldivian police officers in plain dark-blue uniforms with no insignia walking Ahna (deep burgundy hijab), Zaahir and Naasif out through the open-plan office, all three with heads lowered and hands out of view; office staff in modest clothes standing at their desks watching in silence",
         camera="wide shot down the office aisle", amb="office_day", sens="other",
         safe="handcuffing not shown: hands out of view, officers escorting only"),
    dict(to=32, reason="emotional turning point: relief between Layaali and Rafhaan", chars=["layaali", "rafhaan"], loc="cabin",
         visual="Layaali (black hijab) and Rafhaan standing upright side by side by the glass wall, a small gap between their bodies, both heads upright and not touching; Layaali with tears of relief on her cheeks, eyes lifted in gratitude, her hands clasped at her chest; Rafhaan beside her looking at her with a gentle, protective smile, his hands at his sides",
         camera="medium two-shot, eye level", amb="office_quiet", sens="intimacy",
         safe="her tight embrace is shown as a married couple side by side, her hand on his arm only"),
    dict(to=34, reason="time jump and scene change: the case becomes national news", loc="tower",
         visual="a crowd of reporters with plain unmarked cameras and microphones gathered in front of the glass entrance of a modern office tower, camera flashes, busy and excited, seen from behind and at a distance",
         camera="wide shot, eye level", amb="city_day", transition="black"),
    dict(to=37, reason="scene change: the court rules", loc="court",
         visual="an empty quiet courtroom, a wooden gavel resting on the polished judge's bench in the foreground, soft beams of daylight falling across the benches, no people",
         camera="low angle close-up on the gavel, room behind in soft focus", amb="office_quiet"),
    dict(to=39, reason="scene and character change: peace at the mansion, Khadeeja reflects", chars=["khadeeja", "ibrahim"], loc="mansion",
         visual="Khadeeja (pearl-grey hijab) sitting on a cream sofa holding a cup of tea, gazing out of the tall window with a thoughtful, slightly regretful face; Ibrahim sitting beside her, listening calmly with a wise gentle look",
         camera="medium two-shot, eye level", amb="mansion_day", transition="black"),
    dict(to=43, reason="scene and time change: that afternoon Layaali brings the court papers to her father", chars=["qaasim", "layaali", "rafhaan"], loc="house",
         visual="frail Qaasim sitting up on his simple wooden bed, holding a folder of blank papers tightly against his chest with both hands, tears of joy in his eyes, looking upward in gratitude; Layaali (black hijab) sitting on the edge of the bed beside him with tear-filled smiling eyes; Rafhaan seated on a plain chair close by, smiling warmly",
         camera="medium wide, eye level", amb="home_day", transition="black", hum_note="emotional peak"),
    dict(to=46, reason="flashback: Qaasim remembers his humiliation thirty years ago", loc="memory",
         visual="a desaturated memory: a lone man in his thirties in a plain light shirt seen from behind, walking out of an old office carrying a small cardboard box, head bowed, while men in suits at the desks behind him turn away and whisper",
         camera="wide shot from behind", amb="memory", transition="dissolve", sens="other",
         safe="the fraud and accusation are shown only as a lonely man leaving an old office, seen from behind"),
    dict(to=49, reason="back to the present, action change: Qaasim takes Rafhaan's hand", chars=["qaasim", "rafhaan", "layaali"], loc="house",
         visual="close on frail Qaasim on his bed clasping Rafhaan's hand in both of his, a grateful smile through tears; Rafhaan seated close beside the bed, smiling humbly; Layaali (black hijab) behind them, softly smiling",
         camera="medium close-up, eye level", amb="home_day", transition="dissolve"),
    dict(to=52, reason="time jump: months later, Layaali leads with humility", chars=["layaali"], loc="office_later",
         visual="Layaali (black hijab) walking through the bright office with a warm humble smile, stopping to greet an elderly office tea attendant in a plain shirt holding a tray of cups and a young female staff member in a modest grey hijab, all smiling like family",
         camera="medium wide, eye level", amb="office_day", transition="black"),
    dict(to=54, reason="scene change: golden hour on the new resort's balcony with Raina", chars=["rafhaan", "layaali", "raina"], loc="balcony",
         visual="Rafhaan and Layaali (black hijab) standing side by side at the white railing of the resort balcony in golden sunset light, smiling; little Raina in her pink dress running and laughing on the wooden deck near them",
         camera="wide shot, eye level", amb="resort_evening", transition="black"),
    dict(to=57, reason="framing change: the couple's conversation", chars=["rafhaan", "layaali"], loc="balcony",
         visual="Rafhaan and Layaali (black hijab) standing side by side at the balcony railing, the golden sea behind them, looking at each other with loving, peaceful smiles, her hand resting lightly on his arm",
         camera="medium two-shot, eye level", amb="resort_evening", sens="intimacy",
         safe="holding hands / her head on his shoulder shown as standing side by side, her hand on his arm only"),
    dict(to=59, reason="action change: Raina runs to them and Rafhaan lifts her up", chars=["rafhaan", "raina", "layaali"], loc="balcony",
         visual="Rafhaan lifting little Raina high up in the air with both hands, Raina laughing with delight, arms spread; Layaali (black hijab) standing a step apart from him, both her hands clasped together in front of her chest, laughing happily up at Raina, not touching Rafhaan; warm golden sunset glow",
         camera="medium shot, slightly low angle", amb="resort_evening", hum_note="emotional peak"),
    dict(to=60, reason="characters change: both families' parents nearby", chars=["qaasim", "aminath", "ibrahim", "khadeeja"], loc="terrace",
         visual="the parents of both families sitting together on cushioned rattan chairs on the resort terrace, smiling and watching towards the balcony: frail Qaasim and Aminath (white headscarf) on one side, Ibrahim and Khadeeja (pearl-grey hijab) on the other; a cool breeze stirring the palm fronds",
         camera="medium wide, eye level", amb="resort_evening"),
    dict(to=62, reason="ending: back to the little family on the balcony (reuse)", reuse="beat_022", chars=["rafhaan", "layaali", "raina"], loc="balcony",
         visual="(reuse) the family on the balcony at sunset", amb="resort_evening"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "'Rafhaan... time is up,' Zaahir laughed arrogantly. 'Layaali, sign this agreement as quickly as you can.")
sh(2, "Then we get the main control of the company. Otherwise, at four o'clock this afternoon, the prices of all your company's bids will be out on the market.")
sh(3, "Then you'll go bankrupt.' 'Dad. They'll understand. Layaali will sign.' Ahna looked at Layaali. 'Layaali... sign.")
sh(4, "Don't waste this moment. Whatever your father's past may be, today your future is in our hands.'")
sh(5, "Ahna spoke with arrogance. Ahna and her father live by one and the same principle.")
sh(6, "Tears are the most powerful words a heart speaks when words stop. Layaali's tears began to fall, not because she wanted them to.")
sh(7, "Layaali tried as hard as she could to hold back her tears. But at that moment there was no way to hold them back.", hum=True)
sh(8, "In her heart Layaali kept hoping for some good way out. Even if people judge unjustly, there is One who knows.")
sh(9, "Layaali kept praying in her heart: 'O Allah, even if it takes a miracle, decree a way for this to be stopped.'", hum=True)
sh(10, "After the prayer in her heart Layaali looked at the file on the table. She picked up the pen and reached out to sign the agreement.",
   [("paper_shuffle", "ފައިލަށް", -22)])
sh(11, "At that moment Rafhaan bowed his head. It was the hardest moment of their lives — like a man dying of thirst who reaches the water, yet not a single drop touches his lips.", hum=True)
sh(12, "And it was Ahna's moment of greatest triumph. But just as Layaali was about to put the pen to the paper, the cabin door was flung open and in came the IT head, Aasim.",
   [("door_open", "ހުޅުވާލާފައި", -14)])
sh(13, "He had a laptop in his hands. An unusual liveliness showed on his face.")
sh(14, "Layaali looked at Aasim with tear-filled eyes full of hope. 'Wait, Layaali! Don't sign!' Aasim shouted.")
sh(15, "Zaahir stood up in anger. 'Who are you to come in here? Security!' Zaahir shouted. He did not want this moment spoiled.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(16, "'There's no need for security, Zaahir-bey.' Aasim set the laptop down on the table. 'Ahna...",
   [("soft_thud", "ބެހެއްޓިއެވެ", -22)])
sh(17, "did you think burning the paper files in the bank's archive room destroyed all the evidence?")
sh(18, "What you didn't know is that five years ago the bank digitised all its records onto a cloud server.'")
sh(19, "The colour drained from Ahna's and Zaahir's faces at once. Naasif, too, stepped back in alarm.",
   [("gasp", "ބަދަލުވިއެވެ", -22)])
sh(20, "'For the last twenty-two hours I stayed awake checking every trail in the bank's main digital system that Layaali has access to.")
sh(21, "Getting all the access linked to Layaali was a big breakthrough for us. The bank allowing us to check every access we asked for was a huge help from the bank.")
sh(22, "From the archive I recovered the original files of Ahna's father.' Aasim showed the laptop screen to Rafhaan and Zaahir.",
   [("keyboard_typing", "ލެޕްޓޮޕްގެ", -24)])
sh(23, "'Here is the complete digital evidence of how, thirty years ago, Zaahir forged a signature and robbed the company. And that's not all...")
sh(24, "I also found the transfer logs of the money sent from Zaahir's account, through Naasif, to the bank's security man to burn the archive room last night.'")
sh(25, "Aasim's work deserves praise; without sleep he found strong evidence. In a single second the joy of Ahna's triumph turned into a terrifying nightmare.",
   [("heartbeat", "ހުވަފެނަކަށް", -18)], hum=True)
sh(26, "Rafhaan rose from his chair at once. Firm resolve showed in his eyes. 'Zaahir... Ahna... your moment of triumph is over,' Rafhaan said.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(27, "'All of this evidence has already been sent to senior police officers,' Aasim added. Ahna and Zaahir didn't know what to say.")
sh(28, "The cabin door opened and a large team of police came in. They carried an arrest warrant. 'Ahmed Zaahir, Ahna and Naasif...",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -16), ("footsteps_pavement", "ވަނެވެ", -20)])
sh(29, "Arrest them on charges of robbing the company's property, plotting to set fire to the bank, and making threats!' the senior police officer ordered.")
sh(30, "Zaahir's head spun and he dropped into a chair. Ahna screamed. 'No! This can't be! I won't be beaten!'",
   [("soft_thud", "ވެއްޓުނެވެ", -18), ("gasp", "ހަޅޭއްލަވައިގަތެވެ", -18)], hum=True)
sh(31, "But the police held her arm firmly and put handcuffs on her. As they were led out of the cabin under arrest, every member of the office staff stood watching.",
   [("lock_click", "ބިޑި", -18), ("footsteps_pavement", "ނެރުނު", -22)])
sh(32, "Out of the dark cave of deceit, the bright rays of justice broke through. 'Father has got his rights back.' Layaali held on to Rafhaan and wept.",
   [("sob_breath", "ރޮއިގަތެވެ", -22)], hum=True)
sh(33, "After Ahmed Zaahir, Ahna and their lawyer Naasif were taken into police custody,")
sh(34, "this great legal battle between 'Rafhaan Group' and 'Zaahir Investments' made the front-page headlines of news across the whole country.")
sh(35, "Faced with the complete digital evidence Aasim had found, the court settled the case without taking many days and delivered its verdict.",
   [("soft_thud", "އިއްވިއެވެ", -20)])
sh(36, "All the property wrongfully taken from Qaasim thirty years ago, and the entire ownership of 'Zaahir Investments', to its true owner —")
sh(37, "Qaasim — were ordered by the court to be returned. And for setting fire to the bank and making threats, Zaahir and Ahna were given long prison sentences.")
sh(38, "After the great battle, peace settled over the home too. Rafhaan's mother would say now and then:")
sh(39, "'Was Zaahir really that bad a man? He led his own daughter down that path too. What one has to show, one will show.'")
sh(40, "It was the afternoon of that day. Layaali and Rafhaan went together and sat down beside Qaasim. In Layaali's hands were the official court documents.")
sh(41, "'Father... everything you lost has come back to you today.' Looking at her father with tear-filled eyes, Layaali put the papers in Qaasim's hands.",
   [("paper_shuffle", "ދިނެވެ", -22)])
sh(42, "'Zaahir's whole company is now in your name.' Qaasim took the papers Layaali held out. He held on to them tightly.",
   [("paper_shuffle", "ހިފަހައްޓާލިއެވެ", -24)])
sh(43, "Tears of joy streamed from his eyes. 'O Allah. Justice comes to different people at different times, in different ways.",
   [("sob_breath", "އޮހޮރިގެން", -24)], hum=True)
sh(44, "I thought I would leave this world as a disgraced thief. That day, when they robbed me of everything, what an accusation they put on my head.")
sh(45, "They humiliated me in front of the whole world. That day nobody would believe that the real culprit was the one who did it.")
sh(46, "Even now the painful memories of that day are rooted in my heart. My dear child... Rafhaan...", hum=True)
sh(47, "you two are the greatest blessing Allah has given my life.' Qaasim took Rafhaan's hand. 'Father, this isn't something we did.'")
sh(48, "Rafhaan smiled. 'This is simply the reward of honesty. However long a past of injustice may be, its end is always a victory for the humble.")
sh(49, "Those who robbed others' property by deceit all these days have got the punishment they deserve. They are behind prison bars, just as was done to you that day.'")
sh(50, "Two or three months later. The company transferred to Layaali's father has now been renamed 'Layaali Enterprises' and merged with 'Rafhaan Group'.")
sh(51, "Layaali is now one of the most influential and successful businesswomen in the Maldives. Yet the simplicity and humility that were always in her heart have not changed at all.")
sh(52, "She still treats the ordinary office staff like her own family. The good upbringing her parents gave her is a model upbringing.")
sh(53, "As the golden afternoon rays fell on the balcony of the new resort, Rafhaan and Layaali were there. Beside them little Raina was running about and playing.")
sh(54, "Raina's laughter lit up the whole place. 'Layaali... every storm that came into our life has completely passed away today,' Rafhaan said, holding Layaali's hand firmly.")
sh(55, "'From the darkness of the past we have travelled to the horizon of justice.' Rafhaan looked at Layaali lovingly. 'Yes.")
sh(56, "Rafhaan,' Layaali said with a smile, resting her head on Rafhaan's shoulder. 'From the envy of Ahna and her family, we didn't only learn how to run a company.")
sh(57, "We also learned that a place in other people's hearts isn't won by power and wealth — it comes only through kindness and honesty.'")
sh(58, "Raina came running in between the two of them with a sweet smile. In her tiny lovely voice Raina called, 'Mummy. Daddy..",
   [("footsteps_pavement", "ދުވެފައި", -24)])
sh(59, "lift baby up!' Rafhaan lifted Raina up. The little family laughed together. Raina squealed with joy.", hum=True)
sh(60, "A little way off sat the parents of both families. A cool breeze from the sky brushed over them.",
   [("wind_gust", "ރޯޅިއެއް", -22)])
sh(61, "The great schemes of envy, revenge and deceit were shattered, and true love and justice were engraved in letters of gold across their whole life.")
sh(62, "Their love story ends here. But the pure love held in the depths of their hearts will remain forever and ever. (The End)", hum=True)
SHOTS = S

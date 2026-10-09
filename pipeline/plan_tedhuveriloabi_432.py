"""Beat/shot plan for Tedhuveriloabi episode 432 (used by plan_beats.py)."""

LOC = {
    "hq_exterior": "a modern glass high-rise office tower rising above the dense concrete buildings of Malé, Maldives, the turquoise sea and harbour beyond, no signage",
    "finance_floor": "an open-plan finance floor in a modern glass high-rise office in Malé, rows of sleek white desks with computer monitors turned away from the viewer, floor-to-ceiling glass walls with a city and sea view",
    "cabin": "a luxurious glass-walled CEO cabin high in a Malé office tower, a large dark walnut executive desk with a slim laptop with its screen facing away from the viewer, neat blank files and an elegant pen, a black leather executive chair, two guest chairs, floor-to-ceiling windows over the city and the sea",
    "corridor": "a quiet corridor outside a glass-walled executive cabin in a modern Malé office tower, frosted glass walls, polished stone floor, a tall window with the city skyline",
    "sky": "a clear night sky full of bright stars above a calm dark sea, the small distant lights of Malé on the horizon",
    "storm": "the dense Malé city skyline seen across the harbour water at dusk, heavy dark storm clouds rolling in over the city",
    "cafe": "an upscale modern café in Malé, a secluded corner table with plum velvet chairs, a white marble table top, warm brass pendant lamps, a large window onto the evening street",
    "home": "the tiny plain sitting room of a small old house in a narrow Malé lane, a simple single bed against a faded wall, an old wooden window, a small side table with medicine bottles and a glass of water, a slow ceiling fan",
}
MOOD = {
    "hq_exterior": "late afternoon, warm golden sunlight glinting on the glass, aspirational and grand",
    "finance_floor": "late afternoon, golden sunlight streaming through the glass walls, busy and bright",
    "cabin": "late afternoon, warm amber light through the tall windows, hushed and intimate, polished reflections",
    "corridor": "late afternoon turning to dusk, cooler shadows, tense and resentful",
    "sky": "night, deep blue sky, glittering stars, poetic and hopeful",
    "storm": "dusk falling into night, bruised purple and dark grey clouds, ominous",
    "cafe": "evening, warm low pendant light, plum and amber tones, conspiratorial",
    "home": "early evening, a single warm bulb, soft shadows, humble, worried and tender",
}

BEATS = [
    dict(to=2, reason="episode opening: establishing the Rafhaan Group head office in Malé", loc="hq_exterior",
         visual="a low-angle view of a gleaming modern glass office tower rising above the crowded concrete buildings of Malé, golden sunlight flaring off its glass facade, the turquoise harbour glimpsed between buildings, no people, no signs, no lettering on the building",
         camera="wide low-angle establishing shot", amb="city_day"),
    dict(to=7, reason="character introduced: Rafhaan, the young boss everyone talks about", chars=["rafhaan"], loc="finance_floor",
         visual="Rafhaan walking confidently down the aisle of the open-plan finance floor with a warm easy smile, golden light behind him; in the soft-focus background several female office workers in modest abayas and hijabs glance up from their desks towards him",
         camera="medium wide, eye level, Rafhaan centred in the upper half", amb="office_day"),
    dict(to=9, reason="action change: Rafhaan's inner values, alone in his cabin", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan standing at the floor-to-ceiling window of his glass cabin, one hand in his pocket, looking out over the city and the sea with a calm, kind and thoughtful expression, golden light on his face",
         camera="medium shot, three-quarter profile", amb="office_quiet"),
    dict(to=13, reason="characters change: Ahna confronts Layaali at her desk", chars=["ahna", "layaali"], loc="finance_floor",
         visual="Ahna standing tall beside a corner desk with an arrogant cold look, chin raised, a small gold handbag on her arm; Layaali seated at the desk looking up at her, startled, a neat stack of blank files in front of her",
         camera="medium two-shot, slightly low angle on Ahna", amb="office_day"),
    dict(to=16, reason="focus moves to Layaali: her humble character and her family's need", chars=["layaali"], loc="finance_floor",
         visual="Layaali seated at her desk holding out a stack of blank files with both hands, a gentle humble half smile, soft modest eyes, warm golden light from the window on her face; colleagues blurred in the background",
         camera="medium close-up, eye level", amb="office_day"),
    dict(to=18, reason="Ahna takes the files and orders her (reuse of the desk confrontation)", reuse="beat_004",
         chars=["ahna", "layaali"], loc="finance_floor", visual="(reuse) Ahna over Layaali at her desk", amb="office_day"),
    dict(to=21, reason="scene change: they enter Rafhaan's cabin; he sees Layaali", chars=["rafhaan", "ahna", "layaali"], loc="cabin",
         visual="inside the glass cabin Rafhaan seated at his large desk, just looking up from his laptop with a softened, wondering gaze; Ahna striding in first holding the files with a confident smile; Layaali a step behind her near the open glass door, modest and shy",
         camera="wide shot from beside the desk", amb="office_quiet"),
    dict(to=24, reason="action change: Ahna lies; Layaali bows her head", chars=["ahna", "layaali"], loc="cabin",
         visual="Ahna standing in front of the executive desk speaking with a smug self-satisfied smile, one hand on her chest as if taking credit; just behind her Layaali standing with her head bowed and hands clasped, hurt and silent",
         camera="medium two-shot, eye level", amb="office_quiet", hum_note="her hurt"),
    dict(to=26, reason="focus change: Rafhaan sees through it", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan seated at his desk closing a blank file with one hand, looking up and straight ahead with a calm, discerning, quietly firm expression, warm window light on half of his face",
         camera="close-up, eye level", amb="office_quiet"),
    dict(to=29, reason="action change: Ahna is sent out and seethes outside the door", chars=["ahna"], loc="corridor",
         visual="Ahna standing just outside a closed frosted-glass door in the corridor, jaw clenched, eyes blazing with fury, her forced smile gone, fingers gripping her gold handbag tightly",
         camera="medium close-up, slightly low angle", amb="office_quiet"),
    dict(to=33, reason="action change: alone with Rafhaan, Layaali sits", chars=["rafhaan", "layaali"], loc="cabin",
         visual="Rafhaan seated behind his desk gesturing kindly with an open hand towards the guest chair; Layaali sitting across the desk at a respectful distance, gripping the strap of a small handbag on her lap, nervous and uncertain",
         camera="medium wide two-shot across the desk", amb="office_quiet"),
    dict(to=35, reason="emotional turning point: the first exchanged look", chars=["layaali"], loc="cabin",
         visual="close-up of Layaali lifting her eyes for a moment with a shy, moved expression, a soft warm glow on her face, the city window bright and blurred behind her",
         camera="close-up, eye level", amb="office_quiet", sens="romance",
         safe="the first spark of love shown only as her lifted gaze; no touch, Rafhaan off-frame"),
    dict(to=37, reason="symbolic image: 'he is the sky, she is the earth', stars shine in darkness", loc="sky",
         visual="a vast starry night sky over a calm dark sea, one bright star shining above, the faint lights of Malé low on the horizon, no people",
         camera="wide shot", amb="night_exterior", transition="dissolve"),
    dict(to=41, reason="scene and character change: Ahna calls her friends", chars=["ahna"], loc="corridor",
         visual="Ahna standing by the tall corridor window holding a phone to her ear, her face hard and hateful, eyes narrowed, the city skyline behind her",
         camera="medium shot", amb="office_quiet"),
    dict(to=43, reason="symbolic image: a storm of jealousy heading for Layaali as night falls", loc="storm",
         visual="heavy dark storm clouds rolling over the Malé skyline at dusk, the last purple light fading, city lights flickering on, wind on the dark water, no people",
         camera="wide shot", amb="night_exterior"),
    dict(to=45, reason="back in the cabin (reuse)", reuse="beat_011", chars=["rafhaan", "layaali"], loc="cabin",
         visual="(reuse) Rafhaan and Layaali across the desk", amb="office_quiet"),
    dict(to=48, reason="action change: she explains the report and he signs", chars=["rafhaan", "layaali"], loc="cabin",
         visual="Rafhaan signing an open blank file with an elegant pen, smiling with pride; Layaali seated across the desk with an open file of her own, speaking with quiet confidence",
         camera="medium two-shot, slightly high angle over the desk", amb="office_quiet"),
    dict(to=51, reason="focus change: Rafhaan's unease at 'sir'", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan leaning back in his leather chair, chin resting lightly on his hand, gazing across the desk with a faint wistful smile and a hint of unease, the elegant pen lying on the closed file",
         camera="medium close-up", amb="office_quiet"),
    dict(to=53, reason="action change: Layaali leaves the cabin, her heart racing; Ahna fuming", chars=["layaali", "ahna"], loc="finance_floor",
         visual="Layaali walking out of the glass cabin onto the finance floor, files hugged to her chest, a confused soft wonder on her face; far behind her in soft focus Ahna standing by a desk, glaring, her face flushed with anger",
         camera="medium shot, Layaali in the foreground", amb="office_day"),
    dict(to=57, reason="scene change: the posh café with Zoya and Raaya", chars=["ahna", "zoya", "raaya"], loc="cafe",
         visual="three women seated around a marble corner table in the upscale café, coffee cups in front of them: Ahna in the middle, sipping coffee with a sour displeased face; Zoya on one side with a mocking half smile; Raaya on the other, cold and attentive",
         camera="medium wide, eye level", amb="cafe"),
    dict(to=59, reason="focus change: Zoya proposes ruining Layaali's name", chars=["zoya", "ahna"], loc="cafe",
         visual="Zoya leaning back in her velvet chair admiring her long manicured nails with a sly mocking smile as she talks; Ahna beside her listening intently with narrowed eyes",
         camera="medium close-up two-shot", amb="cafe"),
    dict(to=62, reason="emotional turning point: the plot is set, Ahna's dangerous smile", chars=["ahna", "raaya"], loc="cafe",
         visual="Ahna in the foreground with a slow cold dangerous smile, eyes gleaming; Raaya leaning in close behind her shoulder, whispering the plan, the warm lamps casting deep shadows",
         camera="close-up, slightly low angle", amb="cafe"),
    dict(to=66, reason="scene change: Layaali's parents at home, worried", chars=["qaasim", "aminath"], loc="home",
         visual="frail Qaasim half-sitting against a pillow on the simple bed, a hand on his chest, worried and tired; Aminath seated on the edge of the bed beside him, her hand resting gently on his shoulder, a tender reassuring look",
         camera="medium shot, eye level", amb="home_night", sens="illness",
         safe="his coughing shown only as a hand on his chest and a weary face; no blood"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Rising into the sky among Malé's concrete buildings, the head office of 'Rafhaan Group' is not only a centre of business.")
sh(2, "It is a centre of thousands of hopes, of jealousy and secret plots. As the golden rays of the sun poured in through the great glass doors, inside the office there was bustle.")
sh(3, "Everyone's tongue was on one topic: the office's young, educated and kind-hearted boss, Rafhaan.")
sh(4, "The richest person in the world is not the one with a lot of money in hand. It is the owner of a rich heart that can sense the feelings of humble hearts.")
sh(5, "Rafhaan was a courageous young man who stood on his own feet and in a short time built a company with a name in the Maldivian market.")
sh(6, "His good looks, his manly walk and his smile were qualities that had stolen the sleep of many girls.",
   [("footsteps_pavement", "ހިނގުމާއި", -26)])
sh(7, "Many of the office's female employees hung on his every glance, his every word.")
sh(8, "But Rafhaan's thinking was in a completely different direction. He wanted to be a fair, kind and honest leader to every employee who worked under him.")
sh(9, "His heart loved humanity more than wealth. 'Layaali! Are today's financial reports ready?'")
sh(10, "At the voice, in a harsh tone, Layaali, sitting at a desk in one corner of the office, looked up startled. It was Ahna.",
   [("gasp", "ސިހިފައި", -22)])
sh(11, "The head of the office's finance department. Ahna was a beautiful girl from a wealthy family.")
sh(12, "In her heart were arrogance and pride. The scent of her expensive clothes and perfume filled the whole office.")
sh(13, "Rafhaan was Ahna's only goal. Not a day passed without her chasing after him. In her belief, she alone was fit for Rafhaan.")
sh(14, "'Yes, Ahna madam. All the files are prepared, ready to sign,' Layaali answered humbly.",
   [("paper_shuffle", "ފައިލްތަކެއް", -22)])
sh(15, "Layaali was an educated girl from a poor family. The simplicity and humility in her face had earned her the respect and love of all the other staff.")
sh(16, "In her heart there was hostility towards no one. Her only hope was to work well and help her father, lying on his sickbed, and her mother.")
sh(17, "Ahna carelessly took the files Layaali held out. 'Bring these files and come with me to the boss's cabin.",
   [("paper_shuffle", "ހިފިއެވެ", -20)])
sh(18, "Don't try to fool Rafhaan about your level.' Hating Layaali from the depths of her heart, Ahna gave the order arrogantly.")
sh(19, "The two went together and stopped at the door of Rafhaan's luxury cabin. Ahna knocked and went in.",
   [("footsteps_pavement", "ގޮސް", -24), ("knock", "ޓަކިޖަހާލުމަށްފަހު", -14), ("door_open", "ވަނެވެ", -20)])
sh(20, "Rafhaan sat at his big desk, eyes fixed on his laptop. When he looked up and saw Layaali behind Ahna, a completely different life came into his eyes.",
   [("keyboard_typing", "ލެޕްޓޮޕަށް", -24)])
sh(21, "It was a look of humility mixed with a kind of wonder. 'Ahna, did you bring today's reports?'")
sh(22, "Rafhaan's voice was calm, yet firm. 'Yes. I stayed up last night checking these reports.")
sh(23, "Layaali had made some mistakes, so I corrected all of it myself.' Ahna's lie hurt Layaali's heart.", hum=True)
sh(24, "But she stood with her head bowed and said nothing. Speaking against a superior was not something her manners allowed.")
sh(25, "Rafhaan looked at the files. He knew the standard of Layaali's work. He was certain Layaali never worked carelessly.",
   [("page_turn", "ފައިލްތަކަށް", -20)])
sh(26, "After closing the file he looked straight into Layaali's eyes. 'Layaali, I want to hear the details of these reports from Layaali herself.",
   [("page_turn", "ލައްޕާލުމަށްފަހު", -20)])
sh(27, "Ahna, please wait outside,' Rafhaan said. The colour of Ahna's face changed at once. A fire of anger flared up in her heart.")
sh(28, "But so as not to show it in front of Rafhaan, she forced a smile and walked out of the cabin. As the door shut, Ahna's teeth clenched.",
   [("footsteps_pavement", "ނިކުތެވެ", -24), ("door_close", "ލެއްޕުނު", -16)])
sh(29, "'I'll ruin your days, Layaali.' Ahna kept cursing Layaali inwardly. Inside the cabin there was a deep silence.")
sh(30, "Layaali felt uneasy. 'Sit down, Layaali.' Rafhaan kindly gestured to the chair in front of him.")
sh(31, "Layaali slowly sat down and gripped the strap of her little bag tightly. 'As madam said, I...' Layaali tried to speak.",
   [("cloth_rustle", "އިށީނދެ", -24)])
sh(32, "'I know Ahna lied.' Rafhaan cut her short. 'I have no complaint at all about Layaali's work.")
sh(33, "I consider Layaali one of the most valuable employees of this office. And... the owner of the most honest heart.'")
sh(34, "At those words Layaali's heart beat faster. When she raised her head and looked into Rafhaan's eyes, what she saw there was not just a boss's respect.",
   [("heartbeat", "ހިނގުން", -18)], hum=True)
sh(35, "It was a deeper, more moving feeling. Those were the first rays of love. But Layaali lowered her gaze at once.", hum=True)
sh(36, "Her heart reminded her of the great invisible line between them. Rafhaan is the sky. She is the earth.")
sh(37, "The stars in the sky shine brighter the darker the night grows. Layaali did not know that, in the same way, the beauty of honest hearts shines out even from a sea of poverty.")
sh(38, "Stepping out of the office, Ahna immediately took her phone and called her closest 'devil' friends, Zoya and Raaya.",
   [("footsteps_pavement", "ނިކުމެ", -24)])
sh(39, "The three of them were influential among Malé's rich, but given to wicked scheming. 'Zoya! Raaya!")
sh(40, "I want to meet you two right now. That beggarly little saint is trying to snatch my Rafhaan.")
sh(41, "We have to plan how to get her out of the office and ruin her life.' Ahna's voice carried a dangerous tone of hatred and jealousy.")
sh(42, "As the pitch darkness of night settled over Malé, a great storm of jealousy had set its course for Layaali's life, and she",
   [("wind_gust", "ތޫފާނެއް", -20)], hum=True)
sh(43, "did not know it. Will the love born in Rafhaan's heart bring Layaali happiness? Or is it the beginning of her ruin?", hum=True)
sh(44, "The silence that had fallen in the big office cabin made Layaali's heart uneasy.")
sh(45, "The kindness in Rafhaan's eyes and the words of praise from his lips were things Layaali had never once expected in her life.")
sh(46, "She took a deep breath and began explaining the details of the report. Listening to her perfectly ordered explanation, Rafhaan sat proud of the company's future.",
   [("sigh", "ނޭވާއެއްލުމަށްފަހު", -22)])
sh(47, "'Excellent, Layaali. I'm signing this right now,' Rafhaan said, signing the file with his expensive pen.",
   [("pen_scribble", "ސޮއިކޮށްލަމުން", -18)])
sh(48, "'Do you know, Layaali? Most of the staff here work only for the salary. But Layaali's work shows sincerity.'")
sh(49, "'Thank you, sir. My father always says: do every job honestly, and then it will be blessed.'")
sh(50, "Layaali said humbly. When Layaali called him 'sir', Rafhaan felt a little uncomfortable.")
sh(51, "He wanted Layaali to speak to him more closely. But he understood that, because of his position and the office setting, it could not be so.")
sh(52, "As Layaali left the cabin with the files, her heart was beating harder than usual.",
   [("footsteps_pavement", "ނިކުތްއިރު", -24), ("heartbeat", "ތެޅެމުންދިޔައީ", -18)], hum=True)
sh(53, "What kind of feeling it was, she herself could not tell. When she came out of the office, Ahna stood red with anger.")
sh(54, "She went straight to an expensive café in Malé and met her 'devil' friends, Zoya and Raaya.")
sh(55, "Sitting at a table in a corner of the café, the three of them talked of nothing but Layaali.")
sh(56, "'I've never seen Rafhaan look at another girl like that,' Ahna said, displeased, sipping from her coffee cup.",
   [("cup_clatter", "ކޮފީފޮދެއް", -20)])
sh(57, "'That poor simple little saint is now trying to win Rafhaan's heart. I won't give her any room for that.' Ahna's face had turned dark and ugly. 'Mind it, Ahna.'")
sh(58, "Zoya said, looking at her long nails. 'Getting girls like that out of the office is no big deal. We have to destroy her reputation.")
sh(59, "What does Rafhaan hate most? Injustice and theft. Shouldn't we pin a theft accusation on her?' 'That's a good idea.'")
sh(60, "Raaya agreed. 'When a big money transaction for an important office project is going through, we'll frame Layaali in it.")
sh(61, "Then Rafhaan himself will fire her.' A dangerous smile spread across Ahna's face.")
sh(62, "The whirlpool of jealousy towards Layaali in her heart had grown strong. She was ready to smash Layaali's life to pieces in the waves of that sea.", hum=True)
sh(63, "At that moment, in an ordinary small house in Malé, Layaali's mother Aminath and her father Qaasim sat worried.")
sh(64, "Qaasim had lain on a sickbed for many days. His treatment cost a great deal every month. 'Aminath... is Layaali still not home?")
sh(65, "She works so hard for our sake,' Qaasim said, coughing. 'Don't worry, Qaasim. Our daughter is a very strong girl.",
   [("breath_heavy", "ކެއްސަމުން", -24)], hum=True)
sh(66, "She studied so that she could stand on her own feet,' Aminath said, stroking her husband's head.")
SHOTS = S

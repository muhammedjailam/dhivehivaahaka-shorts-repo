"""Beat/shot plan for Tedhuveriloabi episode 479 (used by plan_beats.py)."""

LOC = {
    "hospital_sunset": "a quiet upper-floor corridor of ADK Hospital in Malé at sunset, cool white walls and floor, a large window glowing with warm orange sunset light over the city rooftops and the sea",
    "zaahir_office": "a dark, luxurious private office in a Malé tower at dusk, a heavy dark wooden desk, a leather chair, a tall window with the first city lights of Malé behind",
    "car": "inside a dark luxury car driving through the busy streets of Malé at dusk, city lights and motorbikes blurred outside the windows",
    "ward": "a calm general ward of ADK Hospital in Malé, a single hospital bed with clean white sheets, pale walls, a bedside cabinet with a jug of water, soft daylight through a window",
    "office_floor": "the open-plan finance floor of the Rafhaan Group glass high-rise in Malé in the morning, rows of white desks with computer monitors, glass partition walls, a glass-walled CEO cabin at the far end",
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin in the Rafhaan Group high-rise, a large dark wooden desk with a closed laptop and a phone, a black leather chair, floor-to-ceiling windows over Malé and the turquoise sea",
    "mansion_day": "the spacious sitting room of a large modern mansion in Malé in the daytime, cream sofas, a glass coffee table, a wide curved staircase with a glass railing, tall windows with sheer curtains",
    "lobby": "the bright glass main entrance lobby of the Rafhaan Group high-rise in Malé, tall glass doors, polished pale stone floor, morning daylight",
    "office_late": "a meeting table in the Rafhaan Group office late at night, laptops and stacks of blank paper files, desk lamps, dark glass windows with the night lights of Malé behind",
    "boardroom": "an elegant boardroom in the Rafhaan Group high-rise in the daytime, a long polished table, glass walls, a bright view of Malé and the sea",
    "office_golden": "the finance floor of the Rafhaan Group high-rise in the late afternoon, golden sunlight streaming through big glass doors and windows, long warm light on the floor",
    "harbour": "the sea off Malé harbour, dark storm clouds breaking apart, golden sunlight bursting through onto calm water, a few traditional dhonis safely moored at the harbour",
    "custody": "a bare, plain grey police custody room in Malé, a simple bench against the wall, a small high window letting in a thin shaft of cold light",
    "lane": "a dark narrow lane in Malé at night, old low-walled houses with closed doors, one dim streetlight, a sleek expensive black car parked in the shadows",
    "raaya_car": "inside an expensive black car parked in a dark Malé lane at night, leather seats, faint streetlight through the windows, a soft dashboard glow",
    "mansion_night": "the spacious sitting room of the large modern mansion in Malé in the evening, warm lamp light, cream sofas, a wide curved staircase with a glass railing, night city lights through tall windows",
}
MOOD = {
    "hospital_sunset": "sunset, warm amber and rose light through the window, soft, shy and tender",
    "zaahir_office": "dusk, low-key light, cold blue shadows with a hard amber lamp glow, menacing",
    "car": "dusk, passing city lights flickering over his face, pensive and uneasy",
    "ward": "soft morning daylight, pale and peaceful, relief",
    "office_floor": "cool morning light, muted colours, a tense heavy silence",
    "cabin": "bright but cold daylight, tense, alarming news",
    "mansion_day": "daylight through sheer curtains, cool tones, tense family conflict",
    "lobby": "bright morning daylight, cool tones, worried",
    "office_late": "night, warm desk lamps against dark blue windows, focused determination",
    "boardroom": "bright daylight, crisp and hopeful",
    "office_golden": "late afternoon, rich golden light, warm, joyful and tender",
    "harbour": "storm clearing, dramatic sky, golden hopeful light",
    "custody": "cold grey light, deep shadows, ominous",
    "lane": "night, one dim yellow streetlight, deep blue shadows, ominous",
    "raaya_car": "night, cold blue shadows, faint glow on her face, sinister",
    "mansion_night": "evening, warm lamp light, calm and hopeful with lingering tension",
}

BEATS = [
    dict(to=1, reason="new episode opening: the end of ep 456 at the hospital, Layaali calls him by name", chars=["layaali", "rafhaan"], loc="hospital_sunset",
         visual="Layaali and Rafhaan standing a respectful distance apart by the big sunset window in the hospital corridor; Layaali lowering her head shyly with a small smile, her hands clasped; Rafhaan looking at her with a warm, happy smile; calm empty floor in the lower third",
         camera="medium two-shot, eye level", amb="hospital_corridor"),
    dict(to=3, reason="character change: focus moves to Ahmed Zaahir plotting revenge", chars=["zaahir"], loc="zaahir_office",
         visual="Ahmed Zaahir standing at the tall window of his dark office, a phone lowered in his hand, his heavy face cold and furious, eyes narrowed in a vengeful plan; his reflection faint in the glass",
         camera="medium close-up, low angle", amb="office_night"),
    dict(to=4, reason="scene change: Rafhaan driving through Malé after leaving the hospital", chars=["rafhaan"], loc="car",
         visual="Rafhaan at the wheel of his dark car, seen through the windscreen, his face pensive and uneasy, city lights sliding across the glass",
         camera="medium close-up through the windscreen", amb="car_interior"),
    dict(to=6, reason="scene change: Qaasim moved from the ICU to the ward (the relief in Rafhaan's thoughts)", chars=["qaasim", "aminath"], loc="ward",
         visual="Qaasim resting propped up on pillows in the ward bed, weak but calm, a faint relieved smile; Aminath sitting on a chair beside the bed, holding his hand, her face relieved and grateful",
         camera="medium wide, eye level", amb="hospital_room"),
    dict(to=8, reason="back to Rafhaan in the car, worrying about Zaahir (reuse)", reuse="beat_003", chars=["rafhaan"], loc="car",
         visual="(reuse) Rafhaan driving, pensive", amb="car_interior"),
    dict(to=10, reason="time jump: the next morning, the silent office", chars=["rafhaan"], loc="office_floor",
         visual="Rafhaan walking between rows of desks on the finance floor towards his glass cabin, his face serious; office staff in modest clothes sitting silently at their desks, glancing up anxiously; calm floor in the lower third",
         camera="wide shot, eye level", amb="office_quiet", transition="black"),
    dict(to=16, reason="characters change: Aasim bursts into the cabin with bad news", chars=["aasim", "rafhaan"], loc="cabin",
         visual="inside the glass cabin Aasim standing at the desk, setting down an open laptop whose screen faces away from the viewer, his face anxious; Rafhaan rising from his leather chair behind the desk, alarmed and grim; a phone lying on the desk",
         camera="medium two-shot", amb="office_day"),
    dict(to=17, reason="character change: Khadeeja shouting on the phone at the mansion", chars=["khadeeja"], loc="mansion_day",
         visual="Khadeeja standing in the mansion sitting room holding a phone to her ear, her face furious and distressed, her other hand raised in agitation",
         camera="medium close-up", amb="mansion_day"),
    dict(to=18, reason="back to the cabin: Rafhaan gives Aasim instructions (reuse)", reuse="beat_007", chars=["aasim", "rafhaan"], loc="cabin",
         visual="(reuse) Rafhaan and Aasim in the cabin", amb="office_day"),
    dict(to=21, reason="action and character change: Rafhaan leaving meets Layaali at the main door", chars=["rafhaan", "layaali"], loc="lobby",
         visual="at the glass main doors of the lobby Rafhaan striding out, his face tense and worried, as Layaali arriving for work stops in front of him a respectful distance away, looking at him with concern; calm polished floor in the lower third",
         camera="medium wide two-shot", amb="office_day"),
    dict(to=24, reason="emotional turn: Layaali blames herself", chars=["layaali", "rafhaan"], loc="lobby",
         visual="Layaali with downcast, disappointed eyes glistening, her hands clasped tightly in front of her; Rafhaan standing a respectful distance away looking at her with a worried face",
         camera="medium close two-shot", amb="office_day", hum_note="emotional"),
    dict(to=27, reason="action change: Rafhaan reassures her, she nods", chars=["rafhaan", "layaali"], loc="lobby",
         visual="Rafhaan, a respectful distance from Layaali, speaking to her with a firm, reassuring face, one open hand raised slightly as he speaks; Layaali looking up at him with respect and quiet trust, nodding",
         camera="medium two-shot, over Layaali's shoulder", amb="office_day", sens="intimacy",
         safe="he holds her shoulder in the narration; shown as reassurance at a respectful distance, no touch (not married yet)"),
    dict(to=33, reason="scene change: the mansion, Khadeeja in tears, Ibrahim worried", chars=["khadeeja", "rafhaan", "ibrahim"], loc="mansion_day",
         visual="Khadeeja standing up from the cream sofa with a tear-streaked angry face confronting Rafhaan; Rafhaan standing firm with a raised, serious face; Ibrahim seated on the sofa behind, worried, hands on his knees",
         camera="medium wide, eye level", amb="mansion_day"),
    dict(to=36, reason="time jump: working late into the night on the investor proposals", chars=["layaali", "rafhaan", "aasim"], loc="office_late",
         visual="Layaali, Rafhaan and Aasim working late at a meeting table under desk lamps; Layaali explaining a blank paper plan with a pen, Rafhaan and Aasim listening attentively across the table, laptop screens facing away; table top in the lower third",
         camera="medium wide, slightly high angle", amb="office_night", transition="black"),
    dict(to=38, reason="time jump and character change: the third day, meeting the foreign investor representative", chars=["rafhaan"], loc="boardroom",
         visual="in the boardroom a middle-aged foreign businessman with greying hair in a light-grey suit leafing through a bound business plan with blank pages, impressed and smiling; Rafhaan sitting across the table, hopeful; polished table top in the lower third",
         camera="medium two-shot across the table", amb="office_day", transition="black"),
    dict(to=40, reason="scene change: Rafhaan brings Layaali the happy news in the golden afternoon office", chars=["rafhaan", "layaali"], loc="office_golden",
         visual="in golden afternoon light by the big glass doors Rafhaan standing before Layaali at a respectful distance, smiling with joy; Layaali with happy tears in her eyes, a hand on her chest, smiling",
         camera="medium wide two-shot, backlit", amb="office_day"),
    dict(to=41, reason="emotional turning point: the proposal", chars=["rafhaan", "layaali"], loc="office_golden",
         visual="close two-shot: Rafhaan looking at Layaali with an earnest, hopeful face as he asks her to marry him, standing a respectful distance away; Layaali surprised, eyes wide, both hands pressed together at her chest, golden light between them",
         camera="close two-shot, profile", amb="office_day"),
    dict(to=42, reason="symbolic image: not every storm is destruction, some bring life to a safe harbour", loc="harbour",
         visual="dark storm clouds over the sea off Malé breaking apart, golden sunbeams bursting through onto calm water, a few dhonis safely moored in the harbour; no people",
         camera="wide shot", amb="beach_evening", transition="dissolve"),
    dict(to=44, reason="action change: Layaali smiles and nods yes", chars=["layaali"], loc="office_golden",
         visual="close-up of Layaali lowering her eyes shyly with a soft happy smile, nodding, golden light on her face, a happy tear on her lashes",
         camera="close-up", amb="office_day"),
    dict(to=45, reason="character and scene change: Ahna in custody plotting through Raaya", chars=["ahna"], loc="custody",
         visual="Ahna sitting alone on a plain bench in a bare grey custody room, no makeup glow, her face cold and scheming, eyes narrowed towards the small high window, a thin shaft of light across her",
         camera="medium shot, slightly low angle", amb="room_night", sens="other",
         safe="custody shown as a plain room; no bars, no handcuffs emphasised"),
    dict(to=46, reason="back to the golden happy office (reuse)", reuse="beat_016", chars=["rafhaan", "layaali"], loc="office_golden",
         visual="(reuse) golden office", amb="office_day"),
    dict(to=48, reason="back to Layaali's peaceful smile (reuse)", reuse="beat_019", chars=["layaali"], loc="office_golden",
         visual="(reuse) Layaali's shy smile", amb="office_day"),
    dict(to=50, reason="scene and time change: a dark lane of Malé at night", loc="lane",
         visual="a dark narrow lane in Malé at night, an expensive black car parked in the shadows outside an old house, one dim streetlight, no people",
         camera="wide shot, eye level", amb="street_night", transition="black"),
    dict(to=54, reason="character change: Raaya on the phone in her car", chars=["raaya"], loc="raaya_car",
         visual="Raaya sitting in the driver's seat of her parked car holding a phone to her ear, her face cold and hard, eyes dangerous, half in shadow",
         camera="medium close-up through the side window", amb="car_night", sens="violence",
         safe="the murder plot is only spoken; shown as a cold face on a phone call, no weapon, no victim"),
    dict(to=57, reason="emotional turn: Raaya's wicked half-smile as she chooses the hospital", chars=["raaya"], loc="raaya_car",
         visual="close-up of Raaya's face in the dark car, a wicked one-sided smile, her eyes glinting in the faint streetlight, phone at her ear",
         camera="close-up", amb="car_night", sens="violence", safe="plot to harm Layaali in the hospital shown only as Raaya's sinister smile"),
    dict(to=60, reason="scene change: at home Rafhaan tells his father about Layaali", chars=["ibrahim", "rafhaan"], loc="mansion_night",
         visual="Ibrahim and Rafhaan sitting side by side on the cream sofa in the evening; Ibrahim smiling warmly with his hand resting on his son's shoulder; Rafhaan relieved and grateful",
         camera="medium two-shot, eye level", amb="mansion_night"),
    dict(to=62, reason="character change: Khadeeja comes down the stairs", chars=["khadeeja", "rafhaan", "ibrahim"], loc="mansion_night",
         visual="Khadeeja standing on the lower steps of the curved staircase with a displeased, reluctant face, turning her head away; Rafhaan and Ibrahim on the sofa in the foreground looking up at her",
         camera="medium wide, from behind the sofa", amb="mansion_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "'Rafhaan,' Layaali called softly, shyly. She lowered her head in shyness. But her smile gave Rafhaan his answer.")
sh(2, "But they did not know that behind this happy moment another danger was waiting.", hum=True)
sh(3, "Ahna's father Ahmed Zaahir, on hearing that his daughter had been arrested, has already begun planning to bankrupt Rafhaan's whole company.")
sh(4, "Rafhaan did not yet know how dangerous Ahmed Zaahir was. Leaving the cold air of the hospital, as Rafhaan's car moved through the streets of Malé, turning in his mind was",
   [("car_pass", "މަގުތަކުގެ", -22)])
sh(5, "an unease. That Layaali's father Qaasim had recovered somewhat and been moved from the ICU to the ward was a great relief.")
sh(6, "And with Ahna's guilt proven and her taken into police custody, the black stain of disgrace on Layaali's head was washed away completely.")
sh(7, "But Rafhaan was thinking about the great danger ahead. The power and influence of Ahna's father Ahmed Zaahir could shake Malé's whole business market.")
sh(8, "Zaahir would never let his only daughter Ahna go behind prison bars. And Rafhaan was sure he would not hesitate to tear 'Rafhaan Group' to pieces in revenge.")
sh(9, "The next morning, when Rafhaan came to the office, a frightening silence lay over the whole office.")
sh(10, "The staff sat silent by their desks. Just as Rafhaan entered his cabin and sat down, IT head Aasim opened the door and came in, his face full of worry.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(11, "'Boss! There's a big problem.' Aasim's voice was trembling. 'What happened, Aasim?' Rafhaan stood up.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(12, "'Zaahir's company sent an official letter to the bank this morning. They want to withdraw their forty percent share immediately.")
sh(13, "And besides that, boss, Zaahir has called the main investors of the Seaview Resort project we're starting next month.")
sh(14, "They say they're now reluctant to work with our company,' Aasim said, setting a laptop on the desk.",
   [("soft_thud", "ބަހައްޓަމުން", -22)])
sh(15, "Rafhaan's head spun. Pulling forty percent of the shares out at once was like breaking the company's foundation.",
   [("heartbeat", "އެނބުރުން", -18)], hum=True)
sh(16, "This was Zaahir's revenge for the three-day deadline he had given. At that moment Rafhaan's phone began to ring. It was his mother, Khadeeja. 'Rafhaan!",
   [("phone_buzz", "ރިންގްވާން", -14)])
sh(17, "What a thing have you done? Because you sent Zaahir's daughter to jail, my son is now out on the street, isn't he? Come home right now!'")
sh(18, "Khadeeja shouted down the phone. 'Aasim, prepare all the financial records. And make an appointment to meet the bank manager.")
sh(19, "I'm going home.' Rafhaan let out a deep breath. Then he left the cabin and walked quickly to leave the office.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -20), ("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(20, "As he was going out through the main door he ran into Layaali. Layaali was in her office clothes. Today she had come to work with new hope.",
   [("door_open", "ދޮރުން", -22)])
sh(21, "But Layaali noticed the worry on Rafhaan's face. 'Rafhaan... what happened?' Layaali asked softly.")
sh(22, "Hearing her call him by his name for the first time, Rafhaan's heart found a little peace. 'Layaali... a big storm is coming to the company.")
sh(23, "Zaahir is taking his shares back. I'm going home to see my mother,' Rafhaan said. 'This happened because of me.'")
sh(24, "Disappointment showed in Layaali's eyes. 'Because of me Rafhaan is losing everything,' Layaali said again. 'No, Layaali.", hum=True)
sh(25, "Don't ever think like that.' Rafhaan gently held Layaali's shoulder. 'Work done for the sake of justice will never bring loss.")
sh(26, "Layaali, stay at the office. Look after the finance section. Layaali is the only one I trust.' Layaali nodded.")
sh(27, "In her heart, her love and respect for Rafhaan grew stronger. When Rafhaan got home, Khadeeja was sitting in the living room crying.",
   [("sob_breath", "ރޮވިފައެވެ", -24)])
sh(28, "Rafhaan's father Ibrahim Faahim sat there worried too. 'Rafhaan! What are you doing?' Khadeeja stood up.")
sh(29, "'Zaahir says if Ahna's case is withdrawn instead of going to court, and you agree to the marriage, he'll keep his shares. And he'll fund the new project too.")
sh(30, "That's what you must do!' 'Mother! Do you know what a terrible crime Ahna committed?' Rafhaan's voice rose.")
sh(31, "'She tried to frame a poor girl and send her to jail. And she did things that put a sick man's life in danger.")
sh(32, "I will never marry a woman like that.' 'So you want to end up on the street?' Khadeeja shouted.", hum=True)
sh(33, "'Mother, God willing this company will be saved,' Rafhaan said firmly. 'I'll find new investors.'")
sh(34, "There was resolve in Rafhaan's voice. Rafhaan went back to the office with a new determination.")
sh(35, "He, Layaali and Aasim worked together at the office late into the night. The new proposals for foreign investors to fix the company's finances were prepared through Layaali's hard work.",
   [("keyboard_typing", "މަސައްކަތްކުރިއެވެ", -22)])
sh(36, "Layaali's intelligence and education were a great help to Rafhaan at this moment. On the third day Rafhaan met the Maldives representative of a big foreign company.")
sh(37, "They were amazed when they saw the business plan Layaali had prepared. 'This is an excellent plan, Rafhaan,' the representative said.",
   [("page_turn", "ބަލާފައި", -22)])
sh(38, "'We are ready to buy the forty percent share of your company. And we will fully fund the Seaview Resort project.' Rafhaan's heart filled with joy.")
sh(39, "Zaahir's evil plan was shattered. The company was saved. Rafhaan came straight to the office and gave Layaali the happy news.")
sh(40, "Tears of joy began to show in Layaali's eyes. 'Without Layaali I could never have done this.' Rafhaan stopped in front of Layaali.", hum=True)
sh(41, "'Now all the storms have passed. I want to begin a new chapter of our lives. Layaali, will you marry me?'", hum=True)
sh(42, "Not every storm in life is destruction. Some storms come to make the foundation of true love stronger and to carry life to a safe harbour.",
   [("wind_gust", "ތޫފާނަކީ", -22), ("wave_crash", "ބަނދަރަކަށް", -24)])
sh(43, "This time just such a storm had come into Rafhaan's life. Because of that storm he gained even more courage. Layaali stood there shy.")
sh(44, "But it was what Layaali wanted too. Smiling, Layaali nodded. It was the happiest moment of her life.", hum=True)
sh(45, "But what they did not know was that Ahna, in jail, was planning through her 'devil' friend Raaya one last dangerous attack on Layaali's life.",
   [("heartbeat", "ހަމަލާ", -18)])
sh(46, "It was a frightening plan that would put Layaali's life in danger. With the golden afternoon rays pouring in through the office's big glass doors, an unusual happiness filled the whole place.")
sh(47, "With the joy of the company being saved and the high place she had won in Rafhaan's heart, Layaali's face showed a beautiful smile")
sh(48, "of peace. She had nodded to Rafhaan's proposal, accepting that love from the very depth of her heart.")
sh(49, "But in a dark lane of Malé, outside a house, plans of a different kind were being made.")
sh(50, "Even though Ahna was in police custody, the influence of her power and money had not been cut off completely.")
sh(51, "Of her 'devil' friends, Raaya was a cruel woman who always did whatever Ahna said. Raaya sat in her expensive car, talking to someone on the phone.")
sh(52, "A dangerous look showed in her eyes. 'Even if Ahna is in jail, I'll finish what she wants.'")
sh(53, "Raaya said to the person on the other end of the phone. 'Because of that Layaali our group lost its standing. Rafhaan must not be allowed to marry her.")
sh(54, "I want to wipe every trace of her from this world. Can you do it?' 'If there's money, anything can be done,' came a heavy, dangerous man's voice from the other end.",
   [("heartbeat", "ނުރައްކާތެރި", -18)], hum=True)
sh(55, "'Should I arrange an accident while she's walking on the road?' 'No. This has to be done more secretly.",
   [("brake_screech", "އެކްސިޑެންޓެއް", -22)])
sh(56, "In a way the police won't suspect.' A wicked glint showed in Raaya's eyes. Then she smiled with one corner of her mouth. 'Her father is in the hospital.")
sh(57, "Layaali is always there. Plan something inside the hospital.' Meanwhile, at home, Rafhaan sat talking with his father Ibrahim Faahim and told him about Layaali.")
sh(58, "Ibrahim was a kind-hearted man who loved justice. Hearing about Layaali's hard work, he was very happy. 'My son, Rafhaan...")
sh(59, "I know the company was saved today because of that girl.' Ibrahim laid his hand on Rafhaan's shoulder.",
   [("cloth_rustle", "އަތްބާއްވައިލިއެވެ", -24)])
sh(60, "'However angry your mother is, your father is with you. That is the very best choice. Tomorrow we'll go to their house and formally talk about the marriage.'")
sh(61, "Just then Khadeeja came down the stairs. Her face still showed displeasure. But knowing Zaahir's wickedness and the truth of Ahna's crimes, she had no room left to say anything.",
   [("footsteps_pavement", "ފައިބައިގެން", -22)])
sh(62, "'Rafhaan... do as you like. I have nothing to say. But I'm not at all happy about joining that poor family,' Khadeeja said, and turned away.",
   [("cloth_rustle", "އެނބުރުނެވެ", -24)])
SHOTS = S

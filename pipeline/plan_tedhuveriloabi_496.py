"""Beat/shot plan for Tedhuveriloabi episode 496 (used by plan_beats.py)."""

LOC = {
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin high in a modern glass office tower in Malé, a large dark-wood executive desk with a black leather chair, two guest chairs, floor-to-ceiling glass with a view over the city rooftops and the turquoise sea",
    "sitting": "the spacious sitting room of a large modern family mansion in Malé, cream sofas, a soft beige rug, a low wooden coffee table, a side table in the corner, tall windows with sheer curtains",
    "ahna_car": "inside a sleek black luxury car parked in a quiet Malé street, cream leather seats, tinted windows, the street softly blurred outside",
    "naasif_office": "a small cramped legal office in Malé, a cluttered desk with stacks of plain folders, closed window blinds, a desk lamp",
    "bank_back": "a narrow back lane behind a bank archive building in Malé late at night, a plain grey steel back door in a concrete wall, a single dim lamp above it, wet ground",
    "archive": "a bank archive room with tall grey metal shelves and storage boxes, seen through a closed glass door from a dark corridor",
    "bank_office": "a formal bank manager's office in Malé, a polished desk, a glass partition, grey filing cabinets, plain walls",
    "sitting_night": "the spacious sitting room of a large modern family mansion in Malé at night, cream sofas, a soft beige rug, a low wooden coffee table, a side table in the corner, table lamps glowing, dark windows",
    "lobby": "the bright glass reception corridor of a modern corporate office tower in Malé, polished pale floor, glass walls, potted palms",
    "cabin_morning": "Rafhaan's luxurious glass-walled CEO cabin in a modern glass office tower in Malé, a large dark-wood executive desk, leather chairs, floor-to-ceiling glass with a city and sea view",
}
MOOD = {
    "cabin": "bright daylight through the glass walls with a warm golden edge, tense and serious",
    "sitting": "warm late-afternoon sunlight through sheer curtains, a deceptively calm, polite atmosphere",
    "ahna_car": "late afternoon, shadowy interior, cool light from the tinted windows on her face, scheming and menacing",
    "naasif_office": "dusk, dim amber desk-lamp light, stripes of shadow from the blinds, shady and conspiratorial",
    "bank_back": "deep night, dark blue shadows, one weak yellow lamp, silent and ominous",
    "archive": "night, a strong orange glow inside the room against the dark blue corridor, ominous and still",
    "bank_office": "morning, cool grey-white light, heavy and shocked",
    "sitting_night": "night, warm amber lamplight, deep shadows, a heavy fearful silence",
    "lobby": "bright cold morning light, sharp reflections on glass, confident and threatening",
    "cabin_morning": "cold morning light, muted plum and grey tones, breath-holding tension",
}

BEATS = [
    dict(to=4, reason="new episode opening: Aasim warns Rafhaan about Ahna's contract in the cabin", chars=["aasim", "rafhaan"], loc="cabin",
         visual="Aasim sitting at the large desk with a thick contract open in front of him (blank pages, no text), looking up with a grave serious face; Rafhaan standing beside the desk, one hand on its edge, his jaw clenched in anger, the city behind the glass",
         camera="medium two-shot, eye level", amb="office_day"),
    dict(to=8, reason="action change: Aasim reports on the bank records and Rafhaan phones the lawyer and police", chars=["rafhaan", "aasim"], loc="cabin",
         visual="Rafhaan standing by the glass wall holding a phone to his ear with a determined face; Aasim behind him at the desk with an open laptop whose screen faces away from the viewer, watching him",
         camera="medium shot, slightly low angle", amb="office_day"),
    dict(to=11, reason="scene and time change: that afternoon Ahna brings a toy box to the house", chars=["ahna", "layaali"], loc="sitting",
         visual="Ahna standing in the mansion sitting room holding out a large plain cardboard toy box tied with a pink ribbon (no printing) with a sweet false smile; Layaali facing her, polite but cautious, reaching to take the box",
         camera="medium two-shot, eye level", amb="mansion_day", transition="black"),
    dict(to=14, reason="action change: the box sits in the sitting room and Ahna leaves, smug", chars=["ahna"], loc="sitting",
         visual="in the foreground on a side table in the corner, the large plain cardboard toy box with a pink ribbon; in the soft-focus background Ahna at the doorway, glancing back over her shoulder at the box with a sly, satisfied smile",
         camera="medium wide, the box in the foreground", amb="mansion_day"),
    dict(to=15, reason="scene change: Ahna in her car listening through the hidden microphone", chars=["ahna"], loc="ahna_car",
         visual="Ahna sitting in the back seat of her car with an open laptop on her knees (screen facing away from the viewer), a small wireless earpiece in her ear under the hijab, listening intently with narrowed eyes",
         camera="medium close-up through the car interior", amb="car_interior"),
    dict(to=17, reason="scene and character change: Rafhaan rushes home with the news of the court order", chars=["rafhaan", "layaali"], loc="sitting",
         visual="Rafhaan just through the doorway of the sitting room, slightly out of breath, face lit with excitement, both hands raised in an eager gesture; Layaali turning towards him from the sofa with surprised, hopeful eyes; the cardboard toy box with a pink ribbon on the side table behind them",
         camera="medium two-shot", amb="mansion_day", sens="touch",
         safe="the narration has him take her hand; they are married, but shown standing facing each other without hand-holding"),
    dict(to=19, reason="back to Ahna in the car, now furious (reuse)", reuse="beat_005", chars=["ahna"], loc="ahna_car",
         visual="(reuse) Ahna listening in her car", amb="car_interior"),
    dict(to=21, reason="action change: Ahna phones Naasif", chars=["ahna"], loc="ahna_car",
         visual="close-up of Ahna in the car holding a phone to her ear, eyes cold and dangerous, lips pressed tight, the laptop closed on her knees",
         camera="close-up", amb="car_interior"),
    dict(to=23, reason="character change: Naasif receives the order", chars=["naasif"], loc="naasif_office",
         visual="Naasif sitting behind his cluttered desk, phone at his ear, leaning back with a sly assured smile, his leather briefcase on the desk",
         camera="medium shot", amb="office_quiet"),
    dict(to=25, reason="time and scene change: late at night a masked intruder enters the bank archive", loc="bank_back",
         visual="a man in a dark hooded jacket, dark trousers and dark sneakers, seen only from behind as a dark silhouette, slipping through the half-open steel back door into darkness, broad male shoulders, no face visible",
         camera="wide shot from behind", amb="bank_night", transition="black", sens="crime",
         safe="the intruder is only a dark silhouette from behind; no weapon, no face"),
    dict(to=27, reason="action change: the original files are destroyed", loc="archive",
         visual="an empty archive room seen through a closed glass door from the dark corridor, an orange glow and thin wisps of smoke inside among the metal shelves, no people",
         camera="medium wide, eye level through the glass door", amb="bank_night", sens="fire/crime",
         safe="the burning is shown only as an orange glow in an empty room behind glass, no person, no flames on documents in close-up"),
    dict(to=31, reason="time and scene change: next morning at the bank, the manager reports the fire", chars=["rafhaan", "aasim"], loc="bank_office",
         visual="a middle-aged Maldivian bank manager in a grey suit sitting behind his desk with his head bowed; Rafhaan standing in front of the desk, stunned and pale; Aasim beside him with his mouth slightly open in shock; a Maldivian police officer in a plain dark-blue uniform with no insignia or text standing by the door",
         camera="medium wide, eye level", amb="office_quiet", transition="black"),
    dict(to=34, reason="scene change: Ahna waiting smugly in Rafhaan's cabin", chars=["ahna", "rafhaan"], loc="cabin",
         visual="Ahna sitting comfortably in a leather guest chair in front of the desk, legs crossed under her long abaya, chin raised, an arrogant mocking smile; Rafhaan just entering through the glass door behind her, tired and stunned",
         camera="medium wide, Ahna in the foreground", amb="office_day"),
    dict(to=36, reason="action change: Rafhaan confronts Ahna", chars=["rafhaan", "ahna"], loc="cabin",
         visual="Rafhaan leaning forward over the desk on his fists, furious, accusing her face to face across the desk; Ahna seated on the other side, leaning back, unafraid, with a cold smirk",
         camera="medium two-shot, side view across the desk", amb="office_day", sens="violence/touch",
         safe="the narration has him grab her coat collar and her shake his hand off; shown as an angry confrontation across the desk with no physical contact"),
    dict(to=39, reason="action change: Ahna lays the contract file on the desk and delivers the ultimatum", chars=["ahna", "rafhaan"], loc="cabin",
         visual="close shot of Ahna's hand with gold-embroidered cuff pressing a thick closed dark folder (no text) onto the dark-wood desk; Rafhaan behind the desk staring at it, alarmed and worried",
         camera="close-up on the desk, low angle", amb="office_day"),
    dict(to=41, reason="action change: Ahna stands and walks out smiling", chars=["ahna"], loc="cabin",
         visual="Ahna walking out through the glass door of the cabin, glancing back over her shoulder with a triumphant smile, the city behind the glass",
         camera="medium wide", amb="office_day"),
    dict(to=43, reason="emotional turning point: Rafhaan alone, defeated", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan sitting alone in his black leather chair, elbows on the desk, both hands covering his face, the closed dark folder in front of him, the bright city behind the glass",
         camera="medium shot", amb="office_quiet"),
    dict(to=47, reason="scene and time change: at home Rafhaan tells Layaali; she sinks into a chair", chars=["layaali", "rafhaan"], loc="sitting_night",
         visual="Layaali sinking into an armchair in shock, one hand pressed to her chest, eyes wide and lost; Rafhaan standing a step away beside the chair with his arms at his sides, not touching her, looking down at her with a heavy, worried face",
         camera="medium two-shot, slightly high angle", amb="mansion_night", transition="black"),
    dict(to=49, reason="action change: Layaali asks how Ahna knew; Rafhaan's gaze falls on the toy box", chars=["layaali", "rafhaan"], loc="sitting_night",
         visual="Layaali seated in the foreground with tear-filled eyes looking up at Rafhaan; Rafhaan standing, deep in thought, his gaze turned towards the large cardboard toy box with a pink ribbon on the side table in the corner of the room",
         camera="medium wide, over Layaali's shoulder", amb="mansion_night"),
    dict(to=50, reason="memory: the box Ahna brought (reuse)", reuse="beat_004", chars=["ahna"], loc="sitting",
         visual="(reuse) the toy box with Ahna leaving", amb="memory", transition="dissolve"),
    dict(to=52, reason="action change: Rafhaan empties the box and lifts its false bottom", chars=["rafhaan"], loc="sitting_night",
         visual="Rafhaan kneeling on the rug beside the opened cardboard box, colourful toy cars and small balls spilled around him, lifting a loose cardboard layer from the bottom of the box, his eyes widening",
         camera="medium shot, slightly high angle", amb="mansion_night"),
    dict(to=55, reason="reveal: the hidden device", chars=["rafhaan", "layaali"], loc="sitting_night",
         visual="close-up of Rafhaan's hand holding up a tiny black electronic device with one small glowing green light; behind it, softly out of focus, Rafhaan's angry face and Layaali staring at it in disbelief",
         camera="close-up on the device", amb="mansion_night"),
    dict(to=59, reason="emotional turning point: Layaali's horror and their despair", chars=["layaali", "rafhaan"], loc="sitting_night",
         visual="Layaali standing with one hand over her mouth, frozen in shock and fear; Rafhaan beside her setting the tiny black device down on the coffee table, his face full of disappointment",
         camera="medium two-shot", amb="mansion_night"),
    dict(to=61, reason="time and scene change: next morning Zaahir, Ahna and Naasif arrive at the office", chars=["zaahir", "ahna", "naasif"], loc="lobby",
         visual="Zaahir, Ahna and Naasif striding side by side down the glass office corridor towards the viewer, heads held high, confident triumphant faces, Naasif carrying his briefcase",
         camera="wide shot, low angle", amb="office_day", transition="black"),
    dict(to=62, reason="scene change: the tense meeting in the cabin; Layaali trembling", chars=["layaali", "zaahir", "rafhaan"], loc="cabin_morning",
         visual="view across the large desk: on the far side of the desk Rafhaan and Layaali sit side by side facing the viewer, Layaali's trembling hands clasped on the desk next to a closed contract folder and a pen, Rafhaan grim and protective; in the near foreground on the right, on the opposite side of the desk from them, Zaahir sits in a guest chair seen in three-quarter view from behind his shoulder, leaning back with an arrogant smile",
         camera="medium wide, eye level", amb="office_quiet"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "His face was grave. 'Boss... this is a very dangerous agreement. Going by some of its clauses, if Layaali signs it, all of the company's main shares will pass to 'Zaahir")
sh(2, "Investments'. And it will look as if Layaali herself had taken the company's money.' Rafhaan clenched his teeth.")
sh(3, "Ahna's wickedness hasn't changed. She came out of jail with plans far more dangerous than before. 'This time we'll have them arrested for the crimes of the past.'", hum=True)
sh(4, "Rafhaan said. On one side, right now, Ahna's father's past is being checked. On the other side, Ahna is plotting how to deal Layaali a blow.")
sh(5, "'Aasim... can the original documents from the day Layaali's father's company was robbed be found?' 'Boss...")
sh(6, "I've found some records from the bank's archive. The original files that prove Zaahir forged the signatures are still in the bank's secret safe.")
sh(7, "But getting them won't be that easy,' Aasim said. Rafhaan immediately called the lawyer. He filed the case with the police.",
   [("phone_buzz", "ގުޅިއެވެ", -22)])
sh(8, "The police began working to obtain a court order. The day when the truth of the past comes out and Ahna and Zaahir's whole lives shatter is very near.")
sh(9, "But if Ahna finds out about this, what will she do? That afternoon, while Layaali was at home, Ahna came to the house again.",
   [("doorbell_buzz", "އައެވެ", -18)])
sh(10, "This time she had a big box in her hands — toys she had brought for Raina. But Layaali didn't know that a secret camera and a sound-recording microchip were fitted inside that box.")
sh(11, "Ahna wanted to secretly listen to everything said inside the house. Layaali put the box in the sitting room.",
   [("soft_thud", "ބެހެއްޓިއެވެ", -22)])
sh(12, "Every now and then Ahna's gaze stopped in that direction. Having slipped the toy box into the sitting room, she walked out swelling with pride deep in her heart.",
   [("footsteps_pavement", "ނުކުމެގެން", -24)])
sh(13, "This time her plans were so clever that no one would know what she was doing. She didn't want to stay only on the defensive.")
sh(14, "If Rafhaan and Layaali tried to climb onto her shoulders, she was ready to pull the ground from under their feet first.")
sh(15, "Sitting in her car, Ahna opened a computer. Through the secret microchip in the box, every word spoken in the house reached her ears instantly.",
   [("keyboard_typing", "ހުޅުވާލިއެވެ", -22)])
sh(16, "Just then Rafhaan came into the house almost running and took Layaali's hand. 'Layaali! Aasim got the court order!",
   [("door_open", "ވަދެ", -18)])
sh(17, "Tomorrow morning the original files of your father's that are in the bank's secret safe will be in our hands. Every fraud Ahmed Zaahir committed will be exposed!'")
sh(18, "Rafhaan's voice was full of joy. In the car, Ahna clenched her teeth. Knowing her father's past crimes would come out and all their wealth would go to Layaali, her blood boiled.",
   [("heartbeat", "ކެކިގަތެވެ", -18)], hum=True)
sh(19, "'I won't give you that chance, Rafhaan,' Ahna said to herself. 'This time I'm the one who'll win.'")
sh(20, "Ahna at once picked up the phone and called Naasif — her father's company's most trusted, yet money-hungry, legal adviser.",
   [("phone_buzz", "ގުޅިއެވެ", -18)])
sh(21, "'Naasif! Right now, call our man who has access to the bank's main server.' There was danger in Ahna's voice.")
sh(22, "'Tomorrow morning, before those files are brought out for the court order, Qaasim's original files in the bank's archive room have to be stolen or burned.")
sh(23, "I'll pay whoever does it whatever they want.' 'Don't worry, Ahna. It'll be done late tonight,' Naasif assured her.")
sh(24, "Ahna's plan was one step ahead of Rafhaan. It was the dead of night. While all of Malé slept, a masked person slipped in through the back door of the bank's archive building.",
   [("door_open", "ވަނެވެ", -22)], hum=True)
sh(25, "With the help of an insider, the bank's security systems had been switched off for five minutes.")
sh(26, "He went straight to the big box in Qaasim's name and burned the thirty-year-old original documents inside it with chemicals.",
   [("fire_crackle", "އަންދާލިއެވެ", -18)])
sh(27, "Then he fled. The strongest evidence Rafhaan and Layaali had was turned to ash.",
   [("footsteps_pavement", "ފިލިއެވެ", -22)], hum=True)
sh(28, "The next morning Rafhaan and Aasim went to the bank with the police and the court order. But a great shock awaited them.")
sh(29, "With his head bowed, the bank manager said, 'Rafhaan... last night there was a short circuit and a fire in the bank's archive.")
sh(30, "All of Qaasim's original files have burned to ash. There is no evidence at all that we can give you.'", hum=True)
sh(31, "It was as if the ground had been pulled from under Rafhaan's feet. Aasim, too, was stunned into silence. 'This is no coincidence, boss. Someone did this on purpose.'",
   [("gasp", "ހައިރާންވެ", -22)], hum=True)
sh(32, "Aasim said quietly. When Rafhaan came back to the office in despair, Ahna was sitting in his cabin.",
   [("door_open", "އައިއިރު", -22)])
sh(33, "She sat with her legs crossed and an arrogant smile. The fangs hidden behind her veil were out in the open today. 'What happened, Rafhaan?")
sh(34, "Did you get the files you wanted from the bank?' Ahna asked mockingly. In that moment Rafhaan's mind grasped Ahna's plan.")
sh(35, "Rafhaan seized Ahna hard by the collar of her coat. 'You! You did this! You burned the bank's files!' 'Where's the proof, Rafhaan?'",
   [("cloth_rustle", "ހިފިއެވެ", -18)], hum=True)
sh(36, "Ahna shook off Rafhaan's hand. 'Don't talk without proof. I'm not the old Ahna any more.",
   [("cloth_rustle", "ފޮޅުވާލިއެވެ", -20)])
sh(37, "This time I've come with a power you can't even imagine.' Ahna put a big file on the desk. 'This is the agreement I brought yesterday.",
   [("soft_thud", "ބޭއްވިއެވެ", -16)])
sh(38, "If Layaali doesn't sign it within the next twenty-four hours, big secrets of 'Rafhaan Group' will be leaked to the foreign investors")
sh(39, "and the company will go bankrupt. I have all that information.' 'How did you get that information?' Rafhaan was frightened.")
sh(40, "'That's for you to find out.' Ahna stood up. 'Tell Layaali to sign. Otherwise you'll all end up on the street.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(41, "I've won the first round of this war.' Ahna walked out of the cabin smiling.",
   [("footsteps_pavement", "ނިކުމެގެން", -22)])
sh(42, "Everything she wanted was going exactly to plan. Helpless, Rafhaan sat down in his chair and covered his face with both hands.",
   [("sigh", "އެޅިއެވެ", -20)], hum=True)
sh(43, "Today they had lost to Ahna's cunning. What will happen when Layaali hears this news?")
sh(44, "The news that every original document in the bank's archive room had turned to ash, and the dangerous ultimatum Ahna had given —")
sh(45, "when Rafhaan came home and told Layaali, a fearful silence fell over the whole house.", hum=True)
sh(46, "Layaali sank into a chair with a shock as if two worlds had collided. The strongest evidence for winning back her father's lost rights was gone today.",
   [("cloth_rustle", "އިށީނދެވުނީ", -22)], hum=True)
sh(47, "And that wasn't all. Full power to tear apart the company they had built with hard work was now in Ahna's hands.")
sh(48, "'Rafhaan... how could Ahna get such secret information about our company?' Layaali looked at Rafhaan with eyes full of tears.",
   [("sob_breath", "ކަރުނުން", -24)])
sh(49, "'Our office system is one of the most secure in the Maldives.' Lost in deep thought, Rafhaan's gaze came to rest on the cardboard box in a corner of the sitting room.")
sh(50, "It was the toy box Ahna had brought for Raina. A sudden suspicion rose in Rafhaan's heart.",
   [("heartbeat", "ޝައްކެއް", -20)])
sh(51, "He walked over, picked up the box and emptied out the toy cars and balls inside it.",
   [("footsteps_pavement", "ހިނގާފައި", -24), ("soft_thud", "އޮއްސާލިއެވެ", -20)])
sh(52, "And when he pulled away the cardboard layer at the bottom, which seemed different, his eyes widened.",
   [("paper_shuffle", "ނައްޓާލި", -20), ("gasp", "ބޮޑުވިއެވެ", -22)])
sh(53, "Stuck to the bottom was a tiny black electronic device. A small green light on it was blinking. 'Layaali!",
   [("heartbeat", "ދިއްލެމުން", -18)])
sh(54, "Here's the proof of the trickery!' Rafhaan picked up the device and showed it. 'This is a secret camera and a sound-recording microchip.")
sh(55, "Everything we said at home — the company's secrets, our plan to get the bank files — Ahna heard it all with this device.")
sh(56, "She burned the bank files after hearing about it from here.' Layaali put her hand over her mouth. Seeing how far Ahna's wickedness and scheming went, her whole body went cold.",
   [("gasp", "އަތްއެޅިއެވެ", -18)], hum=True)
sh(57, "'Even if we know it now, we'll never get the bank files back, will we, Rafhaan?")
sh(58, "We have no evidence at all against Zaahir.' Rafhaan put the device down on the table. Disappointment showed on his face.",
   [("soft_thud", "ބޭއްވިއެވެ", -22)])
sh(59, "The victory Ahna had won this time was a huge step ahead of them.")
sh(60, "The next morning Ahna and her father Ahmed Zaahir came to the head office of 'Rafhaan Group' as if celebrating a great victory.",
   [("footsteps_pavement", "އައީ", -22)])
sh(61, "With them, in the team that came in with heads held high, was their legal counsel Naasif. In Rafhaan's cabin the air was filled with a breath-holding silence.")
sh(62, "Layaali sat beside Rafhaan. Her hands had begun to tremble with fear. 'Rafhaan... time's up,' Zaahir said with an arrogant smile.",
   [("heartbeat", "ތުރުތުރުލާން", -18)], hum=True)
SHOTS = S

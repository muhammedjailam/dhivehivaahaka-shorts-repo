"""Beat/shot plan for Tedhuveriloabi episode 483 (used by plan_beats.py)."""

AHNA_PLAIN = ("Ahna here wears a plain dark-grey ankle-length abaya with no embroidery and a plain black cotton hijab, "
              "no makeup and no gold, instead of her usual burgundy hijab and gold-cuffed abaya")

LOC = {
    "prison": "outside the walled prison compound of Maafushi island in the Maldives in the morning: a tall plain pale concrete perimeter wall with a closed heavy grey steel gate, a sandy road, coconut palms and a wide bright tropical sky; no signs",
    "zaahir_living": "the grand living room of Ahmed Zaahir's luxurious villa in Malé: polished marble floor, dark carved wood and gold furnishings, gilded armchairs, tall windows with heavy wine-red curtains",
    "mansion_entry": "the grand front entrance of Rafhaan's large modern white mansion in Malé: a tall dark-wood double door open onto a bright marble foyer with a wide staircase, potted palms",
    "album": "a white bedsheet beside a pillow in a quiet bedroom, soft window light",
    "qaasim_room": "a quiet, simple ground-floor guest bedroom in Rafhaan's mansion where Layaali's frail father now lives: a single bed with white sheets and pillows, a bedside table with medicine bottles and a glass of water, a window with sheer curtains onto a green garden",
    "memory_city": "the Malé waterfront business street thirty years ago, in the early 1990s: a handsome three-storey white commercial building with arched windows and balconies, palm trees, the harbour behind",
    "memory_office": "a private company office thirty years ago, in the early 1990s: a heavy wooden desk with a green banker's lamp, stacks of paper files and ledgers, a rubber stamp, a ceiling fan, wooden venetian blinds",
    "garden": "the lush garden of Rafhaan's mansion: a neat green lawn, frangipani and pink bougainvillea, a white garden bench, a low hedge, the white mansion with tall glass doors behind",
    "gate_lane": "the clean narrow lane outside the tall white gate of Rafhaan's mansion in Malé, palm fronds hanging over the white wall, a parked car",
    "zaahir_study": "the dark-wood study of Ahmed Zaahir's villa in Malé: a large leather chair, a heavy carved desk, bookshelves, a tall window with the city behind",
    "living_night": "the spacious modern living room of Rafhaan's mansion at night: a large cream sofa, warm table lamps, floor-to-ceiling windows with the night lights of Malé and the dark sea beyond",
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin high in the company tower in Malé: a large dark-wood desk, a black leather chair, glass walls, a wide window with the city skyline and the turquoise sea",
}
MOOD = {
    "prison": "bright morning sun, hard clear light, an unsettling calm",
    "zaahir_living": "late afternoon, warm amber light through heavy curtains, rich shadows, a welcome with something cold beneath it",
    "mansion_entry": "afternoon, bright soft daylight from the doorway, tense and emotional",
    "album": "soft daylight, quiet, nostalgic and sad",
    "qaasim_room": "soft daylight through sheer curtains, quiet, heavy with sorrow",
    "memory_city": "sepia-toned, hazy warm light, faded and dreamlike memory, soft vignette",
    "memory_office": "sepia-toned night memory, a single pool of lamp light, deep shadows, secretive, soft vignette",
    "garden": "afternoon sun, dappled light through the trees, deceptively peaceful with an undercurrent of menace",
    "gate_lane": "late afternoon, long shadows, golden light turning cold",
    "zaahir_study": "early evening, low lamp light, deep shadows, scheming",
    "living_night": "night, warm dim lamp light, city lights through the glass, worried and intimate",
    "cabin": "bright morning daylight through the glass, cool blue and warm amber, polite but tense",
}

BEATS = [
    dict(to=4, reason="new episode opening: Ahna released from prison", chars=["ahna"], loc="prison",
         visual=f"Ahna standing alone on the sandy road just outside the closed steel prison gate, chin raised, gazing up at the wide sky with a faint, strange, knowing smile, a small cloth bag in one hand. {AHNA_PLAIN}",
         camera="medium shot from a slightly low angle, her face in the upper third, the empty sandy road in the lower third", amb="prison_exterior"),
    dict(to=6, reason="scene and character change: back in Malé, her father Zaahir welcomes her", chars=["zaahir", "ahna"], loc="zaahir_living",
         visual=f"Ahmed Zaahir, beaming with relief, welcoming his daughter Ahna home in his grand living room, his hands resting fatherly on her shoulders at arm's length; Ahna, fresh out of prison and dressed very plainly, giving him a small, polite, unreadable smile. IMPORTANT: Ahna's hijab is plain matte black (NOT burgundy, NOT red) and her abaya is plain dark grey with completely plain sleeves (NO gold embroidery, no cuffs); keep only her face from the reference. {AHNA_PLAIN}",
         camera="medium two-shot, eye level", amb="mansion_day"),
    dict(to=9, reason="emotional turning point: Ahna reveals her hatred, Zaahir joins her", chars=["ahna", "zaahir"], loc="zaahir_living",
         visual=f"Ahna seated upright in a gilded armchair, her face gone cold and hard, eyes narrowed as she speaks; Zaahir standing beside the chair, his surprise turning into a slow, dangerous smile. {AHNA_PLAIN}",
         camera="medium close two-shot, slightly low angle", amb="mansion_day"),
    dict(to=10, reason="time jump and scene change: next afternoon, Ahna at Rafhaan's front door", chars=["layaali", "ahna"], loc="mansion_entry",
         visual="Layaali holding the front door open, frozen in shock, one hand pressed to her chest; Ahna standing on the doorstep outside in her burgundy hijab, eyes glistening, looking humble and fragile",
         camera="medium two-shot from inside the foyer", amb="mansion_day", transition="black"),
    dict(to=12, reason="action change: Ahna falls at Layaali's feet begging forgiveness", chars=["ahna", "layaali"], loc="mansion_entry",
         visual="Ahna kneeling on the marble floor of the entrance in front of Layaali, looking up at her with tears on her cheeks, hands clasped in plea; Layaali standing, taken aback, her hands drawn to her chest, her face softening",
         camera="medium wide, slightly high angle over Layaali's shoulder", amb="mansion_day", hum_note="emotional peak"),
    dict(to=14, reason="action change: Layaali raises Ahna up and forgives her", chars=["layaali", "ahna"], loc="mansion_entry",
         visual="Layaali bending down and gently taking Ahna's hands to raise her to her feet, a soft forgiving smile on her face; Ahna rising with her eyes lowered, a humble, grateful look",
         camera="medium two-shot, eye level", amb="mansion_day"),
    dict(to=17, reason="character enters: Rafhaan comes home and sees Ahna", chars=["rafhaan", "layaali", "ahna"], loc="mansion_entry",
         visual="Rafhaan in his black suit stepping in through the front door and stopping short with a cold, displeased frown at Ahna; Layaali standing near him, one hand raised gently as she explains; Ahna standing a little apart with her eyes lowered meekly",
         camera="medium wide, eye level", amb="mansion_day"),
    dict(to=19, reason="scene change, detail image: Qaasim's illness and his old photo album", loc="album",
         visual="close-up of an old man's thin hands, in faded light-blue cotton sleeves, holding open a worn brown leather photo album on a white sheet; the album shows faded old photographs of grand white buildings and shiny vintage cars, no writing anywhere",
         camera="close-up from above", amb="room_day"),
    dict(to=22, reason="character and action change: Layaali feeding her father notices the album", chars=["layaali", "qaasim"], loc="qaasim_room",
         visual="Layaali sitting on a chair at her father's bedside holding a small bowl and spoon, feeding him, glancing curiously at the open photo album lying by his pillow; Qaasim propped up on white pillows, his tired eyes wet with tears",
         camera="medium two-shot, eye level", amb="room_day"),
    dict(to=24, reason="flashback: thirty years ago Qaasim Enterprises was Malé's biggest company", loc="memory_city",
         visual="a sepia-toned memory: a proud white three-storey company building on the 1990s Malé waterfront, a row of gleaming vintage 1990s cars parked in front, a few office workers in 1990s clothes in the distance; no signs, no lettering",
         camera="wide establishing shot, eye level", amb="memory", transition="dissolve"),
    dict(to=26, reason="flashback, action change: the trusted partner forges the documents", loc="memory_office",
         visual="a sepia-toned memory at night: a heavy-set man in his early 30s with a thick black moustache and slicked-back black hair, in a 1990s grey suit, bent over the desk under the green lamp, secretly copying a signature onto blank documents with a fountain pen, a sly cold look on his face; the papers show no readable writing",
         camera="medium shot, slightly low angle", amb="memory", transition="dissolve", sens="other",
         safe="the fraud is shown only as a man signing papers at night; no readable documents"),
    dict(to=28, reason="emotional turning point: back in the room, the name Ahmed Zaahir is revealed", chars=["qaasim", "layaali"], loc="qaasim_room",
         visual="Qaasim in the bed weeping openly, one trembling hand over his eyes; Layaali at the bedside frozen in shock, one hand over her mouth, her eyes wide and wet, the photo album open on the blanket",
         camera="medium close two-shot", amb="room_day", transition="dissolve"),
    dict(to=30, reason="scene and character change: meanwhile Ahna with little Raina in the garden", chars=["ahna", "raina"], loc="garden",
         visual="Ahna sitting on the white garden bench with little Raina standing beside her knee; Ahna gently stroking the child's soft curly hair while her eyes, turned slightly away, hold a cold, dangerous look; Raina smiling innocently, holding a small frangipani flower",
         camera="medium shot, eye level", amb="garden_day"),
    dict(to=35, reason="scene change: Layaali alone in her father's room, in tears", chars=["layaali", "qaasim"], loc="qaasim_room",
         visual="Layaali sitting alone on a chair by the window, tears running down her face, wiping her eyes with the back of her hand, staring at nothing; her father asleep on the bed behind her, softly out of focus",
         camera="medium close-up, eye level, window light on her face", amb="room_day"),
    dict(to=36, reason="the narration returns to Ahna in the garden with Raina (reuse)", reuse="beat_013", chars=["ahna", "raina"], loc="garden",
         visual="(reuse) Ahna with Raina in the garden", amb="garden_day"),
    dict(to=40, reason="action change: Raina screams, Layaali rushes out into the garden", chars=["layaali", "ahna", "raina"], loc="garden",
         visual="Layaali hurrying out through the tall glass garden doors, alarmed, her eyes red from crying; on the white bench Ahna sits holding little Raina on her lap and stroking her head, looking up at Layaali with a sweet, gentle smile",
         camera="wide shot across the lawn, eye level", amb="garden_day"),
    dict(to=43, reason="action change: Layaali takes Raina away from Ahna", chars=["layaali", "raina", "ahna"], loc="garden",
         visual="Layaali holding little Raina protectively in her arms, half turned towards the house, her face guarded; Ahna standing by the bench, slightly surprised, then smiling and nodding politely",
         camera="medium two-shot, eye level", amb="garden_day"),
    dict(to=46, reason="scene change: Ahna leaves and phones her father", chars=["ahna"], loc="gate_lane",
         visual="Ahna walking out through the white gate of the mansion into the lane, a phone held to her ear, her sweet smile twisted into a cold, cunning sneer",
         camera="medium shot, eye level", amb="city_day"),
    dict(to=48, reason="character change: Zaahir on the other end of the call", chars=["zaahir"], loc="zaahir_study",
         visual="Ahmed Zaahir leaning back in his large leather chair, a phone to his ear, a confident, cold, scheming smile, his gold watch glinting in the lamp light",
         camera="medium close-up, slightly low angle", amb="office_quiet"),
    dict(to=53, reason="time jump: that night Rafhaan comes home to a troubled Layaali", chars=["layaali", "rafhaan"], loc="living_night",
         visual="Layaali sitting on the cream sofa, lost in sorrowful thought; Rafhaan, home from work in his black suit, sitting down beside her and turning to her with tender concern, her hand resting on his arm",
         camera="medium two-shot, eye level", amb="living_night", transition="black"),
    dict(to=56, reason="emotional turning point: Rafhaan realises Ahna's family is plotting", chars=["rafhaan", "layaali"], loc="living_night",
         visual="Rafhaan standing up by the dark window, stunned, one hand raised to his forehead as realisation dawns on his face; Layaali on the sofa looking up at him, frightened, her hands clasped tightly",
         camera="medium wide, eye level", amb="living_night"),
    dict(to=58, reason="back to the couple on the sofa as Rafhaan makes his promise (reuse)", reuse="beat_020", chars=["layaali", "rafhaan"], loc="living_night",
         visual="(reuse) Rafhaan and Layaali on the sofa", amb="living_night"),
    dict(to=62, reason="time jump and scene change: next day Ahna brings a file to Rafhaan's office", chars=["ahna", "rafhaan"], loc="cabin",
         visual="Ahna in her burgundy hijab standing at Rafhaan's desk, calm and sweetly polite, holding out a thick closed dark-blue file folder with both hands; Rafhaan seated behind the desk, looking up at her with a measured, polite smile",
         camera="medium two-shot, eye level", amb="office_day", transition="black"),
    dict(to=64, reason="action change: alone, Rafhaan phones Aasim about the file", chars=["rafhaan"], loc="cabin",
         visual="Rafhaan alone at his desk, a phone to his ear, the thick file open in front of him showing only blank pages, his face grave and suspicious",
         camera="medium close-up, eye level", amb="office_day"),
    dict(to=65, reason="character enters: two hours later Aasim comes in with his findings", chars=["aasim", "rafhaan"], loc="cabin",
         visual="Aasim stepping into the glass cabin holding an open laptop (screen facing away) and the thick file, his face very serious; Rafhaan rising from his chair behind the desk, watching him",
         camera="medium wide, eye level", amb="office_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Walking out of the jail, she lifted her head and looked up at the sky. An unusual smile came onto her lips. 'Layaali...",
   [("footsteps_pavement", "ނިކުމެ", -24)])
sh(2, "did you think the letter I sent was the truth?' Ahna said to herself. And with that, a smile appeared on that face.")
sh(3, "A smile on the face is no proof of a pure heart. Sometimes the most dangerous snake hides beneath the petals of the most beautiful flower.", hum=True)
sh(4, "'I bore all the pain of jail waiting for the day I would tear your life to pieces.")
sh(5, "I didn't come back only to get Rafhaan. I came to take everything from you.' When Ahna returned to Malé, her father Ahmed Zaahir welcomed her.")
sh(6, "Zaahir thought his daughter had now reformed. Zaahir was happy that his daughter had changed.")
sh(7, "Then Ahna's next sentence gave Zaahir a sudden shock. 'I had to spend three years of my life in jail because of Layaali and Rafhaan.",
   [("gasp", "ސިހުމެއް", -20)])
sh(8, "I will never forgive them.' What Ahna wanted first of all was to win Rafhaan and Layaali's trust.", hum=True)
sh(9, "'From that devilish whisper of yours, my girl, no one will be safe.' Zaahir too began to laugh in a dangerous way. The next afternoon, the doorbell of Rafhaan's house began to ring.",
   [("doorbell_buzz", "ބެލް", -16)])
sh(10, "The bell rang differently from the way others ring it. Layaali opened the door. Seeing Ahna standing at the door, Layaali's heart gave a start.",
   [("door_open", "ހުޅުވާލީ", -18), ("heartbeat", "ސިހުނެވެ", -18)])
sh(11, "The frightening memories of the past spun before her eyes. 'Layaali...' Tears streamed from Ahna's eyes. At once she dropped down at Layaali's feet.",
   [("sob_breath", "ކަރުނަ", -24), ("cloth_rustle", "ތިރިވިއެވެ", -22)])
sh(12, "'Forgive me. I came to ask Layaali's forgiveness. Never again will a seed of envy towards anyone sprout in my heart.", hum=True)
sh(13, "I want to start a new life.' Layaali has always been a calm, kind-hearted girl. Seeing Ahna in this state, her heart softened.")
sh(14, "She took Ahna by the hand and raised her up. 'Ahna... I have forgotten everything in the past. I have forgiven you.'",
   [("cloth_rustle", "އުފުލާލިއެވެ", -22)])
sh(15, "Just then Rafhaan came into the house. Seeing Ahna, displeasure showed on his face. But Layaali made Rafhaan understand",
   [("door_close", "ވަނީ", -20)])
sh(16, "that Ahna had changed and must be given a new chance. The first step of Ahna's plan had succeeded.")
sh(17, "She had slipped into their lives in an innocent guise. Meanwhile, Layaali's father's illness was getting worse day by day.")
sh(18, "Lying in bed, the one thing he always did to calm himself was look through a photo album.",
   [("page_turn", "އަލްބަމް", -20)])
sh(19, "In that album were photos of grand, richly built buildings and cars.",
   [("page_turn", "އަލްބަމްގެ", -22)])
sh(20, "One day, sitting to feed her father, Layaali saw the album and asked, 'Dad... what photos are these? Why do you always look at them?'",
   [("cup_clatter", "ކާންދޭން", -22)])
sh(21, "Qaasim let out a deep breath. Tears welled in his eyes. 'Layaali, my child... today, before my soul leaves this world, I must tell you about my past.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -18)], hum=True)
sh(22, "You think your father was always a poor, humble man, don't you!' Layaali was puzzled. 'Yes, Dad... we are poor, humble people.")
sh(23, "So what happened?' 'No, my child. Thirty years ago, in Malé's business market, \"Qaasim Enterprises\" was the biggest company.")
sh(24, "What you see in these photos are my own buildings and property,' Qaasim said in a trembling voice. 'But...")
sh(25, "my most trusted partner played a great deceit on me, forged all the documents and robbed me of my whole fortune.",
   [("paper_shuffle", "ލިޔެކިޔުންތަކެއް", -22)])
sh(26, "He put me out on the street.' 'Who? Who was it?' Layaali asked again and again. At that moment her heart began to pound. 'It was...",
   [("heartbeat", "ތެޅިގަތެވެ", -16)])
sh(27, "Ahmed Zaahir! Ahna's father!' Qaasim broke down crying. 'The company he built with everything he took from me is the \"Zaahir Investments\" they run today.'",
   [("sob_breath", "ރޮއިގަތެވެ", -20)], hum=True)
sh(28, "Layaali's head began to spin. What kind of terrible coincidence was this? The family of Ahna, who had tried to wreck her life, were the enemies who had torn her father's whole life apart.",
   [("heartbeat", "އެނބުރުން", -18)], hum=True)
sh(29, "This great stain of envy and revenge had been woven long ago in the past. At that very moment, in the garden of Rafhaan's house, Ahna sat playing with little Raina.")
sh(30, "Stroking Raina's head, she looked at that small innocent child with a dangerous gaze.", hum=True)
sh(31, "'Now that the secret of the past is out, what will happen to my life? Why did Dad keep quiet about it all these days?'")
sh(32, "As Layaali talked to herself, she did not know of Ahna's wicked plan. And how will she save her daughter from Ahna's wicked plan?")
sh(33, "Every word from her father's lips was like a thorn piercing Layaali's heart. Until today she had believed her family had always been ordinary poor people.")
sh(34, "But because of the great deceit and trickery of Ahna's father, Ahmed Zaahir, her father had ended up on the street, broken in mind")
sh(35, "and body — knowing that, tears flowed endlessly from Layaali's eyes. What a heartbreaking truth this was!",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(36, "The daughter of the man who tore her father's life apart — Ahna — was today in the garden of her own house, with her own daughter.")
sh(37, "As Layaali came out of the room wiping her tears, she heard Raina scream from the garden.",
   [("gasp", "ހަޅޭއްލަވައިގަތް", -18)])
sh(38, "When Layaali came out, almost running, Ahna was sitting with Raina on her lap, stroking her head again and again.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(39, "Ahna's face showed a look of great tenderness. But today, seeing that scene filled Layaali's heart with fear. 'Layaali, what happened?")
sh(40, "Why are your eyes red?' Ahna asked gently. 'Nothing... Dad is a little unwell, so I'm feeling sad.'")
sh(41, "Layaali quickly went over and took Raina from Ahna's arms. Her heart kept telling her not to trust Ahna. 'Ahna, it's best you go now for today.")
sh(42, "I'm taking my daughter inside.' Lately Ahna had been coming every day to spend a little time with Raina.")
sh(43, "Posing as someone who loves children very much. Ahna seemed a little surprised. But she smiled and nodded. 'All right, Layaali.")
sh(44, "I pray Dad gets well soon. I'll come tomorrow.' As Ahna walked out of the house, the smile on her face turned into a dangerous sneer.",
   [("footsteps_pavement", "ނިކުމެގެން", -24)], hum=True)
sh(45, "At once she took out her phone and called her father Zaahir. 'Dad... I saw some change in Layaali's face.",
   [("phone_buzz", "ފޯނު", -18)])
sh(46, "It looks like she has found something out. Just as you said, their father Qaasim is still alive.")
sh(47, "We have to move the plan forward as fast as we can.' 'Don't worry, my girl,' Zaahir said on the phone. 'Qaasim is a man on his deathbed now.")
sh(48, "There's nothing he can do. Our aim is to carry out a big betrayal inside \"Rafhaan Group\" using Layaali's name.")
sh(49, "Then Rafhaan himself will throw her out of the house.' That night, when Rafhaan came home, Layaali was sitting in the living room, lost in deep thought.",
   [("door_open", "އައިއިރު", -22)])
sh(50, "Rafhaan went and sat down beside Layaali and took her hand. 'Layaali... what's wrong? Today Aasim told me you were trying to find some documents about your father's past.'",
   [("cloth_rustle", "އިށީނދެ", -24)])
sh(51, "Rafhaan asked tenderly. Layaali looked at Rafhaan. Her eyes showed the mark of grief. 'Rafhaan...")
sh(52, "my father's past is a very painful one. Today Dad told me the whole story.'")
sh(53, "Layaali told Rafhaan everything: the details of Ahmed Zaahir's deceit and how he robbed her father of his company.")
sh(54, "Rafhaan was stunned into silence. 'This... this can't be. Zaahir committed such a huge crime?",
   [("gasp", "ހައިރާންވެ", -20)])
sh(55, "Then Ahna doesn't come to this house just to ask forgiveness. And not out of love for Raina either.")
sh(56, "This is something their whole family has planned.' 'Yes, Rafhaan. I'm so scared. When Ahna sat holding Raina today, I felt something evil in my heart too.'", hum=True)
sh(57, "Layaali said. 'Don't worry, Layaali. Right away I'll have Aasim start digging out the base records of Zaahir's \"Zaahir Investments\" and the documents from the past.")
sh(58, "From this moment I will work to win back your father's rights,' Rafhaan promised firmly.")
sh(59, "The next day Ahna came to the office to meet Rafhaan. She came looking very calm and at ease. 'Rafhaan...")
sh(60, "My father wants to make a new business agreement with \"Rafhaan Group\". It's a gift in return for the wrongs of our past.'")
sh(61, "Ahna held out a big file. Rafhaan looked at Ahna and smiled. Then he took hold of the file.",
   [("paper_shuffle", "ފައިލެއް", -20)])
sh(62, "Without letting any displeasure show on his face, he simply nodded. 'All right, Ahna. I'll look through this file.'")
sh(63, "As soon as Ahna left, Rafhaan called Aasim. 'Aasim, check the contracts inside this file Ahna brought.",
   [("footsteps_pavement", "ނިކުމެގެން", -24), ("phone_buzz", "ގުޅިއެވެ", -20)])
sh(64, "There's bound to be some big fraud hidden in here. It would be best to get help from another staff member to check this file.'")
sh(65, "After a careful study, two hours later Aasim walked into Rafhaan's cabin. His face showed how serious it was.",
   [("door_open", "ވަނެވެ", -20)])
SHOTS = S

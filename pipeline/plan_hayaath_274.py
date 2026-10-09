"""Beat/shot plan for Hayaath episode 274 (used by plan_beats.py)."""

LOC = {
    "hospital_room": "a small Maldivian island hospital room in the morning, a single hospital bed with white sheets, pale green walls, a drip stand, soft daylight through a window",
    "bedroom": "Hayaathu's small plain bedroom in an old Maldivian coral-stone house in the late afternoon, a single bed with a simple cotton sheet, a wooden louvered window, a ceiling fan, a plain wooden door with an old bolt",
    "door": "the inside of a plain wooden bedroom door in an old Maldivian coral-stone house, an old iron bolt and lock",
    "fazaal_room": "a spacious room in a large old two-storey house on a Maldivian island, wooden furniture, tall windows with sheer curtains, late afternoon light",
    "fazaal_detail": "a wooden side table in a large old house, late afternoon window light",
    "airport": "a small island airport runway beside a turquoise lagoon at dusk, palm trees",
    "car": "inside a dark car parked on a quiet island road at night, streetlights outside",
    "street": "a narrow island town street at night in the Maldives, warm streetlights, low walled houses, coconut palms, parked motorbikes",
    "sea": "the moonlit sea off a secluded Maldivian beach at night",
}
MOOD = {
    "hospital_room": "morning, soft pale light, fragile and sad",
    "bedroom": "late afternoon, warm low light through the louvers, deep shadows, oppressive and melancholic",
    "door": "dim, low-key light, oppressive",
    "fazaal_room": "late afternoon, warm golden light, pensive and troubled",
    "fazaal_detail": "soft quiet light, grief, stillness",
    "airport": "dusk, warm sky, calm, remembered",
    "car": "night, soft glow of a phone screen on his face, intimate and wondering",
    "street": "night, warm sodium streetlights, blue shadows, quiet",
    "sea": "night, moonlight, ominous",
}

BEATS = [
    dict(to=2, reason="new episode opening: Hayaathu alone in the hospital room after Waheed leaves", chars=["hayaathu"], loc="hospital_room",
         visual="Hayaathu sitting up in the hospital bed, eyes closed, tears on her cheeks, her hands limp on the white sheet; the door ajar where her uncle has just left",
         camera="medium shot, eye level", amb="hospital_room"),
    dict(to=7, reason="characters change: the nurse comforts her", chars=["hayaathu", "nurse"], loc="hospital_room",
         visual="the young nurse sitting on the edge of the hospital bed holding Hayaathu in a comforting embrace and rubbing her back, Hayaathu weeping on her shoulder",
         camera="medium close-up", amb="hospital_room"),
    dict(to=10, reason="scene change: home, Hayaathu locks herself in her room", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting curled in the corner of her bed, knees drawn up, staring at nothing with hopeless red eyes, the bolted wooden door in view",
         camera="medium wide, slightly high angle", amb="room_day", transition="black"),
    dict(to=14, reason="detail image: locked doors and closed paths, then the knocking", loc="door",
         visual="close-up of a plain wooden door bolted shut with an old iron bolt and lock, a thin line of light under it, deep shadows, no people",
         camera="close-up", amb="room_day"),
    dict(to=20, reason="characters change: Areesha at the door with the phone", chars=["areesha", "hayaathu"], loc="bedroom",
         visual="at the open bedroom doorway Areesha holding out a smartphone towards Hayaathu with a smug mocking smile; Hayaathu standing inside, frightened and wary",
         camera="medium two-shot", amb="room_day"),
    dict(to=27, reason="action change: Areesha holds Hayaathu back and taunts her", chars=["areesha", "hayaathu"], loc="bedroom",
         visual="inside the bedroom Areesha holding Hayaathu by the wrist to stop her walking away, leaning in with a mocking grin; Hayaathu, phone in hand, glaring back with anger and tears in her eyes",
         camera="medium close two-shot", amb="room_day"),
    dict(to=29, reason="Areesha returns to the door (reuse)", reuse="beat_005", chars=["areesha", "hayaathu"], loc="bedroom",
         visual="(reuse) Areesha at the doorway", amb="room_day"),
    dict(to=33, reason="action change: alone, Hayaathu looks at the photo", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting on her bed looking down at a smartphone whose screen faces away from the viewer and glows softly, her face frozen in fear, eyes wide",
         camera="medium close-up", amb="room_day", sens="other",
         safe="the photo of the burned face is never shown; only her reaction, the screen faces away"),
    dict(to=36, reason="action change: the phone rings, she answers", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu holding a phone to her ear with a trembling hand, sitting on the edge of the bed, whispering, frightened eyes looking sideways",
         camera="close-up", amb="room_day"),
    dict(to=42, reason="characters change: Waheed at the door", chars=["waheed", "hayaathu"], loc="bedroom",
         visual="Waheed standing in the bedroom doorway with a hard stern face, Hayaathu sitting on the bed looking up at him frightened, the phone set face-down on the bed beside her",
         camera="medium wide, from behind Hayaathu", amb="room_day"),
    dict(to=48, reason="action change: Hayaathu pleads as Waheed turns to leave", chars=["hayaathu", "waheed"], loc="bedroom",
         visual="Hayaathu standing with hands clasped, pleading with tears, as Waheed turns away towards the door with a cold face",
         camera="medium shot", amb="room_day", hum_note="emotional peak"),
    dict(to=49, reason="characters change: Zoona brings Dhooma in", chars=["zoona", "dhooma"], loc="bedroom",
         visual="Zoona pushing Dhooma in her black wheelchair through the bedroom doorway with a bored face, Dhooma looking ahead eagerly",
         camera="medium wide", amb="room_day"),
    dict(to=53, reason="action change: the sisters reunite", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu kneeling beside Dhooma's wheelchair, holding her sister's hand against her own cheek with her eyes closed, Dhooma looking down at her tenderly with tears",
         camera="medium close-up", amb="room_day", sens="other",
         safe="kissing her sister's hand shown as holding the hand to her cheek"),
    dict(to=58, reason="action change: Hayaathu announces her decision", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu sitting on the edge of the bed facing Dhooma in her wheelchair, wiping her tears with a brave, resolved face; Dhooma leaning forward, worried, trying to speak",
         camera="medium two-shot, eye level", amb="room_day"),
    dict(to=62, reason="detail image during the long conversation", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="close-up of two women's hands clasped together on a grey knitted shawl, rose and teal sleeves, warm light from the window",
         camera="extreme close-up", amb="room_day"),
    dict(to=65, reason="action change: Hayaathu leaves the room", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu walking towards the open door, glancing back with a bitter brave smile, while Dhooma in her wheelchair reaches out a hand, pleading; a smartphone left on a small wooden table",
         camera="medium wide", amb="room_day"),
    dict(to=67, reason="scene and character change: Fazaal heard everything on the phone", chars=["young_driver"], loc="fazaal_room",
         visual="Fazaal standing by a tall window in a large old house, phone held to his ear, his face troubled and thoughtful",
         camera="medium close-up", amb="fazaal_room"),
    dict(to=69, reason="symbolic detail for his brother's tragedy", loc="fazaal_detail",
         visual="a framed photograph lying face-down on a wooden side table beside a wilted white flower and a man's watch, soft window light, no people",
         camera="close-up", amb="fazaal_room", sens="injury/death",
         safe="the brother's burned face and death are never shown; a face-down photo frame and a wilted flower instead"),
    dict(to=70, reason="back to Fazaal (reuse)", reuse="beat_017", chars=["young_driver"], loc="fazaal_room",
         visual="(reuse) Fazaal at the window", amb="fazaal_room"),
    dict(to=71, reason="flashback: his arrival", loc="airport",
         visual="a small passenger plane landing on an island runway beside a turquoise lagoon at dusk, palm trees, no people",
         camera="wide shot", amb="airport", transition="dissolve"),
    dict(to=73, reason="flashback: the near-accident from episode 272 (reused image)", reuse="ep272:shot_032", chars=["young_driver"], loc="street",
         visual="(reuse from ep 272) Fazaal striding from his car, angry, backlit by headlights", amb="road_busy", sens="other",
         safe="near-accident shown only as the driver stepping out (image from ep 272)"),
    dict(to=76, reason="flashback: his attention turns to Hayaathu caring for Dhooma (reused image)", reuse="ep272:shot_033", chars=["hayaathu", "dhooma"], loc="street",
         visual="(reuse from ep 272) Hayaathu crouching beside Dhooma's wheelchair at the roadside", amb="road_busy"),
    dict(to=80, reason="action change: the photo message", chars=["young_driver"], loc="car",
         visual="Fazaal sitting in the driver's seat of his dark car at night, his face lit by the soft glow of a phone (screen not visible), an amazed, tender expression",
         camera="close-up through the side window", amb="street_night"),
    dict(to=82, reason="action change: he follows the sisters", chars=["young_driver", "hayaathu", "dhooma"], loc="street",
         visual="on a quiet island street at night, Fazaal walking slowly in the shadows far behind two figures seen from behind: a young woman in a rose dress pushing her sister in a wheelchair under the streetlights",
         camera="wide shot from behind Fazaal", amb="street_night"),
    dict(to=83, reason="cliffhanger: he too jumped into the sea (reused image)", reuse="ep272:shot_091", loc="sea",
         visual="(reuse from ep 272) a splash on the moonlit sea", amb="beach_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Having said what he wanted to say, Waheed walked out. Hayaathu closed her tear-filled eyes.", [("footsteps_pavement", "ނިކުމެގެން", -24)])
sh(2, "'Was I born into this world only to be the prey of hatred?' she said to herself. Where is her happiness?", hum=True)
sh(3, "She too wants to smile. The nurse came close and looked at her. Without meaning to, Hayaathu threw her arms around the nurse.",
   [("cloth_rustle", "ބައްދައިގަނެވުނެވެ", -22)])
sh(4, "With sympathy the girl kept stroking Hayaathu's back. 'What really happened? Why did you jump into the sea?' the nurse asked.")
sh(5, "Hearing that, Hayaathu looked at the nurse in surprise. 'I jumped into the sea to save Dhontha. I couldn't look after my sister well enough.'")
sh(6, "Hayaathu said, crying. Suddenly remembering something, she asked, 'Where is Dhontha?'")
sh(7, "Hayaathu asked anxiously, sobbing. 'Dhontha is fine...' the nurse said.", [("sob_breath", "ގިސްލަމުން", -24)])
sh(8, "From the hospital she went home, straight into her room, and locked it. She didn't want to see anyone.",
   [("door_close", "ވަދެ", -18), ("lock_click", "ތަޅުލިއެވެ", -16)])
sh(9, "Waheed forbade her to meet her sister. The way to meet Maaroof was closed too. Even going to college was forbidden.")
sh(10, "What will she do now? Where are the hopes she had? Where are the dreams of a future with Maaroof?", hum=True)
sh(11, "Sitting in a corner of the bed she sobbed. All around her were closed roads, doors with heavy locks.",
   [("sob_breath", "ގިސްލާ", -24)])
sh(12, "There was no road in sight that led to the light of happiness. All around was darkness and despair.", hum=True)
sh(13, "With Areesha's voice came loud banging on the door. Since that was normal, Hayaathu stayed where she was. Again Areesha's voice came from outside.",
   [("knock", "ތަޅައިގަތް", -12), ("knock", "ބޭރުން", -14)])
sh(14, "'Open this door. Dad says...' Areesha's voice again. 'Still not opening the door?' came Waheed's voice from outside.",
   [("knock", "ދޮރުހުޅުވަބަލަ", -14)])
sh(15, "Hayaathu looked at the door in fear. She hurried over and opened it. 'Here's your phone,' Areesha said, holding it out to her.",
   [("door_open", "ދޮރުހުޅުވާލިއެވެ", -16)])
sh(16, "Hayaathu quickly took the phone. 'Not to call Maaroof — Dad said Fazaal will call soon. Who knows why. Don't make him angry...'")
sh(17, "Areesha said harshly. Hayaathu stared at Areesha in surprise. Areesha smirked with one side of her mouth.")
sh(18, "And began speaking mockingly. 'Don't pretend you don't know... it's your beloved Fazaal.'")
sh(19, "Looking at Hayaathu with a mocking smile, Areesha said, 'Hmm... Prince Fazaal — taking you to his island, Dubai, is he?'")
sh(20, "she said scornfully. 'Then we'll never even get to see you,' Areesha said with a laugh.")
sh(21, "Without a word Hayaathu turned inside with the phone. 'Hey, wait — shouldn't you look at Prince Fazaal's photo once more?'",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -26)])
sh(22, "Areesha said, holding Hayaathu's hand to stop her. Hayaathu glared at Areesha. 'The photo's on the phone.")
sh(23, "I've already sent it to Maaroof too. Oh — and to your classmates as well.")
sh(24, "Read the messages they wrote. If I hadn't sent it before, they'd get a big shock at the wedding party — the kind of shock I got when I saw Fazaal's photo.'")
sh(25, "Areesha went on, laughing. 'When I saw Fazaal's photo and then looked at you, I thought of Beauty and the Beast...'")
sh(26, "Areesha said mockingly, looking at Hayaathu's face. Hayaathu listened to Areesha with her teeth clenched.", hum=True)
sh(27, "'Now wait for the call... bye...' Pressing harder on Hayaathu's wound, Areesha left.",
   [("footsteps_pavement", "ނިކުމެގެން", -26)])
sh(28, "When Areesha left, Hayaathu locked the door again. Areesha banged on it again. Hayaathu opened the door.",
   [("lock_click", "ތަޅުލިއެވެ", -16), ("knock", "ޖަހާލިއެވެ", -14), ("door_open", "ދޮރުހުޅުވާލިއެވެ", -18)])
sh(29, "'Dad said to keep the door unlocked — otherwise you'll secretly call Maaroof.' With that, Areesha went away.")
sh(30, "Hayaathu shut the door and climbed onto the bed. Slowly she opened the phone and looked at the photo on the screen. Her heart started pounding.",
   [("door_close", "ދޮރުލައްޕާފައި", -20), ("heartbeat", "ތެޅިގަނެގެން", -16)])
sh(31, "She shut her eyes tight and tossed the phone away from her. 'What a frightening face!' Her heart kept pounding.",
   [("soft_thud", "އެއްލާލިއެވެ", -18)], hum=True)
sh(32, "'What crime am I being punished for? Why is uncle doing this to me? What is my fault?")
sh(33, "Why is he marrying me to a man so much older than me?' Hayaathu said, sobbing.", [("sob_breath", "ގިސްލާ", -24)])
sh(34, "Just then her phone began to ring. She stared at it in fear. With a trembling hand she picked it up. An unknown number.",
   [("phone_buzz", "ރިންގުވާން", -14)])
sh(35, "Hayaathu was sure it was Fazaal. Frightened, she lifted the phone to her ear. 'H-hello,' she said softly.")
sh(36, "No answer from the other end. With a racing heart she spoke again. 'H... hello... who is it?'", [("heartbeat", "ތެޅިތެޅި", -18)])
sh(37, "she asked fearfully. Just then her uncle appeared at the door and looked at her. 'Whose call?' Waheed thought it was Fazaal.",
   [("door_open", "ދޮރުމައްޗަށް", -20)])
sh(38, "He asked before she could say anything. 'I don't know who — they're not saying anything,' she said, scared. 'Put that phone down, get dressed and come out. The witness for the ring ceremony will be here soon.'")
sh(39, "Waheed said harshly. 'But uncle...' Not knowing who was on the other end of the phone, Hayaathu started talking to Waheed.")
sh(40, "She put the phone to one side. 'There's nothing to argue about. If you want to meet Dhooma, get ready for the ring ceremony. Because of you I can barely breathe —")
sh(41, "seeing Fazaal's ugly face I had decided not to marry Areesha to him, and your big mouth caused all this — accusing Areesha without the truth, humiliating her —")
sh(42, "now look at that face for the rest of your life,' Waheed said harshly. 'Please uncle, just listen to me once.'")
sh(43, "Hayaathu began to cry. 'I don't want to hear your nonsense. Do you think I don't see the truth?",
   [("sob_breath", "ރޮވެން", -24)], hum=True)
sh(44, "Everything Areesha said is the truth,' said Waheed. 'No uncle, I never accused Areesha. All I said was it's not that man's fault that he's ugly...'")
sh(45, "Hayaathu said, crying. 'You have no right to say that.' With that Waheed started to walk out. 'Uncle,",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(46, "let me see Dhontha just once.' Hayaathu began to sob. 'First the ring ceremony...' Waheed said. 'I'll do everything you say, uncle.",
   [("sob_breath", "ގިސްލެވެން", -24)])
sh(47, "Dhontha...' Hayaathu said, sobbing. 'Zoona, bring Dhooma here...' Waheed shouted. 'Be ready in 15 minutes.", hum=True)
sh(48, "And no crying when you talk to Dhooma,' Waheed said sternly. 'I won't cry...' she said, quickly wiping the tears from her eyes.")
sh(49, "A little later Zoona came in pushing Dhooma's wheelchair. She left Dhooma there and went out.",
   [("wheelchair_roll", "ކޮއްޕަމުން", -18), ("footsteps_pavement", "ނިކުމެގެން", -26)])
sh(50, "Hayaathu ran and threw her arms around Dhooma. 'Dhontha...' she tried to speak in a tearful voice.",
   [("footsteps_pavement", "ދުވެފައި", -24), ("sob_breath", "ރޮވިފައިވާ", -24)])
sh(51, "Dhooma seemed to understand what she wanted to say. 'For my little sister... a happy... a happy life... I wanted to find... to find...", hum=True)
sh(52, "but... what... what can be done... no... no luck... for this person...'", hum=True)
sh(53, "Dhooma said with great effort, stroking Hayaathu's cheek. Hayaathu kissed Dhooma's hand and laid her head in her lap. Tears began to flow.", hum=True)
sh(54, "'Dhontha, don't think about luck... don't bury hope before the grave... I...")
sh(55, "in a way I think I'm lucky — to have such a lovely sister...' Hayaathu said softly, bitterly.")
sh(56, "'I don't want a life where I can't see you. I'll marry Fazaal,' Hayaathu said, wiping her tears. 'No. Hayaathu...")
sh(57, "that man...' Dhooma tried to say. 'Even if he's older than me, it doesn't matter...")
sh(58, "Even if Fazaal is older and has an ugly face, in the future he'll be my husband... I've made my heart understand.")
sh(59, "Like you, Dhontha, he is a victim of circumstance. His ugly face is his fate. Getting a husband with such a face is my fate.")
sh(60, "How can anyone fight fate, Dhontha...' Hayaathu said bravely in a tearful voice. 'Hayaathu... it will be hard for you... that ma...", hum=True)
sh(61, "that man...' Dhooma tried to say. Hayaathu stroked Dhooma's cheek. 'If my eyes pretend not to see, there'll be no difficulty,' she smiled.")
sh(62, "'Feelings come from what we see. Beauty and ugliness are told apart by sight. If my eyes don't see, how could I describe a face?...'")
sh(63, "Hayaathu forced a smile. 'Where's Hayaathu?' came Waheed's voice from outside. 'They'll be here in 5 minutes...'")
sh(64, "Hearing Waheed's voice Hayaathu smiled bitterly. Wiping the tears from her eyes, she walked out.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(65, "Dhooma kept begging her not to go. She had put the phone down on the table. From the sounds Fazaal heard, he understood how Hayaathu was being forced, and how cruel Waheed was.", hum=True)
sh(66, "But there was nothing he could do either. On the new road from Dubai to Malé he had learned the marriage with Areesha was off, and he was glad.")
sh(67, "Because he didn't want to marry anyone. On purpose he had sent Waheed his brother's photo — a brother seven years older than him.")
sh(68, "In a fire, Fazaal's brother Fawaz's face had been changed, and because of that the girl he was going to marry left him —", hum=True)
sh(69, "and in that heartbreak Fawaz left this world. Because of it Fazaal came to hate women intensely.", hum=True)
sh(70, "In his eyes every woman loves only beauty and is full of selfish desire. So whenever he proposed to anyone, Fazaal gave all his introductions in Fawaz's name.")
sh(71, "As soon as his flight landed at the airport, he hurried off it and onto the next flight straight to Addu.",
   [("plane_pass", "ޖެއްސުމާއި", -18)])
sh(72, "He went to Addu to spend a holiday, since he'd come to the Maldives even though Areesha refused. Driving from the airport to their big house, his car very nearly hit Dhooma and Hayaathu.",
   [("brake_screech", "އެކްސިޑެންޓު", -14)])
sh(73, "Fazaal got out of the car in anger to shout at them, to take his anger out on them.", [("car_door", "ފޭބީ", -16)])
sh(74, "But Hayaathu paid him no attention. All her attention was on Dhooma, sitting in the wheelchair.")
sh(75, "Seeing Hayaathu's face, Fazaal was stunned. His heart beat faster. He wanted to see her closer.",
   [("heartbeat", "ވިންދު", -16)])
sh(76, "Was it really her? his heart asked at that moment. How could it be? his mind answered.")
sh(77, "Fazaal listened clearly to what the two girls were saying. And at that very moment a message from his father arrived on his phone.",
   [("phone_buzz", "މެސެޖު", -16)])
sh(78, "Fazaal looked at the message, his thoughts still on Hayaathu. His father had sent a photo. Seeing it, Fazaal was amazed.")
sh(79, "Looking carefully at the photo his father sent, he was sure what he'd just seen was no illusion. The girl he was now engaged to was her.")
sh(80, "Fazaal's heart beat harder than before. He felt something he couldn't describe. And seeing her tenderness and love for her sister, a space opened in his heart without him knowing.",
   [("heartbeat", "ވިންދު", -16)], hum=True)
sh(81, "Without meaning to, Fazaal went after the two girls. He parked the car to one side and followed them, listening to what they were saying.",
   [("car_door", "ޕާކު", -20)])
sh(82, "From what they said Fazaal knew Hayaathu had a pure heart. He didn't want to let such a priceless jewel go.")
sh(83, "After Maaroof, Fazaal too had jumped into the sea to save Hayaathu.", [("splash", "ފުންމާލީ", -10)], hum=True)
SHOTS = S

"""Beat/shot plan for Bappage Gatulu episode 521, v2 re-cut on the new audio (used by plan_beats.py).
v1 images are reused via v1="beat_###"; new images only for spec 5.4 (speaker centred)."""

ROOM = ("Iyaan's small bedroom in a modest Hulhumalé apartment: a plain desk with two computer monitors, a keyboard and a "
        "mouse, a black office chair, a wall-sized investigation board covered with small faceless blurred photos linked "
        "by red string, a narrow single bed with a small lamp on the bedside table, a window with half-open blinds, "
        "grey painted walls")

LOC = {
    "room_day": ROOM + ", seen in daylight with the window open onto the busy streets of the city below",
    "entrance": "the narrow entrance hall of a small modest apartment in Hulhumalé, a plain front door standing open onto a "
                "bright corridor, a shoe rack, a framed dried-flower picture, pale tiled floor",
    "storeroom": "a small cramped windowless storeroom deep inside a modest apartment, dusty metal shelves with old cardboard "
                 "boxes and bundles of yellowed paper, a single bare bulb hanging from the ceiling, and in the corner a "
                 "large old dark-wood chest with brass corners and an old iron lock, dust motes floating in the air",
    "memory": "the cosy sitting room of a family home in Malé in 2011: a worn fabric sofa, a small table lamp, rain streaming "
              "down a dark window behind",
    "room_night": ROOM + ", at night with the lights off",
    "board": ROOM + ", at night, the investigation board on the wall lit by a single desk lamp",
}
MOOD = {
    "room_day": "present day, late afternoon, hazy grey-gold daylight through the blinds, muted teal shadows inside, "
                "restless and brooding",
    "entrance": "present day, morning, soft white daylight from the corridor, quiet and tender with a note of loneliness",
    "storeroom": "present day, evening, the dim yellow light of a single bare bulb, deep charcoal shadows, dusty, "
                 "hushed and expectant",
    "memory": "2011, stormy night, cold desaturated blue-grey haze, one small warm lamp glowing on their faces, a soft "
              "dreamlike vignette, tender",
    "room_night": "present day, late at night, the room dark except for the cold blue light of the computer screens and "
                  "the faint amber glow of a small bedside lamp, tense and secretive",
    "board": "present day, late at night, a single desk lamp throwing hard amber light on the board, deep red and teal "
             "shadows around, the screens' blue glow behind, cold controlled fury",
}

BEATS = [
    dict(to=3, v1="beat_001", reason="episode opening: Iyaan at his window, brooding over where his father hid the files",
         chars=["iyaan"], loc="room_day",
         visual="Iyaan standing at his bedroom window with one hand holding the blind aside, looking down at the busy "
                "street below full of motorbikes and cars, his face in three-quarter profile, serious and brooding; "
                "behind him in soft focus the desk with two dark monitors and the edge of the investigation board with "
                "red string",
         camera="medium shot from inside the room, eye level, Iyaan in the upper half, the plain desk top as a calm lower third",
         amb="road_busy"),
    dict(to=5, v1="beat_002", reason="new focus: his father's old wristwatch stopped at the time of his death; he grips it",
         chars=["iyaan"], loc="room_day",
         visual="close-up of Iyaan's hand holding an old silver analog wristwatch with a cracked glass and a plain dial "
                "without any numerals, its two hands stopped at a quarter past eleven; behind it, slightly out of focus, "
                "Iyaan's face looking down at it, jaw tight, eyes heavy with grief",
         camera="close-up, slightly high angle, the watch and his face in the upper two-thirds, the dark desk top below",
         amb="room_day", sens="other",
         safe="the time of the father's death is shown only as an old stopped watch with a plain dial, no numbers"),
    dict(to=7, v1="beat_003", reason="time jump and new character: the day his mother leaves for treatment on an island",
         chars=["aminath", "iyaan"], loc="entrance", transition="black",
         visual="Aminath at the open front door of the apartment, a small travel bag at her feet and prayer beads in her "
                "hand, turning back to look at her son with a weary loving smile; Iyaan standing a step behind her in the "
                "hallway holding a second small bag, giving a gentle reassuring nod",
         camera="medium wide shot, eye level, faces in the upper half, the pale tiled floor as a calm lower third",
         amb="home_day"),
    dict(to=10, v1="beat_004", reason="scene change: alone in the empty apartment he opens the dark storeroom; the wooden chest",
         chars=["iyaan"], loc="storeroom",
         visual="Iyaan standing in the open doorway of the small dark storeroom, one hand on the door frame, the light "
                "from the hallway falling past him into the dust; his eyes fixed on a large old dark-wood chest with brass "
                "corners and an old iron lock in the far corner",
         camera="medium wide shot from inside the storeroom, low angle, Iyaan in the upper half, the dusty floor as a calm lower third",
         amb="room_night"),
    dict(to=12, v1="beat_005", reason="action change: he blows off the dust, opens the old lock and searches the files",
         chars=["iyaan"], loc="storeroom",
         visual="Iyaan kneeling in front of the open wooden chest under the bare bulb, the heavy lid raised, holding up an "
                "old faded file folder and studying it closely; old books, bundles of letters and blank yellowed papers "
                "stacked inside the chest and beside him on the floor, dust swirling in the light",
         camera="medium shot, slightly high angle, his face in the upper half, the chest and papers in the lower third",
         amb="room_night"),
    dict(to=14, v1="beat_006", reason="action change: an hour later, disappointed, the chest emptied; his hand on its bottom",
         chars=["iyaan"], loc="storeroom",
         visual="Iyaan sitting on the storeroom floor surrounded by piles of old files, books and envelopes, the wooden "
                "chest in front of him completely empty; his shoulders slumped in tired disappointment, one hand resting "
                "flat on the bottom inside the chest, a sudden puzzled frown appearing on his face",
         camera="medium wide shot, eye level, his face in the upper half, the piles of paper on the floor as the lower third",
         amb="room_night"),
    dict(to=17, v1="beat_007", reason="turning point: the false bottom lifts and reveals the hidden black hard drive",
         chars=["iyaan"], loc="storeroom",
         visual="close-up from above into the empty wooden chest: Iyaan's hands lifting a thin wooden panel from its bottom, "
                "revealing a hidden shallow compartment in which lies a black metal-cased hard drive; Iyaan's face above "
                "it at the top of the frame, eyes wide, breath held, lit by the bare bulb",
         camera="close-up, high angle looking down into the chest, his face at the top of the frame",
         amb="room_night"),
    dict(to=21, v1="beat_008", reason="scene change: in his locked room he connects the drive — military-grade encryption",
         chars=["iyaan"], loc="room_night",
         visual="Iyaan seated at his desk in the dark locked room, both hands on the keyboard, the black metal hard drive "
                "connected by a cable beside the keyboard; both monitors show a large glowing red padlock symbol and "
                "abstract streams of glowing code with no readable characters; the colour has drained from his face, his "
                "eyes narrowed in concentration",
         camera="medium shot from the side and slightly behind, his face in profile in the upper half, the desk top below",
         amb="hacker_room", sens="other",
         safe="the 'enter code' message is shown only as a red padlock glow, no readable text"),
    dict(to=23, v1="beat_009", reason="emotional turning point: three failed attempts, near lockout; he stops to think",
         chars=["iyaan"], loc="room_night",
         visual="close-up of Iyaan's tense face bathed in a pulsing red warning glow from the screen, two fingers pressed "
                "against his temple, lips pressed together, thinking hard; the edge of the monitor glowing red in the foreground",
         camera="close-up, eye level, his face in the upper two-thirds, the dark desk edge as a calm lower third",
         amb="hacker_room"),
    dict(to=26, v1="beat_010", reason="memory (2011): his father whispering his favourite saying into the boy's ear",
         chars=["zahir", "iyaan_young"], loc="memory", transition="dissolve",
         visual="Ahmed Zahir sitting on the sofa beside his eight-year-old son, leaning down with a warm smile to whisper "
                "into the boy's ear, one hand resting fondly on the boy's shoulder; the boy listening with wide attentive "
                "eyes; rain streaming down the dark window behind them",
         camera="medium close-up two-shot, eye level, faces in the upper half, the sofa cushions as the lower third",
         amb="memory_rain"),
    dict(to=27, reason="return from the memory to the desk: he turns the saying into a code and types it in",
         loc="room_night", reuse="beat_008", transition="dissolve",
         visual="(reuse of beat_008: Iyaan typing at the desk in front of the red padlock glow)",
         amb="hacker_room"),
    dict(to=31, v1="beat_012", reason="turning point: access granted — a green glow, the files open, his eyes widen",
         chars=["iyaan"], loc="room_night",
         visual="Iyaan leaning close to the monitors, his face washed in a soft bright green glow from the screens, eyes "
                "wide and lips slightly parted in disbelief; the screens show only a plain green glow and rows of "
                "abstract glowing folder shapes with no letters",
         camera="medium close-up from beside the monitors, his face in the upper half lit green, the keyboard in the lower third",
         amb="hacker_room", sens="other",
         safe="'ACCESS GRANTED' is shown only as a green glow, no readable text"),
    dict(to=34, v1="beat_013", reason="new framing: the dark room lit only by the small lamp and the blue screens; trembling fingers",
         chars=["iyaan"], loc="room_night",
         visual="wide view of the dark bedroom: the only light is a small lamp on the bedside table and the cold blue glow "
                "of the two monitors; Iyaan seated at the desk seen from the side, hunched forward, his fingers resting on "
                "the mouse, tense and still",
         camera="wide shot, eye level, Iyaan and the glowing screens in the upper half, the dark floor as a calm lower third",
         amb="hacker_room"),
    dict(to=37, v1="beat_014", reason="new focus: what the files reveal — secret land and lagoon sales, millions in accounts",
         chars=["iyaan"], loc="room_night",
         visual="over-the-shoulder view past Iyaan's head and shoulder onto the two monitors: one shows an aerial map of "
                "small green islands and turquoise lagoons with glowing outlines around some of them, the other shows "
                "blurred document pages and abstract bar graphs; no letters, no numbers; the blue light on his cheek",
         camera="over-the-shoulder medium shot, the screens in the upper two-thirds, the desk top as the lower third",
         amb="hacker_room", sens="other",
         safe="documents and bank details are shown only as blurred pages, an island map and abstract graphs"),
    dict(to=40, v1="beat_015", reason="action change: he puts on headphones and plays the 2011 audio file; the voice chills him",
         chars=["iyaan"], loc="room_night",
         visual="Iyaan wearing black over-ear headphones, one hand still pressing them to his ear, frozen in his chair; "
                "on the monitor in front of him a single glowing blue audio waveform; his eyes wide and fixed, a chill "
                "running through him",
         camera="medium close-up, eye level, his face in the upper half, the desk and keyboard in the lower third",
         amb="hacker_room"),
    dict(to=41, v1="beat_016", reason="new character visible: the voice belongs to Asim, the Home Minister he sees on TV",
         chars=["asim", "iyaan"], loc="room_night",
         visual="Iyaan seen from behind and slightly to the side, wearing headphones and staring at his monitors: the left "
                "monitor shows a paused news video of a heavy-set grey-moustached man in a crisp white shirt speaking at a "
                "podium with microphones, with no captions, no ticker and no logos; the right monitor shows the glowing "
                "audio waveform",
         camera="medium shot from behind Iyaan's shoulder, the screens in the upper two-thirds, the dark desk below",
         amb="hacker_room", sens="other",
         safe="Asim is only a voice on the recording; he is shown only as a paused video on the monitor, no text"),
    dict(to=44, reason="5.4: the recorded phone call (Asim and his caller are only voices) — back on the listener, Iyaan "
                       "centred with his headphones",
         loc="room_night", reuse="beat_015",
         visual="(reuse of beat_015: Iyaan frozen with the headphones on, the waveform glowing)",
         amb="hacker_room", sens="other",
         safe="the voices on the 2011 recording are never shown; the listener is centred instead"),
    dict(to=48, v1="beat_017", reason="emotional peak: Asim's cruel laugh and the order — Iyaan's jaw clenches",
         chars=["iyaan"], loc="room_night",
         visual="extreme close-up of Iyaan's face with the headphones on, his jaw clenched hard and teeth gritted, eyes "
                "burning with shock and rage, a faint red reflection of the audio waveform glowing in his dark eyes",
         camera="extreme close-up, eye level, his eyes in the upper third, soft darkness below",
         amb="hacker_room", sens="violence",
         safe="the spoken order is never visualised; only Iyaan's face listening"),
    dict(to=51, v1="beat_018", reason="action change: the audio ends, he flings the headphones down; the answer after 15 years",
         chars=["iyaan"], loc="room_night",
         visual="the black headphones lying where they were flung on the desk in the sharp foreground; behind them Iyaan "
                "pushed back in his chair, one hand pressed against his chest, breathing hard, staring straight ahead in "
                "stunned silence, the screens glowing blue",
         camera="medium shot, low angle from the desk top, the headphones in the lower third, his face in the upper half",
         amb="hacker_room"),
    dict(to=52, v1="beat_019", reason="action change: at the board he removes the centre card, pins Asim's photo and circles it in red",
         chars=["iyaan"], loc="board",
         visual="Iyaan alone in his room, the only person in the scene, standing close to the wall-sized investigation "
                "board and pinning a small printed head-and-shoulders portrait photo (palm-sized, of a heavy-set older man "
                "with a thick grey moustache and a white shirt) into the centre of the board where the red strings "
                "converge, drawing a red circle around the little portrait's face with a red marker; small faceless "
                "blurred photos all around; his face hard and cold",
         camera="medium shot from the side, Iyaan and the portrait in the upper half, the dark desk corner below",
         amb="room_night", sens="other",
         safe="Asim appears only as a small portrait photo on the board, no text, no question mark"),
    dict(to=54, speaker="iyaan",
         reason="5.4 dialogue: Iyaan growls at Asim's circled photo ('Asim... did you think...') — the v1 board image shows "
                "him in profile at the top edge, so a new frame centred on his face",
         chars=["iyaan"], loc="board",
         visual="Iyaan alone in his room, the only person in the scene, standing in front of the wall-sized investigation "
                "board and turned three-quarters towards the camera, a red marker still in his raised right hand; on the "
                "board just beside his shoulder a small palm-sized portrait photo of a heavy-set older man with a thick grey "
                "moustache and a white shirt, freshly circled in red marker, the red strings converging on it; Iyaan's lips "
                "parted as he growls through clenched teeth, his dry eyes cold and burning, his face sharp in the hard amber "
                "lamp light; small faceless blurred photos all around, slightly out of focus",
         camera="medium close-up, eye level, Iyaan's face centred in the upper half of the frame and in sharp focus, the "
                "board soft behind him, his dark t-shirt and the shadowed desk corner as a calm lower third",
         amb="room_night", sens="other",
         safe="Asim appears only as a small portrait photo on the board, no text, no question mark"),
    dict(to=59, v1="beat_020", reason="emotional framing: no tears — a dangerous fire in his eyes; the revenge plan forms",
         chars=["iyaan"], loc="board",
         visual="close-up of Iyaan's face in near-darkness in front of the board, his dry eyes steady and burning with a "
                "dangerous cold fire, half of his face lit amber by the lamp and half in deep red-teal shadow, the red "
                "strings and the small circled portrait blurred behind him",
         camera="close-up, eye level, his face in the upper two-thirds, soft shadow below",
         amb="room_night"),
    dict(to=63, v1="beat_021", reason="action change: hours of research at the computer — Raaya, Asim's only daughter, on his screen",
         chars=["iyaan", "raaya"], loc="room_night",
         visual="Iyaan seated at his desk in profile, a slow dangerous smile on his lips, looking at the main monitor which "
                "shows a photo of a young woman in a white dress and light-grey hijab smiling among large modern paintings "
                "in an art gallery; the second monitor shows a grid of blurred photos; she appears only as a photo on the "
                "screen, a clear arm's-length gap and more between them",
         camera="medium shot from the side, Iyaan's profile and the screen in the upper half, the desk top as the lower third",
         amb="hacker_room", sens="other",
         safe="Raaya is not physically present; she appears only as a photo on the monitor, no text"),
    dict(to=64, speaker="iyaan",
         reason="5.4 dialogue: 'This is the door into Asim's world,' Iyaan says to himself — the v1 image shows him in "
                "profile at the left edge, so a new frame centred on his face",
         chars=["iyaan"], loc="room_night",
         visual="medium close-up of Iyaan, alone, seated at his desk in the dark room, the camera placed just beside his "
                "monitor so that his face is seen three-quarters from the front, lit by the cold blue-white glow of the "
                "screen; a slow dangerous smile on his lips, eyes narrowed and calculating, murmuring to himself; the "
                "glowing edge of the monitor soft at the right edge of the frame; behind him at the left, out of focus, a "
                "second monitor showing a small blurred photo of a young woman in a white dress and light-grey hijab among "
                "paintings, and the dark investigation board with red string",
         camera="medium close-up, eye level, Iyaan's face centred in the upper half of the frame and in sharp focus, the "
                "background soft, the dark desk top and keyboard as a calm lower third",
         amb="hacker_room", sens="other",
         safe="Raaya is not physically present; she appears only as a small blurred photo on a screen, no text"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Iyaan took a deep breath. He got up, went over and looked out of the window. From outside came the noise of vehicles racing along Malé's chaotic streets.",
   [("breath", "ނޭވާއެއް", -22), ("motorbike_pass", "ދުއްވާއެއްޗެހީގެ", -20)])
sh(2, "His heart kept telling him that the real evidence of his father's death must be somewhere. His father was a man who did everything with great planning.")
sh(3, "Where were the political corruption files his father had gathered before he died? If those files were found, he would know who the killer was.")
sh(4, "Iyaan looked at his father's old watch lying on his desk. That watch had stopped at the moment his father died — at a quarter past eleven.")
sh(5, "Iyaan took the watch in his hand and squeezed it hard. He began to feel that the silence of his life was coming close to its end.")
sh(6, "The end of Iyaan's waiting came on the day his mother Aminath had to go to an island for medical treatment.")
sh(7, "With his mother's departure, emptiness took over the whole apartment. But for Iyaan this was the biggest opportunity he had had in the past fifteen years.",
   [("door_close", "ފުރައިގެން", -20)])
sh(8, "Without his mother knowing, Iyaan decided to search through the things linked to his father's memories that his mother always kept safe.")
sh(9, "That was out of concern for how it would affect her heart if he did it in front of her. Iyaan headed for the small storeroom at the very back of the home.")
sh(10, "It was a dark place that smelled of old paper the moment the door opened. In a corner of the room stood the big wooden chest that his father, Ahmed Zahir, had kept in his lifetime.",
   [("door_open", "ހުޅުވާލުމާއެކު", -18), ("creak", "ދޮރު", -22)])
sh(11, "After a deep breath, Iyaan blew off the dust on top of the chest. And he opened its old lock. Inside the chest were the old files his father had used in parliament, books, and some personal letters.",
   [("breath", "ނޭވާއެއްލުމަށްފަހު", -22), ("box_unlock", "ހުޅުވާލި", -16), ("page_turn", "ފައިލްތަކާއި", -22)])
sh(12, "Iyaan went through every paper one by one. But in none of it did he find the political secret he was looking for.",
   [("paper_shuffle", "ކަރުދާހެއް", -20)])
sh(13, "After about an hour of work Iyaan began to lose hope. He took everything in the chest out. The chest was completely empty.",
   [("sigh", "މާޔޫސްވާން", -22), ("paper_shuffle", "ނެގި", -22)])
sh(14, "But the moment Iyaan ran his hand over the bottom of the chest, he noticed something unusual. The height of the chest on the outside and its depth on the inside did not match.")
sh(15, "He pressed hard on the bottom of the chest. Suddenly a part of the bottom lifted up a little. It was a secret compartment. Iyaan's heart began to pound.",
   [("creak", "ހިއްލިގެން", -18), ("heartbeat", "ތެޅެން", -20)])
sh(16, "Slowly he lifted out that piece of wood. Inside lay a black, metal-cased, modern hard drive.")
sh(17, "Although his father died in 2011, this hard drive was, for its time, the most expensive kind, used to store secret information.")
sh(18, "Iyaan grabbed the hard drive, almost ran into his room and locked the door. He connected the hard drive to the computer system on his desk.",
   [("footsteps_pavement", "ދުވެފައި", -22), ("lock_click", "ތަޅުލި", -16), ("computer_beep", "ގުޅާލި", -20)])
sh(19, "The message that came up on the screen changed the colour of Iyaan's face: \"Military-grade encryption. Enter the code.\"",
   [("computer_beep", "ސްކްރީނަށް", -20)])
sh(20, "This was not a code even an ordinary hacker could break. But Iyaan was a digital-forensics expert.")
sh(21, "Using all kinds of software, he set to work breaking the code. His first three attempts all failed.",
   [("keyboard_typing", "ސޮފްޓްވެއާތައް", -20)])
sh(22, "The hard drive was close to locking itself. Iyaan stopped to think. In everything, his father gave priority to family secrets and memories.",
   [("alarm_beep", "ބްލޮކްވާން", -20)])
sh(23, "His father would only use the name or date that mattered most to him. Iyaan typed in his father's birthday, his mother's name and their wedding date.",
   [("keyboard_typing", "ޖަހާލި", -20)])
sh(24, "None of them matched. Then Iyaan remembered something his father had said close to his ear a few days before he died.")
sh(25, "\"My son, after every storm, the birds sing",
   hum=True, speaker="zahir", crop="tight", focus=[44, 37])
sh(26, "in calm weather.\" It was a wise saying his father always used to repeat. Iyaan translated those words into English and arranged the letters and numbers the way his father usually made his codes.",
   speaker="zahir", crop="medium", focus=[44, 42])
sh(27, "And with his very last chance he entered the code. The computer screen blinked twice. And a green message appeared.",
   [("keyboard_typing", "އެންޓާ", -20), ("computer_beep", "ބްލިންކްވެލި", -18)])
sh(28, "\"Access granted.\" It was as if a cold wave ran through Iyaan's body. The files inside the hard drive opened up.",
   [("computer_beep", "ގްރާންޓެޑް", -18)])
sh(29, "They were huge secret documents that could turn the country's political stage upside down.")
sh(30, "Details of bank accounts, and lists of how black money had been shared out. Iyaan's eyes widened.")
sh(31, "His father had torn the curtain off a network at the very top of the country. Iyaan began reading those files with complete certainty that they would lead him to the truth of his father's death.")
sh(32, "Iyaan's eyes stayed fixed on the folders inside the hard drive. Apart from the soft light of a small lamp by the bed, the whole room was ruled by the blue light of the computer screen.")
sh(33, "Iyaan's fingers trembled on the mouse from a fear he could not name. He opened every file one by one.")
sh(34, "In them were detailed reports of the biggest betrayals going on on the Maldives' political stage in 2011.")
sh(35, "Details of bank accounts into which millions of dollars had flowed from secretly selling off state land and lagoons.")
sh(36, "The more Iyaan read, the more he silently praised his father's courage. What Ahmed Zahir had found were no ordinary secrets.")
sh(37, "He had exposed the truth of a network secretly controlling the whole state. At the very bottom of the files Iyaan saw a folder named \"Confidential Audio 2011\".")
sh(38, "When he opened the folder there was just one audio file inside. Iyaan put his headphones on his ears. He played the audio file.",
   [("computer_beep", "ޕްލޭ", -22)])
sh(39, "First came the sound of a phone ringing. Then came a heavy, somewhat rough male voice.",
   [("phone_buzz", "ރިންގުވާ", -18)])
sh(40, "As soon as he heard that voice, Iyaan felt as if the blood in his whole body had frozen. It was a voice he heard almost every day on TV and in the news.",
   [("heartbeat", "ކެކިގަތް", -20)])
sh(41, "It was the voice of today's powerful Home Minister, Asim. Asim was a minister even back then. Years later, today, he is the Home Minister.")
# 42-48: the 2011 recording — Asim and his caller are only voices (bible rule 10), so `speaker` stays unset and the
# listener Iyaan (headphones) is centred instead.
sh(42, "\"So, how did things go?\" came Asim's voice, asking on the phone. Then came another man's voice.",
   crop="tight", focus=[44, 35])
sh(43, "\"Minister, Zahir has all the documents. He is planning to submit them to parliament tomorrow. Our attempts to scare him didn't work.\"",
   crop="medium", focus=[44, 42])
sh(44, "\"He said that for the sake of the country's youth he will wash corruption out of this soil.\" The sound of Asim laughing loudly came through the audio.",
   crop="tight", focus=[44, 35])
sh(45, "The cruelty and ruthlessness in that laugh made Iyaan grit his teeth. \"Zahir has started talking far too much.\"",
   crop="tight", focus=[52, 52])
sh(46, "Asim's voice suddenly turned dangerous. \"Does he think he can bring down the whole government?",
   crop="medium", focus=[52, 50])
sh(47, "Shut his mouth for good. Make tonight his last night in this world. And",
   hum=True, crop="tight", focus=[52, 52])
sh(48, "find the hard drive he has and destroy it. When that's done, the rest of the money will go into the account.\"",
   crop="medium", focus=[52, 50])
sh(49, "The audio cut off. Iyaan pulled off the headphones and threw them onto the desk. His heart was pounding unusually hard.",
   [("soft_thud", "އެއްލާލި", -18), ("heartbeat", "ތެޅެމުންދިޔަ", -18)])
sh(50, "The answer to the question he had searched for over the past fifteen years had come to him today. It was Asim who directly ordered his father's death.")
sh(51, "Responsibility for every drop that fell from his father's body lies with the Home Minister dressed in white, who today is in charge of the nation's security.",
   hum=True)
sh(52, "Iyaan got up, went over and stopped in front of the big board on his room's wall. He removed the big question mark in the middle of the board.",
   [("cloth_rustle", "ތެދުވެގެން", -22)])
sh(53, "And in its place he pinned up a photo of Asim. With a red marker he drew a circle around Asim's face. \"Asim...\"",
   [("paper_shuffle", "ހަރުކޮށްލި", -22), ("pen_scribble", "މާކަރަކުން", -18)], speaker="iyaan", crop="medium", focus=[49, 42])
sh(54, "\"Did you think your crimes were hidden? Did you think that because fifteen years have passed, you were safe?\"",
   hum=True, speaker="iyaan", crop="tight", focus=[49, 35])
sh(55, "A painful growl came out of Iyaan's voice. Not a tear came from Iyaan's eyes. But in his eyes burned a dangerous fire.",
   hum=True)
sh(56, "The spirit of revenge in his heart had now grown unusually strong. Iyaan was a patient, calculating young man.")
sh(57, "He knew that simply going straight at Asim and taking his life was not something that could be done.")
sh(58, "What Iyaan wanted was to see the whole political might Asim had built, his honour, his influence and his family shatter to pieces before his eyes.")
sh(59, "To see him, when the ground slid from under Asim's feet, begging in fear for mercy.")
sh(60, "Iyaan went back to the computer again, sat down, and began gathering information on Asim's private life.",
   [("cloth_rustle", "އިށީނދެ", -24)])
sh(61, "He began looking for the weak point of all Asim's influence. After many hours of research, Iyaan found that point.",
   [("keyboard_typing", "ހޯދަން", -22)])
sh(62, "It was Asim's only child, Raaya. Raaya was a free-thinking young woman, far from politics, who runs a big art gallery in Malé.")
sh(63, "Asim loves his daughter beyond measure. Iyaan sat staring at the screen and smiled dangerously.")
sh(64, "\"This is the door into Asim's world,\" Iyaan said to himself. Iyaan began preparing to take the first step of his revenge. To be continued.",
   speaker="iyaan", crop="tight", focus=[55, 43])
SHOTS = S

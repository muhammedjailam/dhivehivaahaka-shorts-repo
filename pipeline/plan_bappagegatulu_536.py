"""Beat/shot plan for Bappage Gatulu episode 536 (used by plan_beats.py). PRESENT timeline only (plus one memory)."""

LOC = {
    "bank_office": "the managing director's corner office high in a modern glass bank tower in Malé, a large dark polished desk with a slim laptop, a black leather executive chair, floor-to-ceiling windows looking over the city rooftops and the turquoise sea, cold grey-and-steel interior with a few dark wood accents",
    "bank_it": "a cramped bank IT room behind the executive floor, a desk with three monitors showing abstract glowing network maps and graph lines, server racks with tiny blinking lights along one wall, cables, blinds half drawn",
    "lounge": "a secret private lounge on an upper floor in Hulhumalé, dark wood-panelled walls, heavy closed burgundy curtains, three deep leather armchairs around a low polished dark-wood table that is bare except for a few phones, dim brass floor lamps, no windows visible",
    "gallery": "the Athena Art Gallery in Malé, white walls hung with large modern oil paintings, a big oil painting of a red sun rising out of a black sea, polished concrete floor, soft track lighting, a big glass door",
    "hacker_room": "Iyaan's small locked bedroom-study in a modest apartment in Hulhumalé, a desk with three computer monitors glowing with abstract code lines and graphs, a keyboard and a pair of black over-ear headphones, a wall-sized investigation board with small faceless blurred photos linked by red string, window blinds drawn",
    "studio": "a silent rented art studio on the third floor of an old building in a quiet Malé lane, bare peeling plaster walls, blank canvases stacked against a wall, a paint-stained wooden table in the middle of the room with an open laptop on it, one tall old window with a dusty pane looking out over the narrow lane, a worn wooden floor, an old wooden door",
}
MOOD = {
    "bank_office": "present day, 9 am, cold bright morning daylight through the tall windows, glass and steel reflections, the screen's pale blue glow on his face, a sudden chill of dread",
    "bank_it": "present day, mid-morning, dim room lit mainly by the cold blue-and-teal monitor glow, thin stripes of daylight through the blinds, tense and suspicious",
    "lounge": "present day, late morning shut out by heavy curtains, low warm amber lamplight pooling on the table, deep charcoal shadows in the corners, thick tense silence, conspiratorial noir",
    "gallery": "memory, soft hazy desaturated light with a dreamlike vignette, the warm gallery lights blooming, the red sun painting glowing faintly behind them",
    "hacker_room": "present day, late morning, blinds drawn, thin blades of daylight across the room, the cold blue monitor glow on his face, quiet and dangerous",
    "studio": "present day, afternoon, grey overcast daylight falling through the dusty window, long soft shadows, dust in the air, hushed and heavy with emotion",
}

COUPLE_GAP = "a clear arm's-length gap between them, they do not touch"

BEATS = [
    dict(to=4, reason="episode opening, scene and character: Fareed in his bank office at 9 am opens the secret email", chars=["fareed"], loc="bank_office",
         visual="Fareed sitting at his large dark desk, leaning towards the open laptop, the screen turned away from the viewer so only its pale blue glow lights his face; the colour has drained from his face, eyes wide and fixed, one hand frozen above the keyboard, the city and sea bright behind him through the windows",
         camera="medium shot from slightly to the side of the desk, his face in the upper third, the polished desk top as a calm lower third", amb="office_day",
         sens="other", safe="the payment receipts and the threat line are never shown; the screen faces away, only its glow on his face (no readable text)"),
    dict(to=7, reason="character and location change: his most trusted IT man traces where the email came from", chars=["fareed"], loc="bank_it",
         visual="a young bank IT man in a white short-sleeved shirt and lanyard sitting at three monitors full of abstract glowing network maps and connecting lines, pointing at one bright red node on the map; Fareed standing behind his chair, bent forward with one hand on the chair back, staring at the screens, his face darkening with fury",
         camera="medium wide over-the-shoulder shot from behind the monitors' side, faces in the upper half, the desk edge as the lower third", amb="office_day"),
    dict(to=10, reason="action change: Fareed, grinding his teeth, phones Speaker Sameer", chars=["fareed"], loc="bank_office",
         visual="Fareed standing at the floor-to-ceiling window of his office with his back half to the city, a phone pressed to his ear, jaw clenched and teeth gritted, his free hand balled into a fist against the glass, eyes narrowed with rage and suspicion",
         camera="medium close-up, eye level, his face in the upper third, the window frame and city below as a calm lower third", amb="office_day"),
    dict(to=12, reason="time jump and location change: two hours later, the three men meet in a secret private lounge in Hulhumalé", chars=["asim", "fareed", "sameer"], loc="lounge",
         visual="the three men in the dim private lounge: Sameer sitting back in a leather armchair at the left, calm, his hands folded over his stomach; Asim sitting forward in a second armchair at the right, glowering, his jaw set with anger; Fareed standing between and behind them, arms crossed, tense; heavy silence; the low table between them bare",
         camera="wide shot, eye level, the three faces in the upper half, the bare polished table as the calm lower third", amb="lounge_private", transition="black",
         sens="other", safe="the narration says Sameer is smoking: shown seated with his hands folded instead; nothing in his hands, no smoke"),
    dict(to=14, reason="action change: Asim slams his palm on the table and denies sending the email", chars=["asim", "fareed"], loc="lounge",
         visual="Asim leaning forward out of his armchair, his palm pressed flat on the polished table top, his face hard and furious as he shouts up at Fareed; Fareed standing on the other side of the table, glaring down at him",
         camera="medium two-shot from a low angle across the table, faces in the upper half, the table top with Asim's flat hand as the lower third", amb="lounge_private",
         sens="violence", safe="anger only as a palm pressed flat on the table and a raised voice; no strike"),
    dict(to=16, reason="action change: Fareed throws his phone down in front of Asim and accuses him", chars=["fareed", "asim"], loc="lounge",
         visual="Fareed leaning over the low table, having just tossed his phone onto it in front of Asim, the phone lying face-up with a dark blank screen, Fareed's finger jabbing towards it, his face twisted with accusation; Asim seated, staring at the phone, then up at Fareed, stunned and angry",
         camera="medium shot from the side of the table, faces in the upper half, the phone on the table top in the lower third", amb="lounge_private"),
    dict(to=19, reason="focus moves to Sameer: he shouts 'Stop!' and calmly explains the intruder used Asim's IP", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer in the foreground in his armchair, calm and certain, his round glasses catching the amber lamplight, slowly turning a silver pen between his fingers while he looks from one man to the other; Asim and Fareed in soft focus behind the table, listening, their anger cooling into doubt",
         camera="medium close-up on Sameer, eye level, his face in the upper third, the others blurred behind, the table edge as the lower third", amb="lounge_private",
         sens="other", safe="the narration has him flick cigarette ash: shown turning a silver pen between his fingers instead; no smoke"),
    dict(to=21, reason="return to the wide three-shot: Asim and Fareed look at each other; Asim, now afraid, asks who it was", chars=["asim", "fareed", "sameer"], loc="lounge", reuse="beat_004",
         visual="reuse of beat_004: the three men in the dim private lounge, Asim and Fareed exchanging uneasy looks while Sameer sits calm",
         camera="wide shot, eye level", amb="lounge_private",
         sens="other", safe="Sameer seated with hands folded; no smoking shown"),
    dict(to=26, reason="action change: Sameer opens a file on his phone and reveals the journalist Iyaan", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer leaning forward, holding up his phone towards the other two, its screen a soft blue glow with only blurred abstract shapes; Asim and Fareed leaning in from either side of the table, staring at it, faces lit by the cold blue light, tension rising",
         camera="medium shot, slightly high angle over the table, the three faces in the upper half, the table top as the lower third", amb="lounge_private",
         sens="other", safe="the phone file and the cyber-crime logs are never readable: a blurred blue glow only"),
    dict(to=27, reason="strong emotional turning point: Asim learns Iyaan is Ahmed Zahir's only son", chars=["asim"], loc="lounge",
         visual="close-up of Asim frozen in his armchair, his face draining of colour, eyes wide with shock and dawning fear, mouth slightly open, a bead of sweat on his temple, as if the floor has dropped away beneath him",
         camera="close-up, slightly low angle, his face in the upper half, his white shirt and the dark armchair below", amb="lounge_private"),
    dict(to=29, reason="memory: Asim remembers patting the young man's shoulder at Raaya's gallery and the deep look in his eyes", chars=["asim", "iyaan"], loc="gallery",
         visual="in the art gallery, Asim in his white shirt patting the young man Iyaan on the shoulder in a superior way, smiling proudly; Iyaan, wearing a dark charcoal long-sleeved button-up shirt (NOT the plain black t-shirt of the reference), standing still and looking back at him with a deep, unreadable, intense gaze; the large red-sun painting softly blurred behind them",
         camera="medium two-shot, eye level, faces in the upper half, the polished gallery floor as the lower third, a soft dreamlike vignette", amb="memory", transition="dissolve"),
    dict(to=33, reason="action change, back from the memory: Sameer stands up and declares Iyaan must be eliminated", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer standing up from his armchair, buttoning his suit jacket, his face cold and decisive behind his round glasses as he speaks down to the others; Asim still seated, pale and shaken, gripping the armrests; Fareed standing at the side, nodding grimly; the three men united against a new enemy",
         camera="medium wide shot from a low angle, Sameer's face in the upper third, the bare table as the lower third", amb="lounge_private", transition="dissolve",
         sens="other", safe="the narration has him drop his cigarette: shown buttoning his jacket as he stands; nothing in his hands"),
    dict(to=36, reason="location and character change: Iyaan was listening live through Asim's phone; he puts down the headphones with a dangerous smile", chars=["iyaan"], loc="hacker_room",
         visual="Iyaan sitting at his desk in the dim room, setting a pair of black over-ear headphones down on the desk, a monitor behind him glowing with an abstract green audio waveform; no fear on his face, only a slow, dangerous half-smile and cold, steady eyes looking straight ahead",
         camera="medium close-up, eye level, his face in the upper third, the desk top with the headphones as the calm lower third", amb="hacker_room"),
    dict(to=38, reason="action change: Iyaan, two steps ahead, phones Raaya and asks her to come secretly to the studio", chars=["iyaan"], loc="hacker_room",
         visual="Iyaan standing by the window of his room, two fingers parting the blinds as he looks down at the street, a phone held to his ear, his face serious and focused, thin daylight cutting across his eyes, the glowing monitors and the investigation board with red string behind him",
         camera="medium shot, eye level, his face in the upper third, the dark floor and desk edge as the lower third", amb="hacker_room"),
    dict(to=42, reason="time jump and location change: Raaya secretly arrives at the silent third-floor studio; Iyaan waits at the window", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya stepping in through the old wooden door at the left of the studio, anxious, clutching her handbag strap, looking across the room; Iyaan standing far away at the tall window on the right, his back half turned, looking out; the paint-stained table with the open laptop stands between them in the middle of the room; " + COUPLE_GAP + ", the whole room's width apart",
         camera="wide shot, eye level, faces in the upper half, the worn wooden floor as a calm lower third", amb="room_day", transition="black"),
    dict(to=45, reason="emotional turning point: Iyaan turns, without his usual smile, and confesses 'It was me'; Raaya steps back, eyes wide", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan turned to face Raaya, his face grave and unsmiling, standing still by the window; Raaya taking a step backwards near the table, eyes wide with disbelief, one hand rising to her chest; " + COUPLE_GAP + ", several steps apart",
         camera="medium wide two-shot from the side, eye level, faces in the upper half, the wooden floor as the lower third", amb="room_day"),
    dict(to=48, reason="action change: Iyaan accuses Asim; Raaya cries out that it's a lie and turns to the door; he touches the laptop", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya in the foreground turning away towards the old wooden door, tears on her cheeks, looking back over her shoulder in pain and denial; behind her at the table Iyaan, hard-faced and stern, presses one finger on the open laptop's trackpad, the screen facing away with only its glow visible; " + COUPLE_GAP + ", the table between them",
         camera="medium shot, eye level, Raaya's face in the upper third with Iyaan behind, the floor as the lower third", amb="room_day"),
    dict(to=51, reason="action change: Asim's own voice plays from the laptop; Raaya clamps her hands over her ears", chars=["raaya"], loc="studio",
         visual="the open laptop on the paint-stained table in the foreground, its screen turned away with only a pulsing green audio-waveform glow spilling onto the table; behind it Raaya frozen in the middle of the room, both hands pressed over her ears through her hijab, eyes squeezed shut, her face crumpling as she recognises the voice",
         camera="medium shot from behind the laptop, Raaya's face in the upper third, the table top as the lower third", amb="room_day",
         sens="other", safe="the recorded order is only heard; on screen only an abstract waveform glow, no text"),
    dict(to=52, reason="action change: Raaya sinks to the floor, her world stopped", chars=["raaya"], loc="studio",
         visual="Raaya kneeling and sitting back on her heels on the wooden floor against the bare plaster wall, upright, both hands pressed over her mouth, eyes brimming with tears, staring at nothing, her white dress pooled around her; grey window light falling on her",
         camera="medium shot, slightly high angle, her face in the upper half, the empty floor before her as the lower third", amb="room_day",
         sens="other", safe="'sinks to the floor' shown as kneeling upright against the wall, hands over mouth; not lying down"),
    dict(to=55, reason="character enters the frame: Iyaan kneels before her and tells her his father died in his arms", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan kneeling on one knee on the wooden floor facing Raaya, who sits against the wall; his face full of deep grief and old hatred, eyes glistening, his hands resting on his own knee; Raaya looking up at his face, speechless, tears on her cheeks; " + COUPLE_GAP + ", a respectful space of floor between them",
         camera="medium two-shot from the side, eye level, both faces in the upper half, the bare floor between them as the lower third", amb="room_day",
         sens="intimacy", safe="no touching; a clear arm's-length gap kept between Iyaan and Raaya"),
    dict(to=59, reason="action change: Iyaan asks for her help and holds out a small black drive (the narration's taking her hands is replaced)", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan, still kneeling at a respectful distance, holding out a small black metal drive on his open palm towards Raaya, his expression earnest and urgent; Raaya, sitting against the wall, sobbing softly, looking down at the small drive with hesitation; " + COUPLE_GAP + ", only the outstretched drive in the space between them",
         camera="medium two-shot from a low side angle, faces in the upper half, the floor as the lower third", amb="room_day",
         sens="intimacy", safe="the narration has him take her hands: shown instead offering a small black drive on his open palm, no touching, arm's-length gap"),
    dict(to=61, reason="emotional turning point: after a long silence Raaya decides to help and wipes her tears", chars=["raaya"], loc="studio",
         visual="close-up of Raaya wiping a tear from her cheek with the back of her hand, her chin lifting, her wet eyes now firm and resolved, the small black drive held tightly in her other hand against her chest; soft grey window light on her face",
         camera="close-up, eye level, her face in the upper half, her hand with the drive and her white dress below", amb="room_day"),
    dict(to=63, reason="closing: Iyaan's inner vow to Asim", chars=["iyaan"], loc="studio",
         visual="Iyaan standing at the tall dusty window of the studio in profile, looking out over the narrow lane and the grey rooftops of Malé, his face cold, calm and determined, a faint hard light in his eyes; blank canvases in soft shadow behind him",
         camera="medium close-up in profile, his face in the upper third, the window sill and the dark room below as a calm lower third", amb="room_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The secret email Iyaan had sent reached bank MD Fareed at around nine in the morning. He was sitting at his office desk.",
   [("computer_beep", "ލިބުނީ", -20)])
sh(2, "As he opened the email, the colour of Fareed's face changed. In it were",
   [("heartbeat", "ބަދަލުވިއެވެ", -20)])
sh(3, "the secret transaction receipts of the money he had sent in 2011 to the killers' account to have MP Ahmed Zahir murdered.")
sh(4, "At the very bottom of the email was written: \"These secrets cannot stay hidden forever. Get ready to pay the price.\"",
   hum=True)
sh(5, "Fareed immediately had the most trusted man in his IT team trace where the email had come from.",
   [("keyboard_typing", "ޓްރެކް", -20)])
sh(6, "With the answer came the most extreme rage. The email had been sent straight from Home Minister Asim's house.",
   [("computer_beep", "ޖަވާބާއެކު", -20)])
sh(7, "In a split second countless questions rose and fell in his mind. \"Asim... what are you trying to blackmail me for?\"")
sh(8, "Fareed said, grinding his teeth. He believed that whoever entered Asim's house last night was no political enemy, but a drama Asim had staged himself to frighten Fareed and extort money from him.",
   [("breath_heavy", "ދަތްކުނޑިވިކާލަމުން", -22)])
sh(9, "Fareed at once picked up his phone and called Sameer, Speaker of Parliament. \"Sameer!",
   [("phone_buzz", "ގުޅިއެވެ", -22)])
sh(10, "We have to meet right now. Some evil political demon has got into Asim's head.")
sh(11, "He's trying to destroy us!\" Two hours later. Inside a secret private lounge in Hulhumalé sat Sameer, Fareed and Asim.")
sh(12, "Silence hung in the room. Sameer sat smoking. Fareed stood. Asim sat seething with anger. \"Fareed,")
sh(13, "what nonsense is this you're talking?\" Asim said, slamming his hand hard on the table. \"Someone broke into my house last night and only just failed to open my safe!",
   [("soft_thud", "ޖަހަމުން", -16)], hum=True)
sh(14, "For all I know every one of my secret files is gone now. Why on earth would I send you an email?\"")
sh(15, "\"Then why does the IP address of the email that reached my office match your house router?\" Fareed threw his phone down in front of Asim.",
   [("soft_thud", "އެއްލިއެވެ", -20)])
sh(16, "\"You're trying to dump all the blame for Zahir's murder on my head so you can save yourself politically!\" \"Stop!\" Sameer shouted.")
sh(17, "His voice carried political experience and certainty. Flicking the ash off his cigarette, he looked at the two men's faces.")
sh(18, "\"You two still don't get it, do you? Asim is no fool; he wouldn't send an email to blackmail Fareed in a way that's so easy to trace.")
sh(19, "And whoever got into that house last night was no ordinary thief. It was someone who got into the system and used that house's IP to send Fareed the mail.\"")
sh(20, "Asim and Fareed looked at each other. They grasped the truth in Sameer's words. \"Then... who is it?\" Asim asked.")
sh(21, "This time there was fear in his voice. \"Who could know that the three of us were involved in Zahir's murder?\"",
   [("heartbeat", "ބިރުގަތުމުގެ", -22)])
sh(22, "Sameer opened a file on his phone. \"Not a single glimpse of the man who got into Asim's house last night was caught on any camera.")
sh(23, "But when the police cyber-crime department checked the network logs this morning, they saw the way the virus was designed.")
sh(24, "That's work only a top digital forensics expert could do. And besides that...\" Sameer paused. \"Besides what?\"")
sh(25, "Fareed asked hurriedly. \"Lately there's a young journalist writing our corruption stories in the papers with very detailed evidence.")
sh(26, "His name is Iyaan,\" Sameer said. \"Do you know what I found out when I checked his background this morning?")
sh(27, "He is the only son of Ahmed Zahir, whom we destroyed fifteen years ago!\" Asim felt as if the ground had been cut away from under his feet.",
   [("heartbeat", "ބިންގަނޑު", -18)], hum=True)
sh(28, "He remembered the young man he had seen yesterday at Raaya's art gallery. The moment Asim had put his hand on his shoulder,")
sh(29, "the deep look he had seen in that young man's eyes. \"Iyaan...\" Asim's voice trembled. \"He's out for revenge.",
   [("breath", "ތުރުތުރު", -22)])
sh(30, "He used Raaya to get inside my house!\" \"Yes,\" said Sameer, throwing his cigarette to the floor as he stood up.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(31, "\"Zahir's son has grown up and is ready to grab us by the throat. He has every piece of evidence in his hands.")
sh(32, "We have no time to fight among ourselves. Iyaan's days have to be ended for good... he has to be eliminated.\"",
   hum=True)
sh(33, "The war between the three friends suddenly turned against Iyaan. They knew the truth now. But every word of it,")
sh(34, "Iyaan had been listening to live, through something he had done to Asim's phone. Iyaan took off his headphones and put them on the desk.",
   [("cloth_rustle", "ބޭއްވިއެވެ", -22)])
sh(35, "There was no fear on his face. Instead there was a dangerous smile. \"You found out my truth far too late,\"",
   hum=True)
sh(36, "Iyaan said softly. \"When you come to destroy me, the way for every one of you to walk into my net is already prepared.\"")
sh(37, "With Sameer's and Fareed's warnings, Asim began the work of eliminating Iyaan. But Iyaan was two steps ahead of them.")
sh(38, "The very first thing he did was call Raaya. His voice was serious. Iyaan asked her to come secretly to the art studio, unseen by her father's security and the police.",
   [("phone_buzz", "ގުޅުމެވެ", -22)])
sh(39, "Because of the deep trust she had in Iyaan, Raaya agreed to go there in secret from her father.")
sh(40, "When Raaya entered that studio on the third floor of an old building in a quiet Malé lane, the whole place was silent.",
   [("door_open", "ވަތްއިރު", -20)])
sh(41, "On a table in the middle of the room a laptop stood open. Iyaan stood by the window, looking out. \"Iyaan... why did you tell me to come here?")
sh(42, "Bappa is furious right now. There's nothing he won't do to find whoever breached the house's security,\" Raaya said anxiously.")
sh(43, "Iyaan slowly turned around. The smile always on his face was not there today. \"Raaya... do you know who got into your house last night?\" \"No... who?\"")
sh(44, "Raaya asked. \"It was me,\" Iyaan said very carefully. Raaya's feet stepped backwards. Her eyes grew wide. \"What?",
   [("gasp", "ބޮޑުވިއެވެ", -20)], hum=True)
sh(45, "Iyaan... what kind of joke is this? Why?\" \"This is no joke, Raaya. I went into your house to find the truth about my father's murder.")
sh(46, "Your father, Home Minister Asim, may wear white clothes, but he is a murderer stained with an innocent man's blood,\" Iyaan said, his voice hard and angry.")
sh(47, "\"No! That's a lie! My father would never do such a thing!\" Raaya cried out. Tears streamed from her eyes.",
   [("sob_breath", "ކަރުނަ", -22)])
sh(48, "She turned towards the door to leave. \"Listen to this,\" Iyaan said, tapping the laptop's screen.",
   [("computer_beep", "ފިތާލިއެވެ", -20)])
sh(49, "At once the audio file Iyaan had taken from Asim's own safe echoed through the studio. Asim's heavy,")
sh(50, "merciless voice was heard: \"Zahir has started talking far too much... shut his mouth for good. Make tonight his last night in this world...\"",
   hum=True)
sh(51, "Raaya's hands flew to her ears. She knew her father's voice all too clearly. It was, without any doubt, Asim's own voice.",
   [("gasp", "ޖެހުނެވެ", -22)])
sh(52, "Raaya sank to the floor. It was as if her world had stopped. Having to accept that her loving, caring father was a merciless political killer who had ordered a man's death broke her heart.",
   [("soft_thud", "ތިރިވިއެވެ", -24)], hum=True)
sh(53, "Iyaan went and knelt in front of Raaya. \"That murdered Ahmed Zahir was my father. When I was eight years old my father died in my arms.",
   [("cloth_rustle", "ޖެހިއެވެ", -22)], hum=True)
sh(54, "Merciless men killed my father on your father's order. For the past fifteen years the only purpose I have lived for is finding this truth.\"")
sh(55, "Raaya looked at Iyaan's face. Seeing the deep grief and hatred in his eyes, no word left her lips. \"Iyaan... I...")
sh(56, "what should I do?\" Raaya asked, sobbing. \"Asim plans to eliminate me tonight together with Sameer and Fareed.",
   [("sob_breath", "ގިސްލަމުން", -22)])
sh(57, "They think that if I'm gone, all the evidence will disappear. What I need is your help, Raaya.")
sh(58, "Asim can only be defeated from inside his house,\" Iyaan said, taking both Raaya's hands. \"Before Asim's next big political rally, I need")
sh(59, "the second backup drive that holds his data. Only you can do that.\" For a while Raaya sat in silence.")
sh(60, "Standing up against her father was no easy thing. But for the sake of justice, and for the great sin her father had committed, she decided to help Iyaan.")
sh(61, "\"I'll do it,\" Raaya said, wiping away her tears. \"I'll help expose my father's crimes to the whole nation.\"",
   [("breath", "ފޮހެލަމުން", -24)], hum=True)
sh(62, "Iyaan said to himself: Asim... you took my father from me. Today your own child stands against you.")
sh(63, "Your end will be no less heartbreaking than this. To be continued.", hum=True)
SHOTS = S

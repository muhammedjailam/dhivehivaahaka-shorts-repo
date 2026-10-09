"""Beat/shot plan for Nindheveethimeymathee episode 276 (used by plan_beats.py).
PRESENT (night drive, Saba's hospital bedside, morning terrace) -> SCHOOL flashback (A-level video call with Asil,
young Saba walks into Asil's room). Lail and married Saba never touch; Saba's injuries are never shown."""

ROOM = "a private patient room in a modern hospital in Male', Maldives at night: a hospital cot with a raised back and crisp white sheets, a metal IV stand with a drip bag, two padded visitor chairs, a small side cabinet, a wide window with distant city lights, a dim warm night lamp, pale walls"
LOC = {
    "car": "inside a dark car driving through the streets of Male', Maldives at night, a smartphone in a dashboard holder, blurred amber street lights and shop lights streaking past the windscreen",
    "corridor": "a quiet hospital corridor in Male', Maldives late at night: polished pale floor, closed patient-room doors, soft ceiling lights, a long empty perspective",
    "hosp_room": ROOM,
    "hosp_late": ROOM + ", deep in the night",
    "clock": "a pale hospital-room wall at night with a plain round analog wall clock with no numerals and a thin second hand",
    "bangkok": "a large international airport in Bangkok at night seen from the tarmac: a passenger jet parked at a glowing glass terminal gate, wet tarmac reflecting the lights, a distant city glow",
    "studio": "a bright modern TV talk-show studio set in Male' with a red-and-gold backdrop without any letters, a curved presenter sofa, warm studio lights, cameras in soft focus",
    "terrace": "the rooftop terrace of a beachfront penthouse in Hulhumale', Maldives: glass railing, a calm empty terrace pool, potted palms, the lagoon and the waking city beyond",
    "street": "a wide beachfront road in Hulhumale', Maldives seen from a high penthouse terrace: palm-lined pavement, parked cars and a row of parked motorbikes, light morning traffic",
    "lail_room": "teenage Lail's tidy bedroom in a modern Male' apartment years ago: a wooden study desk by a window, an open laptop, sheets of paper and pencils, a bookshelf, a desk lamp",
    "asil_screen": "a laptop screen showing a live video-call picture of a boy's bedroom in a Male' apartment: a neatly made single divan with a plain cover, a wooden dressing table with a mirror, a study desk, a door at the back; the screen has no text, no icons, no interface",
}
MOOD = {
    "car": "night, deep indigo darkness inside the car, cold soft glow of the phone on his face, amber city lights sliding past, dry humid night, weary irritation",
    "corridor": "late night, dry night, cool blue-white hospital light, hushed and anxious",
    "hosp_room": "night, dry night, a dim warm amber night lamp against deep blue shadows, city lights in the window, tearful reunion, aching tenderness",
    "hosp_late": "the small hours of the night, dry night, a single dim warm lamp, deep sapphire shadows, quiet sorrow and tension",
    "clock": "the small hours of the night, dim warm lamp light, deep blue shadows, time slipping away",
    "bangkok": "night, wet tarmac after rain, cold blue and sodium-orange airport lights, distant and indifferent",
    "studio": "soft hazy dreamlike memory glow, bright warm studio lights, cheerful on-air sparkle",
    "terrace": "early morning after a sleepless night, clear bright tropical sky, soft golden low sunlight, a light sea breeze, exhausted and reflective",
    "street": "early morning, clear bright tropical sky, soft golden sunlight and long shadows, lively youthful energy",
    "lail_room": "soft hazy dreamlike memory glow, late-afternoon golden sunlight through the window, carefree school days",
    "asil_screen": "soft hazy dreamlike memory glow, warm late-afternoon light in the room on the screen, the soft glow of the laptop, curious intrigue",
}

SABA_HOSP = ("Saba propped up sitting against raised pillows on the hospital cot, wearing a loose long-sleeved pale-blue hospital "
             "gown and a white hospital headscarf fully covering her hair and neck, a light blanket over her legs, her face clear "
             "and unmarked")
NURSE = "a young nurse in light-blue scrubs and a white hijab fully covering her hair and neck"
SABA_Y = "young Saba in a loose long-sleeved ankle-length powder-blue dress and a white hijab fully covering her hair and neck"

BEATS = [
    # ---------- PRESENT: night drive ----------
    dict(to=2, reason="episode opening: Lail driving at night, rejecting Sara on the phone", chars=["lail"], loc="car",
         visual="Lail at the wheel of a dark car at night, wearing a dark jacket over his slate-blue henley, jaw tight and eyes hard with irritation, glancing at the phone in the dashboard holder whose screen is only a soft glow; blurred amber city lights through the windscreen",
         camera="medium close-up from the passenger seat, his face in the upper third, the dark dashboard as the calm lower third", amb="car_night"),
    dict(to=6, reason="action change: Sara's audio message plays and he answers with a voice note", chars=["lail"], loc="car",
         visual="close-up of the smartphone in the dashboard holder showing only a soft glowing abstract audio waveform, no text; behind it, in soft focus, Lail in his dark jacket slowly shaking his head, weary and unmoved, his face lit by the cold phone glow and passing street lights",
         camera="close-up on the phone with Lail's face behind it in the upper half, the dark dashboard as the lower third", amb="car_night",
         sens="intimacy", safe="Sara is never shown; her love message is only a glowing waveform on a phone"),
    # ---------- hospital ----------
    dict(to=8, reason="scene change: Lail arrives at the hospital and knocks on Saba's door", chars=["lail"], loc="corridor",
         visual="Lail in his dark jacket over the slate-blue henley standing before a closed patient-room door in a hushed hospital corridor, one hand raised to knock softly, his face tense and hesitant, nine years of distance in his eyes",
         camera="medium shot from the side, his face in the upper third, the polished corridor floor as the lower third", amb="hospital_corridor"),
    dict(to=10, reason="characters change: inside the room, Saba sees Lail and her eyes fill with tears; Sadhee rises", chars=["saba", "sadhee", "lail"], loc="hosp_room",
         visual=f"{SABA_HOSP}, looking towards the doorway with tears welling in her large eyes and a trembling attempt at a smile; Sadhee rising from a visitor chair beside the cot, gesturing to offer the seat; Lail standing just inside the doorway in his dark jacket, stricken; the IV stand in the background, no needle visible",
         camera="medium wide, eye level, faces in the upper two-thirds, the white blanket and floor as a calm lower third", amb="hospital_night",
         sens="other", safe="Saba's injuries are never shown: calm clear face, white hospital headscarf, IV stand only in the background"),
    dict(to=14, reason="action change: Lail sits a step away; the three talk and Sadhee stays", chars=["lail", "saba", "sadhee"], loc="hosp_room",
         visual=f"Lail sitting on a visitor chair a full step away from the hospital cot, hands clasped on his own knees, leaning slightly forward, tears in his eyes; {SABA_HOSP}, sobbing softly with her head turned towards him; Sadhee sitting on a chair off to one side by the window, watching them; a clear gap of space between Lail and the cot",
         camera="medium wide, eye level, faces in the upper two-thirds, the floor as a calm lower third", amb="hospital_night",
         sens="intimacy", safe="narration says he holds her hand: shown instead sitting a step away with his hands clasped on his own knees (she is married; no touching)"),
    dict(to=15, reason="detail: the clock's second hand — the night slipping away", loc="clock",
         visual="a plain round analog wall clock with no numerals and a thin second hand on the pale wall of the dim hospital room, lit by a soft warm lamp; below it, out of focus, the silhouette of the IV stand; no people",
         camera="close-up, the clock in the upper half, the soft shadowed wall as the lower third", amb="hospital_night", transition="black"),
    dict(to=18, reason="time jump: deep in the night, Saba and Sadhee asleep, Lail keeps watch", chars=["lail", "saba", "sadhee"], loc="hosp_late",
         visual="deep night in the dim room: Saba asleep propped upright against the raised pillows, eyes closed, white hospital headscarf and pale-blue gown, face peaceful and unmarked; Sadhee dozing in a chair in the corner with her head tilted; Lail sitting on a chair a step away from the cot, hands clasped on his knees, gazing at Saba's sleeping face without blinking",
         camera="wide shot, eye level, faces in the upper two-thirds, the shadowed floor as the lower third", amb="hospital_night",
         sens="other", safe="the 'marks from falling' on her face are not shown; her face stays clear and calm"),
    dict(to=21, reason="emotional turning point: Lail's tears and his fear that she tried to harm herself", chars=["lail"], loc="hosp_late",
         visual="close-up of Lail alone, sitting upright on a visitor chair in the dim warm lamp light, his face in three-quarter view looking off to the side of the frame, eyes red and filled with tears, brows knotted with disbelief and guilt, hands clasped under his chin; behind him only the dark window with blurred city lights; no other person in the frame",
         camera="close-up, Lail's face in the upper half, soft dark shadow below", amb="hospital_night", hum=True,
         sens="other", safe="the possible self-harm is only Lail's worried face; nothing of it is shown"),
    dict(to=24, reason="action change: Sadhee's phone rings; she wakes and warns Lail that Zuhuruf may come", chars=["sadhee", "lail"], loc="hosp_late",
         visual="Sadhee awake in her chair, holding up her ringing phone towards Lail, its screen only a soft glow with no text, her round face alarmed and urgent; Lail turning towards her from his chair, tense; the sleeping Saba a soft shape in the background",
         camera="medium two-shot, eye level, faces in the upper two-thirds, the floor as the lower third", amb="hospital_night"),
    dict(to=27, reason="action change: Sadhee answers Zuhuruf's call by the window while Lail looks at sleeping Saba", chars=["sadhee", "lail", "saba"], loc="hosp_late",
         visual="Sadhee standing by the dark window with the phone at her ear, her face hard and reproachful, city lights behind her; Lail sitting on a visitor chair an arm's length back from the cot, looking towards Saba; Saba asleep SITTING UPRIGHT on the cot whose back is raised high, her back resting on a tall stack of pillows, head tilted gently, eyes closed, in her white hospital headscarf; she is sitting, not lying flat",
         camera="medium wide, eye level, faces in the upper two-thirds, the floor as the lower third", amb="hospital_night"),
    dict(to=30, reason="location cutaway: Zuhuruf has just landed in Bangkok (he is never shown)", loc="bangkok",
         visual="a passenger jet parked at a glowing glass terminal gate of a large airport at night, wet tarmac reflecting blue and orange lights, a distant city glow on low clouds; no people, no airline logos, no signs",
         camera="wide shot, the plane and terminal in the upper two-thirds, the wet tarmac as a calm lower third", amb="hospital_night",
         sens="other", safe="Zuhuruf is only a voice on the phone; never shown"),
    dict(to=33, reuse="beat_010", reason="return to Sadhee on the phone: Zuhuruf hangs up", loc="hosp_late",
         visual="(reuse)", amb="hospital_night"),
    dict(to=37, reason="action change: Sadhee turns on Lail — 'all of this is because of you'", chars=["sadhee", "lail", "saba"], loc="hosp_late",
         visual="Sadhee standing with her arms folded, frowning down at Lail with bitter accusing eyes; Lail sitting on his chair with his head lowered, silent and guilty, hands clasped; Saba asleep propped up in soft focus in the background",
         camera="medium two-shot, slightly low angle on Sadhee, faces in the upper two-thirds, the floor as the lower third", amb="hospital_night"),
    dict(to=42, reason="emotional turning point: Sadhee's furious outburst about Saba's husband", chars=["sadhee", "lail"], loc="hosp_late",
         visual="medium close-up of Sadhee speaking furiously in a low voice, jaw clenched, eyes blazing with anger and hurt, one hand raised and trembling in the air; over-the-shoulder of Lail in the soft-focus foreground, listening in astonishment",
         camera="over-the-shoulder medium close-up, Sadhee's face in the upper half, Lail's shoulder as a dark shape below", amb="hospital_night", hum=True,
         sens="violence", safe="the husband's abuse is only described in dialogue; he is never shown, no violence on screen"),
    dict(to=45, reason="imagined scene: Saba as the cheerful presenter Lail has watched on every show", chars=["saba"], loc="studio",
         visual="Saba in her dusty-lavender floral dress and pale-lavender hijab sitting on a curved presenter sofa on a bright red-and-gold talk-show set without any letters, laughing warmly towards the camera, holding a few blank cue cards, radiant and full of life",
         camera="medium shot, eye level, her face in the upper third, the glossy studio floor as the lower third", amb="tv_studio",
         transition="dissolve"),
    dict(to=46, reuse="beat_007", reason="return to the hospital room: Lail silent beside Saba as Sadhee steps out", loc="hosp_late",
         visual="(reuse)", amb="hospital_night", transition="dissolve"),
    dict(to=49, reason="character enters: a nurse checks the IV and gives an injection", chars=["saba", "lail"], loc="hosp_late",
         visual=f"{NURSE} standing beside the IV stand adjusting the drip bag, a small metal tray in her other hand; Saba propped up against the pillows in her white hospital headscarf, eyes half open, wincing slightly; Lail on his chair a step away from the cot, leaning forward with concern, hands on his own knees",
         camera="medium wide, eye level, faces in the upper two-thirds, the white blanket and floor as the lower third", amb="hospital_night",
         sens="other", safe="the injection is shown only as the nurse adjusting the drip bag; no needle visible"),
    dict(to=52, reason="action change: the nurse asks Lail who he is; Sadhee comes back and answers", chars=["lail", "sadhee"], loc="hosp_late",
         visual=f"Lail, a visitor fully dressed in his slate-blue henley and dark trousers, sitting on a padded wooden visitor chair by the dark window, looking up lost for words; {NURSE} standing in front of him turning towards him with a curious little smile, holding a small metal tray; Sadhee stepping back into the room from a side door at the back, answering with a firm face; the hospital cot is out of frame",
         camera="medium wide, eye level, faces in the upper two-thirds, the floor as the lower third", amb="hospital_night"),
    dict(to=56, reuse="beat_007", reason="return to the night watch: Sadhee grumbles and dozes off, Lail keeps looking at Saba", loc="hosp_late",
         visual="(reuse)", amb="hospital_night"),
    # ---------- morning terrace ----------
    dict(to=59, reason="time jump and scene change: next morning on Lail's penthouse terrace with coffee", chars=["lail"], loc="terrace",
         visual="Lail standing at the glass railing of his beachfront penthouse terrace in the early morning, holding a steaming cup of coffee, still in his slate-blue henley, eyes heavy with sleeplessness, gazing down towards the street; a calm empty terrace pool behind him and the shining lagoon beyond",
         camera="medium shot from the side, his face in the upper third, the terrace floor and railing as the lower third", amb="rooftop_day",
         transition="black"),
    dict(to=63, reason="point of view: the group of young people and their motorbikes on the road below", loc="street",
         visual="high-angle view down onto a palm-lined beachfront road in the morning: a laughing group of young men and young women (the women in hijabs and loose long clothes) loading travel bags into the open boot of a parked white car, and pairs of young riders on motorbikes pulling away fast down the road; small figures, no readable signs or number plates",
         camera="high-angle wide shot from the terrace, the road and people in the upper two-thirds, the sunlit pavement as the lower third", amb="road_busy"),
    dict(to=64, reuse="beat_020", reason="return to Lail on the terrace as the scene carries him into the past", loc="terrace",
         visual="(reuse)", amb="rooftop_day"),
    # ---------- SCHOOL flashback ----------
    dict(to=69, reason="flashback: A-level year, Lail on a video call with Asil, solving a maths question", chars=["lail_young", "asil_young"], loc="lail_room",
         visual="teenage Lail (about 17, light-grey t-shirt) at his study desk writing an answer on paper with a pencil and smiling with satisfaction; the open laptop in front of him shows a live video picture of teenage Asil (about 17, maroon t-shirt) bent over his own papers with a serious frown; the laptop screen shows only the picture, no text, no icons; papers show only soft illegible scribble lines",
         camera="medium shot from the side of the desk, both faces in the upper two-thirds, the desk top as the lower third", amb="memory",
         transition="dissolve"),
    dict(to=71, reason="action change: Asil gets up and leaves his room; Lail keeps writing", chars=["asil_young", "lail_young"], loc="asil_screen",
         visual="over-the-shoulder view past teenage Lail's shoulder onto the laptop screen, which fills most of the frame: in the room on the screen teenage Asil in his maroon t-shirt is getting up from his desk chair and walking towards the door at the back; in the foreground Lail's hand writes on paper with a pencil",
         camera="over-the-shoulder close shot, the screen in the upper two-thirds, the desk and papers as the lower third", amb="memory"),
    dict(to=75, reason="character enters: a girl walks into Asil's room on the screen, seen from behind", chars=["saba_young"], loc="asil_screen",
         visual=f"on the laptop screen: {SABA_Y}, seen from behind, standing by the wooden dressing table with a mirror after setting bundles of papers on the neatly made divan; only a sliver of her face shows in the mirror; she lifts a phone to her ear; at the bottom edge of the frame the dark shape of the laptop's edge and the desk",
         camera="close shot of the laptop screen, the girl in the upper two-thirds, the desk edge as the lower third", amb="memory",
         sens="clothing", safe="narration says she wears very short shorts: shown in a loose ankle-length dress and white hijab"),
    dict(to=79, reason="reveal of a face: she turns and sits on the divan — Lail leans back, startled", chars=["saba_young", "lail_young"], loc="asil_screen",
         visual=f"teenage Lail in his light-grey t-shirt leaning back in his chair in surprise, seen in profile at the left of the frame, his face lit by the laptop glow; on the laptop screen at the right {SABA_Y} sitting in the middle of the neatly made divan, phone at her ear, a mischievous playful smile",
         camera="medium shot from the side, Lail's face and the screen in the upper two-thirds, the desk as the lower third", amb="memory", hum=True),
    dict(to=82, reason="focus change: Lail's growing fascination as she chatters in English-sprinkled Dhivehi", chars=["lail_young"], loc="lail_room",
         visual="close-up of teenage Lail's face lit by the soft glow of the laptop, leaning forward with his chin on his hand, eyes wide with amused curiosity and the beginning of a smile, the pencil forgotten in his fingers",
         camera="close-up, his face in the upper half, the desk and papers in soft shadow below", amb="memory"),
    dict(to=85, reason="action change: on the screen she turns serious, checks her watch — 'meet me around 8'", chars=["saba_young"], loc="asil_screen",
         visual=f"the whole frame is filled by an open laptop screen on a desk; INSIDE the video picture on the screen, in Asil's bedroom: {SABA_Y} sitting on the neatly made divan with the phone at her ear, her face suddenly thoughtful and serious, glancing down at a plain wristwatch with no numbers on her wrist; nobody sits in front of the laptop; the thin laptop frame and keyboard edge visible at the bottom",
         camera="close shot of the screen, her face in the upper half, the divan in soft focus below", amb="memory"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Episode 3. Who is that? \"How many times do I have to tell you that I don't love Sara? My heart longs for someone else. Don't make me repeat this any more.\"")
sh(2, "Lail hung up without waiting for anything she had to say. An audio message arrived on Lail's phone. Lail listened to the message.",
   [("phone_buzz", "އައެވެ", -20)])
sh(3, "\"No matter how much time passes, this love will never be wiped from my heart. Even if Lail forgets me, I still love Lail.\"")
sh(4, "\"This body may be handed over to someone, but no one else will ever be able to touch this heart.\"")
sh(5, "Having listened to the audio message, Lail shook his head. \"Sorry Sara, I never had the slightest interest in you, not then and not now.\"",
   [("sigh", "ހަރަކާތް", -22)])
sh(6, "\"Goodbye.\" Lail sent a voice message, and kept driving towards the hospital. Once again a message came from that number.",
   [("phone_buzz", "ނަމްބަރުން", -20)])
sh(7, "This time Lail had no wish to listen to it. After parking the car, Lail went into the hospital. He looked for the room number Sadhee had sent.",
   [("car_door", "ޕާކުކުރުމަށްފަހު", -20)])
sh(8, "When he found the room, he knocked softly on the door. When Sadhee let him in, Lail stepped inside. Saba had an IV drip attached to one hand.",
   [("knock", "ޓަކިޖަހައިލިއެވެ", -18), ("door_open", "އެތެރެއަށް", -22)])
sh(9, "Saba looked at Lail as he came in through the door. Seeing Lail, tears welled up in Saba's eyes.", hum=True)
sh(10, "As Lail came in, Sadhee rose from her chair and offered Lail the seat. Saba tried to smile. But she began to sob. \"Shh.\"",
   [("sob_breath", "ގިސްލެވެން", -22)])
sh(11, "Lail suddenly found himself drawing close to Saba. Sitting down on the chair, he gently took hold of Saba's hand with the IV. \"I'll wait outside.\"")
sh(12, "Sadhee said. \"No,\" Lail and Saba said at the same time. \"Nine years... there must be so much to talk about,\" Sadhee said.")
sh(13, "\"We won't have that much to talk about. Sadhee, stay here,\" Lail said.")
sh(14, "Sadhee didn't leave; she sat down on a chair off to one side. Again Saba began to sob. This time tears welled up in Lail's eyes too.",
   [("sob_breath", "ގިސްލެވެން", -22)], hum=True)
sh(15, "Seeing Saba cry in front of him was more than he could bear. The second hand of the clock carried on with its duty at its fastest pace.",
   [("clock_tick", "ސިކުންތު", -20)])
sh(16, "As the hours of the night passed one after another, Saba lay asleep. Sadhee too dozed off in her chair with her eyes closed.")
sh(17, "Lail sat there tirelessly, gently stroking Saba's hand. Without blinking, Lail kept looking at Saba's face.")
sh(18, "When Lail last saw it, that face was clear and without a single blemish. But now that face bore the marks of falling here and there.")
sh(19, "Lail's eyes kept filling with tears. He could not believe that Saba would try to harm her own life. Could that be?", hum=True)
sh(20, "Would she do something like that? That question kept troubling Lail's mind. Lail wanted to find the answer.")
sh(21, "But right now Lail didn't want to trouble Saba with questions. What Saba needed now was a restful sleep and gentle care.")
sh(22, "And a heart calmed by happy words. Lail's attention went to Sadhee's phone as it rang. Sadhee too opened her eyes and looked at the phone.",
   [("phone_buzz", "ރިންގުންނެވެ", -18)])
sh(23, "Worry showed on her face. Flustered, she looked at Lail. \"Lail, I think you'd better leave first. Looks like Zuhuruf is coming, he's the one calling.\"")
sh(24, "Showing him the phone, Sadhee said to Lail, \"I swear, this is big trouble. If he sees a face he doesn't know, he'll drive her mad with questions. If he gets even a little suspicious, it's over for Saba.\"")
sh(25, "Sadhee said to Lail before picking up. At that, Lail looked at Saba. Saba was asleep. Sadhee answered the phone. \"What is it, Zuhuruf?\"")
sh(26, "Sadhee began. \"How's Saba now? I only just saw the messages.\" Zuhuruf's voice came over the phone. \"Where are you?\"")
sh(27, "\"When something this serious happened?\" Sadhee asked reproachfully. \"I'm in Bangkok... I've only just landed in Bangkok,\" Zuhuruf said.",
   [("plane_pass", "ލޭންޑު", -22)])
sh(28, "\"Weren't you at home when this happened, Zuhuruf?\" Sadhee asked. \"I went to the airport before sunset,")
sh(29, "I came this way via Lanka, that's why my phone was off. I had no idea anything had happened. When I left, Saba was at the office,")
sh(30, "I just texted her and took off,\" Zuhuruf said. \"Is that so?\" Sadhee said in an offhand tone. \"Where's Saba now?\"")
sh(31, "Zuhuruf asked. \"Asleep. Her life was only just saved. You two still haven't stopped quarrelling, have you? Is that why Saba...\"")
sh(32, "Sadhee pulled a face. She didn't finish her sentence. \"Hold on, tell Saba to call me when she wakes up. I only got a ticket for tomorrow afternoon.")
sh(33, "Hold on.\" Zuhuruf hung up without listening to what Sadhee was saying. \"Is he coming?\" Lail asked as Sadhee put the phone down.")
sh(34, "\"No, luckily. He's in Bangkok, says he only got a ticket for tomorrow afternoon. Someone who really wanted to come would come right away,")
sh(35, "however expensive the ticket.\" Sadhee said, knitting her brows in disgust. After a short silence, Sadhee looked at Lail.")
sh(36, "\"All of this has happened because of you, Lail,\" Sadhee said to Lail resentfully. Lail chose to stay silent.")
sh(37, "Lail too accepted that what Sadhee said was not entirely untrue. The responsibility for the state Saba was in was Lail's to bear.", hum=True)
sh(38, "\"Why did you leave Saba all alone among these beasts?... Think about it: since you left, there's no one here to say a kind word to her. She's even drifted apart from her mother...")
sh(39, "And for a husband she got a real Dracula. All he does is suck Saba's blood. Even when Saba hands him every bit of money she earns,")
sh(40, "it's still not enough. Now he's hounding her because she won't transfer her house into his name.")
sh(41, "If that little place goes into his name, this poor girl is finished. He'd even sell Saba for his own wants. That's the kind of beast he is.\"")
sh(42, "Sadhee said angrily, grinding her teeth. As Sadhee talked, Lail kept staring at her face in astonishment.")
sh(43, "As if he wanted to know how much of what Sadhee said was true. When Saba sat presenting her programmes, nothing of the sort ever showed on her face.")
sh(44, "With her cheerfulness and fun chatter she filled the viewers' hearts with joy. Lail never missed a single one of Saba's programmes.")
sh(45, "If he couldn't watch a programme live, he watched it later. Having poured out everything in her heart, Sadhee calmed down.")
sh(46, "Lail said not a word to anything Sadhee had said. He sat on, stroking Saba's hand. Sadhee got up from her chair and went to the restroom.")
sh(47, "Just then a young nurse came in. She checked the IV, which was running out. Setting the tray in her hands down beside the bed, she took an injection from it and gave it into Saba's IV hand.",
   [("door_open", "އެތެރެއަށް", -22)])
sh(48, "Saba flinched her hand and let out a \"Hmm.\" The injection seemed to have hurt her hand a little.")
sh(49, "Lail gently stroked Saba's hand. \"Who are you to Saba?\" the nurse asked.")
sh(50, "With no answer to give, Lail could only lift his head and look at the nurse. At that moment Sadhee came out of the restroom. \"He's one of our own.\"",
   [("door_open", "ނިކުތެވެ", -22)])
sh(51, "Sadhee said, having heard the nurse's question. \"Really? I thought he was Saba's husband.\"")
sh(52, "the nurse said with a smile on her lips. And she took the tray and went out. \"There's nothing that isn't their business,",
   [("door_close", "ނިކުތެވެ", -22)])
sh(53, "it seems they keep every patient's personal affairs on file just like their records. So annoying.\"")
sh(54, "Sadhee said, sitting down on the chair. \"They'll interrogate you hard like the police: who is that? What did he come for?")
sh(55, "What's between him and her? All they want is something to gossip about.\" Even as her eyes were closing, Sadhee kept grumbling.")
sh(56, "Lail ignored what Sadhee was saying and kept looking at Saba. Holding a steaming cup of coffee, Lail stepped out onto the penthouse terrace.")
sh(57, "He hadn't eaten anything since yesterday; he had run the whole day on coffee. After staying awake all night beside Saba, he came home at dawn, before other people arrived there.")
sh(58, "Even now, the weapon Lail used to drive off the sleep weighing on his eyes was a hot cup of coffee. The question the nurse asked late last night was still circling in Lail's mind.")
sh(59, "Who was he to Saba? He found himself asking that very question now. Taking a sip from the cup, he turned his gaze to the road below.",
   [("cup_clatter", "ބޯލަމުން", -24)])
sh(60, "A group of young men and women were loading bags into a car parked to one side.")
sh(61, "Mingled with the noise of the vehicles speeding along the road, the sound of their laughter echoed all around.",
   [("car_pass", "ވެހިކަލުތަކުގެ", -20)])
sh(62, "Joking and teasing each other, about four of them got into the car. The rest split up among the parked motorbikes.",
   [("car_door", "ކާރަށް", -20)])
sh(63, "Paired up evenly, the motorbikes roared off at top speed. It looked as if the youngsters had started a race.",
   [("motorbike_pass", "ބޫންކަނޑައިފައި", -16)])
sh(64, "Though Lail stood looking at the road, the scene he was watching carried him back into his past without his realising it.")
sh(65, "It was the first year of A-levels. He was quickly writing the answer to a question that had been set.",
   [("pen_scribble", "ލިޔަމުން", -22)])
sh(66, "And when he finished, a happy smile spread across his lips. \"Asil, what's the answer?\"")
sh(67, "Lail asked Asil, who was showing on the screen of the laptop in front of him. Asil was writing on paper at the time.")
sh(68, "Hearing Lail's voice, Asil raised his head and looked up. \"I still don't get this at all.\" His face looked serious.")
sh(69, "\"Okay, I'll explain it once more,\" Lail said. And on another sheet he went on showing how to write the answer.",
   [("paper_shuffle", "ގަނޑެއްގައި", -22)])
sh(70, "\"Ah, now I get it,\" Asil said. \"Lail, I'll be right back, just going to the restroom,\" Asil said, getting up. \"Don't take long,\" Lail said.")
sh(71, "Asil walked out of the room. Lail went on writing answers to more questions. Not long after Asil left, hearing the door open, Lail looked at the screen.",
   [("door_open", "ދޮރުލެއްޕި", -20)])
sh(72, "On the screen in front of him, a girl was seen setting bundles of papers down on the bed and stopping by the dressing table at one side of it.",
   [("paper_shuffle", "ކޮތަޅު", -22)])
sh(73, "Lail watched carefully. Only part of her face showed in the mirror. What Lail could clearly see was her back.")
sh(74, "The girl was dressed in a very short pair of shorts, and Lail longed to see her face properly. \"Oof... so tired.\"",
   [("sigh", "ޓަޔަޑް", -22)])
sh(75, "Just then a phone rang. She took the phone from the pocket of the shorts she was wearing and answered it. \"Hey hi.\"",
   [("phone_buzz", "ރިނގުވާ", -18)])
sh(76, "Saying that, she turned around and sat down around the middle of the bed. Lail saw the girl's face.", hum=True)
sh(77, "Lail found himself leaning back in his chair. It was not a face he had ever seen in that house before. \"What...\"",
   [("gasp", "ލެނގިލެވުނެވެ", -24)])
sh(78, "The girl answered something said on the other end. But at that moment a mischievous smile played on her lips.")
sh(79, "As if she wanted to tease whoever she was talking to. \"What did you eat? Still can't get away from your plate?\" Her voice was teasing.")
sh(80, "She went on talking, laughing. Lail noticed that the girl had trouble speaking Dhivehi.")
sh(81, "Lail noticed the English words she slipped in between every two words. \"It's okay, don't worry...\" the girl carried on.")
sh(82, "After listening for a while to what the other end was saying, she went on again. \"Hmm... hey, listen to me.")
sh(83, "I have something to tell you. It's not my job, but...\" the girl said, falling a little quiet.")
sh(84, "Hearing that, Lail's curiosity seemed to grow. He wanted to know what the girl was about to say.")
sh(85, "And he wanted to know who she was talking to. \"Meet me around 8,\" the girl said, glancing at the watch on her wrist.")
SHOTS = S

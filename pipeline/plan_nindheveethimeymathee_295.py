"""Beat/shot plan for Nindheveethimeymathee episode 295 (used by plan_beats.py).
SCHOOL timeline (A-level year, Lail and Saba 17). New girl Saba exposes Shahid; the long silent look;
Lail at Haizum's CEO office; car; Saba opens the door at Asil's apartment (modest outfit, NOT shorts).
No touching between Lail and Saba (or Asil and Saba); hijab on every girl/woman in every shot."""

UNI_BOY = "white short-sleeved school shirt and dark-navy long trousers"
UNI_SABA = "white long-sleeved school tunic, navy ankle-length skirt and white hijab fully covering her hair and neck"
UNI_SADHEE = "white long-sleeved school tunic, navy ankle-length skirt and cream hijab fully covering her hair and neck"

CLASS = "a bright A-level college classroom in Malé, Maldives: rows of light wooden desks and blue plastic chairs, a blank clean whiteboard, tall windows with louvred shutters opening onto a sunny courtyard with a coconut palm, a ceiling fan, pale-yellow walls"
LOC = {
    "lail_room": "Lail's tidy teenage bedroom in a Malé apartment in the evening: a wooden study desk against the wall with an open laptop, a small desk lamp, a shelf of school books, a window with the lights of neighbouring apartment blocks outside",
    "classroom": CLASS,
    "airport_memory": "the bright arrivals hall of Velana International Airport, Malé, glass walls looking out to the turquoise lagoon and palm trees, a few travellers with suitcases",
    "street": "a narrow sunny street in Malé, Maldives, in the afternoon: pastel-painted four- and five-storey buildings with small balconies, a row of parked motorbikes along one side, a few potted plants, a strip of blue sky, clean paved road",
    "lobby": "the bright modern ground-floor lobby of a corporate office building in Malé: polished pale stone floor, a glass reception desk, potted palms, a pair of steel lift doors, a few office staff walking",
    "corridor": "the third-floor corridor of a modern corporate office in Malé: an open-plan area of desks with computer monitors on one side, a tall dark-wood door with a small plain blank brass plaque at the end, soft carpet, glass partitions",
    "ceo_office": "a spacious modern CEO office in Malé: a large dark-wood executive desk with a leather executive chair, two visitor chairs in front, a desk phone, a tall glass window behind with a view of the Malé skyline and the turquoise sea, bookshelves, a potted plant",
    "office_street": "the street outside a modern glass-fronted office building in Malé in the afternoon, a dark silver car parked at the kerb, a few motorbikes, palm trees in planters",
    "car": "the back of a dark silver car interior in the afternoon: beige leather seats, sunlight through the windows, Malé streets and buildings sliding past outside",
    "asil_building": "the entrance of a tall narrow modern residential apartment building in Malé in the late afternoon: a glass-and-steel front door with an intercom panel beside it, potted plants, a narrow street, the car pulling away",
    "asil_door": "the ninth-floor landing of a modern Malé apartment building in the late afternoon: polished tiled floor, open steel lift doors on one side, an apartment front door standing open opposite with warm light from inside",
}
MOOD = {
    "lail_room": "early evening, deep indigo-blue dusk outside the window, the warm amber desk lamp and the cool white-blue glow of the laptop screen on his face, curiosity",
    "classroom": "morning, bright tropical Malé daylight streaming through the windows, sunny clear weather, lively teenage school atmosphere",
    "airport_memory": "soft hazy golden dreamlike memory glow, bright warm midday sunlight, a quiet hopeful arrival",
    "street": "early afternoon, sunny clear weather, warm bright tropical light with soft shadows, a light breeze, shy teenage awkwardness",
    "lobby": "afternoon, sunny, bright cool office light and warm sunlight through the glass front, purposeful calm",
    "corridor": "afternoon, sunny, cool white office light with warm sunlight through the glass, a quiet nervous moment",
    "ceo_office": "afternoon, sunny clear weather, warm golden sunlight through the tall window, a cautious but affectionate father-son mood",
    "office_street": "afternoon, sunny clear weather, warm bright light",
    "car": "late afternoon, sunny, warm golden light falling through the car windows, gentle motion",
    "asil_building": "late afternoon, sunny, warm golden light slanting between the buildings, soft long shadows",
    "asil_door": "late afternoon, warm golden light from the open apartment door and cool light in the landing, a breathless surprised moment",
}

BEATS = [
    dict(to=4, reason="episode opening: Lail on a video call watches an unknown girl in Asil's room", chars=["lail_young"], loc="lail_room",
         visual="Lail, 17, in his light-grey t-shirt, sitting at his study desk and leaning curiously towards his open laptop, chin on his hand, eyebrows raised; on the laptop screen a soft blurry video-call picture of a teenage girl in a powder-blue dress and white hijab standing in another room holding a phone to her ear; seen from slightly behind his shoulder so both his face in profile and the glowing screen are visible",
         camera="medium over-the-shoulder shot, eye level, the desk top as the calm lower third", amb="room_night"),
    dict(to=6, reason="action change: he slams the laptop shut and covers his face", chars=["lail_young"], loc="lail_room",
         visual="Lail, 17, in his light-grey t-shirt, sitting at his desk with the laptop now shut flat in front of him, both hands pressed over his face, shoulders lifting in a deep breath, embarrassed and flustered; only the warm desk lamp lights him now",
         camera="medium close-up, eye level, the closed laptop and desk as the lower third", amb="room_night"),
    dict(to=11, reason="time jump and scene change: next morning in class, Asil greets Lail with a fist bump", chars=["asil_young", "lail_young"], loc="classroom",
         visual=f"the next morning in the classroom: Asil, beaming, holding out his closed fist and Lail, smiling, bumping it with his own fist at a desk; Asil in his maroon t-shirt and grey track trousers, Lail in his plain light-grey t-shirt and dark jeans (no white shirts); Lail sliding into his seat with his school bag; other students blurred in the background",
         camera="medium two-shot, eye level, the desk tops as the lower third", amb="classroom", transition="black"),
    dict(to=14, reason="character enters: Shahid sits down beside Lail", chars=["lail_young", "shahid_young", "asil_young"], loc="classroom",
         visual=f"three teenage boys in {UNI_BOY} sitting side by side at the classroom desks: Shahid just sitting down beside Lail with a forced casual grin, Lail turned towards him asking a question, Asil leaning in from the other side with a knowing look",
         camera="medium wide three-shot, eye level, desk tops as the lower third", amb="classroom"),
    dict(to=18, reason="character enters: Sadhee walks in, glares at Shahid, and sits apart", chars=["sadhee_young", "shahid_young", "lail_young", "asil_young"], loc="classroom",
         visual=f"Sadhee in her {UNI_SADHEE} walking past the boys' desks with a hurt sideways glare at Shahid, her lips pressed tight; Shahid in his school shirt looking down at his desk; Asil hiding a sly smirk; Lail looking puzzled from one face to the other; she heads to a desk a little apart",
         camera="medium wide, eye level, Sadhee in the foreground on one side, the boys at their desks behind", amb="classroom"),
    dict(to=20, reason="emotional turning point: the new girl walks in and Lail's face changes", chars=["saba_young", "lail_young"], loc="classroom",
         visual=f"Saba, 17, in her {UNI_SABA}, walking in through the classroom doorway with a file under her arm, confident and bright-eyed; in the foreground Lail at his desk in his school shirt, his laughter gone, staring at her in stunned recognition",
         camera="medium shot over Lail's shoulder towards the doorway, faces in the upper two-thirds", amb="classroom"),
    dict(to=25, reason="action change: Saba teases her cousin Asil and offers to tell what happened", chars=["saba_young", "asil_young", "lail_young", "shahid_young"], loc="classroom",
         visual=f"Saba in her {UNI_SABA} standing beside the boys' desks with a teasing grin, playfully waving her file in the air above Asil's head without touching him; Asil, startled, twisting round in his chair to look up at her and laughing; Lail and Shahid watching from their seats; everyone keeps a small distance",
         camera="medium wide, eye level, desks as the calm lower third", amb="classroom", sens="other",
         safe="the head tap and the file swat are shown only as her waving the file above him; no physical contact between the boy and the girl"),
    dict(to=29, reason="action change: Saba announces in broken Dhivehi that Shahid cheated on Sadhee", chars=["saba_young", "asil_young", "shahid_young"], loc="classroom",
         visual=f"Saba in her {UNI_SABA} standing at arm's length in front of the desks, one hand raised as she announces something with frowning eyebrows and dramatic seriousness; Asil at his desk doubled over laughing at her clumsy Dhivehi; Shahid beside him staring at the desk, embarrassed",
         camera="medium shot, slightly low angle from the desks, faces in the upper two-thirds", amb="classroom", sens="other",
         safe="the alleged cheating is only talked about; nothing is shown"),
    dict(to=33, reason="focus change: Shahid's growing panic as Saba mentions photos and videos", chars=["shahid_young", "saba_young"], loc="classroom",
         visual=f"close on Shahid in his {UNI_BOY} sitting at his desk, pale and anxious, eyes darting up; behind him and a little apart, Saba in her {UNI_SABA} standing with her file hugged flat against her chest, arms folded, one eyebrow raised at him",
         camera="medium close-up on Shahid, Saba softly focused behind, eye level", amb="classroom"),
    dict(to=35, reason="action change: Lail stops her; Saba says thank you and goes to sit by Sadhee", chars=["lail_young", "saba_young", "sadhee_young"], loc="classroom",
         visual=f"Lail in his {UNI_BOY} half-rising from his desk with one hand raised in a calm 'stop' gesture, looking firmly but kindly; Saba in her {UNI_SABA} turning away towards a desk further off where Sadhee in her {UNI_SADHEE} sits; Lail's eyes following Saba",
         camera="medium wide, eye level, desks as the lower third", amb="classroom"),
    dict(to=41, reason="focus change: Lail and Asil talk about who Saba is", chars=["asil_young", "lail_young"], loc="classroom",
         visual=f"Lail in his plain light-grey t-shirt and Asil in his maroon t-shirt (no white shirts), sitting side by side at their desks turned towards each other: Asil explaining with open hands and an innocent 'I told you!' face, Lail with one eyebrow raised in disbelief; in the soft background two girls in hijab sitting together at a far desk",
         camera="medium two-shot, eye level, the desk top as the lower third", amb="classroom"),
    dict(to=43, reason="memory: Asil recalls going to the airport to pick Saba up", chars=["asil_young", "saba_young"], loc="airport_memory",
         visual="Asil, 17, in his maroon t-shirt, standing in the bright airport arrivals hall a respectful step away from Saba, 17, in her loose powder-blue dress and white hijab, who pulls a large suitcase and looks around shyly with tired, sad eyes; Asil giving a welcoming wave",
         camera="medium wide, eye level, the shiny floor as the lower third", amb="memory", transition="dissolve"),
    dict(to=46, reason="back to class: Lail glances at Saba and the sad Sadhee", chars=["sadhee_young", "saba_young", "lail_young"], loc="classroom",
         visual=f"Saba in her {UNI_SABA} and Sadhee in her {UNI_SADHEE} sitting together at a desk talking quietly, Sadhee's face downcast and close to tears, Saba leaning towards her comfortingly; in the soft foreground Lail at his desk glancing over at them",
         camera="medium shot, eye level, the girls in focus, Lail softly blurred in the near foreground", amb="classroom", transition="dissolve"),
    dict(to=50, reason="time and scene change: walking home after college, Lail stops to tie his shoelace", chars=["lail_young", "saba_young", "sadhee_young", "asil_young"], loc="street",
         visual=f"on a sunny Malé street after college: Lail in his plain light-grey t-shirt and dark jeans (no white shirt), crouched on one knee tying the lace of his sneaker, school bag on his shoulder, looking back over his shoulder; a few steps behind him Saba and Sadhee in their school uniforms and hijabs walking towards him, Sadhee gloomy; further ahead Asil and Shahid walking away chatting, small in the distance",
         camera="medium wide, low eye level, the paved road as the calm lower third", amb="city_day", transition="black"),
    dict(to=53, reason="action change: Sadhee snaps at Lail; the three walk on slowly", chars=["sadhee_young", "lail_young", "saba_young"], loc="street",
         visual=f"three teenagers walking slowly side by side along the sunny street, an arm's length apart: Sadhee in her {UNI_SADHEE} with arms crossed and an annoyed pout, Lail in his {UNI_BOY} beside her holding his bag strap, his eyes drifting past her towards Saba in her {UNI_SABA} on the far side",
         camera="medium shot walking towards the camera, eye level, the road as the lower third", amb="city_day"),
    dict(to=58, reason="action change: Sadhee whispers to Saba to take tuition from Lail", chars=["saba_young", "sadhee_young", "lail_young"], loc="street",
         visual=f"Sadhee in her {UNI_SADHEE} leaning towards Saba and whispering behind her hand with a sly matchmaking smile; Saba in her {UNI_SABA} pulling a shy horrified face, shaking her head; a few steps ahead Lail in his school shirt walking on, looking back over his shoulder curiously",
         camera="medium two-shot of the girls, Lail softly in the background, eye level", amb="city_day"),
    dict(to=61, reason="emotional turning point: Saba looks at Lail; his faint smile makes her heart jump", chars=["saba_young", "lail_young"], loc="street",
         visual=f"Saba in her {UNI_SABA} looking up at Lail and then lowering her eyes, blushing, her long lashes down, a shy small smile; Lail in his {UNI_BOY} standing an arm's length away with a faint gentle smile; sunlight between them; no touching",
         camera="medium close two-shot in profile, faces in the upper two-thirds, the sunny street softly blurred", amb="city_day", sens="intimacy",
         safe="unmarried teenagers: only a shy look and a smile at arm's length, no touching"),
    dict(to=66, reason="focus change: Lail's racing heart and the silence between them", chars=["lail_young"], loc="street",
         visual=f"close-up of Lail in his {UNI_BOY} on the sunny street, frozen mid-step, lips slightly parted as if to speak but silent, eyes soft and searching, a warm glow of sunlight on his face; behind him in soft blur a girl in a white hijab with her head bowed",
         camera="close-up, eye level, his face in the upper half, soft bokeh of the street below", amb="city_day", sens="intimacy",
         safe="the feelings are shown only through his face; the girl stays at a distance, out of focus"),
    dict(to=68, reason="characters change: Asil and Shahid come back teasing; Sadhee pouts and walks off faster", chars=["asil_young", "shahid_young", "lail_young", "sadhee_young"], loc="street",
         visual=f"Asil and Shahid in {UNI_BOY} standing in the street grinning and pointing teasingly at Lail, who is straightening up with an embarrassed laugh; on the side Sadhee in her {UNI_SADHEE} turning her face away with a pout and striding off quickly",
         camera="medium wide, eye level, the road as the lower third", amb="city_day"),
    dict(to=72, reason="action change: the boys walk behind the two girls while Lail asks about Sadhee and Saba", chars=["lail_young", "asil_young", "shahid_young", "saba_young"], loc="street",
         visual=f"seen from behind: three boys in {UNI_BOY} with school bags walking together along the sunny street, Lail in the middle turning his head to ask Asil something; ahead of them, several steps away, two girls in white school tunics, navy skirts and hijabs (one white, one cream) walking close together and talking",
         camera="wide shot from behind, eye level, the street receding, the road as the lower third", amb="city_day"),
    dict(to=74, reason="scene change: Lail enters the main office building and takes the lift", chars=["lail_young"], loc="lobby",
         visual=f"Lail in his {UNI_BOY} with his school bag walking briskly across the bright office lobby towards the open steel lift doors, not looking at the office workers around him (men in shirts, women in modest office wear and hijab)",
         camera="wide shot, eye level, the polished floor as the lower third", amb="office_day"),
    dict(to=77, reason="location change: at the CEO's door on the third floor, he smiles at the staff and knocks", chars=["lail_young"], loc="corridor",
         visual=f"Lail in his {UNI_BOY} standing before a tall dark-wood door with a small blank brass plaque, taking a deep breath, one hand raised to knock, glancing sideways with a polite small smile at two women office staff in hijabs watching from their desks",
         camera="medium shot from the side, eye level, the carpet as the lower third", amb="office_day"),
    dict(to=81, reason="character enters: Haizum in his executive chair; Lail walks in and sits", chars=["haizum", "lail_young"], loc="ceo_office",
         visual=f"Haizum, about 48, a few grey flecks in his trimmed beard, in his navy suit, leaning back in his big leather executive chair behind the dark-wood desk, a phone glowing softly in one hand, looking up at his son; Lail in his {UNI_BOY} sitting down in the visitor chair opposite, guarded",
         camera="medium wide, eye level, the desk top as the lower third", amb="office_quiet"),
    dict(to=85, reason="action change: father and son talk about the licence and university", chars=["haizum", "lail_young"], loc="ceo_office",
         visual=f"Haizum in his navy suit leaning forward over the desk with his hands clasped, speaking earnestly and warmly; Lail in his {UNI_BOY} in the visitor chair, listening quietly, a cautious softening in his face; a few blank forms on the desk between them",
         camera="medium two-shot across the desk, eye level, the desk top as the lower third", amb="office_quiet"),
    dict(to=88, reason="character enters: the secretary Zeyba brings two coffees", chars=["lail_young", "haizum"], loc="ceo_office",
         visual=f"a young secretary in a modest long-sleeved navy dress and a grey hijab fully covering her hair and neck setting two cups of coffee from a tray on the desk with a friendly smile; Lail in his {UNI_BOY} smiling up at her in thanks; Haizum in his navy suit nodding",
         camera="medium wide, eye level, the desk top as the lower third", amb="office_quiet"),
    dict(to=90, reason="return to the father-son conversation: the dinner invitation", reuse="beat_024", loc="ceo_office",
         visual="(reuse of beat_024)", amb="office_quiet"),
    dict(to=92, reason="scene change: Lail leaves the building and gets into his own car with a driver", chars=["lail_young"], loc="office_street",
         visual=f"Lail in his {UNI_BOY} carrying a paper bag, walking out of the glass office entrance towards a dark silver car parked at the kerb, the back door open; a driver in a white shirt at the wheel",
         camera="medium wide, eye level, the pavement as the lower third", amb="city_day"),
    dict(to=97, reason="location and action change: in the car, his mother calls", chars=["lail_young"], loc="car",
         visual=f"Lail in his {UNI_BOY} sitting in the back seat of the moving car holding a phone to his ear, a warm happy smile fading into a quieter, careful look; a paper bag beside him on the seat; a driver's shoulder visible in the front; sunlit Malé street through the window",
         camera="medium close-up, eye level, the seat as the lower third", amb="car_interior"),
    dict(to=99, reason="location change: the car stops at Asil's building and Lail rings the bell", chars=["lail_young"], loc="asil_building",
         visual=f"Lail in his {UNI_BOY} with his school bag standing at the glass front door of a tall narrow apartment building, pressing the intercom button, waiting; the silver car pulling away behind him",
         camera="medium shot, eye level, the pavement as the lower third", amb="city_day"),
    dict(to=102, reason="emotional turning point: the lift opens and Saba is standing at the open door", chars=["saba_young", "lail_young"], loc="asil_door",
         visual="Lail in his white school shirt and dark-navy trousers stepping out of the lift and stopping short, surprised and breathless; across the landing, a few metres away, Saba, 17, standing in the open apartment doorway in her loose long-sleeved ankle-length powder-blue dress and white hijab fully covering her hair and neck, holding the door, looking at him with wide eyes; no touching",
         camera="medium wide, eye level, from beside the lift, the tiled floor as the lower third", amb="home_day", sens="clothing",
         safe="the narration's short shorts, loose T-shirt and loose hair are ignored: Saba in her modest default powder-blue dress and white hijab"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Meet me around eight,\" the girl said, glancing at the watch on her wrist. \"Okay, same place. Bye.\"")
sh(2, "The girl put the phone down. Lail had been listening to everything she said with intense curiosity. At the same time,")
sh(3, "his heart and mind were busy looking for answers to the questions rising inside him about who she was.")
sh(4, "Because Lail knew that Asil had no full sister of that age. The urge to find out who she was kept growing in his heart.")
sh(5, "With a faint smile Lail looked at the laptop screen in front of him. At that moment his eyes went wide, and with a sudden movement he slammed the laptop shut.",
   [("soft_thud", "ލައްޕާލިއެވެ", -16)])
sh(6, "Calming himself, he covered his face with both hands. And with it he let out a deep breath.",
   [("sigh", "ފުންނޭވާއެއް", -20)])
sh(7, "After that incident he met Asil again the next morning, when he walked into class.")
sh(8, "Seeing Lail, Asil held out his clenched fist towards him with a happy smile.")
sh(9, "Lail clenched his fist the same way, tapped it gently against Asil's, then opened his hand and greeted him.")
sh(10, "It was a greeting that showed the close friendship between the two. \"Where did you go last night? Not a word from you afterwards,\" Asil asked Lail.")
sh(11, "\"I didn't go anywhere, I was at home,\" Lail said, sitting down at the desk. \"Your phone was switched off too. I called you so many times.\"")
sh(12, "said Asil, sitting down on the chair next to him. \"Hey, what are you two plotting without me?\" Shahid asked, sitting down beside Lail.")
sh(13, "\"We're not plotting anything. Why did you vanish yesterday — where were you?\" Lail asked. \"Didn't Asil tell you what happened?\" Shahid said, looking at Asil.")
sh(14, "At Shahid's answer Lail's eyes also turned to Asil. \"Sadhee... long life to you, eh!\" Asil changed the direction of the conversation.")
sh(15, "At that moment Shahid's eyes fell on Sadhee, who had just come in. And without delay he dropped his head.")
sh(16, "Sadhee, giving a small cough, kept her eyes on Shahid as she walked past and sat down a little away from them.",
   [("breath", "ކަޅި", -24)])
sh(17, "Seeing that, a sly smile spread over Asil's lips, while Lail looked at the two faces in surprise. \"Did something happen behind my back?\"")
sh(18, "Lail asked with great curiosity. \"These two went out one night to meet each other!\" Asil said with a light laugh.")
sh(19, "Though Lail burst out laughing at what Asil was telling him, the colour of his face suddenly changed and his laughter stopped.")
sh(20, "His eyes had stopped on the new girl who had just walked into the class. It was the very girl he had seen at Asil's home yesterday.",
   hum=True)
sh(21, "As she passed by Asil, she tapped him lightly on the head. Startled, Asil turned round to look behind him.")
sh(22, "\"You are better at communication, but you cannot be an engineer — you would rather be a politician.\"")
sh(23, "the girl said, swatting Asil with the file in her hand. \"I will tell you what happened,\" she said, looking at Shahid and Lail.",
   [("paper_shuffle", "ފައިލުން", -22)])
sh(24, "\"Will you tell it in Dhivehi? Or...\" Asil turned to the girl with a sly smile. \"Fine, Dhivehi!\"")
sh(25, "the girl said in an annoyed tone. Asil seemed to know her ways well.")
sh(26, "The sly smile was still on his lips. \"Shahid was unfaithful to Sadhee. While going around with another girl...\"")
sh(27, "The girl stopped. She made a face as if thinking about what to say next. Then, after a deep breath, she went on: \"Caught red-handed.\"",
   [("breath", "ފުންނޭވާއެއް", -22)])
sh(28, "the girl said, knitting her eyebrows. Asil burst out laughing. He knew she couldn't speak Dhivehi properly. \"Saba...")
sh(29, "Saba, that's enough, stop it,\" Asil said, laughing. \"Besides, don't talk without knowing the truth of the matter,\" Asil said.")
sh(30, "But Saba was in no mood to let it go. She carried on telling the details of what had happened in English.")
sh(31, "Shahid sat quietly without saying a word. But when she mentioned there were photos and videos of it, Shahid's worry grew greater than before.",
   [("heartbeat", "ކަންބޮޑުވުން", -22)])
sh(32, "Looking at Shahid, Saba raised her eyebrows, pressed the file in her hand against her chest and folded her arms.")
sh(33, "Shahid's face showed the utmost panic and worry, because he was the one who knew Saba's temper and ways best of all.")
sh(34, "\"Now stop that! This is neither the place nor the time to talk about something like that,\" — before Asil could say anything more,")
sh(35, "Lail said it quickly. \"Thank you.\" With that, Saba went and sat down next to Sadhee, and Lail looked after her. \"Who is that girl?\"")
sh(36, "Lail asked, looking at Asil. \"What girl? Didn't you recognise her, Lail? That's Saba, my cousin, the younger one.")
sh(37, "Didn't I tell you about my aunt who lives in Australia?\" Asil said, as though it were someone Lail knew very well.")
sh(38, "Lail stared at Asil strangely, as if asking when he had ever told him that. \"Told me?")
sh(39, "You must have said that in a dream,\" Lail said. \"No, seriously. I always talk about having a little cousin called Saba.")
sh(40, "That's her. After Saba's father passed away, she moved to Malé,\" Asil explained. \"Ah...")
sh(41, "Now I remember — you said a relative in Australia had passed away, but you never said anything about Saba.\"")
sh(42, "Lail said to Asil, raising his eyebrows again. Asil sank into deep thought. Had he really never told him about Saba? No.")
sh(43, "He remembered telling him even on the day he went to the airport to pick Saba up. \"All right, forget about it. That's the end of it.\"")
sh(44, "Lail said. With that Asil settled back in his chair. Lail cleared his throat a little and let his eyes wander to where Saba sat.")
sh(45, "Saba and Sadhee were talking about something. From the dejection on Sadhee's face it was clear that if anyone asked her one more question, the sadness in her heart would burst,",
   hum=True)
sh(46, "and she might cry. When college ended, everyone set off towards wherever they had to go.")
sh(47, "As Asil and Shahid headed home deep in conversation, Lail walked along with them.",
   [("footsteps_pavement", "ހިނގަމުންނެވެ", -24)])
sh(48, "Just then Lail's shoelace came undone and he crouched down to tie it. At that moment Sadhee and Saba, who were coming along behind them talking, caught his eye.")
sh(49, "Even then Sadhee's face showed signs of dejection. When he had tied his shoelace, Lail stood up and straightened himself.")
sh(50, "And he waited for the two of them to catch up with him. \"Sadhee,\" Lail called to her.")
sh(51, "\"If you want to plead Shaadde's case, forget it,\" Sadhee said angrily. \"I'm not pleading anyone's case. I just called your name.\"")
sh(52, "Even though he was talking to Sadhee, Lail's eyes were fixed on Saba. \"I'm so fed up,\" Sadhee said. Silence.")
sh(53, "The three of them walked on slowly. Lail didn't have much to say to Sadhee either — the only thing to talk about was her and Shahid. \"Saba!")
sh(54, "Why don't you take those lessons from Lail? I'm sure every lesson is complete in his books. He has the best grades and the best manners,")
sh(55, "and he's a really diligent student,\" Sadhee whispered, so softly that only Saba could hear. \"I can't, I have never talked to him.\"")
sh(56, "Saba said, pulling a face. \"Hey! He's Asil's best friend, there's no need to be so shy.")
sh(57, "He's a really good boy, and he'll give you tuition too. Why don't you ask him about the lessons you don't understand and clear them up?")
sh(58, "He's really good at Dhivehi too,\" Sadhee said softly as she walked on. \"What are you two whispering about?\"")
sh(59, "Lail asked, hearing their secret whispering. Saba looked towards Lail.")
sh(60, "At the faint smile on Lail's lips, Saba's heart seemed to jump. Because of that deep look she felt as if her whole body had frozen.",
   [("heartbeat", "ތެޅިގަތް", -20)], hum=True)
sh(61, "As her lashes dropped down over her cheeks, Saba lowered her head. In those few seconds her heartbeat quickened,",
   hum=True)
sh(62, "and a strange feeling, hard to describe, was born in her heart. Because of Saba's deep look, Lail's heartbeat quickened too.",
   [("heartbeat", "ތެޅުން", -22)], hum=True)
sh(63, "It was as if an indescribable current ran through every vein of his body. No words passed between them, and the moments slipped by.",
   hum=True)
sh(64, "Lail's question got no answer. It was as though a lock had been put on both their tongues with that question.")
sh(65, "Lail's foolish heart, too, which would not listen, was stretching out like a wave to pour out the emotions surging in it at that moment. But,")
sh(66, "though the feelings of his heart reached his tongue, there was no way for them to come out in the form of words. All talk stopped,")
sh(67, "and they sank into silence. \"Here he comes,\" Asil said, pointing him out to Shahid. \"Afraid you'll die laughing, is that it?\" Asil asked.")
sh(68, "\"My shoelace came undone,\" Lail said. \"Sadhee, are you angry?\" Asil asked. Sadhee pouted. And she began to walk faster.",
   [("footsteps_pavement", "ހިނގުން", -22)])
sh(69, "Saba also walked off along with Sadhee. Lail began walking with Asil and Shahid. \"I'm totally confused now. Sadhee — when did she and Shaadu become a couple?")
sh(70, "Isn't she one of your own family?\" Lail asked as they walked on. \"Hmm, she'd be a second cousin, right!\" Asil said, thinking. \"Yeah...\" Shahid said.")
sh(71, "\"And Saba?\" Lail asked. \"My mum's younger sister's daughter,\" Asil said. \"Oh...\" Lail walked on,")
sh(72, "listening to what the two of them were talking about. Saba and Sadhee, walking ahead of them, were also deep in some conversation of their own.")
sh(73, "Lail went in through the door of the main building he could see on the left. He paid no attention to any of the staff moving about the place.")
sh(74, "He knew very well which way to go and where he had to get to. He took the lift straight up to the third floor.",
   [("lift_ding", "ލިފްޓަށް", -20)])
sh(75, "He stopped at the door of the room marked 'CEO', looked at the sign and let out a deep breath. Calming himself, he looked around,",
   [("breath", "ނޭވާއެއް", -22)])
sh(76, "and gave a faint smile to the women staff who were looking his way. Then, composing himself, he knocked on the door.",
   [("knock", "ޓަކިޖަހައިލިއެވެ", -16)])
sh(77, "At once a deep, manly voice was heard from inside. \"Come in.\" With permission given, Lail opened the door and went in.",
   [("door_open", "ދޮރުހުޅުވާލައިފައި", -20)])
sh(78, "Haizum, leaning back in the big executive chair typing a message on his phone, looked up at Lail as he came in.",
   [("phone_game_taps", "ޓައިޕްކުރަން", -24)])
sh(79, "Gently closing the door behind him, Lail walked forward. Haizum sent the message and put the phone aside. \"Sit down.\"",
   [("door_close", "ދޮރުލައްޕައިލުމަށްފަހު", -20)])
sh(80, "Haizum said. Lail went and sat in the chair in front of him. Haizum picked up the phone on the desk and called his secretary.")
sh(81, "He asked her to bring two cups of coffee and looked at Lail. \"Still angry with Dad?\" Haizum asked.")
sh(82, "Lail shook his head as if to say no. \"How is Mum?\" Haizum asked. \"Okay. Big sister's okay too.\"")
sh(83, "Lail answered before he could ask anything more. \"The form you need for your motorbike licence is filled in now.")
sh(84, "Dad wants you to have the licence done by the time your A-levels finish. And at the same time, Dad is now working on finding a good place to send you and your sister for higher education.")
sh(85, "Tell Dad which university you want to go to, and then Dad will look up information about that place too,\" Haizum said.")
sh(86, "That was when Haizum's secretary brought two cups of coffee on a tray and set them in front of father and son. \"Thank you, Zeyba.\"",
   [("cup_clatter", "ބެހެއްޓި", -20)])
sh(87, "Lail said with a smile. Zeyba smiled back at Lail. \"Shukuriyya,\" Haizum said too.")
sh(88, "Then Zeyba took the empty tray and left the room. \"My son! Why don't you bring your sister tonight and join Dad and Grandma for dinner?")
sh(89, "Grandma would be so happy. She's always complaining that she never sees you two,\" Haizum said lovingly, picking up his coffee cup.")
sh(90, "\"I'll tell my sister,\" Lail answered. After spending a little while talking with his father, Lail left the room.")
sh(91, "And he walked out of his father's office building towards his own car, parked to one side.")
sh(92, "As soon as he had settled into the seat of the car, the driver drove off. Lail put the bag his father had given him on the back seat.",
   [("car_drive_off", "ދުއްވާލިއެވެ", -20)])
sh(93, "Just then his phone began to ring. It was his mother calling. With a happy smile on his face, Lail hurried to answer.",
   [("phone_buzz", "ރިންގުވާން", -18)])
sh(94, "\"Hello, Mum,\" Lail answered. \"So, have you left that place?\" his mother Sana asked. \"Yes.")
sh(95, "I'm in the car, going to Asil's house,\" Lail answered. \"Okay... Don't go anywhere else from that house — come home as soon as you can.\"")
sh(96, "There was worry in Sana's voice. \"All right. But Dad said to go and see Grandma tonight,\" Lail answered quietly.")
sh(97, "\"Then have you told your sister about it?\" she asked from the other end. \"No, I'm messaging her now.\"")
sh(98, "After saying that, Lail put the phone down and typed a message to his sister and sent it. When the car stopped outside Asil's house, Lail told the driver he would call when it was time to pick him up, and got out.",
   [("phone_game_taps", "ލިޔެލާފައި", -24), ("car_door", "ފޭބިއެވެ", -20)])
sh(99, "He walked briskly to the house, rang the bell and waited for the door to open. When the door was opened from inside,",
   [("doorbell_buzz", "ބެލް", -18), ("door_open", "ހުޅުވައިލުމުން", -22)])
sh(100, "he went in, got into the lift in front of him and pressed for the ninth floor. When he stepped out of the lift, Saba was standing there with the door open.",
   [("lift_ding", "ފޭބިއިރު", -20)])
sh(101, "Lail stopped short. Saba was wearing a pair of short shorts and a loose white T-shirt.",
   [("heartbeat", "މަޑުޖެހިލެވުނެވެ", -22)], hum=True)
sh(102, "Her hair was loosely tied and fell forward over one side. [visual: modest powder-blue dress and white hijab instead]", hum=True)
SHOTS = S

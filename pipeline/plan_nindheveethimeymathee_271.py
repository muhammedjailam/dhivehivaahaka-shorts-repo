"""Beat/shot plan for Nindheveethimeymathee episode 271 (used by plan_beats.py).
PRESENT timeline. Saba's fall is NEVER shown (phone glow + shocked face + dropped cup); in hospital she is shown
resting propped up, white hospital headscarf, calm face, NO bandages. Lail never touches Saba/Sadhee/Miya."""

PENT = "Lail's modern beachfront penthouse on the west side of Hulhumale, Maldives"
HOSP = "a modern clean hospital in Male', Maldives"
LOC = {
    "dawn_city": "the west-side beachfront of Hulhumale, Maldives, at sunrise: a row of tall modern white apartment towers along a wide palm-lined promenade, the calm turquoise lagoon and the artificial white-sand beach, small birds on the palm fronds",
    "promenade": "the palm-lined beachfront promenade of Hulhumale in the early morning: a wide paved jogging path, park benches, low beachfront cafe terraces with small tables, the calm empty lagoon beyond",
    "school_street": "a clean wide street in Hulhumale in the early morning: modern apartment blocks, young trees, a school gate with a plain painted wall (no signs), parked motorbikes, people walking to work",
    "balcony_day": f"the wide balcony terrace of {PENT}: a glass-and-steel railing, a green artificial-grass carpet on the floor, two cushioned outdoor chairs and a small round coffee table with a laptop, the turquoise sea and the beachfront towers below",
    "bedroom_day": f"the bedroom of {PENT} in the morning: a tall open wooden wardrobe with neatly hung shirts, a small wooden cabinet beside it with a wallet and keys on top, a large window with white sheer curtains",
    "hosp_entrance": f"the glass entrance doors and bright lobby of {HOSP}: a reception counter in the background, polished floor, potted plants, sunlight from outside",
    "icu_corridor": f"a long quiet corridor outside the intensive care unit of {HOSP}: pale walls, closed double doors with frosted glass panels, empty plastic chairs, polished floor, no people in the distance",
    "theatre_corridor": f"the waiting corridor outside the operation theatre of {HOSP}: a pair of closed swinging doors with round porthole windows, a row of blue plastic chairs, a small anxious crowd of relatives and friends, pale walls",
    "waiting_area": f"a small waiting area in {HOSP}: rows of connected blue plastic chairs, a low table, a potted plant, a large window with daylight",
    "recovery_door": f"a corridor outside the recovery room of {HOSP}: a closed door with a tall narrow glass panel, through which part of the softly lit recovery room is seen, a nurses' trolley along the wall",
    "recovery_room": f"inside the softly lit recovery room of {HOSP}, seen through the glass panel of a door: a hospital recliner with raised white pillows, a monitor glowing softly without numbers, an IV stand in the background",
    "sitting_night": f"the spacious sitting room of {PENT} at night: a low grey sofa, a coffee table, a large flat TV on a low cabinet, floor-to-ceiling glass doors to the balcony showing the dark sea and the city lights",
    "airport_memory": "the arrivals hall of Velana International Airport, Maldives: bright glass walls, luggage trolleys, the lagoon and seaplanes visible outside, travellers in the background",
    "balcony_night": f"the balcony terrace of {PENT} at night: a small private terrace pool with calm empty water lit softly from below, cushioned outdoor chairs beside it, a glass railing, the dark sea and the lights of Male' across the water",
    "car_night": "inside a modern car driving along a Hulhumale road at night: dashboard lit softly, a phone in a dashboard holder glowing, streetlights and palm trees sliding past the windscreen",
}
MOOD = {
    "dawn_city": "sunrise, soft gold light breaking through blue haze, clear sky, peaceful, gentle and fresh",
    "promenade": "early morning, bright soft sunlight, long shadows, clear sky, lively and cheerful",
    "school_street": "early morning, warm bright sunlight, clear sky, busy and hopeful everyday life",
    "balcony_day": "morning, bright warm sunshine, clear blue sky, a gentle sea breeze, calm and focused",
    "bedroom_day": "morning, bright daylight through sheer curtains, urgent hurried energy, anxiety",
    "hosp_entrance": "late morning, bright daylight through the glass doors, cool white lobby light, urgency and panic",
    "icu_corridor": "daytime, cool white fluorescent light, deathly quiet, empty and frightening",
    "theatre_corridor": "daytime, cool white fluorescent light, heavy tense waiting, worry and grief",
    "waiting_area": "afternoon, soft daylight from the window mixed with cool fluorescent light, weary, tense reunion",
    "recovery_door": "afternoon, cool dim corridor light, soft blue glow from the room beyond the glass, hushed and tender, aching worry",
    "recovery_room": "soft dim blue-white light, quiet and still, fragile hope",
    "sitting_night": "night, the room dark except for a single warm amber floor lamp and moonlit indigo light from the glass doors, lonely and restless",
    "airport_memory": "soft hazy dreamlike memory glow, bright afternoon light through glass walls, gentle surprise",
    "balcony_night": "night, deep indigo sky with a cloudy moon, soft turquoise glow from the pool lights, warm amber light from the room behind, lonely and pensive",
    "car_night": "night, dark car interior, orange streetlights sweeping across his face, the cool glow of the phone, weary irritation",
}

LAIL_TEE = "Lail now in a plain dark-grey T-shirt and dark trousers, his hair uncombed"

BEATS = [
    dict(to=2, reason="episode opening: sunrise over Hulhumale, birdsong", loc="dawn_city",
         visual="the beachfront of Hulhumale at sunrise seen from above the water: a row of tall white apartment towers catching the first gold light, palm trees along the promenade, small birds perched on a palm frond in the foreground, the calm lagoon; no people close up",
         camera="wide establishing shot, the towers and sky in the upper two-thirds, the calm lagoon as the lower third", amb="dawn_exterior"),
    dict(to=5, reason="scene change: the morning promenade — joggers, beach walkers, breakfast at cafes", loc="promenade",
         visual="early morning on the beachfront promenade: a few men in tracksuits and women in long loose sportswear with hijabs jogging along the paved path, people having breakfast at small cafe tables on a terrace beside it, the calm empty lagoon beyond with no swimmers",
         camera="wide shot, eye level, the paved path forming a calm lower third", amb="beach_day", sens="clothing",
         safe="the narration mentions swimmers; the sea is shown calm and empty, all women in modest sportswear with hijabs"),
    dict(to=7, reason="scene change: parents walking children to school, people hurrying to work", loc="school_street",
         visual="a sunny street in Hulhumale: a father and a mother in a hijab walking small children in school uniforms (girls in white hijabs) towards a school gate, the children carrying backpacks; office workers walking quickly along the pavement and motorbikes passing in the background",
         camera="medium wide, eye level, the pavement as the lower third", amb="city_day"),
    dict(to=9, reason="scene and character change: Lail on his penthouse balcony with coffee and laptop", chars=["lail"], loc="balcony_day",
         visual="Lail sitting in a cushioned chair on his sunny balcony terrace, leaning forward over the small round coffee table, typing fast on an open laptop (the screen faces away from the viewer), a white coffee cup with a thin wisp of steam beside it, intent and focused face, the turquoise sea behind the glass railing",
         camera="medium shot, eye level, from the side, the table top and green grass carpet as the lower third", amb="upper_balcony"),
    dict(to=13, reason="action change: he stands at the railing with his coffee, then checks his phone", chars=["lail"], loc="balcony_day",
         visual="Lail leaning his forearms on the glass railing of the balcony, the coffee cup in his left hand, his phone in his right hand glowing softly (screen not visible), relaxed half-smile, the sea and towers far below in bright morning light",
         camera="medium shot from slightly behind and to the side, his face in profile in the upper third", amb="upper_balcony"),
    dict(to=16, reason="strong emotional turning point: the breaking news — he freezes, phone and cup fall", chars=["lail"], loc="balcony_day",
         visual="in bright sunny morning daylight under a clear blue daytime sky (not night): Lail frozen in shock by the railing, eyes wide and unseeing, lips parted, his empty hands half-raised and open in front of him; at his feet on the green artificial-grass carpet lie his phone face-down and a white coffee cup tipped over with a small brown coffee stain spreading on the grass",
         camera="medium shot, slightly low angle, his stunned face in the upper third, the dropped cup and phone in the lower third", amb="upper_balcony",
         sens="other", safe="Saba's fall is never shown and the news headline is not readable: only his stunned face and the dropped cup and phone"),
    dict(to=19, reason="action change: the phone rings on the grass carpet; tears; he crouches to pick it up", chars=["lail"], loc="balcony_day",
         visual="Lail crouching on the green artificial-grass carpet, tears running down his cheeks, his hand trembling as he reaches for his phone which lies glowing on the grass (screen blurred, no text), his face blurred with grief",
         camera="close medium shot, eye level, his tear-streaked face in the upper half", amb="upper_balcony"),
    dict(to=24, reason="action change: on the phone with his elder sister, forcing composure", chars=["lail"], loc="balcony_day",
         visual="in bright sunny morning daylight under a clear blue daytime sky (not night): Lail standing by the glass railing holding the phone to his ear with one hand, wiping tears from his eyes with the back of the other hand, forcing a steady face, red-rimmed eyes, the bright sea behind him",
         camera="medium close-up, eye level, the railing as the lower third", amb="upper_balcony"),
    dict(to=27, reason="scene change: he rushes into the bedroom, changes and grabs his wallet", chars=["lail"], loc="bedroom_day",
         visual=f"{LAIL_TEE}, hurrying in his bedroom: the wooden wardrobe doors flung wide open behind him, he snatches his wallet from the top of the small cabinet, his face tense and frantic",
         camera="medium shot, eye level, the polished floor as the lower third", amb="apartment_morning"),
    dict(to=30, reason="scene change: hospital entrance; he almost collides with a woman coming out (Sadhee)", chars=["lail", "sadhee"], loc="hosp_entrance",
         visual=f"{LAIL_TEE}, rushing through the hospital's glass doors and pulling up short an arm's length from a woman coming out — Sadhee — both of them startled and stepping back from each other, he raises one palm in apology without touching her, she clutches her handbag; a reception counter behind",
         camera="medium wide, eye level, the polished floor as the lower third", amb="hospital_day", sens="intimacy",
         safe="the narration's bump is shown as a near-collision at arm's length; no contact between them"),
    dict(to=33, reason="scene change: the deserted ICU corridor", chars=["lail"], loc="icu_corridor",
         visual=f"{LAIL_TEE}, standing alone in the middle of a long empty hospital corridor, out of breath, looking anxiously from one side to the other in front of closed frosted-glass double doors",
         camera="wide shot down the corridor, eye level, the polished floor as the lower third", amb="hospital_corridor"),
    dict(to=36, reason="characters change: a nurse approaches, then Sadhee calls his name from behind", chars=["lail", "sadhee"], loc="icu_corridor",
         visual=f"{LAIL_TEE}, turning around in the corridor towards Sadhee who stands a few steps behind him, her eyes red and puffy, uncertain recognition on her face; in the background a young nurse in light-blue scrubs and a white hijab walks past",
         camera="medium two-shot, eye level, a respectful distance between them", amb="hospital_corridor"),
    dict(to=39, reason="action change: close two-shot, Sadhee explains — she doesn't know what happened", chars=["sadhee", "lail"], loc="icu_corridor",
         visual=f"close two-shot: Sadhee, tearful and exhausted, giving a helpless shrug with her hands spread; {LAIL_TEE}, standing at arm's length facing her with an urgent searching look",
         camera="medium close two-shot, eye level", amb="hospital_corridor"),
    dict(to=42, reason="scene and character change: outside the operation theatre, Asil comes and holds Lail, Miya watches", chars=["asil", "lail", "miya"], loc="theatre_corridor",
         visual=f"outside the operation theatre doors: Asil, weeping, has thrown both arms around Lail's shoulders in a brotherly greeting; {LAIL_TEE}, eyes closed and tearful; a few relatives stand by, and Miya in the background stares at them in surprise",
         camera="medium wide, eye level, the corridor floor as the lower third", amb="hospital_corridor", sens="intimacy",
         safe="a brotherly embrace between two male friends (allowed by the series bible); the women stand apart"),
    dict(to=44, reason="action change: Asil steps back wiping his tears and reproaches Lail", chars=["asil", "lail"], loc="theatre_corridor",
         visual=f"Asil standing back from Lail wiping tears from his cheek with his thumb, his face hurt and reproachful; {LAIL_TEE}, eyes wet, answering softly; the closed theatre doors behind them",
         camera="medium two-shot, eye level", amb="hospital_corridor"),
    dict(to=47, reason="character change: Shahid joins and explains Saba's condition", chars=["shahid", "lail", "asil"], loc="theatre_corridor",
         visual=f"Shahid stepping up beside Lail, speaking quietly and gravely with one hand raised in a calming gesture; {LAIL_TEE}, listening anxiously; Asil beside them with his arms folded and red eyes",
         camera="medium three-shot, eye level", amb="hospital_corridor"),
    dict(to=49, reason="action change: the long anxious wait; Zuhuruf's phone is still off", chars=["sadhee", "asil", "shahid", "lail"], loc="theatre_corridor",
         visual=f"the group waiting on the row of blue plastic chairs outside the closed theatre doors: Sadhee lowering her phone from her ear with a hopeless look, Asil with his head in his hands, Shahid staring at the doors, {LAIL_TEE}, standing against the wall, eyes on the porthole windows",
         camera="wide shot, eye level, the corridor floor as the lower third", amb="hospital_corridor"),
    dict(to=51, reason="character change: the doctors come out — the operation succeeded", chars=["shahid", "asil", "sadhee"], loc="theatre_corridor",
         visual="a doctor in green surgical scrubs and cap stepping out of the swinging theatre doors with a tired reassuring smile, talking to Shahid and Asil; Sadhee behind them raising both palms in gratitude, eyes closed, saying Alhamdulillah",
         camera="medium wide, eye level", amb="hospital_corridor"),
    dict(to=54, reason="scene change: the crowd disperses; Sadhee makes Lail sit in the waiting area, Miya joins", chars=["sadhee", "lail", "miya"], loc="waiting_area",
         visual=f"in the waiting area Sadhee, sitting on the blue plastic chairs, firmly points at the seat a chair away from her for Lail to sit; {LAIL_TEE}, sitting down reluctantly; Miya arriving and sitting down on Sadhee's other side",
         camera="medium wide, eye level, the floor as the lower third", amb="clinic_waiting"),
    dict(to=57, reason="character and action change: Shahid and Asil join; Sadhee confronts Lail about nine years of silence", chars=["sadhee", "lail", "asil", "shahid"], loc="waiting_area",
         visual=f"Sadhee turned towards Lail with a hurt accusing face, one hand pressed to her chest as she speaks; {LAIL_TEE}, sitting a chair away from her, looking down at his clasped hands, closed off; Asil and Shahid standing behind the chairs listening",
         camera="medium wide, eye level", amb="clinic_waiting"),
    dict(to=60, reason="action change: Sadhee falls silent; while she and Miya talk, Lail quietly stands up", chars=["lail", "sadhee", "miya"], loc="waiting_area",
         visual=f"{LAIL_TEE}, quietly rising from the chair with a distant worried look towards the corridor; beside him Sadhee and Miya are turned to each other talking softly, not noticing",
         camera="medium shot, eye level", amb="clinic_waiting"),
    dict(to=64, reason="scene change: at the recovery-room door, two nurses block his view of Saba", chars=["lail"], loc="recovery_door",
         visual=f"{LAIL_TEE}, on tiptoe at a closed door, peering anxiously through its tall narrow glass panel; through the glass two nurses in light-blue scrubs and white hijabs stand by a hospital recliner, one adjusting an IV stand, the other writing on a clipboard, their backs blocking the patient from view",
         camera="medium shot from behind his shoulder, the glass panel in the upper half", amb="hospital_corridor"),
    dict(to=65, reason="strong emotional turning point: he sees Saba's face", chars=["saba"], loc="recovery_room",
         visual="seen through the glass panel of a door: Saba resting propped up against raised white pillows in a hospital recliner, eyes closed, a calm still face, wearing a white hospital headscarf fully covering her hair and neck and a plain pale long-sleeved hospital gown, a light blanket over her, an IV stand in the soft background",
         camera="medium shot through the glass panel, the door frame softly framing the view", amb="icu_room",
         sens="injury", safe="the narration's fully bandaged face is not shown: Saba resting peacefully in a white hospital headscarf, no injuries visible"),
    dict(to=68, reason="character change: Miya stops beside him and questions him", chars=["miya", "lail"], loc="recovery_door",
         visual=f"Miya standing an arm's length beside Lail at the recovery-room door, arms folded, head tilted, a sharp questioning look; {LAIL_TEE}, half-turned towards her, nodding slowly with sad eyes",
         camera="medium two-shot, eye level", amb="hospital_corridor"),
    dict(to=70, reason="action change: he gives a sad smile and walks away; Miya watches suspiciously", chars=["lail", "miya"], loc="recovery_door",
         visual=f"{LAIL_TEE}, walking away down the long corridor with his head lowered, a faint sad smile; Miya in the foreground left behind at the door, watching him go with narrowed suspicious eyes",
         camera="wide shot down the corridor, Miya in the near foreground, the floor as the lower third", amb="hospital_corridor"),
    dict(to=72, reason="time jump: night at the penthouse; Lail pacing restlessly", chars=["lail"], loc="sitting_night",
         visual=f"{LAIL_TEE}, pacing in his dark sitting room at night, one hand rubbing his forehead, exhausted worried face lit by a single amber floor lamp, the glass balcony doors and dark sea behind him",
         camera="medium wide, eye level, the floor as the lower third", amb="apartment_quiet_night", transition="black"),
    dict(to=74, reason="flashback: yesterday at the airport, Saba's surprise message", chars=["lail"], loc="airport_memory",
         visual="Lail in his slate-blue henley with a travel bag over his shoulder, standing in the bright airport arrivals hall looking down at his phone with quiet surprise, the phone casting a soft glow on his face (screen not visible), travellers blurred behind him",
         camera="medium shot, eye level, the polished floor as the lower third", amb="airport", transition="dissolve"),
    dict(to=76, reason="return from the flashback to the night sitting room (same image as beat_026)", chars=["lail"], loc="sitting_night",
         visual="(reuse)", reuse="beat_026", amb="apartment_quiet_night", transition="dissolve"),
    dict(to=79, reason="scene change: on the night terrace by the pool, a call from his friend Jahaadh", chars=["lail"], loc="balcony_night",
         visual=f"{LAIL_TEE}, sitting in a cushioned chair beside the softly lit empty terrace pool at night, holding his phone to his ear with a puzzled frown, the lights of Male' across the dark water",
         camera="medium wide, eye level, the calm pool water as the lower third", amb="balcony_night"),
    dict(to=81, reason="scene and action change: he turns on the TV and sees Saba's smiling face", chars=["lail", "saba"], loc="sitting_night",
         visual=f"seen over Lail's shoulder as he sits on the grey sofa in the dark: the TV screen shows Saba in her lavender hijab smiling warmly at the camera in a red-and-gold studio (no text, no banners on the screen); {LAIL_TEE}, the TV light reflected on his pained face",
         camera="over-the-shoulder medium shot, the TV in the upper half, the dark coffee table as the lower third", amb="apartment_quiet_night",
         sens="other", safe="the TV shows only Saba's smiling face, no news text"),
    dict(to=84, reason="action change: Sadhee's message; he stands up to go", chars=["lail"], loc="sitting_night",
         visual=f"close-up of {LAIL_TEE}, standing up from the sofa, his face lit cool white by the phone in his hand (screen not visible), determined, the TV glow behind him",
         camera="close medium shot, eye level", amb="apartment_quiet_night"),
    dict(to=88, reason="scene change: driving at night; an unwelcome woman's call", chars=["lail"], loc="car_night",
         visual=f"{LAIL_TEE}, driving at night with both hands on the wheel, rolling his eyes with a weary irritated expression while a phone glows in the dashboard holder (screen not visible), orange streetlights sweeping across his face",
         camera="medium shot from the passenger seat, his face in the upper half, the dark dashboard as the lower third", amb="car_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Within the perfection of nature's law, the light of the sun spread over Hulhumale with the lovely songs of the koel birds.")
sh(2, "Caught in the magic of those enchanting songs, many were overcome with drowsiness. Yet although many felt that drowsiness, a great many who had girded themselves with resolve had set out to work.")
sh(3, "Those who wished for good health were busy after the dawn prayer walking laps around the parks.",
   [("footsteps_pavement", "ބުރުއެޅުމުގައި", -24)])
sh(4, "While some shortened the beaches with their running, others found joy swimming in the sea.",
   [("wave_crash", "މޫދުގައި", -24)])
sh(5, "Others were enjoying their morning breakfast at the tables of hotels and cafes by the shore.",
   [("cup_clatter", "ނާސްތާ", -24)])
sh(6, "Many parents, determined to carry the heavy responsibilities of the home, doing their duty and walking their children to school — that sight")
sh(7, "too was one that brought joy to the heart. Along with that, people of all ages trying not to be late for work could be seen on the streets.",
   [("motorbike_pass", "މަގުމަތިން", -22)])
sh(8, "From one of the big buildings built along the west-side beachfront, Lail stepped out of a penthouse onto the balcony holding a steaming cup of coffee.")
sh(9, "Sitting down in the chair, he set the cup in his hand on the small coffee table before him, and began tapping the keys of the laptop in front of him with great speed.",
   [("cup_clatter", "ބެހެއްޓުމަށްފަހު", -22), ("keyboard_typing", "އޮބަން", -22)])
sh(10, "After a little while Lail leaned back in the chair, picked up the cup and took a sip. Then he slowly rose and walked towards the balcony railing.")
sh(11, "Putting his left hand into his pocket and leaning on the railing, he took a sip from the cup.")
sh(12, "Just then, hearing a message arrive on the phone in his right pocket, he took his hand out of his left pocket and moved the cup from his right hand to his left.",
   [("phone_buzz", "މެސެޖެއް", -18)])
sh(13, "Then he reached into his right pocket and took out the phone. He looked at the message. After replying, he went on opening the notifications that had come on Facebook.")
sh(14, "Suddenly Lail's hand stopped moving — at the sight of BREAKING NEWS written in big letters: \"TV announcer Saba has jumped from a balcony.\"",
   [("heartbeat", "ހުއްޓުނެވެ", -18)], hum=True)
sh(15, "The phone and the cup slipped from Lail's hands. As if his strength had left him, he stumbled a step backwards. For a moment it was as if the world had stopped.",
   [("crash_clatter", "ދޫވިއެވެ", -16)], hum=True)
sh(16, "Muffled sounds kept ringing in Lail's ears. It was as if he were drowning somewhere in between.",
   [("heartbeat", "ގުގުމަމުން", -20)], hum=True)
sh(17, "Lail came back to his senses when his phone began to ring on the green artificial-grass carpet laid on the floor.",
   [("phone_buzz", "ރިންގުވާން", -16)])
sh(18, "The tears gathering in his eyes fell without any control. Through the tears the phone looked like something lying under water.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(19, "He was trembling slightly. Lail bent down and picked up the phone. Because his sight was blurred he couldn't read the name on the screen. \"H... hello.\"",
   [("breath", "ތުރުތުރެއް", -24)])
sh(20, "Lail answered the phone. \"Lail, why didn't you tell your big sister you were going to Male'?\" a woman's voice said from the other end. Lail wiped his tears. \"Sorry.\"")
sh(21, "Lail's answer was short. \"Where are little sister and Dad?\" came from the other end. \"They're off the island. Big sister, can I call you in a little while?")
sh(22, "I'm a bit busy right now,\" Lail said hurriedly. \"Wait — has something happened? Your voice sounds so different,\" came the voice from the other end. \"No, big sister,")
sh(23, "everything's okay. Where's little Saha? How is little Saha's fever now?\" Lail asked quickly. \"The fever's down now.\"")
sh(24, "came the voice from the other end. \"Thank goodness. Big sister, I'll call you later.\" Lail hung up, without even waiting to hear what she said.")
sh(25, "Lail hurried from the balcony into the sitting room, and almost at a run went into the bedroom.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(26, "He moved like someone whose own loved one had been hurt. Flinging both wardrobe doors wide open, he took a T-shirt from the hanging clothes and changed.",
   [("creak", "ހުޅުވާލުމަށްފަހު", -22), ("cloth_rustle", "ބަދަލުކޮށްލިއެވެ", -24)])
sh(27, "Without combing his hair or putting on any perfume, he shoved into his pocket the wallet lying on the small cabinet beside the bed, and then")
sh(28, "left the apartment to go to the hospital and got into the lift. After parking the car, Lail went into the hospital almost at a run.",
   [("lift_ding", "ލިފްޓަށް", -20), ("car_door", "ޕާކު", -22)])
sh(29, "Lail went in without looking at the people coming towards him, and so he bumped into someone who was coming out.",
   [("soft_thud", "ލައިގަތެވެ", -22)])
sh(30, "Asking that person's forgiveness, Lail rushed on. Stopping at the counter, he found out where Saba was and went that way.")
sh(31, "Lail's heart grew uneasy and he became anxious, because he didn't know what condition Saba was in. When the lift stopped, Lail hurried towards the ICU.",
   [("lift_ding", "ލިފްޓު", -22)])
sh(32, "When he got to a certain point, Lail's steps slowed. It was quiet near the ICU. There was no sign of anyone there.")
sh(33, "After standing still for a moment, Lail ran that way again. Stopping near the ICU, he looked both ways — to see if anyone was there.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(34, "Just then, seeing a young nurse coming that way, Lail thought of asking her about Saba.")
sh(35, "Before he could ask the nurse anything, a woman's voice came from behind. \"Lail.\" Hearing his name, Lail turned around and looked.")
sh(36, "It was the person Lail had bumped into at the door when he came in. \"Sadhee.\" Lail found himself saying Sadhee's name. \"Is that really you, Lail?\"")
sh(37, "Sadhee asked in an uncertain tone. \"Where's Saba?\" Lail asked about Saba first of all. \"In the operation theatre.\"")
sh(38, "Sadhee said in a hopeless tone. \"What actually happened?\" Lail asked quickly. Sadhee moved her head as if to say she didn't know.")
sh(39, "\"When did this happen?\" Lail asked. \"Late last night. I only found out when the police called me,\" Sadhee said.")
sh(40, "Talking, Sadhee and Lail went towards the operation theatre. When they got there, quite a number of people had gathered.")
sh(41, "Seeing Lail, Asil, about 29, came out from among the people gathered there towards Lail. Asil came forward and, crying, threw his arms around Lail.",
   [("sob_breath", "ރޮމުން", -24), ("cloth_rustle", "ބައްދައިލިއެވެ", -24)], hum=True)
sh(42, "Everyone's eyes stopped on them. Miya stood watching Asil's behaviour in surprise. After a long moment of silence, Asil stepped back from Lail and wiped the tears flowing from his eyes.")
sh(43, "\"Where have you been? Nobody knew where you went or what became of you. Even Haizumbe wouldn't give us a single piece of information about Lail,\" Asil said in a tearful voice.")
sh(44, "\"I didn't go far — I was right there among you all,\" Lail too said in a tearful voice. \"When did you come back to the Maldives?\"")
sh(45, "Shahid asked, stopping beside Lail. \"Yesterday morning,\" Lail answered. \"How is Saba now?\"")
sh(46, "Lail asked before anyone else could ask another question. \"We can't say yet. The doctors are still working...")
sh(47, "Her life was saved because it was the second floor, but nothing can be said for sure yet,\" Shahid said. \"Sadhee, have you reached Zuhuruf?\"")
sh(48, "Shahid asked. \"His phone is still switched off,\" Sadhee said in a hopeless tone. Time went by, playing with the heartbeats of everyone there.")
sh(49, "Worry and despair showed on every face. Ready for heartbreaking news at any moment, they counted the minutes of waiting.",
   [("clock_tick", "ގުނަމުން", -24)])
sh(50, "The doctors came out of the theatre at ease — because the operation they had been doing had succeeded.",
   [("door_open", "ނުކުތީ", -20)])
sh(51, "Telling Shahid and Asil not to lose hope, the doctor walked off. \"Alhamdulillah.\" At the doctors' happy news, Sadhee gave thanks.")
sh(52, "Saba was brought out of the theatre and taken to the recovery room. Since no one could go in there either, some went to the canteen to have something to eat.")
sh(53, "Others went to finish their unfinished work and come back. Almost by force, Sadhee brought Lail along and sat down on one of the chairs in the waiting area —")
sh(54, "to hear the diary of what had happened in Lail's life over the past nine years. Miya came after them and sat down next to Sadhee.")
sh(55, "Shahid and Asil joined them too. \"Where have you been all this time? You didn't answer a single one of all the messages we sent.")
sh(56, "Why did you push us so far away?\" Sadhee said in a complaining tone. \"Not now, Sadhee. I'm not ready to share anything yet.\"")
sh(57, "Lail did not want to share the story of his life with anyone else. His worry was Saba — the moment Saba would wake up.")
sh(58, "Because he didn't know why Saba had done such a thing. His heart was impatient to find out.")
sh(59, "However much they tried to dig into Lail's past, Lail kept stepping back from it without tiring. It was as if Sadhee laid down her weapons.")
sh(60, "Unable to get hold of Lail any further, she fell silent. When Sadhee and Miya got caught up in their conversation, Lail rose from where he sat,",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(61, "and so secretly that nobody noticed, went towards the recovery room. Standing on tiptoe, he looked through the glass pane in the door towards the bed where Saba lay.")
sh(62, "Two nurses were at Saba's side then. One of them, after adjusting the IV, stopped to talk to the other.")
sh(63, "The other one, after checking Saba's pulse, made a note in the file in her hand. Because of the two of them, Saba's face couldn't be seen.")
sh(64, "Lail kept moving his head to try to see Saba's face. When the nurses moved away, Lail could see Saba's face.")
sh(65, "But her whole face was bandaged. Seeing that, Lail's heart began to race. \"You knew Saba before, didn't you?\" Miya asked, stopping beside Lail.",
   [("heartbeat", "އަވަސްވިއެވެ", -20)], hum=True)
sh(66, "At Miya's voice Lail turned around and looked at her. Lail nodded as if to say yes.")
sh(67, "\"My classmate — and my best friend's little cousin,\" Lail said. \"Which classmate?\"")
sh(68, "Miya asked. \"Asil's little cousin,\" Lail said. \"Oh... then why didn't Saba recognise you, Lail? I even asked her before.\"")
sh(69, "Miya asked in a tone full of suspicion. Lail only smiled at the question. \"Maybe it's better if Saba doesn't recognise me now...\"")
sh(70, "Lail said in a hopeless tone. Before Miya could go on to another question, Lail walked off. Asil and Shahid didn't see him,",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(71, "because he knew that if they saw him they wouldn't let him leave. Once again a silent night settled over him in loneliness and despair.")
sh(72, "Lail paced back and forth in the sitting room, full of worry. Not knowing why Saba had jumped, thinking and thinking about it had worn out his mind.",
   [("footsteps_pavement", "ހިނގާލަ", -24)])
sh(73, "Yesterday he had come to Male' at the request of the film's producer, to prepare for the film's premiere night. After he left for the airport, a message to his personal number gave him a little surprise.")
sh(74, "It was a message from Saba. Saba had invited Lail to her show \"Tharinnaa Eku\". Receiving a message from Saba after nine years, Lail didn't want to refuse.")
sh(75, "As agreed long ago, it had been said that if Saba got a job as an announcer and got to host a film programme, Saba would be the very first to take Lail's interview.")
sh(76, "In that way, to keep his promise, Lail had never given an interview to any TV channel or newspaper.")
sh(77, "Lail slowly went out onto the balcony and sat down on one of the chairs by the pool. Just then a call came to Lail's phone. Lail looked at the phone.",
   [("phone_buzz", "ފޯނެއް", -18)])
sh(78, "And answered it. \"Are you watching TV? So this is the beautiful face you've been hiding all these days!\" — the voice of his friend Jahaadh came from the other end.")
sh(79, "Without answering Jahaadh's question, he said he'd call back and hung up. And Lail hurried in from the balcony to the sitting room.")
sh(80, "Sitting down on the sofa, he turned on the TV. The very first thing Lail saw was Saba's smiling face.")
sh(81, "But when he remembered that right now Saba lay in hospital between life and death, his heart ached.", hum=True)
sh(82, "Saba's condition in the hospital rose before his eyes. Just then a message came to Lail's phone. Lail looked at the message.",
   [("phone_buzz", "މެސެޖެއް", -18)])
sh(83, "\"Everyone has left now. I'm staying with Saba tonight. Come if you want, Lail. She's in a room now.\"")
sh(84, "A message from Sadhee. \"On my way.\" Lail typed a message and sent it. Then he got up from the sofa and switched off the TV.")
sh(85, "Lail left the apartment to go to the hospital. He had got into the car and before he could start it, a call came to his phone. Starting the car, Lail looked at the phone.",
   [("car_door", "ކާރަށް", -20), ("phone_buzz", "ފޯނެއް", -18), ("engine_rev", "ކާރުސްޓާޓު", -20)])
sh(86, "He rolled his eyes. Annoyance showed on his face. Driving off, Lail answered the phone. \"Hello.\" Lail answered.",
   [("car_drive_off", "ދުއްވާލަމުން", -20)])
sh(87, "\"In Male', aren't you? I thought you'd never come to Male',\" — it was a woman's voice at the other end. \"What is it? Calling about something?\"")
sh(88, "Lail asked in a fed-up tone. \"Yes — I'm still sitting here waiting for you, Lail. Since you seem to have forgotten, I called to remind you,\" came the voice on the phone. Lail took a deep breath.",
   [("sigh", "ފުންނޭވާއެއް", -20)])
SHOTS = S

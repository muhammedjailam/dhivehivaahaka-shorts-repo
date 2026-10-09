"""Beat/shot plan for Taubaa episode 299 (used by plan_beats.py).
A young man from Riyadh tells the narrator, in a Riyadh mosque, how bad friends led him into years of addiction,
a car crash, a night he thought he was dying, and finally repentance and umrah.
Drugs, alcohol, smoke, the crash and injuries are NEVER shown (series bible substitutions)."""

LOC = {
    "window_night": "a sparse, dim bedroom in a Riyadh apartment at night, a tall window looking out over the far-away scattered lights of the city, plain walls",
    "mosque": "inside a quiet Riyadh mosque in the afternoon, plain cream walls without any decoration or calligraphy, a deep red carpet, slender white columns, soft light through tall arched windows",
    "majlis": "the majlis of a traditional, very religious family home in a Riyadh district, floor cushions along plain walls, a patterned rug, a closed book resting on a small wooden stand, an old brass lamp, no television or screens anywhere",
    "street_dusk": "a narrow residential lane in a Riyadh district at dusk, sand-coloured villa walls, a lone streetlamp just switched on, long shadows",
    "study_room": "a boy's simple bedroom in a Riyadh family home late at night, a wooden desk piled with closed schoolbooks and notebooks, a warm desk lamp, a round wall clock, a dark window",
    "school_yard": "the empty concrete courtyard of a boys' school in Riyadh in harsh midday light, sand-coloured walls, wide concrete steps",
    "courtyard_night": "the walled courtyard of a family villa in Riyadh on a cold winter night, a brand-new white sedan parked inside the gate, a single wall lamp, faint mist in the cold air",
    "highway_fog": "an empty desert highway in Saudi Arabia in the last dark hour before dawn on a winter night, thick drifting fog, no other vehicles",
    "icu": "a hospital intensive-care room at night, a single bed with white sheets, a heart monitor glowing green beside it, a drip stand, dim blue light",
    "dawn_road": "an empty desert highway in Saudi Arabia at dawn, the first gold light rising over the sand, a clear quiet sky",
    "home_room": "a plain room in the father's house in Riyadh in the afternoon, a floor mattress against the wall, light slanting through wooden shutters, an open doorway to a dim corridor",
    "roadside_asr": "a wide roadside in Riyadh in the late afternoon at Asr time, low sand-coloured buildings, a few date palms, cars passing in the golden light",
    "town_school": "the gate of a modest middle school in a smaller Saudi town in the morning, sand-coloured walls, a plain metal gate, soft early sun",
    "car_night": "inside a parked car on a dark empty street of a small Saudi town at night, blurred distant streetlights through the windscreen",
    "classroom": "a plain classroom in a small Saudi town school by day, rows of simple desks, pale walls, a blank board",
    "edge_house": "a lone small house at the far edge of a small Saudi town in the late afternoon, open desert beyond, a dusty unpaved lane",
    "dark_room": "a dim, bare room inside the lone house at night, plain walls, a single weak light from a doorway",
    "washbasin": "a simple white washbasin with a running tap in a plain tiled room at night",
    "prayer_room": "a small bare room in the lone house at night, a prayer rug on the floor facing a plain wall, a single dim lamp",
    "brother_house": "the majlis of the elder brother's house at night, warm light, a long dinner cloth spread on the carpeted floor with plates of rice and dishes, floor cushions",
    "car_drive": "inside a car driving at night through a small Saudi town, streetlights sliding past the windows",
    "clinic": "a small private clinic examination room at night, white walls, an examination couch, a heart monitor, a cool fluorescent light",
    "clinic_exit": "the doorstep of a small private clinic in a Saudi town in the early morning, a quiet street",
    "sleep_room": "a bare room in the lone house at night, a floor mattress, pale moonlight through a small window",
    "town_mosque": "inside a simple small-town mosque in Saudi Arabia in the day, plain white walls without any calligraphy, a green carpet, soft light",
    "makkah": "the open marble courtyard of Masjid al-Haram in Makkah at dusk, the Kaaba seen far away across the courtyard, crowds of pilgrims in white circling it, the minarets glowing",
    "dua_sky": "the open desert at dawn, a lone slender minaret silhouetted against a gold and teal sky, rays of light through thin clouds",
}
MOOD = {
    "window_night": "night, cold steel-blue haze, a faint amber city glow, lonely and heavy",
    "mosque": "afternoon, calm soft light, peaceful and reflective",
    "majlis": "warm amber lamplight, safe, dignified, remembered childhood",
    "street_dusk": "dusk, fading amber light and deep blue shadows, uneasy",
    "study_room": "late night, a pool of warm lamplight in a dark room, restless and strained",
    "school_yard": "harsh flat midday light, empty and defeated",
    "courtyard_night": "cold winter night, steel-blue light, mist, secretive and tense",
    "highway_fog": "pre-dawn darkness, white headlight beams in grey fog, ominous and silent",
    "icu": "night, dim blue hospital light and a soft green monitor glow, fragile stillness",
    "dawn_road": "dawn-gold light, quiet mercy, a new chance",
    "home_room": "dusty afternoon light, stale and confined",
    "roadside_asr": "late afternoon golden light, long shadows, stubborn and lonely",
    "town_school": "soft morning light, a cautious new start",
    "car_night": "night, dark car interior, blurred amber lights outside, hollow and lost",
    "classroom": "flat daylight, dull, absent and numb",
    "edge_house": "late afternoon, dusty amber light, isolated",
    "dark_room": "night, deep shadows, cold blue light, dread",
    "washbasin": "night, a single cool light, urgency, clean running water",
    "prayer_room": "night, a single dim warm lamp, trembling, humble and fearful",
    "brother_house": "warm family lamplight suddenly broken by alarm",
    "car_drive": "night, passing streetlights, urgent and confessional",
    "clinic": "cool fluorescent clinic light, tense",
    "clinic_exit": "early morning, soft dawn-gold light, relief, a new life",
    "sleep_room": "night, pale moonlight, fear and awakening",
    "town_mosque": "soft daylight, peace, brotherhood",
    "makkah": "dusk, soft gold light on white marble, awe, tears of repentance",
    "dua_sky": "dawn, gold and teal light, hope and mercy",
}

BEATS = [
    dict(to=2, reason="episode opening: the young man lost in years of heedlessness", chars=["riyadh_man"], loc="window_night",
         visual="the gaunt young man sitting alone on the floor by a tall window at night, his head resting heavily in one hand, the far-away city lights blurred behind the glass, his face half in shadow",
         camera="medium shot, slightly low angle", amb="city_night_far", sens="drugs/intoxication",
         safe="his years of intoxication shown only as a lonely figure by a night window with distant city lights"),
    dict(to=3, reason="scene change: the narrator meets him in a Riyadh mosque", chars=["riyadh_man"], loc="mosque",
         visual="the young man, now calm and at peace, his off-white thobe clean and neat, sitting cross-legged on the mosque carpet and talking earnestly with a gentle sad smile to an older man seen only from behind in a white thobe and white ghutra",
         camera="medium two-shot over the listener's shoulder", amb="mosque_interior"),
    dict(to=4, reason="flashback: his very religious father at home", chars=["pious_father", "riyadh_boy"], loc="majlis",
         visual="the grave, kind father sitting on a floor cushion in the majlis with a closed book in his lap, the young boy sitting beside him listening respectfully, a warm brass lamp, a simple room with nothing else in it",
         camera="medium wide, eye level", amb="home_day", transition="dissolve"),
    dict(to=6, reason="time jump and new characters: at fourteen the boy meets a group of bad friends", chars=["riyadh_boy"], loc="street_dusk",
         visual="the boy standing in a narrow lane at dusk, looking up uncertainly, surrounded by three older young men in thobes seen only from behind as dark silhouettes against the last light, their faces never visible, closing around him",
         camera="medium wide from behind the silhouettes", amb="street_night", sens="bad friends",
         safe="the bad friends are only dark silhouettes seen from behind; nothing is handed over"),
    dict(to=10, reason="action change: exam time, staying awake night after night", chars=["riyadh_boy"], loc="study_room",
         visual="the boy at his desk late at night bent over open notebooks under a warm desk lamp, eyes unnaturally wide and red-rimmed, a pen in hand, the wall clock showing a late hour, the window black behind him",
         camera="medium close-up, side angle", amb="room_night", sens="drugs (white pills to stay awake)",
         safe="the pills are never shown; only a boy studying sleeplessly by lamplight with tired wide eyes"),
    dict(to=11, reason="the bad friends return with the red pills (reuse)", reuse="beat_004", chars=["riyadh_boy"], loc="street_dusk",
         visual="(reuse) the boy among the shadowy friends", amb="street_night", sens="drugs (red pills)",
         safe="reuse of the silhouetted-friends image; no pills shown"),
    dict(to=14, reason="time jump: three years of addiction, failure at school", chars=["riyadh_boy"], loc="school_yard",
         visual="the boy, now an older teenager about seventeen, thinner, with hollow tired eyes and dark circles, sitting alone on the concrete steps of an empty school courtyard, his school bag dropped at his feet, staring at nothing",
         camera="wide shot, slightly high angle", amb="city_day", transition="black", sens="drug addiction",
         safe="addiction shown only as a hollow-eyed, exhausted teenager alone at school"),
    dict(to=17, reason="time/scene change: a cold winter night, he takes his father's new car", chars=["riyadh_man"], loc="courtyard_night",
         visual="the young man, now about eighteen, in the cold courtyard at night with one hand on the door of the new white car, glancing back guiltily over his shoulder at the dark house, his breath faintly misting in the cold",
         camera="medium wide, eye level", amb="night_exterior"),
    dict(to=19, reason="scene change: the night on the road before dawn", loc="highway_fog",
         visual="a single car's headlights cutting through thick winter fog on an empty desert highway before dawn, seen from a distance, the red tail-lights fading into the grey mist, no people visible",
         camera="wide shot, low angle from the roadside", amb="desert_night", sens="drugs + car crash",
         safe="the drug dose and the drive are shown only as headlights in fog on an empty highway; no lorry, no crash"),
    dict(to=21, reason="time jump: he wakes in the ICU", chars=["riyadh_man"], loc="icu",
         visual="the young man lying still in a hospital bed in a dim ICU room, eyes half open, a white blanket up to his chest, his right leg in a clean white cast resting on top of the blanket, a heart monitor beside him whose screen shows only a single glowing green wave line with no numbers or characters, no wounds visible",
         camera="medium wide, slightly high angle", amb="hospital_night", transition="black", sens="injury / crash",
         safe="crash and injuries never shown; ICU monitor glow, a clean white cast, a calm covered patient"),
    dict(to=23, reason="symbolic detail: Allah's mercy, a new chance at life", loc="dawn_road",
         visual="a pure landscape: an empty desert highway at dawn stretching straight to the horizon, the first gold sunlight rising over the sand dunes, the road clean and quiet; nothing else in the frame — no vehicles, no people, no faces, no figures, no portraits or montage in the sky, just clear sky with soft clouds",
         camera="wide shot, eye level", amb="dawn_exterior", sens="crash under a lorry",
         safe="the lorry and the crash are never shown; only the empty road at dawn"),
    dict(to=27, reason="scene change: recovering at his father's house in Riyadh, the friends keep coming", chars=["riyadh_man"], loc="home_room",
         visual="the young man lying on a floor mattress with his leg in a clean white cast under a blanket, a pair of crutches leaning against the wall, two young men in thobes standing in the doorway seen only from behind as dark silhouettes against the corridor, their faces unseen",
         camera="medium wide from behind the silhouettes", amb="room_day", sens="drugs brought by friends",
         safe="the 'goods' are never shown; the friends are faceless silhouettes in the doorway"),
    dict(to=30, reason="action/scene change: on crutches he tries to stop cars at Asr", chars=["riyadh_man"], loc="roadside_asr",
         visual="the young man standing at the roadside on crutches in the late afternoon golden light, raising one hand towards passing cars that do not stop, his face tired and stubborn, long shadows on the pavement",
         camera="medium wide, eye level", amb="road_busy"),
    dict(to=31, reason="scene and character change: in his brother's town, enrolled at school", chars=["riyadh_man", "elder_brother"], loc="town_school",
         visual="the elder brother standing beside the young man at a school gate in the morning, a hand on his shoulder, encouraging him with a hopeful, worried look; the young man looking at the gate, uncertain",
         camera="medium two-shot", amb="city_day", transition="black"),
    dict(to=34, reason="action change: his secret life of selling and drinking", chars=["riyadh_man"], loc="car_night",
         visual="the young man sitting alone in the driver's seat of a parked car on a dark street at night, hollow eyes staring ahead, his face lit faintly by blurred amber streetlights through the windscreen, hands resting on the steering wheel",
         camera="close-up through the side window", amb="car_night", sens="alcohol + selling pills",
         safe="alcohol and dealing never shown; a lone hollow-eyed young man in a parked car at night"),
    dict(to=38, reason="scene change: at school like a fool, numb and fearful", chars=["riyadh_man"], loc="classroom",
         visual="the young man sitting at a desk at the back of a classroom with glazed, vacant eyes, his head propped on one hand, the other students in front of him only blurred shapes, a distant, numb expression",
         camera="medium shot, eye level", amb="room_day", sens="hashish",
         safe="hashish never shown; only his vacant, glazed look in class"),
    dict(to=41, reason="scene change: the lone house at the edge of town, two friends come for him", chars=["riyadh_man"], loc="edge_house",
         visual="a lone small house at the edge of town in late afternoon, a car waiting in the dusty lane with two young men in thobes standing beside it seen only from behind as dark silhouettes, the young man walking from the house towards them",
         camera="wide shot from behind the silhouettes", amb="city_day", sens="bad friends",
         safe="the friends are faceless silhouettes; the joyride is only implied"),
    dict(to=44, reason="he searches for hours, lost and intoxicated (reuse of the parked-car image)", reuse="beat_015", chars=["riyadh_man"], loc="car_night",
         visual="(reuse) the young man alone in his car at night", amb="car_night", sens="intoxication",
         safe="intoxication shown only as a lost young man alone in a car at night"),
    dict(to=48, reason="action change: chest pain inside the house, death seems to stand before him", chars=["riyadh_man"], loc="dark_room",
         visual="the young man in the dark bare room pressing his back against the wall, one hand clutching his chest, eyes wide with fear, staring at a tall formless dark shadow stretching across the opposite wall in front of him",
         camera="medium shot, low angle", amb="room_night", sens="near-death",
         safe="death shown only as a looming formless shadow on the wall and his frightened face"),
    dict(to=49, reason="action change: he rushes to make wudu", loc="washbasin",
         visual="close-up of a young man's hands cupped under a running tap at a simple white washbasin, clean water spilling over the fingers, the sleeves of an off-white thobe pushed back to the wrists, no face visible",
         camera="extreme close-up", amb="room_night", sens="bathroom",
         safe="only hands under a running tap at a washbasin"),
    dict(to=51, reason="action change: he stands in prayer", chars=["riyadh_man"], loc="prayer_room",
         visual="the young man standing in prayer on a prayer rug facing a plain wall, hands folded on his chest, head bowed, his face pale and trembling, a single dim lamp casting his shadow",
         camera="medium shot from a three-quarter angle behind", amb="room_night"),
    dict(to=55, reason="action change: he lies down on his right side, awaiting death", chars=["riyadh_man"], loc="prayer_room",
         visual="the young man lying on his right side on the prayer rug in the dim room, fully clothed in his thobe, eyes closed, beads of sweat on his brow, his hands drawn close, a single lamp glowing softly",
         camera="medium close-up at floor level", amb="room_night", sens="near-death",
         safe="no gore or distress shown: a still figure on a prayer rug, eyes closed, sweat on the brow"),
    dict(to=56, reason="detail image: his foot moves — hope", loc="prayer_room",
         visual="close-up of a young man's bare foot on a patterned prayer rug, toes just beginning to move, lit by a single warm shaft of light cutting through the darkness of the room",
         camera="extreme close-up at floor level", amb="room_night", sens="near-death",
         safe="the return of life shown only as a bare foot moving in a shaft of light"),
    dict(to=58, reason="scene and character change: he collapses among his brother's family at dinner", chars=["riyadh_man", "elder_brother", "nephew"], loc="brother_house",
         visual="the young man collapsed on the carpet at the edge of a dinner cloth, curled on his side with a hand on his chest; the elder brother half risen from his cushion, leaning over him in shock; the nephew rising behind him in alarm; dinner plates untouched",
         camera="medium wide, eye level", amb="living_night", sens="collapse",
         safe="no injury shown; he lies clothed on the carpet holding his chest"),
    dict(to=60, reason="scene change: the nephew drives him through the night", chars=["nephew", "riyadh_man"], loc="car_drive",
         visual="the nephew driving at night with a worried face, eyes on the road, while the young man sits hunched in the passenger seat, one hand on his chest, talking to him with shame",
         camera="medium two-shot from the back seat between them", amb="car_night"),
    dict(to=63, reason="scene and character change: the private clinic doctor", chars=["clinic_doctor", "riyadh_man", "nephew"], loc="clinic",
         visual="the stern doctor standing by the examination couch with a stethoscope, holding up one hand in refusal, his face grave; the young man lying on the couch in his thobe looking pale; the nephew standing beside the doctor with hands pressed together, pleading",
         camera="medium wide, eye level", amb="clinic_room", sens="alcohol level / police",
         safe="the alcohol test is never shown; only the doctor's stern refusal and the nephew pleading"),
    dict(to=66, reason="character change: his father comes and stands at his bedside", chars=["pious_father", "riyadh_man"], loc="clinic",
         visual="the old father standing silently at the head of the clinic couch, looking down at his son with deep grief, one hand pressed to his own chest, his face pained; the young man lying below, looking up at him with shame",
         camera="medium shot, slightly low angle from the couch", amb="clinic_room", sens="smell of alcohol",
         safe="the smell is conveyed only by the father's grieving, pained face"),
    dict(to=68, reason="time/scene change: leaving the clinic, a new life", chars=["riyadh_man"], loc="clinic_exit",
         visual="the young man stepping out of the clinic door into soft early morning gold light, pausing to breathe deeply, eyes closed, face lifted towards the light",
         camera="medium wide, eye level", amb="dawn_exterior", transition="black"),
    dict(to=71, reason="time/action change: at night he wakes trembling, as if called", chars=["riyadh_man"], loc="sleep_room",
         visual="the young man sitting bolt upright on his floor mattress in the dark, a blanket over his legs, trembling, eyes wide, looking up as if someone had just called him, pale moonlight from the small window falling across his face",
         camera="medium close-up", amb="room_night", sens="cigarette / hashish",
         safe="the smoke is never shown; his fear and awakening at night instead"),
    dict(to=72, reason="night prayer in the last part of the night (reuse of the prayer image)", reuse="beat_021", chars=["riyadh_man"], loc="prayer_room",
         visual="(reuse) the young man standing in prayer", amb="room_night"),
    dict(to=74, reason="time and character change: guarding his prayers; Allah sends a righteous young man", chars=["riyadh_man", "righteous_friend"], loc="town_mosque",
         visual="inside a simple mosque after prayer, the righteous young man sitting beside the young man on the carpet, one hand on his shoulder, smiling warmly; the young man listening with tearful, hopeful eyes",
         camera="medium two-shot, eye level", amb="mosque_interior"),
    dict(to=77, reason="scene change: umrah in Makkah, weeping at the Kaaba", chars=["riyadh_man"], loc="makkah",
         visual="two young men seen from behind, both BAREHEADED with short black hair (no headdress, no ghutra, no cap, nothing on their heads), both wrapped in plain white ihram cloth that fully covers both shoulders and the upper body, standing side by side on the marble courtyard; the young man on the left raising both hands in supplication with his head bowed, his companion on the right with a neat black beard standing quietly beside him; the Kaaba small and far away across the wide courtyard, surrounded by crowds of distant pilgrims in white",
         camera="wide shot from behind, respectful distance", amb="makkah_crowd", hum_note="emotional peak"),
    dict(to=79, reason="back to the mosque in Riyadh: his advice to the youth (reuse)", reuse="beat_002", chars=["riyadh_man"], loc="mosque",
         visual="(reuse) the young man telling his story in the mosque", amb="mosque_interior", transition="dissolve"),
    dict(to=81, reason="closing dua: symbolic image of mercy", loc="dua_sky",
         visual="a pair of raised open hands in supplication seen from behind against a dawn sky, a lone slender minaret silhouetted in the distance, rays of gold light breaking through thin clouds over the desert",
         camera="wide shot, low angle", amb="dawn_exterior"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "He is a young man who became the prey of bad friends. He spent many, many days in a world of intoxicants and misguidance.")
sh(2, "An incident in his life woke him from his heedlessness, and he returned to the path of his Lord.")
sh(3, "When I met him in a mosque in Riyadh, he told me his story, saying: I grew up in a very religious home in a district of Riyadh.")
sh(4, "My father (may Allah have mercy on him) was a very religious man. He would never allow any device of entertainment or corruption to be brought into the house.")
sh(5, "The days went by, and the age of innocent childhood passed. When I turned fourteen, I came across a group of bad friends.")
sh(6, "They were waiting for the most fitting chance to catch me in their net. And they got that chance.")
sh(7, "It was exam time. They brought me white pills that would help me stay awake.")
sh(8, "Without any trace of sleep, without even wanting to sleep, I stayed awake night after night studying my lessons.",
   [("page_turn", "ދަސްކުރުމުގައި", -22)])
sh(9, "When the exams ended I passed with very high marks. Even after the exams I kept on taking those white pills.")
sh(10, "Staying awake like that left me utterly exhausted. Then those friends came, and this time they gave me red pills.",
   [("sigh", "ވަރުބަލިވިއެވެ", -22)])
sh(11, "They said those would bring me sleep and rest. Being so young, I did not see the truth of this dangerous plan and the cunning of those devils among men.", hum=True)
sh(12, "I started taking about ten red pills every day. For about three years or more I stayed in this state.")
sh(13, "And I failed in my studies; I could not finish middle school and get the certificate.")
sh(14, "Hoping to get the certificate I kept moving from one school to another. But it was of no use.")
sh(15, "After the great failure these pills brought me, as a last effort to complete my studies, I decided to move to another town where my eldest brother and his children lived.")
sh(16, "It was a bitterly cold winter night. My father had just bought a new car.", [("wind_gust", "ފިނިގަދަ", -22)])
sh(17, "Without my father knowing, I took that car and set off for that town. In my pocket was a large number of red pills.",
   [("car_door", "ކާރު", -18)])
sh(18, "On the way I stopped with some friends. And that night I took those pills in an extreme amount.")
sh(19, "Those pills plunged me into a miserable, wretched state. A little before dawn I got into the car and set off.",
   [("car_drive_off", "ދަތުރު", -20)])
sh(20, "Within a few minutes the world went dark for me. When I came to, I was lying in hospital in a very bad state. My right leg was broken.",
   [("heartbeat", "ހޮސްޕިޓަލުގައެވެ", -20)], hum=True)
sh(21, "And there were many wounds on my body. For forty-eight hours I lay in the ICU. It was a very dangerous accident.")
sh(22, "My car had gone right under a big lorry. That Allah wrote life for me and gave me a new chance to turn back in repentance from the bad path I was on — that",
   [("brake_screech", "ލޮރީއެއްގެ", -20)])
sh(23, "was the mercy of Allah. But nothing came of it. Even that did not wake me from the sleep of heedlessness.", hum=True)
sh(24, "From the hospital I was moved to my father's house in Riyadh. Even lying at home I kept using those wretched pills.")
sh(25, "You may ask me how, lying on a sickbed, I got hold of those pills. I will tell you that too.")
sh(26, "Those friends would come to my house and offer me their goods. However bad my state was, I would buy from them.",
   [("door_open", "ގެއަށް", -22)])
sh(27, "More than anything I was hooked on those red pills. After some days in that state, I felt my condition improve a little.")
sh(28, "Even then, in my mind was the thought of travelling to my eldest brother's, hoping to complete my studies. One day it was the time of Asr.")
sh(29, "After taking a large number of those pills, I went out with the help of a crutch and began looking for a car that would go to that town.")
sh(30, "I tried to stop car after car. But no one stopped. Then I went to a taxi stand, hired a taxi and went there.",
   [("car_pass", "ކާރެއް", -20)])
sh(31, "I went to that town, and through the efforts of my eldest brother and others I got into a middle school. And I obtained the pass certificate.")
sh(32, "Even while I was studying I kept using intoxicants. But I stopped those red pills and started drinking alcohol.")
sh(33, "At the same time I kept promoting those red pills and selling them at double the price.")
sh(34, "I did not understand how evil and dangerous this was. My only aim was getting money — gathering cash.")
sh(35, "After that I started using hashish. And not just using it; I became hooked on it.")
sh(36, "I used it the way one smokes tobacco. I went to school like a fool.")
sh(37, "The people around me looked to me like flies or tiny insects. But I never harmed anyone.")
sh(38, "Because whoever uses these things becomes a timid, fearful coward. For about two years I stayed in this state.")
sh(39, "At that time I was living alone in an isolated house at one end of the town. One day two of the friends I knew came to me.")
sh(40, "So I parked my car and went with them in their car. By then the time of the Asr prayer had passed.",
   [("car_door", "ކާރުގައި", -18)])
sh(41, "We began driving around the streets of the town, as if no one could match us. After hours of driving, they dropped me beside my car.",
   [("car_pass", "ދުއްވަން", -20)])
sh(42, "I got into my car to go home. But I could not find my way to the house. By then I was utterly intoxicated.",
   [("car_door", "ކާރަށް", -18)])
sh(43, "For two hours or more I searched for the house. But I could not find it.")
sh(44, "After a very long search, at last I found my house. When I saw it I was overjoyed.")
sh(45, "As I was getting out of the car I felt a violent pain in my heart. With great difficulty I got out and went into the house.",
   [("heartbeat", "ތަދެއް", -16)], hum=True)
sh(46, "In those moments, for the first time in years, I remembered death. Yes! By Allah I tell you, O brothers!", hum=True)
sh(47, "Death came to me in the form of something standing before me, about to attack me.",
   [("heartbeat", "ޙަމަލާދޭން", -18)], hum=True)
sh(48, "And I saw astonishing things that I cannot describe now.", hum=True)
sh(49, "Without thinking I got up quickly, went into the washroom and made wudu. I came out, then went back again and made wudu a second time.",
   [("splash", "ވުޟޫކުރީމެވެ", -24)])
sh(50, "Then I hurried into a room, said the takbir and stood for prayer. As I remember, in the first rakat I recited al-Fatiha and 'Say: He is Allah, the One'.")
sh(51, "What I recited in the second rakat I do not remember. What mattered to me was finishing those two rakats before I died. And I dropped to the floor,",
   [("soft_thud", "ވެއްޓިގަނެ", -20)])
sh(52, "lay down on my left side and surrendered to death. In that moment I remembered hearing that it is best to lay a dying person on his right side,", hum=True)
sh(53, "so I turned onto my right side. My whole body felt as if it was shaking violently.",
   [("cloth_rustle", "އެނބުރުނީމެވެ", -22), ("heartbeat", "ތަޅުވައިގަންނަ", -18)], hum=True)
sh(54, "The pages of my life, full of misguidance and indecency, kept flashing one after another through my mind.", hum=True)
sh(55, "I was certain my soul was close to leaving. A moment passed, waiting for death.",
   [("breath", "އިންތިޒާރުގައި", -22)], hum=True)
sh(56, "Suddenly I moved my foot. My foot moved! I was overjoyed. And through that thick darkness I saw a light of hope.",
   [("gasp", "ޙަރަކާތްކޮށްލީމެވެ", -20)], hum=True)
sh(57, "I got up quickly, left the house, got into the car and set off for my eldest brother's house. When I knocked and went in, they were all gathered for dinner.",
   [("car_door", "ކާރަށް", -18), ("knock", "ކޮއްޕާލާފައި", -16)])
sh(58, "I went and collapsed in the middle of them. My eldest brother jumped up, startled, and asked: 'What happened?!' I said: 'My heart hurts terribly.'",
   [("soft_thud", "ވެއްޓިގަތީމެވެ", -18), ("gasp", "ސިހިފައި", -18)], hum=True)
sh(59, "Then one of my eldest brother's sons got up and took me to hospital. On the way I told him about my state, and how heavily I had been using intoxicants.",
   [("car_drive_off", "ގެންދިޔައެވެ", -20)])
sh(60, "And I asked him to take me to a doctor he knew. So he took me to a private clinic.")
sh(61, "The doctor examined me and concluded that my condition was very bad. The alcohol level in my body had risen to 94%.")
sh(62, "So the doctor refused to treat me. And he said the police would have to be called. But after pleading again and again,")
sh(63, "and offering money, he agreed to treat me. Then they did an ECG and began treatment.")
sh(64, "My father too was in that town at the time. When he learned I was in hospital, he came to visit me.",
   [("footsteps_pavement", "އައެވެ", -22)])
sh(65, "I saw my father standing at the head of my bed. The smell that came off my body made my father's chest tighten.", hum=True)
sh(66, "Then, without saying a single word, my father walked out. I spent a night under treatment. Before I left the hospital, the doctor advised me to keep away from intoxicants.",
   [("footsteps_pavement", "ނުކުމެގެން", -22)], hum=True)
sh(67, "And he told me my condition was very bad. When I left the hospital, I felt I had been given a new life.")
sh(68, "Allah willed good for me. After that, every time I caught the smell of hashish, I remembered what happened to me that night, and I remembered death.")
sh(69, "And I would put out the cigarette. Every night when I slept, I felt as if someone was calling me, saying 'Get up!'")
sh(70, "I would wake up trembling with fear. And I would remember death, and paradise, and hell, and the grave.",
   [("gasp", "ހޭލެވެއެވެ", -20)], hum=True)
sh(71, "Likewise I remembered two of my bad friends who had died a short while before.")
sh(72, "I was afraid my end would be like theirs. So in the last part of the night I would get up and pray two rakats.")
sh(73, "Then I began to guard the obligatory prayers. Every time I smelled hashish or smoke, I remembered death and left it.")
sh(74, "For four months or more I stayed in this state. At last Allah decreed for me a righteous young man.")
sh(75, "He rescued me from those bad people and took me to Makkah to perform umrah. Praise be to Allah. On that journey I wept a great deal.",
   [("sob_breath", "ރުއީމެވެ", -22)], hum=True)
sh(76, "On the holy land of Makkah, at that holy House, I begged Allah to accept a repentance that would wipe away all my sins.", hum=True)
sh(77, "I repented to Allah and returned to His path. My advice to Muslim youth is:")
sh(78, "be careful and beware of bad friends. For many years they were the cause of my grief and misfortune.")
sh(79, "Had Allah, by His kindness and mercy, not saved me from their hands, I would have been among the lost.")
sh(80, "I pray in the presence of Allah that He accept the repentance of me and of all sinners and wrongdoers.", hum=True)
sh(81, "Truly He is the Oft-Returning, the Most Merciful. The end.", hum=True)
SHOTS = S

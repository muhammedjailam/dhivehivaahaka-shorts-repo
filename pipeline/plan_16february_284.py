"""Beat/shot plan for 16 February episode 284 (used by plan_beats.py).
The red file, Ahlam's arrival, Malak's faint, Kaif at the site a week later, his rejected confession, Ahlam alone at
midnight. Bible rules: no blood (the handkerchief is a dark cloth), no body/outline (police tape), nobody lying down,
Rishwan never carries Malak on screen, no touch between Malak and any man, hijab on every woman, no readable text."""

RESORT_OFFICE = ("an open-plan back-office of the resort, rows of wooden desks with monitors, glass-walled cabins, large "
                 "windows to palms and sea; the boss's cabin with a dark wooden desk and a leather chair")
BUILDING_SITE = ("a cluster of three-storey half-built concrete guesthouses, bare columns and empty window holes, rusty "
                 "rebar, overgrown with weeds, at the edge of the island near the trees")
NIGHT_ROAD = "a long dark sandy island road lined with tall trees and scattered dim street lamps"
STAFF_ROOM = ("a small plain resort staff room: cream walls, a grey fabric couch with cushions, a low side table, a "
              "simple wall-mounted telephone by the door, a window with white blinds and palm leaves outside, a small "
              "metal IV stand in the corner")

LOC = {
    "office": RESORT_OFFICE,
    "office_door": f"the entrance area of {RESORT_OFFICE}, a glass door standing open, a desk with its chair pushed back",
    "staff_room": STAFF_ROOM,
    "site": f"{BUILDING_SITE}; plain blue-and-white striped police tape with no writing strung between the bare columns around the base",
    "site_road": f"the edge of {NIGHT_ROAD} beside {BUILDING_SITE}, a bare concrete staircase rising inside the dark shell",
    "site_ground": f"the weedy sandy ground beside {BUILDING_SITE}, near the trees",
    "kaif_room": "Kaif's plain small bedroom: whitewashed walls, a single bed with a simple wooden headboard and a grey sheet, a white pillow, a small wooden side table, a window streaked with rain",
    "beach_memory": "a quiet island beach with white sand, leaning coconut palms and calm turquoise water",
    "beach_dusk_memory": "a quiet island beach at dusk, white sand, leaning coconut palms, the lagoon reflecting an orange sky",
    "office_night": f"{RESORT_OFFICE}, empty late at night, rows of dark monitors, rain lashing the large windows",
}
MOOD = {
    "office": "bright tropical late morning, slightly desaturated turquoise-and-sand daylight through the large windows, cool air-conditioned office light, tense stillness",
    "office_door": "bright tropical late morning, slightly desaturated daylight through the glass door, quiet and strangely empty",
    "staff_room": "daytime, soft diffused daylight through white blinds, calm muted colours, quiet worry",
    "site": "overcast grey afternoon more than a week after the storm, damp sand, muted colours, heavy and unresolved",
    "site_road": "overcast grey afternoon, cold shadow inside the unfinished building, a sudden prickle of unease",
    "site_ground": "overcast grey afternoon, a thin shaft of pale light catching something small and shiny, hushed suspense",
    "kaif_room": "rainy night, the room dark except the cold blue glow of a phone screen, rain streaks on the window, sleepless loneliness",
    "beach_memory": "warm golden afternoon, hazy, slightly desaturated memory with soft vignette, carefree friendship",
    "beach_dusk_memory": "dusk, orange and violet sky, hazy, slightly desaturated memory with soft vignette, hope turning to hurt",
    "office_night": "office after midnight in a storm, only one warm desk lamp in a glass cabin, blue-black shadows, lightning flickering at the windows, eerie silence",
}

BEATS = [
    # --- the red file, resort office, day ---
    dict(to=3, reason="episode opening: Malak opens the red file and recoils in terror", chars=["malak"], loc="office",
         visual="Malak standing behind her wooden desk, recoiling a step back with wide terrified eyes and her own hand pressed over her mouth, staring down at a plain blank red folder lying open on the desk with a crumpled dark cloth inside, seen from a distance; her chair pushed back; glass cabins and bright windows behind her",
         camera="medium wide, eye level, her face in the upper third, the desk top as the calm lower third", amb="office_day",
         sens="other", safe="rule 5: the blood-soaked handkerchief is shown only as a crumpled dark cloth in an open red folder seen from a distance; no red stains, no blood"),
    dict(to=6, reason="character change: a young man (Ahlam) enters just as the file lands at his feet", chars=["ahlam"], loc="office_door",
         visual="Ahlam just inside the open glass door, crouching on one knee to pick up a plain blank red folder from the floor, a few blank white sheets scattered around his shoes, looking up and around the seemingly empty office with a puzzled half-smile; in the background a desk with its chair pushed back and nobody visible",
         camera="medium wide, low eye level, his face in the upper half, the tiled floor with blank sheets as the lower third", amb="office_day",
         sens="other", safe="rule 7: Malak's faint is not shown — only the empty desk with the chair pushed back"),
    dict(to=10, reason="character change: Ali the secretary enters; Ahlam hands him the file with a joke", chars=["ahlam", "ali"], loc="office",
         visual="Ahlam, standing tall and relaxed with a playful grin, holding out a plain blank red folder to Ali; Ali facing him with his tablet clutched to his chest, eyebrows raised behind his glasses, startled and unsure; a row of desks and glass cabins behind them",
         camera="medium two-shot, eye level, faces in the upper third", amb="office_day"),
    dict(to=16, reason="action change: Ahlam strolls further in, teasing; Ali flustered with excuses", chars=["ahlam", "ali"], loc="office",
         visual="Ahlam walking past the desks deeper into the office, glancing back over his shoulder with an amused teasing smile; Ali a few steps behind holding the red folder and his tablet, awkward and flustered, mouth half open mid-excuse",
         camera="medium wide, eye level, slightly from the side", amb="office_day"),
    dict(to=18, reason="focus change: Ali alone with the red file, embarrassed he missed Ahlam at the jetty", chars=["ali"], loc="office",
         visual="Ali standing alone in the office aisle, looking down thoughtfully at the closed plain red folder in his hand, then glancing ahead; his face embarrassed and uneasy behind his glasses; in the soft background the blurred figure of a bearded man in black walking away toward the glass cabins",
         camera="medium close-up, eye level", amb="office_day"),
    dict(to=25, reason="narrator's character portrait of Ahlam: new framing on his face (reflective hold, 68 s)", chars=["ahlam"], loc="office",
         visual="Ahlam standing by the large office window, sea and palms bright behind the glass, one hand in his pocket, his face calm and serious with a faint warm smile and intelligent, determined eyes looking out across the office",
         camera="medium close-up portrait, eye level, slightly low angle, his face in the upper third", amb="office_day"),
    # --- Malak found ---
    dict(to=27, reason="character change: Mizoo finds Malak collapsed behind her desk", chars=["mizoo"], loc="office",
         visual="Mizoo bending over beside Malak's desk with a shocked face, one hand at her cheek, having just set a water bottle on the desk; she is looking down behind the desk at the floor out of view; the desk chair pushed back and a plain red folder lying on the floor",
         camera="medium shot, eye level, her face in the upper third", amb="office_day",
         sens="other", safe="rule 7: Malak lying collapsed is not shown — only Mizoo's shocked reaction, the chair pushed back and the fallen red folder"),
    dict(to=31, reason="characters change: Rishwan rushes in and Ali scolds the gathering staff", chars=["ali", "mizoo"], loc="office",
         visual="Ali standing in the office aisle frowning, one hand raised and the tablet in the other, mid-scolding; Mizoo beside the desk turning to him and pointing anxiously down behind the desk; a young male staff member in a sand-beige staff shirt hurrying up from the side; nobody lying visible",
         camera="medium wide, eye level, faces in the upper half", amb="office_day"),
    # --- staff room ---
    dict(to=34, reason="scene change: the staff room; Ali phones Zuhoo, Mizoo covers Malak", chars=["malak", "ali", "mizoo"], loc="staff_room",
         visual="Malak sitting propped up in the corner of a grey couch, unconscious with her eyes closed and her head resting against a cushion, a light blanket over her knees; Mizoo spreading the blanket; Ali by the door holding the wall telephone receiver to his ear, looking back worriedly",
         camera="medium wide, eye level, faces in the upper half, the floor as the lower third", amb="staff_room",
         sens="other", safe="rule 3/7: Rishwan carrying her and laying her on a bed are not shown; Malak sits propped up on a couch, nobody lying down"),
    dict(to=37, reason="character change: Zuhoo the medic arrives and checks Malak", chars=["zuhoo", "malak", "mizoo"], loc="staff_room",
         visual="Zuhoo kneeling beside the couch, two fingers on Malak's wrist checking her pulse and looking at her face with calm professional concern; Malak sitting propped up with eyes closed; Mizoo standing behind with hands clasped, shrugging as she answers",
         camera="medium shot, eye level, faces in the upper half", amb="staff_room"),
    dict(to=39, reason="action change: Malak wakes with a headache and sees the IV", chars=["malak"], loc="staff_room",
         visual="Malak sitting up on the couch, one hand holding her head under her black hijab edge, wincing, pale and dazed, glancing toward a small metal IV stand standing beside the couch in the background; daylight through the blinds",
         camera="medium close-up, eye level", amb="staff_room",
         sens="other", safe="rule 7: no needle shown, only a small IV stand in the background; no visible injury"),
    dict(to=43, reason="character change: Mizoo sits by her; Malak tells of the bloody handkerchief", chars=["malak", "mizoo"], loc="staff_room",
         visual="Mizoo sitting on the edge of the couch, leaning in with a puzzled frown; Malak sitting up, pale and frightened, speaking urgently with wide eyes, hugging her arms against a chill",
         camera="medium two-shot, eye level, faces in the upper third", amb="staff_room"),
    dict(to=48, reason="action change: Mizoo makes her rest and teases her about Ali and the new boss", chars=["mizoo", "malak"], loc="staff_room",
         visual="Mizoo laughing, holding a glass of juice on the side table, chatting playfully; Malak sitting back against the cushions of the couch with her eyes closed and a tired wry expression, a light blanket over her knees",
         camera="medium shot, eye level, the side table top as the lower third", amb="staff_room"),
    dict(to=51, reason="emotional turn: Malak, haunted by the handkerchief, ignores Mizoo who leaves", chars=["malak", "mizoo"], loc="staff_room",
         visual="Malak sitting on the couch staring into empty space with haunted fearful eyes; in the soft background Mizoo at the open door looking back, asking; Malak lifts a hand slightly to wave her off",
         camera="close-up on Malak in the foreground, Mizoo small in the background, face in the upper third", amb="staff_room", hum=True),
    # --- Kaif at the site a week later ---
    dict(to=55, reason="scene and time change: Kaif and his team at the death site more than a week later", chars=["kaif"], loc="site",
         visual="Kaif in uniform standing in front of the taped-off half-built building, his cap in his hand, scanning the bare concrete with a worried questioning frown; two police officers in dark-navy uniforms searching the weedy ground behind him",
         camera="medium wide, eye level, the building in the upper half, the sandy ground as the lower third", amb="island_day",
         transition="black", sens="violence", safe="rule 2: the body outline is replaced by plain police tape around the building base; no body, no blood"),
    dict(to=58, reason="character change: the young officer who blacked out that night reports to Kaif", chars=["kaif"], loc="site",
         visual="Kaif facing a young police officer in a dark-navy uniform who stands stiffly, embarrassed and unsure, gesturing toward the trees; Kaif stern and impatient, raising a hand to dismiss him",
         camera="medium two-shot, eye level, faces in the upper third", amb="island_day"),
    dict(to=61, reason="action change: a sound of someone running to the stairs; Kaif turns", chars=["kaif"], loc="site_road",
         visual="Kaif standing on the sandy road outside the unfinished building, turning sharply back toward an empty bare concrete staircase in the dark shell, alert, his cap in hand; no one on the stairs",
         camera="medium wide from behind and to the side of Kaif, the staircase in the upper half", amb="island_day"),
    dict(to=64, reason="discovery: Kaif finds a glinting earring where Malak ran that night", chars=["kaif"], loc="site_ground",
         visual="Kaif crouching on the weedy sand, holding up a small silver drop earring between his fingers on a white tissue, studying it with shocked recognition, his face close to it",
         camera="close-up, eye level, his face and the earring in the upper half, the sandy ground as the lower third", amb="island_day", hum=True),
    # --- Kaif's room at night ---
    dict(to=69, reason="scene and time change: Kaif sleepless at night, messages Malak, no reply", chars=["kaif"], loc="kaif_room",
         visual="Kaif OFF DUTY at home: bareheaded with NO cap at all (his short black hair visible), wearing a plain dark-grey t-shirt and grey track trousers instead of the police uniform (ignore the uniform and cap of his reference image, use it only for his face), sitting up in bed with his back against the headboard and a pillow on his lap, holding his phone, its cold glow on his sad tired face, head tilted back; the phone screen faces away",
         camera="medium shot, eye level, his face in the upper third, the grey sheet as the lower third", amb="apartment_rain_night",
         transition="black"),
    # --- flashback: friendship and confession ---
    dict(to=71, reason="flashback: Kaif and Malak's inseparable friendship", chars=["malak"], loc="beach_memory",
         visual="a few years younger: a lean young Maldivian man of about 24 (young Kaif) with warm brown skin, a lean face, dark watchful eyes, short black hair uncovered, a thin moustache and light stubble, bareheaded with NO cap, wearing a casual long-sleeved light-blue button shirt and dark jeans, NOT a police uniform and Malak walking side by side along the beach with a clear gap between them, both laughing, sharing a joke",
         camera="medium wide, eye level, faces in the upper third, the wet sand as the lower third", amb="memory",
         transition="dissolve", sens="intimacy", safe="rule 10: step-siblings at a respectful distance, no touch"),
    dict(to=74, reason="flashback turn: Kaif confesses his love at dusk", chars=["malak"], loc="beach_dusk_memory",
         visual="a lean young Maldivian man of about 24 (young Kaif) with warm brown skin, a lean face, dark watchful eyes, short black hair uncovered, a thin moustache and light stubble, bareheaded with NO cap, wearing a casual long-sleeved light-blue button shirt and dark jeans, NOT a police uniform standing on the beach at dusk, speaking earnestly with hopeful nervous eyes, hands at his sides; Malak standing apart from him, listening, her smile fading",
         camera="medium two-shot, eye level, two people standing apart", amb="memory",
         sens="intimacy", safe="rule 10: the confession is two young people standing apart, no touch"),
    dict(to=76, reason="emotional turning point: Malak refuses him", chars=["malak"], loc="beach_dusk_memory",
         visual="Malak turned away from Kaif, her face displeased and hurt; behind her, a few steps apart, a lean young Maldivian man of about 24 (young Kaif) with warm brown skin, a lean face, dark watchful eyes, short black hair uncovered, a thin moustache and light stubble, bareheaded with NO cap, wearing a casual long-sleeved light-blue button shirt and dark jeans, NOT a police uniform, standing frozen, crestfallen",
         camera="medium shot, Malak in the foreground, Kaif in soft focus behind", amb="memory", hum=True),
    dict(to=80, reason="flashback: the friendship breaks; Kaif alone as she drifts away", chars=[], loc="beach_dusk_memory",
         visual="a lean young Maldivian man of about 24 (young Kaif) with warm brown skin, a lean face, dark watchful eyes, short black hair uncovered, a thin moustache and light stubble, bareheaded with NO cap, wearing a casual long-sleeved light-blue button shirt and dark jeans, NOT a police uniform, standing alone on the darkening beach, shoulders slumped, watching a small distant figure of a young woman in a maroon kurta and black hijab walking away along the shoreline",
         camera="wide, Kaif seen from behind and to the side, the long beach and sky in the upper two-thirds", amb="memory"),
    dict(to=82, reason="return to the present: Kaif with her photo, lightning and thunder", chars=["kaif"], loc="kaif_room",
         visual="Kaif OFF DUTY at home: bareheaded with NO cap at all (his short black hair visible), wearing a plain dark-grey t-shirt instead of the police uniform (ignore the uniform and cap of his reference image, use it only for his face), sitting up in bed, eyes closed with a tear on his cheek, pressing his phone against his chest; a white lightning flash lighting the rain-streaked window behind him",
         camera="close-up, eye level, his face in the upper third", amb="apartment_rain_night",
         transition="dissolve", hum=True),
    # --- Ahlam alone after midnight ---
    dict(to=85, reason="scene and time change: Ahlam alone in the office after midnight in the storm", chars=["ahlam"], loc="office_night",
         visual="Ahlam alone at his dark wooden desk in the glass cabin, absorbed in papers and a laptop whose screen faces away, a single warm desk lamp lighting his face; beyond the glass the dark empty open office and rain on the windows",
         camera="medium wide, eye level, through the glass cabin wall", amb="office_storm_night",
         transition="black"),
    dict(to=87, reason="action change: he leaves his cabin and stops, listening to a strange sound", chars=["ahlam"], loc="office_night",
         visual="Ahlam standing in the dark aisle between the desks just outside his lit cabin, one hand at his trouser pocket, frozen mid-step, frowning and listening, head turned slightly",
         camera="medium wide, eye level", amb="office_storm_night"),
    dict(to=89, reason="cliffhanger: warm breath on his shoulder, he spins round into a blinding flash", chars=["ahlam"], loc="office_night",
         visual="Ahlam spinning round, startled, his face lit by a sudden blinding white flash of light from behind, eyes squinting and wide; nobody else visible",
         camera="close-up, eye level, his face in the upper third", amb="office_storm_night", hum=True,
         sens="other", safe="rule 12: no figure shown — only Ahlam startled and lit by a sudden white flash"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Malak's whole body seemed to freeze. Inside the file lay a handkerchief smeared with fresh blood! The handkerchief still showed the wetness of the blood.",
   [("gasp", "ގަނޑުވި", -18)], hum=True)
sh(2, "At the same moment a foul smell spread through the whole place. Wide-eyed, she grabbed the file and flung it aside. She was stunned with fear.")
sh(3, "Her heartbeat raced and her breath grew short. She tried to scream, but no sound came out of her throat.",
   [("heartbeat", "ވިންދު", -18)])
sh(4, "The file Malak had flung landed right at the feet of a young man who at that moment suddenly opened the door and walked in.",
   [("soft_thud", "ވެއްޓުނީ", -18), ("door_open", "ހުޅުވާލާފައި", -20)])
sh(5, "The young man slowly bent down and picked up the file lying on the floor. Gathering the papers that had flown out of it, he looked around the office.",
   [("paper_shuffle", "ކަރުދާސްތައް", -20)])
sh(6, "He could not see anyone in the office. When someone came in, the young man turned round to look.",
   [("footsteps_pavement", "ވަނުމުން", -22)])
sh(7, "There stood the office secretary Ali, holding his iPad against his chest. He handed Ali the file he had picked up from the floor. \"Here.")
sh(8, "I thought that when I arrived I'd be welcomed with a bit more fanfare. That rose petals would fly as I walked down a red carpet — but in this office it's files that fly.\"")
sh(9, "the young man said in a joking tone. At his tone Ali stood bewildered, not sure who this young man in front of him was. \"Ahlam.")
sh(10, "When did you arrive?\" Ali said, taking hold of the file. There was unease in his voice. He had expected that the person coming would be a manager sent by Waleed.")
sh(11, "The young man smiled. Had they not mentioned he was coming? he wondered. \"Didn't you know I was coming? Didn't Grandpa tell you?\"")
sh(12, "the young man asked as he started walking inside. Ali closed his eyes in dismay. This was Ahlam, the grandson of the resort's owner.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -22)])
sh(13, "\"He did tell me, but what he said wasn't that Ahlam would arrive — it was a new GM.\" Before Ali could finish, Ahlam started speaking.")
sh(14, "\"A GM will come, but right now I'm the one here. What's the matter, does Ali not like it that I came?")
sh(15, "You were expecting the GM to be a woman, weren't you?\" Ahlam asked in a teasing tone. \"No. I've never had such a thought.")
sh(16, "It's just that, since you hadn't mentioned you'd be arriving today, I...\" Ali fumbled for an excuse. Ahlam began to laugh, and walked further inside.")
sh(17, "Ali glanced thoughtfully at the red file in his hand. Then he looked at Ahlam walking ahead. He felt ashamed that he hadn't been able to go to the jetty to receive Ahlam.")
sh(18, "He was not a careless man. But today, on Ahlam's very first day, what Ahlam had seen was Ali's carelessness.")
sh(19, "As far as he knew, Ahlam was a responsible young man who kept firm principles in his work.")
sh(20, "In formal moments his face showed deep thought and seriousness. But whenever he met friends who wished him well,")
sh(21, "that face lit up with an incomparable smile. The warmth and the playful, joking nature he showed when talking with friends was a quality that won everyone's heart.")
sh(22, "Yet behind that playful nature was a very sharp, keen mind.")
sh(23, "Ahlam, who put justice and respect first in everything, was a kind-hearted person, quick to understand other people's feelings.")
sh(24, "The gentleness and courtesy in the way he spoke were precious qualities that showed the completeness of his character even more.")
sh(25, "With the courage to face every challenge visible in those eyes, there was no doubt at all that he was a strong-willed person who would never shrink from life's hardships.")
sh(26, "Ali took a deep breath and followed after Ahlam. \"Ya Rabbee.\" Mizoo cried out in alarm.",
   [("sigh", "ފުންނޭވާއެއް", -22), ("gasp", "ޔާރައްބީ", -18)])
sh(27, "Setting the water bottle in her hand down on the desk, Mizoo tried to lift Malak, who was lying fallen beside the chair. \"Rishwan!\"",
   [("cup_clatter", "ބެހެއްތުމަށްފަހު", -22)])
sh(28, "Mizoo called out rather loudly. Just then Rishwan was coming in. \"What happened?\" Rishwan asked, hurrying over and stopping short.",
   [("footsteps_pavement", "ހަލުވިކޮށް", -22)])
sh(29, "\"I came to ask her something and found her lying here collapsed,\" Mizoo said. \"What are you all doing crowding in here? The boss is around.")
sh(30, "Everyone, get back to work,\" Ali said, stopping. \"Malak has collapsed,\" Mizoo said. \"Malak collapsed?\"")
sh(31, "Ali was astonished. \"Don't stand there staring at my face — pick Malak up,\" Ali said. Rishwan lifted Malak and set off behind Ali.")
sh(32, "Ali headed toward the staff rooms. There he opened a room and went inside.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -20)])
sh(33, "Ali went to the phone in the room and dialled a number. \"Zuhoo.\" When the other end picked up, Ali told her to come to the room and put the phone down.")
sh(34, "Rishwan laid Malak down. Mizoo spread a sheet over Malak. \"Mizoo, stay here with Malak. Rishwan, go to the boss.\"",
   [("cloth_rustle", "ފޮތިގަނޑު", -22)])
sh(35, "Ali said. When Rishwan left the room, Ali left too. Before long Zuhoo came in. \"What happened?\"",
   [("door_close", "ނިކުތުމުން", -22), ("door_open", "ވަނެވެ", -22)])
sh(36, "Zuhoo asked. \"We found her collapsed.\" Zuhoo took Malak's wrist and checked her pulse. Then she checked her eyes as well.")
sh(37, "\"Why bring her here instead of to the clinic?\" Zuhoo asked. \"Ali,\" Mizoo said. \"Hmm.\" Knowing Ali's ways, she just made a sound.")
sh(38, "Malak managed to open her eyes. Her head ached as if it were splitting. Her hand hurt as well.",
   [("breath", "ހުޅުވާލެވުނެވެ", -22)])
sh(39, "Slowly she sat up and held her head. Then she noticed the IV attached to her. At that moment Mizoo came in from outside. \"Alhamdulillah. You OK?\"",
   [("door_open", "ވަނެވެ", -22)])
sh(40, "Mizoo asked, sitting down at the edge of the couch. \"Where am I?\" Malak said in a hoarse voice. \"In a room. Ali had us bring you here. What happened?")
sh(41, "Zuhoo says it happened because you went too long without eating,\" Mizoo said. \"Where's that file? Inside it was a handkerchief soaked in blood.")
sh(42, "Is that the kind of prank anyone should play?\" Malak said anxiously. She was still frightened. A chill crept over her body and she felt as if she had frozen.",
   hum=True)
sh(43, "She knew she had flung the file aside. After that she didn't know what happened. \"A file? A handkerchief?\" Mizoo asked, having no idea what she meant.")
sh(44, "Malak was still sitting there, weak. \"Don't talk so much — lie back and rest. Ali has given you the day off. Lucky Ali thought of it.\"")
sh(45, "Mizoo said. Malak leaned back again. \"You should eat something. Ali has sent juice and things. Telling everyone you fell ill at the office.\"")
sh(46, "Mizoo said, laughing. \"Ill, my foot. I was thinking the boss would turn up soon, and then we'd all get to see Ali's antics.\"")
sh(47, "Malak said, closing her eyes. \"Whatever antics he pulls, he's very loyal, you know. And he's so good to you. Hmm. The boss has arrived.")
sh(48, "But this time it isn't the old man — it's his grandson. A really smart lad. Even I saw, when I went to fetch your bag — Rishwan's trailing at his heels like a tail.\"")
sh(49, "Mizoo said, laughing. Malak paid no attention to what Mizoo was saying. Before her eyes she still kept seeing the handkerchief in that file.")
sh(50, "Whose prank could that be? \"Get some rest, I'm off. What shall I bring you to eat?\" Mizoo asked.")
sh(51, "Malak signalled with her hand that she didn't want anything. When Mizoo had gone, Malak closed her eyes.",
   [("door_close", "ދިއުމުން", -22)])
sh(52, "Her health had suddenly worsened only after seeing that handkerchief. ... The spot where the man who fell from above and died had lain was marked out.")
sh(53, "Kaif and his team were going over the area. As he looked at the things there with a questioning gaze, worry showed on his face.")
sh(54, "More than a week had passed. Still no one knew what had happened there. What could have happened here that night, enough for that man to die?")
sh(55, "Through whose negligence? How would Kaif find answers to the questions turning in his mind?")
sh(56, "Taking a deep breath, he shook his head. Just then a young policeman came and stopped before him. \"Where had you been? What happened that night?\"",
   [("sigh", "ފުންނެވާއެއް", -22)])
sh(57, "Kaif asked in a harsh tone. \"I don't know what happened either. When I came to, I was lying in the woods.\" The young man told him what had happened to him.")
sh(58, "Kaif had no time to weigh the truth of what he was saying. With a wave of his hand he signalled him to go.")
sh(59, "After a deep breath, Kaif moved on again and began checking the place. He stepped out onto the road and looked at the spot where the man had fallen.",
   [("sigh", "ފުންނޭވާއެއް", -22)])
sh(60, "At that moment, at the sound of someone running toward the stairs, Kaif turned round. He asked who was there. No answer came.",
   [("footsteps_pavement", "ދުވެފައި", -18), ("heartbeat", "ޖަވާބެއް", -20)])
sh(61, "His team was still busy at work. He let his gaze wander a little further off. Walking slowly, Kaif found himself heading the way Malak had gone that night.",
   [("footsteps_sand", "ހިނގާލާފައި", -22)])
sh(62, "Kaif spotted something glinting on the ground. He crouched down and picked it up. And he went on looking at it with curiosity.")
sh(63, "He took a tissue from his pocket and wiped it clean. Again he held it up and kept looking at it. Astonishment showed on his face. It was an earring.",
   hum=True)
sh(64, "Could he mistake it? He closed his fist tight around the earring. \"One piece of evidence from what happened on 16 February.\"",
   hum=True)
sh(65, "Kaif said quietly. He lay down in bed to sleep. But before his eyes he kept seeing the earring he had found today.")
sh(66, "Was that the answer to the question turning in his heart and mind? Restless, he got up from the bed.")
sh(67, "He leaned against the headboard, taking the pillow beside him and putting it on his lap. Sleep had well and truly turned its back on him. He picked up his phone.")
sh(68, "After sitting and thinking for a while, he typed a message. He sent it and sat waiting for a reply. Even though the message was read, no reply came.",
   [("phone_buzz", "ފޮނުވާލާފައި", -22)])
sh(69, "With a deep sigh Kaif let his head fall back against the headboard. The thought of how far Malak had drifted from him made his heart ache. Why had it changed?",
   [("sigh", "ފުންނޭވާއެއް", -20)])
sh(70, "Theirs was a bond so strong that neither could go without seeing the other. Through every joy and sorrow they gave each other strength,")
sh(71, "sharing everything in life in a friendship so strong it seemed it could never break.")
sh(72, "But as the days passed, Kaif's feelings toward Malak began to change. That it was not just friendship,")
sh(73, "but a far deeper love — Kaif began to feel it. Kaif told her what was in his heart. The love he had kept secret for so many days")
sh(74, "he revealed before Malak in the sweet hope that he would get the same answer from her. But things did not go the way Kaif had imagined.")
sh(75, "Hearing what Kaif said, displeasure and disappointment showed on Malak's face. Malak objected at once. \"Kaif!",
   hum=True)
sh(76, "I have never seen you that way. Because of this proposal, this precious friendship of ours will be lost.\" Malak said, deeply upset.")
sh(77, "After that day everything changed. Kaif's heart broke into pieces. He blamed himself for having confessed his love.",
   hum=True)
sh(78, "More than not being loved back, what hurt him was seeing the closest friend, dearer to him than his own life, slip out of his life and drift away.")
sh(79, "However hard Kaif tried to break down the wall that had risen, the emptiness and distance between them only grew day by day.")
sh(80, "Sometimes, in trying to reach the things you want most, even the most precious thing in your hand can slip away — Kaif realised it only far too late.")
sh(81, "Kaif picked up his phone again. He went to his photos and looked at Malak's photo. Tears welled in his eyes.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(82, "At that moment, with a flash of lightning, thunder rang out. Kaif pressed the phone to his chest and closed both eyes. It was a cold and very dark night, the sky wrapped in rain clouds.",
   [("thunder", "ގުގުރީގެ", -14)])
sh(83, "All the other office staff had gone home. Ahlam came into the office, sat down at his desk and settled in.",
   [("door_open", "ވަދެ", -22)])
sh(84, "A frightening silence had taken over the whole office. All that could be heard was the loud thunder crashing outside.",
   [("thunder", "ގުގުރީގެ", -14)])
sh(85, "He had gone to his room and showered, then remembered something and come back to the office. Lost in his work, he had no sense that someone else was in that office.",
   [("keyboard_typing", "މަސައްކަތަށް", -24)])
sh(86, "After twelve, Ahlam came out of his cabin. Putting a hand in his pocket to read the messages on his phone, he set off to leave.",
   [("footsteps_pavement", "ނިކުތެވެ", -22)])
sh(87, "At that moment his steps stopped. He listened to a sound he could hear. He frowned, not knowing what sound it was.",
   [("creak", "އަޑަށެވެ", -20)])
sh(88, "Before he could dive into the depths of thought, he flinched at the feeling of a warm breath falling on his shoulder from behind.",
   [("breath_heavy", "ނޭވާގެ", -18)], hum=True)
sh(89, "Startled, he spun round. In that instant a light flared into his eyes so that nothing could be made out.",
   [("gasp", "އެނބުރިލިއެވެ", -18), ("thunder", "އަލިވެގެން", -16)], hum=True)
SHOTS = S

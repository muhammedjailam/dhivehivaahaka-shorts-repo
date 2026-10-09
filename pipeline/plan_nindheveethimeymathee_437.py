"""Beat/shot plan for Nindheveethimeymathee episode 437 (used by plan_beats.py).
SCHOOL timeline. Beach confession (no touching), the sticky-note exam scandal, the principal's office with Haizum,
a silent dinner, the old photo album, Sana's recording (silence only, no music) and Sana's box and letter.
Lail and Saba never touch (bible rule 2); old photos of teen Haizum and Sana are small blurred framed photos."""

PENT = "Haizum's spacious modern penthouse in Malé, Maldives"
SCHOOL = "a modern secondary school in Malé, Maldives"
LOC = {
    "beach": "the artificial beach on the edge of Malé, Maldives: pale sand, a low coral-stone and concrete seawall edge, a calm turquoise lagoon, a few young palms, the city skyline softly in the distance",
    "beach_walk": "the long seafront promenade and shoreline of Malé, Maldives, stretching west towards the Maafannu side: a low seawall, pale sand, a calm sea, palms and city buildings in the distance",
    "study_home": "the living room of a Malé apartment set up for an evening revision session: a low wooden coffee table covered with open textbooks, plain notebooks and pencils, cushions and a sofa, a window with city lights",
    "classroom": f"a bright A-level classroom in {SCHOOL}: rows of plain wooden desks and blue plastic chairs, a large blank whiteboard, windows with tropical daylight, ceiling fans",
    "exam_hall": f"the same classroom in {SCHOOL} arranged for an exam: single desks in neat separated rows, each with a question paper and answer sheets, a blank whiteboard, windows with bright daylight, ceiling fans",
    "office": f"the school office of {SCHOOL}: a long counter, a teacher's desk with neat stacks of exam papers, filing cabinets, a closed wooden door to the principal's room, a few plastic chairs along the wall",
    "principal_room": f"the principal's room in {SCHOOL}: a large wooden desk with a few closed files and a pen stand, two visitors' chairs in front of it, a bookshelf of plain binders, a window with tropical daylight, a framed plain landscape picture on the wall",
    "corridor": f"an open school corridor of {SCHOOL} outside the office: a long concrete walkway, a pale wall, a simple wooden bench, a railing open to a sunny courtyard with trees",
    "car": "the interior of a dark luxury car driving through the narrow streets of Malé, Maldives, buildings and motorbikes passing in the window",
    "memory_grad": "a university graduation day, a sunny campus lawn with a modern building behind, graduates in dark gowns in the soft background",
    "dining": f"the dining area of {PENT} at night: a long dark-wood dining table with a simple home-cooked Maldivian dinner (rice, curry, roshi, a jug of water and glasses), warm pendant lamps, floor-to-ceiling windows with the city lights of Malé at night",
    "haizum_room": f"Haizum's large master room in {PENT} at night: a comfortable grey sofa against one wall, a low wooden coffee table in front of it, a tall wooden wardrobe, a warm floor lamp, a window with the night city beyond",
    "wardrobe": f"a corner of Haizum's master room in {PENT} at night: a tall dark-wood wardrobe standing open with neatly hung shirts and folded clothes, a small grey steel safe built into the bottom of the wardrobe",
    "sana_memory": "a quiet small room in Sana's home in Malé in the late afternoon: a small wooden writing desk by a window with a sheer curtain, a cup of tea, a small potted plant",
}
MOOD = {
    "beach": "late afternoon, bright clear tropical sky softening towards gold, gentle sea breeze, calm water, tender then sorrowful",
    "beach_walk": "late afternoon turning to golden hour, warm low sun over the sea, long soft shadows, quiet and full of unspoken feeling",
    "study_home": "evening, warm lamp light, city lights outside the window, busy and friendly, days passing",
    "classroom": "bright tropical daylight through the windows, cheerful and busy, the last day of classes",
    "exam_hall": "bright morning daylight, silent and tense exam atmosphere",
    "office": "daytime, neutral fluorescent and window light, quiet and nervous",
    "principal_room": "daytime, soft window light, serious and tense, then quietly proud",
    "corridor": "daytime, bright courtyard light and soft shadow on the walkway, tender and worried",
    "car": "daytime, bright city light through the windows, reflective and pensive",
    "memory_grad": "soft hazy dreamlike memory glow, warm sunny daylight, proud young happiness",
    "dining": "night, warm amber pendant lamps over the table, deep blue night outside the windows, heavy awkward silence",
    "haizum_room": "night, a warm amber floor lamp against deep blue shadows, intimate, nostalgic, tender father-son warmth",
    "wardrobe": "night, warm amber lamp light from the side, deep shadows inside the wardrobe, quiet surprise",
    "sana_memory": "soft hazy dreamlike memory glow, pale late-afternoon light through a sheer curtain, fragile, sorrowful and tender",
}

LAIL_UNI = "young Lail in his school uniform: a white short-sleeved school shirt and dark-navy long trousers"
SABA_UNI = "young Saba in her school uniform: a white long-sleeved school tunic, a navy ankle-length skirt and a white hijab fully covering her hair and neck"
ASIL_UNI = "young Asil in a white short-sleeved school shirt and dark-navy long trousers"
TEACHER = "the class teacher, a middle-aged Maldivian man with short greying hair and glasses in a pale-blue long-sleeved shirt and dark trousers"
PRINCIPAL = "the school principal, a grey-haired Maldivian man of about 55 in a white long-sleeved shirt and a dark tie"
HAIZUM_HOME = "Haizum at home in a casual dark-grey polo shirt and dark trousers"

BEATS = [
    # ---------------- BEACH ----------------
    dict(to=3, reason="episode opening: Lail and Saba on the beach, she shows him her little brother's photo", chars=["saba_young", "lail_young"], loc="beach",
         visual="young Saba and young Lail sitting side by side on the low seawall edge of the beach, a clear arm's length of space between them; Saba laughing, holding her phone out towards him at arm's length (the screen shows only a soft glow), Lail leaning slightly to look, smiling playfully; the calm lagoon behind them",
         camera="medium two-shot, eye level, their faces in the upper half, the pale sand as a calm lower third", amb="beach_day"),
    dict(to=6, reason="emotional turning point: the question about her brother brings Saba to tears", chars=["saba_young", "lail_young"], loc="beach",
         visual="closer view of the two still sitting apart on the seawall: Saba turned towards the sea, her eyes filling with tears, lips pressed together, phone lowered in her lap; Lail beside her at arm's length, his smile gone, looking at her with shock and concern",
         camera="medium close two-shot, eye level, faces in the upper third", amb="beach_day",
         sens="death", safe="the fatal accident of her father and brother is only spoken of; shown as her tears looking at the sea"),
    dict(to=11, reason="action change: comfort at a distance; both cry, Lail remembering his late mother", chars=["saba_young", "lail_young"], loc="beach",
         visual="Saba with her head bowed, covering her face with both of her own hands, shoulders trembling; Lail sitting an arm's length away, holding out a folded white tissue towards her without touching her, his own eyes glistening with tears, the sea glowing behind them",
         camera="medium two-shot from a slight angle, faces in the upper half, sand as the lower third", amb="beach_day",
         sens="intimacy", safe="narration: he wipes her tears, draws her close and she hides her face on his chest — shown instead as him offering a tissue at arm's length, no touching (unmarried teenagers)"),
    dict(to=13, reason="action and location change: they walk along the shore towards Maafannu", chars=["lail_young", "saba_young"], loc="beach_walk",
         visual="Lail and Saba seen from behind walking slowly side by side along the shoreline promenade towards the low golden sun, a clear gap of space between them, their hands at their own sides, Saba's white hijab and powder-blue dress, Lail's grey t-shirt; long soft shadows on the sand",
         camera="wide shot from behind, the figures and sea in the upper two-thirds, the sand path as the calm lower third", amb="beach_dusk",
         sens="intimacy", safe="narration: he takes her hand and interlaces his fingers — shown as walking side by side with space between them, no hand-holding"),
    # ---------------- REVISION / LAST DAY ----------------
    dict(to=15, reason="time jump: days pass, exam revision sessions in students' homes", chars=["lail_young", "saba_young", "asil_young"], loc="study_home",
         visual="an evening revision session: Lail, Saba and Asil sitting on cushions around a low coffee table covered with open textbooks and plain notebooks, Lail explaining with a pencil, Saba listening attentively on the far side of the table, Asil yawning with a smile; they sit apart from each other",
         camera="medium wide, slightly high angle, faces in the upper half, the table top as the lower third", amb="home_night", transition="black"),
    dict(to=19, reason="scene change: last day of classes, classmates crowd around Lail; Saba and Asil clear his scraps", chars=["lail_young", "saba_young", "asil_young"], loc="classroom",
         visual=f"{LAIL_UNI}, sitting at his desk patiently drawing a small diagram on a yellow sticky note for a group of classmates in uniform in uniform: only boys in white shirts stand right beside him, while two girls in white tunics and white hijabs stand across the desk opposite him, the whole desk between them; on the right side of the room, several steps away from Lail, {SABA_UNI} and {ASIL_UNI} picking up small crumpled paper scraps and dropping them into a plastic dustbin; sticky notes show only soft scribble lines",
         camera="medium wide, eye level, faces in the upper half, desk tops as the lower third", amb="classroom"),
    # ---------------- EXAM ----------------
    dict(to=21, reason="time jump: the next day, the exam; the teacher picks up a paper beside Saba's chair", chars=["saba_young", "lail_young"], loc="exam_hall",
         visual=f"the exam in progress, students bent over their papers in separated rows; in the aisle {TEACHER} bending to pick up a tiny folded yellow paper from the floor beside the chair of {SABA_UNI}, who looks up startled; {LAIL_UNI} two desks away glancing over",
         camera="wide shot down the aisle, eye level, faces in the upper half, the floor as the calm lower third", amb="classroom", transition="black"),
    dict(to=23, reason="emotional turning point: the teacher orders Saba to the office; she cries, Lail shuts his eyes", chars=["saba_young", "lail_young"], loc="exam_hall",
         visual=f"{TEACHER} standing stern beside Saba's desk holding up the small unfolded yellow note (only faint illegible scribbles); {SABA_UNI} sitting frozen, tears running down her cheeks; the other students turned in their seats staring; {LAIL_UNI} in the background closing his eyes in dismay",
         camera="medium shot, eye level, faces in the upper two-thirds", amb="classroom"),
    dict(to=25, reason="action change: Lail stands up and claims the note is his", chars=["lail_young", "saba_young"], loc="exam_hall",
         visual=f"{LAIL_UNI} standing up from his chair, one hand raised slightly, his face determined and pale; the whole class turned towards him in astonishment; {TEACHER} in the foreground turning in surprise with the small note in his hand; {SABA_UNI} seated two desks away, tearful, staring at Lail",
         camera="medium wide, slightly low angle from behind the teacher's shoulder, faces in the upper half", amb="classroom",
         sens="other", safe="cheating accusation shown only as a tense classroom; no punishment"),
    dict(to=29, reason="action change: Lail bows his head; the teacher's searching look; Saba's teary eyes on Lail", chars=["lail_young", "saba_young"], loc="exam_hall",
         visual=f"{LAIL_UNI} standing with his head bowed beside his desk; {TEACHER} looking at him with a long thoughtful searching gaze, the note lowered; in the soft background {SABA_UNI} seated with tear-filled eyes fixed on Lail; classmates watching silently",
         camera="medium shot, eye level, the teacher in the foreground left, Lail centre, Saba soft in the background", amb="classroom"),
    dict(to=32, reuse="beat_007", reason="return to the exam room as everyone wonders; the teacher tells them to finish the paper", loc="exam_hall",
         visual="(reuse)", amb="classroom"),
    # ---------------- OFFICE / PRINCIPAL ----------------
    dict(to=34, reason="scene change: after the exam, the two wait in the school office", chars=["lail_young", "saba_young"], loc="office",
         visual=f"{LAIL_UNI} and {SABA_UNI} standing apart against the office wall, an empty chair between them, heads lowered and nervous; {TEACHER} entering with a stack of exam papers, setting them on his desk",
         camera="medium wide, eye level, faces in the upper half, the tiled floor as the lower third", amb="office_day"),
    dict(to=36, reason="scene change: inside the principal's room, questioning", chars=["lail_young", "saba_young"], loc="principal_room",
         visual=f"{PRINCIPAL} sitting behind his large desk, hands folded, looking up at the two students; {LAIL_UNI} and {SABA_UNI} standing in front of the desk an arm's length apart, both with heads bowed; Saba's eyes red",
         camera="medium wide from behind the desk's side, faces in the upper half", amb="office_quiet"),
    dict(to=38, reason="character change: Haizum enters with the teacher; Lail ashamed", chars=["haizum", "lail_young", "saba_young"], loc="principal_room",
         visual=f"the door of the principal's room opening; Haizum in his dark-navy suit stepping in beside {TEACHER}, his face surprised and serious; {LAIL_UNI} turning, cheeks burning with embarrassment, eyes down; {SABA_UNI} standing apart, tearful",
         camera="medium wide, eye level, faces in the upper half", amb="office_quiet"),
    dict(to=40, reason="character focus change: Saba is sent outside, eyes swollen with tears", chars=["saba_young"], loc="corridor",
         visual=f"{SABA_UNI} stepping out of the office door into the open corridor, head lowered, eyes red and swollen, wiping a tear with the back of her hand; the bright courtyard beyond the railing",
         camera="medium shot, eye level, her face in the upper third, the concrete walkway as the lower third", amb="office_day"),
    dict(to=45, reason="action change: the principal greets Haizum; Lail stands head bowed, afraid to lie before his father", chars=["haizum", "lail_young"], loc="principal_room",
         visual=f"Haizum in his dark-navy suit seated in a visitor's chair before the principal's desk, {TEACHER} seated in the chair next to him; {PRINCIPAL} behind the desk looking gravely at Lail; {LAIL_UNI} standing beside the desk with his head bowed, hands clasped in front of him",
         camera="medium wide, eye level, faces in the upper half, the desk top as the lower third", amb="office_quiet"),
    dict(to=48, reason="action change: the teacher shows Haizum the note; Haizum recognises his son's handwriting", chars=["haizum", "lail_young"], loc="principal_room",
         visual="close two-shot: Haizum seated, holding a small yellow sticky note covered with faint illegible scribble lines, lifting his eyes from it to look at his son with a calm searching expression; Lail standing beside him, glancing at his father anxiously",
         camera="medium close-up, eye level, faces in the upper half, the note at chest height", amb="office_quiet",
         sens="other", safe="the sticky note shows only illegible scribble lines"),
    dict(to=52, reason="action change: Lail tells his father the truth", chars=["lail_young", "haizum"], loc="principal_room",
         visual=f"{LAIL_UNI} standing straight now, one hand open towards his chest, speaking earnestly and respectfully to his seated father; Haizum in his navy suit listening attentively, looking up at his son; the principal's desk and window light behind them",
         camera="medium two-shot, eye level, faces in the upper half", amb="office_quiet"),
    dict(to=54, reason="emotional turning point: Haizum's faint proud smile", chars=["haizum"], loc="principal_room",
         visual="close-up of Haizum in his dark-navy suit, a faint proud smile spreading across his bearded face, his eyes warm and slightly moist, soft window light on his face",
         camera="close-up, eye level, his face in the upper half", amb="office_quiet"),
    dict(to=58, reason="scene and action change: outside, Lail stays beside the crying Saba; Haizum watches and understands", chars=["saba_young", "lail_young", "haizum"], loc="corridor",
         visual=f"{SABA_UNI} sitting on the wooden bench in the corridor crying softly into a tissue; {LAIL_UNI} standing an arm's length beside the bench, leaning slightly towards her with a worried face, speaking gently, not touching her; in the office doorway behind them Haizum in his navy suit pausing to watch them with a thoughtful look",
         camera="medium wide, eye level, faces in the upper half, the walkway as the calm lower third", amb="office_day",
         sens="intimacy", safe="narration: Lail's hand on her shoulder — shown as standing near her without touching"),
    dict(to=60, reason="scene change: Haizum driving home, thinking about his son", chars=["haizum"], loc="car",
         visual="Haizum in his dark-navy suit behind the wheel of his car, both hands on the wheel, eyes on the road but lost in thought, sunlight and passing buildings reflected on the window",
         camera="medium shot from the passenger seat, his face in the upper half, the dashboard as the lower third", amb="car_interior"),
    dict(to=64, reason="memory: Haizum and Sana's past - school love, marriage, his PhD when Lail was three", chars=["haizum", "sana"], loc="memory_grad",
         visual="memory: a younger Haizum, about 30, beard fully black, in a dark academic graduation gown and cap, beaming; beside him Sana, young and radiant, in her sage-green dress and ivory hijab fully covering her hair and neck, holding a little three-year-old boy in a small shirt on her hip; they stand side by side, his hand resting on her shoulder, proud and happy",
         camera="medium shot, eye level, faces in the upper half, green lawn as the lower third", amb="memory", transition="dissolve"),
    dict(to=66, reuse="beat_021", reason="return from the memory to Haizum in the car, wondering if Saba is right for his son", loc="car",
         visual="(reuse)", amb="car_interior", transition="dissolve"),
    # ---------------- DINNER ----------------
    dict(to=71, reason="time and scene change: that night, a silent family dinner", chars=["haizum", "lail_young", "laira", "shafeeqa"], loc="dining",
         visual=f"the family at the long dining table at night: {HAIZUM_HOME} at the head of the table, eating quietly with a distant indifferent face; Laira and Maama Shafeeqa on one side talking animatedly and smiling; Lail in his grey t-shirt on the other side, eyes lowered to his plate, tense; Laira glancing worriedly at her father",
         camera="medium wide, slightly high angle, faces in the upper half, the table top as the lower third", amb="home_night", transition="black"),
    dict(to=74, reason="action and location change: Lail called to his father's room; Haizum waiting on the sofa with two albums", chars=["lail_young", "haizum"], loc="haizum_room",
         visual=f"Lail in his grey t-shirt standing hesitantly in the open doorway of his father's room, worried, expecting a lecture; {HAIZUM_HOME} sitting on the grey sofa looking up at him calmly; two old photo albums with plain covers lying on the coffee table",
         camera="medium wide from inside the room, eye level, faces in the upper half, the rug as the lower third", amb="room_night"),
    dict(to=76, reason="action change: Lail sits beside his father, who gently asks if he hides anything", chars=["haizum", "lail_young"], loc="haizum_room",
         visual=f"{HAIZUM_HOME} and Lail in his grey t-shirt sitting side by side on the grey sofa; Haizum turned towards his son, asking gently with soft eyes; Lail shaking his head slightly, uneasy; the albums closed on the coffee table",
         camera="medium two-shot, eye level, faces in the upper half, the coffee table as the lower third", amb="room_night"),
    dict(to=79, reason="detail change: the album of his parents' school days opens", chars=["haizum", "lail_young"], loc="haizum_room",
         visual="close view over their shoulders of an old photo album open on Haizum's lap; Haizum's finger pointing at one small faded framed photo, softly blurred, of a teenage boy in a white school shirt and a teenage girl in a white school tunic and white hijab standing a little apart in a schoolyard; Lail leaning in, a faint smile in the upper part of the frame",
         camera="over-the-shoulder close-up, faces upper third, the album in the middle", amb="room_night",
         sens="other", safe="old photos of teen Haizum and Sana are small, faded and blurred; Sana in hijab; no text"),
    dict(to=83, reason="emotional change: warmth and laughter; Haizum strokes Lail's head", chars=["haizum", "lail_young"], loc="haizum_room",
         visual=f"{HAIZUM_HOME} laughing warmly, one hand resting affectionately on top of Lail's head; Lail in his grey t-shirt smiling shyly and blushing, the open album on his knees; relief on his face",
         camera="medium close two-shot, eye level, faces in the upper half", amb="room_night"),
    dict(to=85, reason="detail: the photo of Sana's 18th birthday in class", loc="haizum_room",
         visual="close-up of an open old photo album page under warm lamp light: small faded photos softly blurred — a classroom with a small cake on a desk surrounded by teenage girls in white hijabs and boys in white shirts, a group photo on a sports field, a school stage; nothing readable",
         camera="close-up top-down detail, the album filling the frame, warm light", amb="room_night",
         sens="other", safe="photos small, faded and blurred; all girls in hijab"),
    dict(to=89, reuse="beat_026", reason="back to father and son: Lail amazed that his mother played guitar and sang", loc="haizum_room",
         visual="(reuse)", amb="room_night"),
    dict(to=91, reason="action change: Haizum searches the wardrobe and opens the safe", chars=["haizum"], loc="wardrobe",
         visual=f"{HAIZUM_HOME} crouching at the open wardrobe, one hand searching among folded clothes, the other turning the dial of the small grey steel safe at the bottom; his face serious and hesitant",
         camera="medium shot, slightly low angle, his face in the upper half", amb="room_night"),
    dict(to=93, reason="emotional turning point: a box from Sana inside the safe", chars=["haizum"], loc="wardrobe",
         visual="the small safe door open, revealing a neat pale-ivory box the size of a large book tied with a faded ribbon, a small blank card tucked under the ribbon; Haizum's surprised face lit by the lamp as he looks at it",
         camera="medium close-up, eye level, his face in the upper third, the box in the middle", amb="room_night",
         sens="other", safe="the name on the box is not readable: a blank card"),
    dict(to=96, reason="action change: the pen drive in the laptop, Sana's recorded voice fills the room", chars=["lail_young", "haizum"], loc="haizum_room",
         visual=f"Lail in his grey t-shirt and {HAIZUM_HOME} sitting side by side on the sofa before an open laptop on the coffee table with a small pen drive plugged in, the screen showing only a soft glowing audio waveform; Lail's face full of wonder, his lips parted; Haizum smiling tenderly with moist eyes",
         camera="medium two-shot, eye level, faces in the upper half, the laptop on the table as the lower third", amb="room_night",
         sens="other", safe="Sana's singing is not heard (no music): only room silence; screen shows a waveform glow"),
    dict(to=98, reason="action change: Lail leans into his father; father and son moved", chars=["lail_young", "haizum"], loc="haizum_room",
         visual="Lail in his grey t-shirt leaning against his father's shoulder with his eyes closed, Haizum in his dark-grey polo with his arm around his son's back, patting it gently, his eyes wet and his chin resting near his son's head; the laptop glow beside them",
         camera="medium close-up, eye level, faces in the upper half", amb="room_night", sens="other",
         safe="father and son (mahram) - a tender modest father-son moment"),
    dict(to=102, reuse="beat_026", reason="back to the two side by side: Haizum's advice about keeping within limits", loc="haizum_room",
         visual="(reuse)", amb="room_night"),
    dict(to=105, reason="character change: Lail leaves; Haizum alone on the sofa, hand on his forehead", chars=["haizum"], loc="haizum_room",
         visual=f"{HAIZUM_HOME} alone on the grey sofa, leaning back heavily, his right hand pressed to his forehead, eyes half-closed and glistening; the closed albums beside him, the doorway empty",
         camera="medium shot, eye level, his face in the upper half, the coffee table as the lower third", amb="room_night"),
    dict(to=107, reason="action change: Sana's box opened - a locked diary and two letters", chars=["haizum"], loc="haizum_room",
         visual="close view of the pale-ivory box open on Haizum's knees: inside a small dark-blue diary with a little combination lock on its clasp, two sealed plain envelopes beside it; Haizum's hands resting on the box edge, his tear-stained face in soft focus above",
         camera="high-angle close-up, his face upper third, the box in the middle", amb="room_night",
         sens="other", safe="diary and envelopes blank, no readable text"),
    dict(to=111, reason="action change: Haizum reads Sana's note to Lail on the diary and shuts the box", chars=["haizum"], loc="haizum_room",
         visual="Haizum holding the small dark-blue diary in both hands, a little folded slip of paper with faint illegible lines tucked on its cover, his face torn between sorrow and fear, eyes wet; the open box on the sofa beside him",
         camera="medium close-up, eye level, his face in the upper half", amb="room_night", sens="other",
         safe="the note shows only faint illegible lines"),
    dict(to=113, reason="action change: he opens the letter addressed to him", chars=["haizum"], loc="haizum_room",
         visual="Haizum unfolding a single sheet of cream letter paper covered with soft illegible handwriting lines, his hands trembling slightly, his face bent over it in the warm lamp light, a torn plain envelope on his knee",
         camera="medium close-up, slightly high angle, his face in the upper third, the letter in the middle", amb="room_night",
         sens="other", safe="the letter shows only illegible lines"),
    dict(to=119, reason="memory: Sana, gravely ill and tired, writing the letter (her voice)", chars=["sana"], loc="sana_memory",
         visual="memory: Sana in her sage-green dress and ivory hijab fully covering her hair and neck, sitting at a small wooden desk by the window, thin, pale and tired, writing slowly on a sheet of cream paper (only soft illegible lines), her other hand resting on her chest, a distant sorrowful look out of the window",
         camera="medium shot, eye level, her face in the upper half, the desk top as the lower third", amb="memory",
         transition="dissolve", sens="other", safe="her illness and approaching death only implied by her tired face"),
    dict(to=123, reason="return from the memory: Haizum breaks down over the letter", chars=["haizum"], loc="haizum_room",
         visual="close-up of Haizum on the sofa at night, the letter crumpled slightly against his chest in one hand, tears running down his bearded face, eyes closed in deep remorse, the warm lamp behind him and deep blue shadows",
         camera="close-up, eye level, his face in the upper half", amb="room_night", transition="dissolve"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Another child of my father?\" Lail asked jokingly. \"Well done, then!\" Saba laughed and shook her head.")
sh(2, "\"I said that because the name says 'Laith Haizum',\" Lail said, laughing. \"Shall I show you a photo?\" Saba found a photo of her little brother on her phone and showed him.")
sh(3, "Lail looked closely at the photo. \"This is my little brother,\" Saba said. \"Where is he now? Still in Australia?\" Lail asked.")
sh(4, "At that question Saba looked at Lail's face. Within a moment her eyes filled with tears.")
sh(5, "Seeing that, the smile on Lail's lips vanished at once. \"In that terrible accident... my little brother left us along with my father.\"",
   hum=True)
sh(6, "Deep sorrows hidden in the depths of her heart came back fresh and poured from her eyes as tears.", hum=True)
sh(7, "Unable to hold them back, the tears rolled down her cheeks. Tenderly wiping the tears from her eyes, Lail drew her close.",
   [("sob_breath", "ކަރުނަތިކިތައް", -24)])
sh(8, "Saba too, without meaning to, hid her face against Lail's chest. It was the first time those two hearts had come so close.")
sh(9, "Saba could feel Lail's heart beating. After a silent moment, the two moved apart.")
sh(10, "Traces of tears showed in Lail's eyes too. Memories of his late mother also filled his heart at that moment.", hum=True)
sh(11, "Both wiped their eyes and tried to compose themselves. After staying there a while,")
sh(12, "they got up and began to walk along the shore towards Maafannu. As they walked slowly, Lail lovingly took Saba's hand.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(13, "And he laced his fingers through hers. Though neither said a word to the other, there was a deep feeling even in that silence.")
sh(14, "The days passed at their quick pace. Though they never spoke their love aloud, the time they made for each other and spent together kept growing.")
sh(15, "As the year-end exams drew near, revision sessions began in class and in different students' homes.",
   [("page_turn", "މުރާޖަޢާކުރުމުގެ", -24)])
sh(16, "Today was the very last day of classes. Next came the exams. Many classmates gathered around Lail,")
sh(17, "asking about the parts they still didn't understand. Patiently, Lail drew on sticky notes,",
   [("pen_scribble", "ކުރަހައި", -22)])
sh(18, "writing things down to explain the lessons to them. Once their questions were answered, each student would move away.")
sh(19, "Saba and Aseel helped pick up the scraps of paper Lail had used and thrown away, and put them in the dustbin. The next day's exam began,",
   [("paper_shuffle", "ކަރުދާސްކޮޅުތައް", -22)])
sh(20, "and the students were absorbed in answering their question papers. The teacher, who was walking up and down the classroom,",
   [("footsteps_pavement", "ހިނގަހިނގައި", -24)])
sh(21, "suddenly stopped and picked up a small piece of paper from beside Saba's chair. He unfolded it, looked at it, and said in a very harsh tone,",
   [("paper_shuffle", "ނިއުޅުވާލައި", -22)])
sh(22, "\"Aishath Saba Ilyas! Go to the office right now!\" Every student's attention turned that way.",
   [("crowd_gasp", "ސަމާލުކަން", -24)])
sh(23, "Seeing the paper in the teacher's hand, Lail shut his eyes in worry, and Saba burst into tears. \"Sir! That isn't Saba's...",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -22)], hum=True)
sh(24, "it's mine,\" Lail said, standing up from his chair. At that, astonishment showed on the faces of the whole class and the teacher.",
   [("cloth_rustle", "ތެދުވަމުން", -22)])
sh(25, "\"Lail! Are you sure that's the truth? Lail could even be suspended over a copying case,\" the teacher said in a warning tone.")
sh(26, "\"Yes, it's really mine,\" Lail said, bowing his head. The teacher gave Lail a long, deep look.")
sh(27, "The teacher knew Lail was not the kind of student to do such a disgraceful thing. And he understood that Lail had told that lie to save Saba.")
sh(28, "Then the teacher looked at Saba. Saba stood there with tear-filled eyes, gazing towards Lail.")
sh(29, "The whole class was watching the two of them. None of them believed that either of those two students would copy.")
sh(30, "Saba was a student who worked extremely hard at her studies, while Lail was a top student who got A-stars in every subject at O-level, exceptionally gifted at maths, and who helped other students too.")
sh(31, "So no student imagined such a student would cheat in an exam. Then what was that piece of paper?")
sh(32, "That was the question in everyone's mind. \"Both of you sit down and finish the paper. When you finish, go to the principal,\" the teacher ordered.")
sh(33, "As soon as the exam ended, the two went to the office. Just then the teacher too came into the office carrying the papers. Asking the two to wait,",
   [("paper_shuffle", "ޕޭޕަރުތައް", -22)])
sh(34, "the teacher put the papers on his desk and went into the principal's room with Lail's and Saba's papers.")
sh(35, "About fifteen minutes later the teacher came out and let the two inside. To the principal's questions too, Lail gave the same answer:",
   [("door_open", "ނުކުމެ", -22)])
sh(36, "that the paper was his. Saba also said it had nothing to do with her and that she had not copied.")
sh(37, "As the two stood with heads bowed before the principal, there was a knock on the door, and in came Haizum with the teacher.",
   [("knock", "ޓަކިޖަހައިލުމަށްފަހު", -18), ("door_open", "ވަދެގެން", -22)])
sh(38, "For the first time in his school life a parent had to be summoned over something he did, and Lail felt deeply worried and ashamed.")
sh(39, "Haizum too looked at Lail in surprise. \"Saba, wait outside.\" At the teacher's word, Saba politely went out.",
   [("door_close", "ނުކުތެވެ", -22)])
sh(40, "Accused of something she didn't do, and because of the lie Lail told to save her, Saba's eyes were swollen with tears. \"Haizum.\"",
   [("sob_breath", "ކަރުނުން", -24)])
sh(41, "The principal greeted Haizum and invited him to sit. At that moment Lail stood with his head bowed.")
sh(42, "The teacher also sat in the chair next to Haizum. The principal gave Lail a deep look.")
sh(43, "\"Your father is sitting right here, so tell us truthfully what happened, Lail,\" the principal said. Lail still stood with his head lowered,")
sh(44, "because he was reluctant to lie in front of his father. Yet what he was saying wasn't really a lie. That sticky note really was his.")
sh(45, "The handwriting on it was his own writing too. But he did not cheat in the exam. And the thought of doing such a thing would never even cross his mind.")
sh(46, "The teacher showed the note to Haizum. Haizum looked at the note, then at Lail's face. \"This is Lail's handwriting, all right.\"",
   [("paper_shuffle", "ދައްކައިލިއެވެ", -24)])
sh(47, "Haizum said. \"We know that too. And we know Lail would not cheat. The problem is that Lail is trying to take the blame himself to save another student.\"")
sh(48, "the teacher said, looking at Lail. \"My son, is that true? What is the real truth?\" Haizum asked.")
sh(49, "His trust in his son was firm. \"Dad, Saba didn't cheat at all. That note is something I wrote for her yesterday to explain a lesson.")
sh(50, "Yesterday, when we threw away all the leftover papers, it fell there without us noticing.")
sh(51, "I believe Saba shouldn't be punished for something she didn't do. Saba is a very hardworking student.")
sh(52, "And it's not only because it's Saba - even if it weren't my friend, I couldn't bear to watch an innocent person be punished.\"")
sh(53, "Lail revealed the truth to his father with great respect. A faint smile came to Haizum's lips. This was Sana's perfect upbringing.",
   hum=True)
sh(54, "He was proud of his son's honesty and sense of justice. After the meeting went on a while, Lail was sent outside.")
sh(55, "When Haizum came out after talking further with the principal, Saba was crying. Lail was standing beside her,",
   [("door_open", "ނުކުތްއިރު", -22)])
sh(56, "his hand lovingly on her shoulder, comforting her. The worry on Lail's face was no secret to Haizum.")
sh(57, "He was certain she was not just an ordinary friend. She was Lail's special girl. If she weren't that special,")
sh(58, "Lail would be with his other friends. Haizum watched the two of them for a while, then left without saying anything.",
   [("footsteps_pavement", "ނުކުމެގެން", -24)])
sh(59, "He meant to talk to Lail about it once they got home. Even as he drove, Haizum's heart and mind were filled with thoughts of his son.")
sh(60, "He knew Lail had now reached the age of choosing a partner for married life.")
sh(61, "Memories of the past began to take shape before his eyes. He and Sana had first met at this very school, in this very grade.")
sh(62, "Their first friendship slowly turned into love. After that, they finished their degrees, married, and had their first child.")
sh(63, "When Lail was only 3, Haizum earned his PhD. It wasn't that Sana had no chance to study further. But,")
sh(64, "with the responsibility of raising two children, she did not want to study beyond her Master's. Haizum sank into deep thought.")
sh(65, "Was Saba the most suitable girl to be his son's life partner? Was Saba the truth of the sweet dreams he and Sana had dreamed for their son?")
sh(66, "He would never want to hurt his son's heart. Yet he couldn't bear for his son, as dear to him as his own life, to be with just any girl.")
sh(67, "In the end Haizum decided to find out properly about Saba's background. At dinner that night, a deathly silence lay between Haizum and Lail at the table.",
   [("cup_clatter", "ކެއުމުގެ", -24)])
sh(68, "Lail thought his father was angry with him. In that silent moment, memories of his mother filled Lail's heart.")
sh(69, "At the table they were talking about Laira leaving to study next January. Although Maama and Laira talked about it with excitement,")
sh(70, "Haizum seemed indifferent. He gave only short replies like \"Hmm\" or \"We'll see.\"")
sh(71, "Laira also noticed that Dad was in a bad mood. But she didn't dare ask anything, in case it upset him further.")
sh(72, "After the meal, as everyone got up from the table, Lail too headed for his room.",
   [("cloth_rustle", "ތެދުވެގެން", -24)])
sh(73, "Just then Haizum called Lail to come to his room. Lail thought: tonight I'll have to listen to Dad's long lecture.")
sh(74, "When he entered Haizum's room, Haizum was sitting on the sofa at one side of the room. On the table in front of him lay two photo albums.",
   [("door_open", "ވަދެވުނުއިރު", -22)])
sh(75, "Seeing Lail, Haizum asked him to sit beside him. Lail went and sat beside his father. \"Are you hiding anything from Dad, son?\"")
sh(76, "Haizum asked very gently. Lail looked at his father and shook his head to say no. Haizum let out a deep breath,",
   [("sigh", "ނޭވާއެއް", -22)])
sh(77, "leaned forward and opened one of the albums on the table. It was an album Lail had never seen before.",
   [("page_turn", "ހުޅުވައިލިއެވެ", -22)])
sh(78, "In it were kept memories of his mother's and father's school days. \"This is a photo Dad and Mum took at your age.")
sh(79, "At that very school, in that very uniform,\" Haizum said, pointing to a photo. Lail looked at the photo and gave a slight smile.")
sh(80, "\"Mum is so lovely,\" Lail said in a voice full of love. \"And Dad?\" Haizum asked jokingly. \"Dad is very smart.\"")
sh(81, "Lail answered, looking at Haizum's face. With that, Haizum lovingly stroked Lail's head. \"Don't we look alike, son?\"")
sh(82, "Haizum asked with a smile. \"Hmm... the eyebrows,\" Lail said, a little shy. Haizum burst out laughing.")
sh(83, "With that, Lail's heart felt a great relief. Sure now that his father wasn't angry with him, the fear and weight in his heart lifted.")
sh(84, "\"Look, this is your mum's eighteenth birthday. The day a small cake was cut in class,\" Haizum told him.")
sh(85, "And naming each friend in the photo one by one, he explained which subject each was good at and who stood out on the sports field.",
   [("page_turn", "ފޮޓޯގައި", -24)])
sh(86, "\"Did Mum play the guitar too?\" Lail asked in surprise. \"Yes, and Mum sang too.")
sh(87, "In fact, that talent of yours for writing and poetry is something you inherited straight from your mum.\"")
sh(88, "Haizum said, looking at Lail's face. Haizum was trying, more than ever before, to build a close bond with his young son,")
sh(89, "to learn the secrets hidden in that heart and become his son's closest friend. \"Was Mum really that talented?\" Lail asked in surprise.")
sh(90, "\"Wait!\" Saying this, Haizum got up from the sofa, went and opened the wardrobe, and began searching through the clothes for a pen drive.",
   [("creak", "ހުޅުވައިލިއެވެ", -22), ("cloth_rustle", "ހާވަން", -24)])
sh(91, "Then, for the first time in ages, he entered the secret code and opened the safe. Since Sana had gone away,",
   [("lock_click", "ހުޅުވައިލިއެވެ", -20)])
sh(92, "he had not even known what was inside that safe. But as soon as he opened it, his eyes fell on a box about the size of a monitor book.")
sh(93, "Seeing his name written on top of it, surprise showed on Haizum's face. \"To dear Haizum, from Sana.\"", hum=True)
sh(94, "After reading that, he set the box aside, came back with the pen drive he had found, and closed the wardrobe. And sitting beside Lail,",
   [("door_close", "ލައްޕައިލިއެވެ", -24)])
sh(95, "he plugged the pen drive into the laptop and played the song he wanted. At once Sana's beautiful voice filled the room. \"How perfect!\"")
sh(96, "Lail couldn't help saying. Smiling lovingly, Haizum stroked Lail's head. \"This is the day Dad's heart was given to Mum.")
sh(97, "This is her voice, recorded on Dad's phone,\" Haizum said with deep emotion. As silence settled over everything, Lail wrapped his arms around his father.",
   [("cloth_rustle", "ބައްދައިލިއެވެ", -24)], hum=True)
sh(98, "Haizum too lovingly patted his son's back. When Lail drew back, Haizum went on talking again.")
sh(99, "\"Dad knows you might have a girl you like now. That's not a problem.\" Not knowing what to say to that, Lail sat staring.")
sh(100, "\"Liking a girl is not wrong. But you must always keep within your limits. Remember!")
sh(101, "She too is a child raised with her parents' love. To every parent, their children's honour and dignity is everything.\"")
sh(102, "Haizum advised. Lail nodded, agreeing with those words. But he did not yet want to reveal the secret of his heart,")
sh(103, "thinking it was too soon. After looking at the photos for a while, Lail left the room. Haizum let out a deep breath and leaned back on the sofa,",
   [("sigh", "ނޭވާއެއް", -22)])
sh(104, "resting his right hand on his forehead, hoping that even if Lail didn't tell him now, he would share it later.")
sh(105, "Then Haizum got up and put the photo albums back in the wardrobe. The pictures of the past reopened the wounds of his heart, and his eyes filled with memories of Sana.",
   [("creak", "އަލަމާރިއަށް", -24)], hum=True)
sh(106, "Wiping his tears, he brought the box from the safe and sat on the sofa again. Inside the box, bearing Lail's name,",
   [("sob_breath", "ކަރުނަތައް", -24)])
sh(107, "was a diary locked with a password. Besides that there were two letters, written separately to Laira and to Haizum.")
sh(108, "With deep curiosity Haizum read the writing on the outside of Lail's diary. \"When this book reaches you, Mum may no longer be in this world.",
   [("page_turn", "ކިޔައިލިއެވެ", -24)])
sh(109, "The diary's password is hidden in your wardrobe. Even so, you must read this diary only after your A-levels.")
sh(110, "This is the diary of your mother's and father's life,\" Sana had written. Haizum hurriedly put the slip back in the box and closed it.",
   [("soft_thud", "ލައްޕައިލިއެވެ", -22)])
sh(111, "He did not want that box to reach his son's hands at all. Even so, since it was Sana's last wish, Haizum decided to hand the diary to Lail once A-levels were over.")
sh(112, "And after setting the box aside, he tore open the letter meant for him. \"Dear Haizam, after greetings I write.",
   [("paper_shuffle", "ކަނޑައިލިއެވެ", -22)])
sh(113, "When this letter reaches your hands, I may be counting my last breaths. Or I may have said farewell to this passing world and journeyed to the eternal one.",
   hum=True)
sh(114, "Just as I am grateful for the love and kindness I received from you, I am grateful for all the sorrows I received too.")
sh(115, "As you asked, I have forgiven you. But every time you come before me, that painful past comes back to my mind.")
sh(116, "It is hard to bear, and it hurts my heart so much. What drove the two of us apart was the betrayal of a single night.", hum=True)
sh(117, "If that were a wrong I had done, would you forgive me? Surely not.")
sh(118, "And would you believe that I had no fault at all? No, you would not believe that either.")
sh(119, "I didn't want to talk to you about the past because there is nothing more to say. And even if we talked, it would do no good.")
sh(120, "Our future has been decided by both of us. You did not want to let me go.")
sh(121, "And I did not want to live with you. For the children's sake I have lived this long. The time is near.")
sh(122, "I am so very tired now. I want to close my eyes without any complaint. But...", hum=True)
sh(123, "your image never let me be far from those memories. The answer to the one question my heart asks me is in your hands alone. Tell me, what was my fault?\"",
   hum=True)
SHOTS = S

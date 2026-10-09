"""Beat/shot plan for Nindheveethimeymathee episode 420 (SCHOOL timeline; used by plan_beats.py).
Night of grief after Sana's death; Lail and Saba's late-night call; slipping out to a cafe; the seawall at sunset.
Bible rules: hijab always, NO touching between Lail and Saba (arm's length), nobody lying down, no readable phone text."""

FLAT = "the family's modern high-rise apartment in Male', Maldives"
LOC = {
    "sana_room": f"the late mother's softly furnished bedroom in {FLAT} at night: cream walls, a quilted mattress with a padded fabric headboard, a small bedside lamp, a wooden dressing table with a few perfume bottles and a small framed photo blurred beyond recognition, an armchair by the window, sheer curtains over a dark window with distant city lights",
    "scarf": f"a quiet corner of the late mother's bedroom in {FLAT} at night: a wooden armchair by the window with a neatly folded ivory headscarf resting on its seat, a small framed photo on the side table blurred beyond recognition, sheer curtains, distant city lights",
    "memory_couple": "the balcony of a cosy Male' apartment years ago at golden hour, potted plants, a small round table with two cups of tea, the lagoon and city rooftops glowing behind",
    "lail_room": f"a teenage boy's bedroom in {FLAT} late at night: a quilted mattress with a grey padded headboard, a study desk with neat school books and a phone on a charger, a desk lamp switched off, a large window with Male' city lights and the dark lagoon beyond",
    "lail_room_memory": f"a teenage boy's bedroom in {FLAT}: a study desk with school books, a grey quilted mattress, soft curtains, the door open to a warm-lit corridor",
    "saba_room": "a small neat girl's bedroom in a ninth-floor family apartment in Male' late at night: a single quilted mattress with a white padded headboard, fairy lights along a small shelf, a window with sheer curtains and distant city lights",
    "classroom": "a bright A-level classroom in a Male' secondary school in the morning: rows of simple wooden desks and chairs, a plain green board with nothing written on it, tall windows with louvres, sunlight and the leaves of a breadfruit tree outside",
    "school_street": "a narrow sunny street outside the white school wall and gate in Male', parked motorbikes along the wall, a small leafy tree, pastel apartment buildings, a few passers-by",
    "lane": "a narrow busy Male' street in midday sunshine, pastel apartment buildings with balconies, parked motorbikes, a few potted plants and palms, small shops with plain unlettered awnings",
    "cafe": "a small bright modern cafe in Male' at midday: light wooden tables, rattan chairs, a counter with glass jars, plants, large windows to a sunny street, no signage or menus with writing",
    "penthouse": "the spacious living and dining room of a modern Male' penthouse in the morning: floor-to-ceiling windows over the turquoise lagoon, a long dining table, a grey sofa, indoor plants, the front door at the side",
    "building": "a quiet Male' residential street in the late afternoon outside the entrance of a tall white apartment building with a glass door, parked motorbikes, a black family car pulling away down the street",
    "seawall": "the Male' seawall promenade by the artificial beach at sunset: a long wall of large grey coral-stone breakwater blocks along the sea, a small wooden coconut cart with a pile of green king coconuts nearby, palm trees, the open sea stretching to the horizon",
}
MOOD = {
    "sana_room": "late night, the single warm amber bedside lamp against deep indigo-blue shadows, moonlight through the sheer curtains, hushed, heavy grief",
    "scarf": "late night, a thin silver of moonlight and a faint warm lamp glow on the folded scarf, deep blue shadows, still and aching",
    "memory_couple": "soft hazy dreamlike memory glow, warm golden evening light, gentle sea breeze, carefree married happiness",
    "lail_room": "near midnight, the room dark blue, moonlight and city glow through the window, the cool soft glow of a phone, lonely and quiet",
    "lail_room_memory": "soft hazy dreamlike memory glow, warm amber lamplight, tender and aching",
    "saba_room": "late night, the warm glow of fairy lights and the soft cool glow of a phone, moonlit blue window, shy and tender",
    "classroom": "bright tropical morning sunlight through the windows, cheerful school day, quiet undercurrent of sympathy",
    "school_street": "bright tropical midday sunshine, clear blue sky, crisp shadows, light nervous excitement",
    "lane": "bright tropical midday sunshine, clear sky, warm busy city, playful shyness",
    "cafe": "bright midday light through big windows, cool airy cafe, relaxed and warm",
    "penthouse": "bright morning sunlight over the lagoon, calm, life slowly resuming after grief",
    "building": "late afternoon, warm golden sunlight, long soft shadows, clear sky, secret excitement",
    "seawall": "sunset, warm amber and rose-gold sky fading into soft blue over the sea, gentle breeze, light waves, romantic and innocent",
}

HAIZUM_HOME = "Haizum at home in a plain charcoal long-sleeved shirt and dark trousers, his trimmed beard with grey flecks"
LAIL_SCHOOL = "Lail in a white short-sleeved school shirt and dark-navy long trousers"
SABA_SCHOOL = "Saba in a white long-sleeved school tunic, navy ankle-length skirt and white hijab fully covering her hair and neck"
NO_TEXT_PHONE = "the phone screen shows only a soft glow, nothing readable"

BEATS = [
    # ---------------- night of grief in Sana's room ----------------
    dict(to=3, reason="episode opening: Lail opens the door of his late mother's room and finds his father weeping", chars=["haizum", "lail_young"], loc="sana_room",
         visual=f"{HAIZUM_HOME}, sitting on the edge of the quilted mattress in the lamplit room, hurriedly wiping tears from his eyes with both hands, turning his face towards the door; in the half-open doorway on the left stands seventeen-year-old Lail in his light-grey t-shirt and jeans, one hand on the door handle, looking at his father with sad worried eyes",
         camera="medium wide, eye level, faces in the upper half, the carpet in soft shadow as the lower third", amb="apartment_quiet_night",
         sens="other", safe="narration says the father was lying on the bed staring at the ceiling: shown sitting on the edge of the mattress (bible: sitting, not lying)"),
    dict(to=8, reason="action change: Lail sits beside his father, who strokes his head and consoles him", chars=["haizum", "lail_young"], loc="sana_room",
         visual=f"{HAIZUM_HOME}, sitting side by side with his teenage son Lail on the edge of the quilted mattress; Haizum's hand resting tenderly on the back of Lail's head, his own eyes glistening with tears as he speaks softly; Lail looking down, his eyes red, a tear on his cheek; warm lamp glow on their faces",
         camera="medium two-shot, eye level, faces in the upper half, their knees and the carpet as a calm lower third", amb="apartment_quiet_night",
         sens="other", safe="narration says Lail lay down beside his father: shown sitting side by side (no lying down)"),
    dict(to=11, reason="detail image after a long held moment: the mother's folded scarf, the lap he can never rest on again", loc="scarf",
         visual="a neatly folded ivory headscarf resting on the seat of a wooden armchair by the dark window, a thin line of moonlight across it, a small framed photo on the side table blurred beyond recognition, no people",
         camera="close-up still life, the scarf and chair in the upper two-thirds, the dark floor below", amb="apartment_quiet_night",
         sens="other", safe="the mother's absence shown as her folded scarf on an empty chair"),
    dict(to=13, reason="character enters: Laira comes in and sits on her father's other side", chars=["laira", "haizum", "lail_young"], loc="sana_room",
         visual=f"Laira, nineteen, in her dusty-pink dress and dove-grey hijab fully covering her hair and neck, standing in the half-open doorway of the lamplit room, eyes red and sad, one hand lifted to her cheek; in the middle ground {HAIZUM_HOME}, and teenage Lail sitting side by side on the edge of the quilted mattress, both looking up at her with tender sorrowful faces",
         camera="medium wide, eye level, three faces in the upper half, the carpet as the lower third", amb="apartment_quiet_night",
         sens="other", safe="narration says she lay down beside him: shown sitting"),
    dict(to=17, reason="emotional turning point: 'Don't bring us another mother' — he promises and holds both children close", chars=["haizum", "laira", "lail_young"], loc="sana_room",
         visual=f"{HAIZUM_HOME}, sitting between his two children with one arm around each of their shoulders, pulling them close to his sides, his tearful face resolute as he makes a promise; Laira in her dove-grey hijab and dusty-pink dress leaning her head towards his shoulder, crying quietly; teenage Lail on his other side with red eyes; all three fully dressed, the lamp glowing warm",
         camera="medium shot, eye level, the three faces in the upper half, their laps and the carpet in soft shadow below", amb="apartment_quiet_night"),
    dict(to=20, reason="memory: Sana as she used to be — gentle and loving — and the couple's happy married life", chars=["haizum", "sana"], loc="memory_couple",
         visual="a younger Haizum, about 38, beard fully black, in a light-blue casual shirt, and his wife Sana, about 30, in her sage-green dress and ivory hijab fully covering her hair and neck, standing side by side at a balcony railing at golden hour, his hand resting gently on her shoulder; Sana laughing warmly at something he said, her eyes kind and bright; two cups of tea on a small table beside them",
         camera="medium shot, eye level, faces in the upper half, the balcony floor and railing as a calm lower third", amb="memory",
         transition="dissolve"),
    dict(to=23, reason="return to the present: Haizum closes his eyes, tears run down; all three weep silently", chars=["haizum"], loc="sana_room",
         visual=f"head-and-shoulders portrait of {HAIZUM_HOME}, alone in the frame, the only person in the image, sitting in the lamplit room with his eyes closed and his head slightly bowed, a single tear on his cheek, a quiet sorrowful face; soft warm lamp glow on one side of his face, deep blue shadow on the other; no other people",
         camera="close-up, eye level, his face in the upper half, his shoulders and the children soft below", amb="apartment_quiet_night",
         transition="dissolve"),
    dict(to=24, reuse="beat_003", reason="Haizum gazes around the room full of Sana's sweet and bitter memories (return to the scarf detail)", loc="scarf",
         visual="(reuse)", amb="apartment_quiet_night"),
    # ---------------- Lail's room, near midnight ----------------
    dict(to=26, reason="location change: Lail goes to his own room near midnight", chars=["lail_young"], loc="lail_room",
         visual="seventeen-year-old Lail in his light-grey t-shirt and jeans standing just inside the door of his dark bedroom, one hand still on the door frame, looking emptily around the quiet room lit only by moonlight and city glow, his eyes red, shoulders heavy",
         camera="medium wide from inside the room, his face in the upper third, the dark floor as the lower third", amb="room_night"),
    dict(to=28, reason="imagined memory: Mum coming in smiling with something to eat, tidying, tucking the blanket", chars=["sana"], loc="lail_room_memory",
         visual="Sana in her sage-green dress and ivory hijab fully covering her hair and neck, stepping through the open bedroom door with a warm motherly smile, carrying a small plate of food and a glass of milk, a folded blanket over her arm, glancing around the tidy room with love",
         camera="medium shot, eye level, her face in the upper third, the floor softly lit below", amb="memory",
         transition="dissolve", sens="other", safe="Lail's imagining of his late mother shown as a warm hazy memory of her in good health"),
    dict(to=30, reason="return to the present: Lail sits sleepless, chin on hand; the phone on the desk lights up", chars=["lail_young"], loc="lail_room",
         visual="seventeen-year-old Lail sitting on the edge of his grey quilted mattress, one elbow on his raised knee and his chin resting in his hand, tears gathering in his eyes, staring into the dark; across the room on the study desk a phone on its charger has just lit up with a soft glow, nothing readable",
         camera="medium wide, eye level, his face in the upper half, the dark floor as the lower third", amb="room_night",
         transition="dissolve"),
    dict(to=34, reason="action change: he picks up the phone, reads Saba's messages, and a faint smile appears", chars=["lail_young"], loc="lail_room",
         visual=f"seventeen-year-old Lail sitting up against the grey padded headboard with his knees raised, holding his phone in both hands, its soft glow on his face, a faint smile breaking through his wet tired eyes; {NO_TEXT_PHONE}; moonlit window behind him",
         camera="medium close-up, eye level, his face in the upper half, the quilt over his knees as a soft lower third", amb="room_night",
         sens="other", safe="narration says he lay down on the bed: shown sitting up against the headboard"),
    # ---------------- the late-night chat and call ----------------
    dict(to=36, reason="character and location change: Saba alone in her room, texting him", chars=["saba_young"], loc="saba_room",
         visual=f"seventeen-year-old Saba in her powder-blue long-sleeved dress and white hijab fully covering her hair and neck, sitting up against the white padded headboard with a light quilt over her knees, holding her phone in both hands and typing, a small worried caring look on her face lit by the phone glow; {NO_TEXT_PHONE}; fairy lights glowing softly behind her",
         camera="medium close-up, eye level, her face in the upper half, the quilt as a calm lower third", amb="room_night",
         sens="other", safe="girl at night shown sitting up fully dressed in hijab; no readable chat"),
    dict(to=39, reuse="beat_012", reason="cross-cut back to Lail texting: 'someone stole my sleep... can I call?'", loc="lail_room",
         visual="(reuse)", amb="room_night"),
    dict(to=43, reason="action change: the phone call — Lail by his window with the phone at his ear, smiling", chars=["lail_young"], loc="lail_room",
         visual="seventeen-year-old Lail sitting on the wide window ledge of his dark bedroom, phone held to his ear, a soft shy smile on his lips and a new light in his eyes, looking out at the moonlit Male' skyline and the dark lagoon; his reflection faint in the glass",
         camera="medium shot from the side, his face in the upper third, the window ledge and dark room as the lower third", amb="room_night"),
    dict(to=47, reason="character change: Saba on the other end, blushing, her hand over her cheek", chars=["saba_young"], loc="saba_room",
         visual="seventeen-year-old Saba in her powder-blue dress and white hijab fully covering her hair and neck, sitting up against the white headboard with the phone at her ear, her free hand pressed to her blushing cheek, eyes lowered, a shy embarrassed smile; fairy lights glowing behind her",
         camera="close-up, eye level, her face in the upper half, the quilt soft below", amb="room_night"),
    dict(to=50, reuse="beat_015", reason="cross-cut back to Lail teasing and reciting a verse", loc="lail_room",
         visual="(reuse)", amb="room_night"),
    dict(to=53, reuse="beat_016", reason="cross-cut back to Saba: 'I'm hanging up now' — goodnight", loc="saba_room",
         visual="(reuse)", amb="room_night"),
    dict(to=57, reason="framing change: after the call, the hearts — Lail beaming at the glowing phone", chars=["lail_young"], loc="lail_room",
         visual=f"close-up of seventeen-year-old Lail sitting up against his grey headboard, holding the glowing phone close to his chest with both hands and beaming with a wide happy smile, eyes shining, head tilted back slightly; a tiny soft red heart-shaped glow on the screen, {NO_TEXT_PHONE}; moonlight on the window",
         camera="close-up, eye level, face in the upper half, his hands and phone in the middle, the quilt soft below", amb="room_night",
         sens="intimacy", safe="narration says he kissed the phone and lay down: shown smiling at the glowing phone held to his chest, sitting up"),
    # ---------------- school, two days later ----------------
    dict(to=59, reason="time jump and location change: two days later, classmates offer condolences in class", chars=["lail_young"], loc="classroom",
         visual=f"{LAIL_SCHOOL}, seventeen, standing by his wooden desk in the sunny classroom, giving a small grateful smile; around him at a respectful distance three classmates without names — two boys in white school shirts and a girl in a white school tunic and white hijab — looking at him with sympathy",
         camera="medium wide, eye level, faces in the upper half, desk tops as the lower third", amb="classroom",
         transition="black"),
    dict(to=61, reason="characters enter: Asil, Shahid, then Saba with Sadhee; Lail's gaze stops on Saba", chars=["lail_young", "saba_young", "asil_young", "sadhee_young"], loc="classroom",
         visual=f"seen from behind Lail's desk: {LAIL_SCHOOL} seated, turned towards the classroom door; through the door come curly-haired Asil in a white school shirt and a slim boy in a white school shirt, and behind them Saba in a white long-sleeved school tunic, navy ankle-length skirt and white hijab, chatting with Sadhee in the same school uniform with a cream hijab; Saba glances at Lail with a faint secret smile",
         camera="medium wide, eye level, faces in the upper half, desk tops as the lower third", amb="classroom"),
    dict(to=63, reason="focus change: free period — Saba secretly shows Lail's message to Sadhee", chars=["saba_young", "sadhee_young"], loc="classroom",
         visual=f"{SABA_SCHOOL}, sitting at her desk, tilting her phone towards her friend Sadhee beside her (white school tunic, navy skirt, cream hijab), both leaning in, Sadhee's eyes wide with a teasing grin, Saba biting back a shy smile; {NO_TEXT_PHONE}; sunlight through the louvred windows",
         camera="medium close two-shot, eye level, faces in the upper half, the desk top as the lower third", amb="classroom"),
    dict(to=66, reason="location change: outside the school, Saba crosses the road to Lail", chars=["lail_young", "saba_young"], loc="school_street",
         visual=f"{LAIL_SCHOOL}, standing by the white school wall on a sunny Male' street with his hands in his pockets, smiling; {SABA_SCHOOL}, having just crossed the narrow road, stopping an arm's length away from him with her school bag on her shoulder, asking a curious question; a clear gap between them",
         camera="medium wide, eye level, faces in the upper half, the sunny road as the lower third", amb="city_day"),
    dict(to=69, reason="action change: walking together, both phones ring at once and they show each other the screens", chars=["lail_young", "saba_young"], loc="lane",
         visual=f"{LAIL_SCHOOL} and {SABA_SCHOOL}, walking side by side an arm's length apart along a sunny Male' street, both holding up ringing phones and turning the glowing screens towards each other, laughing; {NO_TEXT_PHONE}",
         camera="medium wide from the front, eye level, faces in the upper half, the street as the lower third", amb="road_busy"),
    dict(to=71, reason="location change: they go into a cafe and sit down to talk", chars=["lail_young", "saba_young"], loc="cafe",
         visual=f"{LAIL_SCHOOL} and {SABA_SCHOOL}, sitting opposite each other across a small light wooden table in a bright cafe, two tall glasses of iced fruit juice with straws between them, chatting and smiling easily, their hands on their own sides of the table",
         camera="medium shot from the side, eye level, faces in the upper half, the table top as the lower third", amb="cafe"),
    dict(to=73, reason="location and character change: back in class separately, friends tease Lail with questions", chars=["lail_young", "asil_young", "shahid_young"], loc="classroom",
         visual=f"{LAIL_SCHOOL}, seated at his desk with an innocent shrug and a poker face; curly-haired Asil in a white school shirt and Shahid in a white school shirt leaning over his desk from both sides, grinning and firing questions at him; in the soft background Saba in a white school tunic and white hijab at her own desk, pretending to read",
         camera="medium shot, eye level, faces in the upper half, the desk top as the lower third", amb="classroom"),
    # ---------------- days pass ----------------
    dict(to=76, reason="time jump montage: Haizum back to the office, Laira looks at universities, Maama Shafeeqa moves in", chars=["haizum", "laira", "shafeeqa"], loc="penthouse",
         visual="a sunny morning in the penthouse: Haizum in his navy suit and white open-collar shirt heading towards the front door with a briefcase; Laira in her dusty-pink dress and dove-grey hijab sitting at the long dining table with an open laptop facing away from the viewer; grandmother Shafeeqa in her maroon libaas, white headscarf and gold glasses just arriving through the door with a small wheeled suitcase, smiling warmly at the family",
         camera="wide shot, eye level, faces in the upper half, the polished floor as the lower third", amb="apartment_morning",
         transition="black"),
    dict(to=77, reuse="beat_015", reason="montage: Lail and Saba's calls and messages grow day by day (return to Lail on the phone at night)", loc="lail_room",
         visual="(reuse)", amb="room_night"),
    # ---------------- the secret meeting at the seawall ----------------
    dict(to=79, reason="time and location change: another day — Lail sends the car away outside Asil's building and Saba comes down", chars=["lail_young", "saba_young"], loc="building",
         visual="seventeen-year-old Lail in his light-grey t-shirt and jeans standing on the pavement outside the glass entrance of a tall white apartment building, looking up from his phone with a smile as the black car drives away behind him; Saba in her powder-blue long-sleeved dress and white hijab fully covering her hair and neck stepping out through the glass door a few steps away, smiling shyly",
         camera="medium wide, eye level, faces in the upper half, the pavement as the lower third", amb="city_day",
         transition="black"),
    dict(to=82, reason="location change: the seawall at sunset — Saba sits on the wall, Lail buys a coconut from the cart", chars=["saba_young", "lail_young"], loc="seawall",
         visual="Saba in her powder-blue dress and white hijab sitting on the big grey breakwater stones of the seawall, facing the sunset sea, looking back over her shoulder; a few steps away teenage Lail in his light-grey t-shirt and jeans standing at a small wooden coconut cart, receiving a green king coconut from an elderly cart man in a faded shirt",
         camera="wide shot, eye level, faces in the upper half, the stones and pavement as the lower third", amb="seawall_dusk"),
    dict(to=85, reason="action change: one coconut for the two of them — she sips, he sips from the same straw; her shy smile", chars=["saba_young", "lail_young"], loc="seawall",
         visual="Saba and teenage Lail sitting on the seawall stones facing the sea with a full arm's length between them, a single green king coconut with one straw resting on the stone between them; Saba with a shy embarrassed smile, eyes lowered; Lail grinning mischievously at her; nobody touching; the sunset sky glowing behind",
         camera="medium two-shot from the side, faces in the upper half, the stones and coconut as the lower third", amb="seawall_dusk",
         sens="intimacy", safe="sharing one straw is shown only as a single coconut resting on the wall between them, arm's length apart, no touching"),
    dict(to=90, reason="framing change: 'Are we really just friends?' — Lail turns to her, she shrugs", chars=["lail_young", "saba_young"], loc="seawall",
         visual="teenage Lail sitting sideways on the seawall stones, turned towards Saba with a playful questioning smile; Saba, an arm's length away in her powder-blue dress and white hijab, holding the green coconut on her lap with both hands, giving a pretend-innocent shrug and looking away towards the sea, biting back a smile",
         camera="medium shot over Lail's shoulder, Saba's face in the upper half, the stones as the lower third", amb="seawall_dusk"),
    dict(to=94, reason="emotional turning point: his poem and deep gaze — her heart races, a blushing smile", chars=["saba_young", "lail_young"], loc="seawall",
         visual="close-up of Saba in her white hijab, a deep shy blush on her cheeks, a small trembling smile, eyes lowered; in the soft-focus foreground the side of teenage Lail's face gazing at her intently; warm sunset light on her face",
         camera="close-up, eye level, her face in the upper half, the sunset sea soft below", amb="seawall_dusk"),
    dict(to=98, reason="framing change: she looks away to the wide blue sea; 'you're so good with poems' — 'it's my own'", chars=["lail_young", "saba_young"], loc="seawall",
         visual="wide shot from behind: the two small figures of teenage Lail and Saba (white hijab, powder-blue dress) sitting on the long seawall an arm's length apart, facing the wide sea under a glowing rose-gold sunset sky, Saba looking out to the horizon, Lail turned towards her",
         camera="wide shot from behind, the sky and sea filling the upper two-thirds, the grey stones as the lower third", amb="seawall_dusk"),
    dict(to=101, reuse="beat_033", reason="return to her blushing close-up as he recites another verse", loc="seawall",
         visual="(reuse)", amb="seawall_dusk"),
    dict(to=105, reason="emotional turning point (cliffhanger): Saba looks into his eyes — 'they look like my little brother's, Ali Laith Haizum'", chars=["saba_young", "lail_young"], loc="seawall",
         visual="Saba in her white hijab sitting on the seawall, turned towards teenage Lail and looking straight into his eyes with a gentle, earnest, tender expression as she speaks softly; Lail an arm's length away in the soft-focus foreground, in profile, his smile fading into a flicker of surprise; the last golden light of the sunset on their faces",
         camera="medium close-up over Lail's shoulder, Saba's face in the upper half, the sea soft below", amb="seawall_dusk"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "After opening the door of Sana's room, Lail went inside. At that moment his father was lying on one side of the bed,",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -18)])
sh(2, "his right arm resting on his forehead, staring up at the ceiling. At the sound of the door opening, Haizam looked towards it and hurriedly wiped the tears from his eyes with both hands.")
sh(3, "Lail sensed that his father had been crying. 'My son,' Haizam called. Lail came in and lay down on his father's other side.")
sh(4, "'I miss Mum so much,' Lail said softly. Haizam lovingly stroked Lail's head. 'My son, this is the reality of the world.")
sh(5, "Mum went because her appointed time had come. Whatever the reason, when the time comes one has to go. Just as one cannot go before the time comes, however much one wants to,")
sh(6, "when the time comes it cannot be refused either. One has to say farewell to the world.' Though Haizam's voice was calm, at that moment his own eyes filled with tears.",
   [("sob_breath", "ކަރުނުން", -24)], hum=True)
sh(7, "Lail wiped away the tears falling from his father's eyes. 'Is Dhontha asleep?' Haizam asked. 'I don't know,' Lail answered.")
sh(8, "'You have to go to school next week, you know. You mustn't interrupt your studies. If Mum knew you weren't going to school, she would be very sad.'")
sh(9, "Haizam advised him. Lail lay silent, saying nothing. Though memories of his beloved mother kept coming back,")
sh(10, "the blessing of resting his head on his mother's tender lap was now lost. With that, tears began streaming from his eyes once more.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(11, "While his friends were close by he had found a little comfort, but once they left, that emptiness filled his heart again and his eyes brimmed with tears.")
sh(12, "As father and son lay there in that heartbreaking moment, the door opened and Laira came in. She came and lay down at Haizam's side.",
   [("door_open", "ހުޅުވާލާފައި", -20)])
sh(13, "Haizam lovingly stroked Laira's head too. 'Bappa,' Laira called, wiping her tear-filled eyes. 'What is it, my child?'")
sh(14, "Haizam asked, stroking Laira's head. 'Bappa, please don't bring us another mother, okay?' Laira said in a tearful voice, lying where she was. 'I won't.",
   [("sob_breath", "ރޮވިފައިވާ", -24)])
sh(15, "I will never give your mother's place to anyone else,' Haizam reassured them, lovingly holding both children close.",
   [("cloth_rustle", "ބައްދާލަމުން", -24)], hum=True)
sh(16, "For the sake of those beloved children too, he had no wish to bring another partner into his life.")
sh(17, "Now he alone was both mother and father to those children. It was certain he could never again feel for any other human being the noble love he had felt for Sana.")
sh(18, "He knew, too, the deep love Sana held for him in her heart. The change in Sana's temperament, the stubbornness and short temper that took root in her — their real cause was Haizam himself.")
sh(19, "It was the bitter result of the one mistake he had made. In the past Sana had never had such a temperament. She was a gentle,")
sh(20, "kind, matchless young woman whose speech was full of love and grace. That couple had lived an immensely happy, loving life.")
sh(21, "But who knows whose evil eye fell upon that happy life. Haizam closed his eyes. At that moment, from his tear-filled eyes,")
sh(22, "hot tears spilled over his lashes and ran down his cheeks. All three of them were weeping in Sana's memory.",
   [("sob_breath", "ކަރުނަތިކިތައް", -24)], hum=True)
sh(23, "Though no sound of sobbing escaped, each of them kept secretly wiping away the tears falling from their eyes.")
sh(24, "Haizam cast his gaze around the room. The whole atmosphere was filled with Sana's sweet and bitter memories. Parted from those memories,")
sh(25, "how could they ever move away? Lail went to his room as it was nearing midnight,")
sh(26, "after spending time with his father and sister reliving memories of Mum. It was still hard for Lail's heart to accept that such a loving mother was gone.")
sh(27, "It felt as if any moment now Mum would walk into the room and tidy things up. Or come in smiling, carrying something for Lail to eat.")
sh(28, "Or check whether he was asleep, spread the blanket over him and tuck it around his feet.")
sh(29, "Lail sat at the edge of the bed, his elbow on his knee and his chin resting in his hand.")
sh(30, "Tonight again, memories of Mum had chased the sleep from his eyes. As tears gathered in his eyes, the screen of his phone lying on the study desk lit up.",
   [("phone_buzz", "ދިއްލިގެން", -20)])
sh(31, "A message had come. Lail could guess whose message it was. Wiping his tears, he got up, went over and picked up the phone.",
   [("cloth_rustle", "ތެދުވެގެން", -24)])
sh(32, "The phone was on the charger. When he unplugged it and looked, there were six messages from Saba and one from Asil.")
sh(33, "After sending Asil a short reply, he came back reading Saba's messages and lay down on the bed. With that, a faint smile came to his lips.")
sh(34, "Though his eyes were wet, Saba's messages brought his heart a coolness and a calm that is hard to describe.")
sh(35, "'When you didn't reply, I thought you'd fallen asleep.' He saw the message Saba had sent. 'No, I've just come from sitting with Bappa and Dhontha.")
sh(36, "Besides, tonight sleep has become a stranger to my eyes. Because Mum's gone...' Lail typed and sent. 'Because Mum's gone. And?'",
   [("phone_game_taps", "ޓައިޕްކޮށް", -22)])
sh(37, "Saba asked. 'And... because someone has stolen my sleep,' Lail wrote. 'Oh...' Saba replied. 'Are you alone?'")
sh(38, "Lail asked. 'Hmm, I've just got into bed to sleep,' Saba said. 'Can I call?' Lail asked. 'At this hour? Is something wrong?'")
sh(39, "Saba asked. 'Just to talk. If Saba doesn't mind,' Lail said. 'Okay...' As soon as Saba agreed,")
sh(40, "Lail called Saba's number straight away. Saba picked up on the first ring. 'Hi.' Saba's soft voice came through. 'Hi,'",
   [("phone_buzz", "ރިންގާއެކު", -20)])
sh(41, "Lail said too. After that, as if neither knew what to say, a silence settled over everything. As a faint smile played on Lail's lips,")
sh(42, "an unusual liveliness showed in his eyes. 'Tonight you said something about a pen and a tongue, didn't you?' Saba asked, breaking the silence.")
sh(43, "'When? I don't remember,' Lail said in a careless tone. 'Oh, then never mind,' Saba said.")
sh(44, "'Heart, soul, tongue and pen all turn against me, unable to say it... how fond I've grown of your innocence, when I stop to say it with love.' Lail said softly. 'What did you say?'")
sh(45, "Saba asked. 'Let me guess? Right now your face must have turned a soft onion-skin pink from blushing, hasn't it?'")
sh(46, "Lail said, letting a smile spread across his lips. But no sound came from the other end. 'I know Saba...'")
sh(47, "Lail broke off the sentence he was about to say. 'What about Saba?' Saba asked. 'Saba loves me, right?' Lail asked teasingly. 'No...'")
sh(48, "Saba said quickly. 'Then why did you talk about my photo tonight?' Lail asked. 'I didn't talk about it.")
sh(49, "I only said it was a really beautiful smile,' Saba said in her own defence. 'Thank you!' Lail said. 'For what?'")
sh(50, "Saba wanted to clear up the confusion. 'When ink turns to breath the pen begins to dance to my heartbeat; the diary I write is nearly full, when I stop to hear your praise.'")
sh(51, "Lail recited a verse. 'I'm hanging up now,' Saba said, embarrassed. 'What happened? Don't you like the way I talk?'")
sh(52, "Lail asked. 'No, but...' Saba could not finish her sentence. 'All right. Wishing you a happy night, goodnight.'")
sh(53, "Lail said. 'Goodnight,' Saba said too. As soon as he hung up, Lail quickly wrote a message.",
   [("phone_game_taps", "ލިޔެލިއެވެ", -22)])
sh(54, "'Sorry if I said anything that upset you. But Saba really is that beautiful. That's why I praise you.' Lail sent the message.")
sh(55, "'Lail is very handsome too, especially those two eyes.' The reply came from Saba. When he saw that message, Lail's face lit up. 'Good night.'",
   [("phone_buzz", "ޖަވާބު", -22)])
sh(56, "Lail wrote, and sent a red heart with the message. In the message Saba sent back there was a heart too.")
sh(57, "With that, Lail's smile grew wider than before. Lovingly kissing the phone, he put it aside,", hum=True)
sh(58, "and lay down on the bed at peace. Two days later. Lail came to class a little earlier than usual.")
sh(59, "His friends came and shared his grief over his mother's passing, offering condolences. Thanking them with a smile, he went and sat down at his desk.")
sh(60, "Just then Asil and Shahid were also coming into the class. When he saw Saba coming in behind them, chatting with Sadhee, Lail's gaze stopped on her.")
sh(61, "On seeing Lail, a faint smile came to Saba's lips too. When Saba went and sat at her desk, Lail pretended not to notice and turned away.")
sh(62, "As soon as the class had a free period, Lail texted Saba and hurried outside. After secretly reading the message to Sadhee,",
   [("footsteps_pavement", "ނުކުތެވެ", -24)])
sh(63, "Saba too set off for the place Lail had named. By then Lail was standing outside the school. After looking both ways, Saba")
sh(64, "crossed the road and went over to Lail. 'Why did you ask me to come here?' Saba asked, stopping. 'Nothing really... I thought you wouldn't come.'",
   [("motorbike_pass", "ހުރަސްކޮށް", -22)])
sh(65, "Lail said as he started walking. 'Are we going somewhere?' Saba asked again. 'I thought we could go and eat something since it's break time.")
sh(66, "If Saba doesn't want to, we can go to the canteen too,' Lail said. 'No, whatever Lail wants,' Saba replied. Without saying a word,")
sh(67, "the two walked on together. As they went, now and then they glanced at each other and smiled. At that moment both their phones started ringing at once.",
   [("phone_buzz", "ރިންގުވާން", -18)])
sh(68, "When they looked, it was Asil calling Lail. Sadhee was calling Saba. After showing each other their phone screens, they cut the calls.")
sh(69, "'Asil teases so much,' Saba said as they walked. 'Me too,' Lail said. 'But why you?' Saba asked.")
sh(70, "'Why you?' Lail asked the very same question back. Saba shrugged. Talking all the way, the two went into a cafe that sells cold drinks.",
   [("door_open", "ކެފޭއަކަށެވެ", -24)])
sh(71, "After placing their order, they sat down at a table and began sharing the ordinary things of life with each other.")
sh(72, "When the order came, they ate and drank, then went back to class separately to escape their friends' teasing. Even so,",
   [("cup_clatter", "ކައިބޮއެ", -22)])
sh(73, "their friends noticed and began firing all sorts of questions at them. Yet neither of them admitted they had gone out together.")
sh(74, "The days passed in their swift run, adding pages to the book of life. Haizum, too, began going out to the office as before.")
sh(75, "While Laira was looking at universities for her higher studies, Shafeeqa moved into Haizum's house.")
sh(76, "That was to look after the children during those days, after renting out her own house to some of her own people.")
sh(77, "Lail and Saba's phone calls and messages grew day by day. And meeting secretly, hidden from their friends, became an ordinary thing.")
sh(78, "Today was another such day. Lail went home, changed his clothes and went out with his driver. Reaching Asil's family's house,",
   [("car_door", "ޑްރައިވަރާ", -22)])
sh(79, "he sent the car away and, without going up, texted Saba. In a little while Saba came down.",
   [("car_drive_off", "ފޮނުވައިލުމަށްފަހު", -20)])
sh(80, "Talking as they walked along the road, they came out to the shore, and Saba sat down on the seawall.",
   [("footsteps_pavement", "ހިނގާފައި", -24), ("wave_crash", "އަތިރިމައްޗަށް", -22)])
sh(81, "Lail stopped by a cart nearby. After paying the cart man, Lail came and, on the seawall,")
sh(82, "sat down next to Saba, looking out at the sea. Then, taking the king coconut the cart man brought, Lail held it out to Saba.",
   [("wave_crash", "މޫދާ", -24)])
sh(83, "When the man had gone, Saba looked at Lail's face and asked, 'Where's your coconut?' 'This... I brought just one, for the two of us.'")
sh(84, "Lail said with a mischievous smile. 'Then where's the straw?' Saba asked, taking a sip from the coconut.")
sh(85, "At that very moment Lail took the straw from Saba's hand and took a sip of the coconut water from it too. A shy smile showed on Saba's face.")
sh(86, "'Hmm... can I ask you something? Are we really just friends?' Lail asked, looking at Saba's face.")
sh(87, "Saba shrugged, pretending not to know. 'Did Lail ask to be friends? I didn't hear anything,' Saba said, taking another sip of coconut water.")
sh(88, "'Wait... you didn't hear me ask to be friends?' Saba nodded as if to say yes. 'Then what is this?")
sh(89, "Meeting in hiding from our friends, messaging till late into the night, staying on the phone? Even I don't know where I stand now.'")
sh(90, "Lail said playfully, looking at Saba's face. Even then a mischievous smile played on his lips.")
sh(91, "Saba shrugged again as if she didn't know. 'Tell me you love me, my dear, how my heart longs to hear it; your gaze has carved a place in my heart...")
sh(92, "I want to write my name together with yours; I want to tell you this plea of my heart...' As Lail's deep gaze rested on Saba,")
sh(93, "he recited two verses. With that, a shy, blushing smile spread across Saba's lips.")
sh(94, "As her heart beat with an indescribable force, she herself could not understand the magic in Lail's gaze.",
   [("heartbeat", "ވިންދު", -20)], hum=True)
sh(95, "To steady the trembling of her heart, Saba took her eyes off Lail's face and looked out at the wide blue sea.",
   [("wave_crash", "މޫދާ", -22)])
sh(96, "'Lail is so good at reciting poems,' Saba said gently. A soft laugh came from Lail. 'This isn't someone else's poem.")
sh(97, "This is my very own poem. Every time I see Saba, a new verse is born in my heart,' Lail said, looking straight into Saba's eyes.")
sh(98, "'Oh, stop lying — Lail is so good at making up stories too,' Saba said carelessly, sitting where she was. 'If you don't believe me, there's nothing more I can do.'")
sh(99, "Though Lail said that, he did not take his eyes off Saba's face even a little. And in the same heartfelt way he recited another verse.")
sh(100, "'When ink turns to breath the pen begins to dance to my heartbeat; I've grown so fond of you when I stop to see your innocence. My heart is lost when I see you, standing there so far away,")
sh(101, "even if it comes to mind, I cannot find the words to say it.' Lail's poetic words made Saba even shyer.")
sh(102, "'I don't really understand the meaning of what you recite. But the way Lail recites it does things to my heart I can't explain.")
sh(103, "Shall I tell you something that's on my mind too?' Saba asked. 'Hmm... tell me,' Lail answered, still sitting looking at Saba.")
sh(104, "'Lail's eyes are very beautiful. Lail's eyes look so much like my little brother's. His name is Ali Laith Haizum.'",
   [("heartbeat", "ޙައިޒުމް", -20)], hum=True)
sh(105, "Saba said very softly, sitting there looking into Lail's eyes.", hum=True)
SHOTS = S

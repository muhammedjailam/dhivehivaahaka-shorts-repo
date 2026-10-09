"""Beat/shot plan for Mamma episode 458 (used by plan_beats.py)."""

LOC = {
    "porch_joali": "the front porch (askani) of Azeeza's comfortable older two-storey Malé townhouse: a wooden joali seat (a Maldivian woven-net seat on a dark wooden frame) under the porch roof, a warm porch lamp on the pale wall, a tiled front yard with potted plants and a parked motorbike inside a white gate, the narrow street and tall pastel buildings beyond the gate",
    "shahula_room": "Shahula's small neat room in Azeeza's Malé townhouse: a single bed with a plain pale bedspread, a little wooden cupboard with a folded prayer mat on top, a small study desk with a lamp, a wooden window with a pale curtain, the wooden door of the room",
    "azeeza_bedroom": "Azeeza's bedroom in the Malé townhouse: a large dark wooden bed with white pillows and a soft cream bedspread, a wooden dresser with a mirror, framed pictures of flowers on the pale wall, a warm bedside lamp",
    "yard_gate_night": "the tiled front yard of Azeeza's Malé townhouse at night: potted plants, the white gate open onto the narrow street, tall pastel buildings, motorbikes parked along the walls, a warm streetlight",
    "male_street_night": "a narrow Malé street at night lined with tall pastel buildings and motorbikes parked along the walls, warm amber streetlights and glowing shop windows blurred into soft bokeh",
    "symphony_outside": "the front of a busy modern restaurant on a Malé street at night: a glowing glass frontage with warm pendant lights inside, a few potted palms by the entrance, motorbikes parked along the kerb, no signboard text",
    "symphony_inside": "inside a busy modern Malé restaurant at night: warm hanging pendant lights, dark wood tables, other diners blurred in the background, a table for four set with plates of food, glasses of juice and water",
    "corridor_night": "the dim inner corridor of Azeeza's Malé townhouse at night outside Shahula's room: a pale wall with a small warm wall lamp, Shahula's wooden door standing open with soft light from her room",
    "married_hall": "the sitting room (bodu fendaa) of the Malé townhouse after the marriage: a grey sofa, a low coffee table, a switched-off TV, a dining table at the side, a single standing lamp, heavy curtains",
    "azeeza_bedroom_empty": "Azeeza's bedroom after she is gone: the large dark wooden bed neatly made and empty, a folded cream shawl on it, a closed green cloth-bound book on a small wooden stand on the bedside table, her thin gold-rimmed glasses folded beside it, framed pictures of flowers on the wall",
    "dark_house": "the sitting room (bodu fendaa) of the Malé townhouse in darkness: the grey sofa, the coffee table and the TV in deep shadow, a faint stripe of light falling across the tiled floor from the open kitchen doorway at the back, the front door just opened",
    "marital_bedroom": "the main bedroom of the Malé townhouse at night: a large neatly made bed with a dark-blue bedspread, a wooden wardrobe, a bedside lamp, a closed white side door",
    "hall_confront": "the sitting room (bodu fendaa) of the Malé townhouse at night: the grey sofa facing the main front door, a low coffee table, a single standing lamp throwing hard light and long shadows across the tiled floor",
}
MOOD = {
    "porch_joali": "early night, warm amber porch-lamp light against deep blue shadows, soft and intimate, gentle teasing warmth",
    "shahula_room": "night, warm homely lamplight, soft glow, hopeful and bright",
    "azeeza_bedroom": "night, warm golden bedside-lamp light, soft shadows, tender family moment with an undercurrent of unease",
    "yard_gate_night": "night, warm amber streetlight and porch light, deep blue shadows",
    "male_street_night": "night, streaks of warm amber streetlight and soft bokeh, cool blue shadows, a lonely uncertain mood",
    "symphony_outside": "night, warm golden light spilling from the restaurant glass onto the street, blue night shadows, lively",
    "symphony_inside": "night, warm amber pendant lights, lively busy restaurant atmosphere, soft bokeh",
    "corridor_night": "late night, dim warm wall-lamp light and deep shadows, tense and serious",
    "married_hall": "evening, dim and cold, shadowy, a single lamp, lonely and subdued",
    "azeeza_bedroom_empty": "soft grey early light through the curtain, quiet, still and sorrowful, a soft warm hazy glow on the folded shawl",
    "dark_house": "night, almost dark, deep blue-black shadows, only a faint warm stripe of kitchen light, eerie silence",
    "marital_bedroom": "night, dim bedside lamp, cold shadows, anxious",
    "hall_confront": "night, dim and cold, harsh low lamplight from one side, deep shadows, frightening tension",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear arm's-length gap between them, not touching"
SY = ("teenage Shahula (reference used for her face only; she is now about 19, a young office worker) wearing a loose "
      "long-sleeved ankle-length navy office abaya and a light-grey hijab fully covering her hair and neck, NOT the white school uniform")
SY_PEACH = ("teenage Shahula (reference used for her face only; now about 19) dressed for an evening out in a soft-peach "
            "(pale orange-pink) long-sleeved ankle-length dress and a cream hijab fully covering her hair and neck; her dress is "
            "peach-coloured, NOT white, no school uniform, no navy belt")
A_OFF = "Aamir (reference used for his face only) wearing a light-blue long-sleeved shirt and dark trousers, NOT the white shirt"
A_BLACK = ("Aamir (reference used for his face only) wearing a solid black long-sleeved button shirt and dark trousers; his "
           "shirt is black, NOT white")
AZ = ("Azeeza (reference used for her face and thin gold-rimmed glasses only), ill and resting at home, wearing a loose plain "
      "cream-coloured house dress and a cream hijab fully covering her hair and neck; her dress is cream, NOT green, no emerald abaya")
SW = "Shahula in her loose dusty-rose house dress and cream hijab fully covering her hair and neck, two plain shining gold bangles on her wrist"
SP = SW + ", about seven months expecting, a modest rounded belly under the loose dress"

BEATS = [
    # ---------------- PORCH JOALI, EVENING
    dict(to=3, reason="episode opening: the joali talk continues; she teases him about his long list of girls",
         chars=["shahula_young", "aamir"], loc="porch_joali",
         visual=f"{SY} and {A_OFF} sitting on the two ends of the wooden joali seat on the lamp-lit porch, {GAP}; she glances "
                f"sideways at him with a playful teasing smile, a few blank application papers on her lap; he looks back at her "
                f"amused, one arm resting on the joali frame",
         camera=f"medium two-shot from the front, eye level, {LOW} (porch tiles in soft shadow)", amb="night_exterior",
         sens="intimacy", safe="unmarried pair on the joali shown with a wide gap, no touching"),
    dict(to=5, reason="framing change: Aamir's deep look as he says his heart wants only one person",
         chars=["aamir"], loc="porch_joali",
         visual=f"close-up of {A_OFF}, sitting on the joali and looking off-frame at someone with a deep, warm, meaningful gaze "
                f"and a soft half smile; the warm porch lamp glowing behind him",
         camera=f"close-up, eye level, {LOW} (dark soft-focus porch background)", amb="night_exterior"),
    dict(to=7, reason="action change: she rises from the joali, papers in hand, saying she must go fill her form",
         chars=["shahula_young", "aamir"], loc="porch_joali",
         visual=f"{SY} standing up beside the joali holding a small stack of blank application forms and her handbag on her "
                f"shoulder, smiling brightly and turning toward the front door; {A_OFF} still sitting on the joali looking up at "
                f"her with a puzzled face, {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (porch tiles)", amb="night_exterior"),
    dict(to=10, reason="emotional turning point: her face glows as she speaks of studying Shariah and Law, her mother's dream",
         chars=["shahula_young"], loc="porch_joali",
         visual=f"medium close-up of {SY} holding the blank application form in both hands in front of her, her face radiant "
                f"with joy and hope, big dark eyes shining in the warm lamplight, looking slightly upward as if seeing a bright future",
         camera=f"medium close-up, eye level, {LOW} (the blank form and soft shadow)", amb="night_exterior"),
    dict(to=12, reason="focus change: Aamir alone on the joali, uneasy; he wants a wife who stays home",
         chars=["aamir"], loc="porch_joali",
         visual=f"{A_OFF} sitting alone on the joali, leaning forward with his elbows on his knees, watching someone walk away "
                f"off-frame with a faint frown and narrowed, calculating eyes, his smile gone",
         camera=f"medium shot, slightly low angle, {LOW} (porch tiles)", amb="night_exterior"),
    # ---------------- SHAHULA'S ROOM
    dict(to=15, reason="scene change: in her room she drops her handbag and holds the form close to her heart",
         chars=["shahula_young"], loc="shahula_room",
         visual=f"{SY} standing in her small room beside the single bed where her handbag lies, holding the blank application "
                f"form flat against her heart with both hands, eyes gently closed, a happy hopeful smile",
         camera=f"medium shot, eye level, {LOW} (the plain bedspread and the handbag)", amb="room_night"),
    dict(to=17, reason="character enters: Aamir at her door: 'Mamma is calling'",
         chars=["shahula_young", "aamir"], loc="shahula_room",
         visual=f"{SY} holding her room's wooden door open, looking out questioningly; {A_OFF} standing outside in the doorway, "
                f"a step back, {GAP}, saying something with a calm secret smile",
         camera=f"medium two-shot from inside the room, eye level, {LOW} (the floor in soft shadow)", amb="room_night",
         sens="intimacy", safe="unmarried pair at a doorway with a clear gap; he does not enter"),
    # ---------------- AZEEZA'S ROOM: THE BANGLES
    dict(to=20, reason="scene change: Azeeza sitting up in bed with an old jewellery box, calling Shahula in with unusual joy",
         chars=["azeeza", "shahula_young", "aamir"], loc="azeeza_bedroom",
         visual=f"{AZ} sitting up in her big wooden bed against the pillows with a small old carved wooden jewellery box on the "
                f"bedspread in front of her, beaming and beckoning with one hand; {SY} stepping in through the door toward the bed; "
                f"{A_OFF} just behind her at the door; each person appears only once. Colour check: the lady in bed wears CREAM (not green), "
                f"the young woman wears a DARK NAVY abaya (not white, no belt), the man wears a light-blue shirt",
         camera=f"medium wide shot, eye level, {LOW} (the bedspread and the box)", amb="room_night"),
    dict(to=22, reason="action change: Azeeza seats Shahula beside her and opens the box: two shining gold bangles",
         chars=["azeeza", "shahula_young", "aamir"], loc="azeeza_bedroom",
         visual=f"{AZ} sitting up in bed holding up two plain shining gold bangles taken from the open old jewellery box, smiling "
                f"lovingly; {SY} sitting on the edge of the bed beside her, the box between them, looking at the bangles in "
                f"surprise; {A_OFF} standing at the side of the bed with his hands in his pockets, smiling",
         camera=f"medium shot, eye level, {LOW} (the cream bedspread and the open box)", amb="room_night"),
    dict(to=24, reason="detail: the family heirloom bangles slipped onto Shahula's wrist",
         chars=[], loc="azeeza_bedroom",
         visual="close-up of two women's hands over a cream bedspread: an older woman's hand in a cream long sleeve gently "
                "slipping a plain shining gold bangle onto a young woman's slender wrist in a navy long sleeve; the young hand "
                "hesitant and still; a small old carved wooden jewellery box open beside them, warm lamplight glinting on the gold",
         camera="close-up detail from above, the hands and bangles in the upper two-thirds, the plain bedspread as a calm lower third",
         amb="room_night"),
    dict(to=26, reason="focus change: Aamir's satisfied, contented smile",
         chars=["aamir"], loc="azeeza_bedroom",
         visual=f"medium close-up of {A_OFF}, standing beside the bed, looking down at someone with a quiet, satisfied, "
                f"triumphant smile, chin slightly raised, warm lamplight on his face; he is the only person in the frame, no one else visible",
         camera=f"medium close-up, slightly low angle, {LOW} (soft dark background)", amb="room_night"),
    dict(to=29, reason="emotional turning point: she understands the bangles are a proposal and fears her future",
         chars=["shahula_young"], loc="azeeza_bedroom",
         visual=f"close-up of {SY} sitting on the edge of the bed, two shining gold bangles now on her wrist resting in her lap, "
                f"her eyes closed tightly holding back tears, lips pressed together, a look of quiet pain and fear, the lamplight "
                f"soft on one side of her face; she is the only person in the frame, no second girl, no one in a white uniform anywhere",
         camera=f"close-up, eye level, {LOW} (her hands with the bangles in her lap)", amb="room_night"),
    dict(to=31, reason="back to the three by the bed: 'Shahula, my child, do you agree to this marriage?'",
         reuse="beat_009", chars=["azeeza", "shahula_young", "aamir"], loc="azeeza_bedroom",
         visual="reuse of beat_009", amb="room_night"),
    dict(to=33, reason="action change: Aamir changes the subject, mother and son talk, Shahula forgotten at the side",
         chars=["aamir", "azeeza", "shahula_young"], loc="azeeza_bedroom",
         visual=f"{A_OFF} sitting on a chair beside the bed talking animatedly to {AZ}, who laughs with him; {SY} standing a few "
                f"steps away at the foot of the bed, alone and silent, looking down at the gold bangles on her wrist. Colour check: the lady "
                f"in bed wears CREAM (not green), the young woman a DARK NAVY abaya, the man a LIGHT-BLUE shirt (not white)",
         camera=f"medium wide shot, eye level, {LOW} (the bedspread and the floor)", amb="room_night"),
    # ---------------- MOTORBIKE, NIGHT
    dict(to=35, reason="scene change: outside, Aamir waiting on his motorbike; 'how late you are'",
         chars=["aamir", "shahula_young"], loc="yard_gate_night",
         visual=f"{A_BLACK}, sitting on his parked motorbike at the open white gate, smiling and saying something teasing; "
                f"{SY_PEACH} standing on the tiled yard a step away from the motorbike, silent, not smiling, a small handbag in her "
                f"hand, {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (tiled yard in lamplight)", amb="street_night",
         sens="intimacy", safe="the ride itself is not shown; she stands apart from the bike, no touching"),
    dict(to=39, reason="inner passage: her despair on the ride, no chance to think, a rough sea ahead",
         chars=["shahula_young"], loc="male_street_night",
         visual=f"close-up of {SY_PEACH}, her face turned to the side and lit by passing streaks of amber streetlight, the hijab "
                f"edge fluttering gently in the night wind, eyes empty and lost, deep despair; the blurred Malé street and lights "
                f"behind her",
         camera=f"close-up, eye level, {LOW} (blurred dark street bokeh)", amb="street_night"),
    # ---------------- SYMPHONY RESTAURANT
    dict(to=41, reason="scene change: they arrive at Symphony restaurant; Tholaal walks up smiling",
         chars=["shahula_young", "aamir", "tholaal"], loc="symphony_outside",
         visual=f"{A_BLACK} standing beside his parked motorbike outside the glowing restaurant; {SY_PEACH} standing a step away, "
                f"giving a polite small smile; Tholaal walking up from the restaurant entrance with a sly friendly smile; the men "
                f"and Shahula keep a clear gap, no one touching",
         camera=f"medium wide shot, eye level, {LOW} (the lit pavement)", amb="street_night"),
    dict(to=44, reason="character enters: Naya; introductions — 'This is my Shahoo, we'll marry very soon'",
         chars=["aamir", "shahula_young", "tholaal", "naya"], loc="symphony_outside",
         visual=f"four people standing outside the glowing restaurant entrance: {A_BLACK} proudly gesturing with an open palm "
                f"toward {SY_PEACH}, who smiles shyly; Tholaal and Naya standing side by side across from them, smiling in welcome; "
                f"everyone a clear arm's length apart, no one touching; each person appears only once",
         camera=f"medium wide group shot, eye level, {LOW} (the lit pavement)", amb="street_night",
         sens="other", safe="Tholaal and Naya (an affair) shown only standing apart, no touching or flirtatious pose"),
    dict(to=46, reason="back to the group outside: 'let's go in quickly, it's crowded tonight'", reuse="beat_018",
         chars=["aamir", "shahula_young", "tholaal", "naya"], loc="symphony_outside", visual="reuse of beat_018",
         amb="street_night"),
    dict(to=48, reason="scene change: inside, a table for four; the three colleagues chat excitedly",
         chars=["aamir", "tholaal", "naya", "shahula_young"], loc="symphony_inside",
         visual=f"a table for four inside the busy restaurant: {A_BLACK}, Tholaal and Naya leaning in, talking and laughing loudly "
                f"over plates of food and glasses of juice; {SY_PEACH} sitting at the end of the table, quiet and left out, hands "
                f"in her lap; everyone seated apart, no one touching; each person appears only once. Colour check: Aamir's shirt is BLACK "
                f"(not white), Tholaal's shirt is navy, Naya's abaya wine-red, Shahula's dress peach",
         camera=f"medium wide shot, eye level, {LOW} (the table top with plates and juice glasses)", amb="cafe",
         sens="other", safe="the affair couple only laughing at the table with a gap; drinks are juice and water"),
    dict(to=50, reason="focus change: Shahula learns Tholaal is married and looks at Naya, who shows no remorse",
         chars=["naya", "tholaal"], loc="symphony_inside",
         visual="Naya and Tholaal seen across the table from Shahula's point of view, sitting side by side with a clear gap, not "
                "touching, both laughing carelessly; Naya's face bright and untroubled, no trace of guilt; plates of food and "
                "glasses of juice in front of them",
         camera=f"medium two-shot, eye level, {LOW} (the table top)", amb="cafe",
         sens="other", safe="no touching, no flirtatious pose; only careless laughter"),
    dict(to=53, reason="focus change: her unease; Aamir raises his eyebrows asking what's wrong, she shakes her head",
         chars=["shahula_young", "aamir"], loc="symphony_inside",
         visual=f"{SY_PEACH} and {A_BLACK} seated beside each other at the restaurant table with a clear gap; he pauses his "
                f"laughing and eating to look at her with raised eyebrows in a silent question; she gives a small shake of the "
                f"head with a forced faint smile, sadness in her eyes",
         camera=f"medium two-shot, eye level, {LOW} (the table top with plates)", amb="cafe"),
    # ---------------- HOME, LATE NIGHT
    dict(to=56, reason="scene change: back home she paces her room, troubled by what she saw",
         chars=["shahula_young"], loc="shahula_room",
         visual=f"{SY_PEACH} pacing in her small room at night, one hand at her chin, brows drawn, deep in troubled thought, a "
                f"shiver of distress on her face",
         camera=f"medium wide shot, eye level, {LOW} (the floor in soft lamplight)", amb="room_night"),
    dict(to=61, reason="action change: Aamir knocks; she steps out; 'Isn't Tholaal married? Don't take me to such places again'",
         chars=["shahula_young", "aamir"], loc="corridor_night",
         visual=f"{SY_PEACH} standing in the dim corridor just outside her open door, looking straight into the eyes of "
                f"{A_BLACK}, who stands facing her with a careless shrug, {GAP}; her face serious and pleading",
         camera=f"medium two-shot from the side, eye level, {LOW} (the dim corridor floor)", amb="living_night",
         sens="intimacy", safe="unmarried pair talking with a clear gap"),
    dict(to=64, reason="focus change: Aamir's face changes; he lectures her to stay out of it",
         chars=["aamir"], loc="corridor_night",
         visual=f"medium close-up of {A_BLACK} in the dim corridor, his face hardened with displeasure, jaw tight, explaining "
                f"with one open palm, a cold impatient look in his eyes",
         camera=f"medium close-up, eye level, {LOW} (dark corridor wall)", amb="living_night"),
    dict(to=65, reason="back to the two in the corridor: she falls silent", reuse="beat_024",
         chars=["shahula_young", "aamir"], loc="corridor_night", visual="reuse of beat_024", amb="living_night"),
    # ---------------- AFTER THE WEDDING
    dict(to=68, reason="time jump: after the wedding, she becomes his possession; her life bent to his schedule",
         chars=["shahula"], loc="married_hall",
         visual=f"{SW}, standing alone at the dining table in the dim sitting room setting out one plate and one glass for "
                f"someone who is not there, a man's ironed shirt hanging on the back of a chair, her face subdued and resigned, "
                f"her eyes downcast",
         camera=f"medium shot, eye level, {LOW} (the dining table top)", amb="home_night", transition="black"),
    dict(to=70, reason="time jump: nearly a year into the marriage, Azeeza passes away",
         chars=[], loc="azeeza_bedroom_empty",
         visual="Azeeza's empty wooden bed, neatly made, a folded cream shawl lying on it, her thin gold-rimmed glasses folded "
                "on the bedside table beside a closed green cloth-bound book on a small stand, no people",
         camera="medium wide shot, eye level, the bed in the upper two-thirds, the plain floor as a calm lower third",
         amb="home_day", transition="black", sens="death",
         safe="Azeeza's death shown only as her empty bed with a folded shawl and her glasses"),
    # ---------------- ONE EVENING: THE DARK HOUSE
    dict(to=73, reason="time jump: one evening Aamir comes home to a dark, silent house",
         chars=["aamir"], loc="dark_house",
         visual=f"{A_OFF} just stepped in through the front door into the dark silent sitting room, his figure half in shadow, "
                f"a faint stripe of warm light from the kitchen doorway falling across the floor, his hand reaching for the light "
                f"switch on the wall, looking around uneasily",
         camera=f"medium wide shot, eye level, {LOW} (the dark tiled floor with the stripe of light)", amb="living_night",
         transition="black"),
    dict(to=77, reason="scene change: he searches the bedroom and the house; Shahula is nowhere",
         chars=["aamir"], loc="marital_bedroom",
         visual=f"{A_OFF} standing in the dim bedroom beside the empty neatly made bed, one hand on the handle of the closed white "
                f"side door, turning his head and calling out with an anxious, irritated face",
         camera=f"medium wide shot, eye level, {LOW} (the floor and the edge of the bedspread)", amb="room_night",
         sens="clothing", safe="the bathroom is shown only as a closed door"),
    # ---------------- THE CONFRONTATION
    dict(to=79, reason="action change: after Isha he sits on the sofa staring at the main door",
         chars=["aamir"], loc="hall_confront",
         visual=f"{A_OFF} sitting on the grey sofa with one leg crossed over the other, arms folded, staring fixedly toward the "
                f"front door with cold, hard eyes, harsh low lamplight on one side of his face",
         camera=f"medium shot from the doorway, eye level, {LOW} (the tiled floor in shadow)", amb="living_night"),
    dict(to=80, reason="character enters: Shahula, seven months expecting, steps in and steps back in fear",
         chars=["shahula"], loc="hall_confront",
         visual=f"{SP}, standing just inside the front door, frozen, taking a step back with both hands protectively over her "
                f"rounded belly, her big dark eyes wide with fear",
         camera=f"medium shot, eye level, {LOW} (the tiled floor near the door)", amb="living_night", hum=True),
    dict(to=81, reason="action change: he rises from the sofa, hands on hips, 'Where have you been?'",
         chars=["aamir"], loc="hall_confront",
         visual=f"{A_OFF} standing in front of the grey sofa with his hands on his hips, glaring with a deep, hard, furious stare "
                f"straight at the viewer, harsh low light from below, long shadows; he is the only person in the frame, no silhouette in the foreground",
         camera=f"medium shot from her point of view, slightly low angle, {LOW} (the tiled floor in shadow)",
         amb="living_night", sens="violence", safe="anger shown only as his hard stare from her point of view"),
    dict(to=83, reason="back to Shahula frozen, unable to speak", reuse="beat_032", chars=["shahula"],
         loc="hall_confront", visual="reuse of beat_032", amb="living_night"),
    dict(to=85, reason="action change: he lashes out at the sofa; she flinches (the outburst shown only as a fallen cushion)",
         chars=["shahula", "aamir"], loc="hall_confront",
         visual=f"wide view of the dim sitting room: {A_OFF} standing beside the grey sofa with a clenched jaw and rigid arms at his "
                f"sides, a sofa cushion toppled on the floor; across the room, far from him, {SP} flinching with her shoulders "
                f"raised and both hands over her belly, eyes squeezed shut; a large empty space between them",
         camera=f"wide shot, eye level, {LOW} (the tiled floor with the fallen cushion)", amb="living_night",
         sens="violence", safe="the outburst is shown only as a toppled cushion and her flinch, a wide distance between them"),
    dict(to=87, reason="back to Aamir's hard stare: 'I'm asking for the last time!'", reuse="beat_033",
         chars=["aamir"], loc="hall_confront", visual="reuse of beat_033", amb="living_night"),
    dict(to=90, reason="framing change: his rage breaks loose — accusations about Raamee",
         chars=["aamir"], loc="hall_confront",
         visual=f"close-up of {A_OFF}, his handsome face twisted with rage, shouting, brows knotted, eyes blazing, veins at his "
                f"temple, harsh low lamplight and deep shadows behind him; he is the only person in the frame, the room behind him empty",
         camera=f"close-up, slightly low angle, {LOW} (dark background)", amb="living_night",
         sens="violence", safe="verbal rage only, from her point of view; no gesture toward her"),
    dict(to=93, reason="focus change: her astonishment at Raamee's name, then defiance: 'Stop it!'",
         chars=["shahula"], loc="hall_confront",
         visual=f"close-up of {SW}, her eyes wet and wide with astonishment and hurt, then lifting her chin in defiance, lips "
                f"parted as she speaks out, harsh low lamplight on one side of her face; her face clear and unmarked; she is the only person in "
                f"the frame, the room behind her empty, no silhouette in the foreground",
         camera=f"close-up, eye level, {LOW} (dark soft-focus background)", amb="living_night"),
    dict(to=96, reason="the first blow (NOT shown): symbolic shadow on the floor and the sofa",
         chars=[], loc="hall_confront",
         visual="the dim sitting room floor seen low: a man's long dark shadow stretching across the tiles and over the grey "
                "sofa from the harsh lamp, a toppled sofa cushion on the floor, a woman's small slipper left beside it, no people "
                "visible in the frame",
         camera="low angle wide shot along the floor, the shadow and the sofa in the upper two-thirds, the plain tiles as a calm lower third",
         amb="living_night", sens="violence",
         safe="the slap and the grip are never shown: only a man's long shadow, a fallen cushion and a lone slipper; muffled soft thud at -24 dB"),
    dict(to=98, reason="aftermath: the first time he laid a hand on her; she sits frozen in shock",
         chars=["shahula"], loc="hall_confront",
         visual=f"{SP}, sitting alone on the floor with her back against the grey sofa, knees drawn to one side, both hands "
                f"resting protectively on her rounded belly, her face turned away into shadow, eyes staring blankly in shock; her "
                f"face unmarked; the dim lamp behind her",
         camera=f"medium shot, eye level, {LOW} (the tiled floor in shadow)", amb="living_night",
         sens="violence", safe="aftermath only: she sits alone in shadow, no marks, no one near her", hum=True),
    dict(to=99, reason="return: the kind foster-mother is gone and the loving house has become a dark prison",
         reuse="beat_028", loc="azeeza_bedroom_empty", visual="reuse of beat_028", amb="home_night", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"A good decision? But who is she? I only asked because your list is so long.\" Shahula said in a joking tone, very gently.")
sh(2, "At Shahula's joke a smile came to Aamir's lips. \"However long the list, this heart of mine calls out for only one person.")
sh(3, "From the very first day I saw her, she has been the owner of this heart. But I don't think she feels it.\"")
sh(4, "Aamir said softly, gazing deeply into Shahula's face. Shahula raised her eyebrows with a light smile. \"How lucky!")
sh(5, "I thought every name on that list owned a share of that heart.\" This time too Shahula's words were in jest. Aamir burst out laughing.")
sh(6, "\"Then tell Mamma her name and try to get it done quickly.\" Shahula said, rising from the joali. \"Where are you going?\" Aamir asked. \"To my room.",
   [("creak", "ތެދުވަމުން", -22)])
sh(7, "To change. I haven't even eaten yet. And I have to fill this application form too. Only then can I drop by the university on my way to the office tomorrow.")
sh(8, "I want to be among the very first to hand in the form.\" The greatest happiness showed on Shahula's face.")
sh(9, "Sweet hopes of a bright future shone in her eyes. \"A university form?\" Aamir asked in surprise. \"Yes.")
sh(10, "Shariah and Law. My mother's dream, my future... and to get justice for my father.\" A happy smile appeared on Shahula's lips.")
sh(11, "Even so, those words brought unease into Aamir's heart. What he wanted was a wife who would stay at home and look after the family.")
sh(12, "Though Shahula went to work now, he was sure that after the marriage she would obey his word. \"I'm going.\"")
sh(13, "Shahula smiled and walked toward her room. As soon as she entered, she put the handbag from her shoulder down on the bed.",
   [("cloth_rustle", "ބާއްވައިލިއެވެ", -22)])
sh(14, "And after looking deeply at the form in her hand, she pressed it close against her heart.",
   [("paper_shuffle", "ޖައްސައި", -24)])
sh(15, "Her face shone then with a brightness full of new hopes. At that moment there was a knock on the door of the room.",
   [("knock", "ޓަކިދިން", -18)])
sh(16, "Shahula quickly put the forms down and went to open the door. At the door stood Aamir. \"What is it?\" Shahula asked.",
   [("paper_shuffle", "ބޭއްވުމަށްފަހު", -22), ("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(17, "\"Mamma is calling.\" Aamir said. Without even stopping to change her clothes, Shahula walked toward Azeeza's room.")
sh(18, "Aamir came in behind her. Azeeza was sitting up in bed. In front of her lay a small, old jewellery box.")
sh(19, "\"Shahula... come.\" Azeeza called. Her face showed an unusual happiness.")
sh(20, "Azeeza's face, which always brightened at the sight of Shahula, showed far deeper feelings today. When Shahula went and stopped beside the bed,")
sh(21, "Azeeza took her by the hand and sat her down on the bed. Between them was that jewellery box. Aamir too came and stood beside the bed.")
sh(22, "Smiling, Azeeza glanced at Aamir and opened the box. From inside it she took out two gold bangles, gleaming bright.",
   [("lock_click", "ހުޅުވައިލިއެވެ", -24)])
sh(23, "\"This is a symbol of our family. A precious trust handed down from generation to generation. Today Aamir has found a new owner for these heirlooms passed down from his grandmother's side.\"")
sh(24, "Saying this, Azeeza took Shahula's hand and began to put the bangles on her. Shahula sat stunned and bewildered.")
sh(25, "Even so, she did not dare to draw her hand back. Shahula's eyes went to Aamir's face.")
sh(26, "On Aamir's lips was a light smile full of contentment and joy. Because his mother had agreed at a single word from him, he was overjoyed.")
sh(27, "Though it was said indirectly, Shahula understood at once the deep meaning of Azeeza's words. Realising this was how she was to repay all of Azeeza's kindness to her,")
sh(28, "a sharp pain rose in her heart. Fear closed around her at what her future would become if she married Aamir.",
   hum=True)
sh(29, "She closed her eyes to push back the tears gathering in them. Even so, she wanted to say what was in her heart.",
   [("sigh", "މަރައިލިއެވެ", -22)])
sh(30, "\"Shahula, my child, do you agree to this marriage?\" Azeeza seemed to sense something from the look on Shahula's face.")
sh(31, "By then Azeeza had finished putting the bangles on Shahula's wrist. Aamir gave Shahula no chance to answer.")
sh(32, "He quickly began talking to his mother and changed the subject. As mother and son became lost in their conversation,")
sh(33, "it was as if Azeeza had completely forgotten Shahula standing beside her. When Shahula came outside, Aamir was sitting on his motorbike waiting for her.")
sh(34, "Seeing Shahula, Aamir looked at her attentively. \"You took so long! Even if you make me wait, this is a bit much.\"")
sh(35, "Aamir said jokingly. Without a word of answer Shahula went and got on the back of the motorbike.")
sh(36, "She had not even had a chance to think about the sudden change that had come into her life. She hadn't had the courage to say anything in front of Azeeza.")
sh(37, "In truth, Aamir had not given her that chance. With despair in her heart, she did not know how dangerous,",
   hum=True)
sh(38, "how rough a sea the journey she was beginning would cross. She could not even guess how many thorns would pierce her feet on the hard road she now had to walk.")
sh(39, "All along the ride Aamir kept trying to joke and chat with Shahula. But she paid little attention to any of it.",
   [("motorbike_pass", "ދަތުރުމަތީގައި", -22)])
sh(40, "The motorbike stopped near Symphony restaurant. As Shahula got off, Aamir's friend Tholaal came over and stopped beside them.",
   [("motorbike_pass", "ސައިކަލު", -22)])
sh(41, "And smiled as he looked at Shahula. In return Shahula smiled back. \"Shahoo, this is Tholaal...")
sh(42, "a friend from the same office. And this is...\" Aamir tried to introduce her. \"This is Naya... right?\" Tholaal said, looking at Naya.")
sh(43, "\"This is my Shahoo. We're getting married very soon.\" Aamir introduced Shahula with pride and youthful zeal.")
sh(44, "Again Shahula looked at them and smiled. Naya and Tholaal said a few words of welcome. Shahula smiled in thanks.")
sh(45, "\"Let's go in quickly, it's very crowded tonight.\" Tholaal said. \"Yes, did you book a table?\" Aamir asked. \"Yes, I booked.")
sh(46, "Let's go inside. No use standing out here. We'll only get a good taste in our mouths once we go in and order something, right, Naya?\"")
sh(47, "Tholaal said. With some hesitation Shahula followed them in. And sat down at a table for four.")
sh(48, "Tholaal and Naya's talk was of a very different kind. As the three friends who worked in the same office chatted excitedly, Aamir joined right in.",
   [("cup_clatter", "ފޯރީގައި", -24)])
sh(49, "In that gathering Shahula sat completely left out. When they moved from office talk to their private lives, Shahula learned that Tholaal was someone's husband.")
sh(50, "Shahula looked at Naya in astonishment. Not a trace of complaint or regret showed on Naya's face. Yet,")
sh(51, "having to sit with them in that gathering filled Shahula's heart with unease. Shahula turned her gaze to Aamir, who was laughing happily and eating.",
   [("cup_clatter", "ކެއުމައިގެން", -24)])
sh(52, "Aamir noticed at once that Shahula was uncomfortable in that atmosphere. Raising his eyebrows, he asked with a gesture what was wrong.")
sh(53, "Though Shahula shook her head to say nothing was wrong, Aamir sensed very well the sadness stirring in her heart.")
sh(54, "As soon as she got home, lost in deep thought, Shahula began pacing back and forth in her room. The picture of Tholaal and Naya still kept turning in her mind.",
   [("door_close", "ވަދެވުމާއެކު", -22)])
sh(55, "That they could be so at ease even in such a wrong relationship. And that Aamir supported it worried Shahula deeply.")
sh(56, "Imagining how that poor woman's heart would shatter the day Tholaal's wife learned the truth, a shiver ran through Shahula.",
   [("breath", "ހީބިހި", -22)])
sh(57, "Pacing anxiously, she stopped; suddenly there was a knock on the door. Shahula was sure it was Aamir.",
   [("knock", "ޓަކިދިން", -18)])
sh(58, "She went, opened the door and stepped outside. \"What is it?\" Shahula asked gently. \"You seem so uneasy tonight?\"",
   [("door_open", "ހުޅުވައިލުމަށްފަހު", -20)])
sh(59, "Aamir asked to be sure. \"Isn't Tholaal someone's husband?\" Shahula asked, looking him straight in the eye. \"Yes.")
sh(60, "Is that what you're thinking about so much?\" Aamir said dismissively. \"Aamir. Don't ever take me again to places where such people go.")
sh(61, "I don't like their improper way of living in any way at all.\" Shahula said pleadingly.")
sh(62, "The colour of Aamir's face changed at once. Letting out a deep breath, he tried to make Shahula understand. \"Come on, Shahoo,",
   [("sigh", "ނޭވާއެއް", -20)])
sh(63, "don't care so much about that. I don't think it's anything to be so serious about. Look at Naya, how calm she is about it.")
sh(64, "It's Naya who's with Tholaal. So she's the one to worry about it. Shahoo, stay out of it and keep your distance.\"")
sh(65, "Aamir said in a slightly displeased tone. Shahula gave no further answer and wisely fell silent.")
sh(66, "Because it was easy for Aamir to say that. From the moment the marriage was founded, Shahula became Aamir's complete possession.")
sh(67, "As though not a trace of her own freedom remained. Shahula was forced to reshape her life to fit Aamir's schedule.")
sh(68, "While Aamir kept advising her again and again to be an obedient wife, she wondered whether he could fulfil the duties a husband must.")
sh(69, "When the marriage was nearly a year old, Azeeza bade farewell to this passing world. It was only after that that Shahula saw Aamir's true face.",
   hum=True)
sh(70, "From then on, the cruel nature hidden behind the curtain of a good-natured temper came out into the open.")
sh(71, "What greeted Aamir as he came into the house was a deep silence and darkness spread through the whole house. Because the kitchen light was on,",
   [("door_open", "ވަދެގެން", -22)])
sh(72, "a faint ray of light from there fell into the big hall. Aamir first lit up the hall.")
sh(73, "Then, since this was the time Shahula usually rested, thinking she must be asleep, he headed for the bedroom with quick steps.")
sh(74, "\"Shahoo...\" Going into the room and not finding Shahula on the bed, Aamir called out. Thinking she might be in the bathroom,")
sh(75, "without thinking he grabbed the bathroom door handle and called Shahula's name again. But there was no reply from there either.",
   [("lock_click", "ތަޅުގައި", -22)])
sh(76, "Anxiously Aamir began looking all around the house. There was no sign of Shahula in any room. Not knowing what else to do, he came back into the bedroom.")
sh(77, "\"Where has Shahula gone at this hour? I'd even told her I'd be home early.\" Aamir voiced his worry, talking to himself.")
sh(78, "Shahula, who had had to go out to the office at four in the afternoon, only made it home after the Isha prayer. When Shahula came into the house,",
   [("door_open", "ވަދެގެން", -22)])
sh(79, "Aamir was sitting on the sofa in the big hall, one leg crossed over the other, watching the main door.")
sh(80, "Seeing the way he sat, fear rose in Shahula's heart. Seven months pregnant, she took a step back.",
   [("heartbeat", "ބިރުވެރިކަން", -22)])
sh(81, "Aamir rose from the sofa with an angry question. \"Where have you been?\" Getting up from the sofa, hands on his hips, staring at Shahula with a deep, hard look, Aamir asked.")
sh(82, "Shahula knew at once he was extremely displeased. Though Shahula opened her mouth to answer, no sound would come out,")
sh(83, "and Aamir repeated it in a harsh voice. \"Where have you come from?\" \"Have you eaten anything?\" Hesitating to answer the question,")
sh(84, "Shahula tried to steer the conversation another way. At that, grinding his teeth, Aamir suddenly lashed out at the sofa with his foot.",
   [("soft_thud", "ޖެހިއެވެ", -23)])
sh(85, "Amid fear and panic Shahula flinched. It was plain that Aamir was beside himself with anger.",
   [("gasp", "ހިންދިރުވައިލެވުނެވެ", -22)])
sh(86, "\"I'm asking for the last time! Tell the truth, where have you come from?\" Aamir's voice had a commanding hardness. \"The... the office.")
sh(87, "Something urgent came up.\" Shahula said slowly in a frightened voice. \"Didn't I tell you not to go to the office?")
sh(88, "You're going there secretly to meet Raamee, aren't you! I wore myself out telling you to quit that job, and still you didn't listen. What are you short of?")
sh(89, "Don't I spend on you? Don't I feed you? Or don't I buy you clothes? I know very well what wrong you two get up to at the office at this hour.")
sh(90, "Couldn't that Raamee find anywhere else to work?\" Aamir's anger broke out of control.")
sh(91, "Hearing Raamee's name from Aamir's tongue, Shahula was deeply astonished. Her love for Raamee was a past that had ended long before she married Aamir,")
sh(92, "and lay buried. Then why bring that name up today? If she too wanted to reveal things,")
sh(93, "there were many such names in Aamir's life. \"Stop it!... What do you know, Aamir, that you heap such an ugly accusation on my head?\"",
   hum=True)
sh(94, "Shahula's words were cut short by the hot blow of Aamir's hand across her cheek. With the pain her whole face burned.",
   [("soft_thud", "ހަމަލާއިންނެވެ", -24)], hum=True)
sh(95, "With one hand on her cheek, she held her belly with the other. \"Not one more word out of that mouth!\"",
   hum=True)
sh(96, "Aamir warned her, gripping Shahula hard. From the pain a moan of agony escaped Shahula's lips.",
   [("sob_breath", "އާހެއް", -22)], hum=True)
sh(97, "It was the first time Aamir had laid a hand on her. He felt no pity even for his own child growing inside her.",
   hum=True)
sh(98, "Shahula froze from the shock and the sudden fright. The whole world seemed to spin and turn dark around her.",
   [("heartbeat", "ގަނޑުވިއެވެ", -22)], hum=True)
sh(99, "With her kind foster-mother's farewell to this passing world, that loving house which had given her protection and safety had today become the dark prison of her life.",
   hum=True)
SHOTS = S

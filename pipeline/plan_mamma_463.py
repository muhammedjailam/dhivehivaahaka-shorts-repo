"""Beat/shot plan for Mamma episode 463 (used by plan_beats.py)."""

LOC = {
    "bedroom_morning": "Shahula and Aamir's main bedroom in an older two-storey Malé townhouse: a wooden double bed with a tall plain wooden headboard, pillows and a plain bedspread, a small white wooden baby cot beside the bed, a wooden bedside table with a small glowing night-lamp, a tall wooden wardrobe, a window with heavy drawn curtains, a wooden door to the hall, tiled floor",
    "sitting_room_night": "the sitting room (bodu fendaa) of the same older Malé townhouse: a grey sofa with cushions, a low coffee table, a television with a dark blank screen, framed pictures of flowers on the wall, drawn curtains, tiled floor",
    "taxi_night": "the back seat of a small Malé taxi at night, rain-streaked side windows, blurred warm amber streetlights and tall pastel buildings sliding past outside, wet reflections",
    "hospital_corridor": "a quiet hospital corridor in Malé late at night: pale mint-green walls, a polished floor with reflections, a row of plain waiting chairs along the wall, closed double doors with frosted glass panels, soft ceiling lights, no signs",
    "ward": "a hospital maternity ward bed by a large window: white bedsheets and a white blanket, a white curtain divider on a rail, a small bedside table, a small clear hospital bassinet on a wheeled stand beside the bed, no medical equipment in view",
    "terrace_clothesline": "the small walled back terrace of the older Malé townhouse: a clothesline strung between two posts with small pale-blue and white baby clothes pegged on it, potted plants, a leafy tree leaning over the wall, the walls of neighbouring pastel buildings, a heavy sky of dark rolling clouds",
    "kitchen_day": "the kitchen of the older Malé townhouse: a counter with cupboards, a fridge, a wall telephone, a window over the counter looking out at a leafy tree branch and dark clouds, the kitchen doorway opening to the hall and the front door beyond",
    "bedroom_storm": "the same main bedroom of the older Malé townhouse in the afternoon: the wooden double bed with a packed soft travel bag on the bedspread, the white baby cot, the tall wooden wardrobe with its doors open and a drawer pulled out, a window with the curtains half open on dark clouds, the bedroom door open to a dark hall",
}
MOOD = {
    "bedroom_morning": "early morning but dim: curtains drawn, thin grey daylight at their edges, the small night-lamp still glowing warm amber, cold shadowy room, quiet, sorrowful and heavy",
    "sitting_room_night": "night, dim and cold: a single lamp in the corner, deep blue-grey shadows, the house feels like a silent prison",
    "taxi_night": "rainy night, deep blue-black darkness with warm amber streetlight streaks and bokeh through the wet glass, lonely and frightened, soft hazy memory glow",
    "hospital_corridor": "late night in the hospital, cool fluorescent light mixed with a soft warm glow, quiet tension and worry, soft hazy memory feel",
    "ward": "morning, soft pale daylight through the window, quiet and still, a soft hazy memory glow",
    "terrace_clothesline": "afternoon turned dark: heavy grey-black storm clouds gathering, strong gusting wind tossing the clothes and the branches, cold grey light, urgent and tense",
    "kitchen_day": "stormy afternoon, cold grey light from the window, dark clouds outside, a dim kitchen, tense and hurried",
    "bedroom_storm": "stormy afternoon, cold grey light through the window, dark clouds, the hall beyond the door in deep shadow, tense, a held breath",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear distance between them, never touching"
NOMARK = "her face smooth and unmarked, no marks, no swelling"
SH = ("Shahula in her loose long-sleeved ankle-length dusty-rose house dress and cream hijab fully covering her hair "
      "and neck, two plain gold bangles on her wrist")
SH_ABAYA = ("Shahula (reference used for her face only; wearing a loose long-sleeved ankle-length black abaya and a black "
            "hijab with a white under-scarf fully covering her hair and neck, NOT the dusty-rose dress and cream hijab)")
SH_GOWN = ("Shahula (reference used for her face only; wearing a modest loose long-sleeved pale-blue hospital patient gown "
           "buttoned up to the neck and her cream hijab fully covering her hair and neck, a white blanket over her up to "
           "the waist, NOT the dusty-rose dress)")
SH_TAXI = ("Shahula (reference used for her face only; wearing a loose long-sleeved ankle-length dark-grey abaya and her "
           "cream hijab fully covering her hair and neck, NOT the dusty-rose dress), a modest rounded pregnancy belly "
           "under the loose abaya")
A_HOME = ("Aamir (reference used for his face only; wearing a plain dark-grey long-sleeved t-shirt and long dark track "
          "trousers, NOT the white shirt)")
A_OFFICE = ("Aamir (reference used for his face only; wearing a light-blue long-sleeved shirt and dark trousers, NOT the "
            "white shirt)")
BABY = "baby Zidhaan, a healthy chubby baby boy of a few months fully wrapped in a pale-blue cotton blanket"
SHAWL = "a large soft cream shawl draped over her shoulders and around the baby"

BEATS = [
    # ---------------- MORNING AFTER, THE DIM BEDROOM
    dict(to=3, reason="episode opening: the morning after; Shahula wakes alone in the dim bedroom, aching",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"{SH}, half sitting up against the tall wooden headboard on the pillows, a blanket over her legs, just "
                f"opening her tired, swollen-from-crying eyes and looking around the empty dim room; {NOMARK}; the other "
                f"side of the bed empty and smooth; beside the bed the white baby cot with {BABY} asleep inside; the "
                f"night-lamp glowing on the bedside table",
         camera=f"medium wide shot, eye level, {LOW} (the plain bedspread in soft shadow)", amb="room_day",
         sens="violence", safe="last night's beating is never shown: she wakes alone, unmarked, in a dim room"),
    dict(to=5, reason="framing change: she whispers 'Aamir...' and closes her eyes; his cruelties replay in her mind",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"close-up of {SH}, her head resting back against the headboard, eyes closed, a single tear on her cheek, "
                f"lips slightly parted as if whispering a name, half of her face in soft shadow and half lit warm by the "
                f"night-lamp; {NOMARK}",
         camera=f"close-up, eye level, {LOW} (the dark headboard and pillow in soft shadow)", amb="room_day",
         sens="violence", safe="Aamir's past cruelties are only a closed-eye close-up; no flashback of violence"),
    dict(to=8, reason="return to the wide dim room while she reflects on her prayers and her fate", reuse="beat_001",
         chars=["shahula"], loc="bedroom_morning", visual="reuse of beat_001", amb="room_day"),
    dict(to=12, reason="action change: the baby cries; she gets up, lifts him from the cot and sits on the bed to feed him",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"{SH} sitting on the edge of the bed holding {BABY} snugly against her chest with {SHAWL}, only the "
                f"baby's small peaceful face and tiny hand visible near her shoulder; she looks down at him with tired, "
                f"tender, tear-filled eyes, lips pressed together as if in pain; {NOMARK}; the empty cot beside her",
         camera=f"medium shot, eye level, {LOW} (the bedspread and the floor in soft shadow)", amb="room_day",
         sens="other", safe="feeding is never shown: she only holds the wrapped baby against her under a large shawl; her sore lip is not shown"),
    dict(to=16, reason="character enters: Aamir comes in with a travel bag and orders her to pack for his trip",
         chars=["aamir", "shahula"], loc="bedroom_morning",
         visual=f"{A_HOME} standing near the foot of the bed beside a dark travel bag he has just set down on the floor, "
                f"looking at her with a stern, hard face, arms down at his sides; {SH} sitting up against the headboard "
                f"holding {BABY} under {SHAWL}, nodding slowly with tears running down; {GAP}, the whole length of the "
                f"bed between them; the bedroom door open behind him",
         camera=f"medium wide shot from the side of the room, eye level, {LOW} (the tiled floor and the bag)", amb="room_day",
         sens="violence", safe="a harsh order shown only as his stern face across the room; no hand raised, no pointing"),
    dict(to=18, reason="framing change: Aamir's tense face as he breathes out and tries to hold his temper",
         chars=["aamir"], loc="bedroom_morning",
         visual=f"close-up of {A_HOME}, seen slightly from below as if from her point of view, jaw tight, brows drawn, "
                f"breathing out slowly as he tries to control his temper, a cold displeased look in his eyes; harsh side "
                f"light from the night-lamp and deep shadow behind him; no hands in frame",
         camera=f"close-up, slightly low angle, {LOW} (dark soft-focus background)", amb="room_day"),
    dict(to=19, reason="action change: he sits down on the far edge of the bed; the baby feeds in her lap",
         chars=["aamir", "shahula"], loc="bedroom_morning",
         visual=f"{A_HOME} sitting on the far corner at the foot of the bed, turned towards her, hands resting on his "
                f"knees; {SH} sitting up against the headboard with {BABY} held close in her arms under {SHAWL}; {GAP}, "
                f"an arm's length and more of bedspread between them; dim light, the night-lamp glowing",
         camera=f"medium wide shot, eye level, {LOW} (the bedspread between them)", amb="room_day",
         sens="intimacy", safe="married couple shown far apart on the bed, fully dressed, nobody touching; feeding not shown"),
    dict(to=21, reason="emotional turning point: she turns her face away from his hand; he seizes her arm (not shown)",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"close-up of {SH}, turning her face sharply away to the side with her eyes squeezed shut and her chin "
                f"lifted, holding {BABY} close against her; in the blurred foreground edge only the dark-grey shoulder of "
                f"a man sitting at a distance, his hands out of frame; nobody touching her; {NOMARK}",
         camera=f"close-up, eye level, {LOW} (the cream shawl and the blanket in soft shadow)", amb="room_day",
         sens="violence", safe="his attempt to stroke her cheek and his hard grip on her arm are never shown: only her face turning away and his blurred shoulder at a distance"),
    dict(to=23, reason="framing change: she looks at him with tear-filled eyes that hold no fear this time",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"close-up of {SH}, looking straight ahead at someone just off-frame with tear-filled but steady, "
                f"fearless eyes, lips firmly closed, chin up; {NOMARK}; warm lamp light on one side of her face",
         camera=f"close-up, eye level, {LOW} (soft-focus shawl and bedspread)", amb="room_day"),
    dict(to=24, reason="back to the two of them on the bed: 'Please... don't make me angry'; she gives no answer",
         reuse="beat_007", chars=["aamir", "shahula"], loc="bedroom_morning", visual="reuse of beat_007", amb="room_day"),
    dict(to=28, reason="focus change: the baby smiles up at his mother; she smiles back and counsels him",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"{SH} sitting against the headboard holding {BABY} up in both arms facing her, {SHAWL}; the baby "
                f"smiling up at her with bright eyes and a tiny open mouth; she smiles back at him lovingly through drying "
                f"tears, leaning her face close to his; a thin sliver of grey morning light from the curtain edge; {NOMARK}",
         camera=f"medium close-up, eye level, {LOW} (the blanket and bedspread)", amb="room_day", hum=False),
    dict(to=31, reason="focus returns to Aamir watching her, displeased: 'Giving very good advice, aren't you?'",
         reuse="beat_006", chars=["aamir"], loc="bedroom_morning", visual="reuse of beat_006", amb="room_day"),
    dict(to=34, reason="back to mother and baby as she continues her pointed counsel", reuse="beat_011",
         chars=["shahula"], loc="bedroom_morning", visual="reuse of beat_011", amb="room_day"),
    dict(to=35, reason="she looks straight into Aamir's eyes", reuse="beat_009",
         chars=["shahula"], loc="bedroom_morning", visual="reuse of beat_009", amb="room_day"),
    dict(to=36, reason="action change: his phone rings and he walks out of the room with it at his ear",
         chars=["aamir", "shahula"], loc="bedroom_morning",
         visual=f"{A_HOME} walking out through the open bedroom door into the hall, seen from the side, holding a phone to "
                f"his ear (the screen not visible), his face turned away; in the soft-focus background {SH} sitting on the "
                f"bed holding the wrapped baby, watching him go; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (the tiled floor by the door)", amb="room_day"),
    dict(to=40, reason="action change: alone again, she closes her reddened eyes, amazed at her own courage; her resolve grows",
         chars=["shahula"], loc="bedroom_morning",
         visual=f"{SH} alone, sitting against the headboard with {BABY} asleep against her shoulder, her eyes closed, head "
                f"resting back, a calm, quietly determined expression; {NOMARK}; thin grey morning light at the curtain's "
                f"edge; Aamir's dark travel bag left on the floor near the door",
         camera=f"medium shot, eye level, {LOW} (the bedspread in soft shadow)", amb="room_day",
         sens="violence", safe="her split lip and swollen forehead (narrated) are never shown; her face stays unmarked"),
    dict(to=42, reason="scene change: the house that became a prison of pain; she decides to leave (bridge into memory)",
         loc="sitting_room_night",
         visual="the completely empty, silent sitting room at night with nobody in it: the empty grey sofa with one "
                "cushion fallen onto the floor, the low coffee table, the dark blank television, a single lamp in the "
                "corner throwing long cold shadows, framed flower pictures on the wall; an interior still life with no "
                "people at all, no person, no figure, no silhouette anywhere in the room",
         camera=f"wide shot, eye level, the sofa and lamp in the upper two-thirds, {LOW} (the tiled floor)",
         amb="living_night", sens="violence", safe="years of cruelty symbolised by an empty cold room and a fallen cushion"),
    # ---------------- FLASHBACK: THE FIRST BIRTH
    dict(to=45, reason="flashback, scene change: the night of her first labour; Aamir doesn't answer; she takes a taxi alone",
         chars=["shahula"], loc="taxi_night",
         visual=f"{SH_TAXI} sitting alone in the back seat of a taxi at night, holding a phone to her ear (the screen not "
                f"visible) with one hand and resting the other hand on her rounded belly, eyes closed in pain, tears on "
                f"her cheeks; rain streaks and blurred amber streetlights on the window beside her; only the back of the "
                f"driver's headrest visible",
         camera=f"medium shot from across the back seat, eye level, {LOW} (the dark seat and her lap in shadow)",
         amb="car_night", transition="dissolve",
         sens="other", safe="labour is shown only as a fully dressed woman in a taxi with a hand on her belly, eyes closed"),
    dict(to=48, reason="scene change: the hospital corridor; Fiyaza comes to help; the emergency and the missing consent",
         chars=["fiyaza"], loc="hospital_corridor",
         visual="Fiyaza standing in the night corridor beside the closed frosted double doors, hands clasped anxiously, "
                "talking with a worried face to a female doctor in a white coat over a long-sleeved dress and a white "
                "hijab fully covering her hair and neck, who holds a blank clipboard; a clear distance between them; the "
                "empty waiting chairs along the wall",
         camera=f"medium wide shot, eye level, {LOW} (the polished corridor floor with reflections)",
         amb="hospital_corridor",
         sens="other", safe="the delivery and the emergency are never shown: only a worried talk in the corridor outside closed doors"),
    dict(to=50, reason="action change: Shahula signs the consent form herself",
         chars=["shahula"], loc="hospital_corridor",
         visual=f"close-up of a woman's hand in a long pale-blue sleeve signing a completely blank white sheet of paper on "
                f"a clipboard held out by a nurse's hands; above it, slightly out of focus, the pale, tear-streaked, "
                f"determined face of {SH_GOWN}; the paper has no writing on it at all",
         camera=f"close-up, slightly high angle, the face in the upper part, {LOW} (the blank clipboard and her sleeve)",
         amb="hospital_corridor",
         sens="other", safe="consent for the operation shown only as her hand signing a blank paper; no procedure"),
    dict(to=52, reason="time jump: the next morning in the ward; Fiyaza beside her; the little cot is empty",
         chars=["shahula", "fiyaza"], loc="ward",
         visual=f"{SH_GOWN} sitting up in the ward bed, looking around anxiously with exhausted eyes; Fiyaza sitting on a "
                f"chair beside the bed, her eyes lowered; in the foreground beside the bed an empty small clear hospital "
                f"bassinet with only a neatly folded white blanket inside",
         camera=f"medium wide shot, eye level, {LOW} (the white blanket and the empty bassinet)", amb="hospital_room",
         transition="black", sens="death", safe="the first baby's loss shown only by an empty bassinet with a folded white blanket; no baby shown"),
    dict(to=54, reason="framing change: Fiyaza takes her hand; her tearful face tells Shahula the truth",
         chars=["fiyaza"], loc="ward",
         visual="close-up of Fiyaza sitting by the bed, her face full of sorrow, eyes welling with tears, holding a woman's "
                "hand in a pale-blue sleeve gently in both of hers on the white blanket",
         camera=f"close-up, eye level, {LOW} (the white blanket and the held hands)", amb="hospital_room",
         sens="death", safe="the news is carried only by Fiyaza's tearful face"),
    dict(to=57, reason="emotional turning point: Shahula's silent sobs break into loud grief",
         chars=["shahula", "fiyaza"], loc="ward",
         visual=f"{SH_GOWN} — her gown and sleeves are pale blue, NOT pink and NOT dusty-rose — sitting in the ward bed bent forward with both hands covering her face in grief, shoulders "
                f"shaking; Fiyaza beside her with one hand resting on her shoulder, eyes closed in sorrow; in the "
                f"foreground the empty small clear bassinet with the folded white blanket",
         camera=f"medium shot, eye level, {LOW} (the empty bassinet and white blanket)", amb="hospital_room",
         sens="death", safe="grief shown with dignity, face hidden in her hands; no baby shown"),
    dict(to=60, reason="time and scene change: back home Aamir blames her for the loss; she is soon pregnant again",
         chars=["aamir", "shahula"], loc="sitting_room_night",
         visual=f"{A_HOME} standing in the middle of the dim sitting room with his arms folded, glaring and speaking "
                f"with a cold, accusing face; {SH} sitting at the far end of the grey sofa with her head bowed and her "
                f"hands folded in her lap; {GAP}, the coffee table between them; one lamp lit",
         camera=f"medium wide shot, eye level, {LOW} (the tiled floor and the coffee table)", amb="living_night",
         transition="black", sens="violence", safe="his cruel blame shown only as a cold standing figure and her bowed head across the room"),
    # ---------------- FLASHBACK: THE SECOND BIRTH
    dict(to=64, reason="time jump: after the hard second birth, next morning Aamir sits by her bed, seemingly changed; the newborn asleep",
         chars=["shahula", "aamir"], loc="ward",
         visual=f"{SH_GOWN} sitting up in the ward bed, pale and tired, looking with fragile hope at {A_OFFICE}, who sits "
                f"on a chair beside the bed leaning slightly towards her with an unusually gentle face, asking her "
                f"something; {GAP}; beside the bed a tiny healthy newborn swaddled in a pale-blue cotton blanket sleeping "
                f"peacefully in a small clear bassinet",
         camera=f"medium wide shot, eye level, {LOW} (the white blanket and the bassinet)", amb="hospital_room",
         transition="black",
         sens="other", safe="the transfusion and operation are never shown, only the calm morning after; his tender gesture is shown as a gentle lean, not contact"),
    dict(to=66, reason="character change: instead of Aamir, a canteen boy brings the king coconut",
         chars=["shahula"], loc="ward",
         visual=f"a Maldivian teenage boy of about sixteen in a plain white t-shirt, dark long trousers and a small "
                f"apron standing at the foot of the ward bed holding a green king coconut with a straw; {SH_GOWN} sitting "
                f"up in the bed looking at him in surprise and disappointment; a clear arm's-length gap between them, not "
                f"touching; the newborn asleep in the small bassinet",
         camera=f"medium wide shot, eye level, {LOW} (the white blanket at the foot of the bed)", amb="hospital_room"),
    dict(to=68, reason="action change: Aamir returns an hour later smelling of a woman's perfume; her suspicious eyes",
         chars=["shahula", "aamir"], loc="ward",
         visual=f"{SH_GOWN} sitting up in the ward bed, her eyes wide with sudden doubt, staring searchingly at the face "
                f"of {A_OFFICE}, who stands beside the bed bending a little towards her with a casual smile; {GAP}; the "
                f"untouched green king coconut on the bedside table",
         camera=f"medium shot, eye level, {LOW} (the white blanket and the bedside table)", amb="hospital_room", hum=True),
    # ---------------- PRESENT: SHE PACKS TO LEAVE
    dict(to=70, reason="flashback ends, scene and time change: a stormy afternoon, Aamir gone; she hurriedly takes the baby's clothes off the line",
         chars=["shahula"], loc="terrace_clothesline",
         visual=f"{SH_ABAYA} hurriedly unpegging small pale-blue and white baby clothes from the clothesline and bundling "
                f"them in her arm, glancing up anxiously at the dark rolling clouds; the wind tugging at the clothes and "
                f"her abaya; the tree branch over the wall bending in the wind",
         camera=f"medium shot, eye level, the sky and her face in the upper two-thirds, {LOW} (the terrace floor)",
         amb="garden_day", transition="dissolve"),
    dict(to=73, reason="scene change: in the kitchen she packs the bottle, milk tin and the little money, eyes on the front door",
         chars=["shahula"], loc="kitchen_day",
         visual=f"{SH_ABAYA} standing at the kitchen counter quickly putting a baby bottle and a plain milk-powder tin "
                f"without any label into an open bag, a small open round tin beside it; she glances anxiously over her "
                f"shoulder towards the doorway and the front door; behind her through the window a tree branch tossing "
                f"in the wind under dark clouds",
         camera=f"medium shot, eye level, {LOW} (the counter top with the bag)", amb="home_day"),
    dict(to=75, reason="scene and action change: back in the bedroom with the baby, she leaves Azeeza's gold bangles in the wardrobe drawer",
         chars=["shahula"], loc="bedroom_storm",
         visual=f"{SH_ABAYA} standing at the open wooden wardrobe holding {BABY} against her shoulder with one arm, and with "
                f"her other hand laying two plain shining gold bangles into the open wardrobe drawer, looking down at "
                f"them with sad, resolved eyes; a plain folder of papers tucked under her arm; the packed bag on the bed behind",
         camera=f"medium shot, eye level, {LOW} (the open drawer)", amb="room_day"),
    dict(to=76, reason="cliffhanger: walking out of the room she stops dead, startled, staring into the dark hall",
         chars=["shahula"], loc="bedroom_storm",
         visual=f"{SH_ABAYA} frozen in the open bedroom doorway, seen from the dark hall facing her, {BABY} held against "
                f"her shoulder, a bag on her other shoulder and a plain folder of papers in her hand, her eyes wide with "
                f"sudden shock, lips parted, staring towards the dark hall; grey stormy light behind her from the bedroom "
                f"window; nobody else visible",
         camera=f"medium shot, eye level, {LOW} (the dark floor of the hall)", amb="room_day", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Slowly blinking her eyelids, Shahula opened her eyes. She did not even know when she had fallen asleep, drowned in weeping last night.")
sh(2, "With the throbbing pain from her cheek and the aching that had spread through her whole body making it hard to bear,")
sh(3, "her head too was pounding terribly. When she looked around the room, in the dim light of the night-lamp, there was no one to be seen but her.")
sh(4, "\"Aamir...\" Aamir's name slipped softly from Shahula's lips. As she sank into deep thought, her eyes closed.",
   [("breath", "ބޭރުވެގެން", -24)])
sh(5, "Even with her eyes closed, the cruelties and injustices she had suffered from Aamir rose before her eyes.", hum=True)
sh(6, "Was he truly even a human being? She had always prayed before Allah to be granted a happy family full of love and kindness.")
sh(7, "But what heartbreaking scenes were appearing in her destiny today? Shahula was forced to think deeply about it.")
sh(8, "Aamir's cruelty had now crossed every limit. However much a person plans, she was realising today that the way Almighty Allah decrees may be different.")
sh(9, "Drowned in a sea of deep thoughts, Shahula came back to herself at the sound of her little baby starting to cry. Quickly opening her eyes,")
sh(10, "with the exhaustion that had taken over her body she got up, went and stood by the baby's cot. Lovingly lifting the baby and holding him to her chest, she sat on the bed and began to feed him.",
   [("cloth_rustle", "އުރާލައި", -24)])
sh(11, "The hungry little baby's crying slowly stopped. When Shahula touched the tip of her tongue to her dry lips, the split place stung sharply.")
sh(12, "Unable to bear that pain, her eyes closed. The moment she opened her tear-filled eyes was the moment she heard Aamir's footsteps outside.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކުގެ", -22)])
sh(13, "Shahula let out a deep breath in fear. Opening the bedroom door, Aamir came inside. He had a travel bag in his hand.",
   [("breath", "ނޭވާއެއް", -22), ("door_open", "ހުޅުވައިލުމަށްފަހު", -20)])
sh(14, "Setting the bag down by the bed, he pointed a finger at Shahula and said in a harsh, warning tone: \"I have to travel tomorrow.",
   [("cloth_rustle", "ބެހެއްޓުމަށްފަހު", -22)])
sh(15, "Iron enough clothes for two days and put them in the bag. And this time, my shaving kit,")
sh(16, "toothbrush and toothpaste — don't forget to put them in!\" Shahula slowly nodded. By then the tears were falling from her eyes without restraint.")
sh(17, "Seeing that, Aamir let out a deep breath. \"Why are you trying to make me angry? Shahoo, you know what happens when I get angry.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(18, "Then why do you always work so hard to make me angry?\" Aamir said as he walked towards the bed, trying to get hold of himself.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -24)])
sh(19, "And he went and sat down on the edge of the bed. Meanwhile their little baby lay in his mother's lap, feeding.",
   [("creak", "އިށީނދެލިއެވެ", -24)])
sh(20, "When Aamir tried to stroke Shahula's cheek with his palm, Shahula shook her head from side to side and pushed that hand away.",
   [("cloth_rustle", "ދުރުކޮށްލިއެވެ", -22)], hum=True)
sh(21, "At that, Aamir angrily gripped Shahula's arm hard. That movement made his displeasure plain.",
   [("heartbeat", "ހިފަހައްޓައިލިއެވެ", -22)], hum=True)
sh(22, "Shahula looked at Aamir with tear-filled eyes. This time those eyes held no fear and no hesitation.")
sh(23, "Last night too she had questioned Aamir with that same courage. But this time it was Aamir himself who hesitated. \"Please...")
sh(24, "don't make me angry,\" Aamir said in a soft, gentle tone. Even so, Shahula gave no answer. When the baby had finished feeding,")
sh(25, "looking up at his mother's face, he gave her a loving smile. It seemed as if he was thanking his mother. Shahula too, putting her sorrows aside,")
sh(26, "returned a smile full of love to her baby. She did not want to show that innocent soul any of the anger in her heart.")
sh(27, "\"Mamma's beloved child... you must become a strong, kind person, all right? Never hurt a helpless woman, ever.")
sh(28, "You must become someone with a good heart and fine character, like your grandmother, your grandfather and your great-grandmother. All right?\"")
sh(29, "Knowing that Aamir was sitting right beside her, Shahula said those words on purpose. Aamir sat watching what Shahula was doing.")
sh(30, "The little baby, making soft sounds, began to talk to his mother in his baby language. \"Giving very fine advice from the heart, aren't you?\"")
sh(31, "Aamir said, displeased. But Shahula paid no attention at all to what he said. \"Don't you become one of those who are educated but ignorant,")
sh(32, "you must become a person blessed with knowledge and gentleness, with a broad mind. Remember that women are mothers,")
sh(33, "sisters and little sisters! Know that they too are precious jewels raised on a mother's love! Give love and love is what you receive.")
sh(34, "Give respect and respect is what you receive. If you are unfaithful, do not expect faithfulness. Plant hatred and hatred is all that will grow.\"")
sh(35, "Saying this, Shahula looked straight into Aamir's eyes. Seeing her boldness, surprise rose in Aamir's heart.")
sh(36, "Just as Aamir opened his mouth to say something, his phone began to ring. Aamir got up from the bed, picked up the phone, put it to his ear and started walking out of the room.",
   [("phone_buzz", "ރިންގުވާން", -18), ("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(37, "Shahula slowly closed her reddened eyes. And she herself was amazed at the courage and steadiness she had found.")
sh(38, "The split corner of her mouth and the swelling on her forehead bore witness to the cruelty she had suffered from Aamir last night too.")
sh(39, "In that house she could do nothing right. Where there was no love or kindness, what ruled even the sacred bond of marriage was Aamir's force and cruelty.")
sh(40, "Shahula had endured all this cruelty, suffered without any fault of hers, in the complete hope that Allah, glorified and exalted, would show her a path of mercy.")
sh(41, "The beautiful dreams of happiness, peace and love had turned to vapour, and that house had become a shadow of pain, tears and cruelty. Shahula decided to leave it,")
sh(42, "because of the hardships she had been made to bear on the night her beloved child was born into this world, and because of Aamir's unfaithfulness and cruelty.")
sh(43, "When the pains of childbirth began, Aamir was not at home, and though she called him again and again on the phone, he did not answer. Enduring the fierce pain,",
   [("phone_buzz", "ފޯނުން", -20)])
sh(44, "sobbing and weeping, Shahula found a taxi by herself and went to the hospital. This was never the kind of day she had hoped for.",
   [("car_door", "ޓެކްސީއެއް", -20)])
sh(45, "Again and again Shahula thought: if only Aamir's kind mother were still alive today. When she had to be admitted to hospital, the one she called for help was her close friend from the office, Fiyaza.")
sh(46, "Even then there was no word from Aamir. Eight hours after the pains began, the baby was born, a little after two in the morning.")
sh(47, "An emergency arose and a caesarean was needed, but because there was no one to give consent, it was delayed — all because Aamir was not there.")
sh(48, "As the baby's heartbeat dropped and Shahula's own life came into danger, the doctors decided to do the caesarean at once.")
sh(49, "So, taking that responsibility upon herself, Shahula signed the form on her own behalf. Greater than the pain raging in her body",
   [("pen_scribble", "ސޮއިކުރީ", -20)])
sh(50, "was the fear and pain in her heart that, even in this situation, having a caesarean might become a fault in Aamir's eyes.")
sh(51, "When morning came, Shahula woke with a moan of pain. Though Fiyaza was sitting beside her, the little baby's cot beside the bed was empty.",
   [("breath", "އާހަކާ", -22)])
sh(52, "With worried, exhausted eyes Shahula searched all around her. \"My ba... where is my baby?\"")
sh(53, "Shahula asked in a trembling voice. Fiyaza gently held Shahula's hand, to give her strength.")
sh(54, "But seeing Fiyaza's sorrowful face and her eyes brimming with tears, Shahula understood at once what had happened.", hum=True)
sh(55, "With the sudden pain in her heart she bit down hard on her lip. Beginning with a soft sob,",
   [("sob_breath", "ގިސްލުމަކުން", -22)], hum=True)
sh(56, "hot tears streamed down her cheeks from her swollen eyes. And within moments that silent sobbing", hum=True)
sh(57, "turned into loud, aching weeping. Aamir laid the whole blame for this sorrowful loss on Shahula's head.",
   [("sob_breath", "ރޮވުނު", -24)], hum=True)
sh(58, "He accused her with cruel words, saying the baby was lost through her carelessness. Before even five months had passed since the first birth, Shahula was expecting a second time.")
sh(59, "Aamir made no effort whatsoever to understand how dangerous it was for Shahula's health to be expecting again within such a short time.")
sh(60, "And to the doctors' advice and counsel he turned a deaf ear. The second child too had to be born in extreme pain and hardship.")
sh(61, "Besides needing blood, this time too she had to face a caesarean operation. The next morning, when Shahula woke,")
sh(62, "Aamir was sitting at the bedside. The newborn baby was sleeping peacefully in the little cot beside her.")
sh(63, "As Aamir tenderly stroked Shahula's head and asked whether she wanted something to drink,")
sh(64, "Shahula thought that having the baby had brought a good change in his temper. When Shahula nodded,")
sh(65, "Aamir left the room, saying he would bring her a king coconut. But a little while later, the one who came with the king coconut was a boy who worked in the canteen.",
   [("door_close", "ނުކުތެވެ", -22)])
sh(66, "Seeing that, Shahula was utterly astonished. Aamir knew well that she did not have the strength right now to sit up and drink it on her own.")
sh(67, "The boy put the king coconut on the table and went out. Aamir came back to the room about an hour later. As he came close to Shahula,",
   [("cup_clatter", "ބެހެއްޓުމަށްފަހު", -24), ("door_open", "އައީ", -22)])
sh(68, "at the scent of a woman's perfume coming from Aamir, Shahula's eyes widened. In that moment, with many doubts and questions rising in her heart, Shahula looked deep into Aamir's face.",
   [("gasp", "ބޮޑުވިއެވެ", -22)], hum=True)
sh(69, "Shahula's movements were very hurried. Glancing up at the clouds thickening in the sky,",
   [("wind_gust", "ވިލާގަނޑަށް", -20)])
sh(70, "she quickly began taking her little baby's clothes off the line. Then, going inside, without caring for any order, she folded the clothes and stuffed them into the bag beside her.",
   [("cloth_rustle", "ފަތްޖަހައި", -22)])
sh(71, "After that, with quick steps she went to the kitchen and gathered the baby's bottle, the milk tin and other important things.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -22)])
sh(72, "And she also put into the bag the little money she took out of the savings tin. Every few moments her worried eyes turned towards the front door.")
sh(73, "Even when a tree branch swayed with a gust of wind, Shahula's heart leapt into her mouth. Just then, hearing the baby begin to cry in the bedroom,",
   [("wind_gust", "ވައިރޯޅިއަކާ", -18), ("heartbeat", "މޭގަނޑު", -20)])
sh(74, "she hurried to the room. And lifting the baby and holding him to her chest, she opened the wardrobe.",
   [("footsteps_pavement", "އަވަސްވެގަތީ", -22), ("creak", "ހުޅުވައިލިއެވެ", -22)])
sh(75, "Taking off the two bangles Azeeza had put on her wrist, she placed them in the wardrobe drawer. Then, taking the baby's birth certificate and other important papers, as she started walking out of the room,",
   [("paper_shuffle", "ލިޔެކިޔުންތައް", -22)])
sh(76, "with a sudden start, Shahula stopped dead where she stood.",
   [("gasp", "ސިހުމާ", -18), ("heartbeat", "ހުއްޓެވުނެވެ", -20)], hum=True)
SHOTS = S

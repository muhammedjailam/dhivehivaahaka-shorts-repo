"""Beat/shot plan for Marufas episode 544 (used by plan_beats.py)."""

_FROOM = ("Faarish's room at home in the family's large modern island house: a king-size bed with dark cushions and dark "
          "bedding, a large round wall clock WITH NO NUMBERS and no markings on its plain face, a dim bedside lamp, white "
          "walls, a window with a dark curtain")
_LIVING = ("the large formal living room (beyrugey) of the family's large modern island house: a royal-style cream sofa set "
           "with big gold-trimmed cushions, an Italian marble centre table with crystal vases and ornaments, a soft velvet "
           "rug, a big wall-mounted TV (screen dark/black), a glass display showcase, marble floor")
_KITCHEN = ("a large modern kitchen in the family's island house: carved dark-wood cabinets, a long countertop with a "
            "coffee machine and a blender, a big double-door steel fridge, a sink with a cabinet under it, red clay and "
            "steel bowls, marble floor")
_ER = ("the island hospital's emergency room: curtained beds, pale green curtains, a monitor showing abstract green lines "
       "with NO numbers, white walls")
_CORR = ("the island hospital corridor outside the emergency room: plastic chairs along the wall, a large glass window, "
         "pale walls, a polished floor")
_LANE = ("a white sandy island lane between coral-stone walls leading into thick overgrown scrub, palms and breadfruit "
         "trees, a lonely corner of the island")
_ABANDONED = ("a long-abandoned coral-stone house in a lonely overgrown corner of the island: broken wooden shutters, "
              "peeling walls, dust, cobwebs, a dark back room with a single old wooden chair")

LOC = {
    "faarish_room": _FROOM,
    "faarish_room_dark": _FROOM,
    "living_morning": _LIVING,
    "living_rage": _LIVING,
    "kitchen": _KITCHEN,
    "kitchen_after": _KITCHEN,
    "hospital_er": _ER,
    "hospital_corridor": _CORR,
    "island_lane": _LANE,
    "abandoned_house": _ABANDONED,
}
MOOD = {
    "faarish_room": "late at night, dim, cold blue haze with one warm amber bedside lamp, deep shadows, tense and secretive",
    "faarish_room_dark": "late at night, the lamp switched off, near darkness, only a faint cold blue moonlight through a gap in the curtain, heavy and silent",
    "living_morning": "early morning, soft golden sunlight slanting through tall windows, yet a heavy grey stillness and silence in the room, grief and exhaustion",
    "living_rage": "morning, the golden light turned cold and grey, a cold blue haze creeping through the room, harsh contrasts, chaos and terror",
    "kitchen": "morning, cold grey daylight, the harsh white light of the open fridge, a cold blue haze, chaos and dread",
    "kitchen_after": "morning, cold grey light, a quiet broken stillness after chaos, fear and helplessness",
    "hospital_er": "daytime, cold white fluorescent light, pale green tones, urgent and grave",
    "hospital_corridor": "daytime, cold white fluorescent light, long hard shadows, grief turning to fury",
    "island_lane": "late morning, harsh hot tropical sunlight, deep dark shade under the scrub, grim determination",
    "abandoned_house": "daytime, near darkness inside, thin dusty shafts of light through the broken shutters, dust in the air, smoky grey-brown shadows, dread",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
YAM_BACK = ("a small petite girl in a loose long-sleeved ankle-length pale-lilac dress and a white hijab fully covering her "
            "head and neck, seen strictly from behind, her face not visible")

BEATS = [
    # ---------------- NIGHT: FAARISH'S ROOM
    dict(to=3, reason="episode opening: night, Faarish and Adheel whispering in Faarish's dim room", chars=["faarish", "adheel"],
         loc="faarish_room",
         visual="the two young friends in Faarish's dim room at night, both fully dressed: Faarish half-reclining against the dark cushions on the left side of a very wide king-size bed, Adheel sitting cross-legged at the far right edge of the bed, a wide empty stretch of dark bedcover between them; both turned slightly towards each other, whispering, worried faces in the warm glow of the single bedside lamp; the large plain wall clock without numerals on the wall above",
         camera=f"medium wide shot, eye level, {LOW} (dark bedcover in soft shadow)", amb="room_night",
         sens="other", safe="two male friends shown apart on a wide bed, fully dressed, no closeness"),
    dict(to=6, reason="focus change: Faarish lying back staring at the wall clock, voicing his fear", chars=["faarish"],
         loc="faarish_room",
         visual="Faarish lying on his back against the dark cushions, fully dressed in his black long-sleeved t-shirt, one arm behind his head, staring up anxiously at the large plain round wall clock with no numerals, his jaw tight, worry in his eyes, warm lamp light on one side of his face",
         camera=f"medium close shot from the side, slightly high angle, the clock in the upper part of the frame, {LOW}",
         amb="room_night"),
    dict(to=10, reason="action change: Adheel sits up on the edge of the bed and lays out the plan", chars=["adheel", "faarish"],
         loc="faarish_room",
         visual="Adheel sitting upright on the edge of the bed, elbows on his knees, leaning forward and speaking low with a firm, calculating expression; Faarish behind him on the far side of the bed propped up on one elbow, listening intently; a clear distance between them; warm lamp glow and cold blue shadows",
         camera=f"medium shot, eye level, {LOW} (floor in shadow)", amb="room_night"),
    dict(to=12, reason="return: Faarish settles back on the bed and agrees to the plan (reuse of beat_002)", chars=["faarish"],
         loc="faarish_room", reuse="beat_002", visual="reuse", amb="room_night"),
    dict(to=14, reason="time/light change: the lamp is switched off and the room falls into darkness",
         loc="faarish_room_dark",
         visual="Faarish's room in near darkness: the bedside lamp just switched off, the large plain round wall clock with no numerals faintly lit by a thin strip of cold blue moonlight from a gap in the curtain, the dark shapes of the cushions; nobody visible, a heavy silence",
         camera=f"medium shot, eye level, the clock and the curtain gap in the upper half, {LOW}", amb="room_night"),
    # ---------------- MORNING: LIVING ROOM
    dict(to=18, reason="time jump: the next morning, Saahidha alone on the living-room sofa", chars=["saahidha"],
         loc="living_morning",
         visual="Saahidha sitting alone on the big cream gold-trimmed sofa with her head bowed, her eyes puffy and reddened from a night of weeping, hands limp in her lap, staring at nothing; on the marble centre table before her a cup of tea with a thin curl of steam, untouched; golden morning light slanting across the silent room",
         camera=f"medium shot, eye level, {LOW} (the marble table top in soft shadow)", amb="home_day", transition="black"),
    dict(to=21, reason="character enters: sleepless Khalid sits beside her and lays a hand on her shoulder", chars=["khalid", "saahidha"],
         loc="living_morning",
         visual="Khalid, exhausted and sleepless, sitting beside Saahidha on the cream sofa, his hand resting on her shoulder; the two look into each other's eyes in silence, full of unspoken sorrow; the untouched cup of tea steaming on the marble table; golden morning light",
         camera=f"medium shot, eye level, {LOW} (marble table top in soft shadow)", amb="home_day",
         sens="intimacy", safe="married couple sitting side by side, his hand on her shoulder only"),
    dict(to=24, reason="dramatic turn: Yamna's door bursts open, the parents leap up in terror", chars=["saahidha", "khalid"],
         loc="living_rage",
         visual="Saahidha and Khalid springing up from the sofa in shock, turning towards a corridor at the back of the room where a bedroom door has just burst open; in that dark doorway stands a small blurred figure of a girl in a pale-lilac dress and white hijab, her face lost in deep shadow, a cold blue haze spilling out of the room behind her; the parents' faces frozen in fear",
         camera=f"medium wide shot, eye level, the parents in the foreground and the doorway in the background, {LOW}",
         amb="haunted_living", sens="other",
         safe="possession shown only through the parents' terror, cold haze and a shadowed blurred figure; no wild hair, no reddened eyes"),
    dict(to=27, reason="action change: the rampage begins, crystal smashed against the wall", chars=["yamna"], loc="living_rage",
         visual=f"{YAM_BACK}, standing alone in the middle of the grand living room facing the far wall; glittering crystal fragments flying from the wall and scattered across the soft velvet rug, an overturned crystal vase on the marble table, the big wall TV dark with a crack across its black screen; cold grey light",
         camera=f"medium wide shot from behind her, eye level, {LOW} (rug in shadow)", amb="haunted_living",
         sens="violence", safe="bible rule 6: only the smashed crystal and the cracked dark TV, Yamna from behind, nothing hurt"),
    dict(to=29, reason="aftermath: the beautiful room wrecked (showcase glass, ripped cushions)", loc="living_rage",
         visual="an EMPTY wrecked grand living room, a still-life of objects only with absolutely no people, no figures and no silhouettes anywhere in the frame: the glass display showcase broken with jagged empty panes, the big gold-trimmed sofa cushions ripped open with white stuffing spilling out, crystal shards glinting on the velvet rug, a cracked dark TV on the wall, ornaments strewn on the marble floor",
         camera=f"wide shot, slightly high angle, {LOW} (floor in deep shadow)", amb="haunted_living",
         sens="violence", safe="bible rule 6: destruction shown as objects only; her bleeding hands are never shown"),
    dict(to=32, reason="action change: Saahidha shoved to the floor, Khalid fails to hold Yamna", chars=["saahidha", "khalid"],
         loc="living_rage",
         visual="Saahidha sitting on the marble floor where she has fallen, propped on one hand, unhurt but stunned, her other hand at her mouth; behind her Khalid lunging forward with both arms outstretched towards a small blurred figure in a pale-lilac dress and white hijab who is darting away out of the frame; crystal shards on the rug",
         camera=f"medium shot, low eye level, {LOW}", amb="haunted_living",
         sens="violence", safe="the shove is not shown; Saahidha is shown on the floor in shock, unhurt; Yamna only a blurred passing figure"),
    # ---------------- KITCHEN
    dict(to=37, reason="scene change: Yamna runs into the kitchen (the family's dreaded habit explained)", chars=["yamna"],
         loc="kitchen",
         visual=f"{YAM_BACK}, rushing through the doorway into the large dim kitchen, the carved dark-wood cabinets, long countertop with coffee machine and blender and the big double-door steel fridge ahead of her in cold grey light",
         camera=f"medium wide shot from behind her, eye level, {LOW} (marble floor in shadow)", amb="haunted_living",
         sens="other", safe="her craving is told by the narrator only; the image shows her from behind entering the kitchen"),
    dict(to=40, reason="action change: she wrenches open the fridge and smashes its contents", chars=["yamna"], loc="kitchen",
         visual=f"{YAM_BACK}, standing before the wide-open double-door steel fridge, its harsh white light spilling over her; around her feet on the marble floor smashed glass juice bottles, burst tomatoes, scattered vegetables and rolling fruit; the shelves inside half empty",
         camera=f"medium shot from behind her, eye level, {LOW} (floor in shadow)", amb="haunted_living",
         sens="other", safe="bible rule 4: fridge light, aftermath on the floor, Yamna from behind"),
    dict(to=43, reason="aftermath: appliances thrown down, bowls scattered, every cabinet open", loc="kitchen_after",
         visual="an EMPTY ransacked kitchen, a still-life of objects only with absolutely no people, no figures and no silhouettes anywhere in the frame: every carved dark-wood cabinet door hanging open, a fallen blender and an overturned coffee machine on the marble floor, scattered stainless steel pots and red clay bowls, broken fruit and vegetables, the open cabinet under the sink in the corner",
         camera=f"wide shot, eye level, cabinets and countertop in the upper part, {LOW} (floor fading into deep shadow)",
         amb="haunted_living", sens="other", safe="bible rule 4: aftermath only"),
    dict(to=47, reason="emotional turning point: the family's horror at what she found under the sink",
         chars=["saahidha", "khalid", "faarish"], loc="kitchen",
         visual="in the kitchen doorway Saahidha, Khalid and Faarish recoil in horror: Saahidha with both hands pressed over her mouth, sinking at the knees, Khalid's arm thrown out, Faarish frozen in shock; in the out-of-focus foreground a small girl in a pale-lilac dress and white hijab crouches before the open cabinet under the sink, her back to the camera, nothing visible in her hands; cold grey light",
         camera=f"medium shot, eye level, the family's faces in the upper third, {LOW}", amb="haunted_living",
         sens="other", safe="bible rule 4: only the family's horror and Yamna's back; nothing she eats is ever shown"),
    dict(to=49, reason="action change: the poisoning sets in, her strength drains away, her mother holds her",
         chars=["yamna", "saahidha", "khalid"], loc="kitchen_after",
         visual="Saahidha kneeling on the kitchen floor holding Yamna in her arms; Yamna limp and weak against her mother, pale, eyes half-closed, fully clothed in her pale-lilac dress and white hijab; Khalid kneeling beside them, anxious, holding a phone with a blank dark screen to his ear; open cabinets behind",
         camera=f"medium shot, low eye level, {LOW}", amb="home_day",
         sens="other", safe="food poisoning shown only as pallor and weakness in her mother's arms; no vomiting, no darkened face"),
    # ---------------- HOSPITAL
    dict(to=50, reason="scene change: rushed into the hospital emergency room", chars=["yamna"], loc="hospital_er",
         visual="Yamna lying on an emergency-room bed in a modest long-sleeved pale-blue hospital gown and white hijab, a blanket up to her chest, pale and eyes closed, a thin clear oxygen nasal line; a doctor in green scrubs and a nurse in scrubs with a hijab bending over her, urgently checking; a monitor with abstract green lines and no numbers; pale green curtains",
         camera=f"medium shot, slightly high angle, {LOW} (blanket edge in soft shadow)", amb="hospital_day",
         sens="other", safe="bible rule 10: no needles, no tubes in the mouth, abstract monitor"),
    dict(to=52, reason="scene/focus change: Faarish alone in the corridor, grief turning to rage", chars=["faarish"],
         loc="hospital_corridor",
         visual="Faarish standing alone in the hospital corridor beside a row of empty plastic chairs, his back against the pale wall, head lowered then lifting, fists clenched, his face torn between grief and rising fury, tears in his eyes",
         camera=f"medium shot, eye level, {LOW} (polished floor in shadow)", amb="hospital_corridor"),
    dict(to=54, reason="character enters: Faarish grips Adheel's arm — 'Let's go'", chars=["faarish", "adheel"],
         loc="hospital_corridor",
         visual="in the hospital corridor Faarish gripping Adheel's forearm hard, leaning towards him, his eyes burning with fury and tears, jaw clenched, speaking through his teeth; Adheel serious and grim, nodding",
         camera=f"medium close shot, eye level, {LOW}", amb="hospital_corridor",
         sens="violence", safe="his murderous intent is spoken only; shown as a furious face"),
    # ---------------- ABANDONED HOUSE
    dict(to=56, reason="scene change: the two young men stride to the abandoned house", chars=["faarish", "adheel"],
         loc="island_lane",
         visual="Faarish and Adheel striding fast side by side down a white sandy lane into thick overgrown scrub, grim determined faces, harsh sunlight and deep shade, the ruined coral-stone house half hidden in the bushes ahead",
         camera=f"medium wide shot from the front at a slight angle, eye level, {LOW} (sandy lane in shade)",
         amb="island_day", transition="dissolve"),
    dict(to=58, reason="scene change: the door flung open on the frightened old man", chars=["aadhanbe"], loc="abandoned_house",
         visual="inside the dark dusty back room of the abandoned house: the weathered wooden door just flung open, a hard shaft of daylight falling across the floor onto Aadhanbe sitting alone on a single old wooden chair, startled and frightened, eyes wide, hands resting in his lap, his white shirt, checked sarong and white cap clean, unhurt; peeling walls, cobwebs, broken shutters",
         camera=f"medium wide shot from the doorway, eye level, {LOW} (dusty floor in shadow)", amb="abandoned_house",
         sens="violence", safe="bible rule 3: no ropes or binding, he sits alone, clean and unhurt"),
    dict(to=61, reason="focus change: Faarish's fury in the dark room, Adheel threatening", chars=["faarish", "adheel"],
         loc="abandoned_house",
         visual="Faarish's furious face half in shadow in the dark dusty room, shouting, fists clenched at his sides, a thin shaft of light across his eyes; Adheel standing just behind his shoulder, grim and threatening; the old wooden chair only a dim shape far away in the background",
         camera=f"medium close shot, slightly low angle, {LOW}", amb="abandoned_house",
         sens="violence", safe="bible rule 3: the collar grab and the blow are never shown — only Faarish's furious face at a distance; a muffled offscreen thud"),
    dict(to=64, reason="focus change: the old man pleads, weeping", chars=["aadhanbe"], loc="abandoned_house",
         visual="close shot of Aadhanbe on the old wooden chair, tears running down his deeply wrinkled face, eyes squeezed shut, pleading, his hands clasped together in his lap, his white shirt and cap clean, no marks on him; dust in a thin shaft of light; dark peeling walls",
         camera=f"medium close shot, eye level, {LOW}", amb="abandoned_house",
         sens="violence", safe="bible rule 3: no blood, no injuries; only his frightened, tearful face"),
    dict(to=65, reason="memory flash: his sister fighting for life in hospital (reuse of beat_017)", chars=["yamna"],
         loc="hospital_er", reuse="beat_017", visual="reuse", amb="memory", transition="dissolve"),
    dict(to=69, reason="action change: starved and exhausted, he begs for water", chars=["aadhanbe"], loc="abandoned_house",
         visual="Aadhanbe slumped exhausted on the old wooden chair, his tired face drawn and hollow, parched lips, half-closed tearful eyes gazing down at an empty dusty tin cup lying on its side on the dusty floor near the chair leg; clean and unhurt; faint dusty light through the broken shutters",
         camera=f"medium shot, eye level, his face in the upper third, the cup in the middle of the frame, {LOW}",
         amb="abandoned_house", transition="dissolve",
         sens="other", safe="bible rule 3: starvation shown as his tired face and an empty dusty cup"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "In the dim light of the room, Faarish and Adheel were lying on the big king-size cushioned bed in their room.")
sh(2, "Unlike the silence that ruled the whole atmosphere, a great unease had arisen in the hearts of the two.")
sh(3, "They were quietly discussing what to do next about Aadhanbe. If what had been done to Aadhanbe came out,")
sh(4, "they were sure a great uproar would break out across the whole island. \"Adheel! I don't think that Aadhanu will stay quiet so easily,\" Faarish whispered, lying there staring at the big clock fixed on the wall.")
sh(5, "\"If someone finds him lying there, there'll be terrible trouble!\" Faarish let out the unease that had taken hold of his heart.",
   hum=True)
sh(6, "\"Don't worry so much, Faarish! We didn't leave him where people could find him easily. But...")
sh(7, "we can't keep him there forever. We have to do something.\" Adheel let out a deep breath, got up and sat on the bed.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(8, "\"What way? Do we send him off the island? Or...\" Faarish asked quickly. \"No, if we send him off the island, the police will get involved,\"")
sh(9, "Adheel's voice was firm. \"What we have to do is frighten Aadhanbe. We must shut his mouth by telling him we hold proof of his deceit and sorcery.")
sh(10, "Otherwise there's no way out of this.\" Adheel had come up with a clever plan. \"That's exactly the best way,\" Faarish nodded, settling back on the bed.",
   [("cloth_rustle", "ހަމަޖެހިލަމުން", -22)])
sh(11, "\"Tomorrow at sunrise we'll go to Aadhanbe. We'll tell him we have proof of all the evil he has done,")
sh(12, "and give him a fright strong enough to hold his tongue. Then he'll be in our fist.\"")
sh(13, "Adheel nodded in agreement too and switched off the light. To be ready for the big task tomorrow,",
   [("flashlight_click", "ނިވާލިއެވެ", -22)])
sh(14, "both stopped talking and closed their eyes to try to sleep. As black darkness filled the room, their hearts held only the resolve to carry out tomorrow's plan.")
sh(15, "The next morning an unusual mood hung over the house. Though the golden light of the sun spread into the rooms,")
sh(16, "unease and a deep silence ruled the whole house. After last night's terrifying events, there was no life on anyone's face.")
sh(17, "Saahidha sat on the sofa of their fine living room with her head bowed. Her eyes were red and swollen from crying.")
sh(18, "Though steam rose from the hot cup of tea on the table in front of her, she had no thought of drinking even a sip.")
sh(19, "Khalid came out of the room with slow steps. His body showed the exhaustion of too little sleep.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައެވެ", -24)])
sh(20, "He sat down beside Saahidha and, without a word, laid his hand on her shoulder. As the couple's eyes met,",
   hum=True)
sh(21, "countless griefs and sorrows that no words could express passed from one to the other. Suddenly Yamna's door was flung open with force,",
   [("door_slam", "ހުޅުވާލުމަށްފަހު", -15)])
sh(22, "and she came out of her room. Her wild hair and her red, swollen eyes did not look human.", hum=True)
sh(23, "Her whole body shook with rage. She came out into the living room. \"Get away! Everyone get away!\"",
   [("low_growl", "ދުރަށްދޭ", -20)])
sh(24, "The voice coming out of Yamna's throat was not the voice of an ordinary human. Like someone without a single thought, with unnatural strength,")
sh(25, "she seized the crystal vases and ornaments decorating the \"Italian marble\" table in the middle of the living room and smashed them to pieces against the wall.",
   [("glass_break", "ފުނޑުފުނޑުކޮށްލިއެވެ", -15)])
sh(26, "Shards of crystal scattered over the soft velvet rug on the floor. After that,")
sh(27, "she hurled things at the big theatre-screen TV fixed on the wall and destroyed its display too.",
   [("crash_clatter", "ހަލާކުކޮށްލިއެވެ", -16)])
sh(28, "When she smashed the glass of the showcase beside it with both hands, blood ran from her hands. Yet she seemed to feel no pain at all.",
   [("glass_break", "ފަޅާލިއިރު", -16)])
sh(29, "Ripping the big cushions of the royal sofa set and scattering debris all over the living room, in a moment she turned the beauty of that big house to ruin.",
   [("cloth_rustle", "ވީދާ", -18)])
sh(30, "\"Kamana! My child!\" Saahidha screamed in fear and tried to hold Yamna in her arms.",
   [("gasp", "ހަޅޭއްލަވައިގަންނަމުން", -18)])
sh(31, "But with unnatural strength Yamna shoved Saahidha away. Saahidha was flung down onto the floor.",
   [("soft_thud", "ވެއްޓުނީ", -20)])
sh(32, "Khalid ran and tried to hold Yamna's arms, but he could not control her. Breaking free of Khalid's grip,")
sh(33, "slipping out of his arms, Yamna then ran towards the kitchen. This is what usually happens on these terrifying days when she changes",
   [("footsteps_pavement", "ދުއްވައިގަތީ", -22)])
sh(34, "and darkness takes hold. It is a dangerous habit the family has come to know.")
sh(35, "In this state her whole body craves raw fish and its blood. Somehow or other her heart begins to crave a piece of raw fish.")
sh(36, "Because of this terrible habit of Yamna's, the house no longer keeps raw fish frozen in storage. Even when fish is brought from the market,")
sh(37, "they take care to cook it as fast as they can before it catches Yamna's eye. Entering the kitchen,")
sh(38, "throwing things in every direction, Yamna hunted for that foul food of hers. She ran to the big double-door fridge in the kitchen.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -22)])
sh(39, "She wrenched its doors open with force, and the vegetables, the fruit,",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -18)])
sh(40, "and the drinks in glass bottles inside she grabbed and smashed to pieces on the floor. There was not a trace of the raw fish she wanted.",
   [("glass_break", "ފުނޑުފުނޑުކޮށްލިއެވެ", -16)])
sh(41, "At that her rage grew even stronger, and she swept the expensive coffee machine and electric appliances like the blender off the countertop onto the floor.",
   [("crash_clatter", "ވައްޓާލިއެވެ", -16)])
sh(42, "Stainless steel pots and red clay bowls struck the floor, and the noise rang through the whole house.",
   [("cup_clatter", "ޖެހި", -15)])
sh(43, "Flinging open the doors of the carved wooden cabinets of that spacious kitchen and throwing out everything inside, her steps stopped at the rubbish bin under the sink.",
   [("creak", "ހުޅުވަމުން", -20)])
sh(44, "Seeing the fish guts and raw blood thrown in there when fish was cut that morning, a terrifying smile spread over Yamna's face.",
   [("heartbeat", "ހިނިތުންވުމެކެވެ", -20)], hum=True)
sh(45, "As everyone watched, as if without a single thought, she took the raw guts and began putting them in her mouth.", hum=True)
sh(46, "As the blood ran down her chin, she chewed with unnatural force. \"Kamana! Don't... what a terrible thing that is!\"",
   [("sob_breath", "ހެޔޮނުވާނެ", -20)])
sh(47, "Saahidha, retching and sobbing loudly, sank to the floor. Khalid and Faarish ran to pull Yamna away, but screaming, she shoved them all off.",
   [("sob_breath", "ރޮއިގަންނަމުން", -18)])
sh(48, "But before long, changes began to come over Yamna's body. Because of food poisoning her stomach cramped,")
sh(49, "her face darkened and she began to vomit. By then the unnatural strength that had come over Yamna was fading too.", hum=True)
sh(50, "Through everyone's efforts, Yamna was soon taken to the hospital. When she was brought into the emergency room, her condition was extremely bad.",
   [("siren", "ހޮސްޕިޓަލަށް", -20)])
sh(51, "Standing in the hospital corridor, Faarish's heart was breaking. Seeing his beloved little sister's pitiful, terrible state, an indescribable anguish and sobbing rose in his heart.",
   hum=True)
sh(52, "That grief suddenly turned into rage of the highest degree. It came to his mind that the root of all this was Aadhanbe.",
   hum=True)
sh(53, "His heart began to cry out for revenge for the great cruelty and pain his little sister was suffering. With eyes red as a clot of blood, Faarish went and gripped Adheel's arm hard.")
sh(54, "\"Let's go! Today I won't leave that filthy Aadhanu in this world,\" Faarish said with hatred, grinding his teeth. Adheel nodded too.",
   [("breath_heavy", "ވިކާލަމުން", -20)])
sh(55, "The two young men left the hospital and, with heavy steps, headed for the abandoned house where Aadhanbe was held captive.",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -20)])
sh(56, "In their hearts was a spirit of cruelty and revenge. No memory remained of anything planned in the night.")
sh(57, "Faarish and Adheel went almost at a run, entered the abandoned house, and flung open the door of the room where Aadhanbe was held.",
   [("door_slam", "ހުޅުވާލިއެވެ", -15)])
sh(58, "In the darkness of the room, Aadhanbe, bound to the chair, jolted in fear when he saw them.",
   [("gasp", "ސިހިގެން", -18)])
sh(59, "Seeing the dangerous rage on Faarish's face, his heart almost stopped. \"What evil sorcery did you do to my little sister?\"",
   [("heartbeat", "ހުއްޓުނު", -20)], hum=True)
sh(60, "Shouting, Faarish went, seized Aadhanbe by the collar of his shirt and yanked him up. And without any mercy he struck a hot blow on his temple.",
   [("cloth_rustle", "ދަމައިގަތެވެ", -22), ("soft_thud", "ވިއްސައިލައިފިއެވެ", -24)])
sh(61, "Adheel too stood close by, warning Aadhanbe. \"If you don't tell the truth today, you won't get out of here alive! Where is the source of your sorcery?")
sh(62, "Why are you doing this to Yamna?\" Unable to bear the cruelty he was suffering, moans of pain came out of Aadhanbe's throat.")
sh(63, "As blood ran from his face and mouth, he shut his eyes and began begging for mercy. \"Don't... Faarish!",
   [("sob_breath", "އާދޭސްކުރަން", -20)])
sh(64, "Adheel! Don't do this... don't put my old body through such cruelty! Let me go!\" Aadhanbe, weeping,")
sh(65, "begged in a trembling voice. But it made no impression on Faarish's heart. Every time the sight of his sister fighting for her life in hospital rose before his eyes, the strength in his arm grew.",
   hum=True)
sh(66, "From the hunger of a night and a day and the cruelty he had suffered, Aadhanbe's strength was almost completely spent.")
sh(67, "His throat was parched, his body utterly weak. At last, all his strength gone, tears streaming from his eyes, he began to plead helplessly.",
   [("breath", "ކެނޑި", -22)])
sh(68, "\"I'm dying... please, give me a bite of food... give me even a little drop of water... I'm dying...\"",
   [("sob_breath", "މަރުވަނީ", -22)], hum=True)
sh(69, "With eyes full of tears, Aadhanbe begged Faarish and Adheel for a drop of water and a bite of food. (To be continued)")
SHOTS = S

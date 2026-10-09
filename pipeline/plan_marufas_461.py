"""Beat/shot plan for Marufas episode 461 (used by plan_beats.py)."""

ROOM = ("Yamna's spacious bedroom in the family's large modern island house: white walls, polished white marble floor, "
        "a big bed with white sheets and a pale headboard, a study desk with books and pens under the window, a tall "
        "dark-wood wardrobe, a glass sliding window beside the bed with a sheer white curtain, a round ceiling light")

LOC = {
    "kitchen": "a large modern kitchen in the family's island house: carved dark-wood cabinets, a long countertop with a coffee machine and a blender, a big double-door steel fridge with its freezer section, a sink, red clay and steel bowls, polished marble floor",
    "hospital": "the island hospital emergency room: curtained beds with pale-green curtains, a plain white wall, a small bedside monitor showing only abstract green lines and no numbers",
    "veranda": "the front veranda (fendaa) of the family's large modern island house with a big wooden swing bench, potted plants, a sandy yard and flowering trees by the boundary wall, palms beyond",
    "yamna_eve": ROOM,
    "yamna_room": ROOM,
    "living": "the large formal living room: a royal-style cream sofa set with big gold-trimmed cushions, an Italian marble centre table with crystal vases and ornaments, a soft velvet rug, a big wall-mounted TV with a black screen, a glass display showcase, marble floor",
    "corridor": "the wide marble-floored corridor of the family's large modern island house outside Yamna's closed bedroom door: a tall plain dark-wood door, white walls, polished white marble floor",
}
MOOD = {
    "kitchen": "early afternoon, the kitchen shuttered and dim with grey daylight at the window, the cold white light of the open freezer spilling across the floor and faces, icy and shocking",
    "hospital": "afternoon, flat cool fluorescent light, pale-green tones, hushed and uneasy",
    "veranda": "sunset, a heavy ominous dark-orange and bruised-purple sky with brooding low clouds, long black shadows across the sand, the palms as dark silhouettes, threatening stillness",
    "yamna_eve": "early evening, one warm bedside lamp, soft amber light against cool blue shadows, a fragile calm",
    "yamna_room": "midnight, the ceiling light dimmed almost dark, one weak flickering lamp, a cold blue haze hanging in the room, deep charcoal shadows, dread",
    "living": "night after the isha prayer, dim, a cold blue haze with one warm floor lamp, tense and solemn",
    "corridor": "midnight, the corridor almost dark, a cold blue haze, a thin strip of faint flickering light under the closed door, lonely and frightening",
}

LOW = "faces in the upper two-thirds, a calm dark lower third"
YAM = "Yamna (pale, tired, dark circles under her eyes, but unhurt) in her pale-lilac long-sleeved dress and white hijab fully covering her hair and neck"
BED = "lying in bed under a white blanket up to her chest, her white hijab fully covering her hair and neck"

BEATS = [
    # ---------------- AFTERNOON: THE FREEZER
    dict(to=3, reason="episode opening: Yamna storms into the kitchen and yanks open the freezer; the men rush in",
         chars=["yamna", "khalid", "ghassan", "saahidha"], loc="kitchen",
         visual="seen from behind: Yamna, a petite girl in her pale-lilac ankle-length dress and white hijab, standing rigid in front of the big steel fridge with its freezer door flung wide open, the cold white freezer light glowing around her silhouette, her hands hidden in front of her body; in the kitchen doorway Khalid and Ghassan lunge forward with outstretched arms and Saahidha behind them freezes with a hand over her mouth, all lit by the icy freezer glow",
         camera=f"medium wide shot from behind Yamna's shoulder towards the doorway, eye level, {LOW} (marble floor in shadow)",
         amb="haunted_living", sens="other",
         safe="bible rule 4: open freezer light, Yamna only from behind, no food in her hands, the family recoiling; the eating is never shown"),
    dict(to=7, reason="framing change: the family's horrified reactions to the impossible sight (no Yamna in frame)",
         chars=["saahidha", "khalid", "ghassan"], loc="kitchen",
         visual="Saahidha, Khalid and Ghassan pressed back against the carved dark-wood cabinets, recoiling in horror, their faces lit cold white by the light of the open freezer off-frame: Saahidha with both hands over her mouth and tears in her eyes, Khalid pale and trembling with his hand on her shoulder, Ghassan staring with narrowed, calculating eyes; a fallen steel bowl on the floor",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)",
         amb="haunted_living", sens="other", safe="the raw-food eating is shown only through the family's horrified faces"),
    dict(to=10, reason="character enters and action change: Yamna has collapsed; Faarish arrives from Malé, horrified",
         chars=["faarish", "saahidha", "yamna", "khalid"], loc="kitchen",
         visual="Faarish, just arrived with a small travel backpack on one shoulder, standing in the kitchen doorway, horrified, one hand raised and calling out urgently; in front of him Yamna lies still on her side on the marble floor as if asleep, fully clothed in her pale-lilac dress and white hijab, her face turned away and hidden, unhurt; Saahidha kneels beside her holding her hand, Khalid crouches behind them looking up at his son; the freezer door hangs open, casting cold light",
         camera=f"medium wide shot, eye level, Faarish's face in the upper third, {LOW}",
         amb="haunted_living", sens="other",
         safe="her collapse is shown with her lying peacefully, face turned away, fully clothed; no foam, no rolled eyes"),
    dict(to=11, reason="scene change: the ambulance outside the house rushing her to hospital",
         loc="veranda",
         visual="a white ambulance with flashing lights parked at the gate of the large modern island house in the grey afternoon, rear doors open, two paramedics in navy uniforms seen from behind hurrying an empty wheeled stretcher towards the front door, a young man in a black long-sleeved tee and jeans running alongside; the patient is not visible",
         camera="wide shot from the sandy lane, eye level, the house and ambulance in the upper two-thirds, the white sand as the calm lower third",
         amb="island_day", sens="other",
         safe="the vomiting is never shown; only the ambulance and paramedics from behind, patient hidden"),
    dict(to=13, reason="scene change: hospital emergency room, first aid; Yamna strangely calm, like a lifeless doll",
         chars=["yamna", "saahidha"], loc="hospital",
         visual="Yamna sitting up in a curtained emergency-room bed in a modest long-sleeved pale-blue hospital gown and her white hijab fully covering her hair and neck, a pale-blue blanket over her legs, pale with dark circles under her eyes, sitting perfectly still with a blank doll-like stare into nothing, hands limp in her lap; Saahidha sits at the bedside holding her hand and searching her face anxiously; a nurse in light-blue scrubs and a navy hijab draws the curtain in the background",
         camera=f"medium shot, eye level, {LOW} (blanket edge)",
         amb="hospital_day", transition="dissolve"),
    dict(to=14, reason="time change: an ominous sunset over the house, as if declaring war on the family",
         loc="veranda",
         visual="the family's large island house and its empty veranda with the big wooden swing bench at sunset, the swing hanging still, a heavy dark-orange and bruised-purple sky with brooding clouds above the dark palms, long black shadows stretching across the sandy yard; no people",
         camera="wide shot, slightly low angle, the sky and house in the upper two-thirds, the darkening sand as the calm lower third",
         amb="beach_dusk", transition="black"),
    dict(to=17, reason="action change: at home, Saahidha has bathed and dressed Yamna and feeds her — the only calm moment",
         chars=["saahidha", "yamna"], loc="yamna_eve",
         visual=f"{YAM}, freshly washed and neatly dressed in a clean pale-lilac dress, her white hijab pinned neatly, sitting quietly on the edge of her tidy bed with a calm, empty, doll-like expression; Saahidha sits beside her lovingly feeding her a spoonful of rice porridge from a small bowl, a tender, tired smile on her face",
         camera=f"medium shot, eye level, {LOW} (white bedsheet edge in shadow)",
         amb="room_night"),
    # ---------------- NIGHT: THE RECITATION
    dict(to=19, reason="time jump to night after isha: Ghassan briefs Khalid, Faarish and Adheel before the midnight recitation",
         chars=["ghassan", "khalid", "faarish", "adheel"], loc="living",
         visual="Ghassan standing in the dim living room with his big black leather bag on his shoulder, speaking gravely with one finger raised; Khalid (wearing a white skullcap, just back from prayer), Faarish and Adheel stand around him listening tensely, Adheel taking a deep breath to steel himself; the cream sofas and the marble table in the background",
         camera=f"medium wide shot, eye level, {LOW} (velvet rug in shadow)",
         amb="living_night", transition="black"),
    dict(to=21, reason="action change: Saahidha hugs Yamna tightly in bed, praying, before she must leave",
         chars=["saahidha", "yamna"], loc="yamna_room",
         visual=f"Saahidha sitting on the edge of the bed hugging Yamna tightly to her chest, eyes closed, lips moving in prayer, tears on her cheeks; Yamna {BED}, sitting half up against the pillows inside her mother's embrace, her pale face blank and still; the room dim with one weak lamp",
         camera=f"medium close shot, eye level, {LOW} (blanket in shadow)",
         amb="room_night"),
    dict(to=24, reason="scene change: Saahidha shuts the door and slides down to sit on the floor outside, back against the door",
         chars=["saahidha"], loc="corridor",
         visual="Saahidha sitting alone on the marble floor of the dark corridor with her back against Yamna's closed bedroom door, her knees drawn up, arms wrapped around her knees, her beige hijab and bottle-green dress, her tear-streaked face turned slightly towards the door, listening, every muscle tense; a thin strip of faint light under the door beside her",
         camera=f"medium wide shot, eye level, the door and her face in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="haunted_living", hum=True),
    dict(to=27, reason="scene change: inside, lights dimmed, Ghassan sits by Yamna's head murmuring; the men stand by",
         chars=["ghassan", "yamna", "khalid", "faarish"], loc="yamna_room",
         visual=f"the dim bedroom: Ghassan sitting on a chair at the head of the bed, his right palm held up in the air a hand's width above Yamna's forehead with a clear gap, not touching her, lips moving in a murmur, eyes half closed; Yamna {BED}, eyes closed, still — she is the only girl in the room and appears only once, lying in the bed; standing behind are only three men: Khalid and Faarish at the foot of the bed and a young man with curly hair in an olive-green shirt in the shadows by the wardrobe; no women or girls standing anywhere; his black leather bag on the floor by the chair",
         camera=f"medium wide shot, eye level, {LOW} (bedsheet edge in shadow)",
         amb="haunted_room", sens="other", safe="bible rule 7: palm hovering, no book or text"),
    dict(to=29, reason="framing change: the terrible voice screams; outside, Saahidha presses her hands over her ears",
         chars=["saahidha"], loc="corridor",
         visual="close-up of Saahidha sitting against the closed door in the dark corridor, both hands pressed hard over her ears on top of her beige hijab, eyes squeezed shut, her whole body shaking, tears on her cheeks",
         camera=f"close-up, eye level, {LOW} (her knees and the dark floor)",
         amb="haunted_living", hum=True),
    dict(to=31, reason="detail change: sounds of breaking inside and an icy cold seeping out under the door",
         loc="corridor",
         visual="the closed dark-wood bedroom door seen low from the corridor floor: a pale icy mist creeping out from the gap under the door and spreading across the polished marble, frost forming on the floor, the strip of light under the door flickering; at the very edge of frame the hem of a bottle-green dress; no faces",
         camera="low-angle close shot along the floor, the door in the upper two-thirds, the misty marble floor as the calm lower third",
         amb="haunted_living", sens="other", safe="the struggle inside and the men holding Yamna are never shown; only sound and the cold mist under the door"),
    dict(to=35, reason="framing change: Saahidha, head leaning back on the door, chin raised, prays silently through tears",
         chars=["saahidha"], loc="corridor",
         visual="Saahidha sitting on the floor with the back of her head resting against the closed door, chin lifted, eyes closed, tears running down her cheeks, her hands cupped in front of her chest in silent prayer, her breath visible as faint mist in the cold blue air",
         camera=f"medium close-up, slightly low angle, {LOW} (her knees and the dark floor)",
         amb="haunted_living", hum=True),
    dict(to=38, reason="scene change inside: the possession peaks — flickering light, a smoky shadow on the wall, the men frozen",
         chars=["ghassan", "khalid", "faarish"], loc="yamna_room",
         visual="the dim bedroom in a flickering half-dead light and a cold blue haze: on the white wall above the bed a huge dark smoky shadow spreads with long thin shadowy fingers reaching out, faceless and formless, touching no one; Ghassan leans forward from his chair, reciting fast with his palm raised; Khalid and Faarish shrink back by the wardrobe, terrified; in the bed only a small shape under the crumpled white blanket, a white hijab on the pillow, the face turned away into shadow",
         camera=f"medium wide shot, eye level, the shadow on the wall in the upper half, {LOW}",
         amb="haunted_room", sens="other",
         safe="bible rules 1 and 14: no binding, no convulsion, no rolled eyes; possession shown by the smoky shadow (use 1 of 2), the flickering light and the men's fear"),
    dict(to=42, reason="framing change: Ghassan interrogates the jinn — 'Who are you? Who sent you?'",
         chars=["ghassan"], loc="yamna_room",
         visual="close-up of Ghassan sitting by the bed in the flickering light, leaning forward, his narrow eyes blazing with fierce anger, one palm raised commandingly, lips moving fast, shadows jumping across his angular face; behind him the blurred dark shapes of two men standing",
         camera=f"close-up, slightly low angle, {LOW} (the white sheet in shadow)",
         amb="haunted_room"),
    dict(to=45, reason="action change: a terrible scream, the room seems to heave; the jinn begs 'don't hurt me'",
         chars=["khalid", "faarish", "adheel"], loc="yamna_room",
         visual="Khalid, Faarish and Adheel stumbling back in horror, faces lit by a flickering bulb, Faarish shielding his face with his forearm; beside the bed the sheer white curtain billows violently inward though the window is shut, the white blanket on the bed lifts and ripples, books slide off the desk; the girl in the bed is out of frame",
         camera=f"medium wide shot, eye level, {LOW} (marble floor in shadow)",
         amb="haunted_room", sens="other",
         safe="her body rising off the bed is never shown: only the curtain billowing, the blanket rippling and the men recoiling"),
    dict(to=46, reason="back to Saahidha outside, trembling at the pleading voice", reuse="beat_012", chars=["saahidha"],
         loc="corridor", visual="reuse of beat_012", amb="haunted_living"),
    dict(to=49, reason="back inside: the long battle of words, the jinn shaking the doors and windows", reuse="beat_015",
         chars=["ghassan", "khalid", "faarish"], loc="yamna_room", visual="reuse of beat_015", amb="haunted_room"),
    dict(to=51, reason="emotional turning point: the jinn names 'the old man of this island, Aadhanbe' through Yamna",
         chars=["yamna"], loc="yamna_room",
         visual="close-up of Yamna's face on the white pillow, her white hijab fully covering her hair and neck, the blanket up to her chest: pale, with dark circles under her eyes, completely still, her eyes open and staring at the ceiling with a cold empty stare, lips slightly parted, lit by a weak flickering blue light; no marks on her face",
         camera=f"close-up from slightly above, {LOW} (blanket in shadow)",
         amb="haunted_room", sens="other", safe="bible rule 1: a calm, blank, unmarked face with a cold stare stands for the jinn speaking; Aadhanbe is not shown", hum=True),
    dict(to=54, reason="character change: Khalid, Faarish and Adheel exchange looks of disgust — the jinn lied before",
         chars=["faarish", "khalid", "adheel"], loc="yamna_room",
         visual="Khalid, Faarish and Adheel standing together in the dim room exchanging hard sceptical glances, faces full of disgust and disbelief, Faarish's jaw clenched and his eyes burning, Adheel shaking his head slightly, Khalid frowning darkly",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)",
         amb="haunted_room"),
    dict(to=56, reason="back to Saahidha outside the door, who thinks the same: the jinn blames an innocent old man",
         reuse="beat_010", chars=["saahidha"], loc="corridor", visual="reuse of beat_010", amb="haunted_living"),
    dict(to=58, reason="back inside: the angry jinn thrashes as if to lift her off the bed", reuse="beat_017",
         chars=["khalid", "faarish", "adheel"], loc="yamna_room", visual="reuse of beat_017", amb="haunted_room"),
    dict(to=60, reason="back to Ghassan's final threat; Yamna faints", reuse="beat_016", chars=["ghassan"],
         loc="yamna_room", visual="reuse of beat_016", amb="haunted_room"),
    dict(to=61, reason="action change: the cold fades; Khalid lays a blanket over Yamna and asks Faarish to open the door",
         chars=["khalid", "yamna", "faarish"], loc="yamna_room",
         visual=f"the light steadier and warmer now: Khalid bending over the bed, gently drawing a white blanket up over Yamna with a loving, exhausted face; Yamna {BED}, eyes closed, asleep and peaceful; Faarish in the background turning towards the door, his hand reaching for the handle",
         camera=f"medium shot, eye level, {LOW} (blanket in shadow)",
         amb="room_night"),
    dict(to=62, reason="Saahidha rushes in and hugs Yamna, weeping", reuse="beat_009", chars=["saahidha", "yamna"],
         loc="yamna_room", visual="reuse of beat_009", amb="room_night"),
    dict(to=64, reason="action change: Yamna opens her eyes and looks from face to face, expressionless",
         chars=["yamna", "saahidha", "khalid", "faarish"], loc="yamna_room",
         visual="a quiet family scene in the dim bedroom: Yamna resting against the pillows with the white blanket up to her chest, her white hijab fully covering her hair and neck, eyes open, her face calm and completely expressionless, slowly looking up at the people around her; her mother Saahidha sits on the edge of the bed holding her hand with a hopeful, tear-stained face; Khalid and Faarish stand beside the bed looking down at her with worried love; a soft warm bedside lamp",
         camera=f"medium shot from beside the headboard, eye level, {LOW} (blanket in shadow)",
         amb="room_night"),
    dict(to=65, reason="emotional turning point: her gaze stops on Ghassan and a wide, unsettling smile spreads across her face",
         chars=["yamna", "ghassan"], loc="yamna_room",
         visual="close-up of Yamna's face on the pillow, white hijab fully covering her hair and neck, pale with dark circles, no marks: her eyes fixed coldly on someone just off-frame while a slow, wide, calm smile spreads across her lips — an eerie, knowing, unsettling smile; at the blurred edge of the foreground the white-shirted shoulder of Ghassan, seen from behind",
         camera=f"close-up over Ghassan's shoulder, eye level, {LOW} (blanket in shadow)",
         amb="haunted_room", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "In that rush she went into the kitchen, and Yamna yanked open the freezer compartment of the fridge. At that very second, the big uncut sea fish lying inside,",
   [("door_open", "ހުޅުވާލިއެވެ", -18)])
sh(2, "she took out just as it was, sank her teeth into it, tore at it and began to eat. Seeing that terrifying sight, everyone ran and tried to hold Yamna. But",
   [("cloth_rustle", "ހިފަހައްޓަން", -20)])
sh(3, "the strength in that body was not the strength of an ordinary human. The strong, big men trying to hold her, she flung off with a twist of her body without any difficulty.",
   [("crash_clatter", "ވިއްސާލައިލީ", -20)])
sh(4, "How could an ordinary human bite through and eat a raw fish frozen as hard as a block of iron? Yet,")
sh(5, "because of the evil spiritual power that had mounted that body, as if eating a crunchy chilli biscuit,")
sh(6, "it took Yamna no time at all to eat that big fish with crunching sounds. Everyone watching felt their skin crawl, and their bodies kept trembling with fear.",
   [("heartbeat", "ރޫރޫ", -22)], hum=True)
sh(7, "When she had eaten the whole big fish, Yamna's eyes rolled upward, and foam tinged with the colour of blood came from her mouth,",
   [("gasp", "ފުރޮޅި", -20)])
sh(8, "and she sank to the floor like a limp rag doll. While the whole house was in shock, at that very moment Yamna's elder brother Faarish arrived from Malé and came into the house.",
   [("soft_thud", "ދެމުނެވެ", -20), ("door_open", "ވަނީ", -20)])
sh(9, "With the terrifying sight before him, and on hearing about the extraordinary thing that had just happened, Faarish's face showed the most extreme distress.")
sh(10, "\"Father! Let's take little sister to the hospital right now without delay. Eating such a big raw fish could even cause food poisoning that endangers her life!\"")
sh(11, "Faarish, alarmed, rushed to save his little sister. Before the ambulance came, Yamna threw up everything in her stomach. Taken to the hospital,",
   [("siren", "އެމްބިއުލޭންސް", -20)])
sh(12, "admitted, and given the necessary first aid, she was released home; what could be seen in Yamna then was an unusual calmness.")
sh(13, "She seemed like a doll with no life in its body. That day's sun set mercilessly, as though declaring a great war on that poor family.")
sh(14, "The air grew heavy, and in every direction one looked there was only deep dread, unease and fear. However,",
   [("wind_gust", "ޖައްވު", -22)])
sh(15, "after that terrifying incident at noon, Yamna was completely calm and quiet. No resistance, no anger could be seen in her at all.")
sh(16, "So Saahidha gently bathed her innocent daughter, made her pretty, and fed her too.",
   [("pour", "ފެންވަރުވައި", -22)])
sh(17, "In the terrifying 24 hours that had passed, that was the only short moment when Yamna's soul found a little relief and the family found some peace.")
sh(18, "After finishing the isha prayer, Yamna's family got ready for the dreadful midnight hour at which Raqi Ghassan had advised he would recite.")
sh(19, "As Ghassan had asked, besides Khalid and Faarish, Adheel too summoned his courage and got ready to go into Yamna's room for the recitation.")
sh(20, "Entrusting her to Almighty Allah and praying in her heart, Saahidha hugged her daughter, dear to her as her own life, tightly. Then,",
   [("cloth_rustle", "ބައްދާލިއެވެ", -22)])
sh(21, "before the recitation began, weeping and weeping, she left the room against her heart's will. Just as she came out of Yamna's room,",
   [("sob_breath", "ރޮމުން", -22)])
sh(22, "with a heavy heart Saahidha shut the door of that room. And leaning her back against the door from outside,",
   [("door_close", "ލައްޕާލިއެވެ", -18)])
sh(23, "she slowly slid down and sat on the floor with her knees drawn up. Her heart kept telling her that not even an inch,",
   [("cloth_rustle", "އިށީނދެއްޖެއެވެ", -24)])
sh(24, "not even for a second, did she want to go away from her daughter, the light of her eyes. Her whole body was alert to whatever sound would come from the other side of the door.",
   hum=True)
sh(25, "After the lights of the room were dimmed, Ghassan came and sat down by Yamna's head. The silence in the room was broken by Ghassan, moving his lips,",
   [("bulb_flicker", "ފަނޑުކޮށްލުމަށްފަހު", -22)])
sh(26, "with a murmuring sound. What he was reciting, what he was saying, the men in the room could not make out at all.",
   [("whisper_recite", "ބުންބުން", -23)])
sh(27, "They seemed like dreadful commands called out from within his breath. With the dull sound of Ghassan's muttering, Saahidha, sitting on the other side of the door, felt as if her heart had stopped.")
sh(28, "What could be heard next from inside the room was Yamna's pained moan. But suddenly, from the innocent girl's throat, the same terrifying",
   [("breath_heavy", "އާހުގެ", -22)])
sh(29, "heavy voice as the night before screamed out, and Saahidha's whole body began to shake. She pressed both hands hard over her ears, unable to bear those dreadful sounds.",
   [("low_growl", "ހަޅޭއްލަވައިގަތް", -20)], hum=True)
sh(30, "From inside the room came the sounds of things breaking, and the chaotic sounds of Khalid and Faarish trying to hold Yamna.",
   [("crash_clatter", "ތަޅައިގެންދާ", -20)])
sh(31, "Ghassan's heavy voice grew stronger, the temperature in the room suddenly dropped, and a coldness like a block of ice began to be felt even outside the door.",
   [("wind_gust", "ފިނިކަމެއް", -24)])
sh(32, "As tears flowed endlessly from Saahidha's eyes, she sat with the back of her head resting against the door, chin raised, silently pleading to Allah in her heart.",
   [("sob_breath", "ކަރުނަތައް", -24)], hum=True)
sh(33, "Every pain that came to the daughter she loved more than her own life was something that crushed her own chest directly. Breathless,",
   [("heartbeat", "ނޭވާ", -22)])
sh(34, "though she was growing faint, determined to stay as close as possible to her daughter, Saahidha sat at that door without moving at all,")
sh(35, "and listened to the horrible, dreadful sounds coming from the other side of the door. Ghassan's muttering grew faster,",
   [("whisper_recite", "ތުންތަޅުވުން", -23)])
sh(36, "and the terrifying voice coming from his throat filled the whole room. At the same moment, the body of Yamna, bound tightly to the bed, was seized by a sudden convulsion and her eyes rolled upward.",
   [("bulb_flicker", "ގަދަވެގަތެވެ", -20)], hum=True)
sh(37, "Her veins bulged and the nails of her hands and feet curled. And once again what came out of her throat was not a human voice.")
sh(38, "It was a heavy, dreadful, breath-stopping voice that seemed to shake the whole room. Ghassan fixed his gaze on Yamna and began to question her in a commanding way.")
sh(39, "\"Speak! Who are you? Who sent you here?\" Through Yamna's tongue the terrifying spirit screamed.")
sh(40, "And after an evil laugh it began to speak: \"I don't have to answer every question of a wretch like you!\"",
   [("low_growl", "ހީނގަތުމެއްގެ", -20)])
sh(41, "The spirit showed its displeasure by glaring wide-eyed at Ghassan. \"Shall I show you what happens when you don't answer my question?!\"")
sh(42, "Ghassan's reply was no less harsh. In his eyes was a dreadful anger. His lips moving fast,")
sh(43, "he seemed to be sending out powerful words in a commanding way. At that same moment, a chest-crushing, terrifying scream came from Yamna's throat.",
   [("bulb_flicker", "ހަޅޭކެއްގެ", -20)])
sh(44, "Her body rose up off the bed. \"Don't hurt me! Don't hurt me!\"",
   [("wind_gust", "ހިއްލިގެންދިޔައެވެ", -20)], hum=True)
sh(45, "This time the jinn's voice had lost its earlier power; it came as if filled with pain, weeping and wailing and pleading.",
   [("sob_breath", "ރޮމުން", -24)])
sh(46, "That voice made the heart of Saahidha, sitting outside the room, tremble too. \"Tell me right now! Or else, this very night I will wipe even your scent from this world!\"",
   [("heartbeat", "ތެޅިގަތެވެ", -20)])
sh(47, "Ghassan gave a warning stronger than before. The verbal attacks between Ghassan and the jinn dragged on in the room. Hard to listen to,")
sh(48, "foul words it spoke, and that wicked creature mocked Ghassan and quarrelled with him. It showed a dreadful power that seemed to shake the doors and windows of the room.",
   [("low_growl", "ފުރައްސާރަކޮށް", -21), ("creak", "ތެޅޭ", -20)])
sh(49, "But when at last it knew it could not win against Ghassan's spells either, it laid down its weapons with a pained moan.",
   [("breath_heavy", "އާހަކާއެކު", -22)])
sh(50, "Panting and biting its tongue, the spirit said: \"This is... this island's Aadhanbe! This is the work of that old man Aadhanbe!",
   [("breath_heavy", "ނޭވާ", -22)])
sh(51, "He sent me, and that is why I entered this body!\" At the sentences heard in that dreadful voice, Khalid, Faarish and Adheel, in the room, looked at one another.")
sh(52, "But what showed on their faces was not belief. Instead, deep disgust and displeasure took over. In the previous night's recitation too,")
sh(53, "the jinn that had mounted Yamna's body had told a big lie. Since it had made such a big accusation before,")
sh(54, "this time there was not a single person there who would believe what it said. \"That's all lies! You're a big liar!\"")
sh(55, "Faarish said with displeasure, gritting his teeth. On the other side of the door, Saahidha, sitting on the floor with her knees drawn up, heard those sounds and thought exactly the same in her heart.")
sh(56, "That dreadful spirit was trying to plant doubt and suspicion in the family's hearts and lay the blame on an innocent old man of the island.")
sh(57, "When they did not believe it, the jinn grew even angrier, and Yamna's body began to thrash with a force as if it would lift off the bed.",
   [("bulb_flicker", "ތެޅިފޮޅެން", -22)])
sh(58, "The dread in the room grew minute by minute. But under Ghassan's dangerous power the jinn was restrained and subdued with a further warning.")
sh(59, "\"From now on, for every harm you do to this girl's body, I will cut off one of your limbs,\" Ghassan said, addressing the jinn,")
sh(60, "and began muttering again. This time, making strange sounds and shuddering, Yamna fainted.",
   [("whisper_recite", "ތަޅުވަންފެށިއެވެ", -23), ("breath", "ހޭނެތިއްޖެއެވެ", -22)])
sh(61, "By then the unnatural cold that had filled the room also began slowly to fade. Khalid lovingly laid a blanket over Yamna and asked Faarish to open the door of the room.",
   [("cloth_rustle", "ރަޖާގަނޑު", -22)])
sh(62, "As soon as the door opened, Saahidha, who could wait no longer, hurried into the room, wrapped her arms around Yamna and began to cry.",
   [("door_open", "ހުޅުވާލުމާއެކު", -18), ("sob_breath", "ރޯންފަށައިފިއެވެ", -22)])
sh(63, "Yamna seemed to have felt her mother's touch. She slowly opened her eyes and began to look at the faces of the people around her, one at a time.")
sh(64, "But her face showed no feeling at all. At last her gaze came to rest on Ghassan.")
sh(65, "And with that, a wide smile spread across her face. (To be continued)", hum=True)
SHOTS = S

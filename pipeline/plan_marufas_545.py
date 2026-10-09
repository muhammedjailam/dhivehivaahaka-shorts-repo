"""Beat/shot plan for Marufas episode 545 (used by plan_beats.py)."""

KITCHEN = ("a large modern kitchen in the family's big island house: carved dark-wood cabinets, a long countertop with a "
           "coffee machine and a blender, a big double-door steel fridge, a sink, red clay and steel bowls")
ABANDONED = ("a long-abandoned coral-stone house in a lonely overgrown corner of the island: broken wooden shutters, "
             "peeling walls, dust, cobwebs, a dark back room with a single old wooden chair; reached through scrub")
HOSPITAL = ("the island hospital: ICU corridor with a large glass window into Yamna's room (monitors showing abstract "
            "green lines, NO numbers), plastic chairs along the corridor")
WARD = ("the island hospital: Yamna's hospital room, a single hospital bed with white sheets and a white pillow, "
        "monitors showing abstract green lines with NO numbers, a plastic chair beside the bed, a window with blinds, "
        "pale walls")
LANE = ("white sandy lanes between coral-stone walls, palms and breadfruit trees, a few dim street lamps, overgrown "
        "scrub at the edge of the island")

LOC = {
    "kitchen_memory": KITCHEN,
    "kitchen": KITCHEN,
    "dark_room": ABANDONED + "; inside the dark back room",
    "abandoned_ext": ABANDONED + "; the outside of the house and its weathered front door",
    "abandoned_dusk": ABANDONED + "; the overgrown path through the scrub leading to the house",
    "dark_room_dusk": ABANDONED + "; inside the dark back room",
    "hospital": HOSPITAL,
    "icu_glass": HOSPITAL + "; the view through the glass into the ICU room",
    "hospital_afternoon": HOSPITAL,
    "ward": WARD,
    "ward_night": WARD,
    "search": LANE,
    "police_ext": ABANDONED + "; the outside of the house",
    "police_door": ABANDONED + "; the dim inner passage outside the closed back room",
    "police_room": ABANDONED + "; inside the dark back room",
}
MOOD = {
    "kitchen_memory": "a remembered flash, soft dreamlike haze, cold blue-white light spilling from the open fridge in a dim kitchen, deep charcoal shadows, eerie and sickening",
    "kitchen": "midday, flat harsh daylight through the kitchen window, cold grey-white tones, a heavy silent aftermath",
    "dark_room": "daytime outside but near-darkness inside: thin dusty blades of daylight through the broken shutters, deep charcoal shadows, suffocating dread",
    "abandoned_ext": "gloomy overcast midday, washed-out grey light, the scrub still and silent, ominous",
    "abandoned_dusk": "late afternoon turning to dusk, a low bruised orange sky behind the palms, long dark shadows, urgent and ominous",
    "dark_room_dusk": "dusk: almost total darkness, a faint cold blue glow through the broken shutters, deep black shadows, menace",
    "hospital": "midday, cold white fluorescent light, pale green-grey tones, sterile and tense",
    "icu_glass": "cold fluorescent light, the soft green glow of the monitors reflected on the glass, tense and fragile",
    "hospital_afternoon": "afternoon, warm soft golden light from a corridor window mixing with cool fluorescent light, fragile relief",
    "ward": "afternoon, soft muted daylight through the blinds, pale blue-grey tones, quiet and sorrowful",
    "ward_night": "night, a single dim warm lamp by the bed, the faint green glow of a monitor, deep blue shadows, heavy silence",
    "search": "dusk turning to night, a deep blue sky, the warm moving beams of hand torches, mist among the palms, anxious",
    "police_ext": "dusk, a deep blue-grey sky, white police flashlight beams sweeping the peeling walls, mist, grim",
    "police_door": "dusk, near-darkness, harsh white flashlight beams cutting through dust, grim shock",
    "police_room": "near-darkness, a single harsh white flashlight beam cutting through floating dust, cold blue shadows, desolate",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
GOWN = ("wearing a modest long-sleeved pale-blue hospital gown instead of her lilac dress, her white hijab fully covering "
        "her hair and neck, a white blanket up to her chest")
HAG = "pale, tired, with dark circles under her eyes and hollow cheeks, no marks on her face"

BEATS = [
    # ---------------- MEMORY FLASH + ABANDONED HOUSE (midday)
    dict(to=2, reason="memory flash: Faarish remembers Yamna in the kitchen that morning", loc="kitchen_memory",
         visual="the wrecked kitchen remembered in a hazy flash: the big double-door fridge hanging open and spilling cold light, scattered vegetables and fruit on the floor, open cabinets; ONE single petite girl in a pale-lilac long-sleeved ankle-length dress and a white hijab seen only from BEHIND, a small distant figure hunched at the open cabinet under the sink, her hands hidden in front of her, her face never shown; one continuous scene, no inset portrait, no floating face, no second figure",
         camera=f"wide shot from the kitchen doorway, eye level, the girl small in the middle distance, {LOW} (the marble floor in shadow)",
         amb="memory", transition="dissolve", sens="other",
         safe="Yamna eating raw guts from the bin is never shown: only the wrecked kitchen and her small figure from behind, hands hidden (bible rule 4)"),
    dict(to=3, reason="back to the present in the abandoned house: Faarish's face burns with hatred", chars=["faarish"], loc="dark_room",
         visual="close-up of Faarish in the dark back room, his face half in deep shadow and half caught by a thin dusty blade of daylight through a broken shutter, teeth gritted, jaw clenched, eyes burning with hatred; the room behind him dark and empty",
         camera=f"close-up, slightly low angle, {LOW} (darkness)", amb="abandoned_house", transition="dissolve", hum=True,
         sens="violence", safe="only Faarish's furious face in shadow; the old man and any harm are not shown (bible rule 3)"),
    dict(to=5, reason="scene change: he strides home and stands in the wrecked kitchen", chars=["faarish"], loc="kitchen",
         visual="Faarish standing alone in the wrecked kitchen, looking down at the floor near the sink with a cold, hard expression, jaw set, fists clenched; around him the aftermath: the double-door fridge hanging open, scattered vegetables and fruit, a fallen blender, open cabinets, steel and red clay bowls on the floor; nothing in his hands",
         camera=f"medium shot, eye level, {LOW} (marble floor with scattered vegetables in soft shadow)", amb="home_day",
         sens="other", safe="what he gathers from the floor is never shown; only his cold face in the wrecked kitchen"),
    dict(to=6, reason="scene change: he returns to the abandoned house (closed weathered door)", loc="abandoned_ext",
         visual="the weathered closed wooden front door of the abandoned coral-stone house: cracked grey planks, a rusted latch, peeling lime-washed walls, broken shutters beside it, overgrown scrub and dry leaves at the threshold; no people",
         camera="medium shot, eye level, the door in the upper two-thirds, the dusty threshold and dry leaves as the calm lower third",
         amb="abandoned_house", sens="violence",
         safe="what he throws before the old man is never shown; only the closed door from outside (bible rule 3)"),
    dict(to=8, reason="back to Faarish shouting at the old man (same face in shadow)", reuse="beat_002", chars=["faarish"], loc="dark_room",
         visual="reuse of beat_002", amb="abandoned_house", sens="violence", safe="only Faarish's face in shadow"),
    dict(to=11, reason="focus change: the terrified old man alone on the chair", chars=["aadhanbe"], loc="dark_room",
         visual="Aadhanbe sitting alone on an old wooden chair in the middle of the dark empty back room, hands resting in his lap, his head turned aside and his eyes squeezed shut in fear and despair, frail and trembling but clean and unhurt, his white shirt and cap clean; thin dusty shafts of light through the broken shutters, peeling walls, cobwebs; nobody else in the room",
         camera=f"medium wide shot, eye level, from a distance, {LOW} (dusty floor in shadow)", amb="abandoned_house", hum=True,
         sens="violence",
         safe="the forcing of filth, his vomiting and his injuries are never shown; only the old man alone on the chair, frightened, clean and unhurt (bible rule 3)"),
    dict(to=12, reason="they slam the door and leave (return to the closed door)", reuse="beat_004", loc="abandoned_ext",
         visual="reuse of beat_004", amb="abandoned_house"),
    # ---------------- HOSPITAL (midday)
    dict(to=14, reason="scene change: Faarish and Adheel walk into the hospital, freshly showered but shaken", chars=["faarish", "adheel"], loc="hospital",
         visual="Faarish and Adheel walking quickly side by side down the hospital corridor towards the camera, their hair still damp, clean clothes, tense pale faces, Faarish suddenly slowing, staring ahead at something with dread; plastic chairs along the wall",
         camera=f"medium wide shot, eye level, down the corridor, {LOW} (polished corridor floor)", amb="hospital_corridor", transition="dissolve"),
    dict(to=15, reason="character change: Saahidha crying on a chair, Khalid pacing", chars=["saahidha", "khalid"], loc="hospital",
         visual="in the ICU corridor Saahidha sits bent forward on a plastic chair, head bowed, her face in her hands, weeping; a few steps away Khalid paces, one hand pressed to his forehead, his face drawn with anxiety",
         camera=f"medium wide shot, eye level, {LOW} (corridor floor)", amb="hospital_corridor"),
    dict(to=19, reason="new view: Yamna fighting for her life, seen through the ICU glass", loc="icu_glass",
         visual="view through the large glass window into a quiet intensive-care room, the empty corridor side in the foreground with NOBODY standing at the window: beyond the glass a young girl rests asleep in a hospital bed, small in the frame, in a modest long-sleeved pale-blue hospital gown and a white hijab fully covering her hair and neck, a white blanket up to her chest, her face calm and pale; several monitors and medical machines beside the bed showing abstract green wave lines, no numbers; soft reflections on the glass",
         camera=f"medium shot through the glass, eye level, the bed and monitors in the upper two-thirds, the window ledge in shadow as the calm lower third",
         amb="icu_room", hum=True, sens="other",
         safe="no ventilator tube, no needles, no blood; only an oxygen nasal line and abstract monitors seen through the glass (bible rule 10)"),
    dict(to=21, reason="action change: doctors and nurses work urgently around her bed", loc="icu_glass",
         visual="through the ICU glass: two doctors in green scrubs and a nurse in scrubs and a white hijab fully covering her hair working urgently around the hospital bed, one adjusting a monitor with abstract green lines, the patient almost completely hidden behind them, only the white blanket visible",
         camera=f"medium shot through the glass, eye level, {LOW} (window ledge in shadow)", amb="icu_room",
         sens="other", safe="medical work shown without needles, tubes or blood; the patient hidden by the staff"),
    dict(to=22, reason="focus change: Faarish breaks down in tears at the glass", chars=["faarish"], loc="icu_glass",
         visual="close-up of Faarish standing at the ICU glass window, one palm flat on the glass, tears running down his face, his lips pressed together, the green glow of the monitors reflected on the glass in front of him",
         camera=f"close-up, eye level, slightly from the side, {LOW}", amb="hospital_corridor", hum=True),
    dict(to=27, reason="time change: afternoon, the monitors steady and the doctor brings hope", chars=["khalid", "saahidha"], loc="hospital_afternoon",
         visual="afternoon in the ICU corridor: Khalid and Saahidha standing side by side facing a female Maldivian doctor in green scrubs and a white hijab fully covering her hair who speaks gently; tears of relief in their eyes, Saahidha's hands pressed together at her chest, Khalid's hand on her shoulder; behind them through the glass the monitors glow with calm, even green lines",
         camera=f"medium shot, eye level, {LOW} (corridor floor)", amb="hospital_day", transition="black"),
    dict(to=29, reason="emotional turning point: Yamna opens her eyes, silent and empty", chars=["yamna"], loc="ward",
         visual=f"Yamna awake in the hospital bed in soft afternoon light, propped on a white pillow, {GOWN}; her eyes open with a quiet, distant, faraway look, pale and tired with soft shadows under her eyes, lips closed, silent",
         camera=f"medium close-up, eye level, {LOW} (the white blanket in soft shadow)", amb="hospital_room"),
    dict(to=32, reason="action change: Saahidha holds her hand and calls her; Yamna cannot speak, a single tear", chars=["yamna", "saahidha"], loc="ward",
         visual=f"Saahidha sitting on the chair at the bedside, leaning close and holding Yamna's hand in both of hers, calling to her with pleading eyes; Yamna lies in the bed, {GOWN}, {HAG}, her lips slightly parted as if trying to speak but silent, a single tear running down her cheek",
         camera=f"medium close two-shot, eye level, {LOW} (the white blanket in soft shadow)", amb="hospital_room", hum=True),
    dict(to=35, reason="character change: Faarish and Adheel open the door and see her", chars=["faarish", "adheel"], loc="ward",
         visual="seen from inside the hospital room: Faarish standing in the open doorway, one hand gripping the door frame, his face stricken with shock and grief as he looks towards the bed; Adheel just behind his shoulder in the corridor, his face pale",
         camera=f"medium shot, eye level, {LOW} (the room floor in soft shadow)", amb="hospital_room",
         sens="other", safe="Yamna's wasted state shown only through her brother's face"),
    dict(to=37, reason="back to Yamna's wasted, silent face", reuse="beat_014", chars=["yamna"], loc="ward",
         visual="reuse of beat_014", amb="hospital_room", sens="other",
         safe="the narration's scars are never shown: she is only pale, tired and hollow-cheeked (bible rule 1)"),
    dict(to=41, reason="emotional turning point: she looks at Faarish with tear-filled eyes, trying to speak", chars=["yamna", "faarish"], loc="ward",
         visual=f"Yamna lying in the hospital bed, {GOWN}, {HAG}, her eyes full of tears turned up towards her brother, lips parted, desperately trying to say something; Faarish standing beside the bed looking down at her, his face torn between grief and rising fury",
         camera=f"medium close shot over the bed, eye level, both faces in the upper two-thirds, {LOW} (the white blanket)",
         amb="hospital_room", hum=True),
    dict(to=44, reason="action change: Faarish, shaking with rage, walks out; Adheel follows", chars=["faarish", "adheel"], loc="hospital",
         visual="Faarish striding out of the hospital room into the corridor, his face hardened with fury, eyes burning, jaw clenched, fists tight, his whole body tense and trembling; Adheel following a step behind him with a worried look, asking nothing",
         camera=f"medium shot, eye level, {LOW} (corridor floor)", amb="hospital_corridor"),
    # ---------------- ABANDONED HOUSE (dusk)
    dict(to=45, reason="scene change: the two young men hurry back through the scrub to the abandoned house", chars=["faarish", "adheel"], loc="abandoned_dusk",
         visual="two young men seen from behind, Faarish in a black long-sleeved tee and jeans and Adheel in an olive-green shirt, walking fast almost running along the narrow overgrown path through the scrub towards the dark silhouette of the abandoned coral-stone house, palms against the dusk sky; their faces not shown",
         camera="wide shot from behind, eye level, the figures and the house in the upper two-thirds, the dark sandy path as the calm lower third",
         amb="island_night", transition="dissolve"),
    dict(to=48, reason="scene change: in the dark room Faarish confronts the exhausted old man (at a distance)", chars=["faarish", "aadhanbe"], loc="dark_room_dusk",
         visual="seen from behind Faarish: his dark silhouette standing in the open doorway in the foreground, filling the left side of the frame; far across the dark back room Aadhanbe sits slumped on the old wooden chair, weak and exhausted, eyes half closed, hands in his lap, clean and unhurt, in a faint cold beam of dusk light; a wide empty space of dark floor between them",
         camera=f"wide shot from behind Faarish's shoulder, eye level, {LOW} (dark empty floor)", amb="abandoned_house",
         sens="violence",
         safe="no grabbing, no injuries, no binding: the old man sits alone across the room, clean, and Faarish stays at the doorway (bible rule 3)"),
    dict(to=52, reason="emotional turning point: the unspeakable act, shown only as Faarish's face in shadow", chars=["faarish"], loc="dark_room_dusk",
         visual="extreme close-up of Faarish's face almost entirely swallowed by darkness, only one eye, the bridge of his nose and the edge of his cheek caught by a thin cold blue beam of light, his expression icy, empty and merciless; nothing else visible",
         camera="extreme close-up, eye level, the face in the upper two-thirds, pure darkness as the calm lower third",
         amb="abandoned_house", hum=True, sens="violence",
         safe="the tongue cutting, the knife, the scream and blood are never shown; only Faarish's cold face in shadow, a muffled offscreen thud (bible rule 3)"),
    dict(to=53, reason="they walk away from the house without looking back (return to the path image)", reuse="beat_020",
         chars=["faarish", "adheel"], loc="abandoned_dusk", visual="reuse of beat_020", amb="island_night"),
    # ---------------- TWO DAYS LATER
    dict(to=55, reason="time jump: two days later the islanders search with torches", loc="search",
         visual="islanders searching at dusk: several Maldivian men in shirts and sarongs and two women in long dresses with hijabs fully covering their hair, carrying hand torches, spreading out through overgrown scrub and coconut palms at the edge of the village, calling out, worried faces lit by the torch beams",
         camera="wide shot, eye level, the people and torch beams in the upper two-thirds, the dark sandy ground as the calm lower third",
         amb="island_night", transition="black"),
    dict(to=56, reason="scene change: police arrive at the lonely abandoned house with flashlights", loc="police_ext",
         visual="the abandoned coral-stone house at dusk seen from the scrub: three Maldivian police officers in dark-navy uniforms and caps, no weapons, no badges, approaching the weathered front door, their white flashlight beams sweeping across the peeling walls and broken shutters",
         camera="wide shot, eye level, the house and beams in the upper two-thirds, the dark overgrown ground as the calm lower third",
         amb="night_exterior", sens="other", safe="police shown only with flashlights outside the house (bible rules 3 and 11)"),
    dict(to=57, reason="action change: officers open the room door and recoil (inside not shown)", loc="police_door",
         visual="in the dim inner passage of the abandoned house two Maldivian police officers in plain dark-navy uniforms and plain caps (no patches, no emblems, no badges, a plain belt with no holster and no pouches, nothing on the belt) stand at an open doorway, seen from the side, recoiling a step back with grim, shocked faces, one covering his nose and mouth with his hand, their flashlight beams pointing into the darkness of the room beyond; the inside of the room is not visible",
         camera=f"medium shot from the side in the passage, eye level, {LOW} (dusty floor)", amb="abandoned_house",
         sens="violence", safe="the discovery is shown only through the officers' grim faces at the doorway; the room is not shown (bible rule 3)"),
    dict(to=60, reason="symbolic detail: the empty dark room with the overturned old chair", loc="police_room",
         visual="the empty dark back room: an old wooden chair lying overturned on its side on the dusty floor, a single police flashlight beam cutting through the darkness and falling on it, dust floating in the beam, peeling walls and cobwebs; no people",
         camera="medium wide shot, slightly high angle, the chair and beam in the upper two-thirds, dark floor as the calm lower third",
         amb="abandoned_house", hum=True, sens="violence",
         safe="the body, blood and tongue are never shown; only an empty overturned chair in the flashlight beam (bible rule 3, spec 6.1)"),
    dict(to=61, reason="the police seal off the area (return to the house exterior)", reuse="beat_025", loc="police_ext",
         visual="reuse of beat_025", amb="night_exterior"),
    # ---------------- FINAL: HOSPITAL ROOM
    dict(to=64, reason="scene change and final image: Faarish sits silently by his mute sister's bed", chars=["faarish", "yamna"], loc="ward_night",
         visual=f"Faarish sitting motionless on a plastic chair beside the hospital bed at night, elbows on his knees, his face completely expressionless, quietly watching his sister; Yamna lies in the bed, {GOWN}, {HAG}, eyes open and silent, staring at the ceiling; a single dim lamp, the faint green glow of a monitor",
         camera=f"medium wide shot, eye level, from the foot-side corner of the room, {LOW} (dark floor)", amb="hospital_night",
         transition="dissolve", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "As the words \"something to eat\" left Aadhanbe's tongue, what suddenly appeared in Faarish's mind was his beloved little sister Yamna in the kitchen,")
sh(2, "taking the raw fish guts out of the dustbin and eating them, that terrifying scene. It was as if the fire of hatred born in his heart spread through his whole body.",
   [("heartbeat", "ނަފުރަތުގެ", -22)], hum=True)
sh(3, "\"Something to eat? Wait... today I'll give you something very tasty to eat,\" Faarish said angrily, grinding his teeth.",
   [("breath_heavy", "ދަތްކުނޑި", -22)])
sh(4, "Without any delay, with heavy strides, he left that abandoned house and headed straight for his own home. Entering the house,",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -20), ("door_open", "ވަދެ", -22)])
sh(5, "from the raw guts Yamna had tried to eat in the kitchen but could not, and had thrown on the floor, he took some and put them in a bag.",
   [("cloth_rustle", "ކޮތަޅަކަށް", -22)])
sh(6, "And with that same force he came back, went into the abandoned house, and flung the stuff down in front of Aadhanbe, who lay tied up.",
   [("creak", "ވަދެ", -20), ("soft_thud", "އުކާލިއެވެ", -22)])
sh(7, "The foul stench from the raw fish guts taken out of the bag, and the blood that could be seen, polluted the whole room. \"Eat it!")
sh(8, "This is what my little sister ate today because of you! Today you will have to eat some of this!\" Faarish shouted,")
sh(9, "taking the slimy stuff and trying to push it into Aadhanbe's mouth. But how could a human being in his right mind eat such filth?",
   hum=True)
sh(10, "Screaming in terror and disgust, Aadhanbe began to shake his head. Because the guts were rubbed over his mouth, his head spun and he began to retch.")
sh(11, "After standing a while watching the pitiful sight of Aadhanbe writhing on the lips of death, in the blood from the beatings of the day before and in his own sickness, Faarish and Adheel mercilessly left him in that abandoned house.")
sh(12, "And after slamming the door shut, they went out again. As Faarish and Adheel went in through the hospital door,",
   [("door_slam", "ބަންލާފައި", -18), ("footsteps_sand", "ހިނގައްޖެއެވެ", -22)])
sh(13, "an uneasy silence hung over the whole place. Though the two had showered and tidied themselves, their faces and hurried steps showed how hard their hearts were pounding.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކުން", -22)])
sh(14, "When the two reached the ICU corridor, the sight they saw from a distance made the ground seem to slip from under Faarish's feet.",
   [("heartbeat", "ބިންގަނޑު", -22)])
sh(15, "Saahidha sat on a chair, head bowed, crying hard. Khalid kept pacing anxiously from one end of the corridor to the other.",
   [("sob_breath", "ރޯށެވެ", -24), ("footsteps_pavement", "ހިނގާލަ", -24)])
sh(16, "Looking in through the glass of the room where Yamna lay, the sight was heartbreaking. Yamna was fighting a battle with death.",
   hum=True)
sh(17, "The sounds coming from the many machines connected to her body brought only anguish to everyone.",
   [("monitor_alarm", "މެޝިންތަކުން", -22)])
sh(18, "With the movements of the ventilator helping her breathe, her chest rose and fell in extreme pain. The heart monitor's waves grew faster,",
   [("breath", "ވެންޓިލޭޓަރުގެ", -24), ("monitor_alarm", "މޮނިޓަރުގެ", -20)])
sh(19, "and every time its sound suddenly changed, it was as if the souls of the parents waiting outside were leaving their bodies.",
   [("monitor_alarm", "ބަދަލުވެގެންދާ", -20)], hum=True)
sh(20, "Doctors and nurses moved anxiously around Yamna's bed, trying to hold the last breath in her body.",
   [("footsteps_pavement", "ހަރަކާތްތެރިވަމުން", -24)])
sh(21, "Learning that because of the food poisoning her organs were close to shutting down,")
sh(22, "tears began to pour from Faarish's eyes uncontrollably. As those painful moments passed, by the afternoon of that day,",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(23, "the whole family found some measure of relief. The sounds of the machines connected to Yamna's body softened,",
   [("sigh", "ހަމަޖެހުމެއް", -22)])
sh(24, "and the heart monitor's waves began to hold steady. According to the doctors, the effect of the poison was now fading from her body.")
sh(25, "They also noted that because Yamna's body had not received enough proper food and water in the past days, it had already been weak even before the poisoning.")
sh(26, "And so the doctors also noted that her body now had no strength left to face any harm, however small.")
sh(27, "But the plan of fate is perfect. As Yamna won her battle with death and life began to return to her body, tears of joy fell from Saahidha's and Khalid's eyes.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(28, "But that joy lasted only a short moment. As Yamna slowly opened her eyes, what began to show in her was not the old terrifying rage.",
   [("breath", "ހުޅުވާލުމާއެކު", -24)])
sh(29, "Instead, she was unnaturally silent. Her eyes held only an empty, lifeless gaze.")
sh(30, "Saahidha took Yamna's hand and called out to her child. But there was no answer from Yamna.")
sh(31, "She opened her mouth and tried to speak, but no sound came from her throat. Her tongue was completely locked;",
   [("breath", "ހުޅުވާލައި", -24)])
sh(32, "she had become mute. Out of that silence, a single tear slipped from Yamna's eye and ran down her cheek.",
   hum=True)
sh(33, "Faarish and Adheel walked along the hospital corridor and opened the door of the room where Yamna lay.",
   [("footsteps_pavement", "ފިޔަވަޅުތައް", -22), ("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(34, "Seeing Yamna lying on the bed like lifeless flesh, it was as if Faarish's chest had been split open. It felt as though the blood in his whole body had stopped flowing,",
   [("heartbeat", "މޭފަޅައިލި", -22)])
sh(35, "and he felt a deep pain his heart could hardly bear. In the merciless storm that had passed,")
sh(36, "seeing how withered and wasted his beloved little sister had become, Faarish's chest seemed to tighten. That girl's once soft,")
sh(37, "fair skin had today fallen prey to deep wounds and was covered in scars. Her eyes, robbed of sleep for nights, were dark-ringed and sunken.")
sh(38, "Yamna lay completely silent. There was no movement on her lips. But from eyes like a sea of despair, Yamna looked at Faarish with a gaze full of tears.",
   hum=True)
sh(39, "The painful complaints welling up from the depths of her heart, and the endless pleas of the many things she longed to say, were screaming inside her.")
sh(40, "Though the girl's tongue was locked, her heart was weeping and pleading. Yamna opened her mouth and began to move her lips anxiously.",
   [("sob_breath", "ރޮއި", -24)])
sh(41, "Looking at Faarish, she kept drawing breath as if to say something. But no sound, no word, came out of her throat.",
   [("breath", "ނޭވާލަމުން", -22)])
sh(42, "Her tongue was completely locked. Seeing the tears pour uncontrollably from Yamna's eyes in her anguish at not being able to speak, Faarish's heart filled with hatred and fury and grew hard.",
   hum=True)
sh(43, "It came to his mind that the root of the anguish that had befallen his beloved sister was that wretched Aadhanbe. Faarish's eyes turned red with rage,")
sh(44, "and his whole body began to tremble. As he set off out of the room, Adheel too, without a single question, walked out after him.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(45, "The two young men, almost running, went back into that abandoned house and opened the door of the room where Aadhanbe lay.",
   [("footsteps_sand", "ދުވެފައި", -20), ("creak", "ހުޅުވާލިއެވެ", -18)])
sh(46, "Aadhanbe lay barely conscious in his own sickness and blood. Faarish went over, grabbed Aadhanbe by the hair and lifted his face.")
sh(47, "\"You are the one who made my little sister unable to speak! After today you too will never get the chance to say another word in this world!\"",
   hum=True)
sh(48, "Faarish shouted at the top of his voice. Aadhanbe, eyes wide with fear, opened his mouth to cry for help, but Faarish and Adheel gave him no chance.")
sh(49, "Adheel went and held Aadhanbe's head back and forced his mouth open. With a sharp blade Faarish took from his pocket,")
sh(50, "without any mercy he cut off Aadhanbe's tongue. The whole room rang with the dreadful cry of agony that escaped Aadhanbe's throat.",
   [("soft_thud", "ބުރިކޮށްލިއެވެ", -24)], hum=True)
sh(51, "As blood gushed from his mouth, his tongue fell to the floor.")
sh(52, "In return for the pain his sister had suffered, having silenced Aadhanbe's tongue forever, Faarish threw the blade to the ground.")
sh(53, "As Aadhanbe writhed in that chair, they walked out of that dark abandoned house without once looking back.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(54, "When two days passed with no news of Aadhanbe, his family and the islanders grew worried and began searching for him as a missing person.",
   [("leaves_rustle", "ހޯދުމުގެ", -22)])
sh(55, "As people spread out to search in every direction of the island, and once the case was reported, the police too joined the effort,",
   [("footsteps_sand", "ހޯދަމުން", -22)])
sh(56, "and began checking the island's empty plots and abandoned houses. A police team went into that frightening abandoned house in a lonely corner of the island,",
   [("flashlight_click", "ވަދެ", -18)])
sh(57, "looking inside by the light of their flashlights. The moment they opened the door of the room, the foul smell and the sight they saw shocked even the police, and they stepped back.",
   [("flashlight_click", "ބައްތީގެ", -18), ("creak", "ހުޅުވާލި", -18), ("gasp", "ސިހުން", -22)])
sh(58, "Aadhanbe, though tied to a chair in that pitch-dark room, had slumped down into it. In his own sickness,",
   hum=True)
sh(59, "the filth of the guts and a pool of dried black blood, he lay dead. His mouth lay wide open.")
sh(60, "With his severed tongue lying beside him, the agony of his death throes was plain to see in his bulging eyes and terrified face.",
   hum=True)
sh(61, "Without a chance to say another word, his life ended right there. As the police sealed off the area",
   [("siren", "ސަރަހައްދު", -24)])
sh(62, "and news of the investigation spread across the whole island, in the hospital room Faarish's face showed no expression at all.")
sh(63, "He simply sat watching the face of his beloved little sister Yamna, lying mute and silent on the bed.",
   hum=True)
sh(64, "Though he silenced forever the tongue of the man who silenced his sister's, and ended his world, the silent darkness that has fallen over their lives will never lift. (To be continued)",
   hum=True)
SHOTS = S

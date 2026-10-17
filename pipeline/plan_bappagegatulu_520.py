"""Beat/shot plan for Bappage Gatulu episode 520 — v2 re-cut on the new audio (used by plan_beats.py)."""

FB = "2011, stormy night, cold desaturated blue-grey haze"

LOC = {
    "male_storm": "the Malé city skyline in 2011 seen from the rough seawall at night, dense rows of narrow multi-storey concrete buildings, a few dim windows, heavy black storm clouds pressing low over the city, a dark churning sea breaking white against the concrete tetrapods of the seawall, an empty wet coastal road",
    "sitting_2011": "the modest sitting room of a small Malé house in 2011 at night, a cushioned fabric sofa, a low wooden side table with a small lamp, a plain round wall clock with a blank face and no numerals, a tall window with a thin curtain, rain streaming down the dark glass",
    "window_view": "the narrow rain-swept lane outside a small Malé house in 2011 at night, seen through the rain-streaked glass of the sitting-room window, a low painted boundary wall with a metal gate, a single tall street lamp, wet tarmac shining",
    "lane_2011": "a narrow residential lane in Malé in 2011 at night, low painted walls and closed gates on both sides, tall street lamps, heavy rain bouncing off wet tarmac, deep puddles, dark buildings",
    "doorway_2011": "the wide-open wooden front door of a small Malé house in 2011 at night, seen from inside the narrow entrance hall, rain blowing in across the tiled threshold, the wet lane and a street lamp beyond",
    "road_2011": "the wet tarmac of a narrow Malé lane in 2011 at night directly under a tall street lamp, rain falling in sheets, puddles reflecting only cold white and teal light, the low wall and gate of a small house at the edge of the frame",
    "road_after_2011": "the same narrow rain-soaked Malé lane in 2011 later that night, low walls, a black car with its rear door left open, the upper windows of neighbouring houses lit, a faint pulsing blue glow at the far end of the lane",
    "male_night": "a rain-wet street in Malé today at night between dark multi-storey buildings, red-lit shop fronts with blank signboards, glistening reflections on the pavement, parked motorbikes",
    "newsroom": "the large open-plan newsroom of a big newspaper in Malé today late at night, rows of empty desks with dark monitors, stacks of blank papers, tall windows onto the city lights, only one desk lamp lit",
    "hacker_room": "Iyaan's small locked bedroom in a modest Malé apartment today at night, a wide desk with three computer monitors and a keyboard, cables and small electronic devices, a closed laptop, a single narrow window with rain and distant city lights",
    "apartment": "the small modest sitting room of a Malé apartment today in the evening, a worn cushioned sofa, a low table with a glass of water and small medicine bottles with blank labels, a prayer mat folded on a chair, plain pale walls, a small window",
    "police_station": "the front steps and plain entrance of a police station building in Malé around 2015, grey concrete facade with no sign, glass doors, a few parked motorbikes, an overcast rainy afternoon",
    "board_room": "Iyaan's locked bedroom in a modest Malé apartment today late at night, one whole wall covered by a large cork investigation board filled with small faceless blurred photographs and blank index cards linked by taut red string, a wide desk with computer monitors below it",
}
MOOD = {
    "male_storm": f"{FB}, black clouds, faint lightning glow inside the clouds, spray over the seawall, ominous and silent",
    "sitting_2011": f"{FB}, a single warm amber lamp inside against the cold blue night at the window, anxious waiting",
    "window_view": f"{FB}, the white glare of car headlights and the cold street lamp diffused through rain on the glass, a moment of hope",
    "lane_2011": f"{FB}, darkness and slanting rain, cold street-lamp light, sudden menace",
    "doorway_2011": f"{FB}, cold blue light and rain pouring in through the open door, warm faint lamplight behind, panic",
    "road_2011": f"{FB}, a single cold white street lamp cone in the rain, deep shadows all around, stunned stillness, no red tones",
    "road_after_2011": f"{FB}, cold rain, warm lit windows above, a faint distant pulsing blue emergency glow, numb grief, no red tones",
    "male_night": "present day, night, sharp noir light, wet street reflecting red and teal neon, rain, determined and dangerous",
    "newsroom": "present day, late night, a single warm desk lamp and the cold blue glow of a laptop in a dark empty newsroom, focused and solitary",
    "hacker_room": "present day, night, cold blue and green monitor glow on his face, the rest of the room in deep teal shadow, secretive and intense",
    "apartment": "present day, evening, a dim warm table lamp, soft shadows, quiet, tender and sorrowful",
    "police_station": "a memory about four years after 2011, overcast grey afternoon, light drizzle, soft desaturated haze, disillusionment",
    "board_room": "present day, late night, a single desk lamp and the cold monitor glow throwing long shadows across the red string, obsessive and grim",
}

# v2 re-cut (new audio, 67 segments): v1 images reused via v1="beat_###"; NEW images only where spec 5.4 needs a
# centred, sharp speaker that no crop of a v1 image can give.
BEATS = [
    # ------------------------------------------------------------------ 2011 FLASHBACK
    dict(to=2, v1="beat_001", reason="episode opening: 2011, a stormy November night over Malé", loc="male_storm",
         visual="the Malé skyline under heavy black storm clouds, rough dark waves crashing white against the seawall tetrapods in the foreground, the coastal road empty and shining wet, no people, no vehicles",
         camera="wide establishing shot, the city and clouds in the upper two-thirds, the dark wet seawall road as a calm lower third",
         amb="storm_night"),
    dict(to=7, v1="beat_002", reason="scene and character change: young Iyaan waits at the sitting-room window for his father", chars=["iyaan_young"], loc="sitting_2011",
         visual="the small boy Iyaan kneeling on the sofa cushion by the tall window, both small hands resting on the sill, staring out into the dark rain with a hopeful, waiting expression, raindrops streaming down the glass in front of his face, his reflection faint in the pane",
         camera="medium shot from inside the room, slightly from the side, his face in the upper half, the sofa back and floor shadow as a calm lower third",
         amb="rain_night"),
    dict(to=9, v1="beat_003", reason="character change: focus moves to Aminath, worried on the sofa watching the clock", chars=["aminath_young"], loc="sitting_2011",
         visual="Aminath sitting at the edge of the sofa, her hands twisted together in her lap, glancing up anxiously at a plain round wall clock with a blank face and no numerals, her dark-green hijab fully covering her hair and neck, worry deep in her eyes, the lamp lighting one side of her face",
         camera="medium shot, eye level, the clock high in the frame on the wall behind her",
         amb="living_night"),
    dict(to=14, v1="beat_004", reason="action change: Aminath comes to Iyaan at the window and strokes his hair; he refuses to sleep (dialogue: crops alternate between the boy and his mother)", chars=["iyaan_young", "aminath_young"], loc="sitting_2011",
         visual="Aminath standing beside the window, bending to gently stroke the small boy's hair with a forced tender smile; Iyaan, kneeling on the sofa by the window, shaking his head stubbornly with pleading eyes, refusing to go to bed; rain running down the dark glass behind them",
         camera="medium two-shot, eye level", amb="rain_night",
         sens="intimacy", safe="mother and her own small son: a gentle hand on his hair, both fully clothed"),
    dict(to=16, v1="beat_005", reason="scene and action change: Zahir's black car stops at the gate; Zahir steps out with his briefcase", chars=["zahir"], loc="window_view",
         visual="seen through the rain-streaked window glass: a black sedan stopped at the gate of the house in the rain, its headlights on, Ahmed Zahir in his dark-navy suit jacket stepping out of the back seat holding a big black briefcase, turning to raise one hand and smile at the driver inside; water drops on the glass in the foreground",
         camera="medium wide, from inside the house looking out through the window, the car and Zahir in the upper half, the wet window sill as a calm lower third",
         amb="rain_night"),
    dict(to=19, v1="beat_006", reason="character and action change: the motorbike with two masked riders races in with its headlight off", loc="lane_2011",
         visual="far down the dark rain-swept lane, a motorbike with its headlight switched off speeding toward the camera through sheets of rain, two riders in black clothes and full black helmets seen only as dark faceless silhouettes against the glare of a car's headlights behind them, spray rising from the wheels; their hands are on the handlebars and at their sides, holding nothing",
         camera="wide shot, low angle from far away, the silhouettes small in the upper half, the wet tarmac as a calm lower third",
         amb="storm_night", sens="violence",
         safe="the attackers are only distant faceless helmeted silhouettes holding nothing; no object is drawn, the attack is never shown"),
    dict(to=22, v1="beat_007", reason="action change: Iyaan, face pressed to the glass, witnesses the attack (reaction shot only); his scream 'Bappa!' is a tight crop on his face", chars=["iyaan_young"], loc="sitting_2011",
         visual="extreme close-up of the small boy's face pressed against the rain-streaked window glass from inside, his two small palms flat on the pane, eyes wide with shock and terror, mouth open, his face lit by a harsh white headlight glare from outside, raindrops sliding down the glass over his reflection",
         camera="close-up, eye level, from just outside the glass looking in, face in the upper half",
         amb="rain_night", sens="violence",
         safe="only the boy's horrified face behind rainy glass; what he sees is never shown"),
    dict(to=23, v1="beat_008", reason="action change: Aminath runs to the door, Iyaan throws it open; the bike speeds away", chars=["iyaan_young", "aminath_young"], loc="doorway_2011",
         visual="seen from behind inside the entrance hall: the small boy rushing out through the wide-open front door into the pouring rain, his mother Aminath hurrying right behind him with one hand reaching out, her dark-green hijab fully covering her hair; far down the lane beyond the gate a single small red tail-light vanishing into the rain",
         camera="medium wide from behind them inside the house, the doorway framing the rainy lane in the upper two-thirds, the wet tiled floor as a calm lower third",
         amb="storm_night", transition="xfade"),
    dict(to=24, v1="beat_009", reason="action change: what Iyaan finds in the lane — the briefcase alone on the wet road", loc="road_2011",
         visual="a black leather briefcase lying alone on its side on the rain-soaked tarmac under the cone of a street lamp, rain hammering the road and splashing in the puddles around it, the puddles reflecting only cold white and teal light, nothing and no one else in the frame",
         camera="low close shot at road level, the briefcase and the lamp cone in the upper half, wet tarmac as a calm lower third",
         amb="storm_night", sens="violence",
         safe="the briefcase alone on the wet road stands in for the scene; no person on the ground, no red water"),
    # NEW (5.4): Iyaan calls 'Bappa! Open your eyes!' — the v1 image showed him only from behind
    dict(to=26, reason="5.4 speaker: Iyaan calls out to his father ('Bappa! Bappa! Open your eyes!') — the v1 image showed him only from behind, so a frontal chest-up framing of the boy is needed",
         speaker="iyaan_young", loc="road_2011",
         visual="close-up portrait of a small boy of about eight with short dark hair, in a soaked grey-blue long-sleeved shirt, kneeling in the pouring rain at night, framed from the chest up and centred, his face turned slightly downward and lit from above by a cold white street lamp, his mouth open as he calls out, his eyes wet with tears and rain, raindrops on his cheeks and hair; behind him only dark falling rain, a low garden wall and the soft blurred glow of an open doorway; everything below his chest is out of frame",
         camera="close-up from the front at the boy's eye level, his face sharp and centred in the upper half, his wet shirt and the soft dark blur as a calm lower third",
         amb="storm_night", sens="violence",
         safe="framed on the boy from the chest up, no reference image of the child; whatever he kneels beside is entirely out of frame; no red anywhere"),
    dict(to=27, v1="beat_011", reason="action change: Zahir's last effort to hold his son's hand (symbolic close-up)", loc="road_2011",
         visual="close-up of a grown man's hand in the sleeve of a dark-navy suit jacket and white shirt cuff loosely holding a small boy's hand, their fingers slowly slipping apart, both hands resting on wet rain-splashed paving tiles, raindrops falling, clean rainwater only, cold blue light",
         camera="extreme close-up at ground level, the two hands in the upper half, wet tiles as a calm lower third",
         amb="storm_night", sens="violence",
         safe="last efforts shown only as a father's hand loosening around his son's hand on wet tiles; no injury, no red, no face"),
    dict(to=29, reuse="beat_010", reason="Zahir's last words ('son… Mamma… look after…'): bible safe substitute — the boy's face in the rain, the listener centred; the father is never shown",
         loc="road_2011", visual="(reuse of the boy's face in the rain)", amb="storm_night", sens="violence",
         safe="the speaker (Zahir on the ground) is never shown; his last words play over the boy's face in the rain"),
    dict(to=31, v1="beat_012", reason="action change: the aftermath — Aminath kneeling in grief, the driver phoning, neighbours at their windows", chars=["aminath_young"], loc="road_after_2011",
         visual="Aminath seen from behind and at a distance, kneeling in the rain on the lane with her head bowed and her shoulders shaking, her dark-green hijab and maroon dress soaked; her own kneeling figure hides everything in front of her; to one side the driver, a man in a white shirt, stands by the black car with a phone to his ear, trembling; above, neighbours' lit windows with dark figures looking out; a faint blue glow far down the lane",
         camera="wide shot from behind her, slightly elevated, the windows and figures in the upper two-thirds, empty wet tarmac as a calm lower third",
         amb="rain_night", sens="violence",
         safe="death shown as the mother kneeling seen from behind, neighbours' windows and a distant emergency glow; nothing on the ground is visible"),
    dict(to=32, v1="beat_010", reason="action change: the boy alone in the rain, his crying suddenly stops (shock)", loc="road_2011",
         visual="seen from behind at a short distance: a small boy of about eight in a soaked grey-blue long-sleeved shirt and dark navy trousers, alone on the rain-soaked lane under the cone of a street lamp, his small shoulders hunched and his head bowed low, his back to the camera, heavy rain falling between him and the viewer, the glowing open front door of his house far behind on the left; the ground just in front of him is hidden in deep shadow and rain",
         camera="medium shot from behind him, slightly high angle, his bowed head and shoulders in the upper half, the wet lane as a calm lower third",
         amb="storm_night", sens="violence",
         safe="framed on the boy from the chest up; whatever he kneels beside is entirely out of frame; no red anywhere"),
    dict(to=33, v1="beat_013", reason="action change: the boy's tears dry from shock; he stares at his hands", loc="road_after_2011",
         visual="close-up of a small boy's two open hands held up palms-upward in front of him, trembling, wet only with clear rainwater, raindrops splashing on them, cold blue street light, the dark wet road blurred behind, no red on them at all",
         camera="close-up, the hands in the upper half, the blurred dark road as a calm lower third",
         amb="rain_night", sens="violence",
         safe="'his hands stained' shown as the boy's small open hands wet with clear rain, no red"),
    dict(to=38, v1="beat_014", reason="emotional turning point: the fire of revenge ignites; his vow; his heart turns to stone", chars=["iyaan_young"], loc="road_after_2011",
         visual="portrait of the small boy standing upright on the pavement in light rain at night, his head and shoulders clearly visible and centred, his face calm and serious, eyes dry and fixed straight ahead with quiet determination, a tiny warm amber glint of the street lamp reflected in his dark eyes, raindrops on his cheeks and hair, behind him the softly blurred lane with warm lit windows",
         camera="close-up, eye level, his face in the upper half, his soaked shirt and dark blur as a calm lower third",
         amb="memory_rain", sens="violence", safe="only the boy's resolute face in the rain"),
    # ------------------------------------------------------------------ PRESENT (fifteen years later)
    dict(to=41, v1="beat_015", reason="time jump out of the flashback: fifteen years later, Iyaan at 23", chars=["iyaan"], loc="male_night",
         visual="Iyaan, now a tall strong young man in his plain black t-shirt and charcoal cargo trousers, standing alone in the middle of the rain-wet Malé street at night between dark buildings and red-lit shop fronts, fists clenched at his sides, his intense deep-set eyes staring ahead, his reflection shimmering on the wet pavement",
         camera="medium wide, slightly low angle, his face and shoulders in the upper third, the reflective wet pavement as a calm lower third",
         amb="rain_night", transition="dissolve"),
    dict(to=44, v1="beat_016", reason="scene change: Iyaan the investigative journalist at work in the newsroom", chars=["iyaan"], loc="newsroom",
         visual="Iyaan sitting alone at a desk in the dark empty newsroom late at night, typing intently on a laptop whose screen faces away from the viewer so only its cold blue glow lights his face, a few blank papers and a notebook beside him, his expression focused and hard",
         camera="medium shot, eye level, from across the desk", amb="office_night"),
    dict(to=47, v1="beat_017", reason="scene change: his hacking skills and private tracking network", chars=["iyaan"], loc="hacker_room",
         visual="Iyaan seated at his wide desk in his dark room facing three glowing monitors filled with abstract green code streams and a glowing network map of connected dots, no readable text, his fingers on the keyboard, the screen light reflected in his eyes, seen slightly from the side and behind",
         camera="medium shot over his shoulder from the side, his face and the monitors in the upper two-thirds, the desk top as a calm lower third",
         amb="hacker_room"),
    dict(to=50, v1="beat_018", reason="character and scene change: his frail widowed mother with her prayer beads", chars=["aminath"], loc="apartment",
         visual="the frail mother Aminath sitting on the worn sofa in the small dim sitting room, her white hijab fully covering her hair and neck, slowly passing prayer beads through her thin fingers, lips moving softly in dua, her tired eyes dull and faded with years of grief",
         camera="medium shot, eye level", amb="living_night"),
    # NEW (5.4) shot / reverse shot: Iyaan and his mother talk on the sofa
    dict(to=51, reason="5.4 speaker: Iyaan answers his mother and asks about her medicine — in the v1 hand-kiss image his face is bowed and hidden",
         chars=["iyaan", "aminath"], speaker="iyaan", loc="apartment",
         visual="exactly two people in the image, no one else: over-the-shoulder from behind his mother: Iyaan in his plain black t-shirt sitting close beside his frail mother on the worn sofa, turned toward her, gently holding her thin hands and her prayer beads in both of his after kissing them, looking at her face with a soft, reassuring expression as he speaks; his face sharp, three-quarter towards the camera and centred in the upper half; Aminath only once, in the near foreground at the left edge, seen softly from behind her shoulder, her white hijab fully covering her hair and neck, out of focus; a low table with a glass of water and small medicine bottles with blank labels",
         camera="medium close-up over the mother's shoulder, Iyaan's face centred in the upper half, the table top as a calm lower third",
         amb="living_night", transition="cut", sens="intimacy", safe="mother and son: he holds her hands, both fully clothed"),
    dict(to=54, reason="5.4 speaker: Aminath answers and begs him to be careful ('your father too…') — her face sits at the very edge of the v1 hand-kiss image, beyond the reach of any centred crop",
         chars=["aminath", "iyaan"], speaker="aminath", loc="apartment",
         visual="reverse shot over Iyaan's shoulder: the frail mother Aminath sitting on the worn sofa, her face sharp, three-quarter towards the camera and centred in the upper half, her white hijab fully covering her hair and neck, her worried eyes glistening and her lips trembling as she speaks, her prayer beads in her hands, which her son holds gently; Iyaan in the soft blurred near foreground at the side, seen from behind his shoulder in his plain black t-shirt",
         camera="medium close-up over the son's shoulder, Aminath's face centred in the upper half, their hands and the dim sofa as a calm lower third",
         amb="living_night", transition="cut", sens="intimacy", safe="mother and son: he holds her hands, both fully clothed"),
    dict(to=55, reuse="beat_021", reason="shot / reverse shot: Iyaan reassures his mother ('I will never forget what happened to Bappa')",
         loc="apartment", visual="(reuse of Iyaan speaking to his mother)", amb="living_night", transition="cut"),
    dict(to=58, v1="beat_020", reason="memory / time change: twelve-year-old Iyaan leaving the police station after the case was shelved", chars=["iyaan_young"], loc="police_station",
         visual="the boy Iyaan, now about twelve years old, a little taller and thinner, walking alone down the wet front steps of the plain grey police station in a light drizzle, shoulders slumped, looking back over his shoulder at the glass doors with bitter, disillusioned eyes",
         camera="medium wide, eye level from the foot of the steps, the boy and the doors in the upper two-thirds, wet steps as a calm lower third",
         amb="memory_rain", transition="dissolve"),
    dict(to=61, v1="beat_021", reason="scene change: that night in his locked room, the investigation board", chars=["iyaan"], loc="board_room",
         visual="Iyaan standing seen from behind and slightly to the side, facing the huge investigation board on his bedroom wall: dozens of small faceless blurred photographs and blank cards connected by taut red string, a large red question-mark symbol drawn by hand at the centre, the only mark on the board; his arms folded, the desk lamp casting his long shadow across the board",
         camera="medium wide from behind him, the board filling the upper two-thirds, the dark desk top as a calm lower third",
         amb="hacker_room", transition="dissolve"),
    dict(to=64, v1="beat_022", reason="action change: he opens his laptop and finds the police files stripped of evidence", chars=["iyaan"], loc="hacker_room",
         visual="close-up of Iyaan at his open laptop in the dark, its glow lighting his frowning face from below, the screen showing only blurred abstract document windows with solid black bars, no readable text, his jaw clenched, one hand pressed against his mouth in suspicion and frustration",
         camera="close-up, slightly low angle across the laptop, his face in the upper half", amb="hacker_room"),
    dict(to=67, reuse="beat_025", reason="return to the board: the rider identified and silenced; who gave the order?", loc="board_room",
         visual="(reuse of the investigation board)", amb="hacker_room", sens="other",
         safe="the overdose is never shown; the board with its question mark carries the unanswered question"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# dialogue shots (spec 5.4): speaker + tight crop centred on the speaker's face (focus = [x%, y%] of the image)
def talk(spk, focus=None, crop="tight"):
    d = dict(speaker=spk, crop=crop, motion="slow push-in")
    if focus: d["focus"] = focus
    return d

BOY_004 = [66, 49]        # v1 beat_004: the boy's face (x 66, y 41)
MUM_004 = [37, 27]        # v1 beat_004: Aminath's face (x ~36, y 19) — crop clamps at the top, face in the upper quarter
BOY_007 = [39, 35]        # v1 beat_007: face at the glass
BOY_014 = [47, 41]        # v1 beat_014: the boy's resolute face
MUM_018 = [38, 30]        # v1 beat_018: Aminath on the sofa
IYA_022 = [34, 34]        # v1 beat_022: Iyaan at the laptop
BOY_N1 = [47, 44]         # new beat_010: the boy's face in the rain (x 47, y 36)
IYA_N2 = [56, 25]         # new beat_021: Iyaan (x 56, y 17) — crop clamps at the top
MUM_N3 = [42, 28]         # new beat_022: Aminath (x 42, y 20)

sh(1, "It was the year two thousand and eleven. A night in November. Malé's sky was wrapped in heavy black clouds.",
   [("thunder", "ވިލާތަކުން", -16)])
sh(2, "From the waves breaking on Malé's reef came a sound of nameless dread and unease. Few vehicles were moving on Malé's streets.",
   [("wave_crash", "ރާޅުތަކުން", -18)])
sh(3, "All of Malé lay in a frightening silence. Eight-year-old Iyaan was sitting by the window of his home's sitting room.")
sh(4, "He sat looking outside, lost in some thought. By then heavy rain had begun to fall.",
   [("rain_start", "ވާރޭ", -18)])
sh(5, "The drops of the pouring rain struck the window glass and ran down. In Iyaan's heart there was only waiting —")
sh(6, "for the moment his father, Member of Parliament Ahmed Zahir, would come home. Ahmed Zahir was an honest politician, loved by the people.")
sh(7, "His was a tongue that always spoke out loudly against corruption and oppression. Sometimes the price he had to pay for it was his own safety.")
sh(8, "His wife Aminath knew he had been receiving all kinds of threats against his life. Unease showed on the face of Aminath, sitting on the sitting-room sofa.")
sh(9, "She kept wringing her hands and glancing at the clock. The clock was striking eleven at night. The time Zahir had said the parliament committee meeting would end had long passed.")
sh(10, "\"Mamma, why is Bappa so late?\" Iyaan asked. Aminath forced a smile and moved close to Iyaan,",
   **talk("iyaan_young", BOY_004))
sh(11, "and stroked his hair. \"My child, Bappa is busy with great national work, isn't he?",
   [("cloth_rustle", "ފިރުމާލި", -24)], **talk("aminath_young", MUM_004))
sh(12, "To win the people their rights, Bappa has to work very hard. You go to sleep, my child.",
   **talk("aminath_young", MUM_004, "medium"))
sh(13, "When Bappa comes, Mamma will call you.\" Iyaan shook his head to say no. \"No, Bappa said that when he comes tonight he'll bring me a storybook.",
   **talk("iyaan_young", BOY_004))
sh(14, "I'll go when Bappa comes.\" Just then came the sound of a car stopping outside the house. Iyaan's face lit up. \"That's Bappa!\"",
   [("car_approach", "ކާރެއް", -16)], **talk("iyaan_young", BOY_004))
sh(15, "he cried out with joy. When Iyaan looked out of the window, Ahmed Zahir's black car had stopped at the gate of the house.")
sh(16, "Zahir got out of the back seat of the car. In his hand was a big briefcase. He smiled and raised a hand to the driver, then started walking toward the door of the house.",
   [("car_door", "ފޭބި", -16), ("footsteps_pavement", "ހިނގައިގަތް", -22)])
sh(17, "Suddenly, through the sound of the heavy rain, came the loud roar of a motorbike. On that motorbike, which came racing with its headlight off, were two men dressed in black with their faces covered.",
   [("motorbike_pass", "ސައިކަލެއްގެ", -14)])
sh(18, "The motorbike stopped right in front of Zahir. The driver saw it and tried to get out of the car.",
   [("brake_screech", "މަޑުކޮށްލީ", -18), ("car_door", "ފައިބަން", -20)])
sh(19, "But everything happened faster than anyone could imagine. The man on the back of the motorbike pulled out something like a long blade.",
   [("heartbeat", "ނެގި", -18)], hum=True)
sh(20, "Iyaan stood with his face pressed to the window glass. What he saw was that man striking his father's body with the blade. Not once,",
   [("soft_thud", "ހަރާލި", -24)], hum=True)
sh(21, "but again and again. The briefcase slipped from Bappa's hand and fell to the ground. A loud cry burst from Zahir's mouth. The cry carried into the house.",
   [("soft_thud", "ވެއްޓުނު", -20)], hum=True)
sh(22, "\"Bappa!\" Iyaan screamed. Aminath didn't know what was happening.",
   [("gasp", "ހަޅޭއްލަވައިގަތް", -18)], hum=True, **talk("iyaan_young", BOY_007))
sh(23, "She ran toward the door. Iyaan ran and threw open the big front door of the house. As he came out, the motorbike was speeding away.",
   [("footsteps_pavement", "ދުއްވައިގަތް", -22), ("door_open", "ހުޅުވާލި", -16), ("motorbike_pass", "ނައްޓާލަނީ", -16)])
sh(24, "In the light of the street lamps, Iyaan saw his father's body lying on the ground. The pool of water on the ground was turning red with the blood flowing from Zahir's body.",
   hum=True)
sh(25, "Iyaan ran and threw himself on his father. With his two small hands he held his father's face. \"Bappa!",
   [("sob_breath", "ބައްޕާ", -22)], hum=True, **talk("iyaan_young", BOY_N1))
sh(26, "Bappa! Open your eyes!\" Iyaan kept crying and screaming. His palms were soaked with his father's blood. Zahir was still conscious.",
   [("sob_breath", "ރޮމުން", -22)], hum=True, **talk("iyaan_young", BOY_N1))
sh(27, "With effort he opened his eyes. His breathing was growing short. He tried to take hold of Iyaan's small hand. But there was no strength left in that body.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
# 28-29: Zahir's last words — the speaker is never shown (bible rule 1); the listening boy's face is centred
sh(28, "Blood was coming from Zahir's mouth too. With effort he said: \"S... son... Mamma...",
   hum=True, crop="tight", focus=BOY_N1, motion="slow push-in")
sh(29, "look after...\" Those were his last words. Zahir's eyes closed. His body went still.",
   hum=True, crop="medium", focus=BOY_N1, motion="slow pull-out")
sh(30, "Aminath collapsed over Zahir's lifeless body, weeping. The sound of her weeping spread through the whole neighbourhood.",
   [("sob_breath", "ރޮމުންދިޔަ", -20)], hum=True)
sh(31, "The car's driver, shaking all over, was trying to phone for an ambulance. Neighbours began peering out of the windows of their houses.",
   [("siren", "އެމްބިއުލާންސަށް", -24)])
sh(32, "Iyaan's crying suddenly stopped. Though he wanted to cry, the shock to that small heart dried up his tears.",
   hum=True)
sh(33, "He sat staring at his two palms, soaked in his father's blood. That small mind could not grasp political power or corruption.")
sh(34, "But one thing became certain to him. Someone had snatched away his beloved father, his happy world.",
   hum=True)
sh(35, "As the raindrops struck Iyaan's face, an extraordinary fire was kindling deep in his heart. It was the fire of revenge.",
   [("heartbeat", "އަލިފާންގަނޑެއް", -18)], hum=True)
sh(36, "Looking at his father's face with its closed eyes, he said in his heart: \"Bappa, I will find the people who did this. I will take revenge on them.\"",
   hum=True, **talk("iyaan_young", BOY_014))
sh(37, "This was the night that changed Iyaan's life. That eight-year-old boy's innocence drowned that night in the pool of his father's blood on that road.",
   hum=True)
sh(38, "His heart turned to stone. Finding the truth of his father's death became the one purpose of his life.",
   [("thunder", "ހިލައަށް", -18)])
sh(39, "Fifteen years of silence. Every day that passed after his father's death was a day that washed the colour of happiness out of Iyaan's life.")
sh(40, "The days went by, and today he is twenty-three years old. His body is strong. He has grown into a tall young man.")
sh(41, "Jet-black hair, and deep secrets in his two sharp eyes. He is the most skilled investigative journalist at one of the country's big newspapers.")
sh(42, "Every piece he writes is brilliant, original writing built on hard truths that make government offices and politicians tremble.",
   [("keyboard_typing", "ލިޔާ", -20)])
sh(43, "But what nobody knows is the real purpose of that journalism. Iyaan did not spend the past fifteen years on study and journalism alone.")
sh(44, "Abroad, he has learned various styles of martial arts and the ways of defending himself.")
sh(45, "And beyond that, diving into the deepest corners of the digital world, he has also learned the hacking skills to obtain information and secret files.",
   [("keyboard_typing", "ހެކިންގެ", -20)])
sh(46, "He has also set up his own network for tracking. He is sacrificing his whole youth for one single purpose —",
   [("computer_beep", "ނެޓްވޯކެއް", -20)])
sh(47, "revenge on his father's killers. Iyaan was living with his mother Aminath in a small apartment in Henveiru.")
sh(48, "After his father's death, a great change came over his mother's life. She grew weak in mind and body.")
sh(49, "In that grief even the light in her eyes has faded. Every day when Iyaan comes home, his mother is sitting with her prayer beads, making some dua.")
sh(50, "\"Iyaan, my son, have you come home?\" his mother asked in her frail voice.",
   [("door_close", "އައީތަ", -22)], hum=True, **talk("aminath", MUM_018))
sh(51, "\"Yes, Mamma.\" Iyaan went and sat beside his mother and kissed both her hands. \"Mamma, have you taken your medicine?\"",
   **talk("iyaan", IYA_N2))
sh(52, "\"Yes, I've taken the medicine. My son... Mamma always worries",
   **talk("aminath", MUM_N3))
sh(53, "about this journalism work you do. Be careful when you write about the corruption of powerful politicians.",
   **talk("aminath", MUM_N3, "medium"))
sh(54, "Your father too...\" Her voice began to tremble and she broke off. Iyaan stroked his mother's hand. \"Mamma, don't worry.",
   [("sob_breath", "ތުރުތުރު", -22)], hum=True, **talk("aminath", MUM_N3))
sh(55, "I'm being very careful. I will never forget what happened to Bappa.\" At that moment Iyaan's heart was weeping.",
   hum=True, **talk("iyaan", IYA_N2))
sh(56, "He remembered the day the police shelved his father's murder case as unsolved. He was only twelve years old then.")
sh(57, "When he walked out of the police station, he lost all the trust he had in the country's system of justice.",
   [("footsteps_pavement", "ނުކުމެގެން", -22)])
sh(58, "The promise he made to himself that day was that one day he would still find justice. That night, after his mother fell asleep, Iyaan went into his room and locked the door.",
   [("lock_click", "ތަޅުލި", -18)])
sh(59, "On one wall of the room was a big board. On that board were photos of the night his father was killed and photos of the members of parliament at the time.")
sh(60, "And the information on various people was linked with red string. In the middle of the board was a big question mark.")
sh(61, "That was because he did not know who the real mastermind who ordered his father's killing was. Iyaan opened his laptop.",
   [("power_up", "ހުޅުވާލި", -20)])
sh(62, "He had obtained the investigation files on his father's murder from the police's secret database. As he read through those files, Iyaan noticed one thing.",
   [("keyboard_typing", "ހޯދާފަ", -22)])
sh(63, "Some key evidence and his father's phone recordings had been removed from those files. This could not be done without very high-level influence in the government.")
sh(64, "\"Who? Whose influence?\" Iyaan kept asking himself.",
   hum=True, **talk("iyaan", IYA_022))
sh(65, "He felt as if every road was closing in front of him. Through his work over the past fifteen years, he had identified the man who rode the motorbike that came to kill his father.",
   [("heartbeat", "އިހުސާސެއް", -20)], hum=True)
sh(66, "He was later reported to have died of a drug overdose. Who made him do it?")
sh(67, "That secret lies buried very deep. To be continued.",
   [("thunder", "ވަޅުލެވިފަ", -20)], hum=True)
SHOTS = S

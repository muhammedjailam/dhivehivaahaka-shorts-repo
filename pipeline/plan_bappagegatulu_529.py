"""Beat/shot plan for Bappage Gatulu episode 529 — v2 RE-CUT on the new (slower) audio (used by plan_beats.py).
The break-in at Asim's mansion, the near-capture under the desk, the escape over the balcony, the 'PZ 2011' log and
the 'Partners' Share' sheet (Asim, Sameer, Fareed), Raaya's 8 am call and the first anonymous warning to Fareed.
v2: beats re-anchored on the new segments; v1 images reused via v1="beat_###"; 3 new images for spec 5.4 (speaker
centred and sharp): the Raaya/Asim two-shot on arrival, and the Raaya / Asim shot-reverse-shot in the alarm.
The v1 plan is kept in output/BappageGatulu/v1/plans/plan_bappagegatulu_529.py."""

BREAKIN = ("Iyaan dressed for the break-in in a black long-sleeved hooded top with the hood up, black trousers, black "
           "gloves and a plain black cloth face mask covering his nose and mouth, only his intense dark eyes visible — "
           "NOT the plain black t-shirt of the reference; he carries no weapon of any kind")

MANSION_OFFICE = ("Asim's secret private office upstairs in his huge modern Malé mansion: a large dark polished wooden "
                  "desk with a leather chair, tall dark bookshelves full of leather-bound files covering the walls, a "
                  "big grey steel safe with a small keypad set into the wall behind the desk, a long heavy dark-red "
                  "floor-length curtain on one side hiding a glass balcony door, a heavy wooden door with a small "
                  "biometric reader panel beside it")

LOC = {
    "male_sky": "the skyline of Malé city at night seen across the dark rough sea: dense tall buildings with a few lit windows, black storm clouds piled overhead, wet rooftops",
    "resort": "an elegant open-sided banquet pavilion at Kurumba Maldives resort at night, long tables with white tablecloths, glass water jugs and juice glasses, warm lanterns, palm trees and the dark lagoon beyond",
    "lane": "a narrow dark lane behind a huge modern walled mansion in Malé at night: a high smooth concrete boundary wall topped with lights, overhanging tree branches, wet uneven paving, a single dim street lamp",
    "gate": "the tall dark metal gate in the high outer wall of Asim's huge modern mansion at night, a small black digital lock panel with a card pad beside it, wet paving, tree shadows",
    "sitting": "the vast luxurious sitting room of Asim's mansion at night: polished white marble floors, expensive cream sofas, a glass coffee table, tall windows, a sweeping marble staircase rising in the background",
    "landing": "the upstairs landing of Asim's mansion at night: the top of a marble staircase, a dark corridor and a big heavy dark wooden office door with a small glowing biometric fingerprint reader panel beside it",
    "office_dark": MANSION_OFFICE + ", the room completely dark",
    "office_lit": MANSION_OFFICE + ", the room brightly lit by the ceiling lights",
    "office_alarm": MANSION_OFFICE + ", the room plunged into darkness",
    "hall": "the grand double-height entrance hall of Asim's mansion at night: marble floor, a sweeping marble staircase with a gold handrail, dim wall lights",
    "balcony": "a wide upstairs balcony at the back of Asim's mansion at night: a waist-high smooth white parapet wall, a glass door with a curtain behind it, dark leafy trees beyond the wall, light rain",
    "lane_exit": "the same narrow dark lane behind the mansion at night, wet paving, dark trees spilling over the high wall, a single dim street lamp far away",
    "room_night": "Iyaan's small locked bedroom in a modest Hulhumalé apartment: a single bed with a plain dark cover against one wall, a desk with three computer monitors and a keyboard, a wall-sized investigation board covered in small faceless blurred photos linked by red string",
    "room_morning": "Iyaan's small bedroom in a modest Hulhumalé apartment: a desk with three computer monitors and a keyboard, the wall-sized investigation board covered in small faceless blurred photos linked by red string, a window with half-open blinds",
    "mansion_day": "the luxurious marble sitting room of Asim's mansion in the morning, tall windows with daylight, expensive cream sofas",
}
MOOD = {
    "male_sky": "just past 2 am, pitch-dark sky, a jagged white lightning flash lighting the clouds and the sea, cold damp wind, rain about to pour, ominous",
    "resort": "night, warm golden lantern light, formal and calm, a quiet glittering contrast to the storm over Malé",
    "lane": "just past 2 am, deep teal darkness, the cold blue glow of a phone screen on his masked face, a faint red light from the wall, wind and a coming storm, tense",
    "gate": "just past 2 am, darkness, a small green light glowing on the lock panel, wet reflections, silent tension",
    "sitting": "just past 2 am, dark and silent, faint teal moonlight through tall windows, long shadows on the marble, stealthy",
    "landing": "just past 2 am, darkness, the cold blue glow of the reader panel lighting the gloved hand and masked face, breath-holding suspense",
    "office_dark": "just past 2 am, nearly total darkness cut by the narrow white beam of a small flashlight and a faint green glow from a small device, dust in the beam, tense silence",
    "office_lit": "just past 2 am, harsh bright white ceiling light, hard shadows under the desk, intense danger",
    "office_alarm": "just past 2 am, total darkness pulsing with flashing red alarm light, chaos and panic",
    "hall": "just past 2 am, dim warm wall lights in a dark hall, the storm flickering at the tall windows, tired and quiet",
    "balcony": "just past 2 am, dark night, light rain falling, a flash of distant lightning, cold wet teal light, the glow of the house lights behind the glass, narrow escape",
    "lane_exit": "just past 2 am, dark, light rain, wet reflections, a lonely figure walking away, relief and resolve",
    "room_night": "the small hours of the night, only the cold blue glow of monitors and a tablet in a dark room, red string glinting on the board, shaken and intense",
    "room_morning": "8 am, pale morning daylight through half-open blinds mixing with the cold blue monitor glow, tense calm",
    "mansion_day": "8 am, cold daylight through tall windows, distressed and frightened atmosphere",
}

BEATS = [
    dict(to=2, v1="beat_001", reason="episode opening: the stormy sky over Malé just past 2 am", loc="male_sky",
         visual="a jagged white lightning bolt splitting the black storm clouds over the dark Malé skyline, the rough sea below catching the flash, wind bending a few palm trees in the foreground silhouette, no people",
         camera="wide establishing shot, the sky and lightning in the upper two-thirds, the dark sea as a calm lower third", amb="storm_night"),
    dict(to=3, v1="beat_002", reason="scene and character change: Asim and Raaya are away at the official banquet at Kurumba resort", chars=["asim", "raaya"], loc="resort",
         visual="Asim in his white shirt seated at a long banquet table with white tablecloth, smiling proudly and talking to unseen foreign guests, Raaya seated beside him with a polite tired smile; only glasses of water and juice on the table; the lagoon dark behind them",
         camera="medium shot, eye level", amb="resort_evening"),
    dict(to=8, v1="beat_003", reason="scene and character change: Iyaan waits in the lane behind the mansion and starts the virus", chars=["iyaan"], loc="lane",
         visual=BREAKIN + "; he stands pressed against the high boundary wall in the narrow dark lane, looking down at the phone in his gloved hands, its screen glowing with abstract lines of code, his eyes sharp and focused above the mask",
         camera="medium shot, slightly low angle, the wall rising behind him", amb="night_lane"),
    dict(to=9, v1="beat_004", reason="action change: the copied card opens the outer gate", chars=["iyaan"], loc="gate",
         visual=BREAKIN + "; close view of his gloved hand holding a plain blank white card against a small black lock panel beside the tall dark metal gate, the panel's small light turning green, his masked face in profile just behind, the gate starting to open a crack",
         camera="close-up from the side, his eyes in the upper frame", amb="night_exterior"),
    dict(to=11, v1="beat_005", reason="scene change: he crosses the dark sitting room like a shadow", chars=["iyaan"], loc="sitting",
         visual=BREAKIN + "; he moves silently in a low crouching walk across the vast dark marble sitting room towards the staircase, a dark lean figure among the expensive sofas, his reflection faint on the polished floor",
         camera="wide shot from a high corner, the figure in the upper half, the gleaming floor as a calm lower third", amb="mansion_night"),
    dict(to=14, v1="beat_006", reason="scene and action change: the fingerprint reader at the secret office door", chars=["iyaan"], loc="landing",
         visual=BREAKIN + "; he stands at the big dark office door and presses his gloved right thumb, with a thin transparent silicone layer on it, onto the small glowing biometric reader panel; the panel glows soft green; he holds his breath, eyes wide above the mask",
         camera="medium close-up from the side, the panel and his eyes in the upper two-thirds", amb="mansion_night"),
    dict(to=17, v1="beat_007", reason="scene change: inside Asim's secret office by flashlight", chars=["iyaan"], loc="office_dark",
         visual=BREAKIN + "; he stands just inside the dark office holding a small flashlight, its narrow white beam sweeping over the large dark desk and the tall bookshelves and coming to rest on the big grey steel safe in the wall behind the desk",
         camera="wide shot from behind his shoulder, the beam and the safe in the upper half, the dark floor as a calm lower third", amb="office_night"),
    dict(to=19, v1="beat_008", reason="action change: the code-breaking device on the safe; a car stops outside", chars=["iyaan"], loc="office_dark",
         visual=BREAKIN + "; he crouches in front of the big grey steel safe behind the desk; a small black device is clipped onto the safe's keypad, its little screen flickering with rapidly changing abstract bars of green light (no digits); he has turned his head sharply over his shoulder towards the closed door, eyes wide and alarmed above the mask",
         camera="medium shot, eye level, from the side", amb="office_night"),
    # NEW (5.4): Raaya and Asim both speak (20-21); in the v1 staircase image Raaya is at the left edge (x 25 %)
    dict(to=21, reason="5.4 dialogue: Raaya ('Bappa, I'm so tired') and Asim ('go to sleep, dear') speak as they come in; the v1 staircase image has Raaya at the edge, so a two-shot with both faces near the centre",
         chars=["raaya", "asim"], loc="hall",
         visual="Raaya and her father Asim have just stepped in through the tall front door into the grand entrance hall, standing side by side with a small gap between them, both facing the camera in three-quarter view, both faces clearly visible and sharp close to the centre of the frame: Raaya on the centre-left in her white dress and light-grey hijab fully covering her hair, holding her handbag, tired eyes, speaking wearily to her father; Asim on the centre-right in his white shirt and black trousers, turning his head towards her with a slight paternal smile as he answers; they are not touching; behind them the open front door and the stormy night",
         camera="medium shot, eye level, both faces in the upper half of the frame, the marble floor as a calm lower third", amb="mansion_night"),
    dict(to=22, v1="beat_009", reason="action change: Asim heads up the stairs, straight towards the office", chars=["asim", "raaya"], loc="hall",
         visual="Asim in his white shirt and black trousers starting to climb the sweeping marble staircase with a heavy purposeful step, looking up towards the dark upper floor; Raaya a few steps behind him at the foot of the stairs, holding her handbag, looking tired; dim wall lights",
         camera="wide shot from the upper landing looking down, the figures in the upper half, the marble floor as a calm lower third", amb="mansion_night"),
    dict(to=25, reason="return to Iyaan at the safe as the footsteps reach the door", reuse="beat_008", loc="office_dark",
         visual="reuse", camera="reuse", amb="office_night"),
    dict(to=26, v1="beat_011", reason="action change: he hides under the desk as the door opens and the light comes on", chars=["iyaan"], loc="office_lit",
         visual=BREAKIN + "; he is crouched in the dark space beneath the big wooden desk with his knees drawn up to his chest, clutching the small black device, pressed back against the inner panel, the bright ceiling light suddenly flooding the room around the desk; he is sitting upright in a crouch, not lying",
         camera="low angle from floor level, eye level with him, the desk top in the upper frame", amb="office_night",
         sens="other", safe="hiding shown as an upright crouch under the desk, knees drawn up, never lying flat"),
    dict(to=29, v1="beat_012", reason="new framing: from under the desk he sees Asim's black shoes while Asim searches the files", chars=["iyaan"], loc="office_lit",
         visual=BREAKIN + "; seen from deep under the desk: his masked face and wide eyes in the foreground shadow on the left, and beyond the edge of the desk on the right a pair of expensive polished black leather shoes and black trouser legs of a man standing at the desk; bright light beyond; his gloved hand hovering near a small drawer handle",
         camera="low floor-level shot from under the desk, his eyes in the upper half", amb="office_night"),
    dict(to=32, v1="beat_013", reason="character change: Asim hears the paperweight rattle and searches the room", chars=["asim"], loc="office_lit",
         visual="Asim in his white shirt standing beside the big desk, a stack of blank folders under one hand and a small round glass paperweight on the desk beside it, his head turned sharply, cold narrow eyes suspicious and alarmed, starting to step slowly round to the back of the desk",
         camera="medium shot, slightly low angle", amb="office_night"),
    dict(to=36, v1="beat_014", reason="action change: the power dies, the alarm and red siren light fill the house", chars=["asim"], loc="office_alarm",
         visual="the office plunged into darkness lit only by pulsing red alarm light; Asim, half-turned beside the desk, straightening up in shock and shouting towards the door, one arm raised, his white shirt glowing red in the flashing light",
         camera="medium wide shot, eye level", amb="office_night"),
    dict(to=39, v1="beat_015", reason="focus change: Iyaan under the desk, his phone shows the fuse overload, one minute to escape", chars=["iyaan"], loc="office_alarm",
         visual=BREAKIN + "; crouched under the desk with his knees drawn up, the soft glow of the phone screen in his gloved hand lighting his eyes from below, beads of sweat on his forehead above the mask, flashing red light around him; upright crouch, not lying",
         camera="close-up, eye level", amb="office_night",
         sens="other", safe="'lying under the desk' shown as an upright crouch"),
    # NEW (5.4) shot / reverse shot: Raaya calls out (40-41), Asim answers (42); in the v1 image Raaya is at x 15 % and Asim in profile
    dict(to=41, reason="5.4 dialogue: Raaya bursts in calling 'Bappa! Bappa, where are you?' — in the v1 doorway image she is small at the left edge; new image framed on her",
         chars=["raaya"], loc="office_alarm", speaker="raaya",
         visual="Raaya standing in the open doorway of the dark office, centred in the frame, in her white dress and light-grey hijab fully covering her hair and neck, holding up her phone with its flashlight on, the white beam pointing down and to the side into the room, her face terrified, eyes wide, mouth open as she calls out, her face sharp and clearly lit by the phone glow; pulsing red alarm light on the door frame and the dark corridor behind her",
         camera="medium close-up from inside the room, eye level, Raaya centred in the upper half, the dark floor as a calm lower third", amb="office_night"),
    dict(to=42, reason="5.4 dialogue reverse shot: Asim shouts 'Raaya! Don't come in!' and leads her downstairs — in the v1 image he is in profile; new image framed on him",
         chars=["asim", "raaya"], loc="office_alarm", speaker="asim", transition="cut",
         visual="over Raaya's shoulder from the doorway: Asim in his white shirt and black trousers centred in the frame, striding towards the door through the red-flashing dark office, his face turned towards the camera in three-quarter view, sharp and clearly lit, shouting urgently, one palm raised to stop her and the other hand held out towards her; Raaya seen from behind at the left edge of the frame, soft and out of focus, her light-grey hijab fully covering her hair; they are not touching; the desk and the long curtain dim in the red light behind him",
         camera="over-the-shoulder medium shot, eye level, Asim centred in the upper half", amb="office_night"),
    dict(to=43, v1="beat_016", reason="return to the doorway moment: Asim's attention turns to Raaya — Iyaan's golden chance", chars=["raaya", "asim"], loc="office_alarm",
         visual="Raaya standing in the open office doorway holding up her phone flashlight, its white beam cutting through the red-flashing darkness, her face terrified; Asim striding across the room towards her with one arm raised to stop her coming in; Asim and Raaya not touching",
         camera="medium wide shot from inside the room", amb="office_night"),
    dict(to=45, v1="beat_017", reason="action change: Iyaan slips behind the long curtain to the glass balcony door", chars=["iyaan"], loc="office_alarm",
         visual=BREAKIN + "; a lean dark figure slipping silently behind the long heavy floor-length curtain, one gloved hand drawing it aside to reveal a glass balcony door with rain on the glass beyond, faint red alarm light on the folds",
         camera="medium shot from across the room", amb="office_night"),
    dict(to=48, v1="beat_018", reason="action change: the lights return; Asim looks back into the empty office", chars=["asim", "raaya"], loc="office_lit",
         visual="Asim standing in the office doorway in the restored bright light, looking back over his shoulder into the empty office with a frown of doubt; the desk, the chair and the space under the desk all empty; the long curtain hanging still; Raaya waiting just behind him in the corridor",
         camera="wide shot from inside the room towards the door", amb="mansion_night"),
    dict(to=50, v1="beat_019", reason="scene change: Iyaan on the balcony, breathing again; the safe data is on his phone", chars=["iyaan"], loc="balcony",
         visual=BREAKIN + "; he stands with his back pressed against the wall beside the glass balcony door in the light rain, chest heaving, eyes closed for a moment of relief, his phone in his gloved hand glowing with a small progress bar of light; warm house light leaking through the curtain behind the glass",
         camera="medium shot, eye level", amb="balcony_night"),
    dict(to=51, v1="beat_020", reason="action change: he crouches on the balcony wall, ready to drop into the trees", chars=["iyaan"], loc="balcony",
         visual=BREAKIN + "; seen from behind and to the side, he is crouched low on top of the white balcony parapet wall like a cat, one gloved hand on the wall, poised and balanced, looking down at the dark trees below, rain falling; he is perfectly steady, not falling",
         camera="medium wide shot, slightly low angle, the figure in the upper half", amb="balcony_night",
         sens="other", safe="the jump shown as a steady crouch on the balcony wall, no fall"),
    dict(to=53, v1="beat_021", reason="scene change: in the lane he pulls off the mask and walks away", chars=["iyaan"], loc="lane_exit",
         visual="Iyaan walking away down the dark wet lane in his black long-sleeved hooded top with the hood down, black trousers and black gloves — NOT the plain black t-shirt of the reference — pulling the black cloth mask off his face with one hand, his face revealed, a look of grim relief and resolve, glancing at the glowing phone in his other hand",
         camera="medium shot, slightly from the front", amb="night_lane"),
    dict(to=55, v1="beat_022", reason="scene change: home, in his locked room, he opens the downloaded folder on a tablet", chars=["iyaan"], loc="room_night", transition="black",
         visual="Iyaan sitting upright on the edge of his single bed, fully clothed in his plain black t-shirt and charcoal cargo trousers, still shaken, holding a tablet in both hands, its glow lighting his tense face; behind him the desk monitors glow blue and the investigation board looms in the dark",
         camera="medium shot, eye level", amb="hacker_room",
         sens="clothing", safe="narration has him take off his t-shirt and lie on the bed; shown sitting on the edge of the bed fully clothed"),
    dict(to=59, v1="beat_023", reason="emotional turning point: the secret 2011 police log of Asim's orders", chars=["iyaan"], loc="room_night",
         visual="close-up of Iyaan's face lit by the cold glow of a monitor, his eyes widening in shock and fury; on the desk in front of the screen a blank sealed manila envelope; the monitor shows only blurred grey document pages with no readable marks",
         camera="close-up, eye level, from beside the monitor", amb="hacker_room",
         sens="violence", safe="the destroyed weapon fingerprint report and number plate are only a blank sealed envelope and blurred pages"),
    dict(to=62, v1="beat_024", reason="new reveal: the 'Partners' Share' spreadsheet of three partners", chars=["iyaan"], loc="room_night",
         visual="over Iyaan's shoulder at his desk: the big monitor glows with an abstract spreadsheet grid of coloured cells and three tall red bars, no letters or numbers anywhere, his face reflected faintly in the screen, his hand frozen on the mouse",
         camera="over-the-shoulder medium shot", amb="hacker_room"),
    dict(to=66, reason="return to his face as he takes in that the whole system took his father's life (he speaks: centred by crop)", reuse="beat_026", loc="room_night",
         visual="reuse", camera="reuse", amb="hacker_room"),
    dict(to=69, v1="beat_026", reason="action change: he pins Sameer's and Fareed's photos beside Asim's and links them with red string", chars=["iyaan", "asim", "sameer", "fareed"], loc="room_night",
         visual="Iyaan is the ONLY person in the room: he stands at the wall-sized investigation board stretching a red string between three small printed photo portraits pinned in a row in the centre — a small portrait of Asim in the middle, a small portrait of Sameer with round glasses on the left and a small portrait of Fareed with a thin moustache on the right, each only a palm-sized photo; Asim, Sameer and Fareed appear ONLY as these small pinned photos, not as people in the room; Iyaan's face in three-quarter profile, cold and determined",
         camera="medium shot from the side, the board and his face in the upper two-thirds", amb="hacker_room",
         sens="other", safe="Sameer and Fareed only as small portrait photos on the board; no text on the board"),
    dict(to=71, reason="return to the screen as he separates Fareed's bank files for the plan", reuse="beat_027", loc="room_night",
         visual="reuse", camera="reuse", amb="hacker_room"),
    # phone call 8 am: shot / reverse shot between Iyaan (beat_031) and Raaya (beat_032), clean cuts (5.4 / 11)
    dict(to=73, v1="beat_028", reason="time jump: 8 am, Raaya calls", chars=["iyaan"], loc="room_morning", transition="black",
         visual="Iyaan seated at his desk in pale morning light, holding his phone to his ear, his face carefully composed into calm concern while his eyes stay cold and watchful; the monitors glow behind him",
         camera="medium close-up, eye level", amb="hacker_room"),
    dict(to=75, v1="beat_029", reason="character and scene change: Raaya, frightened, on the phone at the mansion with police around", chars=["raaya"], loc="mansion_day", transition="cut",
         visual="Raaya standing by a tall window in the marble sitting room holding her phone to her ear with both hands, eyes red and frightened, a hand near her mouth; in the soft-focus background two police officers in dark-blue uniforms with no visible weapons examine the staircase",
         camera="medium close-up, eye level", amb="mansion_day"),
    dict(to=77, reason="back to Iyaan acting shocked on the phone ('What? Raaya, calm down...')", reuse="beat_031", loc="room_morning", transition="cut",
         visual="reuse", camera="reuse", amb="hacker_room"),
    dict(to=79, reason="back to Raaya: her father is terrified, she is scared", reuse="beat_032", loc="mansion_day", transition="cut",
         visual="reuse", camera="reuse", amb="mansion_day"),
    dict(to=81, reason="back to Iyaan: a twinge of pity, then his offer to come", reuse="beat_031", loc="room_morning", transition="cut",
         visual="reuse", camera="reuse", amb="hacker_room"),
    dict(to=83, reason="back to Raaya: 'don't come here now', she hangs up", reuse="beat_032", loc="mansion_day", transition="cut",
         visual="reuse", camera="reuse", amb="mansion_day"),
    dict(to=85, v1="beat_035", reason="action change: the CCTV logs show only an empty staircase", chars=["iyaan"], loc="room_morning",
         visual="the big monitor on Iyaan's desk showing a grid of grey surveillance camera views of an empty marble staircase and empty corridors, no people in any of them, no text; Iyaan's dark silhouette in the foreground at the edge of the frame watching with a faint satisfied look",
         camera="over-the-shoulder shot, the screen in the upper two-thirds", amb="hacker_room"),
    dict(to=88, v1="beat_036", reason="action change: he opens the dark hacker network and sends the first warning to Fareed", chars=["iyaan"], loc="room_morning",
         visual="Iyaan leaning towards his monitors, typing, his face lit green by a black screen filled with cascading green code lines and a small white faceless mask silhouette icon, no letters readable; a dangerous slight smile; the investigation board with the red string behind him",
         camera="medium close-up, eye level, from beside the monitors", amb="hacker_room"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# focus points ([x %, y %] of the image) read off the labelled grids (face centre x, face centre y + ~8, clamped to the range)
F003 = [31, 37]   # masked Iyaan in the lane (v1 beat_003)
F013 = [39, 35]   # Asim at the desk, three-quarter (v1 beat_013)
F014 = [46, 35]   # Asim shouting in the red alarm light (v1 beat_014)
F021 = [49, 35]   # Iyaan in the lane, mask off (v1 beat_021)
F023 = [50, 35]   # Iyaan close-up at the monitor (v1 beat_023)
F028 = [54, 35]   # Iyaan on the phone (v1 beat_028)
F029 = [40, 35]   # Raaya on the phone (v1 beat_029)
FN09_R = [32, 35]  # NEW beat_009 two-shot: Raaya (face x 32, y 22)
FN09_A = [69, 35]  # NEW beat_009 two-shot: Asim (face x 69, y 18)
FN17 = [44, 35]    # NEW beat_017 Raaya in the doorway (face x 44, y 17)
FN18 = [52, 35]    # NEW beat_018 Asim over Raaya's shoulder (face x 52, y 16)

sh(1, "The sky over Malé was very dark. Now and then lightning flashed, and every flash spread a frightening light.",
   [("thunder", "ގުގުރަމުން", -16)])
sh(2, "The sound of the thunder was louder still. A cold, damp wind was blowing hard. It seemed the rain could pour down at any moment.",
   [("thunder", "ގުގުރީގެ", -18), ("wind_gust", "ވައި", -20)])
sh(3, "The clock had just passed midnight. Home Minister Asim and his daughter Raaya were away at Kurumba Maldives resort, at a big official banquet held for a foreign delegation.")
sh(4, "At the house there were only the guards who watched the security of the outer wall. Iyaan was in a narrow lane behind Asim's house.")
sh(5, "He was dressed in black. His face was covered with a mask. On the phone in his hand, codes were running.")
sh(6, "His heart was pounding hard. \"Three, two, one, run.\"",
   [("heartbeat", "ތެޅެމުން", -18), ("computer_beep", "ރަން", -20)], speaker="iyaan", crop="tight", focus=F003)
sh(7, "Iyaan said it softly. The virus he had prepared entered the main server of Asim's house and stopped the CCTV camera feeds.",
   [("computer_beep", "ހުއްޓުވާލި", -22)], speaker="iyaan", crop="tight", focus=F003)
sh(8, "Now the guards in the security room would see on their screens only a quiet scene recorded five minutes earlier.")
sh(9, "After slipping the phone into his pocket, Iyaan moved up to the digital lock of the outer gate. As he touched it with the digital card he had copied from Raaya, the gate opened with a quiet beep.",
   [("computer_beep", "ބީޕް", -18), ("lock_click", "ހުޅުވުނު", -18)])
sh(10, "Iyaan slipped into the house like a shadow. He went through the sitting room without paying the cameras any attention.")
sh(11, "The cameras had been hacked. Still, it was so silent that even the sound of each of his footsteps on the floor sent a shiver through the whole place.",
   [("footsteps_pavement", "ފިޔަވަޅެއްގެ", -24)])
sh(12, "He climbed the stairs and stopped in front of Asim's secret office. On the room's big door was a biometric fingerprint reader glowing with a blue light.",
   [("footsteps_pavement", "އަރައި", -24)])
sh(13, "Iyaan placed the thin silicone print stuck to his right thumb on the reader. Shhh...")
sh(14, "A red light ran across the reader. Iyaan held his breath. Beep! The reader's light turned green.",
   [("computer_beep", "ރަތްކުލައިގެ", -22), ("breath", "ނޭވާ", -22), ("computer_beep", "ބީޕް!", -16)], hum=True)
sh(15, "And from inside the door came the heavy sound of the lock opening. Iyaan quickly went in and pushed the door shut. Silence filled the room.",
   [("lock_click", "ހުޅުވުނު", -16), ("door_close", "ލައްޕާލި", -20)])
sh(16, "Iyaan switched on the small flashlight in his hand. It was Asim's secret office: a big desk, and huge bookshelves on the walls.",
   [("flashlight_click", "ދިއްލާލި", -18)])
sh(17, "Iyaan's target was the big steel safe behind the desk. Iyaan realised that his father's murder files and Asim's dark documents would be in there.")
sh(18, "He attached a special device to the safe's screen to crack its digital code. The numbers began changing at great speed.",
   [("computer_beep", "ތަތްކުރި", -22)])
sh(19, "Suddenly a sound reached Iyaan's ears and his whole body went rigid. The sound of a car stopping outside the house.",
   [("car_approach", "ކާރެއް", -20)])
sh(20, "Then came the sound of people talking loudly as they came into the house. \"Bappa,",
   [("door_open", "ވަދެގެން", -22)], speaker="raaya", crop="tight", focus=FN09_R)
sh(21, "I'm so tired today.\" That was Raaya's voice. \"Go to sleep, dear.\" That was Asim's voice.",
   speaker="asim", crop="tight", focus=FN09_A)
sh(22, "His footsteps began to climb the stairs. Iyaan began to sweat. Asim was coming straight to this room.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކުގެ", -20)], hum=True)
sh(23, "The safe still needed another minute to crack the code. When Iyaan looked, the safe's screen still showed the numbers changing.")
sh(24, "There was no way for him to get out of here. The room's door opened straight towards where Asim was coming from.")
sh(25, "The footsteps stopped right at the room's door. The door's biometric lock beeped. The lock began to open.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކުގެ", -18), ("computer_beep", "ބީޕްވި", -16), ("lock_click", "ހުޅުވެން", -16)], hum=True)
sh(26, "Iyaan didn't know what to do. In an instant he snatched the device off the safe, slipped under the desk and hid.",
   [("cloth_rustle", "ނިވާވި", -22)])
sh(27, "At that moment the door opened and the room's big light came on. The whole room lit up. Under the desk, holding his breath, all Iyaan could see were Asim's expensive black shoes.",
   [("door_open", "ހުޅުވި", -18), ("breath", "ނޭވާ", -24)])
sh(28, "Asim walked over and stopped at the desk. He began searching through some files on the desk. Iyaan's heart felt as if it would burst out of his chest.",
   [("paper_shuffle", "ހާވަން", -20), ("heartbeat", "ހިތް", -18)], hum=True)
sh(29, "Iyaan's hand brushed against a small drawer under the desk. The moment his hand trembled slightly, there was the sound of a glass paperweight on the desk rattling.",
   [("cup_clatter", "ގުޑިލި", -18)])
sh(30, "Asim stopped. He looked around. \"Who's there?\" There was alarm and menace in Asim's voice.",
   speaker="asim", crop="tight", focus=F013)
sh(31, "He slowly stepped back and began looking from corner to corner. Asim's footsteps moved slowly round the back of the desk, closer and closer to where Iyaan was.",
   [("footsteps_pavement", "ފިޔަވަޅުތައް", -22)])
sh(32, "Iyaan's eyes went wide. Had his journey of revenge ended right here? Just as Asim was about to bend down under the desk...", hum=True)
sh(33, "Suddenly every light in the house went out and the whole place went dark. A loud alarm rang through the whole house.",
   [("power_down", "ނިވި", -16), ("alarm_beep", "އެލާމެއްގެ", -16)])
sh(34, "The whole place sank into pitch darkness. At that moment the loud red-alert siren of the house filled the entire building.",
   [("siren", "ސައިރަންގެ", -18)], hum=True)
sh(35, "Asim had bent towards the space under the desk, but the sudden power cut and the darkness stopped him in his tracks.")
sh(36, "Stepping back, Asim shouted loudly to his security guards: \"Where are you? Why did the power go? Turn on the backup!\"",
   speaker="asim", crop="tight", focus=F014)
sh(37, "There was command and alarm in Asim's voice. Under the desk, using every ounce of strength his body had, Iyaan")
sh(38, "held his breath. His phone screen slowly lit up. His secret software had overloaded the house's main fuse system.",
   [("breath_heavy", "ނޭވާ", -22), ("computer_beep", "ދިއްލުނު", -24)])
sh(39, "But the backup generator would start in just one minute. Within that minute he had to get out of there.")
sh(40, "Suddenly the big office door was flung open with a bang, and the light of a phone flashlight fell into the room. \"Bappa!",
   [("door_open", "ހުޅުވުނު", -16)], speaker="raaya", crop="medium", focus=[44, 42])
sh(41, "Bappa, where are you?\" It was Raaya's voice. She was nearly out of her mind with fear. With the alarm sounding through the whole house, she had run straight to her father's room.",
   [("footsteps_pavement", "ދުވެފައި", -22)], speaker="raaya", crop="tight", focus=FN17, hum=True)
sh(42, "\"Raaya! Don't come in! Something has gone wrong with the system. Come, dear, let's go downstairs.\" Asim took Raaya by the hand and went out through the door.",
   speaker="asim", crop="tight", focus=FN18)
sh(43, "Those tiny few seconds when Asim's attention turned to Raaya were Iyaan's golden chance.")
sh(44, "Like a shadow Iyaan came out from under the desk and slipped behind the big curtain on the other side of the room.",
   [("cloth_rustle", "ފަރުދާގެ", -22)])
sh(45, "Behind that curtain was a glass door leading out to the balcony. Very quietly, Iyaan opened that door and stepped out onto the balcony.",
   [("door_open", "ހުޅުވާލައި", -22)])
sh(46, "At that moment the house's backup generator started with a loud roar. All the lights in the house came back on. The office lit up too.",
   [("power_up", "ޖެނެރޭޓަރުގެ", -16)])
sh(47, "Standing at the door, Asim turned and looked back into the office. Under the desk and the whole room were empty.")
sh(48, "Deciding it was only his imagination, he locked the door and went down the stairs with Raaya. On the balcony, Iyaan let out a deep breath.",
   [("lock_click", "ތަޅުލުމަށްފަހު", -18), ("footsteps_pavement", "ސިޑިން", -24), ("breath_heavy", "ނޭވާއެއް", -20)])
sh(49, "He was drenched in sweat. He had escaped by a hair. But he had not come away empty-handed.", hum=True)
sh(50, "Before he went under the desk, the device had cracked the safe's digital code and sent the safe's data to Iyaan's phone over wifi.",
   [("computer_beep", "ފޮނުވާފައި", -24)])
sh(51, "Iyaan jumped from the balcony wall and, through the trees behind the house, came out into the narrow lane. Pulling off the mask and putting it in his pocket, he walked away.",
   [("leaves_rustle", "ގަސްތަކުގެ", -20), ("soft_thud", "ފުންމާލައި", -22), ("footsteps_pavement", "ހިނގައިގަތް", -22)])
sh(52, "\"Raaya... you saved my life,\" Iyaan said to himself. But the spirit of revenge in his heart does not change.",
   speaker="iyaan", crop="tight", focus=F021, hum=True)
sh(53, "Asim's end has begun. Iyaan opened his phone. Among the files downloaded from the safe was a folder named 'PZ 2011'.",
   [("computer_beep", "ހުޅުވާލި", -24)])
sh(54, "Iyaan went into his room and locked the door. He was still trembling. He pulled off the black t-shirt he was wearing and lay down on the bed.",
   [("door_close", "ލެއްޕި", -20)])
sh(55, "He picked up the tablet on the bed and connected it to his main system. The folder downloaded from Asim's safe was now open, large on the screen.",
   [("computer_beep", "ގުޅާލި", -22)])
sh(56, "Iyaan opened the very first file in the folder. It was a secret police report from fifteen years ago.")
sh(57, "But this was not the kind of report usually found in police files. It was a log of the secret orders Asim had given to the lead investigator who ran the inquiry into his father's murder at the time.")
sh(58, "The more Iyaan read, the wider his eyes grew. To bury the case of his father's murder, the number plate of the motorbike seen at the scene, and")
sh(59, "the fingerprint reports from the weapon the killers used, had been secretly destroyed by a letter sent with Asim's own signature.",
   hum=True)
sh(60, "But what shook Iyaan most was the Excel sheet beneath it, named 'Partners' Share'.")
sh(61, "Asim was not the only one in the great plan to kill his father. Behind it lay the role of the three most powerful political figures of the government of that time.")
sh(62, "One of them is now the Speaker of Parliament, Sameer. And another is now the managing director of the country's biggest private bank, Fareed.")
sh(63, "From the evidence his father Ahmed Zahir had gathered, it is proven that these three together stole millions from the state budget and deposited them in secret accounts abroad.")
sh(64, "It was Fareed who paid for his father's murder. It was Sameer who covered it up politically. And it was Asim who sent the gangsters and had it carried out.")
sh(65, "\"This isn't only Asim's doing,\" Iyaan said softly. He took a deep breath.",
   [("sigh", "ނޭވާއެއް", -20)], speaker="iyaan", crop="tight", focus=F023)
sh(66, "\"This is the whole system. All of them together took my father's life.\" Iyaan got up, went over to the board on the wall and stopped.",
   speaker="iyaan", crop="medium", focus=[50, 42], hum=True)
sh(67, "On either side of Asim's photo he pinned the photos of Sameer and Fareed. Then he stretched a red string between the three of them, linking them all together.")
sh(68, "The battlefield of revenge has now grown far wider. Targeting Asim alone will never bring justice for his father's blood.")
sh(69, "Those three must break apart in front of one another, lose their power and be made to beg. A new plan began to take shape in Iyaan's mind.")
sh(70, "To destroy the trust between them. To make each of them suspect the other. Iyaan separated out the files of Fareed's secret bank transactions he had got from Asim's safe.",
   [("keyboard_typing", "ވަކިކޮށްލި", -22)], hum=True)
sh(71, "His plan was to use those files to threaten Fareed without Asim knowing. Then Fareed would believe it was Asim who was blackmailing him.")
sh(72, "While Iyaan sat lost in these thoughts, his phone began to vibrate. When he looked at the screen, it was Raaya calling. It was eight in the morning.",
   [("phone_buzz", "ވައިބްރޭޓްވާން", -16)])
sh(73, "After taking a deep breath, Iyaan made his voice sound normal and answered the phone. \"Hello, Raaya,\" Iyaan said.",
   [("breath", "ނޭވާއެއް", -22)], speaker="iyaan", crop="tight", focus=F028)
sh(74, "\"Iyaan... Iyaan... last night someone hacked our house's security system and got in.",
   speaker="raaya", crop="tight", focus=F029)
sh(75, "Bappa caught them while they were trying to open the safe in his office. They ran away. There are police all over the house. They're searching.\"",
   speaker="raaya", crop="medium", focus=[40, 42])
sh(76, "Raaya's voice sounded very distressed. You could tell from her voice that she was crying. Iyaan's heart almost stopped. But he instantly put on a show of shock.",
   [("sob_breath", "ރޮނީކަން", -22)], crop="medium", focus=[54, 42])
sh(77, "\"What? Raaya, calm down. Did anything happen to you? Is Bappa okay?\" \"We're okay.",
   speaker="iyaan", crop="tight", focus=F028)
sh(78, "But Bappa is really scared. Bappa says it's no ordinary thief. He says it's the work of one of Bappa's political enemies.",
   speaker="raaya", crop="medium", focus=[40, 42])
sh(79, "Iyaan... I'm so scared,\" Raaya said, sobbing. A small trace of pity entered Iyaan's heart.",
   [("sob_breath", "ގިސްލަމުން", -22)], speaker="raaya", crop="tight", focus=F029)
sh(80, "Raaya was an innocent girl with no fault in any of this. But she was a killer's child.", hum=True)
sh(81, "The price of her father's cruelty would have to be paid. \"Raaya, don't worry. I'm coming over to your house right now. To see you,\"",
   speaker="iyaan", crop="tight", focus=F028)
sh(82, "Iyaan said. \"No! Don't come to this house now. Bappa is in a state where he suspects all our friends.",
   speaker="raaya", crop="tight", focus=F029)
sh(83, "The police are even checking the phones of everyone in the house. I'll call you later.\" Raaya hung up. Iyaan sat staring at the phone.",
   [("computer_beep", "ކަނޑާލި", -22)], speaker="raaya", crop="medium", focus=[40, 42])
sh(84, "Asim had set out to find him using the entire police force. Iyaan checked the CCTV logs of Asim's house.")
sh(85, "His virus had wiped every frame of him. On the cameras the police would see nothing but an empty staircase.")
sh(86, "But the fear that had taken root in Asim's heart was Iyaan's first psychological victory. Iyaan sat down in front of the computer and opened a secret network of the kind used by hackers in black masks.",
   [("keyboard_typing", "ހުޅުވާލި", -20)])
sh(87, "His plan was to send the first warning letter, containing bank MD Fareed's secret information. The letter would go straight to Fareed's private email.",
   [("computer_beep", "އީމެއިލަށް", -20)])
sh(88, "And the sender's IP address would point to the address of Asim's office. The storm has begun. To be continued.",
   [("thunder", "ތޫފާން", -18)], hum=True)
SHOTS = S

"""Beat/shot plan for Bappage Gatulu episode 586 (used by plan_beats.py). PRESENT timeline only, no flashback.
Raaya takes Asim's red backup drive; four masked thugs raid Iyaan's flat at night (the fight is NEVER shown, bible
rule 13); next morning the fake 'job done' text; the studio; Asim's live-televised rally at 8 pm, Iyaan's signal
hijack, Asim's own recorded order on the hall speakers, Iyaan and Raaya walk in; "I am Ahmed Zahir's son"; Raaya calls
her father a killer; police storm the hall. New episode (no v1 images); spec 5.4 speaker focus built in from the start.
"""

COUPLE_GAP = "a clear arm's-length gap between them, they do not touch"
IYAAN_SUIT = ("Iyaan in a black suit jacket and black trousers over a plain black crew-neck top, no tie — NOT the plain "
              "black t-shirt of the reference; reference used for face only")
THUGS = ("dark faceless silhouettes of men in black hooded jackets with the hoods up and plain black cloth masks "
         "covering their faces, seen only from behind or in deep shadow, their hands empty and lost in shadow")
GOGGLES = "a pair of compact black night-vision goggles"

MANSION_OFFICE = ("Asim's secret private office upstairs in his huge modern Malé mansion: a large dark polished wooden "
                  "desk with a leather chair, tall dark bookshelves full of leather-bound files and books covering the "
                  "wall behind the desk, a big grey steel safe set into the wall at one side, a long heavy dark-red "
                  "floor-length curtain, a heavy wooden door")
HACKER = ("Iyaan's small bedroom-study in a modest apartment: a desk with three computer monitors and a keyboard, a "
          "wall-sized investigation board covered in small faceless blurred photos linked by red string, a window with "
          "blinds, a plain wooden door to a narrow hallway")
RALLY = ("a huge indoor convention-centre hall in Malé at night (8 pm), packed with seated and standing supporters, a "
         "wide raised stage with a podium and microphones, two giant LED screens behind the stage glowing with abstract "
         "images, plain teal-and-white drapes and flags with no symbols, TV cameras on tripods on a riser at the back, "
         "bright white stage lights and cold teal shadows over the crowd, no text, no logos")

LOC = {
    "studio_lane": "the narrow ground-floor doorway of an old three-storey building in a quiet Malé lane: peeling pale plaster, a worn wooden door standing open, a steep narrow staircase inside, the narrow lane outside with a few parked scooters and potted plants",
    "mansion_sitting": "the vast luxurious sitting room of Asim's mansion in Malé: polished white marble floors, expensive cream sofas, a glass coffee table, tall windows with heavy curtains, a sweeping marble staircase rising in the background",
    "office_eve": MANSION_OFFICE + ", a single brass desk lamp switched on",
    "apt_street": "a quiet narrow residential street at night outside a modest four-storey apartment block: wet paving, a single tall street lamp, parked scooters along the wall, the open dark stairwell entrance of the block",
    "hacker_night": HACKER + ", the blinds closed",
    "room_dark": HACKER + ", every light switched off",
    "room_lit": HACKER + ", the ceiling light switched on",
    "mansion_hall": "the grand double-height entrance hall of Asim's mansion at night: marble floor, a sweeping marble staircase with a gold handrail, a tall front door, dim wall lights",
    "room_morning": HACKER + ", the blinds half open",
    "male_road": "a wide main road in Malé in the morning: tall pastel and concrete buildings close on both sides, scooters and cars in the traffic, workers on tall ladders hanging huge plain banners and strings of plain teal-and-white flags from the lamp posts and balconies",
    "studio": "a silent rented art studio on the third floor of an old building in a quiet Malé lane, bare peeling plaster walls, blank canvases stacked against a wall, a paint-stained wooden table in the middle of the room with an open laptop on it, one tall old window with a dusty pane looking out over the narrow lane, a worn wooden floor, an old wooden door",
    "rally_hall": RALLY,
    "van": "the cramped dark interior of a black van parked in a side street not far from the convention centre at night: a narrow fold-down table with an open laptop, a small black satellite-antenna box with cables, tinted side windows with blurred distant city lights",
    "control_room": "the rally hall's control room: a dark room with long mixing desks and rows of monitors glowing with abstract images, cables, two empty office chairs pushed back",
}
MOOD = {
    "studio_lane": "present day, late afternoon, soft grey overcast light in the narrow lane, long shadows, quiet and heavy with grief",
    "mansion_sitting": "present day, early evening, only a few lamps lit, deep shadows over the marble, an unusual hollow silence, tense",
    "office_eve": "present day, evening, the warm pool of a single desk lamp, deep brown shadows on the bookshelves, hushed secret tension",
    "apt_street": "present day, night, cold teal darkness, the sodium-orange cone of one street lamp, wet reflections, menace",
    "hacker_night": "present day, night, the room dark except for the cold blue-and-green monitor glow on his face, calm and dangerous",
    "room_dark": "present day, night, pitch darkness rendered in a grainy green night-vision tint, deep black shadows, breathless tension",
    "room_lit": "present day, night, a plain white ceiling light suddenly on, hard shadows, adrenaline and resolve",
    "mansion_hall": "present day, night, dim wall lights, long shadows on the marble, a secret hurried feeling",
    "room_morning": "present day, the next morning, pale daylight through the half-open blinds, dust in the air, cold calm",
    "male_road": "present day, morning, bright hazy sunlight, busy and noisy, a looming political spectacle being built",
    "studio": "present day, late morning into afternoon, grey-white daylight through the dusty window, soft shadows, hushed and tense",
    "rally_hall": "present day, 8 pm, bright white stage lights and cold teal shadows over the crowd, the glow of the giant LED screens, a charged political spectacle",
    "van": "present day, 8 pm, near-darkness inside the van, the cold blue glow of the laptop on their faces, distant blurred city lights, breathless suspense",
    "control_room": "present day, 8 pm, dark room lit only by the monitors, now all glowing a deep alarming red, panic",
}

BEATS = [
    # ---------------- Day 1, evening: Raaya takes the drive ----------------
    dict(to=2, reason="episode opening, scene and character: Raaya leaves the art studio after the biggest decision of her life", chars=["raaya"], loc="studio_lane",
         visual="Raaya stepping out of the old wooden doorway of the building into the quiet narrow lane, her handbag strap gripped tight against her shoulder, wiping a tear from her cheek with the back of her hand, her eyes wet but set with a new resolve",
         camera="medium shot, eye level, her face in the upper third, the worn paving of the lane as a calm lower third", amb="city_day"),
    dict(to=4, reason="location change: Raaya comes home to the mansion; unusual silence, her father is out", chars=["raaya"], loc="mansion_sitting",
         visual="Raaya standing alone just inside the vast marble sitting room, small against the expensive empty sofas and the dark staircase, glancing warily around the silent house, one hand on her handbag",
         camera="wide shot, slightly high angle, her face in the upper half, the gleaming empty marble floor as the lower third", amb="mansion_night"),
    dict(to=8, reason="location and action change: in her father's office she opens the hidden compartment in the bookshelf and takes the red hard drive", chars=["raaya"], loc="office_eve",
         visual="Raaya standing at the tall bookshelf behind her father's big desk, a row of leather-bound books pushed aside and a narrow hidden wooden panel slid open in the shelf; she holds a small bright red hard drive in her hand, about to slip it into her open handbag, glancing back over her shoulder toward the closed door, her face tense and pale in the lamplight",
         camera="medium shot from the side of the desk, her face in the upper third, the dark desk top as a calm lower third", amb="office_quiet",
         sens="other", safe="a daughter taking a drive in her own home: no break-in imagery"),
    # ---------------- Day 1, night: the raid on Iyaan's flat (never depicted, rule 13) ----------------
    dict(to=10, reason="location and character change (cross-cut): two black motorbikes stop outside Iyaan's apartment block", chars=[], loc="apt_street",
         visual="two black motorbikes standing parked under a single street lamp outside a modest apartment block at night; four " + THUGS + ", walking away from the viewer toward the dark open stairwell entrance",
         camera="wide shot from far behind them at street level, the lamp and the building entrance in the upper half, the wet paving as the lower third", amb="street_night",
         sens="violence", safe="the narration's sharp weapons and iron bars are never shown: faceless silhouettes from far behind, hands empty and in shadow"),
    dict(to=13, speaker="iyaan", reason="location and character change: Iyaan at his computer sees the men on his hidden street cameras; he speaks softly to the screen (5.4)", chars=["iyaan"], loc="hacker_night",
         visual="Iyaan sitting at his desk in three-quarter view, a slim black headset on one ear, his calm cold face centred and lit by the monitor beside him; he is completely alone in the room — no other person anywhere in the room, the door behind him shut; the monitor shows a grainy green-grey security-camera view of an apartment stairwell with four small dark faceless figures climbing the stairs; no fear at all in his eyes",
         camera="medium close-up, eye level, his face centred in the upper half, the desk and keyboard as a calm lower third", amb="hacker_room",
         sens="other", safe="the men only as tiny faceless shapes on a grainy screen; no text or timestamp on the screen"),
    dict(to=17, reason="action change: lights off; Iyaan in night-vision goggles waits behind his door as the door opens", chars=["iyaan"], loc="room_dark",
         visual="Iyaan standing flat against the wall beside his half-open bedroom door in the dark, " + GOGGLES + " over his eyes, perfectly still like a shadow, his hands empty and relaxed; through the gap of the door a thin strip of hallway light and the dark shoulder of a faceless man in a black hooded jacket with a plain black cloth mask appearing at the threshold, his hands out of sight",
         camera="medium shot from inside the room, Iyaan's face in the upper half on one side and the door gap on the other, the dark floor as the lower third", amb="room_night",
         sens="violence", safe="night-vision goggles only; the electric baton is never shown; the intruder is a faceless shape in the door gap"),
    dict(to=20, reason="action change: the struggle in the dark (never depicted, rule 13): a green night-vision view of the room", chars=["iyaan"], loc="room_dark",
         visual="a grainy green night-vision view of the dark bedroom: Iyaan alone in the middle of the room crouched low in a calm martial-arts stance, " + GOGGLES + " over his eyes, both hands open and empty; behind him the doorway is only a blur of dark indistinct shapes; no one on the floor, nothing in anyone's hands",
         camera="wide shot, eye level, his figure centred in the upper half, the dark floor as a calm lower third", amb="room_night",
         sens="violence", safe="the disarming, the stun to the chest and the men falling are never shown: only Iyaan's empty-handed stance in a green night-vision view; muffled soft_thuds"),
    dict(to=23, reason="action change: Iyaan's remote starts Asim's recorded order on the wall speakers; the two remaining men freeze ('What is this?')", chars=[], loc="room_dark",
         visual="two dark faceless men in black hooded jackets with the hoods up and plain black cloth masks covering their faces, their hands empty and lost in shadow, frozen in the dark doorway, one of them centred, both heads turned up toward a small black wall speaker that pulses with a faint green light; beside them a framed picture hangs crooked on the wall; grainy green night-vision tint",
         camera="medium wide shot, eye level, the centred figure and the speaker in the upper half, the dark floor as the lower third", amb="room_night",
         sens="violence", safe="thrown bars never shown, only a crooked picture frame; the men faceless, hands empty"),
    dict(to=25, speaker="iyaan", reason="5.4 dialogue focus: Iyaan's voice from the darkness — 'this is your master's end'", chars=["iyaan"], loc="room_dark",
         visual="close-up of Iyaan, completely alone, his face emerging out of total black darkness with no other person anywhere in the frame, the night-vision goggles pushed up onto his forehead, a faint green glow on his cold calm face, eyes hard and fixed, centred in the frame",
         camera="close-up, eye level, his face centred in the upper half, black shadow below", amb="room_night",
         sens="violence", safe="the blows to the last two men are never shown: only his face in the dark; muffled soft_thud"),
    dict(to=26, speaker="iyaan", reason="action and light change: lights on; Iyaan, alone and resolute, phones Raaya (5.4)", chars=["iyaan"], loc="room_lit",
         visual="Iyaan standing alone by his desk in the now brightly lit room, framed from the waist up, a phone held to his ear, breathing hard but composed, strong determination on his face, centred; the doorway behind him empty, the investigation board with red string at his side",
         camera="medium shot, eye level, his face centred in the upper half, the desk edge as the lower third", amb="hacker_room",
         sens="violence", safe="the four unconscious men are never shown: framed from the waist up, the floor out of frame"),
    dict(to=27, speaker="raaya", transition="cut", reason="5.4 dialogue focus (the other end of the call): Raaya answers that she has the drive", chars=["raaya"], loc="mansion_hall",
         visual="Raaya standing by the tall front door in the dim marble entrance hall, her handbag on her shoulder, a phone held to her ear, the small red hard drive clutched in her other hand against her chest, whispering, tense but relieved, her face centred",
         camera="medium close-up, eye level, her face centred in the upper half, the marble floor and staircase behind her", amb="mansion_night"),
    dict(to=29, reuse="beat_010", transition="cut", reason="reverse shot: back to Iyaan on the phone — 'tomorrow night the whole nation will see the killers' end'", chars=["iyaan"], loc="room_lit",
         visual="reuse of beat_010: Iyaan on the phone in his lit room", camera="medium close-up", amb="hacker_room"),
    # ---------------- Day 2, morning ----------------
    dict(to=32, transition="black", reason="time jump: the next morning; Iyaan reads the thugs' messages to Asim and texts 'job done'", chars=["iyaan"], loc="room_morning",
         visual="Iyaan sitting at his desk in pale morning light, holding one of several cheap black phones laid out on the desk, its screen a blank pale glow, a cold satisfied look on his face; far behind him, out of focus in a shadowed corner of the room, four dark hooded figures sit slumped against the wall, heads bowed, hands out of sight",
         camera="medium shot, eye level, his face in the upper half, the desk with the phones as the lower third, the corner far and blurred", amb="room_day",
         sens="violence", safe="the captives are never shown tied up (rule 13/14): far, blurred, seated, hands out of sight; phone screens blank"),
    dict(to=34, reason="location change: Iyaan slips out and walks through Malé, where Asim's rally banners and flags are going up", chars=["iyaan"], loc="male_road",
         visual="Iyaan walking along the busy pavement with a laptop bag over his shoulder, glancing up coldly; above him workers on tall ladders hang a huge plain banner printed only with a large painted portrait of a heavy-set grey-moustached older man in a white shirt, and strings of plain teal-and-white flags across the road; no letters anywhere",
         camera="medium wide shot, eye level, his face in the upper half, the pavement as the lower third", amb="road_busy",
         sens="other", safe="banners and flags with no text, no logos and no real party colours (rule 14/17)"),
    dict(to=36, reason="location change: the studio; Raaya waits at the table with the red drive as Iyaan comes in", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya sitting at the paint-stained table, the small red hard drive lying on the table in front of her, worry in her eyes as she looks up; Iyaan just stepping in through the old wooden door on the far side of the room with his laptop bag; " + COUPLE_GAP + ", the whole room apart",
         camera="wide shot, eye level, both faces in the upper half, the worn wooden floor as a calm lower third", amb="room_day"),
    dict(to=38, speaker="raaya", reason="5.4 dialogue focus: Raaya stands and says she found all her father's secrets and can't believe the bitter truth", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya standing by the table, holding the small red hard drive out on her open palm, her face centred and sharp, eyes wet with disbelief, speaking; Iyaan seen softly from behind at the edge of the frame, " + COUPLE_GAP,
         camera="over-the-shoulder medium close-up, eye level, her face centred in the upper half, the table edge as the lower third", amb="room_day"),
    dict(to=40, speaker="iyaan", transition="cut", reason="5.4 reverse shot: Iyaan tells her she was very brave (the narration's hand on her shoulder is replaced)", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan facing her, his right hand pressed flat on his own chest in a respectful gesture, nodding gently, his face centred and sharp, warm but serious; Raaya seen softly from behind at the edge of the frame, " + COUPLE_GAP,
         camera="over-the-shoulder medium close-up, eye level, his face centred in the upper half", amb="room_day",
         sens="intimacy", safe="the narration has him lay his hand on Raaya's shoulder: shown as a hand on his own chest, no touching, arm's-length gap"),
    dict(to=44, speaker="iyaan", reason="action change: the drive plugged into his laptop, a light of victory on his face; he lays out the hijack plan (5.4)", chars=["iyaan"], loc="studio",
         visual="Iyaan seated at the paint-stained table in three-quarter view, the small red hard drive connected by a short cable to his open laptop, the screen turned away from the viewer so only its green glow lights his face; a light of victory in his eyes and a faint fierce smile, his face centred",
         camera="medium close-up, eye level, his face centred in the upper half, the table top with the red drive as the lower third", amb="room_day",
         sens="other", safe="the signed documents are never readable: only the screen's glow"),
    dict(to=45, speaker="raaya", transition="cut", reason="5.4 reverse shot: Raaya softly, heartbroken — 'then Bappa will have no way out'", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya sitting across the table, her hands clasped tightly on the table, speaking softly, heartbreak and resolve in her wet eyes, her face centred and sharp; Iyaan's shoulder soft in the foreground at the edge of the frame, " + COUPLE_GAP + ", the table between them",
         camera="over-the-shoulder medium close-up, eye level, her face centred in the upper half, the table as the lower third", amb="room_day"),
    dict(to=48, reuse="beat_018", transition="cut", reason="return to Iyaan at the laptop: 'their power will shatter'; hours of work on the servers", chars=["iyaan"], loc="studio",
         visual="reuse of beat_018: Iyaan at the laptop, typing", camera="medium close-up", amb="room_day"),
    # ---------------- Day 2, evening: the rally ----------------
    dict(to=52, speaker="asim", transition="black", reason="time jump and location change: the rally; Asim, Sameer and Fareed in the VIP seats; Asim whispers to Sameer (5.4)", chars=["asim", "sameer", "fareed"], loc="rally_hall",
         visual="the front VIP row of the rally hall: Asim in his white shirt seated in the middle, leaning toward Sameer to whisper into his ear with a proud smirk, Asim's face three-quarter toward the viewer, centred and sharp; Sameer beside him smiling and nodding; Fareed seated on Asim's other side, smug; rows of supporters and teal-and-white flags behind them, softly blurred",
         camera="medium shot, eye level, Asim's face centred in the upper half, the seat backs as a calm lower third", amb="hall_crowd"),
    dict(to=56, reason="time marker and opening view of the hall: 8 pm, the packed hall, Asim's giant portrait on the LED screens", chars=[], loc="rally_hall",
         visual="a wide opening view of the packed convention hall from the back: thousands of supporters, teal-and-white flags, TV cameras on tripods on the riser in the foreground, and on the two giant LED screens behind the stage a huge portrait of a heavy-set grey-moustached older man in a white shirt; no text anywhere",
         camera="very wide shot from the back riser, the stage and screens in the upper half, the dark crowd as the lower third", amb="hall_crowd",
         sens="other", safe="no slogans, logos or real party colours; the screens show only a portrait"),
    dict(to=57, reason="action change: Asim walks to the podium to thunderous applause, Sameer and Fareed smiling at his sides", chars=["asim", "sameer", "fareed"], loc="rally_hall",
         visual="Asim striding across the stage toward the podium, one hand raised to the cheering crowd, proud and powerful; Sameer and Fareed standing on either side of him smiling with pride, stage lights blazing behind them",
         camera="medium wide shot from a low angle in front of the stage, faces in the upper half, the stage edge as the lower third", amb="hall_crowd"),
    dict(to=60, speaker="iyaan", reason="location change (cross-cut) + 5.4: Iyaan in a black van nearby, ready to hijack the broadcast, asks Raaya 'ready?'", chars=["iyaan", "raaya"], loc="van",
         visual=IYAAN_SUIT + ", sitting behind the narrow fold-down table with the glowing open laptop and a small satellite-antenna box with cables, his face in the exact centre of the frame in three-quarter view, sharp, lit cold blue by the screen, turning slightly to ask a quiet question; Raaya only as a soft out-of-focus shoulder and light-grey hijab at the far right edge of the frame, " + COUPLE_GAP,
         camera="medium close-up, eye level, his face centred in the upper half, the laptop and table as the lower third", amb="car_night"),
    dict(to=61, speaker="raaya", transition="cut", reason="5.4 reverse shot: Raaya takes a deep breath — 'Yes, Iyaan. The truth has to come out.'", chars=["raaya", "iyaan"], loc="van",
         visual="Raaya sitting in the dark van, her face in the exact centre of the frame in three-quarter view, sharp, pale and tense but resolved after a deep breath, the laptop's blue glow on her face, her light-grey hijab fully covering her hair and neck; Iyaan only as a soft out-of-focus dark shoulder at the far left edge of the frame, " + COUPLE_GAP,
         camera="medium close-up, eye level, her face centred in the upper half, her hands and the table as the lower third", amb="car_night"),
    dict(to=64, speaker="asim", reason="5.4 dialogue focus and action change: Asim's speech at the podium — 'a government against corruption'", chars=["asim"], loc="rally_hall",
         visual="Asim at the podium speaking into the microphones, one hand raised in a grand oratorical gesture, a commanding, practised, deceptive smile, his face centred and sharp under the white stage lights, the giant LED screen behind him glowing softly",
         camera="medium close-up from slightly below, his face centred in the upper half, the podium as the lower third", amb="hall_crowd"),
    dict(to=65, reuse="beat_024", transition="cut", reason="cross-cut: Iyaan whispers 'Now' and presses Enter", chars=["iyaan", "raaya"], loc="van",
         visual="reuse of beat_024: the van, Iyaan at the laptop", camera="tight on Iyaan", amb="car_night"),
    dict(to=68, reason="action change: the mic dies, the giant screens go black and glow red; Asim turns; Sameer and Fareed rise", chars=["asim", "sameer", "fareed"], loc="rally_hall",
         visual="from the middle of the hall: the two giant LED screens behind the stage have gone black with a deep pulsing red glow that washes red light over the stage; Asim at the podium turned to look back over his shoulder at the screens; Sameer and Fareed half-risen from their front-row seats, staring; the crowd's heads still and silent; no letters on the screens",
         camera="wide shot from the crowd, the stage and screens in the upper half, dark heads of the crowd as the lower third", amb="hall_crowd",
         sens="other", safe="the narration's red writing is shown only as an abstract red glow (rule 17)"),
    dict(to=71, reason="location change: the control room is locked out; the bank transactions fill every screen", chars=[], loc="control_room",
         visual="two male technicians in dark polo shirts at the long mixing desks, one half-standing and typing frantically, the other with both hands on his head; every monitor in the room glows the same deep red, filled with blurred grey document-like rectangles and abstract graph lines, nothing readable",
         camera="medium wide shot from behind the desks, the glowing monitors in the upper half, the desks as the lower third", amb="server_room",
         sens="other", safe="transactions and orders shown only as blurred shapes and graph lines, no text or numbers"),
    dict(to=73, speaker="asim", reason="5.4 dialogue focus and emotion change: Asim screams 'Stop this right now!'", chars=["asim"], loc="rally_hall",
         visual="Asim at the podium shouting furiously, one arm flung out pointing toward the back of the hall, his face contorted with rage and panic, centred and sharp, the deep red glow of the screens behind him",
         camera="medium close-up, eye level, his face centred in the upper half, the podium as the lower third", amb="hall_crowd"),
    dict(to=75, speaker="asim", reason="5.4 focus on the speaker of the recording: Asim's own voice plays the murder order; he freezes", chars=["asim"], loc="rally_hall",
         visual="Asim frozen at the podium, his face draining pale with horror, mouth slightly open, centred and sharp; behind him a giant jagged white audio waveform glows across the black LED screen",
         camera="medium close-up, eye level, his face centred in the upper half, the podium as the lower third", amb="hall_crowd",
         sens="other", safe="the recorded order is only heard: an abstract waveform on the screen, no text"),
    dict(to=77, reason="action change: the crowd erupts; Fareed sinks into his chair; Sameer signals his guards", chars=["fareed", "sameer"], loc="rally_hall",
         visual="the front row in uproar: Fareed slumped back in his seat, grey with fear, staring at nothing; Sameer half-standing beside him, signalling urgently with a raised hand to a security man in a black suit with an earpiece; behind them supporters on their feet, pointing and shouting; red screen light over everything",
         camera="medium shot, eye level, faces in the upper half, the seat backs as the lower third", amb="hall_crowd",
         sens="other", safe="anger only as standing, pointing and raised voices; nothing thrown (rule 16); the security man carries nothing"),
    dict(to=79, reason="character enters: Iyaan in a black suit strides in through the main doors, Raaya behind him with a big file; cameras swing to them", chars=["iyaan", "raaya"], loc="rally_hall",
         visual=IYAAN_SUIT + ", striding down the centre aisle from the tall open main doors, his face fierce and determined; Raaya walking a few steps behind him carrying a thick plain closed folder against her chest; TV camera operators on the riser swinging their tripod cameras toward them; " + COUPLE_GAP,
         camera="medium wide shot from the aisle ahead of them, faces in the upper half, the aisle floor as the lower third", amb="hall_crowd"),
    dict(to=81, speaker="raaya", reason="5.4 dialogue focus: Raaya steps forward — 'Stay back! This is evidence I brought!'", chars=["raaya", "iyaan"], loc="rally_hall",
         visual="on the stage steps: Raaya stepping forward with her palm raised and the closed folder in her other arm, shouting, her face centred and sharp, fierce and tearful; two security men in black suits in front of her stepping back with open raised palms; Iyaan a step behind her wearing a black suit jacket with lapels and long sleeves over a plain black crew-neck top and black trousers (NOT a t-shirt), " + COUPLE_GAP,
         camera="medium shot from a low angle, her face centred in the upper half, the stage steps as the lower third", amb="hall_crowd",
         sens="other", safe="no grabbing or scuffle: the guards step back with open palms; nothing in their hands"),
    dict(to=82, speaker="asim", transition="cut", reason="5.4 dialogue focus: face to face, Asim gasps 'aren't you…?'", chars=["asim", "iyaan"], loc="rally_hall",
         visual="over Iyaan's shoulder (his back and shoulder soft in the foreground): Asim at the podium face to face with him, eyes wide with disbelief, mouth open, centred and sharp, stage light harsh on his face",
         camera="over-the-shoulder medium close-up, eye level, Asim's face centred in the upper half", amb="hall_crowd"),
    dict(to=85, speaker="iyaan", transition="cut", reason="5.4 reverse shot: Iyaan at the microphones tells the nation 'I am Ahmed Zahir's son'", chars=["iyaan", "asim"], loc="rally_hall",
         visual=IYAAN_SUIT + ", standing at the podium leaning toward the microphones, speaking to the whole nation, his face centred and sharp, calm and fierce, eyes blazing; Asim pale and soft at the side behind him; the red-glowing screen far behind",
         camera="medium close-up from slightly below, his face centred in the upper half, the podium as the lower third", amb="hall_crowd"),
    dict(to=88, speaker="raaya", reason="action change and 5.4 focus: Asim lunges; Raaya steps in front of her father — 'Bappa, you are a killer!'", chars=["raaya", "asim", "iyaan"], loc="rally_hall",
         visual="Asim seen from behind, only his grey-streaked hair, white shirt shoulder and one half-raised hand soft in the bottom-right corner, frozen mid-step: Raaya standing in the exact centre of the frame (her face at the horizontal middle of the image), facing her father and the viewer, both palms raised toward him, tears streaming, crying out, her face centred and sharp; Iyaan behind her at the left wearing a black suit jacket with lapels and long sleeves over a plain black crew-neck top and black trousers (NOT a t-shirt), " + COUPLE_GAP,
         camera="over-the-shoulder medium close-up, eye level, Raaya's face centred in the upper half", amb="hall_crowd",
         sens="violence", safe="Asim's attempt to lay hands on Iyaan is only a half-raised hand frozen mid-step; no contact between the men"),
    dict(to=89, reason="strong emotional turning point: Asim's world shatters before his daughter", chars=["asim"], loc="rally_hall",
         visual="close-up of Asim crushed and hollow, shoulders sagging, his wet eyes empty, all his power drained from his face, the harsh white stage light and the red glow behind him",
         camera="close-up, eye level, his face in the upper half, his white shirt below", amb="hall_crowd"),
    dict(to=90, reason="action change, episode end: the doors burst open and a large police force runs toward the stage", chars=[], loc="rally_hall",
         visual="wide shot from the stage toward the back of the hall: the tall main doors flung wide open and a large group of Maldivian police officers in dark-navy uniforms and caps running down the aisles toward the stage, hands empty, NO weapons, NO shields, NO handcuffs; the crowd turning to stare",
         camera="very wide shot from the stage, the doors and running officers in the upper half, the crowd as the lower third", amb="hall_crowd",
         sens="other", safe="police without weapons or handcuffs; no arrest shown"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Raaya left the art studio having made the biggest decision she had ever made in her life. Her heart was wounded.",
   [("footsteps_pavement", "ނުކުމެގެން", -22)])
sh(2, "Her eyes were full of tears. After learning the truth of her father's dark past, she saw helping Iyaan as a duty she owed to her own self.",
   [("sob_breath", "ކަރުނައިން", -24)], hum=True)
sh(3, "When Raaya went home and stepped inside, the house lay in an unusually deep silence. Her father Asim was out.",
   [("door_open", "ވަތްއިރު", -20)])
sh(4, "He was busy planning, together with Sameer and Fareed, the final steps to end Iyaan's days. Raaya seized the opportunity.")
sh(5, "She went into her father's office room. Just as Iyaan had told her, she opened the secret compartment of the bookshelf behind the big desk there.",
   [("creak", "ހުޅުވި", -20)])
sh(6, "Iyaan had found out that a backup hard drive was kept there. As he had instructed, Raaya moved the books aside and pressed the secret button there.",
   [("box_unlock", "އޮބައިލި", -20)])
sh(7, "A part of the shelf slid slightly open. Inside it she saw a red hard drive. It was the original backup of Asim's entire political life, his black-money network and every document of Zahir's murder.",
   [("creak", "ހުޅުވުނު", -20)], hum=True)
sh(8, "Raaya quickly took the hard drive and put it in her bag. At that same moment, near Iyaan's small apartment in Henveyru,",
   [("cloth_rustle", "ދަބަހަށް", -22)])
sh(9, "two black motorbikes came to a stop. Four men with their faces covered got off the bikes. In their hands were sharp weapons and iron bars.",
   [("motorbike_pass", "ސައިކަލު", -16)], hum=True)
sh(10, "They were gangsters sent by Asim and Sameer. Their order was that Iyaan must not leave that place alive. Iyaan was sitting in his room in front of the computer.")
sh(11, "Through the headset on his ear he heard the alert from the secret cameras he had fixed on the street outside the house.",
   [("alarm_beep", "އެލާޓް", -20)])
sh(12, "The screen showed the gangsters climbing up the stairs. There was no trace of fear on Iyaan's face.")
sh(13, "For the past fifteen years his body and mind had been prepared for situations just like this. \"Did you lot think you could achieve anything?\"",
   speaker="iyaan")
sh(14, "Iyaan said softly. Iyaan stood up and switched off the room's lights. Darkness took over the whole room.",
   [("flashlight_click", "ނިވައިލި", -18)])
sh(15, "He took up a pair of night-vision goggles and a special electric baton. He unlocked his room door, and stood behind the door like a shadow.",
   [("lock_click", "ހުޅުވާލި", -20)])
sh(16, "Then came the sound of the lock on the house's outer door being broken and the door opening. The gangsters forced their way into the apartment. They",
   [("soft_thud", "ހަލާކުކޮށްލައި", -22), ("door_open", "ހުޅުވި", -20)], hum=True)
sh(17, "crept toward Iyaan's room. The first man opened the room door and took a step inside.",
   [("creak", "ހުޅުވާލައި", -20)])
sh(18, "In that second, Iyaan came out of the darkness, seized the iron bar in that man's hand and twisted it.",
   [("soft_thud", "އަނބުރާލި", -22)])
sh(19, "With a sound like an arm snapping, the man fell. The second man swung a machete, but Iyaan leapt up and with a martial-arts move struck him in the chest with the electric baton.",
   [("soft_thud", "ވެއްޓުނު", -24), ("soft_thud", "ޖެހި", -22)])
sh(20, "With the electric shock, the second man too fell unconscious. The remaining two, backing away in fear, threw an iron bar into the room.",
   [("soft_thud", "ވެއްޓުނު", -24)])
sh(21, "It struck the wall. They threw a second iron bar as well. It didn't hit Iyaan either. Iyaan pressed a remote in his pocket.",
   [("soft_thud", "ޖެހުނީ", -22), ("computer_beep", "ފިތާލި", -20)])
sh(22, "With that, an audio began to play loudly from the speakers on the room's walls. It was the audio of Asim ordering Iyaan's father killed.",
   hum=True)
sh(23, "The killers were startled. What they were hearing was their boss's voice. \"What is this?\" one of them asked loudly.",
   [("gasp", "ސިހިގެން", -22)], speaker="intruder")
sh(24, "\"This is the end of your master,\" Iyaan's voice came out of the darkness.",
   speaker="iyaan", hum=True)
sh(25, "Iyaan came from behind and struck the two men on the head with something heavy, knocking them down. Four men lay in a row, unconscious.",
   [("soft_thud", "ޖަހައި", -22)])
sh(26, "Iyaan switched the room's lights on. Strong determination showed on his face. He picked up his phone and called Raaya. \"Raaya, did you get the hard drive?\"",
   [("flashlight_click", "ދިއްލާލި", -18), ("phone_buzz", "ގުޅި", -22)], speaker="iyaan")
sh(27, "\"Yes, Iyaan. I have it in my hand. I'm heading to the studio now,\" Raaya said. \"Very good.",
   speaker="raaya")
sh(28, "Tomorrow night is the night of the campaign rally. In the middle of that rally, in front of the whole nation, we'll release all of this evidence.",
   speaker="iyaan")
sh(29, "Tomorrow night the whole country will see the killers' end,\" Iyaan said. After hanging up the phone, Iyaan looked over at the gangsters.",
   speaker="iyaan", hum=True)
sh(30, "The morning of the following day. After the events of the night, Iyaan had tied up the unconscious gangsters securely and sat them in a corner of the room.")
sh(31, "He took their phones and looked through the messages sent to Home Minister Asim's number. Asim would be thinking that Iyaan was dead by now.")
sh(32, "From their phones Iyaan had sent Asim a message saying the job was done.",
   [("computer_beep", "ފޮނުވާފަ", -22)])
sh(33, "Iyaan put his laptop and important things in a bag, slipped out secretly through the back door of the house, and set off for the art studio to meet Raaya.",
   [("door_close", "ދޮރުން", -22)])
sh(34, "As he went along the road, on Malé's big streets he saw banners and flags for Asim's big political rally being put up.")
sh(35, "That was the biggest campaign rally of Asim's party, to be held tonight. The media would broadcast it live. When Iyaan opened the studio door and went in, Raaya was sitting by a table.",
   [("door_open", "ހުޅުވާލާފައި", -20)])
sh(36, "In front of her lay the backup hard drive taken from her father's office room. Worry showed in Raaya's eyes.")
sh(37, "\"Iyaan, I found it. All of Bappa's secrets are in here. I looked at some of the files — I couldn't even believe my own father's",
   speaker="raaya", hum=True)
sh(38, "bitter truth.\" Raaya stood up, came over and said it. Iyaan laid his hand on Raaya's shoulder. \"Raaya,",
   speaker="raaya")
sh(39, "what you did was a very brave thing. This isn't only about getting justice for my father.",
   speaker="iyaan")
sh(40, "This is revealing the truth to the people of this country.\" Iyaan connected the hard drive to his laptop.",
   [("computer_beep", "ގުޅާލި", -20)], speaker="iyaan")
sh(41, "As he opened the files inside it, a light of victory spread across Iyaan's face.")
sh(42, "In it were the original signed documents of all the crimes committed together since 2011 by Speaker of Parliament Sameer, bank MD Fareed and Asim.")
sh(43, "There was also the evidence of the plan they made to kill Iyaan's father, Ahmed Zahir. \"Tonight, once the rally begins, the moment he steps up to the podium and starts to speak is the moment we strike.",
   speaker="iyaan", hum=True)
sh(44, "What I'm making now is a special signal-hijack program. We'll hack the feeds of every TV channel broadcasting that rally, all at once.",
   speaker="iyaan")
sh(45, "And we'll put these files and audios out live on the rally hall's big screens.\" \"Then Bappa will have no way left to save himself,\"",
   speaker="raaya", hum=True)
sh(46, "Raaya said softly. Her voice was full of heartache. \"Yes, the truth will come out in front of the whole nation.",
   speaker="iyaan")
sh(47, "Their political power will shatter into pieces in that second,\" Iyaan said. His fingers began moving swiftly over the keyboard.",
   [("keyboard_typing", "ކީބޯޑު", -18)], speaker="iyaan")
sh(48, "He went on preparing the servers needed for tonight's big hack. Many hours passed in this work.",
   [("keyboard_typing", "ތައްޔާރުކުރަމުން", -22)])
sh(49, "The sun set, and people began gathering at the ground where the big rally was being held. Asim, Sameer and Fareed sat in the rally's VIP seats.")
sh(50, "Asim's face showed extreme pride. He believed that the biggest obstacle in his path, Iyaan, had been wiped out in last night's attack.")
sh(51, "\"It's all over — the story of Zahir's son is finished now,\" Asim said secretly into Sameer's ear.",
   speaker="asim")
sh(52, "Sameer smiled and nodded. But what they did not know was that Iyaan's virus had already got into the systems of the main control room of the hall they sat in, and lay ready.")
sh(53, "The hands of the clock moved on toward the final seconds of revenge. The clock struck eight at night.",
   hum=True)
sh(54, "The inner hall of the Maafannu youth centre was packed to bursting, filled with people and political flags.")
sh(55, "On the giant LED screen behind the rally hall's big stage was a huge photo of Home Minister Asim.")
sh(56, "He had all but secured the party's presidential ticket. There was no one inside the party who could compete with him.")
sh(57, "As he began walking toward the podium, the whole hall thundered with applause. On either side of Asim stood Speaker of Parliament Sameer and bank MD Fareed, smiling with pride.",
   [("applause", "އަތްތިލަބަޑީގެ", -14)])
sh(58, "At that moment, not far from the convention centre, Iyaan sat in front of his laptop inside a black van.")
sh(59, "Beside him sat Raaya, cold and anxious. Using a high-power satellite antenna inside the van, Iyaan was ready to hijack the rally hall's main broadcast signal and the TV channels' live feeds.")
sh(60, "\"Raaya... ready?\" Iyaan asked. Raaya took a deep breath and nodded. \"Yes, Iyaan.",
   [("breath", "ނޭވާއެއް", -22)], speaker="iyaan")
sh(61, "The truth has to come out.\" On the stage, Asim began to speak.",
   speaker="raaya")
sh(62, "His voice carried authority and the skill of deception. \"This government of ours is",
   speaker="asim")
sh(63, "a government that will work for the rights of the people, against corruption! Guaranteeing the nation's safety and security is our greatest promise...",
   speaker="asim")
sh(64, "I am standing for this government's second term with the pledge to fulfil this and bring happiness to the people.\"",
   speaker="asim")
sh(65, "\"Now,\" Iyaan said softly. His finger pressed the laptop's Enter key.",
   [("computer_beep", "ފިތާލި", -18)], speaker="iyaan", hum=True)
sh(66, "Suddenly a loud noise burst from the rally hall's main speakers. The sound from Asim's microphone cut out.",
   [("power_down", "ކެނޑުނު", -16)])
sh(67, "In that very second the big LED screen behind the stage suddenly went black, and huge red writing appeared: the secret of a fifteen-year-old murder.",
   hum=True)
sh(68, "Astonishment and silence took over the whole hall. Asim broke off his speech and looked behind him. Sameer and Fareed rose from their chairs.",
   [("crowd_gasp", "ހައިރާންކަމާއި", -18)])
sh(69, "The control-room staff tried to restart the systems, but Iyaan's virus had locked down the entire control room.",
   [("keyboard_typing", "ރީސްޓާޓްކުރަން", -22), ("alarm_beep", "ބްލޮކްކޮށްފަ", -22)])
sh(70, "It wasn't only the hall's screen. The scene appeared on the screens of people all over the country watching live on TV.")
sh(71, "Next the screen showed bank transactions from 2011 — the documents of the million rufiyaa sent from Fareed's bank to the account of the killers who murdered Zahir.")
sh(72, "And beneath them appeared the secret orders Sameer had signed to cover up the case. \"What kind of joke is this?\"",
   speaker="asim")
sh(73, "\"Stop this right now!\" Asim screamed from the stage. But the sound that came next from the speakers froze the whole hall.",
   speaker="asim", hum=True)
sh(74, "It was Asim's own voice. \"Zahir has started talking far too much... his mouth —",
   [("heartbeat", "ޢާޞިމްގެ", -20)], speaker="asim", hum=True)
sh(75, "shut it for good. Make tonight his last night in this world...\"",
   speaker="asim", hum=True)
sh(76, "The voices of the ordinary people in the hall began to rise. Asim panicked and began to tremble. Fareed sank into his chair in fear.",
   [("crowd_roar", "ގަދަވާން", -16), ("soft_thud", "ވެއްޓުނު", -24)])
sh(77, "Sameer signalled to his guards that he wanted to get out. At that moment a new video feed came up on the screen.")
sh(78, "It was Iyaan, coming in through the main door of the rally hall. He was wearing a black suit. A fearsome, powerful determination showed on his face.",
   [("door_open", "ދޮރުން", -18)], hum=True)
sh(79, "Walking behind him came Asim's own daughter, Raaya. In Raaya's hands was a big file. The media cameras swung at once toward Iyaan and Raaya.",
   [("camera_shutter", "ކެމެރާތައް", -18)])
sh(80, "Iyaan walked up onto the stage. The security guards tried to stop Iyaan. But Raaya stepped forward and said loudly, \"Stay back!",
   speaker="raaya")
sh(81, "This is evidence I brought!\" Because Raaya was the minister's own daughter, the guards didn't know what to do and stepped back.",
   speaker="raaya")
sh(82, "Iyaan stopped right in front of Asim. Asim's eyes went wide. \"You... you... aren't you dead?\"",
   [("gasp", "ބޮޑުވި", -22)], speaker="asim")
sh(83, "Asim asked slowly. Iyaan leaned toward the podium's microphone. His voice was heard by the whole country. \"Asim...",
   speaker="iyaan")
sh(84, "the killers you sent are locked up in my house. Did you think that fifteen years ago, by murdering Ahmed Zahir, you were safe?",
   speaker="iyaan")
sh(85, "I am that Ahmed Zahir's son — Iyaan Ahmed Zahir. Today, in front of this nation, the crimes of you three stand exposed.\"",
   [("crowd_gasp", "ދަރިފުޅު", -18)], speaker="iyaan", hum=True)
sh(86, "Asim, in a rage, tried to lay his hands on Iyaan. But Raaya stepped in front of her father. \"Bappa...",
   [("crowd_gasp", "ހުއްޓުނު", -20)], speaker="raaya")
sh(87, "stop! I brought out all of Bappa's evidence myself. Bappa, you are",
   speaker="raaya", hum=True)
sh(88, "a killer!\" Raaya said, weeping. Hearing those words from his own child's lips, Asim's whole world shattered to pieces.",
   [("sob_breath", "ރޮމުން", -20)], speaker="raaya", hum=True)
sh(89, "All his power, all his political influence seemed lost in that one second. Before his beloved child, that tyrant could not find the courage to fight on.",
   hum=True)
sh(90, "That was the moment every door of the rally hall burst open and a large force of police rushed inside. They ran straight toward the stage. To be continued.",
   [("door_slam", "ހުޅުވި", -14), ("crowd_panic", "ވަދެގަތް", -18), ("footsteps_pavement", "ދުވެފައި", -16)], hum=True)
# spec 5.4: crop + focus [x%, y%] for every dialogue shot, read off work/grid/*.jpg (x = face centre, y = face + ~8)
T = "tight"; M = "medium"
FOCUS = {
    13: (T, [50, 35]),                                          # beat_005 Iyaan at his monitors
    23: (T, [56, 38]),                                          # beat_008 centred faceless intruder
    24: (T, [50, 38]),                                          # beat_009 Iyaan in the dark
    26: (T, [52, 35]), 28: (M, [52, 42]), 29: (T, [52, 35]),    # beat_010 / 012 Iyaan on the phone
    27: (T, [50, 35]),                                          # beat_011 Raaya on the phone
    37: (T, [45, 35]), 38: (M, [45, 42]),                       # beat_016 Raaya
    39: (T, [40, 35]), 40: (M, [40, 42]),                       # beat_017 Iyaan, hand on chest
    43: (T, [55, 35]), 44: (M, [55, 42]),                       # beat_018 Iyaan at the laptop
    45: (T, [42, 36]),                                          # beat_019 Raaya
    46: (M, [55, 42]), 47: (T, [55, 35]),                       # beat_020 (reuse 018) Iyaan
    51: (T, [55, 46]),                                          # beat_021 Asim whispering
    60: (T, [42, 35]),                                          # beat_024 Iyaan in the van
    61: (T, [52, 35]),                                          # beat_025 Raaya in the van
    62: (T, [47, 35]), 63: (M, [47, 42]), 64: (T, [47, 35]),    # beat_026 Asim's speech
    65: (T, [42, 35]),                                          # beat_027 (reuse 024) Iyaan 'Now'
    72: (M, [42, 42]), 73: (T, [42, 35]),                       # beat_030 Asim shouting
    74: (T, [50, 35]), 75: (T, [50, 36]),                       # beat_031 Asim frozen at his own voice
    80: (T, [45, 35]), 81: (M, [45, 42]),                       # beat_034 Raaya 'Stay back!'
    82: (T, [37, 35]),                                          # beat_035 Asim 'aren't you…'
    83: (T, [48, 35]), 84: (M, [48, 42]), 85: (T, [48, 35]),    # beat_036 Iyaan at the microphones
    86: (T, [52, 35]), 87: (M, [52, 42]), 88: (T, [52, 35]),    # beat_037 Raaya 'Bappa, you are a killer!'
}
for i, (c, f) in FOCUS.items():
    assert S[i][2].get("speaker"), i
    S[i][2].update(crop=c, focus=f)
assert all(i in FOCUS for i in S if S[i][2].get("speaker")), [i for i in S if S[i][2].get("speaker") and i not in FOCUS]
SHOTS = S

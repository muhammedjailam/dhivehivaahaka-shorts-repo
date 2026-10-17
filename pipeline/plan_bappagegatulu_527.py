"""Beat/shot plan for Bappage Gatulu episode 527 v2 (re-cut on the new audio; v1 plan in output/BappageGatulu/v1/plans/).
PRESENT timeline only: the 2 am hacking night, the visit to Raaya's house next afternoon, and the evening back home.
v1="beat_###" = image copied from the v1 render; NEW beats = spec 5.4 speaker framing (shot / reverse shot)."""

SHIRT = ("Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt "
         "of the reference (reference used for his face only)")
RAAYA_DRESS = ("Raaya in her white long-sleeved loose ankle-length dress and light-grey hijab fully covering her hair "
               "and neck")

ROOM = ("Iyaan's small locked bedroom-workroom in a modest Hulhumalé apartment: a desk with three computer monitors "
        "and a keyboard, scattered small electronic parts, microchips and a little card-reader gadget on the desk, a "
        "wall-sized investigation board covered with small faceless blurred photos linked by red string, a narrow "
        "single bed against the side wall, a window with closed blinds")
SITTING = ("the vast luxurious sitting room of Home Minister Asim's mansion in Malé: polished white marble floors, "
           "expensive cream leather sofas, a low glass coffee table, large abstract paintings in gold frames, tall "
           "windows with sheer curtains, a glass door to a balcony, a tall glass display shelf, and in one corner a "
           "small glass-walled network room")

LOC = {
    "room_night": ROOM,
    "room_dawn": ROOM,
    "room_day": ROOM,
    "room_evening": ROOM,
    "gate": ("the high white outer boundary wall and heavy black steel gate of Home Minister Asim's huge fortified "
             "castle-like mansion in Malé, small CCTV cameras on the wall corners, a short paved driveway and "
             "tropical palms behind the wall"),
    "sitting": SITTING,
    "netroom": ("inside a small glass-walled network room in the corner of the mansion's marble sitting room: a "
                "table with a main router and a network box with blinking status lights, tall black server racks "
                "with tidy cables beside it, the luxurious sitting room visible through the glass"),
    "street": ("a clean quiet residential street in Malé running alongside the mansion's high white boundary wall, "
               "palm trees, a few parked cars, low sun"),
    "feed": ("Asim's luxurious white-marble sitting room in the evening, seen from a high ceiling-corner "
             "security-camera angle looking down"),
    "feed_zoom": ("Asim's luxurious white-marble sitting room in the evening, cream leather sofas and warm lamps, seen "
                  "through a zoomed-in security camera mounted high on the wall, slightly high angle"),
}
MOOD = {
    "room_night": "present day, 2 am, deep night, the room dark except for the cold blue-teal glow of the monitors on his face and small red LED accents, silent, focused and intense",
    "room_dawn": "present day, just before dawn, monitors dimmed, the first pale grey-blue light seeping through the blinds, deep shadows, exhausted but resolved",
    "room_day": "present day, the next afternoon, warm daylight through half-open blinds striping the room, monitors dark, quiet anticipation",
    "room_evening": "present day, evening turning to night, the room dark except for the laptop and monitor glow, cold teal light with deep crimson accents, tense and secretive",
    "gate": "present day, bright afternoon sunlight, hard short shadows, watchful tension",
    "sitting": "present day, afternoon, soft bright daylight through tall windows, the cold opulent sheen of marble, a polite surface over hidden tension",
    "netroom": "present day, afternoon, dimmer inside the glass room, cool blue and green status lights, stealthy and tense",
    "street": "present day, late afternoon, low golden sun and long shadows, quiet determination",
    "feed": "present day, evening, warm lamps and cold shadows, slightly grainy security-camera look, ominous",
    "feed_zoom": "present day, evening, warm lamps and cold shadows, slightly grainy zoomed security-camera look, ominous and conspiratorial",
}

BEATS = [
    # ---------------- 2 am: the hacking night
    dict(to=2, v1="beat_001", reason="episode opening: 2 am, Iyaan alone at his computers in his locked room", chars=["iyaan"], loc="room_night",
         visual="Iyaan seated at his desk late at night, leaning towards three glowing monitors that show only abstract scrolling code lines and soft graphs, his face lit cold blue-teal, eyes narrowed in concentration, fingers moving fast over the keyboard; small electronic parts, microchips and a little card-reader gadget scattered on the desk; the investigation board with red string dim in the background",
         camera="medium shot from the side and slightly in front, eye level; the dark desk top as a calm lower third", amb="hacker_room"),
    dict(to=6, v1="beat_002", reason="action change: he cracks the encrypted code of Raaya's copied security card", chars=["iyaan"], loc="room_night",
         visual="close detail: a small plain white electronic key card slotted into a little card-reader gadget wired to the keyboard, a monitor behind it pulsing with abstract glowing blue code blocks and a padlock-shaped glow turning green; Iyaan's intent face leaning in at the top of the frame, lit from below by the screen",
         camera="close-up over the desk, low angle, face in the upper third, the desk surface as a calm lower third", amb="hacker_room"),
    dict(to=9, v1="beat_003", reason="action change: he hacks the CCTV around Asim's house and maps the camera blind spots", chars=["iyaan"], loc="room_night",
         visual="over Iyaan's shoulder: the monitors now show grainy live security-camera views of a mansion's high white wall and black gate at night with two tiny suited guard figures standing at the gate, and a glowing teal digital map of the house outline with small camera cones and shaded blind-spot zones marked in red; Iyaan studying them with one hand on the mouse, his profile lit by the screens",
         camera="over-the-shoulder medium shot, the screens in the upper two-thirds, the dark desk as a calm lower third", amb="hacker_room"),
    dict(to=14, v1="beat_004", reason="action change: a message from his telecom source; he starts building the camera-loop software", chars=["iyaan"], loc="room_night",
         visual="Iyaan holding his glowing smartphone in one hand, its screen tilted away from the viewer, a faint satisfied smile on his face; his other hand already on the keyboard; one monitor behind him shows a still grainy camera view of an empty night street repeated in a looping strip of identical frames, another shows abstract code",
         camera="medium close-up, eye level, face in the upper third", amb="hacker_room"),
    dict(to=19, v1="beat_005", reason="emotional turning point: the biggest obstacle — the secret office door opens only with Asim's fingerprint", chars=["iyaan"], loc="room_night",
         visual="Iyaan sitting back in his chair, chin resting on his fist, deep in thought; a monitor in front of him glows with a huge enlarged swirling fingerprint pattern in luminous blue lines; on the desk under the lamp a small thin translucent silicone sheet and a pair of fine tweezers",
         camera="medium shot from slightly behind and to the side, the glowing fingerprint and his face in the upper two-thirds", amb="hacker_room"),
    dict(to=21, v1="beat_006", reason="action change: he stands at the investigation board and looks at Asim's photo", chars=["iyaan", "asim"], loc="room_night",
         visual="Iyaan standing close to the wall-sized investigation board in the dark, seen in three-quarter profile, staring with cold controlled fury at a small printed head-and-shoulders portrait photo of the grey-moustached man from the second reference pinned at the centre of the board, red string running from it to many small faceless blurred photos; the man himself is not in the room, only his small photo; monitor glow from the side",
         camera="medium shot, eye level, his face and the photo in the upper half", amb="hacker_room",
         sens="other", safe="Asim appears only as a small portrait photo on the board; no text on the board"),
    dict(to=24, v1="beat_007", reason="time change: near dawn, the work is done; the plug-in device goes into his pocket", chars=["iyaan"], loc="room_dawn",
         visual="Iyaan sitting upright on the edge of his narrow bed, fully dressed, elbows on his knees, turning a small black plug-in device with a tiny connector between his fingers and looking at it with quiet resolve; monitors dimmed behind him; pale grey-blue pre-dawn light through the blinds casting thin stripes across the wall",
         camera="medium shot, eye level, his face in the upper third, the dark floor as a calm lower third", amb="hacker_room",
         sens="other", safe="'lay down on the bed' shown as sitting upright on the edge of the bed, fully dressed"),
    # ---------------- next afternoon: the visit
    dict(to=27, v1="beat_008", reason="time jump: next afternoon, Raaya phones and invites him; he packs his tools", chars=["iyaan"], loc="room_day",
         visual="Iyaan standing by his desk in afternoon light holding his phone to his ear with a calm polite smile, while with his free hand he slips a small black device and a small plain spray canister into an open dark shoulder bag on the desk; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium shot, eye level", amb="room_day", transition="black"),
    dict(to=30, v1="beat_009", reason="scene and character change: bodyguards stop him at the mansion gate; Raaya comes out to welcome him", chars=["iyaan", "raaya"], loc="gate",
         visual="at the open black steel gate of the mansion two broad security guards in black suits with earpieces and empty hands stand eyeing Iyaan suspiciously and stepping back, while Raaya walks out from the driveway towards him with a warm welcoming smile and a small wave; Iyaan with a dark shoulder bag, smiling politely, a clear arm's-length gap between Iyaan and Raaya, no touching; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference; Raaya in her white dress and light-grey hijab fully covering her hair and neck",
         camera="medium wide shot, eye level, faces in the upper half, the paved driveway as a calm lower third", amb="mansion_day",
         sens="other", safe="the guards carry no visible weapons; no touching, arm's-length gap"),
    dict(to=31, v1="beat_010", reason="scene change: inside the marble sitting room; he takes in the luxury", chars=["iyaan", "raaya"], loc="sitting",
         visual="wide view of the opulent marble sitting room; Iyaan standing just inside, looking around at the luxury with a polite admiring smile that does not reach his cold eyes; Raaya a clear arm's-length gap away, gesturing graciously towards a cream sofa, smiling; no touching; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference; Raaya in her white dress and light-grey hijab fully covering her hair and neck",
         camera="wide shot, eye level, figures in the upper half, the gleaming marble floor as a calm lower third", amb="mansion_day",
         sens="intimacy", safe="no touching between Iyaan and Raaya; arm's-length gap"),
    dict(to=33, speaker="iyaan", reason="5.4 dialogue: Iyaan praises the house ('Wow, Raaya, your house is so perfect') — in the v1 wide image his face is tiny at the far left edge (x≈20 %); new medium close-up framed on him", chars=["iyaan"], loc="sitting",
         visual=f"medium close-up of Iyaan standing in the opulent marble sitting room, turned towards the viewer and speaking with a warm polite smile that does not reach his cold eyes, one open hand lifted slightly as if admiring the room around him; his face in three-quarter view, centred in the upper half of the frame and in sharp focus; behind him, softly out of focus, gold-framed abstract paintings, cream leather sofas and tall windows with sheer curtains; nobody else in the frame; {SHIRT}",
         camera="medium close-up, eye level, his face centred in the upper half, the softly blurred room below as a calm lower third", amb="mansion_day"),
    dict(to=34, reuse="beat_010", reason="the story returns to the wide sitting-room view: Raaya seats him and orders tea", chars=["iyaan", "raaya"], loc="sitting",
         visual="(reuse of beat_010)", amb="mansion_day"),
    dict(to=37, v1="beat_011", reason="character change: Raaya has left; Iyaan alone spots the glass-walled network room", chars=["iyaan"], loc="sitting",
         visual="Iyaan alone, seated on the edge of the cream sofa, turning his head and fixing a sharp calculating look on a small glass-walled room in the corner of the sitting room, through whose glass a router with blinking lights and tall black server racks are visible; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium shot from behind his shoulder towards the glass room, eye level", amb="mansion_day"),
    dict(to=39, v1="beat_012", reason="action and location change: he slips into the glass room and plugs the device into the router", chars=["iyaan"], loc="netroom",
         visual="Iyaan crouched behind a router on a table inside the glass network room, reaching to its back panel and plugging a small black device into a free port, a tiny green light just glowing on the device, his face tense and focused, glancing over his shoulder; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium close-up, low angle, his face in the upper third", amb="mansion_day"),
    dict(to=42, v1="beat_013", reason="character change: Raaya returns with her paintings; tea and snacks are served", chars=["raaya", "iyaan"], loc="sitting",
         visual="Raaya standing beside the glass coffee table proudly holding up a canvas painting of a red sun rising out of a dark sea, more canvases leaning against the sofa; Iyaan seated on the sofa looking at it with a composed smile, a clear arm's-length gap between them, no touching; in the background a middle-aged household maid in a plain dark uniform dress and a black hijab fully covering her hair sets down a tray with two cups of tea and a small plate of snacks; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference; Raaya in her white dress and light-grey hijab fully covering her hair and neck",
         camera="medium wide two-shot, eye level, faces in the upper half, the coffee table as a calm lower third", amb="mansion_day",
         sens="intimacy", safe="no touching; arm's-length gap"),
    dict(to=43, v1="beat_014", reason="detail and turning point: Asim's gold signing pen on the glass shelf", chars=["iyaan", "raaya"], loc="sitting",
         visual="foreground in sharp focus: a heavy, expensive plain polished gold fountain pen lying alone on a glass display shelf, smooth and unmarked with no engraving; in the soft-focus background Iyaan on the sofa gesturing lightly towards it and Raaya laughing as she answers, a clear arm's-length gap between them, no touching; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="close-up of the pen in the upper-middle of the frame with the two figures blurred above and behind it, glass shelf reflections as a calm lower third", amb="mansion_day",
         sens="other", safe="the pen shows no name or text; no touching between Iyaan and Raaya"),
    dict(to=44, speaker="iyaan", reason="5.4 dialogue (shot): Iyaan asks 'Is it your father's?' — in the v1 pen image both are soft background figures at the frame edges (x≈23 / 75 %); new image framed on Iyaan, reused when he speaks again", chars=["iyaan"], loc="sitting",
         visual=f"medium close-up of Iyaan seated on a cream leather sofa, leaning slightly forward and speaking with a composed, charming smile, one open hand gesturing lightly to the side; a cup of tea on the glass coffee table in front of him; his face in three-quarter view towards the viewer, centred in the upper half of the frame and in sharp focus; in the soft background a tall glass display shelf and gold-framed paintings; nobody else in the frame; {SHIRT}",
         camera="medium close-up, eye level, his face centred in the upper half, the glass coffee table as a calm lower third", amb="mansion_day"),
    dict(to=45, speaker="raaya", reason="5.4 dialogue (reverse shot): Raaya laughs that the pen is Bappa's favourite — new image framed on Raaya", chars=["raaya"], loc="sitting",
         visual=f"medium close-up of Raaya standing beside a tall glass display shelf in the marble sitting room, laughing softly as she speaks, one hand lightly raised towards a plain polished gold pen lying on the glass shelf beside her, the pen smooth with no engraving or text; her face in front three-quarter view, centred in the upper half of the frame and in sharp focus; behind her, softly blurred, gold-framed abstract paintings and tall bright windows; nobody else in the frame; {RAAYA_DRESS}",
         camera="medium close-up, eye level, her face centred in the upper half, the glass shelf as a calm lower third", amb="mansion_day", transition="cut",
         sens="other", safe="the pen shows no name or text"),
    dict(to=47, speaker="raaya", reason="5.4 dialogue + action change: her phone rings — 'Iyaan, wait a moment, it's the gallery staff' — in the v1 balcony image she is tiny at the far right edge; new image framed on Raaya with her phone", chars=["raaya"], loc="sitting",
         visual=f"medium close-up of Raaya standing beside the open glass balcony door of the marble sitting room, holding her smartphone in one hand at chest height with its screen turned away from the viewer, looking towards the viewer with a gentle apologetic smile as she speaks; her face centred in the upper half of the frame and in sharp focus; behind her the bright balcony railing and the sea softly blurred; nobody else in the frame; {RAAYA_DRESS}",
         camera="medium close-up, eye level, her face centred in the upper half, the marble floor and door frame as a calm lower third", amb="mansion_day"),
    dict(to=49, v1="beat_016", reason="action change: he sprays the pen and lifts Asim's thumbprint with tape", chars=["iyaan"], loc="sitting",
         visual="close-up of Iyaan's hands at the glass shelf: one hand misting the gold pen lightly from a tiny plain spray canister, a faint pale swirling thumbprint appearing on the pen's barrel, the other hand holding a small strip of clear tape ready to lift it; Iyaan's focused face just above in the upper part of the frame, holding his breath; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference, his shirt cuffs buttoned",
         camera="close-up, eye level, hands in the middle, face at the top, the glass shelf as a calm lower third", amb="mansion_day"),
    dict(to=50, reuse="beat_015", reason="the story returns to the sofa scene (he sits back down with his tea)", chars=["raaya", "iyaan"], loc="sitting",
         visual="(reuse of beat_015)", amb="mansion_day"),
    dict(to=51, reuse="beat_019", speaker="raaya", reason="5.4 dialogue: Raaya comes back in with her phone — 'Sorry, Iyaan, I took so long'", chars=["raaya"], loc="sitting",
         visual="(reuse of beat_019)", amb="mansion_day", transition="cut"),
    dict(to=52, reuse="beat_017", speaker="iyaan", reason="5.4 dialogue (reverse shot): Iyaan answers and says he must go", chars=["iyaan"], loc="sitting",
         visual="(reuse of beat_017)", amb="mansion_day", transition="cut"),
    dict(to=55, v1="beat_018", reason="scene change: he walks away from the mansion with the stolen print and the network access", chars=["iyaan"], loc="street",
         visual="Iyaan walking away along the high white wall of the mansion in low golden late-afternoon sun, one hand in his trouser pocket, a dark shoulder bag on his shoulder, a faint cold smile and a burning look in his eyes, long shadows on the pavement; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium shot, slightly low angle, walking towards the camera, the shadowed pavement as a calm lower third", amb="city_day"),
    # ---------------- that evening, back home
    dict(to=58, v1="beat_019", reason="scene change: back in his locked room, the house's security data floods his screens", chars=["iyaan"], loc="room_evening",
         visual="Iyaan seated at his desk in the dark room, laptop open beside the monitors, which now show a grid of small grainy live security-camera views of marble interiors, corridors and a gate, plus streams of abstract data; his face lit teal, a grim satisfied focus; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium shot from behind and to the side, the screens in the upper two-thirds", amb="hacker_room"),
    dict(to=61, v1="beat_020", reason="action change: he turns the lifted print into a thin silicone fingerprint with a 3D resin printer", chars=["iyaan"], loc="room_evening",
         visual="close detail on the desk: a compact 3D resin printer glowing violet-blue as it forms a tiny thin translucent fingertip-shaped silicone layer; beside it a strip of clear tape with a faint fingerprint; Iyaan's hand holding tweezers and his concentrated face leaning in at the top of the frame; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="close-up, slightly high angle, face at the top, the desk surface as a calm lower third", amb="hacker_room"),
    dict(to=65, v1="beat_021", reason="action change: he plants the camera-loop virus in Asim's server", chars=["iyaan"], loc="room_evening",
         visual="Iyaan typing decisively, his face reflected faintly in the dark laptop screen; the monitors show a wave of green abstract code flowing into a stylised server icon and a security-camera view of an empty marble sitting room repeating in a looping filmstrip of identical frames; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="medium close-up, eye level, from the front-left of the screens", amb="hacker_room"),
    dict(to=66, v1="beat_022", reason="turning point: a loud alert — Asim has come home", chars=["iyaan"], loc="room_evening",
         visual="Iyaan leaning sharply towards the screen, eyes wide and alert, his face suddenly washed in a pulsing red alert glow from the monitor, one hand enlarging a security-camera view with the mouse; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="close-up, eye level, face in the upper third", amb="hacker_room"),
    dict(to=67, v1="beat_023", reason="character change: Asim enters his sitting room followed by his secretary with a big briefcase", chars=["asim"], loc="feed",
         visual="high-angle security-camera view of Asim walking into his marble sitting room with an uneasy, troubled frown, glancing back to speak; behind him follows his secretary, a lean middle-aged man in a grey suit with neatly combed hair, carrying a big black briefcase; slightly grainy surveillance look, no on-screen text or timestamps",
         camera="high-angle wide shot from a ceiling corner, the figures in the upper-middle, the marble floor as a calm lower third", amb="hacker_room",
         sens="other", safe="seen as a surveillance feed; the secretary (no card) described in the visual only"),
    dict(to=68, speaker="asim", reason="5.4 dialogue (shot): Asim tells his secretary 'All the evidence is now in my office' — in the v1 high-angle feed his face is small; new zoomed-in feed image framed on Asim, reused for his next line", chars=["asim"], loc="feed_zoom",
         visual="zoomed-in security-camera view of Asim standing in his marble sitting room in the evening, half-turned towards his secretary and speaking in a low tense voice, his face uneasy and troubled in front three-quarter view, centred in the upper half of the frame and in sharp focus; at the side, softly out of focus, his secretary, a lean middle-aged man in a grey suit with neatly combed hair, holding a big black briefcase; slightly grainy surveillance look, no on-screen text, no timestamps, no numbers",
         camera="medium shot from a slightly high wall-camera angle, Asim's face centred in the upper half, the marble floor as a calm lower third", amb="hacker_room",
         sens="other", safe="seen as a surveillance feed; the secretary (no card) described in the visual only"),
    dict(to=69, v1="beat_024", reason="emotional turning point: Iyaan listens through his headphones to Asim's voice from the router microphone", chars=["iyaan"], loc="room_evening",
         visual="close-up of Iyaan wearing a pair of black headphones, motionless, his face pale and still with shock in the cold teal screen light, then hardening into icy resolve, jaw clenched; a faint red glow at the edge of the frame; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="close-up, eye level, face in the upper half, dark shadow below", amb="hacker_room", transition="cut",
         sens="violence", safe="the threat to his life is carried only by his face; nothing violent shown"),
    dict(to=70, reuse="beat_030", speaker="asim", reason="5.4 dialogue (shot again): Asim says 'That journalist Iyaan ... has to be stopped'", chars=["asim"], loc="feed_zoom",
         visual="(reuse of beat_030)", amb="hacker_room", transition="cut"),
    dict(to=74, reuse="beat_031", reason="5.4 reverse shot + turning point: Iyaan's blood freezes; he vows 'tomorrow night I will go into that house'", chars=["iyaan"], loc="room_evening",
         visual="(reuse of beat_031)", amb="hacker_room", transition="cut"),
    dict(to=75, v1="beat_025", reason="closing detail: the silicone fingerprint on his palm — the plan is complete", chars=["iyaan"], loc="room_evening",
         visual="close-up of Iyaan's open palm held up in the laptop glow, a tiny thin translucent silicone fingertip layer with a faint swirling fingerprint resting on it; his determined eyes looking at it above, soft focus; the dark board with red string behind; Iyaan wears a dark charcoal long-sleeved button-up shirt and dark trousers, NOT the plain black t-shirt of the reference",
         camera="close-up, the palm in the middle and his eyes in the upper third, dark desk as a calm lower third", amb="hacker_room"),
]

T, M = "tight", "medium"
S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "It was past two in the morning. All of Malé lay in the deep silence of sleep. Iyaan was in his room. Every door was shut and locked.",
   [("lock_click", "ތަޅުލާފައި", -22)])
sh(2, "The light of the computer screen on the desk fell on his face. Beside it lay electronic parts, microchips, and the data reader of the digital card he had secretly scanned from Raaya.")
sh(3, "Iyaan's fingers moved very fast over the keyboard. The first thing he did was break the encrypted codes taken from Raaya's card.",
   [("keyboard_typing", "ކީބޯޑު", -20), ("computer_beep", "ބްރޭކު", -20)])
sh(4, "That card was the security card that opened the gate in the outer wall of Asim's house. But that card alone would not get him inside the house.")
sh(5, "The doors inside the house were fitted with biometric systems. \"Those biometric systems are things that work even offline,\"",
   speaker="iyaan", crop=T, focus=[44, 35])
sh(6, "Iyaan said, talking to himself. \"They can only be breached directly through that system's main server.\"",
   speaker="iyaan", crop=T, focus=[44, 35])
sh(7, "Iyaan hacked the network of the government CCTV cameras around Asim's house and brought the area's live feed onto his screen.",
   [("keyboard_typing", "ހެކްކޮށް", -22)])
sh(8, "Apart from the two bodyguards at the door of the house, there was no other movement. Iyaan studied very closely the angles of the high-definition cameras on the walls of the house.")
sh(9, "He marked the cameras' blind spots — the places the cameras could not see — and drew them on his own digital map.")
sh(10, "At that moment a message came to Iyaan's phone. It was from a source inside a telecom company whom he kept for gathering information secretly.",
   [("phone_buzz", "މެސެޖެއް", -18)])
sh(11, "In it were the IP addresses linking the internet connection and the security systems of Asim's house.")
sh(12, "A look of success showed on Iyaan's face. At once he began preparing special hacking software for the job.",
   [("keyboard_typing", "ތައްޔާރުކުރަން", -22)])
sh(13, "His plan was to get into the security network of Asim's house and make some of the cameras' views repeat.")
sh(14, "Then, when Iyaan went into the house, the men in the security room would see only the view of an empty street.")
sh(15, "But the biggest challenge was Asim's secret office room. That room's door opened only with Asim's own fingerprint.")
sh(16, "For that too Iyaan found an unusual solution. What he prepared was a fake fingerprint made with silicone.")
sh(17, "But before that, he needed a clean print of Asim's finger from something Asim used.")
sh(18, "His heart kept telling him that the only way to do it was to win Raaya's trust even more than before and get inside Asim's house.")
sh(19, "In the ordinary setting of their home, the print could be taken from a cup Asim touched, or something like it.")
sh(20, "Iyaan got up, went over and looked at Asim's photo on the notice board. \"However strong you think your security is,",
   [("cloth_rustle", "ތެދުވެގެން", -24)], speaker="iyaan", crop=T, focus=[40, 35])
sh(21, "I will find a gap to get into it,\" Iyaan said in his heart.",
   hum=True, speaker="iyaan", crop=T, focus=[40, 35])
sh(22, "By the time Iyaan finished his work, dawn was close. Iyaan put a secret plug-in device into his pocket.",
   [("cloth_rustle", "ޖީބަށް", -24)])
sh(23, "If this device could be connected to the router of Asim's house, the whole system would come under Iyaan's control.")
sh(24, "Iyaan lay down on his bed, preparing his heart for the great confrontation of the coming day. The shadow of his revenge had begun to fall on the walls of Asim's house.")
sh(25, "It was the afternoon of the following day. Sooner than he could have imagined, Iyaan got a golden chance. Raaya phoned him.",
   [("phone_buzz", "ގުޅި", -18)])
sh(26, "She invited him to see some of her own paintings in the sitting room of the house, and for tea. Asim had gone out at that time to an important meeting.")
sh(27, "Iyaan put the secret plug-in device, a special spray for lifting fingerprints and other things into his bag and went to Asim's house.",
   [("cloth_rustle", "ދަބަހަށް", -24)])
sh(28, "The bodyguards at the outer door stopped Iyaan. Their eyes fixed on his whole body.",
   [("footsteps_pavement", "ހުއްޓުވި", -22)])
sh(29, "But Raaya had come out just then to welcome Iyaan. When she said Iyaan was her guest, the bodyguards stepped back.")
sh(30, "Without needing to use the digital card he had secretly taken from Raaya, Iyaan went in through the first door. As he entered the house, the wealth of the place caught Iyaan's eye.",
   [("door_open", "އެތެރެވި", -20)])
sh(31, "The marble floors and the expensive furniture showed a luxury built with the people's money.")
sh(32, "Though the flames of hatred in Iyaan's heart blazed higher, he brought a smile to his face. \"Wow, Raaya.",
   speaker="iyaan", crop=M, focus=[47, 42])
sh(33, "Your house is so perfect,\" Iyaan praised. \"Thank you, Iyaan. Come this way.\"",
   speaker="iyaan", crop=T, focus=[47, 35])
sh(34, "Raaya led Iyaan over and seated him on a sofa. And she told a member of the household staff to bring tea for two.",
   crop=M, focus=[60, 42])
sh(35, "The moment Raaya went to her room was the moment for Iyaan to start his work. Iyaan looked around.")
sh(36, "A small room-like space in a corner of the sitting room caught his eye. It was walled all around with glass.")
sh(37, "Inside, on a table, stood the house's main router and network box. Next to them stood server racks too.")
sh(38, "Iyaan went over there with quick steps and quietly opened its door. He took the plug-in device out of his bag and plugged it into a free port at the back of the router.",
   [("door_open", "ހުޅުވައިލި", -22)])
sh(39, "With that, a small green light came on on the device. That meant the system in Iyaan's home now had access to the entire network of Asim's house.",
   [("computer_beep", "ދިއްލުނު", -22)])
sh(40, "Iyaan quickly came out of there and shut the door. Then he came back, sat on the sofa and composed himself. Just then Raaya came out carrying her paintings.",
   [("door_close", "ލައްޕައިލި", -22)])
sh(41, "As the two of them talked about the paintings, tea and some light snacks were set on the table.",
   [("cup_clatter", "ބެހެއްޓުނު", -20)])
sh(42, "In the middle of the conversation Iyaan's gaze stopped on an expensive pen lying on a glass shelf at the other end of the table.")
sh(43, "It was a gold pen bearing Asim's name, which he used to sign official documents. Asim had used that pen and left it there that morning.")
sh(44, "\"Raaya, that's a very beautiful pen. Is it your father's?\" Iyaan pointed. \"Yes,",
   speaker="iyaan", crop=T, focus=[49, 35])
sh(45, "it's the pen Bappa loves most. Bappa really can't stand anyone but him touching it,\"",
   speaker="raaya", crop=T, focus=[46, 35])
sh(46, "Raaya said, laughing. Just as Raaya said that, a call came to her phone. \"Iyaan, wait a moment.",
   [("phone_buzz", "ކޯލެއް", -18)], speaker="raaya", crop=M, focus=[50, 42])
sh(47, "This is someone from the gallery staff — I'll talk and come right back.\" Raaya took her phone and stepped out onto the balcony. This was the second chance.",
   speaker="raaya", crop=T, focus=[50, 35])
sh(48, "Iyaan got up at once and went over to where the pen lay. He took a special chemical spray from his pocket and lightly sprayed the top part of the pen.",
   [("cloth_rustle", "ނަގައި", -24)])
sh(49, "With that, the clear print of Asim's thumb, where he had held the pen, came into view. Iyaan pressed a small piece of tape from his pocket onto the print and very carefully peeled it away.",
   [("breath", "ފާޅުވެގެން", -24)])
sh(50, "Asim's fingerprint was now perfectly copied. After putting the pen back as it lay, Iyaan quickly sat down on the sofa and took a sip from his teacup.",
   [("cup_clatter", "ބޯލި", -22)])
sh(51, "By the time Raaya came back in, Iyaan was sitting calmly. \"Sorry, Iyaan, I took so long,\" Raaya said.",
   speaker="raaya", crop=M, focus=[50, 42])
sh(52, "\"No, no problem at all. Raaya, I have to go now. I'm so glad I got to see your paintings today.\"",
   speaker="iyaan", crop=M, focus=[49, 42])
sh(53, "Iyaan smiled. As Iyaan walked out of Asim's house, in his pocket was the key that would open the door of Asim's secret room.",
   [("footsteps_pavement", "ހިނގައިގަތް", -22)])
sh(54, "And the computer in his home was now receiving the data of the entire security system of Asim's house.")
sh(55, "The plan of revenge had now reached its most important stage. When Iyaan got home and came in, his heart was pounding as hard as it could.",
   [("door_open", "ވަތް", -22), ("heartbeat", "ތެޅުން", -20)])
sh(56, "After locking his room door, he immediately opened his laptop and ran his systems. The data sent by the small device stuck to the router in Raaya's house began flowing onto the screen.",
   [("lock_click", "ތަޅުލުމަށް", -20), ("power_up", "ހުޅުވައިލައި", -22)])
sh(57, "The entire security network of Asim's house, the live feeds of all its CCTV cameras, and the door logs were now under Iyaan's control.")
sh(58, "The very first thing Iyaan did was study the security protocols of Asim's secret office room.")
sh(59, "The biometric system on that room's door was the most modern fingerprint reader. Iyaan picked up the piece of tape lying on his desk.")
sh(60, "On it was the fingerprint taken from Asim's gold pen.")
sh(61, "Using a special 3D resin printer, he began preparing Asim's fingerprint as a thin silicone layer that could be fitted directly onto his own finger.")
sh(62, "\"How do I black out the security system?\" Iyaan asked himself.",
   speaker="iyaan", crop=T, focus=[40, 35])
sh(63, "If the whole system were shut down at once, the guards in the house's security room would know immediately. So Iyaan decided to use the camera-looping trick.")
sh(64, "He sent a special virus into the main server of Asim's house. The purpose of that virus was, at whatever moment Iyaan wanted, to replay five calm minutes of footage the cameras had recorded earlier.",
   [("keyboard_typing", "ފޮނުވައިލި", -20)])
sh(65, "Then, even while Iyaan was walking through the house, the guards' screens would show only an empty sitting room.")
sh(66, "As Iyaan sat at this work, the sound of a loud alert came from the screen. New information had entered the security log of the main door of Asim's house. Asim had come home.",
   [("alarm_beep", "އެލާޓެއްގެ", -16)])
sh(67, "Iyaan immediately enlarged the live feed of the sitting-room camera. As Asim came in, unease showed on his face.",
   [("computer_beep", "ބޮޑުކޮށްލި", -22)])
sh(68, "Behind him came his secret secretary, carrying a big briefcase. \"All the evidence is now in my office room.\"",
   speaker="asim", crop=M, focus=[45, 42])
sh(69, "Asim's words to his secretary came through clearly from the microphone of the router Iyaan had planted.",
   crop=T, focus=[49, 35])
sh(70, "\"That journalist Iyaan is trying to dig up far too much. He has to be stopped.\"",
   speaker="asim", crop=T, focus=[45, 35], hum=True)
sh(71, "The blood in Iyaan's body seemed to freeze. Did Asim know his true identity? No.",
   [("heartbeat", "ގަނޑުވި", -18)], hum=True)
sh(72, "Asim was talking about the stories of government corruption Iyaan had been writing in the newspaper. Asim still did not know who Iyaan really was.")
sh(73, "But it was clear from his words that Asim would not hesitate even to have Iyaan killed. \"Tomorrow night...\" Iyaan said slowly.",
   speaker="iyaan", crop=T, focus=[49, 35])
sh(74, "\"Tomorrow night, when Asim goes to the big political rally, is when I will go into that house.\" Watching the laptop screen, Iyaan looked at the silicone fingerprint he had placed on his palm.",
   [("breath", "ބަލާލި", -24)], speaker="iyaan", crop=M, focus=[49, 42])
sh(75, "His plans were now complete. The time had come to dive to the very depths of the sea of secrets and take hold of the true files of Bappa's murder. To be continued.",
   hum=True)
SHOTS = S

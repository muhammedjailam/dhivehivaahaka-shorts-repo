"""Beat/shot plan for Project Phenix episode 321 (used by plan_beats.py).
Inside the Kandu-huttaa bunker: corridor, lab hall, the video revealing Fairooz, the alarm, the vent shaft,
the isolation ward and Raniya's father, the self-destruct countdown, the cargo lift and the island explosion.
"""

LOC = {
    "bunker_entry": "just inside the heavy rusted steel entrance door of an underground concrete bunker on a deserted island, a short flight of concrete steps leading down into a long concrete corridor, wall-mounted fluorescent tubes, pipes along the ceiling",
    "bunker_corridor": "long concrete corridor underground, wall-mounted fluorescent tubes, cold flat light, pipes along the ceiling",
    "bunker_lab": "a large underground lab hall ringed by small glass-walled rooms with hospital beds behind frosted glass, glowing monitors, steel consoles and computer workstations in the middle of the hall, concrete pillars",
    "bunker_lab_alarm": "a large underground lab hall ringed by small frosted-glass rooms, steel consoles and computer workstations in the middle, concrete pillars, a wide steel double door at the far end, a square steel ventilation grille high in the ceiling",
    "vent_shaft": "a narrow dark square metal ventilation duct deep underground, riveted steel walls close on every side",
    "isolation_ward": "a big white underground isolation room with medical machines and monitors on steel stands, a row of tall cylindrical glass tanks glowing with murky green liquid (nothing visible inside), one hospital bed in the corner, a square ventilation grille in the white ceiling",
    "isolation_ward_alarm": "a big white underground isolation room with medical machines and monitors, tall cylindrical glass tanks glowing murky green (nothing visible inside), one hospital bed in the corner",
    "bunker_corridor_alarm": "a long concrete bunker corridor underground with pipes along the ceiling and square concrete pillars along the walls, leading to a big steel cargo lift",
    "cargo_lift": "a large bare steel freight lift inside an underground bunker, ribbed steel walls, heavy sliding steel doors",
    "east_storehouse": "an old abandoned storehouse of weathered concrete and rusty corrugated-iron roof on the east side of a deserted jungle island, its wide doorway opening onto a white sand beach and the dark sea",
    "kandu_beach_night": "Kandu-huttaa beach at night: white sand, dark calm sea, dense dark jungle of screwpine and coconut palms behind the beach",
}
MOOD = {
    "bunker_entry": "night, underground: flat cold fluorescent white light, deep cold shadows, chilling silence and fear",
    "bunker_corridor": "night, underground: flat cold fluorescent white light, steel-blue shadows, a faint chemical haze, creeping dread",
    "bunker_lab": "night, underground: cold blue-white light from overhead panels and the glow of monitors, sterile and horrifying",
    "bunker_lab_alarm": "night, underground: flashing red emergency light washing over everything in pulses, deep black shadows, panic",
    "vent_shaft": "night, inside a pitch-dark duct: only a small torch beam and the pale glow of a tablet, claustrophobic, cold",
    "isolation_ward": "night, underground: harsh clinical white light, the eerie green glow of the tanks, silent and cold",
    "isolation_ward_alarm": "night, underground: red emergency light flashing over the white room and the green tanks, urgent and frightening",
    "bunker_corridor_alarm": "night, underground: red emergency light flashing in the corridor, smoke-free deep shadows, urgent chase",
    "cargo_lift": "night, underground: red emergency light spilling in from the corridor, a weak bulb in the lift, dust trembling in the air",
    "east_storehouse": "night: cold navy-blue darkness, light rain falling in the doorway, the faint grey of the sea beyond, fresh wind",
    "kandu_beach_night": "night: cold navy-blue darkness lit by a huge distant orange glow and rising smoke beyond the trees, light rain, embers in the sky",
}

ASH = "Ashham (NOT in uniform here: a plain dark-grey long-sleeved civilian shirt and dark trousers, damp and dusty)"
RAN = "Raniya (WITHOUT her white doctor's coat: only her loose long-sleeved ankle-length dusty-blue dress, damp but fully opaque, and her navy hijab fully covering her hair and neck)"
HAB = "Habeeb (glasses, dark-grey zip jacket)"
FATHER = "Raniya's father (thin, white stubble, pale-grey patient clothes)"
LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"

BEATS = [
    # ---------------- INSIDE THE DOOR
    dict(to=4, reason="scene change: the steel door shuts behind them; first moment inside the bunker",
         chars=["ashham", "raniya", "habeeb"], loc="bunker_entry",
         visual=f"the three just inside the shut steel door at the top of the concrete steps: {RAN} standing rigid with fear, hands clasped at her chest; {ASH} a step ahead of her, crouched slightly forward, alert, staring down the long corridor with empty hands; {HAB} beside them holding a small tablet whose pale glow lights his glasses, the screen angled away from the viewer; a clear gap between Raniya and the men",
         camera=f"medium wide shot, eye level, {LOW} (bare concrete steps in shadow)", amb="bunker_machinery"),
    dict(to=7, reason="action change: Raniya leads them down the long fluorescent corridor towards the main lab",
         chars=["raniya", "ashham", "habeeb"], loc="bunker_corridor",
         visual=f"{RAN} walking ahead down the long concrete corridor, half turned back to point the way forward; {ASH} following a few steps behind her, alert, and {HAB} last, clutching his laptop bag; the corridor stretches away into cold fluorescent light, pipes along the ceiling",
         camera=f"medium wide shot from in front, slightly low, {LOW} (grey concrete floor)", amb="corridor_drip"),
    dict(to=9, reason="emotional turning point: a distant cry of pain; Raniya covers her mouth in horror",
         chars=["raniya", "ashham"], loc="bunker_corridor",
         visual=f"close-up of {RAN} stopped in the corridor, one hand pressed over her mouth, eyes wide with horror, looking towards the end of the corridor; {ASH} behind her shoulder at a respectful distance, frozen, listening",
         camera=f"medium close-up, eye level, {LOW} (soft-focus concrete wall)", amb="corridor_drip",
         sens="violence", safe="the test subject's cry is never shown; only a low breath sound and Raniya's horrified face"),
    # ---------------- LAB HALL
    dict(to=11, reason="scene change: they enter the lab hall ringed by glass rooms", loc="bunker_lab",
         visual="a wide view of the cold lab hall: a ring of small glass-walled rooms with frosted glass, behind each pane only a blurred white shape of a hospital bed under a white sheet, indistinct, and a softly glowing monitor beside it; steel consoles in the middle; three small figures seen from behind standing at the entrance of the hall; no faces of patients visible, nothing sharp behind the glass",
         camera="wide shot from behind the three at the entrance, eye level, the glass rooms in the upper two-thirds, the polished grey floor as the calm lower third",
         amb="bunker_machinery", sens="violence",
         safe="the test subjects are never shown: frosted glass with indistinct white-sheeted shapes and glowing monitors only, no faces, no tubes"),
    dict(to=14, reason="framing change: Raniya beside a frosted glass pane explains who the victims are",
         chars=["raniya", "habeeb", "ashham"], loc="bunker_lab",
         visual=f"{RAN} standing beside a tall frosted glass pane, speaking with grief and anger, one hand raised at her chest; {HAB} facing her a few steps away, eyes wide behind his glasses, shocked; {ASH} beside Habeeb, grim; behind the frosted glass only a pale blurred glow, nothing recognisable",
         camera=f"medium wide shot, eye level, {LOW} (grey floor)", amb="bunker_machinery",
         sens="violence", safe="victims stay invisible behind frosted glass"),
    dict(to=18, reason="emotional turning point: Phenix = Naail's mark; Moosa funds the lab; Ashham's fury",
         chars=["ashham"], loc="bunker_lab",
         visual=f"close-up of {ASH}, his jaw clenched and eyes burning with fury and disbelief, cold blue-white light on one side of his face, blurred frosted glass rooms behind him",
         camera=f"close-up, slightly low angle, {LOW} (dark soft-focus background)", amb="bunker_machinery"),
    dict(to=21, reason="action change: Habeeb sits at the central system, plugs in his hard drive and hacks in",
         chars=["habeeb", "ashham"], loc="bunker_lab",
         visual=f"{HAB} sitting at a steel console in the middle of the hall, a small black external hard drive plugged into the computer by a short cable, his fingers on the keyboard, tense and sweating; {ASH} standing just behind him watching the room; the monitors face away from the viewer and only glow",
         camera=f"medium shot, eye level, from the side, {LOW} (console desk top)", amb="bunker_machinery"),
    dict(to=23, reason="emotional turning point: the recording of Naail's killing plays (shown only as screen glow on faces)",
         chars=["ashham", "habeeb", "raniya"], loc="bunker_lab",
         visual=f"the three faces lit from below by the cold flickering glow of a monitor that we see only from behind: {HAB} seated, {ASH} standing behind him, {RAN} a step apart to the side; all staring at the screen in growing horror",
         camera=f"medium shot from behind the monitor, eye level, {LOW} (dark console top)", amb="bunker_machinery",
         sens="violence", safe="the video of Naail tied and killed is NEVER shown; only the screen's glow on the three horrified faces, the screen seen from behind"),
    dict(to=25, reason="reveal: the man in the black coat unmasks — Fairooz, Ashham's own boss",
         chars=["ashham"], loc="bunker_lab",
         visual=f"close-up of {ASH} frozen in shock, his face lit by a cold screen glow; beside him at a steep angle the edge of a monitor showing only a heavily blurred grey image with one tall dark standing silhouette in a long black coat, no other person and no detail on the screen",
         camera=f"close-up, eye level, {LOW} (dark console edge)", amb="bunker_machinery", hum=True,
         sens="violence", safe="the torture and killing in the video are never shown; the screen holds only a blurred dark standing figure, and Ashham's face carries the shock"),
    dict(to=27, reason="return: Raniya recoils, Ashham asks about the download", reuse="beat_008", loc="bunker_lab",
         chars=["ashham", "habeeb", "raniya"], visual="reuse of beat_008", amb="bunker_machinery"),
    # ---------------- ALARM
    dict(to=30, reason="time/light change: sirens and red emergency lights — Fairooz's men have opened the main door",
         chars=["habeeb", "raniya", "ashham"], loc="bunker_lab_alarm",
         visual=f"red emergency light floods the hall: {HAB} half-standing from the console, pointing at a monitor that glows plain red; {RAN} a few steps away crying out in fear, hands at her chest; {ASH} turning sharply towards the far steel door; deep black shadows",
         camera=f"medium wide shot, eye level, {LOW} (dark floor in red light)", amb="alarm_corridor"),
    dict(to=33, reason="action change: Ashham pockets the drive; Raniya shows the vent grille; he climbs a chair and knocks it off",
         chars=["ashham", "raniya", "habeeb"], loc="bunker_lab_alarm",
         visual=f"{ASH} standing on a steel chair under a square steel ventilation grille in the ceiling, shoving the grille loose with his elbow, dust falling; {RAN} below a few steps away pointing up at the opening — she wears NO white coat and NO lab coat, only the dusty-blue dress and navy hijab; {HAB} clutching his laptop bag, looking back towards the door; only these three people in the hall; red emergency light",
         camera=f"medium wide shot, slightly low angle, {LOW} (dark floor)", amb="alarm_corridor"),
    dict(to=35, reason="character enters: Assistant Commissioner Fairooz at the head of five armed men",
         chars=["fairooz"], loc="bunker_lab_alarm",
         visual="Fairooz in his dark-navy senior police uniform standing in the open steel double doorway of the hall, chin raised, cold triumphant sneer, his hands empty at his sides; five dark-clad men in black clothes and black face masks behind him holding only flashlights whose beams cut through the red light",
         camera=f"medium wide shot, low angle, {LOW} (polished floor reflecting red light)", amb="alarm_corridor",
         sens="violence", safe="no weapons: Fairooz's 'big gun' and the men's arms are replaced by empty hands and flashlights"),
    dict(to=37, reason="action change: Ashham takes cover behind a pillar and defies Fairooz",
         chars=["ashham"], loc="bunker_lab_alarm",
         visual=f"{ASH} pressed with his back against a square concrete pillar, shouting towards the door with fierce defiance, his empty hands flat against the concrete; flashlight beams and red light sweeping past the pillar's edge, small bright sparks bursting off the concrete corner; nobody else visible anywhere in the frame, the background behind him empty and dark",
         camera=f"medium close-up, eye level, {LOW} (dark floor)", amb="alarm_corridor",
         sens="violence", safe="the shootout is shown only as Ashham taking cover, sparks on concrete and flashlight beams; no gun"),
    dict(to=38, reason="return to Fairooz laughing and threatening", reuse="beat_013", loc="bunker_lab_alarm",
         chars=["fairooz"], visual="reuse of beat_013", amb="alarm_corridor"),
    dict(to=40, reason="character/framing change: Habeeb and Raniya already in the duct, calling Ashham up",
         chars=["habeeb", "raniya"], loc="bunker_lab_alarm",
         visual=f"looking up at the dark square opening in the ceiling: {HAB} leaning out of the vent opening head and shoulders first, one arm reaching down, shouting urgently; behind him deeper in the dark duct the face of {RAN}, frightened; red light from below on their faces",
         camera=f"low-angle shot looking straight up, the opening in the upper two-thirds, the dark ceiling as the calm lower third", amb="alarm_corridor"),
    dict(to=42, reason="action change: Ashham leaps into the duct and pulls the grille shut; sparks on the steel",
         chars=["ashham"], loc="vent_shaft",
         visual=f"inside the dark metal duct, {ASH} crouched over the closed steel grille he has just pulled shut beneath him, breathing hard; bright sparks bursting on the grille's slats from below and red light leaking up through them onto his face",
         camera=f"medium close-up, high angle, {LOW} (the dark grille)", amb="vent_shaft",
         sens="violence", safe="bullets shown only as sparks on the steel grille; nobody hurt"),
    # ---------------- DUCT
    dict(to=45, reason="action change: crawling through the narrow pitch-dark duct in single file",
         chars=["ashham", "raniya", "habeeb"], loc="vent_shaft",
         visual=f"looking down the narrow duct: {ASH} on his hands and knees in front, coming towards us, shoulders scraping the steel walls, a small torch beam; behind him {RAN} on her hands and knees, her dress and hijab fully covering her; last {HAB}, glasses glinting; a clear gap between each of them",
         camera=f"medium shot from in front, low angle inside the duct, {LOW} (dark steel floor of the duct)", amb="vent_shaft"),
    dict(to=48, reason="action change: Habeeb's tablet map shows the duct splitting — engine room or secret lab",
         chars=["habeeb", "ashham", "raniya"], loc="vent_shaft",
         visual=f"at a junction where the duct splits into two dark branches, {HAB} kneeling holding up a glowing tablet (screen showing only blurred pale lines, no text), its light on his face; {ASH} kneeling beside him looking into the two dark openings; {RAN} kneeling a little behind, frightened, trembling",
         camera=f"medium shot, eye level inside the duct, {LOW} (dark steel floor)", amb="vent_shaft"),
    dict(to=51, reason="action change: dangerous gas — Ashham tears cloth from his shirt for their mouths",
         chars=["raniya", "habeeb", "ashham"], loc="vent_shaft",
         visual=f"in the duct in a faint greenish haze, {RAN} tying a folded dark cloth over her nose and mouth, her navy hijab still fully covering her hair and neck; {HAB} tying another dark cloth over his face; {ASH} ahead, looking back at them with a torn shirt cuff, urgent",
         camera=f"medium shot, eye level, {LOW} (dark steel floor)", amb="vent_shaft"),
    # ---------------- ISOLATION WARD
    dict(to=54, reason="scene change after twenty minutes of crawling: the white isolation ward seen through the grille", loc="isolation_ward",
         visual="the big white isolation ward seen from above through the slats of a ceiling grille: medical machines with glowing monitors, a row of tall cylindrical glass tanks filled with murky glowing green liquid, cloudy and opaque, nothing visible inside, an empty hospital bed in the far corner; the room is completely empty, no people at all anywhere in the room",
         camera="high-angle shot looking down through the grille, the room in the upper two-thirds, the dark grille slats as the calm lower third",
         amb="bunker_machinery", transition="black", sens="violence",
         safe="the organs in the tanks are never shown: only murky green-glowing opaque liquid"),
    dict(to=59, reason="character enters: Raniya finds her father on the bed in the corner",
         chars=["raniya", "raniya_father", "ashham"], loc="isolation_ward",
         visual=f"{RAN}, the dark cloth pulled down from her face, at her father's bedside, weeping, one hand gently on her father's cheek; {FATHER} half-sitting against raised pillows under a white blanket, eyes half open and dull, speaking weakly; no straps, no tubes on him, a monitor beside the bed; {ASH} standing at the foot of the bed a step away, leaning in to listen",
         camera=f"medium shot, eye level, {LOW} (white blanket and floor)", amb="bunker_machinery",
         sens="violence", safe="the father's straps and tubes are not shown; he rests under a white blanket, eyes half open"),
    dict(to=62, reason="action change: Habeeb sees the self-destruct activated; red lights and siren",
         chars=["habeeb"], loc="isolation_ward_alarm",
         visual=f"{HAB} leaning over a desk monitor that glows plain pulsing red (no numbers, no text), his face lit red, eyes wide with alarm, one hand gripping the desk edge; red light flashing over the white room and the green tanks behind him",
         camera=f"medium close-up, eye level, {LOW} (desk top)", amb="alarm_corridor", hum=True),
    dict(to=65, reason="action change: Habeeb cuts the main cables, the machines die, Raniya frees her father",
         chars=["raniya", "raniya_father", "habeeb"], loc="isolation_ward_alarm",
         visual=f"{RAN} helping {FATHER} to sit up on the edge of the bed, her arm around his shoulders; beside them the monitor has gone dark; {HAB} in the background pulling thick black cables out of the back of a machine, a small spark; red emergency light",
         camera=f"medium wide shot, eye level, {LOW} (floor)", amb="alarm_corridor"),
    dict(to=69, reason="action change: Ashham carries the father and they run for the cargo lift; two guards chase",
         chars=["ashham", "raniya_father", "habeeb", "raniya"], loc="bunker_corridor_alarm",
         visual=f"{ASH} running towards us down the red-lit corridor carrying {FATHER} on his back, the father's thin arms around Ashham's shoulders, eyes half open; {HAB} running at his side and {RAN} running a little apart; far behind them at the end of the corridor two small dark silhouettes of guards with flashlight beams",
         camera=f"medium wide shot from in front, eye level, {LOW} (concrete floor)", amb="alarm_corridor",
         sens="violence", safe="the guards' gunfire shown only as distant silhouettes with flashlights"),
    dict(to=71, reason="return: Ashham behind a pillar holding them off", reuse="beat_014", loc="bunker_corridor_alarm",
         chars=["ashham"], visual="reuse of beat_014", amb="alarm_corridor",
         sens="violence", safe="the guard who falls is never shown; only Ashham behind the pillar"),
    dict(to=74, reason="scene change: inside the cargo lift as Ashham dives in and it rises; explosions below",
         chars=["habeeb", "ashham", "raniya_father", "raniya"], loc="cargo_lift",
         visual=f"inside the steel freight lift: {HAB} holding the heavy sliding door open with one arm, shouting; {ASH} lunging in through the gap; {FATHER} sitting on the lift floor against the wall, {RAN} kneeling beside her father holding his hand; dust trembling down from the ceiling",
         camera=f"medium wide shot, eye level, {LOW} (ribbed steel floor)", amb="alarm_corridor"),
    # ---------------- ESCAPE
    dict(to=76, reason="scene change: the lift opens into an old storehouse on the east shore; rain and fresh air",
         chars=["ashham", "raniya_father", "raniya", "habeeb"], loc="east_storehouse",
         visual=f"the four coming out of the dark old storehouse into the wide doorway facing the beach at night: {ASH} carrying {FATHER} on his back, {RAN} and {HAB} beside them, faces turned to the cool wind and the light rain, relief and urgency",
         camera=f"medium wide shot from outside facing the doorway, eye level, {LOW} (wet sand)", amb="rain_night"),
    dict(to=79, reason="action/spectacle: the bunker explodes underground; they are thrown onto the sand", loc="kandu_beach_night",
         visual="four small dark figures seen from behind crouched and kneeling on the white sand of the beach, shielding their heads; far behind the jungle a huge orange glow and a column of smoke and fire rising where the ground has split open, the old storehouse roof caved in at the edge of the trees, embers in the rainy sky",
         camera="wide shot from behind the figures, eye level, the glow and smoke in the upper two-thirds, the dark sand as the calm lower third",
         amb="beach_night", sens="violence",
         safe="the explosion only as distant glow and smoke; nobody hurt, nobody in the fire; they are shown crouched, not thrown"),
    dict(to=81, reason="action change: on the sand — the hard drive is safe, they survived",
         chars=["ashham", "habeeb", "raniya", "raniya_father"], loc="kandu_beach_night",
         visual=f"on the dark sand, dusty and exhausted but unhurt: {ASH} kneeling, holding a small black hard drive in his palm and looking at it; {HAB} sitting on the sand a little apart, breathing hard, glasses askew; {RAN} sitting further away hugging {FATHER} tightly and smiling through relief; orange glow behind the trees",
         camera=f"medium wide shot, eye level, {LOW} (dark sand)", amb="beach_night"),
    dict(to=83, reason="framing change: Ashham stands and looks out to sea — it's not over",
         chars=["ashham"], loc="kandu_beach_night",
         visual=f"{ASH} standing alone at the water's edge, dusty, looking out over the dark sea with grim determination, the orange glow and smoke behind him lighting the edge of his face",
         camera=f"medium shot from the side, eye level, {LOW} (dark sea and sand)", amb="beach_night", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The heavy steel door of the cave dug into the ground shut behind them with a loud bang. A cold silence took over the whole place.",
   [("metal_door", "ބެދިގެން", -16)])
sh(2, "Raniya stood with her body stiff with fear. While Ashham stood with the gun in his hand aimed forward,")
sh(3, "Habeeb took a tablet out of his laptop bag and tried to detect the signals inside. \"Sir, there's a very powerful local server in here.",
   [("cloth_rustle", "ނަގައި", -24)])
sh(4, "It's linked directly to Malé by satellite,\" Habeeb said quietly. \"But from where we are, we have no connection at all with the outside world.\"",
   [("computer_beep", "ސެޓެލައިޓުން", -24)])
sh(5, "They were in a long corridor made of concrete. The fluorescent tubes on the walls spread a dull light.")
sh(6, "The deeper they went, the stronger the chemical smell grew. It was the kind of smell that comes from hospitals. \"This way,\" Raniya said, leading the way forward.")
sh(7, "\"The main laboratory is at the end of this corridor. That's where Naail saw that horrifying sight.\" They moved forward step by step.",
   [("footsteps_pavement", "ފިޔަވަޅަކަށްފަހު", -24)])
sh(8, "Suddenly, from far away, came the sound of someone moaning. It was a cry of pain. Raniya put her hand over her mouth.",
   [("breath_heavy", "ކެކުޅުމުގެ", -24), ("gasp", "އަތްއަޅާލިއެވެ", -22)], hum=True)
sh(9, "\"That's the sound of one of the people they experiment on.\" A crime against humanity: going along the corridor, they came into a hall-like place.")
sh(10, "It was ringed by small glass-walled rooms. Inside every room stood a bed. On those beds were people connected to various tubes and machines.",
   [("computer_beep", "މެޝިންތައް", -24)])
sh(11, "Their faces had the colour of people not dead, yet without life. \"Ya Rabbi! What kind of monstrous horror is this?\" Habeeb's eyes widened.",
   [("gasp", "ބޮޑުވިއެވެ", -22)], hum=True)
sh(12, "\"Who are these people?\" \"These are foreigners who went missing from different islands. And people smuggled into the country,\"")
sh(13, "Raniya said, stepping close to a glass pane. \"And it includes foreign workers secretly brought into the Maldives too. None of them have any records.")
sh(14, "The 'Project Phenix' drug made here is first injected into the people lying in this ward.\" \"Project Phenix?\" Ashham remembered.")
sh(15, "On Naail's back was a tattoo of a phoenix bird. \"So Naail was the one who tried to expose this.\" \"Yes,")
sh(16, "when Naail saw this place he wanted to save all of these people. He copied some files,\" Raniya explained. \"But his father...")
sh(17, "Moosa Thaahir is one of the main funders of this.\" Ashham's blood boiled. While the tycoon Moosa sat in front of him crying, he was a partner in this whole crime.",
   [("heartbeat", "ކެކިގަތެވެ", -20)], hum=True)
sh(18, "Was it he himself who ordered his own son killed? Getting the data: \"Habeeb, there's the system!")
sh(19, "Get in, copy every file,\" Ashham ordered. \"This is the only chance we'll get to expose this to the whole world.\" Habeeb quickly sat down by the main systems in the middle of the hall,")
sh(20, "and connected his hard drive. Even as his hands trembled, they kept moving over the keyboard. \"Sir,",
   [("keyboard_typing", "ކީބޯޑުގައި", -20)])
sh(21, "the security here is very strong. But... I'm in,\" Habeeb said. \"There are video recordings here too.",
   [("computer_beep", "ވަދެވިއްޖެ", -20)])
sh(22, "There's even the recording of the moment Naail was killed!\" \"Play it,\" Ashham said. The screen showed what had happened in this hall a week ago.",
   [("computer_beep", "ޕްލޭ", -22)])
sh(23, "Naail sat tied to a chair. In front of him stood a man wearing a black coat. As he took off his mask, Ashham went cold.",
   [("heartbeat", "ސިއްސައިގެން", -20)], hum=True)
sh(24, "It was not Moosa Thaahir. It was one of the very top chiefs of the police's Malé Area Command, Assistant Commissioner Fairooz. He was Ashham's direct boss!",
   hum=True)
sh(25, "\"Fairooz...\" Ashham's voice cracked. \"He's the one who handed us this case. What he wanted was to send us to this island, lock us in here and kill us.\" The video showed, on Fairooz's orders, Naail being inhumanly tortured,",
   hum=True)
sh(26, "and the merciless scene of his killing. Raniya stepped back in fear and cried out. The trap: \"Habeeb, are the files downloading?\"",
   [("gasp", "ހަޅޭއްލަވައިގަތެވެ", -20)])
sh(27, "Ashham asked anxiously. \"Only 50% so far. Sir, we have no time,\" Habeeb said.")
sh(28, "Suddenly the siren at the hall's main door began to wail. Red lights came on, and a frightening sound filled the whole place.",
   [("siren", "ސައިރަން", -16), ("alarm_beep", "ދިއްލި", -20)])
sh(29, "The system showed that the bunker's main door had been opened from outside. \"They're inside!\" Raniya screamed. \"Fairooz's men are here!\"",
   [("computer_beep", "ހުޅުވައިފިކަން", -22)])
sh(30, "\"Habeeb, take the hard drive! Right now!\" Ashham said. \"But sir, it's not finished yet...\" \"No time, take it!\"")
sh(31, "Ashham took the hard drive from Habeeb's hand and put it in his pocket. \"We have to escape. Raniya, is there another way out of here?\"",
   [("cloth_rustle", "ޖީބަށްލިއެވެ", -22)])
sh(32, "\"Yes, where the pipes connected to the ventilation shaft are. But it's a very narrow way,\" Raniya said, pointing to a steel grille above.")
sh(33, "Ashham climbed onto a chair, struck the grille with the back of his gun and knocked it loose. \"Raniya, you go up first! Hurry!\" Confrontation:",
   [("metal_clang", "ނައްޓާލިއެވެ", -18)])
sh(34, "As Raniya and Zayaan squeezed into the narrow duct, the hall door opened. Five armed men came in.",
   [("door_slam", "ހުޅުވުނެވެ", -18), ("boots_march", "ފަސް", -20)])
sh(35, "At their head stood Assistant Commissioner Fairooz himself. In his hand was a big gun. \"Ashham!\" Fairooz's voice echoed through the whole hall.",
   hum=True)
sh(36, "\"Did you think you could escape from my hands? Your journey ends here.\" Ashham, taking cover behind a pillar, began to fire.",
   [("soft_thud", "ބަޑިޖަހަން", -24)])
sh(37, "\"Fairooz, you're no policeman! You're a criminal!\" Ashham shouted. Fairooz burst out laughing.")
sh(38, "\"Not even your bodies will leave this island. Like Naail, you'll be hidden here too.\" When Fairooz's men all began firing at once,",
   [("metal_clang", "ބަޑިޖަހަން", -20)])
sh(39, "Ashham got no chance to move forward. His bullets were running out. When he looked back, Habeeb and Raniya were inside the vent.")
sh(40, "\"Ashham, climb up quickly!\" Habeeb shouted from above. After sending his last bullets towards Fairooz, Ashham")
sh(41, "leapt up into the duct and shut the grille behind him. At that moment bullets struck that steel plate and sent sparks flying.",
   [("metal_clang", "ބަންދުކުރިއެވެ", -20), ("metal_clang", "ދަގަނޑުގަނޑުގައި", -16)])
sh(42, "They were stuck inside the narrow, dark shaft deep underground. They were now trapped.",
   [("breath_heavy", "ތާށިވިއެވެ", -22)])
sh(43, "The fear of the narrow shaft: inside the ventilation duct it was cold, narrow and pitch dark. As they crawled forward through the steel pipes, Ashham's shoulders scraped against the walls.",
   [("cloth_rustle", "ކޭއްތެމުން", -22)])
sh(44, "Behind him came Raniya, and last of all Habeeb. The sound of gunfire and Fairooz's shouting from outside slowly faded away.",
   [("soft_thud", "ބަޑީގެ", -24)])
sh(45, "Still, their hearts were racing to the extreme. \"Sir, I can see a map of this place,\"",
   [("heartbeat", "ތެޅުން", -20)], hum=True)
sh(46, "Habeeb said quietly, looking at something on the tablet pressed oddly against his body. \"This shaft goes ahead and splits in two.",
   [("computer_beep", "ޓެބްލެޓުން", -24)])
sh(47, "One way goes over the bunker's main engine room. The other way goes to a secret research lab.\" \"Raniya, where would your father be kept?\"")
sh(48, "Ashham asked, pulling himself forward. \"They keep the sick people in an isolation ward next to the secret lab,\" Raniya's voice trembled.")
sh(49, "\"We have to go that way.\" Ashham changed direction to the right side of the shaft. The chemical smell inside the duct kept growing stronger.",
   [("breath", "ވަސް", -22)])
sh(50, "Ashham realised that the effects of a dangerous gas were present there. After tearing off part of his shirt, he gave it to Raniya and Zayaan.",
   [("cloth_rustle", "ވީދާލުމަށްފަހު", -20)])
sh(51, "\"Tie this over your mouths. This is a dangerous chemical.\" Down into the isolation ward: after about twenty minutes of crawling,")
sh(52, "a light appeared below the duct. Ashham slowly looked down. It was a big white room. In it were various medical machines and")
sh(53, "big glass tanks. There was green liquid inside those tanks, and inside it various organs could be seen.",
   hum=True)
sh(54, "There was nobody in the room. Ashham carefully removed the steel grille and jumped down. Behind him Raniya and Habeeb came down too.",
   [("metal_clang", "ނައްޓާލުމަށްފަހު", -20), ("soft_thud", "ފުންމާލިއެވެ", -22)])
sh(55, "Raniya ran towards a bed in the corner of the room. Tied to that bed lay a man past middle age.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -22)])
sh(56, "Tubes were connected to his body. \"Baba!\" Weeping, Raniya touched her father's face. \"Baba, wake up!\"",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(57, "The man slowly opened his eyes. The colour of his eyes had gone dull. \"Daughter... save yourself... they...",
   [("breath", "ހުޅުވާލިއެވެ", -24)])
sh(58, "they will destroy everything tonight...\" \"Destroy what?\" Ashham asked, moving closer. \"Fairooz wants to blow this place up.", hum=True)
sh(59, "To bury all of us here along with all the evidence,\" he said with difficulty. \"He has boarded a launch to go to Malé.\" Running out of time: \"Sir!\"")
sh(60, "Habeeb looked anxiously at a monitor on the desk. \"The bunker's self-destruct system has been activated!",
   [("computer_beep", "މޮނިޓަރަކަށް", -20)])
sh(61, "Only 15 minutes left!\" Red lights came on throughout the bunker and the sound of a loud siren began to ring out.",
   [("alarm_beep", "ދިއްލި", -20), ("siren", "ސައިރަނެއްގެ", -16)], hum=True)
sh(62, "The system's robotic voice began to count down the time in English. \"14 minutes remaining.\" \"Ashham, what do we do?",
   [("alarm_beep", "ރިމެއިނިންގް", -20)])
sh(63, "If we take off these tubes connected to Baba's body his heart rate will drop,\" Raniya said anxiously. \"Habeeb, find the main switch of these machines.")
sh(64, "Raniya, get ready to save your Baba,\" Ashham ordered. \"We'll all go out together.\"")
sh(65, "Habeeb cut the machine's main cables. With that the machines went off. Raniya quickly undid the belts on her father's body.",
   [("electric_spark", "ބުރިކޮށްލިއެވެ", -18), ("power_down", "ނިވުނެވެ", -18)])
sh(66, "Since her father's body had no strength, Ashham lifted him onto his shoulder. \"Sir, we can't get out by the main door.")
sh(67, "It's locked,\" Habeeb said. \"But behind this lab there's a cargo lift. It goes straight up to the beach on the east side of the island.\"")
sh(68, "\"Go!\" Ashham ran, carrying Raniya's father. Confrontation: on their way towards the lift, bullets came from behind.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20), ("metal_clang", "ވަޒަންތަކެއް", -20)])
sh(69, "When Ashham turned and looked back, two guards were running after them. They wanted to kill Ashham and the others without wasting a single second. \"Habeeb!",
   [("boots_march", "ދުވަމުން", -20)])
sh(70, "Take Raniya and get into the lift!\" After handing Raniya's father to Habeeb, Ashham got behind a pillar and began to fire.",
   [("soft_thud", "ބަޑިޖަހަން", -24)])
sh(71, "With Ashham's perfect aim, the first man was hit in the chest and fell to the ground. The second man ran in fear behind a wall and hid.")
sh(72, "At that moment the system kept calling out: \"5 minutes remaining.\" \"Ashham! Come quickly!\" Habeeb shouted, holding the lift door.",
   [("alarm_beep", "ރިމެއިނިންގް", -20)])
sh(73, "Ashham leapt back and got into the lift. As the door closed, the lift began to go up. As it rose from deep underground,",
   [("metal_door", "ބެދުމާއެކު", -18)])
sh(74, "they could hear small explosions starting in the lower parts of the bunker. The whole building was shaking. Escape from the trap:",
   [("distant_boom", "ގޮވުންތައް", -18)], hum=True)
sh(75, "The lift door opened into an old storehouse on the east side of the island. As soon as they got outside, a fresh breeze hit their faces.",
   [("door_open", "ހުޅުވުނީ", -20), ("wind_gust", "ވައިރޯޅިއެއް", -22)])
sh(76, "Rain was still falling gently. As they came out of the storehouse and ran onto the beach, a powerful explosion went off deep underground.",
   [("rain_start", "ވާރޭ", -22), ("distant_boom", "ގޮވުމެއް", -14)])
sh(77, "Where the bunker was, the ground split open and smoke and flames rose up. The ground of the whole island shook.",
   [("distant_boom", "ފަޅައިގެން", -14), ("fire_crackle", "އަލިފާންގަނޑު", -20)], hum=True)
sh(78, "As the storehouse roof caved in, Ashham and the others were thrown onto the sand. Ashham raised his head and looked.",
   [("crash_clatter", "ވިއްސައިގެން", -18)])
sh(79, "The bunker was completely destroyed and had become a pit. A huge pit full of cement and rubble. Nothing could be told apart. Everything had turned to ash.")
sh(80, "Yet the hard drive in Ashham's pocket was safe. This was a big secret Fairooz would not know. \"We... we survived,\"",
   [("breath_heavy", "ސަލާމަތްވެއްޖެ", -22)])
sh(81, "Habeeb said, lying on the sand, breathing hard. Raniya sat hugging her father tightly and smiled. Ashham stood up and looked towards the sea.",
   [("sigh", "ނޭވާލަމުން", -22), ("wave_crash", "ކަނޑާ", -24)])
sh(82, "\"This is not the end yet. Fairooz must be on his way to Malé now. He'll think we died here.", hum=True)
sh(83, "We have to get to Malé first and expose this evidence.\" - To be continued -")
SHOTS = S

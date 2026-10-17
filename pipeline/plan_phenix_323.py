"""Beat/shot plan for Project Phenix episode 323 — v2 re-cut on the new audio (used by plan_beats.py)."""

LOC = {
    "police_hq_corridor": "a busy interior corridor of the Shaheed Hussain Adam Building, Malé police headquarters: polished pale floor, pale walls, glass doors leading to the press hall, uniformed police officers and journalists with TV cameras moving through",
    "police_hq_hall": "the press hall of Malé police headquarters (Shaheed Hussain Adam Building): a wooden podium with a cluster of microphones, rows of seated journalists, TV cameras on tripods with small red lights, a big wall screen behind the podium, security officers standing along the back wall",
    "police_hq_server": "the main server room on the third floor of Malé police headquarters: tall rows of black server racks with blinking blue and green lights, bundles of cables, a desk with a monitor and a laptop, a heavy grey security door with a small card reader",
    "minister_office": "the Home Minister's luxurious office in Malé: a huge dark polished desk, a tall black leather chair, heavy dark-red curtains, wood-panelled walls, a deep soft carpet, tall double doors",
    "warehouse_road": "a lonely road through an industrial area of huge dark warehouses and stacked shipping containers at the edge of Malé's reclaimed land",
    "warehouse": "a big dark empty warehouse: a high corrugated-steel roof lost in darkness, a bare concrete floor, one hanging lamp over a steel chair, a small steel tray table, a huge steel sliding door in the far wall",
    "warehouse_raid": "the same big dark warehouse with its huge steel door blown open: a bare concrete floor, one hanging lamp over a steel chair, smoke rolling in through the broken doorway",
}
MOOD = {
    "police_hq_corridor": "9 am, cool fluorescent ceiling light mixed with bright morning daylight from tall windows, busy and quietly tense",
    "police_hq_hall": "morning, bright TV lights on the podium, small red camera lights glowing, deep navy-blue shadows over the rows, tense and charged",
    "police_hq_server": "cold dim blue light from blinking server racks, the white glow of a monitor, deep navy shadows, humming and tense",
    "minister_office": "late morning, daylight shut out by heavy curtains, warm golden desk-lamp light and deep shadows, quiet and menacing",
    "warehouse_road": "late afternoon under heavy grey clouds, wet tarmac, cold muted steel-blue light, ominous",
    "warehouse": "darkness, cold navy-blue shadows, one warm yellow pool of light from the single hanging lamp, dust drifting in the beam, oppressive",
    "warehouse_raid": "darkness torn open: orange glow and grey smoke pouring through the blown-open door, white flashlight beams cutting the smoke, cold navy shadows, one warm hanging lamp",
}

LOW = "faces in the upper two-thirds, a calm dark lower third"
ASH_D = "Ashham disguised in a dark-navy police uniform with a navy police cap pulled low and dark sunglasses"
HAB_D = "Habeeb disguised in a dark-navy police uniform with a navy police cap and dark sunglasses"
HAB_S = "Habeeb in a dark-navy police uniform with a navy police cap pushed back, wearing his own thin black-rimmed glasses"
ASH_U = "Ashham bareheaded in his dark-navy long-sleeved police combat uniform (no cap, no sunglasses, short stubble)"
FAI = "Assistant Commissioner Fairooz in his senior dark-navy dress uniform, greying hair, thick greying moustache"
SAL = "Home Minister Saleem in a black three-piece suit, thick silver hair and rimless glasses"
FAH = "retired Commissioner Faahid with grey hair and a white moustache, in a black tactical jacket over his olive shirt"
NAA = "Naasir, bald with a thin goatee, in a black suit"


HAB_O = ("Habeeb in a dark-navy police jacket with a plain round shoulder patch over a white t-shirt, a navy police cap with a "
         "small plain badge, his own thin black-rimmed glasses (the same outfit as in the server-room shots)")
CUTX = "the speaker's face centred in the upper half of the frame and in sharp focus"

# v2 re-cut (new audio, 102 segments). v1="beat_###" = the v1 image file reused; NEW beats are marked "5.4" (speaker
# framing) in their reason. Shot/reverse-shot beats use transition="cut".
BEATS = [
    # ---------------- POLICE HQ: arrival in disguise
    dict(to=3, v1="beat_001", reason="episode opening: police HQ unusually busy; Ashham and Habeeb walk in disguised among officers",
         chars=["ashham", "habeeb"], loc="police_hq_corridor",
         visual=f"{ASH_D} and {HAB_D} walking side by side down the busy headquarters corridor inside a small group of uniformed police officers, heads slightly lowered, calm unreadable faces; BOTH men wear identical dark-navy long-sleeved police uniforms, navy police caps and dark sunglasses (Habeeb is NOT wearing his grey jacket or white t-shirt, and wears black police boots); further down, journalists with TV cameras and microphones crowd at the glass doors of the press hall; nobody looks at the two of them",
         camera=f"medium wide shot, eye level, {LOW} (polished floor)", amb="hall_crowd"),
    dict(to=5, v1="beat_002", reason="framing change: Habeeb speaks to Ashham through his earpiece before they split up",
         chars=["habeeb", "ashham"], loc="police_hq_corridor",
         visual=f"two-shot in a quieter bend of the corridor: {HAB_D} touching a small black wireless earpiece in his ear and murmuring with a focused look; {ASH_D} a step beside him, half-turned, glancing back over his shoulder along the corridor, serious",
         camera=f"medium close-up two-shot, eye level, {LOW}", amb="office_day"),
    dict(to=6, reason="5.4 dialogue: Ashham answers Habeeb; in the v1 two-shot he stands at the right edge (x≈75 %) and cannot be centred by a crop",
         chars=["ashham", "habeeb"], loc="police_hq_corridor", speaker="ashham", transition="cut",
         visual=f"medium close-up of {ASH_D} in a quiet bend of the corridor, centred in the frame, head turned slightly toward his partner, one finger touching a small black wireless earpiece in his ear, speaking low with a serious, warning look; at the left edge of the frame, soft and out of focus, {HAB_D} seen in three-quarter back view, listening; BOTH men wear identical dark-navy long-sleeved police uniforms, navy police caps and dark sunglasses",
         camera=f"medium close-up, eye level, Ashham's face centred in the upper half and sharp, Habeeb soft at the left edge, {LOW}", amb="office_day"),
    dict(to=9, v1="beat_003", reason="scene change: Ashham at the back wall of the press hall watching Fairooz prepare at the podium",
         chars=["ashham", "fairooz"], loc="police_hq_hall",
         visual=f"{ASH_D} leaning against the back wall of the press hall among a row of security officers, arms folded, face turned toward the front; far away across the rows of journalists, small but sharp at the podium, {FAI} calmly straightening the buttons of his uniform",
         camera=f"medium shot, Ashham in the right foreground in three-quarter profile, the podium in the distance, {LOW} (dark rows of seats)", amb="hall_crowd"),
    dict(to=10, v1="beat_004", reason="time/action change: 9 am, the red camera lights come on and the live broadcast begins",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"wide view from the back of the press hall: rows of journalists, TV cameras on tripods with glowing red lights, {FAI} at the podium leaning toward the microphones with a solemn face; the big wall screen behind him shows only a soft blue glow",
         camera=f"wide shot, eye level, the podium and screen in the upper two-thirds, {LOW} (the dark backs of the rows)", amb="hall_crowd"),
    dict(to=16, v1="beat_005", reason="framing change: close on Fairooz delivering the false statement (speaker centred by crop)",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"close-up of {FAI} at the microphones, speaking gravely with a staged sorrowful frown, one hand resting on the podium, his eyes cold; in the blurred foreground journalists lean toward each other whispering",
         camera=f"close-up, slightly low angle, {LOW} (the podium top)", amb="hall_crowd"),
    dict(to=17, reuse="beat_005", reason="back to the wide hall: the journalists whisper among themselves",
         chars=["fairooz"], loc="police_hq_hall", visual="reuse of beat_005", amb="hall_crowd"),
    dict(to=20, reuse="beat_006", reason="back to Fairooz continuing the false statement",
         chars=["fairooz"], loc="police_hq_hall", visual="reuse of beat_006", amb="hall_crowd"),
    dict(to=21, v1="beat_006", reason="focus change: Ashham's silent fury at the back of the hall",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"close-up of {ASH_D} standing with his back against the plain dark rear wall of the press hall among other officers, arms folded, no podium and no microphones near him; his jaw clenched hard, the muscles of his face tight with anger behind the dark sunglasses; far behind him, out of focus, the lit stage at the other end of the hall",
         camera=f"close-up, eye level, {LOW}", amb="hall_crowd"),
    # ---------------- SERVER ROOM
    dict(to=26, v1="beat_007", reason="scene change: Habeeb gets into the server room and connects the drive to the broadcast server",
         chars=["habeeb"], loc="police_hq_server",
         visual=f"{HAB_S} crouched at an open server rack, plugging a small black hard drive into it by a cable, a laptop open on a cart beside him with its screen angled away showing only a glowing bar; behind him the heavy security door stands ajar with a small black gadget still clipped to its card reader; a bead of sweat on his brow, intense focus",
         camera=f"medium shot, eye level, {LOW} (dark floor between the racks)", amb="command_center"),
    dict(to=27, reason="5.4 dialogue: the security guard shouts 'Hands up!'; in the v1 standoff image he is at the left edge (x≈23 %)",
         chars=["habeeb"], loc="police_hq_server", speaker="guard", transition="cut",
         visual=f"a stocky security guard in a plain dark-grey uniform shirt with plain epaulettes, short black hair and a moustache, standing in the open server-room doorway in the centre of the frame, shouting with a hard angry face, one arm stretched out pointing straight ahead, his other hand open and empty; in the left foreground, soft and out of focus, {HAB_S} seen from behind over his shoulder with both hands raised; blue blinking server racks on both sides",
         camera=f"medium shot over Habeeb's shoulder, eye level, the guard's face centred in the upper half and sharp, Habeeb soft at the edge, {LOW} (dark floor)", amb="command_center",
         sens="violence", safe="the guard's threat is shown only as a shout and a pointing empty hand; no baton or weapon"),
    dict(to=29, v1="beat_008", reason="action change: the standoff between the guard and Habeeb (the struggle is never shown)",
         chars=["habeeb"], loc="police_hq_server",
         visual=f"tense standoff across the server room: a stocky security guard in a plain dark-grey uniform standing in the open doorway, one arm pointing sharply at Habeeb, his other hand empty; {HAB_S} across the room beside the racks with both hands raised to shoulder height, eyes wide; a heavy office chair on wheels between them; the two men several metres apart",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="command_center",
         sens="violence", safe="the chair kick, the shock baton, the blows, Habeeb's bleeding face and the guard knocked out are never shown: only the standoff at a distance, with a muffled offscreen thud"),
    dict(to=30, reuse="beat_010", reason="back to Habeeb at the server: upload complete",
         chars=["habeeb"], loc="police_hq_server", visual="reuse of beat_010", amb="command_center"),
    # ---------------- THE TRUTH ON SCREEN
    dict(to=31, reuse="beat_006", reason="back to Fairooz wrapping up his statement as the screen cuts out",
         chars=["fairooz"], loc="police_hq_hall", visual="reuse of beat_006", amb="hall_crowd"),
    dict(to=35, v1="beat_010", reason="action change: the hall's big screen cuts and the bunker video plays live",
         loc="police_hq_hall",
         visual="the press hall seen from the side: the big wall screen behind the podium glowing with a dark, heavily blurred, unreadable image; the rows of journalists half-rising and turning toward it, mouths open, TV cameras swinging round; their faces lit by the cold screen glow; the figure at the podium only a small dark silhouette",
         camera="wide shot, eye level, the glowing screen and the turned faces in the upper two-thirds, the dark rows of seats as the calm lower third",
         amb="hall_crowd", sens="violence",
         safe="Naail on the chair, the mask removal and the torture order are never shown: the screen is an unreadable blur, only the audience's reaction; Fairooz's recorded voice is not shown as a person"),
    dict(to=38, v1="beat_011", reason="emotional turning point: Fairooz exposed, his face drained white",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"{FAI} at the podium turned half toward the glowing wall screen behind him, stock-still, his face drained pale grey, eyes wide with panic, one hand thrown up toward the screen as he shouts; the screen's cold blurred glow on him",
         camera=f"medium close-up, eye level, {LOW} (the podium top)", amb="hall_crowd"),
    dict(to=39, reason="5.4 dialogue: Ashham shouts 'That video is the truth, Fairooz!' from the back while still disguised; no v1 image shows him speaking in the cap and glasses",
         chars=["ashham"], loc="police_hq_hall", speaker="ashham", transition="cut",
         visual=f"{ASH_D} standing in the centre aisle at the back of the press hall in front of a row of security officers, centred in the frame, shouting out with one empty hand thrust forward pointing toward the distant podium, mouth open mid-shout, jaw set with fury; in the soft-focus foreground the heads of seated journalists turning round in their seats to look back at him",
         camera=f"medium shot from the middle of the hall, eye level, Ashham's face centred in the upper half and sharp, {LOW} (the dark rows of seats)", amb="hall_crowd"),
    dict(to=40, v1="beat_012", reason="emotional turning point: Ashham throws off cap and glasses",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"{ASH_U} standing tall in the centre aisle at the back of the press hall, having just tossed his navy cap and dark sunglasses aside, the cap tumbling in the air at the edge of the frame; his face hard and blazing with righteous resolve; journalists in the rows turned round in their seats staring at him",
         camera=f"medium wide shot from the front of the hall, eye level, {LOW} (the dark aisle floor)", amb="hall_crowd"),
    dict(to=42, reuse="beat_016", reason="back to Fairooz recoiling in fear", transition="cut",
         chars=["fairooz"], loc="police_hq_hall", visual="reuse of beat_016", amb="hall_crowd",
         sens="violence", safe="Fairooz grabbing the shock gun and Ashham firing it are never shown: only Fairooz's panicked face"),
    dict(to=44, v1="beat_014", reason="action change: Fairooz brought down and surrounded by officers on live TV",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"beside the podium, {FAI} down on one knee, face twisted with rage, as four uniformed police officers close in around him and two of them raise him up by the arms, his hands held behind his back out of view; TV cameras with red lights trained on the scene",
         camera=f"medium wide shot, eye level, {LOW} (the stage floor)", amb="hall_crowd",
         sens="violence", safe="the shock-gun hit, the fall and the handcuffs are never shown: Fairooz kneeling up and escorted, hands out of view"),
    dict(to=47, v1="beat_015", reason="framing change: Ashham speaks to the camera while Fairooz laughs like a madman (each speaker centred by crop)",
         chars=["ashham", "fairooz"], loc="police_hq_hall",
         visual=f"{ASH_U} in the foreground looking straight into a TV camera lens with a stern, steady face; behind him, slightly out of focus, {FAI} being led away between two officers, head thrown back in a wild unhinged laugh, hands behind his back out of view",
         camera=f"medium close-up, eye level, {LOW}", amb="hall_crowd"),
    dict(to=51, v1="beat_016", reason="action change: chaos and camera flashes; Ashham's relief shadowed by the warning",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"{ASH_U} standing in the middle of the chaotic press hall, journalists crowding around him at a little distance holding out microphones, bright white camera flashes bursting all around; he breathes deeply, eyes half closed, a flicker of relief on his face shadowed by unease",
         camera=f"medium shot, eye level, {LOW}", amb="hall_crowd"),
    dict(to=55, v1="beat_017", reason="character enters: Naasir of Internal Affairs praises Ashham and sends him to the Minister",
         chars=["naasir", "ashham"], loc="police_hq_hall",
         visual=f"{NAA} striding up to {ASH_U} in the emptying press hall with a broad approving smile, one hand on Ashham's shoulder, the other gesturing toward the doors; Ashham looking round over the crowd with a searching frown",
         camera=f"medium two-shot, eye level, {LOW}", amb="hall_crowd"),
    # ---------------- MINISTER'S OFFICE
    dict(to=57, v1="beat_018", reason="scene change: the Home Minister's office; Ashham enters and salutes",
         chars=["ashham", "saleem"], loc="minister_office",
         visual=f"wide view of the silent luxurious office: {ASH_U} standing just inside the tall double doors, saluting crisply; far across the room {SAL} sits back in the tall black leather chair behind the huge desk, relaxed and unbothered, fingers laced on his stomach; his hands are empty",
         camera=f"wide shot, eye level, {LOW} (deep dark carpet)", amb="office_quiet",
         sens="other", safe="Saleem's smoking is never shown: his hands are empty"),
    dict(to=59, reason="5.4 dialogue: Saleem tells Ashham to sit and praises him; in the v1 images he is at the far edge (x≈82 % / 19 %)",
         chars=["saleem", "ashham"], loc="minister_office", speaker="saleem",
         visual=f"over-the-shoulder shot from behind Ashham: {SAL} sitting back in the tall black leather chair behind the huge polished desk, centred in the frame, relaxed and unbothered, fingers laced on his stomach, gazing past the camera into the distance with a faint condescending half-smile as he speaks; nothing in his hands, no smoke; in the soft blurred foreground at the lower right edge the back of the head and the dark-navy shoulder of {ASH_U}, standing",
         camera=f"medium close-up over the shoulder, eye level, Saleem's face centred in the upper half and sharp, Ashham soft and out of focus at the edge, {LOW} (the dark desk top)", amb="office_quiet",
         sens="other", safe="Saleem's smoking is never shown: empty hands, no smoke"),
    dict(to=61, reason="5.4 dialogue (reverse shot): Ashham, seated, answers that it is his duty and that big political figures are behind Project Phenix",
         chars=["ashham", "saleem"], loc="minister_office", speaker="ashham", transition="cut",
         visual=f"reverse shot over Saleem's shoulder: {ASH_U} seated in a chair across the huge polished desk, centred in the frame, leaning forward earnestly and speaking with a serious, determined face, both open hands resting on the desk; in the soft blurred foreground at the edge, the silver hair and black-suited shoulder of {SAL} from behind; warm desk-lamp light, heavy dark-red curtains and wood panelling behind Ashham",
         camera=f"medium close-up over the shoulder, eye level, Ashham's face centred in the upper half and sharp, Saleem soft at the edge, {LOW} (the dark desk top)", amb="office_quiet"),
    dict(to=65, v1="beat_020", reason="emotional turning point: Saleem locks the doors with a remote and confesses",
         chars=["saleem"], loc="minister_office",
         visual=f"close-up of {SAL} leaning forward over the desk into the lamp light with a slow cold smile, one finger pressing the button of a small black remote control on the desk; the soft-focus navy shoulder of a seated man in the foreground",
         camera=f"close-up, eye level, {LOW} (the polished desk top)", amb="office_quiet", transition="cut"),
    dict(to=66, v1="beat_021", reason="character enters: three commandos step out of a secret door behind Ashham",
         chars=["ashham"], loc="minister_office",
         visual=f"{ASH_U} standing beside his chair, rigid, slowly raising both open empty hands to shoulder height, face tense, eyes sliding sideways; behind him a hidden panel door in the wood wall stands open and three tall men in black clothes and black face masks step out close behind him with empty hands; the Minister a dark shape at the desk in the background",
         camera=f"medium shot, eye level, {LOW}", amb="office_quiet",
         sens="violence", safe="the commandos' guns aimed at Ashham's head and Ashham reaching for his gun are never shown: masked men with empty hands, Ashham raising empty hands"),
    dict(to=67, reuse="beat_027", reason="5.4 dialogue: back to Saleem as he says 'Put your hand down, Ashham'", transition="cut",
         chars=["saleem"], loc="minister_office", visual="reuse of beat_027", amb="office_quiet"),
    # ---------------- HABEEB BETRAYED
    dict(to=70, v1="beat_022", reason="scene change: Naasir and two police confront Habeeb in the server room",
         chars=["habeeb", "naasir"], loc="police_hq_server",
         visual=f"{HAB_S} half-turned in his chair at the server-room desk, alarmed yet defiant, gripping the chair back; {NAA} standing a few steps away glaring, one hand held out palm-up demanding; two uniformed police officers flanking him; the monitor angled away from view",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="command_center"),
    dict(to=71, reason="5.4 dialogue: Habeeb answers Naasir; in the v1 image he sits at the left edge (x≈29 %) half-turned away",
         chars=["habeeb", "naasir"], loc="police_hq_server", speaker="habeeb", transition="cut",
         visual=f"{HAB_O} half-turned in his chair at the server-room desk, centred in the frame, looking up with alarmed but defiant eyes and speaking, one hand gripping the chair back; in the blurred right foreground the black-suited shoulder and bald head of Naasir seen from behind; blue blinking server racks behind Habeeb; the monitor angled away from view",
         camera=f"medium close-up over Naasir's shoulder, eye level, Habeeb's face centred in the upper half and sharp, Naasir soft at the edge, {LOW} (dark desk and floor)", amb="command_center"),
    dict(to=72, reuse="beat_030", reason="5.4 shot/reverse shot: Naasir demands the original hard drive", transition="cut",
         chars=["naasir", "habeeb"], loc="police_hq_server", visual="reuse of beat_030", amb="command_center"),
    dict(to=73, reuse="beat_031", reason="5.4 shot/reverse shot: Habeeb refuses to give the drive", transition="cut",
         chars=["habeeb", "naasir"], loc="police_hq_server", visual="reuse of beat_031", amb="command_center",
         sens="violence", safe="the policeman's punch is never shown: Habeeb's defiant face, a muffled offscreen thud"),
    dict(to=76, v1="beat_023", reason="action change: Naasir seizes the original drive; Habeeb is led away (the blow is never shown)",
         chars=["naasir", "habeeb"], loc="police_hq_server",
         visual=f"{NAA} in the foreground holding up a small black hard drive between two fingers with a cold triumphant look; behind him two police officers lead {HAB_S} toward the door, his cap gone, glasses askew, face tired but unmarked and defiant, his hands held behind his back out of view",
         camera=f"medium shot, eye level, {LOW}", amb="command_center",
         sens="violence", safe="the punch, the fall, the bleeding mouth and the handcuffs are never shown: Naasir with the drive, Habeeb unmarked being escorted, hands out of view"),
    # ---------------- DARK WAREHOUSE
    dict(to=78, v1="beat_024", reason="scene and time change: Ashham is driven away for an hour (blindfold not shown)",
         loc="warehouse_road",
         visual="a black car with dark tinted windows driving alone along a lonely wet road between huge dark warehouses and stacked plain shipping containers, its headlights on; no people visible",
         camera="wide shot, slightly high angle, the car and the warehouses in the upper two-thirds, the wet road as the calm lower third",
         amb="car_interior", transition="black", sens="other",
         safe="the black cloth over Ashham's eyes and his abduction are shown only as the car on the road"),
    dict(to=80, v1="beat_025", reason="scene change: Ashham on the steel chair in the warehouse before Saleem and Fairooz",
         chars=["ashham", "saleem", "fairooz"], loc="warehouse",
         visual=f"{ASH_U} seated upright on a steel chair under the single hanging lamp, his arms behind the chair back out of view, defiant; standing before him {SAL} with his hands in his pockets and {FAI}, his uniform collar loosened, leaning in with a devilish grin; the vast dark warehouse around them",
         camera=f"medium wide shot, eye level, {LOW} (bare concrete floor in shadow)", amb="storage_hall",
         sens="violence", safe="the bonds are never shown: Ashham seated with his hands out of view, a tense face-off"),
    dict(to=82, reason="5.4 dialogue: Fairooz taunts Ashham; in the v1 warehouse image he stands at the right edge (x≈77 %)",
         chars=["fairooz", "ashham"], loc="warehouse", speaker="fairooz", transition="cut",
         visual=f"{FAI}, his uniform collar loosened, leaning down toward the camera under the single hanging lamp, centred in the frame, speaking with a devilish grin and cold eyes; in the soft blurred foreground at the lower left edge, the dark-navy shoulder and the back of the head of {ASH_U}, seated on a steel chair; the vast dark warehouse behind Fairooz, a dark-clad man waiting in the shadows with empty hands",
         camera=f"medium close-up over Ashham's shoulder, eye level, Fairooz's face centred in the upper half and sharp, Ashham soft at the edge, {LOW}", amb="storage_hall",
         sens="violence", safe="Fairooz's slap is never shown: only his taunting face"),
    dict(to=84, reuse="beat_036", reason="5.4 shot/reverse shot: Ashham answers that the whole country saw the video (centred by crop)", transition="cut",
         chars=["ashham", "saleem", "fairooz"], loc="warehouse", visual="reuse of beat_036", amb="storage_hall"),
    dict(to=87, v1="beat_026", reason="focus change: Saleem lays out the deepfake lie and signals his man",
         chars=["saleem"], loc="warehouse",
         visual=f"{SAL} leaning forward into the lamp light, speaking smoothly with a chilling calm smile, raising one hand to signal to someone behind him; a dark-clad man waits in the shadows behind him with empty hands",
         camera=f"medium close-up, eye level, {LOW}", amb="storage_hall"),
    dict(to=88, v1="beat_027", reason="object detail: the Project Phenix 'vaccine' (shown only as a glowing vial)",
         loc="warehouse",
         visual="close-up of a small glass vial glowing with an eerie bright-blue liquid standing on a small steel tray under the hanging lamp; the dark warehouse behind; the blurred shape of a seated man in navy in the background",
         camera="close-up, eye level, the glowing vial in the middle of the frame, the dark steel tray as the calm lower third",
         amb="storage_hall", sens="violence", safe="the syringe and needle are never shown: only a small glowing blue vial on a tray"),
    dict(to=91, reuse="beat_037", reason="5.4 dialogue: Fairooz describes what the vaccine will do", transition="cut",
         chars=["fairooz", "ashham"], loc="warehouse", visual="reuse of beat_037", amb="storage_hall"),
    dict(to=93, v1="beat_028", reason="emotional peak: Ashham strains in vain and closes his eyes",
         chars=["ashham"], loc="warehouse",
         visual=f"close-up of {ASH_U} on the steel chair straining with all his strength, shoulders and neck taut, eyes squeezed shut, sweat on his face under the lamp; a faint blue glow creeping in from the edge of the frame",
         camera=f"close-up, slightly high angle, {LOW}", amb="storage_hall",
         sens="violence", safe="the needle nearing his neck and the bonds are never shown: only his straining face and a blue glow"),
    # ---------------- THE RAID
    dict(to=95, v1="beat_029", reason="action change: the steel door is blown open and the MNDF unit storms in",
         loc="warehouse_raid",
         visual="the warehouse's huge steel door blown open in a burst of orange glow and billowing grey smoke; through the smoke a line of MNDF special-forces soldiers in plain black combat gear and helmets pour in, bright white flashlight beams cutting the smoke, their hands empty except for flashlights; nobody hurt; no bystanders, no civilians and no women anywhere in the warehouse, only the soldiers coming in and the empty steel chair under the lamp",
         camera="wide shot from inside the warehouse, eye level, the blown doorway and soldiers in the upper two-thirds, the dark concrete floor as the calm lower third",
         amb="chaos_hall", sens="violence", safe="the explosion and the firing are shown only as smoke, glow and flashlight beams; soldiers' hands empty"),
    dict(to=96, reason="5.4 dialogue: the MNDF commander shouts 'Nobody move! Hands up!' with Faahid at the head of the unit; no v1 image shows the commander",
         chars=["faahid"], loc="warehouse_raid", speaker="mndf_commander",
         visual=f"an MNDF special-forces commander in plain black combat gear and a black helmet, his face clearly visible under the helmet (a Maldivian man about forty with a short dark beard), centred in the frame, shouting an order with his mouth open, one empty hand raised flat in a stop gesture; beside him at the right, slightly softer, {FAH} striding in with a stern face; behind them black-clad soldiers in helmets with bright flashlights, grey smoke and orange glow from the blown-open door; no insignia, no lettering",
         camera=f"medium shot, eye level, the commander's face centred in the upper half and sharp, {LOW} (smoky concrete floor)", amb="chaos_hall",
         sens="violence", safe="the soldiers' guns are never shown: empty hands and flashlights only"),
    dict(to=97, v1="beat_030", reason="character enters: Faahid at the head of the soldiers; Saleem and Fairooz raise their hands",
         chars=["faahid", "saleem", "fairooz"], loc="warehouse_raid",
         visual=f"{FAH} striding forward at the head of black-clad MNDF soldiers in helmets with flashlights through drifting smoke, one arm pointing commandingly; in the foreground {SAL} and {FAI} raising both hands in fear, faces pale",
         camera=f"medium wide shot, eye level, {LOW} (smoky floor)", amb="chaos_hall",
         sens="violence", safe="the soldiers' guns are never shown: empty hands and flashlights only"),
    dict(to=98, v1="beat_031", reason="action change: Faahid starts freeing Ashham",
         chars=["faahid", "ashham"], loc="warehouse_raid",
         visual=f"{FAH} kneeling beside the steel chair working at the back of it with both hands, looking up at Ashham with a knowing smile; {ASH_U} still seated, turning his head to Faahid with amazed relief; smoke and flashlight beams drifting behind",
         camera=f"medium two-shot, eye level, {LOW} (concrete floor)", amb="storage_hall",
         sens="violence", safe="the chains are never shown: Faahid works at the back of the chair, out of view"),
    dict(to=100, reason="5.4 dialogue: Faahid explains how he tracked Ashham; in the v1 two-shot he is at the right edge (x≈72 %)",
         chars=["faahid", "ashham"], loc="warehouse_raid", speaker="faahid", transition="cut",
         visual=f"{FAH} kneeling on one knee beside the steel chair, centred in the frame, looking up with a warm, knowing smile as he speaks, his hands at the back of the chair out of view; at the left edge, soft and out of focus, {ASH_U} seated, seen in three-quarter back view; smoke and white flashlight beams drifting behind under the hanging lamp",
         camera=f"medium close-up at Faahid's eye level, Faahid's face centred in the upper half and sharp, Ashham soft at the edge, {LOW} (concrete floor)", amb="storage_hall",
         sens="violence", safe="the chains are never shown: Faahid's hands are at the back of the chair, out of view"),
    dict(to=101, reason="5.4 dialogue: Ashham rises and asks Saleem who fell into the trap; in the v1 image he stands at the left edge (x≈26 %)",
         chars=["ashham", "saleem"], loc="warehouse_raid", speaker="ashham",
         visual=f"{ASH_U} risen to his full height beside the empty steel chair, centred in the frame, chest out, looking hard to one side at the Minister and speaking with a fierce, steady face; at the right edge, soft and out of focus, {SAL} with both hands raised among black-clad soldiers with flashlights, his smug face collapsed; smoke drifting through the lamp light",
         camera=f"medium close-up, eye level, Ashham's face centred in the upper half and sharp, Saleem soft at the edge, {LOW}", amb="storage_hall"),
    dict(to=102, v1="beat_033", reason="cliffhanger: Fairooz reaches for the glowing vial on the floor",
         chars=["fairooz"], loc="warehouse_raid",
         visual=f"low view near the concrete floor: a man's hand in a dark-navy uniform sleeve reaching toward a small glass vial glowing bright blue on the floor in the lamp light; behind it, in soft focus, {FAI} crouching with a desperate, wild-eyed face",
         camera="close-up from floor level, the hand and the glowing vial in the middle of the frame, the face above, the dark floor edge as the calm lower third",
         amb="storage_hall", sens="violence", safe="the syringe and the attempt to inject himself are never shown: only his hand reaching toward a glowing vial"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

T, M = "tight", "medium"
sh(1, "Inside police headquarters, the Shaheed Hussain Adam Building, it was unusually busy.")
sh(2, "Journalists and TV crews had gathered in the hall where the press conference was to be held. With Ashham and Habeeb in official police uniform, wearing caps and dark glasses, nobody noticed their faces.",
   [("camera_shutter", "ނޫސްވެރިންނާއި", -22)])
sh(3, "None of the officers walking down the corridor knew that these were the two investigators who had been declared dead.",
   [("footsteps_pavement", "ހިނގާފައި", -24)])
sh(4, "\"Sir, I'm heading for the main server room,\" Habeeb said quietly through the Bluetooth earpiece in his ear.",
   speaker="habeeb", crop=T, focus=[33, 35])
sh(5, "\"To cut the press conference's live feed and show the video on our hard drive to the whole country, I need just two minutes.\"",
   speaker="habeeb", crop=T, focus=[33, 38])
sh(6, "\"Good, Habeeb, be careful, security in that area will be tight,\" Ashham replied.", speaker="ashham", crop=M, focus=[51, 42])
sh(7, "Ashham headed toward the media hall. He went in among the security officers at the back of the hall and stopped, leaning against the wall.",
   [("footsteps_pavement", "ވަދެ", -24)])
sh(8, "His eyes were fixed on the face of Assistant Commissioner Fairooz, who was getting ready beside the podium.")
sh(9, "Fairooz stood perfectly calm, straightening the buttons of his shirt. The false statement.",
   [("cloth_rustle", "ރީތިކުރަން", -24)])
sh(10, "As the clock struck nine in the morning, the cameras' red lights came on. TV channels across the Maldives began broadcasting this press conference live.",
   [("camera_shutter", "ކެމެރާތަކުގެ", -22)])
sh(11, "Fairooz cleared his throat and leaned toward the microphone. \"Assalaamu alaikum. Dear citizens,",
   speaker="fairooz", crop="full")
sh(12, "and journalists present.\" Fairooz began to speak in a serious tone. \"Today I come",
   speaker="fairooz", crop=T, focus=[48, 35])
sh(13, "with sad news, yet big news connected to national security.", speaker="fairooz", crop=M, focus=[48, 42])
sh(14, "To investigate the death of Naail Moosa Thaahir, who went missing a week ago,", speaker="fairooz", crop=T, focus=[48, 36])
sh(15, "the two Serious Crimes officers sent to a southern atoll, Ashham Mohamed and", speaker="fairooz", crop="full")
sh(16, "Ismail Habeeb, have taken a big bribe from the criminals and betrayed the nation.\"",
   speaker="fairooz", crop=T, focus=[48, 35])
sh(17, "The sound of the journalists in the hall whispering questions to one another echoed. \"They",
   [("crowd_gasp", "ގުގުމާލި", -24)], crop="full")
sh(18, "destroyed the investigation's secret files and then tried to flee the country secretly at night.\"",
   speaker="fairooz", crop=M, focus=[48, 42])
sh(19, "Fairooz kept stringing lies together. \"But because of the rough sea, the launch they fled in sank,",
   speaker="fairooz", crop=T, focus=[48, 35])
sh(20, "and both officers drowned. This is a great", speaker="fairooz", crop="full")
sh(21, "shame for the police institution.\" Standing at the back, Ashham ground his teeth. Seeing the depth of Fairooz's scheming, his blood boiled.",
   hum=True)
sh(22, "The battle of the server room. At that moment Habeeb stood outside the server room on the third floor.")
sh(23, "The door's lock could only be opened with a biometric card. Habeeb touched a small device he took from his pocket to the card reader.",
   [("computer_beep", "ޖެއްސި", -20)])
sh(24, "Thanks to the hacking program he had prepared at the safe house, the door opened slowly without the alarm going off.",
   [("door_open", "ހުޅުވުނު", -22)])
sh(25, "When he went inside, the big server racks were humming. Habeeb found the main broadcast server and connected his hard drive with a cable.",
   [("keyboard_typing", "ގުޅާލި", -22)])
sh(26, "\"Bypassing the system... forty percent... seventy percent,\" showed on the screen. Suddenly the server room door opened.",
   [("door_open", "ހުޅުވުނު", -18)])
sh(27, "A security guard came in. \"Hey! Who are you? Hands up!\" Startled, Habeeb raised his hands.",
   [("gasp", "ސިއްސައިގެން", -22)], speaker="guard", crop=M, focus=[53, 42])
sh(28, "But with his foot he kicked over the heavy chair beside him so that it struck the guard's legs. As the guard stumbled, Habeeb rushed at him, seized the electric shock baton in his hand and twisted it away.",
   [("crash_clatter", "ކޮއްޕާލީ", -20)])
sh(29, "They fell and grappled. The guard's blow drew blood from Habeeb's face, but Habeeb summoned his courage, struck the guard's head against the steel of a server rack and knocked him out.",
   [("soft_thud", "ޖަހައި", -23)])
sh(30, "Breathing hard, Habeeb looked at the computer screen: upload complete. The thunder of truth.",
   [("breath_heavy", "މާނޭވާލަމުން", -20), ("computer_beep", "ކޮމްޕްލީޓް", -20)])
sh(31, "\"So this case now...\" Just as Fairooz was about to wrap up, the signal of the big screen in the hall suddenly cut out.",
   [("power_down", "ކެނޑުނު", -20)], speaker="fairooz", crop=M, focus=[48, 42])
sh(32, "And on TVs across the Maldives, instead of Fairooz's face and the fake documents he had shown, another video began to play.")
sh(33, "It was a video from inside the bunker on the deserted island Kandu-huttaa. Naail sat tied to a chair, and in front of him stood Fairooz.")
sh(34, "It clearly showed him taking off the mask on his face and ordering inhuman torture of Naail. The sound was very clear too.")
sh(35, "\"The secret of this lab, built with your father's money, will be buried with you.\"", hum=True)
sh(36, "Fairooz's voice was heard saying it in the video. Silence fell over the whole media hall. The journalists' mouths fell open, and the colour drained completely from Fairooz's face.",
   [("crowd_gasp", "ހުޅުވި", -18)], crop="full")
sh(37, "\"What... what is this? Stop it!\" Fairooz shouted. But nobody could stop it.",
   speaker="fairooz", crop=T, focus=[31, 35])
sh(38, "After the video, photos and documents of the poor people in the bunker kept appearing on the screen. Confrontation.",
   crop=M, focus=[60, 45])
sh(39, "\"That video is the truth, Fairooz!\" A loud voice came from the back of the hall. Everyone turned round to look.",
   [("crowd_gasp", "ފަސްއެނބުރި", -22)], speaker="ashham", crop=T, focus=[49, 35])
sh(40, "Ashham took off his cap and glasses and threw them away. He stood in full police combat uniform. The fire of vengeance burned in his eyes.",
   [("cloth_rustle", "އެއްލާލި", -22)], crop="full")
sh(41, "\"Ashham?!\" Fairooz stepped back in fear and grabbed the shock gun of the security officer beside him.",
   [("gasp", "ފަހަތަށް", -20)], hum=True, speaker="fairooz", crop=T, focus=[31, 35])
sh(42, "But Ashham was far quicker. At once he took the shock gun, aimed at Fairooz and fired. It struck Fairooz in the chest.",
   [("electric_spark", "ޖެހި", -22)], crop="full")
sh(43, "With that he fell to the floor, screaming. The other police officers in the hall stepped forward at once and surrounded Fairooz on Ashham's order.",
   [("soft_thud", "ވެއްޓުނު", -22), ("boots_march", "ކުރިއަށް", -22)])
sh(44, "Before the whole nation, on live TV, Assistant Commissioner Fairooz was handcuffed. Ashham looked toward the camera.",
   [("lock_click", "އެޅުވުނު", -22)])
sh(45, "\"The law is not a toy.\" At that moment Fairooz let out a strange laugh.", speaker="ashham", crop=T, focus=[34, 35])
sh(46, "\"Ashham... you think this is over? The real owner of Project Phenix is far higher up.",
   hum=True, speaker="fairooz", crop=T, focus=[69, 35])
sh(47, "Your story will end before you ever reach him.\" Fairooz began to laugh like a madman.",
   hum=True, speaker="fairooz", crop=T, focus=[69, 38])
sh(48, "From a sea of victory to the shore of anxiety. As the sight of Fairooz in handcuffs was shown live on TVs across the Maldives, great chaos broke out in the media hall.",
   [("crowd_panic", "ހަލަބޮލިކަމެއް", -22)])
sh(49, "The journalists began firing questions all at once. Amid the cameras' flashes, Ashham took a deep breath.",
   [("camera_shutter", "ފްލޭޝްލައިޓްތަކުގެ", -18), ("breath", "ނޭވާއެއްލި", -22)])
sh(50, "Some measure of peace came to his heart. Naail's real killer, the mastermind of the crimes on the deserted island, had been exposed before the nation.")
sh(51, "But Fairooz's warning kept echoing in Ashham's ears: the real owner of Project Phenix is far higher up. \"Ashham,",
   hum=True)
sh(52, "today you are a national hero,\" said Naasir, head of police Internal Affairs, as he came into the hall.",
   [("footsteps_pavement", "ވަދެގެން", -22)], speaker="naasir", crop=T, focus=[37, 35])
sh(53, "\"Fairooz and Moosa Thaahir have been arrested on the spot. Go to the Home Minister's office now. The Minister wants to meet you right away.\" \"Where's Habeeb?\"",
   speaker="naasir", crop=M, focus=[38, 42])
sh(54, "Ashham looked around. \"He's in the server room, securing the remaining data,\" Naasir replied. \"Go.",
   speaker="naasir", crop=T, focus=[37, 36])
sh(55, "This is an order straight from the very top of the state.\" Ashham headed for the Home Ministry.",
   [("footsteps_pavement", "މިސްރާބު", -24)], speaker="naasir", crop=M, focus=[38, 42])
sh(56, "He believed every danger was over. The Minister's room: Home Minister Mohamed Saleem's office was a place of Malé's finest design.")
sh(57, "Silence filled the room. Ashham went in and saluted. Minister Saleem sat in his big chair, smoking a cigarette.",
   [("door_open", "ވަދެ", -20)])
sh(58, "Not a trace of worry showed on his face. \"Ashham, sit,\" Saleem said, gazing into the distance.",
   speaker="saleem", crop=M, focus=[40, 42])
sh(59, "\"What you did today is a very big thing. Arresting someone as powerful as Fairooz", speaker="saleem", crop=T, focus=[40, 36])
sh(60, "is no easy matter.\" \"That is my duty, sir,\" Ashham said, sitting down in the chair.", speaker="ashham", crop=M, focus=[58, 42])
sh(61, "\"But this doesn't end here. Big political figures are behind Project Phenix.\"", speaker="ashham", crop="full", focus=[58, 50])
sh(62, "Saleem smiled slowly. He pressed the button of a small remote on the desk. With that came the sound of the room's doors locking by themselves.",
   [("lock_click", "ތަޅުލެވުނު", -16)], hum=True, crop="full")
sh(63, "\"Ashham... you think you know everything?\" Saleem leaned forward.", speaker="saleem", crop=T, focus=[45, 35])
sh(64, "\"The lease of the land of the deserted island Kandu-huttaa, and the permit for the foreign pharmaceutical company, I gave them myself.",
   hum=True, speaker="saleem", crop=M, focus=[46, 42])
sh(65, "Fairooz was only the man who carried out my orders.\" Ashham's whole body went rigid.",
   hum=True, speaker="saleem", crop=T, focus=[45, 36])
sh(66, "At once he reached for the gun at his waist. But three armed commandos who came out of a secret door behind him aimed their guns straight at Ashham's head.",
   [("door_open", "ދޮރަކުން", -20), ("footsteps_pavement", "ނުކުތް", -22)], hum=True, crop="full")
sh(67, "\"Put your hand down, Ashham. Today you have walked straight into the middle of the trap.\"",
   speaker="saleem", crop=T, focus=[45, 35])
sh(68, "Habeeb in the net of betrayal. At that moment Habeeb sat in front of the computer in the server room at police headquarters.",
   crop="full")
sh(69, "He was tracing the paths the money in the bunker's remaining secret accounts had travelled. \"Habeeb,\"",
   [("keyboard_typing", "ހޯދަމުން", -22)], speaker="naasir", crop=T, focus=[70, 35])
sh(70, "came Naasir's voice from behind. When Habeeb turned to look, Naasir stood glaring angrily. Two more police officers were with him.",
   crop="full")
sh(71, "\"Naasir sir? What is this?\" Habeeb was alarmed. \"Where's the hard drive?\" Naasir demanded loudly.",
   speaker="habeeb", crop=M, focus=[38, 42])
sh(72, "\"What's in Ashham's pocket is only a copy. We know the original main hard drive is with you. Hand it over, quick!\"",
   speaker="naasir", crop=T, focus=[70, 35])
sh(73, "\"No... I won't give it,\" Habeeb said bravely. At Naasir's signal a policeman struck Habeeb hard in the face with his fist.",
   [("soft_thud", "ޖެހި", -22)], speaker="habeeb", crop=T, focus=[38, 36])
sh(74, "Habeeb staggered and fell to the floor. Blood began to run from his mouth. After searching Habeeb's pockets, Naasir seized the original hard drive.",
   [("soft_thud", "ވެއްޓުނު", -24)], crop="full")
sh(75, "\"Delete every Kandu-huttaa file in the system. And arrest this one and take him to Dhoonidhoo,\" Naasir ordered his men.",
   speaker="naasir", crop=T, focus=[34, 35])
sh(76, "Lying on the floor, Habeeb tried to send Ashham a message through the earpiece in his ear. But they took his phone and all his devices, handcuffed him and led him away.",
   [("footsteps_pavement", "ގެންދިޔަ", -22)], crop=M)
sh(77, "The darkness of the black warehouse. A black cloth was put over Ashham's eyes, and he felt himself being taken outside.")
sh(78, "He was put into a car. It felt as though the car drove this way and that for about an hour. At last the car stopped.",
   [("car_door", "އެރުވީ", -18), ("car_pass", "ދުއްވިހެން", -22)])
sh(79, "When the cloth was taken from his eyes, he was sitting inside a big warehouse. Now he was on a steel chair, bound tightly on four sides.",
   hum=True)
sh(80, "Before him stood Home Minister Saleem, and Fairooz. A devilish smile showed on Fairooz's face. \"Ashham,")
sh(81, "did you think putting police handcuffs on me would put me in jail?\" Fairooz struck Ashham in the face.",
   [("soft_thud", "ޖެހި", -22)], speaker="fairooz", crop=M, focus=[47, 42])
sh(82, "\"All your evidence has now been destroyed. Habeeb too is under our power.\"", speaker="fairooz", crop="full", focus=[47, 50])
sh(83, "\"You... you won't escape,\" Ashham said in a voice choked with tears.", speaker="ashham", crop=T, focus=[53, 35])
sh(84, "\"The people of the whole Maldives have watched that video.\" \"What we will show the people tomorrow",
   speaker="ashham", crop=M, focus=[53, 42])
sh(85, "is that it was a deepfake video made with artificial intelligence.\"", speaker="saleem", crop=T, focus=[36, 35])
sh(86, "Minister Saleem leaned forward. \"It will be decided that you are a terrorist who worked with foreigners to defame the state.",
   speaker="saleem", crop=M, focus=[38, 42])
sh(87, "The news of your death will be heard tomorrow.\" Saleem signalled to his men.", speaker="saleem", crop=T, focus=[36, 36])
sh(88, "With that, one of them came up to Ashham holding a big syringe. In it was the dangerous Project Phenix vaccine made in the Kandu-huttaa bunker.",
   [("footsteps_pavement", "ޖެހިލި", -22)], hum=True)
sh(89, "The last hope cut off. \"When this vaccine enters your body,", speaker="fairooz", crop=M, focus=[47, 42])
sh(90, "every memory in your brain will be wiped,\" Fairooz said. \"You will become", speaker="fairooz", crop="full", focus=[47, 50])
sh(91, "a living body without a soul.\" Ashham struggled hard to break free of his bonds.",
   [("breath_heavy", "ތެޅިގަތް", -20)], speaker="fairooz", crop=T, focus=[47, 35])
sh(92, "But those heavy steel bonds did not budge. The syringe's needle drew closer and closer to the vein in his neck. His eyes closed.",
   [("metal_clang", "ދަގަނޑުތައް", -22), ("heartbeat", "ދެލޯ", -18)], hum=True)
sh(93, "He felt these were the very last seconds of his life. Habeeb was locked up. The evidence had been seized.",
   hum=True)
sh(94, "And the highest leaders of the state were now protecting the criminals. Suddenly the warehouse's huge main steel door burst apart with a powerful blast.",
   [("distant_boom", "ފަޅައިގެން", -14)])
sh(95, "Thick smoke and flames poured into the warehouse. A special MNDF unit in black combat gear stormed in, firing.",
   [("fire_crackle", "އަލިފާންގަނޑު", -20), ("boots_march", "ވަދެގަތް", -18)])
sh(96, "At their head was retired Commissioner Faahid! \"Nobody move! Hands up!\"", speaker="mndf_commander", crop=M, focus=[42, 42])
sh(97, "shouted the commander of the soldiers who came with Faahid. As Minister Saleem and Fairooz raised their hands in fear, the soldiers aimed their guns all around them.")
sh(98, "Faahid ran over and began removing Ashham's chains. Ashham looked at Faahid's face. \"Ashham,",
   [("footsteps_pavement", "ދުވެފައި", -22), ("metal_clang", "ޗޭނުތައް", -24)])
sh(99, "did you think I was just sitting at home?\" Faahid smiled. \"I've been tracking your location through the Ministry's secret monitoring system.",
   speaker="faahid", crop=M, focus=[51, 42])
sh(100, "And I had already sent all the evidence to the head of the military beforehand.\" Ashham rose from the chair.",
   [("cloth_rustle", "ތެދުވި", -22)], speaker="faahid", crop="full", focus=[51, 50])
sh(101, "Powerful strength surged through his body. He looked toward Minister Saleem. \"Now do you know who fell into the trap?\"",
   hum=True, speaker="ashham", crop=T, focus=[34, 35])
sh(102, "But at that moment Fairooz was seen picking up the syringe lying on the floor, trying to inject it into his own body. To be continued.",
   [("heartbeat", "ސިރިންޖު", -18)], hum=True)
SHOTS = S

"""Beat/shot plan for Project Phenix episode 323 (used by plan_beats.py)."""

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

BEATS = [
    # ---------------- POLICE HQ: arrival in disguise
    dict(to=3, reason="episode opening: police HQ unusually busy; Ashham and Habeeb walk in disguised among officers",
         chars=["ashham", "habeeb"], loc="police_hq_corridor",
         visual=f"{ASH_D} and {HAB_D} walking side by side down the busy headquarters corridor inside a small group of uniformed police officers, heads slightly lowered, calm unreadable faces; BOTH men wear identical dark-navy long-sleeved police uniforms, navy police caps and dark sunglasses (Habeeb is NOT wearing his grey jacket or white t-shirt, and wears black police boots); further down, journalists with TV cameras and microphones crowd at the glass doors of the press hall; nobody looks at the two of them",
         camera=f"medium wide shot, eye level, {LOW} (polished floor)", amb="hall_crowd"),
    dict(to=6, reason="framing change: Habeeb speaks to Ashham through his earpiece before they split up",
         chars=["habeeb", "ashham"], loc="police_hq_corridor",
         visual=f"two-shot in a quieter bend of the corridor: {HAB_D} touching a small black wireless earpiece in his ear and murmuring with a focused look; {ASH_D} a step beside him, half-turned, glancing back over his shoulder along the corridor, serious",
         camera=f"medium close-up two-shot, eye level, {LOW}", amb="office_day"),
    dict(to=9, reason="scene change: Ashham at the back wall of the press hall watching Fairooz prepare at the podium",
         chars=["ashham", "fairooz"], loc="police_hq_hall",
         visual=f"{ASH_D} leaning against the back wall of the press hall among a row of security officers, arms folded, face turned toward the front; far away across the rows of journalists, small but sharp at the podium, {FAI} calmly straightening the buttons of his uniform",
         camera=f"medium shot, Ashham in the right foreground in three-quarter profile, the podium in the distance, {LOW} (dark rows of seats)", amb="hall_crowd"),
    dict(to=12, reason="time/action change: 9 am, the red camera lights come on and Fairooz begins the live statement",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"wide view from the back of the press hall: rows of journalists, TV cameras on tripods with glowing red lights, {FAI} at the podium leaning toward the microphones with a solemn face; the big wall screen behind him shows only a soft blue glow",
         camera=f"wide shot, eye level, the podium and screen in the upper two-thirds, {LOW} (the dark backs of the rows)", amb="hall_crowd"),
    dict(to=16, reason="framing change: close on Fairooz delivering the false statement; journalists murmur",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"close-up of {FAI} at the microphones, speaking gravely with a staged sorrowful frown, one hand resting on the podium, his eyes cold; in the blurred foreground journalists lean toward each other whispering",
         camera=f"close-up, slightly low angle, {LOW} (the podium top)", amb="hall_crowd"),
    dict(to=18, reason="focus change: Ashham's silent fury at the back of the hall",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"close-up of {ASH_D} standing with his back against the plain dark rear wall of the press hall among other officers, arms folded, no podium and no microphones near him; his jaw clenched hard, the muscles of his face tight with anger behind the dark sunglasses; far behind him, out of focus, the lit stage at the other end of the hall",
         camera=f"close-up, eye level, {LOW}", amb="hall_crowd"),
    # ---------------- SERVER ROOM
    dict(to=22, reason="scene change: Habeeb gets into the server room and connects the drive to the broadcast server",
         chars=["habeeb"], loc="police_hq_server",
         visual=f"{HAB_S} crouched at an open server rack, plugging a small black hard drive into it by a cable, a laptop open on a cart beside him with its screen angled away showing only a glowing bar; behind him the heavy security door stands ajar with a small black gadget still clipped to its card reader; a bead of sweat on his brow, intense focus",
         camera=f"medium shot, eye level, {LOW} (dark floor between the racks)", amb="command_center"),
    dict(to=25, reason="character enters: a security guard catches Habeeb (the struggle is never shown)",
         chars=["habeeb"], loc="police_hq_server",
         visual=f"tense standoff across the server room: a stocky security guard in a plain dark-grey uniform standing in the open doorway, one arm pointing sharply at Habeeb, his other hand empty; {HAB_S} across the room beside the racks with both hands raised to shoulder height, eyes wide; a heavy office chair on wheels between them; the two men several metres apart",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="command_center",
         sens="violence", safe="the chair kick, the shock baton, the blows, Habeeb's bleeding face and the guard knocked out are never shown: only the standoff at a distance, with a muffled offscreen thud"),
    dict(to=26, reason="back to Habeeb at the server: upload complete", reuse="beat_007",
         chars=["habeeb"], loc="police_hq_server", visual="reuse of beat_007", amb="command_center"),
    # ---------------- THE TRUTH ON SCREEN
    dict(to=31, reason="action change: the hall's big screen cuts and the bunker video plays live",
         loc="police_hq_hall",
         visual="the press hall seen from the side: the big wall screen behind the podium glowing with a dark, heavily blurred, unreadable image; the rows of journalists half-rising and turning toward it, mouths open, TV cameras swinging round; their faces lit by the cold screen glow; the figure at the podium only a small dark silhouette",
         camera="wide shot, eye level, the glowing screen and the turned faces in the upper two-thirds, the dark rows of seats as the calm lower third",
         amb="hall_crowd", sens="violence",
         safe="Naail on the chair, the mask removal and the torture order are never shown: the screen is an unreadable blur, only the audience's reaction"),
    dict(to=33, reason="emotional turning point: Fairooz exposed, his face drained white",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"{FAI} at the podium turned half toward the glowing wall screen behind him, stock-still, his face drained pale grey, eyes wide with panic, one hand thrown up toward the screen as he shouts; the screen's cold blurred glow on him",
         camera=f"medium close-up, eye level, {LOW} (the podium top)", amb="hall_crowd"),
    dict(to=35, reason="emotional turning point: Ashham's voice from the back; he throws off cap and glasses",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"{ASH_U} standing tall in the centre aisle at the back of the press hall, having just tossed his navy cap and dark sunglasses aside, the cap tumbling in the air at the edge of the frame; his face hard and blazing with righteous resolve; journalists in the rows turned round in their seats staring at him",
         camera=f"medium wide shot from the front of the hall, eye level, {LOW} (the dark aisle floor)", amb="hall_crowd"),
    dict(to=37, reason="back to Fairooz recoiling in fear", reuse="beat_011",
         chars=["fairooz"], loc="police_hq_hall", visual="reuse of beat_011", amb="hall_crowd",
         sens="violence", safe="Fairooz grabbing the shock gun and Ashham firing it are never shown: only Fairooz's panicked face"),
    dict(to=39, reason="action change: Fairooz brought down and surrounded by officers on live TV",
         chars=["fairooz"], loc="police_hq_hall",
         visual=f"beside the podium, {FAI} down on one knee, face twisted with rage, as four uniformed police officers close in around him and two of them raise him up by the arms, his hands held behind his back out of view; TV cameras with red lights trained on the scene",
         camera=f"medium wide shot, eye level, {LOW} (the stage floor)", amb="hall_crowd",
         sens="violence", safe="the shock-gun hit, the fall and the handcuffs are never shown: Fairooz kneeling up and escorted, hands out of view"),
    dict(to=41, reason="framing change: Ashham speaks to the camera while Fairooz laughs like a madman",
         chars=["ashham", "fairooz"], loc="police_hq_hall",
         visual=f"{ASH_U} in the foreground looking straight into a TV camera lens with a stern, steady face; behind him, slightly out of focus, {FAI} being led away between two officers, head thrown back in a wild unhinged laugh, hands behind his back out of view",
         camera=f"medium close-up, eye level, {LOW}", amb="hall_crowd"),
    dict(to=46, reason="action change: chaos and camera flashes; Ashham's relief shadowed by the warning",
         chars=["ashham"], loc="police_hq_hall",
         visual=f"{ASH_U} standing in the middle of the chaotic press hall, journalists crowding around him at a little distance holding out microphones, bright white camera flashes bursting all around; he breathes deeply, eyes half closed, a flicker of relief on his face shadowed by unease",
         camera=f"medium shot, eye level, {LOW}", amb="hall_crowd"),
    dict(to=50, reason="character enters: Naasir of Internal Affairs praises Ashham and sends him to the Minister",
         chars=["naasir", "ashham"], loc="police_hq_hall",
         visual=f"{NAA} striding up to {ASH_U} in the emptying press hall with a broad approving smile, one hand on Ashham's shoulder, the other gesturing toward the doors; Ashham looking round over the crowd with a searching frown",
         camera=f"medium two-shot, eye level, {LOW}", amb="hall_crowd"),
    # ---------------- MINISTER'S OFFICE
    dict(to=52, reason="scene change: the Home Minister's office; Ashham enters and salutes",
         chars=["ashham", "saleem"], loc="minister_office",
         visual=f"wide view of the silent luxurious office: {ASH_U} standing just inside the tall double doors, saluting crisply; far across the room {SAL} sits back in the tall black leather chair behind the huge desk, relaxed and unbothered, fingers laced on his stomach; his hands are empty",
         camera=f"wide shot, eye level, {LOW} (deep dark carpet)", amb="office_quiet"),
    dict(to=55, reason="action change: Ashham sits across the desk; they talk",
         chars=["saleem", "ashham"], loc="minister_office",
         visual=f"{SAL} behind the huge desk gazing past Ashham with a faint condescending look; {ASH_U} seated in a chair across the desk, leaning forward earnestly as he speaks; the polished desk between them",
         camera=f"medium two-shot from the side, eye level, {LOW} (the dark desk top)", amb="office_quiet"),
    dict(to=58, reason="emotional turning point: Saleem locks the doors with a remote and confesses",
         chars=["saleem"], loc="minister_office",
         visual=f"close-up of {SAL} leaning forward over the desk into the lamp light with a slow cold smile, one finger pressing the button of a small black remote control on the desk; the soft-focus navy shoulder of a seated man in the foreground",
         camera=f"close-up, eye level, {LOW} (the polished desk top)", amb="office_quiet"),
    dict(to=60, reason="character enters: three commandos step out of a secret door behind Ashham",
         chars=["ashham"], loc="minister_office",
         visual=f"{ASH_U} standing beside his chair, rigid, slowly raising both open empty hands to shoulder height, face tense, eyes sliding sideways; behind him a hidden panel door in the wood wall stands open and three tall men in black clothes and black face masks step out close behind him with empty hands; the Minister a dark shape at the desk in the background",
         camera=f"medium shot, eye level, {LOW}", amb="office_quiet",
         sens="violence", safe="the commandos' guns aimed at Ashham's head and Ashham reaching for his gun are never shown: masked men with empty hands, Ashham raising empty hands"),
    # ---------------- HABEEB BETRAYED
    dict(to=64, reason="scene change: Naasir and two police confront Habeeb in the server room",
         chars=["habeeb", "naasir"], loc="police_hq_server",
         visual=f"{HAB_S} half-turned in his chair at the server-room desk, alarmed yet defiant, gripping the chair back; {NAA} standing a few steps away glaring, one hand held out palm-up demanding; two uniformed police officers flanking him; the monitor angled away from view",
         camera=f"medium wide shot, eye level, {LOW} (dark floor)", amb="command_center"),
    dict(to=68, reason="action change: Naasir seizes the original drive; Habeeb is led away (the blow is never shown)",
         chars=["naasir", "habeeb"], loc="police_hq_server",
         visual=f"{NAA} in the foreground holding up a small black hard drive between two fingers with a cold triumphant look; behind him two police officers lead {HAB_S} toward the door, his cap gone, glasses askew, face tired but unmarked and defiant, his hands held behind his back out of view",
         camera=f"medium shot, eye level, {LOW}", amb="command_center",
         sens="violence", safe="the punch, the fall, the bleeding mouth and the handcuffs are never shown: Naasir with the drive, Habeeb unmarked being escorted, hands out of view"),
    # ---------------- DARK WAREHOUSE
    dict(to=70, reason="scene and time change: Ashham is driven away for an hour (blindfold not shown)",
         loc="warehouse_road",
         visual="a black car with dark tinted windows driving alone along a lonely wet road between huge dark warehouses and stacked plain shipping containers, its headlights on; no people visible",
         camera="wide shot, slightly high angle, the car and the warehouses in the upper two-thirds, the wet road as the calm lower third",
         amb="car_interior", transition="black", sens="other",
         safe="the black cloth over Ashham's eyes and his abduction are shown only as the car on the road"),
    dict(to=74, reason="scene change: Ashham on the steel chair in the warehouse before Saleem and Fairooz",
         chars=["ashham", "saleem", "fairooz"], loc="warehouse",
         visual=f"{ASH_U} seated upright on a steel chair under the single hanging lamp, his arms behind the chair back out of view, defiant; standing before him {SAL} with his hands in his pockets and {FAI}, his uniform collar loosened, leaning in with a devilish grin; the vast dark warehouse around them",
         camera=f"medium wide shot, eye level, {LOW} (bare concrete floor in shadow)", amb="storage_hall",
         sens="violence", safe="the bonds and Fairooz's slap are never shown: Ashham seated with his hands out of view, a tense face-off"),
    dict(to=77, reason="focus change: Saleem lays out the deepfake lie and signals his man",
         chars=["saleem"], loc="warehouse",
         visual=f"{SAL} leaning forward into the lamp light, speaking smoothly with a chilling calm smile, raising one hand to signal to someone behind him; a dark-clad man waits in the shadows behind him with empty hands",
         camera=f"medium close-up, eye level, {LOW}", amb="storage_hall"),
    dict(to=79, reason="object detail: the Project Phenix 'vaccine' (shown only as a glowing vial)",
         loc="warehouse",
         visual="close-up of a small glass vial glowing with an eerie bright-blue liquid standing on a small steel tray under the hanging lamp; the dark warehouse behind; the blurred shape of a seated man in navy in the background",
         camera="close-up, eye level, the glowing vial in the middle of the frame, the dark steel tray as the calm lower third",
         amb="storage_hall", sens="violence", safe="the syringe and needle are never shown: only a small glowing blue vial on a tray"),
    dict(to=82, reason="emotional peak: Ashham strains in vain and closes his eyes",
         chars=["ashham"], loc="warehouse",
         visual=f"close-up of {ASH_U} on the steel chair straining with all his strength, shoulders and neck taut, eyes squeezed shut, sweat on his face under the lamp; a faint blue glow creeping in from the edge of the frame",
         camera=f"close-up, slightly high angle, {LOW}", amb="storage_hall",
         sens="violence", safe="the needle nearing his neck and the bonds are never shown: only his straining face and a blue glow"),
    # ---------------- THE RAID
    dict(to=84, reason="action change: the steel door is blown open and the MNDF unit storms in",
         loc="warehouse_raid",
         visual="the warehouse's huge steel door blown open in a burst of orange glow and billowing grey smoke; through the smoke a line of MNDF special-forces soldiers in plain black combat gear and helmets pour in, bright white flashlight beams cutting the smoke, their hands empty except for flashlights; nobody hurt; no bystanders, no civilians and no women anywhere in the warehouse, only the soldiers coming in and the empty steel chair under the lamp",
         camera="wide shot from inside the warehouse, eye level, the blown doorway and soldiers in the upper two-thirds, the dark concrete floor as the calm lower third",
         amb="chaos_hall", sens="violence", safe="the explosion and the firing are shown only as smoke, glow and flashlight beams; soldiers' hands empty"),
    dict(to=87, reason="character enters: Faahid at the head of the soldiers; Saleem and Fairooz raise their hands",
         chars=["faahid", "saleem", "fairooz"], loc="warehouse_raid",
         visual=f"{FAH} striding forward at the head of black-clad MNDF soldiers in helmets with flashlights through drifting smoke, one arm pointing commandingly; in the foreground {SAL} and {FAI} raising both hands in fear, faces pale",
         camera=f"medium wide shot, eye level, {LOW} (smoky floor)", amb="chaos_hall",
         sens="violence", safe="the soldiers' guns are never shown: empty hands and flashlights only"),
    dict(to=89, reason="action change: Faahid frees Ashham and explains how he tracked him",
         chars=["faahid", "ashham"], loc="warehouse_raid",
         visual=f"{FAH} kneeling beside the steel chair working at the back of it with both hands, looking up at Ashham with a knowing smile; {ASH_U} still seated, turning his head to Faahid with amazed relief; smoke and flashlight beams drifting behind",
         camera=f"medium two-shot, eye level, {LOW} (concrete floor)", amb="storage_hall",
         sens="violence", safe="the chains are never shown: Faahid works at the back of the chair, out of view"),
    dict(to=90, reason="action change: Ashham rises and confronts Saleem",
         chars=["ashham", "saleem"], loc="warehouse_raid",
         visual=f"{ASH_U} risen to his full height beside the steel chair, chest out, strong and resolute, looking hard at {SAL}, who stands among black-clad soldiers with his hands raised, his smug face collapsed",
         camera=f"medium shot, eye level, {LOW}", amb="storage_hall", hum=True),
    dict(to=91, reason="cliffhanger: Fairooz reaches for the glowing vial on the floor",
         chars=["fairooz"], loc="warehouse_raid",
         visual=f"low view near the concrete floor: a man's hand in a dark-navy uniform sleeve reaching toward a small glass vial glowing bright blue on the floor in the lamp light; behind it, in soft focus, {FAI} crouching with a desperate, wild-eyed face",
         camera="close-up from floor level, the hand and the glowing vial in the middle of the frame, the face above, the dark floor edge as the calm lower third",
         amb="storage_hall", sens="violence", safe="the syringe and the attempt to inject himself are never shown: only his hand reaching toward a glowing vial"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Inside police headquarters, the Shaheed Hussain Adam Building, it was unusually busy.")
sh(2, "Journalists and TV crews had gathered in the hall where the press conference was to be held. With Ashham and Habeeb in official police uniform, wearing caps and dark glasses,",
   [("camera_shutter", "ނޫސްވެރިންނާއި", -22)])
sh(3, "nobody noticed their faces. None of the officers walking down the corridor knew that these were the two investigators declared dead.",
   [("footsteps_pavement", "ހިނގާފައި", -24)])
sh(4, "\"Sir, I'm heading to the main server room,\" Habeeb said quietly through the Bluetooth earpiece in his ear.")
sh(5, "\"To cut the press conference's live feed and show the whole nation the video on our hard drive, I need just two minutes.\" \"Good,")
sh(6, "Habeeb, be careful, the security in that area will be tight,\" Ashham replied.")
sh(7, "Ashham headed toward the media hall. He went in among the security officers at the back of the hall and stopped, leaning against the wall.",
   [("footsteps_pavement", "ވަދެ", -24)])
sh(8, "His eyes were fixed on the face of Assistant Commissioner Fairooz, who was getting ready beside the podium.")
sh(9, "Fairooz stood perfectly calm, straightening the buttons of his shirt. The false statement: as the clock struck nine in the morning,",
   [("cloth_rustle", "ރީތިކުރާށެވެ", -24)])
sh(10, "the cameras' red lights came on. TV channels across the Maldives began broadcasting the press conference live.",
   [("camera_shutter", "ކެމެރާތަކުގެ", -22)])
sh(11, "Fairooz cleared his throat and leaned toward the microphone. \"Assalaamu alaikum. Dear citizens, and journalists present.\"")
sh(12, "Fairooz began to speak in a serious tone. \"Today I come with sad news, but a big story connected to national security.")
sh(13, "The two Serious Crimes officers sent to a southern atoll to investigate the death of Naail Moosa Thaahir, who went missing a week ago, Ashham Mohamed and Ismail Habeeb, have...")
sh(14, "taken a large bribe from the criminals and betrayed the nation.\" The sound of the journalists in the hall whispering questions to one another echoed.",
   [("crowd_gasp", "ގުގުމާލިއެވެ", -24)])
sh(15, "\"After destroying the investigation's secret files, they tried to flee the country secretly at night,\" Fairooz went on, stringing lies together.")
sh(16, "\"But because of the rough sea, the launch they fled in sank, and both officers drowned.")
sh(17, "This is a great shame for the police institution.\" Standing at the back, Ashham ground his teeth.")
sh(18, "Seeing the depth of Fairooz's scheming, his blood boiled. The battle of the server room: at that moment Habeeb stood outside the server room on the third floor.",
   hum=True)
sh(19, "The door's lock could only be opened with a biometric card. Habeeb touched a small device he took from his pocket to the card reader.",
   [("computer_beep", "ޖެއްސިއެވެ", -20)])
sh(20, "Thanks to the hacking program he had prepared at the safe house, the door opened slowly without the alarm going off. When he went inside,",
   [("door_open", "ހުޅުވުނެވެ", -22)])
sh(21, "the big server racks were humming. Habeeb found the main broadcast server and connected his hard drive with a cable. \"Bypassing the system...",
   [("keyboard_typing", "ގުޅާލިއެވެ", -22)])
sh(22, "40%... 70%...\" showed on Zayaan's screen. Suddenly the server room door opened. A security guard came in. \"Hey! Who are you?",
   [("door_open", "ހުޅުވުނެވެ", -18)])
sh(23, "Hands up!\" Startled, Habeeb raised his hands. But with his foot he kicked over the heavy chair beside him so that it struck the guard's legs.",
   [("gasp", "ސިއްސައިގެން", -22), ("crash_clatter", "ކޮއްޕާލީ", -20)])
sh(24, "As the guard stumbled, Habeeb rushed at him, seized the electric shock baton in his hand and twisted it away.",
   [("cloth_rustle", "ހިފައި", -22)])
sh(25, "They fell and grappled. The guard's blow drew blood from Habeeb's face, but Habeeb summoned his courage, struck the guard's head against the steel of a server rack and knocked him out.",
   [("soft_thud", "ޖަހައި", -23)])
sh(26, "Breathing hard, Habeeb looked at the computer screen. \"...Complete!\" Thunder of truth: Fairooz was about to wrap up his statement.",
   [("breath_heavy", "މާނޭވާލަމުން", -20), ("computer_beep", "ކޮމްޕްލީޓް", -20)])
sh(27, "\"So this case is now...\" Suddenly the signal of the big screen in the hall cut out.",
   [("power_down", "ކެނޑުނެވެ", -20)])
sh(28, "And on TVs across the Maldives, instead of Fairooz's face and the fake documents he had shown, another video began to play.")
sh(29, "It was a video from inside the bunker on the deserted island Kandu-huttaa. Naail sat tied to a chair, and in front of him stood Fairooz.")
sh(30, "It was a clear view of him taking off the mask on his face and ordering inhuman torture of Naail. The sound was very clear too.")
sh(31, "\"The secret of this lab, built with your father's money, will be buried with you,\" Fairooz's voice was heard saying in the video. Silence fell over the whole media hall.",
   hum=True)
sh(32, "The journalists' mouths fell open, and Fairooz's face went completely white. \"What... what is this? Stop it!\" Fairooz shouted.",
   [("crowd_gasp", "ހުޅުވި", -18)])
sh(33, "But nobody could stop it. After the video, photos and documents of the poor people in the bunker kept appearing on the screen.")
sh(34, "Confrontation: \"That video is the truth, Fairooz!\" a loud voice came from the back of the hall. Everyone turned round to look.",
   [("crowd_gasp", "ފަސްއެނބުރި", -22)])
sh(35, "Ashham took off his cap and glasses and threw them away. He stood in full police combat uniform.",
   [("cloth_rustle", "އެއްލާލިއެވެ", -22)])
sh(36, "The fire of justice burned in his eyes. \"Ashham?!\" Fairooz stepped back in fear",
   [("gasp", "ފަހަތަށް", -20)], hum=True)
sh(37, "and grabbed the shock gun of the security officer beside him. But Ashham was far quicker. At once he took the shock gun, aimed it at Fairooz and fired.",
   [("electric_spark", "ޖެހިއެވެ", -22)])
sh(38, "It struck Fairooz in the chest. With that he fell to the floor, screaming. The other police officers in the hall stepped forward at once",
   [("soft_thud", "ވެއްޓުނެވެ", -22), ("boots_march", "ކުރިއަށް", -22)])
sh(39, "and surrounded Fairooz on Ashham's order. Before the whole nation, on live TV, Assistant Commissioner Fairooz was handcuffed.",
   [("lock_click", "އެޅުވުނެވެ", -22)])
sh(40, "Ashham looked toward the camera. \"The law is not a toy.\" At that moment Fairooz let out a strange laugh. \"Ashham...")
sh(41, "you think this is over? The real owner of 'Project Phenix' is far higher up. Your story will end before you ever reach him,\" and Fairooz began to laugh like a madman.",
   hum=True)
sh(42, "From a sea of victory to the shore of anxiety: as the sight of Fairooz in handcuffs was shown live on TVs across the Maldives,")
sh(43, "great chaos broke out in the media hall. The journalists began firing questions all at once.",
   [("crowd_panic", "ހަލަބޮލިކަމެކެވެ", -22)])
sh(44, "Amid the cameras' flashes, Ashham took a deep breath. Some measure of peace came to his heart.",
   [("camera_shutter", "ފްލޭޝްލައިޓްތަކުގެ", -18), ("breath", "ނޭވާއެއްލިއެވެ", -22)])
sh(45, "Naail's real killer, the mastermind of the crimes on the deserted island, had been exposed before the nation.")
sh(46, "But Fairooz's warning kept echoing in Ashham's ears. The real owner of 'Project Phenix' is far higher up.",
   hum=True)
sh(47, "\"Ashham, today you are a national hero,\" said Naasir, head of police Internal Affairs, as he came into the hall.",
   [("footsteps_pavement", "ވަދެގެން", -22)])
sh(48, "\"Fairooz and Moosa Thaahir have been arrested on the spot. Go now to the Home Minister's office. The Minister wishes to meet you right away.\"")
sh(49, "\"Where's Habeeb?\" Ashham looked around. \"He's in the server room, securing the remaining data,\" Naasir replied.")
sh(50, "\"Go. This is an order straight from the very top of the state.\" Ashham headed for the Home Ministry.",
   [("footsteps_pavement", "މިސްރާބު", -24)])
sh(51, "He believed every danger was over. The Minister's room: Home Minister Mohamed Saleem's office was a place of Malé's finest design.")
sh(52, "Silence filled the room. Ashham went in and saluted. Minister Saleem sat in his big chair, smoking a cigarette.",
   [("door_open", "ވަދެ", -20)])
sh(53, "Not a trace of worry showed on his face. \"Ashham, sit,\" Saleem said, gazing into the distance. \"What you did today is a very big thing.")
sh(54, "Arresting someone as powerful as Fairooz is no easy matter.\" \"That is my duty, sir,\" Ashham said, sitting down in the chair.")
sh(55, "\"But this doesn't end here. Big political figures are behind 'Project Phenix'.\" Saleem smiled slowly.")
sh(56, "He pressed the button of a small remote on the desk. With that came the sound of the room's doors locking by themselves. \"Ashham...",
   [("lock_click", "ތަޅުލެވުނު", -16)], hum=True)
sh(57, "you think you know everything?\" Saleem leaned forward. \"The lease of the land of the deserted island Kandu-huttaa, and")
sh(58, "the permit for the foreign pharmaceutical company, I gave them myself. Fairooz was only the man who carried out my orders.\" Ashham's whole body went rigid.",
   hum=True)
sh(59, "At once he reached for the gun at his waist. But three armed commandos who came out of a secret door behind him aimed their guns straight at Ashham's head. \"Put your hand down, Ashham,\" Saleem said.",
   [("door_open", "ދޮރަކުން", -20), ("footsteps_pavement", "ނުކުތް", -22)], hum=True)
sh(60, "\"Today you have walked straight into the middle of the trap.\" Habeeb in the net of betrayal: at that moment Habeeb sat in front of the computer in the server room at police headquarters.")
sh(61, "He was tracing the paths the money in the bunker's remaining secret accounts had travelled. \"Habeeb,\" came Naasir's voice from behind.",
   [("keyboard_typing", "ހޯދަމުންނެވެ", -22)])
sh(62, "When Habeeb turned to look, Naasir stood glaring angrily. Two more police officers were with him. \"Naasir sir? What is this?\"")
sh(63, "Zayaan was alarmed. \"Where's the hard drive?\" Naasir demanded loudly. \"What's in Ashham's pocket is only a copy.")
sh(64, "We know the original main hard drive is with you. Hand it over, quick!\" \"No... I won't give it,\" Habeeb said bravely.")
sh(65, "At Naasir's signal a policeman struck Zayaan hard in the face with his fist. Habeeb staggered and fell to the floor.",
   [("soft_thud", "ޖެހިއެވެ", -22), ("soft_thud", "ވެއްޓުނެވެ", -24)])
sh(66, "Blood began to run from his mouth. After searching Habeeb's pockets, Naasir seized the original hard drive. \"Delete every Kandu-huttaa file in the system,\"")
sh(67, "Naasir ordered his men. \"And arrest this one and take him to Dhoonidhoo.\" Lying on the floor, Habeeb")
sh(68, "tried to send Ashham a message through the earpiece in his ear. But they took his phone and all his devices, handcuffed him and led him away.",
   [("footsteps_pavement", "ގެންދިޔައެވެ", -22)])
sh(69, "The darkness of the black warehouse: with a black cloth over his eyes, Ashham felt himself being taken outside. He was put into a car.",
   [("car_door", "އެރުވީ", -18)])
sh(70, "It felt as though the car drove this way and that for about an hour. At last the car stopped. When the cloth was taken from his eyes, he was sitting inside a big warehouse.",
   [("car_pass", "ދުއްވިހެން", -22)])
sh(71, "Now he was on a steel chair, bound tightly on four sides. Before him stood Home Minister Saleem, and Fairooz.",
   hum=True)
sh(72, "A devilish smile showed on Fairooz's face. \"Ashham, did you think you could put me in jail by putting police handcuffs on me?\"")
sh(73, "Fairooz struck Ashham in the face. \"All your evidence has now been destroyed. Habeeb too is under our power.\" \"You...",
   [("soft_thud", "ޖެހިއެވެ", -22)])
sh(74, "you won't escape,\" Ashham said in a voice choked with tears. \"The people of the whole Maldives have watched that video.\"")
sh(75, "\"Tomorrow we will show the people it was a 'deepfake' video made with artificial intelligence,\"")
sh(76, "Minister Saleem leaned forward. \"It will be decided that you are a terrorist who worked with foreigners to defame the state.")
sh(77, "The news of your death will be heard tomorrow.\" Saleem signalled to his men. With that, one of them came up to Ashham holding a big syringe.",
   [("footsteps_pavement", "ޖެހިލިއެވެ", -22)])
sh(78, "In it was the dangerous 'Project Phenix' vaccine made in the Kandu-huttaa bunker. The last hope cut off:",
   hum=True)
sh(79, "\"When this vaccine enters your body, every memory in your brain will be wiped,\" Fairooz said.")
sh(80, "\"You will become a living body without a soul.\" Ashham struggled hard to break free of his bonds. But those heavy steel fetters did not budge.",
   [("breath_heavy", "ތެޅިގަތެވެ", -20), ("metal_clang", "ދަގަނޑުތައް", -22)])
sh(81, "The syringe's needle drew closer and closer to the vein in his neck. His eyes closed.",
   [("heartbeat", "ދެލޯ", -18)], hum=True)
sh(82, "He felt these were the very last seconds of his life. Habeeb was locked up. The evidence had been seized.",
   hum=True)
sh(83, "And the highest leaders of the state were now protecting the criminals. Suddenly the warehouse's huge main steel door burst apart with a powerful blast.",
   [("distant_boom", "ފަޅައިގެން", -14)])
sh(84, "Thick smoke and flames poured into the warehouse. A special MNDF unit in black combat gear stormed in, firing.",
   [("fire_crackle", "އަލިފާންގަނޑު", -20), ("boots_march", "ވަދެގަތެވެ", -18)])
sh(85, "At their head was retired Commissioner Faahid! \"Nobody move! Hands up!\"")
sh(86, "shouted the commander of the soldiers who came with Faahid. As Minister Saleem and Fairooz raised their hands in fear,")
sh(87, "the soldiers aimed their guns all around them. Faahid ran over and began removing Ashham's chains. Ashham looked at Faahid's face. \"Ashham,",
   [("footsteps_pavement", "ދުވެފައި", -22), ("metal_clang", "ޗޭނުތައް", -24)])
sh(88, "did you think I was just sitting at home?\" Faahid smiled. \"I was tracking your location through the Ministry's secret monitoring system.")
sh(89, "And I had already sent all the evidence to the head of the military beforehand.\" Ashham rose from the chair.",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(90, "Powerful strength surged through his body. He looked toward Minister Saleem. \"Now do you know who fell into the trap?\" But,")
sh(91, "at that moment Fairooz was seen picking up the syringe lying on the floor, trying to inject it into his own body. To be continued.",
   [("heartbeat", "ސިރިންޖު", -18)], hum=True)
SHOTS = S

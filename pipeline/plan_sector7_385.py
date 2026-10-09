"""Beat/shot plan for Sector 7 episode 385 — the box is opened in Zail's workshop (used by plan_beats.py)."""

NOSCREEN = "every screen shows only soft abstract glowing light and colour, no letters, no numbers, no symbols, no icons"

LOC = {
    "s7_night": "the lowest level of a vast underground bunker city at night: narrow alleys between rusted corrugated-steel shacks and huge heaps of scrap metal, thick pipes running overhead, toxic smoke haze, puddles of dirty water on cracked concrete, a dark rocky cavern ceiling far above",
    "workshop_ext": "an isolated ruined workshop at the far edge of the underground Sector 7: one decayed corner of an old abandoned factory hall, broken rusted steel walls and collapsed girders, tangled cables, a single heavy riveted steel door with a dim slit of light, scrap heaps and puddles in front, no signs",
    "workshop": "the inside of an old exiled scientist's cluttered underground workshop in a ruined factory: a large scratched steel work table in the middle, piles of electrical parts, coils of wire, circuit boards and strange old machines, many old monitors of different sizes stacked around the room, rusted steel walls, a heavy riveted steel door, a hanging work lamp; " + NOSCREEN,
    "workshop_red": "the inside of the old scientist's cluttered underground workshop: a large scratched steel work table, a matte black rugged metal box on it with a cable plugged into its corner, a worn keyboard with blank unmarked keys, old monitors stacked around, the largest monitor facing away from the viewer; " + NOSCREEN,
    "workshop_dark": "the inside of the old scientist's cluttered underground workshop during a power cut: the steel work table, stacked dead monitors and machines barely visible in the darkness, a heavy riveted steel door",
    "workshop_gold": "the inside of the old scientist's cluttered underground workshop: the large steel work table with an opened matte black metal box on it, old monitors stacked around, the biggest monitor facing away from the viewer and pouring light into the room; " + NOSCREEN,
    "surface": "the open surface of the earth seen as live footage: a wide healed landscape under a clear blue sky, lush deep-green valleys and forested hills, a clean sparkling river winding between trees, no buildings, no people",
    "s7_hall": "a large grim communal hall in the underground Sector 7: rusted steel walls, pipes and steam, a huge old screen mounted high on the wall, rows of exhausted workers in grey work clothes standing below it",
    "vision": "a soft hazy dream-like vision of the dark underground Sector 7: dim rusted corridors and machine floors where poor families toil",
    "workshop_raid": "the inside of the old scientist's cluttered underground workshop at night: the heavy riveted steel door at the back, the steel work table, stacked monitors gone dim; " + NOSCREEN,
}
MOOD = {
    "s7_night": "deep night underground, near darkness, cold teal shadows and toxic grey-green haze, the only light a few thin red scanning beams from small patrol drones overhead and a faint sodium-orange glow far away, tense and frightening",
    "workshop_ext": "deep night underground, cold blue-teal darkness, a faint red drone glow in the haze far above, a thin warm amber slit of light around the steel door, lonely and secretive",
    "workshop": "night, dim cold blue glow from the many old monitors mixed with one warm amber hanging work lamp, dust and thin solder smoke hanging in the air, secretive, tense and curious",
    "workshop_red": "night, harsh pulsing red alarm light flooding from the big monitor across the faces and the table, deep black shadows, a few cold blue glows from smaller screens, urgent and frightening",
    "workshop_dark": "a sudden power cut: almost total darkness, only a faint dying red glow from one monitor and cold blue-black shadows, frightening and tense",
    "workshop_gold": "night, the room suddenly flooded with bright clean green and warm golden light pouring from the big monitor onto the faces, dust glittering in the light beams, awe, disbelief and wonder",
    "surface": "bright clear daylight, fresh natural colours, deep blue sky with soft white clouds, sunlight sparkling on the river, peaceful, hopeful and astonishing",
    "s7_hall": "dim cold grey light, the big screen pouring a fake fiery orange glow over the tired faces below, oppressive and deceitful",
    "vision": "hazy, desaturated, dreamlike memory-vision with a soft dark vignette, faint amber work lights in deep shadow, sorrowful and tender",
    "workshop_raid": "night, the room in darkness, sharp thin beams of red laser light slicing in through the cracks around the steel door and sweeping across the walls, cold blue shadows, extreme danger and grim resolve",
}

BEATS = [
    dict(to=2, reason="episode opening: Sector 7 at night, smoke and patrol drones with red lights", loc="s7_night",
         visual="a high wide view over the dark alleys and scrap heaps of the lowest bunker level at night, thick toxic smoke drifting between rusted shacks, three small black patrol drones hovering overhead each casting a thin red scanning beam down through the haze onto the wet ground; no people",
         camera="wide establishing shot, high angle, drones and beams in the upper two-thirds, a wet empty concrete alley as a calm lower third", amb="bunker_machinery"),
    dict(to=6, reason="character enters: Aira sneaking through the night with the black box pressed to her chest", chars=["aira"], loc="s7_night",
         visual="Aira moving silently like a shadow along a narrow alley between rusted shacks and scrap heaps, slightly crouched, both arms clutching a small worn canvas bag tightly against her chest, eyes darting upward with fear and determination, stepping carefully around dark puddles; a faint red drone beam sweeping the haze behind her",
         camera="medium wide, eye level, her face in the upper third, the wet concrete with puddles as a calm lower third", amb="corridor_drip"),
    dict(to=9, reason="action change: a drone passes right over her head and she presses herself behind a steel pipe, holding her breath", chars=["aira"], loc="s7_night",
         visual="Aira pressed flat against the dark side of a huge rusted steel pipe, holding her breath, eyes raised and wide, the bag held tight to her chest; just above the pipe a small black patrol drone glides past, its red scanning beam sweeping the ground a few steps away from her",
         camera="medium shot, low angle, her face and the drone in the upper half, the dark ground beside the pipe as a calm lower third", amb="corridor_drip"),
    dict(to=11, reason="scene change: the isolated ruined workshop where the exiled scientist Zail lives", loc="workshop_ext",
         visual="the lonely ruined corner of an old factory hall at the far edge of Sector 7, broken steel walls and leaning girders, a single heavy riveted steel door with a thin warm line of light around its edges, scrap and puddles in front; no people",
         camera="wide establishing shot, eye level, the door and ruins in the upper two-thirds, the wet empty ground as a calm lower third", amb="bunker_machinery"),
    dict(to=13, reason="character change: Aira knocks the secret code and Zail opens the steel door", chars=["zail", "aira"], loc="workshop_ext",
         visual="the heavy steel door opened a hand's width: Zail's bearded face with round wire glasses peering out cautiously through the gap, warm amber light behind him, his sharp eyes scanning the dark; Aira standing an arm's length away outside the door, one fist still raised from knocking, the bag held to her chest, glancing back over her shoulder",
         camera="medium shot, eye level, both faces in the upper half, the dark ground as a calm lower third", amb="corridor_drip"),
    dict(to=16, reason="scene change: inside the workshop; Aira sets the black box on the table and Zail is shocked", chars=["aira", "zail"], loc="workshop",
         visual="Aira setting a matte black rugged metal box with sharp edges and faint abstract etched grooves (no letters, no symbols) down on the big steel work table; across the table Zail stares at it, eyes wide behind his round glasses, his face drained with shock and fear; monitors and machines crowd the background",
         camera="medium wide, eye level, both faces in the upper half, the steel table top as a calm lower third", amb="workshop",
         sens="other", safe="the 'dangerous symbols and codes' on the box are shown only as faint abstract etched grooves, nothing readable"),
    dict(to=19, reason="action change: Aira tells him about Junction-9 and Zail touches the box, then hurries for his tools", chars=["zail", "aira"], loc="workshop",
         visual="Zail leaning over the table and slowly running his gloved hand over the lid of the black box, serious and breathless; Aira standing on the other side of the table an arm's length away, speaking quietly with an earnest face; behind Zail a cluttered shelf of tools and a wisp of solder smoke rising from a hot soldering iron in its stand",
         camera="medium shot, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop"),
    dict(to=22, reason="new framing: close detail of Zail examining the box's steel coating in the blue screen light", chars=["zail"], loc="workshop",
         visual="close view of Zail bent over the black box under the dim blue glow of the old monitors, his eyes fixed on it through his round glasses, the trembling fingertips of his fingerless gloves tracing the sharp machined edge of the box; scattered fine tools and a small magnifier on the table",
         camera="close-up, slightly high angle, his face in the upper third, his hands and the box lower, the dark table edge as a calm bottom", amb="workshop"),
    dict(to=25, reason="action change: Aira paces anxiously by the table, warning that soldiers will search every home", chars=["aira", "zail"], loc="workshop",
         visual="Aira pacing beside the work table, arms crossed tightly, glancing towards the rattling steel door with a worried tense face; Zail in the background still hunched over the black box at the table; loose steel sheets on the wall trembling",
         camera="medium shot, eye level, Aira's face in the upper third, the floor as a calm lower third", amb="workshop"),
    dict(to=28, reason="action change: Zail connects his handmade device to the box and the big monitor flares red with a warning", chars=["zail", "aira"], loc="workshop_red",
         visual="Zail plugging a thin cable from a small handmade circuit device full of tangled wires and chips into a tiny port in the corner of the black box; the big monitor behind the table faces away from the viewer and floods both of them with harsh red light; Aira a step back on the other side of the table, startled",
         camera="medium wide, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop"),
    dict(to=30, reason="emotional turning point: the red warning on their faces, Aira's breath catches", chars=["aira", "zail"], loc="workshop_red",
         visual="Aira's face lit by pulsing red light, breath caught, one hand pressed to her chest over the pendant, eyes wide; beside her at an arm's length Zail wiping sweat from his forehead with the back of his hand, already reaching for a keyboard with blank keys; the red glowing monitor faces away from the viewer, only its glow is seen",
         camera="medium close-up, eye level, both faces in the upper half", amb="workshop", sens="other",
         safe="the WARNING / ATTEMPT 1/3 message is never shown: only red glow on their faces from a monitor that faces away"),
    dict(to=33, reason="action change: Zail types at lightning speed; streams of green light, then the first attempt fails red", chars=["zail"], loc="workshop_red",
         visual="Zail hunched at a worn keyboard with blank unmarked keys, his fingers a blur, intense focus; flowing streams of soft green light reflected in his round glasses and on his face, mixing with red; small screens around him glowing with abstract green ripples only",
         camera="medium close-up from beside the screens, his face in the upper half, the keyboard and table as a calm lower third", amb="workshop", sens="other",
         safe="'thousands of green numbers and letters' shown only as abstract green light reflected in his glasses"),
    dict(to=35, reason="action change: the power cuts out; in the dark Aira grips a heavy wrench and Zail pulls the backup lever", chars=["aira", "zail"], loc="workshop_dark",
         visual="near-total darkness in the workshop: Aira standing tense with a heavy steel wrench gripped in both hands at her chest, eyes searching the dark; a few steps away Zail bending low to pull a big lever under the table, a faint red glow catching the edge of his glasses",
         camera="medium wide, eye level, faces in the upper half, the dark floor as a calm lower third", amb="workshop", sens="violence",
         safe="'her hand went to her weapon' shown as Aira gripping a heavy steel wrench (series rule: no weapons)"),
    dict(to=37, reason="emotional turning point: the final code works, green light floods the room and the box's lid opens", chars=["aira", "zail"], loc="workshop_gold",
         visual="the matte black box on the table with its lid slowly lifting open and a soft light glowing from inside; Aira and Zail leaning in on opposite sides of the table, faces washed with bright green light from the big monitor that faces away from the viewer, Zail's mouth open, Aira holding her breath",
         camera="medium shot, slightly low angle across the table, faces in the upper half, the box and table top lower", amb="workshop", sens="other",
         safe="ACCESS GRANTED is never shown: only green light on their faces and the opening box"),
    dict(to=39, reason="new framing: the two of them frozen in disbelief in the golden light of the screen", chars=["aira", "zail"], loc="workshop_gold",
         visual="Aira and Zail standing side by side at an arm's length apart, frozen, staring at the big monitor that faces away from the viewer, their faces bathed in warm golden and green light; Aira's large eyes wide with disbelief, Zail's glasses reflecting soft green light",
         camera="medium shot from behind the monitor, eye level, both faces in the upper half, the table edge as a calm lower third", amb="workshop"),
    dict(to=42, reason="scene change: the live footage from the surface fills the frame — blue sky, green valleys, rivers", loc="surface",
         visual="a breathtaking healed landscape: a clear blue sky with soft white clouds above lush deep-green valleys and forested hills, a clean sparkling river winding through the trees, sunlight on the water; no people, no buildings, no text",
         camera="wide aerial view, the sky and hills in the upper two-thirds, the calm river and meadow as a calm lower third", amb="surface_green",
         transition="dissolve", sens="other", safe="the radiation meter numbers are not shown; only the clean landscape"),
    dict(to=44, reason="action change: Aira reaches out and touches the green trees on the screen", chars=["aira"], loc="workshop_gold",
         visual="Aira reaching out slowly with trembling fingertips to touch the glowing glass of an old monitor that shows only green trees and blue sky, her face lit soft green and gold, eyes glistening with tears and wonder",
         camera="medium close-up from the side, her face and hand in the upper half, the dark table edge as a calm lower third", amb="workshop"),
    dict(to=47, reason="scene change (illustrative cutaway): Marcus's weekly broadcast of fake burning-wasteland footage to Sector 7", chars=["marcus"], loc="s7_hall",
         visual="Marcus seen on a huge old screen high on the rusted wall of a grim hall, standing calm and stern in his cream-white gold-trimmed coat in front of a fake background of an orange-glowing ruined wasteland under ash clouds; below, rows of exhausted workers seen from behind look up at him in silence",
         camera="wide shot, low angle, the screen with Marcus in the upper half, the workers' backs and the grey floor as a calm lower third", amb="bunker_machinery",
         sens="other", safe="the fake 'burning hell' footage is an empty glowing wasteland with no people; no text on the screen"),
    dict(to=49, reason="emotional turning point: a tear falls from Aira's eye as she asks why", chars=["aira", "zail"], loc="workshop_gold",
         visual="close view of Aira's face, a single tear running down her cheek, her eyes full of grief and anger, soft green-gold screen light on one side of her face; Zail out of focus in the background rising from his chair",
         camera="close-up, eye level, her face in the upper half, her coat collar and pendant lower", amb="workshop"),
    dict(to=52, reason="action change: Zail stands with both palms on the table and explains Marcus's power; Aira bows her head", chars=["zail", "aira"], loc="workshop",
         visual="Zail standing behind the steel table leaning forward on both spread palms, speaking with grim intensity, his eyes burning behind his round glasses; on the other side of the table Aira with her head bowed and jaw clenched, one fist resting hard on the table top; the opened black box between them",
         camera="medium wide, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop"),
    dict(to=55, reason="action change: Zail spots a red folder, clicks it open and red light floods his face", chars=["zail", "aira"], loc="workshop_red",
         visual="Zail gripping an old computer mouse, leaning close to a monitor that faces away from the viewer, his face suddenly bathed in deep red light, eyes narrowed in alarm; Aira a step behind him, watching his face anxiously",
         camera="medium close-up, eye level, faces in the upper half, the desk with the mouse as a calm lower third", amb="workshop", sens="other",
         safe="the red folder and PROJECT CLEANSLATE title are never shown: only red light on their faces"),
    dict(to=59, reason="new framing: the screen itself — a glowing map of Sector 7's tunnels with red smoke spreading through the vents", loc="workshop_red",
         visual="an object-only still life with absolutely no people, no faces and no figures anywhere: an old monitor screen filling almost the whole frame, standing on a dark empty table in an empty dark room, showing a glowing blue line-drawing map of a maze of tunnels and ventilation ducts seen in cross-section, with thick red smoke spreading through the ducts like veins; abstract shapes only, no letters, no numbers, no symbols; a faint red reflection on the dark table below",
         camera="close-up straight on, the glowing map in the upper two-thirds, the dark table top as a calm lower third", amb="workshop", sens="violence",
         safe="the neurotoxin plan is shown only as abstract red smoke on a map of empty tunnels; no people"),
    dict(to=64, reason="action change: Zail points at the countdown; Aira's legs give way and she grips the table edge", chars=["aira", "zail"], loc="workshop_red",
         visual="Zail pointing with a trembling finger at a red glowing panel on a monitor that faces away from the viewer, his lips trembling; Aira across the table, staggering, both hands gripping the edge of the steel table to hold herself up, face drained, mouth open in shock; the red glow pulsing on both faces",
         camera="medium wide, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop", sens="other",
         safe="the countdown and '7 days' are shown only as a red glowing panel; no digits"),
    dict(to=66, reason="memory/vision: the faces of children, the elderly and families of Sector 7 appear in Aira's mind", loc="vision",
         visual="a soft hazy vision: a small girl in a plain long dress and small headscarf holding her grandmother's hand, an old man in a cap resting against a pipe, a tired worker family with a mother in a hijab sitting together in the dim amber light of a machine floor; quiet, sad, gentle faces",
         camera="medium wide, eye level, faces in the upper half, the dark floor as a calm lower third", amb="memory",
         transition="dissolve", sens="other", safe="'lives taken to the grave' shown only as living, gentle faces of families in a memory-like vision"),
    dict(to=69, reason="action change: Zail slams his fist on the steel table, eyes blazing; Aira refuses to submit", chars=["zail", "aira"], loc="workshop_red",
         visual="Zail with his fist just landed on the steel table, leaning forward, eyes blazing with fury behind his round glasses, the red light hard on his face; Aira on the other side of the table straightening up, her face changing from shock to defiance",
         camera="medium shot, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop"),
    dict(to=72, reason="emotional turning point: Aira looks straight into Zail's eyes, her fear turning to resolve", chars=["aira", "zail"], loc="workshop",
         visual="close view of Aira's face, looking straight ahead with fierce unshakeable determination, jaw set, a dried tear trace on her cheek, the steel pendant on its chain at her chest; Zail's shoulder and glasses blurred in the foreground at the edge of the frame, at a distance",
         camera="close-up over Zail's shoulder, eye level, her face in the upper half", amb="workshop"),
    dict(to=76, reason="action change: Aira pockets the device and lays out the plan to hijack the broadcast", chars=["aira", "zail"], loc="workshop",
         visual="Aira slipping the small handmade circuit device into the pocket of her long coat while speaking with conviction, her other hand gesturing firmly; Zail on the other side of the table watching her in amazement, eyebrows raised; the opened black box and dim monitors between them",
         camera="medium shot, eye level, faces in the upper half, the table top as a calm lower third", amb="workshop"),
    dict(to=78, reason="return to the earlier image: Zail and Aira talking across the table about the secret resistance", reuse="beat_020", chars=["zail", "aira"], amb="workshop", loc="workshop",
         visual="(reuse of beat_020)"),
    dict(to=81, reason="action change and climax: boots outside, red laser beams through the door cracks; Aira grips a heavy wrench", chars=["aira", "zail"], loc="workshop_raid",
         visual="the dark workshop with thin sharp red beams of light slicing in through the cracks around the heavy steel door and sweeping across the walls; Aira standing in front facing the door, gripping a heavy steel wrench in both hands, eyes fierce and ready; Zail a few steps behind her crouched by the table, whispering, wide-eyed; no soldiers visible, only the red beams",
         camera="medium wide, eye level, faces and the door in the upper two-thirds, the dark floor as a calm lower third", amb="workshop", sens="violence",
         safe="soldiers shown only as red light beams through the door cracks; 'Aira takes her weapon' shown as gripping a heavy wrench"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Night in Sector 7 is always an unsafe, frightening time. The whole area is shrouded in the dark smoke of steel scrap and")
sh(2, "the foul smoke of toxic gas. The only light comes from the dangerous red laser lights of the patrol drones flying overhead.",
   [("drone_pass", "ޑްރޯންތަކުގެ", -22)])
sh(3, "Aira, the secret black box found at Junction-9 tucked into her small bag and pressed tightly to her chest,",
   [("cloth_rustle", "ޖައްސާ", -24)])
sh(4, "moved step by step, silently, like a shadow. With every step her heartbeat grew faster.",
   [("heartbeat", "އަވަސްވަމުންނެވެ", -20)])
sh(5, "For her conscience kept telling her that the box held a secret that could change the order of this whole city.")
sh(6, "Hiding behind the big heaps of scrap on the way, placing her feet so the muddy puddles would make no sound, Aira moved on.",
   [("splash", "ފެންގަނޑުތަކަށް", -24)])
sh(7, "From far away came the sound of patrol soldiers' boots and the harsh noise of machinery. Suddenly, as a drone whizzed over her head, Aira pressed herself into the cover of a steel pipe.",
   [("boots_march", "ބޫޓުގެ", -22), ("drone_pass", "ވިއްދައިގެން", -16)])
sh(8, "Holding her breath, she reasoned with herself. If she were caught now, she would have to go to the darkness of prison for the rest of her life,",
   [("breath", "ނޭވާ", -22)], hum=True)
sh(9, "or she might even face a more bitter end. But as the drone's light moved away, Aira again ran towards her destination.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -22)])
sh(10, "It was the most isolated, ruined workshop in Sector 7 — a decayed, derelict part of what was once a great factory.")
sh(11, "Living there was old Zail — once the most senior scientist of the upper level, but exiled to Sector 7 after he stood up against the government's corruption.")
sh(12, "Aira knocked on the door three times in a secret code. After a short moment, the steel door slowly opened,",
   [("knock", "ޓަކިދިނެވެ", -16), ("metal_door", "ހުޅުވި", -20)])
sh(13, "and Zail's face appeared, with his thick beard and sharp eyes. Zail looked around, then quickly let Aira in and locked the door.",
   [("door_close", "ތަޅުލިއެވެ", -18)])
sh(14, "Inside, the workshop was full of all kinds of electrical parts, glowing monitors and strange machines.")
sh(15, "Aira set the secret black box down on the table. On seeing the dangerous symbols and codes on its top, Zail's eyes widened",
   [("soft_thud", "ބޭއްވިއެވެ", -22)])
sh(16, "and the colour drained from his face. \"This... where did you find this?\" Zail's voice was full of utter amazement and fear.")
sh(17, "When Aira briefly told him what happened at Junction-9, Zail slowly reached out and ran his hand over the box. \"This is no ordinary thing, Aira.")
sh(18, "Inside this box may be the radiation chart of the whole city that the government is trying to hide,\" said Zail, letting out a deep breath,",
   [("sigh", "ނޭވާއެއް", -22)])
sh(19, "and he hurried to fetch his special tools to open the box. The workshop reeked of dust and the foul smoke of melting solder.",
   [("metal_clang", "ސާމާނުތައް", -22)])
sh(20, "In the dim blue light spreading from the old screens all around the room, Zail's eyes were fixed on the black box on the table.")
sh(21, "His experienced eye saw at once that the steel coating on the box's outer shell could not be broken with ordinary tools.")
sh(22, "\"If we try to force this box open, the self-destruct mechanism inside will activate and all the data will burn to ash,\" said Zail, running his trembling fingers along the sharp edges of the box.")
sh(23, "There was worry and caution in his voice. Aira paced back and forth beside the table. At the sound of the wind howling outside now and then",
   [("wind_howl", "ވައިގެ", -22)])
sh(24, "and the rattling of steel sheets, her mind jolted with fright. \"Zail, we don't have much time.",
   [("metal_clang", "ތެޅޭ", -22)])
sh(25, "After what happened at Junction-9, soldiers will flood the whole of Sector 7. Once they know this box is missing, they'll search every home.\"")
sh(26, "Zail did not answer. He slowly went and took from a table drawer a small handmade device with many wires and chips connected to it.",
   [("metal_clang", "ވަތްގަނޑަކުން", -24)])
sh(27, "Then he plugged his special cable into a small port in the corner of the box. Suddenly a bright red warning lit up on the big monitor in the room.",
   [("electric_spark", "ގުޅާލިއެވެ", -22), ("power_up", "ދިއްލުނެވެ", -20)])
sh(28, "With it, a loud beeping began, sounding without pause.",
   [("alarm_beep", "ބީޕް", -16)])
sh(29, "[On the screen: WARNING — MILITARY-GRADE ENCRYPTION DETECTED. ATTEMPT 1 OF 3 — UNAUTHORIZED ACCESS WILL TRIGGER DATA WIPE.] Aira's breath caught in her throat.",
   [("gasp", "ތާށިވިއެވެ", -20)], hum=True)
sh(30, "\"Zail! We only have three chances!\" \"Calm down, child,\" said Zail, wiping the sweat from his forehead with the back of his hand as he ran his fingers over the keyboard.",
   [("keyboard_typing", "ކީބޯޑުގައި", -20)])
sh(31, "\"This encryption is a security algorithm that my team and I created twenty years ago.")
sh(32, "Marcus's people will only have changed a few codes in it.\" Zail's fingers danced over the keyboard as fast as lightning.",
   [("keyboard_typing", "ކީބޯޑުމަތީގައި", -18)])
sh(33, "Thousands of green numbers and letters streamed across the screen. When the first attempt failed and the screen turned red, both their hearts jolted.",
   [("alarm_beep", "ރަތްވި", -18), ("heartbeat", "ތެޅިގަތެވެ", -20)])
sh(34, "On the second attempt Zail entered another code. At that moment the power in the whole workshop cut out! In the pitch darkness, Aira's hand went to her own weapon.",
   [("power_down", "ކަނޑައިގެންނެވެ", -16), ("cloth_rustle", "ހަތިޔާރަށް", -22)], hum=True)
sh(35, "\"What happened?\" \"The backup generator is switching over...\" Zail quickly pulled a lever under the table. At once the screens lit up again,",
   [("metal_clang", "ދަމައިގަތެވެ", -20), ("power_up", "ދިއްލި", -18)])
sh(36, "and the beeping faded. And in the very last seconds, as Zail entered the final code, a big green message came up on the screen: [ACCESS GRANTED — DECRYPTING ARCHIVE...]",
   [("computer_beep", "އެންޓަރ", -18)], hum=True)
sh(37, "With a soft sound the lid of the box unlocked and opened. On the screen appeared live satellite data from the past fifteen years, and clear",
   [("box_unlock", "ތަޅުދޫވެ", -16)])
sh(38, "live video footage taken from different parts of the surface. Aira and Zail looked at the screen together. What their eyes were seeing was hard to believe;")
sh(39, "the two of them stood frozen, unable to move. In the golden light spreading from the monitor, Aira stood wide-eyed, unable to believe it.",
   hum=True)
sh(40, "What the screen showed was not the burning hell that the Council's leader Marcus shows them.")
sh(41, "Instead it showed a clear blue sky, deep green valleys, and clean rivers flowing between the trees.",
   hum=True)
sh(42, "The radiation meter readings running over those scenes were green — lower even than any level that could harm a human being.")
sh(43, "\"Is this... is this real?\" Aira's voice trembled. She slowly reached out and touched her finger to the green trees on the screen.")
sh(44, "\"Was the story we were told since we were small a lie? Is there no poison up there?\" Zail let out a deep breath.",
   [("sigh", "ނޭވާއެއް", -22)])
sh(45, "His eyes showed anger and deep sorrow. \"Over the past fifteen years the surface environment has recovered by itself")
sh(46, "and healed. But every week Marcus shows old recordings and computer-made fake visuals on the TV screens.")
sh(47, "He keeps the whole population locked in a prison of fear.\" \"Why would he do this, Zail?\"")
sh(48, "A tear fell from Aira's eye onto her cheek. \"Our parents, and thousands of people in this sector, in the dark —",
   [("sob_breath", "ކަރުނައިގެ", -24)], hum=True)
sh(49, "what is the point of all the pain we endure in sickness and hunger?\" Zail rose from his chair and spread both hands on the table.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(50, "\"The reason is power and slavery, Aira. As long as people live in fear of death, they will be grateful for the little food and little oxygen the government gives them, and they will obey.")
sh(51, "If they knew there was clean air on the surface, no one would obey Marcus's dark kingdom.")
sh(52, "There would be nobody left to work as slaves for the rich of the upper level.\" Aira clenched her teeth and bowed her head, her fist on the table.",
   [("soft_thud", "ގޮށްމުށުން", -22)], hum=True)
sh(53, "But at that moment Zail's eyes suddenly stopped on a red folder at the bottom of the screen.")
sh(54, "On that folder was the highest-level secret classification mark. \"Wait...\" Zail quickly moved the mouse and opened the file.",
   [("computer_beep", "ހުޅުވާލިއެވެ", -20)])
sh(55, "\"There's something more in here.\" One single phrase came up on the screen in big letters: [PROJECT CLEANSLATE: FINAL PHASE PROTOCOL]. As the file opened,",
   hum=True)
sh(56, "the blood drained from Zail's face. On the screen was a chart of Sector 7, and an animation showing red smoke spreading into the chart's main ventilation pipes.",
   hum=True)
sh(57, "\"What... what is this?\" Aira asked in alarm. Zail's lips were trembling. \"Aira...")
sh(58, "Marcus's plan isn't just a lie. On the golden jubilee day when the bunker turns fifty,")
sh(59, "after everyone on the upper level has gone up to the surface, it has been decided to release neurotoxin poison gas into Sector 7's ventilation system —",
   hum=True)
sh(60, "to wipe out everyone in Sector 7 at once!\" Aira's voice barely came out. \"Which day? When is that day?\"",
   [("gasp", "ނުނިކުތީ", -20)])
sh(61, "Zail pointed with a trembling finger at the date on the screen. The countdown timer showed the time remaining until zero.")
sh(62, "\"From today... only seven days are left!\" said Zail in a voice full of grief and fear. \"Seven days...\"",
   hum=True)
sh(63, "Aira's voice came out as a gasp into the silence of the room. Her legs gave way, and she had to grip the side of the table.",
   [("gasp", "ސިހުމަކުންނެވެ", -20)])
sh(64, "The seconds of the red countdown timer on the monitor kept counting down without any mercy.",
   [("heartbeat", "ގުނަމުންނެވެ", -20)])
sh(65, "Every second was a step taking thousands of innocent lives of Sector 7 towards the grave. The faces of the children,",
   hum=True)
sh(66, "the elderly, and the families wasting away in hard labour in the dark rose up in Aira's mind.")
sh(67, "\"They see us as rubbish,\" Zail struck the table with his fist. As the steel table rang out, his eyes blazed with burning anger.",
   [("metal_clang", "ޖަހައިލިއެވެ", -16)])
sh(68, "\"While the upper level goes up and enjoys its freedom, they want to wipe out every trace of Sector 7.")
sh(69, "Marcus wants to leave behind not one voice, not one complaint!\" \"We will not just submit to this, Zail!\"",
   hum=True)
sh(70, "Aira looked straight into Zail's eyes. Her fear was slowly turning into an unbreakable resolve.",
   hum=True)
sh(71, "\"We now hold the truth in our hands. We have proof that a clean world lies above. And Marcus's plan of mass murder is right here to see.")
sh(72, "All of Sector 7 has to know this truth.\" \"But how?\" Zail shrugged.")
sh(73, "\"The Council controls every communication system. The moment we go out into the streets and talk about this, the soldiers will kill us.")
sh(74, "And people won't even believe us.\" Aira took the encrypted device from the table and slipped it into her pocket.",
   [("cloth_rustle", "ކޮށްޕާލިއެވެ", -22)])
sh(75, "\"People will believe it when they see these videos with their own eyes. We have to get into Sector 7's main broadcasting tower,")
sh(76, "hijack the Council's TV frequency, and show this live feed to the whole bunker.\" Zail looked at Aira in amazement.")
sh(77, "It was a mission as dangerous as facing death itself. But from the courage and determination on Aira's face, even Zail's dead hopes came back to life.",
   hum=True)
sh(78, "\"If we're going to do that... we'll need more help,\" Zail said slowly. \"There is a secret resistance group operating in the bunker tunnels of Sector 7.")
sh(79, "We have to make contact with them.\" Just then, from outside the workshop came the sound of heavy boots and the shrill whine of metal detectors.",
   [("boots_march", "ބޫޓުތަކެއްގެ", -18), ("alarm_beep", "ޑިޓެކްޓަރުތަކުގެ", -22)])
sh(80, "Outside, red laser lights came in through the cracks around the door. \"They've found us!\" Zail whispered.",
   [("heartbeat", "ވިސްޕަރ", -20)], hum=True)
sh(81, "Aira took up her weapon and made ready. The seven-day countdown had begun not only as a fight to save the city, but as a war to defend their own lives!",
   [("metal_clang", "ނަގައި", -22)], hum=True)
SHOTS = S

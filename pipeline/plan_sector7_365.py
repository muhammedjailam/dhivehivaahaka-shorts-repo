"""Beat/shot plan for Sector 7 episode 365 — the prologue (used by plan_beats.py)."""

LOC = {
    "wasteland": "the burned surface of the Earth after a nuclear war, an empty ruined city skyline of broken towers on a flat grey ash plain, low heavy ash clouds",
    "bunker_gate": "a colossal round steel blast door set into the face of a dark rocky mountain, a wide concrete ramp leading up to it, the burned grey ash plain stretching away below",
    "bunker_stairs": "a vast dim underground machinery shaft inside a newly built bunker, a long steep steel staircase descending past giant pipes, pumps and generators into the dark depths",
    "cross_section": "a gigantic underground bunker seen in cross-section inside a deep shaft of dark rock two miles below the ground, seven stacked levels, a faint shaft of daylight high at the very top",
    "level1": "Level 1 'Udubburi', the luxurious top level of the bunker: a vast bright hall of white marble, glass walls and gold trim under a huge glowing artificial sun panel in the ceiling, indoor gardens with green trees and fountains, tables laden with real fruit",
    "s7_corridor": "a main corridor of Sector 7, the lowest level of the bunker: towering walls of rusted riveted steel plates streaked with dripping water, broken pipes overhead leaking murky green-brown waste into an open floor channel, puddles, scrap metal",
    "s7_machinery": "a cavernous hydraulic machinery hall in Sector 7: enormous rusted pistons, pumps and valve wheels, tangled pipes, steam vents, metal catwalks and grating",
    "ration_hall": "a cramped ration hall in Sector 7: a steel serving hatch in a rusted wall, long dented metal tables and benches, pipes along the low ceiling",
    "dormitory": "a cavernous workers' dormitory in Sector 7: endless rows of stacked bare steel bunks three high, narrow muddy walkways between them, damp rusted walls, a low dark ceiling of pipes",
    "engine_room": "the main engine room of Sector 7: huge humming turbines and thick riveted pipes that carry clean water and oxygen up to Level 1, round pressure valves with blank gauge faces, steam and heat haze, metal grating floor",
    "memory_home": "a cramped family living cell inside the bunker thirteen years ago: bare steel walls, a small table, a folded blanket on a narrow cot, a steel door ajar to a corridor",
    "alarm_corridor": "a long Sector 7 corridor of rusted steel walls with caged warning lamps fixed along both walls, pipes overhead, haze",
    "control_panel": "the Sector 7 engine-room control station: a large old wall-sized control console with a glowing schematic of pipe lines, switches and dials without markings",
    "death_zone_top": "the edge of the 'death zone' at the bottom of Sector 7: a narrow steel stairway descending from the engine room into pitch darkness, broken railings, drifting haze",
    "flooded_corridor": "a narrow flooded service corridor deep in the death zone: ankle-deep dark water over a floor of mud and scrap metal, cut electric cables dangling from the ceiling, water dripping from rusted walls, a thin greenish gas haze",
    "junction_door": "the deepest passage of the death zone: collapsed steel beams and fallen debris, thick smoke, and at the end a huge round riveted steel hatch door of Junction-9",
    "junction_pipe": "inside Junction-9, an enclosed cramped chamber at the very bottom of the bunker with a low rusted steel ceiling and close riveted walls, no view of any other level: a gigantic main oxygen pipe with a large jagged crack spewing white vapour, dark water bubbling across the grating floor, thick haze of gas all around",
}
MOOD = {
    "wasteland": "dusk-like gloom, a distant deep orange glow on the horizon under ash-grey clouds, cold blue-grey shadows, desolate, silent, no living thing",
    "bunker_gate": "ash-dark sky with a distant orange glow on the horizon, warm golden light spilling out of the open blast door, ominous, the end of the old world",
    "bunker_stairs": "dim amber work lights and sodium-orange glow from below, cold steel-blue shadows, oppressive, the start of servitude",
    "cross_section": "golden warm light on the top level fading to cold blue and finally to smoky rust-orange glow and red embers at the bottom, epic and ominous",
    "level1": "bright warm golden artificial sunlight, soft white glow, clean fresh air, luxurious and serene, a cold contrast to the levels below",
    "s7_corridor": "dim flickering yellow bulbs, cold teal shadows, toxic green haze, damp and rotting, hopeless",
    "s7_machinery": "dim yellowish caged bulbs, sodium-orange glow, steam haze, deafening and oppressive, grim",
    "ration_hall": "harsh single dim bulbs, grey-green cold light, drab and joyless",
    "dormitory": "very dim amber bulbs far apart, deep blue-black shadows, damp haze, weary and hopeless",
    "engine_room": "intense heat, amber and sodium-orange work lights, glowing heat haze, steam, sweat and exhaustion",
    "memory_home": "night thirteen years ago, a single warm bulb, soft hazy dream-like glow at the edges of the frame, tender and frightening",
    "alarm_corridor": "red alarm light flashing and flooding everything in red, deep black shadows, sudden panic",
    "control_panel": "red alarm light from above mixed with the glowing red schematic on the console lighting the faces, urgent",
    "death_zone_top": "red alarm light behind her fading into pitch-black darkness ahead, a single cold beam of her headlamp, lonely and brave",
    "flooded_corridor": "near darkness, cold blue-white beam of her headlamp, brief bright blue-white electric sparks reflected in the water, sickly green gas haze, freezing cold",
    "junction_door": "thick smoke lit by a dim red glow and the cold beam of her headlamp, the hatch door looming, exhausted resolve",
    "junction_pipe": "cold blue darkness broken by the bright white-orange flare of welding sparks, swirling vapour, tense and secretive",
}

AIRA_MASK = ("Aira wears an old battered half-face oxygen mask over her nose and mouth (her determined eyes visible above it), "
             "her charcoal hijab still fully covering her hair and neck, her ankle-length olive-brown coat")

BEATS = [
    dict(to=4, reason="episode opening: the nuclear war burns the surface (world-building narration)", loc="wasteland",
         visual="a completely deserted landscape: a vast empty ruined city skyline of broken towers on a grey ash plain, a distant deep orange glow on the far horizon under heavy ash clouds, drifting ash in the air; absolutely no people, no human figures, no silhouettes, no animals, no explosions shown",
         camera="extreme wide shot, horizon at mid-frame, the ash plain forming a calm lower third", amb="wasteland",
         sens="violence", safe="nuclear war shown only as a distant orange horizon glow over an empty ruined skyline; no mushroom cloud, no people"),
    dict(to=7, reason="new location: the rich and powerful enter the bunkers", loc="bunker_gate",
         visual="a long line of well-dressed wealthy people in long dark coats, the women in hijabs, walking up a concrete ramp into the open colossal round blast door glowing with warm gold light inside, seen from behind and small in the frame, the burned land and orange horizon glow behind them",
         camera="wide shot from below the ramp, the glowing door in the upper half, the grey ramp as the calm lower third", amb="wasteland"),
    dict(to=10, reason="new group and action: poor workers are brought in to run the machines as slaves", loc="bunker_stairs",
         visual="a line of thin poor men in ragged worn work clothes and long trousers descending a long steep steel staircase into the dark machinery depths, heads bowed, carrying tool bags, two stern guards in grey uniforms with empty hands watching from a landing above, giant pumps and pipes below glowing orange",
         camera="high-angle wide shot looking down the staircase, figures in the upper two-thirds, dark grating at the bottom", amb="bunker_machinery"),
    dict(to=12, reason="new location: 'The Sanctuary' near Bremen, two miles underground, divided into seven levels", loc="cross_section",
         visual="a breathtaking cutaway cross-section of the giant bunker in a rock shaft: seven stacked levels like floors of a vast building, the top level glowing gold and white with gardens, middle levels of grey corridors and storage halls, the bottom level a dark rusted smoky maze of machinery with tiny glowing lights, a faint shaft of daylight high above, no labels and no signs",
         camera="wide vertical cutaway view, the levels filling the frame top to bottom, dark rock at the very bottom", amb="bunker_machinery", transition="black"),
    dict(to=13, reason="new location: the luxurious upper Level 1 'Udubburi'", loc="level1",
         visual="elegant wealthy residents in cream and white long robes and coats, the women in light hijabs, strolling and relaxing in a bright marble garden hall under a glowing golden artificial sun, a fountain, crystal bowls of red apples, grapes and oranges on white tables, green trees",
         camera="wide shot, eye level, the people and the glowing ceiling in the upper two-thirds, the polished marble floor as a calm lower third", amb="upper_balcony"),
    dict(to=17, reason="new location: Sector 7, the living hell at the bottom", loc="s7_corridor",
         visual="the rusted steel corridor of Sector 7 in damp gloom, water dripping in streaks down the riveted walls, broken pipes overhead leaking murky green-brown sludge into a floor channel, toxic haze hanging in the air, two hunched workers in worn clothes walking away in the distance",
         camera="wide shot down the corridor, one-point perspective, wet floor in the lower third", amb="corridor_drip"),
    dict(to=21, reason="action/character change: the roaring machinery and the exhausted workers on 16-hour shifts", loc="s7_machinery",
         visual="gaunt, exhausted workers — thin men with hollow cheeks in sweat-soaked long-sleeved shirts and one woman in a dark hijab and long coat — straining together to turn a giant rusted valve wheel among enormous hydraulic pistons, their faces drained of hope, dim yellow caged bulbs swinging above, steam rising",
         camera="medium wide shot, faces in the upper half, the metal grating floor as a calm lower third", amb="bunker_machinery"),
    dict(to=23, reason="action change: the grey-paste rations", loc="ration_hall",
         visual="a queue of weary workers holding dented metal bowls at a steel hatch where a dull grey sticky paste is slopped in; in the foreground a gaunt old worker sits at a metal table staring blankly at the grey paste in his bowl, a spoon in his hand, his eyes empty; a woman in a dark hijab and long coat waits in the queue",
         camera="medium shot, the staring worker's face in the upper half, the metal table top as a calm lower third", amb="warehouse_crowd"),
    dict(to=26, reason="new location: the steel-bunk dormitory — daily routine and a world without sky", loc="dormitory",
         visual="endless rows of stacked bare steel bunks in a dim cavernous hall, tired workers sitting hunched on the edges of the bunks, a young worker lying on a top bunk staring up at the low dark ceiling of pipes where there is no sky, muddy walkway between the rows",
         camera="wide shot down the aisle between the bunks, the muddy walkway forming the lower third", amb="corridor_drip"),
    dict(to=28, reason="character introduced: Aira at work in the main engine room", chars=["aira"], loc="engine_room",
         visual="Aira, sweat on her forehead and a grease smudge on her cheek, straining with both hands on a huge spanner to tighten a bolt on a thick riveted pipe flange, squinting through heat haze and smoke, a heavy cutter tool hanging from her belt, huge turbines behind her",
         camera="medium shot, eye level, her face in the upper third, the grating floor below", amb="engine_room"),
    dict(to=29, reason="return to Level 1 for the contrast with the rich enjoying cool air", loc="level1", reuse="beat_005",
         visual="(reuse of beat_005) the bright luxurious Level 1 garden hall", amb="upper_balcony"),
    dict(to=32, reason="characters enter: the overseer bangs a pipe and threatens rations; Bashir flinches", chars=["aira", "bashir"], loc="engine_room",
         visual="Aira standing at a large round pressure valve with a blank gauge, staring at it without blinking; beside her old Bashir flinching, shoulders hunched, head bowed in fear; to the left a stern Council overseer in a grey-black uniform and visor cap strikes a pipe with a short plain steel rod, shouting, his free hand pointing at them; the overseer keeps well apart from them",
         camera="medium wide three-figure shot, faces in the upper half, the grating floor as a calm lower third", amb="engine_room",
         sens="other", safe="the overseer's threat is shown only as him striking a pipe and shouting; no one is touched or hit"),
    dict(to=35, reason="action change: the overseer has gone; Bashir whispers his warning, Aira's eyes burn", chars=["aira", "bashir"], loc="engine_room",
         visual="old Bashir on the left and Aira on the right standing on either side of a thick vertical pipe, a clear gap of more than an arm's length between them, not touching; Bashir glances sideways towards her and whispers with frightened, tired eyes, his head low; Aira looks straight ahead past the camera, her dark eyes burning with defiance and anger, jaw set, orange light from a turbine on her face",
         camera="medium two-shot, eye level, the two figures clearly separated by the pipe, faces in the upper half, a pipe rail and dark grating in the lower third", amb="engine_room",
         sens="other", safe="regenerated: first image had Bashir's shoulder pressed against Aira's; now separated by a pipe (no touching rule)"),
    dict(to=36, reason="action change: on her break Aira takes out her father's pendant", chars=["aira"], loc="engine_room",
         visual="Aira sitting exhausted on an upturned metal crate in a quieter corner of the engine room, pulling a small worn steel tag pendant on a thin chain out from the collar of her coat, gazing at it with tired, softened eyes, steam drifting behind her",
         camera="medium shot, slightly from the side, her face and hands in the upper half, the floor below", amb="engine_room"),
    dict(to=39, reason="flashback: the night thirteen years ago when her father put the pendant on her", chars=["malik"], loc="memory_home",
         visual="Malik kneeling on one knee and gently hugging his small 10-year-old daughter (a little girl in a plain long-sleeved ankle-length dress and a small light headscarf covering her hair) as he fastens a small steel tag pendant on a chain around her neck, his eyes wet and loving, her face puzzled and frightened; in the half-open doorway behind them two shadowy men in grey uniforms wait with empty hands",
         camera="medium shot, eye level at the girl's height, faces in the upper half, the steel floor below", amb="memory",
         transition="dissolve", sens="other",
         safe="father-daughter (mahram) gentle farewell hug, allowed; the men taking him are only shadows in the doorway"),
    dict(to=43, reason="back from the memory: close-up of the pendant code and her vow", chars=["aira"], loc="engine_room",
         visual="close-up of Aira's fingers tracing a small worn steel tag pendant resting in her palm, a faint engraved code too small to read on it; above it Aira's face, eyes shining with a quiet fierce resolve, amber light on her cheek, machinery blurred behind",
         camera="close-up, her eyes in the upper third and the pendant in her hands at mid-frame, dark coat fabric below", amb="engine_room",
         transition="dissolve"),
    dict(to=45, reason="scene change: the siren wails and red alarm lights flood the corridors", loc="alarm_corridor",
         visual="the rusted Sector 7 corridor suddenly bathed in flashing red light from caged alarm lamps along the walls, workers in worn clothes stopping and looking up in fear, one man covering his ears, haze glowing red",
         camera="wide shot down the corridor, the red-lit floor forming the lower third", amb="alarm_corridor"),
    dict(to=47, reason="action change: the control panel shows Junction-9's oxygen pipe has burst", chars=["aira", "bashir"], loc="control_panel",
         visual="Aira and old Bashir standing in front of the huge old control console, their tense faces lit red by a glowing abstract schematic of pipe lines on which one point deep at the bottom flashes bright red; Aira leaning forward, staring; Bashir shrinking back in fear; no letters or numbers anywhere",
         camera="medium shot from beside the console, faces in the upper half, the console edge as the lower third", amb="alarm_corridor"),
    dict(to=50, reason="action change: Aira masks up, shoulders her toolkit and faces the dark path to the death zone", chars=["aira"], loc="death_zone_top",
         visual=f"{AIRA_MASK}; she stands at the top of a narrow steel stairway, a heavy battered metal toolkit slung over her shoulder, a headlamp on her forehead, looking down with brave eyes into pitch darkness below, red alarm light glowing behind her",
         camera="medium wide shot from slightly below and in front, her face in the upper third, the dark stairway in the lower third", amb="alarm_corridor"),
    dict(to=54, reason="scene change: the descent through the cold flooded corridors with live sparking cables", chars=["aira"], loc="flooded_corridor",
         visual=f"{AIRA_MASK}; she wades carefully through ankle-deep dark water in a narrow corridor, one hand steadying on the wall, avoiding cut electric cables that hang from the ceiling and spit small blue-white sparks over the water ahead, mud and scrap metal under the water, her headlamp beam cutting through green haze",
         camera="medium wide shot from ahead of her, her face in the upper half, the dark water as the lower third", amb="corridor_drip",
         sens="other", safe="the danger of electrocution is shown only as sparks over the water ahead of her; nobody is hurt"),
    dict(to=58, reason="action change: climbing over debris she reaches the huge door of Junction-9", chars=["aira"], loc="junction_door",
         visual=f"{AIRA_MASK}; having climbed over collapsed steel beams and fallen debris, she stands exhausted but resolute before a huge round riveted steel hatch door rising through thick smoke, one hand reaching for its big wheel handle, toolkit on her shoulder, no markings on the door",
         camera="wide shot from behind and beside her, the hatch door filling the upper half, debris on the floor in the lower third", amb="corridor_drip"),
    dict(to=61, reason="scene change: at the burst main pipe of Junction-9 she starts welding", chars=["aira"], loc="junction_pipe",
         visual=f"{AIRA_MASK}; she kneels on the grating beside the gigantic cracked oxygen pipe spewing white vapour, dark water bubbling around her boots, holding a welding torch to the crack that throws a bright shower of white-orange sparks, her open toolkit beside her; she is completely alone, nobody else in the chamber",
         camera="medium shot from the side, her face and the sparks in the upper half, wet grating in the lower third", amb="bunker_machinery"),
    dict(to=64, reason="strong turning point: in the sparks' light she spots a black box hidden inside the pipe", chars=["aira"], loc="junction_pipe",
         visual=f"close-up over Aira's shoulder: {AIRA_MASK}; her wide startled eyes peer into the dark opening of the pipe crack, lit by the dying glow of welding sparks, where a rugged matte-black sealed case with a recessed keypad-like panel (no markings) is wedged deep inside",
         camera="close-up, her eyes in the upper third, the black case at mid-frame, dark pipe metal below", amb="bunker_machinery"),
    dict(to=69, reason="action change: she holds the box, sees her father's handwriting and remembers the pendant", chars=["aira"], loc="junction_pipe",
         visual=f"{AIRA_MASK}; she kneels holding the rugged matte-black case in both trembling gloved hands, having wiped the grime off its lid where faint scratched handwriting is etched (illegible, too small to read); her eyes are wide with shock and tears, and the small steel tag pendant hangs at her chest catching the light; she is completely alone, nobody else in the chamber",
         camera="medium close-up, eye level, her eyes in the upper third, the case at mid-frame, her coat and the dark floor below", amb="bunker_machinery",
         sens="other", safe="the handwriting and the pendant code are shown only as faint illegible scratches; no readable text"),
    dict(to=72, reason="action change: she hides the box in her toolkit, finishes the repair and slips away past the cameras", chars=["aira"], loc="junction_pipe",
         visual=f"{AIRA_MASK}; she kneels closing the latches of her battered metal toolkit with the black case hidden inside, the repaired pipe behind her with a freshly welded seam still glowing orange, glancing warily up at a small security camera with a red light on the wall above her; she is completely alone, nobody else in the chamber",
         camera="medium wide shot, eye level, her face and the camera in the upper half, the wet grating floor as a calm lower third", amb="bunker_machinery"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Fifty years ago, because of the most dangerous war ever fought between the nations of the world, the whole world burned to ashes.",
   [("wind_howl", "އަޅިއަށް", -22)])
sh(2, "The great powers of that time began using nuclear weapons to win the upper hand in the war. At first they used them in secret.")
sh(3, "Then they began openly using tactical nuclear weapons. And as some nations began to lose because of it, the very biggest nuclear weapons were used.",
   [("distant_boom", "ބޭނުންކުރިއެވެ", -22)])
sh(4, "No side won. The poisonous smoke and gas of the nuclear war turned the surface into an uninhabitable desert.",
   [("wind_howl", "ސަހަރާއަކަށް", -20)], hum=True)
sh(5, "When nuclear weapons began to be used, the rich of the world and the leaders of nations, in different regions of the world, prepared huge bunkers")
sh(6, "— underground shelters — stocked with enough food to survive in them for at least 50 years, with the systems and equipment needed to stay alive,")
sh(7, "installed huge machines in them, and began to settle there. Only the rich and politically powerful leaders could enter these bunkers.",
   [("metal_door", "ވަދެވެނީ", -18)])
sh(8, "However, in the last days of the war, to operate without pause the systems and huge machines installed there to keep these people alive,",
   [("power_up", "އޮޕަރޭޓު", -20)])
sh(9, "and to repair them, some lucky ones from among the poor were let into these places. But,",
   [("footsteps_pavement", "ވެއްދިއެވެ", -22)])
sh(10, "it would be no lie to say these people had to live in slavery. Four such bunkers were built in different corners of the world.")
sh(11, "One of them is 'The Sanctuary', built two miles beneath the ground near the city of Bremen in Germany.")
sh(12, "This place became a new world for humanity. But that world is divided into seven levels.")
sh(13, "While the rulers live a life of luxury on the topmost Level 1, 'Udubburi', with the golden light of an artificial sun, fresh air, real fruit and food,")
sh(14, "'Sector 7', at the very bottom, is a living hell full of rust, rot and cold, damp darkness.")
sh(15, "Here live the poor workers. While cold damp drops dripped ceaselessly from the vast rusted steel walls of Sector 7,")
sh(16, "all the waste water and toxic chemicals of the upper levels flow down through pipes and collect in this area.")
sh(17, "The air always hangs heavy with the bitter taste of rusting steel and the suffocating stench of dangerous chemicals.",
   [("steam_hiss", "ވަހެވެ", -22)])
sh(18, "While the endless roar of the heavy hydraulic machinery deep underground and the clanging of steel deafened the whole sector,",
   [("metal_clang", "ތެޅޭ", -18)])
sh(19, "the light of dim yellowish bulbs revealed only fearful scenes full of sorrow.")
sh(20, "The workers who live in this miserable place labour sixteen hours a day without a break on dangerous pipes and engines.")
sh(21, "Their bodies are dried up and wasted, and their faces show the deep marks of exhaustion and lost hope.")
sh(22, "Every day they try to ease their exhaustion by eating a sticky, bitter synthetic food called 'grey paste', handed out in the middle of the work.",
   [("cup_clatter", "ދޫކުރާ", -22)])
sh(23, "It does not just fill an empty stomach; because of it their minds grow dull, and their memories of the past and their feelings of rebellion fade,")
sh(24, "forcing them to shut their eyes to slavery. On steel bunks and muddy paths, this dark and cruel routine, repeated every day, is the only reality of life for the people of Sector 7.")
sh(25, "They have never known the freshness of clean air. Nor can they even imagine the blue colour of a sky above the ground.")
sh(26, "In the depths of this dark bunker, in the smoke of rusting steel, thousands of people struggled on with nothing but the bitter hope of surviving one more day.")
sh(27, "Inside Sector 7's main engine, where the heat had risen to the extreme, sweat was running down the forehead of 26-year-old Aira as she struggled to breathe through the thick smoke and chemicals.")
sh(28, "The sixteen hours Aira spends with heavy spanners and cutters, maintaining the huge pipes that carry clean water and oxygen up to Level 1, are a painful ordeal that drains all strength from her body.",
   [("metal_clang", "ސްޕެނާތަކާއި", -20)])
sh(29, "While the rich of the upper level enjoyed the comfort of cool, fresh air, hundreds of workers like Aira were being ground down deep under the earth to keep their luxurious life complete.")
sh(30, "Amid the deafening roar of the turbines, Aira stood watching the pressure valve in front of her without blinking.",
   [("engine_rev", "ޓާބައިންތަކުގެ", -20)])
sh(31, "Just then a harsh Council overseer came and struck a pipe with a steel rod, making it ring out. \"Hurry up!",
   [("metal_clang", "ޖަހައި", -14)])
sh(32, "If you stand there staring like that, I'll cut today's rations!\" At the overseer's harsh voice, Aira's old friend Bashir, working beside her, flinched and bowed his head in fear.",
   [("gasp", "ސިއްސައިގެން", -22)])
sh(33, "When the overseer had gone, Bashir said in a quiet voice: \"Aira, don't raise your eyes in front of them.")
sh(34, "To them we are nothing but scraps of iron, used and thrown away.\"",
   [("sigh", "ބައެއް", -22)])
sh(35, "But what burned inside Aira was not obedience; it was a flame of hatred for the injustice, and of revenge.")
sh(36, "Exhausted, during a short break from work, Aira took out from inside her shirt the steel pendant her father Malik had given her.",
   [("cloth_rustle", "ނެގީ", -24)])
sh(37, "Thirteen years ago, when Aira was only ten, her father, a brilliant engineer, was suddenly taken away to a secret project — and the frightening memories of that night came back fresh in her mind.")
sh(38, "That night, hugging Aira for the last time, her father had put that pendant around her neck. After that no news of her father ever came,",
   [("cloth_rustle", "ބައްދާލަމުން", -24)], hum=True)
sh(39, "and the Council declared him missing.",
   [("door_close", "ނިންމިއެވެ", -22)])
sh(40, "But the code '50.12.01' deeply engraved on that pendant is the only sign that keeps alive in Aira's heart the hope that her father is still alive.",
   hum=True)
sh(41, "Is this code the key to a secret door out of the dark corners of Sector 7? Or the truth of a great secret the rulers of Level 1 are trying to hide?")
sh(42, "Standing in the noise of the work, running her fingers over the code, Aira made a promise to herself.")
sh(43, "To find out what happened to her father, to break the chains of this slavery and to see the light of the real world, she would face any danger.",
   hum=True)
sh(44, "Suddenly the deep darkness of Sector 7 was filled with the deafening wail of a powerful siren.",
   [("siren", "ސައިރަންގެ", -14)])
sh(45, "As the red lights fixed on the corridor walls began flashing, the whole area was bathed in a frightening red light.",
   [("alarm_beep", "ނިވިދިއްލެން", -20)])
sh(46, "The main control panel showed that the main oxygen pipe of 'Junction-9', at the very bottom of the sector, where no one dares to set foot, had burst.",
   [("computer_beep", "ޕެނަލުން", -20)])
sh(47, "As the air pressure fell to a dangerous level, the heavy duty of saving the lives of the whole sector rested on a decision to be made within a few seconds.",
   [("heartbeat", "ސިކުންތުކޮޅެއްގެ", -20)])
sh(48, "Without the slightest hesitation, Aira pulled her old, worn oxygen mask over her face and tightened it. After slinging her heavy toolkit over her shoulder,",
   [("breath", "މާސްކް", -20), ("metal_clang", "ޓޫލްކިޓް", -22)])
sh(49, "she looked with a brave gaze at the dark path ahead. It was the dangerous depth that everyone calls the 'death zone'.")
sh(50, "In that lonely place where nothing could be heard but her own breathing inside the mask, her heart beat faster, yet she had no thought of turning back.",
   [("breath_heavy", "ނޭވާގެ", -18), ("heartbeat", "ތެޅުން", -18)], hum=True)
sh(51, "The further down she went, the more the temperature dropped, and she felt on her body the cold damp of the drops falling from the walls.")
sh(52, "The floors of the narrow corridors were full of mud and scrap metal.")
sh(53, "With electric sparks running from cut cables into the pools of water, a single slip of the foot would be like falling straight onto the lips of death.",
   [("electric_spark", "ވިހިދުގެ", -18)])
sh(54, "The smell of the poisonous gas drifting in the air seemed to seep through the mask and cloud her mind.",
   [("steam_hiss", "ގޭހުގެ", -22)])
sh(55, "Every step forward through the darkness she took with her life in her hands. Over collapsed steel",
   [("metal_clang", "ގިރި", -20)])
sh(56, "and fallen obstacles she climbed, while Aira's hands and feet grew as cold as ice. Even so,")
sh(57, "the flame of hope burning in her heart did not go out. At last, with great courage, she completed that dangerous journey")
sh(58, "and, through the smoke and the din, reached the huge door of Junction-9.",
   [("metal_door", "ދޮރާއްޓާ", -18)])
sh(59, "Aira stepped towards the main pipe of Junction-9 with great caution. All around was a thick layer of poisonous gas and oxygen vapour.",
   [("steam_hiss", "ދުންތަކުގެ", -18)])
sh(60, "As water bubbled under her feet, the loud roar from the big crack in the pipe echoed through the whole area.",
   [("splash", "ބޮކިޖަހަމުން", -20)])
sh(61, "Breathing with the help of the mask on her face, Aira took out her welding tools and began that dangerous work.",
   [("weld_hiss", "ވެލްޑިންގ", -16)])
sh(62, "As the sparks of fire flew, she caught a small glimpse of something hidden inside the pipe.",
   [("weld_hiss", "ވިހުރިގެން", -18)])
sh(63, "What caught Aira's eye was an unusual black box wedged in a dark corner of the pipe.",
   [("gasp", "އަޅައިގަތީ", -22)])
sh(64, "From its military-grade encrypted features she knew at once it was no ordinary thing. Picking up the box with trembling hands,",
   [("metal_clang", "ނަގައި", -22)])
sh(65, "as she wiped the dirt from its top, Aira felt as if her heart had stopped. Carved and etched on the outside of the box was her father's handwriting.",
   [("heartbeat", "ހުއްޓުނު", -18)], hum=True)
sh(66, "\"The truth is not buried.\" On seeing these words, what instantly came to Aira's mind was the pendant around her neck.",
   hum=True)
sh(67, "Aira became certain that the secret code '50.12.01' on the pendant at her neck was the key to opening this box.")
sh(68, "Keeping any information about the surface is the gravest crime in this bunker, punishable by death.")
sh(69, "But an unbreakable resolve rose in Aira's heart to uncover the secret behind her father's disappearance and the truth tied to the survival of all humanity.",
   hum=True)
sh(70, "Aira quickly hid the box at the very bottom of her toolkit and carefully shut it. After finishing the repair of the crack in the pipe,",
   [("lock_click", "ބަންދުކޮށްލިއެވެ", -20)])
sh(71, "she got ready to continue on her way unseen by the cameras around her. Though she knew the journey ahead was full of fear and challenges,",
   [("footsteps_pavement", "ދަތުރު", -24)])
sh(72, "Aira was fully determined to find the truth her father had left behind.", hum=True)
SHOTS = S

"""Beat/shot plan for Sector 7 episode 406 (used by plan_beats.py).
The ambush at the Sector 1 storage hall. Most violent episode of the arc: every act of violence is replaced by the
series bible's safe substitutions (fear, aftermath without wounds, abstract light streaks and smoke, empty hands)."""

LOC = {
    "tunnel_road": "a wide rough tunnel road deep in Sector 7 of an underground bunker city, rusted riveted steel walls, thick pipes along the ceiling, oily puddles on cracked concrete, drifting steam, dim flickering bulbs",
    "lift_complex": "the approach to the Sector 1 storage complex deep underground: a wide concrete forecourt ending at a colossal riveted steel door set in a towering rust-streaked steel wall, high dark gantries and catwalks above it, thick pipes and vent grilles in the walls",
    "side_tunnel": "a narrow damp side tunnel in Sector 7, rusted pipes dripping water along curved steel walls, puddles on the grated floor, a single caged bulb",
    "vent_duct": "the inside of a large square vertical steel ventilation duct, rusty riveted walls streaked with damp, condensation drops, faint light from a grille high above",
    "door_blast": "the colossal steel door of the Sector 1 storage complex, now buckled and torn open, the concrete forecourt in front of it with parked heavy vans",
    "catwalk": "a narrow steel catwalk bridge with railings high under the ceiling of a vast underground storage hall, a loose ventilation grille hanging open behind it, the enormous hall stretching below",
    "hall": "the vast clean storage hall of Sector 1: towering steel shelves stacked with supplies, crates of clear bottled water, open containers heaped with red apples, sacks of rice, a row of glass-fronted refrigerators holding fresh fish on ice, polished concrete floor, a gigantic closed lift gate at the far end, a thick glass control room glowing blue on one side",
    "hall_chaos": "the vast Sector 1 storage hall during the ambush: shattered skylights high in the ceiling, ropes hanging down, overturned crates and scattered supplies on the concrete floor, thick drifting smoke",
    "emergency_exit": "the far back corner of the Sector 1 storage hall: a narrow steel emergency door in a concrete wall, stacked crates beside it, smoke drifting across",
    "hall_after": "the Sector 1 storage hall in the aftermath: haze and dust settling, overturned crates, spilled apples and scattered boxes on the concrete floor, ropes hanging from broken skylights",
}
MOOD = {
    "tunnel_road": "underground night, harsh white van headlights cutting through steam, amber work lights, deep teal shadows, wild excited energy",
    "lift_complex": "underground, cold white floodlight on the door, deep blue-black shadows above, a faint red indicator glow, ominous silent menace",
    "side_tunnel": "underground, dim amber caged bulb and the soft green glow of a handheld screen, cold teal shadows, urgent and breathless",
    "vent_duct": "underground, near darkness, a dim red glow from a small device lighting her face from below, cold steel-blue edges, claustrophobic tension",
    "door_blast": "underground, a huge cloud of grey smoke and dust lit orange-amber by work lights and white headlights from behind, chaotic",
    "catwalk": "underground, cold white industrial light rising from below through drifting smoke, amber rim light on faces, breathless shock",
    "hall": "underground, bright clean white industrial light and a soft gold glow over the abundance, cool blue glow from the glass room, a cruel contrast with Sector 7's grime",
    "hall_chaos": "underground, flashing abstract streaks of red and blue light through thick smoke, flickering darkness, panic",
    "emergency_exit": "underground, a red emergency light over the door, smoke and flickering blue-red streaks behind, sly escape",
    "hall_after": "underground, cold grey-white light through settling smoke and dust, faint red emergency glow, bleak silence",
}

BEATS = [
    dict(to=4, reason="episode opening: the Revival vans race through Sector 7 towards the lift gate", loc="tunnel_road",
         visual="three heavy battered armoured vans speeding one after another through the wide steam-filled tunnel road towards the camera, harsh headlights blazing, young Revival men in worn jackets leaning out of the open side doors with raised fists, shouting with wild joy; their hands are empty",
         camera="wide low-angle shot, the vans in the upper two-thirds, the wet concrete road as a calm lower third",
         amb="bunker_machinery", sens="violence",
         safe="'raising weapons' shown as raised empty fists; no weapons visible"),
    dict(to=6, reason="scene change: the storage complex and the death trap prepared by Kyle's soldiers", loc="lift_complex",
         visual="the colossal sealed steel door of the storage complex at the end of an empty concrete forecourt, and high above it on a dark gantry a row of motionless commando silhouettes in black full armour and helmets with dark visors, waiting in the shadows, hands empty at their sides",
         camera="wide shot, low angle, the gantry and silhouettes in the upper third, the empty forecourt as the calm lower third",
         amb="storage_hall", sens="violence", safe="the waiting ambush shown as still silhouettes with empty hands; no weapons"),
    dict(to=11, reason="characters and scene change: Aira and Zail chase the vans and find the secret vent route", chars=["aira", "zail"], loc="side_tunnel",
         visual="Aira standing in a narrow dripping tunnel holding a small rugged black communicator whose screen glows with an abstract green line map without any text, pointing at it with determination; Zail an arm's length beside her, bent forward breathless with one gloved hand on the rusted wall, glasses glinting; far behind them the red tail lights of vans fading away",
         camera="medium shot, eye level", amb="corridor_drip"),
    dict(to=15, reason="action change: they open a vent hatch and climb up the shaft; Kyle's message in her mind", chars=["aira", "zail"], loc="vent_duct",
         visual="looking up inside a narrow vertical steel ventilation duct: Aira climbing upward with her boots braced against the rusty walls and hands on the rivets, her ankle-length coat and hijab neat, her determined face lit from below by the dim red glow of the communicator clipped to her coat; Zail climbing below her with a gap between them, his round glasses catching the light",
         camera="low angle looking up the shaft, faces in the upper half, dark duct walls framing a calm lower third", amb="vent_shaft"),
    dict(to=17, reason="action and scene change: through the grille they see the vans arrive and the youths at the steel door", chars=["aira"], loc="lift_complex",
         visual="over Aira's shoulder as she peers down through a vent grille high in the wall: far below, heavy vans parked with headlights on, dozens of young Revival men in worn jackets crowding around the colossal steel door, stacking heavy gas cylinders against its base; Aira's tense face in profile in the upper part of the frame",
         camera="high-angle over-the-shoulder shot looking down", amb="storage_hall", sens="violence",
         safe="the explosive charges are shown only as stacked gas cylinders; no wires, fuses or explosives"),
    dict(to=19, reason="action change: the door is blasted open, the youths storm in, Brent appears with a bandaged head", chars=["brent"], loc="door_blast",
         visual="the buckled steel door torn open with a huge cloud of grey smoke and dust billowing out, young men in worn jackets running into the smoke with raised fists, figures small and far back; behind them, striding out of the haze, tall Brent with a clean white bandage wrapped around his head and a cold grim face",
         camera="wide shot from above, slightly high angle", amb="storage_hall", sens="violence",
         safe="the blast shown as billowing smoke and dust from a buckled door, figures far back, nobody hurt"),
    dict(to=23, reason="action and location change: they kick out the grille, land on the catwalk and look down", chars=["aira", "zail"], loc="catwalk",
         visual="Aira and Zail crouching on the narrow steel catwalk high above the vast hall, the kicked-out vent grille hanging behind them, gripping the railing and staring down through drifting smoke; Aira's hand pressed to her chest, her breath caught in shock; Zail at an arm's length beside her",
         camera="medium shot, slightly low angle, the hall dropping away below", amb="storage_hall", sens="other",
         safe="'Aira held Zail's arm' shown as her turning urgently to him at an arm's length; no touching"),
    dict(to=27, reason="new view: the upper level's wasted abundance in the storage hall", loc="hall",
         visual="the vast storage hall seen from high above, an empty steel railing in the near foreground with nobody on it: towering shelves stacked with crates of clear bottled water, open containers heaped with shining red apples, sacks of fragrant rice, a long row of glass-fronted refrigerators holding fresh fish on ice; tiny figures of young Revival men frozen in amazement in the aisles below, smoke drifting at the entrance; no text on any box",
         camera="wide high-angle establishing shot", amb="storage_hall"),
    dict(to=29, reason="action change: the starving youths fall on the food, weeping with joy", loc="hall",
         visual="young Revival men in worn jackets and a few young women in hijabs kneeling among opened crates on the hall floor, holding red apples and bread, eating hungrily, tears of joy on their thin faces, some laughing and shouting with arms raised",
         camera="medium wide shot, eye level", amb="storage_hall"),
    dict(to=32, reason="focus change: Aira spots the glowing blue central terminal — her chance to find her father's records", chars=["aira", "zail"], loc="catwalk",
         visual="Aira on the catwalk pointing across the hall towards a thick glass control room glowing bright blue with a large terminal of abstract light panels and no text, her eyes wide with sudden hope, whispering; Zail an arm's length beside her, frowning and looking down into the hall",
         camera="medium shot over the railing, the glowing glass room in the background", amb="storage_hall"),
    dict(to=34, reason="characters change: the only people on duty are unarmed lab and medical staff, terrified", loc="hall",
         visual="a small group of unarmed laboratory and medical staff in white coats huddled together against a pale wall of the hall, crouching, their hands raised in fear and pleading, frightened faces; a clipboard on the floor beside them",
         camera="medium wide shot, eye level", amb="storage_hall"),
    dict(to=36, reason="character enters: Brent strides in through the main door and gives the cruel order", chars=["brent"], loc="hall",
         visual="Brent striding in through the blasted doorway with haze swirling behind him, a perfectly clean spotless plain white bandage wrapped around his forehead, cold merciless narrow eyes, one arm thrust forward commanding; several hard-faced young men in worn jackets following behind him, hands empty",
         camera="medium low-angle shot", amb="storage_hall", sens="violence",
         safe="the order to kill shown only as his commanding gesture and cold face; no weapons"),
    dict(to=38, reason="action change: the attack on the unarmed staff (massacre) shown only through shadows and fear", loc="hall",
         visual="huge looming shadows of advancing men cast across a pale wall above the huddled white-coated staff, who cover their faces in terror; the attackers themselves stay out of frame; a dropped clipboard and an overturned crate with apples rolling on the clean floor in the foreground; nobody is hurt",
         camera="medium wide shot, eye level", amb="storage_hall", sens="violence",
         safe="massacre replaced by looming shadows on the wall, terrified staff covering their faces, a dropped clipboard and spilled apples; no blades, no blood, no bodies"),
    dict(to=39, reason="action change: the Sector 7 youths recoil in horror", loc="hall",
         visual="young Revival men and a young woman in hijab stumbling backwards in horror among overturned crates, apples tumbling from their hands, eyes wide, hands over their mouths; spilled red apples and a dropped clipboard on the floor in the foreground",
         camera="medium wide shot, eye level", amb="storage_hall", sens="violence",
         safe="aftermath without wounds: spilled apples, overturned crates, a dropped clipboard and horrified faces"),
    dict(to=41, reason="action change: Aira jumps down the stairs and confronts Brent", chars=["aira", "brent"], loc="hall",
         visual="at the foot of a steel staircase Aira standing an arm's length in front of Brent, shouting at him and pointing at his face, her eyes blazing with fury; Brent towering over her with a bandaged head, throwing his head back in a mocking laugh; they do not touch",
         camera="medium two-shot, eye level", amb="storage_hall", sens="violence",
         safe="'she grabbed his arm' shown as her stepping in front of him and pointing/shouting; no touching"),
    dict(to=45, reason="action change: Brent strikes Aira and she falls to the floor", chars=["aira", "brent"], loc="hall",
         visual="Aira on the concrete floor propped on one arm, the back of her other hand near her mouth, looking up with furious defiant eyes; Brent standing a few steps away above her, teeth gritted, eyes cold and inhuman; her coat and hijab neat; no wound",
         camera="medium shot, slightly high angle from behind Brent's shoulder", amb="storage_hall", sens="violence",
         safe="the blow is not shown; Aira on the floor with a hand near her mouth and furious eyes; no blood, no wound"),
    dict(to=47, reason="the story returns to the frozen, horrified youths", reuse="beat_014", loc="hall",
         visual="(reuse of beat_014)", amb="storage_hall", sens="violence",
         safe="'fresh blood on the floor' shown as the earlier aftermath image: spilled apples, overturned crates, a dropped clipboard"),
    dict(to=48, reason="the story returns to Aira facing Brent: his cunning smile reveals the trap", reuse="beat_015", loc="hall",
         visual="(reuse of beat_015)", amb="storage_hall"),
    dict(to=51, reason="action change: the skylights shatter and commandos rappel in", loc="hall_chaos",
         visual="looking up at the high ceiling of the hall: big skylights bursting apart in a glittering rain of glass shards, and black-clad commandos in full armour with dark-visored helmets sliding down long ropes through the openings, their hands gripping only the ropes; haze and red-blue light below",
         camera="dramatic low-angle wide shot looking up", amb="chaos_hall", sens="violence",
         safe="the commandos' weapons are never shown: hands on the ropes only"),
    dict(to=53, reason="action change: laser fire floods the hall; the youths become prey", loc="hall_chaos",
         visual="abstract streaks of red and blue light slicing through thick smoke across the vast hall, dark silhouettes of young people ducking and running away from the camera into the haze, overturned crates; nobody is hit",
         camera="wide shot, eye level", amb="chaos_hall", sens="violence",
         safe="laser fire shown as abstract red and blue light streaks and smoke, silhouettes running away; nobody hit, no bodies"),
    dict(to=55, reason="location and action change: Brent flees through the emergency door with food and document cases", chars=["brent"], loc="emergency_exit",
         visual="Brent, a perfectly clean spotless plain white bandage wrapped around his forehead, slipping through a narrow steel emergency door, glancing back with a sly cold look, two of his men behind him carrying sealed food crates and black document cases, smoke and red-blue streaks of light behind them",
         camera="medium shot, eye level", amb="chaos_hall"),
    dict(to=57, reason="characters change: a wounded boy falls before Aira and clings to her", chars=["aira"], loc="hall_chaos",
         visual="a frightened thin boy of about twelve in a grey hoodie on his knees on the floor, clinging with both hands to the hem of Aira's coat and looking up at her begging for help; Aira bending down towards him with concern and resolve, smoke and red-blue streaks of light around them; no wound on the boy",
         camera="medium shot, eye level", amb="chaos_hall", sens="violence",
         safe="the wounded boy shown only as a frightened boy clinging to her coat; no wound, no blood"),
    dict(to=59, reason="action change: she carries the boy and is surrounded by four commandos", chars=["aira"], loc="hall_chaos",
         visual="Aira standing still in the smoke with the frightened boy in the grey hoodie carried over her shoulder, her face defiant, surrounded at a distance by four commandos in black full armour and dark-visored helmets, the bright white beams of their flashlights fixed on her; their hands hold only flashlights",
         camera="medium wide shot, eye level, Aira at the centre", amb="chaos_hall", sens="violence",
         safe="laser guns aimed at her head shown as flashlight beams; no weapons"),
    dict(to=61, reason="action change: Aira is struck down and cuffed", chars=["aira"], loc="hall_chaos",
         visual="Aira kneeling on the concrete floor with her hands behind her back in heavy steel restraints, her head lowered but eyes looking up and ahead defiantly, armoured commandos with dark visors standing around her with empty hands, smoke drifting; her coat and hijab neat",
         camera="medium shot, eye level", amb="chaos_hall", sens="violence",
         safe="the rifle-butt blow is not shown: only Aira kneeling in restraints surrounded by armoured figures with empty hands; nobody touches her"),
    dict(to=62, reason="character enters: Commander Kyle walks out of the smoke", chars=["kyle"], loc="hall_chaos",
         visual="Commander Kyle walking slowly out of a thick cloud of smoke and dust, tall and upright in his black high-collared uniform with silver medals, black gloves, calm cold face, red and blue haze behind him; his hands empty",
         camera="medium low-angle shot, full figure", amb="chaos_hall"),
    dict(to=64, reason="scene change: the aftermath of the ambush across the hall", loc="hall_after",
         visual="a wide desolate view of the hall in settling smoke: groups of young Sector 7 rebels sitting on the floor with their hands on their heads, guarded by commandos in black armour holding riot shields; overturned crates, spilled apples and scattered boxes all over the floor; no bodies, nobody hurt visibly",
         camera="wide shot, high angle", amb="chaos_hall", sens="violence",
         safe="the dead and wounded are never shown: only arrested youths sitting with hands on heads and scattered crates and apples"),
    dict(to=67, reason="action change: Kyle stands over the cuffed Aira with a mocking smile; she realises Brent's betrayal", chars=["kyle", "aira"], loc="hall_after",
         visual="Aira kneeling on the floor in steel restraints in the foreground, looking up with horror and defiance; Commander Kyle standing two steps in front of her, looking down at her with a faint mocking smile and merciless eyes; smoke behind them",
         camera="medium two-shot, low angle from behind Aira's shoulder towards Kyle", amb="chaos_hall"),
    dict(to=69, reason="action change: Aira is taken upward as a valuable prisoner", chars=["aira"], loc="hall_after",
         visual="Aira in steel restraints walking between two commandos in black armour who walk beside her without touching her, towards the giant lift gate now opening with a cold white light pouring down from above; she looks back over her shoulder into the smoky hall, searching in fear; seen from behind at a distance",
         camera="wide shot from behind, the lift gate and light in the upper half", amb="storage_hall",
         sens="other", safe="'dragged' shown as escorted between two commandos; nobody touches her"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The roar of heavy vans speeding through the narrow, damp roads of Sector 7 echoed across the whole area.",
   [("engine_rev", "އިންޖީނުގެ", -16)])
sh(2, "Inside the vans, more than a hundred young men of 'Revival', filled with joy and passion, were raising their weapons and shouting at the top of their voices.",
   [("crowd_roar", "ހަޅޭއްލަވަ", -20)])
sh(3, "In their hearts were the dark feelings of escaping generations of slavery and hunger, and of tearing the upper level to pieces.")
sh(4, "They were heading for the main lift gate of Sector 1, the only way up to the upper levels.")
sh(5, "But the truth they did not know was that the lift could only be reached through the heavily secured main storage complex,")
sh(6, "and that Commander Kyle's own soldiers had prepared a death trap there. At that very moment,",
   [("heartbeat", "ދަންމައްޗެއް", -20)])
sh(7, "after striking Brent on the head and knocking him down, Aira and Zail were running after those vans. \"We're too late!\"",
   [("footsteps_pavement", "ދުވަމުން", -20)])
sh(8, "Zail said, catching his breath. \"There isn't much time left before they reach the lift complex!\"",
   [("breath_heavy", "ނޭވާ", -20)])
sh(9, "\"If we go by the main road we'll never catch up with them,\" Aira said, looking at the military communicator in her bag.",
   [("computer_beep", "ކޮމިއުނިކޭޓަރަށް", -22)])
sh(10, "She looked at the secret chart on its screen and pointed with her finger. \"There are secret ventilation ducts from here going up.")
sh(11, "It's a route that connects directly to the main hall of the storage where the main lift gate is. We can get there before they go in!\"")
sh(12, "At once they pulled off the door of a huge steel ventilation duct and plunged inside. The inside of those ducts was extremely damp,",
   [("metal_clang", "ނައްޓާލައި", -18)])
sh(13, "full of rust and eerie noises. As they climbed up with difficulty, bracing their feet against the steel walls of the duct, Commander Kyle's cruel message kept circling in Aira's mind:",
   [("vent_knock", "އަޑުތަކުން", -22)])
sh(14, "[FROM: COMMANDER KYLE — STATUS: AMBUSH READY AT SECTOR-1 ELEVATOR GATE. BRING THEM ALL. NO SURVIVORS.]",
   [("computer_beep", "COMMANDER", -22)])
sh(15, "A treacherous trap planned to wipe out the whole Revival army at once. This was not a way up to the upper level; this was a massacre.",
   hum=True)
sh(16, "The moment they reached the space above the main door of the storage through the ducts was the moment the youths' vans arrived below and stopped.",
   [("engine_rev", "ވޭންތައް", -22)])
sh(17, "The only door into the main lift area was the storage's thick steel door. The youths got out and began fixing powerful explosives to that door.",
   [("metal_clang", "ހަރުކުރަން", -22)])
sh(18, "3... 2... 1... Kaboom! With a mighty blast the whole area shook. The door shattered and fell to the ground,",
   [("distant_boom", "ކަބޫމް", -18)])
sh(19, "and as the youths charged inside through the smoke, shouting, Aira saw through the duct's vent Brent coming in behind them with a bandage on his head.",
   [("crowd_roar", "ހަޅޭއްލަވަމުން", -20)])
sh(20, "He had got up off the ground and come to lead these people into death. Aira held on to Zail's arm. \"We have to stop them...",
   hum=True)
sh(21, "now!\" After kicking out the steel grating of the vent, Aira and Zail jumped down onto the steel bridge above the main storage.",
   [("metal_clang", "ކޮށްޕާލުމަށްފަހު", -18), ("soft_thud", "ފުންމާލީ", -22)])
sh(22, "It was a high place from which every corner of the storage could be seen clearly. When they looked down through the thick smoke left by the blast,")
sh(23, "the sight they saw made Aira hold her breath.",
   [("gasp", "ނޭވާ", -20)])
sh(24, "Piled up in that huge storage in front of the giant lift gate to the upper levels was a wasteful wealth that the poor people of Sector 7 had never seen in their whole lives.")
sh(25, "It was what the upper level threw away every day as leftovers. Crates of clean, sweet water sealed in glass bottles.")
sh(26, "Bright red fresh apples spilling from containers, and real fragrant basmati rice.")
sh(27, "And real kinds of fish piled up in refrigerated cabinets. When the youths who had come to take the lift gate saw this, it was as if they forgot all about the war.")
sh(28, "Those poor people, who had lived in hunger for so many years, threw themselves onto the food boxes like madmen.",
   [("crowd_roar", "ވެއްޓިގަތެވެ", -22)])
sh(29, "Stuffing fruit and food into their mouths, they began crying and shouting with joy. They thought they had won their rights.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(30, "But what caught Aira's eye was the blue-glowing 'Level 3 Central Terminal' inside a thick glass room on one side of the storage.",
   [("computer_beep", "ދިއްލިފައި", -22)])
sh(31, "It was the only chance to find her father's secret records. \"Zail, look!\" Aira whispered. \"There's the terminal.",
   hum=True)
sh(32, "I have to get there... but if we don't get everyone out of here, they'll all die!\" Zail said, looking into the storage.")
sh(33, "\"But the ones guarding this place are ordinary people with no weapons. They're scared to death.\" And in truth,")
sh(34, "the ones on duty in the storage were unarmed ordinary laboratory workers and medical staff. They were crouched against the wall, begging for their lives.",
   [("sob_breath", "އާދޭސްކުރާ", -22)])
sh(35, "Suddenly Brent came in through the main door of the storage. Though there was a bandage on his head, his eyes shone with a cruel, inhuman gleam.",
   [("footsteps_pavement", "ވަދެގެން", -20)])
sh(36, "This was the first step of the crime he had planned, before the soldiers' trap began. \"Let no one go! Everyone on the upper level is a criminal.")
sh(37, "Kill them all!\" Brent ordered his close, hardline supporters loudly. At Brent's order, his men fell upon the unarmed, helpless staff.",
   [("crowd_panic", "ތަޅައިގަތެވެ", -22)])
sh(38, "Ignoring their pleas, they began to cut them down with sharp blades. Within seconds, pools of red blood spread across the floor.",
   hum=True)
sh(39, "The ordinary youths of Sector 7, who had been eating, startled and stepped back in fear. This was not the freedom they wanted; this was a great massacre.",
   [("crowd_gasp", "ސިހި", -20)], hum=True)
sh(40, "\"Stop! Brent, this is not what we came to do!\" Aira jumped down the steel stairs,",
   [("metal_clang", "ފުންމާލައި", -20)])
sh(41, "went straight up in front of Brent and grabbed his arm and pulled. With a mocking laugh, Brent")
sh(42, "turned and struck Aira hard across the face. Aira reeled and fell to the floor. \"This is revenge, Aira!\"",
   [("soft_thud", "ޖެހިއެވެ", -22), ("cloth_rustle", "ވެއްޓުނެވެ", -22)])
sh(43, "Brent ground his teeth. \"No one on the upper level is innocent. Today we'll drink their blood!\"")
sh(44, "Wiping the blood from her mouth with the back of her hand, Aira, who had fallen to the floor, struggled to get up quickly.",
   [("breath_heavy", "ތެދުވަން", -22)], hum=True)
sh(45, "In Brent's cruel eyes she saw a creature in whom the last spark of humanity was gone.")
sh(46, "The whole floor of the storage was covered in the fresh blood of the medical staff. The ordinary youths of Sector 7 stood frozen in fear,")
sh(47, "having dropped the food boxes and stepped back. \"Brent, you brought all these people here to kill them!\" Aira screamed. \"The soldiers are coming right now!")
sh(48, "This is a trap!\" On Brent's face was a cunning smile. Seeing that he was not worried at all, Aira was certain he had planned this trap directly with Commander Kyle.",
   hum=True)
sh(49, "At that very second, the big vents and windows in the storage's high ceiling exploded all at once.",
   [("glass_break", "ގޮވައިގެން", -16)])
sh(50, "As glass and steel shards rained down, a force of black-clad commando soldiers came sliding down on ropes from above,",
   [("cloth_rustle", "އެލިގެން", -20)])
sh(51, "armed with the most modern weapons. \"Ambush!\" someone screamed at the top of his voice. Pew! Pew! Pew!",
   [("gasp", "ހަޅޭއްލަވައިގަތެވެ", -20), ("energy_zaps", "ޕިއު", -22)])
sh(52, "The blue and red fire of laser guns lit up the whole storage. Without any warning, without any mercy, the soldiers' laser attacks were aimed at the unarmed youths of Sector 7.",
   [("energy_zaps", "ލޭޒަރ", -22)])
sh(53, "As they fell one upon another, the whole place echoed with screams and cries. Those poor people, who had come hoping to rise through the lift gate, became prey.",
   [("crowd_panic", "ހަޅޭކާއި", -20)], hum=True)
sh(54, "Brent drew back at once. With his close men, he took the most valuable food boxes and the secret document cases in the storage,")
sh(55, "and, abandoning the hundreds of young people who had trusted him to death, fled through a secret emergency door at the back of the storage.",
   [("metal_door", "ދޮރުން", -18)])
sh(56, "\"Brent!\" Aira screamed. But there was no time to stop him. Right in front of Aira fell a small young boy of Sector 7, hit by a laser shot.",
   [("soft_thud", "ވެއްޓުނީ", -22)])
sh(57, "Bleeding from his chest, he clung to Aira's leg and begged to be saved. Without caring for her own life, Aira",
   [("sob_breath", "ސަލާމަތަށް", -22)], hum=True)
sh(58, "lifted the boy onto her shoulder and ran to carry him somewhere safe. But she did not get far. The sound of heavy boots came from all four sides.",
   [("boots_march", "ބޫޓުތަކުގެ", -18)])
sh(59, "Four commando soldiers in black steel armour came and surrounded Aira. Their laser guns were aimed straight at Aira's head.",
   [("heartbeat", "އަމާޒުވިއެވެ", -20)])
sh(60, "One of them shoved away the youth on Aira's shoulder, then struck Aira hard in the back with the butt of his gun and brought her down to the floor.",
   [("soft_thud", "ޖަހައި", -22)])
sh(61, "Aira's face hit the floor and she stopped moving. As one of the armed soldiers pulled her hands behind her back and locked heavy steel cuffs on them, Aira's eyes caught, in the distance,",
   [("cuffs_click", "ކަސްތޮޅު", -16)])
sh(62, "a tall figure walking slowly out of the smoke. It was Commander Kyle. Pushing through the thick cloud of smoke and dust, Commander Kyle walked slowly forward.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -20)])
sh(63, "All around rose the groans of people wounded in the brutal attack. The youths of Sector 7 lay fallen in pools of blood.",
   [("sob_breath", "އާހްތަކެވެ", -22)], hum=True)
sh(64, "Some had been brutally killed. Others were arrested, under the power of the Council's soldiers. Aira lay pressed to the ground,")
sh(65, "bound with steel cuffs so that she could not even move. Kyle stopped in front of her and looked at her with a mocking smile.")
sh(66, "Kyle's eyes showed mercilessness of the highest degree. At that moment the truth of Brent's great betrayal dawned on Aira's mind.",
   hum=True)
sh(67, "She realised that the Council's cruelty was far more terrifying than she had imagined. Not knowing where Zail had gone in all the chaos,")
sh(68, "a great fear for his life rose in Aira's heart. The soldiers came and began taking Aira, almost dragging her, towards the upper levels.",
   [("boots_march", "ސިފައިން", -20)])
sh(69, "As she was taken away, treated as a valuable prisoner, an indescribable eerie silence lay over the whole sector.",
   hum=True)
SHOTS = S

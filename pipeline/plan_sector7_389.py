"""Beat/shot plan for Sector 7 episode 389 (used by plan_beats.py).
Revival's warehouse, Brent's rage, Kyle's command centre, the communicator, the escape."""

LOC = {
    "tunnel": "a narrow dark rusted service tunnel deep in the lowest level of an underground bunker, corroded pipes along the walls, dripping water, puddles on a steel grated floor, and at its far end a massive rusted steel warehouse door",
    "warehouse": "the vast interior of an old rusted steel warehouse at the very bottom of an underground bunker, the hidden headquarters of a youth resistance movement: high corroded steel girders, hanging chains, steel walkways, burning fire barrels and hanging lamps, a raised steel platform like a stage, crates and old machinery along the walls",
    "side_room": "a cramped private side room in a corner of the rusted warehouse, corrugated steel walls, a big battered steel table, a scratched desk with a small lamp and a canvas bag, a doorway opening onto the orange-lit warehouse hall",
    "workshop": "the floor of the rusted underground warehouse turned into a crude workshop: welding stations throwing sparks, workbenches with steel sheets, stacks of rusty gas cylinders, hanging chains, smoke and haze",
    "command": "the main command centre on the luxurious upper level of the bunker: a high quiet office with tall glass walls, glossy white and gold surfaces, a wide white desk with gold trim, a black leather swivel chair, a curved wall of large thin screens, and beyond the glass a softly gold-lit upper level with clean architecture and green plants",
    "loading": "the dark cavern road outside the warehouse's huge open steel gate deep underground: several old battered armoured vans with open rear doors, closed wooden crates, rusted walls, steam and dust",
    "shortcut": "a narrow secret maintenance shortcut tunnel deep underground, low rusted ceiling with pipes, steel grated floor, puddles, a flickering bulb far ahead",
}
MOOD = {
    "tunnel": "deep darkness, cold steel-blue and teal shadows, a single flickering amber work light, dripping water, tense and hurried",
    "warehouse": "warm flickering orange firelight from burning barrels and amber hanging lamps against deep smoky shadows, haze in the air, charged and restless",
    "side_room": "a single harsh amber desk lamp and orange firelight spilling in from the doorway, deep shadows, tense and close",
    "workshop": "dark smoky hall lit in bursts by bright white-blue welding sparks and orange firelight, haze, feverish and ominous",
    "command": "clean cold white light with soft gold accents, glass reflections, hushed, calm and calculated",
    "loading": "harsh orange sodium lights and red tail lights through smoke and dust, chaotic and dangerous",
    "shortcut": "near darkness, cold blue-teal shadows, a flickering amber bulb far ahead, urgent race against time",
}

BEATS = [
    dict(to=2, reason="episode opening: Aira and Zail escape through the tunnels to the warehouse", chars=["aira", "zail"], loc="tunnel",
         visual="Aira and Zail hurrying side by side, an arm's length apart, along the dark dripping tunnel towards a massive rusted steel warehouse door at its end; Aira gripping her worn toolkit bag, alert and determined, Zail glancing back over his shoulder through his round glasses; the wet grated floor forms a calm lower third",
         camera="medium wide, eye level, from slightly in front of them", amb="corridor_drip"),
    dict(to=4, reason="scene change: the warehouse door opens on hundreds of Revival youths", loc="warehouse",
         visual="wide view through the opening steel door into the huge warehouse hall: hundreds of gaunt young people gathered around burning fire barrels, young men in worn patched jackets and long trousers, young women in loose long dresses and hijabs, hungry, weary, bitter faces lit orange by the flames, smoke rising to the girders",
         camera="wide establishing shot, slightly high angle, the crowd in the middle, the dark steel floor as a calm lower third", amb="warehouse_crowd"),
    dict(to=6, reason="character change: Brent, the charismatic leader, on his raised platform", chars=["brent"], loc="warehouse",
         visual="Brent standing tall on the raised steel platform above the crowd, feet planted wide, chest out, arms slightly open in a commanding pose, firelight on his hard confident face; the backs of many young heads in the foreground below him, his empty hands visible",
         camera="low angle medium wide, Brent in the upper half", amb="warehouse_crowd"),
    dict(to=8, reason="action change: Aira pushes through the crowd calling to Brent", chars=["aira", "zail", "brent"], loc="warehouse",
         visual="Aira pushing forward through a narrow gap in the crowd that parts around her (nobody touches her), one hand raised, calling out urgently towards the platform; Zail a step behind her; on the platform in the background Brent turning to look down at her; young faces turning in the orange firelight",
         camera="medium wide, eye level, Aira in the upper half facing camera", amb="warehouse_crowd"),
    dict(to=10, reason="scene change: Brent takes them into a private room and sees the evidence", chars=["brent", "aira", "zail"], loc="side_room",
         visual="Brent leaning over the battered steel table, eyes wide in disbelief, staring at a small black encrypted box that projects a glowing screen showing a green valley under a blue sky and a glowing red panel (no text, no numbers); Aira and Zail standing on the other side of the table, watching him gravely, an arm's length apart",
         camera="medium shot, eye level, faces lit by the glowing screen", amb="rebel_workshop"),
    dict(to=13, reason="action change: Brent slams the table in rage and calls for revenge", chars=["brent", "aira", "zail"], loc="side_room",
         visual="Brent with both fists slammed down on the steel table, tin cups jumping and toppling over, his face twisted with rage as he shouts; across the table Aira startled, stepping back, her eyes wide with alarm, Zail behind her frowning; nobody is hurt",
         camera="medium shot, slightly low angle on Brent", amb="rebel_workshop", sens="violence",
         safe="rage and the call to kill shown only as a fist on a table and toppled cups; nobody is struck"),
    dict(to=16, reason="action change: Aira steps in to stop him and argues for the lift escape", chars=["aira", "brent", "zail"], loc="side_room",
         visual="Aira stepping in front of Brent with an arm's length gap between them, both palms open before her, pleading earnestly with fierce urgent eyes; Brent glaring down at her, jaw clenched, chest heaving; Zail watching anxiously behind; there is no contact between them",
         camera="medium two-shot, eye level, profiles facing each other", amb="rebel_workshop", sens="intimacy",
         safe="narration has Aira grabbing Brent's arm (and him shaking her hand off); shown as her stepping in front of him and pleading, no touching"),
    dict(to=19, reason="scene/action change: Brent back on the platform rouses the crowd to revenge", chars=["brent"], loc="warehouse",
         visual="Brent on the raised platform shouting with one empty fist raised high, the huge crowd of young people roaring back at him with raised fists, open mouths and furious faces in flickering firelight and smoke; nobody holds anything",
         camera="wide shot from behind the crowd looking up at the platform", amb="warehouse_crowd", sens="violence",
         safe="calls to take up arms and cut throats shown only as a roaring crowd with raised empty fists"),
    dict(to=21, reason="return to Brent on his platform: the narrator hints at his dark side", reuse="beat_003", loc="warehouse",
         visual="(reuse of beat_003: Brent on his platform)", camera="tight crop on Brent", amb="warehouse_crowd"),
    dict(to=24, reason="time skip and action change: the warehouse turns into a crude workshop", loc="workshop",
         visual="the warehouse floor turned into a feverish workshop: young men in worn jackets and welding goggles welding steel plates in showers of bright sparks, others hammering metal sheets on workbenches, rows of stacked rusty gas cylinders, chains hanging, smoke and haze, light flickering between dark and bright",
         camera="wide shot, eye level, the sparks in the upper half, the dark floor as a calm lower third", amb="rebel_workshop",
         transition="black", sens="violence",
         safe="bomb-making shown only as welding sparks, hammering metal sheets and stacked gas cylinders; no wires, fuses or explosives"),
    dict(to=28, reason="character change: Aira watching the preparations from a distance, uneasy", chars=["aira"], loc="workshop",
         visual="Aira standing at the edge of the workshop in the foreground, half in shadow, arms folded, watching with deep unease and worry; in the blurred mid-ground a proud young rebel in a worn jacket raising a fist beside a stack of rusty gas cylinders, others hammering metal under welding sparks",
         camera="medium shot, Aira in the right third facing the scene, three-quarter view", amb="rebel_workshop", sens="violence",
         safe="the boast about blowing the doors is shown as a raised fist beside closed gas cylinders; no wires or explosives"),
    dict(to=33, reason="action change: Aira and Zail confer quietly", chars=["aira", "zail"], loc="workshop",
         visual="Aira leaning slightly towards Zail and speaking quietly, the two standing an arm's length apart beside a rusted steel pillar at the edge of the hall; Zail nodding with worried eyes behind his round glasses; behind them blurred welding sparks and orange firelight",
         camera="medium two-shot, eye level", amb="rebel_workshop"),
    dict(to=36, reason="focus change: Brent resting with upper-level ration packs", chars=["brent"], loc="side_room",
         visual="Brent sitting exhausted at the scratched desk, drinking from a plastic water bottle; spilling out of his open canvas bag on the desk are shiny silver ration packets with a fine gold seal (no text), a sleek black walkie-talkie and a compact black device beside them; seen through the open doorway from a distance",
         camera="medium shot through the doorway, desk at mid height", amb="rebel_workshop"),
    dict(to=39, reason="return to Aira whispering her suspicion to Zail", reuse="beat_012", loc="workshop",
         visual="(reuse of beat_012: Aira and Zail conferring)", camera="tight crop on their faces", amb="rebel_workshop"),
    dict(to=40, reason="return to Brent shouting orders to the crowd", reuse="beat_008", loc="warehouse",
         visual="(reuse of beat_008: Brent rousing the crowd)", camera="medium crop", amb="warehouse_crowd"),
    dict(to=43, reason="scene change: the cold, quiet command centre on the upper level", chars=["kyle"], loc="command",
         visual="Kyle seated upright in a black leather swivel chair at a wide white-and-gold desk in the hushed glass-walled command centre, composed and cold, gloved hands resting on the armrests; tall glass walls and a softly gold-lit upper level beyond",
         camera="wide shot, eye level, Kyle in the upper half, the glossy floor as a calm lower third", amb="command_center"),
    dict(to=46, reason="action change: Kyle watches the warehouse on hidden-camera screens", chars=["kyle"], loc="command",
         visual="over-the-shoulder view of Kyle facing the curved wall of large screens showing live orange-lit images of the warehouse: a crowd with raised fists, welding sparks, a man on a platform (images only, no text, no numbers); Kyle's face in profile with a faint cold mocking smile",
         camera="over-the-shoulder medium shot", amb="command_center"),
    dict(to=49, reason="action change: Kyle sips coffee and opens the secret file on a tablet", chars=["kyle"], loc="command",
         visual="Kyle leaning back in his chair holding a white coffee cup in one gloved hand, looking down at a glowing tablet on the desk that shows a small portrait photo of a man in a rust-red jacket and abstract glowing charts and lines (no readable text, no numbers); his expression cool and knowing",
         camera="medium close-up, slightly high angle, the desk top as a calm lower third", amb="command_center",
         sens="other", safe="the secret file is shown only as a portrait and abstract charts; no readable text"),
    dict(to=53, reason="focus change: Brent revealed as Marcus's paid spy", chars=["brent"], loc="warehouse",
         visual="Brent alone in a shadowy corner of the warehouse behind stacked crates, half his face lit orange by distant firelight and half in cold blue shadow, speaking secretly into a small black communicator held near his mouth, his narrow eyes sly and calculating, glancing sideways",
         camera="medium close-up, slightly low angle", amb="warehouse_crowd"),
    dict(to=57, reason="action change: the red line lights up; Marcus calls Kyle", chars=["kyle", "marcus"], loc="command",
         visual="a red light glowing on a sleek communication console on Kyle's white desk; above it a translucent pale-gold holographic image of Marcus's head and shoulders, cold heavy-lidded eyes; Kyle sitting upright facing the hologram respectfully, composed",
         camera="medium two-shot, eye level, the hologram on the left, Kyle on the right", amb="command_center"),
    dict(to=61, reason="action change: Kyle ends the call and studies Aira's face on the monitor", chars=["kyle", "aira"], loc="command",
         visual="Kyle standing before a large screen, seen in profile, looking up at a live close image of Aira's face lit orange in the warehouse (Aira appears ONLY as an image on the screen); his expression cold and pitiless with a faint smile; the red console light dimming on the desk",
         camera="medium shot, Kyle in the left third, the screen filling the right", amb="command_center"),
    dict(to=63, reason="scene change: the vans being loaded outside the warehouse", loc="loading",
         visual="chaotic scene outside the warehouse gate: young men in worn jackets loading closed wooden crates and rusty gas cylinders into old battered armoured vans, others shouting with raised empty fists, faces fierce, harsh orange lights and red tail lights in smoke and dust",
         camera="wide shot, eye level, the vans across the middle, the dark road as a calm lower third", amb="warehouse_crowd",
         sens="violence", safe="'weapons' loaded into the vans are shown only as closed crates and gas cylinders"),
    dict(to=65, reason="action change: Aira slips to Brent's desk and searches it", chars=["aira"], loc="side_room",
         visual="Aira bent over Brent's desk in the empty side room, quietly opening his canvas bag and checking the things on the desk, glancing tensely back at the doorway where orange light and moving shadows spill in",
         camera="medium shot, eye level, from the side of the desk", amb="rebel_workshop"),
    dict(to=69, reason="action change: Aira finds the hidden communicator and reads the message", chars=["aira"], loc="side_room",
         visual="Aira crouched beside the desk holding a small sleek black military communicator she has just pulled from under it, its screen glowing cold red (abstract red glow only, no text), lighting her shocked face from below; her breath held, eyes wide with horror",
         camera="medium close-up, eye level, the dark floor as a calm lower third", amb="rebel_workshop",
         sens="other", safe="the ambush message is never shown as text; only a red glow and her horrified face"),
    dict(to=72, reason="character change: Brent appears in the doorway, menacing", chars=["brent", "aira"], loc="side_room",
         visual="Brent filling the doorway, backlit by orange firelight, his face hard, cruel and menacing, cold narrow eyes fixed ahead, both hands empty, one empty hand slightly raised towards her; Aira in the foreground seen from behind her shoulder, turned towards him, frozen",
         camera="over-the-shoulder medium shot from behind Aira, Brent in the upper half", amb="rebel_workshop", sens="violence",
         safe="Brent aiming a gun at Aira: shown only as his menacing face in the doorway with empty hands; no gun"),
    dict(to=77, reason="action change: Aira confronts Brent with the communicator, he sneers", chars=["aira", "brent"], loc="side_room",
         visual="Aira standing defiant across the small room, well apart from Brent, holding up the glowing communicator towards him, jaw clenched, eyes blazing; Brent near the doorway throwing his head back in a mocking contemptuous laugh, his hands empty",
         camera="medium wide two-shot, eye level, the two facing each other across the room", amb="rebel_workshop", sens="violence",
         safe="no gun shown at any point; the threat is carried by his sneer and her defiance"),
    dict(to=79, reason="action change: Zail strikes from behind; Brent falls (aftermath only)", chars=["zail"], loc="side_room",
         visual="a heavy metal pipe lying on the steel floor of the side room where it has just clattered down beside a dropped black communicator; in the doorway behind, Zail standing breathless and shaken, his small round wire-rimmed glasses on his face, eyes wide behind them; nobody lying on the floor",
         camera="low angle near the floor, the pipe and communicator in the middle ground, Zail in the upper half", amb="rebel_workshop",
         sens="violence", safe="the blow and Brent's fall are not shown: only a metal pipe on the floor beside the dropped communicator and Zail breathless in the doorway"),
    dict(to=81, reason="scene change: the vans roar off towards the trap", chars=["aira", "zail"], loc="loading",
         visual="Aira and Zail at the huge open warehouse gate, seen from behind in three-quarter view, an arm's length apart, watching the battered vans speed away down the dark cavern road with glowing red tail lights and clouds of dust; Aira slipping the black communicator into her bag, Zail with a hand raised in alarm",
         camera="medium wide shot from behind them, the vans and tail lights in the upper half", amb="warehouse_crowd"),
    dict(to=83, reason="scene change: Aira and Zail race through the secret shortcut", chars=["aira", "zail"], loc="shortcut",
         visual="Aira running hard through the narrow dark shortcut tunnel, coat flowing, looking back over her shoulder with fierce determination towards Zail (small round wire-rimmed glasses on his face, thick grey-white beard) who hurries a few steps behind her; the flickering amber bulb far ahead",
         camera="medium wide, eye level, from in front of them, the grated floor as a calm lower third", amb="corridor_drip"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Out through the back door of Zail's workshop, along narrow dark bunker tunnels, fleeing the soldiers, Aira and Zail came to a steel warehouse at the very bottom of Sector 7.",
   [("footsteps_pavement", "ފިލައިގެން", -22)])
sh(2, "From outside the place looked ruined and abandoned, but inside was the headquarters of 'Revival', a movement secretly formed against the Council's rule.")
sh(3, "As the warehouse's steel door opened, they saw hundreds of young people in the orange light of fire barrels and lamps.",
   [("metal_door", "ހުޅުވާލުމާއެކު", -18), ("fire_crackle", "އަލިފާން", -22)])
sh(4, "On every face could be seen oppression, the pain of hunger and despair. In the middle of them all,")
sh(5, "on a high stage-like platform stood Brent — the young leader, influential among the youth of Sector 7, whose gift of speech made everyone's blood boil.")
sh(6, "His powerful build and sharp voice were like a beacon of hope for the people of Sector 7. 'Brent!'")
sh(7, "Aira pushed forward through the crowd. 'We have learned important truths.'",
   [("cloth_rustle", "ކަފަމުން", -24)])
sh(8, "'We have live data from the surface and the Council's dangerous plan!'")
sh(9, "At once Brent came down from the stage and took Aira and Zail into a private room. On the device placed on the table, the plans of Project Cleanslate,",
   [("computer_beep", "ޑިވައިސުން", -22)])
sh(10, "the seven-day countdown and the views of the clean green world on the surface appeared, and Brent's eyes widened. 'Seven days?'",
   [("gasp", "ބޮޑުވެގެން", -22)])
sh(11, "'To kill all of Sector 7 with poison gas?' Brent gritted his teeth. Suddenly he slammed his fists on the big table so hard that even the cups shook.",
   [("soft_thud", "ޖެހީނުން", -18), ("cup_clatter", "ތެޅިގެން", -16)], hum=True)
sh(12, "'We will not wait to die! This is the time! We must storm the upper level, kill all those rich people,'")
sh(13, "'and seize their food and weapons! We must slaughter them all!' Aira flinched at the hatred and bloodlust in Brent's voice.",
   [("gasp", "ސިހުނެވެ", -22)])
sh(14, "She quickly caught hold of Brent's arm. 'No, Brent! Our goal is not to kill people!' Aira tried to make him understand.")
sh(15, "'If we attack the upper level, their heavy weapons will wipe out everyone in Sector 7.'")
sh(16, "'Our plan must be for everyone to go up to the surface together through the main lift. To step out into a clean world and find freedom!'")
sh(17, "But Brent did not want to hear it. He shook off Aira's hand and went back outside,",
   [("footsteps_pavement", "ނުކުމެ", -22)])
sh(18, "faced the hundreds of young people gathered there and shouted at the top of his voice: 'Today is the day we take revenge! Take up arms!'",
   [("crowd_roar", "ހަޅޭއްލަވައިގަތެވެ", -18)])
sh(19, "'Before they kill us, we will cut their throats!' The whole warehouse echoed with Brent's voice. The young people's blood boiled.",
   [("crowd_roar", "ގުގުމައިގެން", -16)], hum=True)
sh(20, "As people began shouting in the spirit of revenge, those emotions spun out of control. But what Aira did not know")
sh(21, "was the dark side of Brent, who was stoking this fire, and the secret plan behind this whole game.", hum=True)
sh(22, "The inside of the warehouse turned into a frightening battlefield. The screech of saws cutting steel,",
   [("metal_clang", "ކަނޑާ", -20)])
sh(23, "and the flashes of electric welding made the whole place flicker between dark and light. After Brent's fiery speech, more than a thousand Revival youths were boiling with rage.",
   [("weld_hiss", "ވެލްޑިންގގެ", -18), ("electric_spark", "ވިދުމުން", -20)])
sh(24, "They worked tirelessly, sharpening pieces of steel and pouring chemicals into rusty gas cylinders, making homemade bombs.",
   [("metal_clang", "ތޫނުކޮށް", -20), ("steam_hiss", "ކެމިކަލް", -24)])
sh(25, "'With all this we'll blow open the upper level's steel doors!' a young man said proudly, fixing a wire to a gas cylinder.",
   [("metal_clang", "ސިލިންޑަރެއްގައި", -22)])
sh(26, "'We'll overwhelm their security and turn the whole place to ash!' Watching this from a distance, a deep unease grew in Aira's heart.")
sh(27, "This was not the path she wanted. Instead of saving innocent people, what she saw was preparation for bloodshed.", hum=True)
sh(28, "Facing the upper level's most modern high-tech weapons with homemade weapons in their hands was like walking willingly into the jaws of death.")
sh(29, "'Zail, my heart says this is a very wrong direction,' Aira said softly, moving closer to Zail.")
sh(30, "'Brent is leading these people straight into a grave. The Council's soldiers have modern guns and lasers.'")
sh(31, "'If these kids go up holding pieces of steel, they'll all be killed within a single second.' Zail, worried too, nodded.")
sh(32, "'Aira is right. Brent's plan makes no strategic sense at all.'")
sh(33, "'He is using people's anger for a far greater danger.' At that moment Aira's eye fell on the things on Brent's table.")
sh(34, "As Brent sat down exhausted, drinking water from a bottle, the food packets he took out of his bag were nothing the people of Sector 7 had ever seen.",
   [("cloth_rustle", "ދަބަހުން", -24)])
sh(35, "They were special protein rations with an expensive seal, given only to the upper level's soldiers and officials.")
sh(36, "While the ordinary people of Sector 7 were begging for a single morsel, how could Brent get things like these? Aira thought hard.")
sh(37, "Brent's actions, and the way he suddenly whipped people up for war, raised a big doubt in her heart for the first time. 'Zail...'",
   [("heartbeat", "ޝައްކެއް", -22)], hum=True)
sh(38, "'Look at the walkie-talkies and devices Brent uses,' Aira whispered into Zail's ear. 'Those aren't things you can get in this sector.'",
   [("breath", "ކަންފަތްދޮށުގައި", -24)])
sh(39, "'What gives him the confidence to lead everyone up so certainly?' As questions swirled in Aira's mind,")
sh(40, "Brent was again shouting at the youths, ordering them to load the weapons into the vans. But behind those voices was a completely different game, played by someone in a cold room on the upper level.",
   [("crowd_roar", "ހަޅޭއްލަވައި", -20)])
sh(41, "In complete contrast to the smoke and rusty darkness of Sector 7, the main command centre of the upper level was utterly quiet and cold.")
sh(42, "Inside that high-end office, with huge glass walls and fittings of precious metal, was the city's Chief Security Commander, Kyle.")
sh(43, "The military uniform he wore was a suit with the latest defensive coating. Kyle sat at his desk in a black swivel chair.")
sh(44, "On the huge digital screens in front of him, the inside of Revival's warehouse was showing live.",
   [("computer_beep", "ސްކްރީންތަކުން", -22)])
sh(45, "Brent shouting, the young people raging, the way people were making bombs out of gas cylinders —")
sh(46, "all of it Kyle could see clearly through secret sensors hidden in every direction. A wicked, mocking smile spread over Kyle's lips.")
sh(47, "Taking a sip from the coffee cup in his hand, he opened a digital tablet on the desk.",
   [("computer_beep", "ހުޅުވާލިއެވެ", -22)])
sh(48, "On the tablet's screen was a top-secret file: 'Asset file: Operative Brent, Sector 7. Mission: initiate controlled uprising, expedite protocol Cleanslate.'")
sh(49, "The file held Brent's full profile and a detailed list of the special upper-level food secretly sent to him and of crypto-money transactions.")
sh(50, "Brent was no leader who wished the youth of Sector 7 well. He was a spy sold for money, working on the orders of Marcus, the Council's leader.")
sh(51, "The Council's plan was to channel all of Sector 7's anger in one direction and get them to launch an attack of their own accord.")
sh(52, "Then soldiers would come out in the name of 'keeping the peace', and the way would be open to wipe them all out at once without raising any suspicion.")
sh(53, "Before releasing the poison gas, leading them into a grave in the name of rebellion — that was the core scheme of Marcus and Kyle.", hum=True)
sh(54, "At that moment the red communication line on Kyle's desk lit up. It was a direct call from the leader, Marcus. 'Kyle, how are things going?'",
   [("alarm_beep", "ދިއްލުނެވެ", -20)])
sh(55, "Marcus's harsh voice echoed through the room. 'Everything is going according to plan, sir,' Kyle said respectfully.")
sh(56, "'Brent is playing his role perfectly. He is ready to gather all the youth of Sector 7 together and bring them to the main gate.'")
sh(57, "'When they enter the lift area, our heavy artillery will destroy them all at once.' 'Very good,'")
sh(58, "Marcus let out a satisfied breath. 'But remember. That girl, Aira... she has the encrypted box.'",
   [("sigh", "ނޭވާއެއް", -22)])
sh(59, "'Before that evidence gets out, she too must be eliminated in that crowd.' 'No doubt about it, sir.'", hum=True)
sh(60, "'They are walking into our trap all by themselves,' Kyle said, glancing at the screen as he ended the call.",
   [("computer_beep", "ކަނޑާލިއެވެ", -22)])
sh(61, "Looking at Aira's face on the monitor, Kyle said to himself, 'There is no salvation for you.'", hum=True)
sh(62, "As weapons and supplies were being loaded into the vans outside the warehouse, a dangerous chaos filled the whole area.",
   [("metal_clang", "އަރުވަމުން", -20)])
sh(63, "The young people were shouting at the top of their voices, fired up to 'tear the upper level to pieces'. In their eyes was the dark passion of revenge.",
   [("crowd_roar", "ހަޅޭއްލަވަމުންނެވެ", -18)])
sh(64, "But Aira's heart kept giving her a bad warning. Aira quietly slipped over to Brent's own desk.",
   [("cloth_rustle", "ޖެހިލިއެވެ", -24)])
sh(65, "While Brent was busy outside giving people orders, Aira began to check his bag and the things on the desk.")
sh(66, "Suddenly her hand touched a small, ultra-modern military communicator fixed under the desk with a magnet. When Aira lit up the device's screen,",
   [("lock_click", "މެގްނެޓަކުން", -22), ("computer_beep", "ދިއްލާލި", -20)])
sh(67, "the last message on it made her feel as if the ground beneath her feet had given way: 'From: Commander Kyle.'",
   [("heartbeat", "ދެމިގެން", -20)], hum=True)
sh(68, "'Status: ambush ready at the Sector-1 elevator gate. Bring them all.'")
sh(69, "'No survivors.' Aira's breath stopped. Brent was not just an angry young man; he was a Council spy, about to lead them all straight into the jaws of death!",
   [("gasp", "ހުއްޓުނެވެ", -18)], hum=True)
sh(70, "'What are you doing there?' At the harsh voice behind her Aira spun round with a start. In the doorway stood Brent.",
   [("gasp", "ސިއްސައިގެން", -18)])
sh(71, "The friendliness and the air of a leader that had been on his face were completely gone; it now wore a cruel, dangerous look.")
sh(72, "He aimed the gun in his hand straight at Aira's chest. 'Brent... what kind of traitor are you?'",
   [("heartbeat", "އަމާޒުކޮށްލިއެވެ", -20)], hum=True)
sh(73, "Aira gritted her teeth, holding up the communicator. 'All these people trust you!'")
sh(74, "'They think you are the leader of their freedom. But you sold these people for a little of Marcus's money!'")
sh(75, "Brent let out a mocking laugh. 'It's too late for you to understand the truth, Aira. There is no future in this Sector 7.'")
sh(76, "'This is a dark, filthy pit. I want to go up! To live happily in a new world with the rich.'")
sh(77, "'I don't care if this rubbish dies!' 'You won't get away with this!' Aira shouted. 'You won't be alive to stop it,'")
sh(78, "Brent squeezed the trigger. At that very instant, a sound came from behind Brent.",
   [("heartbeat", "ބާރުކޮށްލިއެވެ", -18)], hum=True)
sh(79, "Zail struck Brent on the head with the heavy steel bar in his hand. As Brent staggered and fell to the floor, the gun flew from his hand.",
   [("soft_thud", "ޖެހިއެވެ", -22), ("soft_thud", "ވެއްޓުނު", -22), ("metal_clang", "ވިއްސައިގެން", -18)])
sh(80, "'Aira, run, quickly!' Zail shouted. But at that moment came the sound of van engines revving outside, and the vans speeding off towards the lift gate with hundreds of young people.",
   [("engine_rev", "އިންޖީނު", -16), ("crowd_roar", "ދުއްވައިގަތް", -22)])
sh(81, "They were heading for the death trap Commander Kyle's soldiers had prepared! Aira picked up the device lying on the floor, put it in her bag and looked at Zail.",
   [("cloth_rustle", "ދަބަހަށް", -24)])
sh(82, "'Zail, we have to save them from that trap. We must get to the main gate before they do!'")
sh(83, "Aira and Zail rushed out of the warehouse and raced through a secret shortcut towards the lift gate, in a dangerous race against time.",
   [("footsteps_pavement", "ދުއްވައިގަތީ", -20), ("breath_heavy", "ރޭހެއްގައެވެ", -22)], hum=True)
SHOTS = S

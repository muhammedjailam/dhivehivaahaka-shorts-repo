"""Beat/shot plan for Project Phenix episode 324 — the FINALE (used by plan_beats.py)."""

LOC = {
    "warehouse": "a big dark empty warehouse: bare concrete floor, one warm lamp hanging over a steel chair, a huge steel door at the far end blown open, grey smoke drifting in through it",
    "dhoonidhoo_cell": "a bare cell in Dhoonidhoo detention centre: grey concrete walls, a steel bunk with a thin grey blanket, a small barred window high in the wall, a heavy grey steel door, a plain steel chair",
    "mndf_launch": "an MNDF military fast launch with a plain dark-grey hull and no markings racing across Malé's lagoon towards the small island of Dhoonidhoo",
    "dhoonidhoo_jetty": "the concrete jetty of Dhoonidhoo island: low pale detention-centre buildings behind tall wire fences and palm trees, a few dim lamps on poles",
    "coastguard_launch": "an MNDF coast-guard launch with a plain dark-grey hull and no markings on a rough open sea east of Malé",
    "coastguard_cockpit": "the cockpit of the MNDF coast-guard launch: a steering wheel, a row of glowing navigation and radar screens showing only blurred shapes, rain- and spray-spattered windows",
    "cargo_ship": "the huge dark steel cargo ship MV Orion on the open sea at night: stacked containers, dim deck lights, a tall crane, a plain dark hull with no name, no letters and no markings",
    "ship_deck": "the deck of the huge cargo ship at night: narrow lanes between towering stacked plain steel containers with no markings, dim yellow deck lights, a wet steel deck, a tall crane overhead",
    "red_container": "a plain red steel shipping container with no markings standing mid-ship on the cargo ship's deck; inside it cold refrigerated steel racks holding thousands of small glass vials of glowing blue liquid",
    "police_hq": "the Shaheed Hussain Adam Building, Malé police headquarters: a modern white multi-storey building with no visible signs or lettering, a wide paved forecourt",
    "commissioner_office": "the new Commissioner's office in police headquarters: a polished dark wood desk, plain flags with no emblems on stands, tall bright windows",
    "hulhumale_beach": "Hulhumalé beach: wide white sand, calm turquoise waves rolling in, a few coconut palms, a simple wooden bench under the palms, the city's low skyline far behind",
}
MOOD = {
    "warehouse": "night inside the warehouse: deep navy darkness, one warm hanging lamp, swirling grey smoke, white flashlight beams of soldiers cutting through it, shock and horror",
    "dhoonidhoo_cell": "dusk: cold flat light from a single fluorescent tube, dusky blue light through the barred window, oppressive and tense",
    "mndf_launch": "stormy dusk: heavy dark clouds, the last steel-blue light over the lagoon, white spray, the cool glow of a tablet screen, urgent",
    "dhoonidhoo_jetty": "dusk turning to night: dark clouds, dim amber jetty lamps, navy-blue sea, urgent",
    "coastguard_launch": "night: black sea, white spray, heavy black clouds, a flicker of distant lightning, strong wind, tense",
    "coastguard_cockpit": "night: a dark cockpit lit by the cool blue-green glow of the screens, rain and spray running down the windows",
    "cargo_ship": "night storm at sea: black water, white spray, dim yellow deck lights, a harsh white searchlight, distant lightning",
    "ship_deck": "night: dim yellow deck lights, cold rain, white flashlight beams, drifting smoke, orange fire glow in places, tense",
    "red_container": "night: a cold eerie blue glow from the vials, a small blinking red light, deep shadows, yellow deck lights outside",
    "police_hq": "three weeks later, a clear golden morning, bright blue sky, warm sunlight, hopeful",
    "commissioner_office": "bright clear day, warm sunlight through the tall windows, dignified and proud",
    "hulhumale_beach": "golden late afternoon, a warm low sun, soft long shadows, calm sea, bittersweet and quiet",
}

LOW = "faces in the upper two-thirds, a calm dark lower third"
ASH = "Ashham in his dark-navy long-sleeved police field shirt, dusty and creased but unmarked"
ASHJ = "Ashham wearing a black zip-up tactical jacket over his dark-navy shirt and dark trousers"
FAAJ = "Faahid (grey hair, white moustache) wearing a black tactical jacket over his olive shirt"
HAB = "Habeeb in a rumpled dark-navy police uniform shirt with no cap, his glasses with a thin crack across one lens, tired and dusty but unmarked"
SOLD = "MNDF soldiers in plain black combat gear and helmets with no insignia, their hands empty or holding flashlights"

BEATS = [
    # ---------------- WAREHOUSE
    dict(to=2, reason="episode opening: the warehouse as soldiers storm in; Fairooz seizes the glowing vial", chars=["fairooz"], loc="warehouse",
         visual=f"Fairooz in his rumpled dark-navy senior police uniform, no cap, crouched low on the concrete floor beside an overturned steel tray, clutching a small glass vial of glowing blue liquid tightly to his chest with both hands, his eyes wild and desperate; behind him through the smoke, {SOLD}, pour in through the blown-open steel door with bright flashlight beams",
         camera=f"medium shot, slightly low angle, {LOW} (concrete floor)", amb="storage_hall",
         sens="violence", safe="the syringe and Fairooz injecting himself are never shown: only Fairooz clutching a small glowing blue glass vial; no needle"),
    dict(to=5, reason="action change: Ashham lunges too late; Fairooz's end is shown only by the empty vial", chars=["ashham"], loc="warehouse",
         visual=f"in the foreground a small empty glass vial with a last faint blue glow rolling on the bare concrete floor; behind it, slightly out of focus, {ASH}, frozen mid-lunge with one arm reaching out, his face twisted in anguish and shock; two soldiers in black combat gear at the edge of the frame turning their faces away",
         camera=f"low angle from floor level, the vial in sharp focus at lower middle, Ashham's face in the upper third, {LOW}", amb="storage_hall", hum=True,
         sens="death", safe="Fairooz's convulsions, foam and collapse are never shown, no lying figure, no covered shape: only the empty glowing vial rolling on the floor and the frozen faces"),
    dict(to=8, reason="action change: Saleem kneels weeping and is led out; Faahid's hand on Ashham's shoulder", chars=["faahid", "ashham", "saleem"], loc="warehouse",
         visual=f"{FAAJ} resting a hand on Ashham's shoulder and speaking gravely; {ASH}, standing with a hard, exhausted face; in the background under the hanging lamp the Home Minister Saleem in his black three-piece suit on his knees on the floor with his face in his hands, two soldiers in black combat gear standing beside him ready to lead him away",
         camera=f"medium two-shot, eye level, Saleem small in the background, {LOW} (concrete floor)", amb="storage_hall",
         sens="other", safe="Saleem's arrest shown without handcuffs; Ashham's split lip not shown"),
    # ---------------- DHOONIDHOO CELL
    dict(to=14, reason="scene change: Habeeb held in a Dhoonidhoo cell, Naasir interrogating him with a laptop", chars=["habeeb", "naasir"], loc="dhoonidhoo_cell",
         visual=f"{HAB}, sitting on the edge of the steel bunk with his hands behind his back out of view, head raised defiantly; facing him a few steps away Naasir in his black suit sits on a steel chair with an open laptop on his knees (screen facing away from the viewer), leaning forward with a cold, menacing stare",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (bare concrete floor)", amb="detention_room",
         sens="violence", safe="Habeeb 'tied to an iron bed' with a badly swollen face = seated on a steel bunk, hands out of view, tired but unmarked; the threat to cut his fingers is only spoken"),
    dict(to=17, reason="detail: the hidden smartwatch Habeeb secretly presses", loc="dhoonidhoo_cell",
         visual="extreme close-up of a young man's wrist in a dark-navy shirt cuff resting on a grey blanket on a steel bunk: a slim plain black smartwatch with a soft blue glow and a blank screen, his fingertip quietly pressing its side button; the rest of the cell dark and out of focus",
         camera="extreme close-up, the wrist and watch in the upper-middle of the frame, the grey blanket as the calm lower third", amb="detention_room", hum=True),
    # ---------------- RACE ON THE SEA
    dict(to=21, reason="scene change: Ashham and Faahid race across the lagoon to Dhoonidhoo on a military launch", chars=["ashham", "faahid"], loc="mndf_launch",
         visual=f"{ASHJ}, standing at the rail of the speeding dark-grey military launch holding a glowing tablet (screen showing only soft blurred light), {FAAJ}, leaning in beside him listening intently; white spray flying off the bow, two soldiers in black combat gear and a launch captain at the wheel behind them",
         camera=f"medium shot on the deck, eye level, {LOW} (dark wake and water)", amb="sea_boat"),
    dict(to=24, reason="scene change: the launch reaches Dhoonidhoo jetty; Faahid commands the guards; Ashham runs", chars=["ashham", "faahid"], loc="dhoonidhoo_jetty",
         visual=f"the dark-grey launch moored at the concrete jetty, {SOLD}, stepping ashore; two startled jail security guards in light-blue uniform shirts stepping back with empty hands; {FAAJ}, stepping forward with one hand raised in command; {ASHJ}, already running along the jetty towards the low detention buildings",
         camera=f"medium wide shot, eye level, {LOW} (concrete jetty and dark water)", amb="night_exterior"),
    # ---------------- TIME UP
    dict(to=26, reason="scene change back to the cell: Naasir's last threat, Habeeb stares him down", chars=["naasir", "habeeb"], loc="dhoonidhoo_cell",
         visual=f"Naasir in his black suit standing over by the barred window, looming and menacing, his hands empty, glaring down across the cell; {HAB}, sitting on the steel bunk several steps away, looking straight up into Naasir's eyes with calm defiance",
         camera=f"medium wide shot, slightly low angle from Habeeb's side, {LOW} (concrete floor)", amb="detention_room", hum=True,
         sens="violence", safe="the knife at Habeeb's throat and the kick are never shown: Naasir stands at a distance by the window, hands empty; the kick is only a faint offscreen thud"),
    dict(to=28, reason="character enters: the cell door bursts open and Ashham stands in the doorway", chars=["ashham", "naasir"], loc="dhoonidhoo_cell",
         visual=f"{ASHJ}, standing in the open steel cell doorway with bright corridor light behind him, one open palm raised in command, his face fierce; across the cell Naasir in his black suit spinning round from the window, startled, his hands empty",
         camera=f"medium wide shot from inside the cell, eye level, {LOW} (concrete floor)", amb="detention_room",
         sens="violence", safe="Naasir turning the knife on Ashham is never shown; a tense standoff at a distance, hands empty"),
    dict(to=31, reason="action change: Naasir led away by soldiers; Ashham goes to Habeeb", chars=["ashham", "habeeb", "naasir"], loc="dhoonidhoo_cell",
         visual=f"in the background two soldiers in black combat gear leading Naasir out through the steel door, his hands behind his back; in the foreground {ASHJ}, crouching beside the steel bunk with a hand on Habeeb's shoulder, worried; {HAB}, smiling weakly up at him",
         camera=f"medium shot, eye level, {LOW} (concrete floor)", amb="detention_room",
         sens="violence", safe="Ashham's spinning kick and Naasir's fall are never shown: only the aftermath, Naasir escorted out with hands behind his back, no cuffs"),
    # ---------------- BIG LEAK
    dict(to=35, reason="action change: Habeeb reveals the leak through his watch; world news fills Faahid's tablet", chars=["habeeb", "faahid", "ashham"], loc="dhoonidhoo_cell",
         visual=f"{HAB}, now standing, raising his wrist to show a slim black smartwatch with a soft glow, a tired proud smile; {FAAJ}, holding a tablet that glows with blurred news-like layouts and soft coloured blocks (no readable text), amazed; {ASHJ}, leaning in to look, faces lit blue by the screen",
         camera=f"medium three-shot, eye level, {LOW} (concrete floor in shadow)", amb="detention_room"),
    dict(to=39, reason="emotional turning point: Habeeb's new fear — the real drug container is heading for a foreign ship", chars=["habeeb", "ashham"], loc="dhoonidhoo_cell",
         visual=f"close-up of {HAB}, anxious and urgent, eyebrows drawn together, speaking up at Ashham; beside him in profile {ASHJ}, jaw set, eyes narrowing, ready to move",
         camera=f"close two-shot, eye level, {LOW}", amb="detention_room", hum=True),
    # ---------------- COAST-GUARD LAUNCH
    dict(to=41, reason="scene change: the coast-guard launch heads out onto the rough night sea", loc="coastguard_launch",
         visual="the dark-grey MNDF coast-guard launch with no markings ploughing through big black waves under heavy black clouds, white spray bursting over its bow, three small figures visible behind its lit cockpit windows, a faint flash of lightning on the horizon",
         camera="wide shot from the side, slightly high, the launch in the upper half, the dark heaving sea as the lower third", amb="sea_search"),
    dict(to=47, reason="scene change: in the cockpit Habeeb finds the MV Orion on radar; Ashham zips his jacket", chars=["ashham", "habeeb", "faahid"], loc="coastguard_cockpit",
         visual=f"{HAB}, seated at the glowing radar and navigation screens (blurred shapes only, no numbers), pointing at a bright blip; {FAAJ}, gripping the steering wheel; {ASHJ}, standing behind them zipping his black tactical jacket up to his chin with a hard, determined face",
         camera=f"medium three-shot inside the cockpit, eye level, {LOW} (dark console)", amb="sea_search"),
    # ---------------- THE SHIP
    dict(to=51, reason="scene change: the MV Orion looms out of the dark; its searchlight and fire hit the launch", loc="cargo_ship",
         visual="the huge dark silhouette of the steel cargo ship rising out of the night sea, containers stacked high under dim yellow deck lights, a tall crane; from its deck a blinding white searchlight beam glares down onto the small dark-grey launch in the foreground waves, bright sparks flicking off the launch's metal rail, white spray everywhere; no one visible on the ship",
         camera="wide low angle from sea level, the ship towering in the upper two-thirds, black water as the lower third", amb="storm_night",
         sens="violence", safe="automatic fire shown only as the searchlight glare and sparks on the launch's rail, no weapons, no one hit"),
    dict(to=53, reason="action change: Ashham at the stern; the searchlight shatters into darkness", loc="cargo_ship",
         visual="a tall man in a black tactical jacket seen from behind in silhouette at the stern of the small launch, facing the giant ship; high up on the ship's deck the searchlight bursting into a shower of white sparks and glass, its beam dying, that side of the ship falling into darkness",
         camera="medium wide shot from behind the man, low angle, the ship and burst of sparks in the upper half, dark water as the lower third", amb="storm_night",
         sens="violence", safe="Ashham's rifle shot is never shown: his silhouette from behind with nothing in his hands visible, only the searchlight bursting"),
    dict(to=56, reason="action change: the launch alongside the stern ladder; Ashham and Faahid climb, Habeeb stays below", chars=["habeeb", "ashham", "faahid"], loc="cargo_ship",
         visual=f"looking up the towering dark steel stern of the ship: {ASHJ}, and {FAAJ}, climbing a steel ladder up the wet hull, seen from below and behind; in the foreground {HAB}, standing in the rocking launch with a laptop in a waterproof bag under his arm, looking up anxiously; big waves and spray",
         camera=f"low angle from the launch, the climbers in the upper half, {LOW} (dark sea and the launch's deck)", amb="storm_night"),
    # ---------------- DECK FIGHT
    dict(to=61, reason="scene change: on deck, Ashham and Faahid move through the container lanes; a figure appears above", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"{ASHJ}, and {FAAJ}, crouched low and moving fast along a narrow lane between towering stacked containers, flashlight beams sweeping through the rain; on the deck ahead a dropped flashlight lies alone lighting the empty lane; high above on top of a container a crouched dark silhouette against the deck lights; Faahid pointing up and to the right in alarm",
         camera=f"medium wide shot down the lane, eye level, {LOW} (wet steel deck)", amb="storm_night",
         sens="violence", safe="the two mercenaries and their fall are never shown: only an empty lane and a dropped flashlight; the grenade is not shown"),
    dict(to=62, reason="action change: the blast between the containers", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"a bright orange fireball blooming far down the lane between the towering containers, smoke billowing, steel container doors bent outward; in the foreground, well away from the flames, {ASHJ}, and {FAAJ}, crouched low on the wet deck at two different container corners, shielding their heads with their arms, seen from behind and the side, unhurt; only these two men in the whole scene, no other people, no women",
         camera="wide shot, eye level, the fireball in the upper half, the dark wet deck as the lower third", amb="storm_night",
         sens="violence", safe="the grenade blast shown as distant spectacle with the two men diving clear, no one in the flames"),
    dict(to=64, reason="action change: through the smoke they reach the red container with the electronic lock", chars=["ashham", "faahid"], loc="red_container",
         visual=f"through drifting smoke mid-ship, a plain red steel container with no markings and a big electronic lock on its door (a blank glowing panel, no keys or digits); {ASHJ}, approaching it with one finger pressed to a small earpiece, speaking; {FAAJ}, behind him watching their backs",
         camera=f"medium wide shot, eye level, {LOW} (wet steel deck)", amb="storm_night"),
    dict(to=66, reason="character change: Habeeb in the launch hacks the ship's server", chars=["habeeb"], loc="coastguard_cockpit",
         visual=f"{HAB}, hunched over a laptop in the launch's cockpit, typing fast with intense concentration, the screen glow (blurred shapes only) lighting his face and cracked glasses, spray streaming down the window behind which the dark hull of the giant ship towers",
         camera=f"medium close-up, eye level, {LOW} (dark console)", amb="sea_search"),
    dict(to=69, reason="action change: the container opens on thousands of glowing blue vials; Faahid sets the charge", chars=["ashham", "faahid"], loc="red_container",
         visual=f"inside the open red container: cold steel racks holding thousands of small glass vials glowing eerie blue; {ASHJ}, holding the heavy door open in the doorway, staring in; {FAAJ}, kneeling in the middle of the racks placing a small black case with a blinking red light (no digits, no screen)",
         camera=f"medium wide shot from inside the container looking out, eye level, {LOW} (steel floor in blue shadow)", amb="storm_night",
         sens="violence", safe="the explosives and timer shown only as a small black case with a blinking red light, no digits"),
    # ---------------- MASTERMIND
    dict(to=72, reason="character enters: Dr. Vance appears in the container doorway with four men", chars=["vance", "ashham", "faahid"], loc="red_container",
         visual=f"Dr. Vance, an elderly European man with silver slicked-back hair in a long black overcoat, standing in the container doorway against the yellow deck lights with a cold arrogant face; behind him four dark-clad men in black combat gear with empty hands; in the foreground {ASHJ}, and {FAAJ}, seen from behind, tense, facing him",
         camera=f"medium wide shot over Ashham's and Faahid's shoulders, eye level, {LOW} (steel floor)", amb="storm_night",
         sens="violence", safe="the mercenaries' guns aimed at Ashham and Faahid are never shown: a tense standoff with empty hands"),
    dict(to=74, reason="framing change: Vance's boast and the remote", chars=["vance"], loc="red_container",
         visual="close-up of Dr. Vance, an elderly European with silver slicked-back hair and a black overcoat, a cold contemptuous smile, holding up a small plain black remote device with no screen and no markings; blue vial glow on one side of his face, deck lights behind",
         camera=f"close-up, slightly low angle, {LOW}", amb="storm_night"),
    dict(to=77, reason="return to the container: the charge's red light counts down in silence", reuse="beat_022", loc="red_container",
         visual="reuse of beat_022", amb="storm_night"),
    dict(to=80, reason="back to Vance's arrogant laugh", reuse="beat_024", loc="red_container", visual="reuse of beat_024", amb="storm_night"),
    dict(to=84, reason="framing change: Ashham locks eyes with Vance and signals Habeeb", chars=["ashham"], loc="red_container",
         visual=f"close-up of {ASHJ}, unflinching, eyes locked straight ahead, one finger touching a small earpiece in his ear, the cold blue glow of the vials on his face, rain on his jacket",
         camera=f"close-up, eye level, {LOW}", amb="storm_night", hum=True),
    dict(to=86, reason="action change: Habeeb swings the ship's crane into Vance's men", loc="ship_deck",
         visual="the ship's huge crane arm swinging through the yellow deck lights, its thick steel cable and hook slamming into the side of the red container in a burst of sparks, four bearded men in black combat jackets, trousers and helmets ducking and looking up in alarm with empty hands; only men on the deck, no women anywhere",
         camera="wide low-angle shot, the crane in the upper two-thirds, the dark wet deck as the lower third", amb="storm_night"),
    dict(to=90, reason="action change: the shootout's aftermath — Faahid hit in the shoulder, Ashham covering him", chars=["faahid", "ashham"], loc="ship_deck",
         visual=f"{FAAJ}, sitting back against a container wall holding his left shoulder with his other hand, grimacing in pain; {ASHJ}, crouched protectively beside him, turning to look across the deck; drifting smoke and a few sparks on the container wall, no one else visible",
         camera=f"medium shot, eye level, {LOW} (wet steel deck)", amb="storm_night",
         sens="violence", safe="the shootout and the men falling are never shown; Faahid's wound only as him holding his shoulder and grimacing, no blood"),
    dict(to=92, reason="character change: Vance flees towards the bridge pressing his useless remote", chars=["vance"], loc="ship_deck",
         visual="Dr. Vance in his long black overcoat hurrying across the dark deck towards the lit bridge superstructure, his silver hair whipped by the wind, frantically pressing the buttons of a small black remote device, panic on his face",
         camera=f"medium wide shot, eye level, {LOW} (wet steel deck)", amb="storm_night"),
    dict(to=94, reason="action change: Ashham lifts the wounded Faahid onto his shoulders", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"{ASHJ}, rising to his feet carrying Faahid across his shoulders, his face set with determination; {FAAJ}, slumped over his shoulders, grimacing, eyes half closed; containers and smoke around them, deck lights",
         camera=f"medium shot, slightly low angle, {LOW} (wet steel deck)", amb="storm_night", hum=True),
    dict(to=96, reason="character change: Vance on the upper deck railing", loc="cargo_ship",
         visual="high on the cargo ship's upper deck, a lone elderly man in a long black overcoat with silver hair standing at the steel railing in silhouette against the yellow deck lights, his coat flapping in the wind, shouting down; seen from far below; nothing in his hands visible",
         camera="low angle from the sea far below, the figure small in the upper third against the night, the dark hull and black water below", amb="storm_night",
         sens="violence", safe="Vance's gun is never shown: only his silhouette at the railing"),
    dict(to=98, reason="action change: Habeeb's flare streaks up; a splash in the black sea", loc="cargo_ship",
         visual="a brilliant red flare streaking upward through the night from the small launch far below towards the ship's upper deck, bathing the dark hull in red light; at the foot of the towering hull a white splash bursting in the black waves",
         camera="wide shot from sea level, the red streak in the upper half, the splash and black water in the lower third", amb="storm_night",
         sens="violence", safe="the flare hitting Vance and his fall are never shown: only the flare's red streak and a splash in the waves"),
    dict(to=100, reason="action change: Ashham leaps from the deck into the sea carrying Faahid", loc="cargo_ship",
         visual="from a distance: two dark silhouettes of men, one holding the other tight, leaping off the high railing of the giant ship into the black sea, the ship's deck lights above them and the red glow of the dying flare, white spray below",
         camera="wide shot from the side, the leaping figures in the upper half, the black sea as the lower third", amb="storm_night", hum=True),
    # ---------------- EXPLOSION ON THE SEA
    dict(to=102, reason="action change: the MV Orion explodes and splits apart", loc="cargo_ship",
         visual="seen from far away across the black sea: a gigantic orange fireball erupting from the middle of the huge cargo ship as it splits in two, flames rising hundreds of feet into the night, steel fragments raining down into the sea, the whole sea lit orange; no one near the flames",
         camera="wide establishing shot, the fireball in the upper two-thirds, the orange-lit water as the lower third", amb="sea_search",
         sens="violence", safe="explosion as distant spectacle only, no people in it"),
    dict(to=106, reason="action change: Habeeb pulls Ashham and Faahid out of the sea; tears of joy", chars=["habeeb", "ashham", "faahid"], loc="coastguard_launch",
         visual=f"{HAB}, leaning over the side of the launch and gripping Ashham's hand to pull him up out of the dark water; {ASHJ}, soaked, reaching up from the waves; {FAAJ}, already sitting on the launch deck soaked and exhausted, holding his shoulder; far behind them the burning wreck of the ship sinking in an orange glow; everyone dusty and exhausted but unhurt",
         camera=f"medium shot from the launch's deck, eye level, {LOW} (dark wet deck)", amb="sea_search", hum=True),
    # ---------------- EPILOGUE
    dict(to=110, reason="time jump: three weeks later, a crowd outside police headquarters on a clear morning", loc="police_hq",
         visual="a big peaceful crowd of Maldivian citizens gathered on the sunny forecourt in front of the modern white police headquarters building, men in shirts and trousers and women in long loose dresses and hijabs, seen from behind and the side, golden morning light, a clear blue sky",
         camera="wide establishing shot, slightly high, the building and sky in the upper two-thirds, the paved forecourt as the lower third", amb="city_day", transition="black",
         sens="other", safe="the villains' life imprisonment is only narrated; no prison imagery needed"),
    dict(to=114, reason="scene change: the new Commissioner pins gold medals on Ashham and Habeeb", chars=["faahid", "ashham", "habeeb"], loc="commissioner_office",
         visual="Faahid, now the new Commissioner in a formal dark-navy dress uniform, his shoulder healed, pinning a gold medal on the chest of Ashham, who stands at attention in a formal dark-navy police dress uniform; Habeeb beside him in the same formal dress uniform with a gold medal already on his chest, glasses, smiling proudly",
         camera=f"medium three-shot, eye level, {LOW} (polished desk top and floor)", amb="office_day", hum=True),
    dict(to=117, reason="time and scene change: evening on Hulhumalé beach; Raniya comes to say goodbye", chars=["raniya", "ashham"], loc="hulhumale_beach",
         visual="Raniya in a soft cream long-sleeved ankle-length loose dress and a navy hijab fully covering her hair and neck, facing Ashham on the sand at a clear arm's-length distance, one hand pressed to her own heart, smiling gratefully; Ashham in his formal dark-navy police dress uniform with a gold medal, no cap, smiling gently; they do not touch",
         camera=f"medium two-shot from the side, eye level, {LOW} (sand and gentle surf)", amb="beach_evening", transition="black",
         sens="intimacy", safe="'she took his hand' is never shown: they face each other at arm's length, her hand on her own heart, no touching"),
    dict(to=119, reason="framing change: Ashham's unspoken feelings", chars=["ashham", "raniya"], loc="hulhumale_beach",
         visual="close-up of Ashham in his dark-navy dress uniform, looking at Raniya with quiet longing and words he cannot say, golden light on his face; Raniya soft and out of focus at arm's length in the foreground edge, her navy hijab fully covering her hair and neck",
         camera=f"close-up, eye level, {LOW}", amb="beach_evening", hum=True),
    dict(to=120, reason="action change: Raniya walks away to her father on the bench", chars=["raniya", "raniya_father", "ashham"], loc="hulhumale_beach",
         visual="Raniya in her cream dress and navy hijab walking away along the sand towards her father, a healthy older man with white stubble in a white long-sleeved shirt and a dark sarong sitting on a wooden bench under the palms in the distance; Ashham in the foreground seen from behind and to the side, standing still, watching her go",
         camera=f"medium wide shot over Ashham's shoulder, eye level, {LOW} (sand)", amb="beach_evening"),
    dict(to=122, reason="final image: Ashham alone on the beach looks up at the sky — THE END", loc="hulhumale_beach",
         visual="a tall man in a dark-navy dress uniform standing alone on the wide empty beach seen from behind, looking up at the glowing golden sky, gentle waves at his feet; two tiny figures far away at the end of the beach disappearing in the haze",
         camera="wide shot from behind, the figure and sky in the upper two-thirds, wet sand and surf as the calm lower third", amb="beach_evening", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "As the soldiers burst into the warehouse, Fairooz picked up the dangerous 'Project Phenix' syringe lying on the floor and drove it into his own neck.",
   [("boots_march", "ވަދެގަތް", -18)])
sh(2, "He wanted to wipe out his brain completely, along with all its secrets. \"Fairooz! No!\"", hum=True)
sh(3, "Ashham lunged forward, shouting. But it was too late. As the poison in the syringe emptied into Fairooz's body,",
   [("breath_heavy", "ފުންމާލިއެވެ", -20)], hum=True)
sh(4, "his eyes went wide and his whole body began to shake. White foam came from his mouth,", hum=True)
sh(5, "and within a few seconds he went still. He fell to the floor like a lifeless body.",
   [("soft_thud", "ވެއްޓުނީ", -23)], hum=True)
sh(6, "Minister Saleem, who had given him his orders, sank to his knees weeping in fear. The soldiers at once cuffed Saleem's hands and took him out of the warehouse.",
   [("sob_breath", "ރޮއެގަންނަމުން", -22), ("boots_march", "ގެންދިޔައެވެ", -22)])
sh(7, "\"Ashham, Fairooz has gone and taken many of the main secrets with him,\" Faahid said, putting his hand on Ashham's shoulder.")
sh(8, "\"But what matters most to us now is Habeeb. Naasir has taken him to Dhoonidhoo jail.\" \"Get a launch ready to go to Dhoonidhoo,\"")
sh(9, "Ashham said, wiping the blood from his lip. In an isolated cell of Dhoonidhoo jail, Habeeb lay tied to an iron bed.",
   [("metal_door", "ގޮޅިއެއްގެ", -22)])
sh(10, "His face was badly swollen. In front of him sat Naasir, holding a laptop. \"Habeeb,\"")
sh(11, "\"where is the master password of the secret accounts you hacked?\" Naasir asked loudly. \"All of Minister Saleem's money abroad is now frozen.")
sh(12, "Since that video leaked, the banks have been holding that money. We need your help to move it to a new account of the Minister's.",
   [("keyboard_typing", "އެކައުންޓަކަށް", -24)])
sh(13, "That's the only way you'll be saved.\" \"I... I won't tell,\" Habeeb said with difficulty. \"That money is...")
sh(14, "the blood and lives of so many people.\" Naasir glanced at his watch. \"I'll give you ten minutes. After that I'll start cutting off your fingers.\" Habeeb closed his eyes.",
   hum=True)
sh(15, "His heart was pounding. When they arrested him, they hadn't noticed the smartwatch on his wrist.",
   [("heartbeat", "ތެޅެމުން", -20)], hum=True)
sh(16, "That watch was something he had modified himself, a thing that could send signals in secret. Slowly he pressed one of the watch's buttons.",
   [("computer_beep", "އޮބާލިއެވެ", -22)])
sh(17, "With that, his location and the sound of the conversation inside the cell began to stream to a secret server. Race on the sea:")
sh(18, "Ashham and Faahid were aboard a military launch that had left Malé's lagoon. The launch was heading for Dhoonidhoo.",
   [("boat_engine", "ލޯންޗުގައި", -16)])
sh(19, "Suddenly a signal came onto Faahid's tablet in Ashham's hands. \"Sir! This is the signal from Habeeb's watch!\" Ashham shouted.",
   [("computer_beep", "ސިގްނަލެއް", -20)])
sh(20, "\"I can hear him!\" Naasir's voice began to come from the tablet. \"In ten minutes you will die...\"")
sh(21, "\"We have only eight minutes left,\" Faahid said, looking at the launch's captain. \"Full throttle!\"",
   [("engine_rev", "އިންޖީނު", -16)])
sh(22, "The launch entered Dhoonidhoo's lagoon and came alongside the jetty. The jail's security guards were startled to see the soldiers.",
   [("boat_engine", "ކައިރިކޮށްލިއެވެ", -20)])
sh(23, "Faahid used his official command and brought them under control. With an official warning the soldiers went ashore and got to work.",
   [("boots_march", "ރަށަށްއަރައި", -18)])
sh(24, "\"Naasir is trying to flee after committing a serious crime! Everyone, show us the way!\" Without waiting for anyone, Ashham broke into a run. Time up:",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -18)])
sh(25, "Naasir pressed the sharp knife in his hand against Habeeb's throat. \"Habeeb, time's up. Will you tell me the password?\"",
   [("heartbeat", "ޖައްސާލިއެވެ", -22)], hum=True)
sh(26, "Habeeb looked straight into Naasir's eyes. \"My death will bring these secrets to life.\" Naasir kicked Habeeb in the face.",
   [("soft_thud", "ޖެހިއެވެ", -24)], hum=True)
sh(27, "At that moment came the sound of the cell door opening. It was Ashham. \"Naasir! Hands up!\" Ashham shouted.",
   [("metal_door", "ހުޅުވާލި", -16)])
sh(28, "Startled, Naasir swung the knife towards Ashham. But Ashham was far quicker.")
sh(29, "Spinning round suddenly, his leg struck Naasir's shoulder. He went down at once. Then the soldiers came in and arrested Naasir on the spot.",
   [("soft_thud", "ޖެހުނީ", -23), ("boots_march", "ވަދެ", -20)])
sh(30, "Ashham ran over to Habeeb. \"Habeeb! Are you all right?\" Habeeb smiled faintly. \"Sir... I didn't change the master password.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(31, "But I've done something new.\" \"What?\" Ashham asked, helping Habeeb to his feet. The big leak: Habeeb tapped the watch on his wrist.")
sh(32, "\"Through this watch I've leaked all of Minister Saleem's and Moosa Thaahir's black-money transactions, and the secret documents sent to foreign companies, to the world's media and to Interpol.")
sh(33, "I pressed that button when time was running out.\" At once international news began arriving on Faahid's tablet.",
   [("computer_beep", "ޓެބްލެޓަށް", -20)])
sh(34, "The story of the huge medical mafia run jointly by the Maldives' Home Minister and tycoons made the headlines of the world's biggest TV channels.")
sh(35, "\"What you've done is extraordinary,\" Faahid said. \"Minister Saleem's network is now completely destroyed.\" But,")
sh(36, "worry still showed on Habeeb's face. \"Sir, but among those files I found something else.")
sh(37, "Minister Saleem isn't the one at the very top either. The big container loaded with Project Phenix's real drugs left Malé port about an hour ago, on its way to be loaded onto a secret foreign ship.",
   hum=True)
sh(38, "If those drugs spread around the world, many millions of people will be in danger.\" Ashham was ready. \"Where is that ship?\"")
sh(39, "\"It's out in the open sea off the east side of Malé,\" Habeeb said. Confrontation at sea:")
sh(40, "Though Habeeb's big leak had turned the whole world's attention to the Maldives, there was only a narrow chance to stop the shipment of Project Phenix's dangerous master drug.")
sh(41, "Leaving Dhoonidhoo jail, Ashham, Habeeb and Faahid boarded the military coast-guard launch. The waves were big. Black clouds covered the sky,",
   [("boat_engine", "ލޯންޗަށް", -18), ("wave_crash", "ރާޅުތައް", -20)])
sh(42, "and the wind rocked the launch from side to side. \"Sir, the radar shows a big cargo ship travelling in the open sea, the 'MV Orion',\" Zayaan said, looking at the screens in the launch's cockpit.",
   [("wind_gust", "ވައިރޯޅި", -20), ("computer_beep", "ސްކްރީންތަކަށް", -22)])
sh(43, "\"That ship is registered in the name of a secret foreign company. The container with the drugs has already been loaded onto it.")
sh(44, "They're heading out of Maldivian territorial waters.\" \"How long will it take us to reach that ship?\"")
sh(45, "Ashham asked, zipping his jacket up tight. \"At this speed, 1:45 minutes,\" Faahid answered.",
   [("cloth_rustle", "މަހާލަމުން", -20)])
sh(46, "\"But be careful. That ship is no ordinary cargo ship. There'll be armed foreign mercenaries aboard.\" With the powerful roar of the launch's three engines,",
   [("engine_rev", "އިންޖީނުގެ", -14)])
sh(47, "it surged forward. This was the last chance they would get to stop this dangerous crime from spreading around the world. The shadow of the big ship:",
   hum=True)
sh(48, "Out of the pitch darkness of the sea, the huge silhouette of the 'MV Orion' began to appear. It was a big steel ship.", hum=True)
sh(49, "In the dim lights on the ship's deck, the giant containers could be seen stacked up. As the military launch began to close in on the ship,")
sh(50, "the beam of a powerful searchlight from the ship fell straight on the launch. And then, without any warning, automatic fire poured down from the ship's deck.",
   [("metal_clang", "ހަމަލާތައް", -18)])
sh(51, "Bullets struck all over the launch, sparks flying. \"Get down! Get down!\" Faahid shouted, swinging the launch's wheel.",
   [("metal_clang", "ވަޒަންތައް", -18)])
sh(52, "Ashham came out to the stern, aimed the powerful rifle in his hand at the searchlight on the ship and fired. With a single bullet the searchlight burst,",
   [("soft_thud", "ޖެހިއެވެ", -24), ("glass_break", "ގޮވައި", -14)])
sh(53, "and that side of the ship went dark. Seizing the chance, Faahid brought the launch alongside the steel ladder fixed to the ship's stern.",
   [("boat_engine", "ކައިރިކޮށްލިއެވެ", -20)])
sh(54, "\"Habeeb, you stay in the launch. Work on blocking the ship's systems,\" Ashham said.")
sh(55, "\"We're going up.\" Ashham and Faahid carefully began to climb the ship's steel ladder.",
   [("metal_clang", "ސިޑިން", -22)])
sh(56, "Because of the huge waves the ship was rolling hard from side to side. The deck fight: as Ashham climbed onto the ship's main deck,",
   [("wave_crash", "ރާޅުތަކުގެ", -18)])
sh(57, "two armed men came out from behind the containers. They were in black combat gear.",
   [("boots_march", "ނުކުތެވެ", -20)])
sh(58, "Rolling across the deck, Ashham fired; the bullets struck them squarely in the chest, and they fell to the deck.",
   [("soft_thud", "ވެއްޓުނެވެ", -24)])
sh(59, "Faahid climbed up too and covered Ashham's back. They moved along the narrow lanes between the containers to find the container holding the Project Phenix drugs.",
   [("footsteps_pavement", "ކުރިއަށް", -24)])
sh(60, "Thanks to information Habeeb had given them earlier, they knew it was a red container marked with a secret number. \"Ashham, on the right!\"")
sh(61, "Faahid shouted. From the top of a container above, someone threw a grenade towards them.",
   [("metal_clang", "އެއްލިއެވެ", -22)])
sh(62, "As Ashham and Faahid dived to either side, there was a powerful explosion. The force of the blast tore parts of the steel containers apart, and smoke and fire spread.",
   [("distant_boom", "ގޮވުމެއް", -12), ("fire_crackle", "އަލިފާން", -20)])
sh(63, "Summoning his courage, Ashham rose to his feet and sent a bullet into the forehead of the man on top. The red container: walking on through the smoke,",
   [("soft_thud", "ފޮނުވާލިއެވެ", -24)])
sh(64, "around the middle of the ship they saw the red container. A big electronic lock was fitted on its door. \"Habeeb,")
sh(65, "we've reached the container,\" Ashham said over the walkie-talkie. \"Bypass the system to open its lock.\" In the launch, Habeeb's hands flew over the keyboard.",
   [("keyboard_typing", "ކީބޯޑުގައި", -16)])
sh(66, "\"Sir, I'm into the ship's main server now. The lock opens... now!\" The container's big steel door opened. As Ashham pulled the door open,",
   [("computer_beep", "ހުޅުވޭނީ", -20), ("metal_door", "ހުޅުވުނެވެ", -16)])
sh(67, "inside were special refrigerated racks. And on those racks stood bottles of Project Phenix's blue liquid drug.",
   [("steam_hiss", "ފިނިކުރި", -22)])
sh(68, "There were many thousands of vials. \"All of this has to be destroyed,\" Faahid said. He took powerful explosives from his bag and began fixing them in the middle of the container.",
   [("cloth_rustle", "ދަބަހުން", -22)])
sh(69, "\"I'm setting the timer to five minutes. We have to get off this ship fast.\" The mastermind's confrontation: just as Faahid started the timer,",
   [("computer_beep", "ޖައްސާލި", -20)])
sh(70, "a man's shadow fell across the container's doorway. Ashham raised his gun towards it, but stopped because of who he saw. It was a man in a black coat,",
   [("footsteps_pavement", "ހިޔަންޏެއް", -22)], hum=True)
sh(71, "an elderly foreigner. With him were four armed men. Their guns were aimed straight at Faahid's and Ashham's chests. \"Who do you think you are!")
sh(72, "Did you come here to wage war on a Maldivian minister?\" the man said in English. \"I am the owner of this project. Doctor Vance.")
sh(73, "Your country's ministers are just little boys working for my money.\" Vance showed them a small device in his hand.")
sh(74, "\"The bomb you planted can be deactivated with this remote of mine. And you two will go to the bottom of this sea tonight.\"")
sh(75, "The timer of the bomb in the container stood at '04:00'. As the time ran down, on the ship's deck the last,",
   [("computer_beep", "ޓައިމަރު", -22)], hum=True)
sh(76, "most dangerous confrontation was under way. The bullets in Ashham's gun were running low. The last seconds:")
sh(77, "As the bomb timer fixed inside the red container showed '03:45', a silence reigned over the whole place.",
   [("heartbeat", "ހިމޭންކަމެކެވެ", -20)], hum=True)
sh(78, "Extreme arrogance showed on Doctor Vance's face. The guns of the four armed men behind him were aimed straight at Ashham's and Faahid's chests. \"Ashham, did you think you were a hero?\"")
sh(79, "Vance burst out laughing. \"People of little island nations like yours, in front of great scientists and tycoons like us, are nothing but little test")
sh(80, "mice. These drugs will go out to the world tonight. And you two will turn to ash right here.\"")
sh(81, "Without lowering his gun, Ashham looked straight into Vance's eyes. His mind was calculating faster with every second.", hum=True)
sh(82, "He had only three bullets left. Faahid's gun didn't have many bullets either. \"Vance,")
sh(83, "do you think you can control everything with your remote?\" Ashham said slowly.")
sh(84, "\"Your ship's main system is now under our control.\" Through the earpiece in his ear, Ashham sent a secret code to Habeeb. \"Habeeb...",
   [("computer_beep", "އިއަރޕީސްއިން", -22)], hum=True)
sh(85, "now!\" At that moment the big crane on the ship suddenly began to swing. Habeeb, in the launch, had hacked the ship's hydraulic system and swung the crane straight at where Vance and his men stood.",
   [("creak", "ކްރޭން", -18), ("steam_hiss", "ހައިޑްރޯލިކް", -20)])
sh(86, "The huge steel cable slammed into the side of the container. At the loud crash Vance's men looked up, startled, and in that moment",
   [("metal_clang", "ޖެހުނެވެ", -14)])
sh(87, "Ashham and Faahid dived down together and opened fire. Sea of blood: with Ashham's perfect aim the bullets struck the chests of the two armed men in front, and they dropped to the deck at once.",
   [("soft_thud", "ބަޑިޖަހަން", -23)])
sh(88, "Faahid brought down one of the other two. But the last man left fired at Faahid. The bullet struck Faahid's shoulder.",
   [("soft_thud", "ބަޑިޖަހާލިއެވެ", -23)])
sh(89, "Faahid cried out and stumbled backwards. \"Faahid sir!\" Ashham shouted,",
   [("gasp", "ހަޅޭއްލަވައިގަންނަމުން", -20)], hum=True)
sh(90, "threw away his empty gun, picked up the gun of the man lying on the deck and sent a bullet into the last man's head. Doctor Vance backed away in fear,",
   [("soft_thud", "ފޮނުވާލިއެވެ", -24)])
sh(91, "came out of the container and ran towards the ship's cockpit. He kept pressing the buttons of the remote in his hand to deactivate the bomb.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)])
sh(92, "But because Habeeb had locked the bomb's system too, the remote didn't work. The timer was showing '01:30'.",
   [("computer_beep", "ޓައިމަރުން", -20)])
sh(93, "Only a minute and thirty seconds were left. Ashham ran over and knelt beside Faahid. Blood was pouring from Faahid's shoulder. \"Ashham...",
   hum=True)
sh(94, "leave me and go... the ship's going to blow...\" \"No, I won't leave you behind, sir,\" Ashham said, lifting Faahid onto his shoulder.",
   [("breath_heavy", "އުފުލާލައި", -20)], hum=True)
sh(95, "As he broke into a run, Doctor Vance came out onto the ship's upper deck holding a gun and aimed at Ashham's legs. \"None of you will survive!\"",
   [("footsteps_pavement", "ދުއްވައިގަތް", -20)])
sh(96, "Vance shouted. But at that moment, from below the ship, Habeeb, standing on the military launch, fired the launch's powerful flare gun up at the ship.",
   [("steam_hiss", "ފްލެއާ", -16)])
sh(97, "The blazing flare struck Vance full in the face. Crying out, he toppled backwards over the ship's steel railing and fell into the huge waves of the sea.",
   [("splash", "ވެއްޓުނެވެ", -16)])
sh(98, "He sank completely into the darkness of the sea. The explosion on the sea: \"Thirty seconds on the timer! Ashham sir, jump!\"",
   [("alarm_beep", "ޓައިމަރުގައި", -20)], hum=True)
sh(99, "Habeeb shouted from below. Holding Faahid tight against his chest, Ashham leapt from the ship's upper deck straight into the sea.",
   [("wind_gust", "ފުންމާލިއެވެ", -18)], hum=True)
sh(100, "The second they plunged into the waves was the second the bomb's timer reached '00:00'. \"Boom!\"",
   [("splash", "ގަނބައިގަތް", -14), ("distant_boom", "ބޫމް", -12)])
sh(101, "With an extraordinarily powerful explosion, the 'MV Orion' split apart in the middle. All of Project Phenix's chemicals and drugs became a huge ball of fire,",
   [("distant_boom", "ގޮވުމަކާއެކު", -14), ("fire_crackle", "އަލިފާނުގެ", -18)])
sh(102, "and the flames rose many feet into the air. The ship's big steel pieces rained down into the sea.",
   [("splash", "ބުރައިގެން", -22)])
sh(103, "The powerful wave of the explosion lifted the sea and pushed Ashham and Faahid far away. Carefully, Habeeb drove the launch forward,",
   [("wave_crash", "ރާޅާއެކު", -16), ("boat_engine", "ދުއްވާލައި", -20)])
sh(104, "pulled Ashham and Faahid out of the sea and got them into the launch. Slowly the big ship sank to the bottom of the sea.",
   [("splash", "ނަގައި", -20)])
sh(105, "The deadly plague of Project Phenix was buried in the deepest part of the sea before it could spread around the world. \"We... we've done it.\"",
   hum=True)
sh(106, "Habeeb said, taking a deep breath. Tears of joy ran from his eyes. A new day: three weeks later.",
   [("sigh", "މާނޭވައެއް", -20)], hum=True)
sh(107, "The sky over Malé was clear. As the golden rays of morning fell on the streets, a large crowd of citizens had gathered in front of the Shaheed Hussain Adam Building.")
sh(108, "With this great betrayal and murder at the very top of the state fully exposed, a big change had come over the country's political climate.")
sh(109, "Former Home Minister Saleem, tycoon Moosa Thaahir and the senior jail officer Naasir had been arrested and were in prison.")
sh(110, "Many charges had been brought against them. They would have to spend the rest of their lives in prison.")
sh(111, "Former Commissioner Faahid had been appointed the new Commissioner of the police. The wound to his shoulder had now healed.")
sh(112, "Ashham and Habeeb were in the new Commissioner's office, wearing the police's highest uniform of honour. \"Ashham, Habeeb.",
   [("footsteps_pavement", "އޮފީސް", -24)])
sh(113, "You two have saved the nation,\" Faahid said, pinning gold medals on their chests. \"Naail's death has received justice.\"",
   [("cloth_rustle", "ހަރުކޮށްދެމުން", -22)], hum=True)
sh(114, "\"Thank you, sir,\" Ashham said, saluting. In the evening, Ashham stood on the Hulhumalé beach.")
sh(115, "The waves were rolling gently onto the shore. Walking slowly towards him came Doctor Raniya. \"Ashham,\" Raniya said softly.",
   [("footsteps_sand", "ހިނގާލާފައި", -22)])
sh(116, "\"We're going back to the island tomorrow.\" \"A good decision,\" Ashham smiled. \"The island needs good doctors like you.\"")
sh(117, "\"Without your help we would never have survived,\" Raniya said, taking Ashham's hand. \"Thank you,\" Raniya said softly.")
sh(118, "Ashham looked into Raniya's eyes. What he wanted to say was something else. Other feelings were welling up in his heart.", hum=True)
sh(119, "But he could not find the courage to reveal these feelings. On a bench some distance away sat Raniya's father. He was completely well now.")
sh(120, "After saying goodbye, Raniya walked off in that direction, as if waiting for Ashham to say something. But he just stood there.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(121, "His words had stopped. All he could manage was a smile. After Raniya left, Ashham stood alone on the beach for a long time.", hum=True)
sh(122, "Until Raniya, leaving with her father, disappeared from sight, he kept looking that way. When she vanished from view, he looked up at the sky. — The End.",
   hum=True)

SHOTS = S

"""Beat/shot plan for Project Phenix episode 324 — the FINALE, v2 re-cut on the new audio (used by plan_beats.py).
v1 images are reused with v1="beat_###" (old image file); new images only for spec 5.4 (speaker centred) and fixes."""

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
# v2: Habeeb as he looks in the v1 images of this episode (his card outfit), for the new images
HABN = "Habeeb in his dark-grey zip-up jacket over a plain white T-shirt, black-rimmed glasses with a thin crack across one lens, tired and dusty but unmarked"
OTS = "medium close-up over the listener's shoulder, eye level, the speaker's face centred in the upper half and in sharp focus, the listener soft and out of focus at the edge"

BEATS = [
    # ---------------- WAREHOUSE
    dict(to=1, v1="beat_001", reason="episode opening: the warehouse as soldiers storm in; Fairooz seizes the glowing vial", chars=["fairooz"], loc="warehouse",
         visual=f"Fairooz in his rumpled dark-navy senior police uniform, no cap, crouched low on the concrete floor beside an overturned steel tray, clutching a small glass vial of glowing blue liquid tightly to his chest with both hands, his eyes wild and desperate; behind him through the smoke, {SOLD}, pour in through the blown-open steel door with bright flashlight beams",
         camera=f"medium shot, slightly low angle, {LOW} (concrete floor)", amb="storage_hall",
         sens="violence", safe="the syringe and Fairooz injecting himself are never shown: only Fairooz clutching a small glowing blue glass vial; no needle"),
    dict(to=5, v1="beat_002", reason="action change: Ashham lunges too late; Fairooz's end is shown only by the empty vial", chars=["ashham"], loc="warehouse",
         visual=f"in the foreground a small empty glass vial with a last faint blue glow rolling on the bare concrete floor; behind it, slightly out of focus, {ASH}, frozen mid-lunge with one arm reaching out, his face twisted in anguish and shock; two soldiers in black combat gear at the edge of the frame turning their faces away",
         camera=f"low angle from floor level, the vial in sharp focus at lower middle, Ashham's face in the upper third, {LOW}", amb="storage_hall", hum=True,
         sens="death", safe="Fairooz's convulsions, foam and collapse are never shown, no lying figure, no covered shape: only the empty glowing vial rolling on the floor and the frozen faces"),
    dict(to=6, v1="beat_003", reason="action change: Saleem kneels weeping and is led out; Faahid's hand on Ashham's shoulder", chars=["faahid", "ashham", "saleem"], loc="warehouse",
         visual=f"{FAAJ} resting a hand on Ashham's shoulder and speaking gravely; {ASH}, standing with a hard, exhausted face; in the background under the hanging lamp the Home Minister Saleem in his black three-piece suit on his knees on the floor with his face in his hands, two soldiers in black combat gear standing beside him ready to lead him away",
         camera=f"medium two-shot, eye level, Saleem small in the background, {LOW} (concrete floor)", amb="storage_hall",
         sens="other", safe="Saleem's arrest shown without handcuffs; Ashham's split lip not shown"),
    dict(to=8, speaker="faahid", reason="5.4 dialogue: Faahid speaks to Ashham (in the v1 two-shot his face is at the far left edge, x≈13 %)", chars=["faahid", "ashham"], loc="warehouse",
         visual=f"{FAAJ}, facing the camera, his face centred in the upper half and in sharp focus, speaking gravely with a weary, serious face, his right hand resting on the shoulder of {ASH}, who is seen from behind and slightly to the side at the left edge of the frame, soft and out of focus; behind them in the smoky warehouse under the warm hanging lamp, blurred soldiers in black combat gear with flashlights",
         camera=f"{OTS} (Ashham's shoulder), {LOW} (dark jackets and concrete floor)", amb="storage_hall", transition="cut"),
    # ---------------- DHOONIDHOO CELL
    dict(to=9, v1="beat_004", reason="scene change: Habeeb held in a Dhoonidhoo cell, Naasir interrogating him with a laptop", chars=["habeeb", "naasir"], loc="dhoonidhoo_cell",
         visual=f"{HAB}, sitting on the edge of the steel bunk with his hands behind his back out of view, head raised defiantly; facing him a few steps away Naasir in his black suit sits on a steel chair with an open laptop on his knees (screen facing away from the viewer), leaning forward with a cold, menacing stare",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (bare concrete floor)", amb="detention_room",
         sens="violence", safe="Habeeb 'tied to an iron bed' with a badly swollen face = seated on a steel bunk, hands out of view, tired but unmarked; the threat to cut his fingers is only spoken"),
    dict(to=13, speaker="naasir", reason="5.4 dialogue: Naasir interrogates Habeeb (v1 shows him only in side profile at the right edge) — shot", chars=["naasir"], loc="dhoonidhoo_cell",
         visual="Naasir in his black suit sitting on a plain steel chair facing the camera, his face centred in the upper half and in sharp focus, an open laptop on his knees with its screen facing away from the viewer, leaning forward and speaking with a cold, menacing stare; in the near foreground at the left edge the head and shoulder of a young man with short messy black hair in a dark-grey jacket, seen from behind, soft and out of focus, sitting on a steel bunk; bare grey concrete walls, a small barred window high behind Naasir",
         camera=f"{OTS} (Habeeb's shoulder), {LOW} (the laptop lid and dark floor)", amb="detention_room",
         sens="violence", safe="the threats are only spoken; nobody is touched, Habeeb is seen from behind and unmarked"),
    dict(to=14, speaker="habeeb", reason="5.4 dialogue: Habeeb answers Naasir — reverse shot", chars=["habeeb"], loc="dhoonidhoo_cell",
         visual=f"{HABN}, sitting on the edge of a steel bunk with a thin grey blanket, his hands behind his back out of view, facing the camera, his face centred in the upper half and in sharp focus, looking up and speaking with difficulty but calm defiance, tired eyes; in the near foreground at the right edge the dark shoulder and back of a bald man in a black suit, soft and out of focus, standing a few steps away",
         camera=f"{OTS} (Naasir's shoulder), slightly high angle, {LOW} (grey blanket and concrete floor)", amb="detention_room", transition="cut",
         sens="violence", safe="Habeeb 'tied to an iron bed' with a swollen face = seated, hands out of view, tired but unmarked"),
    dict(to=16, reuse="beat_006", reason="back to Naasir: he gives Habeeb ten minutes (shot / reverse shot)", loc="dhoonidhoo_cell",
         visual="reuse of beat_006", amb="detention_room", transition="cut"),
    dict(to=18, v1="beat_005", reason="detail: the hidden smartwatch Habeeb secretly presses", loc="dhoonidhoo_cell",
         visual="extreme close-up of a young man's wrist in a dark-navy shirt cuff resting on a grey blanket on a steel bunk: a slim plain black smartwatch with a soft blue glow and a blank screen, his fingertip quietly pressing its side button; the rest of the cell dark and out of focus",
         camera="extreme close-up, the wrist and watch in the upper-middle of the frame, the grey blanket as the calm lower third", amb="detention_room", hum=True),
    # ---------------- RACE ON THE SEA
    dict(to=22, v1="beat_006", reason="scene change: Ashham and Faahid race across the lagoon to Dhoonidhoo on a military launch", chars=["ashham", "faahid"], loc="mndf_launch",
         visual=f"{ASHJ}, standing at the rail of the speeding dark-grey military launch holding a glowing tablet (screen showing only soft blurred light), {FAAJ}, leaning in beside him listening intently; white spray flying off the bow, two soldiers in black combat gear and a launch captain at the wheel behind them",
         camera=f"medium shot on the deck, eye level, {LOW} (dark wake and water)", amb="sea_boat"),
    dict(to=25, v1="beat_007", reason="scene change: the launch reaches Dhoonidhoo jetty; Faahid commands the guards; Ashham runs", chars=["ashham", "faahid"], loc="dhoonidhoo_jetty",
         visual=f"the dark-grey launch moored at the concrete jetty, {SOLD}, stepping ashore; two startled jail security guards in light-blue uniform shirts stepping back with empty hands; {FAAJ}, stepping forward with one hand raised in command; {ASHJ}, already running along the jetty towards the low detention buildings",
         camera=f"medium wide shot, eye level, {LOW} (concrete jetty and dark water)", amb="night_exterior"),
    # ---------------- TIME UP
    dict(to=27, speaker="naasir", reason="scene change back to the cell + 5.4: Naasir's last threat, his face centred (the v1 image showed him in profile looking down)", chars=["naasir"], loc="dhoonidhoo_cell",
         visual="Naasir in his black suit standing by the small barred window of the cell, facing the camera, his face centred in the upper half and in sharp focus, glaring down and speaking with cold menace, his hands empty and hanging at his sides; in the near foreground at the lower left edge the soft out-of-focus head and shoulder of a young man with glasses in a dark-grey jacket sitting on the steel bunk, seen from behind, several steps away from Naasir",
         camera=f"medium shot from Habeeb's side, slightly low angle, Naasir's face centred in the upper half, {LOW} (dark concrete floor)", amb="detention_room", hum=True,
         sens="violence", safe="the knife at Habeeb's throat is never shown: Naasir stands at a distance by the window, hands empty"),
    dict(to=28, reuse="beat_007", reason="Habeeb answers Naasir (reverse shot); the kick is never shown", loc="dhoonidhoo_cell",
         visual="reuse of beat_007", amb="detention_room", transition="cut",
         sens="violence", safe="the kick is never shown: only Habeeb's defiant face and a faint offscreen thud"),
    dict(to=29, speaker="ashham", reason="character enters + 5.4: Ashham bursts in and shouts (in the v1 image he is small at the far left edge, x≈21 %)", chars=["ashham"], loc="dhoonidhoo_cell",
         visual=f"{ASHJ}, standing in the open heavy steel cell doorway with bright corridor light behind him, facing the camera, his face centred in the upper half and in sharp focus, one open empty palm raised in command, shouting with a fierce face; at the right edge of the frame in the foreground the soft out-of-focus shoulder of a bald man in a black suit turning round",
         camera=f"medium close-up from inside the cell, slightly low angle, Ashham's face centred in the upper half, {LOW} (dark doorway floor)", amb="detention_room", transition="cut",
         sens="violence", safe="a standoff at a distance, hands empty; no knife"),
    dict(to=30, v1="beat_009", reason="character enters: the cell door bursts open and Ashham stands in the doorway", chars=["ashham", "naasir"], loc="dhoonidhoo_cell",
         visual=f"{ASHJ}, standing in the open steel cell doorway with bright corridor light behind him, one open palm raised in command, his face fierce; across the cell Naasir in his black suit spinning round from the window, startled, his hands empty",
         camera=f"medium wide shot from inside the cell, eye level, {LOW} (concrete floor)", amb="detention_room",
         sens="violence", safe="Naasir turning the knife on Ashham is never shown; a tense standoff at a distance, hands empty"),
    dict(to=32, v1="beat_010", reason="action change: Naasir led away by soldiers; Ashham goes to Habeeb", chars=["ashham", "habeeb", "naasir"], loc="dhoonidhoo_cell",
         visual=f"in the background two soldiers in black combat gear leading Naasir out through the steel door, his hands behind his back; in the foreground {ASHJ}, crouching beside the steel bunk with a hand on Habeeb's shoulder, worried; {HAB}, smiling weakly up at him",
         camera=f"medium shot, eye level, {LOW} (concrete floor)", amb="detention_room",
         sens="violence", safe="Ashham's spinning kick and Naasir's fall are never shown: only the aftermath, Naasir escorted out with hands behind his back, no cuffs"),
    dict(to=33, speaker="habeeb", reason="5.4 dialogue: Habeeb answers Ashham with a weak smile (in the v1 image his face is at the left edge, x≈21 %)", chars=["habeeb"], loc="dhoonidhoo_cell",
         visual=f"{HABN}, sitting on the edge of the steel bunk, facing the camera, his face centred in the upper half and in sharp focus, smiling weakly and speaking with tired but proud eyes; at the left edge of the frame a man in a black tactical jacket crouching beside him, seen from behind and soft out of focus, one hand on Habeeb's shoulder",
         camera=f"{OTS} (Ashham's shoulder), {LOW} (grey blanket and concrete floor)", amb="detention_room", transition="cut"),
    dict(to=34, reuse="beat_016", reason="back to Ashham as he asks and helps Habeeb up (shot / reverse shot)", loc="dhoonidhoo_cell",
         visual="reuse of beat_016", amb="detention_room", transition="cut"),
    # ---------------- BIG LEAK
    dict(to=39, v1="beat_011", reason="action change: Habeeb reveals the leak through his watch; world news fills Faahid's tablet", chars=["habeeb", "faahid", "ashham"], loc="dhoonidhoo_cell",
         visual=f"{HAB}, now standing, raising his wrist to show a slim black smartwatch with a soft glow, a tired proud smile; {FAAJ}, holding a tablet that glows with blurred news-like layouts and soft coloured blocks (no readable text), amazed; {ASHJ}, leaning in to look, faces lit blue by the screen",
         camera=f"medium three-shot, eye level, {LOW} (concrete floor in shadow)", amb="detention_room"),
    dict(to=44, speaker="habeeb", reason="emotional turning point + 5.4: Habeeb's new fear, his face centred (in the v1 close two-shot it sits at x≈21 %)", chars=["habeeb"], loc="dhoonidhoo_cell",
         visual=f"close-up of {HABN}, standing, facing the camera, his face centred in the upper half and in sharp focus, anxious and urgent, eyebrows drawn together, speaking; at the right edge of the frame the soft out-of-focus shoulder and jaw of a tall man in a black tactical jacket listening, seen from behind and to the side",
         camera=f"close-up over Ashham's shoulder, eye level, {LOW} (dark jacket and shadow)", amb="detention_room", hum=True),
    # ---------------- COAST-GUARD LAUNCH
    dict(to=46, v1="beat_013", reason="scene change: the coast-guard launch heads out onto the rough night sea", loc="coastguard_launch",
         visual="the dark-grey MNDF coast-guard launch with no markings ploughing through big black waves under heavy black clouds, white spray bursting over its bow, three small figures visible behind its lit cockpit windows, a faint flash of lightning on the horizon",
         camera="wide shot from the side, slightly high, the launch in the upper half, the dark heaving sea as the lower third", amb="sea_search"),
    dict(to=48, speaker="habeeb", reason="scene change to the cockpit + 5.4: Habeeb reports the MV Orion on radar (in the v1 cockpit image his face is at x≈24 %)", chars=["habeeb"], loc="coastguard_cockpit",
         visual=f"{HABN}, seated at the glowing radar and navigation screens in the dark cockpit, turned three-quarter towards the camera, his face centred in the upper half and in sharp focus, lit blue-green by the screens, speaking urgently while pointing at a bright blip on a screen (blurred shapes only, no numbers); behind him, soft and out of focus, a grey-haired man in a black tactical jacket at the steering wheel; rain and spray streaming down the dark windows",
         camera=f"medium close-up, eye level, Habeeb's face centred in the upper half, {LOW} (dark console)", amb="sea_search"),
    dict(to=52, v1="beat_014", reason="scene change: in the cockpit Habeeb finds the MV Orion on radar; Ashham zips his jacket", chars=["ashham", "habeeb", "faahid"], loc="coastguard_cockpit",
         visual=f"{HAB}, seated at the glowing radar and navigation screens (blurred shapes only, no numbers), pointing at a bright blip; {FAAJ}, gripping the steering wheel; {ASHJ}, standing behind them zipping his black tactical jacket up to his chin with a hard, determined face",
         camera=f"medium three-shot inside the cockpit, eye level, {LOW} (dark console)", amb="sea_search"),
    # ---------------- THE SHIP
    dict(to=56, v1="beat_015", reason="scene change: the MV Orion looms out of the dark; its searchlight and fire hit the launch", loc="cargo_ship",
         visual="the huge dark silhouette of the steel cargo ship rising out of the night sea, containers stacked high under dim yellow deck lights, a tall crane; from its deck a blinding white searchlight beam glares down onto the small dark-grey launch in the foreground waves, bright sparks flicking off the launch's metal rail, white spray everywhere; no one visible on the ship",
         camera="wide low angle from sea level, the ship towering in the upper two-thirds, black water as the lower third", amb="storm_night",
         sens="violence", safe="automatic fire shown only as the searchlight glare and sparks on the launch's rail, no weapons, no one hit"),
    dict(to=57, reuse="beat_023", reason="5.4 dialogue: Faahid shouts 'Get down!' at the wheel — back to the cockpit image, cropped on Faahid", loc="coastguard_cockpit",
         visual="reuse of beat_023", amb="storm_night"),
    dict(to=58, v1="beat_016", reason="action change: Ashham at the stern; the searchlight shatters into darkness", loc="cargo_ship",
         visual="a tall man in a black tactical jacket seen from behind in silhouette at the stern of the small launch, facing the giant ship; high up on the ship's deck the searchlight bursting into a shower of white sparks and glass, its beam dying, that side of the ship falling into darkness",
         camera="medium wide shot from behind the man, low angle, the ship and burst of sparks in the upper half, dark water as the lower third", amb="storm_night",
         sens="violence", safe="Ashham's rifle shot is never shown: his silhouette from behind with nothing in his hands visible, only the searchlight bursting"),
    dict(to=59, speaker="ashham", reason="5.4 dialogue: Ashham orders Habeeb to stay in the launch (no v1 image shows his face here)", chars=["ashham"], loc="cargo_ship",
         visual=f"{ASHJ}, soaked by spray, standing in the rocking dark-grey launch at the foot of a steel ladder on the towering dark wet hull of the cargo ship, turned towards the camera, his face centred in the upper half and in sharp focus, one hand gripping a ladder rung, giving an order with a hard, determined face; in the near foreground at the lower right the soft out-of-focus head and shoulder of a young man with glasses in a dark-grey jacket, seen from behind; white spray, rain, dim deck lights far above",
         camera=f"{OTS} (Habeeb's shoulder), slightly low angle, {LOW} (dark wet deck of the launch)", amb="storm_night"),
    dict(to=60, v1="beat_017", reason="action change: the launch alongside the stern ladder; Ashham and Faahid climb, Habeeb stays below", chars=["habeeb", "ashham", "faahid"], loc="cargo_ship",
         visual=f"looking up the towering dark steel stern of the ship: {ASHJ}, and {FAAJ}, climbing a steel ladder up the wet hull, seen from below and behind; in the foreground {HAB}, standing in the rocking launch with a laptop in a waterproof bag under his arm, looking up anxiously; big waves and spray",
         camera=f"low angle from the launch, the climbers in the upper half, {LOW} (dark sea and the launch's deck)", amb="storm_night"),
    # ---------------- DECK FIGHT
    dict(to=65, v1="beat_018", reason="scene change: on deck, Ashham and Faahid move through the container lanes; a figure appears above", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"{ASHJ}, and {FAAJ}, crouched low and moving fast along a narrow lane between towering stacked containers, flashlight beams sweeping through the rain; on the deck ahead a dropped flashlight lies alone lighting the empty lane; high above on top of a container a crouched dark silhouette against the deck lights; Faahid pointing up and to the right in alarm",
         camera=f"medium wide shot down the lane, eye level, {LOW} (wet steel deck)", amb="storm_night",
         sens="violence", safe="the two mercenaries and their fall are never shown: only an empty lane and a dropped flashlight; the grenade is not shown"),
    dict(to=66, v1="beat_019", reason="action change: the blast between the containers", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"a bright orange fireball blooming far down the lane between the towering containers, smoke billowing, steel container doors bent outward; in the foreground, well away from the flames, {ASHJ}, and {FAAJ}, crouched low on the wet deck at two different container corners, shielding their heads with their arms, seen from behind and the side, unhurt; only these two men in the whole scene, no other people, no women",
         camera="wide shot, eye level, the fireball in the upper half, the dark wet deck as the lower third", amb="storm_night",
         sens="violence", safe="the grenade blast shown as distant spectacle with the two men diving clear, no one in the flames"),
    dict(to=69, v1="beat_020", reason="action change: through the smoke they reach the red container with the electronic lock", chars=["ashham", "faahid"], loc="red_container",
         visual=f"through drifting smoke mid-ship, a plain red steel container with no markings and a big electronic lock on its door (a blank glowing panel, no keys or digits); {ASHJ}, approaching it with one finger pressed to a small earpiece, speaking; {FAAJ}, behind him watching their backs",
         camera=f"medium wide shot, eye level, {LOW} (wet steel deck)", amb="storm_night"),
    dict(to=70, v1="beat_021", reason="character change: Habeeb in the launch hacks the ship's server", chars=["habeeb"], loc="coastguard_cockpit",
         visual=f"{HAB}, hunched over a laptop in the launch's cockpit, typing fast with intense concentration, the screen glow (blurred shapes only) lighting his face and cracked glasses, spray streaming down the window behind which the dark hull of the giant ship towers",
         camera=f"medium close-up, eye level, {LOW} (dark console)", amb="sea_search"),
    dict(to=72, v1="beat_022", reason="action change: the container opens on thousands of glowing blue vials; Faahid sets the charge", chars=["ashham", "faahid"], loc="red_container",
         visual=f"inside the open red container: cold steel racks holding thousands of small glass vials glowing eerie blue; {ASHJ}, holding the heavy door open in the doorway, staring in; {FAAJ}, kneeling in the middle of the racks placing a small black case with a blinking red light (no digits, no screen)",
         camera=f"medium wide shot from inside the container looking out, eye level, {LOW} (steel floor in blue shadow)", amb="storm_night",
         sens="violence", safe="the explosives and timer shown only as a small black case with a blinking red light, no digits"),
    dict(to=74, speaker="faahid", reason="5.4 dialogue: Faahid speaks while setting the charge (in the v1 image he looks down, face hidden)", chars=["faahid"], loc="red_container",
         visual=f"inside the open red container among cold steel racks of small glass vials glowing eerie blue: {FAAJ}, kneeling beside a small black case with a blinking red light on the steel floor (no digits, no screen), looking up towards the camera, his face centred in the upper half and in sharp focus, speaking urgently; at the right edge a tall man in a black tactical jacket seen from behind, soft and out of focus",
         camera=f"medium close-up, slightly high angle, Faahid's face centred in the upper half, {LOW} (steel floor in blue shadow)", amb="storm_night",
         sens="violence", safe="the explosives and timer shown only as a small black case with a blinking red light, no digits"),
    # ---------------- MASTERMIND
    dict(to=76, v1="beat_023", reason="character enters: Dr. Vance appears in the container doorway with four men", chars=["vance", "ashham", "faahid"], loc="red_container",
         visual=f"Dr. Vance, an elderly European man with silver slicked-back hair in a long black overcoat, standing in the container doorway against the yellow deck lights with a cold arrogant face; behind him four dark-clad men in black combat gear with empty hands; in the foreground {ASHJ}, and {FAAJ}, seen from behind, tense, facing him",
         camera=f"medium wide shot over Ashham's and Faahid's shoulders, eye level, {LOW} (steel floor)", amb="storm_night",
         sens="violence", safe="the mercenaries' guns aimed at Ashham and Faahid are never shown: a tense standoff with empty hands"),
    dict(to=81, v1="beat_024", reason="framing change: Vance's boast and the remote", chars=["vance"], loc="red_container",
         visual="close-up of Dr. Vance, an elderly European with silver slicked-back hair and a black overcoat, a cold contemptuous smile, holding up a small plain black remote device with no screen and no markings; blue vial glow on one side of his face, deck lights behind",
         camera=f"close-up, slightly low angle, {LOW}", amb="storm_night"),
    dict(to=83, reuse="beat_033", reason="return to the container: the charge's red light counts down in silence", loc="red_container",
         visual="reuse of beat_033", amb="storm_night"),
    dict(to=88, reuse="beat_036", reason="back to Vance's arrogant laugh", loc="red_container", visual="reuse of beat_036", amb="storm_night"),
    dict(to=92, v1="beat_027", reason="framing change: Ashham locks eyes with Vance and signals Habeeb", chars=["ashham"], loc="red_container",
         visual=f"close-up of {ASHJ}, unflinching, eyes locked straight ahead, one finger touching a small earpiece in his ear, the cold blue glow of the vials on his face, rain on his jacket",
         camera=f"close-up, eye level, {LOW}", amb="storm_night", hum=True),
    dict(to=94, v1="beat_028", reason="action change: Habeeb swings the ship's crane into Vance's men", loc="ship_deck",
         visual="the ship's huge crane arm swinging through the yellow deck lights, its thick steel cable and hook slamming into the side of the red container in a burst of sparks, four bearded men in black combat jackets, trousers and helmets ducking and looking up in alarm with empty hands; only men on the deck, no women anywhere",
         camera="wide low-angle shot, the crane in the upper two-thirds, the dark wet deck as the lower third", amb="storm_night"),
    dict(to=98, v1="beat_029", reason="action change: the shootout's aftermath — Faahid hit in the shoulder, Ashham covering him", chars=["faahid", "ashham"], loc="ship_deck",
         visual=f"{FAAJ}, sitting back against a container wall holding his left shoulder with his other hand, grimacing in pain; {ASHJ}, crouched protectively beside him, turning to look across the deck; drifting smoke and a few sparks on the container wall, no one else visible",
         camera=f"medium shot, eye level, {LOW} (wet steel deck)", amb="storm_night",
         sens="violence", safe="the shootout and the men falling are never shown; Faahid's wound only as him holding his shoulder and grimacing, no blood"),
    dict(to=100, v1="beat_030", reason="character change: Vance flees towards the bridge pressing his useless remote", chars=["vance"], loc="ship_deck",
         visual="Dr. Vance in his long black overcoat hurrying across the dark deck towards the lit bridge superstructure, his silver hair whipped by the wind, frantically pressing the buttons of a small black remote device, panic on his face",
         camera=f"medium wide shot, eye level, {LOW} (wet steel deck)", amb="storm_night"),
    dict(to=101, reuse="beat_041", reason="back to Ashham kneeling beside the wounded Faahid", loc="ship_deck",
         visual="reuse of beat_041", amb="storm_night", hum=True),
    dict(to=102, speaker="faahid", reason="5.4 dialogue: the wounded Faahid begs Ashham to leave him (in the v1 image his face is at the right edge, x≈75 %)", chars=["faahid"], loc="ship_deck",
         visual=f"{FAAJ}, sitting back against a container wall on the wet deck, holding his left shoulder with his other hand, grimacing, looking up and speaking weakly, his face centred in the upper half and in sharp focus; at the left edge a man in a black tactical jacket crouching close beside him, seen from behind, soft and out of focus; drifting smoke and dim yellow deck lights",
         camera=f"{OTS} (Ashham's shoulder), slightly high angle, {LOW} (wet steel deck)", amb="storm_night", hum=True, transition="cut",
         sens="violence", safe="Faahid's wound only as him holding his shoulder and grimacing, no blood"),
    dict(to=103, v1="beat_031", reason="action change: Ashham lifts the wounded Faahid onto his shoulders", chars=["ashham", "faahid"], loc="ship_deck",
         visual=f"{ASHJ}, rising to his feet carrying Faahid across his shoulders, his face set with determination; {FAAJ}, slumped over his shoulders, grimacing, eyes half closed; containers and smoke around them, deck lights",
         camera=f"medium shot, slightly low angle, {LOW} (wet steel deck)", amb="storm_night", hum=True),
    dict(to=104, speaker="vance", reason="character change + 5.4: Vance shouts from the upper-deck railing (the v1 image showed only a tiny silhouette)", chars=["vance"], loc="cargo_ship",
         visual="Dr. Vance, an elderly European with silver slicked-back hair, his long black overcoat flapping in the wind, standing at the steel railing of the cargo ship's upper deck, both gloved hands gripping the railing, leaning over and shouting down with a furious face, his face centred in the upper half and in sharp focus, lit from below by the yellow deck lights, rain streaking past, the black night sky and the ship's crane behind him; Vance is the only person in the image — no other people, no women anywhere",
         camera="medium shot from below, low angle, Vance's face centred in the upper half, the dark steel hull and railing as the calm lower third", amb="storm_night",
         sens="violence", safe="Vance's gun is never shown: both his hands grip the railing"),
    dict(to=105, v1="beat_033", reason="action change: Habeeb's flare streaks up; a splash in the black sea", loc="cargo_ship",
         visual="a brilliant red flare streaking upward through the night from the small launch far below towards the ship's upper deck, bathing the dark hull in red light; at the foot of the towering hull a white splash bursting in the black waves",
         camera="wide shot from sea level, the red streak in the upper half, the splash and black water in the lower third", amb="storm_night",
         sens="violence", safe="the flare hitting Vance and his fall are never shown: only the flare's red streak and a splash in the waves"),
    dict(to=107, speaker="habeeb", reason="character change + 5.4: Habeeb shouts from the launch below (no v1 image shows him here)", chars=["habeeb"], loc="coastguard_launch",
         visual=f"{HABN}, soaked, standing on the deck of the rocking dark-grey launch in the rain, facing the camera three-quarter, his face centred in the upper half and in sharp focus, shouting upward with one cupped hand at his mouth, frantic; behind him the towering dark hull of the cargo ship glowing faintly red from a dying flare high above; white spray flying; Habeeb is the only person on the launch deck — no other people, no women anywhere",
         camera=f"medium close-up, slightly low angle, Habeeb's face centred in the upper half, {LOW} (dark wet deck)", amb="storm_night", hum=True),
    dict(to=108, v1="beat_034", reason="action change: Ashham leaps from the deck into the sea carrying Faahid", loc="cargo_ship",
         visual="from a distance: two dark silhouettes of men, one holding the other tight, leaping off the high railing of the giant ship into the black sea, the ship's deck lights above them and the red glow of the dying flare, white spray below",
         camera="wide shot from the side, the leaping figures in the upper half, the black sea as the lower third", amb="storm_night", hum=True),
    # ---------------- EXPLOSION ON THE SEA
    dict(to=110, v1="beat_035", reason="action change: the MV Orion explodes and splits apart", loc="cargo_ship",
         visual="seen from far away across the black sea: a gigantic orange fireball erupting from the middle of the huge cargo ship as it splits in two, flames rising hundreds of feet into the night, steel fragments raining down into the sea, the whole sea lit orange; no one near the flames",
         camera="wide establishing shot, the fireball in the upper two-thirds, the orange-lit water as the lower third", amb="sea_search",
         sens="violence", safe="explosion as distant spectacle only, no people in it"),
    dict(to=112, v1="beat_036", reason="action change: Habeeb pulls Ashham and Faahid out of the sea; tears of joy", chars=["habeeb", "ashham", "faahid"], loc="coastguard_launch",
         visual=f"{HAB}, leaning over the side of the launch and gripping Ashham's hand to pull him up out of the dark water; {ASHJ}, soaked, reaching up from the waves; {FAAJ}, already sitting on the launch deck soaked and exhausted, holding his shoulder; far behind them the burning wreck of the ship sinking in an orange glow; everyone dusty and exhausted but unhurt",
         camera=f"medium shot from the launch's deck, eye level, {LOW} (dark wet deck)", amb="sea_search", hum=True),
    dict(to=114, speaker="habeeb", reason="emotional turning point + 5.4: Habeeb's 'we did it', tears of joy (in the v1 image his face is at x≈25 %)", chars=["habeeb", "ashham", "faahid"], loc="coastguard_launch",
         visual=f"{HABN}, soaked and exhausted, kneeling on the wet deck of the launch, facing the camera, his face centred in the upper half and in sharp focus, tears of joy on his cheeks, a breathless relieved smile as he speaks; at the left and right edges, smaller, soft and out of focus, Ashham in a soaked black tactical jacket and Faahid (grey hair, white moustache) soaked, sitting on the deck holding his shoulder; far behind, the burning wreck of the giant ship sinking in an orange glow on the black sea",
         camera=f"medium shot, eye level, Habeeb's face centred in the upper half, {LOW} (dark wet deck)", amb="sea_search", hum=True),
    # ---------------- EPILOGUE
    dict(to=118, v1="beat_037", reason="time jump: three weeks later, a crowd outside police headquarters on a clear morning", loc="police_hq",
         visual="a big peaceful crowd of Maldivian citizens gathered on the sunny forecourt in front of the modern white police headquarters building, men in shirts and trousers and women in long loose dresses and hijabs, seen from behind and the side, golden morning light, a clear blue sky",
         camera="wide establishing shot, slightly high, the building and sky in the upper two-thirds, the paved forecourt as the lower third", amb="city_day", transition="black",
         sens="other", safe="the villains' life imprisonment is only narrated; no prison imagery needed"),
    dict(to=121, speaker="faahid", reason="scene change + 5.4 + fix: the new Commissioner speaks while pinning the medals (v1 put Faahid in his olive shirt at the far left edge, x≈21 %)", chars=["faahid", "ashham", "habeeb"], loc="commissioner_office",
         visual="Faahid, now the new Commissioner, wearing a formal DARK-NAVY police dress uniform tunic buttoned to the collar with plain epaulettes, a dark-navy tie and no badges or lettering — the same dark-navy uniform as Ashham (his reference image is used for the FACE ONLY: he wears NO olive or green shirt, no green clothing anywhere), his grey hair and white moustache neat, his shoulder healed, facing the camera three-quarter, his face centred in the upper half and in sharp focus, speaking with a proud, warm face as he pins a gold medal on the chest of Ashham, who stands at attention at the left edge in a formal dark-navy police dress uniform, seen in profile, soft and out of focus; Habeeb in the same formal dark-navy dress uniform with glasses and a gold medal stands soft in the background, smiling",
         camera=f"medium shot over Ashham's shoulder, eye level, Faahid's face centred in the upper half, {LOW} (polished desk top and floor)", amb="office_day", hum=True),
    dict(to=122, speaker="ashham", reason="5.4 dialogue: Ashham salutes and says thank you (reverse shot)", chars=["ashham"], loc="commissioner_office",
         visual="Ashham in a formal dark-navy police dress uniform with plain epaulettes and a gold medal on his chest, standing at attention and saluting, facing the camera, his face centred in the upper half and in sharp focus, a quiet proud smile as he speaks; at the right edge, soft and out of focus, the grey-haired new Commissioner in a dark-navy dress uniform seen from behind; bright office, plain flags without emblems, tall sunny windows",
         camera=f"medium close-up over the Commissioner's shoulder, eye level, Ashham's face centred in the upper half, {LOW} (polished desk top)", amb="office_day", transition="cut"),
    dict(to=123, v1="beat_039", reason="time and scene change: evening on Hulhumalé beach; Raniya comes to say goodbye", chars=["raniya", "ashham"], loc="hulhumale_beach",
         visual="Raniya in a soft cream long-sleeved ankle-length loose dress and a navy hijab fully covering her hair and neck, facing Ashham on the sand at a clear arm's-length distance, one hand pressed to her own heart, smiling gratefully; Ashham in his formal dark-navy police dress uniform with a gold medal, no cap, smiling gently; they do not touch",
         camera=f"medium two-shot from the side, eye level, {LOW} (sand and gentle surf)", amb="beach_evening", transition="black",
         sens="intimacy", safe="'she took his hand' is never shown: they face each other at arm's length, her hand on her own heart, no touching"),
    dict(to=124, speaker="raniya", reason="5.4 dialogue: Raniya speaks (in the v1 two-shot she is in profile at the left) — shot", chars=["raniya"], loc="hulhumale_beach",
         visual="Raniya in a soft cream long-sleeved ankle-length loose dress and a navy-blue hijab wrapped snugly and fully covering her hair and neck (her reference image used for the face only — she wears NO white doctor's coat), standing on the sand facing the camera, her face centred in the upper half and in sharp focus, one hand pressed to her own heart, speaking softly with a grateful smile, warm golden light on her face; at the right edge, at a clear distance, soft and out of focus, the dark-navy uniformed shoulder and the back of a man's head; coconut palms, calm waves and the low sun behind her",
         camera=f"medium close-up over Ashham's shoulder at arm's length, eye level, Raniya's face centred in the upper half, {LOW} (soft sand)", amb="beach_evening", transition="cut",
         sens="intimacy", safe="'she took his hand' is never shown: her hand on her own heart, a clear distance between them, no touching"),
    dict(to=125, v1="beat_040", reason="framing change: Ashham's unspoken feelings (reverse shot: Ashham answers)", chars=["ashham", "raniya"], loc="hulhumale_beach",
         visual="close-up of Ashham in his dark-navy dress uniform, looking at Raniya with quiet longing and words he cannot say, golden light on his face; Raniya soft and out of focus at arm's length in the foreground edge, her navy hijab fully covering her hair and neck",
         camera=f"close-up, eye level, {LOW}", amb="beach_evening", hum=True, transition="cut"),
    dict(to=126, reuse="beat_057", reason="back to Raniya thanking him (shot / reverse shot)", loc="hulhumale_beach",
         visual="reuse of beat_057", amb="beach_evening", transition="cut",
         sens="intimacy", safe="'she took his hand' is never shown: her hand on her own heart, no touching"),
    dict(to=128, reuse="beat_058", reason="back to Ashham looking into her eyes, unable to speak", loc="hulhumale_beach",
         visual="reuse of beat_058", amb="beach_evening", hum=True, transition="cut"),
    dict(to=129, reason="action change + fix: Raniya walks away to her father (the v1 image wrongly showed her in a white doctor's coat)", chars=["raniya", "raniya_father", "ashham"], loc="hulhumale_beach",
         visual="Raniya in a soft cream long-sleeved ankle-length loose dress and a navy-blue hijab fully covering her hair and neck (her reference image used for the face only — she wears NO white doctor's coat and no blue skirt, only the plain cream dress), walking away along the sand towards her father, a healthy older man with white stubble in a white long-sleeved shirt and a dark sarong sitting on a wooden bench under the palms in the distance; Ashham in his dark-navy dress uniform in the foreground seen from behind and to the side, standing still, watching her go",
         camera=f"medium wide shot over Ashham's shoulder, eye level, {LOW} (sand)", amb="beach_evening"),
    dict(to=131, v1="beat_042", reason="final image: Ashham alone on the beach looks up at the sky — THE END", loc="hulhumale_beach",
         visual="a tall man in a dark-navy dress uniform standing alone on the wide empty beach seen from behind, looking up at the glowing golden sky, gentle waves at his feet; two tiny figures far away at the end of the beach disappearing in the haze",
         camera="wide shot from behind, the figure and sky in the upper two-thirds, wet sand and surf as the calm lower third", amb="beach_evening", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)
T = dict(crop="tight")
def spk(who, x=None, y=35, crop="tight"):
    """dialogue shot (spec 5.4): speaker + crop centred on the speaker's face (focus in % of the image)."""
    d = dict(speaker=who, crop=crop)
    if crop == "medium": y = min(max(y, 42), 58)
    if x is not None: d["focus"] = [x, y]
    return d

# ---- warehouse
sh(1, "As the soldiers burst into the warehouse, Fairooz picked up the dangerous Project Phenix syringe lying on the floor and drove it into his own neck.",
   [("boots_march", "ވަދެގަތް", -18)])
sh(2, "He wanted to wipe out his brain completely, along with all its secrets. Fairooz! No!", hum=True, **spk("ashham", 41))
sh(3, "Ashham lunged forward, shouting. But it was too late.", [("breath_heavy", "ފުންމާލި", -20)], hum=True)
sh(4, "As the poison in the syringe emptied into Fairooz's body, his eyes went wide and his whole body began to shake.", hum=True)
sh(5, "White foam came from his mouth, and within a few seconds he went still. He fell to the floor like a lifeless body.",
   [("soft_thud", "ވެއްޓުނީ", -23)], hum=True)
sh(6, "Minister Saleem, who had given him his orders, sank to his knees weeping in fear. The soldiers at once cuffed Saleem's hands and led him out of the warehouse.",
   [("sob_breath", "ރޮއެގަންނަމުން", -22), ("boots_march", "ގެންދިޔަ", -22)])
sh(7, "Ashham, Fairooz has gone and taken many of the main secrets with him, Faahid said, putting his hand on Ashham's shoulder.", **spk("faahid", 46))
sh(8, "But what matters most to us now is Habeeb. Naasir has taken him to Dhoonidhoo jail. Get a launch ready to go to Dhoonidhoo.", **spk("faahid", 46, crop="medium"))
# ---- Dhoonidhoo cell
sh(9, "Ashham said, wiping the blood from his lip. In an isolated cell of Dhoonidhoo jail, Habeeb lay tied to an iron bed.",
   [("metal_door", "ގޮޅިއެއްގެ", -22)])
sh(10, "His face was badly swollen. In front of him sat Naasir, holding a laptop. Habeeb,", **spk("naasir", 53, crop="medium"))
sh(11, "Where is the master password of the secret accounts you hacked? Naasir asked loudly.", **spk("naasir", 53))
sh(12, "All of Minister Saleem's money abroad is frozen now. Since that video leaked, the banks have been holding on to that money.", **spk("naasir", 53, crop="medium"))
sh(13, "We need your help to move that money to a new account of the Minister's. That's the only way you'll be saved. I...",
   [("keyboard_typing", "އެކައުންޓަކަށް", -24)], **spk("naasir", 53))
sh(14, "I won't tell, Habeeb said with difficulty. That money is... the blood and lives of so many people.", hum=True, **spk("habeeb", 38))
sh(15, "Naasir glanced at his watch. I'll give you ten minutes. After that", hum=True, **spk("naasir", 53, crop="medium"))
sh(16, "I'll start cutting off your fingers. Habeeb closed his eyes. His heart was pounding hard.",
   [("heartbeat", "ތެޅެމުން", -20)], hum=True, **spk("naasir", 53))
sh(17, "When they arrested him, they hadn't noticed the smartwatch on his wrist. That watch was something he had modified himself, a thing that could send signals in secret.")
sh(18, "Slowly he pressed one of the watch's buttons. With that, his location and the sound of what was said inside the cell began to stream to a secret server.",
   [("computer_beep", "އޮބާލި", -22)])
# ---- race on the sea
sh(19, "Race on the sea. Ashham and Faahid were aboard a military launch that had left Malé's lagoon. The launch was heading for Dhoonidhoo.",
   [("boat_engine", "ލޯންޗުގައި", -16)])
sh(20, "Suddenly a signal came onto Faahid's tablet in Ashham's hands. Sir! This is the signal from Habeeb's watch! Ashham shouted.",
   [("computer_beep", "ސިގްނަލެއް", -20)], **spk("ashham", 38))
sh(21, "I can hear him! Naasir's voice began to come from the tablet. In ten minutes you will die...", **spk("ashham", 38))
sh(22, "We have only eight minutes left. Faahid looked at the launch's captain. Full throttle!",
   [("engine_rev", "އިންޖީނު", -16)], **spk("faahid", 69))
sh(23, "The launch entered Dhoonidhoo's lagoon and came alongside the jetty. The jail's security guards were startled to see the soldiers.",
   [("boat_engine", "ކައިރިކޮށްލި", -20)])
sh(24, "Faahid used his official command and brought them under control. With an official warning the soldiers went ashore and got to work.",
   [("boots_march", "ރަށަށްއަރައި", -18)])
sh(25, "Naasir sir is trying to flee right now after committing a serious crime! Everyone, show us the way! Without waiting for anyone, Ashham broke into a run.",
   [("footsteps_pavement", "ދުއްވައިގަތް", -18)], **spk("ashham", 34))
# ---- time up
sh(26, "Time up. Naasir pressed the sharp knife in his hand against Habeeb's throat. Habeeb,",
   [("heartbeat", "ޖައްސާލި", -22)], hum=True, **spk("naasir", 55, crop="medium"))
sh(27, "Time's up. Will you tell me the password? Habeeb looked straight into Naasir's eyes.", hum=True, **spk("naasir", 55))
sh(28, "My death will bring these secrets to life. Naasir kicked Habeeb in the face. At that moment came the sound of the cell door opening.",
   [("soft_thud", "ޖެހި", -24), ("metal_door", "ހުޅުވާލި", -16)], hum=True, **spk("habeeb", 38))
sh(29, "It was Ashham. Naasir! Hands up! Ashham shouted.", **spk("ashham", 46))
sh(30, "Startled, Naasir swung the knife towards Ashham. But Ashham was far quicker.")
sh(31, "Spinning round suddenly, his leg struck Naasir's shoulder. He went down at once. Then the soldiers came in and arrested Naasir on the spot.",
   [("soft_thud", "ޖެހުނީ", -23), ("boots_march", "ވަދެ", -20)])
sh(32, "Ashham ran over to Habeeb. Habeeb! Are you all right? Habeeb gave a faint smile.",
   [("footsteps_pavement", "ދުވެފައި", -22)], **spk("ashham", 51))
sh(33, "Sir... I didn't change the master password. But I've done something new.", **spk("habeeb", 47))
sh(34, "What? Ashham asked, helping Habeeb to his feet. The big leak.", **spk("ashham", 51))
# ---- big leak
sh(35, "Habeeb tapped the watch on his wrist. Through this watch, all of Minister Saleem's and", **spk("habeeb", 31))
sh(36, "Moosa Thaahir's black-money transactions, and the secret documents sent to foreign companies,", **spk("habeeb", 31))
sh(37, "I have leaked to the world's media and to Interpol. I pressed that button when time was running out.", **spk("habeeb", 31))
sh(38, "At once international news began arriving on Faahid's tablet. The story of the huge medical mafia run jointly by the Maldives' Home Minister and tycoons made the headlines of the world's biggest TV channels.",
   [("computer_beep", "ޓެބްލެޓަށް", -20)])
sh(39, "What you've done is extraordinary, Faahid said. Minister Saleem's network is now completely destroyed.", **spk("faahid", 53))
sh(40, "But worry still showed on Habeeb's face. Sir, but", **spk("habeeb", 45, crop="medium"))
sh(41, "among those files I found something else. Minister Saleem isn't the one at the very top either.", **spk("habeeb", 45))
sh(42, "The big container loaded with Project Phenix's real drugs left Malé port about an hour ago, on its way to be loaded onto a secret foreign ship.",
   hum=True, **spk("habeeb", 45, crop="medium"))
sh(43, "If those drugs spread around the world, many millions of people will be in danger. Ashham was ready. Where is that ship?", **spk("habeeb", 45))
sh(44, "It's out in the open sea off the east side of Malé, Habeeb said. Confrontation at sea.", **spk("habeeb", 45, crop="medium"))
# ---- coast-guard launch
sh(45, "Though Habeeb's big leak had turned the whole world's attention to the Maldives, there was only a narrow chance to stop the shipment of Project Phenix's dangerous master drug.")
sh(46, "Leaving Dhoonidhoo jail, Ashham, Habeeb and Faahid boarded the military coast-guard launch. The waves were big.",
   [("boat_engine", "ލޯންޗަށް", -18), ("wave_crash", "ރާޅުތައް", -20)])
sh(47, "Black clouds covered the sky, and the wind rocked the launch from side to side. Sir, the radar shows a big cargo ship travelling in the open sea, the MV Orion.",
   [("wind_gust", "ވައިރޯޅި", -20)], **spk("habeeb", 43, crop="medium"))
sh(48, "Zayaan said, looking at the screens in the launch's cockpit. That ship is registered in the name of a secret foreign company. The container with the drugs has already been loaded onto it.",
   [("computer_beep", "ސްކްރީންތަކަށް", -22)], **spk("habeeb", 43))
sh(49, "They're heading out of Maldivian territorial waters. How long will it take us to reach that ship? Ashham asked, zipping his jacket up tight.",
   [("cloth_rustle", "މަހާލަމުން", -20)], **spk("ashham", 37))
sh(50, "At this speed, an hour and forty-five minutes, Faahid answered.", **spk("faahid", 67, 39))
sh(51, "But be careful. That ship is no ordinary cargo ship. There'll be armed foreign mercenaries aboard.", **spk("faahid", 67, 39))
sh(52, "With the powerful roar of the launch's three engines, it surged forward. This was the last chance they would get to stop this dangerous crime from spreading around the world.",
   [("engine_rev", "އިންޖީނުގެ", -14)], hum=True)
# ---- the ship
sh(53, "The shadow of the big ship. Out of the pitch darkness of the sea, the huge silhouette of the MV Orion began to appear.", hum=True)
sh(54, "It was a big steel ship. In the dim lights on the ship's deck, the giant containers could be seen stacked up.")
sh(55, "As the military launch began to close in on the ship, the beam of a powerful searchlight from the ship fell straight on the launch.")
sh(56, "And then, without any warning, automatic fire poured down from the ship's deck. Bullets struck all over the launch, sparks flying.",
   [("metal_clang", "ހަމަލާތައް", -18), ("metal_clang", "ވަޒަންތައް", -18)])
sh(57, "Get down! Get down! Faahid shouted, swinging the launch's wheel. Ashham came out to the stern, aimed the powerful rifle in his hand at the searchlight on the ship and fired.",
   [("soft_thud", "ޖެހި", -24)], **spk("faahid", 67, 39))
sh(58, "With a single bullet the searchlight burst, and that side of the ship went dark. Seizing the chance, Faahid brought the launch alongside the steel ladder fixed to the ship's stern.",
   [("glass_break", "ގޮވައި", -14), ("boat_engine", "ކައިރިކޮށްލި", -20)])
sh(59, "Habeeb, you stay in the launch. Work on blocking the ship's systems, Ashham said. We're going up.", **spk("ashham", 41))
sh(60, "Ashham and Faahid carefully began to climb the ship's steel ladder. Because of the huge waves the ship was rolling hard from side to side.",
   [("metal_clang", "ސިޑިން", -22), ("wave_crash", "ރާޅުތަކުގެ", -18)])
# ---- deck fight
sh(61, "The deck fight. As Ashham climbed onto the ship's main deck, two armed men came out from behind the containers.",
   [("boots_march", "ނުކުތް", -20)])
sh(62, "They were in black combat gear. Rolling across the deck, Ashham fired; the bullets struck them squarely in the chest, and they fell to the deck.",
   [("soft_thud", "ވެއްޓުނު", -24)])
sh(63, "Faahid climbed up too and covered Ashham's back. They moved along the narrow lanes between the containers to find the container holding the Project Phenix drugs.",
   [("footsteps_pavement", "ކުރިއަށް", -24)])
sh(64, "Thanks to information Habeeb had given them earlier, they knew it was a red container marked with a secret number. Ashham, on the right!", **spk("faahid", 57))
sh(65, "Faahid shouted. From the top of a container above, someone threw a grenade towards them.",
   [("metal_clang", "އެއްލި", -22)], **spk("faahid", 57))
sh(66, "As Ashham and Faahid dived to either side, there was a powerful explosion. The force of the blast tore parts of the steel containers apart, and smoke and fire spread.",
   [("distant_boom", "ގޮވުމެއް", -12), ("fire_crackle", "އަލިފާން", -20)])
sh(67, "Summoning his courage, Ashham rose to his feet and sent a bullet into the forehead of the man on top. The red container.",
   [("soft_thud", "ފޮނުވާލި", -24)])
sh(68, "Walking on through the smoke, around the middle of the ship they saw the red container. A big electronic lock was fitted on its door.")
sh(69, "Habeeb, we've reached the container. Bypass the system to open its lock, Ashham said over the walkie-talkie.", **spk("ashham", 46))
sh(70, "In the launch, Habeeb's hands flew over the keyboard. Sir, I'm into the ship's main server now. The lock opens... now!",
   [("keyboard_typing", "ކީބޯޑުގައި", -16), ("computer_beep", "ހުޅުވޭނީ", -20)], **spk("habeeb", 40))
sh(71, "The container's big steel door opened. As Ashham pulled the door open, inside were special refrigerated racks.",
   [("metal_door", "ހުޅުވުނު", -16), ("steam_hiss", "ފިނިކުރި", -22)])
sh(72, "And on those racks stood bottles of Project Phenix's blue liquid drug. There were many thousands of vials.")
sh(73, "All of this has to be destroyed, Faahid said. He took powerful explosives from his bag and began fixing them in the middle of the container.",
   [("cloth_rustle", "ދަބަހުން", -22)], **spk("faahid", 41, crop="medium"))
sh(74, "I'm setting the timer to five minutes. We have to get off this place fast. The mastermind's confrontation.", **spk("faahid", 41))
# ---- mastermind
sh(75, "Just as Faahid started the timer, a man's shadow fell across the container's doorway. Ashham raised his gun towards it, but stopped because of who he saw.",
   [("computer_beep", "ޖައްސާލި", -20)], hum=True)
sh(76, "It was an elderly foreigner in a black coat. With him were four armed men.")
sh(77, "Their guns were aimed straight at Faahid's and Ashham's chests. Who do you think you are!", **spk("vance", 40))
sh(78, "Did you come here to wage war on a Maldivian minister? the man said in English. I am", **spk("vance", 40))
sh(79, "the owner of this project. Doctor Vance. Your country's ministers are just little boys working for my money.", **spk("vance", 40))
sh(80, "Vance showed them a small device in his hand. The bomb you planted can be deactivated with this remote of mine.", **spk("vance", 40))
sh(81, "And you two will go to the bottom of this sea tonight. The timer of the bomb in the container stood at four minutes.",
   [("computer_beep", "ޓައިމަރު", -22)], hum=True, **spk("vance", 40))
sh(82, "As time ran down, on the ship the last, most dangerous confrontation was under way. The bullets in Ashham's gun were running low.")
sh(83, "The last seconds. As the bomb timer fixed inside the red container showed three minutes forty-five seconds, a silence reigned over the whole place.",
   [("heartbeat", "ހިމޭންކަމެއް", -20)], hum=True)
sh(84, "Extreme arrogance showed on Doctor Vance's face. The guns of the four armed men behind him were aimed straight at Ashham's and Faahid's chests.", **T, focus=[40, 40])
sh(85, "Ashham, did you think you were a hero? Vance burst out laughing.", **spk("vance", 40))
sh(86, "People of little island nations like yours, in front of great scientists and tycoons like us,", **spk("vance", 40))
sh(87, "are nothing but little test mice. These drugs will go out to the world tonight.", **spk("vance", 40))
sh(88, "And you two will turn to ash right here. Without lowering his gun, Ashham looked straight into Vance's eyes.", **spk("vance", 40))
sh(89, "His mind was calculating faster with every second. He had only three bullets left.", hum=True)
sh(90, "Faahid's gun didn't have many bullets either. Vance, do you think you can control everything with your remote?", **spk("ashham", 35))
sh(91, "Ashham said slowly. Your ship's main system is now under our control.", **spk("ashham", 35))
sh(92, "Through the earpiece in his ear, Ashham sent a secret code to Habeeb. Habeeb... now!",
   [("computer_beep", "އިއަރޕީސްއިން", -22)], hum=True, **spk("ashham", 35))
sh(93, "At that moment the big crane on the ship suddenly began to swing. Habeeb, in the launch, had hacked the ship's hydraulic system and swung the crane straight at where Vance and his men stood.",
   [("creak", "ކްރޭން", -18), ("steam_hiss", "ހައިޑްރޯލިކް", -20)])
sh(94, "The huge steel cable slammed into the side of the container. At the loud crash Vance's men looked up, startled, and in that moment Ashham and Faahid dived down together and opened fire.",
   [("metal_clang", "ޖެހުނު", -14), ("soft_thud", "ބަޑިޖަހަން", -23)])
sh(95, "Sea of blood. With Ashham's perfect aim the bullets struck the chests of the two armed men in front, and they dropped to the deck at once.")
sh(96, "Faahid brought down one of the other two. But the last man left fired at Faahid.",
   [("soft_thud", "ބަޑިޖަހާލި", -23)])
sh(97, "The bullet struck Faahid's shoulder. Faahid cried out and stumbled backwards. Faahid sir!",
   [("gasp", "ހަޅޭއްލަވައިގަންނަމުން", -20)], hum=True, **spk("ashham", 31))
sh(98, "Ashham shouted, threw away his empty gun, picked up the gun of the man lying on the deck and sent a bullet into the last man's head.",
   [("soft_thud", "ފޮނުވާލި", -24)])
sh(99, "Doctor Vance backed away in fear, came out of the container and ran towards the ship's cockpit. He kept pressing the buttons of the remote in his hand to deactivate the bomb.",
   [("footsteps_pavement", "ދުއްވައިގަތް", -20)])
sh(100, "But because Habeeb had locked the bomb's system too, the remote didn't work. The timer was showing one minute thirty seconds.",
    [("computer_beep", "ޓައިމަރުން", -20)])
sh(101, "Only a minute and thirty seconds were left. Ashham ran over and knelt beside Faahid. Blood was pouring from Faahid's shoulder.", hum=True,
    crop="medium", focus=[40, 42])
sh(102, "Ashham... leave me and go... the ship's going to blow... No, I won't leave you behind, sir.", hum=True, **spk("faahid", 45))
sh(103, "Ashham lifted Faahid onto his shoulder. As he broke into a run, Doctor Vance came out onto the ship's upper deck holding a gun and aimed at Ashham's legs.",
    [("breath_heavy", "އުފުލާލައި", -20), ("footsteps_pavement", "ދުއްވައިގަތް", -20)], hum=True)
sh(104, "None of you will survive! Vance shouted. But at that moment, from below the ship, Habeeb, standing on the military launch, fired the launch's powerful flare gun up at the ship.",
    [("steam_hiss", "ފްލެއާ", -16)], **spk("vance", 46))
sh(105, "The blazing flare struck Vance full in the face. Crying out, he toppled backwards over the ship's steel railing and fell into the huge waves of the sea.",
    [("splash", "ވެއްޓުނު", -16)])
sh(106, "He sank completely into the darkness of the sea. The explosion on the sea. Thirty seconds on the timer!",
    [("alarm_beep", "ޓައިމަރުގައި", -20)], hum=True, **spk("habeeb", 43, crop="medium"))
sh(107, "Ashham sir, jump! Habeeb shouted from below. Holding Faahid tight against his chest, Ashham leapt from the ship's upper deck straight into the sea.",
    [("wind_gust", "ފުންމާލި", -18)], hum=True, **spk("habeeb", 43))
sh(108, "The second they plunged into the waves was the second the bomb's timer reached zero. Boom!",
    [("splash", "ގަނބައިގަތް", -14), ("distant_boom", "ބޫމް", -12)])
sh(109, "With an extraordinarily powerful explosion, the MV Orion split apart in the middle. All of Project Phenix's chemicals and drugs became a huge ball of fire, and the flames rose many feet into the air.",
    [("distant_boom", "ގޮވުމަކާއެކު", -14), ("fire_crackle", "އަލިފާނުގެ", -18)])
sh(110, "The ship's big steel pieces rained down into the sea. The powerful wave of the explosion lifted the sea and pushed Ashham and Faahid far away.",
    [("splash", "ބުރައިގެން", -22), ("wave_crash", "ރާޅާއެކު", -16)])
sh(111, "Carefully, Habeeb drove the launch forward, pulled Ashham and Faahid out of the sea and got them into the launch.",
    [("boat_engine", "ދުއްވާލައި", -20)])
sh(112, "Slowly the big ship sank to the bottom of the sea. The deadly plague of Project Phenix was buried in the deepest part of the sea before it could spread around the world.", hum=True)
sh(113, "We... we've done it. Habeeb said, taking a deep breath.", [("sigh", "މާނޭވައެއް", -20)], hum=True, **spk("habeeb", 47))
sh(114, "Tears of joy ran from his eyes. A new day. Three weeks later.", hum=True)
# ---- epilogue
sh(115, "The sky over Malé was clear. As the golden rays of morning fell on the streets, a large crowd of citizens had gathered in front of the Shaheed Hussain Adam Building.")
sh(116, "With this great betrayal and murder at the very top of the state fully exposed, a big change had come over the country's political climate.")
sh(117, "Former Home Minister Saleem, tycoon Moosa Thaahir and the senior jail officer Naasir had been arrested and were in prison.")
sh(118, "Many charges had been brought against them. They would have to spend the rest of their lives in prison.")
sh(119, "Former Commissioner Faahid had been appointed the new Commissioner of the police. The wound to his shoulder had now healed.")
sh(120, "Ashham and Habeeb were in the new Commissioner's office, wearing the police's highest uniform of honour. Ashham,",
    [("footsteps_pavement", "އޮފީސް", -24)], **spk("faahid", 50, crop="medium"))
sh(121, "Habeeb. You two have saved the nation, Faahid said, pinning gold medals on their chests.",
    [("cloth_rustle", "ހަރުކޮށްދެމުން", -22)], hum=True, **spk("faahid", 50))
sh(122, "Naail's death has received justice. Thank you, sir, Ashham said, saluting.", **spk("ashham", 45))
sh(123, "In the evening, Ashham stood on the Hulhumalé beach. The waves were rolling gently onto the shore.")
sh(124, "Walking slowly towards him came Doctor Raniya. Ashham, Raniya said softly. Tomorrow we",
    [("footsteps_sand", "ހިނގާލާފައި", -22)], **spk("raniya", 45))
sh(125, "are going back to the island. A good decision, Ashham smiled. The island needs good doctors like you.", **spk("ashham", 30))
sh(126, "Without your help we would never have survived. Raniya took hold of Ashham's hand. Thank you.", **spk("raniya", 45, crop="medium"))
sh(127, "Raniya said softly. Ashham looked into Raniya's eyes. What he wanted to say was something else. Other feelings were welling up in his heart.", hum=True)
sh(128, "But he could not find the courage to reveal these feelings. On a bench some distance away sat Raniya's father. He was completely well now.")
sh(129, "After saying goodbye, Raniya walked off in that direction, as if waiting for Ashham to say something. But he just stood there. His words had stopped.",
    [("footsteps_sand", "ހިނގައިގަތް", -22)])
sh(130, "All he could manage was a smile. After Raniya left, Ashham stood alone on the beach for a long time.", hum=True)
sh(131, "Until Raniya, leaving with her father, disappeared from sight, he kept looking that way. When she vanished from view, he looked up at the sky. The End.", hum=True)

SHOTS = S

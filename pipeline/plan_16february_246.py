"""Beat/shot plan for 16 February episode 246 (used by plan_beats.py).
The night of 16 February, part 1. The fall/death is NEVER shown (no man falling, no body, no blood);
the stranger is only a faceless dark silhouette (never `ahlam` in chars); no touch between Malak and any man;
Zain and Kiyaara are only heard behind a closed door; Malak's injuries are never shown."""

FH = ("a single-storey coral-stone island house painted pale green, a sandy yard with a breadfruit tree, a wooden "
      "joali swing chair, a small veranda, tiled sitting room with a ceiling fan")
NIGHT_ROAD = "a long dark sandy island road lined with tall trees and scattered dim street lamps"
SITE = ("a cluster of three-storey half-built concrete guesthouses, bare columns and empty window holes, rusty rebar, "
        "overgrown with weeds, at the edge of the island near the trees")
JETTY = "the island's concrete jetty with ferries and a white resort staff launch, turquoise water"
APT = "a small modern apartment on the home island"

MALAK_NIGHT = ("Malak in her deep wine-maroon long kurta, loose black trousers and black hijab fully covering her hair "
               "and neck, a black leather shoulder handbag")
MALAK_WET = ("Malak in her deep wine-maroon long kurta and black hijab soaked dark with rain, the hijab still fully "
             "covering her hair and neck, a black leather shoulder handbag")
SILHOUETTE = ("a tall dark male silhouette with no visible face, a featureless black shape against the darkness")

LOC = {
    "sea": "the open sea just off a small Maldivian home island at dusk, a wooden passenger ferry dhoni with a small "
           "cabin chugging towards the island, a line of dense coconut palms and tall trees along the shore",
    "jetty": JETTY + "; a wooden passenger ferry dhoni moored alongside, a row of parked motorbikes at the end of the "
             "jetty, a lit white minaret far behind the palms",
    "corner": "a sandy island lane near the jetty, low coral-stone walls, a crossroads of narrow lanes, a few dim "
              "street lamps just lit, palms and breadfruit trees",
    "night_road": NIGHT_ROAD,
    "site": SITE,
    "site_hide": SITE + "; behind a low unfinished cinder-block wall beside a pile of cement bags and sand, weeds and "
                 "bushes, dark tree trunks",
    "apt_door": f"the dark sitting room of {APT} at night: a closed wooden front door, a grey sofa, a small low table, "
                "tiled floor, a rain-streaked window",
    "apt_hall": f"the dark short hallway of {APT} at night: a closed white bedroom door at the end with a thin strip of "
                "warm light under it, tiled floor, a light switch on the wall",
    "cake": f"a small low table in the dark sitting room of {APT} at night",
    "apt_outside": "the outside landing of a small apartment block on an island at night: a closed wooden front door, "
                   "a wet tiled floor, a low concrete railing, heavy rain pouring beyond it, palms in the dark",
    "storm_road": NIGHT_ROAD,
    "malak_room": "Malak's small bedroom in a single-storey coral-stone island house painted pale green: plain pale "
                  "walls, a single bed with a simple cotton sheet, a wooden window with thin curtains, a small cupboard",
    "yard": FH,
    "joali": FH,
    "veranda": FH,
    "yard_police": FH,
}
MOOD = {
    "sea": "dusk just after sunset, the last ember-orange glow on the horizon under heavy charcoal rain clouds rolling "
           "in, cool damp wind, choppy grey-blue sea, ominous",
    "jetty": "dusk at Maghrib, deep blue-grey sky with dark rain clouds and a last thin band of ember-orange on the "
             "horizon, the jetty lamps just switched on, damp breeze",
    "corner": "early evening just after dusk, dim amber street lamps, deep blue shadows, gathering rain clouds, "
              "irritation and unease",
    "night_road": "night, no rain yet but heavy dark clouds, cold damp wind bending the trees, only scattered pools of "
                  "dim amber lamplight on the sand, eerie and lonely",
    "site": "late night, very dark, distant faint lightning glow inside the clouds, cold damp wind, menacing silence",
    "site_hide": "late night, very dark, blue-and-red police lights flickering through the bushes and trees, the first "
                 "light drizzle glinting in the air, terror and suspense",
    "apt_door": "late rainy night, no lamps on, only cold blue-grey light from the rain-streaked window, exhaustion and fear",
    "apt_hall": "late rainy night, the dark hallway lit only by the thin warm strip of light under the bedroom door, dread",
    "cake": "late rainy night, darkness, faint cold blue light from the window on the table, quiet heartbreak",
    "apt_outside": "late night, heavy rain, a weak bare bulb over the door, cold blue shadows, heartbreak",
    "storm_road": "night thunderstorm, pouring rain, a lightning flash lighting the road white-blue for an instant, "
                  "tall trees thrashing in the wind, desperate",
    "malak_room": "bright tropical morning after the storm, a shaft of warm sunlight through the window, slightly "
                  "desaturated, quiet exhaustion",
    "yard": "bright tropical morning after the rain, warm sunlight, wet sand drying, slightly desaturated colours, "
            "ordinary domestic bustle",
    "joali": "bright tropical morning, dappled sunlight under the breadfruit tree, slightly desaturated colours, "
             "light domestic bickering",
    "veranda": "bright tropical morning, warm sunlight on the veranda, slightly desaturated, tension under the surface",
    "yard_police": "bright tropical morning, slightly desaturated, sudden cold tension",
}

BEATS = [
    dict(to=4, reason="episode opening: dusk, rain clouds gathering, the ferry approaching the island", loc="sea",
         visual="a small wooden passenger ferry dhoni with a cabin ploughing through choppy grey-blue water towards a "
                "dark island lined with dense palms and trees; heavy charcoal clouds swallowing the last white clouds "
                "and the orange afterglow; palm fronds bending in the wind; no readable markings on the boat",
         camera="wide shot, the boat and island in the upper two-thirds, dark water as the calm lower third",
         amb="sea_boat"),
    dict(to=6, reason="scene change: the ferry docks at the jetty at Maghrib and Malak steps off", chars=["malak"], loc="jetty",
         visual=f"{MALAK_NIGHT}, stepping off the moored ferry onto the concrete jetty holding a brown paper gift bag, "
                "walking towards a row of parked motorbikes; a few ferry passengers (men in shirts, women in hijabs) "
                "walking off in the background; a lit white minaret far behind the palms",
         camera="medium wide, eye level, Malak in the upper half, the jetty concrete as the lower third",
         amb="beach_dusk"),
    dict(to=8, reason="action change: her motorbike is gone; she sees it disappear round a corner and stops, frowning",
         chars=["malak"], loc="corner",
         visual=f"{MALAK_NIGHT}, standing at a crossroads of sandy lanes holding the paper gift bag, one hand adjusting "
                "the strap of the bag on her shoulder, eyebrows drawn together in an angry frown, staring down a lane "
                "where the small red tail light of a motorbike vanishes round a far corner",
         camera="medium shot from slightly behind and beside her, her face in profile in the upper third, the sandy lane as the lower third",
         amb="village_night"),
    dict(to=12, reason="scene change: the long walk on the dark main road towards Zain", chars=["malak"], loc="night_road",
         visual=f"{MALAK_NIGHT}, walking fast alone along the dark tree-lined sandy road carrying the paper gift bag, "
                "her face tense and determined, glancing at the swaying trees; long stretches of darkness between dim lamps",
         camera="wide shot, low angle, Malak small in the upper half, the long dark sandy road as the lower third",
         amb="night_lane"),
    dict(to=14, reason="action change: she checks the time on her phone at the Isha call, angry after an hour of walking",
         chars=["malak"], loc="night_road",
         visual=f"close view of {MALAK_NIGHT}, walking under a dim street lamp, the paper gift bag swapped to one hand, "
                "glancing down at the phone in her other hand, its cold glow on her annoyed tired face (screen faces "
                "away, nothing readable); far behind the dark trees a small lit minaret",
         camera="medium close-up, eye level, her face in the upper third, the dark road blurred below",
         amb="night_lane", sens="other", safe="phone shown only as glow, no readable time"),
    dict(to=16, reason="scene change: she reaches the abandoned half-built guesthouses and fear grips her", chars=["malak"], loc="site",
         visual=f"{MALAK_NIGHT}, standing small at the edge of the road, slowing to a stop and looking up at the "
                "dark skeletal three-storey concrete guesthouses with empty window holes; piles of cement bags, sand "
                "and rusty rebar heaped to one side; weeds everywhere",
         camera="wide shot, the dark buildings filling the upper two-thirds, Malak small at the left, the sandy ground as the lower third",
         amb="jungle_night"),
    dict(to=20, reason="emotional turning point: she remembers the recent incident there, then hears familiar voices",
         chars=["malak"], loc="site",
         visual=f"close view of {MALAK_NIGHT}, clutching the paper gift bag to her chest, eyes wide and uneasy, turning "
                "her head towards the dark interior of the half-built building as if listening to distant voices; bare "
                "concrete columns and an empty dark upper floor behind her",
         camera="medium close-up, slightly low angle, her face in the upper third",
         amb="jungle_night"),
    dict(to=22, reason="shocking turning point: something falls at her feet and she screams (the fall is NOT shown)",
         chars=["malak"], loc="site",
         visual=f"{MALAK_NIGHT}, recoiling in horror, both hands pressed over her own mouth, eyes wide, her face lit "
                "blue-white by a lightning flash; the brown paper gift bag dropped in a puddle at her feet; behind her "
                "only the dark empty upper floor of the unfinished concrete building; nothing else on the ground",
         camera="medium close-up, low angle, her face in the upper third, the dropped bag in the puddle at the bottom",
         amb="jungle_night", sens="violence",
         safe="the falling man, his body and blood are never shown: only Malak's horrified face lit by lightning, the "
              "dark empty upper floor and her dropped paper bag in a puddle"),
    dict(to=28, reason="character and action change: the stranger pulls her into hiding as police sirens approach",
         chars=["malak"], loc="site_hide",
         visual=f"{MALAK_NIGHT}, crouched hidden in the dark behind a low unfinished cinder-block wall, her own hand "
                f"pressed over her own mouth, eyes wide and wet with fear; an arm's length away {SILHOUETTE} crouches "
                "beside the wall with one finger raised to where his lips would be; blue and red police lights "
                "flickering through the bushes beyond; a clear gap between them, no contact",
         camera="medium shot, eye level, the two figures in the upper half, dark weedy ground as the lower third",
         amb="jungle_night", sens="violence",
         safe="the stranger grabbing her, covering her mouth and dragging her is not shown: Malak covers her own mouth, "
              "the faceless silhouette keeps an arm's length away with a finger to his lips; no touch"),
    dict(to=32, reason="action change: she fights to escape, then gives in and nods; the drizzle begins", chars=["malak"], loc="site_hide",
         visual=f"{MALAK_NIGHT}, pressed back against the cinder-block wall clutching her shoulder bag defensively to her "
                f"chest, tear-streaked defiant face slowly giving way to a small reluctant nod; {SILHOUETTE} an arm's "
                "length away, both open palms raised in a pleading calming gesture; fine drizzle glinting in the "
                "flickering blue-red police light; no contact between them",
         camera="medium two-shot from the side, eye level, faces in the upper half, wet ground below",
         amb="building_site_rain", sens="violence",
         safe="her hitting him with her bags and his holding her are not shown: she clutches her bag defensively, he "
              "keeps his distance with raised palms; no touch"),
    dict(to=35, reason="scene change: Malak lets herself into Zain's dark apartment and leans on the closed door",
         chars=["malak"], loc="apt_door",
         visual=f"{MALAK_WET}, standing with her back against the closed front door of a dark sitting room, head tilted "
                "back, eyes half-closed, exhausted and pale, dropping a small key into her handbag; her hijab slightly "
                "damp and creased but fully covering her hair and neck; no marks on her face",
         camera="medium shot, eye level, her face in the upper third, the dark tiled floor as the lower third",
         amb="apartment_rain_night", sens="violence",
         safe="her bleeding lip, grazed forehead and dirty dress are not shown: only a pale exhausted face and a damp hijab"),
    dict(to=38, reason="action change: the bag slips to the floor, she shivers at the memory and starts to cry",
         chars=["malak"], loc="apt_door",
         visual=f"close view of {MALAK_WET}, eyes closed, one hand pressed flat on her chest, tears running down her "
                "pale face, shivering; her black handbag fallen on the dark tiles at her feet",
         camera="close-up, eye level, her face in the upper third, the fallen bag at the bottom of the frame",
         amb="apartment_rain_night"),
    dict(to=41, reason="action change: a woman's voice from the bedroom; she walks to the closed door and freezes",
         chars=["malak"], loc="apt_hall",
         visual=f"{MALAK_WET}, seen from behind and slightly to the side, standing frozen in the dark hallway a step "
                "from a closed white bedroom door with a thin strip of warm light under it, one hand half-raised "
                "towards the wall, listening",
         camera="medium wide over her shoulder, the lit door gap in the upper middle, dark tiled floor as the lower third",
         amb="apartment_rain_night", sens="intimacy",
         safe="Zain and Kiyaara are never shown: only the closed bedroom door with light under it"),
    dict(to=44, reason="detail image: the cut birthday cake in the dark sitting room while Zain's voice is heard", loc="cake",
         visual="a half-cut round birthday cake with white cream icing on a plate on a small low table in the dark "
                "sitting room, a knife-less clean plate with a used fork beside it, extinguished plain candles with no "
                "numbers lying on the plate, a thin strip of warm light from the hallway falling across the table; no "
                "people, no lettering on the cake",
         camera="close-up, slightly high angle, the cake in the upper half, the dark table top as the lower third",
         amb="apartment_rain_night"),
    dict(to=48, reason="emotional turning point: listening to the betrayal, tears welling", chars=["malak"], loc="apt_hall",
         visual=f"close view of {MALAK_WET}, standing beside the closed bedroom door with her shoulder against the "
                "hallway wall, face half-lit by the warm strip of light from under the door, eyes brimming with tears, "
                "lips pressed together, devastated disbelief",
         camera="close-up, eye level, her face in the upper third",
         amb="apartment_rain_night", sens="intimacy",
         safe="the affair is only heard; nobody else is shown"),
    dict(to=52, reason="action change: she slides down to the floor, biting her lip, then covers her ears", chars=["malak"], loc="apt_hall",
         visual=f"{MALAK_WET}, sitting on the dark hallway floor with her back against the wall beside the closed "
                "bedroom door, knees drawn up, both hands pressed over her ears over the hijab, eyes squeezed shut, "
                "biting her lower lip to hold back sobs; the thin strip of warm light under the door beside her",
         camera="medium shot, slightly high angle, her face in the upper half, tiled floor as the lower third",
         amb="apartment_rain_night"),
    dict(to=56, reason="scene change: she picks up her bag, leaves and leans against the door outside", chars=["malak"], loc="apt_outside",
         visual=f"{MALAK_WET}, standing on the wet outside landing with her back against the closed apartment door, "
                "handbag hanging from her hand, eyes closed, biting her lip, tears on her cheeks; heavy rain pouring "
                "beyond the low railing",
         camera="medium shot, eye level, her face in the upper third, the wet landing floor as the lower third",
         amb="rain_night"),
    dict(to=58, reason="action change: thunder; she wipes her tears and runs off into the dark storm", chars=["malak"], loc="storm_road",
         visual=f"{MALAK_WET}, seen from behind, running away down the dark tree-lined sandy road in pouring rain, "
                "the handbag clutched to her side, a lightning flash lighting the rain sheets and thrashing trees, "
                "her figure about to vanish into the darkness",
         camera="wide shot from behind, low angle, the figure in the upper half, the wet flooded road as the lower third",
         amb="storm_night"),
    dict(to=62, reason="time jump: the next sunny morning in her bedroom, sleepless and with a headache", chars=["malak"],
         loc="malak_room", transition="black",
         visual="Malak in her wine-maroon kurta and black hijab fully covering her hair and neck, sitting up on the "
                "edge of her single bed, one forearm raised to shield her eyes from a bright shaft of morning sunlight "
                "streaming through the window, her other hand pressed to her temple, tired pale face",
         camera="medium shot, eye level, her face in the upper third, the plain sheet and floor as the lower third",
         amb="room_day", sens="other", safe="narration says she lay in bed: shown sitting up, hijab on"),
    dict(to=65, reason="scene and character change: Vimla sweeping the yard; Aanis comes in with a bag from Aashiya",
         chars=["vimla", "aanis"], loc="yard",
         visual="Vimla in her mustard libaas and brown floral headscarf holding a traditional coconut-rib broom "
                "(ilolhi-fathi) in the sandy yard, taking a small plastic carrier bag from Aanis, pulling a wry face; "
                "Aanis in his white skullcap, cream shirt and checked sarong having just come in through the wooden "
                "gate, holding out the bag; the breadfruit tree and the joali behind them",
         camera="medium wide two-shot, eye level, faces in the upper half, swept sand as the lower third",
         amb="island_house_day"),
    dict(to=70, reason="action change: Aanis on the joali with his phone, Vimla sits beside him and bickers",
         chars=["aanis", "vimla"], loc="joali",
         visual="Aanis reclining back seated on the wooden joali swing chair under the breadfruit tree, reading his "
                "phone with a deliberately calm indifferent face (screen faces away, nothing readable); Vimla sitting "
                "on a second joali beside him, turned towards him, gesturing with one hand mid-complaint, worried "
                "frown; the broom leaning against the tree",
         camera="medium two-shot, eye level, faces in the upper half, sandy yard as the lower third",
         amb="island_house_day", sens="other", safe="narration says he lay on the joali: shown reclining but seated"),
    dict(to=72, reason="character enters: Malak steps out of the house putting on sunglasses; her parents turn", chars=["malak"], loc="veranda",
         visual="Malak in her wine-maroon kurta and black hijab fully covering her hair and neck, stepping out of the "
                "house door onto the small veranda, sliding a pair of dark sunglasses onto her face with one hand, "
                "cool guarded expression, chin up; pale green coral-stone wall behind her",
         camera="medium close-up, slightly low angle, her face in the upper third",
         amb="island_house_day", sens="violence",
         safe="her swollen lip and grazed forehead are hidden: sunglasses and a guarded face, no visible marks"),
    dict(to=76, reason="action change: the confrontation — Vimla questions her, notices her face; Aanis gets up",
         chars=["malak", "vimla", "aanis"], loc="veranda",
         visual="Malak in her wine-maroon kurta, black hijab and dark sunglasses standing on the veranda step, one hand "
                "lifted to the edge of her hijab near her forehead, lips pressed tight; Vimla in her mustard libaas and "
                "brown floral headscarf a few steps away in the yard, peering at Malak's face with surprise turning to "
                "worry; Aanis in his white skullcap and checked sarong rising from the joali behind, looking at Malak",
         camera="medium wide, eye level, three faces in the upper half, the sandy yard as the lower third",
         amb="island_house_day", sens="violence",
         safe="her injuries are only spoken of: she wears sunglasses and touches her hijab edge; nothing visible"),
    dict(to=77, reason="character change: police officers walk into the yard; Malak steps back", chars=["malak"], loc="yard_police",
         visual="the wooden gate of the sandy yard swinging open as two police officers in dark-navy uniforms walk in, "
                "seen mid-stride from the chest down and slightly out of focus, faces out of frame; in the foreground "
                "Malak in her wine-maroon kurta, black hijab and dark sunglasses taking a step back, her hand at her chest",
         camera="over-the-shoulder medium shot from behind Malak, the officers at the gate in the upper half, sand below",
         amb="island_house_day"),
    dict(to=79, reuse="beat_018", reason="memory flash: the run through the dark rain that night", loc="storm_road",
         visual="(reuse)", amb="memory_rain", transition="dissolve", sens="violence",
         safe="the memory of the falling man is carried by the storm-run image only; nothing shown"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The light of day was ending, and as if announcing that darkness was taking hold of the world, the dhoni came rolling over the waves.",
   [("dhoni_engine", "ދޫނި", -22)])
sh(2, "The heat of the sun had gone completely, and a damp coolness had begun to fill the air. The clouds in the sky, like tufts of white cotton, slowly vanished from sight and the journey of the dark clouds began.")
sh(3, "Signs of coming rain were spreading over the world. All around were dense trees. The gentle gusts of wind were no secret to the leaves of the trees.",
   [("wind_gust", "ވައިރޯޅި", -22), ("leaves_rustle", "ފަތްތަކުން", -24)])
sh(4, "The waves of the sea, too, bore witness to the wind. The sound of an engine from far away came closer and closer.",
   [("wave_crash", "ލޮނުގަނޑު", -22), ("dhoni_engine", "އިންޖީނުގެ", -18)])
sh(5, "The ferry came alongside the jetty with the call to the Maghrib prayer. The people from the ferry slowly got off.",
   [("footsteps_pavement", "ފައިބަމުން", -24)])
sh(6, "Malak too got off the ferry holding the paper bag she had brought, and walked towards the parked motorbikes.",
   [("footsteps_pavement", "ހިނގައިގަތީ", -22)])
sh(7, "Malak was forced to stop because her motorbike was not there. But when she saw her motorbike turning the corner four lanes away, she ran to stop it.",
   [("motorbike_pass", "އެޅިތަން", -18), ("footsteps_pavement", "ދުވައިގަތީ", -20)])
sh(8, "Standing at the corner looking where the motorbike had gone, she drew her brows together, straightened the bag on her shoulder and walked on along the road.",
   [("footsteps_pavement", "ހިނގައިގަތީ", -22)])
sh(9, "This time she would not let that person off. Malak walked very fast. She was already late to get to Zain.",
   [("footsteps_pavement", "ހިނގުން", -22)])
sh(10, "After all, she had come to the island tonight only for Zain — to celebrate Zain's birthday.")
sh(11, "And also to give the answer to the question he had asked before she left for the resort. Her heart was racing because it was about to rain, and because the road she was walking was a dark road.",
   [("heartbeat", "އަވަސް", -24)])
sh(12, "Eerie sounds could be heard. The wind blowing was damp and cold. Since it was a main road, she kept thinking of a way to find the motorbike.",
   [("wind_gust", "ވައިގާ", -22)])
sh(13, "Still, without losing heart, she walked even faster than before, switching the bag in her hands from one hand to the other.",
   [("paper_shuffle", "ކޮތަޅު", -22)])
sh(14, "She checked the time on her phone when she heard the call to the Isha prayer. She had spent more than an hour on that road.")
sh(15, "She grew angrier than before. She ended up stopping near some guesthouses that had started being built. On reaching that spot Malak grew more frightened than before.",
   [("breath", "ބިރުގަތެވެ", -22)])
sh(16, "Some of the materials of the unfinished work were piled up on one side. It had been ages since work on this place stopped.")
sh(17, "The place was now the home of the young people around here. If a kid went missing, you'd find them by coming here. Just recently an incident had happened at this place.")
sh(18, "When that came to mind, Malak's heart beat harder. 'Would Malak face something like that?' she found herself saying inside. No. That would not happen.",
   [("heartbeat", "ވިންދު", -18)])
sh(19, "It was just paranoia. It wasn't her first time coming here. But coming to that place at such a late hour made Malak hesitate.")
sh(20, "Hearing some people talking, Malak walked towards it — because it was also a voice she knew.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(21, "Before she could get there, someone fell from above right next to Malak's feet. As he fell, Malak let out a scream.",
   [("heartbeat", "ވެއްޓިޖެހުނީ", -16), ("gasp", "ހަޅޭ", -16)], hum=True)
sh(22, "Blood was coming from the man's nose and mouth. Lying where he had fallen, the man closed his eyes. His life was gone.",
   [("heartbeat", "ފުރާނަ", -18)], hum=True)
sh(23, "Malak's voice fell silent that very instant, as someone put a hand over her mouth and pulled her back, hiding her from the others' eyes.",
   [("breath_heavy", "ހިމޭންވީ", -20)], hum=True)
sh(24, "He forcibly dragged Malak backwards. 'Hush.' It was a man's voice whispering beside Malak's ear. By then the sound of police sirens could be heard.",
   [("siren", "ސައިރަން", -18)])
sh(25, "Malak stood crying in fear, trying to push the man's hand away from her mouth.",
   [("sob_breath", "ރޮވިފައި", -22)])
sh(26, "With his hand over Malak's mouth the man slowly moved backwards. 'Please don't make a noise. The police are coming.",
   [("siren", "ޕޮލިސް", -22)])
sh(27, "I need your help, please. Don't make a noise. Otherwise we'll both be arrested.")
sh(28, "The blame for that man's death will fall on your head too.' The man said it in a very low whisper.")
sh(29, "Malak kept hitting the man with the bag and the handbag in her hands, looking for any way to escape. 'Please...'",
   [("cloth_rustle", "ޖަހަންމުން", -20)])
sh(30, "the man said softly in a pleading tone. Malak was still struggling to get free.",
   [("breath_heavy", "ތެޅިފޮޅެމުން", -22)])
sh(31, "Holding Malak tightly, the man kept backing away from the place. In the end, when there was no way to escape, Malak nodded and said yes.")
sh(32, "Azaan slowly took his hand away. A fine drizzle was falling by then. 'Good girl,' the man whispered very softly.",
   [("rain_start", "ހިމަފޮދުވާރޭ", -18)])
sh(33, "Malak slowly opened the apartment door and went inside. There was no light at all in the sitting room. Malak's face showed fear and exhaustion.",
   [("door_open", "ހުޅުވާލާފައި", -18)])
sh(34, "Closing the door, Malak leaned against it. She put the key in her hand into her bag. Blood had come from Malak's mouth.",
   [("door_close", "ދޮރުލައްޕާ", -18), ("keys_jingle", "ތަޅުދަނޑި", -20)])
sh(35, "Her forehead was slightly grazed too. The clothes she was wearing were dirty. Her hair was dishevelled.")
sh(36, "She was soaked to some extent. The bag in Malak's hand slipped and fell to the floor. Exhausted, she closed her eyes.",
   [("soft_thud", "ވެއްޓުނެވެ", -20)])
sh(37, "Even remembering what had happened tonight made her shudder. She slowly put her hand to her chest. She began to cry.",
   [("sob_breath", "ރޮވެން", -20)], hum=True)
sh(38, "She resolved never to go that way again. It was such an eerie place. While Malak was still unable to calm down, a woman's voice reached her ears.")
sh(39, "Malak opened her eyes and looked towards the bedroom door. What added even more to her fear was the woman's voice heard from inside the room.")
sh(40, "A girl could be heard talking very softly. Paying attention to the voice, Malak slowly walked forward.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(41, "Bewildered, she went on. She stopped beside the door. Then her eyes fell on the cut cake on the small sitting-room table. 'Hmm...")
sh(42, "At my birthday last year.' It was Zain's voice. He was answering a question the girl had asked.")
sh(43, "Worry showed on Malak's face more than before. Tears gathered in her eyes. 'That was me, wasn't it...' the girl said. 'Hmm...'",
   hum=True)
sh(44, "'Then what does Malak do for you?' There was no answer from Zain to the girl's question. Malak began to sob. 'Tell me. Why didn't you say?",
   [("sob_breath", "ގިސްލެވެން", -22)])
sh(45, "What is Malak for, then?' the girl said in a bored tone. 'Kiyaara, what are you starting now? Don't bring up Malak right now...'")
sh(46, "Zain was heard saying. 'I'm just amazed. How do you manage like that? Zain is so patient,' Kiyaara said very softly.")
sh(47, "'I won't go that far with her without marrying her — Kiyaara knows that well. She isn't a girl like Kiyaara.")
sh(48, "That's exactly why I like her,' Zain said. 'So boring. Go to that boring woman then,' Kiyaara's voice was heard.")
sh(49, "Zain began to laugh. 'Jealous?' he was heard saying. Malak slowly sank down where she stood. It was as if the strength had left her body.",
   [("cloth_rustle", "ތިރިވިއެވެ", -22)], hum=True)
sh(50, "She bit her lip in case she sobbed aloud. Kiyaara was her closest friend — the special confidante who had kept all her secrets.",
   [("sob_breath", "ގިސްލެވިދާނެތީ", -22)])
sh(51, "They had studied together since the age of eight. All three of them did their O-levels and A-levels at the same place.")
sh(52, "The three of them even completed their higher education abroad together. Malak put her hands over her ears so as not to hear the sounds from the room.")
sh(53, "Even then Malak kept sobbing. Closing her tear-filled eyes, she slowly got up and started to leave.",
   [("sob_breath", "ގިސްލެވެމުން", -22)])
sh(54, "She picked up her fallen bag and opened the door. She looked into the house one last time. Slowly closing the door, she leaned against it.",
   [("door_open", "ހުޅުވާލިއެވެ", -18), ("door_close", "ދޮރުލައްޕާ", -18)])
sh(55, "Biting her lip so as not to sob, she closed her eyes. The two people closest to her heart had stabbed her in the heart and made her weep.",
   hum=True)
sh(56, "How much she had trusted them! And what had she got in return? Betrayal and deceit.", hum=True)
sh(57, "Malak was startled by a flash of lightning and a loud crack of thunder. By then the rain was pouring heavily. Wiping the tears from her eyes, Malak ran off along the road.",
   [("thunder", "ގުގުރީގެ", -14), ("footsteps_pavement", "ދުއްވައިގަތެވެ", -20)], hum=True)
sh(58, "Malak disappeared into the darkness and the pouring rain. After the heavy rain of the night stopped, the sunlight bathed the whole island.")
sh(59, "Slowly the sunlight spread and fell into the room. When the sunlight fell on Malak's face she laid one arm across it.")
sh(60, "She didn't even know when she had fallen asleep, lying there thinking about what had happened in the night.")
sh(61, "Waking at the call to the Fajr prayer, she prayed and lay down to try to sleep again. But sleep would not come. Malak slowly got up and sat.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(62, "Her mother Vimla's voice could be heard in the yard. Malak rubbed her face with both hands. Her head ached terribly.")
sh(63, "Vimla, getting a good grip on the broom, began sweeping the yard. Aanis opened the door from outside and came in.",
   [("door_open", "ހުޅުވާލާފައި", -20)])
sh(64, "Stopping beside Vimla, he held out the bag in his hand. 'Here, something Aashiya gave,' Aanis said.",
   [("paper_shuffle", "ކޮތަޅު", -22)])
sh(65, "Putting the broom aside, Vimla took the bag from Aanis and looked into it. 'Hmm, so I did tell them about the rat burrow in their tree.'",
   [("paper_shuffle", "ކޮތަޅު", -22)])
sh(66, "she said, pulling a face. Ignoring what Vimla said, Aanis went and settled back on the joali, picked up his phone and began reading the news.",
   [("creak", "ޖޯލީގައި", -22)])
sh(67, "His actions showed that he did not want to argue with Vimla. 'Why don't you say anything? Is Aanis upset that I had a go at Aashiya?")
sh(68, "That's fun.' Sitting down on the joali next to him, Vimla talked on. 'Why should I be upset? You two can keep on bickering.",
   [("creak", "ޖޯލީގައި", -22)])
sh(69, "I won't lose a thing from it,' Aanis said calmly. 'Yes... why would you lose anything? When I'm the one who has to carry everything on my head...")
sh(70, "Everything is the same to Aanis, whatever happens. Even now I'm wondering — between us, when will that Malak ever marry someone?'")
sh(71, "she said in a worried tone. 'Don't think about that. I'll marry when I need to marry,' Malak said, coming out of the house and putting on her sunglasses.",
   [("footsteps_sand", "ނިކުނަންމުން", -22)])
sh(72, "Vimla and her husband both looked towards the door. 'When did you come, dear?' Vimla asked in a surprised tone.")
sh(73, "'What, can't I come to my own home?' Malak asked, displeased. 'Mum isn't saying anything to make Malak angry, is she?")
sh(74, "Mum is asking when you came. When Mum went to bed you hadn't come home — and you never even said you'd come home at night.'")
sh(75, "Vimla said. Malak thought about how to answer her mother's question. If she said she had come because it was Zain's birthday, her mother's complaints would never stop.")
sh(76, "'What happened to your forehead? Your lips are swollen too,' Vimla said in a worried tone. Aanis too got up from the joali and looked at Malak.",
   [("creak", "ޖޯލިން", -22)])
sh(77, "At that moment, seeing police come into the yard, Malak stepped back. What had happened in the night rose before her eyes.",
   [("footsteps_sand", "ވަދެގެން", -20), ("heartbeat", "ޖެހިލެވުނެވެ", -18)], hum=True)
sh(78, "Remembering the man who fell dead from the guesthouse, fear showed on her face. Her heart raced and she began to sweat.",
   [("heartbeat", "ވިންދު", -16)], hum=True)
sh(79, "And the run she had made through the dark, among the dense trees in the pouring rain, to save her honour and dignity.",
   [("thunder", "ވާރެ", -20)], hum=True)
SHOTS = S

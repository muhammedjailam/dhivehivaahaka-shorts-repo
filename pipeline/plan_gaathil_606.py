"""Beat/shot plan for Gaathil episode 606 (series opener; used by plan_beats.py)."""

LOC = {
    "storm_lighthouse": "the east tip of a small Maldivian island on a stormy night: an old abandoned white coral-stone lighthouse, crumbling and streaked with black mould, rising from a low rocky point above a black churning sea, leaning wind-bent coconut palms and screw-pines around its base, heavy black clouds pressing down",
    "lighthouse_rocks": "the wet rocky ground and sand at the foot of the old abandoned coral-stone lighthouse on the island's east tip at night: puddles, wind-bent screw-pines and coconut palms, the crumbling mould-stained tower and its old weathered wooden door a short distance away, the black sea beyond",
    "rain_lane": "a narrow sandy island lane at night in pouring rain: old whitewashed coral-stone walls with arched wooden windows on both sides, coconut palms thrashing overhead, puddles on the sand, a single weak yellow lamp far ahead",
    "shahid_room": "Shahid's room in an old coral-stone island house at night: a wooden desk with a desktop computer and a big monitor, a camera connected by a cable, a coffee mug, camera bags and lenses on a shelf, a window with wooden shutters streaked with rain, a single bare ceiling bulb, a closed wooden door behind",
    "photo": "the photograph itself filling the frame: a dark rainy night among the black shadows of trees near the old lighthouse, silver streaks of rain, wet ground",
    "room_door": "the open wooden door of Shahid's room at night: a dim narrow corridor of the old coral-stone house beyond, the warm bulb light of the room spilling onto the corridor floor",
    "memory_warehouse": "a memory of the island twenty years ago: an old whitewashed coral-stone club warehouse with a corrugated roof and closed wooden double doors on a sandy open ground at night, coconut palms, a dark sky",
    "memory_search": "a memory of the island twenty years ago: a dark lagoon and reef at night, small wooden boats with torches moving over the shallows, the silhouettes of small uninhabited islands on the horizon",
    "morning_window": "Shahid's room in the early morning: the wooden shutters of the window thrown open onto a sandy island lane and coconut palms, the desk and the dark monitor behind",
    "morning_lane": "a sandy island lane in the morning: old whitewashed coral-stone houses with arched wooden windows, a small corner shop with an open wooden counter, coconut palms, puddles from the night's rain drying on the sand",
    "police_room": "a bare interview room in a modest whitewashed island police station: a plain table with a closed laptop, two plain chairs facing each other, grey walls, a single window in a plain wooden frame showing a pale sky, a closed door",
}
MOOD = {
    "storm_lighthouse": "pitch-dark stormy night, near-black blue-grey, heavy slanting silver rain, a distant flicker of lightning in the clouds, ominous and eerie",
    "lighthouse_rocks": "stormy night, near-black blue-grey, silver rain streaks, white lightning light on wet surfaces, tense and haunting",
    "rain_lane": "stormy night, near-black blue-grey, heavy rain, faint yellow lamp glow on wet sand, urgent and uneasy",
    "shahid_room": "room at night: a single warm ceiling bulb and the cold blue-white glow of the monitor, rain streaming down the window glass, deep shadows in the corners, tense and claustrophobic",
    "photo": "a dark night photograph: near-black blue-grey, silver rain, a faint cold flash of lightning on wet surfaces, grainy, unsettling and silent",
    "room_door": "night, a warm bulb light against the dark corridor, quiet and tense, a touch of tenderness",
    "memory_warehouse": "faded desaturated sepia memory haze, soft blurred edges, grainy, distant warm lantern glow, sorrowful and secretive",
    "memory_search": "faded desaturated sepia memory haze, soft blurred edges, distant torch glows on dark water, hopeless and grieving",
    "morning_window": "the next morning, pale gold sunlight streaming in, long soft shadows, yet a heavy, sleepless mood",
    "morning_lane": "bright pale gold morning sunlight, long shadows on the sand, quiet, wary and suspicious",
    "police_room": "mid-morning, cold grey police-room light from the single window, flat and bare, tense and silent",
}

HIJ_M = "her beige headscarf fully covering her hair and neck"
WET = "his olive-green utility shirt darkened by rain but still loose and opaque over the grey t-shirt, his black hair wet and plastered to his forehead"
MON = "the big monitor showing only a dark rainy night photograph, no interface, no text"
IB_PHOTO = ("a gaunt weathered man in his fifties with grey stubble and untidy grey-black hair, wearing an old-fashioned heavy "
            "dark-brown thick wool long coat soaked by rain, a real living human man, not a ghost")

BEATS = [
    dict(to=2, reason="episode opening: the pitch-dark stormy night and the old crumbling lighthouse at the island's east tip", loc="storm_lighthouse",
         visual="a wide, ominous view of the old abandoned white coral-stone lighthouse at the island's east tip, crumbling and black-streaked with mould, towering against heavy black storm clouds above a churning black sea; slanting silver sheets of rain, a faint distant flicker of lightning inside the clouds, wind-bent palms and screw-pines thrashing around its base; no people, no faces or shapes in the clouds",
         camera="wide low-angle establishing shot, the lighthouse and the storm in the upper two-thirds, the dark wet rocks and foaming water as a calm lower third",
         amb="storm_night", sens="other", safe="the 'giant spirit rising from the sea' is atmosphere only: an ominous tower in the storm, no faces or ghostly shapes"),
    dict(to=5, reason="character introduced: photographer Ali Shahid with his expensive camera, aiming at the lighthouse door in the rain", chars=["shahid"], loc="lighthouse_rocks",
         visual=f"Ali Shahid standing on the wet rocks in the pouring rain at night, {WET}, raising his expensive black camera with a long lens to his eye, aiming it at the old weathered wooden door of the crumbling lighthouse; his face in three-quarter view, focused, holding his breath; silver rain streaks, the dark tower looming behind at the side",
         camera="medium shot from the side, eye level, Shahid's face and camera in the upper two-thirds, the wet rocks and puddles as the lower third",
         amb="storm_night"),
    dict(to=6, reason="action/turning point: a thunderclap and a blinding lightning flash as the shutter clicks", chars=["shahid"], loc="lighthouse_rocks",
         visual=f"seen from behind over Shahid's shoulder: his dark silhouette in the rain holding the camera up to his eye, and ahead of him the whole crumbling lighthouse and the trees around it suddenly lit stark white by a huge branching bolt of lightning splitting the black sky; rain frozen in the flash as silver streaks; no other people",
         camera="over-the-shoulder wide shot from behind, the lit lighthouse and lightning in the upper two-thirds, Shahid's dark shoulder at the side, the wet rocks as the lower third",
         amb="storm_night"),
    dict(to=8, reason="emotional change: a strange cold feeling, goose-bumps, an uneasy mood; he lowers the camera", chars=["shahid"], loc="lighthouse_rocks",
         visual=f"close-up of Shahid lowering his camera in the rain, {WET}, rain dripping from his face; he glances sideways into the black shadows of the trees with a frown of unexplained unease, shoulders drawn up as if from a sudden chill; the dark trees behind him empty and out of focus",
         camera="close-up, eye level, his face in the upper half, the camera in his hands and dark wet ground as the lower third",
         amb="storm_night", sens="other", safe="the uncanny feeling is shown only on his face; the trees behind are empty"),
    dict(to=9, reason="scene change: soaked, he hurries home through the rain-lashed lanes", chars=["shahid"], loc="rain_lane",
         visual=f"Shahid hurrying along the narrow sandy lane in the pouring rain at night, half running towards the camera, hunched forward, clutching his camera against his chest under one arm, {WET}; splashing through puddles, palms thrashing above the coral-stone walls",
         camera="medium-wide, eye level, Shahid in the upper-middle, the wet sand and puddles as the lower third",
         amb="rain_night"),
    dict(to=11, reason="scene change: in his locked room he transfers the photos to the computer — and at the last photo his eyes widen and the coffee mug slips onto the desk", chars=["shahid"], loc="shahid_room",
         visual=f"Shahid sitting at his desk in his room at night, damp hair, his camera connected by a cable to the computer, {MON}; his eyes suddenly wide and fixed on the screen, his hand just letting go of a coffee mug which tips over on the desk, a little dark coffee spilling across the wooden desk top; the rain-streaked shuttered window and the single warm bulb behind",
         camera="medium shot from the side of the desk, Shahid's face lit by the cold monitor glow in the upper half, the desk top with the tipped mug as the lower third",
         amb="apartment_rain_night"),
    dict(to=14, reason="reveal: the last photo — among the shadows of the trees a figure who is not an ordinary person, in an old heavy coat, standing in the downpour", chars=["ibrahim"], loc="photo", transition="dissolve",
         visual=f"the photograph full frame: a dark rainy night among black tree shadows near the base of the old lighthouse; in the middle distance, half emerging from the shadows of the trees, a lone man standing still and upright in the downpour — {IB_PHOTO}; his face small and shadowed, not yet clear; silver rain streaks, wet ground, the edge of the lighthouse wall at the side",
         camera="wide photo framing, the standing figure small in the upper-middle third, dark wet ground as the lower third",
         amb="apartment_rain_night", sens="other", safe="a real man in the rain, unsettling but human; no ghostly glow, no transparency"),
    dict(to=16, reason="action change: gripping the mouse he zooms in 50, 100, 300% — his breath catches", chars=["shahid"], loc="shahid_room",
         visual=f"close-up of Shahid leaning in towards the big monitor, his hand tight on the mouse, his face lit cold blue-white by the screen, breath held, eyes wide and unblinking; {MON}, showing an enlarged, grainy dark figure among trees; the warm bulb a blur behind him",
         camera="close-up from the side of the monitor, his face in the upper half, the hand on the mouse and the desk top as the lower third",
         amb="apartment_rain_night"),
    dict(to=19, reason="reveal of the face: Ibrahim Naseem, who vanished 20 years ago, staring straight into the lens with pain and fear", chars=["ibrahim"], loc="photo", transition="dissolve",
         visual=f"the zoomed photograph full frame: the face and shoulders of {IB_PHOTO}; rain running down his face, deep-set haunted eyes looking straight into the camera lens, an expression of deep pain and fear; dark tree shadows behind him, silver rain, slight photographic grain",
         camera="close-up, eye level, his face and eyes in the upper half, the wet coat collar as the lower third",
         amb="apartment_rain_night", sens="other", safe="Ibrahim is shown as a living, ordinary, frightened man — never a ghost or a corpse"),
    dict(to=22, reason="action change: the bulb flickers and a slow knock sounds on the door behind him", chars=["shahid"], loc="shahid_room",
         visual=f"Shahid seated at the desk, frozen, half turning his head over his shoulder towards the closed wooden door of his room behind him; the bare ceiling bulb above dimmed and flickering, deep shadows jumping across the walls; {MON} glowing cold beside him; the door handle in shadow",
         camera="medium-wide from beside the desk, Shahid's frightened face and the door in the upper two-thirds, the dim floor as the lower third",
         amb="apartment_rain_night"),
    dict(to=23, reason="return to Ibrahim's frightening eyes on the screen (the fear spiralling in his head)", chars=["ibrahim"], loc="photo",
         reuse="beat_009", amb="apartment_rain_night", visual="(reuse of beat_009)", transition="dissolve"),
    dict(to=24, reason="action change: the wind bangs the window shutters open; he clutches his chest", chars=["shahid"], loc="shahid_room", transition="dissolve",
         visual=f"the wooden window shutters of Shahid's room flung open by a gust of wind, rain blowing in, the night outside black with a white lightning glare; Shahid in the foreground at the side, startled, recoiling with one hand pressed to his chest, his face turned to the window",
         camera="medium shot, eye level, Shahid's startled face and the banging shutters in the upper two-thirds, the rain-wet desk edge and floor as the lower third",
         amb="apartment_rain_night"),
    dict(to=26, reason="action change: he slowly gets up, walks to the door and unlocks it with a trembling hand", chars=["shahid"], loc="shahid_room",
         visual="close shot of Shahid's trembling hand on the old metal key in the lock of the closed wooden door of his room, turning it slowly; his tense face at the side in soft focus, lit by the warm bulb; the door's worn wood and shadow",
         camera="close shot at door height, the hand on the key and his face in the upper two-thirds, the dark floor and the door's lower panel as the lower third",
         amb="apartment_rain_night"),
    dict(to=29, reason="character enters: his worried old mother at the door; he forces a smile and says the coffee mug fell", chars=["shahid_mother", "shahid"], loc="room_door", speaker="shahid_mother",
         visual=f"Shahid's elderly mother standing in the open doorway in her loose maroon long dress with {HIJ_M}, her face full of worry, speaking gently with one hand raised to her chest; Shahid at the side of the frame in the foreground in three-quarter view, holding the door, forcing a tight, unconvincing smile",
         camera="over-the-shoulder medium shot, the mother centred and sharp in the upper half, Shahid soft at the side, the warm-lit floor as the lower third",
         amb="apartment_rain_night"),
    dict(to=30, reason="return to the screen: door locked again, he sits back down and stares at the photo", chars=["shahid"], loc="shahid_room",
         reuse="beat_008", amb="apartment_rain_night", visual="(reuse of beat_008)"),
    dict(to=33, reason="flashback: 20 years ago — the night the powerful businessman was found dead near the island club warehouse", loc="memory_warehouse", transition="dissolve",
         visual="a faded sepia memory: the old whitewashed coral-stone club warehouse at night seen from a distance, its wooden doors shut; a small crowd of islander men in shirts and sarongs holding kerosene lanterns, standing far back at the edge of the sandy ground, seen from behind, looking towards it in shock; palm silhouettes, a dark sky; no body, no blood, no weapon, no victim, no children",
         camera="wide shot, eye level, the warehouse and lantern glow in the upper two-thirds, the dark sand as the lower third",
         amb="memory", sens="violence", safe="the murder and the victim are never shown: only the shut warehouse at night and islanders with lanterns at a distance, in a sepia memory haze; Shahid as a small child is not shown"),
    dict(to=35, reason="flashback scene change: police and islanders search the island, the uninhabited islands and the reefs", loc="memory_search", transition="dissolve",
         visual="a faded sepia memory: small wooden boats with men holding torches moving slowly across a dark lagoon and reef at night, beams of torchlight sweeping the black water, the silhouettes of small uninhabited islands on the horizon; figures small and distant, no uniforms with lettering, no weapons",
         camera="wide shot, the boats and torch beams in the upper two-thirds, the dark still water as the lower third",
         amb="memory", sens="other", safe="'drowned or died' is shown only as a search over dark water; no body"),
    dict(to=37, reason="return from the memory to the screen: \"But he's alive!\" — he enlarges the photo further", chars=["shahid"], loc="shahid_room",
         reuse="beat_008", amb="apartment_rain_night", visual="(reuse of beat_008)", transition="dissolve"),
    dict(to=39, reason="new detail in the photo: an oddly shaped iron piece at Ibrahim's feet and part of an old decaying wall behind him", loc="photo", transition="dissolve",
         visual="the zoomed photograph full frame, lower part of the scene: the wet muddy ground under the rain with the hem of a heavy dark-brown wool coat and a pair of old wet boots at the top of the frame, and beside them a strange, oddly shaped broken rusty iron piece lying on the ground; behind, part of an old decaying, broken coral-stone wall with crumbling edges and black mould; silver rain, dark grain; no face",
         camera="close detail framing, the iron piece and the broken wall in the upper two-thirds, the dark wet mud as the lower third",
         amb="apartment_rain_night"),
    dict(to=41, reason="emotional turning point: he grasps the depth of the secret and decides to take the photo to the police in the morning", chars=["shahid"], loc="shahid_room",
         visual=f"Shahid sitting back in his chair at the desk late at night, tense and resolute, holding a small memory card between his fingers and staring at it, jaw clenched; the monitor glowing cold behind him, rain on the shuttered window, the warm bulb above",
         camera="medium close-up, eye level, his face and the memory card in the upper half, the desk top as the lower third",
         amb="apartment_rain_night"),
    dict(to=43, reason="narrator's foreboding: the path he is taking leads into a dark pit (hold on the storm and the lighthouse)", loc="storm_lighthouse",
         reuse="beat_001", amb="storm_night", visual="(reuse of beat_001)"),
    dict(to=44, reason="action change: lost in these thoughts, he falls asleep at the desk", chars=["shahid"], loc="shahid_room",
         visual=f"Shahid asleep slumped forward at his desk, head resting on his folded arms beside the keyboard, the memory card beside his hand; the monitor dimmed to a faint glow, the bulb low, the rain on the window softer",
         camera="medium-wide, slightly high angle, Shahid and the glowing monitor in the upper two-thirds, the desk top as the lower third",
         amb="apartment_rain_night"),
    dict(to=46, reason="time jump: the golden next morning lights the island, but darkness stays in his heart", chars=["shahid"], loc="morning_window", transition="black",
         visual="Shahid standing at the open wooden shutters of his window in the early morning, pale gold sunlight falling across his tired face, dark circles under his eyes, gazing out with a heavy, haunted look; palm trees and a sunlit sandy lane outside",
         camera="medium close-up, eye level, his face in the upper half lit gold from the side, the window sill as the lower third",
         amb="home_day"),
    dict(to=48, reason="scene change: memory card in his pocket, he walks to the police station, suspecting every face in the lane", chars=["shahid"], loc="morning_lane",
         visual="Shahid walking briskly along the sunlit sandy lane in the morning, one hand pressed to the breast pocket of his olive-green shirt, eyes narrowed and glancing suspiciously sideways at an old bearded man at a corner shop counter and a passer-by, who are soft and blurred; long morning shadows on the sand",
         camera="medium-wide, eye level, Shahid in the upper-middle, the sunlit sand and shadows as the lower third",
         amb="village_day"),
    dict(to=49, reason="scene change: alone in the cold room of the police station, waiting for the chief", chars=["shahid"], loc="police_room",
         visual="Shahid sitting alone at the bare table in the cold grey police interview room, hands clasped tightly on the table, glancing at the closed door; an empty chair opposite; the single window's pale light",
         camera="medium-wide, eye level, Shahid and the door in the upper two-thirds, the bare table top as the lower third",
         amb="detention_room"),
    dict(to=52, reason="character enters: the respected chief Officer Amjad comes in, sits and asks what big matter this is", chars=["amjad", "shahid"], loc="police_room", speaker="amjad",
         visual="Officer Amjad in his dark navy-blue police uniform shirt (no badges, no lettering, no weapon, no belt gear) seated across the table, leaning slightly forward, his sharp vigilant eyes fixed on the viewer, calm and authoritative, speaking; in the soft-focus foreground Shahid's shoulder and the back of his head; a closed laptop on the table",
         camera="over-the-shoulder medium shot, Amjad centred and sharp in the upper half, Shahid blurred in the foreground, the table top as the lower third",
         amb="detention_room"),
    dict(to=54, reason="action/speaker change: Shahid silently puts the memory card in Amjad's laptop and opens the photo — \"look at it carefully\"", chars=["shahid", "amjad"], loc="police_room", speaker="shahid",
         visual="Shahid seated across the table, facing the viewer, leaning forward as he turns the open laptop towards the other side, his other hand beside a small memory card on the table, speaking with a tense trembling look; the laptop screen faces away from the viewer and is not visible; in the soft-focus foreground the shoulder of Amjad's navy uniform",
         camera="over-the-shoulder medium shot, Shahid centred and sharp in the upper half, Amjad's shoulder blurred in the foreground, the table top as the lower third",
         amb="detention_room"),
    dict(to=57, reason="emotional turning point: as the face enlarges Amjad's colour changes — he grips a pen hard, then narrows his eyes", chars=["amjad"], loc="police_room",
         visual="close-up of Officer Amjad in his navy uniform leaning towards an OPEN laptop on the table in the foreground, its lid raised and its back facing the viewer so the screen is not visible, his face lit faintly by its cold glow, eyes fixed on the screen, the colour draining from his face, breath short, his hand gripping a pen hard on the table, knuckles tight; his eyes narrowing as he forces himself back under control",
         camera="close-up, eye level, his face in the upper half, the hand gripping the pen on the table as the lower third",
         amb="detention_room", sens="other", safe="his fear shows only in small signs: the gripped pen, narrowed eyes"),
    dict(to=59, reason="return to Amjad as he names Ibrahim Naseem in a low voice (shot)", chars=["amjad"], loc="police_room",
         reuse="beat_028", amb="detention_room", visual="(reuse of beat_028)", transition="cut"),
    dict(to=60, reason="reverse shot: Shahid insists, with passion, that Ibrahim is alive on the island", chars=["shahid", "amjad"], loc="police_room",
         reuse="beat_027", amb="detention_room", visual="(reuse of beat_027)", transition="cut"),
    dict(to=61, reason="action change: Amjad gets up from the table and stares out of the window", chars=["amjad", "shahid"], loc="police_room",
         visual="Officer Amjad standing at the single window of the police room with his back half turned, in his navy uniform, hands clasped behind him, staring out with a hard unreadable profile; Shahid small and soft at the table in the background watching him; cold grey light",
         camera="medium shot, Amjad's profile and the window in the upper two-thirds, the bare floor as the lower third",
         amb="detention_room"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The whole surroundings lay drowned in the pitch darkness of the night, in a frightening silence. The drops of heavy rain pouring from the black clouds that had thickened the sky were striking the ground with a sharp, ear-splitting sound.")
sh(2, "At the island's east tip, the leaning, crumbling old lighthouse looked like a giant spirit rising up out of the black sea.",
   hum=True)
sh(3, "It was a shadow of memories from ages long past. The famous photographer Ali Shahid stood there holding his expensive camera.")
sh(4, "His is a heart that always loves unusual, mysterious scenes. What that camera stores is, more often than not, unusual scenes.")
sh(5, "And so tonight too Shahid was busy capturing beautiful, unusual scenes of the rain. Turning the camera's lens towards the lighthouse's old door, he held his breath.")
sh(6, "With the sound of thunder and the fierce light of the lightning that lit everything up, the sound of the camera's shutter spread through the whole area.",
   [("thunder", "ގުގުރީގެ", -14), ("camera_shutter", "ޝަޓަރުގެ", -16)])
sh(7, "A strange coldness took hold of Shahid's heart. Why the hairs on his body stood on end, even he himself did not know.",
   hum=True)
sh(8, "The surroundings held a strange, uneasy feeling that cannot be described. After taking a few more photos, Shahid hurried to go home.")
sh(9, "Getting soaked in the rain, half running, he came into the house and locked his room's door. His heart was beating faster than usual.",
   [("footsteps_sand", "ދުވަމުން", -20), ("lock_click", "ތަޅުލި", -18), ("heartbeat", "ހިނގުން", -22)])
sh(10, "After connecting the camera to the computer, he moved the photos he had taken onto the big screen. The scenes were perfect.",
   [("keyboard_typing", "ބަދަލުކޮށްލި", -24)])
sh(11, "Despair showed from the lighthouse's leaning walls. But the moment the screen changed to the last photo he had taken, Shahid's eyes widened, and the coffee mug in his hand dropped onto the desk.",
   [("cup_clatter", "ބަންޑުންވި", -14)], hum=True)
sh(12, "In the pitch-dark background of the lighthouse, a figure that had stepped out from the shadows of the trees could be seen in the photo. It was not an ordinary person.",
   hum=True)
sh(13, "What he was wearing was not clothing of this age. It was a heavy coat of thick cloth from many, many years ago.")
sh(14, "Even in the pouring rain that figure stood there boldly. Shahid's hand began to tremble.",
   [("heartbeat", "ތުރުތުރު", -22)], hum=True)
sh(15, "Gripping the mouse, he began to zoom in towards the man's face. He enlarged it to fifty, a hundred and then three hundred. As the picture grew clearer,",
   [("keyboard_typing", "ޒޫމް", -24)])
sh(16, "Shahid's breath caught short. The breath he was drawing seemed to stiffen in his chest. He felt as if the whole world had started spinning inside the room.",
   [("breath_heavy", "ނޭވާ", -20)], hum=True)
sh(17, "What could be seen on the screen was the owner of the memories that the whole island, twenty years ago, had concluded was dead after he suddenly vanished from this island, and had shrouded and buried.",
   hum=True)
sh(18, "It was Ibrahim Naseem! On his face was a deep pain and a fear, of a kind a human being feels.",
   [("heartbeat", "އިބްރާހީމް", -20)], hum=True)
sh(19, "His two eyes were staring straight into the camera's lens. Were those the eyes of a living human? Or a shadow risen from the desert of the past?",
   hum=True)
sh(20, "The bulb in Shahid's room suddenly dimmed and flickered. Behind him came the sound of someone knocking slowly on the room's door.",
   [("bulb_flicker", "ދިއްލުނު", -18), ("knock", "ޓަކިޖަހާލި", -14)], hum=True)
sh(21, "Perhaps it was because of the fear Shahid had taken. The knock at the door sounded to him like a thunderclap. Suddenly he started with a jolt.",
   [("thunder", "ހޮނުގުގުރީގެ", -22), ("gasp", "ސިއްސައިގެން", -18)])
sh(22, "With the sound of that slow knocking that burst the silent atmosphere of the room, goose-bumps rose all over Shahid's body.",
   [("knock", "ޓަކީގެ", -16)], hum=True)
sh(23, "Ibrahim Naseem's frightening eyes on the computer screen and the sound heard from the room's door — a chain of fear began to spin in his mind.",
   hum=True)
sh(24, "At the sound of the room's window banging hard with a strong wind that struck through the pouring rain, he started and put his hand to his chest.",
   [("wind_gust", "ވަޔާއެކު", -16), ("soft_thud", "ޖެހިގަތް", -14), ("gasp", "ސިއްސައިގެން", -20)])
sh(25, "Shahid slowly got up and began to step towards the door. The soles of his feet felt as if they had gone numb.",
   [("footsteps_pavement", "ފިޔަވަޅު", -22)], hum=True)
sh(26, "When he put his hand on the door's lock, his hand was shaking beyond his own control. Slowly turning the lock, he opened the door.",
   [("lock_click", "އަނބުރާލައި", -18), ("door_open", "ހުޅުވާލި", -18)])
sh(27, "Outside stood his old mother. On mother's face was the look of worry. \"What happened, my child?\"", speaker="shahid_mother")
sh(28, "\"I came because I heard something fall inside the room.\" Mother's soft, gentle voice eased Shahid's anxiety a little.", speaker="shahid_mother")
sh(29, "But the trembling of his heart had still not settled. Forcing a smile, Shahid said the coffee mug had tipped over and sent his mother away.",
   speaker="shahid", crop="medium")
sh(30, "After shutting and locking the door, Shahid came back, sat down at the computer and looked deeply at that photo.",
   [("door_close", "ލައްޕައި", -18), ("lock_click", "ތަޅުލުމަށްފަހު", -20)])
sh(31, "The pages of the past from twenty years ago began to come alive in his memory. Back then Shahid was a small child.")
sh(32, "But the memories of that frightening night have never faded from the hearts of the whole island. It was the night someone was found murdered near the island's club warehouse.",
   hum=True)
sh(33, "The one who had died was an influential businessman of the island. On the night it happened, the last person seen in that area was Ibrahim Naseem.",
   hum=True)
sh(34, "After that he vanished without a living trace. The police and the islanders searched the whole island. They dived the uninhabited islands and the reefs.",
   [("splash", "ފީނި", -22)])
sh(35, "But with no news at all, everyone concluded that Ibrahim Naseem had drowned in the sea or died some other way.")
sh(36, "The heavy suspicion for that murder fell on Ibrahim's head. \"But he is alive!\" Shahid said to himself.",
   speaker="shahid", hum=True)
sh(37, "The living proof that Ibrahim Naseem had not died lay in front of him. Shahid enlarged the photo further and began to look carefully at the surroundings where Ibrahim stood.",
   [("keyboard_typing", "ބޮޑުކޮށް", -24)])
sh(38, "What caught his eye was a piece of iron, shaped in an unusual way, lying at Ibrahim's feet.")
sh(39, "And part of an old, decaying, crumbling wall visible behind him. That was not a wall of the lighthouse. It was a view from another part of the island.")
sh(40, "The nerves in Shahid's head tightened. He began to sense the depth of this secret. The secret of a man who had been hiding, deceiving the whole island for twenty years, lay in his hands.",
   hum=True)
sh(41, "This is no ordinary matter. This is something dangerous. He decided to take this photo to the police station first thing tomorrow morning.")
sh(42, "But what Shahid does not know is that the road he is about to take is a road that will throw his life into a dark pit.",
   hum=True)
sh(43, "And if he knew who lies at the bottom of the case he is about to hand over, he would delete that photo at once!",
   [("thunder", "ފޮހެލީސް", -20)], hum=True)
sh(44, "In Shahid's heart was the wish to share with the police that Ibrahim Naseem, a son of the island who had vanished from it, is alive. Lying in those thoughts, Shahid fell asleep.",
   [("sigh", "ނިދިއްޖެ", -24)])
sh(45, "The police's decision. The golden rays of morning lit up the whole island, but the dark shadow that had taken hold of Shahid's heart did not change at all.")
sh(46, "Though the night's uneasy chill left his body, what kept spinning in his mind were those deep, frightening eyes of Ibrahim Naseem seen on the computer screen.",
   hum=True)
sh(47, "Getting ready in a hurry, with the memory card holding the secret photos in his pocket, he left the house towards the police station.",
   [("footsteps_sand", "ނިކުތީ", -20)])
sh(48, "He found himself looking at the face of every person he saw on the road with suspicion. Is every figure Ibrahim in a changed disguise, kept coming to his mind.",
   [("footsteps_sand", "މަގުމަތީން", -24)])
sh(49, "Inside a cold room of the police station, Shahid sat waiting for the chief officer.")
sh(50, "Suddenly the room's door opened and in came the island's highest police officer, the steadfast officer Amjad, who has earned immense respect and trust among the people.",
   [("door_open", "ހުޅުވައިލައިފައި", -16), ("footsteps_pavement", "އެތެރެއަށް", -22)])
sh(51, "Looking at Shahid with his vigilant, sharp eyes, he sat down on the chair. Shahid. He seems somewhat anxious.",
   [("creak", "ގޮނޑީގައި", -22)])
sh(52, "\"What big matter is it that you're bringing?\" In Amjad's voice was authority and calm.", speaker="amjad")
sh(53, "Without saying a word, Shahid took the memory card out of his pocket and laid it on the table. Then, putting the card into Amjad's laptop, he opened the photo he had zoomed into last night.",
   [("cloth_rustle", "ޖީބުން", -24), ("keyboard_typing", "ހުޅުވާލި", -22)])
sh(54, "\"Please look at this photo carefully... This is a photo I took last night near the lighthouse.\" There was a tremor in Shahid's voice.",
   speaker="shahid")
sh(55, "Amjad leaned forward and fixed his gaze on the screen. As the figure at the back of the photo enlarged and its face began to clear, the colour of Amjad's face suddenly changed!",
   [("heartbeat", "ބަދަލުވެގެންދިޔަ", -22)], hum=True)
sh(56, "His breath grew short, and his hand gripped the pen lying on the table hard. What showed on that face was not surprise.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
sh(57, "It was the secret colour of a fear that had suddenly entered the heart. But very quickly Amjad controlled himself and narrowed his eyes as if it were nothing.",
   hum=True)
sh(58, "\"This... this is Ibrahim Naseem! The man who went missing twenty years ago.\"", speaker="amjad", crop="medium")
sh(59, "Amjad said it barely loud enough to hear. As if a heavy memory of the past had woken in the depths of his heart. \"Yes, officer! He is not dead.\"",
   crop="tight")
sh(60, "\"He is living on the island as a living man. This is a great danger to the whole island,\" Shahid said with passion.", speaker="shahid")
sh(61, "Amjad got up from the table and stood staring out of the room's window.",
   [("creak", "ތެދުވެ", -22)], hum=True)
SHOTS = S

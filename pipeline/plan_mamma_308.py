"""Beat/shot plan for Mamma episode 308 (pilot) (used by plan_beats.py)."""

LOC = {
    "storm_sea": "the open Indian Ocean at night just off a small Maldivian local island: huge dark rolling waves with white foam crests, the dark line of the island's palms on the horizon, a few tiny amber lights of the island harbour, black storm clouds filling the whole sky, no moon, no stars",
    "harbour_night": "the small harbour of a Maldivian local island at night: a long stone jetty (faalan) with a few lamp posts casting warm amber pools of light, a wooden passenger dhoni with a white-and-blue hull and a small wheelhouse rocking in choppy black water beside the jetty, palm trees and low island buildings behind",
    "jetty_night": "the landward end of the island's stone jetty at night, a lamp post glowing amber above, wet stones reflecting the light, the wide white sandy main road (bodumagu) of the island stretching inland between palms and low coral-stone walls, a few weak streetlamps fading into the darkness",
    "main_road_night": "the wide white sandy main road (bodumagu) of a small Maldivian island at night, low white coral-stone walls and tall palms on both sides, a few streetlamps casting warm amber pools of light on the wet sand, puddles reflecting the lamps, nobody else around",
    "mosque_front_night": "the island's old mosque at night seen from the sandy road: white-washed coral-stone walls, a low pitched corrugated roof, a wide covered front porch with low white wall-benches and square white pillars, a single warm amber lamp glowing under the porch roof, a sandy yard, palms bending in the wind",
    "mosque_porch_night": "under the wide covered front porch of the island's old white mosque at night: square white pillars, a low white wall-bench along the edge, a smooth tiled porch floor wet near the edge, a single warm amber lamp on the wall, sheets of rain pouring off the edge of the roof into the dark sandy yard",
    "cemetery_view_night": "the view from the edge of the old mosque's covered porch at night: just beside the mosque the small island cemetery — a sandy yard of plain small white-washed coral headstones without any writing under dark frangipani trees — now enclosed by a new low white wall, all under pouring rain, lit only by the porch lamp and flashes of lightning",
    "memory_island_day": "a neighbour's sunny sandy back yard on the small home island, years ago: a coral-stone wall, a washing line with colourful clothes between two palms, a plastic washing basin, a low wooden step at a kitchen door, soft breadfruit-tree shade",
    "khadheeja_room_day": "the small front room of Khadheeja's modest old coral-stone island house on a rainy day: bare whitewashed walls, a woven mat on the floor, a wooden window with its shutter half open onto grey rain, a few women relatives seated on the mat along the wall",
    "khadheeja_door_day": "the open wooden front door of Khadheeja's small coral-stone island house on a rainy day, seen from inside: the doorway frames the white sandy lane outside under grey pouring rain, palms and coral-stone walls beyond",
    "lane_rain_day": "a white sandy lane of the island in heavy daytime rain, low coral-stone walls and palms on both sides, the sand dark and full of puddles, grey sky, the white wall of the old mosque visible far ahead",
    "cemetery_rain_day": "the small island cemetery beside the old white mosque on a grey rainy day: a sandy yard of plain small white-washed coral headstones without any writing under frangipani trees with fallen white flowers, enclosed by a low white coral wall, heavy rain",
    "memory_glow": "a soft, dreamlike memory space glowing with warm golden haze and floating light particles, a hint of island palms and a coral-stone wall dissolved into soft light",
    "zubair_room_night": "Shahula's small bare bedroom in Zubair's old coral-stone island house at night: whitewashed walls, a narrow wooden bed with a thin pillow, a closed wooden window with rain on the panes, a small kerosene-style lamp on a stool giving warm amber light, a metal basin of water on the floor",
    "open_sea_day": "the open sea far away from the atoll on a grey stormy day: a wooden Maldivian fishing dhoni with a small wheelhouse drifting on rough grey-green waves, low dark rain clouds, spray in the air, no land in sight",
    "island_road_morning": "the white sandy main road of the island in the early morning after the storm: puddles on the sand, palms and coral-stone walls, soft hazy golden light, the harbour and a moored fishing dhoni small in the background",
    "zubair_yard_morning": "the sandy yard of Zubair's old coral-stone island house in the morning: an outdoor kitchen area under a corrugated roof, a low wooden table, a big wooden tray, a wooden joali seat, a plastic water barrel, a towel hanging on a line, the open dark doorway of the house, palms",
    "zubair_doorway_morning": "the open dark wooden doorway of Zubair's old coral-stone island house seen from the sandy yard in the morning, the dim interior behind, soft hazy morning light on the coral-stone wall",
}
MOOD = {
    "storm_sea": "storm night, black sky with no moon, a jagged flash of lightning lighting the clouds, howling wind and spray, ominous, grief-heavy",
    "harbour_night": "storm night, black sky, heavy clouds, wind-whipped water, warm amber lamps on the jetty, the first raindrops, tense and hurried",
    "jetty_night": "storm night, black sky, warm amber lamplight, fine rain starting to fall in the lamp glow, lost, lonely and anxious",
    "main_road_night": "storm night, heavy rain slanting in the amber streetlamp light, a white flash of lightning in the black sky, frightened and alone",
    "mosque_front_night": "storm night, heavy rain, black sky, the porch lamp a warm amber refuge in the darkness, urgent relief",
    "mosque_porch_night": "storm night, black sky, heavy rain curtains lit amber by the single porch lamp, cold blue shadows, weary, lonely and fragile",
    "cemetery_view_night": "storm night, black sky, a flash of lightning silvering the white headstones, heavy rain, warm amber porch light at the edge of the frame, deep grief",
    "memory_island_day": "memory: soft warm hazy glow, gentle golden tropical daylight, slightly desaturated, tender and nostalgic",
    "khadheeja_room_day": "memory of a grey rainy day: dim cool daylight through the window, soft warm haze at the edges, hushed, heartbroken",
    "khadheeja_door_day": "memory of a grey rainy day, cold grey light outside, dim interior, heavy rain, desperate grief",
    "lane_rain_day": "memory of a grey rainy day, heavy rain, cold grey light, a small lonely figure, urgent sorrow",
    "cemetery_rain_day": "memory of a grey rainy day, heavy rain, muted greys and greens, soft haze, silent overwhelming grief",
    "memory_glow": "memory: soft warm hazy golden glow, dreamlike vignette, tender, loving and sorrowful",
    "zubair_room_night": "night, a single warm amber lamp, deep shadows, rain on the window, anxious and caring",
    "open_sea_day": "grey stormy daylight far out at sea, cold muted blues and greys, rough and stranded",
    "island_road_morning": "early morning after the storm, soft hazy tropical light, wet sand glistening, quiet and cold-hearted",
    "zubair_yard_morning": "morning, soft hazy tropical light and cool shade under the roof, tense and hurtful",
    "zubair_doorway_morning": "morning, soft hazy light outside and a dim doorway, fragile and heartbreaking",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
SH = ("Shahula (reference used for her face only) wearing a loose long-sleeved ankle-length black abaya and a black hijab "
      "with a white under-scarf showing at the forehead, fully covering her hair and neck, NOT the dusty-rose dress and "
      "NOT the cream hijab")
BABY = ("her baby son Zidhaan, a healthy few-months-old baby in a pale-blue long-sleeved baby suit wrapped in a pale-blue "
        "cotton blanket, asleep with his head on her shoulder")
KID = "12-year-old Shahula in her faded pink long-sleeved ankle-length dress and white headscarf fully covering her hair and neck"
BODU = ("an elderly island woman (the eldest aunt) in a dark-brown long-sleeved ankle-length libaas dress and a dark headscarf "
        "fully covering her hair and neck")

BEATS = [
    # ---------------- PRESENT: STORM NIGHT ARRIVAL
    dict(to=2, reason="episode opening: the black storm night over the sea, waves rising",
         loc="storm_sea",
         visual="black storm clouds swallowing the whole night sky, no moon and no stars, a jagged lightning bolt far away "
                "lighting the cloud edges, huge dark waves with white foam crests rolling towards the dark low island on the "
                "horizon with a few tiny amber harbour lights; no people",
         camera="wide establishing shot, the sky and the island horizon in the upper two-thirds, dark rolling water as a calm lower third",
         amb="storm_night"),
    dict(to=4, reason="scene change: a passenger dhoni battles into the harbour and comes alongside the jetty; passengers hurry off",
         loc="harbour_night",
         visual="a wooden passenger dhoni tilting in the choppy black water as it comes alongside the stone jetty, spray on "
                "its bow; small figures of passengers in raincoats and headscarves hurrying from the deck onto the jetty with "
                "bags, seen from a distance in the amber jetty lamps; the first raindrops slanting in the wind",
         camera=f"wide shot from the end of the jetty, slightly high, the dhoni and lamps in the upper two-thirds, {LOW} (wet jetty stones)",
         amb="storm_night"),
    dict(to=6, reason="character focus: Shahula steps off with her sleeping baby and a bag and stands lost, looking up the main road",
         chars=["shahula"], loc="jetty_night",
         visual=f"{SH}, standing alone at the end of the stone jetty under a glowing lamp post, {BABY}, a travel bag in her "
                f"other hand, looking up the dark sandy main road with an anxious, bewildered face; fine rain beginning to "
                f"fall in the lamp glow; seen three-quarter from the front",
         camera=f"medium wide shot, eye level, {LOW} (wet jetty stones reflecting the lamp)", amb="storm_night"),
    dict(to=9, reason="action change: she walks up the main road; lightning and thunder make her flinch, the rain pours",
         chars=["shahula"], loc="main_road_night",
         visual=f"{SH}, walking up the wide sandy main road in slanting heavy rain, {BABY}, her bag in her other hand; she "
                f"has stopped mid-step and flinched, shoulders drawn up, looking up fearfully at a white flash of lightning "
                f"in the black sky; her abaya soaked; she shields the baby's head with her cheek",
         camera=f"medium wide shot, eye level, {LOW} (wet sand with puddles reflecting the lamps)", amb="storm_night"),
    dict(to=11, reason="scene change: the island mosque ahead; she hurries into the shelter of its porch",
         chars=["shahula"], loc="mosque_front_night",
         visual=f"the old white island mosque with its lamp-lit covered porch glowing amber ahead in the storm; {SH}, small "
                f"in the frame, hurrying across the sandy yard towards the porch steps in the pouring rain, {BABY}, bag in "
                f"hand; seen from behind and to the side",
         camera=f"wide shot, eye level, the mosque in the upper two-thirds, {LOW} (wet sandy yard with puddles)", amb="storm_night"),
    dict(to=14, reason="action change: under the porch she sets the bag down and shifts the baby to her other arm, murmuring to herself",
         chars=["shahula"], loc="mosque_porch_night",
         visual=f"{SH}, standing under the mosque porch beside a white pillar, soaked and weary, her travel bag set down on "
                f"the low wall-bench beside her; she is shifting her sleeping baby Zidhaan (a healthy few-months-old baby in "
                f"a pale-blue baby suit wrapped in a pale-blue blanket) from one tired arm to the other, cradling him to her "
                f"shoulder, looking out at the rain with a tired, worried face, lips slightly parted as if murmuring",
         camera=f"medium shot, eye level, {LOW} (the wet tiled porch floor)", amb="rain_night"),
    dict(to=19, reason="framing change: she looks out into the storm, lightning and thunder, holds Zidhaan tighter; tears and memories rise",
         chars=["shahula"], loc="mosque_porch_night",
         visual=f"{SH}, standing at the edge of the porch beside a white pillar, cradling her sleeping baby Zidhaan (a healthy "
                f"few-months-old baby in a pale-blue baby suit wrapped in a pale-blue blanket) on her shoulder with both arms, "
                f"gazing out into the dark storm with weary, sorrowful, glistening eyes; a white flash of lightning lights the "
                f"rain curtain pouring off the porch roof behind her",
         camera=f"medium shot, eye level, {LOW} (the wet tiled porch floor and her black abaya in soft shadow)",
         amb="storm_night"),
    # ---------------- MEMORY: KHADHEEJA
    dict(to=22, reason="flashback: Khadheeja, the brave single mother who worked in island houses to pay for Shahula's schooling",
         chars=["khadheeja", "shahula_child"], loc="memory_island_day", transition="dissolve",
         visual=f"memory: Khadheeja in her faded green libaas and white headscarf hanging washed clothes on a line in a "
                f"neighbour's sunny yard, turning with a tired but loving smile towards {KID}, who sits on a low wooden step "
                f"nearby with an open school exercise book on her knees (blank pages, no writing), smiling up at her mother",
         camera=f"medium wide shot, eye level, {LOW} (sunny sand of the yard)", amb="memory"),
    # ---------------- PRESENT: THE CEMETERY
    dict(to=25, reason="scene change back to the present: her gaze falls on the walled cemetery beside the mosque; 'Mamma'",
         chars=["shahula"], loc="cemetery_view_night", transition="dissolve",
         visual=f"{SH}, seen from behind and slightly to the side at the edge of the mosque porch, {BABY}, her head bowed "
                f"slightly, looking out at the small cemetery beside the mosque with its new low white wall and plain white "
                f"headstones under frangipani trees in the pouring rain, lit silver by a flash of lightning",
         camera=f"medium wide over-the-shoulder shot, eye level, the cemetery in the upper two-thirds, {LOW} (wet porch floor)",
         amb="storm_night", sens="death", safe="her mother's resting place shown only as the walled cemetery in the rain"),
    # ---------------- MEMORY: THE DAY OF THE MOTHER'S PASSING (age 12)
    dict(to=29, reason="deep flashback: 12-year-old Shahula takes a last look at her mother's face and breaks into sobs",
         chars=["shahula_child"], loc="khadheeja_room_day", transition="dissolve",
         visual=f"{KID}, sitting on her knees on the woven mat in the dim front room, her head bowed, her big dark eyes "
                f"glistening and sad, both hands folded together at her chest; behind her, island women relatives in long "
                f"dresses and headscarves sit quietly along the wall with lowered heads; grey rainy light from the window",
         camera=f"medium shot, eye level, facing her, {LOW} (the woven mat in soft shadow)", amb="rain_day",
         sens="death", safe="her mother is never shown: only the child's tearful face looking down at something off-frame"),
    dict(to=33, reason="character enters: Faathanikey draws her aside and tells her to be patient; she cannot stop crying",
         chars=["faathanikey", "shahula_child"], loc="khadheeja_room_day",
         visual=f"Faathanikey in her maroon libaas and white headscarf standing beside {KID} near the wall of the dim room, "
                f"one hand resting gently on the girl's shoulder, bending to speak softly with worried, kind eyes; the girl "
                f"stands with her head bowed, tears running down her cheeks, wiping her eyes with the back of her hand",
         camera=f"medium shot, eye level, {LOW} (the woven mat on the floor)", amb="rain_day",
         sens="death", safe="the covering of the mother's face is not shown; only Faathanikey consoling the girl"),
    dict(to=36, reason="action change: the bier is carried out; the eldest aunt stops Shahula at the door; she begs to go with her mother",
         chars=["shahula_child"], loc="khadheeja_door_day",
         visual=f"in the open front doorway, {BODU} stands blocking the way with one arm stretched across the door frame, "
                f"stern; facing her, {KID} with her hands clasped in pleading, tears on her face; beyond them, through the "
                f"doorway, far away down the rainy sandy lane, a small group of men in white shirts and sarongs carrying a "
                f"white-shrouded bier on their shoulders away into the grey rain, seen only from behind and very small",
         camera=f"medium wide shot from inside the room, eye level, {LOW} (the doorstep and wet floor)", amb="rain_day",
         sens="death", safe="the white-shrouded bier only tiny and far away from behind; the aunt bars the door with her arm on the frame, nobody is pulled or held",
         hum=True),
    dict(to=38, reason="action/scene change: she slips out of the room and runs through the heavy rain to the cemetery",
         chars=["shahula_child"], loc="lane_rain_day",
         visual=f"{KID}, running alone along the empty sandy lane through heavy rain towards the white wall of the mosque far "
                f"ahead, her pink dress and white headscarf soaked, seen from behind and slightly to the side, splashes of "
                f"rain on the puddles",
         camera=f"medium wide shot, eye level, {LOW} (puddled wet sand)", amb="rain_day"),
    dict(to=40, reason="scene change: from beside the cemetery wall she watches her mother being laid to rest",
         chars=["shahula_child"], loc="cemetery_rain_day",
         visual=f"{KID}, standing just inside the low white cemetery wall in the heavy rain, seen from behind and to the "
                f"side, one hand on the wall, watching; far off across the cemetery a group of men in white shirts and "
                f"sarongs stand in a quiet circle with their backs to the camera and heads bowed under the frangipani trees",
         camera=f"medium wide shot, eye level, {LOW} (wet sand and fallen frangipani flowers)", amb="memory_rain",
         sens="death", safe="the burial is shown only as mourners' bowed backs far away; nothing of the bier or the ground work is visible",
         hum=True),
    dict(to=42, reason="action change: alone after everyone has left, she kneels by her mother's resting place, head bowed to the sand",
         chars=["shahula_child"], loc="cemetery_rain_day",
         visual=f"{KID}, seen from the side at a little distance, sitting on her knees on the wet sand in the rain beside a "
                f"small low mound of white sand marked with a plain white coral stone and a few white frangipani flowers, her "
                f"head bowed, her hands resting in her lap; frangipani trees and the low white wall around her, nobody else there",
         camera=f"medium shot, slightly high angle, the girl and the headstone in the upper two-thirds, {LOW} (wet sand)",
         amb="memory_rain", sens="death", safe="only the fresh sand mound and a plain white headstone; the child kneels with dignity, head bowed",
         hum=True),
    dict(to=46, reason="memory: her mother's loving voice comes to her ear with her last advice",
         chars=["khadheeja"], loc="memory_glow", transition="dissolve",
         visual="memory: close-up of Khadheeja in her faded green libaas and white headscarf, her thin gentle face softly "
                "glowing in warm golden haze, looking straight at the viewer with tender, tear-bright loving eyes and a faint "
                "smile, as if giving her daughter a last gentle piece of advice",
         camera=f"close-up, eye level, {LOW} (soft golden haze)", amb="memory"),
    dict(to=48, reason="time jump: that night Shahula burns with fever; Faathanikey keeps changing the wet cloths",
         chars=["shahula_child", "faathanikey"], loc="zubair_room_night", transition="black",
         visual=f"{KID}, sitting propped up on a pillow against the head of her narrow bed under a thin faded blanket up to "
                f"her chest, eyes half closed, cheeks flushed with fever, lips murmuring; Faathanikey in her maroon libaas and "
                f"white headscarf sitting on the edge of the bed pressing a folded wet white cloth to the girl's forehead with "
                f"a frightened, worried face; a metal basin of water on the stool beside the lamp",
         camera=f"medium shot, eye level, {LOW} (the blanket and the floor in shadow)", amb="room_night",
         sens="other", safe="fever shown with the girl sitting up propped on a pillow, fully dressed with headscarf, a cool cloth on her forehead"),
    dict(to=52, reason="scene change: Zubair, her uncle, a fisherman stranded far away at sea by engine trouble",
         chars=["zubair"], loc="open_sea_day",
         visual="Zubair in his faded blue checked shirt, dark sarong and a faded cap, standing on the deck of a drifting "
                "fishing dhoni on rough grey waves, one hand on the wheelhouse, looking at the empty horizon with a stern, "
                "impatient frown; the engine hatch open beside him",
         camera=f"medium wide shot, eye level, the man and the horizon in the upper two-thirds, {LOW} (wooden deck)",
         amb="sea_boat"),
    # ---------------- NEXT MORNING: ZUBAIR RETURNS
    dict(to=54, reason="time jump: next morning his dhoni returns; Zubair walks home with his share of fish, no grief on his face",
         chars=["zubair"], loc="island_road_morning", transition="black",
         visual="Zubair in his faded blue checked shirt and dark sarong, walking up the wet sandy road in the soft morning "
                "light carrying a string of three whole silver tuna fish in one hand, his face blank and hard with no sign of "
                "grief; a fishing dhoni moored in the harbour behind him",
         camera=f"medium shot, eye level, {LOW} (wet sand with puddles)", amb="village_day"),
    dict(to=58, reason="scene/character change: in the yard he lays the fish on a tray; Faathanikey comes with a water pot and asks about Shahula's fever",
         chars=["faathanikey", "zubair"], loc="zubair_yard_morning",
         visual="Zubair sitting on a low stool at the low wooden table in the yard, three whole silver tuna fish lying on a "
                "big wooden tray in front of him, his hands resting flat on the edge of the tray, not looking up, his face "
                "cold; Faathanikey in her maroon libaas and white headscarf standing a few steps away with a metal water pot "
                "(bandiyaa) on her hip, speaking to him with a very worried face",
         camera=f"medium wide shot, eye level, {LOW} (the tray and the sandy ground)", amb="island_house_day",
         sens="other", safe="whole fish on a tray only; nothing in his hands, no cutting shown"),
    dict(to=62, reason="framing change: Zubair snaps at her with his hard, cruel answer",
         chars=["zubair"], loc="zubair_yard_morning",
         visual="close-up of Zubair seated at the fish tray, his weathered face tight with irritation, brows drawn down, "
                "glaring sideways at someone off-frame as he speaks sharply, the edge of the tray and a whole fish visible "
                "below; nothing in his hands",
         camera=f"close-up, eye level, {LOW} (the wooden tray edge in soft focus)", amb="island_house_day",
         sens="other", safe="harsh words shown only as a stern face"),
    dict(to=64, reason="character change: Faathanikey, stunned and disappointed, reminds him it was his own sister",
         chars=["faathanikey"], loc="zubair_yard_morning",
         visual="medium close-up of Faathanikey in her maroon libaas and white headscarf, standing in the yard with the "
                "water pot set down at her feet, one hand on her chest, her round kind face full of astonishment and hurt, "
                "eyes wide and wet, speaking pleadingly towards someone off-frame",
         camera=f"medium close-up, eye level, {LOW} (sandy ground in soft shadow)", amb="island_house_day"),
    dict(to=66, reason="back to Zubair's hard face: 'better if she had taken her along!'", reuse="beat_021",
         chars=["zubair"], loc="zubair_yard_morning", visual="reuse of beat_021", amb="island_house_day"),
    dict(to=68, reason="back to Faathanikey's shock as he stands and rinses his hands; can this be the kind man she knew?",
         reuse="beat_022", chars=["faathanikey"], loc="zubair_yard_morning", visual="reuse of beat_022", amb="island_house_day"),
    dict(to=70, reason="action change: Zubair walks inside with the towel; Faathanikey, in tears, sits down to finish the fish",
         chars=["faathanikey", "zubair"], loc="zubair_yard_morning",
         visual="Faathanikey sitting on the low stool at the wooden tray of whole fish, shoulders slumped, eyes full of "
                "tears, looking down at the fish lost in thought, her hands resting on her knees; in the background Zubair "
                "with a towel over his shoulder walking away into the dark doorway of the house, his back turned",
         camera=f"medium wide shot, eye level, {LOW} (the tray and the sandy ground)", amb="island_house_day",
         sens="other", safe="whole fish on a tray only; nothing in her hands"),
    dict(to=73, reason="character/emotional turn: she sees Shahula in the doorway, wrapped in a blanket, shivering, in tears — she heard everything",
         chars=["shahula_child"], loc="zubair_doorway_morning",
         visual=f"{KID}, standing in the dark open doorway of the house, wrapped in a faded checked blanket over her pink "
                f"dress and white headscarf, shivering with fever, clutching the blanket at her chest with both hands, "
                f"silent tears streaming from her big dark eyes, lips pressed together trembling, looking out towards the yard",
         camera=f"medium shot, eye level, {LOW} (the doorstep and the sandy ground)", amb="island_house_day",
         sens="other", safe="the feverish, heartbroken child shown with dignity, standing wrapped in a blanket", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Black heavy clouds had wrapped the whole sky. The moon's silver light had faded, the stars' glitter was lost, and darkness ruled the whole universe.")
sh(2, "It seemed as if the whole world had wrapped itself in a black shawl of grief. The wind grew strong and the waves of the sea rose roaring.",
   [("wind_gust", "ބާރުވެ", -20), ("wave_crash", "ރާޅުތައް", -20)])
sh(3, "A dhoni that had come struggling to stay safe under the crests of the waves entered the island's harbour at that moment and, rocking from side to side, came alongside the jetty.",
   [("dhoni_engine", "ދޯންޏެއް", -18)])
sh(4, "Before the heavy rain poured down, the passengers on the dhoni quickly began to get off onto the jetty.",
   [("footsteps_pavement", "ފައިބަން", -22)])
sh(5, "Shahula too got off the dhoni holding her little child to her chest. And after looking around her surroundings with worry and bewilderment,")
sh(6, "not knowing of any place to go, she stood looking towards the island's main road. At that moment a fine rain began to fall.",
   [("rain_start", "ވެހެން", -18)])
sh(7, "Shahula let out a deep breath, settled the child sleeping on her shoulder, took the bag in her hand and started walking towards the main road.",
   [("sigh", "ނޭވާއެއް", -22), ("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(8, "At the loud crack of thunder that came with the flash of lightning, Shahula flinched. Her steps stopped, and she looked around in fear.",
   [("thunder", "ގުގުރައިގަތް", -14), ("gasp", "ސިއްސައިގެންނެވެ", -22)])
sh(9, "In an instant the raindrops grew heavy and the rain poured enough to soak her through. For the safety of the tiny child she held to her chest, her heart hurried to find some shelter.")
sh(10, "At that moment, the island's mosque could be seen in front of her. Letting out a deep breath, she gathered her courage and, walking fast, went into the mosque.",
   [("footsteps_sand", "ހިނގުމެއްގައި", -22)])
sh(11, "With that shelter, Shahula's heart found a little calm. \"What a stormy night!\" Shahula thought.")
sh(12, "Setting the bag in her hand down to one side, she moved the little child from her tired arm to the other arm.",
   [("cloth_rustle", "ބެހެއްޓުމަށްފަހު", -22)])
sh(13, "\"When will this downpour ever stop?\" she murmured softly to herself.")
sh(14, "\"In rain this heavy, how will I even take Zidhaan anywhere?\" With eyes heavy with sleep,")
sh(15, "she looked towards the mosque's gate. The sky was still dark, and the heavy rain kept pouring without a pause. The strong flashes of lightning")
sh(16, "and the rumbling roar of thunder filled the whole surroundings with fear. With that, waves of fear surrounded Shahula's heart.",
   [("thunder", "ގުގުރީގެ", -16), ("heartbeat", "ބިރުވެރިކަމުގެ", -22)])
sh(17, "She held Zidhaan's tiny body, deep in sleep, even more tightly. \"Subhanallah!\" With the helplessness that filled her heart, the words slipped from Shahula's lips without her meaning to.",
   [("breath", "ބައްދާލިއެވެ", -22)])
sh(18, "Every time loneliness takes over her heart, her eyes, full of tears, close. However much she wants to erase the memories,")
sh(19, "the pages of the past open before her eyes without her having any choice. And she is forced to read every one of those pages.")
sh(20, "Shahula was one of the most noticeably pretty girls of the island. Without any help from a father, Shahula was raised by her brave, lonely mother Khadheeja.")
sh(21, "Khadheeja worked going from house to house on the island doing all kinds of work, to give Shahula the highest education the island could offer.")
sh(22, "But that mother's love and care lasted only a few short days. That mother said her farewell to this passing world forever on just such a stormy night.")
sh(23, "However much she wanted to get away from those painful memories, it could not be done. Her gaze stopped at the cemetery not far from the mosque.")
sh(24, "Now there is even a wall built all around it. Taking two or three steps forward with her child, her gaze settled on the whole cemetery.",
   [("footsteps_pavement", "ފިޔަވަޅެއް", -24)])
sh(25, "With that, her eyes, brimming with tears, closed. The only word that left her lips was \"Mamma\".",
   [("sob_breath", "މަންމާ", -22)], hum=True)
sh(26, "In a moment she sank into the deep memories of the past. Shahula, only twelve years old,")
sh(27, "cast her gaze on her loving mother's face for the very last time. With eyes reddened from crying and full of tears, she kept looking at her mother's face,")
sh(28, "with the noble purpose of laying that beloved image forever in the very depths of her heart. \"Mamma!\"", hum=True)
sh(29, "As this word left Shahula's lips, she broke into heartbreaking sobs.",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -20)], hum=True)
sh(30, "Faathanikey, who was standing nearby, took Shahula by the hand, moved her to one side and told her not to cry but to be patient. But")
sh(31, "today she had no strength to listen to a single one of those words. Her tears kept falling without stopping.")
sh(32, "As the shroud was taken from Shahula's hand to cover her mother's face, people moved her away once again.")
sh(33, "After that she never got another chance to see her mother's beloved face. In less time than it takes to speak a word,")
sh(34, "they began to carry her mother's bier out of the house. Shahula too walked quickly after them, to go with her mother. But",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(35, "the eldest aunt came and forcefully stopped her, forbidding her to go. \"I want to go with Mamma. I'm begging you, let me go to my Mamma!\"",
   hum=True)
sh(36, "Sobbing and crying, Shahula kept pleading. But at that moment they turned a deaf ear. Her pleas touched not a single one of those hearts.",
   [("sob_breath", "ގިސްލާ", -22)])
sh(37, "Though she was taken into a room, Shahula got out of it and ran towards the cemetery. And because the others did not notice her leaving,",
   [("door_open", "ނުކުމެގެން", -22), ("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(38, "she gave praise and thanks to Allah. Through the heavily pouring rain she ran and went into the cemetery surrounded by a low wall.",
   [("footsteps_sand", "ދުވެފައި", -22)])
sh(39, "At that time her beloved mother's bier had been lowered into the grave and sand was being poured to cover it. With a feeling as if the whole world had come to a stop,",
   hum=True)
sh(40, "she stood watching that scene, sobbing and sobbing in heartbreaking grief. When the funeral rites were over and everyone had left the place,",
   [("sob_breath", "ގިސްލަގިސްލާފައި", -22)], hum=True)
sh(41, "full of tears, she went and sat down beside her mother's grave. And with sobs full of grief,")
sh(42, "she laid her head on the sand where her mother was buried. Her mother's moving voice echoed by her ear as if she were giving some last advice.",
   hum=True)
sh(43, "\"My child! Light of Mamma's two eyes! Even though Mamma has left this world, don't let your education go dark!", hum=True)
sh(44, "That Mamma's beloved child, bound to the beat of her heart, becomes a great person full of knowledge and skill is Mamma's greatest hope,")
sh(45, "success in this world and the hereafter for you, my beloved child, dear to Mamma as her own soul! Even on the days when Mamma is no longer in this world, stay firm on good character,")
sh(46, "be an obedient child; you are Mamma's whole life.\" Even while her body burned hot with fever,")
sh(47, "what her lips kept repeating was her beloved mother's name. Though Faathanikey kept changing the wet cloths on Shahula's forehead without a pause, the heat of the fever did not change at all.")
sh(48, "With that, Faathanikey's fear and worry grew beyond measure. Thinking of what would happen if Zubair learned that Shahula had secretly gone to the cemetery,")
sh(49, "and of the hard things they would have to face then. Since Zubair, Shahula's mother Khadheeja's full brother, was a fisherman,")
sh(50, "once he set out fishing he did not come back to the island quickly. When the news of Khadheeja's passing was sent, he was very far from the atoll. And though he had set out for the island,")
sh(51, "because of a problem with the dhoni's engine the trip was delayed, and even now the dhoni had not reached the island.",
   [("dhoni_engine", "އިންޖީނަށް", -22)])
sh(52, "Since it is not desirable to keep the deceased waiting long, following the advice of the island's imam, Khadheeja's funeral rites were completed and she was buried.")
sh(53, "It was the morning of the next day. The dhoni Zubair had sailed on came back to the island. Zubair came home carrying his share of the fish.",
   [("dhoni_engine", "ދޯނި", -20), ("footsteps_sand", "ގެއަށް", -22)])
sh(54, "Not a trace of grief or sorrow at his sister having left this world could be seen on his face.")
sh(55, "Zubair put the fish on a tray and got ready to cut them. At that moment Faathanikey came into the house carrying a water pot.",
   [("footsteps_sand", "ވަދެގެން", -22)])
sh(56, "After setting the pot down, Faathanikey walked towards Zubair. \"Did you look in on Shahula? That girl's fever still hasn't come down.\"",
   [("soft_thud", "ބެހެއްޓުމަށްފަހު", -24)])
sh(57, "Faathanikey said in an extremely worried voice. But no answer came from Zubair.")
sh(58, "As if he did not care at all, he carried on with the work of cutting the fish. Faathanikey repeated her words once more. But")
sh(59, "this time she had to hear a painful answer she never expected. \"Go away and stop pestering my head! After going out to sea,")
sh(60, "after struggling without rest in strong wind and rain until my eyes and head are swollen, is all Faathanikey can think of to bother my head as soon as I come home?")
sh(61, "I heard you going on about this all the way from the dhoni to the island, and from the island all the way to the house. Not satisfied even with that,")
sh(62, "you couldn't stop even after coming into this house, could you? What kind of great burden is this? Is this the first time someone has died?\"")
sh(63, "Zubair answered with displeasure. \"Look, Zubair! She was your own sister, born of the same mother and father.")
sh(64, "Have you forgotten all the countless things that sister did for Zubair?\" Faathanikey said in a voice full of astonishment and disappointment.")
sh(65, "\"Didn't she make us pay the price of those services before she went? While we can't even manage our own lives, now we are stuck dealing with Shahula's affairs.")
sh(66, "What kind of great hardship is this now? How good it would have been if she had taken her along when she went!\" After he stopped cutting the fish,",
   hum=True)
sh(67, "Zubair rinsed his hands in a displeased manner and stood up. Zubair's changed, harsh behaviour gave Faathanikey's heart a great shock.",
   [("pour", "އަތްދޮވެލައިގެން", -20)])
sh(68, "Was this really the same kind Zubair she knew? Could a person change so much in such a short while? It was a truth hard even to believe.")
sh(69, "Through her disappointment, Faathanikey's eyes filled with tears and began to blur. When Zubair carelessly took the towel that was hung up and went into the house, Faathanikey, lost in deep thought,",
   [("footsteps_sand", "ވަދެގެން", -22)])
sh(70, "looked at the fish Zubair had left uncut. In despair, Faathanikey sat down to finish the work Zubair had left unfinished.")
sh(71, "As she tried to wipe away the drops of sweat running down her forehead, Faathanikey's eyes fell on Shahula, standing there looking towards her.")
sh(72, "Wrapped in a blanket, shaking with feverish chills, tears were streaming from Shahula's two eyes.",
   [("breath", "ތުރުތުރުއަޅަމުން", -22)], hum=True)
sh(73, "And on her lips could be seen the trace of a quiet, painful sob.",
   [("sob_breath", "ގިސްލުމެއްގެ", -22)], hum=True)
SHOTS = S

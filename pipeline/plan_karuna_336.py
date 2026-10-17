"""Beat/shot plan for Karuna episode 336 — v2 re-cut on the new audio, all v1 images reused (thrown out, the streets, repentance, Aisamanike; used by plan_beats.py)."""

LOC = {
    "bedroom_storm": "Shima's bedroom on the upper floor of the wealthy family house in Male on a stormy night: polished marble-look floor, a bed with a pale quilt, a dressing table with a mirror at the right, a window with a sheer curtain at the left streaked with rain, the bedroom door open onto the bright landing, a shattered phone lying on the floor tiles",
    "landing_stairs": "the upper landing and wide polished staircase of the wealthy family house in Male at night: marble-look steps curving down into the dark hall, a carved wooden banister, a single wall lamp above casting long shadows down the stairs",
    "gate_lane": "outside the heavy dark front gate (bodu dhoroashi) of the wealthy family house in Male on a stormy night: a tall solid dark wooden gate in a high white wall, a narrow Male lane of wet asphalt with a big muddy puddle, tall pastel buildings, a sodium street light, pouring rain",
    "rain_lane": "a narrow empty Male lane at night in pouring rain: wet black asphalt shining with orange sodium street lights, tall pastel buildings with dark windows, parked motorbikes under plastic covers, rainwater running in the gutter, the lane stretching away into darkness",
    "dark_corner": "a narrow Male lane at night after the rain: a deep dark recessed doorway between two buildings in the foreground, puddles reflecting a single sodium street light far down the lane, parked motorbikes",
    "ruined_eave": "a derelict abandoned house (fal goa) beside a Male lane at night: crumbling whitewashed coral-stone walls, a boarded window, a rusty corrugated roof with an overhanging eave, damp ground beneath it, weeds, dripping water, a faint distant street light",
    "day_lane": "a busy narrow Male lane in hot hazy daylight: tall pastel buildings, small shopfronts with blank awnings, parked motorbikes, a few passers-by, harsh white sunlight and short shadows on the pale concrete",
    "hot_lane": "a quiet back lane of Male in a hot hazy afternoon: a peeling pastel wall, a low concrete step in the thin shade of a doorway, dusty pale concrete ground, harsh light",
    "seaside_tree": "a quiet seaside spot on the edge of Male on a hot hazy afternoon: the wide shade of an old leaning tree on the sand above a small beach, the turquoise lagoon glittering beyond, a low sea wall, heat haze",
    "mosque_night": "the women's prayer area of a small mosque in Male at night: a plain soft green-and-cream prayer carpet in rows, white walls, a simple plain arched mihrab niche with no lettering at the far end, a low wooden rehal stand, warm soft wall lamps, quiet and empty",
    "park_morning": "a small park in Male in the early morning: a simple wooden park bench under a leafy tree, a paved path, low hedges and a few palms, pastel buildings softly blurred behind, gentle morning sun",
    "stone_house_in": "inside Aisamanike's small old whitewashed coral-stone house: a woven mat on the floor, a low wooden bench, a small kitchen corner with a kerosene-blue stove and steaming pots, blue wooden window shutters open to the sandy yard",
    "stone_bedroom": "a small clean bedroom in Aisamanike's old coral-stone house at night: a simple wooden bed with a fresh white sheet and a soft pillow, whitewashed walls, closed blue wooden shutters, a small warm oil-style lamp on a stool",
    "stone_yard": "the sandy yard of Aisamanike's small old whitewashed coral-stone house: a breadfruit tree, a joali (rope swing seat) hanging from a wooden frame, blue wooden window shutters, a low coral-stone boundary wall with the lane beyond",
    "stone_house_lamp": "the main room of Aisamanike's small old coral-stone house in the evening: a woven mat, a low wooden bench, a wooden rehal stand, a single warm lamp, blue shutters closed against the night",
}
MOOD = {
    "bedroom_storm": "storm night: near-black blue shadows, silver rain on the window, cold white lightning flashes mixed with the warm light from the landing; furious, frightening, heartbreaking",
    "landing_stairs": "storm night inside the house: a single warm wall lamp, deep charcoal shadows, white lightning through a high window; tense and frightening",
    "gate_lane": "storm night: near-black blue, heavy silver rain, white lightning, an orange sodium street light reflected in the puddle; devastating and lonely",
    "rain_lane": "rainy night lanes: sodium street lights on wet asphalt, near-black blue sky, silver rain; desolate and lonely",
    "dark_corner": "late night lanes: a single distant sodium street light, deep shadow, wet reflections; tense and fearful",
    "ruined_eave": "late night: deep blue darkness, a faint distant orange street light, dripping water; desolate, cold and sorrowful",
    "day_lane": "hot hazy daytime: harsh white sunlight, bleached colours, short hard shadows; humiliating and lonely",
    "hot_lane": "hot hazy afternoon: harsh light, dusty muted colours, oppressive heat; weary but quietly determined",
    "seaside_tree": "hot hazy afternoon by the sea: cool dappled shade under the tree against the blazing glittering lagoon; tender, tearful joy",
    "mosque_night": "mosque at night: soft warm lamps, gentle golden glow on the plain carpet, deep calm shadows; humble, penitent, peaceful",
    "park_morning": "early morning: soft gentle golden sunlight, fresh air, long soft shadows; weak and exhausted turning to hope",
    "stone_house_in": "Aisamanike's house by day: warm golden morning light through the open blue shutters, steam from the pots; safe, warm and comforting",
    "stone_bedroom": "Aisamanike's house at night: a single cosy warm lamp, soft amber glow, deep calm shadows; peaceful and safe",
    "stone_yard": "warm golden morning in the sandy yard: dappled sunlight through the breadfruit leaves; hopeful and calm",
    "stone_house_lamp": "cosy lamp evening: a single warm lamp glow, soft amber light on faces, deep warm shadows; tender and hopeful",
}

HS = "her cream hijab fully covering her hair and neck"
HN = "her dark navy hijab fully covering her hair and neck"
HA = "her white headscarf fully covering her hair and neck"
WET = ("her dusty-lavender loose long dress and cream hijab soaked dark by the rain but fully opaque and loose, "
       "the hijab still fully covering her hair and neck")

BEATS = [
    # ---------------- opening: the bedroom (seg 1-11) — no contact ever shown
    dict(v1="beat_001", to=3, reason="episode opening, straight after 335's phone smash: Shima on her knees begging her father (speaker focus, shot)",
         chars=["shima", "qasim"], loc="bedroom_storm", speaker="shima",
         visual=f"Shima kneeling on the marble-look bedroom floor with her hands clasped together in front of her chest, begging, her face lifted towards the camera wet with tears, mouth open in a desperate plea; she wears her dusty-lavender loose long dress and {HS}; in the soft-focus foreground at the side the back and shoulder of her father Qasim in his white shirt, standing rigid, well over an arm's length away from her, not touching her; the shattered phone on the tiles between them; rain streaking the window behind",
         camera="over-the-shoulder medium shot from behind Qasim, slightly high angle, Shima centred and sharp in the upper two-thirds, the floor tiles as the lower third",
         amb="apartment_rain_night", sens="violence",
         safe="'clutching his feet' becomes Shima kneeling at a distance with clasped hands; no touching"),
    dict(v1="beat_002", to=8, reason="reverse shot: Qasim, merciless, disowns her and shouts, pointing at the door (speaker focus)",
         chars=["qasim", "shima"], loc="bedroom_storm", speaker="qasim",
         visual="Qasim in his crisp white shirt standing tall, his face dark red with fury, salt-and-pepper moustache, eyes blazing, shouting, his arm stretched out stiffly pointing towards the open bedroom door; in the soft-focus foreground the back of Shima's cream hijab and lavender shoulders as she kneels on the floor far from him; a white lightning flash in the rain-streaked window behind him",
         camera="medium shot from a low angle over the kneeling Shima, Qasim centred and sharp in the upper half, the dim floor as the lower third",
         amb="apartment_rain_night", sens="violence", safe="his rage shown only as a furious face and an arm pointing at the door; no contact"),
    dict(v1="beat_003", to=9, reason="character enters: Naseema runs in weeping and tries to stop him",
         chars=["naseema"], loc="bedroom_storm",
         visual=f"Naseema in her grey-patterned dark dress and {HN} standing frozen in the bright open bedroom doorway, weeping, one hand pressed to her mouth and the other raised open-palmed in a pleading 'stop' gesture, leaning back against the door frame as if held back by her own fear; tears on her cheeks; the warm light of the landing behind her",
         camera="medium shot, eye level, Naseema centred in the upper half, the polished floor as the lower third",
         amb="apartment_rain_night", sens="violence",
         safe="'he shoved Naseema away' becomes Naseema alone at a distance, pressed back against the door frame in fear; nobody touches her"),
    dict(v1="beat_004", to=11, reason="action change: his fury turns on Shima; she cries out in fear on the floor (hair-pulling never shown)",
         chars=["shima"], loc="bedroom_storm",
         visual=f"Shima crouched low on the bedroom floor, both hands raised protectively to the sides of her head over {HS}, her face twisted with fear and crying out; a huge dark man's shadow from the doorway light falls across the wall and floor beside her, the man himself out of frame; the shadow does not touch her; rain on the window",
         camera="medium close shot, high angle, Shima's face in the upper two-thirds, the shadowed floor as the lower third",
         amb="apartment_rain_night", sens="violence",
         safe="seizing her hair and hauling her up is replaced by Shima cowering alone and a looming shadow; no contact, no man in frame"),
    # ---------------- the staircase (seg 12-14)
    dict(v1="beat_005", to=14, reason="scene change: down the staircase; Shima pleads that it is raining and she carries a child (speaker focus)",
         chars=["shima"], loc="landing_stairs", speaker="shima",
         visual=f"Shima halfway down the wide polished staircase, stumbling alone, one hand on the banister, turned back to look up the stairs, her other hand pressed to her belly, pleading with tear-streaked face; she wears her dusty-lavender loose long dress and {HS}; at the top of the stairs only the dark silhouette of her father standing against the lamp light, far above her, his long shadow stretching down the steps",
         camera="medium shot from slightly below on the stairs, Shima centred and sharp in the upper half, the empty lower steps as the lower third",
         amb="apartment_rain_night", sens="violence",
         safe="'dragged down the stairs' becomes Shima stumbling down alone with her father's silhouette and shadow far above; no contact"),
    # ---------------- the gate and the puddle (seg 15-19)
    dict(v1="beat_006", to=16, reason="scene change: the front gate is open onto the rainy lane; Shima is already outside, fallen in a muddy puddle",
         chars=["shima"], loc="gate_lane",
         visual=f"the heavy dark front gate standing open in the high white wall, warm light spilling from the house behind it and the dark silhouette of a man standing in the gateway, featureless; outside in the pouring rain on the lane Shima already sitting in a big muddy puddle, propped on one hand, looking back up at the gate in shock; {WET}; silver rain and an orange street light",
         camera="wide shot from the lane, eye level, the gate and silhouette in the upper half, Shima in the middle, the rain-pocked puddle and wet asphalt as the lower third",
         amb="storm_night", transition="cut", sens="violence",
         safe="the shove is never shown: the open gate, a featureless silhouette, Shima already sitting in the puddle; opaque loose wet clothes"),
    dict(v1="beat_007", to=17, reason="action change: the gate slams and is locked — she is left alone in the dark storm",
         loc="gate_lane",
         visual="the heavy dark wooden front gate firmly shut in the high white wall in the pouring rain, rainwater streaming down its surface, a white flash of lightning across the sky above the house, the lit upper windows of the house behind the wall; the empty wet lane and puddle in front; no people visible",
         camera="medium wide shot, low angle from the lane, the shut gate filling the upper two-thirds, the rain-pocked puddle as the lower third",
         amb="storm_night", transition="cut"),
    dict(v1="beat_008", to=20, reason="emotional turning point: in a lightning flash, Shima sits soaked in the mud, crying with her hand on her belly",
         chars=["shima"], loc="gate_lane",
         visual=f"Shima sitting alone in the muddy puddle in front of the shut gate, lit by a cold white flash of lightning, shivering, crying, one hand resting on her belly and the other at her chest; {WET}; heavy silver rain all around, the orange street light reflected in the water",
         camera="medium close shot, eye level, her face in the upper two-thirds, the rain-pocked muddy water as the lower third",
         amb="storm_night", sens="clothing", safe="soaked clothing stays loose and fully opaque; hijab on"),
    dict(v1="beat_009", to=22, reason="scene change: alone on the street, a long dark road ahead (reflective narration held on one wide image)",
         chars=["shima"], loc="rain_lane",
         visual=f"a small lonely figure of Shima standing alone in the middle of the long empty narrow lane in the pouring rain, seen from behind, her arms wrapped around herself; {WET}; the lane stretching far away into darkness under sodium street lights, thunderclouds lit by lightning above the tall pastel buildings",
         camera="wide shot from behind, eye level, the long lane and stormy sky in the upper two-thirds, the shining wet asphalt as the lower third",
         amb="rain_night"),
    dict(v1="beat_010", to=25, reason="action change: she looks back at the shut gate and the lit house that cast her out",
         chars=["shima"], loc="gate_lane",
         visual=f"Shima standing in the rain in the lane, seen from behind and slightly to the side, looking up at the big lit family house behind the shut dark gate and the high white wall; warm golden windows glowing above, cold rain between; {WET}",
         camera="medium wide shot from behind, low angle, the house and its glowing windows in the upper two-thirds, the wet lane as the lower third",
         amb="storm_night"),
    dict(v1="beat_011", to=28, reason="emotional close-up: hot tears mingling with the rain, hand on her belly, shivering, nowhere to go",
         chars=["shima"], loc="rain_lane",
         visual=f"close-up of Shima's face in the rain, eyes red and brimming, tears and raindrops running down her cheeks together, lips trembling with cold; one hand pressed to her belly; {WET}; blurred orange street lights and dark buildings behind",
         camera="close-up, eye level, her face in the upper two-thirds, her hand on her belly and dark wet dress as a calm lower third",
         amb="rain_night", sens="clothing", safe="soaked clothing stays loose and opaque; hijab on"),
    # ---------------- the night lanes (seg 29-33)
    dict(v1="beat_012", to=31, reason="scene/action change: walking the narrow lanes she hears rowdy youths and hides in a dark corner",
         chars=["shima"], loc="dark_corner",
         visual=f"Shima pressed back into a deep dark recessed doorway in the foreground at the side, hiding, her hand over her belly, her frightened face half lit, holding her breath; her damp dusty-lavender loose dress and {HS}; far away down the lane under a single sodium street light a few blurred dark silhouettes of young men loitering by motorbikes, tiny and indistinct",
         camera="medium shot, eye level, Shima's face in the upper half at the side, the distant lane in the upper middle, the wet ground as the lower third",
         amb="city_lanes_night", sens="other",
         safe="the rowdy youths are only distant blurred silhouettes; no threat shown"),
    dict(v1="beat_013", to=33, reason="scene change: she sleeps under the eave of a derelict house, sobbing",
         chars=["shima"], loc="ruined_eave",
         visual=f"Shima curled up sitting on the damp ground under the overhanging eave of a derelict coral-stone house, her back against the crumbling wall, knees drawn up under her loose damp dusty-lavender long dress, one hand resting on her belly, eyes closed with tears on her cheeks; {HS}; fully covered; water dripping from the rusty eave",
         camera="medium wide shot, eye level, her face in the upper two-thirds, the dark damp ground as the lower third",
         amb="abandoned_house", sens="other", safe="sleeping rough shown sitting curled under the eave, fully covered, no threat"),
    # ---------------- the next days: judgement (seg 34-39)
    dict(v1="beat_014", to=35, reason="time jump to the next day: townswomen stare, point and jeer at her (speaker focus on the gossips)",
         loc="day_lane", speaker="the whispering townswomen",
         visual="in a hot bright Male lane two middle-aged Maldivian townswomen stand together, one in a dark olive patterned long dress with a black hijab and the other in a rust-brown long dress with a dark maroon hijab (neither wears lavender, purple or cream), their hijabs fully covering their hair and neck; they stand by a shopfront, one pointing a finger sharply off to the side with a scornful look while speaking, the other whispering behind her hand; their faces soft, ordinary, not caricatured; harsh white daylight",
         camera="medium shot, eye level, the two women centred in the upper half, the pale sunlit pavement as the lower third",
         amb="city_day", transition="black", sens="other", safe="gossips shown as two ordinary women whispering and pointing at a distance; no caricature"),
    dict(v1="beat_015", to=37, reason="action change: Shima walks on, head bowed, wrapping her dress around herself as women turn their faces away",
         chars=["shima"], loc="day_lane",
         visual=f"Shima walking along the bright lane with her head bowed, pulling the cloth of her loose dusty-lavender long dress tightly around her body, her pregnancy beginning to show under the loose fabric, {HS}; in the background two women in hijabs turning their faces away and a woman pointing at her from a doorway, soft and blurred; harsh sunlight",
         camera="medium shot, slightly low angle, Shima's bowed face in the upper half, the bright pavement as the lower third",
         amb="city_day", sens="clothing", safe="loose long dress, no exposed belly"),
    dict(v1="beat_016", to=39, reason="time jump: days pass; thin and starving, yet a fierce maternal love rises in her",
         chars=["shima"], loc="hot_lane",
         visual=f"Shima, visibly thinner and weary, hollow-cheeked, sitting on a low concrete step in the thin shade of a doorway in a hot back lane, her loose dusty-lavender long dress dusty and creased, {HS}; both hands resting on her visibly pregnant belly under the loose dress, a faint new light of determination in her tired eyes",
         camera="medium shot, eye level, her face in the upper two-thirds, the dusty pale ground as the lower third",
         amb="city_day", transition="black", sens="other", safe="hunger shown only as a thin tired face; no exposed belly"),
    # ---------------- the baby kicks by the sea (seg 40-45)
    dict(v1="beat_017", to=41, reason="scene change: one hot afternoon under a seaside tree the baby kicks — tears of joy",
         chars=["shima"], loc="seaside_tree",
         visual=f"Shima sitting on the sand in the cool shade of an old leaning tree by the sea, startled and overwhelmed, her hand pressed to her visibly pregnant belly under her loose dusty-lavender long dress, tears of joy running down her cheeks and a trembling smile breaking through; {HS}; the glittering turquoise lagoon blazing beyond the shade",
         camera="medium wide shot, eye level, her face in the upper two-thirds, the shaded sand as the lower third",
         amb="seashore_day", sens="clothing", safe="loose long dress, no exposed belly"),
    dict(v1="beat_018", to=45, reason="emotional peak: she strokes her belly with both hands and whispers her promise (speaker focus)",
         chars=["shima"], loc="seaside_tree", speaker="shima",
         visual=f"close-up of Shima's tearful smiling face looking down tenderly, her lips moving in a whisper, both hands gently stroking her pregnant belly under the loose dusty-lavender dress; {HS}; dappled leaf shade on her face, the bright sea softly blurred behind",
         camera="close-up, slightly high angle, her face centred in the upper half, her hands on the loose dress as the lower third",
         amb="seashore_day"),
    # ---------------- the mosque (seg 46-50) — respectful, side/behind
    dict(v1="beat_019", to=47, reason="scene change: that night in a mosque she prays and weeps in sujood, repenting",
         chars=["shima"], loc="mosque_night",
         visual=f"seen from the side at a respectful distance: Shima alone in the empty women's prayer area of a small mosque, in sujood on the plain prayer carpet, her forehead to the carpet, her loose dusty-lavender long dress and {HS} covering her completely, her shoulders shaking with weeping; a plain arched mihrab niche with no lettering softly blurred at the far end; warm soft lamps",
         camera="wide side view, eye level near the floor, the figure and mihrab in the upper two-thirds, the plain carpet as the lower third",
         amb="mosque_interior", sens="other", safe="prayer shown from the side, respectful posture, no text or Arabic lettering anywhere"),
    dict(v1="beat_020", to=50, reason="action change: sitting after prayer, hands raised in dua; calm and hope fill her",
         chars=["shima"], loc="mosque_night",
         visual=f"seen from behind and slightly to the side: Shima sitting on the plain prayer carpet after the prayer, her hands raised in front of her with palms open in dua, head slightly bowed, {HS}, her loose dusty-lavender dress spread around her; the warm lamp light falls softly over her and the plain empty mihrab arch ahead with no lettering",
         camera="medium wide shot from behind three-quarter, the figure and mihrab in the upper two-thirds, the carpet as the lower third",
         amb="mosque_interior", sens="other", safe="dua seen from behind; no text anywhere"),
    # ---------------- Aisamanike (seg 51-61)
    dict(v1="beat_021", to=52, reason="time jump to the next morning: faint with hunger on a park bench, an elderly woman approaches — Aisamanike",
         chars=["shima", "aisamanike"], loc="park_morning",
         visual=f"Shima slumped weakly on a wooden park bench under a leafy tree, pale and exhausted, eyes half closed, one hand on her pregnant belly, {HS}; walking towards her along the paved path from the side, Aisamanike, an elderly kind woman in her sage-green libaas and {HA}, looking at her with deep compassion; soft golden morning sun",
         camera="medium wide shot, eye level, both faces in the upper two-thirds, the paved path as the lower third",
         amb="garden_day", transition="black"),
    dict(v1="beat_022", to=55, reason="dialogue: Aisamanike sits beside her, takes her hand and speaks kindly — 'my daughter...' (speaker focus)",
         chars=["aisamanike", "shima"], loc="park_morning", speaker="aisamanike",
         visual=f"Aisamanike in her sage-green libaas and {HA} sitting on the park bench beside Shima, turned towards her, speaking gently with a warm, kind, sorrowful smile, holding Shima's hand in both of hers; Shima softer at the side in the foreground, her cream hijab and lavender shoulder seen three-quarter from behind; morning sunlight through the leaves",
         camera="over-the-shoulder medium close shot, Aisamanike centred and sharp in the upper half, their joined hands and the bench as the lower third",
         amb="garden_day"),
    dict(v1="beat_023", to=58, reason="reverse shot: Shima, weeping, tries to confess the truth; Aisamanike strokes her head (speaker focus)",
         chars=["shima", "aisamanike"], loc="park_morning", speaker="shima",
         visual=f"Shima sitting on the park bench, weeping, her face crumpling as she tries to speak, eyes lifted to the older woman; {HS}; Aisamanike beside her, softer at the side, in her sage-green libaas and {HA}, gently resting her hand on the top of Shima's hijab-covered head in comfort; morning sunlight",
         camera="medium close shot, eye level, Shima centred and sharp in the upper half, Aisamanike soft at the side, the bench as the lower third",
         amb="garden_day"),
    dict(to=61, reason="return to Aisamanike speaking: people make mistakes, the baby is innocent, come live with me (reverse shot)",
         reuse="beat_022", chars=["aisamanike", "shima"], loc="park_morning", speaker="aisamanike",
         amb="garden_day", transition="cut", visual="(reuse of beat_022)"),
    dict(v1="beat_025", to=62, reason="scene change: in Aisamanike's little house — warm food smells, safe shelter at last",
         chars=["shima", "aisamanike"], loc="stone_house_in",
         visual=f"inside the small whitewashed coral-stone house: Shima sitting on the woven mat, holding a steaming bowl of warm food in both hands, looking around with grateful tearful eyes, {HS}, her loose dusty-lavender dress; Aisamanike in her sage-green libaas and {HA} kneeling beside her ladling more food from a pot with a gentle smile; warm golden light through the blue shutters",
         camera="medium shot, eye level, faces in the upper two-thirds, the woven mat as the lower third",
         amb="stone_house_day"),
    dict(v1="beat_026", to=63, reason="action/time change: that night in a clean soft bed, she sinks into deep sleep",
         chars=["shima"], loc="stone_bedroom",
         visual=f"Shima peacefully asleep on her side in a simple clean wooden bed with a fresh white sheet pulled up to her shoulder, her face calm and relaxed at last, {HS} still on; the small warm lamp glowing on a stool beside the bed; whitewashed walls, closed blue shutters",
         camera="medium shot, slightly high angle, her face in the upper half, the white sheet as a calm lower third",
         amb="stone_house_night", sens="clothing", safe="asleep fully covered with her hijab on, alone"),
    # ---------------- weeks pass (seg 64-73)
    dict(v1="beat_027", to=65, reason="time jump: weeks pass; Shima helps with the housework and her health returns",
         chars=["shima", "aisamanike"], loc="stone_yard",
         visual=f"Shima, healthier with fresh colour in her face and a gentle smile, visibly pregnant under her loose dusty-lavender long dress, {HS}, hanging washed white cloths on a line in the sunny sandy yard; Aisamanike in her sage-green libaas and {HA} handing her a cloth from a basket, smiling; the breadfruit tree and the joali behind",
         camera="medium wide shot, eye level, faces in the upper two-thirds, the sandy yard as the lower third",
         amb="stone_house_day", transition="black", sens="clothing", safe="loose long dress, no exposed belly"),
    dict(v1="beat_028", to=68, reason="dialogue: neighbours gossip over the wall; Aisamanike tells Shima to pay no heed and focus on her baby (speaker focus)",
         chars=["aisamanike", "shima"], loc="stone_yard", speaker="aisamanike",
         visual=f"in the sandy yard Aisamanike in her sage-green libaas and {HA} speaking calmly and firmly to Shima with a reassuring smile, one hand lifted in a 'never mind them' gesture; Shima beside her softer at the side, {HS}, listening; in the far background over the low coral-stone wall two women in hijabs whispering, small and blurred",
         camera="medium shot, eye level, Aisamanike centred and sharp in the upper half, the sand as the lower third",
         amb="stone_house_day", sens="other", safe="gossips only small blurred women in hijabs whispering at a distance"),
    dict(v1="beat_029", to=70, reason="time/action change: each night she recites Quran, makes dua and talks about baby names with Aisamanike",
         chars=["shima", "aisamanike"], loc="stone_house_lamp",
         visual=f"in the warm lamp light Shima sitting on the woven mat, visibly pregnant under her loose dusty-lavender dress, {HS}, holding a closed Quran with a plain unmarked cover against her chest and smiling softly while talking; Aisamanike in her sage-green libaas and {HA} sitting beside her on the low bench, smiling warmly as they talk; an empty wooden rehal stand beside them",
         camera="medium shot, eye level, faces in the upper two-thirds, the woven mat as the lower third",
         amb="stone_house_night", sens="other", safe="the Quran is closed with a plain cover; no text or lettering anywhere"),
    dict(v1="beat_030", to=71, reason="action change: she learns to sew tiny baby clothes and weeps with happiness",
         chars=["shima"], loc="stone_house_lamp",
         visual=f"close shot of Shima sitting in the lamp light holding up a tiny plain white baby garment she has just sewn, a needle and thread in her fingers, tears of happiness shining on her cheeks and a soft smile; {HS}; a small basket of folded tiny white baby clothes beside her",
         camera="medium close shot, eye level, her face and the tiny garment in the upper two-thirds, her lap and the mat as the lower third",
         amb="stone_house_night"),
    dict(v1="beat_031", to=73, reason="closing image: she is now a strong mother, ready to face the world",
         chars=["shima"], loc="stone_yard",
         visual=f"Shima standing tall in the sandy yard in warm golden morning light beside the joali, visibly pregnant under her loose dusty-lavender long dress, {HS}, one hand resting on her belly, her chin raised, her face calm, strong and peaceful, gazing ahead with quiet confidence; the breadfruit tree and the whitewashed house behind",
         camera="medium shot, slightly low angle, her face in the upper third, the sunlit sand as the lower third",
         amb="stone_house_dawn", sens="clothing", safe="loose long dress, no exposed belly"),
]
S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# v2 re-cut: one sh() per NEW segment (work/segments.json, 73 segments, 731 s). English re-split from v1 to the new
# segment boundaries; SFX keys re-checked against the new Dhivehi; hum/speaker kept from the v1 shots on the same words.
sh(1, "Shima dropped to the floor and, clutching Qasim's feet, began to plead: \"Father! Forgive me! Father,\"",
   [("cloth_rustle", "ތިރިވެ", -22)], speaker="shima")
sh(2, "\"I have done wrong! I was led astray by Satan's whisperings. Father, kill me if you must...\"", speaker="shima")
sh(3, "\"...but don't throw me out of the house. Father, forgive me!\" Shima's voice choked in her tears.",
   [("sob_breath", "ކަރުނައިގެ", -22)], speaker="shima", hum=True)
sh(4, "But not the slightest mercy or pity arose in Qasim's heart. The honour and standing he had built over his whole life — his beloved daughter, whom he loved like his own soul, had crushed it into the mud.")
sh(5, "She had shattered his pride and disgraced him in front of the whole community. \"You! You are no child of mine!\"", speaker="qasim")
sh(6, "\"You have taken away my name and my honour! You have strangled me while I am still alive!\"", speaker="qasim")
sh(7, "\"A shameless, fornicating woman like you cannot stay in this house for even a single second! From this day on\"",
   speaker="qasim", hum=True)
sh(8, "\"I have no daughter!\" Qasim's voice echoed through the whole house.", speaker="qasim")
sh(9, "Hearing that terrifying voice, Shima's mother Naseema came running and, weeping, tried to stop Qasim. But with a sweep of his arm Qasim shoved Naseema away.",
   [("footsteps_pavement", "ދުވެފައި", -22), ("soft_thud", "ހޫރާލި", -22)])
sh(10, "He was in no state to listen to anyone or to forgive. Qasim seized Shima by the hair and forcibly hauled her up from the floor.")
sh(11, "Shima went on crying and screaming in pain. But she could not free herself from the strength of her father's grip.",
   [("gasp", "ހަޅޭއްލަވަމުން", -20)])
sh(12, "Down the stairs of the house he dragged her cruelly. \"Father! It's raining so hard tonight...\"",
   [("footsteps_pavement", "ސިޑިން", -22), ("thunder", "ވާރޭ", -20)], speaker="shima")
sh(13, "\"There is a child in my belly... Father, don't throw me out... Where will I go?\"", speaker="shima", hum=True)
sh(14, "\"I could die!\" The sound of Shima's sobbing would break anyone's heart.", hum=True)
sh(15, "But Qasim's hard, stony heart did not hear it. After opening the big front gate of the house, Qasim shoved Shima very hard out onto the road.",
   [("metal_gate", "ހުޅުވާލުމަށްފަހު", -18)])
sh(16, "Shima fell into a muddy puddle that had formed on the road. Into the heavy rain pouring from above, into that dark and frightening night, he left her all alone.",
   [("water_splash_small", "ވެއްޓުނީ", -16)])
sh(17, "The gate slammed shut with great force, and the sound of it being locked was heard. With that, Shima's whole world was shut.",
   [("door_slam", "ލެއްޕި", -14), ("lock_click", "ތަޅުލި", -16)])
sh(18, "In the light of a flash of lightning, there could be seen the pitiful sight of Shima sitting in the mud of the road, in the heavy rain, her clothes soaked through, crying with her hand on her belly.",
   [("thunder", "ވިދާލި", -14)], hum=True)
sh(19, "Her whole body was cold and trembling, yet the pain and the sense of guilt in her heart were far greater than that cold.",
   [("breath_heavy", "ތުރުތުރުއަޅަމުން", -22)])
sh(20, "The beautiful girl who had grown up with so much love and care was today, because of her own sin, all alone in the whole world, out on the street.")
sh(21, "Like the sky thundering overhead, what lay before her was a long road — barren, dark and full of pain.",
   [("thunder", "ގުގުރަމުންދިޔަ", -16)])
sh(22, "The price of the wrong she committed, lost in the intoxication of love, she now had to pay in a most heartbreaking way. This was the painful beginning of the many pains she would have to carry and the many tears she would have to shed.",
   hum=True)
sh(23, "In the pouring rain, Shima stood all alone on the road. The painful sight of the big front gate slamming shut in her face with a loud bang kept replaying before her eyes.",
   [("door_slam", "ލެއްޕިގެން", -22)])
sh(24, "From the beloved home she had lived in since the day she was born, her own parents had cast her out without any mercy or sympathy.")
sh(25, "Because of a single wrong, her whole life had turned barren, and before her own family she had become a great shame.")
sh(26, "As she grew soaked in the rain, the hot tears flowing from her eyes mingled with the rainwater.",
   [("sob_breath", "ކަރުނަތައް", -22)])
sh(27, "Standing with her hand on her belly, trembling in the bitter cold, Shima had nowhere in particular to go.",
   [("breath_heavy", "ތުރުތުރު", -22)])
sh(28, "The pitch darkness and emptiness of the night made her feel her helplessness all the more. Spending a night on the street while pregnant was something she had never imagined.")
sh(29, "With every step, her exhausted body felt more pain. Fear and unease closed in around her.",
   [("footsteps_pavement", "ފިޔަވަޅަކާއެކު", -22)])
sh(30, "As she walked through the narrow lanes of the island, hearing the voices of rowdy youths hanging about the streets, her heart shook with fear.",
   [("motorbike_pass", "ޕާޓޭ", -22), ("heartbeat", "ތެޅިގަނޭ", -20)])
sh(31, "To protect herself and the innocent child in her belly, she hurriedly slipped into a dark corner and hid.",
   [("footsteps_pavement", "އަވަސްއަވަހަށް", -22)])
sh(32, "That night she finally fell asleep under the eave of a derelict house by the road. Lying on the damp ground with her hand on her belly, Shima cried, sobbing and sobbing.",
   [("sob_breath", "ގިސްލަގިސްލާފައި", -22)])
sh(33, "The deceit of her lover and the hatred of her parents had broken her heart to pieces. With the sunrise of the next day, Shima had to face yet more hardship.")
sh(34, "When she stepped out into the daylight, people's eyes kept fixing on her. As her pregnancy began to show, it seemed everyone who saw her hurled words of reproach at her.")
sh(35, "\"There goes that shameless woman! Look at her — she has dragged her parents' good name down, and now she's wandering the streets!\"",
   speaker="the whispering townswomen")
sh(36, "Such heart-rending words kept reaching her ears. Some women pointed their fingers at her and turned their faces away, as though she were something unclean.")
sh(37, "Shima walked on with her head bowed, wrapping the dress she wore tightly around her body. The wounds those words gave her were far deeper and more painful than her physical exhaustion.",
   [("cloth_rustle", "ބޮނޑިކޮށްލަމުން", -22), ("footsteps_pavement", "ހިނގަމުން", -24)])
sh(38, "The days went by in such a wretched state. From hunger and thirst, Shima's body grew thin and wasted.")
sh(39, "Yet an extraordinary strength began to rise in her heart. It was the deep maternal love growing for the child in her belly.")
sh(40, "One afternoon, in the fierce heat, as she sat in the shade of a tree on the beach, the baby in her belly kicked very hard.",
   [("heartbeat", "ތޮޅެލި", -20)])
sh(41, "At that moment the tears flowing from Shima's eyes were tears of joy. Amid so much pain and sorrow, feeling that this innocent soul was with her brought her helpless heart an indescribable peace.",
   [("sigh", "ހިތްހަމަޖެހުމެއް", -22)], hum=True)
sh(42, "Stroking her belly with both hands, she whispered: \"My darling! However great the pain Mummy has to bear,\"", speaker="shima")
sh(43, "\"I will never let any harm come to you. Mummy will protect you.\"", speaker="shima", hum=True)
sh(44, "This was the strong promise Shima made for that child. After that day Shima's thinking changed completely.")
sh(45, "As she understood it, even if society was handing her the punishment her sin deserved, Almighty Allah is the Merciful Lord who forgives sins again and again.")
sh(46, "That night she entered a mosque, made wudu and stood to pray. Lying in sujood, she wept as one weeps for the dead.",
   [("water_splash_small", "ވުޟޫކޮށްގެން", -24), ("cloth_rustle", "ސަޖިދައިގައި", -24), ("sob_breath", "ރުއީ", -22)])
sh(47, "Confessing the sin she had committed, she repented with a complete repentance. \"O Allah! Forgive this servant of Yours the sin she has committed!\"",
   hum=True)
sh(48, "\"Save this servant from this wretchedness, and for the sake of the innocent child in her belly, show this servant a way!\"",
   hum=True)
sh(49, "Her prayers rose to the sky straight from the very depths of her heart. As soon as she finished praying, an extraordinary coolness and calm came over her heart.",
   [("sigh", "ފިނިކަމަކާއި", -22)], hum=True)
sh(50, "The fear she had felt vanished, and a new spirit of hope began to flow through her body. Allah's mercy reached Shima the very next morning.")
sh(51, "As she sat on a park bench, too hungry even to walk, an elderly aunty came towards her, her face full of boundless tenderness and kindness.",
   [("footsteps_pavement", "އައީ", -24)])
sh(52, "That was Aisamanike. Aisamanike is a lonely, childless woman who lives in a small house apart from the island's people.")
sh(53, "Seeing Shima's state moved Aisamanike's heart deeply. The talk going around the island about Shima had reached Aisamanike's ears too.")
sh(54, "But Aisamanike is someone who loves to be kind to people rather than criticise their faults. \"My daughter...\"",
   speaker="aisamanike")
sh(55, "\"Why are you sitting here all alone in this heat, in that state? Come with aunty to aunty's house,\" Aisamanike said very kindly, taking Shima's hand.",
   speaker="aisamanike")
sh(56, "At first Shima could hardly believe it. She had never imagined anyone would speak to her so lovingly.")
sh(57, "Weeping, Shima tried to reveal the truth about herself. \"Aunty... I... I am...\"", speaker="shima")
sh(58, "Before she could finish the sentence, Aisamanike stroked her head.",
   [("cloth_rustle", "ފިރުމާލި", -24)])
sh(59, "\"Aunty knows, my daughter. But human beings make mistakes. What matters is to feel remorse for it and repent.\"", speaker="aisamanike")
sh(60, "\"This innocent soul has no fault at all. Come, my daughter, and live with aunty.\"", speaker="aisamanike")
sh(61, "\"From today on, you are like aunty's very own child.\" As soon as Shima stepped into Aisamanike's little house, she felt that, after such a long time, she had found safe shelter.",
   [("door_open", "ވަނުމާއެކު", -22)], speaker="aisamanike")
sh(62, "The delicious smell of food drifting through the house and Aisamanike's kindness began to heal the wounds in Shima's heart.")
sh(63, "Aisamanike gave Shima hot food and made up a clean bed for her to sleep in. That night, as soon as she lay down on that soft bed, Shima sank into a deep sleep after so many sleepless nights.",
   [("cup_clatter", "ކާއެއްޗެހި", -24), ("cloth_rustle", "އޮށޯވެލުމާއެކު", -24)])
sh(64, "Days turned into weeks. Aisamanike brought joy and hope into Shima's life.")
sh(65, "As Shima helped Aisamanike with the housework, the wasting her body had suffered faded away and freshness began to return to her face.")
sh(66, "Some people in the community still criticised Aisamanike and reproached her for taking that disgraceful woman into her home.")
sh(67, "But Aisamanike paid no attention to any of that talk. \"What people say will take nothing away from our provision, my daughter.\"",
   speaker="aisamanike")
sh(68, "\"What you should focus on is the baby you are about to have,\" Aisamanike would always say, encouraging Shima.", speaker="aisamanike")
sh(69, "As her pregnancy came to term, the maternal love in Shima's heart grew beyond measure.")
sh(70, "Every night before sleeping she would recite the Quran and make heartfelt dua for her child. She would talk over with Aisamanike the beautiful names to give the baby once it was born.",
   [("page_turn", "ކިޔަވައި", -24)])
sh(71, "It was from Aisamanike, too, that she learned to sew tiny clothes for the baby. Every time she held those tiny garments in her hands, tears of joy would spill from Shima's eyes.",
   [("cloth_rustle", "ފަހަން", -24)], hum=True)
sh(72, "She is no longer the old Shima, frightened and despairing. She is now a strong mother.")
sh(73, "She stands ready to face every challenge society brings. Through repenting of her wrong and returning to the path of Allah, the spiritual peace she found has greatly restored her mental well-being.",
   hum=True)
SHOTS = S

"""Beat/shot plan for Karuna episode 337 (series finale; v2 re-cut on the new audio; used by plan_beats.py)."""

LOC = {
    "yard": "the sandy yard of Aisamanike's small old whitewashed coral-stone house in Male: blue wooden window shutters, a breadfruit tree, a wooden joali (rope swing seat) hanging in its shade, swept white sand, a low coral wall",
    "delivery": "a hospital delivery room: a plain white ceiling with a strong round white examination light, a heart monitor on a stand showing only a soft green wave line and no numbers, pale walls, a white sheet and a pillow",
    "hospital_window": "the window of the hospital delivery room: a pale blind half open, beyond it the rooftops of Male and a strip of sea",
    "memory_gate": "a narrow Male lane outside a wealthy family's house on a stormy night: a heavy dark front gate (bodu dhoroashi) in a high wall, wet asphalt with a muddy puddle, a sodium street light",
    "rented_room": "a tiny bare rented room in Male: peeling pale-green walls, a single bare bulb hanging from the ceiling, a thin mattress on the floor with a faded sheet, a small plastic table, a folded pile of baby clothes, a small window with a cheap curtain",
    "shop_lane": "a narrow Male lane outside a tiny corner grocery shop: tall pastel buildings, parked motorbikes, a shop counter with shelves of plain unlabelled tins and packets",
    "small_office": "an ordinary small office in Male: a few cheap desks, stacks of plain folders, an old computer monitor turned away, a filing cabinet, a window with a blind",
    "company_office": "the bright modern office of a successful Male company: glass partitions, a long light-wood meeting table, a view of the sea and the city through tall windows, green plants",
    "apartment": "Shima's bright modern apartment in Male: a light sitting room with a sofa, a low coffee table with crayons and paper, children's drawings of suns, houses and flowers pinned on the wall (pictures only, no words), soft toys and a toy box, big windows with sheer curtains",
    "beach_sunset": "the Male artificial beach at golden sunset: a long paved walkway along the seafront, a wooden bench facing the calm lagoon, a few young palm trees, the sun low over the sea",
    "beach_dusk": "the Male artificial beach at blue dusk after sunset: the paved walkway, the wooden bench, the calm dark lagoon, the first street lamps glowing warm, the city lights of Male behind",
}
MOOD = {
    "yard": "fresh early morning, soft golden sunrise light through the breadfruit leaves, dewy and peaceful, hopeful",
    "delivery": "cold white ceiling light of a hospital room, sterile pale blues and whites, tense and exhausting, with warmth only on the faces",
    "hospital_window": "first light of dawn breaking: cold blue night turning to warm gold, symbolic hope, quiet",
    "memory_gate": "memory: near-black blue stormy night, silver rain, a flash of white lightning, sodium light on wet asphalt, soft dreamlike blur at the edges, desaturated",
    "rented_room": "night, the dim yellow light of a single bare bulb, deep shadows, tired and lonely but tender",
    "shop_lane": "hot hazy afternoon, harsh sunlight and hard shadows in the narrow lane, muted colours",
    "small_office": "neutral flat daylight of a modest office, slightly grey, hard-working",
    "company_office": "bright clear daylight, clean airy whites and soft blues, confident and successful",
    "apartment": "bright warm afternoon daylight through sheer curtains, cheerful soft colours, cosy and happy",
    "beach_sunset": "golden sunset: warm amber and rose light across the sky and the water, long soft shadows, emotional and tender",
    "beach_dusk": "blue dusk after sunset: violet and deep blue sky with a last pink glow on the horizon, warm lamp light, calm and peaceful",
}

HIJ = "her cream hijab fully covering her hair and neck"
HIJ_O = "her ivory hijab fully covering her hair and neck"
HIJ_Z = "her small white headscarf fully covering her hair and neck"
GOWN = f"a loose long-sleeved pale hospital gown with a white sheet drawn up to her chest and {HIJ}"
TIRED = f"Shima a little older and tired, thinner, dark circles under her eyes, in her plain dusty-lavender long dress and {HIJ}"

BEATS = [
    # ---- morning in Aisamanike's yard
    dict(to=4, v1="beat_001", reason="episode opening: a morning months later, Shima on the joali in Aisamanike's yard talks to her unborn child",
         chars=["shima"], loc="yard", speaker="shima",
         visual=f"Shima, visibly pregnant in a loose ankle-length dusty-lavender dress and {HIJ}, sitting on the wooden joali swing seat in the sandy yard, one hand resting gently on her rounded belly over the loose dress, looking down at it with a soft tender smile and moist eyes, lips parted as if whispering; morning light through the breadfruit leaves",
         camera="medium shot, eye level, her face in the upper third, the swept white sand as a calm lower third",
         amb="stone_house_dawn", sens="clothing", safe="pregnancy shown only by a loose long dress; no exposed belly"),
    dict(to=9, v1="beat_002", reason="action change: the labour pains begin; Aisamanike at her side, Shima calm and hopeful",
         chars=["shima", "aisamanike"], loc="yard",
         visual=f"Shima, visibly pregnant in her loose dusty-lavender dress and {HIJ}, standing up from the joali with one hand on her lower back, a brief wince turning into a calm, brave, hopeful expression; Aisamanike in her sage-green libaas and white headscarf beside her, holding her elbow supportively and smiling encouragingly; the blue-shuttered coral-stone house behind",
         camera="medium two-shot, eye level, faces in the upper two-thirds, the sand as the lower third",
         amb="stone_house_day"),
    # ---- the delivery room
    dict(to=11, v1="beat_003", reason="scene change: the hospital delivery room — the heart monitor and the white ceiling light (Shima's blurred view)",
         loc="delivery",
         visual="looking up from a hospital bed: a strong round white light on the plain white ceiling, slightly blurred and haloed as if seen through tired eyes; at the side a heart monitor on a stand with only a glowing green wave line and no numbers; nobody in view",
         camera="low-angle point of view looking up, the light in the upper third, the soft pale wall as the lower third",
         amb="delivery_room", sens="other", safe="childbirth shown only through Shima's point of view of the ceiling light and the monitor"),
    dict(to=14, v1="beat_004", reason="character focus: Shima's face in labour — short breath, sweat, clenched teeth",
         chars=["shima"], loc="delivery",
         visual=f"close-up of Shima's face and shoulders on a white pillow, in {GOWN}; beads of sweat on her brow and running down her cheeks, eyes squeezed half shut, teeth clenched in effort, one hand gripping the sheet near her shoulder; cold white light from above",
         camera="close-up, slightly high angle, her face in the upper half, the white sheet as the lower third",
         amb="delivery_room", sens="other", safe="childbirth: only her face and upper body under the sheet, hijab on, no lower body, no medical detail"),
    dict(to=15, v1="beat_005", reason="flashback: the memory of the rainy night she was thrown out of the gate", transition="dissolve",
         chars=["shima", "qasim"], loc="memory_gate",
         visual=f"memory: on a pouring stormy night young Shima sits alone in a muddy puddle on the wet lane outside a heavy dark gate, soaked, her loose dusty-lavender dress opaque and heavy with rain, {HIJ}, one hand on the ground, looking back up at the gate in despair; the gate is closing and in the narrowing gap Qasim in his white shirt stands as a dark stern silhouette, pointing away down the lane; silver rain, a flash of lightning, soft dreamlike blur at the edges",
         camera="wide shot, eye level, the gate and silhouette in the upper two-thirds, the rain-pocked puddle and wet asphalt as the lower third",
         amb="memory_rain", sens="violence",
         safe="being thrown out is shown only as the aftermath: Shima already sitting in the puddle, Qasim's silhouette in the closing gate, no contact"),
    dict(to=19, v1="beat_006", reason="return from memory: the experienced nurse holds Shima's hand for the final push", transition="dissolve",
         chars=["shima", "nurse"], loc="delivery",
         visual=f"Shima on the hospital pillow in {GOWN}, tears and sweat streaming down her face, eyes squeezed shut, taking a deep breath for a final effort; the nurse in light-blue scrubs and white hijab leans in beside the bed, holding Shima's hand firmly in both of hers with a kind, steady, encouraging look; the monitor with a green wave line without numbers softly behind",
         camera="medium close-up, eye level, both faces in the upper half, their clasped hands and the white sheet in the lower third",
         amb="delivery_room", sens="other", safe="childbirth: faces, upper bodies and the clasped hands only"),
    dict(to=20, v1="beat_007", reason="symbolic: a step out of the darkness of the past toward the light of hope (reflective narration)",
         loc="hospital_window",
         visual="the hospital window at the first moment of dawn: a pale blind half open, the cold blue night outside giving way to a warm golden sunrise over the rooftops of Male and a strip of glittering sea, a beam of gold light falling into the white room; no people",
         camera="medium shot of the window, the sunrise in the upper two-thirds, the pale windowsill and shadowed wall as the lower third",
         amb="delivery_room"),
    dict(to=23, v1="beat_008", reason="turning point: the baby's first cry — all pain vanishes; deep relief and tears",
         chars=["shima", "nurse"], loc="delivery",
         visual=f"Shima lying back on the pillow in {GOWN}, exhausted, her eyes opening wide in wonder, tears of relief running down her cheeks, a trembling smile beginning; in the soft-focus background the nurse in light-blue scrubs and white hijab lifting a small bundle wrapped in a soft white blanket; warm light now on Shima's face",
         camera="close-up on Shima, slightly high angle, her face in the upper half, the nurse softly blurred behind, the sheet as the lower third",
         amb="delivery_room", sens="other", safe="birth shown only by Shima's relieved face; the baby is a clean white bundle; no crying sound used"),
    dict(to=26, v1="beat_009", reason="action change: the nurse lays the clean swaddled baby girl on Shima's chest",
         chars=["shima", "nurse"], loc="delivery",
         visual=f"Shima in {GOWN}, holding a tiny clean newborn baby swaddled in a soft white blanket against her chest with both arms, gazing down at the baby's tiny face and small curled hands with overwhelming love and tears of joy; the nurse in light-blue scrubs and white hijab smiling at her side, her hands just letting go of the bundle; warm soft light",
         camera="medium close-up, slightly high angle, Shima's face and the baby in the upper two-thirds, the white blanket and sheet as the lower third",
         amb="delivery_room", sens="other", safe="newborn clean and swaddled in white, held against her gown"),
    dict(to=30, v1="beat_010", reason="emotional peak: 'Mother's little Zeeva' — Shima kisses her baby's forehead and makes her promise",
         chars=["shima"], loc="delivery", speaker="shima",
         visual=f"close-up of Shima in {GOWN} tenderly kissing the forehead of the tiny newborn swaddled in a soft white blanket held at her chest, her eyes closed, tears on her cheeks, a deeply peaceful smile; warm golden light on both faces, the cold room blurred away",
         camera="close-up, eye level, Shima's face and the baby's head in the upper half, the white blanket as the lower third",
         amb="delivery_room"),
    # ---- the hard years
    dict(to=32, v1="beat_011", reason="time jump: the days pass quickly — a tiny rented room, sleepless nights with the baby", transition="black",
         chars=["shima"], loc="rented_room",
         visual=f"{TIRED}, sitting on the thin mattress on the floor of the tiny rented room late at night, rocking a crying baby wrapped in a pale-yellow blanket against her shoulder, her own eyes wet and heavy with exhaustion; the single bare bulb casting a dim yellow light, deep shadows on the peeling walls",
         camera="medium wide, eye level, her face and the baby in the upper half, the bare floor and mattress as the lower third",
         amb="room_night", sens="other", safe="baby Zeeva has no card: described as a baby in a pale-yellow blanket"),
    dict(to=34, v1="beat_012", reason="scene change: buying milk with her last money; judging looks from townspeople",
         chars=["shima"], loc="shop_lane",
         visual=f"{TIRED}, carrying a baby in a pale-yellow romper on her hip in a cloth sling, holding a single plain unlabelled tin of baby milk, walking out of a tiny corner shop with her head held quietly high; in the soft background two women in hijabs whisper to each other and glance at her, their faces soft and blurred",
         camera="medium wide, eye level, her face in the upper third, the sunlit lane paving as the lower third",
         amb="city_day", sens="other", safe="gossips shown as two blurred women whispering at a distance; no caricature; no readable labels"),
    dict(to=36, v1="beat_013", reason="emotional turning point: Zeeva's tiny hand on her face gives her new life",
         chars=["shima"], loc="rented_room",
         visual=f"close-up of {TIRED} lying on the thin mattress facing a smiling baby in a pale-yellow romper; the baby's tiny palm resting on Shima's cheek; Shima's tired face breaking into a tearful, radiant smile; warm light from the bulb on both faces",
         camera="close-up, eye level, both faces in the upper half, the faded sheet as the lower third",
         amb="room_night", sens="other", safe="baby Zeeva described in text, no card"),
    dict(to=38, v1="beat_014", reason="scene change: her first low-level job in an ordinary small office",
         chars=["shima"], loc="small_office",
         visual=f"{TIRED} but focused, standing at a cluttered desk in a small plain office carrying a tall stack of plain folders, sleeves neat, working hard; in the soft background an older office boss in a shirt glances at her with an approving nod; no readable papers or screens",
         camera="medium shot, eye level, her face in the upper third, the desk top as the lower third",
         amb="office_day"),
    dict(to=40, v1="beat_015", reason="scene/time change: at night after Zeeva sleeps, Shima studies in the rented room",
         chars=["shima"], loc="rented_room",
         visual=f"{TIRED}, sitting at the small plastic table late at night studying, a notebook with unreadable lines and an old laptop whose soft glow lights her determined face (screen turned away); behind her on the mattress a small toddler in a pale-yellow romper sleeps peacefully under a blanket; the single bare bulb overhead",
         camera="medium shot, eye level, her face in the upper third, the table top as the lower third",
         amb="room_night"),
    # ---- seven years later
    dict(to=41, v1="beat_016", reason="time jump: seven years later — Shima is a respected senior manager at a successful company", transition="black",
         chars=["shima_older"], loc="company_office",
         visual=f"Shima, now about 28, in her camel-brown coat dress and {HIJ_O}, standing confidently at the head of a long light-wood meeting table in a bright glass-walled office, smiling calmly as she speaks; two colleagues (a man in a shirt and a woman in a hijab) listen respectfully, soft at the side; no readable screens, papers or nameplates",
         camera="medium shot, eye level, Shima centred in the upper third, the polished table as the lower third",
         amb="office_day"),
    dict(to=44, v1="beat_017", reason="scene change: her bright apartment full of Zeeva's drawings and toys; Zeeva at seven",
         chars=["zeeva", "shima_older"], loc="apartment",
         visual=f"in the bright sitting room seven-year-old Zeeva in her pale-yellow dress and {HIJ_Z} kneels at the low coffee table drawing with crayons, looking up with a bright happy smile; her colourful drawings of suns, houses and flowers (no words) pinned on the wall behind; soft toys on the floor; Shima in her camel-brown coat dress and {HIJ_O} sits on the sofa behind her watching with a loving smile",
         camera="medium wide, eye level, faces in the upper two-thirds, the light floor rug as the lower third",
         amb="apartment_morning", sens="other", safe="drawings are pictures only, no readable text"),
    dict(to=46, v1="beat_018", reason="reflective turn: freedom and peace of mind; past tears turned to a proud smile",
         chars=["shima_older"], loc="apartment",
         visual=f"Shima in her camel-brown coat dress and {HIJ_O} standing at the big window of her apartment, sheer curtain lifting, looking out over Male towards the sea with a calm, proud, peaceful smile; warm afternoon light on her face",
         camera="medium close-up, three-quarter view, her face in the upper third, the window sill and soft shadow as the lower third",
         amb="apartment_morning"),
    # ---- the beach
    dict(to=47, v1="beat_019", reason="scene change: golden sunset over the Male artificial beach", loc="beach_sunset",
         visual="a wide establishing view of the Male artificial beach at golden sunset: rays of gold spreading across the sky, the sun low over the calm lagoon, the long paved walkway and a wooden bench facing the sea, a few young palms; no people close",
         camera="wide establishing shot, the sunset sky in the upper two-thirds, the calm water and paving as the lower third",
         amb="beach_dusk"),
    dict(to=49, v1="beat_020", reason="characters enter: Shima and Zeeva on the bench, Zeeva with her ice-cream cup, chattering",
         chars=["shima_older", "zeeva"], loc="beach_sunset",
         visual=f"Shima in her camel-brown coat dress and {HIJ_O} and Zeeva in her pale-yellow dress and {HIJ_Z} sitting side by side on the wooden bench by the sea at golden sunset; Zeeva holds a small ice-cream cup and spoon, laughing as she tells a story with a lively gesture; Shima turned towards her, smiling with a full heart; the glowing lagoon behind",
         camera="medium two-shot from the front and side, faces in the upper two-thirds, the paved walkway as the lower third",
         amb="beach_dusk"),
    dict(to=51, v1="beat_021", reason="new figure: a frail white-haired old man approaches very slowly along the walkway with a cane",
         chars=["qasim_old"], loc="beach_sunset",
         visual="far along the walkway, coming from the left, a frail thin stooped old man with white hair in a faded grey shirt walks very slowly towards the camera, leaning heavily on a wooden cane, every step an effort; the golden sun behind him makes a soft halo, his face not yet clearly visible; the long walkway and the glowing sea",
         camera="long shot along the walkway, the figure in the upper-middle, the long paving as the lower third",
         amb="beach_dusk"),
    dict(to=53, v1="beat_022", reason="reveal: it is her father Qasim — no harshness left, only despair and sorrow",
         chars=["qasim_old"], loc="beach_sunset",
         visual="close-up of old Qasim STANDING upright on the walkway (not sitting, no bench behind him), stooped forward over his wooden cane: white hair, thin lined face, white stubble moustache, faded grey shirt, both hands on the cane; his face full of deep despair and sorrow, no trace of pride, eyes shining with tears; warm golden sunset light on one side of his face",
         camera="close-up, eye level, his face in the upper half, the cane and blurred sea below",
         amb="beach_dusk"),
    dict(to=55, v1="beat_023", reason="his gaze: first Shima's face, then little Zeeva, who looks just like the child Shima",
         chars=["shima_older", "zeeva", "qasim_old"], loc="beach_sunset",
         visual=f"over the shoulder of old Qasim (white hair, grey shirt, cane, blurred in the foreground): Shima in her camel-brown coat dress and {HIJ_O} sitting on the bench, looking up at him in shock; beside her Zeeva in her pale-yellow dress and {HIJ_Z} looking up curiously, her small face a mirror of her mother's; golden sunset behind them",
         camera="over-the-shoulder medium shot, Shima and Zeeva in the upper two-thirds, the paving as the lower third",
         amb="beach_dusk"),
    dict(to=56, v1="beat_024", reason="emotional turning point: Shima sits frozen as the dark pages of the past replay",
         chars=["shima_older", "zeeva"], loc="beach_sunset",
         visual=f"close-up of Shima in {HIJ_O} and camel-brown coat dress frozen on the bench, staring ahead, her face stunned, eyes wide and glistening, lips slightly parted; Zeeva beside her soft and out of focus; the golden light dimming slightly",
         camera="close-up, eye level, her face in the upper half, blurred sea below",
         amb="beach_dusk"),
    dict(to=57, reason="memory flash: the sound of the gate slamming on the rainy night (return to the memory image)",
         reuse="beat_005", chars=["shima", "qasim"], loc="memory_gate", transition="dissolve",
         visual="(reuse of beat_005)", amb="memory_rain", sens="violence", safe="reuse of the safe gate memory image"),
    dict(to=58, v1="beat_026", reason="return from memory: Shima stands slowly, Zeeva holding her hand (reverse shot planned for the beach dialogue)",
         chars=["shima_older", "zeeva"], loc="beach_sunset", transition="dissolve",
         visual=f"low angle as if from a kneeling man's eye level: Shima in her camel-brown coat dress and {HIJ_O} standing tall, looking down towards the camera with tears in her eyes and a guarded, conflicted expression; Zeeva in her pale-yellow dress and {HIJ_Z} standing close beside her holding her mother's hand, looking down curiously at the camera; the golden sunset sky and sea behind them",
         camera="slightly low-angle medium shot, both faces in the upper half, the paving and soft shadow as the lower third",
         amb="beach_dusk"),
    dict(to=59, v1="beat_027", reason="action detail: Qasim's trembling voice; the cane slips from his hand and falls",
         chars=["qasim_old"], loc="beach_sunset",
         visual="detail: a worn wooden cane lying fallen on the warm paving stones of the walkway, an old man's trembling empty hand just above it and his feet in plain sandals beside it; long golden sunset shadows",
         camera="close detail shot, low angle, the hand and cane in the upper-middle, the paving as the lower third",
         amb="beach_dusk"),
    dict(to=60, v1="beat_028", reason="action change: Qasim drops to his knees before Shima and hides his face in his hands, sobbing",
         chars=["qasim_old"], loc="beach_sunset", transition="cut",
         visual="old Qasim with white hair in his faded grey shirt kneeling on the paving of the walkway, his face hidden in both hands, his thin shoulders shaking as he sobs like a child; his wooden cane lying beside him; the hem of a camel-brown dress at the edge of the frame; golden sunset over the sea behind",
         camera="medium shot, slightly high angle (from Shima's viewpoint), his bowed head and hands in the upper half, the paving as the lower third",
         amb="beach_dusk", sens="other", safe="kneeling and weeping only, no injury"),
    dict(to=63, v1="beat_029", reason="dialogue: Qasim lifts his tear-streaked face and begs forgiveness (shot, speaker focus)",
         chars=["qasim_old"], loc="beach_sunset", speaker="qasim_old", transition="cut",
         visual="old Qasim kneeling on the walkway, his tear-streaked face lifted up towards the camera, speaking brokenly, his hands clasped in front of his chest pleading, white hair lit gold by the sunset; the cane lying beside him; the glowing sea behind",
         camera="slightly high-angle medium close-up, his face centred in the upper half, the paving as the lower third",
         amb="beach_dusk"),
    dict(to=64, reason="reverse shot: Shima, tears gathering, does not know what to say", reuse="beat_026",
         chars=["shima_older", "zeeva"], loc="beach_sunset", transition="cut", visual="(reuse of beat_026)", amb="beach_dusk"),
    dict(to=67, reason="shot: Qasim goes on, crying (speaker focus)", reuse="beat_029", speaker="qasim_old",
         chars=["qasim_old"], loc="beach_sunset", transition="cut", visual="(reuse of beat_029)", amb="beach_dusk"),
    dict(to=69, reason="return to Qasim's face in his hands: seeing his granddaughter breaks his heart", reuse="beat_028",
         chars=["qasim_old"], loc="beach_sunset", transition="cut", visual="(reuse of beat_028)", amb="beach_dusk"),
    dict(to=71, v1="beat_033", reason="emotional turning point: a storm inside Shima — old wounds against motherly tenderness",
         chars=["shima_older"], loc="beach_sunset",
         visual=f"close-up of Shima in {HIJ_O}, her face torn by inner conflict, tears welling, lips pressed together, eyes cast down; the sea wind lifting the loose end of her ivory hijab (still fully covering her hair and neck); behind her the sky turning stormy-gold, a few dark clouds lit by the sunset",
         camera="close-up, eye level, her face in the upper half, blurred sea below",
         amb="beach_dusk"),
    dict(to=75, v1="beat_034", reason="character focus: she looks down into Zeeva's innocent eyes and understands",
         chars=["zeeva"], loc="beach_sunset",
         visual=f"high-angle point of view looking down: Zeeva in her pale-yellow dress and {HIJ_Z} looking up with big innocent, kind, trusting eyes, holding her mother's hand (a woman's hand in a camel-brown sleeve entering from the top of the frame); golden sunset light on her face",
         camera="high-angle close shot, Zeeva's face in the upper half, the warm paving as the lower third",
         amb="beach_dusk"),
    dict(to=79, v1="beat_035", reason="action change: Shima kneels and lays her hand on her father's shoulder; startled, he looks up; she speaks gently (speaker focus)",
         chars=["shima_older", "qasim_old", "zeeva"], loc="beach_sunset", speaker="shima_older",
         visual=f"over old Qasim's shoulder (white hair, grey shirt, blurred in the foreground): Shima in her camel-brown coat dress and {HIJ_O} kneeling in front of him on the walkway, her hand resting gently on his shoulder, tears on her cheeks yet her face calm and gentle as she speaks; Zeeva in her pale-yellow dress and {HIJ_Z} standing just behind her, watching; golden sunset sky",
         camera="over-the-shoulder medium close-up, Shima centred and sharp in the upper half, the paving as the lower third",
         amb="beach_dusk", sens="other", safe="mahram father and daughter: only her hand on his shoulder"),
    dict(to=83, v1="beat_036", reason="dialogue close-up: Shima forgives him and the whole past for her own peace",
         chars=["shima_older"], loc="beach_sunset", speaker="shima_older",
         visual=f"close-up of Shima in {HIJ_O} kneeling, speaking softly with a gentle, tearful, serene smile, her eyes warm and at peace; warm golden light on her face, the sea and sky glowing softly behind",
         camera="close-up, eye level, her face centred in the upper half, blurred golden sea below",
         amb="beach_dusk"),
    dict(to=85, v1="beat_037", reason="action change: Shima helps her father up by the hand and introduces Zeeva: 'this is your grandfather'",
         chars=["shima_older", "qasim_old", "zeeva"], loc="beach_sunset", speaker="shima_older",
         visual=f"Shima in her camel-brown coat dress and {HIJ_O} standing, holding her father's hand having helped him to his feet; old Qasim beside her, white-haired and stooped, his other hand on his wooden cane, eyes wide and wet with amazement; Shima turns her smiling face towards Zeeva in her pale-yellow dress and {HIJ_Z}, who stands shyly a little apart looking up at the old man; golden sunset",
         camera="medium wide, eye level, faces in the upper two-thirds, the paving as the lower third",
         amb="beach_dusk", sens="other", safe="mahram father and daughter holding hands"),
    dict(to=86, v1="beat_038", reason="action change: Zeeva hesitates, then steps forward and hugs her grandfather's leg",
         chars=["zeeva", "qasim_old", "shima_older"], loc="beach_sunset",
         visual=f"little Zeeva in her pale-yellow dress and {HIJ_Z} hugging old Qasim's leg with both arms, her cheek against his trouser leg, eyes closed with a shy smile; Qasim leaning on his cane, looking down at her astonished, tears running down his face, his free hand hovering tenderly over her headscarf; Shima in her camel-brown coat dress and {HIJ_O} behind them smiling through tears; golden sunset",
         camera="medium shot, eye level, faces in the upper two-thirds, the paving as the lower third",
         amb="beach_dusk", sens="other", safe="mahram grandchild hugging her grandfather's leg, fully clothed, tender"),
    dict(to=88, v1="beat_039", reason="emotional peak: Qasim holds his granddaughter; the three together — reconciliation",
         chars=["qasim_old", "zeeva", "shima_older"], loc="beach_sunset",
         visual=f"old Qasim, kneeling again on one knee, holding little Zeeva (pale-yellow dress, {HIJ_Z}) in a gentle hug, his eyes closed and tears of relief on his face; Shima in her camel-brown coat dress and {HIJ_O} kneeling beside them with her hand on her father's shoulder and her other hand on Zeeva's back, smiling through tears; the three close together, the last golden sunset glow behind them",
         camera="medium close shot, eye level, the three faces in the upper half, the paving as the lower third",
         amb="beach_dusk", sens="other", safe="embrace only between mahram family: grandfather holds granddaughter, Shima's hand on her father's shoulder; fully clothed, tender"),
    # ---- ending
    dict(to=91, v1="beat_040", reason="time change: the sun sets and the calm of night spreads; the storm of her life is over",
         chars=["shima_older", "zeeva", "qasim_old"], loc="beach_dusk",
         visual=f"seen from behind, the three walk slowly along the seafront walkway into the blue dusk: Shima in her camel-brown coat dress and {HIJ_O}, little Zeeva in her pale-yellow dress and {HIJ_Z} in the middle holding hands with both, old white-haired Qasim leaning on his cane; warm street lamps, the calm lagoon, the last pink glow on the horizon",
         camera="medium wide from behind, the figures in the upper-middle, the lamp-lit paving as the lower third",
         amb="beach_evening"),
    dict(to=93, v1="beat_041", reason="emotional close: the tears of pain have become tears of happiness",
         chars=["shima_older"], loc="beach_dusk",
         visual=f"close-up of Shima in {HIJ_O} at blue dusk, a single tear of joy on her cheek and a serene, radiant smile, eyes lifted to the clearing sky; warm lamp light on her face, the soft lights of Male behind",
         camera="close-up, eye level, her face in the upper half, the dark blurred sea below",
         amb="beach_evening"),
    dict(to=94, v1="beat_042", reason="ending: a peaceful dusk — the beginning of a happiness that never ends (The End)",
         loc="beach_dusk",
         visual="a peaceful wide view of the calm lagoon at dusk: a deep violet-blue sky with the first star, a last thin line of pink on the horizon, the still water reflecting the glow, the empty wooden bench under a warm street lamp on the walkway; no people",
         camera="wide shot, the sky in the upper two-thirds, the still water and paving as the lower third",
         amb="beach_evening"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Mother's beloved child...\" One morning, sitting on the joali in the yard, Shima stroked her belly with her hand and spoke quietly to herself.",
   [("creak", "ޖޯލީގައި", -24)])
sh(2, "\"Mother has committed a very great wrong. But you will be born a pure child, without any sin.", speaker="shima")
sh(3, "Mother will find you the happiest life in the world. I will protect you from people's blame and hatred.", speaker="shima")
sh(4, "Even if it costs Mother her life, I will build you a good future.\"", speaker="shima")
sh(5, "With this strong resolve, Shima kept waiting for the happy moment when that child, who would bring a new light into her life, would draw its first breath in the world.")
sh(6, "As the pains in her belly began and the time of labour drew near, there was no fear in her heart. There was only hope and courage.",
   [("breath_heavy", "ރިއްސަން", -22)])
sh(7, "With Aisamanike's kindness and help, she had begun to trust herself. And in her heart was the certainty")
sh(8, "that, with Allah's mercy, after these hard days a happy dawn would come for her and her child.")
sh(9, "Awaiting that dawn, Shima stood firm with courage, her heart filled with the noble love of motherhood.")
sh(10, "In the cold hospital room echoed the steady, even sound of the heart-monitor machine.",
   [("heart_monitor", "މެޝިނުގެ", -18)])
sh(11, "Through the strong white light fixed to the room's ceiling, all Shima's eyes could see was a blur.")
sh(12, "Because of the fierce pain coursing through her whole body, her breath had grown short.",
   [("breath_heavy", "ނޭވާ", -20)])
sh(13, "As beads of sweat ran from her forehead in a line down her cheeks, her spine ached from how hard she clenched her teeth.")
sh(14, "This was the greatest physical pain she had ever borne in her life. Yet even through this pain, what kept coming back to her was the grief and loneliness she had carried through the past nine months.",
   hum=True)
sh(15, "The memory of being cast out by her own family and thrown onto the street on the day she needed them most. Her father's harsh words, and the blame society heaped upon her.",
   hum=True)
sh(16, "All of it, together with the labour pain she bore today, sent a flood of tears streaming from her eyes. Shima —",
   [("sob_breath", "ކަރުނައިގެ", -22)])
sh(17, "so very brave. Now only the very last moment remained. Drawing a deep breath, she pushed...",
   [("breath_heavy", "ނޭވާއެއް", -20)])
sh(18, "The experienced nurse beside her held Shima's hand tenderly and gave her courage. Shima shut her eyes tight.")
sh(19, "Gathering the last strength left in her body, with a deep breath she poured out all her courage.",
   [("breath_heavy", "ނޭވާއަކާއެކު", -20)], hum=True)
sh(20, "This was not merely the strength she used to bring a child into the world. It was the strength she used to escape her hard past and breathe into a new life.")
sh(21, "A step taken out of the darkness of the past, toward the light of hope. Suddenly the silence of the whole room was broken by the loud, clear cry of a tiny baby.",
   [("gasp", "ކުއްލިއަކަށް", -22)], hum=True)
sh(22, "As that sound reached her ears, it was as if all the pain pressing on Shima's body vanished in a single second.")
sh(23, "A deep rest came over her exhausted body. The tears running down her face kept flowing without stopping — this time not because of pain,",
   [("sigh", "އަރާމެއް", -22)])
sh(24, "but out of utmost happiness and gratitude. After cleaning the baby, the nurse brought that tiny soul and laid her on Shima's chest.",
   [("cloth_rustle", "ބޭއްވި", -24)])
sh(25, "The moment that soft, warm little body touched Shima's skin, she felt as if all the joy in the world had come to her at once.",
   hum=True)
sh(26, "Looking at those tiny hands and that innocent face, by the strength of the motherly love born in Shima's heart, she completely forgot all her past grief.")
sh(27, "\"Mother's little Zeeva...\" Sobbing softly, Shima kissed her tiny child's forehead.",
   [("sob_breath", "ގިސްލަމުން", -22)], hum=True, speaker="shima")
sh(28, "From this day on, the course of her life changed. This child was her new world. All her hope was this little soul.")
sh(29, "At that moment Shima made a strong promise to herself and to the tiny child lying on her chest: a promise never to let any sorrow reach this child, and for this child to fight every force in the world.")
sh(30, "A noble pledge that, just as she had been lonely, she would never let this child be lonely. The days passed quickly.")
sh(31, "Shima's life began from zero. In a tiny rented room, raising her child all alone, she lived in great hardship.")
sh(32, "Most nights were nights robbed of sleep. Through Zeeva's illnesses and crying, Shima shed tears on many a night.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(33, "There were not a few days when, without a single coin in hand, she went hungry herself and bought a tin of milk for her child with her last rufiyaa.")
sh(34, "She faced the evil looks of some in society, and the challenges of living as an unmarried, lone mother, with the utmost patience.")
sh(35, "Every time her courage was about to give way, Zeeva's tiny palm touching her face, or the sight of that innocent smile, gave Shima's body new life.",
   hum=True)
sh(36, "Zeeva was her healing. She was the only reason she was alive. With a firm resolve to give her child a good future, Shima began to go out to work.")
sh(37, "She started with the lowest-level job in an ordinary small office. After leaving Zeeva at a daycare, Shima worked hard at the office from morning to evening.",
   [("paper_shuffle", "މަސައްކަތްކުރޭ", -24)])
sh(38, "It did not take many days for the bosses at the office to notice her sincerity, honesty and care for her work.")
sh(39, "At night, after putting her child to sleep, Shima did extra training and worked on her own progress. Her every breath was bound to success.",
   [("page_turn", "ތަމްރީނުތައް", -24)])
sh(40, "Her goal was to become a woman standing on her own feet, never needing anyone's help.")
sh(41, "In this way seven years went by. After that long, hard journey of seven years, today Shima holds a senior position in a successful company —")
sh(42, "a strong woman, accepted by society, respected, and standing on her own feet. Instead of the tiny room of old, today she lives in a spacious, beautiful apartment.")
sh(43, "From every corner of that home you see the signs of Zeeva's happiness: Zeeva's drawings on the walls and the toys in the sitting room.")
sh(44, "Seven-year-old Zeeva is a clever, pretty and well-mannered child. Growing up in the shelter of her mother's boundless love, Zeeva's face always shines with brightness and joy.")
sh(45, "This revolutionary change in Shima's life is not just financial comfort. It is the freedom and peace of mind she found within herself.")
sh(46, "The painful tears of the past have turned today into a proud smile. A lovely afternoon.")
sh(47, "As the sun was setting, the golden rays spreading across the sky adorned the Malé artificial beach.",
   [("wave_crash", "ބީޗް", -26)])
sh(48, "Shima and Zeeva were sitting on a bench near the sea. Zeeva had an ice-cream cup in her hand, and she was laughing as she told some funny story.")
sh(49, "Seeing her child's smile, Shima's heart was full. Just then, Shima's eyes caught someone approaching from afar. The person walked very slowly.",
   [("footsteps_pavement", "ހިނގުން", -22)])
sh(50, "Leaning on the cane in his hand, it seemed every single step forward took great effort.")
sh(51, "The hair on his head had turned completely white; his body was dried up, thin and stooped. When the man came and stopped right beside Shima and her daughter, it was as if Shima's heart stopped for a second.",
   [("heartbeat", "ވިންދު", -20)], hum=True)
sh(52, "It was no one else. It was her father, Qasim. The father who, years ago, with pride and arrogance, had thrown her out onto the street.",
   hum=True)
sh(53, "But today not a trace of that harshness could be seen on his face. On that face were only deep despair and the marks of sorrow.")
sh(54, "Her father's eyes were full of tears. Qasim's gaze rested first on Shima's face,")
sh(55, "then on the face of the lovely seven-year-old Zeeva sitting beside her. In that little girl's features he saw the features of his own daughter Shima as a child.")
sh(56, "His own blood. Shima sat frozen. All the dark pages of the past played in her mind like scenes from a film.",
   [("heartbeat", "ގަނޑުވެފަ", -22)])
sh(57, "The sound of that house's gate being slammed shut and locked on the rainy night seemed to ring in her ears again. Shima slowly stood up.",
   [("rain_start", "ވާރޭ", -22), ("metal_gate", "ލައްޕާލި", -16)], hum=True)
sh(58, "Zeeva, too, holding her mother's hand, stood looking in wonder at the unknown old man in front of them. \"Shima...\"")
sh(59, "Qasim's voice came out with great difficulty, trembling and faltering. The cane slipped from his hand and fell to the ground.",
   [("soft_thud", "ވެއްޓުނު", -16)])
sh(60, "With that, Qasim suddenly dropped to his knees in front of Shima. Hiding his face in both hands, he began to sob and cry like a little child. \"My child...",
   [("cloth_rustle", "ކަކޫމައްޗަށް", -22), ("sob_breath", "ގިސްލާ", -20)], hum=True)
sh(61, "forgive your father... Today your father has realised how great a wrong he committed...", speaker="qasim_old", hum=True)
sh(62, "Out of fear of what society might say, your father's own blood,", speaker="qasim_old")
sh(63, "his own child — for throwing her out onto the street on the day she needed him most, your father today regrets it beyond measure...\"", speaker="qasim_old")
sh(64, "Tears gathered in Shima's eyes. She stood not knowing what to say. Qasim, still weeping, went on: \"That day your father",
   [("sob_breath", "ރޮމުން", -24)])
sh(65, "threw you out without any mercy. Your father thought your life would be ruined.", speaker="qasim_old")
sh(66, "But... but today your father sees a different sight. Here you are,", speaker="qasim_old")
sh(67, "standing on your own feet, a strong woman. Even without your father, you have found success.", speaker="qasim_old")
sh(68, "When your father saw you today... when he saw that little angel of a granddaughter, your father's heart feels as if it will break.",
   [("sob_breath", "ފަޅައިގެންދާ", -22)])
sh(69, "Your father did not come because he has any right... only to ask for your forgiveness...\"",
   hum=True)
sh(70, "A powerful storm rose inside Shima. On one side, the ache of the deep wounds she had received in the past. The loneliness and hunger of those nights.")
sh(71, "But on the other side, the tenderness of motherhood grown in her heart. She looked down.")
sh(72, "She looked into the innocent eyes of Zeeva, who was holding her hand. In Zeeva's eyes there was only kindness. Shima understood.")
sh(73, "Carrying the hatred and anger of the past in her heart would only cast a shadow over the happy, peaceful life she lives now.")
sh(74, "Even though her father had treated her in the worst way that day, she accepted that it was because of it that she had gained this strength today.")
sh(75, "And more than that, she wanted to show her child the beautiful example of forgiveness. She did not want to pour the poison of hatred into Zeeva's life.")
sh(76, "Shima slowly knelt down and laid her hand on her father's shoulder. Startled, Qasim raised his head. Though tears flowed from Shima's eyes, her face was calm.",
   [("cloth_rustle", "ތިރިވެ", -24), ("gasp", "ސިހިފައި", -22)], hum=True)
sh(77, "\"Father...\" Instead of the hurt once in Shima's voice, today there was tenderness. \"Father, you don't need", speaker="shima_older")
sh(78, "to ask me for forgiveness. It's true that the way you treated me that day left", speaker="shima_older")
sh(79, "very deep scars in my heart. So many nights I cried, remembering you,", speaker="shima_older")
sh(80, "longing for your love. But... today there is no heaviness, no anger at all in my heart.", speaker="shima_older")
sh(81, "If you had not let me go that day, I would never have known the strength within myself.", speaker="shima_older")
sh(82, "I am not forgiving only you... For my own peace of mind,", speaker="shima_older")
sh(83, "I have forgiven the whole past.\" Qasim's eyes widened.", speaker="shima_older", hum=True)
sh(84, "Seeing his daughter's kindness and nobility, his heart wept all the more. Shima took her father's hand and raised him to his feet.",
   [("cloth_rustle", "ނެގި", -24)])
sh(85, "Then, looking at Zeeva beside her, she smiled. \"Zeeva... this is your grandfather,\" Shima said.", speaker="shima_older")
sh(86, "Though little Zeeva hung back at first, at the smile on her mother's face she stepped forward and wrapped her arms around Qasim's leg.",
   [("footsteps_pavement", "ޖެހިލައި", -24)])
sh(87, "Qasim held his granddaughter close in his arms. The guilt and remorse he had hidden in his heart for so many years seemed to wash away in a single moment.",
   hum=True)
sh(88, "As the three of them held each other, this was a moment of reconciliation come after years of pain.",
   hum=True)
sh(89, "As the sun's last rays vanished over the horizon and the calm of night began to spread, today there was no fear at all in Shima's heart.",
   [("wave_crash", "އުދަރެހުން", -26)])
sh(90, "The anguish her father bore for the wrong he committed has faded away. The scars of the past in Shima's heart have fully healed.")
sh(91, "The storm that struck her life has come to an end, and today the sky of her life is clear.")
sh(92, "The tears of pain she shed for so many days have today turned into tears of happiness and complete success.",
   hum=True)
sh(93, "With the pure, clear love of motherhood her life has become bright, bringing peace and joy to her whole life.")
sh(94, "It is the beginning of a happiness that will never end. The End.")

SHOTS = S

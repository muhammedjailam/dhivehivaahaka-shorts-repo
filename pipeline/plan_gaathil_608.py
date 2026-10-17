"""Beat/shot plan for Gaathil episode 608 (Shahid's night + Ibrahim/Adam flashback; used by plan_beats.py)."""

LOC = {
    "room_night": "Shahid's room in an old coral-stone island house at night: a wooden desk with a computer and a big monitor, a desk lamp, camera gear and lenses on a shelf, a closed window with old wooden shutters, rough whitewashed coral-stone walls",
    "photo_sea": "a grainy night photograph shown full frame: the black open sea off the island at night, far out near the horizon a small old wooden fishing dhoni seen from behind, a tiny dark silhouette of a man standing at its helm",
    "imagined_shop": "a small old island shop in Shahid's imagination: a narrow wooden counter, shelves of sacks of rice and sugar, tins and bunches of bananas, an open doorway onto a sunlit sandy lane",
    "imagined_harbour": "the island harbour in Shahid's imagination: an old coral-stone quay, moored wooden fishing dhonis, sacks and crates stacked on the quay, coconut palms behind",
    "memory_lane": "the home island twenty years ago at night: a narrow sandy lane between crumbling whitewashed coral-stone walls, coconut palms, and far away at the end of the lane the old club warehouse with a small crowd of islanders holding lanterns at a distance",
    "memory_shore": "a dark lonely corner of the home island's shore twenty years ago at night: wet sand, black water, a small wooden rowing boat pulled up at the waterline, leaning coconut palms",
    "far_arrival": "the sea in another atoll at dawn: a small wooden dhoni gliding towards a lonely, sparsely populated island with a quiet little harbour, a few fishing dhonis and low houses among coconut palms",
    "far_sea": "the open sea off the remote island: a small open wooden fishing boat on deep blue water, the low green island far behind",
    "far_lane": "the remote island's quiet sandy shore lane: whitewashed low coral-stone houses with wooden doors, coconut palms, fishing nets drying on poles, the bright lagoon beyond",
    "nikah_room": "the front room of a modest island house on the remote island: plain whitewashed walls, a woven mat spread on the floor, a low tray with two cups of tea and a plate of sweets, an open wooden window with daylight",
    "far_room_night": "a small dark bedroom-side room of Adam's house on the remote island at night: a wooden window with half-open shutters, moonlight falling in, plain walls",
    "far_yard_night": "the sandy yard behind Adam's small house on the remote island at night: a coconut palm, a low coral-stone wall, the dark sea glimmering beyond",
    "storm_symbol": "a stormy open sea: huge dark waves, a small empty wooden boat tossed and tilting on the swell, a low black sky",
    "far_house_lamp": "the inside of Adam's small house on the remote island late at night: a single oil lamp on a low table, plain whitewashed walls, a wooden door, a cloth bundle and a small bag half packed",
    "launch_night": "the pitch-black open sea at night: a small open launch crossing the water, a tiny lantern glow, the black silhouette of an island ahead",
    "jungle_night": "the most isolated part of the home island's jungle at night: dense big screw-pines with stilt roots, thick magoo shrubs, tangled undergrowth, a narrow trodden path",
    "hatch_clearing": "a hidden spot deep in the jungle at night: big screw-pines and magoo shrubs closing in around a patch of bare sand where an old rusted square iron hatch is set in the ground",
    "bunker": "a small underground bunker room: rough concrete walls, a single dim bare electric bulb hanging from the ceiling, a plain wooden table and chair, a narrow iron cot with a thin mattress, stacked sealed cardboard food boxes, stacks of blank old papers and plain folders, an iron ladder leading up to a hatch",
}
MOOD = {
    "room_night": "night, room lit by a single warm desk lamp and the cold blue-white glow of the monitor, deep charcoal shadows, tense and quiet",
    "photo_sea": "night photograph: near-black blue-grey sea and sky, grainy, desaturated, faint silver reflections, unsettling",
    "imagined_shop": "hazy imagined daylight, soft pale-gold glow with blurred dreamlike edges and a faint vignette, quietly suspicious",
    "imagined_harbour": "hazy imagined overcast daylight, soft grey-gold glow with blurred dreamlike edges and a faint vignette, quietly suspicious",
    "memory_lane": "sepia memory of twenty years ago at night: faded brown-gold tones, distant warm lantern points, deep shadows, haze, fear",
    "memory_shore": "sepia memory of twenty years ago at night: faded brown-grey tones, faint moonlight on the water, secretive and tense",
    "far_arrival": "pale dawn, soft sea-blue and warm peach light, calm water, quiet and lonely new beginning",
    "far_sea": "bright sea-blue day, strong sunlight, glittering water, lonely",
    "far_lane": "bright warm sea-blue afternoon, soft sunlight, gentle and kind",
    "nikah_room": "warm soft daylight, gentle and modest, a quiet happy occasion",
    "far_room_night": "pitch-dark night, only a thin cold moonlight through the shutters, deep black shadows, lonely and sorrowful",
    "far_yard_night": "dark night, cold moonlight, a faint grey glow, sudden dread",
    "storm_symbol": "storm, near-black blue-grey, white spray, turmoil",
    "far_house_lamp": "late night, warm flickering oil-lamp light, long shadows, urgent and uneasy",
    "launch_night": "pitch-black sea night, almost no light, one tiny warm lantern point, cold and ominous",
    "jungle_night": "green-black jungle night lit only by a single torch beam, deep black shadows, frightening",
    "hatch_clearing": "green-black jungle night, a torch beam cutting into a dark opening, ominous",
    "bunker": "dim yellow light of a single bare bulb, heavy dark shadows in the corners, claustrophobic and secretive",
}

MARI = "Mariyam in her loose long-sleeved ankle-length dusty-rose dress with her cream hijab fully covering her hair and neck"
MASK = ("a soft, flesh-toned theatrical silicone face mask like a film-studio prop (clearly a rubbery prop object, "
        "no blood, nothing gory)")

BEATS = [
    # ---- present: Shahid's room at night ----
    dict(to=2, reason="episode opening: Shahid at night at his desk with the silicone mask, gripping the mouse", chars=["shahid"], loc="room_night",
         visual=f"Shahid sitting at his desk at night, leaning forward, holding {MASK} loosely in his left hand and staring at it with narrowed suspicious eyes; his right hand grips the computer mouse hard; the monitor glows cold blue-white beside him showing only a dark photo, the warm desk lamp lights his face from one side",
         camera="medium shot from the side of the desk, eye level, Shahid's face and the mask in the upper two-thirds, the dark desk top as the lower third",
         amb="home_night"),
    dict(to=4, reason="scene change: full-frame view of another night photo — a fishing dhoni far out at sea, a figure at the helm", loc="photo_sea",
         visual="a dark grainy night photograph filling the frame: the black sea under a near-black sky, far out near the horizon a small old wooden fishing dhoni seen from behind, a tiny dark silhouette of a lean man standing at its helm, a faint silver glint on the water; no interface, no text, no registration on the boat",
         camera="full-frame photograph, the dhoni in the upper-middle third, the black water as the lower third",
         amb="home_night", transition="dissolve"),
    dict(to=5, reason="return to Shahid at the desk: the realisation that Ibrahim lives in disguises", loc="room_night",
         reuse="beat_001", chars=["shahid"], amb="home_night", transition="dissolve", visual="(reuse of beat_001)"),
    dict(to=7, reason="imagination: Shahid pictures Ibrahim as an old bearded man buying goods at a shop", loc="imagined_shop",
         visual="a hazy dreamlike imagined scene: a lean stooped old man with a long grey beard, a white skullcap and a loose faded kurta and sarong standing at the wooden counter of a small island shop, paying for a sack of rice, glancing sideways with wary deep-set eyes; the shopkeeper a soft blur behind the counter; blurred dreamy edges",
         camera="medium shot, eye level, the old man's face in the upper third, the worn counter as the lower third",
         amb="memory", transition="dissolve", sens="other",
         safe="Shahid's imagined disguises are generic figures without a character card, shown in a hazy imagined look"),
    dict(to=9, reason="imagination: a young fisherman and a foreign labourer on the harbour — nobody recognises him", loc="imagined_harbour",
         visual="a hazy dreamlike imagined scene on the island harbour: in front a lean labourer in a dusty work shirt and cap carrying a sack on his shoulder along the quay, head lowered; behind him a young fisherman in a plain t-shirt coiling a rope on a moored wooden dhoni; islanders pass by without looking at them; blurred dreamy edges, no lettering on boats",
         camera="medium-wide, eye level, the labourer in the upper-middle third, the stone quay as the lower third",
         amb="memory", sens="other",
         safe="the disguises are generic figures without a character card, in a hazy imagined look"),
    dict(to=11, reason="return to Shahid at the desk (out of imagination); the message arrives", loc="room_night",
         reuse="beat_001", chars=["shahid"], amb="home_night", transition="dissolve", visual="(reuse of beat_001)"),
    dict(to=14, reason="action change: Shahid opens the threatening message with a trembling hand", chars=["shahid"], loc="room_night",
         visual="close-up of Shahid at the desk holding a phone up with a trembling hand, the phone's back turned to the viewer so the screen is not visible, its soft white glow lighting his frightened face from below; eyes wide, lips parted, breath held; on the desk beside the keyboard in the lamp light lies the flesh-toned silicone full-face disguise mask from the previous scene (a rubbery human-face prop with eye holes, nose and lips, like a film-studio prop; NOT a medical or surgical mask)",
         camera="medium close-up, eye level, Shahid's face in the upper half, the phone and the desk top below",
         amb="home_night", sens="other", safe="the message is never readable: only the phone's glow on his face"),
    dict(to=17, reason="emotional change: wide view — Shahid frozen alone in the dark room, questions without answers", chars=["shahid"], loc="room_night",
         visual="a wide, dark view of the room: Shahid sitting hunched and motionless at his desk, staring down at the glowing phone in his hands (screen facing away), the desk lamp a small warm pool of light, the monitor dimmed, the closed wooden shutters and deep black shadows filling the room around him",
         camera="wide shot from the corner of the room, slightly high angle, Shahid in the upper-middle third, the dark floor as the lower third",
         amb="home_night"),
    # ---- flashback: Ibrahim's memories ----
    dict(to=19, reason="flashback (time jump): twenty years ago, young Ibrahim flees in fear", chars=["ibrahim_young"], loc="memory_lane",
         visual="sepia memory: young Ibrahim hurrying along a dark sandy lane between crumbling coral-stone walls at night, glancing back over his shoulder with desperate frightened eyes, breathing hard; far behind him at the end of the lane the old club warehouse with a small crowd of islanders holding lanterns at a distance",
         camera="medium-wide, eye level, Ibrahim's face in the upper third, the dark sand of the lane as the lower third",
         amb="memory", transition="dissolve", sens="violence",
         safe="the murder is never shown: only the distant warehouse with lanterns and the fleeing man"),
    dict(to=21, reason="character change: young Amjad gives young Ibrahim his secret advice (Amjad speaks)", chars=["amjad_young", "ibrahim_young"], loc="memory_shore",
         visual="sepia memory on the dark shore at night: young Amjad in his navy police shirt standing close, leaning in and speaking low with a hard, commanding look, pointing out to sea; young Ibrahim beside him at the side listening, frightened and exhausted; a small rowing boat at the waterline behind them",
         camera="medium two-shot, eye level, Amjad centred and sharp in the upper half, Ibrahim softer at the side, wet sand as the lower third",
         amb="memory", speaker="amjad_young"),
    dict(to=23, reason="scene change: Ibrahim lands on a lonely island in another atoll", chars=["ibrahim_young"], loc="far_arrival",
         visual="young Ibrahim standing at the bow of a small wooden dhoni seen from behind, his face not visible, looking at a lonely low island with a quiet little harbour and coconut palms in the pale dawn; calm sea-blue water; no lettering on the boat",
         camera="wide shot from behind, the island and Ibrahim's silhouette in the upper two-thirds, the calm water as the lower third",
         amb="sea_boat"),
    dict(to=26, reason="character/scene change: as 'Adam', the masked quiet fisherman, alone at sea every day", chars=["adam"], loc="far_sea",
         visual="Adam alone in a small open wooden fishing boat on the bright blue sea, sitting at the stern holding a hand line, his sleeves rolled up, his calm handsome face clouded with a distant, troubled look towards the horizon; the low green island far behind",
         camera="medium shot, eye level, Adam's face in the upper half, the boat's wooden floor and the water as the lower third",
         amb="sea_boat"),
    dict(to=29, reason="character change: Adam meets Mariyam, whose kindness ends his loneliness", chars=["mariyam", "adam"], loc="far_lane",
         visual=f"on the sunny sandy shore lane {MARI} standing at a respectful distance offering Adam a small covered basket of food with a kind, shy smile; Adam facing her, carrying fishing nets over his shoulder, his calm face softening into a gentle smile; houses with nets drying and palms behind",
         camera="medium two-shot, eye level, both faces in the upper half, the bright sand as the lower third",
         amb="village_day", sens="intimacy", safe="before marriage: only a kind exchange at a respectful distance"),
    dict(to=31, reason="scene/time change: the modest nikah — the marriage is tied without obstacle", chars=["mariyam", "adam"], loc="nikah_room",
         visual=f"a modest nikah in a simple island house: Adam and {MARI} sitting side by side on a woven mat with a little space between them, her henna-decorated hands resting in her lap; two cups of tea on a low tray before them; an elderly man in a white shirt and cap and two elderly women in hijabs sitting around them, smiling quietly",
         camera="medium-wide, eye level, the couple's faces in the upper half, the mat and tea tray as the lower third",
         amb="island_house_day", sens="intimacy",
         safe="the wedding is a modest nikah: seated families, henna hands, two cups; the couple side by side without touching"),
    dict(to=34, reason="action/time change: every night Adam secretly removes the mask in the dark", chars=["adam"], loc="far_room_night",
         visual="Adam standing alone by a dark window at night, seen from behind, only a thin cold line of moonlight on his shoulder, one hand raised to his face near the jaw; his face is not visible; the room around him pitch dark",
         camera="medium shot from behind, Adam's silhouette in the upper two-thirds, the dark floor as the lower third",
         amb="island_house_night", sens="intimacy",
         safe="no bed and no couple: Adam alone, from behind, by the window; no mask removal shown"),
    dict(to=36, reason="time jump (two years later): Amjad's call on the secret phone shatters the new life", chars=["adam"], loc="far_yard_night",
         visual="Adam standing in the dark sandy yard behind his house at night, holding a plain old black phone to his ear, his face tense and pale with dread, his free hand clenched; a coconut palm and the dim moonlit sea behind; the house's window dark",
         camera="medium close-up, eye level, Adam's face centred in the upper half, the dark sand as the lower third",
         amb="island_night", transition="black"),
    dict(to=38, reason="symbolism: life tossed like a boat in a storm", loc="storm_symbol",
         visual="a small empty wooden boat tossed and tilting on huge dark storm waves under a low black sky, white spray flying; no people, no lettering",
         camera="wide shot, eye level, the boat in the upper-middle third, dark churning water as the lower third",
         amb="storm_night"),
    dict(to=40, reason="action/scene change: one night Adam tells Mariyam they must leave at once (Adam speaks)", chars=["adam", "mariyam"], loc="far_house_lamp",
         visual=f"inside the small house by oil-lamp light: Adam standing centred, speaking urgently and low, one hand raised, his calm face tense; {MARI} at the side holding a folded cloth, looking at him with worried, questioning eyes; a half-packed bag on the floor",
         camera="medium two-shot, eye level, Adam centred and sharp in the upper half, Mariyam softer at the side",
         amb="island_house_night", speaker="adam"),
    dict(to=42, reason="reverse shot: Mariyam, uneasy but trusting, decides to follow him", chars=["mariyam", "adam"], loc="far_house_lamp",
         visual=f"{MARI} in the oil-lamp light tying a cloth bundle, her face anxious but trusting, looking up towards Adam; Adam soft and out of focus at the side of the frame",
         camera="medium close-up, eye level, Mariyam centred in the upper half, the bundle and the low table as the lower third",
         amb="island_house_night", transition="cut"),
    dict(to=45, reason="scene/time change: on a small launch across the pitch-black sea to the island of his past", loc="launch_night",
         visual="a small open launch crossing the pitch-black sea at night, seen from a distance: two small figures sitting close in it — a man in a light shirt and a woman in a dusty-rose dress and cream hijab fully covering her hair — lit only by one tiny lantern; ahead the black silhouette of an island; no lettering on the boat",
         camera="wide shot, the launch in the upper-middle third, the black water as the lower third",
         amb="sea_boat", transition="black"),
    dict(to=47, reason="scene change: into the frightening jungle; Mariyam, afraid, asks where they are going (Mariyam speaks)", chars=["mariyam", "adam"], loc="jungle_night",
         visual=f"in the dark jungle at night {MARI} centred, frightened, speaking with wide eyes, one hand gripping Adam's arm; Adam beside her at the side holding a torch whose beam cuts through dense screw-pines and magoo shrubs ahead",
         camera="medium two-shot, eye level, Mariyam centred and sharp in the upper half, Adam at the side, the dark path as the lower third",
         amb="jungle_night", speaker="mariyam", sens="intimacy", safe="married couple: only her hand gripping his arm"),
    dict(to=49, reason="reverse shot: Adam, despairing, tells her to be quiet — safety is here (Adam speaks)", chars=["adam", "mariyam"], loc="jungle_night",
         visual=f"Adam centred, turned towards Mariyam, speaking in a low strained whisper with despair in his eyes, the torch in his hand lighting the screw-pine leaves; {MARI} at the side of the frame, softer, still gripping his arm",
         camera="medium close-up, eye level, Adam centred and sharp in the upper half, Mariyam soft at the side",
         amb="jungle_night", speaker="adam", transition="cut"),
    dict(to=51, reason="action change: Adam opens the iron hatch onto a dark underground bunker; Mariyam's eyes widen", chars=["adam", "mariyam"], loc="hatch_clearing",
         visual=f"Adam crouching and heaving open an old rusted square iron hatch raised from the sandy ground among big screw-pines, the torch beam shining down into a black shaft with an iron ladder; {MARI} standing just behind him, her eyes wide with shock, a hand at her chest",
         camera="medium-wide, slightly low angle, faces in the upper half, the open hatch and sand as the lower third",
         amb="jungle_night"),
    dict(to=53, reason="scene change: the small bunker room with electricity, papers and sealed food boxes", chars=["mariyam", "adam"], loc="bunker",
         visual=f"{MARI} standing at the foot of the iron ladder inside the small bunker room, looking around in astonishment under the single dim bare bulb; a plain table with stacks of blank papers and plain folders, sealed cardboard food boxes stacked against the wall, a narrow iron cot; Adam at the side setting down a bag, his back half turned",
         camera="medium-wide, eye level, Mariyam's face in the upper half, the concrete floor as the lower third",
         amb="storeroom"),
    dict(to=54, reason="time jump: the second night — Mariyam wakes and sees Adam at the table", chars=["mariyam", "adam"], loc="bunker",
         visual=f"{MARI} half-sitting up on the narrow iron cot under a shawl, fully dressed, just woken, her eyes opening wide; far across the dim room Adam sits at the table under the bare bulb, seen from behind and to the side, one hand on his face",
         camera="medium-wide from the cot, Mariyam in the foreground at one side, Adam small at the table in the background, the floor as the lower third",
         amb="storeroom", transition="black", sens="intimacy",
         safe="'lying asleep' becomes Mariyam half-sitting fully dressed with hijab on the cot; Adam far across the room"),
    dict(to=55, reason="action change: at the table Adam's hand moves to the edge of his jaw near the ear", chars=["adam"], loc="bunker",
         visual="Adam seen in profile from slightly behind, sitting at the table under the dim bulb, his fingers resting at the edge of his jaw just below the ear as if loosening something; his face mostly in shadow; the papers and a tin cup on the table",
         camera="medium close-up in profile, his head and hand in the upper half, the table top as the lower third",
         amb="storeroom", sens="other", safe="no skin peeling shown: only his hand at his jaw near the ear in dim light"),
    dict(to=56, reason="reaction: Mariyam covers her mouth to stop a scream", chars=["mariyam"], loc="bunker",
         visual=f"close-up of {MARI} half-sitting on the cot under her shawl, both hands pressed over her mouth, eyes wide with terror, holding her breath; dim yellow bulb light on one side of her face, deep shadow behind",
         camera="close-up, eye level, her face in the upper half, the shawl as the lower third",
         amb="storeroom"),
    dict(to=57, reason="the reveal: the real face of the man at the table — a different, ageing face", chars=["ibrahim"], loc="bunker",
         visual=f"Ibrahim's real face revealed at the table under the dim bare bulb: gaunt, weathered, grey stubble, untidy grey-black hair, deep-set sad tired eyes, an ordinary ageing man; he wears Adam's faded sky-blue long-sleeved shirt (NOT the brown coat); on the table in front of him lies {MASK}, flat and empty",
         camera="medium close-up, eye level, his face in the upper half, the table and the prop mask as the lower third",
         amb="storeroom", sens="other",
         safe="the mask is a soft prop lying on the table; his real face is ordinary, weathered and sad — not monstrous, not ghostly"),
    dict(to=58, reason="return to Mariyam frozen, holding her breath: who did she marry?", loc="bunker",
         reuse="beat_027", chars=["mariyam"], amb="storeroom", transition="cut", visual="(reuse of beat_027)"),
    dict(to=59, reason="detail: her eyes fixed on the table where her husband's 'face' lies — the silicone mask", loc="bunker",
         visual=f"a close detail of the wooden table top under the dim yellow bulb: {MASK} lying crumpled and flat beside a tin cup and a stack of blank papers; soft shadows; no person in the shot",
         camera="close-up from a low angle across the table, the mask in the middle third, the dark wood as the lower third",
         amb="storeroom", sens="other", safe="the mask is shown only as a soft rubbery film prop on the table"),
    dict(to=60, reason="return to the real face at the table; all strength drains from Mariyam", loc="bunker",
         reuse="beat_028", chars=["ibrahim"], amb="storeroom", transition="cut", visual="(reuse of beat_028)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"That is a mark of the kind used only in films, or by foreign secret spy agencies that prepare high-grade equipment for special missions.\"")
sh(2, "\"How did Ibrahim Naseem get something like this?\" Shahid asked himself. He sat gripping the mouse with a forceful hand.")
sh(3, "And he began looking through the other photos he had taken that night too. In the corner of another photo, the stern of a fishing dhoni sailing far off came into view.")
sh(4, "When he compared the build of the man at that dhoni's helm with the build of the old man who had run away from in front of him today, he noticed they were almost the same.")
sh(5, "It suddenly turned over in Shahid's mind that Ibrahim Naseem is not someone who lives only in the guise of an old man. People like that live by changing their appearance.")
sh(6, "In his imaginary world he sketched pictures of Ibrahim Naseem in all kinds of different forms.")
sh(7, "One day buying goods from the island's shops in the guise of an old man wearing a long beard; another day living in the guise of an ordinary young fisherman.")
sh(8, "Sometimes he may even live in the guise of a foreign labourer working on the harbour. That is why,")
sh(9, "the man who went missing twenty years ago, even while living before the eyes of the islanders, could not be recognised by a single person as Ibrahim.")
sh(10, "Shahid wondered about something else. For what secret is Ibrahim, disguised, trying to meet the people who use those warehouses all over the island?")
sh(11, "What is the truth he is trying to hide? At that very moment, a message came to Shahid's phone from an unknown number.",
   [("phone_buzz", "މެސެޖެއް", -18)])
sh(12, "With a trembling hand he picked up the phone and opened the message. Written in it was a frightening line: \"That mask in your hand",
   [("heartbeat", "ތެޅެމުންދިޔަ", -22)], hum=True)
sh(13, "could become your death sentence. Don't try to find out its secret!", hum=True)
sh(14, "If Amjad sees it, that night will be the last night you ever spend in this world!\" Shahid's breath stopped.",
   [("gasp", "ނޭވާ", -18)], hum=True)
sh(15, "Did Ibrahim Naseem himself send this message? How did he know Shahid's number? And what did he mean by what he said about Amjad?")
sh(16, "Questions, all of them without answers. Sitting there staring at the phone's screen, Shahid's heart was drifting in an ocean of unease.")
sh(17, "\"If Amjad sees it, that night will be the last night you ever spend in this world!\" That frightening line kept repeating in his mind.",
   [("heartbeat", "ތަކުރާރުވަމުންދިޔަ", -22)], hum=True)
sh(18, "To understand the background of all this, we must turn the pages of the past back — into Ibrahim Naseem's own memories.")
sh(19, "Years ago, to the terrifying days when he fled this island. At that time Ibrahim had run out of any way to turn.",
   [("breath_heavy", "ފިލައިގެން", -22)])
sh(20, "When Amjad laid all the suspicion for the murder that happened on the island on his head, he fled the island to save his life.",
   hum=True)
sh(21, "That was also Amjad's secret advice: \"If you want to stay safe from here, never even think of setting foot on this island again, ever!\"")
sh(22, "Amjad sent him away with the intention of securing his own safety. Ibrahim went and landed on a remote, sparsely populated island in another atoll.",
   [("dhoni_engine", "ބަނދަރުކުރީ", -22)])
sh(23, "He stepped onto that island with a new face. Using the silicone mask Amjad had secretly supplied him, he changed the look of his face entirely.")
sh(24, "Not a trace of the former Ibrahim showed in that face. He introduced himself on that island by the name of Adam —")
sh(25, "as a quiet, hard-working fisherman who loves a solitary life. Life on the new island gave Adam a completely different feeling.")
sh(26, "Even as he went out to sea every day, waging war with himself, the dark secret of the past kept gnawing at his heart.",
   [("wave_crash", "ކަނޑުމައްޗަށް", -24)])
sh(27, "Yet into that bitter life a moonlight of hope appeared, because of an innocent young woman he met on that island. Her name was Mariyam.")
sh(28, "Mariyam's kindness and obedience drove away Adam's loneliness. Mariyam knows nothing of Adam's past, nor that his real name is Ibrahim Naseem.")
sh(29, "To Mariyam he is simply Adam, a man of good character who moved to the island to live.")
sh(30, "After days of closeness, just as Adam wished, he asked Mariyam's family for her hand in marriage. Without any obstacle, the knot of that marriage was tied.")
sh(31, "After the marriage Adam believed the dark shadow of his past would never follow him. He began building a new life with Mariyam.")
sh(32, "But every night, when lying down to sleep, he had to take off the fake mask on his face in pitch darkness, secretly, hidden from Mariyam.")
sh(33, "It had become a life lived inside a strange wonder. And Adam had to carry the sorrow of it.")
sh(34, "The pain of a husband unable to show his own true face to his own wife! After about two years passed that way, one night a call came to Adam's secret phone.",
   [("phone_buzz", "ކޯލެއް", -18)])
sh(35, "It was Amjad's call. With that call the foundation of Adam's new life was smashed to pieces. Amjad ordered him to leave that island at once and come back to the old island.")
sh(36, "Otherwise, he warned, he would tear off his mask in front of Mariyam. Ibrahim was forced to take Mariyam and suddenly flee that island, back to the land of his frightening past.",
   hum=True)
sh(37, "What kind of trial is this? Not even the chance to take a calm breath. Not even the chance to settle on another island and live in peace.")
sh(38, "That easy life was lost once again. Suddenly life was thrown this way and that; like a boat drifting into a fierce storm at sea, Mariyam's life changed faster than she could ever imagine.",
   [("wave_crash", "ތޫފާނެއްގެ", -20)])
sh(39, "Without any warning, the orders began to come. One night Adam came and said they had to leave the island at once.",
   [("door_open", "އައިސް", -20)])
sh(40, "When Mariyam asked, Adam gave a short answer: \"This is part of a very secret, dangerous government mission.\"", speaker="adam")
sh(41, "\"If we want to save our lives, we have to flee at once.\" Mariyam is an innocent woman who loves Adam beyond measure and trusts him with her whole heart.")
sh(42, "As words of fear came from her husband's lips, her heart filled with unease. But without a single complaint she decided to follow her husband.")
sh(43, "In the middle of a pitch-black night they came on a small launch and landed on the island of Adam's frightening past.",
   [("boat_engine", "ލޯންޗެއްގައި", -20)])
sh(44, "Even when they landed on that island, all Mariyam knew was that her husband's name was Adam.")
sh(45, "That his real name was Ibrahim Naseem, believed to have died twenty years ago, and that what was on his face was a silicone mask, never even crossed Mariyam's mind.")
sh(46, "Adam did not take Mariyam to where the islanders live, but to the most isolated, frightening jungle area of the island, thick and overgrown with trees.",
   [("leaves_rustle", "ޖަންގަލި", -22)])
sh(47, "\"Adam... where are we going? This isn't a place where people live, is it?\"", speaker="mariyam")
sh(48, "Mariyam, in fear, gripped Adam's arm tightly. \"Mari... be quiet! Our safety lies here.\"",
   [("cloth_rustle", "ހިފަހައްޓައިލި", -22)], speaker="adam")
sh(49, "There was despair in Adam's voice. They went into the dense part of the jungle and stopped at a spot covered by big screw-pines and small magoo shrubs.",
   [("leaves_rustle", "ވަދެގެން", -22)])
sh(50, "In that place there was an iron hatch raised up from the ground. When Adam opened that hatch, what could be seen below was a dark underground bunker.",
   [("metal_door", "ހުޅުވައިލި", -16)], hum=True)
sh(51, "Mariyam's eyes grew wide. She had never once imagined that such great secrets lay in the depths of her husband's life.",
   [("gasp", "ބޮޑުވެގެން", -20)])
sh(52, "Inside the bunker a small room had been built. There was even electricity inside it. Mariyam stood amazed.",
   [("bulb_flicker", "ކަރަންޓު", -22)])
sh(53, "There were some secret papers, and boxes of food carefully sealed. Mariyam was forced to begin her new life in that narrow, frightening bunker room.")
sh(54, "But the seed of doubt was planted in Mariyam's heart on the second night of living there. While Mariyam lay asleep, she opened her eyes to find Adam sitting by the table in the dim light of the room.",
   [("heartbeat", "ހުޅުވައިލެވުނު", -22)], hum=True)
sh(55, "Adam sat with his hand on his face. Suddenly, from near his ear, Adam pulled at something like a skin.",
   [("cloth_rustle", "ދަމައިލި", -22)], hum=True)
sh(56, "Mariyam, holding her breath, clapped her hand over her mouth, lest she scream. When he lifted the whole mask off her husband's face and laid it on the table, the face of a completely different person appeared!",
   [("gasp", "ހިފަހައްޓައިލަމުން", -20), ("soft_thud", "ބޭއްވި", -24)], hum=True)
sh(57, "That was not the Adam she knew. It was a completely strange, ageing, different face. Mariyam's whole world spun.",
   [("heartbeat", "އެނބުރިގަތް", -20)], hum=True)
sh(58, "To whom had she been bound by the knot of marriage? Who, really, was her husband? In the dim, pale light that filled the bunker, Mariyam lay holding her breath.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
sh(59, "Her eyes stayed fixed on the table. What lay there was her husband's face — the silicone mask he had just pulled off as if peeling away his own skin.",
   hum=True)
sh(60, "Looking at the real face of the man sitting at the table, all strength drained from Mariyam's body, as if she had frozen.",
   [("heartbeat", "ހަކަތަ", -22)], hum=True)
SHOTS = S

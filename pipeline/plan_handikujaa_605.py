"""Beat/shot plan for Handi Kujaa episode 605 (used by plan_beats.py).
Continuation of 594: the storm night in the tent -> the roof torn open -> the run to the ancient nika (banyan) tree ->
the fake grandfather with backward feet -> the iron knife in the sand -> the red-eyed crows."""

LOC = {
    "tent": "inside the family's large canvas camping tent on the beach at night during the storm: woven mats on the sand floor, bags piled along the sides, a single oil lantern hanging from the wooden centre pole, the canvas walls bellying and shaking in the wind",
    "tent_torn": "inside the family's canvas camping tent at night just after its roof has ripped open down the middle: a long jagged tear in the canvas roof, rain pouring through it, torn canvas flaps whipping, the oil lantern swinging on the wooden centre pole, mats and bags getting soaked",
    "tent_top": "the top of the family's torn canvas camping tent on the beach at night, seen from below through the long rip in its roof: the wooden centre pole rising up through the tear, the ripped canvas edges flapping, the storm sky above",
    "beach_run": "the island's wide powder-white beach at night in the storm: the wrecked canvas tent left behind, coconut palms thrashing, the black jungle edge on one side and dark breaking surf on the other",
    "jungle_edge": "the edge of the dense dark island jungle along the shore at night: screw-pines, magoo shrubs and leaning palm trunks, a strip of wet sand between them, the huge dark shape of an ancient banyan tree far ahead",
    "banyan": "an enormous centuries-old nika (banyan) tree standing alone on the shore of the island at night: a vast dark spreading canopy, curtains of hanging aerial roots, huge twisting roots spreading over the sand and forming deep hollows, the stormy sea beyond",
    "roots": "inside the hollows among the huge twisting roots of the ancient nika (banyan) tree at night: thick gnarled root walls curving around them like a shelter, a damp sand floor, hanging aerial roots, the heavy canopy above keeping off most of the rain",
    "outside_shade": "the stormy night beach just outside the shade of the ancient nika (banyan) tree, seen from among its roots: the edge of the canopy's dark shade drawn on the smooth wet sand, silver rain falling beyond it, the dark jungle and the sea behind",
    "canopy": "the dense dark canopy of the ancient nika (banyan) tree seen from below at night: thick twisting branches, heavy clusters of leaves, hanging aerial roots, rain dripping through",
}
MOOD = {
    "tent": "storm night inside the tent: a single warm oil-lantern light, deep shadows, the canvas walls shaking, a cold sea-green spectral tinge creeping in the shadows, tense and dreadful",
    "tent_torn": "storm night: the warm oil lantern swinging and flaring, cold silver rain pouring through the tear, a white lightning flash above, chaos and terror",
    "tent_top": "storm night: near-black indigo sky, slanting silver rain, white lightning behind, a cold sea-green spectral glow, two red-glowing eyes, terrifying",
    "beach_run": "storm night: near-black indigo, silver rain, white lightning flashes, the wet sand glowing an eerie dull wine-red in the storm light (just a red tint of light, no liquid), panic and flight",
    "jungle_edge": "storm night: near-black indigo, silver rain, tree shadows like giant ghosts, a cold sea-green spectral glow from above, flight and dread",
    "banyan": "storm night: near-black indigo, silver rain, a white lightning flash outlining the huge tree, a faint calm stillness under its canopy, awe and refuge",
    "roots": "storm night under the banyan: dim blue-grey darkness, the weak warm beam of a hand torch lying on the sand, white lightning flickering through the hanging roots, cramped and frightened",
    "outside_shade": "storm night: silver rain, white lightning, a cold sea-green spectral glow on the wet sand outside the shade, sinister and uncanny",
    "canopy": "storm night: near-black leaves, a lightning flicker through the branches, hundreds of small red glowing eyes, menacing",
}

HIJ_S = "Shareefa in her deep-maroon dress with her black hijab fully covering her hair and neck"
HIJ_A = "Aisha in her lavender dress with her white hijab fully covering her hair and neck"
KIDS = "three small children (little girls about 5 to 10 in small headscarves covering their hair) small and in the background, huddled behind the women"
POSS = "Aslam (mustard t-shirt and open grey checked shirt) pale and ashen, eyes pale milky white, limp"
HANDI_HORROR = ("the handi in her horror form: her opaque loose long-sleeved white gown and opaque white veil fully covering her hair "
                "and neck, long dark smoky ribbons trailing from under the veil, her face now ashen grey and cracked like old "
                "porcelain with dark hollow eyes glowing red (no blood, no tears, no rot, no fangs)")
HANDI_FLY = ("the handi: opaque loose long-sleeved white gown and opaque white veil fully covering her hair and neck, the gown "
             "and long veil ends streaming behind her, long dark smoky ribbons trailing on the wind, ashen grey face with red-glowing eyes")
FAKE = ("the fake grandfather: an old man with exactly Aadhambe's look — white skullcap, short white beard, white kurta-style shirt "
        "and checked sarong — holding a broken half of a wooden walking stick, wearing a sly, unnatural fixed smile, soaked by rain "
        "but strangely calm")
KNIFE = "an old plain dark iron kitchen knife with a worn wooden handle"
WET_M = "clothes soaked by rain but loose and opaque"

BEATS = [
    # ---------------------------------------------------------------- in the tent (continuation of 594)
    dict(to=2, reason="continuation of 594's last moment: Aslam's unconscious body floating in the air of the tent; Aisha reaches for his foot", chars=["aslam", "aisha", "aadhambe"], loc="tent",
         visual=f"inside the lantern-lit tent: {POSS}, his body floating horizontally in the air about a metre above the mat, seen from the side, lying flat on his back with his face turned up toward the tent roof, arms and legs hanging loosely down; {HIJ_A} kneeling below him in tears, reaching one hand up toward his foot; Aadhambe (white skullcap, white beard, white kurta, checked sarong) at the side raising his open palm sharply to stop her, shouting; the lantern flame trembling, canvas walls shaking",
         camera="medium-wide side view at eye level, the floating body and the faces in the upper two-thirds, the dark mats on the sand floor as the lower third",
         amb="tent_storm", sens="other", safe="levitation shown calm and eerie (flat, side view, limbs hanging), no contortion, no bent-back head, no fluids"),
    dict(to=4, reason="action change: Aadhambe recites over the water bowl and throws it — blue sparks burst from Aslam and he drops to the floor", chars=["aadhambe", "aslam"], loc="tent",
         visual=f"Aadhambe in the centre of the tent, eyes fierce, lips moving in recitation, flinging the water from a small brass bowl in a glittering arc toward Aslam's floating body; where the water strikes Aslam's chest a burst of tiny bright electric-blue sparks flies off him as he drops toward the mat; {POSS}; the lantern flaring, women in hijab blurred in the background",
         camera="medium shot from a low angle, Aadhambe's face and the arc of water and blue sparks in the upper two-thirds, the mat on the sand floor as the lower third",
         amb="tent_storm", sens="other", safe="ruqyah shown respectfully: a small bowl of water, no visible text; the 'shock' is only tiny blue sparks"),
    dict(to=7, reason="action change: a shriek on the roof, the canvas roof rips open down the middle and rain pours in on the family", chars=["zaahid", "shareefa", "naazim", "aisha"], loc="tent_torn",
         visual=f"the family inside the tent looking up in horror as the canvas roof splits open down the middle with a long jagged tear, sheets of rain pouring in through the rip; Zaahid (sky-blue shirt, grey moustache) and big bearded Naazim (dark-green t-shirt) staring upward, {HIJ_S} pulling {KIDS} close, {HIJ_A} beside her; the lantern swinging wildly; only these four adults and the three small girls in the picture, nobody lying on the floor, the empty wet mats in front",
         camera="medium-wide, slightly low angle, the frightened upturned faces and the torn roof in the upper two-thirds, the wet mats as the lower third",
         amb="tent_storm"),
    dict(to=11, reason="reveal: through the rip, the handi stands on top of the tent pole in the rain, her beauty gone — she threatens them", chars=["handi"], loc="tent_top", speaker="handi",
         visual=f"looking up through the long rip in the canvas roof: {HANDI_HORROR}; her beauty is completely gone — the face is no longer pretty or smiling but ash-grey and lifeless, crazed with fine dark cracks like a broken porcelain mask, sunken dark hollow eye sockets with burning red glowing eyes, a cold furious glare, mouth set hard; her gown is thick, heavy, fully opaque fabric hanging very loose and wide, the long veil draped wide over her chest and shoulders like a cape; she is standing upright on the very top of the tent's wooden centre pole high above in the pouring rain, her white gown and veil thrashing in the wind, one long arm stretched downward pointing with long dark fingernails; behind her a white lightning flash in the black sky; torn canvas edges in the foreground",
         camera="low-angle shot looking straight up, the handi centred in the upper half, the dark torn canvas framing the lower third",
         amb="tent_storm", sens="other", safe="'rotten blackened face, tears of red blood' replaced by an ashen grey cracked porcelain-like face with red-glowing eyes; gown and veil opaque, hair never visible"),
    dict(to=13, reason="speaker change: Aadhambe shouts orders, raising his stick to face the spirit, while Zaahid and Naazim lift Aslam", chars=["aadhambe", "zaahid", "naazim", "aslam"], loc="tent_torn", speaker="aadhambe",
         visual=f"Aadhambe standing firm in the middle of the torn tent with rain pouring on him through the rip, raising his long wooden walking stick high toward the sky, shouting back over his shoulder; behind him Zaahid and big bearded Naazim lifting the unconscious Aslam between them by his arms and legs; the lantern swinging",
         camera="medium shot, Aadhambe centred and sharp in the upper half, the brothers with Aslam softer behind, the wet sand floor as the lower third",
         amb="tent_storm"),
    # ---------------------------------------------------------------- the run along the beach
    dict(to=16, reason="scene change: the family runs out of the wrecked tent into the rain — the white sand looks red", chars=["shareefa", "aisha", "zaahid", "naazim"], loc="beach_run",
         visual=f"the family running away from the wrecked tent across the stormy beach toward the camera: {HIJ_S} and {HIJ_A}, both {WET_M}, each pulling a small headscarfed girl by the hand (a third small child between them); behind them Zaahid and Naazim carrying the limp Aslam between them; the sand under their feet glowing an eerie dull wine-red in the storm light, footprints sinking; the ruined tent with flapping canvas far behind",
         camera="wide shot at eye level, the running figures in the upper two-thirds, the red-tinted wet sand as the lower third",
         amb="beach_storm_night", sens="other", safe="'sand like blood' = dull wine-red storm light on the sand only, no liquid"),
    dict(to=17, reason="action change: a thunderclap lights everything — Naazim, running, glances back", chars=["naazim"], loc="beach_run",
         visual=f"close-up of big bearded Naazim (dark-green t-shirt, {WET_M}) mid-run, turning his head back over his shoulder, eyes wide, his face lit stark white by a sudden lightning flash, rain streaming down his beard",
         camera="close-up, eye level, his face in the upper half, his shoulder and the dark rain as the lower third",
         amb="beach_storm_night"),
    dict(to=19, reason="new view (what Naazim sees): Aadhambe fallen on the sand, his stick snapped in two, the handi flying toward them", chars=["handi", "aadhambe"], loc="beach_run",
         visual=f"looking back down the stormy beach: far away beside the wrecked tent, old Aadhambe fallen on the wet sand on his side, propped on one elbow, alive, the two broken halves of his wooden walking stick lying near him; above, much closer to the camera, {HANDI_FLY}, flying low through the rain toward the viewer, arms reaching forward; white lightning in the sky, the sand tinted dull wine-red",
         camera="wide shot, the flying handi large in the upper third, the small fallen grandfather in the middle distance, the red-tinted sand as the lower third",
         amb="beach_storm_night", sens="violence", safe="the attack on Aadhambe is never shown: only the old man fallen far away and the snapped stick"),
    dict(to=20, reason="return to Naazim's face as grandfather's last words ring in his ears", chars=["naazim"], loc="beach_run",
         reuse="beat_007", amb="beach_storm_night", visual="(reuse of beat_007)"),
    dict(to=22, reason="speaker change: Zaahid shouts 'Don't look back! Run!' as the two brothers carry Aslam on through the rain", chars=["zaahid", "naazim", "aslam"], loc="beach_run", speaker="zaahid",
         visual=f"Zaahid (sky-blue shirt, grey moustache, {WET_M}) running toward the camera through the pouring rain, shouting with his mouth wide open, carrying the limp unconscious Aslam across his and Naazim's shoulders; big bearded Naazim on the other side, head down; the sand dull wine-red, lightning behind",
         camera="medium shot, eye level, Zaahid centred and sharp in the upper half, the splashing wet sand as the lower third",
         amb="beach_storm_night"),
    # ---------------------------------------------------------------- along the jungle edge
    dict(to=25, reason="scene change: the women run with the children along the jungle edge while the laughing handi stretches over their heads like a shadow", chars=["handi", "shareefa", "aisha"], loc="jungle_edge",
         visual=f"{HIJ_S} large in the front centre, running toward the camera with her eyes raised and her lips moving in prayer, and {HIJ_A} just behind her, both {WET_M}, running along the dark jungle edge, hurrying {KIDS} ahead of them; directly above them in the rain, {HANDI_FLY}, drifting overhead like a huge pale shadow, laughing, her long dark smoky ribbons hanging down and shedding silver rain drops; screw-pines and palms thrashing; the huge dark banyan tree far ahead",
         camera="wide low-angle shot, the hovering handi and the women's faces in the upper two-thirds, the wet sand path as the lower third",
         amb="jungle_storm_night"),
    dict(to=27, reason="speaker/action change: Raaidhu shouts 'Wait!' as black roots burst from the sand to grab their feet", chars=["raaidhu"], loc="jungle_edge", speaker="raaidhu",
         visual="lanky Raaidhu (red t-shirt, black track trousers, soaked) stopping short on the wet sand, shouting in alarm, arms flung out, staring down; all around his sneakers thick black gnarled roots bursting up out of the sand and snaking toward his ankles; other running feet blurred beside him; rain and the dark jungle behind",
         camera="medium-wide, slightly high angle, Raaidhu's face centred in the upper half, the black roots curling over the sand in the lower part",
         amb="jungle_storm_night"),
    dict(to=28, reason="return to the women running under the hovering handi: Shareefa recites Aayathul Kursi (crop on Shareefa)", chars=["shareefa", "aisha", "handi"], loc="jungle_edge",
         reuse="beat_011", amb="jungle_storm_night", visual="(reuse of beat_011)", sens="other", safe="recitation from memory, no visible text"),
    # ---------------------------------------------------------------- the ancient nika tree
    dict(to=31, reason="scene change: they reach the huge centuries-old nika tree on the shore (held through its history)", loc="banyan",
         visual="a wide, awe-inspiring view of the enormous ancient nika (banyan) tree standing on the dark shore in the storm: its vast canopy spreading wide, curtains of hanging aerial roots, giant twisting roots arching over the sand into deep hollows; a white lightning flash outlining it against the black sky; the small figures of a running family arriving at its roots; the stormy surf beyond; a sense of quiet refuge under it",
         camera="wide establishing shot, low angle, the tree filling the upper two-thirds, the sand and roots as the lower third",
         amb="beach_storm_night"),
    dict(to=32, reason="action change: everyone squeezes in among the giant roots and crouches; the brothers lay Aslam down", chars=["naazim", "zaahid", "aslam", "shareefa"], loc="roots",
         visual=f"inside a deep hollow among the giant twisting roots: Naazim and Zaahid kneeling and gently laying the unconscious Aslam down on the sand; {HIJ_S} crouched against a thick root with {KIDS} tucked behind her; Aisha's lavender sleeve and white hijab at the edge; hanging aerial roots around them, rain falling beyond",
         camera="medium-wide, eye level, the crouching family in the upper two-thirds, the damp sand floor as the lower third",
         amb="beach_storm_night"),
    dict(to=36, reason="new figure: the handi halts in mid-air at the edge of the tree's shade, cannot enter, claws the air and screams threats", chars=["handi"], loc="outside_shade", speaker="handi",
         visual=f"just outside the edge of the banyan's dark shade: {HANDI_HORROR}, floating in mid-air in the rain as if stopped by an invisible wall, her face twisted in a furious shriek, both hands raised clawing at the empty air with long dark fingernails, her gown and veil streaming; hanging aerial roots in the dark foreground framing her",
         camera="medium shot from among the roots, the handi centred in the upper half, the line of shade on the smooth wet sand as the lower third",
         amb="beach_storm_night", sens="other", safe="horror form = ashen cracked porcelain face, red eyes; no monster face"),
    dict(to=38, reason="action change: Aslam stirs, his eyes darken, he grips Aisha's foot and speaks in another voice: 'grandpa is coming'", chars=["aslam", "aisha"], loc="roots", speaker="aslam",
         visual=f"close shot among the roots: Aslam lying on the sand, ashen, his milky-white eyes clouded with a shadowy darkness, his head turned to the side, whispering; one hand gripping the hem of the dress at the ankle of {HIJ_A}, who sits frozen beside him, staring down at him in fear; dim torch light",
         camera="close shot, Aslam's face centred in the upper half, his hand and the sand as the lower third",
         amb="beach_storm_night", sens="other", safe="possession shown only by eyes and pallor, no contortion"),
    dict(to=40, reason="new view: everyone looks out toward the jungle — the figure of 'grandfather' walking slowly out of the rain", chars=["zaahid", "naazim", "aadhambe"], loc="outside_shade",
         visual=f"over-the-shoulder from inside the roots: the dark backs and shoulders of Zaahid and big Naazim in the foreground looking out; beyond the edge of the shade, out of the dark jungle and the pouring rain, the figure of an old man in a white skullcap, white kurta and checked sarong walking slowly toward the tree, still small and half lost in rain and darkness",
         camera="over-the-shoulder wide shot, the approaching figure centred in the upper half, the smooth wet sand as the lower third",
         amb="jungle_eerie"),
    dict(to=41, reason="speaker change: 'grandfather' is near, smiling, holding the broken stick — Zaahid cries 'Bappa!' and starts toward him", chars=["zaahid", "aadhambe"], loc="outside_shade", speaker="zaahid",
         visual=f"Zaahid rising from the roots with a face full of relief and joy, one arm reaching out, calling out; behind him, softer in the rain just outside the shade, {FAKE}; the lower part of the old man's body hidden in darkness",
         camera="medium shot, Zaahid centred and sharp in the upper half, the old man softer behind, the roots and sand as the lower third",
         amb="jungle_eerie"),
    dict(to=42, reason="speaker change: Naazim grabs Zaahid's arm — 'Wait!' — his eyes fixed on grandfather's feet", chars=["naazim", "zaahid"], loc="roots", speaker="naazim",
         visual="big bearded Naazim (dark-green t-shirt) gripping Zaahid's arm firmly, holding him back, his face tense and suspicious, his eyes narrowed and staring downward past the camera; Zaahid half turned beside him, startled; dark roots and rain around them",
         camera="medium close-up, Naazim centred and sharp in the upper half, Zaahid at the side, the roots as the lower third",
         amb="jungle_eerie"),
    dict(to=45, reason="reveal: the old man's bare feet are turned backwards and leave no footprints on the wet sand", chars=["aadhambe"], loc="outside_shade",
         visual="low-angle shot from near the ground of the old man standing in the rain FACING the viewer: the front of his white kurta-style shirt with its button placket, both his hands holding the broken half of a wooden walking stick upright in front of his body, his checked sarong; his face at the top of the frame half in shadow with a sly smile; and at the bottom his two bare feet are unnaturally turned backwards — the heels point forward toward the viewer while the toes point away behind him, opposite to the way his body faces; he stands on perfectly smooth, unmarked wet sand with no footprints anywhere; rain splashing, a cold sea-green glow on the sand",
         camera="low angle from near the ground, the body and the backward feet in the upper two-thirds, the smooth unmarked sand as the lower third",
         amb="jungle_eerie", sens="other", safe="backward feet shown plainly, not gory: smooth skin, no wounds, no twisting"),
    dict(to=46, reason="reaction framing: the 'grandfather' smile now looks cunning and evil", chars=["aadhambe"], loc="outside_shade",
         visual=f"{FAKE}, standing at the very edge of the banyan's shade in the rain, staring straight at the viewer with a sly, cunning, unnatural smile and unblinking eyes; behind him the smooth wet sand without a single footprint; a faint cold sea-green glow around him",
         camera="medium shot, eye level, his face centred in the upper half, the smooth wet sand as the lower third",
         amb="jungle_eerie", sens="other", safe="the impostor is uncanny only through his fixed smile and stillness; no gore"),
    dict(to=47, reason="return to Zaahid and Naazim: 'No, that's not Bappa!' — Zaahid steps back", chars=["naazim", "zaahid"], loc="roots",
         reuse="beat_020", amb="jungle_eerie", visual="(reuse of beat_020)"),
    dict(to=50, reason="new figures together: the handi laughs at the grandfather-figure and the two circle the tree — 'Your grandfather is ours now!'", chars=["handi", "aadhambe"], loc="outside_shade", speaker="handi",
         visual=f"outside the banyan's shade in the storm: {HANDI_FLY}, floating in the air and laughing a wide cruel laugh — her gown made of thick, heavy, solid white cloth like a heavy robe, completely non-transparent, nothing of her body shape visible through it, hanging very loose and wide, the veil draped wide over her chest like a cape; below her the fake grandfather in white skullcap, white kurta and checked sarong with a sly smile, walking with the broken stick, his legs and feet hidden behind a thick dark root in the foreground; the two figures circling around the outside of the tree, seen between the hanging aerial roots; lightning, silver rain",
         camera="medium-wide shot from among the roots, the handi's face centred in the upper half, the old man lower at the side, the wet sand as the lower third",
         amb="beach_storm_night"),
    dict(to=53, reason="action/speaker change: Aslam goes rigid as iron; Aisha, crying, holds his hands — 'Do something! Aslam is dying!'", chars=["aisha", "aslam"], loc="roots", speaker="aisha",
         visual=f"{HIJ_A} kneeling over Aslam among the roots, crying out over her shoulder, both her hands holding his wrists down on the sand; Aslam lying straight and rigid as a plank, eyes wide and milky white, face ashen; dim torch light, rain beyond the roots",
         camera="medium shot, Aisha centred and sharp in the upper half, Aslam lying across the lower middle, the sand as the lower third",
         amb="beach_storm_night", sens="other", safe="Aslam clawing at his own throat is not shown: he lies rigid while Aisha holds his hands"),
    dict(to=55, reason="emotional turning point: Naazim remembers grandfather's old tale — spirits fear iron", chars=["naazim"], loc="roots",
         visual="close-up of big bearded Naazim in the dark among the roots, rain dripping from his hair and beard, his eyes suddenly wide with realisation, lit by a flash of lightning through the hanging roots, one hand lifting as he turns to call his brother",
         camera="close-up, eye level, his face in the upper half, his shoulder and the dark roots as the lower third",
         amb="beach_storm_night"),
    dict(to=57, reason="action change: Zaahid tears open his wet bag and pulls out the big old iron kitchen knife", chars=["zaahid", "naazim"], loc="roots",
         visual=f"Zaahid kneeling on the sand among the roots, the flap of his soaked canvas shoulder bag thrown open, lifting out {KNIFE} by its handle, the blade pointing upward and glinting in a lightning flash; big Naazim beside him reaching out an open hand for it",
         camera="medium close-up, Zaahid's face and the raised knife in the upper half, the open bag on the sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the knife is only held up, pointing to the sky, near no one"),
    dict(to=60, reason="action change: Naazim, praying under his breath, drives the iron knife into the sand beside Aslam's head; Aslam relaxes", chars=["naazim", "aslam", "aisha"], loc="roots",
         visual=f"{KNIFE} standing upright, stuck deep in the sand a hand's width away from Aslam's head, Naazim's big hand just letting go of its handle; Naazim kneeling above, his lips moving in prayer, eyes closed; Aslam lying calm now, eyes closed, breathing deeply; Aisha's lavender sleeve and white hijab at the side; a lightning glint on the blade",
         camera="medium close-up from a low angle, Naazim's face and the upright knife in the upper two-thirds, the sand around the knife as the lower third",
         amb="beach_storm_night", sens="violence", safe="the knife only stands in the sand as a talisman, touching no one"),
    # ---------------------------------------------------------------- the crows
    dict(to=62, reason="new subject: a rustle above — hundreds of black crows with red eyes in the canopy, watching them", loc="canopy",
         visual="looking straight up into the dark canopy of the giant banyan: on every twisting branch and among the thick leaves sit hundreds of black crows packed together, all their small eyes glowing red in the darkness, staring down; rain dripping through the leaves, a lightning flicker behind",
         camera="extreme low angle looking up, the crowded branches and red eyes filling the upper two-thirds, the darker hanging roots as the lower third",
         amb="beach_storm_night"),
    dict(to=63, reason="action change: with a roar of wings the crows pour down from the treetop like a black cloud", loc="banyan",
         visual="a huge swirling black cloud of hundreds of crows with red eyes pouring down out of the banyan's canopy toward the giant roots below, wings spread, rain and lightning; tiny figures of the family crouched among the roots at the bottom, covering their heads",
         camera="wide shot, low angle, the descending black cloud of crows in the upper two-thirds, the roots and sand as the lower third",
         amb="beach_storm_night"),
    dict(to=65, reason="action change: the crows swirl and peck; Zaahid covers his head shouting, Naazim whirls a cloth overhead", chars=["zaahid", "naazim"], loc="roots", speaker="zaahid",
         visual="among the banyan roots, black crows with red eyes swirling all around: Zaahid crouched shouting, both arms wrapped over his head; big bearded Naazim, still wearing his dark-green t-shirt, standing and whirling a checked sarong cloth over his head like a sail to beat the birds away; flapping wings everywhere, feathers in the air, rain",
         camera="medium-wide, eye level, Zaahid's shouting face centred and Naazim's whirling cloth in the upper two-thirds, the sand as the lower third",
         amb="beach_storm_night", sens="violence", safe="the crows never wound anyone: people covering heads, crows swirling, no marks; Naazim keeps his t-shirt on and whirls a sarong cloth"),
    dict(to=66, reason="action change: Shareefa and Aisha push the small children into the root hollow and shield them with their bodies", chars=["shareefa", "aisha"], loc="roots",
         visual=f"{HIJ_S} and {HIJ_A} bent protectively over the opening of a deep hollow between two giant roots, their arms and backs shielding {KIDS} tucked inside, only small headscarves visible; a few black crows swirling above them, wings beating, the women's faces turned up in fear",
         camera="medium shot, the women's faces in the upper half, the root hollow and sand as the lower third",
         amb="beach_storm_night", sens="other", safe="children small, hidden and untouched; no wounds"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Yet his head was tipped back, his whole face turned straight up toward the roof of the tent. A foul stench was coming from his body, stronger than before.",
   hum=True)
sh(2, "\"Ya Allah! Aslam!\" Aisha, bursting into tears, raised her hand to grab her husband's foot. \"Don't touch him! Get back!\"",
   [("gasp", "ރޮއިގަންނަމުން", -20)], speaker="aadhambe", crop="medium", focus=[80, 42])
sh(3, "Aadhambe shouted loudly. With firmness in his voice, after reciting over the bowl of water in his hand and blowing on it, he threw it toward Aslam's body.",
   [("splash", "އުކާލި", -18)], speaker="aadhambe")
sh(4, "As that splash of water struck Aslam's chest, it was as if a powerful electric shock had hit him. Tiny blue sparks burst out of his body, and with a loud noise he fell to the floor.",
   [("soft_thud", "ވެއްޓުނު", -14)], hum=True)
sh(5, "At that moment, from the roof of the tent came a dreadful, piercing shriek that seemed to burst the heart. It was a shriek that shattered their hopes to pieces.",
   [("wind_howl", "ހަޅޭކެއްގެ", -16)], hum=True)
sh(6, "Khrees — with a loud sound the canvas of the tent's roof tore apart down the middle. The drops of the pouring heavy rain began to pour into the tent.",
   [("fabric_tear", "ޚްރީސް", -12), ("rain_start", "އޮއްސައިގަތް", -16)])
sh(7, "Even the only shelter they had was lost. Through that torn cloth, everyone saw the figure standing above.")
sh(8, "In the pouring heavy rain, standing upright on top of the tent pole was that dreadful handi. While her white gown thrashed in the wind, there was no trace on her face of the beauty seen just before.",
   [("wind_gust", "ތެޅެމުންދިޔައިރު", -18)], hum=True)
sh(9, "The skin of her face was rotten and blackened. Drops of red blood flowing from her two eyes ran down, mixed with the rainwater.",
   hum=True)
sh(10, "\"Not one of you will leave this island alive tonight!\"", speaker="handi", hum=True)
sh(11, "the handi said, stretching her hand with its long sharp nails downward. \"Zaahid! Naazim! Raaidhu!\"")
sh(12, "\"Take Aslam and run! Go toward the big nika tree on the shore!\" Aadhambe raised his long walking stick and prepared to face the handi.",
   speaker="aadhambe")
sh(13, "\"I'm coming right behind you. Nobody look back!\" Zaahid and Naazim quickly lifted Aslam's body.",
   speaker="aadhambe")
sh(14, "Shareefa and Aisha, holding the small children by the hand, came out of the wrecked tent and ran into the heavy rain. The white sand of the whole island was a different colour.",
   [("footsteps_sand", "ދުއްވައިގަތް", -18)])
sh(15, "It seemed as if the whole white sand had been soaked in the colour of red blood. With every step their feet sank into the ground.",
   [("footsteps_sand", "ފިޔަވަޅަކާއެކު", -20)], hum=True)
sh(16, "As they ran, from behind them came the sound of Aadhambe reciting loudly and the dreadful shriek of that handi.",
   [("wind_howl", "ހަޅޭކުގެ", -20)])
sh(17, "Suddenly, with the sound of a great thunderclap, the whole area lit up. At that moment Naazim, running, couldn't help glancing back.",
   [("thunder", "ގުގުރިއެއްގެ", -12)], hum=True)
sh(18, "Aadhambe lay fallen on the ground. And that dreadful handi, after snapping Aadhambe's long stick in two, began flying through the air toward where the family was running.",
   [("wind_gust", "އުދުހިފަ", -18)], hum=True)
sh(19, "Seeing Aadhambe fallen on the ground and the walking stick he used broken in two, Naazim's heart all but stopped.",
   [("heartbeat", "ހުއްޓުނު", -18)], hum=True)
sh(20, "He was the whole family's only shield. But grandfather's last words kept ringing in his ears. \"Nobody look back! Run!\"")
sh(21, "\"Naazim! Don't look back! Run!\" Zaahid shouted at the top of his voice.", speaker="zaahid")
sh(22, "The two of them, carrying Aslam's body on their shoulders, ran on through the pouring heavy rain.",
   [("footsteps_sand", "ދުވަމުންދިޔަ", -20)])
sh(23, "Shareefa and Aisha, taking the small children, crying and screaming, headed through the jungle toward the nika tree.",
   [("leaves_rustle", "ވަލުތެރެއިން", -20)])
sh(24, "The sound of the wind heard behind them suddenly changed into the dreadful laughter of the handi. That terrifying figure, as if drifting through the air, stretched over their heads like a shadow.",
   [("wind_howl", "ހުނުމުގެ", -18)], hum=True)
sh(25, "From her long hair the drops of rain fell to the ground like black chemicals. \"Wait!\"")
sh(26, "Raaidhu suddenly shouted. Something was spreading through the white sand he was running on.", speaker="raaidhu")
sh(27, "Big black roots came out of the depths of the earth, trying to coil around their feet. It seemed as if the whole island was trying to hold them back.",
   [("low_growl", "ބިމުގެ", -18)], hum=True)
sh(28, "\"Ya Allah! Save us!\" Shareefa, reciting Aayathul Kursi, kept telling the children to recite the Kursi too.",
   speaker="shareefa", crop="medium", focus=[50, 40])
sh(29, "Gasping for breath, their bodies growing weak, they reached the huge nika tree on the shore.",
   [("breath_heavy", "މާނޭވާލެވެމުން", -18)])
sh(30, "It is a huge tree, many hundreds of years old, its roots spread over the whole area. As Aadhambe always said, it is a tree under which island people travelling in olden times would always come and sit.")
sh(31, "Back then many people would sit there reciting the Quran. In those days, when talk of evil on the island arose, many recited protections were buried beneath that tree.")
sh(32, "Everyone crept in among the big roots of that tree and crouched down. Naazim and Zaahid laid Aslam on the ground.",
   [("cloth_rustle", "ބޮނޑިވެލި", -22)])
sh(33, "At that moment the dreadful handi who had come after them suddenly stopped in mid-air at the point where the nika tree's shade began.",
   [("wind_gust", "ހުއްޓުނު", -18)], hum=True)
sh(34, "She did not dare to enter the shade of that tree. Staying outside the tree, the handi kept clawing at the air with her long nails.")
sh(35, "Her face changed with a shriek full of terror. \"You can't stay there forever!\"",
   [("low_growl", "ހަޅޭކަކާއެކު", -16)], speaker="handi", hum=True, focus=[35, 25])
sh(36, "\"Before sunrise I will tear up that tree too!\" At that moment Aslam's body, lying on the ground, began to tremble again.",
   speaker="handi")
sh(37, "From within the white of his eyes, this time a black terror began to show. Slowly he took hold of the foot of Aisha, who sat beside him.",
   [("heartbeat", "ހިފެހެއްޓި", -20)], hum=True)
sh(38, "But this time a different voice came out of his mouth. \"Uncle... grandpa... grandpa is coming there...\"",
   speaker="aslam", hum=True)
sh(39, "With a trembling voice, Aslam pointed toward the jungle. Everyone looked toward the jungle.")
sh(40, "Out of the darkness, through the pouring rain, the figure of someone walking slowly appeared. It was true. It was grandfather.",
   hum=True)
sh(41, "In his hand was the stick broken in two. On his face was a smile. \"Bappa!\" Zaahid tried to run to him with joy.",
   speaker="zaahid", focus=[28, 30])
sh(42, "\"Wait!\" Naazim grabbed Zaahid's arm hard. Naazim's eyes were fixed on Aadhambe's feet.",
   [("gasp", "ހިފެހެއްޓި", -20)], speaker="naazim")
sh(43, "Though the rain was pouring, and though the white sand was wet, not a single trace of the approaching Aadhambe's footsteps appeared on the sand.",
   [("heartbeat", "ނިޝާނެއް", -18)], hum=True)
sh(44, "And the soles of his feet were turned backwards! At Naazim's shout, Zaahid suddenly pulled back.",
   [("gasp", "ފަސްޖެހުނު", -18)], hum=True)
sh(45, "As his eyes stopped on the feet of the figure in grandfather's form, goose-bumps rose all over his body. That figure's two feet were turned backwards.",
   hum=True)
sh(46, "As he came walking, not a single footprint formed in the white sand. The smile on his face now looked extremely cunning and evil.",
   hum=True)
sh(47, "\"Bappa... no, that's not Bappa!\" Zaahid stepped back in fear.", speaker="zaahid", crop="medium", focus=[76, 28])
sh(48, "The female handi flying in the air outside the nika tree's shade, on seeing the figure in grandfather's form, laughed loudly.",
   [("wind_howl", "ހީނގަތް", -18)])
sh(49, "The two figures together began to circle around the nika tree. From outside the tree came piercing sounds full of terror.",
   [("wind_howl", "އަޑުތައް", -20)], hum=True)
sh(50, "\"Your grandfather is now in our power! That tree will give you no protection!\"", speaker="handi", hum=True, focus=[38, 22])
sh(51, "A heavy, frightening voice came from the mouth of the figure in grandfather's form. At that moment Aslam's eyes, as he lay among the tree's roots, grew wide, and his body began to go rigid like iron.",
   [("low_growl", "ބިރުވެރި", -16)], hum=True)
sh(52, "Thrashing on the ground, he kept trying to grab his own throat. The power of the spirits outside was reaching Aslam inside the tree. \"Zaahid!\"",
   [("breath_heavy", "ތެޅެމުން", -20)], hum=True)
sh(53, "\"Naazim! Quickly, do something! Aslam is dying!\" Aisha, crying, tried to hold Aslam's hands.", speaker="aisha")
sh(54, "Suddenly an old tale that grandfather had told came back to Naazim's mind. When a spiritual affliction comes upon you,")
sh(55, "the power of iron is something those things fear. \"Zaahid!\"", speaker="naazim")
sh(56, "\"Where are the knives we brought for cooking?\" Naazim asked loudly. \"It's there! It's in my bag!\"")
sh(57, "Zaahid quickly opened the wet bag on his shoulder. From inside it he took out a big, sharp iron knife.",
   [("cloth_rustle", "ހުޅުވާލި", -20), ("metal_clang", "ވަޅިއެއް", -22)])
sh(58, "Naazim took the knife and, his lips moving as if reciting something, drove it hard into the ground beside Aslam's head.",
   [("soft_thud", "ހަރާލި", -14)], hum=True)
sh(59, "With that, the rigidness that had come over Aslam's body suddenly let go, and he took a deep breath. From outside the tree came the pained shrieks of the two figures.",
   [("sigh", "ނޭވާއެއް", -18), ("wind_howl", "ހަޅޭކުގެ", -18)])
sh(60, "Because of the iron knife, their spiritual hold was cut. But the terror was not over yet.")
sh(61, "Through the pouring heavy rain, a 'khrees' sound began to be heard from the top of the nika tree. When everyone raised their heads and looked up, among the thick leaves at the top of the tree, many hundreds of black crows sat watching them.",
   [("leaves_rustle", "ޚްރީސް", -14)], hum=True)
sh(62, "Those birds' eyes were red. And the birds were all getting ready to fly at them at once.",
   hum=True)
sh(63, "With the loud sound of wings beating at the top of the huge nika tree, the whole area echoed. Many hundreds of crows came down from the treetop at once, like a big black cloud descending to the earth.",
   [("wings_flap", "ފިޔަޖެހުމުގެ", -12)], hum=True)
sh(64, "With those birds' sharp beaks and claws they began pecking and wounding the family's bodies. \"Cover your bodies! Hide the children!\"",
   [("wings_flap", "ކޮށާ", -16)], speaker="zaahid")
sh(65, "Zaahid, shouting loudly, covered his head with both arms. Naazim pulled off his shirt and began whirling it in the air to drive the crows away.",
   [("cloth_rustle", "ހޫރަން", -16)])
sh(66, "Shareefa and Aisha pushed the small children in between the tree's big roots and shielded them with their own bodies.")
SHOTS = S

"""Beat/shot plan for Handi Kujaa episode 583 (continues 580 deep in the storm jungle; used by plan_beats.py)."""

LOC = {
    "jungle_spell": "deep inside the dense dark jungle of Beenaafushi island on a stormy night: a small opening among tall screw-pines, magoo shrubs and huge old trees with twisting roots, wet fallen leaves on dark sand, rain slanting through the canopy",
    "jungle_path": "the dense dark jungle of Beenaafushi island on a stormy night: narrow sandy paths between screw-pines, magoo shrubs and huge old banyan-like trees with twisting roots, tree shadows like giant ghosts, rain slanting through the canopy",
    "jungle_dark": "the dense jungle of Beenaafushi island in near-total darkness on a stormy night: black tree trunks and twisting roots barely visible, thrashing screw-pines, needle-like silver rain",
    "jungle_canopy": "the jungle canopy of Beenaafushi island seen from below on a stormy night: tall screw-pines and huge dark trees thrashing against a black sky full of storm clouds",
    "jungle_edge": "the edge of the jungle of Beenaafushi island opening onto the beach on a stormy night: the last screw-pines and palms bent by the wind, white sand, and beyond it the large canvas family tent on the beach glowing faintly from within, the black stormy sea behind",
    "tent": "inside a large canvas family camping tent on the beach at night in a storm: woven mats on the sand floor, travel bags piled at the sides, canvas walls and roof billowing and flapping in the wind, a single oil lantern hanging from the centre pole, the door flap at one end showing black rain outside",
    "tent_door": "the entrance of the large canvas family tent on the beach at night seen from outside: the door flap lifted, warm lantern light spilling out onto the wet white sand, rain slanting across, the canvas walls flapping",
    "shore": "the beach of Beenaafushi island at night in a storm, seen from the tent: wet white sand sloping to the black sea, big frothing waves breaking in white foam, dark coral rocks at the side, palms bent by the wind, heavy silver rain",
}
MOOD = {
    "jungle_spell": "storm night: near-black indigo, silver rain, white lightning flickers, an eerie sea-green spectral glow around the spirit, mist between the trunks, bewitching and dreadful",
    "jungle_path": "torchlit storm night in the jungle: warm flickering torch beams against near-black indigo, silver rain, a pale sea-green glow far off among the trees, tense and frightened",
    "jungle_dark": "pitch-dark storm night: almost black, only a faint cold blue lightning flicker revealing shapes, silver rain like needles, blind terror",
    "jungle_canopy": "storm night: near-black indigo sky lit by a white lightning flash, silver rain, thrashing black treetops, dreadful",
    "jungle_edge": "storm night: near-black indigo, silver rain, a single flickering torch beam, the faint warm glow of the tent ahead, exhausted and urgent",
    "tent": "tent at night in a storm: single warm oil-lantern light, deep shadows, canvas walls glowing amber and billowing, cold blue lightning flashing through the canvas, claustrophobic and frightening",
    "tent_door": "storm night: warm amber lantern light from inside the tent against the near-black indigo night, silver rain, a white lightning flash, dread",
    "shore": "storm night on the shore: near-black indigo, silver rain, white lightning flashes, an eerie sea-green spectral glow on the breaking waves, dreadful",
}

HANDI = ("the handi in her opaque, loose, long-sleeved, ankle-length white gown and an opaque white veil fully covering her hair "
         "and neck, long dark smoky ribbons trailing from under the veil on the wind, barefoot, floating just above the ground, "
         "a faint sea-green glow around her")
WETM = "his clothes darkened by the rain but loose and opaque"
POSS = "Aslam possessed: ashen-pale skin, his eyes completely milky-white with no pupils, a rigid unnatural posture (eerie, not grotesque)"
SHAR = "Shareefa in her maroon dress with her black hijab fully covering her hair and neck"
AISH = "Aisha in her lavender dress with her white hijab fully covering her hair and neck"
NOTXT = "no letters or symbols that look like writing"

BEATS = [
    dict(to=2, reason="episode opening (continuation of 580): deep in the storm jungle the white-clad spirit glides towards the spellbound Aslam", chars=["handi", "aslam"], loc="jungle_spell",
         visual=f"{HANDI}, gliding slowly towards Aslam between the dark trunks in the rain, her feet not touching the wet leaves, the rain falling on her yet she is untouched and serene, sea-green glowing eyes and a calm bewitching smile; Aslam in the foreground at the side, {WETM}, standing frozen and spellbound, his face in three-quarter view, staring at her",
         camera="medium-wide, eye level, the spirit centred in the upper two-thirds, Aslam at the side, wet leaves and dark sand as the lower third",
         amb="jungle_storm_night", sens="other", safe="the spirit redesigned modestly (bible rule 2): opaque gown and veil, smoky ribbons instead of hair"),
    dict(to=5, reason="action change: she raises her long cold hand with long dark nails towards his face; her voice in his head 'Come to me'; he lifts his hand to take hers", chars=["handi", "aslam"], loc="jungle_spell", speaker="handi",
         visual=f"close two-shot: {HANDI}, now very close, centred, raising one long pale hand with long dark fingernails towards Aslam's face, her lips closed, sea-green eyes glowing hypnotically; Aslam in profile at the side, rain on his face, eyes glazed, slowly lifting his own hand towards hers, their hands not yet touching",
         camera="close two-shot, eye level, her face and raised hand in the upper half, Aslam's profile at the side, dark rain-blurred jungle as the lower third",
         amb="jungle_storm_night", sens="other", safe="no touch between them; the spell shown by the glow and his glazed eyes"),
    dict(to=7, reason="character change: Zaahid's distant shout 'Aslam! My son! Where are you?' breaks the spell", chars=["zaahid", "naazim", "raaidhu", "aadhambe"], loc="jungle_path", speaker="zaahid",
         visual=f"Zaahid in the rain-lashed jungle, {WETM}, one hand cupped to his mouth shouting into the dark with a desperate face, the other hand holding up a flaming torch; behind him in the torchlight Naazim (huge, full beard, dark-green t-shirt) with a torch, lanky Raaidhu in his red t-shirt, and old Aadhambe in his white skullcap with his walking stick, all soaked and searching",
         camera="medium shot, eye level, Zaahid centred and sharp in the upper half, the others softer behind, wet roots and sand as the lower third",
         amb="jungle_storm_night"),
    dict(to=10, reason="emotional turning point / reveal: her beauty melts away into a terrifying face with a dreadful smile; Aslam cannot scream", chars=["handi", "aslam"], loc="jungle_spell",
         visual=f"the spirit's horror form, centred: her face ashen grey, cracked like old porcelain, dark hollow eyes glowing red, a terrifying fixed smile, still wearing the opaque white gown and the opaque white veil fully covering her hair and neck, dark smoky ribbons whipping around her in the wind; a white lightning flash; Aslam in the foreground at the side seen from behind his shoulder, recoiling, his mouth open in a soundless scream",
         camera="medium close-up over Aslam's shoulder, her face in the upper half, the dark ground as the lower third",
         amb="jungle_storm_night", sens="other", safe="'rotting face, black tears' shown only as an ashen cracked porcelain-like face with red-glowing hollow eyes (bible rule 2); no tears, no blood, no monster face"),
    dict(to=11, reason="action change: panicking, he steps back, catches a tree root and falls to the ground", chars=["aslam"], loc="jungle_spell",
         visual=f"Aslam stumbling backwards over a huge twisting tree root and falling onto the wet leaf-strewn ground, propped on one elbow, {WETM}, his face frozen in terror looking up out of frame, lit cold sea-green by a glow in front of him; rain streaking, dark trunks behind",
         camera="medium shot, slightly high angle, Aslam's face and upper body in the upper two-thirds, the roots and wet leaves as the lower third",
         amb="jungle_storm_night"),
    dict(to=14, reason="scene/character change: the search party — Raaidhu points to a pale blue-green glow in the west; Zaahid runs towards it, Aadhambe trying to stop him", chars=["raaidhu", "zaahid", "naazim", "aadhambe"], loc="jungle_path",
         visual="the search party in the torchlit jungle, their clothes darkened by the rain but loose and opaque: lanky Raaidhu in his red t-shirt in the centre shouting and pointing his arm towards a pale blue-green glow far among the trees; Zaahid already breaking into a run towards it; big bearded Naazim holding up a torch, staring; old Aadhambe with his stick reaching out a hand after Zaahid; rain in the torch beams",
         camera="medium-wide, eye level, Raaidhu centred in the upper half, the distant glow behind, the dark roots and sand as the lower third",
         amb="jungle_storm_night"),
    dict(to=17, reason="scene change: in the glowing spot they find Aslam unconscious and ice-cold, strange black marks in the sand around him and a wet black handprint on his shirt; Zaahid lifts him into his arms", chars=["zaahid", "aslam", "naazim", "raaidhu"], loc="jungle_spell", speaker="zaahid",
         visual=f"Zaahid kneeling on the wet sand lifting the unconscious Aslam up into his arms, calling to him with an anguished face; Aslam limp, pale, eyes closed, a dark wet handprint-shaped stain on the front of his mustard t-shirt; around them on the sand a ring of strange abstract black swirls and claw-like scratches ({NOTXT}); Naazim and Raaidhu standing behind holding torches, horrified; a fading pale blue-green mist hanging in the air",
         camera="medium shot, eye level, Zaahid's face centred in the upper half, the marked sand as the lower third",
         amb="jungle_storm_night", sens="other", safe="Aslam is unconscious (not hurt); the marks are abstract shapes, not text or symbols"),
    dict(to=18, reason="action/turning point: with a dreadful shriek a huge shadow flies off over the screw-pine treetops", loc="jungle_canopy",
         visual="looking up from the jungle floor: a huge dark shape trailing long pale tattered cloth and dark smoky ribbons sweeping away over the thrashing screw-pine treetops against a black storm sky, lit from behind by a white lightning flash, leaves and rain whirling in its wake; no face, no people",
         camera="low-angle wide shot, the flying shadow and treetops in the upper two-thirds, dark trunks fading into black as the lower third",
         amb="jungle_storm_night"),
    dict(to=21, reason="action change: the wind redoubles and every torch suddenly dies; pitch darkness and needle-like rain", loc="jungle_dark",
         visual="near-total darkness in the jungle: the dark silhouettes of four men in the trees, one hunched holding a limp figure, their torches just snuffed out, thin trails of smoke curling from the dead torch heads, a last orange ember fading; silver needle-like rain caught in a faint distant blue lightning flicker, trees bending violently",
         camera="wide shot, eye level, the silhouettes and smoking torches in the upper two-thirds, black ground as the lower third",
         amb="jungle_storm_night", sens="other", safe="the darkness is shown by a faint lightning flicker on silhouettes"),
    dict(to=22, reason="character focus: Raaidhu gropes blindly in the dark, screaming 'Bappa! Naazim! Where are you?'", chars=["raaidhu"], loc="jungle_dark", speaker="raaidhu",
         visual=f"Raaidhu alone in the blackness, {WETM}, arms stretched out in front of him groping blindly, his face terrified, mouth open shouting, eyes wide and unseeing, lit only from the side by a cold blue lightning flicker; rain streaking, black trees thrashing behind",
         camera="medium close-up, eye level, his face centred in the upper half, darkness as the lower third",
         amb="jungle_storm_night"),
    dict(to=24, reason="character focus: 'Stay calm! I'm here!' — Zaahid sits on the ground clutching ice-cold Aslam to his chest", chars=["zaahid", "aslam"], loc="jungle_dark", speaker="zaahid",
         visual=f"Zaahid sitting on the dark wet ground holding the unconscious Aslam tightly against his chest, {WETM}, calling out into the dark, his face lit faintly by a cold blue lightning flicker, shivering as if from ice; Aslam limp and pale against him, eyes closed; needle rain, black trees",
         camera="medium shot, eye level, Zaahid's face centred in the upper half, the dark ground as the lower third",
         amb="jungle_storm_night"),
    dict(to=29, reason="character focus: Aadhambe recites Aayathul Kursi steadfastly and the sounds quieten; Naazim's charged phone is dead; Aadhambe orders them to the beach", chars=["aadhambe", "naazim"], loc="jungle_dark", speaker="aadhambe",
         visual=f"old Aadhambe standing firm in the dark rain, {WETM}, eyes closed, both hands raised with palms open and cupped in prayer, his walking stick in the crook of his arm, reciting from memory with calm steadfast resolve; beside him at the side big bearded Naazim frowning at a mobile phone in his hand whose screen is completely dark and blank; a faint lightning glow reveals them, the trees behind a little stiller",
         camera="medium shot, eye level, Aadhambe centred in the upper half, Naazim at the side, the dark ground as the lower third",
         amb="jungle_storm_night", sens="other", safe="recitation from memory, no Quran pages or text shown; dead phone screen blank and dark"),
    dict(to=31, reason="action change: Naazim's torch flickers back on; the brothers lift Aslam and, guided by Aadhambe, carry him out of the jungle to the tent on the beach", chars=["naazim", "zaahid", "aslam", "aadhambe"], loc="jungle_edge",
         visual=f"Naazim and Zaahid carrying the unconscious Aslam between them out of the last trees towards the beach, Naazim's torch flickering back on and throwing a shaky beam ahead; old Aadhambe walking in front with his stick guiding them; lanky Raaidhu in a red t-shirt following behind; ahead the canvas tent glows faintly on the sand, the stormy sea beyond; rain",
         camera="medium-wide, eye level, the group in the upper two-thirds, the white wet sand as the lower third",
         amb="beach_storm_night"),
    dict(to=35, reason="scene change: inside the lantern-lit tent Shareefa and Aisha run to Aslam crying; his face is white and swollen, his lips dark, a foul smell", chars=["shareefa", "aslam", "aisha"], loc="tent", speaker="shareefa",
         visual=f"inside the tent: Aslam laid on a woven mat, unconscious, his face strangely pale white and a little puffy, his lips darkened grey; {SHAR}, kneeling beside him crying, her hand on his cheek; {AISH}, kneeling at his other side, crying, one hand over her nose and mouth; the men standing behind soft and blurred; the single oil lantern above, canvas billowing",
         camera="medium shot, slightly high angle, Shareefa's face centred in the upper half, the mat as the lower third",
         amb="tent_storm", sens="other", safe="'swollen face, black lips' kept mild: a pale, slightly puffy face and greyish lips; the smell shown by a hand over the nose"),
    dict(to=37, reason="action/speaker change: Aisha takes Aslam's hand and snatches it back — 'His hand is so hot! But father said it was cold'", chars=["aisha", "aslam"], loc="tent", speaker="aisha",
         visual=f"{AISH}, kneeling by the mat, centred, pulling her hand sharply back from Aslam's hand as if burned, eyes wide with shock, speaking; Aslam's limp hand on the mat in the foreground, his pale face at the side; warm lantern light",
         camera="medium close-up, eye level, Aisha's face centred in the upper half, Aslam's hand and the mat as the lower third",
         amb="tent_storm"),
    dict(to=39, reason="turning point: Aslam opens completely white eyes, sits up, stares out of the tent door into the rain and laughs; everyone backs away", chars=["aslam", "zaahid", "shareefa", "aisha"], loc="tent",
         visual=f"{POSS}, sitting bolt upright on the mat, staring past the viewer out through the open tent door into the black rain with an unnatural wide grin; around him the family recoiling backwards: Zaahid, {SHAR}, {AISH}; the lantern light flickering, lightning beyond the door",
         camera="medium-wide, eye level, Aslam centred in the upper half, the family at the sides, the mat as the lower third",
         amb="tent_storm", sens="other", safe="possession without body horror (bible rule 4): milky-white eyes, ashen skin, rigid posture only"),
    dict(to=42, reason="new framing for dialogue: the deep woman's voice speaks from Aslam's mouth — 'She has come... she has come for me...'", chars=["aslam"], loc="tent", speaker="aslam",
         visual=f"close-up of {POSS}, his lips parted speaking, the lantern light from below throwing hard shadows up his face, a faint eerie sea-green glow over his skin, the canvas wall behind him billowing",
         camera="close-up, eye level, his face centred in the upper half, his shoulders and dark shadow as the lower third",
         amb="tent_storm", sens="other", safe="eerie face only, no distortion"),
    dict(to=44, reason="character change: Shareefa screams and hides the small children behind her; Aisha stands stunned", chars=["shareefa", "aisha"], loc="tent",
         visual=f"{SHAR}, kneeling at the back of the tent with her arms spread protectively wide in front of the piled bags behind her, her face alarmed, mouth open calling out; {AISH}, kneeling beside her, motionless, both hands raised to her mouth, eyes wide and stunned; warm lantern light, the canvas billowing",
         camera="medium shot, eye level, Shareefa's face in the upper half, Aisha at the side, the mat as the lower third",
         amb="tent_storm", sens="other", safe="the children only small and half hidden behind their mother (bible rule 9)"),
    dict(to=46, reason="action change: Zaahid looks to Aadhambe; the grandfather steels himself, kneels and faces Aslam with determined eyes", chars=["aadhambe", "aslam", "zaahid"], loc="tent",
         visual=f"old Aadhambe kneeling down on the mat face to face with the rigid sitting Aslam (milky-white eyes, ashen skin), Aadhambe's eyes full of determination, his stick laid beside him; Zaahid behind Aadhambe at the side, looking at him with frightened eyes; warm lantern light between them",
         camera="medium shot from the side, Aadhambe's determined face centred in the upper half, the mat as the lower third",
         amb="tent_storm"),
    dict(to=49, reason="action change: as Aadhambe raises his hand to Aslam's forehead, Aslam seizes his wrist in an iron grip — 'Old man! Do you think you can break my power?'", chars=["aslam", "aadhambe"], loc="tent", speaker="aslam",
         visual=f"{POSS}, centred, leaning forward with a cold mocking sneer, speaking, his hand gripping old Aadhambe's raised right wrist in mid-air; Aadhambe at the side in three-quarter view, unflinching; the lantern swaying above",
         camera="medium close-up, Aslam's face centred in the upper half, the gripped wrist in the middle, the mat as the lower third",
         amb="tent_storm", sens="violence", safe="only a hand gripping a wrist (bible rule 5 allows it); no struggle"),
    dict(to=51, reason="speaker change: Aslam's eyes turn red-veined; Aadhambe declares 'By Allah's leave your power will leave this body!', frees his hand and recites Surat al-Jinn aloud", chars=["aadhambe", "aslam"], loc="tent", speaker="aadhambe",
         visual=f"old Aadhambe kneeling, centred, his freed right hand raised with the palm open, reciting loudly from memory with fierce, steadfast eyes; Aslam at the side in profile, ashen, his white eyes now glaring with red veins, recoiling; the lantern flame flaring",
         camera="medium close-up, eye level, Aadhambe centred in the upper half, Aslam at the side, the mat as the lower third",
         amb="tent_storm", sens="other", safe="recitation from memory, no Quran text shown"),
    dict(to=53, reason="action change: strong convulsions — Aslam on the mat, hands over his ears, screaming; the canvas whips, the lantern flares and dims", chars=["aslam", "aadhambe"], loc="tent",
         visual=f"Aslam lying on his side on the mat with both hands clamped over his ears, his ashen face screwed up in an anguished scream, eyes squeezed shut; behind him old Aadhambe kneeling, reciting with raised hands; the tent canvas violently whipping inwards, the hanging lantern swinging, its flame flaring bright and then guttering",
         camera="medium-wide, slightly high angle, Aslam and Aadhambe in the upper two-thirds, the mat as the lower third",
         amb="tent_storm", sens="other", safe="convulsions shown as a scream with hands over the ears; no contortion (bible rule 4)"),
    dict(to=54, reason="return to Aadhambe giving the order 'Naazim! Zaahid! Hold him!' without stopping his recitation (shot)", chars=["aadhambe", "aslam"], loc="tent", speaker="aadhambe",
         reuse="beat_021", amb="tent_storm", visual="(reuse of beat_021)", transition="cut"),
    dict(to=56, reason="action change: Zaahid and Naazim hold his arms, Raaidhu pins his feet — he has the strength of four men", chars=["zaahid", "naazim", "raaidhu", "aslam"], loc="tent",
         visual="Zaahid and big bearded Naazim kneeling on either side of Aslam who lies on his back on the mat, each steadying one of his arms with both hands, their faces tense with effort; lanky Raaidhu in his red t-shirt kneeling at his feet, steadying his ankles; Aslam ashen, eyes closed, head turned aside; old man reciting softly in the background is out of focus; the lantern swinging, the canvas billowing",
         camera="medium-wide, slightly high angle, the men's straining faces in the upper two-thirds, the mat as the lower third",
         amb="tent_storm", sens="violence", safe="the restraint shown as holding his arms and feet down on the mat, no struggle gore (bible rule 5)"),
    dict(to=58, reason="action change: the black liquid (not shown) — the strength leaves him and he falls unconscious again; sudden silence", chars=["aslam", "aadhambe", "zaahid", "naazim"], loc="tent",
         visual="Aslam lying limp and unconscious on his back on the mat, his face pale and peaceful, eyes closed; Zaahid and Naazim slowly letting go and sitting back on their heels, exhausted and breathing hard; old Aadhambe lowering his hands; lanky Raaidhu in a red t-shirt slumped at Aslam's feet; the lantern steadying to a low warm glow",
         camera="medium-wide, slightly high angle, the family in the upper two-thirds, the mat as the lower third",
         amb="tent_storm", sens="other", safe="the black liquid from his mouth is never shown; only the moment after, his face clean and calm"),
    dict(to=62, reason="dialogue: Zaahid, wiping his eyes, asks 'Is he saved?'; Aadhambe, grave: 'Only for now — the handi is in this jungle and wants Aslam's soul'", chars=["aadhambe", "zaahid", "aslam"], loc="tent", speaker="aadhambe",
         visual="old Aadhambe sitting cross-legged on the mat, centred, his face grave and weary, speaking quietly; Zaahid beside him at the side wiping his eyes with the back of his hand; Aslam lying unconscious in the foreground; the lantern's low warm light, deep shadows, rain-streaked canvas",
         camera="medium shot, eye level, Aadhambe centred in the upper half, Zaahid at the side, Aslam and the mat as the lower third",
         amb="tent_storm"),
    dict(to=64, reason="speaker change: Naazim reminds them the dhoni's engine is broken; hopes fade — then a sliding sound on the sand outside", chars=["naazim", "zaahid", "shareefa", "aisha"], loc="tent", speaker="naazim",
         visual=f"the family sitting together in a tight circle on the mat in the lantern-lit tent: big bearded Naazim centred, speaking with a heavy, hopeless face, one hand open; Zaahid, {SHAR} and {AISH} sitting around him despondent, all heads beginning to turn towards the closed door flap at the side; nobody lying down; the lantern low",
         camera="medium-wide, eye level, Naazim centred in the upper half, the family around, the mat as the lower third",
         amb="tent_storm"),
    dict(to=65, reason="action change: Naazim slowly lifts the tent's door flap and looks out into the rain", chars=["naazim"], loc="tent_door",
         visual=f"seen from outside: big bearded Naazim in the tent doorway, slowly lifting the canvas door flap with one hand, leaning out and staring towards the sea with wide eyes; warm lantern light behind him; rain slanting across the frame",
         camera="medium shot, eye level, Naazim's face centred in the upper half, the wet lit sand as the lower third",
         amb="beach_storm_night"),
    dict(to=66, reason="reverse shot / reveal: by the frothing waves the handi stands in white, facing the tent; the surf roars louder where she stands", chars=["handi"], loc="shore",
         visual=f"{HANDI}, standing still at the edge of the frothing waves, facing straight towards the viewer (the tent); the waves around her rising higher and wilder than elsewhere, white foam swirling at her bare feet; rain; distant lightning",
         camera="wide shot from the tent door, the spirit small but centred in the upper two-thirds, the wet sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the spirit modestly covered (bible rule 2)"),
    dict(to=67, reason="return to Naazim frozen in the doorway as lightning reveals the scene (shot / reverse-shot)", chars=["naazim"], loc="tent_door",
         reuse="beat_028", amb="beach_storm_night", visual="(reuse of beat_028)", transition="cut"),
    dict(to=68, reason="emotional peak: a lightning flash shows her in the surf — her long 'hair' spread over the foam, two red eyes glowing like lit lamps", chars=["handi"], loc="shore",
         visual=f"closer view of {HANDI.replace('a faint sea-green glow around her', 'her eyes now glowing blood-red like two lit lamps in the dark')}, standing among the breaking waves, the long dark smoky ribbons spreading out over the white foam like a net; a white lightning flash behind, rain; menacing and still",
         camera="medium shot, low angle, her face and red glowing eyes in the upper half, the foaming waves as the lower third",
         amb="beach_storm_night", sens="other", safe="'long hair spread over the foam' drawn as dark smoky ribbons from under her opaque veil (bible rule 2)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Even as the drops of the pouring rain were striking her body, she felt no coldness at all.")
sh(2, "The girl slowly began to walk towards Aslam. As she walked, not a single sound came from the leaves on the ground.")
sh(3, "She seemed to be flying through the air like a light leaf in the wind. Closing the distance between her and Aslam, she raised her long cold hand towards Aslam's face.",
   hum=True)
sh(4, "The nails of her fingers were long and black. \"Come to me...\"", speaker="handi", hum=True)
sh(5, "Though the girl's lips did not move, that voice echoed inside Aslam's head. Aslam slowly raised his hand and tried to take hold of the girl's hand.",
   hum=True)
sh(6, "At that moment a voice from far away struck his ear. \"Asla...m! My son! Where are you?\"", speaker="zaahid")
sh(7, "It was the voice of his father Zaahid. With that voice a sudden jolt went through Aslam's body. He came back to his senses.",
   [("gasp", "ސިހުމެއް", -18)])
sh(8, "He could now see the figure in front of him properly. At that moment the beauty suddenly faded from the lovely girl's face, and a face with shrivelled skin appeared.",
   [("thunder", "ކުއްލިއަކަށް", -16)], hum=True)
sh(9, "At that moment something black and liquid could be seen running from that thing's two eyes. Her bewitching smile changed into a terrifying smile.",
   hum=True)
sh(10, "On the face showed the dread of something dead for many, many years. Aslam tried to scream in terror. But no sound came out of him.",
   [("breath_heavy", "ހަޅޭއްލަވައިގަންނަން", -20)], hum=True)
sh(11, "Stumbling backwards in total panic, he caught his foot on a tree root and fell to the ground. \"Look — a light!\"",
   [("soft_thud", "ވެއްޓުނު", -16)])
sh(12, "Raaidhu shouted loudly, pointing his arm towards the western side of the jungle. Zaahid and Naazim looked that way.",
   speaker="raaidhu")
sh(13, "Among the trees a pale blue-green light was glowing. It was not the light of an ordinary lamp. \"Aslam!\"",
   hum=True)
sh(14, "Zaahid ran that way with all his strength. Aadhambe tried to stop him, but stopping the steps of a father burning with love for his child is not something that can be done.",
   [("footsteps_sand", "ދުއްވައިގަތް", -18)])
sh(15, "When they ran and reached that spot, they found Aslam lying unconscious on the ground. His body was completely cold.",
   [("footsteps_sand", "ދުވެފައި", -20)], hum=True)
sh(16, "But the most frightening thing was the strange black drawings written in the sand all around Aslam, and the mark of a wet black handprint on his shirt.",
   hum=True)
sh(17, "\"Aslam! My son, open your eyes!\" Zaahid raised Aslam's body up and took him into his arms.",
   [("cloth_rustle", "ތެދުކޮށްލައި", -22)], speaker="zaahid")
sh(18, "At that moment, above their heads, from among the screw-pine trees, with a dreadful sound like a bird shrieking, a huge shadow was seen flying away.",
   [("wind_howl", "ހަޅޭއްލަވައިގަންނަފަދަ", -16), ("wings_flap", "އުދުހިގެން", -14)], hum=True)
sh(19, "With that, the storm winds that had taken over the whole island grew ten times stronger than before, and the light of the torches they carried suddenly went out!",
   [("wind_gust", "ވައިރޯޅިތައް", -14), ("flashlight_click", "ނިވިއްޖެ", -18)], hum=True)
sh(20, "The whole jungle sank into a dreadfulness filled with darkness. As the torches' light suddenly died, a pitch-black darkness took over everything around them.")
sh(21, "Out of a darkness so blind one could not even tell the four directions, the drops of the heavy rain felt like tiny needles piercing the body.")
sh(22, "With the force of the wind, it seemed the trees would be torn out by their roots. \"Bappa! Naazim! Where are you?\" Raaidhu screamed in fear.",
   [("wind_howl", "ގަދަކަމުން", -18)], speaker="raaidhu", hum=True)
sh(23, "He kept groping about with his hands in the pitch darkness. \"Stay calm! I'm right here!\" Zaahid's voice was heard.",
   speaker="zaahid")
sh(24, "He was sitting on the ground holding the unconscious Aslam's body tight against his chest. The cold rising from Aslam's body was seeping into Zaahid like a block of ice.",
   [("heartbeat", "ބާރުކޮށްލައިގެން", -22)])
sh(25, "At that moment the sound of grandfather beginning to recite the Quran was heard. He recited Aayathul Kursi with great steadfastness.",
   speaker="aadhambe")
sh(26, "With grandfather's voice, the dreadful sounds of the trees and the secret sounds around them seemed to grow fainter and quieten.",
   [("leaves_rustle", "ގަސްތަކުގެ", -22)])
sh(27, "Naazim kept trying to switch on his phone's light, but the phone would not work. The phone with a fully charged battery was dead. \"This is",
   [("flashlight_click", "ދިއްލާލަން", -20)], crop="tight")
sh(28, "the doing of that bird that flew off,\" Aadhambe said after breaking off his recitation. \"Quickly, let's take Aslam and go to the beach.",
   speaker="aadhambe")
sh(29, "If we stay in this jungle, these things will play with all of our minds.\" \"But how will we even get out of here? Nothing can be seen.\"",
   speaker="aadhambe")
sh(30, "Zaahid said worriedly. As soon as Zaahid said that, Naazim's torch flickered and came on. Naazim and Zaahid together lifted Aslam up.",
   [("flashlight_click", "ދިއްލުނު", -16)])
sh(31, "Guided by Aadhambe, they slowly stepped out of the jungle and reached the tent pitched on the beach.",
   [("footsteps_sand", "ފިޔަވަޅު", -20)])
sh(32, "As Aslam was carried into the dim light of the oil lantern inside the tent, Shareefa and Aisha came running, crying.",
   [("cloth_rustle", "ދުވެފައި", -22)])
sh(33, "\"What has happened to my son?\" Shareefa laid her hand on Aslam's face.", speaker="shareefa")
sh(34, "Aslam's face was completely white and strangely swollen. His lips had turned black. Everyone was frightened — though he was breathing — because of a smell coming from his body.",
   hum=True)
sh(35, "It was a stench of rotting fish from the jungle and of something burning. \"Grandpa!")
sh(36, "Let's leave this island quickly!\" Aslam's wife Aisha, crying, took hold of Aslam's hand. At that moment Aisha started and snatched her hand back.",
   [("gasp", "ސިހިފައި", -18)], speaker="aisha")
sh(37, "\"Aslam's hand is so hot! But father said it was very cold.\" Suddenly the unconscious Aslam opened both his eyes.",
   [("heartbeat", "ހުޅުވާލި", -20)], speaker="aisha", hum=True)
sh(38, "His eyes kept moving as if searching for something. Everyone drew back. The black of Aslam's eyes had vanished completely; the whole eye was white.",
   hum=True)
sh(39, "The muscles of his face stretched, and a look too frightening for a human came over his face. He sat up and, staring out through the tent door into the pouring rain, began to laugh.",
   [("cloth_rustle", "ތެދުވެ", -22)])
sh(40, "That was not Aslam's voice. It was a bewitching, dreadful woman's voice, as if heard from the jungle, that seemed to shake the whole island!",
   hum=True)
sh(41, "\"She has come... she has come for me...\"", speaker="aslam", hum=True)
sh(42, "A heavy woman's voice came out of Aslam's young body. At that heavy woman's voice from Aslam's mouth, the hearts of everyone in the tent seemed to stop.",
   [("heartbeat", "ވިންދު", -20)], hum=True)
sh(43, "Shareefa cried out in fear and hid the little children behind her. Aisha stood stunned.",
   [("gasp", "ހަޅޭއްލަވައިގަނެ", -18), ("cloth_rustle", "ފޮރުވި", -22)])
sh(44, "From her beloved husband's body came a voice she had never heard before. \"Father! What kind of thing has befallen us?\"",
   crop="tight")
sh(45, "Zaahid looked towards Aadhambe in fear. Grandfather was deeply shaken. But grandfather knew that this was no time to give in to fear.")
sh(46, "He did not let go of his firmness. He went down on his knees and faced Aslam. In Aadhambe's eyes was a look full of determination.",
   [("cloth_rustle", "ތިރިވެ", -24)])
sh(47, "He raised his right hand and tried to rest it on Aslam's forehead. At that moment Aslam suddenly seized Aadhambe's hand.",
   [("gasp", "ހިފި", -18)])
sh(48, "His grip felt as strong and cold as an iron blade. \"Old man!",
   [("heartbeat", "ދަގަނޑު", -20)], speaker="aslam", hum=True)
sh(49, "Do you think you can break my power?\" Once again that heavy voice came out of Aslam's mouth.", speaker="aslam", hum=True)
sh(50, "Through his white eyes the veins showed and began to turn red. \"By Allah's leave, your power will leave this body!\"",
   speaker="aadhambe", hum=True)
sh(51, "Aadhambe said it loudly. And after freeing his left hand from Aslam's grip, he began to recite Surat al-Jinn aloud.",
   speaker="aadhambe")
sh(52, "As grandfather began to recite, strong convulsions seized Aslam's body. Writhing on the ground, he clamped his hands over his own ears and began to cry and scream.",
   [("cloth_rustle", "ފުރޮޅެމުން", -20)], hum=True)
sh(53, "It was a scream like a heart bursting with pain. The tent's canvas whipped in the wind harder than ever. The lantern's light flared bright, dimmed and swirled.",
   [("wind_gust", "ތެޅެމުންދިޔައީ", -14), ("bulb_flicker", "ދިއްލި", -18)], hum=True)
sh(54, "\"Naazim! Zaahid! Hold him down!\" Grandfather gave the order without breaking off his recitation.", speaker="aadhambe", crop="medium")
sh(55, "Zaahid and Naazim ran over and held down Aslam's two arms and two legs. But that young man's body had the strength of four men.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(56, "He tried to throw them off. Raaidhu too ran over and threw himself on Aslam's legs. Aadhambe made his recitation stronger.",
   [("cloth_rustle", "އޮބިއަޅާލި", -20)], hum=True)
sh(57, "His voice echoed through the whole tent. Suddenly a black liquid spilled from Aslam's mouth onto the ground.")
sh(58, "With that all the strength left his body, and he fell to the ground unconscious once more. A sudden silence came over everything.",
   [("soft_thud", "ވެއްޓުނު", -18)])
sh(59, "There was no sound except the rain outside. Everyone was breathless. \"Father... is he saved?\"",
   speaker="zaahid", crop="tight")
sh(60, "Zaahid asked, wiping his eyes. Aadhambe drew a deep breath. \"For now, the power of that thing has been broken.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(61, "But this is only the beginning. That handi is here in this island's jungle. What she wants is", speaker="aadhambe", hum=True)
sh(62, "Aslam's soul. We have to survive this night here.\" \"But", speaker="aadhambe", hum=True)
sh(63, "isn't the dhoni's engine broken?\" As Naazim reminded them, everyone's hopes faded once again.",
   [("sigh", "ފަނޑުވި", -22)], speaker="naazim")
sh(64, "At that moment, from outside the tent, came a sound like something sliding over the white sand. A sound like 'shhhh'.",
   [("cloth_rustle", "ދެމެމުންދާ", -16)], hum=True)
sh(65, "Naazim slowly lifted the tent's door flap. Outside, through the pouring rain, beside the frothing waves, stood that woman — the handi, in a white frock.",
   [("cloth_rustle", "ދޮރުފޮތިގަނޑު", -18), ("wave_crash", "ރާޅުތަކުގެ", -16)], hum=True)
sh(66, "She stood staring towards the tent's door. The most frightening thing was that the waves of the sea where she stood roared louder than ordinary waves.",
   [("wave_crash", "ގަދަވެގެންދާ", -14)], hum=True)
sh(67, "Naazim's eyes widened and his whole body froze at the dreadfulness of the scene he saw in a flash of lightning.",
   [("thunder", "ވިދުވަރަކާއެކީގަ", -12)], hum=True)
sh(68, "Among the waves rushing up onto the shore, a girl could be seen standing. Her long hair lay spread over the foam, and her two red eyes were glowing in the dark like lit lamps.",
   [("wave_crash", "ބިންދަމުންދިޔަ", -16), ("heartbeat", "ދިއްލެމުންދިޔައީ", -18)], hum=True)
SHOTS = S

"""Beat/shot plan for Handi Kujaa episode 580 (series opener; used by plan_beats.py)."""

LOC = {
    "sea_crossing": "the open sea of a Maldivian atoll on a bright holiday morning: calm, glassy turquoise and deep-blue water smooth as silk, a wooden Maldivian dhoni with a small cabin (gegandu) on deck cutting a white wake, a tiny green island with white sand and coconut palms on the horizon",
    "dhoni_prow": "the curved wooden prow and front deck of a family's Maldivian dhoni on a bright sunny morning, the small wooden cabin behind, the turquoise sea and a white sky with a few soft clouds all around",
    "lagoon_landing": "the clear shallow turquoise lagoon of the uninhabited picnic island Beenaafushi at hot early afternoon: the wooden dhoni anchored close to shore, knee-deep crystal water over white sand, powder-white beach and leaning coconut palms",
    "beach_camp": "the powder-white beach of Beenaafushi in the hot early afternoon: a shady spot under leaning coconut palms with woven mats, bags, a small cooking fire of coconut husks with a pot and a kettle, tea cups on a tray, the clear turquoise lagoon beyond",
    "beach_wide": "a wide view of Beenaafushi's long powder-white beach and turquoise lagoon at midday: coconut palms, dark coral rocks at the far shore, the dense dark-green jungle behind the beach, the family's small picnic camp under the palms and their dhoni anchored in the lagoon",
    "storm_beach": "Beenaafushi's beach after four in the afternoon as a storm arrives: a huge black storm cloud rolling in from the north and swallowing the sky, coconut palms bending and thrashing in the wind, the lagoon darkening and choppy, sand whipping along the beach, the family's picnic things scattered",
    "lagoon_storm": "the edge of Beenaafushi's lagoon in the rising storm late in the afternoon: the wooden dhoni rocking hard on wild grey-green waves near the reef channel, spray over its wooden stern and tiller, a black sky",
    "sunset_beach": "Beenaafushi's beach at a dreadful sunset during the storm: a burning orange-violet band of light under massive black-violet clouds, palms thrashing, the dark jungle edge behind, the dhoni stranded in the lagoon",
    "west_shore": "the island's west shore at stormy dusk: dark wet coral rocks and big breaking waves, white foam, a last strip of orange light under black clouds, palms bending, the dark jungle behind",
    "jungle_clearing": "a small sparse clearing inside the dense dark jungle of Beenaafushi on a stormy night: black screw-pines, magoo shrubs and huge old twisted trees around, wet leaf litter on the ground, silver rain",
    "jungle_path": "the dense dark jungle of Beenaafushi on a stormy night: black twisted tree trunks, screw-pine leaves and hanging roots, wet leaves underfoot, silver rain falling through the canopy",
    "tent_night": "inside the family's large canvas camping tent on the beach on a stormy night: canvas walls bellying and straining in the wind, a single oil lantern (faanoos) hanging from the centre pole, woven mats on the sand floor, bags and folded clothes",
    "tent_flap": "the open flap of the family's canvas tent on the beach on a stormy night, warm lantern light behind, and outside nothing but pitch-black darkness and slanting silver rain",
    "jungle_torch": "the edge and inside of Beenaafushi's dense dark jungle on a stormy night, torch beams cutting through the rain between black tree trunks and screw-pines, huge tree shadows stretching across the leaves",
    "banyan_roots": "deep in the jungle on a stormy night: the vast twisting roots of an enormous ancient nika (banyan) tree forming dark hollows, wet leaves and mud between them, torch beams and rain",
}
MOOD = {
    "sea_crossing": "bright sunny holiday morning, brilliant turquoise and white, clear sky, sparkling water, joyful and peaceful, no storm, no night colours",
    "dhoni_prow": "bright sunny morning, warm sunlight, turquoise sea and white sky, happy and carefree, no storm, no night colours",
    "lagoon_landing": "hot bright early afternoon, blazing sun, glittering turquoise water, white sand, cheerful holiday mood, no storm, no night colours",
    "beach_camp": "hot early afternoon, dappled palm shade on white sand, warm golden-white light, relaxed and happy, no storm, no night colours",
    "beach_wide": "bright midday sunshine, turquoise and white, a calm, peaceful, deserted-island feeling, no storm, no night colours",
    "storm_beach": "sudden storm late afternoon: bruised violet-grey light, a black sky closing in, wind-whipped and ominous",
    "lagoon_storm": "storm late afternoon: bruised grey-violet light, dark choppy water, spray and wind, tense and alarming",
    "sunset_beach": "dreadful sunset: a narrow band of burning orange under massive black-violet storm clouds, long dark shadows, foreboding",
    "west_shore": "stormy dusk turning to night: the last orange glow fading under black-violet clouds, dark sea, white foam, rain beginning, a white lightning flash",
    "jungle_clearing": "storm night: near-black indigo, silver rain, an eerie cold sea-green spectral glow coming from the woman in white, white lightning in the canopy, hypnotic and frightening",
    "jungle_path": "storm night: near-black indigo jungle, silver rain, faint white lightning, a cold sea-green glow, dreadful and claustrophobic",
    "tent_night": "tent at night: a single warm amber oil-lantern light, deep shadows, canvas walls shaking, the storm roaring outside, anxious and fearful",
    "tent_flap": "storm night: warm lantern light behind against the pitch-black rainy darkness outside, silver rain streaks, desperate",
    "jungle_torch": "torchlit jungle on a storm night: white-yellow torch beams in near-black indigo darkness, silver rain, giant tree shadows, dread",
    "banyan_roots": "torchlit jungle on a storm night: harsh torch light on wet roots, near-black indigo surroundings, silver rain, a faint grey haze, horror and dread",
}

WETM = "clothes darkened by rain but still loose and opaque, hair wet"
HANDI = ("her opaque loose long-sleeved ankle-length white gown and opaque white veil fully covering her hair and neck, "
         "long dark smoky ribbons trailing from under the veil on the wind")
KIDS = "three small children (girls in small headscarves fully covering their hair)"

BEATS = [
    dict(to=3, reason="episode opening: the family's dhoni crossing the silk-blue sea towards Beenaafushi on a sunny holiday morning", loc="sea_crossing",
         visual="a bright, joyful wide view from slightly above of a wooden Maldivian dhoni gliding over a calm, silky turquoise sea, a white wake behind it; on deck under the cabin roof the small figures of a family of ten on holiday - an old man in a white skullcap, men in shirts, women in long dresses and hijabs fully covering their hair; far ahead on the horizon a tiny green island ringed with white sand and coconut palms; brilliant sunshine, a clear sky; no lettering on the boat",
         camera="wide high-angle establishing shot, the dhoni and the island horizon in the upper two-thirds, smooth turquoise water as the calm lower third",
         amb="sea_boat"),
    dict(to=7, reason="characters introduced: Aslam at the dhoni's prow calls to his father Zaahid, who smiles up at the sky (two-shot for both speakers)", chars=["aslam", "zaahid"], loc="dhoni_prow",
         visual="Aslam standing at the curved wooden prow of the dhoni in the sunshine, turning back with a big excited grin and one arm flung out towards the sea, talking; his father Zaahid a step behind him on the deck, smiling contentedly and gazing up at the clear sky; both faces clearly visible in three-quarter view; sparkling turquoise sea and white sky behind them",
         camera="medium two-shot at eye level, Aslam slightly left and Zaahid slightly right, both faces in the upper half, the wooden deck as the lower third",
         amb="sea_boat"),
    dict(to=9, reason="scene change: they land in Beenaafushi's lagoon; Raaidhu helps grandfather down, Aslam helps his mother", chars=["raaidhu", "aadhambe", "aslam", "shareefa"], loc="lagoon_landing",
         visual="the family climbing down from the side of the anchored dhoni into knee-deep crystal turquoise water: lanky Raaidhu in the water holding grandfather Aadhambe's hand and arm, carefully helping the old man down, Aadhambe holding his walking stick; behind them Aslam reaching up to help his mother Shareefa step down from the boat, her long maroon dress and black hijab fully covering hair and neck; blazing sun, glittering water, white beach and palms beyond",
         camera="medium-wide, eye level, the four figures and the dhoni's side in the upper two-thirds, the clear turquoise water over white sand as the lower third",
         amb="beach_day"),
    dict(to=11, reason="action change: grandfather and mother set up the cooking and the afternoon tea while the children play in the lagoon", chars=["aadhambe", "shareefa", "aisha"], loc="beach_camp",
         visual=f"a happy picnic camp in the palm shade on the white beach: grandfather Aadhambe sitting on a woven mat stirring a pot over a small coconut-husk fire, Shareefa beside him pouring tea from a kettle into cups on a tray, Aisha in her lavender dress and white hijab laughing as she lays out food; in the background at the water's edge {KIDS}, fully dressed, splashing and playing in the shallow turquoise water and on the white sand, small and far away; everyone smiling",
         camera="medium-wide, eye level, the adults' faces and the camp in the upper two-thirds, the dappled white sand directly in front of the mat as the lower third, one seamless continuous painting with no seams or panels",
         amb="beach_day"),
    dict(to=13, reason="scene/time change: by midday the two other groups' dhonis leave - the family has the island to themselves", loc="beach_wide",
         visual="a wide, peaceful view of the long powder-white beach and turquoise lagoon at midday: two small wooden dhonis motoring away towards the horizon, leaving white wakes; the family's single dhoni still anchored near shore; their small picnic camp under the palms with tiny distant figures; the dense dark-green jungle rising behind the beach; empty sand everywhere else; no lettering on any boat",
         camera="wide establishing shot, the lagoon, departing boats and palms in the upper two-thirds, smooth white sand as the lower third",
         amb="island_day"),
    dict(to=16, reason="time jump and turning point: after 4 pm a black cloud from the north swallows the sky; Aadhambe shouts to Zaahid to call the skipper", chars=["aadhambe", "zaahid", "shareefa"], loc="storm_beach", speaker="aadhambe", transition="black",
         visual="grandfather Aadhambe standing on the wind-whipped beach gripping his long stick, his white kurta and checked sarong flapping, pointing urgently at a gigantic black storm cloud rolling in over the sea from the north, his face alarmed, shouting; Zaahid beside him turning towards the lagoon, worried; Shareefa behind them hurriedly gathering cups and bags, her black hijab fully covering hair and neck; coconut palms bending and thrashing, leaves tearing in the wind, the lagoon turning dark",
         camera="medium-wide, low angle, Aadhambe centred and sharp with the black cloud above him in the upper two-thirds, the blowing sand as the lower third",
         amb="island_storm_day"),
    dict(to=17, reason="scene/action change: trying to leave the lagoon in wild waves, something tangles in the propeller and the engine dies", chars=["sameer"], loc="lagoon_storm",
         visual="the wooden dhoni pitching on wild grey-green waves at the edge of the lagoon, spray bursting over its stern; the skipper Sameer leaning far over the stern rail beside the wooden tiller, staring down into the churning water at the propeller with a tense, dismayed face, one hand raised to signal to the shore; a black sky; no lettering on the boat",
         camera="medium-wide, eye level from the water, Sameer and the dhoni's stern in the upper two-thirds, the churning water as the lower third",
         amb="island_storm_day"),
    dict(to=19, reason="time change and new speaker: stranded at a dreadful sunset, Shareefa calls to Aslam not to go far into the jungle", chars=["shareefa", "aisha"], loc="sunset_beach", speaker="shareefa",
         visual=f"Shareefa standing on the beach at a dreadful sunset, her maroon dress and black hijab (fully covering hair and neck) whipped by the wind, both hands cupped around her mouth, calling anxiously towards the dark edge of the jungle; Aisha behind her at the side holding {KIDS} close, small in the background; above them a narrow band of burning orange light under massive black-violet clouds spreading over the island like a dreadful curtain; the dhoni stranded in the lagoon; palms thrashing",
         camera="medium shot, slightly low angle, Shareefa centred and sharp in the upper half, the dark sand as the lower third",
         amb="beach_dusk"),
    dict(to=21, reason="scene change: Aslam alone on the west shore watching the storm waves - thunder, and the rain begins to pour", chars=["aslam"], loc="west_shore",
         visual="Aslam standing alone on dark wet coral rocks on the island's west shore at stormy dusk, seen in three-quarter view from behind, his open checked shirt flapping in the wind, watching huge waves crash into white foam; a branching white lightning bolt splitting the black-violet sky over the sea, the first heavy slanting rain starting to fall; the last strip of orange light on the horizon",
         camera="wide shot, eye level, Aslam and the lightning over the sea in the upper two-thirds, the dark wet rocks and foam as the lower third",
         amb="beach_dusk"),
    dict(to=25, reason="scene change and reveal: running back through the jungle he sees a woman in white in a small clearing, her long dark 'hair' flowing in the wind, eyes glowing, a bewitching smile", chars=["handi", "aslam"], loc="jungle_clearing",
         visual=f"over Aslam's shoulder from behind (his back, wet hair and rain-dark checked shirt soft in the foreground at the side): in the middle of a small clearing among black twisted trees stands a tall, unearthly beautiful woman in {HANDI}, the smoky ribbons streaming far behind her in the storm wind; her luminous pale-olive face turned towards him, eyes glowing faintly sea-green like a cat's in the dark, a calm bewitching smile; a soft cold sea-green glow around her lighting the silver rain; the jungle black all around",
         camera="over-the-shoulder medium-wide, the woman centred and sharp in the upper half, Aslam's shoulder soft at the side, the dark wet leaf litter as the lower third",
         amb="jungle_storm_night", sens="other", safe="the narration's long black hair is drawn as dark smoky ribbons trailing from under an opaque white veil; opaque modest gown"),
    dict(to=27, reason="reverse shot / emotional change: Aslam frozen to the ground, heart racing - 'Is she human? Or a handi?'", chars=["aslam"], loc="jungle_path",
         visual=f"close-up of Aslam standing frozen among the black trees in the pouring rain, {WETM}, his face pale and lit by a cold sea-green glow from in front of him, eyes wide and fixed, lips parted, rain running down his face, uncertain between fascination and fear",
         camera="close-up, eye level, his face in the upper half, his rain-dark shirt and the dark trunks as the lower third",
         amb="jungle_storm_night"),
    dict(to=28, reason="action change: she slowly raises her hand and beckons; her eyes turn red in the darkness", chars=["handi"], loc="jungle_clearing",
         visual=f"the woman in white in the dark clearing, {HANDI}; her gown is made of thick heavy matte white cotton, fully opaque with no translucent layers, falling in wide loose folds that hide any body shape; slowly raising one pale long-fingered hand and beckoning with a curl of her fingers; her eyes now glowing an eerie red in the darkness, the smile still sweet; the sea-green glow around her darkening, rain falling through the light; black twisted trees behind",
         camera="medium shot, eye level, her face and beckoning hand centred in the upper half, the dark leaf litter and her bare feet as the lower third",
         amb="jungle_storm_night", sens="other", safe="horror conveyed only by red glowing eyes in the dark; she remains fully covered and beautiful"),
    dict(to=30, reason="return to Aslam (reverse shot): goose-bumps, he realises she is not of this world, but cannot run", chars=["aslam"], loc="jungle_path",
         reuse="beat_011", amb="jungle_storm_night", visual="(reuse of beat_011)", transition="cut"),
    dict(to=31, reason="return to her (shot): her long dark tresses dance in the wind like living things", chars=["handi", "aslam"], loc="jungle_clearing",
         reuse="beat_010", amb="jungle_storm_night", visual="(reuse of beat_010)", transition="cut"),
    dict(to=32, reason="return to Aslam (reverse shot): a soft voice whispers his name and he starts", chars=["aslam"], loc="jungle_path",
         reuse="beat_011", amb="jungle_storm_night", visual="(reuse of beat_011)", transition="cut"),
    dict(to=35, reason="action change: the handi steps back into the jungle, her soaked white gown glowing like light from the deep sea, drawing him after her", chars=["handi"], loc="jungle_path",
         visual=f"the beautiful handi stepping slowly backwards between black tree trunks into the deeper jungle, still facing the viewer with her glowing sea-green eyes and an inviting smile, {HANDI}; rain pours on her yet the gown stays opaque and gives off a strange cold blue-green light like light rising from the depths of the sea, lighting the wet leaves and hanging roots around her; she seems to float",
         camera="medium-wide, eye level, her figure and face centred in the upper two-thirds, the glowing wet leaf litter as the lower third",
         amb="jungle_storm_night", sens="other", safe="the soaked gown stays opaque and loose; the glow comes from the cloth"),
    dict(to=38, reason="action change: Aslam tears himself away to run - and a terrible growl shakes the whole jungle", chars=["aslam"], loc="jungle_path",
         visual=f"Aslam half turned in mid-stride, trying to run back towards the beach through the black jungle, teeth clenched, {WETM}, his face twisted in terror as he looks back over his shoulder; around him the huge trees bending and their leaves shaking violently as if the whole jungle is trembling from a deep growl, rain flung sideways, a white lightning flash through the canopy; no creature visible, no faces in the shadows",
         camera="medium shot, eye level, Aslam's terrified face in the upper half, the dark wet ground as the lower third",
         amb="jungle_storm_night", sens="other", safe="the growl is shown only as the trembling jungle and Aslam's terror; no monster"),
    dict(to=41, reason="scene change: the family in the storm-lashed tent; Aadhambe recites Quran, Shareefa near tears asks where Aslam is", chars=["shareefa", "aadhambe", "aisha", "zaahid"], loc="tent_night", speaker="shareefa",
         visual=f"inside the canvas tent lit by a single swinging oil lantern, the walls bellying in the wind: Shareefa kneeling in the foreground centre, her black hijab fully covering hair and neck, her face anguished and close to tears, turned to speak towards Zaahid at the side; behind her grandfather Aadhambe sitting cross-legged on a mat, eyes closed, cupped hands raised, reciting from memory with a deeply troubled face; Aisha in lavender and white hijab sheltering {KIDS} small in the background",
         camera="medium shot, eye level, Shareefa centred and sharp in the upper half with Aadhambe behind, the woven mat floor as the lower third",
         amb="tent_storm", sens="other", safe="recitation shown with raised cupped hands, no visible Quran pages or text"),
    dict(to=43, reason="action/speaker change: Zaahid at the tent flap shouts Aslam's name into the black rain, his voice lost in the wind", chars=["zaahid"], loc="tent_flap",
         visual="Zaahid standing in the open flap of the tent with both hands cupped around his mouth, shouting with all his strength out into the pitch-black night, rain blowing into his face, his sky-blue shirt darkened by rain; warm lantern light behind him, nothing but darkness and slanting silver rain in front",
         camera="medium shot from slightly outside the tent, Zaahid centred and sharp in the upper half, the wet sand at the threshold as the lower third",
         amb="tent_storm"),
    dict(to=45, reason="characters enter: big Naazim switches on a torch and steps out into the rain to search; Raaidhu wants to come too", chars=["naazim", "raaidhu"], loc="tent_flap", speaker="naazim",
         visual=f"huge broad-shouldered Naazim in his dark-green t-shirt stepping out of the tent flap into the rain, switching on a big torch whose white beam cuts through the darkness, his bearded face determined; just behind him in the lantern-lit opening lanky Raaidhu in his red t-shirt leaning forward eagerly, calling after him; both faces clearly visible",
         camera="medium shot, eye level, Naazim centre-left and Raaidhu centre-right with both faces in the upper half, the wet sand and torch glow as the lower third",
         amb="beach_storm_night"),
    dict(to=48, reason="speaker change / turning point: Aadhambe breaks off his recitation - 'Nobody goes into the jungle! This is no ordinary storm'", chars=["aadhambe"], loc="tent_night", speaker="aadhambe",
         visual="close-up of grandfather Aadhambe sitting in the lantern-lit tent, his hands lowered from recitation, holding up one hand firmly, his eyes wide and fearful yet stern, speaking in a hard voice; deep shadows on the shaking canvas behind him, the lantern flame wavering",
         camera="medium close-up, eye level, Aadhambe's face centred in the upper half, his hands and white kurta as the lower third",
         amb="tent_storm"),
    dict(to=49, reason="return to Zaahid (reverse shot): 'But Bappa, Aslam is out there alone'", chars=["zaahid"], loc="tent_flap",
         reuse="beat_019", amb="tent_storm", visual="(reuse of beat_019)", transition="cut"),
    dict(to=51, reason="action change: Aadhambe rises leaning on his long stick - 'Let's go, but all together; take the torches'", chars=["aadhambe", "zaahid", "naazim", "raaidhu"], loc="tent_night", speaker="aadhambe",
         visual="grandfather Aadhambe rising to his feet in the lantern-lit tent, leaning his weight on his long wooden stick, his face resolute, speaking; around him Zaahid, huge Naazim and lanky Raaidhu picking up torches, tense; the canvas walls shaking in the storm",
         camera="medium shot, slightly low angle, Aadhambe centred and sharp in the upper half, the men around him, the mat floor as the lower third",
         amb="tent_storm"),
    dict(to=53, reason="scene change: the four men enter the jungle with torches while the women pray in the tent; tree shadows like giant ghosts", chars=["naazim", "zaahid", "aadhambe", "raaidhu"], loc="jungle_torch",
         visual="from behind, four men walking in a tight group into the black jungle in the pouring rain - huge Naazim in a dark-green t-shirt in front, Zaahid in a sky-blue shirt, grandfather in a white skullcap with his long stick, lanky Raaidhu in a red t-shirt - their torch beams spreading among the tree trunks; the huge shadows of the trees stretching and swirling around them like giant looming ghosts; far behind them through the trees the small warm glow of the tent on the beach",
         camera="wide shot from behind at eye level, the men and torch beams in the upper two-thirds, the dark wet leaves as the lower third",
         amb="jungle_storm_night", sens="other", safe="the 'giant ghosts' are only tree shadows; no faces in the shadows"),
    dict(to=56, reason="action change: a loud crash on the right - Naazim's torch reveals the huge roots of a giant nika tree; everyone's breath catches", chars=["naazim", "zaahid", "raaidhu"], loc="banyan_roots",
         visual="huge Naazim swinging his torch to the right, its white beam falling on the vast twisting roots of a gigantic ancient nika tree; Naazim, Zaahid and Raaidhu standing frozen side by side in the rain, faces lit by the torch glow, staring with wide eyes and held breath at something in the roots out of frame",
         camera="medium shot, eye level, the three torchlit faces in the upper half, the wet roots and mud as the lower third",
         amb="jungle_storm_night"),
    dict(to=58, reason="reveal: a large dead seabird caught in the roots, and a stench of sea rot and burning", loc="banyan_roots",
         visual="close view into a dark hollow of the giant twisting banyan roots lit by a torch beam: a large dark seabird lying still among the roots, half in shadow, its long wings spread, as if dropped there; rain dripping from the roots; a faint grey haze drifting in the torchlight; no wound, no blood, nothing gory",
         camera="close detail framing, the roots and the still bird in the upper two-thirds, dark mud and rain as the lower third",
         amb="jungle_storm_night", sens="violence", safe="the torn, bleeding seabird is shown only as a still bird in shadow with wings spread; no blood, no wound"),
    dict(to=59, reason="return to the men's faces: Naazim asks in a strained voice what this is", chars=["naazim", "zaahid", "raaidhu"], loc="banyan_roots",
         reuse="beat_025", amb="jungle_storm_night", visual="(reuse of beat_025)", transition="cut"),
    dict(to=61, reason="action change: Aadhambe steps forward and prods the bird with his stick; his eyes widen in fear", chars=["aadhambe"], loc="banyan_roots",
         visual="grandfather Aadhambe stepping slowly forward among the giant roots in the torchlight, lowering the tip of his long wooden stick towards a dark shape lying deep in the shadow of the roots; his eyes widening, fear spreading over his face; rain on his white skullcap and kurta; the dark shape indistinct; deep inside the dense jungle, surrounded only by black tree trunks, hanging roots and screw-pines - no tent, no beach, no sea and no boats visible",
         camera="medium shot, eye level, Aadhambe's face and the stick in the upper two-thirds, the roots and mud as the lower third",
         amb="jungle_storm_night", sens="other", safe="the worms falling from the bird are not shown; only Aadhambe's fearful face"),
    dict(to=63, reason="emotional turning point: Aadhambe whispers 'This was not done by humans - hurry, Aslam's life is in danger'", chars=["aadhambe"], loc="banyan_roots", speaker="aadhambe",
         visual="close-up of grandfather Aadhambe alone in the frame, his face lit from the side by the white glare of a torch held by someone out of frame, rain on his white skullcap, white beard dripping, eyes wide and grave, speaking in a low urgent whisper as he turns his head towards the black depths of the jungle; no other people in the image, no women, no lantern; only dark wet jungle leaves and rain behind him",
         camera="close-up, eye level, Aadhambe's face centred in the upper half, his shoulders and stick as the lower third",
         amb="jungle_storm_night"),
    dict(to=66, reason="scene change: deep in the jungle Aslam is lost in her spell, drowned in her gaze and blue light, feeling no cold", chars=["aslam"], loc="jungle_path",
         visual=f"Aslam standing motionless deep in the black jungle in the pouring rain, {WETM}, entranced: his face bathed in a soft blue-green glow from something in front of him, eyes glazed and dreamy, a faint lost smile, rain streaming over him unnoticed; everything around him dark and blurred",
         camera="medium close-up, eye level, his entranced face in the upper half, his rain-dark shirt as the lower third",
         amb="jungle_storm_night", sens="other", safe="the 'sickness of love' is shown only as an entranced, dreamy face; no touch"),
    dict(to=68, reason="action change: the handi glides slowly towards him, her feet making no sound on the leaves, as if floating on the wind", chars=["handi", "aslam"], loc="jungle_path",
         visual=f"over Aslam's shoulder (his back soft and dark in the foreground at the side): the handi gliding slowly towards him through the black jungle, {HANDI}, her bare feet hovering just above the wet fallen leaves without touching them, her gown and veil streaming as if she floats like a leaf on the wind; sea-green glowing eyes and a sweet smile; a cold blue-green glow and silver rain around her",
         camera="over-the-shoulder medium-wide, the handi centred in the upper two-thirds, the undisturbed wet leaves beneath her feet as the lower third",
         amb="jungle_storm_night", sens="other", safe="she stays a respectful distance away; no touch"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Over a sea the colour of blue, like a silken curtain, the dhoni sped along, bringing joy to the family's hearts.",
   [("dhoni_engine", "ދުވަމުންދިޔައީ", -20)])
sh(2, "Beenaafushi is a famous uninhabited island that everyone in the atoll travels to on weekends and special days.")
sh(3, "The island's white powdery sand and clear lagoon are always crowded with people. So the ten members of Aadhambe's family decided to go to that island to enjoy the holiday.")
sh(4, "\"Bappa! The weather's really clear today, isn't it?\" said young Aslam, standing at the dhoni's prow, to his father Zaahid.",
   speaker="aslam")
sh(5, "Aslam, only twenty-two, is the most talkative one in the family, and the young man most eager to explore islands.",
   speaker="aslam")
sh(6, "Zaahid smiled and looked up at the sky. \"Yes, my son. Today looks like it will be a really lovely day.\"",
   speaker="zaahid")
sh(7, "But this is the season when the weather changes quickly. Even before noon, this season is very hot.")
sh(8, "In that blazing heat the dhoni entered Beenaafushi's lagoon. The whole family climbed down excitedly. \"Grandpa, come down quickly!\"",
   [("splash", "ފޭބި", -20)])
sh(9, "Raaidhu took Aadhambe by the hand and slowly helped him down to the shore. At the same moment Aslam helped his mother Shareefa down too.",
   [("footsteps_sand", "ބޭލި", -22)])
sh(10, "With grandpa and mother in charge, they began to prepare the cooking and the afternoon tea. The little children swam in the lagoon and played on the clean white sand.",
   [("cup_clatter", "ސައިގެ", -24), ("splash", "ފަތާ", -24)])
sh(11, "Joy showed on every face. Since this is an island people always come to, the most pleasant spot on it goes to whoever arrives first.")
sh(12, "Having got that spot, the family was content. Around midday two more dhonis set off and left. Three groups had come today.",
   [("dhoni_engine", "ފުރައިގެން", -24)])
sh(13, "With two of those groups gone, Aadhambe's family had the island to enjoy all to themselves. After four in the afternoon, the atmosphere began to change suddenly.")
sh(14, "A heavy black cloud coming from the north wrapped the whole area. The winds grew strong and the leaves of the trees began to thrash.",
   [("wind_gust", "ވައިރޯޅިތައް", -16), ("leaves_rustle", "ހަލަބޮލިވާން", -18)], hum=True)
sh(15, "Clouds massed in the sky as if the rain would pour down any moment. Then Aadhambe told everyone to hurry back home without even having the afternoon tea.")
sh(16, "\"Zaahid! Call the skipper to the dhoni! A powerful storm is coming!\" Aadhambe shouted, worried.",
   speaker="aadhambe")
sh(17, "But at that moment the sea's waves turned wild, and while they were trying to take the dhoni out of the lagoon, something got tangled in its propeller - the skipper reported that the engine had stopped.",
   [("wave_crash", "ރާޅުތައް", -18), ("dhoni_engine", "ނެރެން", -20)], hum=True)
sh(18, "The whole family panicked. They were stuck on the island. The colours of sunset were spreading over the whole island like a dreadful curtain.",
   hum=True)
sh(19, "\"Aslam! My son, don't go too far into the jungle!\" Shareefa's cry rang out.",
   [("wind_gust", "ހަޅޭއްލަވައިގަތް", -20)], speaker="shareefa")
sh(20, "But in the strong wind that was blowing, it didn't seem that her voice reached Aslam. Aslam was on the beach on the island's west side.",
   [("wind_howl", "ވައިގެ", -18)])
sh(21, "He wanted to see how the sea's waves rise when a storm comes. Suddenly, with a loud clap of thunder, the rain began to pour.",
   [("wave_crash", "ރާޅުތައް", -20), ("thunder", "ގުގުރިއެއްގެ", -12), ("rain_start", "ވެހިގަތް", -16)])
sh(22, "Aslam hurried through the trees towards where the family was. But as soon as he entered the jungle, among the dense dark trees he saw a strange sight.",
   [("footsteps_sand", "އަވަސްވެގަތީ", -20), ("leaves_rustle", "ގަސްތަކުގެ", -22)], hum=True)
sh(23, "In a sparse clearing among the trees stood a woman in a white gown. Her hair was jet black, so long it touched the ground, flowing in the wind.",
   hum=True)
sh(24, "It was not a beauty one would ever see in a human being. The colour of her eyes glowed like a cat's eyes.",
   hum=True)
sh(25, "The young woman stood gazing at Aslam, with a bewitching smile on her lips.",
   crop="tight")
sh(26, "Aslam's feet froze to the ground. His heartbeat quickened and his whole body went cold. This was an island people always come to.",
   [("heartbeat", "ވިންދު", -18)], hum=True)
sh(27, "But on a stormy night like this, in this dense jungle, how could such a beautiful woman be alone? Was she human? Or... a handi?",
   speaker="aslam", hum=True)
sh(28, "The young woman slowly raised her hand and beckoned Aslam to come. At that moment Aslam saw the colour of her eyes turn red in the darkness.",
   hum=True)
sh(29, "Aslam's feet went cold and goose-bumps rose all over his body against his will. It dawned on him that the figure before him was not that of a worldly human.",
   [("breath_heavy", "ހީބިހި", -22)], hum=True)
sh(30, "But such was the pull in that girl's two eyes that his body had no courage to turn back and run.")
sh(31, "As the winds howled through the trees, the girl's long black hair seemed to dance in the wind like living tendrils.",
   [("wind_howl", "ކޭއްތެމުން", -18)])
sh(32, "\"Aslam...\" A soft, gentle and beautiful voice whispered at his ear through the wind. Hearing his own name, Aslam started.",
   [("gasp", "ސިހިގެން", -16)], hum=True)
sh(33, "On this uninhabited island, at such a dreadful hour, who would know his name? The young woman - or that beautiful handi - slowly took a step backwards.",
   hum=True)
sh(34, "Even as her white gown grew wet in the pouring rain, a strange light, like one rising from the depths of the sea, shone from the dress.")
sh(35, "Still gazing at Aslam, she began to go into the jungle. Aslam felt as if his feet had left the ground, as if he were compelled to follow that figure.",
   hum=True)
sh(36, "\"No... what kind of thing is this?\" Aslam said to himself. Clenching his teeth, he turned around and tried to run towards the beach.",
   [("breath_heavy", "ދަތްތަކަށް", -20), ("leaves_rustle", "ދުއްވައިގަންނަން", -22)], speaker="aslam")
sh(37, "At that moment the whole area echoed with a powerful growl. It was not the soft voice heard a moment ago.",
   [("low_growl", "ހުނުމެއްގެ", -12)], hum=True)
sh(38, "A dreadful growl, the kind that stops the heart, that shook the whole jungle. At that moment, at the other end of the island, the family had pitched a temporary tent and sat holding their breath.",
   [("low_growl", "ހުނުމެއް", -16)], hum=True)
sh(39, "The winds were so strong it seemed they would blow the pitched tent away. Aadhambe sat reciting verses of the Quran.",
   [("wind_howl", "ވައިރޯޅިތަކުގެ", -18), ("cloth_rustle", "ޓެންޓް", -20)])
sh(40, "What showed on his face was no ordinary worry. \"Zaahid! Where is Aslam?\"",
   speaker="shareefa", hum=True)
sh(41, "\"He still hasn't come back!\" There was a sound close to weeping in Shareefa's voice. Zaahid looked outside.",
   speaker="shareefa", hum=True)
sh(42, "Nothing could be seen but the heavy rain pouring through the pitch-black darkness. \"Asla...m! Asla..........m!\"",
   speaker="zaahid")
sh(43, "Zaahid cupped both hands round his mouth and shouted loudly. But his voice was lost in the roar of the strong wind.",
   [("wind_gust", "ވައިގެ", -16)])
sh(44, "\"Wait, I'll go and find Aslam,\" said Naazim, Zaahid's younger brother and Aslam's uncle. Naazim is a huge, powerfully built man.",
   speaker="naazim")
sh(45, "After switching on the torch he stepped out into the rain. \"Uncle, I'm coming too.\" Eighteen-year-old Raaidhu tried to follow him out.",
   [("flashlight_click", "ދިއްލާލުމަށްފަހު", -16), ("footsteps_sand", "ނިކުތް", -22)], speaker="raaidhu")
sh(46, "\"No! Nobody is to go into the jungle!\" Suddenly grandpa broke off his recitation and said it in a hard voice.",
   speaker="aadhambe", hum=True)
sh(47, "His eyes were wide. \"This is no ordinary storm. Even though this is an island people come to...\"",
   speaker="aadhambe")
sh(48, "\"...I can feel that tonight this island is in a dreadful state.\" Grandpa's face, too, conveyed the terror of this night.",
   speaker="aadhambe", hum=True)
sh(49, "Everyone looked at grandpa in fear. What was grandpa talking about? \"But Bappa, Aslam is out there alone.\"",
   speaker="zaahid")
sh(50, "Zaahid said, worried. Aadhambe stood up, leaning on his long stick. \"Let's go. But all of us together. Nobody splits off.\"",
   [("cloth_rustle", "ތެދުވި", -22)], speaker="aadhambe")
sh(51, "\"Take the torches and come!\" The family's men - Zaahid and Naazim, Aadhambe and Raaidhu - took torches and set off towards the jungle.",
   [("flashlight_click", "ޓޯޗުތައް", -18), ("footsteps_sand", "މިސްރާބު", -22)], speaker="aadhambe")
sh(52, "The women stayed in the tent, trembling with fear, praying. As they entered the jungle and switched on the torches, the light spread among the trees.",
   [("flashlight_click", "ދިއްލައިލުމުން", -18)])
sh(53, "The shadows of the trees seemed to swirl around them like giant ghosts. \"Asla...m! My son!\"",
   hum=True)
sh(54, "Zaahid kept calling. Suddenly a loud noise came from the right side of the jungle - it sounded like a big tree breaking and crashing down.",
   [("creak", "ބިނދިގެން", -16), ("soft_thud", "ވެއްޓުނު", -14)])
sh(55, "As the light of the torch Naazim pointed spread into the dense trees, everyone's breath caught in their throats.",
   [("gasp", "ތާށިވި", -18)], hum=True)
sh(56, "In the light could be seen the great roots of a huge nika tree. But what startled them was something stuck among those roots.",
   [("heartbeat", "ސިއްސުވާލީ", -20)], hum=True)
sh(57, "It was a large seabird that seemed to have died only moments ago. It lay torn open. Drops of its blood were falling to the ground with the pouring rain.",
   hum=True)
sh(58, "Strangest of all, a stench of rotting sea-refuse and of something burnt had suddenly spread through the jungle of that clean uninhabited island.")
sh(59, "\"Bappa... what kind of thing is this?\" Naazim asked in a strained voice.",
   speaker="naazim", crop="medium")
sh(60, "Aadhambe slowly stepped forward. With his long stick he prodded the seabird's body.",
   [("footsteps_sand", "ފިޔަވަޅެއް", -22), ("soft_thud", "ކޮށްޓާލި", -22)])
sh(61, "At that moment tiny black worms began to drop from the bird's body to the ground. Aadhambe's eyes widened, and the colour of fear showed on his face.",
   [("gasp", "ބޮޑުވެ", -20)], hum=True)
sh(62, "\"This is not something done by human beings,\" Aadhambe said in a whisper.",
   speaker="aadhambe", hum=True)
sh(63, "\"Hurry and find Aslam! His life is in danger.\" At that very moment, Aslam, somewhere deep in the jungle, was going through strange things.",
   [("heartbeat", "ނުރައްކާ", -20)], speaker="aadhambe")
sh(64, "Aslam lies lost in the sickness of love. His mind was completely drowned in that beautiful girl's bewitching gaze and the blue light radiating from her body.",
   hum=True)
sh(65, "It seemed to him that the whole world had stopped, and that nothing existed except that girl.",
   hum=True)
sh(66, "Even as the heavy raindrops pelted his body, he felt no cold at all.")
sh(67, "The girl slowly began to walk towards Aslam. As she walked, not a sound came from the leaves on the ground.",
   hum=True)
sh(68, "She seemed to be flying through the air like a light leaf drifting on the wind.",
   [("wind_gust", "ވައިގެ", -24)], hum=True)
SHOTS = S

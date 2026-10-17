"""Beat/shot plan for Handi Kujaa episode 629 (series finale-cliffhanger; used by plan_beats.py)."""

LOC = {
    "banyan_roots": "inside the giant twisting roots of an enormous centuries-old banyan (nika) tree on the shore of a small uninhabited Maldivian island at night: huge dark root walls and hollows big enough to shelter in, a vast black canopy overhead, wet white sand between the roots, an old plain iron kitchen knife standing upright stuck in the sand, glimpses of the beach and the dark lagoon between the roots",
    "banyan_edge": "the wet white sand beach just outside the edge of the giant banyan tree's shade at night, seen from between its huge outer roots: the open storm-lashed beach, smooth unmarked wet sand, the dark sea and breaking surf beyond",
    "memory": "a memory of a hundred years ago: a small, old, empty clearing deep in the island's jungle, huge ancient trees and screw-pines around it, bare ground with fallen leaves",
    "red_shore": "the shore in front of the giant centuries-old banyan tree at night: the sea's waves rolling up the white sand towards the tree's huge twisting outer roots, the dark banyan canopy above",
    "banyan_red": "inside the giant twisting roots of the enormous centuries-old banyan tree on the shore at night: huge dark root walls and hollows, a vast black canopy overhead, wet sand between the roots, the glowing sea visible between the roots",
    "jungle": "the dense pitch-dark jungle in the island's interior at night: screw-pines, thorny magoo shrubs, huge old trees with hanging roots, black mud puddles on the ground, rain falling through the canopy",
    "shrine": "a treeless clearing of old bare ground in the centre of the island at night, ringed by the black jungle: in its middle a small, very old whitewashed coral-stone ziyaarath (shrine building), pale and weathered, with a dark low open doorway, no text, no symbols, no inscriptions",
}
MOOD = {
    "banyan_roots": "storm night: near-black indigo, silver rain slanting between the roots, white lightning flashes, a cold sea-green spectral glow from outside the tree, dread and chaos",
    "banyan_edge": "storm night: near-black indigo, silver rain, white lightning, a cold sea-green spectral glow on the smooth wet sand, eerie and deceptive",
    "memory": "faded desaturated sepia memory haze, soft blurred edges, grainy, pale hazy daylight through the trees, silent and sorrowful",
    "red_shore": "storm night: the sea glowing an eerie wine-red from within, the red light tinting the wet sand and the roots, near-black indigo sky, silver rain, white lightning, dreadful and supernatural (red light only, no blood)",
    "banyan_red": "storm night inside the roots: near-black indigo with an eerie wine-red glow from the sea spilling between the roots, silver rain, white lightning, desperate and urgent",
    "jungle": "pitch-dark jungle at night: near-black indigo, silver rain through the canopy, brief white lightning flashes, a faint sea-green glow from above, panicked flight",
    "shrine": "night: a strange still silence, near-black indigo sky, thin silver rain, a pale cold light on the whitewashed shrine, a faint sea-green mist low on the bare ground, ominous",
}

KIDS = "three small children (little girls in small headscarves) huddled small in the background"
FAKE = ("the impostor in the grandfather's likeness: exactly Aadhambe's look and clothes but rain-soaked, holding the "
        "snapped half of his wooden walking stick, a subtly wrong, sly unnatural smile and eyes with a faint cold glint")
HANDI_HORROR = ("the spirit in her angry form: her face ashen grey and faintly cracked like old porcelain, dark hollow eyes "
                "glowing red, still in her opaque loose long-sleeved white gown and opaque white veil fully covering her "
                "hair and neck, long dark smoky ribbons trailing from under the veil, long dark fingernails")
KNIFE = "an old plain iron kitchen knife"

BEATS = [
    dict(to=3, reason="continuation of 605 (same place, same light): the women shield the children in the banyan roots while crows and the handi's power rage outside", chars=["shareefa", "aisha"], loc="banyan_roots",
         visual=f"inside the huge banyan roots in the storm night: Shareefa and Aisha crouching in a deep root hollow, shielding {KIDS} behind them with their own bodies and outstretched arms, faces tense and frightened, looking up; above them in the rain a swirling black cloud of crows with tiny red eyes whirling through the canopy; in the foreground {KNIFE} standing upright stuck in the sand, glinting in a lightning flash; outside the roots a cold sea-green glow",
         camera="medium-wide, slightly low angle, the women's faces and the swirling crows in the upper two-thirds, the wet sand and the upright knife as the lower third",
         amb="beach_storm_night", sens="violence", safe="the crows never touch or wound anyone: they swirl overhead while the women shield the children; children small in the background"),
    dict(to=5, reason="action change: Aslam suddenly rises from the ground and stands, eyes normal but full of terror, screaming", chars=["aslam"], loc="banyan_roots",
         visual="Aslam standing bolt upright between the giant banyan roots in the rain, his mustard t-shirt and open grey checked shirt soaked but loose and opaque, his eyes normal and wide open, his face full of extreme terror, mouth open in a scream; black crows with red eyes whirling around him in the dark without touching him; white lightning behind",
         camera="medium shot, low angle, Aslam's face and the swirling crows in the upper two-thirds, the dark roots and sand as the lower third",
         amb="beach_storm_night"),
    dict(to=7, reason="turning point: at Aslam's \"Stop!\" every crow falls silent and flies back up to the treetop", chars=["aslam"], loc="banyan_roots",
         visual="Aslam seen from a low angle standing in the roots, one arm flung up towards the canopy, shouting; above him hundreds of black crows streaming back up and settling silently on the highest branches of the vast banyan canopy, their tiny red eyes glowing in the dark like embers; rain falling, a sudden eerie stillness",
         camera="low-angle wide shot looking up, Aslam's face and raised arm in the middle, the crowded canopy of red-eyed crows in the upper half, the dark roots as the lower third",
         amb="beach_storm_night"),
    dict(to=10, reason="emotional turning point / speaker: Shareefa steps forward crying; Aslam turns to her in tears and speaks to his mother and uncle", chars=["aslam", "shareefa", "naazim", "zaahid"], loc="banyan_roots", speaker="aslam",
         visual="Aslam in the roots turned towards the viewer, tears running down his pale frightened face, speaking urgently; in the soft-focus foreground at the side Shareefa in her maroon dress and black hijab fully covering her hair and neck, reaching towards her son and weeping; behind Aslam the big bearded Naazim in his dark-green t-shirt and Zaahid in his sky-blue shirt, both soaked, watching anxiously",
         camera="over-the-shoulder medium shot, Aslam centred and sharp in the upper half, Shareefa soft at the side, the men behind, the wet sand as the lower third",
         amb="beach_storm_night"),
    dict(to=12, reason="action change: Aslam points out towards the shore where the waves break — the secret in the depths of the lagoon", chars=["aslam"], loc="banyan_roots",
         visual="Aslam seen from behind and slightly to the side standing between two huge roots, pointing out towards the storm-lashed shore where white waves are breaking; beyond, the dark lagoon with a faint sea-green glow deep under the water; rain, lightning over the sea",
         camera="over-the-shoulder wide shot, Aslam's profile and the glowing sea in the upper two-thirds, the dark sand between the roots as the lower third",
         amb="beach_storm_night"),
    dict(to=14, reason="flashback (told by Aslam): a hundred years ago, in this jungle — shown only symbolically", loc="memory", transition="dissolve",
         visual="a faded sepia memory: a small, old, empty jungle clearing with huge ancient trees around it; on the bare leaf-covered ground lies a tiny, empty, abandoned woven palm-leaf basket like a small cradle, slightly tipped on its side; a few faint old footprints leading away into the trees; no people, no child, no figures, nothing violent",
         camera="wide shot, eye level, the clearing and the empty basket in the upper two-thirds, the leaf-strewn ground as the lower third",
         amb="jungle_eerie", sens="violence", safe="the killing of the child a century ago is never shown and no child appears: only an empty clearing and an abandoned woven cradle-basket in sepia"),
    dict(to=15, reason="return from the memory to Aslam speaking: she wants the life of the family's youngest male", chars=["aslam", "shareefa", "naazim", "zaahid"], loc="banyan_roots",
         reuse="beat_004", amb="beach_storm_night", visual="(reuse of beat_004)", transition="dissolve"),
    dict(to=17, reason="focus shift to a new character: Aslam names Raaidhu; everyone turns to him; he backs against a root as the handi laughs outside", chars=["raaidhu", "zaahid", "aslam", "shareefa"], loc="banyan_roots",
         visual="Raaidhu, a young man in a rain-darkened red t-shirt and black track trousers, standing with his back against a huge banyan root, startled wide eyes, both palms resting on the bark behind him; in the soft-focus foreground the shoulders of Zaahid, Aslam and Shareefa (black hijab) turned towards him; between the roots behind him a distant cold sea-green glow outside the tree",
         camera="medium shot, eye level, Raaidhu's frightened face centred in the upper half, the family's backs soft at the sides, the sand as the lower third",
         amb="beach_storm_night"),
    dict(to=19, reason="new character in frame: the false grandfather stands outside the banyan's shade and calls Raaidhu with outstretched arms", chars=["aadhambe"], loc="banyan_edge", speaker="aadhambe",
         visual=f"just outside the edge of the banyan's shade on the wet beach in the rain: {FAKE}; he stands with both arms stretched out towards the viewer as if inviting a hug, smiling lovingly; his feet are hidden behind a low twisting outer root in the foreground; behind him the dark stormy sea, a faint sea-green glow, silver rain",
         camera="medium shot from between the roots, the old man's face and open arms centred in the upper two-thirds, the dark outer root as the lower third",
         amb="beach_storm_night", sens="other", safe="the impostor is Aadhambe's own look with a faint wrongness (sly smile, cold glint); his backward feet are hidden by the roots as the narration says"),
    dict(to=21, reason="action/emotion change: Raaidhu hears grandfather's loving voice and is drawn, entranced, forward between the roots", chars=["raaidhu"], loc="banyan_roots",
         visual="Raaidhu, a young man in a red t-shirt, standing between the giant banyan roots with a dreamy, faraway gaze as if hearing a beloved voice in the distance, his face softening, taking one slow step forward towards the viewer, one hand half raised; rain dripping from the roots; behind him the dark hollows of the tree",
         camera="medium close-up, eye level, Raaidhu's entranced face in the upper half, the sand and roots as the lower third",
         amb="beach_storm_night", sens="other", safe="the spell is shown only as a glazed, entranced look"),
    dict(to=23, reason="return to the false grandfather calling with outstretched arms (reverse shot)", chars=["aadhambe"], loc="banyan_edge",
         reuse="beat_009", amb="beach_storm_night", visual="(reuse of beat_009)", transition="cut"),
    dict(to=25, reason="return to Raaidhu stepping forward, his steps no longer his own (shot)", chars=["raaidhu"], loc="banyan_roots",
         reuse="beat_010", amb="beach_storm_night", visual="(reuse of beat_010)", transition="cut"),
    dict(to=27, reason="character enters / action change: Zaahid runs and grips Raaidhu's shoulders; Raaidhu strains to go: \"Bappa, it's grandpa!\"", chars=["raaidhu", "zaahid"], loc="banyan_roots", speaker="raaidhu",
         visual="Zaahid in his soaked sky-blue shirt holding his son Raaidhu firmly by both shoulders from behind, his face desperate; Raaidhu in his red t-shirt facing the viewer, straining forward against his father's hands, eyes glazed and pleading, speaking; the dark roots around them, silver rain, sea-green glow from outside",
         camera="medium shot, eye level, Raaidhu centred and sharp in the upper half with Zaahid just behind his shoulder, the sand as the lower third",
         amb="beach_storm_night"),
    dict(to=28, reason="speaker change: Naazim shouts it is a trick and, hand on the iron knife in the sand, begins to recite", chars=["naazim"], loc="banyan_roots", speaker="naazim",
         visual=f"Naazim, a huge bearded man in a soaked dark-green t-shirt, kneeling on one knee in the sand between the roots, one big hand resting on the handle of {KNIFE} that stands upright stuck in the sand, his eyes raised and lips moving as he shouts and then recites; lightning lighting his face from the side",
         camera="medium close-up, slightly low angle, Naazim's face centred in the upper half, his hand on the upright knife and the sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the iron knife only stands upright in the sand under his hand like a talisman"),
    dict(to=30, reason="new character in frame / action: the handi descends and lays her long nails on the false grandfather's shoulder — his loving face turns ashen with red eyes", chars=["handi", "aadhambe"], loc="banyan_edge",
         visual=f"outside the banyan's shade on the dark wet beach: the spirit floating down out of the rain behind the false grandfather, {HANDI_HORROR}, one hand resting lightly on his shoulder; the impostor in Aadhambe's clothes and white skullcap, holding the snapped stick, his kind look gone — his face turned ashen grey and cracked like dry clay, his eyes glowing red; silver rain, lightning, the stormy sea behind",
         camera="medium shot, eye level, both faces in the upper two-thirds, the smooth wet sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the 'rotting' face is drawn as ashen cracked clay with red eyes; no flesh, no gore; the handi fully veiled"),
    dict(to=31, reason="return to Raaidhu held by his father as the spell breaks and he falls back, awake", chars=["raaidhu", "zaahid"], loc="banyan_roots",
         reuse="beat_013", amb="beach_storm_night", visual="(reuse of beat_013)", transition="cut"),
    dict(to=34, reason="speaker change: the handi's threat — none will survive till sunrise, the sea is coming", chars=["handi"], loc="red_shore", speaker="handi",
         visual=f"the spirit hovering above the shore just beyond the banyan's outer roots, {HANDI_HORROR}; her gown is made of thick, heavy, completely opaque matte white cloth, solid and not see-through, hanging in loose folds; her veil streaming in the wind, speaking towards the viewer with a cold menacing look; behind her the sea has begun to glow an eerie wine-red, tall waves rising; silver rain, white lightning",
         camera="medium shot from the waist up, slightly low angle, the spirit's face centred in the upper half, the red-lit sea and sand as the lower third",
         amb="beach_storm_night", sens="other", safe="horror form = ashen cracked porcelain face with red eyes, fully veiled; the red sea is only red light"),
    dict(to=36, reason="scene/action change: the red waves creep up the shore and blacken the banyan's outer roots", loc="red_shore",
         visual="the waves of the sea glowing an eerie translucent wine-red, rolling up the white sand towards the giant banyan; where the glowing red foam touches the tree's huge outermost roots, the roots turn dark and charred-black; the black canopy above with tiny red-eyed crows restless in the branches; rain, lightning; no people",
         camera="wide low-angle shot from the shoreline, the red waves and the darkening roots in the upper two-thirds, the red-lit wet sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the 'sea of blood' is shown only as an eerie wine-red glowing sea; no blood, no liquid gore"),
    dict(to=38, reason="speaker change: Aslam, breathless, urges Naazim to go to the old ziyaarath in the middle of the island", chars=["aslam", "naazim"], loc="banyan_red", speaker="aslam",
         visual="Aslam close to Naazim in the roots, breathing hard, speaking urgently and pointing back towards the island's dark interior; Naazim's big bearded profile soft in the foreground at the side; a wine-red glow from the sea lighting their wet faces from one side, rain",
         camera="over-the-shoulder medium shot, Aslam centred and sharp in the upper half, Naazim soft at the side, the dark sand as the lower third",
         amb="beach_storm_night"),
    dict(to=39, reason="speaker change: Zaahid warns that entering the jungle is walking into death's mouth", chars=["zaahid"], loc="banyan_red", speaker="zaahid",
         visual="Zaahid in his soaked sky-blue shirt, grey-flecked moustache, gripping a root, his worried face turned towards the viewer, speaking with fear; behind him between the roots the black wall of the jungle; a wine-red glow on one side of his face, rain",
         camera="medium close-up, eye level, Zaahid centred in the upper half, the root and sand as the lower third",
         amb="beach_storm_night"),
    dict(to=40, reason="return to the red waves breaking harder on the roots; the crows shriek again", loc="red_shore",
         reuse="beat_018", amb="beach_storm_night", visual="(reuse of beat_018)"),
    dict(to=41, reason="return to Zaahid as he decides: no other way, Aslam lead us, all into the jungle together", chars=["zaahid"], loc="banyan_red",
         reuse="beat_020", amb="beach_storm_night", visual="(reuse of beat_020)", transition="cut"),
    dict(to=42, reason="action change: Naazim pulls the iron knife from the sand; the eight get ready to leave", chars=["naazim", "shareefa", "aisha", "raaidhu"], loc="banyan_red",
         visual=f"Naazim pulling {KNIFE} up out of the sand and gripping it tight, held upright in front of his chest, his jaw set; behind him Shareefa (black hijab) and Aisha (white hijab, lavender dress) each lifting a small child onto their hips, the third little girl holding Aisha's dress, and Raaidhu in his red t-shirt standing ready; the wine-red glow of the sea between the roots, rain",
         camera="medium-wide, eye level, Naazim and the knife in the upper-middle, the family behind, the sand as the lower third",
         amb="beach_storm_night", sens="other", safe="the knife is held upright as a talisman, pointed at no one"),
    dict(to=45, reason="scene/action change: the family steps out of the shade; with thunder the handi dives down, her smoky ribbons spreading like a net over the jungle", chars=["handi"], loc="red_shore",
         visual=f"wide view: small figures of the family seen from behind running out from under the vast banyan onto the red-lit sand towards the black jungle; above them the spirit diving down out of a sky split by a huge white lightning bolt, {HANDI_HORROR}, her white gown and veil streaming and her long dark smoky ribbons spreading out wide like an enormous net over the treetops; red glowing sea at the side, silver rain",
         camera="wide low-angle shot, the diving spirit and lightning in the upper half, the small running figures in the middle, the red-lit sand as the lower third",
         amb="beach_storm_night", sens="other", safe="her 'long black hair' is drawn as dark smoky ribbons from under her opaque veil; the family small and seen from behind"),
    dict(to=47, reason="action change: Naazim holds the iron knife up high; the handi recoils shrieking into the treetops", chars=["naazim", "handi"], loc="jungle",
         visual=f"Naazim at the edge of the jungle holding {KNIFE} up high above his head, the blade glinting white in a lightning flash, shouting; above him in the branches the spirit recoiling backwards and upwards into the treetops, {HANDI_HORROR}, her gown streaming; a clear distance between them",
         camera="low-angle medium-wide shot, Naazim's face and the raised knife in the middle, the recoiling spirit in the upper part, the dark muddy ground as the lower third",
         amb="jungle_storm_night", sens="violence", safe="the knife is only held up high like a talisman, never pointed at or touching her; she recoils at a distance"),
    dict(to=49, reason="scene change: Aslam leads the family through the black jungle; mud puddles and sharp thorns", chars=["aslam", "zaahid", "raaidhu"], loc="jungle",
         visual="Aslam pushing through the pitch-dark jungle towards the viewer, leading the way, his face lit by a lightning flash, brushing aside thorny branches; behind him Zaahid and Raaidhu following closely, soaked; black mud puddles reflecting the lightning, thorny shrubs, rain through the canopy",
         camera="medium-wide, eye level, Aslam's face in the upper half, the others behind, the black puddles as the lower third",
         amb="jungle_storm_night"),
    dict(to=51, reason="focus change / speaker: the women carry the children; Zaahid, holding Raaidhu's hand, gasps \"Is it far?\"", chars=["zaahid", "raaidhu", "shareefa", "aisha"], loc="jungle", speaker="zaahid",
         visual="in the dark jungle: Zaahid, breathless, calling out ahead towards the viewer, holding Raaidhu by the hand beside him as they hurry along a narrow path; just behind them Shareefa (maroon dress, black hijab) and Aisha (lavender dress, white hijab), both hijabs fully covering hair and neck, hurrying close behind; rain, screw-pine leaves, lightning",
         camera="medium shot, eye level, Zaahid centred and sharp in the upper half, the others behind, the muddy ground as the lower third",
         amb="jungle_storm_night"),
    dict(to=52, reason="return to Aslam leading as he answers — cut off by a crash on the right", chars=["aslam", "zaahid", "raaidhu"], loc="jungle",
         reuse="beat_026", amb="jungle_storm_night", visual="(reuse of beat_026)", transition="cut"),
    dict(to=54, reason="new character bursts in: the false grandfather runs out of the trees on backward-turned feet towards Naazim at the back", chars=["aadhambe", "naazim"], loc="jungle",
         visual=f"in the black jungle: the false grandfather bursting out of the thorny bushes on the right, lunging forward with an unnatural crooked stride, his feet hidden in the low ferns and black mud, ashen grey cracked face, eyes glowing red, one hand with long dark nails reaching out; Naazim at the back of the group a little distance away turning with a start, holding {KNIFE} low at his side; rain, lightning",
         camera="medium-wide, eye level, the lunging figure and Naazim's startled face in the upper two-thirds with a clear gap between them, the mud as the lower third",
         amb="jungle_storm_night", sens="violence", safe="the attack is not shown as contact: the figure reaches out across a gap; no wound"),
    dict(to=55, reason="action change: Naazim has fallen, clutching his shoulder; Zaahid turns back shouting his name", chars=["naazim", "zaahid"], loc="jungle", speaker="zaahid",
         visual="Naazim fallen on the muddy jungle ground, propped on one elbow, clutching his left shoulder with his other hand, grimacing in pain, his dark-green t-shirt intact; Zaahid in the background turning back with his arm out, shouting; rain, a lightning flash, black trees",
         camera="medium shot, slightly high angle, Naazim's pained face in the upper-middle, Zaahid behind, the muddy ground as the lower third",
         amb="jungle_storm_night", sens="violence", safe="the shoulder wound and the 'fresh blood' are never shown: only Naazim on the ground clutching his shoulder, no blood"),
    dict(to=57, reason="action change: the figure looms to drag him off; Naazim raises the iron knife and it recoils with an inhuman roar", chars=["naazim", "aadhambe"], loc="jungle",
         visual=f"Naazim kneeling on the ground holding {KNIFE} upright at arm's length in front of his chest like a protective talisman, blade pointing straight up at the sky (not raised to strike), a faint sea-green shimmer around the iron; the looming false grandfather several steps away; the figure, ashen grey cracked face and red glowing eyes, mouth open in a roar, recoiling backwards away from the raised iron with its arms thrown up; a clear distance between them; the deep darkness of the jungle behind",
         camera="low-angle medium shot, the raised knife and the recoiling figure in the upper two-thirds, Naazim's shoulders and the mud as the lower third",
         amb="jungle_storm_night", sens="violence", safe="no strike is shown: the iron is raised between them like a talisman and the figure recoils; no contact, no blood"),
    dict(to=58, reason="action change: Zaahid and Aslam lift Naazim, his arm over their shoulders — \"Hurry!\"", chars=["naazim", "zaahid", "aslam"], loc="jungle",
         visual=f"Zaahid and Aslam hauling the big Naazim up from the muddy ground, his arms over their shoulders, Naazim still gripping {KNIFE} pointed down, his face strained; all three soaked, hurrying forward towards the viewer; rain, lightning, black trees",
         camera="medium shot, eye level, the three faces in the upper half, the mud and puddles as the lower third",
         amb="jungle_storm_night"),
    dict(to=60, reason="action change: the handi descends again through the breaking branches, her red eyes fixed on Raaidhu, as the family flees", chars=["handi", "raaidhu"], loc="jungle",
         visual=f"looking up through the jungle canopy: the spirit descending through snapping branches above, {HANDI_HORROR}, her red eyes fixed hungrily downwards; below her, small in the lower middle, Raaidhu in his red t-shirt running and glancing back up in terror; flying leaves, rain, lightning",
         camera="low-angle vertical shot, the descending spirit in the upper half, Raaidhu in the middle, dark foliage as the lower third",
         amb="jungle_storm_night"),
    dict(to=61, reason="scene change: a treeless clearing with the small ancient whitewashed ziyaarath in strange silence", loc="shrine",
         visual="establishing shot: the small, very old whitewashed coral-stone ziyaarath standing alone in the middle of a treeless clearing of old bare ground, pale and weathered, its low doorway a dark rectangle; the black jungle all around, faint mist on the ground, thin rain, an eerie stillness; no people",
         camera="wide shot, eye level, the shrine in the upper-middle, the bare misty ground as the lower third",
         amb="jungle_eerie"),
    dict(to=63, reason="speaker / emotional change: at the clearing's edge Raaidhu prays and the family feels a flicker of hope", chars=["raaidhu", "zaahid", "aslam", "naazim"], loc="shrine", speaker="raaidhu",
         visual="at the edge of the clearing Raaidhu standing with raised cupped hands, eyes lifted, praying with desperate hope; around him Zaahid, Aslam and the big Naazim (holding his shoulder) catching their breath, gazing ahead; Shareefa and Aisha in hijab with the small children behind them; the pale shrine glimmering soft in the distance behind",
         camera="medium shot, eye level, Raaidhu centred and sharp in the upper half, the others around him, the bare ground as the lower third",
         amb="jungle_eerie"),
    dict(to=66, reason="cliffhanger reveal: in the shrine doorway stands skipper Sameer, whom they saw dead on the dhoni — death-white face, black eyes, arm outstretched", chars=["sameer"], loc="shrine",
         visual="in the dark low doorway of the pale whitewashed shrine stands Sameer, upright and utterly still, in his faded navy work shirt and checked sarong, soaked; his face drained to a ghostly chalk-white pallor, like pale ash, clearly unnatural, his eyes entirely black like polished black glass with no whites, a blank stare; one arm stretched straight out towards the viewer; his collar and neck lost in deep shadow; at the bottom edge the dark silhouettes of the family's heads seen from behind; faint sea-green mist, thin rain",
         camera="medium shot, eye level, Sameer large and centred in the doorway, his chalk-white face clearly visible in the upper third, the family's silhouettes and the bare ground as the lower third",
         amb="jungle_eerie", sens="violence", safe="Sameer's revenant: ashen-white face and black eyes only; the 'deep wounds on his neck' and 'black blood' are never shown — collar and neck in deep shadow"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Shareefa and Aisha pushed the small children in between the big roots of the tree and shielded them with their own bodies.")
sh(2, "In the pouring heavy rain, the terrifying cries of the crows and the family's anguished screams blended together.",
   [("wings_flap", "ކާޅުތަކުގެ", -18)], hum=True)
sh(3, "Because of the iron knife driven into the ground the handi could not get inside the banyan tree, but using her evil power she has turned all the birds of the island against the family.")
sh(4, "In the middle of that chaos, Aslam, who was lying on the ground, suddenly rose and stood upright. This time his eyes were open in the normal way.",
   [("cloth_rustle", "ތެދުވެ", -22)])
sh(5, "But his face showed terror of the utmost degree. Paying no heed to the crows flying around him, he screamed out loud.",
   [("wings_flap", "އުދުހެމުންދިޔަ", -18)], hum=True)
sh(6, "\"Stop!\" The whole jungle echoed with Aslam's own voice. Strangely, the moment he said it, all the crows flying around fell suddenly silent, turned back and settled at the very top of the tree.",
   [("wings_flap", "ކާޅުތަކެއް", -16)], speaker="aslam", hum=True)
sh(7, "It seemed as though there was a secret in Aslam's body that those things obeyed. \"Aslam! My child, are you awake?\"")
sh(8, "Shareefa stepped forward, weeping. Aslam turned round and looked towards his mother. Tears were falling from his eyes. \"Mamma...\"",
   speaker="aslam", hum=True)
sh(9, "\"Uncle... we can't stay safe here. She has loosened my tongue.\"", speaker="aslam")
sh(10, "\"She wants to make me tell this story.\" \"What story?\" Zaahid asked anxiously.", speaker="aslam")
sh(11, "Aslam pointed towards the shore where the waves were breaking. \"This island is an island people are always coming to.\"",
   [("wave_crash", "ރާޅުތައް", -18)], speaker="aslam")
sh(12, "\"But no one knows the secret lying at the bottom of this island, in the depths of this lagoon.\"",
   speaker="aslam", hum=True)
sh(13, "\"A hundred years ago, people who travelled to this island killed her child here in this island's jungle.\"",
   hum=True)
sh(14, "\"Her spirit of revenge comes back to life once every hundred years. Tonight is the night those hundred years are complete!\"",
   hum=True)
sh(15, "A new wave of fear broke over everyone's hearts. \"What she wants is the life of this family's youngest male.\"",
   [("heartbeat", "ފުރާނަ", -20)], speaker="aslam", hum=True)
sh(16, "Aslam said in a trembling voice: \"That is... Raaidhu!\" Everyone started and looked towards eighteen-year-old Raaidhu.",
   [("gasp", "ސިހިފައި", -18)], hum=True)
sh(17, "Raaidhu shrank back in fear and pressed against a tree root. At that moment, from outside the banyan, came the sound of that evil handi laughing loudly.",
   [("soft_thud", "ލެނގިލި", -22)], hum=True)
sh(18, "And the figure in the grandfather's likeness, standing outside the tree, stretched out a hand towards Raaidhu and said: \"Raaidhoo...\"",
   speaker="aadhambe")
sh(19, "\"Come to me...\" As that evil figure in the grandfather's likeness, standing outside the banyan's shade, began calling Raaidhu, an evil silence fell over the whole surroundings.",
   speaker="aadhambe", hum=True)
sh(20, "In the pouring rain, that figure's voice was not heard by the ears alone. It was the grandfather's own loving voice, reaching the very depths of the heart.")
sh(21, "Instead of fear, that voice carried the colour of protection and tenderness. \"Raaidhu... my child,\"")
sh(22, "\"come to grandpa. I've come out here looking for you, my child. Grandpa is safe.\"", speaker="aadhambe")
sh(23, "The figure said this, stretching out both arms. His feet, turned backwards, were now hidden behind the roots of the tree.",
   hum=True)
sh(24, "Raaidhu's eyes widened and his body slowly began to move forward. His mind was telling him that this was not his grandfather.",
   [("footsteps_sand", "ކުރިއަށް", -22)])
sh(25, "But it was as if he had no control over his own steps. The effect of the sorcery had begun to reach Raaidhu's young body. \"Raaidhu!\"",
   [("heartbeat", "ސިހުރުގެ", -20)], hum=True)
sh(26, "\"Wait!\" Zaahid ran and gripped Raaidhu's shoulders hard. But at that moment Raaidhu tried to shake off Zaahid's hands.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(27, "\"Bappa, it's grandpa! Grandpa is calling!\" There was no ordinary awareness in Raaidhu's voice.", speaker="raaidhu")
sh(28, "\"No, little one! That's not grandpa! It's a great trick!\" Naazim shouted, and with his hand on the iron knife driven into the ground, he began to recite Aayathul Kursi.",
   speaker="naazim", hum=True)
sh(29, "At that moment the female handi outside the tree was heard laughing loudly. She came down through the air and laid her long black fingernails on the shoulder of the figure in the grandfather's likeness.",
   [("wind_gust", "ތިރިވެ", -18)], hum=True)
sh(30, "With that, the loving look vanished from the face of the figure in the grandfather's likeness; its skin decayed and its eyes turned red.",
   [("low_growl", "ބަދަލުވެގެންދިޔަ", -18)], hum=True)
sh(31, "As the veil of deceit was torn away, Raaidhu suddenly started and fell backwards. His awareness had come back.",
   [("soft_thud", "ވެއްޓުނު", -18)])
sh(32, "\"You won't stay safe in there until sunrise.\"", speaker="handi", hum=True)
sh(33, "The handi's heavy voice echoed over the whole shore. \"The sea's wave is coming up.\"",
   [("wave_crash", "ލޮނގަނޑު", -16)], speaker="handi")
sh(34, "\"Even that tree will go to the bottom of this sea of blood tonight!\" Everyone started and looked down.",
   [("gasp", "ސިހިފައި", -20)], speaker="handi", hum=True)
sh(35, "The handi was telling the truth. The red waves of blood breaking on the shore were slowly advancing towards the banyan tree.",
   [("wave_crash", "ރާޅުތައް", -18)], hum=True)
sh(36, "As the wave came and began to strike the tree's outermost roots, those roots began to turn black. The power of that wave is destroying the tree's protection.",
   [("wave_crash", "ބީހެން", -20)])
sh(37, "Aslam, panting, moved close to Naazim. \"Uncle... we have to go to the other end of this island. In the middle of the island there is an old ziyaarath.\"",
   [("breath_heavy", "މާނޭވާލަމުން", -20)], speaker="aslam")
sh(38, "\"Grandpa said that place is the oldest and safest building on this island. That wave of blood can't reach that place.\"",
   speaker="aslam")
sh(39, "\"But going into the jungle is like walking by ourselves into the lips of death!\" Zaahid said anxiously. \"In the jungle those things' power will be much stronger.\"",
   speaker="zaahid")
sh(40, "The waves of blood began to break on the tree's roots harder than before. The crows at the top of the tree became agitated once again and began to shriek.",
   [("wave_crash", "ބިންދަން", -16), ("wings_flap", "ކަނޑުކާޅުތައް", -16)], hum=True)
sh(41, "Everyone understood that the tree's shelter was disappearing. \"There's no other way! Aslam, lead the way! We all go into the jungle together!\"",
   speaker="zaahid")
sh(42, "Naazim pulled the iron knife out of the ground and gripped it tight. Of the family's ten, the eight who were left got ready to go into the jungle once more.",
   [("cloth_rustle", "ތައްޔާރުވި", -22)])
sh(43, "The moment they left the tree's shade, with a strong gust of wind from overhead, that evil handi began to come down.",
   [("wind_gust", "ވައިރޯޅިއަކާއެކު", -14)], hum=True)
sh(44, "The moment the family's eight stepped out of the banyan's protective shade was a moment when, with a mighty thunderclap from the sky, every colour changed completely.",
   [("thunder", "ގުގުރިއަކާއެކު", -12)], hum=True)
sh(45, "With a strong gust that evil handi plunged down through the air. Her long black hair seemed like a huge net spreading among the trees of the jungle.",
   [("wind_howl", "ވައިރޯޅިއާއެކު", -16)], hum=True)
sh(46, "\"Go! Get into the jungle!\" Naazim shouted, swinging the iron knife in his hand through the air.",
   [("wind_gust", "ހޫރައިލި", -18)], speaker="naazim")
sh(47, "Seeing the power of the iron, the handi drew back a little and, with a cry of pain, flew up into the branches at the tops of the trees.",
   [("leaves_rustle", "ކުރެދިތަކުގެ", -18)])
sh(48, "Aslam, out in front, forced a path into the pitch darkness of the jungle. Because of the heavy rain, black puddles of mud had formed on the jungle floor.",
   [("footsteps_sand", "މަގުކޮށަމުންދިޔަ", -20)])
sh(49, "And strange thorns, sharp thorns that felt as if they cut the feet with every step, kept scraping against their bodies.",
   [("leaves_rustle", "ހެރެމުންދިޔަ", -20)])
sh(50, "Shareefa and Aisha ran with the small children held close, urging them on. \"Aslam! Is it still far?\"",
   [("footsteps_sand", "ދުވަމުންދިޔަ", -20)], speaker="zaahid")
sh(51, "Zaahid asked, panting. He was holding Raaidhu by the hand. Since Raaidhu was those things' main target, he could not be left alone.",
   [("breath_heavy", "މާނޭވާލަމުން", -20)], speaker="zaahid")
sh(52, "\"No, Bappa! It's near the middle of the island! If we go up from here there'll be...\" Aslam's words were cut short by the sound of a violent crash from the right side of the jungle.",
   [("leaves_rustle", "ހޫރުމެއްގެ", -14)], speaker="aslam", hum=True)
sh(53, "Out of the trees, suddenly, burst that evil figure in the grandfather's likeness.",
   [("leaves_rustle", "ނުކުތީ", -16)], hum=True)
sh(54, "Running fast on its backward-turned feet, it came and raked with its long fingernails at the shoulder of Naazim, who was running at the very back of the family.",
   [("footsteps_sand", "ދުވަމުން", -18)], hum=True)
sh(55, "\"Naazim!\" Zaahid turned and looked back. Fresh blood showed on Naazim's shoulder. With a cry of pain he fell to the ground.",
   [("soft_thud", "ވެއްޓުނު", -16)], speaker="zaahid", hum=True)
sh(56, "The figure in the grandfather's likeness tried to drag Naazim's body away into the deep darkness of the jungle.",
   [("cloth_rustle", "ދަމާފަ", -18)], hum=True)
sh(57, "Naazim struck hard at the figure's arm with the iron knife in his hand. At that, a heavy, evil sound no human could make came out of the figure's mouth.",
   [("low_growl", "ނާމާން", -14)], hum=True)
sh(58, "It let go of Naazim and fell back. Zaahid and Aslam ran, lifted Naazim from the ground and put his arms over their shoulders. \"Hurry!\"",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(59, "\"It's coming again!\" Naazim said in a trembling voice. Snapping the branches of the trees above the jungle, the female handi too was coming down on them from above.",
   [("leaves_rustle", "ބިނދެމުން", -16)], hum=True)
sh(60, "This time her eyes showed an evil determination to take Raaidhu no matter what. Panting, running through the jungle, the whole family suddenly came out onto an open ground with few trees.",
   [("breath_heavy", "މާނޭވާލަމުން", -20)], hum=True)
sh(61, "In the middle of that ground stood a small, pale white ziyaarath built of ancient stones. That ground was a place over which a strange silence had fallen.")
sh(62, "But standing in the doorway of that ziyaarath, blocking their way, was... \"O Holy Lord! Lord who created and raised us!\"",
   speaker="raaidhu", hum=True)
sh(63, "\"Save us all!\" Raaidhu began to pray. Seeing the ancient ziyaarath standing in the middle of that old treeless ground, the family's hearts felt a little hope.",
   speaker="raaidhu")
sh(64, "But that small flame of hope suddenly went out at the sight of the figure standing upright in the ziyaarath's doorway. It was skipper Sameer, whom they had seen lying dead inside the dhoni!",
   [("heartbeat", "ސަމީރު", -16)], hum=True)
sh(65, "His body stood upright. The skin of his face had turned the white of death and his eyes had gone completely black.",
   hum=True)
sh(66, "From the deep wounds on his neck, black blood was still flowing. He stood staring towards them with his arm stretched out.",
   hum=True)
SHOTS = S

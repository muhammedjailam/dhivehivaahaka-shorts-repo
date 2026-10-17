"""Beat/shot plan for Handi Kujaa episode 594 (third of five; continues 583's last lines; used by plan_beats.py)."""

LOC = {
    "shore_waves": "the beach of the small uninhabited island Beenaafushi on a storm night, seen from the camping tent: powder-white sand turned grey in the dark, black breaking surf with foam, dark coral rocks, thrashing coconut palms at the edge",
    "tent_flap": "the entrance of the large canvas family camping tent on the beach at night: the canvas door flap held open, the rain-lashed dark beach and surf outside, the warm lantern-lit interior behind",
    "lagoon_dhoni": "the dark lagoon of the island on a storm night: the family's wooden Maldivian dhoni with a small cabin on deck anchored a short way off the beach, rocking on black choppy water, rain sweeping across",
    "tent_lantern": "inside the large canvas family camping tent on the beach at night: canvas walls and a sloping canvas roof held up by wooden poles, woven mats on the sand floor, bags against the walls, a single oil lantern hanging from the centre pole",
    "surf_run": "the dark beach and the shallow surf of the lagoon on a storm night: knee-deep foaming water, pouring rain, the anchored wooden dhoni ahead with lantern light swinging in its little cabin",
    "dhoni_cabin": "inside the small wooden cabin of a Maldivian dhoni at night: old tarred wooden planks and beams, an open square engine-room hatch in the deck floor, a swinging oil lantern on a hook, rain hammering the roof",
    "dhoni_stern": "the open wooden stern deck of the Maldivian dhoni at night in the storm: the long wooden tiller, wet planks, the cabin behind, black waves rising beyond the gunwale",
    "dhoni_deck": "the wet wooden deck of the Maldivian dhoni on a storm night, between the cabin and the stern, black sea and huge waves around",
    "sea_night": "the black lagoon water beside the dhoni on a storm night, rain hammering the surface, huge dark waves",
    "shore_night": "the water's edge of the island beach on a storm night: wet powder-white sand gone grey, foaming surf, the dhoni a dark shape out in the lagoon",
    "tent_dark": "inside the large canvas family camping tent on the beach at night after the lantern has died: canvas walls and wooden poles almost invisible in the dark, woven mats on the sand floor, a small clay pot with glowing embers on the floor",
    "tent_outside": "the large canvas family camping tent standing alone on the dark storm-lashed beach at night, the jungle black behind it, the surf in front",
}
MOOD = {
    "shore_waves": "storm night: near-black indigo, silver rain, a white flash of lightning, an eerie sea-green spectral glow around the spirit, two red glowing eyes; dread",
    "tent_flap": "storm night: warm amber oil-lantern light from inside the tent on the faces against the near-black indigo rain outside, silver rain streaks; horror and disbelief",
    "lagoon_dhoni": "storm night: near-black indigo, silver rain, a single warm amber lantern glow inside the dhoni's cabin, a distant flicker of lightning; ominous",
    "tent_lantern": "tent at night: a single warm oil-lantern light, deep shadows in the corners of the canvas, rain beating on the canvas; claustrophobic fear",
    "surf_run": "storm night: near-black indigo, slanting silver rain, white foam, the small warm lantern glow of the dhoni ahead; desperate urgency",
    "dhoni_cabin": "night inside the cabin: harsh swinging amber light of a single oil lantern throwing moving shadows, everything else black; shock and horror",
    "dhoni_stern": "storm night on the dhoni: near-black indigo, silver rain, an eerie sea-green spectral glow around the spirit, faint amber lantern spill from the cabin; terror",
    "dhoni_deck": "storm night on the dhoni: near-black indigo, white lightning, silver rain and white spray, violent motion; panic",
    "sea_night": "storm night: near-black indigo water, silver rain, white spray, a white lightning flash; desperate",
    "shore_night": "storm night: near-black indigo, silver rain, white foam, a faint sea-green glow far out on the lagoon; exhausted dread",
    "tent_dark": "tent in darkness: near-black, only a faint warm ember-orange glow from the clay pot lighting faces from below, deep shadows; terror",
    "tent_outside": "storm night: near-black indigo, silver rain, white lightning, a faint warm ember glow through the canvas, a swirling sea-green spectral mist around the tent; overwhelming dread",
}

SH_HIJ = "her black hijab fully covering her hair and neck"
AI_HIJ = "her white hijab fully covering her hair and neck"
KIDS = "three small children (little girls in small headscarves) small and huddled in the background behind the women"
WETBROS = "both men drenched by rain and sea, their shirts dark with water but loose and opaque, hair plastered to their foreheads"
HANDI = "the spirit in her opaque loose long-sleeved ankle-length white gown and opaque white veil fully covering her hair and neck, long veil ends and dark smoky ribbons streaming on the wind"
POSS = "Aslam possessed: ashen pale skin, eyes glowing a pale milky white, a rigid unnatural stillness"

BEATS = [
    dict(to=1, reason="continuation of 583's last image: the spirit standing by the waves facing the tent, her dark ribbons spread over the surf, red eyes glowing", chars=["handi"], loc="shore_waves",
         visual=f"seen from the tent across the dark beach: {HANDI}, standing barefoot at the edge of the black breaking surf, facing the viewer; the long dark smoky ribbons from under her veil spread out over the white foam like a net; her two eyes glowing deep red like lamps in the dark; a faint sea-green glow around her, silver rain, a white flash of lightning on the clouds; no other figures",
         camera="wide shot from the tent's height, the spirit and her glowing eyes in the upper-middle third, the dark wet sand and foam as the lower third",
         amb="beach_storm_night", sens="other", safe="her famous 'long hair spread over the surf' is drawn as dark smoky ribbons from under her opaque veil"),
    dict(to=3, reason="characters/action: Naazim frozen at the tent flap pointing out with a trembling hand; Zaahid comes up behind him and sees her — \"Ya Allah!\"", chars=["zaahid", "naazim"], loc="tent_flap", speaker="zaahid",
         visual="inside the tent at the open canvas door flap: Naazim, huge and bearded, holding the flap aside with one hand and pointing out into the rain with the other, trembling, his face frozen in fear; Zaahid just behind him looking out over his shoulder, eyes wide, mouth open in horror, gasping 'Ya Allah'; warm lantern light on their faces, the black rain-lashed beach outside",
         camera="medium two-shot from inside the tent, three-quarter view, Zaahid's horrified face centred in the upper half, Naazim at the side, the mat and sand floor as the lower third",
         amb="tent_storm"),
    dict(to=5, reason="scene change: a loud scream from the dhoni anchored in the lagoon — skipper Sameer, who stayed aboard to fix the engine", loc="lagoon_dhoni",
         visual="the family's wooden Maldivian dhoni anchored in the black lagoon, rocking on choppy water in the pouring rain, a small warm lantern glow swinging inside its little cabin, nobody visible; a distant flicker of lightning, the dark line of the beach in the foreground",
         camera="wide shot from the beach, the dhoni and its glowing cabin in the upper-middle third, the dark water and foam as the lower third",
         amb="beach_storm_night", sens="other", safe="Sameer's scream is heard only; the dhoni is shown from afar with nobody visible"),
    dict(to=7, reason="speaker change: Aadhambe calls loudly 'Wait! Don't go outside!' as the brothers ready to go", chars=["aadhambe", "zaahid", "naazim"], loc="tent_lantern", speaker="aadhambe",
         visual="inside the lantern-lit tent: Aadhambe on his knees on the mat, one hand raised firmly, calling out loudly with a stern, urgent face, his long wooden walking stick beside him; in the soft-focus foreground at the side, Zaahid and Naazim half turned toward the open door flap, seen from behind and in profile, about to rush out",
         camera="over-the-shoulder medium shot, Aadhambe centred and sharp in the upper half, the brothers soft at the side, the mat floor as the lower third",
         amb="tent_storm"),
    dict(to=9, reason="scene change: the two brothers run out through the pouring rain and the surf to the dhoni and climb aboard", chars=["zaahid", "naazim"], loc="surf_run",
         visual=f"Zaahid and Naazim seen from behind, wading and running through knee-deep foaming surf in the pouring rain toward the anchored dhoni, {WETBROS}; ahead the dhoni's little cabin glows with a swinging lantern light; slanting silver rain, waves breaking around them",
         camera="wide shot from behind at water level, the two men and the glowing dhoni in the upper two-thirds, the foaming water as the lower third",
         amb="beach_storm_night"),
    dict(to=13, reason="scene change: inside the dhoni's cabin, a heart-stopping sight at the open engine-room hatch; Naazim cries Sameer's name; a soft laugh from the stern", chars=["zaahid", "naazim"], loc="dhoni_cabin",
         sens="violence", safe="Sameer's death, wounds and blood are never shown: only the brothers' horrified faces in the swinging lantern light, the open hatch, a fallen spanner and one rubber sandal",
         visual=f"inside the small wooden dhoni cabin: Zaahid and Naazim standing frozen at the edge of an open square engine-room hatch, staring down past the bottom edge of the frame with faces of pure horror, Naazim's hand reaching out, Zaahid's hand over his mouth, {WETBROS}; a swinging oil lantern above throws moving amber light; on the clean rain-wet planks in front of the hatch lie only a fallen metal spanner and a single rubber sandal; nobody else in the cabin",
         camera="medium shot from inside the cabin looking up at the men, their faces and the lantern in the upper half, the planks with the spanner and the sandal as the lower third",
         amb="sea_rough"),
    dict(to=16, reason="reveal/character change: by the tiller at the stern sits the spirit, soaked with sea water, laughing — 'Now it is your turn, you two...'", chars=["handi"], loc="dhoni_stern", speaker="handi",
         visual=f"{HANDI}, sitting by the long wooden tiller at the dhoni's stern, her white gown and veil soaked with sea water yet still opaque and loose, sea droplets running down her pale face; she looks straight at the viewer with a cold, cruel laughing smile, her eyes glowing red; a sea-green spectral glow around her, rain and black waves behind",
         camera="medium shot, eye level, her face centred in the upper half, the wet stern planks as the lower third",
         amb="sea_rough", sens="other", safe="the 'blood on her face' is replaced by sea-water droplets; her guilt is carried by her cruel smile and red eyes"),
    dict(to=18, reason="action change: she rises and steps toward the brothers, the planks creaking; they realise they must jump", chars=["handi", "zaahid", "naazim"], loc="dhoni_deck",
         visual=f"on the dhoni's wet deck: {HANDI}, risen to her full tall height and gliding slowly toward the viewer, her long pale hands with dark fingernails at her sides, red eyes glowing; in the foreground at the side, Zaahid and Naazim backing away toward the gunwale, faces turned toward her in terror; behind them a huge black wave rising",
         camera="medium-wide shot over the brothers' shoulders, the advancing spirit in the upper-middle, the wet planks as the lower third",
         amb="sea_rough"),
    dict(to=19, reason="action change: a huge wave strikes the side; the whole dhoni tilts and the brothers fall onto the deck", chars=["zaahid", "naazim"], loc="dhoni_deck",
         visual=f"the dhoni heeling steeply to one side as a huge white-crested wave breaks over its side; Zaahid and Naazim thrown off balance, falling onto the tilted wet deck, clutching at a rope and the gunwale, {WETBROS}; white spray in the air, lightning flash",
         camera="dutch-angle medium-wide shot, the men and the breaking wave in the upper two-thirds, the tilted wet planks as the lower third",
         amb="sea_rough"),
    dict(to=21, reason="action change: with the lurch the spirit flies up onto the cabin roof, red eyes blazing in the pitch dark", chars=["handi"], loc="dhoni_deck",
         visual=f"low angle up at the dhoni's small cabin roof: {HANDI}, standing on the cabin roof after flying up onto it, her gown and veil streaming upward in the wind, her two red eyes blazing like lamps in the pitch dark; rain, lightning behind her, a sea-green spectral glow",
         camera="low-angle shot, the spirit and her glowing eyes in the upper half, the dark cabin wall and wet deck as the lower third",
         amb="sea_rough"),
    dict(to=22, reason="action change: 'Jump!' — Zaahid dives into the waves, Naazim right after him", chars=["zaahid", "naazim"], loc="sea_night",
         visual="Zaahid diving off the side of the dark dhoni into the black heaving sea, Naazim right behind him at the gunwale about to leap; both seen from the side in a white flash of lightning, white spray bursting up, rain streaks; the men fully clothed",
         camera="wide side shot, the diving men and the dhoni's side in the upper two-thirds, the black water and spray as the lower third",
         amb="sea_rough"),
    dict(to=24, reason="scene change: through cold, oily, foul water they swim and drag themselves onto the island's white sand", chars=["zaahid", "naazim"], loc="shore_night",
         visual=f"Zaahid and Naazim crawling out of the foaming surf onto the wet grey sand on hands and knees, gasping, {WETBROS}, a dull oily sheen on the dark water around them, their faces twisted in disgust at a foul smell; rain, the dark dhoni far out in the lagoon behind them",
         camera="medium-wide shot at sand level, the men's faces in the upper half, the wet sand and foam as the lower third",
         amb="beach_storm_night"),
    dict(to=26, reason="action change: looking back, they see the spirit on the dhoni's cabin roof stretching her arm toward the jungle, as if signalling", chars=["handi"], loc="shore_night",
         visual=f"seen from the beach across the dark lagoon: the dhoni rocking at anchor and, standing on its small cabin roof, {HANDI}, a small glowing pale figure, slowly stretching one long arm out toward the island's dark jungle as if signalling; a sea-green glow around her reflecting on the waves, rain, lightning",
         camera="wide shot from the shore, the dhoni and the pointing spirit in the upper-middle third, the wet sand and foam as the lower third",
         amb="beach_storm_night"),
    dict(to=27, reason="return to the brothers on the sand: Naazim, panting, urges Zaahid back to the tent (reverse shot)", chars=["naazim", "zaahid"], loc="shore_night",
         reuse="beat_012", visual="(reuse of beat_012)", amb="beach_storm_night", transition="cut"),
    dict(to=29, reason="scene change: in the tent the women and children are terrified; Aslam lies in the middle, twitching", chars=["shareefa", "aisha", "aslam"], loc="tent_lantern",
         visual=f"inside the lantern-lit tent: Aslam lying unconscious on his back on a woven mat in the middle, pale and still, one hand twitching; Shareefa in her maroon dress with {SH_HIJ} and Aisha in her lavender dress with {AI_HIJ} kneeling close together nearby, holding each other, faces stricken with fear, staring at the canvas walls; {KIDS}; the single lantern swaying on the pole",
         camera="medium-wide shot, slightly high angle, the women's frightened faces in the upper half, Aslam on the mat across the middle, the mat floor as the lower third",
         amb="tent_storm", sens="other", safe="the small children stay small in the background"),
    dict(to=31, reason="character focus: grandfather burns leaves in a small clay pot for smoke and calmly tells the women to bring the children to the middle", chars=["aadhambe"], loc="tent_lantern", speaker="aadhambe",
         visual="Aadhambe sitting cross-legged beside a small clay pot on the tent floor, dropping dried leaves onto glowing embers, a thin grey curl of smoke rising across his face; he looks up and speaks calmly and firmly, his walking stick across his knees; warm lantern light, the canvas wall behind",
         camera="medium close-up, eye level, Aadhambe's face and the rising smoke in the upper half, the clay pot on the mat as the lower third",
         amb="tent_storm"),
    dict(to=33, reason="turning point: a long, stretched, inhuman shadow slides across the canvas; long fingers scrape the cloth from outside", loc="tent_lantern",
         visual="inside the lantern-lit tent looking at the canvas wall: a tall, impossibly long and thin bent shadow of a figure slides across the outside of the canvas, with very long thin fingers pressed against the cloth from outside, the canvas dimpling under them; in the dark foreground the family are only small dark silhouettes huddled together, recoiling",
         camera="wide shot from inside, the stretched shadow on the canvas in the upper two-thirds, the huddled silhouettes and the mat floor as the lower third",
         amb="tent_storm", sens="other", safe="the only face-free shadow allowed (bible rule 11): a tall thin silhouette with long fingers on the canvas"),
    dict(to=34, reason="return to the women: Aisha screams 'It's come! Grandpa!' and drops beside Aslam (shot / reverse shot)", chars=["shareefa", "aisha", "aslam"], loc="tent_lantern",
         reuse="beat_015", visual="(reuse of beat_015)", amb="tent_storm", transition="cut"),
    dict(to=36, reason="action change: Aadhambe stands, recites over a bowl of water, blows three times and sprinkles it around the tent; a pained shriek outside", chars=["aadhambe"], loc="tent_lantern",
         visual="Aadhambe standing in the lantern-lit tent, eyes half closed in recitation, holding a small bowl of water in one hand and flicking drops of water from his fingers toward the canvas walls, the drops glinting in the lamplight; the canvas wall behind him shudders as if struck from outside",
         camera="medium shot, slightly low angle, Aadhambe's face and the bowl in the upper half, the mat floor as the lower third",
         amb="tent_storm"),
    dict(to=38, reason="action change: the tent's only lantern dims, its flame shrinking until it goes out completely", loc="tent_lantern",
         visual="close-up of the old oil lantern hanging from the tent's wooden pole, its flame shrunk to a tiny trembling blue-orange point, the glass dim, deep darkness closing in around it, the canvas behind barely visible",
         camera="close-up, the lantern and its dying flame in the upper half, the dark pole and shadow as the lower third",
         amb="tent_storm", sens="violence", safe="the moment Aslam seizes Aisha's throat (shot 38) is carried by the lantern dying — the grip is never shown"),
    dict(to=41, reason="time/light change: total darkness; only Aslam's pale eyes glow as he sits up rigid — the struggle is heard, not seen", chars=["aslam"], loc="tent_dark",
         visual=f"near-total darkness inside the tent: only the faint outline of Aslam sitting bolt upright, {POSS}, his two eyes glowing pale milky white in the black, staring straight ahead; everything else lost in shadow; nobody else visible",
         camera="medium close-up, Aslam's glowing eyes in the upper half, black emptiness as the lower third",
         amb="tent_storm", sens="violence", safe="the throat-grip on Aisha is never shown: darkness and glowing eyes only; Aisha is not in the frame"),
    dict(to=42, reason="character/action change: Raaidhu gropes to the clay pot and blows the embers alight; a little light returns", chars=["raaidhu"], loc="tent_dark",
         visual="Raaidhu on his knees in the dark tent, bent low over the small clay pot, blowing into it, the embers flaring bright orange and lighting his frightened young face from below, a few sparks rising; darkness all around",
         camera="close-up, slightly low angle, Raaidhu's face and the glowing pot in the upper half, the dark floor as the lower third",
         amb="tent_storm"),
    dict(to=44, reason="speaker/action change: in the ember light Shareefa pulls her son's arm — 'Aslam! Let go, my son!' — he will not budge", chars=["shareefa", "aslam"], loc="tent_dark", speaker="shareefa",
         visual=f"in the faint orange ember light: Shareefa in her maroon dress with {SH_HIJ}, gripping her son's forearm with both hands and pulling with all her strength, crying out in anguish; Aslam in the soft foreground at the side, {POSS}, sitting rigid and unmoving, his arm stretched away out of frame into the darkness; nobody else visible",
         camera="medium shot, Shareefa's anguished face centred in the upper half, Aslam soft at the side, dark floor as the lower third",
         amb="tent_storm", sens="violence", safe="Aisha is out of frame; only Shareefa pulling Aslam's arm in ember light"),
    dict(to=46, reason="speaker change: the spirit's heavy voice from Aslam's mouth — 'He is mine! None of you can save him!'", chars=["aslam"], loc="tent_dark", speaker="aslam",
         visual=f"close-up of Aslam in the ember light, {POSS}, a faint red vein-like glare in his milky eyes, lips parted as a deep voice that is not his own comes out, a cold sneer; dark shadows around him",
         camera="close-up, eye level, Aslam's face centred in the upper half, the dark collar of his checked shirt as the lower third",
         amb="tent_storm", sens="other", safe="possession shown without body horror: pale eyes, ashen skin, a sneer"),
    dict(to=48, reason="action change: Aadhambe recites the strongest verses and raises his stick; Aslam lets go and falls aside", chars=["aadhambe"], loc="tent_dark",
         visual="Aadhambe standing tall in the orange ember light, reciting loudly with a fierce, firm face, his long wooden walking stick raised high above his head in both hands; a faint shimmer of heat in the air in front of him; nobody else in the frame",
         camera="low-angle medium shot, Aadhambe's face and the raised stick in the upper half, the dark floor as the lower third",
         amb="tent_storm", sens="violence", safe="the stick strike is never shown as contact: only the raised stick while reciting; Aslam's fall is heard"),
    dict(to=51, reason="characters enter: Aisha gasping on the floor as Zaahid and Naazim tear through the door flap, soaked and stinking — 'Sameer has been killed!'", chars=["zaahid", "naazim", "aisha", "shareefa"], loc="tent_dark", speaker="zaahid",
         visual=f"the tent door flap thrown open: Zaahid and Naazim bursting in from the rain, {WETBROS}; Zaahid in front, weeping as he speaks, his face crumpled with grief; in the soft foreground Aisha in her lavender dress with {AI_HIJ} sitting on the floor with a hand at her collar, catching her breath, Shareefa in her maroon dress with {SH_HIJ} holding her shoulders; ember-orange light from below",
         camera="medium shot from inside, Zaahid's grieving face centred in the upper half, Naazim beside him, the women soft in the foreground, the floor as the lower third",
         amb="tent_storm"),
    dict(to=53, reason="return to the brothers at the flap: Naazim in panic — 'How can we be saved? The engine is broken!'", chars=["zaahid", "naazim", "aisha", "shareefa"], loc="tent_dark",
         reuse="beat_026", visual="(reuse of beat_026)", amb="tent_storm", transition="cut"),
    dict(to=56, reason="speaker change: Aadhambe looks at everyone — only sunrise saves them; they must stay shut in the tent", chars=["aadhambe"], loc="tent_dark", speaker="aadhambe",
         visual="Aadhambe sitting upright on the mat in the dim ember light, his walking stick planted beside him, looking around at the family with grave, steady eyes, speaking firmly, one hand raised in warning; the dark canvas wall behind him",
         camera="medium close-up, eye level, Aadhambe's face centred in the upper half, his hand and the stick, the dark mat as the lower third",
         amb="tent_storm"),
    dict(to=60, reason="scene change: something heavy lands on the tent roof; around the tent the beautiful terrible voice now speaks like a hundred voices — 'Aslam... come to me...'", chars=["handi"], loc="tent_outside",
         visual=f"the lone canvas tent on the dark storm-lashed beach seen from outside, faintly glowing orange from within, its wooden poles bent and the roof sagging under a pale crouching figure on top: {HANDI}, crouched on the tent roof, red eyes glowing; a swirling ring of sea-green mist circling the whole tent, with no faces in it; rain, lightning, the black jungle behind",
         camera="wide shot, the tent and the crouching spirit in the upper two-thirds, the dark wet sand as the lower third",
         amb="beach_storm_night"),
    dict(to=65, reason="turning point: Aslam's unconscious body slowly rises into the air, limbs hanging, face turned up to the roof; the family freeze in terror", chars=["aslam", "aadhambe", "shareefa", "aisha"], loc="tent_dark",
         visual=f"seen from the side in the orange ember light: Aslam floating horizontally about a metre above the tent floor as if lying on an invisible mat, perfectly straight and stiff like a plank, arms and legs hanging loosely downward, his head supported flat and level as on an invisible pillow, chin tucked slightly toward his chest, his calm sleeping face looking straight up at the canvas roof, eyes and mouth closed, peaceful and eerie; a faint grey haze around him; Aadhambe, Shareefa in her maroon dress with {SH_HIJ} and Aisha in her lavender dress with {AI_HIJ} recoiling at the side with their hands over their mouths; {KIDS}",
         camera="wide side shot, the floating figure and the family's faces in the upper two-thirds, the dark floor below him as the lower third",
         amb="tent_storm", sens="other", safe="levitation shown calm and eerie (bible rule 4): horizontal, limbs hanging, face upward — no bent-back head, no contortion"),
    dict(to=66, reason="action/speaker change: weeping Aisha reaches for her husband's foot; Aadhambe shouts 'Don't touch him! Get back!'", chars=["aadhambe", "aisha"], loc="tent_dark", speaker="aadhambe",
         visual=f"Aadhambe in the ember light shouting a warning, one arm thrust out to stop her, his face fierce and urgent; beside him Aisha in her lavender dress with {AI_HIJ}, worried and tearful, kneeling and lifting one open hand up toward the top of the frame, where a pale grey haze drifts down from above in the ember light; Aadhambe's outstretched arm held between her and that haze; only these two people in the frame",
         camera="medium shot, Aadhambe's shouting face centred in the upper half, Aisha's reaching hand and the hanging foot above, the dark floor as the lower third",
         amb="tent_storm"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Her long hair lay spread over the surf, and her two red eyes were glowing out of the darkness like red bulbs.",
   [("wave_crash", "ލޮނގަނޑުގެ", -20)], hum=True)
sh(2, "\"Naazim! What happened?\" Zaahid came slowly up from behind and asked. Without answering, Naazim pointed outside with a trembling hand.")
sh(3, "As soon as Zaahid too looked outside, his heart nearly leapt into his mouth. \"Ya Allah! What kind of terror is this?\"",
   [("gasp", "ކިރިޔާ", -18)], speaker="zaahid", hum=True)
sh(4, "Zaahid clapped his hand over his mouth. At that moment a loud scream was heard from the dhoni anchored in the lagoon.",
   [("heartbeat", "ހަޅޭކެއްގެ", -20)], hum=True)
sh(5, "It was the voice of the skipper Sameer, who had stayed behind to work on repairing the dhoni's engine. In that voice was an anguish like someone crying out for his life. \"Sameer!\"",
   [("wave_crash", "ދޯނީގެ", -24)])
sh(6, "Zaahid shouted. \"Wait! You must not go outside!\" Aadhambe called out loudly.", speaker="aadhambe")
sh(7, "But because skipper Sameer was a close friend of the family, Naazim and Zaahid could not bring themselves to stay quietly inside the tent.")
sh(8, "The two of them came out of the tent and, through the pouring heavy rain, heedless of the waves, ran towards the dhoni.",
   [("footsteps_sand", "ދުއްވައިގަތް", -18), ("wave_crash", "ރާޅުތަކަށް", -20)])
sh(9, "When they reached the dhoni, they could see a lantern's light swinging inside it. Zaahid and Naazim climbed aboard the dhoni.",
   [("creak", "އެރި", -18)])
sh(10, "When they stepped into the dhoni's cabin, what they saw was a heart-stopping sight. Skipper Sameer lay fallen at the engine-room door.",
   [("heartbeat", "ހިތްހުއްޓޭ", -18)], hum=True)
sh(11, "His eyes were open. On his throat were deep wounds, as if cut by long, sharp nails.", hum=True)
sh(12, "The blood flowing from those wounds was spreading through the dhoni. \"Sameer! Sameer!\"", speaker="naazim")
sh(13, "Naazim took hold of Sameer and shook him. But his soul had already left his body. Suddenly, from the stern of the dhoni, came the sound of a soft laugh.",
   [("heartbeat", "ހިނިތުންވުމެއްގެ", -20)], hum=True)
sh(14, "Startled, Zaahid and Naazim looked that way. By the dhoni's tiller, drenched in the salt sea, that female spirit sat laughing.",
   [("gasp", "ސިހިފަ", -18)], hum=True)
sh(15, "Seeing the blood on her face, they knew the spirit had something to do with Sameer's death. \"Next it is...\"", hum=True)
sh(16, "\"...your turn, you two...\" From the spirit's mouth came a frightening sound that made their hair stand on end.",
   [("low_growl", "ހީބިހިނަގާ", -20)], speaker="handi", hum=True)
sh(17, "It slowly stood up and began stepping toward Zaahid and Naazim. With each of her steps came a sound as if the dhoni's planks were cracking.",
   [("creak", "މުގުރެމުންދާ", -14)], hum=True)
sh(18, "Zaahid and Naazim realised there was no escape but to jump from the dhoni. Just as they turned to leap into the sea, a big wave rose out of the sea and shook the dhoni violently.",
   [("wave_crash", "ރާޅެއް", -14)])
sh(19, "As the huge wave struck one side of the dhoni, the whole dhoni heeled over to one side. Zaahid and Naazim lost their balance and were thrown onto the dhoni's deck.",
   [("wave_crash", "ބިޔަ", -14), ("soft_thud", "ޖެހުނު", -14)])
sh(20, "With that violent lurch, the wicked spirit by the tiller went up as if flying into the air and landed on the roof of the dhoni's cabin.",
   [("wind_gust", "އުދުހިގަތް", -16)], hum=True)
sh(21, "Her two red eyes glowed out of the pitch darkness like a terrifying light. \"Naazim! Jump! Hurry!\"",
   [("heartbeat", "ދިއްލެމުންދިޔައީ", -20)], hum=True)
sh(22, "Without a glance at the waves, Zaahid dived into the sea. Naazim too dived into the sea right behind him.",
   [("splash", "ފުންމާލި", -14), ("splash", "ފުންމާލައިފި", -16)])
sh(23, "As they sank into the cold sea water, what their bodies felt was not the feeling of an ordinary sea.")
sh(24, "The water had an oiliness and a foul smell, as if something were rotting. When they swam ashore to the island's white sand, a stench of rot rose from their whole bodies.",
   [("breath_heavy", "ފަތާފަ", -20), ("footsteps_sand", "ދޮންވެލިގަނޑަށް", -22)])
sh(25, "When they looked back, the spirit standing on the dhoni's cabin roof was slowly stretching out her arm towards the jungle.", hum=True)
sh(26, "It seemed as if she was signalling to the others of the family on the island. \"Zaahid!\"")
sh(27, "\"Quick, let's go to the tent! Everyone must be not knowing what has happened to us!\" Naazim ran off, panting.",
   [("breath_heavy", "މާނޭވާލަމުން", -18), ("footsteps_sand", "ދުއްވައިގަތް", -20)], speaker="naazim")
sh(28, "Meanwhile, the women and children in the tent were close to dying of fear.")
sh(29, "After the skipper's loud scream outside and the sound of Zaahid and the others running off, a dreadful silence had fallen over the whole area. Aslam's body, laid in the middle of the tent, twitched now and then.",
   [("heartbeat", "ތުރުތުރުއަޅައިގަނޭ", -22)], hum=True)
sh(30, "Grandfather sat beside a small clay pot, burning certain leaves to make smoke. With the scent of that smoke, the foul smell inside the tent faded a little.",
   [("fire_crackle", "އަންދައިގެން", -20)])
sh(31, "\"Shareefa, Aisha... bring the children and move to the middle of the tent. Don't go near the outer cloth of the tent.\"", speaker="aadhambe")
sh(32, "Aadhambe said in a calm, quiet voice. Suddenly a shadow could be seen stretching across the outside of the tent's cloth.",
   [("cloth_rustle", "ހިޔަންޏެއް", -20)], hum=True)
sh(33, "That was not a human's shadow. The shadow was very long and bent. The sound of its long fingers scraping at the tent's cloth from outside began to be heard.",
   [("cloth_rustle", "އުނގުޅަމުންދިޔަ", -16)], hum=True)
sh(34, "Khrees... khrees... \"It's come! Grandpa!\" Screaming in fear, Aisha dropped down beside Aslam.",
   [("cloth_rustle", "ޚްރީސް", -14), ("gasp", "ހަޅޭއްލަވައިގަންނަމުން", -18)], speaker="aisha", crop="tight", focus=[50, 18])
sh(35, "Aadhambe stood up, took the bowl of water in his hand and recited something. Then, after blowing over it three times, he began to sprinkle it around the tent.",
   [("breath_heavy", "ފުމެލާފަ", -24)])
sh(36, "At that moment a cry of pain was heard from outside. It seemed as if the body of something outside burned where those drops of water struck it.",
   [("low_growl", "ހަޅޭކެއްގެ", -18)], hum=True)
sh(37, "But in the midst of that terror, the light of the only lantern in the tent slowly began to dim.",
   [("bulb_flicker", "ފަނޑުވާން", -18)])
sh(38, "The oil lantern's flame shrank and shrank and suddenly went out altogether! As the whole tent sank into darkness, Aslam, lying unconscious, suddenly sat up and seized Aisha's throat hard with both hands.",
   [("bulb_flicker", "ނިވިއްޖެ", -16), ("gasp", "ހިފަހައްޓައިފި", -16)], hum=True)
sh(39, "In the darkness nothing at all could be seen. A loud cry of pain came from Aisha's throat.",
   [("heartbeat", "އަނދިރިކަމުގެ", -18)], hum=True)
sh(40, "Aslam's two hands were clamped on Aisha's throat like iron tongs. A dreadful strength no human could have had taken hold of that skinny young man's body.", hum=True)
sh(41, "As Aisha struggled to save herself, her breath was choking in her throat. At that moment everyone tried to get some light into the tent.",
   [("breath_heavy", "ނޭވާ", -18)])
sh(42, "Raaidhu, groping around, reached the pot where grandfather had made the smoke and began to blow into it with his mouth, and the pot caught fire. A little light came into the tent.",
   [("fire_crackle", "ރޯވެއްޖެ", -16)])
sh(43, "\"Aslam! Let go! My son! You're killing Aisha!\"", speaker="shareefa", hum=True)
sh(44, "Shareefa took hold of Aslam's arm and began to pull. But Aslam was locked so fast he could not even be budged.",
   [("cloth_rustle", "ދަމަންފެށި", -20)], speaker="shareefa")
sh(45, "From his mouth came the heavy, rasping voice of that wicked spirit. \"He is mine!\"",
   [("low_growl", "ހުނުމުގެ", -16)], speaker="aslam", hum=True)
sh(46, "\"None of you can save him today!\" That voice came out of Aslam's mouth.", speaker="aslam", hum=True)
sh(47, "Aadhambe began to recite loudly the most powerful verses he knew by heart. Reciting on, he struck Aslam's back hard with the pundit's stick in his hand.",
   [("soft_thud", "ޖެހި", -16)], hum=True)
sh(48, "With that, it seemed as if a hot vapour left Aslam's body. With a cry of pain he let go of Aisha's throat and fell to the other side of the tent.",
   [("soft_thud", "ވެއްޓުނު", -16)])
sh(49, "Aisha, coughing, sank to the ground, struggling to breathe. At that very moment Zaahid and Naazim tore through the tent's door cloth and burst inside.",
   [("fabric_tear", "ފަޅާލާފަ", -16)])
sh(50, "The rotten stench rising from their whole bodies hit everyone's nose. Naazim and Zaahid were panting. \"Bappa! Sameer...\"",
   [("breath_heavy", "މާނޭވާލަމުންދިޔަ", -18)], speaker="zaahid")
sh(51, "\"Sameer has been killed!\" Zaahid said, breaking down in tears. At this news, the hearts of the women in the tent seemed to leap into their mouths.",
   speaker="zaahid", hum=True)
sh(52, "This is a safe uninhabited island where people always come. But tonight this island has turned into a graveyard of death.")
sh(53, "\"How can we be saved now? The dhoni's engine is broken too!\" Naazim said in panic.", speaker="naazim", crop="tight", focus=[78, 16])
sh(54, "Aadhambe looked around at everyone. \"We'll leave this island only with the sunrise.\"", speaker="aadhambe")
sh(55, "\"That thing's power works in the black darkness of the night. We have no other way but to stay shut inside this tent tonight.\"", speaker="aadhambe")
sh(56, "\"No one must go outside! I kept telling you not to go just now, and still you went.\" Suddenly a loud sound came from the roof of the tent.",
   [("soft_thud", "އަޑެއް", -12)], speaker="aadhambe", hum=True)
sh(57, "It sounded as if something big and heavy had jumped down onto the roof. With that, the wooden poles holding up the tent seemed about to snap.",
   [("creak", "ބިންދައިގެންދިޔަހެން", -14)], hum=True)
sh(58, "From outside, beyond the tent's cloth, again came that beautiful yet terrifying woman's voice. But this time it was not the voice of a single person.",
   [("wind_howl", "ބިރުވެރި", -22)])
sh(59, "Like a hundred people speaking at once all around the tent, the voice echoed. \"Aslam...\"",
   [("wind_howl", "ގުގުމަމުންދިޔަ", -18)], speaker="handi", hum=True)
sh(60, "\"Come to me... or else your whole family will have to be buried here tonight.\"",
   [("low_growl", "ފޮރުވަން", -20)], speaker="handi", hum=True)
sh(61, "At that moment Aslam's body, lying unconscious on the ground, began slowly to rise into the air without anyone's help!",
   [("heartbeat", "ހިއްލެން", -18)], hum=True)
sh(62, "As his body rose straight up towards the top of the tent, everyone stood with their hands over their mouths in fear.",
   [("gasp", "އަތްއަޅައިގެން", -18)], hum=True)
sh(63, "Seeing Aslam's body rising slowly into the air without anyone touching it, everyone in the tent felt as if their blood had frozen.", hum=True)
sh(64, "His arms and legs hung downward. But his head was tipped back, his whole face turned straight up towards the tent's roof.", hum=True)
sh(65, "A foul, rotten smell came from his body more strongly than before. \"Ya Allah! Aslam!\"", hum=True)
sh(66, "Weeping, Aisha raised her hand to take hold of her husband's foot. \"Don't touch him! Get back!\" Aadhambe shouted loudly.",
   speaker="aadhambe", hum=True, crop="full", focus=[22, 40], motion="slow push-in")
SHOTS = S

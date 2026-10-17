"""Beat/shot plan for Aliflaila episode 509 (Night 5: the Third Old Man's tale; used by plan_beats.py)."""

LOC = {
    "chamber_night": "King Shahryar's palace bedchamber at night: a large Persian carpet in deep red and blue, a low cushioned divan with silk bolsters, brass lanterns hanging on chains, an arched window with a carved lattice screen opening on a moonlit city of white onion domes and slender towers under a huge moon",
    "chamber_dawn": "King Shahryar's palace bedchamber at the break of dawn: the Persian carpet, the cushioned divan, brass lanterns burning low, the arched carved-lattice window now glowing with golden dawn light over the city of domes, a distant slender minaret silhouetted against the pale gold sky",
    "desert": "a wide open sea of golden sand dunes beside a lone leafy tree and a small spring of clear water, distant blue mountains on the horizon, wind-rippled sand",
    "trader_home": "the comfortable courtyard home of a young trader in an old Arabian Nights town: whitewashed walls, a carved wooden door, potted lemon trees, a small tiled fountain, hanging brass lanterns, silk curtains in arched doorways",
    "ship": "the wooden deck of a large old cargo sailing ship with billowing cream sails, coiled ropes and bales of trade goods, open turquoise sea and a far coastline of foreign domes and palm trees",
    "back_door_night": "the narrow back lane behind a whitewashed town house late at night, a small low wooden back door in the wall, a vine climbing the wall, a huge moon over flat rooftops and domes",
    "house_night": "the dark inside of a whitewashed town house at midnight, a narrow hallway with a tiled floor and arched doorways, a wooden bedroom door standing slightly ajar with a thin wedge of dim amber lamplight spilling out",
    "room_night": "a dim richly furnished room of a town house at midnight lit by one small brass oil lamp: violet silk curtains, a Persian rug, a tall clay water jar in the corner, an arched window with its curtain blowing outward into the night",
    "street_night": "a moonlit cobbled street of an old Arabian Nights town at midnight, closed wooden doors, flat-roofed houses, long blue shadows",
    "alley_night": "a cold narrow alley behind houses at night, heaps of old baskets, broken crates and palm-leaf rubbish against a crumbling wall, puddles reflecting a pale moon",
    "fish_shop": "a small open-fronted fish shop in a busy morning bazaar of an old Arabian Nights town: a wooden counter with baskets of silver fish on palm leaves, a striped awning, sunlit stone street",
    "fishseller_home": "the simple, tidy home of an old fish-seller: whitewashed walls, a woven reed mat, a low wooden table with clay cups and a water jug, a plain sky-blue cloth curtain hanging across an arched doorway, sunlight through a small window",
    "sea_vision": "a lonely beach at dawn beside a calm sea, a poor fisherman's small wooden boat drawn up on the sand, a cast net in the shallow water",
}
MOOD = {
    "chamber_night": "deep midnight-blue night with warm amber lantern light and a big silver moon through the lattice window, intimate and suspenseful",
    "chamber_dawn": "break of dawn, soft rose and golden light pouring through the lattice window, the lanterns burning low, hushed relief",
    "desert": "bright golden afternoon sunlight, turquoise sky, long shadows on the dunes, wonder and suspense",
    "trader_home": "warm golden daylight with a soft golden storybook glow, gentle and loving but with a faint chill of hidden secrets",
    "ship": "golden late-afternoon sun over the sea with a soft golden storybook glow, wistful longing",
    "back_door_night": "midnight, deep blue moonlight and long shadows with a soft storybook glow, hushed and secretive",
    "house_night": "midnight, almost dark, deep blue shadows and one thin wedge of dim amber lamplight, dread and shock",
    "room_night": "midnight, a single small amber oil-lamp glow against deep violet shadows, tense and eerie",
    "street_night": "midnight, cold blue moonlight with a soft storybook glow, loneliness and fear",
    "alley_night": "the cold dead of night, pale blue moonlight, shivering misery",
    "fish_shop": "fresh early-morning golden sunlight with a soft golden storybook glow, kindness and pity",
    "fishseller_home": "warm late-afternoon sunlight with a soft golden storybook glow, gentle wonder",
    "sea_vision": "misty dawn with a dreamy soft golden glow, mysterious and enticing",
}

BEATS = [
    dict(to=5, reason="episode opening: Night 5 in the frame chamber — Shahrazad asks leave to continue, the king is impatient",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_night",
         visual="Shahrazad kneeling on a cushion on the carpet, bowing her head graciously with one hand on her heart and the other raised in a polite gesture, her large dark eyes lifted towards the king; King Shahryar sitting fully dressed on the divan an arm's length away, leaning forward eagerly with one empty hand waving her on impatiently, curious frown; little Dunyazad sitting on the carpet beside her sister hugging her knees, wide-eyed; the moonlit city of domes through the lattice window behind them",
         camera="wide shot, eye level, the three figures in the upper two-thirds, the carpet as a calm lower third", amb="palace_night"),
    dict(to=8, reason="story level change into the tale: the desert — the jinni, the merchant and the third old man stepping forward with his mule",
         chars=["merchant_jinni", "old_man_mule", "merchant", "old_man_gazelle"], loc="desert", transition="dissolve",
         visual="the towering giant jinni rising from a column of charcoal smoke beside the lone tree, arms folded, empty-handed, glowering down with ember eyes; in front of him the thin old man in a maroon robe and blue cap steps forward boldly holding the halter of a plain grey mule, looking straight up at the jinni with a firm steady face; the merchant in a plain white travelling robe kneels on the sand a little behind with hopeful eyes; the white-bearded first old man with his staff stands further back beside a small gazelle on a golden cord",
         camera="dramatic low angle wide shot, the jinni filling the upper frame, the figures in the middle, smooth sand as a calm lower third", amb="desert_day"),
    dict(to=11, reason="story level change into the old man's own tale: the young trader and his outwardly lovely wife",
         chars=["old_man_mule_young", "sorceress_wife"], loc="trader_home", transition="dissolve",
         visual="soft golden storybook glow; the young trader in his maroon robe and blue cap standing in his sunny courtyard smiling fondly at his beautiful wife, who stands a step away in her black-and-violet gown and dark-violet headscarf fully covering her hair and neck, smiling sweetly at him while her violet eyes glint with a cold secret; behind her, in the shade of an arched doorway, a faint wisp of violet smoke curls mysteriously",
         camera="medium wide two-shot, eye level, the fountain and tiles forming a calm lower third", amb="stone_house_day"),
    dict(to=14, reason="scene change: the year-long trading voyage at sea",
         chars=["old_man_mule_young"], loc="ship",
         visual="soft golden storybook glow; the young trader standing at the rail of a big sailing ship, the cream sails billowing above him, gazing back over the sea with a wistful longing look, one hand resting on the rail, foreign domes and palm trees on a far coast",
         camera="medium wide shot, slightly low angle, sails in the upper frame, calm sea as the lower third", amb="ship_deck"),
    dict(to=17, reason="time jump: a year later he returns secretly at midnight and slips in through the back door",
         chars=["old_man_mule_young"], loc="back_door_night", transition="black",
         visual="soft storybook glow; the young trader in his maroon robe and blue cap, a small travel bundle on his shoulder, quietly pushing open the small low back door of his house with a hopeful secretive smile, glancing over his shoulder, moonlight on the wall",
         camera="medium shot, eye level, from the side, the moonlit cobbles as a calm lower third", amb="city_lanes_night"),
    dict(to=21, reason="emotional turning point: at the half-open bedroom door he sees the betrayal (shown only on his face)",
         chars=["old_man_mule_young"], loc="house_night",
         visual="the young trader standing frozen in the dark hallway beside a door that is slightly ajar, a thin wedge of dim amber light falling across his face; his eyes wide with shock and heartbreak, mouth open, one hand gripping the door frame and the other pressed to his chest; nothing of the room beyond the door is visible, only the warm light",
         camera="close-up on his face and hand at the door frame, the dark tiled floor as a calm lower third", amb="stone_house_night",
         sens="intimacy", safe="the adultery is never shown: no lover, no couple, no bed — only the husband's shocked face in the wedge of light at the door"),
    dict(to=24, reason="action change: he bursts in; the room is empty but for his furious wife, the window curtain still flying",
         chars=["sorceress_wife", "old_man_mule_young"], loc="room_night",
         visual="the sorceress wife standing fully dressed in her black-and-violet gown and dark-violet headscarf in the middle of the dim room, her eyes blazing with violet fire, glaring defiantly towards the doorway; the young trader seen from behind in the foreground at the open door, shoulders tense; behind her the arched window stands open and empty, its curtain whipping outward into the night; no other person anywhere",
         camera="medium wide shot over the husband's shoulder, eye level, the rug as a calm lower third", amb="stone_house_night",
         sens="intimacy", safe="the lover who escaped is never drawn — only an empty open window with a blowing curtain; no bed is visible"),
    dict(to=26, reason="action change: she casts the spell with the water",
         chars=["sorceress_wife"], loc="room_night",
         visual="the sorceress wife beside the tall clay water jar, flinging a handful of water from her cupped hand towards the viewer, the water bursting into a glittering arc of violet sparkles and swirling smoke, her face fierce and commanding, her other hand pointing; magical violet glow lighting the dim room",
         camera="medium shot, slightly low angle, the sparkling arc crossing the frame, the rug as a calm lower third", amb="stone_house_night",
         sens="other", safe="sorcery as fairy-tale violet sparkles and smoke, no occult symbols"),
    dict(to=29, reason="action change: the transformation is complete — a big black dog stands where he was",
         loc="room_night",
         visual="a big black dog with sad human-like eyes sitting bewildered on the rug in the dim room, the last violet sparkles and wisps of smoke swirling away around it, a small dark-blue cap wrapped in grey cloth lying on the floor beside it; the dog looks up in confusion",
         camera="medium shot, eye level, the dog in the upper middle, the rug as a calm lower third", amb="stone_house_night",
         sens="other", safe="transformation shown only as the finished animal amid fading sparkles, never a half-changed body"),
    dict(to=31, reason="scene change: he is driven out into the street at night",
         chars=["sorceress_wife"], loc="street_night",
         visual="the big black dog standing alone on the moonlit cobbled street, looking back at a house doorway where the sorceress wife stands in silhouette against the amber light, one empty hand pointing out into the night, about to shut the heavy wooden door; nobody is touched",
         camera="wide shot, eye level, the empty cobbles as a calm lower third", amb="city_lanes_night",
         sens="violence", safe="the beating with a stick is not shown: only the wife's pointing silhouette at the door and the cast-out dog"),
    dict(to=34, reason="scene change: the frightened night among the other dogs and the rubbish heaps",
         loc="alley_night",
         visual="the big black dog curled up shivering among old baskets and broken crates in a cold moonlit alley, ears flat, sad eyes looking out; far away at the mouth of the alley three other dogs stand as dark silhouettes against the moonlight, their heads turned towards him",
         camera="medium wide shot, low angle, the puddled ground as a calm lower third", amb="city_lanes_night",
         sens="violence", safe="the attack is not shown: the other dogs only as distant silhouettes, the dog hiding and shivering"),
    dict(to=37, reason="time jump: the next morning at the kind old fish-seller's shop",
         chars=["fish_seller"], loc="fish_shop", transition="black",
         visual="soft golden storybook glow; the round kindly old fish-seller in his white skullcap and brown apron leaning over his wooden counter with a gentle pitying smile, tossing a small piece of fish down to the thin black dog that sits before the shop looking up at him with pleading, sorrowful eyes; baskets of silver fish, a striped awning, a few small background shoppers in modest clothing",
         camera="medium wide shot, eye level, the sunlit street as a calm lower third", amb="bazaar_day"),
    dict(to=40, reason="scene and character change: at the fish-seller's home the veiled daughter hides behind the curtain",
         chars=["fishseller_daughter", "fish_seller"], loc="fishseller_home",
         visual="soft golden storybook glow; the old fish-seller standing just inside his doorway with the black dog sitting at his feet; across the room his veiled daughter in a sky-blue gown, white headscarf and white face veil half-hidden behind a sky-blue curtain in an arched doorway, one hand drawing the curtain across herself, her large dark eyes wide with alarm, her other hand raised towards her father",
         camera="medium wide shot, eye level, the reed mat as a calm lower third", amb="stone_house_day"),
    dict(to=43, reason="emotional turning point: she reveals he is an enchanted man; the dog nods with tearful eyes",
         chars=["fish_seller"], loc="fishseller_home",
         visual="soft golden storybook glow; close on the big black dog sitting on the reed mat, nodding its head, tears shining in its sad human-like eyes; beside it the old fish-seller bends down in astonishment, hands raised, mouth open, eyebrows high",
         camera="medium close-up, low eye level, the mat as a calm lower third", amb="stone_house_day"),
    dict(to=45, reason="action change: the daughter breaks the spell with water and prayerful words",
         chars=["fishseller_daughter"], loc="fishseller_home",
         visual="soft golden storybook glow; the veiled daughter in her sky-blue gown and white headscarf standing calmly, holding a clay cup of water, sprinkling a gentle arc of shining golden water-drops towards the black dog in front of her, warm golden sparkles beginning to swirl around the dog; her dark eyes kind and serene",
         camera="medium wide shot, eye level, the mat as a calm lower third", amb="stone_house_day",
         sens="other", safe="her counter-spell shown as gentle golden light and water-drops, no occult symbols"),
    dict(to=47, reason="action change: he is a man again and thanks them with joy",
         chars=["old_man_mule_young", "fish_seller", "fishseller_daughter"], loc="fishseller_home",
         visual="soft golden storybook glow; the young trader in his maroon robe and blue cap standing restored in a fading swirl of golden sparkles, hands pressed together in heartfelt thanks, tears of joy on his face, bowing towards the beaming old fish-seller; the veiled daughter stands a respectful distance away by the curtain, her eyes smiling",
         camera="medium wide shot, eye level, the mat as a calm lower third", amb="stone_house_day",
         sens="other", safe="transformation back shown only as the finished man amid fading sparkles; no touching between him and the girl"),
    dict(to=50, reason="action change: he asks for justice and she prepares the little flask of water",
         chars=["fishseller_daughter", "old_man_mule_young", "fish_seller"], loc="fishseller_home",
         visual="soft golden storybook glow; the veiled daughter holding up a small corked glass flask of water that glows softly with golden light, setting it down on a small brass tray on the low table; across the table the young trader leans forward earnestly with determined eyes, the old fish-seller beside him nodding",
         camera="medium shot, eye level, the table top as a calm lower third", amb="stone_house_day",
         sens="other", safe="no touching: the flask is placed on a tray between them"),
    dict(to=53, reason="time jump: that midnight he returns home with the flask",
         chars=["old_man_mule_young"], loc="room_night", transition="black",
         visual="the young trader in his maroon robe and blue cap standing in the dim room at midnight, his face grim and resolute in the amber lamplight, holding up the uncorked little flask and flinging a glittering golden arc of water towards a dim covered shape far back in the violet shadows; only a heap of dark blankets is seen there, no person visible",
         camera="medium shot from the side, eye level, the rug as a calm lower third", amb="stone_house_night",
         sens="other", safe="the sleeping wife is never shown in a bed: only a dark covered heap far in the shadows; magic as golden sparkles"),
    dict(to=54, reason="action change: the wife has become a mule",
         loc="room_night",
         visual="a plain grey mule standing in the dim room among swirling golden-and-violet sparkles that fade away, its ears back, a dark-violet scarf slipping off its neck onto the rug; amber lamplight",
         camera="medium wide shot, eye level, the rug as a calm lower third", amb="stone_house_night",
         sens="other", safe="transformation shown only as the finished animal amid fading sparkles"),
    dict(to=56, reason="story level change back to the tale: the old man presents the mule to the jinni",
         chars=["old_man_mule", "merchant_jinni"], loc="desert", transition="dissolve",
         visual="the thin old man in his maroon robe and blue cap standing beside the grey mule in the golden sand, one open hand presenting the mule, his other hand raised in a questioning gesture, a sly confident smile; the towering smoky jinni in his dark-red robe leans down over them, empty-handed, eyebrows raised in fascination",
         camera="low angle medium wide shot, the jinni in the upper frame, the sand as a calm lower third", amb="desert_day"),
    dict(to=60, reason="action change: the delighted jinni claps and frees the merchant entirely",
         chars=["merchant_jinni", "merchant", "old_man_mule", "old_man_dogs"], loc="desert",
         visual="the towering jinni rising high on his smoke column, throwing back his head and clapping his huge empty hands in delight, laughing, his ember eyes bright; golden sand swirling around him; below, the merchant in his white travelling robe on his knees raising both hands in joy and disbelief; the old man with the grey mule and the second old man in brown beside two black dogs sitting calmly on leashes look up smiling",
         camera="dramatic low angle wide shot, the jinni filling the upper frame, the sand as a calm lower third", amb="desert_day",
         sens="violence", safe="the jinni's sword is never drawn: his hands are empty, clapping"),
    dict(to=61, reason="action change: the jinni turns to black smoke and sinks into the earth",
         chars=["merchant"], loc="desert",
         visual="a huge column of swirling charcoal-black smoke spiralling down into a glowing crack in the golden sand and vanishing, sand grains flying; the merchant in his white travelling robe kneels in the foreground with his hands on his chest, weeping with relief, looking at the place where the jinni disappeared",
         camera="wide shot, eye level, the smoke spiral in the upper half, smooth sand as a calm lower third", amb="desert_day"),
    dict(to=63, reason="action change: the merchant thanks the three old men, who leave with their animals",
         chars=["merchant", "old_man_gazelle", "old_man_dogs", "old_man_mule"], loc="desert",
         visual="the merchant in his white travelling robe joyfully clasping the hands of the three old men by the lone tree, tears of joy on his face; the white-bearded first old man with his staff and the gazelle on a golden cord, the second old man in brown with two black dogs sitting calmly on leashes at a little distance, the thin third old man in maroon holding the grey mule's halter; a sunset glow over the dunes behind",
         camera="wide shot, eye level, the figures in the middle band, the sand as a calm lower third", amb="desert_day"),
    dict(to=66, reason="story level change back to the frame: the tale ends, the king sighs with relief",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_night", transition="dissolve",
         visual="King Shahryar alone on the divan on the right, leaning back against the bolsters with a deep sigh of relief, eyes half-closed and a faint satisfied smile, one empty hand resting on his knee; on the left, down on the carpet well apart from the divan (more than an arm's length away), Shahrazad kneels on a floor cushion with a modest confident smile, hands folded in her lap, and little Dunyazad sits on the carpet beside her smiling happily; nobody else sits on the divan; lanterns glowing, the moonlit domes in the lattice window between them",
         camera="medium wide shot, eye level, the carpet as a calm lower third", amb="palace_night"),
    dict(to=70, reason="Shahrazad's teaser of the next tale: a vision of the poor fisherman's net with a golden jar",
         chars=["fisherman"], loc="sea_vision", transition="dissolve",
         visual="dreamy soft golden glow like a vision; the thin old fisherman in his patched blue tunic standing knee-deep in the calm dawn sea, hauling in his cast net with an astonished face; tangled in the net a large gleaming golden-brass jar with a sealed lid glows mysteriously, a faint thread of dark smoke curling from its lid",
         camera="medium wide shot, eye level, the still water as a calm lower third", amb="dream_glow",
         sens="other", safe="the terrifying thing from the jar is not shown — only a faint thread of smoke; the seal is a plain lid with no symbols"),
    dict(to=72, reason="return to the frame: the king's eyes widen with new curiosity", reuse="beat_001", loc="chamber_night",
         transition="dissolve", amb="palace_night",
         visual="(reuse of beat_001)"),
    dict(to=76, reason="time change: dawn breaks — Shahrazad falls silent, the king spares her another day and rises for court",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="golden dawn light pouring through the arched lattice window, a distant slender minaret silhouetted against the pale gold sky; King Shahryar rising from the divan, fully dressed, turning towards the door with a thoughtful look back over his shoulder; Shahrazad sitting quietly on her cushion with lowered eyes and a hidden relieved smile, Dunyazad leaning against her sister's shoulder, the lanterns burning low",
         camera="wide shot, eye level, the window light in the upper frame, the carpet as a calm lower third", amb="palace_dawn"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Shahrazad looked towards King Shahryar with her beautiful, deep-dark eyes, and, lowering her head with great courtesy, asked for permission.",
   [("cloth_rustle", "ޖަހައިލަމުން", -24)])
sh(2, "\"Most noble and mighty king, will you grant me leave to continue the story?\" \"Tell it quickly!\"")
sh(3, "King Shahryar said hastily. \"I very much want to know what the third old man's secret is,")
sh(4, "and my heart is impatient to see whether that jinni killed the merchant or not.\"")
sh(5, "Shahrazad began the tale in her soft, lovely voice. \"O mighty and wise king!")
sh(6, "When the second old man finished his story, the huge jinni pardoned two of the three thirds of the merchant's life. Then,")
sh(7, "the third old man, leading a mule by the hand, stepped forward. Looking straight at the fearsome jinni, he began to speak with great firmness.",
   [("footsteps_sand", "ޖެހިލިއެވެ", -22)])
sh(8, "'O mighty jinni! This mule standing here beside me is no ordinary animal. In truth it is my very own wife.")
sh(9, "She and I were married many years ago. From the outside she was an exceedingly beautiful, loving woman.")
sh(10, "But hidden inside her were utterly wicked, dark secrets. That she had learned the worst arts of sorcery and witchcraft,")
sh(11, "that she was a most evil sorceress, I had no idea. One year after our wedding, I had to make a long journey to a very distant country for trade.")
sh(12, "Before setting out, I put my wife in charge of everything in the house and bade her a loving farewell.")
sh(13, "Then I sailed away on a big ship. A whole year passed on my journey.",
   [("wave_crash", "ނަވެއްގައި", -24)])
sh(14, "Even while I was in foreign lands, my heart was always full of memories of my wife.")
sh(15, "When the journey was over, I came back to my island and landed at midnight.")
sh(16, "Wanting to surprise my wife, I told no one, and crept secretly into my house through the small door at the back.",
   [("door_open", "ދޮރުން", -20)])
sh(17, "The whole house was dark. Stepping slowly, I made my way up to our bedroom,",
   [("footsteps_pavement", "ފިޔަވަޅު", -24)])
sh(18, "and its door stood slightly open. A dim light was showing from inside. The moment I looked into the room,",
   [("creak", "ހުޅުވިފައެވެ", -22)])
sh(19, "the sight before my eyes almost stopped my heart. My most beloved wife was with another man in my own bed!",
   [("heartbeat", "ހުއްޓުނު", -18)], hum=True)
sh(20, "That man was big, dark and frightening to look at. The two of them were taking their pleasure.", hum=True)
sh(21, "At that sight it was as if the sky had fallen on my head. Rage and grief set my whole body trembling. Unable to bear it,",
   [("breath_heavy", "ތުރުތުރުއަޅަން", -20)])
sh(22, "I flung the bedroom door open and went in. The moment he saw me, that man sprang to his feet,",
   [("door_open", "ހުޅުވައިލާފައި", -16)])
sh(23, "leapt out through the window and fled. But my wife, without the least fear, stood glaring at me in utter fury.",
   [("wind_gust", "ކުޑަދޮރުން", -22)])
sh(24, "Her eyes seemed to blaze with fire. Without giving me a chance to say a word, she scooped a handful of water from a jar in the corner of the room,",
   [("pour", "ނެގިއެވެ", -20)])
sh(25, "and after chanting a spell in strange, terrifying words she threw the water on me. And she screamed: 'Leave your human form,",
   [("magic_shimmer", "ކިޔެވުމަށްފަހު", -18), ("water_splash_small", "ޖެހިއެވެ", -18)])
sh(26, "and become a dog at once!' O mighty jinni! As soon as those drops touched my body,",
   [("magic_shimmer", "ޖެހުމާއެކު", -18)])
sh(27, "an indescribable pain went through my whole body. The bones of my body broke and my shape began to change.",
   [("breath_heavy", "ވޭނެއް", -20)], hum=True)
sh(28, "My mouth grew long, hair sprouted all over me, and I fell onto four paws. In a short moment I was no longer human.")
sh(29, "I had become a big black dog! When I tried to speak, only the sound of a dog's barking came out of my mouth.")
sh(30, "That wicked wife took a stick and began to beat me. Tormenting me all the way,")
sh(31, "she drove me out of the house door and threw me into the street. That night I roamed the street in terrible fear.",
   [("door_slam", "އެއްލައިލިއެވެ", -18)])
sh(32, "As soon as the other dogs saw me, they came at me angrily. Suddenly,")
sh(33, "three big, fierce dogs came to attack me. To save my life I ran, and hid among the rubbish heaps behind the houses.",
   [("footsteps_pavement", "ދުވަމުން", -20)])
sh(34, "From hunger and cold I was close to dying. The next morning, as I walked along the street, starving,",
   [("wind_gust", "ފިނީގެ", -24)])
sh(35, "I saw a fish shop. In that shop stood a very kind old fish-seller. I went up to him,")
sh(36, "and stood looking at him the way a person would plead. That old man saw the sorrow in my eyes and felt pity.")
sh(37, "He tossed me a piece of fish and a bone. I ate it, and to show my thanks I rubbed my head against his feet.",
   [("soft_thud", "އެއްލިއެވެ", -24)])
sh(38, "That day, when he closed the shop and went home, I followed behind him. He went into his house and let me come inside too.",
   [("door_open", "ވަދެ", -22)])
sh(39, "Living in that house were he and his young daughter. As soon as the girl saw me,")
sh(40, "she suddenly covered her face and hid behind a curtain. 'Father!' the girl cried out. 'Who is this you have brought into the house?",
   [("cloth_rustle", "ނިވާކޮށް", -22), ("gasp", "ބައްޕާއެވެ", -22)])
sh(41, "That is no dog! That is an enchanted man! I am someone who knows the science of magic. As far as I can tell,")
sh(42, "his wicked wife put a spell on him and turned him into a dog.' The fish-seller was utterly astonished.",
   [("gasp", "ޙައިރާންވިއެވެ", -22)])
sh(43, "He found it hard to believe what his daughter said. But to show that what the girl said was true, I nodded my head and looked at them with tearful eyes.",
   [("sob_breath", "ކަރުނަވީ", -24)], hum=True)
sh(44, "The girl went inside and came back with a cup of water. Gazing into the cup, she recited beautiful words over it.",
   [("pour", "ފެންތައްޓެއް", -22)])
sh(45, "Then she sprinkled the water on me and said: 'By the will of God, leave the form of a dog and become human again!'",
   [("water_splash_small", "ޖަހާފައި", -18), ("magic_shimmer", "އިރާދަފުޅުން", -18)])
sh(46, "At once my body began to change back. Within a few seconds I had turned back into a human being!",
   [("magic_shimmer", "ބަދަލުވާން", -18)], hum=True)
sh(47, "Overjoyed, I thanked the old man and his daughter again and again. Then I made a request of his daughter.")
sh(48, "'O good girl! I want to repay my wicked wife for the cruelty she did to me.")
sh(49, "Teach me a way to give her the punishment she deserves.' The girl smiled, poured water into a small flask, recited over it, blew on it, and gave it to me.",
   [("pour", "އަޅައި", -22), ("breath", "ފުމުމަށްފަހު", -24)])
sh(50, "'Take this flask of water. Go to your house, wait until she is asleep, and throw this water on her.")
sh(51, "Then name whatever animal you wish and command her to turn into that shape.' I hid the flask and went secretly into my house.",
   [("door_open", "ވަނީމެވެ", -22)])
sh(52, "It was midnight. My wife lay fast asleep. I went near her, pulled the stopper from the flask and threw the water on her face.",
   [("water_splash_small", "ޖެހީމެވެ", -18)])
sh(53, "And I cried out loudly: 'Leave your human form and become a mule at once!' At that moment she woke and screamed.",
   [("magic_shimmer", "ބަދަލުވާށެވެ", -18), ("gasp", "ހަޅޭއްލަވައިގަތެވެ", -20)])
sh(54, "But her voice changed, her body grew bigger, her bones swelled, and in a short moment she had turned into a mule!",
   [("magic_shimmer", "ބަދަލުވެއްޖެއެވެ", -18)], hum=True)
sh(55, "O mighty jinni! This standing here beside me is that very mule. This is my wicked wife.")
sh(56, "This is the story of what happened between her and me. Is it not far more wondrous than the two earlier old men's stories?' The huge,")
sh(57, "fearsome jinni threw down his big sword and clapped his hands in joy. The sound echoed across the whole desert. 'Yes! Yes!' the jinni cried.",
   [("soft_thud", "އެއްލައިލައި", -20), ("thunder", "ގުގުމައިލިއެވެ", -22)])
sh(58, "'That is truly a most wondrous story, full of lessons. The three stories you three old men have told me are wonderful tales such as I have never heard in all my life.")
sh(59, "Therefore, for the third old man's story, I pardon the remaining third of this merchant's life as well.")
sh(60, "He is free now. I give him leave to go wherever he wishes!' Having said this, the huge jinni once again turned into a great,")
sh(61, "black cloud of smoke, split the ground, sank down into it and vanished. The merchant felt as if he had been born again. Weeping with joy,",
   [("smoke_whoosh", "ދުންގަނޑަކަށް", -16), ("stone_scrape", "ފަޅާފައި", -18), ("sob_breath", "ރޮމުން", -24)], hum=True)
sh(62, "he embraced the three old men and thanked them again and again. 'You are the angels who saved my life!' he said.", hum=True)
sh(63, "After that, the three old men went on their way with their animals. And the merchant returned joyfully to his island, to his beloved wife and children.",
   [("footsteps_sand", "ހިނގައްޖެއެވެ", -24)])
sh(64, "Here ends the tale of the merchant and the jinni.\" As Shahrazad finished the story, King Shahryar let out a deep breath.",
   [("sigh", "ނޭވާއެއް", -18)])
sh(65, "A great calm came over his heart. But he said: \"That is truly a very beautiful, wondrous story.\"")
sh(66, "Shahrazad said, very gently but with confidence: \"O noble king. This story is finished. But it is")
sh(67, "nothing at all compared with the story I mean to tell next, the tale of 'The Fisherman and the Jinni'.")
sh(68, "That story is many times more wondrous, more frightening and more thrilling than this one. If you were to hear the story of the poor")
sh(69, "old fisherman who, on the day he cast his net into the sea, found a big golden flask caught in it,",
   [("net_cast", "އެއްލި", -20), ("splash", "ދަލުގައި", -22)])
sh(70, "and of the fearsome thing that came out of that flask, Your Majesty would be astonished.\"",
   [("smoke_whoosh", "ނުކުތް", -22)])
sh(71, "King Shahryar's eyes grew wide. A great fire of new curiosity was kindled in his heart.")
sh(72, "He longed intensely to know what had happened to that poor fisherman. At that very moment, the beautiful golden light of dawn appeared in the east,")
sh(73, "and the call to the dawn prayer spread across the whole capital. Shahrazad fell silent at once. The king spoke to himself.")
sh(74, "\"I will not kill her today either. Tonight, after hearing that fisherman's story, I will kill her tomorrow morning.\" And so the king rose,",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(75, "and went to the court to govern. The fifth night was over. Through Shahrazad's wisdom and her great skill at storytelling,",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -24)])
sh(76, "her life was saved for one more day. Next comes the sixth night, when the fisherman's great secret will be revealed.",
   [("breath", "ސަލާމަތްވީއެވެ", -22)], hum=True)

SHOTS = S

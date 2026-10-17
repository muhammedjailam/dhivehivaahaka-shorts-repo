"""Beat/shot plan for Aliflaila episode 585 (Night 8: King Yunan and Sage Duban, part two; the four-coloured fish)."""

LOC = {
    "chamber": "King Shahryar's palace bedchamber at night: a deep midnight-blue room with carved white arches, a large arched window with a carved lattice screen showing a moonlit city of onion domes and slender towers under a huge moon, glowing brass lanterns, a rich Persian carpet with silk cushions, a cushioned divan along the wall",
    "yunan_hall": "King Yunan's grand throne hall: tall white marble columns, a raised throne of carved gold and purple velvet on a marble dais, high arched windows with lattice screens, hanging brass lanterns, a polished marble floor with inlaid geometric patterns",
    "yunan_private": "King Yunan's private sitting room in his palace: a small richly furnished room with purple silk curtains, a low cushioned divan, a carved lattice window, a brass lamp on a low table, a polished marble floor",
    "yunan_hall_dark": "King Yunan's grand throne hall emptied of people: tall white marble columns, a raised throne of carved gold and purple velvet on a marble dais, high arched windows, a polished marble floor",
    "seashore": "a lonely sandy seashore below low rocks, the open turquoise sea with gentle waves, wet sand and a few shells, a wide sky with soft clouds",
    "journey": "a sweeping wild landscape of great rocky mountains and golden desert dunes under a vast sky",
    "lake": "a hidden wondrous lake ringed by four tall rocky mountains, water clear as crystal over pale pebbles, a narrow shore of smooth stones and low green reeds",
    "sultan_hall": "the Sultan's audience hall: blue-and-white tiled arches, sapphire silk curtains, a cushioned throne seat on a low dais, brass lanterns, a polished marble floor",
    "kitchen": "a large palace kitchen: whitewashed stone walls, a big clay-and-brick hearth with a glowing fire, copper pots hanging from hooks, baskets of onions and herbs, a wide black iron frying pan on the fire, a flagstone floor",
    "chamber_dawn": "King Shahryar's palace bedchamber at the break of dawn: carved white arches, a large arched window with a carved lattice screen opening onto a city of domes and a distant slender minaret silhouette, brass lanterns burning low, a rich Persian carpet with silk cushions, a cushioned divan",
}
MOOD = {
    "chamber": "late night just before dawn, deep midnight-blue shadows, warm amber lantern glow on the faces, a big silver moon in the window, intimate and expectant",
    "yunan_hall": "bright daytime, golden sunlight slanting through the high windows, a soft golden storybook glow over everything (tale within the tale), courtly splendour with an undercurrent of envy and tension",
    "yunan_private": "daytime, warm dim light through the lattice window, a soft golden storybook glow (tale within the tale), secretive and conspiratorial",
    "yunan_hall_dark": "the light fading, cold grey-violet gloom, one beam of pale golden light falling from a high window, a soft golden storybook glow at the edges (tale within the tale), solemn, eerie and tragic",
    "seashore": "late afternoon, warm golden sunlight, sparkling turquoise sea, a light breeze, fairy-tale full colour",
    "journey": "bright midday sunlight, turquoise sky, long shadows on golden sand, a sense of wonder and adventure",
    "lake": "clear bright day, turquoise sky, sunlight glittering on crystal water, magical and wondrous with soft sparkles",
    "sultan_hall": "bright daytime, sunlight through blue-tiled arches, rich sapphire and gold colours, joyful wonder",
    "kitchen": "evening, warm orange firelight from the hearth, deep shadows in the corners, then an eerie emerald magic glow, mysterious",
    "chamber_dawn": "dawn, soft rose-gold morning light pouring through the lattice window, lanterns burning low, the minaret silhouette against a pale golden sky, a hushed relieved mood",
}

BEATS = [
    dict(to=6, reason="episode opening: the frame chamber — Dunyazad asks for the rest of the tale, the king permits, Shahrazad begins",
         chars=["shahrazad", "dunyazad", "shahryar"], loc="chamber",
         visual="Shahrazad sits gracefully on a silk cushion on the carpet, turning towards the king with a respectful bow of her head and one hand raised in an elegant storytelling gesture; little Dunyazad sits on the carpet beside her, leaning eagerly towards her sister with bright pleading eyes and clasped hands; King Shahryar sits upright on the cushioned divan an arm's length away, fully dressed, chin resting on his hand, nodding with keen curiosity; the moonlit city of domes through the lattice window behind them",
         camera="medium wide, eye level, the three faces in the upper two-thirds, the patterned carpet as a calm lower third", amb="palace_night"),
    dict(to=8, reason="scene change: dissolve into the tale of King Yunan — the vizier's envy of Duban at court",
         chars=["king_yunan", "sage_duban", "yunan_vizier"], loc="yunan_hall", transition="dissolve",
         visual="in the sunlit throne hall King Yunan, healthy and smiling on his golden throne, warmly lays a rich embroidered robe of honour over the shoulders of the old sage Duban who bows gratefully before him; at the side behind a marble column the thin vizier in grey turban and olive robe watches with narrowed jealous eyes and a bitter scowl, half in shadow; small courtiers in modest robes in the background; soft golden storybook glow",
         camera="wide shot, slightly low angle, the vizier in the foreground right, the king and Duban mid-ground, the marble floor as a calm lower third", amb="throne_hall"),
    dict(to=11, reason="location and action change: the vizier secretly approaches the king alone",
         chars=["yunan_vizier", "king_yunan"], loc="yunan_private",
         visual="King Yunan sits alone on a low cushioned divan in his private room; the thin vizier bends close at his side with one hand raised beside his mouth as if whispering a secret, his face set in false worried loyalty, his narrow eyes sly; the king turns his head towards him, listening with a puzzled frown; soft golden storybook glow",
         camera="medium two-shot, eye level, faces in the upper half", amb="palace_day"),
    dict(to=15, reason="emotional turning point: the king angrily rejects the accusation and defends Duban",
         chars=["king_yunan", "yunan_vizier"], loc="yunan_private",
         visual="King Yunan has risen from the divan, angry, one empty hand raised in a firm stopping gesture, his brows drawn together, defending his friend; the vizier steps back a pace, bowing low with hands pressed together in mock humility while his eyes still glint with cunning; soft golden storybook glow",
         camera="medium wide, eye level, the king slightly higher in frame", amb="palace_day"),
    dict(to=19, reason="action change: the vizier's cunning insinuation — the cure could just as easily become murder",
         chars=["yunan_vizier", "king_yunan"], loc="yunan_private",
         visual="close on the vizier leaning in with a sly persuasive half-smile, one bony finger lifted as he makes his point; on the low table between him and the king lie an old wooden polo mallet and a small ornate perfume flask catching the light; behind him, slightly out of focus, King Yunan sits back on the divan, his anger giving way to unease; a long dark shadow of the vizier falls across the lattice wall; soft golden storybook glow",
         camera="medium close-up over the table, the vizier's face in the upper third, the king behind", amb="palace_day"),
    dict(to=21, reason="emotional turning point: the seed of doubt — fear takes hold of the king and he decides on Duban's death",
         chars=["king_yunan"], loc="yunan_hall",
         visual="King Yunan sits alone on his golden throne gripping its armrests, his face pale with fear and suspicion, eyes wide and darting, sweat on his brow; behind him on the marble wall looms a huge twisting dark shadow shaped like the vizier's whispering profile; a servant in a plain robe hurries out through a far archway to summon the sage; the soft golden storybook glow dimmed by gathering gloom",
         camera="medium shot, slightly low angle, the king and the looming shadow in the upper two-thirds", amb="throne_hall"),
    dict(to=25, reason="character entrance and action change: Duban arrives hopeful, sees the angry king and the guards, and is accused",
         chars=["sage_duban", "king_yunan"], loc="yunan_hall",
         visual="the old sage Duban has just stepped into the throne hall with a hopeful gentle smile fading into shock, one hand at his chest; ahead of him King Yunan on his throne glares down and points an accusing finger at him; a row of stern palace guards in tall turbans stands along the columns with their empty hands clasped behind their backs, no weapons; soft golden storybook glow turning cold",
         camera="wide shot from behind Duban's shoulder towards the throne, the king high in the frame, the marble floor as a calm lower third", amb="throne_hall",
         sens="violence", safe="the death sentence is only spoken; the guards carry no weapons and stand still with empty hands"),
    dict(to=29, reason="action change: Duban pleads for his life; the poisoned king coldly orders the execution",
         chars=["sage_duban", "king_yunan", "yunan_vizier"], loc="yunan_hall",
         visual="Duban kneels on the marble floor before the dais with both palms raised in desperate pleading, tears in his kind old eyes; King Yunan has turned his face away on the throne, cold and unmoved, one hand lifted in a dismissive command; behind the throne the vizier smirks in quiet triumph; no executioner and no weapon visible; soft golden storybook glow",
         camera="medium wide, eye level, Duban in the left foreground, the king and vizier upper right", amb="throne_hall",
         sens="violence", safe="the execution order is shown only as the king turning away; the executioner is never shown, no sword"),
    dict(to=33, reason="emotional turning point: Duban accepts his fate and asks for time and to present a gift",
         chars=["sage_duban"], loc="yunan_hall",
         visual="the old sage Duban standing calmly alone on the marble floor, eyes half closed after a deep sigh, one hand laid over his heart and the other open towards the throne in a dignified offering gesture, a beam of soft golden light from a high window falling on him, his long white beard and ochre robe glowing; peaceful resignation on his face; soft golden storybook glow",
         camera="medium shot, slightly low angle, his face in the upper third", amb="throne_hall"),
    dict(to=39, reason="action change: the king's curiosity about the wondrous book; he grants Duban one day",
         chars=["king_yunan", "sage_duban"], loc="yunan_hall",
         visual="King Yunan leans forward on his throne with wide fascinated eyes and a hand on his beard, captivated; Duban stands before him gesturing with both hands, and between them floats a dreamy glowing image of a large closed ancient book with a plain leather cover, surrounded by swirling golden sparkles; no writing anywhere; soft golden storybook glow",
         camera="medium wide, eye level, the floating glowing book at the centre", amb="throne_hall"),
    dict(to=43, reason="time jump: the next day — the whole court assembled, Duban arrives with the old book and medicine bottles",
         chars=["sage_duban", "king_yunan"], loc="yunan_hall", transition="black",
         visual="the throne hall full of courtiers standing in rows along the columns; the old sage Duban kneels on the marble floor before the throne, carefully setting a large heavy ancient book with a plain worn leather cover on a low carved wooden stand, three small glass medicine bottles with corks beside it; King Yunan watches eagerly from his throne; Duban's face is calm and knowing; no tray; soft golden storybook glow",
         camera="wide shot, eye level, Duban and the book centre, the king upper right, the marble floor as a calm lower third", amb="throne_hall"),
    dict(to=44, reason="sensitive turning point: the execution — shown only as a snuffed candle",
         chars=[], loc="yunan_hall_dark",
         visual="close on a tall white candle in a brass holder standing on the marble floor beside the closed ancient book on its carved stand; the flame has just gone out and a thin curl of grey smoke rises from the wick into a beam of pale light; in the far blurred background the shadows of courtiers turning their faces away; no people in focus, no weapon",
         camera="close-up, low angle, the candle and smoke in the upper two-thirds", amb="throne_hall",
         sens="violence", safe="Duban's beheading is never shown (bible rule 10): only a candle snuffed out beside the closed book; no sword, head, tray, blood or body"),
    dict(to=46, reason="sensitive magical moment: the 'speaking head' — shown only as the glowing closed book in a beam of light",
         chars=[], loc="yunan_hall_dark",
         visual="a big closed old book with a plain worn brown leather cover and no decoration lying flat on a low solid square wooden side table with four short straight legs (not a folding stand) in the middle of the marble floor, lit by a single shaft of golden light from a high window, a soft eerie golden glow and slow drifting sparkles rising from it like a voice; at the edges of the frame the astonished courtiers in the shadows stepping back with hands raised in amazement, small and blurred",
         camera="medium wide, slightly low angle, the book in a column of light in the upper two-thirds", amb="throne_hall",
         sens="violence", safe="the severed speaking head is never shown (bible rule 10): only the glowing closed book in a beam of light and the court's amazement"),
    dict(to=50, reason="action change: the king tries to read the book — the stuck pages are blank",
         chars=["king_yunan"], loc="yunan_hall_dark",
         visual="King Yunan seated on his throne holding the huge heavy book open across his knees, the pages completely blank and pale, lifting the corner of a stuck page with a fingertip raised near his lips, his face puzzled and impatient, leaning over the empty pages; a beam of pale golden light on him; the hall around him dim",
         camera="medium shot, eye level, the king's face and the open blank pages in the upper two-thirds", amb="throne_hall"),
    dict(to=53, reason="reveal: the pages are poisoned — close detail",
         chars=[], loc="yunan_hall_dark",
         visual="extreme close-up of the pages of the huge old book being turned by a royal hand with a gold ring, the pages blank and slightly stuck together, a faint sickly green shimmer and tiny green sparkles clinging to the paper and to the fingertip; no writing on the pages; dark purple velvet sleeve at the edge of the frame",
         camera="extreme close-up of the hand and pages, high angle", amb="throne_hall",
         sens="violence", safe="the poisoning is shown only as a faint green shimmer on blank pages; no suffering shown"),
    dict(to=55, reason="sensitive turning point: the king collapses — shown only as the fallen crown",
         chars=[], loc="yunan_hall_dark",
         visual="the king's gold crown has fallen and lies tilted on the polished marble floor at the foot of the dais beside the big old book lying closed on the floor, the beam of light now pale and cold, a dark shadow sweeping across the floor; no person visible",
         camera="low angle close on the floor, the crown and book in the middle third, rising columns behind", amb="throne_hall",
         sens="violence", safe="the king's agony, fall and death are never shown (bible rule 10): only the fallen crown beside the closed book; no body"),
    dict(to=57, reason="scene turning point: the end of King Yunan — the empty throne",
         chars=[], loc="yunan_hall_dark",
         visual="the golden throne stands empty on its marble dais in the silent grey hall, a purple velvet cushion askew, a snuffed candle beside it with a last wisp of smoke, cold grey-violet light, long shadows of the columns; no people",
         camera="wide shot, eye level, the empty throne in the upper two-thirds, the marble steps as a calm lower third", amb="throne_hall",
         sens="violence", safe="the deaths of Duban and the king are shown only as an empty throne and a snuffed candle"),
    dict(to=59, reason="scene change: dissolve out of the Yunan tale back to the fisherman at the sealed jar on the shore",
         chars=["fisherman"], loc="seashore", transition="dissolve",
         visual="the thin old fisherman stands on the sand beside a large sealed brass jar lying on its side, its lead stopper marked with a glowing abstract eight-petalled geometric rosette; he wags a stern finger down at the jar with a shrewd satisfied look, his cast net over his shoulder; the sea sparkling behind him",
         camera="medium wide, eye level, the fisherman and jar in the upper two-thirds, smooth wet sand as a calm lower third", amb="seashore_day"),
    dict(to=63, reason="action change: the trapped jinni weeps and begs; the fisherman considers",
         chars=["fisherman"], loc="seashore",
         visual="the old fisherman crouches beside the sealed brass jar on the sand, one hand thoughtfully stroking his grey beard, eyebrows raised in careful thought; from tiny gaps around the rosette-sealed stopper seep faint wisps of indigo-violet smoke shaped like falling teardrops and small pleading sparkles; the turquoise sea behind",
         camera="medium shot, slightly low angle, the fisherman's face upper third, the jar mid-frame", amb="seashore_day"),
    dict(to=65, reason="action change: the jinni swears by God's name; the fisherman lifts the lead stopper",
         chars=["fisherman"], loc="seashore",
         visual="the old fisherman kneels on the sand and carefully lifts the heavy lead stopper with the abstract eight-petalled rosette from the mouth of the brass jar with both hands, a cautious hopeful face; a soft pure golden light rises from inside the jar; the golden afternoon sea behind",
         camera="medium close-up, eye level, his face and the stopper in the upper two-thirds", amb="seashore_day",
         sens="other", safe="the oath by God's name is shown only as soft golden light; the seal is an abstract rosette without letters"),
    dict(to=68, reason="action change: black smoke bursts out, the giant jinni re-forms, kicks the jar into the sea and smiles",
         chars=["jar_jinni", "fisherman"], loc="seashore",
         visual="a colossal pillar of swirling indigo-black smoke has risen from the shore and formed the towering jinni of the jar, empty-handed, his midnight-purple robe closed and wrapped up to the neck over a high-collared long-sleeved dark inner tunic so his chest is completely covered, grinning down with blazing golden eyes and a broad friendly smile; far out to sea the brass jar splashes into the waves in a fountain of spray; the small old fisherman below has stumbled back onto the sand, arms raised in alarm; sparkles swirl in the smoke",
         camera="dramatic low angle from the sand, the jinni filling the upper two-thirds, the fisherman small in the lower middle", amb="seashore_day"),
    dict(to=70, reason="scene change: the journey over mountains and deserts to the lake",
         chars=["jar_jinni", "fisherman"], loc="journey",
         visual="the giant jinni glides ahead on his swirling indigo smoke tail across golden dunes, pointing an empty hand towards distant mountains; the small old fisherman trudges behind him with his net over his shoulder, shading his eyes; ahead between four tall rocky peaks a gleaming lake catches the sun",
         camera="wide sweeping vista, the figures in the middle, the dunes as a calm lower third", amb="desert_day"),
    dict(to=73, reason="scene change: the wondrous lake with fish of four colours; the jinni gives instructions",
         chars=["jar_jinni", "fisherman"], loc="lake",
         visual="the crystal-clear lake ringed by four mountains, in the clear water swim bright fish of four colours — white, red, blue and gold — glittering in the sunlight; the giant jinni hovers over the shore pointing to the water with an empty hand and instructing; the old fisherman stands at the water's edge holding his folded net, looking at the fish with wonder",
         camera="wide shot, slightly high angle, the jinni and fisherman in the upper half, the fish in the clear water below", amb="lake_mountains"),
    dict(to=75, reason="action change: the jinni vanishes into the ground; the fisherman casts and catches four fish",
         chars=["fisherman"], loc="lake",
         visual="the old fisherman casting his net in a wide circle over the crystal lake, four bright fish — white, red, blue and gold — leaping in the shimmering net; behind him on the stony shore a glowing crack in the ground is closing with a last swirl of indigo smoke and sparkles where the jinni vanished",
         camera="medium wide, eye level, the fisherman and the spreading net in the upper two-thirds, calm water as the lower third", amb="lake_mountains"),
    dict(to=77, reason="scene and character change: the Sultan receives the wondrous fish and pays 400 dinars",
         chars=["fish_sultan", "fisherman"], loc="sultan_hall",
         visual="the Sultan in sapphire blue leans down from his cushioned seat in amazement towards a large basin of water held up by the kneeling old fisherman, in which swim four bright fish of white, red, blue and gold; a servant in a plain robe at the side holds out a heavy pouch spilling gold coins towards the fisherman, who beams with joy",
         camera="medium wide, eye level, faces in the upper half, the marble floor as a calm lower third", amb="throne_hall"),
    dict(to=80, reason="scene change and magical turning point: in the palace kitchen the wall splits and the woman appears and questions the fish",
         chars=["wall_woman", "palace_cook"], loc="kitchen",
         visual="the whitewashed kitchen wall has split open with a glowing emerald crack, and through it steps the mysterious woman in an emerald gown with an emerald headscarf fully covering her hair and neck, holding out a slender green wand that glows towards the black iron frying pan on the fire where four fish lie sizzling and lift their heads to answer; far across the kitchen the plump cook in white cap and apron has backed away against the shelves, frozen in astonishment; emerald sparkles in the air",
         camera="medium wide, eye level, the woman in the upper left, the pan in the middle third", amb="palace_kitchen",
         sens="other", safe="the magic is fairy-tale sparkles only; the woman is fully covered and the cook stands far away"),
    dict(to=83, reason="scene change: dissolve back to the frame — dawn breaks, Shahrazad stops, the king spares her another day",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber_dawn", transition="dissolve",
         visual="rose-gold dawn light pours through the lattice window, a slender minaret silhouette against the pale golden sky; Shahrazad on her cushion has fallen silent with lowered eyes and a small knowing smile, hands folded in her lap; King Shahryar on the divan an arm's length away gazes at her with intense curiosity, raising a hand in a gesture granting another day; Dunyazad beside her sister yawns happily",
         camera="medium wide, eye level, the three faces and the window in the upper two-thirds, the carpet as a calm lower third", amb="palace_dawn"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Chapter Eight: The Fisherman's Cunning and the Tale of King Yunan (Part Two).")
sh(2, "When the following night's pre-dawn stillness had settled over the whole palace and the cool breezes of dawn began to blow from the east, Dunyazad called to her elder sister Shahrazad.",
   [("wind_gust", "ރޯޅިތައް", -24)])
sh(3, "\"Dear sister! If you are not asleep, tell us about the evil plot that King Yunan's wicked, envious vizier laid against Hakim Duban, and what happened because of it.")
sh(4, "My heart is very impatient to know what became of that fisherman and the jinni shut up in the jar.\"")
sh(5, "King Shahryar too was very eager to hear the rest of the tale, and he gave Shahrazad leave to continue.")
sh(6, "Shahrazad began with great courtesy: \"O noble, mighty King! I will continue the tale from where I stopped yesterday.")
sh(7, "In the heart of that wicked vizier at King Yunan's court, seeing the honour and respect the king was showing Hakim Duban, a great envy of Duban arose.")
sh(8, "What he plotted was to finish Hakim Duban by any means and to bring down his worth in the king's eyes. And so,")
sh(9, "one day, watching for a moment when the king sat alone, the vizier went secretly to the king and said: 'O noble King!",
   [("footsteps_pavement", "ގޮސް", -24)])
sh(10, "I always pray that your power and your reign may last. But to keep from you a great fear in my heart would go against my loyalty.")
sh(11, "This Hakim Duban, who is said to have cured you, is a great danger to your life.")
sh(12, "He is a spy sent by your enemies!' King Yunan said angrily: 'What are you saying?")
sh(13, "He is my greatest helper. He is the man who cured my terrible disease completely, without my drinking any medicine or rubbing anything on my body.")
sh(14, "When I am in his debt, why do you make such an accusation against him?")
sh(15, "Are you envious of him and trying to bring him down?' The vizier answered most cunningly: 'O noble King!")
sh(16, "Because your heart is so pure you cannot see the truth about that deceiver. Think about it!")
sh(17, "For a man who completely drove out your great illness with a stick held in your hand, how easy would it be to kill you with some other such thing, or with something fragrant?")
sh(18, "He came from another land to win your trust, then to kill you in secret and seize this kingdom.")
sh(19, "If you do not believe my words, you may very soon perish.' Hearing this wicked vizier's words again and again,")
sh(20, "the seed of doubt was planted in the king's heart. Fear surrounded his mind. The king said: 'If there is truth in what you say, I must kill him at once.",
   [("heartbeat", "ބިރުވެރިކަން", -20)], hum=True)
sh(21, "The only way to be safe from the harm he means to do me is to kill him.' At once the king ordered Hakim Duban to be brought to the palace.")
sh(22, "Duban came to the palace with a happy face, hoping for a great reward. But when he saw the king's angry face",
   [("footsteps_pavement", "އައީ", -22)])
sh(23, "and the armed guards all around, he realised something was wrong. The king said: 'O Duban!")
sh(24, "You came to me to win my trust and then to kill me. You are a spy.")
sh(25, "So today I have ordered your head to be cut off!' Hakim Duban, astonished and grieving, said: 'O King!",
   [("gasp", "ޙައިރާންވެ", -20)])
sh(26, "What kind of thing are you doing? I cured your illness and gave you a new life — is this the reward for that kindness?")
sh(27, "Do not kill me! If you spare me, God will spare you. If you kill me,", hum=True)
sh(28, "He will destroy you too!' But because of the poison the vizier had poured into the king's mind,")
sh(29, "there was no pity left in his heart for Duban. The king ordered the executioner to cut off his head at once.",
   [("heartbeat", "އަމުރުކުރެއްވީ", -18)], hum=True)
sh(30, "When Duban was certain he would not be saved, he sighed deeply and said to the king: 'O King!",
   [("sigh", "ނޭވާއެއްލައި", -20)])
sh(31, "Before you kill me, let me go home and bid my family farewell,")
sh(32, "and give me the chance to give away my precious books of medicine and my gifts to the people. And above all, the most precious,")
sh(33, "wondrous book I hold I wish to present to you. It is the book most fit to be kept in your royal treasury.'")
sh(34, "The king asked eagerly: 'What kind of book is it? What is special about it?'")
sh(35, "Duban answered: 'In that book are the greatest secrets of the world. And its greatest marvel is that after my head is cut off,")
sh(36, "if that head is placed on a tray and a certain page of the book is opened and you question my head,")
sh(37, "that severed head will speak to you and answer every question you ask!'")
sh(38, "Hearing this, the king was utterly amazed. A longing arose in his heart to see a severed head speak.")
sh(39, "So the king gave Duban one day's respite to go home and settle his affairs. The next day,")
sh(40, "the whole court was assembled. Hakim Duban came to the palace carrying an old heavy book, a small tray and some little medicine bottles.",
   [("footsteps_pavement", "އައެވެ", -22)])
sh(41, "He knelt before the king and set down the tray and the book. He said: 'O King! Here is the book.",
   [("soft_thud", "ބެހެއްޓިއެވެ", -22)])
sh(42, "After my head is cut off, place it on this tray. And to stop the blood flowing, rub a little of the medicine in this bottle on the cut.")
sh(43, "Then open this book and keep turning its pages, and question my head.'")
sh(44, "At the king's command the executioner stepped forward and struck off Hakim Duban's head. The head was placed on the tray at once.",
   [("crowd_gasp", "ބުރިކޮށްލިއެވެ", -18)], hum=True)
sh(45, "After the flowing blood had stopped, as everyone watched, like a wonder, that severed head opened its eyes and began to speak to the king!",
   [("magic_shimmer", "ހުޅުވައި", -18), ("crowd_gasp", "ވާހަކަދައްކަން", -20)])
sh(46, "The head said: 'O King! Open the book!' The king hurriedly took up the heavy book and tried to open its first page. But",
   [("page_turn", "ހުޅުއްވަން", -18)])
sh(47, "the pages of that book were stuck very tightly to one another. To separate the pages, the king")
sh(48, "put his finger to his mouth, wet it, and kept turning the pages. The first page,",
   [("page_turn", "އުއްތަވަމުން", -18)])
sh(49, "the second page and the third page he opened. But there was no writing on them at all. The king asked: 'O Duban!",
   [("page_turn", "ހުޅުއްވިއެވެ", -20)])
sh(50, "Nothing at all is written in here!' The head answered: 'O King! Keep turning. You will see very soon.'")
sh(51, "Again the king wet his finger and went on separating the pages. But what he did not know",
   [("page_turn", "ވަކިކުރައްވަމުން", -20)])
sh(52, "was that Hakim Duban had smeared every page of that book with a deadly, fast-acting poison!",
   [("heartbeat", "ވިހައެއް", -18)], hum=True)
sh(53, "As the king kept wetting his finger and turning the book, the poison entered his mouth and his body and spread into his blood.")
sh(54, "Suddenly darkness came before the king's eyes, and a pain beyond words arose throughout his body.",
   [("heartbeat", "އަނދިރިވެ", -16)], hum=True)
sh(55, "Trembling, he fell to the floor. At that moment Duban's head on the tray said in a stern voice: 'O tyrant King!",
   [("soft_thud", "ވެއްޓުނެވެ", -14)])
sh(56, "You killed me while I was doing you good. Today your end has come. This is the reward of tyranny!'")
sh(57, "Having said this, the head closed its eyes and died. And within a few seconds King Yunan too passed away from the power of the poison.", hum=True)
sh(58, "The fisherman said towards the jinni: 'O great jinni! Your case is the same. When you tried to kill me, I used my wits to shut you up in that jar.")
sh(59, "I saved you and you tried to kill me. Now you will never be saved from this jar!'")
sh(60, "The jinni, lying inside the jar, utterly miserable, began to weep and beg: 'O good fisherman! Forgive me!",
   [("sob_breath", "ރޮމުންރޮމުން", -20)], hum=True)
sh(61, "I swear to you: if you save me, I will do you no harm at all.")
sh(62, "And I will find you a treasure greater than any human has ever seen. Believe my words!' The fisherman stopped to think for a while.")
sh(63, "He said: 'Will you swear by the name of God and give your firm promise never to harm me?'")
sh(64, "The jinni at once swore by the name of God and made a solemn promise never to harm the fisherman and to make him rich.",
   [("magic_shimmer", "ހުވާކޮށް", -20)])
sh(65, "Trusting the jinni's oath, the fisherman very carefully removed the lead stopper. At once,",
   [("metal_lid", "ނައްޓުވާލިއެވެ", -16)])
sh(66, "a thick black smoke poured out of the jar and turned again into the form of that giant jinni. As soon as the jinni appeared,",
   [("smoke_whoosh", "ދުންގަނޑު", -14), ("magic_shimmer", "ބަދަލުވިއެވެ", -18)])
sh(67, "he kicked that brass jar and flung it into the sea. The fisherman was frightened. But",
   [("splash", "އެއްލާލިއެވެ", -14), ("gasp", "ބިރުގަތެވެ", -20)])
sh(68, "the jinni looked at the fisherman and smiled: 'O fisherman! Follow me. I will keep my promise.'")
sh(69, "The jinni led the fisherman across great mountains and burning deserts. At last",
   [("footsteps_sand", "ދަތުރުކުރިއެވެ", -22)])
sh(70, "they reached a most wondrous, beautiful lake in the middle of four mountains.")
sh(71, "The water of the lake was clear as crystal, and in it swam fish of four colours: white,")
sh(72, "red, blue and gold. The jinni said: 'O fisherman! Cast your net into this lake, and catch one fish of each colour,")
sh(73, "and take those fish to the king of this land. He will give you a great deal of money. And remember!")
sh(74, "Never cast your net in this lake more than once a day.' Having said this, the jinni split the ground open and vanished. The fisherman cast his net into the lake.",
   [("stone_scrape", "ފަޅާލާފައި", -16), ("net_cast", "އެއްލިއެވެ", -18)])
sh(75, "And on the very first cast he caught four fish of the four colours. Full of joy,",
   [("water_splash_small", "ބޭނުނެވެ", -20)])
sh(76, "he put the fish in a basin filled with water and went to the Sultan's palace. When the king saw these wondrous fish,",
   [("footsteps_pavement", "ދިޔައެވެ", -24)])
sh(77, "he was utterly astonished and gave the fisherman four hundred gold dinars. The fisherman bought everything his family needed and went home happily.")
sh(78, "But when they tried to fry the fish in the palace kitchen, the kitchen wall split open and a very beautiful woman appeared and asked the fish: 'O fish!",
   [("fire_crackle", "ތެއްލަން", -20), ("stone_scrape", "ފަޅާލާފައި", -14), ("magic_shimmer", "ފާޅުވެ", -18)])
sh(79, "Are you true to your covenant?' The fish answered: 'Yes!")
sh(80, "If you return, we return too.' Then the woman went into the wall and vanished, and",
   [("magic_shimmer", "ގެއްލުމާއެކު", -18)])
sh(81, "the fish in the frying pan burned black.\" As the tale reached this point, the light of dawn entered the room and the first rays of the sun appeared.")
sh(82, "Shahrazad stopped her tale at once. King Shahryar, wanting so much to know the secret of the four-coloured fish")
sh(83, "and the truth about the woman who appeared from the kitchen wall, spared Shahrazad's life once more for one more day.", hum=True)
SHOTS = S

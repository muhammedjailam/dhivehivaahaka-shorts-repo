"""Beat/shot plan for Inssafuge Magu episode 615 (used by plan_beats.py)."""

LOC = {
    "train": "inside a quiet Amtrak train carriage travelling from New York to Boston at dawn: rows of dark-blue seats, a large window with misty autumn countryside streaming past — trees and roads carpeted with golden-yellow leaves — and a small fold-down table in front of the window seat",
    "train_table": "the small fold-down table in front of a window seat of an Amtrak train at dawn, the misty autumn countryside with golden-yellow trees blurred outside the window",
    "study_memory": "a remembered moment: Judge Richard Brand's dark wood-panelled home study at night, a heavy desk with a warm desk lamp, shelves of law books, a stone side table, rain streaking the dark window",
    "cambridge_street": "a quiet street in Cambridge, Massachusetts: old red-brick buildings with white-framed windows, tall trees with golden-yellow autumn leaves, wet dark pavement with puddles full of fallen golden leaves",
    "harris_house": "the front of a big old 19th-century Victorian house in Cambridge: steep slate roof, a turret, tall bay windows, a wet stone front staircase up to a heavy wooden front door, plain yellow police tape with no lettering strung along the garden railings, wet golden leaves on the path",
    "house_door": "the open heavy wooden front door of the old Victorian house at the top of its wet stone steps, a dim wood-panelled entrance hall behind",
    "hallway": "the dim wood-panelled inner hallway of the old Victorian house: a dark wooden staircase, old picture frames with blank dark canvases, a worn runner rug, a doorway at the end glowing with warm lamp light",
    "library": "a large private library in the old Victorian house: four walls of tall dark wooden bookshelves packed with old history books and manuscripts, a big old wooden desk in the middle covered with scattered papers under a green-shaded brass lamp, a tall arched window with rain-streaked glass, a worn rug on dark floorboards",
    "photo_1998": "an old faded black-and-white photograph filling the frame, slightly worn paper edges: a group portrait taken in 1998 in front of an old stone college building",
    "library_smoke": "the same large private library filled with billowing thick black smoke, the tall arched window shattered, glass shards on the floorboards, bookshelves looming as dark shapes in the haze; outside the window only a grey daytime Cambridge garden in the rain — wet trees with golden-yellow leaves and the roofs of old red-brick houses, no skyscrapers, no city skyline, no night lights",
    "library_after": "the same large private library as the black smoke slowly thins to a grey haze, the tall arched window shattered and rain blowing in, papers scattered on the floor and the big desk; outside the window only a grey daytime Cambridge garden in the rain — wet trees with golden-yellow leaves and the roofs of old red-brick houses, no skyscrapers, no city skyline, no night lights",
}
MOOD = {
    "train": "early dawn, misty pale gold light through the window, soft grey shadows inside the carriage, quiet, sleepless and heavy",
    "train_table": "early dawn, misty pale gold light falling across the table, cool shadows, a faint crimson-amber glint on the coin, brooding",
    "study_memory": "night, warm amber desk-lamp light against near-black shadows, silver rain on the window, soft dreamlike blurred edges, frightened and tense",
    "cambridge_street": "grey overcast morning after rain, wet glossy pavement reflecting the sky, warm golden leaves as the only colour, quiet and cold",
    "harris_house": "grey overcast day, damp air, wet glossy stone and slate, golden leaves, plain yellow tape as a sharp accent, sombre",
    "house_door": "grey overcast daylight outside, dim warm light inside the hall, cool and guarded",
    "hallway": "dim interior, grey daylight from a side window, a warm lamp glow ahead, hushed and tense",
    "library": "dim grey daylight from the tall rain-streaked window and the warm amber glow of the green-shaded desk lamp, deep shadows between the bookshelves, grave and silent",
    "photo_1998": "faded black-and-white photograph, soft grain, slightly worn paper, a cold, secretive, ominous stillness",
    "library_smoke": "grey-black haze, cold white window light cutting through billowing smoke, the desk lamp a dim amber blur, chaotic and frightening",
    "library_after": "a thinning grey haze, cold grey daylight and silver rain at the broken window, the amber lamp glow returning, shaken and urgent",
}

ALEX = "Alex in his long black wool overcoat over a charcoal suit, white shirt and loosened slim dark tie"
SARAH = "Sarah in her long ash-grey ankle-length overcoat and black hijab fully covering her hair and neck"
GLOVE = "thin pale-blue latex gloves"
COIN = ("an ancient heavy bronze Roman coin with a laurel-crowned emperor's head in profile facing right and a worn, "
        "illegible rim inscription")
NOBODY = "the desk's black leather chair empty and turned away, no one sitting or lying at the desk"
PHOTO = ("a faded black-and-white photograph filling the whole frame: seven young American men in their early twenties in "
         "dark suits and ties standing in a row in front of an old stone college building, each with a small round "
         "coin-shaped pin on his lapel, smiling stiffly; the young man at the far right confident and sharp-featured, the "
         "one beside him with a slight gentle smile, a tall self-assured young man in the middle; the face of one young "
         "man is completely scraped away into a rough pale blank scratched patch; a little apart, behind the group, a "
         "young woman in a long loose modest dress with a headscarf fully covering her hair and neck, standing quietly; "
         "soft photographic grain, worn paper edges, no caption, no text")

BEATS = [
    dict(to=2, reason="episode opening: dawn on the Amtrak to Boston — Alex sits sleepless by the window", chars=["alex"], loc="train",
         visual=f"{ALEX}, sitting by the large window of the quiet train carriage at dawn, leaning back with his head resting against the seat and his arms folded, but wide awake: tired, sleepless grey eyes staring ahead; behind him through the window misty countryside streams by — autumn trees and roads carpeted with golden-yellow leaves in pale gold mist",
         camera="medium shot from across the aisle, eye level, Alex's face in the upper half by the window, the seat back and small table as the lower third",
         amb="train_dawn"),
    dict(to=5, reason="detail: the coin in its evidence bag and the fax sheet on the little table; the fax words repeating like the wheels", chars=["alex"], loc="train_table",
         visual=f"close shot of the small fold-down table in front of Alex's train seat: a clear plastic evidence bag holding {COIN}, lying beside a single white fax sheet with only a few blurred, faint, unreadable dark lines; Alex's hands resting at the edge of the table, the sleeve of his long black overcoat; pale gold dawn light from the window, misty golden autumn trees blurred outside",
         camera="close shot, slightly high angle, the coin and the sheet in the upper two-thirds, the plain dark table edge as the lower third",
         amb="train_dawn", sens="other", safe="the fax text is a few blurred unreadable lines; the coin inscription illegible"),
    dict(to=7, reason="remembered moment: his father's frightened call last night, the phone switched off ever since", chars=["richard"], loc="study_memory", transition="dissolve",
         visual="Judge Richard Brand alone at night in his dark wood-panelled home study, sitting at his heavy desk under a warm desk lamp with a phone pressed to his ear, his face frightened and tense, grey eyes wide, his free hand gripping the desk edge; law books on the shelves behind, rain streaking the dark window, an intact crystal glass of water on a stone side table; soft dreamlike blurred edges",
         camera="medium close-up, eye level, his face and the phone in the upper half, the polished desk top as the lower third",
         amb="memory", sens="other", safe="Richard shown alive and frightened on the phone only — never hurt"),
    dict(to=9, reason="return to Alex on the train as he recalls the urgent message from the FBI Boston field office", chars=["alex"], loc="train",
         reuse="beat_001", amb="train_dawn", visual="(reuse of beat_001)", transition="dissolve"),
    dict(to=11, reason="time/place jump: South Station, then Alex striding into Cambridge's old red-brick streets with wet golden leaves", chars=["alex"], loc="cambridge_street", transition="black",
         visual=f"{ALEX}, walking briskly towards the camera along a quiet Cambridge street of old red-brick buildings, his long coat open and swinging with his stride, his face set and focused; wet dark pavement and puddles full of fallen golden-yellow leaves, tall trees with yellow leaves above, grey overcast sky; no church spires, no crosses, no signs",
         camera="medium-wide, eye level, Alex in the upper-middle, the wet leaf-strewn pavement as the lower third",
         amb="rain_day"),
    dict(to=13, reason="scene change: the big Victorian house with police tape; an officer stops Alex at the door", chars=["alex"], loc="harris_house",
         visual=f"the big old 19th-century Victorian house with a steep slate roof, a turret and tall bay windows, plain yellow police tape with no lettering strung along the front railings; {ALEX}, seen from behind and the side, climbing the wet stone front steps towards the heavy front door, where a uniformed police officer in a plain dark-blue uniform (no badges, no lettering, no weapon, no belt gear) raises one hand to stop him; wet golden leaves on the steps, grey overcast sky",
         camera="wide low-angle shot from the garden path, the house, door and the two men in the upper two-thirds, the wet leaf-covered path as the lower third",
         amb="rain_day", sens="other", safe="police tape plain with no lettering; officer with no badge text or weapon; Alex's badge not shown"),
    dict(to=17, reason="character introduced: Detective Sarah Allison comes out, hands in her coat pockets, and introduces herself (speaker)", chars=["sarah", "alex"], loc="house_door", speaker="sarah",
         visual=f"{SARAH}, standing tall in the open front doorway of the old house with her hands deep in her coat pockets, speaking with a cool, appraising look, sharp intense dark eyes; in the soft-focus foreground at the side, Alex's shoulder and the back of his head in his black overcoat, a respectful distance between them; the dim panelled hall behind her",
         camera="over-the-shoulder medium shot, Sarah centred and sharp in the upper half, Alex blurred at the side, the wet stone landing as the lower third",
         amb="rain_day", sens="intimacy", safe="the handshake is not shown: Sarah keeps her hands in her pockets; a respectful nod at a distance"),
    dict(to=19, reason="action change: Sarah leads him inside, talking over her shoulder about his record and her doubts", chars=["sarah", "alex"], loc="hallway", speaker="sarah",
         visual=f"{SARAH}, walking ahead down the dim wood-panelled hallway and glancing back over her shoulder while speaking, hands in her coat pockets, a sceptical half-frown; {ALEX}, following a few steps behind, attentive; a dark staircase at the side, a doorway at the end glowing with warm lamp light",
         camera="medium shot, eye level, Sarah's face centred in the upper half, Alex soft behind, the runner rug as the lower third",
         amb="library_rain_day"),
    dict(to=22, reason="scene change: the big library where the professor lies dead (never shown) — they enter", chars=["alex", "sarah"], loc="library",
         visual=f"wide view of the large private library from its doorway: four walls of tall dark bookshelves packed with old books and manuscripts, the big old wooden desk in the middle under the green-shaded lamp, covered with scattered papers, {NOBODY}; the tall arched rain-streaked window with grey daylight; {ALEX} and {SARAH}, standing just inside the doorway at the side in the foreground, a clear distance apart, looking towards the desk with grave faces; a small plain forensic marker cone with no numbers on the rug",
         camera="wide shot, eye level, the desk, window and the two figures in the upper two-thirds, the dark floorboards and rug as the lower third",
         amb="library_rain_day", sens="violence", safe="the professor's body is never shown: an empty chair turned away, papers, the lamp, rain on glass"),
    dict(to=24, reason="detail/action: Alex pulls on gloves beside the desk; the overturned cup; he looks at the professor's hand (below frame)", chars=["alex"], loc="library",
         visual=f"close shot beside the big library desk: Alex pulling a {GLOVE.rstrip('s')} tight onto his hand, his eyes lowered with sharp focus towards something just below the frame at the desk's edge; on the desk top in the foreground an overturned white porcelain teacup lying on its saucer among scattered papers, the green-shaded lamp glowing warm",
         camera="close medium shot, eye level, Alex's face and gloved hands in the upper half, the desk top with the overturned teacup as the lower third",
         amb="library_rain_day", sens="other", safe="the foam, the open dead hand and the empty whisky glass are not shown: an overturned porcelain teacup, Alex's lowered gaze"),
    dict(to=26, reason="speaker change: Sarah stops by the desk, folds her arms — 'cyanide suicide, a lonely man'", chars=["sarah", "alex"], loc="library", speaker="sarah",
         visual=f"{SARAH}, standing beside the big library desk with her arms folded, speaking with a blunt, matter-of-fact expression, chin raised; the green-shaded lamp and scattered papers beside her, bookshelves behind; Alex soft and blurred at the edge of the frame in his black overcoat",
         camera="medium shot, eye level, Sarah centred and sharp in the upper half, the desk top as the lower third",
         amb="library_rain_day"),
    dict(to=28, reason="reverse shot: Alex answers and points to the white sheet with shaky Latin letters", chars=["alex", "sarah"], loc="library", speaker="alex", transition="cut",
         visual=f"{ALEX} and {GLOVE}, leaning over the big library desk and speaking quietly with a sharp, focused gaze, one gloved finger pointing at a single white sheet of paper on the desk covered only with faint shaky illegible pen marks, no readable letters; scattered papers and the overturned teacup at the side, warm lamp light on his face; Sarah soft in the background",
         camera="medium close-up, slightly low angle, Alex's face centred in the upper half, the desk top with the sheet as the lower third",
         amb="library_rain_day", sens="other", safe="the Latin scrawl is faint illegible marks; the professor beside it is not shown"),
    dict(to=30, reason="action change: Alex searches the professor's coat pocket (below frame) and finds something heavy and round; Sarah's eyes widen", chars=["alex", "sarah"], loc="library",
         visual=f"Alex crouched on one knee at the side of the big library desk in his black overcoat, looking down at something below the frame, his pale-blue gloved hand rising from below holding a small heavy round dark object; {SARAH} standing behind him at a distance, her eyes widening in surprise; lamp light, bookshelves behind",
         camera="medium shot, eye level, Alex's face, the object and Sarah in the upper two-thirds, the dark floorboards as the lower third",
         amb="library_rain_day", sens="violence", safe="turning the body and searching the coat are kept below frame: only Alex's lowered gaze and gloved hand"),
    dict(to=32, reason="reveal: an identical Roman coin, 'Mors omnia solvit'", chars=["alex"], loc="library",
         visual=f"extreme close-up of Alex's pale-blue latex-gloved fingers holding up {COIN} against the warm lamp light, the metal gleaming bronze-gold with crimson and amber reflections; the dark library and bookshelves softly blurred behind; no readable letters",
         camera="extreme close-up, the coin in the upper half, the blurred dark desk as the lower third",
         amb="library_rain_day", sens="other", safe="the coin's Latin inscription is worn and illegible"),
    dict(to=35, reason="speaker: Alex lifts the coin into the light — the second death, one killer, same night", chars=["alex", "sarah"], loc="library", speaker="alex",
         visual=f"{ALEX} and {GLOVE}, standing by the library desk raising the bronze Roman coin between his gloved fingers into the warm lamp light, studying it while speaking with cold certainty, grey eyes narrowed; {SARAH} at the side in soft focus, serious, a little apart, glancing towards the bookshelves",
         camera="medium close-up, eye level, Alex's face and the raised coin centred in the upper half, the desk top as the lower third",
         amb="library_rain_day"),
    dict(to=37, reason="reverse shot: Sarah on Harris's past — Harvard since the 1990s, secret societies", chars=["sarah", "alex"], loc="library",
         reuse="beat_011", amb="library_rain_day", visual="(reuse of beat_011)", transition="cut"),
    dict(to=38, reason="reverse shot: Alex — 'we have to find the link, their past'", chars=["alex", "sarah"], loc="library",
         reuse="beat_015", amb="library_rain_day", visual="(reuse of beat_015)", transition="cut"),
    dict(to=40, reason="action change: Sarah searches the drawers and pulls out a dusty yearbook", chars=["sarah", "alex"], loc="library", speaker="sarah",
         visual=f"{SARAH}, bent over the big library desk pulling a heavy dusty old yearbook with a plain dark cloth cover (no lettering) out of an open wooden drawer, a puff of dust glowing in the lamp light, speaking with sudden urgency; Alex beside the desk at a distance, watching",
         camera="medium shot, eye level, Sarah's face and the book in the upper half, the desk front and drawer as the lower third",
         amb="library_rain_day"),
    dict(to=42, reason="action change: Alex flips the 1998 yearbook's pages and stops at the secret-clubs section", chars=["alex", "sarah"], loc="library",
         visual="close shot over the big library desk: Alex's pale-blue gloved hands quickly flipping the thick yellowed pages of an open old yearbook, the pages showing only blurred small black-and-white photos and faint grey lines, no readable text; one hand stopping flat on a page; Sarah in her ash-grey coat and black hijab leaning in at the side a little apart, soft; warm lamp light",
         camera="close shot, high angle, the hands and pages in the upper two-thirds, the dark desk wood as the lower third",
         amb="library_rain_day", sens="other", safe="yearbook pages have no readable text"),
    dict(to=46, reason="reveal: the 1998 photo of seven young men with Roman-coin pins, one face scratched out", loc="photo_1998", transition="dissolve",
         visual=PHOTO,
         camera="full-frame photograph, the group in the upper two-thirds, the plain lower border of the photo as the lower third",
         amb="memory", sens="other", safe="the dead men appear only young and alive in the photo; the scratched face is a pale blank patch; no caption text"),
    dict(to=48, reason="return from the photo: Alex and Sarah over the yearbook — six members, two dead, five left", chars=["alex", "sarah"], loc="library", speaker="alex", transition="dissolve",
         visual=f"{ALEX} and {SARAH}, standing side by side but a clear distance apart over the open old yearbook on the library desk under the warm lamp, both looking down at it; Alex speaking quietly with a tense face, Sarah staring intently at the page",
         camera="medium shot from across the desk, eye level, both faces in the upper half, the open book on the desk as the lower third",
         amb="library_rain_day"),
    dict(to=50, reason="emotional turning point: Sarah turns pale and points with a trembling finger — Senator William Hastings", chars=["sarah"], loc="library", speaker="sarah",
         visual=f"close-up of {SARAH}, bending over the open yearbook on the desk, her face suddenly pale, eyes narrowed with grief and anger, lips pressed, breath held; her trembling index finger pointing down at a photo on the page; warm lamp light from the side",
         camera="close-up, eye level, her face in the upper half, the finger and the page edge as the lower third",
         amb="library_rain_day", transition="cut"),
    dict(to=51, reason="return to the photo: the man in the middle is Hastings", loc="photo_1998",
         reuse="beat_020", amb="memory", visual="(reuse of beat_020)", transition="dissolve"),
    dict(to=52, reason="return to Sarah: grief and anger in her eyes", chars=["sarah"], loc="library",
         reuse="beat_022", amb="library_rain_day", visual="(reuse of beat_022)", transition="dissolve"),
    dict(to=54, reason="detail of the photo: the young woman standing a little apart behind the men — Emily Ward", loc="photo_1998", transition="dissolve",
         visual="close detail of the same faded black-and-white photograph: behind the dark-suited shoulders of the young men (blurred in the foreground), a young woman of about twenty in a long loose modest dress with a headscarf fully covering her hair and neck, standing a little apart, a quiet, shy, uncertain expression; photographic grain, worn paper edge; no text",
         camera="close detail framing, the young woman's face in the upper half, the blurred shoulders and the photo's lower edge as the lower third",
         amb="memory", sens="other", safe="Emily appears only inside the photo, fully covered"),
    dict(to=56, reason="return to Sarah as she tells how Emily vanished in 1998 and the case was closed", chars=["sarah"], loc="library",
         reuse="beat_022", amb="library_rain_day", visual="(reuse of beat_022)", transition="dissolve"),
    dict(to=57, reason="emotional turning point: the pieces connect in Alex's mind", chars=["alex"], loc="library",
         visual=f"close-up of {ALEX}, standing near the tall arched library window in dim grey daylight, deep in thought, grey eyes narrowed and distant, jaw tight; rain streaming down the glass beside him, a faint amber reflection of the lamp; bookshelves blurred behind",
         camera="close-up, eye level, his face in the upper half, the dark window sill as the lower third",
         amb="library_rain_day", transition="cut"),
    dict(to=58, reason="shock action: the library's big window shatters as something is thrown in", loc="library", transition="cut",
         visual="the tall arched library window bursting inward, its rain-streaked glass shattering into a spray of glittering shards against the grey daylight, a puff of dark smoke at the break; bookshelves of old books at both sides; no people, nothing in anyone's hand",
         camera="medium-wide, eye level, the bursting window in the upper two-thirds, the dark floorboards with first falling shards as the lower third",
         amb="library_rain_day", sens="violence", safe="the smoke bomb is shown only as shattering glass and a puff of smoke; no device or thrower"),
    dict(to=60, reason="action change: both drop to the floor as thick black smoke fills the library", chars=["alex", "sarah"], loc="library_smoke",
         visual=f"inside the library, {ALEX} and {SARAH}, both crouched low on the floorboards beside the big desk at a clear distance from each other, arms raised to shield their faces, glittering shards of window glass falling between them, thick black smoke billowing in across the floor from the shattered window; not touching",
         camera="medium-wide, low angle, both crouched figures in the upper two-thirds, the floorboards and creeping smoke as the lower third",
         amb="smoke_room", sens="intimacy", safe="'Alex pulls Sarah down' = both drop to the floor a clear distance apart; no touching"),
    dict(to=61, reason="character enters: a dark figure jumps in through the window into the smoke", chars=["masked_killer"], loc="library_smoke",
         visual="billowing black smoke filling the library, cold white light from the shattered tall window; a tall dark hooded figure crouching on the floorboards just inside below the broken window, having just landed, its shape half-hidden in the smoke, only the glint of his eyes above a black cloth mask; glass shards on the floor; empty gloved hands",
         camera="medium-wide, eye level, the window and the crouching figure in the upper two-thirds, the smoky floor as the lower third",
         amb="smoke_room", sens="violence", safe="Alex drawing his pistol is not shown; only the intruder's silhouette, empty-handed"),
    dict(to=63, reason="action/speaker change: Sarah shouts 'Stop!' from the floor; a bookshelf splinters in the smoke; Alex rises", chars=["sarah", "alex"], loc="library_smoke", speaker="sarah",
         visual=f"{SARAH}, low on the floorboards behind the big desk, propped on one elbow, shouting fiercely with her mouth open, her empty hand raised palm-out towards the smoke; in the smoke behind, a wooden bookshelf with a fresh splintered gash, splinters and old books tumbling; Alex rising to one knee at the far side, staring hard into the smoke, hands empty",
         camera="medium shot, low angle, Sarah's face centred in the upper half, the smoky floorboards as the lower third",
         amb="smoke_room", sens="violence", safe="no guns: the shot is only a splintered bookshelf; Sarah's and Alex's hands are empty; sound is a muffled thud, no gunshot"),
    dict(to=65, reason="action change: the masked figure has come for the yearbook and snatches it from the desk", chars=["masked_killer"], loc="library_smoke",
         visual="in the swirling black smoke of the library, the tall masked figure in a black hooded coat leaning over the big desk and snatching up the heavy old yearbook in his black-gloved hands, his dark eyes above the black mask hard and focused; papers flying off the desk; grey light from the broken window behind",
         camera="medium shot, eye level, the masked figure's eyes and the book in the upper half, the cluttered desk top as the lower third",
         amb="smoke_room", sens="violence", safe="Alex grabbing the coat is not shown"),
    dict(to=67, reason="action change: after a fast struggle (not shown) Alex is thrown back against the desk; the figure heads for the window", chars=["alex", "masked_killer"], loc="library_smoke",
         visual=f"inside the black smoke, {ALEX}, half-fallen backwards against the edge of the big desk, one hand pressed to his chest, catching his breath, his face strained; a few metres beyond, the dark hooded figure, blurred in the smoke, moving away towards the shattered window with a book under his arm; a clear distance between them, nobody touching",
         camera="medium shot, eye level, Alex's face in the upper half with the distant figure behind, the desk edge and smoky floor as the lower third",
         amb="smoke_room", sens="violence", safe="the fight (grab, arm twist, elbow) is never shown: only the aftermath — Alex against the desk catching his breath, the figure at a distance"),
    dict(to=70, reason="speaker: at the window the masked figure turns — 'The third will die tonight! Give my regards to your father!' — and jumps", chars=["masked_killer"], loc="library_smoke", speaker="masked_killer",
         visual="the masked figure standing at the shattered tall library window with one foot on the sill, turning back over his shoulder towards the viewer, hood up, black cloth mask below the eyes, his dark eyes burning with deep fury; the old yearbook clutched under one arm, his other gloved hand empty; grey rain outside, black smoke swirling around him",
         camera="medium close-up, eye level, his eyes centred in the upper half, the window sill and smoke as the lower third",
         amb="smoke_room"),
    dict(to=71, reason="action change: the smoke clears; Alex gets up coughing; Sarah at the window — the figure has vanished into the rain", chars=["sarah", "alex"], loc="library_after",
         visual=f"the library with the smoke thinning to a grey haze: {SARAH}, standing at the shattered tall window with her back half-turned, looking out into the pouring rain, cold air blowing in; {ALEX}, in the foreground at the side, getting up from the floor, coughing into his fist",
         camera="medium-wide, eye level, Sarah at the window and Alex in the upper two-thirds, the glass-strewn floorboards as the lower third",
         amb="smoke_room"),
    dict(to=74, reason="detail: the yearbook is gone, but a torn page is left in Alex's hand — the third name is Hastings", chars=["alex"], loc="library_after",
         visual=f"close-up of Alex holding up a single torn yellowed page from an old book, a list shown only as rows of blurred faint grey lines, no letters, a ragged ripped edge; his serious face above it, grey eyes narrowed; behind him in soft focus the empty desk with scattered papers and a fading haze",
         camera="close-up, eye level, his face and the page in the upper two-thirds, the blurred desk as the lower third",
         amb="library_rain_day", sens="other", safe="the list of names is blurred lines with no letters"),
    dict(to=75, reason="speaker change: Sarah comes up to Alex — 'It's Hastings!' — as he straightens his coat", chars=["sarah", "alex"], loc="library_after", speaker="sarah",
         visual=f"{SARAH}, standing in front of Alex at a respectful distance in the hazy library, speaking urgently, eyes intense; {ALEX}, at the side straightening the collar of his long black overcoat, jaw set; the broken window grey behind",
         camera="over-the-shoulder medium shot, Sarah centred and sharp in the upper half, Alex at the side, the floorboards as the lower third",
         amb="library_rain_day", sens="violence", safe="Alex holstering his pistol is shown only as him straightening his coat"),
    dict(to=77, reason="scene change: the two hurry out into the rain to save the third target", chars=["alex", "sarah"], loc="harris_house",
         visual=f"{ALEX} and {SARAH}, hurrying side by side but apart down the wet stone front steps of the big old Victorian house into the pouring rain, determined faces, Alex's coat wet; plain yellow police tape (no lettering) fluttering, wet golden leaves on the path, grey late-afternoon light",
         camera="medium-wide, slightly low angle, both figures in the upper two-thirds, the wet leaf-strewn path as the lower third",
         amb="rain_day"),
    dict(to=78, reason="closing question: what was scratched out of that photo?", loc="photo_1998",
         reuse="beat_020", amb="memory", visual="(reuse of beat_020)", transition="dissolve"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Through the window of the Amtrak train travelling from New York to Boston, the sleepy mist of dawn and roads carpeted with pale golden leaves went streaming past outside.")
sh(2, "Alex Brand sat in the train seat with his head resting back, yet there was not a trace of sleep in his eyes.")
sh(3, "On the small table in front of him lay that heavy Roman coin sealed in a plastic bag, and the fax sheet found at the New York office.",
   [("paper_shuffle", "ކަރުދާސްކޮޅު", -24)])
sh(4, "\"The first step has been taken. Six remain. The sins of 1998 will not be hidden by buried bones.\"",
   hum=True)
sh(5, "These words were fixed in his mind, never stopping, like the sound of the train's iron wheels striking the track.")
sh(6, "Last night, after the call from his father, Judge Richard Brand, was cut off, he had tried many times to call his father. But his father's phone was switched off.",
   [("dial_tone", "ނިއްވާލާފަ", -22)], hum=True)
sh(7, "What could be the reason for the fear in his father's voice? What happened in 1998?",
   hum=True)
sh(8, "Alex had to head for Boston before he had even finished with the New York crime scene, because of an urgent message from the FBI's Boston field office.",
   [("phone_buzz", "މެސެޖަކާ", -20)])
sh(9, "Another death just like it had been found near the campus of Boston's famous Harvard University. The dead man is Professor Edward Harris, a professor specialising in history and ancient civilisations.")
sh(10, "As the train stopped at Boston's South Station, Alex stepped out with quick strides and headed towards the quiet, old red buildings of Cambridge.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -20)])
sh(11, "The mark of the rain lay heavy on this city too. The yellow leaves fallen on the streets lay soaked and swollen in the puddles.",
   [("leaves_rustle", "ފަތްތައް", -24)])
sh(12, "The house where it happened was a big, old house from the nineteenth-century Victorian era. Yellow police tape had been strung all around the house.")
sh(13, "Climbing the steps, Alex was stopped by a policeman standing guard at the door. When Alex showed his FBI badge, out from inside came a tall woman with jet-black hair and sharp eyes.",
   [("footsteps_pavement", "ސިޑިން", -20), ("door_open", "ނުކުމެގެން", -20)])
sh(14, "Standing with her hands thrust into the pockets of the ash-coloured overcoat she wore, the woman had a face that showed a strong personality. \"Alex Brand?\"",
   speaker="sarah")
sh(15, "she asked. In her voice was a local Boston accent. \"I'm Detective Sarah Allison, Boston Police Homicide.\"",
   speaker="sarah")
sh(16, "\"I haven't laid a hand on anything here until you got here from New York.\" \"Thank you, Detective.\" Alex greeted her.",
   speaker="sarah")
sh(17, "From the firmness of Sarah's grip, Alex knew at once that she was a cop who doesn't back down, who knows the truths of the street.",
   crop="medium")
sh(18, "\"I've looked at your record,\" Sarah said as she started walking inside. \"The FBI's best pattern analyst.\"",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -22)], speaker="sarah")
sh(19, "\"But I don't believe there's any link between a New York banker dying and an old professor here dying.\"",
   speaker="sarah")
sh(20, "\"The man's lying dead inside his own library — it looks like he took poison.\" They went into the big library deep inside the house.",
   [("door_open", "ވަދެގެން", -20)])
sh(21, "The four walls of the room are filled with history books and ancient writings. In the middle of the room stood")
sh(22, "a big desk, and on it, fallen across a pile of papers, lay the body of Professor Harris, about sixty years old.",
   hum=True)
sh(23, "Foam had come from his mouth and dried. On the desk stood an expensive scotch whisky glass, empty. Alex stepped forward, pulling on his gloves.",
   [("cloth_rustle", "އަންގި", -22)])
sh(24, "The first thing he looked at was the professor's hand. But the hand lay open. It was not clenched like Victor Vance's.")
sh(25, "Sarah stopped beside the desk and folded her arms. \"See? Didn't I tell you — this is a man who killed himself by drinking cyanide! He has no family.\"",
   speaker="sarah")
sh(26, "\"Something done out of loneliness and despair.\" \"When lonely people kill themselves,", speaker="sarah")
sh(27, "they don't write historical phrases on the desk at the last moment,\" Alex said. His gaze stopped on a white sheet of paper lying near the professor's head.",
   [("paper_shuffle", "ކަރުދާސްގަނޑަކަށް", -24)], speaker="alex")
sh(28, "On it were some letters written in Latin with a faint tremor — signs showing they had been written with great effort as his breath was running out.",
   hum=True)
sh(29, "Alex slowly turned the body to the other side, and began to check the pockets of the tweed coat the professor was wearing.",
   [("cloth_rustle", "ޖީބުތައް", -22)])
sh(30, "From inside the left pocket his hand touched something heavy and round. Alex took it out. Sarah's eyes went wide.",
   [("coin_clink", "ނެގި", -18)], hum=True)
sh(31, "It was an ancient Roman coin exactly like the one found in New York. On one side was the same emblem of the face and the olive crown.",
   hum=True)
sh(32, "On the other side, the same Latin words: Mors omnia solvit. \"This... what is this?\"")
sh(33, "The hardness in Sarah's voice broke, and seriousness took over. \"This is the mark of a second death.\"")
sh(34, "Alex said, raising the coin into the light. \"Victor Vance died in New York at nine at night. Professor Harris died the same night, at two in the morning.\"",
   [("coin_clink", "ހިއްލައިލަމުން", -22)], speaker="alex")
sh(35, "\"This is in no way a coincidence. This is the handiwork of one killer.\" Sarah let out a deep breath. She looked towards the bookshelves.",
   [("sigh", "ނޭވާއެއް", -22)], speaker="alex")
sh(36, "\"Harris has been teaching at Harvard since the 1990s.\"", speaker="sarah")
sh(37, "\"He's an expert on ancient secret societies. Why would anyone want revenge on him?\"", speaker="sarah")
sh(38, "Alex thought for a moment. \"We have to find what link there is between Victor Vance and Edward Harris. Their past,\"",
   speaker="alex")
sh(39, "\"their younger days.\" As if she had suddenly remembered something, Sarah began to search the desk's drawers. \"Wait!\"",
   [("creak", "ވަތްގަނޑުތައް", -20)], speaker="sarah")
sh(40, "\"Harris's diaries and yearbooks will be here!\" Sarah took out a big yearbook thick with dust and set it on the desk.",
   [("soft_thud", "ބޭއްވި", -18)], speaker="sarah")
sh(41, "It was the Harvard University students' album of 1998. Alex quickly began to turn its pages.",
   [("page_turn", "އުކަން", -20)])
sh(42, "When he reached the section in the middle of the book dedicated to secret clubs and societies, his hand stopped. On that page was a black-and-white",
   [("page_turn", "ދެވުމާއެކު", -22)], hum=True)
sh(43, "photo taken of seven young men together. All of them wore suits, with a badge shaped like a Roman coin pinned to their chests.",
   hum=True)
sh(44, "Written under the photo was \"The Seventh Senate 1998\" — the Seventh Senate. Standing at the far right of the photo was a young Victor Vance.")
sh(45, "Beside him, smiling a little, stood a young Professor Harris. Another man's face cannot be seen.",
   hum=True)
sh(46, "That face had been scratched off the photo with something and completely erased. \"Here they are.\" As Sarah said this, Alex's heart began to race.",
   [("heartbeat", "ތެޅުން", -20)], hum=True)
sh(47, "\"They studied together — members of one secret club. In 1998 there were six members in this club.\"", speaker="alex")
sh(48, "\"Now two of them have died. Five are left.\" Sarah looked deeply at the photo.", speaker="alex")
sh(49, "Suddenly the colour of her face changed. Her eyes narrowed, as if she were holding her breath. \"Sarah? What's wrong?\" Alex asked.",
   [("gasp", "ހިފަހައްޓައިލި", -20)], hum=True)
sh(50, "Sarah pointed with a trembling finger at another man in the middle of the photo. \"This man... this is Senator William Hastings.\"",
   speaker="sarah", hum=True)
sh(51, "\"He's a popular political leader now. And beside him, here, is...\" Sarah stopped.")
sh(52, "What showed in her eyes was more grief and anger than fear. \"Who?\" Alex asked. \"In this photo,",
   hum=True)
sh(53, "the young girl you can see a little way behind these men...\" Sarah said quietly.", hum=True)
sh(54, "\"That's Emily Ward. She was our neighbour when I was little.\"", hum=True)
sh(55, "\"In late 1998 she suddenly disappeared while she was studying at Harvard. There was no news at all.\"",
   speaker="sarah", hum=True)
sh(56, "\"The police said she ran away on her own. They filed the case and closed it. But she never came back.\"",
   speaker="sarah", hum=True)
sh(57, "Things began to connect in Alex's mind. A secret club from 1998, a missing girl, and a killer murdering the club's members one after another.",
   hum=True)
sh(58, "The killer wants justice. But it is not legal justice. It is the dark justice of blood for blood. At that very moment, smashing the glass of the library's big window, a small black metal object came flying in.",
   [("glass_break", "ފޫއަޅުވާލާފައި", -12)], hum=True)
sh(59, "\"Down!\" Alex shouted, pulling Sarah down. As the two dropped to the floor, thick smoke began to pour out of it.",
   [("soft_thud", "ތިރިވި", -18), ("smoke_whoosh", "ދުންތަކެއް", -16)], hum=True)
sh(60, "It was a smoke bomb. In a moment the whole library was filled with thick black smoke; it became hard to breathe, and nothing could be seen.",
   [("smoke_whoosh", "ފުރި", -20)])
sh(61, "Coughing, eyes narrowed, Alex drew his pistol. Through the smoke came the sound of soft footsteps — the sound of someone jumping in through the window.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގެ", -20), ("soft_thud", "ފުންމާލި", -18)], hum=True)
sh(62, "\"Stop!\" Sarah shouted from where she lay on the floor, and fired towards the sound. The bullet struck a wooden bookshelf.",
   [("soft_thud", "ބަޑި", -20), ("crash_clatter", "ފޮތްހަރުގަނޑެއްގަ", -16)], speaker="sarah")
sh(63, "Alex got up and aimed at a faint shadow showing through the smoke.",
   [("heartbeat", "ހިޔަންޏަކާ", -20)], hum=True)
sh(64, "But the shadow's aim was not them. The figure had come to take the 1998 yearbook lying on the desk.")
sh(65, "Dressed in black, face covered, the figure snatched up the book with great skill. Alex rushed forward and caught hold of the figure's coat.",
   [("paper_shuffle", "ޖަހައިގަތް", -18), ("footsteps_pavement", "ދުއްވައިގަނެ", -20)])
sh(66, "A fierce struggle broke out between the two. The figure's movements were very strong and fast, like someone with military training.",
   [("cloth_rustle", "ކުރިމަތިލުމެއް", -18), ("breath_heavy", "ހަލުވިކޮށް", -20)], hum=True)
sh(67, "After grabbing and twisting Alex's arm, he struck a hard blow to his chest with an elbow. Alex was thrown backwards and hit the desk. The figure ran towards the window.",
   [("soft_thud", "ހަމަލާއެއް", -18), ("crash_clatter", "ޖެހުނު", -18), ("breath_heavy", "ދުއްވައިގަތް", -22)], hum=True)
sh(68, "Before jumping through, he turned and looked at Alex. In his eyes, showing above the black mask, was a deep, dark fury.",
   [("heartbeat", "ރުޅިވެރިކަމެއް", -20)], hum=True)
sh(69, "He said, in a voice like the wind, calmly: \"Alex! The third one will die tonight! Alex!\"",
   speaker="masked_killer", hum=True)
sh(70, "\"Give my regards to your father!\" The figure leapt out of the window and fled.",
   [("wind_gust", "ފުންމާލައި", -16)], speaker="masked_killer")
sh(71, "As the smoke slowly cleared, Alex rose to his feet, coughing. Sarah ran to the window and looked out, but the figure had vanished into the rain.",
   [("footsteps_pavement", "ދުވެފައި", -20)])
sh(72, "Alex looked at the desk. The yearbook had been taken. But in the moment he struggled with the killer, a page torn from that book had stayed in Alex's hand.",
   [("paper_shuffle", "ވީދައިލެވުނު", -22)])
sh(73, "Just one page. It was part of a list with the names of the members of that secret club. The third name on that page: Senator William Hastings.",
   hum=True)
sh(74, "He is scheduled to give an interview tonight at a live TV station in Boston. Sarah came up to Alex and stopped.")
sh(75, "\"He said the third one dies tonight! That's Hastings!\" Alex straightened his coat and put his pistol back in its holster.",
   [("cloth_rustle", "ރަނގަޅުކޮށްލަމުން", -22)], speaker="sarah")
sh(76, "\"We don't have much time. Let's go.\" The two went out together into the rain — towards the dangerous battle to save the third",
   [("door_open", "ނުކުމެގެން", -20), ("footsteps_pavement", "ވިއްސާރައިގެ", -20)], speaker="alex")
sh(77, "target on the killer's list. And yet, in Alex's heart there still remained the biggest question.")
sh(78, "What was in the part that had been erased from that photo? To be continued.",
   [("thunder", "ކޮންބައެއްބާ", -18)], hum=True)
SHOTS = S

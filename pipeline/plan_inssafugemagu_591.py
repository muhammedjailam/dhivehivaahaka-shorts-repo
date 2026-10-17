"""Beat/shot plan for Inssafuge Magu episode 591 (series opener; used by plan_beats.py)."""

LOC = {
    "manhattan_street": "a Manhattan avenue at night in heavy cold late-September rain, deep between towering glass skyscrapers of the Financial District, the wet black asphalt below streaked with smeared red and white car-light trails",
    "vance_office": "Victor Vance's huge glass-walled corner office on the 44th floor of Vance & Hart Investments in the Financial District: floor-to-ceiling rain-streaked glass walls with the whole night city of Manhattan below, an expensive dark-red Persian carpet, tall mahogany bookshelves, a massive dark polished desk with a black high-backed leather chair, a green-shaded desk lamp, a heavy dark wooden door",
    "vance_desk": "the massive dark polished mahogany desk in Victor Vance's 44th-floor office at night: financial reports, a computer keyboard and a monitor, a green-shaded desk lamp, a black high-backed leather chair, the rain-streaked glass wall and the night city behind",
    "office_window": "the floor-to-ceiling glass wall of Victor Vance's 44th-floor corner office at night, rain streaming down the glass, the whole of Manhattan spread far below like a black sea dotted with crimson and amber lights",
    "fax_corner": "a dark corner of Victor Vance's 44th-floor glass office at night: an antique beige fax machine on a small mahogany side cabinet beside the tall bookshelves, the rain-streaked glass wall and the city glow beside it",
    "richard_study": "Judge Richard Brand's home study at night: dark wood panelling, shelves of heavy law books, a big wooden desk with a brass desk lamp, a crystal glass of water on a small grey marble side table, a dark stone floor, a tall window streaked with rain",
}
MOOD = {
    "manhattan_street": "Manhattan storm night: near-black, deep crimson and amber reflections on wet glass and asphalt, slanting silver rain, cold and ominous",
    "vance_office": "night office: dim warm desk-lamp pools, cold blue city glow through the rain-streaked glass, crimson and amber reflections, near-black shadows, a frozen eerie silence",
    "vance_desk": "night office: a single warm desk-lamp pool on the dark wood, cold blue city glow, crimson reflections from the city on polished surfaces, near-black shadows, tense and silent",
    "office_window": "night: cold blue city glow and crimson-amber lights far below, silver rain on the glass, the dark office behind, lonely and foreboding",
    "fax_corner": "night office: near-black, the cold blue glow of the city through the glass, a small green indicator light glowing on the machine, uncanny and tense",
    "richard_study": "judge's study at night: warm amber lamp light against deep shadows, rain running down the dark window, cold blue night outside, frightened and claustrophobic",
}

GLOVES = "thin pale-blue latex gloves on his hands"
WET = "his long black overcoat glistening with rain drops"
NOBODY = "the tall black leather chair is completely EMPTY, nobody sitting in it, its high back turned towards the viewer"
COIN = ("an ancient thick heavy bronze-gold Roman coin, about an inch across, showing a laurel-crowned Roman emperor in profile "
        "facing right, with a worn, completely illegible rim inscription")

BEATS = [
    dict(to=3, reason="episode opening: Manhattan drowned in the cold September night rain, car lights smeared on the wet asphalt", loc="manhattan_street",
         visual="a deep vertical view down a Manhattan avenue between towering glass skyscrapers in heavy night rain; rain streaming down the tall glass facades; far below, smeared red and white light trails of passing cars on the wet black asphalt, their crimson glow spreading over the glossy street; silver rain streaks everywhere; no people",
         camera="wide establishing shot, slightly high angle, the towers and their lit tops in the upper two-thirds, the wet glossy street as the lower third",
         amb="city_rain_night", sens="other", safe="the narration's 'blood-coloured' sheen is shown only as crimson reflected light on wet asphalt, never liquid"),
    dict(to=6, reason="scene change: the 44th floor of Vance & Hart Investments — the grand glass-walled office, Persian carpet and mahogany shelves", loc="vance_office",
         visual="the huge glass-walled corner office seen wide from near the door: floor-to-ceiling rain-streaked glass walls with the whole glittering night city of Manhattan below, an expensive dark-red Persian carpet, tall mahogany bookshelves on the side wall, and far away by the glass the massive dark desk with a single green-shaded lamp glowing; the high-backed black leather chair behind the desk empty and turned away; no people",
         camera="wide shot, eye level, the glass walls, city and the lamp-lit desk in the upper two-thirds, the dark Persian carpet as the lower third",
         amb="office_storm_night"),
    dict(to=8, reason="the shadow of death: the founder Victor Vance at his big desk (never shown — the empty chair turned away)", loc="vance_desk",
         visual=f"the massive dark desk under the green-shaded lamp in the otherwise dark office; {NOBODY}, half turned towards the rain-streaked glass wall; the city lights glow crimson and amber through the rain behind; a heavy, frozen silence; nobody in the room",
         camera="medium-wide shot, eye level from across the room, the chair, lamp and glass wall in the upper two-thirds, the polished desk top as the lower third",
         amb="office_storm_night", sens="violence", safe="Victor Vance's body is never shown: only the empty black leather chair turned away under the desk lamp", hum=True),
    dict(to=10, reason="detail: the desk top with the financial reports and the keyboard (the wound and the blood are never shown)", loc="vance_desk",
         visual="close detail of the dark polished desk top in the lamp light: loose financial reports scattered in disarray, a computer keyboard knocked askew, a pen lying on its side; deep crimson city-light reflections gleaming on the glossy wood; behind, out of focus, the bare dark office wall; no person, no hand, no liquid, all papers blurred with no readable text",
         camera="close detail shot, low angle along the desk top, the scattered papers and lamp in the upper two-thirds, the dark glossy desk edge as the lower third",
         amb="office_storm_night", sens="violence", safe="the head wound, the blood on the reports and the dead man's face and pistol are never shown: only scattered papers and a keyboard in lamp light, red only as reflected city light"),
    dict(to=12, reason="character enters: the heavy door opens and FBI analyst Alex Brand walks in with a cold gust", chars=["alex"], loc="vance_office",
         visual=f"Alex Brand stepping in through the heavy dark wooden door of the office, {WET}, white shirt and slim dark tie, his calm deep grey eyes already scanning the room; a cold gust stirs the hem of his coat; the dim corridor light behind him, the dark office and the glass city glow in front",
         camera="medium-wide shot from inside the office, Alex centred in the doorway in the upper two-thirds, the dark carpet as the lower third",
         amb="office_storm_night", sens="weapon", safe="Victor's pistol in his hand (shot 11) is never shown; the image is Alex's arrival"),
    dict(to=17, reason="character enters: NYPD Detective Rogers arrives behind him, shakes the rain off his jacket and calls it an obvious suicide", chars=["rogers", "alex"], loc="vance_office", speaker="rogers",
         visual="Detective Rogers standing just inside the office door, shaking rain drops off his worn brown leather jacket, light-blue shirt and loose brown tie, his grey moustache drooping, speaking in a bored, impatient way with one empty hand raised in a dismissive gesture; in the soft-focus foreground at the side, Alex's dark shoulder and the back of his head in the black overcoat; the dim office and glass city glow behind",
         camera="over-the-shoulder medium shot, Rogers centred and sharp in the upper half, Alex blurred in the foreground, the carpet as the lower third",
         amb="office_storm_night"),
    dict(to=18, reason="action change: Alex silently loosens his tie and walks slowly towards the desk, mapping the room's geometry", chars=["alex"], loc="vance_office",
         visual="Alex walking slowly and silently across the dark-red Persian carpet towards the lamp-lit desk, one hand loosening the knot of his slim dark tie, his eyes moving over the room, measuring it; the empty black leather chair turned away behind the desk ahead of him, the rain-streaked glass walls and the city glow around",
         camera="medium shot from the side, slightly low, Alex's face and the desk in the upper two-thirds, the carpet as the lower third",
         amb="office_storm_night"),
    dict(to=21, reason="action change: Alex kneels by the desk and looks closely; he tells Rogers suicides lock the door but don't arrange everything", chars=["alex"], loc="vance_desk", speaker="alex",
         visual=f"Alex crouching on one knee beside the dark desk next to the empty black leather chair, {GLOVES}, his face lit by the green-shaded lamp, looking down intently at something below the frame, then speaking calmly with a firm, quiet expression; the rain-streaked glass wall and city glow behind him; nobody in the chair",
         camera="medium close-up, eye level, Alex centred and sharp in the upper half, the dark desk side as the lower third",
         amb="office_storm_night", sens="violence", safe="the body Alex examines is never shown: he looks down at something below the frame"),
    dict(to=24, reason="action change: Rogers steps up; Alex points with his latex-gloved finger at the staged desk — phone, wallet and papers lined up on the left", chars=["alex", "rogers"], loc="vance_desk", speaker="alex",
         visual=f"Alex leaning over the dark desk, {GLOVES}, pointing with one gloved finger at a phone, a leather wallet and a neat stack of papers lined up precisely on the left side of the desk, while the rest of the desk is in disarray; he looks up as he explains, sharp and focused; Detective Rogers in his brown leather jacket standing behind the desk at the side, frowning down; the green lamp between them; no person in the chair, papers blurred",
         camera="medium shot, slightly high angle, Alex centred and sharp in the upper half, Rogers softer at the side, the desk top with the neat objects as the lower third",
         amb="office_storm_night", sens="violence", safe="'the blood ran from the right' is only described; the image shows the neatly lined-up objects, no blood"),
    dict(to=28, reason="turning point: Alex bends down to the left hand — 'the most important thing' — rigid, clenched (never shown)", chars=["alex"], loc="vance_desk", speaker="alex",
         visual=f"close-up of Alex crouched low beside the armrest of the empty black leather chair, {GLOVES} raised slightly, his narrowed grey eyes fixed on something just below the frame, explaining in a low voice; lamp light on one side of his face, cold blue glow on the other",
         camera="close-up, eye level, Alex's face centred in the upper half, the dark chair leather and shadow as the lower third",
         amb="office_storm_night", sens="violence", safe="the dead man's clenched hand is never shown: only Alex's face and his own gloved hands"),
    dict(to=30, reason="action change: with great care he begins to open the cold fingers one by one (shown only as Alex's own gloved hands)", chars=["alex"], loc="vance_desk",
         visual=f"extreme close-up of Alex's own two hands in {GLOVES}, moving slowly and carefully together in the warm lamp light just above the dark edge of the desk, fingertips delicate as if about to open something; his tense face soft and out of focus above them; no other hands, nothing else in the frame",
         camera="extreme close-up, the gloved hands in the middle of the frame and his blurred face above, the dark desk edge and shadow as the lower third",
         amb="office_storm_night", sens="violence", safe="opening the corpse's fingers is shown only as Alex's own careful gloved hands; no corpse hand", hum=True),
    dict(to=31, reason="reaction: Rogers's eyes widen at what lies in the palm", chars=["rogers"], loc="vance_desk",
         visual="close-up of Detective Rogers leaning forward over the desk, his tired blue eyes suddenly wide with astonishment, grey moustache, the warm lamp light on his ruddy face, staring down at something below the frame",
         camera="close-up, eye level, Rogers's face centred in the upper half, the dark leather jacket and desk edge as the lower third",
         amb="office_storm_night"),
    dict(to=33, reason="reveal: the ancient Roman coin with the laurel-crowned emperor and its Latin inscription", chars=["alex"], loc="vance_desk",
         visual=f"close-up of {COIN}, resting in the open palm of Alex's pale-blue latex-gloved hand under the warm lamp light, its bronze glinting gold, deep crimson city-light reflections on its surface; the dark polished desk and blurred rain-streaked glass behind",
         camera="close-up macro shot, the coin and gloved palm in the upper-middle of the frame, the dark desk as the lower third",
         amb="office_storm_night", sens="other", safe="the coin's Latin inscription is never legible; no blood on it, red is only reflected light"),
    dict(to=34, reason="return to Rogers (shot): 'What is this? An antique from his collection?'", chars=["rogers"], loc="vance_desk",
         reuse="beat_012", amb="office_storm_night", visual="(reuse of beat_012)", transition="cut"),
    dict(to=36, reason="action change: Alex translates, lifts the coin into the light — a death-gift for the honoured dead — and notes skin under the nails", chars=["alex"], loc="vance_desk", speaker="alex",
         visual=f"Alex crouched beside the desk holding {COIN} up between two pale-blue latex-gloved fingers into the beam of the green-shaded lamp, studying it with narrowed grey eyes, then turning his face towards the viewer as he speaks with quiet intensity; the rain-streaked glass wall and the city's crimson glow behind",
         camera="medium close-up, eye level, Alex's face and the raised coin centred in the upper half, the dark desk side as the lower third",
         amb="office_storm_night", sens="violence", safe="the skin under the nails is only spoken about; the image shows Alex and the coin"),
    dict(to=38, reason="return to Alex (shot): he reconstructs the struggle — someone held him from behind and forced the trigger", chars=["alex"], loc="vance_desk",
         reuse="beat_010", amb="office_storm_night", visual="(reuse of beat_010)", transition="cut", sens="violence",
         safe="the struggle and the forced trigger are only narrated over Alex's face; no gun, no attacker shown"),
    dict(to=39, reason="return to Rogers (shot): 'The cameras...' — Alex: hackers loop cameras like a children's game", chars=["rogers"], loc="vance_desk",
         reuse="beat_012", amb="office_storm_night", visual="(reuse of beat_012)", transition="cut"),
    dict(to=40, reason="action change: Alex stands up straight and orders the servers seized and forensics in — it is murder", chars=["alex", "rogers"], loc="vance_office", speaker="alex",
         visual="Alex standing up tall beside the lamp-lit desk, upright and resolute in his long black overcoat with the loosened slim tie, speaking firmly with a hard, decisive look straight ahead; Detective Rogers soft in the background at the side, turning towards him in surprise; the rain-streaked glass walls and city glow behind",
         camera="medium shot, slightly low angle, Alex centred and sharp in the upper half, the carpet and desk edge as the lower third",
         amb="office_storm_night"),
    dict(to=43, reason="scene change: Alex walks to the window — from the 44th floor the city is a black sea; a long-planned revenge", chars=["alex"], loc="office_window",
         visual="Alex standing alone at the floor-to-ceiling glass wall seen from behind and slightly to the side, his tall silhouette in the long black overcoat, looking down at the whole of Manhattan far below, spread out like a black sea dotted with crimson and amber lights; rain streaming down the glass, his faint reflection in it",
         camera="medium-wide shot from behind at an angle, Alex and the city in the upper two-thirds, the dark floor and the base of the glass as the lower third",
         amb="office_storm_night", hum=True),
    dict(to=45, reason="action change: his phone vibrates — the screen says 'Father' — his hero, Judge Richard Brand", chars=["alex"], loc="office_window", speaker="alex",
         visual="Alex at the glass wall turning towards the viewer, holding his phone in one hand and looking down at its glowing screen, which shows only a soft blank light with no characters, its cold glow lighting his surprised face from below; the rain-streaked glass and the crimson city lights behind him",
         camera="medium close-up, eye level, Alex's face and the phone in the upper half, the dark coat as the lower third",
         amb="office_storm_night", sens="other", safe="the caller name 'Father' is narration only; the screen shows no text"),
    dict(to=47, reason="scene change: Judge Richard Brand in his study at night, phone at his ear, his voice trembling", chars=["richard"], loc="richard_study", speaker="richard",
         visual="Judge Richard Brand standing beside his big wooden desk in his dark study at night, holding a phone to his ear, his silver hair neatly combed, charcoal waistcoat and loosened burgundy tie, his lined face tense and pale, eyes wide with hidden fear, his other hand gripping the edge of the desk; a crystal glass of water on the grey marble side table beside him, the brass lamp's warm light, rain running down the dark window behind",
         camera="medium shot, eye level, Richard centred and sharp in the upper half, the desk top and dark stone floor as the lower third",
         amb="mansion_night"),
    dict(to=50, reason="reverse shot: Alex on the phone, calmly — 'I'm at the crime scene; it is murder' — then a long silence", chars=["alex"], loc="office_window", speaker="alex",
         visual="close-up of Alex holding the phone to his ear in the dim office by the rain-streaked glass, speaking calmly with a steady, serious face, then listening intently to the silence on the line, his grey eyes narrowing; cold blue city glow on one side of his face, warm lamp light from the office on the other",
         camera="close-up, eye level, Alex's face centred in the upper half, the dark overcoat as the lower third",
         amb="office_storm_night"),
    dict(to=52, reason="return to Richard (reverse shot): his breathing fast, an unheard warning in his voice", chars=["richard"], loc="richard_study",
         reuse="beat_021", amb="mansion_night", visual="(reuse of beat_021)", transition="cut", hum=True),
    dict(to=55, reason="emotional turning point: Richard warns him off — Vance dealt with dangerous people, accept suicide, think of your career", chars=["richard"], loc="richard_study", speaker="richard",
         visual="close-up of Judge Richard Brand in his study, the phone pressed to his ear, sitting forward in his chair, his silver brows drawn together, eyes glistening with fear and pleading, speaking low and urgently; the brass lamp's warm light on his lined face, deep shadows and the rain-streaked dark window behind",
         camera="close-up, eye level, Richard's face centred in the upper half, the charcoal waistcoat and burgundy tie as the lower third",
         amb="mansion_night", hum=True),
    dict(to=57, reason="action change: stunned, Alex raises his voice — 'Why are you saying this?' — and mentions the Roman coin in his hand", chars=["alex"], loc="office_window", speaker="alex",
         visual=f"Alex by the rain-streaked glass wall with the phone at his ear, his face hardening in shock and disbelief, speaking with rising intensity, while his other pale-blue latex-gloved hand holds up {COIN} near his face; crimson and amber city lights behind",
         camera="medium close-up, eye level, Alex's face and the coin centred in the upper half, the dark overcoat as the lower third",
         amb="office_storm_night"),
    dict(to=58, reason="shock: on the line a crystal glass shatters on stone, a frightened gasp, the call cuts (Richard never shown hurt)", loc="richard_study", transition="cut",
         visual="low close-up on the dark stone floor beside the judge's desk: a crystal water glass shattering, shards and droplets of clear water flying in the warm lamp light; above, on the edge of the desk, a phone lying abandoned; an empty desk chair pushed back in the shadows; no person, rain on the dark window behind",
         camera="low close-up near the floor, the shattering glass and the desk edge in the upper two-thirds, the dark stone floor as the lower third",
         amb="mansion_night", sens="violence", safe="whatever happened to Richard is never shown: only clear water and crystal shards on the stone floor, an abandoned phone and an empty chair", hum=True),
    dict(to=59, reason="emotional change: 'Dad? Dad!' — only the dead tone; Alex lowers the phone, a cold fear spreading", chars=["alex"], loc="office_window", speaker="alex", transition="cut",
         visual="Alex by the dark rain-streaked glass, slowly lowering the phone from his ear, his face pale and stricken, lips parted, grey eyes wide with cold fear and confusion; the city lights blurred crimson behind him",
         camera="close-up, eye level, Alex's face centred in the upper half, the lowered phone and dark coat as the lower third",
         amb="office_storm_night", hum=True),
    dict(to=61, reason="new event: the antique fax machine in the corner starts by itself; Rogers starts (his hand to his hip is never shown)", chars=["rogers"], loc="fax_corner",
         visual="the antique beige fax machine in the dark corner of the office suddenly whirring to life, its small green light glowing, the edge of a white sheet starting to feed out; in the background at the side, Detective Rogers in his brown leather jacket startled and half turning towards it, both of his hands empty and raised slightly in front of his chest; cold blue city glow through the glass",
         camera="medium shot, eye level, the fax machine in the upper-middle and Rogers soft at the side, the dark cabinet top as the lower third",
         amb="office_storm_night", sens="weapon", safe="Rogers reaching for his gun is shown as a startled man with empty hands; no gun, no holster"),
    dict(to=63, reason="action change: Alex walks to the fax as a white sheet slowly slides out; no name, no sender; he picks it up", chars=["alex"], loc="fax_corner",
         visual="Alex standing beside the antique fax machine in the dark corner, looking down with a fixed, wary gaze as a white sheet of paper slowly slides out of it, one pale-blue latex-gloved hand reaching to take it; the paper's surface blank and turned away; the small green light and the cold city glow on his face",
         camera="medium close-up from the side, Alex's face and the emerging paper in the upper two-thirds, the dark cabinet top as the lower third",
         amb="office_storm_night"),
    dict(to=65, reason="detail: the fax sheet — 'The first step has been taken. Six remain. ... Justice comes in the rain, Alex.' (unreadable)", chars=["alex"], loc="fax_corner",
         visual="close-up of a single white fax sheet held in Alex's pale-blue latex-gloved hands, showing only a few blurred, smudged dark lines that cannot be read; behind it, out of focus, Alex's narrowed grey eyes staring at the page; cold blue glow and crimson reflections of rain on the glass",
         camera="close-up, the sheet in the middle of the frame and Alex's eyes above it, the dark coat as the lower third",
         amb="office_storm_night", sens="other", safe="the fax message is never legible: only blurred dark lines", hum=True),
    dict(to=66, reason="turning point: the killer knew he'd come and knows his name — thunder, and the lights flicker", chars=["alex"], loc="vance_office",
         visual="the dark office in a sudden flash of white lightning beyond the glass walls, the lamps dimmed and flickering; Alex standing in the middle of the room holding the white sheet at his side, his face half lit by the lightning, hard and alarmed, looking up; the rain-streaked glass and the stormy city behind",
         camera="medium-wide shot, eye level, Alex and the lightning-lit glass wall in the upper two-thirds, the dark carpet as the lower third",
         amb="office_storm_night", hum=True),
    dict(to=68, reason="closing: a dangerous game over a twenty-year-old secret, with Alex and his family in the middle (return to Alex at the window over the city)", chars=["alex"], loc="office_window",
         reuse="beat_019", amb="office_storm_night", visual="(reuse of beat_019)", transition="dissolve"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Manhattan, New York City, lay drowned in the merciless wetness of heavy rain. Late in the month of September,",
   [("rain_start", "ވިއްސާރައިގެ", -18)])
sh(2, "on this cold night, the raindrops beating on the tall glass of the skyscrapers sounded like the cracks of angry gunfire.")
sh(3, "The light of the red and white lamps of the cars racing through the streets fell on the soaked asphalt, giving the whole city a faint, blood-coloured, foamy shimmer.",
   [("car_pass", "ދުއްވާ", -20)])
sh(4, "On the forty-fourth floor of Vance & Hart Investments, one of the tallest and most prestigious buildings of the Financial District, lay a frightening, frozen silence.")
sh(5, "The main office on that floor is a grand place walled all round with glass, so that the beautiful view of the whole of Manhattan can be seen.")
sh(6, "The expensive Persian carpet laid on its floor and the mahogany bookshelves on the walls displayed the power of authority and money amassed over many years.")
sh(7, "But tonight, in the midst of all that wealth, the shadow of death had fallen. Sitting in the black leather chair beside the office's big desk was the company's founder,",
   hum=True)
sh(8, "the famous fifty-year-old billionaire Victor Vance. His body lay leaning outward, slumped onto the thick desk.",
   hum=True)
sh(9, "Because of a shot that had burst out through the right temple of his head, a stream of hot blood had spread over the financial reports and the computer keyboard on the desk.")
sh(10, "His pupils were fixed on the office's empty wall. His mouth slightly open, his face showed a terror hard to describe.",
   hum=True)
sh(11, "In his right hand lay a nine-millimetre pistol, his finger still inside the trigger. With the sound of the heavy door opening, and with a cold gust of wind, in came the FBI's special criminal analyst, Alex Brand.",
   [("door_open", "ހުޅުވިގެން", -16), ("wind_gust", "ވައިރޯޅިއަކާއެކު", -18)])
sh(12, "Alex, a man of a black coat and a silent, deep gaze, is a mind noted across the whole Bureau for spotting the small details in investigations.")
sh(13, "Behind him, with quick steps, came the New York Police Department's experienced Detective Rogers.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -20)])
sh(14, "Shaking out his jacket, Rogers began to talk in a bored tone. \"Alex, I can't see why you came running here.\"",
   [("cloth_rustle", "ފޮޅާލަމުން", -20)], speaker="rogers")
sh(15, "\"Look at this case. It's a straight suicide. The security cameras show him going into this room alone at eight-thirty tonight.\"",
   speaker="rogers")
sh(16, "\"After that nobody came to this floor. The door was locked from the inside. With a big Wall Street slump coming,\"",
   speaker="rogers")
sh(17, "\"these people killing themselves is nothing new to us.\" Alex gave no answer.", speaker="rogers")
sh(18, "Loosening the tie at his throat a little, he began walking slowly towards the dead man, so softly that not even his shoes made a sound. With every step he took, the geometry of the whole room and the way things were placed were being drawn into his mind.",
   [("cloth_rustle", "ދޫކޮށްލަމުން", -24)])
sh(19, "Alex knelt down beside the desk and looked very closely at Victor's body.",
   [("cloth_rustle", "ކަކޫޖަހައިގެން", -24)])
sh(20, "\"People who kill themselves lock the door so that nobody comes in from outside and stops them, Rogers,\" Alex said.",
   speaker="alex")
sh(21, "His voice was soft, but there was firmness in every word. \"But people who kill themselves don't put everything in such neat order before they die.\"",
   speaker="alex")
sh(22, "\"What are you saying?\" Rogers moved closer to the desk. \"Look at this.\" Alex pointed at the desk with his latex-gloved finger.",
   [("footsteps_pavement", "ޖެހިލި", -24)], speaker="alex")
sh(23, "\"We're told Victor was shot in the head from the right. The blood from his head ran from the right side towards the middle of the desk. But his phone,\"",
   speaker="alex")
sh(24, "\"his wallet and his papers are on the left side, lined up in order. That's a sign someone cleared the desk before he died and staged it a certain way.\"",
   speaker="alex")
sh(25, "\"And the most important thing is this...\" Alex bent lower and looked at Victor's left hand.", speaker="alex")
sh(26, "\"Normally, when a man dies of a shot to the head, his muscles and nerves let go at once, and the body goes weak and limp.\"",
   speaker="alex")
sh(27, "\"But Victor's left hand is rigid, clenched so hard that the nails are digging into the flesh of the palm.\"",
   speaker="alex")
sh(28, "\"The fingertips of that hand have turned white, as if the blood stopped flowing. Look at this palm,\" Alex said.",
   speaker="alex")
sh(29, "With great care, he began to part Victor's cold, stiffened fingers one from another. At that moment small sounds came from the bones.",
   hum=True)
sh(30, "\"When a man kills himself, he only clenches this hard if there's something in his hand. Or else someone put that thing in his hand and pressed the hand shut with force at the moment of death.\"",
   speaker="alex", hum=True)
sh(31, "As the fingers opened completely, Rogers's eyes widened at what was seen in the middle of the palm. It was not a thing of this age.",
   [("gasp", "ބޮޑުވި", -20)], hum=True)
sh(32, "An inch-wide, thick, heavy, bronze-gold ancient Roman coin. On one side was struck the image of a Roman emperor wearing a crown of olive leaves.",
   [("coin_clink", "ފައިސާފޮއްޗެއް", -18)])
sh(33, "On the other side, deeply engraved, was a phrase in Latin: Mors omnia solvit. Rogers stepped forward in astonishment.",
   [("footsteps_pavement", "ޖެހިލި", -24)])
sh(34, "\"What is this? An antique coin he kept in his collection?\" \"Death settles everything.\"", speaker="rogers")
sh(35, "Alex translated the Latin words. He picked up the coin and raised it into the light. \"This is no ordinary Roman denarius.\"",
   [("coin_clink", "ނަގައި", -20)], speaker="alex")
sh(36, "\"It's the kind of coin placed in the mouth or the hand of people being buried, as the gift of an honourable death! And look — under the nails of Victor's left hand there are bits of someone else's skin.\"",
   speaker="alex", hum=True)
sh(37, "\"He struggled with someone before he died. Someone came up behind him, held something over his mouth, and made him pull the trigger with his own hand.\"",
   [("heartbeat", "ފިއްތުވީ", -22)], speaker="alex", hum=True)
sh(38, "\"This is a murder planned as perfectly as carved stone. But—\"", speaker="alex")
sh(39, "\"The cameras...\" Rogers tried to argue. \"For hackers, swapping a camera loop is child's play.\"", speaker="rogers")
sh(40, "Standing up straight, Alex said firmly: \"Seize the security servers right now. Tell the forensic team this is a murder investigation.\"",
   [("cloth_rustle", "ތެދުވަމުން", -22)], speaker="alex")
sh(41, "Alex walked over to the window. Looking down from the forty-fourth floor, the whole city lay like a black, dark sea.",
   [("footsteps_pavement", "ހިނގައިގަތް", -22)])
sh(42, "Killing a man as influential as Victor Vance, master of billions of dollars, and placing such a sign in his hand, is no ordinary cruelty or personal anger.",
   hum=True)
sh(43, "This is the beginning of a very long-planned, very deep revenge. At that very moment, the phone in the inner pocket of Alex's coat began to vibrate.",
   [("phone_buzz", "ވައިބްރޭޓްވާން", -16)], hum=True)
sh(44, "When he looked at the screen, the name showing was 'Father' — Dad. Alex's father, Richard Brand, is one of the most respected judges of New York's State Supreme Court.")
sh(45, "As a model of law and justice, Alex had always seen his father as his one and only hero. Alex picked up the phone and held it to his ear. \"Dad?\"",
   speaker="alex")
sh(46, "\"At this hour?\" From the other end came a heavy voice, yet one trembling unusually. \"Alex... I\"",
   speaker="richard")
sh(47, "\"just saw it on the TV breaking news. The news that Victor Vance killed himself.\"", speaker="richard")
sh(48, "\"Are you on the investigation, son?\" \"Yes, Dad. I'm at the crime scene,\" Alex said calmly.", speaker="alex")
sh(49, "\"But this isn't a suicide. This is a crime someone planned and carried out.\"", speaker="alex")
sh(50, "Suddenly silence fell on the other end of the line. Every second that silence stretched on was a moment in which a rhythm of suspicion began to beat in Alex's mind.",
   [("heartbeat", "ހިމޭންކަން", -22)], hum=True)
sh(51, "Through the phone Alex could clearly hear that his father's breathing had grown unusually fast. \"Alex...\"",
   [("breath_heavy", "ނޭވާލާ", -20)], speaker="richard", hum=True)
sh(52, "In Richard's voice was a trace of warning and anxiety never heard before. \"Some things are not things it is wise to look into deeper than you should.\"",
   speaker="richard", hum=True)
sh(53, "\"Victor Vance did business with very dangerous, powerful people. Sometimes people die because they have to carry the weight of great sins that cannot be shown to the world.\"",
   speaker="richard", hum=True)
sh(54, "\"Respect the police's decision; the wise thing is to close it as a suicide — a man who took his own life.\"", speaker="richard")
sh(55, "\"Think of your career, son.\" Alex froze. The father who had taught him all his life that finding the truth stands above everyone,",
   speaker="richard", hum=True)
sh(56, "today is telling him to stop the investigation? \"Dad, why are you saying this?\" Alex's voice rose a little.", speaker="alex")
sh(57, "\"What was found in his hand was an ancient Roman coin. On it is...\" Alex could not finish his sentence.", speaker="alex")
sh(58, "From the other end came a sound like a crystal glass breaking and falling onto stone. With the sound of a frightened gasp from Richard's mouth, the line suddenly went dead.",
   [("glass_break", "ތަޅައިގެން", -14), ("gasp", "އާހެއްގެ", -16)], hum=True)
sh(59, "\"Dad? Dad!\" Alex called out. But all he heard was the empty tone. As Alex lowered the phone, an indescribable coldness ran through his heart.",
   [("dial_tone", "ޓޯންގެ", -20)], speaker="alex", hum=True)
sh(60, "Does Father know about this coin? Or what connection does Father have with Victor Vance's past? At that very moment, an antique fax machine in a corner of the silent office started up by itself.",
   [("fax_print", "ހިނގައިގަތް", -16)], hum=True)
sh(61, "Its mechanical sound echoed through the whole room. Rogers started and put his hand on the gun at his waist.",
   [("fax_print", "މެކޭނިކަލް", -18), ("gasp", "ސިއްސައިގެން", -20)])
sh(62, "Alex walked slowly over and stopped beside the fax machine. A white sheet of paper was slowly coming out of the machine.",
   [("footsteps_pavement", "ހިނގާފަ", -24), ("paper_shuffle", "ކަރުދާސްގަނޑެއް", -20)])
sh(63, "On that paper there was no name, no sender's address. Only a few lines printed in black ink. Alex took the paper and read it.",
   [("paper_shuffle", "ނަގައި", -22)])
sh(64, "\"The first step has been taken. Six remain. The sins of nineteen ninety-eight cannot be hidden",
   hum=True)
sh(65, "by buried bones. Justice comes riding the rain, Alex.\" Alex's eyes stopped on his own name on the paper.",
   [("heartbeat", "ނަމަށް", -22)], hum=True)
sh(66, "The killer knew he would come here. And he knows his name too. With the sound of a loud thunderclap from outside, all the lights in the room flickered out for a brief moment.",
   [("thunder", "ގުގުރީގެ", -14), ("bulb_flicker", "ނިވިދިއްލިގެން", -16)], hum=True)
sh(67, "This is not just a matter of a death. This is a dangerous game, soaked in blood, begun to expose a dark secret from some twenty years ago.",
   hum=True)
sh(68, "And in the middle of that game are Alex himself and his family. To be continued.",
   [("thunder", "ނުނިމޭ", -22)], hum=True)
SHOTS = S

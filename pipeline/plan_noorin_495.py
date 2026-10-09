"""Beat/shot plan for Noorin episode 495 (used by plan_beats.py)."""

FB = "twelve years earlier, warm soft golden haze"

LOC = {
    "street": "a busy commercial street in Malé twelve years ago at night, a row of small shops with canvas awnings and roller shutters, wet tarmac reflecting shop lights and streetlamps, parked motorbikes, narrow multi-storey buildings",
    "jetty": "a busy ferry jetty on the edge of Malé twelve years ago, small wooden passenger ferries moored at a concrete quay, the city's colourful low-rise buildings behind",
    "mother_room": "a small plain bedroom in an old Malé apartment twelve years ago at night, whitewashed walls, a narrow window streaked with rain, a single wooden chair, a closed wooden door",
    "mother_lane": "a narrow residential lane in Malé twelve years ago at night, the gated entrance of an old multi-storey apartment building, rain-wet concrete, a few lit windows above",
    "luxury_room": "a luxurious modern bedroom twelve years ago, cream and soft-gold decor, a wide neatly made bed with crisp white linen, sheer curtains, a tall wooden wardrobe, a sleek modern writing desk with a lamp and a notebook",
    "apartment": "Noorin's tidy modern apartment in Malé today at night, a small dining table, a writing desk with a laptop, a tall wall mirror, grey-blue walls, a window with rain and city lights",
    "zee_office": "Zee's small cosy home office in Malé at night, shelves of bound scripts, a desk lamp, film posters with blank unreadable surfaces on the wall",
    "case_house": "the outside of a small two-storey house on a narrow Malé street at night, rain-wet road, an ambulance parked at the door",
    "case_living": "a modest living room of a Malé house at night, a worn fabric sofa, a low table, a woven rug, a ceiling fan, a window reflecting flashing red and blue light from the street",
    "office": "Noorin's office at the Malé police headquarters, a large wooden desk with stacked folders with blank covers, a desk lamp, window blinds, a plain wall",
    "classroom": "an empty school classroom in Malé on a rainy day, rows of small wooden desks and chairs, a large rain-streaked window",
    "child_room": "a small child's bedroom in a Malé flat at night, a little study desk with closed schoolbooks and a small desk lamp, a dark rain-streaked window",
    "prison_corridor": "a narrow corridor in a Maldivian prison, steel-barred cell doors along one side, grey concrete walls, cold fluorescent ceiling lights",
    "prison_cell": "a bare prison interview cell, grey concrete walls, a wall of steel bars with a barred door, a small metal table and two metal chairs, a small security camera high in one corner",
    "court": "the steps and paved forecourt of a white court building in Malé in the daytime, a few palm trees, a white police vehicle with a light bar parked at the kerb, traffic in the street",
    "car": "the inside of a police vehicle driving through Malé in the daytime, the passenger-side window and side mirror, city buildings sliding past",
}
MOOD = {
    "street": f"{FB} over a stormy night: flashes of lightning, heavy slanting rain lit amber by shop lights and streetlamps, glistening reflections, lonely and desperate",
    "jetty": f"{FB}, bright gentle morning sunshine, turquoise water, hopeful and innocent",
    "mother_room": f"{FB} on a rainy night, dim lamplight, deep soft shadows, rain trickling down the glass, silent heartbreak",
    "mother_lane": f"{FB} on a rainy night, a dim amber lamp over the gate, deep blue shadows, heartbreak",
    "luxury_room": f"{FB}, soft morning light through sheer curtains, a calm luxurious stillness contrasting with her confusion and fear",
    "apartment": "present day, night, cool navy and teal tones, warm amber desk lamp, the cold glow of a laptop screen, rain on the window, quiet and private",
    "zee_office": "present day, night, warm amber desk lamp, cosy and earnest",
    "case_house": "present day, night, flashing red and blue emergency lights on wet tarmac, urgent and grave",
    "case_living": "present day, night, a single dim lamp, flashing red and blue light from the window, heavy grief",
    "office": "present day, daytime, cool grey-blue light through the blinds, a warm desk lamp, controlled and heavy",
    "classroom": "rainy grey daylight, soft muted blue tones, empty and lonely, a quiet memory",
    "child_room": "night, a small warm desk lamp against deep blue shadows, rain on the window, fearful and lonely",
    "prison_corridor": "present day, cold fluorescent white light and hard shadows, tense",
    "prison_cell": "present day, cold fluorescent light, harsh shadows, steel-grey and navy tones, tense and charged",
    "court": "present day, bright tropical midday sun, crisp shadows, blue sky",
    "car": "present day, bright daylight through the window, cool shade inside the vehicle, quiet and guarded",
}

YN = "young Noorin (about 22)"
UNI = "Noorin in her dark-navy police uniform, black hijab fully covering her hair and neck and black beret"
OFF = "Noorin, not in uniform: wearing a loose deep-plum long abaya-style dress and a black hijab fully covering her hair and neck, no cap"
LOW = "faces in the upper two-thirds, a calm uncluttered lower third"

BEATS = [
    # ---------------- TWELVE YEARS AGO
    dict(to=4, reason="episode opening: twelve years ago, thunderstorm over a crowded Malé street at night", loc="street",
         visual="a wide view of the crowded Malé street at night under a thunderstorm: a jagged bolt of lightning splits the dark clouds above narrow buildings, heavy rain, motorbikes and cars jammed on the wet road with headlights glaring, many people hurrying to shelter under the shop awnings; nobody's face in close detail",
         camera=f"wide establishing shot, slightly high angle, the stormy sky and street in the upper two-thirds, the glistening wet road as the calm lower third",
         amb="storm_night", transition="dissolve"),
    dict(to=7, reason="character enters: young Noorin among the people sheltering under an awning", chars=["noorin_young"], loc="street",
         visual=f"{YN} standing among a few strangers under a shop's canvas awning, soaked through, her dusty-rose dress and cream hijab dark with rain, her eyes red and swollen, tears mixing with raindrops on her cheeks, staring out at the downpour with a lost, anguished look; the other people are blurred and keep their distance",
         camera=f"medium shot, eye level, {LOW} (wet pavement)", amb="rain_night"),
    dict(to=8, reason="memory/time change: she had come to her birth mother in Malé full of hope", chars=["noorin_young"], loc="jetty",
         visual=f"{YN} stepping off a small wooden ferry onto the sunny quay, holding a small cloth travel bag in both hands, a shy hopeful smile, looking up towards the city buildings",
         camera=f"medium wide shot, eye level, {LOW} (sunlit concrete quay)", amb="jetty_day", transition="dissolve"),
    dict(to=12, reason="scene change: her struggle in her mother's house, shown only through her face, rain and a closed door",
         chars=["noorin_young"], loc="mother_room",
         visual=f"{YN} standing alone at a narrow rain-streaked window in a small dim room at night, one hand resting flat on the glass, her face half turned towards us with quiet anguish and stubborn resolve, her small cloth bag packed on the chair; behind her a closed wooden door; nobody else in the room",
         camera=f"medium shot, eye level, slightly from the side, {LOW} (bare floor in soft shadow)", amb="memory_rain",
         sens="other", safe="the stepfather and the danger to her honour are never shown or implied; only her face, rain on the window and a closed door"),
    dict(to=14, reason="action change: she leaves her mother's house sobbing into the dark rainy night", chars=["noorin_young"], loc="mother_lane",
         visual=f"{YN} hurrying out through the gate of the old apartment building into the dark rainy lane, her small cloth bag clutched to her chest, one hand pressed to her mouth, tears on her face, glancing back up at a softly lit window; nobody else in the lane",
         camera=f"medium wide shot, eye level, {LOW} (wet concrete lane)", amb="rain_night", transition="dissolve"),
    dict(to=16, reason="time change: the rain eases, people leave, shops close at eleven; she stands frozen", chars=["noorin_young"], loc="street",
         visual=f"the rain thinning over the street late at night: a shopkeeper in the background pulling down a metal roller shutter, the last few people walking away with umbrellas in different directions; {YN} standing completely still alone under the awning in the middle of the frame, soaked, staring blankly ahead like a statue",
         camera=f"medium wide shot, eye level, {LOW} (glistening empty pavement)", amb="rain_night"),
    dict(to=18, reason="action change: exhausted, she sits down at the roadside in the rain, shivering", chars=["noorin_young"], loc="street",
         visual=f"{YN} sitting hunched on the edge of the pavement at the empty roadside in the rain, arms wrapped tightly around herself, shivering, her dress and hijab soaked, eyes half closed with exhaustion and grief, closed shutters behind her and puddles reflecting the streetlamps",
         camera=f"medium shot, slightly high angle, {LOW} (wet road surface)", amb="rain_night"),
    dict(to=20, reason="character change: a stranger with an umbrella is beside her (young Uvaish, shown only from behind)", loc="street",
         visual="the empty rain-wet street late at night: a tall young man seen only from behind as a dark silhouette, in a white long-sleeved shirt and beige trousers, holding a large black umbrella, standing still at the edge of the pavement and looking down towards the kerb, under the warm halo of a single streetlamp, rain falling in silver streaks; his face is not shown and no one else is visible",
         camera="wide shot from behind the man, low angle, his silhouette and the umbrella in the upper two-thirds, the shining wet road as the calm lower third",
         amb="rain_night", sens="other",
         safe="her fainting and being lifted in his arms are never shown; only the stranger (young Uvaish) as a silhouette with an umbrella seen from behind, no contact"),
    dict(to=24, reason="time and scene change: she wakes in an unknown luxurious room in clean clothes", chars=["noorin_young"], loc="luxury_room",
         visual=f"{YN} sitting bolt upright on the edge of the wide neatly made bed, feet on the floor, startled and frightened, eyes wide, one hand at her chest, looking around the strange elegant room; she is fully dressed in a clean dry dusty-rose long-sleeved ankle-length dress and a cream hijab fully covering her hair and neck",
         camera=f"medium wide shot, eye level, {LOW} (soft cream carpet)", amb="room_day", transition="black"),
    dict(to=28, reason="action change: she finds her bag by the wardrobe, writes a short note and hurries out", chars=["noorin_young"], loc="luxury_room",
         visual=f"{YN} bending over the sleek writing desk, quickly writing a short note in an open notebook with a pen, her small cloth bag already over her shoulder, glancing anxiously towards the door; the tall wardrobe behind her; the notebook page shows only faint blurred lines",
         camera=f"medium shot, eye level, {LOW} (desk top in soft light)", amb="room_day"),
    # ---------------- PRESENT
    dict(to=31, reason="time jump to the present: Inspector Noorin comes home, puts her cap down and looks at her stars in the mirror", chars=["noorin"], loc="apartment",
         visual=f"Noorin in her dark-navy police uniform, her black beret just taken off and placed neatly on the table beside her, her black hijab still fully covering her hair and neck: she stands before the tall wall mirror in her apartment, fingertips touching the two small silver stars on her shoulder epaulette, a quiet proud look; seen from behind her shoulder with her reflection in the mirror",
         camera=f"medium shot over her shoulder, eye level, {LOW} (table top with the beret)", amb="home_night", transition="dissolve"),
    dict(to=33, reason="action change: freshened up, she opens her laptop and reads her e-mails; her face changes", chars=["noorin"], loc="apartment",
         visual=f"{OFF}, sitting at the writing desk, the open laptop angled away from the viewer so its screen is not visible, its cold glow on her face, her expression suddenly changing to tense surprise",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="home_night"),
    dict(to=37, reason="action change: she phones Zee about PictureLand and her pen name WhiteLily", chars=["noorin"], loc="apartment",
         visual=f"{OFF}, sitting at the desk holding a phone to her ear, speaking firmly with an irritated frown, her other hand raised palm-up in exasperation, the laptop beside her angled away from the viewer",
         camera=f"medium close-up, eye level, {LOW} (desk top)", amb="home_night"),
    dict(to=38, reason="character change: Zee on the other end of the line", chars=["zee"], loc="zee_office",
         visual="Zee sitting at her desk holding a phone to her ear, leaning forward with an earnest, coaxing expression, a stack of bound script pages with blank covers on the desk in front of her",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="office_night"),
    dict(to=39, reason="back to Noorin on the phone", reuse="beat_013", loc="apartment", chars=["noorin"],
         visual="reuse of beat_013", amb="home_night"),
    dict(to=41, reason="emotional turning point: she sees Uvaish's name in the business news and shuts the laptop", chars=["noorin"], loc="apartment",
         visual=f"close-up of {OFF}, pressing the laptop lid shut with her palm, her face hardened and cold, jaw tight, eyes burning with old pain, the last glow of the screen fading; the screen itself is not visible",
         camera=f"close-up, eye level, {LOW} (the closed laptop on the desk)", amb="home_night"),
    dict(to=44, reason="scene change: a case — a girl rushed to hospital (shown only as the ambulance outside)", loc="case_house",
         visual="an ambulance with flashing red and blue lights parked outside the small house at night, its rear doors open, two paramedics in uniform seen from behind hurrying in through the lit front door, a few neighbours watching from across the wet street; nobody else visible",
         camera="wide shot from across the street, eye level, the house and ambulance in the upper two-thirds, the wet reflective road as the calm lower third",
         amb="night_exterior", transition="black", sens="violence",
         safe="the girl, her wrist, any blood or cloth are never shown; only the ambulance lights and paramedics' backs at the door, seen from far"),
    dict(to=48, reason="character change: Noorin notices the girl's sobbing mother and walks to her", chars=["noorin"], loc="case_living",
         visual=f"a Maldivian mother in her forties in a loose long-sleeved dark-green dress and a grey hijab fully covering her hair, sitting on the sofa bent forward with her face in her hands, sobbing; {UNI} standing a few steps away, looking at her with a grave, controlled expression",
         camera=f"medium wide shot, eye level, {LOW} (woven rug)", amb="living_night"),
    dict(to=51, reason="framing change: the mother's plea — what people would say, where could she go", chars=["noorin"], loc="case_living",
         visual="the mother on the sofa looking up with red, tear-filled eyes, her hands clasped together in a pleading gesture, speaking through sobs; Noorin's dark-navy uniformed shoulder and black hijab soft and out of focus in the foreground, her face turned away",
         camera=f"medium close-up on the mother over Noorin's shoulder, eye level, {LOW}", amb="living_night"),
    dict(to=55, reason="framing change: Noorin's stern rebuke of the mother", chars=["noorin"], loc="case_living",
         visual=f"close-up of {UNI}, speaking firmly with stern, disappointed eyes, slightly shaking her head, the mother blurred on the sofa behind her",
         camera=f"close-up, eye level, {LOW}", amb="living_night", hum=True),
    dict(to=59, reason="scene change: Noorin sits alone at her office desk, old wounds reopened", chars=["noorin"], loc="office",
         visual=f"{UNI} sitting alone at her office desk, hands folded on the desk, back straight, her face composed and serious but her eyes heavy with old pain, stacked folders beside her",
         camera=f"medium shot, eye level, {LOW} (desk top)", amb="office_day", transition="black"),
    dict(to=63, reason="symbolic detail: the children's voices she has heard in her cases (no child shown)", loc="classroom",
         visual="an empty small wooden school desk and chair by a large rain-streaked window, a small child's school bag resting alone against the desk leg, raindrops running down the glass; no people",
         camera="medium shot, eye level, the window and desk in the upper two-thirds, the plain floor as the calm lower third",
         amb="rain_day", transition="dissolve", sens="other",
         safe="the child's confession about 'something friends gave' is never shown: no child, no drugs, no pills, no smoke; only an empty desk and a school bag by a rainy window"),
    dict(to=66, reason="symbolic detail: the child's sleepless, frightened nights (no child shown)", loc="child_room",
         visual="a little study desk in a dim child's room at night with closed schoolbooks and a small glowing desk lamp, a small school bag hanging on the chair, the dark window streaked with rain; no people",
         camera="medium shot, eye level, the desk and window in the upper two-thirds, the floor in soft shadow as the calm lower third",
         amb="room_night", sens="other", safe="no child shown; symbolic empty study desk at night"),
    dict(to=68, reason="back to Noorin: she covers her ears to shut out the voices", chars=["noorin"], loc="office",
         visual=f"{UNI} at her office desk with both hands pressed over her ears, eyes squeezed shut, head turned slightly as if shaking off voices, anguish breaking through her composure",
         camera=f"medium close-up, eye level, {LOW} (desk top)", amb="office_day", transition="dissolve", hum=True),
    dict(to=69, reason="scene change: her work with young offenders; she walks into the prison", chars=["noorin"], loc="prison_corridor",
         visual=f"{UNI} walking purposefully down the narrow prison corridor away from the camera towards a barred cell door that a male prison officer in uniform holds open ahead of her, an arm's-length gap between them",
         camera="medium wide shot, eye level, down the corridor, the figures in the upper two-thirds, the polished concrete floor as the calm lower third",
         amb="detention_room", transition="black"),
    dict(to=74, reason="action change: the smirking offender across the table taunts her", chars=["noorin"], loc="prison_cell",
         visual=f"a smirking middle-aged Maldivian man in a plain grey long-sleeved prison shirt and grey trousers sitting back in a metal chair with his arms folded and a mocking grin; {UNI} standing on the other side of the small metal table, the table and a clear arm's-length gap between them, looking down at him coldly",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (bare concrete floor)", amb="detention_room"),
    dict(to=78, reason="emotional turning point: her fury breaks loose (the strikes are never shown)", chars=["noorin"], loc="prison_cell",
         visual=f"close-up of {UNI}, her face in cold fury, jaw clenched, eyes blazing, one hand pressed flat on the metal table; the offender only a blurred grey shape far across the table behind her",
         camera=f"close-up, slightly low angle, {LOW} (table top)", amb="detention_room", sens="violence",
         safe="the two strikes and his reaction are never shown: only her furious face before, with muffled offscreen thuds; he never touches her on screen"),
    dict(to=83, reason="action change: officers rush in and move the offender away; she calmly reveals it was recorded and leaves", chars=["noorin"], loc="prison_cell",
         visual=f"two male police officers in uniform stepping in and steering the offender (grey prison shirt) away to the far side of the cell by his arms; {UNI} standing composed on the other side of the room, straightening her uniform collar, a faint cold mocking smile; the small security camera with a red light high in the corner; nobody is hurt",
         camera=f"medium wide shot, eye level, {LOW} (concrete floor)", amb="detention_room", sens="violence",
         safe="aftermath only: officers between them, Noorin composed, no injury, no handcuffs"),
    dict(to=84, reason="scene and time change: leaving the court with other officers, she suddenly stops", chars=["noorin"], loc="court",
         visual=f"{UNI} walking down the court steps with two male police officers in uniform towards the white police vehicle, an arm's-length gap between her and them, suddenly stopping mid-step, her eyes fixed on someone ahead",
         camera=f"medium wide shot, eye level, {LOW} (sunlit paving)", amb="city_day", transition="black"),
    dict(to=85, reason="character change: Aakif sees her from a distance, overjoyed", chars=["aakif"], loc="court",
         visual="Aakif standing completely alone in the middle of the open sunny court forecourt, nobody near him and nobody in the foreground, staring into the distance with wide eyes and parted lips, overwhelmed wonder and joy in his face as if he has found a long-lost jewel, palm trees and traffic far behind him",
         camera=f"medium shot, eye level, {LOW} (sunlit paving)", amb="city_day", hum=True),
    dict(to=86, reason="action change: she puts on sunglasses, ignores him and gets into the vehicle", chars=["noorin"], loc="court",
         visual=f"{UNI} sliding on dark sunglasses with an expressionless face as she walks alone towards the white police vehicle and reaches for its open passenger door herself; two male officers already walking to the far side of the vehicle several steps away from her, a wide gap between them",
         camera=f"medium shot, eye level, {LOW} (sunlit road)", amb="city_day"),
    dict(to=88, reason="back to Aakif: he thinks he imagined her", reuse="beat_030", chars=["aakif"], loc="court",
         visual="reuse of beat_030", amb="city_day"),
    dict(to=92, reason="scene change: inside the moving vehicle she looks back at Aakif in the side mirror", chars=["noorin"], loc="car",
         visual=f"{UNI} in the passenger seat of the moving police vehicle, holding her sunglasses in one hand, looking into the side mirror with a guarded, unreadable, faintly sad expression; in the mirror a small distant figure of a man in black on the sunny road",
         camera=f"medium close-up from inside the vehicle, eye level, {LOW} (dashboard in soft shade)", amb="car_interior"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With the flash of lightning the whole sky echoed with the roar of thunder. The darkened sky looked as if it were furious.",
   [("thunder", "ގުގުރީގެ", -14)])
sh(2, "As black clouds closed over the sky, the lightning and thunder grew ever stronger.",
   [("thunder", "ގުގުރުމުގެ", -16)])
sh(3, "The chaos on the road grew extreme; the streets were jammed with vehicles and people going in every direction.",
   [("car_pass", "އުޅަނދުފަހަރާއި", -22)])
sh(4, "At this time of night the roads are usually busy anyway, and when heavy rain began to fall, many people ran to shelter under the shop awnings.",
   [("rain_start", "ވާރޭ", -18)])
sh(5, "Waiting for the rain to stop, among the people sheltering under an awning, stood Noorin too.")
sh(6, "Her face showed unease and deep distress. The tears falling from her eyes, red and swollen from crying,",
   [("sob_breath", "ރޮއިރޮއި", -24)])
sh(7, "were mixing with the raindrops running down her face. She was now certain that there was no one in this world who would feel for her helpless state.",
   hum=True)
sh(8, "After her father left, she had escaped from her cruel stepmother's hands and come to her birth mother, full of sweet, joyful hopes.")
sh(9, "But the few days she was able to spend in her mother's house became a great battle she had to fight to protect her own honour and dignity.")
sh(10, "However much her mother loved her, Noorin understood that there was nothing her mother could do. And Noorin did not want to destroy the complete trust and respect her mother had for her stepfather.")
sh(11, "So she hid the pain in her heart in front of her mother and buried that bitter truth in the deepest part of her heart.")
sh(12, "Thanks to her alertness she had escaped her stepfather's traps, but how long could she endure such a dangerous battle?")
sh(13, "In the end, to save her own honour, even though it would break her mother's heart, she left that house crying and sobbing.",
   [("door_close", "ނުކުތީއެވެ", -20), ("sob_breath", "ގިސްލަމުން", -24)], hum=True)
sh(14, "But where could she go on this dark night? She had no direction, no destination to go to.")
sh(15, "As the rain eased, the people under the awning began to leave in different directions. But Noorin, with nowhere left to turn,",
   [("footsteps_pavement", "ދާން", -24)])
sh(16, "stood where she was like a statue, without moving. When the clock struck eleven at night, the shops closed and the street began to fall silent.",
   [("metal_door", "ބަންދުކޮށް", -22)])
sh(17, "Exhausted and wretched, Noorin slowly went and sat down at the side of the road. The rain was still pouring.",
   [("footsteps_pavement", "ގޮސް", -24)])
sh(18, "The clothes she wore were soaked through, and her body shivered in the cold gusts of wind. Her head aching from thinking and thinking, Noorin's eyes slowly closed,",
   [("wind_gust", "ވައިރޯޅިތަކުން", -20)])
sh(19, "and she fainted. But before her head struck the ground, she fell against the feet of a man standing beside her.",
   [("soft_thud", "ވެއްޓުނެވެ", -22)], hum=True)
sh(20, "It was as if that man had been standing there waiting for just such a moment. At once he bent down and lifted Noorin in his strong arms.")
sh(21, "When Noorin came to, she found herself in a completely unfamiliar place. A pleasant fragrance filled her nose.",
   [("breath", "ހޭލެވުނުއިރު", -22)])
sh(22, "When she sat up from the bed with a start, she noticed she was wearing clean, changed clothes.",
   [("gasp", "ސިހިފައި", -20)])
sh(23, "Looking around with an unknown fear, there was no trace of anyone. It was a room decorated to perfection, in a modern style.")
sh(24, "As she tried to get up her head spun a little, but she could not remember anything that had happened in the night.")
sh(25, "When she saw her bag beside the wardrobe next to the bed, she gathered her courage, went over, opened the bag and looked inside.",
   [("cloth_rustle", "ހުޅުވައި", -22)])
sh(26, "Everything in it was as it had been. Her mind full of questions, Noorin looked around the room once again. \"Whose house is this?")
sh(27, "How did I come to be here?\" The questions piled up in Noorin's heart. But without thinking for long,")
sh(28, "after writing a short note in the notebook lying on the desk, she wasted no time: she took her bag and hurried out of that place.",
   [("pen_scribble", "ލިޔެލުމަށް", -20), ("door_close", "ނުކުމެގެން", -22)])
sh(29, "Twelve years later. Opening the door of the room, Noorin stepped inside. Before changing out of the police uniform she was wearing,",
   [("door_open", "ހުޅުވާލުމަށް", -20)])
sh(30, "she took off the cap on her head and placed it neatly on the table. Then, stopping in front of the mirror, she ran her eyes over her uniform.",
   [("cloth_rustle", "ނަގައި", -24)])
sh(31, "And she touched the two stars shining on her shoulder. The promotion she received today was the sweet result of the patience and hard work of the past days.")
sh(32, "Having been made an Inspector, today she felt truly proud of herself. After a shower she came out refreshed,")
sh(33, "opened her laptop and began to look through the e-mails that had arrived. Suddenly the colour of Noorin's face changed.",
   [("keyboard_typing", "ލެޕްޓޮޕް", -22)])
sh(34, "Quickly she picked up the phone lying on the desk and dialled a number. \"Hello! PictureLand has mailed again.")
sh(35, "I've already told them clearly that I can't give my real name. What is the problem with it being under the name 'WhiteLily'?")
sh(36, "I write scripts under the name WhiteLily, and that name can't be changed. If they want to buy the script they should buy it,")
sh(37, "if not, let it go. I have no problem at all.\" Noorin said, unsettled.")
sh(38, "\"They want to enter the film 'Rihun' in the film festival,\" came the voice from the other end of the phone. \"Zee!")
sh(39, "I can't talk much more about this. Tell them that if they want to enter it in the festival, they can do it under the name 'WhiteLily'.")
sh(40, "I don't want to argue any more.\" Saying this, Noorin hung up. Then she began to look at the day's news. Among the business news,")
sh(41, "on seeing the name \"Uvaish\" printed in big bold letters, every expression on Noorin's face changed.", hum=True)
sh(42, "Disturbed, she shut the laptop at once. A girl lay fallen beside a bed. Because a vein in her wrist had been cut,",
   [("soft_thud", "ލައްޕައިލިއެވެ", -18)])
sh(43, "a pool of blood was forming on the floor where she lay. People were tying a cloth around the girl's arm,")
sh(44, "working without pause to stop the bleeding. When the girl was rushed to hospital for urgent treatment,",
   [("siren", "ހޮސްޕިޓަލަށް", -20)])
sh(45, "Noorin's gaze fell on the girl's mother, standing to one side sobbing and crying. Noorin slowly walked towards the woman.",
   [("sob_breath", "ގިސްލާ", -22)])
sh(46, "\"Why didn't you stop it when something this serious was going on?\" Noorin asked calmly. At that,")
sh(47, "the woman's crying grew louder. \"Crying is no use now. What has passed can't be undone.",
   [("sob_breath", "ރުއިމުގެ", -22)])
sh(48, "A mother cannot fail to feel the pain and sorrow in her child's heart. The bond of motherhood is far stronger, a special bond.\"")
sh(49, "Noorin said with sympathy. \"I know everything. But for fear of what people would say... and even otherwise, where would I go with my daughter?")
sh(50, "Who would help us?\" the woman said, sobbing. \"For fear of what people would say, you left the child born of your own womb on the lips of death?",
   [("sob_breath", "ގިސްލަމުން", -24)])
sh(51, "She took such a dangerous step because she could not bear the torment she was suffering.")
sh(52, "You could have taken your daughter and lived an honourable life, protecting your own dignity and honour. All that takes is a little courage.")
sh(53, "In the name of finding her a father's love, why did you leave the child in the traps of a man who is like a beast?")
sh(54, "Mothers must know the sorrows in their children's hearts. Protecting those children is the greatest responsibility placed on a parent's shoulders.")
sh(55, "Why did you forget that responsibility?\" Noorin shook her head in despair.",
   [("sigh", "ހޫރައިލިއެވެ", -22)], hum=True)
sh(56, "The woman sat with her head bowed, sobbing on. On entering her office, Noorin sat down at her desk.",
   [("sob_breath", "ގިސްލަމުން", -24)])
sh(57, "Even she could not grasp the truth of the storm whirling in her mind. Today, once again, the wounds of her heart had opened fresh and ached.")
sh(58, "The bitter memories of her youth passed before her eyes. Not letting the pain and anguish rising in her heart show on her face,")
sh(59, "though she always showed a firm, serious manner, that heart was breaking into pieces.")
sh(60, "The cases of crimes against children increasing day by day was something that worried her deeply.")
sh(61, "How can such inhuman acts be stopped? Why do some people cast humanity aside and live like beasts?")
sh(62, "The sentences those innocent children had spoken kept echoing in Noorin's ears. \"Mum and Dad's quarrels, the other kids' mockery,")
sh(63, "the teachers' punishments... to escape from all of it I used something my friends gave me. When I use it my heart feels very calm.")
sh(64, "I can't hear any sound, my mind feels light!\" The sound of that child's sobbing could be heard. \"How am I supposed to learn my lessons?",
   [("sob_breath", "ގިސްލުމުގެ", -24)])
sh(65, "My mind can't think of anything. At night I can't sleep from fear. When I fall asleep it starts to hurt. Even when I'm told not to, I keep doing it again and again.")
sh(66, "How am I supposed to study? Nothing I study stays in my head. Even if I tell someone, no one believes me.")
sh(67, "There's no one who feels my pain and anguish.\" As those painful voices echoed in Noorin's ears,", hum=True)
sh(68, "she covered both ears with her hands and shook her head to get away from those voices. Helping the young offenders brought there,",
   [("heartbeat", "ކަންފަތުގައި", -20)])
sh(69, "Noorin always works extremely hard to make those children useful members of society. Noorin went into the prison cell.",
   [("metal_door", "ވަދެގެން", -18)])
sh(70, "And she looked at the middle-aged offender standing before her with a mocking smile.")
sh(71, "\"People like you should be kept in a pen with the beasts. You are a low kind with no trace of humanity.")
sh(72, "Human beings have noble, kind hearts. But...\" Noorin's words were cut off. \"But what can be done?")
sh(73, "Don't you know we men have our desires? Did you think I'd be afraid because you came before me wearing a uniform?")
sh(74, "Whatever clothes they wear, women are still just women. You lot are there to satisfy our desires,\" the offender said in a scornful tone.")
sh(75, "Hearing those vile words, Noorin's anger slipped out of control. Without waiting any longer,", hum=True)
sh(76, "she swung a powerful blow at the man's face, and blood ran from his mouth. At that,",
   [("soft_thud", "ވީއްލައިލި", -22)])
sh(77, "in pain and rage the man began to shout filthy words at Noorin. A second time Noorin swung a hot blow at the side of his head.",
   [("soft_thud", "ވީއްލައިލިއެވެ", -22)])
sh(78, "At that, the man turned on her in fury, struck Noorin in the face and grabbed the collar of her uniform.",
   [("soft_thud", "ޖަހައި", -24), ("cloth_rustle", "ހިފިއެވެ", -22)])
sh(79, "At once the police officers outside came in and pulled the man away. A mocking smile settled on Noorin's lips.",
   [("metal_door", "ވަދެ", -18)])
sh(80, "\"Don't even dream of getting out of this place now! Whatever a woman can do, you won't get help from any man now. For a question",
   )
sh(81, "I asked, you laid hands on a police officer's uniform without any right and struck me. Do you know the penalty for assaulting a senior officer?\"")
sh(82, "Noorin said in a calm tone. \"Where's your proof of that?\" the man replied stubbornly. \"Not enough witnesses?")
sh(83, "There's a recording of the whole scene too.\" Utterly calm, Noorin walked out of the place.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(84, "Coming out of the court, as she walked with the other officers towards the police vehicle, a face she saw ahead brought Noorin's steps to a sudden stop.",
   [("footsteps_pavement", "ދަނިކޮށް", -24)])
sh(85, "On that man's face was joy of the highest degree. It was as if he had found a precious jewel lost for ages. But",
   hum=True)
sh(86, "Noorin paid it no attention at all; putting on her sunglasses she walked on. And talking with the officers, she got into the vehicle.",
   [("car_door", "އެރިއެވެ", -18)])
sh(87, "Stunned by the sight, the man said to himself: \"That was Noorin herself... but Noorin in a police uniform?")
sh(88, "No, I must have imagined it. Noorin is far weaker than that,\" Aakif told himself. As the vehicle drove off,",
   [("car_drive_off", "ދުއްވާލުމާއެކު", -18)])
sh(89, "Noorin took off her glasses and looked at Aakif in the side mirror. Today she had no wish to treat Aakif as someone she knew.")
sh(90, "Twelve years ago she had erased from her memory Aakif, who had shared an important chapter of her life.")
sh(91, "Their world and hers were two completely different worlds. She has devoted her whole life to the service of her nation and her religion.")
sh(92, "In that heart there is no room at all for the feelings of worldly love.", hum=True)
SHOTS = S

"""Beat/shot plan for Noorin episode 503 (final episode of the batch; used by plan_beats.py)."""

OFF = ("Noorin is NOT in uniform here: she wears a loose long-sleeved ankle-length deep-plum abaya-style dress and a "
       "black hijab wrapped snugly and fully covering her hair and neck, no beret, no cap, no badges, no stars")
OFF2 = ("IMPORTANT: Noorin is at home, off duty: use her reference image ONLY for her face; she is NOT wearing the police "
        "uniform, NO beret, NO cap, no epaulettes, no stars, no belt; instead she wears a loose long-sleeved ankle-length "
        "deep-plum abaya-style dress and a plain black hijab wrapped snugly and fully covering her hair and neck")
GAP = "a clear arm's-length gap between them, nobody touching"

LOC = {
    "corridor": "the bright tiled common corridor of a modern mid-rise apartment building in Malé, two neighbouring plain wooden apartment doors side by side, a white wall, a window at the far end with tropical morning light",
    "street": "a narrow sunny Malé street outside a modern mid-rise apartment building, pastel buildings, parked scooters, a few palm fronds, the building's glass entrance at the side",
    "crime": "the luxurious top-floor office of a famous businessman in Malé after a break-in: a glass partition wall shattered with glittering glass shards scattered on the dark marble floor, a heavy steel wall safe standing open and empty, files and loose papers scattered across the floor, a large executive desk, tall windows over the city",
    "uvaish_home": "the luxurious modern sitting room of Uvaish's penthouse in Malé, a long dark leather sofa, a low glass coffee table, a floor lamp, tall dark windows with distant city lights",
    "flash_room": "a small plain rented room twelve years earlier, a simple wooden chair beside a small open window with a thin white curtain, a bare whitewashed wall",
    "flash_office": "a simple sunlit resort site office twelve years earlier, a wooden desk with neat plain folders, rattan blinds, a view of coconut palms and turquoise water",
    "uvaish_window": "Uvaish's dark penthouse beside a floor-to-ceiling window overlooking the night lights of Malé and the dark sea",
    "police_office": "Inspector Noorin's plain office at police headquarters in Malé: pale walls, a dark wooden desk with a closed laptop and neat plain folders, two visitor chairs, a grey filing cabinet, a small side desk with a computer monitor turned away from the viewer, window blinds, no flags, no emblems, no signs",
    "home_eve": "Noorin's modest modern apartment living room in Malé: cream walls, a grey fabric sofa and a matching armchair, a small wooden coffee table, a tall window with sheer curtains, a small desk with a desktop computer, the front door at the side",
    "home_night": "the corner of Noorin's apartment living room late at night: a small desk with a desktop computer and keyboard by a tall window with sheer curtains, rain streaking the dark glass",
    "doorway": "the front door of Noorin's apartment at night during a heavy storm, the door opening onto an open-air walkway of the apartment building, rain blowing in sheets beyond the railing, a wet tiled floor",
    "memory": "a hazy remembered empty hotel corridor twelve years earlier, a row of closed wooden doors, dim wall lamps, rain on a window at the far end",
}
MOOD = {
    "corridor": "morning, bright clean daylight from the end window, cool teal shadows, a charged surprised silence",
    "street": "morning, bright tropical sunlight with cool blue shadows, brisk and determined, a touch of longing",
    "crime": "daytime, cool grey daylight from the tall windows, a bright white camera flash, tense and procedural",
    "uvaish_home": "late night, a single warm amber floor lamp and the cold blue glow of a phone, deep navy shadows, lonely and remorseful",
    "flash_room": "twelve years earlier, warm soft golden haze, fading dusk light through the curtain, fragile, wounded and resolute",
    "flash_office": "twelve years earlier, warm soft golden haze, bright afternoon sun through rattan blinds, a heavy revelation",
    "uvaish_window": "night, the cold blue glow of the city through the glass, deep navy shadows, years of lonely longing",
    "police_office": "late afternoon, warm slanting sunlight through window blinds striping the room, cool navy shadows, cold, controlled tension",
    "home_eve": "early evening after sunset, a single warm table lamp against deep blue dusk at the window, quiet, heavy and lonely",
    "home_night": "late night, the cool glow of the computer screen and a warm desk lamp, rain on the window, sudden white lightning, lonely",
    "doorway": "stormy night, cold blue rain light and lightning outside, warm amber light from inside the apartment, raw emotion",
    "memory": "twelve years earlier, warm soft golden haze turned cold and blurred, a bitter dreamlike memory, soft vignette",
}

BEATS = [
    dict(to=5, reason="new episode opening: Noorin and Aakif step out of neighbouring apartments at the same moment", chars=["noorin", "aakif"], loc="corridor",
         visual=f"two neighbouring apartment doors side by side; Noorin in uniform has just stepped out of the left door and stopped in surprise; Aakif has just stepped out of the right door and stands still, staring at her, deeply moved; {GAP}, more than two metres apart, both faces in the upper part of the frame",
         camera="medium wide two-shot, eye level, the tiled floor forming a calm lower third", amb="home_day"),
    dict(to=8, reason="focus change: Aakif tells her about his training and his new strength", chars=["aakif", "noorin"], loc="corridor",
         visual=f"medium close-up of Aakif in the corridor, strong and composed, speaking with intense calm conviction, his gaze fixed on Noorin; Noorin at the edge of the frame in the soft-focus foreground seen from behind her shoulder (black hijab and black beret), {GAP}",
         camera="over-the-shoulder medium close-up on Aakif", amb="home_day"),
    dict(to=13, reason="emotional turning point: Aakif declares his love, Noorin coldly refuses", chars=["noorin", "aakif"], loc="corridor",
         visual=f"Noorin in uniform standing on the left side of the frame, her face cold and composed, turned slightly away from him, a pair of dark sunglasses folded in one hand; Aakif standing on the right side of the frame, a wide empty stretch of corridor about two metres wide between them, having stepped a little closer but keeping his distance, looking at her tenderly and earnestly; {GAP}",
         camera="medium wide two-shot side by side across the frame, eye level", amb="home_day"),
    dict(to=15, reason="scene and action change: Noorin rides off on her police motorbike while Aakif watches", chars=["noorin", "aakif"], loc="street",
         visual="Noorin in her dark-navy uniform wearing dark sunglasses and a black open-face motorcycle helmet over her black hijab, seated upright on a plain white-and-navy police motorbike with no lettering, pulling away down the street; far behind her at the glass entrance of the building Aakif stands still, watching her go with a wistful knowing look",
         camera="medium wide, low angle, the sunlit road surface as a calm lower third", amb="road_busy"),
    dict(to=17, reason="scene change: the break-in at a famous businessman's office; Noorin studies the scene", chars=["noorin"], loc="crime",
         visual="Noorin in uniform standing in the wrecked office, leaning slightly forward with a sharp focused gaze, studying the scattered files and the open empty safe; a male police photographer in a navy uniform takes a picture with a camera, a bright white flash lighting the glittering glass shards on the floor; nobody is hurt, no people on the floor",
         camera="medium wide, eye level, the glass-strewn marble floor as the lower third", amb="office_day", sens="violence",
         safe="crime scene shown only as shattered glass, an open safe and scattered files with a photographer's flash; nobody hurt (bible rule 12)"),
    dict(to=19, reason="character enters: Uvaish walks in and is stunned to see her as a strong officer", chars=["uvaish", "noorin"], loc="crime",
         visual=f"Uvaish in his charcoal suit has just walked in through the office doorway and stopped mid-step, stunned, staring across the room; in the foreground Noorin in uniform stands firm and upright, seen in three-quarter view from behind; {GAP}, several metres apart",
         camera="medium wide, from behind Noorin's shoulder towards the doorway", amb="office_day"),
    dict(to=23, reason="action change: the secretary's question, Noorin's cold answer and her order to Jinaah", chars=["noorin", "uvaish"], loc="crime",
         visual=f"Noorin in uniform standing tall in the wrecked office giving a cold, firm look, speaking with authority; beside her a male police officer, Jinaah (Maldivian man of about 30, dark-navy police uniform and navy cap, holding a small notebook), listening attentively; a few steps away Uvaish in his charcoal suit and his secretary (a young Maldivian man of about 30 in a white long-sleeved shirt and grey trousers) look at her in surprise; {GAP}",
         camera="medium wide group shot, eye level", amb="office_day"),
    dict(to=26, reason="action change: sunglasses on, she passes Uvaish, pauses and turns her face to him", chars=["noorin", "uvaish"], loc="crime",
         visual=f"Noorin in uniform wearing dark sunglasses, having just walked past Uvaish, pausing and slowly turning her head back over her shoulder towards him with a cold, faintly mocking expression; Uvaish behind her stands stiff and wounded, more than an arm's length away; {GAP}",
         camera="medium close two-shot, Noorin in front, eye level", amb="office_day"),
    dict(to=28, reason="scene and time change: Uvaish alone at home at night reading her old message", chars=["uvaish"], loc="uvaish_home",
         visual="Uvaish alone on the long leather sofa, jacket off, white shirt, leaning forward with his phone held in both hands, reading; the phone screen faces away from the viewer and its cold glow lights his sad, worn face",
         camera="medium shot, eye level, the glass coffee table as the lower third", amb="living_night", transition="black"),
    dict(to=31, reason="flashback: twelve years ago young Noorin writes her farewell message", chars=["noorin_young"], loc="flash_room",
         visual="twelve years earlier: young Noorin, about 22, sitting alone on a simple wooden chair beside the small window, typing a message on her phone with both thumbs, the phone screen turned away from the viewer; her face is pale, her eyes red and wet, her lips pressed together in quiet resolve",
         camera="medium shot, eye level, slightly from the side", amb="memory", transition="dissolve", hum=True),
    dict(to=34, reason="back to the present: Uvaish breaks down in tears over the message", chars=["uvaish"], loc="uvaish_home",
         visual="close-up of Uvaish on the sofa, head bowed over the glowing phone in his hand (screen turned away from the viewer), tears running down his cheeks, his other hand pressed against his forehead, shoulders shaking",
         camera="close-up, eye level", amb="living_night", transition="dissolve"),
    dict(to=37, reason="flashback: three months after that night, Aakif tells Uvaish the truth", chars=["aakif_young", "uvaish_young"], loc="flash_office",
         visual="twelve years earlier: young Aakif, about 24, with glasses and a light-blue shirt, standing across the desk speaking earnestly, one open hand raised as he explains; young Uvaish, about 26, clean-shaven, in a white linen shirt, half-risen from his chair behind the desk, stunned, the colour drained from his face as the truth hits him",
         camera="medium wide two-shot across the desk, eye level", amb="memory", transition="dissolve"),
    dict(to=41, reason="time passage: years of Uvaish's lonely longing for Noorin and the child", chars=["uvaish"], loc="uvaish_window",
         visual="Uvaish in his charcoal suit standing alone at the floor-to-ceiling window at night, seen in three-quarter view from behind so his sad profile shows, looking out over the city lights and the dark sea, his phone hanging loosely in one hand, his shoulders heavy with longing",
         camera="medium wide, eye level, the dark polished floor as the lower third", amb="city_night_far", transition="dissolve"),
    dict(to=46, reason="scene and time change: one afternoon Uvaish's lawyer comes to Noorin's office", chars=["noorin", "uvaish_lawyer"], loc="police_office",
         visual="Noorin in uniform seated behind her desk, leaning back, one eyebrow raised and a faint mocking smile on her lips; across the desk Uvaish's lawyer sits upright in a visitor chair with a leather briefcase on his knees, speaking coolly; the desk between them",
         camera="medium wide, eye level, the desk top as the lower third", amb="office_quiet", transition="black"),
    dict(to=49, reason="time change: the next day Uvaish and the lawyer arrive while a clerk types a report", chars=["noorin", "uvaish", "uvaish_lawyer"], loc="police_office",
         visual="Noorin in uniform standing behind her desk, gesturing politely and coldly towards the two visitor chairs; Uvaish and his lawyer sitting down across the desk; at the small side desk a young female clerk (Maldivian woman of about 24, light-grey long-sleeved blouse, long dark skirt, navy hijab fully covering her hair and neck) pauses at her keyboard, the monitor turned away from the viewer; the desk keeps a clear gap between Noorin and the men",
         camera="medium wide, eye level", amb="office_quiet", transition="black"),
    dict(to=51, reason="action change: Noorin drops the file on the desk; the lawyer reads it", chars=["uvaish_lawyer", "uvaish", "noorin"], loc="police_office",
         visual="the lawyer holding open a plain beige file and reading, its pages showing only blurred grey lines with no readable text; Uvaish beside him leaning in, worried; Noorin standing behind the desk with her arms folded, cold and still; the desk between them",
         camera="medium shot over the desk, eye level", amb="office_quiet", sens="other",
         safe="the file's content (the baby's loss) is never shown: blurred pages only (bible rule 13)"),
    dict(to=54, reason="emotional turning point: Uvaish learns what happened to the child", chars=["uvaish"], loc="police_office",
         visual="close-up of Uvaish seated in the visitor chair, his face drained of colour, eyes brimming with tears, looking up across the desk in shattered disbelief; the lawyer's shoulder blurred at the edge of the frame",
         camera="close-up, eye level", amb="office_quiet", hum=True),
    dict(to=57, reason="focus change: Noorin confirms the report, then confronts the lawyer", chars=["noorin", "uvaish_lawyer"], loc="police_office",
         visual="Noorin in uniform standing behind her desk, upright, her face fierce and controlled, speaking firmly towards the lawyer who sits in the soft-focus foreground seen from behind; in the background the young female clerk in her navy hijab gives a small nod from the side desk",
         camera="medium shot, slightly low angle, from behind the lawyer's shoulder", amb="office_quiet", sens="violence",
         safe="the harm and the miscarriage are dialogue only; shown as Noorin's controlled fierce face"),
    dict(to=61, reason="emotional turning point: Noorin closes her tear-filled eyes; the room stares; Uvaish frozen", chars=["noorin", "uvaish", "uvaish_lawyer"], loc="police_office",
         visual="Noorin in uniform standing behind the desk with her eyes closed and her chin raised, a single tear on her cheek, holding back her emotions; across the desk Uvaish sits frozen and speechless, staring at her; the lawyer and the young female clerk in her navy hijab watch her in silence; the desk keeps a clear gap",
         camera="medium wide, eye level", amb="office_quiet", hum=True),
    dict(to=64, reason="action change: Noorin pronounces his punishment and walks out", chars=["noorin", "uvaish"], loc="police_office",
         visual=f"Noorin in uniform walking out through the office doorway, upright, her back half turned, not looking back; behind her in the room Uvaish still sits in the visitor chair, head bowed, hands clasped in despair; {GAP}",
         camera="medium wide, from inside the room towards the doorway", amb="office_quiet"),
    dict(to=66, reason="scene and time change: Noorin alone at home in the evening, hope gone", chars=["noorin"], loc="home_eve",
         visual=f"{OFF}; she sits alone on the grey sofa in the lamplit living room, a closed plain paper folder on her lap, staring at nothing with a numb, empty sorrow",
         camera="medium shot, eye level, the coffee table as the lower third", amb="room_night", transition="black"),
    dict(to=69, reason="detail image: she opens the doctors' report and the scans and weeps", chars=["noorin"], loc="home_eve",
         visual=f"{OFF}; close view from slightly above of Noorin bent over the open folder on her lap, her fingertips tracing two dark grey ultrasound scan prints showing only soft abstract fan-shaped grey patterns, a report page with only blurred grey lines beside them, no readable text, no numbers; her lowered face in the upper part of the frame, tears falling silently",
         camera="close medium shot from slightly above", amb="room_night", hum=True, sens="other",
         safe="the medical report and scans show no readable text and only abstract grey shapes"),
    dict(to=71, reason="characters enter: Reem and her husband Naaif at the door", chars=["noorin", "reem"], loc="home_eve",
         visual=f"{OFF2}; Noorin holding the front door open, her eyes still slightly red, surprised; on the threshold stand Reem, now about 34, with a gentle hesitant smile, and beside Reem her husband Naaif (Maldivian man of about 36, short black hair, short neat beard, light-grey long-sleeved shirt, dark trousers); a clear arm's-length gap between Noorin and Naaif, nobody touching",
         camera="medium wide, from inside the apartment towards the door", amb="living_night"),
    dict(to=75, reason="action change: they sit down; Reem introduces Naaif and explains her marriage", chars=["reem"], loc="home_eve",
         visual=f"in the lamplit living room Reem, about 34, and her husband Naaif (short black hair, short neat beard, light-grey long-sleeved shirt) sit side by side on the grey sofa; Reem leans forward speaking earnestly; in the armchair opposite sits Noorin, a slim Maldivian woman of about 34 with warm brown skin, an oval face, large dark almond-shaped eyes and straight dark eyebrows, silent and stunned, at home and off duty: she wears a loose long-sleeved ankle-length deep-plum abaya-style dress and a plain black hijab wrapped snugly and fully covering her hair and neck, no uniform, no beret, no cap; the coffee table between them keeps a clear gap",
         camera="medium wide, eye level, the coffee table as the lower third", amb="living_night"),
    dict(to=78, reason="focus change: Reem pleads that Uvaish still loves only Noorin", chars=["reem"], loc="home_eve",
         visual="medium close-up of Reem, about 34, on the sofa, leaning forward with sincere, pleading eyes and one hand open in front of her as she speaks; her husband Naaif sits beside her in soft focus, nodding quietly",
         camera="medium close-up, eye level", amb="living_night"),
    dict(to=82, reason="emotional turning point: Noorin's outburst — she bore the pain alone; it is too late", chars=["noorin", "reem"], loc="home_eve",
         visual=f"{OFF2}; Noorin sitting forward in the armchair, her eyes wet and blazing, one hand pressed flat to her own chest as she speaks with passion and pain; Reem in soft focus opposite, listening with sorrow",
         camera="medium close-up on Noorin, eye level", amb="living_night", hum=True),
    dict(to=84, reason="return: Noorin alone again after they leave", reuse="beat_021", chars=["noorin"], loc="home_eve",
         visual="(reuse) Noorin alone on the sofa, numb with sorrow", amb="room_night"),
    dict(to=87, reason="time and action change: late at night she pours her pain into her story at the computer", chars=["noorin"], loc="home_night",
         visual=f"{OFF2}; Noorin sitting at the small desk typing on the keyboard, the monitor angled away from the viewer so only its soft glow lights her sad, intent face; a white flash of lightning through the rain-streaked window behind",
         camera="medium shot, three-quarter view, the desk top as the lower third", amb="room_night", transition="black"),
    dict(to=89, reason="character enters: Uvaish soaked at her door in the storm", chars=["uvaish", "noorin"], loc="doorway",
         visual=f"seen from inside the apartment: Noorin holding the door open, frozen in shock ({OFF}); Uvaish stands outside on the wet walkway, soaked to the skin, his suit and hair dripping, rain blowing behind him; {GAP}, he stays outside the threshold",
         camera="medium wide, eye level, the wet tiled floor as the lower third", amb="storm_night"),
    dict(to=92, reason="emotional turning point: for a moment her stone heart softens", chars=["noorin"], loc="doorway",
         visual=f"{OFF}; close-up of Noorin alone in the frame just inside the open doorway, her eyes slowly closing, one hand resting on the door edge, a fragile conflicted softness on her face, cold blue rain light on one side of her face and warm amber light on the other",
         camera="close-up, eye level", amb="storm_night", hum=True, sens="intimacy",
         safe="the sudden embrace is NOT shown (bible rule 6): Noorin alone in the frame with her eyes closed"),
    dict(to=95, reason="action change: Uvaish begs for forgiveness at the threshold", chars=["uvaish", "noorin"], loc="doorway",
         visual=f"Uvaish soaked on the wet walkway just outside the threshold, his hands open palms-up, his face anguished and wet with rain and tears, pleading; Noorin has stepped back inside the doorway, upright, her face turned partly away ({OFF2}); {GAP}, a wide space between them",
         camera="medium wide two-shot, eye level", amb="storm_night", sens="intimacy",
         safe="no embrace: he stays at the threshold with a clear gap and she steps back (bible rule 6)"),
    dict(to=96, reason="memory: the bitter memories of twelve years ago flash before her eyes", loc="memory",
         visual="a hazy empty hotel corridor from twelve years ago, one closed wooden door in the centre, dim wall lamps, rain on the window at the far end, no people",
         camera="wide symmetrical shot down the corridor, the floor as the lower third", amb="memory_rain", transition="dissolve", sens="violence",
         safe="the night twelve years ago is never shown: only a closed door in an empty hotel corridor (bible rules 1 and 8)"),
    dict(to=98, reason="action change: she sends him away — shown as her pointing him out", chars=["noorin", "uvaish"], loc="doorway",
         visual=f"{OFF2}; Noorin standing firm inside the doorway, one arm extended straight, pointing out into the rainy night, her face fierce and cold; Uvaish outside on the wet walkway, more than an arm's length away, stunned, his hands lowered; {GAP}",
         camera="medium wide two-shot, eye level", amb="storm_night", transition="dissolve", sens="violence",
         safe="the push is NOT shown (bible rule 6): she points him out with a clear gap between them"),
    dict(to=101, reason="emotional peak: Noorin's furious warning", chars=["noorin"], loc="doorway",
         visual=f"{OFF}; close-up of Noorin alone in the doorway, her face fierce, jaw tight, eyes blazing with fury and old pain, speaking out loud, her hands at her sides; the dark rainy night behind her",
         camera="close-up, slightly low angle", amb="storm_night", hum=True, sens="other",
         safe="her threats are dialogue only: a fierce face, no gestures of violence"),
    dict(to=103, reason="return: Uvaish recoils and steps back; the door slams", reuse="beat_033", chars=["noorin", "uvaish"], loc="doorway",
         visual="(reuse) Noorin pointing him out, Uvaish outside stunned", amb="storm_night"),
    dict(to=105, reason="action change: the door closed, Noorin inside with her hand on her heart", chars=["noorin"], loc="doorway",
         visual=f"{OFF2}; seen from inside the dim apartment: Noorin standing with her back close to the now-closed front door, her right hand pressed flat on her chest over her heart, chin raised, eyes wet but steady, a quiet fierce resolve; lightning flickers on the rain-streaked window beside her",
         camera="medium shot, eye level", amb="storm_night", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Just as Noorin stepped out of her apartment to go to the office, at that very moment Aakif also stepped out right in front of her.",
   [("door_open", "ނިކުތް", -20)])
sh(2, "It was Aakif himself who had moved into the apartment right next to hers. What an astonishing coincidence!")
sh(3, "As Noorin stood staring at Aakif in surprise, Aakif's eyes too were fixed on Noorin. \"After a long wait of twelve years,")
sh(4, "I never once imagined I would meet you again like this, Noorin,\" Aakif said with deep emotion. \"I never imagined it either.\"")
sh(5, "Noorin's answer was quiet. \"There is no effort I didn't make to find you, Noorin.\" Keeping his gaze on her face, Aakif said:")
sh(6, "\"I went away for training. This world taught me the real truth of life. Power and influence are everything.")
sh(7, "I washed out of my heart the fear I had of others, and today I have become a strong personality whom others fear.\"")
sh(8, "In a cold tone that showed no feeling, Noorin spoke. \"But I am still here, waiting only for you, Noorin.\"")
sh(9, "Aakif said tenderly. \"Today my heart is like a stone. No feeling, no emotion touches that heart any more.")
sh(10, "So how could I give love?\" There was a deep silence in Noorin's voice. \"I will turn that heart into a soft flower.")
sh(11, "That is how much I love you, Noorin,\" Aakif said with certainty, stepping a little closer to her. \"Forgive me, Aakif.",
   [("footsteps_pavement", "ކައިރިވެލަމުން", -24)])
sh(12, "In my heart there is regard and respect for you, Aakif. But my whole life, my love,")
sh(13, "and every moment are now devoted to my national duty — my job. There is no longer any room in my life to give to anyone else.\"")
sh(14, "Putting on the sunglasses in her hand, Noorin walked away without looking back. Aakif stood watching her get on her motorbike and ride off until she vanished from sight.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22), ("motorbike_pass", "ދުއްވާލި", -16)])
sh(15, "Even though Noorin had spoken such harsh words, Aakif understood that in a corner of her heart the memories of Uvaish and his love were still kept.")
sh(16, "Photographs were being taken of the shattered glass and of the safe that had been forced open.")
sh(17, "It was the moment Noorin was carefully studying the things scattered all over the crime scene. In walked Uvaish.",
   [("footsteps_pavement", "ވަދެގެން", -22)])
sh(18, "Seeing Noorin standing so firm in her police uniform, Uvaish felt a sudden shock hard to describe. The gentle Noorin he had known in the past —",
   [("heartbeat", "ސިހުމެކެވެ", -20)])
sh(19, "he had never, even in his dreams, expected her to become such a strong police officer. \"Is a woman officer investigating this case?\"")
sh(20, "the secretary standing nearby asked in surprise. Noorin gave the secretary a cold look, then fixed her eyes straight on Uvaish's.")
sh(21, "\"Whether a case is investigated by a woman officer or a man officer is not what matters. What matters is that person's competence and fitness for the job.\"")
sh(22, "Looking them straight in the face, Noorin said with firmness and strong resolve: \"Jinaah! Carry the investigation forward thoroughly.")
sh(23, "Our team must not fall behind. This is the break-in at the office of one of the Maldives' most famous businessmen.\"")
sh(24, "She gave the order in a firm voice. Stepping forward and passing in front of Uvaish, Noorin paused, her sunglasses on.",
   [("footsteps_pavement", "ފިޔަވަޅު", -22)])
sh(25, "And slowly turning her face towards Uvaish, she said: \"Not respecting women is perhaps simply in some people's nature.")
sh(26, "But I am loyal to my duty. I serve even the disloyal professionally, with the integrity of my job.\"")
sh(27, "Noorin said this in a mocking tone. Sitting on the sofa in his sitting room, Uvaish was reading the message Noorin had sent him twelve years ago.")
sh(28, "Reading that message every day was Uvaish's habit. The pain and anguish that every word of it brought to his heart is hard even to describe.")
sh(29, "\"Living with a man who does not respect a woman is like jumping into a fire by one's own choice.", hum=True)
sh(30, "Today the paths of the two of us have completely parted. I am ashamed that I ever loved someone like you.")
sh(31, "I even hesitate to say that the father of my child is you. I hope you will not treat Reem the way you treated me.")
sh(32, "Learn to respect women! Your mother is a woman too. The station of women is a noble and exalted station.")
sh(33, "Mankind reaches paradise from beneath a woman's feet — and that is your mother.\" When he finished reading Noorin's message, tears began to stream from Uvaish's eyes.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(34, "\"How can I prove that I did no wrong?\" Uvaish asked himself, sobbing.",
   [("sob_breath", "ގިސްލަމުން", -22)])
sh(35, "Uvaish learned the truth of what had passed between Aakif and Noorin only three months later.")
sh(36, "It was when, one day, they happened to meet and Aakif told him the whole story truthfully. When he learned that Aakif's only aim had been to help Noorin,")
sh(37, "Uvaish's heart filled with grief. Shame and sorrow engulfed him — that, as her husband, he had left Noorin alone in the storms of the world.", hum=True)
sh(38, "Thinking that the child must be grown up by now, his heart cried out with longing to see that child.")
sh(39, "The days passed in their swift race. Days turned into weeks and months into years, yet Uvaish's efforts never changed.")
sh(40, "He kept doing everything he could to win back Noorin's forgiveness and love. Yet")
sh(41, "Noorin did not want to walk even on a road that Uvaish had walked. Noorin's whole life and time were devoted to her job.")
sh(42, "It was one afternoon. Noorin was surprised when Uvaish's lawyer came to her office to meet her. But",
   [("knock", "އައުމުން", -20)])
sh(43, "out of that surprise, a mocking smile spread across her lips. Without knowing the truth,")
sh(44, "Uvaish was once again getting ready to step into a blazing fire. \"The child?\"")
sh(45, "Noorin asked in surprise. \"Yes! Uvaish wants to go to court to get the child. Or else to reunite with you in a good way.\"")
sh(46, "the lawyer said coldly. Noorin let out a deep breath and said: \"Tell Uvaish to come and meet me tomorrow.\"",
   [("breath", "ނޭވާއެއް", -22)])
sh(47, "The lawyer told Uvaish how things had gone that day. And, as Noorin had asked, the next day Uvaish went there with the lawyer.")
sh(48, "At that moment Noorin was having a clerk prepare a report. Asking the young woman to wait, Noorin invited them to sit.",
   [("keyboard_typing", "ރިޕޯޓެއް", -24)])
sh(49, "Then, after a glance at Uvaish, with a mocking smile on her lips, she began to speak to the lawyer.")
sh(50, "\"A real father would know very well what happened to his child.\" Noorin opened a drawer, took out a file and dropped it on the desk.",
   [("soft_thud", "ވައްޓައިލިއެވެ", -20)])
sh(51, "\"Every detail is in here.\" The lawyer opened the file and read what was written in it. Then, looking at Uvaish, he began to explain the details.",
   [("page_turn", "ހުޅުވައި", -20)])
sh(52, "As he listened to the lawyer, the colour of Uvaish's face changed; unease and anguish took hold of him. The moment he learned what had happened to the child,")
sh(53, "it felt as if boiling water had been poured over his heart. His eyes filled with tears. In those twelve years he had not been waiting only for Noorin.",
   hum=True)
sh(54, "He had been waiting for the child too, the light of his eyes. With tear-filled eyes he looked towards Noorin.")
sh(55, "Looking at the young woman writing the report, Noorin asked, \"Done?\" When the girl nodded,")
sh(56, "Noorin looked at Uvaish's lawyer and said firmly: \"Should I file a case against Uvaish for harming me against my will when I was five months pregnant?",
   hum=True)
sh(57, "For my tiny five-month child, who left before ever drawing a breath in this world because of that harm?\"", hum=True)
sh(58, "Having said that much, Noorin's eyes filled with tears, and she closed them to hold back her emotions.",
   [("breath", "މަރައިލިއެވެ", -24)], hum=True)
sh(59, "Her heartbreaking words drew the eyes of everyone in the room to her. Uvaish sat frozen, not knowing what to say.")
sh(60, "It was as if she wanted revenge for the scorn and mockery she had faced, and for the deep sorrows she had been given.")
sh(61, "She wished that Uvaish would receive the punishment that heartbreak deserved. In this world, could there be any greater punishment than Uvaish's honour and dignity being trampled into the sand?")
sh(62, "\"I am ready for any punishment you give me, Noorin.\" Uvaish's voice was full of sorrow and despair.")
sh(63, "\"Your greatest punishment is to receive no lawful punishment at all, and to be left writhing in that guilt and pain for the rest of your life!\"")
sh(64, "Saying that very coldly, yet in a powerful tone, Noorin walked out of the place without looking back.",
   [("footsteps_pavement", "ހިނގައްޖެއެވެ", -22)])
sh(65, "The effort Noorin had been making to find even a spark of happiness in the darkness had now stopped.")
sh(66, "It was a despair in which no ray of light would ever be seen. After twelve years had passed, she was once again reminded of her beloved child.")
sh(67, "After opening the doctors' report in her hand, as she ran her fingers over the scans that came with it,",
   [("paper_shuffle", "ހުޅުވައިލުމަށްފަހު", -22)])
sh(68, "nothing could stop the tears pouring from her eyes. All her life, the only thing that had stayed loyal to her was the tears from those eyes.",
   [("sob_breath", "ކަރުނަތަކަށް", -24)], hum=True)
sh(69, "With every deep feeling of her heart, those tears fulfil their duty most faithfully. Noorin came to herself at the ring of the doorbell.",
   [("doorbell_buzz", "ރަނގަބީލު", -16)])
sh(70, "Quickly wiping away her tears, she went and opened the door. In front of her stood Reem. Beside Reem stood another man she did not know. \"Reem!\"",
   [("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(71, "Noorin exclaimed in surprise. And when she invited them in, they came inside and sat down on the sofa in the sitting room.",
   [("footsteps_pavement", "ވަދެ", -24)])
sh(72, "\"This is my husband, Naaif,\" Reem introduced him. Noorin sat speechless, staring at Reem in surprise.")
sh(73, "\"Won't you ask why I have come here?\" Reem asked. But Noorin sat in silence, giving no answer.")
sh(74, "\"Uvaish and I married only because our families wished it — to fulfil a promise made between the two families.")
sh(75, "Then, and still now, the one I love is Naaif. With time I learned to accept the truth and to live with it.")
sh(76, "When his grandfather passed away, I divorced Uvaish. I was only his friend. Uvaish never even laid a finger on me.")
sh(77, "He still loves only you, Noorin. He is still waiting for you. He has already received the punishment for his wrong.")
sh(78, "What was lost was not only your child, Noorin — it was Uvaish's own blood too... He feels it as deeply as you do.\"")
sh(79, "Reem said with deep feeling. \"I am the one who bore that pain! Because I was a woman, I was the one who had to face the whole world!",
   hum=True)
sh(80, "Every finger was pointed and every accusation fell on my head! How could Uvaish ever understand this pain and these feelings?")
sh(81, "All Uvaish knows is that a child of his left this world.\" Noorin's voice choked and her eyes filled with tears again. \"And besides,",
   [("sob_breath", "ބެދި", -24)], hum=True)
sh(82, "it is far too late to talk about this now. Twelve years have gone by before that truth was told. In these twelve years my poor heart has turned to hard stone.\"",
   hum=True)
sh(83, "Noorin said with strong resolve. After Reem and her husband had left, Noorin tried to steady herself.",
   [("door_close", "ނުކުމެގެން", -20)])
sh(84, "But the sorrows hidden in her heart began to swell more than ever. The loneliness around her grew until it numbed her.",
   [("sigh", "އެކަނިވެރިކަން", -22)])
sh(85, "She poured the emotions and sorrows welling up in her heart into the story she was writing. As she typed on the computer keyboard,",
   [("keyboard_typing", "ކީބޯޑުގައި", -22)])
sh(86, "she kept wishing she could change the pages of her own life with that keyboard too. But real life is not a computer you can erase and rewrite as you please.",
   [("keyboard_typing", "ކީބޯޑުން", -24)])
sh(87, "Nor is it a tale shaped by one's own imagination. At the mighty crack of thunder that came with the lightning, Noorin started.",
   [("thunder", "ގުގުރީގެ", -12)])
sh(88, "Only then did she notice that it was raining heavily outside. At the same moment she heard the doorbell ring.",
   [("rain_start", "ވާރޭ", -18), ("doorbell_buzz", "ރަނގަބީލު", -16)])
sh(89, "Noorin got up from the computer, went and opened the door. Seeing Uvaish standing soaked at the door, she froze.",
   [("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(90, "Without giving her a chance to say anything, Uvaish suddenly embraced Noorin. Slowly, Noorin's eyes closed.",
   [("heartbeat", "މަރައިލެވުނެވެ", -20)], hum=True)
sh(91, "However much she tried to show that hers was a heart of stone, before love that heart melts.")
sh(92, "The things Reem had told her today had moved Noorin's heart deeply. However much strength she showed on the outside,")
sh(93, "she too had a delicate, womanly heart. That heart too longed for tenderness and love. \"Noorin, forgive me!\"")
sh(94, "Uvaish said in a voice full of emotion. \"I didn't know any of the truth. Give me any punishment you want. But don't go far away from me...")
sh(95, "Please!\" Uvaish begged in a tearful voice, hiding his face in her hair.",
   [("sob_breath", "ރޮވިފައިވާ", -22)])
sh(96, "But Uvaish's emotional words faded as they reached Noorin's ears. Before her eyes rose the bitter memories of twelve years ago.",
   hum=True)
sh(97, "Instantly, without any mercy, she put her hand to Uvaish's chest and pushed him away. For a moment Uvaish had thought he had won Noorin's love back,",
   [("soft_thud", "ކޮށްޕައިލިއެވެ", -24)])
sh(98, "that Reem's words had softened Noorin's heart. But the wound of those memories was far deeper than the strong stone wall built around Noorin could cover.")
sh(99, "\"If you try to harass me like this again, I will file a case for the sexual assault on me twelve years ago!", hum=True)
sh(100, "And I will also bring cases for stalking and threatening me, and for the domestic abuse during our marriage!")
sh(101, "I will not leave you a single door of escape!\" Noorin screamed, the veins of her neck swelling, her voice trembling with rage.",
    [("breath_heavy", "ހަޅޭއްލަވައިގަތެވެ", -20)])
sh(102, "Uvaish recoiled at the dangerous fury he saw in Noorin. Feeling the bitterness of the truth he now had to face,")
sh(103, "he involuntarily took a step back. With that, Noorin slammed the door hard in Uvaish's face.",
    [("footsteps_pavement", "ފިޔަވަޅެއް", -22), ("door_close", "ބަންކޮށްލިއެވެ", -12)])
sh(104, "\"I am not weak... and not helpless either! I don't need any man's help. This is that same 'Noorin'!\"", hum=True)
sh(105, "Pressing her hand to her chest over her heart, Noorin said softly to herself with strong resolve.", hum=True)
SHOTS = S

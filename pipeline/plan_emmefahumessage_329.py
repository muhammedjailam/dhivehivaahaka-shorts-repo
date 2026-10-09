"""Beat/shot plan for Emme Fahu Message episode 329 (series finale; used by plan_beats.py).
Amaan finally plays Eethan's last voice message (imagined as Eethan calm in his parked car at night in the rain, dissolved
with Amaan listening sitting up against the headboard), the weeks of grief, the nausea, Luha, the pregnancy test (a small
white stick by a frosted window, never a toilet), and months later the nursery in golden evening light.
Rules: the accident is never shown; no kissing/embracing between Amaan and Eethan; no man touches Amaan; hijab fully
covering hair and neck on every woman in every shot; Amaan never lying down; no readable text/numbers anywhere."""

AMAAN_HOME = ("Amaan wears her loose long-sleeved ankle-length cream dress with a loose long grey cardigan over it and her "
              "dusty-rose hijab wrapped snugly, fully covering her hair and neck")
AMAAN_DAY = ("Amaan wears her loose long-sleeved ankle-length cream dress and her dusty-rose hijab fully covering her hair "
             "and neck")
EETHAN_CAR = "Eethan wears a dark-olive zip-up rain jacket over the navy t-shirt and dark jeans"
HEADBOARD = "sitting upright against the wooden headboard with a soft blanket over her legs (never lying down)"
PHONE = "the phone screen shows only a soft blank glow, no text, no numbers"
SINGLE = ("one single unified scene with only the people named here; no inset vignettes, no thought-bubble images, no ghostly "
          "overlay faces or figures on the walls, in the glow or in the sky, no second copy of any person")

LOC = {
    "bedroom_night": "a small modest bedroom in a third-floor Hulhumalé apartment at night, a plain wooden headboard, white "
                     "pillows, a small bedside table with a dim amber lamp, a window with rain streaming down the glass",
    "car": "the inside of a small ordinary hatchback car parked at the kerb of a quiet empty rain-washed Hulhumalé street at "
           "night, rain running down the windscreen, wipers at rest, blurred amber streetlights and their reflections on the "
           "wet road, the soft blue-green glow of the dashboard",
    "memory_street": "a quiet wet Hulhumalé side street in a light monsoon drizzle, a closed shop with a plain grey rolled-down "
                     "shutter and a small plain awning, puddles reflecting the sky, potted plants, no signs",
    "memory_home": "the small cosy sitting room of the apartment imagined as a future family home: a worn sofa with a vermilion "
                   "cushion, a low wooden coffee table, a woven rug on a wooden floor",
    "bedroom_dawn": "the same small modest bedroom in a third-floor Hulhumalé apartment at first light, a plain wooden "
                    "headboard, white pillows, a small bedside table, a window with rain-streaked glass",
    "balcony": "a narrow third-floor apartment balcony in Hulhumalé with a simple metal railing, a small folding chair and a "
               "potted plant, wet rooftops and palm tops of the town beyond",
    "kitchen": "the tiny apartment kitchen: a narrow counter, simple cupboards, a kettle, a small window with rain on the glass, "
               "a small two-seat dining table at the edge of the kitchen",
    "bedroom_clean": "the small bedroom freshly cleaned at night: crisp fresh white sheets and pillows, the window wide open to "
                     "the rainy night air with a sheer curtain lifting, a folded blanket on a wooden chair",
    "bedroom_morning": "the small bedroom early in the morning, fresh white sheets slightly rumpled, a small bedside table, a "
                       "window with pale grey light",
    "clinic_memory": "a fertility specialist's consulting room: a wooden desk, a plain cream wall, a small potted plant, a "
                     "closed folder on the desk",
    "sitting_day": "the small sitting room of the apartment: a worn sofa with a vermilion cushion, a low wooden coffee table with "
                   "a novel and reading glasses, framed photos on the walls, a plain analog wall clock with no numerals, a "
                   "balcony door with rain on the glass",
    "photo": "a low wooden cabinet in the sitting room beneath a plain wall mirror, a small vase and a framed photograph on top, "
             "rain light from a nearby window",
    "vanity": "a small plain room off the hallway with a narrow pale counter under a frosted glass window, a folded hand towel "
              "on the counter, a white door ajar to a hallway; no toilet, no shower, no bathtub, no sink fixtures visible",
    "hallway": "the narrow apartment hallway outside a small room, a plain cream wall, a wooden floor, a soft light from the "
               "kitchen at the end",
    "imagined_door": "the apartment's front doorway and the narrow entrance hall, a wooden door standing open",
    "sitting_night": "the small sitting room of the apartment at night: a worn sofa with a vermilion cushion, a low coffee "
                     "table, a balcony door with rain streaming down the dark glass, one warm amber floor lamp",
    "nursery": "a small children's room: a white wooden crib with a soft blanket, a low chest with neatly folded tiny baby "
               "clothes, a pale wall, a window with a sheer curtain, a phone lying on the windowsill",
}
MOOD = {
    "bedroom_night": "rainy night after midnight, a single dim amber lamp against cold grey-blue rain light from the window, "
                     "heavy silent grief, intimate and still",
    "car": "rainy night, an imagined scene seen in a soft dissolve: deep blue darkness, the gentle dashboard glow on his face, "
           "warm blurred streetlight bokeh through the rain on the glass, calm, quiet and safe, no danger",
    "memory_street": "soft hazy golden dreamlike memory glow, warm light breaking through a light drizzle, tender and funny",
    "memory_home": "soft hazy golden dreamlike memory glow, a warm night lamp, gentle and wistful, a dream of a future",
    "bedroom_dawn": "rainy dawn, pale blue first light mixing with the last warm glow of the lamp, exhausted, tear-stained "
                    "and quietly tender",
    "balcony": "early morning after rain, soft pale gold sunlight through thinning grey clouds, wet glistening rooftops, "
               "quiet and fragile",
    "kitchen": "grey rainy morning light from the small window mixed with warm amber kitchen light, steam rising, quiet ache",
    "bedroom_clean": "rainy night, cool fresh air, soft blue night light from the open window and a small warm lamp, a "
                     "tentative new beginning",
    "bedroom_morning": "early morning, pale grey monsoon daylight, soft and heavy, a hint of unease",
    "clinic_memory": "soft hazy golden dreamlike memory glow, muted and sad, a quiet heavy silence",
    "sitting_day": "rainy grey afternoon, soft diffused grey-blue daylight from the balcony door and one warm amber lamp, "
                   "tender worry",
    "photo": "rainy grey afternoon, soft diffused daylight, a warm amber lamp glow on the frame, longing",
    "vanity": "rainy grey afternoon, soft milky light through the frosted glass, very quiet, suspense and fragile hope",
    "hallway": "rainy grey afternoon with warm amber light from the kitchen, overwhelming emotion, tears of joy and grief",
    "imagined_door": "soft hazy golden dreamlike memory glow, warm and joyful, an imagined moment",
    "sitting_night": "rainy night, one warm amber lamp against deep blue shadows, the soft glow of a phone, tearful wonder",
    "nursery": "months later, a clear golden late-afternoon after the rains, warm golden sun rays slanting through the window "
               "across the crib, peaceful, hopeful, gently fading to deep gold",
}

BEATS = [
    # ---------------------------------------------------------------- the night she listens
    dict(to=3, reason="episode opening: Amaan wakes to the rain after midnight, his empty side of the bed", chars=["amaan"],
         loc="bedroom_night",
         visual=f"Amaan {HEADBOARD} in the dim bedroom, staring up at the ceiling with red, swollen, sleepless eyes, one hand "
                f"resting on the slightly dented white pillow on the empty side beside her; her phone lies face down on the "
                f"bedside table; rain streams down the window; {SINGLE}. {AMAAN_HOME}",
         camera="medium shot from the foot of the mattress, her face in the upper third, the smooth blanket as a calm lower "
                "third", amb="apartment_rain_night", sens="other",
         safe="'lay staring at the ceiling' shown as sitting up against the headboard; hijab kept on at night"),
    dict(to=6, reason="action change: she picks up the phone and decides to listen just once", chars=["amaan"],
         loc="bedroom_night",
         visual=f"close-up of Amaan {HEADBOARD}, holding her phone in both hands close to her chest, looking down at its soft "
                f"glow with trembling resolve, her thumb hovering over the screen, the glow lighting her tear-stained face; "
                f"{PHONE}. {AMAAN_HOME}",
         camera="medium close-up, slightly high angle, her face in the upper half, her hands and the phone below",
         amb="apartment_rain_night"),
    dict(to=8, reason="imagined scene: the voice message begins — Eethan alone in his parked car in the rain", chars=["eethan"],
         loc="car",
         visual=f"Eethan sitting calmly alone in the driver's seat of his parked car at night, seen from the passenger side, "
                f"holding his phone loosely near his mouth as he records a voice message, his face tired and gentle, a deep "
                f"breath, both of them still and safe; rain runs down the windscreen, blurred amber streetlights outside; "
                f"{PHONE}. {EETHAN_CAR}",
         camera="medium wide from the passenger seat, his face in the upper half, the dark dashboard and seat as a calm "
                "lower third", amb="car_rain", transition="dissolve", sens="other",
         safe="the voice message is imagined as Eethan calm in his PARKED car in the rain — no driving danger, no crash"),
    dict(to=10, reason="focus change: back to Amaan listening with her eyes closed", chars=["amaan"], loc="bedroom_night",
         visual=f"Amaan {HEADBOARD}, the phone held against her ear with one hand, her eyes closed, her other hand pressed to "
                f"her lips, holding her breath as she hears his voice; the amber lamp beside her, rain on the window. "
                f"{AMAAN_HOME}",
         camera="close-up, eye level, her face in the upper half, the folded blanket below", amb="apartment_rain_night",
         transition="dissolve"),
    dict(to=13, reason="imagined scene: Eethan in the car searching for the right words", chars=["eethan"], loc="car",
         visual=f"close side profile of Eethan in the driver's seat of the parked car at night, looking down thoughtfully, "
                f"searching for the right words, the phone held near his mouth, his free hand resting calmly on the steering "
                f"wheel, a thin silver wedding ring; the side window behind him streaked with rain and soft amber bokeh; "
                f"{PHONE}. {EETHAN_CAR}",
         camera="close-up profile, his face in the upper half, the dark door panel below", amb="car_rain",
         transition="dissolve"),
    dict(to=15, reason="memory: one of the things he loves about her — she cries when she sees a cat in the street",
         chars=["amaan", "eethan"], loc="memory_street",
         visual=f"a memory: Amaan crouching on a wet pavement under a small awning beside a tiny wet ginger kitten, tears in "
                f"her eyes and a tender smile; Eethan standing beside her holding a vermilion-red umbrella over her, smiling "
                f"down at her fondly with amused love, not touching her. {AMAAN_DAY}. {EETHAN_CAR}",
         camera="medium wide, eye level, both faces in the upper half, the wet pavement as a calm lower third",
         amb="memory_rain", transition="dissolve"),
    dict(to=17, reason="action change: Amaan laughs through tears and presses the phone to her chest", chars=["amaan"],
         loc="bedroom_night",
         visual=f"Amaan {HEADBOARD}, a small surprised laugh breaking through her tears, both hands pressing the phone flat "
                f"against her chest, eyes shining, head tilted back slightly against the headboard; the amber lamp, rain on "
                f"the window. {AMAAN_HOME}",
         camera="medium close-up, eye level, her face in the upper third", amb="apartment_rain_night", transition="dissolve"),
    dict(to=19, reason="imagined dream: the child they both dreamed of — toys scattered through the house", loc="memory_home",
         visual="a soft dreamlike image of the little sitting room as a family home: colourful wooden toys, building blocks "
                "and a small stuffed bear scattered across the woven rug, a pair of tiny baby shoes beside the sofa, two cups "
                "of tea on the coffee table, a small night lamp glowing; nobody in the room, no people or children anywhere in the image, no figures in the glow or on the walls",
         camera="wide shot from a low angle, the toys and sofa in the middle, the soft rug as a calm lower third",
         amb="memory", transition="dissolve", sens="other", safe="the dreamed child is shown only through toys and tiny shoes"),
    dict(to=21, reason="return to the imagined car scene: his voice grows softer", reuse="beat_003", loc="car",
         chars=["eethan"], visual="(reuse of beat_003: Eethan calm in his parked car at night)", amb="car_rain",
         transition="dissolve"),
    dict(to=25, reason="action change / emotional peak: Amaan bends forward and cries silently", chars=["amaan"],
         loc="bedroom_night",
         visual=f"Amaan {HEADBOARD} but bent forward over her drawn-up knees, the phone still held to her ear, her other hand "
                f"covering her mouth, shoulders shaking as she cries silently, tears on her cheeks; the amber lamp, rain "
                f"streaming down the window. {AMAAN_HOME}",
         camera="medium shot, slightly from the side, her face in the upper half, the blanket over her knees below",
         amb="apartment_rain_night", transition="dissolve"),
    dict(to=28, reason="imagined scene: Eethan's tender promise about 'a little miracle'", chars=["eethan"], loc="car",
         visual=f"close-up of Eethan in the driver's seat of the parked car at night, turned slightly towards the camera, a "
                f"gentle loving smile and glistening eyes as he speaks softly into the phone near his mouth, the warm "
                f"dashboard glow on his face, rain drops on the windscreen behind him; {PHONE}. {EETHAN_CAR}",
         camera="close-up from the passenger side, his face in the upper half", amb="car_rain", transition="dissolve",
         sens="other", safe="calm, safe, parked; nothing about the drive that followed is shown"),
    dict(to=32, reason="time change: the recording ends; dawn — she plays it again and again", chars=["amaan"],
         loc="bedroom_dawn",
         visual=f"Amaan {HEADBOARD} in the pale dawn light, the phone pressed to her ear, red-rimmed eyes, a tear on her cheek "
                f"and at the same time a faint helpless smile, as if listening again and again; the lamp still on, rain "
                f"easing on the window; {SINGLE}. {AMAAN_HOME}",
         camera="medium shot, eye level, her face in the upper third, the blanket as a calm lower third",
         amb="apartment_rain_night", transition="dissolve"),
    # ---------------------------------------------------------------- the first days and weeks
    dict(to=35, reason="time and location change: the first days — she carries his voice everywhere; morning coffee on the "
                       "balcony", chars=["amaan"], loc="balcony",
         visual=f"Amaan sitting on a small folding chair on the narrow balcony in the early morning, a vermilion-red mug of "
                f"coffee in one hand, her phone held to her ear with the other, listening with calm wet eyes, looking out over "
                f"the wet rooftops; {PHONE}; {SINGLE}. {AMAAN_DAY}",
         camera="medium shot from the side, her face in the upper third, the balcony floor as a calm lower third",
         amb="apartment_morning"),
    dict(to=37, reason="action change: grief without warning — pouring tea into a second cup", chars=["amaan"],
         loc="kitchen",
         visual=f"Amaan at the kitchen counter, a teapot in her hand frozen just above a second empty cup next to her own full "
                f"one, her face suddenly still as she remembers there is no one to drink it; Eethan's vermilion-red mug is "
                f"the empty one. {AMAAN_DAY}",
         camera="medium close-up, eye level, her face in the upper third, the two cups on the counter in the lower part",
         amb="apartment_morning"),
    dict(to=40, reason="time jump ('weeks passed'): she throws the condolence flowers away and looks at the empty vases",
         chars=["amaan"], loc="kitchen",
         visual=f"a grey rainy afternoon weeks later: Amaan standing beside a tall kitchen bin heaped with wilted white and "
                f"pale green flowers, looking at a row of empty glass vases on the small dining table, her hands hanging at "
                f"her sides, a hollow, undecided expression. {AMAAN_DAY}",
         camera="medium wide, eye level, her face in the upper third, the floor as a calm lower third",
         amb="apartment_rain_day", transition="black"),
    dict(to=43, reason="time and action change: that night she cleans the room and moves back to her own side",
         chars=["amaan"], loc="bedroom_clean",
         visual=f"the freshly cleaned bedroom at night: Amaan {HEADBOARD} on HER OWN side, the other side smooth, empty and "
                f"neatly made with fresh white sheets, the window wide open with the curtain lifting in the rainy night air, "
                f"the washed blanket folded on a chair; she looks into the darkness with quiet resolve. {AMAAN_HOME}",
         camera="medium wide from the foot of the room, her face in the upper third", amb="apartment_quiet_night"),
    # ---------------------------------------------------------------- the nausea
    dict(to=47, reason="time jump: the next morning she wakes heavy and nauseous", chars=["amaan"], loc="bedroom_morning",
         visual=f"Amaan sitting on the edge of the mattress in the early morning, one hand pressed to her stomach and the other "
                f"lightly at her lips, pale and queasy, eyes tired from crying; a small framed photo lies face down on the "
                f"blanket behind her. {AMAAN_HOME}",
         camera="medium shot, eye level, her face in the upper third, the wooden floor as a calm lower third",
         amb="apartment_morning", transition="black"),
    dict(to=50, reason="location and action change: nausea again in the kitchen after making tea — a thought she pushes away",
         chars=["amaan"], loc="kitchen",
         visual=f"Amaan standing still in the tiny kitchen, one hand resting on her stomach, the other on the counter beside a "
                f"steaming cup of tea she just made, her eyes distant and wide as a thought crosses her mind, a small shake "
                f"of the head. {AMAAN_DAY}",
         camera="medium shot, eye level, her face in the upper third, the counter top as a calm lower third",
         amb="apartment_morning"),
    dict(to=52, reason="memory: every hope ended in a negative test or the doctor's sympathetic silence",
         chars=["dr_mathews", "amaan"], loc="clinic_memory",
         visual=f"a muted memory: Dr. Mathews behind his wooden desk with a kind, sad, silent look and his hands folded, a "
                f"small plain white plastic test stick lying on the desk; Amaan seated across the desk, seen from the side, "
                f"her eyes lowered; a clear distance across the desk between them. {AMAAN_DAY}",
         camera="medium shot over the desk, both faces in the upper half, the desk top as a calm lower third",
         amb="memory", transition="dissolve"),
    dict(to=56, reason="time and character change: that afternoon Luha notices how unwell she is",
         chars=["amaan", "luha"], loc="sitting_day",
         visual=f"Amaan sitting on the sofa looking pale and dizzy, one hand on her stomach, glancing up; her elder sister Luha "
                f"standing a step away in front of her, leaning slightly forward with a worried frown, then a dawning "
                f"realisation on her face. {AMAAN_DAY}. Luha in her deep-teal dress and black hijab",
         camera="medium wide two-shot, eye level, both faces in the upper half, the rug as a calm lower third",
         amb="apartment_rain_day", transition="dissolve"),
    dict(to=58, reason="emotional turning point: the question stuns her — she cannot count time since he died",
         chars=["amaan"], loc="sitting_day",
         visual=f"close-up of Amaan sitting on the sofa, frozen and stunned, staring into nothing, lips slightly parted, the "
                f"room soft and out of focus behind her with a plain analog wall clock without numerals. {AMAAN_DAY}",
         camera="close-up, eye level, her face in the upper half", amb="apartment_rain_day", sens="other",
         safe="the narration mentions the day of the accident — nothing of it is shown, only her stunned face"),
    dict(to=61, reason="action change: Luha sits beside her and takes her hand", chars=["amaan", "luha"], loc="sitting_day",
         visual=f"Luha sitting close beside Amaan on the sofa, holding Amaan's hand in both of hers with a kind, serious face; "
                f"Amaan looking down at their joined hands, afraid. {AMAAN_DAY}. Luha in her deep-teal dress and black hijab",
         camera="medium shot, eye level, both faces in the upper half, their joined hands in the middle",
         amb="apartment_rain_day"),
    dict(to=64, reason="emotional turning point: 'what if it's negative? what if it's positive?' — Luha's eyes fill",
         chars=["luha", "amaan"], loc="sitting_day",
         visual=f"closer two-shot of the two sisters on the sofa: Luha's eyes filling with tears and a gentle brave smile, "
                f"Amaan whispering a frightened question, still holding hands; a small plain white unopened box with no "
                f"printing lies on the coffee table in front of them. {AMAAN_DAY}. Luha in her deep-teal dress and black hijab",
         camera="medium close-up, eye level, both faces in the upper half", amb="apartment_rain_day"),
    dict(to=66, reason="object focus: Eethan's framed photo under the mirror, smiling, his hand on her shoulder",
         chars=["eethan", "amaan"], loc="photo",
         visual="a framed photograph standing on the low cabinet under a plain wall mirror: in the photo Eethan smiles warmly "
                "with his hand on Amaan's shoulder, Amaan beside him in her cream dress and dusty-rose hijab, a beach sunset "
                "behind them; the mirror reflects only the soft empty room; nobody else is in the scene",
         camera="close-up of the cabinet top and the frame, the frame in the upper half", amb="apartment_rain_day",
         sens="other", safe="Eethan appears only in a small framed photo (husband's hand on her shoulder)"),
    # ---------------------------------------------------------------- the test
    dict(to=68, reason="location and action change: she waits by the frosted window, the test face down",
         chars=["amaan"], loc="vanity",
         visual=f"Amaan standing at the narrow pale counter under a frosted glass window, both hands resting on the counter "
                f"edge, head bowed, listening; a small plain white plastic stick lies face down on the counter in front of "
                f"her; milky rain light from the frosted glass. {AMAAN_DAY}",
         camera="medium shot, eye level, her face in the upper third, the counter top as a calm lower third",
         amb="apartment_rain_day", sens="other",
         safe="the 'bathroom counter/basin' is shown as a plain counter by a frosted window; no toilet, sink or shower"),
    dict(to=70, reason="emotional turning point: she turns it over — two lines", chars=["amaan"], loc="vanity",
         visual=f"close-up of Amaan's trembling hand holding a small plain white plastic test stick showing two faint pink "
                f"lines in its little window, no text or logo on it; above it her stunned, disbelieving face, wide eyes "
                f"brimming, soft milky light from the frosted window. {AMAAN_DAY}",
         camera="close-up, her face in the upper third, the hand and stick in the middle", amb="apartment_rain_day",
         sens="other", safe="pregnancy test = a plain white stick with two faint pink lines, held in her hand"),
    dict(to=72, reason="character enters: Luha in the doorway; Amaan shows her the test", chars=["luha", "amaan"],
         loc="vanity",
         visual=f"Luha stopping in the open doorway, one hand flying to cover her mouth in shock, eyes wide and filling with "
                f"tears; Amaan facing her, speechless, holding out the small white test stick in her trembling hand. "
                f"{AMAAN_DAY}. Luha in her deep-teal dress and black hijab",
         camera="medium wide two-shot, eye level, both faces in the upper half", amb="apartment_rain_day"),
    dict(to=75, reason="action change / emotional peak: Luha holds her as she sobs — 'positive, really positive'",
         chars=["amaan", "luha"], loc="vanity",
         visual=f"Luha wrapping her arms tightly around her younger sister Amaan; Amaan sobbing against Luha's shoulder, eyes "
                f"squeezed shut, the small white stick still clutched in her hand; Luha's eyes closed with tears; two "
                f"sisters, fully covered. {AMAAN_DAY}. Luha in her deep-teal dress and black hijab",
         camera="medium close-up, eye level, both faces in the upper half", amb="apartment_rain_day",
         sens="other", safe="a sisters' hug (allowed); no bathroom fixtures shown"),
    dict(to=80, reason="action change: both sink to the floor; she lays her palm on her belly — 'hello'",
         chars=["amaan", "luha"], loc="hallway",
         visual=f"Amaan sitting on the hallway floor with her back against the cream wall, the white test stick in one hand "
                f"and her other palm resting gently on her still-flat stomach, looking down at it with tearful wonder and a "
                f"tiny smile; Luha kneeling beside her, tears on her cheeks, a hand on Amaan's arm. {AMAAN_DAY}. Luha in her "
                f"deep-teal dress and black hijab",
         camera="medium shot, slightly high angle, both faces in the upper half, the wooden floor as a calm lower third",
         amb="apartment_rain_day"),
    dict(to=82, reason="imagined scene: how Eethan would have taken the news", chars=["eethan"], loc="imagined_door",
         visual="an imagined moment: Eethan standing in the open front doorway in his navy t-shirt, holding the small white "
                "test stick in one hand, his other hand pressed to his forehead, his face breaking into laughing, crying joy, "
                "eyes shining with tears; nobody else in the frame",
         camera="medium shot, eye level, his face in the upper third", amb="memory", transition="dissolve",
         sens="intimacy", safe="the imagined joyful hug is shown as Eethan alone, overwhelmed with joy in the doorway"),
    dict(to=84, reason="return from the imagined scene: 'I wish Eethan were here' — Luha's hand on her shoulder",
         reuse="beat_029", chars=["amaan", "luha"], loc="hallway",
         visual="(reuse of beat_029: Amaan and Luha on the hallway floor)", amb="apartment_rain_day", transition="dissolve"),
    dict(to=89, reason="time jump: that night alone in the sitting room she plays the message — 'we met'",
         chars=["amaan"], loc="sitting_night",
         visual=f"Amaan sitting alone on the sofa at night, her phone lying on the cushion beside her with a soft glow, one "
                f"hand resting on her stomach, eyes full of tears and a trembling, wondering smile as she whispers; rain "
                f"streams down the dark balcony door; {PHONE}. {AMAAN_HOME}",
         camera="medium shot, eye level, her face in the upper third, the sofa seat and rug as a calm lower third",
         amb="apartment_rain_night", transition="black"),
    # ---------------------------------------------------------------- months later
    dict(to=93, reason="time jump ('months later'): the nursery Eethan built, golden evening light", chars=["amaan"],
         loc="nursery",
         visual="Amaan, now visibly pregnant with a gently rounded belly, standing beside a white wooden crib in the small "
                "children's room, one hand resting softly on her belly, looking at the neatly folded tiny baby clothes; warm "
                "golden late-afternoon rays slant across the crib; her phone lies on the windowsill. Amaan wears a loose "
                "long-sleeved ankle-length soft cream maternity dress and her dusty-rose hijab fully covering her hair and neck",
         camera="medium wide, eye level, her face in the upper third, the floor in golden light as a calm lower third",
         amb="nursery_evening", transition="black"),
    dict(to=97, reason="final emotional close: one hand on her chest, one on her belly — she smiles at the future",
         chars=["amaan"], loc="nursery",
         visual="close-up of Amaan, visibly pregnant, looking down at her rounded belly with a peaceful, hopeful smile and "
                "tear-bright eyes, one hand on her chest and the other resting on her belly, bathed in deep golden evening "
                "light by the window; the crib softly out of focus behind her. Amaan wears a loose long-sleeved "
                "ankle-length soft cream maternity dress and her dusty-rose hijab fully covering her hair and neck",
         camera="medium close-up, eye level, her face in the upper third, her hands in the middle", amb="nursery_evening"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# ---- the night she listens
sh(1, "From past midnight the rain kept falling. Amaan woke to the sound of that rain. As she felt the grief that had formed in her chest,")
sh(2, "she stayed staring at the ceiling without moving. She turned towards Eethan's side of the bed.",
   [("cloth_rustle", "އެނބުރިލިއެވެ", -24)])
sh(3, "His pillow there was still a little dented — from the way Amaan had hugged it. Suddenly Amaan's gaze stopped on her phone.")
sh(4, "For the first time since Eethan left, seeing the phone felt different. Amaan wanted to listen to the message on it.")
sh(5, "Her feelings were pushing her towards it, so Amaan did not want to delay even a moment. She picked up the phone at once. \"Just once.",
   [("cloth_rustle", "ފޯނުނެގިއެވެ", -24)])
sh(6, "Only once, I'll listen just once,\" she whispered. Then Amaan played the message. For a moment,")
sh(7, "all she heard was the soft sound of a car driving. Then she heard a deep breath she knew so well, one that hurt her heart. \"Hi love..\"",
   [("breath_heavy", "ނޭވާއެއްގެ", -20)])
sh(8, "Amaan's breath caught in her chest. It really was Eethan. \"I know you're still angry with me.\"",
   [("gasp", "ހިފެހެއްޓުނެވެ", -22)], hum=True)
sh(9, "Eethan went on calmly. \"I'm so sorry I walked out without waiting. I really should have waited until we'd both calmed down.")
sh(10, "I just didn't know what to say without making things worse.\" Amaan closed her eyes. Eethan sitting in the car,")
sh(11, "she could picture him searching for the right words. \"I thought of calling again, but I felt you'd need a little time.")
sh(12, "But I wanted to say something before I come home. You are not someone without hope. And you are not a failure.")
sh(13, "Not having a child of your own doesn't make you any less of a woman. I didn't marry you hoping you'd give me children.\"")
sh(14, "Amaan opened her eyes. \"I married you only for you. For grabbing the blanket while you sleep at night,")
sh(15, "and then accusing me of grabbing it. For crying when you see a cat on the street. For expecting me to eat the worst pancakes ever baked in the world.\"")
sh(16, "A small laugh escaped Amaan's throat. \"And because when I come home after a tiring day,")
sh(17, "you are the one who takes the whole day's tiredness away.\" Amaan pressed the phone hard against her chest. \"I know,",
   [("cloth_rustle", "ޖައްސައި", -24)])
sh(18, "you think I'm angry because we can't have a child. I dreamed of our child too.")
sh(19, "The day little feet would run through the house, the day toys would be scattered everywhere, the day they'd wake us up crying at three in the morning.")
sh(20, "But none of those things matter more than you.\" His voice grew softer.")
sh(21, "\"Even if we never have a child, I'll be the luckiest person in this world.")
sh(22, "Because I got to spend my whole life with you.\" Amaan bent forward and began to cry without a sound.",
   [("sob_breath", "ރޯންފެށިއެވެ", -22)], hum=True)
sh(23, "\"You are a perfect person. You will always be perfect. I love you endlessly.")
sh(24, "And if you ever felt that was a lie, I'm sorry for that. I'm coming home very soon.")
sh(25, "We'll talk properly, the two of us. And whatever we decide, we'll decide together. You'll never have to carry anything alone.\"")
sh(26, "Every sentence Eethan spoke cut deep into Amaan's heart. \"And if one day we meet a little miracle, tell that child for me,")
sh(27, "even without knowing its name, that its father loved its mother endlessly. I'll always choose you. Every time.", hum=True)
sh(28, "In every life. I'm coming home very soon. Try to get some sleep. Don't forget to eat. Don't make pancakes without me.", hum=True)
sh(29, "We both know you need someone to look after you.\" The recording ended. Amaan sat without moving.")
sh(30, "The phone was still pressed to her ear. Then she played the message again. And again.")
sh(31, "Sometimes she cried. Sometimes she laughed at the bit about the pancakes. Sometimes, overwhelmed when Eethan said her name, she stopped the recording.",
   [("sob_breath", "ރޮވުނެވެ", -24)])
sh(32, "But every time, she let herself listen to that voice a little more.")
# ---- the first days and weeks
sh(33, "In the first days after hearing Eethan's message, wherever Amaan went she carried the phone in her hand.")
sh(34, "Folding laundry, washing the dishes, even sitting on the balcony with her morning coffee, she listened to that message. She didn't listen to it to cry.",
   [("cloth_rustle", "ފައްޖަހާއިރު", -24), ("cup_clatter", "ތަށިދޮންނައިރު", -24)])
sh(35, "She listened because hearing Eethan's voice now felt like holding on to something precious saved from a fire.")
sh(36, "Grief still came without any warning. Times she went to pour tea into a second cup and remembered there was no one to drink it, and times she woke thinking she'd heard Eethan call her in the room.",
   [("pour", "ސައިއަޅަން", -20)])
sh(37, "But when loneliness took hold, she no longer felt the kind of loneliness she used to feel.")
sh(38, "In her hands were Eethan's precious words. The weeks went by. One afternoon Amaan threw all the flowers people had brought into the bin.",
   [("leaves_rustle", "އުކާލިއެވެ", -20)])
sh(39, "And stood beside the bin, looking at the empty vases.")
sh(40, "Keeping the flowers didn't feel right to her. Throwing them away didn't feel right either. That night she cleaned the room.")
sh(41, "She changed the sheets, opened the windows, and washed the blanket Eethan always complained was too thin.",
   [("cloth_rustle", "ބަދަލުކޮށް", -22), ("creak", "ހުޅުވައި", -22)])
sh(42, "For months she had slept on Eethan's side, because it was the only place where the loneliness felt even a little lighter.")
sh(43, "But that night she moved back to her own side. \"I'm trying to move on with my life,\" she said softly into the darkness.",
   [("sigh", "ބުނެލިއެވެ", -22)])
# ---- the nausea
sh(44, "The next morning Amaan woke before the alarm, feeling an unusual heaviness in her body.")
sh(45, "As she got up and sat, she felt sick. She thought it was because of the grief.")
sh(46, "The night before, she had spent looking at old photos of Eethan. Crying over every photo,")
sh(47, "she finally fell asleep with a photo pressed to her chest. She hadn't eaten that night either. Even the thought of food turned her stomach.")
sh(48, "But when the nausea came again after she made tea, Amaan stood still in the kitchen with a hand on her stomach.",
   [("pour", "ހެދުމަށްފަހުވެސް", -22)])
sh(49, "Suddenly thoughts flooded Amaan's mind. What if it were true? At once Amaan shook her head. She had felt this before, too.")
sh(50, "Every time her period was late, every morning her body changed in some unusual way, hope came alive again in her heart.")
sh(51, "But every time that hope ended — with a test, or with the doctor's sympathetic silence.")
sh(52, "She did not want to face that pain again. Especially not on a day without Eethan. All day she tried not to think about it.")
sh(53, "But in the afternoon the nausea began again. Seeing how Amaan was, Luha looked at her with concern. \"What's wrong?\" Luha asked.")
sh(54, "\"Nothing.\" \"These days that's what you always say,\" Luha said, raising her voice. \"I'm dizzy and I feel sick.\"")
sh(55, "Amaan said, looking up. \"Since when?\" \"Maybe a month.\" \"Amaan. When was your last period?\"")
sh(56, "Luha's expression changed. \"I don't know. I don't keep track of dates.\" Amaan stood there, stunned.")
sh(57, "It was as if that question circled the whole room and came back to reach her. Since Eethan passed away, counting time was something she simply couldn't do.",
   hum=True)
sh(58, "The day of the accident she would remember all her life. But everything else had faded. \"Have you taken a test?\"")
sh(59, "Luha came and sat beside her. Amaan shook her head. \"Because it won't be that. I can't bear that pain again.\"",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(60, "When Luha asked why, Amaan answered. Then Luha spoke, her voice serious. \"You don't have to hope.")
sh(61, "Just take a test.\" Kindness showed on Luha's face. She took Amaan's hand. Amaan looked at their joined hands.")
sh(62, "Even the thought frightened her. A pregnancy test is a tiny plastic thing. But she knew the weight of grief it could bring.")
sh(63, "Five years of waiting, every test that came back negative, every time she imagined how she would tell Eethan the news and then had to be disappointed.")
sh(64, "\"What if it's negative?\" she asked softly. \"Then we'll face it.\" \"What if it's positive?\" \"We'll face that too.\" Tears came to Luha's eyes.",
   hum=True)
sh(65, "Amaan looked towards the sitting room. Under the mirror there was a photo of Eethan. He was smiling.")
sh(66, "His hand rested on Amaan's shoulder. She remembered Eethan's voice. As Amaan waited, the test lay face down on the bathroom counter.")
# ---- the test
sh(67, "She stood with her hands on the edge of the basin, listening to Luha moving about in the kitchen. Through the house drifted the smell of tea and the dampness of the rain.")
sh(68, "Amaan looked at the test. Her heart began to race. Slowly she turned the test over. Two lines were showing.",
   [("heartbeat", "އަވަސްވިއެވެ", -20)], hum=True)
sh(69, "She couldn't believe what was in front of her. She stood staring at the test, waiting for the lines to fade away,")
sh(70, "and for her to realise she had been mistaken. But the lines didn't fade. They stayed, very clear. \"Luha?\" Amaan's hands began to tremble.",
   [("breath", "ތުރުތުރުލާން", -22)], hum=True)
sh(71, "Her elder sister stopped in the doorway. Just seeing Amaan's face, Luha knew what had happened. Amaan couldn't say a word.")
sh(72, "She only showed the test in her hand. Luha took it, looked at it, and put her hand over her mouth. Amaan began to cry.",
   [("gasp", "އަތްއެޅިއެވެ", -20)])
sh(73, "A flood of tears with nothing holding them back. Luha came in and wrapped her arms around her. \"Positive,\" Amaan said softly.",
   [("sob_breath", "އޮހޮރުމެކެވެ", -20)], hum=True)
sh(74, "\"Really positive.\" Amaan nodded, sobbing even harder. After five years of waiting, of medicines,",
   [("sob_breath", "ގިސްލާފައި", -22)])
sh(75, "of lost hopes, at last a life was forming inside her. The dream Eethan had dreamed.", hum=True)
sh(76, "A life she thought would never become real. She sat down on the floor. The test was still in her hand.",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(77, "Luha knelt down beside her. Tears were flowing from her eyes too. \"Let's go and see a doctor soon,\" Luha said.")
sh(78, "Amaan looked at her stomach. It was still just as it had been. Nothing had changed on the outside.")
sh(79, "Slowly she rested her palm on her stomach. \"Hello,\" she whispered. Then she looked towards the door,", hum=True)
sh(80, "smiling without knowing why, with an innocent hope that Eethan might walk in and ask why the two of them were crying.")
sh(81, "She imagined giving Eethan the news, his face changing as he stared at the test,")
sh(82, "how he would wrap his arms around her, laughing and crying with joy, and then immediately start worrying about all the things they hadn't bought yet.")
sh(83, "\"I wish Eethan were here,\" Amaan said. \"I know.\" Luha laid her hand on her shoulder.")
sh(84, "\"He said he'd come home very soon.\" Amaan pressed the test hard against her chest. Luha didn't try to answer,",
   hum=True)
sh(85, "because there was no answer that could ease the pain of those words. That night, sitting alone in the sitting room, Amaan")
sh(86, "listened to Eethan's last message on her phone, the volume turned up a little. She had listened to it many times since morning. But")
sh(87, "now every word of it seemed to give her a new meaning. \"If we ever meet our little miracle...\" \"We met.\"", hum=True)
sh(88, "Amaan said softly. And she rested her hand on her stomach. Her eyes filled with tears.",
   [("breath", "ފުރުނެވެ", -24)])
sh(89, "Holding her stomach, Amaan listened until the message ended. When it ended, she played it again. Months later.")
# ---- months later
sh(90, "In the little children's room Eethan had made years ago, Amaan stood with her hand resting gently on her belly.")
sh(91, "The golden rays of the evening sun fell across the small crib and the folded baby clothes laid out there.")
sh(92, "She set the phone down by the window and played Eethan's message for the very last time. His voice spread through the silent room.")
sh(93, "She felt as if Eethan were standing beside her. The dream the two of them had dreamed together, the baby's room, those tiny clothes — she hoped Eethan could see them.",
   hum=True)
sh(94, "Then Amaan looked down at her belly. \"Eethan loved you so much, little one,\" she said softly.", hum=True)
sh(95, "Outside, as the sunlight softened, the whole room glowed gold. Amaan laid one hand on her chest.")
sh(96, "And with the other she touched the tiny child in her belly. Eethan is gone.")
sh(97, "But the love Eethan gave Amaan is still with her. In that moment, for the first time since Eethan left, she smiled as she thought about her happy future.",
   hum=True)
SHOTS = S

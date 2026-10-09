"""Beat/shot plan for Emme Fahu Message episode 327 (used by plan_beats.py).
The negative result in Dr. Mathews' office, the silent drive home in the rain, the kitchen argument as the evening rain
starts, Eethan leaving with the car keys, Amaan on the kitchen floor, the declined calls and the voice-message
notification. Rules: married couple -> no kissing/embracing, hands held in the car only; no needles (pill boxes instead);
hijab fully covering hair on every woman; phones show only a soft blank glow; no readable text anywhere."""

AMAAN = ("Amaan in her loose long-sleeved ankle-length cream-oatmeal dress and dusty-rose hijab fully covering her hair "
         "and neck")
E_OUT = ("Eethan wearing a dark-olive zip-up rain jacket over his navy t-shirt and dark jeans (NOT the grey joggers of the "
         "reference)")
E_HOME = ("Eethan in his plain navy crew-neck t-shirt and dark jeans (NOT the grey joggers of the reference), his rain "
          "jacket taken off")
GAP = "a clear gap between them, they do not touch"
NOTEXT = "the phone screen is only a soft blank glow with no text, no icons, no numbers"

LOC = {
    "clinic": "Dr. Mathews' calm consulting room in a private fertility clinic in Malé: cream walls, a wooden desk with a "
              "closed plain folder, a few blank sheets and a small plant, a computer monitor turned away, two patient "
              "chairs facing the desk, a tall window with rain-streaked glass and the grey blurred city behind it",
    "car": "inside a small modest hatchback car driving home through Hulhumalé in the rain, wet grey streets, apartment "
           "blocks and palms blurred behind rain-streaked windows, the wipers sweeping the windscreen",
    "kitchen_quiet": "the tiny narrow kitchen of a slightly old third-floor apartment in Hulhumalé: pale cream wall tiles, a "
                     "steel sink under a small window, light wooden cabinets, a small fridge, a short counter, a round "
                     "plain analog wall clock with no numerals, a doorway through to a small sitting room with a sofa and "
                     "small blurred framed photos, a red mug on the counter",
    "window": "the sitting-room window and glass balcony door of a third-floor apartment in Hulhumalé, looking out over "
              "wet rooftops, apartment blocks and palm trees toward a darkening sea-grey sky, a sofa arm and a small "
              "lamp at the edge of the frame",
    "kitchen": "the tiny narrow kitchen of a slightly old third-floor apartment in Hulhumalé in the evening: pale cream "
               "wall tiles, a steel sink under a small rain-streaked window, light wooden cabinets, a small fridge, a "
               "short counter with a few grocery bags and a red mug, a round plain analog wall clock with no numerals, a "
               "warm amber pendant lamp, a doorway to the small sitting room",
    "kitchen_night": "the same tiny narrow apartment kitchen later in the evening: pale cream wall tiles, a steel sink "
                     "under a small window streaming with heavy rain, light wooden cabinets, a small fridge, a short "
                     "counter, a round plain analog wall clock with no numerals, one warm amber pendant lamp, a doorway "
                     "to the small sitting room and the narrow entrance hall",
    "entrance": "the narrow entrance hall of the small apartment seen from the kitchen doorway: a plain wooden front door "
                "with a metal lever handle, a small side table by the door with a little bowl for keys, small blurred "
                "framed photos on the wall, a coat hook with an umbrella",
    "floor": "the tiny apartment kitchen seen from low down near the floor: the lower wooden cabinet doors, the edge of "
             "the counter above, the small rain-streaked window, the amber pendant lamp glowing overhead",
}
MOOD = {
    "clinic": "rainy grey afternoon, soft flat window light mixed with a warm desk lamp, hushed and heavy, a kind but sad "
              "atmosphere, small vermilion accent of a red pen holder",
    "car": "rainy grey afternoon, cool blue-grey light through streaming glass, soft reflections of red traffic lights "
           "smeared by the rain, silent, numb and tender",
    "kitchen_quiet": "early evening turning to night, the apartment dim and still, a single warm amber lamp against "
                     "cold grey-blue window light, an oppressive heavy silence",
    "window": "dusk turning to a rainy night, dark grey-blue rain clouds massing over the city, the last light fading, "
              "the first raindrops on the glass, a warm amber lamp reflection inside",
    "kitchen": "rainy evening, the first rain outside, warm amber pendant light inside against grey-blue window light, "
               "quiet tension and exhaustion",
    "kitchen_night": "rainy night, heavy rain streaming down the dark window, one warm amber lamp, deep blue shadows, "
                     "raw grief and heartbreak",
    "entrance": "rainy night, warm amber lamp light in the hall, the dark front door, a tender and tragic farewell mood",
    "floor": "rainy night, dim amber lamp light from above, cold blue shadows on the floor, loneliness and regret, the "
             "soft glow of a phone",
}

BEATS = [
    dict(to=2, reason="episode opening: the negative result in Dr. Mathews' office", chars=["amaan", "dr_mathews", "eethan"],
         loc="clinic",
         visual=f"{AMAAN} sitting very still on a patient chair in front of the desk, her face blank and numb, staring at the "
                f"doctor; {E_OUT} sitting in the chair beside her, looking at her with worry; Dr. Mathews behind the desk "
                "facing them, his hands resting on a closed plain folder, a kind but sad expression",
         camera="medium wide three-shot, eye level, from beside the desk so all three faces are in the upper half",
         amb="clinic_room"),
    dict(to=5, reason="focus change: Dr. Mathews explains levels, percentages and statistics", chars=["dr_mathews", "amaan"],
         loc="clinic",
         visual="Dr. Mathews leaning forward across the desk, gesturing gently over a few blank sheets of paper with soft "
                "abstract blurred grey graphs and no writing, explaining patiently; in the soft-focus foreground the side "
                f"of {AMAAN}, her eyes distant and unfocused, not really listening",
         camera="over-the-shoulder medium shot from behind Amaan's shoulder toward the doctor", amb="clinic_room"),
    dict(to=8, reason="focus change: Eethan asks the doctor calm, practical questions", chars=["eethan", "amaan", "dr_mathews"],
         loc="clinic",
         visual=f"{E_OUT} leaning forward in his chair, elbows on his knees, asking the doctor a question with calm focused "
                f"eyes; {AMAAN} beside him turning her head to look at him with quiet admiration and sadness; Dr. Mathews "
                "partly visible at the edge of the frame across the desk",
         camera="medium two-shot of the couple from the doctor's side of the desk", amb="clinic_room"),
    dict(to=10, reason="scene change: the silent drive home in the rain", chars=["amaan", "eethan"], loc="car",
         visual=f"{AMAAN} in the passenger seat, her head turned to the side window, watching raindrops slide down the glass, "
                f"her reflection faint in it, a hollow quiet face; {E_OUT} driving beside her, eyes on the road; the "
                "wipers sweeping the rain-blurred windscreen",
         camera="medium shot from the back seat between the two front seats, slightly to Amaan's side", amb="car_rain"),
    dict(to=12, reason="action change: at a red light Eethan rests his hand on hers", chars=["eethan", "amaan"], loc="car",
         visual=f"the car stopped at a red light; {E_OUT} reaching across the centre console and resting his hand on "
                f"{AMAAN}'s hand on the console, her fingers squeezing his, both thin silver wedding rings visible; both "
                "faces above, looking ahead silently, a red traffic-light glow smeared by rain on the windscreen",
         camera="medium close-up from the dashboard, faces in the upper part, the joined hands in the middle of the frame",
         amb="car_rain", sens="intimacy", safe="married couple: only a hand resting on a hand in the car, no other touch"),
    dict(to=14, reason="time jump: that evening the apartment is heavily silent, the clock ticks loudly", loc="kitchen_quiet",
         visual="the empty tiny kitchen and the dim sitting room beyond the doorway, no people; the round plain analog wall "
                "clock without any numerals in sharp focus on the wall, two unwashed mugs by the sink, grocery bags "
                "slumped on the counter, a heavy stillness",
         camera="medium shot, eye level, the clock in the upper third", amb="apartment_quiet_night",
         transition="black"),
    dict(to=17, reason="scene change: dark rain clouds gather over the city, the first drops hit the window", loc="window",
         visual="view through the sitting-room window over wet Hulhumalé rooftops and palm trees, heavy dark grey rain "
                "clouds gathering over the city in the fading dusk light, the first fat raindrops just landing on the "
                "glass, a warm amber lamp reflected faintly in the pane; no people",
         camera="wide shot through the glass, the sky in the upper two-thirds, the window sill as a calm lower third",
         amb="apartment_quiet_night"),
    dict(to=20, reason="scene change: Amaan scrubbing a mug at the sink while Eethan unpacks groceries behind her",
         chars=["amaan", "eethan"], loc="kitchen",
         visual=f"{AMAAN} standing at the kitchen sink with her back half-turned, scrubbing one spot on a red coffee mug, "
                f"lost in thought, her face in profile; behind her {E_HOME} putting fruit and vegetables into the small "
                f"fridge, tins and a loaf of bread on the counter, glancing at her; {GAP}",
         camera="medium wide, eye level, from the doorway of the kitchen", amb="apartment_rain_night"),
    dict(to=23, reason="focus change: Eethan breaks the silence and suggests a trip to the sea", chars=["eethan", "amaan"],
         loc="kitchen",
         visual=f"{E_HOME} leaning against the counter with his arms loosely folded, giving a hopeful gentle smile as he "
                f"talks; {AMAAN} at the sink in the foreground, her eyes still fixed on the red mug in her hands, not "
                f"answering; {GAP}",
         camera="medium shot over Amaan's shoulder toward Eethan", amb="apartment_rain_night"),
    dict(to=25, reason="action change: Amaan closes her eyes and refuses; Eethan's smile fades", chars=["amaan", "eethan"],
         loc="kitchen",
         visual=f"close on {AMAAN}, her eyes closed in exhaustion, drying the red mug with a cloth; in soft focus behind "
                f"her {E_HOME}, his smile fading, nodding slowly",
         camera="medium close-up on Amaan, Eethan soft in the background", amb="apartment_rain_night"),
    dict(to=29, reason="action change: Eethan steps toward her with concern; her broken laugh", chars=["eethan", "amaan"],
         loc="kitchen",
         visual=f"{E_HOME} taking a step toward Amaan, looking at her with tender concern; {AMAAN} by the counter letting out "
                f"a broken, tearful laugh, her eyes wet and exhausted, one hand pressed to her forehead; {GAP}",
         camera="medium two-shot, eye level, side view", amb="apartment_rain_night"),
    dict(to=33, reason="action change: Amaan turns to face him: five years of treatments", chars=["amaan", "eethan"],
         loc="kitchen",
         visual=f"{AMAAN} turned to face Eethan, her voice trembling, her eyes full of pain and anger, one hand gripping the "
                "edge of the counter; on the counter beside her a plastic weekly pill organiser and two plain blank "
                f"medicine boxes; {E_HOME} standing a step away, listening",
         camera="medium shot, the pill organiser in the middle of the frame on the counter, faces in the upper third",
         amb="apartment_rain_night", sens="other",
         safe="the needles and marks on her arms are not shown; a pill organiser and blank medicine boxes stand in for "
              "five years of treatment"),
    dict(to=36, reason="action change: Eethan moves closer, her tears begin", chars=["eethan", "amaan"], loc="kitchen",
         visual=f"{E_HOME} moving closer, his face pained and sincere; {AMAAN} facing him with tears starting to spill from "
                f"the corners of her eyes, shaking her head, her lips pressed tight; {GAP}",
         camera="medium close two-shot, faces in the upper half", amb="apartment_rain_night"),
    dict(to=38, reason="emotional turning point: close-up, 'every month...', her voice breaks", chars=["amaan"],
         loc="kitchen",
         visual=f"close-up of {AMAAN}, a single tear rolling down her cheek, her mouth trembling mid-sentence, eyes lowered, "
                "the warm amber lamp behind her and the rain-streaked window soft in the background",
         camera="close-up, face in the upper half, her hands at the counter edge below", amb="apartment_rain_night"),
    dict(to=41, reason="action change: Eethan reaches for her hand, she pulls it away; the rain grows louder",
         chars=["eethan", "amaan"], loc="kitchen_night",
         visual=f"{E_HOME} with one open hand stopped in mid-air where her hand used to be, his face falling; {AMAAN} a "
                "full step away from him, both of her hands pulled back and clasped tightly against her chest, her "
                "shoulder turned away from him, eyes down; a wide empty gap of air between his hand and her, nobody "
                "touches; behind them the small kitchen window streaming with heavy rain",
         camera="medium two-shot, the two hands with a gap between them in the centre of the frame",
         amb="apartment_rain_night"),
    dict(to=45, reason="action change: Amaan says they should stop the treatments; Eethan agrees and she flares",
         chars=["amaan", "eethan"], loc="kitchen_night",
         visual=f"{AMAAN} looking up at Eethan, wounded and angry, her hands spread in disbelief; {E_HOME} across from her "
                f"by the fridge, frowning in confusion; {GAP}, the counter between them",
         camera="medium wide two-shot, eye level", amb="apartment_rain_night"),
    dict(to=49, reason="focus change: Eethan steady — 'I'm choosing you'", chars=["eethan", "amaan"], loc="kitchen_night",
         visual=f"{E_HOME} speaking softly but firmly, his eyes steady and loving, one hand open in front of his chest; in "
                f"the soft-focus foreground the dusty-rose hijab and shoulder of {AMAAN} as she looks at him",
         camera="over-the-shoulder medium close-up on Eethan", amb="apartment_rain_night"),
    dict(to=53, reason="emotional turning point: Eethan's own broken dreams; he looks away for the first time",
         chars=["eethan"], loc="kitchen_night",
         visual=f"{E_HOME} turning his face away toward the dark rain-streaked kitchen window, his eyes glistening, jaw "
                "tight, his voice breaking; his reflection faint in the wet glass",
         camera="medium close-up in profile, face in the upper half", amb="apartment_rain_night"),
    dict(to=55, reason="action change: Amaan almost steps toward him, then guilt wins", chars=["amaan", "eethan"],
         loc="kitchen_night",
         visual=f"{AMAAN} half a step toward Eethan, then stopping herself, one hand clenched at her chest, her face torn "
                f"between longing and guilt as she speaks; {E_HOME} a few steps away looking at her; {GAP}",
         camera="medium wide two-shot, eye level", amb="apartment_rain_night"),
    dict(to=59, reason="emotional turning point: her words strike him; his face drains", chars=["eethan", "amaan"],
         loc="kitchen_night",
         visual=f"close on {E_HOME}, his face gone pale and stunned as if he had been struck, eyes hurt, lips parted, "
                f"asking quietly; {AMAAN} soft in the background by the counter, looking at him",
         camera="medium close-up on Eethan, Amaan out of focus behind", amb="apartment_rain_night"),
    dict(to=62, reason="action change: Amaan turns away crying; Eethan closes his eyes", chars=["amaan", "eethan"],
         loc="kitchen_night",
         visual=f"{AMAAN} turned away toward the sink, tears running down her cheeks; {E_HOME} standing apart with his eyes "
                "closed, head slightly bowed, speaking softly; the wide empty space of the kitchen floor between them",
         camera="medium wide, eye level, both in the upper half, the empty floor below", amb="apartment_rain_night"),
    dict(to=65, reason="scene/action change: Eethan takes the car keys from the table by the front door",
         chars=["eethan", "amaan"], loc="entrance",
         visual=f"{E_OUT} by the small side table at the front door, picking up the car keys, looking back over his "
                f"shoulder with a very small tired smile; in the kitchen doorway in the foreground {AMAAN} looking up at "
                "him, wanting to speak",
         camera="medium wide from behind Amaan's shoulder down the narrow hall", amb="apartment_rain_night"),
    dict(to=68, reason="action change: his hand on the door handle — 'I love you' — then he goes", chars=["eethan", "amaan"],
         loc="entrance",
         visual=f"{E_OUT} at the front door with his hand on the metal handle, the door slightly open onto the dark rainy "
                f"stairwell, looking back with sad love in his eyes; {AMAAN} frozen still in the kitchen doorway, her lips "
                f"pressed together; {GAP}",
         camera="medium wide down the hall, the door in the upper half", amb="apartment_rain_night"),
    dict(to=70, reason="action change: alone, Amaan slides down to the kitchen floor", chars=["amaan"], loc="floor",
         visual=f"{AMAAN} sitting on the kitchen floor with her back against the lower cabinet doors, knees drawn up under "
                "her long dress, her face covered with both hands, shoulders shaking; the empty kitchen around her",
         camera="medium shot, slightly high angle, Amaan in the upper-middle of the frame, calm floor below",
         amb="apartment_rain_night", sens="other",
         safe="'collapsed to the floor' shown as sitting against the cabinets, face in her hands"),
    dict(to=72, reason="action change: her phone vibrates on the counter — Eethan calling", chars=["amaan"], loc="floor",
         visual=f"low view from the floor: a phone glowing at the edge of the counter above, {NOTEXT}; {AMAAN} still sitting "
                "on the floor below it, wiping tears from her cheek with one hand, looking up at the phone without "
                "moving",
         camera="low angle, the glowing phone in the upper third, Amaan's face in the middle", amb="apartment_rain_night"),
    dict(to=75, reason="action change: the voice-message notification; she turns the phone face down", chars=["amaan"],
         loc="floor",
         visual=f"{AMAAN} standing alone at the kitchen counter, the only person in the image, looking down with a "
                f"tear-stained, proud and hurt face at a phone lying face up on the counter that glows softly, {NOTEXT}; "
                "her hand hovering just above it, about to turn it over; plain dim kitchen wall behind her, no pictures, "
                "no figures",
         camera="close-up, the glowing phone in the centre, her face soft in the upper third", amb="apartment_rain_night",
         sens="other", safe="the notification text is not shown; only a blank glowing screen"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"The result is negative.\" Amaan showed no emotion at all. She only sat looking at the doctor. Negative.", hum=True)
sh(2, "That word no longer surprised her. Every time she heard it, it was as if something inside her emptied out. Dr.")
sh(3, "Mathews carried on talking, explaining hormone levels, the percentages of conception, the things that could be "
      "changed, numbers and statistics.")
sh(4, "Numbers. Always numbers. Not one of those numbers answered the only question Amaan wanted to ask. 'Why?")
sh(5, "Why does it happen for everyone else, but not for us?' Although Amaan didn't hear even half of what was said,")
sh(6, "she nodded politely. Sitting beside her, Eethan asked questions. Calm questions. Practical questions.")
sh(7, "\"What options do we have? Will another cycle improve the chances? What do you recommend, doctor?\"")
sh(8, "Amaan admired Eethan for that. Even now, when every door Amaan could see was closed, Eethan kept looking for "
      "another door.")
sh(9, "The drive home was silent. The windscreen wipers moved at a steady pace while raindrops slowly struck the "
      "windscreen.", [("wipers", "ވައިޕަރުތައް", -18)])
sh(10, "Amaan sat watching the raindrops slide down the glass of the door. Through them the world outside looked like a "
       "blurred grey kind of beauty.")
sh(11, "When they stopped at a red light, Eethan reached across the middle of the car and rested his hand on Amaan's "
       "hand. He said not a word.")
sh(12, "Only warmth. Amaan squeezed Eethan's fingers. Eethan squeezed back. That evening the apartment was unusually "
       "silent.")
sh(13, "It was not the comfortable silence that was always there between Amaan and Eethan. This silence was far heavier.")
sh(14, "Even the ticking of the clock on the kitchen wall seemed louder than usual. Every second that passed on that "
       "clock dragged by in unbearable detail.", [("clock_tick", "ގަޑީގެ", -18)])
sh(15, "Outside, the sky had turned a dark grey. Dimming the last light of the day, rain clouds were gathering over the "
       "city.")
sh(16, "Although the forecast had said it would rain, that morning neither of them had paid it much attention.")
sh(17, "Suddenly the first drops of rain began to tap softly on the sitting-room window. Amaan stood at the kitchen sink, "
       "washing a coffee mug.", [("rain_start", "ތިކިތައް", -18)])
sh(18, "She had been scrubbing one spot on that mug for almost five minutes. Behind her, Eethan was taking out and "
       "putting away the groceries he had bought on the way back from the clinic.",
   [("paper_shuffle", "ކޮތަޅުތަކުން", -22)])
sh(19, "He put the fresh fruit and vegetables in the fridge, lined the tins up neatly in the cupboard, and set a loaf of "
       "bread on the counter.", [("cup_clatter", "ކަބަޑުތެރޭގައި", -24)])
sh(20, "Since coming home neither of them had said a word. Not out of anger. Because neither of them knew how to begin.")
sh(21, "\"I was thinking.\" At last Eethan broke the silence. \"Hm?\" Amaan's eyes were still fixed on the mug.")
sh(22, "\"Maybe this holiday we could get out of the city. Just the two of us.\" Amaan didn't answer. \"We could go "
       "somewhere by the sea.")
sh(23, "Rent a little cabin, the kind you'd like.\" He smiled gently. Still no answer.")
sh(24, "Amaan slowly closed her eyes. \"I don't want to go.\" Eethan's smile faded. \"That's fine.")
sh(25, "We don't have to go.\" He nodded slowly. Amaan dried the mug and put it back in the cupboard. \"I don't want to "
       "do anything.\"", [("cup_clatter", "ކަބަޑަށް", -20)])
sh(26, "Eethan stood looking at Amaan with care. Amaan looked utterly exhausted. Not physically. Emotionally.")
sh(27, "Like someone who has carried something far too heavy for far too long. Eethan walked toward Amaan. \"Amaan...\"")
sh(28, "Eethan called in a soothing voice. \"I'm fine,\" Amaan answered. \"You don't have to be fine.\"")
sh(29, "When Eethan said that, Amaan laughed. It was not a happy laugh. It was the kind of laugh that escapes when you "
       "are worn out from crying. \"Just great.\"", [("sob_breath", "ހިނިގަނޑެކެވެ", -24)])
sh(30, "Amaan turned toward Eethan. \"I'm not fine.\" The words echoed through the whole apartment.")
sh(31, "\"I've spent five years letting doctors put needles into my body. Keeping track of the times I have to take my "
       "medicines.")
sh(32, "There are marks on my arms that feel like they'll never fade.\" Her voice was trembling.")
sh(33, "\"I keep hearing pregnancy news from people who don't even try. Do you know what that feels like, Eethan?\"")
sh(34, "She let out another bitter laugh. \"I know.\" Eethan moved closer. \"No. You don't know.")
sh(35, "You don't know what that feeling is.\" She swallowed hard. Tears began to flow from the corners of her eyes.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(36, "\"You don't know how it feels when your own body fails you.\" Eethan opened his mouth.")
sh(37, "But before Eethan could speak, Amaan went on. \"Every month... every single month I tell myself this time will "
       "be different.\"")
sh(38, "Her voice broke. A tear rolled down her cheek. \"And every month...\" She couldn't finish.",
   [("sob_breath", "ކަރުނައެއް", -22)], hum=True)
sh(39, "Eethan gently tried to take her hand. But Amaan pulled her hand away. \"Amaan.\" Eethan's heart sank. "
       "\"I'm tired.")
sh(40, "I'm so tired of hoping.\" The room fell silent. The sound of the rain on the window grew much louder. Eethan "
       "waited.", [("rain_start", "ވާރޭގެ", -18)])
sh(41, "Over the years he had learned that sometimes, before listening, you have to give people room to let out what is "
       "in their heart.")
sh(42, "\"I think we should stop this. The treatments. I can't do this any more.\" She looked up.")
sh(43, "\"If that's what you want, OK. I'll support whatever you decide.\" Eethan nodded slowly. \"Eethan...")
sh(44, "Just like that? That easily?\" Amaan snapped. \"What do you mean?\" Eethan frowned.",
   [("breath_heavy", "އެސްފިޔަ", -22)])
sh(45, "\"You don't even want to fight for it. I fought for five years with you.")
sh(46, "And you're giving it up that easily.\" \"No. I'm choosing you, Amaan.")
sh(47, "Children or no children, I don't care.\" There was a calm in his voice. Amaan stood looking at him. \"I care.")
sh(48, "I always cared,\" Amaan said. \"I know.\" \"But Eethan...\" Amaan struggled to find the words.")
sh(49, "\"You're fine with it.\" \"No.\" Eethan's answer came at once. \"I'm not fine. My heart is broken.")
sh(50, "I wanted to teach our son to ride a bicycle.\" For the first time he looked somewhere other than Amaan's face.")
sh(51, "\"I wanted to dance with you at our daughter's wedding. I wanted all of it.\" His voice broke.", hum=True)
sh(52, "\"But I want it with you.\" He looked at Amaan again. A silence formed between them.")
sh(53, "\"If that dream costs me you, then that dream is worth nothing.\" He swallowed hard.", hum=True)
sh(54, "For one fragile moment Amaan wanted to step into Eethan's arms. But the guilt she had carried for years was "
       "stronger than Eethan's love.")
sh(55, "\"You're only saying that to comfort me. One day you'll wake up and realise you married the wrong woman.\"")
sh(56, "When Amaan said that, Eethan's expression changed. \"No. Amaan.\" The colour drained completely from his face.",
   [("gasp", "ބަދަލުވެގެން", -24)])
sh(57, "\"You deserve someone who can give you a real family.\" The words hung in the air. Forever.", hum=True)
sh(58, "Eethan stood looking at Amaan as if she had struck him. Not because she had questioned their future.")
sh(59, "Because she had questioned his love. \"Do you really think that of me?\" His voice was barely audible.")
sh(60, "\"I think I've ruined your life.\" Amaan looked away. Her tears began to flow again.",
   [("sob_breath", "ކަރުނަތައް", -24)])
sh(61, "Eethan closed his eyes. \"You have never ruined a single day of my life.\" When he spoke again,", hum=True)
sh(62, "his voice was even softer than before. Amaan didn't answer. Eethan waited. No answer came. \"I'm going for a "
       "drive.\"")
sh(63, "At last Eethan reached for the car keys on the table by the front door. \"Eethan...\" Amaan looked up.",
   [("keys_jingle", "ތަޅުދަނޑިއަށް", -18)])
sh(64, "\"I just need some fresh air right now.\" He gave a very small smile. Amaan wanted to stop him.")
sh(65, "She wanted to say sorry. She wanted to tell him that none of what she had said came from her heart.")
sh(66, "Instead she stayed where she was, without moving. Eethan walked to the door and put his hand on the handle. "
       "\"I love you so much.\"", [("lock_click", "ތަޅުގަނޑުގައި", -22)], hum=True)
sh(67, "Silence. Not because Amaan didn't love Eethan. But because pride snatched the words away before they could "
       "reach her lips.")
sh(68, "Eethan waited a few more seconds. Then he slowly opened the door. She heard it close behind him.",
   [("door_open", "ހުޅުވާލިއެވެ", -20), ("door_close", "ލެއްޕުނު", -16)])
sh(69, "The apartment suddenly felt enormous. Amaan sank to the kitchen floor. The tears poured out all at once. Hard.",
   [("cloth_rustle", "ވެއްޓުނެވެ", -22), ("sob_breath", "ކަރުނަތައް", -20)], hum=True)
sh(70, "Unbearably. She covered her face with both hands. \"I didn't mean it...\" she whispered into the empty "
       "apartment.", hum=True)
sh(71, "Just then her phone on the kitchen counter began to vibrate. Eethan was calling. She sat watching it until it "
       "stopped ringing.", [("phone_buzz", "ވައިބްރޭޓްވާން", -16)])
sh(72, "A few seconds later it vibrated again. Eethan calling again. She wiped her tears. \"I can't.\" She declined the "
       "call.", [("phone_buzz", "ވައިބްރޭޓްވިއެވެ", -16)])
sh(73, "The apartment fell silent again. Another minute passed. The phone screen lit up again. This time it wasn't a "
       "call.", [("phone_buzz", "ދިއްލުނެވެ", -20)])
sh(74, "It was a notification: '1 voice message from Eethan.' Amaan looked at the screen. Her pride stood firm in the "
       "middle of that notification.", hum=True)
sh(75, "She turned the phone face down. \"I'll listen later,\" Amaan said.", [("soft_thud", "ޖެހިއެވެ", -24)])
SHOTS = S

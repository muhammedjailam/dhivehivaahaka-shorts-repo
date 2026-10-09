"""Beat/shot plan for Milahanduvaru episode 256 (used by plan_beats.py).
Zumra meets the parents; moonlit thundi and the sudden rain; the wedding (nikah) with her huge father and the
frightened qazi; the decorated bridal room; next morning an empty house and the island's rumours.
NIKAH happens at shot 61-62 (~555 s): NO touching between Shamaan and Zumra in any beat before beat_020.
"""

HOUSE = "an old single-storey coral-stone house on a small Maldivian island"
YARD = (f"the wide sandy yard of {HOUSE}: a wooden joali frame with woven rope seats under a big shady tree, "
        "whitewashed walls with a wooden doorway, a low coral-stone boundary wall with a small gate, coconut palms")
WED_YARD = (f"the wide sandy yard of {HOUSE} on the wedding night: strings of small multi-coloured fairy-light bulbs "
            "hung through the big trees, tables with white cloths, flower vases and plates of food, rows of plastic chairs, "
            "a small table for the qazi with two decorated chairs facing it, coconut palms and the dark edges of the yard beyond the lights")

LOC = {
    "sitting_night": f"the small plain sitting room of {HOUSE} late at night, whitewashed walls, a simple wooden sofa set with cushions, a low table with tea cups, a woven mat on a tiled floor, a ceiling fan, a doorway to an inner room",
    "gate_predawn": f"the small gate in the low coral-stone boundary wall of {HOUSE}, opening onto a narrow white sandy island lane lined with coconut palms",
    "bedroom_night": f"Shamaan's simple bedroom in {HOUSE} at night, whitewashed walls, a wooden bed with a plain sheet, a small bedside table with a little lamp, a small toddler cot, a wooden bedroom door",
    "bedroom_morning": f"Shamaan's simple bedroom in {HOUSE} in the early morning, whitewashed walls, a wooden bed with a rumpled plain sheet, a small bedside table with a mobile phone lying face down, a window with a thin pale curtain",
    "yard_day": YARD,
    "yard_dusk": YARD,
    "yard_night": YARD,
    "thundi": "the long narrow tip of a white sandbank (thundi) at the end of a small Maldivian island at night, gentle waves lapping on both sides, open sea to the horizon, a big wide-crowned kaani tree standing alone a little way back on the sand",
    "thundi_storm": "the long narrow tip of a white sandbank (thundi) at the end of a small Maldivian island at night, open sea, a big wide-crowned kaani tree a little way back on the sand, coconut palms bending in the wind",
    "kaani_rain": "under the low wide crown of a big old kaani tree near the sandbank tip of a small Maldivian island at night, its thick trunk and spreading roots in the sand, the open beach and sea beyond",
    "veranda_rain": f"the small front veranda of {HOUSE} at night, tin-roof eaves streaming with rainwater, an open wooden front door with warm light inside, the dark sandy lane beyond a low wall",
    "wedding_arrival": f"the front yard and open doorway of {HOUSE} on the wedding evening, strings of small multi-coloured fairy lights just lit in the big trees, a low coral-stone wall with a small gate onto the sandy lane",
    "sitting_wedding": f"the small sitting room of {HOUSE} on the wedding evening, whitewashed walls, a simple wooden sofa set with cushions, a low table with a vase of fresh flowers and small plates of sweets, a woven mat on a tiled floor",
    "wedding_yard": WED_YARD,
    "wedding_tense": WED_YARD,
    "bridal_room": f"Shamaan's bedroom in {HOUSE} transformed into a bridal room: garlands of white jasmine and red roses along the walls and the wooden bed frame, petals scattered on a white bedspread, many small glowing lamps, white curtains at an open window",
    "house_morning": f"the inside of {HOUSE} in the morning: a short corridor opening into the small sitting room with a sofa set and a woven mat, a few leftover wedding flowers in a vase, every door open, nobody there",
    "kitchen": f"the simple kitchen of {HOUSE}: a two-burner gas stove with clean empty pots, a plain wooden table with plates and glasses set out from the night before, a small window, a water jug",
    "yard_morning": YARD,
    "sea_rumour": "a wide calm sea at night beyond the dark outline of a small uninhabited island with a few palms",
}
MOOD = {
    "sitting_night": "late night, warm amber glow of a single lamp against deep indigo shadows in the corners, polite but quietly guarded",
    "gate_predawn": "the last hour before dawn, deep blue sky just beginning to pale at the horizon, the last stars, soft silver haze over the lane, hushed and happy",
    "bedroom_night": "night, dim amber glow of the small bedside lamp, deep teal shadows, quiet and tender",
    "bedroom_morning": "early morning, soft pale-gold sunlight through the thin curtain, sleepy and warm",
    "yard_day": "morning, bright soft tropical daylight dappled through the leaves of the big tree, warm and drowsy",
    "yard_dusk": "just after sunset, the sky fading from apricot to deep indigo, the first stars and a rising moon, warm lamplight in the doorway, expectant",
    "yard_night": "early night, silver moonlight filtering through the big tree, a warm amber glow from the house doorway, romantic and mysterious",
    "thundi": "night, a bright full moon high above, silver light across the white sand and the sea, calm, dreamy and romantic",
    "thundi_storm": "night, dark storm clouds suddenly swallowing the full moon, the first gusts bending the palms, light draining away, foreboding",
    "kaani_rain": "night, heavy pouring rain in cold blue-grey darkness, a faint silvery glow around Zumra alone, eerie calm",
    "veranda_rain": "night, heavy rain, warm amber light spilling from the doorway against the cold dark blue rain",
    "wedding_arrival": "evening just after sunset, deep blue sky, the first coloured fairy lights and warm lamp glow, festive anticipation with a hint of awe",
    "sitting_wedding": "evening, warm amber lamplight, formal, respectful and slightly tense",
    "wedding_yard": "night, glowing multi-coloured fairy lights and warm lamps under a deep indigo sky, festive and joyful",
    "wedding_tense": "night, the coloured fairy lights still glowing but the edges of the yard sinking into deep shadow, hushed, uneasy and mysterious",
    "bridal_room": "night, soft warm glow of many small lamps, silver moonlight at the window, fragrant, dreamy yet mysterious",
    "house_morning": "morning, golden sunbeams slanting through the windows with floating dust motes, utterly still and silent, an eerie emptiness",
    "kitchen": "morning, flat pale daylight from the small window, empty, cold and unsettling",
    "yard_morning": "late morning, bright daylight outside with deep cool shade under the big tree, uneasy",
    "sea_rumour": "night, hazy dreamlike silver moonlight and thin mist over the water, eerie and unreal, an imagined rumour",
}

NOTOUCH = "they do not touch; a clear arm's-length gap between them"

BEATS = [
    # ---------------------------------------------------------------- night: Zumra meets the parents
    dict(to=2, reason="episode opening: Sakeena questions Zumra in the sitting room at night", chars=["sakeena", "zumra", "shamaan"], loc="sitting_night",
         visual="Sakeena sitting upright in an armchair on the left with a polite tight smile and uneasy watchful eyes, asking a question; Zumra sitting composed at the far end of the sofa on the right, hands folded in her lap, answering with a calm enigmatic smile, a faint silvery sparkle in her eyes; Shamaan sitting on a separate chair between them a little behind, glancing anxiously at his mother; cups of tea on the low table; " + NOTOUCH,
         camera="medium wide three-shot, eye level, faces in the upper half, the tiled floor and mat as a calm lower third", amb="living_night"),
    dict(to=4, reason="character change: Shamaan's father comes out of the inner room and asks about the island", chars=["shamaan_father", "zumra", "sakeena"], loc="sitting_night",
         visual="Shamaan's father stepping out of the inner-room doorway into the lamplight, one hand on the door frame, curious and slightly wary, asking about the island; Zumra on the sofa turning her head towards him with a calm polite smile, explaining; Sakeena seated nearby watching Zumra closely",
         camera="medium wide, eye level, the doorway on the left, the woven mat as a calm lower third", amb="living_night"),
    dict(to=7, reason="scene and time change: Shamaan sees Zumra off at the gate just before dawn", chars=["shamaan", "zumra"], loc="gate_predawn",
         visual="Shamaan standing at the open gate in the low coral-stone wall, smiling softly and content; Zumra already a few steps away down the misty sandy lane, glancing back at him over her shoulder with a gentle smile as she leaves, the palms dark against the paling sky; " + NOTOUCH,
         camera="medium wide shot from inside the yard, the lane receding into haze, sand as a calm lower third", amb="dawn_exterior"),
    dict(to=11, reason="scene and character change: back in his room he falls asleep; a knock — his mother at the door", chars=["shamaan", "sakeena"], loc="bedroom_night",
         visual="Shamaan standing in his half-open bedroom doorway, sleepy and surprised, one hand on the door edge; his mother Sakeena standing just outside in the dim corridor, her face carefully composed but her eyes uneasy and thoughtful, about to turn away; his bed with a rumpled sheet and the small toddler cot behind him in the lamp glow",
         camera="medium shot, eye level, from inside the room, the floor as a calm lower third", amb="room_night"),
    # ---------------------------------------------------------------- next morning
    dict(to=13, reason="time jump: next morning — the alarm, then Yameen climbs onto the bed", chars=["shamaan", "yameen"], loc="bedroom_morning",
         visual="Shamaan lying sleepily on the bed in the morning light, half-smiling with heavy eyes, as little toddler Yameen in his yellow t-shirt clambers onto the bed beside him with a big cheerful grin, reaching for his father's face; the phone lying face down on the bedside table",
         camera="medium shot, slightly high angle, the plain bed sheet as a calm lower third", amb="room_day", transition="black"),
    dict(to=15, reason="scene change: father and son sit on the joali in the yard; Shamaan dozes off and his mother scolds him", chars=["shamaan", "sakeena", "yameen"], loc="yard_day",
         visual="Shamaan sitting slumped on the rope joali under the big shady tree, jerking awake from a doze with startled sleepy eyes; Sakeena standing beside the joali holding little Yameen on her hip, frowning at her son with a disapproving, worried look and half-scolding words",
         camera="medium wide, eye level, the sandy yard as a calm lower third", amb="garden_day"),
    dict(to=17, reason="time change: at sunset, freshly dressed, he lies on the joali waiting for Zumra", chars=["shamaan"], loc="yard_dusk",
         visual="Shamaan, freshly bathed with neatly combed hair and a crisp clean light-blue shirt, lying back on the rope joali under the big tree with his hands behind his head, gazing at the darkening sky with a quiet hopeful smile, waiting",
         camera="wide shot, slightly low angle, the tree and the sky in the upper two-thirds, the sand as a calm lower third", amb="island_night", transition="black"),
    # ---------------------------------------------------------------- night 2: thundi and the rain
    dict(to=20, reason="character enters: Zumra appears silently behind the joali and invites him to the thundi", chars=["zumra", "shamaan"], loc="yard_night",
         visual="Zumra suddenly standing alone in the moonlight on the sand about two metres away from the joali, on the far left of the frame, as if she had appeared from nowhere, smiling playfully, one arm extended away from him pointing towards the moonlit lane that leads to the beach, her other hand at her side; Shamaan sitting on the joali on the right of the frame, turning his head towards her, delighted and a little startled; wide empty sand between them, nobody touches anyone",
         camera="medium shot, eye level, the sandy yard as a calm lower third", amb="island_night", sens="intimacy",
         safe="narration: she takes his hand and pulls him up — shown instead as her inviting gesture with an open hand, no touching before the nikah"),
    dict(to=25, reason="scene change: the two sit at the tip of the moonlit thundi and talk of marriage", chars=["zumra", "shamaan"], loc="thundi",
         visual="Shamaan and Zumra sitting on the white sand at the very tip of the sandbank facing the moonlit sea, seen from a three-quarter back angle, a clear gap of an arm's length between them; Zumra turned towards him with a serious, earnest look and a faint silvery sparkle in her eyes; Shamaan smiling at her, smitten; the full moon and its silver path on the water above them",
         camera="wide shot, the moon and the two figures in the upper two-thirds, the smooth sand as a calm lower third", amb="beach_night", sens="intimacy",
         safe="narration: she rests her head on his shoulder and moves closer — shown instead sitting apart at arm's length, no touching before the nikah"),
    dict(to=27, reason="action change: Zumra suddenly gets up to leave and the sky darkens all at once", chars=["zumra", "shamaan"], loc="thundi_storm",
         visual="Zumra walking away along the sand with her dress and hijab stirring in a sudden wind, glancing back calmly; Shamaan hurrying after her a few steps behind, one hand raised as if calling her to wait, never reaching her; dark clouds racing across and swallowing the full moon, the kaani tree in the background",
         camera="wide shot, the clouds and figures in the upper two-thirds, the sand as a calm lower third", amb="beach_night", sens="intimacy",
         safe="narration: he runs and embraces her waist — shown instead hurrying after her several steps behind, no touching before the nikah"),
    dict(to=32, reason="action/weather change: heavy rain — Zumra sits serenely under the kaani tree while Shamaan shivers", chars=["zumra", "shamaan"], loc="kaani_rain",
         visual="Zumra sitting serenely at the foot of the big kaani tree trunk, her midnight-blue dress and silver-grey hijab strangely dry and glowing faintly, untouched by the rain, calm and smiling; Shamaan standing a few steps away at the edge of the tree's shelter, completely soaked, hunched with his arms wrapped round himself, shivering, hair dripping; sheets of rain all around",
         camera="medium wide, eye level, the sand and roots as a calm lower third", amb="rain_night", sens="other",
         safe="supernatural cue only: she is dry and softly glowing in the rain; he lies down soaked in the narration — shown standing apart, shivering"),
    dict(to=38, reason="scene change: back at the house in the rain — he stops her from leaving alone; she jokes she is a jinni and disappears into the dark", chars=["zumra", "shamaan"], loc="veranda_rain",
         visual="on the rain-lashed front veranda, Zumra standing at the top of the step about to go out into the dark rainy lane, looking back over her shoulder with a teasing mysterious smile; Shamaan, soaked, standing in the lit doorway with one hand raised in a pleading stop gesture, worried; a clear gap between them; the dark lane and rain beyond",
         camera="medium wide, eye level, the wet veranda floor as a calm lower third", amb="rain_night", sens="intimacy",
         safe="narration: he holds her back — shown as a pleading raised hand from the doorway, no touching before the nikah"),
    dict(to=40, reason="scene change: alone in his room, changed into dry clothes; the rain stops, an unusual silence", chars=["shamaan"], loc="bedroom_night",
         visual="Shamaan lying on his back in bed in dry clothes with a thin sheet pulled up to his chest, still a little shivery, eyes open and gazing at the ceiling with a quiet hopeful smile; the window behind him with the last drops falling from the eaves and the moon coming out from the clouds",
         camera="medium shot, slightly high angle, the plain sheet as a calm lower third", amb="room_night"),
    # ---------------------------------------------------------------- the wedding
    dict(to=44, reason="time jump to the wedding evening: Zumra arrives with her huge father", chars=["ahmadhufulhu", "zumra", "sakeena", "shamaan"], loc="wedding_arrival",
         visual="at the small gate, Zumra stepping into the yard beside her father Ahmadhufulhu, a towering, broad and powerful man in a long charcoal kurta who stands a full head taller than everyone, stern and silent; Sakeena in front of the doorway greeting them with surprised eyes and a questioning look; Shamaan in a neat light-blue shirt standing a little behind his mother, smiling; coloured fairy lights glowing in the trees",
         camera="wide shot, eye level, the figures in the upper two-thirds, the swept sand as a calm lower third", amb="island_house_night", transition="black"),
    dict(to=47, reason="scene change: in the sitting room Zumra's father solemnly asks Shamaan to look after his daughter", chars=["ahmadhufulhu", "shamaan", "zumra", "sakeena"], loc="sitting_wedding",
         visual="Ahmadhufulhu, huge and imposing, seated on the sofa leaning forward with his hands on his knees, speaking gravely to Shamaan; Shamaan sitting on a chair opposite, nodding respectfully; Zumra seated quietly at the far end of the sofa with her eyes lowered; Sakeena standing by the doorway watching",
         camera="medium wide, eye level, the woven mat as a calm lower third", amb="living_night"),
    dict(to=53, reason="scene change: the decorated wedding yard at night; guests at the tables and the qazi arrives", chars=["shamaan", "zumra", "sakeena"], loc="wedding_yard",
         visual="wide view of the festive yard: strings of multi-coloured lights in the trees, guests in their best clothes seated at white-clothed tables smiling; an elderly qazi in a white thobe and white cap sitting at a small table; Shamaan seated on a decorated chair facing the qazi with a radiant happy face; a little apart to one side Zumra seated on a decorated chair beside Sakeena among a few women, head modestly bowed; " + NOTOUCH,
         camera="wide establishing shot, slightly high angle, the lights and people in the upper two-thirds, the sand between the tables as a calm lower third", amb="hall_crowd"),
    dict(to=54, reason="emotional turning point: close on Zumra, head bowed and uneasy", chars=["zumra", "sakeena"], loc="wedding_tense",
         visual="close on Zumra seated on her decorated chair, head bowed, eyes lowered, her face troubled and lost in deep thought rather than shy; soft blurred coloured lights behind her; Sakeena softly out of focus beside her",
         camera="medium close-up, eye level, her face in the upper half, her folded hands and dress as a calm lower third", amb="island_night"),
    dict(to=56, reason="characters change: the two fathers sit beside the groom; the qazi begins the sermon and silence falls", chars=["ahmadhufulhu", "shamaan_father", "shamaan"], loc="wedding_tense",
         visual="at the qazi's small table: Shamaan seated in the middle, and beside him the two fathers on chairs — the towering Ahmadhufulhu in his charcoal kurta and Shamaan's slight father in his white skullcap — both looking proud and hopeful; the elderly qazi in white seen from behind in the foreground beginning the sermon, everyone quiet and attentive",
         camera="medium wide, eye level, the table top as a calm lower third", amb="island_night"),
    dict(to=59, reuse="beat_017", reason="returns to Zumra: Shamaan glances at her lovingly, she stays head bowed; what is she hiding?", loc="wedding_tense",
         visual="(reuse of beat_017)", amb="island_night"),
    dict(to=63, reason="character/action change: the qazi is nervous and sweating, finishes the nikah quickly and hurries out", chars=["shamaan"], loc="wedding_tense",
         visual="the thin elderly qazi in a white thobe and white cap half-rising from his chair at the small table, beads of sweat on his forehead, glancing nervously over his shoulder towards the dark gate, clearly eager to leave; Shamaan seated across from him looking puzzled; coloured lights above",
         camera="medium shot, eye level, the table top as a calm lower third", amb="island_night"),
    dict(to=66, reason="action change: after the nikah — Shamaan's father asks why the qazi rushed off and Zumra answers sharply", chars=["shamaan_father", "zumra", "shamaan", "ahmadhufulhu"], loc="wedding_tense",
         visual="Shamaan's father seated at the table with a suspicious narrowed look, turning towards Zumra; Zumra, now the bride seated beside Shamaan, lifting her head and answering with a hard, cold expression; Shamaan between them looking from one to the other in surprise; Ahmadhufulhu large and still in the background",
         camera="medium wide, eye level, the table top as a calm lower third", amb="island_night"),
    dict(to=71, reason="action change (after the nikah): Shamaan studies her uneasy eyes and gently takes her hand — she pulls it away", chars=["zumra", "shamaan"], loc="wedding_tense",
         visual="the newly married couple seated side by side on their decorated chairs: Zumra sharply pulling her hand back away from Shamaan's open hand as if startled by a shock, her eyes wide and uneasy; Shamaan looking at her with gentle concern, his hand still open; coloured lights behind them",
         camera="medium two-shot, eye level, their hands and laps as the lower third", amb="island_night", sens="intimacy",
         safe="after the nikah: a married couple's brief hand contact only, fully clothed; she withdraws her hand"),
    dict(to=73, reason="action change: Zumra stares into a dark corner of the yard; Ahmadhufulhu stands and reassures everyone", chars=["ahmadhufulhu", "zumra", "shamaan"], loc="wedding_tense",
         visual="Ahmadhufulhu rising to his full towering height beside the table, one large hand raised in a calming gesture, his expression forcedly composed; Zumra seated, her gaze fixed past everyone on a deep dark corner of the yard beyond the lights where nothing can be seen but shadow under the palms; Shamaan watching her",
         camera="medium wide, low angle, the dark corner visible in the background, the sand as a calm lower third", amb="island_night"),
    dict(to=76, reason="action change: the meal is served but nobody eats; Shamaan's parents are uneasy while he only sees Zumra", chars=["shamaan_father", "sakeena", "shamaan", "zumra"], loc="wedding_tense",
         visual="a table full of rice, curries, fish and sweets under the coloured lights, the food untouched; Shamaan's father sitting deep in thought with a frown, Sakeena beside him with a worried face; across the table Shamaan gazing at Zumra, enchanted and oblivious, Zumra quiet with lowered eyes",
         camera="medium wide, slightly high angle, the laden table as the lower third", amb="island_night"),
    dict(to=80, reuse="beat_016", reason="the party ends well; guests leave happy, proud of the new bride (returns to the wide festive yard)", loc="wedding_yard",
         visual="(reuse of beat_016)", amb="hall_crowd"),
    dict(to=85, reason="scene change: the room has been mysteriously decorated as a bridal room; Zumra by the window, her eyes flash strangely", chars=["zumra", "shamaan"], loc="bridal_room",
         visual="Shamaan sitting tired on the edge of the flower-decked bed, looking up at his bride with an affectionate weary smile and surprise at the decorations; Zumra standing a few steps away by the moonlit window, half turned towards him with a soft smile, her eyes catching a brief strange silvery flash; flower garlands and many small lamps around the room",
         camera="medium wide, eye level, the petal-strewn floor as a calm lower third", amb="room_night", sens="intimacy",
         safe="married couple in the bridal room: he sits on the bed edge, she stands apart by the window, fully clothed, no intimacy"),
    # ---------------------------------------------------------------- next morning
    dict(to=88, reason="time jump: next morning the house is deathly silent; Shamaan walks through the empty rooms", chars=["shamaan"], loc="house_morning",
         visual="Shamaan stepping out of the corridor into the empty sunlit sitting room, looking around in puzzlement, golden sunbeams cutting across the still room, nobody anywhere, every door open",
         camera="wide shot, eye level, the tiled floor as a calm lower third", amb="home_day", transition="black"),
    dict(to=90, reason="scene change: in the kitchen — no food, last night's plates still set out", chars=["shamaan"], loc="kitchen",
         visual="Shamaan standing in the kitchen doorway with a hand on his stomach, looking at the cold stove with empty clean pots and the plates still set out from last night, disappointed and uneasy",
         camera="medium wide, eye level, the table top as a calm lower third", amb="home_day"),
    dict(to=94, reason="scene/character change: he lies on the joali in the yard; his mother comes in frightened and sits beside him", chars=["sakeena", "shamaan"], loc="yard_morning",
         visual="Shamaan lying on the rope joali in the deep shade of the big tree, raising his head; Sakeena coming in from the gate and sitting down on the edge of the joali beside him, her face pale and frightened, glancing around the yard to make sure no one is listening",
         camera="medium wide, eye level, the sand as a calm lower third", amb="garden_day"),
    dict(to=96, reason="action change: Sakeena leans close and whispers the islanders' rumours", chars=["sakeena", "shamaan"], loc="yard_morning",
         visual="close two-shot on the joali: Sakeena leaning close to her son and whispering urgently, one hand half-raised, her eyes wide with fear; Shamaan sitting up beside her, listening with a confused, disbelieving face",
         camera="medium close-up two-shot, eye level, the joali ropes as a calm lower third", amb="garden_day"),
    dict(to=97, reason="the rumour visualised: Zumra's father seen leaving by walking on the sea at night", loc="sea_rumour",
         visual="far away on the hazy moonlit sea, a very tall dark silhouette of a man in a long robe walking away across the surface of the calm water towards a small dark uninhabited island, seen from behind at a great distance, no face visible, mist on the water",
         camera="wide shot, the silhouette and island small in the upper half, calm water as the lower third", amb="memory", transition="dissolve", sens="other",
         safe="supernatural rumour shown only as a tiny distant silhouette from behind in mist; no face, no reference image"),
    dict(to=98, reuse="beat_030", reason="back to mother and son: she trembles as she speaks, he is shocked", loc="yard_morning",
         visual="(reuse of beat_030)", amb="garden_day", transition="dissolve"),
    dict(to=100, reason="emotional turning point: Shamaan alone with his doubts — is Zumra really human?", chars=["shamaan"], loc="yard_morning",
         visual="close-up of Shamaan sitting on the joali in the shade, elbows on his knees, staring into the distance with a deeply troubled, torn expression, the bright sunlit yard and the sea glimpsed through the palms behind him",
         camera="close-up, eye level, his face in the upper half, his clasped hands as a calm lower third", amb="garden_day"),
]
S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Though Shamaan saw the unease on his mother's face, he noticed she was trying hard not to show it. \"Which island are you from, girl?\"")
sh(2, "asked Shamaan's mother, Sakeena. \"I'm a Malé girl. I come very often to my father's uninhabited island near here,\" Zumra answered.")
sh(3, "\"Aren't you afraid living alone on that island?\" mother asked again. \"That's the island Donmanik looks after, isn't it?\" said the father, coming out of the room just then.",
   [("door_open", "ކޮޓަރިން", -22)])
sh(4, "\"No — the island is entrusted to Donmanik. My father mostly lives in Singapore,\" Zumra explained.")
sh(5, "That night's meeting ended as happily as Shamaan had hoped. Zumra went back only as dawn drew near.")
sh(6, "As she said, she had to reach that island before sunrise. After seeing Zumra off, Shamaan came into his room, completely at peace.")
sh(7, "After so many days a partner was coming into his life, and his son would have a mother — he was happy.", hum=True)
sh(8, "Not long after he lay down, he fell asleep. But suddenly a knock on the door woke him. When the door opened, his mother stood before him.",
   [("knock", "ޓަކިޖެހި", -16), ("door_open", "ހުޅުވިއިރު", -20)])
sh(9, "\"Mother, what happened?\" Shamaan asked in surprise. \"I came to see if you were asleep,\" mother said. \"Mother, Zumra is a very good,")
sh(10, "kind girl,\" Shamaan began praising his partner. \"Yes, she seems different from other girls,\" mother said, and walked away.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(11, "His mother's words left an unease in Shamaan's heart. Were his parents not pleased about it, he wondered.")
sh(12, "Next, Shamaan woke to the sound of the alarm. Looking at the clock, it was half past six. Meaning to skip the office and stay home today, he lay down again.",
   [("phone_buzz", "އެލާމްވާ", -18)])
sh(13, "But when Yameen came and climbed onto the bed, Shamaan couldn't sleep. \"Let's go outside,\" Shamaan said, cuddling Yameen. Father and son went out and sat on the joali.")
sh(14, "Heavy sleepiness showed on Shamaan's face. \"Hey! You're asleep!\" At his mother's voice Shamaan woke with a start.",
   [("gasp", "ސިއްސައިގެން", -22)])
sh(15, "He looked around to see where Yameen was. \"Go on, sleep some more. The way you're carrying on, how far will it go this time?\" mother said, displeased.")
sh(16, "After handing Yameen to his mother, Shamaan went into his room to rest. As on the previous night, at sunset Shamaan bathed, dressed up nicely, and went to lie on the joali.")
sh(17, "Waiting for Zumra. Now there was no need to meet in different places. The family already knew everything.")
sh(18, "Shamaan didn't have to wait long. He saw Zumra come and stop behind him. He couldn't even tell from which direction she had come.",
   [("footsteps_sand", "ހުއްޓިލި", -22)])
sh(19, "\"Waiting for me, aren't you?\" Zumra said, coming closer to Shamaan. \"Yes — well, I can't wait for anyone else, can I?\" Shamaan smiled.")
sh(20, "\"Let's go to the thundi, the moonlight is so beautiful,\" Zumra said, taking Shamaan's hand as she stood up. Shamaan had no courage to refuse.")
sh(21, "The two went and sat at the tip of the thundi. The whole area lay lit by the moonlight. The sound of the waves kissing the shore brought the heart a peace hard to describe.",
   [("wave_crash", "ރާޅުތައް", -22)])
sh(22, "\"Now tell me, when will we marry?\" Zumra asked, resting her head on Shamaan's shoulder. \"As soon as possible,\" was Shamaan's very short answer.")
sh(23, "Only Zumra was in Shamaan's heart. \"But I'm a very busy person. So most of the day I'll be occupied with business matters,\" Zumra said.")
sh(24, "There was a certain seriousness in her voice. \"Yes, I know that. You think I'm a little kid, don't you?\" Shamaan smiled.")
sh(25, "He was ready to say yes to everything Zumra said. \"Even if I can't be around during the day, I won't let any hardship come to Shamaan,\" Zumra said, drawing closer.")
sh(26, "\"Okay, okay, I won't complain about that,\" Shamaan said. \"I'm leaving now, tonight,\" Zumra said, suddenly getting up and walking off.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(27, "Shamaan ran and embraced Zumra's waist. At that very moment the atmosphere suddenly changed. The sky darkened,",
   [("footsteps_sand", "ދުވެފައި", -20), ("wind_gust", "ބަނަވެ", -16)], hum=True)
sh(28, "and suddenly heavy rain began to pour. The two of them ran towards a big kaani tree nearby.",
   [("rain_start", "ވާރޭ", -14), ("footsteps_sand", "ދުއްވައިގަތީ", -20)])
sh(29, "Zumra went and sat at the foot of the kaani tree. From the way Zumra acted, it seemed the rain had no effect on her at all. She sat there perfectly calm.")
sh(30, "\"Let's go now,\" Shamaan said, shivering. Because of the cold his teeth were chattering. \"I'll sit here getting wet in the rain.",
   [("breath_heavy", "ދެދަތްޕިލަ", -22)])
sh(31, "You go, Shamaan.\" Zumra had changed her mind. She no longer wanted to go. \"Okay, then I won't go either.")
sh(32, "I'll even sleep here,\" Shamaan said, lying down at the foot of the tree, soaked by the rain. At that Zumra got up and started walking — taking Shamaan with her.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(33, "By the time they reached the house the two were completely drenched. Shamaan went inside. But Zumra wanted to leave quickly.",
   [("door_open", "ގޭތެރެއަށެވެ", -22)])
sh(34, "Saying it was time for the dhoni to leave, Zumra set off. Shamaan went and held Zumra back. \"Listen, you can't go alone on a stormy night like this,\" Shamaan said, worried.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(35, "\"No, I'm a jinni. Nothing will happen to me,\" Zumra said with a smile, to frighten Shamaan.", hum=True)
sh(36, "\"Sure — jinni or ghost, whichever. Mother won't be at ease if I send Zumra off alone,\" Shamaan complained.")
sh(37, "The love in his heart for Zumra was far greater than any fear. They parted only after agreeing to meet again at the thundi tomorrow night.")
sh(38, "When Zumra vanished into the darkness, Shamaan turned back and went into his room. It was still raining heavily.",
   [("door_close", "ވަނެވެ", -22)])
sh(39, "When Shamaan entered his room he was shivering. He quickly changed his clothes and lay down to sleep. By then the pouring rain had stopped.",
   [("cloth_rustle", "ހެދުންބަދަލުކޮށް", -24)])
sh(40, "An unusual silence had settled over everything. In Shamaan's heart was the hope of tomorrow night.")
sh(41, "For the happy occasion of the wedding, everyone was dressed in their best, impatient for the celebration to begin.")
sh(42, "Just then Zumra was suddenly seen arriving at the place. Beside Zumra stood a huge man with a powerful body.",
   [("footsteps_sand", "ވަތްތަނެވެ", -22)])
sh(43, "\"This is my father,\" Zumra said first, addressing Shamaan's mother. \"Is that so. Why didn't you bring your father before? And where is your mother?\"")
sh(44, "asked Shamaan's mother. \"Father came back this afternoon after living abroad. My mother has passed away,\" Zumra answered.")
sh(45, "Shamaan's mother welcomed father and daughter, led them to the sitting room and seated them. Shamaan sat with them too.")
sh(46, "\"This is my father,\" Zumra then said, introducing her father to Shamaan. \"Be good to my daughter. And look after her well.")
sh(47, "Living with you, there may sometimes be difficulties. Zumra is a girl who will be working very hard during the day,\" Zumra's father said to Shamaan.")
sh(48, "It was the joyful wedding night. The spacious yard of the house was decorated more beautifully than ever before.")
sh(49, "The light of small coloured bulbs strung in the trees of the yard lit up the whole place.")
sh(50, "The sweet scent of flowers filling the air and the gently blowing breezes brought freshness to every heart.",
   [("leaves_rustle", "ރޯޅިތަކުން", -22)])
sh(51, "When the qazi arrived to perform the nikah, the relatives and friends who had come to the celebration sat down by the tables in the yard.")
sh(52, "Smiles and joy showed on every face. Shamaan and Zumra sat on two special chairs prepared to face the qazi.")
sh(53, "Shamaan's face showed the utmost happiness. The greatest dream of his life was about to come true.")
sh(54, "But Zumra sat with her head bowed. Her face showed unease, or the look of someone lost in deep thought.", hum=True)
sh(55, "On the chairs next to them sat Zumra's father and Shamaan's father. Both fathers' faces showed pride and hope.")
sh(56, "As the qazi began the sermon, silence fell over everything. Everyone's attention was fixed on the moment the two would be joined in that sacred bond.")
sh(57, "Now and then Shamaan glanced at Zumra with great love. Yet Zumra stayed just as she was, head bowed.")
sh(58, "What feelings were passing through her heart? Was it the shyness of starting a new life?")
sh(59, "Or was some other secret hidden behind it? As the wedding ceremony went on, some unusual things were noticed about the qazi.", hum=True)
sh(60, "The qazi was extremely anxious. Sweat was breaking out on his forehead, and now and then he glanced towards the door.",
   [("heartbeat", "ހާސްވެފައެވެ", -22)], hum=True)
sh(61, "It seemed he was afraid of something, or that someone might come. The nikah did not take long.")
sh(62, "\"I'm a little unwell tonight,\" the qazi said, rising hurriedly as soon as the nikah was done. Saying that, he walked out.",
   [("footsteps_sand", "ހިނގައިގަތީ", -22)])
sh(63, "From his movements it seemed he didn't want to stay there even a moment longer. \"Why did they leave so quickly?\"")
sh(64, "Shamaan's father was surprised by the qazi's unusual haste. After a suspicious look, he asked.")
sh(65, "\"Why should they sit around here for so long?\" Zumra answered Shamaan's father's question at once.")
sh(66, "The harshness in Zumra's voice drew everyone's attention to her. From the way Zumra answered, it seemed she too was trying to hide something.", hum=True)
sh(67, "Shamaan looked at Zumra's face. Unease showed in Zumra's eyes. Behind that happy night,")
sh(68, "Shamaan sensed, there was a great secret hidden. But he could not tell what it was.", hum=True)
sh(69, "An indescribable silence had fallen over the wedding party. The qazi's hurried exit added to the questions in Shamaan's heart.")
sh(70, "Puzzled by Zumra's answer, Shamaan gently took hold of her palm.")
sh(71, "But Zumra pulled her hand away like someone who had touched a live wire. \"Zumra, what's wrong?\" Shamaan asked softly.",
   [("gasp", "ދަމައިގަތީ", -20)], hum=True)
sh(72, "Zumra gave no answer. Her gaze was fixed on a dark corner of the yard. Just then Zumra's father, Ahmadhufulhu, cleared his throat and stood up.")
sh(73, "\"Now don't think about it so much. Perhaps the qazi left quickly because he is ill. Let's get on with the meal.\" Shamaan noticed a tremor in Ahmadhufulhu's voice too.")
sh(74, "The aroma of the delicious food laid out on the tables filled the whole place. Yet no one seemed very eager to eat.",
   [("cup_clatter", "މޭޒުމަތީގައި", -24)])
sh(75, "Shamaan's father sat lost in deep thought. Shamaan's parents were very uneasy about it all. What were they to do?")
sh(76, "Even when someone spoke to Shamaan, he didn't hear a word. He was spellbound by Zumra's beauty and her goodness.")
sh(77, "The wedding party ended perfectly — in a way Shamaan's family had never expected.")
sh(78, "The only difference was that this party was held with just family members and a few friends.")
sh(79, "From Zumra's side, only her father attended. After the party, everyone went home very happy.")
sh(80, "The family seemed proud of their new bride. Her good manners and her smile won everyone's hearts.")
sh(81, "When everyone had gone, Shamaan and Zumra went into the room to sleep. Shamaan got a sudden surprise. The whole room had been decorated.",
   [("door_open", "ކޮޓަރިއަށެވެ", -22)])
sh(82, "The whole room was fragrant. But when, and who had done it, Shamaan wondered. Shamaan went and lay down on the bed.",
   [("cloth_rustle", "އޮށޯވެލިއެވެ", -24)])
sh(83, "He was very tired. \"Come, let's lie down,\" Shamaan said, holding Zumra's hand. \"I'm not someone who gets tired the way Shamaan does,\" Zumra replied with a smile.")
sh(84, "At that moment Shamaan thought the colour of her eyes flashed in a strange way. \"If only you'd asked your father to stay here at this house,\" Shamaan said to Zumra.", hum=True)
sh(85, "\"No, father leaves tonight. I don't know when he'll ever be able to come again,\" Zumra said. There was an inexpressible depth of feeling in her voice.")
sh(86, "Though the golden rays of morning were falling into the room through the window, the whole house was filled with a deathly silence.", hum=True)
sh(87, "When Shamaan woke, the whole house felt like an abandoned, empty house. Not a single one of the usual sounds could be heard.")
sh(88, "Shamaan came out of the room and looked all around the house. There was no one to be seen. He thought: Zumra must have gone to work very early today.",
   [("footsteps_pavement", "ނިކުމެ", -22)])
sh(89, "Being very hungry, Shamaan hurried into the kitchen, hoping something had been cooked.",
   [("footsteps_pavement", "ބަދިގެއަށް", -22)])
sh(90, "But when he went into the kitchen and looked, no food had been prepared at all. Even the plates were still set out just as they had been laid last night.")
sh(91, "Seeing the state of the house, an unease rose in Shamaan's heart. Not staying there any longer, Shamaan went out into the yard.",
   [("door_open", "ނިކުމެލިއެވެ", -22)])
sh(92, "And he lay down on the joali under a big shady tree, hoping to find some peace of mind. Just then he saw his mother coming in from outside.",
   [("footsteps_sand", "އަންނަތަން", -22)])
sh(93, "His mother's walk and the colour of her face were not as usual. Her face showed clear signs of being frightened by something serious.")
sh(94, "Mother came and sat down beside the joali where Shamaan lay. And after looking all around, she asked in a whisper, afraid someone might hear.",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(95, "\"Where's Zumra?\" \"Zumra went to work very early today,\" Shamaan answered. \"Shamaan...")
sh(96, "today I heard some people of this island saying she's an unusual girl. That she may even be a jinni. They say her father is a man who has been seen on an uninhabited island around here.")
sh(97, "And some people even say that last night he left by walking over the sea.\" Mother let out a deep breath. And, moving closer to Shamaan, she said,",
   [("sigh", "ނޭވާއެއް", -20)])
sh(98, "Mother said all this trembling all over with fear. Shamaan felt a sudden jolt. Mother was telling him the frightening rumours spreading across the island about Zumra.",
   [("heartbeat", "ސިހުމެކެވެ", -20)], hum=True)
sh(99, "Between the love in his heart for Zumra and the things his mother had said, Shamaan's mind filled with questions.")
sh(100, "Is Zumra truly a human being? Or is she an unusual creature, as the islanders say?", hum=True)
SHOTS = S

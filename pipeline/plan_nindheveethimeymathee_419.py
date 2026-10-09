"""Beat/shot plan for Nindheveethimeymathee episode 419 (used by plan_beats.py).
SCHOOL timeline, a few weeks after Sana's death (401). Friends visit Lail at Haizum's penthouse.
Lail <-> Saba never touch: no tear in a palm, no whisper at the ear, no hand-holding (series bible rule 2).
Saba always in her white hijab (the narration's loose wind-blown hair / hair tie -> hijab fluttering / a hijab pin)."""

PH = "the top floor of Haizum's luxury multi-level penthouse on a very tall residential high-rise in Malé, Maldives"
TERRACE = (f"the open rooftop terrace on {PH}: a long rectangular swimming pool of calm, still, empty turquoise water, cream "
           "stone tiles, two cushioned outdoor lounge chairs and a low side table, a long outdoor dining table with chairs, "
           "potted palms, a waist-high glass-and-steel railing along the edge, and beyond it the dense rooftops of Malé "
           "and the open blue Indian Ocean far below")
LOC = {
    "terrace_day": TERRACE,
    "terrace_sky": "the view from a very high rooftop terrace in Malé, Maldives, out over the open Indian Ocean: towering "
                   "clouds over the sea, a grey veil of distant rain falling from one cloud far out on the horizon, "
                   "sunlight breaking through, the turquoise lagoon and reef rings below",
    "terrace_table": f"the outdoor dining table on the rooftop terrace on {PH}: a long wooden table with chairs beside the "
                     "calm empty pool, potted palms, a glass railing, the Malé skyline and the sea beyond, a glass door "
                     "leading inside to an upstairs sitting room",
    "railing_sunset": f"the glass-and-steel railing at the edge of the rooftop terrace on {PH}, the dense city of Malé "
                      "far, far below with tiny streets and rooftops, the ocean horizon beyond",
    "terrace_night": f"the rooftop terrace on {PH} after dark: warm string lights and low lamps glowing, the calm empty "
                     "pool lit turquoise from within, potted palms, the glass-and-steel railing, the glittering lights of "
                     "Malé city and harbour far below",
    "sitting": "the main-floor sitting room of a luxury Malé penthouse at night: an open floating staircase coming down "
               "from the upper floor, cream sofas, a low coffee table, warm wall lamps, a corridor with room doors, "
               "the front door with a low shoe rack and a few pairs of sandals and sneakers",
    "bedroom": "a seventeen-year-old boy's tidy own room in a luxury Malé penthouse at night: a wooden study desk with neatly "
               "stacked school books and a small framed photo, a desk lamp, a bookshelf, a wide window with the night "
               "city lights, the room's door standing wide open onto a lit corridor; only the desk, window and doorway "
               "side of the room is seen",
    "landing": "the marble top-floor landing of a modern high-rise at night: the penthouse's front door standing open and "
               "spilling warm light across the floor, opposite it a brushed-steel lift with its doors sliding shut",
    "lift": "the inside of a modern apartment-building lift at night: brushed-steel walls, a soft ceiling light, a "
            "handrail, a mirror-polished back wall, the doors closed",
    "lobby": "the ground-floor lobby of a modern Malé high-rise at night: brushed-steel lift doors sliding open, polished "
             "floor, warm downlights, glass entrance doors onto the street",
    "street": "the quiet narrow street at the foot of a very tall residential high-rise in Malé at night: warm street "
              "lamps, parked motorbikes along the wall, a few palms, the tower rising into the night sky above",
    "lookup": "a dramatic low-angle view straight up the face of a very tall residential high-rise in Malé at night, rows "
              "of lit windows, and at the very top a small lit rooftop balcony with string lights",
}
MOOD = {
    "terrace_day": "late afternoon, warm golden sunlight slanting low, a light sea breeze, clear sky with soft clouds, "
                   "tender, quiet and a little sad",
    "terrace_sky": "late afternoon, golden light breaking through towering clouds, a distant rain shower over the sea, "
                   "calm, timeless and reflective",
    "terrace_table": "bright late-afternoon DAYLIGHT, the sun still well above the horizon, a blue sky with white clouds, no moon, no night, the city and sea below in clear daylight, warm sunlight, light breeze, cheerful and friendly with a quiet undercurrent",
    "railing_sunset": "sunset, the sky glowing amber, rose and violet, a steady breeze, shy and hopeful",
    "terrace_night": "early night just after sunset, deep sapphire-indigo sky with the last violet glow on the horizon, "
                     "warm amber string lights, breezy, playful and romantic",
    "sitting": "night, warm amber wall lamps against deep blue shadows, cosy and quiet",
    "bedroom": "night, the warm pool of the desk lamp against deep indigo shadows, city lights glittering in the window, "
               "hushed, shy and tender",
    "landing": "night, warm amber light from the open door against the cool light of the landing, bittersweet goodbye",
    "lift": "night, soft cool ceiling light on brushed steel, playful teasing and laughter",
    "lobby": "night, warm downlights, laughter",
    "street": "night, warm street lamps against a deep sapphire sky, light breeze, playful and warm",
    "lookup": "night, deep moonlit indigo sky with soft clouds, warm amber lights at the top of the tower, longing",
}

BEATS = [
    dict(to=3, reason="episode opening: Saba and Lail sitting apart from the friends on the rooftop terrace, a quiet smile", chars=["saba_young", "lail_young"], loc="terrace_day",
         visual="Saba (17, white hijab fully covering her hair and neck, powder-blue dress) sitting on one cushioned lounge chair lowering her phone, its dark screen facing away, and Lail (17, light-grey t-shirt, jeans) sitting on a separate lounge chair an arm's length away with a low side table between them; they look at each other with a quiet, meaningful smile; Lail's face tired and grieving",
         camera="medium two-shot, eye level, faces in the upper half, the stone tiles and calm pool edge as the lower third", amb="rooftop_day"),
    dict(to=7, reason="emotional turning point: Saba speaks of her father's death and a tear runs down her cheek", chars=["saba_young", "lail_young"], loc="terrace_day",
         visual="close two-shot on the lounge chairs: Saba's eyes glistening, a single tear running down her cheek, her white hijab snug around her face; Lail, an arm's length away on his own chair, leaning slightly forward with a gentle, understanding look, holding out a small packet of tissues towards her across the side table, his arm extended, not touching her",
         camera="medium close-up two-shot, eye level, the side table top as the lower third", amb="rooftop_day", sens="intimacy",
         safe="the narration's tear falling into Lail's open palm is replaced by a tear on her cheek and Lail offering a tissue packet across the table at arm's length; no touching"),
    dict(to=12, reason="action change: Lail, lost in thought, looks at his own open palm and talks about the tears of centuries", chars=["lail_young", "saba_young"], loc="terrace_day",
         visual="Lail sitting on his lounge chair, gazing down thoughtfully at his own open right palm resting on his knee, a faint wistful smile, speaking softly; Saba on her separate chair an arm's length away in the soft background, a folded white tissue in her hands, listening",
         camera="medium shot favouring Lail, slightly from the side, his face in the upper third, Saba soft-focus behind", amb="rooftop_day",
         sens="intimacy", safe="no tear in his palm: he just looks at his own empty open hand"),
    dict(to=15, reason="focus change: Saba listening, agreeing, Lail eager to hear how", chars=["saba_young", "lail_young"], loc="terrace_day",
         visual="Saba in the foreground on her lounge chair, half turned towards Lail, her eyes still slightly wet but a small thoughtful smile forming as she thinks; Lail an arm's length away, leaning forward eagerly, eyebrows raised, waiting for her answer",
         camera="over-the-shoulder medium shot from behind Lail's shoulder onto Saba's face, faces in the upper half", amb="rooftop_day"),
    dict(to=18, reason="detail image: Lail explains the water cycle - the sea, the clouds and the rain beyond the terrace", loc="terrace_sky",
         visual="a sweeping view from high above Malé over the ocean: towering sunlit clouds, a soft grey curtain of rain falling from one cloud far out at sea, sun rays breaking through, the turquoise lagoon and reef rings shimmering far below; pure landscape seen from the air, no railing, no terrace, no people, no figures at all",
         camera="wide shot, the clouds and rain in the upper two-thirds, the calm sea as the lower third", amb="rooftop_day"),
    dict(to=20, reason="characters enter: Laira brings pizza and Maama a basket of drinks; the friends take them", chars=["laira", "shafeeqa", "asil_young", "sadhee_young"], loc="terrace_table",
         visual="Laira (19) stepping out of the glass door carrying three stacked plain unmarked pizza boxes, Asil (17, maroon t-shirt) reaching to take them from her; behind her grandmother Shafeeqa with gold glasses carrying a small woven basket of small plain unlabelled glass bottles of dark soda, Sadhee (17, cream hijab) taking the basket from her with a smile; the long outdoor table beside them",
         camera="medium wide, eye level, faces in the upper half, the table top as the lower third", amb="rooftop_day",
         sens="other", safe="Coke bottles shown as plain unlabelled soda bottles, no logos"),
    dict(to=22, reason="action change: Maama quietly asks Asil to make sure the grieving siblings eat", chars=["shafeeqa", "asil_young"], loc="terrace_table",
         visual="grandmother Shafeeqa leaning a little towards Asil with one hand raised beside her mouth confidentially, a warm worried look in her eyes behind her gold glasses; Asil (17) nodding seriously, a pizza box in his hands; pizza boxes and soda bottles on the table behind them",
         camera="medium two-shot, eye level, the table top as the lower third", amb="rooftop_day"),
    dict(to=25, reason="action change: everyone sits down to eat; Saba and Lail steal glances across the table", chars=["saba_young", "lail_young", "sadhee_young", "asil_young"], loc="terrace_table",
         visual="the friends eating pizza at the long outdoor table: Saba seated beside Sadhee on one side, Lail seated beside Asil on the opposite side; Saba and Lail glancing at each other across the table with shy, searching looks while Sadhee and Asil chat and eat; open pizza boxes and plain glass soda bottles on the table",
         camera="medium wide, slightly high eye level, faces in the upper half, the table top as the lower third", amb="rooftop_day"),
    dict(to=27, reason="action change: after the meal everyone drifts apart - Laira takes a call, Asil games, Sadhee and Shahid chat", chars=["asil_young", "laira", "shahid_young", "sadhee_young"], loc="terrace_table",
         visual="after the meal: Asil slouched in a chair at the table, grinning at a phone held sideways in both hands (screen facing away, only a glow); in the background Laira walking towards the glass door with a phone at her ear; Sadhee and Shahid standing a little apart by the potted palms, chatting and laughing; empty pizza boxes on the table",
         camera="medium wide, eye level, the table top as the lower third", amb="rooftop_day"),
    dict(to=31, reason="location and action change: Saba goes to the railing and looks down; Lail joins her", chars=["saba_young", "lail_young"], loc="railing_sunset",
         visual="Saba standing at the glass railing with both hands resting on the top rail, looking down at the tiny city far below; Lail standing an arm's length away, leaning on the railing with his arms folded, turning his head to look at her; the sunset sky behind them",
         camera="medium wide two-shot from the side, slightly behind, their faces in the upper half, the railing and the drop to the city as the lower third", amb="rooftop_day"),
    dict(to=36, reason="emotional turning point: the Dhivehi lesson - wind, shyness and a shared smile at sunset", chars=["saba_young", "lail_young"], loc="railing_sunset",
         visual="Saba at the railing holding the fluttering loose end of her white hijab down with both hands in the breeze, cheeks flushed, a shy embarrassed smile, eyes lowered; Lail an arm's length away facing her, smiling encouragingly; the sky blazing amber and violet behind them",
         camera="medium close two-shot, eye level, faces in the upper half, the railing as the lower third", amb="rooftop_day",
         sens="clothing", safe="narration's loose hair blowing in the wind shown as the loose end of her hijab fluttering; hair fully covered"),
    dict(to=39, reason="time change (night falls, terrace lights on) and character enters: Asil comes to tease them", chars=["asil_young", "lail_young", "saba_young"], loc="terrace_night",
         visual="Asil (17) stopping beside the two at the railing with a sly teasing grin, hands in his pockets; Lail calm and composed, arms folded; Saba a step apart, pushing the edge of her white hijab away from her face, frowning at Asil in mock annoyance; string lights glowing overhead",
         camera="medium wide three-shot, eye level, faces in the upper half, the railing as the lower third", amb="rooftop_night"),
    dict(to=43, reason="action change: Asil bursts out laughing at Saba's broken Dhivehi, Lail glares, Shahid calls Asil away", chars=["asil_young", "saba_young", "lail_young", "shahid_young"], loc="terrace_night",
         visual="Asil doubled over laughing, one hand raised in apology; Saba blushing red with embarrassment, hands over her mouth; Lail glaring sideways at Asil; in the background by the lit pool Shahid waving Asil over",
         camera="medium wide, eye level, faces in the upper half, the tiles as the lower third", amb="rooftop_night"),
    dict(to=46, reason="action change: alone again, Lail teases her and Saba quickly pins her loosened hijab", chars=["saba_young", "lail_young"], loc="terrace_night",
         visual="Saba at the railing, flustered and smiling, quickly fastening the loose end of her white hijab with a small pin, eyes down; Lail an arm's length away leaning on the railing with a mischievous little smile, watching her; string lights and the city glitter behind",
         camera="medium two-shot, eye level, faces in the upper half, the railing as the lower third", amb="rooftop_night",
         sens="clothing", safe="narration's hair tie / tying back her hair shown as her fastening her hijab with a pin; hair fully covered"),
    dict(to=49, reason="emotional peak: Lail softly speaks a line of verse; Saba lowers her head, her heart stirring", chars=["lail_young", "saba_young"], loc="terrace_night",
         visual="Lail standing at the railing looking out over the night city, speaking softly as if to himself, a gentle dreamy expression; Saba an arm's length away, her head lowered shyly, a hand resting on her heart, a small blushing smile; moonlight and warm string lights",
         camera="medium two-shot from the side, faces in the upper half, the railing and the glittering city as the lower third", amb="rooftop_night",
         sens="intimacy", safe="no whisper at her ear: he speaks quietly towards the city, standing an arm's length away"),
    dict(to=51, reuse="beat_012", reason="Asil comes back to them: time to go; he pats Lail's shoulder", loc="terrace_night",
         visual="(reuse)", amb="rooftop_night"),
    dict(to=55, reason="location change: downstairs sitting room; Maama sees them off, Saba remembers her bag", chars=["saba_young", "shafeeqa", "asil_young", "sadhee_young"], loc="sitting",
         visual="the friends at the foot of the floating staircase in the lamp-lit sitting room: grandmother Shafeeqa smiling warmly in her doorway; Saba pointing down the corridor towards a room door with a sudden 'oh!' look; Asil gesturing 'go, quickly'; Sadhee bending to pick up her sandals by the shoe rack near the front door",
         camera="medium wide, eye level, faces in the upper half, the polished floor as the lower third", amb="living_night"),
    dict(to=58, reason="location change: Saba alone in Lail's room picks up his photo from the study desk", chars=["saba_young"], loc="bedroom",
         visual="Saba with her shoulder bag on, standing at the study desk in the lamplight holding a small framed photo of a smiling teenage boy (the photo small and softly blurred), smiling tenderly down at it; school books stacked on the desk, city lights in the window",
         camera="medium shot, eye level, her face in the upper third, the desk top as the lower third", amb="room_night"),
    dict(to=62, reason="character enters: Lail appears; verse and teasing across the room", chars=["saba_young", "lail_young"], loc="bedroom",
         visual="Saba standing just inside the wide-open doorway of the room clutching her bag strap, startled then blushing with a shy smile; Lail standing far back across the room by the window with the night city behind him, leaning on the window frame with a mischievous smile, several steps of open floor between them",
         camera="medium wide, eye level, faces in the upper half, the wooden floor between them as the lower third", amb="room_night",
         sens="intimacy", safe="no whispering at her ear and no closeness in the bedroom: she stays at the open doorway, he stands far back by the window"),
    dict(to=67, reason="emotional turning point: the unspoken moment - she turns back at the door, a long look, 'I'll be waiting'", chars=["saba_young", "lail_young"], loc="bedroom",
         visual="Saba at the open doorway, turning back over her shoulder with a shy smile, about to leave; Lail several steps away in the middle of the room, one hand half raised towards her and stopped in mid-air, surprised at himself, then smiling at her lovingly; a long silent look between them, the desk lamp glowing",
         camera="medium wide two-shot, eye level, faces in the upper half, the floor as the lower third", amb="room_night",
         sens="intimacy", safe="the narration's hand-holding is replaced by his hand half raised and stopped in mid-air several steps away; no touching"),
    dict(to=70, reason="location change: farewell at the lift; Lail waves from the open door as the lift doors close", chars=["saba_young", "lail_young", "sadhee_young", "asil_young"], loc="landing",
         visual="seen from inside the lift: the steel doors sliding shut, through the narrowing gap Lail standing in the warm light of the open penthouse door across the landing, raising his hand in farewell; in the foreground inside the lift Saba giving a small shy wave with a soft smile, Sadhee and Asil beside her grinning",
         camera="medium shot from inside the lift, faces in the upper half, the lift floor as the lower third", amb="home_night"),
    dict(to=74, reason="location change: inside the lift the friends tease Saba", chars=["saba_young", "sadhee_young", "asil_young", "shahid_young"], loc="lift",
         visual="Saba in the middle of the lift frowning with her eyebrows knitted, cheeks pink; Sadhee playfully bumping her shoulder against Saba's with a hidden grin; Asil standing on the other side a little apart, grinning slyly; Shahid in the back corner raising his eyebrows teasingly",
         camera="medium wide, eye level, faces in the upper half, the lift floor as the lower third", amb="home_night"),
    dict(to=77, reason="action change: the lift opens on the ground floor; Saba walks out, everyone laughing", chars=["saba_young", "sadhee_young", "asil_young", "shahid_young"], loc="lobby",
         visual="the lift doors open onto the lobby; Saba stepping out first with a flustered smile, chin up; behind her Sadhee, Asil and Shahid laughing out loud",
         camera="medium wide, eye level, faces in the upper half, the polished floor as the lower third", amb="home_night"),
    dict(to=80, reason="location change: the street at night, Asil waving up at the tower", chars=["asil_young", "saba_young", "sadhee_young", "shahid_young"], loc="street",
         visual="the four friends walking along the lamp-lit street at the foot of the tall tower; Asil a step ahead, looking up and waving at the top of the building with a mocking grin; Sadhee nudging Saba's shoulder with her own, teasing; Saba embarrassed; Shahid laughing",
         camera="medium wide, eye level, faces in the upper half, the street as the lower third", amb="street_night"),
    dict(to=82, reason="emotional ending: Saba looks up and sees Lail, tiny, on the high balcony", loc="lookup",
         visual="low-angle view up the tall tower at night: far, far up at the very top a small lit balcony with string lights where the tiny distant silhouette of a teenage boy stands at the railing looking down",
         camera="extreme low angle, the tiny lit balcony near the top of the frame, the dark lower part of the tower and a lamp-lit edge of the street as the lower third", amb="street_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Saba too switched off her phone screen and looked at Lail. In that moment a silent but deeply meaningful smile passed between them.")
sh(2, "'How are you?' Lail asked gently. 'I am doing great. Thank you for asking. What about you?' Saba asked.")
sh(3, "'Not completely fine yet. But thank you so much for messaging every night to check on me. It truly makes me happy.'")
sh(4, "Lail said, looking at Saba. Saba only smiled. But Lail saw her eyes slowly filling with tears.")
sh(5, "'My father also passed away six months ago. I can understand what Lail must be going through.'", hum=True)
sh(6, "As she said it, a tear fell from Saba's eye and ran down her cheek. The tear landed on the palm Lail had held out.",
   [("sob_breath", "ކަރުނަތިކި", -24)], hum=True)
sh(7, "Saba looked first at Lail, and then at Lail's hand. In the middle of his palm the tear trembled.")
sh(8, "Lail slowly closed his hand. 'Do you know what a tear tastes like?' Lail asked with feeling. 'Salt,' Saba answered.")
sh(9, "From the way Lail looked, Saba thought she had given the wrong answer. Even so, a faint smile came over Lail's lips.")
sh(10, "Saba asked whether her answer was wrong. Lail slowly shook his head to say no, and opened his palm.")
sh(11, "The wetness of the tear was still on his hand. 'This tear might even be one shed centuries ago by a lover in grief,")
sh(12, "or the tear of a little child, a mother, a father, a sibling, or some other living creature.'")
sh(13, "Lail said, gazing at his palm, deep in thought. Saba sat listening attentively. 'I'm talking real nonsense, aren't I?'")
sh(14, "Lail asked with a faint smile. 'No, that could actually be true,' Saba said, agreeing with Lail. 'How so?'")
sh(15, "Lail asked very eagerly. Saba took a moment to think. 'You take that long to answer such a small question? Shall I tell you?")
sh(16, "The amount of water in the world neither increases nor decreases. The salt water of the oceans, the water that we and other living things drink,")
sh(17, "the water that leaves our bodies, the water used for cleansing and every other purpose - it rises into the sky as vapour and falls to the earth again as rain.")
sh(18, "This natural cycle has been repeating for many centuries,' Lail explained. With a gentle smile, Saba wiped the corners of her eyes.")
sh(19, "Just then Laira came out carrying three pizza boxes stacked on top of each other. Behind her, Shafeeqa came out too, carrying a basket of small Coke bottles.",
   [("door_open", "ނުކުތީ", -22)])
sh(20, "Asil and Shahid went and took the pizza boxes from Laira, and Sadhee took the basket from Maama's hands. They laid everything out on the table.",
   [("cup_clatter", "އަތުރައިލިއެވެ", -22)])
sh(21, "'Make sure Lail and Laira eat properly, okay!' Maama whispered very quietly in Asil's ear. Asil nodded in agreement.")
sh(22, "'Eat happily,' Maama said with a smile. As Maama left, Laira went and sat beside Sadhee and started chatting.")
sh(23, "'Hey, aren't you coming? Come and eat.' Asil beckoned Lail and Saba with a wave of his hand.")
sh(24, "The two got up almost together and went to sit at the table with their friends. Saba sat next to Sadhee, and Lail sat beside Asil.")
sh(25, "Even while eating, Saba and Lail kept stealing glances at each other. It seemed as if both of them wanted to say something important.")
sh(26, "After eating, everyone stayed on there to talk. Then Laira got a phone call and walked off towards the sitting room.",
   [("phone_buzz", "ފޯނެއް", -20)])
sh(27, "While Sadhee and Shahid drifted to one side deep in conversation, Asil started playing a game on his phone.",
   [("phone_game_taps", "ގޭމުކުޅެން", -22)])
sh(28, "Saba got up from her seat and went to stand by the balcony railing. Resting her hands on the railing, she looked down. It was a very tall building.")
sh(29, "Lail came up behind her and leaned on the railing with his arms folded. 'Can I ask you something?'")
sh(30, "Lail asked gently, looking at Saba. 'Hmm,' Saba said, turning towards him.")
sh(31, "'Between Australia and the Maldives, where would Saba rather live?' Lail asked. 'Maldives.'")
sh(32, "Saba answered, holding down with both hands her hair that was blowing in the wind. 'Then from today, try speaking in Dhivehi.'",
   [("wind_gust", "ވައިރޯޅިތަކާއެކު", -20)])
sh(33, "Lail said. When Lail said that, Saba felt shy. Lail carried on.")
sh(34, "'This is nothing to be shy about. It doesn't matter if you say it wrong - I'll correct you. We have to respect our own language.'")
sh(35, "Lail said with a smile. Saba too let a smile come to her lips. Once again silence settled between them.")
sh(36, "They looked at each other and exchanged a faint smile. The sun set, and as darkness fell over the world, the terrace lights came on.")
sh(37, "'What cosy talk are you two having?' Asil asked, stopping beside them. 'Since everyone was busy with different things,")
sh(38, "the two of us just talked to pass the time,' Lail said very calmly. 'Hmm, sure! Look closely and you can tell, right?'")
sh(39, "Asil said in a teasing tone. 'Don't talk nonsense now!' Saba said, pushing aside the hair that was falling over her face.")
sh(40, "Although she said it in Dhivehi, the sentence didn't come out right. Asil burst out laughing at that. Saba turned red with embarrassment.")
sh(41, "At that very moment Lail glared at Asil. 'Sorry, sorry.' He started laughing again. Instead of Saba, it was Lail who faced up to Asil.")
sh(42, "Just then Shahid called Asil. 'Asil. Come over here for a moment,' Shahid called.")
sh(43, "As Asil left, laughing and teasing Saba, complete silence fell between the two of them once again.")
sh(44, "The way Lail kept looking at her made Saba a little shy. 'Why don't you tie your hair with that hair tie in your hand?'")
sh(45, "Lail said with a mischievous smile. Saba grew even shyer. She had completely forgotten there was a hair tie in her hand. 'Oh!")
sh(46, "I really did forget all about it.' Saba quickly took the hair tie from her hand, gathered her hair back and tied it. At that moment,")
sh(47, "words slipped softly from Lail's lips: 'Heart, soul, tongue and pen all turn against me, unable to describe it - yet it becomes just as I wish when you say it so simply, with love.'")
sh(48, "These lines left Lail's lips very gently. However quietly he said them, their sweet feeling reached Saba's ears.")
sh(49, "As Saba shyly lowered her head, it was as if a new beat struck in her heart. Lail's words had stirred an unknown tremor in Saba's heart.",
   [("heartbeat", "ވިންދެއް", -20)], hum=True)
sh(50, "'Well, aren't you going? Let's go,' Asil said, coming over to them. 'Yes, it's already very late.'")
sh(51, "Saba answered quickly. Patting Lail's shoulder affectionately, Asil said, 'I'll send the lessons once I get home.'")
sh(52, "When they all went down the stairs together, there was nobody in the sitting room. Hearing their footsteps, Maama came out of her room and lovingly asked whether they were leaving.",
   [("footsteps_pavement", "ފިޔަވަޅުގެ", -24), ("door_open", "ކޮޓަރިން", -22)])
sh(53, "'My bag!' Saba suddenly remembered. 'Where did you leave it?' Asil asked. 'In that room.'")
sh(54, "Saba said, pointing towards Lail's room. 'Go get it, quick.' As Asil said that, Maama smiled.")
sh(55, "Just then Laira called, and Maama went into a room. As Asil and the others began putting on their shoes,")
sh(56, "Lail hurried off, unseen by them, and went into his room. Saba was just picking up her bag and putting it on her shoulder.",
   [("cloth_rustle", "ދަބަސް", -24)])
sh(57, "At that moment, Lail's photo frame on the study desk caught Saba's eye. Picking up the photo and looking at it - 'What a lovely smile,'")
sh(58, "she murmured softly to herself. As she put the frame back and turned, Saba was startled to see Lail leaning in the doorway.",
   [("gasp", "ސިހޭގޮތްވިއެވެ", -22)])
sh(59, "A mischievous smile came over Lail's lips. Taking a step towards Saba, he spoke beside her ear as if telling a secret.")
sh(60, "'As I write, my breath falters and my heart begins to tremble and beat; my diary is close to filling as I wait to hear your praise.' Those words made Saba even shyer.",
   [("heartbeat", "ވިންދާ", -22)], hum=True)
sh(61, "Even so, a gentle smile showed on her lips. 'Will you message tonight too, to check on me?' Lail asked playfully.")
sh(62, "'You're fine now, aren't you?' Saba answered with a smile too. Just then, hearing Asil call, Saba hurried to walk out of the room.")
sh(63, "But without thinking, Lail caught hold of Saba's hand. Lail himself was surprised by that sudden move.",
   [("breath", "ހިފަހައްޓައިލިއެވެ", -24)])
sh(64, "Saba's steps stopped, and she found herself looking at Lail's face. A deep silence fell over the room. Saba did not ask why he had taken her hand.", hum=True)
sh(65, "Nor did Lail have any answer to give. As a shy smile appeared on Saba's face,")
sh(66, "Lail too smiled lovingly, gazing into Saba's eyes. 'I'll be waiting.'", hum=True)
sh(67, "Lail said gently, letting go of Saba's hand. As Saba hurried out, Lail followed her out too.")
sh(68, "Not daring even to look back, Saba put on her shoes. Lail, standing out at the door, raised his hand in farewell. 'Going.'")
sh(69, "Saying that, Saba walked quickly and stepped into the lift. 'Did you go and weave a bag or what?' Sadhee teased jokingly.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -24), ("lift_ding", "ލިފްޓަށް", -18)])
sh(70, "Through the gap of the closing lift doors, Saba saw Lail. When Lail raised his hand again, Saba smiled softly and waved goodbye.")
sh(71, "Inside the lift, Sadhee and Asil playfully pressed against Saba's shoulders. Hidden smiles showed on both their faces.")
sh(72, "Shahid too looked at Saba and raised his eyebrows teasingly. 'What?' Saba asked, knitting her brows.")
sh(73, "'Looks like a flower is getting ready to bloom,' Asil teased. 'What were you two talking about by the pool? You looked so cosy!")
sh(74, "Lail, who never even talks to me or any other girl - today I saw him sitting close to Saba, deep in conversation!'")
sh(75, "Sadhee said, laughing. 'True. What were you talking about?' Shahid asked eagerly too. 'Nothing like what you're thinking.")
sh(76, "We talked about water,' Saba said, stepping out as the lift door opened. Everyone burst out laughing.",
   [("lift_ding", "ހުޅުވުމާއެކު", -18)])
sh(77, "They teased her all the more for trying to speak Dhivehi for Lail's sake. They all walked out together.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(78, "Walking ahead, Asil looked up towards Lail's apartment and waved. 'Got it - it was water you were talking about.")
sh(79, "Is he standing there watching until Saba is out of sight, hoping to get a drop of water?' Asil asked mockingly. 'We used to come here before too,")
sh(80, "but Lail never once came out on the balcony to watch,' Sadhee teased, bumping her shoulder against Saba's again.",
   [("cloth_rustle", "ޖައްސައިލަމުން", -24)])
sh(81, "When Saba looked up, she could see Lail, small, on the balcony of the tall building. Because of her friends' innocent teasing,", hum=True)
sh(82, "Saba could do nothing but lower her head in shyness.")
SHOTS = S

"""Beat/shot plan for Nindheveethimeymathee episode 401 (used by plan_beats.py).
SCHOOL timeline. Sana's last night, her death (an accident, NEVER shown), burial only as a distant cemetery at dawn,
family grief, Saba's first texts to Lail, a week later the lawyer, friends visit the rooftop pool terrace.
No touching between Lail and Saba; no swollen lip shown; nobody lying down; nobody swims."""

SANA_HOME = "Sana's modest modern apartment in Malé, Maldives"
PENT = "Haizum's luxurious multi-level penthouse in Malé, Maldives"
ASIL_HOME = "Asil's family's ordinary ninth-floor apartment in Malé, Maldives"

LOC = {
    "sana_room": f"Sana's bedroom in {SANA_HOME}: a double bed with a padded headboard and soft white pillows, a small bedside table with a warm lamp and a phone, beige curtains drawn over a night window, a closed white door at the back of the room",
    "saba_room": f"Saba's small simple bedroom in {ASIL_HOME}: a single bed with a plain headboard and a light-blue cover, a small bedside table, a narrow wardrobe, a small study desk with schoolbooks, a window with thin curtains over the city",
    "saba_door": f"the narrow inner corridor of {ASIL_HOME} seen from inside Saba's bedroom doorway: a plain wooden bedroom door standing open, a dim corridor beyond, tiled floor",
    "hospital": "the emergency-department corridor of a modern hospital in Malé: pale walls, a row of steel waiting chairs, closed double doors with frosted glass panels at the end, cold overhead strip lights, a nurse in light-blue scrubs and white hijab passing far in the background",
    "cemetery": "a traditional Maldivian cemetery in Malé seen from a distance: low whitewashed coral-stone walls, rows of simple carved coral-stone grave markers under the shade of old leafy trees, a white mosque wall nearby, a sandy ground",
    "lail_room": f"Lail's spacious bedroom in {PENT}: a large bed in the middle with small cabinets on both sides, a wall-wide wardrobe, a two-seater sofa, a study desk with a chair, a small balcony door to the right of the bed",
    "laira_room": f"Laira's bedroom in {PENT}: a bed with a soft pink cover and a padded headboard, a dressing table, sheer curtains",
    "haizum_room": f"a quiet master bedroom in {PENT}: a large bed with dark wood headboard, an armchair with a neatly folded ivory scarf lying on it, heavy curtains half drawn",
    "asil_living": f"the small open living room and kitchen of {ASIL_HOME}: a fabric sofa and a low table, a small TV on a cabinet (screen dark), a kitchen counter with a sink under a warm pendant light, a short corridor of bedroom doors",
    "memory_father": "a small plain apartment living room on a grey rainy day, rain on the window, a sofa and a side table, everything soft and blurred at the edges",
    "proverb": "a symbolic night landscape: in the foreground a tiny humble thatched palm-leaf hut lit only by the faint glow of a single small oil lamp in its doorway, a sandy path in front; far behind it across a dark lagoon a grand white mansion blazing with bright glittering chandeliers in every window",
    "pent_living": f"the elegant living room of {PENT}: a large cream sofa set, a low glass coffee table, a big flat TV on a wall cabinet, floor-to-ceiling windows over the Malé skyline and the lagoon, a front door in a marble entrance hall",
    "pent_door": f"the marble entrance hall of {PENT}: a tall wooden front door standing open, warm wall lights, a shoe cabinet",
    "upstairs": f"the upper floor of {PENT}: an elegant sitting room opening through tall glass doors onto a wide open rooftop terrace with a rectangular swimming pool of calm empty turquoise water, white beach loungers along the pool, a glass balcony railing, potted palms, the Malé skyline and the sea beyond",
}
MOOD = {
    "sana_room": "late night, the warm amber bedside lamp the only light, deep indigo shadows, a moonlit window behind the curtains, frightened tenderness, foreboding",
    "saba_room": "night, a soft lamp and the blue city glow through the thin curtains, quiet, dreamy and shy",
    "saba_door": "pre-dawn about half past five, dark blue light, a dim corridor bulb, sudden alarm",
    "hospital": "very early morning before sunrise, cold blue-white strip lighting, a hushed grieving silence",
    "cemetery": "dawn, the first pale gold light through a soft blue haze, still air, calm and sorrowful",
    "lail_room": "morning after the burial, curtains drawn, dim grey-blue light with a thin bright line of tropical daylight at the edge, heavy grief",
    "laira_room": "morning, soft muted daylight through sheer curtains, tender sorrow",
    "haizum_room": "late morning, curtains half drawn, a dim grey-gold light, lonely grief",
    "asil_living": "late night, warm pendant light over the kitchen counter, the rest of the room in soft blue shadow, quiet and sleepy",
    "memory_father": "soft hazy dreamlike memory glow, grey rainy daylight, raw grief",
    "proverb": "soft hazy dreamlike glow, deep blue night, a faint warm lamp versus dazzling golden chandelier light, reflective",
    "pent_living": "a bright tropical day one week later, clear weather, soft daylight from the big windows but a heavy, subdued mood inside",
    "pent_door": "bright clear afternoon, soft daylight, warm welcome",
    "upstairs": "a bright clear tropical afternoon, sunny blue sky with a few white clouds, sparkling calm pool water, a light sea breeze, gentle shy hope",
}

L_DEF = "Lail in his light-grey t-shirt and jeans"
HZ_HOME = "Haizum in a plain white shirt with the sleeves rolled up, no jacket, no tie"

BEATS = [
    # --- Sana's last night ---
    dict(to=2, reason="episode opening: Haizum supports exhausted Sana back to her bed", chars=["haizum", "sana"], loc="sana_room",
         visual=f"{HZ_HOME}, standing beside his wife Sana and steadying her with one hand on her shoulder and the other holding her hand, slowly walking her from a closed white door at the back of the room towards the bed; Sana in her sage-green dress and ivory hijab fully covering her hair and neck, pale, exhausted, eyes half closed; his face tight with worry",
         camera="medium wide, eye level, their faces in the upper third, the carpet as a calm lower third", amb="apartment_quiet_night",
         sens="other", safe="the vomiting is not shown: only her exhaustion as he walks her from a closed door"),
    dict(to=8, reason="action change: Sana resting, Haizum phones Ilyas in New York for a specialist", chars=["haizum", "sana"], loc="sana_room",
         visual=f"Sana sitting up against the padded headboard with a light blanket over her legs, ivory hijab fully covering her hair and neck, eyes closed, utterly drained; {HZ_HOME}, standing beside the bedside table holding a phone to his ear, looking down at her with deep worry, his free hand on his hip",
         camera="medium shot, eye level, faces in the upper half, the blanket as a calm lower third", amb="apartment_quiet_night"),
    dict(to=14, reason="action change: he sits beside her; she admits she has been ill for days; both in tears", chars=["haizum", "sana"], loc="sana_room",
         visual=f"{HZ_HOME}, sitting on the edge of the bed beside Sana and gently holding her hand in both of his, eyes full of tears; Sana sitting up against the headboard, ivory hijab fully covering her hair and neck, tears running down her pale cheeks, looking at him with tired resignation; the warm lamp beside them",
         camera="medium close two-shot, eye level, faces in the upper half", amb="apartment_quiet_night",
         sens="intimacy", safe="married couple: only holding hands while sitting side by side, fully clothed"),
    # --- Saba, same night ---
    dict(to=19, reason="scene change: Saba in her room at night, smiling at the thought of Lail", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting up against the plain headboard of her single bed, hugging a soft pillow to her chest, her phone set aside on the cover, eyes closed with a faint shy dreamy smile, one hand lightly touching her own cheek; powder-blue dress and white hijab fully covering her hair and neck",
         camera="medium shot, eye level, her face in the upper third, the bed cover as a calm lower third", amb="room_night",
         sens="other", safe="narration says she lies down: shown sitting up against the headboard"),
    dict(to=22, reason="time jump: knocking wakes her at half past five", chars=["saba_young"], loc="saba_room", transition="black",
         visual="Saba sitting up in her bed in the dark blue pre-dawn light, rubbing one sleepy eye, holding her phone whose screen gives only a soft glow on her face, looking towards the bedroom door with a puzzled frown; white hijab fully covering her hair and neck, powder-blue dress",
         camera="medium shot, slightly from the side, the door in the soft background", amb="room_night",
         sens="other", safe="phone shows only a glow, no clock digits"),
    dict(to=23, reason="action/character change: she opens the door to a worried Asil", chars=["saba_young", "asil_young"], loc="saba_door",
         visual="Saba standing just inside her open bedroom door, white hijab fully covering her hair and neck, one hand still on the door handle; Asil standing in the dim corridor an arm's length away in his maroon t-shirt, face full of anxiety, eyes wet, urging her to hurry",
         camera="medium two-shot, eye level, faces in the upper half, tiled floor as the lower third", amb="home_night"),
    dict(to=26, reason="emotional turning point: the news that Lail's mother has died", chars=["saba_young"], loc="saba_door",
         visual="close-up of Saba frozen in shock in the doorway, very large eyes wide open, one hand raised to her mouth, white hijab fully covering her hair and neck, the dim corridor light on her face",
         camera="close-up, eye level, her face in the upper half", amb="home_night", sens="other",
         safe="the death is only heard as news; shown as her shocked face"),
    dict(to=29, reuse="beat_006", reason="return to the doorway: Asil explains Lail called crying, Thitthi will drive them", loc="saba_door",
         visual="(reuse)", amb="home_night"),
    # --- Hospital ---
    dict(to=31, reason="scene change: hospital emergency corridor, Lail outside the ER, Laira with Maama", chars=["lail_young", "laira", "shafeeqa"], loc="hospital",
         visual=f"{L_DEF}, standing alone near the closed frosted ER doors, hands hanging at his sides, staring at the floor, numb; on the steel chairs nearby Laira in her dusty-pink dress and dove-grey hijab fully covering her hair and neck, weeping with her head on the shoulder of her grandmother Maama Shafeeqa in maroon libaas, white headscarf and gold glasses, who sits frozen, staring ahead with deep silent sorrow",
         camera="medium wide, eye level, faces in the upper half, the corridor floor as a calm lower third", amb="hospital_corridor",
         sens="other", safe="death shown only through grief in the corridor; the ER doors stay closed"),
    dict(to=34, reason="characters enter: Asil and Saba arrive and stand silently beside Lail; relatives gather", chars=["lail_young", "asil_young", "saba_young"], loc="hospital",
         visual=f"{L_DEF}, standing by the corridor wall with red, empty eyes; Asil standing right beside him; Saba standing a step further away from Lail at a respectful distance, hands clasped in front of her, sad eyes on him, white hijab fully covering her hair and neck; blurred relatives in modest clothes and hijabs gathering quietly in the background",
         camera="medium wide, eye level, faces in the upper half", amb="hospital_corridor"),
    # --- Burial (distant only) ---
    dict(to=39, reason="scene change: the burial, shown only as a distant cemetery at dawn", loc="cemetery", transition="black",
         visual="a distant view across low whitewashed coral-stone walls into the cemetery at dawn: a quiet gathering of men in white clothes standing in rows under the trees with their heads bowed, small and far away; one solitary man standing apart by the low wall with his arms folded; no close-up of any grave, nothing carried",
         camera="wide shot from outside the low wall, the trees and figures in the upper half, the sandy ground as a calm lower third", amb="cemetery_dawn",
         sens="other", safe="burial only as a distant cemetery at dawn with white-clad men; no body, no bier, no close-up"),
    # --- Home grief ---
    dict(to=41, reason="scene change: back home, Lail breaks down alone behind his closed door", chars=["lail_young"], loc="lail_room",
         visual="Lail in a plain white shirt, kneeling on the floor with his back against his closed bedroom door, both hands covering his face, shoulders shaking as he finally weeps; a thin line of daylight at the curtain edge",
         camera="medium shot, slightly high angle, his bowed head in the upper half, the floor as a calm lower third", amb="room_day"),
    dict(to=43, reason="character change: Maama comforts Laira in her room", chars=["laira", "shafeeqa"], loc="laira_room",
         visual="Laira sitting in a cushioned armchair by the window with her eyes closed and a sad, tired face, dove-grey hijab fully covering her hair and neck; her grandmother Maama Shafeeqa in maroon libaas, white headscarf and gold glasses standing beside the armchair, gently resting one hand on Laira's head with a tender, caring expression",
         camera="medium two-shot, eye level, faces in the upper half, the cover as a calm lower third", amb="room_day",
         sens="other", safe="narration says Laira is lying in bed crying: shown sitting quietly in an armchair, Maama beside her"),
    dict(to=46, reason="character change: Haizum alone in the room, praying and whispering Sana's name", chars=["haizum"], loc="haizum_room",
         visual="Haizum in a plain white long-sleeved shirt sitting on the edge of the bed, elbows on his knees, both hands joined and pressed to his forehead, eyes shut, tears on his cheeks, lips trembling; beside him on the armchair Sana's ivory scarf lies neatly folded",
         camera="medium shot, eye level, his face in the upper half", amb="room_day",
         sens="other", safe="loss shown through Sana's folded ivory scarf and his prayer"),
    # --- That night at Asil's home ---
    dict(to=51, reason="scene/time change: sleepless Saba steps out; Asil at the sink, his mother turning in", chars=["saba_young", "asil_young"], loc="asil_living", transition="black",
         visual="Saba standing at the corridor entrance in her powder-blue dress and white hijab fully covering her hair and neck, tired sleepless eyes; Asil in his maroon t-shirt at the kitchen counter placing a glass in the sink and looking over at her; Asil's mother, a kind Maldivian woman of about fifty in a loose dark-green dress and black hijab, standing up from the sofa with the TV remote, the TV screen dark, speaking gently to Saba",
         camera="medium wide, eye level, faces in the upper half, the floor as a calm lower third", amb="living_night"),
    dict(to=54, reason="action change: Asil saves Lail's number in Saba's phone", chars=["asil_young", "saba_young"], loc="asil_living",
         visual="Asil standing by the kitchen counter tapping on Saba's phone with a half-smile and a warning look, the screen only a soft glow; Saba standing an arm's length away, waiting a little impatiently with her hands clasped, white hijab fully covering her hair and neck",
         camera="medium two-shot, eye level", amb="living_night",
         sens="other", safe="phone screen only a glow, no readable number"),
    dict(to=57, reason="scene change: back in her room she sends a short message and waits", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting on the edge of her bed holding her phone in both hands, its soft glow on her face, chewing her lip with anxious hope as she waits for a reply; white hijab fully covering her hair and neck; the dark window behind her",
         camera="medium shot, eye level, her face in the upper third", amb="room_night",
         sens="other", safe="phone screen only a glow; she sits instead of lying back"),
    dict(to=58, reason="action change: a sudden 'Hi' makes her jump and the phone slips", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting up against her headboard, startled, eyes wide, both hands flying up in surprise as her phone tumbles out of her fingers onto the bed cover, its screen glowing softly; white hijab fully covering her hair and neck",
         camera="medium shot, eye level, her face in the upper third", amb="room_night",
         sens="other", safe="the phone falling on her face is shown only as it slipping from her hands"),
    dict(to=60, reason="action change: she hurries to the mirror, hand at her mouth", chars=["saba_young"], loc="saba_room",
         visual="Saba standing in front of a small wall mirror by the wardrobe, one hand pressed over her mouth, wincing with a comic pained frown, her reflection in the mirror showing the same; white hijab fully covering her hair and neck, powder-blue dress",
         camera="medium shot over her shoulder towards the mirror, faces in the upper half", amb="room_night",
         sens="other", safe="no swollen lip shown: her hand covers her mouth"),
    dict(to=63, reason="action change: cross-legged on the bed with an ice pack, she reads his two messages eagerly", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting cross-legged on her bed, her long dress covering her feet, holding a small blue ice pack against her mouth with one hand and her phone in the other, eyes wide and eager as she reads, the soft glow of the screen on her face; white hijab fully covering her hair and neck",
         camera="medium shot, eye level, her face in the upper third", amb="room_night",
         sens="other", safe="phone shows only a glow; the ice pack hides her lip"),
    dict(to=67, reason="action change: ice pack put aside, she types quickly and they exchange good-nights", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting cross-legged on her bed typing on her phone with both thumbs, a small shy smile, the ice pack resting on the little bedside table; the screen only a soft glow seen from the side; white hijab fully covering her hair and neck",
         camera="medium close-up, slightly from the side, her face in the upper half", amb="room_night",
         sens="other", safe="no readable messages; screen only a glow"),
    dict(to=70, reason="emotional change: staring at his photo until the screen goes dark; a heavy sigh", chars=["saba_young"], loc="saba_room",
         visual="Saba sitting against her headboard holding the ice pack loosely at her lips, gazing down at her phone whose screen has just gone dark, her brows drawn together in an unnameable ache; moonlight from the window on her face; white hijab fully covering her hair and neck",
         camera="close-up, eye level, her face in the upper half", amb="room_night"),
    dict(to=74, reason="memory: five months ago, her father's death, only her mother to comfort her", chars=["saba_young"], loc="memory_father", transition="dissolve",
         visual="a memory: Saba in a plain black dress and black hijab fully covering her hair and neck, sitting on a sofa weeping with her face in her hands; her mother, a Maldivian woman in her forties in a dark-grey dress and grey hijab, sitting close beside her rubbing her back with a grieving face; no one else in the empty room",
         camera="medium shot, eye level, faces in the upper half", amb="memory_rain", hum=True,
         sens="other", safe="her father's death is never shown: only the two mourners alone"),
    dict(to=77, reason="the narrator's proverb: few visit the poor man's hut, many crowd the rich man's mansion (symbolic)", loc="proverb", transition="dissolve",
         visual="a tiny humble thatched hut glowing faintly with a single small oil lamp in the foreground, its sandy path empty, while far behind it across dark water a grand white mansion blazes with glittering crystal chandeliers in every window and many small distant figures walk towards it; no faces visible",
         camera="wide shot, the mansion and sky in the upper half, the empty sandy path as a calm lower third", amb="memory",
         sens="other", safe="symbolic illustration of the proverb"),
    dict(to=79, reuse="beat_022", reason="return to the present: Saba sets the ice pack aside with a sad smile", loc="saba_room",
         visual="(reuse)", amb="room_night", transition="dissolve"),
    # --- One week later ---
    dict(to=83, reason="time jump: a week later at Haizum's penthouse; Laira withdrawn, Haizum home from work, Maama staying", chars=["laira", "haizum", "shafeeqa"], loc="pent_living", transition="black",
         visual="Laira sitting curled in the corner of the large cream sofa hugging a cushion, staring blankly at nothing, dove-grey hijab fully covering her hair and neck; Haizum in a casual dark-grey polo shirt and trousers standing behind the sofa watching her with heavy concern; Maama Shafeeqa in maroon libaas and white headscarf sitting beside Laira with a hand on her shoulder",
         camera="medium wide, eye level, faces in the upper half, the glass coffee table as a calm lower third", amb="home_day"),
    dict(to=88, reason="action change: Haizum switches off the TV; Shafeeqa urges that only justice will bring peace", chars=["haizum", "shafeeqa"], loc="pent_living",
         visual="Haizum in a dark-grey polo shirt sitting on the sofa, lowering the TV remote, the wall TV now dark, his face weary and pained; Maama Shafeeqa sitting on the sofa beside him, turned towards him, speaking earnestly with sorrowful eyes behind her gold glasses",
         camera="medium two-shot, eye level, faces in the upper half", amb="home_day",
         sens="other", safe="the TV news about the accident is never shown; the screen is dark"),
    dict(to=90, reason="emotional turning point: Haizum relives the night and breaks down", chars=["haizum", "shafeeqa"], loc="pent_living",
         visual="Haizum sinking back into the sofa with both hands covering his face, shoulders bowed in grief; his mother Maama Shafeeqa beside him resting a comforting hand on his shoulder, her own eyes wet",
         camera="medium close-up, eye level, faces in the upper half", amb="home_day", hum=True),
    dict(to=92, reason="character enters: Shafeeqa opens the door to the lawyer", chars=["shafeeqa"], loc="pent_door",
         visual="Maama Shafeeqa holding the tall front door open with a polite welcoming gesture; in the doorway a Maldivian lawyer of about forty-five in a charcoal suit and trousers, neatly trimmed moustache, holding a plain closed file folder under his arm, nodding respectfully",
         camera="medium wide, eye level, faces in the upper half, the marble floor as a calm lower third", amb="home_day"),
    dict(to=98, reason="action change: the lawyer meeting — the motorcyclist is arrested; Haizum reads the papers; coffee served", chars=["haizum", "shafeeqa"], loc="pent_living",
         visual="Haizum in a dark-grey polo shirt sitting on the sofa with red, teary eyes, reading a document whose lines are only soft illegible grey marks; the lawyer in a charcoal suit sitting in an armchair beside him with an open file on his knee, speaking reassuringly; Maama Shafeeqa setting down two cups of coffee from a tray on the glass table",
         camera="medium wide, eye level, faces in the upper half, the coffee table as a calm lower third", amb="home_day",
         sens="other", safe="the accident and the arrest are only talked about; document shows no readable text"),
    # --- Friends visit ---
    dict(to=101, reason="characters enter: Lail's friends at the door, Shafeeqa welcomes them", chars=["shafeeqa", "asil_young", "sadhee_young", "saba_young"], loc="pent_door",
         visual="Maama Shafeeqa at the open front door smiling warmly and beckoning the young visitors in; Asil in his maroon t-shirt in front, Sadhee in her rust-orange dress and cream hijab beside him, a slim teenage boy in a white t-shirt and black trousers (Shahid) behind them, and Saba a little behind at the side, shy, white hijab fully covering her hair and neck, powder-blue dress",
         camera="medium wide, from inside the hall, faces in the upper half", amb="home_day"),
    dict(to=105, reason="scene change: Lail's spacious room; friends settle while Saba looks around", chars=["saba_young", "lail_young", "asil_young", "sadhee_young"], loc="lail_room",
         visual=f"Saba standing hesitantly just inside the doorway of the spacious bedroom, looking around in quiet wonder; across the room {L_DEF} sitting up on the two-seater sofa looking tired, Asil sitting beside him, Sadhee in rust-orange dress and cream hijab sitting on the study-desk chair; the big bed, wall-wide wardrobe and small balcony door visible; bright daylight",
         camera="wide shot from behind Saba's shoulder, faces in the upper half, the floor as a calm lower third", amb="room_day"),
    dict(to=107, reason="emotional moment: their eyes meet; a shy smile", chars=["saba_young", "lail_young"], loc="lail_room",
         visual=f"Saba now sitting on a chair by the desk, glancing up across the room with a shy blushing smile, white hijab fully covering her hair and neck; {L_DEF} on the sofa several metres away looking up at her with a gentle faint smile; the space of the room between them",
         camera="medium wide two-shot, eye level, both faces in the upper half", amb="room_day",
         sens="intimacy", safe="only an exchanged glance across the room, no contact"),
    dict(to=110, reason="character enters: Maama at the door offers pizza and sends them upstairs", chars=["shafeeqa", "lail_young", "asil_young"], loc="lail_room",
         visual=f"Maama Shafeeqa standing in the open bedroom doorway with a kind smile, asking the children; {L_DEF} on the sofa turning to her with a small tired smile; Asil beside him grinning and gesturing politely",
         camera="medium wide, eye level, faces in the upper half", amb="room_day"),
    dict(to=113, reason="action change: everyone leaves; Lail and Saba walk out last, apart, silent", chars=["lail_young", "saba_young"], loc="lail_room",
         visual=f"Saba and Lail walking out of the bedroom doorway one after the other, a full arm's length apart, glancing at each other without a word; Saba in powder-blue dress and white hijab fully covering her hair and neck, {L_DEF}; the other friends' backs disappearing up a staircase beyond",
         camera="medium shot, eye level, faces in the upper half", amb="room_day",
         sens="intimacy", safe="they walk apart, no contact"),
    # --- Rooftop terrace ---
    dict(to=116, reason="scene change: the upper floor and the rooftop terrace with the pool", chars=["sadhee_young", "saba_young", "asil_young", "shahid_young"], loc="upstairs",
         visual="the friends settling on the sunny rooftop terrace beside the calm, empty turquoise pool: Sadhee in rust-orange dress and cream hijab sitting comfortably on a white lounger with its backrest raised, waving Saba over; Saba walking towards the next lounger, white hijab fully covering her hair and neck; Asil in maroon t-shirt and Shahid in white t-shirt sitting on chairs by the glass railing, already chatting; nobody in the water",
         camera="wide shot, eye level, faces in the upper half, the still pool water as a calm lower third", amb="rooftop_day",
         sens="other", safe="the pool is empty and calm; nobody swims; Sadhee sits instead of lying"),
    dict(to=121, reason="action change: Lail at the railing watching Saba while she whispers with Sadhee", chars=["lail_young", "saba_young", "sadhee_young"], loc="upstairs",
         visual=f"in the foreground Saba and Sadhee sitting on two neighbouring white loungers, leaning towards each other and whispering, Saba with a sulky frown; in the background {L_DEF} leaning against the glass balcony railing, quietly watching Saba; the sea and skyline behind him",
         camera="medium wide, eye level, faces in the upper half", amb="rooftop_day"),
    dict(to=123, reason="action change: Sadhee goes to talk to Lail; his eyes keep drifting to Saba, who scrolls her phone", chars=["lail_young", "sadhee_young", "saba_young"], loc="upstairs",
         visual=f"{L_DEF} at the glass railing talking with Sadhee, who stands an arm's length from him gesturing cheerfully, but his eyes glancing past her towards the loungers; in the foreground Saba sitting alone on a lounger looking down at her phone, its screen only a soft glow, pretending not to notice",
         camera="medium wide, eye level, faces in the upper half", amb="rooftop_day",
         sens="other", safe="phone shows only a glow"),
    dict(to=125, reason="action change: Lail slips away and sits on the lounger beside Saba; a silent meaningful smile", chars=["lail_young", "saba_young"], loc="upstairs",
         visual=f"Lail and Saba sitting on two separate neighbouring white loungers by the calm pool, a full arm's length apart, turned slightly towards each other and sharing a quiet, meaningful smile; Saba has lowered her dark phone to her lap; {L_DEF}; Saba in powder-blue dress and white hijab fully covering her hair and neck; friends blurred in the background",
         camera="medium two-shot, eye level, faces in the upper half, the still pool water as a calm lower third", amb="rooftop_day",
         sens="intimacy", safe="separate loungers at arm's length, only a smile; no touching"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Haizum held Sana up. Even until the exhausted Sana came out after rinsing her mouth, Haizum kept holding her up.")
sh(2, "Then he took Sana to the bed, laid her down and covered her with a blanket. Utterly exhausted, Sana closed her eyes.",
   [("cloth_rustle", "ރަޖާއަޅައި", -24)])
sh(3, "Haizum picked up the phone from the little table by the bed, quickly found a number and called. \"Ilyas! It's me — where are you?\"")
sh(4, "Haizum asked. \"Right now I'm in New York,\" came Ilyas's voice from the other end. \"I'm calling because something urgent has come up.")
sh(5, "Could you arrange for us to go to the hospital right away and see a specialist?\" Looking at Sana,")
sh(6, "Haizum asked in a voice full of worry. \"Yes! Why not? Who are you trying to take?\" Ilyas asked.")
sh(7, "Haizum told him about the troubles Sana had been going through, and asked which doctor was the best one to see.")
sh(8, "Ilyas gave him the details of suitable doctors and told him the best one to see. After finishing with Ilyas, Haizum put the phone down and went and sat beside Sana.")
sh(9, "\"Did you vomit blood last night too?\" Haizum asked, lovingly stroking Sana's head. Sana nodded to say yes.")
sh(10, "\"Why didn't you tell me? What if this isn't something ordinary but something serious — what then?\"")
sh(11, "Haizum said softly, resting his head against hers. Tears began to fall from Sana's eyes.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(12, "Haizum's eyes filled with tears too — because she had been this ill and he had not known. \"Come, get up and get ready,",
   hum=True)
sh(13, "we're going to the hospital right now,\" Haizum said quietly. This time Sana did not resist.")
sh(14, "She too could feel that her time was running short. Yawning, Saba came into her room.", hum=True)
sh(15, "Since morning she had been busy without rest, finishing her unfinished lessons. Without even changing the clothes she was wearing,")
sh(16, "she lay down on that soft bed and settled. Hugging the pillow beside her and putting the phone in her hand aside, she closed her eyes.",
   [("cloth_rustle", "ބާލީސް", -24)])
sh(17, "Not long after closing her eyes, a faint smile came over those lips. After lying there a while,")
sh(18, "she slowly opened her eyelids and touched her own cheek. \"While gazing into these eyes with your eyes, what is the invitation you give them?\"")
sh(19, "Asking it to herself, with a faint smile on her lips, Saba closed her eyes. Saba was suddenly woken by the sound of someone knocking on her door.",
   [("knock", "ޓަކިދޭ", -16)])
sh(20, "Rubbing her sleep-heavy eyes she picked up the phone beside her and looked — it was only half past five in the morning. \"Who could it be at this hour?\"")
sh(21, "Saba asked herself, yawning. Just then came a knock on the door, even harder than before. \"Saba, it's me.\"",
   [("knock", "ތަޅައިގަތް", -14)])
sh(22, "It was Asil's voice outside. \"Something big must have happened.\" Straightening her messy hair, Saba went and opened the door. \"What happened?\"",
   [("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(23, "Saba asked, yawning. \"Come on, let's go quickly!\" Asil's face showed signs of extreme worry. \"Where to?\"")
sh(24, "Saba asked again. \"To the hospital. Lail's mother has passed away.\" Asil's eyes filled with tears. The news gave Saba a sudden shock.",
   [("gasp", "ސިހުމެކެވެ", -20)], hum=True)
sh(25, "She could only stand there with her eyes wide, not knowing what to say. At sunset Lail had left this house so very happy. And yet,")
sh(26, "what heartbreaking state must he be in now! \"Wh... what happened?\" Saba managed to ask in bewilderment. \"I don't know either.")
sh(27, "Lail just called and said his mum has passed away and they're at the hospital. He cried so much. You know how dearly Lail loves his mum, don't you?")
sh(28, "Will you come? If you want to come, get ready quickly. I've called Thitthi. Thitthi will take us,\" Asil said.")
sh(29, "Saba nodded, went inside and closed the door. Outside the emergency room Lail stood waiting,",
   [("door_close", "ލައްޕައިލިއެވެ", -20)])
sh(30, "because his father had asked him not to go in. Laira sat clinging to Maama, sobbing.",
   [("sob_breath", "ގިސްލާ", -24)])
sh(31, "However chaotic the hospital was, Shafeeqa sat frozen. Her face showed the deep grief and despair of losing her own son's beloved wife.")
sh(32, "Asil and Saba came into the hospital and went to where Lail stood. Without a single word, they quietly waited beside him.")
sh(33, "A little later some of Laira's friends came too. Slowly the relatives of Haizum's and Sana's families gathered.")
sh(34, "Everyone came and quietly waited. No one asked any more questions. Even that silence spoke of deep grief.")
sh(35, "The shade of the cemetery filled with Haizum's and Sana's families, and many friends and well-wishers besides.")
sh(36, "Laira's and Lail's close companions had also come to share their grief.")
sh(37, "Laira kept crying without stopping, wrapped in Shafeeqa's arms. How would she go on without her beloved mother?",
   [("sob_breath", "ރޮވެމުން", -24)])
sh(38, "Though no tears fell from Lail's eyes, those eyes showed an unbearable heartache.")
sh(39, "Haizum stood leaning against the wall with his arms folded, watching over Sana's lifeless body. His eyes were red and worn out from crying.",
   hum=True)
sh(40, "After coming back home from the cemetery, Lail went into his room and locked the door. And after standing leaning against the door for a while,",
   [("door_close", "ލައްޕައިލިއެވެ", -20)])
sh(41, "he sank to his knees. Only then did the tears he had held back begin to pour. Covering his face with both hands, he began to sob.",
   [("sob_breath", "ގިސްލާ", -22)], hum=True)
sh(42, "Shafeeqa sat on the edge of the bed, stroking Laira's head with endless love and tenderness, wiping away the tears that kept falling from her eyes.")
sh(43, "Though Laira lay with her eyes closed, tears kept falling from between her lashes. Haizum quietly opened the door of a room and went in.",
   [("door_open", "ހުޅުވާލައި", -22)])
sh(44, "He sat down on the edge of the bed, resting his elbows on his knees, and pressed his joined hands to his forehead.")
sh(45, "Tears fell from his eyes too, beyond holding back. As his lips trembled, Sana's name escaped his tongue.")
sh(46, "He had come far, far too late. \"Sana...\" he said her name in a voice full of heartbreak.", hum=True)
sh(47, "After tossing and turning in bed, unable to sleep, Saba got up and came out of her room. Asil had just finished drinking water and was putting the cup in the sink.",
   [("cup_clatter", "ސިންކަށް", -22)])
sh(48, "Asil's mother too had switched off the TV and was getting up to go to bed. \"Son, call Lail before you sleep, okay?\" Asil's mother said.")
sh(49, "\"Yes,\" Asil replied. \"Saba? Why are you up instead of sleeping? Do you need something?\" Asil's mother asked.")
sh(50, "Saba shook her head to say no. \"Then go to sleep soon. You have to go to school tomorrow too,\" Mamma said.")
sh(51, "Saba nodded. When Mamma went into her room, Saba looked towards Asil. \"Will you give me the number?\" Saba asked. \"Whose? Lail's?\"")
sh(52, "Asil asked. When Saba nodded, Asil held out his hand. When Saba gave him the phone in her hand, Asil saved Lail's number in it.")
sh(53, "\"Don't say anything too upsetting, okay? He's a boy who gets hurt very easily,\" Asil said.")
sh(54, "Without another word Saba took the phone and hurried into her room. As she paced back and forth in the room,")
sh(55, "Saba thought about what to say. After thinking for a while, she opened the phone and sent a short message to Lail's number.")
sh(56, "Then, eyes on the phone, she sat on the edge of the bed. The message was delivered, but no reply came.")
sh(57, "Still watching the phone, Saba fell back onto the bed. And she looked at Lail's profile photo. \"What a lovely smile.\"",
   [("soft_thud", "ވެއްޓިގަތެވެ", -24)])
sh(58, "Saba murmured softly. Suddenly a message came saying \"Hi\" — Saba jumped, the phone slipped from her hand and fell straight onto her face.",
   [("phone_buzz", "އައުމާއެކު", -18), ("soft_thud", "ވެއްޓުނެވެ", -18)])
sh(59, "She let out a cry of pain and quickly rubbed her lips. Then she got off the bed, half-running to stand in front of the mirror.",
   [("gasp", "ލައްވައިލެވުމާއެކު", -22)])
sh(60, "By then her upper lip was a little swollen. \"That really hurt,\" Saba said, touching her lip again.")
sh(61, "Then she walked out quickly and came back pressing an ice pack to her lip. Sitting cross-legged on the bed,",
   [("footsteps_pavement", "ހިނގުމެއްގައި", -24)])
sh(62, "she picked up the phone and saw that two more messages had come. Her eyes widened and she eagerly began to read them. \"Don't understand a lesson?\"")
sh(63, "said the first message. \"Send me the question, I'll explain,\" said the second.")
sh(64, "Saba put the ice pack down on the little table beside her and quickly began typing a reply.",
   [("phone_game_taps", "ޓައިޕްކުރަން", -22)])
sh(65, "\"I just messaged to see how you are — are you okay?\" Saba sent. \"A little better. Thank you so much for checking on me!",
   [("phone_buzz", "ފޮނުވައިލިއެވެ", -22)])
sh(66, "It was very comforting that all the friends came.\" Lail's reply came instantly. \"Okay... just checking. Good night,\" Saba replied.",
   [("phone_buzz", "ޖަވާބު", -22)])
sh(67, "\"Thanks, good night.\" The conversation ended with that short message from the other end. After putting the phone down, Saba")
sh(68, "picked up the ice pack and pressed it to her sore mouth. But her whole attention was fixed on Lail's profile photo.")
sh(69, "As she sat gazing at it, the photo suddenly changed and the whole screen sank into black darkness.")
sh(70, "Saba's brows knitted together and a feeling hard to put into words came over her heart. \"Hmm...\" Saba let out a sound with a deep breath.",
   [("sigh", "ނޭވާއަކާއެކު", -20)])
sh(71, "The painful moment she had endured five months ago had today come into Lail's life as well.")
sh(72, "The pain left in her heart when her beloved father said farewell to this temporary world was still fresh.")
sh(73, "That day, when she wept with a heart-breaking cry, the only one there to comfort her and stroke her back was her mother.",
   [("sob_breath", "ރޮއި", -26)], hum=True)
sh(74, "No relative and no friend shared that loneliness. But today there are so many people around Lail.")
sh(75, "Crowds of well-wishers and family, and close friends besides. What people say is so very true.")
sh(76, "Few will visit a poor man's hut, for all that is seen in it is the light of a dim oil lamp. But,")
sh(77, "the great mansions of the rich are visited by many friends and relatives, for in those homes bright glittering lamps are lit,")
sh(78, "and they are surrounded by costly crystal. With a despairing smile Saba put the ice pack aside,")
sh(79, "lay down on the bed and hugged the pillow. A week passed, and still Lail could not go to school. But,")
sh(80, "Asil kept sending Lail every day's lessons with great care.")
sh(81, "Haizum too stayed home instead of going to the office, because of how low Laira's state of mind had fallen.")
sh(82, "Haizum knew well that the children having seen their beloved mother's passing with their own eyes was not a sight easily erased from memory.")
sh(83, "That is why, to look after the children in this hard time, Shafeeqa too was staying in that house.")
sh(84, "\"The way TV programmes and the news keep describing the incident, the memories of that terrible night will never be erased from the children's hearts.\"")
sh(85, "Haizum said in a pained voice, switching off the TV. \"My son! Switching off the TV won't solve anything.")
sh(86, "The whole world lies open in those children's hands. What is there they can't see on those phones? What news can't they find?")
sh(87, "Until the investigation into that dangerous accident that night is over and justice is done, those children's hearts won't find peace. Nor will your own heart, my son.")
sh(88, "Tell Mamma — will you ever be able to forget losing Sana?\" Shafeeqa asked with feeling. With these words of Shafeeqa's,")
sh(89, "Haizum felt as if that tragic incident had just happened before his eyes. He covered his face with both hands and sank back into the sofa.",
   hum=True)
sh(90, "And he wiped his tear-filled eyes. Just then the doorbell rang and Shafeeqa went and opened the door. \"Haizum asked me to come.\"",
   [("doorbell_buzz", "ބެލް", -18), ("door_open", "ހުޅުވައިލިއެވެ", -22)])
sh(91, "At the door stood a lawyer in a suit and trousers, holding a file in his hand. \"Welcome! Please come in.\"")
sh(92, "Shafeeqa invited him in respectfully. As the man came in, Haizum got up from the sofa, greeted him with salaam and asked him to sit.")
sh(93, "The lawyer sat in an armchair to one side. \"I want justice for my wife's death.")
sh(94, "Even if it wasn't intentional, it happened because of extreme negligence,\" Haizum said, looking at the lawyer with tear-filled eyes.")
sh(95, "\"Don't worry, God willing, justice will be done. The police have now arrested the man who was riding the motorcycle and taken his statement as well.\"")
sh(96, "the lawyer said reassuringly. He opened the file, took out a sheet and handed it to Haizum. Haizum took the sheet,",
   [("paper_shuffle", "ފައިލު", -22)])
sh(97, "and read through what was written on it carefully. A little later Shafeeqa came with two cups of coffee on a tray.")
sh(98, "She set the two cups in front of Haizum and the man, then took the empty tray back to the kitchen.",
   [("cup_clatter", "ބެހެއްޓުމަށްފަހު", -22)])
sh(99, "While Shafeeqa was busy in the kitchen, the doorbell rang. When she went and opened the door, Lail's friends were standing there.",
   [("doorbell_buzz", "ބެލް", -18), ("door_open", "ހުޅުވައިލިއިރު", -22)])
sh(100, "Shafeeqa welcomed the youngsters with a smile. \"It's so good that you've come. Come in! Lail still hasn't eaten anything, he's in his room.\"")
sh(101, "Shafeeqa said. At her word they all went in and opened the door of Lail's room. Lail was lying on the sofa.",
   [("door_open", "ހުޅުވައިލިއެވެ", -22)])
sh(102, "When Asil came in and waited, Lail got up and sat. Asil and Shahid sat on the sofa, while Sadhee sat on a chair by the study desk.")
sh(103, "Saba came into the room hesitantly and cast her eyes over the surroundings. Compared with ordinary rooms in Malé, the room was spacious.")
sh(104, "There was a big bed in the middle, small cabinets on both sides of the bed, and a large wardrobe as wide as the wall.")
sh(105, "The two-seater sofa visible as you enter, the study desk in front of it, and the small balcony seen to the right of the bed added to the room's perfection.")
sh(106, "\"Don't be shy, sit down.\" Sadhee took Saba by the hand and sat her on a chair. At Sadhee's voice Lail raised his head and looked up — at the same moment Saba looked too.")
sh(107, "As their eyes met, a shy smile came over Saba's lips.", hum=True)
sh(108, "Lail answered with a gentle smile too. \"Dear, shall Maama order a pizza?\" Shafeeqa asked, opening the door.",
   [("door_open", "ހުޅުވައިލަމުން", -24)])
sh(109, "\"Really? What should we get?\" Lail asked. \"Whatever Maama likes,\" Asil said with a smile. \"Dear, you should take all the kids upstairs.")
sh(110, "To relax a bit,\" Shafeeqa suggested. \"We're going, Maama,\" Lail said. And looking at his friends, \"Let's go upstairs!\"")
sh(111, "he said. When Lail stood up, everyone stood. As Asil and Shahid went out chatting, Sadhee joined their conversation and followed behind.")
sh(112, "When Saba lingered, Lail came behind her. Though they looked at each other, not a word passed between them,")
sh(113, "and the two left the room together. Climbing the stairs by the kitchen, they entered a sitting room as elegantly done as the floor below.",
   [("footsteps_pavement", "އެރުމުން", -24)])
sh(114, "But the special difference of the upper floor was the swimming pool on the terrace outside. Saba looked around.")
sh(115, "This was truly no ordinary apartment. Everyone went out to the terrace and settled in chairs. Sadhee went and stretched out on a beach lounger by the pool.")
sh(116, "\"Saba, come, it's so comfy.\" When Sadhee called, Saba went and sat on the lounger next to her.")
sh(117, "Lail went and leaned against the balcony railing and looked at Saba. Asil and Shahid, forgetting why they had even come, were caught up in a funny conversation.")
sh(118, "\"Why are you sitting so strangely? Something wrong?\" Sadhee asked Saba in a whisper. \"No — should we come to a new place and have fun?")
sh(119, "We only came because Lail's Maama asked, to see if he'd eat something. Not to have fun,\" Saba said, barely audible. \"That's why I'm saying,")
sh(120, "go talk to Lail and cheer him up,\" Sadhee said in a joking tone. \"What would I talk about? He's been with you lot since nursery.")
sh(121, "It's you lot who'd have things to talk about,\" Saba said, letting out a deep breath. Sadhee shook her head, got up and went to talk with Lail.",
   [("sigh", "ނޭވާއެއް", -22)])
sh(122, "Even as he talked with Sadhee, Lail's gaze kept resting on Saba every now and then. To pass the time, Saba picked up her phone and began browsing Instagram.")
sh(123, "At this point Asil and Shahid joined Sadhee's conversation too. As the debate between them grew heated,")
sh(124, "Lail quietly drew away from them. And he came and sat on the lounger right next to where Saba sat. Saba too switched off her phone screen and looked at Lail.")
sh(125, "At that moment a silent but deeply meaningful smile passed between the two.", hum=True)
SHOTS = S

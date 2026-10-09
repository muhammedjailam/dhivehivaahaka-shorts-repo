"""Beat/shot plan for Mamma episode 350 (used by plan_beats.py)."""

LOC = {
    "mosque_porch_day": "the home island's old mosque: white-washed coral-stone walls, a wide covered front porch with low white wall-benches along its edge, wooden doors, palms; close beside it the island cemetery, a sandy yard of plain white-washed coral headstones with no writing under frangipani trees, enclosed by a low white wall",
    "main_road_day": "the island's wide white sandy main road (bodumagu) lined with tall coconut palms, breadfruit trees and low coral-stone walls with simple island houses behind them, the old white mosque small in the far distance",
    "zubair_yard_day": "the front of Zubair's old coral-stone island house: a corrugated-iron roof, a weathered wooden front door, a raised wooden porch platform (ashi) along the front wall, a sandy yard with a wooden joali seat and a low coral-stone boundary wall with a gap for a gate",
    "zubair_yard_night": "the sandy yard of Zubair's old coral-stone island house at night: an outdoor kitchen area under a corrugated-iron lean-to with a low wooden table set with simple plates, a covered pot and a tray of rice, a bare bulb hanging above, the weathered wooden front door of the house open behind, a low coral-stone wall and palms in the dark",
    "thahmeena_door_night": "Thahmeena's neat island house at night, two or three houses down the sandy lane: a lit open front doorway with warm yellow light spilling onto a small porch, a white-washed wall, a streetlamp on the lane outside, inside a glimpse of a bright room where guests sit around a table with dishes",
    "island_lane_night": "a white sandy island lane at night between low coral-stone walls and palms, a single streetlamp on a wooden pole casting a warm amber pool of light on the sand, the lit doorway of Thahmeena's neat house at one side, simple island houses with dark doorways further along",
    "guest_room_night": "a small guest bedroom in an island house at night: white-washed walls, a wooden bed with a plain white sheet, a wooden window with its shutter half open to the dark palms, a small bedside table with a dim lamp",
    "thahmeena_porch_day": "the front porch of Thahmeena's neat island house in the morning: a wooden joali seat and a low table with two cups of tea, a white-washed wall, potted plants, the sunny sandy lane and palms beyond",
    "male_gate_day": "the front of Azeeza's comfortable older two-storey townhouse in Malé: a pastel-cream facade with balconies, an open metal gate in a white wall, a tiled front yard with potted plants and a parked motorbike, a front porch (askani) with a wooden joali seat, the narrow Malé street with tall pastel buildings behind",
    "male_hall_day": "the bright hall (fendaa) of Azeeza's Malé townhouse: cream walls, framed pictures of flowers, a wooden dining table with chairs, a doorway to the inner rooms, sunlight through a window with light curtains, tiled floor",
    "male_porch_day": "the front porch (askani) of Azeeza's Malé townhouse in the afternoon: a wooden joali seat, a small wooden side table, potted plants, the tiled front yard and the white gate beyond",
    "male_porch_dusk": "the front porch and doorway of Azeeza's Malé townhouse at dusk: a wooden joali seat on the porch, a warm lamp above the open front door showing the bright hall inside, the tiled front yard with potted plants and the white gate, tall pastel Malé buildings behind under a deep-blue evening sky",
    "male_kitchen_night": "the kitchen of Azeeza's Malé townhouse at night: a tall white fridge, light wooden cabinets, a small square dining table with two chairs, a wall-mounted telephone with a coiled cord beside the doorway, warm ceiling light, tiled floor",
    "shahula_room_night": "Shahula's small neat room in the Malé townhouse at night: a single bed with a plain cover, a little wooden cupboard, a small desk with schoolbooks, a wooden door, a warm bedside lamp",
    "male_yard_night": "the tiled front yard of Azeeza's Malé townhouse at night: the open white gate in the front wall, potted plants, the porch with its joali seat lit by a warm porch lamp, the narrow Malé street outside lit by warm streetlights, tall pastel buildings",
}
MOOD = {
    "mosque_porch_day": "afternoon at the time of Asr, soft hazy tropical light, long gentle shadows, quiet and grieving, melancholic",
    "main_road_day": "late afternoon, soft hazy golden tropical light filtering through the palms, quiet and tender",
    "zubair_yard_day": "late afternoon, soft hazy tropical light and dappled palm shade, still and heavy",
    "zubair_yard_night": "night, deep blue-black darkness around a single warm amber bulb, worried and tense",
    "thahmeena_door_night": "night, warm amber light from the open doorway against the deep blue-black lane, anxious",
    "island_lane_night": "night, deep blue-black shadows and a warm amber streetlamp pool, palm silhouettes, anxious and sad",
    "guest_room_night": "late night, dim warm lamp light and deep blue shadows, sleepless and troubled",
    "thahmeena_porch_day": "morning, soft hazy tropical light, calm, thoughtful and gently hopeful",
    "male_gate_day": "bright soft morning light in Malé, warm homely colours, a gentle new beginning",
    "male_hall_day": "warm homely daylight, golden and safe, years later",
    "male_porch_day": "warm homely afternoon light with soft shade, light-hearted",
    "male_porch_dusk": "early evening at dusk, warm homely lamplight against a deep-blue sky",
    "male_kitchen_night": "evening, warm homely kitchen light, quiet and a little awkward",
    "shahula_room_night": "night, a single warm lamp, soft shadows, uneasy and pensive",
    "male_yard_night": "night, warm amber porch lamp and streetlights against the deep blue-black sky, a motorbike headlight glow",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear arm's-length gap between them, not touching"
SC = "12-year-old Shahula in her faded pink long-sleeved ankle-length dress and white headscarf fully covering her hair and neck"
SHAWL = "with a thin faded cotton shawl wrapped around her shoulders"
SY = ("teenage Shahula (reference used for her face only; wearing a loose long-sleeved ankle-length lavender home dress and "
      "a white hijab fully covering her hair and neck, NOT the white school uniform)")
AM = ("Aamir (reference used for his face only; wearing a light-blue long-sleeved shirt and dark trousers, NOT the white shirt)")
AZ_ILL = ("Azeeza (reference used for her face and gold-rimmed glasses only; wearing a loose cream long-sleeved ankle-length "
          "house dress and a cream hijab, NOT the emerald abaya)")
THA = "Thahmeena, a Maldivian woman of about 40 in a yellow long-sleeved ankle-length libaas and a white headscarf fully covering her hair and neck"

BEATS = [
    # ---------------- ISLAND, AFTERNOON (Asr)
    dict(to=4, reason="episode opening: Shahula alone on the mosque porch wall at Asr, staring at the cemetery, wiping tears",
         chars=["shahula_child"], loc="mosque_porch_day",
         visual=f"{SC} {SHAWL}, sitting alone on the low white wall-bench at the edge of the mosque's covered porch, small and "
                f"still, wiping a tear from her cheek with the back of her hand, gazing sadly across at the low white cemetery wall "
                f"and the plain blank white headstones under the frangipani trees; her face shown with quiet dignity",
         camera=f"medium wide shot from the side, eye level, {LOW} (the sandy ground and the porch floor in soft shade)",
         amb="island_day", sens="death", safe="grief shown with dignity: the girl sitting on the mosque wall looking at the walled cemetery; no grave scene"),
    dict(to=6, reason="character enters: old Moosafulhu, leaving the mosque after prayer, stops beside her and speaks gently",
         chars=["moosafulhu", "shahula_child"], loc="mosque_porch_day",
         visual=f"old Moosafulhu standing beside the porch wall-bench, bending slightly towards {SC} {SHAWL}, speaking to her "
                f"gently with a kind, sorrowful face; she looks up at him with wet eyes; a few men in white kurtas and sarongs "
                f"leaving the mosque doors in the background and walking away",
         camera=f"medium shot, eye level, {LOW} (sandy ground in soft shade)", amb="village_day"),
    dict(to=8, reason="scene change: he walks her home along the main road; her tears keep falling",
         chars=["moosafulhu", "shahula_child"], loc="main_road_day",
         visual=f"old Moosafulhu walking slowly along the wide white sandy main road beside {SC} {SHAWL}, the two seen from the "
                f"front walking side by side towards the camera, he looks down at her with kindness, she walks with head bowed, "
                f"a tear on her cheek; palms and coral-stone walls on both sides",
         camera=f"medium wide shot, eye level, {LOW} (white sand of the road)", amb="village_day"),
    dict(to=11, reason="scene change: at Zubair's house; Moosafulhu calls softly, Shahula slips inside, Zubair asleep on the porch",
         chars=["moosafulhu", "zubair", "shahula_child"], loc="zubair_yard_day",
         visual=f"old Moosafulhu standing at the open front door of the old coral-stone house, leaning his head in to call softly; "
                f"{SC} seen from behind slipping in through the doorway; Zubair asleep, lying on his side on the raised wooden "
                f"porch platform along the front wall, his cap over his eyes, an arm under his head",
         camera=f"medium wide shot, eye level, {LOW} (the sandy yard)", amb="island_house_day"),
    # ---------------- NIGHT: SHAHULA IS MISSING
    dict(to=15, reason="time jump to night and action change: dinner; Faathanikey finds the room empty and hurries out, Zubair rises",
         chars=["faathanikey", "zubair"], loc="zubair_yard_night",
         visual="Faathanikey hurrying across the dark sandy yard towards the lane with a worried, frightened face, one hand at her "
                "headscarf; behind her Zubair half-rising from the low wooden dinner table under the hanging bulb, frowning in "
                "puzzlement, plates of rice and curry on the table",
         camera=f"medium wide shot, eye level, {LOW} (dark sand of the yard)", amb="island_house_night", transition="black"),
    dict(to=19, reason="scene change: at Thahmeena's lit doorway Faathanikey asks for Shahula; her voice breaks into tears",
         chars=["faathanikey"], loc="thahmeena_door_night",
         visual=f"Faathanikey standing on the small porch at the lit open doorway, asking anxiously, her eyes filling with tears; "
                f"{THA} standing in the doorway facing her with a worried face, one hand on the door; behind her a few guests "
                f"seated around a table in soft focus",
         camera=f"medium shot from the side, eye level, {LOW} (the porch step in warm light)", amb="village_night"),
    dict(to=23, reason="character enters: Zubair's voice behind her; she turns, he strides off towards the main road and she hurries after",
         chars=["zubair", "faathanikey"], loc="island_lane_night",
         visual="Zubair in the sandy lane under the streetlamp, turning to stride off towards the main road with a stern, "
                "irritated face; Faathanikey just behind him turned towards him, her face full of worry and fear, about to "
                "hurry after him",
         camera=f"medium wide shot, eye level, {LOW} (lamp-lit sand of the lane)", amb="night_lane"),
    dict(to=27, reason="character enters: Azeeza, a Malé guest, asks if a child is lost; Faathanikey pleads with Zubair; Thahmeena explains",
         chars=["azeeza", "faathanikey", "zubair"], loc="island_lane_night",
         visual=f"in the lane under the streetlamp Faathanikey at her husband Zubair's side, her hand on his shirt sleeve, pleading "
                f"with him, Zubair stern and impatient; a few steps away at the lit doorway Azeeza, a dignified lady in her emerald "
                f"abaya, cream hijab and gold-rimmed glasses, stands watching with concern beside {THA}",
         camera=f"wide shot, eye level, {LOW} (lamp-lit sand)", amb="village_night",
         sens="other", safe="a married couple only: her hand on her husband's sleeve as she pleads; no anger shown towards anyone"),
    dict(to=30, reason="emotional turning point: a girl walks past under the streetlamp and her face of utter despair is seen clearly",
         chars=["shahula_child", "azeeza"], loc="island_lane_night",
         visual=f"{SC} walking alone through the warm pool of streetlamp light, her small face clearly lit, full of utter despair "
                f"and hopelessness, eyes wet and lost; in the soft-focus foreground at the edge of the frame Azeeza in her emerald "
                f"abaya seen from behind, watching her pass",
         camera=f"medium shot, eye level, {LOW} (lamp-lit sand)", amb="night_lane"),
    dict(to=32, reason="character enters: 15-year-old Aamir stops by his mother; 'Who is that girl?'; she sends him in and follows the girl",
         chars=["azeeza", "aamir_teen"], loc="island_lane_night",
         visual="Azeeza standing in the lane under the streetlamp looking away down the lane with a worried face, her 15-year-old "
                "son Aamir standing beside her, answering politely with a shrug; Thahmeena's lit doorway behind them",
         camera=f"medium shot, eye level, {LOW} (lamp-lit sand)", amb="night_lane"),
    dict(to=36, reason="action/character change: the girl goes into a house two doors away; Faathanikey returns crying and talks with Azeeza",
         chars=["faathanikey", "azeeza"], loc="island_lane_night",
         visual="Faathanikey and Azeeza standing in the lamp-lit lane facing each other, Faathanikey in tears, shaking her head, "
                "one hand pressed to her chest; Azeeza listening with deep concern; in the background, two houses down, a small "
                "figure's shadow just disappearing through a dark doorway",
         camera=f"medium two-shot, eye level, {LOW} (lamp-lit sand)", amb="night_lane"),
    dict(to=39, reason="scene/time change: that night Azeeza cannot sleep thinking of the girl, and sits up with a start",
         chars=["azeeza"], loc="guest_room_night",
         visual="Azeeza in her emerald abaya and cream hijab sitting up suddenly on the edge of the guest bed in the dim lamp-lit "
                "room, wide awake, her gold-rimmed glasses on the bedside table beside the lamp, staring towards the dark window "
                "with a troubled, anxious face",
         camera=f"medium shot, eye level, {LOW} (the plain white sheet and floor in soft shadow)", amb="island_house_night"),
    # ---------------- A WEEK LATER
    dict(to=40, reason="time jump (a week later): Shahula still sits silently by the mosque staring at the cemetery",
         reuse="beat_001", chars=["shahula_child"], loc="mosque_porch_day", visual="reuse of beat_001",
         amb="island_day", transition="black"),
    dict(to=42, reason="character/scene change: Azeeza asks Zubair to let her take Shahula to Malé; he asks for time",
         chars=["azeeza", "zubair"], loc="zubair_yard_day",
         visual=f"Azeeza in her emerald abaya, cream hijab and gold-rimmed glasses standing in Zubair's sandy yard, speaking "
                f"earnestly with her hands folded; Zubair standing by the wooden joali seat with his arms folded, looking at the "
                f"ground in thought, a grieving, guarded face; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (the sandy yard)", amb="island_house_day"),
    dict(to=47, reason="scene change: Azeeza and Thahmeena talk on Thahmeena's porch about Shahula and Zubair; Azeeza smiles",
         chars=["azeeza"], loc="thahmeena_porch_day",
         visual=f"Azeeza sitting on the wooden joali seat on the porch with a cup of tea, speaking thoughtfully, then smiling "
                f"softly; {THA} sitting beside her on a chair, leaning in and talking; two cups of tea on the low table",
         camera=f"medium shot, eye level, {LOW} (the porch floor and the low table)", amb="island_house_day"),
    # ---------------- MALÉ
    dict(to=49, reason="scene change: Azeeza brings Shahula to her house in Malé, a safe and happy home",
         chars=["azeeza", "shahula_child"], loc="male_gate_day",
         visual=f"Azeeza in her emerald abaya leading {SC} in through the open white gate into the tiled front yard of the "
                f"townhouse, Shahula holding a small cloth bag in both hands and looking up at the big house with shy wonder, "
                f"Azeeza smiling warmly down at her",
         camera=f"medium wide shot, eye level, {LOW} (the tiled yard)", amb="city_day", transition="black"),
    dict(to=52, reason="time jump (years pass): teenage Shahula devoted to her studies; Aamir secretly loves her",
         chars=["shahula_young", "aamir"], loc="male_hall_day",
         visual=f"{SY} sitting at the wooden dining table, absorbed in her schoolbooks and notebooks with blank pages, a pen in "
                f"her hand; across the hall Aamir (white long-sleeved shirt, dark trousers) leaning in the doorway, secretly "
                f"watching her with a soft, hidden longing; the whole hall between them",
         camera=f"medium wide shot, eye level, {LOW} (the table top with books)", amb="home_day", transition="black"),
    dict(to=56, reason="action change: Aamir the playboy on endless phone calls and letters; Shahula even writes some replies",
         chars=["aamir", "shahula_young"], loc="male_porch_day",
         visual=f"Aamir (white long-sleeved shirt, dark trousers) lounging on the porch joali seat, laughing charmingly into a "
                f"mobile phone held to his ear, a loose pile of plain blank envelopes beside him; {SY} sitting at the small side "
                f"table a few steps away, writing on a blank sheet of paper with a weary, resigned little face; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (the porch floor)", amb="home_day",
         sens="intimacy", safe="the playboy life shown only as a phone call and a pile of blank envelopes; no girlfriends shown"),
    dict(to=58, reason="time/action change: Aamir lands a job at his first interview; Azeeza is overjoyed",
         chars=["aamir", "azeeza"], loc="male_hall_day",
         visual=f"{AM} standing in the bright hall holding a plain blank folder, smiling proudly; Azeeza in her emerald abaya, "
                f"cream hijab and gold-rimmed glasses facing him, beaming with joy, her hands pressed together at her chest",
         camera=f"medium shot, eye level, {LOW} (tiled floor)", amb="home_day"),
    dict(to=61, reason="scene/time change: evening at home; Shahula calls them to dinner; Azeeza goes to pray, Aamir comes in",
         chars=["shahula_young", "azeeza", "aamir"], loc="male_porch_dusk",
         visual=f"{SY} standing in the open lit front doorway calling out with a gentle smile; Azeeza in her emerald abaya sitting "
                f"on the wooden joali on the porch, turning to her; {AM} walking up from the white gate across the tiled yard; "
                f"everyone apart, nobody touching",
         camera=f"medium wide shot, eye level, {LOW} (the tiled yard)", amb="home_night"),
    dict(to=64, reason="scene change: the kitchen; she takes water from the fridge, he asks for lukewarm water while serving rice",
         chars=["shahula_young", "aamir"], loc="male_kitchen_night",
         visual=f"{SY} standing by the open fridge holding a water bottle, turned towards the table; {AM} seated at the small "
                f"kitchen table serving rice onto his plate, looking up at her and speaking; a cup of water on the table; {GAP}; her dress is a plain solid lavender colour all over with no belt and no sash (NOT white, NOT a school uniform);",
         camera=f"medium wide shot, eye level, {LOW} (the table top and floor)", amb="home_night",
         sens="intimacy", safe="unmarried teen girl and young man: at a distance across the kitchen, no touching"),
    dict(to=67, reason="framing change: he calls her name; she stops, eyes lowered, pale and uneasy; he asks her to stay a moment",
         chars=["shahula_young", "aamir"], loc="male_kitchen_night",
         visual=f"{SY} stopped near the kitchen doorway, half turned back, eyes lowered, her face pale and uneasy; {AM} seated at "
                f"the table looking up at her with a soft searching gaze, a cup of warm water in front of him; {GAP}",
         camera=f"medium two-shot, eye level, {LOW} (the table top)", amb="home_night"),
    dict(to=70, reason="action change: the wall telephone rings; she answers, then hands it over and leaves",
         chars=["shahula_young", "aamir"], loc="male_kitchen_night",
         visual=f"{SY} standing at the wall-mounted telephone holding the receiver to her ear, looking back over her shoulder "
                f"at Aamir with a calm, closed face; {AM} rising from his chair at the table, surprised; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (tiled floor)", amb="home_night"),
    dict(to=74, reason="focus change: Aamir alone at the phone, annoyed, hangs up on an old flame; only Shahula is in his heart",
         chars=["aamir"], loc="male_kitchen_night",
         visual=f"{AM} alone by the wall-mounted telephone, placing the receiver back on its hook with an annoyed frown, then "
                f"gazing towards the empty kitchen doorway where Shahula left, a deep, thoughtful longing in his eyes",
         camera=f"medium close-up, eye level, {LOW} (soft-focus kitchen behind)", amb="home_night"),
    dict(to=76, reason="scene change: in her room after prayer Shahula puts the folded prayer mat on the cupboard, uneasy; a knock",
         chars=["shahula_young"], loc="shahula_room_night",
         visual=f"{SY} placing a neatly folded prayer mat on top of the little wooden cupboard, then pausing, sitting on the edge "
                f"of her bed lost in thought with an uneasy, fearful face, turning slightly towards the closed door",
         camera=f"medium shot, eye level, {LOW} (the floor in soft lamplight)", amb="room_night",
         sens="other", safe="prayer itself not shown, only the folded mat being put away"),
    dict(to=78, reason="character enters: she opens the door to Azeeza, in great pain in her leg, asking her to fetch Fathuma",
         chars=["azeeza", "shahula_young"], loc="shahula_room_night",
         visual=f"{SY} holding her room door open with an alarmed face; in the doorway {AZ_ILL}, leaning one hand on the door "
                f"frame, the other hand on her knee, her face tight with pain, asking for help",
         camera=f"medium shot, eye level, {LOW} (the floor at the doorway)", amb="room_night"),
    # ---------------- FRONT YARD AT NIGHT
    dict(to=80, reason="scene change: Shahula hurries out; Aamir arrives at the gate on his motorbike with Ayya and calls 'Shahoo'",
         chars=["aamir", "ayya", "shahula_young"], loc="male_yard_night",
         visual=f"{SY} hurrying across the tiled front yard towards the gate; at the open gate {AM} sitting astride his motorbike "
                f"with its headlight glowing, calling to her; Ayya standing beside the motorbike; {GAP} and more between her and the men",
         camera=f"medium wide shot, eye level, {LOW} (the tiled yard)", amb="street_night"),
    dict(to=82, reason="emotional turning point: she stops, astonished — he has never called her 'Shahoo' before",
         chars=["shahula_young"], loc="male_yard_night",
         visual=f"close-up of {SY}, stopped in the yard and turned back, her large dark eyes wide with astonishment and a faint "
                f"shy confusion, the warm porch lamp and a soft headlight glow on her face",
         camera=f"close-up, eye level, {LOW} (soft-focus dark yard)", amb="street_night"),
    dict(to=84, reason="focus change: Aamir on his bike offers to take her; tells Ayya to wait",
         chars=["aamir", "ayya"], loc="male_yard_night",
         visual=f"{AM} sitting on his motorbike at the open gate, leaning forward with a charming, inviting smile, gesturing "
                f"towards the empty back seat; Ayya standing beside the bike with his hands in his pockets, grinning",
         camera=f"medium shot, eye level, {LOW} (the street paving)", amb="street_night"),
    dict(to=88, reason="action change: she shyly refuses at the gate; Ayya laughs; Aamir looks deep into her face",
         chars=["shahula_young", "aamir", "ayya"], loc="male_yard_night",
         visual=f"{SY} standing just inside the gate, a step back from the motorbike, eyes lowered shyly, hands clasped in front "
                f"of her; {AM} on the motorbike looking deeply at her face with a teasing smile; Ayya behind the bike laughing "
                f"heartily; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (the tiled yard)", amb="street_night",
         sens="intimacy", safe="she refuses the ride: standing at the gate at a distance, Aamir on the bike, no touching"),
    dict(to=90, reason="action change: she hurries back inside; Aamir is left speechless",
         chars=["shahula_young", "aamir"], loc="male_yard_night",
         visual=f"{SY} seen from behind walking quickly up to the lit front door of the house; in the foreground at the gate "
                f"{AM} on his motorbike watching her go, speechless; {GAP}; her dress is a plain solid lavender colour all over with no belt and no sash (NOT white, NOT a school uniform);",
         camera=f"medium wide shot from behind Aamir, eye level, {LOW} (the tiled yard)", amb="street_night"),
    dict(to=92, reason="action change: Ayya climbs on the back of the bike and teases Aamir about his hopeless hope",
         chars=["ayya", "aamir"], loc="male_yard_night",
         visual=f"Ayya sitting on the back of the motorbike behind {AM}, grinning and teasing; Aamir in front looking back over "
                f"his shoulder at the lit house; the white gate and the warm streetlights",
         camera=f"medium shot, eye level, {LOW} (the street paving)", amb="street_night"),
    dict(to=94, reason="framing change: Aamir's sly smile — every obstacle is gone; he will have her",
         chars=["aamir"], loc="male_yard_night",
         visual=f"close-up of {AM} on the motorbike at night, a sly, knowing half-smile, his dark eyes intense and determined, "
                f"warm streetlight on one side of his face, the lit house soft-focus behind",
         camera=f"close-up, eye level, {LOW} (soft-focus dark street)", amb="street_night"),
    dict(to=96, reason="back to the two on the bike: Ayya stunned, questioning him", reuse="beat_032",
         chars=["ayya", "aamir"], loc="male_yard_night", visual="reuse of beat_032", amb="street_night"),
    dict(to=99, reason="back to Aamir's determined face: he will wait for her last year at school (cliffhanger)", reuse="beat_033",
         chars=["aamir"], loc="male_yard_night", visual="reuse of beat_033", amb="street_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Even as the call to the Asr prayer was heard, Shahula sat at the foot of the mosque wall, staring towards the cemetery.")
sh(2, "Straightening the thin cloth wrapped around her body, she wiped away the tears running down her cheeks.",
   [("cloth_rustle", "ރަނގަޅުކޮށްލަމުން", -24)])
sh(3, "Her grief-filled heart longed only to go to her beloved mother. In this whole big world it seemed there was no one left to care for her.",
   hum=True)
sh(4, "The harsh, venomous words her eldest uncle had spoken that morning still echoed in her ears.")
sh(5, "When the prayer was over and the people coming out of the mosque set off for their homes, Moosafulhu caught sight of Shahula and stopped beside her. \"Little one!",
   [("footsteps_sand", "ފޭބި", -24)])
sh(6, "If your mother saw you sitting here like this, how it would hurt her heart! Come, child, let's go home. Faathanikey will be looking for you by now.\"")
sh(7, "Moosafulhu said softly and gently, kindly taking Shahula's hand and helping her up. Holding Shahula's hand, Moosafulhu set off along the main road",
   [("footsteps_sand", "ހިނގައިގަތީ", -22)])
sh(8, "to take her home. Even then there was no stopping the tears falling from Shahula's eyes. \"Faathanikey! Faathanikey!\"")
sh(9, "Moosafulhu called softly, putting his head in at the door. Meanwhile Shahula went inside and into her room.")
sh(10, "Seeing Zubair asleep on the porch bench outside the house, Moosafulhu did not dare call out loudly.")
sh(11, "Hearing no sign of anyone else inside the house, Moosafulhu turned and walked back towards his own home.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)])
sh(12, "Zubair sat down at the table to do justice to the evening meal. Faathanikey, having finished preparing the food,",
   [("cup_clatter", "ތައްޔާރުކޮށް", -24)])
sh(13, "walked towards the room to call Shahula. But not long after going into the room,")
sh(14, "Faathanikey came out, worried, and hurried straight out of the house. Not knowing what had happened, puzzled,",
   [("footsteps_sand", "ނުކުމެގެން", -20)])
sh(15, "Zubair too got up from the table and hurried after Faathanikey. Faathanikey went to the house of Leeza, Shahula's closest friend, who studies in the same class.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(16, "Standing at the door, Faathanikey called out a salaam, and it was Leeza's mother Thahmeena who answered. \"Did Shahula come to this house?\"")
sh(17, "Faathanikey asked in a voice full of anxiety. \"No! What happened?\" Thahmeena asked, worried too.")
sh(18, "It was a time when Thahmeena was extremely busy hosting some people visiting from Malé. \"Shahula isn't at home.")
sh(19, "She has a very high fever...\" Faathanikey's voice broke and tears fell from her eyes. \"What misery is this now?\"",
   [("sob_breath", "ބެދި", -22)])
sh(20, "came Zubair's voice from behind. When Faathanikey turned at the voice, her face showed the deepest worry.")
sh(21, "Shahula had heard the harsh words Zubair spoke that morning. Faathanikey could feel what those words would do to that innocent heart.")
sh(22, "She too had endured that kind of pain and harshness. Having said that, Zubair set off towards the main road to look for Shahula.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(23, "Faathanikey hurried after him, afraid that the anger in Zubair's heart would be taken out on that poor child.",
   [("footsteps_sand", "އަވަސްއަވަހަށް", -22)])
sh(24, "\"Is a child lost?\" Azeeza asked, coming over and stopping. Azeeza was a respected lady from an influential, wealthy Malé family.")
sh(25, "Faathanikey went along holding her husband's arm, pleading with him, to stop Zubair. Thahmeena and Azeeza stood at the door watching the scene.")
sh(26, "\"Yes. She's Leeza's classmate. Her mother passed away last night,\" Thahmeena said sadly. \"Come, let's go inside.\"")
sh(27, "Thahmeena said. But saying she would come in a moment, Azeeza stepped out onto the street.",
   [("footsteps_sand", "ނުކުތީ", -24)])
sh(28, "Just then she saw her fifteen-year-old son Aamir coming that way. A little ahead of Aamir, from the other side of the road, a girl came walking.",
   [("footsteps_sand", "ހިނގައިފައި", -24)])
sh(29, "As the girl passed Azeeza, the light of the streetlamp on the road showed the girl's face clearly.")
sh(30, "That face showed the utmost despair and hopelessness. Aamir came and stopped beside his mother.", hum=True)
sh(31, "\"Who is that girl?\" Azeeza asked anxiously. \"I don't know either,\" Aamir answered politely. \"Go inside.")
sh(32, "Thahmeena has the food ready.\" When Azeeza said this, Aamir went into the house. But Azeeza walked after the girl.",
   [("footsteps_sand", "ހިނގައިގަތީ", -24)])
sh(33, "The girl went into a house two or three doors away. At that moment Azeeza caught sight of Faathanikey, walking back from the end of the road. \"Has the lost child been found?\"",
   [("door_close", "ގެއަކަށެވެ", -24)])
sh(34, "Azeeza asked in a deeply worried voice. \"No... I don't even know where she went. I've looked near the cemetery too.")
sh(35, "But there's no sign of Shahula. It must be that the innocent child left home after hearing the cruel words Zubair said this morning.\"",
   hum=True)
sh(36, "Faathanikey said, crying. Unable to talk any more, she walked into the house. \"Then was it Shahula who just went into that house?",
   [("sob_breath", "ރޮމުން", -24)])
sh(37, "Where could that girl have been?\" The question rose in Azeeza's heart. Though she lay down to sleep that night, Shahula's sorrowful state kept echoing in Azeeza's mind.")
sh(38, "The things Thahmeena had told her, and what Faathanikey had revealed in tears that night. Thinking of how Zubair would treat that poor child when he came home, Azeeza could not bear it.")
sh(39, "She sat up from the bed with a start. Even after a week had passed, Shahula's grief had not eased in the least.",
   [("gasp", "ފުންމައިގެން", -22)])
sh(40, "The once cheerful girl had become completely silent and withdrawn. Whenever she left the house, she always sat by the mosque, staring towards the cemetery.")
sh(41, "Azeeza could not bear to watch this heartbreaking sight. At last Azeeza asked Zubair to let Shahula go with her to Malé.")
sh(42, "Zubair said he needed some time to think it over. \"Why do you want to take Shahula to Malé? She's an orphan child,\"")
sh(43, "Thahmeena said. \"If that girl is taken away from this place, everything may get better. As long as she sits at the foot of the mosque wall staring at the cemetery,")
sh(44, "that child's health, of mind and of body, will be lost too,\" Azeeza said with a deep sigh.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(45, "\"I don't think Zubair will send the child. She is the only trust his sister left behind.")
sh(46, "These days Zubair is short-tempered because of the grief of Khadheeja's sudden death. Otherwise he is a very kind man too.\"")
sh(47, "Thahmeena revealed. Azeeza only smiled. It seemed she too could feel Zubair's grief and his situation.")
sh(48, "When Azeeza went back to Malé, she took Shahula with her. And in her house she gave Shahula a safe, happy home.")
sh(49, "She put her in a good school and began her education. As the days went by, forgetting the island, Shahula began to grow used to her new life.")
sh(50, "And she gave all her attention to her studies. Azeeza's son Aamir's heart leaned towards Shahula.")
sh(51, "Even in his school days, it was Shahula's name that was carved in the deepest corner of Aamir's heart. But Aamir never let Shahula catch even a hint of those feelings.")
sh(52, "He kept that secret love hidden in his heart. Aamir was a young man with the handsome, youthful looks that easily win girls' hearts.")
sh(53, "In those days he too made use of those looks. Countless sweethearts came into his life,")
sh(54, "and love affairs bloomed freely. While his time went on exchanging phone calls and letters,",
   [("paper_shuffle", "ސިޓީތައް", -24)])
sh(55, "Shahula herself had to write the replies to some of those letters. Yet between Shahula and Aamir there was always a silent,",
   [("pen_scribble", "ލިޔަން", -22)])
sh(56, "hard-to-describe closeness. After finishing his studies, Aamir began looking for a job.")
sh(57, "Though he had the chance to go to two or three interviews, by good luck he did not have to go to many places.")
sh(58, "He got the job at the very first interview. The news brought Azeeza a happiness beyond words. \"Aziththa!")
sh(59, "Dinner is ready,\" Shahula said, coming out to the hall. \"Very good, dear. You go and eat. Mamma is going to pray.")
sh(60, "Have you prayed, son?\" Azeeza asked. \"Yes! I stopped at the mosque on the way home and prayed.\"")
sh(61, "Aamir answered as he walked inside. Azeeza too got up from the joali and walked towards her room. And Shahula went to the kitchen.")
sh(62, "Shahula opened the fridge, took out a water bottle and was about to pour water into a glass. Just then Aamir looked at Shahula and began to speak.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -24), ("pour", "އަޅަން", -20)])
sh(63, "\"Give me a little lukewarm water, please. My stomach is upset; if I drink cold water it might get worse,\" Aamir said, serving rice onto his plate.",
   [("cup_clatter", "އަޅަމުން", -24)])
sh(64, "Shahula put the water bottle back in the fridge, took a cup of lukewarm water and gave it to Aamir. Then, as she started to walk out, Aamir called. \"Shahula.\"",
   [("cup_clatter", "ދިނެވެ", -24)])
sh(65, "Shahula stopped. Since Aamir was not usually someone who talked with her, Shahula always tried as hard as she could to avoid meeting his eyes.")
sh(66, "\"What is it?\" Shahula asked quietly. Aamir clearly noticed the paleness and unease on her face.")
sh(67, "\"Do you need something?\" Shahula asked again. \"No... I just called. Won't you stay here a little while?\" Aamir asked.")
sh(68, "Before their talk could go any further, the phone in the kitchen began to ring. Shahula went and picked it up. \"Hello!\" \"Is Aamir there?\"",
   [("phone_buzz", "ރިންގުވާން", -16)])
sh(69, "It was a girl's voice at the other end. \"Please hold.\" Saying this, Shahula looked at Aamir: \"A call for you.\" Surprised,")
sh(70, "asking whether it was for him, Aamir got up and took the receiver. Handing over the phone, Shahula left the kitchen at once.")
sh(71, "She had no interest at all in hearing what Aamir talked about. As soon as he heard the girl's voice at the other end, Aamir's mood was completely spoiled.")
sh(72, "Without even checking who was calling, he hung up the phone. He had never thought a girl would call suddenly at a time like this.",
   [("soft_thud", "ކަނޑައިލިއެވެ", -24)])
sh(73, "The caller was Zuhdha. Zuhdha was a girl he had befriended back in grade eight. After a brief bloom of romance, that relationship had become the past.")
sh(74, "Though many such girls had come and gone in his life, what was still rooted deep in Aamir's heart was Shahula's name and her lovely face.")
sh(75, "Having finished her prayer, Shahula folded the prayer mat and placed it on the little cupboard. Her face showed that something was troubling her.",
   [("cloth_rustle", "ފަތްޖަހައިލުމަށްފަހު", -22)])
sh(76, "A fear she could not describe was rising in her heart. As she sat sunk in a deep sea of thoughts, there was a knock at her door.",
   [("knock", "ޓަކިޖަހައިލި", -16)])
sh(77, "Shahula hurried to open the door. Standing there was Azeeza. \"Aunty! What's wrong?\" Shahula asked anxiously.",
   [("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(78, "\"My leg is hurting terribly. Please go and bring Fathuma. I can't bear it any more,\" Azeeza begged in a very weak voice. \"All right!")
sh(79, "I'm going.\" Without delay Shahula left the house to fetch Fathuma. That was just when Aamir arrived home with Ali.",
   [("motorbike_pass", "ވަންނަން", -20)])
sh(80, "Seeing Shahula hurrying out so anxiously, Aamir wanted to find out what was going on. \"Shahoo...\" Aamir called.")
sh(81, "Shahula stopped and looked towards Aamir in utter astonishment. For never before had Aamir called her by the name 'Shahoo'.")
sh(82, "Only a very few people, those very close to her, called her by that pet name. \"Where are you off to in such a hurry?\" Aamir asked.")
sh(83, "Shahula briefly explained what was happening and started to go out. \"Shahoo, wait, I'll take you.")
sh(84, "That place is very far from here. Ayya, wait here a bit! I'll drop Shahoo at that house and come back,\" Aamir said.")
sh(85, "Shahula did not know what to say. This time she was being pushed to ride on the back of Aamir's motorbike. But out of shyness, in a hesitant voice, Shahula said:")
sh(86, "\"It would be much better if Aamir went to fetch Fathumaththa. I'll stay with Aunty.\" When Shahula said this, Ayya burst out laughing.")
sh(87, "\"What's the matter? Are you shy to go with me?\" Aamir asked, looking deep into Shahula's face.")
sh(88, "Aamir's question made Shahula even shyer. Never having ridden on a motorbike with Aamir, Shahula was hesitant.")
sh(89, "Even living in the same house, few words had ever passed between them. \"No... perhaps it's best if just one of us goes.\"")
sh(90, "Shahula said hurriedly, turning to go inside. Before Aamir could say anything more, Shahula went into the house.",
   [("footsteps_pavement", "ވަދެގެން", -24)])
sh(91, "Then Ayya came and climbed onto the back of the motorbike. \"I wonder what kind of girl she is!\" escaped from Aamir's lips.",
   [("cloth_rustle", "އެރިއެވެ", -24)])
sh(92, "\"I think this time, Aamir, you're chasing a hopeless hope. Shahula won't fall into that net,\" Ayya teased Aamir with a smirk.")
sh(93, "\"That's what you think! Every obstacle that stood in my way has now been removed,\" Aamir said with a sly smile. \"What are you trying to say?\"")
sh(94, "Ayya asked in surprise. \"I won't let her become anyone else's before she becomes mine. I want her, no matter what.\"")
sh(95, "Aamir's intention seemed clear. Ayya sat staring at Aamir, stunned. \"Aamir...")
sh(96, "Do you know what you're saying? Have you ever even once asked Shahula to be friends?\" Ayya asked.")
sh(97, "\"Asking needs a chance like that too. Whenever I try to say something, she makes some excuse and walks away.")
sh(98, "But this time I won't let that happen. I'm waiting only because she's still studying. This is her last year. I'll wait a little longer.")
sh(99, "I won't rest until I have her,\" Aamir said with complete certainty.",
   [("heartbeat", "ޔަޤީންކަމާއެކު", -24)], hum=True)
SHOTS = S

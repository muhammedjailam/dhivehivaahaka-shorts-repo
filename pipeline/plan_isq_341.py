"""Beat/shot plan for Isq episode 341 (pilot), used by plan_beats.py."""

LOC = {
    "male_bedroom": "Jaleel's dark, luxurious modern master bedroom high above Malé at night: black marble, a single gold lamp turned low, a deep dark leather armchair by floor-to-ceiling windows full of Malé's night lights, a tall glass sliding door with a sheer curtain leading to a balcony over a road",
    "male_balcony": "the balcony of Jaleel's dark, luxurious modern home high above Malé at night: a sleek dark glass-and-metal railing, the tall glass sliding door behind glowing faintly gold from a lamp inside, a road far below lit by streetlights, Malé's dense night skyline of lit apartment towers and city lights, the dark sea beyond the city's edge",
    "runway": "the newly enlarged small airport of a Maldivian local island at night: a long freshly extended runway edged with rows of runway lights, a modern low white terminal building with a lit glass front, a few palms, the dark lagoon beyond",
    "apron": "the apron of the newly enlarged small island airport at night: a small white passenger plane with plain unmarked livery parked with its boarding stairs down, the modern low white terminal with a warmly lit glass front, apron floodlights, palms at the edge",
    "arrivals": "outside the arrivals exit of the new small island airport terminal at night: a covered walkway with warm lights, a few travellers with luggage trolleys, potted palms, white pillars, the dark sky beyond",
    "carpark": "the small car park beside the new island airport terminal at night: a modest silver family car with its boot open under a streetlamp, palms, the warmly lit terminal behind",
    "car": "inside a modest family car driving along a new island road at night, the soft glow of the dashboard, streetlamps, dark palms and coral-stone walls sliding past the windows",
    "gate": "Maura's family house on a Maldivian local island at night: a two-storey house with pale onion-pink walls, a white gate (dhoraashi) in a coral-stone wall with magenta bougainvillea spilling over it, a sandy front yard with potted plants, a garden hose and a wooden joali seat, a warm porch lamp, a sandy lane lit by a streetlamp",
    "house_upstairs": "Maura's family house on a Maldivian local island seen from the sandy lane late at night: the two-storey house with pale onion-pink walls, the coral-stone wall with magenta bougainvillea, and upstairs the glass balcony door with a white curtain opening onto a small balcony with a white railing facing the street",
    "kitchen": "the kitchen and dining area of Maura's family house at night: a long wooden dining table, a slowly turning ceiling fan, warm yellow light, simple wooden kitchen cabinets, a tall fridge, a window onto the dark night",
    "landing": "the upstairs landing of Maura's family house at night: a simple tiled corridor with warm light, the open white door of Maura's bedroom",
    "maura_room": "Maura's newly redecorated bedroom upstairs: pale-green and pale-grey walls, a white queen bed, a white four-door wardrobe, a white dressing table, a white side table, and a glass balcony door with a white curtain opening onto a small balcony with a white railing that faces the street",
}
MOOD = {
    "male_bedroom": "late night, Malé, one dim gold lamp and the cold blue glow of city lights through the windows, deep velvety shadows, heavy and lonely",
    "male_balcony": "late night, Malé, silver moonlight and a sky full of stars, gold and amber city lights below, a cool damp breeze, deep velvety shadows, empty and melancholic",
    "runway": "night, a bright moon lighting up the horizon, deep indigo sky with stars, glittering amber runway lights, a hopeful homecoming",
    "apron": "night, warm floodlights and the golden glow of the terminal under a deep indigo moonlit sky, fresh and wondering",
    "arrivals": "night, warm golden walkway lights against the dark tropical sky, joyful and tender",
    "carpark": "night, a warm amber streetlamp, deep blue shadows, cheerful",
    "car": "night, soft amber dashboard glow and passing streetlamp light on faces, cosy and playful",
    "gate": "night, a warm golden porch lamp and a streetlamp, magenta bougainvillea glowing in the lamplight, joyful and warm",
    "house_upstairs": "late night, silver moonlight and a streetlamp on the pale-pink walls, the upstairs window dark and still, quiet and peaceful",
    "kitchen": "night, warm yellow kitchen light, homely, lively and full of laughter",
    "landing": "night, warm soft hallway light, homely and sleepy",
    "maura_room": "night, soft warm lamplight on pale-green and pale-grey walls and white furniture, calm and delighted",
    "kitchen_3am": "3 a.m., the house dark and silent, only the cold white light from the open fridge on her face, drowsy",
}
LOC["kitchen_3am"] = LOC["kitchen"]
MOOD["maura_room_3am"] = "3 a.m., dark room, faint silver moonlight through the white balcony curtain, drowsy and quiet"
LOC["maura_room_3am"] = LOC["maura_room"]

J = ("Jaleel at home late at night, NOT in his suit: he wears only a soft plain dark-grey long-sleeved lounge shirt with "
     "the top button open and long dark trousers; no suit jacket, no blazer, no tie, no white shirt, no pocket square; "
     "his gold wristwatch")
LILAC = ("Maura, wearing a loose long-sleeved ankle-length soft-lilac home dress and a white hijab fully covering her "
         "hair and neck")
LOW = "faces in the upper two-thirds, a calm uncluttered lower third"

BEATS = [
    # ---------------- MALÉ, NIGHT: Jaleel cannot sleep
    dict(to=3, reason="episode opening: Malé, late night, Jaleel awake and restless in his dark bedroom", chars=["jaleel"],
         loc="male_bedroom",
         visual=f"{J}, sitting alone in the deep dark armchair by the tall windows of the dim bedroom, leaning his head back, eyes closed, one hand pressed to his temple, a deep-thinking, troubled stern face; Malé's lights glitter through the glass behind him; nobody else is in the frame",
         camera=f"medium shot, eye level, slightly from the side, {LOW} (dark marble floor in shadow)", amb="room_night",
         sens="intimacy",
         safe="the married couple's bed and his sleeping wife are not shown; Jaleel sits alone in an armchair, fully dressed"),
    dict(to=5, reason="action change: he slides open the balcony door and steps out into the night breeze", chars=["jaleel"],
         loc="male_balcony",
         visual=f"{J}, stepping out through the tall glass sliding door onto the balcony, seen from behind at three-quarter view, the cool breeze stirring his swept-back hair and the sleeves of his fully buttoned shirt; ahead of him a big bright moon over Malé's glittering skyline",
         camera=f"medium wide shot from behind, slightly low angle, the moon and skyline in the upper two-thirds, {LOW} (the dark balcony floor)",
         amb="balcony_night", transition="xfade", sens="clothing",
         safe="the narration's breeze on his 'exposed body' is shown with Jaleel fully dressed in a long-sleeved shirt and long trousers"),
    dict(to=7, reason="action change: hands on the railing, he stares down at the road (the cigarette is not shown)",
         chars=["jaleel"], loc="male_balcony",
         visual=f"{J}, leaning forward with both empty hands resting on the dark balcony railing, his face in profile, stern and hollow-eyed, staring down at the streetlit road far below; nothing in his hands, nothing at his lips; city lights soft behind",
         camera=f"medium close-up from the side, eye level, {LOW} (the railing in soft shadow)", amb="balcony_night",
         sens="other", safe="the cigarette and smoke are never shown: his empty hands rest on the railing"),
    dict(to=10, reason="framing change: his inner reflection — 28, rich and powerful, yet empty", chars=["jaleel"],
         loc="male_balcony",
         visual=f"close-up of {J}: his handsome bearded face lit by silver moonlight from one side and the gold glow of the lamp behind from the other, eyes heavy with an emptiness he cannot explain, jaw set; his hand with the gold wristwatch resting on the railing in the lower part of the frame",
         camera=f"close-up, eye level, {LOW} (the railing and his wrist in soft shadow)", amb="balcony_night"),
    dict(to=13, reason="framing change: the emptiness and darkness ahead — a lone figure under the stars and moon", loc="male_balcony",
         visual="a wide view from behind and above: a tall broad-shouldered man in a dark-grey long-sleeved shirt and long dark trousers standing small and alone at the railing of a high balcony, looking out over the vast dark city and the black sea beyond; above him a velvet-black sky scattered with countless glittering stars like little pearls and a bright moon; his face is not seen",
         camera="wide shot from behind, slightly high angle, the starry sky and moon in the upper two-thirds, the dark balcony floor and railing as the calm lower third",
         amb="balcony_night"),
    # ---------------- THE ISLAND, NIGHT: Maura comes home
    dict(to=14, reason="scene change: the island at night, the plane lands on the enlarged runway under the moon", loc="runway",
         visual="a small white passenger plane with plain unmarked livery touching down on the long lit runway of the small island airport at night, landing lights on, a bright moon low over the horizon silvering the lagoon, palms in silhouette; no people",
         camera="wide shot, eye level, the plane, moon and sky in the upper two-thirds, the dark runway tarmac with its lights as the calm lower third",
         amb="airport", transition="dissolve"),
    dict(to=17, reason="character enters: Maura steps off the plane and looks around amazed at the enlarged airport",
         chars=["maura"], loc="apron",
         visual="Maura in her white lace dress and white hijab with a small white frangipani, a small handbag on her shoulder, standing at the foot of the plane's boarding stairs behind a few other passengers walking ahead, looking around with wide, amazed eyes and parted lips at the new terminal and the long lit runway",
         camera=f"medium wide shot, eye level, {LOW} (floodlit tarmac)", amb="airport"),
    dict(to=18, reason="character enters: heavily pregnant Reema walks towards her through the arrivals walkway",
         chars=["reema", "maura"], loc="arrivals",
         visual="Reema, eight months pregnant with a modest rounded bump under her loose sage-green dress, walking slowly and heavily towards the camera along the lit arrivals walkway with one hand under her bump and a huge happy smile; in the foreground Maura seen from behind over her shoulder pulling a wheeled suitcase, her white hijab with the frangipani",
         camera=f"medium shot over Maura's shoulder, eye level, {LOW} (the tiled walkway floor)", amb="airport"),
    dict(to=21, reason="action change: the sisters hug and tease each other", chars=["maura", "reema"], loc="arrivals",
         visual="Maura happily hugging her pregnant elder sister Reema from the side, leaning in around Reema's rounded bump, both laughing with joy, Maura's wheeled suitcase standing beside them; then teasing faces",
         camera=f"medium shot, eye level, {LOW} (the tiled walkway floor and the suitcase)", amb="airport", hum=False),
    dict(to=24, reason="character enters: Assad stops behind Reema; Maura looks around for the others", chars=["maura", "reema", "assad"],
         loc="arrivals",
         visual="the three standing in the lit arrivals walkway: Reema laughing in front, her husband Assad standing just behind her with a friendly grin, and Maura a clear arm's-length away from Assad, smiling at him politely while craning her neck to look past them as if searching for someone",
         camera=f"medium wide shot, eye level, {LOW} (tiled floor)", amb="airport"),
    dict(to=27, reason="action change: they walk to the car; Assad has already loaded the boxes", chars=["assad", "reema", "maura"],
         loc="carpark",
         visual="Assad closing the open boot of the silver family car, two taped cardboard boxes and Maura's wheeled suitcase already loaded inside; Reema walking towards the car talking animatedly with one hand on her bump, Maura beside her laughing; a clear arm's-length gap between Maura and Assad; plain boxes with no writing",
         camera=f"medium wide shot, eye level, {LOW} (the dark tarmac of the car park)", amb="airport"),
    dict(to=30, reason="scene change: the night drive home through the developed island", chars=["maura", "reema", "assad"],
         loc="car",
         visual="inside the car at night, seen from the dashboard looking back: Assad driving with both hands on the wheel, Reema in the front passenger seat pointing out of the window and explaining, and Maura in the back seat in the middle leaning forward between the seats, her face lit by passing streetlamps, thrilled and amazed",
         camera=f"medium shot from the dashboard, eye level, {LOW} (the dark seats)", amb="car_night"),
    dict(to=33, reason="framing change: Reema turns round with a mischievous smile to tease Maura about a boyfriend",
         chars=["reema", "maura"], loc="car",
         visual="close on Reema in the front passenger seat, turned back over her shoulder towards the back seat with a teasing, mischievous smile and raised eyebrows; Maura in the back seat soft in the foreground, giggling",
         camera=f"medium close-up between the front seats, eye level, {LOW} (seat backs in shadow)", amb="car_night"),
    dict(to=36, reason="back to the three in the car as Maura explains (reuse)", reuse="beat_012", chars=["maura", "reema", "assad"],
         loc="car", visual="reuse of beat_012", amb="car_night"),
    dict(to=37, reason="scene change: the car stops at the family's gate where everyone has gathered", loc="gate",
         visual="the silver family car stopped in the sandy lane in front of the white gate of the pale-pink two-storey house at night, its headlights glowing; a small crowd of family members and neighbours, women in loose dresses with headscarves and men in shirts and sarongs, gathered at the open gate under the bougainvillea and the porch lamp, waving; nobody in close-up",
         camera="wide shot from the lane, eye level, the house, gate and people in the upper two-thirds, the sandy lane as the calm lower third",
         amb="village_night"),
    dict(to=40, reason="action change: Zulfa hugs Maura the moment she gets out of the car", chars=["zulfa", "maura"], loc="gate",
         visual="Zulfa warmly hugging her daughter Maura at the white gate, her eyes shut with happiness and a wide smile, Maura beaming over her mother's shoulder; magenta bougainvillea and the warm porch lamp above them",
         camera=f"medium shot, eye level, {LOW} (sandy yard)", amb="village_night"),
    dict(to=45, reason="character change: Nafeesa and the neighbours greet Maura; Nafeesa's jokes make everyone laugh",
         chars=["nafeesa", "maura", "zulfa"], loc="gate",
         visual="old Nafeesa, small and lively, patting Maura's shoulder with a wide wrinkled grin and twinkling eyes; Maura smiling shyly; Zulfa beside them laughing; behind them two or three neighbour women in loose dresses and headscarves laughing heartily; all in the sandy yard by the gate under the lamplight",
         camera=f"medium shot, eye level, {LOW} (sandy yard)", amb="village_night"),
    dict(to=47, reason="framing change: Maura looks round at her home — the bougainvillea and pale-pink walls", chars=["maura"],
         loc="gate",
         visual="Maura standing in the sandy front yard, turned three-quarters away from us, looking up at the house with a soft contented smile; magenta bougainvillea spilling down over the coral-stone wall, the pale onion-pink walls glowing in the warm porch light, potted plants and the wooden joali seat in the yard",
         camera="medium wide shot from slightly behind Maura, eye level, the house and bougainvillea in the upper two-thirds, the sandy yard as the calm lower third",
         amb="village_night"),
    dict(to=51, reason="character enters: her father Salaam appears behind her; she turns and greets him", chars=["salaam", "maura", "reema"],
         loc="gate",
         visual="Maura, beaming with joy, holding both of her father Salaam's hands in hers; Salaam smiling tenderly down at her; Reema a step behind them with a teasing grin, one hand on her bump; the white gate and bougainvillea behind",
         camera=f"medium shot, eye level, {LOW} (sandy yard)", amb="village_night",
         sens="other", safe="per the series rule, the daughter's hug with her father is shown as her holding both his hands"),
    dict(to=53, reason="scene change: in the kitchen Zulfa lays out dish after dish; Maura is amazed", chars=["zulfa", "maura"],
         loc="kitchen",
         visual="Zulfa setting down one more dish on the long dining table already crowded with bowls and plates of food, smiling proudly; Maura sitting at the table with wide amazed eyes and a hand at her cheek",
         camera=f"medium shot, eye level, {LOW} (the table top with dishes)", amb="home_night"),
    dict(to=55, reason="detail: the feast Zulfa has cooked (bondibai, breadfruit rice, garudhiya, lonumirus)", loc="kitchen",
         visual="a tight top-down close-up of the crowded dining table so the dishes fill the entire frame edge to edge, no room or background visible: a bowl of clear Maldivian tuna soup (garudhiya), a dish of yellow breadfruit rice, a bowl of creamy sweet rice pudding (bondibai), a small dish of red chilli-onion relish (lonumirus) with lime, steamed rice, fried fish and flatbread on a wooden table, under warm yellow light; no people, no hands, no chairs",
         camera="top-down close-up, the dishes filling the whole frame, the dishes in the lower third kept simple and calm",
         amb="home_night"),
    dict(to=59, reason="character change: the whole family laughing at the table", chars=["maura", "zulfa", "salaam", "reema"],
         loc="kitchen",
         visual="the family seated around the long table full of food: Salaam laughing heartily, Zulfa wide-eyed and mock-stern pointing at the food, Maura with wide eyes and an embarrassed laugh, Reema laughing with a hand on her bump, and next to Reema her husband (a stocky man with a short beard in a navy polo shirt) laughing",
         camera=f"medium wide shot, eye level, {LOW} (the table top)", amb="home_night"),
    dict(to=62, reason="scene change: full and drowsy, Maura stops at her bedroom door; Reema calls from behind", chars=["maura", "reema"],
         loc="landing",
         visual="Maura standing at the open white door of her bedroom on the upstairs landing, one hand resting on her stomach, turning back with a sleepy smile and a small nod; Reema at the other end of the corridor calling to her with one hand raised",
         camera=f"medium wide shot, eye level, {LOW} (tiled corridor floor)", amb="home_night"),
    dict(to=66, reason="location change: her redecorated white room, prepared by her father", chars=["maura"], loc="maura_room",
         visual="Maura in her white lace dress and white hijab standing just inside her room, hands clasped at her chest, looking around in delight at the pale-green and pale-grey walls, the white wardrobe, the white dressing table and the white bed; the balcony door with its white curtain behind",
         camera=f"medium wide shot, eye level, {LOW} (light floor tiles)", amb="room_night"),
    dict(to=67, reason="time change: she falls asleep — the house at night, her upstairs window dark", loc="house_upstairs",
         visual="the pale-pink two-storey house seen from the quiet sandy lane late at night: the upstairs balcony door's white curtain dim and still, the house asleep, bougainvillea over the wall, the moon high above the palms; no people",
         camera="wide shot from the lane, slightly low angle, the house and moon in the upper two-thirds, the empty sandy lane as the calm lower third",
         amb="island_night", transition="xfade"),
    dict(to=68, reason="time jump: she wakes thirsty at 3 a.m.", chars=["maura"], loc="maura_room_3am",
         visual=f"{LILAC}, sitting up on the edge of her white bed in the dark room with her feet on the floor, drowsy, one hand at her throat, glancing at the empty white side table beside her; faint moonlight through the white curtain",
         camera=f"medium shot, eye level, {LOW} (the dark floor)", amb="room_night", transition="black",
         sens="clothing", safe="bedtime: she wears a long lilac home dress and a white hijab, sitting up, never lying down"),
    dict(to=69, reason="location change: half asleep she takes a water bottle from the fridge", chars=["maura"], loc="kitchen_3am",
         visual=f"{LILAC}, standing at the open fridge in the dark kitchen, its cold white light on her sleepy half-closed eyes, taking out a plain clear water bottle with no label",
         camera=f"medium shot, eye level, {LOW} (the dark kitchen floor)", amb="home_night"),
    dict(to=70, reason="back to the sleeping house as she sinks back into sleep (reuse)", reuse="beat_025", loc="house_upstairs",
         visual="reuse of beat_025", amb="island_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Jaleel looked at Shaaliya, lying on one side of the bed wrapped in a blanket, sunk in the comfort of sleep. Getting up from the bed and straightening his body,")
sh(2, "Jaleel leaned against the headboard. Letting out a deep breath like someone trying to calm himself, Jaleel closed his eyes.",
   [("sigh", "ފުންނޭވާއެއް", -22)])
sh(3, "It seemed as if he were thinking over something big. Or as if he wanted to escape from his thoughts. After sitting like that for a moment, Jaleel got up.")
sh(4, "And sliding open the door of the balcony attached to the room, he stepped outside. The cool, damp breeze blowing brushed against Jaleel's uncovered skin and played with it.",
   [("door_open", "ކަހައިލަމުން", -20), ("wind_gust", "ވައިރޯޅިތައް", -22)])
sh(5, "Yet neither that enchanting atmosphere, the cool breezes blowing, nor the queen of the night smiling and reigning in the sky could bring any peace to Jaleel's heart.")
sh(6, "Resting both hands on the railing, Jaleel let out a chest-filling breath. And taking a cigarette from the packet in his hand, he put it to his lips, lit it and drew on it.",
   [("breath_heavy", "ނޭވާއެއް", -22)])
sh(7, "Drawing on the cigarette twice, he released its smoke into the air. Rubbing his chest, as if lost in a thought, Jaleel stood gazing at the road before him.")
sh(8, "Even at twenty-eight, even after marrying, Jaleel could not understand at all why he still could not find the peace his heart ought to have.")
sh(9, "Money, wealth, power and influence are all in Jaleel's hands. Anything he wants, from anywhere in the world, can be his. Any girl he wants can be his.")
sh(10, "Jaleel holds power and money enough to settle matters with a single snap of his fingers. And yet... Shaaliya is a beautiful, good wife.")
sh(11, "His parents' choice was not a bad one. She is perfect in every way. Even so, why does he feel that something, some thing, is missing from his life?")
sh(12, "Why is there an emptiness in his heart that will not fade? Why does it feel as if a darkness lies ahead in which no road can be seen?",
   hum=True)
sh(13, "Like little pearls on a black shawl, the stars twinkled and glittered in the sky. The queen of the night stood shining in the sky, tireless in doing her duty.")
sh(14, "The moon's lovely light had lit up the whole horizon. As the plane touched down on the runway, people began to get up from their seats.",
   [("plane_pass", "ޖެއްސުމާއި", -16)])
sh(15, "Maura too put her headset into her handbag, slipped her phone into her pocket and rose from her seat. Behind the other passengers, Maura stepped off the plane.")
sh(16, "She looked all around in amazement, as if she could not believe the development that had come to the island. The island's airport had been enlarged and the runway extended too.")
sh(17, "Compared with how the airport looked years ago when Maura left this island, what she saw now was so different and complete that it would amaze anyone.")
sh(18, "Pulling her luggage, as Maura came out from among the crowd, her eyes fell on Reema, walking heavily towards her with her eight-month belly.",
   [("footsteps_pavement", "ދަމަމުން", -24)])
sh(19, "\"Dhontha...!\" Running a little, Maura came and hugged Reema. Though Reema's swollen belly kept her from holding her as close as she wanted, Maura very tightly",
   [("footsteps_pavement", "ދުވެލާފައި", -24), ("cloth_rustle", "ބައްދައިލިއެވެ", -24)])
sh(20, "held on to Reema. \"Maoo... oh, how pretty you are now... how grown up you've become!\" Reema said, smiling, as she drew back from Maura.")
sh(21, "\"Only me? Look at you, Dhontha... all puffed up!\" Maura said playfully. Just then Maura noticed Reema's husband Assad, who had come and stopped behind Reema.")
sh(22, "Giving Assad a smile, Maura looked up and down as if searching for something. \"Didn't anyone else come? Where are Mum and the others?\"")
sh(23, "Maura asked. \"They couldn't come... Mum is busy making tea for when you arrive... she's gathered just about all the neighbours...")
sh(24, "Your diet's going to be ruined this time, you know,\" Reema said, laughing. \"Oh no... Mum just wants to fatten me up even more... because it's been ages, that's why...\"")
sh(25, "Maura joked. \"Well, that's why she's always talking about missing you... how many days has it been since you came?... Even last time Mum was upset that you ate so little...")
sh(26, "When I told her you were coming, she said she couldn't wait... she said this time she'd make you something delicious...\"")
sh(27, "Reema said as she started walking towards the car. By then Assad, ahead of them, had already carried the boxes over and loaded them into the car.",
   [("car_door", "އަރުވައި", -20)])
sh(28, "In the short time it took to get home, Reema and Maura asked each other many questions. Seeing the development on the island, Maura was truly thrilled.")
sh(29, "\"Yes... the member elected this time is good... the ones before only cared about piling up money before their term ran out, you see...")
sh(30, "That's why things were the way they were...\" Reema explained. And even in the dark of night she kept pointing out places to Maura. \"Dhontha, when are you due?\"")
sh(31, "Maura asked. \"There's still a month to go... I can't wait to see the baby now... it's very hard too... always kicking,\" said Reema.")
sh(32, "\"That's true... Dhontha hasn't slept for nights on end with the baby kicking,\" Assad said with a laugh. \"Really...?\"")
sh(33, "Maura said, smiling. \"So where's little sister's guy, then?... Didn't you bring him?\" Reema asked, turning back a little to look at Maura with a mischievous smile.")
sh(34, "\"No... I just haven't found anyone I like,\" Maura said with a click of her tongue. \"Oh, what happened? Before, it seemed like you were talking to some boy...\"")
sh(35, "Reema said. \"Oh, that never became anything... I found out later he was talking to other girls too... so then I got fed up...")
sh(36, "Lucky I found out before we got close, otherwise I'd have been far more hurt... right?\" Maura said. Reema nodded in agreement.")
sh(37, "When the car pulled up by the gate of the yard, almost the whole household had gathered at the gate. And some of the neighbours were there too.",
   [("car_approach", "ކާރު", -20)])
sh(38, "As soon as Maura got out of the car, the very first to hug her was her mother. \"My darling... I'm so happy...",
   [("car_door", "ނިކުތުމާއިއެކު", -20)])
sh(39, "so very happy when you said you were moving back to the island for good... I've cooked lots of things... there's bondibai too...")
sh(40, "breadfruit rice, garudhiya and lonumirus too...\" Zulfa said, overjoyed, hugging her daughter.")
sh(41, "\"Look, Nafeesaththa and the others have come too, just wanting to see you...\" Turning round, Mum showed Maura the neighbours by the house.")
sh(42, "Smiling, Maura greeted everyone. \"Hasn't this girl grown! Back from living in Malé, she's even got the Malé look... how fair this girl is...\"")
sh(43, "Nafeesa said, patting Maura's shoulder. Maura smiled. \"Yes, that's how Malé girls are...")
sh(44, "...and what can we do about it now... our young years are gone... we've turned into withered old sticks... into scraps of old tin...")
sh(45, "Nobody would look at us now...\" At old Nafeesa's words everyone burst out laughing. Everyone laughed heartily.")
sh(46, "Maura too, holding back her laughter, looked around. The bougainvillea spilling down over the wall of the house pleased Maura very much.")
sh(47, "Though it was not a grand house, it could not be called an ordinary house either. The pale onion-pink colour on the walls gave Maura's heart an extra coolness.")
sh(48, "\"Where's Dad?\" Maura asked, not seeing Salaam. \"Dad's right here...\" The voice came from behind Maura.")
sh(49, "As Maura turned round, there stood Salaam before her, smiling. \"Daddy...!\" Maura said, hugging Salaam tightly. \"Aww, Daddy's princess...\"",
   hum=True)
sh(50, "Reema teased. \"Daddy's still my favourite,\" Maura replied, sticking her tongue out at Reema. \"I know, I know...\"")
sh(51, "said Reema, smiling. Everyone went into the house. But the neighbours left, saying they would come tomorrow.",
   [("footsteps_sand", "ވަނެވެ", -24)])
sh(52, "After putting the boxes in her room, Maura came into the kitchen. Zulfa was busy putting the dishes on the table.",
   [("cup_clatter", "ތަށިތައް", -22)])
sh(53, "As all kinds of food were laid out on the table, Maura sat amazed, not knowing how she could possibly eat all of it.")
sh(54, "Maura knew Zulfa was a skilled cook. Maura's heart had no doubt at all that everything would taste good.")
sh(55, "\"Mum, how am I supposed to eat all this...?\" Maura said, widening her eyes. \"Don't make such a fuss... you'll have to eat...")
sh(56, "Mum went to such trouble picking breadfruit to cook this rice...\" Zulfa said, widening her eyes too. Salaam, seated, burst out laughing.")
sh(57, "Reema and Assad started laughing too. \"Ha, my child... Mum has been at it since the afternoon, it seems, for something like this...\" said Salaam. \"That's true...")
sh(58, "but if I eat this much I'll probably get even fatter... look how I am already...\" said Maura.")
sh(59, "\"So you'd rather dry up into a skeleton? Better for Mum that you're plump... at least it looks like you're eating well,\" Zulfa said as she began to eat.")
sh(60, "Once again everyone's laughter rang through the kitchen. Having eaten more than ever before, her stomach uncomfortable, Maura came and stopped at her bedroom door.")
sh(61, "Just then she heard Reema calling from behind. \"If you need anything, call Dhontha, okay... oh, and one more thing...")
sh(62, "tomorrow you have to go to the hospital with Dhontha, okay...\" said Reema. Nodding yes, Maura went into her room.",
   [("door_open", "ކޮޓަރިއަށް", -22)])
sh(63, "She ran her eyes around the room. The furniture had been changed and the whole room had been made over.")
sh(64, "Wherever she looked, she could see it was her father's work.")
sh(65, "Maura had learned from Reema that ever since she said she was moving back to the island, Salaam had been working non-stop to get the room ready just the way she would like it.",
   hum=True)
sh(66, "The pale green and pale grey of the room's walls brought her heart peace. The queen-size bed, the big four-door wardrobe and the dressing table were all white.")
sh(67, "After a shower, Maura lay down on the bed hoping to sleep. Tired as she was, it did not take long to fall asleep.")
sh(68, "When Maura woke up thirsty, the clock had struck three. Only then did she remember she had not brought a water bottle to her room.",
   [("breath", "ހޭލެވުނު", -24)])
sh(69, "Even half asleep she got up and went to the kitchen, she was so thirsty. Taking a water bottle from the fridge, drinking as she walked, she came back into her room.",
   [("footsteps_pavement", "ދިޔައީ", -26), ("door_open", "އަލަމާރިން", -24)])
sh(70, "Setting the water bottle down on the side table, Maura sank once again into sleep. To be continued.",
   [("soft_thud", "ބަހައްޓައިލަމުން", -24)])
SHOTS = S

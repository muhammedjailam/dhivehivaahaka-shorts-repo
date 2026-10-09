"""Beat/shot plan for Isq episode 428 (used by plan_beats.py)."""

LOC = {
    "kitchen": "the simple kitchen of Nafeesa's house on a small Maldivian local island: plain pale walls, a white sink under a small window, a small fridge with a box of tissues on top, a few pots and dishes on a wooden shelf, and a little open door looking out to the sunny sandy courtyard and the gate",
    "male_living": "Jaleel's dark, luxurious modern home high above Malé at night: a living room with floor-to-ceiling windows full of the city's night lights, gold lamps, black marble floor and walls, and a long cream sofa",
    "male_study": "a dark, luxurious modern home office in Jaleel's Malé home at night: a wide black marble desk with a gold desk lamp, a high-backed black leather chair, a closed slim laptop and neat folders with blank covers, floor-to-ceiling windows on Malé's city lights",
    "male_bedroom": "the dark, luxurious master bedroom of Jaleel's Malé home at night: black marble and cream textiles, gold lamps, a cream upholstered bench beside a tall glass balcony door with Malé's city lights and a road far below",
    "gate": "the front of Maura's family house on a small Maldivian local island at night: a two-storey house with pale onion-pink walls, a white gate (dhoraashi) in a coral-stone wall with magenta bougainvillea spilling over it, a sandy front yard with potted plants and a wooden joali seat, a white sandy lane lit by a streetlamp, palms, and further down the lane a small white mosque glowing softly",
    "beach_edge": "the place where a white sandy island lane from the small white mosque opens onto an empty white beach at night, palms and coral-stone walls on one side, and beyond, the beach with traditional Maldivian joali seats (hanging seats of woven rope netting on a wooden frame) hung under leaning trees and a small open beach pavilion (holhuashi) lit by a single tube light",
    "beach": "an empty white beach on a small Maldivian local island at night: traditional Maldivian joali seats (hanging seats of woven rope netting on a wooden frame) hung from the branches of leaning trees, a small open wooden beach pavilion (holhuashi) lit by a single white tube light, a calm lagoon and the open sea under a full moon, a sky full of stars",
    "beach_lane": "a white sandy island lane leading up from the empty beach towards the houses at night, coral-stone walls, palms and breadfruit trees, the moonlit sea behind",
}
ISL = "night, a brilliant full moon, silver-blue moonlight on white sand, a sky full of twinkling stars, the soft white glow of the pavilion's tube light, a cool sea breeze"
MOOD = {
    "kitchen": "noon, scorching tropical midday sunlight pouring through the small window and the open door, bright warm whites and gold, a hushed, charged tension",
    "male_living": "night, warm gold lamplight against deep velvety shadows, the glittering city lights beyond the glass, quiet and melancholic",
    "male_study": "night, a single gold desk lamp, deep velvety shadows, cold city lights beyond the glass, empty, stern and lonely",
    "male_bedroom": "night, dim gold lamplight and deep velvety shadows, cool blue city light through the glass, lonely and heartbroken",
    "gate": "night after Isha, a full moon and stars, warm streetlamp glow on the sandy lane, a cool breeze stirring the bougainvillea, quiet and a little lonely",
    "beach_edge": f"{ISL}, quiet and charged with wonder",
    "beach": f"{ISL}, tender, romantic and hushed",
    "beach_lane": f"{ISL}, tender and hopeful",
}

JK = ("Jaleel, NOT in a suit: a white long-sleeved shirt with a faint pink juice stain on the front, black jeans, no jacket, "
      "no tie, black sunglasses folded and hooked at his open collar, his hair slicked back")
JB = ("Jaleel, NOT in a suit: a black long-sleeved shirt with the sleeves rolled up to the elbows and dark trousers, "
      "no jacket, no tie, a gold wristwatch, collar-length black hair swept back")
MW = ("Maura in her white long-sleeved lace ankle-length dress and white hijab fully covering her hair and neck, "
      "a small white frangipani pinned at its side")
SH = "Shaaliya in her black velvet long-sleeved dress with gold cuffs and deep-maroon hijab fully covering her hair and neck"
FZ = "Fauziyya in her dark-green libaas, cream headscarf fully covering her hair and neck and gold-rimmed glasses"
GAP = "a clear arm's-length gap between them, they do not touch"
LOW = "faces in the upper two-thirds, a calm uncluttered lower third"

BEATS = [
    # ---------------- NOON, NAFEESA'S KITCHEN (continuing 393)
    dict(to=2, reason="episode opening: continuing 393 in Nafeesa's kitchen at noon, Jaleel asks to tell her something big",
         chars=["jaleel", "maura"], loc="kitchen",
         visual=f"{JK}, standing a respectful step away from the sink with both hands in his pockets, looking at her with an intense, serious, earnest face; {MW}, standing by the sink holding a few folded tissues, looking up at him wide-eyed and speechless; {GAP}",
         camera=f"medium two-shot from the side, eye level, {LOW} (tiled kitchen floor in sunlight)", amb="island_house_day",
         sens="other", safe="two non-mahram young people alone in a kitchen: shown standing apart with a clear arm's-length gap, his hands in his pockets"),
    dict(to=4, reason="action change: at the sound of someone coming, he steps back, gives her one long deep look and leaves",
         chars=["jaleel", "maura"], loc="kitchen",
         visual=f"{JK}, having stepped back to the little open door of the kitchen, half turned to leave, looking back over his shoulder at her with a long, deep, unreadable look; {MW}, still by the sink in the background holding the tissues, watching him; a wide gap of several steps between them; bright sunlight in the doorway behind him",
         camera=f"medium wide shot, eye level, {LOW} (sunlit kitchen floor)", amb="island_house_day"),
    dict(to=6, reason="character change: Jaleel has gone; Maura alone, rooted to the spot, full of questions",
         chars=["maura"], loc="kitchen",
         visual=f"{MW}, standing alone and still by the sink, the folded tissues forgotten in one hand, the other hand resting on her chest, gazing at the empty sunlit doorway with a confused, tender, wondering expression",
         camera=f"medium close-up, eye level, {LOW} (sink edge and floor in soft light)", amb="island_house_day"),
    # ---------------- NIGHT, MALÉ
    dict(to=8, reason="scene change: night in Malé — Shaaliya sits down beside her mother-in-law Fauziyya on the cream sofa",
         chars=["shaaliya", "fauziyya"], loc="male_living",
         visual=f"{SH}, sitting down on the cream sofa beside {FZ}; Fauziyya holds a small traditional red-and-black lacquered tray with betel leaves and areca nut resting on her knees; Shaaliya leans towards her with a polite, gentle smile, asking; the city lights glitter beyond the floor-to-ceiling windows",
         camera=f"medium wide two-shot, eye level, {LOW} (black marble floor)", amb="mansion_night", transition="dissolve",
         sens="other", safe="the betel (dhufaa) tray is shown only as a small traditional lacquered tray with leaves"),
    dict(to=10, reason="emotional turning point: at the question about Jaleel, Shaaliya's face falls and she forces a lie",
         chars=["shaaliya", "fauziyya"], loc="male_living",
         visual=f"close two-shot on the cream sofa: {SH} in front, her face fallen, sad eyes cast down, forcing a small polite smile; beside her {FZ} looking down at the small lacquered tray on her knees, folding a betel leaf, not noticing",
         camera=f"medium close-up two-shot, eye level, {LOW} (the lacquered tray and sofa cushion in soft shadow)", amb="mansion_night"),
    dict(to=14, reason="action change: alone, Shaaliya holds her silent phone — three days without a call; her unanswered love",
         chars=["shaaliya"], loc="male_living",
         visual=f"{SH}, standing alone at the floor-to-ceiling window of the dark living room, holding her phone against her chest with both hands, its screen dark, gazing out at Malé's night lights with quiet longing and hurt; her faint reflection in the glass",
         camera=f"medium shot from slightly behind and to the side, eye level, {LOW} (black marble floor)", amb="mansion_night"),
    dict(to=17, reason="symbolic detail: the narration describes Jaleel's rigid principles, work, power and money (he is away)",
         loc="male_study",
         visual="Jaleel's empty home office at night: the high-backed black leather chair pushed in at the wide black marble desk, a gold desk lamp lighting a closed slim laptop, neat folders with blank covers and a gold fountain pen lying straight, the glittering city far below through the glass; no people",
         camera="medium shot, eye level, the desk, chair and window in the upper two-thirds, the dark marble desk front as the calm lower third",
         amb="mansion_night"),
    # ---------------- NIGHT, THE ISLAND, FULL MOON
    dict(to=20, reason="scene change: the island at night after Isha — Maura, bored and alone, steps out to her gate",
         chars=["maura"], loc="gate",
         visual=f"{MW}, standing at her open white gate under the bougainvillea, one hand on the gate post, looking down the moonlit sandy lane with a bored, slightly lonely face, the loose end of her white hijab stirring in the breeze while the hijab still fully covers her hair and neck; far down the lane a few men in shirts, sarongs and white skullcaps walk away from the softly lit small white mosque",
         camera=f"medium wide shot, eye level, {LOW} (moonlit sandy lane)", amb="island_night", transition="dissolve",
         sens="other", safe="the Isha prayer is not shown, only men leaving the mosque far down the lane; her 'long curly hair in the wind' is the loose end of her hijab"),
    dict(to=22, reason="scene change: she walks down to the empty beach under the full moon and stars",
         loc="beach",
         visual="a wide view of the empty white beach at night under a huge full moon and a sky of twinkling stars, the moon's silver path on the calm sea, joali seats hanging under leaning trees, the small open pavilion glowing with its tube light; a small petite figure of a young woman in a long white dress and white hijab seen from behind, walking slowly across the white sand towards the joalis",
         camera="wide establishing shot, eye level, the moon, sky and sea in the upper two-thirds, the smooth moonlit sand as the calm lower third",
         amb="beach_night"),
    dict(to=24, reason="action change: Maura sits on a joali under a tree by the tube-lit pavilion, calmed by the breeze",
         chars=["maura"], loc="beach",
         visual=f"{MW}, sitting peacefully on a joali hung from a leaning tree, her hands folded in front of her, eyes half closed, a soft content smile as the sea breeze moves the loose end of her hijab; the small pavilion with its glowing tube light just behind her, the moonlit sea beyond",
         camera=f"medium shot, eye level, {LOW} (moonlit sand under the joali)", amb="beach_night"),
    dict(to=29, reason="character change: Jaleel, coming out of the mosque lane, recognises Maura from behind and slowly approaches",
         chars=["jaleel"], loc="beach_edge",
         visual=f"{JB}, standing where the sandy lane opens onto the beach, hands in his pockets, stopped mid-step and gazing towards the beach with quiet wonder and inner conflict on his stern face; far away across the sand a tiny figure of a young woman in white sits on a joali under a tree with her back to him, beside the small tube-lit pavilion; nobody else anywhere",
         camera=f"medium shot from the side and slightly behind him, eye level, {LOW} (moonlit sand)", amb="beach_night"),
    dict(to=31, reason="action change: he calls her name; startled, she turns round on the joali",
         chars=["maura", "jaleel"], loc="beach",
         visual=f"{MW}, sitting on the joali, turned round looking back over her shoulder, startled and shy, lips parted; {JB}, standing on the sand a few steps behind her joali, hands in his pockets, looking at her; {GAP}",
         camera=f"medium two-shot, eye level, {LOW} (moonlit sand)", amb="beach_night",
         sens="other", safe="two non-mahram young people alone on a beach at night: a clear distance between them, no contact"),
    dict(to=34, reason="action change: Jaleel sits on another joali a little apart and asks question after question",
         chars=["jaleel", "maura"], loc="beach",
         visual=f"two separate joalis hung from two different trees with a clear gap of about two metres between them: {JB} (IMPORTANT: he wears only the plain black shirt with rolled sleeves — absolutely no suit jacket, no tie, no white shirt), sitting on one, leaning forward slightly towards her with his forearms on his knees, asking; {MW}, sitting on the other, looking down with a shy sweet smile; the tube-lit pavilion and the moonlit sea behind; {GAP}",
         camera=f"medium wide two-shot, eye level, {LOW} (moonlit sand between the joalis)", amb="beach_night"),
    dict(to=37, reason="framing change: Maura's view of Jaleel — his firm, manly presence in the moonlight",
         chars=["jaleel"], loc="beach",
         visual=f"{JB}, sitting on his joali in the moonlight, seen in three-quarter view, his black sleeves rolled to the elbows, collar-length black hair swept back and stirred by the breeze, a neatly trimmed beard, a calm, firm, serious face looking towards the side of the frame; fully dressed",
         camera=f"medium close-up, eye level, {LOW} (his folded hands and the joali netting in soft shadow)", amb="beach_night",
         sens="other", safe="her admiration of his body and scent is shown only as a close-up of his face and rolled sleeves, fully dressed"),
    dict(to=41, reason="back to the two of them talking on their joalis", reuse="beat_013", chars=["jaleel", "maura"], loc="beach",
         visual="reuse of beat_013", amb="beach_night"),
    dict(to=43, reason="emotional turning point: 'Business...' — their eyes meet and an unspoken current passes between them",
         chars=["maura", "jaleel"], loc="beach",
         visual=f"side view of the two BOTH SITTING on their own separate joalis hung from two different trees, nobody standing, turned towards each other, their eyes meeting; {MW}, sitting, looking up at him with a shy, luminous look; {JB}, gazing back with a rare softness in his stern face; the full moon over the sea fills the gap of about two metres between them; {GAP}",
         camera=f"medium two-shot in profile, eye level, {LOW} (moonlit sand)", amb="beach_night"),
    dict(to=47, reason="framing change: a long silence on the empty beach; he worries what people would say if they were seen",
         loc="beach",
         visual="a wide view from behind of the empty moonlit beach: two separate joalis hung under two trees far apart, on one a man in a black long-sleeved shirt glancing back over his shoulder towards the dark sandy lane, on the other a petite young woman in a long white dress and white hijab looking out at the sea; the small pavilion glows with its tube light; the full moon and stars over the calm sea",
         camera="wide shot from behind, eye level, the moon, sea and the two small figures in the upper two-thirds, the smooth sand as the calm lower third",
         amb="beach_night"),
    dict(to=51, reason="action change: his phone rings — Shaaliya; his calm vanishes, sweat on his brow, and Maura notices",
         chars=["jaleel", "maura"], loc="beach",
         visual=f"{JB}, sitting on his joali holding his phone, the back of the phone towards the viewer so its screen is not visible, its cold glow on his face, his calm gone, a few beads of sweat on his forehead, jaw tight; in the soft-focus background {MW} on her own joali watching him with quiet concern; {GAP}",
         camera=f"medium close-up on him, eye level, {LOW} (his knee and the joali netting in shadow)", amb="beach_night"),
    dict(to=53, reason="framing change: on the phone, his gaze is fixed on the end of her hijab fluttering in the wind",
         chars=["maura"], loc="beach",
         visual=f"{MW}, sitting on her joali in profile, looking out at the moonlit sea with a soft dreamy face, the long loose end of her white hijab fluttering and lifting in the sea breeze while the hijab stays snugly covering all her hair and neck; moonlight on her face",
         camera=f"medium close-up in profile, eye level, {LOW} (the joali netting and moonlit sand)", amb="beach_night",
         sens="clothing", safe="'her long curly hair in the wind' is shown as the loose end of her hijab fluttering; no hair visible"),
    dict(to=55, reason="character/scene change: Shaaliya on the other end of the call in the Malé bedroom",
         chars=["shaaliya"], loc="male_bedroom",
         visual=f"{SH}, sitting alone on the cream upholstered bench by the glass balcony door, holding the phone to her ear, her face tender and hopeful but anxious, her other hand clasped at her chest; city lights through the glass",
         camera=f"medium shot, eye level, {LOW} (dark marble floor)", amb="mansion_night", transition="dissolve"),
    dict(to=56, reason="back to the beach: Maura tucks the edge of her hijab by her ear and his heart stands still",
         reuse="beat_019", chars=["maura"], loc="beach", visual="reuse of beat_019", amb="beach_night", transition="dissolve",
         sens="clothing", safe="'a strand of hair behind her ear' stays on the hijab image; no hair visible"),
    dict(to=58, reason="back to Jaleel on the phone: he forgets the call, then hurriedly cuts it short",
         reuse="beat_018", chars=["jaleel", "maura"], loc="beach", visual="reuse of beat_018", amb="beach_night"),
    dict(to=60, reason="character/scene change: the call cut off, Shaaliya alone and heartbroken",
         chars=["shaaliya"], loc="male_bedroom",
         visual=f"{SH}, sitting alone on the cream bench by the glass balcony door, the phone lowered in both hands with its screen dark, one hand then pressed to her chest, staring at nothing with glistening eyes, deeply hurt; dim gold lamp and cold city light",
         camera=f"medium close-up, eye level, {LOW} (her hands and the phone in soft shadow)", amb="mansion_night",
         transition="dissolve",
         sens="other", safe="'as if someone squeezed her heart' is shown as her hand pressed to her chest and a quiet, hurt face"),
    dict(to=62, reason="scene/action change: back on the beach, Jaleel stands up from the joali — 'I'm going'",
         chars=["jaleel", "maura"], loc="beach",
         visual=f"{JB}, standing up beside his joali, hands sliding into his pockets, looking down at her with a composed face; {MW}, still sitting on her own joali, looking up at him with a faint hidden disappointment, saying 'okay'; {GAP}",
         camera=f"medium wide two-shot, eye level, {LOW} (moonlit sand)", amb="beach_night", transition="dissolve"),
    dict(to=64, reason="action change: a few steps away he turns back — 'Aren't you coming? The house is close.'",
         chars=["jaleel", "maura"], loc="beach",
         visual=f"{JB}, several steps away on the moonlit sand towards the lane, turned half back and looking over his shoulder at her with a rare gentle look, one hand lifted slightly towards the lane as an invitation; in the soft-focus foreground {MW} seen from behind on her joali; a wide gap between them",
         camera=f"medium wide shot over her shoulder, eye level, {LOW} (moonlit sand)", amb="beach_night"),
    dict(to=65, reason="action change: Maura comes to him smiling and they walk side by side with a clear gap",
         chars=["maura", "jaleel"], loc="beach_lane",
         visual=f"{MW} and {JB} walking side by side up the moonlit sandy lane from the beach towards the houses, {GAP}; Maura looking down with a light, shy smile she tries to hide, Jaleel with his hands in his pockets and a softened face; the moonlit sea behind them",
         camera=f"medium wide shot from the front, eye level, {LOW} (moonlit sandy lane)", amb="beach_night",
         sens="other", safe="walking home together at night: side by side with a clear gap, no contact"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Maura... I have something very big I want to tell you... Will you give me the chance to tell you?\" Jaleel said, putting his hands into both pockets.",
   [("cloth_rustle", "ޖީބަށް", -22)])
sh(2, "Not knowing what to say, Maura could only stand there. What big matter could a man like Jaleel have to tell an ordinary girl like Maura?")
sh(3, "Maura's mind kept filling with questions that had no answers. At the sound of someone coming towards the kitchen, Jaleel quickly stepped away from Maura.",
   [("footsteps_pavement", "އަންނަ", -24)])
sh(4, "After looking at Maura very deeply, as if for the very last time, Jaleel walked out of the kitchen with quick steps.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(5, "Maura stood rooted to the spot, watching Jaleel go. The questions that had formed in her heart were so many. What truth had that look of Jaleel's told her?")
sh(6, "Why did Maura feel an indescribable closeness in that gaze? Why did Maura's young heart long for that closeness?",
   [("heartbeat", "ހިތް", -22)], hum=True)
sh(7, "Coming out from the direction of the kitchen, Shaaliya saw Fauziyya sitting on the sofa. Though she had been about to go to her room, Shaaliya turned back and sat down beside Fauziyya.",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(8, "\"Mamma, aren't you going to sleep yet?\" Shaaliya asked politely. \"No... I'll go soon... So, hasn't Jaleel called?\"")
sh(9, "Fauziyya asked in an ordinary way. At that question Shaaliya's face fell. But Fauziyya, sitting with the betel tray on her knees, did not see it.")
sh(10, "Had she seen it, questions would have arisen in Fauziyya's heart. \"Yes, he calls... he even sent his salaam to Mamma...\" Shaaliya was forced to tell a lie.",
   [("sigh", "މަޖުބޫރު", -24)])
sh(11, "In the three days since Jaleel left for the island, he had not called Shaaliya even once. Even when Shaaliya called, he would not pick up the phone.",
   [("phone_buzz", "ގުޅައިލިޔަސް", -22)])
sh(12, "Though she did not want thoughts running through her mind, Shaaliya could not help it. Even if it was a marriage made without love, at the family's wish, in Shaaliya's heart the buds of love for Jaleel had begun to bloom.")
sh(13, "That is why Jaleel's careless behaviour hurts her. Shaaliya wants there to be love for her in Jaleel's heart too.", hum=True)
sh(14, "At the very least she wants to be valued. But Shaaliya is as certain as the night that this will never happen.")
sh(15, "Jaleel is a firm man who keeps rigid principles, a man always tirelessly busy with his work.")
sh(16, "Perhaps, just as influence, power and money are in Jaleel's hands, his heart too has its own particular rules and its own particular nature.")
sh(17, "Surely the girl who can light a flame of love in Jaleel's hard heart would have to be a very special person.")
sh(18, "Bored of sitting inside the house, Maura stepped out to the gate. Just then she could see people coming out of the mosque after the Isha prayer.",
   [("door_open", "ނިކުމެލިއެވެ", -22)])
sh(19, "The cool breezes kept playing with Maura's long curly hair. Since she had not been on the island many days, Maura had no friends yet.",
   [("wind_gust", "ވައިރޯޅިތައް", -22)])
sh(20, "And when Reema, whose legs were aching, also went into her room, Maura was left completely alone.")
sh(21, "After standing at the gate for a while, Maura began walking towards the beach. The house being close enough to the beach, after two or three minutes' walk she stepped down onto the sand.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(22, "There was not a trace of anyone in the whole area. The moon of the fourteenth night sat reigning on its throne, and around it, in service to that queen, the stars twinkled brightly.")
sh(23, "The cool breezes kept bringing calm to Maura's soul. Walking on the soft white sand, Maura went and sat on a joali hung on a tree.",
   [("wind_gust", "ރޯޅިތަކުން", -24), ("cloth_rustle", "އިށީނދެލިއެވެ", -24)])
sh(24, "The tube light lit beside the beach pavilion spread just enough light over the whole place. Coming out of the mosque, as he was about to step onto the road where the guest house stands,")
sh(25, "the girl sitting on the joali on the beach caught Jaleel's eye. Even though he saw her only from behind, Jaleel was sure it was Maura.")
sh(26, "As there was no one to be seen anywhere around, Jaleel slowly began to step closer to Maura.",
   [("footsteps_sand", "ފިޔަވަޅު", -22)])
sh(27, "Jaleel did not know what kind of magic that girl held. This was not the way Jaleel used to be.")
sh(28, "Going up to anyone on his own for anything, like some vagabond, was not something Jaleel's principles allowed.")
sh(29, "But ever since he began running into Maura, even Jaleel himself did not know where those principles had gone. \"Maura...\"")
sh(30, "Jaleel called, stopping behind Maura. Startled, Maura turned and looked back. \"Yes...\" Maura answered politely.",
   [("gasp", "ސިހިފައި", -20)])
sh(31, "\"What are you doing here...?\" Jaleel could not help asking. \"Just sitting here...\" Maura said.")
sh(32, "Jaleel sat down on a joali a little away from Maura. \"Why alone...?\" Jaleel went on asking question after question.",
   [("cloth_rustle", "އިށީނދެލިއެވެ", -24)])
sh(33, "But instead of being bothered, it brought a sweetness to Maura's heart. Maura began to like the qualities of the young, manly man sitting before her.")
sh(34, "Jaleel had none of the boyish ways other men have. Every movement carried firmness. Manliness at its very height.")
sh(35, "Even his build looked fit and strong. His long black hair, just long enough to hide his shirt collar, and his beard, neither too light nor too dark, struck Maura's heart.")
sh(36, "The long-sleeved black shirt he wore, rolled up to the elbows, made him look even more attractive.")
sh(37, "The passing breezes succeeded in carrying Jaleel's manly scent to Maura.",
   [("wind_gust", "ވައިރޯޅިތައް", -24)])
sh(38, "Maura felt as though she were travelling into an indescribable world. \"I'm just sitting... since I don't have any friends yet...\"")
sh(39, "Maura said. \"Why is that... aren't you from this island...?\" Jaleel's heart grew even more eager to know about Maura.")
sh(40, "He did not even know what kind of spell that girl was casting on him. \"No, I am from this island...")
sh(41, "But I was in Malé studying, and it's only been two days since I came back to the island... that's why...\" Maura said softly and modestly. \"Is that so...?")
sh(42, "What did you study...?\" Jaleel asked. \"Business...\" Maura said, meeting Jaleel's eyes.",
   [("heartbeat", "ހަތަރުކަޅި", -22)])
sh(43, "An indescribable current passed between the two of them. That lovely setting, that beautiful moonlight and the gentle passing breezes made the sound of their two hearts one.",
   hum=True)
sh(44, "Though Maura was eager to know about Jaleel, because of Jaleel's standing she did not dare to ask him anything.")
sh(45, "That is why a quiet silence settled between them. But that emptiness and that silence were a treasure to Jaleel's heart.")
sh(46, "Jaleel was also forced to think about the talk that might spread if anyone saw him sitting near Maura.")
sh(47, "Jaleel's heart did not want Maura's name to be shamed. The silence that had settled over the place was broken by the ringing of Jaleel's phone.",
   [("phone_buzz", "ރިންގުގެ", -18)])
sh(48, "As he took the phone out of his pocket and looked at it, Maura clearly saw the calm leave his face and sweat bead on his forehead.",
   [("cloth_rustle", "ޖީބުން", -24)])
sh(49, "Who could have given Jaleel such a start? \"Hello...\" As he answered the phone, Shaaliya's soft voice reached Jaleel's ear.")
sh(50, "Though that voice was gentle enough to melt hearts with love, Jaleel found no peace and no joy in it.")
sh(51, "Jaleel could not love his faultless, kind wife. He could not feel attached to her. \"Hello...\"")
sh(52, "Even as he answered the phone, Jaleel's gaze stayed fixed on Maura's lovely long curly hair scattering in the wind in front of him.",
   [("wind_gust", "ވިހުރެމުން", -24)])
sh(53, "The thought kept rising in Jaleel's heart: if only he were the cool breeze that plays with Maura's hair.", hum=True)
sh(54, "If only such fortune could be his, the thought kept rising. \"How are you...? You haven't even called since you went there...?\"")
sh(55, "Being his wife, Shaaliya could not help complaining. \"Yes, because I've been busy...\" Jaleel said, just to say something.")
sh(56, "At that moment Maura tucked a strand of hair by her ear. At that sight Jaleel's heart stood still for a moment.",
   [("heartbeat", "ހިތް", -22)])
sh(57, "For a brief moment he even forgot he was on a call with his wife. \"But you could at least have sent a message...\" Shaaliya said in a complaining tone.")
sh(58, "\"Yes... I just didn't have time... I'll call later, okay... I'm busy with something right now...\" Jaleel said hurriedly and cut the call.")
sh(59, "before Shaaliya could say anything at her end. Shaaliya felt as if someone had reached in and squeezed her heart. She was hurt beyond measure.",
   [("sob_breath", "ދެރަވިއެވެ", -24)], hum=True)
sh(60, "That Jaleel did not love Shaaliya was a truth Shaaliya knew. But that careless act of Jaleel's was a thorn that pierced Shaaliya's heart.")
sh(61, "Watching Maura's movements, Jaleel stood up from the joali. \"I'm going, okay...\" Jaleel said. But to Maura it sounded as if he had said, \"Come with me.\"",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(62, "\"Okay...\" Maura said softly, hiding the many thoughts in her heart. After going a little way, Jaleel turned back and looked.",
   [("footsteps_sand", "ގޮސްފައި", -22)])
sh(63, "Jaleel's heart would not agree to leave without Maura. He did not want to leave Maura alone in such a setting, not knowing what the island's people were like. \"Aren't you coming...?")
sh(64, "You should come... the house is close too, isn't it...\" What girl would dare say no to Jaleel's invitation?...")
sh(65, "Though her heart felt as if it would fly away with joy, trying not to let it show on her face, Maura came to Jaleel with a light smile. To be continued.",
   [("footsteps_sand", "އައެވެ", -22)], hum=True)
SHOTS = S

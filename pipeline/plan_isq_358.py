"""Beat/shot plan for Isq episode 358 (used by plan_beats.py).
3 a.m. water -> dawn -> Jaleel leaves Malé -> jetty welcome -> guest house -> Maura at her gate -> Zulfa in the yard
-> hospital pharmacy collision (moment after only) -> sunset balconies (Jaleel secretly photographs Maura)."""

HOUSE = ("Maura's family house on a small Maldivian local island: a two-storey house with pale onion-pink walls, a white "
         "gate in a coral-stone wall with magenta bougainvillea spilling over it, a sandy front yard with potted plants, a "
         "garden hose and a wooden joali seat")
ROOM = ("Maura's upstairs bedroom: pale-green and pale-grey walls, a white queen bed, a white four-door wardrobe, a white "
        "dressing table, a small white side table, and a glass balcony door with a white curtain opening onto a small "
        "balcony with a white railing that faces the sandy street")
GUEST = ("the island's best guest house, a modern two-storey white building with dark-wood balconies, directly across the "
         "sandy street from Maura's pale-pink house")

LOC = {
    "kitchen": "the ground-floor kitchen of Maura's family house on a small Maldivian island at night: simple white cabinets, a tiled counter, a tall fridge, a doorway leading to the stairs",
    "room": ROOM,
    "male_home": "Jaleel's dark, luxurious modern home high above Malé: a wide entrance hall of black marble with gold wall lamps, floor-to-ceiling windows on the city, a tall dark front door standing open",
    "sea": "the turquoise lagoon and open sea just off a small Maldivian local island, the island's palms, white beach and small harbour ahead",
    "jetty": "the harbour jetty of a small Maldivian local island: a concrete quay with white bollards, turquoise water, palms and low white buildings and a small white mosque behind",
    "lane": "a white sandy lane on a small Maldivian local island, coral-stone walls with bougainvillea, palms and breadfruit trees on both sides",
    "guest_front": f"the front of {GUEST}: a black car parked on the sandy street at its entrance, palms, Maura's coral-stone wall and white gate with bougainvillea opposite",
    "gate": f"the white gate in the coral-stone wall of {HOUSE}; across the sandy street stands {GUEST}",
    "yard": f"the sandy front yard of {HOUSE}",
    "hospital": "the small hospital of a Maldivian local island: an open, shaded outdoor walkway along a white single-storey building, the outpatient pharmacy's glass door and window, a wooden bench outside it, potted palms, a sunny sandy courtyard beyond",
    "street_sunset": "the sandy street between Maura's pale-pink two-storey house with its small white-railed balcony and the modern white guest house with dark-wood balconies directly across, palms and rooftops of a small Maldivian island",
    "maura_balcony": "the small balcony of Maura's upstairs bedroom in her pale-pink house: a white railing, a glass balcony door with a white curtain behind her, the sandy street and palms below",
    "jaleel_balcony": "the guest-house balcony of Jaleel's room: a dark-wood railing, an open glass door with a long cream curtain, looking across the sandy street at a pale-pink house with a small white-railed balcony",
}
MOOD = {
    "kitchen": "3 a.m., deep night, the only light the cold white glow from the open fridge, deep velvety shadows, sleepy and quiet",
    "room": "early dawn just before sunrise, soft pale-gold and lilac light through the white curtain of the balcony door, a fresh peaceful morning, birds outside",
    "male_home": "early morning in Malé, cool grey-blue dawn light through the tall windows, gold wall lamps still glowing, rich dark marble, a cold and quiet mood",
    "sea": "bright late-morning tropical sunshine, sparkling turquoise water, white spray, energetic",
    "jetty": "bright late-morning tropical sunshine, crisp shadows, luminous turquoise water, formal and imposing",
    "lane": "bright late-morning sunshine, white sand glaring, crisp palm shadows, speed and dust",
    "guest_front": "bright late-morning tropical sunshine, crisp shadows, tense and angry",
    "gate": "bright morning sunshine, warm golden light, magenta bougainvillea glowing, curious",
    "yard": "bright warm morning sunshine, dappled shade under the bougainvillea, homely and light-hearted",
    "hospital": "bright late-morning tropical light, cool shade under the walkway, sunlit courtyard beyond, calm",
    "street_sunset": "sunset, the sky ablaze with red, orange and gold clouds, long warm shadows, romantic",
    "maura_balcony": "sunset, rich red-orange and golden light on her face, glowing red clouds behind, joyful and romantic",
    "jaleel_balcony": "sunset, warm red-gold light through the cream curtain, the room behind him in soft shadow, secret and spellbound",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
M_LILAC = ("Maura wearing a loose long-sleeved ankle-length soft-lilac home dress instead of the white lace dress, and a "
           "white hijab fully covering her hair and neck, no flower")
M_WHITE = ("Maura in her white long-sleeved lace ankle-length dress and white hijab fully covering her hair and neck, a small "
           "white frangipani pinned on the hijab")
M_ORANGE = ("Maura wearing a loose long-sleeved ankle-length orange dress instead of the white lace dress, and a white hijab "
            "fully covering her hair and neck with a small white frangipani pinned at its side")
J_SUIT = "Jaleel in his black suit, white shirt and black tie"
J_SHADES = "Jaleel in his black suit, white shirt and black tie, wearing black sunglasses"
J_WHITE = ("Jaleel wearing a plain white long-sleeved buttoned shirt and long dark trousers instead of the suit (no jacket, "
           "no tie, fully dressed), his collar-length black hair damp and swept back")
GUARDS = ("two very large, broad-shouldered men in plain black uniforms (black long-sleeved shirts and black trousers) with "
          "empty hands")
OFFICIALS = "a few island council officials and businessmen in short-sleeved shirts and trousers"

BEATS = [
    # ---------------- 3 A.M., MAURA'S HOUSE
    dict(to=2, reason="episode opening: 3 a.m., thirsty Maura fetches a water bottle from the kitchen fridge", chars=["maura"], loc="kitchen",
         visual=f"{M_LILAC}, standing sleepy-eyed in front of the open fridge in the dark kitchen, holding a cold water bottle in one hand and sipping from it, the fridge's white glow lighting her drowsy face, the rest of the kitchen in deep shadow",
         camera=f"medium shot, eye level, slightly from the side, {LOW} (dark tiled floor)", amb="home_night"),
    dict(to=5, reason="time jump: dawn birds; Maura wakes, sits up and checks the time on her phone, then hurries out to pray", chars=["maura"], loc="room",
         visual=f"{M_LILAC}, sitting upright on the edge of her white bed with her feet on the floor, stretching one arm above her head with a sleepy smile while looking at the softly glowing phone in her other hand (screen not visible); a water bottle on the white side table; through the glass balcony door and the half-open white curtain two small birds perch on the white railing in the pale-gold dawn light",
         camera=f"medium wide shot, eye level, {LOW} (pale floor in soft light)", amb="dawn_exterior", transition="black",
         sens="other", safe="her lying asleep is not shown; she is seen sitting up on the bed; the dawn prayer is only implied by narration"),
    # ---------------- MALÉ, EARLY MORNING
    dict(to=10, reason="scene change: Malé, Jaleel leaves home with his suitcase; Shaaliya bids him a loving goodbye", chars=["jaleel", "shaaliya"], loc="male_home",
         visual=f"{J_SUIT}, standing near the tall open front door holding the handle of a black wheeled suitcase, stone-faced and unsmiling, looking away; Shaaliya facing him a clear arm's-length gap away, looking up at him lovingly with a soft hopeful smile, her hands clasped together in front of her; nobody touching; in the background at the open door a male house staff member in a plain dark shirt waits to take the suitcase",
         camera=f"medium wide shot, eye level, the two of them in the upper two-thirds, {LOW} (polished black marble floor)", amb="mansion_day", transition="dissolve",
         sens="intimacy", safe="Shaaliya's goodbye hug is not shown: the married couple stand at arm's length at the door, she looks up lovingly with hands clasped, he holds the suitcase stone-faced"),
    # ---------------- THE ISLAND: ARRIVAL
    dict(to=11, reason="scene change: a speedboat cuts through the waves towards the island harbour", loc="sea",
         visual="a sleek white speedboat racing across the sparkling turquoise sea towards a small palm-fringed island harbour, white spray and a long wake behind it, the hull plain white with no markings; nobody's face visible",
         camera="wide shot, slightly high angle, the boat and island in the upper two-thirds, open turquoise water as the calm lower third", amb="sea_boat", transition="dissolve"),
    dict(to=14, reason="scene change: council officials and businessmen welcome Jaleel on the jetty; sunglasses, two huge bodyguards", chars=["jaleel"], loc="jetty",
         visual=f"{J_SHADES}, walking along the sunny jetty, shaking hands with one of {OFFICIALS} who greets him with a respectful bow, his face cold and unsmiling; right behind him {GUARDS}; the speedboat moored at the quay behind them",
         camera=f"medium wide shot, eye level, {LOW} (sunlit concrete quay)", amb="jetty_day"),
    dict(to=16, reason="action change: Jaleel gets into the car, which speeds off along the sandy lanes to the guest house", loc="lane",
         visual="a black car speeding along a white sandy island lane, kicking up a cloud of fine sand behind it, coral-stone walls with bougainvillea and palms rushing past; a startled elderly island man in a white shirt and checked sarong steps back against a wall to let it pass; the car's windows are dark, nobody inside visible",
         camera="low-angle wide shot down the lane, the car and palms in the upper two-thirds, the white sand lane as the calm lower third", amb="village_day"),
    dict(to=20, reason="action change: Jaleel steps out at the guest house, angrily scolding his staff on the phone (Farhaadh is fired)", chars=["jaleel"], loc="guest_front",
         visual=f"{J_SHADES}, stepping out of the black car in front of the white guest house with a phone pressed to his ear, his face hard with fury, brows drawn, jaw clenched; one of {GUARDS} holds the car door open, the other stands behind; a few island officials waiting at the guest-house entrance",
         camera=f"medium shot, eye level, {LOW} (sandy street in sunlight)", amb="village_day"),
    # ---------------- MAURA AT HER GATE
    dict(to=22, reason="character change: Maura at her gate with a coffee mug hears everything but cannot see his face", chars=["maura"], loc="gate",
         visual=f"{M_WHITE}, standing at her open white gate under the magenta bougainvillea holding a coffee mug in both hands, rising on tiptoe and peering curiously across the sandy street; across the street a black car parked at the white guest house blocks her view, a few island officials gathered beside it",
         camera=f"medium shot from the side, eye level, {LOW} (sandy ground at the gate)", amb="village_day"),
    dict(to=25, reason="action change: she sees only the tall man's back as he strides into the guest house", chars=["maura"], loc="gate",
         visual=f"over-the-shoulder view from behind {M_WHITE} at her gate, coffee mug in hand: across the sandy street a tall broad-shouldered man in a black suit with collar-length swept-back black hair, seen only from behind, strides through the entrance of the white guest house with two very large men in black uniforms following him; his face is not visible",
         camera=f"over-the-shoulder medium wide shot, eye level, {LOW} (sandy street)", amb="village_day"),
    # ---------------- THE YARD WITH ZULFA
    dict(to=29, reason="character change: Maura comes into the yard and asks Zulfa, who is watering the plants", chars=["zulfa", "maura"], loc="yard",
         visual=f"Zulfa standing in the sunny sandy front yard watering the potted plants with a green garden hose, a sparkling arc of water, turning her head to answer with a knowing look; {M_WHITE}, a coffee mug in her hands, standing a few steps away asking with wide curious eyes",
         camera=f"medium wide shot, eye level, {LOW} (wet sand and pots)", amb="garden_day"),
    dict(to=32, reason="action change: Maura sits on the joali with her coffee, teased by Zulfa", chars=["maura", "zulfa"], loc="yard",
         visual=f"{M_WHITE}, sitting on the wooden joali seat in the yard with her coffee mug, pouting her lips playfully; Zulfa standing nearby with the garden hose, smiling at her daughter with fond amusement",
         camera=f"medium shot, eye level, {LOW} (sandy ground)", amb="garden_day"),
    dict(to=36, reason="character enters: pregnant Reema comes out of the house to walk to the hospital", chars=["reema", "maura", "zulfa"], loc="yard",
         visual=f"Reema stepping out of the house door into the sunny yard, one hand resting on her rounded pregnant belly, a small handbag on her shoulder, smiling; {M_WHITE}, getting up from the joali and handing her empty coffee mug to Zulfa, who stands by the hose tap; a warm family moment",
         camera=f"medium wide shot, eye level, {LOW} (sandy yard)", amb="garden_day"),
    # ---------------- HOSPITAL
    dict(to=38, reason="scene change: at the hospital pharmacy Reema waits on the bench and phones someone while Maura goes in", chars=["reema", "maura"], loc="hospital",
         visual=f"Reema sitting on the wooden bench outside the pharmacy, holding a phone to her ear, one hand on her pregnant belly; {M_WHITE}, walking towards the pharmacy's glass door with a small purse; no readable signs",
         camera=f"medium wide shot, eye level, {LOW} (tiled walkway)", amb="hospital_day", transition="black"),
    dict(to=41, reason="action change: the collision, shown only as the moment after: she steps back holding her forehead, the medicine bag on the floor", chars=["maura", "jaleel"], loc="hospital",
         visual=f"{M_WHITE}, just outside the pharmacy door, having stepped back, eyes squeezed shut, fingertips pressed to her forehead, wincing; a small brown paper medicine bag lies on the tiled floor between them; a step away {J_SHADES} stands still, a clear arm's-length gap between them, nobody touching; two very large men in plain black uniforms behind him with their empty hands folded in front, nothing on their belts",
         camera=f"medium shot, eye level, {LOW} (tiled floor with the paper bag)", amb="hospital_day",
         sens="other", safe="the bump of her head against his shoulder is never shown; only the moment after, with a clear gap between them"),
    dict(to=44, reason="emotional turning point: she opens her eyes and freezes: it is the angry man from the guest house, flanked by two huge bodyguards", chars=["jaleel", "maura"], loc="hospital",
         visual=f"{J_SHADES}, standing tall and motionless in the shaded walkway, staring down through his dark sunglasses, flanked on both sides by {GUARDS} and with a few island officials behind; in the near foreground at the edge of the frame {M_WHITE}, startled, drawing back with a frightened little gasp; a clear arm's-length gap between them",
         camera=f"medium wide shot from just behind Maura's shoulder, eye level, {LOW} (tiled walkway)", amb="hospital_day"),
    dict(to=46, reason="emotional turning point: Jaleel's point of view: time stands still", chars=["jaleel"], loc="hospital",
         visual=f"close-up of {J_SHADES}, completely still, lips slightly parted, his stern face softened by spellbound wonder, the walkway and people around him melted into a soft golden blur as if time had stopped",
         camera="close-up, eye level, his face in the upper half, a soft blurred background below", amb="hospital_day"),
    dict(to=48, reason="his point of view: her innocent face and white lace dress as she winces", chars=["maura"], loc="hospital",
         visual=f"a dreamy soft-focus medium close-up of {M_WHITE}: eyes gently closed, fingertips touching her forehead, an innocent pained little frown, the delicate lace of her sleeve catching the light, glowing in a soft golden haze as if the world had paused",
         camera=f"medium close-up, eye level, her face in the upper half, {LOW} (soft blurred light)", amb="hospital_day",
         sens="other", safe="the narration's admiration of her body is shown only as her innocent face and lace sleeve in a soft haze, never framed on her body"),
    dict(to=50, reason="back to Jaleel: his heart races, he forgets for a moment that he has a wife", reuse="beat_016", chars=["jaleel"], loc="hospital",
         visual="reuse of beat_016", amb="hospital_day"),
    dict(to=53, reason="action change: she says sorry and steps aside; he nods and walks on, longing to look back", chars=["maura", "jaleel"], loc="hospital",
         visual=f"{M_WHITE}, standing aside against the white wall, head bowed shyly, clutching the paper medicine bag; {J_SHADES}, walking past her a clear distance away towards the sunny courtyard with the two very large men in black uniforms and the officials, his head turned very slightly back towards her",
         camera=f"medium wide shot, eye level, {LOW} (tiled walkway)", amb="hospital_day"),
    dict(to=56, reason="action change: Reema comes over; her feet ache, Maura phones for a taxi", chars=["reema", "maura"], loc="hospital",
         visual=f"Reema standing by the bench outside the pharmacy, one hand pressed to her lower back, the other on her pregnant belly, looking tired and uncomfortable; {M_WHITE}, holding the paper medicine bag and lifting her phone to her ear, still a little dazed, glancing towards the courtyard",
         camera=f"medium shot, eye level, {LOW} (tiled walkway)", amb="hospital_day"),
    # ---------------- SUNSET
    dict(to=58, reason="time jump: sunset; Maura photographs the red clouds from her balcony", chars=["maura"], loc="street_sunset",
         visual=f"a wide view of the fiery red and gold sunset sky over the island rooftops and palms; small on the white-railed balcony of the pale-pink house, {M_ORANGE}, holding up her phone to photograph the glowing clouds; the back of the phone towards us",
         camera="wide shot from the street, low angle, the sky and her balcony in the upper two-thirds, the sandy street in soft shadow as the calm lower third", amb="beach_evening", transition="black"),
    dict(to=60, reason="action change: she pins a flower on her hijab and takes playful selfies with the red clouds", chars=["maura"], loc="maura_balcony",
         visual=f"{M_ORANGE}, on her balcony holding her phone up at arm's length for a selfie (the back of the phone towards us), smiling playfully with her head tilted, one hand touching the frangipani on her hijab, the red-gold clouds glowing behind her",
         camera=f"medium shot, eye level, {LOW} (white balcony railing in soft shadow)", amb="beach_evening"),
    dict(to=64, reason="character change: across the street Jaleel, just out of the shower, watches her half hidden by his curtain", chars=["jaleel"], loc="jaleel_balcony",
         visual=f"{J_WHITE}, standing half behind the long cream curtain at the open balcony door of his guest-house room, one hand holding the curtain edge, gazing across the street with a spellbound, softened expression, the red-gold sunset light falling across his face",
         camera=f"medium shot, eye level, {LOW} (dark floor and curtain folds in shadow)", amb="beach_evening",
         sens="clothing", safe="'just out of the shower with a towel' is shown as a plain white long-sleeved shirt and long trousers with damp hair, half behind the curtain"),
    dict(to=65, reason="his point of view: Maura in orange on her balcony across the street, matching the red clouds", chars=["maura"], loc="jaleel_balcony",
         visual=f"view across the sandy street from behind the edge of a cream curtain and a dark-wood railing: on the small white-railed balcony of the pale-pink house opposite, {M_ORANGE}, smiling at her phone, glowing in the red-gold sunset; she is small in the distance",
         camera="wide shot from behind the curtain edge, eye level, the opposite balcony in the upper two-thirds, the dark railing in soft shadow as the calm lower third", amb="beach_evening",
         sens="other", safe="secret watching shown with dignity from a distance, never framed on her body"),
    dict(to=68, reason="action change: he quickly photographs her and gazes at the photo: 'Do fairies really live in this world?'", chars=["jaleel"], loc="jaleel_balcony",
         visual=f"{J_WHITE}, half behind the cream curtain, holding his phone up with the back of the phone towards us, its soft glow on his face, a faint wondering smile breaking through his stern features as he gazes at it; red-gold sunset light",
         camera=f"medium close-up, eye level, {LOW} (curtain folds in shadow)", amb="beach_evening",
         sens="other", safe="the photo on his phone is never shown; only the back of the phone and its glow on his face"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Maura woke up thirsty, and the clock had struck three. Only then did she remember she hadn't even brought a water bottle to her room.")
sh(2, "Though she was drowsy, she got up and went to the kitchen because she was so thirsty. She took a water bottle from the fridge and came back into her room sipping from it.",
   [("door_open", "އަލަމާރިން", -22)])
sh(3, "Putting the bottle down on the side table, Maura sank into sleep once again. At the lovely hour of dawn, the calls of the birds and the koel filled the whole surroundings with the sound of beautiful music.",
   [("soft_thud", "ބަހައްޓައިލަމުން", -24)])
sh(4, "Stretching lazily, Maura got up and sat on the bed. Picking up the phone lying on the cabinet beside the bed, she checked what time it was.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(5, "By then it was nearly half past five. Maura hurried to the bathroom so she could pray before sunrise.")
sh(6, "As Jaleel came out of the room pulling a suitcase with one hand, Shaaliya hugged him. Though Jaleel's face didn't show that he disliked it much, it didn't seem that he liked it much either.")
sh(7, "\"I'll miss you very much, okay... Call me once you get there, okay...\" Shaaliya said, looking lovingly at her husband's face.")
sh(8, "Since this was the first time after the wedding that she had to be away from her husband, a kind of unease had begun to grow in Shaaliya's heart.")
sh(9, "But she calmed herself, thinking that Jaleel would be back before many days. Nodding at Shaaliya's words, Jaleel walked towards the door.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(10, "And handing the suitcase to the man standing at the door, he took his phone from his pocket, dialled a number and put the phone to his ear.",
   [("door_open", "ދޮރުމަތީގައި", -22)])
sh(11, "Cutting through the waves of the sea at high speed, the launch came in towards the harbour. To welcome Jaleel, the island council's leaders and the island's",
   [("boat_engine", "ލޯންޗު", -16), ("wave_crash", "ލޮނުގަނޑު", -22)])
sh(12, "most notable businessmen had come down and were waiting on the harbour. Greeting them one after another, Jaleel moved forward.",
   [("footsteps_pavement", "ކުރިއަށް", -24)])
sh(13, "But not even a speck of a smile could be seen on that face. Because of the black sunglasses he wore, the man's strong personality showed all the more.")
sh(14, "And because of the two huge men beside him, like bodyguards, even the smallest child would surely know that Jaleel was no ordinary man.")
sh(15, "As Jaleel headed for the car, the two men in black uniforms came behind him at a brisk pace.",
   [("footsteps_pavement", "ހަލުވި", -22)])
sh(16, "As soon as Jaleel got into the car it sped off, vanishing in the blink of an eye. The car came fast and stopped in front of the best guest house built on that island.",
   [("car_door", "އެރުމާއިއެކު", -18), ("car_drive_off", "ދުއްވާލާފައި", -16), ("car_approach", "މަޑުކޮށްލީ", -20)])
sh(17, "As the big man opened the door, Jaleel stepped out of the car with the phone held to his ear.",
   [("car_door", "ހުޅުވައި", -18)])
sh(18, "On his face then were signs of extreme anger and displeasure. \"What did I tell you people? Don't let them get that project...")
sh(19, "Even after I told you everything from A to Z, do this, do that, this is what you do... What a shame... Where is that Farhaadh now?...")
sh(20, "Tell him it's best he doesn't come to the office any more.\" Having said clearly what had to be said, Jaleel stuffed the phone into his pocket and strode firmly towards the guest house.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(21, "Maura, standing at her gate with a coffee mug in her hand, heard all of it. But however much she looked, she couldn't see the face of the tall man hidden behind the car.")
sh(22, "The anger in his voice came through openly, without being hidden in the least. From the island's leaders gathered there, Maura could tell he was no ordinary man.")
sh(23, "Maura saw the back of the man as he walked in with quick steps into the guest house.",
   [("footsteps_sand", "ހިނގާލާފައި", -24)])
sh(24, "Though she saw him only from behind, Maura noticed his manliness and how attractive his build was.")
sh(25, "Something stirred in Maura's young, inexperienced heart. \"Mum... who is it that's come to stay at the guest house across the street...?\"",
   [("heartbeat", "ގޮތެއް", -22)], hum=True)
sh(26, "Maura asked Zulfa, who was holding the hose to water the plants, as she came in through the gate. \"I don't know, dear...",
   [("pour", "ހޮޅި", -24)])
sh(27, "Nafeesaththa said the other day that some famous businessman from Malé was coming... something about a project that's been arranged to start here...\"")
sh(28, "Zulfa said. \"Is that so...?\" Maura said, as if thinking it over. \"Has he come...?\" Zulfa asked. \"Yes..")
sh(29, "I just saw him going into the guest house... but he seems a very bad-tempered man, Mum... he was saying all sorts of things to someone on the phone as he went in...")
sh(30, "I think he even fired someone from their job...\" Sipping from her coffee cup, Maura sat on the joali. \"Hehehe, is that so... That's what Malé people are really like...\"",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(31, "Zulfa smiled, looking at Maura. \"Don't you want to drink tea...? Is it only coffee you drink...?\" Zulfa asked.")
sh(32, "\"Oh Mum, now you've started not wanting to feed me... I'm still not hungry after how much I ate last night...\" Maura said with a pout. \"Hmm, now you say that...")
sh(33, "Where's your sister now... still not out yet...?\" Zulfa asked. \"No, here she comes...\" Maura said, looking at Reema coming out of the house.")
sh(34, "\"Let's go, Maoo... Mum, we're going to the hospital, okay.. If Assad comes, make him some tea, okay...\" Reema said. \"Yes.. Go carefully, okay...")
sh(35, "Shall I call a taxi...?\" Zulfa said, turning off the tap and facing Reema and the others. \"No, we'll walk...")
sh(36, "They've told me to walk now that the birth is near...\" Reema said. Getting up from the joali, Maura handed the empty coffee mug to Zulfa and set off with Reema.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)])
sh(37, "Coming out of the hospital's outpatient section, Reema and Maura stopped in front of the pharmacy that opens from inside the hospital.",
   [("footsteps_pavement", "ނިކުމެގެން", -24)])
sh(38, "Reema sat waiting on the bench in front of the pharmacy while Maura went in for the medicine. And she took her phone from her handbag and called someone.")
sh(39, "Maura, hurrying out of the pharmacy without paying attention, walked straight into a man who was walking by.",
   [("footsteps_pavement", "ހަލުވިކޮށް", -22)])
sh(40, "At that moment the medicine bag in her hand fell to the floor, and Maura's head struck hard against the man's shoulder. \"Ouch....\"",
   [("soft_thud", "ވެއްޓުމާއިއެކު", -18), ("gasp", "އައޫ", -20)])
sh(41, "Her head hurting, Maura squeezed her eyes shut and put her hand to her forehead. As she opened her eyes and looked, she froze where she stood at the sight of the man in front of her.")
sh(42, "Standing in front of her was the bad-tempered yet manly man she had seen going into the guest house today.")
sh(43, "With him were the island's well-known people, and on either side of him stood two men as huge as mountains, in black uniforms.")
sh(44, "Startled, Maura stepped back. Because of the sunglasses he wore she couldn't tell how he was looking, but Maura could feel that he was staring at her without blinking.",
   [("gasp", "ސިހިފައި", -22)])
sh(45, "Jaleel was bound by a feeling as if everything around him had stopped. It felt as if the whole universe had paused for a moment.",
   [("heartbeat", "ހުއްޓުނު", -20)], hum=True)
sh(46, "Jaleel's eyes stopped on the flawless beauty before him. Why did the innocent way that girl said 'ouch' with her eyes shut in pain strike Jaleel's hard, ice-like heart?")
sh(47, "Jaleel's gaze stopped on the innocence of that fair face and the gentle grace of that delicate figure.")
sh(48, "In the white dress reaching to her ankles, even through the lace sleeves of that dress, the girl's fairness was showing through.")
sh(49, "His heart was beating harder than it had ever beaten before. Jaleel had seen many women in many places around the world.",
   [("heartbeat", "ތެޅުން", -20)], hum=True)
sh(50, "But for the first time his unruly heart began to race, out of control, at the sight of a woman. For a little while, even the fact that he had a wife slipped from Jaleel's memory.")
sh(51, "\"S-sorry....\" the girl said in fright, stepping aside. Nodding as if to say yes, Jaleel walked on.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(52, "Even after leaving the hospital, Jaleel's heart longed restlessly to turn back and look once more at that lovely face.", hum=True)
sh(53, "But Jaleel did not want to give the people with him a chance to gossip. \"What happened to you...?\"")
sh(54, "Reema asked Maura, who had come and stopped beside her. \"I don't know, I just bumped into him... I came out without looking...\" Maura said. \"Okay, let's go now...")
sh(55, "My feet have already started aching...\" Reema said, looking uncomfortable. \"Then we'll go in a taxi, right... I'm calling a taxi, okay...\"")
sh(56, "Maura said, picking up the phone. Uncomfortable from her aching feet, Reema quickly nodded.")
sh(57, "The light of day faded away, and the sun bade farewell as it welcomed the queen of the night.")
sh(58, "Maura stood on her bedroom balcony, never tiring of photographing the red clouds that had spread across the sky.",
   [("camera_shutter", "ފޮޓޯ", -20)])
sh(59, "After taking photos in all sorts of ways, at last she put a flower on her head and began taking selfies so beautifully that the red clouds would be in them too.",
   [("camera_shutter", "ސެލްފީ", -20)])
sh(60, "Smiling, Maura took many photos in all sorts of cute poses. But was Maura the only one taking Maura's photos?",
   [("camera_shutter", "ފޮޓޯއެއް", -22)])
sh(61, "Was that image being captured only on the phone's screen? Jaleel stood hidden behind the curtain of his open balcony door.",
   [("cloth_rustle", "ފޮތިގަނޑާއި", -24)])
sh(62, "Every pose Maura struck on the balcony of the house opposite was visible to Jaleel.")
sh(63, "Just out of the shower, Jaleel stood there, and from his slightly long hair drops of water")
sh(64, "kept dripping down onto his shoulders. Jaleel was losing himself, carried away by Maura's wondrous beauty.")
sh(65, "Behind the curtain, Jaleel was delighting in that sight. The orange dress Maura wore, matching the red clouds in the sky, made Jaleel's heart even more lovesick.",
   hum=True)
sh(66, "Seeing the poses Maura struck, Jaleel almost laughed. Quickly picking up his phone, he saved that sight on it.",
   [("camera_shutter", "ރައްކާ", -20)])
sh(67, "And for a while Jaleel stood lost in Maura's photo on the phone's screen. Jaleel's whole soul agreed that Maura was beautiful enough to fall in love with.")
sh(68, "\"What beauty....\" Even Jaleel's hard heart bore witness to Maura's beauty. \"Do fairies really live in this world...?\" Jaleel's heart cried out. To be continued.",
   [("heartbeat", "ގޮވައިލިއެވެ", -22)], hum=True)
SHOTS = S

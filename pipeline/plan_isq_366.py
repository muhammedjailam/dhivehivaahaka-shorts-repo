"""Beat/shot plan for Isq episode 366 (used by plan_beats.py)."""

PINK_HOUSE = ("Maura's family house: a two-storey house with pale onion-pink walls, a white gate (dhoraashi) in a coral-stone "
              "wall with magenta bougainvillea spilling over it, a sandy front yard with potted plants")
GUEST_HOUSE = ("the guest house, the island's best: a modern two-storey white building with dark-wood balconies; Jaleel's room "
               "has a balcony with a dark railing and a cream curtain at the open door")

LOC = {
    "gh_balcony": f"the upstairs balcony of {GUEST_HOUSE}; directly across a sandy street lined with palms stands {PINK_HOUSE}, its small upstairs balcony with a white railing and a glass door with a white curtain facing the guest house",
    "maura_balcony": f"the small upstairs balcony of {PINK_HOUSE}: a white railing, a glass balcony door with a white curtain behind; directly across the sandy street stands {GUEST_HOUSE}",
    "street_sunset": f"a sandy street on a small Maldivian local island, palms and a breadfruit tree; on one side {PINK_HOUSE} with its small upstairs balcony with a white railing and a white-curtained glass door; directly across the street {GUEST_HOUSE}; the two balconies face each other over the street",
    "maura_room": "Maura's upstairs bedroom in her family's pale-pink house: pale-green and pale-grey walls, a white queen bed, a white four-door wardrobe, a white dressing table, a side table, and a glass balcony door with a white curtain",
    "home_kitchen": "the kitchen of Maura's family house at night: a simple clean Maldivian home kitchen, pale-yellow walls, a gas stove with pots, a steel sink, a small fridge, open shelves with jars and plates, a single warm ceiling bulb, a wooden doorway to the hall",
    "lane_night": f"a white sandy lane on a small Maldivian island at night between coral-stone walls with bougainvillea, palms overhead, streetlamps; {PINK_HOUSE.split(':')[0]} on one side and, two doors down, the open gate of Nafeesa's house with a warmly lit sandy courtyard inside",
    "courtyard": "Nafeesa's house at night: an open sandy courtyard enclosed by a coral-stone wall with a gate, a long wooden table with plastic chairs around it, a string of warm bulbs overhead, palm fronds and a breadfruit tree, the lit doorway of a simple kitchen at one side",
    "nafeesa_kitchen": "Nafeesa's simple kitchen at night: a steel sink under a small window, a small white fridge, a work table with a box of tissues, pots and serving bowls, plain cream walls, a single warm bulb, and a little open door looking out to the courtyard and the gate",
}
MOOD = {
    "gh_balcony": "sunset, a sky of fiery red and orange clouds, warm low golden light on his face, long soft shadows, a hush of wonder",
    "maura_balcony": "sunset, fiery red and orange clouds, warm golden rim light, shy surprise",
    "street_sunset": "sunset, a sky of red and orange clouds over the palms, golden light on the two balconies, the sandy street in soft violet shadow, romantic stillness",
    "maura_room": "sunset light glowing orange through the white curtain, soft warm shadows in the room, a flutter of shy joy",
    "home_kitchen": "night, warm yellow light from a single ceiling bulb, deep soft shadows, homely and lively",
    "lane_night": "night, warm amber streetlamps and moonlight on white sand, deep blue shadows, the warm glow of the courtyard ahead",
    "courtyard": "night, warm golden light from a string of bulbs, velvety dark sky, steam rising from the food, festive and warm",
    "nafeesa_kitchen": "night, warm golden light from a single bulb, soft velvety shadows, quiet and charged, a world away from the chatter outside",
}

M_OR = ("Maura in a loose long-sleeved ankle-length orange dress (NOT the white lace dress of the reference) and a white hijab "
        "fully covering her hair and neck with a small white frangipani pinned at its side")
J_OPEN = ("Jaleel in a plain white long-sleeved buttoned shirt (no jacket, no tie) and long dark trousers, his black hair damp "
          "and swept back")
J_DIN = ("Jaleel in a white long-sleeved shirt open at the collar and black trousers (no jacket, no tie), gold watch, hair "
         "swept back")
Z = "Zulfa in her soft-blue floral housecoat dress and maroon headscarf"
N = "Nafeesa in her lavender libaas and white headscarf"
L = "Lamha in her mint-green dress and coral-pink hijab"
GAP = "a clear arm's-length gap between them, nobody touching"
LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GUESTS = ("about ten Maldivian men from Malé in neat button shirts and long trousers")

BEATS = [
    # ---------------- SUNSET, the two balconies
    dict(to=3, reason="episode opening: the 358 sunset moment from Jaleel's side, staring from the guest-house balcony",
         chars=["jaleel"], loc="gh_balcony",
         visual=f"{J_OPEN} — NOT the black suit of the reference: no jacket, no tie, no suit, just the plain white shirt fully buttoned up to the collar with only the top collar button open, chest completely covered, the sleeves down — standing half-hidden by the cream curtain at the open balcony door, one hand resting on the dark railing, gazing across the street with a face of stunned wonder, lips slightly parted, completely forgetting himself; the pale-pink house across the street soft and out of focus behind",
         camera=f"medium shot from the side, eye level, {LOW} (the dark railing in soft shadow)", amb="island_day",
         sens="clothing", safe="narration: he came out without drying off / wearing nothing on his upper body; shown fully dressed in a white long-sleeved shirt and trousers, damp hair"),
    dict(to=4, reason="character change: Maura turns with her phone and sees the young man across the street", chars=["maura"], loc="maura_balcony",
         visual=f"{M_OR}, standing at her white balcony railing, half turned towards the street with her phone lowered in one hand (its screen not visible), caught mid-turn, eyes widening in surprise as she notices someone on the balcony opposite",
         camera=f"medium shot, eye level, {LOW} (the white railing)", amb="island_day"),
    dict(to=6, reason="framing change: her view of the young man on the guest-house balcony across the street", chars=["jaleel"], loc="street_sunset",
         visual=f"seen from Maura's balcony across the sandy street: the white guest house's upstairs balcony with its dark railing, and on it {J_OPEN}, tall and broad-shouldered, standing beside the cream curtain, a few drops of water glinting at the ends of his damp hair, looking straight across at the viewer with an intense unblinking gaze; the white railing of Maura's balcony blurred in the near foreground",
         camera="medium-long shot across the street, eye level, the guest-house balcony and his figure in the upper two-thirds, the blurred white railing and the sandy street as the calm lower third",
         amb="island_day", sens="clothing", safe="narration describes him covered only by a white towel with water drops on his body; shown in a white long-sleeved shirt and trousers, only damp hair"),
    dict(to=7, reason="framing change: the two of them gazing at each other across the street (wide)", loc="street_sunset",
         visual="a wide view of the sandy street at sunset from street level: on the left the pale-pink house's small upstairs balcony with a petite young woman in an orange ankle-length dress and a white hijab standing still at the white railing; on the right, directly across, the white guest house's balcony with a tall man in a white long-sleeved shirt standing by a cream curtain; the two small figures look at each other across the whole width of the empty street",
         camera="wide shot from the middle of the sandy street, low angle, both balconies and the red sky in the upper two-thirds, the empty sandy street as the calm lower third",
         amb="island_day", hum=True),
    dict(to=8, reason="action change: she hurries back inside and shuts the balcony door", chars=["maura"], loc="maura_balcony",
         visual=f"{M_OR}, hurrying back in through the glass balcony door, pulling it shut behind her with one hand, the white curtain swirling, her face turned down and away with flustered shyness",
         camera=f"medium shot from the balcony, eye level, {LOW} (balcony floor in shadow)", amb="island_day"),
    dict(to=10, reason="scene change: inside her room, hand on her racing heart, an unexplained smile", chars=["maura"], loc="maura_room",
         visual=f"{M_OR}, standing with her back against the closed glass balcony door inside her room, the white curtain glowing orange behind her, one hand pressed to her chest over her heart, eyes closed for a moment, catching her breath, a small helpless smile on her lips",
         camera=f"medium shot, eye level, {LOW} (pale floor tiles)", amb="island_house_day"),
    # ---------------- NIGHT, Maura's home kitchen
    dict(to=14, reason="time jump to night (after Isha, prayer not shown): Zulfa on the phone in the kitchen, Maura at the doorway",
         chars=["zulfa", "maura"], loc="home_kitchen",
         visual=f"{Z} standing by the stove talking animatedly into a phone held to her ear, her free hand raised in exasperation; in the wooden doorway behind her, {M_OR} has just stopped and is listening curiously",
         camera=f"medium wide shot, eye level, {LOW} (kitchen floor)", amb="island_house_night", transition="black",
         sens="other", safe="the Isha prayer is only mentioned; prayer is never shown"),
    dict(to=19, reason="action change: mother and daughter talk face to face about Nafeesa's call", chars=["zulfa", "maura"], loc="home_kitchen",
         visual=f"{Z} facing her daughter, phone lowered in one hand, explaining with a tired, amused shake of her head; {M_OR} listening attentively a step away, hands clasped",
         camera=f"medium two-shot, eye level, {LOW} (kitchen counter edge)", amb="island_house_night"),
    dict(to=23, reason="action change: Maura hesitates, Zulfa switches off the kitchen light and reassures her", chars=["maura", "zulfa"], loc="home_kitchen",
         visual=f"{M_OR}, standing quietly with a thoughtful, slightly nervous expression, fingers fidgeting; behind her {Z} reaches for the light switch by the doorway, smiling reassuringly at her daughter",
         camera=f"medium shot on Maura, eye level, {LOW} (kitchen floor)", amb="island_house_night"),
    # ---------------- to Nafeesa's
    dict(to=26, reason="scene change: they lock up and walk two doors down; through the gate the long table and girls setting chairs",
         chars=["zulfa", "maura"], loc="lane_night",
         visual=f"{Z}, slipping a key into her housecoat pocket, and {M_OR} walking side by side along the moonlit sandy lane towards an open gate two doors down; through the gate a warmly lit courtyard with a long wooden table where two young girls in long dresses and hijabs are arranging plastic chairs",
         camera=f"medium wide shot from behind and to the side, eye level, {LOW} (white sand lane)", amb="village_night", transition="dissolve"),
    dict(to=29, reason="scene change: Nafeesa's kitchen, Nafeesa dishing up with a helper girl; Zulfa arrives", chars=["nafeesa", "zulfa", "maura"], loc="nafeesa_kitchen",
         visual=f"{N} ladling curry into serving bowls at the work table with a helper girl in a pale-yellow dress and grey hijab, looking up with a relieved, delighted face; {Z} stepping in through the door, arms open in greeting, and {M_OR} shyly behind her mother",
         camera=f"medium wide shot, eye level, {LOW} (work table top with bowls)", amb="island_house_night"),
    dict(to=31, reason="action change: Maura carries the hot chicken curry and sets dishes on the long table", chars=["maura"], loc="courtyard",
         visual=f"{M_OR}, setting a steaming bowl of chicken curry down on the long wooden table with both hands, more bowls and plates already arranged, a gentle focused smile; plastic chairs around the table, nobody seated yet",
         camera=f"medium shot, eye level, {LOW} (the table top with bowls)", amb="village_night"),
    dict(to=34, reason="action change: the full table; Maura photographs it with her phone", chars=["maura"], loc="courtyard",
         visual=f"the long wooden table laden with Maldivian dishes in the foreground: chicken curry, mung-bean curry, a green leaf salad, a big dish of rice, a stack of roshi flatbread, fried fish and fried chicken, three desserts, jugs of cold water and a small lacquered dhufaa tray; at the far end {M_OR} holds up her phone to photograph the table (its screen not visible), with a satisfied little smile",
         camera="medium shot along the table, eye level, Maura's face in the upper third, the dishes filling the middle, the table edge as the calm lower third",
         amb="village_night"),
    dict(to=38, reason="character change: the Malé guests arrive and eat; Maura stands apart; Jaleel at the table keeps glancing at her",
         chars=["jaleel", "maura", "zulfa", "nafeesa"], loc="courtyard",
         visual=f"{GUESTS} seated along the long table eating; among them {J_DIN} at the near side, pausing with his plate to look up towards the edge of the courtyard; {Z} and {N} serving food to the guests; at the courtyard edge, well apart from the table, {M_OR} stands with her hands clasped, glancing shyly at Jaleel",
         camera=f"medium wide shot, eye level, {LOW} (sandy courtyard floor)", amb="courtyard_dinner"),
    dict(to=41, reason="character enters: Lamha beside Maura, teasing her about the businessman", chars=["lamha", "maura"], loc="courtyard",
         visual=f"{L} standing beside Maura at the edge of the courtyard, leaning in to whisper with a mischievous dimpled grin and a small nod towards the dinner table; {M_OR} pretending not to understand, eyes shyly lowered; the guests at the long table blurred in the background",
         camera=f"medium two-shot, eye level, {LOW} (sandy ground)", amb="courtyard_dinner"),
    dict(to=43, reason="emotional turning point: Maura's astonishment — it's Yoosuf Jaleel", chars=["maura"], loc="courtyard",
         visual=f"close-up of {M_OR}, her eyes wide and lips parted in astonishment, one hand raised to her mouth, the warm string lights and the blurred dinner table behind her",
         camera=f"close-up, eye level, {LOW} (soft bokeh)", amb="courtyard_dinner", hum=True),
    dict(to=44, reason="back to Lamha introducing herself", reuse="beat_015", chars=["lamha", "maura"], loc="courtyard",
         visual="reuse of beat_015", amb="courtyard_dinner"),
    dict(to=46, reason="action change: Zulfa calls Maura and points to Jaleel standing beside her; Maura freezes", chars=["zulfa", "jaleel", "maura"], loc="courtyard",
         visual=f"{Z} near the kitchen doorway gesturing with one hand towards {J_DIN}, who stands a respectful step beside her with his hands in his pockets, his intense gaze fixed on Maura; in the foreground {M_OR} has stopped still, stiff with nervousness; {GAP}",
         camera=f"medium wide shot over Maura's shoulder, eye level, {LOW} (sandy ground)", amb="courtyard_dinner"),
    # ---------------- Nafeesa's kitchen, the sink
    dict(to=48, reason="action change: Maura leads the way to the kitchen, Jaleel following several steps behind", chars=["maura", "jaleel"], loc="nafeesa_kitchen",
         visual=f"{M_OR} stepping in through the little kitchen door and pointing politely towards the steel sink, eyes lowered; several steps behind her in the doorway {J_DIN} follows, hands in his pockets, gazing at her; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (kitchen floor)", amb="island_house_night"),
    dict(to=50, reason="action change: he washes his hands; she holds out tissues at arm's length, head bowed", chars=["jaleel", "maura"], loc="nafeesa_kitchen",
         visual=f"{J_DIN} at the steel sink drying his hands; a full arm's length away {M_OR} holds out a few white tissues at the full stretch of her arm, her head bowed shyly; he turns his head to look at her; {GAP}",
         camera=f"medium two-shot from the side, eye level, {LOW} (kitchen floor)", amb="island_house_night"),
    dict(to=53, reason="framing change: Jaleel's close look at her, softly asking her name", chars=["jaleel"], loc="nafeesa_kitchen",
         visual=f"close-up of {J_DIN}, STANDING by the steel sink, a crumpled white tissue in one hand, his stern face softened, dark eyes full of wonder, looking slightly down towards someone off-frame and asking a quiet question; the warm bulb and the kitchen softly blurred behind him; he is the only person in the frame, nobody in the foreground",
         camera=f"close-up, eye level, {LOW} (soft dark background)", amb="island_house_night", hum=True,
         sens="clothing", safe="narration mentions her feet showing below the ankle-length dress; never shown — only his face"),
    dict(to=55, reason="action change: she says her name head bowed; he puts his hands in his pockets and takes a step", chars=["jaleel", "maura"], loc="nafeesa_kitchen",
         visual=f"{J_DIN} standing with both hands in his trouser pockets, a faint warm look on his face; facing him a full arm's length away {M_OR}, head bowed in shyness, hands clasped in front of her; {GAP}",
         camera=f"medium two-shot in profile, eye level, {LOW} (kitchen floor)", amb="island_house_night"),
    dict(to=58, reason="emotional turning point: she looks up astonished at the compliment, then blushes and lowers her head", chars=["maura"], loc="nafeesa_kitchen",
         visual=f"close-up of {M_OR}, cheeks flushed pink, a faint shy smile, eyes lowered, head tilted down, glowing in the warm light",
         camera=f"close-up, eye level, {LOW} (soft background)", amb="island_house_night", hum=True),
    dict(to=60, reason="back to Jaleel: 'I like it very much' (double meaning)", reuse="beat_021", chars=["jaleel"], loc="nafeesa_kitchen",
         visual="reuse of beat_021", amb="island_house_night"),
    dict(to=61, reason="action change: he leaves through the door without another word; she watches, puzzled", chars=["maura", "jaleel"], loc="nafeesa_kitchen",
         visual=f"{M_OR} in the foreground, brows drawn together in a puzzled, questioning look, watching {J_DIN} walk away out through the little door towards the courtyard, his back to us; {GAP}, he is far away near the door",
         camera=f"medium shot over Maura's shoulder, eye level, {LOW} (kitchen floor)", amb="island_house_night"),
    dict(to=64, reason="closing reflection: Maura alone, his name settling in her heart", chars=["maura"], loc="nafeesa_kitchen",
         visual=f"{M_OR}, alone at the little open kitchen door, leaning lightly against the frame, one hand resting over her heart, gazing out dreamily towards the warmly lit courtyard and gate, a soft secret smile",
         camera=f"medium shot from inside the kitchen, eye level, {LOW} (kitchen floor in soft shadow)", amb="island_house_night", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"What beauty...\" Even Jaleel's hard heart bore witness to Maura's beauty. \"Do fairies really live in this world...?\" Jaleel's heart cried out.")
sh(2, "Lost in thought, Jaleel had stepped out onto the balcony without even drying himself. He didn't seem to notice that he stood there with nothing on his upper body, nor that he was staring at Maura without blinking.")
sh(3, "Jaleel's heart had completely surrendered to the enchanting beauty before him. He even forgot that he had a wife.", hum=True)
sh(4, "Turning around with her phone in hand, Maura saw the young man standing on the balcony of the guest house opposite.")
sh(5, "His body was covered only by a white towel, and drops of water from his hair were trickling down that strong body.")
sh(6, "Maura felt her throat go dry at the sight of how attractive the young man was.")
sh(7, "As the young man stood watching Maura without blinking, Maura's heart too was stirring. It was as if an indescribable melody were being born in her heart.")
sh(8, "Maura didn't dare hold that piercing gaze for long. She hurried back into her room and shut the balcony door.",
   [("door_close", "ލައްޕާލައިފިއެވެ", -18)])
sh(9, "Pressing her hand to her chest over her pounding heart, she quickly took two or three breaths to calm herself.",
   [("heartbeat", "ތެޅެމުން", -20), ("breath", "ނޭވާއެއް", -22)])
sh(10, "Why a smile came to her lips, Maura herself didn't know. It was night. Having prayed Isha, Maura came downstairs, heard Zulfa talking loudly in the kitchen and headed that way.")
sh(11, "Who could Zulfa be talking to at this hour, Maura wondered. As she entered the kitchen she began to hear clearly what Zulfa was saying.")
sh(12, "\"Well, Nafeesa, you're something, aren't you... When you called this afternoon you said nothing like this... I haven't even cooked dinner yet...")
sh(13, "It's nearly eight now... How am I supposed to cook anything now... But what else can I do... It's Nafeesa, after all... I'll have to go...")
sh(14, "Yes, no problem... yes... I'm coming right now...\" As Zulfa hung up and turned towards the kitchen door, she saw Maura standing in the doorway.")
sh(15, "\"What happened, Mum? What did Nafeesaththa do?\" Maura asked. \"What would she do, dear... That's just Nafeesaththa's way...")
sh(16, "She only panics once the fire is already under the pot. She called because tonight she has to serve dinner to the delegation that has come from Malé.")
sh(17, "Vaafiraththa can't come either, so she called to ask me to come and help... Nafeesaththa is doing it all alone... How hard it must be... dinner for ten people...")
sh(18, "Luckily the cooking is done, she says...\" Zulfa sighed. \"Then you should go, Mum,\" Maura said. \"Yes, I'm going...",
   [("sigh", "އަމުނައިލިއެވެ", -22)])
sh(19, "But I shouldn't go alone... You should come too, dear... Even today you only went out to the hospital with your sister... You get bored staying at home...")
sh(20, "It's when you go out that you make friends,\" Zulfa said. Maura stood silent, as if thinking it over.")
sh(21, "Even Zulfa couldn't tell what she was thinking. \"What are you thinking about... Are you scared?\" Zulfa asked, switching off the kitchen light.")
sh(22, "\"No... but I might not know how to behave there... What if I make a mistake... they're respected people...\" Maura said. \"Don't worry...")
sh(23, "Mum is right here... Let's go... On our way back we'll bring food for your sister... She's asleep now... the poor thing couldn't sleep last night either...\"")
sh(24, "Zulfa said as she stepped out of the door and slipped on her sandals. Then, taking the key from the pocket of her housecoat, she locked the door.",
   [("door_close", "ނިކުމެ", -22), ("lock_click", "ތަޅުލައިފިއެވެ", -18)])
sh(25, "Mother and daughter walked to Nafeesa's house, two doors down. As they came in through the gate, Maura saw a long wooden table set up in the middle of the courtyard.",
   [("footsteps_sand", "ހިނގާލާފައެވެ", -22)])
sh(26, "And she saw two girls busy arranging chairs around it. Zulfa led Maura towards the kitchen.")
sh(27, "There Nafeesa and another girl were busy putting food into bowls and plates. \"Nafeesa...\" Zulfa called as she entered the kitchen. \"Zulfa, you've come...",
   [("cup_clatter", "ތަށިތައްޓަށް", -24)])
sh(28, "How good that you came... I just can't manage... There's still so much to do... I haven't even got the dhufaa tray ready...")
sh(29, "And at the last minute Vadheefa said she couldn't come...\" Nafeesa said. \"Never mind that now... Give it here, I'll dish up the food...\"")
sh(30, "Zulfa moved over to Nafeesa and took the bowl from her hands. Maura carried the bowl of hot chicken curry and set it on the table in the middle of the courtyard.",
   [("cup_clatter", "ބެހެއްޓިއެވެ", -22)])
sh(31, "Like that, Maura brought plate after plate and arranged them on the table. The whole table filled with all kinds of food. Chicken curry and mung-bean curry.",
   [("cup_clatter", "އަތުރަމުން", -24)])
sh(32, "A salad made with two kinds of leaves, rice and roshi. At the last minute fried fish and chicken were added too.")
sh(33, "Three kinds of dessert, cold drinking water and the dhufaa tray were on the table too. With everything laid out and a moment to spare, Maura took a photo of the table.",
   [("camera_shutter", "ފޮޓޯއެއް", -18)])
sh(34, "Maura looked over the table with satisfaction. Just then, seeing people opening the gate and coming in, Maura stepped back a little.",
   [("door_open", "ހުޅުވާފައި", -22)])
sh(35, "Zulfa, Nafeesa and another girl were busy helping them, serving food onto their plates.",
   [("cup_clatter", "އަޅައި", -24)])
sh(36, "Maura stood a little apart, watching for Zulfa's signals. Standing there, Maura's eyes kept going to the young man she had seen on the balcony today.")
sh(37, "When they had served themselves and begun to eat, the young man's gaze too kept settling on Maura from time to time.")
sh(38, "But it didn't seem that anyone there noticed any of it. \"Handsome, isn't he...\"")
sh(39, "asked the girl who had stopped beside Maura. \"Who...?\" Maura pretended not to know. \"Don't try to fool me... He keeps looking at you so much...\"")
sh(40, "The girl was pointing at that very young man. \"Do you know who he is?\" the girl asked. \"No, I don't... Who?\"")
sh(41, "Maura asked eagerly. \"The famous businessman Yoosuf Jaleel...\" the girl said. \"What...!!!\"",
   [("gasp", "ވަޓް", -20)])
sh(42, "Maura asked in astonishment, her eyes wide. She couldn't believe it. Yoosuf Jaleel was a name Maura had heard. A famous name.")
sh(43, "But only now did she learn who he was. Only now did she see him with her own eyes. And Maura wondered why the gaze of a man like Yoosuf Jaleel would settle on an ordinary girl like her.")
sh(44, "\"By the way... I'm Lamha...\" the girl introduced herself. Maura gave a light smile.")
sh(45, "Just then Zulfa called out to Maura, \"Dear... show this gentleman the sink...\" Zulfa said, pointing to Jaleel, who was standing beside her.")
sh(46, "Maura felt as if something cold rose inside her. Her whole body seemed to freeze when she saw Jaleel's piercing gaze fixed on her.",
   [("heartbeat", "ގަނޑުވާ", -20)], hum=True)
sh(47, "Still, obeying her mother, Maura set off towards the kitchen. Jaleel came along behind her,",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)])
sh(48, "gazing without blinking at the orange dress Maura was wearing. Entering the kitchen, Maura showed him the sink.")
sh(49, "As soon as she stepped away from the sink, Jaleel began washing his hands. Just as he finished, Maura took two or three tissues from the table, came and held them out.",
   [("pour", "ދޮންނަން", -24), ("cloth_rustle", "ޓީޝޫ", -24)])
sh(50, "And she stopped a little distance away with her head bowed. Wiping off the water with the tissues, Jaleel looked at Maura.")
sh(51, "Seeing Maura from so near stirred indescribable feelings in Jaleel's heart. How well that orange dress suits Maura, Jaleel found himself thinking.")
sh(52, "Since the dress came only to her ankles, a little of Maura's fair feet could be seen. \"What is your name...?\"")
sh(53, "Jaleel asked, as gently as he possibly could. His heart was desperate to learn that beautiful fairy's name. It compelled him. \"Maura...\"",
   [("heartbeat", "ތެޅިފޮޅި", -22)])
sh(54, "Maura said, standing with her head bowed in shyness. \"Maura...\" Jaleel repeated, as if savouring it.")
sh(55, "Then, putting both hands into the pockets of his black trousers, Jaleel took a step towards Maura. \"A very beautiful name...\"",
   [("cloth_rustle", "ޖީބަށް", -24)])
sh(56, "Hearing Jaleel's compliment, Maura raised her head and looked at him in surprise. \"You're even more beautiful...\" Jaleel said, meeting her eyes.")
sh(57, "This time Maura truly blushed. With a faint smile on her lips she lowered her head, not daring to meet Jaleel's eyes.", hum=True)
sh(58, "\"Shyness is an even more beautiful quality...\" Jaleel complimented her a second time. Maura swayed like a flower wilting with shyness.")
sh(59, "Maura felt she could sink into the ground from shyness. \"I like it very much...\" Jaleel said, in a way that carried two meanings.")
sh(60, "Maura couldn't tell for sure whether Jaleel meant he liked the quality of shyness, or that he liked Maura.")
sh(61, "Maura looked at him, brows drawn together in question. But without another word Jaleel went out the door, leaving some kind of stir in Maura's young heart.",
   [("footsteps_sand", "ނިކުމެގެން", -24)])
sh(62, "Having stirred sweet, sweet feelings in her heart. Maura had seen men in Malé and in other places too. And she had male friends as well.")
sh(63, "But she had never met anyone who could cast a spell like the one Jaleel had cast. Why Maura's young,")
sh(64, "inexperienced heart should give itself to such a respected man, Maura herself could not understand. All she knew was that in the heart of Maura, who did not know what love was and had never known it, Jaleel's name was settling in without her choosing. To be continued.",
   hum=True)
SHOTS = S

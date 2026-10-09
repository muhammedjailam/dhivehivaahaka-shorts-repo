"""Beat/shot plan for Isq episode 393 (used by plan_beats.py)."""

LOC = {
    "maura_room": "Maura's upstairs bedroom in her family's two-storey pale onion-pink house on a small Maldivian local island: pale-green and pale-grey walls, a white queen bed, a white four-door wardrobe, a white dressing table, a small side table, and a glass balcony door with a white curtain opening onto a small balcony with a white railing that faces the sandy street",
    "maura_balcony": "the small balcony of Maura's upstairs bedroom with a white railing and a glass balcony door with a white curtain, on her family's two-storey pale onion-pink house with magenta bougainvillea spilling over the coral-stone wall below; across the sandy street, lit by streetlamps, stands the island's best guest house, a modern two-storey white building with dark-wood balconies",
    "guest_balcony": "the balcony of Jaleel's room in the island's best guest house, a modern two-storey white building with dark-wood balconies, a dark railing and a cream curtain at the open balcony door, directly across a sandy street lit by streetlamps from Maura's two-storey pale onion-pink house with magenta bougainvillea and her small white-railed balcony with a white curtain",
    "jaleel_room": "Jaleel's room in the island guest house: a modern room with white walls and dark-wood furniture, the open balcony door with a cream curtain looking across the sandy street at Maura's two-storey pale onion-pink house and her small white-railed balcony with a white curtain",
    "across_view": "the view at night from the dark guest-house balcony across the sandy street lit by streetlamps: Maura's two-storey pale onion-pink house with magenta bougainvillea spilling over the coral-stone wall and the white gate, and upstairs her small balcony with a white railing and an open glass balcony door with a white curtain drawn half aside, her softly lit bedroom (pale-green walls, a white queen bed) visible beyond it",
    "noon_lane": "a white sandy lane on the small Maldivian local island, low coral-stone walls with magenta bougainvillea, palms and a breadfruit tree, the white gate of Nafeesa's house two doors down from Maura's pale onion-pink house",
    "nafeesa_kitchen": "Nafeesa's simple island kitchen: a sink under a small window, a small white fridge, a wooden table, a little door looking out to the sandy courtyard and the gate, plain pastel walls",
    "nafeesa_courtyard": "Nafeesa's open sandy courtyard two doors down from Maura's house: a long wooden table with plastic chairs, a wooden joali seat under a breadfruit tree, a coral-stone wall with a white gate, a palm, the house's open doorway and a little kitchen door at one side",
    "sunset_memory": "Maura's small upstairs balcony with a white railing and a white curtain on her family's pale onion-pink house with magenta bougainvillea, seen from the dark-wood guest-house balcony across the sandy street",
}
MOOD = {
    "maura_room": "2 a.m., deep night, a dim warm bedside lamp and silver moonlight through the white curtain, velvety shadows, quiet and sleepless, tender longing",
    "maura_balcony": "2 a.m., deep night, a bright near-full moon, warm amber streetlamps glowing on the sandy street, the guest house's lights spilling across, velvety blue shadows, hushed and romantic",
    "guest_balcony": "2 a.m., deep night, warm amber streetlamp light from below and the cool glow of moonlight, velvety shadows, quiet and charged",
    "jaleel_room": "2 a.m., deep night, the room light switched off, only faint amber streetlamp light and moonlight through the gap in the cream curtain falling across his face, velvety darkness, secret and tender",
    "across_view": "2 a.m., deep night, the dark street with warm amber streetlamps, a near-full moon, her room glowing softly with a dim lamp and the pale bluish light of a laptop, peaceful and intimate from afar",
    "noon_lane": "scorching noon, blazing white tropical sun high overhead, harsh short shadows, shimmering heat haze over the white sand, glaring bright",
    "nafeesa_kitchen": "noon, bright hot daylight pouring through the small window and the little door, warm golden reflections, soft cooler shade inside",
    "nafeesa_courtyard": "scorching noon, blazing tropical sun on the white sand, dappled shade under the breadfruit tree, warm luminous colours",
    "sunset_memory": "memory of yesterday's sunset, fiery red and orange clouds over the island, warm golden-rose light, a soft dreamy haze",
}

ML = ("Maura wearing a loose long-sleeved ankle-length soft-lilac home dress (instead of her white lace dress) and a plain "
      "white hijab wrapped snugly and fully covering her hair and neck, no flower")
JN = ("Jaleel wearing a plain dull-grey T-shirt and long dark trousers (instead of his suit; no jacket, no tie), his black "
      "hair swept back")
JD = ("Jaleel wearing a crisp white long-sleeved shirt (instead of his suit; no jacket, no tie), black jeans, his black hair "
      "slicked straight back")
MD = "Maura in her white long-sleeved lace dress and white hijab fully covering her hair and neck, a small white frangipani pinned on the hijab"
LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear arm's-length gap between them"
MEN = "a few Maldivian men of different ages in plain short- and long-sleeved shirts and trousers (island officials and Malé guests)"

BEATS = [
    # ---------------- 2 A.M., THE FACING BALCONIES
    dict(to=6, reason="episode opening: 2 a.m., Maura sleepless in her room, sits up and drinks water, checks the time",
         chars=["maura"], loc="maura_room",
         visual=f"{ML}, sitting upright on the edge of her white bed with her feet on the floor, holding a small water bottle in both hands, gazing dreamily into space with a soft thoughtful face; her phone glowing face-down on the white side table beside her; the glass balcony door with its white curtain behind her",
         camera=f"medium shot, eye level, {LOW} (pale floor in soft shadow)", amb="room_night",
         sens="other", safe="the narration's tossing in bed is shown with her sitting upright on the edge of the bed, fully dressed in a hijab"),
    dict(to=8, reason="action change: she draws back the white curtain and looks out at the lamplit street and the guest house",
         chars=["maura"], loc="maura_room",
         visual=f"{ML}, standing at the glass balcony door and drawing the white curtain aside with one hand, seen from inside the dim room over her shoulder in soft profile, looking out at the sandy street glowing under amber streetlamps and the white two-storey guest house with dark-wood balconies directly across the street, one of its windows lit",
         camera=f"medium shot from behind her shoulder, eye level, {LOW} (dark floor and the hem of the curtain)", amb="balcony_night"),
    dict(to=12, reason="character enters: Jaleel steps out on the guest-house balcony frowning at his phone",
         chars=["jaleel"], loc="guest_balcony",
         visual=f"{JN}, standing at the dark railing of the guest-house balcony with one hand resting on the railing and the other holding his phone, frowning down at it with deep lines on his forehead, stern and absorbed; the phone is seen from the back with only a soft glow on his face; the cream curtain stirring at the open door behind him; his hands hold nothing else",
         camera=f"medium shot from across the street at a slight upward angle, {LOW} (the dark railing and the wall below in soft shadow)",
         amb="balcony_night", sens="other",
         safe="the narration's cigarette and smoke are not shown: one hand on the railing, the other holding his phone; the knee shorts are shown as long dark trousers"),
    dict(to=15, reason="character/action change: Maura hides behind the curtain, then peeks out at him and smiles",
         chars=["maura"], loc="maura_balcony",
         visual=f"{ML}, half-hidden behind the edge of the white curtain at her glass balcony door, peeking out shyly with one eye and half her face, fingers holding the curtain edge, a sweet involuntary smile on her lips, her cheeks faintly blushing in the amber streetlamp light",
         camera=f"medium close-up from the balcony side, eye level, {LOW} (the white curtain folds in soft shadow)", amb="room_night"),
    dict(to=17, reason="back to her view of him: his firm stance on the balcony", reuse="beat_003", chars=["jaleel"], loc="guest_balcony",
         visual="reuse of beat_003", amb="balcony_night"),
    dict(to=19, reason="action change: he suddenly looks up; startled, she lets go of the curtain and hides against the wall",
         chars=["maura"], loc="maura_room",
         visual=f"{ML}, standing pressed flat against the pale-green wall inside her dim room right beside the glass balcony door, one hand pressed to her chest, eyes wide and startled, lips parted, holding her breath; the white curtain still swaying beside her",
         camera=f"medium shot, eye level, {LOW} (dark floor)", amb="room_night"),
    dict(to=21, reason="POV change: Jaleel notices a fold of her dress beside the curtain and smiles",
         chars=["jaleel"], loc="guest_balcony",
         visual=f"{JN}, standing at the dark railing of his balcony seen over his shoulder and in three-quarter profile, looking across the lamplit street at Maura's pale-pink house: on her small white-railed balcony the white curtain hangs at the glass door and only a small fold of a soft-lilac dress shows at its edge; a faint amused smile breaking his stern face; no person visible on her balcony",
         camera=f"over-the-shoulder medium shot, eye level, {LOW} (the dark railing and the street below in shadow)",
         amb="balcony_night", sens="other", safe="secret watching shown with dignity: his face of quiet amusement, her house far away, nothing of her but a fold of fabric"),
    dict(to=23, reason="action change: he goes inside, draws the curtain, switches off the light and waits in the dark",
         chars=["jaleel"], loc="jaleel_room",
         visual=f"{JN}, standing in his darkened guest-house room just behind the drawn cream curtain, holding its edge slightly open with two fingers and looking out through the narrow gap, a thin stripe of amber streetlamp light falling across his eyes and face, the rest of the room in velvety darkness",
         camera=f"medium close-up from inside the room, eye level, {LOW} (the dark folds of the curtain)", amb="room_night"),
    dict(to=24, reason="back to her: the curtain lifts and her face peeks out", reuse="beat_004", chars=["maura"], loc="maura_balcony",
         visual="reuse of beat_004", amb="room_night"),
    dict(to=27, reason="action change: she steps out onto the balcony and looks at his dark room, disappointed",
         chars=["maura"], loc="maura_balcony",
         visual=f"{ML}, standing alone on her small balcony with both hands on the white railing, looking across the street towards the dark guest-house balcony with a small disappointed pout and lowered eyebrows; a near-full moon in the night sky above, magenta bougainvillea below; the guest-house balcony across the street is dark, empty and unlit, with no person on it; she is the only person in the image",
         camera=f"medium shot from across the street at a slight upward angle, {LOW} (the white railing and the pink wall below in soft shadow)",
         amb="balcony_night"),
    dict(to=30, reason="scene change: from his dark balcony he watches her inside her room with her laptop and chips",
         chars=["maura"], loc="across_view",
         visual=f"a distant view across the dark street into Maura's softly lit bedroom through her open balcony doorway: small in the distance, {ML}, sitting upright cross-legged on her white bed with an open laptop on her knees and a packet of chips beside her, the laptop's pale glow lighting her smiling face; the dark edge of a cream curtain in the near foreground; nobody else in view",
         camera=f"wide shot from across the street, eye level, the lit balcony doorway in the upper half, {LOW} (the dark street and the pink wall below)",
         amb="balcony_night", sens="other",
         safe="her room is seen only at a distance through the balcony doorway; she sits upright, fully dressed in a hijab, never lying down; the laptop screen is not readable"),
    dict(to=33, reason="emotional turning point: for the first time Jaleel feels peace", chars=["jaleel"], loc="jaleel_room",
         visual=f"close-up of {JN}, standing in the dark beside the cream curtain, his stern face softened into rare calm, a faint peaceful smile, his eyes gentle and far away, a soft stripe of warm light from across the street on his face",
         camera=f"close-up, eye level, {LOW} (soft dark curtain folds)", amb="room_night"),
    # ---------------- SCORCHING NOON, NAFEESA'S HOUSE
    dict(to=35, reason="time and scene change: scorching noon; Maura walks to Nafeesa's house with the juice jug",
         chars=["maura"], loc="noon_lane",
         visual=f"{MD}, walking along the edge of the sun-scorched white sandy lane, carrying a big five-litre plastic jug of bright red watermelon juice in both hands, squinting slightly in the blazing sun, heading towards the white gate of Nafeesa's house; heat haze shimmering over the empty lane",
         camera=f"medium wide shot, eye level, {LOW} (glaring white sand with short shadows)", amb="island_day", transition="black"),
    dict(to=39, reason="scene change: Nafeesa's kitchen; Maura sets down the jug and pours the juice into crystal glasses",
         chars=["maura", "nafeesa"], loc="nafeesa_kitchen",
         visual=f"{MD}, standing at the kitchen table pouring bright red watermelon juice from the big five-litre jug into a row of sparkling crystal glasses on a tray, smiling; Nafeesa beside the sink turning towards her mid-chat, holding two more crystal glasses, lively and hurried",
         camera=f"medium shot, eye level, {LOW} (the table top with the tray of glasses)", amb="home_day"),
    dict(to=42, reason="characters enter: through the little kitchen door Maura sees men arriving, Jaleel among them",
         chars=["maura", "jaleel"], loc="nafeesa_courtyard",
         visual=f"seen past {MD}, who peeks shyly out of the little kitchen door in the near foreground at the right edge, her face in soft profile: across the sunny sandy courtyard the white gate stands open and {MEN} walk in; at their front, far from her, {JD} and black sunglasses, walking tall with his hands in his pockets; {GAP}, the whole courtyard between them",
         camera=f"medium wide shot from inside the kitchen doorway, eye level, {LOW} (bright sand of the courtyard)", amb="garden_day"),
    dict(to=44, reason="action change: she comes out with the tray and shyly hands out the juice; her hand trembles at Jaleel",
         chars=["maura", "jaleel"], loc="nafeesa_courtyard",
         visual=f"in the shady courtyard {MEN} sit on plastic chairs at the long wooden table holding glasses of red juice; {MD}, walking shyly with a tray of crystal glasses of watermelon juice, eyes lowered, cheeks blushing, approaching {JD}, who sits on the wooden joali with his black sunglasses pushed up on his head, watching her; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (sandy ground in dappled shade)", amb="garden_day"),
    dict(to=47, reason="action change: the glass tips and juice splashes on his shirt; everyone is shocked",
         chars=["maura", "jaleel"], loc="nafeesa_courtyard",
         visual=f"{JD}, seated on the wooden joali, glancing calmly down at a bright pink-red splash of watermelon juice on his white shirt sleeve and shirt front; {MD}, standing a step away holding the tray with one glass tipped over on it, one hand at her mouth, eyes wide with horror; the seated men in the background half-rising in surprise; {GAP}",
         camera=f"medium shot, eye level, {LOW} (sandy ground in dappled shade)", amb="garden_day",
         sens="other", safe="the juice spills on his shirt sleeve and front only, nothing at his lap (the narration says lap); no contact"),
    dict(to=49, reason="framing change: no anger on his face, only a sharp meaningful gaze; the guests exchange looks",
         chars=["jaleel"], loc="nafeesa_courtyard",
         visual=f"close-up of {JD}, his black sunglasses in one hand, a faint pink juice stain on his white shirt front, looking up with calm, sharp, meaningful eyes and not the slightest displeasure; behind him, softly out of focus, two seated men glancing at each other in disbelief",
         camera=f"close-up, eye level, {LOW} (his stained white shirt front in soft focus)", amb="garden_day"),
    dict(to=51, reason="scene change: in the kitchen she shows him the sink and hurries to fetch tissues from the top of the fridge",
         chars=["maura", "jaleel"], loc="nafeesa_kitchen",
         visual=f"{JD} with a faint pink juice stain on the shirt front and sleeve, standing at the kitchen sink rinsing his sleeve, his sunglasses tucked in his shirt pocket; across the kitchen {MD}, reaching up on tiptoe to take a tissue packet from the top of the small white fridge; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (plain kitchen floor)", amb="home_day"),
    dict(to=53, reason="framing change: he looks deeply at her anxious, radiant face", chars=["maura"], loc="nafeesa_kitchen",
         visual=f"close-up of {MD}, looking down anxiously, holding a few white tissues out at arm's length in both hands, lips pressed together, her fair face glowing radiant and lovely in the bright window light",
         camera=f"close-up from slightly above (his height), {LOW} (the tissues and her hands in soft focus)", amb="home_day"),
    dict(to=57, reason="action change: he wipes his hands and reassures her; she looks up guiltily; he asks her name",
         chars=["jaleel", "maura"], loc="nafeesa_kitchen",
         visual=f"{JD} with a faint pink juice stain on the shirt front, standing beside the sink wiping his hands with white tissues, looking down at her with a gentle reassuring face; {MD}, standing a respectful distance away by the fridge with her hands clasped, looking up at him guiltily; {GAP}",
         camera=f"medium two-shot from the side, eye level, {LOW} (plain kitchen floor)", amb="home_day",
         sens="other", safe="'he took a step closer' is kept at a clear arm's-length gap; no contact"),
    dict(to=58, reason="emotional turning point: he asks her forgiveness; she stares wide-eyed in astonishment",
         chars=["maura"], loc="nafeesa_kitchen",
         visual=f"close-up of {MD}, looking up with wide astonished eyes and parted lips, a faint blush on her cheeks, completely at a loss for words",
         camera=f"close-up, eye level, {LOW} (soft blurred kitchen behind)", amb="home_day"),
    dict(to=60, reason="framing change: Jaleel confesses he photographed her without permission", chars=["jaleel"], loc="nafeesa_kitchen",
         visual=f"close-up of {JD}, standing in the bright kitchen, his black sunglasses in one hand, speaking earnestly and quietly with a softened, honest, slightly guilty look, a faint pink juice stain on his white shirt front; he is alone in the frame, no other person and no foreground figure, the plain kitchen softly blurred behind him",
         camera=f"close-up, eye level, {LOW} (his white shirt in soft focus)", amb="home_day"),
    dict(to=62, reason="memory: yesterday's sunset on the balcony when he took her photo", chars=["maura"], loc="sunset_memory",
         visual="far across the sandy street at sunset, on her small white-railed balcony, Maura in a loose long-sleeved ankle-length orange dress (instead of her white dress) and a white hijab fully covering her hair and neck with a small white frangipani pinned at its side, holding up her phone to photograph the fiery red clouds, small in the distance; in the near foreground a man's hand holds a phone seen only from its plain dark back, its screen not visible",
         camera="wide shot from across the street, eye level, the balcony and the red sky in the upper two-thirds, the dark-wood railing of the guest-house balcony as the calm lower third",
         amb="memory", transition="dissolve", sens="other",
         safe="the secret photo is shown with dignity: her figure small and far away, only the dark back of his phone, no screen"),
    dict(to=64, reason="back to the kitchen: she stands stunned as a sweet feeling takes root", reuse="beat_022", chars=["maura"],
         loc="nafeesa_kitchen", visual="reuse of beat_022", amb="home_day", transition="dissolve"),
    dict(to=67, reason="action change: hands in his pockets, he asks to tell her something very big",
         chars=["jaleel", "maura"], loc="nafeesa_kitchen",
         visual=f"{JD} with a faint pink juice stain on the shirt front, standing tall by the sink with both hands in his pockets, looking at her with serious, intense, gentle eyes as he speaks; {MD}, standing a respectful distance away by the fridge, holding the crumpled tissues, looking up at him uncertainly; {GAP}",
         camera=f"medium two-shot from the side, eye level, {LOW} (plain kitchen floor)", amb="home_day"),
    dict(to=69, reason="cliffhanger: her mind fills with unanswered questions", reuse="beat_022", chars=["maura"],
         loc="nafeesa_kitchen", visual="reuse of beat_022", amb="home_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Maura had seen men in Malé and in other places too. And she had male friends as well.")
sh(2, "But she had never met anyone who could cast a spell like the one Jaleel had cast. Why she should give her young,")
sh(3, "inexperienced heart to such an honourable gentleman, even Maura could not understand.")
sh(4, "But what she did know was that in Maura's heart, which did not know what love was and had never experienced it, Jaleel's name was being engraved beyond her control.")
sh(5, "Tossing and turning from side to side, unable to sleep, Maura got up and sat on the bed. Letting a deep breath out into the air, she picked up the water bottle on the side table and drank.",
   [("breath", "ނޭވާއެއް", -22)])
sh(6, "With no sleep coming to her eyes, she picked up her phone and checked the time. It was just turning two in the morning. Who knows what came over her.")
sh(7, "Even in the darkness of the night, Maura suddenly wanted to step out onto the balcony. Getting up from the bed, she drew back the white curtain hanging at the balcony door and looked outside.",
   [("cloth_rustle", "ކަހައިލުމާއިއެކު", -20)])
sh(8, "The streetlamps along the road lit the street well enough. And with the light from the guest house opposite, the whole surroundings looked bright even at this hour of the night.")
sh(9, "Suddenly the door of the guest house opposite slid open, and the one she saw step out was Jaleel.",
   [("door_open", "ކަހައިލުމާއިއެކު", -22)])
sh(10, "Wearing a dull-coloured T-shirt and black shorts reaching just below his knees, looking at his phone, holding a cigarette in one hand, he came out")
sh(11, "and stopped, resting his hand on the railing. From the lines crowding his forehead, it seemed he was looking at something very important on his phone.")
sh(12, "Every now and then he drew on the cigarette in his hand and blew its smoke out into the air.")
sh(13, "Maura shrank back and hid behind the curtain at the balcony door. At that moment she did not want Jaleel to know she was there.",
   [("cloth_rustle", "ފިލިއެވެ", -22)])
sh(14, "But drawing the curtain aside a little, Maura kept watching Jaleel. As she watched, a lovely smile spread on Maura's lips without her meaning it.")
sh(15, "Why she wanted to keep looking more and more, she did not know. Maura's young heart surrendered to that charming sight. Her heart began to praise that manliness.",
   hum=True)
sh(16, "His firm way of standing there carved itself even deeper into Maura's innocent heart.")
sh(17, "Jaleel must be a handsome man full of manliness. That a man's greatest manliness is firmness, Maura's young,")
sh(18, "inexperienced heart agreed for the first time. Suddenly Jaleel looked straight ahead. Startled by his sudden move, Maura let go of the curtain and hid against the wall.",
   [("gasp", "ސިހިފައި", -20), ("cloth_rustle", "ދޫކޮށްލެވުމާއިއެކު", -22)])
sh(19, "In her alarm her hand went to her chest. In her heart she prayed that Jaleel would not suspect she was there.",
   [("heartbeat", "މޭގައި", -20)])
sh(20, "But it was certain to Jaleel that Maura was there. A smile ran over his lips when, as she stood hidden against the wall, he saw a little of Maura's dress beside the balcony curtain.")
sh(21, "\"So she was watching secretly,\" Jaleel thought. Seeing that innocence made him want to laugh. A longing to see Maura began to stir in his heart.")
sh(22, "But Jaleel knew that Maura would not come out while he stood there. So, pretending nothing had happened, he went inside the room.",
   [("footsteps_pavement", "ވަނެވެ", -24)])
sh(23, "Drawing the curtain at the balcony door, he switched off the room's light too. Then, very secretly, Jaleel stood waiting for the moment Maura would come out.",
   [("cloth_rustle", "ދަމައިލުމާއިއެކު", -22), ("lock_click", "ނިއްވައިލައިފިއެވެ", -22)])
sh(24, "The curtain at the balcony door of the house opposite lifted a little. Through that narrow gap Jaleel saw Maura's fair face, like the full moon of the fourteenth night shining in a pitch-dark night.",
   [("cloth_rustle", "ހިއްލުނެވެ", -24)], hum=True)
sh(25, "At that very moment, beyond his control, the sight took root in Jaleel's heart. Secretly looking both ways, Maura came out from under the curtain.")
sh(26, "And Jaleel also saw her look towards his room opposite. Jaleel saw the signs of disappointment on Maura's face.",
   [("sigh", "މާޔޫސްކަމުގެ", -22)])
sh(27, "From that, Jaleel knew he was not the only one who had wanted to see. Why a sweetness ran through his heart, Jaleel could not understand.")
sh(28, "Jaleel stood watching Maura's movements without tiring. Now and then Maura would check her phone. Or she might lie on the bed in her room.")
sh(29, "Once he even saw her leave the room and come back with a packet of chips. Opening her laptop, she put on a film.")
sh(30, "In Maura's dimly lit room, Maura's face began to show beautifully in the light from the laptop. To Jaleel it was a sight he could never tire of.")
sh(31, "Jaleel, who had always been busy with business without rest, felt for the first time something like finding peace.")
sh(32, "His mind was growing lighter. His heart was finding ease. He was giving Maura an attention he had never given any girl before, not even his own wife.",
   [("breath", "ލުއިވަމުން", -24)], hum=True)
sh(33, "In Jaleel's heart a place was being cleared for Maura. Like a line carved into stone, Maura's name was being engraved in Jaleel's heart.")
sh(34, "It was the hot hour of noon. The streets lay in a gloom under the blazing sun. The sun was so fierce you could not open your eyes, and the scorching heat felt as if it would roast a person.")
sh(35, "Walking along one side of the street, Maura came into Nafeesa's house. Carrying the five-litre jug of watermelon juice in her hands, Maura headed straight for Nafeesa's kitchen.",
   [("footsteps_sand", "ހިނގަމުން", -22)])
sh(36, "\"Nafeesaththa... here's the juice jug Mum sent...\" Maura said, calling to Nafeesa at the sink as she set the jug down on the table.",
   [("soft_thud", "ބަހައްޓަމުން", -22)])
sh(37, "\"Oh... you've come? Pour the juice into the glasses for me, would you... They'll be arriving any moment now...")
sh(38, "Lamha was here too, I don't know where she's gone off to now...\" Nafeesa said, hurrying as she took out the crystal glasses. \"No problem...",
   [("cup_clatter", "ބިއްލޫރި", -22)])
sh(39, "If Nafeesaththa asks, I'll do that too...\" Smiling, Maura began pouring the juice into the glasses.",
   [("pour", "އަޅަން", -18)])
sh(40, "Just as she finished pouring juice into every glass, she heard the gate open and some people come in. When Maura looked towards the gate through the small kitchen door, she saw a crowd coming in through the gate.",
   [("door_open", "ހުޅުވާފައި", -22), ("footsteps_sand", "ވަދެގެން", -22)])
sh(41, "Among them, the one who caught Maura's eye was Jaleel, in a white shirt and black jeans.")
sh(42, "With his hair slicked straight back and the black sunglasses he wore, his good looks and manliness stood out.")
sh(43, "Her throat going dry at the sight, she swallowed, took the glasses of juice on a tray and came out to the middle yard.",
   [("cup_clatter", "ތަބަށް", -22)])
sh(44, "Very shyly she held out a glass of juice to each person in turn. When she reached Jaleel, Maura's hand was trembling badly.")
sh(45, "Because of that, Maura had to face something so embarrassing a person could die of shame. \"Sorry, sorry...\"",
   [("gasp", "ސޮރީ", -20)])
sh(46, "Maura blurted with wide eyes, seeing the glass of juice spilled onto Jaleel's lap. Everyone's reactions made it clear that it had shocked everyone there.",
   [("splash", "ބަންޑުންވި", -18), ("crowd_gasp", "ސިހިގެންދިޔަވަރުގެ", -22)], hum=True)
sh(47, "Maura thought she would have to face Jaleel's anger. \"It's nothing...\" Jaleel said, contrary to what she expected.")
sh(48, "There was no displeasure at all on his face. But his sharp gaze was looking at Maura in a meaningful way.")
sh(49, "The others there glanced at each other as if they could not believe it. It seemed like something happening for the first time. \"Shall we go to the sink so you can wash it...\"")
sh(50, "Maura offered first, taking responsibility for her mistake. Jaleel rose very easily from the joali, came after Maura and went into the kitchen.",
   [("footsteps_sand", "ތެދުވެގެން", -24)])
sh(51, "Showing Jaleel the sink, Maura hurried to bring tissues from the tissue packet on top of the fridge.",
   [("paper_shuffle", "ޓިޝޫ", -22)])
sh(52, "After cleaning off the juice he saw on his shirt, Jaleel turned towards Maura. Jaleel looked deeply at the anxious face of the girl, who stood shorter than him.")
sh(53, "Like the full moon that lights the night, that face was radiant and beautiful. There was something in that face one could never tire of looking at.",
   hum=True)
sh(54, "Taking the tissues Maura held out and wiping his hands, Jaleel took a step closer to Maura. \"That's nothing...\"",
   [("paper_shuffle", "ފޮހެލަމުން", -22)])
sh(55, "Jaleel tried to ease Maura's anxiety. Maura looked at Jaleel like a guilty person. \"Your shirt got dirty because of me, didn't it...?\"")
sh(56, "Maura said. \"That's nothing... these things happen...\" Jaleel said. \"You said your name is Maura, right...\" Jaleel changed the subject.")
sh(57, "Slowly Maura nodded. \"Without Maura's permission I have done something too... Will you forgive me...?\"")
sh(58, "When Jaleel said something so astonishing, Maura looked at him with wide eyes. Could an honourable gentleman like Jaleel have done something for which he had to ask forgiveness of an ordinary girl like Maura?")
sh(59, "\"What is it...?\" Maura asked. \"Without Maura's permission, I took a photo of Maura...\" Jaleel said.")
sh(60, "Questions rising, Maura stood still once again. Why would a gentleman like Jaleel take a photo of an ordinary girl like Maura?")
sh(61, "What was so special about Maura? \"Yesterday, as the sun was setting, when you were on the balcony...\" Jaleel explained further. \"I hope you'll forgive me...")
sh(62, "But I took it because I truly wanted to...\" Maura stood amazed at Jaleel's words.",
   [("camera_shutter", "ނެގުނީ", -20)])
sh(63, "At the same time, an indescribable sweet feeling was taking root in Maura's heart at Jaleel's words. Her heart felt strange.",
   [("heartbeat", "ހިތުގައި", -22)], hum=True)
sh(64, "Receiving the attention of a gentleman like Jaleel, she began to feel in a way she could not explain. But no words came to Maura's tongue.")
sh(65, "\"Maybe it was luck that this juice glass spilled... Otherwise I'd never have had the chance to talk with Maura like this...\" Jaleel said.")
sh(66, "Maura noticed the closeness in the voice of Jaleel, who always spoke harshly to people. \"Maura... I have something very big I need to tell you...")
sh(67, "Will you give me the chance to tell it...?\" Jaleel said, putting both hands in his pockets. Maura stood not knowing what to say.",
   [("cloth_rustle", "ޖީބަށް", -24)])
sh(68, "What big thing could a gentleman like Jaleel have to say to an ordinary girl like Maura?")
sh(69, "Maura's mind kept filling with unanswered questions. To be continued.", hum=True)
SHOTS = S

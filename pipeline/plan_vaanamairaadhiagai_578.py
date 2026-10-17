"""Beat/shot plan for Vaanama Iraadhiagai episode 578 (used by plan_beats.py). ANIME look (series style.txt)."""

LOC = {
    "living": "the bright simple sitting room of a small single-storey Maldivian island house, whitewashed coral-stone walls, a cushioned wooden sofa with pastel cushions, a woven mat on a cool tiled floor, a ceiling fan, a wooden front door and an open window looking onto coconut palms",
    "bedroom": "Luyoon's small tidy bedroom in a Maldivian island house, whitewashed walls, a neatly made single bed, a small wooden desk, an open window with a light curtain looking out on palm fronds and a coral-stone garden wall",
    "lane": "a quiet white coral-sand lane on a small Maldivian island, coral-stone garden walls, tin-roofed houses, coconut palms and breadfruit trees, glimpses of the turquoise lagoon at the end of the lane",
    "veranda": "the small shaded front veranda and open wooden front door of a single-storey Maldivian island house, a low coral-stone garden wall, potted plants, a sandy yard with a palm tree, a motorbike parked by the gate",
    "collapse": "the cool tiled floor just inside the open front door of a small Maldivian island house, bright daylight spilling in from the veranda",
    "hospital": "a clean bright room of a small island hospital in the Maldives, a single hospital bed with white sheets, a drip stand, pale mint-green walls, a large window with coconut palms and blue sky outside",
    "park": "a small green island park in the Maldives with swings, a slide, shady trees, coconut palms, white coral-sand paths and wooden benches, the turquoise lagoon sparkling beyond a low seawall",
    "kitchen": "the small family kitchen and dining corner of a Maldivian island house, a wooden dining table with a breakfast of roshi flatbread, mas huni, tea cups and a teapot, a window with morning sun and palm leaves",
    "school_lane": "a sunny coral-sand lane leading to the low white wall and open gate of a small Maldivian island school, coconut palms, flowering bougainvillea over coral-stone walls, no signs",
    "maaniu_office": "the entrance hall of a modern state-company office on a Maldivian island, glass doors, potted palms, a small fingerprint attendance device on the wall beside the door showing only a soft blank glow",
    "office": "a bright small health-sector office on a Maldivian island, a tidy desk with a computer turned away from the viewer, files in neat stacks, a potted plant, a window with palm trees and blue sky",
    "restaurant": "a small airy island restaurant in the Maldives with wooden tables, rattan chairs, potted plants, wide open windows onto a sunny lane with a motorbike parked outside and the turquoise lagoon beyond",
}
MOOD = {
    "living": "bright late morning, soft daylight through the window, cool shadows indoors, worried and tender anime drama",
    "bedroom": "bright late morning, soft white light through the curtain, sorrowful and lonely, anime tears glistening",
    "lane": "bright late morning, dazzling sun on white sand, deep blue sky with drifting clouds, urgent and hopeful",
    "veranda": "bright late morning, strong sunlight outside and cool shade on the veranda, tense, emotional, anime tears shining",
    "collapse": "bright late morning light turning dim and blurry, a dark soft vignette closing in, dizzy and dreamlike",
    "hospital": "soft calm daylight, gentle white and mint light, quiet and tender relief",
    "park": "golden afternoon, warm low sunlight, long soft shadows, sparkling lagoon, lens glow, warm and joyful",
    "kitchen": "bright early morning, fresh golden sunbeams through the window, steam rising from tea cups, a new beginning",
    "school_lane": "bright early morning, crisp sunlight and long shadows on white sand, fresh and cheerful",
    "maaniu_office": "bright early morning, cool clean light inside, busy and purposeful",
    "office": "bright midday, clean airy light, calm and content",
    "restaurant": "bright midday, warm airy light, sparkling lagoon in the background, gentle hopeful romance at a respectful distance",
}

BEATS = [
    dict(to=5, reason="episode opening: the mother questions her daughters about Luyoon's tears", chars=["aishath", "luyoon", "zaina"], loc="living",
         visual="Aishath standing in the sitting room with a worried, questioning anime face, one hand on her chest, looking at her two daughters; Luyoon sitting on the sofa with red puffy eyes and anime tears, looking down at her hands; Zaina standing beside the sofa with a nervous forced smile, waving her hand to say it is nothing",
         camera="medium wide three-shot, eye level", amb="home_day"),
    dict(to=7, reason="character focus change: Zaina alone on the sofa, sighing and worrying for her sister", chars=["zaina"], loc="living",
         visual="Zaina sitting alone on the cushioned sofa, leaning back and letting out a deep sigh, eyes half closed, gazing up thoughtfully toward the turning ceiling fan, her face full of worry for her sister; soft window light on one side of her face",
         camera="medium shot, slightly low angle", amb="home_day"),
    dict(to=11, reason="scene and character change: Luyoon alone in her room, the call from an unsaved number", chars=["luyoon"], loc="bedroom",
         visual="Luyoon sitting on the edge of her neatly made bed, fully dressed in her cream-white dress and black hijab, holding her phone to her ear with both hands, its back toward the viewer, anime tears streaming down her cheeks, eyes wide with hurt and surprise; light curtains moving in the window breeze",
         camera="medium close-up, eye level, from the side", amb="room_day",
         sens="other", safe="bedroom scene: she sits up on the bed edge fully dressed in her hijab; the phone screen is never visible"),
    dict(to=13, reason="scene and action change: Maaniu rides his motorbike to Luyoon's house", chars=["maaniu"], loc="lane",
         visual="Maaniu riding his motorbike ALONE along the bright white coral-sand lane toward the viewer, nobody behind him, leaning forward with a determined, sorrowful face, his curly hair blown by the wind, palms and coral walls streaming past, dust glittering in the sun",
         camera="dynamic low-angle wide shot, the lane as a calm lower third", amb="island_day"),
    dict(to=16, reason="location and character change: Zaina opens the door to Maaniu and confronts him", chars=["zaina", "maaniu"], loc="veranda",
         visual="Zaina standing in the half-open front doorway holding the door edge, frowning angrily with an anime anger look, about to close the door; Maaniu standing outside on the sunny veranda step a few steps away, one palm raised gently in a pleading gesture, eyes sad",
         camera="medium wide two-shot from the side, eye level", amb="island_house_day"),
    dict(to=19, reason="character enters: Luyoon comes to the door; Maaniu in tears asks her to listen", chars=["luyoon", "maaniu", "zaina"], loc="veranda",
         visual="Luyoon standing in the open doorway with Zaina just behind her shoulder, facing Maaniu who stands outside on the veranda an arm's length away and more; Maaniu with glistening anime tears gathering in his eyes, head bowed, hands open in apology; Luyoon's eyes wide and trembling; no touching",
         camera="medium two-shot over Zaina's shoulder, eye level", amb="island_house_day"),
    dict(to=22, reason="emotional turning point: Luyoon hears the truth, tears roll and her vision starts to darken", chars=["luyoon", "zaina"], loc="veranda",
         visual="dramatic anime close-up of Luyoon's face in the doorway, big glistening tears rolling down her cheeks, her eyes losing focus, the edges of the image softly blurring; she reaches one hand out toward Zaina beside her, who turns to her in alarm",
         camera="close-up on Luyoon's face, Zaina at the edge of frame", amb="island_house_day"),
    dict(to=23, reason="action change: the collapse, shown symbolically", loc="collapse",
         visual="a dropped phone lying on the cool tiled floor just inside the doorway, its screen dark, the bright doorway beyond tilted and blurred, a soft dark vignette closing in from the edges like fading consciousness; no people visible",
         camera="tilted low angle at floor level, dreamlike blur", amb="home_day", sens="other",
         safe="the fainting fall is never shown: a dropped phone and a tilted, darkening, blurred view"),
    dict(to=25, reason="scene and time change: Luyoon wakes in the island hospital", chars=["luyoon", "zaina", "aishath"], loc="hospital",
         visual="Luyoon sitting up in the hospital bed, propped on pillows, fully dressed in her cream-white dress and black hijab covering hair and neck, no shoulder bag, a white blanket over her legs, both hands bare and resting folded on the blanket with nothing attached to her hands or arms, a drip stand with a bag standing beside the bed (its tube hanging loose at the stand), looking weak and asking softly; Zaina sitting on a chair beside the bed answering gently, Aishath standing at the bedside with a relieved tender face; a doctor in a white coat as a small background figure at the door",
         camera="medium wide, eye level", amb="hospital_room", transition="black", sens="other",
         safe="hospital: fully dressed in hijab, sitting up, blanket over legs, drip line only, no needles in skin, no blood"),
    dict(to=28, reason="scene and time change: discharge afternoon at the park", chars=["luyoon", "aishath"], loc="park",
         visual="Luyoon and Aishath sitting together on a wooden park bench under a shady tree in golden afternoon light, Aishath leaning toward her daughter asking with a caring look, Luyoon smiling softly for the first time; small children playing on the swings and elderly people walking on the sand paths as small background figures in modest clothing",
         camera="medium wide shot, eye level", amb="garden_day", transition="black"),
    dict(to=30, reason="characters enter: Maaniu, Zaina and Nawfal arrive with drinks and snacks", chars=["maaniu", "zaina", "nawfal"], loc="park",
         visual="Maaniu, Zaina and the little boy Nawfal walking across the golden park toward the viewer, Maaniu and Zaina each holding a drink cup in both hands, Zaina also holding a small paper bag of snacks, Nawfal grinning beside them, sun glow behind them",
         camera="wide shot, low angle, figures in the upper half, sand path in the lower third", amb="garden_day"),
    dict(to=32, reason="action change: Maaniu offers her favourite vanilla milk; the family laughs together", chars=["luyoon", "maaniu", "aishath", "zaina"], loc="park",
         visual="the family gathered around a park picnic table in the warm golden light, laughing and joking: Luyoon on one side holding her own cup of vanilla milk with a happy smile, Maaniu standing across the table an arm's length away smiling at her, Aishath laughing beside Luyoon, Zaina opening the snacks; no touching",
         camera="medium wide group shot, eye level, the table top as the lower third", amb="garden_day"),
    dict(to=34, reason="time jump: the morning schools reopen, a new day at home", chars=["luyoon", "aishath", "zaina", "nawfal"], loc="kitchen",
         visual="a bright busy morning at the breakfast table: Aishath and Luyoon setting out tea and roshi together, Luyoon fresh and ready for work in her cream-white dress and black hijab, Zaina in a white hijab and plain blue school dress and Nawfal in a white school shirt grabbing breakfast before school",
         camera="medium wide shot, eye level", amb="kitchen_busy", transition="black"),
    dict(to=36, reason="location and character change: Luyoon walks her siblings to school while Naaifaa watches unhappily", chars=["luyoon", "zaina", "nawfal", "naaifaa"], loc="school_lane",
         visual="Luyoon walking cheerfully along the sunny coral-sand lane with Zaina and Nawfal in school clothes toward the school gate; in the background, Naaifaa half hidden behind a palm trunk, watching them with a sour, jealous frown",
         camera="wide shot, eye level, the lane forming the lower third", amb="village_day", sens="other",
         safe="Naaifaa's scheming shown only as a look from behind a palm"),
    dict(to=38, reason="action change: Naaifaa calls out to Luyoon, who ignores her and walks home", chars=["luyoon", "naaifaa"], loc="lane",
         visual="Luyoon walking calmly toward the viewer along the coral-sand lane with a serene face, eyes straight ahead, ignoring Naaifaa who stands behind her by a coral-stone wall, one hand raised calling out with an irritated face",
         camera="medium wide shot, Luyoon in the foreground, Naaifaa behind her", amb="village_day"),
    dict(to=41, reason="location and action change: after breakfast with her mother Luyoon phones Maaniu", chars=["luyoon", "aishath"], loc="kitchen",
         visual="Luyoon standing by the breakfast table with her brown shoulder bag on, holding her phone to her ear (back of the phone to the viewer) and glancing at her wrist with a smile; Aishath clearing the tea cups behind her and smiling",
         camera="medium shot, eye level", amb="home_day"),
    dict(to=43, reason="location and character change: Maaniu clocks in at work", chars=["maaniu"], loc="maaniu_office",
         visual="Maaniu in a plain light-blue work shirt pressing his finger to the small blank-glowing fingerprint device by the glass office door, his phone held to his ear in the other hand, smiling as he talks",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=46, reason="location and time change: Luyoon, healthy again, at her office break", chars=["luyoon"], loc="office",
         visual="Luyoon at her tidy office desk in a plain pastel office abaya and black hijab, a lanyard with a blank card around her neck, looking healthy and glowing, smiling as she takes her phone out of her brown bag; the computer screen turned away",
         camera="medium shot, eye level", amb="office_quiet"),
    dict(to=49, reason="location and action change: their first outing together since the breakup at a restaurant", chars=["luyoon", "maaniu"], loc="restaurant",
         visual="Luyoon and Maaniu sitting on opposite sides of a wooden restaurant table, an arm's length apart, both smiling shyly and talking about their dreams, each with their own glass of juice; Maaniu's motorbike parked outside the open window; a waiter in a white shirt as a small background figure walking away with a notepad",
         camera="medium two-shot from the side, the table top as the lower third", amb="cafe", sens="intimacy",
         safe="unmarried couple: opposite sides of a table, no touching; the motorbike ride is shown only as the parked bike (no pillion)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Child, are you hiding something? Don't lie, tell me!\" There was worry in Aishath's voice.")
sh(2, "Seeing the children she raised with love now full of tears, Aishath could not bear it. She wanted to know why so many days of dreams had lost their colour.")
sh(3, "\"Mamma, nothing's wrong...\" Luyoon's voice was full of sorrow and despair. She had asked Zeeniya not to let anyone know about all this.")
sh(4, "\"Is it true nothing has happened to dhonthi? I just heard you two talking... what was that about?\" said Aishath.")
sh(5, "But Zeeniya pretended she knew nothing about it, and said: \"Mamma, it's nothing... dhonthi is just a little upset...\"")
sh(6, "Saying this, Zeeniya walked toward the sitting room. After sitting down on the sofa she let out a deep breath, and thought to herself:",
   [("sigh", "ނޭވާ", -20)])
sh(7, "how will all this ever be put right? Dhonthi had so many hopes. But in a short moment those dreams...")
sh(8, "were scattered. That is the way of the world. Luyoon came to know that her life had been turned upside down in a short time because of someone.")
sh(9, "It was because of Naifa. Luyoon's phone started ringing. She looked to see who it was. The call was coming from a number not saved in her phone.",
   [("phone_buzz", "ރިންގް", -18)])
sh(10, "Luyoon never answered unsaved numbers. Two or three times the same number called. Luyoon answered. \"Hi Luyoon, this is Maaniu...")
sh(11, "I have something to tell you.\" There was pain in Maaniu's voice. \"After hurting my heart all these days, why are you calling today?\" Luyoon said, crying.",
   [("sob_breath", "ރޮމުން", -24)], hum=True)
sh(12, "\"Luyoon, I want to meet... to tell you how things went. I'm coming to your house.\" After saying this Maaniu hung up, got on his motorbike and rode toward Luyoon's house.",
   [("motorbike_pass", "ދުއްވާލީ", -18)])
sh(13, "It was to meet Luyoon. A while later, \"Assalaamu alaikum,\" Maaniu called out the greeting.")
sh(14, "Zaina, sitting in the sitting room, returned the greeting, got up from the sofa and went to open the door. When she opened it, it was Maaniu standing there.",
   [("door_open", "ހުޅުވާލިއިރު", -18)])
sh(15, "\"Why have you come to this house? Who are you looking for? What for?\" Zaina fired the questions all at once, because after doing that to Luyoon he had no reason to come here.")
sh(16, "And she tried to close the door. \"Zaina, wait. Is dhonthi here? I came to talk to dhonthi, to explain what happened...\" said Maaniu.",
   [("creak", "ލައްޕަން", -20)])
sh(17, "When that voice reached Luyoon's ears she walked quickly toward the front door. \"Maaniu, what happened, why have you come to this house today...",
   [("footsteps_pavement", "ހިގުމެއް", -22)])
sh(18, "\" Luyoon asked, uneasy. \"Luyoon, wait, please listen to this...\" Tears were gathering in Maaniu's eyes.", hum=True)
sh(19, "He was begging forgiveness for what he had done. Maaniu told her the whole story, word by word.")
sh(20, "The tears gathered in Luyoon's eyes rolled down her cheeks. It even felt as if her eyes were going dark.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(21, "But Luyoon tried hard not to show it. Maaniu had fallen into the trap someone set to separate or drive apart two people in love, and had drowned in it,")
sh(22, "and Luyoon was heartbroken. \"Zaina... something is happening to me... I need your help,\" Luyoon said softly.", hum=True)
sh(23, "Everything around Luyoon began to go dark in a strange way. When she came to, Luyoon had been admitted to the hospital. \"Zaina...",
   [("heartbeat", "އަދިރި", -18)], hum=True)
sh(24, "when was I brought here, who brought me?\" she asked weakly. \"Maaniu bebe brought you... you collapsed,\" said Zaina.")
sh(25, "\"Where is Maaniu now?\" said Luyoon. The doctors said it had happened because of grief, and asked that nobody upset Luyoon.")
sh(26, "It was afternoon, the day Luyoon was discharged. After she left the hospital they took Luyoon somewhere with fresh air: to the park.")
sh(27, "Small children and elderly people were there. \"Luyoon, are you okay now?\" said Aishath. \"Yes, mamma...")
sh(28, "\" Luyoon said with a smile. With new hope and new resolve, they began working to give Luyoon strength.", hum=True)
sh(29, "\"Where is Maaniu now?\" Luyoon asked, looking around. \"He was at the hospital today too,\" said Aishath. Zaina and Maaniu were seen in the distance.")
sh(30, "Both of them held drink cups in both hands. Zaina was carrying snacks. Their little brother was beside them too, smiling.")
sh(31, "\"Here, Luyoon's favourite drink, take it,\" Maaniu said, holding out a vanilla milk. Mother, the two younger ones and Luyoon all joined in the fun.")
sh(32, "And everyone resolved to help with the business Luyoon most wanted to do. After the long holidays, the schools reopened.")
sh(33, "Zaina and Zen, the two kids, were getting ready to go to school. Luyoon was also getting up to go to the office.")
sh(34, "After making breakfast with her mother, she went to freshen up and came out ready. It was a whole new day. New things.",
   [("cup_clatter", "ނާސްތާ", -24)])
sh(35, "Luyoon had her mother Aishath's full support for the things she most wanted to do. Maaniu and Luyoon came together again with a new beginning.")
sh(36, "Many promises were made. Naifa was unhappy and restless about it. As Luyoon's office time was 8:00, she went to drop Zaina and Zen at school.")
sh(37, "Once Zaina and Zen had gone into the school, Luyoon started walking toward home. \"Hey, Luyoon!\" Naifa called out in a displeased voice.",
   [("footsteps_sand", "ހިގައިގަތެވެއެވެ", -22)])
sh(38, "Without answering that voice, Luyoon walked on toward home, to have breakfast with her mother before it was time.")
sh(39, "After mother and daughter had breakfast together: \"Mom, I'm going,\" Luyoon said, and then phoned Maaniu.")
sh(40, "Maaniu works at a government-share company. Maaniu also has to go and fingerprint before 7:30.")
sh(41, "She looked at the phone in her hand. It was already 7:15. \"Maaniu, where are you? Come and pick me up,\" said Luyoon. \"It'll be a little while.")
sh(42, "I'm going to fingerprint first, then I'll come.\" With that he hung up. After fingerprinting, Maaniu went to pick up Luyoon.")
sh(43, "Since Luyoon works in health, she hurried to fingerprint, and asked him to come and see her at break time.")
sh(44, "It was as if a whole new chapter had begun in Luyoon's life. Luyoon's body, which had become thin and frail, was now healthy.")
sh(45, "The secret of this was her little sister Zaina's help. It was the office break. Luyoon took the phone from her bag and dialled Maaniu to ask where he was.",
   [("cloth_rustle", "ދަބަހުގައި", -24)])
sh(46, "\"I'm very busy, but I'm coming,\" Maaniu said. Maaniu too wanted to spend some time with Luyoon.")
sh(47, "They needed time to share their many dreams. A while later Maaniu came on his motorbike to pick up Luyoon.",
   [("motorbike_pass", "ސައިކަލް", -18)])
sh(48, "And he took Luyoon to a restaurant. It was the first time since they had drifted apart that the two went out together again as a couple.")
sh(49, "When the waiter came they ordered, and Luyoon and Maaniu told each other their dreams. They shared so many things.")
SHOTS = S

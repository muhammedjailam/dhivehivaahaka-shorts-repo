"""Beat/shot plan for Milahanduvaru episode 252 (used by plan_beats.py)."""

LOC = {
    "bedroom": "Shamaan's small bedroom in an old coral-stone island house late at night, whitewashed walls, a wooden double bed with a plain sheet and a thin blanket, a small wooden bedside table with a framed photo and a small dim lamp, a wooden-shuttered window with a thin pale curtain, a slow ceiling fan",
    "memory_yard": "a soft dreamlike memory of the sunny sandy yard of a coral-stone island house, a joali rope seat under a big leafy tree, flowering bougainvillea along the low wall",
    "lane_night": "a narrow sandy lane of a small Maldivian island village at night, low coral-stone walls, small tin-roofed houses with a few warm lit windows, coconut palms and a big leafy tree, a joali seat beside a gate",
    "memory_beach": "a soft dreamlike memory of a quiet island beach, white sand, gentle turquoise lagoon, leaning coconut palms",
    "memory_lane_dusk": "a soft dreamlike memory of a narrow sandy island lane at dusk, low coral-stone walls, coconut palms in silhouette",
    "window_night": "the wooden-shuttered window of the island bedroom at night, looking out over a sandy yard with coconut palms and a big leafy tree under heavy dark clouds and a hidden moon",
    "bedroom_morning": "the same small bedroom of the old coral-stone island house in the early morning, whitewashed walls, wooden double bed with a rumpled sheet, small bedside table, wooden-shuttered window open to the morning",
    "kitchen": "the small kitchen of an old coral-stone island house in the morning, a simple gas stove with a steaming pot, a wooden shelf with steel pots and plates, a small window with green leaves outside",
    "sitting_room": "the plain sitting room of an old coral-stone island house, whitewashed walls, a worn cushioned sofa, a woven mat on a tiled floor, a low wooden table, an open doorway to the sandy yard, a few small toys on the mat",
    "sitting_room_evening": "the plain sitting room of an old coral-stone island house in the late afternoon, whitewashed walls, a worn cushioned sofa, a woven mat on a tiled floor with a few small toys, an open doorway to the sandy yard",
    "dining": "the simple dining corner of an old coral-stone island house in the morning, a wooden table with plates of flat roshi bread, a bowl of tuna curry and glasses of milky tea, plastic chairs",
    "front_door": "the open wooden front door of an old coral-stone island house leading to the sandy yard, morning",
    "lane_morning": "a narrow sandy lane of a small Maldivian island village in the morning, low coral-stone walls, coconut palms and bougainvillea, long soft shadows",
    "office": "a small plain island government office, a few wooden desks with desktop computers seen from behind or the side, a filing cabinet, a window with palm leaves outside, whitewashed walls",
    "lane_evening": "a narrow sandy lane of a small Maldivian island village in the late afternoon, low coral-stone walls, coconut palms, long golden shadows",
}
MOOD = {
    "bedroom": "late night, soft silver-blue moonlight from the window and a faint warm amber glow from the small bedside lamp, deep indigo shadows, quiet grief and tenderness",
    "memory_yard": "a gentle warm golden daylight memory, soft blur and glowing haze at the edges, tender and wistful",
    "lane_night": "night, deep indigo sky, moonlight through palm fronds, warm amber light from a few windows, hushed and uneasy",
    "memory_beach": "a hazy pale daylight memory, washed-out soft colours, gentle glow at the edges, bittersweet",
    "memory_lane_dusk": "a hazy dusk memory, cold violet and grey-teal light, mist at the edges, cold and ominous",
    "window_night": "windy night, heavy dark clouds rolling across the sky, silver moonlight breaking through, palms bending in the strong wind, eerie and ominous",
    "bedroom_morning": "early morning, soft pale-gold sunlight through the window, fresh and quiet",
    "kitchen": "morning, warm soft daylight through the small window, gentle steam, homely",
    "sitting_room": "daytime, soft natural tropical light from the open doorway, quiet and heavy",
    "sitting_room_evening": "late afternoon, warm golden light streaming in through the open doorway, joyful and tender",
    "dining": "morning, warm soft daylight, cosy family warmth",
    "front_door": "morning, bright soft daylight outside the door and gentle shade inside, sad farewell",
    "lane_morning": "morning, soft warm sunlight and long shadows, quiet and heavy-hearted",
    "office": "midday, flat cool office light with bright tropical sun outside the window, distracted and lonely",
    "lane_evening": "late afternoon, warm golden light and long shadows, eager and hopeful",
}

BEATS = [
    dict(to=2, reason="episode opening: night, Yameen cries and Shamaan wakes and picks him up", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan sitting up on the edge of the bed in the dark bedroom, lifting his small crying toddler son Yameen into his arms and holding him close to his chest, Yameen's face scrunched in tears, Shamaan's tired face full of tender concern; the moonlit window behind them",
         camera="medium shot, eye level, faces in the upper half, the bed sheet as a calm lower third", amb="island_house_night"),
    dict(to=6, reason="flashback: Shamaan's late wife Zihuna, who died two years into the marriage (hazy memory)", chars=["zihuna"], loc="memory_yard",
         visual="a soft hazy memory of Zihuna standing alone in the sunny yard beside the joali under the big tree, smiling gently and shyly towards the viewer, her lilac dress and pale pink hijab glowing in soft golden light, the edges of the image dissolving into a warm blur",
         camera="medium shot, eye level, soft focus, her face in the upper third, sand as a calm lower third", amb="memory", transition="dissolve",
         sens="other", safe="her sudden death is never shown; only a soft smiling memory"),
    dict(to=9, reason="scene change: island rumours of sorcery about Zihuna's sudden death", loc="lane_night",
         visual="three or four island villagers, men in shirts and sarongs and women in long dresses with dark headscarves, standing close together in a small huddle on a dark sandy lane under a big tree, whispering, seen from a distance and partly from behind, one of them glancing over a shoulder towards a house with a single lit window",
         camera="wide shot, eye level, figures small in the middle of the frame, the moonlit sandy lane as a calm lower third", amb="village_night",
         sens="other", safe="sorcery is only talked about; no rituals, amulets or symbols are shown, only whispering villagers at a distance"),
    dict(to=12, reason="scene change: back in the bedroom, Shamaan lies awake beside the sleeping child", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan lying on his back on the bed, wide awake, staring up at the slowly turning ceiling fan with sad, troubled eyes; little Yameen asleep beside him under a thin blanket, his small face peaceful; silver moonlight across the bed",
         camera="high angle looking down over the bed, Shamaan's face in the upper half", amb="island_house_night"),
    dict(to=13, reason="return to the memory of Zihuna (her good character since school days)", reuse="beat_002", loc="memory_yard",
         visual="reuse of the Zihuna memory", amb="memory", transition="dissolve"),
    dict(to=15, reason="flashback: before the arranged marriage Shamaan was with another girl, Nashwa", chars=["shamaan"], loc="memory_beach",
         visual="a hazy memory of a younger Shamaan standing on the beach talking and smiling with a young woman in a long dark-green dress and black hijab (Nashwa); the two stand a clear arm's length apart facing each other, not touching, she seen in three-quarter view; washed-out soft colours",
         camera="medium wide shot, eye level, both figures in the upper two-thirds, white sand as a calm lower third", amb="memory", transition="dissolve",
         sens="intimacy", safe="the earlier romance is shown only as two people talking at arm's length, no touching"),
    dict(to=16, reason="back to the present: a frightening thought — did that girl turn to sorcery?", reuse="beat_004", loc="bedroom",
         visual="reuse of Shamaan lying awake", amb="island_house_night", transition="dissolve"),
    dict(to=18, reason="action/character change: his mother opens the door; he quickly shuts his eyes and pretends to sleep", chars=["shamaan", "sakeena", "yameen"], loc="bedroom",
         visual="the bedroom door opening slowly, Sakeena standing in the doorway as a soft figure with warm corridor light behind her, looking in with concern; in the foreground Shamaan lying on the bed with his eyes shut, pretending to sleep, little Yameen asleep beside him",
         camera="medium wide shot from the head of the bed towards the door, Sakeena in the upper half", amb="island_house_night"),
    dict(to=22, reason="action change: Sakeena comes to the bed, tucks Yameen's blanket and weeps quietly", chars=["sakeena", "yameen", "shamaan"], loc="bedroom",
         visual="Sakeena bending over the bed, gently straightening the thin blanket over sleeping little Yameen, a tear on her cheek, her worried loving eyes on the child's innocent face; Shamaan lying behind with his eyes closed; soft moonlight and a faint amber lamp glow",
         camera="medium shot, eye level, Sakeena's face in the upper third", amb="island_house_night"),
    dict(to=24, reason="flashback: the happy memories of married life with Zihuna", chars=["shamaan", "zihuna"], loc="memory_beach",
         visual="a soft hazy memory of Shamaan and his wife Zihuna walking side by side along the water's edge at sunset, both smiling and talking, fully clothed and modest, a little space between them, warm golden haze dissolving at the edges",
         camera="medium wide shot from the side, the couple in the upper half, wet sand and gentle foam as a calm lower third", amb="memory", transition="dissolve"),
    dict(to=26, reason="new framing: he opens his eyes and looks at Zihuna's photo on the bedside table", chars=["shamaan", "zihuna"], loc="bedroom",
         visual="close-up of a simple wooden-framed photograph standing on the small bedside table in dim light, the photo shows Zihuna smiling gently in her pale pink hijab; behind it, softly out of focus, Shamaan lying on his side on the pillow gazing at the photo with sad wet eyes; Zihuna appears ONLY inside the photo frame",
         camera="close-up, shallow depth of field, the photo frame in the upper half, the table top as a calm lower third", amb="island_house_night",
         sens="other", safe="the late wife is shown only as a smiling framed photo"),
    dict(to=30, reason="action change: Shamaan holds sleeping Yameen's tiny hand and whispers his promise", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan lying on his side facing his sleeping toddler son, his large hand gently holding Yameen's tiny hand on the pillow, his eyes wet with tears but his face set in loving determination, whispering; Yameen asleep peacefully",
         camera="close two-shot, slightly above, both faces in the upper half, the sheet as a calm lower third", amb="island_house_night"),
    dict(to=32, reason="new detail: a cold wind blows in through the window; an ominous atmosphere", loc="window_night",
         visual="the bedroom window seen from inside, the thin pale curtain blowing inward in a cold gust of wind, outside coconut palms bending under heavy dark rolling clouds lit by a hidden moon, no people",
         camera="medium shot of the window, eye level, the dark wooden window sill as a calm lower third", amb="night_exterior"),
    dict(to=35, reason="new framing: in the darkness he pictures Zihuna's last innocent smile and resolves to find the truth", chars=["shamaan", "zihuna"], loc="bedroom",
         visual="Shamaan lying in the dark room with his eyes open, his face turned up, thoughtful and resolved; above him in the darkness, like soft glowing mist, a faint translucent dreamlike memory of Zihuna's gentle smiling face in her pale pink hijab fading into the shadows",
         camera="medium close-up from above, Shamaan's face in the middle third, the faint memory face in the upper third", amb="island_house_night",
         sens="other", safe="Zihuna only as a faint hazy memory, never as a body"),
    dict(to=38, reason="action change: he gets up and goes to the window; the trees thrash in the strong wind", chars=["shamaan"], loc="window_night",
         visual="Shamaan seen from behind and slightly to the side standing at the open window, one hand on the wooden frame, looking out at coconut palms and a big tree thrashing in the strong wind under dark heavy clouds; his worried face half visible in silver moonlight",
         camera="medium shot over the shoulder, the window and sky in the upper two-thirds", amb="night_exterior"),
    dict(to=41, reason="flashback: Nashwa's hateful warning on the day the relationship ended", loc="memory_lane_dusk",
         visual="a hazy memory of a young woman in a long dark-green dress and black hijab (Nashwa) standing alone in a dusky sandy lane, turned half back towards the viewer, her face cold and bitter, eyes full of resentment, arms folded; mist at the edges of the frame",
         camera="medium shot, eye level, her face in the upper third, the sandy lane as a calm lower third", amb="memory", transition="dissolve",
         sens="other", safe="her hatred is shown only as a cold expression at a distance; no threat or gesture"),
    dict(to=44, reason="back to the present: the warning echoes; a shiver of dread", chars=["shamaan"], loc="bedroom",
         visual="Shamaan sitting on the edge of the bed in the dark, elbows on his knees and hands clasped before his mouth, staring into the darkness with uneasy, frightened eyes; the shadow of the window frame and of swaying palm fronds stretching across the whitewashed wall behind him",
         camera="medium shot, eye level, his face in the upper half, the floor as a calm lower third", amb="island_house_night", transition="dissolve"),
    dict(to=46, reason="return to the opening image: Yameen startles and cries, Shamaan lifts and soothes him", reuse="beat_001", loc="bedroom",
         visual="reuse of Shamaan lifting crying Yameen", amb="island_house_night"),
    dict(to=49, reason="action change: he sits holding the child to his chest, stroking his face, crying too", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan sitting on the bed holding little Yameen against his chest, gently stroking the child's small wet cheek with his fingers, tears in his own eyes, Yameen still sobbing softly with his head on his father's shoulder; warm amber lamp glow and moonlight",
         camera="medium close-up, eye level, both faces in the upper half", amb="island_house_night"),
    dict(to=51, reason="detail: the child's small hand grips his father's shirt as he falls asleep again", chars=["yameen", "shamaan"], loc="bedroom",
         visual="close-up of little Yameen asleep against his father's chest, his tiny hand tightly gripping a fold of Shamaan's light-blue shirt, his eyelashes still wet, Shamaan's hand resting protectively on the child's back; the curtain lifting softly in the breeze behind",
         camera="close-up, eye level, the hand and the child's face in the upper half", amb="island_house_night"),
    dict(to=54, reason="action change: he lays the child down, kisses his forehead and lies beside him", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan lying beside sleeping Yameen, curled protectively towards him with one arm around the child above the blanket, having just kissed his forehead, his eyes closing at last; soft silver moonlight, the room calm",
         camera="medium shot, slightly above the bed, faces in the upper half", amb="island_house_night"),
    dict(to=56, reason="time jump: the morning alarm; he wakes and gets ready", chars=["shamaan", "yameen"], loc="bedroom_morning", transition="black",
         visual="Shamaan sitting up on the edge of the bed in the morning, rubbing one eye with his hand, his mobile phone in his other hand, looking back at little Yameen still deeply asleep on the other side of the bed; pale gold sunlight through the window",
         camera="medium shot, eye level", amb="island_house_day",
         sens="clothing", safe="his bath is not shown; he is shown fully dressed"),
    dict(to=57, reason="location and character change: Sakeena cooks with Yameen on her hip", chars=["sakeena", "yameen"], loc="kitchen",
         visual="Sakeena standing at the small stove holding little Yameen on her hip with one arm and stirring a steaming pot with the other, Yameen watching the steam with sleepy curious eyes",
         camera="medium shot, eye level, faces in the upper half", amb="island_house_day"),
    dict(to=59, reason="character change: the father sits ill with a fever on the sofa", chars=["shamaan_father"], loc="sitting_room",
         visual="Shamaan's father sitting slumped on the worn sofa looking weak and feverish, one hand pressed to his forehead, eyes half closed, a glass of water on the low table beside him",
         camera="medium shot, eye level, his face in the upper half, the woven mat as a calm lower third", amb="island_house_day",
         sens="other", safe="illness shown only as a tired feverish posture"),
    dict(to=63, reason="action change: the family sits down to breakfast of roshi and curry", chars=["shamaan", "yameen", "shamaan_father", "sakeena"], loc="dining",
         visual="the family at the small breakfast table: Shamaan sitting with little Yameen on his lap, the giggling toddler reaching for a small piece of roshi from his father's plate; the father sitting beside them looking tired but smiling faintly; Sakeena standing at the table pouring tea; plates of roshi, a bowl of curry and glasses of tea",
         camera="medium wide shot, eye level, faces in the upper half, the table top as a calm lower third", amb="island_house_day"),
    dict(to=67, reason="action change: he leaves for the office; Yameen cries 'Bappa' and reaches for him", chars=["shamaan", "yameen", "sakeena"], loc="front_door",
         visual="Shamaan at the open front door, dressed for work with a small shoulder bag, turned back towards the room with a pained torn face; in the foreground Sakeena holding little Yameen, who is crying with tears on his cheeks and stretching both small arms out towards his father",
         camera="medium wide shot from inside the house towards the door, faces in the upper half", amb="island_house_day"),
    dict(to=69, reason="location change: he walks to the office, wiping a tear", chars=["shamaan"], loc="lane_morning",
         visual="Shamaan walking alone down the sandy village lane towards the viewer, wiping a tear from his eye with the back of his hand, a small bag on his shoulder, his face sad but determined",
         camera="medium wide shot, eye level, his face in the upper third, the sandy lane as a calm lower third", amb="village_day"),
    dict(to=73, reason="location change: at the office his mind stays at home", chars=["shamaan"], loc="office",
         visual="Shamaan sitting at his office desk in front of a desktop computer seen from the side (the screen not visible), his chin resting on his hand, staring absently out of the window, lost in thought",
         camera="medium shot, eye level, his face in the upper half, the desk top as a calm lower third", amb="office_day"),
    dict(to=76, reason="action change: midday break, he phones home and is relieved", chars=["shamaan"], loc="office",
         visual="Shamaan standing by the bright office window holding a mobile phone to his ear, his worried face slowly easing into a relieved smile, bright midday sun and palm leaves outside",
         camera="medium close-up, eye level, his face in the upper third", amb="office_quiet"),
    dict(to=78, reason="time and location change: after work he hurries home", chars=["shamaan"], loc="lane_evening",
         visual="Shamaan walking briskly down the sandy lane towards home in the warm late-afternoon light, a small hopeful smile on his face, his long shadow on the sand",
         camera="medium wide shot from the side, eye level, the sandy lane as a calm lower third", amb="village_day"),
    dict(to=81, reason="action change: Yameen runs to his father and Shamaan scoops him up", chars=["shamaan", "yameen"], loc="sitting_room_evening",
         visual="in the sitting room, Shamaan just through the doorway bending down with a wide happy smile and lifting little Yameen, who has run to him and is laughing with joy, arms reaching up; a few small toys on the woven mat; warm late-afternoon light from the doorway",
         camera="medium shot, eye level, both faces in the upper half, the mat as a calm lower third", amb="island_house_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "At the sound of his little son crying, Shamaan woke with a start. He got up at once and lovingly picked the child up.",
   [("sob_breath", "ރޮއިގަތް", -22), ("cloth_rustle", "ތެދުވެ", -24)])
sh(2, "It is Shamaan alone who looks after everything for little Yameen, carrying the full responsibility of a father.")
sh(3, "He is the only soul he has in this world. Since his wife Zihuna passed away, Shamaan has had no thought of marrying again.")
sh(4, "Although that marriage had been the family's decision, some kind of love for Zihuna had grown in his heart.")
sh(5, "Barely two years into the marriage Zihuna left this world, leaving Yameen in Shamaan's arms as a priceless trust.")
sh(6, "To give his son, in full, the care and love Zihuna could not give him is Shamaan's greatest resolve.", hum=True)
sh(7, "After Zihuna's sudden death, all kinds of talk went around the island. Some said it was the result of sorcery,")
sh(8, "while others believed it had happened because of fanditha magic aimed at Shamaan. But,")
sh(9, "Shamaan was certain that no harm had come to Zihuna's body, and he had noticed nothing unusual at all.")
sh(10, "After putting his son to sleep, Shamaan came and lay down on the bed, meaning to rest. But,")
sh(11, "every night he gets only a very little sleep. Tonight too, sleep would not come to Shamaan's eyes. Though tomorrow was a day he had to go to the office,")
sh(12, "uneasy thoughts were circling in his mind. Who could have dared to kill an innocent girl like Zihuna, who never troubled anyone?")
sh(13, "Ever since her school days Zihuna had been a calm girl of fine character, with a beautiful face.")
sh(14, "In those days Shamaan was in a relationship with another girl. That girl, too, was an obedient, good girl.")
sh(15, "Shamaan himself admits that one sees no flaws in the person one loves. With every preparation for marrying that girl already done, the family's decision forced Shamaan to marry Zihuna.")
sh(16, "Yet now a frightening thought was rising in his mind. Could that girl have sought the help of sorcery?", hum=True)
sh(17, "Lying deep in such thoughts, Shamaan was startled by the sound of his mother opening the bedroom door. Afraid his mother would worry,",
   [("door_open", "ހުޅުވައިލި", -18)])
sh(18, "he quickly shut his eyes and pretended to be asleep. While Shamaan is at work, it is his mother Sakeena who lovingly looks after everything for his son Yameen.")
sh(19, "Shamaan's mother Sakeena quietly came into the room and checked whether Shamaan and little Yameen were asleep. Since Zihuna's death,",
   [("footsteps_pavement", "ވަދެ", -24)])
sh(20, "emptiness and despair are all one sees in that house. Silence now reigns over the little family that was once full of smiles and joy.")
sh(21, "Sakeena came over, straightened the blanket covering Yameen, and let out a deep breath.",
   [("cloth_rustle", "ރަނގަޅުކޮށްލުމަށްފަހު", -24), ("sigh", "ނޭވާއެއް", -20)])
sh(22, "Looking at that innocent face, tears welled in Sakeena's eyes. Her heart was afraid for the future of this little child, starved of a mother's love.",
   hum=True)
sh(23, "Though Shamaan lay pretending to be asleep, the trembling of his heart did not change. As he lay with his eyes closed,")
sh(24, "happy memories of the time spent with Zihuna were circling in his mind. When Sakeena left the room, Shamaan slowly opened his eyes.")
sh(25, "In the dim light of the room he looked at Zihuna's photo on the table beside the bed.")
sh(26, "Realising that this smile would never again be seen in his life, a pain rose from the very depths of his heart.", hum=True)
sh(27, "Shamaan held the tiny palm of Yameen, asleep beside him. \"My son... your father will never let you be alone.\" Shamaan's voice came out with great difficulty.",
   hum=True)
sh(28, "Zihuna's passing was sudden. It was a great shock to the whole family. Though he tried to carry on with life with Sakeena's help,")
sh(29, "every day the sun rose with memories of Zihuna scraping at Shamaan's heart. But every time he looked at Yameen's face,")
sh(30, "he found the strength to pull himself together and rise. He is the most precious trust Zihuna left behind. At that moment, with a cold wind coming in through the bedroom window,",
   [("wind_gust", "ރޯޅިއަކާއެކު", -18)])
sh(31, "it was as if an ominous feeling settled over everything. What came to Shamaan's mind was his former love.")
sh(32, "The things that girl had said in those days, and the warnings she made when the marriage was called off, began to echo in his mind.")
sh(33, "Hearing Sakeena leave the room, Shamaan slowly opened his eyes. In the darkness of the room he kept seeing Zihuna's last smile.")
sh(34, "He does not know what secrets were hidden behind that innocent smile. But one thing he knows: he must work to find the root of this great storm that has come into his life.")
sh(35, "For his son Yameen's sake as well, finding the truth is now his duty. Like the dark clouds gathering in the sky, the doubts in Shamaan's heart kept growing.")
sh(36, "Shamaan found no peace of mind. He got up from the bed, went to the window and looked outside. As the trees thrashed in the strong wind,",
   [("cloth_rustle", "ތެދުވެ", -24), ("wind_howl", "ވަޔާއެކު", -18)])
sh(37, "the scene outside was frightening. He needed answers to the questions forming in his heart. Was Zihuna's death a natural one?",
   [("leaves_rustle", "ބޭރުން", -20)])
sh(38, "Or was it the result of a dangerous plot someone had made? Shamaan lay tossing and turning in bed. Sleep had fled from his eyes.",
   [("cloth_rustle", "ފުރޮޅި", -24)])
sh(39, "Memories from two years ago were still circling in his mind: the image of his former love Nashwa, and the last things she said.")
sh(40, "\"Shamaan, I will never let you be happy with anyone but me.\" The hatred and anger he saw in Nashwa's eyes the day that relationship broke will never fade from Shamaan's memory.",
   hum=True)
sh(41, "The words Nashwa spoke that day still echo in his ears today like a frightening warning.")
sh(42, "Shamaan's heart kept telling him that something evil was at work. Today he has begun to feel that Nashwa's warning was no ordinary thing.")
sh(43, "Every time the thought crossed his mind that every obstacle placed in the way of his happiness might be the result of Nashwa's 'curse', gooseflesh rose on Shamaan's skin.",
   [("heartbeat", "ހީބިހި", -18)])
sh(44, "He does not know what kind of storm lies ahead. But one thing he knows: that shadow of the past will not let go of him.")
sh(45, "Just then Yameen suddenly started in his sleep and began to cry. Shamaan hurried over, took his son in his arms and began to soothe him. \"My son,",
   [("sob_breath", "ރޯން", -20)])
sh(46, "Bappa is right here,\" he said softly. Seeing the tears falling from Yameen's little eyes, Shamaan's heart broke into pieces.", hum=True)
sh(47, "He felt how much this innocent child needs a mother's love. As Yameen's soft crying echoed in the room, tears fell from Shamaan's eyes too.",
   [("sob_breath", "ރުއިމުގެ", -24)], hum=True)
sh(48, "He sat holding his son to his chest, stroking that little face. \"My son, Bappa will never leave you alone.", hum=True)
sh(49, "Even if I cannot fill the gap of your mother's absence, Bappa will sacrifice his whole life for you,\" Shamaan promised himself in his heart.", hum=True)
sh(50, "As a cold breeze came into the room, Yameen's crying slowly stopped. Holding tight to his father's shirt with his little hand,",
   [("wind_gust", "ރޯޅިއެއް", -22)])
sh(51, "he sank again into the deep sea of sleep. Shamaan sat for a long time like that, watching his son. A hard journey lay ahead.")
sh(52, "But that son's smile is the greatest hope of his life. After a while Shamaan gently laid Yameen down on the bed.")
sh(53, "And after kissing his son's forehead, he lay down beside him, to give him the feeling that there was nothing at all to fear,")
sh(54, "assuring him that in any situation he will be there to protect him. With the ring of the phone alarm, Shamaan woke up.",
   [("phone_buzz", "އެލާމް", -18)])
sh(55, "Rubbing his eyes he sat up and looked at little Yameen, fast asleep on one side of the bed. He got up quietly and went into the bathroom,",
   [("door_close", "ފާޚާނާއަށް", -24)])
sh(56, "taking great care not to wake Yameen. When Shamaan came out after his bath, the smell of cooking from the kitchen had filled the whole house.")
sh(57, "Yameen was awake by then too. Shamaan's mother Sakeena was holding Yameen in one arm and finishing the kitchen work with the other.",
   [("cup_clatter", "ބަދިގެތެރޭގެ", -24)])
sh(58, "Bappa was sitting on the sofa in the sitting room, very unwell. Bappa, who usually goes out fishing at dawn every day,")
sh(59, "stayed home today because he had come down with a fever. \"Give Yameen to me, mother, and make the tea,\" Shamaan said kindly.")
sh(60, "Sakeena lovingly handed Yameen to Shamaan and hurried to make the tea. Before long she laid out hot roshi and curry on the table.",
   [("cup_clatter", "މޭޒުމަތީ", -20)])
sh(61, "\"Come, son, have your tea,\" Sakeena called. Shamaan and Bappa sat down to their tea.")
sh(62, "Little Yameen sat on his father Shamaan's lap, giggling away as he tried to eat a small piece of roshi from his father's plate.")
sh(63, "That was the happiest moment of Shamaan's life. But when he looked at the clock it was time to go to the office. Shamaan got up,")
sh(64, "got ready for the office and started towards the door. Just then the colour of Yameen's face changed and his eyes filled with tears. \"Bappa... Bappa...\"",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(65, "he called, and began to cry loudly. He wanted to go with his father. As he stood crying, stretching his little arms towards Shamaan, it was enough to break Shamaan's heart.",
   [("sob_breath", "ރޯން", -20)], hum=True)
sh(66, "Shamaan stopped. He wanted to pick his son up and soothe him. His heart even told him to skip the office and stay. But,", hum=True)
sh(67, "for the responsibilities on his shoulders, his sick father's treatment, and above all Yameen's bright future, he has to work.")
sh(68, "Wiping away a tear that fell from his eye, Shamaan steeled himself and left the house. Not out of any wish to go to the office,")
sh(69, "but with the noble resolve to give that son a good life. Even as he walked along the road, the sound of Yameen's crying echoed in Shamaan's ears.",
   [("footsteps_sand", "ހިނގަމުން", -22)])
sh(70, "Every day the time to go to the office comes with heartache. After entering the office and sitting down, though he switched on the computer,",
   [("keyboard_typing", "ކޮމްޕިއުޓަރު", -24)])
sh(71, "his mind was at home. As he went about his office work, the painful event that had happened before kept coming back to Shamaan's mind.")
sh(72, "With Yameen's mother, his beloved wife, gone, it is Shamaan who has to give Yameen a mother's love as well as a father's.")
sh(73, "Though he has his mother Sakeena's help, the more Yameen grows, the more he needs a mother.")
sh(74, "It was the hot hour of midday. At the office break Shamaan hurried to call home. Sakeena picked up the phone. \"Mother, how is Yameen?",
   [("phone_buzz", "ގުޅައިލުމަށެވެ", -24)])
sh(75, "Is he still crying?\" Shamaan asked anxiously. \"No, son, he has calmed down now. He ate and is sleeping next to Bappa.")
sh(76, "Bappa's fever has also eased a little now.\" Sakeena's answer brought great relief to Shamaan's heart.",
   [("sigh", "ހަމަޖެހުމެއް", -22)])
sh(77, "Amid the strain of the work, the office closing time came. Shamaan set off for home earlier than on other days.",
   [("footsteps_sand", "މިސްރާބު", -22)])
sh(78, "His heart longed to take that son in his arms as soon as possible and kiss that face.")
sh(79, "As soon as he stepped into the house, the moment Yameen, sitting playing in the sitting room, saw his father, extraordinary joy lit up his face. \"Bappa!\"",
   [("door_open", "ވަދެވުމާއެކު", -20)])
sh(80, "Calling out, he came running and hugged Shamaan's legs. Shamaan lovingly picked Yameen up and held him to his chest.",
   [("footsteps_pavement", "ދުވެފައި", -24)], hum=True)
sh(81, "The feelings of the morning and the pain he had carried melted away with that little smile.", hum=True)
SHOTS = S

"""Beat/shot plan for Milahanduvaru episode 254 (used by plan_beats.py)."""

_YARD = ("the sandy front yard of a modest single-storey coral-stone family house in a small Maldivian island village, "
         "a huge old banyan tree with hanging aerial roots in the middle of the yard, a woven joali rope seat under it, "
         "a shaded veranda with a wooden door, a low whitewashed coral-stone boundary wall and coconut palms beyond")
_ROOM = ("Shamaan's small plain bedroom in an old Maldivian coral-stone house, whitewashed walls, a simple wooden double "
         "bed with a plain pale sheet, a small wooden bedside table, a wooden wardrobe, a window with a thin plain curtain, "
         "a low wooden toy box with a few soft toys in one bare corner, a tiled floor")
_SHOW = ("the edge of the island's big open sandy ground during a night music show: rows of plastic chairs set out on "
         "the sand, a brightly lit stage far away in the distance, strings of coloured bulbs in the trees, dark palms "
         "and deep shadows around the quiet edge where only a few chairs are occupied")

LOC = {
    "yard_dusk": _YARD,
    "room_evening": _ROOM,
    "yard_morning": _YARD,
    "kitchen": "a simple Maldivian house kitchen with whitewashed walls, a gas stove with big aluminium pots, a wooden table with bowls of food, an open back door looking out onto a sunny sandy yard with a huge banyan tree",
    "yard_noon": _YARD,
    "yard_party": _YARD,
    "room_dusk": _ROOM,
    "room_phone": _ROOM,
    "house_day": "the plain sitting area of a modest Maldivian coral-stone house, whitewashed walls, a woven mat on the tiled floor, a low wooden table, an open window with a thin curtain onto a sunny sandy yard",
    "field_night": "the main sandy sports field of a small Maldivian island village at night during Eid festivities, a football pitch and a volleyball net under tall floodlights, strings of coloured bulbs across the palms and houses around it",
    "lane_night": "a narrow sandy lane between low coral-stone walls in a Maldivian island village late at night, coconut palms overhead, a few strings of coloured festive bulbs on the walls",
    "room_rain": _ROOM,
    "room_predawn": _ROOM,
    "field_morning": "the edge of the main sandy sports field of a small Maldivian island village in the morning, young men practising football in the distance, a big shady tree at the edge of the field with its roots in the sand",
    "akram_house": "the shaded front veranda of a modest Maldivian island house, a woven joali rope seat and a small wooden table with two glasses of tea, a sandy yard with potted plants and palms",
    "show": "the island's big open sandy ground during a night music show, a brightly lit stage far away, a crowd of islanders young and old seated on rows of plastic chairs on the sand and some standing, strings of coloured bulbs in the trees",
    "show_edge": _SHOW,
    "show_edge_alone": _SHOW,
    "show_dark": _SHOW,
}
MOOD = {
    "yard_dusk": "early evening dusk, the last violet-blue light in the sky, a single warm amber lamp glowing on the veranda, heavy sorrowful family tension",
    "room_evening": "evening, a dim bedside lamp casting warm amber light against deep teal shadows, wounded, brooding, then quietly resolute",
    "yard_morning": "bright clear morning, soft golden tropical sunlight through the banyan leaves, fresh, hopeful and busy",
    "kitchen": "late morning, warm sunlight through the open back door, steam rising from the pots, homely and busy",
    "yard_noon": "bright early afternoon, dappled sunlight and deep shade under the banyan tree, playful but with a faint uneasy undertone",
    "yard_party": "golden late afternoon sun, long warm shadows, festive balloons glowing, joyful party bustle with a quiet worried undertone",
    "room_dusk": "Maghrib dusk, the room dim, only fading violet-blue light from the window and one small amber bedside lamp, eerie unease",
    "room_phone": "deep night, the room almost dark, only the cold white light of a phone screen, alarm and tenderness",
    "house_day": "pale daylight, quiet and heavy, a worried, uneasy household",
    "field_night": "night, bright white floodlights and colourful festive bulbs against a deep indigo sky, lively Eid excitement",
    "lane_night": "late night around eleven, moonlight and a few coloured bulbs on the walls, playful teasing voices, Shamaan tired",
    "room_rain": "late night around midnight, heavy rain streaking the window, only a dim amber night lamp, a faint silvery haze in the air, mysterious stillness",
    "room_predawn": "the dark early hours before dawn, cold blue-grey light from the window, silent and uneasy",
    "field_morning": "morning, soft clear tropical light, distant players, Shamaan quiet and heavy-hearted",
    "akram_house": "late morning, soft warm daylight in the shade of the veranda, friendly, Shamaan thoughtful",
    "show": "night, the stage glowing with bright warm lights far away, coloured festive bulbs, a joyful crowd under a deep indigo sky",
    "show_edge": "night, the stage lights glowing far away, the quiet edge lit only by moonlight and a few coloured bulbs, calm",
    "show_edge_alone": "night, distant warm stage glow, silver moonlight on the quiet edge, an enigmatic, slightly unsettling stillness",
    "show_dark": "night, the stage light distant and small, deep darkness and palm shadows all around, rising fear and unease",
}

BEATS = [
    # --- the confrontation with the father (continues from 253)
    dict(to=4, reason="episode opening: Shamaan's anguish before his parents about aunt Naasira",
         chars=["shamaan", "shamaan_father", "sakeena"], loc="yard_dusk",
         visual="Shamaan standing by the joali under the big banyan tree, tears on his cheeks, one hand pressed to his chest, speaking in anguish; his father sitting on a plain wooden chair a few steps away, head bowed, sorrowful; his mother Sakeena standing near the veranda step behind them with her hands clasped at her chest, worried",
         camera="medium wide three-shot, eye level, faces in the upper half, the sandy yard forming a calm lower third",
         amb="island_house_night", sens="other",
         safe="the accusation of sorcery is only spoken; no sorcery imagery shown"),
    dict(to=6, reason="action change: the father rises and lays a hand on his son's shoulder",
         chars=["shamaan_father", "shamaan"], loc="yard_dusk",
         visual="the father standing beside Shamaan with one hand resting gently on his son's shoulder, looking at him with tired sad eyes; Shamaan raising his head to look at his father, his eyes wet and his jaw tight, still burning inside",
         camera="medium two-shot, eye level", amb="island_house_night"),
    dict(to=9, reason="scene change: Shamaan alone in his room after shutting the door, deciding to seek a scholar",
         chars=["shamaan"], loc="room_evening",
         visual="Shamaan sitting on the edge of his bed in the dim room, elbows on his knees, hands clasped before his mouth, staring ahead with wounded but slowly resolving eyes; the closed wooden door behind him",
         camera="medium shot, slightly low angle from the side", amb="room_night"),
    # --- Yameen's second birthday
    dict(to=12, reason="time jump: the following days, Shamaan takes heart for Yameen; the birthday morning",
         chars=["shamaan", "yameen"], loc="yard_morning", transition="black",
         visual="Shamaan standing in the sunny yard holding little Yameen on his hip, the toddler smiling and reaching up at the banyan leaves; Shamaan smiling softly with a quiet determined look, the morning sun on their faces",
         camera="medium shot, eye level", amb="island_house_day"),
    dict(to=14, reason="action change: friends and island youths decorate the yard",
         chars=["shamaan"], loc="yard_morning",
         visual="the yard being decorated: Shamaan on a short wooden ladder tying a bunch of colourful balloons to a branch of the big banyan tree, two or three young island men below handing up balloons and stretching a plain colourful paper bunting with no letters between the tree and the veranda; balloons and streamers everywhere",
         camera="wide shot, slightly low angle, the tree and balloons in the upper two-thirds", amb="island_house_day",
         sens="other", safe="the 'Happy Birthday' banners are shown as plain colourful bunting without any letters"),
    dict(to=16, reason="character and location change: Sakeena cooking in the kitchen; Yameen plays by the tree outside",
         chars=["sakeena", "yameen"], loc="kitchen",
         visual="Sakeena at the stove stirring a big pot with a ladle, steam rising, a contented busy face; through the open back door behind her the sunny yard with balloons, where small Yameen in his yellow t-shirt plays by the roots of the big banyan tree in the distance",
         camera="medium shot, eye level, Sakeena in the foreground, the bright doorway behind her", amb="home_day"),
    dict(to=19, reason="action change: Yameen runs around the banyan tree, Shamaan watches and goes to pick him up; a small cat",
         chars=["yameen", "shamaan"], loc="yard_noon",
         visual="little Yameen running around the thick trunk of the big banyan tree, laughing with his head turned back as if someone chases him; Shamaan a few steps away in the shade smiling and bending forward with his arms open to scoop him up; a small grey tabby cat sitting by the tree roots; a faint soft dark shadow stretched on the trunk behind the child",
         camera="medium wide shot, eye level", amb="island_house_day"),
    dict(to=22, reason="time change: late afternoon, Shamaan comes out freshly dressed; guests arrive, Sakeena welcomes them holding Yameen",
         chars=["sakeena", "yameen", "shamaan"], loc="yard_party",
         visual="at the yard gate decorated with balloons, Sakeena holding little Yameen's hand and smiling to welcome a few small village children arriving in festive clothes (small boys in shirts and long trousers, and little girls in long-sleeved ankle-length dresses with small hijabs fully covering their hair); Yameen in a clean new yellow t-shirt, neatly combed; Shamaan stepping out of the veranda door behind them, freshly dressed with damp combed hair",
         camera="medium wide shot, eye level", amb="island_house_day", sens="clothing",
         safe="his bath is only mentioned; he is shown afterwards, fully dressed, stepping out of the house"),
    dict(to=25, reason="action change: at the party Yameen keeps apart; Shamaan notices with worry",
         chars=["yameen", "shamaan"], loc="yard_party",
         visual="little Yameen sitting alone on the veranda step with a balloon string slack in his hand, staring quietly into empty space while blurred children play with balloons in the yard behind; Shamaan standing a little apart in the yard, looking at his son with a worried frown",
         camera="medium shot, eye level, Yameen in the foreground on one side, Shamaan behind", amb="island_house_day"),
    # --- Maghrib: Yameen talks to an empty corner
    dict(to=29, reason="time and scene change: Maghrib, Sakeena takes Yameen into the room; he babbles to someone unseen",
         chars=["sakeena", "yameen"], loc="room_dusk",
         visual="Sakeena sitting on the edge of the bed in the dim room with little Yameen beside her; the toddler waving both hands in the air and babbling towards the empty side of the room; Sakeena stroking his head with one hand, her lips moving in a silent prayer, her eyes fearful",
         camera="medium shot, eye level", amb="room_night"),
    dict(to=33, reason="action change: Yameen points and laughs at the empty corner; Sakeena holds him to her chest",
         chars=["sakeena", "yameen"], loc="room_dusk",
         visual="Sakeena standing and holding little Yameen against her chest; the toddler squirming and looking back over her shoulder towards an empty dim corner where a wooden toy box stands, laughing loudly with one arm stretched out; Sakeena's face pale and frightened",
         camera="medium close shot, eye level, the empty corner visible in the soft background", amb="room_night",
         sens="other", safe="nothing is shown in the corner; only the child's gaze and the grandmother's fear"),
    dict(to=36, reason="character enters: Shamaan comes into the room and sees his mother's fear",
         chars=["shamaan", "sakeena", "yameen"], loc="room_dusk",
         visual="Shamaan standing just inside the doorway with a concerned questioning face; Sakeena facing him holding little Yameen in her arms, her face fearful, one hand pointing towards the corner; Yameen looking away towards the corner",
         camera="medium wide shot, eye level", amb="room_night"),
    dict(to=38, reason="detail image: the corner Shamaan looks at holds only Yameen's toy box",
         chars=[], loc="room_dusk",
         visual="close view of the bare dim corner of the room: a small wooden toy box with a few soft toys and a little ball, the whitewashed walls meeting, fading violet light from the window falling across it; nobody there",
         camera="close-up, eye level, the toy box in the middle of the frame, the tiled floor as a calm lower third", amb="room_night"),
    dict(to=40, reason="memory: Shamaan recalls the dark shadow behind Yameen at the tree", reuse="beat_007",
         loc="yard_noon", visual="(reuse) Yameen running around the banyan tree, faint shadow on the trunk",
         amb="memory", transition="dissolve"),
    dict(to=42, reason="time jump: late that night Yameen is found curled at the foot of the bed, cold",
         chars=["shamaan", "yameen"], loc="room_phone", transition="black",
         visual="Shamaan kneeling on the bed in the dark room, lifting little Yameen from the foot of the bed and holding him close against his chest, the white light of a phone lying on the sheet lighting their faces from below; the child fully clothed, eyes half closed and still; Shamaan's face alarmed and tender",
         camera="medium close shot, eye level", amb="room_night", sens="other",
         safe="the child's coldness is shown only as a still child held tenderly in his father's arms; no distress, no marks"),
    dict(to=45, reason="time jump: the following days, Yameen withdrawn; the family concludes it is spiritual",
         chars=["yameen", "sakeena", "shamaan"], loc="house_day", transition="black",
         visual="little Yameen sitting alone on the woven mat beside an untouched small bowl of food, murmuring softly to himself and looking at nothing; in the doorway behind him Sakeena and Shamaan standing side by side watching him, their faces heavy with worry",
         camera="medium wide shot, eye level, the child in the foreground, the adults behind", amb="home_day",
         sens="other", safe="the strange marks on the child's body are never shown; he is fully clothed, only the adults' worry carries it"),
    # --- Eid games and the night walk home
    dict(to=48, reason="scene change: Eid games night on the floodlit field",
         chars=["shamaan"], loc="field_night",
         visual="the crowded floodlit island field at night, young men playing football in the middle distance, a volleyball net beside, a big crowd of cheering islanders around the edges; Shamaan in the foreground walking in with a few team mates in sports t-shirts, looking towards the games",
         camera="wide shot, eye level, the floodlights and crowd in the upper two-thirds", amb="village_night"),
    dict(to=53, reason="scene change: walking home at eleven; the girls tease him",
         chars=["shamaan"], loc="lane_night",
         visual="Shamaan in the sandy lane at night half-turned and looking back over his shoulder with a puzzled face; a few friends walking ahead of him; behind him at a distance a small group of island girls in long modest dresses and hijabs walking together, laughing and teasing",
         camera="medium wide shot, eye level, Shamaan in the foreground, the girls small in the background", amb="island_night"),
    # --- midnight: rain, footsteps, flower scent
    dict(to=55, reason="scene change: home at midnight, mother asleep beside Yameen; he takes a towel; rain begins",
         chars=["shamaan", "sakeena", "yameen"], loc="room_rain",
         visual="the dim bedroom at midnight: Sakeena asleep on the bed, fully covered with a sheet and still in her headscarf, beside little Yameen asleep; Shamaan quietly standing by the wardrobe with a folded towel over his arm, looking at them tenderly; heavy rain starting to streak the dark window",
         camera="medium wide shot, eye level", amb="rain_night"),
    dict(to=58, reason="action change: after his bath he feels someone behind him; a strange sweet flower scent fills the room",
         chars=["shamaan"], loc="room_rain",
         visual="Shamaan, fully dressed with a towel around his neck, stopping in the middle of the dim room and looking back over his shoulder towards the empty dark doorway, uneasy; a faint silvery haze drifting softly through the air in the lamplight; rain on the window",
         camera="medium shot, eye level", amb="rain_night", sens="clothing",
         safe="the shower is only mentioned; he is shown afterwards, fully dressed"),
    dict(to=60, reason="time change: early before dawn he wakes to footsteps in the room; no one there",
         chars=["shamaan"], loc="room_predawn",
         visual="Shamaan sitting up in bed in the dark, propped on one arm, staring warily into the empty room; the cold blue-grey light from the window, the room completely empty",
         camera="medium shot, eye level", amb="room_night"),
    # --- the next day
    dict(to=63, reason="time jump: next morning at the field; he sits under a tree; Akram comes",
         chars=["shamaan", "akram"], loc="field_morning", transition="black",
         visual="Shamaan sitting alone in the shade under the big tree at the edge of the field, arms on his knees, heavy-hearted; his friend Akram walking up to him grinning and beckoning with one hand; players practising football small in the distance",
         camera="medium wide shot, eye level", amb="village_day"),
    dict(to=67, reason="scene change: tea at Akram's house; Akram urges the show; Shamaan thinks of his son",
         chars=["akram", "shamaan"], loc="akram_house",
         visual="Akram and Shamaan sitting on the joali on Akram's veranda with glasses of tea; Akram leaning forward talking excitedly with lively hands; Shamaan holding his glass, looking away into the distance with a thoughtful, responsible expression",
         camera="medium two-shot, eye level", amb="island_house_day"),
    # --- the music show and Zumra
    dict(to=70, reason="scene and time change: the night music show begins",
         chars=[], loc="show",
         visual="the big sandy ground at night seen from behind the crowd: a brightly lit stage far away with a row of bodu beru drummers small in the distance, islanders young and old seated on rows of chairs and some standing, coloured bulbs in the trees, joyful atmosphere",
         camera="wide establishing shot from behind the crowd, the stage in the upper half, dark sand forming a calm lower third",
         amb="village_night", transition="black", sens="other",
         safe="the music is only shown as tiny distant drummers on the stage; no dancing; no music in the sound mix"),
    dict(to=74, reason="action change: Shamaan and Akram sit at the quiet edge; Akram is restless",
         chars=["shamaan", "akram"], loc="show_edge",
         visual="Shamaan and Akram sitting on two plastic chairs at the quiet, dim edge of the show ground, only a few people far around them; Shamaan relaxed and watching the distant lit stage; Akram fidgeting on the edge of his seat, turning towards Shamaan and pointing towards the stage",
         camera="medium two-shot, eye level, the far stage glow behind them", amb="night_exterior"),
    dict(to=76, reason="character leaves: Akram goes to the stage; Shamaan alone, absorbed in the show",
         chars=["shamaan"], loc="show_edge_alone",
         visual="Shamaan sitting alone on a plastic chair at the quiet edge with empty chairs on both sides of him, absorbed in watching the distant glowing stage, his face lit faintly by the warm far-away light; a small figure of a man in a checked shirt walking away towards the stage in the distance",
         camera="medium shot, eye level from the side, the empty chairs beside him", amb="night_exterior"),
    dict(to=81, reason="character enters: a strange girl, Zumra, speaks to him (first appearance)",
         chars=["zumra", "shamaan"], loc="show_edge_alone",
         visual="Zumra standing a clear step away beside Shamaan's chair in the moonlight, her hands folded together at her waist, leaning slightly forward with a warm enigmatic smile and a silvery sparkle in her eyes; Shamaan turned half round in his chair, startled and displeased, frowning up at this stranger; a clear gap between them, nobody touching",
         camera="medium two-shot, eye level, faces in the upper half", amb="night_exterior", sens="intimacy",
         safe="the narrated hand on his shoulder is not shown; she stands a clear step away from him, no touch"),
    dict(to=84, reason="action change: Zumra sits down uninvited on a chair at a distance and promises to meet tomorrow",
         chars=["zumra", "shamaan"], loc="show_edge_alone",
         visual="Zumra sitting composed on a plastic chair with one empty chair between her and Shamaan, her hands in her lap, turned slightly towards him with a small knowing smile; Shamaan sitting stiffly, frowning sideways at her with suspicion; the distant stage glow behind, moonlight on her silver-grey hijab",
         camera="medium wide two-shot, eye level, the empty chair between them clearly visible", amb="night_exterior",
         sens="intimacy", safe="strangers seated apart with an empty chair between them; no touching"),
    dict(to=86, reason="return: Zumra has left; Shamaan alone again at the edge", reuse="beat_026",
         loc="show_edge_alone", visual="(reuse) Shamaan alone on his chair among empty chairs", amb="night_exterior"),
    dict(to=90, reason="character returns: Akram rushes back, urging him to come and teasing about jinn",
         chars=["akram", "shamaan"], loc="show_edge",
         visual="Akram standing in front of Shamaan slightly out of breath, grinning mischievously and waving an arm towards the far stage; Shamaan still seated, shaking his head firmly with a calm face",
         camera="medium two-shot, eye level", amb="night_exterior"),
    dict(to=93, reason="action change: alone, fear creeps in; Shamaan stands up and looks into the darkness",
         chars=["shamaan"], loc="show_dark",
         visual="Shamaan rising from his chair at the dark edge of the ground, looking around anxiously into the deep shadows of the palms behind the empty chairs, the distant stage only a small glow far behind him; an uneasy, watchful face",
         camera="medium shot, slightly low angle", amb="night_exterior", sens="other",
         safe="the jinn is only suggested by darkness and his fear; nothing is shown in the shadows"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Mother, how can I calm down? When some of my own family have robbed me of my happiness, how can I be patient?\"")
sh(2, "Shamaan wept. The pain that had built up in his heart poured out in his words. \"Son, Naasira is a very jealous person.",
   [("sob_breath", "ރޮވުނެވެ", -22)], hum=True)
sh(3, "She wanted you to marry one of her children. When we refused, she was very unhappy.")
sh(4, "But I don't believe she would do something so low — something like sorcery, which is a great sin in Islam.\" Sorrow was in the father's voice.")
sh(5, "The father let out a deep breath and rose from his chair. He walked slowly over and laid his hand on Shamaan's shoulder. Shamaan raised his head and looked at his father.",
   [("sigh", "ނޭވާއެއް", -20), ("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(6, "Though the questions in his heart had found some kind of answer, the fire burning in his heart did not die down.")
sh(7, "What he wanted was to learn the truth, and for those who stole his happiness to get the punishment they deserved. Without a word, Shamaan went into his room and shut the door.",
   [("door_close", "ލެއްޕިއެވެ", -16)])
sh(8, "The wounds in his heart were fresh again. He decided to seek the help of a religious scholar in this matter.", hum=True)
sh(9, "He felt that this was the best way to be saved from the evil of sorcery.")
sh(10, "After that day, changes began to come into Shamaan's life. For Yameen's sake he took heart. He cut all ties with aunt Naasira's family.")
sh(11, "The day little Yameen turned two was a day that brought joy to the whole household. Shamaan was determined to celebrate his only child's birthday in full colour.")
sh(12, "As it was the Eid holidays, many of the island's young people who live away had also come back home.")
sh(13, "So, with the help of Shamaan's friends and the island youths, the work of decorating the yard began with great enthusiasm.")
sh(14, "The whole yard was bright with colourful balloons and banners saying \"Happy Birthday\".")
sh(15, "Shamaan's mother Sakeena was busy in the kitchen preparing food for the guests coming to the party.")
sh(16, "The sweet smell of cooking had spread all around. In the middle of all this bustle, little Yameen was playing by the big banyan tree in the yard.")
sh(17, "Shamaan stood at a distance watching over his son. Now and then Yameen laughed loudly, and at other times he started running around the tree.",
   [("footsteps_sand", "ދުވަން", -24)])
sh(18, "At a glance it looked as if some mysterious person was chasing him, or as if he was playing with someone. Smiling, Shamaan went and picked up his son.")
sh(19, "Just then he saw a small cat by the tree. Shamaan said to himself: so my son was running after this cat.")
sh(20, "As the heat of the sun faded and the cool evening breezes began to blow, the work was just finished. Shamaan hurried off to bathe and get ready,",
   [("leaves_rustle", "ރޯޅިތައް", -24)])
sh(21, "because he had to be ready before the children came to the party. When he came out after his bath, some children had already started to arrive.",
   [("footsteps_sand", "އަންނަން", -24)])
sh(22, "Sakeena stood holding Yameen's hand, welcoming the guests. Yameen looked lovely in his new clothes.")
sh(23, "But Shamaan noticed one thing. Even in the bustle of the party, Yameen wanted to be alone.")
sh(24, "He showed little interest in playing or joining in with the other children. Shamaan was somewhat worried about this change that had come over Yameen.")
sh(25, "Keeping to himself, behaving as if he lived in a world of his own — this was something unusual to see in Yameen. When the party was over,")
sh(26, "as the sun set and the call to the Maghrib prayer began, Sakeena took Yameen into the room. At that moment Yameen was waving his hands and chattering about something.")
sh(27, "It seemed as if he was talking to someone who could not be seen, complaining about something. But since he could not yet speak properly, Sakeena could not understand what he was saying.")
sh(28, "Yameen's behaviour stirred fear in Sakeena's heart. Stroking Yameen's head, she tried to calm the child, praying silently all the while.", hum=True)
sh(29, "In the dim light of the room, Sakeena grew more and more uneasy at the way Yameen was behaving.")
sh(30, "Every now and then Yameen pointed at an empty corner of the room and laughed. And he waved his hand as if calling to someone.")
sh(31, "Sakeena quickly picked Yameen up and held him to her chest. But Yameen tried to wriggle free of her arms. He still wanted to play.",
   [("cloth_rustle", "އުރާލައިގެން", -24)])
sh(32, "\"My dear, it's bedtime now,\" Sakeena said softly. But Yameen's eyes were fixed on something over Sakeena's shoulder, behind her.")
sh(33, "Suddenly Yameen burst out laughing. Something strange in the sound of that laughter made the hair on Sakeena's skin stand on end.",
   [("heartbeat", "ހީބިހި", -20)], hum=True)
sh(34, "She began to feel that it was not just a small child's playful laugh. It was at that moment that Shamaan came into the room.",
   [("door_open", "ވަނީ", -22)])
sh(35, "He saw the fear on his mother's face. \"Mother, what happened?\" Shamaan asked. \"Shamaan, look how this child is behaving.")
sh(36, "Every now and then he looks at that corner and talks. It's as if someone is standing there,\" Sakeena said in a trembling voice. \"Mother, that's just what little children do.")
sh(37, "They live in an imaginary world of their own. He's acting like this because he's very tired today.\" Shamaan looked at that corner.")
sh(38, "All that was there was the box holding Yameen's toys. Shamaan wanted to put his mother's mind at rest.")
sh(39, "But doubt had arisen in his own heart too. He remembered how, in the afternoon, when Yameen ran by the tree, it had seemed to him that a dark shadow went after him.",
   hum=True)
sh(40, "At the time he had thought it was the cat. But now quite different fears were creeping into his mind.")
sh(41, "Late that night Shamaan woke to the sound of Yameen whimpering softly. When he quickly looked by the light of his phone,",
   [("sob_breath", "ގިސްލާ", -24)])
sh(42, "Yameen was lying curled up against the foot of the bed. When Shamaan picked him up and held him to his chest, he felt that Yameen's body was as cold as a lump of ice.",
   [("heartbeat", "ފިނިވެފައި", -20)], hum=True)
sh(43, "After that, the changes in Yameen grew. He ate less, and spent much of his time sitting alone, talking softly to himself.")
sh(44, "Sometimes strange marks and red patches, as if he had been pinched, began to appear on his body.")
sh(45, "Sakeena and Shamaan concluded that this was something spiritual rather than a matter of health. Tonight was the night the joyful Eid games began. The whole island was lit up,")
sh(46, "decorated with coloured bulbs. On the island's main field many exciting games like football, volleyball and baibalaa were under way, and the whole place was abuzz.")
sh(47, "But what everyone was waiting for most was the special music show tonight. Shamaan, too, got ready with his team mates and went to the sports ground.")
sh(48, "The field was packed with people who had come to cheer on the games. When the games were over,")
sh(49, "at nearly eleven at night, Shamaan set off for home. Other friends walked slowly along with him. \"Shamaan, wait a moment!\"",
   [("footsteps_sand", "ހިނގަމުން", -24)])
sh(50, "At a girl's call from behind, Shamaan started and turned to look back. A group of girls was coming along behind, joking and laughing.",
   [("gasp", "ސިހިފައި", -22)])
sh(51, "\"Who called me?\" Shamaan asked. \"Hey, you're just making something up to set yourself up with a girl here, right?")
sh(52, "We didn't call you,\" Aroosha said with a mocking smile. \"Sorry.\" Deciding he had imagined it, Shamaan started walking again.")
sh(53, "\"Hey, this girl says salaam!\" Aroosha called out again just then. Shamaan paid it little attention.")
sh(54, "All he had in mind was to get home quickly and rest. By the time he got home it was twelve o'clock. When he went into his room, his mother was asleep beside his little son.",
   [("door_open", "ވަތްއިރު", -22)])
sh(55, "Quietly he took a towel and went to the bathroom. Just as he began to bathe, heavy rain started to fall. The wind rose, and the leaves of the trees could be heard thrashing.",
   [("rain_start", "ވާރޭ", -16), ("wind_gust", "ގަދަވެ", -20), ("leaves_rustle", "ހޫރޭ", -22)])
sh(56, "\"How nice this is. I'll be able to sleep in peace,\" Shamaan thought. But as he came out after his bath,")
sh(57, "it felt as if someone was walking behind him, and he turned to look back. There was no one to be seen. When he went into the room and lay down, the whole room was filled with the scent of a very sweet flower.",
   [("footsteps_pavement", "ހިނގާފައި", -24)], hum=True)
sh(58, "He searched all around, but found nothing that could give off such a scent. Deciding that his mother must have sprayed an air freshener, he tried to sleep.")
sh(59, "Some time in the early hours, Shamaan woke to the sound of someone walking inside the room. When he got up from the bed and looked, there was no one to be seen.",
   [("footsteps_pavement", "ހިނގާ", -24)])
sh(60, "Though a little fear rose in his heart, he took it to be his imagination and went back to sleep. \"Hey, still sleeping?",
   [("breath", "ބިރުވެރިކަމެއް", -24)])
sh(61, "Hurry up, let's go!\" In the morning he woke to his friends calling him. When they went to the field, the games had already begun.")
sh(62, "But since Shamaan's team was playing tonight, today there was only practice. As Shamaan's heart was uneasy,")
sh(63, "instead of playing he went and sat under a tree. \"Let's go to my place for tea. Mum will have made some sweet tea.\" His closest friend Akram came and led Shamaan off towards his house.")
sh(64, "\"Let's go tonight. It's going to be great fun.\" Akram wanted to go to tonight's music show. Shamaan took a deep breath.",
   [("sigh", "ނޭވައެއްލިއެވެ", -20)])
sh(65, "Unlike other young men, he no longer had any interest in having fun or chasing after girls.")
sh(66, "All his hope was to give his beloved son a bright future and to raise him well.")
sh(67, "Even amid the joy of Eid, that responsible thought kept turning in his mind.")
sh(68, "The music show on the island's big ground opened with a lively traditional Dhivehi cultural item.")
sh(69, "The sound of the bodu beru drums and the tunes of all kinds of instruments filled the whole area.")
sh(70, "Everyone on the island, young and old, had gathered there, sitting here and there on chairs set out in every direction.")
sh(71, "Some stood up and cheered; the whole atmosphere was full of joy. Shamaan and Akram had come to share in this joy too,",
   [("applause", "ފޯރިނަގަމުން", -24)])
sh(72, "and they sat on chairs in a quieter, secluded spot with fewer people. Only very few people were nearby.")
sh(73, "Perhaps that was because it was a little far from the stage. But Shamaan felt that, without any trouble,")
sh(74, "he could watch the show in peace sitting there. Akram couldn't sit still there; he was far too caught up in the excitement of the show. \"Shamaan!")
sh(75, "Come on, let's go up front. What are we doing sitting here?\" Akram said. But when Shamaan refused,")
sh(76, "Akram went off alone, as close to the stage as he could get, to feel the excitement up close. Shamaan sat completely lost in the item being performed on stage.",
   [("footsteps_sand", "ދިޔައީ", -24)])
sh(77, "\"Hello... you're so lost in it?\" Suddenly, at the sound of someone speaking, Shamaan gave a start.",
   [("gasp", "ސިއްސައިގެން", -20)], hum=True)
sh(78, "It was a girl who asked him that, laying a hand on his shoulder. When Shamaan looked, she was not a girl he had ever seen on this island before.")
sh(79, "Her looks and her way of dressing were different from the girls of this island. \"Who are you?\" Shamaan said, displeased.")
sh(80, "He was displeased by the girl's lack of decency. Coming up to a man she didn't know,")
sh(81, "and touching him the very first time — that was not something Shamaan accepted. \"I'm Zumra. You were sitting here alone, so I thought I'd talk to you,\" Zumra said with a smile.")
sh(82, "And without even waiting for Shamaan's permission, she sat down on an empty chair near him. \"Which island are you from?",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(83, "I don't know you from this island.\" Shamaan was still displeased. Zumra laughed softly and said, \"You'll find out. Be patient.")
sh(84, "Tomorrow night we'll meet right here.\" Saying that, she got up very quickly and walked off towards the stage.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)], hum=True)
sh(85, "Shamaan did not want to think about it much. Even without knowing who she was or which island she came from,")
sh(86, "he did not like the way she behaved. As he sat there, he saw Akram coming towards him very fast.",
   [("footsteps_sand", "އަންނަތަން", -24)])
sh(87, "He looked as if he was flustered about something, or out of breath. \"Hey! There are some really cool chicks over there. Looks like they're from the island next door.",
   [("breath_heavy", "ނޭވާ", -22)])
sh(88, "Come on, let's go!\" Akram begged. But Shamaan did not change his mind. \"No. It's much more comfortable here.")
sh(89, "I'll stay,\" he said firmly. \"Sit there like that and a jinni will come for you!\" Akram said with a mocking grin.")
sh(90, "Having said that to scare Shamaan, Akram went off again towards the stage, almost at a run.",
   [("footsteps_sand", "ދުވެފައި", -24)])
sh(91, "As soon as Akram left, fear crept into Shamaan's heart. He looked at the darkness all around him.",
   [("heartbeat", "ބިރުވެރިކަމެއް", -20)], hum=True)
sh(92, "Was Zumra, who had just come, really a human being? Or was she a jinni, as Akram had said? With those troubling fears, Shamaan rose from his chair.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)], hum=True)
sh(93, "All he wanted now was to find Akram and go to him.")
SHOTS = S

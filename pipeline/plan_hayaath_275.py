"""Beat/shot plan for Hayaath episode 275 (used by plan_beats.py)."""

LOC = {
    "far_beach": "a deserted moonlit beach on the far side of a Maldivian island, far from the village, a large old two-storey house with a veranda among the palm trees behind the beach",
    "veranda": "the wide wooden veranda of a large old two-storey house among coconut palms on the far side of a Maldivian island, wooden railings and steps leading down to a secluded white-sand beach, the calm lagoon beyond, at sunset",
    "beach_dusk": "the secluded white-sand beach in front of a large old two-storey house among coconut palms on the far side of a Maldivian island, calm lagoon, gentle waves, at sunset turning to dusk",
    "street_memory": "a quiet island roadside at night in the Maldives, warm streetlights, blurred headlights in the background",
    "fazaal_detail": "a wooden side table in a large old house, late afternoon window light",
    "house_lane": "the narrow sandy lane outside the gate of an old Maldivian coral-stone house in the early evening, low white coral walls, a coconut palm, a parked motorbike, a warm porch light by the gate",
    "bedroom": "Hayaathu's small plain bedroom in an old Maldivian coral-stone house in the early evening, a single bed with a simple cotton sheet and pillow, a wooden louvered window, a ceiling fan, a small bedside lamp, a plain wooden door with an old iron bolt",
    "hallway": "a dim narrow hallway in an old Maldivian coral-stone house in the evening, a closed plain wooden bedroom door, a single warm ceiling bulb",
    "sea_memory": "a paved path between palms leading to a moonlit Maldivian beach at night, the sea beyond",
}
MOOD = {
    "far_beach": "night, full moon, silver moonlight, remembered, tender and dreamlike",
    "veranda": "sunset, warm golden-orange light, long soft shadows, tender and hopeful",
    "beach_dusk": "sunset fading into violet dusk, warm horizon, cool blue shadows, pensive and calm",
    "street_memory": "night, warm streetlights, hazy remembered softness",
    "fazaal_detail": "soft quiet light, grief, stillness",
    "house_lane": "early evening, violet-blue sky, warm porch light, lively",
    "bedroom": "early evening to night, dark blue outside the louvers, the warm glow of a small bedside lamp, deep shadows, lonely and tense",
    "hallway": "evening, harsh single warm bulb, tense",
    "sea_memory": "night, moonlight, remembered, ominous",
}

BEATS = [
    # ---- Fazaal at the big house, sunset ----
    dict(to=1, reason="new episode opening: recap of the rescue that made Fazaal's heart change (reused image from ep 273)", reuse="ep273:beat_013",
         chars=["hayaathu", "young_driver"], loc="far_beach",
         visual="(reuse from ep 273) Hayaathu coming round on the moonlit sand, Fazaal kneeling at a distance, astonished", amb="memory",
         sens="other", safe="rescue shown only as the moment she comes round, at a respectful distance (ep 273 image)"),
    dict(to=3, reason="scene change: present day, Fazaal on the veranda of the big house gazing at Hayaathu's photo", chars=["young_driver"], loc="veranda",
         visual="Fazaal sitting on the wooden veranda steps of the big old house at sunset, looking down at a smartphone in his hand whose screen faces away from the viewer and glows softly, a tender surprised smile rising on his lips, the golden lagoon behind him",
         camera="medium shot, slightly low angle", amb="beach_dusk", transition="dissolve"),
    dict(to=7, reason="action change: the call from Yasir, then he looks out to sea with relief", chars=["young_driver"], loc="veranda",
         visual="Fazaal standing at the wooden veranda railing, a phone lowered in one hand, letting out a breath of relief and gazing out at the sunset over the calm lagoon, a calm peaceful face, palm fronds framing the sky",
         camera="medium shot from the side", amb="beach_dusk"),
    dict(to=9, reason="flashback: the tenderness he saw Hayaathu show her sister (reused image from ep 272)", reuse="ep272:shot_037",
         chars=["hayaathu", "dhooma"], loc="street_memory",
         visual="(reuse from ep 272) Hayaathu crying, holding Dhooma's hand under a streetlight", amb="memory", transition="dissolve"),
    dict(to=11, reason="emotional turning point: he resolves to leave hatred behind", chars=["young_driver"], loc="veranda",
         visual="close-up of Fazaal's face in warm golden sunset light, the sea breeze moving his hair, his intense dark eyes softened, a calm determined expression, the glowing lagoon blurred behind",
         camera="close-up, eye level", amb="beach_dusk", transition="dissolve"),
    dict(to=12, reason="action change: he walks down to the shore", chars=["young_driver"], loc="beach_dusk",
         visual="Fazaal walking slowly barefoot across the white sand towards the water's edge at sunset, seen from behind and slightly to the side, hands in his pockets, his footprints trailing behind him, the big old house among the palms in the background",
         camera="wide shot", amb="beach_dusk"),
    dict(to=13, reason="flashback: the night he laid Hayaathu on this beach (reused image from ep 273)", reuse="ep273:beat_012",
         chars=["hayaathu", "young_driver"], loc="far_beach",
         visual="(reuse from ep 273) Hayaathu lying on the moonlit sand, Fazaal standing a few steps away", amb="memory", transition="dissolve",
         sens="other", safe="rescue and carrying not shown; she already lies on the sand and he stands at a distance (ep 273 image)"),
    dict(to=17, reason="back to the present: Fazaal at the water's edge, reflecting on his secret and his 'drama'", chars=["young_driver"], loc="beach_dusk",
         visual="Fazaal standing alone at the water's edge at dusk, hands in his pockets, gentle waves at his feet, looking at the horizon with a pensive, guarded half smile, violet and orange sky, a lone leaning palm",
         camera="medium wide, eye level", amb="beach_dusk", transition="dissolve",
         sens="intimacy", safe="his past romances are not shown; he stands alone"),
    dict(to=19, reason="flashback symbol: his brother Fawaz's tragedy (reused image from ep 274)", reuse="ep274:beat_018", loc="fazaal_detail",
         visual="(reuse from ep 274) a face-down photo frame beside a wilted white flower and a watch", amb="memory", transition="dissolve",
         sens="injury/death", safe="the fire and the disfigured face are never shown; a face-down photo frame and a wilted flower instead"),
    dict(to=21, reason="back to the present: Hayaathu's photo has changed him; the phone rings again", chars=["young_driver"], loc="beach_dusk",
         visual="Fazaal sitting on the trunk of a leaning coconut palm on the beach at dusk, glancing down at the phone lighting up in his hand (screen facing away from the viewer), a quiet confident smile, the lagoon turning violet behind him",
         camera="medium shot", amb="beach_dusk", transition="dissolve"),
    dict(to=24, reason="characters change: Yasir on the other end of the call", chars=["yasir"], loc="house_lane",
         visual="Yasir standing in the sandy lane outside the gate of an old coral-stone house in the early evening, holding a phone to his ear, eyebrows raised in amazement, his free hand gesturing as he talks",
         camera="medium shot, eye level", amb="street_night"),
    dict(to=28, reason="characters change: back to Fazaal, worried by what he hears about Hayaathu", chars=["young_driver"], loc="beach_dusk",
         visual="Fazaal standing on the beach at dusk with the phone to his ear, his smile gone, brows drawn together in concern, listening intently, the darkening sea and palms behind him",
         camera="medium close-up", amb="beach_dusk"),
    dict(to=31, reason="action change: Yasir calls back to tease him", chars=["yasir"], loc="house_lane",
         visual="Yasir leaning against a parked motorbike in the lamp-lit lane, phone to his ear, a teasing suspicious grin and one eyebrow raised, early evening sky",
         camera="medium shot", amb="street_night"),
    dict(to=33, reason="emotional change: Fazaal laughs", chars=["young_driver"], loc="beach_dusk",
         visual="Fazaal alone on the beach at dusk laughing warmly, head tilted back slightly, the phone lowered from his ear, the first stars appearing over the violet lagoon, nobody else nearby",
         camera="medium shot, slightly low angle", amb="beach_dusk", sens="other",
         safe="the 'girl beside him' is only his joke; he is shown alone"),
    # ---- Hayaathu's bedroom, evening ----
    dict(to=35, reason="scene change: Hayaathu back in her room after the ring ceremony", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu lying face down across her bed with her face buried in the pillow, one arm hanging over the edge, her rose dress and blush-pink hijab, the bedside lamp glowing, dusk blue through the louvers",
         camera="medium wide, slightly high angle", amb="room_night", transition="black"),
    dict(to=37, reason="action change: she reads Maaroof's messages", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting up on the bed, holding a smartphone whose screen faces away from the viewer and glows on her face, reading, tears welling in her eyes, the bolted wooden door behind her",
         camera="medium close-up", amb="room_night"),
    dict(to=38, reason="characters change: Zoona knocks at the door", chars=["zoona"], loc="hallway",
         visual="Zoona standing in the dim hallway knocking on the closed wooden bedroom door with her knuckles, calling out with an impatient, irritated face, a smartphone in her other hand",
         camera="medium shot", amb="living_night"),
    dict(to=40, reason="back to Hayaathu reading (reuse)", reuse="beat_016", chars=["hayaathu"], loc="bedroom",
         visual="(reuse) Hayaathu reading the messages, tears", amb="room_night"),
    dict(to=42, reason="action change: she sits on the floor against the bed", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting on the floor with her back against the side of the bed, knees drawn up, the phone clutched to her chest, staring ahead hopelessly with wet cheeks, lamp light from above",
         camera="medium shot, eye level", amb="room_night"),
    dict(to=44, reason="action change: she lies down on the floor and closes her eyes", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu lying curled on her side on the floor beside the bed, fully clothed in her rose dress and blush-pink hijab, eyes closed, a tear on her cheek, the phone lying near her hand, lamp light and shadows",
         camera="low angle from the floor, medium shot", amb="room_night"),
    dict(to=47, reason="action change: a message from an unknown number — Fazaal", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu propped up on one elbow on the floor, looking at the glowing phone in her hand (screen facing away) with surprise, wiping a tear from her cheek with the back of her other hand",
         camera="medium close-up", amb="room_night"),
    dict(to=51, reason="detail image: typing and deleting messages", chars=["hayaathu"], loc="bedroom",
         visual="close-up of a young woman's hands with rose sleeves holding a smartphone, a thumb hovering hesitantly over the softly glowing screen seen at a steep angle so nothing on it is readable, her blush-pink hijab blurred in the background, lamp light",
         camera="extreme close-up", amb="room_night"),
    dict(to=54, reason="emotional turning point: she realises she was typing to Fazaal", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting on the floor against the bed with her eyes shut, one hand pressed to her chest, taking a deep breath of relief, the phone resting in her lap",
         camera="medium close-up", amb="room_night"),
    dict(to=57, reason="emotional change: Fazaal wants to meet her", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu holding the phone tightly against her chest with both hands, eyes squeezed shut, her face full of dread, tears on her lashes",
         camera="close-up", amb="room_night", hum_note="emotional peak"),
    dict(to=61, reason="action change: waiting as the clock moves towards nine", chars=["hayaathu"], loc="bedroom",
         visual="Hayaathu sitting on the edge of the bed in the lamp-lit room, tears gathering in her eyes, the phone in her lap, looking up anxiously at a plain round wall clock with no numbers (only tick marks) on the wall above, its hands near nine",
         camera="medium wide, eye level", amb="room_night"),
    dict(to=63, reason="characters change: Dhooma at the door", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu holding the bedroom door open, her tense face softening with relief; Dhooma in her black wheelchair in the doorway, looking up at her sister with concern, the dim hallway behind",
         camera="medium shot from inside the room", amb="room_night"),
    dict(to=67, reason="action change: the message went to the wrong person", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu standing by the closed door looking at her phone with worried shock, one hand at her mouth; Dhooma in her wheelchair in the middle of the room behind her, watching her anxiously",
         camera="medium wide", amb="room_night"),
    dict(to=71, reason="action change: the sisters talk about Maaroof", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu sitting on the edge of the bed facing Dhooma in her wheelchair; Dhooma leaning forward, looking at her with astonishment and asking; Hayaathu looking down in silence, her hands twisted in her lap",
         camera="medium two-shot, eye level", amb="room_night"),
    dict(to=73, reason="action change: Hayaathu embraces her sister before leaving", chars=["hayaathu", "dhooma"], loc="bedroom",
         visual="Hayaathu bending down to embrace Dhooma, who sits in her wheelchair, whispering near her ear with a brave forced smile; Dhooma's eyes wide with worry",
         camera="medium close-up", amb="room_night"),
    dict(to=74, reason="characters change: Dhooma alone after Hayaathu leaves", chars=["dhooma"], loc="bedroom",
         visual="Dhooma alone in her black wheelchair in the lamp-lit bedroom, looking towards the open doorway where her sister has just gone, sorrow and helplessness on her face",
         camera="medium wide, from behind the bed", amb="room_night"),
    dict(to=75, reason="flashback: Dhooma went into the sea for her sister's happiness (reused image from ep 272)", reuse="ep272:shot_084",
         chars=["dhooma"], loc="sea_memory",
         visual="(reuse from ep 272) Dhooma rolling her wheelchair alone along the moonlit path towards the sea", amb="memory", transition="dissolve",
         sens="other", safe="her going into the sea is shown only as her rolling towards the beach (ep 272 image); no person in the water"),
    dict(to=77, reason="emotional peak: Dhooma prays for her sister", chars=["dhooma"], loc="bedroom",
         visual="Dhooma in her black wheelchair in the lamp-lit bedroom, both palms raised in front of her in quiet supplication (dua), eyes lifted, tears on her cheeks, a peaceful hopeful glow on her face",
         camera="medium close-up, slightly low angle", amb="room_night", transition="dissolve"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "After Maaroof, Fazaal too dived into the sea to save Hayaathu. How tenderness and love for Hayaathu were born in the heart of Fazaal, who had hated women, he did not know.", hum=True)
sh(2, "He kept gazing at Hayaathu's photo on the phone screen. A feeling he couldn't describe came over him.")
sh(3, "Hayaathu's lovely smile seemed to be telling so many stories. A smile rose on Fazaal's lips.")
sh(4, "As he sat lost in the photo, the phone began to ring and the photo vanished. Fazaal answered. 'Hello...' came Fazaal's manly voice.",
   [("phone_buzz", "ރިންގުވާން", -14)])
sh(5, "'Hayaathu has accepted the ring...' came the voice of Fazaal's friend Yasir from the other end. 'Hmm...' Without asking anything more, Fazaal hung up.")
sh(6, "Fazaal let out a breath of relief. The first step had been taken. Before many days pass, Hayaathu may become his.",
   [("sigh", "ނޭވާ", -20)])
sh(7, "He looked out at the sea in front of him. It was as if he had found some kind of peace.")
sh(8, "For so many days he had lived restless, a fire of hatred burning in his heart. Seeing the tenderness Hayaathu showed her sister, it was as if the hatred he felt for women had been wiped from his heart.", hum=True)
sh(9, "That heart now longs for love and tenderness. The world is telling him the truth. He is sure there is no deceit in it.")
sh(10, "Every human being gets the chance to live in this world only once. Then why not make good use of that chance?")
sh(11, "Why should his heart give room to hatred? Yes. He will use that chance to live a successful life.")
sh(12, "He will not let his life go to waste. Fazaal slowly walked down to the shore. Not long ago, one night, he had pulled Hayaathu from the sea as she was sinking and laid her down right here.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(13, "The scene came back to Fazaal. The feeling in his heart when he saw Hayaathu's lovely face in the moonlight is still fresh.", hum=True)
sh(14, "He is impatient to make that beautiful girl his. He has no wish to reveal the secret hidden in his heart.")
sh(15, "Setting his hidden love aside, he had been linked with many girls. Not one girl who came to him in love had ever reached his heart.")
sh(16, "He never meets the girls his father arranges for him to marry either. Before any meeting, the girl's family refuses the marriage.")
sh(17, "That is how it goes — thanks to the success of the drama he has been playing behind his father's back. His name is Fazaal, but the age and the face are those of his brother, seven years older.")
sh(18, "The accident that changed the face of Fazaal's brother Fawaz is not something that has faded from Fazaal's heart.", hum=True)
sh(19, "Because of that accident, the hatred towards women growing in his heart only increased day by day.")
sh(20, "But these last two or three days his mood, his feelings, are different. From the moment his father sent Hayaathu's photo, Hayaathu had become his.")
sh(21, "Not wanting to wait any longer, he decided to arrange the wedding as soon as possible. Once again the phone began to ring. It was Yasir.",
   [("phone_buzz", "ރިނގުވާން", -14)])
sh(22, "After a deep breath Fazaal answered. 'What is it?' Fazaal asked. 'I've just seen Hayaathu and I'm completely stunned.'",
   [("breath", "ފުންނޭވާ", -22)])
sh(23, "There was amazement in Yasir's voice. 'Why?' Fazaal knew why. Still, he wanted to hear it from Yasir's own mouth.")
sh(24, "'You and Hayaathu have met before, haven't you?' Yasir asked quickly. Fazaal fell silent. He didn't want to talk about it any further.")
sh(25, "'We'll talk when I get home,' Fazaal said slowly. 'Okay. Hayaathu is asking for your number... what should I do? Should I give it?'")
sh(26, "came Yasir's voice. 'What happened? Has something gone wrong again?' Fazaal asked. 'I don't know... I think... she looked like she'd been crying a lot.")
sh(27, "Something big is going on in that house... her uncle doesn't seem like a very good man... think about it. So what should I do?")
sh(28, "Should I give her the number?' Yasir asked calmly. 'No... I'll call her... but first find out why she wants the number.'")
sh(29, "Fazaal said calmly. 'Okay...' As soon as Yasir said it, Fazaal hung up. Yasir called back again at once. Fazaal picked up.",
   [("phone_buzz", "ގުޅާލިއެވެ", -16)])
sh(30, "'Hanging up that fast — are you sitting next to some girl?' Yasir asked, full of suspicion. 'So what? Yes, I'm sitting next to a girl.'")
sh(31, "Fazaal said, raising an eyebrow. 'Oh... you get engaged to the prettiest girl on the island,")
sh(32, "and not even an hour later you're cosying up to another woman — where's your shame?' Yasir teased. 'Now stop disturbing me. Tell me what happened...'")
sh(33, "Fazaal said, laughing. 'Now I won't tell you anything... carry on...' Yasir hung up. Fazaal laughed.")
sh(34, "As soon as Hayaathu entered her room, she fell onto the bed. Without her even thinking, her whole life had changed — faster than the blink of an eye.",
   [("soft_thud", "ވެއްޓިގަތެވެ", -18)])
sh(35, "Until yesterday she was Maaroof's to keep. But now, from this very moment, she has become the right of a man she doesn't even know.", hum=True)
sh(36, "Hayaathu marvelled at the way the world turns. She lifted her face from the pillow, reached out, found her phone, picked it up and opened it.",
   [("cloth_rustle", "ހިއްލާލިއެވެ", -24)])
sh(37, "She began to read the long messages Maaroof had sent. She got up from the bed and quickly shut and locked the door, afraid someone would come before she finished reading.",
   [("door_close", "ލައްޕާ", -18), ("lock_click", "ތަޅުލިއެވެ", -16)])
sh(38, "And that is exactly what happened. Zoona's voice came, knocking at the door. 'Hayaathu... Yasir is here, Fazaal sent him...' Zoona said loudly.",
   [("knock", "ޖަހާލަމުން", -12)])
sh(39, "'I'm having a bath...' Hayaathu said quickly in a tearful voice, not wanting to open the door. All she wanted now was to sit alone and read Maaroof's messages.")
sh(40, "The more she read, the more the tears poured from her eyes. As the sobs rose, she bit down on her lip.",
   [("sob_breath", "ގިސްލެވެމުން", -24)], hum=True)
sh(41, "Leaning back against the bed, she sat on the floor. What answer could she give to those messages? If her uncle found out she had replied, he would make her days a misery.")
sh(42, "And the punishment would fall on her beloved sister and on Maaroof. Even when one is forced, this is too much — forced until patience breaks and hands and feet lose their way.", hum=True)
sh(43, "Slowly she lay down on the floor. The tears were still falling. Hayaathu closed her eyes. Just then Zoona knocked on the door again.",
   [("knock", "ޖަހާލިއެވެ", -12)], hum=True)
sh(44, "'Still not done? How long has Yasir been waiting outside...' Zoona said harshly. 'Not done yet...' Hayaathu said, lying just as she was.")
sh(45, "At that moment a message came to Hayaathu's phone. Opening her eyes quickly, she looked at the phone, thinking it was from Maaroof.",
   [("phone_buzz", "މެސެޖެއް", -16)])
sh(46, "It was a message from an unknown number. 'This is my number — Fazaal.' Hayaathu read the message.")
sh(47, "The call a little while ago had come from that same number. Hayaathu wiped the tears from her eyes, and typed a reply.")
sh(48, "'Why would I want your number?' Hayaathu typed and sent. 'Yasir said you asked for my number.' Another message arrived.",
   [("phone_buzz", "އައެވެ", -16)])
sh(49, "'No... I didn't ask for it.' Hayaathu typed and sent it. No reply came. Hayaathu sat staring at the phone.")
sh(50, "Hayaathu typed again. After looking at it for a while, she deleted it. Then she wrote another message.",
   [("phone_game_taps", "ޓައިޕް", -24)])
sh(51, "She looked at it and deleted it. Like that, she kept writing and erasing message after message — absent-mindedly, thinking she was writing to Maaroof's number.")
sh(52, "'?????' Suddenly a message came from Fazaal's phone — nothing but question marks. Hayaathu stared at it in astonishment.",
   [("phone_buzz", "ކުއްލިޔަކަށް", -14)])
sh(53, "Realising she had been writing and erasing those messages in Fazaal's chat, Hayaathu took a deep breath and closed her eyes.",
   [("breath", "ނޭވާއެއް", -20)])
sh(54, "'Thank God not one message got sent,' Hayaathu said to herself. Another message came. Hayaathu read it.",
   [("phone_buzz", "އައެވެ", -16)])
sh(55, "'I want to meet you...' Hayaathu read Fazaal's message. She squeezed her eyes shut. 'Meet him...")
sh(56, "I won't go to meet him. The moment I see his face my heart will break...'", hum=True)
sh(57, "Hayaathu said softly to herself. 'At nine... Yasir will come to pick you up.' Another message had arrived on Hayaathu's phone.",
   [("phone_buzz", "އައެވެ", -16)])
sh(58, "Hayaathu's heart began to pound. But she had no reason not to go. Now she was Fazaal's by right. She had to obey his wish.",
   [("heartbeat", "ތެޅިގަނެގެން", -16)])
sh(59, "But would Hayaathu dare to look at that face? Could the place Maaroof holds in her heart ever be given to Fazaal?", hum=True)
sh(60, "Once again tears began to gather in Hayaathu's eyes. Her heart beat as loudly as the tick-tock of the clock.",
   [("heartbeat", "ވިންދުޖަހަމުން", -16)], hum=True)
sh(61, "As the clock's hand went round, Hayaathu's anxiety only grew. Hayaathu picked up the phone and typed a message.",
   [("phone_game_taps", "ޓައިޕްކޮށްލިއެވެ", -24)])
sh(62, "Before she could send it, there was a knock on the door. 'Hayaathu, it's Dhontha — open the door.' Dhooma's voice came from outside.",
   [("knock", "ދޮރުގައިޓަކިޖަހާލި", -12)])
sh(63, "Hayaathu hurriedly sent the message, then went and opened the door. Seeing Dhooma, Hayaathu breathed a sigh of relief.",
   [("door_open", "ދޮރުހުޅުވާލިއެވެ", -16), ("sigh", "ނޭވާއެއް", -22)])
sh(64, "As soon as Dhooma came in, Hayaathu shut the door. Then she picked up the phone and looked. When she saw who the message had gone to, she closed her eyes in dismay.",
   [("wheelchair_roll", "ވަނުމުން", -20), ("door_close", "ދޮރުލައްޕާ", -18)])
sh(65, "She deleted the message. Then she typed it again and sent it to Maaroof.")
sh(66, "When she goes with Yasir to meet Fazaal, Hayaathu had decided to secretly meet Maaroof without them knowing.")
sh(67, "She wrote that and sent the message to Maaroof. But the first message had gone to Fazaal. Luckily for Hayaathu, Fazaal hadn't looked at it.")
sh(68, "'What happened?' Dhooma asked. 'Dhontha... I want to meet Maaroof,' Hayaathu said quickly.")
sh(69, "Dhooma looked at Hayaathu in astonishment. 'But how?' Dhooma asked. 'I've just messaged Maaroof...'")
sh(70, "Hayaathu said softly. 'But Hayaathu... if you want to go with Maaroof, why did you accept the ring to marry that man?' Dhooma asked in astonishment.")
sh(71, "Hayaathu stood silent, giving no answer. 'Hayaathu... they've come to pick you up,' came Zoona's voice from outside. Hayaathu looked at Dhooma.")
sh(72, "Trying hard to smile, she embraced Dhooma. 'Dhontha, I won't take a wrong step... but I want to see Maaroof just once...'", hum=True)
sh(73, "Hayaathu whispered softly near Dhooma's ear. Then she walked out of the room. Dhooma looked after her, towards where Hayaathu had gone.",
   [("footsteps_pavement", "ނިކުމެގެން", -26)])
sh(74, "She grieves with her little sister for the sorrow she carries because of their uncle's cruelty. But what can she possibly do?", hum=True)
sh(75, "Even throwing herself into the sea was because she wanted to bring her little sister some happiness. But even after that, Hayaathu's life only grew harder, and she was forced.", hum=True)
sh(76, "Tears began to gather in Dhooma's eyes. Praying for God's mercy on her little sister, she raised her hands.", hum=True)
sh(77, "She prayed that the person coming into Hayaathu's life would be a kind-hearted man who would love gentle Hayaathu beyond measure.", hum=True)
SHOTS = S

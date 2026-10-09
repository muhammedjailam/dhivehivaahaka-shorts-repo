"""Beat/shot plan for Sahar episode 574 (used by plan_beats.py).
Spring 1948. Evening at Hashim's house in Ein Karem: the decision to flee to Jordan tonight; the truck is loaded. On the
French ship Claire tells Yazan why he was spared; a storm; Yazan's vow, seasickness and dua. 3 a.m.: Hashim locks his
house forever; the night drive past the drunk checkpoint fighters; Sahar weeps, Ameen comforts her; Fajr in the truck bed
at Ramadha; 6 a.m. the Jordanian border, the phone call to Abdullah, permission, tears of joy; the plan to accept
Jordanian citizenship. Rules (series bible): no violence/weapons/flags/text; hijab fully covering hair and neck on every
woman; Sahar's LEFT forearm in a plain cloth sling; Claire always >= two arm's lengths from Yazan with an open door/deck;
drunk fighters = far-off swaying silhouettes round a small fire, no bottles; seasickness = gripping the porthole rim."""

SLING = "her LEFT forearm resting in a plain cloth sling made from a strip of plain cream cloth (no visible injury)"
SAHAR = f"Sahar in her black thobe with deep-red embroidery and black hijab fully covering her hair and neck, {SLING}"
YAZ = ("Yazan in his usual clothes, dusty and creased, his black-and-white keffiyeh around his neck, his hands loosely "
       "wrapped in clean white cloth at the wrists and palms, no wounds")
CLAIRE_FAR = ("Claire in her navy ankle-length crew uniform and navy headscarf, arms folded, standing at least two arm's "
              "lengths away from Yazan, they never touch, nothing romantic")
HIJAB = "every woman's headscarf fully covers her hair and neck"

LOC = {
    "dinner": "the main room of Hashim's old stone house in Ein Karem at night: thick golden limestone walls, a deep arched "
              "window with closed wooden shutters, woven rugs and floor cushions, a low round wooden table with copper "
              "plates and clay bowls left from dinner, an oil lamp on a wall niche, wooden chests along the wall",
    "courtyard": "the stone courtyard of Hashim's house in Ein Karem at night: a high limestone wall with an arched wooden "
                 "gate, a fig tree, an old 1940s flatbed truck with a wooden cargo bed being loaded with wooden chests, "
                 "rolled rugs, sacks and copper pots, a hurricane lantern hanging from the tailboard",
    "lane_night": "a dirt lane leading out of the green valley village of Ein Karem at night, stone houses with dark "
                  "windows, terraced hills and cypress trees in silhouette, the lane curving away into the darkness",
    "balcony": "the small private balcony of a surprisingly elegant cabin on the top deck of an old 1940s French passenger "
               "steamship at sea: a polished wooden rail, two wooden deck chairs placed far apart, the cabin's glass "
               "balcony door wide open behind, the open grey-blue Mediterranean to the horizon",
    "ship_sea": "an old black-and-white 1940s passenger steamship with one tall funnel sailing alone on the open "
                "Mediterranean, seen from a distance, dark storm clouds massing above it, the far coastline of hills "
                "fading behind",
    "cabin_storm": "the inside of an elegant 1940s ship cabin: polished wood panelling, a round brass porthole, a small "
                   "writing desk with nothing on it, an armchair, the glass balcony door now shut and streaming with rain, "
                   "the cabin's wooden corridor door standing WIDE OPEN onto a dim wood-panelled ship corridor",
    "cabin_night": "the same elegant 1940s ship cabin during a storm: polished wood panelling, a round brass porthole "
                   "streaming with rain and spray, a swaying brass wall lamp, an armchair, a plain rug on the floor",
    "door_3am": "the arched wooden front door of Hashim's old limestone house in Ein Karem at night, worn stone steps, a "
                "jasmine vine on the wall, an old iron key in the lock",
    "lane_truck": "the dirt lane outside Hashim's house in Ein Karem at night, the old 1940s flatbed truck standing with "
                  "its headlights on, its wooden cargo bed piled with chests, rugs and sacks and a small space at the "
                  "back for people",
    "truck_bed": "the back of the old 1940s truck's wooden cargo bed at night, piled chests, rolled rugs and sacks, wooden "
                 "side boards, the dark terraced hills and a starry sky passing behind",
    "checkpoint": "a dark potholed road through the hills outside Jerusalem at night, low stone walls, a few stone houses "
                  "with one or two dimly lit windows, the silhouettes of old-city domes faint on the far horizon",
    "dawn_road": "a roadside on a hilly road near Ramadha at the break of dawn, the old 1940s truck pulled over beside "
                 "olive terraces, a distant small mosque dome silhouette on a hill",
    "rough_road": "a rough rocky potholed dirt road winding down through bare hills toward the Jordan valley before "
                  "sunrise, the old 1940s flatbed truck piled with chests driving fast, dust rising",
    "border": "the Jordanian border crossing in the early morning: a dusty road, a distant small wooden border post with a "
              "simple wooden barrier pole, a small stone hut, a couple of small distant figures, bare golden hills",
    "border_hut": "inside a small stone border hut: rough limestone walls, a small wooden window letting in golden early "
                  "morning light, an old wooden wall-mounted crank telephone with a brass bell and a hand crank, a plain "
                  "wooden table with folded blank papers",
    "cab": "inside the cab of an old 1940s truck driving through Jordan in the morning: a big thin steering wheel, a "
           "simple metal dashboard with round blank gauges, the windscreen showing a long dusty road and golden hills",
    "truck_back_day": "the back of the old 1940s truck's wooden cargo bed in the morning on a road in Jordan, piled chests "
                      "and rugs, looking back west over golden hills toward a faint hazy horizon",
    "plain": "a vast open golden plain in Jordan, a long straight dusty road running toward low hills and the morning sun",
}
MOOD = {
    "dinner": "night oil-lamp glow, warm amber light on faces against deep blue-charcoal shadows, fear and urgency",
    "courtyard": "night, deep blue sky with stars, the warm amber glow of the hurricane lantern, hurried and anxious",
    "lane_night": "moonlit night, cold blue light, a sorrowful exodus, quiet fear",
    "balcony": "overcast late afternoon at sea, grey-silver light, a cool sea wind, melancholy and guarded",
    "ship_sea": "storm at sea gathering, heavy charcoal clouds, a thin strip of ember light on the horizon, ominous",
    "cabin_storm": "storm at sea, rain lashing the balcony glass, the warm glow of a brass wall lamp inside, grey storm "
                   "light outside, tense and uncertain",
    "cabin_night": "storm at sea at night, a swaying brass wall lamp throwing warm amber light, deep blue storm darkness "
                   "outside the porthole, lonely, fearful, prayerful",
    "door_3am": "moonlit night at 3 a.m., cold blue moonlight on the limestone, a faint warm lantern glow, heartbreak "
                "and farewell",
    "lane_truck": "moonlit night at 3 a.m., the truck's yellow headlight beams in the dark lane, deep blue shadows, tense",
    "truck_bed": "moonlit night, cold blue moonlight and stars, deep shadows, sorrowful and fearful",
    "checkpoint": "night, deep blue darkness, a small orange fire glowing far off, a tense silent passing",
    "dawn_road": "dawn blue-gold, a grey-blue sky with the first gold on the eastern horizon, hushed and prayerful",
    "rough_road": "first light before sunrise, blue-grey sky turning pale gold in the east, dust, urgent",
    "border": "spring morning gold at 6 a.m., low golden sunlight and long shadows, hopeful and anxious",
    "border_hut": "spring morning gold, a shaft of warm golden light through the small window, dust motes, hopeful",
    "cab": "spring morning gold, warm sunlight through the windscreen, thoughtful and resolute",
    "truck_back_day": "spring morning gold with a faint smoky haze on the far western horizon, bittersweet",
    "plain": "spring morning gold, a wide bright sky, a sense of a new beginning, quietly hopeful",
}

BEATS = [
    dict(to=5, reason="episode opening: the decision to flee at Hashim's house after dinner",
         chars=["sahar", "hashim", "safoora", "hamza"], loc="dinner",
         visual=f"Hashim with his round glasses and white beard sitting on a floor cushion by the low table, speaking "
                f"earnestly with one hand raised; beside him Hamza in his red-and-white keffiyeh listening gravely; "
                f"{SAHAR}, sitting on a cushion across the table with tears welling in her eyes; Safoora in her white "
                f"headscarf leaning over the table gathering the copper plates, looking up decisively; {HIJAB}",
         camera="medium wide shot, eye level, faces in the upper two-thirds, the rug and table edge as a calm lower third",
         amb="stone_house_night"),
    dict(to=8, reason="scene change: the courtyard — checking and loading the truck", chars=["hashim", "hamza"],
         loc="courtyard",
         visual="Hashim kneeling beside a front tyre of the old truck working a simple hand tyre pump, Hamza in his "
                "red-and-white keffiyeh lifting a wooden chest up onto the heavily loaded wooden cargo bed, the lantern "
                "glowing, the truck bed almost full",
         camera="wide shot, slightly low angle, the truck filling the upper two-thirds, the courtyard stones below",
         amb="night_exterior"),
    dict(to=10, reason="scene change: the exodus — many families leaving the area, some on foot", loc="lane_night",
         visual="seen from behind and far away, a few families walking away down the moonlit lane carrying bundles, a "
                "rolled rug and a lantern, the women in long dresses and headscarves, a donkey with sacks; nobody's face "
                "visible, a mood of forced departure",
         camera="wide shot from behind, the lane leading into the distance, the dirt lane as the calm lower third",
         amb="night_exterior", sens="war",
         safe="the fear after Deir Yassin is shown only as families walking away at night, seen from behind"),
    dict(to=14, reason="action change: Hamza's worry about passports, Hashim's plan", chars=["hashim", "hamza"],
         loc="courtyard",
         visual="Hashim and Hamza standing face to face beside the loaded truck under the hanging lantern; Hamza "
                "frowning with worry, both hands open in question; Hashim calm and reassuring, one hand on Hamza's "
                "shoulder, talking quickly",
         camera="medium two-shot, eye level, faces in the upper third", amb="night_exterior"),
    dict(to=17, reason="storyline cut to the ship: Claire introduces herself on Yazan's balcony",
         chars=["claire", "yazan"], loc="balcony", transition="black",
         visual=f"{CLAIRE_FAR}, standing by the far end of the balcony rail with the open cabin door beside her, "
                f"speaking calmly; {YAZ}, sitting on the second deck chair at the opposite end of the balcony, listening "
                f"warily; a wide empty space of deck between them",
         camera="wide shot, eye level, both figures in the upper two-thirds, the deck boards and sea below",
         amb="ship_deck", sens="intimacy",
         safe="bible rule 8: Claire stands arms folded far from Yazan on the open balcony, no closeness"),
    dict(to=19, reason="narrated explanation: the ship and its prisoners — symbolic wide view", loc="ship_sea",
         visual="the old steamship small on the wide grey sea, dark storm clouds massing above it, a few tiny blurred "
                "figures sitting along a lower deck rail far away, no faces, no flags, no markings",
         camera="extreme wide shot, the ship in the upper half, open water as the lower third", amb="ship_deck",
         sens="war", safe="the prisoners are only tiny blurred distant figures; no guards, no restraints"),
    dict(to=21, reason="emotional turn: Yazan's despair — why was he not killed", chars=["yazan", "claire"],
         loc="balcony",
         visual=f"close on {YAZ}, sitting forward on the deck chair, his eyes wet and despairing, his wrapped hands "
                f"resting loosely on his knees; far behind him, small and out of focus, {CLAIRE_FAR}, by the rail",
         camera="medium close-up on Yazan, eye level, his face in the upper third", amb="ship_deck"),
    dict(to=22, reuse="beat_006", reason="return: the Saudi warning and the planned state — symbolic storm clouds over "
         "the old ship", loc="ship_sea", amb="ship_storm", visual="(reuse of beat_006)", sens="other",
         safe="bible rule 9: politics shown only as storm clouds over an old ship at sea, no flags"),
    dict(to=26, reason="scene/action change: the rain drives them inside the cabin; Claire leaves",
         chars=["claire", "yazan"], loc="cabin_storm",
         visual=f"{CLAIRE_FAR}, standing in the WIDE OPEN corridor doorway of the cabin with a faint kind smile, about to "
                f"leave; {YAZ}, seated in the armchair on the far side of the cabin by the rain-streaked balcony door; "
                f"the whole width of the cabin between them",
         camera="wide shot from inside the cabin, eye level, the open doorway and Yazan both in the upper two-thirds, "
                "the rug as the calm lower third", amb="ship_storm", sens="intimacy",
         safe="bible rule 8: cabin door wide open, Claire in the doorway, Yazan seated far from her"),
    dict(to=31, reason="character focus: Yazan alone, his questions and his vow to find Sahar", chars=["yazan"],
         loc="cabin_night",
         visual=f"{YAZ}, sitting alone on the edge of the armchair in the swaying lamplight, staring at his wrapped "
                f"hands, his jaw set with fierce determination, his lips moving as he talks to himself, rain on the "
                f"porthole",
         camera="medium shot, slightly low angle, his face in the upper third", amb="ship_storm"),
    dict(to=33, reason="action change: the storm makes him seasick", chars=["yazan"], loc="cabin_night",
         visual=f"{YAZ}, standing and gripping the brass rim of the round porthole with both wrapped hands, his eyes "
                f"shut tight, his face pale and strained, the cabin tilted by the rolling ship, spray on the glass",
         camera="medium close-up, slightly dutch angle, his face in the upper third", amb="ship_storm", sens="other",
         safe="bible rule 11: seasickness = gripping the porthole rim with eyes shut, no vomit"),
    dict(to=35, reason="action change: Yazan prays for safety", chars=["yazan"], loc="cabin_night",
         visual=f"{YAZ}, sitting on the plain rug on the cabin floor facing the porthole, both wrapped hands raised "
                f"before his chest in dua, eyes closed, lips moving, calm returning to his face",
         camera="medium wide shot from the side, eye level, his face in the upper two-thirds", amb="ship_cabin"),
    dict(to=38, reason="storyline cut and time jump: 3 a.m., Hashim locks his house forever",
         chars=["hashim", "safoora"], loc="door_3am", transition="black",
         visual="Hashim standing frozen on the stone step before his locked front door, the old iron key still in his "
                "hand, tears behind his round glasses, holding his wife Safoora's hand; Safoora in her white headscarf "
                "beside him, sad but steady, looking at him with gentle encouragement",
         camera="medium shot from a slight angle, eye level, faces in the upper third, the stone steps below",
         amb="night_exterior"),
    dict(to=42, reason="action change: everyone boards and the truck sets off near 3 a.m.",
         chars=["hashim", "hamza", "sahar"], loc="lane_truck",
         visual=f"Hashim at the open driver's door of the truck, one foot on the step, looking back over his shoulder "
                f"with a shrewd calm expression; at the back of the truck Hamza in his red-and-white keffiyeh holding "
                f"the hand of his daughter {SAHAR}, helping her climb up into the small space in the cargo bed",
         camera="wide shot, eye level, the truck in the upper two-thirds, the dark lane below", amb="truck_night"),
    dict(to=45, reason="scene change: in the moving truck bed Sahar thinks of Yazan",
         chars=["sahar", "laila", "fathimaa"], loc="truck_bed",
         visual=f"{SAHAR}, sitting at one edge of the truck bed against the side boards, looking out at the dark hills, "
                f"a tear on her cheek; behind her, sitting upright and awake among the chests, Laila in her indigo thobe "
                f"and long white headscarf and Fathimaa in her forest-green thobe and cream headscarf, huddled and "
                f"anxious; {HIJAB}",
         camera="medium shot, eye level, faces in the upper two-thirds, the wooden truck bed as the lower third",
         amb="truck_night"),
    dict(to=48, reason="character enters focus: Ameen comforts his sister", chars=["sahar", "ameen"], loc="truck_bed",
         visual=f"{SAHAR}, wiping her tears with her right hand; her younger brother Ameen (14, grey shirt) sitting close "
                f"beside her with a protective arm around her shoulders, trying to be brave, his own eyes sad",
         camera="medium close-up two-shot, eye level, faces in the upper third", amb="truck_night", sens="intimacy",
         safe="bible rule 7: only her brother puts an arm round her shoulders"),
    dict(to=51, reason="scene change: passing the checkpoints of the drunk fighters near Jerusalem", loc="checkpoint",
         visual="the dark loaded truck driving past along the potholed road in the foreground, seen from behind; far "
                "off beside the road a small campfire with a few dark faceless silhouettes swaying around it, no "
                "bottles, no weapons, no uniforms, no flags",
         camera="wide shot from behind the truck, the fire small in the distance, the road as the lower third",
         amb="checkpoint_night", sens="war",
         safe="bible rule 11: the drunk fighters are only far-off swaying silhouettes around a small fire"),
    dict(to=53, reuse="beat_015", reason="return to Sahar in the truck bed: sleepless, doing dhikr until dawn",
         loc="truck_bed", amb="truck_night", visual="(reuse of beat_015)", chars=["sahar", "laila", "fathimaa"]),
    dict(to=55, reason="scene/time change: dawn near Ramadha — Fajr prayed inside the truck",
         chars=["sahar", "hamza", "fathimaa", "laila"], loc="dawn_road",
         visual=f"the family sitting in the truck bed among the chests at dawn with their hands raised in dua, faces "
                f"calm and devout: Hamza in his red-and-white keffiyeh, Fathimaa in her cream headscarf, Laila in her "
                f"white headscarf, and {SAHAR} raising her right hand; {HIJAB}",
         camera="medium wide shot from the side of the truck, eye level, faces in the upper two-thirds",
         amb="desert_dawn", sens="other",
         safe="bible rule 10: prayer shown as the family sitting in the truck bed with hands raised; no adhan sound"),
    dict(to=58, reason="action change: Hashim races the dawn along rough roads", chars=["hashim"], loc="rough_road",
         visual="the loaded truck bouncing fast along the rocky road toward the camera, dust rising behind it, Hashim "
                "visible through the windscreen gripping the big steering wheel with concentration, the eastern sky "
                "turning gold",
         camera="wide low-angle shot, the truck in the upper two-thirds, the rocky road as the lower third",
         amb="truck_back"),
    dict(to=60, reason="scene change: 6 a.m. at the Jordanian border", chars=["hashim"], loc="border",
         visual="the truck stopped at the end of a short line of carts and one other old vehicle on the dusty road; "
                "Hashim stepping down from the cab with a deep breath; far ahead a small wooden border post with a "
                "simple barrier pole and two small distant figures; no flags, no signs",
         camera="wide shot from behind and beside the truck, the border post small in the distance",
         amb="border_post_day"),
    dict(to=62, reason="scene change: Hashim telephones his son Abdullah from the border hut", chars=["hashim"],
         loc="border_hut",
         visual="Hashim standing at the old wooden wall crank telephone, the receiver to his ear, his other hand "
                "turning the crank, listening hopefully through his round glasses in the golden window light",
         camera="medium shot, eye level, his face in the upper third", amb="border_post_day"),
    dict(to=64, reason="emotional turning point: permission granted, tears of joy",
         chars=["sahar", "laila", "fathimaa", "hashim"], loc="border",
         visual=f"at the tailboard of the truck in the golden morning light, Hashim holding up folded blank papers with "
                f"a broad smile; in the truck bed Laila and Fathimaa hugging {SAHAR}, all three with tearful joyful "
                f"smiles; {HIJAB}",
         camera="medium wide shot, eye level, faces in the upper two-thirds", amb="border_post_day", sens="intimacy",
         safe="bible rule 7: only the women (mother and mother-in-law) hug Sahar"),
    dict(to=66, reason="scene change: driving on into Jordan, Hashim explains the plan", chars=["hashim", "hamza"],
         loc="cab",
         visual="seen from outside through the open side window of the moving truck's cab: Hashim at the big steering "
                "wheel talking seriously, glancing aside at Hamza in his red-and-white keffiyeh sitting beside him, who "
                "listens and nods slowly; the truck door's weathered green paint and the dusty road below",
         camera="medium two-shot from outside beside the driver's door, faces in the upper third, the door panel and "
                "dusty road as the calm lower third", amb="truck_back"),
    dict(to=69, reason="focus change: the family looks back toward the homeland they lost",
         chars=["sahar", "ameen", "laila", "fathimaa"], loc="truck_back_day",
         visual=f"seen from beside the truck bed, {SAHAR}, her brother Ameen in his grey shirt, Laila in her white "
                f"headscarf and Fathimaa in her cream headscarf sitting among the chests and looking back west toward "
                f"the hazy hills of Palestine, faces sad and thoughtful; {HIJAB}",
         camera="medium wide shot, eye level, faces in the upper two-thirds", amb="truck_back", sens="war",
         safe="the looting and burning of their homes is only a faint haze over the far horizon"),
    dict(to=71, reason="episode ending: the road ahead into Jordan", loc="plain",
         visual="the small loaded truck far away on the long straight road across the golden plain, driving toward "
                "the morning sun and the low hills, a thin trail of dust behind it",
         camera="extreme wide shot, the sky and sun in the upper half, the road as the lower third", amb="vast_plain"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"We can't stay here. Next they'll come for us. If we fall into their hands, they won't hesitate even to kill us all.\"")
sh(2, "Hashim said. \"Then they will kill my husband, won't they?\" Sahar was close to tears. \"No, my child!",
   [("sob_breath", "ރޮވޭ", -24)], hum=True)
sh(3, "God willing, your husband will be safe,\" Hashim said to give Sahar courage. \"Then there's nothing to delay for.")
sh(4, "Let us set out tonight with our guests. Almighty God will grant us good,\" Safoora said as she gathered up the plates from the meal.",
   [("cup_clatter", "ތަށިތައް", -20)])
sh(5, "Everyone agreed with Safoora. They hurried to pack whatever could be taken into boxes and get ready.",
   [("cloth_rustle", "ފޮށިތަކަށް", -22)])
sh(6, "Hashim and Hamza went to check that the truck arranged for the journey was in good order, and to pump air into the tyres.")
sh(7, "When they were ready to go after several hours, it was eight o'clock at night. Everything that could be taken from Hashim's house was loaded onto the truck.",
   [("soft_thud", "އެރުވިއެވެ", -20)])
sh(8, "Now there was only a small space left on the truck for people to climb in. By then many people had already started leaving the area.")
sh(9, "After 'Deir Yassin', the fear that their area too would be overrun had risen in everyone's heart.")
sh(10, "They were leaving their own homes because they had no choice. With no destination, some were even travelling on foot.",
   [("footsteps_sand", "ފައިމަގުގައި", -24)])
sh(11, "\"What will people without passports do? Will they let us into Jordan without passports?\" Hamza asked. \"Don't worry about that.")
sh(12, "A friend of my son Abdullah works in Jordanian immigration. He said that once we get near the border, I should go into a phone booth and call.")
sh(13, "I know that when you suddenly have to flee your home, nobody will have a passport.")
sh(14, "That's why I asked that young man how to handle it.\" Without even giving a chance for another question, Hashim told them the whole story.")
sh(15, "The girl sat down in one of the two chairs on the balcony and settled herself. Then she asked Yazan to sit in the chair beside it.",
   [("creak", "އިށީނދެލައި", -22)])
sh(16, "\"My name is 'Claire'. I'm one of the crew of this ship. Every year this ship leaves France and makes a voyage around the world.")
sh(17, "This time too it set out that way, and on the way back to France, at a request from England, the ship came close to this region.")
sh(18, "After we arrived here, they said the ship had been brought to take some prisoners to France. When we spoke to the French authorities, we learned what was going on.")
sh(19, "There are about thirty prisoners on board. But only Yazan was brought from 'Deir Yassin'. The rest were all brought from the 'Jerusalem' area.\"")
sh(20, "Claire told him everything while watching Yazan's face. \"Why me? Why didn't they kill me?\" Yazan said, sitting there in despair.",
   hum=True)
sh(21, "\"Don't talk like that, Yazan! As far as I know, they tried to kill all the prisoners.")
sh(22, "But because Saudi Arabia warned that it would not let them establish the state they are trying to establish, we believe Yazan too was let go without being killed.\"")
sh(23, "Claire said kindly. It began to rain and the sea grew rough. Yazan and Claire went inside the room and shut the balcony door.",
   [("rain_start", "ވިއްސާރަވެ", -18), ("wave_crash", "ކަނޑުގަދަވާން", -20), ("door_close", "ލައްޕާލިއެވެ", -20)])
sh(24, "\"I'll go now. It really feels like a storm is coming. The restaurants are on the first deck of the ship. Don't stay hungry.\"",
   [("thunder", "ތޫފާނެއްގެ", -20)])
sh(25, "Claire spoke with a smile. \"How many days will it take to reach France?\" Yazan asked. \"We'll get there in about five days.")
sh(26, "You should go out and look around the ship. When the sea calms down, I'll come and see you, Yazan. I have to go without telling you all the things I came to tell you,\" Claire said as she closed the cabin door.",
   [("door_close", "ލައްޕާލަމުން", -22)])
sh(27, "Many questions rose in Yazan's heart. \"Why is this girl taking pity on me?")
sh(28, "Why did she come to my room and tell me all this?\" Yazan wanted answers to those questions.")
sh(29, "But Yazan kept advising himself to think things through and go forward carefully. He realised that the days ahead would be safe only if he acted wisely.")
sh(30, "\"By the mercy of Almighty Allah I will find my family... For that I will make any sacrifice I have to...")
sh(31, "I will still get my Sahar back...\" Like a man possessed, Yazan kept talking to himself. The sea grew rough,",
   [("wave_crash", "ކަނޑުގަދަވެ", -18)], hum=True)
sh(32, "and as the ship rolled from side to side, Yazan's head began to ache. He felt sick to his stomach and began to throw up.",
   [("creak", "ތަޅުވަމުންދާތީ", -18), ("breath_heavy", "މޭނުބައިކޮށް", -24)])
sh(33, "Until the sea calmed, Yazan tried to get some sleep. He had never made a sea voyage before, so he was uneasy and frightened.")
sh(34, "But Yazan was a courageous young man, so this time too he went on bravely, putting his trust in Almighty Allah.")
sh(35, "Yazan spent the time in dua, asking that the days ahead be made safe and that he be granted the good fortune of reaching a shore of safety.")
sh(36, "After locking the door of his house for good, Hashim stood frozen. \"I thought I would die here...",
   [("lock_click", "ތަޅުލުމަށްފަހު", -16)])
sh(37, "But because of an evil people we have had to leave even our own homeland...\" Hashim said, holding Safoora's hand.",
   [("sigh", "ވަޒަން", -22)], hum=True)
sh(38, "\"That too is Allah's mercy; we must be patient... This is far better than falling into the hands of these Jews.\" However sad she was, Safoora tried to give Hashim courage.")
sh(39, "Once everyone had climbed onto the truck, they set off for Jordan when it was nearly three in the morning.",
   [("truck_start", "ފެށީ", -16)])
sh(40, "The reason was that on the road from 'Ein Karem' into 'Jerusalem City', the fighters were out celebrating,")
sh(41, "and Hashim was sure that by this hour of the night their activity would have died down. \"They drink alcohol and all sorts of things.")
sh(42, "After drinking, by now they'll be finished. So even if we drive past, they won't notice,\" Hashim said shrewdly.")
sh(43, "Everyone sat with fear in their hearts. On a journey expected to take about three hours, they all kept wondering how things would turn out.")
sh(44, "Sahar, sitting at one edge of the back of the truck, kept thinking about Yazan. \"How good it would be if Yazan were here.")
sh(45, "He would never let my courage fail. He would tell me all kinds of stories to comfort me.")
sh(46, "What a great trial I have been made to face.\" Wiping away the tears falling from her eyes, Sahar said to herself. \"Sister, are you crying?\"",
   [("sob_breath", "ކަރުނަތައް", -24)], hum=True)
sh(47, "asked Ameen, sitting next to Sahar. \"I keep remembering Yazan... I don't even know what state the poor man is in...\"")
sh(48, "Not knowing what to say to comfort her, Ameen sat holding Sahar close. Though his heart was breaking to pieces, Ameen stayed strong for his sister.",
   [("cloth_rustle", "ބައްދާލައިގެން", -24)], hum=True)
sh(49, "Sahar and the others travelled on through the 'Jerusalem' area. Hashim had spoken the truth. The fighters were so drunk they no longer knew what was happening.",
   [("fire_crackle", "ހަނގުރާމަވެރިން", -24)])
sh(50, "Although checkpoints had been set up, the men celebrating at them could not even stand up straight. How vast is the mercy of Almighty God.")
sh(51, "No checkpoint even tried to stop them. As they drove along those roads full of potholes, a sense of danger never left them.",
   [("engine_rev", "ދުވަމުންދިޔައިރު", -20)])
sh(52, "Though lights could be seen in some houses, there was no sign of human movement. However hard they tried, nobody could sleep.")
sh(53, "Feeling all kinds of fear, Sahar sat repeating her dhikr. As they travelled on and entered the 'Ramadha' area, the call to the Fajr prayer began to be heard.")
sh(54, "After pulling the truck over to one side of the road, everyone performed the obligatory prayer while staying inside the truck.")
sh(55, "Because of the hour and the danger, everyone was afraid to get down from the truck to pray. They had all left home with wudu, keeping this in mind.")
sh(56, "After Fajr they quickly set off again, hoping to cross the Jordanian border area before sunrise. As they travelled,",
   [("truck_start", "ދަތުރުފެށީ", -18)])
sh(57, "everyone was amazed at Hashim's skill. Even on such difficult roads, Hashim kept the truck balanced.")
sh(58, "Hashim had experience of driving these potholed, rocky, rough roads. Driving fast, they reached the Jordanian border at six o'clock.",
   [("engine_rev", "ދުވެއްޔެއްގައި", -18)])
sh(59, "Although there wasn't a big queue, they had to wait a while. \"In the daytime the fighters would be here. Without trouble from them,")
sh(60, "crossing this area would be hard,\" Hashim said, letting out a deep breath. After stopping the truck, Hashim got out.",
   [("sigh", "ނޭވާއެއް", -20), ("car_door", "ފޭބިއެވެ", -18)])
sh(61, "He called his son Abdullah and completed everything that had to be done at immigration. After that,")
sh(62, "he came back to the truck about half an hour later, carrying the papers immigration had given him. \"So, is everything settled?\"",
   [("footsteps_sand", "އާދެވުނީ", -22), ("paper_shuffle", "ލިޔުންތައް", -20)])
sh(63, "Hamza asked anxiously. \"Hamza, how worried you look. We've been given permission. Everyone, rejoice.")
sh(64, "Give praise and thanks to Almighty Allah.\" As soon as Hashim said that, tears of joy fell from everyone's eyes.",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(65, "As he drove on, Hashim began to explain what they had to do next. \"Abdullah says Jordan is giving citizenship to refugees coming from Palestine.",
   [("engine_rev", "ދުއްވާލަމުން", -20)])
sh(66, "Our land, our houses and all our belongings are being looted by those oppressors. Burned to ashes.")
sh(67, "Surely it is far better to live under the shelter of a Muslim nation than under the hand of those oppressors.")
sh(68, "So I think we should do that quickly. Otherwise they may try to pressure this country into handing over all the refugees.")
sh(69, "If we fall into their hands, they will put an end to all our days.")
sh(70, "That is not a fate anyone could accept,\" Hashim said, displeased. Everyone agreed with what Hashim said.")
sh(71, "And deep in their hearts they accepted that, as things stood now, there was no other way.")
SHOTS = S

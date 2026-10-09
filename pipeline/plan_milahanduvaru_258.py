"""Beat/shot plan for Milahanduvaru episode 258 (used by plan_beats.py)."""

LOC = {
    "rain_lane": "a narrow sandy lane between old whitewashed coral-stone walls on a small Maldivian island at night, heavy rain pouring down, puddles shining on the sand, coconut palm fronds bending overhead, one dim distant lamp on a wall",
    "funeral": "the island's wide sandy main lane under tall coconut palms leading towards a small island cemetery with plain white grave markers, low coral-stone walls on both sides",
    "yard_dusk": "the sandy front yard of Shamaan's family home: a single-storey whitewashed coral-stone house with a corrugated tin roof and a plain wooden front door, a big old shady tree, two traditional joali rope seats facing each other under the tree, a low coral-stone boundary wall with an open wooden gate onto a sandy lane",
    "yard_sunset": "the sandy front yard of Shamaan's family home: a single-storey whitewashed coral-stone house with a corrugated tin roof and a plain wooden front door, a big old shady tree, two traditional joali rope seats side by side under the tree, a low coral-stone boundary wall with an open wooden gate",
    "lane_dusk": "a narrow sandy island lane between low coral-stone walls and coconut palms, a simple white mosque with a small minaret far away at the end of the lane",
    "hassan_gate": "the open wooden gate of a small old coral-stone house on a sandy island lane where a visiting elder lodges, a frangipani tree by the wall, the white mosque minaret visible over the roofs",
    "road_setup": "the island's broad sandy main road between coral-stone walls and coconut palms, long plain white cloths laid along the ground and hung along the walls, a big plain wooden table set in the middle of the road with simple plastic chairs in a circle around it",
    "road_night": "the island's broad sandy main road at night between coral-stone walls and coconut palms, long plain white cloths along the ground, a big plain wooden table in the middle of the road with simple plastic chairs in a circle around it, small clay oil lamps on the sand and thin incense smoke",
    "carry_lane": "a dark sandy island lane at night leading to the open gate of Shamaan's family house, coral-stone walls and palms",
    "bedroom": "Shamaan's simple bedroom in an old Maldivian coral-stone house, whitewashed walls, a wooden single bed with a plain sheet, a wooden window with thin curtains, a wooden door",
}
MOOD = {
    "rain_lane": "late night, heavy rain, cold blue-black darkness with silver rain streaks, faint amber glow of a distant lamp, eerie and frightening",
    "funeral": "the next morning, grey overcast daylight, soft muted colours, deep collective grief and fear",
    "yard_dusk": "early evening just after sunset, soft orange-violet afterglow in the sky, warm amber light from the house doorway, uneasy calm turning tense",
    "yard_sunset": "another evening close to sunset, long low golden-orange light through the palms fading into blue dusk, troubled and anxious",
    "lane_dusk": "dusk, deep blue twilight with the last orange glow on the horizon, long shadows, urgent and emotional",
    "hassan_gate": "dusk around maghrib time, deep blue twilight, a warm lamp glowing in the doorway, tense and charged",
    "road_setup": "Friday evening close to sunset, fading orange light, dim and still, solemn and uneasy",
    "road_night": "night after maghrib, dim light, warm flickering amber of small oil lamps and fires against deep indigo darkness, incense haze, tense and fearful",
    "carry_lane": "night, deep indigo darkness, a little warm lamplight from the house doorway, exhausted and sorrowful",
    "bedroom": "late night, cool silver-blue moonlight through the window and the faint amber of a small lamp, quiet, mysterious and sorrowful",
}

BEATS = [
    # ---- cold open: Sattar and the girl in the rain
    dict(to=3, reason="episode opening, scene: Sattar chases a girl running through the night rain", chars=["sattar"], loc="rain_lane",
         visual="Sattar seen from behind and slightly to the side, soaked, running along the rain-flooded lane; far ahead at the end of the lane a small slim female figure in a long dark dress and dark hijab running away into the curtain of rain, only a blurred distant silhouette",
         camera="medium wide from behind Sattar, the lane receding into the rain in the upper half, wet sand and puddles as a calm lower third", amb="rain_night"),
    dict(to=7, reason="action change: walking home soaked, he finds the girl standing motionless against a wall", chars=["sattar"], loc="rain_lane",
         visual="Sattar, drenched, approaching slowly and cautiously with a puzzled frown; a few steps ahead of him a slim girl in a long dark dress and a dark hijab stands perfectly still leaning against the coral-stone wall, seen in deep shadow from the side, her head bowed so her face is not visible, rain running off her",
         camera="medium wide, eye level, Sattar's face in the upper third", amb="rain_night", sens="other",
         safe="the jinn girl is only a still figure in deep shadow, face not visible (bible: red-eyed jinn never in close-up)"),
    dict(to=11, reason="emotional turning point: the jinn reveals herself and his strength drains away", chars=["sattar"], loc="rain_lane",
         visual="Sattar sinking down onto one knee on the wet sand with his head bowed and his shoulders slumped, exhausted and terrified, rain pouring over him; in the left foreground a plain dark near-black silhouette of a slim girl in an ordinary long black dress and black hijab seen strictly from behind in deep shadow, facing him, her face never visible, perfectly still; only the faintest dim reddish tint in the rain mist far behind them, no glowing lines, no aura",
         camera="medium shot over the silhouette's shoulder, Sattar's frightened face in the upper half", amb="rain_night", sens="violence",
         safe="no red eyes in close-up and no grip shown: the girl only as a silhouette from behind with a faint red haze; Sattar's fear shown by him sinking to one knee"),
    dict(to=15, reason="action change: Sattar falls and the figure vanishes into the rain", loc="rain_lane",
         visual="ground-level view along the empty rain-flooded lane, raindrops splashing in the puddles close to the camera, and far away at the end of the lane a faint translucent silhouette of a girl in a long dress and hijab fading into the rain mist; no other person",
         camera="low ground-level wide shot, the fading silhouette in the upper half", amb="rain_night", sens="violence",
         safe="Sattar's collapse is not shown: only the empty rainy lane and the figure fading away"),
    # ---- the funeral
    dict(to=18, reason="scene and time change: Sattar's funeral the next day, Hassanfulhu unshaken", chars=["hassanfulhu"], loc="funeral",
         visual="Hassanfulhu standing apart in the foreground under a palm, upright and stern, watching; in the background many island men in white carrying a covered bier on their shoulders down the sandy lane towards the cemetery, villagers following with bowed heads, some women in hijab grieving at a gateway",
         camera="medium wide, Hassanfulhu in the upper-left two-thirds, the procession small in the background", amb="village_day",
         transition="black", sens="death", safe="funeral shown only as a covered bier carried at a distance; no body"),
    # ---- the yard: Hassanfulhu's visit
    dict(to=21, reason="scene and time change: Shamaan, Zumra and Sakeena on the joali in the yard", chars=["shamaan", "zumra", "sakeena"], loc="yard_dusk",
         visual="Shamaan and Zumra freshly dressed sitting side by side on one joali under the big tree, a married couple with a little space between them; Sakeena sitting on the facing joali; all three talking in low voices with worried, uneasy faces",
         camera="medium wide, eye level, faces in the upper half, the sandy yard as a calm lower third", amb="garden_day", transition="black"),
    dict(to=25, reason="character enters: Hassanfulhu comes into the yard with a young man and is introduced", chars=["hassanfulhu", "shamaan", "sakeena", "zumra"], loc="yard_dusk",
         visual="Hassanfulhu stepping in through the open gate with one hand raised in greeting, a young island man in a plain white shirt beside him; Shamaan standing up from the joali respectfully; Sakeena gesturing politely towards the empty joali; Zumra still seated on the joali, looking away with a tense face",
         camera="wide shot, eye level, the gate and figures in the upper two-thirds", amb="garden_day"),
    dict(to=29, reason="action change: Zumra storms into the house while Hassanfulhu stares after her", chars=["hassanfulhu", "zumra"], loc="yard_dusk",
         visual="Zumra walking quickly and stiffly towards the open wooden front door of the house, seen from behind and in partial profile, her face set in anger; in the foreground Hassanfulhu standing still, his sharp piercing gaze fixed on her, his face grave and suspicious",
         camera="over-the-shoulder medium shot from behind Hassanfulhu, Zumra and the doorway in the upper half", amb="garden_day"),
    dict(to=34, reason="emotional turning point: open confrontation — Shamaan and Sakeena order Hassanfulhu out", chars=["shamaan", "sakeena", "hassanfulhu"], loc="yard_dusk",
         visual="Shamaan standing tall with an angry face, one arm stretched out pointing towards the gate; Sakeena standing beside him, furious and indignant; Hassanfulhu facing them at a clear distance across the sand, calm, firm and unmoved",
         camera="medium wide three-shot, eye level, faces in the upper half", amb="garden_day", hum=True),
    dict(to=37, reason="action change: Hassanfulhu leaves shaking his head; the family's worries", chars=["sakeena", "hassanfulhu"], loc="yard_dusk",
         visual="Hassanfulhu walking out through the gate onto the dusky lane, seen from behind, shaking his head slowly; in the foreground Sakeena standing in the yard with her arms folded, angry yet worried, watching him go",
         camera="medium wide, Sakeena in the foreground right, the gate in the upper middle", amb="garden_day"),
    # ---- another evening: Zumra comes back hurt
    dict(to=40, reason="time change: near sunset, Zumra comes into the yard hurt and in tears", chars=["zumra", "shamaan", "sakeena"], loc="yard_sunset",
         visual="Zumra standing in the yard holding her forearm wrapped in a plain white cloth, her face pained and tearful; Shamaan sitting up on the joali, alarmed and angry; Sakeena sitting on the next joali looking at Zumra with concern",
         camera="medium wide, eye level, faces in the upper half", amb="garden_day", transition="black", sens="violence",
         safe="Zumra's 'injuries' shown only as a forearm wrapped in plain cloth and a pained face; no wounds or blood"),
    dict(to=42, reason="action change: Shamaan rushes off to confront Hassanfulhu, his mother hurrying after him", chars=["shamaan", "sakeena", "zumra"], loc="lane_dusk",
         visual="Shamaan striding fast down the sandy lane with clenched fists and an angry determined face; Sakeena hurrying behind him with one arm outstretched, calling out anxiously; far behind at the corner of a wall Zumra standing small, watching",
         camera="wide shot down the lane, eye level, the figures in the upper two-thirds", amb="village_night"),
    dict(to=45, reason="scene change: at Hassanfulhu's lodging house, face-to-face standoff", chars=["shamaan", "hassanfulhu"], loc="hassan_gate",
         visual="Shamaan and Hassanfulhu standing face to face at arm's length in front of the gate, Shamaan leaning forward with a furious face and wild eyes, Hassanfulhu leaning back with one open palm raised to keep distance, calm but stern, on his way to the mosque",
         camera="medium two-shot in profile, eye level", amb="village_night", sens="violence",
         safe="the grab at the throat and the push are not shown: a tense standoff at arm's length"),
    dict(to=48, reason="character focus change: Sakeena tries to hold Shamaan back while Hassanfulhu warns them", chars=["sakeena", "shamaan", "hassanfulhu"], loc="hassan_gate",
         visual="Sakeena holding her son Shamaan's arm with both hands and pulling him back, her face pleading and upset; Shamaan straining forward, shouting; Hassanfulhu a few steps away with both open palms raised, earnestly warning them",
         camera="medium wide, eye level, faces in the upper half", amb="village_night", hum=True),
    dict(to=50, reason="character enters: Zumra on the road in tears, she runs to Shamaan", chars=["zumra", "shamaan", "sakeena"], loc="lane_dusk",
         visual="Zumra standing upright beside her husband Shamaan in the dusky lane, both facing the viewer side by side, her head held upright and not leaning on him, only her one hand lightly resting on his forearm; both are weeping: Zumra with tears running down her cheeks, brows drawn together in pain and sorrow, no smile at all; Shamaan with wet eyes and a grief-stricken face looking down at her; Sakeena standing a few steps behind them, troubled",
         camera="medium shot, eye level, faces in the upper half", amb="village_night", sens="intimacy",
         safe="the hug is shown as husband and wife standing close side by side with her hand on his arm (bible)", hum=True),
    dict(to=55, reason="character change: Hassanfulhu approaches, Zumra flees and vanishes, the argument", chars=["hassanfulhu", "shamaan", "sakeena"], loc="lane_dusk",
         visual="Hassanfulhu walking towards the camera down the darkening lane, puzzled and stern; Shamaan glaring at him; Sakeena holding Shamaan's hand and turning him away; far in the background a faint silver-blue translucent silhouette of a girl in a long dress fading into the twilight mist",
         camera="wide shot, eye level, the figures in the upper two-thirds", amb="village_night"),
    dict(to=57, reason="action change: the scuffle, separated by island youths", chars=["shamaan", "hassanfulhu"], loc="lane_dusk",
         visual="a group of young island men stepping in between Shamaan and Hassanfulhu with outstretched arms, holding the two apart at a distance; Shamaan's face furious, Hassanfulhu's face stern; a white knitted skullcap lying on the sand in the foreground",
         camera="medium wide, eye level, faces in the upper half, the cap on the sand in the lower third", amb="village_night",
         sens="violence", safe="the blow is not shown: men stepping in between and a fallen cap on the sand"),
    # ---- Friday: the recitation on the road
    dict(to=59, reason="scene and time change: Friday evening, the main road laid with white cloth and a big table", loc="road_setup",
         visual="the empty main road laid with long white cloths, a big wooden table in the middle with plastic chairs in a circle around it, a few strong young island men standing quietly at the edges, no one else",
         camera="wide establishing shot, slightly high angle, the table in the upper half", amb="village_night", transition="black"),
    dict(to=62, reason="characters enter: Hassanfulhu and his group sit down after maghrib and begin the recitation", chars=["hassanfulhu"], loc="road_night",
         visual="Hassanfulhu sitting at the head of the big table, his eyes closed and both palms open before him in recitation; young men in plain shirts seated on the chairs around the table with closed books, waiting attentively; small oil lamps on the sand",
         camera="wide shot, eye level, the table group in the upper two-thirds", amb="night_exterior"),
    dict(to=65, reason="framing change: incense and encouragement; a young man voices doubt", chars=["hassanfulhu"], loc="road_night",
         visual="closer view of Hassanfulhu raising one hand reassuringly while incense smoke curls up from a small clay burner on the table; beside him a young man in a plain shirt looks at him with doubtful, worried eyes",
         camera="medium close shot, eye level", amb="night_exterior"),
    dict(to=68, reason="character enters: Shamaan charges in shouting, the men cannot stop him", chars=["shamaan", "hassanfulhu"], loc="road_night",
         visual="Shamaan running in along the white cloth with a wild furious face, several young men stepping in front of him with outstretched arms but failing to stop him; in the background Hassanfulhu sitting calm and ready at the table",
         camera="medium wide, eye level, Shamaan's face in the upper half", amb="night_exterior"),
    dict(to=70, reason="action change: water thrown in his face, Shamaan falls powerless", chars=["shamaan", "hassanfulhu"], loc="road_night",
         visual="Shamaan lying on his back on the white cloth fully clothed, eyes closed, completely still and breathing faintly, droplets of water on his face; Hassanfulhu standing over him holding an empty brass water bowl, calm and solemn",
         camera="medium shot, slightly high angle, faces in the upper half", amb="night_exterior", sens="violence",
         safe="no impact shown: Shamaan unconscious and unhurt on the cloth, water droplets on his face"),
    dict(to=73, reason="action change: Shamaan laid on the big table, the men recite around him in fear", chars=["shamaan", "hassanfulhu"], loc="road_night",
         visual="Shamaan lying fully clothed and still on the big wooden table, eyes closed; Hassanfulhu seated beside the table leading the recitation with open palms; only young island men in plain shirts (no women at all) sitting around in a circle reciting intently from closed books, their faces tense and frightened; incense haze and oil lamps",
         camera="wide shot, slightly high angle, the table in the upper half", amb="night_exterior", hum=True),
    dict(to=75, reason="character enters: Sakeena bursts in and rushes towards Hassanfulhu", chars=["sakeena", "hassanfulhu"], loc="road_night",
         visual="Sakeena rushing in from the dark edge of the road with a frantic tearful face, her empty hand raised, crying out; Hassanfulhu turning calmly towards her and signalling the young men with a raised palm",
         camera="medium wide, eye level, faces in the upper half", amb="night_exterior"),
    dict(to=78, reason="action change: the young men hold Sakeena back; Hassanfulhu keeps reciting", chars=["sakeena", "hassanfulhu"], loc="road_night",
         visual="two young men holding Sakeena back gently with outstretched arms, her empty hands reaching forward, her face crying and desperate; behind them Hassanfulhu sitting at the table reciting with open palms, his face firm and unmoved",
         camera="medium shot, eye level, Sakeena's face in the upper half", amb="night_exterior", sens="violence",
         safe="the knife taken from her hand is never shown: Sakeena held back by men's outstretched arms with empty hands (bible)", hum=True),
    dict(to=83, reason="shocking turn: flames rise in a ring around the table", chars=["hassanfulhu", "shamaan"], loc="road_night",
         visual="low flames burning in a circle on the sand at a distance around the big table, Shamaan lying unharmed and still on the table in the middle of the ring; Hassanfulhu standing with one arm raised commanding the startled young men to stay back; the men frozen in fear, faces lit orange",
         camera="wide shot, slightly high angle, the ring of fire and table in the upper two-thirds", amb="night_exterior", sens="other",
         safe="the 'ring of fire' = flames in a circle on the sand at a distance around the table, Shamaan unharmed (bible)", hum=True),
    dict(to=86, reason="character focus change: Sakeena held by men, Hassanfulhu alone by the table until the fire dies", chars=["sakeena", "hassanfulhu"], loc="road_night",
         visual="Sakeena crying out desperately, held back by several strong young men with outstretched arms, her empty hands reaching forward, the orange glow of the fire ring on her tear-streaked face; in the background Hassanfulhu sitting alone beside the table inside the dying ring of flames",
         camera="medium wide, eye level, Sakeena's face in the upper half", amb="night_exterior", sens="violence",
         safe="no weapon, no harm: Sakeena only held back by outstretched arms"),
    dict(to=88, reason="action change: the recitation ends, Shamaan is carried home", chars=["shamaan", "sakeena"], loc="carry_lane",
         visual="young island men carrying the exhausted Shamaan home, his arms across two men's shoulders, his head drooping and eyes half closed; Sakeena following close behind, weeping and calling out",
         camera="medium wide, eye level, faces in the upper half", amb="village_night"),
    dict(to=90, reason="scene change: in his bedroom, his mother comforts him and leaves", chars=["sakeena", "shamaan"], loc="bedroom",
         visual="Shamaan lying fully clothed on the bed under a sheet, exhausted, eyes half open; Sakeena sitting on the edge of the bed beside him, one hand gently on his shoulder, comforting him with a tired sad face",
         camera="medium shot, eye level, faces in the upper half", amb="room_night"),
    dict(to=94, reason="character enters: late at night Zumra is in the room, hurt and in tears", chars=["zumra", "shamaan"], loc="bedroom",
         visual="Zumra standing in the moonlight by the window, holding her forearm wrapped in a plain cloth, her pained face streaked with tears and a faint silvery sparkle in her eyes; Shamaan standing near her, bewildered and worried, looking at her",
         camera="medium two-shot, eye level, faces in the upper half", amb="room_night", sens="violence",
         safe="her injuries shown only as a forearm wrapped in plain cloth and a pained face; no wounds or blood", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Suddenly Sattar saw a girl running along the road. At such an unsafe hour,",
   [("footsteps_sand", "ދުވެލާފައި", -22)])
sh(2, "a girl alone outside in this heavy rain — to see who she was, Sattar ran after her.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(3, "But it was in vain. The girl ran on and vanished from sight. Sattar thought she had gone into some house because of the rain.")
sh(4, "Soaked through, Sattar did not want to wait any longer. He began walking slowly towards home.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(5, "Suddenly the same girl caught his eye. Without any movement, she was standing leaning against a wall.")
sh(6, "Though she was soaked with rain, she did not seem to feel the cold at all. Sattar slowly went closer to her.")
sh(7, "\"What are you doing here?\" Sattar asked. \"Come, let's go home. You shouldn't be here alone.\" The girl gave no answer.")
sh(8, "Sattar said it a second time. Then the girl looked at Sattar's face. Because of the terror he saw in those eyes, Sattar tried to run.",
   [("gasp", "ބިރުވެރިކަމެއްގެ", -18)])
sh(9, "Those were not human eyes. There was a fire-coloured redness in them. But the girl came swiftly and seized Sattar by the arm.",
   [("heartbeat", "ހިފެހެއްޓިއެވެ", -18)], hum=True)
sh(10, "However strong Sattar was, before that girl he became helpless. The cold of that hand spread through Sattar's whole body.",
   [("wind_gust", "ފިނިކަން", -20)])
sh(11, "The strength left his body and he was forced to bow his head. \"Listen, I am a jinni. What is this work you are doing?\" the girl said in a frightening voice.",
   [("breath_heavy", "އިސްޖަހާލަން", -20)], hum=True)
sh(12, "It was the very jinni that Sattar and the others had been trying to drive from the island with their recitations. \"Let me go...")
sh(13, "I will never take part in such a thing again\" was all Sattar could say. His voice came out faintly.",
   [("breath", "ކިރިޔާއެވެ", -22)])
sh(14, "Slowly his breathing grew laboured, his strength gave way and he fell to the ground. As Sattar fell,",
   [("soft_thud", "ވެއްޓިއްޖެއެވެ", -16)], hum=True)
sh(15, "he dimly saw that frightening figure disappear into the rain.",
   [("thunder", "ގެއްލިގެން", -18)])
sh(16, "As some people lost their trust in Hassanfulhu, others believed that because of Hassanfulhu's work those sorcerous powers had grown stronger.")
sh(17, "But Hassanfulhu did not lose heart. This was nothing new to him. Many people of the island attended Sattar's funeral.")
sh(18, "As tears flowed from everyone's eyes, every heart held the same question: \"Who will be next?\"",
   [("sob_breath", "ކަރުނަ", -24)], hum=True)
sh(19, "That is now the big question in everyone's heart. It was a lovely evening hour. Bathed and nicely dressed, Shamaan and Zumra were sitting on the joali in the yard.")
sh(20, "Shamaan's mother was sitting on the joali in front of them. Unease showed on their faces.")
sh(21, "They were talking about the frightening things that had lately been harming people on the island. The whole island lived in fear.")
sh(22, "As they talked, they saw Hassanfulhu call out a salaam and come into the yard. Hassanfulhu was an elderly",
   [("footsteps_sand", "ވަދެގެން", -22)])
sh(23, "man with seriousness written on his face. Out of respect for Hassanfulhu, Shamaan stood up. \"This is Hassanfulhu.",
   [("cloth_rustle", "ތެދުވެލިއެވެ", -24)])
sh(24, "He has come to do fanditha work on this island,\" the young man beside Hassanfulhu introduced him.")
sh(25, "\"Come, please sit,\" Shamaan's mother said, pointing to the joali. \"This is my son, and that is his wife sitting there,\" she introduced them to Hassanfulhu.")
sh(26, "At that very moment Zumra suddenly stood up and started walking into the house. By her movements she seemed extremely angry about something.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(27, "Hassanfulhu's sharp gaze stayed fixed on Zumra. \"That's an unusual girl, isn't she,\" Hassanfulhu said, nodding at Zumra with a deep breath.",
   [("breath", "ނޭވާއެއް", -22)])
sh(28, "\"Yes, she is a very good and very gentle girl. And she loves Shamaan dearly,\" Shamaan's mother answered him.")
sh(29, "\"That's not what I mean. Is she even a human being? I have my doubts.\" With that sentence a silence fell over the whole place.",
   hum=True)
sh(30, "\"Hey, there is no need to come to this house and talk such strange things. You've got some nerve!\" Shamaan's patience ran out and he grew angry.")
sh(31, "\"Did you come to this house to sow trouble?\" Shamaan's mother was furious too. Hearing such things about her own child's wife, she could not stay patient.")
sh(32, "\"I think she is a jinni. She may have a hand in what is happening on this island,\" Hassanfulhu said very firmly.")
sh(33, "\"Hey, even as an old man you're out to chase young girls!\" Shamaan shouted. \"Get out of this house! Never come into this house again.")
sh(34, "And he's not even from this island — coming here to talk strange things,\" Shamaan's mother said, ordering Hassanfulhu out of the house.")
sh(35, "Without another word, shaking his head, Hassanfulhu left the house, displeased. Shamaan's mother was still angry.",
   [("footsteps_sand", "ނިކުމެގެން", -22)])
sh(36, "It was because of how the islanders were talking about Shamaan. Shamaan's first marriage too had ended so painfully.")
sh(37, "They did not want it to go that way again this time. And Shamaan certainly did not want to be parted from Zumra.",
   [("sigh", "ނޭދެއެވެ", -24)])
sh(38, "Near sunset Shamaan was lying on the joali in the yard. His mother was lying on the joali next to it.")
sh(39, "Zumra too came into the yard. \"Are the islanders trying to destroy me? Look what they have done to me,\" Zumra complained.",
   [("footsteps_sand", "ވަދެގެން", -22)])
sh(40, "\"Who did this?\" Shamaan flared up. \"That Hassanfulhu. It hurts so much,\" Zumra wept. \"I'm going straight to this Hassanfulhu.",
   [("sob_breath", "ރޮވުނެވެ", -22)], hum=True)
sh(41, "I'll do to him what he did to Zumra.\" Shamaan ran off. His mother ran after him, afraid that Shamaan would hurt Hassanfulhu.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -18)])
sh(42, "Zumra stood far away, watching. Shamaan went straight on and stopped at the house where Hassanfulhu was staying. It was just when Hassanfulhu was coming out to go to the mosque.")
sh(43, "Shamaan went and first grabbed Hassanfulhu by the arm. \"How do you think you can carry on, not knowing to stay away from my wife?\" Shamaan pressed at Hassanfulhu's throat.",
   [("cloth_rustle", "ހިފީ", -20)], hum=True)
sh(44, "\"Hey, this man should get off this island,\" Shamaan's mother began shouting at Hassanfulhu too. \"Listen, what I am doing is for your own safety too,\" Hassanfulhu said, pushing Shamaan away.",
   [("soft_thud", "ކޮއްޕާ", -20)])
sh(45, "\"Oh yes, very safe. Just look at what you have done to my wife,\" Shamaan said.")
sh(46, "All the while his mother kept trying to hold Shamaan back. \"Believe me, she really is a jinni.")
sh(47, "She could do you any kind of harm,\" Hassanfulhu tried to make them understand. \"Look, your wife and your children are jinn.",)
sh(48, "My wife is a human being. A wonderfully good girl.\" As Shamaan said this, Hassanfulhu pushed him off. His mother tried to hold him, but in vain.",
   [("soft_thud", "ކޮއްޕާލިއެވެ", -18)])
sh(49, "His mother set off home, taking Shamaan with her. As they came out onto the road, Shamaan saw Zumra standing in the road.")
sh(50, "Tears were still falling from Zumra's eyes. On seeing Shamaan, Zumra ran to him and clung to him. At that, Shamaan too broke into tears.",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -22)], hum=True)
sh(51, "Suddenly they saw Hassanfulhu coming towards them. The moment she saw Hassanfulhu, Zumra ran away.",
   [("footsteps_sand", "ދުއްވައިގެންފިއެވެ", -22)])
sh(52, "As Shamaan stood watching, Zumra ran off and vanished. \"Are you two still not going home?\" Hassanfulhu began. \"Two of us?")
sh(53, "Look, you've gone blind now, haven't you. And still you chase after young girls,\" Shamaan answered. \"Let's go, my son.")
sh(54, "He's a very wicked man,\" his mother said, taking Shamaan by the hand and walking off. \"Wait! I only saw the two of you.")
sh(55, "I saw no one else,\" Hassanfulhu said. \"Didn't you see my wife? She ran away in fear when she saw you,\" Shamaan retorted.")
sh(56, "Hassanfulhu said, \"That is exactly why I said she is a jinni.\" At these words the enraged Shamaan went and struck Hassanfulhu hard in the mouth.",
   [("soft_thud", "ހަމަލާއެއް", -16)], hum=True)
sh(57, "Hassanfulhu did not stand still either. The scuffle between the two was stopped by the island youths who gathered there at that moment.",
   [("crowd_gasp", "ޒުވާނުންތަކެކެވެ", -20)])
sh(58, "On Friday, close to sunset, the island's main road was covered with white cloth.",
   [("cloth_rustle", "ފޮތިން", -24)])
sh(59, "A big table had been set in the middle of the road with chairs placed around it. No one could be seen except the young men known as the island's strongest.")
sh(60, "The place was dimly lit. Hassanfulhu and his group came from the maghrib prayer and sat down by the table.",
   [("footsteps_sand", "ފައިބައިގެން", -24)])
sh(61, "The young men of the group sat on the chairs set around it. Everyone was waiting for Hassanfulhu's word.")
sh(62, "They did not have to wait long. Hassanfulhu gave the word. Hassanfulhu began the recitation.")
sh(63, "He burned incense, showing off his craft. \"Boys, don't lose heart. Anything may happen.",
   [("fire_crackle", "ދުންއަޅައި", -22)])
sh(64, "But as long as I am here, no harm will ever come to you,\" Hassanfulhu kept encouraging them. \"You said that before too.")
sh(65, "But last night we still lost someone,\" one of the young men said. It seemed that they too no longer trusted Hassanfulhu.")
sh(66, "\"That happened because he did not listen to me,\" Hassanfulhu said. Everyone was startled when Shamaan came running in and started shouting.",
   [("crowd_gasp", "ސިހިގެން", -20)])
sh(67, "Without hesitating, a few of them went and held Shamaan back. But it was in vain. Tonight Shamaan had an unnatural strength.",
   [("cloth_rustle", "ހިފެހެއްޓިއެވެ", -20)])
sh(68, "Not one of them could stop Shamaan. Shamaan charged towards Hassanfulhu. Hassanfulhu sat ready for anything that might happen.",
   [("footsteps_sand", "ދުއްވައިގަތީ", -18)])
sh(69, "Just as Shamaan came close to Hassanfulhu, the water in the bowl in Hassanfulhu's hand struck Shamaan's face. Shamaan instantly fell to the ground.",
   [("splash", "ފެންތަށި", -16), ("soft_thud", "ވެއްޓިއްޖެއެވެ", -16)], hum=True)
sh(70, "The man who had been given such great strength now had no strength left in his body. He was only breathing.",
   [("breath", "ނޭވާލާ", -22)])
sh(71, "The silence over the island was broken by the loud recitation of Hassanfulhu's group. With Shamaan laid on the big table in the middle of the yard,")
sh(72, "everyone around him recited with the utmost concentration. The changes coming over Shamaan's body,")
sh(73, "and the sight of his eyes rolling upward, left the people near him frozen with fear.",
   [("heartbeat", "ބިރުން", -20)], hum=True)
sh(74, "Suddenly the door burst open and in came Shamaan's mother. Waving her hand, she ran straight towards Hassanfulhu.",
   [("door_open", "ހުޅުވާލާފައި", -18), ("footsteps_sand", "ދުވެފައި", -20)])
sh(75, "\"What are you doing to my son?\" she kept screaming. Very calmly, Hassanfulhu signalled the men near him to protect them.")
sh(76, "But Shamaan's mother could not reach Hassanfulhu. The alert young men beside Hassanfulhu stopped her at once,")
sh(77, "and took the knife from her hand. \"Hey! Let my son go now! Why are you hurting him?\" Shamaan's mother began to scream, weeping.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(78, "Her voice was full of the deepest worry and fear. \"No, I will not stop. This is the only way his life can be saved,\" said Hassanfulhu, without breaking off the recitation,")
sh(79, "answering very firmly. While this quarrel went on, the whole place was struck by a sudden shock. From the four corners of the table where Shamaan lay, fire suddenly blazed up and surrounded the whole table.",
   [("crowd_gasp", "ސިހުމެކެވެ", -18), ("fire_crackle", "ރޯވެ", -16)], hum=True)
sh(80, "Seeing that, the other members of the group rushed in fear to pull Shamaan out of the fire. Shamaan's mother screamed loudly.",
   [("footsteps_sand", "ދުއްވައިގަތީ", -20)])
sh(81, "\"Leave him! No one is to touch his body!\" Hassanfulhu's loud voice rang through the whole yard.")
sh(82, "At his command everyone stopped. \"This is not a fire you see on the outside. This is the fire that burns away the evil powers in his body.")
sh(83, "If you touch him, everything will go wrong.\" At Hassanfulhu's words, everyone held their breath and watched.",
   [("breath", "ނޭވާ", -22)])
sh(84, "Shamaan lay in the middle of that fire, unmoving and still. Shamaan was lying on the table, writhing.",
   [("fire_crackle", "އަލިފާނުގެ", -20)])
sh(85, "Standing beside him, Shamaan's mother was screaming like one gone mad. Five strong men were holding her back.")
sh(86, "Only Hassanfulhu sat by the table where Shamaan lay. No one else had his permission to come near the table. After a while the fire died out.",
   [("wind_gust", "ނިވިއްޖެއެވެ", -22)])
sh(87, "Shamaan got up too. There seemed to be no strength left in his body. He could barely stand.")
sh(88, "When the recitation was over, they all carried Shamaan on their shoulders and brought him into the house. Shamaan's mother still followed behind them, screaming like one gone mad.",
   [("footsteps_sand", "ގެނެސް", -20)])
sh(89, "\"Be strong, my son. Pay no mind to what they do,\" his mother kept encouraging him after they had gone. Zumra had not come home yet either.")
sh(90, "Then, telling him to get some sleep, Shamaan's mother Sakeena closed the bedroom door and went out. Shamaan fell asleep too.",
   [("door_close", "ދޮރުލައްޕާފައި", -18)])
sh(91, "Shamaan woke up feeling that someone was moving about in the room. He slowly opened his eyes and looked. Shamaan had sensed right.",
   [("breath", "ހޭލެވުނީ", -24)])
sh(92, "Zumra was pacing back and forth in the room. Shamaan got up and went to Zumra. Zumra had been hurt in some way.",
   [("footsteps_pavement", "ހިނގާލަ", -24)])
sh(93, "\"What has happened to you?\" Shamaan asked in surprise. \"There's no need to pretend you don't know,\" Zumra said, upset.")
sh(94, "\"I don't know,\" Shamaan answered. \"Look, this is that Hassanfulhu's doing,\" Zumra said, and began to cry.",
   [("sob_breath", "ރޮވެންފެށުނެވެ", -22)], hum=True)
SHOTS = S

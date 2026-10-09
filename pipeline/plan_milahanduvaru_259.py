"""Beat/shot plan for Milahanduvaru episode 259 (used by plan_beats.py)."""

HOME = ("Shamaan's family home on a small Maldivian island: an old single-storey whitewashed coral-stone house with a "
        "corrugated tin roof and wooden shuttered windows")
YARD = (HOME + ", seen from its sandy front yard with a low coral-stone boundary wall, a wooden gate, a big shady tree "
        "with a joali (a traditional Maldivian rope-net seat on a wooden frame) beneath it, coconut palms")
SITTING = ("the simple sitting room of " + HOME + ": whitewashed walls, a woven mat on a tiled floor, a cushioned wooden "
           "sofa, a few wooden chairs, a ceiling fan, a doorway to a small kitchen with steel pots on a shelf")
THUNDI = ("the thundi, the long sandy tip of a small Maldivian island at night: smooth pale sand reaching into a calm "
          "dark lagoon, a big old kaani tree and leaning coconut palms at the edge of the beach vegetation")

LOC = {
    "shamaan_room": ("Shamaan's small bedroom in " + HOME + " at night: whitewashed walls, a wooden wardrobe, a low "
                     "wooden bench under an open shuttered window, a small oil lamp on a shelf"),
    "room_window": ("the open wooden-shuttered window of Shamaan's small bedroom at night, looking out over moonlit "
                    "sandy lanes, tin roofs and coconut palms of the island village"),
    "jetty": ("the small wooden-and-concrete jetty of a Maldivian island village in the morning, a traditional wooden "
              "dhoni moored alongside, turquoise lagoon, palms along the shore"),
    "yard_day": YARD + ", in the late morning",
    "sitting_room": SITTING + ", by day",
    "dining": ("the small dining area beside the kitchen of " + HOME + ": a plain wooden table with steel plates, a pot of "
               "rice, a bowl of fish curry and a stack of roshi flatbread, wooden chairs, whitewashed walls"),
    "yard_afternoon": YARD + ", in the mid-afternoon",
    "yard_dusk": YARD + ", at dusk, a warm lamp lit on the small front veranda",
    "hassan_house": ("the small sandy yard of a modest coral-stone house where the reciter Hassanfulhu stays, a narrow "
                     "veranda with two simple wooden chairs, an oil lamp hanging by the door, a low boundary wall and "
                     "a wooden gate, coconut palms"),
    "yard_night": YARD + ", at night, the joali under the tree lit by a single lamp hanging from a branch",
    "sunset": ("the sky over a small Maldivian island at sunset: golden-orange and rose clouds above the sea horizon, "
               "an empty sandy village lane, coral-stone walls, coconut palms in silhouette"),
    "mosque_path": ("a sandy island path leading from a small white village mosque towards the beach, coconut palms on "
                    "both sides"),
    "thundi_calm": THUNDI,
    "thundi_wind": THUNDI + ", the palms and the kaani tree bending in a rising wind",
    "thundi_storm": THUNDI + ", in a violent squall of blowing sand and heavy rain",
}
MOOD = {
    "shamaan_room": "night, warm amber oil-lamp glow mixed with silver-blue moonlight from the window, intimate, uneasy and mysterious",
    "room_window": "night, silver moonlight and deep indigo shadows, a single warm lamp behind him, brooding and uncertain",
    "jetty": "morning, bright soft tropical daylight, turquoise water, a relieved homecoming shadowed by worry",
    "yard_day": "late morning, bright tropical daylight with soft shade under the tree, tense family argument",
    "sitting_room": "daytime, soft warm daylight through the shuttered windows, joyful and tender",
    "dining": "daytime, warm soft daylight, homely, close and loving family atmosphere",
    "yard_afternoon": "mid-afternoon, dappled warm light under the tree, drowsy and quiet",
    "yard_dusk": "dusk, the last orange glow in the sky turning to deep blue, warm amber veranda lamp, warm greeting turning to alarm",
    "hassan_house": "evening after sunset, deep blue sky, warm amber light from the hanging oil lamp, tense and wary",
    "yard_night": "night, a single warm lamp on the joali against deep indigo shadows, suspicion and tension like an interrogation",
    "sunset": "sunset, rich gold and orange sky fading to violet, an unnatural deep silence, foreboding",
    "mosque_path": "early night just after sunset, deep blue sky, the mosque's warm light behind them, solemn determination",
    "thundi_calm": "night, bright full moonlight silvering the sand and the lagoon, clear starry sky, gentle breeze, calm and spiritual",
    "thundi_wind": "night, moonlight dimming behind fast clouds, wind whipping the fronds, a creeping sense of an unseen presence",
    "thundi_storm": "night, storm, moon hidden behind dark clouds, blowing sand and slanting rain, cold silver-blue light, fear",
}

BEATS = [
    dict(to=3, reason="episode opening: Shamaan and Zumra in his room at night, he holds her hurt arm",
         chars=["shamaan", "zumra"], loc="shamaan_room",
         visual="Shamaan and his wife Zumra sitting side by side on a low wooden bench under the window of his room; Shamaan gently holds her forearm, which is wrapped in a plain white cloth, looking at her with worry and a hesitant half-smile; Zumra smiles back an enigmatic faint smile, a silvery sparkle in her eyes, moonlight on her face",
         camera="medium two-shot, eye level, faces in the upper half, the plain floor as a calm lower third",
         amb="room_night", sens="other",
         safe="Zumra's unseen injuries shown only as a forearm wrapped in a plain clean cloth; married couple, he only holds her arm"),
    dict(to=6, reason="action change: Shamaan alone at the window, brooding over Hassanfulhu and the island's fear",
         chars=["shamaan"], loc="room_window",
         visual="Shamaan standing alone at the open wooden window of his room, one hand on the shutter, troubled and lost in thought, looking out over the moonlit village; far away down the sandy lane a tiny figure of an old man all in white walks past a few islanders who stand in small whispering groups",
         camera="medium shot from slightly behind and beside him, his profile in the upper half, the village beyond",
         amb="room_night"),
    dict(to=9, reason="scene and time change: the next day the father returns to the island from treatment in Malé",
         chars=["shamaan_father", "shamaan"], loc="jetty",
         visual="Shamaan's father, healthy again, stepping off a wooden dhoni onto the island jetty holding a small travel bag; Shamaan steps forward to take the bag from him with a relieved smile; the father's face is healthy but clouded with worry, his brow furrowed",
         camera="medium wide, eye level, both men in the upper two-thirds, the jetty planks and calm water as the lower third",
         amb="jetty_day", transition="black"),
    dict(to=13, reason="scene change: at the house the father demands to meet Hassanfulhu; Sakeena and Shamaan plead",
         chars=["shamaan_father", "sakeena", "shamaan"], loc="yard_day",
         visual="in the sandy front yard the stern father stands with his travel bag at his feet, speaking firmly with a determined frown; Sakeena faces him a step away, hands clasped in worry; Shamaan stands beside them with tears in his eyes, one hand raised palm-open, pleading with his father",
         camera="medium wide three-shot, eye level, faces in the upper half, the sandy yard as a calm lower third",
         amb="island_house_day", sens="other", safe="Shamaan's sobbing shown only as tearful pleading eyes"),
    dict(to=16, reason="scene and character change: inside, Yameen runs to his grandfather and hugs him",
         chars=["shamaan_father", "yameen", "shamaan"], loc="sitting_room",
         visual="the grandfather crouching down in the sitting room, hugging little toddler Yameen, who has run into his arms beaming with joy; a few small toy cars lie scattered on the woven mat; the grandfather's face full of deep love; Shamaan stands smiling in the doorway behind them",
         camera="medium shot, slightly low eye level, faces in the upper half, the woven mat with toy cars as the lower third",
         amb="home_day", sens="other", safe="grandfather and grandson: a warm family hug"),
    dict(to=20, reason="action change: the grandfather sits with the thin child and asks for Zumra; Sakeena works in the kitchen",
         chars=["shamaan_father", "yameen", "sakeena"], loc="sitting_room",
         visual="the grandfather seated on a wooden chair with Yameen on his lap, looking down at the small thin boy with concern, then glancing around the house as if searching for someone; in the background through the kitchen doorway Sakeena arranges steel plates on a shelf, sighing, half-turned towards them",
         camera="medium shot, eye level, the grandfather and child in the foreground upper half, Sakeena small in the background",
         amb="home_day"),
    dict(to=24, reason="action change: the whole family sits down to eat together for the first time in many days",
         chars=["shamaan_father", "yameen", "shamaan", "sakeena"], loc="dining",
         visual="the family eating together at a plain wooden table: the grandfather at the head, little Yameen sitting right beside him gazing up at him expectantly as if waiting for a story; Shamaan across the table smiling; Sakeena serving rice onto a plate; warm closeness",
         camera="medium wide, eye level, faces in the upper half, the table top as the lower third",
         amb="home_day"),
    dict(to=26, reason="time and action change: afternoon, Sakeena takes Yameen outside and lies on the joali so the father can sleep",
         chars=["sakeena", "yameen"], loc="yard_afternoon",
         visual="Sakeena reclining on a joali rope seat under the big shady tree in the yard, fully dressed, with little Yameen nestled against her side, his cheeks still wet from crying and his lip pouting, calming down sleepily; the house door behind them closed",
         camera="medium wide, eye level, the joali and faces in the upper half, the sandy ground as the lower third",
         amb="garden_day"),
    dict(to=29, reason="time and character change: at dusk Zumra comes home and the father greets her",
         chars=["zumra", "shamaan_father"], loc="yard_dusk",
         visual="at dusk Zumra walks in through the wooden yard gate with a graceful soft smile; the father, freshly dressed for the sunset prayer, stands on the small lamp-lit veranda smiling warmly at her as he greets her, a few steps apart",
         camera="medium wide, eye level, both figures in the upper two-thirds, the sandy yard as the lower third",
         amb="island_house_night", transition="black", sens="other",
         safe="his bath before the prayer is not shown; he appears already dressed"),
    dict(to=32, reason="emotional turning point: the father sees the wounds on Zumra's arm",
         chars=["zumra", "shamaan_father", "sakeena"], loc="yard_dusk",
         visual="on the lamp-lit veranda Zumra stands holding her forearm, wrapped in a plain cloth, close to her chest, eyes lowered, speaking softly with a pained look; the father before her leans forward, startled, then his face hardens in anger; Sakeena behind him with a frightened face, one hand raised to stop him",
         camera="medium close three-shot, eye level, faces in the upper half",
         amb="island_house_night", sens="violence",
         safe="the burn wounds are never shown: only a forearm wrapped in a plain clean cloth and pained faces"),
    dict(to=35, reason="scene change: the father and Sakeena wait at Hassanfulhu's house; he arrives and greets them",
         chars=["hassanfulhu", "shamaan_father", "sakeena"], loc="hassan_house",
         visual="Hassanfulhu, tall and all in white, walking in through the wooden gate of the small yard with his right hand on his chest in a salaam greeting; Shamaan's father and Sakeena waiting in the yard, the father returning the greeting with a small polite smile, Sakeena uneasy behind him",
         camera="medium wide, eye level, figures in the upper two-thirds, the sandy yard as the lower third",
         amb="village_night"),
    dict(to=39, reason="action change: they sit down and talk; Hassanfulhu warns that Zumra is a jinn",
         chars=["shamaan_father", "hassanfulhu", "sakeena"], loc="hassan_house",
         visual="Shamaan's father and Hassanfulhu sitting on two wooden chairs on the narrow veranda facing each other at arm's length under the oil lamp; the father speaks patiently with an open hand; Hassanfulhu leans forward earnestly, his steady eyes urgent; Sakeena stands back by the veranda post listening",
         camera="medium two-shot from the side, eye level, faces in the upper half",
         amb="village_night"),
    dict(to=42, reason="action change: the talk turns hostile and the father leaves",
         chars=["hassanfulhu", "shamaan_father", "sakeena"], loc="hassan_house",
         visual="Hassanfulhu standing on the veranda, stern and calm, one open palm raised as he explains; the father has turned away from him towards the gate, looking back over his shoulder with a reproachful, scornful frown; Sakeena hurrying after the father; a clear distance between the men",
         camera="medium wide, eye level, faces in the upper half, the yard sand as the lower third",
         amb="village_night"),
    dict(to=45, reason="scene change: back home the angry father questions Shamaan about Zumra",
         chars=["shamaan_father", "shamaan"], loc="yard_night",
         visual="Shamaan sitting on the joali under the single hanging lamp, hands clasped, looking down uneasily like a man at an interrogation table; his father standing over him with his hands behind his back, studying his son's face with a suspicious stern look",
         camera="medium shot, slightly high angle over the father's shoulder, faces in the upper half",
         amb="island_house_night"),
    dict(to=48, reason="character change: Sakeena comes, sits beside Shamaan and sends him inside",
         chars=["sakeena", "shamaan", "shamaan_father"], loc="yard_night",
         visual="Sakeena sitting beside Shamaan on the joali, tenderly stroking his head as a mother does, protective and annoyed at her husband; Shamaan bewildered and silent; the father standing a few steps away with crossed arms",
         camera="medium shot, eye level, faces in the upper half",
         amb="island_house_night", sens="other", safe="mother and son (mahram): she only strokes his head"),
    dict(to=52, reason="character change: Shamaan has gone inside; the father voices his doubts about Zumra to Sakeena",
         chars=["shamaan_father", "sakeena"], loc="yard_night",
         visual="the father sitting on the joali leaning forward, troubled, gazing towards the dimly lit window of the house; Sakeena standing beside the joali with her arms folded, displeased, scolding him; the lamp swinging softly above them",
         camera="medium two-shot, eye level, faces in the upper half, the sandy ground as the lower third",
         amb="island_house_night"),
    dict(to=53, reason="return to an earlier image: the father says 'look at Zumra's arm'", reuse="beat_010",
         loc="yard_dusk", visual="(reuse of beat_010: Zumra's wrapped arm)", amb="island_house_night",
         transition="dissolve"),
    dict(to=55, reason="time and scene change: the next sunset over the strangely silent island",
         loc="sunset",
         visual="a golden-orange and rose sunset sky over the sea horizon above the island, an empty silent sandy village lane between coral-stone walls, coconut palms in dark silhouette, no people",
         camera="wide establishing shot, the sky in the upper two-thirds, the empty lane as the lower third",
         amb="beach_dusk", transition="black"),
    dict(to=58, reason="character and action change: after the sunset prayer the men head to the thundi for the recitation",
         chars=["hassanfulhu"], loc="mosque_path",
         visual="Hassanfulhu in white leading a group of island men and young men in plain shirts and sarongs along the sandy path away from the small white mosque towards the beach, every face serious and determined, some carrying closed books under their arms",
         camera="medium wide, slightly low angle, faces in the upper half, the sandy path as the lower third",
         amb="village_night"),
    dict(to=62, reason="scene change: under the full moon the recitation begins on the thundi",
         chars=["hassanfulhu"], loc="thundi_calm",
         visual="Hassanfulhu sitting cross-legged on the moonlit sand at the tip of the island, holding a closed book in his hands, eyes calm; young men of the island sitting cross-legged in a circle around him with open palms and closed books, the calm silver lagoon and the big kaani tree behind them, the full moon high; everyone in the circle is a man or young man with short black hair, bare-headed or in a white skullcap, wearing plain shirts and sarongs — no women, no headscarves, no hooded or cloaked figures",
         camera="wide shot from slightly above, the circle and the moon in the upper two-thirds, smooth sand as the lower third",
         amb="beach_night", sens="other", safe="recitation shown with closed books and open palms; no script"),
    dict(to=66, reason="action change: the wind rises, leaves shake and they feel an unseen presence",
         chars=["hassanfulhu"], loc="thundi_wind",
         visual="the circle of reciting men on the sand seen wider, heads bowed in concentration, Hassanfulhu in the center; the palm fronds and kaani leaves whipping in a sudden wind, clouds racing across the moon, the dark line of trees behind them full of deep shadows as if someone unseen were watching, no figure visible; everyone in the circle is a man or young man with short black hair, bare-headed or in a white skullcap, wearing plain shirts and sarongs — no women, no headscarves, no hooded or cloaked figures",
         camera="wide shot, eye level, the trees and sky in the upper half, the sand as the lower third",
         amb="beach_night"),
    dict(to=69, reason="action change: a squall of sand and heavy rain; some men stand up in fear",
         chars=["hassanfulhu"], loc="thundi_storm",
         visual="a squall of blowing sand and slanting heavy rain sweeping across the beach; the young men shielding their eyes with their forearms, some rising to their feet in fear, one calling out to the old reciter; Hassanfulhu still seated in the center, his white clothes whipping in the wind; everyone in the circle is a man or young man with short black hair, bare-headed or in a white skullcap, wearing plain shirts and sarongs — no women, no headscarves, no hooded or cloaked figures",
         camera="medium wide, eye level, faces in the upper half, the rain-pocked sand as the lower third",
         amb="storm_night"),
    dict(to=71, reason="emotional turning point: Hassanfulhu stands firm and urges courage",
         chars=["hassanfulhu"], loc="thundi_storm",
         visual="close view of Hassanfulhu seated firm in the driving rain, his long white beard and white clothes soaked and blowing, eyes steady and certain, one open palm raised as he urges the young men to be brave",
         camera="medium close-up, eye level, his face in the upper half, the wet sand as the lower third",
         amb="storm_night"),
    dict(to=75, reason="action change: some men walk away while a few stay and continue reciting",
         chars=["hassanfulhu"], loc="thundi_storm",
         visual="several young men walking away up the beach into the rain, seen from behind, shoulders hunched; in the foreground a few brave young men remain seated close around Hassanfulhu, reciting with bowed heads in the wind and rain",
         camera="wide shot, eye level, the departing figures in the upper half, the sand as the lower third",
         amb="storm_night"),
    dict(to=77, reason="character change: a figure that looks like Shamaan appears in the distance",
         loc="thundi_storm",
         visual="through the slanting rain, far away at the edge of the palms, a blurred motionless male figure in a light-blue shirt stands watching, his face not visible, only a vague silhouette; in the foreground the seated young men glance towards it in fear while an old man in white raises a warning hand; the seated men in the foreground all have short black hair or white skullcaps and wear plain shirts — no women, no headscarves, no hooded or cloaked figures",
         camera="wide shot over the shoulders of the seated men, the distant figure small in the upper third",
         amb="storm_night", sens="other",
         safe="the jinn apparition shown only as a distant blurred figure, no face, no reference image"),
    dict(to=79, reason="character change: the young reciter Najmee trembles with fear; Hassanfulhu reassures him",
         chars=["hassanfulhu"], loc="thundi_storm",
         visual="a slim young island man of about twenty in a soaked white shirt sitting on the wet sand hugging his knees, trembling, wide frightened eyes; beside him Hassanfulhu turns to him calmly, speaking words of courage; behind them in the distance only empty rain where the figure stood",
         camera="medium two-shot, eye level, faces in the upper half, the wet sand as the lower third",
         amb="storm_night"),
    dict(to=82, reason="character change: a figure that looks like Sakeena comes hurrying through the rain",
         chars=["hassanfulhu"], loc="thundi_storm",
         visual="far away along the rain-swept beach a blurred figure of a woman in a dark maroon dress and beige headscarf hurries towards the circle, her face not visible, empty hands; in the foreground the young men spring to their feet in fear, while Hassanfulhu stays seated, unmoved and calm",
         camera="wide shot, eye level, the distant figure small in the upper third, the men in the middle, the sand as the lower third",
         amb="storm_night", sens="violence",
         safe="the knife is not shown; the apparition is a distant blurred figure with empty hands, no reference image"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"We have just come from being near them. There was no Zumra there,\" Shamaan said, holding Zumra's arm.")
sh(2, "\"Look, if I were a jinni, I could have been there, couldn't I?\" Zumra smiled. \"Oh, how funny, you a jinni,\" Shamaan said a little hesitantly. It was true.")
sh(3, "Strange, unnatural things were being seen in Zumra. Without anyone seeing, Zumra was suffering injuries.")
sh(4, "According to Zumra, these came from Hassanfulhu, who had come to do fanditha. But would Hassanfulhu dare to inflict such great harm on a human in front of the islanders?")
sh(5, "And would the islanders stay silent watching such harm being done? These were the questions arising in Shamaan's mind.", hum=True)
sh(6, "After that night's frightening event, Hassanfulhu's name was a hope of safety for some on the island, but for others it was the beginning of an unknown fear.")
sh(7, "It was the day Shamaan's father came back to the island after his treatment in Malé. Because he was coming, Shamaan and his mother Sakeena were very busy with the housework.",
   [("dhoni_engine", "ރަށަށް", -22)])
sh(8, "Father had had to stay many days in Malé because of his illness, but this time he came back in full health. However,")
sh(9, "because of the distressing events the family had faced on the island, father was deeply uneasy.")
sh(10, "As soon as he reached the house, the first one father looked for was Zumra. But Zumra was not home at that time. \"What I want is to meet this great Hassanfulhu you speak of and talk to him,\" Shamaan's father said in a harsh tone.")
sh(11, "\"No, there is no point going there. He is a very dangerous man. He has stirred up strife and mischief all over the island,\" Sakeena said with worry.")
sh(12, "\"They are working to destroy us,\" Shamaan said, sobbing. \"That won't happen. I will show them who I am too,\" father said with displeasure.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(13, "\"Bappa, I beg you. Don't go to confront them,\" Shamaan pleaded with his father. Shamaan did not want this matter to grow any bigger.")
sh(14, "When Shamaan brought his father into the house, little Yameen was sitting in the sitting room playing with his cars. On seeing his grandfather,",
   [("door_open", "ވަދެގެން", -20)])
sh(15, "joy spread across Yameen's face. He ran at once and clung to his grandfather. Grandfather's face showed an overwhelming love.",
   [("footsteps_pavement", "ދުވެގޮސް", -22)])
sh(16, "Grandfather had always loved Yameen very much. \"Sakeena, don't you even feed this boy?\" Hugging Yameen, grandfather looked at his little body.")
sh(17, "Because Yameen was thinner than before, father asked in a worried tone. \"However hard I try, he doesn't want to eat.")
sh(18, "He's always just looking for something to play with,\" said Sakeena, who was arranging plates in the kitchen, after a deep sigh. \"I still haven't met Zumra.",
   [("cup_clatter", "ތަށިތައް", -20), ("sigh", "ނޭވާއެއް", -22)])
sh(19, "Where is that girl?\" Sitting down on a chair, father looked around the house. Not seeing Zumra anywhere, father again wanted his confusion cleared.")
sh(20, "\"Now stop talking so much and come and eat. That girl comes after sunset. She'll be arriving soon,\" Sakeena said a little sharply as she got the food ready.")
sh(21, "Shamaan took his father by the hand and led him to the dining table. The worry and love father held for everyone in the family")
sh(22, "showed even in that little moment. Yameen sat beside his grandfather,")
sh(23, "as if waiting for a story grandfather would tell. The house showed the closeness of a Maldivian family and how they care for one another.")
sh(24, "After many days, the whole family ate together. After the meal, father went to his room to rest from the tiredness of the journey.")
sh(25, "When Shamaan went out, Sakeena also took Yameen outside. Although Yameen cried, wanting to go to his grandfather for a present,",
   [("sob_breath", "ރޮމުން", -24)])
sh(26, "so that father's sleep would not be disturbed, Sakeena took him and lay down on the joali outside. Father woke up when sunset was near.")
sh(27, "He quickly got up, bathed and got ready to go to the Maghrib prayer. That was the moment Zumra too came into the house.",
   [("door_open", "ވަދެގެން", -20)])
sh(28, "\"My dear, you are so busy,\" father said on seeing Zumra. \"Yes Bappa, I've come after a lot of work.")
sh(29, "I knew you were coming, so I managed to come a little early today,\" Zumra answered. \"My dear, what has happened to your arm? Did someone burn you?\"")
sh(30, "Father was startled to see the wounds on Zumra's arm. \"This... this... is harm done by that Hassanfulhu,\" Zumra said softly.",
   [("gasp", "ސިހުނެވެ", -20)], hum=True)
sh(31, "\"Is that the man who has come to this island? Well, he won't find us letting it go,\" father became very angry. \"Don't go to that house,\" Sakeena said in fear.")
sh(32, "\"Nothing will happen because of you, Sakeena. But I will go to meet Hassanfulhu.\" Father was not at ease.")
sh(33, "When father set off to meet Hassanfulhu, Sakeena followed behind in fear. When they reached that house, there was no one to be seen.",
   [("footsteps_sand", "ހިނގައިގަތުމުން", -22)])
sh(34, "But father did not want to go back without meeting Hassanfulhu. After a short wait, Hassanfulhu came into the house.",
   [("footsteps_sand", "ވަދެގެން", -22)])
sh(35, "On seeing Sakeena and the others, Hassanfulhu greeted them with salaam. Father too returned the salaam with a smile.")
sh(36, "\"I came to see Hassanfulhu about something,\" father said. \"Tell me quickly, what is it?\" Hassanfulhu asked kindly.")
sh(37, "\"I heard that Hassanfulhu hurt Zumra. I came to tell you not to do such things,\" father spoke very patiently.")
sh(38, "\"Please believe what I am telling you. That is not a human, that is a jinn girl.", hum=True)
sh(39, "Hurry and save yourselves from that danger,\" Hassanfulhu tried to make him understand the truth. \"All these problems started after you came to this island.")
sh(40, "I have heard you are a man who chases after girls,\" father said in a reproachful tone. \"Listen to me properly.")
sh(41, "Learn the difference between humans and jinn. That Zumra you speak of will not be seen by anyone in the daytime.")
sh(42, "She does all her doings after sunset,\" Hassanfulhu told him again. \"I'll see how long you can carry on like this,\" father said, and with that he walked out of that house.",
   [("footsteps_sand", "ނިކުމެގެން", -22)])
sh(43, "When he came home, father was very angry. As soon as he entered, the first one he called was Shamaan. \"Shamaan, where is Zumra?\"",
   [("door_open", "ވަދެގެން", -22)])
sh(44, "father asked. \"She's inside the house,\" Shamaan answered briefly. \"Why is Zumra never seen in the house in the daytime?\"")
sh(45, "father asked after looking at Shamaan's face with a suspicious gaze. \"Because her office work is heavy, she says.\" As he said it, Shamaan felt as if he were sitting at the interrogation table of an investigation agency.")
sh(46, "\"Even so, I think some day she should take part in the household things and spend some time here,\" Shamaan's father went on asking one question after another.")
sh(47, "Shamaan sat not knowing what to answer, at a loss for what to say. \"Well done! Has Shamaan become a criminal now?\"", hum=True)
sh(48, "Saying this, Sakeena came quickly and sat down beside Shamaan. \"My son, go inside now,\" Sakeena said, lovingly stroking Shamaan's head.",
   [("cloth_rustle", "އިށީނެވެ", -22)])
sh(49, "At his mother's request Shamaan went inside at once. \"Doubts have started to rise in my heart too,\" Shamaan's father said to Sakeena.",
   [("door_close", "ވަދެގެން", -22)])
sh(50, "\"What are you so suspicious about? Do you remember that I am your wife?\" Sakeena retorted with displeasure. \"No,")
sh(51, "what I am saying is, is Zumra a human? Her ways and her nature are very different from ordinary people,\" Shamaan's father voiced the worry in his heart.", hum=True)
sh(52, "\"People will say all kinds of things. When you talk like that, think about what will go through that boy's mind,\" Sakeena said, uneasy.")
sh(53, "\"Look at Zumra's arm. But no one on this island can be found who would do such harm to her,\" Shamaan's father said, uneasy, and then started walking inside.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(54, "Sakeena too followed after him. It was the time near sunset. While the golden-orange colours on the horizon covered the whole sky,")
sh(55, "an unusual stillness was settling over the island. Just as on other days, Hassanfulhu and his companions were preparing for the kiyevelli recitation.")
sh(56, "This was very important work to save the islanders from the terror they faced. A large number of the island's men took part in it.")
sh(57, "On every face could be seen sincerity and unshakable determination. Tonight was the night the real work of destroying the jinn troubling the island would begin.")
sh(58, "Because of that trouble, everyone on the island, young and old, lived in unease. Coming out from the Maghrib prayer, they all headed to the thundi.",
   [("footsteps_sand", "ޖެހީ", -24)])
sh(59, "By then the lovely moonlight lit up the whole area. Apart from the sound of the sea's waves kissing the shore, no other sound was heard there.",
   [("wave_crash", "ރާޅުތައް", -24)])
sh(60, "In that enchanting setting, with a clear sky and a gentle breeze blowing, Hassanfulhu sat down calmly on the sand of the thundi.")
sh(61, "The young men of the island came and sat down around him. Taking the kiyevelli books that were in Hassanfulhu's hands, the work began.",
   [("page_turn", "ފޮތްތައް", -22)])
sh(62, "With the sound of the recitation flowing from his lips, the hearts of the young men around him found calm. But")
sh(63, "everyone was there ready for anything at all. As soon as the recitation began, the breeze that was blowing suddenly grew stronger,",
   [("wind_gust", "ބާރުވެ", -18)])
sh(64, "and the leaves of the trees began to shake wildly. Everyone could feel that this was the beginning of what they were about to face.",
   [("leaves_rustle", "ފަތްތައް", -18)])
sh(65, "They recited without looking at anyone's face, with the greatest care. But before long they began to feel that someone was moving around them.", hum=True)
sh(66, "Although fear surrounded them, no one could be seen there. All that could be heard was the eerie rustling of the leaves of the trees.",
   [("leaves_rustle", "ހެލިލާ", -18)])
sh(67, "Suddenly the wind grew strong, and sand came blowing and began to hit their faces. It was as if someone were throwing sand on purpose.",
   [("wind_howl", "ގަދަވެ", -16)])
sh(68, "So much sand was blowing that it was hard even to open their eyes. And the wind grew stronger, and heavy rain began to fall.",
   [("rain_start", "ވާރޭ", -16)])
sh(69, "In this chaos fear entered everyone's hearts. \"Hassanfulhu! Let's go find some shelter,\" some of those there said, getting up in fear.",
   [("breath_heavy", "ތެދުވަމުން", -22)])
sh(70, "Staying there in that situation became extremely hard. \"No, be brave! To save this island, your courage is very much needed today,\" Hassanfulhu said firmly.", hum=True)
sh(71, "His voice held patience and certainty. Whatever might happen, he wanted to complete the work he had begun. But")
sh(72, "opinions differed among them, and some, not accepting Hassanfulhu's word, started to walk away from there.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(73, "In their view, staying there at such a dangerous time was a great danger to their lives. Hassanfulhu and a few others")
sh(74, "stood firm in the strong wind and rain and carried on their recitation. It was a mighty struggle they made for the future of the island.",
   [("wind_gust", "ވަޔާއި", -20)])
sh(75, "\"Pay them no mind; you who have stayed are a very brave group,\" Hassanfulhu said, encouraging the young men who had heeded him and stayed.")
sh(76, "At that moment Shamaan was seen standing far away. He was extremely angry. Hassanfulhu knew the truth of these things.",
   [("heartbeat", "ފެނުނެވެ", -20)])
sh(77, "Not daring to come close to them, Shamaan stopped and stood at a distance. \"That is not Shamaan; don't look that way,\" Hassanfulhu warned.", hum=True)
sh(78, "\"But Shamaan might do anything,\" said Najmee, sitting there trembling with fear. \"No, he cannot do anything.",
   [("breath_heavy", "ރޫރޫ", -22)])
sh(79, "It comes in different forms to frighten you,\" Hassanfulhu went on encouraging them. Suddenly Shamaan vanished.",
   [("wind_gust", "ގެއްލުނެވެ", -20)])
sh(80, "No one knew which way he had gone. A short while later, what was seen was Shamaan's mother Sakeena")
sh(81, "coming at a fast walk holding a knife. Everyone who was reciting stood up in fear, but Hassanfulhu sat without even moving.",
   [("footsteps_sand", "ހިނގުމުގައި", -20), ("crowd_gasp", "ތެދުވި", -20)])
sh(82, "\"It's Sakeena coming!\" someone screamed in fear. \"That is not Sakeena; that is the jinni Zumra,\" Hassanfulhu answered calmly.",
   [("gasp", "ހަޅޭލަވައިގަތެވެ", -18)], hum=True)
SHOTS = S

"""Beat/shot plan for Hayaath episode 273 (used by plan_beats.py)."""

LOC = {
    "shore": "the edge of a secluded beach on the quiet side of a Maldivian island at night, rough coral rocks at the waterline, white sand, palm trees, full moon over a dark lagoon, waves breaking on the distant reef",
    "sea": "the dark open lagoon off a Maldivian island at night, moonlight on the water, distant torches on the shore",
    "hospital_night": "a small Maldivian island hospital corridor at night, pale green walls, plastic waiting chairs, fluorescent light, a door to the emergency room",
    "hospital_room": "a small Maldivian island hospital room at night, a single hospital bed with white sheets, pale green walls, a drip stand, a bedside table with a glass of water",
    "memory": "a modest Maldivian home in an earlier time, remembered, hazy and soft",
    "far_beach": "a deserted moonlit beach on the far side of a Maldivian island, far from the village, a large old two-storey house with a veranda among the palm trees behind the beach",
    "search": "the dark sea off a Maldivian island at night with a coast guard boat and small wooden dhonis searching with spotlights",
    "dawn_mosque": "outside a white coral-stone Maldivian mosque at dawn, sandy lane, palm trees, low walls, pink and pale-blue sky",
    "dawn_beach": "the deserted beach at dawn on the far side of a Maldivian island in front of a large old two-storey house among palms",
    "hospital_day": "a small Maldivian island hospital corridor in the early morning, pale green walls, daylight through the windows, a closed ward door",
}
MOOD = {
    "shore": "night, silver moonlight, deep blue sea, tense and shocked",
    "sea": "night, silver moonlight, dark water, desperate and exhausted",
    "hospital_night": "night, cold fluorescent light, tense and anxious",
    "hospital_room": "night, soft cold light, fragile and tense",
    "memory": "hazy, desaturated, dreamlike memory, soft vignette",
    "far_beach": "night, full moon, bright silver moonlight on the sand, mysterious and tender",
    "search": "night, spotlights sweeping the dark water, tense",
    "dawn_mosque": "early dawn, soft pink and blue light, tired and quiet",
    "dawn_beach": "early dawn, soft pale light, mysterious and quiet",
    "hospital_day": "early morning, pale daylight, tense",
}

BEATS = [
    dict(to=1, reason="new episode opening: scene continues on the shore right after the splash", chars=["hayaathu", "maaroof"], loc="shore",
         visual="Hayaathu on the moonlit shore pressing her hand over her mouth in shock, staring at spreading ripples on the sea; Maaroof standing a few steps away, also staring at the water, alarmed",
         camera="medium wide, eye level", amb="beach_night"),
    dict(to=3, reason="action change: Hayaathu has jumped into the sea and Maaroof dives after her", chars=["maaroof"], loc="shore",
         visual="Maaroof at the edge of the coral rocks, leaning forward to dive into the moonlit sea, shouting, a large splash and white foam in the water ahead of him where someone has just jumped in",
         camera="wide shot from the side", amb="beach_night", sens="other",
         safe="her jump into the sea is shown only as a splash; no person in the water"),
    dict(to=6, reason="characters change: people arrive and Maaroof brings Dhooma ashore", chars=["maaroof"], loc="shore",
         visual="on the moonlit beach a small crowd of Maldivian men with torches at the waterline; a young woman (Dhooma: round gentle face, warm medium-brown skin, muted teal-green long dress, cream hijab) lies unconscious on the sand wrapped in a dry grey blanket; Maaroof, soaking wet, kneels a respectful arm's length away looking at her anxiously; there is NO wheelchair anywhere in the scene, only one woman",
         camera="medium wide, slightly high angle", amb="beach_night", sens="other",
         safe="the rescue and carrying are not shown; Dhooma already on the sand, covered, Maaroof at a respectful distance"),
    dict(to=9, reason="action change: Maaroof searches the sea alone", chars=["maaroof"], loc="sea",
         visual="Maaroof soaking wet, standing waist-deep in the moonlit sea, exhausted and breathing hard, staring at the dark water with tearful eyes; far away small torches and a boat searching",
         camera="medium shot, eye level", amb="sea_search"),
    dict(to=13, reason="scene change: the hospital", chars=["waheed", "zoona", "areesha"], loc="hospital_night",
         visual="in the hospital corridor Waheed scolding his wife Zoona with a hard angry face, Zoona answering back defensively, while their daughter Areesha sits on a plastic chair nearby chatting on her phone, ignoring them",
         camera="medium wide, eye level", amb="hospital_night"),
    dict(to=14, reason="emotional turning point: Areesha's secret smile", chars=["areesha"], loc="hospital_night",
         visual="close-up of Areesha sitting on a hospital waiting chair holding her phone, a small secret satisfied smile spreading on her face",
         camera="close-up", amb="hospital_night"),
    dict(to=18, reason="flashback: Areesha's jealousy of Hayaathu", chars=["areesha", "maaroof", "hayaathu"], loc="memory",
         visual="memory: Areesha half hidden behind a doorway, watching with jealous eyes as Maaroof and Hayaathu talk shyly at a respectful distance in a sunny garden",
         camera="over-the-shoulder from behind Areesha", amb="memory", transition="dissolve"),
    dict(to=21, reason="flashback, different place and characters: Areesha complaining to her parents", chars=["areesha", "waheed", "zoona"], loc="memory",
         visual="memory: in the family living room Areesha pretending to cry, dabbing her eyes, in front of her parents Waheed and Zoona who sit on the sofa listening with grave faces; an envelope-like wedding proposal card on the table",
         camera="medium wide", amb="memory"),
    dict(to=22, reason="return to the hospital (reuse)", reuse="beat_006", loc="hospital_night", chars=["areesha"],
         visual="(reuse) Areesha's secret smile in the hospital", amb="hospital_night", transition="dissolve"),
    dict(to=26, reason="scene change: back to the shore; divers sit beside Maaroof", chars=["maaroof", "hassan"], loc="shore",
         visual="Maaroof sitting on the coral rocks at the shore in wet clothes, wiping his tears, his friend Hassan sitting beside him with a hand on his shoulder, consoling; tired divers resting on the sand behind them",
         camera="medium shot, eye level", amb="beach_night"),
    dict(to=27, reason="detail image after a long moment: the moonlit view they always watched together", loc="shore",
         visual="the full moon over the calm lagoon laying a silver path of light across the water, a leaning palm silhouette, an empty spot on the rocks, no people",
         camera="wide shot", amb="beach_night"),
    dict(to=29, reason="scene change: the far side of the island, a stranger brings Hayaathu ashore", chars=["hayaathu", "young_driver"], loc="far_beach",
         visual="Hayaathu lying unconscious on her back on the moonlit sand, fully clothed in her wet rose dress and blush-pink hijab, eyes closed, face lit by the moon; a young man in a wet black polo shirt stands a few steps away looking down at her face in wonder; the big old house among the palms behind",
         camera="wide shot, slightly high angle", amb="beach_night", sens="other",
         safe="the rescue and carrying are not shown; she already lies on the sand and he stands at a distance"),
    dict(to=32, reason="action change: Hayaathu comes round", chars=["hayaathu", "young_driver"], loc="far_beach",
         visual="Hayaathu propped up on one elbow on the moonlit sand, coughing, eyes half open and dazed; the young man kneels on the sand an arm's length away watching her face, astonished, moved",
         camera="medium shot, low angle from the sand", amb="beach_night", sens="other",
         safe="first aid and touching are not shown; only the moment she comes round, at a respectful distance"),
    dict(to=34, reason="scene change: the coast guard search at sea", loc="search",
         visual="a coast guard boat and several small wooden Maldivian dhonis on the dark sea at night sweeping their spotlights across the water, searching, no visible faces",
         camera="wide shot", amb="sea_search"),
    dict(to=37, reason="characters change: islanders gather on the shore, Maaroof learns the truth", chars=["maaroof"], loc="shore",
         visual="a crowd of islanders gathered on the moonlit beach talking in low voices, Maaroof among them in wet clothes listening, his face hardening with anger as he realises the truth",
         camera="medium wide", amb="beach_night"),
    dict(to=40, reason="scene change: hospital, waiting for Dhooma to wake", chars=["waheed", "zoona"], loc="hospital_night",
         visual="Waheed and Zoona standing worried in a hospital corridor in front of a large glass window, Waheed's jaw clenched; through the glass, inside the room, a young woman in a cream hijab lies unconscious in a hospital bed covered by a white sheet up to her shoulders; there is NO wheelchair anywhere and only one young woman, the one in the bed",
         camera="medium wide, eye level", amb="hospital_night"),
    dict(to=44, reason="characters change: Maaroof storms in and confronts Waheed", chars=["maaroof", "waheed", "zoona", "areesha"], loc="hospital_night",
         visual="in the hospital corridor Maaroof, furious and red-faced in his wet shirt, held back by the arms by two men, confronting Waheed; Waheed, Zoona and Areesha staring at him",
         camera="medium wide, eye level", amb="hospital_night", sens="violence",
         safe="the near attack is shown only as men holding Maaroof back; no blow"),
    dict(to=50, reason="focus moves to Areesha: her lying accusation", chars=["areesha", "zoona", "waheed", "maaroof"], loc="hospital_night",
         visual="Areesha talking with a fake innocent, scornful face, Zoona tugging at her sleeve to stop her, Waheed and Maaroof both glaring at Areesha with narrowed eyes",
         camera="medium shot", amb="hospital_night"),
    dict(to=52, reason="action change: Zoona pulls Areesha away; Maaroof's scornful reply", chars=["maaroof", "zoona", "areesha"], loc="hospital_night",
         visual="Maaroof in the foreground with a scornful half smile, while behind him Zoona leads Areesha away down the corridor by the hand, Areesha glancing back sulkily",
         camera="medium close-up with deep background", amb="hospital_night"),
    dict(to=55, reason="action change: Hayaathu is brought into the emergency room", chars=["hassan", "maaroof"], loc="hospital_night",
         visual="at the hospital emergency entrance at night police officers and medics rush in a stretcher with a young woman under a blanket (face not visible); Hassan in the foreground, breathless, calling out; Maaroof turning towards him",
         camera="wide shot, eye level", amb="hospital_night"),
    dict(to=58, reason="time jump and location change: dawn after Fajr prayer", chars=["maaroof"], loc="dawn_mosque",
         visual="men in sarongs and caps leaving a white coral-stone mosque at dawn; Maaroof, sleepless and tired, leaning back against a low white wall with his arms crossed, staring at the pale pink sky",
         camera="medium wide", amb="dawn_exterior", transition="black", sens="other",
         safe="the narration mentions him lighting a cigarette; smoking is never shown, he simply leans against the wall"),
    dict(to=62, reason="characters change: Hassan joins Maaroof", chars=["maaroof", "hassan"], loc="dawn_mosque",
         visual="Maaroof and Hassan standing by the white wall in the dawn light talking, Hassan with a serious puzzled face, Maaroof turning to him in surprise",
         camera="medium two-shot", amb="dawn_exterior", sens="other", safe="cigarette never shown"),
    dict(to=64, reason="detail image for the story's mystery: where Hayaathu was found", loc="dawn_beach",
         visual="a deserted beach at dawn in front of a large old two-storey house among palms, a single line of footprints in the wet sand leading out of the water up the beach, no people",
         camera="wide shot, low angle", amb="dawn_exterior"),
    dict(to=69, reason="return to the conversation (reuse)", reuse="beat_022", loc="dawn_mosque", chars=["maaroof", "hassan"],
         visual="(reuse) Maaroof and Hassan talking at dawn", amb="dawn_exterior"),
    dict(to=74, reason="characters change: Asad joins them", chars=["asad", "maaroof", "hassan"], loc="dawn_mosque",
         visual="Asad in white kurta and skullcap laughing as he talks, Maaroof and Hassan listening, the three men starting to walk along the sandy lane in the dawn light",
         camera="medium wide", amb="dawn_exterior"),
    dict(to=82, reason="scene change: hospital in the morning, Waheed blocks Maaroof", chars=["waheed", "maaroof"], loc="hospital_day",
         visual="Waheed standing in front of a closed ward door with his arm out barring the way, cold and hard; Maaroof facing him, frustrated and angry",
         camera="medium two-shot, eye level", amb="hospital_day"),
    dict(to=84, reason="scene change: Hayaathu awake in her hospital room", chars=["hayaathu", "nurse"], loc="hospital_room",
         visual="Hayaathu sitting up weakly in a hospital bed, leaning back against the pillow, pale and exhausted, hijab on; the nurse beside the bed offering her a glass of water",
         camera="medium shot", amb="hospital_room"),
    dict(to=89, reason="characters/action change: Waheed bursts in and the glass falls", chars=["waheed", "hayaathu", "nurse"], loc="hospital_room",
         visual="a dropped glass shattered on the hospital floor with spilled water in the foreground; Waheed standing in the doorway red with anger; Hayaathu on the bed looking at him with tearful eyes; the nurse startled",
         camera="low angle from the floor, deep focus", amb="hospital_room"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Hayaathu clapped her hand over her mouth and began to cry. 'Dhooma...' Maaroof said too. Hayaathu ran with all her strength.",
   [("gasp", "ރޯން", -20), ("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(2, "Before Maaroof could catch her hand, Hayaathu jumped into the sea to save her sister. Maaroof was stunned.",
   [("splash", "ފުންމާލިއެވެ", -12)])
sh(3, "'Hayaathu!' Maaroof shouted at the top of his voice and dived in where she had jumped. He knew Hayaathu couldn't swim.",
   [("splash", "ފުއްމާލިއެވެ", -12)], hum=True)
sh(4, "At the noise people started coming. Two or three men jumped into the sea to save them. A while later Maaroof came ashore carrying Dhooma.",
   [("splash", "ފުންމާލިއެވެ", -18)])
sh(5, "The others kept diving, searching for Hayaathu. 'Dhooma... Dhooma...' Maaroof called, gently tapping her cheek.")
sh(6, "Dhooma didn't respond. The people there took her to the hospital. Maaroof dived into the sea again, to look for Hayaathu.",
   [("splash", "ފުންމާލިއެވެ", -16)])
sh(7, "He dived to the bottom and came back up. The divers too searched for Hayaathu like this for a long time.")
sh(8, "Diving again and again, Maaroof came up exhausted. He couldn't believe Hayaathu would leave him and go so quickly.",
   [("breath_heavy", "އެރިއެވެ", -22)], hum=True)
sh(9, "Exhausted, Maaroof stared at the sea with tear-filled eyes. Police and many islanders kept searching for Hayaathu.", hum=True)
sh(10, "At the hospital Zoona and Waheed waited anxiously. As worried as he was, Waheed was furious with Zoona.")
sh(11, "Waheed, who raises his voice anywhere, had already shouted at Zoona twice since Dhooma was brought in.")
sh(12, "Zoona was a loud, sharp-tongued woman, but even she feared Waheed. Next to Zoona, Areesha chatted on her phone, ignoring what they said.")
sh(13, "She went on with what she was doing. 'I'm telling you the truth — tonight Hayaathu will die by my hand,' Waheed said harshly.", hum=True)
sh(14, "At that sentence a smile appeared on Areesha's face. Who knows why. Areesha hates Hayaathu.")
sh(15, "She never wanted anything good to happen to Hayaathu. While she kept begging Maaroof, he proposed to Hayaathu — and her hatred grew.")
sh(16, "Even before, Hayaathu's beauty had cost her sleep. For days Areesha had tried every way to ruin the beauty of Hayaathu's face.")
sh(17, "But nothing changed Hayaathu's beauty. Even a pimple healed quickly without leaving a mark.")
sh(18, "Because of that, sleep had left Areesha's eyes. But today Areesha was very happy.")
sh(19, "She had managed to push her own marriage proposal onto Hayaathu. The game she played to marry that old man to Hayaathu didn't even take long.")
sh(20, "Crying and sobbing two or three times in front of her father and mother, saying Hayaathu mocked her and gossiped about the man to others —")
sh(21, "— and so her father gave Hayaathu in her place, and the man's family agreed to the marriage with Hayaathu. Today Areesha was very happy.")
sh(22, "And on the other side, the blame for what happened to Dhooma would also fall on Hayaathu. So why shouldn't Areesha be happy?")
sh(23, "Maaroof still sat at the water's edge. The police and divers continued the search for Hayaathu. Tears kept falling from Maaroof's eyes.")
sh(24, "To win Hayaathu he had worked until this very day. Her uncle's condition was 3 million rufiyaa.")
sh(25, "He had worked day and night to earn it. The divers, exhausted, came ashore and sat down beside Maaroof.")
sh(26, "Maaroof wiped away his tears. 'Maaroof... be strong...' his friend Hassan said, in a voice that had given up hope.",
   [("sigh", "ފުހެލިއެވެ", -22)], hum=True)
sh(27, "Maaroof was still looking at the dark sea. The silver moonlight on the sea was the view he always came to watch with Hayaathu.")
sh(28, "He closed his tear-filled eyes and let out a deep sigh. Far from the village, on the other side of the island, a young man came out of the sea carrying the unconscious Hayaathu.",
   [("sigh", "ހަށިފުރާ", -20), ("footsteps_sand", "ގޮވައިގެން", -22)])
sh(29, "He laid her down on the sand and looked at her. It was a full-moon night, and in the silver light he saw Hayaathu's beautiful face.")
sh(30, "He tapped her cheek two or three times. No response. Without waiting, he gave her the first aid for drowning.", hum=True)
sh(31, "After a while, with a choking cough, she brought up the salt water. The young man kept looking at her face.",
   [("gasp", "ކެއްސާލުމާއި", -18)])
sh(32, "Who knows why. His heart was beating hard. It was something he had never felt before.",
   [("heartbeat", "ވިންދު", -16)])
sh(33, "The search had gone on for nearly 3 hours. Still no Hayaathu. The coast guard and many island boats were out searching.",
   [("boat_engine", "ދޯނި", -20)])
sh(34, "As time passed Maaroof lost heart. Angry that he hadn't held her back, he began to be furious with himself.", hum=True)
sh(35, "Many islanders had gathered. Maaroof listened closely to the questions being asked and the answers given.")
sh(36, "That was how Maaroof learned why Hayaathu and Dhooma had cried tonight. He already knew how bad her uncle Waheed was.")
sh(37, "But he never thought it would go this far. Hearing it all, Maaroof ran to the hospital.",
   [("footsteps_pavement", "ބާރުލާފައި", -20)])
sh(38, "Waheed and Zoona were worried because Dhooma hadn't woken. If anything happened to Dhooma, Waheed's whole life would be ruined.")
sh(39, "On the other hand, no one knew what had happened to Hayaathu. If anything happened to her, plenty of fingers would point at him.")
sh(40, "And he had gone against his father's will. Waheed sat furious about all of it. Meanwhile Areesha kept wishing Hayaathu would not be found.")
sh(41, "Then Maaroof would be hers. She was sure of it. 'Waheed.' Maaroof called Waheed by name with no respect at all.")
sh(42, "Waheed and the others in the hospital looked at Maaroof. He was red with anger.")
sh(43, "If the people there hadn't held him back, Maaroof would have attacked Waheed.", hum=True)
sh(44, "'I never thought you were that kind of man. After promising me, you decided to marry Hayaathu to someone else — now you see the result. Aren't you ashamed?'")
sh(45, "Maaroof said, furious. 'Dad didn't do anything...' Areesha said quickly. 'Hayaathu did everything...")
sh(46, "She agreed to marry that man herself. Dad didn't say a thing. Hayaathu told me about it first.")
sh(47, "She wants to leave this place fast. Does Maaroof think she's such a good person? You don't know her tricks.")
sh(48, "She's not like us,' Areesha said mockingly. As soon as Areesha started talking, Zoona hurried to stop her.")
sh(49, "Waheed narrowed his eyes at Areesha. Maaroof too narrowed his eyes at her. Could Areesha fool Maaroof?")
sh(50, "Areesha was very good at lying and fake crying. Whatever wrong she did, she put on Hayaathu's head.")
sh(51, "Maaroof smiled scornfully with one side of his mouth. 'Yes, Areesha, you're right — Hayaathu is not someone like you.'")
sh(52, "Zoona understood what Maaroof meant. 'Areesha, dear, never mind... come this way...' Zoona took Areesha by the hand and led her away.",
   [("footsteps_pavement", "ދުރަށް", -24)])
sh(53, "As Maaroof was about to say something to Waheed, police officers rushed into the emergency room carrying an unconscious girl.",
   [("wheelchair_roll", "އެމެޖެންސީގައި", -20)])
sh(54, "The people gathered there ran over. Many knew who she was. 'Maaroof, Hayaathu's been found!'",
   [("footsteps_pavement", "ދުވެފައި", -20)])
sh(55, "Hassan said, catching his breath. Without a glance at Waheed, Maaroof ran towards the emergency room.",
   [("footsteps_pavement", "ދުވެފައި", -20)])
sh(56, "After the dawn prayer, people left the mosques in every direction. Coming out of the mosque, Maaroof stopped by the wall.")
sh(57, "After last night, Maaroof hadn't slept yet. He leaned back against the wall, staring into the sky.")
sh(58, "Last night he had almost lost Hayaathu. Knowing how Waheed thinks, he was afraid she would be forced to marry someone.", hum=True)
sh(59, "He breathed out slowly into the morning air. Hassan came up from behind and patted him on the back. 'So...",
   [("cloth_rustle", "ކޮއްޓާލިއެވެ", -22)])
sh(60, "how is she now?' Hassan asked Maaroof. 'What can I say... I felt my heart stop at that moment.'")
sh(61, "Maaroof said. 'Hayaathu wasn't found in the sea... did you know?' Hassan asked.")
sh(62, "Maaroof turned and looked at Hassan. 'What? She jumped in right in front of me to save Dhooma...'")
sh(63, "Maaroof said. 'We saw that too. I mean she was found on the beach far from the village, in front of that big house. I think someone saved her.")
sh(64, "Brought her all the way to shore...' Hassan said slowly. 'What are you trying to say?' Maaroof asked. 'I'm saying... I don't think it was a human.'", hum=True)
sh(65, "Hassan said. Maaroof shook his head and raised his eyebrows, looking at Hassan.")
sh(66, "'I never thought you'd talk such nonsense, Hassan,' Maaroof said with a smile. 'Ask the hospital nurses...")
sh(67, "or go and see for yourself... Hayaathu's...' Hassan stopped halfway. Maaroof kept looking at him.")
sh(68, "'All of us young men were with you — the police, the fishermen, the divers — searching for Hayaathu...")
sh(69, "who would think she'd be found so far from the village, laid on the shore? If it were a person, they'd have told us...'")
sh(70, "Hassan said thoughtfully. Just then Asad, coming out of the mosque, stopped to listen. 'Well done, Hassan,")
sh(71, "someone called to say Hayaathu was found... and now the stories begin. Lucky I happened to be near the phone when the call came.'")
sh(72, "Asad said, laughing. 'Who called?' Maaroof asked. 'No idea,' Asad said, thinking.")
sh(73, "'The owner of that big house lives off the island, right?' Maaroof said. 'Yes, but last week we heard some people came to stay there.'")
sh(74, "Asad said. Talking, they started walking. Instead of going home, Maaroof went to the hospital.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)])
sh(75, "But because of Waheed he wasn't allowed in. 'Bring the 3 million... then you can meet Hayaathu...'")
sh(76, "Waheed said harshly. 'After promising me, now you're marrying Hayaathu to someone else,' Maaroof said, displeased.")
sh(77, "'Whoever puts 3 million in my hand gets Hayaathu,' Waheed said, unmoved. 'What kind of man are you... Hayaathu loves me.")
sh(78, "You have no right to do this to her,' Maaroof said angrily. 'Did her parents leave her to me with no rights?")
sh(79, "With no responsibility? I raised her... why shouldn't I put a price on her? What about everything I spent?")
sh(80, "I raised her with dignity... why shouldn't I name a price?' Waheed said loudly. 'You're her father's younger brother...")
sh(81, "you're the one who must look after her,' Maaroof said. 'Brother... but half...' Waheed said.")
sh(82, "'Anyway, there's no time for long talk. Give 3 million and take her... otherwise I'll marry her to whoever I want.'")
sh(83, "Waheed said, walking inside. She got up from the bed and leaned wearily against the pillow. The nurse tried to give Hayaathu some water.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -24), ("cloth_rustle", "ތެދުވެ", -24)])
sh(84, "Her face showed she had swallowed salt water. She looked a little pale. Yet when she was brought in there was no sign of salt water.")
sh(85, "As the glass touched her lips, she heard Waheed's harsh voice. The glass in her hand fell.",
   [("glass_break", "ވެއްޓުނެވެ", -14)])
sh(86, "The nurse jumped at the sound. With tear-filled eyes Hayaathu looked at Waheed standing before her, red with anger.",
   [("gasp", "ސިހުމަކާއި", -18)])
sh(87, "Why is uncle angry again today? What wrong has she done? 'If anything had happened to Dhooma...", hum=True)
sh(88, "you're lucky nothing happened to Dhooma,' the furious Waheed told Hayaathu. 'People are spreading all kinds of talk. You will marry Fazaal — ugly, hideous, lame or blind,", hum=True)
sh(89, "this is my final decision,' Waheed said, stressing every word.", hum=True)
SHOTS = S

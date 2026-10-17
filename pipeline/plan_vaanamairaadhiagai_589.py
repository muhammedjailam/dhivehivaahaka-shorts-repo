"""Beat/shot plan for Vaanama Iraadhiagai episode 589 (used by plan_beats.py). Anime look; see series_bible.md."""

LOC = {
    "lane": "a white coral-sand lane on a small Maldivian island, coral-stone garden walls, small single-storey houses with tin roofs and verandas, tall coconut palms, a glimpse of the turquoise lagoon at the end of the lane",
    "home_afternoon": "the front yard and open veranda of Luyoon's family house on a Maldivian island: a small single-storey house with a tin roof, a wide open veranda with a wooden bench and potted plants, a low coral-stone wall with a gate onto the sand lane, a rope swing-seat (joali) under a leafy tree, coconut palms beyond",
    "naaifa_dusk": "a small simple bedroom in Naaifaa's island house, a wooden window seat by an open window with a view of coconut palms and the lagoon, plain whitewashed walls, a curtain moving in the breeze",
    "office": "a small bright open-plan office of a state company on a Maldivian island, simple desks, a desktop computer, a window with coconut palms and a blue sky outside",
    "naaifa_yard": "the sandy back yard of Naaifaa's island house, a simple wooden bench under a breadfruit tree, a coral-stone wall, potted plants, coconut palms",
    "study_night": "the small modest living room of Luyoon's family house at night, a low wooden table covered with open school textbooks and notebooks with blank pages, a warm table lamp, a ceiling fan, a doorway to the veranda",
    "joali_night": "the front yard of Luyoon's family house at night: a wide rope swing-seat (joali) under a leafy tree, the house veranda behind with its door open and warm lamp light spilling out, a low coral-stone wall and gate, coconut palms against a starry sky",
    "morning": "the sand lane and gate in front of Luyoon's family house in the early morning, freshly swept white coral sand, coconut palms, the sun rising over the lagoon beyond the rooftops",
    "naaifa_morning": "a small simple bedroom in Naaifaa's island house in the morning, a wooden window seat by an open window with coconut palms and a sparkling lagoon outside",
}
MOOD = {
    "lane": "golden late afternoon, warm sunlight slanting through the palms, long soft shadows, sparkling lagoon light, tender romantic mood with a hint of watchful whispers",
    "home_afternoon": "golden late afternoon, warm sunlight and leaf shadows dappling the yard, soft lens glow, gentle but troubled",
    "naaifa_dusk": "blue dusk, the sky outside fading from orange-pink to deep blue, the room dim, her face lit by a cold soft phone glow, lonely and jealous",
    "office": "bright midday, clear white daylight from the window, crisp and tense",
    "naaifa_yard": "golden afternoon, warm light filtering through the breadfruit leaves, quiet and sorrowful but tender",
    "study_night": "night, warm amber lamp light on the table and faces, deep blue shadows in the corners, cosy and hopeful",
    "joali_night": "moonlit night, deep blue sky full of stars, warm amber lamp light from the open door, gentle breeze in the palms, intimate then tense",
    "morning": "bright morning, the sun just risen, soft gold light and long shadows, glowing sky with drifting pink-gold clouds, fresh and happy",
    "naaifa_morning": "soft bright morning, gentle sunlight through the window, calm and remorseful",
}

BEATS = [
    dict(to=4, reason="episode opening: Luyoon and Maaniu happy together while the island watches", chars=["luyoon", "maaniu"], loc="lane",
         visual="Luyoon and Maaniu walking side by side along the white sand lane towards the viewer, an arm's length apart with a clear gap between them, both smiling shyly at each other; in the background two small women in headscarves peek over a coral-stone wall whispering to each other and an old man glances from a doorway; sweeping wide anime frame with glowing sky and palms",
         camera="wide shot, eye level, the couple in the upper two-thirds, the sand lane as a calm lower third", amb="village_day",
         sens="intimacy", safe="unmarried couple: walking side by side an arm's length apart, no touching"),
    dict(to=9, reason="scene and character change: Luyoon comes home from the office and Zaina runs to her with the classmate's gossip", chars=["luyoon", "zaina"], loc="home_afternoon",
         visual="Luyoon just stepping through the garden gate after work with her brown shoulder bag, bending slightly towards her younger sister Zaina, who has run up to her across the yard with a hurt, earnest face, telling her something; Luyoon's eyes widening with surprise and the first flicker of anger",
         camera="medium wide two-shot, eye level", amb="island_house_day"),
    dict(to=13, reason="action change: Luyoon phones Maaniu, upset", chars=["luyoon"], loc="home_afternoon",
         visual="close-up of Luyoon standing on the veranda holding a phone to her ear (the phone's back facing the viewer), her other hand gripping the strap of her brown shoulder bag, brows drawn together, anime tears welling in her large eyes, lips parted mid-question",
         camera="close-up, slightly low angle, her face in the upper half", amb="island_house_day"),
    dict(to=18, reason="character change: Maaniu arrives at the house; Luyoon cries and they promise to stay together", chars=["luyoon", "maaniu", "aishath"], loc="home_afternoon",
         visual="on the open veranda, Luyoon sitting on the wooden bench wiping anime tears from her cheek with the back of her hand; Maaniu standing at the top of the veranda steps an arm's length away from her, leaning slightly forward with a gentle, serious, reassuring expression; her mother Aishath standing in the open doorway behind them watching with concern",
         camera="medium wide, eye level", amb="island_house_day", sens="intimacy",
         safe="unmarried couple: on the open veranda with Aishath present, an arm's length apart, no touching"),
    dict(to=20, reason="scene and character change: island talk of the wedding; Naaifaa texts and calls Maaniu", chars=["naaifaa"], loc="naaifa_dusk",
         visual="Naaifaa sitting alone on the window seat, knees drawn up, holding her phone to her ear with its back facing the viewer, her face lit by its cold glow, eyes narrowed with longing and jealousy, lips pressed together; the dusk sky glowing orange-pink behind the palms outside",
         camera="medium close-up, eye level, from the side", amb="home_night"),
    dict(to=23, reason="time jump and scene change: one noon Naaifaa calls Maaniu at work; he begs her to stop", chars=["maaniu"], loc="office",
         visual="Maaniu sitting at his desk holding the phone to his ear (back of the phone to the viewer), his other hand pressed to his forehead, eyes half closed in tired frustration as he pleads; the computer monitor turned away from the viewer showing only a soft glow; bright window with palms behind",
         camera="medium shot, eye level", amb="office_day", transition="black"),
    dict(to=26, reason="action change: Maaniu hangs up, blocks her and throws himself into his work", chars=["maaniu"], loc="office",
         visual="Maaniu placing his phone face-down on the desk with a firm hand and turning back to his keyboard, typing, his face calm and resolved, a faint determined smile; the monitor seen from behind; sunlight across the desk",
         camera="medium wide, slightly from the side", amb="office_day"),
    dict(to=29, reason="scene and character change: Naaifaa cries to her mother Hawwa Manike", chars=["naaifaa", "hawwa_manike"], loc="naaifa_yard",
         visual="Naaifaa sitting on the wooden bench under the breadfruit tree, head bowed, anime tears on her cheeks, her phone held loosely in her lap; her mother Hawwa Manike sitting beside her with a hand on her daughter's shoulder, speaking softly with a calm, wise, gently sad expression",
         camera="medium two-shot, eye level", amb="garden_day", sens="other",
         safe="her crying is shown calmly on a bench with her mother comforting her (bible rule 10), no hysteria"),
    dict(to=32, reason="time jump and scene change: Zaina's O-level exam days; Luyoon helps her study at night", chars=["luyoon", "zaina", "aishath"], loc="study_night",
         visual="Luyoon and Zaina sitting side by side at the low table covered with open textbooks (pages blank, no writing), Luyoon pointing to a page and explaining with a kind smile, Zaina's face lighting up with understanding, a pencil in her hand; their mother Aishath standing in the doorway behind them smiling happily with her hands clasped",
         camera="medium wide, slightly high angle", amb="living_night", transition="black"),
    dict(to=37, reason="scene change: night on the joali; Aishath is happy, Luyoon tells her about Naaifaa", chars=["aishath", "luyoon"], loc="joali_night",
         visual="Aishath and Luyoon sitting together on the wide rope swing-seat under the tree in the moonlit yard, Aishath turned towards her daughter with a warm happy smile, Luyoon looking down at her hands with a worried, sad face; warm lamp light from the open door behind, stars glittering above the palms",
         camera="medium wide, eye level, the stars and tree in the upper part", amb="island_house_night"),
    dict(to=40, reason="character change: neighbour Zahuriyya arrives and disparages Maaniu", chars=["zahuriyya", "aishath", "luyoon"], loc="joali_night",
         visual="Zahuriyya standing a few steps inside the gate in the moonlight, leaning forward with a gossiping, disapproving smirk and raised eyebrows; Aishath on the swing-seat turning to her with a polite, puzzled smile; Luyoon beside her mother, her face tightening, eyes flashing",
         camera="medium wide, eye level", amb="island_house_night"),
    dict(to=43, reason="action change: Luyoon stands up and tells Zahuriyya to leave; Aishath stunned", chars=["luyoon", "zahuriyya", "aishath"], loc="joali_night",
         visual="Luyoon standing up in front of the swing-seat, upright and firm, hands at her sides, speaking with a determined, hurt expression and shining eyes; Zahuriyya a respectful distance away, taken aback, leaning back with her mouth open; Aishath still seated on the swing-seat, speechless, a hand near her mouth; nobody pointing, no raised hands",
         camera="medium wide, eye level", amb="island_house_night", sens="other",
         safe="the argument is shown only as tense faces at a respectful distance (bible rule 11)", ),
    dict(to=45, reason="action change: relieved, Luyoon goes inside to sleep, Aishath follows", chars=["luyoon", "aishath"], loc="joali_night",
         visual="Luyoon seen from behind walking up the veranda steps into the warm lamp-lit doorway, her shoulders relaxed, glancing back with a small relieved face; Aishath following a few steps behind her; the empty rope swing-seat in the foreground moonlight and a deep starry sky",
         camera="wide shot from the yard, slightly low", amb="island_house_night"),
    dict(to=48, reason="time jump: the next morning; Luyoon leaves happily for work, Zaina off to her last exam", chars=["luyoon", "zaina"], loc="morning",
         visual="Luyoon at the gate in the fresh morning with her brown shoulder bag, smiling brightly with a phone to her ear (back of the phone to the viewer); Zaina beside her clutching her books to her chest and a school bag on her shoulder, ready for her exam, looking up hopefully; the rising sun glowing gold over the lagoon behind the palms",
         camera="medium wide, eye level, faces in the upper half, sunlit sand below", amb="dawn_exterior", transition="black"),
    dict(to=50, reason="character change: Naaifaa stops harassing them and sends an apology", chars=["naaifaa"], loc="naaifa_morning",
         visual="Naaifaa sitting on the window seat in soft morning light, looking down at the glowing phone in both hands (screen not visible), typing a message with a remorseful, softened face and a single small anime tear, the sparkling lagoon outside the window",
         camera="medium close-up, eye level", amb="room_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Many eyes and many tongues in this world are there just for that kind of people. Around people who live in love there will be many watching eyes, and many discussions will go on.")
sh(2, "Much effort will be made to find something to hurt them. That is the nature of the world.")
sh(3, "As Luyoon and Maaniu went on living beautifully, many people kept watching them, and Maaniu and Luyoon noticed many things being done.")
sh(4, "But they dismissed those eyes as something pointless. Yet Naaifa and Luyoon... it meant nothing to them.")
sh(5, "Between the two of them there was such boundless love that no one else could come in. It was the time Luyoon came home after finishing at the office.")
sh(6, "Little Zaina came running to Luyoon. \"Donthi... a girl in my class said Donthi is a bad girl...",
   [("footsteps_sand", "ދުވެފައި", -22)])
sh(7, "I said Donthi is not that kind of girl at all.\" said Zaina. Zaina had always kept a very close bond with Luyoon.")
sh(8, "\"Zaina, did you ask that girl who said it?\" said Luyoon. \"She said Naaifa Dhaththa said it.\" Those words of Zaina's made hatred rise in Luyoon's heart.")
sh(9, "There was no reason at all for Naaifa to say such things to children that young.")
sh(10, "At once Luyoon took the phone from her handbag and called Maaniu. \"Maaniu... why is Naaifa doing this...",
   [("cloth_rustle", "އަތްދަބަހުގައި", -24), ("phone_buzz", "ގުޅާލިއެވެ", -22)])
sh(11, "She's running around the whole island telling bad stories about me. What is my crime? Is being friends with Maaniu the problem?\"")
sh(12, "Luyoon fired the questions all at once. It was a moment when Luyoon needed to let out the sadness in her heart.")
sh(13, "\"I'm coming to your house right now.\" With that, Maaniu went to Luyoon's house, to see what was going on.",
   [("footsteps_sand", "ދިޔައީ", -22)])
sh(14, "As soon as Maaniu came to Luyoon's house, she began to complain. \"How big a thing is this, Maaniu... she's picking on us...")
sh(15, "Why must such things happen...\" Luyoon said, bursting into tears. Every one of these lessons had become a hardship for Luyoon and Maaniu.",
   [("sob_breath", "ރޮއިގަނެފައި", -24)], hum=True)
sh(16, "All the two of them could do was go on with patience. They promised each other to keep loving in every situation.")
sh(17, "They resolved to go on without caring what people said. More and more, they let Naaifa see them together.")
sh(18, "Because they were sure it would make Naaifa so heartsick that her anger would boil over beyond control.")
sh(19, "The talk of Maaniu and Luyoon's marriage became common across the island. For Naaifa this was painful and hard to bear.")
sh(20, "Naaifa started sending messages to Maaniu's phone. Saying she loved him boundlessly, she even called Maaniu's phone many times.",
   [("phone_buzz", "ގުޅަން", -20)])
sh(21, "But Maaniu paid no attention at all; he turned a deaf ear. It was noon one day. Naaifa started calling Maaniu's phone to bother him.",
   [("phone_buzz", "ގުޅާ", -18)])
sh(22, "\"Naaifa, why are you doing this... Once you already caused a problem between the two of us, didn't you... So can't you stop calling me?")
sh(23, "I'm begging you,\" Maaniu said in a pleading tone. Because what Maaniu wanted was to start a life with Luyoon.",
   [("sigh", "އާދޭހުގެ", -22)])
sh(24, "Maaniu had in his heart never to do anything at all that would hurt Luyoon. \"Maaniu, just listen to what I'm saying...\"")
sh(25, "Naaifa's stubbornness showed. Maaniu hung up. After blocking the number, Maaniu kept himself busy with his work, without a break.",
   [("keyboard_typing", "މަސައްކަތުގައި", -24)])
sh(26, "This is a true example of love. Because he had so many hopes of a life with the one he loved, Maaniu kept doing everything he could. \"Mother...")
sh(27, "...why is Maaniu refusing to stay in touch with me... I want him so much...\" Naaifa said, crying, to her mother (Hawwa Manike).",
   [("sob_breath", "ރޮމުން", -24)], hum=True)
sh(28, "\"Naaifa... the world turns like a wheel. Whoever goes will go, whoever comes will come. Nobody can be brought by force,\" said Hawwa Manike.")
sh(29, "That is true. The world turns like a wheel. Sometimes we must face sorrow; at other times we face joy.")
sh(30, "That is the way of the world. It was Zaina's O-level days. Luyoon gave Zaina a great deal of help.")
sh(31, "She kept clearing up the many questions Zaina didn't know. Zen's studies, too, got better day after day.",
   [("page_turn", "އޮޅުންފިލުވައި", -24)])
sh(32, "Aishath was overjoyed at this. When Zaina went to sleep, Luyoon went outside to her mother at the joali.",
   [("creak", "ޖޯލިފައްޗަށް", -24)])
sh(33, "\"My child, Mother is so happy today to see you two living happily,\" said Aishath.")
sh(34, "But for Luyoon it had become a completely sad subject. \"Mother, don't say that...")
sh(35, "Maybe the two of us will break up completely,\" said Luyoon. At that, Aishath said in surprise,",
   [("gasp", "ހައިރާން", -24)])
sh(36, "\"Did something go wrong again... Is Maaniu angry again...?\" said Aishath. \"No, Mother...")
sh(37, "a woman called Naaifa is trying to come between Luyoon and Maaniu.\" Maaniu was at his wits' end.")
sh(38, "Luyoon told her everything, word for word. \"Aishath, what a soft little chat you two are having...\" said Zahuriyya. \"Well, of course mother and daughter have things to talk about...\"")
sh(39, "Aishath replied cheerfully. \"Oh, not that... I've heard the story. That rotten, good-for-nothing boy Maaniu...")
sh(40, "...is this house's fine, decent girl Luyoon going with him?\" Zahuriyya said disapprovingly. Hearing that, Luyoon, unsettled, shouted at Zahuriyya.",
   [("breath_heavy", "ގޮވުނެވެ", -22)])
sh(41, "\"Only I know who I should marry, not anyone else. Zahuriyya, it would be better if you stopped talking like that and left,\" said Luyoon.",
   hum=True)
sh(42, "No one had ever heard her argue rudely with anyone in front of her elders. But with things having come this far, Luyoon's anger slipped out of control.")
sh(43, "Aishath could only sit there with nothing to say. It seemed Luyoon had held this in for many days.",
   hum=True)
sh(44, "Having said what she wanted to Zahuriyya, a coolness came over Luyoon's heart, and much happiness. \"Mother, Luyoon is going to sleep...\"",
   [("sigh", "ފިނި", -22)])
sh(45, "Still unsettled, Luyoon went into the house. Aishath followed her towards the house. And the sun rose to do its duty.",
   [("door_open", "ވަނެވެ", -22), ("footsteps_sand", "ހިނގައިގަތީ", -24)])
sh(46, "The island was bustling. Zaina was getting ready to go to her exam.")
sh(47, "Luyoon too was busy getting ready for the office. Happiness showed on Luyoon's face. Maaniu...",
   [("keys_jingle", "އޮފީހަށް", -24)])
sh(48, "Before going to work, Luyoon called Maaniu; he said he was awake. Because it was Zaina's last exam, she had spent these three days reading her books,",
   [("phone_buzz", "ގުޅަލިއެވެ", -22), ("page_turn", "ފޮތް", -24)])
sh(49, "and clearing up the many questions she didn't know. Now Naaifa bothered Maaniu less and less.")
sh(50, "And she even sent Luyoon and Maaniu a message asking for forgiveness.",
   [("phone_buzz", "މެސްޖް", -20)], hum=True)
SHOTS = S

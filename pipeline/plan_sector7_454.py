"""Beat/shot plan for Sector 7 episode 454 (used by plan_beats.py)."""

LOC = {
    "detention": "a modern high-security detention room inside a secret building on the clean upper level of the underground bunker: smooth white walls sealed with seamless brushed-steel panels, thin cold white neon light strips in the ceiling, a clear glass table with two padded white chairs facing each other, one wall made entirely of thick glass looking out at the distant white towers of the upper-level city, a polished pale grey floor",
    "detention_dim": "the same white high-security detention room on the upper level of the bunker, now with the ceiling light strips dimmed: steel-panelled white walls, the clear glass table and two padded white chairs, the tall glass wall showing the distant towers of the upper-level city at night, a polished pale grey floor",
    "cctv": "a luxurious upper-level Council meeting room with white and gold walls, soft golden ceiling light and a long polished white table with high-backed chairs",
    "memory": "a cluttered secret engineering workshop deep inside the bunker years ago: a steel drafting table covered with large blueprint sheets of glowing pale-blue line diagrams of tunnels and shafts (only lines, no writing), old hanging lamps, pipes and tools on rusted walls",
    "warehouse": "the old rusted steel warehouse HQ of the Revival resistance in Sector 7: rusted girders, a raised metal platform, fire barrels and hanging work lamps, a crowd of young people in worn jackets",
    "bunker": "a vast symbolic cross-section of the Sanctuary bunker deep underground: a tall stone shaft with the clean white-and-gold luxury upper level near the top and the rusted, smoky machinery levels of Sector 7 at the bottom, tiny lit windows and walkways on every level",
    "balcony": "a high balcony with a clear glass railing on a tall white tower of the bunker's upper level, overlooking the upper-level city of white towers and glass bridges spread beneath a vast dark rock cavern ceiling",
}
MOOD = {
    "detention": "cold clinical white neon light, pale steel-blue shadows, sterile silence, tense and guarded",
    "detention_dim": "dimmed cold white light, deep steel-blue shadows, the glass wall dark blue with sparse distant city lights, heavy silence, exhaustion turning into quiet resolve",
    "cctv": "seen as grainy blue-green tinted high-angle security-camera footage with soft scan lines and a faint vignette, cold and sinister",
    "memory": "warm faded amber lamplight, soft hazy dreamlike glow with a soft vignette and desaturated colours, nostalgic and secretive",
    "warehouse": "flickering orange firelight from fire barrels, smoke haze, faded like a bitter memory, rousing yet hollow",
    "bunker": "the upper levels glowing soft gold, the lowest levels in rusted dark red and amber, a broad band of grey haze between them, solemn and contemplative",
    "balcony": "night cycle, the artificial sun switched off, cold deep-blue darkness with sparse cold white window lights below, a faint wind, foreboding and determined",
}

BEATS = [
    dict(to=5, reason="scene change / time jump: Aira wakes up in the upper-level detention room", chars=["aira"], loc="detention",
         visual="Aira slumped sideways in a padded white chair at a clear glass table, her head resting against the high chair back, eyes only half open and squinting up at the cold white neon strips in the ceiling, her face weary and smudged with grime, her olive-brown coat dusty, charcoal hijab slightly askew but fully covering her hair and neck; the bare glass table top and pale floor fill the lower third",
         camera="medium shot from slightly above, her face in the upper half", amb="detention_room", transition="black",
         sens="violence", safe="the remembered gunfire and friends' cries are only heard (muffled distant thud); the image shows only her waking"),
    dict(to=8, reason="action change: she sits up, finds her hands free and takes in the sealed room", chars=["aira"], loc="detention",
         visual="Aira sitting bolt upright on the padded white chair at the glass table, alert and guarded, shoulders tensed in a defensive posture, eyes darting around the sealed white room; her hands free with no restraints, resting tensely on the glass; around her the seamless steel-panelled white walls, ceiling light strips and the tall glass wall with distant towers; the opposite chair still in soft shadow",
         camera="wide shot, eye level, the room around her, the glass table and pale floor as a calm lower third", amb="detention_room",
         sens="other", safe="the iron chains she expected are not shown: her hands are visibly free"),
    dict(to=11, reason="character enters the frame: Commander Kyle sitting across the table", chars=["kyle", "aira"], loc="detention",
         visual="over-the-shoulder view from behind Aira (her charcoal hijab and olive coat shoulder soft in the foreground left) towards Kyle sitting upright on the other side of the clear glass table, his immaculate black high-collared uniform without a crease, the row of small silver medals on his chest gleaming in the cold light, no holster; his calm, unreadable dark eyes fixed on her; the empty glass table top between them",
         camera="medium over-the-shoulder two-shot, eye level, Kyle's face in the upper third", amb="detention_room"),
    dict(to=14, reason="focus change: close-up of Aira's furious accusation", chars=["aira"], loc="detention",
         visual="close-up of Aira leaning forward over the glass table, eyes blazing with anger and distrust, jaw set, speaking sharply; her tired, grimy hands clenched into fists on the glass in front of her; her small steel tag pendant on its chain over her coat; cold white light on her face",
         camera="medium close-up, eye level", amb="detention_room",
         sens="violence", safe="'blood-coloured fingers' and her accusation of slaughter shown only as tired grimy fists and an angry face; no blood, no wounds"),
    dict(to=17, reason="action change: the tablet reveal — CCTV of Brent sitting with top Council officers", chars=["kyle"], loc="detention",
         visual="Kyle seated on the far side of the clear glass table holding a slim glowing digital tablet out towards the viewer in his black-gloved hands, his calm face above it; the bright screen fills much of the frame and shows grainy blue-tinted high-angle security-camera footage of a broad man in a rust-red jacket with shaved sides sitting at a long white-and-gold table with three stern older officers in charcoal-grey high-collared uniforms, leaning in to talk; beside it small glowing bar charts; the room around Kyle is empty, nobody else in the foreground; no letters or numbers anywhere on the screen",
         camera="medium close-up from Aira's point of view across the table, the tablet screen in the centre", amb="detention_room"),
    dict(to=20, reuse="beat_003", reason="return to the face-off: Kyle explains Brent was Marcus's agent", loc="detention",
         visual="(reuse of beat_003)", amb="detention_room",
         sens="violence", safe="the planned bloodshed is only spoken about; the image stays on Kyle's calm face"),
    dict(to=24, reason="action change: the Project Cleanslate file opens as a glowing red map", chars=["kyle", "aira"], loc="detention",
         visual="side view across the clear glass table: Kyle seated on the right side of the table and Aira seated on the left side opposite him, the full width of the table between them; in the middle of the table the tablet projects a glowing holographic cross-section map of the vertical bunker levels, the lowest level glowing an ominous deep red with thin red lines running through its ventilation shafts and every doorway marked by a red light; Kyle reaches one black-gloved fingertip to the map from his side; Aira, lit red, stares at it in growing horror; no letters, numbers or symbols, only lines and glow",
         camera="medium wide profile two-shot, eye level, the red map in the centre, the two faces on either side in the upper third", amb="detention_room",
         sens="violence", safe="the gassing plan is shown only as an abstract glowing red map of the lowest level; no gas, no people"),
    dict(to=26, reason="emotional turning point: Aira's mind freezes at the scale of the betrayal", chars=["aira"], loc="detention",
         visual="close-up of Aira sitting very still, frozen in shock, staring straight ahead at nothing, lips parted, eyes wide and glistening, the last faint red glow fading from one side of her face while cold white light falls on the other; her charcoal hijab fully covering hair and neck",
         camera="close-up, eye level, slight low angle", amb="detention_room"),
    dict(to=30, reuse="beat_003", reason="return to the face-off: 'Then who are you?' and Kyle's long silence", loc="detention",
         visual="(reuse of beat_003)", amb="detention_room"),
    dict(to=32, reason="action change: Kyle stands, opens his collar and holds out a pendant", chars=["kyle", "aira"], loc="detention",
         visual="Kyle now standing on his side of the glass table, the top of his black high collar unbuttoned, holding out at arm's length a small worn steel tag pendant on a thin chain that dangles from his black-gloved fingers, his face sorrowful and open; on the near side Aira, seated, has pulled back slightly with her breath caught, eyes wide in disbelief, one hand at her own identical pendant on her chest; the full width of the glass table keeps a clear arm's-length gap between them",
         camera="medium two-shot from the side of the table, eye level, faces in the upper third, the table top as the lower third", amb="detention_room"),
    dict(to=35, reason="detail: the two identical pendants side by side", chars=["aira", "kyle"], loc="detention",
         visual="extreme close-up framed tightly on two hands only, no faces visible: from the left edge Aira's tired grimy hand in her olive-brown coat sleeve lifts her small worn steel tag pendant on its thin chain; from the right edge Kyle's black-gloved hand in a black uniform sleeve holds up an identical worn steel tag pendant on its chain; a wide empty gap of more than a forearm's length between the two hands, which never touch; each tag bears a faint engraved code too small to read; soft cold light glints on the metal; the glass table top below",
         camera="extreme close-up, shallow depth of field, the pendants in the upper half, the glass table as the lower third", amb="detention_room",
         sens="other", safe="engraving kept unreadable; only the hands are shown, a wide gap apart"),
    dict(to=39, reason="flashback: the two fathers working in secret on the way to the surface", chars=["malik"], loc="memory",
         visual="memory scene: Malik in his dark-blue engineer's jacket bending over the drafting table with a second engineer seen only as a vague soft-focus figure from behind in a dark work jacket, both studying the glowing line blueprints of tunnels and a shaft rising towards a pale circle of light; Malik pointing up the shaft with a hopeful, determined face; warm lamplight, faded edges",
         camera="medium shot, eye level, slightly soft focus", amb="memory", transition="dissolve",
         sens="violence", safe="the murder of the two fathers and the 'raid' are not shown: only the fathers alive and working together in memory"),
    dict(to=41, reuse="beat_004", reason="return to Aira's challenge: 'why do you wear that uniform?'", loc="detention",
         visual="(reuse of beat_004)", amb="detention_room"),
    dict(to=45, reason="action change: Kyle at the glass wall looking out at the city", chars=["kyle"], loc="detention",
         visual="Kyle standing at the tall glass wall of the white room with his back half turned to the camera, hands clasped behind his back, looking out at the distant white towers and glass bridges of the upper-level city glowing under the dark cavern ceiling; his face in three-quarter profile, calm and burdened; his reflection faint in the glass; the pale floor as the lower third",
         camera="medium wide, from behind and to the side of him", amb="detention_room"),
    dict(to=49, reason="action change: Aira, alarmed, asks about Zail; Kyle turns and shakes his head", chars=["aira", "kyle"], loc="detention",
         visual="Aira half-risen from her chair with both hands braced on the glass table, leaning forward with sudden fear and urgent worry in her eyes; across the room by the glass wall Kyle has turned towards her, slowly shaking his head, his face heavy with regret; a wide distance between them",
         camera="medium wide two-shot, eye level, faces in the upper half", amb="detention_room",
         sens="violence", safe="the chaos and shooting where Zail was lost are only spoken about"),
    dict(to=53, reason="emotional turning point: the countdown and Aira's black-and-white world turning grey", chars=["aira"], loc="detention",
         visual="Aira sitting alone at the glass table, head slightly bowed, her face split between cold white light and deep shadow, holding her steel tag pendant between her fingers in thought; the tablet lies on the glass before her showing only a red glowing panel; behind her the dark glass wall with distant city lights; Kyle out of focus far in the background",
         camera="medium close-up, eye level, slight side angle", amb="detention_room",
         sens="other", safe="countdown shown only as a red glowing panel, no digits"),
    dict(to=55, reason="scene change (reflection): Brent rousing the crowd in the Sector 7 warehouse", chars=["brent"], loc="warehouse",
         visual="Brent standing on the raised metal platform of the rusted warehouse, one arm raised high with an open hand, shouting passionately; below him a crowd of young people in worn jackets (the women in hijabs) seen from behind, faces turned up to him in trust; fire barrels glowing orange; the whole image faded like a bitter memory",
         camera="low-angle medium wide shot from inside the crowd, Brent in the upper third", amb="warehouse_crowd", transition="dissolve",
         sens="other", safe="no weapons or violence: only Brent's rousing speech; the sacrificed lives are only spoken about"),
    dict(to=56, reuse="beat_014", reason="return to Kyle at the glass wall: the man sacrificing his life for everyone", loc="detention",
         visual="(reuse of beat_014)", amb="detention_room", transition="dissolve"),
    dict(to=59, reason="symbolic: the real war is between humanity and greed, not upper vs lower", loc="bunker",
         visual="a vast symbolic cross-section of the bunker deep in the earth: the gold-lit luxury upper level at the top, the rusted smoky Sector 7 machinery levels at the bottom, and a wide band of grey haze filling the levels in between where gold light and rust-red light blur together; a single thin shaft of pale daylight falls from the very top down through the whole structure; no people",
         camera="wide vertical establishing shot, the structure filling the frame, dark rock as a calm lower third", amb="memory", transition="dissolve"),
    dict(to=63, reason="action change: back in the room, Kyle leans back in his chair and asks for trust", chars=["kyle", "aira"], loc="detention_dim",
         visual="side view of the glass table: Kyle seated again on the right, leaning back in his chair with a deep tired breath, his collar still open, speaking earnestly; Aira seated on the left, upright and composed, listening with a calm but firm gaze; the tablet lying dark between them; the dark glass wall with distant city lights behind",
         camera="medium wide profile two-shot, eye level, faces in the upper third, the table as the lower third", amb="detention_room", transition="dissolve"),
    dict(to=66, reason="focus change: Aira looks at her tired hands and her despair turns into resolve", chars=["aira"], loc="detention_dim",
         visual="close-up of Aira looking down at her tired, grimy, work-worn hands resting open on the glass table, her steel tag pendant hanging at her chest; her face weary but a firm determination beginning to rise in her eyes; dim cold light",
         camera="medium close-up, slightly high angle, her face in the upper half, her hands on the glass below", amb="detention_room",
         sens="violence", safe="'injured hands' shown as tired grimy hands; no blood, no wounds"),
    dict(to=68, reason="action change: Kyle stands a respectful step away and gives his assurance; trust is born", chars=["aira", "kyle"], loc="detention_dim",
         visual="Kyle standing a respectful step away beside the glass table, slightly bowed towards Aira with an earnest, reassuring face, his hands at his sides; Aira seated, looking up at him, her face exhausted and worried but steady; a clear gap between them; dim cold light and the dark glass wall with distant city lights behind",
         camera="medium two-shot, eye level, faces in the upper half", amb="detention_room",
         sens="intimacy", safe="no touching: Kyle keeps a respectful step away"),
    dict(to=70, reuse="beat_021", reason="return to Aira: her fear turns into strong resolve", loc="detention_dim",
         visual="(reuse of beat_021)", amb="detention_room",
         sens="intimacy", safe="'Kyle places his hand on her shoulder' is not shown: the image stays on Aira alone"),
    dict(to=71, reuse="beat_022", reason="return to Kyle's promise, standing a respectful step away", loc="detention_dim",
         visual="(reuse of beat_022)", amb="detention_room",
         sens="intimacy", safe="no touching: Kyle stands a respectful step away"),
    dict(to=73, reason="scene change: the two of them on the high balcony looking over the dark city", chars=["aira", "kyle"], loc="balcony",
         visual="seen from behind, Aira and Kyle standing at the glass railing of a high balcony an arm's length apart, looking out over the vast dark upper-level city of white towers with sparse cold lights beneath the dark cavern ceiling; Aira's olive-brown coat and charcoal hijab moving slightly in a faint wind, Kyle's black uniform; both still and resolute",
         camera="wide shot from behind, the two figures and the city in the upper two-thirds, the balcony floor as the lower third", amb="upper_balcony",
         transition="black"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With the chill of the cold steel floor, a pitch darkness slowly settled over Aira's eyes. Still echoing in her ears were the gunfire she had heard in Sector 7 and the painful cries of her friends.",
   [("distant_boom", "ބަޑީގެ", -24), ("sob_breath", "ރުއިމުގެ", -24)])
sh(2, "With the sharp pain spreading through different parts of her body, she slowly opened her eyelids. The first thing she saw was the neon lights fixed in the ceiling above.",
   [("breath", "ތަޅުވާލިއެވެ", -22)])
sh(3, "They were completely different from the dim, faded lights of the lower levels — a cold, clean white light.")
sh(4, "What reached her nose was the cold smell of sterilised chemicals and air-conditioning. The smoke of Sector 7, the stench of rubbish,")
sh(5, "and the smell of gunpowder had vanished completely. Aira tried to get up. She thought heavy iron chains would be locked on her hands and feet. But")
sh(6, "she could move both hands without any obstacle. She was sitting on a soft chair. In front of her was a glass table.",
   [("cloth_rustle", "ހަރަކާތްކޮށްލެވުނެވެ", -22)])
sh(7, "This was no ordinary prison cell; it was a modern detention room inside the most secret building of the upper level.")
sh(8, "The walls were sealed with steel panels so that no sound from outside could get in. Aira was instantly alert and brought her body into a defensive stance.",
   [("breath_heavy", "ސަމާލުވެ", -22)])
sh(9, "Her blood-coloured fingers clenched into fists. Sitting on the other side of the table was Security Chief Commander Kyle.")
sh(10, "There was not a single crease in his black commander's uniform. The silver medals pinned on his chest gleamed in the cold light.")
sh(11, "Kyle's eyes were fixed on Aira. The cruel, contemptuous look she had seen on his face in Sector 7 was gone now.")
sh(12, "Instead there was a deep calm that was hard to describe. \"Are you trying to kill me?\"")
sh(13, "Aira's voice came out like a poisoned arrow. Her eyes showed hatred and anger. \"After slaughtering everyone in Sector 7,")
sh(14, "did you bring me here to complete the pleasure of your cruelty?\" Kyle said nothing. He slowly placed both hands on the table.",
   [("cloth_rustle", "ބާއްވާލިއެވެ", -24)])
sh(15, "Then he took a digital tablet from his pocket and showed it to Aira. As the tablet's screen lit up, it began to show secret security-camera videos and bank transfer records.",
   [("computer_beep", "ދިއްލިގެން", -20)])
sh(16, "Those videos showed Brent. Although Aira already knew that Brent was a traitor,")
sh(17, "the truth these records revealed was far more terrifying. Brent was sitting at the same table with the Council's most senior officers.")
sh(18, "\"Do you know how deep the real reason for Brent's betrayal goes?\" Kyle's voice was soft, but the weight in it chilled her heart more than the cold of the room.")
sh(19, "\"He isn't just a man who sold out for money. He is the man who, on Marcus's direct orders, stirred up unrest in Sector 7")
sh(20, "and had them plan this attack. Marcus wanted to carry out a great bloodbath of Sector 7's young people sent up above.\"")
sh(21, "As Kyle touched the screen, a secret file named 'Project Cleanslate' opened.",
   [("computer_beep", "ޖައްސާލުމާއެކު", -20)])
sh(22, "\"This is Marcus's real plan,\" Kyle explained. \"To show the people of the lower levels to the upper-level public as dangerous terrorists threatening the main city, and to create fear.")
sh(23, "Then, by running 'Project Cleanslate', sealing every door of Sector 7 at once,")
sh(24, "and sending in poison gas to kill all of you at once — he would have the full consent of the upper level's ordinary citizens.")
sh(25, "Brent is the pawn Marcus used to pave the way for that great massacre.\" Aira's whole mind seemed to freeze.",
   [("heartbeat", "ގަނޑުވި", -22)], hum=True)
sh(26, "She had never imagined that Brent's treachery reached this far, or that the upper level had devised such a merciless plan to tear their whole lives apart.")
sh(27, "Aira raised her head and looked into Kyle's eyes. But the questions and doubts in her heart still would not stop. \"Then... who are you?\"")
sh(28, "Aira's voice trembled. \"Aren't you Marcus's highest man — the chief of his cruel soldiers?")
sh(29, "What is the purpose of bringing me here and telling me all this?\" With Aira's hard questions, a deep silence fell over the whole room.")
sh(30, "For a while Kyle sat without a word, watching Aira's face. His eyes showed the trace of a heavy grief he had kept hidden in the depths of his heart for years.")
sh(31, "Slowly rising from the chair, Kyle undid the buttons at the collar of his black commander's uniform.",
   [("cloth_rustle", "ނައްޓާލިއެވެ", -22)])
sh(32, "Then he drew out a pendant hanging round his neck and showed it to Aira. Aira felt as if her breath had caught in her throat. It was an exactly identical,",
   [("gasp", "ތާށިވި", -20)], hum=True)
sh(33, "old, worn steel pendant. The pendant round Aira's neck and the one round Kyle's — their design and the faded mark on them were exactly the same.")
sh(34, "It was a childhood token recalling the close bond between their families. \"This... how is this possible?\"")
sh(35, "Aira's voice trembled. \"Why is that pendant round your neck?\" \"My father too was an engineer who worked with your father building the bunker,\" Kyle's voice this time came out with deep pain.")
sh(36, "\"They were killed when Marcus learned the secret of this bunker. Our fathers had begun working to free everyone from this wretched slavery,",
   hum=True)
sh(37, "and to clear the way to take people up to the real surface of the world, into the light of the sun.\" Aira gripped the table hard with both hands.")
sh(38, "Some childhood memories, faint as they were, began to swirl in her mind: the stories her father told, and the other engineer he always met in secret.")
sh(39, "All those days Aira had believed her father was killed in an ordinary soldiers' raid. But the truth was that it was a great crime carried out on Marcus's direct plan.",
   hum=True)
sh(40, "\"Then why do you stand there in that uniform, as the chief of Marcus's top soldiers?\" The question that rose in Aira's heart burst out again.")
sh(41, "\"Why, serving under them, did you allow such great cruelty in Sector 7?\" Kyle let out a deep breath.",
   [("sigh", "ދޫކޮށްލިއެވެ", -20)])
sh(42, "He looked out through the room's glass wall at the tall buildings of the city in the distance. \"Because Marcus's system can only be torn apart from inside it,\"")
sh(43, "Kyle said calmly. \"I don't wear this uniform just for revenge...")
sh(44, "but to make the dream our fathers dreamed come true. To take everyone up to the surface. I was harsh in Sector 7")
sh(45, "because Marcus's spies were watching my every move. At that moment the only way to save you was to arrest you as a 'valuable prisoner' and bring you here.\"")
sh(46, "Just then the memory of Zail came back to Aira, and a wave of fear ran through her body. \"Zail... where is Zail?",
   [("heartbeat", "ބިރުވެރިކަމުގެ", -22)])
sh(47, "What happened to him?\" Aira's voice was full of extreme worry. Kyle's face showed despair. He slowly shook his head.")
sh(48, "\"In the great chaos and the shooting in Sector 7, I don't know where Zail went or what happened to him either.")
sh(49, "In that chaos the only one I could save was you. But if he is alive, there is still time...")
sh(50, "only a few hours are left on the countdown to Marcus's 'Project Cleanslate'.\" The cold, heavy silence in the room left Aira short of breath.",
   [("breath_heavy", "ހާސްކުރުވަމުން", -22)])
sh(51, "The records on the tablet, the pendant round Kyle's neck and the truths he had revealed shook Aira's whole way of thinking.")
sh(52, "She had lived most of her life by a simple, clear philosophy: in Sector 7 of the lower levels there were only suffering")
sh(53, "innocents; on the upper level only tyrannical, bloodthirsty oppressors. But now, behind this curtain, she saw a far more tangled world — not black and white, but grey.")
sh(54, "Brent was a man born in the slums of Sector 7. Everyone trusted the fire in his voice and the promises he made.")
sh(55, "But he sold himself for his own desires. He sacrificed hundreds of lives out of greed for a comfortable life on the upper level. On the other hand,")
sh(56, "Kyle, standing here in the Council's most senior and fearsome uniform, is a man risking his life to stop the cruelty of the whole system and take everyone up to the surface.")
sh(57, "A deep truth dawned on Aira. The upper level was not full only of oppressors. And Sector 7 was not full only of innocents.",
   hum=True)
sh(58, "The real war was not a war between the upper and lower levels; nor was it a struggle between the poor and the rich.")
sh(59, "It was a dark war between humanity and selfish greed. \"Why did you bring me here?\"")
sh(60, "Aira asked in a calm but firm voice. \"What is the real purpose of telling me all this?\"")
sh(61, "Kyle let out a deep breath and leaned back in his chair. \"I wanted to reveal the truth to you. To make you feel how vast the darkness we are about to face is.",
   [("sigh", "ދޫކޮށްލަމުން", -20), ("cloth_rustle", "ލެނގިލިއެވެ", -24)])
sh(62, "After what happened in Sector 7, we now have only one chance.")
sh(63, "If the two of us don't trust each other, the dream our fathers dreamed and the lives of thousands will be lost forever.\"")
sh(64, "Aira looked at her wounded hands. Though her body ached, the fire of despair burning in her heart turned into firm resolve.")
sh(65, "The honesty in Kyle's eyes and the memories of the identical pendants round their necks gave rise to new courage in her heart.",
   hum=True)
sh(66, "Aira raised her head and met Kyle's eyes. Her face showed an unflinching steadiness.")
sh(67, "In the dim light, Aira's face showed extreme exhaustion and worry. But as Kyle came closer to her,",
   [("footsteps_pavement", "ޖެހިލައި", -24)])
sh(68, "the assurance he gave laid the foundation of a new trust between them. Every second counting down to Marcus's dangerous 'Project Cleanslate' became a moment that made them hold their breath.")
sh(69, "As time ran short, the tension in the air grew stronger. Although not knowing what had become of Zail still worried Aira,")
sh(70, "the fear in her heart turned into strong resolve. Gently placing a hand on Aira's shoulder, Kyle said:")
sh(71, "\"As long as I'm here I won't let any harm come to you. But the war ahead is one that will change our whole lives.",
   hum=True)
sh(72, "Get ready.\" Standing on the balcony of the tall building, the two of them looked down together into the cold pitch darkness of the city below.",
   [("wind_gust", "ބެލްކަނީގައި", -22)])
sh(73, "They knew: this was not just a struggle to survive. This was the last, and most dangerous, war they had to face to tear apart Marcus's dark plans.",
   hum=True)
SHOTS = S

"""Beat/shot plan for Marufas episode 510 (used by plan_beats.py)."""

ROOM = ("Yamna's spacious bedroom in the family's large modern island house: white walls, polished white marble floor, "
        "a big bed with white sheets and a pale headboard, a study desk with books and pens under the window, a tall "
        "dark-wood wardrobe, a glass sliding window beside the bed with a sheer white curtain, a round ceiling light")
LIVING = ("the large formal living room (beyrugey): a royal-style cream sofa set with big gold-trimmed cushions, an "
          "Italian marble centre table with crystal vases and ornaments, a soft velvet rug, a big wall-mounted TV with a "
          "dark black screen, a glass display showcase, marble floor")
CORRIDOR = ("the wide corridor leading off the large living room to the bedrooms of the modern island house: white "
            "walls, polished white marble floor, closed dark-wood bedroom doors with round brass handles, a single "
            "small wall lamp")

LOC = {
    "yamna_room": ROOM,
    "yamna_room_sleep": ROOM,
    "yamna_room_day": ROOM,
    "yamna_room_dark": ROOM,
    "living": LIVING,
    "living_3am": LIVING,
    "corridor": CORRIDOR,
    "house_ext": ("the family's large white modern two-storey house on a small Maldivian island, behind a coral-stone "
                  "boundary wall with flowering trees, seen from the white sandy lane with palms and breadfruit trees "
                  "and a dim street lamp"),
    "dining": ("the dining area at the edge of the large modern kitchen: a long dark-wood dining table, carved dark-wood "
               "cabinets and a long countertop with a coffee machine behind, a big double-door steel fridge, a window "
               "with daylight"),
}
MOOD = {
    "yamna_room": "night about a month after the last episode, a dim warm bedside lamp against cold blue-grey shadows, a faint haze, hushed and uneasy",
    "yamna_room_sleep": "about 4 am, one soft warm bedside lamp in a quiet blue-dark room, the haze gone, an eerie stillness that the family mistakes for peace",
    "yamna_room_day": "morning, pale grey-white daylight through the sheer curtain, desaturated and lifeless, a heavy silence",
    "yamna_room_dark": "daytime with the curtains drawn, the ceiling bulb dead, the room in cold blue-grey gloom with a dusty grey shaft of light at the curtain edge, oppressive and grim",
    "living": "night, dim warm amber lamplight in the big living room, deep smoky shadows, a tense hushed atmosphere",
    "living_3am": "3 am, an eerie unnatural cold, a cold blue haze filling the living room, one warm table lamp, anxious waiting",
    "corridor": "3 am, the corridor in cold blue darkness with a thin mist over the marble floor, one small warm wall lamp, ominous",
    "house_ext": "late night before dawn, faint misty moonlight, cold blue-grey haze, dark palms, one dim warm street lamp, ominous stillness",
    "dining": "midday, warm soft daylight from the window, a homely calm with a faint undercurrent of unease",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
YB = "Yamna lying in her bed under a white blanket up to her chest, her white hijab fully covering her hair and neck, her long lilac sleeves covering her arms"
HAG = "pale, tired, with dark circles under her eyes"

BEATS = [
    dict(to=4, reason="episode opening: a month of Ghassan's nightly recitations with the parents watching",
         chars=["ghassan", "yamna", "saahidha", "khalid"], loc="yamna_room",
         visual=f"{YB}, eyes closed, {HAG}; Ghassan sitting on a chair at the head of the bed, his open palm raised a hand's width ABOVE her forehead without touching her, lips murmuring a recitation; on the bedside table a few folded plain white cloths and a plain dark clay bowl of water; Saahidha and Khalid standing together at the foot of the bed watching him with hopeful, trusting, exhausted faces",
         camera=f"medium wide shot from the side of the bed, eye level, {LOW} (the bedsheet edge and marble floor in shadow)",
         amb="haunted_room", sens="other",
         safe="recitation per bible rule 7: palm hovering above, never touching; both parents in frame; his 'sorcery items' are only plain white cloths and a plain clay bowl, no symbols or letters"),
    dict(to=6, reason="action/place change: in the living room Ghassan announces the final, most dangerous stage",
         chars=["ghassan", "khalid", "saahidha", "faarish"], loc="living",
         visual="Ghassan standing beside the marble centre table with his black leather bag on his shoulder, one hand raised in a grave warning gesture, speaking with a solemn, authoritative face; Khalid, Saahidha and Faarish sitting on the cream sofas looking up at him with worried, attentive faces; beside Faarish a young man with curly hair and a goatee in an olive-green shirt also listening",
         camera=f"medium wide shot, eye level, {LOW} (velvet rug in shadow)", amb="living_night"),
    dict(to=8, reason="framing change: the desperate parents nod and give him their full trust",
         chars=["khalid", "saahidha"], loc="living",
         visual="close two-shot of Khalid and Saahidha sitting side by side on the cream sofa, nodding slowly with desperate, trusting, tear-tired eyes, Saahidha's hands clasped in her lap, Khalid leaning forward; Ghassan's white-shirted shoulder blurred and out of focus in the near foreground",
         camera=f"medium close-up, eye level, {LOW} (sofa cushions in shadow)", amb="living_night"),
    dict(to=10, reason="time jump to 3 am: Ghassan walks down the cold corridor with his bag to the bedroom door",
         chars=["ghassan"], loc="corridor",
         visual="Ghassan seen from behind and slightly to the side walking with heavy deliberate steps down the dim corridor towards a closed dark-wood bedroom door at the far end, his big black leather bag on his shoulder; cold mist drifting low over the marble floor; the door is closed and nothing inside any room is visible; nobody else in the corridor",
         camera="medium wide shot from behind down the corridor, eye level, the figure and the door in the upper two-thirds, the misty marble floor as the calm lower third",
         amb="home_night", transition="black", sens="other",
         safe="bible rule 2: Ghassan is never shown inside the room or alone with Yamna; only his back in the corridor approaching a closed door"),
    dict(to=12, reason="character/place change: the family waits on the living-room sofas at 3 am",
         chars=["khalid", "saahidha", "faarish", "adheel"], loc="living_3am",
         visual="Khalid, Saahidha, Faarish and Adheel sitting on the cream sofas in the dim cold living room at 3 am, all turned towards the dark corridor, tense and anxious; Saahidha with her hands clasped tightly at her chest, Khalid with his chin resting on his hand, Faarish leaning forward with his elbows on his knees, Adheel sitting still beside him; cold blue haze around them",
         camera=f"medium wide shot, eye level, {LOW} (velvet rug and marble floor in shadow)", amb="living_night"),
    dict(to=15, reason="emotional turning point: the silence breaks with Yamna's own voice crying behind the locked door",
         loc="corridor",
         visual="the closed, locked dark-wood bedroom door at the end of the dim corridor seen from a distance, its round brass handle catching a glint, a thin line of cold bluish light under the door, cold mist creeping out under it across the marble floor; the corridor is empty",
         camera="static wide shot down the corridor, eye level, the door in the upper two-thirds, the misty marble floor as the calm lower third",
         amb="haunted_room", sens="other",
         safe="Yamna's cries are heard only; the image shows the locked door from outside, nothing of the room"),
    dict(to=18, reason="framing change: the family's anguish as they listen, believing it is her battle with the jinn",
         chars=["saahidha", "khalid"], loc="living_3am",
         visual="close shot of Saahidha on the sofa pressing both hands over her mouth, eyes squeezed shut, tears on her cheeks; Khalid beside her bent forward with his head bowed and his hands clasped against his forehead, praying; cold blue haze and one warm lamp behind them",
         camera=f"medium close-up, eye level, {LOW} (sofa and rug in shadow)", amb="living_night"),
    dict(to=21, reason="action change: an hour later Ghassan comes out of the room, drenched in sweat, panting, and reassures them",
         chars=["ghassan", "khalid", "saahidha", "faarish"], loc="corridor",
         visual="Ghassan standing in the dim corridor just in front of the closed bedroom door, which he has already pulled shut behind him, his white shirt damp with sweat, beads of sweat on his forehead, breathing hard, his black bag on his shoulder, wearing a tired but sly, reassuring expression and raising one calming hand; Khalid, Saahidha and Faarish standing a few steps away in the foreground, seen partly from behind, anxious and eager to believe him",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)", amb="home_night", sens="other",
         safe="the red mark on his cheek is skipped entirely; the door behind him is closed, nothing of the room is shown"),
    dict(to=23, reason="symbolic detail: the black sorcery in Ghassan's bag growing stronger over the relieved family",
         loc="corridor",
         visual="close-up of Ghassan's large black leather shoulder bag resting on a small side chair in the dim corridor, its flap slightly open, a thin wisp of dark grey smoke curling up out of it into the cold air; beside it on a small table a plain dark clay bowl and a few folded plain white cloths; no people",
         camera="close-up, slightly low angle, the bag and the curling smoke in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="home_night", sens="other", safe="sorcery only as a plain bag and a wisp of smoke, no symbols or letters"),
    dict(to=25, reason="back to Ghassan in the corridor as he reassures them and goes to his own room", reuse="beat_008",
         chars=["ghassan", "khalid", "saahidha", "faarish"], loc="corridor", visual="reuse of beat_008", amb="home_night"),
    dict(to=30, reason="action/place change: the parents open the door and find Yamna sleeping peacefully",
         chars=["yamna", "saahidha", "khalid", "faarish"], loc="yamna_room_sleep",
         visual=f"{YB}, sleeping peacefully on her back, her hijab neat and tidy, her calm innocent face turned slightly up, eyes gently closed, cheeks faintly glistening, no marks of any kind; Saahidha standing at the bedside with one hand over her heart and happy tears in her eyes; Khalid standing beside her at the foot of the bed letting out a breath of relief; Faarish in the open doorway behind them",
         camera=f"medium wide shot from the side of the bed, eye level, {LOW} (the white blanket edge and marble floor in soft shadow)",
         amb="room_night", sens="other",
         safe="bible rule 2: Yamna is shown asleep peacefully only with her parents and brother in frame; dried tears as a faint glisten, calm face, no marks"),
    dict(to=32, reason="action change: Khalid sends Faarish and Adheel to the mosque for fajr and goes to rest",
         chars=["khalid", "faarish", "adheel", "saahidha"], loc="corridor",
         visual="the corridor in soft lamplight: Khalid smiling gently and patting Faarish on the shoulder; Faarish and Adheel wearing white skullcaps, ready to leave for the mosque; Saahidha standing beside Khalid with a calm relieved face; the bedroom door behind them closed",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)", amb="home_night"),
    dict(to=33, reason="place change / symbolic: the 'peace' is really the black darkness of sorcery over the house",
         loc="house_ext",
         visual="the big white house seen from the dark sandy lane before dawn: every window dark except one faint cold bluish glow behind a curtained window, a low cold mist hanging around the house, palms dark against the sky",
         camera="wide shot from the lane, eye level, the house in the upper two-thirds, the dark sandy lane as the calm lower third",
         amb="island_house_night", transition="dissolve"),
    dict(to=35, reason="time jump to the next morning: Yamna isolated, silent and mute",
         chars=["yamna"], loc="yamna_room_day",
         visual=f"Yamna in her lilac dress and white hijab fully covering her hair and neck, sitting alone and very still on the edge of her neatly made bed, {HAG}, staring blankly at the floor, hands limp in her lap; an untouched cup of tea on the study desk; pale morning light through the sheer curtain",
         camera=f"medium wide shot, eye level, {LOW} (marble floor in shadow)", amb="room_day", transition="black"),
    dict(to=38, reason="framing change: the inner truth — she is a silent prisoner who longs to call her mother",
         chars=["yamna"], loc="yamna_room_day",
         visual=f"close-up of Yamna's face in her white hijab, {HAG}, her lips pressed closed and still, her face calm and expressionless, but her large dark eyes glistening and pleading, as if trying desperately to speak without being able to",
         camera=f"close-up, eye level, {LOW} (her lilac shoulder in shadow)", amb="room_day", sens="other",
         safe="the narrator's account of the ifreet's captivity is shown only as her still, silent face"),
    dict(to=42, reason="character enters: her mother sits beside her and caresses her; Yamna cannot respond",
         chars=["saahidha", "yamna"], loc="yamna_room_day",
         visual=f"Saahidha sitting beside Yamna on the edge of the bed, gently stroking Yamna's hand and looking at her with tender, worried love; Yamna in her lilac dress and white hijab sitting stiff and motionless, {HAG}, staring straight ahead, unable to turn towards her mother",
         camera=f"medium shot, eye level, {LOW} (bedsheet and floor in shadow)", amb="room_day"),
    dict(to=46, reason="emotional turning point: her silent tears — she cannot tell her mother what is happening",
         chars=["yamna", "saahidha"], loc="yamna_room_day",
         visual=f"close-up of Yamna's calm, still face in her white hijab, {HAG}, a single clear tear rolling silently down her cheek, her lips closed, eyes lowered; Saahidha's hand resting gently on Yamna's lilac sleeve at the edge of the frame; soft grey light",
         camera=f"close-up, eye level, {LOW} (soft shadow)", amb="room_day", sens="other",
         safe="bible rule 2: the implied abuse is never shown or suggested; only her calm face with a silent tear, no marks, her mother's hand beside her"),
    dict(to=48, reason="time/state change: 'the other days' — the maarid in control, the room turns dark and grim",
         chars=["yamna"], loc="yamna_room_dark",
         visual="the dim bedroom with the curtains drawn and the ceiling bulb dead: Yamna only as a small dim silhouette sitting up on the far side of the bed in the dark, her face hidden in deep shadow, her lilac dress and white hijab barely visible; the sheer curtain lifting into the room although there is no wind; crumpled bedsheets; a cold blue haze",
         camera="wide shot from the doorway, eye level, the silhouette and curtain in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="haunted_room", transition="black", sens="other",
         safe="bible rule 1: the foul words and wildness are shown only as a dim silhouette with her face in shadow, a dead bulb and a lifting curtain"),
    dict(to=51, reason="character change: the parents' grief at the doorway, unable to go near her",
         chars=["saahidha", "khalid"], loc="yamna_room_dark",
         visual="Saahidha and Khalid standing just inside the open bedroom doorway, unable to step closer: Saahidha with both hands pressed over her mouth, tears streaming, her eyes full of anguish; Khalid gripping the door frame, his face crumpled with helpless grief, staring towards the dark far side of the room which is lost in deep shadow",
         camera=f"medium shot from inside the room towards the doorway, eye level, {LOW} (dark marble floor)",
         amb="haunted_room", sens="violence",
         safe="bible rule 1: her self-harm is never shown; only the parents' grief at the doorway and a dark room"),
    dict(to=54, reason="framing change: the neglected room and the stench — what she eats on those days is never shown",
         chars=["saahidha"], loc="yamna_room_dark",
         visual="the neglected bedroom in grey gloom: crumpled bedsheets half on the floor, crumpled paper wrappers and scattered torn pages on the marble floor, an untouched plate of food on the desk, dust in the grey light at the edge of the drawn curtain; Saahidha standing in the doorway holding the end of her beige hijab over her nose and mouth, her eyes wet with grief; nobody else visible",
         camera=f"medium wide shot, eye level, {LOW} (dim floor in soft shadow)", amb="haunted_room", sens="other",
         safe="bible rule 1: the eating of rubbish and insects and her unwashed state are never shown; only the neglected room and the mother's grief"),
    dict(to=56, reason="symbolic turning point: the sea maarid that even Ghassan's ifreet cannot overpower",
         loc="yamna_room_dark",
         visual="the dark empty bedroom wall above the crumpled empty bed: two huge masses of black smoky shadow with long shadowy fingers swirling and pressing against each other across the white wall, faceless, the ceiling light flickering faintly, cold blue haze; no people",
         camera="wide shot, slightly low angle, the shadows on the wall in the upper two-thirds, the dark bed edge and floor as the calm lower third",
         amb="haunted_room", sens="other",
         safe="bible rule 14: the maarid and the ifreet only as faceless smoke and shadow on the wall (one of the episode's shadow uses)"),
    dict(to=59, reason="character change: Ghassan's true purpose — his sly face in the corridor at night",
         chars=["ghassan"], loc="corridor",
         visual="Ghassan standing alone in the dim corridor at night, a few steps from a closed bedroom door, his black bag on his shoulder, his face lit from one side by the small warm wall lamp, a faint sheen of sweat on his brow, a thin sly smile and cold calculating narrowed eyes looking off to the side; the door stays closed",
         camera=f"medium close-up, eye level, {LOW} (dark corridor wall and floor)", amb="home_night",
         transition="dissolve", sens="other",
         safe="bible rule 2: his intent is shown only as his sly face in the corridor; never inside the room, never with Yamna"),
    dict(to=63, reason="time jump to noon and place change: lunch after the dhuhr prayer, fried fish on the table",
         chars=["khalid", "saahidha", "ghassan"], loc="dining",
         visual="the long dark-wood dining table at noon: a large platter of golden fried fish, a pot of rice and plates; Khalid wearing a white skullcap sitting at the head of the table, breaking a piece off the fried fish with his fingers while talking animatedly; Saahidha sitting across from him leaning forward with eager interest; Ghassan sitting at the side of the table eating and listening",
         camera=f"medium wide shot, eye level, {LOW} (the table top in soft shadow)", amb="home_day", transition="black"),
    dict(to=65, reason="emotional turning point: Khalid looks at Ghassan for permission for Saeed to sit in",
         chars=["ghassan", "khalid"], loc="dining",
         visual="Ghassan in the foreground at the dining table, his hand stopped above his plate, his face stiffening into a cold, guarded expression, eyes narrowed; behind him and slightly out of focus Khalid in his white skullcap looking at him hopefully, as if asking for his permission",
         camera=f"medium close-up, eye level, {LOW} (table top with the plate)", amb="home_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Ghassan carried on with the recitations, night after night.",
   [("whisper_recite", "ކިޔެވެލިތައް", -23)])
sh(2, "Though he kept giving Yamna white cloths drawn with strange letters, and bowls of water blown on with the filthy words of sorcery to drink, no hoped-for change came over her condition.",
   [("pour", "ފެންތަށިތައް", -24)])
sh(3, "But Ghassan was no ordinary fraud. Making out that what afflicted Yamna was an extremely powerful sorcery,")
sh(4, "with tales of lies and delusion he had, over the past month or so, won the complete trust of that innocent family.")
sh(5, "After some days Ghassan's methods and plans began to change. \"Now this is the final and most dangerous stage; the jinn is showing its very last strength.")
sh(6, "When the family is inside the room, it calls on outside help and grows stronger. So tonight I want to go into the room alone and recite.\"")
sh(7, "Ghassan caught Yamna's family in his snare with cunning planning. To that helpless family, who had run out of ways to save their child from that death-trap, Ghassan gave not the slightest chance to perceive the black intent and dangerous plans behind him.")
sh(8, "Ready to do anything at all if only their child would be saved, they nodded in trust.", hum=True)
sh(9, "And that was also how the way was opened for Ghassan to enter the room alone. At three o'clock in the dead of night,")
sh(10, "an eerie cold had taken over the whole atmosphere. Carrying his secret black bag, with heavy steps, Ghassan went into Yamna's room and locked the door from inside.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކަށް", -22), ("lock_click", "ތަޅުލިއެވެ", -18)])
sh(11, "Then, anxious about what would happen next and counting the moments as they waited, the innocent girl's family sat on the sofas in the living room.")
sh(12, "Their hearts pounded for the terrible sound that might come from the room next. Once the door shut, first came a few terrifying minutes of deathly silence.",
   [("heartbeat", "ތެޅެމުންދިޔައީ", -20)])
sh(13, "But that silence was shattered, the whole air ringing with Yamna's loud scream. Unlike on other nights,",
   [("gasp", "ހަޅޭކުގެ", -20)])
sh(14, "tonight what came out of that room was not the jinn's heavy voice. It was Yamna's very own soft, innocent voice.")
sh(15, "In that voice was a painful cry that could crush a heart. \"Don't do this! Please... Mother! Father! Save me!\"", hum=True)
sh(16, "With the sound of painful sobbing, those heart-rending, pleading cries were tearing apart the hearts of the family members outside.",
   [("sob_breath", "ރުއިމުގެ", -24)], hum=True)
sh(17, "But they believed it was Yamna's battle to free herself from the spiritual force.")
sh(18, "After a terrible hour full of tears and pain had passed like this, the sounds in the room slowly fell silent. A little while later,")
sh(19, "the door of the room opened and Ghassan came out. He was drenched in sweat from head to foot, breathing fast and exhausted.",
   [("door_open", "ހުޅުވާލާފައި", -20), ("breath_heavy", "ނޭވާ", -20)])
sh(20, "A red mark stood out on his cheek. \"Tonight, because I was alone, it fought very hard...")
sh(21, "but from now on it will get lighter night after night,\" said Ghassan, hiding his evil intent and giving the family a deceitful hope that calmed their hearts.")
sh(22, "Hearing Yamna's own normal voice instead of the terrifying jinn's voice of other nights, the helpless family took it for the beginning of her healing.")
sh(23, "As their hearts breathed a sigh of relief, the black knots of sorcery inside Ghassan's bag were growing ever stronger over them.", hum=True)
sh(24, "Ghassan went off to his room next door, giving that helpless family great reassurance")
sh(25, "and the certainty that nothing would trouble Yamna any more tonight. But after the painful sounds heard over the past hour,")
sh(26, "everyone badly wanted to see Yamna with their own eyes before going to sleep. Hearts pounding with worry, Khalid opened the bedroom door, stepped in, and let out a breath of relief.",
   [("door_open", "ހުޅުވާލައި", -20), ("sigh", "ދޫކޮށްލިއެވެ", -22)])
sh(27, "Yamna lay on her back on the bed, sleeping calmly and deeply. The tears that had fallen from her eyes had dried on her cheeks.")
sh(28, "From her neck down, a white blanket like a soft shroud lay neatly spread over her.")
sh(29, "Instead of the frightening look her face usually wore on recitation nights, her face showed an unusual, innocent stillness.")
sh(30, "Her hair, too, had been neatly arranged. Seeing that sight, tears of joy fell from Saahidha's eyes.")
sh(31, "\"Now we'll sleep after praying fajr. Son, take Aadhil with you to the mosque too.\" Giving the precious advice he always gave his children, Khalid gently patted Faarish on the shoulder.")
sh(32, "Then, putting his arm round Saahidha's shoulder, he headed towards their room, his heart filled with a deep peace he had not felt in many months.")
sh(33, "As their hearts filled with gratitude to Ghassan, the poor parents did not realise in the least that this calm sleep was a black darkness, given after Ghassan's sorcery had knocked Yamna's body senseless.")
sh(34, "Even when the sun rose on a new day, what showed in Yamna was the same unusual isolation and deathly quietness seen in her on certain other days.")
sh(35, "On such days she does not speak properly with anyone in the house. All the time she sits silent and mute.")
sh(36, "But the terrifying truth behind that outward calm, which the family does not realise at all,")
sh(37, "is that on such days Yamna's whole being is held captive by a wicked ifreet under Ghassan's evil command. To move her tongue")
sh(38, "and call out \"Mother!\" is what the innocent girl wants with all the depth of her heart. But the power of that tongue has been completely taken from her.", hum=True)
sh(39, "She strains until her chest tightens to bring out even a tiny voice from her throat, asking for help.",
   [("breath", "ފިތޭވަރަށް", -24)])
sh(40, "But the dangerous power of the evil sorcery Ghassan has let loose on her body has wiped out every ability to make that sound.")
sh(41, "Though the poor girl is bathed in the caresses and love, full of compassion, of the mother sitting beside her,")
sh(42, "her captive body has no freedom at all to lay her head on her mother's chest and draw close.")
sh(43, "Under Ghassan's merciless hold, her heart weeps and begs to tell her mother the story of the tears of blood as her honour is robbed every night.", hum=True)
sh(44, "Though she wanted to tell her family those painful complaints and beg them to save her from that filthy sorcerer,")
sh(45, "her own body has betrayed her and turned into a silent prison. The silent tears flowing from Yamna's eyes say that in her own home, in front of her own parents,", hum=True)
sh(46, "she is living like someone wrapped in a shroud while still alive. On the other days, Yamna is a completely different,")
sh(47, "strange creature. On such days she shows wickedness of the most extreme degree and a harsh, frightening terror.")
sh(48, "From her tongue come filthy words that deafen the ears, unbearable to hear, and vile screams. On such days,",
   [("low_growl", "ގޮވުންތަކެވެ", -21)])
sh(49, "in front of her loving family, she does much harm to that poor body herself. Biting herself, clawing her skin with her nails,")
sh(50, "banging her head against the bed's headboard and the wall, while the parents watching the sight have their hearts break into pieces.", hum=True)
sh(51, "They are unable to save Yamna from that harm because, in such moments, the unnatural powers the girl possesses")
sh(52, "let no one come near her. And the most painful thing is that on such days, what she eats is not the kind of thing human beings eat.")
sh(53, "She eats rubbish, and live cockroaches found in the room, which she gulps into her mouth. There is no bathing, no cleansing.")
sh(54, "From her body comes a foul smell that sickens anyone who comes near. That smell is closest to the stench of the reef drying out at low tide. But,")
sh(55, "the terrifying truth that no one in that house knows is that the evil devil holding the girl's body captive on such days cannot be subdued, not even for a moment, by Ghassan's powerful sorcery.")
sh(56, "Even the powerful ifreet in Ghassan's service has, on those days, failed to overpower the maarid riding that body.", hum=True)
sh(57, "Though Ghassan tries to show off his mastery in front of Yamna's family, on such nights he goes into the room not to tie more knots of sorcery.")
sh(58, "Instead, he works to increase the strength of the ifreet under his command, which Ghassan makes fight that evil maarid,")
sh(59, "so as to gain the power to imprison Yamna's whole body under his control and do with her as he pleases.", hum=True)
sh(60, "After the noon prayer, Khalid came home with Ghassan to have lunch. \"Today, as I was coming out of the shop,",
   [("door_open", "ގެޔަށް", -22)])
sh(61, "I happened to meet Saeed!\" Khalid said, breaking off a piece of the big fried fish. \"Really? What did he say?\"",
   [("cup_clatter", "ނައްޓާލަމުން", -24)])
sh(62, "Saahidha asked eagerly. \"He asked how kamana is doing. He also asked whether she is getting even a little better.")
sh(63, "I told him that with Ghassan's help she is slowly improving,\" Khalid went on.")
sh(64, "\"And he said that since he too wants to learn shar'i ruqyah, he would like to sit in and watch on the nights the recitation is done with him.\"")
sh(65, "Saying this, Khalid looked at Ghassan's face, as if asking for his permission. (To be continued)", hum=True)
SHOTS = S

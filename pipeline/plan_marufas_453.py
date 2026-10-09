"""Beat/shot plan for Marufas episode 453 (used by plan_beats.py)."""

HOUSE_EXT = ("the family's large modern two-storey island house seen from its sandy front yard: white walls, a front "
             "veranda (fendaa) with a big wooden swing bench (undhoali), potted plants, flowering trees by the boundary "
             "wall, tall palms and breadfruit trees behind")
CORRIDOR = ("the long inner corridor of the family's large modern island house: polished white marble floor, white "
            "walls, tall dark-wood bedroom doors along one side, a round ceiling light, the living room and the kitchen "
            "at the far end")
YAMNA_ROOM = ("Yamna's spacious bedroom in the family's large modern island house: white walls, polished white marble "
              "floor, a big bed with white sheets and a pale headboard, a study desk with books and pens under the "
              "window, a tall dark-wood wardrobe, a glass sliding window beside the bed with a sheer white curtain, a "
              "round ceiling light")
PARENTS_ROOM = ("the parents' bedroom: dark-wood bed with cream bedding, a bedside lamp, a framed abstract picture, "
                "heavy curtains")
LIVING = ("the large formal living room (beyrugey): a royal-style cream sofa set with big gold-trimmed cushions, an "
          "Italian marble centre table with crystal vases and ornaments, a soft velvet rug, a big wall-mounted TV "
          "(screen dark/black), a glass display showcase, marble floor")
VERANDA = ("the front veranda (fendaa) with a big wooden swing bench (undhoali), potted plants, a sandy yard, "
           "flowering trees by the boundary wall")

LOC = {
    "dawn_ext": HOUSE_EXT,
    "corridor_dawn": CORRIDOR,
    "veranda": VERANDA,
    "living_memory": LIVING,
    "corridor_morning": CORRIDOR,
    "living_morning": LIVING,
    "living_noon": LIVING,
    "corridor_noon": CORRIDOR,
    "yamna_room": YAMNA_ROOM,
    "parents_room": PARENTS_ROOM,
    "corridor_rest": CORRIDOR,
    "corridor_dim": CORRIDOR,
}
MOOD = {
    "dawn_ext": "sunrise, soft pale-gold first light breaking through misty palms, long blue-grey shadows, the house still and silent, a heavy melancholy calm",
    "corridor_dawn": "dawn, cold grey-blue first light from a far window, the ceiling light off, deep soft shadows, quiet and heavy with grief",
    "veranda": "early morning around seven, low soft golden sunlight filtered through the flowering trees, drifting morning mist, long shadows, quiet sorrow",
    "living_memory": "a memory of last night: dim warm amber lamplight, a cold blue haze, soft dreamy blur and vignette at the edges",
    "corridor_morning": "morning, muted daylight from a far window, cool grey shadows along the corridor, tense and uneasy",
    "living_morning": "morning, soft muted daylight through sheer curtains, cool grey tones, a tense heavy silence",
    "living_noon": "noon, flat daylight muted by the drawn sheer curtains, cool grey tones, anxious stillness",
    "corridor_noon": "noon, but the corridor is dim; a cold blue-grey light spills out of the opening bedroom door, dread",
    "yamna_room": "noon outside but the room is dim and cold: muted grey daylight through the cracked window and the sheer curtain, the round ceiling light unlit, a cold blue-grey haze hanging in the air, oppressive and eerie",
    "parents_room": "early afternoon, heavy curtains half drawn, soft grey light, a dim warm bedside lamp, exhausted and grieving",
    "corridor_rest": "afternoon, curtains drawn, soft dim grey light, a warm sliver of lamplight from a half-open door, a fragile quiet",
    "corridor_dim": "late afternoon gone dim, curtains drawn, the round ceiling light flickering, a cold blue haze, deep shadows, sudden dread",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
YAM = ("Yamna, a petite 15-year-old girl, pale and tired with dark circles under her eyes, in her loose long-sleeved "
       "ankle-length pale-lilac dress with the sleeves down to her wrists and her white hijab wrapped snugly, fully "
       "covering her hair and neck")

BEATS = [
    dict(to=2, reason="episode opening: sunrise over the family's island house the morning after the night of terror", loc="dawn_ext",
         visual="the large white two-storey house at sunrise seen from the sandy front yard, pale-gold light breaking through misty palms behind it, the empty wooden swing bench on the front veranda, all windows dark and still; no people",
         camera="wide establishing shot, eye level, the house and misty palms in the upper two-thirds, the shadowed sandy yard as the calm lower third",
         amb="dawn_exterior"),
    dict(to=5, reason="character focus: Saahidha, shattered, outside Yamna's room at dawn (the skipped prayer)", chars=["saahidha"], loc="corridor_dawn",
         visual="Saahidha standing alone in the dim corridor just outside Yamna's half-closed dark-wood bedroom door, clutching a plain folded green prayer mat with no writing to her chest, her head lowered, eyes swollen from crying, tears on her cheeks, a look of utter heartbreak and betrayal",
         camera=f"medium shot, eye level, slightly from the side, {LOW} (polished marble floor in shadow)",
         amb="home_day", transition="dissolve"),
    dict(to=9, reason="scene change: 7 am, she sits weeping on the veranda swing and answers her son's call", chars=["saahidha"], loc="veranda",
         visual="Saahidha sitting on the big wooden swing bench on the veranda, wiping tears from her cheek with one hand while holding a phone to her ear with the other, the phone's back turned to us and blank, her face crumpled with grief, flowering trees and morning mist behind her",
         camera=f"medium shot, eye level, {LOW} (wooden veranda floor in soft shadow)", amb="garden_day"),
    dict(to=12, reason="emotional turning point: at the word 'Dad' her face hardens", chars=["saahidha"], loc="veranda",
         visual="close-up of Saahidha on the swing with the phone pressed to her ear, her tear-streaked face suddenly hard and cold, jaw set, eyes narrowed with bitter anger and distrust, morning light on one side of her face",
         camera=f"close-up, eye level, {LOW} (her shoulder and the swing's wooden backrest in soft shadow)", amb="garden_day", hum=True),
    dict(to=15, reason="memory (Faarish's account): before reciting last night Ghassan checked the family's names and details with Khalid", chars=["ghassan", "khalid"], loc="living_memory",
         visual="last night in the living room: Ghassan sitting forward on the cream sofa asking a question with a calm searching look, his big black leather bag beside him; Khalid sitting opposite, leaning towards him and answering earnestly, one open hand raised as he explains; nobody else",
         camera=f"medium two-shot, eye level, {LOW} (velvet rug and marble table edge in shadow)", amb="memory", transition="dissolve"),
    dict(to=18, reason="back to Saahidha on the phone with Faarish (until he hangs up and she reflects)", reuse="beat_004", chars=["saahidha"], loc="veranda",
         visual="reuse of beat_004", amb="garden_day", transition="dissolve"),
    dict(to=23, reason="action change: after tea she goes to call Yamna; the door is locked from inside and she knocks twice", chars=["saahidha"], loc="corridor_morning",
         visual="Saahidha standing at Yamna's closed dark-wood bedroom door holding a small tray with a cup of tea in one hand, knocking softly on the door with the knuckles of her other hand, her head tilted to listen, worried and hesitant",
         camera=f"medium shot, eye level, from the side along the corridor, {LOW} (marble floor in soft shadow)", amb="home_day"),
    dict(to=27, reason="scene change: the living room — Ghassan deep in thought, Khalid chin in hand, Saahidha with a broom", chars=["ghassan", "khalid", "saahidha"], loc="living_morning",
         visual="the living room: Ghassan sitting leaning back in a single armchair-sofa, fingers steepled, lost in deep thought, speaking with a grave look; Khalid sitting at one end of the long cream sofa with his chin resting on his hand, exhausted; Saahidha standing a few steps away holding a broom, turning to listen with a tense, guarded face",
         camera=f"medium wide shot, eye level, {LOW} (velvet rug and marble floor)", amb="home_day"),
    dict(to=30, reason="time change: noon, the door is still shut; she turns to Ghassan and Khalid answers that he has the spare key", chars=["saahidha", "ghassan", "khalid"], loc="living_noon",
         visual="Saahidha standing before Ghassan in the living room, speaking anxiously with her hands clasped; Ghassan seated, looking up at her; Khalid half-rising from the long sofa behind, one hand raised as he answers her; Saahidha does not look at Khalid",
         camera=f"medium wide shot, eye level, {LOW} (marble floor)", amb="home_day", transition="black"),
    dict(to=32, reason="action change: Khalid unlocks Yamna's door with the spare key; everyone freezes in shock", chars=["khalid", "saahidha", "ghassan"], loc="corridor_noon",
         visual="Khalid at Yamna's bedroom door, a bunch of keys in the lock, pushing the door open; Saahidha and Ghassan close behind him; all three frozen in the doorway with shocked, wide-eyed faces, a cold blue-grey light falling on them from inside the room",
         camera=f"medium shot from inside the room looking back at the doorway, eye level, {LOW} (shadowed marble floor)",
         amb="haunted_living", hum=True),
    dict(to=36, reason="reveal: the wrecked bedroom (bible rule 5)", loc="yamna_room",
         visual="the wrecked bedroom with nobody in view: the tall wardrobe doors hanging open and torn clothes flung across the marble floor and the bed, the white walls covered with dark chaotic abstract marker scrawls of swirling lines (no letters, no faces, no symbols), the desk drawers pulled out, books and pens scattered everywhere, the sliding window glass cracked into a spider-web pattern, the sheer curtain lifting slightly with no wind",
         camera="wide shot from the doorway, eye level, the walls and window in the upper two-thirds, the floor with scattered clothes in soft dark shadow as the lower third",
         amb="haunted_room", sens="other", safe="destruction shown as a still, empty room; scrawls are abstract lines with no words, faces or symbols"),
    dict(to=39, reason="emotional turning point: everyone's eyes turn to Yamna sitting on the study desk", chars=["yamna"], loc="yamna_room",
         visual=f"{YAM}, sitting on top of the study desk under the cracked window with her legs hanging down, her hands resting hidden in the folds of the dress in her lap, her face half in shadow, staring at the doorway with a cold, blank, unblinking stare; scattered books and torn clothes on the floor below; her face unmarked",
         camera=f"medium wide shot, eye level, {LOW} (scattered books on the dark floor)",
         amb="haunted_room", hum=True, sens="violence",
         safe="her cut hair, nail marks on her face, torn sleeves and bitten arms are never shown: she is fully clothed in her lilac dress and hijab, face half in shadow, cold stare, unhurt"),
    dict(to=43, reason="reaction: the parents' horror at her state; Saahidha feels the ground give way", chars=["saahidha", "khalid"], loc="corridor_noon",
         visual="Saahidha in the bedroom doorway with one hand pressed over her mouth and the other gripping the door frame, eyes wide with horror and tears, her knees starting to buckle; Khalid right behind her, his hand on her shoulder, staring into the room aghast",
         camera=f"medium close shot, eye level, {LOW} (dark door frame and floor in shadow)",
         amb="haunted_room", hum=True, sens="violence", safe="the injuries described are shown only through the parents' horrified faces"),
    dict(to=44, reason="possession: the mocking words and a heavy laugh fill the room (shadow use 1 of 1)", loc="yamna_room",
         visual="the dim wrecked room: a petite girl in a pale-lilac dress and white hijab only as a dark silhouette sitting on the desk against the grey window light, her face completely in shadow; on the scrawled white wall behind her a huge dark smoky shadow with long thin shadowy fingers spreads upward, no face, touching no one; cold blue haze",
         camera="medium wide shot, slightly low angle, the silhouette and the shadow in the upper two-thirds, the dark floor as the calm lower third",
         amb="haunted_room", hum=True, sens="other", safe="the jinn's laugh shown only as a faceless smoky shadow on the wall; the girl only as a silhouette"),
    dict(to=46, reason="scene change: Khalid has laid the fainted Saahidha on their bed and turns to run back to his daughter", chars=["saahidha", "khalid"], loc="parents_room",
         visual="Saahidha lying unconscious on top of the cream bedding of the dark-wood bed, fully dressed in her bottle-green dress with her beige hijab on, eyes closed; Khalid standing beside the bed, half turned towards the door, looking back at her with a torn, frantic expression",
         camera=f"medium wide shot, eye level, {LOW} (the bed's edge and floor in soft shadow)", amb="room_day",
         sens="intimacy", safe="the carrying in his arms is not shown; only the aftermath, her lying alone and him standing apart"),
    dict(to=48, reason="action change: Khalid calls to his daughter lovingly; she rejects him", chars=["khalid", "yamna"], loc="yamna_room",
         visual=f"Khalid standing a few steps from the study desk in the wrecked room, both hands open towards his daughter, his face full of love and pain; {YAM}, sitting on the desk, her face turned away from him in cold defiance, half in shadow",
         camera=f"medium two-shot, eye level, {LOW} (scattered books on the floor)", amb="haunted_room"),
    dict(to=51, reason="action change: Khalid brings the first-aid box; unexpectedly she lets him tend to her", chars=["khalid"], loc="yamna_room",
         visual="Khalid crouching beside the study desk holding an open plain white first-aid box with rolls of white bandage and cotton inside, his face close and full of worry and tender concern, eyes glistening; at the edge of the frame only the hem of a pale-lilac dress hanging from the desk",
         camera=f"medium close-up, eye level, {LOW} (the open box and the dark floor)", amb="haunted_room",
         sens="violence", safe="no injury, no dressing of wounds shown: only the open first-aid box and the father's worried face"),
    dict(to=53, reason="back to Khalid pleading with Yamna, who gives no response to his offer of food", reuse="beat_016", chars=["khalid", "yamna"], loc="yamna_room",
         visual="reuse of beat_016", amb="haunted_room"),
    dict(to=54, reason="character change: Ghassan comes out of Yamna's room with a dress and a lock of her hair", chars=["ghassan"], loc="corridor_noon",
         visual="Ghassan stepping out of the bedroom doorway into the dim corridor, holding a neatly folded pale-lilac dress with a small closed white cloth bundle on top of it, his black leather bag on his shoulder, a faint sly satisfied look in his narrow eyes",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)", amb="home_day"),
    dict(to=56, reason="scene change: Khalid revives Saahidha with water; she opens her eyes", chars=["saahidha", "khalid"], loc="parents_room",
         visual="Saahidha lying on top of the bedding, fully dressed with her beige hijab on, slowly opening her exhausted tear-filled eyes; Khalid sitting on a chair beside the bed holding a glass of water, leaning towards her with deep concern",
         camera=f"medium shot, eye level, {LOW} (bed edge in soft shadow)", amb="room_day"),
    dict(to=58, reason="emotional turning point: she breaks down and accuses him (bible rule 8)", chars=["saahidha", "khalid"], loc="parents_room",
         visual="Saahidha sitting on the edge of the bed, bent forward, sobbing hard into both her hands; Khalid standing in front of her at arm's length, tears running down his face, hands half raised helplessly",
         camera=f"medium two-shot, eye level, {LOW} (floor in shadow)", amb="room_day", hum=True,
         sens="intimacy", safe="the chest-beating is replaced by Saahidha crying into her hands in front of a weeping Khalid; no contact"),
    dict(to=61, reason="framing change: Khalid's tearful oath by Allah", chars=["khalid"], loc="parents_room",
         visual="close-up of Khalid weeping openly, tears running into his grey-streaked beard, his right hand pressed flat on his chest as he swears, his face full of anguish and sincerity",
         camera=f"close-up, eye level, {LOW} (his shoulder and dim room in shadow)", amb="room_day", hum=True),
    dict(to=64, reason="action change: her doubts dissolve; they sit together calmly (bible rule 8)", chars=["saahidha", "khalid"], loc="parents_room",
         visual="Saahidha and Khalid sitting side by side on the edge of the bed, his hand resting on her shoulder; her head bowed, eyes closed, letting out a long deep breath, tear tracks on her cheeks, the tension gone from her face; Khalid looking down at her with tired relief",
         camera=f"medium two-shot, eye level, {LOW} (floor in soft shadow)", amb="room_day",
         sens="intimacy", safe="her resting her head on his chest is shown only as sitting side by side with his hand on her shoulder"),
    dict(to=69, reason="time passes: the exhausted couple rest (never shown lying together) — reflective passage", loc="corridor_rest",
         visual="the quiet dim corridor: the parents' bedroom door left slightly ajar with a soft warm sliver of lamplight on the marble floor, and further down the corridor Yamna's closed dark-wood door in cold blue shadow; no people",
         camera="medium wide shot down the corridor, eye level, the doors in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="home_day", transition="dissolve", sens="intimacy", safe="the couple lying on the bed is not shown; only the half-open bedroom door"),
    dict(to=72, reason="action change: Yamna's door slams with a huge bang and the house shakes", loc="corridor_dim",
         visual="Yamna's dark-wood bedroom door just slammed shut at the end of the dim corridor, a puff of dust and cold haze trembling in the air around its frame, the round ceiling light flickering, deep shadows; no people",
         camera="medium shot, slightly low angle, the door in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="haunted_living", hum=True),
    dict(to=73, reason="action change: the couple rush out of their room in alarm", chars=["khalid", "saahidha"], loc="corridor_dim",
         visual="Khalid and Saahidha rushing out of their bedroom doorway into the dim corridor, startled and terrified, Khalid in front with one arm raised, Saahidha just behind him clutching the edge of her hijab, both staring down the corridor",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)", amb="haunted_living", hum=True),
    dict(to=74, reason="action change: Yamna, not herself, marches towards the kitchen; Ghassan comes out of his room", chars=["ghassan"], loc="corridor_dim",
         visual="a petite girl in a long pale-lilac dress and a white hijab seen only from behind, walking with rigid heavy steps down the dim corridor towards the kitchen doorway at the far end; on one side Ghassan stepping out of a side doorway, startled, staring after her",
         camera="medium wide shot from behind, eye level, the figures in the upper two-thirds, the dark marble floor as the calm lower third",
         amb="haunted_living", hum=True, sens="other", safe="Yamna's possessed state shown only as a rigid figure seen from behind"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The sun rising on a new day brought many people new hopes. But Saahidha's heart lay in pieces.")
sh(2, "The sweet hopes she had held for the future of the daughter she had raised with such love, like a piece of her own heart, had shattered to dust.")
sh(3, "Today was the first day since that child turned seven that she had missed an obligatory prayer. Saahidha's heart was full of endless grief.",
   hum=True)
sh(4, "From the day she married Khalid at just fifteen and came to his house until today, Khalid had never wounded her heart the way he had wounded it today.")
sh(5, "The trust she had placed in the husband she had lived with, trusting him most of all her life, was lost in a single short moment.")
sh(6, "Having come out of Yamna's room and sat down on the big swing on the veranda, Saahidha was still sitting there weeping when the clock struck seven in the morning.",
   [("creak", "އުނދޯލީގައި", -22), ("sob_breath", "ރޯލަ", -24)])
sh(7, "At the ring of the phone in her lap she wiped her tears and pressed the phone to her ear. \"My son! Your little sister is in such a terrible state,",
   [("phone_buzz", "ރިންގުގެ", -18)])
sh(8, "what are we going to do now!\" As she said this, Saahidha broke down crying again. \"Mum! Dad called me, so I'm calling you too;",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -22)])
sh(9, "Dad even told me how things went last night.\" On hearing the word \"Dad\" among Faarish's words, the colour of Saahidha's face changed.")
sh(10, "\"He is not someone even you should call Dad!\" Saahidha's sentence was short. But there was authority in that command. \"Mum!")
sh(11, "So as not to decide alone on what Dad told me, I found Ghassan's phone number and called Ghassan too!")
sh(12, "He said he strongly believes that what the jinn did was a lie,\" Faarish said. \"Why should Ghassan think that?\"")
sh(13, "Saahidha wanted to understand the reason. \"Before Ghassan started reciting last night, he confirmed little sister's name, her age, Mum's full name and Dad's full name with Dad, you know!")
sh(14, "Ghassan even asked me later whether Dad had given him the right details. Dad...")
sh(15, "if he wanted to kill little sister, he wouldn't give the right details, would he! And he wouldn't spend so much bringing Ghassan to do the ruqyah, would he!\"")
sh(16, "Faarish tried to make his mother see the truth of the matter. As he knew from some stories he had heard,")
sh(17, "in situations like this, tearing a family apart and dividing it is a clever trick that jinn use. Saying that, at Dad's request, he and his friend Adheel would come to the island tomorrow, he put down the phone.")
sh(18, "Saahidha thought over what Faarish had said. For a moment she could believe it, but then the voices she had heard last night came back to her mind.",
   hum=True)
sh(19, "She could not decide which way to believe. Saahidha made the morning tea and called Ghassan to have tea.",
   [("cup_clatter", "ތައްޔާރުކޮށްފައި", -22)])
sh(20, "She was still not at ease with Khalid. Before leaning on a suspicion and making a decision, she wanted to be sure.")
sh(21, "When Khalid and Ghassan had finished their tea, Saahidha went to call Yamna for tea. This time Yamna's room was locked from the inside.",
   [("lock_click", "ތަޅުލާފައެވެ", -22)])
sh(22, "Since, when she told Ghassan what happened at dawn, he had advised her not to keep asking the same thing of Yamna,")
sh(23, "after knocking on the door twice, Saahidha turned back and walked towards the kitchen.",
   [("knock", "ޓަކިޖަހާލުމަށްފަހު", -16)])
sh(24, "In the living room Ghassan sat leaning back on a single sofa, lost in deep thought. Beside him, at one end of the long sofa, Khalid sat with his chin resting on his hand.")
sh(25, "\"The two boys will arrive by the time we start reciting tonight, won't they!\" Ghassan asked, as if to make sure. As Khalid nodded,")
sh(26, "Ghassan then turned his question to Saahidha, who was standing with a broom to sweep the house.")
sh(27, "\"To prepare for tonight's recitation I'll need one of her dresses and a lock of her hair too! Women may not enter the place of the recitation!\"")
sh(28, "Ghassan gave a frightening warning. Even by noon Yamna's door had not opened. By then Saahidha had knocked on the door two or three times. In the end,",
   [("knock", "ޓަކިވެސް", -18)])
sh(29, "out of options, she went and told Ghassan, not even wanting to speak to Khalid. \"I have the spare key to that door.\"")
sh(30, "Though she had asked Ghassan, it was Khalid who answered. As Khalid said that, Saahidha too remembered the spare key.")
sh(31, "She had been so anxious and worried that she had even forgotten there was a spare key. With heavy steps Khalid went, fetched the bunch of keys and opened the door of Yamna's room.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -22), ("lock_click", "ހުޅުވައިލިއެވެ", -18)])
sh(32, "As the door opened, it was as if everyone's breath suddenly stopped. In the sudden shock, they all froze.",
   [("creak", "ހުޅުވައިލުމާއެކު", -20), ("gasp", "ނޭވާވެސް", -20)], hum=True)
sh(33, "The clothes that had been neatly folded in order in the wardrobe had been torn and flung all over the room.")
sh(34, "The bright white walls of the room were ruined, covered all over with frightening drawings scrawled in markers of many colours.")
sh(35, "The drawers of the desk where Yamna usually sat to study had been pulled out, and the books and pens in them flung to every side of the room.")
sh(36, "Even the glass pane of the window beside the bed had been smashed to pieces. Filling the whole room",
   [("wind_gust", "އައިސްފައި", -22)])
sh(37, "was a foul stench; the eyes of everyone, held fast by it, turned with a shock to Yamna, sitting on the study desk with her legs hanging down.",
   [("heartbeat", "ސިހުމަކާއެކު", -20)], hum=True)
sh(38, "The sight cast an indescribable anguish over the whole place. Yamna's beautiful long hair had been cruelly,", hum=True)
sh(39, "chopped short without any order. The deep nail marks gouged into her face during last night's terrible event stood out on that fair face in a way that tore at the heart.")
sh(40, "The sleeves of the long-sleeved T-shirt she wore had been torn off at the elbow, leaving that innocent girl's arms bare.")
sh(41, "And on that smooth skin there were now many painful wounds. From the deep wounds torn by nails, blood was still oozing.", hum=True)
sh(42, "A little lower, near the wrists, reddened bite marks clearly showed the harm done to that clean skin.")
sh(43, "At this heartbreaking sight Saahidha felt as if the ground had slipped away from beneath her feet. \"Still putting on such a big act, eh!",
   [("breath_heavy", "ދެމިގެން", -22)])
sh(44, "This drama has only just begun!\" These were Yamna's mocking words. At the same moment, the sound of a foul, heavy laugh echoed through the room.",
   [("low_growl", "ހިނިގަނޑުގެ", -20)], hum=True)
sh(45, "Khalid lifted Saahidha in his arms, carried her to their room and laid her on the bed.",
   [("footsteps_pavement", "ގެންގޮސް", -24)])
sh(46, "Then he ran back again to see how his daughter was. Did the girl not even feel the pain of the wounds all over her body,",
   [("footsteps_pavement", "ދުއްވައިގަތީ", -22)])
sh(47, "Khalid wondered. As he entered the room, Khalid called out to his daughter with boundless love. \"I am not your child!")
sh(48, "Don't call me your child any more!\" Yamna ordered her father, showing defiance and stubbornness.", hum=True)
sh(49, "Then Khalid hurried to bring the first-aid box and, opening it, came close to Yamna to put medicine on the wounds on his daughter's body.",
   [("cloth_rustle", "ހުޅުވާލަމުން", -22)])
sh(50, "Yet he had no hope at all of getting anywhere even with that. But contrary to what he expected,")
sh(51, "he was allowed to treat his daughter's wounds without much resistance, and for that he gave thanks before Allah, Glorified and Exalted.",
   [("sigh", "ޝުކުރު", -24)])
sh(52, "Knowing that Yamna had eaten nothing since she drank tea yesterday afternoon, Khalid tried every way he could to get her to eat something.")
sh(53, "But none of his words got any response from Yamna. Khalid then hurried to see how his wife was.",
   [("footsteps_pavement", "އަވަސްވެގަތީ", -24)])
sh(54, "Just then Ghassan, too, came out of Yamna's room holding one of the girl's dresses and a lock of her hair. After gently rubbing a few drops of water on Saahidha's face,",
   [("door_close", "ނިކުމެއްޖެއެވެ", -22), ("pour", "ފެންފޮދެއް", -24)])
sh(55, "Khalid lovingly patted her cheek twice. At that, her eyes, full of utter exhaustion and anguish,")
sh(56, "Saahidha slowly opened. On seeing Khalid before her, the tears she had held back for so long burst out like a broken dam.",
   [("sob_breath", "ކަރުނަތައް", -22)])
sh(57, "Crying out with the pain rising in her heart, she began to beat on Khalid's chest with both hands. \"Why?",
   [("sob_breath", "ރޮއިގަންނަމުން", -20)], hum=True)
sh(58, "Why are you doing such great harm to my child, the light of my eyes?\" Saahidha asked, sobbing and breaking down, in a voice of grievance. \"Saahidha!",
   [("sob_breath", "ރޮއިރޮއި", -22)])
sh(59, "She is my child too, made of my own flesh and blood! Every day of my life I spend for the future of those children.")
sh(60, "Saahidha! Don't do this, trust me!\" As Khalid's voice broke, pearls of tears fell from his eyes too.",
   [("breath", "ބެދިގެންދިޔައިރު", -22)], hum=True)
sh(61, "\"I swear by Allah, I have never done even the smallest harm or hurt to my own child, and I never will.\"", hum=True)
sh(62, "This time Khalid spoke sobbing and weeping. The extreme pain showing on Khalid's face",
   [("sob_breath", "ގިސްލާ", -22)])
sh(63, "and the truth in his words touched the depths of Saahidha's heart. It was as if the doubts that had arisen in her heart faded away.")
sh(64, "Slowly resting her head on Khalid's broad chest, Saahidha let out a deep breath to ease the weight on her heart. After that,",
   [("sigh", "ނޭވާއެއް", -20)])
sh(65, "to shake off their exhaustion, the couple lay down on the bed. In the past frightening and anxious days,",
   [("cloth_rustle", "އޮށޯވެލިއެވެ", -24)])
sh(66, "they had not had a single chance to rest their backs on a bed in peace. Sweet sleep at night had become a stranger to them.")
sh(67, "Because of their anguish and deep grief, they could swallow only enough food to keep the life in their bodies.")
sh(68, "Even so, with all that pain and with hearts breaking to pieces, the couple kept up their courage only for their beloved daughter.")
sh(69, "As their backs touched the bed, the couple, who had been enduring extreme exhaustion, slowly sank into a deep sea of sleep.",
   [("breath", "ނިދީގެ", -24)])
sh(70, "But that calm lasted only a short while. Suddenly, shattering the silence of the whole place,", hum=True)
sh(71, "with a loud 'BANG' of Yamna's bedroom door, the couple woke with a start.",
   [("door_slam", "ބަން", -12), ("gasp", "ހޭލެވުނެވެ", -20)], hum=True)
sh(72, "The door slammed so hard it was as if the walls of the whole house shook. In the sudden shock and alarm at the loud noise,",
   [("heartbeat", "ސިހުމާއި", -20)])
sh(73, "the couple did not even know how they leapt out of bed. When they came running out of the room, Yamna did not look like someone in her right mind.",
   [("footsteps_pavement", "ދުވެފައި", -20)], hum=True)
sh(74, "With heavy steps she was heading towards the kitchen. At that moment, because of the loud noise, Ghassan, who was in his room, came out too. (To be continued)",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -20), ("door_open", "ނިކުމެއްޖެއެވެ", -22)], hum=True)
SHOTS = S

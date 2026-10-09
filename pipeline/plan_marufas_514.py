"""Beat/shot plan for Marufas episode 514 (used by plan_beats.py)."""

LOC = {
    "dining": "the family's dining area beside the large modern kitchen of their big island house: a long polished dark-wood dining table with high-backed chairs, white walls, a polished white marble floor, a wide window with sheer white curtains",
    "living": "the large formal living room (beyrugey) of the family's big modern island house: a royal-style cream sofa set with big gold-trimmed cushions, an Italian marble centre table with crystal vases and ornaments, a soft velvet rug, a big wall-mounted TV with a dark black screen, a glass display showcase, a polished marble floor",
    "corridor": "the inner corridor of the family's big modern island house outside Yamna's bedroom: white walls, a polished white marble floor, Yamna's white wooden bedroom door, a single dim wall lamp",
    "yamna_room": "Yamna's spacious bedroom in the family's large modern island house: white walls, polished white marble floor, a big bed with white sheets and a pale headboard, a study desk with books and pens under the window, a tall dark-wood wardrobe, a glass sliding window beside the bed with a sheer white curtain, a round ceiling light",
    "island_lane": "white sandy lanes between coral-stone walls on a small Maldivian island, palms and breadfruit trees, a few dim street lamps",
    "beach_night": "the Rannikamagu beach of the island at 3 am: a dark lagoon, faint moonlight, a huge old beach tree whose shadow falls on the pale sand",
    "abandoned_house": "a long-abandoned coral-stone house in a lonely overgrown corner of the island: broken wooden shutters, peeling walls, dust, cobwebs, a dark back room with a single old wooden chair; reached through scrub",
    "veranda": "the front veranda (fendaa) of the family's big island house with a big wooden swing bench (undhoali), potted plants, a sandy yard, flowering trees by the boundary wall",
}
MOOD = {
    "dining": "midday, soft bright tropical daylight filtered through the sheer curtains but cool grey shadows inside the room, a tense, uneasy silence",
    "living": "evening, dim, one warm table lamp against cool blue-grey shadows, heavy and weary",
    "corridor": "late night, dim, cold blue haze with one warm wall lamp, deep shadows, uneasy and sinister",
    "yamna_room": "late night, the round ceiling light flickering and dimming, a cold blue haze filling the room, one weak warm bedside lamp, icy dread",
    "island_lane": "about 3 am, dark night, dim cold blue haze, one weak amber street lamp far away, deep shadows, tense and secretive",
    "beach_night": "about 3 am, faint silver moonlight through thin clouds, a dark still lagoon, cold blue-grey mist, the deep black shadow of the big tree, eerie and deserted",
    "abandoned_house": "about 3 am, pitch dark, one thin shaft of cold blue moonlight through a broken shutter, drifting dust, cold dread",
    "veranda": "a warm golden afternoon memory, soft sunlight and a gentle dreamy haze, tender and safe",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
YB = "Yamna lying in the bed under a white blanket pulled up to her chest, her pale-lilac long-sleeved dress and white hijab fully covering her hair and neck, pale, tired, dark circles under her eyes, no marks on her face"

BEATS = [
    # ---------------- LUNCH: GHASSAN DEMANDS SECRECY AND MONEY
    dict(to=5, reason="scene continues from 510: lunch at the dining table, Ghassan's displeased reaction to Saeed's request",
         chars=["ghassan", "khalid", "saahidha", "faarish"], loc="dining",
         visual="the family at lunch around the long dark-wood dining table with simple dishes of rice and curry and glasses of water; Ghassan seated at the head of the table in the centre of the frame, his face cold, hard and displeased, eyes narrowed, lips pressed thin; Khalid, Saahidha and Faarish seated along the sides, turned towards him, uneasy and silent",
         camera=f"medium wide shot, eye level from the far end of the table, Ghassan's face in the upper third, {LOW} (table top in soft shadow)",
         amb="home_day"),
    dict(to=7, reason="action change: Ghassan stands up from the table and gives his orders for tomorrow night",
         chars=["ghassan", "khalid", "saahidha", "faarish"], loc="dining",
         visual="Ghassan standing up at the head of the dining table, his big black leather bag on his shoulder, looking down over the seated family with a cold commanding stare, one hand flat on the table; Khalid, Saahidha and Faarish looking up at him, worried and obedient; no money, no papers, nothing written",
         camera=f"low-angle medium shot from the side of the table, Ghassan towering in the upper half, {LOW} (table top)",
         amb="home_day", sens="other",
         safe="his demand for another 20,000 rufiyaa is carried only by his cold commanding face; no money, no bank screens, no account details"),
    dict(to=11, reason="time/focus change: the parents' quiet sacrifice for their daughter, a reflective passage",
         chars=["khalid", "saahidha"], loc="living",
         visual="Khalid and Saahidha sitting side by side on the cream gold-trimmed sofa, exhausted and heavy-hearted; Saahidha looking down at her clasped hands, her eyes tired and wet; Khalid beside her, his hand resting on her shoulder, staring into the distance; the marble table with crystal vases before them, the dark TV on the wall",
         camera=f"medium shot, eye level, {LOW} (velvet rug and marble floor in shadow)",
         amb="living_night"),
    dict(to=14, reason="time jump to the next night and focus change: Ghassan's secret scheme before the session",
         chars=["ghassan"], loc="corridor",
         visual="Ghassan standing alone in the dim corridor outside Yamna's closed white bedroom door, his big black leather bag on his shoulder, half of his lean face lit by the weak wall lamp, a sly calculating look and a thin cold smile; the door firmly closed; nobody else in the corridor",
         camera=f"medium close-up, slightly low angle, his face in the upper third, {LOW} (marble floor in shadow)",
         amb="home_night", transition="black", sens="other",
         safe="bible rule 2: his intent to abuse the girl is never implied visually; only his sly face outside the closed door, Yamna not in frame"),
    # ---------------- THE SESSION: THE MAARID EXPOSES GHASSAN
    dict(to=16, reason="scene change: after isha and dinner the whole family is in Yamna's room for the session",
         chars=["yamna", "ghassan", "khalid", "saahidha"], loc="yamna_room",
         visual=f"{YB}, her eyes open wide and staring blankly at the ceiling, her face completely still; Ghassan standing beside the bed reciting with his palm raised and hovering above her forehead without touching her; Khalid and Saahidha standing together at the foot of the bed, gripped with fear; the ceiling light flickering, cold blue haze",
         camera=f"medium wide shot, eye level from the corner of the room, {LOW} (bedsheet edge and marble floor in shadow)",
         amb="haunted_room", sens="other",
         safe="bible rule 1: the convulsion and blood-red eyes are not shown; Yamna lies still under the blanket with a blank stare, the flickering light and the family's fear carry the possession"),
    dict(to=19, reason="strong turning point: the maarid's heavy voice and sinister laugh fill the room",
         chars=[], loc="yamna_room",
         visual="the bedroom in near darkness, the ceiling bulb dead, only a weak cold bluish glow: a huge dark smoky shadow with long thin shadowy clawed fingers spreads across the white wall above the bed's headboard, no face, touching nobody; below it the small dim silhouette of a girl in a white hijab sitting up in the bed under the white blanket, her face lost in deep shadow; at the edges of the frame the dark shapes of adults recoiling",
         camera=f"wide shot, eye level, the shadow on the wall filling the upper half, {LOW} (dark bedsheet and floor)",
         amb="haunted_room", sens="other",
         safe="bible rules 1 and 14: the maarid is only a faceless smoky shadow on the wall (use 1 of 2); Yamna is a silhouette with her face in shadow"),
    dict(to=22, reason="reaction: Khalid and Faarish freeze at the maarid's accusation against Ghassan",
         chars=["khalid", "faarish"], loc="yamna_room",
         visual="Khalid and Faarish standing side by side against the white bedroom wall, frozen in shock, eyes wide, jaws clenched, slowly turning to stare at someone off-frame; flickering cold light on their faces, cold blue haze around them",
         camera=f"medium close-up two-shot, eye level, {LOW} (dark wall and floor)",
         amb="haunted_room", sens="other",
         safe="bible rule 2: the accusation of abuse is carried only by the men's shocked faces; nothing about it is shown"),
    dict(to=25, reason="action change: Ghassan recites faster and denies it; Faarish shouts back at the jinn",
         chars=["ghassan", "faarish"], loc="yamna_room",
         visual="Ghassan standing beside the bed in the foreground, reciting faster with one palm raised, his face hard and sweating, lips moving quickly; behind him Faarish leaning forward in anger, shouting, his fists clenched at his sides; the bed edge with the white blanket only partly visible at the bottom; flickering bulb, cold blue haze",
         camera=f"medium shot, eye level, {LOW} (white bedsheet edge in shadow)",
         amb="haunted_room"),
    dict(to=28, reason="focus change: the maarid mocks them through Yamna and names Rannikamagu beach",
         chars=["yamna"], loc="yamna_room",
         visual=f"close-up of {YB}, her head on the pillow, her face pale and completely still, a cold unblinking stare straight ahead and a faint unsettling half-smile; the light flickering over her calm face; cold blue haze",
         camera=f"close-up, slightly high angle, her face in the upper half, {LOW} (white blanket in shadow)",
         amb="haunted_room", sens="other",
         safe="bible rule 1: a calm close-up of her blank, unmarked face with a cold stare; no red eyes, no contortion"),
    dict(to=31, reason="reveal of a face: Ghassan is startled and afraid; Khalid and Faarish look at each other",
         chars=["ghassan", "khalid", "faarish"], loc="yamna_room",
         visual="close-up of Ghassan's face in the foreground, suddenly startled and afraid, eyes wide, a bead of sweat on his brow, his raised hand frozen in mid-air; in the soft-focus background Khalid and Faarish turning to look at each other with suspicion; deathly still room, cold blue haze",
         camera=f"close-up with a deep background, eye level, {LOW} (dark)",
         amb="haunted_room"),
    # ---------------- THE 3 AM RUN TO RANNIKAMAGU BEACH
    dict(to=34, reason="scene change: Faarish and Adheel run out into the 3 am darkness to the beach",
         chars=["faarish", "adheel"], loc="beach_night",
         visual="Faarish and Adheel seen from behind, running fast across the dark pale sand towards a huge old beach tree far ahead whose black branches spread against the faint moonlight; deep in the shadow under the tree, far away, a tiny pale figure sitting on the sand; the dark lagoon with small waves on one side",
         camera=f"wide shot, eye level from behind the running men, the tree and sky in the upper two-thirds, {LOW} (dark sand)",
         amb="beach_night", transition="black"),
    dict(to=36, reason="character enters: Aadhanbe under the big tree with a strange bowl",
         chars=["aadhanbe"], loc="beach_night",
         visual="Aadhanbe sitting cross-legged on the sand in the deep shadow of the huge old beach tree, holding a plain dark clay bowl of dark water in both hands, bending over it and murmuring, lips moving, eyes narrowed; faint moonlight on his white cap, white shirt and checked sarong; the dark lagoon behind him; the bowl plain with no symbols",
         camera=f"medium shot, slightly low angle, his face in the upper half, {LOW} (sand in shadow)",
         amb="beach_night"),
    dict(to=38, reason="action change: Faarish shouts 'Stop!'; Aadhanbe turns, the two young men come at him",
         chars=["aadhanbe", "faarish", "adheel"], loc="beach_night",
         visual="Aadhanbe in the foreground sitting on the sand under the big tree, turning his head back over his shoulder, startled and frightened, the clay bowl still in his hands; far behind him across the moonlit sand two young men, Faarish and Adheel, hurrying towards him, still at a distance, small in the frame",
         camera=f"medium wide shot, eye level, {LOW} (sand)",
         amb="beach_night", sens="violence",
         safe="bible rule 3: the grab is shown only as the two young men approaching the old man at a distance; no contact"),
    dict(to=39, reason="object detail: the bowl drops and the black water soaks into the sand",
         chars=[], loc="beach_night",
         visual="close-up of a plain dark clay bowl lying tipped on its side on the pale sand under the tree, dark water spilling out and soaking into the sand, scattered footprints around it, faint moonlight; nobody in frame",
         camera="close-up, high angle looking down at the sand, the bowl in the upper half",
         amb="beach_night", sens="violence",
         safe="bible rule 3: the struggle is shown only by the dropped bowl on the sand"),
    dict(to=42, reason="focus change: Faarish is now certain and furious",
         chars=["faarish"], loc="beach_night",
         visual="close-up of Faarish standing on the moonlit beach under the big tree, his face furious, teeth gritted, eyes burning, chest heaving; the dark lagoon and mist behind him; nobody else in frame",
         camera=f"close-up, slightly low angle, {LOW} (dark)",
         amb="beach_night", sens="violence",
         safe="bible rule 3: the threat and the gagging with the cap are carried only by Faarish's furious face; Aadhanbe is not shown"),
    # ---------------- THE ABANDONED HOUSE
    dict(to=45, reason="scene change: the long-abandoned house far from people",
         chars=[], loc="abandoned_house",
         visual="outside view at night of a long-abandoned coral-stone house deep in overgrown scrub, broken wooden shutters hanging askew, peeling walls, its weathered wooden door closed; faint cold moonlight, a trampled sandy path leading to the door; no people",
         camera=f"medium wide shot, eye level, the house in the upper two-thirds, {LOW} (dark scrub and sand)",
         amb="abandoned_house", sens="violence",
         safe="bible rule 3: the dragging and binding with rope are replaced by the weathered closed door of the abandoned house; nobody shown"),
    dict(to=46, reason="scene change: inside the dark house, Faarish confronts the old man",
         chars=["faarish", "adheel"], loc="abandoned_house",
         visual="inside the dark abandoned house: Faarish standing near the broken doorway, his furious face half in shadow, lit by a thin shaft of cold moonlight through a broken shutter, glaring across the room; Adheel just behind his shoulder, tense and angry; cobwebs, peeling walls, drifting dust; nobody else in frame",
         camera=f"medium close-up, eye level, {LOW} (dusty floor in darkness)",
         amb="abandoned_house", sens="violence",
         safe="bible rule 3: the interrogation is shown as Faarish's furious face apart from the old man"),
    dict(to=48, reason="focus change: Aadhanbe trembling and begging",
         chars=["aadhanbe"], loc="abandoned_house",
         visual="Aadhanbe sitting alone on a single old wooden chair in the middle of the dark back room, frightened and trembling, tears on his wrinkled cheeks, his hands resting in his lap holding his white cloth cap, his white hair uncovered; he is unhurt and clean, his white shirt and checked sarong neat; a thin shaft of cold moonlight falls on him; dust and cobwebs around",
         camera=f"medium shot, eye level, his face in the upper half, {LOW} (dusty floor in shadow)",
         amb="abandoned_house", sens="violence",
         safe="bible rule 3: Aadhanbe alone on the chair, unhurt, hands in his lap; no rope, no gag, nobody touching him"),
    dict(to=51, reason="return: Faarish's accusation and Adheel's anger (same moment as beat_017)",
         reuse="beat_017", chars=["faarish", "adheel"], loc="abandoned_house", amb="abandoned_house",
         visual="reuse of beat_017: Faarish and Adheel, furious, apart from the old man",
         sens="violence", safe="bible rule 3: faces only, at a distance"),
    dict(to=53, reason="return: Aadhanbe swears by Allah about Jaleel (same image as beat_018)",
         reuse="beat_018", chars=["aadhanbe"], loc="abandoned_house", amb="abandoned_house",
         visual="reuse of beat_018: Aadhanbe alone on the chair, pleading",
         sens="violence", safe="bible rule 3: Aadhanbe alone, unhurt"),
    dict(to=55, reason="memory: Faarish remembers protecting his little sister since childhood",
         chars=["faarish", "yamna"], loc="veranda",
         visual="a warm memory: the big older brother Faarish sitting at one end of the big wooden swing bench on the sunny front veranda and his much smaller little sister Yamna at the other end, a clear gap between them, not touching, both holding cups of tea; he smiles at her protectively like a guardian while she laughs happily, healthy and bright-eyed in her pale-lilac dress and white hijab fully covering her hair and neck; potted plants, soft golden sunlight, flowering trees",
         camera=f"medium shot, eye level, {LOW} (veranda floor in soft shade)",
         amb="memory", transition="dissolve", sens="violence",
         safe="bible rule 3: the stick is never shown; his rage is carried by the tender memory of his sister"),
    dict(to=57, reason="return: the blow and the scream are kept offscreen outside the closed house (same image as beat_016)",
         reuse="beat_016", loc="abandoned_house", amb="abandoned_house", transition="dissolve",
         visual="reuse of beat_016: the closed weathered door of the abandoned house at night",
         sens="violence", safe="bible rule 3: no hitting, no stick; only the closed house from outside with a muffled offscreen thud"),
    dict(to=58, reason="return: Adheel urges Faarish to leave (same image as beat_017)",
         reuse="beat_017", chars=["faarish", "adheel"], loc="abandoned_house", amb="abandoned_house",
         visual="reuse of beat_017: Faarish and Adheel in the dark room",
         sens="violence", safe="bible rule 3: faces only"),
    dict(to=60, reason="scene change: the two young men hurry home through the dark lanes",
         chars=["faarish", "adheel"], loc="island_lane",
         visual="Faarish and Adheel hurrying along a dark white-sand lane between coral-stone walls, glancing back over their shoulders, tense and secretive; one weak street lamp far behind them; black palm and breadfruit trees against the night sky",
         camera=f"medium wide shot, eye level, {LOW} (dark sand of the lane)",
         amb="night_lane"),
    # ---------------- HOME: THE LIE
    dict(to=63, reason="scene change: back home, Ghassan comes out of Yamna's room, worried",
         chars=["ghassan", "faarish", "adheel"], loc="corridor",
         visual="the dim corridor: Ghassan stepping out of Yamna's half-open bedroom door, his black leather bag on his shoulder, his face uneasy and worried, a bead of sweat at his temple; Faarish and Adheel just arrived in the corridor facing him, breathless; Faarish answering with a hard look",
         camera=f"medium shot, eye level, {LOW} (marble floor in shadow)",
         amb="home_night"),
    dict(to=65, reason="characters enter: Khalid and Saahidha come out, furious",
         chars=["saahidha", "khalid"], loc="corridor",
         visual="Khalid and Saahidha stepping out of Yamna's bedroom door into the dim corridor; Saahidha in front, her eyes reddened from crying, jaw clenched, her face hard with hatred; Khalid just behind her, stern and grim",
         camera=f"medium close-up, eye level, {LOW} (dark marble floor)",
         amb="home_night"),
    dict(to=67, reason="focus change: Faarish lies to his parents, his heart pounding",
         chars=["faarish"], loc="corridor",
         visual="close-up of Faarish in the dim corridor forcing a calm, steady expression, a bead of sweat on his temple, his eyes slightly evasive, a tight jaw; behind him in soft focus the shapes of his parents and Ghassan; warm wall lamp against cold blue shadow",
         camera=f"close-up, eye level, {LOW} (dark)",
         amb="home_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With that, displeasure showed on Ghassan's face. His voice had a harsh, commanding tone.")
sh(2, "\"Nobody on this island must know about Yamna's condition and this progress! Because that would be information that reaches the person doing sihr on this girl,")
sh(3, "and he might make the sihr even stronger.\" Ghassan used the excuse sorcerers usually give to hide his own evil.")
sh(4, "\"Once they've studied at Madinah University, these people think they're so great!\" The words of mockery and envy from Ghassan's tongue were aimed,")
sh(5, "as everyone there understood, at Saeed, who had come back with an Islamic education from Madinah. He wanted to keep Saeed away from that house.")
sh(6, "Because he knew a real scholar would not take long to expose his sorcery. After Ghassan finished eating,")
sh(7, "he stood up and cast his gaze over everyone. \"Tomorrow night is a big night. Everyone should come into the room for the recitation, and send another twenty thousand rufiyaa to my account!\"",
   [("cloth_rustle", "ތެދުވަމުން", -22)])
sh(8, "Every night such a recitation was held was a night on which Ghassan, exploiting the couple's helplessness, robbed that family of large sums of money.")
sh(9, "For the parents, heartbroken at their child's painful state and helplessness, the boundless love for Yamna boiling in their hearts was greater than the hardship of Ghassan's greed.",
   hum=True)
sh(10, "So, setting aside the heavy financial losses and the distress, they tied all their hope to saving their beloved child's life.")
sh(11, "They sacrificed their own happiness and property for the family's \"kamana\". That night, Ghassan wanted to perform an extremely powerful sihr.")
sh(12, "To take back the control of Yamna's body that the cursed maarid, which would not submit to his power, seized on some days, to defeat it,")
sh(13, "and to bring that body completely under the power of the ifreet in his own service. Holding that innocent girl's whole soul in his fist,",
   hum=True)
sh(14, "so as to take unlawful advantage of her forever under his savage, evil desires, he went on plotting scheme after scheme.",
   hum=True)
sh(15, "The family was ready to fall into that great trap. As Ghassan had planned, after the isha prayer and dinner, he began his game. After a while,",
   [("whisper_recite", "ފަށައިފިއެވެ", -23)])
sh(16, "a sudden convulsion seized Yamna's body as she lay in the bed, and her eyes flew wide open. At that moment blood gathered in those eyes and they turned red.",
   [("bulb_flicker", "ހުޅުވިގެންދިޔައެވެ", -20)], hum=True)
sh(17, "From her throat came a heavy, terrible voice that seemed to shake the very walls. It was the powerful maarid of the sea.",
   [("low_growl", "އަޑެކެވެ", -20)], hum=True)
sh(18, "But this time it did not scream; instead, after laughing in a sinister way,")
sh(19, "in front of everyone it exposed Ghassan's deceit. \"You're all blind! You think this is someone trying to save you, don't you?\"")
sh(20, "The terrible spirit spoke through Yamna's tongue. \"I'm the one who has entered this body... I am a maarid! But,")
sh(21, "this deceitful Ghassan sitting in front of you has handed this body to a powerful ifreet through his sihr! Every night he goes into this room alone,")
sh(22, "and through his ifreet he imprisons this girl's body and robs her of her honour!\" At those terrifying words Khalid's and Faarish's blood boiled. But,",
   [("heartbeat", "ކެކިގަތެވެ", -20)], hum=True)
sh(23, "Ghassan at once sped up his murmuring and said harshly: \"This is a big lie the jinn is telling!",
   [("whisper_recite", "ތުންތަޅުވުން", -22)])
sh(24, "It's trying to sow discord among us and lead us astray!\" As Khalid and the others remembered the lies the jinn had told before,")
sh(25, "it was not hard to believe Ghassan's words. \"We won't believe your filthy lies!\" Faarish shouted. With that,")
sh(26, "the jinn in Yamna's body laughed loudly. \"Hmm... last time, when I told you about Aadhanbe, you didn't believe me either, did you?\" it said mockingly.",
   [("low_growl", "ހީނގަތެވެ", -21)])
sh(27, "\"If you want to be sure, go right now to Rannikamagu beach! Even now he is there with a bowl of water with sihr written for this girl,")
sh(28, "ready on the shore to pour that bowl into the sea! Go and see!\" With that sentence a heavy silence fell over the room.",
   hum=True)
sh(29, "Suddenly shock and fear showed on Ghassan's face. The jinn had given them a direct challenge that could not be lied about.",
   [("gasp", "ސިހުމާއި", -22)], hum=True)
sh(30, "Faarish and Khalid looked at each other, to decide whether to go right now and check the truth. With the maarid's direct challenge,")
sh(31, "a deathly silence fell over the room. In Faarish's heart a fire of suspicion flared and his blood boiled.",
   [("heartbeat", "ކެކިގަތެވެ", -22)], hum=True)
sh(32, "Without a moment's delay he glanced at Adheel, and the two of them left the room together and ran at full speed towards Rannikamagu beach.",
   [("door_open", "ނިކުމެ", -20), ("footsteps_sand", "ދުއްވައިގަތެވެ", -18)])
sh(33, "In the pitch darkness of the small hours, apart from the sound of the waves, the whole area was deserted. But as Faarish and Adheel drew near the sand of the beach,",
   [("wave_crash", "ރާޅުތަކުގެ", -20)])
sh(34, "in the faint moonlight, in the shade of a huge tree on the shore, they saw a shadowy figure moving.",
   [("leaves_rustle", "ރުކެއްގެ", -22)], hum=True)
sh(35, "That man wore a checked white sarong and a white shirt, with a white cap on his head. He was sitting on the ground,")
sh(36, "gazing at a strange bowl in his hand, murmuring. He was at the very last stage of pouring a black bowl of sihr water made for Yamna into the sea.",
   [("whisper_recite", "ތުންތަޅުވާށެވެ", -24)])
sh(37, "\"Stop!\" At Faarish's shout, Aadhanbe started and looked behind him. But before he could get up,",
   [("gasp", "ސިހިފައި", -22)])
sh(38, "young Faarish and Adheel ran up and seized him hard. At that moment the bowl slipped from Aadhanbe's hand,",
   [("footsteps_sand", "ދުވެގޮސް", -18), ("soft_thud", "ދޫވެ", -22)])
sh(39, "and the black water in it soaked into the sand. \"Let go... let me go!\" Aadhanbe cried out in his old man's voice, struggling to get free.",
   [("pour", "އޮހޮރިގެންދިޔައެވެ", -22)])
sh(40, "But from the fear on that face, Faarish became one hundred percent certain that this was the sorcerer who had been tormenting Yamna all these days.",
   hum=True)
sh(41, "\"Tonight I'll end your days,\" Faarish said, gritting his teeth. Fearing that Aadhanbe would cry out,")
sh(42, "Adheel at once took the cap from Aadhanbe's head, balled it up and forced it into his mouth. After that,")
sh(43, "the two of them took Aadhanbe, half dragging him, far from the beach to where nobody lived,")
sh(44, "into a house that had been abandoned for a long time. Together, inside that pitch-dark abandoned house,",
   [("creak", "ވެއްދިއެވެ", -20)])
sh(45, "they tied Aadhanbe tightly to a chair with a strong rope and held him captive. That old body had no strength left to defend itself.",
   hum=True)
sh(46, "Faarish stood in front of Aadhanbe and gave him a warning look. \"Tell me now! Why are you doing sihr on my little sister? Who told you to?\"")
sh(47, "There was danger in Faarish's voice. Aadhanbe trembled with fear. Then Adheel pulled the cloth out of his mouth. \"Let me go!",
   [("sob_breath", "ރޫރޫއަޅަމުން", -24)])
sh(48, "For Allah's sake, let me go! I don't do sihr on anyone's innocent child!\" Aadhanbe, in his old,")
sh(49, "trembling voice, begged with tears. \"Just because you lie in the mosque's first row five times a day, am I supposed to believe your filthy lies?")
sh(50, "That's the kind of devils you people are!\" By then Adheel too was so furious his whole body was shaking. The distress afflicting Yamna,")
sh(51, "her terrifying state, he had seen with his own eyes. Whatever was done to a merciless sorcerer who dared inflict such a state on a helpless girl would be no sin, he thought.",
   hum=True)
sh(52, "\"I swear by Allah... I was on the beach because Jaleel asked me to do something so that bait fish would come to the island!\"")
sh(53, "Aadhanbe made one last effort to escape that dangerous captivity. But at that moment Faarish's blood boiled beyond all limits.",
   [("heartbeat", "ކެކިގަތީ", -20)])
sh(54, "His little sister's pained, pleading cries seemed to ring in his ears. Ever since she was tiny, he had been there for every sorrow and hardship she faced.",
   hum=True)
sh(55, "In the sudden rage that came as loving memories of Yamna returned, he picked up a stick lying on the ground,",
   hum=True)
sh(56, "and Faarish struck a powerful blow on Aadhanbe's body. With that, the old man tried to writhe free,",
   [("soft_thud", "އަޅައިފިއެވެ", -22)])
sh(57, "and screamed loudly from the pain. At once Adheel hurriedly took the cap and forced it into his mouth again.")
sh(58, "\"Hey bro... come on, let's go now! We have to check on the others too!\" As Adheel hurriedly reminded him,")
sh(59, "they left the man in that state inside the abandoned house, and the two of them hurried out.",
   [("door_close", "ނިކުތެވެ", -20)])
sh(60, "Through the pitch darkness of the small hours, secretly glancing both ways, they headed home with their hearts in their mouths.",
   [("footsteps_sand", "މިސްރާބުޖެހީ", -22)])
sh(61, "When the two of them got home and came in, Ghassan, having finished his deceitful recitation, was coming out of Yamna's room.",
   [("door_open", "ނިކުންނަނީއެވެ", -20)])
sh(62, "His face showed the look of someone worried about something. \"Well, did you find any proof?\"")
sh(63, "Hiding the unease in his heart, Ghassan wanted to confirm what had happened. \"Yes! We caught him red-handed!\"")
sh(64, "At Faarish's words, Khalid and Saahidha too came out of Yamna's room with a start. Their faces showed extreme anger.",
   [("door_open", "ނިކުތެވެ", -20)])
sh(65, "\"Killing such merciless people would be no sin!\" Saahidha said with hatred, gritting her teeth, her eyes red as blood. \"Where is that Aadhanu now?\"")
sh(66, "Sensing the seriousness of the situation and wanting more details, Khalid asked quickly. \"His deceitful scheme was exposed,")
sh(67, "and having failed, he has now run off screaming,\" Faarish lied, putting on a calm face to hide what they had done in secret. But his heart was pounding hard. (To be continued)",
   [("heartbeat", "ތެޅެމުންދިޔައެވެ", -18)], hum=True)
SHOTS = S

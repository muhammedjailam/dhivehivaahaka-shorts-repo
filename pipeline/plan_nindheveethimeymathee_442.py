"""Beat/shot plan for Nindheveethimeymathee episode 442 (used by plan_beats.py).
Frame: SCHOOL-era Haizum (~48) weeping over Sana's farewell letter. Flashback (PAST): Vietnam business trip,
Haizum (~38) meets his old friend Shifa at a hotel party. No handshake, no arm tap, no touching;
never the two of them in a hotel room (the episode ends inside the lift). Sana appears only as a phone photo."""

HOTEL = "a luxury hotel in Da Nang, Vietnam"
LOC = {
    "song": "a rain-streaked window of a quiet Malé apartment at night, a cloudy moon over the dark lagoon beyond, on the windowsill a folded ivory headscarf and a small vase with a single wilted white flower",
    "sana_room": "late Sana's quiet bedroom in a Malé apartment at night: a cushioned armchair by a rain-streaked window, a small side table with a warm lamp, a folded ivory headscarf on the arm of the chair, sheer curtains, a wooden wardrobe in shadow",
    "skyline": f"the night skyline of Da Nang, Vietnam: {HOTEL} tower glowing with warm windows beside a wide river, a lit bridge reflected in the water, palm trees along the riverside promenade",
    "stairs": f"the grand curved marble staircase of {HOTEL} at night, polished brass railing, a crystal chandelier, tall potted palms, warm golden light, the open doors of a ballroom at the foot of the stairs",
    "hall": f"the large ballroom of {HOTEL} during a formal business reception at night: round tables with white cloths, crystal chandeliers, guests in formal wear, waiters with trays of juice glasses, tall glass doors open onto a pool terrace",
    "pool": f"the poolside dining terrace of {HOTEL} at night: small round tables with white cloths and candles beside a large illuminated turquoise swimming pool with calm empty water, palm trees with fairy lights, the ballroom glowing behind tall glass doors",
    "buffet": f"the long buffet counter in the ballroom of {HOTEL} at night: silver chafing dishes, bowls of pasta and salads, small blank white label cards with no writing, stacks of white plates, warm golden light",
    "corridor": f"a quiet carpeted corridor off the ballroom of {HOTEL} at night: warm wall sconces, dark wood panelling, a plain unmarked wooden door, a tall potted palm",
    "lift_lobby": f"the lift lobby of {HOTEL} at night: polished marble floor, two brass lift doors, one standing open with warm light inside, a tall vase of white orchids",
    "lift": f"the inside of a spacious mirrored hotel lift of {HOTEL} at night: brass handrails, warm ceiling light, polished wood panels, the closed brass doors",
}
MEM = "soft hazy dreamlike memory glow, "
MOOD = {
    "song": "late rainy night, deep indigo and sapphire-blue moonlight through rain streaks, one faint warm amber glow, melancholic and aching",
    "sana_room": "late night, heavy rain outside, a single warm amber lamp against deep blue shadows, grief and regret, quiet and heavy",
    "skyline": MEM + "warm summer night, clear sky, city lights shimmering on the river, a sense of the past",
    "stairs": MEM + "evening, warm golden chandelier light, elegant and festive, tender",
    "hall": MEM + "night, warm golden chandelier light and festive murmur, a lively crowd, a moment of surprise",
    "pool": MEM + "warm tropical night, clear sky, turquoise pool glow on faces, warm candlelight, relaxed and cheerful",
    "buffet": MEM + "night, warm golden light over the buffet, light-hearted and playful",
    "corridor": MEM + "night, warm dim sconce light, an awkward, slightly uneasy quiet",
    "lift_lobby": MEM + "late night, warm golden light on marble, a quiet hush away from the party",
    "lift": MEM + "late night, warm soft ceiling light, playful laughter with an undercurrent of unease",
}

H38 = "Haizum younger, about 38, beard fully black, no grey"
H38_STAINED = H38 + ", brownish soup stains splashed across his navy sleeve and white shirt front"
SHIFA_STAINED = "Shifa in her loose long-sleeved ankle-length white dress and pale-gold hijab fully covering her hair and neck, brownish soup and food stains spread across the front of her white dress"

BEATS = [
    # --- opening song ---
    dict(to=5, reason="episode opening: the sung lament over a rainy night — symbolic image of lost love", loc="song",
         visual="close view of a rain-streaked window at night, raindrops glinting like pearls on the glass, a cloudy moon over the dark lagoon outside; on the windowsill a folded ivory headscarf and a small vase holding a single wilting white flower; no people",
         camera="medium close-up, the moon and window in the upper two-thirds, the windowsill as a calm lower third",
         amb="rain_night", sens="other", safe="song lyrics mention lying in bed together and wounds: shown only as a rainy window, a folded scarf and a wilting flower"),
    # --- present frame (SCHOOL-era Haizum ~48) ---
    dict(to=7, reason="scene change: the frame story — Haizum reads Sana's farewell letter", chars=["haizum"], loc="sana_room",
         visual="Haizum, about 48, grey flecks in his trimmed beard and at his temples, in a plain dark-grey long-sleeved shirt, sitting hunched in the armchair by the rainy window, holding a handwritten letter of two pale pages in both hands, his red eyes reading it, lips pressed together; the pages show only soft illegible faded lines; a folded ivory headscarf on the arm of the chair",
         camera="medium close-up from slightly above his shoulder, his face in the upper third, the letter in the middle, his lap in soft shadow below",
         amb="apartment_rain_night", sens="other", safe="letter shown only as soft illegible lines; Sana's death only implied, she is not shown"),
    dict(to=10, reason="emotional turning point: he breaks down and presses the letter to his chest", chars=["haizum"], loc="sana_room",
         visual="Haizum, about 48, grey flecks in his trimmed beard, in a plain dark-grey long-sleeved shirt, sitting in the armchair, head bowed, eyes shut, tears running down his cheeks, pressing the folded letter flat against his chest with both hands; the warm lamp beside him and the rain-streaked window behind",
         camera="medium shot, eye level, his face in the upper third, the dark carpet as a calm lower third", amb="apartment_rain_night"),
    # --- flashback: Vietnam (PAST) ---
    dict(to=12, reason="time jump: flashback to the business trip to Vietnam years ago", loc="skyline",
         visual="the night skyline of Da Nang seen from across the river: a tall luxury hotel tower glowing with warm windows, a lit bridge and city lights reflected in the calm river, palm trees along the promenade; no people in focus",
         camera="wide establishing shot, the hotel tower and sky in the upper two-thirds, the dark rippling river as the lower third",
         amb="city_night_far", transition="dissolve"),
    dict(to=17, reason="scene change: the third night — Haizum comes down the hotel staircase talking to pregnant Sana on the phone", chars=["haizum"], loc="stairs",
         visual=f"{H38}, in his dark-navy suit and white open-collar shirt, walking down the grand curved staircase with one hand on the brass railing and his phone held to his ear, a soft tender smile, eyes lowered as he listens; the open ballroom doors glowing below",
         camera="medium wide, slightly low angle from the foot of the stairs, his face in the upper half, the marble steps as the lower third", amb="hotel_hall"),
    dict(to=20, reason="action change: the loving goodbye and the end of the call", chars=["haizum"], loc="stairs",
         visual=f"{H38}, in his dark-navy suit, standing at the foot of the staircase near the ballroom doors, the phone pressed to his ear, eyes closed, a warm loving smile, his other hand in his trouser pocket",
         camera="medium close-up, eye level, his face in the upper third, the polished floor and blurred chandelier light below", amb="hotel_hall",
         sens="intimacy", safe="married couple's 'love you' and phone kiss shown only as a tender smile with closed eyes; the wife is not visible"),
    dict(to=23, reason="scene and character change: entering the ballroom he recognises a familiar face", chars=["haizum", "shifa"], loc="hall",
         visual=f"{H38}, in his dark-navy suit, stopped mid-step inside the busy ballroom, half turned back, looking with a surprised slow smile towards a small group of young women in modest long dresses and hijabs standing by a round table; among them Shifa in her white dress and pale-gold hijab, a few metres away from him; Shifa appears only once in the image; all other guests and the other women wear dark or coloured clothes (navy, maroon, emerald, plum) with dark or coloured hijabs, no other woman in white or gold",
         camera="medium wide, eye level, faces in the upper half, the patterned carpet as the lower third", amb="hall_crowd"),
    dict(to=27, reason="action change: Shifa recognises him — a happy greeting from a respectful distance", chars=["shifa", "haizum"], loc="hall",
         visual=f"Shifa, in her loose white dress and pale-gold hijab, smiling brightly in delighted surprise, her right hand placed on her chest in greeting; {H38}, in his dark-navy suit, smiling back with his own hand on his chest, his hair and beard jet-black without any grey, standing clearly more than an arm's length apart, not touching; the chandelier-lit ballroom behind them",
         camera="medium two-shot, eye level, both faces in the upper half", amb="hall_crowd",
         sens="intimacy", safe="the narration's handshake is replaced by a polite hand-on-heart greeting at a distance; no contact"),
    dict(to=29, reason="location change: they sit at a table beside the big swimming pool", chars=["haizum", "shifa"], loc="pool",
         visual=f"{H38}, in his dark-navy suit, and Shifa in her white dress and pale-gold hijab sitting on opposite sides of a small round candle-lit table beside the large illuminated pool, chatting and smiling; two empty glasses on the white cloth; the calm empty turquoise water and palm trees behind them",
         camera="medium wide, eye level, faces in the upper half, the pool edge and tiles as a calm lower third", amb="resort_evening",
         sens="other", safe="pool shown calm and empty, no swimmers"),
    dict(to=34, reason="location and action change: choosing food at the buffet", chars=["shifa", "haizum"], loc="buffet",
         visual=f"Shifa, in her white dress and pale-gold hijab, holding an empty white plate, leaning to peer doubtfully at the small blank label cards in front of the silver dishes; {H38}, in his dark-navy suit, a step away holding a plate of pasta with a little salad, watching her with an amused grin",
         camera="medium shot, eye level, faces in the upper half, the buffet counter as the lower third", amb="hotel_hall",
         sens="other", safe="food labels shown as blank cards, no text"),
    dict(to=39, reason="location and action change: back at the poolside table, eating and talking; Shifa jokes about her husband", chars=["shifa", "haizum"], loc="pool",
         visual=f"Shifa, in her white dress and pale-gold hijab, sitting at the candle-lit poolside table with a plate holding only a little salad, talking animatedly with expressive hands and a playful pulled face; {H38}, in his dark-navy suit, sitting across the table with a plate of pasta, laughing; glasses of orange juice on the table; the empty illuminated pool behind",
         camera="medium two-shot from the side of the table, faces in the upper half, the white tablecloth as the lower third", amb="resort_evening"),
    dict(to=42, reason="focus change: Haizum laughs and shrugs with his juice while the narration recalls their tuition-days friendship", chars=["haizum"], loc="pool",
         visual=f"{H38}, in his dark-navy suit, sitting at the poolside table laughing heartily with a little shrug, raising a glass of orange juice to his lips, his short hair and trimmed beard jet-black without a single grey hair, looking younger than his reference; a plate of pasta in front of him; across the table only the soft edge of a white sleeve; turquoise pool light flickering on his face",
         camera="medium close-up, eye level, his face in the upper third, the tablecloth and plate below", amb="resort_evening",
         sens="other", safe="party drinks are orange juice only"),
    dict(to=47, reuse="beat_012", reason="return to the same table moment: he answers her questions about his wife and children", loc="pool",
         visual="(reuse)", amb="resort_evening"),
    dict(to=50, reason="detail: the family photos on his phone — Sana and the children", chars=["sana"], loc="pool",
         visual="close-up of a man's hand in a dark-navy suit sleeve holding a phone across a candle-lit table; on the screen a soft warm family photo: Sana in her sage-green dress and ivory hijab smiling gently with a boy and a girl beside her, slightly soft-focus; no text or icons on the screen; the turquoise pool glow blurred in the background",
         camera="close-up, the phone in the upper-middle of the frame, the white tablecloth as the calm lower third", amb="resort_evening",
         sens="other", safe="Sana appears only inside a phone photo; no readable text or interface on the screen"),
    dict(to=51, reuse="beat_011", reason="return to the table two-shot: Shifa's warm 'Mashallah' and his thanks", loc="pool",
         visual="(reuse)", amb="resort_evening"),
    dict(to=56, reason="action change: a guest bumps a waiter and the tray of soup spills on them", chars=["haizum", "shifa"], loc="pool",
         visual=f"the poolside table at the moment after a spill: a waiter in a white jacket with an empty tilted silver tray, an embarrassed guest in a grey suit apologising with raised palms; {H38_STAINED}, jumping up from his chair, staring down at his sleeve; {SHIFA_STAINED}, also on her feet a step away, a hand over her nose and mouth, grimacing at the smell; spilled soup and a toppled bowl on the white tablecloth",
         camera="medium wide, eye level, faces in the upper half, the tablecloth and floor as the lower third", amb="resort_evening",
         sens="other", safe="lukewarm soup only — no burns, no injury; nausea shown as a hand over the nose, no vomiting"),
    dict(to=58, reason="location change: he waits worried in the corridor outside the ladies' restroom", chars=["haizum"], loc="corridor",
         visual=f"{H38_STAINED}, standing in the quiet corridor beside a plain closed wooden door, holding a folded white napkin, glancing at the door with a worried frown",
         camera="medium shot, eye level, his face in the upper third, the carpet as the lower third", amb="hotel_hall",
         sens="other", safe="the restroom itself is never shown; only a closed unmarked door"),
    dict(to=63, reason="character enters: Shifa comes out dismayed in her ruined dress; he offers to have it laundered", chars=["shifa", "haizum"], loc="corridor",
         visual=f"{SHIFA_STAINED}, standing in the corridor looking down at her ruined dress with a dismayed pout, holding the skirt slightly away from her with two fingers; {H38_STAINED}, standing well apart from her, gesturing reassuringly towards the far end of the corridor while explaining",
         camera="medium two-shot, eye level, faces in the upper half, the carpet as the lower third", amb="hotel_hall",
         sens="clothing", safe="the narration's short white dress is shown as Shifa's long loose white dress and pale-gold hijab"),
    dict(to=66, reason="action change: she texts her companions to leave without her", chars=["shifa", "haizum"], loc="corridor",
         visual=f"{SHIFA_STAINED}, a small handbag on her arm, typing on her phone with both thumbs, its soft glow on her face, the screen not visible; {H38_STAINED}, a few steps away, glancing back towards the ballroom with a brief nod",
         camera="medium shot, eye level, her face in the upper third", amb="hotel_hall",
         sens="other", safe="phone shown only as a glow; no readable screen"),
    dict(to=70, reason="location change: they walk to the lift and step in", chars=["haizum", "shifa"], loc="lift_lobby",
         visual=f"{H38_STAINED}, and {SHIFA_STAINED}, walking side by side but an arm's length apart across the marble lift lobby towards an open brass lift door, Shifa smiling brightly as she asks a question, Haizum answering with a grin",
         camera="medium wide, from behind and to the side, faces in the upper half, the polished marble floor as the lower third", amb="hotel_room",
         sens="other", safe="they only take the lift; no hotel-room scene with both of them is shown"),
    dict(to=75, reason="location change: inside the lift — laughter about Daniyal's six children", chars=["shifa", "haizum"], loc="lift",
         visual=f"inside the mirrored lift, {SHIFA_STAINED}, standing against the left wall with one hand over her mouth, eyes wide, laughing in astonishment; {H38_STAINED}, standing against the opposite right wall, grinning teasingly; a wide empty space of floor between them",
         camera="medium wide, eye level, faces in the upper half, the empty polished floor between them as the lower third", amb="hotel_room",
         sens="intimacy", safe="they stand at opposite sides of the lift, no contact"),
    dict(to=79, reason="action change: she blushes about her childhood crush, sniffs her dress again and grimaces", chars=["shifa", "haizum"], loc="lift",
         visual=f"inside the mirrored lift, {SHIFA_STAINED}, at the left wall, blushing and wrinkling her nose as she lifts the stained sleeve towards her face to sniff it; {H38_STAINED}, at the opposite right wall, laughing at her with his head tipped back; the space between them clear",
         camera="medium shot, eye level, faces in the upper half", amb="hotel_room",
         sens="intimacy", safe="the narration's playful tap on his arm is omitted; they stay at opposite walls; the lift doors stay closed and the episode ends there"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "[Song] \"Is it you who goes away now, without looking back... the heart I hurt has no complaint, because no one listens...")
sh(2, "...it began to ache, deep within the heart; hand on it, I lay; my eyes grew wet... was this love you gave, with all its pain...")
sh(3, "...to have you, I emptied this heart, made so many vows and promises; the moon risen in the sky is witness to this...")
sh(4, "...lying in bed together we watched dreams, exchanged them together; the wounds that wounded my heart, the pain is still there...")
sh(5, "...pearl-like drops are flowing; there is no one to tell my heart's many grievances, to care for me; loneliness, memories remain...\"")
sh(6, "\"...loyalty broken — where was my fault? Tell me...\" A heart that gave loyalty only to be sold. \"Do not be lonely in a world without me.")
sh(7, "Haizum, you spent most of your life in loneliness. My wish is that you find a partner of good character and honesty, who will love Haizum and our children without any conditions.")
sh(8, "I always wish you a prosperous, happy life.\" Tears flowed uncontrollably from Haizum's eyes. He pressed the letter hard against his chest.",
   [("sob_breath", "ކަރުނަތައް", -24), ("paper_shuffle", "ޖައްސައި", -22)], hum=True)
sh(9, "It was he himself who had broken the heart of his own loving wife. That was a past that would never be erased from his memory. The punishment for the one mistake he made —",
   hum=True)
sh(10, "he had never imagined it would become a poison he would have to drink for the rest of his life. Because of Sana's farewell letter, the pages of a bitter past buried deep in his heart began to stir again.",
   hum=True)
sh(11, "With the memories of Sana he closed his eyes. It was the trip Haizum made to Vietnam for a business meeting.",
   [("sigh", "މަރައިލެވުނެވެ", -24)])
sh(12, "The first two days of that four-day trip were spent in meetings. The third night was a night with a formal reception held to strengthen ties between the partners.")
sh(13, "The party was arranged in the big hall of the hotel where they were staying. All dressed up, Haizum came downstairs talking on the phone with Sana.",
   [("footsteps_pavement", "ފޭބީ", -24)])
sh(14, "\"What time did you get the appointment?\" Haizum asked. \"Half past six. Mum will come to take me.")
sh(15, "But I feel so uneasy having to go for the scan without Haizum for the first time.\" There was worry in Sana's voice. \"Don't worry.")
sh(16, "My heart is always with you. Send me a video of the scan. If I didn't have to go to this party tonight,")
sh(17, "I'd have looked at our baby right away on a video call too. But the friends insist so much that I can't not go.\"")
sh(18, "Haizum said in a disappointed tone. \"That's fine. Just hearing you say that has calmed my heart. I'll send the video.")
sh(19, "I'll hang up now, OK? Love you, miss you,\" Sana said. \"Love you too. Miss you too.\"")
sh(20, "With words full of love Haizum kissed the phone. \"Take good care of yourself. Bye, love you.\" After hanging up the phone,")
sh(21, "Haizum went into the hall to look for his friends. Just then, as he passed a spot where a group of young women were standing,")
sh(22, "his steps slowed. There he saw a very familiar face, one he knew. He stepped back,")
sh(23, "and as he looked properly in that direction, a light smile came onto Haizum's lips. \"Shifa... is it?\" Haizum asked, in a tone of disbelief.")
sh(24, "\"Hey, Haizum!\" On Shifa's face too appeared a smile of surprise and joy.")
sh(25, "Without thinking she held out her hand to greet him. Haizum too took his right hand out of his pocket and, with a smile, greeted Shifa.")
sh(26, "\"It's been so long since I've seen you. Where are you living now?\" Haizum asked, a light smile on his lips.")
sh(27, "\"I got married and moved to Australia. And now here I am again, out looking for a stone to drop anchor on,\" Shifa said jokingly. \"Why's that?\"")
sh(28, "Talking with Shifa, Haizum walked towards a table. And he sat down at one of the tables set beside the big swimming pool that lay in open view.")
sh(29, "\"How about we go and get some food?\" Shifa asked. \"That's exactly right, come on!\" Haizum too got up and headed towards the buffet.",
   [("cloth_rustle", "ތެދުވެގެން", -24)])
sh(30, "And after picking up a plate he handed it to Shifa. Though Shifa took the plate, her gaze was fixed on the name cards of the dishes.",
   [("cup_clatter", "ތައްޓެއް", -24)])
sh(31, "Haizum too took another plate and looked over the area where the food was laid out. Usually what he ate there was pasta.")
sh(32, "So after putting in some pasta, with a little salad on one side of the plate, he waited until Shifa finished. \"Shifa, still not done?\"")
sh(33, "Haizum asked. \"What can I do? Not just anything goes down this mouth. That's my problem. And the problem between me and Ille is this too —")
sh(34, "food.\" Shifa said. \"Only food?\" Haizum asked jokingly. Shifa started to laugh.")
sh(35, "And after looking hard at the food, all she put on her plate was a bit of salad. After that she went with Haizum, sat at the table, and they carried on eating as they talked.")
sh(36, "\"After all that looking, all you took was a bit of salad,\" Haizum said. Shifa started to laugh. That was always her way.")
sh(37, "\"So tell me, what happened?\" Haizum asked again. \"Ille wouldn't agree to me going to work.")
sh(38, "Haizum, you know I'd never want to sit at home without a job. I'm someone who loves being social, being with people.")
sh(39, "So how am I supposed to sit locked up at home looking after kids, right?\" Shifa talked in a playful tone, pulling faces and gesturing with her hands.")
sh(40, "Haizum laughed out loud. And shrugging both shoulders he picked up his juice glass and sipped it. Shifa was always someone who never held back in talking,",
   [("cup_clatter", "ޖޫސްތަށި", -24)])
sh(41, "a girl with a sharp tongue and a temper that never wanted to give in. Haizum and Shifa had gone to tuition with the same teacher.")
sh(42, "From those days on the two of them were close friends. After Shifa went to Malaysia to study for her degree, there had been no news at all until this meeting just now.")
sh(43, "So surely Shifa had many things in her heart she wanted to tell. \"Where's your wife?\" Shifa asked. \"She's fine.")
sh(44, "She's unwell, so I didn't bring her on this trip,\" Haizum replied. \"I saw the wedding photos on Facebook. First kid?\" Shifa asked again.")
sh(45, "\"No, there are two kids. The third one is on the way now,\" Haizum said in a happy tone. \"I asked because I never saw any photos of the children.\"")
sh(46, "Shifa said, looking at Haizum. \"Yes... we don't put the children's photos on social media.")
sh(47, "Mum doesn't really approve, so my wife respected that too,\" Haizum replied. \"So you won't show me either?\" Shifa asked.")
sh(48, "\"No... of course I'll show you, Shifa.\" Saying this, Haizum took out his phone and showed her photos of Laira and Lail.")
sh(49, "Shifa looked at the photo eagerly. \"This is my prince, Lail. And this is my princess, my life, Laira.")
sh(50, "And this is my beloved wife, Sana. This is my whole world.\" As he proudly introduced his family, a happy smile spread across Haizum's face.",
   hum=True)
sh(51, "Seeing that, a lovely smile came onto Shifa's lips too. \"Mashallah, such a lovely family!\" Shifa praised. \"Thank you.\"")
sh(52, "Haizum said, putting the phone in his pocket. At that moment a man getting up from a nearby table bumped into a waiter passing by.",
   [("soft_thud", "ޖެހިގަތެވެ", -18)])
sh(53, "With that, the tray in the waiter's hand tipped over straight onto Shifa and Haizum. Startled, both of them jumped to their feet at once.",
   [("crash_clatter", "ބަންޑުންވެގެން", -14), ("gasp", "ސިހުމާއެކު", -20)])
sh(54, "On that tray were soup and all kinds of food. \"I'm terribly sorry, sir!\" the man who had got up from the table apologised in a panic.")
sh(55, "And he apologised to the waiter too. Haizum said nothing and looked down at his clothes.")
sh(56, "As Shifa smelled what had splashed on her, she began to gag at the foul smell.",
   [("breath", "އޯކާދެމެން", -22)])
sh(57, "Haizum too, after smelling his hand, felt sick and quickly stepped away from there. Shifa went almost running to the ladies' restroom.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(58, "And, still gagging, she tried as best she could to clean her dress. When she came out of the restroom, Haizum was waiting outside, worried.",
   [("door_open", "ނިކުތްއިރު", -22)])
sh(59, "\"How am I even going to go anywhere with this smell?\" Shifa said, dismayed. \"Aren't you staying at this hotel, Shifa?\" Haizum asked. \"No,")
sh(60, "this is a business trip. I came here because I was invited to a dinner.\" Shifa looked down at her dress.")
sh(61, "Her white dress was completely ruined, stained with the colours of food and soup. \"Come with me. We'll send the dress to the laundry.")
sh(62, "The laundry service here is very fast. Wear something else and wait until the dress comes back. Once it's back I'll drop you at your hotel.")
sh(63, "How does that sound?\" Haizum suggested. \"Perfect. If I don't get away from this smell I might just throw up.\"")
sh(64, "Pulling a face, Shifa agreed. Then she took her phone out of her handbag and sent someone a message.",
   [("phone_game_taps", "މެސެޖެއް", -24)])
sh(65, "\"I texted them to go if I'm late, in case they look for me not knowing where I am,\" Shifa said, putting the phone back in her bag. \"Hmm.\"")
sh(66, "Haizum said briefly. \"I still have to go back there too. Daniyal and the others haven't even seen me yet.\"")
sh(67, "Talking, the two of them walked towards the lift. Even then Shifa was struggling, feeling sick. \"Is Daniyal here too?\"",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(68, "Shifa asked with a happy smile. \"Yes, Jimmy and Vildhaan are here too,\" Haizum replied, stepping into the lift.",
   [("lift_ding", "ލިފްޓަށް", -18)])
sh(69, "\"I'll have to change and meet everyone. It's been so long since I saw the whole group,\" Shifa said. \"You're the one who ran away,")
sh(70, "so what's there to say?\" Haizum said. \"So tell me, is Daniyal married?\" Shifa asked, pretending not to care.")
sh(71, "At that Haizum laughed out loud. \"After all this time, would he still be unmarried? Is that even a question to ask! Yes, he's married.")
sh(72, "He got married before me. He has six kids now,\" Haizum said. \"Oh my God! Seriously? Did he marry a Japanese fish?\"",
   [("gasp", "މާތްކަލާކޯ", -22)])
sh(73, "Shifa asked, laughing with a hand over her mouth. \"All three times they had twins. So of course they multiplied fast,\" Haizum said, laughing.")
sh(74, "\"Lucky that didn't happen to me — got any photos?\" Shifa asked eagerly. \"Hmm. When you meet him, look straight on Daniyal's phone.")
sh(75, "That'll be much better. Maybe the past between you two as well,\" Haizum teased with a mischievous smile. \"Haizum, you're so mean.")
sh(76, "That was a childhood thing,\" Shifa said shyly. \"You're still just like a little kid.")
sh(77, "That's exactly why you flare up at every little thing,\" Haizum said, laughing. Laughing too, Shifa sniffed her dress again.")
sh(78, "And again she felt sick. \"Lucky it wasn't something hot,\" Shifa said. \"Truly lucky.")
sh(79, "Otherwise the two of us would have had to go to the hospital tonight,\" Haizum said.")
SHOTS = S

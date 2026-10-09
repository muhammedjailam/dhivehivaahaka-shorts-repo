"""Beat/shot plan for Hayaath episode 415 (used by plan_beats.py)."""

LOC = {
    "beach_night": "a secluded Maldivian beach at night, white sand, gentle small waves, coconut palms leaning over the shore, a full moon over the dark lagoon",
    "memory_beach": "the same secluded Maldivian beach in golden late-afternoon light, turquoise shallow lagoon, white sand, coconut palms",
    "fazaal_room_night": "a spacious room in a large old two-storey house on a Maldivian island at night, dark wooden furniture, tall windows with sheer curtains, a single table lamp",
    "house_gate": "the gate and sandy front yard of an old Maldivian coral-stone house on a narrow sandy island lane at night, a low white-washed coral wall, a wooden gate, a single streetlight",
    "maaroof_door": "the closed wooden front door of a modest Maldivian house at night, dark shuttered windows, a small porch step, a narrow sandy lane, one dim streetlight",
    "street": "a narrow island town street at night in the Maldives, warm streetlights, low walled houses, coconut palms, deserted",
    "car": "inside a dark grey sedan parked on a quiet island road at night, streetlights outside the windscreen",
    "sitting_room": "the sitting room of an old Maldivian coral-stone house at night, a worn fabric sofa, a low wooden coffee table in front of it, a wooden wall shelf with ornaments, a terrazzo floor, a short corridor leading to bedroom doors",
    "glass_floor": "the terrazzo floor of a dim sitting room at night beside the legs of a low wooden coffee table",
    "bedroom_night": "Hayaathu's small plain bedroom in an old Maldivian coral-stone house at night, a single bed with a simple cotton sheet, a wooden louvered window, a ceiling fan, a plain wooden door",
    "areesha_room": "a better-furnished bedroom in the same old house at night, a large bed with a floral bedspread, a dressing table with a mirror, warm lamp light, the door ajar",
}
MOOD = {
    "beach_night": "night, silver moonlight, soft blue shadows, quiet, melancholic and tender",
    "memory_beach": "warm golden late-afternoon light, soft haze, happy, nostalgic, slightly dreamlike",
    "fazaal_room_night": "night, single warm lamp, deep shadows, guarded and bitter",
    "house_gate": "night, one warm streetlight, deep blue shadows, tense",
    "maaroof_door": "late night, dim streetlight, cold blue shadows, lonely and desperate",
    "street": "night, warm sodium streetlights, blue shadows, empty and lonely",
    "car": "night, dark car interior, streetlight glow through the windscreen, watchful",
    "sitting_room": "night, harsh overhead light and deep shadows, frightening, chaotic",
    "glass_floor": "night, cold harsh light glinting on glass, shock",
    "bedroom_night": "night, dim warm bedside lamp, intimate sadness",
    "areesha_room": "night, warm lamp light, cosy but cold-hearted",
}

BEATS = [
    # ---------------- the beach at night after the ring ceremony ----------------
    dict(to=3, reason="new episode opening: Fazaal and Hayaathu on the moonlit beach after the ring ceremony", chars=["young_driver", "hayaathu"], loc="beach_night",
         visual="Fazaal standing a few metres behind Hayaathu on the moonlit sand, gazing at her tenderly; Hayaathu stands silently at the water's edge with her back half turned, looking far out over the dark lagoon",
         camera="wide shot, eye level, from behind Fazaal's shoulder", amb="beach_night"),
    dict(to=6, reason="action change: Fazaal walks up close and sees she is crying", chars=["hayaathu", "young_driver"], loc="beach_night",
         visual="Fazaal standing beside Hayaathu at a respectful arm's-length distance, turned towards her with a gentle concerned face; Hayaathu looking out at the sea with tears glistening on her cheeks, not looking at him",
         camera="medium two-shot, slight low angle, moon behind them", amb="beach_night"),
    dict(to=9, reason="flashback: happy moments with Maaroof on this same beach", chars=["hayaathu", "maaroof"], loc="memory_beach",
         visual="Hayaathu and Maaroof walking slowly side by side along the shoreline at a respectful distance, both smiling, footprints in the wet sand, golden light",
         camera="wide shot, eye level", amb="memory", transition="dissolve"),
    dict(to=15, reason="flashback continues: the conversation about Waheed's three-million-rufiyaa price", chars=["maaroof", "hayaathu"], loc="memory_beach",
         visual="Maaroof standing facing Hayaathu at a respectful distance on the sand, smiling with gentle mockery and talking with an open hand gesture; Hayaathu looking at him in surprise",
         camera="medium two-shot, eye level", amb="memory", sens="intimacy",
         safe="Maaroof touching her cheek is not shown; they stand apart, only his loving smile carries the moment"),
    dict(to=18, reason="action change: Maaroof slips into the sea and the playful chase", chars=["hayaathu", "maaroof"], loc="memory_beach",
         visual="Hayaathu running away along the sand laughing, her rose dress and hijab fluttering, while far behind her Maaroof, fully dressed in his opaque white long-sleeved shirt buttoned to the collar and dark trousers, with only his trouser hems splashed, steps out of the ankle-deep shallows laughing and starts to run",
         camera="wide shot, low angle along the shoreline", amb="memory"),
    dict(to=20, reason="back to the present: Fazaal watches her smile at the memory", chars=["hayaathu", "young_driver"], loc="beach_night",
         visual="close-up of Hayaathu's moonlit face, a faint wistful smile through drying tears, eyes on the sea; Fazaal's profile softly out of focus at the edge of the frame watching her",
         camera="close-up, shallow depth of field", amb="beach_night", transition="dissolve"),
    dict(to=23, reason="action change: he reaches for her hand, she closes her eyes and withdraws", chars=["hayaathu", "young_driver"], loc="beach_night",
         visual="Hayaathu with her eyes tightly shut, drawing her own hands together against her chest and turning slightly away; Fazaal standing a step away, his hand lowered, looking at her quietly",
         camera="medium close two-shot", amb="beach_night", sens="intimacy",
         safe="taking her hand (engaged, not married) is not shown; she holds her own hands to her chest, a clear gap between them"),
    dict(to=27, reason="emotional turning point: Hayaathu tells him her heart belongs to someone else", chars=["hayaathu"], loc="beach_night",
         visual="Hayaathu facing the camera with the moonlit sea behind her, speaking with a firm trembling chin while tears run down her cheeks, hands clasped tightly in front of her",
         camera="medium close-up, eye level", amb="beach_night"),
    dict(to=30, reason="focus change: Fazaal answers 'I too marry under compulsion'", chars=["young_driver"], loc="beach_night",
         visual="close-up of Fazaal in moonlight, serious steady eyes fixed on someone just out of frame, a softly blurred pink hijab at the edge of the frame",
         camera="close-up over her shoulder", amb="beach_night"),
    dict(to=33, reason="framing change: both lost in their own thoughts", chars=["young_driver", "hayaathu"], loc="beach_night",
         visual="two small figures standing apart on the moonlit beach, both looking out at the moon over the lagoon, a wide stretch of silver sand between them, Fazaal with a faint smile",
         camera="extreme wide shot, from behind", amb="beach_night"),
    dict(to=38, reason="reflection/flashback: Fazaal's past distrust of women", chars=["young_driver"], loc="fazaal_room_night",
         visual="Fazaal alone in a dim room at night sitting in an armchair, looking down at a smartphone in his hand (screen facing away from the viewer, softly glowing), his face cold, guarded and cynical",
         camera="medium shot, slightly high angle", amb="room_night", transition="dissolve"),
    dict(to=39, reason="back on the beach (reuse): he has found the girl he wished for", reuse="beat_006", chars=["hayaathu", "young_driver"], loc="beach_night",
         visual="(reuse) Hayaathu's moonlit face, Fazaal watching", amb="beach_night", transition="dissolve"),
    # ---------------- that night: Hayaathu runs to Maaroof's house ----------------
    dict(to=41, reason="time/scene change: dropped home, she slips back out", chars=["hayaathu"], loc="house_gate",
         visual="Hayaathu stepping back out through the wooden gate of the old coral-stone house, glancing anxiously both ways down the dark empty lane, the red tail lights of a car disappearing at the far end",
         camera="medium wide shot, eye level", amb="night_exterior", transition="black"),
    dict(to=44, reason="scene change: at Maaroof's door, knocking with no answer", chars=["hayaathu"], loc="maaroof_door",
         visual="Hayaathu at the closed wooden front door of a dark silent house, one hand raised knocking, breathless, tears on her face, the windows all dark",
         camera="medium shot, from the side", amb="street_night"),
    dict(to=46, reason="action change: Dhooma calls, she answers in tears", chars=["hayaathu"], loc="maaroof_door",
         visual="Hayaathu sitting on the porch step of the dark house, holding a phone to her ear with a trembling hand, crying, leaning her head against the closed door",
         camera="close-up", amb="street_night"),
    dict(to=48, reason="action change: she walks home in despair", chars=["hayaathu"], loc="street",
         visual="Hayaathu walking alone down the empty night street under the streetlights, head bowed, shoulders hunched, a phone held loosely in her hand",
         camera="wide shot, eye level, from in front", amb="street_night"),
    dict(to=50, reason="character change: Fazaal was watching from his parked car", chars=["young_driver"], loc="car",
         visual="Fazaal in the driver's seat of his dark parked car, hand on the ignition, watching through the windscreen with a faint knowing smile, a small distant female figure walking away under a streetlight",
         camera="medium shot from the passenger seat", amb="car_night"),
    dict(to=53, reason="action change: he follows her silently", chars=["hayaathu"], loc="street",
         visual="a small lone figure of a young woman in a rose dress and pink hijab walking under the streetlights, and far behind her a dark grey sedan creeping slowly with dimmed headlights",
         camera="high wide shot", amb="street_night"),
    dict(to=57, reason="framing change: Fazaal's possessive resolve (the message he read)", chars=["young_driver"], loc="car",
         visual="close-up profile of Fazaal at the steering wheel, jaw set, eyes fixed intently ahead, streetlight sliding across his face, determined and possessive",
         camera="close-up profile", amb="car_night"),
    # ---------------- home: Areesha's mockery ----------------
    dict(to=59, reason="scene change: home, Areesha blocks her way", chars=["areesha", "hayaathu"], loc="sitting_room",
         visual="Areesha springing up from the sofa with a smartphone in hand and stepping into Hayaathu's path with a mocking grin; Hayaathu stopped in the middle of the sitting room, head down",
         camera="medium wide shot", amb="living_night"),
    dict(to=61, reason="emotional turn: Hayaathu's red swollen eyes stop Areesha", chars=["hayaathu", "areesha"], loc="sitting_room",
         visual="close-up of Hayaathu's face, eyes red and swollen from crying, fresh tears on her cheeks; behind her, out of focus, Areesha's smirk faltering",
         camera="close-up", amb="living_night"),
    dict(to=66, reason="action change: Areesha taunts her about the 'ugly prince'", chars=["areesha", "hayaathu"], loc="sitting_room",
         visual="Areesha standing with arms crossed and a poisonous laugh, head tilted; Hayaathu half turned away towards the bedroom corridor, stopped mid-step, tears falling",
         camera="medium two-shot", amb="living_night"),
    dict(to=68, reason="scene change: in her room, Dhooma has been waiting", chars=["dhooma", "hayaathu"], loc="bedroom_night",
         visual="Dhooma in her wheelchair in the bedroom looking up anxiously as Hayaathu shuts the door behind her with her back against it, crying",
         camera="medium wide shot", amb="room_night"),
    dict(to=70, reason="action change: Hayaathu breaks down with her sister", chars=["hayaathu", "dhooma"], loc="bedroom_night",
         visual="Hayaathu kneeling beside Dhooma's wheelchair with her head on her sister's lap, sobbing; Dhooma bending over her, gently stroking her back, tears in her eyes",
         camera="medium close-up", amb="room_night", hum_note="emotional peak"),
    # ---------------- Waheed's rage ----------------
    dict(to=72, reason="character change: Waheed bursts in", chars=["waheed", "hayaathu", "dhooma"], loc="bedroom_night",
         visual="Waheed in the flung-open bedroom doorway, face twisted with rage, shouting; Hayaathu and Dhooma turning towards him at once, frozen in fright",
         camera="medium wide shot, from behind the sisters", amb="room_night", sens="violence",
         safe="only his furious face and their startled reaction; the grabbing of her arm is not shown"),
    dict(to=73, reason="action change: Hayaathu dragged out (shown through Dhooma)", chars=["dhooma"], loc="bedroom_night",
         visual="Dhooma alone in her wheelchair in the bedroom, crying in fear, one hand reaching towards the empty open doorway, the grey shawl slipped from her lap onto the floor",
         camera="medium shot", amb="room_night", sens="violence",
         safe="the dragging and throwing are not shown; Dhooma's helpless reaction and the empty doorway instead"),
    dict(to=75, reason="scene change: aftermath in the sitting room, Zoona and Areesha run out", chars=["hayaathu", "zoona", "areesha"], loc="sitting_room",
         visual="Hayaathu slumped on the floor beside the low coffee table, face hidden in her arm, no injury visible; in the corridor doorway behind, Zoona and Areesha appear in surprise",
         camera="wide shot, slightly high angle", amb="living_night", sens="violence",
         safe="her fall against the table is not shown; only the aftermath, no wounds"),
    dict(to=77, reason="character/action change: Dhooma wheels out, helpless", chars=["dhooma"], loc="sitting_room",
         visual="Dhooma wheeling herself out of the corridor into the sitting room in her black wheelchair, crying, her face full of helpless anguish",
         camera="medium shot, eye level", amb="living_night"),
    dict(to=79, reason="action change: Waheed smashes the glass vase (symbolic detail)", loc="glass_floor",
         visual="a glass flower vase shattering on a terrazzo floor, sharp shards flying and glittering, no people, no blood",
         camera="low-angle close-up", amb="living_night", sens="violence",
         safe="the smash shown as a breaking vase only; the shard piercing Hayaathu's back is never shown"),
    dict(to=81, reason="character change: Areesha cries out in pain", chars=["areesha"], loc="sitting_room",
         visual="Areesha in a bedroom doorway clutching the doorframe, face crumpled in pain and shock, crying out; glass shards glinting on the floor in front of her, her feet not visible",
         camera="medium shot", amb="living_night", sens="injury",
         safe="her cut foot and blood are not shown; only her face and the glass on the floor"),
    dict(to=85, reason="action change: Zoona picks her way to Areesha, blaming Hayaathu", chars=["zoona", "areesha"], loc="sitting_room",
         visual="Zoona stepping carefully between glass shards towards Areesha, who sits crying on the floor by the doorway with her knees drawn up under her dress; Zoona glaring back over her shoulder with contempt",
         camera="medium wide shot", amb="living_night"),
    dict(to=87, reason="characters change: Waheed and Zoona argue", chars=["waheed", "zoona", "areesha"], loc="sitting_room",
         visual="Waheed standing stiffly, pointing towards the corridor; Zoona, supporting the crying Areesha by the shoulders, rolling her eyes at him",
         camera="medium wide three-shot", amb="living_night"),
    dict(to=90, reason="action change: Waheed threatens Hayaathu", chars=["waheed", "hayaathu"], loc="sitting_room",
         visual="Waheed standing several steps away from the coffee table with a raised pointing finger and a hard cold face; Hayaathu slumped with her head on the coffee table, eyes shut, crying",
         camera="medium wide, low angle on Waheed", amb="living_night", sens="violence",
         safe="no injury or blood visible; Hayaathu shown from the front"),
    dict(to=93, reason="action change: Dhooma comes to her sister and calls for help", chars=["dhooma", "hayaathu"], loc="sitting_room",
         visual="Dhooma in her wheelchair beside the coffee table where Hayaathu lies with her head down sobbing, seen from the front; Dhooma turned towards a closed corridor door, crying and calling out with her hand raised",
         camera="medium shot, eye level", amb="living_night", sens="injury",
         safe="the glass in her back and the blood are never shown; Hayaathu seen from the front"),
    dict(to=96, reason="scene change: Zoona comforts only her own daughter", chars=["zoona", "areesha"], loc="areesha_room",
         visual="Zoona sitting on the bed beside the tearful Areesha, lovingly stroking her daughter's head while throwing a bored, dismissive glance towards the door",
         camera="medium shot", amb="room_night"),
    dict(to=98, reason="back to the sisters (reuse); Dhooma tries to help alone", reuse="beat_034", chars=["dhooma", "hayaathu"], loc="sitting_room",
         visual="(reuse) Dhooma beside Hayaathu at the coffee table", amb="living_night", sens="injury",
         safe="removing the glass is not shown"),
    dict(to=101, reason="action change: Zoona shouts at the sisters and slams the door", chars=["zoona"], loc="sitting_room",
         visual="Zoona standing in an open bedroom doorway pointing angrily at the glass on the floor, shouting, merciless cold eyes",
         camera="medium shot, slight low angle", amb="living_night"),
    dict(to=105, reason="action change: alone, Hayaathu weeps in Dhooma's lap", chars=["hayaathu", "dhooma"], loc="sitting_room",
         visual="Hayaathu kneeling on the floor with her head in Dhooma's lap, sobbing, her back covered by her dress; Dhooma in the wheelchair, her trembling hand resting on her sister's shoulder, her face lost and tear-streaked",
         camera="medium close-up, eye level", amb="living_night", sens="injury",
         safe="pulling out the glass and the bleeding are not shown; Dhooma's trembling hand on the shoulder and her face carry it"),
    dict(to=109, reason="character change: aunt Shafeena arrives and is shocked", chars=["shafeena", "dhooma"], loc="sitting_room",
         visual="Shafeena just inside the front door, hand over her mouth in shock, staring at the glass on the floor; Dhooma in her wheelchair looking up at her with red, tear-filled eyes",
         camera="medium wide shot", amb="living_night", sens="injury",
         safe="the blood she sees is not shown; only the glass on the floor and her shocked face"),
    dict(to=111, reason="action change / cliffhanger: Shafeena lifts Hayaathu, who collapses", chars=["shafeena", "hayaathu"], loc="sitting_room",
         visual="Shafeena kneeling on the floor holding Hayaathu by both shoulders, her face full of alarm, as Hayaathu, eyes closed and body limp, slumps sideways against her arm",
         camera="medium close-up", amb="living_night", sens="injury",
         safe="no wound or blood; the faint is shown as a limp body and closed eyes"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "...So how could he walk away from that love? Today Hayaathu is his future wife.")
sh(2, "With what heart could he let her become someone else's? Fazaal came back to his senses at a message on his phone.",
   [("phone_buzz", "މެސެޖަކުންނެވެ", -22)])
sh(3, "At that moment Hayaathu stood silently, still gazing far away. A light smile came to Fazaal's lips.")
sh(4, "It was because of a sweet daydream. He slowly walked over, stopped very close to Hayaathu and looked at her face.",
   [("footsteps_sand", "ހިނގާލާފައި", -24)])
sh(5, "Fazaal sensed that Hayaathu was crying. 'Would you like to share anything with me?' Fazaal asked gently.")
sh(6, "Hearing Fazaal's voice Hayaathu started a little and became aware of where she was. This lovely beach scene")
sh(7, "was where she had spent happy moments with Maaroof. As those memories returned, her lips moved slightly.")
sh(8, "How could she part from those sweet memories? Every time she wanted to escape uncle's harshness, Zoona's evil schemes and Areesha's mockery,", hum=True)
sh(9, "her shelter was Maaroof's kindness. Maaroof was the friend who always gave her courage and advised her to be patient.")
sh(10, "The day Maaroof went to uncle to ask for her hand is a day that will never fade from her heart. 'Hayaathu...")
sh(11, "I only just found out that Hayaathu's uncle is a very poor man,' Maaroof said seriously. 'What did you say?'")
sh(12, "Hayaathu asked in surprise. 'I mean, if he weren't poor, would he ask three million rufiyaa from someone just starting out in business like me?'")
sh(13, "Maaroof said with a smile. In his voice was scorn for her uncle. He had never seen such a greedy man in his life.")
sh(14, "'Why does uncle want three million rufiyaa?' Hayaathu's surprise grew. 'That's Hayaathu's price...")
sh(15, "If I want to marry Hayaathu, I have to give Waheed three million rufiyaa,' Maaroof said with a smile full of love.")
sh(16, "Hayaathu stood speechless looking at Maaroof. As Maaroof tried to come closer, his foot slipped and he fell into the sea.",
   [("splash", "ވެއްޓުނެވެ", -14)])
sh(17, "Seeing that, Hayaathu burst out laughing. Maaroof got up out of the sea and ran towards her, meaning to soak her too.",
   [("footsteps_sand", "ދުއްވައިގަތީ", -22)])
sh(18, "Hayaathu ran off laughing, and Maaroof ran after her. With these memories a smile came to Hayaathu's lips.",
   [("footsteps_sand", "ދުއްވައިގަތްއިރު", -22)])
sh(19, "At that moment Fazaal was gazing at Hayaathu's lovely face. A faint smile came to Fazaal's lips too.")
sh(20, "Surely some happy thought was turning in her mind. But there was still no answer to Fazaal's question.")
sh(21, "He gently moved closer to Hayaathu and lovingly took her hand. At that moment Hayaathu quickly shut her eyes.",
   [("cloth_rustle", "ހިފާލިއެވެ", -24)])
sh(22, "Watching without blinking, Fazaal noticed even the slightest movement of her eyelashes. 'I'll need time.'")
sh(23, "Hayaathu said, pulling her hand away from Fazaal's. 'How much time?' Fazaal asked softly. 'This is a marriage.")
sh(24, "It's a strong, sacred covenant between two people. Loyalty, love and care are things with a very deep meaning.")
sh(25, "My soul has to prepare itself for all of that. My heart has been given to someone else... I don't want to hide anything from Fazaal.", hum=True)
sh(26, "I'm going through with this marriage because I'm forced to. All Fazaal will get is this body of mine... not my heart.'", hum=True)
sh(27, "Hayaathu's words broke off as she couldn't hold back her tears and began to cry. 'I'm also going through with this marriage under compulsion.'",
   [("sob_breath", "ރޮވެން", -24)], hum=True)
sh(28, "Fazaal said, his eyes fixed on her face. At the word 'compulsion' questions crowded Hayaathu's heart. What compulsion could Fazaal have?")
sh(29, "He is free. A grown man of thirty-two. The only difference is that frightening burned look on his face.")
sh(30, "So what compulsion could he have? Still, Hayaathu thought deeply. Yes.")
sh(31, "Everyone may have compulsions of their own. As Hayaathu sank into a sea of thoughts, she didn't know that Fazaal was compelled by the call of his own heart.")
sh(32, "Fazaal was compelled by Hayaathu's love, her chaste character and her kindness. A light smile came to Fazaal's lips.")
sh(33, "Though countless things he wanted to tell Hayaathu crowded his heart, he didn't know how to begin.")
sh(34, "This might be the first time he had met a girl alone. Before this he had talked with many girls on the phone.")
sh(35, "But when it came to marriage, he would send his brother's photo to test who the girls really were. Once they saw that photo their tone changed.")
sh(36, "Quite a few stopped picking up the next day, or changed their numbers out of fear of his looks. He always pictured girls")
sh(37, "as selfish people chasing worldly glitter and outward beauty,")
sh(38, "and as people who hide their true face beneath a mask to win others' love.")
sh(39, "But only just now had he met a girl of the noble character he had wished for. So why shouldn't he be compelled by that heart?", hum=True)
sh(40, "Slowly opening the door of the house, Hayaathu stepped inside. But a moment later she stepped back and went out again.",
   [("door_open", "ހުޅުވާލަމުން", -20)])
sh(41, "Fazaal drove off only once he was sure she had gone in. Hayaathu looked up and down the road, then ran with all her strength.",
   [("car_drive_off", "ދުއްވާލީ", -18), ("footsteps_pavement", "ދުއްވައިގަތެވެ", -22)])
sh(42, "Hayaathu reached Maaroof's house exhausted, gasping for breath. Steadying her breathing, she knocked on the door.",
   [("breath_heavy", "ނޭވާ", -20), ("knock", "ޓަކި", -14)])
sh(43, "In the late-night silence nothing moved on the road. Getting no answer, Hayaathu took a deep breath and knocked again and again.",
   [("knock", "ޖަހަން", -14)])
sh(44, "The deserted silence all around began to fill her heart with fear. Crying and sobbing she kept knocking, but not a sound came from inside.",
   [("knock", "ތަޅަމުން", -14), ("sob_breath", "ގިސްލަމުން", -24)], hum=True)
sh(45, "Suddenly Hayaathu's phone vibrated and began to ring. Startled, she looked at it — Dhooma was calling.",
   [("phone_buzz", "ވައިބްރޭޓްވެ", -14)])
sh(46, "Seeing it was Dhooma, Hayaathu cried harder than before. 'Hello,' she said in a trembling voice, the phone to her ear. 'Where are you, Hayaathu?'", hum=True)
sh(47, "Dhooma asked anxiously. 'I'm coming home,' Hayaathu said, sobbing. Hanging up, she began walking towards home.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(48, "She had gone to that house with great hope of meeting Maaroof. But she walked away with deep despair in her heart.")
sh(49, "A little after she set off, a car parked far away started up. Watching where Hayaathu went, Fazaal smiled.",
   [("car_drive_off", "ސްޓާޓްވިއެވެ", -22)])
sh(50, "Fazaal understood well what was in Hayaathu's heart. He knew she might take a step like this.")
sh(51, "So Fazaal had deliberately left her to her own will. Carefully watching her every move, Fazaal drove on.",
   [("car_pass", "ދުއްވާލިއެވެ", -24)])
sh(52, "Pretending to go somewhere other than her house, Fazaal quietly drove along behind Hayaathu.")
sh(53, "From what he had just witnessed, however strong Hayaathu thought she was, he was sure she had no strength against Fazaal.")
sh(54, "The message Hayaathu sent Maaroof after tonight's ring ceremony was seen by Fazaal. Thinking he wouldn't see it, she deleted it, but Fazaal had read it long before.")
sh(55, "At first Fazaal had planned to go and see Hayaathu with Yasir. But after seeing that message, he decided to go to her himself.")
sh(56, "He didn't want to share it with anyone. Fazaal's heart didn't want to give Hayaathu even a single chance to meet Maaroof.")
sh(57, "If he could, Fazaal wanted to make Hayaathu his own this very night. But everything has its time and its rules.")
sh(58, "Entering the house, Hayaathu walked slowly towards her room. Areesha, sitting in the sitting room playing with her phone, saw her, jumped up at once and blocked her way.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -26)])
sh(59, "'Hey Beauty, wait!' Areesha called, quickly catching up with Hayaathu.")
sh(60, "Hayaathu looked at Areesha with eyes red and swollen from crying. Seeing the grief and despair on her face, Areesha suddenly stopped short.")
sh(61, "Only then did Areesha realise something had gone wrong. Before Hayaathu could say a word, tears poured down her cheeks again.")
sh(62, "'So how's the Prince of Dubai? What gift did he give you? Came back empty-handed? I thought on the ring night he took you out to give you something really expensive.'")
sh(63, "Areesha said, meaning to mock her. But Hayaathu walked towards her room without a word.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -26)])
sh(64, "'Hey, wait a bit more!' Areesha called with a poisonous laugh. 'What is it?' Hayaathu asked irritably.")
sh(65, "'After the ring ceremony you're as good as a wife. No point crying over Maaroof now. Now learn to be happy thinking of the ugly Prince of Dubai.'")
sh(66, "Areesha said mockingly. Those venomous words seemed to break Hayaathu's heart to pieces. With that deep hurt, tears fell from her eyes.", hum=True)
sh(67, "Not wanting to be the prey of Areesha's venom any longer, Hayaathu hurried into her room and shut the door.",
   [("door_close", "ލައްޕައިލިއެވެ", -16)])
sh(68, "Areesha's tongue was more poisonous than Fazaal's looks. When Hayaathu came in, Dhooma was sitting there, worried because she was late.")
sh(69, "Seeing her sister, Hayaathu broke into sobs. Dhooma tenderly stroked her back.",
   [("sob_breath", "ގިސްލައި", -24)], hum=True)
sh(70, "'Dhontha, I went to that house to see Maaroof.' The moment she said it was the moment Waheed reached the room. Hearing it,")
sh(71, "furious beyond measure, Waheed kicked the door open. 'Hayaathu!' Waheed roared in a voice full of rage.",
   [("door_open", "ކޮއްޕައި", -10)], hum=True)
sh(72, "At that terrifying voice Dhooma and Hayaathu both started and looked up. Waheed at once seized Hayaathu by the arm and hauled her up.",
   [("gasp", "ސިހިފައި", -16)])
sh(73, "As Hayaathu began to tremble with fear, Dhooma too burst into frightened tears. Dragging Hayaathu out of the room by the arm, ignoring her pleas, he flung her into the sitting room.",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -24)], hum=True)
sh(74, "Hayaathu was thrown against the coffee table in front of the sofa. At Waheed's loud voice,",
   [("soft_thud", "ޖެހުނީ", -12)])
sh(75, "Zoona, who had been asleep, and Areesha, who was getting ready for bed, came rushing out. Behind them, to help her little sister,",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(76, "Dhooma too came out, crying, driving her wheelchair. But what could that helpless girl do?",
   [("wheelchair_roll", "ދުއްވާފައި", -18)], hum=True)
sh(77, "She had no choice but to sit and watch, weeping. Hayaathu lay there unable even to get up from the hurt and the pain, and unable to control his boiling rage,")
sh(78, "Waheed grabbed a glass vase from the shelf beside him and smashed it on the floor.",
   [("glass_break", "ތަޅައިލިއެވެ", -10)])
sh(79, "At that moment a sharp shard from the flying glass pierced Hayaathu's back. 'Ahh!'",
   [("gasp", "އާހް", -14)], hum=True)
sh(80, "A moan of pain escaped Hayaathu's lips. 'Dad! Ouch!' Areesha, standing at her bedroom door, screamed too,",
   [("gasp", "ހަޅޭއްލަވައިގަނެވުނެވެ", -16)])
sh(81, "because a flying piece of glass had struck her foot and cut it deeply. 'Waheed, look where you are!")
sh(82, "However angry you are, that's too much. Look how badly you've hurt Areesha,' Zoona said in a voice full of anger and resentment. 'Mum,")
sh(83, "it really hurts,' Areesha said, sobbing. Very carefully, avoiding the glass scattered on the floor, Zoona went to Areesha.",
   [("sob_breath", "ގިސްލަމުން", -24)])
sh(84, "Areesha was sobbing and writhing in pain. Zoona looked at her daughter's wounded foot. 'What a disaster this is!")
sh(85, "Because of this one, our daughter had to get hurt too,' Zoona said venomously, glaring at Hayaathu.")
sh(86, "'Stop talking so much, take Areesha inside and put medicine on that foot,' Waheed told Zoona, his anger cooling a little.")
sh(87, "'Still taking your anger out on me, aren't you?' Zoona said, rolling her eyes at Waheed. 'Mum, it really hurts.'")
sh(88, "Areesha pleaded, crying like a small child. Zoona led Areesha off towards her room. 'Hayaathu! Have you no shame at all?",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(89, "You're now engaged to marry Fazaal. If he finds out about this, how low will our standing fall? He's no ordinary man.")
sh(90, "From now on you will not meet Maaroof. Otherwise the consequences will be very bitter.' Having said that in the harshest tone,")
sh(91, "Waheed went inside. With heartbreaking sobs, Dhooma drove her wheelchair towards Hayaathu.",
   [("footsteps_pavement", "ވަދެގެން", -24), ("wheelchair_roll", "ދުއްވާލިއެވެ", -18)])
sh(92, "Hayaathu lay with her head on the coffee table, sobbing in unbearable pain. Blood was flowing around the shard of glass in her back.",
   [("sob_breath", "ގިސްލާ", -24)], hum=True)
sh(93, "Seeing it, Dhooma cried even harder. 'Dha...ttha... Dha...ttha...' Stammering, in a trembling voice, Dhooma kept calling Zoona.", hum=True)
sh(94, "'As if anything's happened! Now Dhooma's drama starts,' Zoona said wearily, rolling her eyes. 'Mum, it really hurts.'")
sh(95, "Areesha repeated, crying. 'Mummy knows it hurts, darling. Don't come out until that glass has been picked up and cleaned,")
sh(96, "or it might cut your foot again,' Zoona said, lovingly stroking Areesha's head.")
sh(97, "Hayaathu's silent sobs and the pain from the wound kept growing. With no one coming to help,")
sh(98, "Dhooma tried to pull the shard of glass out of Hayaathu's back by herself. Just then Zoona opened the bedroom door and came out.",
   [("door_open", "ހުޅުވާލުމަށްފަހު", -18)])
sh(99, "'Pick up that glass, quickly! Or Areesha might get hurt again.' Without any mercy, Zoona shouted angrily at the sisters.")
sh(100, "Sobbing, Dhooma tried to say something, but no voice came through her tears.")
sh(101, "Glaring at the two of them as if there was nothing more to say, Zoona went back into the room and slammed the door.",
    [("door_close", "ޖެހިއެވެ", -10)])
sh(102, "At that Hayaathu lifted her head, then laid it again on Dhooma's lap and began to sob. The piece of glass in Hayaathu's back",
    [("sob_breath", "ގިސްލާ", -24)], hum=True)
sh(103, "Dhooma, summoning her courage, pulled out. As the blood began to flow more than before, Dhooma pressed her hand on the spot to stop it.",
    [("gasp", "ދަމައިގަތެވެ", -18)], hum=True)
sh(104, "Sobbing so hard, even Dhooma's hand was trembling. More than the physical pain Hayaathu felt,")
sh(105, "the wound to her heart was deeper and more painful. As Hayaathu wept without stopping, Dhooma sat at a loss, not knowing what to do.", hum=True)
sh(106, "A while later Shafeena came into the house; seeing this scene, deeply alarmed, she hurried towards the two girls.",
    [("door_open", "ވަދެގެން", -20), ("footsteps_pavement", "އަވަސްވެގަތެވެ", -22)])
sh(107, "Shafeena is Dhooma and Hayaathu's father's full younger sister, the girls' beloved aunt. 'Dhooma! My dear, what happened?'")
sh(108, "Hearing Shafeena's kind voice, Dhooma looked up at her with eyes red from crying. 'Dha.... Dhattha...'")
sh(109, "Dhooma burst into even harder tears. Seeing the blood running from Hayaathu's back and the glass scattered across the floor, Shafeena was utterly shocked.",
    [("gasp", "ސިހުން", -16)], hum=True)
sh(110, "After an anxious glance at Dhooma, she hurried over and took Hayaathu by both shoulders to lift her. But",
    [("cloth_rustle", "ހިފައި", -22)])
sh(111, "Hayaathu's body, without any strength left in it, slumped to one side at that moment.",
    [("soft_thud", "އަރިއަޅާލިއެވެ", -18)], hum=True)
SHOTS = S

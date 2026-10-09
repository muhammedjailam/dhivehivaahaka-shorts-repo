"""Beat/shot plan for Noorin episode 497 (used by plan_beats.py)."""

OFF_DUTY = ("not in uniform: wearing a loose deep-plum long abaya-style dress with long sleeves and a black hijab "
            "wrapped snugly and fully covering her hair and neck, no beret, no cap, no badge")
GOWN = ("not in uniform: wearing an elegant loose floor-length long-sleeved ivory-white satin gown with subtle silver "
        "embroidery at the cuffs and a soft ivory hijab wrapped snugly and fully covering her hair and neck, no beret, "
        "no cap, no badge")
PRODUCER = ("Sen Dil, a middle-aged South Asian film producer with a short salt-and-pepper beard, wearing a black "
            "high-collared bandhgala jacket and dark trousers")
GAP = "a clear arm's-length gap between them, nobody touching"

LOC = {
    "apartment": "Noorin's modern, tidy apartment in Malé at night, a simple wooden desk with an open laptop beside a tall window streaked with rain, the city lights blurred outside, a warm desk lamp",
    "festival_hall": "a grand modern festival auditorium in Malé during a film award ceremony, rows of plush seats filled with elegantly dressed guests, a wide stage with soft spotlights and a huge projection screen showing only blurred abstract colours, deep red curtains",
    "festival_stage": "the wide stage of a grand modern festival auditorium in Malé, a single bright spotlight, a glossy dark floor, the dark audience hall beyond with soft points of light, a huge projection screen behind glowing with blurred abstract colours",
    "foyer": "the elegant glass-walled foyer of a modern festival auditorium in Malé after an award ceremony, crystal chandeliers, polished marble floor, guests in formal clothes talking in small groups in the soft-focus background",
    "bedroom": "Noorin's quiet bedroom in her Malé apartment at night, a neatly made bed with a dark bedspread, a tall window streaked with rain, the city lights blurred outside, a dim bedside lamp",
    "construction": "a tropical island resort under construction in the Maldives, half-built white villas with wooden scaffolding, sand paths, piles of coral stone blocks and timber, blue tarpaulins, coconut palms, a turquoise lagoon beyond",
    "staff_room": "young Noorin's small simple staff room in the resort's staff quarters, whitewashed walls, a small two-seat fabric sofa, a low wooden coffee table in front of it, a wooden door to the outside, a window with palm leaves outside",
    "site_office": "a small temporary site office at the resort under construction, a plain desk with neat blank papers and a desk phone, a wall-mounted fan, a window looking out to scaffolding and palms",
    "rain_street": "Majeedhee Magu, a main street of Malé, late at night in heavy rain, closed shop shutters, wet shining asphalt reflecting the streetlights, the street empty",
    "files_office": "a rich young businessman's office in Malé late at night, a large dark-wood desk covered with plain staff files and folders, a desk lamp, a dark window with the city lights",
}
MOOD = {
    "apartment": "present day, late night, cool navy and teal shadows, the warm amber desk lamp and the cold glow of the laptop on her face, tired and guarded",
    "festival_hall": "present day, evening, dark hall with warm golden stage spotlights and cool blue edges, glamorous and expectant",
    "festival_stage": "present day, evening, a single warm white spotlight against the dark hall, triumphant yet cold and composed",
    "foyer": "present day, night, warm chandelier light against deep navy glass walls, tense, charged silence",
    "bedroom": "present day, late night, deep navy shadows, cold rain-light from the window and a dim amber lamp, raw grief",
    "construction": "twelve years earlier, warm soft golden haze, bright tropical morning sunlight, dust in the air, busy and alive",
    "staff_room": "twelve years earlier, warm soft golden haze, late-morning sunlight through the window, quiet, intimate and shy",
    "site_office": "twelve years earlier, warm soft golden haze, calm morning light through the window, quiet routine",
    "rain_street": "twelve years earlier, a memory, warm soft golden haze over a rainy night, blue-grey rain with amber streetlight glow, lonely",
    "files_office": "twelve years earlier, warm soft golden haze, late night, warm desk-lamp light in a dark room, sudden hope",
}

BEATS = [
    dict(to=5, reason="episode opening: Noorin home off duty at her computer, the festival invitation and her call to Zee", chars=["noorin"], loc="apartment",
         visual=f"Noorin, {OFF_DUTY}, sitting at the desk by the rainy window, freshly washed and tired, the open laptop in front of her with its screen showing only soft blurred glowing shapes, holding a phone to her ear with a cool, unsmiling face",
         camera="medium shot, eye level, slightly from the side", amb="home_night"),
    dict(to=8, reason="time jump and scene change: the award ceremony of the SAARC film festival", chars=["noorin", "zee"], loc="festival_hall",
         visual=f"Noorin, {GOWN}, seated in the audience of the grand hall beside her friend Zee (red-framed glasses, mustard-yellow hijab, olive-green dress), both faces lit by the stage lights, watching the stage where the huge screen glows with blurred abstract colours; elegant guests in rows around them",
         camera="medium shot from slightly in front of the seats, the stage glow behind", amb="hall_crowd", transition="black",
         sens="other", safe="the screen and festival backdrop show only blurred colours, no titles, no logos"),
    dict(to=9, reason="turning point: WhiteLily is revealed — Noorin on stage with the award", chars=["noorin"], loc="festival_stage",
         visual=f"Noorin, {GOWN}, standing alone in the spotlight at the centre of the stage holding a plain smooth crystal award with no engraving, her face calm, cool and composed, looking out over the dark astonished audience",
         camera="medium wide, low angle from the front rows", amb="hall_crowd",
         sens="other", safe="the award is a plain blank crystal shape, no engraving or text"),
    dict(to=10, reason="character change: Uvaish in the audience, as if he has seen a ghost", chars=["uvaish"], loc="festival_hall",
         visual="Uvaish in his charcoal suit seated among the audience, half-risen from his seat, staring towards the stage in total shock, eyes wide, lips parted, the stage light falling on his face while the guests around him are in soft shadow",
         camera="medium close-up, eye level", amb="hall_crowd"),
    dict(to=12, reason="scene change: after the ceremony in the foyer with Zee and the producer; Uvaish's voice", chars=["noorin", "zee"], loc="foyer",
         visual=f"Noorin, {GOWN}, holding the plain crystal award, standing in the foyer talking with Zee and {PRODUCER}; Noorin's face suddenly frozen, her eyes widening as if she has just heard a voice behind her",
         camera="medium wide three-shot, eye level", amb="hall_crowd"),
    dict(to=15, reason="action change: she turns and faces Uvaish after twelve years", chars=["noorin", "uvaish"], loc="foyer",
         visual=f"Noorin, {GOWN}, in the foreground, turned around and frozen, her face pale, guarded and shaken, looking at Uvaish; Uvaish in his charcoal suit standing several steps away facing her, his eyes full of longing and disbelief; {GAP}",
         camera="over-the-shoulder medium shot, Noorin's face sharp, Uvaish in the background", amb="hall_crowd"),
    dict(to=19, reason="action change: their bitter exchange about WhiteLily and 'Rihun'", chars=["noorin", "uvaish"], loc="foyer",
         visual=f"two-shot in profile: Noorin, {GOWN}, with a cold, forced half-smile and hard eyes, speaking to Uvaish with reproach; Uvaish in his charcoal suit facing her, earnest and pleading, one hand open at his chest; {GAP}",
         camera="medium two-shot, profile, eye level", amb="hall_crowd"),
    dict(to=20, reason="action change: she walks away, he reaches out — the moment before the slap", chars=["noorin", "uvaish"], loc="foyer",
         visual=f"Noorin, {GOWN}, mid-turn back towards Uvaish, her face blazing with cold fury, her own hands clenched at her sides; Uvaish a step behind her with one hand half-raised towards her, stopped in the air, not touching her, his face startled; {GAP}",
         camera="medium two-shot, eye level", amb="hall_crowd", sens="violence",
         safe="the hand-grab and the slap are not shown: only the tense moment before, with an arm's-length gap and no contact"),
    dict(to=23, reason="action change: the aftermath — Uvaish stunned, Zee and the producer staring", chars=["uvaish", "zee"], loc="foyer",
         visual=f"Uvaish in his charcoal suit standing alone, stunned and hurt, his hand lowered at his side, staring after someone who is leaving the frame; a few steps away Zee and {PRODUCER} stand frozen, staring wide-eyed, glancing at each other",
         camera="medium wide, eye level", amb="hall_crowd", sens="violence",
         safe="aftermath only: no mark on his face, nobody touching, the strike is never shown"),
    dict(to=25, reason="time jump and scene change: home, she throws her things down and cries out her pain", chars=["noorin"], loc="bedroom",
         visual=f"Noorin, {GOWN}, standing beside the bed, her small clutch bag and the crystal award flung onto the dark bedspread, her head tilted back and eyes squeezed shut, her face twisted in anguish as she cries out, fists clenched",
         camera="medium shot, eye level", amb="room_night", transition="black", hum=True),
    dict(to=27, reason="emotional turning point: quiet, the buried past rises — leading into the flashback", chars=["noorin"], loc="bedroom",
         visual=f"Noorin, {GOWN}, sitting on the floor by the rain-streaked window with her back against the wall, knees drawn up under the gown, staring into the distance with wet, empty eyes, the rain shadows running over her face",
         camera="medium close-up, slightly high angle", amb="room_night"),
    # ---------------- flashback: twelve years earlier
    dict(to=28, reason="flashback: twelve years earlier, young Noorin hurries across the resort under construction", chars=["noorin_young"], loc="construction",
         visual="young Noorin walking briskly along a sand path between half-built villas, holding a plain folder to her chest, past workers carrying timber and stone blocks on their shoulders; she looks straight ahead, not up",
         camera="medium wide tracking shot, eye level", amb="island_day", transition="dissolve"),
    dict(to=30, reason="action change: 'Madam, careful!' — the young man warns her and she stumbles aside", chars=["uvaish_young", "noorin_young"], loc="construction",
         visual=f"young Uvaish shouting a warning with one arm flung up, young Noorin stumbling a step sideways in surprise, holding her own hand to her forehead with a pained wince; {GAP}; dust rising from the scaffolding above",
         camera="medium two-shot, eye level", amb="island_day", sens="intimacy",
         safe="the narration has him pull her by the hand and their heads bump; shown as a warning shout and her stumbling aside alone, no contact"),
    dict(to=33, reason="action change: the falling stone and the tarpaulin; workers rush to help", loc="construction",
         visual="a large coral stone block lying on the sand path where she was about to walk, a cloud of golden dust, a big dusty blue tarpaulin slid down from the scaffolding into a heap, several workers in work clothes rushing over and lifting its edge with both hands; nobody visible beneath it",
         camera="wide shot, eye level", amb="island_day", sens="violence",
         safe="no one is hit or hurt: only the fallen stone, dust and workers lifting the tarpaulin; nobody shown underneath"),
    dict(to=35, reason="action change: freed, she brushes off the dust and looks at her arm", chars=["noorin_young"], loc="construction",
         visual="young Noorin standing in the settling dust, brushing sand off her dusty dress with one hand while looking down at her other forearm, its long sleeve dusty with only a faint pinkish scuff on the cloth, her face shaken but calm",
         camera="medium shot, eye level", amb="island_day", sens="violence",
         safe="the scraped arm is shown only as a dusty sleeve with a faint pinkish scuff; no wound, no blood"),
    dict(to=40, reason="character focus change: the young man teases her about 'thank you'", chars=["uvaish_young", "noorin_young"], loc="construction",
         visual=f"young Uvaish, his white linen shirt dusted with sand, standing with his hands on his hips and a playful, slightly arrogant grin; young Noorin facing him, flustered and surprised, clutching her folder; {GAP}",
         camera="medium two-shot, eye level", amb="island_day"),
    dict(to=44, reason="action change: the breakfast invitation; she talks to her own heart", chars=["uvaish_young", "noorin_young"], loc="construction",
         visual=f"young Uvaish smiling warmly and gesturing with an open hand towards a thatched open-air restaurant pavilion by the lagoon; young Noorin in the foreground looking at his face with a doubtful, thoughtful expression, lips pressed; {GAP}",
         camera="medium two-shot, Noorin closer to camera", amb="island_day"),
    dict(to=48, reason="action change: she walks away towards her room, stops and closes her eyes; he smiles behind her", chars=["noorin_young", "uvaish_young"], loc="construction",
         visual="young Noorin in the foreground on the sand path to the staff quarters, stopped mid-step with her eyes closed, taking a deep breath; far behind her in soft focus young Uvaish stands watching her go with a happy smile",
         camera="medium shot, shallow depth of field, Noorin sharp, Uvaish blurred", amb="island_day"),
    dict(to=49, reason="scene change: alone in her staff room, she looks at her arm", chars=["noorin_young"], loc="staff_room",
         visual="young Noorin sitting on the small sofa in her staff room, gently touching her sleeve-covered forearm, the sleeve dusty with a faint pinkish scuff, a small bowl of water and tissues on the coffee table, her face quiet and reflective, in bright daytime: warm late-morning sunlight streams in through the window, green palm leaves and a blue sky outside, no rain, not night",
         camera="medium shot, eye level", amb="room_day", sens="violence",
         safe="no wound shown: only a dusty sleeve with a faint pinkish scuff"),
    dict(to=51, reason="backstory: two months ago she came to the resort as a secretary — at work in the site office", chars=["noorin_young"], loc="site_office",
         visual="young Noorin sitting at the plain desk of the small site office, organising blank papers into a folder, a calm diligent face, the scaffolding visible through the window behind her",
         camera="medium shot, eye level", amb="office_day",
         sens="other", safe="papers are blank, no readable text"),
    dict(to=53, reason="returns to her staff room as she cleans her arm (reuse)", reuse="beat_019", chars=["noorin_young"], loc="staff_room",
         visual="(reuse) young Noorin on the sofa looking at her arm", amb="room_day"),
    dict(to=57, reason="character change: Naahidh at the door with the ointment from 'the boss'", chars=["noorin_young", "naahidh"], loc="staff_room",
         visual=f"young Noorin standing in the open doorway of her staff room, frowning with knitted brows; Naahidh outside on the step holding out a small plain ointment bottle at full arm's length with a matter-of-fact face; {GAP}",
         camera="medium two-shot from inside the room, eye level", amb="room_day"),
    dict(to=61, reason="character change: the rescuer himself walks in with an ice pack — 'Not boss, Uvaish'", chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual=f"young Uvaish having just stepped into the staff room, turned back towards the door and holding out a blue ice pack at full arm's length with a confident smile; young Noorin standing by the open door, one hand on the door edge, staring at him in startled astonishment; {GAP}",
         camera="medium wide two-shot, eye level", amb="room_day"),
    dict(to=63, reason="action change: the door swings shut and he gestures her to the sofa", chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual=f"young Uvaish gesturing politely with an open palm towards the small sofa; young Noorin standing shy and hesitant, the wooden door behind her slowly swinging closed; {GAP}",
         camera="medium two-shot, eye level", amb="room_day"),
    dict(to=66, reason="action change: she sits on the sofa holding the ice pack, he sits on the coffee table facing her", chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual=f"young Noorin sitting on the sofa holding the blue ice pack to her own forehead with one hand, wincing a little; young Uvaish sitting on the low coffee table opposite her, leaning back, watching her face with soft, wondering eyes; {GAP}",
         camera="medium two-shot in profile, eye level", amb="room_day", sens="intimacy",
         safe="the narration has him press the ice pack to her head; she holds it herself, he sits at arm's length"),
    dict(to=68, reason="memory within the flashback: the rainy night on Majeedhee Magu two months earlier", loc="rain_street",
         visual="a lone man holding a large black umbrella, seen only from behind as a silhouette, standing on the empty rain-soaked street at night, rain pouring in sheets through the amber streetlight",
         camera="wide shot from behind, low angle", amb="memory_rain", transition="dissolve", sens="other",
         safe="her fainting is not shown: only the man's silhouette with an umbrella on the rainy street"),
    dict(to=71, reason="scene change: Uvaish finds her file among the staff files", chars=["uvaish_young"], loc="files_office",
         visual="young Uvaish at the desk late at night holding an open staff file, a small folded note in his other hand, his face lighting up with sudden recognition and hope; the file pages show only blurred lines",
         camera="medium close-up, eye level", amb="office_night",
         sens="other", safe="the file and note show no readable text"),
    dict(to=73, reason="back to the staff room: his gaze makes her shy (reuse)", reuse="beat_025", chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual="(reuse) young Noorin on the sofa, Uvaish on the coffee table", amb="room_day", transition="dissolve"),
    dict(to=76, reason="action change: she tries to rise; he asks her to stay — 'I came only to meet Noorin'", chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual=f"young Noorin half-rising from the sofa with her eyes lowered shyly, the ice pack lowered in her hand; young Uvaish sitting on the far side of the low wooden coffee table, the whole table between them, raising one palm gently in the air, asking her to stay seated, leaning slightly forward with a serious, sincere face; {GAP}, in bright daytime: warm late-morning sunlight streams in through the window, green palm leaves and a blue sky outside, no rain, not night",
         camera="medium two-shot, eye level", amb="room_day", sens="intimacy",
         safe="the narration has him sit her back down; shown as a gentle raised palm, no contact"),
    dict(to=81, reason="action change: he stands and takes a small paper from his pocket; she stands up, embarrassed", chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual=f"young Uvaish standing, holding up a small folded piece of paper between two fingers with a meaningful look; young Noorin standing up from the sofa, her face suddenly flushed with embarrassment, one hand at her chest; {GAP}",
         camera="medium two-shot, eye level", amb="room_day",
         sens="other", safe="the note shows no readable text"),
    dict(to=85, reason="emotional change: she anxiously apologises about the unlocked door; his face turns playful", chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual=f"young Noorin with her hands clasped in front of her, anxious and apologetic, eyes wide; young Uvaish facing her with a slow playful smile spreading over his face, the small folded paper still in his hand; {GAP}, in bright daytime: warm late-morning sunlight streams in through the window, green palm leaves and a blue sky outside, no rain, not night",
         camera="medium close two-shot, eye level", amb="room_day"),
    dict(to=89, reason="emotional peak: his sudden closeness — she freezes, breath held", chars=["noorin_young"], loc="staff_room",
         visual="close-up of young Noorin frozen in place, eyes wide, breath held, one hand pressed to her chest, her lips slightly parted; only the soft out-of-focus edge of a white shirt sleeve at the far side of the frame",
         camera="close-up, eye level", amb="room_day", sens="intimacy",
         safe="the whisper close to her ear is not shown: only her frozen face, then him at the doorway"),
    dict(to=91, reason="action change: he walks to the door and looks back; she stands frozen", chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual="young Uvaish at the open doorway of the staff room, golden light outside, turned halfway back and looking at her with a mischievous smile; young Noorin in the foreground standing frozen in the middle of the room, well apart from him",
         camera="medium wide, from behind Noorin's shoulder", amb="room_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Utterly exhausted, she came home, changed out of her uniform, freshened up with a shower, and Noorin sat down at the desk.",
   [("door_close", "އައިސް", -22)])
sh(2, "As drops of water still fell from her wet hair, she swept it to one side and opened the computer.",
   [("keyboard_typing", "ކޮމްޕިއުޓަރު", -24)])
sh(3, "Checking her e-mail, she found a mail inviting her to the SAARC film festival. Noorin at once picked up the phone and called Zee,")
sh(4, "and asked her to bring the invitation card. \"Noorin, I'm sorry, okay! They were pestering so much that I gave them Noorin's ID,\" Zee said meekly.")
sh(5, "Without another word Noorin hung up. The days passed at a tremendous pace, and the time to go to the SAARC film festival drew near.")
sh(6, "This year the festival was held in the Maldives. Noorin, too, got ready and went to the award ceremony with her friend Zee.")
sh(7, "Trailers of the films were shown. Awards were handed to the best in each category.",
   [("applause", "ހަވާލުކުރަމުން", -20)])
sh(8, "Best screenplay went to \"Rihun\", the film Noorin had written under the name 'WhiteLily'. Every gaze was fixed, waiting to see who WhiteLily was.",
   [("applause", "ހޮވުނީ", -16)])
sh(9, "When they saw Noorin step onto the stage and take the award, everyone was astonished. The most astonished of all was Uvaish, one of the country's famous businessmen.",
   [("crowd_gasp", "ހައިރާންވެގެން", -20)])
sh(10, "To Uvaish it was as if he had seen a ghost before him. What had he not done to find Noorin? He had spent twelve years searching for her.",
   [("heartbeat", "ރޫހެއް", -20)], hum=True)
sh(11, "When the ceremony was over, people talked to one another, strengthening their connections. Noorin and Zee were talking with the film's producer, Sen Dil.")
sh(12, "\"Noorin.\" Uvaish's voice came from very close to Noorin. The feeling in that voice sent a shiver through her. Could Noorin ever mistake that voice?",
   [("heartbeat", "ހީބިހި", -20)], hum=True)
sh(13, "Twelve years ago she had heard that voice countless times. Noorin turned around and looked at Uvaish.",
   [("cloth_rustle", "ފަސްއެނބުރި", -24)])
sh(14, "She could not find the courage to take even one more step, backwards or forwards.", hum=True)
sh(15, "She had spent twelve years running from Uvaish for a reason. The person who had turned her heart to stone was Uvaish.")
sh(16, "And the one who had once caressed that heart with tenderness was Uvaish too. Noorin forced a kind of smile. \"Noorin is WhiteLily?")
sh(17, "I never imagined it. With the stories you write, you play on the deepest strings of the heart. Especially this one, \"Rihun\",\" Uvaish said, standing very close.")
sh(18, "\"This is not Noorin. WhiteLily. Only those who have felt \"Rihun\" — the pain — know the truth of that pain.")
sh(19, "I don't think Uvaish could ever feel it,\" Noorin said in a tone of reproach. Not wanting to talk to Uvaish any longer, Noorin walked on.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(20, "At that moment Uvaish caught Noorin's hand. Noorin turned back and looked at Uvaish. And without a second thought she struck him across the cheek.",
   [("soft_thud", "ޖެހިއެވެ", -22)], hum=True)
sh(21, "Seeing that, Zee and the film's producer were stunned. They glanced at each other. \"Let go of my hand.\"",
   [("crowd_gasp", "ހައިރާންވިއެވެ", -22)])
sh(22, "Uvaish, too, was shocked by what Noorin did. Slowly he let go of her hand. Greater than the pain spreading over Uvaish's cheek")
sh(23, "was the hurt striking his heart. He had never imagined Noorin could change so much.",
   [("sigh", "ނާރައެވެ", -22)], hum=True)
sh(24, "As soon as she got home, she flung the things in her hands onto the bed. The storm of pain hidden in her heart surged up. Crying out at the top of her voice,",
   [("soft_thud", "އެއްލާލިއެވެ", -22)], hum=True)
sh(25, "she let out the grief crushed inside her heart. She had always known that one day she would have to face those people.",
   [("sob_breath", "ބޭރުކޮށްލިއެވެ", -20)])
sh(26, "In the silence, the hardest days of her life began to take shape among Noorin's memories.")
sh(27, "It was like having to bring a buried past back to life, forced to read the diary of her life. That was twelve years ago.",
   [("page_turn", "ޑައިރީ", -24)])
sh(28, "Noorin left her room and set off at a brisk pace towards the resort manager's office. As the resort was still being developed, workers were busy carrying materials in every direction.",
   [("footsteps_sand", "ހިނގުމެއްގައި", -22)])
sh(29, "\"Madam, careful!\" With a shout from someone behind her, he caught Noorin's hand and pulled her towards him.",
   [("gasp", "ސަމާލުވާތި", -20)])
sh(30, "The two of them collided and fell, and Noorin's forehead struck his head. \"Ouch!\" Noorin put her hand to her head.",
   [("soft_thud", "ވެއްޓި", -22)])
sh(31, "At that moment a stone falling from above struck the ground in front of them. With it, a tarpaulin fell over the two of them, trapping them beneath it.",
   [("soft_thud", "ގާގަނޑެއް", -18), ("cloth_rustle", "ދާގަނޑެއް", -18)], hum=True)
sh(32, "Materials came tumbling down everywhere. Noorin struggled to free herself from the tarpaulin. The man beside her, still trapped under it, looked at nothing but Noorin's face.",
   [("soft_thud", "ފައިބައިގަތެވެ", -20), ("cloth_rustle", "ސަލާމަތްވުމަށް", -22)])
sh(33, "Noorin grew exhausted struggling to get out from under it. Workers came over and pulled the two of them out from under the tarpaulin.",
   [("breath_heavy", "ވަރުބަލިވަމުން", -22), ("footsteps_sand", "މަސައްކަތްތެރިން", -22)])
sh(34, "Calming herself, Noorin brushed the sand off. Her white dress was soiled, past wearing any longer; then her attention went to a spot on her arm that had been scraped.",
   [("cloth_rustle", "ވެލިފޮޅައިލިއެވެ", -22)])
sh(35, "Noorin touched the spot. And she looked at the man who had saved her from something falling on her head. \"Thank you,\" Noorin said softly.")
sh(36, "\"Thank you — is that all?\" There was a certain arrogance in his voice. Noorin looked at the young man in surprise.")
sh(37, "\"What else do people say at a time like this?\" Noorin asked. The man smiled.")
sh(38, "\"When someone saves you from death, does it end with just a thank you?\" the young man asked, looking at Noorin's flustered face. \"Sorry.\"")
sh(39, "Noorin began. \"Sorry, thank you — you don't know any other words, do you?\" he said in the same tone as before. \"Okay.\"")
sh(40, "Once again Noorin began. \"Yes, now that's better.\" The young man smiled.")
sh(41, "\"In return for the kindness you did today, what is it you would ask for?\" Noorin asked, composing herself.")
sh(42, "\"Very simple. I'm going to the restaurant for breakfast. You should join me for breakfast.\"")
sh(43, "the young man said with a grin, looking at Noorin. Noorin looked at his face, and began to talk to her own heart.")
sh(44, "\"Not accepting my thanks, he's decided I should have breakfast with him,\" Noorin said to herself. \"Lost in what thought?\"")
sh(45, "the young man asked. Instead of answering him, Noorin walked off towards her room. \"I'll wait.\"",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(46, "the young man said as Noorin walked away. Noorin stopped and thought. Instead of turning to look back, she closed her eyes.")
sh(47, "She thought deeply about what was happening to her. Then, after a deep breath, she went into her room.",
   [("breath", "ނޭވާއެއް", -22), ("door_close", "ވަނެވެ", -22)])
sh(48, "A happy smile spread over the young man's lips. Once inside her room, Noorin calmed down.")
sh(49, "And she looked at the scraped spot on her arm. She touched it gently. As the young man had said, today had been a brush with death.")
sh(50, "She had left her room to meet the manager because he had called. Two months earlier she had come to the resort as a secretary.")
sh(51, "As the resort was under construction and no guests came yet, there wasn't much work; but there were day-to-day matters to see to, so she had to meet the manager about them every day.")
sh(52, "\"Even after being told so often that I must look up when I walk, I always forget it,\" Noorin said to herself.")
sh(53, "And she went on cleaning the scraped spot with water. Just then the room's bell rang. Wiping her hands with a tissue, Noorin went and opened the door.",
   [("doorbell_buzz", "ބެލް", -16), ("door_open", "ހުޅުވައިލިއެވެ", -20)])
sh(54, "In front of her stood Naahidh, who worked with her in the office. In his hand was a small medicine bottle. As soon as Noorin opened the door he held the bottle out to her.")
sh(55, "\"The boss said to bring this to Noorin. If you won't take it, I'm to rub the ointment on even by force before I come back,\" Naahidh said in his usual tone. \"The boss?")
sh(56, "Who is that?\" Noorin asked, knitting her brows. \"Your forehead's swollen too,\" Naahidh said, without answering her question.")
sh(57, "Touching her head, Noorin told him not to bother about it and went back into the room. A little later, hearing another knock at the door, Noorin opened it.",
   [("door_close", "ކޮޓަރިތެރެއަށް", -22), ("knock", "ޓަކިޖަހާލި", -16), ("door_open", "ހުޅުވައިލިއެވެ", -22)])
sh(58, "Startled, Noorin looked at the young man standing in front of her. Realising he was the young man who had just saved her life, her astonishment grew.",
   [("gasp", "ސިހުންގެ", -22)])
sh(59, "As the young man pushed the door open and stepped into the room, Noorin's astonishment grew even more. He turned around",
   [("door_open", "ހުޅުވައިލާފައި", -22)])
sh(60, "and looked at Noorin, who stood by the door staring in amazement. Holding out the ice pack in his hand, the young man said,")
sh(61, "\"Naahidh said your head got hurt, that it needs ice.\" \"The boss,\" slipped softly from Noorin's lips. \"Not the boss — Uvaish.\"", hum=True)
sh(62, "Uvaish said, taking two steps towards Noorin. As Noorin stood looking at him, he came forward towards her and stopped very close.",
   [("footsteps_pavement", "ދެފިޔަވަޅެއް", -24)])
sh(63, "At that moment the door slipped from Noorin's bashful hand and slowly swung shut. He pointed her to a sofa to sit on.",
   [("door_close", "ލެއްޕުނެވެ", -20)])
sh(64, "Shyly, Noorin went and sat down on the sofa. Uvaish sat on the small coffee table in front of the sofa,",
   [("cloth_rustle", "އިށީނެވެ", -24)])
sh(65, "and put the ice pack to the swollen spot on Noorin's head. \"Ouch.\" The sudden pain escaped in Noorin's voice. \"Does it hurt a lot?\"",
   [("gasp", "އައުޗް", -22)])
sh(66, "Uvaish asked. \"A little,\" Noorin answered softly. Uvaish kept gazing at Noorin's face. Could he ever forget that face?", hum=True)
sh(67, "Two months earlier, it was a night in the rainiest days of the year. How many days had he searched for this young woman who fainted on Majeedhee Magu and fell at his feet?",
   [("rain_start", "ވިއްސާރަކުރި", -20)])
sh(68, "He could not forget that night's scene even in his dreams. What would have happened if he had not saved this young woman's life that night? And yet,")
sh(69, "without waiting for him she had left only a \"thank you\" note. Two months later, while he was sorting the files of the staff of the resort he was building,",
   [("paper_shuffle", "ފައިލްތައް", -20)])
sh(70, "by chance Uvaish came across Noorin's file. Without wasting a moment, he came to the resort late that night.",
   [("page_turn", "ފައިލް", -22)])
sh(71, "And by chance, today again, he had become the means of saving Noorin from harm.", hum=True)
sh(72, "Under Uvaish's gaze, Noorin seemed to want to flee. The intensity of that gaze unsettled her.")
sh(73, "With a bashful look, Noorin raised her head and looked at Uvaish. The moment their eyes met, Noorin quickly lowered her head.",
   [("heartbeat", "ހަތަރުކަޅި", -22)])
sh(74, "\"Why lower your head?\" Uvaish asked. Instead of answering, Noorin moved the hand holding the ice pack away.")
sh(75, "And she tried to get up from the sofa. At that moment Uvaish stopped her rising and sat her back down on the sofa. \"I came here only to meet Noorin.\"")
sh(76, "Uvaish said, leaning a little towards Noorin. \"To meet me?\" burst suddenly from Noorin's lips.")
sh(77, "Uvaish took a deep breath and stood up. Noorin sat looking at Uvaish, not knowing any reason why this young man would want to meet her.",
   [("breath", "ނޭވާއެއް", -22)])
sh(78, "Uvaish slipped a hand into his pocket and took out a scrap of paper. Noorin kept looking at Uvaish in surprise.",
   [("paper_shuffle", "ކަރުދާސްކޮޅެއް", -22)])
sh(79, "And suddenly embarrassment showed on her face and she rose from the sofa. \"I'm sorry... that day I...\"",
   [("cloth_rustle", "ތެދުވެވުނެވެ", -24)])
sh(80, "Noorin began. \"I came here to find something Noorin stole,\" Uvaish said, looking at Noorin. Noorin's astonishment grew.")
sh(81, "She stared at Uvaish without blinking, as if asking what it was she had stolen. That day she had left that house carrying only her own bag.")
sh(82, "\"I didn't steal anything,\" Noorin said anxiously. She thought. That day she had come away without locking the door of the house.")
sh(83, "At that moment her heart told her that a thief must have got into that house. \"I'm so very sorry, that day I came away without locking the door.")
sh(84, "Perhaps a thief got into your house at that time,\" Noorin said, as best she could think. Uvaish smiled.")
sh(85, "And the seriousness left his face, and a playful mood showed instead. Noorin stood dreading what Uvaish would say.")
sh(86, "She did not even know how valuable the thing lost from that house was. Just as Noorin opened her mouth to speak, at Uvaish's movement her words stopped,")
sh(87, "and her eyes went wide. Noorin stood without a thought; at this movement of Uvaish's it was as if her breath had stopped.",
   [("gasp", "ނޭވާ", -22)], hum=True)
sh(88, "The beating of her heart raced and her whole body froze. Unable to move, her feet were rooted to the floor. Uvaish smiled mischievously.",
   [("heartbeat", "ވިންދު", -18)], hum=True)
sh(89, "\"Learn to say something other than sorry and thank you,\" he whispered softly near Noorin's ear.",
   [("breath", "ވައިއަޑުން", -24)], hum=True)
sh(90, "Even then Noorin stood frozen, unable to move. Smiling, Uvaish walked towards the door.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(91, "And after going a little way, he turned back and looked at Noorin. Even then Noorin stood frozen on the spot.", hum=True)
SHOTS = S

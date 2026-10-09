"""Beat/shot plan for Milahanduvaru episode 253 (used by plan_beats.py)."""

LOC = {
    "bedroom": "Shamaan's small plain bedroom in an old Maldivian coral-stone house, whitewashed walls, a simple wooden double bed with a plain white sheet, a small wooden bedside table, a wooden window with faded curtains, a woven mat on the tiled floor",
    "office_door": "the entrance of a small government office building on a Maldivian island, a glass door in a white-painted wall, a small plain wall-mounted fingerprint scanner device beside the door with no screen text, potted plants",
    "office": "a small modest island office room, a few simple wooden desks with closed files and computer monitors turned away from the viewer, white walls, a window with louvred shutters showing palm trees outside, a slow ceiling fan",
    "inlaw_yard": "the sandy front yard of a small old coral-stone house on a Maldivian island, a low coral-stone boundary wall with a wooden gate, a traditional joali rope seat under a shady breadfruit tree, potted plants, a white-painted veranda",
    "lane_pm": "a narrow sandy lane of a small Maldivian island village between low coral-stone walls, coconut palms and breadfruit trees, simple houses with tin roofs",
    "bedroom_dusk": "Shamaan's small plain bedroom in an old Maldivian coral-stone house, whitewashed walls, a simple wooden bed with a plain sheet, a wooden chair with a folded towel over its back, an open wooden window looking out on palm tops and a distant small white mosque minaret",
    "yard_night": "the sandy yard of Shamaan's family home, an old single-storey coral-stone house with a tin roof, a traditional joali rope seat under a big leafy tree, a low coral-stone wall with an open wooden gate onto a dark sandy lane, a single bulb over the veranda door",
    "kitchen": "the small plain kitchen of an old Maldivian house, a simple two-burner gas stove with aluminium pots, a wooden shelf with plates and jars, whitewashed walls, a small window onto the dark yard",
    "memory_old": "a faded remembered room of an old Maldivian coral-stone house about thirty years ago, a wooden bed with a plain sheet, a woven palm-leaf baby cradle hanging from a beam, an open wooden window",
    "memory_boy": "the front step of an old Maldivian coral-stone house about twenty-five years ago, a sandy yard, a breadfruit tree, a wooden door",
    "memory_zihuna": "a hazily remembered small sitting room of a Maldivian house at night, a simple cushioned sofa, a dim lamp, a doorway opening onto a dark corridor",
    "lane_am": "a sandy lane of a small Maldivian island village in the morning, low coral-stone walls with bougainvillea, coconut palms, simple houses, a few distant bicycles",
    "naasira": "the dim doorway of an old coral-stone house on a Maldivian island, a heavy dark wooden door, long shadows across a sandy yard",
    "lane_walk": "a long straight sandy lane of a small Maldivian island village, low coral-stone walls, coconut palms and breadfruit trees, the family's house gate at the far end",
    "yard_day": "the sandy yard of Shamaan's family home, an old single-storey coral-stone house with a tin roof and an open wooden front door, a traditional joali rope seat under a big leafy tree, a low coral-stone wall",
}
MOOD = {
    "bedroom": "night, warm amber glow of a small bedside lamp against deep indigo shadows, tender, quiet and protective",
    "office_door": "early morning, fresh soft tropical daylight, slightly hurried",
    "office": "late morning, soft cool daylight through the shutters, a quiet, lonely, heavy-hearted mood",
    "inlaw_yard": "late afternoon, warm golden sunlight filtering through the leaves, long soft shadows, gentle and bittersweet",
    "lane_pm": "late afternoon, warm golden low sun through the palms, long shadows on the sand, warm family feeling",
    "bedroom_dusk": "evening twilight turning to night, deep blue light through the window, the room dim, tired stillness",
    "yard_night": "night after the Isha prayer, deep indigo darkness, faint silver-blue moonlight, one weak bulb by the door, eerie and silent",
    "kitchen": "night, a single warm ceiling bulb, amber light and teal shadows, tense",
    "memory_old": "faded sepia-toned memory with soft hazy edges and a gentle vignette, dim afternoon light, sorrowful",
    "memory_boy": "faded sepia-toned memory with soft hazy edges and a gentle vignette, pale afternoon light, lonely and wistful",
    "memory_zihuna": "hazy dreamlike memory at night, desaturated indigo with a dim amber lamp, soft blurred edges, uneasy and anxious",
    "lane_am": "morning, soft clear tropical daylight, the mood turning tense and uneasy",
    "naasira": "hazy imagined moment, dim grey-blue light, deep shadows, cold suspicion, soft blurred edges",
    "lane_walk": "late morning, harsh bright sunlight with hard shadows, tense and angry",
    "yard_day": "late morning, bright daylight dappled through the leaves of the big tree, tense and emotional",
}

BEATS = [
    dict(to=4, reason="episode opening: night, Shamaan holds Yameen and whispers his promise", chars=["shamaan", "yameen"], loc="bedroom",
         visual="Shamaan sitting on the edge of the bed holding sleepy toddler Yameen against his chest, leaning his cheek close to the boy's ear and whispering, his eyes tender and determined; Yameen relaxed and safe in his arms, eyelids heavy; the bedside lamp glowing warm",
         camera="medium close-up, eye level, faces in the upper half, the plain sheet and floor as a calm lower third", amb="room_night"),
    dict(to=7, reason="time and scene change: the next morning, he reaches the office just in time", chars=["shamaan"], loc="office_door",
         visual="Shamaan, slightly out of breath with a bag strap over his shoulder, pressing his fingertip onto a small plain wall-mounted fingerprint scanner beside the glass office door, glancing at his wristwatch, his face tired and distracted",
         camera="medium shot, three-quarter side view, eye level", amb="office_day", transition="black"),
    dict(to=11, reason="action change: alone at his desk, lost in grief for Zihuna", chars=["shamaan", "zihuna"], loc="office",
         visual="Shamaan sitting alone at his office desk, chin resting on his hand, staring blankly towards the shuttered window with sad lonely eyes; in the soft window light a faint translucent dreamlike memory of Zihuna smiling gently, like a soft glowing reflection, clearly only a memory",
         camera="medium shot, eye level, Shamaan in the lower-middle, the memory glow in the upper part of the frame", amb="office_quiet",
         sens="other", safe="Zihuna's death is never shown; she appears only as a soft smiling translucent memory"),
    dict(to=14, reason="character enters: colleague Vaasif sits by his desk and jokes", chars=["shamaan"], loc="office",
         visual="a cheerful Maldivian colleague about 30 (Vaasif) in a white short-sleeved polo shirt and beige trousers sitting sideways on a chair beside Shamaan's desk, grinning and leaning in with a teasing gesture; Shamaan at his desk letting out a deep sigh, eyes downcast, unsmiling",
         camera="medium two-shot, eye level", amb="office_day"),
    dict(to=17, reason="scene change: after work he visits Zihuna's mother and younger sister", chars=["shamaan"], loc="inlaw_yard",
         visual="Shamaan standing just inside the wooden gate of the sandy yard, giving a small sad smile; on the joali under the tree sit Zihuna's mother, a gentle Maldivian woman about 50 in a dark-green long-sleeved libaas and a grey headscarf, and her teenage younger daughter in a long navy dress and a white hijab, both turning towards him with warm eager faces as if asking a question",
         camera="medium wide, eye level, from slightly behind Shamaan's shoulder", amb="island_house_day"),
    dict(to=20, reason="scene and character change: in the lane he meets his father carrying Yameen", chars=["shamaan", "yameen", "shamaan_father"], loc="lane_pm",
         visual="in the sandy lane Shamaan happily lifting toddler Yameen from his old father's arms, smiling; Yameen pouting with a crumpled unhappy face, twisting round and stretching one small arm back towards his grandfather; the grandfather in his white skullcap smiling patiently beside them",
         camera="medium wide, eye level", amb="village_day"),
    dict(to=22, reason="time and action change: exhausted, he falls asleep at home until the Isha call", chars=["shamaan"], loc="bedroom_dusk",
         visual="Shamaan asleep fully dressed on top of the plain sheet, lying on his side with one arm under his head, face tired and peaceful; a folded towel over the chair back; through the open window the twilight sky deepening to night with a distant small white minaret silhouette",
         camera="medium wide, slightly high angle", amb="home_night", transition="black",
         sens="clothing", safe="the shower is only mentioned: he is shown fully dressed asleep, a towel on a chair"),
    dict(to=24, reason="scene and action change: alone on the joali at night, a figure seems to slip out of the house", chars=["shamaan"], loc="yard_night",
         visual="Shamaan sitting on the joali under the big tree in the dark yard, turning his head sharply towards the gate with a puzzled uneasy face; far away by the open gate a dim indistinct figure in dark clothing and a headscarf, seen only from behind as a soft blurred silhouette, slipping out into the dark lane",
         camera="wide shot, eye level, Shamaan in the middle of the frame, the gate in the background, sandy ground as a calm lower third", amb="island_house_night",
         sens="other", safe="the eerie figure is only a distant blurred silhouette from behind, no face, nothing frightening"),
    dict(to=26, reason="character enters: his mother comes back into the yard", chars=["sakeena", "shamaan"], loc="yard_night",
         visual="Sakeena stepping in through the wooden gate into the yard under the weak bulb light, her face calm and ordinary; Shamaan half sitting up on the joali, propped on one elbow, looking at her with a slightly frightened, questioning face",
         camera="medium wide, eye level", amb="island_house_night"),
    dict(to=28, reason="scene and action change: in his room he notices an amulet on Yameen's arm", chars=["yameen", "shamaan"], loc="bedroom",
         visual="toddler Yameen crawling happily on the woven mat on the bedroom floor near a small toy; a thin plain black cord tied around his small upper arm, seen small and unremarkable; Shamaan crouching nearby frowning at the boy's arm with a displeased, unbelieving look",
         camera="medium wide, low eye level", amb="room_night",
         sens="other", safe="the amulet is a tiny plain cord seen at a distance, never in close-up and with no writing"),
    dict(to=30, reason="scene change: he confronts his mother in the kitchen", chars=["shamaan", "sakeena", "yameen"], loc="kitchen",
         visual="Shamaan holding toddler Yameen on his hip and gesturing towards the child's arm with an angry, upset face; Sakeena standing by the stove turned towards him, answering calmly with a defensive, worried look; a clear gap between them",
         camera="medium two-shot, eye level", amb="home_night"),
    dict(to=33, reason="action and place change: his mother knocks, comes into his room and sits on the bed", chars=["sakeena", "shamaan", "yameen"], loc="bedroom",
         visual="Sakeena sitting on the edge of the bed with her hands folded in her lap, her face heavy with disappointment and sorrow as she begins to speak; Shamaan standing by the closed door with his arms crossed, upset, then turning to her in alarm; toddler Yameen asleep at the far side of the bed",
         camera="medium wide, eye level", amb="room_night"),
    dict(to=36, reason="flashback: Sakeena's illness when she was twenty and the healer who cured her", loc="memory_old",
         visual="faded memory: a pale young Maldivian woman about twenty in a maroon long-sleeved dress and beige headscarf sitting weakly on the wooden bed, one hand pressed to her forehead, eyes half closed; a baby boy sleeping in the woven cradle beside her; an old village healer in white clothes seated cross-legged at a respectful distance with his open palms raised in prayer",
         camera="medium wide, eye level", amb="memory", transition="dissolve",
         sens="other", safe="her illness and fainting are shown only as weakness on the bed; the healer only with open palms, no amulets or script"),
    dict(to=37, reason="emotional turning point: Shamaan weeps for his mother's suffering", chars=["shamaan", "sakeena"], loc="bedroom",
         visual="Shamaan sitting on the edge of the bed beside his mother, tears running down his cheeks, looking at her with grief; Sakeena turned towards him, her eyes sad and tender",
         camera="medium close two-shot, eye level", amb="room_night", transition="dissolve"),
    dict(to=40, reason="flashback: his own childhood illness and late speech", loc="memory_boy",
         visual="faded memory: a thin quiet Maldivian boy about seven in a pale shirt and shorts sitting alone on the front step of the old house hugging his knees, silent and wistful, watching other children's shadows far away in the yard",
         camera="medium wide, eye level", amb="memory", transition="dissolve"),
    dict(to=44, reason="back to mother and son talking (reuse of the two-shot)", reuse="beat_014", chars=["shamaan", "sakeena"], loc="bedroom",
         visual="(reuse) Shamaan and Sakeena sitting on the edge of the bed talking", amb="room_night", transition="dissolve"),
    dict(to=48, reason="flashback: Zihuna felt watched, lost sleep and had headaches before she died", chars=["zihuna"], loc="memory_zihuna",
         visual="hazy memory: Zihuna sitting alone on the sofa at night, one hand pressed to her temple, glancing anxiously over her shoulder towards the dark empty doorway, tired and frightened; nothing in the doorway but shadow",
         camera="medium shot, eye level", amb="memory", transition="dissolve",
         sens="other", safe="her fear is shown only through her face and an empty dark doorway; no figure, no illness or death shown"),
    dict(to=50, reason="action change: Shamaan looks at sleeping Yameen; his mother comforts him", chars=["shamaan", "sakeena", "yameen"], loc="bedroom",
         visual="Shamaan sitting on the edge of the bed looking worriedly at toddler Yameen asleep on the pillow; Sakeena standing beside him, gently resting her hand on his head, speaking softly with a calm, caring face",
         camera="medium shot, eye level", amb="room_night", transition="dissolve"),
    dict(to=52, reason="time change: later that night he lies awake and resolves to find the truth", chars=["shamaan", "yameen"], loc="bedroom",
         visual="late night, Shamaan lying awake on his back on the bed beside sleeping Yameen, eyes open and fixed, thinking hard; on the bedside table a small framed photo of a smiling young woman in a pale pink hijab catches the last of the lamplight",
         camera="medium shot from slightly above the bedside table", amb="room_night"),
    dict(to=57, reason="time and scene change: the next morning he meets Zihuna's best friend Fathuma", chars=["shamaan"], loc="lane_am",
         visual="in the morning lane Shamaan standing facing Zihuna's friend Fathuma, a young Maldivian woman about 25 in a long-sleeved peach dress and a cream hijab fully covering her hair, a handbag on her shoulder; they stand a clear respectful distance apart, Shamaan asking earnestly with an impatient strained face, Fathuma hesitant, holding her bag strap",
         camera="medium wide two-shot, eye level", amb="village_day", transition="black"),
    dict(to=61, reason="emotional turning point: she names aunt Naasira; the ground seems to slip from under him", chars=["shamaan"], loc="lane_am",
         visual="close on Shamaan standing in the lane, his face pale and stunned, eyes wide, one hand half raised to his chest, his body trembling; slightly out of focus a step away, Fathuma (peach dress, cream hijab) glancing away uneasily",
         camera="medium close-up, slightly low angle", amb="village_day"),
    dict(to=64, reason="imagined: his trusted aunt Naasira and the hidden plan he now suspects", loc="naasira",
         visual="a stern older Maldivian woman in a dark-brown long-sleeved libaas and a black headscarf seen only from behind, standing still in the dim doorway of an old coral-stone house, her long shadow stretching across the sandy yard, her face not visible",
         camera="wide shot, eye level, from behind at a distance", amb="memory", transition="dissolve",
         sens="other", safe="the suspected sorceress is never shown doing anything: a still figure from behind at a distance"),
    dict(to=67, reason="back to the lane: Fathuma repeats herself, Shamaan stands silent (reuse)", reuse="beat_021", chars=["shamaan"], loc="lane_am",
         visual="(reuse) Shamaan stunned in the lane, Fathuma glancing away", amb="village_day", transition="dissolve"),
    dict(to=70, reason="action change: furious, he heads straight home", chars=["shamaan"], loc="lane_walk",
         visual="Shamaan striding fast down the long sandy lane towards home, jaw clenched, fists tight at his sides, eyes burning with anger and grief, his shadow hard on the sand",
         camera="medium wide, front view, slightly low angle", amb="village_day"),
    dict(to=74, reason="scene and character change: he confronts his father on the joali", chars=["shamaan", "shamaan_father"], loc="yard_day",
         visual="the old father sitting on the joali under the big tree, lost in thought; Shamaan standing in front of him at arm's length, looking straight into his eyes and asking with a trembling, pained face; the father looking up, his face darkening with old painful memories",
         camera="medium wide two-shot, eye level", amb="island_house_day"),
    dict(to=76, reason="emotional peak: the father bows his head, Shamaan cries out in tears", chars=["shamaan", "shamaan_father"], loc="yard_day",
         visual="the father sitting on the joali with his head bowed low and his hands limp in his lap; Shamaan standing over him at arm's length, tears streaming down his face, one open hand thrown out in anguish as he cries out, nobody touching",
         camera="medium shot, eye level", amb="island_house_day", sens="violence",
         safe="the confrontation is words only: tears and a raised voice at arm's length, no touching or threat"),
    dict(to=77, reason="character enters: Sakeena rushes out of the house to calm him", chars=["sakeena", "shamaan", "shamaan_father"], loc="yard_day",
         visual="Sakeena hurrying out of the open front door of the house with one hand raised in a calming gesture and a worried, anxious face; in the foreground Shamaan standing tearful and the father seated with head bowed on the joali, all three at a distance from each other",
         camera="medium wide, eye level, from beside the joali towards the house door", amb="island_house_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "'My son, Papa does all this work just for you,' Shamaan whispered softly beside Yameen's ear.")
sh(2, "Yameen could not understand the deep meaning of those words, but in the shelter of his father's arms he felt safe.")
sh(3, "That night, as he lay down to sleep, Shamaan's heart held a new resolve. Facing every hardship in life,")
sh(4, "he would win a happy future for his father and his son. Today he believed that the alarm he heard every dawn was the start of a new step towards that future.")
sh(5, "Shamaan reached the office just in time. With only a few seconds to spare, he pressed his finger on the fingerprint scanner.",
   [("footsteps_pavement", "އޮފީހަށް", -22)])
sh(6, "This was his habit. Even at the office, he could not focus on the work he had to do.",
   [("keyboard_typing", "މަސައްކަތްތަކަށް", -24)])
sh(7, "Thoughts of his lonely life kept turning in his mind. Everyone he saw on the roads and at the office seemed so happy.")
sh(8, "But more than anything, it was Zihuna's sudden death that weighed on Shamaan's heart. Some people on the island put the blame for it on him.",
   hum=True)
sh(9, "They made all kinds of accusations. These stories hurt him deeply. He was never someone who tried to hurt anyone.",
   [("sigh", "ދެރަވެއެވެ", -22)])
sh(10, "Nor had he ever done anything that would make anyone work sorcery against him. Even when it came to love,")
sh(11, "he was not someone who kept many girlfriends like others did. His whole world was Zihuna. 'Hey, what are you sitting there lost in?")
sh(12, "Go and find yourself a nice girl around here,' Vaasif joked as he came and sat down by Shamaan's desk. 'I just can't get over this.",
   [("cloth_rustle", "އިށީނދެ", -24)])
sh(13, "Hearing what people say about Zihu's death hurts my heart so much,' Shamaan said with a deep sigh. 'Then forget about it.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(14, "That's over. Now steer a good course,' Vaasif said, resting his hand on Shamaan's shoulder, and walked out of the office.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(15, "When work was over, Shamaan headed home. But before going home, he decided to drop in at Zihuna's parents' house.")
sh(16, "When he entered the yard, Zihuna's mother and younger sister were sitting on the joali. The very first thing they asked on seeing him was where Yameen was.",
   [("footsteps_sand", "ވަންއިރު", -22)])
sh(17, "They loved Shamaan's son Yameen dearly. Some nights they even took him to their house to keep him there.")
sh(18, "He had not gone far from that house when he saw his father coming with Yameen. Shamaan happily went and hugged his son,",
   [("footsteps_sand", "އަންނަނިކޮށް", -24)])
sh(19, "and set off home. But Yameen resisted. Although Yameen was not yet old enough to talk,")
sh(20, "he showed what he wanted by crying and wriggling. Since the boy insisted, Shamaan walked home slowly on his own.",
   [("sob_breath", "ރޮއިގެންނާއި", -24), ("footsteps_sand", "ހިނގާފައި", -24)])
sh(21, "Back from the office, Shamaan was utterly exhausted. So he went home, showered and lay down for a while.")
sh(22, "He meant to go out once his son was brought home, but he fell asleep. He woke as the call to the Isha prayer was being made.")
sh(23, "He got up quickly, showered in the washroom by the well and came out to find no one in the house. Shamaan went outside and sat on the joali.",
   [("door_open", "ނިކުތްއިރު", -22)])
sh(24, "Just then it seemed someone came out of the house and went away; thinking it was his mother, he called out. But the person did not seem to hear.",
   [("footsteps_sand", "ނިކުމެގެން", -24)], hum=True)
sh(25, "Deciding it was only his imagination, he lay down again. A little later his mother came in from outside into the yard. 'Mother, wasn't that you who just went out?'",
   [("footsteps_sand", "ވަނެވެ", -22)])
sh(26, "Shamaan asked, a little frightened. 'Yes, I just went over to Alifulhube's house and came back,' his mother said casually.",
   [("breath", "ބިރުގެންފައި", -24)])
sh(27, "Shamaan took Yameen into his room. His father was still not back from the mosque. As Yameen crawled about the room, Shamaan's eye fell on an amulet on Yameen's arm.",
   [("door_open", "ކޮޓަރިއަށް", -22)])
sh(28, "Amulets and fanditha were something Shamaan had never believed in. At once he picked up his son and went to his mother in the kitchen.",
   [("footsteps_pavement", "ދިޔައެވެ", -24)])
sh(29, "'Who put this amulet on him?' Shamaan was deeply upset. 'That's an amulet I had put on so Yameen won't catch people's evil eye,' his mother Sakeena answered.")
sh(30, "'Oh Mother, with an amulet on his arm Yameen looks like an old toddy tapper,' Shamaan said angrily. He went into his room and slammed the door.",
   [("door_close", "ލެއްޕި", -14)])
sh(31, "He was hurt that things he didn't believe in were being done to his son. After a while his mother came and knocked on the room door.",
   [("knock", "ޓަކި", -18)])
sh(32, "When Shamaan opened the door, his mother came in and sat on the bed. Her face showed disappointment. 'When you were small,",
   [("door_open", "ހުޅުވުމުން", -20)])
sh(33, "your father's family did a lot of sorcery against us.' As his mother said this, Shamaan was frightened, and anger rose in him against his father's family.",
   [("gasp", "ބިރުގަނެ", -22)], hum=True)
sh(34, "'That was the year I turned twenty. You were only one year old. I started becoming very ill.")
sh(35, "The doctor said I was low on blood. But later I kept getting dizzy and collapsing. I was in a terrible state.")
sh(36, "A fanditha man who came to this island made me well. That's why, out of fear, I had the amulet put on Yameen's arm too,' his mother went on.")
sh(37, "Hearing his mother's story, Shamaan wept, thinking of the suffering she had borne. He thought: how wicked can people be?",
   [("sob_breath", "ރޮވުނެވެ", -22)], hum=True)
sh(38, "Shamaan remembered the illness he had as a child. He only began to speak properly at the age of twelve.")
sh(39, "Was that too the result of such a thing, he wondered. His mother's words filled Shamaan's heart with fear and unease.")
sh(40, "Were the health problems of his whole life, and his late speech, caused by that, he wondered.")
sh(41, "His heart began to ask whether some such secret might be hidden behind Zihuna's death too.",
   hum=True)
sh(42, "'Then why did you keep this secret for so long, Mother?' Shamaan asked softly. 'My son,")
sh(43, "I wanted to keep you away from those frightening memories. But the way things are going now, I feel you need to know everything.")
sh(44, "Even a few days before Zihuna died, I noticed some unusual things,' Sakeena said with a deep sigh.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(45, "'What kind of things?' Shamaan's eyes widened. 'Zihu used to say she always felt as if someone was following her.",
   [("gasp", "ބޮޑުވިއެވެ", -22)])
sh(46, "She said even when she sat alone in the house she felt someone was watching her. And she lost her sleep and began having frightening dreams,' his mother told him.",
   [("heartbeat", "ފާރަލާހެން", -22)], hum=True)
sh(47, "Shamaan remembered what Zihuna had told him a week before she died. She said her head ached all the time")
sh(48, "and her whole body was exhausted. Back then Shamaan thought it was from too much work. 'Then could they harm Yameen?'")
sh(49, "Shamaan looked at his son with worry. Yameen was lying asleep on the bed. 'That is exactly why I had the amulet put on him. For protection.")
sh(50, "My son, there are evil people in this world. To be safe from their envy, we must pay attention to our religion")
sh(51, "and seek Allah's mercy,' his mother said, stroking Shamaan's head. That night Shamaan could not sleep. He kept thinking of Zihuna.")
sh(52, "He resolved to find the truth about Zihuna's death. He wanted to know whether it was only an illness or something someone had done.",
   hum=True)
sh(53, "The next day, on the road to the office, Shamaan ran into Zihuna's closest friend, Fathuma. Seeing Fathuma, Shamaan stopped.",
   [("footsteps_sand", "މަގުމަތީގައި", -22)])
sh(54, "He hoped Fathuma might hold the answers to the many questions that had risen in his heart. 'Fathun, may I ask you something?")
sh(55, "Before Zihu died, did she talk about anyone? Or was she having trouble with someone?' Shamaan asked.")
sh(56, "His voice showed his patience wearing thin. 'Shamaan, actually Zihu said someone in your family was giving her a lot of trouble.")
sh(57, "But Zihu told me not to tell you, because it would hurt you if you knew,' Fathun said, a little hesitantly.")
sh(58, "Her face showed unease. 'Who? Who are you talking about?' Shamaan felt as if the ground was slipping from under his feet.",
   [("heartbeat", "ބިންގަނޑު", -18)], hum=True)
sh(59, "His pounding heart and his fear together set his whole body trembling. 'It's your aunt Naasira.",
   [("heartbeat", "ތުރުތުރުލާން", -20)])
sh(60, "She apparently said she had never approved of your marriage to Zihuna,", hum=True)
sh(61, "and that she would bring it to an end — that's what Zihu told me,' Fathun said, glancing away. Hearing this, Shamaan's mind went blank.",
   hum=True)
sh(62, "Aunt Naasira was one of the most trusted people in his family. But could such an evil plan be hidden behind that clean image?")
sh(63, "His heart drove him to find out what link there was between Zihuna's sudden parting and Naasira's warnings. 'Zihu lived in great fear.")
sh(64, "She wanted to save this marriage, but Naasira's displeasure was extreme.' Shamaan said nothing, lost in deep thought.")
sh(65, "Fathuma went on: 'Zihu lived in great fear. She wanted to save this marriage, but Naasira's displeasure was extreme,' Fathuma added.")
sh(66, "Shamaan said nothing, lost in deep thought. The suspicions about his aunt that had formed in his heart began to turn into certainty.")
sh(67, "He decided to find out the truth, whatever the sacrifice. Getting justice for Zihuna was now his greatest resolve.",
   hum=True)
sh(68, "Shamaan remembered some things his mother had told him before — the story of his father's family doing sorcery.")
sh(69, "Naasira was his father's eldest sister. All of this together filled Shamaan's heart with anger. His blood began to boil.",
   [("heartbeat", "ކެކެން", -18)], hum=True)
sh(70, "His patience gone, he set off home at once. He wanted to get the truth of this straight from his father.",
   [("footsteps_sand", "މިސްރާބު", -20)])
sh(71, "When he got home, his father was sitting on the joali in the yard, lost in deep thought. Shamaan strode up and stopped in front of him.",
   [("footsteps_sand", "ހިނގުމެއްގައި", -20)])
sh(72, "His face showed displeasure and grief. 'Father, what is the problem between Aunt Naasira and us?'")
sh(73, "Shamaan asked in a trembling voice, looking straight into his father's eyes. 'My son, those are very old stories.")
sh(74, "There's no point talking about them now.' His father's face changed at once, as if painful memories had been reopened.",
   [("sigh", "ހަނދާންތަކެއް", -22)])
sh(75, "He slowly lowered his head. 'There is a point, Father! Zihu may have died because of those people. They ruined my life!'",
   hum=True)
sh(76, "Shamaan's voice rose. Tears poured from his eyes. The suspicion that behind the death of his beloved wife Zihu",
   [("sob_breath", "ކަރުނަ", -22)], hum=True)
sh(77, "lay the hand of sorcery grew ever larger in his heart. 'Shamaan, calm down. Don't talk to your father like that.' At that moment his mother came out of the house. Worry showed on her face too.",
   [("door_open", "ނިކުތެވެ", -20)])
SHOTS = S

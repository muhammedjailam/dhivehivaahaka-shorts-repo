"""Beat/shot plan for Hayaath episode 319 (used by plan_beats.py)."""

LOC = {
    "house_front": "the front of uncle Waheed's old Maldivian coral-stone house at night, a low white-washed boundary wall with an open wooden gate, a warmly lit doorway, a sandy lane with a coconut palm and a single streetlight",
    "car": "inside a dark grey sedan at night, dim dashboard glow, the dark sea and the passing streetlights of a long seaside causeway road outside the windows",
    "link_road_memory": "the long seaside causeway road between two islands in the Maldives at sunset, turquoise lagoon on both sides, a low white sea wall, a few coconut palms",
    "windscreen": "a quiet seaside causeway road at night seen through a car windscreen, lit by the headlights, a row of streetlights, the dark sea on both sides",
    "moon_beach": "a secluded Maldivian beach at night under a full moon, white sand, dark coconut palms, gentle waves, a silver path of moonlight on the sea, a sandy track where a dark grey sedan is parked",
}
MOOD = {
    "house_front": "night, warm doorway light and a cool streetlight, tense and uneasy",
    "car": "night, very dim, soft dashboard glow and passing streetlight on faces, quiet and heavy",
    "link_road_memory": "sunset, warm golden light, soft and nostalgic, dreamlike",
    "windscreen": "night, bright headlights against blue darkness, a sudden jolt",
    "moon_beach": "night, silver full-moon light, deep blue shadows, quiet, lonely and longing",
}

BEATS = [
    dict(to=1, reason="new episode opening: night at the house gate, Yasir waits by the car as Hayaathu comes out", chars=["yasir", "hayaathu", "zoona", "areesha"], loc="house_front",
         visual="at night outside the coral-stone house a young man leans casually against a dark grey sedan by the open gate, empty hands in his pockets, straightening up as Hayaathu steps out of the lit doorway with eyes lowered; Zoona and Areesha follow her out of the doorway, curious",
         camera="wide shot, eye level", amb="night_exterior", sens="other",
         safe="Yasir smokes and throws away a cigarette in the narration: no cigarette is shown, he only leans on the car with empty hands"),
    dict(to=4, reason="characters change: Waheed arrives in his car and greets Yasir", chars=["waheed", "yasir", "hayaathu"], loc="house_front",
         visual="the bright headlights of a second car glowing behind; Waheed, just stepped out of it, smiling politely at the young man standing by the grey sedan; Hayaathu standing a little apart near the gate with her eyes lowered",
         camera="medium wide two-shot", amb="night_exterior"),
    dict(to=5, reason="Areesha's mocking remark; back to the group at the gate (reuse)", reuse="beat_001", chars=["yasir", "hayaathu", "zoona", "areesha"], loc="house_front",
         visual="(reuse) Yasir by the car, Hayaathu, Zoona and Areesha at the doorway", amb="night_exterior"),
    dict(to=7, reason="action change: Yasir opens the car door, Hayaathu hesitates at the stranger in the driver's seat", chars=["yasir", "hayaathu"], loc="house_front",
         visual="Yasir holding open the front passenger door of the dark grey sedan with a reassuring small nod; Hayaathu hesitating beside the door, looking at him worriedly; inside, behind the wheel, the dim silhouette of a man bent over a faintly glowing phone, his face hidden in shadow",
         camera="medium shot, slightly low angle", amb="night_exterior"),
    dict(to=8, reason="action change: the car drives off with Yasir following on a motorbike; the family stares", chars=["waheed", "zoona", "areesha", "yasir"], loc="house_front",
         visual="Waheed, Zoona and Areesha standing at the gate staring in surprise as the dark grey sedan pulls away down the lane, its red tail-lights glowing, and Yasir rides after it on a motorbike",
         camera="wide shot from behind the family", amb="street_night"),
    dict(to=11, reason="scene change: inside the car, Hayaathu beside the man she believes is the 'ugly' Fazaal", chars=["hayaathu", "young_driver"], loc="car",
         visual="inside the dim car Hayaathu sits stiffly in the front passenger seat, turned towards the window with tears gathering in her eyes; at the wheel Fazaal, his face softly lit by the dashboard, glances at her with a faint gentle smile",
         camera="medium two-shot from the back seat", amb="car_night", transition="xfade"),
    dict(to=12, reason="flashback: the same road with Maaroof", chars=["hayaathu", "maaroof"], loc="link_road_memory",
         visual="Hayaathu and Maaroof standing at a respectful distance beside the sea wall of a long causeway road at sunset, a motorbike parked nearby, both smiling shyly at each other, golden light on the lagoon",
         camera="wide shot, eye level", amb="memory", transition="dissolve"),
    dict(to=13, reason="action change: Fazaal offers her a tissue", chars=["young_driver", "hayaathu"], loc="car",
         visual="close-up inside the dim car: Fazaal holding out a folded white tissue towards Hayaathu; she takes it by its edge with her fingertips, their hands not touching, her tear-wet eyes still turned to the window",
         camera="close-up", amb="car_night", transition="dissolve"),
    dict(to=16, reason="emotional turning point: 'why did you agree to marry me?', the photo, her confession", chars=["hayaathu", "young_driver"], loc="car",
         visual="close-up of Hayaathu in the passenger seat with her eyes shut tight, tear tracks on her cheeks, a crumpled tissue in her hands; behind her, softly out of focus, Fazaal at the wheel turned towards her",
         camera="close-up", amb="car_night"),
    dict(to=17, reason="action change: sudden brake for a cat crossing the road", loc="windscreen",
         visual="seen through the windscreen of a stopped car, a small cat trotting safely across a quiet seaside road in the bright beam of the headlights, streetlights and the dark sea beyond, no people",
         camera="point of view through the windscreen", amb="car_night"),
    dict(to=19, reason="driving on, she stares out of the window (reuse)", reuse="beat_006", chars=["hayaathu", "young_driver"], loc="car",
         visual="(reuse) Hayaathu turned to the window, Fazaal at the wheel", amb="car_night"),
    dict(to=22, reason="action change: she speaks to him — 'how much did you pay for me?' — and begs", chars=["hayaathu", "young_driver"], loc="car",
         visual="inside the dim car Hayaathu half-turned towards the driver but with her eyes lowered, tears running, her face bitter and pleading; Fazaal with one hand on the wheel turning to her with a puzzled, concerned frown",
         camera="medium close two-shot through the windscreen", amb="car_night"),
    dict(to=24, reason="she refuses to look at him (reuse)", reuse="beat_009", chars=["hayaathu", "young_driver"], loc="car",
         visual="(reuse) Hayaathu with eyes shut, head bowed", amb="car_night"),
    dict(to=27, reason="scene change: a secluded beach under the full moon; Fazaal opens her door", chars=["young_driver", "hayaathu"], loc="moon_beach",
         visual="on a secluded moonlit beach the dark grey sedan is parked under coconut palms; Fazaal stands beside the open passenger door at a respectful distance, speaking gently; Hayaathu sits inside with her head lowered; a full moon over the sea",
         camera="wide shot", amb="beach_night"),
    dict(to=29, reason="action change: she walks to the sea and pulls away from him", chars=["hayaathu", "young_driver"], loc="moon_beach",
         visual="on the moonlit sand Hayaathu stepping quickly away towards the sea, startled, clutching her own wrist to her chest; a few steps behind her Fazaal stops with his hand half raised, surprised; the parked car in the background",
         camera="medium wide shot", amb="beach_night", sens="intimacy",
         safe="he grabs her hand in the narration: the touch is not shown, only the moment after, with the two standing apart"),
    dict(to=31, reason="action change: she stands alone at the water's edge in tears", chars=["hayaathu", "young_driver"], loc="moon_beach",
         visual="Hayaathu standing alone at the water's edge, gentle waves washing in around the hem of her long dress, tears glistening on her cheeks in the moonlight, looking out at the silver moon path; far behind her on the sand Fazaal is a small figure near the car",
         camera="wide shot from the side, the figure in the upper two-thirds", amb="beach_night"),
    dict(to=33, reason="her thoughts go to Maaroof (reuse of the memory image)", reuse="beat_007", chars=["hayaathu", "maaroof"], loc="link_road_memory",
         visual="(reuse) Hayaathu and Maaroof by the sea wall at sunset", amb="memory", transition="dissolve"),
    dict(to=34, reason="back to the shore as Fazaal walks towards her (reuse)", reuse="beat_016", chars=["hayaathu", "young_driver"], loc="moon_beach",
         visual="(reuse) Hayaathu at the water's edge, Fazaal behind", amb="beach_night", transition="dissolve"),
    dict(to=35, reason="flashback: the night he rescued her from the sea (reused image from ep 273)", reuse="ep273:beat_012", chars=["hayaathu", "young_driver"], loc="moon_beach",
         visual="(reuse from ep 273) Fazaal standing on the moonlit sand looking down in wonder at the rescued Hayaathu", amb="memory", transition="dissolve",
         sens="other", safe="the rescue itself is not shown (image from ep 273)"),
    dict(to=38, reason="focus moves to Fazaal: his racing heart and his feelings", chars=["young_driver"], loc="moon_beach",
         visual="Fazaal standing on the moonlit beach with one hand pressed to his chest, gazing ahead with wonder and longing, the sea and the full moon behind him",
         camera="medium close-up, low angle", amb="beach_night", transition="dissolve"),
    dict(to=41, reason="action change: he comes to stand beside her; she shuts her eyes in fear", chars=["hayaathu", "young_driver"], loc="moon_beach",
         visual="at the water's edge Fazaal stands an arm's length beside Hayaathu, looking at her tenderly; Hayaathu has her eyes squeezed shut and her face turned slightly away, tears on her cheeks, hands clasped tight",
         camera="medium two-shot, eye level", amb="beach_night", sens="intimacy",
         safe="his wish to hold her in his arms is never shown; they stand apart, not touching"),
    dict(to=44, reason="emotional turning point: his promise, and he sees her tears are for Maaroof", chars=["young_driver", "hayaathu"], loc="moon_beach",
         visual="on the moonlit shore Hayaathu stands on the left facing the sea in profile, eyes closed, tears on her cheeks, hands clasped; Fazaal stands well apart on the right, a clear arm's length of empty space between them, half-turned towards her, looking at her with sad tenderness and taking a deep breath; they do not touch",
         camera="medium two-shot, eye level, the two figures separated by open space", amb="beach_night"),
    dict(to=46, reason="closing image: the two of them apart under the full moon", chars=["young_driver", "hayaathu"], loc="moon_beach",
         visual="wide shot from behind: two small figures, a young man and a young woman in a rose dress and pink hijab, standing apart at the edge of a silver moonlit sea under a huge full moon, palms framing the sides",
         camera="wide shot from behind", amb="beach_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "When Hayaathu came out, a car was waiting at the gate, Yasir leaning against it with a cigarette. Seeing Hayaathu, he threw it away. Zoona and Areesha came out behind her. Just then her uncle Waheed drove up and stopped there.",
   [("car_approach", "އައިސް", -20)])
sh(2, "As the headlights fell on them, Yasir and Hayaathu looked that way. Waheed parked, got out, came over and smiled at Yasir. 'Going somewhere?' Surprised to find everyone outside, he asked — gently, for once.",
   [("car_door", "ފައިބައިގެން", -18)])
sh(3, "He didn't want to show his harsh temper in front of guests. 'Yes, Fazaal asked.' Yasir answered quite casually. 'Where is Fazaal?' Waheed asked, eager to see him. He had heard that Fazaal's face was ugly.")
sh(4, "And the photo he'd received had proved it true. Still, he wanted to see that face with his own eyes. But instead of answering, Yasir only gave a meaningful smile. 'Dad! How would Fazaal come out like that? Think a little!'")
sh(5, "Areesha said, in a tone that mocked Hayaathu. Yasir looked at Areesha in surprise, but said nothing; his eyes settled on Hayaathu. 'Let's go!' At that Hayaathu walked quietly over and stopped beside the car.",
   [("footsteps_pavement", "ހިނގުމެއްގައި", -24)])
sh(6, "Yasir opened the front passenger door for her. As she was about to get in, Hayaathu hesitated — someone else was sitting in the driver's seat. The light inside the car was very dim.",
   [("car_door", "ހުޅުވައިދިނެވެ", -18)])
sh(7, "The man sat with his head down, playing on his phone, its screen dimmed, so his face couldn't be seen. Hayaathu looked anxiously at Yasir; he smiled and nodded. So, hesitantly, she got in. Yasir shut the door and went to his motorbike.",
   [("phone_game_taps", "ކުޅެން", -24), ("car_door", "ލައްޕައިލުމަށްފަހު", -16)])
sh(8, "Zoona, Areesha and Waheed stood staring at Yasir in surprise. The car started and drove off, and Yasir followed on his motorbike. 'Was that Fazaal driving?' Zoona asked. 'Damn, I didn't even see his face. I wanted to embarrass Hayaathu,' said Areesha.",
   [("car_drive_off", "ދުއްވައިލުމުން", -16), ("motorbike_pass", "ސައިކަލުގައި", -18)])
sh(9, "'Haven't you done enough already?' Waheed said, going inside. With Yasir gone, unease filled Hayaathu's heart. She didn't dare look at the driver. She knew well what it meant for a girl to sit alone in the front seat: this was no ordinary driver.")
sh(10, "It was Fazaal himself, who had been engaged to her that very night. Perhaps his ugly looks had kept him from facing the family. At these thoughts tears welled in her eyes. Silently she turned her face away. At that moment Fazaal looked at her.",
   hum=True)
sh(11, "Seeing her turn away, a faint smile touched Fazaal's lips. In silence the car moved along the Link Road at an easy speed. Deep silence lay between them. Taking his eyes off the road for a moment, Fazaal looked at her.")
sh(12, "Hayaathu's gaze stayed on the scenery outside the window. This road was full of memories of countless rides with Maaroof. How could she ever leave those sweet, painful memories behind? To this day her heart belonged to Maaroof. Yet now she had to sit beside a complete stranger.",
   hum=True)
sh(13, "Her sorrow fell as tears. Seeing them, Fazaal took a tissue and held it out. 'Here...' he said gently. She looked at it, slowly took it, and wiped the tears from her cheeks. 'Thank you...' she whispered, looking out of the window again.",
   [("cloth_rustle", "ޓިޝޫއެއް", -24)], hum=True)
sh(14, "'Why did you agree to marry me?' came Fazaal's calm, manly voice. Hayaathu closed her eyes. She could find no answer. How could she explain the turmoil at home and what she was facing? So she chose silence.")
sh(15, "'I won't force anything on you, Hayaathu. I don't think you even looked at the photo I sent...' Fazaal said meaningfully. At the mention of the photo her heart began to pound. She was sitting beside the man with that frightening face.",
   [("heartbeat", "ވިންދު", -16)], hum=True)
sh(16, "At that thought her unease and anxiety grew even more. 'I'm in love with someone,' Hayaathu said softly. At that very moment the car braked hard. 'Lucky...' said Fazaal, his eyes fixed ahead.",
   [("brake_screech", "ޖައްސައިލިއެވެ", -14)])
sh(17, "Hayaathu thought he had stopped because of what she said. But the car had stopped for a cat crossing the road. 'Lucky the cat didn't end up under the car,' Fazaal said with a light smile. But Hayaathu sat as if she hadn't heard, staring out of the window. 'What did you just say?'")
sh(18, "Fazaal repeated, driving on. Hayaathu sat speechless, not knowing what to answer. When she kept looking outside as if she didn't want to talk, he spoke again: 'I didn't catch what you said... Are you marrying under some kind of pressure?' — knowing nothing of the truth.")
sh(19, "At that question her eyes filled with tears. Forced? Yes! This truly was a forced marriage. For her sister. For Maaroof. And for the love in her own heart. Could Fazaal, sitting beside her, ever understand all this? Even if she said it, would he believe her?",
   hum=True)
sh(20, "'How much did you pay to marry me?' Hayaathu asked without moving. 'What?' Fazaal asked, not catching it. 'What price did my uncle put on me?' she asked again. 'A price? What kind of talk is that?' Fazaal asked in surprise. But she didn't want to say more.")
sh(21, "'If you want to do something for me, arrange the wedding somewhere private... away from the family, too.' Crying, in a soft voice full of grief, she pleaded. Fazaal only smiled faintly. For he wanted the wedding held openly, grandly, in front of everyone.")
sh(22, "And to announce it to the whole world. 'Why?' Fazaal asked. 'I don't want anyone to hear any news of this marriage.' She began to sob. 'Are you ashamed?' he asked. 'I don't want anything else... I'm begging you... I won't ask you for anything ever again...'",
   [("sob_breath", "ގިސްލެވެން", -24)], hum=True)
sh(23, "As the sobs came, she couldn't go on. 'Look this way,' Fazaal said gently. But Hayaathu sat motionless, head bowed. If she saw Fazaal's face, she wouldn't even dare stay in the car.",
   [("sob_breath", "ގިސްލެވެން", -24)], hum=True)
sh(24, "Even seeing that face on a phone screen had filled her heart with fear. While Hayaathu sat like that,",
   [("heartbeat", "ބިރުވެރިކަމުން", -20)])
sh(25, "Fazaal drove on and stopped at a secluded place with no sign of people. It was a quiet, enchanting spot.")
sh(26, "The silver light of the full moon bathed the whole place. Fazaal got out of the car, came round and opened Hayaathu's door.",
   [("car_door", "ފައިބައިގެން", -18), ("car_door", "ހުޅުވާލިއެވެ", -20)])
sh(27, "As Fazaal came close, Hayaathu quickly lowered her head. 'Are you going to stay in the car?' Fazaal asked gently.")
sh(28, "Without even looking at him, Hayaathu slowly got out of the car and walked silently towards the beach. Fazaal shut the car door,",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22), ("car_door", "ލައްޕާލުމަށްފަހު", -16)])
sh(29, "hurried after her and caught her by the hand. Startled, Hayaathu instantly pulled her hand out of his.",
   [("footsteps_sand", "ހިނގުމެއްގައި", -22), ("gasp", "ސިހުމާއެކު", -18)], hum=True)
sh(30, "And as she strode towards the sea, tears streamed uncontrollably from her eyes.",
   [("footsteps_sand", "ހިނގައިގަތްއިރު", -22)], hum=True)
sh(31, "Her heart would never want anyone but Maaroof to touch her. As the waves touched her feet, Hayaathu stopped.",
   [("wave_crash", "ރާޅުބާނިތައް", -20)], hum=True)
sh(32, "She wondered: why had Fazaal brought her here? Tonight she had wanted to go out no matter what — to meet Maaroof.")
sh(33, "To steal a little time somehow and go to Maaroof. But the one who had brought her here was Fazaal.")
sh(34, "How would she ever meet Maaroof now? Slowly, step by step, Fazaal headed towards Hayaathu.",
   [("footsteps_sand", "ފިޔަވަޅުތައް", -24)])
sh(35, "It was as if some force was drawing him towards her. The feelings he had felt the night he saved Hayaathu from the sea began to grow in his heart again tonight.")
sh(36, "His heart raced until it hurt. He could not understand why his heart longed to touch that beautiful girl.",
   [("heartbeat", "ތެޅުން", -16)], hum=True)
sh(37, "In Dubai he had met many beautiful girls from many countries. But none of them had ever made him feel what he felt on seeing Hayaathu.")
sh(38, "Fazaal, who had never wanted to grow close to any girl except the beloved hidden deep in his heart,")
sh(39, "tonight wanted to draw Hayaathu into his arms and shelter her there. Slowly Fazaal went and stood beside her.",
   [("footsteps_sand", "ގޮސް", -24)])
sh(40, "At that moment, so as not to see his face, Hayaathu squeezed her eyes shut. Couldn't Fazaal sense the fear and unease in her heart?",
   hum=True)
sh(41, "In such a silent, lonely place, how could she bear to be with the man with that frightening face?", hum=True)
sh(42, "'I hope you will be faithful to me. I will give you, Hayaathu, sincere love and faithfulness.'")
sh(43, "Watching the tears falling from her eyes, Fazaal took a deep breath. Because deep in his heart he knew that he was not the true owner of those tears.",
   [("breath", "ނޭވާއެއް", -20)], hum=True)
sh(44, "Those tears were shed for Maaroof. And yet, before his own heart's desire, he was helpless.", hum=True)
sh(45, "It was because of Hayaathu that his heart had first begun to beat with love. Then how could he walk away from that love?", hum=True)
sh(46, "Today Hayaathu was his future wife. How could his heart ever let her go to become someone else's?", hum=True)
SHOTS = S

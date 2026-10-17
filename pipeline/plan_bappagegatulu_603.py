"""Beat/shot plan for Bappage Gatulu episode 603 — the SERIES FINALE (ends "ނިމުނީ").
Continuous from 586: the 8 pm rally hall, the police unit storms in, the Assistant Commissioner arrests Asim, Sameer and
Fareed; Fareed tries to run, Sameer gives up; Asim's threat (the pistol is NEVER shown — bible rule 12); Raaya begs and
kneels; Iyaan overpowers Asim; the three are led out; Iyaan thanks Raaya. Next morning: Zahir's grave in Malé's Aasahara
cemetery, Iyaan's dua with Aminath behind him, first tear in fifteen years, drizzle, peace.
Rules: bible 1-17 (no weapons, no handcuffs, nobody lying on the floor, crowds throw nothing, no touching between Iyaan
and Raaya, hijab fully covering hair on every woman, no readable text). Spec 5.4: speaker= on every dialogue shot."""

SUIT = ("Iyaan (reference used for his face only) wears a black suit jacket and black trousers over a plain black "
        "crew-neck top, no tie, NOT the plain black t-shirt of the reference")
WHITE = ("Iyaan (reference used for his face only) wears a plain white long-sleeved shirt and dark trousers, NOT the black "
         "t-shirt of the reference")
RAAYA = "Raaya in her loose long-sleeved ankle-length white dress and a light-grey hijab fully covering her hair and neck"
POLICE = "Maldivian police officers in dark-navy uniforms and caps, NO weapons, NO shields, NO handcuffs"
CROWD = "every woman in the crowd wears a hijab fully covering her hair and neck"
GAP = "a clear arm's-length gap between Iyaan and Raaya, they do not touch"

LOC = {
    "rally_hall": "a huge indoor convention-centre hall in Malé at night (8 pm), packed with seated and standing supporters, "
                  "a wide raised stage with a podium and microphones, two giant LED screens behind the stage glowing with "
                  "abstract images, plain teal-and-white drapes and flags with no symbols, TV cameras on tripods on a riser "
                  "at the back, bright white stage lights and cold teal shadows over the crowd, no text, no logos",
    "home_tv": "a small modest sitting room in a Malé home at night, a worn sofa, a low table with tea glasses, plain walls, "
               "a television set on a cabinet with its screen turned away from the viewer",
    "cemetery": "Malé's Aasahara cemetery the next morning: white sand ground, rows of low plain white Maldivian headstones "
                "with no inscriptions, tall shady trees, a low white boundary wall, overcast pale-grey morning light",
    "cemetery_rain": "Malé's Aasahara cemetery the next morning: white sand ground, rows of low plain white Maldivian "
                     "headstones with no inscriptions, tall shady trees, a low white boundary wall, overcast pale-grey "
                     "morning light",
}
MOOD = {
    "rally_hall": "present day, 8 pm, night inside the hall: hard bright white stage lights and bursting camera flashes, "
                  "cold teal shadows over the crowd, glowing abstract LED screens, red accents, shock and tension, noir",
    "home_tv": "present day, night, a dim room lit mainly by the cold blue flickering glow of the television on the faces, "
               "stunned silence",
    "cemetery": "the next morning, overcast pale-grey soft daylight, still air, gentle breeze in the leaves, quiet, sorrowful "
                "and peaceful, muted teal and grey tones with soft white sand",
    "cemetery_rain": "the next morning, a light cold drizzle falling in fine silver streaks, wet leaves and darkened sand, a "
                     "soft pale light beginning to break through the grey clouds, calm, release and peace",
}

BEATS = [
    # 001
    dict(to=2, reason="episode opening, scene: the hall's main doors burst open and a large police unit marches in",
         loc="rally_hall",
         visual=f"seen from the back of the packed hall: the big double doors flung wide open and a large unit of {POLICE}, "
                f"marching fast in tight formation down the centre aisle over the polished marble floor; the seated crowd "
                f"twisting round in their seats in shock; the bright stage far ahead; {CROWD}",
         camera="wide shot from just inside the doors, low angle, the marching officers and the crowd in the upper two-thirds, "
                "the empty polished marble aisle as the calm lower third", amb="hall_crowd",
         sens="other", safe="police 'in full kit' with shields: plain uniforms and caps, empty hands, no weapons, no shields"),
    # 002
    dict(to=4, reason="action change: the live-TV cameramen run forward and swing their cameras and flashes onto the stage",
         chars=["asim"], loc="rally_hall",
         visual="TV cameramen in dark clothes running along the side aisle with big shoulder cameras, others swinging their "
                "tripod cameras towards the stage, bright white flashes bursting; far ahead on the lit stage Asim stands at "
                "the podium, small, frozen in the glare",
         camera="medium wide shot from the side aisle, the cameramen in the foreground and the stage in the upper half, the "
                "marble floor as the lower third", amb="hall_crowd"),
    # 003
    dict(to=7, reason="character focus: Asim at the podium, fear and rage, sweat, veins, trembling — he still thinks they came for Iyaan",
         chars=["asim"], loc="rally_hall",
         visual="close-up of Asim behind the podium under the hard stage lights and flashes: beads of sweat on his brow, "
                "the veins on his neck standing out, his heavy face a mix of fear and rage, his jaw trembling, eyes darting "
                "towards the advancing officers off-frame",
         camera="close-up, slightly low angle, his face in the upper half, the dark podium top with microphones as the lower "
                "third", amb="hall_crowd"),
    # 004 speaker Asim
    dict(to=11, speaker="asim",
         reason="5.4 dialogue: Asim steps to the front of the podium and shouts orders into the microphone — framed on him",
         chars=["asim"], loc="rally_hall",
         visual="Asim leaning over the front of the podium, both hands gripping its edges, shouting furiously into the "
                "microphones, his mouth wide, eyes blazing with arrogance and rage, his face centred and sharp; camera "
                "flashes bursting around him; the giant LED screens glowing behind him; police officers soft and out of "
                "focus below the stage",
         camera="medium close-up on Asim from slightly below the stage, his face centred in the upper half and in sharp "
                "focus, the podium top as the lower third", amb="hall_crowd"),
    # 005
    dict(to=13, reason="character enters: the Assistant Commissioner walks with heavy steps straight towards Asim, a court order in hand",
         chars=["asst_commissioner", "asim"], loc="rally_hall",
         visual=f"the Assistant Commissioner striding up the centre aisle towards the stage with heavy, steady steps, his "
                f"face calm and unflinching, a plain white folded document held in his right hand; a line of {POLICE} "
                f"behind him; on the lit stage in the background Asim at the podium, eyes wide with disbelief",
         camera="medium wide shot from the stage steps looking back down the aisle, the officer's face in the upper half, "
                "the marble floor as the lower third", amb="hall_crowd",
         sens="other", safe="the court order is a plain white folded document, no text"),
    # 006 speaker Assistant Commissioner
    dict(to=16, speaker="asst_commissioner",
         reason="5.4 dialogue: the Assistant Commissioner reads out the arrest — framed on him, Asim from behind",
         chars=["asst_commissioner", "asim"], loc="rally_hall",
         visual="on the stage the Assistant Commissioner standing face to face with Asim, holding the plain white folded "
                "document up high in his right hand and speaking loudly and firmly, his face centred and sharp, steady "
                "eyes; Asim seen from behind over his shoulder, his grey-streaked hair and white shirt soft and out of "
                "focus at the left edge of the frame; the giant LED screens glowing behind",
         camera="over-the-shoulder medium close-up on the Assistant Commissioner, his face centred in the upper half and in "
                "sharp focus, the stage floor as the lower third", amb="hall_crowd",
         sens="other", safe="arrest announcement only; no handcuffs, no weapons; the document is blank"),
    # 007
    dict(to=19, reason="action change: the hall falls silent, then thousands erupt in anger at the politicians on stage",
         loc="rally_hall",
         visual=f"the packed hall on its feet: rows of ordinary Maldivian men and women standing up, shouting and raising "
                f"their open hands towards the stage, faces full of fifteen years of anger and shock, nothing in their "
                f"hands; {CROWD}; the bright stage with tiny figures far behind them",
         camera="wide shot from the side of the stage looking out over the crowd, faces in the upper two-thirds, the front "
                "row's empty floor as the lower third", amb="hall_crowd",
         sens="other", safe="crowd anger shown only as standing, raised hands and shouting; nothing thrown"),
    # 008
    dict(to=21, reason="location change: the whole nation watches the arrest live on TV",
         loc="home_tv",
         visual="a modest Maldivian family in their small sitting room at night — a grey-haired grandfather, a mother in a "
                "plain hijab fully covering her hair and neck and two teenage sons — leaning forward on a worn sofa, "
                "staring at a television whose screen faces away from the viewer, its cold blue glow on their stunned faces",
         camera="medium shot from beside the television, their faces in the upper half, the low table with tea glasses as "
                "the calm lower third", amb="home_night",
         sens="other", safe="the TV screen faces away; no text, no logos"),
    # 009
    dict(to=23, reason="emotional turning point: Asim's world spins — his power blows away; he steps back from the podium",
         chars=["asim"], loc="rally_hall",
         visual="Asim stepping back from the podium, his face blank and grey with shock, his eyes wide and empty, one hand "
                "lifted vaguely towards his chest, the stage lights glaring around him and the giant LED screens behind him "
                "blurring as if the whole hall were spinning",
         camera="medium close-up, slightly high angle, slow tilt, his face in the upper half, the dark stage floor as the "
                "lower third", amb="hall_crowd"),
    # 010
    dict(to=25, reason="character and action change: Fareed jumps up from his chair and runs for a secret door behind the stage",
         chars=["fareed"], loc="rally_hall",
         visual="Fareed in his navy pinstripe suit bolting from his chair at the back of the stage towards a dark plain door "
                "half hidden behind the teal drapes, his face terrified and glistening with sweat, eyes searching wildly for "
                "a way out, an empty overturned chair behind him",
         camera="medium shot from behind the drapes, his face in the upper half, the polished stage floor as the lower third",
         amb="hall_crowd"),
    # 011
    dict(to=27, reason="action change: officers catch Fareed before he gets out (the narration's tackle replaced)",
         chars=["fareed"], loc="rally_hall",
         visual=f"at the dark door behind the stage two {POLICE} stopping Fareed: he kneels upright on the marble floor, his "
                f"expensive pinstripe suit rumpled, sweat on his face, eyes wide with fear, each officer holding one of his "
                f"upper arms, his hands behind his back out of sight",
         camera="medium shot, eye level, Fareed's face in the upper half, the polished marble floor as the lower third",
         amb="hall_crowd",
         sens="violence", safe="'thrown to the ground and handcuffed' shown as kneeling upright between two officers, hands "
                               "behind his back out of frame; no handcuffs, nobody on the floor"),
    # 012
    dict(to=30, reason="character change: Speaker Sameer stands silent, head bowed, defeated, and is led off the stage",
         chars=["sameer"], loc="rally_hall",
         visual=f"Sameer standing on the stage with his head bowed, his round glasses catching the stage light, his eyes "
                f"full of despair and defeat, not resisting; two {POLICE} at either side of him, each with a hand on his "
                f"upper arm, his hands behind his back out of sight, leading him towards the stage steps",
         camera="medium shot, eye level, his face in the upper half, the stage floor as the lower third", amb="hall_crowd",
         sens="other", safe="the arrest without handcuffs: officers either side, hands behind his back out of frame"),
    # 013 speaker Asim (threat; the pistol is NEVER shown)
    dict(to=33, speaker="asim",
         reason="5.4 dialogue + sensitive: Asim, crazed, threatens everyone to stay back — framed tight on his face only",
         chars=["asim"], loc="rally_hall",
         visual=f"a tight close-up of Asim's face and shoulders only, his arms below the frame: his eyes red-"
                f"rimmed and wild, sweat streaming, mouth open in a hoarse shout, a man who has lost his mind, his face "
                f"centred and sharp; behind him {POLICE} stepping back with their empty open palms raised, soft and out "
                f"of focus",
         camera="tight close-up on Asim's face, centred in the upper half and in sharp focus, his white shirt collar and the "
                "dark background as the lower third, nothing else in frame", amb="hall_crowd",
         sens="violence", safe="rule 12: the grabbed pistol is never shown — only Asim's crazed face with his arms out of "
                               "frame, officers stepping back with empty raised palms"),
    # 014
    dict(to=35, reason="character change: Iyaan stands calm and unflinching as Asim's threat swings towards him",
         chars=["iyaan"], loc="rally_hall",
         visual=f"Iyaan standing still at the front of the stage, calm and unflinching, his hands empty at his sides, his "
                f"intense dark eyes fixed straight ahead on Asim off-frame, not a trace of fear; behind him the crowd frozen "
                f"and ducking low, soft and out of focus; {SUIT}",
         camera="medium close-up, eye level, his face in the upper half, his black suit and the stage floor as the lower "
                "third", amb="hall_crowd",
         sens="violence", safe="rule 12: the aimed pistol is never shown — only Iyaan's calm face facing off-frame"),
    # 015 speaker Raaya
    dict(to=38, speaker="raaya", transition="cut",
         reason="5.4 dialogue: Raaya screams and begs her father to stop — framed on her",
         chars=["raaya"], loc="rally_hall",
         visual=f"{RAAYA} standing on the stage, crying out 'Bappa!' with all her strength, tears running down her cheeks, "
                f"her face twisted with terror and grief, both open hands lifted a little in front of her, her face centred "
                f"and sharp; {POLICE} soft in the background, standing tense and still",
         camera="medium close-up on Raaya, her face centred in the upper half and in sharp focus, her white dress and the "
                "stage floor as the lower third", amb="hall_crowd"),
    # 016
    dict(to=40, reason="action change: Raaya sinks to her knees before her father and bursts into loud sobbing",
         chars=["raaya"], loc="rally_hall",
         visual=f"{RAAYA} kneeling upright on the stage floor, both hands pressed over her face, her shoulders shaking with "
                f"sobs; a man's polished black shoes and black trouser legs standing soft and out of focus at the edge of the "
                f"frame before her; hard stage light falling on her from above",
         camera="medium shot, slightly high angle, her face and hands in the upper half, the empty stage floor as the lower "
                "third", amb="hall_crowd",
         sens="other", safe="rule 15: kneeling upright with hands over her face; not lying"),
    # 017 speaker Iyaan
    dict(to=43, speaker="iyaan",
         reason="5.4 dialogue + emotional peak: Iyaan steps forward and dares Asim to shoot — framed tight on his face",
         chars=["iyaan"], loc="rally_hall",
         visual=f"a close-up of Iyaan's face as he steps forward, calm, defiant and fearless, his eyes locked on Asim "
                f"off-frame with fifteen years of cold fire in them, speaking slowly and firmly, his face centred and sharp; "
                f"a bright halo of stage light behind his head, the hall dark and blurred behind; {SUIT}",
         camera="close-up from a slightly low angle, his face centred in the upper half and in sharp focus, his black suit "
                "collar as the lower third, nothing in front of his face", amb="hall_crowd",
         sens="violence", safe="rule 12: the muzzle at his forehead is never shown — only his defiant face"),
    # 018 reverse shot: Asim's reply (reuse of 013)
    dict(to=44, speaker="asim", transition="cut", reuse="beat_013",
         reason="5.4 shot / reverse shot: Asim answers 'I'll finish you like your father' — reuse of his tight close-up",
         chars=["asim"], loc="rally_hall",
         visual="reuse of beat_013: tight close-up of Asim's crazed face, arms out of frame",
         camera="tight close-up", amb="hall_crowd",
         sens="violence", safe="rule 12: face only, the pistol never shown"),
    # 019
    dict(to=46, reason="action change: Iyaan forces Asim's arm up; the shot goes into the ceiling and plaster falls",
         chars=["iyaan", "asim"], loc="rally_hall",
         visual=f"seen from the hall floor looking up at the stage: a cloud of fine white plaster dust and a few small "
                f"flakes drifting down from the high ceiling through the hard stage lights; people in the front rows "
                f"ducking with their arms over their heads; on the stage, half veiled by the dust, Iyaan gripping Asim's "
                f"wrist and holding it high above their heads, both men's hands open and empty; {SUIT}; {CROWD}",
         camera="wide shot, low angle from the front rows, the dust and the two men in the upper half, the ducking heads "
                "of the crowd as the lower third", amb="hall_crowd",
         sens="violence", safe="rule 12: the shot is only plaster dust from the ceiling and ducking people; both hands empty, "
                               "no gun, no flash, no smoke"),
    # 020
    dict(to=48, reason="action change: Iyaan disarms and throws Asim down — shown as stance and stagger only",
         chars=["iyaan", "asim"], loc="rally_hall",
         visual=f"on the stage Iyaan in a low, balanced martial-arts stance, one open palm extended in front of him, his face "
                f"calm and controlled; a few steps away Asim staggering backwards off balance, arms flung out, hands empty, "
                f"his face shocked; no contact between them; {SUIT}",
         camera="medium wide shot, eye level, both faces in the upper half, the bare stage floor as the lower third",
         amb="hall_crowd",
         sens="violence", safe="rule 12/14: the disarm and the strike are never shown — only a stance and a stagger, no "
                               "contact, nothing on the floor"),
    # 021 speaker Iyaan
    dict(to=51, speaker="iyaan",
         reason="5.4 dialogue: Iyaan stands over Asim — 'This is the son of Ahmed Zahir… today justice is done'",
         chars=["iyaan", "asim"], loc="rally_hall",
         visual=f"Iyaan standing tall on the stage looking down, his face calm, cold and dignified, speaking firmly, his "
                f"face centred and sharp; in the foreground at the lower left Asim sitting on the stage floor propped up on "
                f"one hand, dishevelled, seen from behind over his shoulder, soft and out of focus; stage lights behind "
                f"Iyaan; {SUIT}",
         camera="low-angle over-the-shoulder medium shot on Iyaan, his face centred in the upper half and in sharp focus, "
                "Asim's soft shoulder and the stage floor in the lower third", amb="hall_crowd",
         sens="violence", safe="'lying on the ground' shown as Asim sitting on the stage floor propped on one hand"),
    # 022
    dict(to=53, reason="action change: the three political criminals are led out through the jeering crowd",
         chars=["asim", "sameer", "fareed"], loc="rally_hall",
         visual=f"down the centre aisle {POLICE} walking on either side of Asim, Sameer and Fareed, one behind the other, "
                f"each officer with a hand on a man's upper arm, the men's hands behind their backs out of sight, Asim "
                f"glaring, Sameer's head bowed, Fareed pale; on both sides the crowd on their feet shouting and raising "
                f"their open hands, nothing thrown; {CROWD}",
         camera="wide shot from the far end of the aisle, faces in the upper half, the empty marble aisle as the lower third",
         amb="hall_crowd",
         sens="other", safe="rule 14/16: no handcuffs (hands behind their backs out of frame); the crowd throws nothing"),
    # 023 reuse 016
    dict(to=55, reuse="beat_016",
         reason="return: Raaya still kneeling on the stage, sobbing — reuse of beat_016",
         chars=["raaya"], loc="rally_hall",
         visual="reuse of beat_016: Raaya kneeling upright on the stage floor, hands over her face",
         camera="medium shot", amb="hall_crowd",
         sens="other", safe="kneeling upright, not lying"),
    # 024 speaker Iyaan
    dict(to=57, speaker="iyaan",
         reason="5.4 dialogue: Iyaan comes to Raaya and thanks her (the narration's hand-take replaced, no touching)",
         chars=["iyaan", "raaya"], loc="rally_hall",
         visual=f"Iyaan standing before Raaya on the stage, his right hand placed on his own chest, bowing his head slightly "
                f"in respect and gratitude, his face gentle and soft for the first time, speaking quietly, his face centred "
                f"and sharp; {RAAYA} seen from the side at the left edge of the frame, soft and out of focus, rising to her "
                f"feet by herself; {GAP}; {SUIT}",
         camera="medium close-up on Iyaan, his face centred in the upper half and in sharp focus, the stage floor between "
                "them as the lower third", amb="hall_crowd",
         sens="intimacy", safe="rule 6/15: the narration has him take her hand and raise her — instead a hand-on-chest "
                                "bow while she rises by herself; arm's-length gap, no touching"),
    # 025 reverse shot: Raaya
    dict(to=58, transition="cut",
         reason="reverse shot: Raaya nods and wipes her tears",
         chars=["raaya", "iyaan"], loc="rally_hall",
         visual=f"{RAAYA} standing now, wiping a tear from her cheek with the back of her hand and giving a small nod, her "
                f"wet eyes calm and brave, a faint fragile smile; Iyaan's black-suited shoulder soft and out of focus at the "
                f"right edge of the frame; {GAP}",
         camera="medium close-up on Raaya, her face centred in the upper half, her white dress as the lower third",
         amb="hall_crowd"),
    # 026 cemetery
    dict(to=61, transition="black",
         reason="time jump and location change: the next morning at Zahir's grave; Iyaan prays, Aminath stands behind him",
         chars=["iyaan", "aminath"], loc="cemetery",
         visual=f"in the quiet cemetery Iyaan sitting on the white sand beside a low plain grave marked by a plain white "
                f"pointed headstone with no inscription, both palms raised in front of him in prayer, his head bowed; a step "
                f"behind him Aminath standing in her white hijab with her prayer beads, her tired eyes wet; tall trees "
                f"above, their leaves stirring; {WHITE}",
         camera="medium wide shot, eye level, both faces in the upper half, the smooth white sand as the calm lower third",
         amb="cemetery_dawn",
         sens="other", safe="a respectful Maldivian cemetery: plain uninscribed white headstone, prayer with raised palms; "
                            "Zahir never shown"),
    # 027 speaker Iyaan
    dict(to=63, speaker="iyaan",
         reason="5.4 dialogue + emotional peak: 'Bappa…' — his first real tear in fifteen years",
         chars=["iyaan"], loc="cemetery",
         visual=f"close-up of Iyaan's face in three-quarter view as he sits beside the plain white headstone, his palms "
                f"still raised before him, a single tear running down his cheek, his lips parted in a whisper, deep grief "
                f"and release in his eyes, his face centred and sharp; the white headstone and trees soft behind; {WHITE}",
         camera="close-up, eye level, his face centred in the upper half and in sharp focus, his raised palms and the white "
                "sand as the lower third", amb="cemetery_dawn"),
    # 028 speaker Iyaan
    dict(to=64, speaker="iyaan",
         reason="5.4 dialogue + action change: 'I kept my promise' — he rises and rests his hand on his mother's shoulder",
         chars=["iyaan", "aminath"], loc="cemetery",
         visual=f"Iyaan standing up beside his mother, his hand resting gently on her shoulder (mother and son), his face "
                f"calm and at peace, centred and sharp; Aminath beside him in her white hijab with her prayer beads, looking "
                f"up at her son with tearful pride; the plain white headstone behind them; {WHITE}",
         camera="medium shot, eye level, Iyaan's face centred in the upper half and in sharp focus, the white sand as the "
                "lower third", amb="cemetery_dawn",
         sens="intimacy", safe="mother and son only (allowed by rule 6)"),
    # 029 closing
    dict(to=66, reason="closing image: drizzle; the fifteen-year fire of revenge goes out; peace — The End",
         chars=["iyaan", "aminath"], loc="cemetery_rain",
         visual=f"seen from behind, Iyaan and Aminath walking slowly side by side along the sand path between the rows of "
                f"plain white headstones in a light silver drizzle, his arm protectively around her shoulders, the tall "
                f"trees dripping above, a soft pale light breaking through the grey clouds ahead of them; {WHITE}",
         camera="wide shot from behind, the two figures and the breaking light in the upper half, the wet sand path as the "
                "calm lower third", amb="rain_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "With a loud crash the convention centre's main doors swung open — a moment in which the unease filling the whole hall sank into shock and panic.",
   [("door_slam", "ހުޅުވިގެން", -16), ("crowd_gasp", "ސިހުމާއި", -20)])
sh(2, "Through those doors marched a large special police unit, in full kit. The sound of their boots and shields striking the hall's marble floor echoed through the whole place.",
   [("boots_march", "ބޫޓުތަކާއި", -18)])
sh(3, "The cameramen of the main media outlets broadcasting live picked up their cameras and began running up the sides.",
   [("footsteps_pavement", "ދުވަން", -22)])
sh(4, "The cameras' lights and flashes swung straight towards the stage. Home Minister Asim's face showed a mixture of fear and rage.",
   [("camera_shutter", "ފްލޭޝްތައް", -18)])
sh(5, "Sweat was pouring from his forehead. The veins in his neck stood out, swollen. His whole body was trembling.",
   [("heartbeat", "ތުރުތުރު", -22)])
sh(6, "Even then he believed the police under his political influence had come there to arrest Iyaan —")
sh(7, "for storming an official ceremony and causing a huge commotion, and for making such accusations against a powerful minister and acting on his own.")
sh(8, "To show the pride and arrogance in his heart he stepped to the front of the podium. Rage blazed in his eyes. \"Arrest him!",
   speaker="asim")
sh(9, "Seize him at once!\" Asim roared into the podium microphone. His voice echoed through the whole hall.",
   speaker="asim")
sh(10, "\"He is trying to topple the government. Smearing the leaders of the state with lies, what he has done is an illegal act.",
   speaker="asim")
sh(11, "He is a dangerous terrorist trying to take away this nation's security! Confiscate every electronic device he has!\"",
   speaker="asim", hum=True)
sh(12, "Asim's eyes widened in astonishment. Not a single officer obeyed his order. The Assistant Commissioner at the head of the unit walked with heavy steps straight towards Asim.",
   [("boots_march", "ފިޔަވަޅުތަކުގައި", -20)])
sh(13, "His face showed an unflinching firmness. In his right hand was a formal court order issued by the court that morning.")
sh(14, "He stopped in front of Asim, raised the order high and said, so loudly that the whole hall rang: \"Home Minister Asim,",
   [("paper_shuffle", "ހިއްލާލަމުން", -20)], speaker="asst_commissioner", hum=True)
sh(15, "Speaker of Parliament Sameer, and bank MD Fareed. You are now, for the politically planned killing in 2011 of the Member of Parliament Ahmed Zahir",
   speaker="asst_commissioner")
sh(16, "and on the charge of embezzling state funds, under arrest by a lawful court order.\"",
   speaker="asst_commissioner", hum=True)
sh(17, "The Assistant Commissioner's voice carried complete power and certainty. For a moment the whole hall fell silent.")
sh(18, "Then, in their shock, the many thousands of ordinary citizens in the hall began to shout.",
   [("crowd_roar", "ހަޅޭއްލަވަން", -16)])
sh(19, "Some stretched their arms towards the stage, venting their anger at the politicians who had deceived them for the past fifteen years.")
sh(20, "The people of the whole country, watching live on TV, were seeing this historic moment of justice. After the police headquarters' cyber division confirmed the authenticity of the digital evidence Iyaan had sent,")
sh(21, "the court, on the Prosecutor General's direct instruction, had issued the order to arrest these criminals. Asim's eyes went wide.")
sh(22, "It was as if the whole world were spinning around his head. All the power and pride he had built up for so long by abusing the position of the highest minister for internal security blew away into the wind.",
   [("heartbeat", "އެނބުރިގެން", -20)], hum=True)
sh(23, "The glory and splendour of mighty influence and black money ended in an instant. He stepped back. He could think of nothing more to do.")
sh(24, "He was caught in the net of the law. Bank MD Fareed leapt up from his chair in fear and, his whole body trembling, ran for a secret door behind the stage.",
   [("footsteps_pavement", "ދުއްވައިގަތް", -20)])
sh(25, "His eyes searched for any way to escape. Sweat poured from his forehead. But before he could get out through that door, the special police officers there at once")
sh(26, "seized him and brought him to the ground. Fareed's expensive Italian suit dragged across the marble floor.",
   [("soft_thud", "ވައްޓާލި", -22), ("cloth_rustle", "ކިލާވަމުން", -20)])
sh(27, "The officers pulled both his hands behind his back and cuffed them. Speaker of Parliament Sameer stood in silence with his head bowed.")
sh(28, "His whole political life — the influence and wealth he had built over fifteen years — shattered in a few seconds, and it went down his throat like bitter medicine.")
sh(29, "He made no attempt to resist. His eyes showed despair and the acceptance of defeat.")
sh(30, "Officers came, cuffed his hands and took him down from the stage. Asim still would not admit his guilt.")
sh(31, "His mind was filled with the black smoke of hatred and rage. Suddenly, from the waist of the police security guard standing beside him,",
   hum=True)
sh(32, "he snatched the pistol and pointed it straight at Iyaan's head. \"Stay back!",
   [("crowd_gasp", "ދަމައިގަތް", -18)], speaker="asim", hum=True)
sh(33, "Nobody come near! Or no one will be safe. Make way for me to get out of here!\" Asim's eyes had turned red. The man had lost his mind.",
   [("heartbeat", "ހަމައިން", -20)], speaker="asim")
sh(34, "Like a madman he swung the pistol from side to side. He was screaming at the top of his voice.",
   [("crowd_panic", "ހަޅޭއްލަވަމުން", -20)])
sh(35, "His hand was shaking terribly, but in the end he aimed the muzzle at Iyaan.")
sh(36, "Suddenly Raaya let out a loud scream. Her voice rang through the whole hall. Everyone fell silent. The police stood ready, their guns aimed.")
sh(37, "Raaya screamed: \"Bappa! Don't do this! What are you doing now?",
   speaker="raaya", hum=True)
sh(38, "Are you still trying to harm Iyaan? Bappa's truth is known to the whole nation now!\"",
   speaker="raaya")
sh(39, "Raaya could say no more. Filled with tears, she sank to her knees in front of her father.",
   [("cloth_rustle", "އިށީން", -22)])
sh(40, "At that she broke down and began to cry out loud. Iyaan stood looking straight into Asim's eyes, without the slightest fear or hesitation.",
   [("sob_breath", "ރޯން", -20)])
sh(41, "His face showed firmness. He took a step forward — so close that the end of the pistol almost touched his forehead.",
   [("heartbeat", "ގާތްވި", -18)], hum=True)
sh(42, "\"Shoot, Asim. Pull the trigger. Fifteen years ago, when you drove the blade into my father's body, my father did not kneel before you either.",
   speaker="iyaan", hum=True)
sh(43, "I won't be afraid of that gun of yours either. The days of your tyranny are over now.",
   speaker="iyaan")
sh(44, "Your end has come today.\" — \"I'll finish you too, just like your father!\"",
   speaker="asim", hum=True)
sh(45, "Asim tried to fire. In that very second, Iyaan's lightning-fast move forced Asim's arm upwards.",
   [("cloth_rustle", "ހިއްލާލި", -20)])
sh(46, "At that moment the loud sound of the pistol rang out. The bullet went into the hall's high ceiling. Pieces of the ceiling fell to the floor.",
   [("soft_thud", "އިވުނު", -20), ("crowd_gasp", "އުންޑަ", -18), ("soft_thud", "ފޭބި", -24)], hum=True)
sh(47, "Iyaan twisted Asim's arm and knocked the pistol to the floor. Then he struck Asim hard in the chest with his hand and threw him down onto the stage floor.",
   [("soft_thud", "ޖަހައި", -22)])
sh(48, "Asim fell with a loud thud. For the past fifteen years Iyaan had prepared for exactly this kind of moment —",
   [("soft_thud", "ވެއްޓުނު", -20)])
sh(49, "mastering every martial-arts training to use it. Iyaan stood over Asim.")
sh(50, "His gaze was fixed on the eyes of Asim on the floor. \"This is the son of the former honourable Member of Parliament Ahmed Zahir.",
   speaker="iyaan", hum=True)
sh(51, "Today justice has been done. Today the killer lies where he belongs.\" At Iyaan's move the police ran up and took control of Asim,",
   [("footsteps_pavement", "ދުވެފައި", -20)], speaker="iyaan")
sh(52, "pulled both his hands behind his back and cuffed them. The three political criminals began to be led out of the hall.")
sh(53, "From the crowd people shouted, throwing things towards them. The sounds of hatred spread through the whole place.",
   [("crowd_roar", "ހަޅޭއްލަވަމުން", -18)])
sh(54, "Raaya was still sitting on the floor, sobbing. The world of the father she had been so proud of had shattered completely.",
   [("sob_breath", "ގިސްލަމުން", -22)])
sh(55, "Though her heart was broken, she felt that she had fulfilled a great duty she owed to justice.")
sh(56, "Iyaan walked slowly over and stopped beside Raaya. He took Raaya's hand and raised her to her feet. \"Raaya... thank you.",
   [("footsteps_pavement", "ހިނގާފައި", -24)], speaker="iyaan", hum=True)
sh(57, "If it weren't for you, this justice would never have come today. What you did was a courageous act that changed history.\"",
   speaker="iyaan")
sh(58, "This time there was gentleness in Iyaan's voice. Raaya nodded and wiped away her tears. The morning of the next day.",
   [("breath", "ފޮހެލި", -24)])
sh(59, "Silence lay over Malé's Aasahara cemetery. Iyaan stood beside his father's grave. The leaves of the trees stirred gently in the breeze.",
   [("leaves_rustle", "ހެލެމުންދޭ", -18)])
sh(60, "Iyaan sat down beside his father's grave. He raised both hands and prayed for his father. Behind him stood his mother, Aminath.")
sh(61, "Tears ran from his mother's tired eyes — tears of a feeling that mixed the memory of Zahir, her son's courage and the sense of today's justice.")
sh(62, "\"Bappa...\" Iyaan said softly. For the first time in the past fifteen years a real tear fell from his eyes to the ground.",
   [("breath", "ބުނެލި", -24)], speaker="iyaan", hum=True)
sh(63, "\"The truth of your death is known to the whole nation now. Full justice has been done for your blood. Bappa...",
   speaker="iyaan", hum=True)
sh(64, "I have kept the promise I made to you.\" Iyaan stood up and rested his hand on his mother's shoulder. They began to walk out of the cemetery.",
   speaker="iyaan")
sh(65, "The cold drops of the fine drizzle falling at that moment put out completely the great fire of revenge that had burned in Iyaan's heart for fifteen years.",
   [("rain_start", "ވާރޭގެ", -16)], hum=True)
sh(66, "An unknown peace came over his whole being. Justice had been found for his father's murder. The End.",
   hum=True)
# spec 5.4: crop/focus for every dialogue shot, read off work/grid/new_*.jpg (face centre x, face y + ~8, clamped to range)
FOCUS = {
    8: ("medium", [48, 42]), 9: ("tight", [48, 35]), 10: ("medium", [48, 42]), 11: ("tight", [48, 35]),   # beat_004 Asim
    14: ("medium", [52, 42]), 15: ("tight", [52, 38]), 16: ("tight", [52, 38]),                          # beat_006 AC
    32: ("tight", [48, 44]), 33: ("tight", [48, 44]),                                                    # beat_013 Asim
    37: ("tight", [50, 35]), 38: ("medium", [50, 42]),                                                   # beat_015 Raaya
    42: ("tight", [48, 35]), 43: ("medium", [48, 42]),                                                   # beat_017 Iyaan
    44: ("tight", [48, 44]),                                                                             # beat_018 = 013 Asim
    50: ("tight", [55, 35]), 51: ("tight", [55, 35]),                                                    # beat_021 Iyaan
    56: ("tight", [50, 35]), 57: ("medium", [50, 42]),                                                   # beat_024 Iyaan
    62: ("tight", [48, 35]), 63: ("medium", [48, 42]),                                                   # beat_027 Iyaan
    64: ("tight", [42, 35]),                                                                             # beat_028 Iyaan
}
for _i, (_c, _f) in FOCUS.items():
    assert S[_i][2].get("speaker"), _i
    S[_i][2].update(crop=_c, focus=_f)
SHOTS = S

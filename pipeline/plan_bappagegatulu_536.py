"""Beat/shot plan for Bappage Gatulu episode 536 — v2 re-cut on the new audio (used by plan_beats.py). PRESENT timeline only (plus one memory).
v1 plan kept in output/BappageGatulu/v1/plans/."""

LOC = {
    "bank_office": "the managing director's corner office high in a modern glass bank tower in Malé, a large dark polished desk with a slim laptop, a black leather executive chair, floor-to-ceiling windows looking over the city rooftops and the turquoise sea, cold grey-and-steel interior with a few dark wood accents",
    "bank_it": "a cramped bank IT room behind the executive floor, a desk with three monitors showing abstract glowing network maps and graph lines, server racks with tiny blinking lights along one wall, cables, blinds half drawn",
    "lounge": "a secret private lounge on an upper floor in Hulhumalé, dark wood-panelled walls, heavy closed burgundy curtains, three deep leather armchairs around a low polished dark-wood table that is bare except for a few phones, dim brass floor lamps, no windows visible",
    "gallery": "the Athena Art Gallery in Malé, white walls hung with large modern oil paintings, a big oil painting of a red sun rising out of a black sea, polished concrete floor, soft track lighting, a big glass door",
    "hacker_room": "Iyaan's small locked bedroom-study in a modest apartment in Hulhumalé, a desk with three computer monitors glowing with abstract code lines and graphs, a keyboard and a pair of black over-ear headphones, a wall-sized investigation board with small faceless blurred photos linked by red string, window blinds drawn",
    "studio": "a silent rented art studio on the third floor of an old building in a quiet Malé lane, bare peeling plaster walls, blank canvases stacked against a wall, a paint-stained wooden table in the middle of the room with an open laptop on it, one tall old window with a dusty pane looking out over the narrow lane, a worn wooden floor, an old wooden door",
}
MOOD = {
    "bank_office": "present day, 9 am, cold bright morning daylight through the tall windows, glass and steel reflections, the screen's pale blue glow on his face, a sudden chill of dread",
    "bank_it": "present day, mid-morning, dim room lit mainly by the cold blue-and-teal monitor glow, thin stripes of daylight through the blinds, tense and suspicious",
    "lounge": "present day, late morning shut out by heavy curtains, low warm amber lamplight pooling on the table, deep charcoal shadows in the corners, thick tense silence, conspiratorial noir",
    "gallery": "memory, soft hazy desaturated light with a dreamlike vignette, the warm gallery lights blooming, the red sun painting glowing faintly behind them",
    "hacker_room": "present day, late morning, blinds drawn, thin blades of daylight across the room, the cold blue monitor glow on his face, quiet and dangerous",
    "studio": "present day, afternoon, grey overcast daylight falling through the dusty window, long soft shadows, dust in the air, hushed and heavy with emotion",
}

COUPLE_GAP = "a clear arm's-length gap between them, they do not touch"


# v2 re-cut on the new (slower) audio: v1 images reused via v1="beat_###"; NEW images only for spec 5.4 (speaker focus).
BEATS = [
    dict(to=4, v1="beat_001", reason="episode opening, scene and character: Fareed in his bank office at 9 am opens the secret email", chars=["fareed"], loc="bank_office",
         visual="Fareed sitting at his large dark desk, leaning towards the open laptop, the screen turned away from the viewer so only its pale blue glow lights his face; the colour has drained from his face, eyes wide and fixed, one hand frozen above the keyboard, the city and sea bright behind him through the windows",
         camera="medium shot from slightly to the side of the desk, his face in the upper third, the polished desk top as a calm lower third", amb="office_day",
         sens="other", safe="the payment receipts and the threat line are never shown; the screen faces away, only its glow on his face (no readable text)"),
    dict(to=7, v1="beat_002", reason="character and location change: his most trusted IT man traces where the email came from", chars=["fareed"], loc="bank_it",
         visual="a young bank IT man in a white short-sleeved shirt and lanyard sitting at three monitors full of abstract glowing network maps and connecting lines, pointing at one bright red node on the map; Fareed standing behind his chair, bent forward with one hand on the chair back, staring at the screens, his face darkening with fury",
         camera="medium wide over-the-shoulder shot from behind the monitors' side, faces in the upper half, the desk edge as the lower third", amb="office_day"),
    dict(to=10, v1="beat_003", reason="action change: Fareed, grinding his teeth, phones Speaker Sameer", chars=["fareed"], loc="bank_office",
         visual="Fareed standing at the floor-to-ceiling window of his office with his back half to the city, a phone pressed to his ear, jaw clenched and teeth gritted, his free hand balled into a fist against the glass, eyes narrowed with rage and suspicion",
         camera="medium close-up, eye level, his face in the upper third, the window frame and city below as a calm lower third", amb="office_day"),
    dict(to=11, v1="beat_004", reason="time jump and location change: two hours later, the three men meet in a secret private lounge in Hulhumalé", chars=["asim", "fareed", "sameer"], loc="lounge",
         visual="the three men in the dim private lounge: Sameer sitting back in a leather armchair at the left, calm, his hands folded over his stomach; Asim sitting forward in a second armchair at the right, glowering, his jaw set with anger; Fareed standing between and behind them, arms crossed, tense; heavy silence; the low table between them bare",
         camera="wide shot, eye level, the three faces in the upper half, the bare polished table as the calm lower third", amb="lounge_private", transition="black",
         sens="other", safe="the narration says Sameer is smoking: shown seated with his hands folded instead; nothing in his hands, no smoke"),
    dict(to=14, v1="beat_005", reason="action change: Asim slams his palm on the table and denies sending the email", chars=["asim", "fareed"], loc="lounge",
         visual="Asim leaning forward out of his armchair, his palm pressed flat on the polished table top, his face hard and furious as he shouts up at Fareed; Fareed standing on the other side of the table, glaring down at him",
         camera="medium two-shot from a low angle across the table, faces in the upper half, the table top with Asim's flat hand as the lower third", amb="lounge_private",
         sens="violence", safe="anger only as a palm pressed flat on the table and a raised voice; no strike"),
    dict(to=15, v1="beat_006", reason="action change: Fareed throws his phone down in front of Asim and accuses him", chars=["fareed", "asim"], loc="lounge",
         visual="Fareed leaning over the low table, having just tossed his phone onto it in front of Asim, the phone lying face-up with a dark blank screen, Fareed's finger jabbing towards it, his face twisted with accusation; Asim seated, staring at the phone, then up at Fareed, stunned and angry",
         camera="medium shot from the side of the table, faces in the upper half, the phone on the table top in the lower third", amb="lounge_private"),
    dict(to=19, v1="beat_007", reason="focus moves to Sameer: he shouts 'Stop!' and calmly explains the intruder used Asim's IP", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer in the foreground in his armchair, calm and certain, his round glasses catching the amber lamplight, slowly turning a silver pen between his fingers while he looks from one man to the other; Asim and Fareed in soft focus behind the table, listening, their anger cooling into doubt",
         camera="medium close-up on Sameer, eye level, his face in the upper third, the others blurred behind, the table edge as the lower third", amb="lounge_private",
         sens="other", safe="the narration has him flick cigarette ash: shown turning a silver pen between his fingers instead; no smoke"),
    # NEW (5.4): Asim speaks; in the v1 wide three-shot he sits at the right edge (face x≈76 %) and cannot be centred
    dict(to=21, speaker="asim", reason="5.4 dialogue focus: Asim, now afraid, asks who it could be — the wide three-shot cannot centre him (he sits at the frame edge)", chars=["asim", "fareed"], loc="lounge",
         visual="Asim sitting forward on the edge of his leather armchair, centred in the frame, his face turned towards the camera in three-quarter view, the anger gone from it, his eyes uneasy and fearful, a sheen of sweat on his brow, lips parted as he asks a frightened question; Fareed standing behind him at the side, small, soft and out of focus, glancing at him uneasily; the bare polished table edge in front",
         camera="medium close-up on Asim, eye level, his face centred in the upper half and sharp, Fareed blurred in the background at the side, the dark table edge as a calm lower third", amb="lounge_private"),
    dict(to=27, v1="beat_009", reason="action change: Sameer opens a file on his phone and reveals the journalist Iyaan", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer leaning forward, holding up his phone towards the other two, its screen a soft blue glow with only blurred abstract shapes; Asim and Fareed leaning in from either side of the table, staring at it, faces lit by the cold blue light, tension rising",
         camera="medium shot, slightly high angle over the table, the three faces in the upper half, the table top as the lower third", amb="lounge_private",
         sens="other", safe="the phone file and the cyber-crime logs are never readable: a blurred blue glow only"),
    dict(to=28, v1="beat_010", reason="strong emotional turning point: Asim learns Iyaan is Ahmed Zahir's only son", chars=["asim"], loc="lounge",
         visual="close-up of Asim frozen in his armchair, his face draining of colour, eyes wide with shock and dawning fear, mouth slightly open, a bead of sweat on his temple, as if the floor has dropped away beneath him",
         camera="close-up, slightly low angle, his face in the upper half, his white shirt and the dark armchair below", amb="lounge_private"),
    dict(to=29, v1="beat_011", reason="memory: Asim remembers patting the young man's shoulder at Raaya's gallery and the deep look in his eyes", chars=["asim", "iyaan"], loc="gallery",
         visual="in the art gallery, Asim in his white shirt patting the young man Iyaan on the shoulder in a superior way, smiling proudly; Iyaan, wearing a dark charcoal long-sleeved button-up shirt (NOT the plain black t-shirt of the reference), standing still and looking back at him with a deep, unreadable, intense gaze; the large red-sun painting softly blurred behind them",
         camera="medium two-shot, eye level, faces in the upper half, the polished gallery floor as the lower third, a soft dreamlike vignette", amb="memory", transition="dissolve"),
    dict(to=30, reuse="beat_010", reason="back from the memory: Asim, his voice trembling, realises Iyaan used Raaya (speaker centred on the close-up)", chars=["asim"], loc="lounge",
         visual="reuse of beat_010: close-up of Asim in his armchair, shaken and afraid",
         camera="close-up, slightly low angle", amb="lounge_private", transition="dissolve"),
    dict(to=34, v1="beat_012", reason="action change, back from the memory: Sameer stands up and declares Iyaan must be eliminated", chars=["sameer", "asim", "fareed"], loc="lounge",
         visual="Sameer standing up from his armchair, buttoning his suit jacket, his face cold and decisive behind his round glasses as he speaks down to the others; Asim still seated, pale and shaken, gripping the armrests; Fareed standing at the side, nodding grimly; the three men united against a new enemy",
         camera="medium wide shot from a low angle, Sameer's face in the upper third, the bare table as the lower third", amb="lounge_private",
         sens="other", safe="the narration has him drop his cigarette: shown buttoning his jacket as he stands; nothing in his hands"),
    dict(to=38, v1="beat_013", reason="location and character change: Iyaan was listening live through Asim's phone; he puts down the headphones with a dangerous smile", chars=["iyaan"], loc="hacker_room",
         visual="Iyaan sitting at his desk in the dim room, setting a pair of black over-ear headphones down on the desk, a monitor behind him glowing with an abstract green audio waveform; no fear on his face, only a slow, dangerous half-smile and cold, steady eyes looking straight ahead",
         camera="medium close-up, eye level, his face in the upper third, the desk top with the headphones as the calm lower third", amb="hacker_room"),
    dict(to=40, v1="beat_014", reason="action change: Iyaan, two steps ahead, phones Raaya and asks her to come secretly to the studio", chars=["iyaan"], loc="hacker_room",
         visual="Iyaan standing by the window of his room, two fingers parting the blinds as he looks down at the street, a phone held to his ear, his face serious and focused, thin daylight cutting across his eyes, the glowing monitors and the investigation board with red string behind him",
         camera="medium shot, eye level, his face in the upper third, the dark floor and desk edge as the lower third", amb="hacker_room"),
    dict(to=42, v1="beat_015", reason="time jump and location change: Raaya secretly arrives at the silent third-floor studio; Iyaan waits at the window", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya stepping in through the old wooden door at the left of the studio, anxious, clutching her handbag strap, looking across the room; Iyaan standing far away at the tall window on the right, his back half turned, looking out; the paint-stained table with the open laptop stands between them in the middle of the room; " + COUPLE_GAP + ", the whole room's width apart",
         camera="wide shot, eye level, faces in the upper half, the worn wooden floor as a calm lower third", amb="room_day", transition="black"),
    # NEW (5.4) shot / reverse shot for the standing confrontation: R1 Raaya anxious, I1 Iyaan grave, R2 Raaya shocked
    dict(to=44, speaker="raaya", reason="5.4 dialogue focus: Raaya anxiously asks why he called her — in the wide entrance shot she stands at the left edge (x≈16 %)", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya standing a few steps inside the old wooden door, centred in the frame, facing the camera in three-quarter view, anxious and worried, speaking, one hand clutching the strap of her handbag, wearing her loose long-sleeved ankle-length plain white dress and a light-grey hijab wrapped snugly and fully covering her hair and neck; far behind her, small and out of focus at the tall window at the side of the room, Iyaan in his black t-shirt stands looking out; the paint-stained table with the open laptop softly blurred between them; " + COUPLE_GAP + ", the whole room apart",
         camera="medium close-up on Raaya, eye level, her face centred in the upper half and sharp, Iyaan soft and small in the background at the side, the worn wooden floor as the lower third", amb="room_day"),
    dict(to=46, speaker="iyaan", reason="5.4 dialogue focus (reverse shot): Iyaan turns from the window and tells her it was him — no v1 image centres his face", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan standing by the tall dusty window beside the paint-stained table with the open laptop, turned to face the camera, centred in the frame, his face grave and unsmiling, eyes steady and intense, speaking quietly and carefully, in his plain black t-shirt; Raaya in the soft-focus foreground at the side, seen from behind over her shoulder, only her light-grey hijab and white dress visible and blurred; " + COUPLE_GAP + ", several steps apart; the laptop screen turned away with only a faint glow",
         camera="over-the-shoulder medium close-up on Iyaan from behind Raaya, eye level, his face centred in the upper half and sharp, Raaya blurred at the edge of the frame, the table top as the lower third", amb="room_day", transition="cut"),
    dict(to=48, speaker="raaya", reason="5.4 dialogue focus (reverse shot): Raaya steps back, eyes wide — 'What kind of joke is this?'; in the v1 two-shot she is at the right edge", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya taking a step backwards, centred in the frame, facing the camera, her eyes wide with shock and disbelief, lips parted as she speaks, one hand rising to her chest, in her loose long-sleeved white dress and light-grey hijab fully covering her hair and neck; Iyaan in the soft-focus foreground at the side, seen from behind, only the back of his black t-shirt shoulder and his dark hair blurred; " + COUPLE_GAP + ", several steps apart",
         camera="over-the-shoulder medium close-up on Raaya from behind Iyaan, eye level, her face centred in the upper half and sharp, Iyaan blurred at the frame edge, the floor as the lower third", amb="room_day", transition="cut"),
    dict(to=50, reuse="beat_018", reason="shot / reverse shot: Iyaan accuses Asim", chars=["iyaan", "raaya"], loc="studio",
         visual="reuse of beat_018: Iyaan speaking, centred, Raaya blurred in the foreground", camera="over-the-shoulder medium close-up on Iyaan", amb="room_day", transition="cut"),
    dict(to=51, v1="beat_017", reason="action change: Iyaan accuses Asim; Raaya cries out that it's a lie and turns to the door; he touches the laptop", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya in the foreground turning away towards the old wooden door, tears on her cheeks, looking back over her shoulder in pain and denial; behind her at the table Iyaan, hard-faced and stern, presses one finger on the open laptop's trackpad, the screen facing away with only its glow visible; " + COUPLE_GAP + ", the table between them",
         camera="medium shot, eye level, Raaya's face in the upper third with Iyaan behind, the floor as the lower third", amb="room_day", transition="cut"),
    dict(to=52, reuse="beat_018", reason="shot / reverse shot: Iyaan, by the laptop, says 'Listen to this'", chars=["iyaan", "raaya"], loc="studio",
         visual="reuse of beat_018: Iyaan speaking beside the open laptop, centred", camera="over-the-shoulder medium close-up on Iyaan", amb="room_day", transition="cut"),
    dict(to=56, v1="beat_018", reason="action change: Asim's own voice plays from the laptop; Raaya clamps her hands over her ears", chars=["raaya"], loc="studio",
         visual="the open laptop on the paint-stained table in the foreground, its screen turned away with only a pulsing green audio-waveform glow spilling onto the table; behind it Raaya frozen in the middle of the room, both hands pressed over her ears through her hijab, eyes squeezed shut, her face crumpling as she recognises the voice",
         camera="medium shot from behind the laptop, Raaya's face in the upper third, the table top as the lower third", amb="room_day",
         sens="other", safe="the recorded order is only heard; on screen only an abstract waveform glow, no text"),
    dict(to=57, v1="beat_019", reason="action change: Raaya sinks to the floor, her world stopped", chars=["raaya"], loc="studio",
         visual="Raaya kneeling and sitting back on her heels on the wooden floor against the bare plaster wall, upright, both hands pressed over her mouth, eyes brimming with tears, staring at nothing, her white dress pooled around her; grey window light falling on her",
         camera="medium shot, slightly high angle, her face in the upper half, the empty floor before her as the lower third", amb="room_day",
         sens="other", safe="'sinks to the floor' shown as kneeling upright against the wall, hands over mouth; not lying down"),
    # NEW (5.4) shot / reverse shot for the kneeling conversation: I2 Iyaan, R3 Raaya, I3 Iyaan offering the drive
    dict(to=60, speaker="iyaan", reason="5.4 dialogue focus: Iyaan kneels before her and tells her his father died in his arms — in the v1 two-shot he is in profile at the left edge", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan kneeling on one knee on the worn wooden floor, centred in the frame, facing the camera in three-quarter view, his hands resting on his own raised knee, his face full of deep grief and old hatred, eyes glistening, speaking low, in his plain black t-shirt; in the soft-focus foreground at the side, Raaya sitting on the floor against the wall seen from behind, only her light-grey hijab and white dress blurred; " + COUPLE_GAP + ", a respectful space of floor between them",
         camera="over-the-shoulder medium close-up on Iyaan from behind Raaya, slightly low eye level, his face centred in the upper half and sharp, the floor as the lower third", amb="room_day",
         sens="intimacy", safe="no touching; a clear arm's-length gap kept between Iyaan and Raaya"),
    dict(to=61, speaker="raaya", reason="5.4 dialogue focus (reverse shot): Raaya, speechless, asks 'what should I do?'", chars=["raaya", "iyaan"], loc="studio",
         visual="Raaya sitting upright on the wooden floor with her back against the bare plaster wall, centred in the frame, looking up towards the camera in three-quarter view, tears on her cheeks, lips trembling as she speaks, both hands resting in her lap, in her loose long-sleeved white dress and light-grey hijab fully covering her hair and neck; Iyaan in the soft-focus foreground at the side, seen from behind kneeling, only his black t-shirt shoulder and dark hair blurred; " + COUPLE_GAP + ", a respectful space of floor between them",
         camera="over-the-shoulder medium close-up on Raaya from behind Iyaan, slightly high angle, her face centred in the upper half and sharp, the floor before her as the lower third", amb="room_day", transition="cut",
         sens="intimacy", safe="no touching; a clear arm's-length gap kept between Iyaan and Raaya"),
    dict(to=63, reuse="beat_025", reason="shot / reverse shot: Iyaan tells her Asim plans to eliminate him tonight and asks for her help", chars=["iyaan", "raaya"], loc="studio",
         visual="reuse of beat_025: Iyaan kneeling, speaking, centred, Raaya blurred in the foreground", camera="over-the-shoulder medium close-up on Iyaan", amb="room_day", transition="cut"),
    dict(to=65, speaker="iyaan", reason="5.4 dialogue focus + action change: Iyaan holds out a small black drive while asking for the backup drive (the narration's taking her hands is replaced); in the v1 offer shot he is in profile at the left edge", chars=["iyaan", "raaya"], loc="studio",
         visual="Iyaan, still kneeling at a respectful distance, centred in the frame and facing the camera in three-quarter view, holding out a small black metal drive on his open palm towards Raaya, his expression earnest and urgent, speaking; Raaya in the soft-focus foreground at the side, seen from behind sitting against the wall, only her light-grey hijab and white dress blurred; " + COUPLE_GAP + ", only the outstretched drive in the space between them",
         camera="over-the-shoulder medium close-up on Iyaan from behind Raaya, eye level, his face centred in the upper half and sharp, the outstretched hand with the drive at mid-frame, the floor as the lower third", amb="room_day",
         sens="intimacy", safe="the narration has him take her hands: shown instead offering a small black drive on his open palm, no touching, arm's-length gap"),
    dict(to=67, v1="beat_022", reason="emotional turning point: after a long silence Raaya decides to help and wipes her tears", chars=["raaya"], loc="studio",
         visual="close-up of Raaya wiping a tear from her cheek with the back of her hand, her chin lifting, her wet eyes now firm and resolved, the small black drive held tightly in her other hand against her chest; soft grey window light on her face",
         camera="close-up, eye level, her face in the upper half, her hand with the drive and her white dress below", amb="room_day"),
    dict(to=69, speaker="iyaan", reason="5.4 dialogue focus: Iyaan's inner vow to Asim — the v1 closing image shows him in strict profile, so a three-quarter framing centred on his face", chars=["iyaan"], loc="studio",
         visual="Iyaan standing alone by the tall dusty window of the studio, turned towards the camera in three-quarter view, centred in the frame, his face cold, calm and determined, a faint hard light in his eyes, lips closed in a silent inner vow, in his plain black t-shirt; the grey rooftops of Malé blurred through the window at his side; blank canvases in soft shadow behind him",
         camera="medium close-up, eye level, his face centred in the upper half and sharp, the window sill and the dark floor below as a calm lower third", amb="room_day"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)
T = "tight"; M = "medium"

sh(1, "The secret email Iyaan had sent reached bank MD Fareed at around nine in the morning. He was sitting at his office desk.",
   [("computer_beep", "ލިބުނީ", -20)])
sh(2, "As he opened the email, the colour of Fareed's face changed.",
   [("heartbeat", "ބަދަލުވި", -20)])
sh(3, "In it were the secret transaction receipts of the money he had sent in 2011 to the killers' account to have Member of Parliament Ahmed Zahir murdered.")
sh(4, "At the very bottom of the email was written: these secrets cannot be kept hidden forever. Get ready to pay the price.",
   hum=True)
sh(5, "Fareed immediately had the most trusted man on his IT team track where the email had come from.",
   [("keyboard_typing", "ޓްރެކް", -20)])
sh(6, "With the answer came rage of the most extreme degree. The email had been sent straight from Home Minister Asim's house.",
   [("computer_beep", "ޖަވާބާއެކު", -20)])
sh(7, "Within seconds countless questions rose and fell in his mind. \"Asim... for what purpose are you trying to blackmail me?\"",
   speaker="fareed", crop=T, focus=[40, 35])
sh(8, "Fareed said, grinding his teeth. He believed that whoever entered Asim's house last night was no political enemy, but a drama Asim had staged himself to frighten Fareed and take money from him.",
   [("breath_heavy", "ދަތްކުނޑިވިކާލަމުން", -22)], speaker="fareed", crop=T, focus=[42, 35])
sh(9, "Fareed at once picked up his phone and called Sameer, the Speaker of Parliament. \"Sameer! We have to meet right now.",
   [("phone_buzz", "ގުޅި", -22)], speaker="fareed", crop=M, focus=[42, 42])
sh(10, "Some evil political jinn has got into Asim's head. He's trying to destroy us!\" Two hours later.",
   speaker="fareed", crop=T, focus=[42, 35])
sh(11, "Inside a secret private lounge in Hulhumalé sat Sameer, Fareed and Asim. Silence hung over the room. Sameer sat smoking a cigarette.")
sh(12, "Fareed stood. Asim sat seething with anger. \"Fareed, what kind of nonsense is this you're talking?\"",
   speaker="asim", crop=M, focus=[36, 42])
sh(13, "Asim said, slamming his hand hard on the table. \"Someone got into my house last night and only just failed to open my safe!",
   [("soft_thud", "ޖަހަމުން", -16)], hum=True, speaker="asim", crop=T, focus=[36, 35])
sh(14, "For all I know every one of my secret files is gone now. Why would I send you an email?\" \"Then why does the IP address of the email that came to my office match your house's router?\"",
   speaker="asim", crop=T, focus=[36, 35])
sh(15, "Fareed threw his phone down in front of Asim. \"You're trying to pin all the blame for Zahir's murder on my head so you can save yourself politically!\"",
   [("soft_thud", "އެއްލި", -20)], speaker="fareed", crop=T, focus=[40, 35])
sh(16, "\"Stop!\" Sameer shouted. His voice carried political experience and certainty.",
   speaker="sameer", crop=T, focus=[30, 35])
sh(17, "Flicking the ash off his cigarette, he looked at the two men's faces. \"You two still don't understand anything, do you?",
   speaker="sameer", crop=T, focus=[30, 36])
sh(18, "Asim is no fool; he wouldn't send an email to blackmail Fareed in a way that's so easy to catch.",
   speaker="sameer", crop=T, focus=[30, 35])
sh(19, "And whoever got into that house last night was no ordinary thief. It was someone who got into the system and used that house's IP to send Fareed the mail.\"",
   speaker="sameer", crop=T, focus=[30, 36])
sh(20, "Asim and Fareed looked at each other. They grasped the truth in Sameer's words. \"Then... who is it?\"",
   speaker="asim", crop=T, focus=[45, 35])
sh(21, "Asim asked. This time there was a trace of fear in his voice. \"Who could know that the three of us were involved in Zahir's murder?\"",
   [("heartbeat", "ބިރުގަތުމުގެ", -22)], speaker="asim", crop=M, focus=[45, 42])
sh(22, "Sameer opened a file on his phone. \"Not a single glimpse of the man who got into Asim's house last night was caught on any camera.",
   speaker="sameer", crop=T, focus=[50, 36])
sh(23, "But when the police cyber-crime department checked the network logs this morning, they saw how the virus had been designed.",
   speaker="sameer", crop=M, focus=[50, 42])
sh(24, "That's work only a very skilled digital forensics expert could do. And besides that...\" Sameer paused.",
   speaker="sameer", crop=T, focus=[50, 36])
sh(25, "\"Besides what?\" Fareed asked hurriedly. \"Lately a young journalist has been writing our corruption stories in the papers with very detailed evidence.",
   speaker="sameer", crop=M, focus=[50, 42])
sh(26, "His name is Iyaan,\" Sameer said.",
   speaker="sameer", crop=T, focus=[50, 36])
sh(27, "\"Do you know what I found out when I checked his background this morning? He is the only son of Ahmed Zahir, whom we destroyed fifteen years ago!\"",
   hum=True, speaker="sameer", crop=T, focus=[50, 35])
sh(28, "Asim felt as if the ground had been cut away from under his feet. He remembered the young man he had seen yesterday at Raaya's art gallery.",
   [("heartbeat", "ބިންގަނޑު", -18)], hum=True)
sh(29, "The moment Asim had put his hand on his shoulder, the deep look he had seen in that young man's eyes. \"Iyaan...\"",
   speaker="asim", crop=T, focus=[30, 35])
sh(30, "Asim's voice began to tremble. \"He's out for revenge. He used Raaya to get inside my house!\"",
   [("breath", "ތުރުތުރު", -22)], speaker="asim", crop=T, focus=[45, 35])
sh(31, "\"Yes,\" said Sameer, throwing his cigarette to the floor as he stood up. \"Zahir's son has grown up and is ready to grab us by the throat.",
   [("cloth_rustle", "ތެދުވި", -22)], speaker="sameer", crop=T, focus=[53, 35])
sh(32, "He has every piece of evidence in his hands. We have no time to fight among ourselves.",
   speaker="sameer", crop=M, focus=[53, 42])
sh(33, "Iyaan's days have to be ended for good... he has to be eliminated.\"",
   hum=True, speaker="sameer", crop=T, focus=[53, 35])
sh(34, "The war among the three friends suddenly turned against Iyaan. They knew the truth now.", crop="full")
sh(35, "But every word of all this Iyaan had been listening to live, through something he had done to Asim's phone. Iyaan took off his headphones and put them on the desk.",
   [("cloth_rustle", "ބޭއްވި", -22)], crop="full")
sh(36, "No fear could be seen on his face. Instead there was a dangerous smile. \"By the time you found out my truth,",
   hum=True, speaker="iyaan", crop=T, focus=[49, 35])
sh(37, "it was far too late,\" Iyaan said softly. \"When you come to destroy me,",
   speaker="iyaan", crop=M, focus=[49, 42])
sh(38, "the way for every one of you to walk into my net is already prepared.\" With Sameer's and Fareed's warnings, Asim began the work of eliminating Iyaan.",
   speaker="iyaan", crop=T, focus=[49, 35])
sh(39, "But Iyaan was two steps ahead of them. The very first thing he did was call Raaya.",
   [("phone_buzz", "ގުޅުން", -22)])
sh(40, "His voice was serious. Iyaan asked her to come secretly to the art studio, unseen by her father's security and the police.",
   crop=T, focus=[40, 35])
sh(41, "Because of the deep trust she had in Iyaan, Raaya agreed to go there in secret from her father.")
sh(42, "When Raaya entered that studio on the third floor of an old building in a quiet Malé lane, the whole place was silent.",
   [("door_open", "ވަތްއިރު", -20)])
sh(43, "On a table in the middle of the room a laptop stood open. Iyaan stood by the window, looking outside. \"Iyaan...",
   speaker="raaya", crop=M, focus=[40, 42])
sh(44, "why did you tell me to come here? Bappa is very upset right now. There's nothing Bappa won't do to find whoever breached the house's security,\"",
   speaker="raaya", crop=T, focus=[40, 35])
sh(45, "Raaya said anxiously. Iyaan slowly turned around. The smile always seen on his face was not there today. \"Raaya...",
   speaker="iyaan", crop=M, focus=[43, 42])
sh(46, "do you know who got into your house last night?\" \"No... who?\" Raaya asked. \"It was me,\"",
   speaker="iyaan", crop=T, focus=[43, 35])
sh(47, "Iyaan said very carefully. Raaya's feet stepped backwards. Her eyes grew wide. \"What? Iyaan...",
   [("gasp", "ބޮޑުވި", -20)], hum=True, speaker="raaya", crop=M, focus=[38, 42])
sh(48, "what kind of joke is this? Why?\" \"This is no joke, Raaya.",
   speaker="raaya", crop=T, focus=[38, 35])
sh(49, "I went into your house to find the truth about my father's murder.",
   speaker="iyaan", crop=T, focus=[43, 35])
sh(50, "Your father, Home Minister Asim, may wear white clothes, but he is a killer stained with an innocent man's blood,\" Iyaan said, his voice hard and angry.",
   speaker="iyaan", crop=M, focus=[43, 42])
sh(51, "\"No! That's a lie! My father would never do such a thing!\" Raaya cried out. Tears rolled from her eyes.",
   [("sob_breath", "ކަރުނަ", -22)], speaker="raaya", crop=T, focus=[30, 35])
sh(52, "She turned towards the door to leave. \"Listen to this,\" Iyaan said, tapping the laptop's screen.",
   [("computer_beep", "ފިތާލި", -20)], speaker="iyaan", crop=T, focus=[43, 35])
sh(53, "At once the audio file Iyaan had taken from Asim's own safe echoed through the studio. Asim's heavy, merciless voice was heard.")
sh(54, "\"Zahir has started talking far too much... shut his mouth for good.",
   hum=True)
sh(55, "Make tonight the last night he spends in this world...\"",
   hum=True)
sh(56, "Raaya's hands went to her ears. She knew her father's voice all too clearly. It was, beyond any doubt, Asim's own voice.",
   [("gasp", "ޖެހުނު", -22)])
sh(57, "Raaya sank to the floor. It was as if her world had stopped. Having to accept that her loving, caring father was a merciless political killer who had ordered a man's death broke her heart.",
   [("soft_thud", "ތިރިވި", -24)], hum=True)
sh(58, "Iyaan went and knelt in front of Raaya. \"That murdered Ahmed Zahir was my father. When I was eight years old",
   [("cloth_rustle", "ޖެހި", -22)], hum=True, speaker="iyaan", crop=M, focus=[40, 42])
sh(59, "my father died in my arms. Merciless men killed my father on your father's order.",
   speaker="iyaan", crop=T, focus=[40, 35])
sh(60, "For the past fifteen years the only purpose I have lived for is finding this truth.\" Raaya looked at Iyaan's face.",
   speaker="iyaan", crop=M, focus=[40, 42])
sh(61, "Seeing the deep grief and hatred in Iyaan's eyes, no word left Raaya's lips. \"Iyaan... I... what should I do?\"",
   speaker="raaya", crop=T, focus=[41, 35])
sh(62, "Raaya asked, sobbing. \"Asim is planning to eliminate me tonight together with Sameer and Fareed.",
   [("sob_breath", "ގިސްލަމުން", -22)], speaker="iyaan", crop=T, focus=[40, 35])
sh(63, "They think that if I'm killed, all the evidence will disappear. What I need is your help, Raaya.",
   speaker="iyaan", crop=M, focus=[40, 42])
sh(64, "Asim can only be defeated from inside his house,\" Iyaan said, taking both of Raaya's hands. \"What I need is to get, before Asim's next big political rally, the second backup drive that holds his data.",
   speaker="iyaan", crop=M, focus=[40, 42])
sh(65, "Only you can do that.\" Raaya sat in silence for a while. Standing up against her father was no easy thing.",
   speaker="iyaan", crop=T, focus=[40, 35])
sh(66, "But for the sake of justice, and for the great sin her father had committed, she decided to help Iyaan. \"I'll do it,\"",
   speaker="raaya", crop=T, focus=[39, 35])
sh(67, "Raaya said, wiping away her tears. \"I'll help expose my father's crimes to the whole nation.\"",
   [("breath", "ފޮހެލަމުން", -24)], hum=True, speaker="raaya", crop=M, focus=[39, 42])
sh(68, "Iyaan said to himself: Asim... you took my father from me. Today your own child stands against you.",
   speaker="iyaan", crop=M, focus=[52, 42])
sh(69, "Your end will be no less heartbreaking than this. To be continued.",
   hum=True, speaker="iyaan", crop=T, focus=[52, 35])
SHOTS = S

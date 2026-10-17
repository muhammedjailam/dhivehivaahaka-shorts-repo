"""Beat/shot plan for Karuna episode 335 (series opener; used by plan_beats.py).
v2 re-cut on the re-recorded audio (66 segments): same 31 beats and v1 images (v1=), re-timed shots."""

LOC = {
    "living_day": "the living room of Qasim's wealthy modern multi-storey house in Male: polished cream marble-look floor, a wide curving staircase with a dark wooden handrail in the background, a large soft beige sofa, tall windows with sheer curtains, a low glass table with a vase of white flowers",
    "house_dusk": "the outside of Qasim's wealthy modern multi-storey house in a narrow Male lane: pale walls, tall windows, a heavy dark front gate, neighbouring pastel buildings, parked motorbikes along the lane",
    "college_corridor": "a bright open-air corridor of a college in Male: a long row of pillars, pale walls, a few students far away softly blurred, a green tree in a courtyard",
    "library": "a college library: tall wooden bookshelves with plain unlabelled book spines, long reading tables with a few closed books, big windows letting in daylight",
    "shima_room_night": "Shima's bedroom in the wealthy house at night: a bed with a pale quilt, a dressing table with a mirror at the right, a window with a sheer curtain at the left, a single warm bedside lamp",
    "cafe": "a quiet small cafe in Male: a small round wooden table by a big window, two cups of tea on the table, a blurred lane outside",
    "gate_lane_night": "the narrow Male lane outside Qasim's house late at night: the heavy dark front gate slightly ajar, tall pastel buildings, parked motorbikes, sodium street lights on the asphalt, the house dark",
    "apartment_corridor": "a dim, narrow corridor of an old apartment building in Male late at night: bare walls, a flickering ceiling light, a row of plain closed wooden doors without numbers",
    "rain_window": "a rain-streaked window high up in Male at night, looking out over the dark city skyline of tall buildings with a few lit windows",
    "shima_room_day": "Shima's bedroom in the wealthy house by day: a bed with a pale quilt, a dressing table with a mirror at the right, a window with a sheer curtain at the left, the attached bathroom door closed",
    "pharmacy": "a small pharmacy in a far-off Male lane: a plain counter, shelves of plain white boxes with no labels, fluorescent light",
    "dusk_shore": "a lonely deserted spot at the edge of Male by the sea: an empty stretch of reclaimed sandy ground and a low concrete sea wall, the open sea beyond, nobody around",
    "storm_house": "Qasim's wealthy house and the narrow Male lane in a violent storm at night: heavy rain, flooded asphalt, the dark house with one dim window",
    "shima_room_storm": "Shima's bedroom in the wealthy house on a stormy night: a bed with a pale quilt, a dressing table with a mirror at the right, a window with a sheer curtain at the left with rain streaming down the glass, the bedroom door to the hallway",
}
MOOD = {
    "living_day": "bright soft daylight through tall windows, warm marble interior, comfortable and wealthy, a quiet undertone of strictness",
    "house_dusk": "bruised dusk, dark heavy storm clouds gathering over the city, a cold wind, ominous foreboding",
    "college_corridor": "bright airy daylight, fresh and youthful",
    "library": "bright airy daylight, calm and hushed, a shy warmth",
    "shima_room_night": "night, a warm bedside lamp and the cold glow of a phone on her face, intimate and secretive",
    "cafe": "soft warm late-afternoon light, cosy and hopeful",
    "gate_lane_night": "late night, orange sodium street lights, deep blue shadows, secretive and tense",
    "apartment_corridor": "late night, dim and cold, a weak yellow ceiling light, heavy silence, foreboding",
    "rain_window": "late night, near-black blue, silver rain streaks, distant blurred city lights, sorrowful",
    "shima_room_day": "pale morning daylight filtered through the sheer curtain, cold and anxious",
    "pharmacy": "flat cold fluorescent daylight, furtive and anxious",
    "dusk_shore": "bruised violet-orange dusk, the sun gone, a cold wind off the sea, desolate",
    "storm_house": "near-black blue storm night, silver sheets of rain, white lightning, menacing",
    "shima_room_storm": "near-black blue storm night inside the room, a dim warm lamp, the cold glow of a phone, white lightning flashes through the window, dread",
}

H_S = "her cream hijab fully covering her hair and neck"
H_N = "her dark navy hijab fully covering her hair and neck"
ROOM = "her bed with a pale quilt, the dressing table with a mirror at the right, the window with a sheer curtain at the left"

BEATS = [
    # 1 -- new seg 1-4
    dict(to=4, v1="beat_001", reason="episode opening: Shima, the adored only daughter, and her proud, strict wealthy father Qasim at home", chars=["shima", "qasim"], loc="living_day",
         visual=f"Shima in her loose dusty-lavender long dress with {H_S} sitting on a large beige sofa in the bright marble living room, smiling softly; her father Qasim in his crisp white shirt stands behind the sofa a little to the side, upright and proud, hands behind his back, a stern dignified face with a faint protective pride as he looks at her; the wide staircase and tall sheer-curtained windows behind",
         camera="medium wide, eye level, faces in the upper two-thirds, the polished marble floor as the lower third",
         amb="mansion_day"),
    # 2 -- new seg 5-7
    dict(to=7, v1="beat_002", reason="character change: grown-up Shima's bright smile, and her gentle mother Naseema introduced", chars=["shima", "naseema"], loc="living_day",
         visual=f"Shima with {H_S} laughing radiantly while arranging white flowers in a vase on the low table; her mother Naseema in her grey-patterned dark dress with {H_N} standing beside her, watching her daughter with a soft loving smile, a hand on Shima's shoulder; sunlight through the sheer curtains",
         camera="medium shot, eye level, both faces in the upper two-thirds, the table top and flowers as the lower third",
         amb="mansion_day"),
    # 3 -- new seg 8-9
    dict(to=9, v1="beat_003", reason="emotional turning point: the narrator foreshadows a great storm over the family", loc="house_dusk",
         visual="the wealthy multi-storey house seen from the narrow lane at dusk, one warm lit upper window, while enormous dark storm clouds roll in over the Male skyline behind it; the heavy dark front gate closed; nobody in the lane; no signs, no lettering",
         camera="wide establishing shot, low angle from the lane, the house and the storm clouds in the upper two-thirds, the empty lane as the lower third",
         amb="mansion_night", sens="other", safe="foreshadowing shown as gathering storm clouds over the house"),
    # 4 -- new seg 10-11
    dict(to=11, v1="beat_004", reason="scene and character change: at college, charming Yazan is introduced", chars=["yazan"], loc="college_corridor",
         visual="Yazan in his open light-grey overshirt over a white t-shirt, swept-back hair, leaning casually against a pillar in the bright college corridor, a confident light smile on his lips and a deep dark gaze towards the camera; a few students far away and softly blurred",
         camera="medium close-up, eye level, his face in the upper half, the pale corridor floor as the lower third",
         amb="classroom"),
    # 5 -- new seg 12-14
    dict(to=14, v1="beat_005", reason="scene change: first meeting of eyes in the college library; Yazan starts talking to her", chars=["shima", "yazan"], loc="library",
         visual=f"in the bright library Shima with {H_S} sits at a long reading table with a closed book, looking up shyly with a small surprised smile; Yazan stands across the table on the far side, a full arm's length and more away beside a tall bookshelf, speaking to her with a charming smile; the two clearly apart, not touching; plain unlabelled books",
         camera="medium wide, eye level, both faces in the upper two-thirds, the reading table top as the lower third",
         amb="library_day", sens="intimacy", safe="the growing attraction shown only as glances and talking across a library table at a respectful distance"),
    # 6 -- new seg 15-16
    dict(to=16, v1="beat_006", reason="time/scene change: long secret phone calls at night in her bedroom", chars=["shima"], loc="shima_room_night",
         visual=f"Shima alone at night sitting cross-legged on her bed against the headboard, fully dressed in her lavender long dress with {H_S}, holding a phone to her ear and smiling dreamily, her eyes shining; the warm bedside lamp beside her; {ROOM}; the phone screen not visible",
         camera="medium shot, eye level, her face in the upper half, the pale quilt as the lower third",
         amb="room_night"),
    # 7 -- new seg 17-18
    dict(to=18, v1="beat_007", reason="scene change: a secret meeting where Yazan makes sweet promises of marriage", chars=["yazan", "shima"], loc="cafe",
         visual=f"Yazan and Shima sitting opposite each other across a small round wooden table in a quiet cafe, a full arm's length apart, two cups of tea between them; Yazan leaning back slightly, one hand on his chest, speaking earnestly with a persuasive smile; Shima with {H_S} listening, entranced and trusting, her hands around her cup; warm window light",
         camera="medium two-shot from the side, eye level, faces in the upper two-thirds, the table top and cups as the lower third",
         amb="cafe", sens="intimacy", safe="romance shown only as two people talking across a table at a respectful distance, never touching"),
    # 8 -- new seg 19-20
    dict(to=20, v1="beat_008", reason="time and scene change: late at night, Qasim away and Naseema asleep, Shima slips out of the house", chars=["shima"], loc="gate_lane_night",
         visual=f"Shima in her lavender long dress with {H_S} seen from behind and to the side, slipping out through the narrow gap of the heavy dark front gate into the empty lane, glancing back nervously over her shoulder at the dark sleeping house where every window is unlit; orange street light, deep shadows",
         camera="medium wide, eye level, her figure and the gate in the upper two-thirds, the dark wet asphalt as the lower third",
         amb="street_night", sens="intimacy", safe="the secret night meeting is shown only as her leaving the dark house alone"),
    # 9 -- new seg 21-22
    dict(to=22, v1="beat_009", reason="scene change: the empty apartment -- shown only as a closed door in a dim corridor (night of the sin never depicted)", loc="apartment_corridor",
         visual="a dim narrow apartment corridor late at night, completely empty, one plain wooden door at the end firmly closed, a thin line of weak light under it, a flickering ceiling light, long shadows; no people at all, no numbers or signs",
         camera="medium wide, eye level down the corridor, the closed door in the upper-middle, the bare floor as the lower third",
         amb="apartment_quiet_night", sens="intimacy", safe="what happens inside is never shown: only an empty corridor and a closed door"),
    # 10 -- new seg 23-24
    dict(to=24, v1="beat_010", reason="symbolic substitution: rain on a night window over the city while the narration speaks of the sin", loc="rain_window",
         visual="a close view of a dark window pane streaked with silver rain drops at night, beyond it the blurred dark city skyline with a few lit windows; no people, no reflections of people, nothing inside the room visible",
         camera="close-up, eye level, rain streaks and skyline filling the frame, dark sill as the lower third",
         amb="apartment_rain_night", sens="intimacy", safe="the night of the sin is shown only as rain on a dark window (bible rule 3)"),
    # 11 -- new seg 25-26
    dict(to=26, v1="beat_011", reason="scene change: back home alone in her room, she sobs in shame", chars=["shima"], loc="shima_room_night",
         visual=f"Shima alone in her dim bedroom at night, fully dressed in her lavender long dress with {H_S}, sitting on the edge of her bed with her face buried in her hands, shoulders shaking, crying; the bedside lamp low; {ROOM}",
         camera="medium shot, slightly high angle, her bowed head in the upper half, the pale quilt and floor as the lower third",
         amb="room_night", sens="intimacy", safe="aftermath shown only as Shima alone, fully dressed, crying on the edge of her bed"),
    # 12 -- new seg 27-28
    dict(to=28, v1="beat_012", reason="action change: Yazan's messages calm her; she hides the sin from herself and her father", chars=["shima"], loc="shima_room_night",
         visual=f"close-up of Shima lying on her side on top of the quilt, fully dressed with {H_S}, her face lit by the cold glow of a phone held near her face, tear tracks on her cheeks but a fragile relieved look returning to her eyes; the screen faces away and is not visible; warm lamp in the soft background",
         camera="close-up, eye level, her face in the upper half, the pale quilt as the lower third",
         amb="room_night"),
    # 13 -- new seg 29-31
    dict(to=31, v1="beat_013", reason="time jump: months pass; morning nausea and changes in her health", chars=["shima"], loc="shima_room_day",
         visual=f"Shima in her lavender long dress with {H_S} standing by the sheer-curtained window of her bedroom in pale morning light, one hand pressed over her mouth, the other on the window frame, pale and dizzy, eyes worried; an untouched breakfast tray on the dressing table",
         camera="medium shot, eye level, her face in the upper half, the floor tiles as the lower third",
         amb="room_day", transition="black"),
    # 14 -- new seg 32
    dict(to=32, v1="beat_014", reason="scene change: she secretly buys a pregnancy test at a far-away pharmacy, her face covered", chars=["shima"], loc="pharmacy",
         visual=f"Shima with {H_S}, the end of the hijab drawn across her lower face so only her anxious eyes show, standing at a plain pharmacy counter and quickly taking a small plain white box with no writing; she glances sideways nervously; shelves of unlabelled white boxes behind; no pharmacist face in focus",
         camera="medium close-up, eye level, her eyes in the upper half, the counter top as the lower third",
         amb="shop_day", sens="other", safe="the test bought at a pharmacy with blank packaging; the bathroom is never shown"),
    # 15 -- new seg 33-34
    dict(to=34, v1="beat_015", reason="action change: the test -- her trembling hands holding a small white stick in her bedroom", chars=["shima"], loc="shima_room_day",
         visual=f"close-up of Shima's trembling hands holding a small plain white plastic stick, sitting on the edge of her bed in her lavender long sleeves; the stick has no writing, only two faint blurred lines; behind, softly out of focus, her frightened face with eyes squeezed shut and {H_S}; the attached bathroom door closed in the far background",
         camera="close-up on the hands in the middle, her blurred face in the upper part, the pale quilt as the lower third",
         amb="room_day", sens="other", safe="the test shown only as hands and a small plain stick in her bedroom, never a bathroom interior (bible rule 4)"),
    # 16 -- new seg 35-37
    dict(to=37, v1="beat_016", reason="action change: the test falls to the floor; she sobs, clamping a hand over her mouth", chars=["shima"], loc="shima_room_day",
         visual=f"Shima sitting on the bedroom floor with her back against the side of the bed, in her lavender long dress with {H_S}, one hand clamped over her mouth, eyes wide and streaming with tears, shocked and dizzy; a small plain white stick lying on the floor tiles in front of her",
         camera="medium shot, slightly high angle, her face in the upper half, the floor tiles and the little white stick as the lower third",
         amb="room_day", sens="other", safe="her despair is shown only by her face and posture"),
    # 17 -- new seg 38-40
    dict(to=40, v1="beat_017", reason="action change: terror of her father and dark thoughts; she calls Yazan in tears", chars=["shima"], loc="shima_room_day",
         visual=f"Shima crouched in the corner of her bedroom beside the window, knees drawn up, fully dressed with {H_S}, pressing a phone to her ear with a trembling hand and sobbing, her other hand gripping her knees; the sheer curtain half drawn, the room gone dim and grey; the phone screen not visible",
         camera="medium close-up, eye level, her face in the upper half, the floor as the lower third",
         amb="room_day", sens="other", safe="her thoughts of death are shown only as terror and tears, nothing else"),
    # 18 -- new seg 41
    dict(to=41, v1="beat_018", reason="scene change: dusk, a lonely place by the sea; Yazan is taken aback by her swollen eyes", chars=["shima", "yazan"], loc="dusk_shore",
         visual=f"a wide view at dusk of a desolate stretch of sand by a low sea wall; Shima with {H_S} stands on the left facing Yazan, who stands on the right in his light-grey overshirt, with a clear gap of about two metres of empty ground between them; Yazan's brow furrowed in surprise; her eyes red and swollen; violet-orange sky over the sea",
         camera="wide two-shot in profile, eye level, the figures and sky in the upper two-thirds, the empty sand as the lower third",
         amb="beach_dusk", sens="intimacy", safe="the two always stand clearly apart, never touching"),
    # 19 -- new seg 42 (shot: Shima)
    dict(to=42, v1="beat_019", reason="dialogue: Shima, trembling, tells him she is pregnant (shot, speaker focus)", chars=["shima", "yazan"], loc="dusk_shore",
         speaker="shima", transition="cut",
         visual=f"Shima facing the camera at dusk with {H_S}, speaking in a trembling voice, her red tearful eyes pleading, hands clasped at her chest; in the far soft-focus foreground at the side, the blurred shoulder of Yazan seen from behind, a clear gap between them; violet-orange sky behind her",
         camera="medium close-up over Yazan's distant shoulder, Shima centred and sharp in the upper half, the dusky ground as the lower third",
         amb="beach_dusk"),
    # 20 -- new seg 43-44 (reverse shot: Yazan)
    dict(to=44, v1="beat_020", reason="dialogue: Yazan's face turns cold and contemptuous; he denies the child (reverse shot, speaker focus)", chars=["yazan", "shima"], loc="dusk_shore",
         speaker="yazan", transition="cut",
         visual="Yazan facing the camera at dusk in his light-grey overshirt, his handsome face now hard and cold, lip curled in disgust and anger, eyes narrowed, speaking harshly; in the far soft-focus foreground at the side the blurred back of Shima's cream hijab, a clear gap of empty air between them; the darkening sea behind him",
         camera="medium close-up over Shima's distant shoulder, Yazan centred and sharp in the upper half, the dusky ground as the lower third",
         amb="beach_dusk"),
    # 21 -- new seg 45-47 (reuse Shima)
    dict(to=47, reason="return to Shima pleading that she has never been with anyone else (shot / reverse-shot)", loc="dusk_shore",
         reuse="beat_019", chars=["shima", "yazan"], speaker="shima", transition="cut", amb="beach_dusk", visual="(reuse of beat_019)",
         sens="intimacy", safe="'she tried to take his hand' is not shown; the two remain apart"),
    # 22 -- new seg 48-51 (reuse Yazan)
    dict(to=51, reason="return to Yazan coldly telling her to solve it herself (shot / reverse-shot)", loc="dusk_shore",
         reuse="beat_020", chars=["yazan", "shima"], speaker="yazan", transition="cut", amb="beach_dusk", visual="(reuse of beat_020)",
         sens="other", safe="'shook off her hand' is not shown (they never touch); 'abortion' is only spoken (bible rule 5)"),
    # 23 -- new seg 52
    dict(to=52, v1="beat_023", reason="action change: Yazan turns and walks away while Shima kneels on the ground pleading", chars=["shima", "yazan"], loc="dusk_shore",
         visual=f"Shima kneeling on the sand in the foreground with {H_S}, her hands clasped and raised, crying and pleading; far away in the background, many metres off, Yazan in his light-grey overshirt walking away with his back turned, already small, never looking back; a huge empty gap of sand between them; the last violet light over the sea",
         camera="wide, low angle from behind Shima's shoulder, her face in three-quarter view in the upper half, Yazan small in the distance, the sand as the lower third",
         amb="beach_dusk", sens="intimacy", safe="'fell at his feet' becomes kneeling on the sand while he is already far away walking off"),
    # 24 -- new seg 53-55
    dict(to=55, v1="beat_024", reason="time change: Yazan vanishes; Shima hides in her room, frozen with fear, life gone from her face", chars=["shima"], loc="shima_room_night",
         visual=f"Shima sitting on the floor of her dim bedroom with her back against the closed bedroom door, hugging her knees, fully dressed in her lavender long dress with {H_S}, her face pale and lifeless, staring at nothing; a dark phone lying on the floor beside her; the lamp barely lit; {ROOM}",
         camera="medium shot, eye level, her face in the upper half, the floor as the lower third",
         amb="room_night"),
    # 25 -- new seg 56
    dict(to=56, v1="beat_025", reason="character change: Qasim notices the change and urges her to see a doctor; she makes excuses", chars=["qasim", "shima"], loc="shima_room_day",
         visual=f"Qasim in his crisp white shirt standing in the open bedroom doorway, frowning with stern fatherly concern, one hand on the door frame, speaking; Shima with {H_S} sitting on the far side of her bed, half turned away from him, pulling the pale quilt over her lap, eyes lowered, making an excuse; daylight through the sheer curtain",
         camera="medium wide, eye level, Qasim's face and Shima's face in the upper two-thirds, the floor as the lower third",
         amb="mansion_day"),
    # 26 -- new seg 57-58
    dict(to=58, v1="beat_026", reason="time and scene change: a terrifying storm night over Male, thunder and lightning", loc="storm_house",
         visual="the wealthy house and the narrow Male lane in a violent storm at night: sheets of silver rain, a white lightning bolt splitting the black sky, the flooded asphalt reflecting the flash, one dim upper window lit; no people; no lettering",
         camera="wide establishing shot, low angle, the house and lightning in the upper two-thirds, the flooded lane as the lower third",
         amb="storm_night"),
    # 27 -- new seg 59-60
    dict(to=60, v1="beat_027", reason="scene change: in her storm-lit room she weeps over hundreds of unanswered messages", chars=["shima"], loc="shima_room_storm",
         visual=f"Shima curled on top of her bed in her lavender long dress with {H_S}, crying, her face lit by the cold glow of the phone in her hands, the screen turned away and not visible; rain streaming down the window at the left, a white lightning flash lighting the room; the bedroom door at the back closed",
         camera="medium shot, eye level, her face in the upper half, the pale quilt as the lower third",
         amb="storm_night", sens="other", safe="phone shown only as a glow on her face, no readable screen"),
    # 28 -- new seg 61-63
    dict(to=63, v1="beat_028", reason="character/action change: Qasim bursts in, takes the phone and reads the messages", chars=["qasim", "shima"], loc="shima_room_storm",
         visual=f"Qasim in his white shirt standing in the middle of the dark storm-lit bedroom holding Shima's phone, its cold glow lighting his stern face from below as he reads, his expression darkening in disbelief; the screen faces away from the camera and is not visible; behind him on the bed, frozen in terror, Shima with {H_S} with both hands pressed to her mouth; lightning in the window",
         camera="medium shot, eye level, Qasim's face centred in the upper half, Shima softer behind, the floor as the lower third",
         amb="storm_night", sens="violence", safe="'snatched the phone from her hand' is not shown: the phone is already in his hand, no contact"),
    # 29 -- new seg 64
    dict(to=64, v1="beat_029", reason="object detail: the pregnancy test kit lying on the dressing table catches Qasim's eye", loc="shima_room_storm",
         visual="a close view of the dressing table top in the dark storm-lit bedroom: among a hairbrush and small bottles lies a small plain white plastic stick with no writing; the mirror above reflects only a dark blur and a flash of lightning; cold white light falling across the table",
         camera="close-up on the table top, the small white stick in the middle, the mirror in the upper part, the polished wood as the lower third",
         amb="storm_night", sens="other", safe="the test kit shown only as a small plain white object"),
    # 30 -- new seg 65
    dict(to=65, v1="beat_030", reason="emotional turning point: Qasim's face red with rage, his whole body trembling", chars=["qasim"], loc="shima_room_storm",
         visual="close-up of Qasim's face in the dark storm-lit room, his eyes wide and blazing, his face flushed red with fury, jaw clenched, the salt-and-pepper moustache trembling, the phone gripped in his shaking hand raised near his chest, its screen turned away; a white lightning flash behind him",
         camera="close-up, slightly low angle, his face in the upper half, his shirt and shaking hand as the lower third",
         amb="storm_night"),
    # 31 -- new seg 66
    dict(to=66, v1="beat_031", reason="action change: he smashes the phone on the floor (episode ending)", chars=["qasim"], loc="shima_room_storm",
         visual="the phone shattered on the polished floor tiles of the dark bedroom, its dark cracked screen with no image, small shards of glass scattered across the tiles, lit by a cold white flash of lightning; at the top of the frame only Qasim's dark trouser legs and his empty trembling hand hanging at his side",
         camera="low angle close to the floor, the shattered phone in the middle, Qasim's legs and hand in the upper part, the tiles as the lower third",
         amb="storm_night", sens="violence", safe="his rage is shown only as the smashed phone on the tiles and his shaking hand"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

# v2 re-cut: one sh() per NEW segment (66), English re-checked against the new Dhivehi
sh(1, "To say that Shima's life was a dream world would be no lie. Belonging to a wealthy upper-class family of Male, Shima is her parents' one and only child.")
sh(2, "Above all, she is the most precious jewel bound to the very soul of her father, Qasim. Qasim is a man greatly respected in society, but very rigid in temperament and stubborn about his principles.")
sh(3, "His name and honour among people are what he is proudest of. Shima grew up under that father's firm, and at times stifling, strict upbringing.")
sh(4, "Even so, she was never denied anything. Whatever she needed, whatever she wished for, was fulfilled at once.")
sh(5, "By the time she turned twenty, Shima was a girl the whole family singled out as a model of beauty and good character.")
sh(6, "Her wide smile brought life to the whole house. Shima's mother, Naseema, is a gentle, soft-spoken woman.")
sh(7, "Her whole world was Shima's happiness, and within the four walls of that house there was perfect peace and safety.")
sh(8, "But behind that perfect happiness, no one caught the scent of a great storm that would shake the foundations of the whole family.",
   [("wind_gust", "ތޫފާނެއްގެ", -22)], hum=True)
sh(9, "Shima's innocence and her ignorance of the world -- she did not sense then that these were the greatest danger she would face.")
sh(10, "The great change in Shima's safe life came when she met Yazan at college. Yazan is a handsome twenty-two-year-old young man, extraordinarily gifted at talking.")
sh(11, "The depth in his eyes and the light smile on his lips were a magic that could melt any girl's heart.")
sh(12, "From the first day their eyes met in the college library, a new rhythm began to beat in Shima's heart.",
   [("page_turn", "ލައިބްރަރީން", -22)])
sh(13, "Yazan himself took the lead and began talking to Shima. His sweet words and his looks full of love reached the deepest corner of Shima's heart.")
sh(14, "For Shima, who had never before been so close to any boy, Yazan's attention became something that changed her whole world.")
sh(15, "Talking on the phone for hours every day, and meeting secretly, hidden from the family, became a habit.",
   [("phone_buzz", "ފޯނުން", -22)])
sh(16, "What Shima came to feel for Yazan was an extraordinary, foolish love. She came to believe he was a part of her very soul.")
sh(17, "Caught up in the intoxication of love, things went so far that Shima could no longer tell right from wrong. Yazan made countless sweet promises that he would spend his whole life with her and marry her as soon as their studies were over.")
sh(18, "Shima believed every one of those words without any doubt or fear. Caught in that deceitful air, Shima made the greatest mistake she could ever make in her life.",
   hum=True)
sh(19, "That night Qasim was away from Male on a business trip. Her mother, with a headache, had gone to sleep very early.",
   [("clock_tick", "ނިދާފަ", -24)])
sh(20, "A deep silence had settled over the house. At Yazan's request, Shima slipped secretly out of the house and went to meet him at an empty apartment belonging to a friend of Yazan's.",
   [("metal_gate", "ނުކުމެގެން", -22), ("footsteps_pavement", "ދިޔައީ", -22)])
sh(21, "The moment she went in there, Shima's heart began to pound with fear. \"If you love me, won't you trust me?\"",
   [("door_close", "ވަދެވުމާއެކު", -22), ("heartbeat", "ތެޅެން", -22)])
sh(22, "Before Yazan's words full of love, and the pleading he made as he said it, Shima lost all control over herself.")
sh(23, "Caught in the whispers of Satan, she stepped beyond every boundary set by Islam and by society.",
   [("rain_start", "ވަސްވާސްތަކުގައި", -22)], hum=True)
sh(24, "That night she surrendered her most precious chastity to Yazan. She realised she had done wrong only after the moment had passed.",
   hum=True)
sh(25, "As she felt the enormity of the betrayal she had committed against herself, Shima began to cry. Coming home, she went into her room, threw herself onto the bed and sobbed.",
   [("sob_breath", "ރޮވެން", -22), ("door_close", "ވަދެ", -22), ("sob_breath", "ގިސްލަގިސްލާފައި", -20)], hum=True)
sh(26, "Her heart was pounding with a fear beyond words. The guilt of having lost her purity made her breath ragged.")
sh(27, "But that night the messages Yazan sent calmed her. As he kept repeating his assurance that he would marry her, Shima hid that great sin, deceived herself and set her heart at rest.",
   [("phone_buzz", "މެސެޖުތަކުން", -22)])
sh(28, "She was ashamed even to look at Qasim's face. But in the blindness of love she tried to forget it.")
sh(29, "Months passed. Unusual changes began to come over Shima's body and her health.")
sh(30, "She turned away from food, and on waking in the morning she felt dizzy and sick. Her usual daily routine changed.",
   [("breath_heavy", "ހޮޑުލެވޭގޮތް", -22)])
sh(31, "At first she thought it was an ordinary illness or tiredness. But as the days went by, the frightening suspicions in her heart began to turn into certainty.")
sh(32, "Her monthly period had stopped too. One day, covering her face, secretly so that no one would know, she went to a pharmacy far away, bought a pregnancy test, came back, went into the bathroom of her room and locked the door.",
   [("lock_click", "ތަޅުލި", -20)])
sh(33, "After testing with trembling hands, she spent those three minutes like someone standing on the very lips of death.",
   [("clock_tick", "މިނެޓު", -22)], hum=True)
sh(34, "Eyes shut, she slowly opened them and looked at the test kit. The moment she saw the two red lines that had appeared, Shima felt as if the ground had given way beneath her feet.",
   [("heartbeat", "ރޮނގު", -18)], hum=True)
sh(35, "The test kit in her hand fell to the floor. She burst into loud sobs, and quickly clamped her hand over her mouth to keep the sound from getting out.",
   [("soft_thud", "ވެއްޓުނު", -22), ("sob_breath", "ރޮއިގަނެވުނު", -20)], hum=True)
sh(36, "The whole world spun and she grew dizzy. With the enormity of the sin she had committed and its consequence there before her, she could hardly breathe.",
   [("breath_heavy", "ނޭވާ", -22)], hum=True)
sh(37, "Knowing that a child of sin was forming in her womb, her mind went blank. \"This can't happen... This is a dream...")
sh(38, "I might die...\" Her heart kept pounding with fear. When she thought of what would happen if her father found out, her whole body went cold with dread.",
   [("heartbeat", "ތެޅެމުންދިޔަ", -20)], hum=True)
sh(39, "Her conscience began to cry out that there was no way out but death. Shima's only hope, her only refuge, was Yazan.",
   hum=True)
sh(40, "With trembling hands she called Yazan at once and, crying and pleading, begged him to meet her. At dusk, the two met in a lonely place with few people about.",
   [("phone_buzz", "ގުޅައި", -22), ("sob_breath", "ރޮމުން", -22), ("wind_gust", "ހަވީރުގެ", -24)])
sh(41, "Seeing the distress on Shima's face and her eyes swollen from crying, Yazan was taken aback.")
sh(42, "Gathering all her courage, Shima told him in a trembling voice that she was pregnant -- and the colour of Yazan's face changed completely.",
   speaker="shima")
sh(43, "In place of that loving look appeared the colours of disgust, anger and contempt. \"What? Pregnant?",
   speaker="yazan")
sh(44, "How am I supposed to know that's my child?\" Those harsh words from Yazan's mouth pierced Shima's heart like hundreds of sharp daggers.",
   speaker="yazan", hum=True)
sh(45, "\"Yazan! Don't say that. I have never had anything to do with anyone but you, Yazan.",
   speaker="shima")
sh(46, "Didn't you say we would always be together? That you would marry me? Now we have no choice but to marry...",
   speaker="shima")
sh(47, "If my father finds out, he'll kill me!\" Crying and pleading, Shima tried to take hold of Yazan's hand.",
   [("sob_breath", "ރޮމުން", -22)], speaker="shima")
sh(48, "But Yazan shook that hand off roughly. \"I'm still a student. My family will never accept this.",
   [("cloth_rustle", "ފޮޅާލި", -22)], speaker="yazan")
sh(49, "And I'm not ready to raise children. Find your own way out of this, Shima.",
   speaker="yazan")
sh(50, "Whether you get an abortion or pin it on someone else -- that's your own business, Shima.",
   speaker="yazan")
sh(51, "Don't come after me from now on!\" Yazan left her, turned and walked away.",
   [("footsteps_sand", "ހިނގައިގަތް", -20)], speaker="yazan")
sh(52, "Shima fell at his feet and begged him again and again. But Yazan never once looked back. After that day Yazan switched off his phone.",
   [("sob_breath", "ވެއްޓި", -20)], hum=True)
sh(53, "Shima could find out neither where he lived nor where he went. Her lover, after robbing her of her chastity, abandoned her at her most helpless moment and fled.",
   hum=True)
sh(54, "Shima's life turned into a terrifying hell without any freedom. Inside the house she went about frozen with fear.")
sh(55, "She did not even dare go out to the dining room. All the joy and life had vanished from her face. Qasim noticed these unusual changes in his daughter.")
sh(56, "Thinking she was ill, Qasim asked her many times to let him take her to a doctor. But Shima made excuses and escaped by staying in her room.")
sh(57, "Even so, the truth is not something that can be hidden. It is a great secret that will burst open one day. It was a frightening night, with heavy rain pouring down on Male.",
   [("rain_start", "ވާރޭވެހެމުންދިޔަ", -18)])
sh(58, "The rumble of thunder across the sky made all of Male shudder. Flashes of lightning lit up the room.",
   [("thunder", "ގުގުރަމުން", -14), ("thunder", "ވިދުވަރުގެ", -18)])
sh(59, "As Shima lay in her room sobbing, she opened her phone to see whether any message had come.",
   [("sob_breath", "ގިސްލަގިސްލާފައި", -22)])
sh(60, "She lay reading the hundreds of messages she had sent Yazan that got no answer. Suddenly the door of the room opened -- it was Qasim.",
   [("door_open", "ހުޅުވިގެން", -16)])
sh(61, "He had come because he heard crying from Shima's room. Seeing Shima's panic and the way she tried to hide the phone, suspicions arose in Qasim's heart.",
   [("gasp", "ހާސްކަމާއި", -20)])
sh(62, "He went straight over, snatched the phone from Shima's hand and began to read the messages in it.",
   [("cloth_rustle", "ޖަހައިގަތް", -20)])
sh(63, "In those messages it was all there, plain to see: Shima saying she was pregnant, her pleading with Yazan, and her begging him to have mercy on the child in her womb.",
   [("heartbeat", "ސާފުކޮށް", -20)], hum=True)
sh(64, "On top of that, the pregnancy test kit lying on Shima's dressing table, which she had not dared to throw away, caught Qasim's sharp eye.",
   [("heartbeat", "ކިޓުވެސް", -18)], hum=True)
sh(65, "Qasim's eyes widened and his face turned red with anger. His whole body began to tremble with the utmost fury that had come over him.",
   [("thunder", "ރުޅިން", -20), ("breath_heavy", "ތުރުތުރުއަޅަން", -20)], hum=True)
sh(66, "He hurled the phone in his hand down onto the floor and smashed it to pieces.",
   [("crash_clatter", "ޖަހައި", -14), ("glass_break", "މުގުރާލި", -12)], hum=True)
SHOTS = S

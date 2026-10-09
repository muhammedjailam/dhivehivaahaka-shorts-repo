"""Beat/shot plan for Marufas episode 430 (used by plan_beats.py)."""

ROOM = ("Yamna's spacious bedroom in the family's large modern island house: white walls, polished white marble floor, "
        "a big bed with white sheets and a pale headboard, a study desk with books and pens under the window, a tall "
        "dark-wood wardrobe, a glass sliding window beside the bed with a sheer white curtain, a round ceiling light")

LOC = {
    "yamna_room": ROOM,
    "yamna_room_calm": ROOM,
    "yamna_room_dawn": ROOM,
    "yamna_room_morning": ROOM,
    "yamna_room_sunset": ROOM,
    "corridor": "the dim marble-floored corridor outside Yamna's bedroom in the family's large modern island house, "
                "white walls, the half-open dark-wood bedroom door with faint light spilling out",
    "kitchen": "a large modern kitchen: carved dark-wood cabinets, a long countertop with a coffee machine and a blender, "
               "a big double-door steel fridge, a sink, red clay and steel bowls",
    "veranda_lane": "the front veranda (fendaa) of the family's large house with a big wooden swing bench, potted plants, "
                    "a sandy yard and flowering trees by the boundary wall, its open gate looking onto a white sandy "
                    "island lane between coral-stone walls, palms and breadfruit trees",
    "island_lane": "white sandy lanes between coral-stone walls, palms and breadfruit trees, a few dim street lamps",
    "mosque": "a small white island mosque seen from the sandy lane outside, palms around it",
    "lagoon": "the dark lagoon and open sea off a small Maldivian island at night, the island's palms a black line on "
              "the horizon",
}
MOOD = {
    "yamna_room": "late night, the round ceiling light dark or flickering, an icy cold blue haze filling the room, a "
                  "single weak warm lamp in a corner, deep charcoal shadows, dread and horror",
    "yamna_room_calm": "late night after the storm of fear, dim cold blue haze, one warm bedside lamp, deep soft shadows, "
                       "exhausted, uneasy stillness",
    "yamna_room_dawn": "just before dawn, faint cold blue-grey light through the sheer curtain, one dim warm lamp, quiet "
                       "and fragile, then a chill",
    "yamna_room_morning": "early morning, soft pale daylight through the sheer curtain, cool clean whites, a fragile calm",
    "yamna_room_sunset": "sunset, a deep crimson and orange sky through the glass window fading into darkness, long "
                         "shadows creeping across the white walls, ominous",
    "corridor": "near midnight, dim cold blue corridor light, a sliver of warm light from the bedroom door, secretive "
                "and tense",
    "kitchen": "morning, soft warm daylight through a window, steam from a cup of tea, homely but a little fragile",
    "veranda_lane": "bright fresh morning sunshine, crisp shadows on white sand, gentle and relieved",
    "island_lane": "deep night, pitch-dark island, a single dim street lamp, cold misty blue haze, urgent and fearful",
    "mosque": "dawn, the first pale blue-grey light of fajr, a warm light glowing from the mosque doorway, mist among the "
              "palms, quiet and peaceful",
    "lagoon": "night, faint silver moonlight on black water, mist on the sea, one small white light on the boat, urgent "
              "and lonely",
}

LOW = "faces in the upper two-thirds, a calm dark uncluttered lower third"
BEDY = ("Yamna lying in the big bed under a white blanket pulled up to her chest, her white hijab snugly covering her hair "
        "and neck, long lilac sleeves")
UNIF = ("a Maldivian school uniform: long-sleeved white tunic to the knees over long navy trousers, white hijab, school "
        "bag on her shoulder")
POSS = ("possession is never shown on her body: no marks, no contortion, she is fully covered and still; the horror is "
        "carried by the room, the light and the parents' faces")

BEATS = [
    # ---------------- NIGHT 1: the first attack
    dict(to=4, reason="episode opening: night, a terrible deep voice comes out of Yamna in her marble bedroom",
         chars=["saahidha", "khalid", "yamna"], loc="yamna_room",
         visual=f"the dark marble bedroom at night: {BEDY}, half sitting against the pale headboard, her face lost in "
                "deep shadow, perfectly still; at the foot of the bed Saahidha and Khalid have stepped back in shock, "
                "Saahidha's hands pressed to her mouth, Khalid's eyes wide, both faces lit from below by a weak lamp; a "
                "cold blue haze hangs in the air",
         camera=f"wide shot from the doorway, eye level, {LOW} (polished marble floor in shadow)", amb="haunted_room",
         sens="other", safe=f"the demonic voice is carried by the parents' horrified faces; {POSS}", transition="dissolve"),
    dict(to=8, reason="action change: the possession attack seizes her on the bed", chars=["yamna"], loc="yamna_room",
         visual=f"the big bed seen from its foot in near darkness: the white sheet violently crumpled and pulled into deep "
                f"ridges, {BEDY}, her face turned up towards the ceiling and hidden in shadow; on the white wall above the "
                "headboard a huge dark smoky shadow with long thin clawed shadowy fingers spreads upward like smoke, "
                "with no face; the round ceiling light flickers",
         camera=f"medium wide, low angle from the foot of the bed, {LOW} (the crumpled sheet edge in soft shadow)",
         amb="haunted_room", sens="violence",
         safe="the arching body, blood-red eyes, foam and torn sheet are replaced by the crumpled sheet, the flickering "
              "light and the smoky shadow on the wall (shadow use 1 of 2); Yamna fully covered, face in shadow"),
    dict(to=12, reason="turning point: the room freezes, the bulbs die, Saahidha screams for Khalid to fetch Saeed",
         chars=["saahidha", "khalid"], loc="yamna_room",
         visual="the bedroom plunged into darkness, the round ceiling light just gone out, faint frosty cold-blue mist "
                "drifting across the marble floor and their breath misting in the cold; Saahidha in her bottle-green "
                "dress and beige hijab turning to Khalid, sobbing, mouth open in a desperate cry, one hand clutching his "
                "sleeve; Khalid pale and frozen beside her; the bed is a dim shape behind them",
         camera=f"medium shot, eye level, {LOW} (dark marble floor with creeping mist)", amb="haunted_room"),
    dict(to=13, reason="location change: Khalid runs out into the dark island night for help", chars=["khalid"],
         loc="island_lane",
         visual="Khalid running fast down an empty white sandy lane at night between coral-stone walls, his cream "
                "shirt pale in the darkness, a single dim street lamp ahead, palms black against the sky, his face "
                "desperate",
         camera=f"medium wide tracking shot from behind and to the side, {LOW} (pale sand of the lane)", amb="night_lane"),
    dict(to=16, reason="character enters: Saeed arrives and recites by the bed", chars=["saeed", "yamna", "saahidha"],
         loc="yamna_room",
         visual=f"Saeed in his light-grey long kurta and white skullcap standing beside the bed with both cupped hands "
                f"raised in front of him, eyes half closed, lips moving in recitation; {BEDY}, her face turned away into "
                "the shadows; Saahidha pressed against the wardrobe in the background, terrified; a weak lamp, cold "
                "blue haze, no book visible",
         camera=f"medium shot from the side of the bed, eye level, {LOW} (blanket edge in shadow)", amb="haunted_room",
         sens="violence", safe=f"the screams and convulsions are carried by the recitation scene; {POSS}"),
    dict(to=20, reason="action change: the attack ends, Yamna sleeps, Saeed gives his grave advice to the parents",
         chars=["saeed", "khalid", "saahidha", "yamna"], loc="yamna_room_calm",
         visual=f"in the background {BEDY}, asleep peacefully with her eyes closed; in the foreground Saeed in his grey "
                "kurta and white skullcap turned to Khalid and Saahidha, speaking gravely with worry on his young face; "
                "the parents exchanging an uneasy look",
         camera=f"medium shot, eye level, {LOW} (marble floor in soft shadow)", amb="room_night"),
    dict(to=22, reason="character leaves: Saeed gone, the parents sit by her bed; Saahidha strokes her forehead",
         chars=["saahidha", "khalid", "yamna"], loc="yamna_room_calm",
         visual=f"{BEDY}, asleep; Saahidha sitting on the edge of the bed gently stroking her daughter's forehead, "
                "looking across at Khalid with pleading, frightened eyes; Khalid sitting on a chair beside the bed, "
                "elbows on his knees",
         camera=f"medium close shot, eye level, {LOW} (white blanket in soft shadow)", amb="room_night"),
    dict(to=24, reason="memory: Khalid recalls Yamna picking garden flowers at sunset these past two weeks",
         chars=["yamna"], loc="veranda_lane",
         visual="a hazy memory: Yamna in her pale-lilac long dress and white hijab standing in the sandy front yard at "
                "sunset under a flowering tree, gathering an armful of pale flowers, looking back towards the house "
                "with a strange distant expression; long amber light, a soft vignette",
         camera=f"medium wide, eye level, {LOW} (sandy yard in long shadow)", amb="memory", transition="dissolve"),
    dict(to=26, reason="time change: the fajr adhan at dawn, Khalid goes to the mosque", chars=["khalid"], loc="mosque",
         visual="the small white island mosque at first light with a warm glow in its doorway; Khalid, a white skullcap "
                "on his head, cream shirt, walking along the sandy lane towards it, seen from behind and the side",
         camera=f"wide shot, eye level, {LOW} (pale sand of the lane)", amb="dawn_exterior", transition="dissolve"),
    # ---------------- MORNING
    dict(to=28, reason="time change: morning, Yamna wakes aching and remembers nothing", chars=["yamna", "saahidha"],
         loc="yamna_room_morning",
         visual=f"{BEDY}, just opening her eyes, weary and confused, wincing slightly; Saahidha sitting on the edge of "
                "the bed bending over her with a forced gentle smile that hides her fear",
         camera=f"medium close shot, slightly high angle, {LOW} (blanket in soft morning shadow)", amb="room_day",
         transition="black"),
    dict(to=31, reason="action change: alone, Saahidha quickly strips the ruined bedsheet", chars=["saahidha"],
         loc="yamna_room_morning",
         visual="Saahidha alone in the bright bedroom hurriedly pulling a badly crumpled, twisted white sheet off the "
                "bed, glancing nervously over her shoulder at the closed bathroom door; a folded fresh sheet waiting on "
                "the chair",
         camera=f"medium shot, eye level, {LOW} (marble floor in soft light)", amb="room_day",
         sens="other", safe="the torn sheet is shown only as crumpled; no marks of the night on Yamna"),
    dict(to=35, reason="location change: Yamna in school uniform asks for tea in the kitchen",
         chars=["yamna", "saahidha"], loc="kitchen",
         visual=f"Yamna dressed for school, NOT in her lilac dress: {UNIF} — a plain white long tunic and navy-blue trousers — "
                "smiling brightly but a little pale and tired, standing at the long countertop; Saahidha "
                "pouring tea into a cup for her, watching her daughter's face with quiet worry",
         camera=f"medium shot, eye level, {LOW} (countertop in soft shadow)", amb="home_day"),
    dict(to=38, reason="location/action change: Yamna sets off to school laughing with friends, Saahidha watches",
         chars=["yamna", "saahidha"], loc="veranda_lane",
         visual=f"in the bright sandy lane outside the gate Yamna in {UNIF} walks away laughing with two school friends "
                "(girls in the same white uniform and white hijab), turning her head to smile; in the foreground Saahidha "
                "stands at the veranda gate watching them go, a hand on her heart, relieved",
         camera=f"wide shot over Saahidha's shoulder, eye level, {LOW} (white sand of the yard)", amb="island_day"),
    # ---------------- SUNSET: the second attack
    dict(to=40, reason="time change: sunset, the sky reddens and Yamna's smile vanishes", chars=["yamna"],
         loc="yamna_room_sunset",
         visual="Yamna in her pale-lilac long dress and white hijab standing at the glass window of her bedroom, a deep "
                "crimson sunset sky behind the palms outside; her face, half lit by the dying light and half in shadow, "
                "slowly losing its smile, turning blank and still, her eyes wide and empty",
         camera=f"medium close shot, eye level, {LOW} (dark windowsill and floor)", amb="haunted_room",
         transition="black", sens="other", safe="calm blank face only, no marks"),
    dict(to=43, reason="action change: the attack returns worse than before, a heavy male voice screams",
         chars=["saahidha", "khalid", "yamna"], loc="yamna_room",
         visual=f"night, the ceiling light stuttering; {BEDY}, shown only as a dark still shape with her face hidden in "
                "shadow, the sheet crumpled in ridges around her; Saahidha and Khalid standing a little apart side by side, "
                "backed against the white wall, not touching each other, each frozen alone in terror, their faces lit by the flickering light",
         camera=f"wide shot, eye level, {LOW} (marble floor in shadow)", amb="haunted_room",
         sens="violence", safe=f"the convulsions are shown through the flickering light and the parents' terror; {POSS}"),
    dict(to=46, reason="focus change: Khalid, sweating, realises Saeed was right; Saahidha weeps",
         chars=["khalid", "saahidha"], loc="yamna_room",
         visual="close on Khalid's face in the flickering dark, beads of sweat on his forehead, jaw set with sudden "
                "resolve, looking to the side; behind him, out of focus, Saahidha sits crumpled on a chair crying into "
                "her hands",
         camera=f"close-up, eye level, {LOW} (dark shirt and shadow)", amb="haunted_room", transition="xfade"),
    dict(to=47, reason="location change: a launch is sent across the night sea for the raqi", chars=[], loc="lagoon",
         visual="a small white speed launch cutting across the black lagoon at night, its single light reflected on the "
                "water, a white wake behind it, mist on the sea, the island a dark line of palms",
         camera="wide shot, slightly high angle, the boat in the upper half, the dark water as the calm lower third",
         amb="sea_boat"),
    # ---------------- MIDNIGHT: Ghassan
    dict(to=49, reason="character enters: near midnight the raqi Ghassan arrives with his black bag",
         chars=["ghassan", "yamna"], loc="yamna_room",
         visual=f"Ghassan in a white shirt buttoned to the collar and black trousers, a big black leather bag on his "
                f"shoulder, standing in the bedroom doorway, frowning with unease; in the foreground {BEDY}, lying very "
                "still, staring at him with wide cold unblinking eyes, her face pale and unmarked; icy blue haze",
         camera=f"medium shot from beside the bed towards the door, {LOW} (blanket edge in shadow)",
         amb="haunted_room", sens="other", safe="cold stare only, no marks"),
    dict(to=51, reason="location/action change: Ghassan takes Khalid aside and whispers in secret",
         chars=["ghassan", "khalid"], loc="corridor",
         visual="Ghassan leaning close to Khalid in the dim corridor outside the bedroom, one hand on Khalid's shoulder, "
                "speaking low and secretively; Khalid listening anxiously; the black bag hanging at Ghassan's side",
         camera=f"medium two-shot, eye level, {LOW} (marble corridor floor in shadow)", amb="living_night"),
    dict(to=54, reason="action change: Ghassan holds his palm over her forehead and recites; the attack erupts",
         chars=["ghassan", "yamna", "khalid", "saahidha"], loc="yamna_room",
         visual=f"Ghassan standing over the bed, his right palm hovering just above Yamna's forehead without touching, "
                f"lips moving in a low powerful recitation; {BEDY}, her face in shadow; Khalid and Saahidha on the "
                "other side of the bed, leaning in with outstretched hands but afraid to touch, strained and frightened; "
                "the ceiling light flickering",
         camera=f"medium wide, eye level, {LOW} (dark sheet and floor)", amb="haunted_room",
         sens="violence", safe=f"palm hovers, never touches; the thrashing is shown through the strained parents; {POSS}"),
    dict(to=56, reason="action change: Yamna flings Saahidha away", chars=["saahidha", "yamna"], loc="yamna_room",
         visual="Saahidha sitting on the cold marble floor beside the bed where she has been flung, one hand on the floor, "
                "the other at her mouth, staring up in shock; above her on the bed only Yamna's dark silhouette sitting "
                "up, face completely in shadow, her white hijab a faint pale shape",
         camera=f"medium shot, low angle from the floor, {LOW} (marble floor)", amb="haunted_room",
         sens="violence", safe="the shove and the self-scratching are not shown: only Saahidha unhurt on the floor in "
                            "shock and Yamna as a faceless silhouette"),
    dict(to=58, reason="turning point: a heavy male laugh, 'Stop reciting!' — the jinn's presence fills the room",
         chars=["ghassan"], loc="yamna_room",
         visual="a huge dark smoky shadow with long thin clawed shadowy fingers rising up the white bedroom wall above "
                "the headboard, like smoke, with no face, the ceiling light dimmed to a faint glow; Ghassan seen from behind in the "
                "lower left, a dark figure with his palm raised towards it",
         camera=f"wide shot, low angle, the shadow filling the upper wall, {LOW} (dark headboard and floor)",
         amb="haunted_room", sens="violence",
         safe="blood and torn cheeks replaced by the smoky shadow on the wall (shadow use 2 of 2); Yamna not shown"),
    dict(to=60, reason="focus change: Ghassan questions the jinn; a cold mocking smile on Yamna's face",
         chars=["yamna", "ghassan"], loc="yamna_room",
         visual="close-up of Yamna's face resting against the white pillow, half in deep shadow, completely unmarked and "
                "still, white hijab snug around her face, a faint cold smile and a cold stare; Ghassan's raised palm "
                "blurred at the edge of the frame",
         camera=f"close-up, eye level, {LOW} (pillow and blanket in shadow)", amb="haunted_room",
         sens="other", safe="cold smile only, no marks, no red eyes"),
    dict(to=63, reason="turning point: the jinn turns her head to Khalid at the door and accuses him",
         chars=["khalid", "yamna", "saahidha"], loc="yamna_room",
         visual="over Yamna's shoulder from behind — only the back of her white hijab as she sits up in bed in the dark "
                "— towards Khalid standing frozen in the doorway, his face drained of colour, mouth open; Saahidha at "
                "the side of the bed turning to stare at him in disbelief; cold blue haze",
         camera=f"over-the-shoulder medium shot, eye level, {LOW} (dark blanket and floor)", amb="haunted_room"),
    dict(to=66, reason="action change: Saahidha jumps up, hugs Yamna and sobs", chars=["saahidha", "yamna"],
         loc="yamna_room",
         visual=f"Saahidha sitting on the bed holding her daughter tightly in her arms, cheek pressed to Yamna's white "
                "hijab, eyes squeezed shut, weeping; Yamna limp and still in her lilac dress, face turned away into "
                "shadow, the blanket over her lap",
         camera=f"medium close shot, eye level, {LOW} (blanket in shadow)", amb="haunted_room"),
    dict(to=68, reason="return to Ghassan reciting at the bed; he grows anxious and slows the recitation",
         chars=["ghassan", "yamna", "khalid", "saahidha"], loc="yamna_room", reuse="beat_020", amb="haunted_room",
         visual="reuse of Ghassan reciting at the bed"),
    dict(to=71, reason="turning point: Saahidha glares at Khalid with hatred and orders him out; Khalid and Saeed leave",
         chars=["saahidha", "khalid", "saeed", "yamna"], loc="yamna_room_calm",
         visual=f"in the background {BEDY}, asleep; Saahidha standing by the bed glaring at Khalid with cold fury, chin "
                "raised; Khalid, head bowed like a scolded child, turning towards the doorway where Saeed in his grey "
                "kurta and white skullcap waits, eyes lowered",
         camera=f"medium wide, eye level, {LOW} (marble floor)", amb="room_night"),
    # ---------------- FAJR
    dict(to=73, reason="time change: after fajr Saahidha sits by Yamna and calls her to pray",
         chars=["saahidha", "yamna"], loc="yamna_room_dawn",
         visual=f"{BEDY}, asleep on her side; Saahidha in her bottle-green dress and beige hijab sitting beside her on "
                "the bed, leaning over gently, one hand reaching to tap her daughter's arm through the blanket, calling "
                "her softly",
         camera=f"medium shot, eye level, {LOW} (white blanket)", amb="room_night", transition="black"),
    dict(to=76, reason="action change: Yamna jolts upright and glares at her mother",
         chars=["yamna", "saahidha"], loc="yamna_room_dawn",
         visual="Yamna sitting bolt upright in bed in her lilac dress and white hijab, the blanket at her waist, glaring "
                "at Saahidha with a cold, hostile stare, half her face in shadow, unmarked; Saahidha recoiling slightly, "
                "her soft smile freezing on her face",
         camera=f"medium two-shot, eye level, {LOW} (blanket in shadow)", amb="haunted_room",
         sens="other", safe="hostility shown only by a cold stare"),
    dict(to=80, reason="action change: Saahidha, shaken, leaves the room as the voice echoes",
         chars=["saahidha", "yamna"], loc="yamna_room_dawn",
         visual="Saahidha in the doorway seen from the corridor, one hand gripping the door frame, the other pressed to "
                "her chest, trembling, eyes full of tears, about to step out; behind her in the dim room Yamna's dark "
                "silhouette sitting upright in bed, face in shadow, a cold blue haze around her",
         camera=f"medium shot from the corridor, eye level, {LOW} (marble floor of the corridor)", amb="haunted_room",
         sens="other", safe="Yamna only as a silhouette"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The pitiless silence that ruled that spacious modern room with its gleaming marble floor was shattered by a terrifying voice that came out of Yamna's throat.",
   [("low_growl", "އަޑުންނެވެ", -21)], hum=True)
sh(2, "\"Do you people think what you're doing is something so clever?\" With those words, everyone gathered near Yamna felt their skin crawl.")
sh(3, "The femininity and gentleness that had been in her voice only a little while before had now vanished completely.")
sh(4, "There was no longer any trace of a human being in that voice. That voice held only heaviness and terror. And with those very words,")
sh(5, "Yamna's body was wrenched backwards on the big bed. In an unnatural way no human strength could manage, her spine bent,",
   [("cloth_rustle", "ދަމައިގަތެވެ", -20)], hum=True)
sh(6, "and her belly rose upward. Her head fell back, and her eyes, filled with blood-red, grew huge and fixed on the ceiling.",
   hum=True)
sh(7, "As thick dark foam spread over her face and ran down her chin, the loud scream pouring from her throat felt as if it would burst their eardrums.")
sh(8, "At the same time, the fingers of her hands and feet curled, her veins bulged, and like claws they tore at the bedsheet and sank into the mattress.",
   [("cloth_rustle", "ވީދައިލަމުން", -19)])
sh(9, "The temperature of the whole room suddenly dropped, and a cold that could freeze the blood took over the whole atmosphere.",
   hum=True)
sh(10, "At that same moment the brightly lit bulbs went out. \"Khalid! Khalid, hurry, go and fetch Saeed!\"",
   [("bulb_flicker", "ނިވިގެންދިޔައެވެ", -16)])
sh(11, "As Yamna's mother, Saahidha, cried this out, she broke into loud sobs. Her voice was full of utter panic and trembling.",
   [("sob_breath", "ރޮވިއްޖެއެވެ", -22)])
sh(12, "Seeing her child in this terrifying state had filled her heart with unbearable feelings. At Saahidha's words, Yamna's father,")
sh(13, "Khalid, rushed out of the room, hoping to find help in any way he could. With fear ruling the whole house, the hours of the night dragged on.",
   [("footsteps_sand", "ދުއްވައިގަތީ", -22)])
sh(14, "Even when Saeed came with Khalid and entered the room, there was no change in Yamna's state. Saeed quickly came close,",
   [("door_open", "ވަތްއިރުވެސް", -20)])
sh(15, "recited verses of the Holy Quran and began a short ruqyah. As the noble sound of the Quran echoed through the room,",
   [("whisper_recite", "ކިޔަވައި", -23)])
sh(16, "Yamna's screams grew louder too. Then convulsions ran through Yamna's body, and at last, utterly exhausted, she collapsed onto the bed.",
   [("soft_thud", "ވެއްޓުނެވެ", -22)], hum=True)
sh(17, "By then the whole island lay in pitch darkness, deep in the night. When Yamna's breathing settled, Saeed let out a deep breath and looked at Khalid and Saahidha.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(18, "By then Yamna lay in a deep sleep. \"This doesn't look like an ordinary matter. Even though I know how to recite a little,")
sh(19, "I think this girl should be shown to someone who performs ruqyah, to have her checked!\" Saeed gave advice that made their hearts tremble.")
sh(20, "Saahidha and Khalid looked at each other uneasily. They too could see the shades of fear and unease on Saeed's young face.")
sh(21, "After Saeed left the house, Saahidha and Khalid sat down beside the bed where Yamna lay. Stroking Yamna's forehead, Saahidha looked at Khalid.",
   [("door_close", "ނިކުމެގެންދިޔުމާއެކު", -22)])
sh(22, "\"Last week she had such a high fever and such a bad headache... could it be because of that?\" Saahidha asked Khalid, not wanting to accept the terrifying truth she had seen with her own eyes.")
sh(23, "Khalid sat in silence without an answer, not knowing what to believe. What kept coming back to his mind were certain behaviours he had noticed in Yamna over the past two weeks or so.")
sh(24, "Lately she had always been ill, and around sunset she would pick flowers from the trees beside the house and bring them inside; those memories became",
   hum=True)
sh(25, "signs that made his skin crawl. As the couple sat sunk in these thoughts, the call to the fajr prayer rang out and a coolness settled on their hearts.")
sh(26, "\"Call kamana to pray! I'll come too, after I've prayed.\" Saying this, Khalid got up from the bed and walked away. \"Mother!",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -24)])
sh(27, "My body aches so much!\" When Saahidha called her twice, Yamna opened her eyes and said this wearily.")
sh(28, "For a while Saahidha sat not knowing what to answer. \"Maybe it's because you sat up studying too long before you slept, dear.\"")
sh(29, "Realising Yamna had no memory at all of what had happened in the night, Saahidha did not want to put that fear into her innocent child's heart.")
sh(30, "That was also why, the moment her daughter went into the bathroom, she quickly changed the torn bedsheet on the bed",
   [("door_close", "ވަތް", -22), ("cloth_rustle", "ބެޑްޝީޓް", -20)])
sh(31, "and tidied up the room. \"Mother, there's a very important test at school today.")
sh(32, "So even if my body aches, I can't stay at home, can I! Make me some tea, quick!\" Yamna said with a smile as she came out of her room.")
sh(33, "She was in her school uniform, her soft black hair neatly tied up. \"Mother, there are swollen red patches on my skin!")
sh(34, "Maybe I got an allergy from eating out last night! I'll take a tablet too, okay!\" Yamna said with a smile.")
sh(35, "Not a trace of the terrifying figure of the night could be seen on that innocent face today. Yet however brave she tried to be, the weariness showed on her face.")
sh(36, "Yamna sat calmly, drank her tea, slung her school bag on her shoulder and set off for school. Joking with the friends she met on the road,",
   [("cup_clatter", "ސައިބޮއިގެން", -20)])
sh(37, "she went off to school laughing and laughing, while Saahidha stood watching. A great relief settled on the hearts of the whole family.",
   [("footsteps_sand", "ދިޔަތަން", -24)])
sh(38, "Everyone believed the night's terror had been something passing, and that Yamna was completely well. However,")
sh(39, "it was the kind of brief silence that comes before a storm. The daytime slipped by quickly, and soon it was close to sunset.",
   hum=True)
sh(40, "As the sky turned red and darkness began to take over the world, the brightness and the smile on Yamna's face suddenly began to fade.",
   hum=True)
sh(41, "Her eyes widened, her body began to tremble again, and her body began to behave in ways far more frightening than the night before.",
   [("heartbeat", "ތުރުތުރު", -20)])
sh(42, "Those terrifying convulsions seized her body once more. On the bed, even more frighteningly than the night before, Yamna's spine bent backwards,")
sh(43, "her belly rising up. Clawing at the bedsheet with curled fingers, a heavy male voice screamed from her throat, so loud it seemed to make the very walls of the house shake.",
   [("low_growl", "ފިރިހެން", -20)], hum=True)
sh(44, "\"Saeed was right! This is no ordinary thing.\" As beads of sweat broke out on Khalid's forehead,")
sh(45, "he anxiously looked at his wife, Saahidha. Saahidha sat there in tears, so frightened she had no idea what to do.",
   [("sob_breath", "ރޮވިފައެވެ", -24)])
sh(46, "Khalid was an influential businessman of the island, and he could not bear to watch his only daughter suffer such pain.")
sh(47, "He immediately picked up the phone, called a very famous and skilled raqi from outside the island, and sent a launch so that he would come to the island that same night.",
   [("phone_buzz", "ފޯނު", -22), ("boat_engine", "ލޯންޗެއް", -20)])
sh(48, "When it was close to midnight, the raqi Ghassan, dressed in black trousers and a white shirt, arrived and entered the room.",
   [("door_open", "ވަނެވެ", -20)])
sh(49, "On his shoulder hung a big black bag. At the unnatural cold ruling the room, and at the terrifying gaze of Yamna, lying back with eyes wide open, unease showed even on Ghassan's face.")
sh(50, "Ghassan tapped Khalid gently on the shoulder and signalled him to step aside to talk alone. After that,")
sh(51, "after secretly discussing some important matters with Khalid, he stepped forward and stopped right beside Yamna.",
   [("footsteps_pavement", "ފިޔަވަޅުތައް", -24)])
sh(52, "Without hesitation Ghassan placed his palm over Yamna's forehead. Moving his lips, he began to recite in a soft yet powerful tone.",
   [("whisper_recite", "ކިޔަވަން", -22)])
sh(53, "At once a violent convulsion seized Yamna's whole body, and she thrashed harder than before. It was no ordinary human strength.",
   [("cloth_rustle", "ތެޅިގަތެވެ", -18)], hum=True)
sh(54, "Khalid and Saahidha, right beside her, could not calm her or hold her down even with all their courage.")
sh(55, "Suddenly, like a madwoman, Yamna flung her arms out and threw Saahidha off. And as quick as lightning,",
   [("soft_thud", "ކޮއްޕާލައިފިއެވެ", -20)])
sh(56, "she raked her long sharp nails down her own cheeks. As she slowly lowered her hand, deep gashes stretched across that beautiful fair face.",
   [("gasp", "ހަރާލިއެވެ", -22)], hum=True)
sh(57, "At that moment the skin split and red blood ran down her cheeks. With that horrifying sight, a loud laugh in a heavy male voice came from Yamna's throat.",
   [("low_growl", "ހިނިގަނޑެއްގެ", -19)], hum=True)
sh(58, "That voice was full of cruelty and mockery. \"Stop! Stop that reciting!\" screamed the unseen force inside Yamna's body.")
sh(59, "Ghassan did not stop reciting. He recited more forcefully and began to question the jinn directly. \"Who sent you?",
   [("whisper_recite", "ކިޔެވުން", -22)])
sh(60, "Why are you inside this innocent girl's body?\" At that moment a wicked, mocking smile spread across Yamna's face.")
sh(61, "She slowly turned her head and looked at Khalid, who stood at the door frozen with fear. \"It was one of you who sent me to destroy this girl!\"",
   [("heartbeat", "ބިރުން", -22)], hum=True)
sh(62, "said the jinn. \"Who?\" Khalid shouted impatiently. The jinn answered Khalid's question even more loudly than before.")
sh(63, "\"Are you trying to be a saint? It was you yourself who handed this innocent girl over to us!\" As it became clear the jinn meant Khalid, astonishment showed on the faces of the other two as well.",
   [("gasp", "ހައިރާންކަމެވެ", -20)], hum=True)
sh(64, "Saahidha, who had been frozen by the sudden shock, sprang up, threw her arms around Yamna and began to weep.",
   [("sob_breath", "ރޯންފެށިއެވެ", -22)])
sh(65, "Yamna was her only daughter. Seeing the wretched state her child was in today, her heart broke into pieces.")
sh(66, "And how could she believe that the root of this harm to her child was Khalid? Yet that voice came from her child's own mouth.")
sh(67, "\"Stop reciting right now! Or what I do to this body next will be far worse than this.\" At its wicked command Ghassan grew anxious.")
sh(68, "In the light of his long experience, he was sure he could only go further after more preparation. So he slowly let his recitation fade.")
sh(69, "With that, just like the night before, Yamna's body slowly settled back onto the bed. On Saahidha's face were the colours of hatred.")
sh(70, "She looked at Khalid in anger. \"That's not true,\" was the only short sentence Khalid could say. \"Get out right now!\" was Saahidha's harsh command.")
sh(71, "Like an obedient little child, Khalid walked out of the room. After Khalid, Saeed too walked out of that room.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(72, "As usual, after praying fajr Saahidha went to wake Yamna for prayer. She sat beside her darling daughter, the apple of her eye, and called her to pray.")
sh(73, "When there was no response from Yamna even after calling two or three times, Saahidha tapped Yamna's arm.")
sh(74, "At that, Yamna jolted up and sat upright on the bed, and stared angrily into Saahidha's face.",
   [("cloth_rustle", "ތެދުވެ", -18)], hum=True)
sh(75, "Saahidha instantly sensed the sudden change in Yamna's nature. \"You'll pray and then go back to sleep, won't you, dear!\"")
sh(76, "Saahidha said very tenderly, hoping to coax her child. \"What prayer? Go and do your own thing, what's it got to do with me?\"")
sh(77, "At Yamna's reply Saahidha felt as if boiling water had been poured over her heart. That child had never once raised her voice to Saahidha.",
   hum=True)
sh(78, "She was certain that the words and the tone were not her daughter's.")
sh(79, "Her daughter's body was now held captive by some unknown, powerful spirit creature. \"Get out of here right now!\" Yamna's voice echoed through the room.",
   hum=True)
sh(80, "Saahidha left trembling. With the blow her heart had taken, she slowly walked out of the room. (To be continued)",
   [("door_close", "ހިނގައިގަތެވެ", -22)])
SHOTS = S

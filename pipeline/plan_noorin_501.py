"""Beat/shot plan for Noorin episode 501 (used by plan_beats.py).
The whole episode is the TWELVE-YEARS-AGO timeline (noorin_young, uvaish_young, aakif_young, reem ~22).
Series content rules (series_bible.md) override the literal narration."""

FB = "twelve years earlier, warm soft golden haze"

LOC = {
    "staff_room": "young Noorin's small staff room at a resort under construction in the Maldives, twelve years ago: whitewashed walls, a simple cushioned sofa, a small wooden desk, a window with sheer white curtains and palm fronds outside, an open wooden door",
    "rain_memory": "a crowded Malé street at night twelve years ago, shop awnings, heavy rain, a wet road reflecting amber shop lights",
    "nikah": "a small modest nikah gathering in the living room of a simple Maldivian home twelve years ago: woven mats and floor cushions, a low wooden table, white jasmine flowers, an open window to palms at sunset",
    "home_divorce": "the bright furnished living room of a modern house in Malé where the young couple lived twelve years ago: a cream sofa, a wooden front door, a window with sheer curtains",
    "home_alone": "the bright furnished living room of a modern house in Malé where the young couple lived twelve years ago: a cream sofa, an empty armchair, a window with sheer curtains",
    "island_lane": "a sandy lane on a small Maldivian island twelve years ago, low coral-stone walls, coconut palms, small houses with tin roofs",
    "island_beach": "the quiet beach of a small Maldivian island twelve years ago, dry white sand, a calm turquoise lagoon, leaning coconut palms",
    "stairwell": "a narrow concrete stairwell inside an old apartment building in Malé twelve years ago, steep stairs with a metal handrail, a closed lift door on the landing, a small dusty window",
    "island_house": "the shaded veranda of a small island house twelve years ago, a wooden bench, a coral-stone wall, palms and a sandy yard",
    "aakif_home": "the elegant living room of a large respectable family home in Malé twelve years ago: carved wooden furniture, cream sofas, a patterned rug, tall windows with curtains, paintings of the sea without any text",
    "event": "an elegant evening reception hall in Malé twelve years ago: round tables with white tablecloths, warm crystal chandeliers, blurred guests mingling in the background, glasses of juice",
    "side_room": "a small empty side room off the reception hall twelve years ago: a few stacked chairs, a plain wall, a closed wooden door, a single wall lamp",
    "corridor": "an empty carpeted hotel corridor in Malé at night twelve years ago, a row of closed wooden doors, dim brass wall sconces",
    "night_window": "a hotel room window at night twelve years ago, rain streaks running down the glass, blurred Malé city lights beyond, a plain windowsill",
    "aakif_room": "Aakif's quiet study in his family home in Malé at night twelve years ago: a wooden desk, a desk lamp, bookshelves, a dark window",
    "big_beach": "a wide open beach on a Maldivian island like Maafushi at dusk twelve years ago, wide dry white sand, huge waves breaking far out, dark storm clouds over the ocean, a line of palms behind",
    "beach_grief": "a wide open beach on a Maldivian island at dusk twelve years ago, dry white sand, palms, a cloudy sky over the ocean",
    "beach_light": "a wide open beach on a Maldivian island like Maafushi at dusk twelve years ago, wide dry white sand, big waves far out, storm clouds over the ocean, a line of palms behind",
    "symbol_lane": "a peaceful sunlit lane on a Maldivian island, low coral-stone walls, coconut palms, white sand",
    "symbol_hands": "a softly blurred background of a sunlit Maldivian island garden",
    "dawn": "the sky over a calm Maldivian island lagoon at dawn, coconut palms in silhouette and a simple white mosque minaret against the brightening sky",
}
MOOD = {
    "staff_room": f"{FB}, late afternoon light through sheer curtains, tender, tearful, hopeful",
    "rain_memory": f"{FB} over the rain, a blurred dreamlike recollection, amber streetlights in rain streaks, soft vignette",
    "nikah": f"{FB}, glowing sunset light, joyful, shy, tender",
    "home_divorce": f"{FB} turned grey and cold, overcast daylight, shock and heartbreak",
    "home_alone": f"{FB} fading into dusk, long shadows, a single lamp, lonely and aching",
    "island_lane": f"{FB}, harsh bright afternoon sun and hard shadows, hostile whispers, humiliation",
    "island_beach": f"{FB}, evening, the sun low over the lagoon, long shadows, lonely, melancholic",
    "stairwell": f"a memory within the memory: {FB}, dusty daylight beams through the small window, sudden urgency",
    "island_house": f"{FB}, gentle late afternoon, earnest, protective, kind",
    "aakif_home": f"{FB}, soft warm daylight, safe, calm, a new beginning",
    "event": f"{FB}, warm chandelier light, festive murmur turning tense",
    "side_room": f"{FB} gone dim and cold, a single wall lamp, tense, accusing, heartbreaking",
    "corridor": f"{FB} almost gone, late night, dim amber sconces in long shadows, silent, heavy grief",
    "night_window": f"{FB} almost gone, late night, cold blue rain light, deep sorrow, stillness",
    "aakif_room": f"{FB}, night, the single warm desk lamp against dark shadows, worry",
    "big_beach": f"{FB} at dusk under dark storm clouds, roaring waves, wind, desolate, despairing",
    "beach_grief": f"{FB} at dusk under heavy clouds, wind, overwhelming sorrow",
    "beach_light": f"{FB}, dusk, a shaft of golden light breaking through the dark storm clouds, hope returning, peace",
    "symbol_lane": "soft warm golden morning light, dignity, patience, gentle hope",
    "symbol_hands": "warm golden light, compassion, kindness",
    "dawn": "dawn, soft gold light rays breaking through blue haze, peaceful, hopeful, spiritual",
}

BEATS = [
    # ---------------- the proposal (staff room at the resort) ----------------
    dict(to=2, reason="episode opening (flashback continues from 497): Uvaish turns back into Noorin's room; her eyes fill with tears",
         chars=["noorin_young", "uvaish_young"], loc="staff_room", transition="dissolve",
         visual="young Uvaish has just walked back in from the open door and stands a clear arm's-length away from young Noorin, looking at her gently; young Noorin stands by the sofa, her large eyes filling with tears, hands clasped at her chest; a clear arm's-length gap, nobody touching",
         camera="medium two-shot, eye level, both faces in the upper half", amb="room_day"),
    dict(to=5, reason="memory: the rainy night two months ago and the unknown man who protected her",
         loc="rain_memory", transition="dissolve",
         visual="dreamlike memory: a rainy Malé street at night, a tall young man in a white shirt seen only from behind holding a black umbrella under a shop awning, the rain glowing amber around him, the whole scene softly blurred like a recollection; no faces visible",
         camera="medium wide, from behind the man, the umbrella in the upper half, the wet reflective road as a calm lower third",
         amb="memory_rain"),
    dict(to=8, reason="back from the memory to the room: he says he came to find his heart", reuse="beat_001",
         chars=["noorin_young", "uvaish_young"], loc="staff_room", transition="dissolve",
         visual="(reuse of beat_001)", amb="room_day"),
    dict(to=10, reason="emotional turning point: the marriage proposal",
         chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual="young Uvaish, earnest and serious now, one hand placed on his own chest, speaking a heartfelt proposal; young Noorin facing him at a clear arm's-length gap, her tear-filled eyes wide open in disbelief; nobody touching",
         camera="medium two-shot from the side, eye level", amb="room_day"),
    dict(to=14, reason="focus moves to Noorin's inner doubts: why would the rich resort owner choose her",
         chars=["noorin_young"], loc="staff_room",
         visual="close-up of young Noorin's face, tear-filled wide eyes glancing aside, lost in thought, doubt and wonder mixed together, her cream hijab neatly covering her hair and neck",
         camera="close-up, eye level, face in the upper half", amb="room_day"),
    dict(to=18, reason="action change: Uvaish smiles playfully and keeps asking teasing questions",
         chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual="young Uvaish smiling playfully with his head tilted, hands in his trouser pockets, asking a teasing question; young Noorin facing him at a clear arm's-length gap, looking down shyly, lips parted, unsure what to answer; nobody touching",
         camera="medium wide two-shot, eye level, from the window side", amb="room_day"),
    dict(to=23, reason="focus on Uvaish's face as he speaks softly and sincerely of his love and two months of waiting",
         chars=["uvaish_young", "noorin_young"], loc="staff_room",
         visual="over-the-shoulder shot from behind young Noorin's cream hijab towards young Uvaish's face: his kind dark eyes full of tenderness, a soft sincere expression as he speaks quietly; a clear arm's-length gap between them",
         camera="over-the-shoulder close shot, eye level", amb="room_day"),
    dict(to=24, reason="return to Noorin's face: her heart filled with gratitude", reuse="beat_005",
         chars=["noorin_young"], loc="staff_room", visual="(reuse of beat_005)", amb="room_day"),
    dict(to=28, reason="action change: she begins to answer and he raises his palm to stop her words",
         chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual="young Noorin starting to speak, hesitant and frightened; young Uvaish raises one hand palm-out in the air between them at a clear arm's-length distance to gently stop her words, a pleading, emotional look on his face; nobody touching",
         camera="medium two-shot, eye level", amb="room_day", sens="intimacy",
         safe="the narration's finger on her lips is replaced by Uvaish raising a palm-out hand at arm's length (bible rule 6); no touch"),
    dict(to=31, reason="emotional turning point: despite her unease she decides to trust him and accepts",
         chars=["noorin_young", "uvaish_young"], loc="staff_room",
         visual="young Noorin looking up at Uvaish with a shy, trembling, hopeful smile and a small nod, her eyes still wet, a trace of unease in her face; young Uvaish smiling with relief; a clear arm's-length gap, nobody touching",
         camera="medium close two-shot, slightly low angle, warm window light behind them", amb="room_day"),
    # ---------------- marriage, divorce, waiting ----------------
    dict(to=33, reason="time jump: the nikah and the first two happy weeks of marriage",
         chars=["noorin_young", "uvaish_young"], loc="nikah", transition="black",
         visual="young Noorin and young Uvaish, newly married, seated side by side on floor cushions at a small nikah gathering, both smiling shyly; her henna-decorated hands folded in her lap; on the low table before them two cups of tea and a small open ring box; a few blurred relatives in the background; fully clothed, no embrace",
         camera="medium wide, eye level, the couple in the upper half, the low table as the lower third", amb="home_day",
         sens="intimacy", safe="married couple shown only seated side by side at the nikah with henna hands, tea cups and a ring box (bible rule 7)"),
    dict(to=36, reason="time jump two weeks later: the sudden divorce and his departure",
         chars=["uvaish_young", "noorin_young"], loc="home_divorce", transition="black",
         visual="young Uvaish standing at the open front door with a travel bag in his hand, half turned away, his face troubled and evasive, not meeting her eyes; young Noorin standing several steps back in the room, frozen in shock, tears running down her cheeks, one hand at her mouth",
         camera="medium wide, eye level, from inside the room", amb="home_day"),
    dict(to=39, reason="action change: she waits alone in the house, pregnant, and finally decides to leave for her island",
         chars=["noorin_young"], loc="home_alone",
         visual="young Noorin sitting alone on the cream sofa by the window, one hand resting gently on a small modest pregnancy bump under her loose dress, gazing at the empty armchair opposite with sad, aching eyes; a small packed travel bag at her feet",
         camera="medium wide, eye level, slightly from the side", amb="home_day"),
    # ---------------- the island ----------------
    dict(to=42, reason="scene change: on her home island the rumours spread and islanders mock her in the lane",
         chars=["noorin_young"], loc="island_lane", transition="black",
         visual="young Noorin walking alone down the sandy lane, eyes lowered, both arms wrapped protectively around a gentle modest pregnancy bump under her loose dress; far behind her in the background a few islanders (women in headscarves, men in shirts and sarongs) whisper behind their hands and point at her; a few scraps of crumpled paper and coconut husks lie on the sand near her feet; nobody near her",
         camera="medium wide, eye level, Noorin in the upper half, the sandy lane as the lower third", amb="village_day",
         sens="violence", safe="the rubbish-throwing is shown only as distant pointing and whispering and a few scraps on the sand; nothing hits her on screen (bible rule 10)"),
    dict(to=47, reason="scene change: in the evening she goes to the beach for a little comfort",
         chars=["noorin_young"], loc="island_beach",
         visual="young Noorin sitting alone on the dry white sand far from the water, knees drawn up beside her gentle pregnancy bump, arms resting around it, gazing at the lagoon and the low sun with tired, lonely eyes",
         camera="wide shot from the side, she sits in the upper half, the smooth sand as the lower third", amb="beach_evening"),
    dict(to=51, reason="action change: something thrown at her; she shields her unborn child",
         chars=["noorin_young"], loc="island_beach",
         visual="young Noorin on the dry sand, flinching and curled forward, both arms wrapped protectively around her gentle pregnancy bump, eyes squeezed shut, a tear on her cheek; a crumpled scrap of rubbish lying on the sand beside her; far in the background under the palms a few shadowy figures turning away; nobody near her",
         camera="medium shot, eye level", amb="beach_evening",
         sens="violence", safe="the impact is not shown: only her protective reaction and a scrap of rubbish on the sand (bible rule 10)"),
    # ---------------- Aakif's backstory (flashback within the flashback) ----------------
    dict(to=53, reason="flashback within the flashback: her first day in Malé, climbing the stairs, an inhaler falls at her feet",
         chars=["noorin_young"], loc="stairwell", transition="dissolve",
         visual="young Noorin climbing the narrow concrete stairs with a travel bag in her hand, stopping in surprise and looking down at a small blue inhaler that has just fallen onto the step at her feet, then glancing up the stairwell",
         camera="medium shot from a few steps above, looking down at her", amb="memory"),
    dict(to=54, reason="action change: she hurries up and brings the inhaler to the young man struggling to breathe",
         chars=["noorin_young", "aakif_young"], loc="stairwell",
         visual="young Aakif sitting on a stair step on the landing, breathless, one hand pressed to his chest, his glasses askew, eyes pleading; young Noorin, her bag set down on the steps behind her, holding the small blue inhaler out to him at a clear arm's-length gap; nobody touching",
         camera="medium two-shot, eye level", amb="memory", sens="other",
         safe="the asthma attack is shown calmly: he is sitting up on a step, she holds out the inhaler at arm's length"),
    dict(to=58, reason="back from the inner flashback: Aakif, having heard her story, vows to repay her kindness",
         chars=["aakif_young", "noorin_young"], loc="island_house", transition="dissolve",
         visual="young Aakif standing on the veranda at a clear arm's-length gap from young Noorin, speaking earnestly with one hand on his own chest, determined and kind; young Noorin sitting on the wooden bench, her gentle pregnancy bump under her loose dress, listening with teary, grateful eyes; nobody touching",
         camera="medium two-shot, eye level", amb="island_house_day"),
    dict(to=61, reason="scene change: Aakif brings her to Malé and keeps her in his family home",
         chars=["noorin_young", "aakif_young"], loc="aakif_home", transition="black",
         visual="young Noorin seated on a cream sofa in the elegant living room, hands folded over her gentle pregnancy bump, looking around shyly; young Aakif standing several steps away with a kind welcoming gesture; an older Maldivian woman in a dark headscarf and long dress (his mother) smiling warmly in the background",
         camera="medium wide, eye level", amb="mansion_day"),
    # ---------------- the event ----------------
    dict(to=64, reason="scene change: at an event they run into Uvaish and his wife Reem",
         chars=["noorin_young", "uvaish_young", "aakif_young", "reem"], loc="event",
         visual="young Noorin walking beside Aakif (a clear arm's-length gap) stops short, her face pale and her eyes wide, one hand on her gentle pregnancy bump; across a round table Uvaish stands frozen with a glass of orange juice in his hand, staring at her in shock; beside him his wife Reem, about 22, elegant and calm; nobody touching",
         camera="medium wide, eye level, faces in the upper half, the white tablecloth as the lower third", amb="hall_crowd"),
    dict(to=68, reason="characters change: Noorin leaves; Aakif tells Reem and Uvaish she is his pregnant wife",
         chars=["aakif_young", "uvaish_young", "reem"], loc="event",
         visual="young Aakif smiling politely and talking to Reem (about 22) and Uvaish beside a round table, all three standing a respectful distance apart; Reem curious and friendly; Uvaish holding a glass of orange juice, listening with a tense, stunned face; far in the background the small figure of a young woman in a dusty-rose dress and cream hijab walking away across the hall",
         camera="medium three-shot, eye level", amb="hall_crowd"),
    dict(to=71, reason="focus on Uvaish: he asks how many months and sinks into calculation",
         chars=["uvaish_young", "aakif_young"], loc="event",
         visual="close medium shot of young Uvaish staring into the distance, calculating, jaw tight, brow furrowed, holding a glass of orange juice; young Aakif slightly out of focus at the edge of the frame, answering casually",
         camera="close medium shot, eye level", amb="hall_crowd"),
    dict(to=73, reason="Aakif tells how Noorin saved his life (same conversation)", reuse="beat_022",
         chars=["aakif_young", "uvaish_young", "reem"], loc="event", visual="(reuse of beat_022)", amb="hall_crowd"),
    dict(to=75, reason="action change: five months since the divorce — he sets down his juice and storms out",
         chars=["uvaish_young"], loc="event",
         visual="a half-full glass of orange juice just set down on a white tablecloth in the sharp foreground; in the background young Uvaish striding quickly away across the hall, his back turned, shoulders tense",
         camera="low table-level shot, the glass in the upper-middle of the frame, Uvaish beyond it", amb="hall_crowd"),
    # ---------------- the side room ----------------
    dict(to=78, reason="scene change: he confronts her in a nearby room — 'Whose child is that?'",
         chars=["uvaish_young", "noorin_young"], loc="side_room",
         visual="young Uvaish standing in front of the closed door, leaning forward, demanding, angry and hurt, one hand raised palm-up in a questioning gesture; young Noorin facing him at a clear arm's-length gap, startled and shocked, both arms wrapped protectively around her five-month pregnancy bump; nobody touching",
         camera="medium two-shot, eye level", amb="room_night", sens="violence",
         safe="the narration's grabbing her hand and pulling her into the room is not shown; they stand apart in the room"),
    dict(to=80, reason="focus on Uvaish: his eyes turn red and tears fall as he concludes she betrayed him",
         chars=["uvaish_young"], loc="side_room",
         visual="close-up of young Uvaish alone in the frame, eyes red and full of tears, a tear running down his cheek, anguish and wounded anger; behind him only the plain wall and the closed door of the empty room, no other people",
         camera="close-up, eye level", amb="room_night"),
    dict(to=83, reason="focus on Noorin: she stays silent, her eyes full of reproach and unanswered questions",
         chars=["noorin_young"], loc="side_room",
         visual="close-up of young Noorin alone in the frame, silent, lips pressed shut, her teary eyes looking just past the camera full of reproach and unspoken questions; behind her only the plain wall and the wall lamp, no other people in the frame",
         camera="close-up, eye level", amb="room_night"),
    dict(to=86, reason="action change: she tries to leave; he steps in front of her and blocks the door",
         chars=["uvaish_young", "noorin_young"], loc="side_room",
         visual="young Uvaish standing squarely in front of the closed door, blocking it, arms at his sides, his face torn between love and fury; young Noorin a clear arm's-length away, half turned towards the door, both arms around her pregnancy bump, frightened; nobody touching",
         camera="medium wide two-shot, eye level", amb="room_night"),
    dict(to=88, reason="return to Uvaish: his grief and anger overflow", reuse="beat_027",
         chars=["uvaish_young"], loc="side_room", visual="(reuse of beat_027)", amb="room_night"),
    dict(to=90, reason="return to Noorin: still his wife in her iddah, she could never tell him about the baby", reuse="beat_028",
         chars=["noorin_young"], loc="side_room", visual="(reuse of beat_028)", amb="room_night"),
    # ---------------- that night (never shown) ----------------
    dict(to=92, reason="that night's cruelty is never shown: a closed door in an empty corridor",
         loc="corridor",
         visual="a closed wooden door in an empty dim hotel corridor at night, a thin line of warm light under the door, the corridor carpet stretching towards it; no people",
         camera="wide, eye level, the door in the upper half, the empty carpet as the lower third", amb="hospital_night",
         sens="violence", safe="the night of the baby's loss is never depicted — only a closed door in an empty corridor (bible rules 1 and 8)"),
    dict(to=94, reason="symbolic detail: the innocent baby who never saw the light of the world",
         loc="night_window",
         visual="a dark hotel window at night, rain streaks running down the glass, blurred city lights beyond, a single wilted white flower lying on the plain windowsill; no people",
         camera="close medium shot, the window in the upper two-thirds, the windowsill as the lower third", amb="rain_night",
         sens="other", safe="the loss of the baby is shown only symbolically (rain on a window, a wilted flower)"),
    dict(to=96, reason="action change: she leaves the place, weak, one hand pressed to her side",
         chars=["noorin_young"], loc="corridor",
         visual="young Noorin walking slowly away down the empty dim hotel corridor, seen from a three-quarter back angle, one hand pressed to her side, her face pale and drained, no tears, shoulders slumped",
         camera="medium wide, eye level, from behind and to the side", amb="hospital_night",
         sens="violence", safe="no injury or blood shown (the narration's blood on her lips is omitted); only her pale face and her hand at her side (bible rule 8)"),
    dict(to=97, reason="character change: Aakif receives her short message",
         chars=["aakif_young"], loc="aakif_room",
         visual="young Aakif sitting at his desk under the lamp, looking down at the phone in his hand, the screen glowing with blurred unreadable shapes, his face stunned and worried",
         camera="medium close-up, eye level", amb="room_night"),
    # ---------------- the beach (rule 9) ----------------
    dict(to=98, reason="scene and time change: alone on the shore facing huge waves",
         chars=["noorin_young"], loc="big_beach", transition="black",
         visual="young Noorin standing alone on wide dry sand well back from the waterline, seen from behind and slightly to the side, facing huge waves breaking far out under dark clouds at dusk, her loose dress and cream hijab moving in the wind; the water far from her feet",
         camera="wide shot from behind, the horizon and clouds in the upper half, the wide dry sand as the lower third", amb="beach_dusk",
         sens="other", safe="she stands on dry sand far from the water (bible rule 9)"),
    dict(to=100, reason="action change: the doctor's words echo; she presses her hands over her ears",
         chars=["noorin_young"], loc="beach_grief",
         visual="medium close-up of young Noorin standing on the beach, eyes shut tight, both palms raised to the sides of her head over her cream hijab as if shutting out a sound, overwhelmed, the wind moving the fabric, a cloudy dusk sky and palms behind her",
         camera="close-up, eye level", amb="beach_dusk", sens="other",
         safe="the doctor's words are only heard; the loss is shown as her grief, nothing medical shown"),
    dict(to=102, reason="return to the wide shore: lonely, abandoned by family, she looks at the endless sea", reuse="beat_036",
         chars=["noorin_young"], loc="big_beach", visual="(reuse of beat_036)", amb="beach_dusk",
         sens="other", safe="she stays on dry sand far from the water (bible rule 9)"),
    dict(to=104, reason="turning point: her conscience wakes; light breaks through the clouds",
         chars=["noorin_young"], loc="beach_light",
         visual="young Noorin standing still on the dry sand well back from the water, eyes closed, face lifted; a shaft of golden light breaks through the dark storm clouds and falls softly on her; the waves far away behind her",
         camera="medium wide, slightly low angle, light rays in the upper part of the frame", amb="beach_dusk",
         sens="other", safe="the step towards the sea is not shown; the turning point is light breaking through the clouds (bible rule 9)"),
    # ---------------- the conscience monologue (symbolic) ----------------
    dict(to=106, reason="symbolic image for the conscience: the blind and the disabled who face life with patience",
         loc="symbol_lane", transition="dissolve",
         visual="an elderly Maldivian man in a white shirt and sarong with a white cane walking calmly and with dignity along the sunlit lane, beside him a young man in a wheelchair smiling peacefully; both seen from a gentle distance",
         camera="medium wide, eye level, figures in the upper half, the white sand lane as the lower third", amb="village_day"),
    dict(to=108, reason="symbolic image: live for a higher purpose, reach out your hand to those who need help",
         loc="symbol_hands", transition="dissolve",
         visual="close-up of a young woman's hand in a long dusty-rose sleeve reaching down to take the outstretched wrinkled hand of an elderly woman in a long sleeve, helping her up, warm light between their hands",
         camera="close-up of the two hands in the upper-middle of the frame, soft blurred background below", amb="garden_day"),
    dict(to=110, reason="symbolic image: serve your religion and your nation",
         loc="dawn", transition="dissolve",
         visual="soft golden rays of dawn breaking through blue haze over a calm lagoon, a simple white mosque minaret and coconut palms in silhouette against the brightening sky, no people",
         camera="wide shot, sky and minaret in the upper two-thirds, the still lagoon as a calm lower third", amb="dawn_exterior",
         sens="other", safe="religious exhortation shown only as a dawn minaret; no religious text rendered"),
    dict(to=111, reason="closing: she breathes deeply, closes her eyes and turns away from the sea",
         chars=["noorin_young"], loc="beach_light", transition="dissolve",
         visual="young Noorin has turned her back to the sea and stands on the dry sand facing the palms, taking a deep breath with her eyes closed, a calm, exhausted peace on her face, golden light through the clouds behind her",
         camera="medium shot, eye level, face in the upper half", amb="beach_dusk",
         sens="other", safe="the turning point is shown as her turning away from the sea (bible rule 9)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Uvaish came back to Noorin once again. Tears were gathering in Noorin's eyes. Giving herself courage,",
   [("sob_breath", "ކަރުނަ", -24)])
sh(2, "she had been facing the world with great strength. After the night Uvaish speaks of, Noorin had sworn never to cry again.")
sh(3, "She did not know who it was she met that night, or what kind of person he was. Still, the one thing she knew was that the man had not taken advantage of her helplessness that night.")
sh(4, "So she had pictured an image of that man in her mind, and with all her heart she kept feeling grateful to him.")
sh(5, "But Noorin had never imagined that person would be so young, handsome and perfect. Tears rolled down Noorin's cheeks.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(6, "She had not stolen anything. How could she accept the accusation this young man had put on her? \"I didn't tell you to cry.\"")
sh(7, "Seeing the tears falling from Noorin's eyes, Uvaish said softly. \"I said I came to find the thing Noorin stole.")
sh(8, "How can I live without my heart? I came to find my heart.\" Noorin stared, more astonished by Uvaish's words than before.")
sh(9, "\"I want to marry Noorin. As my wife, Noorin will be under my care every single day.")
sh(10, "Nothing will ever harm Noorin,\" Uvaish said. Hearing his words, Noorin stood staring in disbelief with her tear-filled eyes wide open.",
   [("gasp", "ބޮޑުކޮށްލައިގެން", -22)], hum=True)
sh(11, "A flood of questions rose in Noorin's heart and mind at once. Noorin was sure a young man like Uvaish could not be without a girl to marry.")
sh(12, "In her eyes Uvaish was a perfect young man. He had good looks, youth and wealth.")
sh(13, "The sentence Naahidh had said was still in her memory: \"The resort owner!\" Now she was sure it was Uvaish.")
sh(14, "Would a man so well off really have no girl to marry? \"Why me?\" Noorin asked.")
sh(15, "Uvaish smiled. He knew that question would be aimed at him. \"Must we say everything right now? Then there'd be nothing left to talk about later.\"")
sh(16, "At that moment a playful smile sat on Uvaish's lips. \"But...\" Noorin stopped what she was about to say because of the question Uvaish asked.")
sh(17, "Once again he gave Noorin no chance to speak. \"Are you in a relationship with someone?\" Uvaish asked. \"There's no such relationship.\"")
sh(18, "Noorin said softly. \"Then what's the problem?\" Uvaish asked. Noorin stood there, not knowing how to answer.")
sh(19, "Just then she found herself looking at Uvaish's face. The kindness in his eyes, the youth of his face, that emotional gaze — Noorin's heart grew weak.")
sh(20, "Could it be her fortune to have a man with such a kind, sincere heart? Looking at the tears in her eyes, Uvaish spoke very softly.")
sh(21, "\"I will always give that soul love and care. I will give that heart strength and bring it endless joy. Noorin is the meaning of my life.")
sh(22, "Believe it. I want Noorin to love me the way I love her. Believe it or not,")
sh(23, "yours is the face that has taken the sleep from my eyes. I spent two months waiting for you; if I hadn't found you here, I don't know what I'd have done.\"")
sh(24, "His words filled Noorin's heart. For his kind nature and the sincerity in every word he spoke, Noorin's heart was filled with gratitude.")
sh(25, "Looking at his face, Noorin said with courage: \"My heart is afraid to love. I don't want to refuse your proposal, but...\"")
sh(26, "Noorin tried to speak. But at that moment Uvaish stopped her words, gently silencing her.",
   [("breath", "ހުއްޓުވައިލަމުން", -22)], hum=True)
sh(27, "\"This heart isn't used to hearing 'no'; this heart belongs to Noorin alone. Don't refuse, or this heart may break into pieces.\"")
sh(28, "Uvaish said with great emotion. Noorin could not bring herself to refuse Uvaish's wish. He was a good-natured person.")
sh(29, "He had come all that way to find Noorin because he loved her. Isn't that proof enough? Even so,")
sh(30, "an unease and a fear she couldn't explain surrounded her heart. Who can know what the future holds?")
sh(31, "For now, the only way was to trust Uvaish completely and become a part of his life. Their love grew stronger and stronger,")
sh(32, "and before many days had passed the two were married. And Noorin stepped into her new life.")
sh(33, "In the first two weeks of their marriage Uvaish filled Noorin's heart with joy, with colourful promises that they would never part.")
sh(34, "Yet that happiness lasted only those two weeks. What lay behind the sudden change in Uvaish's mood,")
sh(35, "and what compulsion was behind it, she never knew. As the painful words of divorce were heard, Noorin's whole world seemed to collapse.",
   [("heartbeat", "ބިންދައިގެން", -20)], hum=True)
sh(36, "Tears fell from her eyes without her permission. \"I will come back. Stay in this house, Noorin. I have to go today.\"",
   [("sob_breath", "ކަރުނަ", -22)])
sh(37, "That single sentence was all that left Uvaish's lips. Every second spent in that house waiting for Uvaish became an unbearable pain for Noorin.")
sh(38, "The memories of the loving moments they had spent together broke her heart into pieces. In the end,")
sh(39, "with the noble intention of giving the tiny baby in her womb a bright future, Noorin decided to leave that house and move to her own island. However,")
sh(40, "once she reached the island, because of her stepmother's scheming wickedness, shameful stories about Noorin's honour spread.")
sh(41, "She had to face the islanders' mockery and taunts. As she walked along the street, besides people's scorn, they threw rubbish and all sorts of things at her.",
   [("soft_thud", "އުކައި", -24)])
sh(42, "Was this the punishment she got for loving? It was the bitter result of lies people spread without seeking the truth. As it was a pleasant evening hour,")
sh(43, "Noorin went out to the beach to find even a little comfort for her heart. Once night fell, she would become the prey of people's endless harm and mockery.",
   [("footsteps_sand", "ނިކުމެލިއެވެ", -22)])
sh(44, "She kept fighting tirelessly to escape all that cruelty. Such is the way of the world. When people see someone helpless,")
sh(45, "there is no limit to how they test that person's patience and torment them. Her state was like that of a brave warrior fighting with her life to defend her own honour and dignity.")
sh(46, "That there was no one else to help her was a bitter truth she had to accept. Though the human heart is made with kindness on one side,")
sh(47, "if it becomes a slave to Shaitan's whisperings it becomes destruction and danger. As Noorin sat lost in thought,")
sh(48, "a piece of rubbish suddenly flew at her, and the pain brought tears to her eyes. Yet without a thought for the harm to her own body,",
   [("soft_thud", "ޖެހުނު", -22), ("gasp", "ތަދުގެ", -20)], hum=True)
sh(49, "Noorin hurried to shield and protect the innocent baby in her womb,",
   [("cloth_rustle", "ނިވާކޮށް", -24)])
sh(50, "for fear the attacks being thrown might do even the slightest harm to that tiny soul. Some good deeds done in life")
sh(51, "are noble deeds whose value is never lost. Aakif was a young man desperately wanting to repay a kindness he had received from Noorin.")
sh(52, "The two first met on the day Noorin first came to Malé, on the stairs of her mother's building. Because the lift was broken,")
sh(53, "as Noorin was climbing the stairs carrying her bag, a Ventolin inhaler fell from above and landed at her feet. As she picked it up and climbed on,",
   [("footsteps_pavement", "އަރަމުން", -22), ("soft_thud", "ވެއްޓުނެވެ", -24)])
sh(54, "the sound of someone gasping for breath and calling for help reached Noorin's ears. Setting down the bag in her hand, Noorin hurried to help that person.",
   [("breath_heavy", "ނޭވާ", -18), ("footsteps_pavement", "އަވަސްވެގަތެވެ", -22)], hum=True)
sh(55, "After that day Aakif was always waiting for a chance to do something good for Noorin. Aakif, who belonged to a respected family in Malé,")
sh(56, "rescued Noorin from the hard, troubled situations she faced for that reason. \"How could I ever forget your kindness, Noorin?")
sh(57, "If Noorin hadn't helped me that day, I'd be under the ground today. When I was struggling, unable to breathe, you were the one who brought the inhaler to me.",
   [("breath_heavy", "ނޭވާ", -22)])
sh(58, "Today is the time for me to help Noorin.\" Aakif said after hearing Noorin's story.")
sh(59, "And Aakif decided to make Noorin a part of his life. Though Noorin openly objected,")
sh(60, "Aakif resolved to marry Noorin, to protect her from people's eyes and give her a happy life. Aakif")
sh(61, "brought Noorin to Malé and kept her in his home. And in front of people he presented her as his wife.")
sh(62, "He took Noorin to various invitations with great joy and contentment. The world has become a small place, and the Maldives especially is a very small place.")
sh(63, "By coincidence, today Noorin had to come face to face with Uvaish and his wife Reem. On seeing Uvaish, Noorin's heartbeat quickened.",
   [("heartbeat", "ތެޅުން", -20)], hum=True)
sh(64, "The same happened to Uvaish on seeing Noorin. Not wanting to stand in front of Uvaish,")
sh(65, "Noorin said she needed the washroom and went away from there. \"Excuse us! My wife is expecting, so she has to rush to the washroom now and then.",
   [("footsteps_pavement", "ދިޔައެވެ", -24)])
sh(66, "Reem will know that too when she's expecting.\" Aakif said to Reem with a smile. \"When did you get married?\" Reem asked.")
sh(67, "Since that was the very question Uvaish wanted to ask, he too listened with great interest. \"Never mind when we got married, come on!")
sh(68, "I don't question you about that, do I? All anyone needs to know is that she is my wife. And now she is expecting my child.\"")
sh(69, "Aakif answered with a smile. He did not want to reveal the truth to the world. He himself never asked Noorin anything either.")
sh(70, "He never asked who had ruined Noorin's life. \"How many months along is she now?\" Uvaish asked. There was something he wanted to make sure of.")
sh(71, "\"I think about four or five months.\" Aakif said, thinking. Uvaish sank into deep thought.",
   [("heartbeat", "ގެނބިގެން", -22)])
sh(72, "And he kept asking questions to learn the details of how Aakif and Noorin met. As Aakif told it, the two first met when his life was in danger and Noorin saved it.")
sh(73, "And Aakif said he fell in love with Noorin after that incident. Aakif's words made Uvaish's heart beat faster,",
   [("heartbeat", "ތެޅުން", -20)])
sh(74, "and his heart longed to find out the truth of the story. Having got all the information he needed, Uvaish thought.")
sh(75, "It was now five months since he had divorced Noorin. Putting the juice glass in his hand down on the table, Uvaish walked out of there with fast steps.",
   [("cup_clatter", "ބެހެއްޓުމަށްފަހު", -18), ("footsteps_pavement", "ހިނގުމެއްގައި", -20)])
sh(76, "As Noorin came out of the washroom and walked on, Uvaish came and took her into a nearby room.",
   [("door_close", "ވެއްދިއެވެ", -18)])
sh(77, "Noorin looked at Uvaish's face in surprise and shock. \"Whose child is that in your womb?\" Uvaish demanded, raising his voice.",
   [("gasp", "ސިހުމާއެކު", -20)])
sh(78, "But Noorin gave no answer and stood in silence. \"Didn't I tell you I'd come back, to wait for me!")
sh(79, "But as soon as I divorced you, you went and took up with Aakif?\" Uvaish's eyes turned red. \"That means even before, you two...\"")
sh(80, "Tears began to roll down his cheeks. Uvaish concluded on his own that Noorin had betrayed him.",
   [("sob_breath", "ކަރުނަތައް", -22)], hum=True)
sh(81, "Noorin answered none of the questions Uvaish kept asking. She stood staring into his eyes, full of countless grievances and questions.")
sh(82, "When had she ever betrayed him? In truth she was still Uvaish's right. Wasn't it Uvaish himself who had betrayed?")
sh(83, "Even so, Uvaish gave her no chance to say any of it. Noorin started to walk away.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22)])
sh(84, "At that moment Uvaish suddenly stepped in front of her and blocked her way. Five months pregnant, Noorin struggled to get away from Uvaish.",
   [("breath_heavy", "މިންޖުވުމަށެވެ", -22)])
sh(85, "But Uvaish's stubbornness and emotions were not the kind that would let Noorin go. He still loved Noorin beyond measure.")
sh(86, "His longing for Noorin was still alive in his heart. He wanted to tell Noorin about the forced situation he faced, the sacrifice he made for his family, and the promise made to his grandfather.")
sh(87, "Yet, believing that Noorin had betrayed him, his grief and anger boiled over.")
sh(88, "Whatever happened, he would never let Noorin become someone else's. Why didn't Uvaish know that the bond between them was not broken?")
sh(89, "Even though he had spoken the words of divorce, during the iddah period Noorin was still his wife.")
sh(90, "Noorin had tried many times to tell him she was carrying his child. But because of Uvaish's merciless actions, there was never a way to reveal it.")
sh(91, "Seeing Noorin after five months, Uvaish seemed to lose his reason. That painful moment of that night became the moment Noorin's love and respect for Uvaish shattered forever.",
   [("heartbeat", "ހިތްދަތި", -22)], hum=True)
sh(92, "The cruel act Uvaish committed without any mercy is something Noorin could never erase from her heart.")
sh(93, "That innocent baby had to close its eyes forever before ever seeing the light of the world. When she opened her eyes, Noorin saw Uvaish nearby.",
   hum=True)
sh(94, "The tears that had flowed in every sorrow had dried up this time. Not a single tear could fall from her eyes.")
sh(95, "Bearing the severe pain in her belly, she rose from the carpet. After wiping her lips,",
   [("breath_heavy", "ވޭނަށް", -22)])
sh(96, "with one hand pressed to her side, she left the place, exhausted. \"Sorry, Aakif... I can no longer marry you.\"",
   [("footsteps_pavement", "ނިކުމެގެން", -24)])
sh(97, "That short message from Noorin was all Aakif received. Aakif did not know what had happened to Noorin or where she had gone.",
   [("phone_buzz", "މެސެޖެވެ", -16)])
sh(98, "Noorin stood on the shore, staring at the huge rising waves. The doctor's words kept ringing in her ears.",
   [("wave_crash", "ރާޅުތަކަށް", -16)])
sh(99, "\"Because of the forced relation, the baby has been lost... we will have to clear the womb.\" Closing her tear-filled eyes,",
   [("heartbeat", "ބީވެފައި", -20)], hum=True)
sh(100, "as if she did not want to hear that voice, Noorin pressed her hands hard over both her ears. Opening her eyes again, she gazed at the boundless sea.",
   [("wave_crash", "ކަނޑަށް", -18)])
sh(101, "Losing the baby in her womb was a grief greater than her heart could bear. Her mother and her whole family had abandoned her, alone.")
sh(102, "What meaning was there now in living in this world? Even if she threw herself into this endless sea, there was not a single person who would grieve.",
   [("wave_crash", "ކަނޑަށް", -18)])
sh(103, "At the moment she took a step forward, her conscience awoke and the voice of her heart called out: \"Will you give victory to the world's oppressors?",
   [("heartbeat", "ފިޔަވަޅެއް", -20)], hum=True)
sh(104, "Will you fulfil their evil purpose? Taking one's own life is a great sin before Allah.")
sh(105, "Even the blind, who cannot see the light of the world, face life with patience. Think of those whose hands and feet are disabled,")
sh(106, "and the helpless who cannot hear or speak. Feel the effect it would have on their hearts.")
sh(107, "You are a human being blessed with every limb whole. Don't be so weak. Instead of taking your own life,")
sh(108, "live for a far nobler and more useful purpose. Reach out your hand to those who ask for help.")
sh(109, "How many people in society bear hardships like yours? Give them courage,")
sh(110, "work to make them people who benefit society. Serve your religion and your nation.\"")
sh(111, "Releasing a deep breath, Noorin closed her tear-filled eyes. Had her sleeping conscience not woken that day, today she would be a loser who had lost both this world and the next.",
   [("breath", "ނޭވާއެއް", -18)], hum=True)
SHOTS = S

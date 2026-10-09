"""Beat/shot plan for Mamma episode 460 (used by plan_beats.py).
Reysham visits Shahula in the afternoon; night: Shahula and baby Zidhaan; Aamir comes home; 11 p.m. confrontation."""

HOUSE = ("the main bedroom of Azeeza's older two-storey Malé townhouse, now Shahula and Aamir's room: a wooden double bed "
         "with a pale bedspread against the wall, a small white baby cot beside it, a wooden wardrobe, a small bedside table "
         "with a lamp, a wooden window with a sheer curtain, plain cream walls, a tiled floor")
LOC = {
    "bedroom_afternoon": HOUSE + ", in the afternoon",
    "front_hall": ("the entrance of the same Malé townhouse: the wide front hall (fendaa) just inside the open main wooden "
                   "double door, a tiled floor, a small console table by the wall with a framed flower picture, beyond the "
                   "doorway a glimpse of the tiled front yard with potted plants in the afternoon sun"),
    "sitting_room": ("the sitting room (bodu fendaa) of the same Malé townhouse: a grey fabric sofa facing a matching grey "
                     "armchair-sofa across a low wooden coffee table, a TV on a low cabinet, a small side table, framed flower "
                     "pictures on cream walls, a window with sheer curtains, a doorway to the kitchen and a doorway to the "
                     "corridor leading to the bedroom"),
    "memory_bedroom": HOUSE + ", seen in a memory about a year earlier, at night",
    "bedroom_evening": HOUSE + ", in the evening after dark, the curtain drawn",
    "bedroom_late": HOUSE + ", late at night (about 11 p.m.), almost dark",
}
MOOD = {
    "bedroom_afternoon": "quiet afternoon, soft muted daylight through the sheer curtain, slightly cool and still, a gentle domestic calm",
    "front_hall": "afternoon, bright daylight from the open front door behind the visitor, the hall itself a little dim and cool, an uneasy stillness",
    "sitting_room": "afternoon, soft cool daylight from the window, muted colours, tense polite stillness, a cold undercurrent",
    "memory_bedroom": "a memory: soft warm hazy glow, slightly desaturated and dreamlike, a soft vignette, lonely distance",
    "bedroom_evening": "night, Malé home after the marriage: dim, cold and shadowy, a single warm bedside lamp, deep blue shadows, melancholic and lonely",
    "bedroom_late": "late night, a dark bedroom lit only by one dim amber night lamp, deep blue-black shadows, cold, tense and heartbreaking",
}

LOW = "faces in the upper two-thirds, a calm uncluttered lower third"
GAP = "a clear arm's-length gap between them, not touching"
BANG = "two plain shining gold bangles on her wrist"
BABY = ("baby Zidhaan, a healthy chubby baby boy of a few months in a pale-blue long-sleeved baby suit, wrapped in a pale-blue "
        "cotton blanket")
SH = "Shahula in her loose long-sleeved ankle-length dusty-rose house dress and cream hijab fully covering her hair and neck"
SH_MINT = ("Shahula freshly dressed (reference used for her face only; wearing a clean pale-mint long-sleeved ankle-length dress "
           "and a white hijab fully covering her hair and neck, NOT the dusty-rose dress and NOT the cream hijab)")
MINT_X = ("wearing a PALE MINT-GREEN long-sleeved ankle-length dress and a WHITE hijab - the dress is pale mint green, "
          "NOT pink, NOT dusty-rose, NOT rose")
RE = "Reysham in her lilac long-sleeved ankle-length abaya and silver-grey hijab fully covering her hair and neck, neat makeup"
A_OFFICE = ("Aamir just home from work (reference used for his face only; wearing a light-blue long-sleeved shirt and dark "
            "trousers, NOT the white shirt)")
A_HOME = ("Aamir (reference used for his face only; wearing a plain dark-grey long-sleeved t-shirt and long dark track "
          "trousers, NOT the white shirt)")
SAFE_DV = "violence never shown (bible rule 1): no raised hand, no contact, no marks on her face; only reaction, shadow and aftermath"

BEATS = [
    # ---------------- AFTERNOON: the visitor
    dict(to=1, reason="episode opening: afternoon in the bedroom, Shahula lays the sleeping baby down at a call of salaam",
         chars=["shahula"], loc="bedroom_afternoon",
         visual=f"{SH}, {BANG}, bending over the wooden bed gently laying down {BABY}, who is fast asleep; she glances "
                f"over her shoulder toward the open bedroom door, alert, as if someone has called from outside",
         camera=f"medium shot, eye level, {LOW} (the pale bedspread)", amb="room_day"),
    dict(to=4, reason="scene/character change: a young stranger stands inside the main door holding a paper gift bag",
         chars=["reysham", "shahula"], loc="front_hall",
         visual=f"{RE}, standing just inside the open main door of the hall, holding out a plain paper gift bag with no "
                f"writing on it toward Shahula with a light, knowing smile; {SH} standing facing her a few steps away, "
                f"looking at the bag with puzzled surprise; the bright doorway behind the visitor",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (the tiled floor)", amb="home_day"),
    dict(to=7, reason="emotional turning point: 'I'm Reysham' - Shahula frozen, she knows the name",
         chars=["shahula"], loc="front_hall",
         visual=f"close-up of {SH}, frozen, her large dark eyes wide with shock and dawning recognition, lips slightly "
                f"parted, one hand resting at her collar; the bright blurred doorway behind her is empty"
                f"; she is the only person in the image, no one else anywhere in the frame",
         camera=f"close-up, eye level, {LOW} (soft-focus dim hall)", amb="home_day", hum=True),
    dict(to=9, reason="focus change: Reysham's fresh youth, in which Shahula sees her own younger self",
         chars=["reysham"], loc="front_hall",
         visual=f"medium close-up of {RE}, fresh, young and polished, a faint self-assured smile, sharp knowing eyes "
                f"looking straight ahead, the paper gift bag in her hand; soft daylight from the doorway on her face",
         camera=f"medium close-up, eye level, {LOW} (soft-focus background)", amb="home_day"),
    dict(to=11, reason="focus change: Shahula feels worn out after the birth, comparing herself (body never shown)",
         chars=["shahula"], loc="front_hall",
         visual=f"medium close-up of {SH}, tired and weary, faint shadows under her eyes, glancing at her own face in a "
                f"small round mirror on the hall wall, only her face reflected, a sad self-conscious look; loose dress, "
                f"only her face and shoulders in the frame",
         camera=f"medium close-up, eye level, {LOW} (the plain console table top)", amb="home_day",
         sens="other", safe="her post-birth body is never shown or hinted (bible rule 3): only her tired face in a small mirror"),
    dict(to=12, reason="back to Reysham, 'like a fresh rose on its branch'; then 'Sit!'", reuse="beat_004",
         chars=["reysham"], loc="front_hall", visual="reuse of beat_004", amb="home_day"),
    dict(to=14, reason="scene/character change: in the sitting room Shahula calls the helper Suneetha for a cold drink",
         chars=["shahula", "suneetha", "reysham"], loc="sitting_room",
         visual=f"{SH} standing beside the grey armchair-sofa, turned toward the kitchen doorway, calmly asking for something; "
                f"Suneetha (beige dress, brown headscarf) appearing in the kitchen doorway, nodding; {RE} seated on the grey "
                f"sofa in the background with the paper gift bag beside her, looking around the room; every person appears only once",
         camera=f"medium wide shot, eye level, {LOW} (the coffee table top and tiled floor)", amb="home_day"),
    dict(to=18, reason="action change: Shahula sits opposite Reysham and asks how she knows her",
         chars=["shahula", "reysham"], loc="sitting_room",
         visual=f"two women seated facing each other across the low coffee table: {SH}, {BANG}, sitting upright on the "
                f"armchair-sofa with her hands folded in her lap, calm and direct, asking a question; {RE} on the grey sofa "
                f"opposite, slightly taken aback, eyebrows lifted; seen from the side",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (the empty coffee table top)", amb="home_day"),
    dict(to=22, reason="focus change: Reysham speaks without shame - 'I know you through Aamir... he's a man'",
         chars=["reysham"], loc="sitting_room",
         visual=f"medium shot of {RE}, leaning back comfortably on the grey sofa, one hand lightly raised as she talks, a cool "
                f"confident half-smile, looking across at someone off-frame with mocking eyes; she is the only person in the image, no one else in the "
                f"foreground or at the edges of the frame",
         camera=f"medium shot, eye level, {LOW} (sofa cushions in soft shadow)", amb="home_day",
         sens="other", safe="the affair is shown only as Reysham's mocking expression; modest and seated (bible rule 9)"),
    dict(to=25, reason="focus change: Shahula's speechless astonishment, then a deep breath to steady herself",
         chars=["shahula"], loc="sitting_room",
         visual=f"close-up of {SH}, stunned by what she hears, eyes wide and hurt, lips pressed together, then drawing a "
                f"slow deep breath to compose herself; the soft grey sofa blurred behind",
         camera=f"close-up, eye level, {LOW} (soft-focus background)", amb="home_day"),
    dict(to=28, reason="action change: Shahula answers firmly and with dignity",
         chars=["shahula"], loc="sitting_room",
         visual=f"medium shot of {SH}, {BANG}, sitting very upright on the armchair-sofa, chin raised, speaking calmly and "
                f"firmly with quiet dignity, her hands still in her lap, steady eyes looking across the room toward someone "
                f"off-frame; she is the only person in the image, no one else in the foreground or anywhere in the frame",
         camera=f"medium shot, slightly low angle, {LOW} (the coffee table edge)", amb="home_day"),
    dict(to=32, reason="back to Reysham, eyebrow raised: 'three years in the office... you hold him with a child'",
         reuse="beat_009", chars=["reysham"], loc="sitting_room", visual="reuse of beat_009", amb="home_day"),
    # ---------------- MEMORY: the first pregnancy
    dict(to=35, reason="flashback: the days of her first pregnancy, Aamir's coldness and distance",
         chars=["shahula", "aamir"], loc="memory_bedroom",
         visual=f"a memory: {SH}, with a modest rounded bump under the loose dress, sitting alone on a chair by the bed with one "
                f"hand resting on her belly, looking sadly across the room; {A_HOME} standing far away by the window with "
                f"his back half turned to her, looking down at the glow of his phone (screen not visible), distant and cold; "
                f"the whole width of the room between them, not touching",
         camera=f"wide shot, eye level, {LOW} (the dim tiled floor)", amb="memory", transition="dissolve",
         sens="intimacy", safe="the murmured name in intimate moments is shown only as emotional distance across a room (bible rule 5)"),
    # ---------------- BACK IN THE SITTING ROOM
    dict(to=38, reason="back to the present: Reysham leans in - 'whenever you fight he comes to me'",
         chars=["reysham", "shahula"], loc="sitting_room",
         visual=f"over-the-shoulder view from behind {SH} seated stiffly on the armchair-sofa (only her cream hijab and shoulder "
                f"in the soft-focus foreground), toward {RE} on the grey sofa across the coffee table, leaning forward with a "
                f"sly confiding smile as she talks",
         camera=f"over-the-shoulder medium shot, eye level, {LOW} (the coffee table top)", amb="home_day",
         transition="dissolve"),
    dict(to=41, reason="action change: Reysham's mocking laugh - 'his mother's burden'",
         chars=["reysham"], loc="sitting_room",
         visual=f"medium close-up of {RE} on the grey sofa letting out a mocking laugh, head tilted slightly back, fingertips "
                f"near her lips, eyes narrowed with scorn",
         camera=f"medium close-up, eye level, {LOW} (soft-focus sofa)", amb="home_day",
         sens="other", safe="mockery shown by expression only"),
    dict(to=44, reason="focus change: Shahula sits silent, swallowing her humiliation, choosing reason over anger",
         chars=["shahula"], loc="sitting_room",
         visual=f"{SH}, {BANG}, sitting still and silent on the armchair-sofa, eyes glistening but no tears falling, her "
                f"hands tightly clasped in her lap, face composed with great effort, cool window light on one side of her face",
         camera=f"medium close-up, eye level, {LOW} (her clasped hands on the dress fabric)", amb="home_day", hum=True),
    dict(to=47, reason="action/character change: Reysham rises leaving the gift; Suneetha serves masala tea and short-eats",
         chars=["reysham", "suneetha"], loc="sitting_room",
         visual=f"{RE} standing up beside the grey sofa, having set the plain paper gift bag on the side table, smiling a "
                f"sweet, poisonous smile; Suneetha (beige dress, brown headscarf) bending to place a tray with cups of milky "
                f"masala tea and a plate of small fried Maldivian short-eats on the low coffee table",
         camera=f"medium wide shot, eye level, {LOW} (the coffee table with the tray)", amb="home_day"),
    dict(to=49, reason="action change: Shahula stands too; the baby cries and Suneetha runs to the bedroom",
         chars=["shahula", "reysham", "suneetha"], loc="sitting_room",
         visual=f"{SH} and {RE} both standing, facing each other across the coffee table with the tea tray, a clear distance "
                f"between them, Shahula silent and restrained, Reysham smug; in the background Suneetha (beige dress, brown "
                f"headscarf) hurrying through the corridor doorway toward the bedroom; every person appears only once",
         camera=f"medium wide shot, eye level, {LOW} (the coffee table with the tray)", amb="home_day"),
    dict(to=52, reason="focus change: Reysham standing, scornful advice - 'move to another room'",
         chars=["reysham"], loc="sitting_room",
         visual=f"medium shot of {RE} standing with her arms folded, chin lifted, a condescending, scornful smile, looking "
                f"down at someone off-frame; she is the only person in the image, no one else in the foreground or at the "
                f"edges of the frame",
         camera=f"medium shot, slightly low angle, {LOW} (soft-focus room behind)", amb="home_day"),
    dict(to=56, reason="focus change: Shahula's firm reply - 'I have as much say in this house as Aamir'",
         chars=["shahula"], loc="sitting_room",
         visual=f"close-up of {SH} standing, holding back her anger, jaw set, eyes steady and burning, speaking with calm "
                f"firm authority; she is the only person in the image, the sitting room behind her empty, no other man or "
                f"woman anywhere in the frame",
         camera=f"close-up, eye level, {LOW} (soft-focus background)", amb="home_day"),
    dict(to=59, reason="back to Reysham shaking her head with a mocking smile", reuse="beat_019",
         chars=["reysham"], loc="sitting_room", visual="reuse of beat_019", amb="home_day",
         sens="other", safe="the narration about her wet chest and the smell of milk is never shown (bible rule 4); only Reysham's look"),
    dict(to=60, reason="action change: Reysham walks out, the front door slams",
         chars=["reysham", "shahula"], loc="front_hall",
         visual=f"{RE} seen from behind walking out through the open main door into the bright afternoon yard, the door "
                f"swinging shut behind her; {SH} standing alone farther back in the dim hall, watching",
         camera=f"medium wide shot from inside the hall, eye level, {LOW} (the tiled floor)", amb="home_day"),
    dict(to=65, reason="action change: alone, Shahula holds her head, the world spinning; tears finally flow",
         chars=["shahula"], loc="front_hall",
         visual=f"{SH}, {BANG}, alone in the dim hall, leaning against the wall, holding her head with both hands, eyes "
                f"squeezed shut, tears on her cheeks, shoulders bowed with exhaustion and heartbreak",
         camera=f"medium shot, eye level, {LOW} (the tiled floor in soft shadow)", amb="home_day", hum=True),
    dict(to=66, reason="action change: with sudden resolve she flings Reysham's gift bag away",
         chars=["shahula"], loc="sitting_room",
         visual=f"{SH} standing by the sofa, her arm just swung forward after throwing, jaw clenched with anger; the plain "
                f"paper gift bag tumbling across the tiled floor, a small boxed baby bottle sliding out of it",
         camera=f"medium wide shot, eye level, {LOW} (the tiled floor with the tumbling bag)", amb="home_day"),
    # ---------------- NIGHT: Shahula and Zidhaan
    dict(to=71, reason="time jump: night falls; Shahula rocks the baby in her lap, lost in thought",
         chars=["shahula"], loc="bedroom_evening",
         visual=f"{SH} sitting on the edge of the bed under the single lamp, {BABY} lying in her lap; she rocks him gently, "
                f"her gaze fixed blankly on one spot, lost in painful thoughts",
         camera=f"medium shot, eye level, {LOW} (the bedspread in shadow)", amb="room_night", transition="black"),
    dict(to=73, reason="focus change: the baby waving his arms and legs, smiling a gummy smile",
         chars=[], loc="bedroom_evening",
         visual=f"close-up of {BABY} lying in his mother's lap on the dusty-rose fabric of her dress, wide awake, waving his "
                f"tiny arms and legs, smiling a wide toothless gummy smile up at her, lit by warm lamp light",
         camera=f"close-up from above, {LOW} (soft fabric folds)", amb="room_night"),
    dict(to=76, reason="action change: she lifts the baby to her shoulder, her tears fall, the baby cries with her",
         chars=["shahula"], loc="bedroom_evening",
         visual=f"{SH} sitting on the bed holding {BABY} upright against her shoulder, her cheek resting on his little head, "
                f"eyes closed, tears running down her cheeks; the baby's small face scrunched with a little open mouth",
         camera=f"medium close-up, eye level, {LOW} (the bedspread in lamp shadow)", amb="room_night", hum=True),
    # ---------------- AAMIR COMES HOME
    dict(to=79, reason="character/time change: Aamir comes home; Shahula, freshly dressed, shakes the baby bottle",
         chars=["shahula", "aamir"], loc="bedroom_evening",
         visual=f"{SH_MINT}, {BANG}, sitting on the edge of the bed calmly shaking a baby bottle of milk in her hand; "
                f"{A_OFFICE} standing just inside the bedroom doorway, surprised, eyebrows raised, looking at the bottle; "
                f"the empty baby cot by the bed; {GAP}",
         camera=f"medium wide shot, eye level, {LOW} (the tiled floor and bedspread)", amb="room_night"),
    dict(to=81, reason="focus change: Shahula's cold smile - 'a gift your office girl brought for Zidhaan'",
         chars=["shahula"], loc="bedroom_evening",
         visual=f"close-up of {SH_MINT}, a cold, faintly mocking smile on her lips, eyes hard and hurt, the baby bottle "
                f"set on the bedside table beside her",
         camera=f"close-up, eye level, {LOW} (the bedside table top)", amb="room_night"),
    dict(to=84, reason="action change: she leaves; Aamir alone stares at the bottle, puzzled",
         chars=["aamir"], loc="bedroom_evening",
         visual=f"{A_OFFICE} standing alone by the bedside table, frowning down at a baby bottle standing on it, puzzled and "
                f"uneasy, one hand on his hip; the bedroom door open and the corridor empty behind him",
         camera=f"medium shot, eye level, {LOW} (the bedside table top with the bottle)", amb="room_night"),
    # ---------------- 11 P.M.
    dict(to=89, reason="time jump: near 11 p.m. Aamir comes to the room; Shahula turned away, awake in tears; 'Who is Reysham?'",
         chars=["shahula", "aamir"], loc="bedroom_late",
         visual=f"{SH_MINT} sitting on the far edge of the bed with her back half turned to the door, fully dressed, her eyes "
                f"open and staring at the wall, tears on her cheek; {A_HOME} standing in the doorway across the room, yawning, "
                f"looking at her; the whole room between them, not touching",
         camera=f"wide shot, eye level, {LOW} (the dark floor and bedspread)", amb="room_night", transition="black",
         sens="intimacy", safe="no couple in bed, no hand on her, no cheek kiss (bible rule 5): she sits on the far edge of the bed, he stands at the door"),
    dict(to=90, reason="character focus: Aamir frozen with shock",
         chars=["aamir"], loc="bedroom_late",
         visual=f"medium close-up of {A_HOME} sitting on a chair across the room from the bed, frozen, staring in shock and "
                f"surprise, his face half lit by the dim amber lamp",
         camera=f"medium close-up, eye level, {LOW} (dark shadow)", amb="room_night"),
    dict(to=92, reason="action change: she turns to face him, eyes locked; 'Who... came to this house?'",
         chars=["shahula", "aamir"], loc="bedroom_late",
         visual=f"{SH_MINT} sitting on the edge of the bed, turned toward {A_HOME}, who sits on a chair across the room; "
                f"their eyes locked, her eyes brimming with tears and a bitter smile on her lips, he uneasy and hesitant; "
                f"the dim lamp between them, the width of the room between them, not touching",
         camera=f"medium wide two-shot from the side, eye level, {LOW} (the dark tiled floor)", amb="room_night"),
    dict(to=95, reason="focus change: Shahula's bitter accusation - she has heard the name from his own lips",
         chars=["shahula"], loc="bedroom_late",
         visual=f"medium close-up of {SH_MINT}, tears on her cheeks, a bitter hurt smile, speaking with quiet trembling "
                f"conviction, the amber lamp glow on one side of her face",
         camera=f"medium close-up, eye level, {LOW} (the bedspread in shadow)", amb="room_night",
         sens="intimacy", safe="the narration about intimate moments is carried by her face alone"),
    dict(to=96, reason="back to Aamir, speechless", reuse="beat_032", chars=["aamir"], loc="bedroom_late",
         visual="reuse of beat_032", amb="room_night"),
    dict(to=98, reason="back to Shahula's trembling questions - 'she will never give birth, will she?'", reuse="beat_034",
         chars=["shahula"], loc="bedroom_late", visual="reuse of beat_034", amb="room_night"),
    dict(to=100, reason="emotional turning point: Aamir's face hardens into fury (the blow itself is never shown)",
         chars=["aamir"], loc="bedroom_late",
         visual=f"close-up of {A_HOME}, his handsome face hardening into cold fury, jaw clenched, eyes dark, lit harshly from "
                f"below by the lamp, seen from her point of view; his hands not visible",
         camera=f"close-up, slightly low angle, {LOW} (dark shadow)", amb="room_night", hum=True,
         sens="violence", safe=SAFE_DV + "; the blow and the hurt lip are shown only as his furious face from her point of view and a muffled thud"),
    dict(to=101, reason="detail: she looks at her own trembling hand in the dim light",
         chars=[], loc="bedroom_late",
         visual="extreme close-up filling the frame with only a young woman's trembling open hand, palm up, clean and unmarked, with two plain gold bangles on "
                "the wrist and the sleeve of a pale-mint dress, lit by the dim amber lamp against a dark background; only the hand, wrist and sleeve are in the frame, no face, no "
                "other person, the palm completely clean",
         camera=f"close-up, {LOW} (dark bedspread)", amb="room_night",
         sens="violence", safe="the narration's stain on her palm is not shown: a clean trembling hand only"),
    dict(to=103, reason="emotional turning point: no more tears - she stands up to him with a strong question",
         chars=["shahula"], loc="bedroom_late",
         visual=f"{SH_MINT}, {MINT_X}, sitting on the edge of the bed, face turned up toward someone off-frame, dry-eyed and defiant, "
                f"chin raised, no marks on her face, her face half in amber lamp light and half in shadow",
         camera=f"medium close-up, slightly high angle, {LOW} (the bedspread in shadow)", amb="room_night"),
    dict(to=104, reason="cliffhanger: Aamir steps forward to show his power (the grip never shown)",
         chars=["aamir", "shahula"], loc="bedroom_late",
         visual=f"{A_HOME} taking a step forward, looming tall and menacing in the dim lamp light, his long shadow falling "
                f"over {SH_MINT}, {MINT_X}, who sits frozen on the edge of the bed looking up at him with wide shocked eyes; his hands "
                f"at his sides, {GAP}",
         camera=f"medium wide shot, low angle from beside the bed, {LOW} (the dark floor)", amb="room_night", hum=True,
         sens="violence", safe=SAFE_DV + "; the grip on her arms is shown only as his looming shadow over her"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Hearing someone call out a salaam, Shahula gently laid her dear little baby, asleep on her shoulder, on the bed, and answering the greeting she hurried out to the hall.",
   [("footsteps_pavement", "ނުކުތެވެ", -24)])
sh(2, "There, inside the main door of the house, right by the hall door, stood a completely unfamiliar face. \"Shahula?\" the young woman asked, gesturing toward her.")
sh(3, "Shahula nodded in agreement. \"I came to meet Shahula,\" the young woman said. Shahula invited her to come inside.")
sh(4, "With that, by way of introducing herself, the girl held out the paper bag in her hand to Shahula. As Shahula looked at the bag with a gaze full of surprise, a light smile spread over the girl's lips.",
   [("paper_shuffle", "ދިއްކޮށްލިއެވެ", -22)])
sh(5, "\"I'm Reysham...\" the young woman said. Shahula stood frozen, not knowing what to do or what to say.")
sh(6, "The name 'Reysham' was not unfamiliar to her. But this was the first time she had laid eyes on that Reysham. With that, Shahula's heart began to pound harder.",
   [("heartbeat", "ތެޅުން", -22)])
sh(7, "Though she did not know the real reason Reysham had come to the house, her sixth sense kept warning her that no good intention lay behind that visit.")
sh(8, "At the same time, an unease about Reysham's looks rose in Shahula's heart. In Reysham's image she was seeing a picture of her own youth.")
sh(9, "The lively, fresh youth Shahula had at seventeen or eighteen could be seen in Reysham.")
sh(10, "Since giving birth, Shahula's body had changed a great deal. The place of the caesarean was still swollen.")
sh(11, "The swelling of her legs from the pregnancy had not fully gone, and her figure was sagging terribly. Compared with her present state,")
sh(12, "Reysham looked like a fresh rose still blooming on its branch, untouched by anyone. \"Sit!\" Shahula said calmly.")
sh(13, "And after calling Suneetha, who helped in the house, she asked her to bring a cold drink.")
sh(14, "Since that house had always been a model of fine customs of hospitality, caring for any guest who came, in any circumstance, was something she would never give up.")
sh(15, "These were the noble qualities she had inherited from her aunt Azeeza. Settling on the sofa opposite, Shahula spoke.",
   [("cloth_rustle", "ހަމަޖެހިލަމުން", -24)])
sh(16, "\"How does Reysham know me? I don't know any Reysham. I don't remember ever meeting before.\"")
sh(17, "Reysham was a little surprised by Shahula's direct question. Yet from the small start on Shahula's face, Reysham was sure that Shahula had now realised who she was.")
sh(18, "The patience and calm Shahula showed were the way she had chosen to face this situation wisely. Even so,")
sh(19, "Reysham's real aim was to take away that calm and unsettle her heart. \"True, we've never met before.")
sh(20, "But I know Shahula through Aamir. We've been together a long time now.")
sh(21, "So it would be much better not to try to hold on to Aamir. He's a man.")
sh(22, "You know men have many freedoms and choices that a woman doesn't.\" Reysham said it without the slightest hesitation.")
sh(23, "Reysham's impudent words left Shahula astonished beyond words. Without any shame,")
sh(24, "she had dared to say such a truth so openly, right to her face.")
sh(25, "Controlling the unease that filled her heart, letting out a deep breath, Shahula answered steadily.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(26, "\"Rather than saying what you're saying to me, it would be much better to say it to Aamir.")
sh(27, "And besides, do you really think a man of that nature can be held on to by any woman?\"")
sh(28, "Shahula said in a calm but weighty tone. As if she had not grasped the meaning of Shahula's words,")
sh(29, "Reysham sat staring, one eyebrow raised. Again without any hesitation, Shahula asked: \"How long has this relationship you speak of been going on?\"")
sh(30, "\"We've worked in the same office for three years. We've been seeing each other for a year and a half now. And it was Aamir himself who first asked to be friends.")
sh(31, "Who would refuse a man of such charm when he asks? Even Shahula couldn't refuse him, could you?")
sh(32, "And to hold on to him, you even went and had a child for nothing.\" Reysham said with a wide smile. With those words,")
sh(33, "Shahula's thoughts plunged into the depths of the past. The days of her first pregnancy were the days she felt Aamir's strangeness and distance the most.")
sh(34, "Now it was all very clear. Nothing was confusing any more. Even in tender moments of love, she would sometimes hear Reysham's name slip from Aamir's tongue.")
sh(35, "But Shahula never had the courage to ask which Reysham that was. Because she did not want to become a victim of Aamir's anger.")
sh(36, "\"You two have a lot of problems, don't you? Every time there's trouble between you, do you know it's to me that Aamir goes when he leaves the house?")
sh(37, "All these days that habit of his hasn't changed. He never goes to anyone else.")
sh(38, "He comes straight to me to find comfort... I asked him why you still live together when there's no peace at all.")
sh(39, "Aamir isn't a man without options, after all. But he said it would be hard to leave Shahula.")
sh(40, "In his view, Shahula is a great responsibility laid on his shoulder. A great burden his mother entrusted to him as she left this world, so he can't separate, he said.")
sh(41, "Even so, I won't say it's easy for Aamir to end a relationship.\" Saying this, Reysham let out a mocking laugh.")
sh(42, "The poisonous mockery in Reysham's voice felt to Shahula as if a flame had burned her honour and dignity to ashes.", hum=True)
sh(43, "Aamir had ground her self-respect into sand. Even so, Shahula sat silent with patience, saying nothing.")
sh(44, "She put reason above anger. What use was it being angry at that girl? The real culprit was Aamir.")
sh(45, "His faithless, unfaithful deeds. \"This is a gift I brought for the little one,\" Reysham said, rising from the sofa.",
   [("cloth_rustle", "ތެދުވަމުން", -24)])
sh(46, "Just then Suneetha came with cups of masala tea and a tray of short-eats to have with the tea, and set them on the small table in front of the sofa.",
   [("cup_clatter", "ބެހެއްޓިއެވެ", -20)])
sh(47, "\"Thank you so much, the service is excellent! From now on, I'll be the one doing the hosting in this house.\"")
sh(48, "A poisonous, mocking smile showed on Reysham's lips. Shahula too stood up. But, saying nothing, she held her patience.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(49, "Just then came the sound of the little baby starting to cry. Before Shahula could move, Suneetha ran into the room.",
   [("footsteps_pavement", "ދުވެފައި", -22)])
sh(50, "\"I know that where Shahula can't keep her husband content, she doesn't know how to look after children either.")
sh(51, "Because of the little baby's crying, Aamir has lost his restful sleep at night. Isn't it time you moved to another room!\"")
sh(52, "Reysham said in a tone of mockery and scorn. \"Thank you very much for the advice you gave!")
sh(53, "But Reysham has no need to show me where I and my child should sleep. And Aamir doesn't know that either.")
sh(54, "In this house my authority runs just as far as Aamir's does. Didn't Aamir tell you that?\"")
sh(55, "Shahula said firmly, holding back the anger burning in her heart. Reysham smirked mockingly once more.")
sh(56, "\"Have you finished saying everything you came to say? Then it would be best for you to go now. I need to go to my child.\"")
sh(57, "By then the baby was crying with hunger for milk, and Shahula felt it. With a light scornful smile Reysham looked at Shahula and shook her head.")
sh(58, "Even as she had come in, Reysham had sensed the new mother about her. Shahula was furious beyond measure.")
sh(59, "Even so, she spoke to Reysham patiently, in her ordinary voice. A sweet smile crept onto Reysham's lips as she became sure she had achieved her aim.")
sh(60, "So, without lingering any longer, she started to leave. As Reysham went out and the front door slammed, Shahula felt as if the whole world was spinning.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -22), ("door_slam", "ލެއްޕުނު", -16)])
sh(61, "She found herself holding her head with both hands. And pressing both hands to her aching chest.",
   [("breath_heavy", "ހިފަހައްޓައިލެވުނެވެ", -22)])
sh(62, "Though she had not wanted to show her weakness in front of Reysham, once she was alone every emotion came and engulfed her.")
sh(63, "Into the emotional frailty she had suffered since the birth, and the neglect and cruelty she saw from Aamir,")
sh(64, "his unfaithfulness was added, like an arrow that shattered her heart to pieces. Even something done in secret could not cause a heart pain like this.")
sh(65, "Tears poured from her eyes without restraint. After hiding her face in both hands, she suddenly lowered them at a thought and looked straight ahead.",
   [("sob_breath", "އޮހޮރިގަތީ", -22)], hum=True)
sh(66, "And gathering her courage she got up, picked up the bag Reysham had left, gritted her teeth and flung it with all the strength of her arm.",
   [("soft_thud", "ހޫރައިލިއެވެ", -20)])
sh(67, "The darkness of night spread over the whole universe and silence fell. With the little baby resting in her lap,")
sh(68, "as Shahula gently rocked him, she sat lost, her gaze fixed on one spot. Echoing in her mind and heart were the hurtful words Reysham had said that afternoon.")
sh(69, "\"Now I understand... everything has become very clear. All this time I was trying to piece together the shards of a shattered vase.")
sh(70, "But how will the cracks in it ever disappear? How will that bond ever be restored as it was before?")
sh(71, "I have endured Aamir's cruelty for the sake of that poor mother, on the promise I made her before she passed away. But this is enough now.\"", hum=True)
sh(72, "Shahula went on talking to herself. She looked at her baby, who was waving his arms and legs and making soft little sounds.")
sh(73, "Just then the tiny soul smiled so wide that his innocent gums showed. There was no trace of sleep in those dear little eyes.")
sh(74, "Lifting her baby, Shahula lovingly pressed her lips to his cheek. At that moment the tears she had been holding back rolled down her cheeks.")
sh(75, "Holding the baby tight to her chest, she began to sob. Hearing his mother cry, the little one too puckered his lips and began to cry.",
   [("sob_breath", "ގިސްލެވެން", -22)], hum=True)
sh(76, "As if the pain in the mother's heart could be felt by that tiny heart too. When Aamir came home, Shahula had bathed and dressed up nicely.",
   [("door_open", "އައިއިރު", -22)])
sh(77, "Unlike other nights, there was a freshness about her. Instead of the milky smell that usually clings after a birth, a completely different sweet fragrance came from her.")
sh(78, "She slowly shook the bottle in her hand and set it on the table nearby. Seeing a sight he had never seen before, Aamir was surprised.")
sh(79, "\"Are you going to give the little one a bottle?\" Aamir asked, utterly surprised. \"Yes, this is the one from this afternoon... what was her name?\"")
sh(80, "Shahula said with a cold smile. \"I don't remember the name. A gift that office girl of yours brought for Zidhaan. So it wouldn't do to throw it away unused, would it?\"")
sh(81, "There was mockery and scorn in Shahula's words. \"I'm going to cook,\" Shahula said quickly, giving Aamir no chance to ask anything more.")
sh(82, "And with hurried steps she left the room. As Shahula went out, Aamir looked at the bottle Shahula had been holding.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -22)])
sh(83, "He could not work out who had brought it. Shahula knew very well that Zidhaan was not yet old enough for a bottle.")
sh(84, "Then why was she doing this? When it was nearly eleven at night, after switching off the TV, Aamir stretched to shake off his tiredness.")
sh(85, "By then Shahula was nowhere to be seen in the sitting room. Yawning, Aamir went into the room; Shahula was lying on the bed with her back to the door.",
   [("door_open", "ވަންއިރު", -22)])
sh(86, "Aamir slowly came to the bed, and laid his hand lovingly on Shahula's shoulder. \"Asleep?\" Aamir asked gently.")
sh(87, "But Shahula gave no answer. Instead she squeezed her eyes shut tighter. Her heart was in pieces, sobbing deep inside.")
sh(88, "Reysham's words were still echoing in her ears. While those poisonous words were running through Shahula's mind,")
sh(89, "she felt Aamir's affection on her cheek. \"Who is Reysham?\" Shahula asked, suddenly opening her eyes.",
   [("breath", "ހުޅުވާލަމުން", -22)])
sh(90, "With that, the movement of Aamir's hand on Shahula's shoulder stopped. Aamir could only stare, in shock and surprise.",
   [("heartbeat", "ހުއްޓުނެވެ", -22)])
sh(91, "Then the tears that had gathered in Shahula's eyes rolled down her cheeks unchecked. Shahula turned towards Aamir and met his eyes with her own, full of tears.")
sh(92, "\"Who... came to this house?\" Aamir asked in a hesitant voice. At that moment a bitter, mocking smile came to Shahula's lips.")
sh(93, "\"Even if no one else told me, I have heard that name from your own mouth many times.")
sh(94, "Even in our most private moments, it is Reysham's name you whisper.")
sh(95, "Before, I thought it was just a suspicion. But today I am certain it is a bitter truth.\" At Shahula's words,")
sh(96, "Aamir, not knowing what to say, could only stare at her face. \"She may be prettier and younger than me. Yes!")
sh(97, "She'll never have a baby, will she? That youth will stay with her forever. She'll give Aamir everything he wants, again and again.")
sh(98, "And no baby's crying will ever be heard from her room, isn't that so?\" From the questions Shahula asked, her eyes fixed on his face, Aamir clearly felt the pain and trembling in her voice.")
sh(99, "Even so, Aamir felt that Shahula had no right to put such questions to him.")
sh(100, "In a violent fit of rage that overcame him, he struck Shahula across the face. Her lip was hurt at once.",
    [("soft_thud", "ޖެހިއެވެ", -23)], hum=True)
sh(101, "When Shahula touched her lip, she felt the mark of it on her palm. In the dim light of the room she looked at her own hand.",
    [("breath", "ބަލައިލިއެވެ", -22)])
sh(102, "\"You've shown that you're a strong man. But does Aamir know what happens when we women find our courage and stand up?\"")
sh(103, "This time not a single tear fell from Shahula's eyes. Nor did she sob. Instead she faced him with a strong question. At that moment,")
sh(104, "to show his own power and strength, Aamir stepped forward and seized both of Shahula's arms tightly.",
    [("heartbeat", "ހިފެހެއްޓިއެވެ", -20)], hum=True)
SHOTS = S

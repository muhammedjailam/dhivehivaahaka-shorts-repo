"""Beat/shot plan for Yaraa episode 582 (second episode, continues directly from 573; used by plan_beats.py)."""

LOC = {
    "jungle_path": "a narrow white coral-sand path winding through the dense overgrown jungle of a deserted Maldivian island: tall leaning coconut palms, screw-pines with stilt roots, tangled magoo shrubs and undergrowth closing in on both sides, the canopy opening to the sky above the path",
    "pond": "an inland jungle pond (kulhi) on the deserted island: still dark-green water ringed with reeds and soft pale muddy sand banks, an old overgrown taro field (kandoofa) of big heart-shaped taro leaves on one side, thick tall grass clumps, a dense wall of coconut palms and screw-pines all around",
    "taro_field": "the old overgrown taro field beside the jungle pond: rows of tall taro plants with huge heart-shaped leaves, thick tall grass clumps draped with silvery spider webs, the dark mouth of the deep jungle beyond, empty sand paths disappearing between the trees",
    "island_aerial": "a high wide view over the small deserted jungle island: an unbroken green canopy of palms, a tiny glinting pond in a clearing, a thin ring of white beach and a dark grey-green sea stretching empty to the horizon in every direction",
    "shoreline": "the deserted island's white sand shoreline at the jungle edge: the waterline with small choppy grey waves, coconut palms leaning over the beach, the open empty sea beyond",
    "beach_ridge": "the shady beach ridge of the deserted island where the bags were left: low leafy trees and magoo shrubs over white sand, a couple of bags and a cooler box in the shade, the beach and the sea beyond",
    "tarp_shelter": "a tiny makeshift shelter on the beach ridge of the deserted island: a small blue tarpaulin tied between two leaning coconut palms over a patch of sand, bags beneath it, the beach and the heaving grey sea beyond",
    "memory_beach": "the dazzling white sand beach of the island in the morning, remembered: a turquoise lagoon, coconut palms, the long sand spit at the island's tip",
    "memory_dinghy": "a small white dinghy with an outboard engine gliding over a calm turquoise sea in the morning, remembered, the green island on the horizon",
    "memory_magoo": "the shade of a magoo bush on the island's beach ridge in the morning, remembered: a woven coconut-leaf mat on white sand, the turquoise lagoon glittering beyond",
    "open_sea": "the open sea between the island and Male: big rough grey-blue waves with white crests, a wide stormy sky, the faint low skyline of Male far on the horizon",
    "male_jetty": "a Male jetty at dusk: a concrete quay with mooring bollards, small dinghies and wooden dhonis moored alongside, tall amber lamp posts, the dense skyline of Male buildings behind, the harbour water reflecting the lamps",
    "male_lane": "a narrow lamp-lit Male lane at night: tall apartment buildings close on both sides with dim balconies, a few parked motorbikes, warm amber street lamps on the walls, a soft fog hanging in the lane, no signs",
}
MOOD = {
    "jungle_path": "darkening early afternoon, an enormous shapeless black cloud rising over the jungle canopy, the green jungle shade turning gloomy, an ominous stillness before the storm",
    "pond": "green jungle shade under a darkening sky, the huge black cloud overhead, muted and unsettling, a cold stillness",
    "taro_field": "gloomy green jungle shade, dim grey light filtering down, silvery webs catching the light, quietly unsettling and lonely",
    "island_aerial": "a vast shapeless black storm cloud spreading over the island, slate-grey light, small and utterly alone",
    "shoreline": "slate-grey storm light building, black clouds over a dark grey-green sea, wind rising",
    "beach_ridge": "slate-grey overcast afternoon, a fragile calm before the storm, soft diffused light",
    "tarp_shelter": "slate-grey storm, heavy silver rain slanting in strong wind, palms bending, the blue tarpaulin glistening, cold, lonely and tense",
    "memory_beach": "warm hazy memory glow: golden morning sunlight with a soft dreamy bloom and faded edges, tender and nostalgic",
    "memory_dinghy": "warm hazy memory glow: soft golden light on turquoise water, dreamy bloom and faded edges, tender and nostalgic",
    "memory_magoo": "warm hazy memory glow: dappled golden light through leaves, soft dreamy bloom and faded edges, shy happiness",
    "open_sea": "late grey dusk over a heaving sea, salt spray, the last cold light, the first faint lights of Male far away",
    "male_jetty": "blue dusk with warm amber lamps, the sky deep blue with a last glow on the horizon, lamp reflections on the dark harbour water, uneasy calm",
    "male_lane": "foggy teal night exactly like the cover: deep teal-blue haze, warm amber street lamps with glowing halos, golden rim light, mysterious and tense",
}

BEATS = [
    dict(to=2, reason="episode opening: the black cloud arrives with a thunderclap as Mifzaal and Naveen walk inland", chars=["mifzaal", "naveen"], loc="jungle_path",
         visual="Mifzaal and Naveen seen from behind and slightly to the side, walking fast along the narrow sand path into the dense jungle, small in the frame; Mifzaal in his white linen shirt glancing up anxiously; above the palm canopy an enormous shapeless black storm cloud billows up, a faint flash of lightning inside it; palm fronds stirring; the cloud is only cloud, no faces or figures in it",
         camera="wide shot from behind, low angle, the black cloud and canopy filling the upper two-thirds, the pale sand path as a calm lower third",
         amb="jungle_eerie", sens="other", safe="the ominous 'warning' is shown only as a black storm cloud over the jungle"),
    dict(to=5, reason="scene change: they reach the jungle pond and shout their wives' names; no reply, no footprints", chars=["mifzaal", "naveen"], loc="pond",
         visual="Mifzaal and Naveen standing on the muddy bank of the still dark-green jungle pond, both calling out loudly with hands cupped round their mouths, faces strained and anxious; Naveen in his navy polo, Mifzaal in his white linen shirt; the smooth pale mud of the bank in front of them completely untouched, no footprints anywhere; the taro field and tall grass beyond; the black cloud above the palms",
         camera="medium wide, eye level, the two men in the upper two-thirds, the smooth untouched mud bank and pond water as a calm lower third",
         amb="pond_jungle"),
    dict(to=7, reason="action change: Mifzaal points at the taro field and speaks (speaker focus)", chars=["mifzaal", "naveen"], loc="pond",
         visual="Mifzaal, centred and in sharp focus, face three-quarter to camera, pointing with his arm outstretched towards the old taro field of big heart-shaped leaves beside the pond, speaking urgently with a flicker of hope in his anxious eyes; Naveen softer at the side, turning to look where he points",
         camera="medium shot, eye level, Mifzaal's face in the upper third, the pond edge as the lower third",
         amb="pond_jungle"),
    dict(to=9, reason="action change: searching the taro field — only rustling leaves and spider webs; they dare not enter the deep jungle", chars=["mifzaal", "naveen"], loc="taro_field",
         visual="in the foreground thick tall grass clumps strung with many silvery spider webs and huge taro leaves stirred by the wind; in the middle distance Mifzaal and Naveen seen from behind, standing still at the edge of the taro field, hesitating before the dark mouth of the deep jungle where an empty sand path disappears between the trees; nobody else anywhere",
         camera="medium wide from behind, the webs in sharp focus in the foreground, the two men and the dark jungle in the upper two-thirds, the trampled grass as the lower third",
         amb="jungle_eerie", sens="other", safe="horror built only with atmosphere: webs, rustling leaves, an empty dark path; nothing in the jungle"),
    dict(to=11, reason="emotional turning point: despair on both faces as time passes and questions pile up", chars=["mifzaal", "naveen"], loc="pond",
         visual="close two-shot of Mifzaal and Naveen standing side by side by the pond, sweat on their foreheads, both faces drawn with despair and confusion; Mifzaal staring into the jungle with worried eyes, Naveen rubbing his brow; dim green light under the black sky",
         camera="medium close-up, eye level, both faces in the upper half, their shirts and the dark water as the lower third",
         amb="pond_jungle"),
    dict(to=14, reason="scene change in framing: they are alone on a deserted island cut off from all communication", chars=["mifzaal", "naveen"], loc="island_aerial",
         visual="a high wide view looking down over the deserted jungle island: Mifzaal and Naveen two tiny figures standing in the small clearing by the glinting pond, swallowed by the endless green canopy; a vast shapeless black cloud spreading over the island; an empty dark sea in every direction, no boats, no other island near; no faces or shapes in the clouds",
         camera="extreme wide high-angle shot, the black sky in the upper third, the island in the middle, dark sea as the lower third",
         amb="island_wild"),
    dict(to=16, reason="action change: the strange voice spins in Mifzaal's head, his hands tremble; Naveen frozen", chars=["mifzaal", "naveen"], loc="pond",
         visual="Mifzaal in the foreground holding up his trembling hands and staring at them, then glancing back over his shoulder with frightened wide eyes towards an empty sand path vanishing into the dark trees; the path is completely empty; behind him, softer, Naveen stands frozen with one hand on his head; leaves swaying, long palm shadows",
         camera="medium close-up on Mifzaal, eye level, his face in the upper third, the empty path behind him, the muddy bank as the lower third",
         amb="jungle_eerie", sens="other", safe="the hoarse voice is never shown; only Mifzaal's fear and an empty path"),
    dict(to=18, reason="speaker change: Naveen breaks down — has Shifza left him like their baby did? (speaker focus)", chars=["naveen"], loc="pond",
         visual="Naveen, centred and in sharp focus, standing with one hand pressed on top of his head, his broad face crumpling with grief, wet eyes lifted to the black sky, mouth open as he speaks broken words; the pond and the dark jungle blurred behind him",
         camera="medium close-up, slightly low angle, Naveen's face in the upper half, the dark sky above",
         amb="pond_jungle", sens="other", safe="the lost baby is never shown; only Naveen's grieving face and the sky"),
    dict(to=20, reason="action change: Mifzaal lays a hand on Naveen's shoulder and speaks of a father's feelings (speaker focus)", chars=["mifzaal", "naveen"], loc="pond",
         visual="Mifzaal, centred and in sharp focus facing the camera, laying his hand gently on Naveen's shoulder, speaking softly with a deep, strangely knowing sadness in his eyes; Naveen in three-quarter view from behind at the side, head bowed; the dim pond behind",
         camera="medium shot over Naveen's shoulder, eye level, Mifzaal's face in the upper third",
         amb="pond_jungle", sens="other", safe="men comforting each other (hand on shoulder); no child shown"),
    dict(to=21, reason="return to Naveen's framing: he asks how a newlywed could know a father's feelings (shot / reverse-shot)", loc="pond",
         reuse="beat_008", visual="(reuse of beat_008)", amb="pond_jungle"),
    dict(to=22, reason="emotional turning point: Mifzaal stunned as if struck by thirty-two bolts of lightning", chars=["mifzaal"], loc="pond",
         visual="close-up of Mifzaal frozen in shock, eyes wide and unblinking, lips parted, the colour drained from his face; behind him a jagged silver lightning bolt splits the black sky over the palms, a cold white flash rim-lighting his face",
         camera="close-up, eye level, his face in the upper half, his white shirt collar and the dark background as the lower third",
         amb="pond_jungle", sens="other", safe="his secret is not invented or shown; only his shocked face"),
    dict(to=24, reason="scene change: Mifzaal goes to the shoreline and calls the coast guard", chars=["mifzaal"], loc="shoreline",
         visual="Mifzaal standing alone at the waterline of the white beach, his phone pressed to his ear (screen facing away, no readable screen), his other hand on his hip, talking urgently; choppy grey waves at his feet; black clouds rolling over the empty sea; no boats and no people in sight",
         camera="medium wide, eye level, Mifzaal in the upper two-thirds, the wet sand and foam as the lower third",
         amb="island_wild", sens="other", safe="the coast guard is only a phone call; no officers shown"),
    dict(to=26, reason="action change: a little relief — the two men sit in the shade of the beach ridge waiting", chars=["naveen", "mifzaal"], loc="beach_ridge",
         visual="Mifzaal and Naveen sitting on the white sand in the shade of the beach-ridge trees beside the bags, gazing out at the grey sea; tired faces with a small fragile relief, but still heavy with grief; Naveen's elbows on his knees, Mifzaal leaning back on one hand",
         camera="medium wide, eye level, the two in the upper two-thirds, the white sand as the lower third",
         amb="beach_day"),
    dict(to=29, reason="weather change: strong wind and heavy rain; they huddle under a small blue tarpaulin shelter; a message tone", chars=["mifzaal", "naveen"], loc="tarp_shelter",
         visual="the small blue tarpaulin shelter tied between two bending coconut palms on the beach ridge, heavy silver rain slanting across in the strong wind; Mifzaal and Naveen huddled underneath sitting on the sand, damp clothes clinging loosely but opaque, hugging their knees, looking out at the storm; the grey sea churning beyond; Mifzaal reaching for the phone in his pocket",
         camera="medium wide, eye level, the shelter and the men in the upper two-thirds, the rain-pocked sand as the lower third",
         amb="island_storm_day"),
    dict(to=31, reason="emotional turning point: a message from Yaraa's phone — Mifzaal reads it", chars=["mifzaal"], loc="tarp_shelter",
         visual="close-up of Mifzaal under the blue tarpaulin, rain dripping from its edge, his face softly lit from below by the pale glow of the phone he holds (screen facing away from the camera, nothing readable); his eyes wide, searching, lips trembling; the grey storm blurred behind",
         camera="close-up, eye level, his face in the upper half, the glowing phone back and his hands in the lower part",
         amb="rain_day", sens="other", safe="phone screen never readable, only its glow on his face"),
    dict(to=33, reason="memory (dissolve): Yaraa on the beach with him that morning; she left promising to come right back", chars=["yaraa"], loc="memory_beach",
         visual="a soft dreamlike memory: Yaraa standing barefoot on the dazzling white beach in her loose crimson long dress and black hijab fully covering her hair and neck, turning back over her shoulder with a radiant warm smile and a little wave of her hand, the loose end of her hijab fluttering in the breeze; turquoise lagoon and palms behind; hazy golden bloom",
         camera="medium shot, eye level, her face in the upper third, the white sand as the lower third",
         amb="memory", transition="dissolve", sens="other",
         safe="Yaraa only in a happy memory of that morning, never in the present, no hint of harm; hijab fully covering"),
    dict(to=34, reason="memory detail: 'your gentle hands' — their hands held together in the dinghy", chars=["yaraa", "mifzaal"], loc="memory_dinghy",
         visual="a soft dreamlike memory close-up: Mifzaal and Yaraa sitting side by side on the back seat of the dinghy, only their two hands shown clasped together on the seat between them, her crimson long sleeve and his rolled white linen sleeve and steel wristwatch, sparkling turquoise water rushing past; warm golden haze",
         camera="close-up of the clasped hands in the upper half, the boat seat and water as the lower third",
         amb="memory", transition="dissolve", sens="intimacy", safe="married couple: only holding hands, side by side"),
    dict(to=35, reason="return to the present (dissolve): 'what was to happen has happened'", loc="tarp_shelter",
         reuse="beat_015", visual="(reuse of beat_015)", amb="rain_day", transition="dissolve"),
    dict(to=37, reason="memory (dissolve): their resolve to make room for a little child, married only three days — the shy moment under the magoo", chars=["yaraa", "mifzaal"], loc="memory_magoo",
         visual="a soft dreamlike memory: Mifzaal and Yaraa sitting side by side on a woven mat in the dappled shade of a magoo bush, leaning back against the trunk, holding hands; Yaraa in her crimson dress and black hijab fully covering her hair and neck, looking down with a shy joyful smile, Mifzaal smiling tenderly at the glittering lagoon; hazy golden bloom",
         camera="medium shot, eye level, their faces in the upper third, the mat and sand as the lower third",
         amb="memory", transition="dissolve", sens="intimacy",
         safe="married couple sitting side by side holding hands only; the hoped-for child is never shown"),
    dict(to=38, reason="return to the present (dissolve): 'little hope I can come back to you'", loc="tarp_shelter",
         reuse="beat_015", visual="(reuse of beat_015)", amb="rain_day", transition="dissolve"),
    dict(to=39, reason="return to the shelter: 'don't stay on this island; tell Naveen Shifu is fine'", loc="tarp_shelter",
         reuse="beat_014", visual="(reuse of beat_014)", amb="island_storm_day"),
    dict(to=41, reason="memory (dissolve): her last words — Yaraa beside him in the dinghy", chars=["yaraa", "mifzaal"], loc="memory_dinghy",
         visual="a soft dreamlike memory: Yaraa sitting side by side with Mifzaal on the back seat of the small white dinghy, her hand on his arm, turning her face to him with a loving radiant smile; crimson dress, black hijab fully covering her hair and neck, its loose end fluttering in the sea breeze; Mifzaal softer at the side; calm turquoise sea and the green island behind; warm golden haze",
         camera="medium close-up, eye level, Yaraa's face centred in the upper third, the boat and sea as the lower third",
         amb="memory", transition="dissolve", sens="intimacy",
         safe="married couple side by side, her hand on his arm only; Yaraa only in memory"),
    dict(to=43, reason="return to the present (dissolve): tears run from Mifzaal's eyes — yet relief that they are alive", chars=["mifzaal"], loc="tarp_shelter",
         visual="Mifzaal under the blue tarpaulin with tears streaming down his cheeks mixed with rain, the phone lowered against his chest (screen hidden), a trembling half-smile of relief through his grief, eyes closed and lifted; silver rain behind",
         camera="close-up, slightly low angle, his face in the upper half, his damp white shirt as the lower third",
         amb="rain_day", transition="dissolve"),
    dict(to=45, reason="return to the shelter: little comfort; the message tells them there is no use staying", loc="tarp_shelter",
         reuse="beat_014", visual="(reuse of beat_014)", amb="island_storm_day"),
    dict(to=47, reason="return to the shoreline call: they cancel the coast guard request", loc="shoreline",
         reuse="beat_012", visual="(reuse of beat_012)", amb="island_storm_day"),
    dict(to=48, reason="scene change: crossing the huge waves back to Male", chars=["mifzaal", "naveen"], loc="open_sea",
         visual="the small white dinghy climbing a big rough grey-blue wave, spray flying; Naveen at the outboard in the stern, Mifzaal in front gripping the side, both grim and drenched, clothes opaque; a vast grey dusk sky, faint lights of Male far on the horizon; no markings on the boat",
         camera="wide shot, slightly low angle from the water, the boat and sky in the upper two-thirds, dark water as the lower third",
         amb="sea_rough"),
    dict(to=50, reason="time jump: arrival in Male at about 7 pm; the hoarse voice again in his ear", chars=["mifzaal"], loc="male_jetty",
         visual="Mifzaal standing on the concrete jetty at blue dusk beside a mooring bollard, his face turned sharply to one side as if listening, eyes wide with dread, one hand half-raised near his ear; amber lamps glowing behind him, the moored dinghy below; the quay behind him empty, nobody there",
         camera="medium close-up, eye level, his face in the upper third, the quay as the lower third",
         amb="male_jetty_dusk", transition="black", sens="other", safe="the voice is never shown; only Mifzaal listening in fear on an empty quay"),
    dict(to=51, reason="action change: Mifzaal sits in deep thought — was the voice behind the disappearance?", chars=["mifzaal"], loc="male_jetty",
         visual="Mifzaal sitting alone on the edge of the jetty bench under an amber lamp post, elbows on his knees, hands clasped at his mouth, staring into the dark harbour water in deep troubled thought; lamp reflections rippling",
         camera="medium wide, eye level, Mifzaal in the upper two-thirds, the dark water and quay as the lower third",
         amb="male_jetty_dusk"),
    dict(to=53, reason="character enters and speaks: Naveen pats his shoulder — let's go home tonight (speaker focus)", chars=["naveen", "mifzaal"], loc="male_jetty",
         visual="Naveen, centred and in sharp focus, standing beside the jetty bench with his hand patting the shoulder of the seated Mifzaal, speaking with a tired, kind, reassuring face; Mifzaal softer in the foreground looking up at him; amber lamps and blue dusk behind",
         camera="medium shot, eye level, Naveen's face in the upper third",
         amb="male_jetty_dusk"),
    dict(to=55, reason="scene change: Naveen on his motorbike in a lamp-lit lane; Mifzaal tells him about the voice; Naveen's eyes widen", chars=["naveen", "mifzaal"], loc="male_lane",
         visual="Naveen sitting astride his motorbike in the foggy lamp-lit Male lane, a plain dark helmet in his hand, his eyes suddenly wide in shock as he stares at Mifzaal; Mifzaal standing beside the bike in three-quarter view, leaning in, speaking in a low urgent voice; warm amber street lamps and teal haze; no plates, no signs",
         camera="medium shot, eye level, Naveen's widened eyes in the upper third, the wet lane as the lower third",
         amb="street_night", sens="other", safe="no readable plates or signs"),
    dict(to=56, reason="final turning point: someone behind calls his name — Mifzaal turns around (cliffhanger)", chars=["mifzaal"], loc="male_lane",
         visual="Mifzaal in the middle of the foggy teal night lane turning around over his shoulder towards the camera, eyes wide, face rim-lit in warm gold by the amber street lamps; the lane behind him stretching away empty and out of focus into teal fog, glowing lamp halos; nobody else visible anywhere",
         camera="medium close-up, eye level, his face in the upper third, the misty lane as the lower third",
         amb="night_lane", sens="other", safe="the person calling his name is never shown; the lane stays empty"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "The black storm cloud that came looming overhead welcomed them with a loud crack of sound. The sound of a thunder rumble that makes hearts feel fear.",
   [("thunder", "އަޑުފައްގަނޑަކާ", -14)])
sh(2, "Perhaps it was even nature's warning that something was about to go wrong. But there was no change at all in Mifzaal and Naveen's pace.",
   [("footsteps_sand", "ހިނގުމަކަށް", -22)])
sh(3, "It would be no lie to say the two were impatient to reach their beloved wives. In a moment they had reached the pond.",
   [("footsteps_sand", "އާދެވިއްޖެ", -24)])
sh(4, "At the top of their voices, both began calling loudly by their partners' names. But from that place there was not the slightest stir of anyone.")
sh(5, "Strangely, not even the footprints of where they had walked could be seen. With no range, there was no way to call any phone.")
sh(6, "Anxiously, Mifzaal pointed toward the taro field made on one side of the pond and said: \"Hey, maybe the two went into the taro field.")
sh(7, "Yaraa is so keen to learn how Maldivians lived in the old days. Come on, let's go and check there.\" With that the two went there and called out every name, hoping to find them.",
   [("footsteps_sand", "ގޮސް", -22)])
sh(8, "But no sound could be heard except a leaf rustling on a tree. And in the big grass clumps on one side, spider webs were strung in no small number.",
   [("leaves_rustle", "ހެލިލާ", -20)])
sh(9, "Whatever the case, the only certain truth was that neither of them would dare to go alone into that big jungle.",
   hum=True)
sh(10, "Their hearts would grow far weaker than that. As time passed, despair upon despair showed ever more plainly on Mifzaal and Naveen's faces.")
sh(11, "Nor were the questions rising in their hearts few. Where did they go without telling us? Or did someone do something to them?")
sh(12, "Or are they hiding to scare us? However often these questions are repeated, will anyone come to answer them? No.")
sh(13, "No one will come. Not a single one. How would they even let anyone know, at the very least, what was happening?")
sh(14, "On this deserted island cut off from every communication service, what's the use — there will be no one even to check on us.",
   [("wind_gust", "ފަޅު", -22)])
sh(15, "At that moment Mifzaal's heart jolted. Spinning through his whole head at that moment was the voice that had called to him in that strange, unknown way.",
   [("heartbeat", "ތެޅިގަތް", -20), ("low_growl", "ގޮވާލި", -24)], hum=True)
sh(16, "His whole body, hands and feet, was trembling. Naveen too stood with his hand on his head, unable even to move from the spot.",
   [("breath_heavy", "ތުރުތުރު", -22)], hum=True)
sh(17, "From Naveen's throat at that moment came words just as full of feeling: \"My beloved baby too bade this world",
   [("sob_breath", "ނަވީންގެ", -22)], hum=True)
sh(18, "farewell without any warning. Has my beloved wife Shifza too", hum=True)
sh(19, "left me in just the same way?\" To bring some comfort to the pain aching in Naveen's heart, Mifzaal stroked his shoulder tenderly and said:",
   [("cloth_rustle", "ފިރުމާލަމުން", -24)])
sh(20, "\"Naveen, I too know the feeling a father has when his most beloved child bids farewell in some unknown way.\"")
sh(21, "With Mifzaal's words another question arose in Naveen's heart. \"Mifzaal, but you only just got married, didn't you?")
sh(22, "Then why did you say you know a father's feelings?\" At Naveen's question, Mifzaal's body felt as if thirty-two bolts of lightning had struck at once.",
   [("thunder", "ތޮށިގަނޑު", -16), ("gasp", "ހަށިގަނޑަށް", -20)], hum=True)
sh(23, "But at this delicate moment Mifzaal had no courage in him to answer Naveen's question. So, suddenly saying the phone had got a signal, he got up and went close to the shoreline.",
   [("footsteps_sand", "ތެދުވެ", -22), ("wave_crash", "ރާޅުފަށާ", -22)])
sh(24, "And he quickly called the coast guard and explained their situation. When they said they would come very quickly to rescue them, he hung up.")
sh(25, "With this news Mifzaal and Naveen's hearts found some measure of calm. Though it was happy news for only a short while, both believed it would be the way through all of this.",
   [("sigh", "ހަމަޖެހުމެއް", -22)])
sh(26, "Yet two women vanishing in some unknown way on a deserted island where no one lives is no small, ordinary thing. The scar of that grief, in the heart of everyone")
sh(27, "who grieves for it, is something that will never heal. How sad, isn't it? In a moment, with a strong wind, heavy rain began to pour.",
   [("wind_gust", "ގަދަވަޔާ", -16), ("rain_start", "ވާރޭ", -16)])
sh(28, "On that island they sat in the cover of a tiny shelter made of a tarpaulin, waiting for someone to reach out a helping hand.",
   [("cloth_rustle", "ސަތަރިން", -22)])
sh(29, "How good it would be if Yaraa and Shifza came to shelter from the rain. Suddenly the sound of a message came from Mifzaal's phone.",
   [("phone_buzz", "މެސެޖެއްގެ", -16)])
sh(30, "It was a message sent from Yaraa's phone. He quickly opened the message and began to read. Written in Yaraa's message was:")
sh(31, "\"Mifzaal, I love you, Mifzaal, beyond all limits. And in this very heart your love has laid its foundations forever and ever.",
   hum=True)
sh(32, "You will know very well that only a little while ago I spent time with you on the beach.")
sh(33, "When I left saying I'd be right back with you, it was in the sweet hope of returning,")
sh(34, "longing and longing for the moment those innocent hands of yours would stroke me again.")
sh(35, "But now what was to happen has happened. Still, don't wipe my memory from your heart.")
sh(36, "And the strong resolve we made for our life, to give room in our lives to a tiny little child —")
sh(37, "don't forget it. I know too that it has been only three days since our marriage,")
sh(38, "and I believe you know it too. But now there is very little hope of my coming back to you.", hum=True)
sh(39, "So don't stay on this deserted island — go to Malé. And tell Naveen that Shifu is fine too.")
sh(40, "As my very last word, and as Mifzaal's beloved wife Yaraa,")
sh(41, "the very last word I have to say is... I will always love you, Mifzaal.", hum=True)
sh(42, "I love you so, so much, Mifzaal.\" At Yaraa's words, tears poured from both of Mifzaal's eyes. Strangely, he was also overjoyed,",
   [("sob_breath", "ކަރުނަ", -22)], hum=True)
sh(43, "because now it was certain that Yaraa and Shifza were safe. But where they were, no one knew.")
sh(44, "Though a little comfort reached Mifzaal and Naveen's despairing hearts, there was no real meaning in it.")
sh(45, "Still, they knew the two who were lost were safe. And from Yaraa's message both understood very well that staying on this island would serve no purpose.")
sh(46, "So they called the coast guard and cancelled the request for help, because the two wanted to carry out the search for Yaraa and Shifza themselves.")
sh(47, "But Mifzaal and Naveen made this decision without any thought for what would happen next. What could happen, after all?")
sh(48, "Reluctantly, crossing the huge waves of the ocean, they reached Malé as it was striking seven after sunset.",
   [("boat_engine", "ހުރަސްކޮށް", -18), ("wave_crash", "ރާޅުތައް", -20)])
sh(49, "Even then it seemed to Mifzaal that, right by his ear, someone with that strange hoarse, scratchy voice was calling his name: \"Ey Mifzaal,",
   [("low_growl", "މުސްކުޅި", -24), ("heartbeat", "ގޮވާހެން", -20)], hum=True)
sh(50, "this is a new beginning. Keep in mind that you must still come out under Yaraa's protection.\"", hum=True)
sh(51, "Because of these words something more crept into Mifzaal's mind. Could that one be the real reason Yaraa and Shifza disappeared?")
sh(52, "Or is this a false suspicion of mine? Patting the shoulder of Mifzaal, who sat deep in thought, Naveen said: \"Come on,",
   [("soft_thud", "ޖަހާލަމުން", -22)])
sh(53, "let's go home tonight. We know now that Yaraa and Shifza are all right, don't we? Tomorrow we'll see whether there's any more news.\"")
sh(54, "With that, Naveen went and got on his motorbike. But thinking that telling Naveen about that hoarse voice was the best thing to do at this point, Mifzaal told him all of it.",
   [("engine_rev", "ސައިކަލަށް", -22)])
sh(55, "Naveen's eyes suddenly went wide. And at that very moment someone else called Mifzaal's name from behind.",
   [("gasp", "ބޮޑުވެގެން", -20), ("heartbeat", "ގޮވާލި", -18)], hum=True)
sh(56, "And he turned around to see who it was. And, bewildered, Naveen fired more questions at Mifzaal.",
   [("footsteps_pavement", "އެނބުރިލި", -22)], hum=True)
SHOTS = S

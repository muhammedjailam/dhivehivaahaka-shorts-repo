"""Beat/shot plan for 16 February episode 356 (used by plan_beats.py).
The watch purchase, Malak's run in the rain on 16 Feb, Ali's key, Zain at the jetty, Ahlam and the watch, Ahlam's secret.
Bible rules: hijab always; no touch between Malak and any man; no fall/injury/blood on Malak; the stranger of 16 Feb is a
faceless silhouette in Malak's flashback; Ahlam may be shown alone in the rain in his own flashback; no weapons; no text."""

SHOP = "a small resort souvenir shop with a lit glass watch showcase, shells and sarongs on shelves"
ROAD = "a long dark sandy island road lined with tall trees and scattered dim street lamps"
SITE = "a cluster of three-storey half-built concrete guesthouses, bare columns and empty window holes, rusty rebar, overgrown with weeds, at the edge of the island near the trees"
JETTY = "the island's concrete jetty with ferries and a white resort staff launch, turquoise water"
OFFICE = "an open-plan back-office of the resort, rows of wooden desks with monitors, glass-walled cabins, large windows to palms and sea; the boss's cabin with a dark wooden desk and a leather chair"
NIGHT_MEM = "dark rainy night, lightning flashes, hazy desaturated memory, soft vignette"

LOC = {
    "shop_now": SHOP,
    "shop_memory": SHOP,
    "road_memory": ROAD,
    "site_memory": SITE,
    "jetty": JETTY,
    "villa": "Ahlam's private sitting room in a staff villa on the resort island: a dark leather sofa, a low dark-wooden coffee table, a tall floor lamp, a large glass window to dark palms, plain walls",
    "cabin_memory": OFFICE,
    "training": "a Maldivian coastal defence-force training ground: a wide sandy parade ground by the sea, low white barracks buildings, coconut palms, a calm lagoon beyond",
    "cabin_night": OFFICE,
}
MOOD = {
    "shop_now": "bright late-morning tropical daylight, slightly desaturated turquoise-and-sand tones, cool reflections on the glass showcase, a heavy haunted stillness",
    "shop_memory": "hazy, slightly desaturated memory with soft vignette, warm golden shop lights and bright daytime outside, happy shy anticipation",
    "road_memory": f"{NIGHT_MEM}, cold blue-black shadows, ember-orange glints of lightning on wet sand, terror",
    "site_memory": f"{NIGHT_MEM}, faint blue-and-red police lights flickering far off through the trees, held-breath danger",
    "jetty": "bright tropical morning, slightly desaturated turquoise-and-sand daylight, a light sea breeze, tense and uneasy",
    "villa": "before dawn, a single warm amber floor lamp against deep blue-black shadows, rain streaks on the dark window, brooding and lonely",
    "cabin_memory": "hazy, slightly desaturated memory with soft vignette, bright tropical daylight through large windows, composed and proud",
    "training": "hazy, slightly desaturated memory with soft vignette, golden dawn light over the sea, disciplined and resolute",
    "cabin_night": "late night, a storm outside, lightning flashing at the window, a single ember-orange desk lamp, deep blue-black shadows, secret and resolute",
}

MALAK_NIGHT = "Malak in her deep wine-maroon kurta and black hijab soaked dark with rain, the hijab fully covering her hair and neck, her long sleeves pulled down over her wrists"
BAG = "a small black paper shopping bag"
NO_TEXT_WATCH = "a men's wristwatch with a plain dial, no brand, no numerals"

BEATS = [
    # ---------------- present: the souvenir-shop window
    dict(to=2, reason="episode opening: Malak in the present at the souvenir-shop window, staring at the watch showcase", chars=["malak"], loc="shop_now",
         visual=f"Malak standing outside the small souvenir shop, seen in three-quarter profile, staring through the glass at the lit watch showcase; her pale tired face faintly reflected in the glass over rows of watches with plain dials; one hand resting on the strap of her shoulder bag, eyes distant and haunted",
         camera="medium close-up, eye level, her face and the glass in the upper two-thirds, the wooden ledge of the showcase as a calm lower third", amb="resort_day"),
    # ---------------- memory: buying the watch a week before
    dict(to=6, reason="flashback: a week earlier, inside the shop, Ubey teasing Malak about the price", chars=["malak", "ubey"], loc="shop_memory",
         visual=f"inside the souvenir shop: Malak on the customer side of the glass watch showcase, leaning slightly to look at {NO_TEXT_WATCH} on a dark velvet tray, a bright happy smile; Ubey behind the counter in his teal staff shirt, grinning and raising his eyebrows teasingly; the counter between them",
         camera="medium two-shot across the counter, eye level, faces in the upper half, the glass counter top as the lower third", amb="memory",
         transition="dissolve"),
    dict(to=9, reason="action change: Ubey sets the watch down for her, she strokes it lovingly; he boxes it", chars=["malak", "ubey"], loc="shop_memory",
         visual=f"close shot over the glass counter: Malak's fingertips gently stroking {NO_TEXT_WATCH} lying on a dark velvet tray, her face above it soft with love and a shy smile; Ubey behind the counter holding an open small black watch box ready, smiling; their hands never meet",
         camera="close-up, slightly high angle, Malak's face in the upper third, the watch and tray in the middle, the counter glass below", amb="memory"),
    dict(to=13, reason="action change: paying by card; Ubey says he leaves for Malé tonight, his mother is ill; another attendant walks in", chars=["ubey", "malak"], loc="shop_memory",
         visual=f"Ubey behind the counter holding a small card machine, his smile fading into a sad worried look as he talks about his ill mother; Malak across the counter holding {BAG}, listening with sympathy; in the soft background another young male staff member in a teal shirt walking in through the shop door",
         camera="medium shot, eye level, faces in the upper half, the counter as the lower third", amb="memory",
         sens="other", safe="the card machine shows no readable screen or numbers"),
    # ---------------- present: 16 February, a black date
    dict(to=16, reason="return to the present: Malak's bitter monologue at the showcase — '16 February, a black date'; lightning-fast memory", chars=["malak"], loc="shop_now",
         visual="close-up of Malak in front of the shop window, her eyes glistening, lips pressed together in bitter sorrow, her reflection in the glass overlaid with a faint ghostly flash of white lightning and dark rain, as if the storm lives inside the glass",
         camera="close-up, eye level, face in the upper half, the showcase ledge soft below", amb="resort_day",
         transition="dissolve", sens="other", safe="the date is spoken only; no date or numbers rendered"),
    # ---------------- flashback: night of 16 February, Malak's run
    dict(to=18, reason="flashback: the night of 16 February — Malak running in terror on the dark road clutching the watch bag", chars=["malak"], loc="road_memory",
         visual=f"{MALAK_NIGHT}, running along the dark tree-lined sandy road in the rain, clutching {BAG} to her chest with both hands, looking back over her shoulder with wide terrified eyes; rain slanting through a dim street lamp; trees black on both sides",
         camera="medium wide, eye level, slightly ahead of her, her face in the upper half, the wet sand road as the lower third", amb="memory_rain",
         transition="dissolve"),
    dict(to=21, reason="action change: she stumbles and the bag flies from her hand into the mud", chars=["malak"], loc="road_memory",
         visual=f"in the foreground {BAG} lying on its side in a muddy rain puddle on the dark road, rain drops splashing around it; behind it in soft focus {MALAK_NIGHT}, kneeling up on the wet sand, one hand stretched out towards the bag, face turned up in fright, lit by a flash of lightning",
         camera="low angle close on the bag, Malak kneeling in the upper half of the frame, the puddle in the middle", amb="memory_rain",
         sens="violence", safe="the fall and her injuries (grazed arm, bleeding lip) are not shown: only the dropped bag in the mud and Malak kneeling up, unhurt-looking"),
    dict(to=24, reason="action change: dry leaves crunch — someone is coming; she edges backwards in fear", chars=["malak"], loc="road_memory",
         visual=f"{MALAK_NIGHT}, half-risen, crouching on one knee on the wet road with one hand at the edge of her hijab, staring towards the dark trees at the roadside where branches are shaking, terrified, shrinking backwards; the paper bag forgotten behind her; thin rain",
         camera="medium shot, slightly low angle, her face in the upper half, the wet road below", amb="memory_rain",
         sens="violence", safe="no blood on her hand or lip; fear shown by her face and posture only"),
    dict(to=26, reason="character change: a dark faceless figure emerges from the trees and comes straight at her", loc="road_memory",
         visual="a tall dark male silhouette stepping out from between the black trees onto the rain-swept road, backlit by a flash of lightning, his face completely in shadow and unrecognisable, moving forward with quick steps; rain streaks in the air; no other people",
         camera="medium wide, low angle, the silhouette in the upper two-thirds, the wet road as the lower third", amb="memory_rain",
         sens="other", safe="the stranger stays a faceless dark silhouette; he is not shown reaching her"),
    # ---------------- present: Ali startles her, hands her a key
    dict(to=29, reason="return to the present and character change: Ali calls her name; she startles, gasping", chars=["malak", "ali"], loc="shop_now",
         visual="in front of the souvenir shop: Malak spun round with a sharp intake of breath, one hand pressed to her own chest, eyes wide; Ali in his glasses, white shirt and navy tie standing an arm's length away, his hand already drawn back and raised apologetically, a tablet tucked under his other arm, his face surprised and concerned",
         camera="medium two-shot, eye level, faces in the upper half, the paved path as the lower third", amb="resort_day",
         transition="dissolve", sens="other", safe="narration says Ali touched her shoulder: shown with his hand already drawn back, no contact"),
    dict(to=31, reason="action change: Ali holds out a room key with a meaningful smile; she silently takes it", chars=["ali", "malak"], loc="shop_now",
         visual="Ali in glasses and navy tie holding out a single brass key on a plain wooden key tag at arm's length, a knowing meaningful half-smile; Malak reaching for the dangling key tag from the other end, quiet and serious; their fingers do not touch; bright resort palms behind",
         camera="medium close two-shot, eye level, faces in the upper half, the key in the middle, the path soft below", amb="resort_day",
         sens="other", safe="the key passes by its tag with no hand contact; the tag is blank"),
    # ---------------- home island jetty: Zain
    dict(to=33, reason="scene and time change: home island jetty — Malak steps out of a taxi, Zain arrives on his motorbike", chars=["malak", "zain"], loc="jetty",
         visual="Malak with a small travel bag on her shoulder stepping out of a small white island taxi car near the jetty, glancing back with a worried face; behind her at a distance Zain in his light-grey polo stopping a motorbike and swinging off it; the white resort staff launch moored at the concrete jetty, turquoise water",
         camera="wide shot, eye level, figures in the upper two-thirds, the concrete jetty as the lower third", amb="jetty_day",
         transition="black", sens="other", safe="no number plates or signs; the taxi is plain"),
    dict(to=36, reason="action change: Zain runs after her; she stops and turns to him with reluctance", chars=["zain", "malak"], loc="jetty",
         visual="on the concrete jetty: Zain several steps away, one hand raised, calling out with a pleading hurt face; Malak in the foreground half-turned towards him, travel bag on her shoulder, exhaling a deep breath, her face closed and unwilling; the white launch waiting behind her; a clear gap between them",
         camera="medium wide two-shot, eye level, faces in the upper half, the jetty concrete as the lower third", amb="jetty_day"),
    dict(to=38, reason="emotional framing change: Malak's reproachful bitter smile — 'the real culprit is me'", chars=["malak"], loc="jetty",
         visual="close-up of Malak on the sunny jetty, a faint reproachful bitter smile on her lips, her eyes shining with pain as she looks at someone off-frame; sea glitter and the white launch blurred behind her",
         camera="close-up, eye level, face in the upper half, the sea soft below", amb="jetty_day", hum=True),
    dict(to=42, reason="framing change: Zain bewildered, Malak's disgust at a faithless man", chars=["zain", "malak"], loc="jetty",
         visual="over-the-shoulder shot from behind Malak's black hijab and shoulder: Zain facing her two steps away, completely bewildered, palms open, brows knitted; Malak's partly visible face in the foreground cold and disgusted",
         camera="over-the-shoulder medium shot, Zain's face in the upper third, the jetty concrete below", amb="jetty_day"),
    dict(to=45, reason="action change: Malak walks away towards the launch, Zain stops her again; she nods and makes an excuse", chars=["malak", "zain"], loc="jetty",
         visual="Malak walking away along the jetty towards the moored white launch, travel bag on her shoulder, glancing back with a short nod; Zain a few paces behind her, stopped, one hand half-raised, asking in disbelief",
         camera="medium wide, from the side, faces in the upper half, the jetty as the lower third", amb="jetty_day"),
    dict(to=49, reason="focus change: Zain, disappointed, asks about her birthday; she shrugs", chars=["zain", "malak"], loc="jetty",
         visual="medium close-up of Zain on the jetty, a disappointed wounded look, eyebrows raised pleadingly, hands in the pockets of his jeans; at the near edge of the frame Malak's black hijab and maroon shoulder in soft focus, shrugging",
         camera="medium close-up, eye level, his face in the upper half, the sea soft below", amb="jetty_day"),
    dict(to=52, reason="emotional turning point: anger floods Malak — 'have you forgotten what you did that night?'", chars=["malak"], loc="jetty",
         visual="close-up of Malak, her jaw tight and eyes blazing with silent anger and hurt, staring straight ahead without speaking, the sea wind tugging at the edge of her hijab, hair fully covered; the sky behind her slightly overcast",
         camera="close-up, slightly low angle, face in the upper half, the sky and sea soft below", amb="jetty_day", hum=True,
         sens="intimacy", safe="Zain's 'disgusting act' (the affair) is never shown or described; only Malak's angry face"),
    dict(to=54, reason="action change: Zain announces the ring ceremony; Malak's head throbs", chars=["zain", "malak"], loc="jetty",
         visual="two-shot on the jetty at a respectful distance: Zain smiling eagerly, gesturing with an open hand as he announces his plan; Malak facing him with two fingers pressed to her temple, eyes half-closed, overwhelmed",
         camera="medium two-shot, eye level, faces in the upper half, the jetty as the lower third", amb="jetty_day",
         sens="intimacy", safe="the engagement is only spoken about; no ring or touch shown"),
    dict(to=56, reason="action change: at the launch she stops, looks back — 'I did come… on 16 February' — and boards", chars=["malak"], loc="jetty",
         visual="Malak standing at the edge of the jetty with one foot on the step of the white resort launch, turning her head to look back over her shoulder, a grave, meaningful stare; travel bag on her shoulder; turquoise water below",
         camera="medium shot, slightly low angle, her face in the upper third, the water and launch hull below", amb="jetty_day", hum=True),
    dict(to=58, reason="focus change: Zain left alone on the jetty as the launch pulls away", chars=["zain"], loc="jetty",
         visual="Zain standing alone at the end of the concrete jetty, seen from behind and slightly to the side, staring after the white launch pulling away across the turquoise water with a wake behind it, one hand on the back of his neck, confused",
         camera="wide shot, eye level, Zain and the launch in the upper half, the jetty concrete as the lower third", amb="sea_boat"),
    # ---------------- Ahlam and the watch
    dict(to=61, reason="scene and character change: Ahlam alone before dawn opens a small box holding the same watch", chars=["ahlam"], loc="villa",
         visual=f"Ahlam sitting forward on the dark leather sofa, elbows on his knees, holding an open small black watch box in his hands, looking down at {NO_TEXT_WATCH} inside with a deep thoughtful frown; warm lamp light on one side of his bearded face; rain on the dark window behind",
         camera="medium close-up, eye level, his face in the upper third, the box and his hands in the middle, the coffee table soft below", amb="room_night",
         transition="black", sens="other", safe="the watch has a plain dial with no brand"),
    # ---------------- flashback: Ahlam's side of the night
    dict(to=64, reason="flashback from Ahlam's side: hiding the screaming girl from the men near the building site", chars=["malak"], loc="site_memory",
         visual=f"{MALAK_NIGHT}, crouched hidden behind a low broken concrete wall of the half-built guesthouses, wide frightened eyes, her own hand pressed over her mouth; an arm's length away a tall dark male silhouette crouches, face in shadow, a finger to his lips; faint blue-and-red police lights through the bushes; rain",
         camera="medium shot, eye level, faces in the upper half, the wet ground below", amb="memory_rain",
         transition="dissolve", sens="violence",
         safe="he does not cover her mouth: she holds her own hand over it and he crouches apart (bible rule 3); the murder itself is never shown"),
    dict(to=67, reason="action change: she bites him and runs, a phone lies in the wet leaves; he picks it up and gives chase", chars=["ahlam"], loc="site_memory",
         visual="Ahlam alone in the pouring rain at night among wet bushes, his black shirt soaked, bent down picking up a dark phone lying in the wet leaves while holding his other hand against his chest, staring ahead into the darkness where a small fleeing figure disappears between the trees far away; lightning",
         camera="medium shot, eye level, his face in the upper half, the wet leaves below", amb="memory_rain",
         sens="violence", safe="the bite is not shown; only Ahlam alone holding his hand, and the phone in the wet leaves (rule 3)"),
    dict(to=71, reason="location and action change: out of the trees onto the road — the girl runs off, he picks up the dropped bag", chars=["ahlam"], loc="road_memory",
         visual=f"Ahlam standing on the dark rain-swept tree-lined road holding {BAG} he has just picked up from the mud, looking into it, then up the road where far away a tiny dark figure in a long kurta and hijab runs off into the rain; a dim street lamp; lightning",
         camera="medium wide, eye level, his face in the upper half, the wet sand road as the lower third", amb="memory_rain",
         sens="other", safe="the girl is never shown fallen: only a tiny distant figure running away; no touch"),
    # ---------------- present: the alarm, his vow
    dict(to=73, reuse="beat_022", reason="return to the present: his phone alarm wakes him from the memory; he strokes the watch", loc="villa",
         visual="(reuse)", amb="room_night", transition="dissolve", hum=True),
    dict(to=75, reason="action change: he puts the watch back in its box, sets it on the table and leans back on the sofa", chars=["ahlam"], loc="villa",
         visual="Ahlam leaning back on the dark leather sofa with his head resting against the backrest, eyes on the ceiling, exhaling deeply; on the low coffee table in front of him the closed small black watch box beside a phone lying face down; the floor lamp glowing amber",
         camera="medium wide, eye level, his face in the upper third, the coffee table as the lower third", amb="room_night"),
    # ---------------- backstory narration
    dict(to=78, reason="narrated backstory: the public face — businessman Ahlam Umar, heir of the resort owner", chars=["ahlam"], loc="cabin_memory",
         visual="Ahlam standing in the boss's glass cabin of the resort office in his black shirt with sleeves rolled, hands in his pockets, looking out through the large window over palms and turquoise sea, composed and powerful, the dark wooden desk and leather chair behind him",
         camera="medium wide from behind and to the side, his face in profile in the upper third, the polished floor as the lower third", amb="office_day",
         transition="dissolve", sens="other", safe="Hassan Waleed is only mentioned, not shown"),
    dict(to=81, reason="narrated backstory: six months away — he returned as a defence-force officer serving the nation", chars=["ahlam"], loc="training",
         visual="Ahlam standing at attention on the sandy parade ground at dawn, his whole figure visible from head to boots, both feet planted firmly on top of the flat sand, in a plain dark-green defence-force uniform with small embroidered rank stars on the shoulders, a plain beret, dark boots, no name tags, no text, no weapons, his bearded face proud and resolute, low white barracks, the sea and palms glowing gold behind him",
         camera="full-length shot from a little distance, eye level, his face in the upper third, the flat sand ground in front of his boots as the lower third", amb="beach_day",
         sens="other", safe="military service shown without any weapon; insignia plain, no readable text"),
    dict(to=84, reason="narrated backstory: the double life — outwardly a businessman, secretly an undercover officer on an unfinished mission", chars=["ahlam"], loc="cabin_night",
         visual="Ahlam alone in his dark office cabin at night in his black shirt, half his bearded face lit ember-orange by a single desk lamp, the other half in deep shadow, gazing at the storm-dark window where a faint ghostly reflection of himself in a dark-green uniform stands; lightning in the sky beyond",
         camera="medium close-up, eye level, face in the upper third, the dark desk top as the lower third", amb="office_storm_night",
         transition="dissolve", hum=True),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Through the glass of the souvenir shop, what she began to see was not the present. It was the reality of a week before.")
sh(2, "Her mind sank into those memories of the past; with the ticking seconds of that watch, it carried her back once again to that frightening time.",
   [("clock_tick", "ސިކުންތު", -20)])
sh(3, "After looking carefully at the watch, Malak met the shop attendant's eyes and smiled. \"Are you sure? This is a very expensive brand,\"")
sh(4, "the attendant said with a smile. \"No matter how expensive, it's no problem. Even if I have to spend all the money I've saved, that's fine.")
sh(5, "You know too, Ubey, that I'd buy this watch,\" Malak said happily. Ubey chuckled softly. \"Hmm...")
sh(6, "For someone very special, right? We don't get that kind of luck,\" Ubey joked. \"Yes... it really is a very special person.\"")
sh(7, "Malak answered with a shy smile. Ubey picked up the watch and held it out to Malak. Malak stroked the watch with great love and care.")
sh(8, "\"It will look perfect on the wrist,\" she said. \"Shall I gift-wrap it?\" Ubey asked. \"No, give it as it is.\"")
sh(9, "Smiling at her answer, Ubey put the watch in its box, placed it in a nice bag and handed it to Malak.",
   [("paper_shuffle", "ކޮތަޅަކަށް", -22)])
sh(10, "Malak quickly held out her card to pay. \"Malak, I'm leaving for Malé tonight.")
sh(11, "I'll only be back in about a month,\" Ubey said, swiping the card in the machine. \"Really? Such a long holiday?\" Malak asked in surprise.")
sh(12, "\"Yes, my mother is very ill, she has to go to India for treatment.\" Ubey handed back the card.")
sh(13, "Just then the shop's other attendant came in too. Wishing Ubey's mother a quick recovery and praying for a safe journey,",
   [("door_open", "ވަދެއްޖެއެވެ", -22)])
sh(14, "Malak left the shop and walked away. \"With how much love and joy did I buy that watch? My whole life has changed, my whole life has turned upside down.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(15, "16 February became a black, dark date that changed my life completely,\" Malak murmured softly, with deep sorrow.", hum=True)
sh(16, "\"16 February.\" Slowly the poisonous date repeated itself on her tongue. Suddenly, as fast as lightning, the terror of that day came alive before her eyes.",
   [("thunder", "ވިދުވަރެއް", -16)], hum=True)
sh(17, "In her hand at that moment was the expensive watch from the shop. Gripping the bag tightly and looking back, she was running through dark roads thick with trees.",
   [("footsteps_sand", "ދުވަމުން", -20)])
sh(18, "It was as if she were running for her life from a bloodthirsty hunter. Malak's hair, soaked by the rain, lay scattered",
   [("breath_heavy", "ދުވާ", -22)])
sh(19, "over her face. Running and trembling with fear, she tripped on a stone in the road and fell face-down to the ground.",
   [("thunder", "ވެއްޓުނެވެ", -16)])
sh(20, "With that, the bag in her hand flew away — the bag she had guarded more than her own life. \"Mamma!\"",
   [("gasp", "މަންމާ", -18)])
sh(21, "burst from Malak's mouth with the pain. She pushed up the sleeve of her kurta and looked at where she was hurt.")
sh(22, "And when she touched her aching lips and looked, there was red blood on her hand. She was so frightened she could hardly breathe. At that moment,",
   [("heartbeat", "ފިތްކަނޑައިގެންދާ", -20)], hum=True)
sh(23, "the crunch of dry leaves began to come from among the nearby trees. Someone was coming towards her, fast.",
   [("leaves_rustle", "ހިކިފަތްތައް", -16)])
sh(24, "Frozen with fear, Malak began to edge backwards. The drizzle that was falling soaked her completely.",
   [("breath", "ފަހަތަށް", -22)])
sh(25, "Out of the darkness came the young man who had tried to hold her back. In the dark it wasn't clear who he was.")
sh(26, "That mysterious person came with quick steps straight towards Malak. \"Malak!\" Ali suddenly called, touching Malak's shoulder.",
   [("footsteps_sand", "ފިޔަވަޅުތަކެއްގައި", -20)])
sh(27, "Startled, Malak was left gasping. It was as if she had been holding her breath for a long time and had let it go. \"Malak...",
   [("gasp", "ސިހުމާއެކު", -18)])
sh(28, "It's me!\" Seeing how startled she was, Ali flinched a little too. \"Calm down! What's the matter with you? Did you see something scary?\"")
sh(29, "Ali asked with concern. Without saying a word, Malak shook her head as if to say no.")
sh(30, "Ali held out a key towards Malak. \"From now on, the boss has arranged for you to stay here on nights you can't get back to the island.\"",
   [("keys_jingle", "ތަޅުދަނޑި", -20)])
sh(31, "As Ali said this, a meaningful smile appeared on his lips. Malak silently took the key.",
   [("keys_jingle", "ތަޅުދަނޑީގައި", -24)])
sh(32, "With a small travel bag on her shoulder, Malak got out of a taxi near the jetty. Just then Zain arrived on his motorbike, stopped,",
   [("car_door", "ފޭބީ", -20), ("motorbike_pass", "ސައިކަލުގައި", -18)])
sh(33, "and came walking quickly towards Malak. Seeing Zain, Malak worriedly grabbed her bag and hurried towards the launch in the harbour.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -22)])
sh(34, "\"Malak! Wait!\" Zain shouted at the top of his voice, running after her. Malak slowed her steps.",
   [("footsteps_pavement", "ދުވަމުން", -22)])
sh(35, "And letting out a deep breath, she turned to look at Zain. Her face made it clear she didn't want to talk to him at all.",
   [("sigh", "ނޭވާއެއް", -20)])
sh(36, "\"Why are you running away from me? Did I do something wrong?\" Zain asked sadly, not knowing what had happened.")
sh(37, "Painful scenes from the past came alive in Malak's mind once again. She looked at Zain with a reproachful smile.")
sh(38, "And she said the guilty one wasn't Zain — the real culprit was herself. \"Say clearly what you're trying to say!\"")
sh(39, "Zain's face showed utter astonishment. \"Forgive me, Zain! I can't talk any more right now.")
sh(40, "I can never be the kind of person you want.\" Malak's voice was full of unease and anxiety.")
sh(41, "Yet her face showed extreme disgust — the hatred and anger born of giving her heart to a faithless man.", hum=True)
sh(42, "\"I don't understand any of this! What are you talking about?\" Zain asked, not grasping her words, lost.")
sh(43, "\"Don't ask any more questions, Zain. When the time comes everything will be clear. I'm going... I'm very late!\" Malak turned and walked off. But",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(44, "since he hadn't said what he'd come to say, Zain stopped her again. \"Are you leaving so you won't come back to the island?\" he asked, astonished.")
sh(45, "Malak nodded in agreement. And she made the excuse that she had a big project to finish and had to spend most of her time on that island.")
sh(46, "In truth, only her own conscience knew she was running from a bitter past. \"Won't you come even for your birthday, Malak?\"")
sh(47, "Zain asked in a disappointed voice. Moved by the feeling in his voice, Malak stood looking at him for a while.")
sh(48, "Was Zain really worried? Or was it a skilful act? Malak shrugged as if she didn't know.")
sh(49, "Zain went on talking. \"Even when you didn't come on my birthday, I didn't complain at all, did I?\"")
sh(50, "Before Zain had finished his sentence, anger took hold of Malak's heart. \"Only the noble have the right to complain! And besides,")
sh(51, "have you forgotten what disgusting thing you were doing that night? Haven't you even an atom of shame?\"", hum=True)
sh(52, "Malak cursed Zain in her heart. Then Zain started talking again. \"But you have to be on the island on your birthday.")
sh(53, "I've already arranged for the ring ceremony that night,\" Zain said. Hearing those words, Malak's head began to throb.")
sh(54, "She didn't want to marry anyone yet. Least of all Zain. \"I think it's still far too soon for that.")
sh(55, "And I need to think a lot... I'm going.\" After walking a little way, Malak stopped and looked back at Zain.")
sh(56, "\"On the night of your birthday, I did come... on the sixteenth of February.\" With that she went with quick steps and boarded the launch.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގައި", -22)], hum=True)
sh(57, "Not knowing what she meant, Zain was left standing there. \"She came to the island on the sixteenth of February — and went where?\"")
sh(58, "As he asked himself in bewilderment, the launch left with Malak. Ahlam,",
   [("boat_engine", "ލޯންޗު", -16)])
sh(59, "after sitting and staring at the small box in front of him, slowly opened it. Inside was an expensive branded wristwatch.",
   [("box_unlock", "ހުޅުވާލިއެވެ", -20)])
sh(60, "As he took the watch in his hand, a deep feeling stirred in a corner of his heart. \"A night that changed my whole life... the sixteenth of February...\"", hum=True)
sh(61, "Ahlam murmured softly. And the image of the unknown girl he had seen that night rose before his eyes.")
sh(62, "When that girl screamed in fear, Ahlam had put his hand over her mouth with the noble purpose of saving her life.",
   [("gasp", "ހަޅޭއްލަވައިގަތް", -20)])
sh(63, "Even though he didn't know who she was, Ahlam was sure she had no part in the murder that had taken place.")
sh(64, "If those evil people had known she was there, that innocent life would have become their prey too.")
sh(65, "But Ahlam could only lead the girl a short way. Before he could properly explain what had happened,")
sh(66, "the girl bit his hand and ran to escape. And she even threw a phone at him.",
   [("soft_thud", "އެއްލިއެވެ", -22)])
sh(67, "Ahlam picked up the phone and ran after the girl again. When he came out of the trees,",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(68, "the girl was lying fallen on the ground. In the dark it wasn't easy to tell who she was.",
   [("thunder", "ވެއްޓިފައެވެ", -18)])
sh(69, "Ahlam quickly stepped forward to help her. But, paying no attention to anything he said,")
sh(70, "the girl got up and ran. Picking up the bag lying on the ground, Ahlam looked inside it.",
   [("paper_shuffle", "ކޮތަޅު", -22)])
sh(71, "And after standing and looking in the direction she had run, he ran that way again with the bag.",
   [("footsteps_sand", "ދުއްވައިގަތެވެ", -20)])
sh(72, "Ahlam woke from those memories when his phone alarm began to ring. After switching off the alarm, he stroked the watch in his hand.",
   [("phone_buzz", "އެލާމް", -16)])
sh(73, "\"If I hadn't met this girl that night, I surely wouldn't be alive today. Where will I find her? If only we could meet even once.", hum=True)
sh(74, "Then I'd tell her everything about what happened on 16 February and the reason it happened.\" Letting out a deep breath, Ahlam put the watch back in its box,",
   [("sigh", "ނޭވާއެއް", -20)])
sh(75, "set it on the table and leaned back on the sofa. He had not come to that island only because he was the grandson of the resort's owner.",
   [("cloth_rustle", "ލެނގިލިއެވެ", -24)])
sh(76, "He came with lofty responsibilities on his shoulders as well. More than the name of the famous businessman \"Ahlam Umar\",")
sh(77, "the worth and honour of the stars shining on his chest in national service meant far more to him. His grandfather Hassan Waleed's greatest hope was")
sh(78, "that his only grandson would stay on and grow the family business. Even so, Ahlam chose the path his heart desired.")
sh(79, "He finished his studies and took his higher education in the field his grandfather wanted, but then, in the name of a holiday, he left his family for six months.")
sh(80, "His family gave him that chance too, hoping he would come back and join the business. But")
sh(81, "he did not come back only as Waleed's grandson. He came back as a loyal son serving the nation. Because it was his own decision,")
sh(82, "even Waleed found it hard to oppose. Ahlam's link with the national defence force has been kept secret for a special purpose.")
sh(83, "Outwardly, he is a young man running his grandfather's business. But in truth he is a secret agent holding a high rank in the military.")
sh(84, "So he does not yet want anyone to know his true identity. The end of the big mission he has begun still lies ahead.", hum=True)
SHOTS = S

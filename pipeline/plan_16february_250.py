"""Beat/shot plan for 16 February episode 250 (used by plan_beats.py).
The morning after 16 February: Kaif at the house, the ride to the jetty, the resort, the red file.
Rules: no falling man/body, no blood (also not on the handkerchief), no injuries on Malak, no touch between Malak and
any man (motorbike ride: she sits sideways behind with a clear gap), hijab on every woman, nobody lying down,
Naaif never shown, no readable text anywhere."""

LOC = {
    "building_site": "a cluster of three-storey half-built concrete guesthouses, bare columns and empty window holes, rusty rebar, overgrown with weeds, at the edge of the island near the trees",
    "family_house": "a single-storey coral-stone island house painted pale green, a sandy yard with a breadfruit tree, a wooden joali swing chair, a small veranda, tiled sitting room with a ceiling fan",
    "house_lane": "the sandy island lane just outside the gate of a single-storey coral-stone island house painted pale green, a low coral-stone boundary wall, a breadfruit tree leaning over the wall, coconut palms along the lane",
    "island_road": "a long sandy island road lined with tall trees and scattered street lamps, low coral-stone walls and houses behind the trees",
    "road_memory": "a long sandy island road lined with tall trees and scattered street lamps, low coral-stone walls and houses behind the trees",
    "jetty": "the island's concrete jetty with ferries and a white resort staff launch, turquoise water",
    "resort_pier": "the resort island's long wooden pier with a white staff launch moored alongside, turquoise lagoon water, white sand, coconut palms and a garden path leading inland towards low resort buildings",
    "souvenir_shop": "a small resort souvenir shop with a lit glass watch showcase, shells and sarongs on shelves",
    "shop_memory": "a small resort souvenir shop with a lit glass watch showcase, shells and sarongs on shelves",
    "garden_path": "a resort garden path of white sand between freshly watered tropical plants, hibiscus and palms, low white staff buildings with dark wooden doors",
    "resort_office": "an open-plan back-office of the resort, rows of wooden desks with monitors, glass-walled cabins, large windows to palms and sea; the boss's cabin with a dark wooden desk and a leather chair",
}
MOOD = {
    "building_site": "dark rainy night, lightning flashes, hazy desaturated memory, soft vignette; pouring rain, cold blue-white lightning against black sky, terror",
    "family_house": "bright tropical morning after a stormy night, soft slightly desaturated sunlight, damp sand in the yard, dappled shade from the breadfruit tree, uneasy tension under ordinary family warmth",
    "house_lane": "bright tropical morning, soft slightly desaturated sunlight, damp sand from last night's rain, palm shadows on the lane, awkward tension",
    "island_road": "bright tropical morning, soft slightly desaturated sunlight filtering through the trees, damp sand, a cool breeze, strained silence",
    "road_memory": "hazy, slightly desaturated memory with soft vignette; pale overcast afternoon light, a quiet aching estrangement",
    "jetty": "bright tropical morning, slightly desaturated turquoise and sand colours, sun glinting on the water, a light sea breeze, worry and loneliness",
    "resort_pier": "bright tropical morning at the resort, slightly desaturated turquoise and white, soft sea breeze, quiet unease",
    "souvenir_shop": "bright tropical morning outside, the shop interior dim with the glass showcase softly lit from inside, reflections on the glass, a frozen eerie stillness",
    "shop_memory": "hazy, slightly desaturated memory with soft vignette; warm soft showcase light, a quiet happy moment from a week ago",
    "garden_path": "bright tropical morning, slightly desaturated greens, dappled palm shade, sprinkler-wet leaves glistening, concern and nerves",
    "resort_office": "daytime office, cool white light from the large windows mixed with soft overhead lights, palms swaying outside, a calm ordinary office turning cold and ominous",
}

MALAK_DAY = "Malak in her wine-maroon kurta and black hijab pulled snugly low over her forehead, her face tired and pale"

BEATS = [
    # 1 — memory of 16 February night
    dict(to=2, reason="episode opening: Malak's memory of the night of 16 February (time jump to the past)", chars=["malak"], loc="building_site",
         visual="Malak running through dense wet bushes in the pouring rain at night, glancing back over her shoulder with wide horrified eyes, her maroon kurta and black hijab soaked dark with rain and still fully covering her hair and neck; behind her the dark half-built concrete guesthouse looms with an empty black upper floor, lit for an instant by a lightning flash; nobody else visible",
         camera="medium shot, slightly low angle, her face in the upper third, wet leaves and a puddle as the calm lower third",
         amb="memory_rain", transition="dissolve", sens="violence",
         safe="the man falling to his death is NOT shown: only Malak's terrified face lit by lightning and the dark empty upper floor of the building; the threat to her honour is shown only as her flight through the rain"),
    # 2 — Kaif arrives
    dict(to=4, reason="scene and time change: the next morning at the family house, Kaif the policeman walks in", chars=["kaif", "vimla"], loc="family_house",
         visual="Kaif in his dark-navy police uniform stepping into the sandy front yard, lifting the peaked cap off his head with one hand and smoothing his hair with the other; on the small veranda behind him Vimla in her mustard libaas and brown floral headscarf lights up with a happy, relieved smile",
         camera="medium wide, eye level, Kaif in the foreground left, Vimla on the veranda behind, the damp sand as the calm lower third",
         amb="island_house_day", transition="dissolve"),
    # 3 — Malak tries to leave
    dict(to=6, reason="characters change: Aanis smiles, Malak sighs and turns to walk out, Vimla calls her back", chars=["malak", "vimla", "aanis"], loc="family_house",
         visual=f"{MALAK_DAY}, stepping down from the veranda towards the gate with a deep tired breath, her shoulders tense; behind her on the veranda Vimla raises a hand calling her back; Aanis in his white skullcap and checked sarong sitting on the wooden joali in the yard, smiling warmly towards the gate",
         camera="medium wide, eye level, Malak in the foreground walking towards camera, the family behind", amb="island_house_day"),
    # 4 — face to face
    dict(to=10, reason="action change: Malak comes face to face with Kaif, who notices her face and starts asking questions", chars=["kaif", "malak"], loc="family_house",
         visual=f"Kaif holding his peaked cap in his hand, standing an arm's length and more away from Malak in the sandy yard, looking at her face with quiet concern; {MALAK_DAY}, half turned away from him, one hand at the edge of her hijab near her cheek, eyes guarded and wary",
         camera="medium two-shot, eye level, a clear gap between them, faces in the upper half",
         amb="island_house_day", sens="violence",
         safe="her swollen lip and bruised forehead are never shown: her face is turned slightly away, hijab low over the forehead, a hand at the hijab edge"),
    # 5 — wide: the argument, the family watching
    dict(to=13, reason="characters change: the wider family scene — Vimla puzzled, Aanis back on the joali with his phone — as Malak claims the bike was stolen", chars=["malak", "kaif", "vimla", "aanis"], loc="family_house",
         visual="wide view of the sandy front yard: Malak and Kaif facing each other at a respectful distance in the middle, Malak speaking with a cool indifferent tilt of her head, Kaif listening with his cap in hand; Vimla on the veranda watching them with a puzzled frown; Aanis sitting back on the wooden joali under the breadfruit tree reading his phone, the phone screen turned away from the viewer",
         camera="wide shot, eye level, all four figures in the upper two-thirds, sand as the calm lower third", amb="island_house_day"),
    # 6 — Kaif calm, Malak angry
    dict(to=17, reason="action change: Kaif calmly presses her, hand in pocket, cap in the other hand; Malak snaps at him angrily", chars=["kaif", "malak"], loc="family_house",
         visual=f"Kaif standing calm with his right hand in his trouser pocket and his peaked cap held in his left hand, eyes half closed in a patient sigh; facing him at a distance {MALAK_DAY}, her chin raised, eyes flashing with anger, one hand cutting the air",
         camera="medium two-shot over the yard, Kaif slightly closer to camera, a clear gap between them", amb="island_house_day"),
    # 7 — Kaif explains the murder
    dict(to=20, reason="emotional turning point: Kaif tells her a man was found murdered and her bike was seen there", chars=["kaif"], loc="family_house",
         visual="close-up of Kaif alone in the frame, in his dark-navy uniform, leaning slightly forward and speaking gently and earnestly towards someone just out of frame, his brows drawn together in worry, the peaked cap held against his chest; the green house wall and breadfruit leaves soft and blurred behind him; no other person visible",
         camera="close-up, eye level, his face in the upper third", amb="island_house_day"),
    # 8 — Malak lies
    dict(to=23, reason="focus moves to Malak: she lies that she has nothing to hide, frightened and determined to shut Kaif out", chars=["malak"], loc="family_house",
         visual=f"close-up of {MALAK_DAY}, her eyes lowered and sliding away, lips pressed tight, fingers twisting the long sleeve of her kurta down over her wrist; fear hidden behind a cold expression",
         camera="close-up, slightly from the side, face in the upper third", amb="island_house_day", hum=True),
    # 9 — Aanis asks; Malak slips away; Kaif stops her
    dict(to=27, reason="characters change: Aanis on the joali asks about the victim; Malak seizes the chance to walk out and Kaif stops her", chars=["aanis", "kaif", "malak"], loc="family_house",
         visual="Aanis in the foreground sitting on the wooden joali with his phone lowered, looking up and asking a question; Kaif turned half towards him, but holding up a firm hand towards the gate; in the background Malak frozen mid-step near the gate, her back half turned, glancing back over her shoulder",
         camera="medium wide, eye level, layered depth: Aanis front, Kaif middle, Malak at the gate", amb="island_house_day"),
    # 10 — Naaif
    dict(to=32, reason="characters change: Kaif walks in and asks Vimla where Naaif is; she answers too fast and Aanis glances at her", chars=["vimla", "kaif", "aanis"], loc="family_house",
         visual="on the small veranda Vimla answering Kaif too quickly with a nervous over-bright smile, her hands clasped tightly; Kaif standing at the veranda steps looking at her questioningly; Aanis on the joali in the yard turning his head towards Vimla with a knowing, suspicious look; a closed bedroom door visible inside the house behind her",
         camera="medium wide, eye level, faces in the upper half", amb="island_house_day", sens="other",
         safe="Naaif is only mentioned and never shown: just a closed door inside the house"),
    # 11 — Malak disappointed
    dict(to=34, reason="focus moves to Malak: she watches her mother's warmth towards Kaif with disappointment", chars=["malak", "vimla", "kaif"], loc="family_house",
         visual=f"{MALAK_DAY}, standing at the side of the yard with arms folded, watching with a disappointed hurt look; in the soft background Vimla warmly inviting Kaif in for tea and Kaif politely declining with his cap in hand",
         camera="medium shot, Malak sharp in the foreground, the others soft behind", amb="island_house_day"),
    # 12 — Aanis asks Kaif to drop her
    dict(to=39, reason="action change: Aanis asks Kaif to drop Malak at the jetty; she reluctantly agrees and Kaif heads out", chars=["aanis", "kaif", "malak"], loc="family_house",
         visual="Aanis on the joali gesturing kindly towards Malak; Kaif putting his peaked cap back on and glancing at Malak, unsure; Malak picking up her handbag with a resigned, stiff face, standing well apart from Kaif",
         camera="medium wide, eye level", amb="island_house_day"),
    # 13 — Kaif's suspicion
    dict(to=41, reason="emotional turning point: 'my phone is broken' — another mystery in Kaif's mind", chars=["kaif"], loc="family_house",
         visual="Kaif at the gate in his uniform and cap, turned back to look towards the house with narrowed thoughtful eyes, suspicion and worry on his face; morning light and breadfruit-leaf shadows across him",
         camera="close-up, slight low angle, face in the upper third", amb="island_house_day", hum=True),
    # 14 — Vimla and Aanis about the phone; Vimla's sorrow
    dict(to=47, reason="characters change: Vimla and Aanis argue about the broken phone; Vimla's sorrow at her daughter drifting away", chars=["vimla", "aanis"], loc="family_house",
         visual="Vimla standing on the veranda with her arms folded across her chest, shaking her head, looking sadly towards the gate where her daughter left; Aanis on the joali waving a calm dismissive hand at her; a small first-aid ointment tube in Vimla's hand",
         camera="medium shot, eye level, Vimla's face in the upper third", amb="island_house_day"),
    # 15 — outside: Malak refuses the bike
    dict(to=50, reason="scene change: outside the gate, Kaif on his motorbike, Malak refuses to get on", chars=["kaif", "malak"], loc="house_lane",
         visual="Kaif in uniform and cap sitting astride a plain dark motorbike in the sandy lane, looking back over his shoulder at Malak; Malak standing a few steps away on the lane with dark sunglasses, her handbag on her shoulder, arms crossed, refusing",
         camera="medium wide, eye level, a clear gap between them, sand lane as calm lower third", amb="island_day"),
    # 16 — the ride
    dict(to=55, reason="action change: the ride to the jetty — Malak sits sideways behind him, Kaif asks about her lip", chars=["kaif", "malak"], loc="island_road",
         visual="Kaif riding the motorbike slowly along the tree-lined sandy road, his eyes glancing up to the small round mirror; Malak seated sideways on the rear of the seat with a clear gap between them, holding the rear seat rail with one hand, dark sunglasses on, turned away with an annoyed closed face; no contact between them",
         camera="medium wide, three-quarter front view from the roadside, both faces in the upper half, the sandy road as calm lower third",
         amb="island_day", sens="intimacy",
         safe="no touch between Malak and Kaif: she sits sideways behind with a clear gap, holding the seat rail"),
    # 17 — Kaif hurt
    dict(to=57, reason="emotional turning point: Kaif is hurt by her words", chars=["kaif"], loc="island_road",
         visual="close-up of Kaif riding, his eyes lowered in the small round motorbike mirror, a hurt, resigned expression as he exhales a long sigh; blurred trees and dappled light behind",
         camera="close-up, face in the upper third", amb="island_day", hum=True),
    # 18 — jetty, limping
    dict(to=59, reason="scene change: the jetty — Malak walks to the staff launch, Kaif sees her careful step", chars=["malak", "kaif"], loc="jetty",
         visual=f"Malak in her wine-maroon kurta, black hijab and dark sunglasses walking away along the concrete jetty towards the white staff launch with a slow careful step; in the foreground Kaif sitting on his parked motorbike watching her with worry; a ferry pulling away from the harbour in the background",
         camera="wide, from behind Kaif's shoulder, Malak small in the middle distance, the turquoise water and jetty as calm lower third",
         amb="jetty_day", sens="violence", safe="her limp is shown only as a slow careful step seen from a distance"),
    # 19 — Kaif alone
    dict(to=62, reason="characters change: Malak has gone; Kaif alone watching the launch disappear, remembering their closeness", chars=["kaif"], loc="jetty",
         visual="Kaif sitting alone on his parked motorbike at the end of the jetty, cap in his lap, looking out to sea where the white launch is a small speck on the turquoise water, a lonely sad expression",
         camera="medium wide from the side, his face in the upper third, water as the calm lower third", amb="jetty_day"),
    # 20 — memory: estrangement on the road
    dict(to=64, reason="memory: the two have become strangers — she passes him on the road with her head bowed", chars=["malak", "kaif"], loc="road_memory",
         visual="on the tree-lined island road, Malak in her maroon kurta and black hijab walking past with her head bowed, not looking; Kaif in a casual light-blue shirt a few metres away turning to look after her with a hopeful, hurt face; wide empty space between them",
         camera="medium wide, eye level, both faces in the upper half", amb="memory", transition="dissolve", hum=True),
    # 21 — back at the jetty, phone call
    dict(to=66, reuse="beat_019", reason="return from the memory to Kaif at the jetty; his phone rings and he leaves", loc="jetty",
         visual="(reuse)", amb="jetty_day", transition="dissolve"),
    # 22 — resort pier
    dict(to=67, reason="scene change: the launch arrives at the resort and Malak walks towards the office", chars=["malak"], loc="resort_pier",
         visual="the white staff launch alongside the wooden pier, resort staff in sand-beige uniforms stepping off; Malak in her wine-maroon kurta, black hijab and sunglasses walking ahead alone along the pier, looking at no one",
         camera="wide, eye level, Malak in the upper middle, the pier boards and water as the calm lower third", amb="resort_day"),
    # 23 — souvenir shop
    dict(to=70, reason="scene and character change: Malak stops at the souvenir shop showcase; Ubey inside freezes", chars=["malak", "ubey"], loc="souvenir_shop",
         visual="Malak standing still outside the souvenir shop's glass front, sunglasses pushed up, staring through the glass at the softly lit watch showcase; inside behind the showcase Ubey in his teal staff shirt has stopped wiping the glass with a cloth and stares back at her, frozen; faint reflections on the glass; the watches have plain dials",
         camera="medium shot, eye level, Malak in the foreground right, Ubey behind the glass on the left, faces in the upper half", amb="shop_day"),
    # 24 — memory: the watch in the black box
    dict(to=72, reason="memory: the watch taken from that showcase and placed in a black box", loc="shop_memory",
         visual="extreme close-up of only two hands, no faces and no people visible: a man's hand in a teal shirt cuff laying a modern silver wristwatch with a plain blank dial and no markings into an open black gift box lined with black satin, on top of a softly lit glass showcase counter; blurred warm shop lights behind",
         camera="close-up, slightly high angle, the box in the upper half, the glass counter as calm lower third",
         amb="memory", transition="dissolve"),
    # 25 — startled by Mizoo
    dict(to=75, reason="action change: someone taps her shoulder — Malak screams 'Mamma!'; it is Mizoo", chars=["malak", "mizoo"], loc="souvenir_shop",
         visual="outside the souvenir shop Malak spinning round in terror, one hand pressed to her chest, eyes wide; Mizoo in her teal hijab and sand-beige staff uniform right behind her with her hand still raised from tapping her shoulder, surprised and apologetic",
         camera="medium two-shot, eye level, faces in the upper half", amb="resort_day", transition="dissolve"),
    # 26 — Mizoo's concern
    dict(to=80, reason="action change: Mizoo sees her face, Malak admits to 'a small accident'; Mizoo insists on treatment", chars=["mizoo", "malak"], loc="garden_path",
         visual="on the resort garden path Mizoo with a hand on Malak's back, looking at her with worried eyes; Malak tugging the long sleeve of her kurta down over her wrist, her face turned slightly away, explaining with a tired shrug; the two women walking slowly side by side",
         camera="medium two-shot, eye level, faces in the upper half, the white sand path as calm lower third",
         amb="resort_day", sens="violence",
         safe="her bruised arm and face are never shown: the sleeve stays pulled down over her wrist, her face half turned"),
    # 27 — office arrival
    dict(to=82, reason="scene change: after the clinic, Malak enters the back-office and sits at her desk; Mizoo goes to the front office", chars=["malak", "mizoo"], loc="resort_office",
         visual="Malak sitting down at her wooden desk in the open-plan office, putting her bag down, her face tired and pale; at the glass doorway in the background Mizoo giving a small wave as she leaves for the front office",
         camera="medium wide, eye level, Malak's face in the upper half, the desk top as calm lower third", amb="office_day"),
    # 28 — the red file
    dict(to=83, reason="action change: a blank red file lies on her desk; she opens it with curiosity", chars=["malak"], loc="resort_office",
         visual="close view across the desk: a plain red folder with no writing on it lying on the wooden desk, Malak's hands with the slim silver watch opening its cover, her curious face above, leaning in",
         camera="medium close-up, slightly high angle, the folder in the middle, her face in the upper third", amb="office_day"),
    # 29 — the shock
    dict(to=86, reason="emotional turning point: the handkerchief inside — she throws the file and cannot scream", chars=["malak"], loc="resort_office",
         visual="Malak recoiling back in her office chair, both eyes wide with horror, her own hand clamped over her mouth, breath caught; in the foreground on the desk, seen from a distance, the red folder lying open with a crumpled dark cloth inside; no stains, nothing graphic",
         camera="medium shot, eye level, her face in the upper third, the desk top with the folder in the lower part",
         amb="office_day", hum=True, sens="violence",
         safe="the blood-soaked handkerchief is shown only as a crumpled DARK cloth in an open red folder seen from a distance; no blood or stains"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Remembering the man who had fallen dead from the top of the guest house, fear showed on her face. Her heart began to race.",
   [("thunder", "ވެއްޓުނު", -16), ("heartbeat", "ވިންދު", -18)], hum=True)
sh(2, "And she remembered how she had run through the darkness, through the pouring rain and the bushes, to save her honour.",
   [("leaves_rustle", "ބޯގަސް", -22), ("footsteps_sand", "ދުވި", -20)], hum=True)
sh(3, "The police boy who came in walked forward, took the cap off his head and smoothed his hair.",
   [("footsteps_sand", "ވަދެގެން", -24), ("cloth_rustle", "ތޮފި", -24)])
sh(4, "He was a young man of good height and an ordinary fair complexion. Seeing the young man, happiness showed on Vimla's face.")
sh(5, "The smile on her lips was proof enough that she was relieved. Aanis too smiled happily. Malak took a deep breath and started to walk out.",
   [("sigh", "ފުންނޭވާ", -22)])
sh(6, "She seemed to feel that she was not needed. \"Malak, dear, wait a moment. Mum still has something to talk about.\"")
sh(7, "Vimla said quickly. By then Malak had come face to face with the young man. He looked at Malak with concern.")
sh(8, "The swelling on her lip and the bruise on her forehead caught his eye too. \"What time did Malak come home last night?\"")
sh(9, "the young man asked in a very ordinary way. \"Kaif doesn't need to check on that,\" Malak said in an ordinary tone. \"I'm not asking because I have to.")
sh(10, "It's because Malak's motorbike was seen last night somewhere it shouldn't have been.\" Kaif spoke softly. Malak kept looking at Kaif with worry.")
sh(11, "Not knowing what the two of them were talking about, Vimla watched. Meanwhile Aanis sat back on the joali and went on reading the news on his phone.")
sh(12, "\"My motorbike was stolen last night, I don't know if you'll believe it. I even reported it to the police — don't you check those reports?\"")
sh(13, "Malak asked in a careless tone. \"When did you find out the bike was stolen? Why didn't you call me?\"")
sh(14, "Kaif asked calmly, slipping his hand into his right pocket. His cap was in his left hand. \"After I came back from the resort.")
sh(15, "It wasn't by the jetty, so I reported it to the police,\" Malak said. \"Why didn't you call me?\" Kaif asked.")
sh(16, "\"Do I call Kaif every time something happens? Or do I have to?\" Malak snapped angrily in a harsh tone.")
sh(17, "Kaif took a deep breath and closed his eyes. He didn't know why Malak was so angry. He believed it was a question that had to be asked.",
   [("sigh", "ފުންނޭވާ", -22)])
sh(18, "\"Malak. Do you know why I'm asking this? Last night someone was found murdered.")
sh(19, "It's known that Malak's motorbike travelled in that area. Tomorrow the police will come to question Malak too. That's why. Tell me without hiding anything.\"")
sh(20, "Kaif showed his concern. He spoke to Malak gently, with patience. He did not want to make Malak angry.")
sh(21, "\"If there were anything worth telling, I'd tell you. There's nothing I need to hide.\" Malak hid the truth. Having to lie frightened her too.",
   hum=True)
sh(22, "But she chose to stay silent because she did not want to drag her mother and the family into that worry.")
sh(23, "Above all, she did not want Kaif to know. She did not want to share anything of hers with Kaif.")
sh(24, "\"Son, Kaif — the one killed on this island last night wasn't from this island, was he?\" Aanis asked, reclining with the news on his phone. Kaif looked at Aanis.")
sh(25, "Malak quickly started to walk out, seeing it as a chance she'd been given. Instead of answering Aanis, Kaif made Malak stop.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(26, "\"Malak, wait a moment. I haven't finished talking.\" This time there was firmness in Kaif's voice. Malak didn't dare go on.")
sh(27, "Telling Malak to come back in, Kaif began talking to Aanis. \"Yes, Bappa. He wasn't from this island. But he's known to be the child of a high-ranking family.")
sh(28, "Whose, the name hasn't been released yet,\" Kaif said, walking inside. \"Daththa, where's Naaif?\" Kaif asked, looking at Vimla.",
   [("footsteps_sand", "ހިނގައިގަންނަމުން", -24)])
sh(29, "\"He's asleep,\" Vimla said. \"Did Naaif go out last night?\" Kaif asked. \"No, no.")
sh(30, "Naaif came home very early last night and went to sleep,\" Vimla said quickly. Because Vimla answered so fast, Aanis looked at her.")
sh(31, "It was as if Aanis knew Vimla was lying. \"Son, why are you looking for your little brother?\" Aanis asked. \"Just checking where he is.")
sh(32, "I haven't seen him for many days,\" Kaif said. \"Have some tea before you go. How many days since you came home!\" Vimla said warmly.")
sh(33, "Malak looked at her mother. The warm way her mother talked to Kaif did not sit well with her. Disappointment showed on her face. \"No, Daththa.")
sh(34, "Not now. I'm on my way to the station. I'll come another time. Tell Naaif I came looking for him. Tell him to call me,\" Kaif said.")
sh(35, "Vimla agreed. \"Bappa, I'll go for now. I'll come again later,\" Kaif said. \"Yes... Son, drop Malak at the jetty on your way, will you.")
sh(36, "I don't think Malak has even had her tea yet,\" Aanis said. Kaif looked at Malak.")
sh(37, "There was little certainty that Malak would go with him. Against her heart, Malak decided to go with Kaif.")
sh(38, "She did not want to spoil the peace of the household. Kaif noticed the change of colour on Malak's face.")
sh(39, "Even so, he too did not want to brush aside his father's wish. Saying 'come on', he walked out. \"Bebe, I'm going. Mamma, I'm going.",
   [("footsteps_sand", "ހިނގައިގަތެވެ", -22)])
sh(40, "Don't call my phone — it's broken,\" Malak said as she went out. When she mentioned the phone, Kaif looked at Malak. Another 'mystery'.")
sh(41, "It struck Kaif's mind. The motorbike seen where a man had died, Malak's broken phone, the marks on her forehead and lip — they seemed to tell many stories.",
   hum=True)
sh(42, "He found it hard to believe what Malak said. \"What happened to the phone? It was bought only last month. Why did it break so soon?\"")
sh(43, "Vimla asked in surprise. \"Vimla...\" Aanis said in a tone that made light of it. \"Come on, things can break.")
sh(44, "Don't make such a big deal of it. That girl works to earn the things she buys. Don't you worry about it, Vimla. Let the two kids go quickly,")
sh(45, "or Malak might not make it to the resort,\" Aanis said. Vimla shook her head and folded her arms across her chest.",
   [("cloth_rustle", "އަތްޖަހާލިއެވެ", -24)])
sh(46, "She had even wanted to put some medicine on the wound on Malak's forehead. But Vimla knew the stubborn girl would brush that aside too.")
sh(47, "Malak had become so different from before. The old closeness was gone. She didn't know what had happened. She and her daughter had drifted apart.",
   hum=True)
sh(48, "Vimla let out a disappointed sigh. Outside, Kaif got onto his motorbike and settled. Malak stood waiting without getting on.",
   [("sigh", "އަޑެއް", -22)])
sh(49, "Seeing that Malak hadn't got on, Kaif looked at her. \"Go on, Kaif. I'll take a taxi,\" Malak said before Kaif could say anything.")
sh(50, "\"I won't eat you, Malak. Get on. Calling a taxi will take time too — the launch leaves at a fixed time, doesn't it?\"")
sh(51, "Kaif said in an ordinary tone. What Kaif said was true. Reluctantly, Malak got on behind Kaif. Kaif started the motorbike and looked at Malak in the mirror.",
   [("engine_rev", "އިސްޓާޓް", -16)])
sh(52, "What showed on Malak's face was annoyance. \"What's happened to your lip?\" Kaif asked. No answer came from Malak.")
sh(53, "She didn't seem to want to talk to Kaif. Kaif repeated the question. \"I fell.\" Malak's answer was short. \"Fell? Where?\"")
sh(54, "Kaif asked a second question. \"Don't you know I don't have to answer every question Kaif asks? You're not my brother or my father.")
sh(55, "And you're not my boyfriend either,\" Malak said, stressing her words. It showed on his face that it had hurt Kaif.",
   hum=True)
sh(56, "He let out a deep, disappointed sigh. \"I know that. But I ask because I worry about you, Malak,\" Kaif said in a quiet tone.",
   [("sigh", "ފުންއާހް", -22)])
sh(57, "\"It'd be better if you didn't worry,\" Malak said in a fed-up tone. When they reached the jetty, Malak got off the motorbike and went towards a launch.")
sh(58, "As Malak walked away, Kaif, sitting on the motorbike watching her, noticed that she was limping slightly.",
   [("footsteps_pavement", "ހިނގައިފައި", -24)])
sh(59, "He was certain something big had happened to Malak last night. Malak went and boarded the launch. Just then the ferry she had come on last night was also leaving the harbour.",
   [("boat_engine", "ފަޅުން", -18)])
sh(60, "Kaif sat there until the launch was out of sight. Malak was his stepmother's daughter. The two of them had grown up together.",
   [("boat_engine", "ލޯންޗު", -22)])
sh(61, "Lately, because of the change that had come over Malak, Kaif was saddened. The close friendship of before, the fun,")
sh(62, "the long phone calls that went on for hours without either tiring — all of it had stopped. Slowly Malak had begun to drift away from Kaif.")
sh(63, "Living in the same house, the two had become strangers. Even if they met on the road, she would bow her head and walk on, as if she didn't see him.",
   hum=True)
sh(64, "Even when Kaif sent a message to ask how she was, Malak's reply came very short and careless.")
sh(65, "She had pushed him out of her life without any warning. He let out a disappointed sigh.",
   [("sigh", "ފުންނޭވާ", -22)])
sh(66, "When the phone in his pocket began to ring, Kaif took it out and answered. Saying he was on his way, he cut the call short.",
   [("phone_buzz", "ރިންގުވާން", -16)])
sh(67, "When the launch came alongside the pier, Malak got off with the other staff. Without looking at anyone, she headed towards the office where she worked.",
   [("boat_engine", "ލޯންޗު", -22), ("footsteps_pavement", "ފޭބިއެވެ", -24)])
sh(68, "Malak's slow steps suddenly stopped as she reached the souvenir shop. Through the shop's dim light,",
   [("footsteps_pavement", "ހިނގަމުން", -24)])
sh(69, "her gaze went straight to the big glass showcase inside. At that moment the shop boy was wiping the showcase clean with a cloth.",
   [("cloth_rustle", "ފޮހެ", -24)])
sh(70, "But when he saw Malak standing outside the glass, staring in with a deep gaze, the boy's movements stopped completely. In that instant,")
sh(71, "an old memory came alive in Malak's mind. The modern branded watch taken out of that showcase,")
sh(72, "the scene of it being placed in a black box, came back as vividly as if it had just happened before her eyes.",
   [("box_unlock", "ފޮށްޓަކަށް", -22)])
sh(73, "Malak's heart nearly stopped when someone tapped her on the shoulder from behind. \"Mamma!\" Utterly startled,",
   [("gasp", "މަންމާ", -14), ("heartbeat", "ހިތް", -18)])
sh(74, "Malak screamed out in fear. The terror and fright that showed on her face at that moment,")
sh(75, "made it look as if she were facing a danger she had never imagined. \"It's me,\" said her friend Mizoo. Malak stood with her hand on her chest.",
   [("breath_heavy", "މޭގައި", -22)])
sh(76, "\"Sorry!\" Malak said in a shaky voice. \"What happened to your forehead? Your lip is swollen too.\"")
sh(77, "Mizoo said, touching Malak's back. \"I had a small accident last night,\" Malak said, rolling up the sleeve of her long-sleeved kurta.")
sh(78, "Her arm was badly bruised. Mizoo clicked her tongue against her teeth as she spoke. \"Ya Rabbee...")
sh(79, "Come, let's get it treated. Why didn't you go to the hospital when it's this bad?\" Mizoo said with concern. \"You know how Mum is — she'd make a huge thing of it,")
sh(80, "and that Kaif would be there to back Mum up. So I didn't tell, because I didn't want to worry Mum,\" Malak said as she walked on with Mizoo.",
   [("footsteps_pavement", "ދަމުން", -24)])
sh(81, "After getting treated at the resort clinic, Mizoo and Malak came to the office. When Malak went into the office, Mizoo walked off to where she works.",
   [("door_open", "ވަނުމުން", -22)])
sh(82, "Mizoo works at the front office. Malak went into the office, sat down at her desk and settled. When Malak glanced over the desk,")
sh(83, "there was a red file lying on it. There was no writing on the outside. Curious, she picked up the file and opened it.",
   [("paper_shuffle", "ހުޅުވާލިއެވެ", -20)])
sh(84, "Malak's whole body seemed to freeze. Inside the file lay a handkerchief smeared with fresh blood! The blood on it still looked wet.",
   [("heartbeat", "ގަނޑުވި", -16)], hum=True)
sh(85, "At the same moment a foul smell spread through the whole place. Her eyes wide, she flung the file from her hand. In fear she gasped.",
   [("soft_thud", "ހޫރާލިއެވެ", -16), ("gasp", "ދާހިތްލާލިއެވެ", -18)], hum=True)
sh(86, "Her heart raced and her breath came short. She tried to scream, but no sound came out of her throat.",
   [("heartbeat", "ވިންދު", -18), ("breath_heavy", "ނޭވާ", -20)], hum=True)
SHOTS = S

"""Beat/shot plan for Yaraa episode 573 (series opener; used by plan_beats.py)."""

LOC = {
    "male_dawn": "the sea off Male at sunrise: the dense skyline of Male's tall pastel buildings across a calm glassy turquoise harbour, a few moored wooden dhonis and speedboats, a long concrete jetty in the foreground, the sun just risen over the horizon",
    "jetty": "a Male jetty in the early morning: a concrete quay edge with old tyres as fenders, a small white open fibreglass dinghy with an outboard engine bobbing alongside on calm turquoise water, a couple of cool-boxes and picnic bags on the quay, Male's pastel buildings softly blurred behind",
    "open_sea": "the open sea between Male and the outer islands on a dead-calm day: a vast glassy turquoise sea, a perfectly clear cloudless sky, the small white open dinghy cutting a long white wake",
    "dinghy": "inside the small white open fibreglass dinghy on the calm sea: two padded bench seats one behind the other, picnic bags at their feet, the outboard engine at the stern, glittering turquoise water and a clear sky all around",
    "arrival": "a beautiful uninhabited Maldivian island seen from the sea as the dinghy approaches: a dazzling silver-white sand beach curving around turquoise shallows, behind it a dense overgrown jungle of tall coconut palms, screw-pines and dark green magoo shrubs, no buildings, no people",
    "beach_ridge": "the beach of the deserted island: a shady line of leafy trees and magoo shrubs along the low sandy beach ridge, picnic bags and a cool-box left in the shade, the dazzling white beach sloping down to clear turquoise shallows, dense jungle behind",
    "beach_walk": "the long empty white beach of the deserted island: deep soft powdery sand with footprints, gentle turquoise waves lapping on the right, the green wall of coconut palms and screw-pines on the left, the island's narrow sandy tip ahead",
    "sandspit": "the narrow tip of the deserted island (thundi): a long tongue of dazzling white sand reaching out into a shallow glittering turquoise lagoon, open sea on both sides, a few windswept coconut palms at its base, a vast sky",
    "magoo_shade": "the deep shade of a big wind-shaped magoo bush on the beach ridge of the deserted island: a woven coconut-leaf mat spread on the cool sand under its low twisted branches, dappled light, the bright white beach and turquoise sea glittering beyond",
    "male_office": "Faisal's small modern office in Male: a desk with a closed laptop and a few plain folders, a window behind showing a blurred view of Male's dense pastel buildings and a sliver of sea, a potted plant, soft daylight",
    "jungle_edge": "the beach ridge of the deserted island at the edge of the dense jungle: the magoo bush, tall coconut palms and screw-pines, a narrow sand path disappearing into dark green undergrowth",
    "black_cloud": "the deserted island's jungle seen from the beach: an empty narrow sand path disappearing between dense coconut palms and screw-pines into deep green shadow, above the canopy an enormous towering black cloud rising and spreading across the sky, swaying fronds, nobody anywhere",
    "beach_hurry": "the long empty white beach of the deserted island under a darkening sky: long slanting palm shadows across the sand, the jungle a dark wall on one side, the turquoise sea on the other, the small white dinghy pulled up on the sand far ahead",
    "landing": "the landing place on the deserted island beach: the small white open dinghy pulled up on the wet sand at the waterline, picnic bags in the shade of the trees on the ridge, the jungle behind, a big dark cloud spreading over part of the sky",
    "pond_path": "a narrow white sand path leading from the beach ridge into the dense jungle of the deserted island towards an inland pond: tall coconut palms and screw-pines closing overhead, thick tall grass on either side, dappled green light fading into shadow ahead",
}
MOOD = {
    "male_dawn": "calm clear Eid-holiday morning, soft golden sunrise light on the water, peaceful and fresh, a faint warm haze",
    "jetty": "calm sunny morning, clear sky, sparkling turquoise water, bright and cheerful with a quiet tender undertone",
    "open_sea": "calm sunny morning, dazzling sunlight, perfectly clear sky without a single cloud, glassy sea, carefree",
    "dinghy": "calm sunny morning, bright warm sunlight, cool sea breeze, sparkling reflections, playful and romantic",
    "arrival": "bright late-morning sun, glittering sea, crystal-clear air, a sense of wonder at untouched beauty",
    "beach_ridge": "bright late-morning sunlight, cool green shade under the trees, cheerful holiday mood",
    "beach_walk": "bright late-morning sunlight, warm golden glow on the sand, tender and joyful",
    "sandspit": "golden noon sunlight, brilliant glittering sea, strong sea wind, radiant, free and joyful",
    "magoo_shade": "golden noon, cool dappled green shade against the blazing white beach, tender, warm and intimate",
    "male_office": "bright daytime office light, cool neutral tones, friendly and teasing",
    "jungle_edge": "early afternoon, green jungle shade, the light dimming as a cloud shadow falls, quietly unsettling",
    "black_cloud": "early afternoon, the sun swallowed by an enormous black cloud, cold grey-green light over the jungle, ominous stillness, eerie and frightening",
    "beach_hurry": "early afternoon, dim grey light under the spreading black cloud, long dark palm shadows, anxious and uneasy",
    "landing": "early afternoon, patchy light, half the sky still blue and half darkened by a black cloud, uneasy calm",
    "pond_path": "early afternoon, green jungle shade, dim and still under the cloud, quietly unsettling, foreboding",
}

HIJAB_Y = "her black hijab fully covering her hair and neck"
HIJAB_S = "her white hijab fully covering her hair and neck"

BEATS = [
    dict(to=2, reason="episode opening: a calm clear Eid-holiday morning dawns over Male", loc="male_dawn",
         visual="a calm wide establishing view of Male at sunrise across the glassy harbour: the golden sun just above the horizon, a warm path of light on the still turquoise water, the pastel skyline of Male soft in the morning haze, a few moored wooden dhonis, a long empty concrete jetty leading into the picture; no people, no lettering on any boat",
         camera="wide establishing shot, eye level, sun and skyline in the upper two-thirds, the calm water and jetty as the lower third",
         amb="jetty_day"),
    dict(to=4, reason="characters introduced: Naveen and Shifza, the couple who faced hard trials and lost their first baby", chars=["shifza", "naveen"], loc="jetty",
         visual=f"Naveen in his navy polo and grey cargo trousers and Shifza in her mint-green long dress with {HIJAB_S} standing side by side on the sunny quay beside the moored dinghy; Naveen holds a cool-box with a warm brave smile, Shifza looks out to sea with a soft wistful smile and a trace of old sadness in her eyes, her hand resting on Naveen's arm; picnic bags at their feet; no child anywhere",
         camera="medium wide, eye level, faces in the upper two-thirds, the sunlit quay and water as the lower third",
         amb="jetty_day", sens="other", safe="their lost first baby is only spoken about; no child or baby is shown, only Shifza's wistful gaze to the sea"),
    dict(to=5, reason="characters change: introducing the newlyweds Mifzaal and Yaraa, married only three days", chars=["mifzaal", "yaraa"], loc="jetty",
         visual=f"Mifzaal in his white linen shirt with rolled sleeves and beige chinos and Yaraa in her loose crimson long dress with {HIJAB_Y} standing side by side on the quay holding hands, about to step down into the dinghy; Mifzaal carries a picnic bag over his shoulder and smiles down at her proudly, Yaraa smiles shyly with lowered eyes, radiant; the morning sun glows on their faces",
         camera="medium shot, eye level, faces in the upper two-thirds, the quay edge and water as the lower third",
         amb="jetty_day"),
    dict(to=6, reason="action/scene change: the four set out in the dinghy on a dead-calm sea under a cloudless sky", chars=["mifzaal", "yaraa", "naveen", "shifza"], loc="open_sea",
         visual=f"a high wide view of the small white open dinghy speeding across a vast glassy turquoise sea leaving a long white wake; four small figures aboard: Naveen at the outboard tiller in his navy polo, Shifza in mint green with {HIJAB_S} on the front bench, Mifzaal in white and Yaraa in crimson with {HIJAB_Y} side by side on the back bench; a perfectly clear cloudless sky; Male a faint line on the horizon; the hull plain white with no lettering",
         camera="wide aerial three-quarter view, the boat in the upper-middle third, open sea and sky around, calm water as the lower third",
         amb="sea_boat"),
    dict(to=8, reason="action change: close on the newlyweds on the back seat holding hands, her hijab fluttering in the breeze", chars=["yaraa", "mifzaal"], loc="dinghy",
         visual=f"Mifzaal and Yaraa sitting close side by side on the back bench of the dinghy, their hands clasped together with fingers interlaced resting on his knee; Yaraa in her crimson long dress with {HIJAB_Y}, the loose end of her black hijab fluttering in the sea wind near his shoulder, both smiling contentedly at the sea; sunlight sparkling on the water behind them",
         camera="medium close two-shot, eye level, faces in the upper two-thirds, their clasped hands and the boat bench in the lower third",
         amb="sea_boat", sens="intimacy",
         safe="married couple only sitting side by side holding hands; her 'shining hair blowing on his face' and head on his shoulder become the end of her black hijab fluttering near his shoulder"),
    dict(to=10, reason="dialogue: Naveen, on the front bench, turns round to tease Yaraa (speaker focus)", chars=["naveen", "shifza", "yaraa", "mifzaal"], loc="dinghy",
         visual=f"Naveen in his navy polo sitting on the front bench, turned round towards the camera, grinning broadly and pointing teasingly with one finger, eyebrows raised; Shifza beside him in mint green with {HIJAB_S} laughing softly; in the soft-focus foreground the backs of Mifzaal's and Yaraa's heads and shoulders (her black hijab fully covering her hair) on the back bench; glittering sea behind",
         camera="over-the-shoulder medium shot from behind the back bench, Naveen centred and sharp in the upper half, the couple blurred in the foreground",
         amb="sea_boat"),
    dict(to=11, reason="dialogue: Shifza speaks, asking Mifzaal whether he has nothing to say (speaker focus)", chars=["shifza", "naveen"], loc="dinghy",
         visual=f"Shifza in her mint-green long dress with {HIJAB_S} sitting on the front bench, turned towards the camera, speaking gently with a playful questioning smile and one hand lifted, palm up; Naveen beside her softer and out of focus, still grinning; bright sea and sky behind",
         camera="medium close-up, eye level, Shifza centred and sharp in the upper half, Naveen soft at the side",
         amb="sea_boat"),
    dict(to=14, reason="dialogue: Mifzaal answers that he gave his whole heart to his queen; everyone laughs (speaker focus)", chars=["mifzaal", "yaraa"], loc="dinghy",
         visual=f"Mifzaal sitting on the back bench speaking with a warm theatrical smile, one hand on his heart, the other holding Yaraa's hand; Yaraa sitting beside him in her crimson dress with {HIJAB_Y}, laughing shyly and looking down, her cheeks glowing; bright sunlight, sparkling sea and clear sky behind",
         camera="medium shot from the front bench, eye level, Mifzaal centred and sharp in the upper half, Yaraa beside him",
         amb="sea_boat"),
    dict(to=15, reason="scene change: time passes and the dinghy reaches a beautiful deserted island", loc="arrival",
         visual="point of view from inside the small white dinghy as it glides in: only the plain white pointed bow tip and a coiled rope in the bottom foreground, crystal-clear turquoise shallows over white sand, and ahead a dazzling silver-white beach backed by a dense overgrown jungle of tall coconut palms, screw-pines and dark magoo shrubs; brilliant sun, clear sky; no people visible at all, no buildings, no lettering",
         camera="wide point-of-view shot from the boat, the island and jungle in the upper two-thirds, the clear shallows and bow as the lower third",
         amb="sea_boat"),
    dict(to=17, reason="scene/action change: bags left in the shade; Mifzaal leads Yaraa towards the island's tip while Naveen and Shifza play in the shallows", chars=["mifzaal", "yaraa", "naveen", "shifza"], loc="beach_ridge",
         visual=f"on the bright beach Mifzaal and Yaraa ({HIJAB_Y}, crimson long dress) walk side by side holding hands along the waterline towards the far tip of the island, seen from behind and to the side; in the background Naveen in his navy polo and Shifza in mint green with {HIJAB_S} wade knee-deep fully clothed in the turquoise shallows, laughing and splashing water at each other, small in the distance; picnic bags in the shade of the trees on the ridge",
         camera="wide shot, eye level, the figures in the middle third, the white sand as the lower third",
         amb="beach_day", sens="clothing", safe="'playing in the sea' shown as wading knee-deep fully clothed, splashing water, seen from a distance"),
    dict(to=19, reason="action change: walking in the soft sand, Yaraa stumbles and Mifzaal steadies her", chars=["yaraa", "mifzaal"], loc="beach_walk",
         visual=f"Yaraa in her crimson long dress with {HIJAB_Y} stumbling a little in the deep soft sand, laughing, holding her hem slightly with one hand; Mifzaal walking side by side with her, holding her other hand firmly to steady her, smiling tenderly; their bare feet sinking into the powdery white sand; turquoise waves glittering beside them",
         camera="medium wide, slightly low angle, faces in the upper two-thirds, the deep soft sand and footprints as the lower third",
         amb="beach_day", sens="intimacy", safe="'holding her by the shoulders' becomes him holding her hand to steady her"),
    dict(to=21, reason="action change: at the tip she lets go of his hand and runs barefoot across the white sand", chars=["yaraa", "mifzaal"], loc="sandspit",
         visual=f"Yaraa running barefoot away from the camera across the dazzling white sand spit towards the glittering sea, in her loose flowing ankle-length crimson long-sleeved dress with {HIJAB_Y}, the dress and hijab end streaming in the wind; Mifzaal walking slowly behind her in the foreground at the side, seen from behind, watching her with a happy smile",
         camera="medium-wide from behind and to the side, figures in the upper-middle, the white sand as a calm lower third",
         amb="beach_day", sens="clothing",
         safe="the 'red swimming dress' and her figure are never shown: she wears her normal loose crimson long dress and hijab, seen running from behind, no body shape described"),
    dict(to=23, reason="action change: Yaraa stops at the very tip, spreads her arms in the wind and beckons Mifzaal", chars=["yaraa"], loc="sandspit",
         visual=f"Yaraa standing at the very end of the sand spit, turned back towards the camera, her arms spread wide in the strong sea wind, beckoning with one hand and laughing freely; her loose crimson long dress and {HIJAB_Y} rippling in the wind; glittering turquoise lagoon and open sea all around, brilliant sky",
         camera="medium-wide, eye level, her face in the upper third, the wet shining sand and lapping water as the lower third",
         amb="beach_day", sens="clothing", safe="loose modest long dress and hijab; no body emphasis"),
    dict(to=25, reason="emotional peak: the two together at the tip in the golden sun", chars=["yaraa", "mifzaal"], loc="sandspit",
         visual=f"Mifzaal and Yaraa standing close side by side at the tip of the sand spit, both laughing joyfully; Yaraa's arms spread wide in the wind, her face lifted to the golden sunlight, glowing; Mifzaal beside her looking at her with delight, hands at his sides; her crimson dress and {HIJAB_Y} rippling; glittering sea behind",
         camera="medium shot, slightly low angle, faces in the upper two-thirds, the shining wet sand as the lower third",
         amb="beach_day", sens="intimacy",
         safe="'she jumped into his arms / lay in his arms' becomes the couple standing side by side laughing, her arms spread in the wind; no embrace, no carrying"),
    dict(to=27, reason="action/scene change: escaping the heat they rest in the shade of a magoo bush", chars=["mifzaal", "yaraa"], loc="magoo_shade",
         visual=f"Mifzaal and Yaraa sitting side by side on a woven coconut-leaf mat in the deep cool shade of a big magoo bush, leaning back against its twisted trunk, relaxed; Yaraa in her crimson dress with {HIJAB_Y}, Mifzaal turning his head towards her about to speak, a hopeful look; their hands resting together between them; the blazing white beach and turquoise sea bright beyond the shade",
         camera="medium wide, eye level, faces in the upper two-thirds, the mat and cool sand as the lower third",
         amb="island_day", sens="intimacy", safe="'lay down in the shade' becomes sitting side by side on a mat leaning against the trunk"),
    dict(to=29, reason="emotional turning point: Mifzaal shares his hope of a child; Yaraa is speechless with joy", chars=["yaraa", "mifzaal"], loc="magoo_shade",
         visual=f"close two-shot in the dappled shade: Yaraa with {HIJAB_Y}, sitting beside Mifzaal, looking into his eyes with a radiant, overwhelmed smile, eyes shining with happy tears, lips parted, speechless; Mifzaal soft in the near foreground at the side, seen three-quarter from behind; warm golden light filtering through the magoo leaves",
         camera="medium close-up over Mifzaal's shoulder, Yaraa's face centred in the upper half",
         amb="island_day", sens="other", safe="the hoped-for child is only spoken about; no child shown, only Yaraa's joyful face"),
    dict(to=31, reason="action change: at noon Yaraa gets up to fetch food from Shifza; Mifzaal pretends to sulk", chars=["mifzaal", "yaraa"], loc="magoo_shade",
         visual=f"Mifzaal sitting on the mat in the magoo shade, leaning back with his arms folded and a comically sulky pout, speaking; Yaraa standing up beside the mat in her crimson dress with {HIJAB_Y}, looking down at him with an amused smile, about to go; bright noon beach beyond",
         camera="medium shot, eye level, Mifzaal centred in the upper half, Yaraa standing at the side",
         amb="island_day"),
    dict(to=32, reason="action change: Yaraa walks away, looking back with a warm smile and a little wave", chars=["yaraa"], loc="beach_walk",
         visual=f"Yaraa walking away along the bright beach towards the trees, glancing back over her shoulder with a warm loving smile and a small wave of her hand; her crimson long dress and {HIJAB_Y}, the hijab end lifting in the breeze; long palm shadows, glittering sea",
         camera="medium-wide, eye level, her face in the upper third, the bright sand and her footprints as the lower third",
         amb="beach_day", sens="intimacy", safe="the blown kiss becomes a warm look back over the shoulder and a little wave"),
    dict(to=35, reason="scene/character change: Mifzaal alone in the shade answers a call from Faisal (shot)", chars=["mifzaal"], loc="magoo_shade",
         visual="Mifzaal alone sitting on the mat in the magoo shade, holding his phone to his ear with a broad friendly smile, his free hand resting on his knee; the phone screen faces away and is not visible; the bright beach behind him empty",
         camera="medium close-up, eye level, Mifzaal centred in the upper half, the mat and sand as the lower third",
         amb="island_day"),
    dict(to=37, reason="character change: Faisal on the phone in his Male office, teasing (reverse shot, speaker focus)", chars=["faisal"], loc="male_office",
         visual="Faisal with his glasses and light-grey shirt leaning back in his office chair, phone to his ear, laughing and teasing with a mischievous grin; the window behind shows blurred pastel Male buildings; the phone screen not visible",
         camera="medium close-up, eye level, Faisal centred and sharp in the upper half, the desk top as the lower third",
         amb="office_day"),
    dict(to=39, reason="return to Mifzaal on the phone (shot / reverse-shot): he laughs, but something stings", loc="magoo_shade",
         reuse="beat_019", chars=["mifzaal"], amb="island_day", visual="(reuse of beat_019)"),
    dict(to=41, reason="action change: the call ends, still no Yaraa; he dials her — and a voice calls his name from behind", chars=["mifzaal"], loc="jungle_edge",
         visual="Mifzaal standing at the edge of the shade, lowering the phone from his ear and looking along the empty beach where Yaraa went, brows knitted with growing worry; the phone screen faces away; behind him the dense green jungle and a narrow sand path disappearing into the undergrowth, the light dimming",
         camera="medium shot, eye level, Mifzaal centred in the upper half, the sand path as the lower third",
         amb="island_day"),
    dict(to=44, reason="emotional turning point: a strange hoarse woman's voice; frozen in shock he slowly turns", chars=["mifzaal"], loc="jungle_edge",
         visual="close-up of Mifzaal frozen in shock, eyes wide with fear, beads of sweat, slowly turning his head to look back over his shoulder towards the jungle; the phone still in his hand at his side; the jungle behind him out of focus, only dark green leaves and palm trunks, nobody there",
         camera="close-up, eye level, his frightened face in the upper half, dark foliage around",
         amb="jungle_eerie", sens="other",
         safe="the voice is never shown as a person: only Mifzaal's frightened face; the jungle behind him is empty"),
    dict(to=45, reason="what he sees: only a huge black cloud over the silent jungle, nobody", loc="black_cloud",
         visual="an enormous towering black cloud rising over the jungle canopy and blotting out the sun; below it an empty narrow sand path disappearing between dense coconut palms and screw-pines into deep green shadow; fronds bending in a sudden wind; absolutely no people, no figures, no faces or shapes in the clouds or trees",
         camera="wide shot, low angle from the beach, the black cloud filling the upper two-thirds, the empty pale sand path as the lower third",
         amb="jungle_eerie", sens="other", safe="the source of the voice is never drawn; only the black cloud and the empty jungle"),
    dict(to=47, reason="action change: frightened, he calls Yaraa again; her phone is switched off", chars=["mifzaal"], loc="jungle_edge",
         visual="Mifzaal standing on the beach ridge with the phone pressed to his ear, his face tense and pale with fear, his other hand gripping his hair; behind him the jungle edge in cold grey-green light under the black cloud; the phone screen not visible",
         camera="medium close-up, eye level, his face centred in the upper half, the grey sand as the lower third",
         amb="jungle_eerie"),
    dict(to=49, reason="action change: he hurries back along the beach towards the boat, glancing back, feeling followed", chars=["mifzaal"], loc="beach_hurry",
         visual="Mifzaal hurrying along the empty beach towards the camera, glancing back fearfully over his shoulder; behind him only his own footprints, long dark palm shadows and the empty beach; the black cloud spreading above the jungle; nobody follows",
         camera="medium-wide, eye level, Mifzaal in the upper-middle, the empty sand and footprints as the lower third",
         amb="island_wild", sens="other", safe="the feeling of being followed is shown only by his look back at an empty beach"),
    dict(to=52, reason="character change: at the dinghy he finds Naveen, who is puzzled and says the women went to the pond (speaker focus)", chars=["naveen", "mifzaal"], loc="landing",
         visual="Naveen in his navy polo and grey cargo trousers standing beside the small white dinghy pulled up on the sand, facing the camera, puzzled, speaking with one hand raised in a calming gesture and the other pointing inland towards the jungle; in the soft-focus foreground Mifzaal seen from behind, out of breath; the hull plain white with no lettering",
         camera="over-the-shoulder medium shot, Naveen centred and sharp in the upper half, Mifzaal blurred in the foreground",
         amb="island_wild"),
    dict(to=53, reason="dialogue: Mifzaal asks why Yaraa's phone is switched off (reverse shot, speaker focus)", chars=["mifzaal", "naveen"], loc="landing",
         visual="Mifzaal facing the camera beside the dinghy, still anxious, holding up his phone with its screen turned away towards himself, asking a question with furrowed brows; Naveen in the soft-focus foreground seen from behind; the jungle and the dark cloud behind Mifzaal",
         camera="over-the-shoulder medium shot, Mifzaal centred and sharp in the upper half, Naveen blurred in the foreground",
         amb="island_wild"),
    dict(to=54, reason="return to Naveen explaining the weak signal (shot / reverse-shot)", loc="landing",
         reuse="beat_027", chars=["naveen", "mifzaal"], amb="island_wild", visual="(reuse of beat_027)"),
    dict(to=56, reason="return to Mifzaal: the voice is still fixed in his mind; he asks if anyone lives here (reverse shot)", loc="landing",
         reuse="beat_028", chars=["mifzaal", "naveen"], amb="island_wild", visual="(reuse of beat_028)"),
    dict(to=59, reason="action change: Naveen laughs off the question — the island has been deserted for ages (speaker focus)", chars=["naveen", "mifzaal"], loc="landing",
         visual="Naveen beside the dinghy laughing in disbelief, one arm sweeping out towards the empty jungle and beach as if to say 'look, nobody here', the other hand on his hip; Mifzaal at the side in three-quarter view, silent and uneasy, glancing at the jungle; the big dark cloud spreading over the trees behind; nobody else anywhere",
         camera="medium two-shot, eye level, Naveen centred and sharp in the upper half, Mifzaal at the side, the wet sand as the lower third",
         amb="island_wild"),
    dict(to=60, reason="action change: keeping the voice to himself, Mifzaal walks with Naveen inland towards the pond (author credit)", chars=["mifzaal", "naveen"], loc="pond_path",
         visual="Mifzaal and Naveen seen from behind walking side by side along the narrow white sand path into the dense jungle towards the pond, tall palms and screw-pines closing overhead, thick tall grass on either side; Mifzaal glancing uneasily to the side; the path fading into green shadow ahead, empty",
         camera="medium-wide from behind, eye level, the figures and the path into the jungle in the upper two-thirds, the pale sand path as the lower third",
         amb="jungle_eerie"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Even if not now, Yaraa, we will meet again — if it is meant to be.\" The sun rose, giving way to a new day.")
sh(2, "In the excitement of the Eid al-Adha holidays, Mifzaal decided to go on a picnic trip to an island near Male with his life partner, Yaraa.")
sh(3, "Shifza and her husband also joined the two of them on that trip. They are a couple who have faced many different challenges in life with courage.")
sh(4, "Even the first child of their marriage bade farewell to this world without warning. But Mifzaal and Yaraa have been married only three days.",
   hum=True)
sh(5, "Mifzaal is someone always busy running his own business in Male. That is why, in this short holiday he got, he thought of marrying Yaraa quickly.")
sh(6, "To go on the trip, the four of them boarded a dinghy. It was a calm-sea day. In the sky not a single wisp of cloud, nor anything else, could be seen.",
   [("boat_engine", "ޑިންގީއަށް", -20)])
sh(7, "In the cool breezes blowing, Yaraa's shining hair kept brushing across Mifzaal's face.",
   [("wind_gust", "ވައިރޯޅިތަކުން", -22)])
sh(8, "As Mifzaal sat on the back seat of the dinghy, Yaraa, her head resting on his shoulder, had both her hands interlaced in the fingers of Mifzaal's two hands.")
sh(9, "Shifza's husband Naveen, sitting in front of them, said: \"Hey Yaraa, if you grip his fingers that hard, they might come right off, you know.")
sh(10, "Mifzaal isn't going to let go of Yaraa and go anywhere.\" As he said this, a shy smile spread over Yaraa's face.")
sh(11, "And sitting quietly, Shifza said: \"Mifzaal, aren't you going to say anything at all?\"")
sh(12, "In answer to Shifza's question, Mifzaal said: \"Everyone, listen to what I'm about to say.")
sh(13, "I married Yaraa having given my whole heart to that queen,")
sh(14, "so I have nothing in particular to say about that.\" As he said this, everyone burst out laughing loudly at once.")
sh(15, "Time passed and the dinghy reached its destination. It was a beautiful island. A naturally dazzling silver-white sandy beach lay ahead, while the inside of the island was overgrown with trees and had turned to jungle.",
   [("water_splash_small", "އަތުވެއްޖެ", -22)])
sh(16, "After putting the things they had brought among the shady trees growing on the beach ridge, the very first thing Mifzaal decided was to take Yaraa towards the tip of the island.")
sh(17, "Naveen and Shifza were in the sea at the time, having fun splashing about. So they didn't even notice where Yaraa and Mifzaal had gone.",
   [("splash", "މޫދުގައި", -22)])
sh(18, "As their feet sank into the soft sand of the beach, Yaraa nearly fell several times.",
   [("footsteps_sand", "ފައި", -20)])
sh(19, "But Mifzaal's gentle hands held Yaraa firmly by the shoulders with boundless tenderness.")
sh(20, "On reaching the tip, Yaraa let go of Mifzaal's hand and ran off towards that beautiful open stretch of white sand.",
   [("footsteps_sand", "ދުއްވައިގަތީ", -20)])
sh(21, "Walking behind with slow steps, Mifzaal's heart was made all the more complete by the graceful sight of Yaraa as she ran.",
   [("footsteps_sand", "ހިނގާފައި", -24)])
sh(22, "In that beautiful red dress she had worn for the sea, she was an enchanting sight that would captivate anyone.")
sh(23, "Standing freely in the wind with both arms spread wide, Yaraa beckoned Mifzaal to come close.",
   [("wind_gust", "ވައިގެ", -22)])
sh(24, "What made this emotional moment of the two even more complete was Yaraa leaping up into Mifzaal's arms.")
sh(25, "What a touching moment, isn't it? As she lay in Mifzaal's arms, the golden rays of the sun falling on Yaraa's face made her fair complexion and the glow of her face shine all the more.")
sh(26, "But in that blazing heat they could bear it only a short while. To rest from their tiredness they went and lay down in the shade of a magoo tree growing on the beach ridge.",
   [("cloth_rustle", "އޮށޯވެލި", -24)])
sh(27, "And, for the first time, Mifzaal told Yaraa of a hope he had been nursing without saying: \"Yaraa, tell me,")
sh(28, "next time we come on a trip like this, we should bring a lovely little baby along too, shouldn't we?\" At Mifzaal's words, the tiredness on Yaraa's face seemed to vanish completely.")
sh(29, "With a smiling face Yaraa lay looking into Mifzaal's eyes, not knowing what to say, so great was her happiness.")
sh(30, "By then it had turned past twelve noon. Saying she would bring something to eat, Yaraa set off walking towards Shifza and Naveen.",
   [("footsteps_sand", "ހިނގައިގަތް", -22)])
sh(31, "Lying there impatiently, he said: \"When it's time to go over to Shifu's, I don't matter at all, huh?\"")
sh(32, "Yaraa looked towards Mifzaal and blew him a kiss from her hand through the air. And with a smile, saying \"I'll be right back,\" she walked off.",
   [("footsteps_sand", "ހިނގައިގަތް", -24)])
sh(33, "Not long after Yaraa left, Mifzaal's phone began to ring. It was his closest friend, Faisal, calling.",
   [("phone_buzz", "ރިންގުވާން", -18)])
sh(34, "Faisal is the one who always gives Mifzaal the closest counsel. Mifzaal always agrees with every decision Faisal makes.")
sh(35, "And Faisal, too, sees Mifzaal as a friend like no other. So, before Yaraa came back, he quickly picked up the phone and held it to his ear.")
sh(36, "\"Where are you, Mifzaal? Now you're always going around with your wife, so you've completely forgotten me, huh?\" Joking along, Mifzaal said:")
sh(37, "\"Yes, well, when you go around with a wife, that's how it is, right?\" At this Faisal said: \"I'll see how many days Mifzaal can go on living under his wife's thumb.\"")
sh(38, "At Faisal's words Mifzaal burst out laughing. But at that moment something inside Mifzaal's heart stung a little.")
sh(39, "In any case, Faisal is not someone who would ever do Mifzaal harm, or ever wish him harm.")
sh(40, "So, after saying \"many salaams,\" he ended the call. Even after all that time there was no word from Yaraa.")
sh(41, "He hurried to call Yaraa's number to see what had happened. At that moment someone behind him called out Mifzaal's name.",
   [("low_growl", "ގޮވާލި", -24)], hum=True)
sh(42, "He got a sudden fright. Who could that be, coming from inside the vast jungle of this deserted island where no one lives, he thought.",
   [("gasp", "ސިހުމެއް", -18)], hum=True)
sh(43, "Questions churned in his heart. It was certainly a woman's voice. But that voice was very different from Yaraa's and Shifza's voices.",
   [("heartbeat", "ފުނިޖެހެމުން", -22)], hum=True)
sh(44, "A hoarse, scratchy voice. Not daring to look behind, he slowly turned around.",
   [("low_growl", "މުސްކުޅިވެ", -24), ("leaves_rustle", "އެނބުރިލި", -22)], hum=True)
sh(45, "At that moment, behind him there was a huge black cloud. But there was no sign of anyone at all.",
   [("wind_howl", "ވިލާގަނޑެއް", -22)], hum=True)
sh(46, "Fear kept taking hold of Mifzaal's heart. So he quickly called to find out where Yaraa was.",
   [("heartbeat", "ބިރުވެރިކަން", -20)], hum=True)
sh(47, "But the other end said the phone was switched off. And Yaraa is not someone who ever goes around with her phone switched off.",
   [("breath_heavy", "ނިއްވާލާފަ", -22)], hum=True)
sh(48, "So great was his worry that he set off at a fast walk towards where they had landed. Even then Mifzaal felt as if someone were walking behind him.",
   [("footsteps_sand", "ހިނގައިގަތް", -18), ("leaves_rustle", "ހިނގާފައި", -24)], hum=True)
sh(49, "Every now and then he found himself glancing back, so great was his anxiety. When he got there, the dinghy they had come in was right where it had been.",
   [("breath_heavy", "ބަލައިލެވޭ", -22)], hum=True)
sh(50, "Not far off Mifzaal saw Naveen. He quickly ran over and asked where Yaraa was.",
   [("footsteps_sand", "ދުވެފައި", -20)])
sh(51, "Puzzlement showed on Naveen's face. \"Calm down, Mifzaal, you look so worried — did something go wrong?")
sh(52, "Yaraa and Shifza, the two of them went to that pond over there.\" As Naveen said this, Mifzaal's heart felt some measure of relief.",
   [("sigh", "ފިނިކަމެއް", -22)])
sh(53, "But there were still questions in his heart left unanswered. For this reason he asked Naveen: \"If that's so, why is Yaraa's phone switched off?")
sh(54, "When I call, it says it's switched off.\" Naveen said: \"The signal around here is very weak. When I called Shifza too, it said switched off.\"")
sh(55, "However much he didn't want to ask, the voice of someone calling him was still fixed in Mifzaal's heart, as if it had happened only a moment ago.",
   hum=True)
sh(56, "So he decided to ask Naveen about it. \"Naveen, does anyone live on this island?\"")
sh(57, "At Mifzaal's words Naveen sensed that something had happened to him, and he said: \"Hey Mifzaal, have you gone mad?")
sh(58, "This island has been deserted for who knows how long. So what would anyone be doing on this island? Nobody could be living here.")
sh(59, "Why are you asking so many questions, Mifzaal?\" Whatever happened, Mifzaal did not want to tell Naveen what had happened.")
sh(60, "So, after saying \"It's nothing,\" both of them set off walking towards the pond. Shail Abdurrazzaq.",
   [("footsteps_sand", "ހިނގައިގަތް", -22)])
SHOTS = S

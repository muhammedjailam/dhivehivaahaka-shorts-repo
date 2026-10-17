"""Beat/shot plan for Aliflaila episode 551 (Night 7) (used by plan_beats.py).
FRAME (night chamber) -> TALE: the Fisherman and the Jinni on the seashore -> TALE-WITHIN-THE-TALE: the jinni Sakhr's
own backstory (rebellion, capture by Asif, sealed in the brass jar, centuries on the sea floor) -> back to the shore:
the fisherman's trick, the jinni flows back into the jar, the lid slammed -> FRAME at dawn, the king spares Shahrazad.
Bible rules: Prophet Sulaiman NEVER depicted (empty throne in light; the glowing eight-petalled rosette seal, no
letters); Asif only as a distant figure in white seen from behind; God's Name = only golden light; no weapons (jinni
empty-handed), the death threat = towering jinni with a pointing finger; every woman's hair and neck fully covered;
frame scenes: Shahrazad on a cushion, Dunyazad on the carpet, the king on a divan an arm's length away (no bed);
minaret only as a distant silhouette; no text/letters anywhere."""

GLOW = "soft golden storybook glow"
JAR = ("a large tarnished brass jar with a round belly and a long narrow neck, its open mouth empty, and beside it on the "
       "sand a thick round dull-grey lead stopper with a small glowing abstract eight-petalled geometric rosette on top "
       "(no letters, no star)")
FISHERMAN = "the old fisherman in his faded patched blue tunic, white skullcap and beige wrap"
CHAMBER_SET = ("Shahrazad sits on a floor cushion on the carpet, Dunyazad sits on the carpet close beside her, and King "
               "Shahryar sits fully dressed on a cushioned divan an arm's length or more away from them")

LOC = {
    "palace_ext": "King Shahryar's vast white palace with golden onion domes, slender towers and arched windows on a hill "
                  "above a sleeping city of domes, a few windows glowing amber",
    "chamber": "King Shahryar's private palace chamber: Persian carpets, plump floor cushions, a long cushioned divan with "
               "silk bolsters, silk curtains, hanging brass lanterns, and a tall arched window with a carved lattice "
               "screen showing a moonlit city of domes and slender towers",
    "shore": "a lonely wide golden sandy seashore beside a turquoise sea, low dunes and a few leaning date palms, a "
             "fisherman's cast net lying on the sand, and " + JAR,
    "shore_dark": "the same lonely golden sandy seashore beside the sea, low dunes and leaning date palms, a fisherman's "
                  "cast net on the sand, and " + JAR,
    "peaks": "an ancient fairy-tale land of jagged rocky mountain peaks and deep valleys in a long-ago age, a distant "
             "radiant white-gold light glowing on the far horizon",
    "hall": "a vast ancient marble throne hall of a long-ago age, rows of tall white columns, high arches, a polished "
            "marble floor, and at the far end a high dais with an empty golden throne",
    "sea_deep": "deep inside a vast blue sea, rays of light slanting down from the surface far above, drifting silver "
                "bubbles, the dark hull of an old wooden sailing ship floating far above at the surface",
    "seabed": "the dark, silent bottom of the deep sea: soft sand, rocks, waving seaweed and coral, faint shafts of blue "
              "light from far above",
    "hut": "a humble palm-thatch fisherman's hut at the edge of a poor fishing village by the sea, a reed doorway, a few "
           "empty clay bowls and an empty cooking pot on a cold hearth stone",
    "city_dawn": "the capital city of domes and flat roofs seen from the palace terrace at dawn, a distant slender "
                 "minaret silhouette against the sky",
    "chamber_dawn": "King Shahryar's private palace chamber at dawn: Persian carpets, floor cushions, a long cushioned "
                    "divan with silk bolsters, brass lanterns with dying flames, and the tall arched lattice window now "
                    "filled with golden dawn light over the city of domes",
    "court": "King Shahryar's grand throne hall (darbar): tall arches, marble columns, a raised golden throne under a "
             "silk canopy, carpets, rows of courtiers in long robes and turbans",
}
MOOD = {
    "palace_ext": "late night, deep midnight-blue sky full of twinkling stars, a huge pale moon above the domes, warm amber "
                  "glow in a few windows, deep hush and silence",
    "chamber": "late night, deep midnight-blue shadows, warm amber lantern light, moonlight through the lattice, intimate "
               "hush, eager anticipation",
    "shore": "bright morning sunlight, turquoise sky, sparkling sea, but tense and fearful; drifting wisps of indigo smoke",
    "shore_dark": "morning, but the sky above the shore is darkened by swirling indigo-violet storm clouds of the jinni's "
                  "smoke, a sickly purple gloom on the sand, dramatic rim light, menace and dread",
    "peaks": "soft golden storybook glow of a long-ago tale, dusky violet sky, proud and ominous",
    "hall": "soft golden storybook glow, a dazzling column of pure white-gold light pouring down onto the empty throne, "
            "awe and solemn majesty",
    "sea_deep": "soft golden storybook glow over deep sapphire-blue water, sinking silence, loneliness",
    "seabed": "soft golden storybook glow faintly over cold deep blue-black water, dim and lonely, centuries passing",
    "hut": "dusk, soft rose-and-amber light, a gentle dreamy haze of an imagined scene, poverty and tenderness",
    "city_dawn": "the very first dawn, rose-gold light rising on the horizon, the last stars fading, peaceful and holy",
    "chamber_dawn": "dawn, warm golden light streaming through the lattice window and laying patterns on the carpet, the "
                    "lantern flames pale, suspense melting into relief",
    "court": "bright morning, golden sunlight in long shafts through the high arched windows, formal and majestic",
}

BEATS = [
    dict(to=3, reason="episode opening: the seventh night falls over Shahryar's palace", loc="palace_ext",
         visual="the vast white palace with golden onion domes standing on its hill under a huge pale moon and a sky full of "
                "twinkling stars, a single tall arched window high in the palace glowing warm amber, the sleeping city of "
                "domes below in deep blue shadow; no people visible",
         camera="wide establishing shot, low angle, the palace and moon in the upper two-thirds, a calm dark garden wall "
                "and shadowed slope as the lower third", amb="palace_night"),
    dict(to=7, reason="scene change: the frame chamber, Dunyazad asks her sister to finish the tale",
         chars=["dunyazad", "shahrazad", "shahryar"], loc="chamber",
         visual=CHAMBER_SET + "; little Dunyazad leans eagerly toward her sister with her hands clasped under her chin, big "
                "pleading eyes; Shahrazad turns to her with a gentle smile; the king leans forward on the divan, impatient "
                "and curious, one hand on his knee",
         camera="wide shot, eye level, the three figures in the upper two-thirds, the patterned carpet as a calm lower third",
         amb="palace_night"),
    dict(to=10, reason="action change: Shahrazad looks at the king and bows, asking permission; he says 'begin!'",
         chars=["shahrazad", "shahryar", "dunyazad"], loc="chamber",
         visual="Shahrazad on her cushion bowing her head gracefully toward the king with one hand on her heart, her large "
                "dark eyes lifted respectfully; King Shahryar on the divan an arm's length away gesturing with an open "
                "empty hand, 'begin!', his eyes wide with eager impatience; Dunyazad beside her sister in the background "
                "watching excitedly",
         camera="medium two-shot over the carpet, eye level", amb="palace_night"),
    dict(to=13, reason="scene change, enter the TALE: on the seashore the colossal jinni bows to the ground begging 'Sulaiman' for mercy",
         chars=["jar_jinni", "fisherman"], loc="shore",
         visual="the colossal jinni bowed low over the sand, his huge body hunched and his smoky indigo tail coiled on the "
                "beach, his empty hands pressed together in pleading, golden eyes frightened; small in the foreground the "
                "thin old fisherman stands trembling, clutching his net, staring up with a flicker of relief; the brass "
                "jar lies open on the sand between them with thin smoke still curling out",
         camera="wide shot, slightly low angle, the jinni filling the upper two-thirds, the sand a calm lower third",
         amb="seashore_day", transition="dissolve"),
    dict(to=17, reason="focus change: the fisherman gathers courage and tells the jinni that Sulaiman died long ago",
         chars=["fisherman", "jar_jinni"], loc="shore",
         visual="the old fisherman standing straight, one hand lifted with an open palm, explaining in a trembling but brave "
                "voice, his net over his shoulder; behind him the giant bowed jinni raises his head in confusion, one "
                "heavy eyebrow lifted, listening",
         camera="medium shot from slightly low, the fisherman in front, the jinni's face looming above him",
         amb="seashore_day"),
    dict(to=20, reason="action change: the jinni suddenly rises to his full height, his fear turning into rage",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the colossal jinni surging up to his full towering height, his smoke billowing out into the darkening sky, "
                "his blazing golden eyes wide and furious, heavy brows knotted, empty fists clenched; the tiny old "
                "fisherman stumbles back on the sand in shock",
         camera="dramatic very low angle from the sand, the jinni towering into the storm-dark sky",
         amb="seashore_day"),
    dict(to=23, reason="action change: the jinni roars like thunder and orders him to choose how he will die",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the giant jinni leaning down and thundering, mouth wide open in a roar, one huge empty-handed finger "
                "pointing down at the fisherman, the sand around them shivering and blowing in swirls, purple lightning in "
                "the smoke clouds; the small fisherman cowers with his arms raised before his face",
         camera="high-drama low angle over the fisherman's shoulder up at the jinni", amb="seashore_day",
         sens="violence", safe="the death threat is shown only as the towering jinni pointing with an empty hand; no weapon, no harm"),
    dict(to=27, reason="action change: the fisherman falls to his knees weeping and begging for mercy",
         chars=["fisherman", "jar_jinni"], loc="shore_dark",
         visual="the old fisherman on his knees on the sand, tears streaming down his lined cheeks, his hands pressed "
                "together in desperate pleading, looking up; the merciless jinni towers above him with folded arms, "
                "glaring down",
         camera="medium wide, high angle from behind the jinni's shoulder down onto the kneeling fisherman",
         amb="seashore_day", sens="violence", safe="emotional pleading only; no harm shown"),
    dict(to=29, reason="time jump, enter the TALE-WITHIN-THE-TALE: the jinni Sakhr's proud rebellion long ago",
         chars=["jar_jinni"], loc="peaks",
         visual=GLOW + "; long ago, the giant jinni standing proudly on a jagged mountain peak with his arms folded and his "
                "chin raised in arrogance, turning his back on a distant radiant white-gold light on the horizon, while far "
                "below in the valley rows of smaller shadowy smoke-jinn bow toward that light",
         camera="wide shot, low angle, the jinni and peak in the upper two-thirds, a dark misty valley as the lower third",
         amb="memory", transition="dissolve"),
    dict(to=31, reason="action change: the vizier Asif is sent and binds the rebellious jinni",
         chars=["jar_jinni"], loc="peaks",
         visual=GLOW + "; ribbons of glowing golden light winding like chains around the giant jinni's arms and smoky body "
                "as he strains against them with a furious face; small and distant in the middle of the picture a single "
                "figure in a plain flowing white robe and white turban seen from behind, standing calmly on a rock with "
                "one open hand raised; his face is never seen",
         camera="wide shot, eye level, the struggling jinni in the upper two-thirds, the figure in white small and seen from behind",
         amb="memory", sens="other",
         safe="Asif ibn Barkhiya appears only as a small distant figure in white seen from behind (bible rule 9)"),
    dict(to=33, reason="scene change: the bound jinni brought before the empty throne bathed in light, he refuses to obey",
         chars=["jar_jinni"], loc="hall",
         visual=GLOW + "; the giant jinni bound in glowing golden light-chains, held in the middle of the vast marble hall "
                "before a high dais with an empty golden throne bathed in a dazzling column of white-gold light; nobody "
                "sits on the throne; the jinni turns his face away proudly with a defiant scowl",
         camera="wide shot, symmetrical, from behind and beside the jinni toward the radiant empty throne",
         amb="throne_hall", sens="other",
         safe="Prophet Sulaiman is never depicted: only the empty throne in a column of light"),
    dict(to=35, reason="action change: the jinni is shut inside the brass jar and sealed with lead and the rosette seal",
         loc="hall",
         visual=GLOW + "; close view of the tarnished brass jar with a long narrow neck standing on the polished marble floor, "
                "the last swirl of indigo smoke being drawn down into its mouth, the thick dull-grey lead stopper set "
                "firmly on its neck, and on top of the stopper a glowing abstract eight-petalled geometric rosette seal "
                "shining with pure golden light; a shaft of white-gold light falls on it from above; no hands, no people, "
                "no letters",
         camera="close-up, slightly low angle, the jar and glowing seal in the upper two-thirds, the marble floor as the lower third",
         amb="throne_hall", sens="other",
         safe="the sealing is shown only as the jar and the glowing abstract rosette; no prophet, no hand, God's Name = light only"),
    dict(to=37, reason="scene change: the jar is thrown into the deepest sea and sinks",
         loc="sea_deep",
         visual=GLOW + "; the sealed brass jar sinking slowly down through deep sapphire-blue water, trailing a stream of "
                "silver bubbles, its rosette seal glowing faintly; far above at the bright surface the dark hull of an old "
                "wooden ship and a spreading ring of ripples",
         camera="vertical underwater shot looking up, the ship and light at the top, the jar sinking in the middle, dark deep water below",
         amb="memory"),
    dict(to=42, reason="time jump: centuries on the sea floor and the jinni's changing vows (riches, treasures, three wishes)",
         loc="seabed",
         visual=GLOW + "; the lonely brass jar lying on its side on the dark sea floor, half buried in sand and slowly "
                "overgrown with coral and seaweed; above it, faint dreamy golden visions float in the water like glowing "
                "bubbles: a heap of gold coins, an open treasure chest of jewels, and three small glowing orbs of light",
         camera="medium wide, eye level on the sea floor, the jar and visions in the upper two-thirds, smooth sand as the lower third",
         amb="memory", transition="black"),
    dict(to=44, reason="emotional turning point: in the fourth century his patience breaks and he vows to kill his rescuer",
         loc="seabed",
         visual=GLOW + " turned cold; the coral-encrusted brass jar on the dark sea floor glowing from within with an angry "
                "violet-red light, dark smoke seeping around the lead stopper, and two blazing golden eyes glaring out of "
                "the shadow of its neck; the golden visions are gone",
         camera="close-up, low angle, the glowing jar in the upper two-thirds, dark sand below",
         amb="memory", transition="black"),
    dict(to=46, reason="return to the shore (leave the jinni's tale): 'today you freed me, so you must die'",
         chars=["jar_jinni", "fisherman"], loc="shore_dark", reuse="beat_007",
         visual="(reuse of beat_007)", amb="seashore_day", transition="dissolve",
         sens="violence", safe="threat only, towering jinni pointing with an empty hand"),
    dict(to=49, reason="scene change (imagined): the fisherman's poor wife and hungry little children at home",
         loc="hut",
         visual="a dreamy imagined scene seen from inside the humble palm-thatch hut looking out through the reed doorway at "
                "the sunset sea: a poor mother in a plain patched brown gown and a plain brown headscarf wrapped snugly over "
                "her whole head and neck, and three small thin children sitting close beside her, all seen from BEHIND, "
                "their faces not visible: two little boys in small plain white skullcaps and one little girl whose pale "
                "beige headscarf is wrapped snugly over her whole head with no hair showing; an empty cooking pot and empty "
                "clay bowls on the floor beside them; soft hazy edges like a memory",
         camera="medium wide, eye level, the family in the upper half, the bare swept earth floor as a calm lower third",
         amb="village_day", transition="dissolve"),
    dict(to=51, reason="return to the shore, action change: the jinni has no mercy and refuses",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the giant jinni with his arms folded across his chest and his chin raised, turning his blazing golden eyes "
                "away in cold contempt; at his feet the small old fisherman still kneels with tear-wet cheeks, his hands "
                "reaching up",
         camera="low angle wide shot, the jinni towering in the upper two-thirds", amb="seashore_day", transition="dissolve"),
    dict(to=54, reason="emotional turning point: the fisherman realises crying is useless and an idea comes to him",
         chars=["fisherman"], loc="shore_dark",
         visual="close-up of the old fisherman's lined face, the last tears drying on his cheeks, his bright clever eyes "
                "narrowing as a sly idea dawns on him, a tiny glint of light sparkling in his eye, one finger stroking his "
                "grey beard; the dark smoky shape of the jinni blurred behind him",
         camera="close-up, eye level, face in the upper half, his shoulder and the blurred sand below", amb="seashore_day"),
    dict(to=58, reason="action change: he stops crying, stands firm and asks the jinni to swear by the Name on the seal",
         chars=["fisherman", "jar_jinni"], loc="shore_dark",
         visual="the old fisherman standing on his feet again, calm and steady, looking straight up at the jinni with a "
                "firm face, one hand pointing to the lead stopper with its glowing eight-petalled rosette lying on the sand "
                "beside the brass jar; the giant jinni bends down, listening suspiciously",
         camera="medium wide, low angle past the jar and stopper in the foreground, the two figures above",
         amb="seashore_day"),
    dict(to=61, reason="action change: at the Name the jinni trembles and swears to answer truthfully",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the rosette on the lead stopper flares with pure golden light; the colossal jinni recoils and trembles, his "
                "smoke shivering, then nods with one empty hand laid on his chest as he swears, his golden eyes wide with "
                "awe; the fisherman stands watching calmly",
         camera="wide shot, low angle, the golden glow lighting the jinni's face from below", amb="seashore_day",
         sens="other", safe="God's Greatest Name shown only as golden light from the abstract rosette; no script"),
    dict(to=66, reason="action change: the trick — the fisherman points at the tiny jar and says the giant could never fit in it",
         chars=["fisherman", "jar_jinni"], loc="shore_dark",
         visual="the old fisherman pointing at the small brass jar on the sand with a look of exaggerated disbelief, "
                "eyebrows raised and head tilted; the jar looks tiny in the foreground while the colossal jinni towers up "
                "behind into the clouds, his huge hand bigger than the whole jar",
         camera="forced-perspective wide shot, low angle, the jar in the lower-middle foreground, the jinni filling the sky",
         amb="seashore_day"),
    dict(to=72, reason="action change: the jinni's pride is wounded; the fisherman insists he only saw smoke",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the giant jinni bending all the way down so his huge offended face hangs just above the small fisherman, "
                "eyes bulging, nostrils flaring with hurt pride; the fisherman stands with his arms folded and his chin up, "
                "shaking his head with a sly stubborn half-smile",
         camera="medium two-shot, side view, eye level of the fisherman", amb="seashore_day"),
    dict(to=74, reason="action change: the jinni dissolves into a huge black column of smoke that covers the sky",
         chars=["jar_jinni", "fisherman"], loc="shore_dark",
         visual="the colossal jinni spreading his arms with a proud roar as his giant body dissolves upward into an enormous "
                "swirling column of dark indigo-black smoke and glittering violet sparkles that spreads across the whole "
                "sky; the small old fisherman (faded patched blue tunic, white skullcap, beige wrap, net on his shoulder) watches from the sand, holding on to his skullcap in the wind",
         camera="extreme wide shot, low angle, the smoke column filling the sky", amb="seashore_day"),
    dict(to=77, reason="action change: the smoke swirls down into the jar's mouth until all of it is inside",
         loc="shore_dark",
         visual="a spiralling whirlwind of indigo-black smoke and violet sparkles funnelling down from the dark sky straight "
                "into the narrow mouth of the brass jar standing upright on the sand, the last thin tail of smoke "
                "disappearing inside, the empty beach around it",
         camera="medium shot, low angle on the jar, the smoke funnel above it", amb="seashore_day"),
    dict(to=78, reason="climax: the fisherman leaps forward and slams the lead stopper back onto the jar",
         chars=["fisherman"], loc="shore",
         visual="the old fisherman lunging forward and pressing the thick lead stopper with its glowing rosette down hard "
                "onto the neck of the brass jar with both hands, his face fierce and triumphant; the dark clouds are "
                "breaking apart and bright sunlight bursts back over the sea",
         camera="medium close-up, slightly low angle, his face and hands on the jar in the upper two-thirds",
         amb="seashore_day"),
    dict(to=79, reason="leave the TALE, time change: dawn breaks over the capital",
         loc="city_dawn",
         visual="the city of domes at the first light of dawn, a rose-gold glow rising along the horizon, the last stars "
                "fading, a distant slender minaret silhouette against the brightening sky, soft mist over the rooftops; no people",
         camera="wide establishing shot, the sky and minaret in the upper two-thirds, the quiet rooftops as a calm lower third",
         amb="mosque_dawn", transition="dissolve", sens="other",
         safe="the Fajr call to prayer = only a distant minaret silhouette at dawn; the adhan is not synthesised"),
    dict(to=82, reason="scene change: the chamber at dawn — Shahrazad falls silent, the king sits up wide-eyed",
         chars=["shahryar", "shahrazad", "dunyazad"], loc="chamber_dawn",
         visual=CHAMBER_SET + "; golden dawn light streams through the lattice window; Shahrazad sits silent with lowered "
                "eyes and folded hands; the king has sat bolt upright on the divan, eyes wide and one empty hand raised "
                "in an eager question; Dunyazad looks from one to the other",
         camera="wide shot, eye level, the window light behind them", amb="palace_dawn"),
    dict(to=84, reason="focus change: Shahrazad smiles calmly and promises the rest tomorrow night",
         chars=["shahrazad", "dunyazad"], loc="chamber_dawn",
         visual="Shahrazad in close view with a calm, gentle, knowing smile, her ivory headscarf glowing in the golden dawn "
                "light from the lattice window, one hand raised softly as if promising more; Dunyazad sitting close beside "
                "her sister, smiling; both headscarves are wrapped low across the forehead and snugly around the face so "
                "that not a single strand of hair shows at the hairline, temples or neck",
         camera="medium close-up, eye level, faces in the upper half, her folded hands and the carpet below",
         amb="palace_dawn"),
    dict(to=86, reason="action change: the king decides to spare her again and rises",
         chars=["shahryar", "shahrazad"], loc="chamber_dawn",
         visual="King Shahryar rising from the divan in the golden dawn light, adjusting his bronze brocade coat and gold "
                "sash, his face thoughtful and secretly curious; Shahrazad remains seated on her cushion an arm's length "
                "away, bowing her head gracefully with quiet relief",
         camera="medium wide, eye level", amb="palace_dawn"),
    dict(to=88, reason="scene change: the king goes to his throne hall to rule; the night ends",
         chars=["shahryar"], loc="court",
         visual="King Shahryar seen from behind and slightly to the side, walking with a stately stride down the long carpet "
                "of the sunlit throne hall toward his golden throne, empty-handed, small courtiers in long robes and turbans "
                "bowing on both sides, golden morning shafts of light through the high windows",
         camera="wide symmetrical shot down the hall, the throne in the upper part, the long carpet as the lower third",
         amb="throne_hall"),
]
S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Night Seven: the fisherman's cleverness and the jinni's defeat. The deep darkness of the seventh night spread over the world,")
sh(2, "and as the stars began to twinkle in the sky, a deep silence settled over King Shahryar's great, awe-inspiring palace.")
sh(3, "The king's mind was filled with longing for a new story.")
sh(4, "He was utterly impatient to hear how the tale of the poor fisherman and the terrible jinni, which Shahrazad had broken off on the sixth night, would go on.")
sh(5, "As the last and quietest hour of the night drew near, Dunyazad, sitting as usual on the costly carpet beside them, softly called to her elder sister.")
sh(6, "\"Dear sister,\" said Dunyazad, her voice full of eagerness and longing. \"If you are not asleep, that lovely story you broke off yesterday —")
sh(7, "the story of the poor fisherman and the terrible creature that came out of the brass jar found in the sea — please finish telling it to us.")
sh(8, "My heart is pounding to know whether that fisherman was saved.\" Shahrazad looked toward King Shahryar with her beautiful, deep dark eyes,")
sh(9, "and lowering her head with great courtesy, asked his leave. \"Will you grant me permission to continue that story, O noble and mighty king?\"",
   [("cloth_rustle", "އިސްދަށަށް", -24)])
sh(10, "\"Begin at once!\" King Shahryar said hurriedly. \"My heart longs greatly to know why that jinni cried out Sulaiman's name, and what became of that poor fisherman.\"")
sh(11, "Shahrazad began the story in her soft, lovely voice. O mighty and wise king! Where I left the story yesterday,")
sh(12, "that terrible giant jinni had come down to the ground and was begging Sulaiman to spare his life.",
   [("magic_shimmer", "ތިރިވެ", -22)])
sh(13, "When the old fisherman, who was shaking with fear, saw this, his mind found a little calm.",
   [("breath", "ރޫރޫއަޅަމުންދިޔަ", -24)])
sh(14, "And he understood that the jinni was under some great confusion. \"O great jinni!\" said the fisherman, gathering his courage,")
sh(15, "in a trembling voice. \"What are you saying? You are begging Sulaiman, the Prophet of God.")
sh(16, "But it is now one thousand eight hundred years since he left this world and passed away! We live in an entirely different age now.")
sh(17, "I am not who you think I am. I am a lowly, poor fisherman who lives by casting his net into the sea.")
sh(18, "I am the one who took you out of that jar and set you free.\" On hearing this, the giant jinni suddenly rose up to his full height.",
   [("smoke_whoosh", "ތެދުވިއެވެ", -18)])
sh(19, "He widened his blazing eyes and stared at the fisherman. The fear and pleading on his face",
   [("heartbeat", "ބަލާލިއެވެ", -22)])
sh(20, "suddenly turned into the most extreme rage. \"Is that so?\" the jinni roared in a voice like thunder.",
   [("thunder", "ގުގުރިއެއް", -18)], hum=True)
sh(21, "Even the sand on the shore trembled at his voice. \"So you are not Sulaiman? You are only a lowly human?",
   [("wind_gust", "ތުރުތުރުއަޅައިގެން", -20)])
sh(22, "Then how did you dare to speak to me so rudely and disrespectfully? Get ready at once!")
sh(23, "Today is the last day of your life. Choose the way you want to die!\"", hum=True)
sh(24, "The fisherman felt as if the ground had split open beneath his feet. Weeping, he joined his hands and began to plead.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(25, "\"For God's sake, have mercy on me! What wrong have I done you? I took you out of that dark jar,")
sh(26, "saved you from the bottom of the sea and won you your freedom. I did you a kindness — is my reward to be killed?")
sh(27, "What injustice is this?\" \"Yes!\" the jinni answered in fury. \"Because you saved me, your reward is death.")
sh(28, "You do not know who I truly am. Listen! I am a mighty jinni called Sakhr.")
sh(29, "I grew proud over the other jinn, the devils and the demons, and I disobeyed Sulaiman, the Prophet of God.")
sh(30, "When all other creatures obeyed him, I rebelled. So Sulaiman sent his grand vizier, Asif ibn Barkhiya, to seize me and take me prisoner.")
sh(31, "Asif came, overpowered me, bound me and brought me before Sulaiman.\"",
   [("magic_shimmer", "ބަނދެގެން", -20)])
sh(32, "The jinni took a deep breath and spoke louder than before. \"Sulaiman commanded me to obey him and to believe in God.",
   [("breath_heavy", "ނޭވާއެއް", -22)])
sh(33, "But out of my pride I refused. So Sulaiman grew angry,")
sh(34, "had this thick brass jar brought, and shut me up inside it. Then he poured thick lead over it, and with his blessed ring",
   [("smoke_whoosh", "ބަންދުކުރެއްވިއެވެ", -20), ("metal_lid", "އޮއްސައި", -18)])
sh(35, "he pressed a seal bearing the Greatest Name of God onto that lead.",
   [("magic_shimmer", "ޖެއްސެވިއެވެ", -18)])
sh(36, "Then he ordered his soldiers to carry me off and throw me into the deepest part of the sea.\"",
   [("splash", "އެއްލައިލުމަށެވެ", -16)])
sh(37, "The fisherman stood frozen with fear. The jinni went on with his story. \"In the dark depths of the sea,")
sh(38, "inside this cold jar, I lay for many hundreds of years. In the first hundred years I said to myself:")
sh(39, "if someone comes and saves me, I will give him the greatest wealth in the world for the rest of his life. But nobody came.")
sh(40, "When the second hundred years began, I decided: to whoever saves me, I will open up all the treasures hidden beneath the earth.")
sh(41, "But nobody came. When the third hundred years began, I decided: I will fulfil any three wishes of the one who saves me, whatever they may be.")
sh(42, "But still nobody came.\" The rage in the jinni's voice grew fiercer. \"At last, when the fourth hundred years began, my patience ran out.")
sh(43, "My heart filled with hatred and anger. I said to myself: if anyone comes and saves me after this, I will give him no reward at all.",
   [("breath_heavy", "ނަފްރަތާއި", -22)], hum=True)
sh(44, "Instead, I will kill him at once. And the only choice I will give him")
sh(45, "is to choose the way he wants to die. And today, because you came and saved me, you must die. Your time has come.", hum=True)
sh(46, "Speak quickly! In what way do you want to die?\" The fisherman began to weep loudly. \"O jinni! Forgive me!",
   [("sob_breath", "ރޯން", -20)])
sh(47, "I am a lowly poor man. Think of my wife and my little children who depend on me.", hum=True)
sh(48, "My little daughter and son at home are hungry. They are poor little ones, like three chicks with nothing to eat.")
sh(49, "If I die, those children may starve to death. If you kill me, God will punish you.\"", hum=True)
sh(50, "But there was not the slightest mercy in that terrible jinni's heart. \"Stop this useless talk! What becomes of your children is nothing to do with me.")
sh(51, "My oath cannot be changed. There is no way for you but death. Choose quickly!\"")
sh(52, "The fisherman understood that pleading and weeping would not save his life. Suddenly a thought came to his mind. He said to himself:")
sh(53, "\"This is just a foolish jinni with nothing but a huge body and strength. He has no sense. But I am a human to whom God has given intelligence.")
sh(54, "Using my wits I will overpower this jinni, big as a phantom, and defeat him. And I will save my life.\"")
sh(55, "The fisherman suddenly stopped crying. He wiped the fear from his face and looked at the jinni with great firmness.",
   [("breath", "ހުއްޓާލިއެވެ", -24)], hum=True)
sh(56, "\"Very well,\" said the fisherman. \"I am certain you will kill me. And I stand ready to die.")
sh(57, "But before my soul departs, and before the bond between us is cut, I want to ask you one question.")
sh(58, "Swear by the Greatest Name of God on that jar that you will answer my question truthfully.")
sh(59, "Then I will stretch out my neck to die of my own accord.\" At the mention of God's Name, the jinni's huge body began to tremble.",
   [("magic_shimmer", "ތުރުތުރުއަޅައިގެން", -20)])
sh(60, "Jinn and devils know the power of that exalted Name. So the jinni nodded and said, \"Yes, I swear by that exalted Name")
sh(61, "that I will answer your question truthfully. Ask quickly!\" The fisherman pointed toward the jar")
sh(62, "and said, full of wonder: \"My question is this. Are you saying you lay inside that jar for hundreds of years?")
sh(63, "You, with that enormous body that touches the thick clouds, and two great feet planted firmly on the ground — you giant jinni...")
sh(64, "how did you get into this tiny little jar? This jar is too small even for the palm of your hand.")
sh(65, "Not even one toe of your foot would go inside it. So how can I believe that all of you was inside it?")
sh(66, "You are plainly lying. I do not believe in the least that you were inside it.\"")
sh(67, "The jinni was utterly astonished, and angered by the blow to his pride, he said: \"You don't believe it?",
   [("gasp", "ޙައިރާންވެ", -22)])
sh(68, "Even after seeing me come out of this jar before your very eyes, you don't believe me?\"")
sh(69, "\"No,\" said the fisherman very stubbornly. \"All I saw was a cloud of smoke.")
sh(70, "Until I see with my own eyes that you go entirely inside it, I will never, ever believe it as long as I live.")
sh(71, "You could never get inside it!\" The jinni's pride and arrogance rose to their peak.")
sh(72, "He could not bear the fisherman doubting his power. \"Then watch closely, you foolish human!\" the jinni roared.",
   [("thunder", "ހަޅޭއްލަވައިގަތެވެ", -20)])
sh(73, "\"I will show you how I go inside it!\" With that, the giant jinni's body slowly dissolved and once again, into a huge,",
   [("smoke_whoosh", "ހަލާކުވެ", -16)])
sh(74, "pitch-black cloud of smoke it began to change. The smoke rose up, covered the whole sky, and then, swirling round and round, came down",
   [("wind_howl", "އެނބުރެމުން", -20)])
sh(75, "and like a cold wind it began to enter the mouth of the brass jar lying on the ground. The smoke kept flowing in and in,",
   [("smoke_whoosh", "ވަންނަން", -18)])
sh(76, "until at last the whole cloud of smoke had gone inside the jar and vanished. And from inside the jar came the jinni's voice: \"Now do you believe?\"",
   [("magic_shimmer", "ހުސްވެއްޖެއެވެ", -20)])
sh(77, "The jinni called from inside the jar: \"I am inside the jar now! Do you believe it now?\" Without giving any answer, the fisherman")
sh(78, "suddenly leapt forward, snatched up the thick lead stopper lying on the ground, put it at once on the jar's mouth, pressed it down hard and sealed it shut!",
   [("footsteps_sand", "ޖެހިލައި", -20), ("metal_lid", "ފިތާލައި", -14)], hum=True)
sh(79, "When Shahrazad had brought the story this far, the lovely golden light of dawn appeared on the horizon. The sweet sound of the call to the dawn prayer spread through the air of the whole capital.")
sh(80, "At that, Shahrazad broke off the story at once and fell courteously silent. King Shahryar was completely lost in the story.")
sh(81, "His eyes had grown wide. Suddenly he sat up and said: \"What happened next? Did the fisherman lock that jinni in?",
   [("cloth_rustle", "ތެދުވެވަޑައިގެން", -22)])
sh(82, "What did the jinni do then? Was the fisherman saved?\" Shahrazad smiled gently. \"O noble king.")
sh(83, "Dawn has come. My time is over. But if I am still in this world tomorrow night, I will tell what passed between the jinni trapped in the jar and the fisherman,")
sh(84, "and how the fisherman saved his life. It is a story even more exciting and wiser than this one.\"")
sh(85, "The longing in King Shahryar's heart had grown beyond measure. He was certain he could not bear not knowing what would happen next between the fisherman and the jinni.")
sh(86, "So again today the king decided to spare Shahrazad and not have her killed. And rising, he put on his royal robes",
   [("cloth_rustle", "ތުރުކުރައްވައިގެން", -22)], hum=True)
sh(87, "and went to the court to rule. The seventh night was over. Thanks to Shahrazad's great skill as a storyteller, the executioner's sword was put off for one more day.",
   [("footsteps_pavement", "ވަޑައިގަތެވެ", -22)])
sh(88, "Next comes the eighth night, when the result of the fisherman's cleverness will be seen. To be continued.")
SHOTS = S

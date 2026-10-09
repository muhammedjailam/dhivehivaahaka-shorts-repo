"""Beat/shot plan for Taubaa episode 287 (used by plan_beats.py)."""

LOC = {
    "living": "the small plain living room of an ordinary old Maldivian house late at night, bare whitewashed coral-stone walls, a simple low wooden cabinet with an old flat-screen TV, a worn cushioned sofa, a woven mat on a tiled floor, a ceiling fan, a single dim wall lamp",
    "exterior": "a small ordinary single-storey Maldivian house with a corrugated tin roof and a low coral-stone boundary wall on a quiet sandy island lane late at night, coconut palms, a starry sky",
    "mother_room": "the mother's small plain bedroom in an old Maldivian house late at night, whitewashed walls, a narrow wooden bed with a simple sheet, a small wooden table with a single small oil lamp, a prayer mat on the tiled floor facing a plain wall",
    "corridor": "a narrow dark corridor inside a small old Maldivian house late at night, whitewashed walls, a wooden door at the far end left half open with a pale light spilling out",
    "son_room": "the son's small cluttered bedroom in an old Maldivian house late at night, whitewashed walls, an unmade single bed, a low wooden cabinet, a single bare ceiling bulb",
    "dawn": "the sky over a small Maldivian island at the break of dawn, a calm lagoon, coconut palms in silhouette and a simple white mosque minaret against the sky",
}
MOOD = {
    "living": "late night, the cold blue-white flicker of the TV screen on his face, the rest of the room in deep teal shadow, careless and empty",
    "exterior": "late night, deep blue sky full of stars, one window glowing with warm amber lamplight and another window flickering cold blue, silence, quiet longing",
    "mother_room": "the last third of the night, warm amber glow of the small oil lamp against deep teal shadows, deep silence, prayerful, tender and sorrowful",
    "corridor": "night, deep shadows, pale light from the half-open door, sudden urgency and fear",
    "son_room": "night, harsh single bulb light and long shadows, tense turning point then tender release",
    "dawn": "dawn, soft gold light rays breaking through blue haze, peaceful, hopeful, spiritual",
}

BEATS = [
    dict(to=2, reason="episode opening: the son and his nights in front of the TV", chars=["tv_son"], loc="living",
         visual="the son slumped on a worn sofa in the dark living room, seen from the side and slightly behind the TV, his tired face lit cold blue-white by the TV glow, staring at the screen with a blank absorbed look; the TV screen itself faces away from the viewer so only its glow is seen",
         camera="medium shot, eye level, from beside the TV", amb="living_night", sens="other",
         safe="the films and dramas are never shown; the screen faces away, only its glow on his face"),
    dict(to=5, reason="characters change: the mother advises him to pray and he mocks her", chars=["devout_mother", "tv_son"], loc="living",
         visual="the frail old mother standing a few steps beside the sofa with her hands gently clasped, leaning towards her son and pleading softly with sad eyes; the son still slouched on the sofa, waving a dismissive hand at her without looking away from the TV glow, a mocking smirk on his face; the TV screen faces away from the viewer",
         camera="medium wide two-shot, eye level", amb="living_night"),
    dict(to=7, reason="scene change: the house at night — the mother's dua versus the son's late nights", loc="exterior",
         visual="the small single-storey house seen from the sandy lane at night under a sky full of stars, two small windows: the left one glowing with warm amber lamplight, the right one flickering cold blue, a faint soft golden light rising from the roof into the starry sky; no people visible",
         camera="wide establishing shot, low angle, the house in the upper half, the sandy lane forming a calm lower third", amb="night_exterior"),
    dict(to=11, reason="scene and character change: the mother in dua in the last third of the night", chars=["devout_mother"], loc="mother_room",
         visual="the old mother sitting on a prayer mat on the floor of her dim room, both palms raised before her chest in dua, eyes lifted, tears running down her wrinkled cheeks, the small oil lamp beside her casting warm amber light on her face and white headscarf",
         camera="medium shot, eye level, slightly from the side", amb="room_night"),
    dict(to=12, reason="action change: the crash — she runs crying towards her son's room", chars=["devout_mother"], loc="corridor",
         visual="the frail old mother hurrying down the narrow dark corridor towards a half-open door at the far end, one hand raised towards it, her face full of alarm, her white headscarf and sea-green dress caught in the pale light from the doorway",
         camera="medium wide, from behind and slightly to the side of her", amb="home_night"),
    dict(to=14, reason="scene and action change: the son has smashed the TV", chars=["tv_son", "devout_mother"], loc="son_room",
         visual="the son standing over an old flat-screen TV lying on the floor, its dark screen cracked across in a spider-web pattern; he holds a wooden mallet lowered loosely at his side, breathing hard, his face resolved and remorseful, looking up towards the doorway where his old mother stands frozen in surprise, one hand at her chest; nobody is hurt",
         camera="medium wide, eye level", amb="room_night", sens="violence",
         safe="the smashing itself is not shown: only the aftermath — a cracked dark screen and the tool lowered at his side; nobody is harmed"),
    dict(to=16, reason="action change: he kisses his mother's head and embraces her; her tears of joy", chars=["tv_son", "devout_mother"], loc="son_room",
         visual="the son gently embracing his small old mother, bending to kiss the top of her white headscarf, his eyes closed in remorse; the mother held against his chest, her eyes closed, tears of joy on her cheeks and a trembling grateful smile; both fully clothed, a tender modest embrace",
         camera="medium close-up, eye level", amb="room_night", sens="intimacy",
         safe="mother and son (mahram): a modest forehead/head kiss and gentle embrace, both fully clothed"),
    dict(to=19, reason="the closing Quran verse (Al-Baqarah 2:186): symbolic imagery", loc="dawn",
         visual="soft golden rays of dawn breaking through blue haze over a calm lagoon, a simple white minaret and coconut palms in silhouette against the brightening sky, no people",
         camera="wide shot, the sky and minaret in the upper two-thirds, the still lagoon as a calm lower third", amb="dawn_exterior",
         transition="dissolve", sens="other",
         safe="Quran verse shown only as symbolic dawn light and a minaret; no Arabic script rendered"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "He lived with his old mother in an ordinary little house. Most of his time he spent in front of the TV.")
sh(2, "He was very keen on watching films and dramas, and he spent his nights awake doing it.")
sh(3, "He did not go to the mosque to pray the obligatory prayers with the Muslims. And every time his old mother advised him to pray,")
sh(4, "he scolded and mocked her, and paid no attention at all to what she said. How sad that poor mother must have been! She was a powerless,",
   [("sigh", "ދެރަވާނެއެވެ", -22)])
sh(5, "frail old woman. If guidance were something that could be bought, that mother would have given everything she had to buy it for her only child.",
   hum=True)
sh(6, "That mother had only one thing... only one thing. It was dua — the duas she kept making in the last part of the night.")
sh(7, "Those are arrows that never miss their target. While her son stayed awake at night watching bad scenes,")
sh(8, "that mother rose in the last part of the night and prayed that her son be granted guidance and goodness. That is no wonder.",
   [("cloth_rustle", "ތެދުވެ", -24)])
sh(9, "For a mother's love and tenderness cannot be compared with anything else. That is a mother. A mother's love. It was the last part of one night.")
sh(10, "Silence had settled over the world. The mother was sitting in her room with both hands raised, praying to Allah.")
sh(11, "Tears were running down her cheeks — tears of grief and pain. Suddenly that deep silence was broken by a loud crash.",
   [("sob_breath", "ކަރުނަތައް", -24), ("glass_break", "އަޑުފައްގަނޑަކުންނެވެ", -14)], hum=True)
sh(12, "It was an unusual sound. Crying out 'My beloved son!', the mother ran quickly towards where the sound had come from.",
   [("gasp", "ހަޅޭއްލަވަމުން", -20), ("footsteps_pavement", "ދުވެފައި", -22)])
sh(13, "When she entered her son's room, he was smashing the TV to pieces with a mallet, saying it was the thing that had kept him from obeying Allah and his mother,",
   [("door_open", "ވަދެވުނުއިރު", -20), ("soft_thud", "ތަޅައި", -16), ("glass_break", "ސުންނާފަތި", -18)])
sh(14, "and from praying the obligatory prayers. Then he went to his mother, kissed her head, pressed her to his chest and embraced her.",
   [("cloth_rustle", "ބައްދާލިއެވެ", -22)], hum=True)
sh(15, "At that moment, as the mother stood stunned, tears ran down her cheeks. But this time they were not tears of grief and pain.",
   [("sob_breath", "ކަރުނަ", -24)])
sh(16, "They were tears of joy. In this way Allah answered that mother's dua and gave her son guidance. The word of Allah the Exalted is the truth.",
   hum=True)
sh(17, "[Al-Baqarah 2:186, recited in Arabic] \"And when My servants ask you concerning Me,")
sh(18, "(say!) then indeed I am near (to them).")
sh(19, "I answer the call of the caller when he calls upon Me.\" (The end)", hum=True)
SHOTS = S

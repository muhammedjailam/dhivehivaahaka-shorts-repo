"""Series character cards for Handi Kujaa (a horror story: Aadhambe's family of ten goes on a holiday picnic to the
popular uninhabited picnic island Beenaafushi; a storm strands them, a beautiful female spirit (handi) lures 22-year-old
Aslam into the jungle, possesses him, kills the boatman Sameer and hunts the family through a night of rain).
Creates card.json only for characters that don't exist yet. The cover shows the spirit with uncovered hair and a sheer
dress, so every reference is generated from text only and the spirit is redesigned modestly.
Usage: python characters_handikujaa.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="aadhambe", name="Aadhambe", name_dhivehi="އާދަމްބޭ",
         role="the grandfather (about 75), head of the family; pious, calm and firm; recites Quran and does ruqyah against the spirit; walks with a long wooden stick",
         gender="male", age="about 75",
         ethnicity_look=MV,
         face="thin lined face, deep-set kind but piercing dark eyes, bushy white eyebrows, neatly trimmed short white beard and white moustache",
         hair="short white hair under a white knitted skullcap",
         build="thin, slightly stooped, average height",
         default_outfit="a loose white long-sleeved collarless kurta-style shirt, a dark-brown and grey checked sarong (feyli) to the ankles, a white knitted skullcap, a long plain wooden walking stick",
         distinguishing_features="white skullcap, short white beard, long wooden walking stick, checked sarong",
         personality_cues="wise, steady, eyes widening with recognition of danger; reciting with raised cupped hands",
         visual_prompt="Aadhambe: a thin, slightly stooped Maldivian grandfather of about 75 with warm brown skin, a thin lined face, deep-set kind but piercing dark eyes, bushy white eyebrows and a neatly trimmed short white beard and moustache; wears a white knitted skullcap, a loose white long-sleeved collarless kurta-style shirt and a dark-brown and grey checked sarong to the ankles, and carries a long plain wooden walking stick."),
    dict(id="zaahid", name="Zaahid", name_dhivehi="ޒާހިދު",
         role="Aadhambe's elder son (about 50), father of Aslam and Raaidhu, Shareefa's husband; loving, anxious father",
         gender="male", age="about 50",
         ethnicity_look=MV,
         face="square weathered face, worried dark eyes, thick black moustache flecked with grey, clean-shaven chin",
         hair="short black hair greying at the temples",
         build="medium height, sturdy, slight paunch",
         default_outfit="a light sky-blue long-sleeved button shirt with the sleeves rolled to the forearm, dark-grey long trousers, black rubber sandals",
         distinguishing_features="sky-blue shirt, grey-flecked moustache, greying temples",
         personality_cues="warm smile in daylight, then frantic worry for his son",
         visual_prompt="Zaahid: a sturdy Maldivian man of about 50 with warm brown skin, a square weathered face, worried dark eyes, a thick black moustache flecked with grey, a clean-shaven chin and short black hair greying at the temples; wears a light sky-blue long-sleeved button shirt with the sleeves rolled to the forearm and dark-grey long trousers."),
    dict(id="shareefa", name="Shareefa", name_dhivehi="ޝަރީފާ",
         role="Zaahid's wife (about 47), mother of Aslam and Raaidhu; protective, prays and shields the small children",
         gender="female", age="about 47",
         ethnicity_look=MV,
         face="round motherly face, soft dark eyes, gentle mouth, faint lines at the eyes",
         hair="fully covered by a black hijab",
         build="medium height, plump",
         default_outfit="a loose long-sleeved ankle-length deep-maroon dress and a black hijab wrapped snugly, fully covering her hair and neck",
         distinguishing_features="deep-maroon dress, black hijab",
         personality_cues="tender, tearful, praying, arms spread around the children",
         visual_prompt="Shareefa: a plump Maldivian woman of about 47 with warm brown skin, a round motherly face, soft dark eyes and faint lines at the eyes; wears a loose long-sleeved ankle-length deep-maroon dress and a black hijab wrapped snugly, fully covering her hair and neck."),
    dict(id="aslam", name="Aslam", name_dhivehi="އަސްލަމް",
         role="Zaahid's son (22), Aisha's husband; talkative and curious explorer; lured and possessed by the spirit",
         gender="male", age="22",
         ethnicity_look=MV,
         face="lean youthful face, lively dark eyes, thin dark moustache and light stubble",
         hair="short thick wavy black hair",
         build="slim, wiry, average height",
         default_outfit="a mustard-yellow crew-neck t-shirt under an open short-sleeved grey-and-white checked shirt, dark-blue long jeans, black rubber sandals",
         distinguishing_features="mustard-yellow t-shirt with open grey checked shirt, wavy black hair, slim",
         personality_cues="cheerful and curious; later entranced, pale and frightened",
         visual_prompt="Aslam: a slim wiry Maldivian young man of 22 with warm brown skin, a lean youthful face, lively dark eyes, a thin dark moustache with light stubble and short thick wavy black hair; wears a mustard-yellow crew-neck t-shirt under an open short-sleeved grey-and-white checked shirt and dark-blue long jeans."),
    dict(id="aisha", name="Aisha", name_dhivehi="އާއިޝާ",
         role="Aslam's young wife (about 21); devoted and terrified for him",
         gender="female", age="about 21",
         ethnicity_look=MV,
         face="delicate oval face, large dark tearful eyes, softly arched eyebrows, small straight nose",
         hair="fully covered by a white hijab",
         build="slim, petite",
         default_outfit="a loose long-sleeved ankle-length soft lavender dress and a white hijab wrapped snugly, fully covering her hair and neck",
         distinguishing_features="lavender dress, white hijab",
         personality_cues="gentle, loving, frightened, crying for her husband",
         visual_prompt="Aisha: a slim petite Maldivian young woman of about 21 with warm brown skin, a delicate oval face, large dark eyes, softly arched eyebrows and a small straight nose; wears a loose long-sleeved ankle-length soft lavender dress and a white hijab wrapped snugly, fully covering her hair and neck."),
    dict(id="naazim", name="Naazim", name_dhivehi="ނާޒިމް",
         role="Zaahid's younger brother (about 40), uncle of Aslam and Raaidhu; big and strong, brave; uses the old iron knife against the spirits",
         gender="male", age="about 40",
         ethnicity_look=MV,
         face="broad strong face, bold dark eyes, heavy eyebrows, full short black beard",
         hair="short cropped black hair",
         build="very tall, broad-shouldered, powerfully built",
         default_outfit="a dark forest-green crew-neck t-shirt, long khaki cargo trousers, black rubber sandals",
         distinguishing_features="very big and broad, dark-green t-shirt, full black beard",
         personality_cues="steady and protective, shaken but brave",
         visual_prompt="Naazim: a very tall, broad-shouldered, powerfully built Maldivian man of about 40 with warm brown skin, a broad strong face, bold dark eyes, heavy eyebrows, a full short black beard and short cropped black hair; wears a dark forest-green crew-neck t-shirt and long khaki cargo trousers."),
    dict(id="raaidhu", name="Raaidhu", name_dhivehi="ރާއިދު",
         role="Zaahid's younger son (18), Aslam's brother; eager, frightened; later the spirit's target",
         gender="male", age="18",
         ethnicity_look=MV,
         face="boyish narrow face, wide dark eyes, faint wisp of a moustache",
         hair="short black hair with a slightly messy fringe",
         build="lanky, tall and thin",
         default_outfit="a red crew-neck t-shirt, black long track trousers with a thin white side stripe, black rubber sandals",
         distinguishing_features="red t-shirt, lanky teenager, messy fringe",
         personality_cues="eager to help, wide-eyed fear",
         visual_prompt="Raaidhu: a lanky, tall and thin Maldivian teenager of 18 with warm brown skin, a boyish narrow face, wide dark eyes, a faint wisp of a moustache and short black hair with a slightly messy fringe; wears a red crew-neck t-shirt and black long track trousers with a thin white side stripe."),
    dict(id="sameer", name="Sameer", name_dhivehi="ސަމީރު",
         role="the boat's skipper/crewman (about 38), a close family friend; stays on the dhoni to repair the engine; killed by the spirit (never shown)",
         gender="male", age="about 38",
         ethnicity_look=MV,
         face="lean sun-darkened face, narrow dark eyes, short black stubble beard",
         hair="short black hair",
         build="lean, wiry, average height",
         default_outfit="a faded navy-blue long-sleeved work shirt with the sleeves rolled up, a faded blue-and-white checked sarong to the ankles",
         distinguishing_features="faded navy work shirt, checked sarong, sun-darkened skin",
         personality_cues="practical, quiet, reliable",
         visual_prompt="Sameer: a lean, wiry Maldivian boatman of about 38 with sun-darkened brown skin, a lean face, narrow dark eyes, a short black stubble beard and short black hair; wears a faded navy-blue long-sleeved work shirt with the sleeves rolled up and a faded blue-and-white checked sarong to the ankles."),
    dict(id="handi", name="the Handi (female spirit)", name_dhivehi="ހަންޑި",
         role="the vengeful female spirit of the island (a handi) whose child was killed there a century ago; lures, possesses and hunts the family",
         gender="female", age="ageless, looks about 22",
         ethnicity_look="unearthly, Maldivian features, luminous pale-olive skin",
         face="unearthly beautiful oval face, large almond-shaped eyes that glow faintly sea-green (red when angry), calm enigmatic smile",
         hair="fully covered by a long white veil",
         build="tall, slender, seems to float",
         default_outfit="an opaque, loose, long-sleeved, ankle-length flowing white gown and a long opaque white veil wrapped over her head, fully covering her hair and neck; the very long ends of the veil and long dark smoky ribbons trail behind her on the wind; barefoot",
         distinguishing_features="opaque flowing white gown and white veil, faint sea-green glow around her, trailing dark smoky ribbons, long dark fingernails",
         personality_cues="eerie stillness, beckoning hand, hypnotic gaze",
         ref_pose="left: head-and-shoulders portrait; right: full-body standing view, the gown and veil ends drifting softly",
         visual_prompt="the Handi, a female spirit: a tall slender unearthly beautiful young woman with luminous pale-olive skin, an oval face, large almond-shaped eyes glowing faintly sea-green and a calm enigmatic smile; wears an opaque, loose, long-sleeved, ankle-length flowing white gown and a long opaque white veil wrapped over her head fully covering her hair and neck, the long veil ends and dark smoky ribbons trailing on the wind; a faint sea-green glow surrounds her; barefoot."),
]

FIRST = {c["id"]: 580 for c in CARDS}

if __name__ == "__main__":
    series_dir, episode = sys.argv[1], int(sys.argv[2])
    for c in CARDS:
        d = os.path.join(series_dir, "characters", c["id"])
        p = os.path.join(d, "card.json")
        if os.path.exists(p):
            continue
        os.makedirs(d, exist_ok=True)
        card = dict(c)
        card["first_seen_episode"] = FIRST.get(c["id"], episode)
        card["reference_from_cover"] = False
        json.dump(card, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("new", c["id"])

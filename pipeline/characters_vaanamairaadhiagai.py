"""Series character cards for Vaanama Iraadhiagai ("If God wills"; an island romance drawn in anime style: Luyoon, the
devout eldest daughter of a widowed mother, is matched with her former classmate Maaniu; jealous Naaifaa's lies split
them, they reunite, and Naaifaa finally asks forgiveness).
Creates card.json only for characters that don't exist yet.
Usage: python characters_vaanamairaadhiagai.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin, drawn in anime style"
CARDS = [
    dict(id="luyoon", name="Luyoon", name_dhivehi="ލުޔޫން",
         role="heroine; eldest of three children of the widowed Aishath (about 22), works in an office in the health sector, brave and devout, Maaniu's intended (not married)",
         gender="female", age="about 22",
         ethnicity_look=MV,
         face="soft oval anime face, large gentle dark-brown eyes with long lashes, thin dark eyebrows, small nose, small warm smile",
         hair="fully covered by a black hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length cream-white abaya-style dress, a black hijab wrapped snugly and fully covering her hair and neck, a small brown leather shoulder bag",
         distinguishing_features="cream-white dress with black hijab (like the cover), brown leather shoulder bag",
         personality_cues="bright, brave, caring big sister; quiet sad eyes when hurt",
         visual_prompt="Luyoon: a slim young Maldivian woman of about 22 with warm brown skin, a soft oval anime face, large gentle dark-brown eyes with long lashes, thin dark eyebrows and a small warm smile; wears a loose long-sleeved ankle-length cream-white abaya-style dress and a black hijab wrapped snugly and fully covering her hair and neck, a small brown leather shoulder bag."),
    dict(id="maaniu", name="Maaniu", name_dhivehi="މާނިއު",
         role="hero; Luyoon's former classmate and intended (about 24), well-mannered and prays, works at a state company, rides a motorbike",
         gender="male", age="about 24",
         ethnicity_look=MV,
         face="slim anime face, kind dark eyes, straight eyebrows, clean-shaven, gentle smile",
         hair="thick wavy-curly black hair, slightly messy",
         build="tall and slim",
         default_outfit="a dark charcoal-black jacket over a plain white long-sleeved shirt, dark trousers, black shoes",
         distinguishing_features="wavy-curly black hair, dark charcoal jacket (like the cover)",
         personality_cues="warm, teasing, sincere; ashamed and tearful when apologising",
         visual_prompt="Maaniu: a tall slim young Maldivian man of about 24 with warm brown skin, a slim clean-shaven anime face, kind dark eyes, straight eyebrows and thick wavy-curly slightly messy black hair; wears a dark charcoal-black jacket over a plain white long-sleeved shirt, dark trousers and black shoes."),
    dict(id="aishath", name="Aishath", name_dhivehi="އައިޝަތު",
         role="Luyoon's widowed mother (about 48), raised three children alone; approves of Maaniu",
         gender="female", age="about 48",
         ethnicity_look=MV,
         face="kind round anime face with soft smile lines, warm tired dark eyes",
         hair="fully covered by a headscarf",
         build="medium height, slightly plump",
         default_outfit="a loose long-sleeved ankle-length traditional Maldivian libaas dress in deep maroon with a simple gold-thread collar, and a light beige headscarf fully covering her hair and neck",
         distinguishing_features="maroon libaas, beige headscarf",
         personality_cues="loving, firm, a little sad when she thinks of her late husband",
         visual_prompt="Aishath: a Maldivian mother of about 48 with warm brown skin, a kind round anime face with soft smile lines and warm tired dark eyes, medium height and slightly plump; wears a loose long-sleeved ankle-length traditional Maldivian libaas dress in deep maroon with a simple gold-thread collar and a light beige headscarf fully covering her hair and neck."),
    dict(id="zaina", name="Zaina", name_dhivehi="ޒައިނާ",
         role="Luyoon's younger sister (about 14–15, O-level student), playful teaser and Luyoon's confidante; nickname Zen",
         gender="female", age="about 14",
         ethnicity_look=MV,
         face="round youthful anime face, big bright mischievous dark eyes, cheeky grin",
         hair="fully covered by a white hijab",
         build="small and slim, a teenage girl",
         default_outfit="a loose long-sleeved ankle-length sky-blue dress and a white hijab fully covering her hair and neck",
         distinguishing_features="sky-blue dress, white hijab, cheeky grin",
         personality_cues="lively, teasing, fiercely protective of her sister",
         visual_prompt="Zaina: a small slim Maldivian teenage girl of about 14 with warm brown skin, a round youthful anime face, big bright mischievous dark eyes and a cheeky grin; wears a loose long-sleeved ankle-length sky-blue dress and a white hijab fully covering her hair and neck."),
    dict(id="nawfal", name="Nawfal", name_dhivehi="ނައުފަލް",
         role="Luyoon's youngest sibling, a boy of about 10 (the transcripts also call him Kyle / Zen)",
         gender="male", age="about 10",
         ethnicity_look=MV,
         face="small round anime boy's face, big curious dark eyes, mischievous smile",
         hair="short neat black hair",
         build="small, a ten-year-old boy",
         default_outfit="a short-sleeved yellow t-shirt with a plain blank chest and knee-length navy shorts, rubber flip-flops",
         distinguishing_features="yellow t-shirt, mischievous grin",
         personality_cues="cheeky, energetic",
         visual_prompt="Nawfal: a small Maldivian boy of about 10 with warm brown skin, a small round anime face, big curious dark eyes, a mischievous smile and short neat black hair; wears a short-sleeved yellow t-shirt with a plain blank chest, knee-length navy shorts and rubber flip-flops."),
    dict(id="naaifaa", name="Naaifaa", name_dhivehi="ނާއިފާ",
         role="antagonist (about 23), Hawwa Manike's daughter, jealous of Luyoon and in love with Maaniu; spreads lies, later asks forgiveness",
         gender="female", age="about 23",
         ethnicity_look=MV,
         face="sharp heart-shaped anime face, narrow dark eyes with a cool sidelong look, arched eyebrows, a thin smug smile",
         hair="fully covered by a hijab",
         build="slim, slightly taller than Luyoon",
         default_outfit="a loose long-sleeved ankle-length plum-purple abaya and a pale lilac hijab fully covering her hair and neck, holding a phone",
         distinguishing_features="plum-purple abaya, lilac hijab, smug sidelong glance, phone in hand",
         personality_cues="jealous, scheming, later tearful and remorseful",
         visual_prompt="Naaifaa: a slim young Maldivian woman of about 23 with warm brown skin, a sharp heart-shaped anime face, narrow dark eyes with a cool sidelong look, arched eyebrows and a thin smug smile; wears a loose long-sleeved ankle-length plum-purple abaya and a pale lilac hijab fully covering her hair and neck."),
    dict(id="hawwa_manike", name="Hawwa Manike", name_dhivehi="ހައްވާ މަނިކެ",
         role="Naaifaa's mother (about 55), calm and wise",
         gender="female", age="about 55",
         ethnicity_look=MV,
         face="lined long anime face, calm wise dark eyes, faint frown lines",
         hair="fully covered by a headscarf",
         build="thin, medium height",
         default_outfit="a loose long-sleeved ankle-length dark-green libaas dress and a cream headscarf fully covering her hair and neck",
         distinguishing_features="dark-green libaas, cream headscarf",
         personality_cues="patient, wise, gently scolding",
         visual_prompt="Hawwa Manike: a thin Maldivian woman of about 55 with warm brown skin, a lined long anime face with calm wise dark eyes; wears a loose long-sleeved ankle-length dark-green libaas dress and a cream headscarf fully covering her hair and neck."),
    dict(id="zahuriyya", name="Zahuriyya", name_dhivehi="ޒަހުރިއްޔާ",
         role="gossiping older neighbour (about 60) who looks down on Maaniu",
         gender="female", age="about 60",
         ethnicity_look=MV,
         face="plump anime face, disapproving raised eyebrows, pursed lips",
         hair="fully covered by a headscarf",
         build="short and stout",
         default_outfit="a loose long-sleeved ankle-length mustard-yellow floral-print dress and a brown headscarf fully covering her hair and neck",
         distinguishing_features="mustard floral dress, brown headscarf, disapproving face",
         personality_cues="nosy, sharp-tongued",
         visual_prompt="Zahuriyya: a short stout Maldivian woman of about 60 with warm brown skin, a plump anime face with disapproving raised eyebrows and pursed lips; wears a loose long-sleeved ankle-length mustard-yellow floral-print dress and a brown headscarf fully covering her hair and neck."),
]

FIRST = dict(luyoon=549, aishath=549, zaina=549, nawfal=549, maaniu=565, naaifaa=576, hawwa_manike=589, zahuriyya=589)

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
        card["reference_from_cover"] = bool(c.get("reference_from_cover"))
        json.dump(card, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("new", c["id"])

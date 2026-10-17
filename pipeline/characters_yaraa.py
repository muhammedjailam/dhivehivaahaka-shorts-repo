"""Series character cards for Yaraa (a newlywed horror-mystery: three days after their wedding, Mifzaal takes his bride
Yaraa on an Eid picnic to a deserted jungle island near Male with their friends Naveen and Shifza; a hoarse woman's
voice calls Mifzaal's name from the jungle, and Yaraa and Shifza vanish).
Creates card.json only for characters that don't exist yet. The covers show Yaraa with uncovered hair, so every
reference is generated from text only.
Usage: python characters_yaraa.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="yaraa", name="Yaraa", name_dhivehi="ޔާރާ",
         role="heroine; Mifzaal's bride of three days (about 24), radiant, playful and shy; vanishes on the deserted island with Shifza",
         gender="female", age="about 24",
         ethnicity_look=MV,
         face="delicate oval face with high cheekbones, large dark expressive eyes, softly arched eyebrows, small straight nose, full lips with a natural rosy tint",
         hair="fully covered by a black hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length deep crimson-red dress with a soft flowing skirt and a gathered waist sash (like the cover), and a soft black chiffon hijab wrapped snugly, fully covering her hair and neck",
         distinguishing_features="deep crimson-red long dress with black hijab; glowing warm rim light on her face",
         personality_cues="radiant smile, shy blush, playful; later only seen in memories",
         visual_prompt="Yaraa: a slim young Maldivian woman of about 24 with warm brown skin, a delicate oval face with high cheekbones, large dark expressive eyes, softly arched eyebrows, a small straight nose and full lips with a natural rosy tint; wears a loose long-sleeved ankle-length deep crimson-red dress with a soft flowing skirt and a gathered waist sash, and a soft black chiffon hijab wrapped snugly and fully covering her hair and neck."),
    dict(id="mifzaal", name="Mifzaal", name_dhivehi="މިފްޒާލް",
         role="hero; Yaraa's husband of three days (about 29), runs his own business in Male; loving, joking, secretly carrying something about 'a father's feelings'",
         gender="male", age="about 29",
         ethnicity_look=MV,
         face="handsome lean face, warm dark-brown eyes, strong straight eyebrows, neatly trimmed short black beard and moustache",
         hair="short neat black hair, slightly longer on top and swept back",
         build="tall, athletic",
         default_outfit="a loose white linen long-sleeved shirt with the sleeves rolled to the forearm, beige chino trousers, brown leather sandals, a plain steel wristwatch",
         distinguishing_features="white linen shirt, trimmed short beard, steel wristwatch",
         personality_cues="affectionate and teasing with Yaraa, increasingly frightened and haunted",
         visual_prompt="Mifzaal: a tall athletic Maldivian man of about 29 with warm brown skin, a handsome lean face, warm dark-brown eyes, strong straight eyebrows, a neatly trimmed short black beard and moustache and short neat black hair swept back; wears a loose white linen long-sleeved shirt with the sleeves rolled to the forearm, beige chino trousers, brown leather sandals and a plain steel wristwatch."),
    dict(id="naveen", name="Naveen", name_dhivehi="ނަވީން",
         role="Shifza's husband (about 32), joker of the group; he and Shifza lost their first baby; Mifzaal's companion in the search",
         gender="male", age="about 32",
         ethnicity_look=MV,
         face="broad round friendly face, smiling dark eyes, thick eyebrows, full short black beard",
         hair="short cropped black hair",
         build="stocky, medium height, a little heavy",
         default_outfit="a navy-blue polo shirt, long grey cargo trousers, black rubber sandals",
         distinguishing_features="navy polo shirt, full short beard, stocky build",
         personality_cues="cheerful teaser; grief-stricken and shaking when Shifza vanishes",
         visual_prompt="Naveen: a stocky Maldivian man of about 32 with warm brown skin, a broad round friendly face, smiling dark eyes, thick eyebrows, a full short black beard and short cropped black hair; wears a navy-blue polo shirt, long grey cargo trousers and black rubber sandals."),
    dict(id="shifza", name="Shifza", name_dhivehi="ޝިފްޒާ",
         role="Naveen's wife (about 28), Yaraa's friend; gentle and teasing ('Shifu'); vanishes with Yaraa",
         gender="female", age="about 28",
         ethnicity_look=MV,
         face="soft round face, gentle dark eyes, dimpled smile",
         hair="fully covered by a white hijab",
         build="petite, average height",
         default_outfit="a loose long-sleeved ankle-length mint-green dress and a white hijab fully covering her hair and neck",
         distinguishing_features="mint-green dress, white hijab, dimples",
         personality_cues="warm, gently teasing, a quiet sadness in her eyes",
         visual_prompt="Shifza: a petite Maldivian woman of about 28 with warm brown skin, a soft round face, gentle dark eyes and a dimpled smile; wears a loose long-sleeved ankle-length mint-green dress and a white hijab fully covering her hair and neck."),
    dict(id="faisal", name="Faisal", name_dhivehi="ފައިސަލް",
         role="Mifzaal's closest friend and adviser in Male (about 30); phones him on the island and teases him about married life",
         gender="male", age="about 30",
         ethnicity_look=MV,
         face="slim angular face, sharp clever dark eyes behind thin black rectangular glasses, thin moustache, clean-shaven chin",
         hair="neat black hair with a side parting",
         build="slim, average height",
         default_outfit="a light-grey long-sleeved button-down shirt, dark-navy trousers, black shoes",
         distinguishing_features="thin black rectangular glasses, light-grey shirt",
         personality_cues="witty, knowing smile, loyal",
         visual_prompt="Faisal: a slim Maldivian man of about 30 with warm brown skin, a slim angular face, sharp clever dark eyes behind thin black rectangular glasses, a thin moustache, a clean-shaven chin and neat black hair with a side parting; wears a light-grey long-sleeved button-down shirt and dark-navy trousers."),
]

FIRST = dict(yaraa=573, mifzaal=573, naveen=573, shifza=573, faisal=573)

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

"""Series character cards for Sector 7 (a dystopian sci-fi story in an underground bunker city, 'The Sanctuary').
Creates card.json only for characters that don't exist yet.
Usage: python characters_sector7.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="aira", name="Aira", name_dhivehi="އައިރާ",
         role="protagonist; 26-year-old maintenance mechanic in Sector 7, the lowest level of the bunker; daughter of the vanished engineer Malik; wears his steel pendant engraved '50.12.01'",
         gender="female", age="26",
         ethnicity_look=MV,
         face="determined oval face, large dark intense eyes, straight dark eyebrows, a faint smudge of grease on one cheek",
         hair="covered by hijab",
         build="slim, athletic, average height",
         default_outfit="loose ankle-length dark olive-brown canvas work coat buttoned to the neck with long sleeves, worn loose dark trousers and scuffed boots, a charcoal-grey hijab wrapped snugly and fully covering her hair and neck, a small worn steel tag pendant on a thin chain hanging over her hijab at the chest",
         distinguishing_features="olive-brown work coat, charcoal hijab, steel tag pendant, fierce eyes",
         personality_cues="brave, defiant, compassionate, restless anger at injustice",
         visual_prompt="Aira: a slim athletic Maldivian young woman of 26 with warm brown skin, a determined oval face, large dark intense eyes, straight dark eyebrows and a faint grease smudge on one cheek; wears a loose ankle-length dark olive-brown canvas work coat buttoned to the neck with long sleeves, loose dark trousers and scuffed boots, a charcoal-grey hijab wrapped snugly and fully covering her hair and neck, and a small worn steel tag pendant on a thin chain over her hijab at the chest."),
    dict(id="zail", name="Zail", name_dhivehi="ޒައިލް",
         role="elderly former top scientist of the upper level, exiled to Sector 7 for opposing the council's corruption; lives in a hidden ruined workshop; Aira's mentor and ally; co-designed the encryption algorithm",
         gender="male", age="about 65",
         ethnicity_look=MV,
         face="lined thoughtful face, sharp piercing dark eyes, a thick bushy grey-white beard",
         hair="untidy short grey-white hair",
         build="lean, slightly stooped",
         default_outfit="patched long dark-brown coat over a faded grey long-sleeved shirt, dark trousers, fingerless wool gloves, small round wire-rimmed glasses",
         distinguishing_features="thick grey-white beard, round wire glasses, patched brown coat",
         personality_cues="brilliant, cautious, weary, flashes of anger at the council",
         visual_prompt="Zail: a lean slightly stooped Maldivian man about 65 with weathered warm brown skin, a lined thoughtful face, sharp piercing dark eyes behind small round wire-rimmed glasses, untidy short grey-white hair and a thick bushy grey-white beard; wears a patched long dark-brown coat over a faded grey long-sleeved shirt, dark trousers and fingerless wool gloves."),
    dict(id="bashir", name="Bashir", name_dhivehi="ބަޝީރު",
         role="Aira's elderly co-worker and friend in the Sector 7 engine room; timid, advises her to keep her head down",
         gender="male", age="about 60",
         ethnicity_look=MV,
         face="gaunt hollow-cheeked face, tired kind eyes, short patchy grey stubble",
         hair="thin grey hair under a dark knitted cap",
         build="thin, bony, stooped",
         default_outfit="dark knitted cap, a grimy faded blue long-sleeved work shirt and patched grey work trousers",
         distinguishing_features="knitted cap, gaunt face",
         personality_cues="fearful, gentle, beaten down",
         visual_prompt="Bashir: a thin bony stooped Maldivian man about 60 with warm brown skin, a gaunt hollow-cheeked face, tired kind eyes and short patchy grey stubble; wears a dark knitted cap, a grimy faded blue long-sleeved work shirt and patched grey work trousers."),
    dict(id="malik", name="Malik", name_dhivehi="މާލިކް",
         role="Aira's father; brilliant engineer who helped build the bunker; taken to a 'secret project' 13 years ago and never returned (killed on Marcus's orders); left the box and the pendant code",
         gender="male", age="about 45 (in memories)",
         ethnicity_look=MV,
         face="kind intelligent face, warm dark eyes, neat short black beard",
         hair="short black hair",
         build="medium build, average height",
         default_outfit="long-sleeved dark-blue engineer's jacket with many pockets over a light grey shirt, dark trousers",
         distinguishing_features="dark-blue engineer's jacket, neat beard",
         personality_cues="loving, quietly resolute",
         visual_prompt="Malik: a Maldivian man about 45 of medium build with warm brown skin, a kind intelligent face, warm dark eyes, short black hair and a neat short black beard; wears a long-sleeved dark-blue engineer's jacket with many pockets over a light grey shirt and dark trousers."),
    dict(id="brent", name="Brent", name_dhivehi="ބްރެންޓް",
         role="charismatic young leader of the underground rebel movement 'Revival' in Sector 7; secretly a paid spy of the council (Marcus/Kyle) who leads the rebels into a deadly trap",
         gender="male", age="about 30",
         ethnicity_look=MV,
         face="hard handsome angular face, intense narrow dark eyes, short black stubble beard, a confident smirk",
         hair="short black hair shaved at the sides",
         build="tall, broad-shouldered, powerful",
         default_outfit="long-sleeved dark rust-red canvas jacket with a high collar over a black shirt, dark cargo trousers, heavy boots",
         distinguishing_features="rust-red jacket, shaved sides, smirk",
         personality_cues="fiery orator, then cold, cruel and treacherous",
         visual_prompt="Brent: a tall broad-shouldered powerful Maldivian man about 30 with warm brown skin, a hard handsome angular face, intense narrow dark eyes, a short black stubble beard and short black hair shaved at the sides; wears a long-sleeved dark rust-red canvas jacket with a high collar over a black shirt, dark cargo trousers and heavy boots."),
    dict(id="kyle", name="Kyle", name_dhivehi="ކައިލް",
         role="Chief Security Commander of the city; appears to be Marcus's ruthless enforcer but is secretly working from inside to free everyone; his father was an engineer with Aira's father and he wears a matching pendant",
         gender="male", age="early 30s",
         ethnicity_look=MV,
         face="composed clean-shaven face with a strong jaw, cool watchful dark eyes, a faint scar-free calm expression",
         hair="short neat black hair, sides cut short",
         build="tall, upright, athletic",
         default_outfit="immaculate black high-collared commander's uniform with long sleeves, a row of small silver medals on the chest, black gloves and polished black boots",
         distinguishing_features="black commander uniform with silver medals",
         personality_cues="controlled, unreadable, hidden grief and honesty",
         visual_prompt="Kyle: a tall upright athletic Maldivian man in his early 30s with warm brown skin, a composed clean-shaven face with a strong jaw, cool watchful dark eyes and short neat black hair; wears an immaculate black high-collared commander's uniform with long sleeves, a row of small silver medals on the chest, black gloves and polished black boots."),
    dict(id="marcus", name="Marcus", name_dhivehi="މާކަސް",
         role="the council's leader who rules the bunker from the luxurious Level 1; hides that the surface has healed; plans 'Project Cleanslate' to gas Sector 7",
         gender="male", age="about 60",
         ethnicity_look=MV,
         face="smooth well-fed face, cold heavy-lidded dark eyes, thin lips, a neatly trimmed silver goatee",
         hair="silver hair slicked back",
         build="heavy-set, upright",
         default_outfit="tailored long-sleeved cream-white high-collared long coat with fine gold trim over dark trousers",
         distinguishing_features="cream-white coat with gold trim, slicked silver hair",
         personality_cues="cold, polished, contemptuous",
         visual_prompt="Marcus: a heavy-set upright Maldivian man about 60 with warm brown skin, a smooth well-fed face, cold heavy-lidded dark eyes, thin lips, silver hair slicked back and a neatly trimmed silver goatee; wears a tailored long-sleeved cream-white high-collared long coat with fine gold trim over dark trousers."),
]

FIRST = dict(aira=365, zail=385, bashir=365, malik=365, brent=389, kyle=389, marcus=385)

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

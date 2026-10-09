"""Series character cards for Bappage Gatulu ("Father's Killers"; a Maldivian political revenge thriller: in 2011 MP
Ahmed Zahir is murdered in front of his eight-year-old son Iyaan; fifteen years later Iyaan, now an investigative
journalist and hacker, hunts the powerful men who ordered it).
Creates card.json only for characters that don't exist yet.
Usage: python characters_bappagegatulu.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="iyaan", name="Iyaan", name_dhivehi="އިޔާން",
         role="protagonist (PRESENT, 23); investigative journalist, digital-forensics hacker and trained martial artist secretly hunting the men who ordered his father's murder",
         gender="male", age="23",
         ethnicity_look=MV,
         face="lean handsome face with high cheekbones, intense deep-set dark eyes under straight heavy eyebrows, a firm jaw, clean-shaven",
         hair="thick short black hair, swept up and back",
         build="tall, athletic and strong",
         default_outfit="a plain black crew-neck t-shirt, dark charcoal cargo trousers, black sneakers, a black digital wristwatch",
         distinguishing_features="all-black clothes, intense unsmiling gaze, swept-back black hair",
         personality_cues="patient, calculating, controlled; a cold fire behind a polite smile",
         visual_prompt="Iyaan: a tall athletic Maldivian young man of 23 with warm brown skin, a lean handsome clean-shaven face with high cheekbones, intense deep-set dark eyes under straight heavy eyebrows, a firm jaw and thick short black hair swept up and back; wears a plain black crew-neck t-shirt, dark charcoal cargo trousers and a black wristwatch.",
         reference_from_cover=True, cover_crop=[0.27, 0.29, 0.75, 0.62]),
    dict(id="iyaan_young", name="Iyaan (age 8, 2011)", name_dhivehi="އިޔާން",
         role="FLASHBACK (2011, 8 years old); Zahir's only son, who watches his father's murder from the window",
         gender="male", age="8",
         ethnicity_look=MV,
         face="small round boyish face, big dark eyes, thick eyebrows, soft cheeks",
         hair="short tousled black hair",
         build="small, slight eight-year-old boy",
         default_outfit="a soft grey-blue long-sleeved cotton t-shirt and dark navy long trousers",
         distinguishing_features="big dark eyes, grey-blue long-sleeved t-shirt",
         personality_cues="eager, loving, waiting for his father",
         visual_prompt="young Iyaan: a small slight Maldivian boy of 8 with warm brown skin, a small round face, big dark eyes, thick eyebrows and short tousled black hair; wears a soft grey-blue long-sleeved cotton t-shirt and dark navy long trousers."),
    dict(id="zahir", name="Ahmed Zahir", name_dhivehi="އަޙްމަދު ޒާހިރު",
         role="FLASHBACK (2011, about 45); Iyaan's father, an honest, beloved Member of Parliament who exposed corruption",
         gender="male", age="about 45",
         ethnicity_look=MV,
         face="kind dignified face, warm dark eyes, a short neatly trimmed black beard with a little grey",
         hair="short neat black hair with a side parting",
         build="medium height, sturdy",
         default_outfit="a dark-navy suit jacket over a long-sleeved white shirt (no tie), dark-grey trousers, black shoes, carrying a large black leather briefcase",
         distinguishing_features="navy jacket, trimmed beard, black briefcase, warm smile",
         personality_cues="warm, principled, fearless",
         visual_prompt="Ahmed Zahir: a sturdy Maldivian man of about 45 with warm brown skin, a kind dignified face, warm dark eyes, short neat side-parted black hair and a short neatly trimmed black beard with a little grey; wears a dark-navy suit jacket over a long-sleeved white shirt with no tie and dark-grey trousers."),
    dict(id="aminath_young", name="Aminath (2011)", name_dhivehi="އާމިނަތު",
         role="FLASHBACK (2011, about 35); Zahir's wife and Iyaan's mother",
         gender="female", age="about 35",
         ethnicity_look=MV,
         face="gentle oval face, soft worried dark eyes, arched eyebrows",
         hair="fully covered by a dark-green hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length deep-maroon dress and a dark-green hijab wrapped snugly and fully covering her hair and neck",
         distinguishing_features="maroon dress, dark-green hijab",
         personality_cues="loving, anxious, protective",
         visual_prompt="Aminath (2011): a slim Maldivian woman of about 35 with warm brown skin, a gentle oval face, soft worried dark eyes and arched eyebrows; wears a loose long-sleeved ankle-length deep-maroon dress and a dark-green hijab fully covering her hair and neck."),
    dict(id="aminath", name="Aminath", name_dhivehi="އާމިނަތު",
         role="PRESENT (about 50); Iyaan's widowed mother, frail and ill since the murder, always praying",
         gender="female", age="about 50",
         ethnicity_look=MV,
         face="thin gentle face with tired sunken eyes, faint lines, a weary sad smile",
         hair="fully covered by a white hijab",
         build="thin and frail",
         default_outfit="a loose long-sleeved ankle-length faded grey-blue dress and a plain white hijab fully covering her hair and neck, holding a string of prayer beads",
         distinguishing_features="white hijab, prayer beads, frail tired look",
         personality_cues="prayerful, fragile, worried for her son",
         visual_prompt="Aminath: a thin frail Maldivian woman of about 50 with warm brown skin, a thin gentle face with tired sunken eyes, faint lines and a weary sad smile; wears a loose long-sleeved ankle-length faded grey-blue dress and a plain white hijab fully covering her hair and neck, holding a string of prayer beads."),
    dict(id="asim", name="Asim", name_dhivehi="ޢާޞިމް",
         role="PRESENT (about 60); the powerful Home Minister who ordered Zahir's murder in 2011; Raaya's doting father",
         gender="male", age="about 60",
         ethnicity_look=MV,
         face="heavy square face, cold narrow dark eyes, a thick grey moustache, deep lines around the mouth, an arrogant expression",
         hair="black hair streaked with grey, slicked back",
         build="tall, heavy-set, broad",
         default_outfit="a crisp long-sleeved white shirt with buttoned cuffs, black trousers, polished black shoes, a heavy gold wristwatch",
         distinguishing_features="white shirt and black trousers, thick grey moustache, gold watch, cold arrogant gaze",
         personality_cues="arrogant, commanding, ruthless; secretly fearful",
         visual_prompt="Asim: a tall heavy-set Maldivian man of about 60 with warm brown skin, a heavy square face, cold narrow dark eyes, a thick grey moustache, deep lines around the mouth and grey-streaked black hair slicked back; wears a crisp long-sleeved white shirt with buttoned cuffs, black trousers and a heavy gold wristwatch."),
    dict(id="raaya", name="Raaya", name_dhivehi="ރާޔާ",
         role="PRESENT (about 23); Asim's only daughter, an independent-minded painter who runs the Athena Art Gallery; innocent of her father's crimes",
         gender="female", age="about 23",
         ethnicity_look=MV,
         face="soft heart-shaped face, large bright innocent dark eyes, gentle smile",
         hair="fully covered by a soft light-grey hijab",
         build="slim, graceful",
         default_outfit="a loose long-sleeved ankle-length plain white dress and a soft light-grey hijab wrapped snugly and fully covering her hair and neck",
         distinguishing_features="white dress, light-grey hijab, a faint smudge of paint on one sleeve cuff",
         personality_cues="warm, artistic, trusting, idealistic",
         visual_prompt="Raaya: a slim graceful Maldivian young woman of about 23 with warm brown skin, a soft heart-shaped face, large bright innocent dark eyes and a gentle smile; wears a loose long-sleeved ankle-length plain white dress and a soft light-grey hijab wrapped snugly and fully covering her hair and neck."),
    dict(id="sameer", name="Sameer", name_dhivehi="ސަމީރު",
         role="PRESENT (about 62); Speaker of Parliament, the political brain who covered up Zahir's murder",
         gender="male", age="about 62",
         ethnicity_look=MV,
         face="round fleshy face, shrewd small eyes behind round wire-rimmed glasses, a clean-shaven double chin",
         hair="balding, with a short grey fringe at the sides",
         build="short and plump",
         default_outfit="a dark-grey three-piece suit, a long-sleeved white shirt and a maroon tie",
         distinguishing_features="round glasses, balding head, maroon tie",
         personality_cues="calm, cunning, experienced",
         visual_prompt="Sameer: a short plump Maldivian man of about 62 with warm brown skin, a round fleshy clean-shaven face, shrewd small eyes behind round wire-rimmed glasses and a balding head with a short grey fringe; wears a dark-grey three-piece suit, a long-sleeved white shirt and a maroon tie."),
    dict(id="fareed", name="Fareed", name_dhivehi="ފަރީދު",
         role="PRESENT (about 55); managing director of the biggest private bank, who paid for Zahir's murder",
         gender="male", age="about 55",
         ethnicity_look=MV,
         face="long lean face, sharp nervous dark eyes, hollow cheeks, a thin black moustache",
         hair="glossy black hair combed straight back",
         build="tall and thin",
         default_outfit="a navy pinstripe suit, a long-sleeved light-blue shirt and a silver tie",
         distinguishing_features="navy pinstripe suit, thin moustache, glossy slicked hair",
         personality_cues="greedy, suspicious, quick-tempered",
         visual_prompt="Fareed: a tall thin Maldivian man of about 55 with warm brown skin, a long lean face with hollow cheeks, sharp nervous dark eyes, a thin black moustache and glossy black hair combed straight back; wears a navy pinstripe suit, a long-sleeved light-blue shirt and a silver tie."),
]

FIRST = dict(iyaan=520, iyaan_young=520, zahir=520, aminath_young=520, aminath=520, asim=521, raaya=522,
             sameer=529, fareed=529)

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

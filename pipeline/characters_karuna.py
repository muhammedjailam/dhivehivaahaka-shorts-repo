"""Series character cards for Karuna (a Malé family drama: Shima, the only daughter of a proud wealthy family, is deceived
by her college boyfriend Yazan, becomes pregnant, is thrown out into the rain by her father Qasim, is taken in by the
kind childless Aisamanike, raises her daughter Zeeva alone, succeeds, and seven years later forgives her broken father).
Creates card.json only for characters that don't exist yet. Only Naseema is taken from the cover (crop); everyone else
is generated from text.
Usage: python characters_karuna.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="shima", name="Shima", name_dhivehi="ޝިމާ",
         role="protagonist; the only, much-loved daughter (20) of a wealthy, respected Malé family; college student who is deceived, becomes pregnant and is thrown out of home",
         gender="female", age="20",
         ethnicity_look=MV,
         face="soft oval face, large expressive dark eyes, gentle arched eyebrows, small nose, full lips, a wide bright smile when happy",
         hair="fully covered by a cream hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length dusty-lavender dress and a cream hijab fully covering her hair and neck",
         distinguishing_features="dusty-lavender dress, cream hijab, big expressive eyes",
         personality_cues="innocent and cheerful at first; later frightened, ashamed and tearful; then quietly determined",
         visual_prompt="Shima: a slim young Maldivian woman of 20 with warm brown skin, a soft oval face, large expressive dark eyes, gentle arched eyebrows, a small nose and full lips; wears a loose long-sleeved ankle-length dusty-lavender dress and a cream hijab fully covering her hair and neck."),
    dict(id="shima_older", name="Shima (seven years later)", name_dhivehi="ޝިމާ",
         role="Shima at about 28, seven years later: a confident, respected senior manager at a successful company and a devoted single mother",
         gender="female", age="about 28",
         ethnicity_look=MV,
         face="soft oval face, calm confident large dark eyes, gentle arched eyebrows, small nose, a warm composed smile",
         hair="fully covered by an ivory hijab",
         build="slim, average height, upright poised posture",
         default_outfit="an elegant loose long-sleeved ankle-length camel-brown abaya-style coat dress over a cream inner dress, an ivory hijab fully covering her hair and neck, a small simple wristwatch",
         distinguishing_features="camel-brown coat dress, ivory hijab, poised posture",
         personality_cues="calm, strong, warm; the old pain shows only in her eyes",
         visual_prompt="Shima at about 28: a slim, poised Maldivian woman with warm brown skin, a soft oval face, calm confident large dark eyes, gentle arched eyebrows and a warm composed smile; wears an elegant loose long-sleeved ankle-length camel-brown abaya-style coat dress over a cream inner dress, an ivory hijab fully covering her hair and neck, and a small simple wristwatch."),
    dict(id="qasim", name="Qasim", name_dhivehi="ޤާސިމް",
         role="Shima's father (about 55): a wealthy, highly respected Malé businessman, strict, proud and obsessed with his name and honour",
         gender="male", age="about 55",
         ethnicity_look=MV,
         face="square stern face, hard proud dark eyes, heavy brows, neatly trimmed salt-and-pepper moustache, clean-shaven chin, deep frown lines",
         hair="short neatly combed salt-and-pepper hair",
         build="tall, solid, upright commanding posture",
         default_outfit="a crisp white long-sleeved button shirt, dark charcoal trousers, a polished leather belt, a gold wristwatch",
         distinguishing_features="crisp white shirt, salt-and-pepper moustache, commanding posture",
         personality_cues="stern, proud, controlling; explosive anger",
         visual_prompt="Qasim: a tall, solid Maldivian man of about 55 with warm brown skin, a square stern face, hard proud dark eyes, heavy brows, a neatly trimmed salt-and-pepper moustache, a clean-shaven chin and short neatly combed salt-and-pepper hair; wears a crisp white long-sleeved button shirt, dark charcoal trousers, a polished leather belt and a gold wristwatch."),
    dict(id="qasim_old", name="Qasim (seven years later)", name_dhivehi="ޤާސިމް",
         role="Qasim seven years later: broken, aged far beyond his years, walking slowly with a cane, full of regret",
         gender="male", age="looks about 70",
         ethnicity_look=MV,
         face="gaunt hollow-cheeked face with deep wrinkles, sad tearful dark eyes, a thin completely white moustache, white stubble",
         hair="thin, completely white hair",
         build="thin, frail, stooped, leaning on a wooden walking cane",
         default_outfit="a loose faded grey long-sleeved shirt hanging on his thin frame, old dark trousers, worn sandals, a plain wooden walking cane",
         distinguishing_features="completely white hair, stooped frail body, wooden cane, faded grey shirt",
         personality_cues="broken, ashamed, pleading, humble",
         visual_prompt="old Qasim: a thin, frail, stooped Maldivian man who looks about 70, with warm brown skin, a gaunt hollow-cheeked deeply wrinkled face, sad tearful dark eyes, a thin completely white moustache, white stubble and thin completely white hair; wears a loose faded grey long-sleeved shirt hanging on his thin frame, old dark trousers and worn sandals, and leans on a plain wooden walking cane."),
    dict(id="naseema", name="Naseema", name_dhivehi="ނަސީމާ",
         role="Shima's mother (about 48): gentle, quiet, devoted to her daughter; powerless against her husband",
         gender="female", age="about 48",
         ethnicity_look=MV,
         face="soft rounded face with fine lines, gentle sorrowful dark-brown eyes, tear-streaked when upset",
         hair="fully covered by a dark navy hijab",
         build="medium height, soft build",
         default_outfit="a loose long-sleeved ankle-length dark charcoal dress with a fine grey patterned print, and a dark navy hijab fully covering her hair, neck and shoulders",
         distinguishing_features="dark navy hijab, grey-patterned charcoal dress, sorrowful eyes (the woman on the cover)",
         personality_cues="soft-spoken, loving, anxious, tearful",
         visual_prompt="Naseema: a Maldivian woman of about 48 with warm brown skin, a soft rounded face with fine lines and gentle sorrowful dark-brown eyes; wears a loose long-sleeved ankle-length dark charcoal dress with a fine grey patterned print and a dark navy hijab fully covering her hair, neck and shoulders.",
         reference_from_cover=True, cover_crop=[0.26, 0.03, 1.0, 0.60]),
    dict(id="yazan", name="Yazan", name_dhivehi="ޔަޒަން",
         role="handsome, smooth-talking college student (22) who seduces Shima with promises of marriage and abandons her when she is pregnant",
         gender="male", age="22",
         ethnicity_look=MV,
         face="handsome angular face, deep dark eyes with a confident gaze, a slight charming smile, neatly trimmed light stubble",
         hair="thick black hair styled up and swept back",
         build="tall, slim-athletic",
         default_outfit="a fitted plain white t-shirt under an open light-grey long-sleeved overshirt, dark blue jeans, white sneakers",
         distinguishing_features="light-grey open overshirt over white t-shirt, swept-back styled hair, charming smile",
         personality_cues="charming and attentive at first; later cold, contemptuous and dismissive",
         visual_prompt="Yazan: a tall, slim-athletic Maldivian man of 22 with warm brown skin, a handsome angular face, deep dark eyes with a confident gaze, a slight charming smile, neatly trimmed light stubble and thick black hair styled up and swept back; wears a fitted plain white t-shirt under an open light-grey long-sleeved overshirt, dark blue jeans and white sneakers."),
    dict(id="aisamanike", name="Aisamanike", name_dhivehi="އައިސާމަނިކެ",
         role="a kind, elderly, childless woman (about 68) who lives alone in a small old house; takes Shima in and treats her as her own daughter",
         gender="female", age="about 68",
         ethnicity_look=MV,
         face="round deeply lined kind face, warm smiling dark eyes with crow's feet, soft cheeks",
         hair="fully covered by a white headscarf",
         build="short, plump, slightly stooped",
         default_outfit="a traditional loose long-sleeved ankle-length faded sage-green libaas (dhigu hedhun) with a simple embroidered neckline, and a white headscarf fully covering her hair and neck",
         distinguishing_features="faded sage-green libaas, white headscarf, warm smile",
         personality_cues="tender, motherly, unbothered by gossip, full of faith",
         visual_prompt="Aisamanike: a short, plump, slightly stooped elderly Maldivian woman of about 68 with warm brown skin, a round deeply lined kind face and warm smiling dark eyes with crow's feet; wears a traditional loose long-sleeved ankle-length faded sage-green libaas (dhigu hedhun) with a simple embroidered neckline and a white headscarf fully covering her hair and neck."),
    dict(id="zeeva", name="Zeeva", name_dhivehi="ޒީވާ",
         role="Shima's daughter at 7: bright, sweet, well-mannered and always smiling",
         gender="female", age="7",
         ethnicity_look=MV,
         face="round sweet child's face, big bright dark eyes, dimpled smile",
         hair="covered by a small white child's headscarf",
         build="small seven-year-old girl",
         default_outfit="a loose long-sleeved ankle-length pale-yellow dress and a small white child's headscarf covering her hair",
         distinguishing_features="pale-yellow dress, small white headscarf, big bright eyes",
         personality_cues="cheerful, chatty, curious, a little shy with strangers",
         visual_prompt="Zeeva: a small seven-year-old Maldivian girl with warm brown skin, a round sweet face, big bright dark eyes and a dimpled smile; wears a loose long-sleeved ankle-length pale-yellow dress and a small white child's headscarf covering her hair."),
    dict(id="nurse", name="the nurse", name_dhivehi="ނަރުސް",
         role="an experienced, kind hospital nurse (about 40) who holds Shima's hand during the birth",
         gender="female", age="about 40",
         ethnicity_look=MV,
         face="calm oval face, kind steady dark eyes",
         hair="fully covered by a white hijab",
         build="medium height",
         default_outfit="loose light-blue long-sleeved nurse scrubs (tunic and trousers) and a white hijab fully covering her hair and neck, no badge",
         distinguishing_features="light-blue scrubs, white hijab",
         personality_cues="calm, reassuring, gentle",
         visual_prompt="the nurse: a Maldivian woman of about 40 with warm brown skin, a calm oval face and kind steady dark eyes; wears loose light-blue long-sleeved nurse scrubs and a white hijab fully covering her hair and neck, no badge."),
]

FIRST = dict(shima=335, shima_older=337, qasim=335, qasim_old=337, naseema=335, yazan=335, aisamanike=336, zeeva=337,
             nurse=337)

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

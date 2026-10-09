"""Series character cards for Nindheveethimeymathee (ނިންދެވޭތީ މޭމަތީ; a Malé romance drama on three timelines:
PRESENT — writer Lail returns after nine years and meets again Saba, now a TV presenter in an unhappy marriage;
SCHOOL — their A-level years, Lail's parents Haizum and Sana, Sana's death; PAST — Haizum's "one mistake" with Shifa on a
business trip to Vietnam, Sana's lost baby). Age-split cards: lail / lail_young / lail_child, saba / saba_young, etc.
Creates card.json only for characters that don't exist yet.
Usage: python characters_nindheveethimeymathee.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"


def card(id, name, dv, role, gender, age, face, hair, build, outfit, features, cues, vp, **kw):
    return dict(id=id, name=name, name_dhivehi=dv, role=role, gender=gender, age=age, ethnicity_look=kw.pop("eth", MV),
                face=face, hair=hair, build=build, default_outfit=outfit, distinguishing_features=features,
                personality_cues=cues, visual_prompt=vp, **kw)


CARDS = [
    # ---------------------------------------------------------------- PRESENT timeline
    card("lail", "Lail (Ahmed Laail Haizum)", "ލައިލް", "male lead (present, about 29): award-winning writer whose stories become films; "
         "back in the Maldives after nine years; lives in a Hulhumalé beachfront penthouse", "male", "about 29",
         "handsome lean face, thoughtful deep-set dark eyes under thick straight black eyebrows, light stubble, a quiet half-smile",
         "short thick black hair swept back, slightly tousled", "tall, lean",
         "a slate-blue long-sleeved henley shirt with the sleeves pushed up and dark trousers", "thick straight eyebrows, light stubble, slate-blue henley",
         "reserved, camera-shy, intense steady gaze",
         "Lail: a tall lean Maldivian man of about 29 with warm brown skin, a handsome lean face, thoughtful deep-set dark eyes under thick straight black eyebrows, light stubble and short thick black hair swept back; wears a slate-blue long-sleeved henley shirt with the sleeves pushed up and dark trousers."),
    card("saba", "Saba", "ސަބާ", "female lead (present, about 28): TV presenter of the talk show 'Tharinnaa Eku', married to Zuhuruf "
         "(an unhappy, controlling marriage); Lail's first love from school", "female", "about 28",
         "soft oval face, very large dark eyes with long lashes, gentle arched eyebrows, small nose, full lips, a sad guarded look",
         "fully covered by a pale-lavender hijab", "slim, average height",
         "an elegant loose long-sleeved ankle-length dusty-lavender dress with a subtle pattern of small blue and lilac flowers, and a pale-lavender hijab wrapped snugly and fully covering her hair and neck; a thin ring",
         "very large dark eyes, lavender floral dress, pale-lavender hijab", "poised on camera, fragile and tearful off camera",
         "Saba: a slim Maldivian woman of about 28 with warm brown skin, a soft oval face, very large dark eyes with long lashes, gentle arched eyebrows and full lips; wears an elegant loose long-sleeved ankle-length dusty-lavender dress with a subtle pattern of small blue and lilac flowers and a pale-lavender hijab wrapped snugly and fully covering her hair and neck."),
    card("miya", "Miya", "މިޔާ", "Saba's co-host and blunt protective friend (present)", "female", "about 28",
         "heart-shaped face, sharp lively dark eyes, a confident wry smile", "fully covered by a black hijab", "medium height, slim",
         "a loose long-sleeved ankle-length deep-burgundy dress with a fitted plain blazer over it and a black hijab fully covering her hair and neck",
         "burgundy dress, black hijab", "outspoken, protective, impatient",
         "Miya: a slim Maldivian woman of about 28 with warm brown skin, a heart-shaped face, sharp lively dark eyes and a confident wry smile; wears a loose long-sleeved ankle-length deep-burgundy dress with a plain blazer over it and a black hijab fully covering her hair and neck."),
    card("zavee", "Zavee", "ޒަވީ", "producer of the TV show (present)", "male", "about 35",
         "round friendly face, short trimmed beard, busy eyes", "short black hair", "stocky, medium height",
         "a black polo shirt, dark trousers and a headset hanging around his neck", "headset, black polo", "busy, hurried",
         "Zavee: a stocky Maldivian man of about 35 with warm brown skin, a round friendly face, a short trimmed beard and short black hair; wears a black polo shirt, dark trousers and a headset hanging around his neck."),
    card("sadhee", "Sadhee", "ސަދީ", "Saba's closest friend since school (present, about 28)", "female", "about 28",
         "round cheerful face, bright dark eyes, dimpled cheeks", "fully covered by a cream hijab", "short, slightly plump",
         "a loose long-sleeved ankle-length rust-orange dress and a cream hijab fully covering her hair and neck",
         "rust-orange dress, cream hijab, dimples", "warm, fierce, quick-tempered",
         "Sadhee: a short slightly plump Maldivian woman of about 28 with warm brown skin, a round cheerful face, bright dark eyes and dimpled cheeks; wears a loose long-sleeved ankle-length rust-orange dress and a cream hijab fully covering her hair and neck."),
    card("asil", "Asil", "އަސިލް", "Lail's best friend and Saba's cousin (present, about 29)", "male", "about 29",
         "round good-natured face, laughing eyes, a short full black beard", "short curly black hair", "broad, stocky",
         "a maroon polo shirt and dark-grey trousers", "curly hair, full short beard, maroon polo", "joker, emotional, loyal",
         "Asil: a broad stocky Maldivian man of about 29 with warm brown skin, a round good-natured face, laughing eyes, short curly black hair and a short full black beard; wears a maroon polo shirt and dark-grey trousers."),
    card("shahid", "Shahid", "ޝާހިދު", "friend from school (present, about 29)", "male", "about 29",
         "narrow sharp-jawed face, clean-shaven, alert eyes", "short neat black hair with a side parting", "slim, tall",
         "a white long-sleeved button shirt with rolled sleeves and black trousers", "sharp jaw, white shirt", "calm, practical",
         "Shahid: a slim tall Maldivian man of about 29 with warm brown skin, a narrow sharp-jawed clean-shaven face, alert eyes and short neat black hair with a side parting; wears a white long-sleeved button shirt with rolled sleeves and black trousers."),
    # ---------------------------------------------------------------- SCHOOL timeline (A-level years)
    card("lail_young", "Lail (17)", "ލައިލް", "Lail at 17 (school timeline): shy clever A-level student who writes poetry; son of Haizum and Sana",
         "male", "about 17",
         "boyish lean face, soft thoughtful dark eyes under thick straight black eyebrows, clean-shaven, shy smile",
         "short neat black hair", "slim, tall for his age",
         "a plain light-grey crew-neck t-shirt (blank chest) and dark jeans", "thick straight eyebrows, shy smile",
         "shy, gentle, poetic",
         "young Lail: a slim tall Maldivian boy of about 17 with warm brown skin, a boyish lean clean-shaven face, soft thoughtful dark eyes under thick straight black eyebrows and short neat black hair; wears a plain light-grey crew-neck t-shirt with a blank chest and dark jeans."),
    card("saba_young", "Saba (17)", "ސަބާ", "Saba at 17 (school timeline): raised in Australia, came to Malé after her father died; lives with "
         "her cousin Asil's family; speaks mostly English", "female", "about 17",
         "youthful soft oval face, very large bright dark eyes with long lashes, small nose, playful smile",
         "fully covered by a white hijab", "slim, petite",
         "a loose long-sleeved ankle-length powder-blue dress and a white hijab wrapped snugly and fully covering her hair and neck",
         "very large bright eyes, powder-blue dress, white hijab", "bold, teasing, quick to blush",
         "young Saba: a slim petite Maldivian girl of about 17 with warm brown skin, a youthful soft oval face, very large bright dark eyes with long lashes and a playful smile; wears a loose long-sleeved ankle-length powder-blue dress and a white hijab wrapped snugly and fully covering her hair and neck."),
    card("asil_young", "Asil (17)", "އަސިލް", "Asil at 17: Lail's best friend, Saba's cousin; the group's joker and matchmaker", "male", "about 17",
         "round boyish face, laughing eyes, clean-shaven", "short curly black hair", "stocky",
         "a maroon t-shirt and grey track trousers", "curly hair, maroon t-shirt", "joker, teasing",
         "young Asil: a stocky Maldivian boy of about 17 with warm brown skin, a round boyish clean-shaven face, laughing eyes and short curly black hair; wears a maroon t-shirt and grey track trousers."),
    card("sadhee_young", "Sadhee (17)", "ސަދީ", "Sadhee at 17: Saba's friend and classmate", "female", "about 17",
         "round cheerful face, bright dark eyes, dimpled cheeks", "fully covered by a cream hijab", "short, slightly plump",
         "a loose long-sleeved ankle-length rust-orange dress and a cream hijab fully covering her hair and neck",
         "rust-orange dress, cream hijab, dimples", "warm, dramatic",
         "young Sadhee: a short slightly plump Maldivian girl of about 17 with warm brown skin, a round cheerful face, bright dark eyes and dimpled cheeks; wears a loose long-sleeved ankle-length rust-orange dress and a cream hijab fully covering her hair and neck."),
    card("shahid_young", "Shahid (17)", "ޝާހިދު", "Shahid at 17: classmate and friend", "male", "about 17",
         "narrow sharp-jawed boyish face, clean-shaven", "short neat black hair with a side parting", "slim, tall",
         "a white t-shirt and black jeans", "sharp jaw, side parting", "cool, a little cocky",
         "young Shahid: a slim tall Maldivian boy of about 17 with warm brown skin, a narrow sharp-jawed clean-shaven face and short neat black hair with a side parting; wears a white t-shirt and black jeans."),
    card("laira", "Laira", "ލައިރާ", "Lail's elder sister (school timeline, about 19)", "female", "about 19",
         "gentle oval face, soft dark eyes, a kind sad smile", "fully covered by a dove-grey hijab", "slim, medium height",
         "a loose long-sleeved ankle-length dusty-pink dress and a dove-grey hijab fully covering her hair and neck",
         "dusty-pink dress, dove-grey hijab", "caring, emotional, likes singing",
         "Laira: a slim Maldivian young woman of about 19 with warm brown skin, a gentle oval face, soft dark eyes and a kind sad smile; wears a loose long-sleeved ankle-length dusty-pink dress and a dove-grey hijab fully covering her hair and neck."),
    card("haizum", "Haizum", "ހައިޒުމް", "Lail and Laira's father, wealthy CEO; the man whose one mistake (an affair with Shifa in Vietnam) "
         "broke his marriage to Sana; about 38 in the PAST timeline, about 48 in the SCHOOL timeline", "male", "about 42",
         "strong square face, the same thick straight black eyebrows as Lail, deep tired dark eyes, a neatly trimmed black beard with a few grey flecks",
         "short neat black hair with a little grey at the temples", "tall, broad-shouldered",
         "a dark-navy suit with a white open-collar shirt (no tie)", "thick eyebrows, trimmed beard with grey flecks, navy suit",
         "powerful but guilt-ridden, tender with his children",
         "Haizum: a tall broad-shouldered Maldivian man of about 42 with warm brown skin, a strong square face, thick straight black eyebrows, deep tired dark eyes, a neatly trimmed black beard with a few grey flecks and short neat black hair greying slightly at the temples; wears a dark-navy suit with a white open-collar shirt and no tie."),
    card("sana", "Sana", "ސަނާ", "Haizum's wife, mother of Laira and Lail; heartbroken by his betrayal, depressed, later seriously ill; "
         "dies in the school timeline (ep 401)", "female", "about 38",
         "delicate oval face, sorrowful dark eyes, high cheekbones, a faint tired smile",
         "fully covered by an ivory hijab", "slim, slender",
         "a loose long-sleeved ankle-length sage-green dress and an ivory hijab fully covering her hair and neck",
         "sage-green dress, ivory hijab", "gentle, proud, wounded",
         "Sana: a slender Maldivian woman of about 38 with warm brown skin, a delicate oval face, high cheekbones, sorrowful dark eyes and a faint tired smile; wears a loose long-sleeved ankle-length sage-green dress and an ivory hijab fully covering her hair and neck."),
    card("shafeeqa", "Shafeeqa (Maama)", "ޝަފީޤާ", "Haizum's mother, the children's grandmother 'Maama'", "female", "about 65",
         "kind wrinkled round face, warm dark eyes behind thin gold-rimmed glasses", "fully covered by a white headscarf",
         "short, plump", "a traditional loose long-sleeved ankle-length dark-maroon libaas dress and a white headscarf fully covering her hair and neck",
         "gold-rimmed glasses, maroon libaas, white headscarf", "warm, wise, firm",
         "Maama Shafeeqa: a short plump Maldivian grandmother of about 65 with warm brown skin, a kind wrinkled round face and warm dark eyes behind thin gold-rimmed glasses; wears a traditional loose long-sleeved ankle-length dark-maroon libaas dress and a white headscarf fully covering her hair and neck."),
    # ---------------------------------------------------------------- PAST timeline (Vietnam trip, Sana's lost baby)
    card("lail_child", "Lail (10)", "ލައިލް", "Lail at 10 (past timeline)", "male", "about 10",
         "small boyish face, big curious dark eyes under thick black eyebrows", "short black hair", "small, slim",
         "a striped blue-and-white t-shirt and long khaki trousers", "thick eyebrows, striped t-shirt", "sweet, curious",
         "little Lail: a slim Maldivian boy of about 10 with warm brown skin, a small boyish face, big curious dark eyes under thick black eyebrows and short black hair; wears a striped blue-and-white t-shirt and long khaki trousers."),
    card("laira_child", "Laira (12)", "ލައިރާ", "Laira at 12 (past timeline)", "female", "about 12",
         "small gentle oval face, soft dark eyes", "fully covered by a small dove-grey hijab", "small, slim",
         "a loose long-sleeved ankle-length pink dress and a small dove-grey hijab fully covering her hair and neck",
         "pink dress, small grey hijab", "caring big sister",
         "little Laira: a slim Maldivian girl of about 12 with warm brown skin, a small gentle oval face and soft dark eyes; wears a loose long-sleeved ankle-length pink dress and a small dove-grey hijab fully covering her hair and neck."),
    card("shifa", "Shifa", "ޝިފާ", "Haizum's old friend from tuition days, married, living in Australia; the woman of his 'one mistake' "
         "in Vietnam (past timeline)", "female", "about 35",
         "striking angular face, lively almond-shaped dark eyes, a bright chatty smile", "fully covered by a pale-gold hijab",
         "slim, tall", "a loose long-sleeved ankle-length plain white dress and a pale-gold hijab fully covering her hair and neck",
         "white dress, pale-gold hijab", "talkative, stubborn, restless",
         "Shifa: a slim tall Maldivian woman of about 35 with warm brown skin, a striking angular face, lively almond-shaped dark eyes and a bright chatty smile; wears a loose long-sleeved ankle-length plain white dress and a pale-gold hijab fully covering her hair and neck."),
    card("daniyal", "Daniyal", "ދަނިޔާލް", "Haizum's close friend and business partner (past timeline)", "male", "about 38",
         "round jovial face, thick black moustache and short beard, twinkling eyes", "short receding black hair", "stout",
         "a light-blue long-sleeved shirt and khaki trousers", "moustache, stout, light-blue shirt", "cheerful, loyal",
         "Daniyal: a stout Maldivian man of about 38 with warm brown skin, a round jovial face, a thick black moustache and short beard, twinkling eyes and short receding black hair; wears a light-blue long-sleeved shirt and khaki trousers."),
    card("shaneez", "Shaneez", "ޝާނީޒު", "lawyer friend of Haizum and Daniyal (past timeline, ep 552)", "male", "about 38",
         "thin serious face, rectangular black-framed glasses, clean-shaven", "short neat black hair", "thin, medium height",
         "a charcoal-grey suit, white shirt and dark tie", "black-framed glasses, charcoal suit", "precise, cautious",
         "Shaneez: a thin Maldivian man of about 38 with warm brown skin, a thin serious clean-shaven face, rectangular black-framed glasses and short neat black hair; wears a charcoal-grey suit, a white shirt and a dark tie."),
]

FIRST = dict(lail=269, saba=269, miya=269, zavee=269, sadhee=271, asil=271, shahid=271,
             lail_young=276, saba_young=276, asil_young=276, sadhee_young=295, shahid_young=295,
             haizum=295, laira=339, shafeeqa=339, sana=400, lail_child=445, laira_child=445,
             shifa=442, daniyal=445, shaneez=552)

if __name__ == "__main__":
    series_dir, episode = sys.argv[1], int(sys.argv[2])
    for c in CARDS:
        d = os.path.join(series_dir, "characters", c["id"])
        p = os.path.join(d, "card.json")
        if os.path.exists(p):
            continue
        os.makedirs(d, exist_ok=True)
        cd = dict(c)
        cd["first_seen_episode"] = FIRST.get(c["id"], episode)
        cd["reference_from_cover"] = False
        json.dump(cd, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("new", c["id"])

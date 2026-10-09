"""Series character cards for Mamma (މަންމަ) — a Maldivian family drama: orphaned Shahula is raised in Malé by the kind
Azeeza, marries Azeeza's son Aamir and suffers his cruelty and betrayal.
Creates card.json only for characters that don't exist yet. Adult Shahula's reference uses a crop of the series poster
(the woman on the bench); all other references are text-only.
Usage: python characters_mamma.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"


def C(id, name, dv, role, gender, age, face, hair, build, outfit, dist, pers, vp, look=MV, **kw):
    return dict(id=id, name=name, name_dhivehi=dv, role=role, gender=gender, age=age, ethnicity_look=look, face=face,
                hair=hair, build=build, default_outfit=outfit, distinguishing_features=dist, personality_cues=pers,
                visual_prompt=vp, **kw)


CARDS = [
    C("shahula", "Shahula", "ޝަހުލާ",
      "protagonist; orphan raised in Malé by Azeeza, later Aamir's wife and Zidhaan's mother, about 24",
      "female", "about 24",
      "soft oval face, large dark expressive eyes with long lashes, thick softly arched eyebrows, small straight nose, full lips",
      "fully covered by a hijab", "slim, average height",
      "a loose long-sleeved ankle-length dusty-rose house dress and a cream hijab fully covering her hair and neck",
      "large sad dark eyes, gentle dignified bearing", "gentle, patient, quietly strong, often near tears",
      "Shahula: a slim Maldivian woman of about 24 with light warm-brown skin, a soft oval face, large dark expressive eyes "
      "with long lashes, thick softly arched eyebrows, a small straight nose and full lips; wears a loose long-sleeved "
      "ankle-length dusty-rose house dress and a cream hijab fully covering her hair and neck.",
      look="Maldivian, South Asian features, light warm-brown skin",
      reference_from_cover=True, cover_crop=[0.45, 0.24, 0.90, 0.62]),
    C("shahula_young", "Shahula (teen)", "ޝަހުލާ",
      "Shahula at about 17: studious schoolgirl living at Azeeza's house in Malé",
      "female", "about 17",
      "youthful soft oval face, large dark expressive eyes, thick softly arched eyebrows, small straight nose",
      "fully covered by a white hijab", "slim",
      "Maldivian girls' school uniform: a white long-sleeved ankle-length tunic dress with a navy-blue belt, a white hijab fully covering her hair and neck, no badge, no lettering",
      "white school uniform, large gentle eyes", "shy, studious, polite, a little sad",
      "teenage Shahula: a slim Maldivian girl of about 17 with light warm-brown skin, a youthful soft oval face, large dark "
      "expressive eyes and thick softly arched eyebrows; wears a white long-sleeved ankle-length school tunic dress with a "
      "navy-blue belt and a white hijab fully covering her hair and neck.",
      look="Maldivian, South Asian features, light warm-brown skin"),
    C("shahula_child", "Shahula (child)", "ޝަހުލާ",
      "Shahula at 12 on her home island, just orphaned",
      "female", "12",
      "small round childish face, big dark eyes, thick eyebrows",
      "covered by a white headscarf", "slim, small",
      "a faded pink long-sleeved ankle-length cotton dress and a white headscarf fully covering her hair and neck",
      "faded pink dress, big tearful eyes", "grieving, quiet, frightened",
      "12-year-old Shahula: a small slim Maldivian girl with light warm-brown skin, a small round childish face, big dark "
      "eyes and thick eyebrows; wears a faded pink long-sleeved ankle-length cotton dress and a white headscarf fully "
      "covering her hair and neck.",
      look="Maldivian, South Asian features, light warm-brown skin"),
    C("khadheeja", "Khadheeja", "ޚަދީޖާ",
      "Shahula's mother, a brave single mother who did housework for other families; died on a stormy night (memories only)",
      "female", "about 38",
      "thin gentle face, tired kind dark eyes, faint lines, a soft smile",
      "covered by a white headscarf", "thin",
      "a faded green traditional long-sleeved libaas dress, ankle length, and a white headscarf fully covering her hair and neck",
      "faded green libaas, tired kind eyes", "loving, hard-working, hopeful",
      "Khadheeja: a thin Maldivian woman of about 38 with warm brown skin, a thin gentle face, tired kind dark eyes and a "
      "soft smile; wears a faded green traditional long-sleeved ankle-length libaas dress and a white headscarf fully "
      "covering her hair and neck."),
    C("zubair", "Zubair", "ޒުބައިރު",
      "Khadheeja's brother, Shahula's uncle; a fisherman who turns cold and harsh after her death",
      "male", "about 45",
      "weathered square face, deep-set stern dark eyes, short greying beard",
      "short greying black hair", "stocky, strong arms",
      "a faded blue checked long-sleeved shirt with rolled cuffs and a dark-brown sarong (feyli)",
      "greying beard, sun-weathered skin, checked shirt", "stern, irritable, unsmiling",
      "Zubair: a stocky Maldivian fisherman of about 45 with sun-weathered dark brown skin, a weathered square face, "
      "deep-set stern dark eyes, short greying black hair and a short greying beard; wears a faded blue checked "
      "long-sleeved shirt with rolled cuffs and a dark-brown sarong."),
    C("faathanikey", "Faathanikey", "ފާތާނިކެ",
      "Zubair's wife, Shahula's kind aunt by marriage",
      "female", "about 42",
      "round kind face, soft worried dark eyes",
      "covered by a white headscarf", "plump, short",
      "a maroon dhigu-hedhun style long-sleeved ankle-length libaas dress and a white headscarf fully covering her hair and neck",
      "maroon libaas, round kind face", "warm, motherly, anxious",
      "Faathanikey: a plump short Maldivian woman of about 42 with warm brown skin, a round kind face and soft worried "
      "dark eyes; wears a maroon dhigu-hedhun style long-sleeved ankle-length libaas dress and a white headscarf fully "
      "covering her hair and neck."),
    C("moosafulhu", "Moosafulhu", "މޫސާފުޅު",
      "a kind old man of the island",
      "male", "about 70",
      "thin kind wrinkled face, gentle eyes, neat white beard",
      "covered by a white skullcap", "thin, slightly stooped",
      "a white long-sleeved kurta, a dark checked sarong and a white skullcap",
      "white beard, white skullcap", "gentle, grandfatherly",
      "Moosafulhu: a thin, slightly stooped Maldivian man of about 70 with warm brown skin, a kind wrinkled face, gentle "
      "eyes and a neat white beard; wears a white skullcap, a white long-sleeved kurta and a dark checked sarong."),
    C("azeeza", "Azeeza", "އަޒީޒާ",
      "a respected wealthy Malé lady who takes Shahula in and raises her; Aamir's mother",
      "female", "about 50",
      "dignified oval face, kind warm eyes behind thin gold-rimmed glasses, gentle smile",
      "covered by a cream hijab", "medium build, graceful",
      "an elegant emerald-green long-sleeved ankle-length abaya and a cream hijab fully covering her hair and neck, thin gold-rimmed glasses",
      "emerald abaya, gold-rimmed glasses", "kind, dignified, generous",
      "Azeeza: a graceful Maldivian lady of about 50 with warm brown skin, a dignified oval face, kind warm eyes behind "
      "thin gold-rimmed glasses and a gentle smile; wears an elegant emerald-green long-sleeved ankle-length abaya and a "
      "cream hijab fully covering her hair and neck."),
    C("aamir_teen", "Aamir (teen)", "އާމިރު",
      "Azeeza's son at 15", "male", "15",
      "handsome boyish face, bright dark eyes, clean-shaven", "neat short black hair", "slim, tall for his age",
      "a plain white t-shirt and long dark trousers", "neat hair, polite manner", "polite, curious",
      "teenage Aamir: a slim Maldivian boy of 15 with warm brown skin, a handsome boyish clean-shaven face, bright dark "
      "eyes and neat short black hair; wears a plain white t-shirt and long dark trousers."),
    C("aamir", "Aamir", "އާމިރު",
      "Azeeza's only son; a handsome charming playboy who marries Shahula and becomes cruel and unfaithful",
      "male", "about 25",
      "very handsome face with a strong jaw, dark confident eyes, light trimmed stubble, a charming smile that can turn hard",
      "thick black hair styled up and back", "tall, athletic",
      "a white long-sleeved shirt with the cuffs buttoned, dark trousers, a silver wristwatch",
      "styled hair, light stubble, silver watch", "charming, confident, possessive, quick-tempered",
      "Aamir: a tall athletic Maldivian man of about 25 with warm brown skin, a very handsome face with a strong jaw, dark "
      "confident eyes, light trimmed stubble and thick black hair styled up and back; wears a white long-sleeved shirt "
      "with buttoned cuffs, dark trousers and a silver wristwatch."),
    C("ayya", "Ayya (Ali)", "އައްޔަ",
      "Aamir's close friend", "male", "about 21",
      "round cheerful face, playful dark eyes, clean-shaven", "short curly black hair", "stocky",
      "a mustard-yellow t-shirt and blue jeans", "curly hair, round cheerful face", "joking, easygoing",
      "Ayya: a stocky Maldivian young man of about 21 with warm brown skin, a round cheerful clean-shaven face, playful "
      "dark eyes and short curly black hair; wears a mustard-yellow t-shirt and blue jeans."),
    C("raamee", "Raamee", "ރާމީ",
      "Shahula's schoolboy sweetheart who turns cold", "male", "about 17",
      "lean serious face, narrow dark eyes, clean-shaven", "short black hair with a side parting", "lean",
      "a white long-sleeved school shirt and dark-navy long trousers, no badge, no lettering",
      "side-parted hair, serious face", "cold, distant, guarded",
      "Raamee: a lean Maldivian schoolboy of about 17 with warm brown skin, a lean serious clean-shaven face, narrow dark "
      "eyes and short side-parted black hair; wears a white long-sleeved school shirt and dark-navy long trousers."),
    C("tholaal", "Tholaal", "ތޮލާލް",
      "Aamir's married office colleague", "male", "about 32",
      "narrow face, sly smile, thin moustache", "slicked-back black hair", "lean",
      "a navy long-sleeved shirt and grey trousers", "slicked hair, thin moustache", "loud, flashy",
      "Tholaal: a lean Maldivian man of about 32 with warm brown skin, a narrow face, a sly smile, a thin moustache and "
      "slicked-back black hair; wears a navy long-sleeved shirt and grey trousers."),
    C("naya", "Naya", "ނަޔާ",
      "office colleague seeing the married Tholaal", "female", "about 26",
      "bright made-up face, confident eyes", "covered by a black hijab", "slim",
      "a wine-red long-sleeved ankle-length abaya and a black hijab fully covering her hair and neck",
      "wine-red abaya", "carefree, laughing",
      "Naya: a slim Maldivian woman of about 26 with warm brown skin, a bright made-up face and confident eyes; wears a "
      "wine-red long-sleeved ankle-length abaya and a black hijab fully covering her hair and neck."),
    C("reysham", "Reysham", "ރޭޝަމް",
      "Aamir's young office colleague and secret mistress", "female", "about 22",
      "pretty youthful face, sharp knowing eyes with neat eyeliner, a mocking smile", "covered by a silver-grey hijab",
      "slim",
      "a lilac long-sleeved ankle-length abaya and a silver-grey hijab fully covering her hair and neck",
      "lilac abaya, mocking smile", "smug, provocative, cold",
      "Reysham: a slim Maldivian young woman of about 22 with light warm-brown skin, a pretty youthful face, sharp "
      "knowing eyes with neat eyeliner and a mocking smile; wears a lilac long-sleeved ankle-length abaya and a "
      "silver-grey hijab fully covering her hair and neck."),
    C("suneetha", "Suneetha", "ސުނީތާ",
      "the household helper", "female", "about 35",
      "plain kind face, quick attentive eyes", "covered by a simple brown headscarf", "thin",
      "a plain beige long-sleeved ankle-length dress and a simple brown headscarf fully covering her hair and neck",
      "beige dress, brown headscarf", "helpful, quiet",
      "Suneetha: a thin South Asian household helper of about 35 with medium-brown skin, a plain kind face and quick "
      "attentive eyes; wears a plain beige long-sleeved ankle-length dress and a simple brown headscarf fully covering "
      "her hair and neck.", look="South Asian, medium-brown skin"),
    C("fiyaza", "Fiyaza", "ފިޔާޒާ",
      "Shahula's close friend from her office", "female", "about 27",
      "warm round face, caring dark eyes", "covered by a grey hijab", "average",
      "a navy long-sleeved ankle-length abaya and a light-grey hijab fully covering her hair and neck",
      "navy abaya, caring eyes", "loyal, caring, tearful",
      "Fiyaza: a Maldivian woman of about 27 with warm brown skin, a warm round face and caring dark eyes; wears a navy "
      "long-sleeved ankle-length abaya and a light-grey hijab fully covering her hair and neck."),
]

FIRST = dict(shahula=308, shahula_child=308, khadheeja=308, zubair=308, faathanikey=308, moosafulhu=350, azeeza=350,
             aamir_teen=350, aamir=350, ayya=350, shahula_young=350, raamee=457, tholaal=458, naya=458, reysham=460,
             suneetha=460, fiyaza=463)

if __name__ == "__main__":
    series_dir, episode = sys.argv[1], int(sys.argv[2])
    for c in CARDS:
        d = os.path.join(series_dir, "characters", c["id"])
        p = os.path.join(d, "card.json")
        if os.path.exists(p):
            print("reuse", c["id"]); continue
        os.makedirs(d, exist_ok=True)
        card = dict(c)
        card["first_seen_episode"] = FIRST.get(c["id"], episode)
        card["reference_from_cover"] = bool(c.get("reference_from_cover"))
        json.dump(card, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("new", c["id"])

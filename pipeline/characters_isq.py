"""Series character cards for Isq (ޢިޝްގު, "Love"): a Maldivian island romance — Jaleel, a rich, cold, married Malé
businessman, falls for Maura, a shy young woman who has just moved back to her home island.
Creates card.json only for characters that don't exist yet. References are text-only (the series poster shows
non-Maldivian models with uncovered hair, so it is used for outfit cues only: Jaleel's black suit and gold watch,
Shaaliya's black dress, Maura's white lace dress and white flower).
Usage: python characters_isq.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="jaleel", name="Yoosuf Jaleel", name_dhivehi="ޖަލީލް",
         role="male lead; 28-year-old famous, very wealthy and powerful Malé businessman; married to Shaaliya by family arrangement; cold, stern and principled, falls for Maura",
         gender="male", age="28",
         ethnicity_look=MV + ", wheatish skin",
         face="handsome strong face with a sharp defined jaw, intense dark eyes under straight heavy eyebrows, a neatly trimmed short black beard, a stern unsmiling mouth",
         hair="thick black hair, slightly long, swept back and reaching his collar",
         build="tall, broad-shouldered, athletic",
         default_outfit="a tailored black suit over a crisp white long-sleeved shirt and a black tie, a white pocket square, a gold wristwatch, polished black shoes",
         distinguishing_features="swept-back collar-length black hair, trimmed beard, gold watch, often black sunglasses, hands in his pockets",
         personality_cues="cold, commanding, rarely smiles; softens only when he looks at Maura",
         visual_prompt="Jaleel: a tall broad-shouldered athletic Maldivian man of 28 with wheatish warm-brown skin, a handsome strong face with a sharp defined jaw, intense dark eyes under straight heavy eyebrows, a neatly trimmed short black beard and thick slightly long black hair swept back to his collar; wears a tailored black suit over a crisp white long-sleeved shirt with a black tie, a white pocket square and a gold wristwatch."),
    dict(id="maura", name="Maura", name_dhivehi="މައުރާ",
         role="female lead; about 22, has just finished business studies in Malé and moved back to her home island; shy, playful, innocent; falls for Jaleel",
         gender="female", age="about 22",
         ethnicity_look="Maldivian, South Asian features, fair light warm-brown skin",
         face="soft round innocent face, large bright dark eyes, gently arched eyebrows, small nose, a shy sweet smile",
         hair="fully covered by a white hijab",
         build="petite, short, slim",
         default_outfit="a loose long-sleeved ankle-length white dress with delicate lace sleeves and a softly flowing skirt, a plain white hijab wrapped snugly and fully covering her hair and neck, a small white frangipani flower pinned at the side of the hijab",
         distinguishing_features="petite and fair, white lace dress, white hijab with a small white frangipani",
         personality_cues="shy, blushes easily, looks down, sudden bright smiles",
         visual_prompt="Maura: a petite slim Maldivian young woman of about 22 with fair light warm-brown skin, a soft round innocent face, large bright dark eyes, gently arched eyebrows, a small nose and a shy sweet smile; wears a loose long-sleeved ankle-length white dress with delicate lace sleeves and a plain white hijab wrapped snugly and fully covering her hair and neck, with a small white frangipani flower pinned at the side of the hijab."),
    dict(id="shaaliya", name="Shaaliya", name_dhivehi="ޝާލިޔާ",
         role="Jaleel's wife in Malé, married by family arrangement; beautiful, kind and gentle, beginning to love him and hurt by his coldness",
         gender="female", age="about 26",
         ethnicity_look=MV,
         face="elegant oval face, large expressive dark eyes with long lashes, softly arched eyebrows, full lips, a gentle sad expression",
         hair="fully covered by a deep-maroon hijab",
         build="tall, slender, graceful",
         default_outfit="a loose long-sleeved ankle-length black velvet abaya-style dress with fine gold embroidery at the cuffs, a deep-maroon satin hijab wrapped snugly and fully covering her hair and neck, small gold stud earrings hidden under the hijab",
         distinguishing_features="black velvet dress with gold cuffs, deep-maroon hijab, elegant and wealthy",
         personality_cues="soft-spoken, devoted, quietly hurt",
         visual_prompt="Shaaliya: a tall slender graceful Maldivian woman of about 26 with warm brown skin, an elegant oval face, large expressive dark eyes with long lashes, softly arched eyebrows and full lips; wears a loose long-sleeved ankle-length black velvet abaya-style dress with fine gold embroidery at the cuffs and a deep-maroon satin hijab wrapped snugly and fully covering her hair and neck."),
    dict(id="fauziyya", name="Fauziyya", name_dhivehi="ފައުޒިއްޔާ",
         role="Jaleel's mother (Shaaliya calls her 'Mamma'); wealthy older lady of the Malé household",
         gender="female", age="about 58",
         ethnicity_look=MV,
         face="round dignified face with soft lines, calm dark eyes, small gold-rimmed reading glasses",
         hair="fully covered by a cream headscarf",
         build="medium, slightly plump",
         default_outfit="a traditional loose long-sleeved ankle-length dark-green libaas-style dress with a gold-embroidered neckline, a cream headscarf fully covering her hair and neck",
         distinguishing_features="dark-green libaas with gold neckline, cream headscarf, gold-rimmed glasses",
         personality_cues="composed, matriarchal, unaware of the couple's trouble",
         visual_prompt="Fauziyya: a dignified slightly plump Maldivian woman of about 58 with warm brown skin, a round face with soft lines, calm dark eyes and small gold-rimmed reading glasses; wears a traditional loose long-sleeved ankle-length dark-green libaas-style dress with a gold-embroidered neckline and a cream headscarf fully covering her hair and neck."),
    dict(id="reema", name="Reema", name_dhivehi="ރީމާ",
         role="Maura's elder sister ('Dhontha'), eight months pregnant, married to Assad; warm and teasing",
         gender="female", age="about 28",
         ethnicity_look=MV,
         face="friendly round face, laughing dark eyes, full cheeks",
         hair="fully covered by a dusty-pink hijab",
         build="average height, heavily pregnant with a modest rounded bump",
         default_outfit="a loose long-sleeved ankle-length sage-green maternity dress, a dusty-pink hijab fully covering her hair and neck, flat sandals",
         distinguishing_features="eight months pregnant, sage-green dress, dusty-pink hijab",
         personality_cues="cheerful, teasing, tired feet",
         visual_prompt="Reema: a Maldivian woman of about 28 with warm brown skin, a friendly round face with full cheeks and laughing dark eyes, eight months pregnant with a modest rounded bump; wears a loose long-sleeved ankle-length sage-green maternity dress and a dusty-pink hijab fully covering her hair and neck."),
    dict(id="assad", name="Assad", name_dhivehi="އައްސަދު",
         role="Reema's husband, Maura's brother-in-law; good-humoured, drives the family car",
         gender="male", age="about 31",
         ethnicity_look=MV,
         face="broad friendly face, easy grin, short black beard",
         hair="short black hair",
         build="stocky, average height",
         default_outfit="a navy-blue polo shirt and khaki long trousers, a black digital watch",
         distinguishing_features="navy polo shirt, short beard, easy grin",
         personality_cues="cheerful, laughs a lot",
         visual_prompt="Assad: a stocky Maldivian man of about 31 with warm brown skin, a broad friendly face with an easy grin, short black hair and a short black beard; wears a navy-blue polo shirt and khaki long trousers."),
    dict(id="zulfa", name="Zulfa", name_dhivehi="ޒުލްފާ",
         role="Maura and Reema's mother; famous on the island for her cooking; warm, practical, always pushing food on her daughters",
         gender="female", age="about 52",
         ethnicity_look=MV,
         face="kind round face with laugh lines, warm dark eyes",
         hair="fully covered by a maroon headscarf",
         build="medium, plump",
         default_outfit="a loose long-sleeved ankle-length floral housecoat-style dress in soft blue with a small pocket, a maroon headscarf fully covering her hair and neck",
         distinguishing_features="soft-blue floral housecoat dress, maroon headscarf",
         personality_cues="bustling, warm, laughing",
         visual_prompt="Zulfa: a plump Maldivian woman of about 52 with warm brown skin, a kind round face with laugh lines and warm dark eyes; wears a loose long-sleeved ankle-length soft-blue floral housecoat-style dress and a maroon headscarf fully covering her hair and neck."),
    dict(id="salaam", name="Salaam", name_dhivehi="ސަލާމް",
         role="Maura and Reema's father; quiet, gentle, smiling; redecorated Maura's room for her return",
         gender="male", age="about 58",
         ethnicity_look=MV,
         face="lean kind face, gentle smile, short grey beard",
         hair="short grey hair under a white knitted skullcap",
         build="slim, average height",
         default_outfit="a light-grey long-sleeved kurta-style shirt over a dark checked sarong (feyli) to the ankles, a white knitted skullcap",
         distinguishing_features="white skullcap, grey beard, light-grey kurta, checked sarong",
         personality_cues="calm, affectionate, few words",
         visual_prompt="Salaam: a slim Maldivian man of about 58 with warm brown skin, a lean kind face, a gentle smile and a short grey beard; wears a white knitted skullcap, a light-grey long-sleeved kurta-style shirt and a dark checked ankle-length sarong."),
    dict(id="nafeesa", name="Nafeesa", name_dhivehi="ނަފީސާ",
         role="older neighbour two doors down ('Nafeesaththa'); lively, funny, hosts the delegation's dinners and the Eid lunch",
         gender="female", age="about 62",
         ethnicity_look=MV,
         face="thin lively face with deep laugh lines, twinkling eyes, a wide toothy smile",
         hair="fully covered by a white headscarf",
         build="small, wiry",
         default_outfit="a traditional loose long-sleeved ankle-length lavender libaas-style dress with a simple embroidered neckline, a white headscarf fully covering her hair and neck",
         distinguishing_features="lavender libaas, white headscarf, wide grin",
         personality_cues="chatty, self-mocking, flustered when busy",
         visual_prompt="Nafeesa: a small wiry Maldivian woman of about 62 with warm brown skin, a thin lively face with deep laugh lines, twinkling eyes and a wide smile; wears a traditional loose long-sleeved ankle-length lavender libaas-style dress and a white headscarf fully covering her hair and neck."),
    dict(id="lamha", name="Lamha", name_dhivehi="ލަމްހާ",
         role="cheerful island girl about Maura's age from Nafeesa's household; becomes Maura's first friend; teasing and energetic",
         gender="female", age="about 21",
         ethnicity_look=MV,
         face="heart-shaped face, mischievous bright eyes, dimpled grin",
         hair="fully covered by a bright coral-pink hijab",
         build="slim, lively",
         default_outfit="a loose long-sleeved ankle-length mint-green dress, a bright coral-pink hijab fully covering her hair and neck",
         distinguishing_features="mint-green dress, coral-pink hijab, dimples",
         personality_cues="talkative, mischievous, energetic",
         visual_prompt="Lamha: a slim lively Maldivian young woman of about 21 with warm brown skin, a heart-shaped face, mischievous bright eyes and a dimpled grin; wears a loose long-sleeved ankle-length mint-green dress and a bright coral-pink hijab fully covering her hair and neck."),
]

FIRST = dict(jaleel=341, maura=341, shaaliya=341, reema=341, assad=341, zulfa=341, salaam=341, nafeesa=341,
             lamha=366, fauziyya=428)

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

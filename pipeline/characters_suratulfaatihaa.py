"""Series character cards for Suratul Faatihaa (ސޫރަތުލް ފާތިޙާ — a reflective, non-fiction book on the meanings of
Surah Al-Fatiha, read aloud). There is no plot: these are the recurring anonymous "everyday" figures the narration
uses as examples ("you, the listener", a mother and her small son, a powerful man...). Sacred figures are never cards.
Creates card.json only for characters that don't exist yet.
Usage: python characters_suratulfaatihaa.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="listener", name="The listener", name_dhivehi="ތިބާ",
         role="'you' — the ordinary Maldivian believer the narration addresses; prays daily, faces loss, illness, sin and repentance, rediscovers the meaning of Al-Fatiha",
         gender="male", age="early 30s",
         ethnicity_look=MV,
         face="gentle thoughtful face, warm dark eyes, defined eyebrows, a short neatly trimmed black beard",
         hair="short neat black hair",
         build="slim, average height",
         default_outfit="a loose off-white long-sleeved collarless kurta shirt reaching mid-thigh and plain dark-grey trousers; a white crocheted prayer cap when he prays",
         distinguishing_features="short trimmed black beard, off-white kurta",
         personality_cues="reflective, sincere, sometimes weary or troubled, quietly hopeful",
         visual_prompt="the listener: a slim Maldivian man in his early 30s with warm brown skin, a gentle thoughtful face, warm dark eyes, short neat black hair and a short neatly trimmed black beard; wears a loose off-white long-sleeved collarless kurta shirt reaching mid-thigh and plain dark-grey trousers."),
    dict(id="mother", name="The mother", name_dhivehi="މަންމަ",
         role="a young Maldivian mother — the narration's recurring image of tenderness and care (sick child at night, first words, hugs then advice)",
         gender="female", age="late 20s",
         ethnicity_look=MV,
         face="soft round face, kind large dark eyes, gentle smile, faint tiredness",
         hair="fully covered by a cream hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length sage-green dress and a cream hijab wrapped snugly and fully covering her hair and neck",
         distinguishing_features="sage-green dress, cream hijab",
         personality_cues="tender, patient, protective",
         visual_prompt="the mother: a slim Maldivian woman in her late 20s with warm brown skin, a soft round face, kind large dark eyes and a gentle smile; wears a loose long-sleeved ankle-length sage-green dress and a cream hijab wrapped snugly and fully covering her hair and neck."),
    dict(id="son", name="The little son", name_dhivehi="ދަރިފުޅު",
         role="the mother's small son, about 5",
         gender="male", age="about 5",
         ethnicity_look=MV,
         face="round chubby face, big bright dark eyes",
         hair="short black hair",
         build="small child",
         default_outfit="a plain light-blue short-sleeved t-shirt and long navy shorts below the knee",
         distinguishing_features="light-blue t-shirt",
         personality_cues="curious, trusting",
         ref_pose="left: head-and-shoulders portrait; right: full-body standing view of the small child",
         visual_prompt="the little son: a small Maldivian boy of about 5 with warm brown skin, a round chubby face, big bright dark eyes and short black hair; wears a plain light-blue short-sleeved t-shirt and long navy shorts below the knee."),
    dict(id="powerful_man", name="The powerful man", name_dhivehi="ބާރުގަދަ މީހާ",
         role="the narration's image of the rich, powerful and arrogant who think they own the world and will one day stand alone",
         gender="male", age="about 55",
         ethnicity_look="South Asian features, light-brown skin",
         face="heavy square jaw, sharp proud dark eyes, a neatly groomed grey-streaked short beard",
         hair="slicked-back black hair greying at the temples",
         build="tall, heavy-set",
         default_outfit="an expensive tailored charcoal-black suit, white shirt and a dark tie, a heavy gold wristwatch with a blank face",
         distinguishing_features="charcoal suit, grey temples, gold watch",
         personality_cues="proud, commanding; later small and alone",
         visual_prompt="the powerful man: a tall heavy-set South Asian man of about 55 with light-brown skin, a heavy square jaw, sharp proud dark eyes, slicked-back black hair greying at the temples and a neatly groomed grey-streaked short beard; wears an expensive tailored charcoal-black suit, a white shirt and a dark tie."),
    dict(id="elder", name="The old fisherman", name_dhivehi="މުސްކުޅި މަސްވެރިޔާ",
         role="a humble, poor, devout old Maldivian fisherman — the narration's image of simple sincere faith, patience and the guided poor",
         gender="male", age="about 70",
         ethnicity_look=MV,
         face="deeply lined weathered face, kind calm eyes, a short white beard, sun-darkened skin",
         hair="short white hair under a white crocheted cap",
         build="thin, slightly stooped",
         default_outfit="a faded long-sleeved pale-blue cotton shirt and a checked blue-and-white sarong (feyli) to the ankles, a white crocheted cap",
         distinguishing_features="white beard, white cap, checked sarong",
         personality_cues="serene, grateful, unhurried",
         visual_prompt="the old fisherman: a thin slightly stooped Maldivian man of about 70 with sun-darkened warm brown skin, a deeply lined weathered face, kind calm eyes and a short white beard; wears a white crocheted cap, a faded long-sleeved pale-blue cotton shirt and a checked blue-and-white sarong to the ankles."),
]

FIRST = dict(listener=422, mother=422, son=423, powerful_man=423, elder=422)

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

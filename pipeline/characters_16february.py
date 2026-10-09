"""Series character cards for 16 February (16 ފެބްރުއަރީ; island mystery thriller: on the rainy night of 16 February
resort office worker Malak witnesses a man fall to his death at an abandoned building site, is pulled into hiding by a
stranger — undercover officer Ahlam, the resort owner's grandson — and is left hurt, betrayed by her boyfriend Zain
and questioned by her stepbrother Kaif, a police officer).
Creates card.json only for characters that don't exist yet.
Usage: python characters_16february.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="malak", name="Malak", name_dhivehi="މަލަކް",
         role="protagonist; resort office worker (about 24) who witnessed a death on the night of 16 February",
         gender="female", age="about 24",
         ethnicity_look=MV,
         face="striking oval face, large dark almond eyes, defined dark eyebrows, straight nose, full lips, a guarded serious expression",
         hair="fully covered by a black hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length deep wine-maroon kurta tunic over loose black trousers and a plain black hijab wrapped snugly and fully covering her hair and neck; a slim silver wristwatch",
         distinguishing_features="wine-maroon kurta, black hijab, slim silver wristwatch",
         personality_cues="proud, sharp-tongued, haunted, hides fear behind coldness",
         visual_prompt="Malak: a slim Maldivian woman of about 24 with warm brown skin, a striking oval face, large dark almond eyes, defined dark eyebrows and full lips, a guarded serious expression; wears a loose long-sleeved ankle-length deep wine-maroon kurta tunic over loose black trousers and a plain black hijab wrapped snugly and fully covering her hair and neck, a slim silver wristwatch."),
    dict(id="ahlam", name="Ahlam", name_dhivehi="އަހްލަމް",
         role="the resort owner's grandson (about 32), new boss of the resort company; secretly an undercover defence-force officer; the stranger of 16 February",
         gender="male", age="about 32",
         ethnicity_look=MV,
         face="strong handsome face, intense deep-set dark eyes under heavy brows, a straight prominent nose, a full neatly kept black beard",
         hair="thick wavy black hair, slightly tousled",
         build="tall, broad-shouldered, athletic",
         default_outfit="a fitted black long-sleeved button shirt with the sleeves neatly rolled to the forearms, charcoal trousers, a dark leather-strap wristwatch",
         distinguishing_features="full black beard, thick wavy hair, intense frown, black shirt",
         personality_cues="witty, sharp, principled, watchful",
         reference_from_cover=True, cover_crop=[0.44, 0.05, 0.92, 0.45],
         visual_prompt="Ahlam: a tall broad-shouldered Maldivian man of about 32 with warm brown skin, a strong handsome face, intense deep-set dark eyes under heavy brows, a straight prominent nose, thick wavy black hair and a full neatly kept black beard; wears a fitted black long-sleeved button shirt with the sleeves rolled to the forearms, charcoal trousers and a dark leather-strap wristwatch."),
    dict(id="kaif", name="Kaif", name_dhivehi="ކައިފް",
         role="police officer (about 28), Aanis's son and Malak's stepbrother; investigating the 16 February death; in love with Malak, who rejected him",
         gender="male", age="about 28",
         ethnicity_look=MV,
         face="lean serious face, dark watchful eyes, straight nose, a short thin moustache and light stubble",
         hair="short black hair, slightly messy on top",
         build="tall, lean",
         default_outfit="a dark-navy long-sleeved Maldivian police uniform shirt with plain epaulettes, dark-navy trousers, black belt and boots, a dark-navy peaked cap, no readable badges or text",
         distinguishing_features="police uniform and cap, thin moustache",
         personality_cues="dutiful, quietly hurt, persistent",
         reference_from_cover=True, cover_crop=[0.52, 0.40, 0.86, 0.64],
         visual_prompt="Kaif: a tall lean Maldivian police officer of about 28 with warm brown skin, a lean serious face, dark watchful eyes, short black hair, a short thin moustache and light stubble; wears a dark-navy long-sleeved police uniform shirt with plain epaulettes, dark-navy trousers, a black belt and a dark-navy peaked cap, no readable badges or text."),
    dict(id="vimla", name="Vimla", name_dhivehi="ވިމްލާ",
         role="Malak's mother (about 50), Aanis's wife and Kaif's stepmother; talkative, fussy, protective",
         gender="female", age="about 50",
         ethnicity_look=MV,
         face="round expressive face, lively dark eyes, a few smile lines",
         hair="fully covered by a printed headscarf",
         build="short, plump",
         default_outfit="a loose long-sleeved ankle-length traditional mustard-yellow libaas dress with a small print, and a soft brown floral headscarf fully covering her hair and neck",
         distinguishing_features="mustard libaas, brown floral headscarf, often holding a broom or a tea tray",
         personality_cues="chatty, scolding, warm underneath",
         visual_prompt="Vimla: a short plump Maldivian woman of about 50 with warm brown skin, a round expressive face and lively dark eyes; wears a loose long-sleeved ankle-length mustard-yellow libaas dress with a small print and a soft brown floral headscarf fully covering her hair and neck."),
    dict(id="aanis", name="Aanis", name_dhivehi="އާނިސް",
         role="Malak's stepfather (about 58), Kaif's father; calm, reads the news on his phone on the joali",
         gender="male", age="about 58",
         ethnicity_look=MV,
         face="lined kind face, observant eyes, a short grey-and-white beard",
         hair="short grey hair under a white crocheted skullcap",
         build="medium height, thin",
         default_outfit="a pale cream short-collared cotton shirt with long sleeves and a checked dark-blue feyli sarong, a white crocheted skullcap",
         distinguishing_features="white skullcap, grey beard, checked sarong",
         personality_cues="patient, quietly perceptive",
         visual_prompt="Aanis: a thin Maldivian man of about 58 with warm brown skin, a lined kind face, observant eyes and a short grey-and-white beard; wears a white crocheted skullcap, a pale cream long-sleeved cotton shirt and a checked dark-blue feyli sarong."),
    dict(id="zain", name="Zain", name_dhivehi="ޒައިން",
         role="Malak's boyfriend (about 26) who betrayed her with her best friend Kiyaara on his birthday, 16 February",
         gender="male", age="about 26",
         ethnicity_look=MV,
         face="smooth handsome boyish face, clean-shaven, confident smile, bright dark eyes",
         hair="short black hair styled up at the front",
         build="medium height, slim",
         default_outfit="a light-grey polo shirt, dark-blue jeans and white sneakers",
         distinguishing_features="clean-shaven, styled hair, light-grey polo",
         personality_cues="smooth, charming, self-assured, evasive",
         visual_prompt="Zain: a slim Maldivian man of about 26 with warm brown skin, a smooth handsome clean-shaven boyish face, bright dark eyes, a confident smile and short black hair styled up at the front; wears a light-grey polo shirt, dark-blue jeans and white sneakers."),
    dict(id="mizoo", name="Mizoo", name_dhivehi="މިޒޫ",
         role="Malak's friend and colleague at the resort front office (about 24); cheerful gossip",
         gender="female", age="about 24",
         ethnicity_look=MV,
         face="round cheerful face, bright eyes, dimpled smile",
         hair="fully covered by a teal hijab",
         build="petite",
         default_outfit="a resort staff uniform: a loose long-sleeved ankle-length sand-beige tunic dress with a teal sash and a teal hijab fully covering her hair and neck",
         distinguishing_features="teal hijab, sand-beige uniform",
         personality_cues="bubbly, curious, caring",
         visual_prompt="Mizoo: a petite Maldivian woman of about 24 with warm brown skin, a round cheerful face, bright eyes and a dimpled smile; wears a resort staff uniform — a loose long-sleeved ankle-length sand-beige tunic dress with a teal sash — and a teal hijab fully covering her hair and neck."),
    dict(id="ali", name="Ali", name_dhivehi="ޢަލީ",
         role="the resort office secretary / office manager (about 40), loyal, flustered, a teasing matchmaker",
         gender="male", age="about 40",
         ethnicity_look=MV,
         face="round friendly face, rectangular thin-framed glasses, a neat short moustache",
         hair="short black hair with a side parting, receding a little",
         build="medium height, a little chubby",
         default_outfit="a white long-sleeved shirt with a navy tie, dark-grey trousers, often holding a tablet in a dark case",
         distinguishing_features="thin-framed glasses, navy tie, tablet in hand",
         personality_cues="eager, nervous, mischievous smile",
         visual_prompt="Ali: a slightly chubby Maldivian man of about 40 with warm brown skin, a round friendly face, rectangular thin-framed glasses, a neat short moustache and short side-parted black hair; wears a white long-sleeved shirt with a navy tie and dark-grey trousers, holding a tablet in a dark case."),
    dict(id="ubey", name="Ubey", name_dhivehi="އުބޭ",
         role="attendant of the resort souvenir shop (about 30) who sold Malak the watch",
         gender="male", age="about 30",
         ethnicity_look=MV,
         face="thin friendly face, a short trimmed beard, lively eyes",
         hair="short black hair",
         build="slim",
         default_outfit="a resort staff uniform: a short-sleeved teal shirt with a sand-beige collar over a plain white long-sleeved undershirt, beige trousers",
         distinguishing_features="teal staff shirt, short beard",
         personality_cues="talkative, joking, later frightened",
         visual_prompt="Ubey: a slim Maldivian man of about 30 with warm brown skin, a thin friendly face, lively eyes, short black hair and a short trimmed beard; wears a resort staff uniform — a teal shirt with a sand-beige collar over a plain white long-sleeved undershirt — and beige trousers."),
    dict(id="zuhoo", name="Zuhoo", name_dhivehi="ޒުހޫ",
         role="the resort's medic / nurse (about 35)",
         gender="female", age="about 35",
         ethnicity_look=MV,
         face="calm capable face, gentle dark eyes",
         hair="fully covered by a white hijab",
         build="medium height",
         default_outfit="light-blue long-sleeved medical scrubs with a white coat over them and a white hijab fully covering her hair and neck, a stethoscope around her neck",
         distinguishing_features="white hijab, light-blue scrubs, stethoscope",
         personality_cues="brisk, kind, competent",
         visual_prompt="Zuhoo: a Maldivian woman of about 35 with warm brown skin, a calm capable face and gentle dark eyes; wears light-blue long-sleeved medical scrubs under a white coat, a white hijab fully covering her hair and neck and a stethoscope around her neck."),
]

FIRST = dict(malak=246, ahlam=246, vimla=246, aanis=246, zain=246, kaif=250, mizoo=250, ubey=250,
             ali=284, zuhoo=284)

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

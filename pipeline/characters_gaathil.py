"""Series character cards for Gaathil (an island mystery-thriller: photographer Ali Shahid photographs Ibrahim Naseem,
presumed dead for 20 years after a murder, by the old lighthouse; police chief Amjad secretly protects him; Ibrahim
lived in another atoll as the fisherman 'Adam' behind a silicone mask and married Mariyam).
Creates card.json only for characters that don't exist yet. Only the masked stranger is taken from the cover (crop);
everyone else is generated from text.
Usage: python characters_gaathil.py <series_dir> <first_episode>
"""
import json, os, sys

MV = "Maldivian, South Asian features, warm brown skin"
CARDS = [
    dict(id="shahid", name="Ali Shahid", name_dhivehi="ޢަލީ ޝާހިދު",
         role="protagonist; well-known island photographer (about 30) who loves mysterious scenes; photographs the missing Ibrahim Naseem and starts digging on his own",
         gender="male", age="about 30",
         ethnicity_look=MV,
         face="lean intelligent face, alert dark-brown eyes, straight eyebrows, light black stubble",
         hair="short slightly wavy black hair",
         build="slim, average height",
         default_outfit="a dark olive-green long-sleeved utility shirt worn open over a plain grey t-shirt, black trousers, dark sneakers, a professional black camera on a strap",
         distinguishing_features="olive-green utility shirt, light stubble, camera on a strap",
         personality_cues="curious, observant, brave but increasingly anxious and suspicious",
         visual_prompt="Ali Shahid: a slim Maldivian man of about 30 with warm brown skin, a lean intelligent face, alert dark-brown eyes, straight eyebrows, light black stubble and short slightly wavy black hair; wears a dark olive-green long-sleeved utility shirt open over a plain grey t-shirt, black trousers and dark sneakers."),
    dict(id="shahid_mother", name="Shahid's mother", name_dhivehi="ޝާހިދުގެ މަންމަ",
         role="Shahid's elderly mother (about 62), gentle and worried",
         gender="female", age="about 62",
         ethnicity_look=MV,
         face="soft lined round face, kind tired dark eyes",
         hair="fully covered by a beige headscarf",
         build="short, slightly stooped",
         default_outfit="a loose long-sleeved ankle-length maroon dress (traditional libaas style) and a beige headscarf fully covering her hair and neck",
         distinguishing_features="maroon libaas, beige headscarf",
         personality_cues="worried, soft-spoken, motherly",
         visual_prompt="Shahid's mother: a short, slightly stooped elderly Maldivian woman of about 62 with warm brown skin, a soft lined round face and kind tired dark eyes; wears a loose long-sleeved ankle-length maroon dress in traditional libaas style and a beige headscarf fully covering her hair and neck."),
    dict(id="amjad", name="Officer Amjad", name_dhivehi="އަމްޖަދު",
         role="the island's police chief (about 55), deeply respected; secretly protects Ibrahim Naseem",
         gender="male", age="about 55",
         ethnicity_look=MV,
         face="square stern face, sharp narrow vigilant dark eyes, heavy brows, thick salt-and-pepper moustache, clean-shaven chin, deep lines on the forehead",
         hair="short salt-and-pepper hair combed back",
         build="tall, broad-shouldered, upright posture",
         default_outfit="a dark navy-blue police uniform shirt with long sleeves and plain shoulder epaulettes (no badges, no lettering), dark navy trousers, black belt with no holster, black shoes",
         distinguishing_features="navy police uniform, salt-and-pepper moustache, piercing eyes",
         personality_cues="calm, authoritative, controlled; hidden fear shows only in small gestures",
         visual_prompt="Officer Amjad: a tall broad-shouldered Maldivian man of about 55 with warm brown skin, a square stern face, sharp narrow vigilant dark eyes, heavy brows, a thick salt-and-pepper moustache, a clean-shaven chin and short salt-and-pepper hair combed back; wears a long-sleeved dark navy-blue police uniform shirt with plain shoulder epaulettes and no badges or lettering, dark navy trousers and a plain black belt; no weapon."),
    dict(id="amjad_young", name="Officer Amjad (20 years ago)", name_dhivehi="އަމްޖަދު",
         role="Amjad twenty years ago (about 35), a rising police officer who blamed Ibrahim and secretly helped him flee",
         gender="male", age="about 35",
         ethnicity_look=MV,
         face="square face, sharp narrow dark eyes, heavy brows, thick black moustache, clean-shaven chin",
         hair="short black hair combed back",
         build="tall, broad-shouldered",
         default_outfit="a dark navy-blue police uniform shirt with long sleeves and plain shoulder epaulettes (no badges, no lettering), dark navy trousers, black belt with no holster",
         distinguishing_features="navy police uniform, black moustache",
         personality_cues="hard, scheming, persuasive",
         visual_prompt="young Officer Amjad: a tall broad-shouldered Maldivian man of about 35 with warm brown skin, a square face, sharp narrow dark eyes, heavy brows, a thick black moustache, a clean-shaven chin and short black hair combed back; wears a long-sleeved dark navy-blue police uniform shirt with plain shoulder epaulettes and no badges or lettering and dark navy trousers; no weapon."),
    dict(id="ibrahim", name="Ibrahim Naseem", name_dhivehi="އިބްރާހީމް ނަސީމް",
         role="the man who vanished 20 years ago after a murder and was believed dead (about 55 now); his real ageing face",
         gender="male", age="about 55",
         ethnicity_look=MV,
         face="gaunt weathered face with hollow cheeks and deep lines, deep-set haunted dark eyes full of pain and fear, grey stubble beard",
         hair="untidy grey-black hair",
         build="lean, wiry, medium height",
         default_outfit="an old-fashioned heavy dark-brown thick wool long coat buttoned up, a dark shirt underneath, dark trousers",
         distinguishing_features="heavy old dark-brown wool coat, haunted deep-set eyes, grey stubble",
         personality_cues="hunted, sorrowful, watchful",
         visual_prompt="Ibrahim Naseem: a lean wiry Maldivian man of about 55 with warm brown skin, a gaunt weathered face with hollow cheeks and deep lines, deep-set haunted dark eyes full of pain and fear, a grey stubble beard and untidy grey-black hair; wears an old-fashioned heavy dark-brown thick wool long coat buttoned up over a dark shirt and dark trousers."),
    dict(id="ibrahim_young", name="Ibrahim Naseem (20 years ago)", name_dhivehi="އިބްރާހީމް ނަސީމް",
         role="Ibrahim twenty years ago (about 35), blamed for the murder, fleeing the island",
         gender="male", age="about 35",
         ethnicity_look=MV,
         face="lean face, deep-set dark eyes, black moustache, clean-shaven chin",
         hair="short black hair",
         build="lean, wiry, medium height",
         default_outfit="a faded blue long-sleeved button shirt and grey trousers",
         distinguishing_features="faded blue shirt, black moustache",
         personality_cues="desperate, frightened",
         visual_prompt="young Ibrahim Naseem: a lean wiry Maldivian man of about 35 with warm brown skin, a lean face, deep-set dark eyes, a black moustache, a clean-shaven chin and short black hair; wears a faded blue long-sleeved button shirt and grey trousers."),
    dict(id="adam", name="Adam", name_dhivehi="އާދަމް",
         role="Ibrahim Naseem living under a silicone mask as 'Adam', a quiet hard-working fisherman on a remote island in another atoll; Mariyam's husband",
         gender="male", age="looks about 38",
         ethnicity_look=MV,
         face="calm, smooth, handsome oval face, gentle dark eyes, neatly trimmed short black beard and moustache",
         hair="short neat black hair",
         build="lean, wiry, medium height",
         default_outfit="a faded sky-blue long-sleeved cotton shirt with sleeves rolled to the forearm, dark-grey trousers",
         distinguishing_features="faded sky-blue shirt, neat short beard, unusually smooth calm face",
         personality_cues="quiet, kind, secretive, burdened",
         visual_prompt="Adam: a lean wiry Maldivian man who looks about 38, with warm brown skin, a calm smooth handsome oval face, gentle dark eyes, a neatly trimmed short black beard and moustache and short neat black hair; wears a faded sky-blue long-sleeved cotton shirt with the sleeves rolled to the forearm and dark-grey trousers."),
    dict(id="mariyam", name="Mariyam", name_dhivehi="މަރިޔަމް",
         role="innocent, kind young woman (about 24) of a remote island; marries 'Adam' and follows him trustingly",
         gender="female", age="about 24",
         ethnicity_look=MV,
         face="gentle oval face, large innocent dark eyes, soft eyebrows, small nose",
         hair="fully covered by a cream hijab",
         build="slim, average height",
         default_outfit="a loose long-sleeved ankle-length dusty-rose dress and a cream hijab fully covering her hair and neck",
         distinguishing_features="dusty-rose dress, cream hijab, innocent wide eyes",
         personality_cues="trusting, loving, quiet; later frightened",
         visual_prompt="Mariyam: a slim young Maldivian woman of about 24 with warm brown skin, a gentle oval face, large innocent dark eyes, soft eyebrows and a small nose; wears a loose long-sleeved ankle-length dusty-rose dress and a cream hijab fully covering her hair and neck."),
    dict(id="masked_stranger", name="the masked stranger", name_dhivehi="",
         role="the mysterious figure from the cover, wrapped in black with only his eyes visible; warns Shahid at the warehouses and runs",
         gender="male", age="unknown",
         ethnicity_look=MV,
         face="only wary dark eyes visible, the skin around them smeared with grime",
         hair="hidden under a black turban-style head wrap",
         build="medium height, lean",
         default_outfit="a long loose black robe, a black turban-style head wrap and a black cloth covering nose, mouth and chin",
         distinguishing_features="all in black, face cloth, grime-smeared eyes",
         personality_cues="wary, glancing back over his shoulder",
         visual_prompt="the masked stranger: a lean man wrapped in a long loose black robe, a black turban-style head wrap and a black cloth covering his nose, mouth and chin, so only his wary dark eyes are visible, the skin around them smeared with grime.",
         reference_from_cover=True, cover_crop=[0.22, 0.29, 0.72, 0.86],
         ref_pose="left: head-and-shoulders portrait glancing over his shoulder; right: full-body standing view"),
]

FIRST = dict(shahid=606, shahid_mother=606, amjad=606, amjad_young=608, ibrahim=606, ibrahim_young=608, adam=608,
             mariyam=608, masked_stranger=607)

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

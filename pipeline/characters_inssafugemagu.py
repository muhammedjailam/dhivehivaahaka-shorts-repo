"""Series character cards for Inssafuge Magu ("The Path of Justice"; a New York / Boston crime thriller: FBI analyst
Alex Brand finds an ancient Roman coin in the hand of murdered billionaire Victor Vance; a killer is hunting the seven
members of a 1998 Harvard secret society, 'The Seventh Senate'; Alex's father is judge Richard Brand).
The story is set in the USA, so the characters look American (not Maldivian); the modesty rules still apply
(every woman in a hijab and long loose clothing). The cover has no people: all references are generated from text.
Creates card.json only for characters that don't exist yet.
Usage: python characters_inssafugemagu.py <series_dir> <first_episode>
"""
import json, os, sys

CARDS = [
    dict(id="alex", name="Alex Brand", name_dhivehi="އެލެކްސް ބްރޭންޑް",
         role="protagonist; FBI special criminal analyst (about 33), the bureau's best pattern analyst; quiet, deep gaze, notices the smallest details; son of judge Richard Brand",
         gender="male", age="about 33",
         ethnicity_look="American man of European descent, light olive skin",
         face="lean angular face, calm deep-set dark-grey eyes, straight dark brows, strong jaw, clean-shaven with a faint shadow",
         hair="short dark-brown hair neatly combed back",
         build="tall, lean, upright",
         default_outfit="a long black wool overcoat over a charcoal-grey suit, a white shirt and a slim dark tie slightly loosened, black leather shoes",
         distinguishing_features="long black overcoat, loosened dark tie, calm piercing grey eyes",
         personality_cues="silent, focused, observant; controlled emotion that cracks only for his father",
         visual_prompt="Alex Brand: a tall lean American man of about 33 with light olive skin, a lean angular face, calm deep-set dark-grey eyes, straight dark brows, a strong clean-shaven jaw and short dark-brown hair neatly combed back; wears a long black wool overcoat over a charcoal-grey suit, a white shirt and a slim dark tie slightly loosened."),
    dict(id="rogers", name="Detective Rogers", name_dhivehi="ރޮޖަރސް",
         role="experienced, weary NYPD detective (about 55) who wants the Vance case closed as a suicide",
         gender="male", age="about 55",
         ethnicity_look="American man, ruddy fair skin",
         face="broad fleshy face, tired heavy-lidded blue eyes, thick grey moustache, deep frown lines",
         hair="short grey crew cut, receding",
         build="stocky, heavy-set, medium height",
         default_outfit="a worn brown leather jacket over a rumpled light-blue button shirt, loose dark-brown tie, grey trousers; no badge lettering, no weapon visible",
         distinguishing_features="brown leather jacket, grey moustache, weary look",
         personality_cues="impatient, cynical, but startled by Alex's discoveries",
         visual_prompt="Detective Rogers: a stocky heavy-set American man of about 55 with ruddy fair skin, a broad fleshy face, tired heavy-lidded blue eyes, a thick grey moustache and a short receding grey crew cut; wears a worn brown leather jacket over a rumpled light-blue button shirt, a loose dark-brown tie and grey trousers; no weapon."),
    dict(id="richard", name="Judge Richard Brand", name_dhivehi="ރިޗަޑް ބްރޭންޑް",
         role="Alex's father (about 65), one of the most respected judges of the New York State Supreme Court; Alex's hero; secretly afraid of the 1998 past",
         gender="male", age="about 65",
         ethnicity_look="American man of European descent, fair skin",
         face="distinguished long face, deep lines, grey eyes under heavy silver brows, clean-shaven",
         hair="thick silver-white hair neatly combed",
         build="tall, slim, dignified",
         default_outfit="at home at night: a dark charcoal waistcoat over a white shirt with the sleeves down and a loosened burgundy tie, dark trousers",
         distinguishing_features="silver-white hair, charcoal waistcoat, burgundy tie",
         personality_cues="dignified, measured; tonight frightened, breathing fast",
         visual_prompt="Judge Richard Brand: a tall slim dignified American man of about 65 with fair skin, a distinguished long lined face, grey eyes under heavy silver brows, clean-shaven, and thick silver-white hair neatly combed; wears a dark charcoal waistcoat over a long-sleeved white shirt with a loosened burgundy tie and dark trousers."),
    dict(id="sarah", name="Detective Sarah Allison", name_dhivehi="ސާރާ އެލިސަން",
         role="Boston Police homicide detective (about 35), tough, street-wise, with a Boston accent; grew up as Emily Ward's neighbour",
         gender="female", age="about 35",
         ethnicity_look="American woman, fair skin",
         face="strong oval face with high cheekbones, sharp intense dark-brown eyes, defined dark brows",
         hair="fully covered by a black hijab",
         build="tall, athletic",
         default_outfit="a long loose ash-grey wool overcoat reaching her ankles, buttoned, over a loose dark long-sleeved top and loose black trousers, a black hijab fully covering her hair and neck, black boots",
         distinguishing_features="tall, ash-grey long overcoat, black hijab, sharp eyes",
         personality_cues="strong, blunt, fearless; hands in her coat pockets; grief and anger about Emily",
         visual_prompt="Detective Sarah Allison: a tall athletic American woman of about 35 with fair skin, a strong oval face with high cheekbones, sharp intense dark-brown eyes and defined dark brows; wears a long loose ash-grey wool overcoat reaching her ankles, buttoned, over a loose dark long-sleeved top and loose black trousers, and a black hijab fully covering her hair and neck."),
    dict(id="masked_killer", name="the masked killer", name_dhivehi="ޤާތިލު",
         role="the unknown killer of the Seventh Senate members; moves like a trained soldier; only his eyes are ever seen",
         gender="male", age="unknown",
         ethnicity_look="unknown, face hidden",
         face="face hidden by a fitted black cloth mask, only intense dark eyes full of deep, dark anger visible",
         hair="hidden under a black hood",
         build="tall, strong, athletic",
         default_outfit="a long black hooded coat over black clothes, a fitted black cloth mask covering the face below the eyes, black gloves",
         distinguishing_features="all in black, hood and mask, burning eyes",
         personality_cues="silent, precise, fast; glances back with cold anger",
         visual_prompt="the masked killer: a tall strong athletic man all in black, in a long black hooded coat over black clothes and black gloves, the hood up and a fitted black cloth mask covering his face below the eyes, so only his intense dark eyes full of deep, dark anger are visible; empty hands, no weapon.",
         ref_pose="left: head-and-shoulders portrait with the hood up, eyes glaring; right: full-body standing view, empty hands"),
]

FIRST = dict(alex=591, rogers=591, richard=591, sarah=615, masked_killer=615)

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

"""Beat/shot plan for Bappage Gatulu episode 522 — v2 RE-CUT on the new (slower, re-worded) audio.
First meeting of Iyaan and Raaya at the gallery, Asim's arrival, the café the next afternoon, the copied key card.
v1 images are reused via v1="beat_###" (old image file); new images only for spec 5.4 (speaker centred and sharp):
shot / reverse-shot pairs in the gallery (Raaya / Iyaan), Asim speaking, the café (Raaya x2 / Iyaan) and the car.
Rules: no touching between Iyaan and Raaya (hand-on-chest greeting, arm's-length gap in every two-shot), Raaya always in
a hijab fully covering her hair, Iyaan in a charcoal button-up shirt today, no readable text anywhere."""

SHIRT = ("Iyaan wears a dark charcoal long-sleeved button-up shirt with the top button done up and dark trousers, "
         "NOT the plain black t-shirt of the reference")
SHIRT2 = ("Iyaan (reference used for his face only) wears a dark charcoal long-sleeved button-up shirt with a collar and "
          "a row of buttons, the top button done up, and dark trousers, NOT the plain black t-shirt of the reference")
RAAYA_W = "Raaya in her loose long-sleeved ankle-length white dress and a light-grey hijab fully covering her hair and neck"
RAAYA_B = ("Raaya in a loose long-sleeved ankle-length soft light-blue dress (NOT the white dress of the reference) and her "
           "light-grey hijab fully covering her hair and neck")
GAP = "a clear arm's-length gap between Iyaan and Raaya, no touching"

LOC = {
    "male_day": "the dense skyline of Malé on a clear bright morning seen from above the harbour, tightly packed colourful "
                "concrete buildings, a busy main road along the waterfront full of motorbikes and cars, turquoise water and "
                "moored boats in the foreground",
    "bedroom": "Iyaan's small bedroom in a modest apartment in the morning, a tall plain mirror on a wardrobe door, a desk "
               "with dark computer monitors in the background, plain walls, a window with pale daylight",
    "gallery": "inside a spacious modern art gallery on a Malé seafront road: polished light-grey concrete floor, tall white "
               "walls hung with large modern paintings, a wide glass front with a big glass door looking onto the bright "
               "street, track spotlights, only a few quiet visitors",
    "gallery_front": "the glass front of a modern art gallery on a sunny Malé seafront road, a big glass door, the bright "
                     "street outside with palm trees and the sea wall beyond, no signs, no lettering",
    "cafe": "a breezy open-air seaside café near the Hulhumalé ferry terminal, wooden tables and chairs on a terrace right "
            "by the sea wall, turquoise sea and a ferry in the distance, other customers at tables in the background",
    "mansion_gate": "the front of a huge castle-like white mansion behind a high wall with a heavy steel gate, small CCTV "
                    "cameras on the wall corners, a glowing keypad panel beside the gate, two security guards in black suits",
    "car": "inside a dark modern car parked in front of a huge castle-like white mansion with a high wall and a steel gate",
}
MOOD = {
    "male_day": "a new day, clear blue morning sky, bright crisp sunlight with long soft shadows, busy ordinary life, a calm "
                "surface over coming tension",
    "bedroom": "early morning, pale cool daylight from the window and a dim teal room, his reflection in the mirror, quiet "
               "cold determination",
    "gallery": "late morning, soft diffused daylight through the glass front mixing with warm spotlights on the paintings, "
               "cool white and charcoal tones with red accents from the art, quiet and tense beneath the calm",
    "gallery_front": "midday, bright sunlight, sharp reflections in the glass, a sense of triumph",
    "cafe": "the next afternoon, bright breezy sea light, sparkling turquoise water, warm sun on the terrace, a light wind, "
            "a friendly mood hiding a calculated purpose",
    "mansion_gate": "afternoon, hard bright sunlight and deep shadows under the high wall, cold and guarded, imagined detail "
                    "with a faint soft vignette",
    "car": "late afternoon, warm golden sunlight slanting through the car windows, long shadows from the high mansion wall",
}

BEATS = [
    # 001
    dict(to=2, v1="beat_001", reason="episode opening: a new day in busy Malé", loc="male_day",
         visual="a bright clear morning over Malé: the dense colourful skyline under a clean blue sky, the busy waterfront "
                "road full of motorbikes and cars, a few small boats with plain unmarked white hulls on the turquoise water "
                "in the foreground, no people in close view, no signs, no lettering or numbers on any boat or building",
         camera="wide establishing shot, the skyline and sky in the upper two-thirds, calm water as the lower third",
         amb="city_day"),
    # 002
    dict(to=5, v1="beat_002", reason="scene and character change: Iyaan dressing in front of the mirror, steeling himself",
         chars=["iyaan"], loc="bedroom",
         visual=f"Iyaan standing fully dressed in front of a tall mirror, doing up the top button of his shirt with both "
                f"hands, staring at his own reflection with cold, controlled, calculating eyes; {SHIRT}; his reflection "
                f"visible in the mirror",
         camera="medium shot over his shoulder towards the mirror, both his face and the reflection in the upper half",
         amb="room_day"),
    # 003
    dict(to=8, v1="beat_003", reason="scene change: Iyaan enters the Athena Art Gallery", chars=["iyaan"], loc="gallery",
         visual=f"Iyaan stepping in through the big glass door of a bright modern gallery, one hand still on the door "
                f"handle, looking around at the large modern paintings on the white walls, two or three distant visitors "
                f"in the background; {SHIRT}",
         camera="medium wide shot from inside the gallery towards the glass door", amb="gallery"),
    # 004
    dict(to=9, v1="beat_004", reason="action change: he stops before the large painting of a red sun rising from a black sea",
         chars=["iyaan"], loc="gallery",
         visual=f"Iyaan standing still in the middle of the gallery seen from slightly behind and to the side, gazing up "
                f"at a huge oil painting of a blazing red sun rising out of a dark black sea, thick expressive brushstrokes, "
                f"warm spotlight on the canvas, the red light reflecting faintly on his face; {SHIRT}",
         camera="medium wide shot, low angle, the painting filling the upper half", amb="gallery"),
    # 005 NEW — Raaya speaks (shot of the gallery shot / reverse-shot pair)
    dict(to=11, speaker="raaya",
         reason="5.4 dialogue: Raaya speaks behind him about the painting — framed on her (shot / reverse shot)",
         chars=["raaya", "iyaan"], loc="gallery",
         visual=f"Raaya standing near the huge painting of a red sun rising out of a black sea, speaking softly with a "
                f"gentle, knowing smile and an innocent face, her face lit warmly by the gallery spotlight, hands folded in "
                f"front of her; seen past Iyaan, whose shoulder and the back of his head are soft and out of focus at the "
                f"left edge of the frame as he turns towards her; {GAP}, open floor between them; {RAAYA_W}; {SHIRT2}",
         camera="over-the-shoulder medium close-up on Raaya, her face centred in the upper half and in sharp focus, "
                "Iyaan soft and blurred in the left foreground, the polished floor as the lower third",
         amb="gallery"),
    # 006
    dict(to=12, v1="beat_005", reason="character enters: Raaya speaks behind him and he turns to face her",
         chars=["iyaan", "raaya"], loc="gallery",
         visual=f"Iyaan on the left, turned around from the red-sun painting to face Raaya, who stands on the right a "
                f"full arm's length and more away from him, with open floor clearly visible between them; {RAAYA_W}, "
                f"clean white sleeves, a soft innocent face and a gentle curious smile, hands folded in front of her; "
                f"Iyaan gives a small, simple smile; {GAP}, they stand well apart facing each other; {SHIRT}",
         camera="medium wide two-shot, eye level, side-on, the red-sun painting softly behind them", amb="gallery"),
    # 007 NEW — Iyaan answers (reverse shot)
    dict(to=14, speaker="iyaan", transition="cut",
         reason="5.4 dialogue: Iyaan answers about victory and hope — reverse shot framed on him",
         chars=["iyaan", "raaya"], loc="gallery",
         visual=f"Iyaan speaking calmly with a small simple smile and thoughtful, intelligent eyes, the huge painting of a "
                f"red sun rising out of a black sea glowing behind him; Raaya seen from behind, soft and out of focus at "
                f"the right edge of the frame, only her light-grey hijab and white sleeve visible; {GAP}; {SHIRT2}; "
                f"{RAAYA_W}",
         camera="over-the-shoulder medium close-up on Iyaan, his face centred in the upper half and in sharp focus, "
                "Raaya soft and blurred from behind in the right foreground",
         amb="gallery"),
    # 008
    dict(to=15, reuse="beat_005", transition="cut", reason="dialogue: Raaya introduces herself as the painter (reuse)",
         loc="gallery", visual="(reuse)", amb="gallery"),
    # 009
    dict(to=16, v1="beat_006", reason="action change: Raaya introduces herself as the painter; greeting with a hand on the chest",
         chars=["raaya", "iyaan"], loc="gallery",
         visual=f"Raaya, eyes wide with pleased surprise, smiling and nodding in greeting; Iyaan with his right hand placed "
                f"flat on his chest in a polite greeting, a slight respectful nod; they stand facing each other with "
                f"{GAP}; {RAAYA_W}; {SHIRT}; the red-sun painting on the wall beside them",
         camera="medium two-shot, eye level, side-on", amb="gallery",
         sens="intimacy", safe="the narration's handshake is replaced by a hand-on-chest greeting and a nod; arm's-length gap"),
    # 010
    dict(to=19, v1="beat_007", reason="action change: they walk and talk about art, philosophy and great artists",
         chars=["raaya", "iyaan"], loc="gallery",
         visual=f"Raaya and Iyaan walking slowly side by side along a white gallery wall of large modern paintings, Raaya "
                f"gesturing towards a canvas, talking animatedly with bright delighted eyes, Iyaan listening attentively "
                f"with a measured polite smile; {GAP}; {RAAYA_W}; {SHIRT}",
         camera="medium wide shot, slight low angle, paintings in the background", amb="gallery"),
    # 011
    dict(to=23, v1="beat_008", reason="characters change: two cars stop outside and Home Minister Asim walks in with security guards",
         chars=["iyaan", "asim", "raaya"], loc="gallery",
         visual=f"Iyaan in the sharp foreground, his jaw clenched and eyes hard with barely controlled rage, holding very "
                f"still; behind him in the mid-ground Raaya turning towards the glass door with a smile; beyond them Asim "
                f"striding in through the big glass door, proud and powerful in his crisp white shirt and black trousers, "
                f"two security guards in black suits with earpieces behind him and two black cars parked outside in the sun; "
                f"{GAP}; {RAAYA_W}; {SHIRT}",
         camera="close-up of Iyaan's face in the upper left foreground, deep focus to the door", amb="gallery"),
    # 012 NEW — Asim speaks
    dict(to=25, speaker="asim", transition="cut",
         reason="5.4 dialogue: Asim greets his daughter and asks who Iyaan is — framed on Asim (he is at the edge in the "
                "v1 three-shot)",
         chars=["asim", "raaya", "iyaan"], loc="gallery",
         visual=f"Asim speaking, a proud, cold, appraising face under his grey moustache, his shrewd narrow eyes looking "
                f"straight ahead towards the young man in the foreground; one hand resting fatherly on his daughter "
                f"Raaya's shoulder as she stands smiling beside him, slightly softer; Iyaan seen from behind, only his "
                f"dark hair and shoulder soft and out of focus at the left edge of the frame; two security guards in black "
                f"suits blurred near the glass door behind; {RAAYA_W}; {SHIRT2}",
         camera="over-the-shoulder medium close-up on Asim, his face centred in the upper half and in sharp focus, "
                "Raaya slightly softer beside him, Iyaan's shoulder blurred in the foreground",
         amb="gallery",
         sens="other", safe="father-daughter touch (Asim's hand on Raaya's shoulder) only; Iyaan stays apart"),
    # 013
    dict(to=26, v1="beat_009", transition="cut",
         reason="action change: Asim puts his hand on Raaya's shoulder and looks sharply at Iyaan",
         chars=["asim", "raaya", "iyaan"], loc="gallery",
         visual=f"Asim standing beside his daughter with one hand resting fatherly on Raaya's shoulder, his cold narrow "
                f"eyes fixed searchingly on Iyaan; Raaya smiling as she introduces Iyaan; Iyaan facing them composed, "
                f"hands at his sides; {GAP}; {RAAYA_W}; {SHIRT}; security guards blurred near the glass door",
         camera="medium three-shot, eye level", amb="gallery",
         sens="other", safe="father-daughter touch (Asim's hand on Raaya's shoulder) only; Iyaan stays apart"),
    # 014
    dict(to=27, reuse="beat_012", transition="cut", reason="dialogue: Asim asks which family Iyaan is from (reuse)",
         loc="gallery", visual="(reuse)", amb="gallery"),
    # 015
    dict(to=30, v1="beat_010", transition="cut",
         reason="emotional turning point: Iyaan looks the man straight in the eye and lies about his family",
         chars=["iyaan", "asim"], loc="gallery",
         visual=f"Iyaan and Asim face to face, Iyaan looking straight into Asim's eyes with a calm polite face and a cold "
                f"fire deep in his eyes, Asim with a slight appraising nod, a faint arrogant half-smile under his grey "
                f"moustache; {SHIRT}",
         camera="over-the-shoulder two-shot favouring Iyaan's face, eye level", amb="gallery"),
    # 016
    dict(to=32, reuse="beat_012", transition="cut", reason="dialogue: Asim says goodbye to Raaya and leaves (reuse)",
         loc="gallery", visual="(reuse)", amb="gallery"),
    # 017
    dict(to=34, v1="beat_011", reason="action change: Asim pats Iyaan's shoulder and leaves; Iyaan's silent vow",
         chars=["iyaan", "asim"], loc="gallery",
         visual=f"Iyaan in the foreground glancing down at his own shoulder where he was just patted, his face hardening "
                f"into silent cold resolve; in the background Asim walking away out of the glass door between his "
                f"security guards towards the black cars; {SHIRT}",
         camera="medium close-up of Iyaan, the doorway softly focused behind", amb="gallery"),
    # 018
    dict(to=35, reuse="beat_007", transition="cut", reason="dialogue: Iyaan tells Raaya he must go (reuse)",
         loc="gallery", visual="(reuse)", amb="gallery"),
    # 019
    dict(to=36, reuse="beat_005", transition="cut", reason="dialogue: Raaya says she will wait (reuse)",
         loc="gallery", visual="(reuse)", amb="gallery"),
    # 020
    dict(to=37, v1="beat_012", reason="scene change: Iyaan leaves the gallery onto the street, his first trap set",
         chars=["iyaan", "raaya"], loc="gallery_front",
         visual=f"Iyaan walking out of the gallery onto the bright sunny street with a faint confident smile, the glass "
                f"door swinging shut behind him; far behind the glass, Raaya inside the gallery watching him go with a "
                f"happy smile; {GAP}, the full width of the glass and the doorway between them; {RAAYA_W}; {SHIRT}",
         camera="medium wide shot from the street, eye level, the pavement as the lower third", amb="city_day"),
    # 021
    dict(to=41, v1="beat_013", reason="time jump and scene change: the next afternoon at the seaside café, Iyaan hides his notebook",
         chars=["iyaan"], loc="cafe",
         visual=f"Iyaan sitting alone at a sea-facing café table with a cup of black coffee, closing a small dark notebook "
                f"and slipping it into a bag at his side, his eyes lifted towards someone approaching in the distance, the "
                f"turquoise sea and a distant ferry behind him, the wind moving the parasol; the notebook pages are not "
                f"visible; {SHIRT}",
         camera="medium shot, eye level, the table top as the lower third", amb="harbour_cafe", transition="black"),
    # 022 NEW — Raaya arrives and speaks (café shot / reverse-shot pair)
    dict(to=42, speaker="raaya",
         reason="5.4 dialogue: Raaya arrives and greets him ('am I late?') — framed on her",
         chars=["raaya", "iyaan"], loc="cafe",
         visual=f"Raaya just sitting down across the sea-facing café table, smiling happily and speaking, bright-eyed, "
                f"her face in warm sea light; Iyaan seen from behind over his shoulder, only his dark hair and shoulder "
                f"soft and out of focus at the left edge of the frame; a cup of black coffee on the table between them, "
                f"the sparkling turquoise sea and a distant ferry behind her; {GAP}, the table between them; {RAAYA_B}; "
                f"{SHIRT2}",
         camera="over-the-shoulder medium close-up on Raaya, her face centred in the upper half and in sharp focus, "
                "Iyaan soft and blurred in the left foreground, the table top as the lower third",
         amb="harbour_cafe"),
    # 023 NEW — Iyaan at the café (reverse shot)
    dict(to=43, speaker="iyaan", transition="cut",
         reason="5.4 dialogue: Iyaan answers and asks what she would like — reverse shot framed on him",
         chars=["iyaan", "raaya"], loc="cafe",
         visual=f"Iyaan sitting at the sea-facing café table, speaking with a very friendly warm smile but sharp, "
                f"attentive eyes, a cup of black coffee in front of him, the turquoise sea and a distant ferry behind him; "
                f"Raaya seen from behind over her shoulder, soft and out of focus at the right edge of the frame, only her "
                f"light-grey hijab and light-blue sleeve visible; {GAP}, the table between them; {SHIRT2}; {RAAYA_B}",
         camera="over-the-shoulder medium close-up on Iyaan, his face centred in the upper half and in sharp focus, "
                "Raaya soft and blurred from behind in the right foreground, the table top as the lower third",
         amb="harbour_cafe"),
    # 024
    dict(to=45, v1="beat_014", reason="character enters: Raaya joins him and they order and talk", chars=["raaya", "iyaan"],
         loc="cafe",
         visual=f"Raaya seated across the café table from Iyaan, smiling happily as she talks about her paintings and "
                f"dreams; Iyaan listening attentively with a warm measured smile; two cups on the table between them, the "
                f"sparkling sea behind; {GAP}, the table between them; {RAAYA_B}; {SHIRT}",
         camera="medium two-shot from the side, eye level", amb="harbour_cafe"),
    # 025
    dict(to=47, reuse="beat_023", transition="cut",
         reason="dialogue: Iyaan's aim, and his casual question about her father's security (reuse)",
         loc="cafe", visual="(reuse)", amb="harbour_cafe"),
    # 026
    dict(to=48, v1="beat_015", transition="cut",
         reason="action change: he steers the talk to her father's security; she sighs about the cameras and guards",
         chars=["raaya", "iyaan"], loc="cafe",
         visual=f"Raaya looking down at her cup with a weary sigh, her smile fading as she talks about life under guard; "
                f"Iyaan leaning slightly forward across the table, a casual friendly face but sharp attentive eyes taking "
                f"in every word; {GAP}, the table between them; {RAAYA_B}; {SHIRT}",
         camera="medium close two-shot, favouring Iyaan's eyes, Raaya in soft profile", amb="harbour_cafe"),
    # 027 NEW — Raaya, serious (complaints about the security / the locked office)
    dict(to=51, speaker="raaya", transition="cut",
         reason="5.4 dialogue: Raaya talks about the guards, cameras and biometric lock — framed on her, a wistful mood "
                "different from her happy greeting",
         chars=["raaya", "iyaan"], loc="cafe",
         visual=f"Raaya at the café table speaking quietly with a wistful, weary look, her smile faded, her eyes lifted "
                f"to Iyaan, both hands around a white cup on the table; Iyaan seen from behind over his shoulder, only his "
                f"dark hair and shoulder soft and out of focus at the left edge of the frame; the bright sea behind her; "
                f"{GAP}, the table between them; {RAAYA_B}; {SHIRT2}",
         camera="over-the-shoulder medium close-up on Raaya, her face centred in the upper half and in sharp focus, "
                "Iyaan soft and blurred in the left foreground, the table top as the lower third",
         amb="harbour_cafe"),
    # 028
    dict(to=52, v1="beat_016", reason="imagined detail: the fortified mansion — CCTV, security guards, the biometric lock",
         loc="mansion_gate",
         visual="a close detail of a heavy steel mansion gate in hard sunlight: a sleek fingerprint scanner panel glowing "
                "soft blue beside the gate, a small CCTV camera on the high white wall above, two security guards in black "
                "suits with earpieces standing by the gate, faces turned away, no visible weapons, no text on the panel",
         camera="medium close-up of the scanner panel with the gate and camera above, slight low angle", amb="harbour_cafe",
         transition="dissolve"),
    # 029
    dict(to=54, reuse="beat_023", transition="dissolve", reason="dialogue: Iyaan reassures her (reuse)",
         loc="cafe", visual="(reuse)", amb="harbour_cafe"),
    # 030
    dict(to=55, reuse="beat_024", transition="cut", reason="return to the café two-shot: Raaya feels understood (reuse)",
         loc="cafe", visual="(reuse)", amb="harbour_cafe"),
    # 031
    dict(to=57, reuse="beat_027", transition="cut",
         reason="dialogue: Raaya on politics and her father's locked office (reuse)",
         loc="cafe", visual="(reuse)", amb="harbour_cafe"),
    # 032
    dict(to=58, v1="beat_018", reason="emotional turning point: he learns of the locked office and fixes his aim on it",
         chars=["iyaan"], loc="cafe",
         visual=f"close-up of Iyaan raising the coffee cup to his lips, his eyes narrowed and fixed on a far point over "
                f"the sea, a cold calculating focus behind a calm face, the wind stirring his swept-back hair; {SHIRT}",
         camera="close-up, eye level, the sea softly blurred behind", amb="harbour_cafe"),
    # 033
    dict(to=59, v1="beat_019", reason="scene change: he drives Raaya home to Asim's castle-like mansion",
         chars=["iyaan", "raaya"], loc="car",
         visual=f"inside the parked car: Iyaan in the driver's seat and Raaya in the passenger seat, turned slightly "
                f"towards each other and smiling warmly as they say goodbye, the centre console and {GAP}; through the "
                f"passenger window behind Raaya the high white wall and steel gate of a huge castle-like mansion; "
                f"{RAAYA_B}; {SHIRT}",
         camera="medium two-shot from the back seat between them, eye level", amb="car_interior"),
    # 034 NEW — Raaya in the car (car shot / reverse-shot pair)
    dict(to=60, speaker="raaya", transition="cut",
         reason="5.4 dialogue: Raaya says she had a happy day — framed on her (she is at the edge of the v1 car two-shot)",
         chars=["raaya", "iyaan"], loc="car",
         visual=f"inside the parked car: Raaya in the passenger seat turned towards the driver, speaking with a warm happy "
                f"smile, her face lit by golden late-afternoon light; through the passenger window behind her the high "
                f"white wall and steel gate of a huge castle-like mansion; Iyaan's shoulder in the driver's seat soft and "
                f"out of focus at the left edge of the frame; the centre console between them, {GAP}; {RAAYA_B}; {SHIRT2}",
         camera="medium close-up on Raaya from the driver's side, her face centred in the upper half and in sharp focus, "
                "Iyaan's shoulder blurred in the left foreground",
         amb="car_interior"),
    # 035 NEW — Iyaan in the car (reverse shot)
    dict(to=61, speaker="iyaan", transition="cut",
         reason="5.4 dialogue: Iyaan answers that he was happy too, later hands back the keys — reverse shot on him",
         chars=["iyaan", "raaya"], loc="car",
         visual=f"inside the parked car: Iyaan in the driver's seat turned towards the passenger seat, speaking with a "
                f"warm friendly smile, one hand on the steering wheel, golden light on his face; Raaya's light-blue sleeve "
                f"and light-grey hijab soft and out of focus at the right edge of the frame; the centre console between "
                f"them, {GAP}; the white mansion wall through the window behind him; {SHIRT2}; {RAAYA_B}",
         camera="medium close-up on Iyaan from the passenger side, his face centred in the upper half and in sharp focus, "
                "Raaya blurred at the right edge",
         amb="car_interior"),
    # 036
    dict(to=63, v1="beat_020", reason="action change: her key ring falls and he picks it up, secretly copying the card",
         chars=["iyaan"], loc="mansion_gate",
         visual=f"beside the open car door on the paving in front of the mansion gate, Iyaan crouching quickly to pick up a "
                f"small key ring with a few keys and a plain blank white electronic card, a tiny black scanner device "
                f"hidden in his palm under the card glowing a faint blue, his eyes focused and calm; {SHIRT}",
         camera="close-up on his hands and the key ring with his face in the upper frame, low angle", amb="car_interior",
         sens="other", safe="the card is plain and blank, no text; the copying is shown only as a faint blue glow in his palm"),
    # 037
    dict(to=64, reuse="beat_035", transition="cut", reason="dialogue: Iyaan hands back her keys with a smile (reuse)",
         loc="car", visual="(reuse)", amb="car_interior",
         sens="intimacy", safe="the hand-back of the keys is not shown as a touch"),
    # 038
    dict(to=67, v1="beat_021", reason="action change: Raaya walks to the house and Iyaan drives away smiling",
         chars=["iyaan", "raaya"], loc="car",
         visual=f"Iyaan behind the wheel of the car with a slow triumphant smile, looking out of the side window; far "
                f"outside, Raaya walking away towards the mansion gate holding her key ring, seen from behind; {GAP}, "
                f"Raaya many metres away outside the car; {RAAYA_B}; {SHIRT}",
         camera="medium close-up of Iyaan from the passenger side, the mansion gate through the window behind him",
         amb="car_interior",
         sens="intimacy", safe="the hand-back of the keys is not shown as a touch; Raaya is already walking away with them"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "A new day. The sky over Malé was clear. All across Malé the usual bustling life could be seen.")
sh(2, "But inside Iyaan something else was going on. His heart kept burning with a fire that would not go out.")
sh(3, "He was like a traveller on a journey to a destination he did not know. Standing in front of the mirror, he was doing up the buttons of his shirt.",
   [("cloth_rustle", "އަޅުވަމުން", -24)])
sh(4, "Looking at his reflection in the mirror, he reminded himself: from today on, every smile, every word and every glance of his would have to be carefully calculated and measured.")
sh(5, "He was setting out on a war to tear apart the world of an evil man, one of the most powerful people in the country.")
sh(6, "Iyaan headed for the Athena Art Gallery on Boduthakurufaanu Magu. It was the place run by Raaya, the daughter of Home Minister Asim.")
sh(7, "As he opened the gallery's big glass door, the smell of expensive canvases and all kinds of paints drifted out from inside.",
   [("door_open", "ހުޅުވާލުމާއެކު", -20)])
sh(8, "All kinds of modern paintings hung on the walls. There were few people inside. Iyaan walked slowly on and stopped in front of a big painting in the middle of the gallery.",
   [("footsteps_pavement", "ހިނގަމުން", -24)])
sh(9, "It was a deeply emotional painting of a red sun rising out of a black sea. Brought to life with oil colours, it was an extraordinarily fine painting.")
sh(10, "Iyaan stood gazing deeply at the painting. Soft footsteps sounded behind him. \"What this painting shows",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގެ", -22)], speaker="raaya")
sh(11, "is not just a sunrise.\" A young woman's gentle voice was heard. Iyaan slowly turned around.", speaker="raaya")
sh(12, "Standing before him was Raaya. She wore a simple white dress. With her shoulder-length hair and the innocence on her face, it would be hard even to believe she was the child of a cruel, evil killer.")
sh(13, "Iyaan smiled very simply. \"Yes, I think so too. This painting looks like the victory that comes after a great war.",
   speaker="iyaan")
sh(14, "Or like hope coming out of darkness.\" Raaya's eyes widened. People who could grasp the deep meaning of her paintings didn't usually come here.",
   speaker="iyaan")
sh(15, "\"That's a really good way to see it. I'm Raaya. I'm the one who painted this.\" \"I'm Iyaan.\"", speaker="raaya")
sh(16, "Iyaan held out his hand. Raaya greeted him with a smile. At that moment memories of his father's death came to Iyaan's heart, but his face showed no trace of it.")
sh(17, "Iyaan carried the conversation on. He talked about painting, philosophy and the world's famous artists.")
sh(18, "For many hours every night Iyaan had studied and memorised every subject Raaya liked.")
sh(19, "Raaya felt she had found an unusually good friend whose thinking matched hers completely. This was the first success of the trap Iyaan had set.")
sh(20, "While the two were talking, two cars stopped at the gallery door. Security guards got out of them. And walking in with them came Home Minister Asim.",
   [("car_approach", "ކާރު", -18), ("car_door", "ފޭބީ", -20), ("footsteps_pavement", "ހިނގާފައި", -22)])
sh(21, "He wore a white shirt and black trousers. His face showed pride and power. As Asim came into the gallery, Raaya said,")
sh(22, "\"Oh, that's my father.\" Iyaan's heart pounded harder. The very killer who had ordered his father's death was standing right in front of him.",
   [("heartbeat", "ތެޅުން", -20)], speaker="raaya", crop="tight", focus=[54, 35])
sh(23, "Iyaan's fists tightened. To control the rage rising inside him, he had to use all the strength of his will.",
   [("breath_heavy", "ރުޅިވެރިކަން", -22)], hum=True)
sh(24, "After a deep breath he brought his usual calm expression back to his face. \"My dear Raaya,\" Asim said, coming over and taking hold of Raaya's shoulder.",
   [("breath", "ނޭވާއެއްލުމަށްފަހު", -22)], speaker="asim")
sh(25, "His gaze stopped on Iyaan. Those shrewd political eyes looked Iyaan over. \"Who is this?\"", speaker="asim")
sh(26, "Raaya smiled. \"Bappa, this is Iyaan. He's someone who really loves my paintings.\"",
   speaker="raaya", crop="tight", focus=[34, 39])
sh(27, "Asim gave Iyaan an odd look. \"Iyaan... what family are you from?\"", speaker="asim")
sh(28, "Iyaan looked straight into Asim's eyes. It was as if the memories of the day his father died were swimming in them.",
   hum=True)
sh(29, "But Iyaan smiled and said, \"I'm from an ordinary family, Minister. My father was",
   speaker="iyaan", crop="tight", focus=[34, 35])
sh(30, "someone who used to run a business. He's no longer in this world.\" Asim nodded.",
   speaker="iyaan", crop="medium", focus=[36, 42])
sh(31, "He did not see in Iyaan's face the image of Ahmed Zahir, whom he had destroyed fifteen years ago. \"Good. Raaya, Bappa is off to a meeting.",
   speaker="asim")
sh(32, "Take care of yourself, dear,\" Asim said. As he turned to go, he patted Iyaan's shoulder lightly.",
   [("cloth_rustle", "ޖަހާލި", -22)], speaker="asim")
sh(33, "It was the kind of gesture a superior makes to someone beneath him. When Asim had gone out, Iyaan looked at the shoulder Asim had patted.",
   [("door_close", "ދިޔުމުން", -22)])
sh(34, "He said to himself, \"Your end will come by this very hand of mine.\" Iyaan turned back towards Raaya.",
   speaker="iyaan", crop="tight", focus=[33, 35], hum=True)
sh(35, "\"Raaya, I have to go now. We'll meet again later, won't we?\" Raaya nodded happily. \"Yes, of course.",
   speaker="iyaan")
sh(36, "I'll be waiting.\" When Iyaan left the gallery and stepped out onto the street, his first trap had been laid perfectly.",
   [("footsteps_pavement", "މަގުމައްޗަށް", -22)], speaker="raaya")
sh(37, "He had won the heart of Asim's daughter. And by coming face to face with the killer himself, he had cleared the road to his prey.")
sh(38, "After the first meeting at the Athena Art Gallery, the following afternoon was when Iyaan and Raaya had decided to meet at a café near the Hulhumalé ferry terminal.")
sh(39, "It was a place with lovely sea waves and cool breezes, but busy and crowded.",
   [("wave_crash", "ރާޅުތަކާއި", -22), ("wind_gust", "ރޯޅިތައް", -24)])
sh(40, "Iyaan sat at a table on the sea side, having ordered a black coffee. In the notebook in front of him some names and plans were written.")
sh(41, "But the moment he saw Raaya walking towards him in the distance, he quickly shut the book and put it in his bag. Today Raaya wore a soft light-blue dress.",
   [("page_turn", "ލައްޕާލައި", -20), ("cloth_rustle", "ދަބަހަށް", -24)])
sh(42, "Her face showed a happier smile than yesterday. \"Hello Iyaan, am I late?\"", speaker="raaya")
sh(43, "Raaya asked as she came and sat down on the chair. \"No, I just got here. What would Raaya like?\"",
   [("creak", "އިށީންނަމުން", -24)], speaker="iyaan")
sh(44, "Iyaan smiled in a very friendly way. After they ordered, the two began to talk. Raaya talked about her paintings and the dreams she had.")
sh(45, "Iyaan listened very attentively. But in another part of his mind a completely different plan was at work.")
sh(46, "Iyaan's aim was to get, from Raaya's own lips, the habits of Asim's household and its security details.")
sh(47, "\"Your father's very busy, isn't he? From what I saw yesterday, he seems to keep a lot of security too.\"",
   speaker="iyaan")
sh(48, "Iyaan asked in a very ordinary way, choosing his moment in the conversation. Raaya sighed deeply.",
   [("sigh", "ނޭވާއެއްލި", -20)])
sh(49, "\"Yes, because of Bappa's political life, things at home are kept very closed. Around the house", speaker="raaya")
sh(50, "there are always CCTV cameras and bodyguards. Sometimes I get fed up with having to live like that.", speaker="raaya")
sh(51, "Even getting inside the house is only possible through a biometric lock system.\" Iyaan's heart leapt. A biometric lock system.",
   [("heartbeat", "ތެޅިގަތް", -20)], speaker="raaya")
sh(52, "That was important information for him. It meant Asim's house could only be entered with Asim's or Raaya's own fingerprint, or by scanning their faces.")
sh(53, "\"Well, that's for your safety, isn't it. But being shut in that much at home", speaker="iyaan")
sh(54, "can't be easy for an artist,\" Iyaan said in a way that would reassure Raaya. \"That's so true,\"", speaker="iyaan")
sh(55, "Raaya looked at Iyaan, having decided that he was the only person who understood her feelings.")
sh(56, "\"Bappa wants me to go into politics too. But I don't want that.", speaker="raaya")
sh(57, "Even going into Bappa's office room is forbidden for us. It's always kept locked.\"", speaker="raaya")
sh(58, "Iyaan touched the coffee cup to his lips. He became certain that the secret office room in Asim's house was where the remaining evidence of his father's death and the papers of Asim's present dirty dealings would be kept.",
   [("cup_clatter", "ތަށި", -22)])
sh(59, "His aim was to get into that room. But that was not going to be easy. After finishing the coffee, Iyaan set off to drop Raaya home.",
   [("car_approach", "ހިނގައިގަތް", -20)])
sh(60, "They stopped at the gate of Asim's huge, castle-like house. \"Iyaan, today I was really happy, because I found a friend who thinks like that.\"",
   speaker="raaya")
sh(61, "\"I was very happy too,\" Iyaan said. Just as Raaya was getting out of the car, a small key ring fell from her handbag to the ground.",
   [("car_door", "ފައިބަން", -20), ("soft_thud", "ވެއްޓުނު", -22)], speaker="iyaan")
sh(62, "On that key ring, besides the keys of Raaya's art gallery, there was a small electronic card. Iyaan quickly bent down and picked up the key ring.",
   [("cloth_rustle", "ގުދުވެ", -24)])
sh(63, "The moment he picked it up, a tiny digital scanner hidden in his palm secretly copied the data of that electronic card.",
   [("computer_beep", "ކޮޕީކޮށްލި", -22)], hum=True)
sh(64, "It was something Iyaan had come prepared for. \"Here are Raaya's keys,\" Iyaan said with a smile, holding them out. \"Thanks, Iyaan.\"",
   speaker="iyaan")
sh(65, "Raaya took them, got out of the car and set off towards the door of the house. Iyaan drove off.",
   [("car_door", "ފައިބައިގެން", -20), ("footsteps_pavement", "ހިނގައިގަތް", -24), ("car_drive_off", "ދުއްވާލި", -18)])
sh(66, "His face showed a smile full of the hope of success. In his hand now was a copy of the digital card that could open the first security door of Asim's house.")
sh(67, "The second step was close at hand. To be continued.")

# 5.4: crop/focus of the dialogue shots on the NEW speaker images, read off work/grid/new_0#.jpg (face centre, y + ~8)
FOCUS = {
    10: ("tight", [62, 37]), 11: ("medium", [62, 42]), 15: ("tight", [62, 37]), 36: ("medium", [62, 42]),   # beat_005 Raaya
    13: ("tight", [40, 35]), 14: ("medium", [40, 42]), 35: ("tight", [40, 35]),                             # beat_007 Iyaan
    24: ("medium", [47, 42]), 25: ("tight", [47, 35]), 27: ("tight", [47, 35]),                             # beat_012 Asim
    31: ("medium", [47, 42]), 32: ("tight", [47, 35]),
    42: ("tight", [56, 37]),                                                                                # beat_022 Raaya
    43: ("tight", [38, 35]), 47: ("tight", [38, 35]), 53: ("medium", [38, 42]), 54: ("tight", [38, 35]),   # beat_023 Iyaan
    49: ("medium", [58, 44]), 50: ("tight", [58, 42]), 51: ("medium", [58, 44]),                            # beat_027 Raaya
    56: ("tight", [58, 42]), 57: ("medium", [58, 44]),
    60: ("tight", [45, 37]),                                                                                # beat_034 Raaya
    61: ("tight", [50, 35]), 64: ("medium", [50, 42]),                                                      # beat_035 Iyaan
}
for _i, (_c, _f) in FOCUS.items():
    assert S[_i][2].get("speaker"), _i
    S[_i][2].update(crop=_c, focus=_f)
SHOTS = S

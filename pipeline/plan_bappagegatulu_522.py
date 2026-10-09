"""Beat/shot plan for Bappage Gatulu episode 522 (used by plan_beats.py).
First meeting of Iyaan and Raaya at the gallery, Asim's arrival, the café the next afternoon, the copied key card.
Rules: no touching between Iyaan and Raaya (hand-on-chest greeting, arm's-length gap in every two-shot), Raaya always in
a hijab fully covering her hair, Iyaan in a charcoal button-up shirt today, no readable text anywhere."""

SHIRT = ("Iyaan wears a dark charcoal long-sleeved button-up shirt with the top button done up and dark trousers, "
         "NOT the plain black t-shirt of the reference")
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
    dict(to=2, reason="episode opening: a new day in busy Malé", loc="male_day",
         visual="a bright clear morning over Malé: the dense colourful skyline under a clean blue sky, the busy waterfront "
                "road full of motorbikes and cars, a few small boats with plain unmarked white hulls on the turquoise water "
                "in the foreground, no people in close view, no signs, no lettering or numbers on any boat or building",
         camera="wide establishing shot, the skyline and sky in the upper two-thirds, calm water as the lower third",
         amb="city_day"),
    dict(to=6, reason="scene and character change: Iyaan dressing in front of the mirror, steeling himself", chars=["iyaan"],
         loc="bedroom",
         visual=f"Iyaan standing fully dressed in front of a tall mirror, doing up the top button of his shirt with both "
                f"hands, staring at his own reflection with cold, controlled, calculating eyes; {SHIRT}; his reflection "
                f"visible in the mirror",
         camera="medium shot over his shoulder towards the mirror, both his face and the reflection in the upper half",
         amb="room_day"),
    dict(to=9, reason="scene change: Iyaan enters the Athena Art Gallery", chars=["iyaan"], loc="gallery",
         visual=f"Iyaan stepping in through the big glass door of a bright modern gallery, one hand still on the door "
                f"handle, looking around at the large modern paintings on the white walls, two or three distant visitors "
                f"in the background; {SHIRT}",
         camera="medium wide shot from inside the gallery towards the glass door", amb="gallery"),
    dict(to=11, reason="action change: he stops before the large painting of a red sun rising from a black sea",
         chars=["iyaan"], loc="gallery",
         visual=f"Iyaan standing still in the middle of the gallery seen from slightly behind and to the side, gazing up "
                f"at a huge oil painting of a blazing red sun rising out of a dark black sea, thick expressive brushstrokes, "
                f"warm spotlight on the canvas, the red light reflecting faintly on his face; {SHIRT}",
         camera="medium wide shot, low angle, the painting filling the upper half", amb="gallery"),
    dict(to=14, reason="character enters: Raaya speaks behind him and he turns to face her", chars=["iyaan", "raaya"],
         loc="gallery",
         visual=f"Iyaan on the left, turned around from the red-sun painting to face Raaya, who stands on the right a "
                f"full arm's length and more away from him, with open floor clearly visible between them; {RAAYA_W}, "
                f"clean white sleeves, a soft innocent face and a gentle curious smile, hands folded in front of her; "
                f"Iyaan gives a small, simple smile; {GAP}, they stand well apart facing each other; {SHIRT}",
         camera="medium wide two-shot, eye level, side-on, the red-sun painting softly behind them", amb="gallery"),
    dict(to=17, reason="action change: Raaya introduces herself as the painter; greeting with a hand on the chest",
         chars=["raaya", "iyaan"], loc="gallery",
         visual=f"Raaya, eyes wide with pleased surprise, smiling and nodding in greeting; Iyaan with his right hand placed "
                f"flat on his chest in a polite greeting, a slight respectful nod; they stand facing each other with "
                f"{GAP}; {RAAYA_W}; {SHIRT}; the red-sun painting on the wall beside them",
         camera="medium two-shot, eye level, side-on", amb="gallery",
         sens="intimacy", safe="the narration's handshake is replaced by a hand-on-chest greeting and a nod; arm's-length gap"),
    dict(to=20, reason="action change: they walk and talk about art, philosophy and great artists",
         chars=["raaya", "iyaan"], loc="gallery",
         visual=f"Raaya and Iyaan walking slowly side by side along a white gallery wall of large modern paintings, Raaya "
                f"gesturing towards a canvas, talking animatedly with bright delighted eyes, Iyaan listening attentively "
                f"with a measured polite smile; {GAP}; {RAAYA_W}; {SHIRT}",
         camera="medium wide shot, slight low angle, paintings in the background", amb="gallery"),
    dict(to=24, reason="characters change: two cars stop outside and Home Minister Asim walks in with security guards",
         chars=["iyaan", "asim", "raaya"], loc="gallery",
         visual=f"Iyaan in the sharp foreground, his jaw clenched and eyes hard with barely controlled rage, holding very "
                f"still; behind him in the mid-ground Raaya turning towards the glass door with a smile; beyond them Asim "
                f"striding in through the big glass door, proud and powerful in his crisp white shirt and black trousers, "
                f"two security guards in black suits with earpieces behind him and two black cars parked outside in the sun; "
                f"{GAP}; {RAAYA_W}; {SHIRT}",
         camera="close-up of Iyaan's face in the upper left foreground, deep focus to the door", amb="gallery"),
    dict(to=27, reason="action change: Asim puts his hand on Raaya's shoulder and looks sharply at Iyaan",
         chars=["asim", "raaya", "iyaan"], loc="gallery",
         visual=f"Asim standing beside his daughter with one hand resting fatherly on Raaya's shoulder, his cold narrow "
                f"eyes fixed searchingly on Iyaan; Raaya smiling as she introduces Iyaan; Iyaan facing them composed, "
                f"hands at his sides; {GAP}; {RAAYA_W}; {SHIRT}; security guards blurred near the glass door",
         camera="medium three-shot, eye level", amb="gallery",
         sens="other", safe="father-daughter touch (Asim's hand on Raaya's shoulder) only; Iyaan stays apart"),
    dict(to=30, reason="emotional turning point: Iyaan looks the man straight in the eye and lies about his family",
         chars=["iyaan", "asim"], loc="gallery",
         visual=f"Iyaan and Asim face to face, Iyaan looking straight into Asim's eyes with a calm polite face and a cold "
                f"fire deep in his eyes, Asim with a slight appraising nod, a faint arrogant half-smile under his grey "
                f"moustache; {SHIRT}",
         camera="over-the-shoulder two-shot favouring Iyaan's face, eye level", amb="gallery"),
    dict(to=33, reason="action change: Asim pats Iyaan's shoulder and leaves; Iyaan's silent vow",
         chars=["iyaan", "asim"], loc="gallery",
         visual=f"Iyaan in the foreground glancing down at his own shoulder where he was just patted, his face hardening "
                f"into silent cold resolve; in the background Asim walking away out of the glass door between his "
                f"security guards towards the black cars; {SHIRT}",
         camera="medium close-up of Iyaan, the doorway softly focused behind", amb="gallery"),
    dict(to=35, reason="scene change: Iyaan leaves the gallery onto the street, his first trap set",
         chars=["iyaan", "raaya"], loc="gallery_front",
         visual=f"Iyaan walking out of the gallery onto the bright sunny street with a faint confident smile, the glass "
                f"door swinging shut behind him; far behind the glass, Raaya inside the gallery watching him go with a "
                f"happy smile; {GAP}, the full width of the glass and the doorway between them; {RAAYA_W}; {SHIRT}",
         camera="medium wide shot from the street, eye level, the pavement as the lower third", amb="city_day"),
    dict(to=38, reason="time jump and scene change: the next afternoon at the seaside café, Iyaan hides his notebook",
         chars=["iyaan"], loc="cafe",
         visual=f"Iyaan sitting alone at a sea-facing café table with a cup of black coffee, closing a small dark notebook "
                f"and slipping it into a bag at his side, his eyes lifted towards someone approaching in the distance, the "
                f"turquoise sea and a distant ferry behind him, the wind moving the parasol; the notebook pages are not "
                f"visible; {SHIRT}",
         camera="medium shot, eye level, the table top as the lower third", amb="harbour_cafe", transition="black"),
    dict(to=42, reason="character enters: Raaya joins him and they order and talk", chars=["raaya", "iyaan"], loc="cafe",
         visual=f"Raaya seated across the café table from Iyaan, smiling happily as she talks about her paintings and "
                f"dreams; Iyaan listening attentively with a warm measured smile; two cups on the table between them, the "
                f"sparkling sea behind; {GAP}, the table between them; {RAAYA_B}; {SHIRT}",
         camera="medium two-shot from the side, eye level", amb="harbour_cafe"),
    dict(to=46, reason="action change: he steers the talk to her father's security; she sighs about the cameras and guards",
         chars=["raaya", "iyaan"], loc="cafe",
         visual=f"Raaya looking down at her cup with a weary sigh, her smile fading as she talks about life under guard; "
                f"Iyaan leaning slightly forward across the table, a casual friendly face but sharp attentive eyes taking "
                f"in every word; {GAP}, the table between them; {RAAYA_B}; {SHIRT}",
         camera="medium close two-shot, favouring Iyaan's eyes, Raaya in soft profile", amb="harbour_cafe"),
    dict(to=48, reason="imagined detail: the fortified mansion — CCTV, security guards, the biometric lock", loc="mansion_gate",
         visual="a close detail of a heavy steel mansion gate in hard sunlight: a sleek fingerprint scanner panel glowing "
                "soft blue beside the gate, a small CCTV camera on the high white wall above, two security guards in black "
                "suits with earpieces standing by the gate, faces turned away, no visible weapons, no text on the panel",
         camera="medium close-up of the scanner panel with the gate and camera above, slight low angle", amb="harbour_cafe",
         transition="dissolve"),
    dict(to=50, reuse="beat_014", reason="return to the café two-shot: Raaya feels understood", loc="cafe",
         visual="(reuse)", amb="harbour_cafe", transition="dissolve"),
    dict(to=53, reason="emotional turning point: he learns of the locked office and fixes his aim on it",
         chars=["iyaan"], loc="cafe",
         visual=f"close-up of Iyaan raising the coffee cup to his lips, his eyes narrowed and fixed on a far point over "
                f"the sea, a cold calculating focus behind a calm face, the wind stirring his swept-back hair; {SHIRT}",
         camera="close-up, eye level, the sea softly blurred behind", amb="harbour_cafe"),
    dict(to=55, reason="scene change: he drives Raaya home to Asim's castle-like mansion", chars=["iyaan", "raaya"],
         loc="car",
         visual=f"inside the parked car: Iyaan in the driver's seat and Raaya in the passenger seat, turned slightly "
                f"towards each other and smiling warmly as they say goodbye, the centre console and {GAP}; through the "
                f"passenger window behind Raaya the high white wall and steel gate of a huge castle-like mansion; "
                f"{RAAYA_B}; {SHIRT}",
         camera="medium two-shot from the back seat between them, eye level", amb="car_interior"),
    dict(to=58, reason="action change: her key ring falls and he picks it up, secretly copying the card",
         chars=["iyaan"], loc="mansion_gate",
         visual=f"beside the open car door on the paving in front of the mansion gate, Iyaan crouching quickly to pick up a "
                f"small key ring with a few keys and a plain blank white electronic card, a tiny black scanner device "
                f"hidden in his palm under the card glowing a faint blue, his eyes focused and calm; {SHIRT}",
         camera="close-up on his hands and the key ring with his face in the upper frame, low angle", amb="car_interior",
         sens="other", safe="the card is plain and blank, no text; the copying is shown only as a faint blue glow in his palm"),
    dict(to=61, reason="action change: Raaya walks to the house and Iyaan drives away smiling", chars=["iyaan", "raaya"],
         loc="car",
         visual=f"Iyaan behind the wheel of the car with a slow triumphant smile, looking out of the side window; far "
                f"outside, Raaya walking away towards the mansion gate holding her key ring, seen from behind; {GAP}, "
                f"Raaya many metres away outside the car; {RAAYA_B}; {SHIRT}",
         camera="medium close-up of Iyaan from the passenger side, the mansion gate through the window behind him",
         amb="car_interior",
         sens="intimacy", safe="the hand-back of the keys is not shown as a touch; Raaya is already walking away with them"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "A new day. The sky over Malé was clear. Ordinary, bustling life could be seen all through the city.")
sh(2, "But something else was going on inside Iyaan. His heart kept burning with a fire that would not go out.")
sh(3, "He was like a traveller on a journey whose destination he did not know. Standing in front of the mirror, he did up the buttons of his shirt.",
   [("cloth_rustle", "އަޅުވަމުން", -24)])
sh(4, "Looking at his reflection in the mirror, he reminded himself:")
sh(5, "from today on, every smile, every word and every glance of his would have to be carefully calculated and measured.")
sh(6, "He was setting out on a war to tear apart the world of one of the most evil men among the most powerful people in the country.")
sh(7, "Iyaan headed for the 'Athena Art Gallery' on Boduthakurufaanu Magu. It was the place run by Raaya, the daughter of Home Minister Asim.")
sh(8, "As he opened the gallery's big glass door, the smell of expensive canvases and all kinds of paints drifted out from inside.",
   [("door_open", "ހުޅުވާލުމާއެކު", -20)])
sh(9, "All sorts of modern paintings hung on the walls. There were few people inside. Iyaan walked slowly on,",
   [("footsteps_pavement", "ހިނގަމުން", -24)])
sh(10, "and stopped in front of a large painting in the middle of the gallery. It showed a red sun rising out of a black sea —")
sh(11, "a deeply emotional painting. Brought to life with oil colours, it was an extraordinarily fine work. Iyaan stood gazing at it intently.")
sh(12, "Soft footsteps sounded behind him. \"This painting doesn't show only a sunrise,\" came a young woman's gentle voice.",
   [("footsteps_pavement", "ފިޔަވަޅުތަކެއްގެ", -22)])
sh(13, "Iyaan slowly turned around. Standing before him was Raaya. She wore a simple white dress. With her shoulder-length hair",)
sh(14, "and the innocence on her face, it would be hard even to believe she was the child of a cruel, evil killer. Iyaan smiled very simply.")
sh(15, "\"Yes, I think so too. This painting looks like the victory that comes after a great war. Or like hope rising out of darkness.\"")
sh(16, "Raaya's eyes widened. People who could grasp the deep meaning of her paintings rarely came here. \"That's a wonderful way to see it. I'm Raaya.")
sh(17, "I'm the one who painted it.\" \"I'm Iyaan,\" Iyaan said, offering his greeting. Raaya returned the greeting with a smile.")
sh(18, "At that moment memories of his father's death came to Iyaan's heart, but his face showed no trace of it. Iyaan carried on the conversation.")
sh(19, "He talked about painting, philosophy and the world's famous artists. For many hours each night Iyaan had studied and memorised every subject Raaya loved.")
sh(20, "Raaya felt she had found an unusually good friend whose thinking matched hers completely. This was the first success of the trap Iyaan had set.")
sh(21, "While the two were talking, two cars stopped at the gallery door. Security guards got out of them.",
   [("car_approach", "ކާރު", -18), ("car_door", "ފޭބީ", -20)])
sh(22, "And walking in with them came Home Minister Asim. He wore a white shirt and black trousers. His face showed pride and power.",
   [("footsteps_pavement", "ހިނގާފައި", -22)])
sh(23, "As Asim entered the gallery, Raaya said, \"Oh, that's my father.\" Iyaan's heart began to pound.",
   [("heartbeat", "ތެޅުން", -20)])
sh(24, "The very man who had ordered his father's death was standing in front of him. Iyaan's fists tightened. It took all his willpower to control the rage rising inside him.",
   [("breath_heavy", "ރުޅިވެރިކަން", -22)], hum=True)
sh(25, "After a deep breath he brought his usual calm expression back to his face. \"My dear Raaya,\" Asim said, coming over and taking hold of Raaya's shoulder.",
   [("breath", "ނޭވާއެއްލުމަށްފަހު", -22)])
sh(26, "His gaze stopped on Iyaan. Those shrewd political eyes looked Iyaan over. \"Who is this?\" Raaya smiled. \"Bappa, this is Iyaan.")
sh(27, "He's someone who really loves my paintings.\" Asim gave Iyaan an odd look. \"Iyaan... which family are you from?\"")
sh(28, "Iyaan looked straight into Asim's eyes. It was as if the memories of the day his father died were swimming in them. But Iyaan smiled and said,",
   hum=True)
sh(29, "\"I'm from an ordinary family, Minister. My father used to run a business. He is no longer in this world.\"")
sh(30, "Asim nodded. He did not see in Iyaan's face the image of Ahmed Zahir, whom he had destroyed fifteen years ago. \"Good. Raaya,")
sh(31, "Bappa is off to a meeting. Take care of yourself, dear,\" Asim said. As he turned to go, he patted Iyaan's shoulder lightly.",
   [("cloth_rustle", "ޖަހާލިއެވެ", -22)])
sh(32, "It was the kind of gesture a superior makes to someone beneath him. When Asim had left, Iyaan looked at the shoulder Asim had touched. He said to himself,",
   [("door_close", "ދިޔުމުން", -22)])
sh(33, "\"Your end will come by this very hand of mine.\" Iyaan turned back to Raaya. \"Raaya, I have to go now. We'll meet again, won't we?\"",
   hum=True)
sh(34, "Raaya nodded happily. \"Yes, of course. I'll be waiting.\" As Iyaan left the gallery and stepped out onto the street,",
   [("footsteps_pavement", "މަގުމައްޗަށް", -22)])
sh(35, "his first trap had been laid perfectly. He had won the heart of Asim's daughter, and by coming face to face with the killer himself he had cleared the road to his prey.")
sh(36, "After that first meeting at the Athena Art Gallery, the next afternoon was the time Iyaan and Raaya had decided to meet at a café near the Hulhumalé ferry terminal.")
sh(37, "It was a place with lovely sea waves and cool breezes, but busy and crowded. Iyaan sat at a table facing the sea, having ordered a black coffee.",
   [("wave_crash", "ރާޅުތަކާއި", -22), ("wind_gust", "ރޯޅިތައް", -24)])
sh(38, "In the notebook in front of him some names and plans were written. But the moment he saw Raaya walking towards him in the distance, he quickly shut it and put it in his bag.",
   [("page_turn", "ލައްޕާލައި", -20), ("cloth_rustle", "ދަބަހަށް", -24)])
sh(39, "Today Raaya wore a soft light-blue dress. Her face showed a happier smile than yesterday. \"Hello Iyaan, am I late?\"")
sh(40, "Raaya asked as she sat down. \"No, I just got here,\" Iyaan said with a very friendly smile. \"What would you like, Raaya?\"",
   [("creak", "އިށީންނަމުން", -24)])
sh(41, "After they ordered, the conversation began. Raaya talked about her paintings and the dreams she had.")
sh(42, "Iyaan listened very attentively. But in another part of his mind a completely different plan was at work.")
sh(43, "Iyaan's aim was to get from Raaya's own lips the habits of Asim's household and its security details. \"Your father's very busy, isn't he?")
sh(44, "From what I saw yesterday, he seems to keep a lot of security too,\" Iyaan asked very casually, choosing his moment in the conversation.")
sh(45, "Raaya sighed deeply. \"Yes. Because of Bappa's political life, things at home are kept very closed.",
   [("sigh", "ނޭވާއެއްލިއެވެ", -20)])
sh(46, "There are always CCTV cameras and security guards around the house. Sometimes I get fed up with having to live like that.")
sh(47, "You can only even get inside the house through a biometric lock system.\" Iyaan's heart leapt. A biometric lock system. That was important information for him.",
   [("heartbeat", "ތެޅިގަތެވެ", -20)])
sh(48, "It meant that Asim's house could only be entered with Asim's or Raaya's own fingerprint, or by scanning their faces.")
sh(49, "\"Well, that's for your safety, isn't it,\" Iyaan said in a way that would reassure Raaya. \"But being shut in that much at home can't be easy for an artist.\"")
sh(50, "\"That's so true,\" Raaya said, looking at Iyaan and deciding he was the only person who understood her feelings.")
sh(51, "\"Bappa wants me to go into politics too. But I don't want that. Even going into Bappa's office room is forbidden for us.")
sh(52, "It's always kept locked.\" Iyaan touched the coffee cup to his lips. He became certain that the secret office room in Asim's house was where the remaining evidence of his father's death,",
   [("cup_clatter", "ތަށި", -22)])
sh(53, "and the papers of Asim's present dirty dealings, would be kept. His goal was to get into that room.")
sh(54, "But that would not be easy. After finishing the coffee, Iyaan set off to drop Raaya home. They stopped at the gate of Asim's huge, castle-like house.",
   [("car_approach", "ހިނގައިގަތެވެ", -20)])
sh(55, "Raaya said, \"Iyaan, I had a really happy day today. Because I found a friend who thinks like that.\" \"I was very happy too,\" Iyaan said.")
sh(56, "Just as Raaya was getting out of the car, a small key ring fell from her handbag to the ground.",
   [("car_door", "ފައިބަން", -20), ("soft_thud", "ވެއްޓުނެވެ", -22)])
sh(57, "On that key ring, besides the keys of Raaya's art gallery, there was a small electronic card. Iyaan quickly bent down and picked up the key ring. The moment he picked it up,",
   [("cloth_rustle", "ގުދުވެ", -24)])
sh(58, "a tiny digital scanner hidden in his palm secretly copied the data of that electronic card. It was something Iyaan had come prepared for.",
   [("computer_beep", "ކޮޕީކޮށްލިއެވެ", -22)], hum=True)
sh(59, "\"Here are your keys, Raaya,\" Iyaan said with a smile, holding them out. \"Thanks, Iyaan,\" Raaya said, taking them, and she got out of the car and walked towards the door of the house.",
   [("car_door", "ފައިބައިގެން", -20), ("footsteps_pavement", "ހިނގައިގަތެވެ", -24)])
sh(60, "Iyaan drove off. His face showed a smile full of the hope of success.",
   [("car_drive_off", "ދުއްވާލިއެވެ", -18)])
sh(61, "In his hand now was a copy of the digital card that could open the first security door of Asim's house. The second step was close. To be continued.")
SHOTS = S

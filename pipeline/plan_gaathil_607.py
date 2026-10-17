"""Beat/shot plan for Gaathil episode 607 (police station -> photo at home -> harbour warehouses -> the mask; used by plan_beats.py)."""

LOC = {
    "interview_room": "a cold bare interview room in the modest whitewashed island police station: plain grey-white walls with faint mould stains, a scratched wooden table with two chairs, a closed laptop-style computer on the table with its screen turned away, one tall window with old wooden frames and a dusty glass looking out onto a sandy lane and coconut palms",
    "amjad_office": "Officer Amjad's small office in the island police station: a heavy wooden desk with a closed laptop and a few plain blank folders, a desk drawer pulled fully open, a closed plain wooden door with a key turned in its lock, half-closed window blinds striping the wall with thin bars of light",
    "station_lane": "outside the modest whitewashed island police station: a low coral-stone building with arched wooden windows and a plain wooden door with no sign, a wide sandy lane in front lined with coconut palms and low coral-stone walls",
    "shahid_room_day": "Shahid's room in an old coral-stone island house by day: a wooden desk with a computer and a big monitor, camera gear and lenses on the desk, a window with half-open wooden shutters letting in a slanting beam of daylight, a ceiling bulb switched off",
    "photo": "the inside of Shahid's rainy night photograph shown full-frame: a dark patch of wet sandy ground among the shadows of trees, silver rain streaks, a broken old coral-stone wall behind",
    "warehouses": "the row of old abandoned warehouses (ba gudhan) near the east-side harbour of the island: long low buildings of weathered broken whitewashed coral-stone with black mould streaks, partly collapsed rusted corrugated-iron roofs, sagging grey wooden doors hanging open on dark interiors, narrow sandy lanes between them strewn with rusted iron scraps, one broken wall with a crumbling arched opening, a glimpse of the grey harbour water and an old moored wooden dhoni with no lettering beyond",
    "harbour_lane": "the sandy lane leading away from the east harbour warehouses towards the village: coconut palms, low crumbling coral-stone walls, long shadows, the old warehouses small in the distance behind",
    "shahid_room_night": "Shahid's room at night in the old coral-stone island house: the wooden desk under a bright angled desk lamp throwing a hard warm cone of light, the big monitor dark, camera gear in shadow, the wooden window shutters closed, the room door shut and locked",
}
MOOD = {
    "interview_room": "mid-morning, cold flat grey daylight through the window, bare and tense, deep shadows in the corners",
    "amjad_office": "mid-morning behind closed blinds, dim cold grey light cut into thin bright stripes, secretive and claustrophobic",
    "station_lane": "late morning, pale washed-out sunlight under a hazy sky, ordinary daylight with an uneasy, watchful undertone",
    "shahid_room_day": "daytime, a single slanting beam of pale daylight through the shutters plus the cold glow of the monitor, quiet concentration",
    "photo": "near-black blue-grey storm night, silver rain, a white flash of lightning lighting the ground, grainy and unsettling",
    "warehouses": "overcast afternoon, flat grey light, heavy brooding clouds over the harbour, empty and silent, quietly menacing",
    "harbour_lane": "late overcast afternoon turning to dusk, grey-amber sky, long soft shadows, anxious",
    "shahid_room_night": "evening, the room dark except for the single hard warm cone of the desk lamp, intimate, secretive, deep charcoal shadows",
}

COPS = ("two or three ordinary island police officers in plain dark navy uniform shirts with no badges and no lettering, "
        "empty hands, no weapons, no holsters, no batons, no handcuffs")
MASK = ("a soft flesh-toned theatrical silicone face mask like a film-studio prop: a smooth matte beige rubbery hollow face "
        "shape with empty eye holes, limp and slightly crumpled, no hair, clearly an artificial prop, no blood, nothing gory")

BEATS = [
    dict(to=2, reason="episode opening (repeat of 606's end): Amjad has risen and stands at the interview-room window, a storm in his head", chars=["amjad", "shahid"], loc="interview_room",
         visual="Officer Amjad standing at the tall window of the bare interview room with his back half-turned to the room, seen in three-quarter profile, his jaw clenched and his sharp eyes narrowed as he stares out at the grey sandy lane, one hand resting tensely on the window frame; behind him at the table Shahid sits watching him, softer and smaller, the laptop on the table with its screen turned away; cold grey light falls across Amjad's face",
         camera="medium wide, eye level, Amjad at the window in the upper two-thirds, the bare table top and floor as the lower third",
         amb="office_quiet"),
    dict(to=7, reason="action change + dialogue: Amjad turns, puts his hand on Shahid's shoulder and swears him to secrecy (Amjad speaking; Shahid's reaction on a crop)", chars=["amjad", "shahid"], loc="interview_room",
         visual="Officer Amjad standing beside the seated Shahid, his right hand resting firmly on Shahid's shoulder, leaning down slightly and speaking in a low commanding voice, face calm and controlled but his eyes hard; Shahid seated at the table turned up towards him in three-quarter view, listening, nodding slowly, a faint guarded suspicion in his eyes; both faces clearly visible; cold grey window light from the side",
         camera="medium two-shot, slightly low angle, Amjad's face centred in the upper half, Shahid's face lower-right in the upper half, the table top as the lower third",
         amb="office_quiet"),
    dict(to=10, reason="scene/character change: alone behind the locked office door Amjad calls on a secret phone from the bottom of his drawer", chars=["amjad"], loc="amjad_office",
         visual="Officer Amjad alone at his desk, half-standing and hunched forward, pressing a plain old black mobile phone to his ear with one hand, the other hand braced on the desk beside the pulled-open drawer; his face tense, breath short, eyes darting towards the shut door behind him; thin stripes of light from the blinds across his face and uniform; the phone has no visible screen",
         camera="medium close-up, eye level, Amjad's face centred in the upper half, the desk top and open drawer as the lower third",
         amb="office_quiet", sens="other", safe="the secret phone is a plain old black phone held to the ear; nothing on it is readable"),
    dict(to=14, reason="scene change: Shahid walks out of the police station, uneasy, suspicion burning", chars=["shahid"], loc="station_lane",
         visual="Shahid walking slowly out of the plain wooden door of the whitewashed police station into the sandy lane, looking back over his shoulder at the building with narrowed troubled eyes, his jaw tight, one hand on the strap of a canvas shoulder bag; the station behind him quiet, no signs, no lettering",
         camera="medium shot, eye level, Shahid's face in the upper half, the bright empty sand of the lane as the lower third",
         amb="village_day"),
    dict(to=15, reason="scene change: at home Shahid opens last night's photo again on his monitor", chars=["shahid"], loc="shahid_room_day",
         visual="Shahid sitting at his desk leaning close to the big monitor, chin resting on his hand, eyes narrowed in deep concentration, his face lit by the cold screen glow and a slanting beam of daylight; the monitor, seen at an angle, shows a dark rainy photo of a man in a heavy coat standing among dark trees, no interface text; camera gear on the desk",
         camera="medium shot over the corner of the desk, Shahid's face centred in the upper half, the desk top with camera and lenses as the lower third",
         amb="home_day", transition="xfade"),
    dict(to=17, reason="detail image: the photo itself, focus on the broken iron piece at his feet and the old ruined wall", loc="photo",
         visual="full-frame view of the rainy night photograph: the lower half of a man in an old-fashioned heavy dark-brown thick wool long coat standing on wet sand, cropped at the chest so his head is out of frame, his boots sunk in puddles; at his feet an oddly shaped broken rusty iron piece like a twisted old bracket half buried in the sand; directly behind him a broken old coral-stone wall with a crumbling arched opening and black mould streaks; silver rain, tree shadows, a flash of lightning; a real man, nothing ghostly",
         camera="close detail shot, slightly high angle, the iron piece and wall in the middle and upper part, the wet ground as the lower third",
         amb="home_day", transition="dissolve", sens="other", safe="Ibrahim in the photo stays a real man in a coat, cropped below the face; no supernatural look"),
    dict(to=18, reason="return to Shahid at the monitor: he recognises the warehouses by the east harbour (reuse)", chars=["shahid"], loc="shahid_room_day",
         reuse="beat_005", amb="home_day", transition="dissolve", visual="(reuse of beat_005)"),
    dict(to=19, reason="scene change: at the old harbour warehouses Shahid finds fresh footprints and a small folded note", chars=["shahid"], loc="warehouses",
         visual="Shahid crouching in a sandy lane between the abandoned coral-stone warehouses, holding up a small folded scrap of plain paper with no visible writing that he has just pulled from a crack in the wall, examining it warily; in front of him a fresh line of footprints pressed into the damp sand leading into a dark open warehouse doorway; rusted iron scraps; the broken wall with the arched opening behind him",
         camera="medium wide, slightly high angle, Shahid in the upper half, the footprints in the sand as the lower third",
         amb="jetty_day", sens="other", safe="the meeting note is a folded blank-looking scrap; nothing readable"),
    dict(to=20, reason="character change: a strange-looking masked figure appears behind Shahid and warns him", chars=["masked_stranger", "shahid"], loc="warehouses",
         visual="the masked stranger standing in a dark warehouse doorway a few metres away, in his long loose black robe, black turban wrap and black face cloth, only his grime-smeared wary eyes visible, one hand raised with a pointing finger in a silent warning; in the soft-focus foreground Shahid seen from behind and to the side, frozen mid-turn; grey light, sagging wooden door, mould-streaked walls; no weapon, no fighting",
         camera="over-the-shoulder medium shot, the stranger centred and sharp in the upper half, Shahid blurred in the foreground, the sandy ground as the lower third",
         amb="abandoned_house", sens="violence", safe="the stranger only warns with a raised finger; no weapon, no contact"),
    dict(to=21, reason="action change: the stranger runs into the warehouses; Shahid chases at a distance and loses him", chars=["shahid", "masked_stranger"], loc="warehouses",
         visual="a long narrow sandy lane between the abandoned warehouses: far ahead the dark figure of the masked stranger in his black robe vanishing around a crumbling corner, only the flutter of the black cloth visible; Shahid running after him in the middle distance, seen from behind and slightly to the side, his arm outstretched; dust kicked up from the sand; collapsing rusted roofs, deep shadows",
         camera="wide shot down the lane, eye level, the figures in the upper-middle, the empty sand and footprints as the lower third",
         amb="abandoned_house", sens="violence", safe="a chase at a distance only; no contact, no fighting"),
    dict(to=22, reason="action/character change: Shahid finds the dropped silicone mask as Amjad and a police team arrive", chars=["shahid", "amjad"], loc="warehouses",
         visual=f"Shahid crouching in the sand at the corner where the stranger vanished, staring in astonishment at {MASK}, lifting it carefully from the sand with both hands; at the far end of the lane behind him Officer Amjad striding into view with {COPS}, small and approaching",
         camera="medium wide, eye level, Shahid and the mask in the upper half, Amjad and the officers small in the background, the sand as the lower third",
         amb="jetty_day", sens="other", safe="the mask is a soft rubbery film prop held in the hands, never skin; police carry nothing"),
    dict(to=24, reason="dialogue: Amjad orders his officers to seal the area, then turns his warning eyes on Shahid (Amjad speaking)", chars=["amjad", "shahid"], loc="warehouses",
         visual=f"Officer Amjad standing in the warehouse lane, one arm stretched out pointing sharply as he barks an order, his face stern and commanding, eyes hard; behind him {COPS} spreading out along the warehouses; at the side Shahid stands smaller and softer, watching; grey overcast light",
         camera="medium shot, slightly low angle, Amjad's face centred and sharp in the upper half, the sandy lane as the lower third",
         amb="jetty_day", sens="violence", safe="sealing the area is shown only as a pointed order; no weapons, no tape with lettering"),
    dict(to=28, reason="action change: Amjad steps close and whispers a threat at Shahid's ear; Shahid freezes and understands (dialogue + reaction)", chars=["amjad", "shahid"], loc="warehouses",
         visual="close two-shot in the grey warehouse lane: Officer Amjad leaning in close beside Shahid's ear, seen in sharp profile, whispering with narrowed menacing eyes and a hard mouth under his salt-and-pepper moustache; Shahid facing the camera in three-quarter view, frozen, eyes wide with dawning fear, leaning slightly away; no touching of weapons, no handcuffs; mould-streaked wall behind them",
         camera="medium close-up two-shot, eye level, both faces in the upper half (Amjad left, Shahid right), the dark wall and sand as the lower third",
         amb="jetty_day", sens="violence", safe="the arrest is only a whispered threat; no handcuffs, no grabbing"),
    dict(to=30, reason="scene change: Shahid walks away afraid, feeling the weight of the bag with the mask on his shoulder", chars=["shahid"], loc="harbour_lane",
         visual="Shahid walking away along the sandy lane towards the camera, one hand gripping the strap of the canvas shoulder bag slung across his body as if it were heavy, glancing back over his shoulder with fear mixed with a new determined spark in his eyes; far behind him the old warehouses small and grey under a darkening sky",
         camera="medium shot, eye level, Shahid's face in the upper half, the sandy lane as the lower third",
         amb="village_day"),
    dict(to=31, reason="scene/time change: evening at home, door locked, Shahid takes out the silicone mask under the desk lamp", chars=["shahid"], loc="shahid_room_night",
         visual=f"Shahid sitting at his desk under the hard warm cone of the angled desk lamp, holding {MASK} up into the light with both hands and studying it intently, his face lit from below, eyes narrowed; the canvas bag open beside him on the desk; the rest of the room in deep shadow, the locked door dark behind him",
         camera="medium close-up, eye level, Shahid's face and the mask in the upper half, the lit desk top as the lower third",
         amb="home_night", sens="other", safe="the mask is a soft rubbery film prop in his hands, never skin or a face"),
    dict(to=33, reason="detail image / emotional turning point: the tiny maker's mark inside the edge of the mask", loc="shahid_room_night",
         visual="extreme close-up under the warm desk lamp: two fingertips folding back the thin edge of a soft matte beige silicone prop mask, revealing on its inner side a tiny engraved abstract emblem, a small precise geometric symbol of a circle crossed by three fine lines, crisply pressed into the material; nothing else on it; a small magnifying glass at the edge of the frame; behind the hands only the dark empty room in deep shadow, the closed wooden shutters and the dark monitor, absolutely no other people anywhere in the room, only one man's two hands in the frame; shallow depth of field",
         camera="macro close-up, the emblem in the upper-middle, the lit desk top as the lower third",
         amb="home_night", hum=True, sens="other", safe="the 'fine letters' of the mark become an abstract geometric emblem with no letters or numbers"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Amjad got up from the table and stood looking out through the room's window. A storm was swirling in his mind.")
sh(2, "A secret that had lain buried for twenty years had come back to life through this young man's single photo. Turning around, Amjad laid his hand on Shahid's shoulder.",
   [("cloth_rustle", "ބާއްވައިލި", -22)], hum=True)
sh(3, "\"Shahid, this is not an ordinary matter. This is the beginning of a big secret connected even to national security.", speaker="amjad", crop="medium", focus=[31, 24])
sh(4, "From today on, the investigation of this matter is handed directly to me. But remember,", speaker="amjad", crop="tight", focus=[31, 24])
sh(5, "no one on the island — and not even another police officer — may know anything about this photo.", speaker="amjad", crop="full", focus=[31, 30])
sh(6, "This is a secret between you and me.\" There was a commanding tone in Amjad's voice. Shahid nodded.", crop="medium", focus=[70, 45])
sh(7, "Yet from Amjad's sudden decision and the colour that showed on his face, a seed of strange suspicion was planted in Shahid's heart.", crop="tight", focus=[70, 45])
sh(8, "As soon as Shahid left the room, Amjad hurriedly locked the door. And from the very bottom of his drawer he took a secret phone and called a number.",
   [("lock_click", "ތަޅުލިއޭ", -18), ("creak", "ވަތްގަނޑުގެ", -22)])
sh(9, "While the phone rang, his breath was quick. \"Hello... where are you?",
   [("phone_buzz", "ރިންގުވަމުން", -20), ("breath_heavy", "ނޭވާ", -22)], hum=True, speaker="amjad")
sh(10, "You've been seen! Your face got into a camera's lens... Leave that place right now!\"", hum=True, speaker="amjad")
sh(11, "Amjad said it secretly, through gritted teeth. Shahid, coming out of the police station, had a heart full of unease.",
   [("footsteps_pavement", "ނުކުތް", -22)])
sh(12, "The sudden change seen on Officer Amjad's face, and the order to keep the matter secret, were like fuel thrown onto the fire of suspicion kindling in his heart.")
sh(13, "Was saying that no one must know meant for the safety of the investigation? Or was it a trick to hide something else?")
sh(14, "Shahid's mind kept churning with these questions. He decided to get to the bottom of this on his own, without the police's help.")
sh(15, "He came back home and opened last night's photo again. This time his gaze did not stop on Ibrahim Naseem's face —",
   [("keyboard_typing", "ހުޅުވައިލިއޭ", -22)])
sh(16, "but on the broken iron piece lying at his feet, and the old, ruined wall that could be seen behind him.")
sh(17, "Since Shahid knows every corner of the island well and goes about photographing all kinds of places, he was sure the shape of that wall was not the lighthouse wall.")
sh(18, "Staring deeply at the photo, Shahid recognised it as the area of the old warehouses near the harbour on the island's east side.")
sh(19, "When he went to that area and looked, he found fresh footprints and a small note hinting at a meeting.",
   [("footsteps_sand", "ސަރަހައްދަށް", -22), ("paper_shuffle", "ނޯޓެއް", -20)])
sh(20, "As he was about to hurry out of the place, suddenly a strange-looking man appeared behind him, and he was gripped by fear.",
   [("gasp", "ފެނި", -20), ("heartbeat", "ބިރުވެރިކަމެއްގެ", -20)], hum=True, focus=[52, 30])
sh(21, "The man in front of Shahid gave a warning, then suddenly ran off into the warehouses. Shahid ran after him, but the man had vanished.",
   [("footsteps_sand", "ދުއްވައިގަތް", -18), ("footsteps_sand", "ދުވެފައި", -20)], hum=True)
sh(22, "In that area Shahid found a mask used to change one's appearance. At that moment Officer Amjad arrived with a police team, and finding Shahid there, questioned him and showed his displeasure.",
   [("footsteps_sand", "ޓީމަކާއެކު", -20)])
sh(23, "Amjad at once ordered his officers: \"Seal off the whole area! Nobody is to leave this place!\"", speaker="amjad", crop="medium", focus=[52, 33])
sh(24, "But when Amjad turned towards Shahid, there was a strange colour of warning in his eyes.", hum=True, crop="tight", focus=[52, 33])
sh(25, "Amjad stepped about two paces forward and said softly, close to Shahid's ear: \"Shahid, didn't I tell you",
   [("footsteps_sand", "ފިޔަވަޅެއްވަރު", -22)], speaker="amjad", crop="medium", focus=[38, 30])
sh(26, "this is no business of yours? Today you got away. Next time I see you here, I'll have to arrest you.\"", hum=True, speaker="amjad", crop="tight", focus=[38, 30])
sh(27, "Shahid stepped back. From those words of Amjad's he was certain: Amjad isn't trying to find Ibrahim. He is trying to hide Ibrahim!",
   [("footsteps_sand", "ޖެހިލި", -24)], hum=True, crop="medium", focus=[60, 33])
sh(28, "Or to shut Ibrahim's mouth. Or worse — to shut Shahid's mouth too. Officer Amjad's strange words of warning seemed to leave Shahid's ears ringing.",
   [("heartbeat", "ބައްވެފައި", -22)], hum=True, crop="tight", focus=[60, 33])
sh(29, "He set off walking away from the police area with a frightened heart. Yet, as he felt the weight of the bag slung on his shoulder, a new excitement rose in a corner of his heart.",
   [("footsteps_sand", "ހިނގައިގަތީ", -22), ("cloth_rustle", "ދަބަހުގެ", -24)])
sh(30, "Inside that bag lay the first big piece of evidence of a great truth hidden from the whole island: the secret mask Ibrahim Naseem had dropped.")
sh(31, "After coming home and locking his room door, Shahid quickly took the silicone mask out of the bag. Bringing it under the strong light of the lamp on the desk, he began to study it very carefully.",
   [("lock_click", "ތަޅުލުމަށްފަހު", -18), ("cloth_rustle", "ދަބަހުން", -22)])
sh(32, "It was no ordinary mask. Near the edge on its inside, a mark had been stamped in very fine letters.", hum=True)
sh(33, "It is a mark of the kind used only by those making high-grade items, like the ones used in films or by foreign secret spy agencies for special missions. How did Ibrahim Naseem get such a thing? Shahid asked himself.",
   hum=True)
SHOTS = S

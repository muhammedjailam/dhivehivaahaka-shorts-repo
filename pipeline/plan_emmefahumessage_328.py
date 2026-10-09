"""Beat/shot plan for Emme Fahu Message episode 328 (used by plan_beats.py).
The night of the police at the door. The accident is NEVER shown; no man touches Amaan."""

APT = "a small slightly old third-floor apartment in Hulhumalé, Maldives"
LOC = {
    "kitchen": f"the tiny kitchen of {APT} at night: pale wooden cabinets, a narrow counter, a dripping tap over a small sink, a small window streaked with heavy rain, tiled floor",
    "sitting": f"the small sitting room of {APT} at night: a worn grey sofa with a crumpled cream throw blanket, a low wooden coffee table, framed blurry photos on the walls, a glass balcony door streaked with rain, a single warm floor lamp, an analog wall clock with a plain face and no numerals",
    "bedroom": f"the couple's small bedroom in {APT} at night: a double bed with a plain wooden headboard and two white pillows, a bedside table with a small warm lamp, an analog wall clock with a plain face and no numerals, a window streaked with rain, a wooden wardrobe",
    "hallway": f"the narrow entrance hallway of {APT} at night: a plain wooden front door with a simple lock, a small table with a key bowl by the door, framed blurry photos on the wall, tiled floor",
    "doorway": "the open front door of a third-floor apartment at night, seen from inside, looking out onto the wet concrete stair landing of an old apartment building, heavy rain pouring beyond the open stairwell railing, wet reflective floor, a weak bare stairwell bulb",
    "beach_memory": "a quiet white-sand beach on a honeymoon at sunset, a calm turquoise sea, a warm orange sky",
    "door_memory": f"the entrance hallway of {APT} on a bright morning, the front door open, sunlight in the stairwell beyond",
    "flowers": f"the small sitting room of {APT} one week later at rainy dusk: white and pale-green flower bouquets in vases everywhere — on the dining table, beside the TV cabinet, on the windowsill — a worn grey sofa with cushions, grey rain on the window",
    "wardrobe": f"the couple's small bedroom in {APT} in the evening: a tall wooden wardrobe standing open with men's shirts hung neatly by colour and jackets on one side, an empty half of rail, a soft lamp",
    "tie_memory": f"the couple's bedroom in {APT} on a bright morning: a full-length mirror on the wardrobe door, sunlight through sheer curtains",
    "bedroom_late": f"the couple's small bedroom in {APT} late at night one week later: the double bed with a plain wooden headboard and two pillows, a bedside table, a dark window streaked with rain",
}
MOOD = {
    "kitchen": "late night, heavy rain and distant thunder outside, cold blue-grey light from the rainy window, one dim warm amber under-cabinet light, numb and heavy",
    "sitting": "late rainy night, a single warm amber floor lamp against cold blue-grey shadows, rain streaks glinting on the balcony glass, lonely tenderness and quiet worry",
    "bedroom": "near midnight, rainy night, the small warm bedside lamp the only light, deep blue shadows, rain on the window, lonely longing",
    "hallway": "past midnight, rainy night, dim warm hallway light, cold blue shadows, hope tangled with exhaustion",
    "doorway": "past midnight, pouring rain, the cold weak light of a bare stairwell bulb on wet concrete, warm amber light spilling from the apartment behind, ominous stillness",
    "beach_memory": "soft hazy golden dreamlike memory glow, warm sunset light, gentle sea breeze, carefree joy",
    "door_memory": "soft hazy golden dreamlike memory glow, bright warm morning sunlight, tender everyday happiness",
    "flowers": "rainy grey dusk, soft grey-blue light from the window, a few warm lamps lit, the room quiet and heavy with mourning, the flowers pale and luminous",
    "wardrobe": "evening, rain outside, soft warm lamp light on the clothes, deep shadows, aching memory",
    "tie_memory": "soft hazy golden dreamlike memory glow, bright warm morning sunlight, playful affectionate happiness",
    "bedroom_late": "deep rainy night, no lamp, cold blue-grey light from the rain-streaked window, the faint cold glow of a phone, profound loneliness",
}

AMAAN_NIGHT = "Amaan in her loose long grey cardigan over her cream ankle-length dress, dusty-rose hijab fully covering her hair and neck"

BEATS = [
    dict(to=5, reason="episode opening: Amaan still sitting on the kitchen floor after Eethan left, the phone face down on the counter", chars=["amaan"], loc="kitchen",
         visual="Amaan sitting on the kitchen floor with her back against the lower cabinets, knees drawn up, arms around her knees, her cream dress and dusty-rose hijab, swollen eyes staring up at the counter above her where her phone lies face down at the edge; rain streaming down the small dark window; numb, lost in thought",
         camera="medium shot from slightly above, her face in the upper half, the tiled floor as the calm lower third", amb="apartment_rain_night"),
    dict(to=8, reason="action and location change: she gets up and wanders into the sitting room, sees the blanket they shared", chars=["amaan"], loc="sitting",
         visual="Amaan walking slowly into the dim sitting room, one hand resting on the back of the sofa for support, her face tired and puffy-eyed, looking down at the crumpled cream throw blanket still lying across the sofa where two people sat last night; the floor lamp casting a warm pool of light",
         camera="medium wide, eye level, the floor and rug as the lower third", amb="apartment_rain_night"),
    dict(to=12, reason="action change: she picks up Eethan's reading glasses from the coffee table", chars=["amaan"], loc="sitting",
         visual="Amaan standing by the low coffee table holding a pair of men's dark-framed reading glasses carefully in both hands, a faint sad smile; on the table a closed novel with a plain blank cover; a vermilion-red coffee mug resting on the sofa arm; an analog wall clock with no numerals in the soft background",
         camera="medium close-up, eye level, the coffee table top as the lower third", amb="apartment_rain_night"),
    dict(to=17, reason="action change: she sits with her phone, sends 'I'm sorry' and waits for a reply that never comes", chars=["amaan"], loc="sitting",
         visual="Amaan sitting on the edge of the sofa, holding her phone in both hands, the soft cold glow of the screen on her anxious face, eyes fixed on it, waiting; the screen faces her, only a glow visible to us; the rain-streaked balcony door dark behind her",
         camera="medium shot, slightly low eye level, the coffee table top as the lower third", amb="apartment_rain_night"),
    dict(to=21, reason="detail change: scrolling up through thousands of their messages, smiling through tears", chars=["amaan"], loc="sitting",
         visual="close-up over Amaan's shoulder of her phone held in her hand: a soft glowing screen with blurred rounded chat bubbles and tiny blurred photo thumbnails scrolling past, nothing readable; in the upper part of the frame her face in soft focus, tears in her eyes and a small trembling smile",
         camera="over-the-shoulder close-up, her face upper third, the phone in the middle, her lap in soft shadow below", amb="apartment_rain_night",
         sens="other", safe="phone screen shown only as blurred bubbles and glow; no readable text"),
    dict(to=23, reason="memory: the honeymoon beach photo on his contact comes alive", chars=["amaan", "eethan"], loc="beach_memory",
         visual="a joyful honeymoon moment on a sunset beach: Amaan laughing with her dusty-rose hijab fully covering her hair and neck, its loose end fluttering in the sea breeze, sunglasses sitting crooked on her face; Eethan beside her in a light shirt and dark trousers, grinning at her; they stand side by side, not touching, the orange sun low over the sea",
         camera="medium shot, eye level, their faces in the upper half, wet sand and gentle surf as the lower third", amb="memory",
         transition="dissolve", sens="clothing",
         safe="narration says her hair was blowing in the wind: shown instead as her hijab's loose end fluttering, hair fully covered"),
    dict(to=25, reuse="beat_004", reason="return to the present: unbearable silence, 11:30 and he is not home", loc="sitting",
         visual="(reuse)", amb="apartment_rain_night", transition="dissolve"),
    dict(to=29, reason="scene change: she goes to bed, his side empty, hugging his pillow", chars=["amaan"], loc="bedroom",
         visual=f"{AMAAN_NIGHT}, sitting up against the wooden headboard on her own side, legs under a light blanket, hugging a white pillow to her chest with both arms, her cheek resting on it, eyes red and longing; the other side of the double mattress empty and smooth; the small bedside lamp glowing warm",
         camera="medium shot, eye level, her face in the upper third, the smooth blanket as a calm lower third", amb="apartment_rain_night",
         sens="other", safe="in bed she is shown sitting up against the headboard, fully dressed with hijab, never lying down"),
    dict(to=31, reason="turning point: loud knocking, she looks at the clock — 12:47", chars=["amaan"], loc="bedroom",
         visual=f"close-up of {AMAAN_NIGHT}, sitting bolt upright against the headboard, eyes suddenly wide open, turning her head towards the bedroom door, a flicker of hopeful relief on her face; beside her on the wall an analog clock with a plain face and no numerals, its hands near a quarter to one; lamp light, deep shadows",
         camera="close-up, eye level, her face in the upper half, the pillow and blanket soft below", amb="apartment_rain_night"),
    dict(to=34, reason="action and location change: she hurries out to the front door, straightening her hijab", chars=["amaan"], loc="hallway",
         visual=f"{AMAAN_NIGHT}, hurrying down the narrow hallway towards the closed front door, one hand straightening the edge of her hijab, the other reaching for the lock, a tired hopeful smile, her eyes still red",
         camera="medium wide from behind and slightly to the side, the tiled floor as the lower third", amb="apartment_rain_night"),
    dict(to=37, reason="characters change: not Eethan — two uniformed police officers at the door in the pouring rain", chars=["amaan", "officer_raain", "officer_young"], loc="doorway",
         visual="Amaan seen from behind, standing in the open doorway with one hand still on the door; outside on the wet stair landing stand two police officers in dark-navy uniforms and peaked caps, rain dripping from their caps and shoulders: an older officer with a greying moustache in front, solemn, and a young clean-shaven officer just behind him; rain pours beyond the stairwell railing; nobody moves",
         camera="over-the-shoulder medium wide, the officers' faces in the upper half, the wet reflective floor as the lower third", amb="rain_night"),
    dict(to=40, reason="focus change: Officer Raain takes off his cap; his face alone stops her heart", chars=["officer_raain", "officer_young", "amaan"], loc="doorway",
         visual="the older officer with the greying moustache holding his removed peaked cap against his chest with both hands, his weary kind eyes full of sorrow, speaking softly; the young officer half a step behind him looking pale; at the near edge of the frame Amaan's dusty-rose hijab and shoulder in soft focus, rain dripping in the stairwell behind them",
         camera="medium close-up over Amaan's shoulder, the officer's face in the upper third, wet floor below", amb="rain_night"),
    dict(to=44, reason="location and action change: the officers step inside, close the door and deliver the news", chars=["amaan", "officer_raain", "officer_young"], loc="hallway",
         visual=f"inside the narrow hallway with the front door now closed: {AMAAN_NIGHT}, standing frozen, both hands pressed to her mouth, eyes wide in disbelief; facing her at a respectful distance of two steps the older officer holding his cap in his hands, speaking gently with a grave face, the young officer beside the door; rain water dripping from their uniforms onto the tiles",
         camera="medium wide two-sided composition, eye level, faces in the upper half, the tiled floor as the lower third", amb="apartment_rain_night",
         sens="violence", safe="the fatal car accident is only spoken about; never shown — only the officers' grave faces and Amaan's shock"),
    dict(to=46, reason="emotional framing change: close-up of Amaan's denial — 'he just went for a drive, he's coming home'", chars=["amaan"], loc="hallway",
         visual=f"close-up of {AMAAN_NIGHT}, shaking her head slowly, a broken exhausted disbelieving smile on her trembling lips, eyes glistening with tears; behind her the hallway falls into soft dark blur",
         camera="close-up, eye level, face in the upper half, her clasped hands soft below", amb="apartment_rain_night"),
    dict(to=49, reason="focus change: the young officer looks down; she searches their faces for a mistake", chars=["officer_young", "officer_raain", "amaan"], loc="hallway",
         visual="seen from behind Amaan's shoulder in soft focus: the two police officers standing two steps away by the closed door; the young clean-shaven officer has lowered his head and looks at the floor, distressed; the older officer with the greying moustache holds his cap at his side and meets her gaze in heavy silence",
         camera="over-the-shoulder medium shot, the officers' faces in the upper half, the tiled floor as the lower third", amb="apartment_rain_night"),
    dict(to=52, reason="action change: her knees give way and she sinks to the floor", chars=["amaan", "officer_raain", "officer_young"], loc="hallway",
         visual=f"{AMAAN_NIGHT}, sinking down onto her knees on the hallway floor, one hand pressed to her chest, the other clutching her own cardigan sleeve, mouth open, gasping for breath, alone in the left half of the frame; the older officer with the greying moustache stands bareheaded a full step back on the right, his peaked cap held in one hand at his side, his other open hand half-raised in the air in concern, a clear gap of empty floor between him and her — he does not touch her; the young officer behind him by the door, stricken",
         camera="medium wide, slightly high angle, faces in the upper two-thirds, the tiled floor as the lower third", amb="apartment_rain_night",
         sens="other", safe="narration says the officer caught her and she gripped his forearm: shown instead as her sinking to her knees with the officers a step away, no man touches her"),
    dict(to=54, reason="framing change: close-up of her sobs — 'I didn't say goodbye, I didn't tell him I love him'", chars=["amaan"], loc="hallway",
         visual=f"close-up of {AMAAN_NIGHT}, kneeling on the floor, her face crumpled in grief, tears streaming down her cheeks, one hand over her mouth, eyes squeezed shut; dim warm hallway light, deep shadows",
         camera="close-up, slightly high angle, face in the upper half, her knees and the floor in soft shadow below", amb="apartment_rain_night"),
    dict(to=55, reason="memory: the apartment that same morning, Eethan smiling at the door before leaving", chars=["eethan"], loc="door_memory",
         visual="Eethan standing in the open front doorway on a bright morning, in a dark-olive zip-up rain jacket over his navy t-shirt and dark jeans, turning back to look into the apartment with a warm affectionate smile, keys in his hand, sunlight around him",
         camera="medium shot, eye level, his face in the upper third, the sunlit floor as the lower third", amb="memory",
         transition="dissolve", sens="intimacy", safe="the daily forehead kiss is omitted: shown only as Eethan smiling back at the door"),
    dict(to=58, reason="time and character change: an hour later the officers have left, her sister Luha arrives and offers water", chars=["amaan", "luha"], loc="sitting",
         visual=f"{AMAAN_NIGHT}, curled up in the corner of the sofa, drained and cried out, staring at nothing; her elder sister Luha in a deep-teal dress and black hijab sitting close beside her, holding out a glass of water towards her with gentle worried eyes; Amaan does not take it",
         camera="medium shot, eye level, faces in the upper half, the coffee table top as the lower third", amb="apartment_rain_night",
         transition="dissolve"),
    dict(to=63, reason="detail change: the medicine reminder and, beneath it, Eethan's unheard voice message; her thumb hovers, she turns the screen off", chars=["amaan", "luha"], loc="sitting",
         visual="close-up of Amaan's hands holding her phone in her lap, the screen a soft cold glow with two small blurred notification bars, nothing readable, her thumb hovering just above it; above, her face in soft focus with a single tear rolling down her cheek; at the edge of the frame Luha's deep-teal sleeve and hand resting near her",
         camera="close-up, slightly high angle, her face in the upper third, her hands and the phone in the middle, the cardigan in soft shadow below", amb="apartment_rain_night",
         sens="other", safe="phone notifications shown as blurred glowing bars; no readable text or time"),
    dict(to=66, reason="time jump: one week later the apartment overflows with white and pale-green flowers", loc="flowers",
         visual="the small sitting room filled with white and pale-green flower bouquets — lilies, roses and chrysanthemums in white and soft green — in vases on the dining table, beside the TV cabinet and on the windowsill where a man used to drink his morning coffee; cushions on the sofa; grey rain light on the window; no people",
         camera="wide shot, eye level, the flowers and window in the upper two-thirds, the floor as a calm lower third", amb="apartment_rain_day",
         transition="black", sens="other", safe="the condolence visits and funeral are suggested only by the flowers"),
    dict(to=70, reason="characters change: Luha asks if she has eaten, sits beside her and holds her hand", chars=["amaan", "luha"], loc="flowers",
         visual=f"{AMAAN_NIGHT}, sitting on the sofa among the white and pale-green flowers, pale and hollow-eyed; Luha in her deep-teal dress and black hijab sitting beside her, holding Amaan's hand in both of hers on Amaan's knee, looking at her with tender concern; Amaan gazing towards the bedroom door",
         camera="medium shot, eye level, faces in the upper half, the coffee table with a vase as the lower third", amb="apartment_rain_day"),
    dict(to=74, reason="location and action change: she stands before Eethan's wardrobe, still exactly as he kept it", chars=["amaan"], loc="wardrobe",
         visual=f"{AMAAN_NIGHT}, standing still in front of the open wooden wardrobe, one hand lightly touching the sleeves of men's shirts hung neatly by colour, jackets on one side, an empty half of the rail kept for her; her face in profile, eyes closed for a moment as if breathing in a familiar scent",
         camera="medium shot from the side, eye level, her face in the upper third, the wardrobe floor in soft shadow below", amb="apartment_quiet_night"),
    dict(to=75, reason="action change: she takes out the navy suit he wore to her sister's wedding", chars=["amaan"], loc="wardrobe",
         visual=f"{AMAAN_NIGHT}, standing at the open wardrobe holding a man's navy suit jacket on its hanger pressed to her chest with both arms, her chin resting on its shoulder, eyes wet and distant; no other people",
         camera="medium close-up, eye level, her face in the upper third, the dark jacket filling the middle, soft shadow below", amb="apartment_quiet_night",
         sens="other", safe="the narration says the suit is for the funeral: no funeral imagery, only Amaan holding the suit at the wardrobe"),
    dict(to=78, reason="memory (dissolve): the morning of the wedding, Eethan fixing his crooked tie at the mirror", chars=["eethan", "amaan"], loc="tie_memory",
         visual="seen from the mirror's point of view (no mirror visible in the frame): Eethan facing the camera in a navy suit, white shirt and a tie, fiddling with his crooked tie and grinning playfully; behind him in the background Amaan in her cream dress and dusty-rose hijab leaning in the bedroom doorway a few steps away, laughing with her hand near her mouth; only these two people, each appears once",
         camera="medium wide, eye level, faces in the upper half, the sunlit floor as the lower third", amb="memory",
         transition="dissolve", sens="intimacy",
         safe="the cheek kiss after straightening the tie is omitted: only the playful moment at the mirror, Amaan at a distance in the doorway"),
    dict(to=80, reuse="beat_024", reason="return from the memory: she presses the suit to her chest, wanting to see him in it once more", loc="wardrobe",
         visual="(reuse)", amb="apartment_quiet_night", transition="dissolve"),
    dict(to=82, reason="action and character change: she sinks to the floor; later Luha finds her still holding the suit", chars=["amaan", "luha"], loc="wardrobe",
         visual=f"{AMAAN_NIGHT}, sitting on the bedroom floor in front of the open wardrobe, the navy suit jacket held in her arms against her chest, head bowed; in the doorway behind her Luha in her deep-teal dress and black hijab stands quietly watching with sorrowful eyes, one hand on the door frame, not intervening",
         camera="medium wide, eye level, faces in the upper two-thirds, the wooden floor as the lower third", amb="apartment_quiet_night"),
    dict(to=85, reason="time change: that night she sleeps on his side of the bed, hugging his pillow", chars=["amaan"], loc="bedroom_late",
         visual=f"{AMAAN_NIGHT}, sitting up against the headboard on his side of the double mattress, hugging his white pillow tightly to her chest, her eyes lifted towards the ceiling; rain drops sliding down the dark window beside her; on the small bedside table her phone lies face down; a plain bare dark wall behind the headboard with no pictures, no visions, no other figures; no lamp, only cold blue rain light",
         camera="medium shot, eye level, her face in the upper third, the blanket as a calm lower third", amb="apartment_rain_night",
         transition="black", sens="other", safe="in bed she is shown sitting up against the headboard, fully dressed with hijab, never lying down"),
    dict(to=90, reason="action change: she reaches for the phone, the screen lights up, her thumb hovers over the voice message", chars=["amaan"], loc="bedroom_late",
         visual="close-up of Amaan's hand reaching to the bedside table, her phone screen lit with a soft cold glow and a small blurred waveform shape, nothing readable, her thumb hovering just above it; her face above in soft focus lit by the glow, eyes wide and wet, holding her breath",
         camera="close-up, eye level, her face in the upper third, the hand and phone in the middle, the dark bedside table below", amb="apartment_rain_night",
         sens="other", safe="the notification is shown only as a glowing screen with a blurred waveform; no readable text"),
    dict(to=92, reason="closing image: she turns the phone face down — 'Tomorrow' — and falls asleep for the first time without his good night", chars=["amaan"], loc="bedroom_late",
         visual="the dark bedroom from the side: on the bedside table in the foreground the phone lying face down with a faint glow leaking from its edges; behind it, softly out of focus, Amaan in her grey cardigan and dusty-rose hijab sitting against the headboard with the pillow in her arms and her eyes closed; rain-streaked window glowing faint blue",
         camera="close-up of the bedside table in the foreground, eye level, Amaan soft in the upper background, the table top as the lower third", amb="apartment_rain_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Amaan had no idea how long she had been sitting on the kitchen floor. Outside, the falling rain had grown heavier.")
sh(2, "The sound of drops hitting the windows and distant thunder came together. Amaan's phone still lay on the counter.",
   [("thunder", "ގުގުރައިލާ", -18)])
sh(3, "Face down. Every now and then she glanced towards the phone. Amaan kept thinking about Eethan's voice message.")
sh(4, "She knew she would have to listen to it. In her heart Amaan wondered what Eethan had said in that message. \"I'm sorry.")
sh(5, "Let's go home and talk about it, okay? I love you very much, Amaan.\" Whatever Eethan had said,")
sh(6, "Amaan was not yet ready to hear it. After rubbing her swollen eyes, she lifted her body to get up from where she sat.")
sh(7, "Her knees ached from sitting on the floor for so long. With no purpose at all, she began to wander around the apartment.")
sh(8, "In the sitting room the blanket the two of them had shared last night while watching a film was still lying there.")
sh(9, "Eethan's coffee mug sat on the arm of the sofa. Beside the novel he had started reading, his glasses lay on the coffee table. Amaan picked up the glasses.")
sh(10, "\"If they lie here they'll get scratched,\" she said to herself. The words left her lips before she realised there was no one to hear them.")
sh(11, "She smiled a little. Amaan put the glasses back exactly where she had taken them from, making sure they lay just as before.")
sh(12, "Eethan could not stand other people touching his things. The clock had struck ten at night.",
   [("clock_tick", "ގަޑިން", -22)])
sh(13, "Amaan picked up her phone and opened Eethan's chat. 'I'm sorry,' she wrote, and sent Eethan the message.")
sh(14, "After sending it she stood staring at the screen. In the corner below the message only a single tiny grey tick showed.")
sh(15, "Amaan waited for Eethan's reply. But there was no news at all. Once again Amaan sent another message. 'Please, I'm begging you,")
sh(16, "come home soon.' No reply came. The message was not even delivered. A knot of pain gripped Amaan's stomach.")
sh(17, "She kept telling herself that Eethan was still driving. Maybe his phone's battery had died.")
sh(18, "Or he had stopped somewhere to clear his head. She opened their chat and began scrolling up.")
sh(19, "Thousands of messages. Photos. Shopping lists. Heart emojis. Arguments that ended in forgiveness.")
sh(20, "Funny little jokes no one else would understand. Ordinary messages sent in the middle of everyday life. \"I miss you so much.\"")
sh(21, "\"Bring a carton of milk, will you.\" \"The sunset today is so beautiful.\" \"I love you so much.\" Amaan smiled through the tears gathered in her eyes.",
   hum=True)
sh(22, "And she touched the photo on Eethan's number. It was a photo taken on the beach on their honeymoon.")
sh(23, "Her hair was spread out in the wind. The sunglasses on her face sat crooked.")
sh(24, "Suddenly an unbearable silence settled over the apartment. Even at half past eleven, Eethan had not come home.")
sh(25, "Amaan began to wonder whether she had blown things out of proportion herself. Eethan was always the kind of person who needed time after an argument.")
sh(26, "But he would come home. Amaan put on her nightclothes, got into bed, and left the lamp beside the bed on.")
sh(27, "The side where Eethan slept lay empty. His pillow smelled of the cologne he wore. Amaan picked up that pillow and hugged it to her chest.",
   [("cloth_rustle", "ބޮނޑިކޮށްލިއެވެ", -24)])
sh(28, "\"I want to apologise properly. I'll make everything right,\" she whispered into the empty room.", hum=True)
sh(29, "She closed her eyes. But sleep did not come. At that moment there was a very loud knocking on the apartment door. Amaan's eyes flew open.",
   [("knock", "ޓަކިޖެހި", -14), ("gasp", "ހުޅުވުނެވެ", -22)])
sh(30, "She looked at the clock on the bedroom wall. It was 12:47 at night. The knocking came again, louder than before this time. \"Eethan?\"",
   [("clock_tick", "ގަޑިއަށް", -22), ("knock", "ޓަކިޖެހި", -12)])
sh(31, "Amaan was worried. And at the same time a great relief came over her. Eethan had come home.")
sh(32, "Straightening her hair as she walked towards the door, she hurried out of the room.",
   [("footsteps_pavement", "ނުކުތެވެ", -24)])
sh(33, "\"Eethan, I'm sorry. I was so hurt at that moment that I found it hard to let go.\"")
sh(34, "Amaan called out with a weary smile. No answer came from Eethan. Amaan rushed over and unlocked the door.",
   [("lock_click", "ތަޅުހުޅުވާލިއެވެ", -18)])
sh(35, "Contrary to what she expected, the one standing on the other side of the door was not Eethan. In front of her stood two police officers in uniform.",
   [("door_open", "ދޮރުގެ", -20)])
sh(36, "It was still raining heavily. The entrance of the apartment building lay soaking wet.")
sh(37, "For a brief moment Amaan just stood staring at them, not knowing why they would be there. \"Are you Eethan's wife?\"")
sh(38, "One of the officers took the cap off his head and asked. The look on his face alone was enough to make Amaan's heart stop. \"Yes...\"",
   [("cloth_rustle", "ތޮފި", -24)])
sh(39, "\"My name is Officer Raain. May we come inside?\" His voice was soft and gentle.")
sh(40, "The bewilderment in Amaan's heart slowly turned to fear. \"Eethan... is Eethan okay?\"",
   [("heartbeat", "ބިރުވެރިކަމަށް", -22)])
sh(41, "Neither of the two officers answered at once. Instead they stepped inside and gently closed the door.",
   [("door_close", "ލައްޕާލިއެވެ", -20)])
sh(42, "Officer Raain glanced at his partner and then looked at Amaan again. \"I am so sorry to have to tell you this.")
sh(43, "Your husband was in a serious accident tonight.\" Every sound in the room stopped. The sound of the rain.",
   hum=True)
sh(44, "The ticking of the clock's hand. The sound of the breathing of the people there. Everything stopped at once. \"No.\" Amaan shook her head.",
   [("clock_tick", "ގަޑީގެ", -24), ("breath", "ނޭވާގެ", -24)], hum=True)
sh(45, "\"Because the rain was so heavy, he lost control of the car.\" \"No..\" The word left Amaan's mouth in a faint whisper.")
sh(46, "She smiled wearily. Unable to believe it, she kept shaking her head. \"He only went for a drive. He's on his way home.\"")
sh(47, "Amaan's voice trembled. \"I'm so sorry.\" The younger officer, distressed, lowered his head.",
   [("sob_breath", "ތުރުތުރުއެޅިއެވެ", -24)])
sh(48, "Amaan looked from one officer's face to the other, waiting — for the moment they would say this was a mistake.")
sh(49, "She wanted to hear that the man driving the car they found was some other Eethan. But there was only silence. Amaan understood.")
sh(50, "Her small heart shattered. \"No.. No!\" she cried out loud. Her knees gave way and she was falling to the floor.",
   [("cloth_rustle", "ތިރިވެ", -20)], hum=True)
sh(51, "Before she hit the floor the older officer caught hold of her. She could hardly breathe. Every breath was a struggle; her chest heaved.",
   [("breath_heavy", "ނޭވާލާން", -22)])
sh(52, "As if refusing to accept the truth, she gripped the officer's forearm tightly. \"I didn't even...\"")
sh(53, "The words caught in her throat. \"I didn't say goodbye.\" Her voice broke in places through the tears. \"I...\"",
   [("sob_breath", "ކަރުނައިގެ", -22)], hum=True)
sh(54, "Her voice cut off. \"I didn't tell him I love him.\" The whole apartment echoed with the sound of Amaan's sobbing.",
   [("sob_breath", "ރޮއިގަތުމުގެ", -20)], hum=True)
sh(55, "This was the apartment that, that very morning, had been full of laughter and teasing. The apartment where every day, before going out, Eethan kissed her forehead.")
sh(56, "But not a trace of that happiness could be seen there now. An hour later the officers who had brought the news left.",
   [("door_close", "ދިޔައެވެ", -22)])
sh(57, "When Amaan's elder sister Luha arrived. By then Amaan sat on the sofa, quietly hiccupping with sobs, as though she had cried until her tears ran dry.",
   [("door_open", "އައުމުންނެވެ", -22)])
sh(58, "Luha put a glass of water in Amaan's hand. Amaan looked at it. But she had no thought of drinking from it. At that moment her phone vibrated.",
   [("phone_buzz", "ވައިބްރޭޓްވިއެވެ", -16)])
sh(59, "She immediately looked down. It was a reminder that it was time to take her medicine.")
sh(60, "And right below that message, a single notification was still waiting on the screen. A message that had come to the phone at 7:18.")
sh(61, "Amaan sat staring at the notification. Her thumb stopped above it. Then she slowly switched off the phone's screen.")
sh(62, "\"If I hear his voice... I won't be able to bear it..\" A single tear rolled down Amaan's cheek.",
   [("sob_breath", "ކަރުނައިގެ", -24)], hum=True)
sh(63, "It was as if some part of her body kept telling her: if she listened to that message, Eethan would truly be gone from her. One week later.")
sh(64, "The flowers brought by family and friends who came to visit Amaan filled the house. The whole apartment was full of white and pale-green flowers.")
sh(65, "Eethan's two favourite colours. The sweet scent of the flowers had settled into the curtains and the sofa cushions.")
sh(66, "The flowers still stood where the people who brought them had placed them. On the dining table. Beside the TV.")
sh(67, "By the window where Eethan used to sit and drink his coffee in the morning. \"Have you eaten anything?\" Luha asked. Amaan shook her head to say no.")
sh(68, "\"Try and see if you can eat something,\" Luha said tenderly. \"I'll eat later.\" Since the police came to the house, Amaan had given everyone the same answer.")
sh(69, "That she would eat later. Luha came and sat beside Amaan and took her hand. For a while the two of them sat without a sound.",
   [("cloth_rustle", "އިށީނުމަށްފަހު", -24)])
sh(70, "\"I have to take Eethan's suit,\" Amaan said suddenly, looking towards the bedroom. \"Amaan. It's all right if you don't do that tonight.\"")
sh(71, "Luha squeezed Amaan's hand. \"I know.\" Even as she said it, she stood up. Eethan's wardrobe was still just as he kept it.",
   [("cloth_rustle", "ތެދުވިއެވެ", -24)])
sh(72, "The shirts were hung in order, separated by colour, while the jackets were pushed to one side. The other half had been set aside especially for Amaan, but")
sh(73, "she had never once used that space. Along with the scent of the cologne he wore, from among Eethan's clothes")
sh(74, "came the clean smell of washed laundry. Amaan paused in front of the wardrobe and stood there for a few seconds. Then,")
sh(75, "she took hold of the navy suit Eethan had worn to her sister's wedding.",
   [("cloth_rustle", "ހިފެހެއްޓިއެވެ", -22)])
sh(76, "The memory of that morning came over Amaan's mind: Eethan standing in front of the mirror trying to fix his tie, and her laughing in the bedroom doorway.")
sh(77, "\"You're doing it all wrong. The whole tie is crooked,\" Amaan said, laughing. \"This is the fashion now,\" Eethan replied. \"There, it's nice now.\"")
sh(78, "Amaan came over and fixed his tie for him, and kissed his cheek. \"Now?\" Eethan smiled, looking at Amaan's reflection in the mirror.")
sh(79, "That memory was a very ordinary memory. But the ache it raised in her heart was greater even than Eethan's funeral.", hum=True)
sh(80, "Amaan pressed the suit to her chest and held it tight. Even knowing it could never happen, she wanted to take the suit to Eethan,",
   [("cloth_rustle", "ޖައްސައި", -22)], hum=True)
sh(81, "and see him standing in it just once more. Suddenly Amaan came back to reality. She sat down on the floor.",
   [("cloth_rustle", "އިށީނެވެ", -20)])
sh(82, "A while later, when Luha found her, she was still sitting like that, holding on to the suit. Luha did not try to take the suit from her hands.")
sh(83, "That night she slept on Eethan's side of the bed. The room had gone cold. But his scent still drifted faintly from the pillow.")
sh(84, "As raindrops tapped softly on the window, she lay hugging that pillow tightly to her chest, staring at the ceiling.")
sh(85, "Her phone lay on the small table beside the bed. She knew what was waiting for her on that phone.")
sh(86, "Every day since the accident she had seen that notification. 1 new voice message from Eethan.")
sh(87, "She stretched her hand towards the phone. The screen lit up at once. Her thumb stopped above the message.")
sh(88, "For a moment, the way she would play the message came into her mind. She imagined how Eethan's voice would sound.")
sh(89, "Knowing that the message would hold something completely new — not the sounds of Eethan's memories recorded in her mind — Amaan's heart began to race.",
   [("heartbeat", "އަވަސްވެގެންދިޔައެވެ", -20)], hum=True)
sh(90, "Perhaps that was the reason she found it so hard to open the message. Amaan never wanted to accept that Eethan had said goodbye to the world.")
sh(91, "She could not do it. She turned the phone face down and laid it on the table. \"Tomorrow,\" she said softly.",
   [("soft_thud", "ޖަހައި", -24)])
sh(92, "Then she closed her eyes. And for the first time in the past nine years, she fell asleep without hearing Eethan's voice say 'good night'.",
   [("sigh", "ލައްޕައިލިއެވެ", -24)], hum=True)
SHOTS = S

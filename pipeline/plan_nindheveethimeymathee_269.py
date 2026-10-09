"""Beat/shot plan for Nindheveethimeymathee episode 269 (used by plan_beats.py).
PRESENT timeline. One night at the TV studio of "Tharinnaa Eku": Saba hides a mark under makeup, writer Lail is the
guest, their eyes lock; Lail leaves his card; Miya slips it into Saba's bag.
Rules: no bruise shown; NO touching between Lail and Saba (or Lail and Miya) - greetings are a hand on the heart and a
nod at arm's length; no readable text on the backdrop, the card or phones."""

STUDIO = "a modern television studio in Malé, Maldives"
LOC = {
    "set_empty": f"the empty talk-show set inside {STUDIO}: a large glossy red-and-gold backdrop panel with an ornamental swirl pattern and no letters at all, a red carpet laid on the floor in front of it, two sets of soft cushioned armchairs facing each other on either side of the carpet, big bright studio lights on stands from six sides and more lights hanging from the ceiling grid, three studio cameras on tripods",
    "floor": f"the dark working floor of {STUDIO} beside the glowing red-and-gold talk-show set: cables on the black floor, light stands, a monitor desk where crew members in black work, a plain grey door to the makeup room at one side",
    "makeup": f"a small makeup room next to {STUDIO}: a long dressing table with a big mirror framed by round warm bulbs, makeup brushes and palettes, a box of tissues, a handbag on the counter, a swivel chair, a plain grey door",
    "set_live": f"the red-and-gold talk-show set of {STUDIO} during a recording: the glossy red-and-gold ornamental backdrop with no letters, the red carpet, the soft cushioned armchairs, bright studio lights, a studio camera on a tripod and a boom of lights at the edges of the frame",
    "desk": "a writer's quiet desk by a dark window late at night: an open notebook covered in soft illegible scribble lines, a pen lying across it, a cold cup of tea, a few crumpled paper balls, rain streaks on the window glass and blurred city lights beyond",
}
MOOD = {
    "set_empty": "night, the set blazing with bright warm white and golden studio light, deep indigo darkness beyond the lights, glossy, expectant and grand",
    "floor": "night, bright warm spill light from the set against the deep blue-black shadows of the studio floor, quiet hurried bustle",
    "makeup": "night, warm amber glow of the mirror bulbs against cool blue shadows in the corners, intimate, fragile and heavy-hearted",
    "set_live": "night, bright warm studio key light on the faces, red and gold reflections, deep indigo darkness behind the cameras, charged and tender undercurrent",
    "desk": "late rainy night, a single small warm desk lamp against deep sapphire-blue darkness, rain on the glass, lonely aching longing",
}

BEATS = [
    dict(to=4, reason="episode opening: establishing the bright TV studio set of 'Tharinnaa Eku'", loc="set_empty",
         visual="the empty talk-show set seen from behind the studio cameras: the big glossy red-and-gold ornamental backdrop glowing in the centre with no lettering, the red carpet leading to two pairs of soft cushioned armchairs facing each other, bright lamps blazing from all sides and from the ceiling grid; no people",
         camera="wide establishing shot, slightly low angle, the backdrop and lights in the upper two-thirds, the dark studio floor as a calm lower third", amb="tv_studio",
         sens="other", safe="the show title on the backdrop is shown only as a red-and-gold ornamental pattern without letters"),
    dict(to=5, reason="character enters: Miya walks into the studio on a phone call", chars=["miya"], loc="floor",
         visual="Miya walking briskly across the dark studio floor with a phone held to her ear, raising her free hand in a quick wave to two crew members in black at a monitor desk, a cheerful busy smile, heading towards a grey door at the side; the red-and-gold set glowing behind her",
         camera="medium wide, eye level, the dark floor as the lower third", amb="tv_studio"),
    dict(to=8, reason="character change: Saba slips in unseen, head down, pretending to search her handbag", chars=["saba"], loc="floor",
         visual="Saba walking quickly along the edge of the dark studio floor with her head bowed, one hand rummaging in an open handbag on her arm, her face half hidden and tense, avoiding everyone's eyes; crew members in the background busy at the monitor desk with their backs turned; the grey makeup-room door just ahead of her",
         camera="medium shot, slightly from the side, the dark floor as the lower third", amb="tv_studio"),
    dict(to=11, reason="scene change: in the makeup room Saba checks the hidden mark at her temple and her eyes fill with tears", chars=["saba", "miya"], loc="makeup",
         visual="Saba standing close to the bulb-framed mirror, her face turned slightly to one side, two fingertips touching the edge of her pale-lavender hijab near her temple, her large eyes glistening with tears, a folded tissue in her other hand; her skin is smooth and evenly made up, no marks visible; in the soft background Miya stands with her back half turned, still talking on her phone",
         camera="medium close-up from the side of the mirror, Saba's face in the upper third, the dressing table top as the lower third", amb="tv_studio",
         sens="violence",
         safe="the hidden mark from the abuse is never shown: only her fingertips near her temple, perfect makeup and tears"),
    dict(to=15, reason="action change: Miya finishes her call, grabs Saba's hand and sees her tears", chars=["miya", "saba"], loc="makeup",
         visual="Miya, phone lowered in one hand, catching Saba's wrist with her other hand and looking at her with sudden worry; Saba, sitting on the swivel chair at the dressing table with a makeup brush in her hand, turning to Miya startled, tears gathering in her eyes; warm bulb light on both faces",
         camera="medium two-shot, eye level, the dressing table top as the lower third", amb="tv_studio"),
    dict(to=17, reason="emotional turning point: 'This is my fate' - Saba's bitter smile in the mirror", chars=["saba", "miya"], loc="makeup",
         visual="Saba sitting at the dressing table looking at her own face in the mirror with a bitter little smile, blinking away watery eyes; Miya standing behind her shoulder with her arms crossed, frowning, upset and protective",
         camera="medium shot from behind and beside the mirror, both faces in the upper half, the dressing table top as the lower third", amb="tv_studio"),
    dict(to=19, reason="character enters: the producer Zavee opens the door - the guest has arrived", chars=["zavee", "saba", "miya"], loc="makeup",
         visual="Zavee leaning in through the half-open grey door of the makeup room, headset around his neck, one hand on the door handle, a joking grin; Saba at the mirror turning towards him while dabbing her face with a powder puff, Miya beside her laughing at his joke",
         camera="medium wide, eye level, from inside the room towards the door, the floor as the lower third", amb="tv_studio"),
    dict(to=21, reason="scene and character change: the guest Lail arrives; Zavee greets him", chars=["lail", "zavee"], loc="floor",
         visual="Lail walking onto the studio floor, still chatting with a young male crew assistant in a black T-shirt beside him; Zavee stepping forward to meet him with a hand on his own chest in greeting and a welcoming smile; the red-and-gold set glowing behind",
         camera="medium wide, eye level, the dark floor as the lower third", amb="tv_studio"),
    dict(to=23, reason="emotional turning point: Lail sees Saba coming out of the makeup room; both freeze", chars=["lail", "saba"], loc="floor",
         visual="over Lail's shoulder: Lail in the foreground turning his head, frozen in mid-step; a few metres away Saba stepping out of the grey makeup-room door, stopping still, their eyes meeting across the dim studio floor",
         camera="over-the-shoulder medium wide, Saba in the upper half of the frame, the dark floor as the lower third", amb="tv_studio"),
    dict(to=27, reason="focus change: Lail's eyes on Saba's face - large dark eyes, a face like the full moon; she blushes", chars=["saba"], loc="floor",
         visual="close-up of Saba in the doorway, her very large dark eyes lowered shyly, a deep rosy blush rising on her cheeks, her pale-lavender hijab and the blue-and-lilac flowered dress lit softly by the warm spill of the set lights, her face luminous against the dark studio like a full moon in a night sky",
         camera="close-up, eye level, face in the upper third, her clasped hands and dress in soft focus below", amb="tv_studio"),
    dict(to=30, reason="character enters: Miya greets Lail, but his gaze stays on Saba", chars=["lail", "miya", "saba"], loc="floor",
         visual="Miya standing a polite arm's length in front of Lail with her right hand on her heart in greeting and a friendly smile; Lail nodding to her but his eyes drifting past her towards Saba, who walks slowly towards them a few steps behind Miya, looking back at him",
         camera="medium wide three-shot, eye level, the dark floor as the lower third", amb="tv_studio",
         sens="intimacy", safe="the narrated handshakes are shown as hand-on-heart greetings at a distance; nobody touches"),
    dict(to=34, reason="action change: Lail and Saba greet each other and stand gazing silently", chars=["lail", "saba", "miya", "zavee"], loc="floor",
         visual="Lail and Saba standing facing each other a full arm's length apart, Lail with his right hand on his chest in greeting and a gentle smile, Saba with her hands clasped in front of her, eyes lifted to his, both silent and captivated; Miya standing between and slightly behind them, Zavee leaning to say something to her",
         camera="medium wide side view, their faces in the upper half, the open space between them clear, the dark floor as the lower third", amb="tv_studio",
         sens="intimacy",
         safe="the narration's long handshake between the married Saba and Lail is shown as a polite hand-on-heart greeting at a distance, Miya between them; no touching"),
    dict(to=36, reason="action change: Miya whispers 'let's hurry' and Saba starts out of the gaze", chars=["saba", "miya"], loc="floor",
         visual="Miya leaning close to Saba's side and murmuring to her; Saba blinking as if waking up, a small startled breath, her clasped hands drawn back against her chest, turning towards the set; the glowing red-and-gold set behind them",
         camera="medium two-shot, eye level, the dark floor as the lower third", amb="tv_studio"),
    dict(to=37, reason="action change: they take their seats on the set; Zavee asks 'Ready?'", chars=["lail", "saba", "miya", "zavee"], loc="set_live",
         visual="Saba and Miya sitting side by side in two cushioned armchairs facing Lail, who sits opposite them across the red carpet; Zavee standing behind a studio camera at the side giving a thumbs-up, headset on; the red-and-gold backdrop without letters behind them",
         camera="wide shot from behind the studio camera, the people in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=40, reason="action change: on air - Miya and Saba greet the viewers", chars=["miya", "saba"], loc="set_live",
         visual="Miya and Saba sitting side by side in their armchairs, both smiling brightly straight into the camera with small clip microphones on their clothes, Saba's smile bright but her eyes a little tired; the glossy red-and-gold backdrop behind them",
         camera="medium two-shot straight on, as if from the studio camera, faces in the upper half, their laps and the red carpet as the lower third", amb="tv_studio"),
    dict(to=43, reason="focus change: the guest Lail, 29, award-winning writer, tries to smile and relax", chars=["lail"], loc="set_live",
         visual="Lail sitting in a cushioned armchair on the set, a small clip microphone on his henley, his hands resting on the armrests, a calm, slightly shy smile slowly forming, thoughtful dark eyes; warm studio light on his face",
         camera="medium shot, eye level, his face in the upper third, the armchair and red carpet as the lower third", amb="tv_studio"),
    dict(to=46, reason="detail: Lail's gaze falls on Saba's hands nervously twisting her ring", chars=["saba"], loc="set_live",
         visual="close-up of Saba's hands resting in her lap on her flowered dress, the fingers of one hand nervously turning a simple gold ring on the other hand; above, in soft focus, her face with an uneasy distracted look",
         camera="close-up, her face soft in the upper third, the hands and ring in the middle, the dress folds as the lower third", amb="tv_studio"),
    dict(to=49, reason="action change: Saba introduces tonight's guest to the camera", chars=["saba", "miya", "lail"], loc="set_live",
         visual="Saba leaning slightly forward in her armchair, speaking with a professional smile and turning to Miya with a questioning look; Miya beside her nodding; Lail seen from behind at the edge of the frame, listening",
         camera="over-the-shoulder from behind Lail towards the two hosts, faces in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=51, reuse="beat_015", reason="return: Miya turns to the camera and names the guest", loc="set_live", visual="(reuse)", amb="tv_studio"),
    dict(to=55, reason="action change: Lail thanks them - his very first interview; Miya jokes", chars=["lail", "miya", "saba"], loc="set_live",
         visual="the three in their armchairs seen from the side: Lail giving a small modest nod with a shy smile, Miya laughing as she jokes, Saba smiling softly between them; the red-and-gold backdrop glowing",
         camera="wide side view of the set, faces in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=60, reason="emotional change: Saba says she is his fan; Lail's face lights up and he leans back", chars=["saba", "lail"], loc="set_live",
         visual="Saba speaking warmly with a happy smile, eyes shining with admiration; across from her Lail leaning back in his armchair, his face lit up with quiet joy; a full arm's length of red carpet between them",
         camera="medium wide two-shot from the side, faces in the upper half, the red carpet between them as the lower third", amb="tv_studio"),
    dict(to=62, reason="action change: Saba asks Lail how much weight a 'word' carries", chars=["saba", "lail"], loc="set_live",
         visual="over Lail's shoulder: Saba looking directly at him across the set as she asks her question, her head slightly tilted, curious and soft; Lail's shoulder and the back of his head in the foreground, a faint smile on the edge of his face",
         camera="over-the-shoulder medium close-up, Saba's face in the upper third, the armchair arm as the lower third", amb="tv_studio"),
    dict(to=66, reason="inner monologue: his 'words' are years of tears, lost sleep and a love held back - symbolic", loc="desk",
         visual="a lonely writer's desk by a rain-streaked window at night: an open notebook covered in soft illegible scribbled lines, a pen lying across it, a cold cup of tea, crumpled paper balls, a single small warm lamp; no people",
         camera="medium shot from above the desk at an angle, the window and lamp in the upper half, the desk top as the lower third", amb="apartment_rain_night",
         transition="dissolve", sens="other",
         safe="his years of pain are shown only symbolically; the notebook holds only illegible lines"),
    dict(to=69, reason="return to the interview: he answers carefully; Miya asks how he became a writer", chars=["lail", "miya", "saba"], loc="set_live",
         visual="wide view of the set from behind a studio camera: Lail answering thoughtfully with his hands loosely clasped, Miya and Saba listening opposite him, bright lights glowing around them",
         camera="wide shot from behind a studio camera, the people in the upper half, the red carpet as the lower third", amb="tv_studio",
         transition="dissolve"),
    dict(to=71, reason="emotional turning point: 'feelings for someone' - Saba's face changes; Lail smiles faintly at her", chars=["saba", "lail"], loc="set_live",
         visual="Saba frozen in her armchair, her face suddenly pale and her eyes widening, lips parted; across the set Lail looking straight at her with a faint knowing smile; a full arm's length of red carpet between them",
         camera="medium two-shot across the set, faces in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=73, reason="action change: Miya teases 'Who's the lucky one?' and Lail laughs it off", chars=["miya", "lail"], loc="set_live",
         visual="Miya leaning forward in her armchair with a playful teasing grin; Lail opposite her laughing lightly and raising one open palm as if to brush the question away",
         camera="medium two-shot from the side, faces in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=77, reason="action change: Saba asks why he never gave interviews; 'no time' - the hosts exchange a puzzled glance", chars=["saba", "miya", "lail"], loc="set_live",
         visual="Saba and Miya turning to look at each other with puzzled raised eyebrows; Lail in the foreground seen from behind and to the side, slightly out of focus",
         camera="over-the-shoulder medium shot from behind Lail, the two hosts' faces in the upper half, the armchair as the lower third", amb="tv_studio"),
    dict(to=79, reuse="beat_016", reason="return: Lail explains he is camera-shy and called arrogant for refusing", loc="set_live", visual="(reuse)", amb="tv_studio"),
    dict(to=82, reason="emotional peak: his meaningful gaze holds Saba; she drowns in his eyes and blushes", chars=["lail", "saba"], loc="set_live",
         visual="side profile view across the set: Lail in his armchair looking at Saba with a deep meaningful smile, Saba opposite him meeting his eyes, spellbound, a rosy blush spreading over her face; a full arm's length of glowing red carpet and studio light between them",
         camera="medium wide profile two-shot, faces in the upper half, the empty space between them clear, the red carpet as the lower third", amb="tv_studio",
         sens="intimacy", safe="a married woman and another man: only a look across the set at a distance, no touch"),
    dict(to=86, reason="action change: the interview ends; Saba leaves her mic and hurries off; Miya and Lail unclip theirs", chars=["saba", "miya", "lail"], loc="set_live",
         visual="Saba walking away quickly towards the grey makeup-room door in the background, head down; in the foreground Miya unclipping the small microphone from her blazer and looking after her, Lail still seated, unclipping his microphone, his eyes following Saba; a small clip microphone left on Saba's empty armchair",
         camera="medium wide, eye level, from the set towards the door, faces in the upper half, the red carpet as the lower third", amb="tv_studio"),
    dict(to=90, reason="action change: Miya thanks Lail and tells him Saba was the one who invited him", chars=["miya", "lail"], loc="floor",
         visual="Miya and Lail standing at the edge of the set at a polite distance, Miya speaking with an animated happy smile, Lail listening with a quiet amused smile, a calm independent look in his eyes; the red-and-gold set glowing behind them",
         camera="medium two-shot, eye level, the dark floor as the lower third", amb="tv_studio"),
    dict(to=92, reason="action change: Lail says goodbye to Zavee and glances at the makeup-room door", chars=["lail", "zavee", "miya"], loc="floor",
         visual="Lail standing with Zavee, his hand on his heart in farewell, but his head turned towards the closed grey makeup-room door at the side; Miya beside Zavee also glancing towards the door, a little anxious",
         camera="medium wide, eye level, the dark floor as the lower third", amb="tv_studio"),
    dict(to=95, reason="action change: Lail takes a business card from his wallet and offers it to Miya, then leaves", chars=["lail", "miya"], loc="floor",
         visual="Lail holding out a small plain white business card between two fingers at arm's length towards Miya, an open wallet in his other hand, a friendly smile; Miya reaching to take the card by its far edge; the card shows only soft blank space, no writing",
         camera="medium two-shot, eye level, the dark floor as the lower third", amb="tv_studio",
         sens="other", safe="the card is blank (no readable text); only the card passes between them, no touch"),
    dict(to=99, reason="scene change: back in the makeup room - Saba, changed, lost in thought; Miya puts the card down", chars=["saba", "miya"], loc="makeup",
         visual="Saba sitting at the dressing table in a different modest outfit - a loose long-sleeved plain dusty-mauve dress, her pale-lavender hijab fully covering her hair and neck - staring blankly into the distance; Miya just inside the door, placing the small blank white card on the dressing table beside her, giving her a searching sideways look",
         camera="medium two-shot, eye level, the dressing table top as the lower third", amb="tv_studio"),
    dict(to=101, reason="detail: Saba's watery smile, her fingertip circling the card on the table", chars=["saba"], loc="makeup",
         visual="close-up of Saba sitting at the dressing table in her plain dusty-mauve dress and pale-lavender hijab, a sad smile with tears welling in her eyes, her fingertip slowly tracing circles on the small blank white card lying on the table in front of her",
         camera="close-up, her face in the upper third, the card and her hand on the table top as the lower third", amb="tv_studio"),
    dict(to=104, reason="emotional turning point: 'I'm married' - Miya: 'that's a life sentence, not a marriage'", chars=["miya", "saba"], loc="makeup",
         visual="Miya standing with her arms crossed, eyebrows drawn together and lips pursed in frustration, looking down at Saba; Saba sitting at the dressing table looking up at her with a tired, resigned expression, wearing her plain dusty-mauve dress and pale-lavender hijab",
         camera="medium two-shot, slightly low angle, the dressing table top as the lower third", amb="tv_studio"),
    dict(to=106, reason="action change: Saba gets ready to leave - changes her earrings, smooths her clothes, straightens her hijab", chars=["saba"], loc="makeup",
         visual="Saba standing at the bulb-framed mirror in her plain dusty-mauve dress, adjusting the folds of her pale-lavender hijab with both hands, her handbag on the counter, a closed sad face, preparing to go",
         camera="medium shot from the side of the mirror, her face in the upper third, the dressing table top as the lower third", amb="tv_studio",
         sens="clothing", safe="narration has her tying up her hair: shown as adjusting her hijab, hair always covered"),
    dict(to=108, reason="character change: Miya alone photographs the card and slips it into Saba's bag", chars=["miya"], loc="makeup",
         visual="Miya alone in the makeup room, holding the small blank white card and slipping it into the open handbag left on the swivel chair, her phone in her other hand with its screen showing only a soft glow, a hopeful determined little smile",
         camera="medium shot, eye level, her face in the upper third, the chair and bag in the lower third", amb="tv_studio",
         sens="other", safe="card blank, phone screen only a glow"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Huge bright lamps blazed from six sides, and the ceiling above was fitted with the same bright lamps.")
sh(2, "In the middle of the studio, built so it could be filmed from three directions, a big red-and-gold backdrop sparkled with the name 'Tharinnaa Eku'.")
sh(3, "In front of the backdrop a red carpet was laid on the floor. On the carpet, on both sides, soft cushioned chairs were set out for four people.")
sh(4, "The purpose of this beautifully made set was to give viewers a polished programme in a spacious, high-quality setting.")
sh(5, "Miya came into the studio on a phone call. Signalling to her friends there that she was coming, she headed for the makeup room inside the studio.")
sh(6, "Just then Saba came into the studio too, head down, pretending to look for something in her handbag.")
sh(7, "Everyone there was busy with what they were doing, so Saba could slip in without anyone seeing her.")
sh(8, "Saba hurried into the makeup room after Miya. Miya was still on the phone, so she paid Saba no attention.",
   [("footsteps_pavement", "ހިނގުމެއް", -24)])
sh(9, "Saba put down the bag in her hand and stopped in front of the mirror. Then, turning her face a little to one side, she looked at her temple.")
sh(10, "It was obvious the foundation had been rubbed on to hide a mark on her face. Saba touched it gently. At that moment her eyes filled with tears.",
   [("sob_breath", "ކަރުނުން", -24)], hum=True)
sh(11, "Saba quickly wiped beside her eyes with a tissue. Since Miya was still on the phone, Saba hurried to fix the smudged makeup on her face.")
sh(12, "\"An exclusive interview - wow!\" Miya said, a happy smile on her lips.")
sh(13, "Saba was busy finishing her makeup as fast as she could. When Saba didn't answer, Miya looked over.")
sh(14, "And with a quick movement Miya took hold of Saba's hand. Saba looked up at Miya's face, startled.",
   [("gasp", "ސިހިފައި", -22)])
sh(15, "Then she saw the tears gathering in her eyes. \"Tonight too?\" Miya asked in a worried voice.")
sh(16, "\"This is my fate - how do I change it?\" Saba blinked her watery eyes with a bitter smile. \"I wouldn't stay.\"",
   [("sigh", "ހިތިހިނިތުން", -24)], hum=True)
sh(17, "Miya said, unsatisfied. \"I'm not Miya, Miya,\" Saba said, looking at her face in the mirror again. \"Ready yet?\"")
sh(18, "the show's producer Zavee asked, opening the door. \"Just finishing,\" Saba said. \"Hurry up, tonight's guests have arrived,\" said Zavee.",
   [("door_open", "ހުޅުވައިލަމުން", -20)])
sh(19, "\"Guests? How many?\" Saba couldn't help asking. \"Sorry - guest... OK,\" Zavee said with a joking smile.")
sh(20, "Zavee pulled the door shut and looked into the studio. Just then tonight's guest walked in, chatting with a young man there.",
   [("door_close", "ލައްޕައިލައިފައި", -20)])
sh(21, "Zavee went forward, greeted him and introduced himself. \"Assalaamu alaikum, I'm Zavee, the producer of this show.\"")
sh(22, "Zavee said, greeting him. \"Laail,\" Laail replied. At that moment Laail's eyes fell on Saba, coming out of the makeup room.")
sh(23, "Saba stopped too when she saw Laail. Once he looked at Saba's face, he couldn't take his eyes off it.", hum=True)
sh(24, "As he looked at the face of that young woman in a top decorated with blue and pale-purple flowers, a wave of a strange")
sh(25, "feeling rushed through his heart. Big eyes with the darkest black kohl. Hair like a black night.")
sh(26, "And that fair face like the full moon of the fourteenth night, shining out of the darkness of a black night. So Laail imagined.")
sh(27, "Sensing Laail looking at her, the red of shyness rose into her face. She looked as if she had turned into a red rose-apple.")
sh(28, "Miya, who came up behind Saba, held out her hand to greet Laail. \"Hi, I'm Miya,\" Miya said with a smile. \"Hi, Laail,\"")
sh(29, "he said, greeting Miya. But even then Laail's gaze was fixed on Saba, who was slowly coming that way.")
sh(30, "Saba's gaze too was fixed on Laail's face. Her heartbeat was racing unusually fast.",
   [("heartbeat", "ތެލެމުން", -22)], hum=True)
sh(31, "Afraid the unease would show on her face, Saba lowered her head. \"Hi,\" Laail said with a smile.")
sh(32, "At the sound of Laail's voice Saba raised her head. Laail stood holding out his hand to greet her. \"Hi,\" came Saba's choked voice.")
sh(33, "Saba too greeted Laail. When Zavee said something in Miya's ear, she nodded and looked at Laail.")
sh(34, "Even then Laail's and Saba's eyes were locked. Without a single word the two kept looking at each other. Their hands were still joined.",
   hum=True)
sh(35, "\"Saba, come on, let's hurry,\" Miya said softly in Saba's ear. With a little start Saba drew her hand back from Laail's.",
   [("breath", "ސިހުމަކާއެކީގައި", -22)])
sh(36, "She nodded in agreement with what Miya had said. When Saba asked Laail to take a seat, he walked alongside her.")
sh(37, "Saba and Miya sat in the two chairs facing Laail. \"Ready?\" Zavee asked. \"Ready - Laail, are you OK?\" Miya asked.")
sh(38, "Laail nodded that he was ready. \"Assalaamu alaikum,\" the two girls said together, looking into the camera.")
sh(39, "\"Welcome to Tharinnaa Eku - I'm Miya.\" As Miya got that far, Saba began to speak. \"And I'm Saba.\"")
sh(40, "Saba said with a happy smile on her lips. At that moment, wiping away the worry and unease on her face, Saba kept talking.")
sh(41, "Seeing Miya's and Saba's cheerful mood, Laail's restless heartbeat settled down.")
sh(42, "Laail tried to bring a happy smile to his lips too. Twenty-nine-year-old Laail was a gifted writer who had won many awards in the Maldives and abroad.")
sh(43, "Many films had been made from his stories and had seen the light of day. Tonight Laail was on 'Tharinnaa Eku' as the guest.")
sh(44, "\"Tonight's show, too, opens with a beautiful song,\" Miya said. Laail's eyes settled on Saba's hand.")
sh(45, "She was playing with the ring on her finger. Then Laail's gaze stopped on Saba's uneasy face.")
sh(46, "With a glance Miya asked Saba if she was OK. Saba gave a small nod to say she was.")
sh(47, "After a short silence Saba began to speak again. \"On our show we usually bring you film stars,")
sh(48, "so tonight too we bring you a talented artist - one whose face isn't seen in the films,")
sh(49, "but who plays the biggest role in making them. Did I put that right?\" Saba asked Miya.")
sh(50, "Miya smiled at the camera to answer Saba's question. \"Right... His work begins the moment someone thinks of making a film - with flowing phrases and powerful words")
sh(51, "he plays with the heartbeats of viewers and readers: the famous writer Ahmed Laail Haizum.\"")
sh(52, "Miya said with a happy smile. \"A very warm welcome to the show, Laail,\" Miya said, smiling. \"Thank you.\"")
sh(53, "Laail replied. \"I think this is the first time we've met Laail, isn't it?\" Miya asked.")
sh(54, "Laail gave a small nod. \"That's right... my first interview,\" Laail answered with a smile.")
sh(55, "\"So, Saba, we two are very lucky,\" Miya said with a smile in a joking tone. Saba smiled too.")
sh(56, "\"I'm a fan of Laail's stories,\" Saba said with a happy smile on her lips.")
sh(57, "Hearing Saba's words, joy showed on Laail's face. He relaxed and leaned back in his chair. \"It seems -")
sh(58, "no, it's certain - Laail has countless fans in love with his stories. Not only in the Maldives,")
sh(59, "abroad too,\" Saba said with a happy smile. \"Laail's stories are written with such deep feeling,")
sh(60, "with words strung together in phrases too beautiful to describe. So tonight we bring you a little about the film 'Lafuz', due to be screened at Olympus next Friday night.\"")
sh(61, "Miya went on with a smile. \"A word - you could call it something very powerful, you could call it something very brief, or you could dismiss it as something very small.")
sh(62, "How much weight does this 'word' really carry?\" Saba asked, looking at Laail's face. Laail smiled.")
sh(63, "With what 'words' would he explain 'word'? Years of tears. Years of lost sleep.", hum=True)
sh(64, "The trembling of a restless heart. The story of his own conscience, its throat choked by love.")
sh(65, "In the form of 'words' he was describing the love in his heart for someone.")
sh(66, "How could he tell the story of the pain, the longing and the grievances in his heart that he had been pouring out through his writing?")
sh(67, "The interview went on. Laail answered the questions the girls asked very carefully.")
sh(68, "For he feared that even one word said by mistake could wreck his future. \"How did you get into this field?\" Miya asked.")
sh(69, "\"You could say it was because of feelings that grew in my heart for someone,\" Laail blurted out without meaning to.", hum=True)
sh(70, "Laail saw the colour drain from Saba's face. At the same moment a faint smile appeared on his lips.", hum=True)
sh(71, "But Laail's eyes were still fixed on Saba's face. \"Oh...\" Miya said with a smile. \"And who's the lucky one?\"")
sh(72, "Miya asked. \"I said it as a joke, there's nothing like that... Passion... Writing is my hobby. A friend gave me the chance to write for the magazine he published,")
sh(73, "and I'd like to take this chance to thank Haseena, editor of the magazine 'Addu Vas',\" Laail said with a smile.")
sh(74, "\"What's the secret behind never giving a single interview all this time?\" Saba asked. Laail gave a faint smile.")
sh(75, "Saba sat waiting for his answer. Miya too kept looking at Laail with a smile.")
sh(76, "Though Laail didn't know what the girls were thinking, he composed himself and got ready to answer. \"Because I don't have time.\"")
sh(77, "Laail said quietly. Miya and Saba looked at each other. They didn't believe his answer. Laail could tell from their look.")
sh(78, "\"I'm very shy in front of the camera - maybe that's the secret. When people called for interviews and I refused,")
sh(79, "some even said I was very arrogant,\" Laail answered, trying to stay calm. Even then Laail's eyes were fixed on Saba, who was asking the questions.")
sh(80, "It was as if Saba sank into the eyes of Laail, who sat with his gaze fixed on her face.", hum=True)
sh(81, "On Laail's lips now was a smile full of meaning. An intoxicated look. As if his gaze were touching her.", hum=True)
sh(82, "The red of shyness spread over Saba's face. \"So shall we watch the film's teaser?\" Since Saba asked nothing more, Miya asked her, to bring her into the talk.")
sh(83, "\"The film's teaser,\" Saba said, tearing her eyes from Laail's face. When the interview ended, Saba hurried to run away from in front of Laail.")
sh(84, "It was as if Laail's look was killing her. Quickly Saba removed the mic fixed to her clothes and put it on the chair she had been sitting in.",
   [("cloth_rustle", "ނައްޓާލުމަށްފަހު", -24)])
sh(85, "Then, without looking at anyone else, she walked quickly into the makeup room. Miya, removing the mic clipped to her clothes, looked where Saba had gone.",
   [("footsteps_pavement", "ހިނގުމުގައި", -22)])
sh(86, "Laail too removed the mic fixed to his T-shirt and put it on the chair. \"Thank you for coming tonight,\" Miya said, saying goodbye to Laail.")
sh(87, "\"Thank you for inviting me to the show,\" Laail said with a smile too. \"Saba deserves more thanks than I do.")
sh(88, "Saba plucked up the courage to message Laail, paying no attention to the rumours going around about Laail. Zavee and I thought Laail would refuse, but Saba was sure Laail wouldn't refuse this show.\"")
sh(89, "Miya spoke with a happy smile. Laail smiled too, because he also knew the stories about his temper that were spreading through the papers.")
sh(90, "To tell the truth, he didn't care about any of it. He was a free-thinking man, not someone used to dancing to every drum that beats.")
sh(91, "After saying goodbye to Zavee, Laail looked towards the makeup room. When Laail looked that way, Miya, standing beside Zavee, looked over too.")
sh(92, "\"Sorry Laail, Saba had to leave a bit early - she has a shoot for another programme, so she went to change.\"")
sh(93, "Miya said hurriedly. \"Oh... no worries.\" Laail took his wallet from his pocket, took out his card and held it out to Miya.",
   [("cloth_rustle", "ވޮލެޓު", -24)])
sh(94, "\"If you need more information, best to call - or send a message,\" Laail said with a smile on his lips. \"Thank you,\"")
sh(95, "Miya said. \"I'm off.\" Laail set off to leave. When Laail had gone, Miya went into the makeup room.",
   [("footsteps_pavement", "ހިނގައިގަތެވެ", -24), ("door_open", "ވަނެވެ", -22)])
sh(96, "Saba was sitting by the dressing table, lost, staring at one spot. Saba had changed her clothes.")
sh(97, "Miya came in and put the card Laail had given on the dressing table. \"I think this was meant for you,\" Miya said quietly.")
sh(98, "\"Has Laail gone?\" Saba asked. \"Yes... You knew Laail before, didn't you? The way he kept looking at you was so different...")
sh(99, "I'm not the only one who noticed - Zavee noticed too,\" Miya asked in a voice full of suspicion. Saba smiled.")
sh(100, "At the same moment her eyes filled with tears. \"I could say the same to you, Miya - a month ago the makeup artist who came looked at you exactly like that...",
   hum=True)
sh(101, "Did I ask about that?\" Saba asked, tracing circles with her finger on the card Miya had put on the table. Miya watched Saba's hand.")
sh(102, "\"So you don't need the card, right?\" Miya asked. \"No, I won't need it. Besides, I think you've forgotten I'm 'married'.\"")
sh(103, "Saba said, in a tone of reminding her of something. \"LOL... that's no marriage - you're living a life prison sentence, and you don't even know your crime.\"",
   hum=True)
sh(104, "Miya said, frowning and pursing her lips. \"OK, I don't want to argue. I'm going to get ready -")
sh(105, "Mod will come looking for me soon.\" She said this while changing her earrings. After looking at her face in the mirror, she smoothed the clothes she was wearing.")
sh(106, "And she tied her hair up. \"I'm off,\" Saba said, setting off. Miya looked at the card in her hand.",
   [("footsteps_pavement", "ހިނގައިގަންނަމުން", -24)])
sh(107, "Then, after taking a photo of the card, she put it into Saba's bag. \"Maybe this card will take Saba's life in a new direction - a way out of that pitch-dark, thorny jungle.\"",
   [("camera_shutter", "ފޮޓޮއެއް", -20)], hum=True)
sh(108, "Miya said softly. Miya had put the card into Saba's bag without thinking twice.")
SHOTS = S

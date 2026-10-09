"""Beat/shot plan for Tedhuveriloabi episode 480 (used by plan_beats.py)."""

LOC = {
    "ward": "a hospital ward room at ADK Hospital in Malé at night, a single hospital bed with white sheets, cool white walls, a drip stand, a bedside cabinet, a plain chair, a door to the corridor, a dark window with distant city lights",
    "corridor": "a long cool-white hospital corridor at night, glossy pale floor tiles, ceiling lights, closed doors along the walls",
    "entrance": "the main entrance lobby of a modern hospital in Malé at night, glossy pale floor, wide sliding glass doors, the dark street beyond",
    "street": "the entrance of a modern apartment building on a Malé street at night, warm streetlights, a dark glass doorway, potted palms",
    "lane_morning": "a narrow Malé lane outside a small plain old house with pale peeling walls, a wooden front door, potted plants, a low wall",
    "lane_afternoon": "a narrow Malé lane leading to a small plain old house with pale peeling walls, a wooden front door, potted plants, a low wall",
    "sitting": "the tiny plain sitting room of an old Malé house, a simple single bed against the wall, faded walls, a small window, plastic chairs, a doorway to a bedroom hung with a floral cloth curtain",
    "office": "the open-plan finance floor of a modern glass high-rise office in Malé, tidy desks with monitors facing away, glass walls, a city and sea view",
    "cabin": "Rafhaan's luxurious glass-walled CEO cabin in a high-rise, a large dark wood desk, a black leather chair, floor-to-ceiling windows over Malé and the sea",
    "hall": "an elegant wedding hall in Malé decorated with white and golden flowers, soft cream drapes, warm crystal chandeliers, a flower-decked low stage",
    "nikah": "a wedding hall in Malé, a table draped in white cloth with white and golden flower arrangements, guests softly blurred in the background",
    "terrace": "an open rooftop terrace of the wedding hall at night overlooking the lights of Malé, a starry sky, a low railing, pots of white flowers",
}
MOOD = {
    "ward": "night, soft warm bedside lamp against cool blue shadows, quiet and tender",
    "corridor": "night, harsh cool fluorescent light, motion and urgency",
    "entrance": "night, cool white light inside, dark blue night outside, tense",
    "street": "night, amber streetlights and deep blue shadows, cold and grim",
    "lane_morning": "early morning, fresh golden sunrise light, hopeful",
    "lane_afternoon": "late afternoon, warm golden light, hopeful and expectant",
    "sitting": "late afternoon, warm golden light through the small window, gentle and joyful",
    "office": "bright daytime, soft natural light, warm and cheerful",
    "cabin": "late afternoon, golden light through the glass, heavy and solemn",
    "hall": "evening, warm golden chandelier light, white and gold glow, festive and tender",
    "nikah": "evening, warm golden light, solemn and joyful",
    "terrace": "night, starry dusk-blue sky, soft warm fairy lights, peaceful and romantic",
}

BEATS = [
    dict(to=6, reason="new episode opening: night in the ward, Qaasim recovering and talking with Layaali", chars=["qaasim", "layaali"], loc="ward",
         visual="Qaasim sitting up in the hospital bed against white pillows, smiling weakly and talking; Layaali sitting on a plain chair beside the bed listening with a gentle smile, her hands folded in her lap",
         camera="medium two-shot, eye level", amb="hospital_night"),
    dict(to=10, reason="characters change: the masked fake nurse enters the ward", chars=["fake_nurse", "layaali", "qaasim"], loc="ward",
         visual="in the foreground Layaali sitting by the bed with her head lowered shyly; behind her, in the open doorway, a woman in a white nurse uniform and a pale-blue surgical mask stepping in, carrying a small steel tray with medicine vials, her eyes darting nervously; Qaasim resting in the bed at the side",
         camera="medium wide, eye level", amb="hospital_night"),
    dict(to=12, reason="action change: the fake nurse prepares the syringe beside Layaali", chars=["fake_nurse", "layaali"], loc="ward",
         visual="the masked nurse standing close beside Layaali's chair holding up a small capped syringe, her narrowed eyes cold and tense above the mask; Layaali looking up at her trustingly, sleeves still down, unaware",
         camera="medium close two-shot", amb="hospital_night", sens="violence",
         safe="the poison injection is never shown: only a capped syringe held up and the nurse's tense eyes; no needle near the arm"),
    dict(to=15, reason="characters change: Rafhaan walks in, the syringe falls", chars=["rafhaan", "fake_nurse", "layaali"], loc="ward",
         visual="Rafhaan standing in the open ward doorway with a sharp, suspicious stare; the masked nurse frozen in shock near the bed, her empty hands trembling; a small syringe lying on the pale floor tiles between them; Layaali seated, confused",
         camera="medium wide, from inside the room towards the door", amb="hospital_night", sens="violence",
         safe="the attempted poisoning is shown only as a syringe dropped on the floor and a frightened face"),
    dict(to=17, reason="scene and action change: the chase down the corridor", chars=["fake_nurse", "rafhaan"], loc="corridor",
         visual="the masked woman in white nurse uniform running away down the long hospital corridor, looking back over her shoulder in panic; Rafhaan running after her in the distance, one arm raised, shouting for help",
         camera="wide shot down the corridor, low angle", amb="hospital_corridor"),
    dict(to=19, reason="scene change: she is caught at the hospital's main door, security arrives", chars=["rafhaan", "fake_nurse"], loc="entrance",
         visual="at the hospital's glass main entrance, the masked woman sitting on the floor, caught and frightened, her eyes wide; Rafhaan standing between her and the glass doors at an arm's length, breathing hard, blocking the exit; two security guards in plain dark uniforms hurrying in from the side",
         camera="medium wide, eye level", amb="hospital_night", sens="violence",
         safe="the takedown is not shown: she is already sitting on the floor, Rafhaan simply blocks the door at a distance"),
    dict(to=22, reason="characters change: the police arrive and she confesses", chars=["rafhaan", "fake_nurse"], loc="entrance",
         visual="the woman in the white nurse uniform, her surgical mask pulled down to her chin revealing her thin face, weeping as she speaks to two Maldivian police officers in plain dark-blue uniforms with no visible insignia or text; Rafhaan standing beside them in his black suit with a clenched jaw and blazing, shocked eyes",
         camera="medium shot, eye level", amb="hospital_night", sens="other",
         safe="arrest shown as officers listening, no handcuffs, no weapons"),
    dict(to=26, reason="scene change: back in the ward, Rafhaan reassures the frightened Layaali", chars=["layaali", "rafhaan"], loc="ward",
         visual="Layaali sitting on the chair by the bed with tears on her cheeks, hands clasped tightly at her chest, looking up; Rafhaan crouching in front of her at a respectful distance, not touching her, his face firm and tender, speaking reassuringly",
         camera="medium close two-shot, eye level", amb="hospital_night", sens="intimacy",
         safe="he lifts her face and she hugs him in the narration (not yet married): shown as a reassuring look at a respectful distance, no touch"),
    dict(to=30, reason="scene and character change: Raaya is arrested", chars=["raaya"], loc="street",
         visual="Raaya being escorted out of a dark glass doorway by two Maldivian police officers in plain dark-blue uniforms with no visible insignia or text, walking on either side of her; her cold face now pale and shocked",
         camera="medium wide, eye level", amb="street_night", sens="other",
         safe="arrest shown as being escorted, no handcuffs, no weapons"),
    dict(to=32, reason="time jump: the next morning, Qaasim discharged and brought home", chars=["rafhaan", "qaasim", "layaali"], loc="lane_morning",
         visual="Rafhaan gently supporting frail Qaasim by the arm as he walks slowly towards the wooden front door of the small house; Layaali following a step behind carrying a small cloth bag, smiling with relief",
         camera="medium wide, eye level", amb="city_day", transition="black"),
    dict(to=35, reason="time and character change: Ibrahim and Rafhaan come to the house in the afternoon", chars=["ibrahim", "rafhaan"], loc="lane_afternoon",
         visual="Ibrahim Faahim and Rafhaan walking side by side up the narrow lane towards the small plain house, Ibrahim carrying a small wrapped gift box and smiling warmly, Rafhaan slightly nervous and hopeful",
         camera="medium wide, eye level", amb="city_day"),
    dict(to=39, reason="scene change: the proposal in the tiny sitting room", chars=["ibrahim", "qaasim", "aminath", "rafhaan"], loc="sitting",
         visual="in the tiny sitting room Qaasim sitting up on his simple bed with Aminath standing beside him, both with joyful moist eyes; Ibrahim Faahim and Rafhaan sitting on plastic chairs opposite them, Ibrahim leaning forward smiling as he speaks, Rafhaan respectful",
         camera="medium wide, eye level", amb="home_day"),
    dict(to=41, reason="focus moves to Layaali behind the curtain", chars=["layaali"], loc="sitting",
         visual="Layaali standing half hidden behind a floral cloth curtain in the bedroom doorway, her head lowered, blushing shyly, glancing sideways towards the sitting room",
         camera="medium close-up", amb="home_day"),
    dict(to=42, reason="back to the families as the wedding date is set (reuse)", reuse="beat_012", chars=["ibrahim", "qaasim", "aminath", "rafhaan"], loc="sitting",
         visual="(reuse) the families in the sitting room", amb="home_day"),
    dict(to=45, reason="scene change: the office celebrates Layaali", chars=["layaali"], loc="office",
         visual="Layaali at her desk on the finance floor holding a blank cream invitation card with no writing, smiling shyly, while colleagues in the background (women in modest abayas and hijabs, men in shirts) smile and congratulate her",
         camera="medium shot, eye level", amb="office_day"),
    dict(to=48, reason="time jump and character change: Zaahir arrives humbled at Rafhaan's cabin", chars=["zaahir", "rafhaan"], loc="cabin",
         visual="Ahmed Zaahir standing just inside the glass door of the cabin with slumped shoulders and a defeated, aged face; Rafhaan standing up behind his desk with a hard, guarded expression",
         camera="medium wide two-shot", amb="office_quiet", transition="black"),
    dict(to=51, reason="emotional turning point: Zaahir lowers his head and apologises", chars=["zaahir"], loc="cabin",
         visual="close view of Ahmed Zaahir with his head bowed and one hand pressed to his chest, eyes lowered in shame, the golden window light behind him",
         camera="close-up", amb="office_quiet"),
    dict(to=52, reason="Rafhaan's doubts (reuse)", reuse="beat_016", chars=["zaahir", "rafhaan"], loc="cabin",
         visual="(reuse) Zaahir and Rafhaan in the cabin", amb="office_quiet"),
    dict(to=56, reason="action change: Rafhaan speaks kindly, Zaahir weeps and blesses the marriage", chars=["zaahir", "rafhaan"], loc="cabin",
         visual="Rafhaan, softened, standing in front of his desk speaking gently; Zaahir facing him with tears running down his cheeks, his hands raised slightly in a grateful gesture, about to turn towards the door",
         camera="medium two-shot, eye level", amb="office_quiet", hum_note="emotional peak"),
    dict(to=59, reason="time jump and scene change: the wedding hall, Layaali in her white gown", chars=["layaali"], loc="hall",
         visual="Layaali standing in the flower-decked hall; today she is NOT in her black abaya: she wears a loose long-sleeved ankle-length white lace modest gown and a white lace hijab fully covering her hair and neck; a soft joyful shy smile, eyes lowered, white and golden flowers around her",
         camera="medium full shot, eye level", amb="hall_crowd", transition="black"),
    dict(to=61, reason="focus moves to Rafhaan waiting for his bride", chars=["rafhaan"], loc="hall",
         visual="Rafhaan in his black suit standing beside the flower-decked stage, hands folded in front, gazing ahead with a tender, expectant smile",
         camera="medium shot, eye level", amb="hall_crowd"),
    dict(to=62, reason="action change: the nikah at the table", chars=["rafhaan", "ibrahim", "qaasim"], loc="nikah",
         visual="the nikah: at a white-draped table Rafhaan seated on one side, solemn and happy, facing an imam in a white thobe and white cap; Ibrahim Faahim and Qaasim seated together at one side of the table, both smiling with moist eyes; blank papers lying on the table with no writing",
         camera="medium wide, eye level", amb="hall_crowd"),
    dict(to=65, reason="characters change: Khadeeja blesses Layaali", chars=["khadeeja", "layaali"], loc="hall",
         visual="at the wedding, Khadeeja gently laying her hand on the bride Layaali's covered head in blessing, her eyes moist and remorseful; Layaali is the bride and is dressed ENTIRELY IN WHITE (NOT in her black abaya, no black clothing at all): a loose long-sleeved ankle-length white lace modest wedding gown and a white lace hijab fully covering her hair and neck; Layaali standing, holding Khadeeja's other hand with both hands, tears of joy in her eyes; white and golden flowers behind them",
         camera="medium close two-shot", amb="hall_crowd"),
    dict(to=67, reason="scene and time change: stars over Malé, the married couple side by side", chars=["rafhaan", "layaali"], loc="terrace",
         visual="Rafhaan in his black suit and Layaali in her white lace modest gown and white lace hijab standing side by side at the terrace railing, seen from slightly behind and to the side, her hand resting lightly on his arm, both looking up at the stars above the city lights",
         camera="medium wide, from slightly behind", amb="balcony_night"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "Having said that, Khadeeja turned away. That night Layaali was sitting beside her father in the hospital ward. Qaasim's condition was now much better.")
sh(2, "He was sitting up in bed, talking with Layaali. 'My child... Rafhaan is a very good young man.")
sh(3, "The respect he has shown to humble people like us is priceless,' Qaasim said with a smile.")
sh(4, "'Father is so happy that such a good young man has come into your life. But there is one thing father worries about.")
sh(5, "Wealth and poverty are two things that never mix.' 'Yes, father. I never imagined a boss like Rafhaan would care for poor people like us.")
sh(6, "But now I know he has a noble heart. That is why I agreed to start a life with him.'")
sh(7, "Layaali lowered her head shyly. At that moment a masked woman in a nurse's uniform entered the ward.",
   [("door_open", "ވަނެވެ", -20)])
sh(8, "In her hands were some medicine vials and a syringe. She was the one Raaya had sent. She had come with a dangerous injection for Layaali. 'Layaali?'",
   [("cup_clatter", "ފުޅިތަކަކާއި", -24)])
sh(9, "the nurse called softly. 'The doctor said Rafhaan asked for a check-up for you — to check your blood pressure because of the stress at the office.'")
sh(10, "Layaali was surprised. 'Me? Isn't father the patient?' 'Yes — your boss asked especially. He said to check your health.'")
sh(11, "The nurse was lying. Hearing Rafhaan's name, the doubt in Layaali's heart faded away. The nurse prepared Layaali's arm and picked up the syringe.",
   [("cloth_rustle", "ތައްޔާރުކޮށް", -24)])
sh(12, "Inside it was a deadly poison that could stop the heart. Just as she was about to put the needle to Layaali's arm, the ward door suddenly opened and Rafhaan walked in.",
   [("heartbeat", "ޒަހަރެކެވެ", -18), ("door_open", "ހުޅުވާލާފައި", -16)], hum=True)
sh(13, "'Layaali!' Rafhaan called out happily. Seeing Rafhaan, the nurse started. Her hand began to tremble and the syringe fell to the floor.",
   [("gasp", "ސިހުނެވެ", -20), ("soft_thud", "ވެއްޓުނެވެ", -22)])
sh(14, "Rafhaan's sharp gaze stopped on the syringe on the floor and on the nurse's face. He understood at once that something was wrong.",
   [("heartbeat", "ހުއްޓުނެވެ", -18)], hum=True)
sh(15, "'What happened to Layaali?' Rafhaan was worried, thinking Layaali had suddenly fallen ill. 'Which nurse are you?")
sh(16, "The head nurse of this ward is outside.' Rafhaan took a step forward. The woman instantly shoved Rafhaan aside and ran out of the door.",
   [("soft_thud", "ކޮއްޕާލުމަށްފަހު", -20), ("footsteps_pavement", "ދުއްވައިގަތެވެ", -16)])
sh(17, "'Help!' Rafhaan shouted as he ran after her. It was as if a relay race had begun in the hospital corridor.",
   [("footsteps_pavement", "ދުއްވައިގަތެވެ", -14), ("breath_heavy", "ރިލޭ", -20)])
sh(18, "Rafhaan was a strong young man. Just as she was about to leave by the hospital's main door, he caught the woman by the arm and brought her down to the floor.",
   [("soft_thud", "ތިރިކުރިއެވެ", -18)])
sh(19, "Hospital security came at once. When the woman's mask was removed, it was clear she was not hospital staff.",
   [("footsteps_pavement", "އައެވެ", -20)])
sh(20, "Just then the police were brought there too. Facing the police's hard questions, she revealed the truth at once.",
   [("footsteps_pavement", "ގެނެވިއްޖެއެވެ", -22)])
sh(21, "'Raaya paid me! She told me to kill Layaali!' the woman said, crying. Rafhaan clenched his teeth.",
   [("sob_breath", "ރޮމުން", -22)], hum=True)
sh(22, "He had never imagined jealousy could go this far. Layaali's life had been saved by a hair's breadth.", hum=True)
sh(23, "When Rafhaan hurried back to the ward, Layaali was sitting there, crying in fear. Rafhaan went close to Layaali and lifted her face with both hands. 'Layaali...",
   [("footsteps_pavement", "ދިޔައިރު", -22), ("sob_breath", "ރޮވިފައެވެ", -24)])
sh(24, "Don't be afraid. No harm will come to you. I will smash every trap these wicked people set.'", hum=True)
sh(25, "There was firmness and tenderness in Rafhaan's voice. Layaali held on to Rafhaan tightly.",
   [("sob_breath", "ބައްދާލިއެވެ", -26)], hum=True)
sh(26, "She had been saved from the danger of that unseen shadow because of Rafhaan — because he had come there at that very moment.")
sh(27, "As the police set out to arrest Raaya, Rafhaan decided to complete the wedding as soon as possible.")
sh(28, "Before their love there was no longer room for any enemy. After the frightening incident in the hospital, an unusual gloom had settled over everything.")
sh(29, "Yet even through that darkness, the news that Raaya had been arrested, thanks to the swift work of the police, came as a great")
sh(30, "relief to Layaali's family. All the dangerous traps laid by Ahna and her 'devil' friends were shattered, and they were brought before justice.")
sh(31, "The next day's sun rose with completely new hopes. When Layaali's father Qaasim was discharged from hospital, he was moved home with Rafhaan's own help.")
sh(32, "Rafhaan now wanted to make Layaali part of his life without delaying a single moment more.")
sh(33, "One afternoon Rafhaan's father Ibrahim Faahim and Rafhaan went together to Layaali's house.",
   [("footsteps_pavement", "ދިޔައެވެ", -22)])
sh(34, "Khadeeja did not come with them, but Rafhaan was sure she would not oppose the marriage.")
sh(35, "Now that the company had escaped Zaahir's influence and was running stronger than ever with the new investors, the fear in Khadeeja's heart had faded.")
sh(36, "Khadeeja's worry had been losing their wealth. 'Qaasimbe... we have come for a very important purpose,' Ibrahim Faahim said with a smile.")
sh(37, "'My son Rafhaan's heart is in your daughter's hands. I want these two children's wedding done as soon as possible.'")
sh(38, "Joy shone in the eyes of Qaasim and Aminath. 'Ibrahim... we are very ordinary, humble people.")
sh(39, "For a successful young man like Rafhaan to want our daughter is a great honour for us. If Layaali agrees, I have no objection at all.'")
sh(40, "Qaasim said happily. Behind the curtain at the bedroom door, Layaali's face was turning red with shyness.",
   [("cloth_rustle", "ފަރުދާގެ", -24)])
sh(41, "She stood with her head lowered, her heart pounding. As Rafhaan glanced that way, their eyes met in secret.",
   [("heartbeat", "ތެޅެމުންދިޔައެވެ", -18)], hum=True)
sh(42, "After so much pain and so many tears it was a deep peace for their hearts. The wedding date was set for the following week.")
sh(43, "Rafhaan wanted a celebration that was simple yet complete. Every employee of the office was invited.",
   [("paper_shuffle", "ދައުވަތު", -22)])
sh(44, "Everyone was happy for Layaali. Kind, justice-loving Layaali was no longer just the office's head of finance.")
sh(45, "She was the boss's wife-to-be. But just two days before the wedding, someone came to Rafhaan's office.",
   [("knock", "އައެވެ", -16)])
sh(46, "It was Ahmed Zaahir, father of the jailed Ahna. The arrogance and pride once seen on his face were completely gone.")
sh(47, "He looked defeated and aged. 'Rafhaan...' Zaahir called softly. Rafhaan rose from his cabin chair. 'Zaahirbe...",
   [("cloth_rustle", "ތެދުވިއެވެ", -22)])
sh(48, "why have you come here? There is nothing more to talk about between us.' Rafhaan's voice was hard.")
sh(49, "'I didn't come here to fight, Rafhaan.' Zaahir lowered his head. 'When I learned the truth about what my daughter Ahna did, I was ashamed.")
sh(50, "I never imagined her jealousy could go this far. I came to ask forgiveness from you, Rafhaan, and above all from Layaali.", hum=True)
sh(51, "In jail Ahna keeps telling me to get Layaali's forgiveness for her. Her heart has changed now.'")
sh(52, "Rafhaan was taken aback. Had Ahna's heart really changed? Then why had Raaya sent that woman? Many questions rose in Rafhaan's mind.")
sh(53, "'Zaahirbe... Layaali is a very kind-hearted girl. She has already forgiven Ahna. At the hospital, when Layaali's father needed blood, Ahna gave hers.")
sh(54, "Since that day there has been no grievance in Layaali's heart,' Rafhaan said. Tears poured from Zaahir's eyes. 'Thank you, Rafhaan.",
   [("sob_breath", "ފޮހެލިއެވެ", -24)], hum=True)
sh(55, "I pray that your marriage is blessed.' With that, Zaahir left the cabin and walked away.",
   [("door_close", "ނިކުމެގެން", -20)])
sh(56, "Rafhaan felt that love and forgiveness had triumphed over hatred. The time of the wedding arrived.")
sh(57, "The hall prepared for the wedding glowed with white and golden flowers. Layaali wore a beautiful white lace dress.")
sh(58, "Her simple beauty was complete today. Her face shone with a quiet but joyful radiance.")
sh(59, "Everyone who saw Layaali in that dress was enchanted. That grace was what had captured Rafhaan's heart.")
sh(60, "In his suit Rafhaan's manliness and charm were doubled.")
sh(61, "He was waiting for the moment the queen of his heart would come to him. The wedding sermon began.")
sh(62, "Rafhaan's father and Layaali's father sat on one side of the table. When the words 'I accept her as my wife' left Rafhaan's lips before everyone, tears of joy filled Layaali's eyes.", hum=True)
sh(63, "The invisible line between them was wiped away today; two hearts became one. From among the guests Khadeeja came and stroked Layaali's head.")
sh(64, "'My child... forgive me. I didn't know before how noble your heart is. You are the greatest blessing that came into Rafhaan's life.'", hum=True)
sh(65, "Khadeeja said. Layaali held Khadeeja's hand tightly. 'Mother... it's all right.")
sh(66, "I will always strive to keep this family happy.' As the sun set and the stars came out over Malé's sky, Rafhaan came close to Layaali.")
sh(67, "'Layaali... a new chapter of our life has begun. No storm will ever be able to part us again,' Rafhaan said softly.", hum=True)
SHOTS = S

"""Beat/shot plan for Sahar episode 421 (used by plan_beats.py).
The cave reunion with Hamza, Fathimaa and Ameen; the news of Mahmood, Noor and Yazan; Fathimaa's account of Hamza's
foresight; the midnight escape by hand-lamp through the pine forest; parallel: Yazan in the soldiers' camp (bible rule 4:
no chain, no urination, no cage on screen); dawn arrival at Hashim and Safoora's house in Ein Karem; Sahar's sleepless
dawn, Fajr, and sleep beside Laila. Rules: Sahar's LEFT forearm in a plain cloth sling throughout (except the golden
memory of the garden, which is before her injury); Safiyya's forehead wrapped in a clean cloth strip; every woman's hijab
fully covers hair and neck, also asleep (sitting against a wall under a blanket); no embrace between Sahar and Yazan;
soldiers only as faceless distant silhouettes, no weapons, no insignia; no readable text."""

SLING = ("her LEFT forearm resting in a sling made from a strip of plain beige cloth tied around her neck, no visible "
         "injury")
SAHAR = f"Sahar in her black thobe with deep-red embroidery and black hijab fully covering her hair and neck, {SLING}"
SAFIYYA = ("Safiyya in her dark thobe and black hijab, her forehead wrapped in a clean strip of plain white cloth over "
           "the hijab, no blood")
YAZAN_P = ("Yazan as a prisoner: his same shirt and trousers dusty and creased, the black-and-white keffiyeh still loosely "
           "around his neck, his hands loosely wrapped in clean white cloth at the wrists and palms, no wounds, no blood, "
           "nothing on his neck but the keffiyeh")
SOLDIERS = "only as tiny faceless dark silhouettes far away, no weapons, no uniforms with insignia, no flags"

LOC = {
    "cave_mouth": "the mouth of a large limestone cave high on a wooded hillside west of Jerusalem, framed by pine trees, "
                  "big boulders and thorny bushes, a rocky ledge in front of the opening",
    "cave": "inside a large, roomy limestone cave: rough golden-grey rock walls, a woven rug spread on the sandy floor, "
            "a few clay water jars, cloth sacks of food, a copper pot and canvas bags along the wall, the bright "
            "opening of the cave behind",
    "hillside": "a steep terraced hillside of pine trees, olive trees and huge limestone boulders, the dark mouth of a "
                "cave almost completely hidden behind the trees and rocks halfway up the slope, a narrow footpath far "
                "below",
    "memory_house": "the sitting room of Hamza's golden limestone house in Deir Yassin at night: arched window, a low "
                    "wooden table with an old wooden 1940s valve radio set and a few folded newspapers and books with "
                    "no visible writing, woven cushions, an oil lamp",
    "memory_dawn": "the wooded rocky hillside above Deir Yassin at dawn, a narrow goat path climbing between pines and "
                   "boulders, the golden stone houses of the village far below",
    "cave_dusk": "the mouth of the limestone cave seen from inside, the rough rock walls framing the opening, pine trees "
                 "and the sky outside, a woven rug and bags on the floor",
    "cave_inner": "a quiet corner deep inside the limestone cave, rough rock wall, a woven rug, a folded wool blanket",
    "cave_night": "inside the dark limestone cave at midnight, rough rock walls, bundles and canvas bags on a woven rug, "
                  "two small sticks with a tiny flame on the sandy floor",
    "cave_exit": "a steep rocky path leading down from the dark mouth of the limestone cave at night, huge boulders, "
                 "thorny bushes and pine trunks on both sides",
    "camp_night": "an open dusty field in the hills at night: a few dark canvas army tents in a loose half-circle, a "
                  "small campfire in the middle of the field, pine-covered hills black against the sky",
    "camp_face": "the edge of a soldiers' camp at night, dark canvas tents blurred far behind, the warm flicker of a "
                 "campfire just out of frame",
    "camp_dawn": "the edge of the open dusty field of the camp at sunrise, blurred canvas tents far behind, a flat "
                 "stone on the ground, dry grass and pebbles",
    "camp_truck": "a dusty dirt track leaving the field camp at dawn, dry grass and stones on both sides, pine hills "
                  "fading into haze, distant tents",
    "forest": "a dense dark pine forest on rocky hills at night, tall straight pine trunks, thorny scrub and "
              "limestone boulders, a faint moonlit sky between the treetops",
    "ek_door": "the arched wooden front door of a two-storey golden limestone house in Ein Karem, a green valley "
               "village of stone houses, cypress trees and a stone step, a sleeping village around it",
    "ek_room": "the warm sitting room of Hashim and Safoora's stone house in Ein Karem: arched window, low cushioned "
               "benches along the walls, woven rugs, a brass tray, an oil lamp on a carved wooden table",
    "women_room": "a beautiful spacious bedroom in a 1940s stone house in Ein Karem: clean whitewashed arched walls, a "
                  "carved wooden chest, woven rugs, folded wool blankets, simple geometric-patterned wall hangings and "
                  "a string of prayer beads on a hook (no writing, no script, no symbols), a tall arched window",
    "garden_memory": "the flowering garden of Mahmood's two-storey golden limestone house in Deir Yassin, almond and "
                     "olive trees in blossom, roses, a stone path",
}
MOOD = {
    "cave_mouth": "smoke-darkened ember day around noon, hazy amber light filtering through pines, a column of smoke "
                  "far away, overwhelming relief and tears of joy",
    "cave": "smoke-darkened ember day, warm amber daylight spilling in from the cave opening, soft shadows on the rock, "
            "fragile relief mixed with grief",
    "hillside": "smoke-darkened ember day, dusty amber haze, distant columns of smoke on the horizon, hidden and silent",
    "memory_house": "soft hazy golden dreamlike memory glow, warm oil-lamp light at night, quiet worry",
    "memory_dawn": "soft hazy golden dreamlike memory glow over a dawn blue-gold sky, dark columns of smoke rising far "
                   "below over the village, urgent fear",
    "cave_dusk": "dusk, a smoke-darkened ember-orange sky outside the cave opening, deep charcoal shadows inside, urgency",
    "cave_inner": "late afternoon, dim amber light reflected off the rock, deep shadows, grief and tenderness",
    "cave_night": "midnight, deep blue darkness, a warm oil-lamp glow and a tiny flame, tense and prayerful",
    "cave_exit": "night, deep blue darkness, the small warm glow of a single oil hand-lamp, fear and resolve",
    "camp_night": "night, deep blue-black darkness, one small orange campfire far off, cold and menacing",
    "camp_face": "night, harsh flickering orange firelight on one side of his face, the rest in deep shadow, humiliation "
                 "endured with patience",
    "camp_dawn": "sunrise, dawn blue-gold light, long soft shadows, lonely and prayerful",
    "camp_truck": "dawn blue-gold light through dust and haze, cold and uncertain",
    "forest": "night, deep blue moonlit darkness among the trunks, tiny warm oil-lamp glows, eerie and frightening",
    "ek_door": "the blue hour just before dawn, deep blue sky, warm oil-lamp light from the doorway, hope and relief",
    "ek_room": "the blue hour before dawn, warm oil-lamp glow inside, kindness and safety",
    "women_room": "night before dawn, a single small oil lamp glowing amber, deep blue shadows, sleepless grief",
    "garden_memory": "soft hazy golden dreamlike memory glow, golden-hour spring sunlight, tender love",
    "women_dawn": "dawn, soft blue-gold light from the arched window, a single small oil lamp, peaceful and prayerful",
    "women_morning": "sunrise, warm golden morning light through the arched window, exhausted peace",
}
LOC["women_dawn"] = LOC["women_room"]
LOC["women_morning"] = LOC["women_room"]

BEATS = [
    dict(to=3, reason="episode opening: the reunion at the cave mouth", chars=["fathimaa", "sahar", "hamza", "laila"],
         loc="cave_mouth",
         visual=f"at the cave mouth Fathimaa hugs her daughter tightly, eyes shut, tears of joy on her cheeks; {SAHAR}, "
                "weeping with relief in her mother's arms; Hamza in his red-and-white keffiyeh hurries towards them from "
                "the cave opening, arms reaching out; Laila in her indigo thobe and long white headscarf stands a step "
                "behind, exhausted",
         camera="medium wide, eye level, the cave opening and pines behind, the rocky ledge as a calm lower third",
         amb="hillside_smoke", sens="other",
         safe="mother-daughter hug only (bible rule 7); Sahar's injury shown only as a clean cloth sling"),
    dict(to=5, reason="scene change: inside the cave, Sahar sees her parents and brother safe", chars=["sahar", "ameen", "fathimaa", "hamza"],
         loc="cave",
         visual=f"{SAHAR}, sitting on a woven rug inside the cave with a tearful, relieved smile; her brother Ameen in "
                "his grey shirt sits beside her holding her right hand; Fathimaa in her forest-green thobe and cream "
                "headscarf and Hamza in his red-and-white keffiyeh sit facing her, Hamza resting one hand gently on top "
                "of her hijab",
         camera="medium shot, eye level, the bright cave opening blurred behind", amb="cave", sens="other",
         safe="only father (hand on head) and brother (hand held) touch Sahar (bible rule 7)"),
    dict(to=8, reason="the narrator describes the hidden cave: establishing shot", loc="hillside",
         visual="a steep pine-and-boulder hillside where the dark mouth of a cave is almost completely hidden behind "
                "trees and huge rocks; far away on the horizon thin columns of smoke rise into an amber sky; no people",
         camera="wide shot, low angle from the footpath below, the hidden cave in the upper half", amb="hillside_smoke"),
    dict(to=10, reason="emotional turning point: Hamza sees the broken arm and Fathimaa asks where the others are",
         chars=["hamza", "sahar", "fathimaa", "laila"], loc="cave",
         visual=f"Hamza, pale and stunned, looks down at his daughter's arm; {SAHAR}, her face crumpling as her voice "
                "breaks; Fathimaa beside them presses one hand to her chest, eyes wide with dread; Laila sits a little "
                "apart, trembling",
         camera="medium shot, eye level", amb="cave", sens="violence",
         safe="the deliberately broken arm is shown only as the clean cloth sling, no injury"),
    dict(to=14, reason="focus moves to Laila telling her loss; Fathimaa weeps", chars=["laila", "fathimaa"], loc="cave",
         visual="Laila in her indigo thobe and long white headscarf sits on the woven rug, her face pale and drawn, "
                "tears running down, her hands open in her lap as she speaks through sobs; Fathimaa beside her covers "
                "her face with one hand, weeping",
         camera="medium close-up, eye level", amb="cave", sens="violence",
         safe="the killing of Mahmood and Noor is only spoken of; shown only as Laila's grieving face"),
    dict(to=17, reason="focus moves to Hamza: grief for his friend, then he takes cloth from a bag", chars=["hamza"],
         loc="cave_mouth",
         visual="Hamza sits alone on a boulder at the cave mouth, head bowed, one hand pressed over his eyes in grief; "
                "in his other hand a folded piece of clean cloth taken from an open canvas bag beside him",
         camera="medium shot, slightly from the side", amb="hillside_smoke", sens="violence",
         safe="Mahmood's martyrdom shown only as Hamza's private grief"),
    dict(to=21, reason="action change: Fathimaa tends the arm while Safiyya tells her story", chars=["sahar", "fathimaa", "safiyya", "sama"],
         loc="cave",
         visual=f"Fathimaa kneels and gently adjusts the cloth sling on {SAHAR}, a copper bowl of clean water and a "
                f"folded white cloth on a rock beside them; nearby {SAFIYYA}, speaks through tears; Sama, a 12-year-old "
                "girl in a pale-blue embroidered dress and white hijab, clings quietly to her mother's arm",
         camera="medium wide, eye level", amb="cave", sens="violence",
         safe="no wounds treated on screen: a sling adjusted, a bowl of water; Sama's father's killing and the "
              "soldiers' crimes are only spoken of"),
    dict(to=24, reason="characters change: Ameen comforts his sister", chars=["sahar", "ameen"], loc="cave_inner",
         visual=f"{SAHAR}, sitting against the rough cave wall, her right hand pressed over her eyes, weeping; Ameen "
                "sits close beside her, his arm around her shoulders, speaking softly with tears in his own eyes",
         camera="medium shot, eye level", amb="cave", sens="violence",
         safe="Yazan's imagined torture is not shown; only Sahar's weeping (brother's arm around her, rule 7)"),
    dict(to=28, reason="emotional turning point: Sahar speaks of Yazan; tighter framing", chars=["sahar", "ameen"],
         loc="cave_inner",
         visual=f"close two-shot: {SAHAR}, looking at her brother with tear-filled eyes as she speaks of her husband; "
                "Ameen holds her right hand in both of his and gives a brave, tearful nod; a folded wool blanket beside "
                "them",
         camera="close two-shot, eye level, faces in the upper half", amb="cave"),
    dict(to=32, reason="time jump: Sahar wakes; Fathimaa offers bread and water", chars=["sahar", "fathimaa", "ameen"],
         loc="cave",
         visual=f"{SAHAR}, just woken, sits up against the cave wall; Fathimaa kneels beside her holding out a piece of "
                "flatbread and a small clay cup of water with a kind, tired smile; behind them Ameen sits eating a piece "
                "of bread; clay jars and cloth sacks of food stacked along the wall",
         camera="medium shot, eye level", amb="cave", transition="black"),
    dict(to=36, reason="flashback: Fathimaa tells how Hamza followed the news and prepared", chars=["hamza"],
         loc="memory_house",
         visual="Hamza sits at a low wooden table in his lamplit sitting room, leaning close to an old wooden valve "
                "radio set, a few folded newspapers with no visible writing beside him, his face deeply worried",
         camera="medium shot, slightly from the side", amb="memory", transition="dissolve", sens="other",
         safe="newspapers and books show no readable text; the political news is only a worried face"),
    dict(to=39, reason="flashback, scene change: the dawn of the attack, the family flees up the mountain",
         chars=["hamza", "fathimaa", "ameen"], loc="memory_dawn",
         visual="seen from behind, Hamza leads Fathimaa and Ameen hurriedly up a narrow rocky path between pines; Hamza "
                "glances back over his shoulder towards the village below, where dark columns of smoke rise over the "
                "golden stone houses",
         camera="wide shot from behind and below, the climbing figures in the upper half, the rocky path as the lower third",
         amb="hillside_smoke", sens="violence",
         safe="the guns and gunfire are shown only as distant smoke over the village and a muffled offscreen sound"),
    dict(to=41, reason="back to the present, dusk: Hamza returns and says they must leave",
         chars=["hamza", "laila", "safiyya", "sama"], loc="cave_dusk",
         visual=f"Hamza stands in the cave opening, a dark figure against an ember-orange dusk sky, one hand raised "
                f"urgently as he speaks; Laila in her white headscarf, {SAFIYYA}, and Sama in her white hijab and pale-blue "
                "dress, who have just come back in, turn to look at him",
         camera="medium wide, from inside the cave towards the opening", amb="cave", transition="dissolve",
         sens="violence", safe="'the whole area is burning' is only the ember sky outside"),
    dict(to=45, reason="characters change: Sahar clings to Laila, who consoles her", chars=["sahar", "laila"],
         loc="cave_dusk",
         visual="two women sit side by side on the rug just inside the cave; on the LEFT the young woman Sahar in her "
                "black thobe with deep-red embroidery and black hijab, HER OWN left forearm resting in a plain beige cloth "
                "sling, leans her head against the older woman, eyes shut, tears on her cheeks; on the RIGHT Laila in her "
                "indigo thobe and long white headscarf, with NO sling and both arms free, puts one arm around Sahar's "
                "shoulders and speaks softly with a brave, tearful face; inland wooded hills outside, no sea",
         camera="medium close-up, eye level", amb="cave", sens="other",
         safe="mother-in-law hug (rule 7); Yazan's feared torture is only spoken of"),
    dict(to=49, reason="time jump to midnight: Hamza prepares the hand-lamps", chars=["hamza", "fathimaa", "laila", "sahar"],
         loc="cave_night",
         visual=f"Hamza kneels by an open canvas bag, taking out small brass oil hand-lamps, speaking gravely in a low "
                f"voice; around him in the dark Fathimaa, Laila and {SAHAR} sit listening with bundles ready, their faces "
                "lit by one tiny flame",
         camera="medium wide, eye level", amb="cave_night", transition="black"),
    dict(to=52, reason="action change: they leave the cave by lamplight onto the rocky path", loc="cave_exit",
         visual="seven small figures in long robes and headscarves leave the dark mouth of the cave in single file, seen "
                "from behind; the first, a man in a keffiyeh, holds up a small glowing oil hand-lamp; the path ahead is "
                "huge boulders and thorny bushes; the figures are small silhouettes",
         camera="wide shot from behind, slightly high, the lamp glow in the upper half", amb="forest_night",
         sens="other", safe="the family seen only as small silhouettes from behind"),
    dict(to=56, reason="storyline cut: Yazan in the soldiers' camp at night", loc="camp_night",
         visual=f"a dark army camp seen from far away across an open field at night: a few canvas tents, one small "
                f"campfire in the middle, a few standing figures around it {SOLDIERS}; nobody on the ground is visible",
         camera="extreme wide shot from a distance, the fire in the upper half, dark dry grass as the lower third",
         amb="army_camp_night", transition="black", sens="violence",
         safe="the neck chain and being tied 'like a dog' are never shown (rule 4): only the camp from a distance and "
              "an offscreen chain rattle"),
    dict(to=59, reason="focus moves to Yazan: humiliation endured, then Fajr prayer", chars=["yazan"], loc="camp_face",
         visual=f"close-up of {YAZAN_P}; his face half in shadow and half in flickering firelight, head slightly bowed, "
                "eyes closed, lips moving silently in dua; his face clean, calm and enduring",
         camera="close-up, eye level, his face in the upper half", amb="army_camp_night", sens="violence",
         safe="the soldier urinating on him is never shown (rule 4): only his closed eyes and silent dua"),
    dict(to=61, reason="time change: sunrise, his dua and the 'breakfast' of two olives", chars=["yazan"], loc="camp_dawn",
         visual=f"{YAZAN_P}, sitting on the ground seen from the side, both hands raised before his chest in dua, eyes "
                "closed; beside him on a flat stone lie just two olives and a tiny bottle cap of water",
         camera="medium wide side view, eye level, the flat stone in the lower part", amb="army_camp_dawn", sens="violence",
         safe="no chains, no wounds; the deprivation is shown only as two olives and a capful of water"),
    dict(to=65, reason="action change: the lorry takes him away", loc="camp_truck",
         visual="an old 1940s army truck with a closed canvas-covered wooden cargo bed, seen from behind, driving away "
                "down a dusty dirt track at dawn, a trail of dust behind it; no markings, no people visible",
         camera="wide shot from behind, the truck in the upper half, the dusty track as the lower third",
         amb="army_camp_dawn", sens="violence",
         safe="the animal cage and loading him into it are never shown (rule 4): only the closed truck from behind"),
    dict(to=67, reason="storyline cut back to the family walking through the forest at night", loc="forest",
         visual="deep in a dark pine forest seven tiny figures in long robes and headscarves walk close together in a "
                "line between tall trunks and thorny scrub, small silhouettes from a distance, two tiny oil-lamp glows "
                "among them",
         camera="extreme wide shot, low angle, the lamp glows in the upper half, dark rocks as the lower third",
         amb="forest_night", transition="black"),
    dict(to=70, reason="scene change: Ein Karem near dawn, the door opens", chars=["hashim", "hamza", "laila", "sahar"],
         loc="ek_door",
         visual=f"the arched wooden door stands open; Hashim with his round glasses and white beard, in his tweed jacket, "
                f"holds up an oil lamp in the doorway, surprised and kind; Hamza in his red-and-white keffiyeh stands on "
                f"the step before him; behind Hamza wait Laila in her white headscarf and {SAHAR}, exhausted",
         camera="medium wide, eye level, from the side of the step", amb="night_exterior"),
    dict(to=73, reason="scene change: inside, Safoora brings water and dates", chars=["safoora", "hashim", "laila", "sahar"],
         loc="ek_room",
         visual=f"in the lamplit sitting room Safoora in her olive-green embroidered thobe and white headscarf offers a "
                f"brass tray with cups of water and a plate of dates to Laila and {SAHAR}, who sit on a cushioned bench; "
                "Hashim stands behind, gesturing kindly for them to rest",
         camera="medium shot, eye level", amb="stone_house_night"),
    dict(to=75, reason="scene change: the women's room; everyone rests but Sahar cannot sleep",
         chars=["sahar", "laila", "fathimaa", "safiyya"], loc="women_room",
         visual=f"in the lamplit women's room the women sit asleep against the whitewashed wall under wool blankets, "
                f"heads resting back, every hijab and headscarf fully on: Laila, Fathimaa and {SAFIYYA}; at the end of "
                f"the row {SAHAR}, sits awake, eyes open, staring into the lamplight",
         camera="medium wide, eye level", amb="stone_house_night", sens="clothing",
         safe="sleeping women shown sitting against the wall, fully covered, never lying in a bed (rule 5)"),
    dict(to=77, reason="memory: Sahar remembers Yazan", chars=["sahar", "yazan"], loc="garden_memory",
         visual="a golden memory: Sahar in her black thobe with deep-red embroidery and black hijab (no sling, before "
                "her injury) walks side by side with Yazan, tall with curly black hair and his black-and-white keffiyeh, "
                "along the stone path of the flowering garden, exchanging a shy smiling glance; they do not embrace",
         camera="medium wide, eye level, the couple in the upper half, the stone path as the lower third",
         amb="dream_glow", transition="dissolve", sens="intimacy",
         safe="'his caresses' and 'his manly body' are replaced by the couple walking side by side at golden hour "
              "(bible rule 6)"),
    dict(to=79, reason="back from the memory: Sahar alone with her empty hand; the Fajr call", chars=["sahar", "laila"],
         loc="women_room",
         visual=f"close shot: {SAHAR}, sitting against the wall, gazes at her own open right palm in the amber lamplight, "
                "a tear on her cheek; beside her Laila sleeps sitting under a blanket, white headscarf on",
         camera="medium close-up, eye level, her face and hand in the upper two-thirds", amb="stone_house_dawn",
         transition="dissolve", sens="intimacy", safe="the longing for her husband shown as her empty hand (rule 6)"),
    dict(to=81, reason="action change: Sahar prays Fajr", chars=["sahar"], loc="women_dawn",
         visual=f"{SAHAR}, seated on a simple prayer mat facing the arched window with the first blue-gold dawn light, "
                "her right hand raised in dua, head bowed; the other women are still covered shapes sleeping against the "
                "wall in the background",
         camera="medium wide, from behind and slightly to the side", amb="stone_house_dawn", sens="other",
         safe="prayer shown respectfully, no text; the bathroom/wudu is not shown"),
    dict(to=83, reason="action change: sunrise, Sahar finally sleeps beside Laila", chars=["sahar", "laila"],
         loc="women_morning",
         visual=f"{SAHAR}, asleep sitting against the wall under a wool blanket beside Laila, her black hijab still fully "
                "on, her head resting against the wall, eyes closed and swollen from crying; Laila asleep beside her in "
                "her white headscarf; warm sunrise light across them from the window",
         camera="medium shot, eye level", amb="stone_house_dawn", sens="clothing",
         safe="removing her 'burqa' (face veil) is not shown: her black hijab stays fully on (bible rule 5)"),
]

S = {}
def sh(i, en, sfx=(), **opt): S[i] = (en, list(sfx), opt)

sh(1, "\"Subhanallah! Hamza... Hamza! There is my Sahar... safe... my child!\" Fathimaa burst into tears.",
   [("sob_breath", "ރޮވޭ", -22)])
sh(2, "When she saw Sahar and the others at the mouth of the cave, Fathimaa felt emotions she could not describe.")
sh(3, "She ran and threw her arms around Sahar, holding her tight. Behind her Hamza came and hugged Sahar too. And after greeting Laila and the others,",
   [("footsteps_sand", "ބާރުބާރަށް", -22), ("cloth_rustle", "ބައްދާ", -22)])
sh(4, "he asked everyone to sit. Inside the cave, seeing her mother, her father and her little brother Ameen safe, Sahar's heart filled with joy.")
sh(5, "That shattered heart found some kind of relief. It was a large, spacious cave, a place bound up with many of Sahar's childhood memories.")
sh(6, "Thanks to the trees and big rocks, the cave was so well hidden that someone walking below could not see it.")
sh(7, "It was a fitting place to hide in a situation like this. Hamza and Fathimaa too were overcome with sudden astonishment.")
sh(8, "They had not expected to find Sahar alive, because they had heard that the fighters first attacked the houses in the area where Sahar's family lived.")
sh(9, "\"Did my child's arm break?\" Hamza asked, turning pale. \"It didn't break... it was broken...\" Laila said in a trembling voice. \"Where are the others?",
   [("sob_breath", "ތުރުތުރު", -24)])
sh(10, "Mahmood, Noor... where is my child Yazan?\" Fathimaa asked, a hand on her chest. \"Mother...\" Sahar's voice broke.",
   [("gasp", "ބެދޭގޮތްވިއެވެ", -22)], hum=True)
sh(11, "Anyone who saw Laila's drawn face could feel the grief she was going through.")
sh(12, "How could one ever describe Laila's grief for her beloved husband and her two children?", hum=True)
sh(13, "Yet she gathered her courage and began to speak, weeping and sobbing. The story they were hearing",
   [("sob_breath", "ގިސްލަމުން", -22)])
sh(14, "shook Hamza and Fathimaa deeply. \"If only this were a nightmare...\" Fathimaa said, crying, her hand over her face.",
   [("sob_breath", "ރޮމުން", -24)])
sh(15, "When he learned that his closest friend Mahmood and his child had been martyred and that his son-in-law was missing,",
   hum=True)
sh(16, "Hamza felt something he could not put into words. But he kept telling himself that he had to stay strong for his family.",
   [("sigh", "ވިސްނައިދެމުންނެވެ", -22)])
sh(17, "Gathering his courage he stood up, took a piece of cloth from a bag, and tried to give Sahar's arm some kind of treatment.",
   [("cloth_rustle", "ފޮތި", -20)])
sh(18, "Wiping her tear-filled eyes, Fathimaa too steadied herself and, together with Hamza, tried to tend to what Sahar and Safiyya had suffered.")
sh(19, "And Safiyya and Sama explained their story too. How Sama's father was killed, and the cruel fighters entered that house")
sh(20, "and committed their crimes. Safiyya told it weeping and sobbing. How, at a brief chance, they jumped over the wall",
   [("sob_breath", "ގިސްލަމުން", -24), ("soft_thud", "ފުންމާލައި", -22)])
sh(21, "and mother and daughter escaped, she told with deep emotion. Ameen meanwhile kept trying to calm Sahar. Massaging Sahar's head,")
sh(22, "he urged her to be strong. \"God willing, Yazan bebe will still come... I'm here with you, dhaththa... I'll look after you...\"")
sh(23, "Ameen too broke into tears. \"Now try to get some sleep... you're so worn out,\" Ameen said tenderly. \"How can I sleep...",
   [("sob_breath", "ރޮވޭ", -24)])
sh(24, "Even when I close my eyes I see them torturing Yazan... I don't even know what state that poor man is in,\" Sahar said, lying with her hand over her face, crying.",
   [("sob_breath", "ރޮމުން", -24)])
sh(25, "\"Kokko! How will I live without Yazan? We grew up together since we were little, always together...")
sh(26, "every memory I have is tied to Yazan... such a loving, kind, good husband he is... I will miss him so much, kokko!\"",
   hum=True)
sh(27, "Sahar said, weeping. \"Bebe will come... he'll come very soon... bebe will be very strong... inshaAllah. Don't lose hope...\"")
sh(28, "Holding Sahar close, Ameen kept encouraging her. After a while had passed like that, worn out as she was, Sahar fell asleep.",
   [("cloth_rustle", "ބައްދާލާ", -24)])
sh(29, "She did not know how the time went by. Sahar woke when Fathimaa called her. Ameen was sitting eating a piece of bread. \"You should eat something, my child?\"")
sh(30, "Fathimaa said tenderly. \"Where is Yazan's mother?\" Sahar asked, not seeing Laila. \"Mother went outside here to relieve herself.")
sh(31, "Safiyya dhaththa went with mother too,\" Fathimaa said, handing her a piece of bread and a cup of water. \"Did you have time to get ready, mother?",
   [("cup_clatter", "ތައްޓެއް", -22)])
sh(32, "I ask because food and water have been brought here,\" Sahar asked, wanting to understand.")
sh(33, "\"Your father had been watching what the Jewish fighters were doing closely. His work was listening to the radio and reading books, newspapers and magazines.")
sh(34, "Whenever he went to the market he would buy lots of food... When I asked, he'd say he feared we might have to leave this area.")
sh(35, "That we must always stay alert. And he always said, very sadly, that even when he told Mahmood this, Mahmood wouldn't believe it, that he called it a false suspicion,")
sh(36, "that they would never come and overpower us. Since he heard Mahmood was martyred, your father has been so heartbroken,\" Fathimaa went on, her head bowed.",
   [("sigh", "ދެރަވެފަ", -22)])
sh(37, "\"This morning, after going to the Fajr prayer, your father came back and said it's not going well, he had seen a group coming with guns.")
sh(38, "Let's get ready and go and fetch Sahar's family, he said. He even had the car ready; just as we were about to leave, gunfire started from the direction of your house.",
   [("distant_shots", "ބަޑީގެ", -24)])
sh(39, "As we climbed the mountain to flee, your father said, 'If my Sahar is safe, she will come this way.'\" Just as the story reached this point, Laila, Safiyya and Sama came back into the cave.",
   [("footsteps_sand", "ވަދެފިއެވެ", -22)])
sh(40, "Behind them Hamza came in and said in a low voice: \"Everyone get ready! There's no shelter left for us in this area.")
sh(41, "The whole area is burning to ashes. Let's escape over the mountain and get away from here... we must be gone from here before sunrise...",
   [("fire_crackle", "އަނދާ", -24)])
sh(42, "There's no safety here anymore.\" Hamza broke into tears. \"We'll never see Yazan again, will we? The humiliation those evil men will make that poor man suffer,",
   [("sob_breath", "ރޮވޭ", -24)])
sh(43, "the torture they'll do to him - every time it comes to my mind my heart trembles,\" Sahar said, holding Laila tight. \"Be strong, my child...",
   [("cloth_rustle", "ބައްދާލަމުން", -24), ("heartbeat", "ރޫރޫ", -20)], hum=True)
sh(44, "This is what was decreed for today... all we have is patience... you are my hope... the greatest strength I have to go on living...")
sh(45, "you are a mercy Allah has given... whatever happens, I'll be with you...\" Laila tried to give Sahar some strength.")
sh(46, "Hamza waited until midnight. He knew that at midnight the fighters' activity would slow down.")
sh(47, "And Hamza knew by heart the paths from the mountain area into the dense forest.")
sh(48, "The danger and insecurity of the path they were about to take were enormous. He urged everyone to be patient")
sh(49, "and to draw strength from dua and dhikr. Then he set about lighting the hand-lamps he had brought in a bag.",
   [("cloth_rustle", "ދަބަހަކަށް", -22)])
sh(50, "With the fire they had lit by heating two sticks of wood to light the cave, he lit the lamps, and with Hamza in front, everyone left the cave.",
   [("fire_crackle", "ރޯކޮށް", -22), ("footsteps_sand", "ނިކުތެވެ", -22)])
sh(51, "Thinking of the length of the road ahead on foot and how hard it would be, everyone was gripped by fear.")
sh(52, "They went forward slowly along a path full of big rocks and thorny trees. Hamza's aim was to leave the area where they had lived",
   [("stone_scrape", "ހިލަތަކާއި", -22), ("leaves_rustle", "ގަސްތަކުން", -22)])
sh(53, "and reach Ein Karem. Yazan woke to the sound of people talking. They were not speaking a language Yazan knew.",
   [("breath", "ހޭލެވުނީ", -24)])
sh(54, "Exhausted as he was, Yazan begged them for a drop of water. Yazan lay beside a fire in the middle of the field,",
   [("fire_crackle", "އަލިފާންގަނޑެއް", -24)])
sh(55, "a chain put around his neck, tied up the way a wild dog is tied. That he be saved from the evil deeds of these cruel men,",
   [("chain_rattle", "ޗޭނުގަނޑެއް", -22)])
sh(56, "and that his beloved wife and mother be kept safe, Yazan prayed without stopping. When he had called out for a drop of water many times,",
   hum=True)
sh(57, "one of the fighters there came over to Yazan and urinated on his face. After that,",
   [("footsteps_sand", "އައިސް", -22)], hum=True)
sh(58, "he said in English, \"Now you'll have had your fill of water,\" and walked away. There was no other way today but to be strong. Even in that state Yazan did not miss his prayer.")
sh(59, "Since his hands and feet were not tied, with great difficulty he did tayammum and prayed Fajr sitting where he was. Even while he was praying, now and then one of the fighters would come",
   [("cloth_rustle", "ތަޔައްމަމު", -24)])
sh(60, "and cause Yazan some kind of trouble. And so the sun rose. Calling it breakfast,")
sh(61, "they brought him just two olives and a drop of water in the cap of a water bottle.",
   [("stone_scrape", "ގެނެސްދިނެވެ", -24)])
sh(62, "After that they brought an iron cage of the kind used to carry animals like lions, put Yazan inside it, and loaded it onto a big lorry.",
   [("metal_gate", "ކޮށިގަނޑު", -22), ("truck_start", "ލޮރީއަކަށް", -18)])
sh(63, "When the chain around his neck was taken off, Yazan felt some kind of relief.",
   [("chain_rattle", "ޗޭނުގަނޑު", -22)])
sh(64, "But wondering what kind of terror lay ahead of him, Yazan was deeply anxious.")
sh(65, "Yet deep in his heart Yazan believed that Allah the Exalted does not decree evil for any of His servants.")
sh(66, "From among the dense trees the calls of different animals could sometimes be heard. The darkness all around filled their hearts with dread.",
   [("leaves_rustle", "ގަސްތަކުގެ", -22)])
sh(67, "They all stayed together. Picking out the thorny bushes and keeping clear of them, walking very slowly,",
   [("footsteps_sand", "ހިނގަމުން", -22)])
sh(68, "by the time Hamza and the others reached Ein Karem it was close to Fajr. The whole area was asleep and silent.")
sh(69, "Hesitantly they knocked at the door of the first house they saw, and after a while it opened. When the people of the house saw Hamza and the others, they realised these were people in distress because of the war.",
   [("knock", "ޓަކި", -16), ("door_open", "ހުޅުވައިފިއެވެ", -18)])
sh(70, "Because Ein Karem is very close to Deir Yassin, the news of the attack had already reached Ein Karem.")
sh(71, "So instead of asking what had happened, they began to help at once. Giving them water and things like dates,",
   [("pour", "ފެނާއި", -22)])
sh(72, "they kept urging them to calm down and rest. Sahar and the others had come to the house of a very good couple.")
sh(73, "Only that middle-aged couple lived in the house. They gave Hamza and Ameen a room of their own, and Sahar and all the women another.")
sh(74, "It was a beautiful, spacious, modern room. Religious emblems were hung in different places around the room.")
sh(75, "When everyone lay down to sleep, Sahar too tried to sleep. But sleep would not come. Even with her eyes closed she saw yesterday's scenes.",
   [("cloth_rustle", "އޮށޯތުމުން", -24)])
sh(76, "Of all those painful memories, the ones that hurt Sahar most were her memories of Yazan: his passionate caresses and his tender words.")
sh(77, "Every time she closed her eyes, she pictured Yazan's manly figure, his thin handsome beard and those striking eyes.",
   hum=True)
sh(78, "All Sahar could do was pray to Allah the Exalted, strengthen her certainty in Him, and renew her hope of meeting her beloved husband again.")
sh(79, "As she lay tossing and turning, the call to the Fajr prayer was heard. A while earlier Laila's sobbing could be heard, but now Laila too had fallen asleep.",
   [("cloth_rustle", "ފުރޮޅި", -24)])
sh(80, "Sahar quietly got up, went to the washroom, made wudu, came back and prayed Fajr, and spent the time until sunrise in dua and dhikr.",
   [("water_splash_small", "ވުޟޫކޮށްގެން", -22)])
sh(81, "Worn out and heavy with exhaustion, everyone except Sahar was asleep.")
sh(82, "From weeping and weeping through her dua, Sahar's eyes were swollen. And feeling a great heaviness, she took the veil off her head,",
   [("sob_breath", "ރޮއެ", -24)], hum=True)
sh(83, "and Sahar too lay down beside Laila. Before long, sleep came.",
   [("breath", "ނިދޭ", -24)])
SHOTS = S

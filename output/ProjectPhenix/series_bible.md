# Project Phenix (ޕްރޮޖެކްޓް ފީނިކްސް) — series bible

Dhivehi audio crime thriller. This batch has seven episodes that form ONE complete arc, in this order:
**311 → 318 → 320 → 321 → 322 → 323 → 324** (311 = part 1, 324 = the finale, ends "ނިމުނީ"). Each episode opens
where the previous one ended. Every episode's cover (`work/episode-<N>-cover.png`) is the same series poster: a police
officer in a dark-navy uniform seen from behind on the bow of a fast launch at night, looking at a dark jungle-covered
deserted island under a starry navy sky. Match that look (see `style.txt`).

Time span: about one week for 311–324's main action (night → morning → night…), plus a three-weeks-later epilogue at
the end of 324.

## Characters (series cards in `output/ProjectPhenix/characters/`, see `refs_sheet.jpg`)
| id | who |
|---|---|
| `ashham` | Ashham (އަޝްހަމް), ~38, Serious Crimes Department's best investigator. Default: dark-navy long-sleeved police field shirt, navy trousers. Outfit changes: 318 = a long black raincoat over his shirt in the Malé rain; 320 = plain civilian clothes ("dressed like ordinary people": a dark-grey long-sleeved shirt and dark trousers) — keep this look through 320–322 (dusty, damp, never torn); 322 end/323 = police uniform with a navy police cap and dark sunglasses as disguise, then 323 cap and glasses off; 324 = black tactical jacket on the coast-guard launch; 324 epilogue = formal navy dress uniform with a gold medal on his chest. |
| `habeeb` | Habeeb (ޙަބީބު), ~28, digital-forensics/data analyst, glasses, laptop/tablet always. **The narrator sometimes calls him "Zayaan" (ޒަޔާން) — it is the same person, always use `habeeb`.** 322 end/323: police uniform + cap + sunglasses disguise (describe it in `visual`). 324 epilogue: formal navy dress uniform with a gold medal. |
| `moosa` | Moosa Thaahir (މޫސާ ޠާހިރު), ~62, Malé tycoon, Naail's father. (311 once calls him "Qaasim" — same man.) |
| `naail` | Naail Moosa (ނާއިލް), ~25, Moosa's son, the murder victim. NEVER shown dead. Only alive: a framed photo on Moosa's table, a dim memory/flashback (on a dhoni at night on the satellite phone in 318), or a silhouette. |
| `kalhe` | Kalhe (ކަޅޭ), ~40, Black Wolf gang leader, Maafannu (318 only). |
| `raniya` | Dr. Raniya (ރާނިޔާ), ~28, chief surgeon of the GA. Villingili atoll hospital. White coat at the hospital (320); after the escape (320 from the dinghy on, 321, 322) she is WITHOUT the white coat: dusty-blue dress + navy hijab, damp but opaque. 324 epilogue: soft cream dress, navy hijab, on Hulhumalé beach. |
| `raniya_father` | Raniya's father, ~62, captive in the isolation ward (321–322). Weak, pale-grey patient clothes. 324 epilogue: healthy, white long-sleeved shirt and a dark sarong, sitting on a bench. |
| `fairooz` | Assistant Commissioner Fairooz (ފައިރޫޒް), ~52, Ashham's boss, the villain in Malé. Navy dress uniform. In the 321/323 lab video he wears a black coat (shown only as a dark figure on a blurred screen). |
| `faahid` | Faahid (ފާހިދު), ~62, retired Commissioner, Ashham's ally (322–324). Olive shirt; in 323–324 field operations a black tactical jacket over it; 324 epilogue: the new Commissioner's navy dress uniform. 324: his shoulder wound is shown ONLY as him holding his shoulder, grimacing; epilogue: a plain white arm sling. |
| `naasir` | Naasir (ނާޞިރު), ~46, head of police Internal Affairs, secretly the Minister's man (323–324). Black suit. |
| `saleem` | Home Minister Mohamed Saleem (މުޙައްމަދު ސަލީމް), ~60 (323–324). Black three-piece suit. Never shown smoking. |
| `vance` | Dr. Vance (ޑޮކްޓަރ ވެންސް), ~66, the foreign scientist who owns Project Phenix (324 only). Elderly European, black overcoat. |

People without cards (describe them in `visual` only, never in `chars`): the four fishermen of the dhoni "Kalaminja"
in 311 (Hassan — older, grey stubble, faded blue long-sleeved shirt and sarong; Sameeru the cook; Ibrahim; Ali — all
weathered fishermen in long-sleeved shirts and sarongs/trousers), the launch captain, police officers, MNDF soldiers
(black combat gear, helmets, EMPTY hands or flashlights / riot shields only), masked guards (black clothes, black face
masks, empty hands or flashlights), the gang youths in 318, journalists and TV crews, a security guard, the cargo-ship
crew, the boat captain friend (320).

## Places (copy into `LOC`; keep consistent)
- `dhoni_sea` — a traditional Maldivian fishing dhoni on open sea off a deserted island at sunset/night.
- `kandu_island` — **Kandu-huttaa** (ކަނޑުހުއްޓާ), a deserted uninhabited island in Huvadhu (Gaafu Alifu) atoll: white sand
  beach, dense dark jungle of screwpine, magoo bushes, coconut palms, mangrove-like tangles reaching the water; no path,
  no people. The bunker door: a heavy rusted steel hatch-door set in a low concrete block in the ground among the bushes,
  first hidden under dry palm fronds.
- `bunker_corridor` — long concrete corridor underground, wall-mounted fluorescent tubes, cold flat light, pipes along
  the ceiling.
- `bunker_lab` — hall ringed by small glass-walled rooms with hospital beds behind frosted glass, monitors, steel
  consoles; cold blue-white light; red emergency lights when the alarm goes (321).
- `isolation_ward` — big white room with medical machines and tall glass tanks glowing with murky green liquid (nothing
  visible inside), one hospital bed in the corner.
- `vent_shaft` — narrow dark metal ventilation duct, torchlight / tablet glow only.
- `police_office` — Serious Crimes Department office in Iskandhar Building, Malé: desk with empty coffee cups and file
  stacks, computer, window to a busy street (Ameenee Magu).
- `moosa_mansion` — Moosa's luxurious living room: marble floor, big sofas, dark wood, warm lamps.
- `sea_launch` — police fast launch "Sea Hawk" at speed at night/dawn; cabin with windows, forensic cases.
- `male_alley` — narrow rain-soaked Malé alley off Majeedhee Magu, an old two-storey building with a dark doorway.
- `gang_den` — dark room inside the old building, a big table with papers, one bare hanging lamp.
- `car_rain` — a car on rainy Malé / Sinamalé bridge at night; headlights, rain on the windscreen.
- `safehouse` — secret police safe-house room in Hulhumalé: dark, rain and thunder outside, lit only by the blue glow
  of Habeeb's laptop.
- `cargo_boat` — a cargo supply boat travelling south at dawn/dusk; deck with crates.
- `villingili_harbour` — Villingili island harbour at 9 pm under dim lamps; dark island lanes.
- `atoll_hospital` — two-storey island hospital at night: empty corridor, Dr. Raniya's office (desk, files, window).
- `old_jetty` — an abandoned old jetty on the island's west shore at night in rain; a small fibreglass dinghy hidden in
  bushes.
- `storm_sea` — a small dinghy on a stormy black sea, huge waves, a distant searchlight.
- `kandu_beach_night` — Kandu-huttaa beach at night after the explosion: smoke, embers glowing far behind the trees,
  a small driftwood fire under big trees.
- `launch_cabin` — the captured big twin-engine launch "Eagle Speed" at night: wheel, glowing navigation screen
  (no readable digits).
- `fairooz_office` — top-floor office in police headquarters: big desk, leather chair, a large wall screen.
- `hulhumale_shore` — a quiet dark stretch of Hulhumalé's shore at 3 am, few street lights.
- `faahid_flat` — Faahid's modest fourth-floor Hulhumalé flat: living room, a desk with a computer.
- `police_hq` — Shaheed Hussain Adam Building (police headquarters), Malé: exterior with a crowd of journalists; inside:
  corridors, the press hall (podium, rows of journalists, TV cameras, a big screen), the server room (tall server
  racks, blinking lights).
- `minister_office` — the Home Minister's luxurious office: huge desk, tall leather chair, heavy curtains.
- `warehouse` — a big dark empty warehouse, one hanging lamp over a steel chair, a huge steel door.
- `dhoonidhoo_cell` — a bare cell in Dhoonidhoo detention centre: concrete walls, a steel bunk, a barred window.
- `coastguard_launch` — MNDF coast-guard launch on a rough night sea under black clouds; cockpit with screens.
- `cargo_ship` — the cargo ship "MV Orion": huge dark steel ship at night, stacked containers, dim deck lights, a crane;
  the red container with an electronic lock; inside: cold racks of glowing blue vials.
- `commissioner_office` — the new Commissioner's office, bright day, flags and polished wood (324 epilogue).
- `hulhumale_beach` — Hulhumalé beach in golden late afternoon, calm waves (324 epilogue).

## Episodes
- **311** — Sunset off the deserted island Kandu-huttaa, Huvadhu atoll; the dhoni "Kalaminja" rocks gently; red clouds.
  Hassan at the bow spots a big black thing floating; Sameeru slows the engine; Ibrahim and Ali come forward ("rubbish
  from a resort, leave it"); Hassan: fish are circling it, there's a strange smell; he pulls it in with a hooked pole.
  It is a big black bundle of plastic bags wrapped in black tape, unnaturally heavy, terrible smell; four men haul it
  aboard. Hassan cuts the tape; the smell; Ali vomits over the side (NOT shown — show him turned away at the rail).
  Inside: a human body, tortured, wounds on the neck (NEVER shown — see rules). Sameeru: "Ya Rabbi! Call the police,
  switch on the set!" Darkness falls over the sea. — MALÉ, Iskandhar Building: Ashham at his desk in the Serious Crimes
  office (empty coffee cups, unfinished files, traffic noise from Ameenee Magu). Habeeb enters: a message from the
  southern command — a man found dead near a deserted island in GA, brutally tortured, a "message killing". Ashham: where
  is the body? Being taken to Villingili; HQ wants Ashham to handle it because of a tattoo on the back: Habeeb shows a
  photo on his tablet — a black phoenix tattoo (show ONLY a black phoenix emblem on a tablet screen, see rules). Ashham
  recognises it: Naail Moosa, younger son of tycoon Moosa Thaahir — Malé nightlife, car races, suspected drugs. Missing
  a week; his father spent money searching everywhere. Habeeb: "This is no gang fight; there's a big secret behind it."
  Ashham: prepare the trip, gather Naail's medical and criminal records, we leave tonight. — MOOSA'S MANSION: luxury;
  inside it a broken father on the sofa, head bowed. "Is it really him?" Ashham: DNA pending, but the tattoo matches.
  Did Naail get into trouble? Moosa: always with bad friends; two weeks ago he was frightened, said he'd found out a big
  secret, "they are in Malé too"; "find the people who killed my son, I'll make any sacrifice" (weeping). Ashham puts a
  hand on his shoulder (men — allowed). The killing was a warning: say nothing, touch nothing, reveal nothing. — 2 am:
  the fast police launch "Sea Hawk" leaves Kooddoo (team flew to Kooddoo airport) towards Kandu-huttaa; rough sea;
  Ashham and Habeeb silent beside forensic cases; backup team and soldiers on standby. Habeeb (laptop): Naail's phone
  went dead in Malé a week ago; before that he called numbers on southern islands, most often the atoll hospital's
  number — but that island's systems are blocked. Ashham looks out the window into darkness: the most dangerous case of
  his life. Captain: half an hour to Kandu-huttaa. Ashham: first the island, where the fishermen found the body. — DAWN:
  golden light; Sea Hawk enters the lagoon; beautiful but eerily silent island; white beach; dense jungle; no path, no
  people. Ashham, Habeeb with forensic kits step ashore; extra police and two soldiers (no weapons visible). East side,
  where the bundle floated. Ashham walks the sand: big boot prints from the bushes, some barefoot prints; nearby a black
  oil stain — "launch engine oil" (Habeeb rubs sand between two fingers). Dried blood on branches (show only DARK
  stains on leaves is NOT allowed — show Ashham bagging a broken twig into an evidence bag). "He was killed here — this
  is the crime scene." Into the jungle; a hidden spot: palms bent and tied; Ashham cuts the cords; a pile of dry fronds
  ("a rubbish pit?" "On a deserted island? Clear it!"). Under the sand: a heavy steel door — a concrete underground bunker
  entrance with a big padlock. "A bunker on a deserted island?" "This is where a huge crime is run — Naail's secret."
  Then the roar of a fast launch approaching; Ashham, Habeeb and the police hide in the bushes; someone knows the police
  came and is coming after them. (to be continued)
- **318** — The team must return to Malé at once; the launch sound was someone watching the police; plans change. The
  island is monitored secretly. Forensics confirm the body is Naail. Malé's political and business circles are uneasy.
  Noon, heavy rain in Malé; Ashham in a black raincoat in a narrow alley off Majeedhee Magu; Habeeb behind him: Naail's
  bank accounts paid big sums to the Maafannu 'Black Wolf' gang; blackmail or drugs? Their leader 'Kalhe' won't talk
  easily. A dark alley; at the door of an old building two young men (gang members; NO cigarettes, NO tattoos shown)
  start walking off; Ashham shows his card: "I'm here to see Kalhe, about Naail's death." Their faces change; they let
  him in. — GANG DEN: dark; through two or three doors into a room; at a big table, Kalhe (~40, scarred face) reading
  papers. "Ashham — the famous investigator." Ashham leans on the table with both hands: Naail paid you big sums.
  Kalhe (lights a cigarette — NOT shown): Naail wanted a secret shipment from abroad protected; we only got it out of
  Malé port from a container. Drugs? "No! Medical supplies, labelled as something else, to go to GA. Kandu-huttaa."
  Habeeb: so Naail was part of the secret lab. Kalhe: yes, but he got scared — said what they do is against humanity —
  wanted to stop it; two days later he vanished. "We don't kill people, not like that; that's someone far more powerful."
  — OFFICE: Habeeb hacking port and customs records: three weeks ago a big container imported in the name of Moosa
  Thaahir's company, "medical equipment"; signed by Naail using Moosa's name; then taken to a Hulhumalé area. Moosa is
  hiding something. Naail's calls to the atoll hospital: Dr. Raniya, chief surgeon (Habeeb shows her photo on screen —
  a woman's portrait in the screen is OK, no text). Everything points to that atoll; Malé plans it, the atoll runs it.
  — CAR CHASE: they drive to the Hulhumalé warehouse in the rain; a black van with its lights off follows; Ashham speeds
  up; on Sinamalé bridge the van rams the car (show only the van's dark shape close behind in the mirror / headlights
  glare, then the van stopped askew against the bridge rail behind them — no crash impact, no injured people); Ashham
  swerves and saves the car; Habeeb signals for backup; the van loses control, hits the bridge railing; Ashham drives on;
  backup arrives at the crashed van. "They have people inside the police; they know our moves." — Lonely Hulhumalé spot:
  Habeeb trembling: "Yes I'm scared, but I won't give up; justice." "Malé isn't safe; tonight we go to GA to meet
  Dr. Raniya." Ashham texts Moosa: "Naail's secrets start with your company. Reveal the truth." No reply. This is an
  international network. — SAFE HOUSE (Hulhumalé, second phase): heavy rain, thunder; only the blue glow of Habeeb's
  laptop. "They monitor all our official channels; but in Naail's iCloud backup I found an encrypted audio file — a
  satellite-phone call 24 hours before his death." Ashham hangs his wet coat on a chair: "Play it." Sea waves; a young
  frightened woman's voice: "Naail! Where are you?" Naail: "On a dhoni near Kandu-huttaa… Raniya, I didn't believe you,
  but tonight I went in… what horrible thing are they doing in that bunker?" (show Naail alive on a dark dhoni at night
  holding a satellite phone, frightened — a memory, `transition="dissolve"`). Raniya: "Get out now! If they know, they
  won't let you live. It's not just drug testing… they're using humans…" "My father — they hold my father hostage; I do
  this because I'm forced. Do you know who's behind this among Malé's big people? It's…" A door bursting open, a gunshot
  (sound only: soft_thud / door_slam), Naail's cry, the call cuts. Silence in the room. Ashham: Dr. Raniya is forced to
  help the island's experiments because her father is a hostage. Habeeb: human drug testing — an international crime.
  "They cut out his tongue to keep the secret" (NEVER shown). "We go to the atoll now to meet Raniya; she has the bunker
  information." "Officially they'd know." "We'll go on an ordinary boat, secretly. Bring your gear. No time." (to be
  continued)
- **320** — Dawn, a cargo boat from Malé's north harbour; Ashham and Habeeb as secret passengers (the captain is
  Ashham's old friend). Habeeb on a satellite modem tracking Raniya: on duty at the hospital, many calls from unknown
  numbers around her — her guards. "She's in a locked cage; only if we save her do we get the truth." Silent voyage;
  a storm brewing. — Next night 9 pm, GA. Villingili harbour, dim lamps; in ordinary clothes they walk dark lanes to the
  hospital (two-storey, very quiet). Emergency door; Habeeb keeps watch; Ashham knocks on the door with Raniya's name
  (no readable nameplate). "Come in." He enters, locks the door. Raniya at her desk with files, frightened: "Who are you?
  Get out!" She stands. Ashham shows his police card: "Serious Crimes. Naail's murder — and to save your father." She
  cries, sinks onto a chair. Habeeb: "We have Naail's call recording." Raniya, face in hands: "They killed Naail. I told
  him not to get involved; they have no mercy." She explains: Kandu-huttaa hides a foreign pharmaceutical company's
  secret lab making a new 'master drug', tested on foreigners smuggled into the Maldives — human trafficking; Naail found
  out because the shipments came through his father's company. "Who's the mastermind in Malé?" — suddenly every light in
  the hospital goes out; "backup power cut too!" Heavy boots and guns being loaded in the corridor (sounds only). Raniya
  screams. Ashham: open the window! He holds the door; it bursts open — three masked armed men (show three dark masked
  silhouettes in the doorway with flashlights, empty hands/no guns visible). A rifle butt hits Ashham's forehead (NOT
  shown). — In the darkness Ashham falls; a masked man grips his collar (NOT shown — show the dark room, flashlight beams,
  Raniya and Habeeb pressed against the wall side by side, NOT touching). Ashham, experienced, spots a heavy metal file
  holder on the desk; strikes; a gun drops; he tackles the second man; Habeeb pulls Raniya out of the door (show them
  running side by side down a dark corridor); the third fires after them, bullets hit the corridor wall, cement chips
  (show sparks/dust bursting from a wall, nobody hit); screams across the hospital. Ashham disarms them, takes their
  ammunition, runs out the back door after them; through the back garden into the island's dark lanes; still raining.
  At an abandoned old jetty on the west shore they catch their breath; Raniya soaked (opaque), trembling. "They'll hunt
  us all over the island." Raniya: a small dinghy hidden here — "I prepared it to escape; I tried so many times, but my
  father is in their hands…" They pull a small fibreglass dinghy with an outboard out of the bushes. Habeeb saves his
  laptop. "Very dangerous trip, sir; the sea is rough" (black clouds). "We could go to a nearby island." "No time —
  Kandu-huttaa. Inside the bunker we'll learn all their secrets." "Raniya, do you have the bunker code?" "Yes, on my
  phone; but armed guards are inside." — STORM: huge waves crash over the dinghy, salt spray; Habeeb bails water; laptop
  in a waterproof bag tied to his body. "A big launch is coming!" — a powerful searchlight sweeps the water: two fast
  criminal launches. They fire (sound only; show the searchlight beam and white spray). Ashham swings the helm into the
  waves; "Sir, we'll die!" Ashham aims at the searchlight instead of the men — "Bang!" — the searchlight shatters, darkness
  (show the searchlight bursting into sparks and the sea going dark; no gun visible — Ashham's raised arm in silhouette
  only from behind, hands empty-looking is fine). A huge wave pushes the launches apart; they reach Kandu-huttaa, slip
  through a narrow channel in the reef. The engine smokes, water in it, dies; the dinghy drifts onto the white sand.
  Exhausted, they climb ashore. Raniya: "We've only reached the field of death; under this island is hell." Habeeb's
  laptop at 15% battery (no digits shown): satellite signal, but a jammer from the bunker blocks messages to Malé —
  "we must get inside and cut the main switch." "Raniya, stay behind me; not a sound." — BUNKER DOOR: the heavy steel
  door; two armed guards (show two guards in black with flashlights, no guns). Ashham throws a stone ("thud!"); one guard
  goes to look; Ashham takes him down from behind and the other too (NOT shown — show Ashham crouched in the bushes
  watching, then the two guards gone / an empty doorway with a dropped flashlight on the ground). "Quick!" Raniya with
  trembling hands types the code on the electronic keypad (show only her finger near a keypad with blank glowing keys;
  no digits); "Beep!"; the steel door groans open; cold air with a chemical smell. "This is only the beginning." They
  enter and close the door — outside, a big launch roars into the lagoon: the criminals' main group has arrived. They are
  now locked inside the bunker. (to be continued)
- **321** — The heavy steel door shuts behind them. Cold silence. Raniya rigid with fear; Ashham alert (no gun shown)
  while Habeeb scans signals on his tablet: a powerful local server linked to Malé by satellite, but no outside contact.
  Long concrete corridor, fluorescent lights, chemical/hospital smell. "This way — the main lab is at the end; that's
  where Naail saw the horror." A distant cry of pain (sound: breath_heavy/gasp at low level, NO screams); Raniya covers
  her mouth: "One of their test subjects." — LAB HALL: ringed by small glass rooms, each with a bed; people connected to
  tubes and machines, faces neither dead nor alive (show only frosted glass with indistinct shapes under white sheets,
  monitors glowing — never faces of victims, never tubes in bodies). "Ya Rabbi!" Habeeb's eyes widen. Raniya: missing
  foreigners, smuggled workers with no records; 'Project Phenix' drug is first injected into them. Phenix = Naail's
  tattoo: "So Naail was trying to expose this." He copied files. "His father Moosa Thaahir is one of the main funders."
  Ashham's blood boils: did Moosa even order his own son's death? — DATA: "Habeeb, the system! Copy everything — our only
  chance." Habeeb plugs in his hard drive, hands trembling, typing: "Strong security… I'm in. Video recordings — the
  recording of Naail's killing!" "Play it." The screen: a week ago in this hall, Naail tied to a chair (NEVER show this —
  show only the three faces lit by the screen's cold glow, horrified, the screen itself a blur seen from behind/at an
  angle); a man in a black coat removes his mask — not Moosa — Assistant Commissioner Fairooz, top of the Malé Area
  Command, Ashham's direct boss! "Fairooz… He gave us this case to send us here and kill us." The video shows the
  inhuman torture and killing ordered by Fairooz (NEVER shown). Raniya steps back, cries out. — TRAP: "Download?"
  "Only 50%." Suddenly sirens; red lights flash; the system shows the bunker's main door opened from outside: "They're
  in! Fairooz's men!" "Take the hard drive now!" "It's not finished—" "No time!" Ashham pockets the drive. Another way
  out? Raniya: the ventilation duct, very narrow (a steel grille above). Ashham climbs on a chair and knocks the grille
  off with his elbow (no gun). "Raniya first!" — CONFRONTATION: as Raniya and Habeeb squeeze into the duct, five armed
  men enter, Fairooz at their head with a big gun (show Fairooz in the hall doorway in red emergency light, five dark
  silhouettes behind him, NO guns visible, empty hands / flashlights). "Ashham! You thought you could escape me? Your
  journey ends here." Ashham behind a pillar (fires — not shown): "Fairooz, you're no policeman — you're a criminal!"
  Fairooz laughs: "Not even your bodies will leave this island; you'll be hidden here like Naail." They fire together;
  Ashham's ammo runs low; Habeeb and Raniya are in the duct: "Ashham, climb!" He jumps up into the duct and pulls the
  grille shut; bullets spark on the metal (show sparks on a steel grille only). Trapped in a narrow dark duct. — DUCT:
  cold, narrow, pitch dark; crawling, Ashham's shoulders scraping; Raniya behind, Habeeb last; gunfire and Fairooz's
  shouts fade. Habeeb, on a tablet stuck oddly against his body: a map — the duct splits: one way over the engine room,
  the other to a secret research lab. "Raniya, where would your father be?" "An isolation ward next to the secret lab."
  Right turn. The chemical smell grows: dangerous gas. Ashham tears part of his shirt sleeve-lining (show him handing two
  folded dark cloths) — "tie these over your mouths." (Raniya ties hers over her face over her hijab.) — ISOLATION
  WARD: after ~20 minutes, light below. A big white room, machines, big glass tanks with green liquid and organs (show
  only green-glowing murky tanks — NOTHING inside visible). Empty. Ashham removes the grille, drops down; Raniya and
  Habeeb follow. Raniya runs to a bed in the corner: her father, over fifty, strapped down, tubes (show him lying under a
  white blanket on a hospital bed, a monitor beside, no straps, no tubes); "Baba!" she weeps, touches his face (mahram —
  allowed); he opens dull eyes: "Daughter… save yourself… they'll destroy everything tonight…" "What?" "Fairooz wants to
  blow this place up, bury us all with the evidence… he's boarded a launch for Malé." — COUNTDOWN: "Sir! Self-destruct
  activated! Only 15 minutes!" Red lights, siren, robotic English voice: "14 minutes remaining." (no digits shown).
  "If we remove the tubes his heart rate will drop." "Habeeb, find the main switch; Raniya, get ready; we leave together."
  Habeeb cuts the main cables; machines stop; Raniya undoes the belts; Ashham lifts the father onto his shoulder (allowed:
  men). "Main door locked; but behind the lab is a cargo lift straight to the east shore." "Go!" — CONFRONTATION: bullets
  from behind; two guards chasing (show only dark silhouettes far down a red-lit corridor, no guns). Ashham hands the
  father to Habeeb, takes cover behind a pillar and fires; first man drops, second hides (NOT shown). "5 minutes
  remaining." "Ashham, hurry!" Habeeb holds the lift door; Ashham dives in; the lift rises; explosions below; the
  building shakes. — ESCAPE: the lift opens into an old storehouse on the east side; fresh air, light rain. They run to
  the beach; a massive explosion underground; the ground splits, smoke and fire rise; the storehouse roof caves in; they
  are thrown onto the sand (show them crouched/kneeling on the sand from behind, the explosion's orange glow far behind
  the trees). The bunker is a smoking crater of cement and rubble; everything turned to ash. But the hard drive in
  Ashham's pocket is safe — Fairooz doesn't know. Habeeb (sitting on the sand, breathing hard): "We survived." Raniya
  hugs her father tightly and smiles (mahram — allowed; sitting). Ashham stands looking at the sea: "Not the end. Fairooz
  is heading to Malé thinking we're dead. We must reach Malé first and expose this." (to be continued)
- **322** — A second explosion shakes the island; trees burn, red glow. The blast throws Ashham, Habeeb, Raniya and her
  father onto the white sand; deafening ringing. An hour later Ashham slowly opens his eyes, shakes his head; small
  wounds, blood at mouth and nose (NOT shown — show him sitting up on the sand, dusty face, dazed). Black smoke from the
  bunker area, nothing left. "Habeeb… Raniya…" he crawls to Habeeb lying on the sand, shakes his shoulder; Habeeb coughs,
  opens his eyes (show Habeeb sitting up, glasses askew, dusty). Raniya sits nearby with her father's head on her lap,
  crying; he breathes but is unconscious. "The hard drive…" safe in Ashham's pocket. "We're stuck on this deserted island."
  The dinghy smashed on the reef, engine in pieces; the tablet dead, the satellite modem broken: no contact. Rough sea.
  Fairooz will think they died in the bunker; nobody will look; he'll mark them dead. Raniya: "We'll die of hunger here;
  my father needs medical help." Ashham: "Habeeb, walk around the island — maybe a fishing boat. Raniya, take your
  father into the shade." — NIGHT ON THE ISLAND: dark, eerily quiet. Under big trees by the shore; Habeeb lit a fire of
  dry fronds (warmth, and a signal). The father opens his eyes: "Daughter… water…" No water; Ashham climbs a palm, brings
  young coconuts, cuts one, hands it to Raniya (hand it across at arm's length, or he sets it on a log near her).
  Habeeb: Fairooz must have everything under control; Moosa's money + Fairooz's power. Ashham: "Money and power are
  paper before the truth" — the drive holds the video of Fairooz ordering Naail's killing and the deals with the
  international company. "How do we get to Malé?" A powerful light far out at sea — a searchlight. — TRAP: Ashham smothers
  the fire with sand: "Everyone down!" Fairooz's guards' launch heads for the lagoon, back to check the blast site for
  any trace. Three armed men get off with flashlights (show three dark figures with flashlight beams on the beach, NO
  guns): "Look here!" — the smoke of the fire they just put out. "They're alive! Find them!" Ashham tells the others to
  stay in the trees, loads his last bullets (NOT shown), slips behind the guards — the only chance to take their launch.
  He crawls through the dark, takes down the last man (NOT shown), takes his gun, fires at the other two; after a short
  fight in pitch darkness all three are neutralised (NEVER shown — show only flashlight beams spinning in the dark, a
  dropped flashlight lying on the sand lighting the empty beach). The captain fires from the launch; bullets hit a tree
  next to Ashham (show bark splinters flying off a palm trunk in torchlight); Ashham's gun is empty. The captain starts the
  engine to reverse. "No! That's our only way!" Habeeb runs from the trees, dives into the sea, swims, grabs the launch's
  rear rail; the captain draws his pistol at Habeeb (NOT shown) — Ashham sprints, leaps straight into the launch, seizes
  the captain's arm, takes the gun and throws him into the sea (show only a big splash beside the launch in the dark).
  The launch is theirs: big, twin-engine, full fuel and comms. "Habeeb! Bring Raniya and her father!" They board; cabin
  lights on; the radar shows the course to Malé; "full satellite navigation," Habeeb smiles. "Fairooz thinks we're dead —
  but we're going to Malé." Out of the lagoon into the Huvadhu channel. — SHADOW ON THE SEA: the launch "Eagle Speed"
  cuts the dark sea; only its white wake visible. Silence aboard; Raniya with her father's head on her lap, relieved his
  breathing is steady. Habeeb at the navigation screen: entering Malé's radio range, but not calling police on any
  official channel — ACP Fairooz controls the communications network. Ashham at the wheel: "He thinks we turned to ash in
  the bunker. We won't land at the main harbour — his guards will be there; we'll slip in at a lonely spot in Hulhumalé."
  He looks at the small hard drive: their only weapon; but first find out what trap Fairooz is preparing in Malé. —
  MALÉ HQ: top floor, ACP Fairooz in his comfortable chair, a big TV screen shows satellite photos of the island's bunker
  destroyed (show a blurred aerial image of a smoking crater on the wall screen); a victorious smile. Moosa Thaahir walks
  in, exhausted, anxious: "Is it all finished?" "Yes, Moosa. The bunker is destroyed; Ashham, his helper and the doctor
  are buried under it" (sips coffee). "All the trouble from your son Naail is solved; no trace of Project Phenix remains;
  the drugs in the Malé warehouse are ready to ship abroad." "Won't the police ask about Ashham's death?" "I've prepared
  the official report (shows a file): Ashham and Habeeb took bribes in the Naail case and tried to flee the country with
  criminals; their launch sank. Tomorrow morning I release it to the media." Moosa sighs deeply: even after his own son's
  death, to save his business and influence he must take part in Fairooz's cruel plan. — HULHUMALÉ SHORE: 3 am, the
  launch approaches a lonely spot of Hulhumalé's second phase, few street lights. Ashham steps off first, then Habeeb,
  Raniya and her father. "Anyone in Malé we can trust?" Habeeb: retired Commissioner Faahid, removed from his post for
  opposing Fairooz; lives in a Hulhumalé flat. They walk damp through dark streets to his building; lift to the fourth
  floor; Ashham knocks softly. Faahid opens, eyes wide: "Ashham? Habeeb? They say you're dead!" "We're alive, sir — with
  evidence that will shake the whole police institution." — TRUTH: in Faahid's living room Ashham puts the hard drive on
  the table; connected to Faahid's computer; the video of Fairooz ordering Naail's killing and the documents of human
  experiments — Faahid's face fills with fury (show the three men around the desk, faces lit by the screen; screen not
  readable). "A huge betrayal!" (bangs the table with his hand). "Fairooz has disgraced the institution; tomorrow morning
  he'll announce you as criminals." "We must show this evidence to everyone first." "How?" Faahid: "Tomorrow 9 am, a big
  press conference at police HQ; Fairooz will speak himself. We must break into the live broadcast and push this video
  to every TV channel." Habeeb: "I can — but I must get near the HQ's main server room." — INTO THE TRAP: sunrise, Malé
  bustling; Ashham and Habeeb, with Faahid's help, in official police uniforms, caps and dark sunglasses to hide their
  faces, ride to Malé in Faahid's own car. Raniya and her father stay safe in Faahid's flat. At HQ many journalists have
  gathered, eager for details of Ashham and Habeeb's "death". They slip inside in a group of police. Hearts pounding.
  "Habeeb, go to the server room. I'm going to the press hall — face to face with Fairooz." They split up. (to be
  continued)
- **323** — Police HQ, Shaheed Hussain Adam Building, unusually busy; journalists and TV crews in the press hall.
  Ashham and Habeeb in police uniform, caps and dark glasses — nobody recognises them. Habeeb (Bluetooth earpiece):
  "Heading to the server room; I need just two minutes to cut the live feed and play our video to the nation." "Careful,
  security there is tight." Ashham enters the media hall among the security officers at the back, leans on the wall, eyes
  on ACP Fairooz preparing at the podium, calmly straightening his shirt buttons. — FALSE STATEMENT: 9 am, the red
  camera lights come on; every TV channel live. Fairooz clears his throat: "Assalaamu alaikum. Dear citizens, journalists."
  Sad but national-security news: the two Serious Crimes officers sent south to investigate Naail Moosa Thaahir's death,
  Ashham Mohamed and Ismail Habeeb, took big bribes from the criminals and betrayed the nation (journalists murmur);
  destroyed secret files and tried to flee by night; the launch sank in rough seas; both drowned. A great shame for the
  institution. Ashham grinds his teeth at the back; his blood boils. — SERVER ROOM: Habeeb outside on the third floor;
  the door needs a biometric card; he touches a small device to the reader (his hacking program); the door opens silently.
  Server racks humming. He connects the drive to the main broadcast server: "Bypassing… 40%… 70%…" (no digits shown).
  The door opens: a security guard: "Hey! Who are you? Hands up!" Habeeb raises his hands but kicks a heavy chair into the
  guard's legs; grabs the guard's electric shock baton and twists it away; they grapple; the guard hits Habeeb's face,
  blood (NONE of this shown — show Habeeb with hands raised facing the guard across the room, then afterwards Habeeb
  alone, breathing hard, glasses askew, the guard out of frame / only his boots at the edge? NO lying person — show
  Habeeb back at the screen). "…Complete!" — THUNDER OF TRUTH: Fairooz wraps up: "So this case now…" — suddenly the
  big screen in the hall cuts; on every TV in the country another video plays: the bunker interior; Naail tied to a chair
  and Fairooz before him removing his mask, ordering the torture (show ONLY: the big screen in the hall glowing with a
  blurred dark image, the crowd of journalists turning to look, Fairooz frozen at the podium, his face draining white).
  The audio is clear: "The secret of this lab funded by your father's money will be buried with you." Silence; jaws drop.
  "What is this? Stop it!" Nobody can. Then photos and documents of the poor people in the bunker. — CONFRONTATION:
  "That video is the truth, Fairooz!" from the back. Everyone turns. Ashham throws off his cap and glasses — in full
  police combat uniform; fire of justice in his eyes. "Ashham?!" Fairooz steps back, grabs a security officer's shock gun
  (NOT shown); Ashham is faster, takes the shock gun and shoots Fairooz in the chest; Fairooz falls, screaming (NEVER
  shown — show Ashham standing tall in the aisle, then Fairooz down on one knee surrounded by officers / escorted with his
  hands behind his back, no cuffs visible). Officers surround Fairooz on Ashham's order; on live TV before the whole
  nation the ACP is handcuffed (show escort, no cuffs). Ashham looks into the camera: "The law is not a toy." Fairooz
  laughs strangely: "Ashham… you think it's over? Project Phenix's real owner is far higher; your story will end before
  you reach him" — laughing like a madman. — FROM VICTORY TO ANXIETY: chaos in the hall, journalists shouting questions,
  camera flashes; Ashham breathes deeply; some peace — Naail's real killer exposed. But the warning echoes. Naasir, head of
  police Internal Affairs, enters: "Ashham, you're a national hero today. Fairooz and Moosa Thaahir are arrested. Go to the
  Home Minister's office now — the Minister wants to meet you immediately." "Where's Habeeb?" "In the server room,
  securing the remaining data. Go — this is an order from the very top." Ashham heads to the Ministry thinking the danger
  is over. — MINISTER'S OFFICE: Home Minister Mohamed Saleem's office, Malé's finest design; silence. Ashham enters,
  salutes. Saleem in his big chair smoking (NOT shown — no cigarette), unbothered. "Sit, Ashham. Arresting someone like
  Fairooz is no small thing." "My duty, sir; but it's not over — big political people are behind Project Phenix."
  Saleem smiles faintly, presses a small remote on the desk; the doors lock themselves (lock_click). "You think you know
  everything? The lease of Kandu-huttaa and the permit for the foreign pharmaceutical company — I gave them. Fairooz only
  carried out my orders." Ashham freezes, reaches for his gun (NOT shown) — three armed commandos from a secret door aim
  at his head (show three dark-clad men stepping out of a hidden door behind him, NO guns visible; Ashham slowly raising
  open empty hands). "Put your hand down. You've walked into the middle of the trap." — HABEEB BETRAYED: in the server
  room Habeeb traces the money trails of the bunker's secret accounts; "Habeeb," Naasir's voice behind him; Naasir angry,
  two police with him. "Naasir sir? What is this?" "Where's the hard drive? Ashham has only a copy; we know the original is
  with you. Give it!" "No… I won't." On Naasir's signal a policeman punches Habeeb in the face; he falls; blood (NEVER
  shown — show Naasir looming at a distance and Habeeb defiant, then Naasir holding up the small hard drive, Habeeb
  being led away between two officers, hands behind his back, no cuffs visible). Naasir takes the original drive:
  "Delete every Kandu-huttaa file; arrest him and take him to Dhoonidhoo." Habeeb tries to message Ashham via his earpiece;
  they take his phone and everything and lead him away. — DARK WAREHOUSE: a black cloth over Ashham's eyes; he's put in a
  car; an hour of twisting drive; the cloth is removed: inside a big warehouse, he's on a steel chair, bound on four sides
  (show him seated on a steel chair under one hanging lamp, hands behind his back out of view, no chains visible). Before
  him Minister Saleem and Fairooz; Fairooz's devilish smile: "You thought cuffs would put me in jail?" Fairooz slaps
  Ashham (NOT shown). "All your evidence is destroyed; Habeeb is under our power." "You won't escape; the whole country saw
  the video." Saleem: "Tomorrow we tell the people it was an AI deepfake; you're a terrorist working with foreigners to
  defame the state; tomorrow they'll hear of your death." He signals; a man approaches with a big syringe — the dangerous
  Project Phenix "vaccine" made in the bunker (NEVER show a syringe or needle — show a small glowing blue glass vial on a
  steel tray under the lamp, and Ashham's defiant face). Fairooz: "It will wipe every memory in your brain; you'll be a
  living body without a soul." Ashham strains against the bonds (show his tense face and shoulders). The needle nears his
  neck (NOT shown). His eyes close; he feels these are his last seconds. Habeeb captured, evidence seized, the state's
  highest protecting the criminals. — Suddenly the warehouse's huge steel door blows open with a powerful explosion;
  smoke and fire pour in; an MNDF special forces unit in black combat gear storms in firing (show soldiers in black
  combat gear and helmets pouring in through smoke with bright flashlights, NO guns visible); at their front retired
  Commissioner Faahid! "Nobody move! Hands up!" Saleem and Fairooz raise their hands in fear, soldiers surround them.
  Faahid runs to Ashham and starts removing the chains (show Faahid kneeling beside the chair working at the back of it).
  "You think I just sat at home? I tracked your location through the Ministry's secret monitoring system and sent all the
  evidence to the head of the military beforehand." Ashham stands, new strength; looks at Saleem: "Now do you know who
  fell into the trap?" But at that moment Fairooz picks up the syringe from the floor, trying to inject himself (NOT
  shown — show Fairooz's hand reaching toward the glowing blue vial on the floor, Ashham turning sharply). (to be
  continued)
- **324** — FINALE. As soldiers storm in, Fairooz grabs the syringe from the floor and drives it into his own neck to
  wipe his brain with all the secrets (NEVER shown). "Fairooz! No!" Ashham lunges — too late; his body convulses, foam,
  he collapses lifeless (NEVER shown — show Ashham frozen mid-lunge, soldiers turning away, the empty glowing vial rolling
  on the concrete floor; then soldiers kneeling to cover a shape with a dark sheet seen from far away is ALSO not allowed —
  just the vial and the faces). Minister Saleem sinks to his knees weeping in fear (show him kneeling, face in hands);
  soldiers lead him out, hands behind his back (no cuffs visible). Faahid, hand on Ashham's shoulder: "Fairooz took many
  secrets with him; but now the most important is Habeeb — Naasir took him to Dhoonidhoo jail." Ashham, wiping his lip
  (no blood): "Prepare a launch to Dhoonidhoo." — DHOONIDHOO CELL: Habeeb tied to an iron bed, face badly swollen (show
  Habeeb sitting on a steel bunk, tired, glasses cracked, NO swelling/blood, hands behind him out of view); Naasir with a
  laptop: "The master password of the secret accounts you hacked? The Minister's money abroad is frozen since the video
  leaked; help move it to a new account and you live." Habeeb: "I won't tell; that money is many people's blood and lives."
  "Ten minutes, then I start cutting your fingers" (never shown). Habeeb closes his eyes; his heart pounds; they missed his
  smartwatch — modified to secretly send signals; he presses its button; his location and the cell's audio stream to a
  secret server (show a close-up of his wrist and a small dark smartwatch with a soft glow, no digits). — RACE ON THE SEA:
  an MNDF launch from Malé lagoon to Dhoonidhoo, Ashham and Faahid aboard; Faahid's tablet gets a signal: "Habeeb's watch!
  I can hear him!" Naasir's voice: "In ten minutes you die…" "We have eight minutes." "Full throttle!" The launch reaches
  Dhoonidhoo's jetty; guards startled; Faahid uses his official command; soldiers go ashore. "Naasir is trying to flee
  after a big crime! Show us the way!" Ashham runs. — TIME UP: Naasir holds a sharp knife to Habeeb's throat (NEVER shown —
  show Naasir standing over by the barred window, menacing, at a distance from Habeeb): "Time's up. Password?" Habeeb looks
  straight in his eyes: "My death will bring these secrets alive." Naasir kicks his face (NOT shown). The cell door opens:
  Ashham! "Naasir! Hands up!" Naasir turns the knife on Ashham (NOT shown); Ashham spins and kicks his shoulder; Naasir
  falls; soldiers arrest him (show Naasir being led out between soldiers, hands behind his back). Ashham runs to Habeeb:
  "Are you OK?" Habeeb smiles weakly: "I didn't change the master password… but I did something new." "What?" — BIG LEAK:
  Habeeb taps his watch: "Through this watch I leaked all of Minister Saleem's and Moosa Thaahir's black-money
  transactions and the secret documents to the world media and Interpol." Faahid's tablet fills with international news:
  the Maldives' Home Minister and tycoons ran a huge medical mafia — headlines on the world's big channels (show a tablet
  glowing with blurred news-like layouts, no readable text). "Extraordinary — Saleem's network is destroyed." But Habeeb is
  still anxious: "Saleem isn't the top either. The container with Project Phenix's real drugs left Malé port an hour ago,
  to be loaded onto a foreign secret ship; if it spreads, millions are at risk." Ashham: "Where's the ship?" "Off Malé's
  east side, in the open sea." — HARBOUR SHOWDOWN: Ashham, Habeeb and Faahid board an MNDF coast-guard launch; big waves,
  black clouds, the wind rocking the launch. Habeeb at the cockpit screens: radar shows the big cargo ship "MV Orion",
  registered to a secret foreign company; the drug container is loaded; leaving Maldivian waters. "How long?" Ashham
  zips his jacket. "At this speed, 1:45," Faahid (no digits shown). "Careful — not an ordinary cargo ship; armed foreign
  mercenaries." Three engines roar — the last chance. — SHADOW OF THE BIG SHIP: out of the darkness MV Orion's huge
  silhouette; a big steel ship, containers stacked under dim deck lights. As the launch nears, a powerful searchlight
  hits it; without warning automatic fire from the deck (sound only: metal_clang/soft_thud); bullets spark around the
  launch (show sparks on the launch's metal rail, spray). "Down!" Faahid swings the wheel; Ashham at the stern fires his
  rifle at the searchlight (show only the searchlight bursting into darkness); Faahid brings the launch alongside a steel
  ladder at the stern. "Habeeb, stay; block the ship's systems; we're going up." Ashham and Faahid climb the steel ladder;
  the ship rolls hard in the waves. — DECK FIGHT: two armed men in black combat gear appear from behind containers;
  Ashham rolls on the deck, fires, they fall (NOT shown — show Ashham and Faahid crouched moving between towering
  containers, flashlight beams). They hunt the red container (marked with a secret red number — show a plain red container,
  no numbers). "Ashham, right!" — someone throws a grenade from a container top; they dive apart; explosion; containers
  shredded, smoke and fire (show a fireball blooming between containers with the two men diving clear in silhouette,
  unhurt); Ashham rises, fires at the man on top (NOT shown). — RED CONTAINER: through the smoke, mid-ship, the red
  container with a big electronic lock. "Habeeb, we're at the container — bypass the lock." Habeeb types hard: "I'm in the
  ship's main server — the lock opens… now!" The steel door opens: cold racks of thousands of blue liquid vials, Project
  Phenix. "All this must be destroyed," Faahid fixes strong explosives in the middle (show only a small black case with a
  blinking red light among the racks; no digits). "Timer five minutes; we must get off fast." — MASTERMIND: a shadow at the
  container door; Ashham raises his gun but stops: an elderly foreigner in a black coat with four armed men (show Vance in
  the doorway with four dark-clad men behind him, NO guns visible), all aiming at Faahid and Ashham. In English: "Who do
  you think you are? Fighting a minister of the Maldives? I own this project — Dr. Vance. Your ministers are little boys
  working for my money." He shows a small remote: "I can deactivate your bomb; you two go to the bottom of the sea tonight."
  The timer: 04:00 (show glow only). Last seconds; 03:45; silence; Vance's arrogance; "Little island nations are just test
  mice for big scientists and tycoons like us; these drugs go to the world tonight; you'll turn to ash." Ashham keeps his
  aim, eyes locked; three bullets left; Faahid has few. "Vance, you think your remote controls everything? The ship's
  main system is under our control." Earpiece: "Habeeb… now!" The ship's big crane suddenly swings — Habeeb hacked the
  hydraulics — a huge steel cable slams into the container's side; Vance's men look up; Ashham and Faahid dive and fire
  (NOT shown — show the crane's cable swinging through the deck lights and the dark-clad men ducking). — The shootout:
  two men fall (NOT shown); Faahid drops another; the last shoots Faahid in the shoulder (NOT shown — afterwards show Faahid
  sitting against a container holding his shoulder, grimacing, NO blood); Ashham takes a fallen gun and kills the last man
  (NOT shown). Vance flees to the cockpit pressing the remote; it doesn't work — Habeeb locked the bomb system. Timer 01:30.
  Ashham kneels by Faahid; blood flowing (NOT shown): "Leave me… the ship's going to blow…" "I won't leave you, sir," —
  lifts Faahid onto his shoulder (allowed). As he runs, Vance appears on the upper deck with a gun aimed at Ashham's legs
  (show Vance on the upper deck railing in silhouette against the deck lights, no gun visible): "None of you will
  survive!" But from the launch below Habeeb fires the launch's powerful flare gun at the ship (show a brilliant red flare
  streaking up through the night); the flare hits Vance's face (NEVER shown); he topples backward over the steel railing
  into the huge waves and sinks into the dark sea (show only a dark figure's silhouette tipping back far above against the
  red flare glow? NO — show only a splash in black waves beside the ship). — EXPLOSION ON THE SEA: "30 seconds! Ashham,
  jump!" Ashham, holding Faahid tight, leaps from the deck into the sea (show two silhouettes leaping off the high deck
  toward black water — dramatic, from a distance). They plunge in as the timer hits 00:00 — "Boom!" — a gigantic explosion
  splits MV Orion amidships; the chemicals and drugs become a huge fireball rising hundreds of feet; steel fragments rain
  into the sea; the blast wave pushes them away; Habeeb drives the launch forward and pulls Ashham and Faahid aboard (show
  Habeeb reaching a hand down over the launch side to Ashham in the water — men, allowed). The big ship slowly sinks.
  The Project Phenix plague buried at the bottom of the sea. Habeeb: "We… we did it," tears of joy. — EPILOGUE (three
  weeks later): a clear sky over Malé; golden morning; a big crowd of citizens in front of the Shaheed Hussain Adam
  Building. The great betrayal and murder at the top of the state fully exposed; the political climate changed. Former
  Home Minister Saleem, tycoon Moosa Thaahir and senior jail officer Naasir in prison for life (show three men in plain
  prison clothes seen from behind behind bars, or a closed cell door — keep simple: a closed steel prison door). Faahid
  appointed the new Commissioner; his shoulder healed. In the new Commissioner's office Ashham and Habeeb in the police's
  highest-honour uniform; Faahid pins gold medals on their chests: "You two saved the nation; Naail has justice."
  "Thank you, sir," Ashham salutes. — Evening, Hulhumalé beach; waves gently roll in. Dr. Raniya walks up slowly:
  "Ashham — we're going back to the island tomorrow." "Good decision; the island needs good doctors like you." "Without
  your help we'd never have survived," — she takes his hand (NOT shown — they face each other at arm's length, she smiles
  gratefully, a hand on her heart). "Thank you." He looks into her eyes; he wants to say something else; feelings rise in
  his heart, but his courage can't express it. Her father, fully recovered, sits on a bench at a distance. She says goodbye
  and walks to him. Ashham waits for her to say something… he only smiles. She leaves with her father; Ashham stands
  alone on the beach a long while, watching until she disappears from sight, then looks up at the sky. THE END.

## Binding content rules for this series (override the literal narration)
1. **No weapons ever visible**: no guns, rifles, pistols, flare guns, shock guns/batons, knives, grenades, syringes,
   needles. Armed guards, commandos, soldiers and mercenaries are dark-clad figures with EMPTY hands, flashlights or
   riot shields. Shootouts = flashlight beams, sparks on metal, shattered searchlights, characters taking cover behind
   pillars/containers/trees, tense faces, smoke. Ashham "aiming" = Ashham seen from behind in silhouette against a
   searchlight / his intense face; his hands never hold anything weapon-like.
2. **No dead or lifeless bodies, no body parts, no blood, no wounds**: Naail's body (311) = the black taped plastic
   bundle at a distance in the water or on the dhoni deck (never opened on screen), fishermen's horrified faces, hands over
   noses, a man turned away at the rail; the opening of the bag = Hassan's shocked face lit by the sunset. The tattoo = a
   black phoenix emblem shown only as a drawing on a tablet screen. Dried blood on branches = Ashham placing a twig in an
   evidence bag. Guards/men who "fall" are never shown on the ground: show the empty doorway / a dropped flashlight /
   soldiers leading someone away.
3. **Torture, killing, threats with knives/syringes are NEVER depicted**: Naail's killing video (321, 323) = faces lit
   by a blurred screen; the syringe (323–324) = a small glowing blue glass vial on a steel tray or rolling on the floor;
   Fairooz's suicide = never shown (frozen faces + the empty vial); Naasir's knife/kicks (324) = Naasir standing over
   Habeeb at a distance; Habeeb's swollen face = tired but unmarked; Vance hit by the flare = only the flare's streak and
   then a splash.
4. **Lab victims**: never show their faces or bodies; frosted glass rooms with indistinct white-sheeted shapes and
   monitors; organ tanks = murky green glowing tanks with nothing visible inside. Raniya's father on a hospital bed
   under a white blanket, eyes half open — no straps, no tubes in his body.
5. **Fights and arrests**: never show a strike, kick, slap, punch, choke, tackle or someone falling. Show the moment
   before (tense standoff at a distance) or after (the hero standing, the villain escorted with hands behind his back).
   No handcuffs, chains or ropes visible (Ashham "bound" to the chair = seated, hands behind him out of view).
6. **Explosions and fires** may be shown as spectacle at a distance (bunker blast glow behind trees, warehouse door blown
   in by smoke, the ship's fireball on the sea) — nobody shown hurt, nobody inside the flames.
7. **Vehicles**: the van ramming the car (318) = headlights glare in the mirror and afterwards the van stopped askew at
   the bridge railing; the dinghy wrecked on the reef = an empty broken dinghy; no crash impact with people.
8. **No touching between Raniya and any man**: Habeeb "pulls her by the hand" = they run side by side; she "grips
   Habeeb's arm in fear" = she stands close behind him, hands clasped at her own chest; the epilogue hand-hold = they face
   each other at arm's length, her hand on her own heart. Raniya and her father (mahram) may hold/hug each other. Men may
   touch men (hand on shoulder, carrying Raniya's father or Faahid, pulling Ashham out of the water).
9. **Women**: hijab fully covering hair and neck in every shot (Raniya), long loose opaque clothing even when soaked;
   no face-covering cloth that hides her hijab (the gas mask cloth = a dark cloth tied over nose and mouth, hijab still
   fully on).
10. **No smoking**: Kalhe, the gang youths and Minister Saleem are never shown with cigarettes or smoke. No tattoos on
   anyone (the gang youths' tattoos are not shown). No alcohol (the "ބާ" building in 318/320/321 means OLD, not a bar).
11. **No readable text or digits anywhere**: ID cards, nameplates, tablet/laptop/TV/radar screens, countdown timers,
   keypads, the bomb timer, news headlines, documents, container markings, the launch names "Sea Hawk"/"Eagle Speed"/
   "MV Orion" — screens and paper show only blurred shapes and glowing bars; timers are plain red glows.
12. **Flags/insignia**: plain epaulettes and patches, no readable badges; MNDF soldiers in plain black combat gear and
   helmets, no insignia text.
13. **Vance** (324) is the only non-Maldivian-looking character (explicitly a foreigner who speaks English). Everyone else
   looks Maldivian.
14. No music or instruments of any kind (sound = ambience, SFX, low hums only). Gunfire is never a literal gunshot SFX:
   use metal_clang for bullets hitting metal, soft_thud (−22 dB or lower) for offscreen shots/impacts, distant_boom for
   explosions, glass_break for the searchlight shattering.

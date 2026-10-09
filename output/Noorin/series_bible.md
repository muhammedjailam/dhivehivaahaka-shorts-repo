# Noorin (ނޫރިން) — series bible

Dhivehi audio drama, emotional crime/romance drama. This batch has four episodes that form one arc, in this order:
**495 → 497 → 501 → 503** (the episodes in between are not part of this batch). Every episode's cover
(`work/episode-<N>-cover.png`) is the same series poster: Noorin as a police officer at night on a rain-wet Malé street,
black hijab under a black beret, dark-navy uniform, a flashlight, a police car with blue/red lights behind her. Match that
look (see `style.txt`).

The story runs on TWO TIMELINES. Keep them visually distinct:
- **PRESENT** — Noorin is about 34, a police officer just promoted to **Inspector**. Cool night palette, navy/teal with
  crimson and police-light accents, rain, modern Malé. Characters: `noorin`, `uvaish`, `aakif`, `zee`, `reem`,
  `uvaish_lawyer`.
- **TWELVE YEARS AGO** (flashbacks) — Noorin is about 22, a fragile, gentle young woman. Warmer, softer, slightly hazy
  golden light. Characters: `noorin_young`, `uvaish_young`, `aakif_young`, `naahidh`, `reem` (younger — say "about 22"
  in the visual).
Use `transition="dissolve"` into and out of flashbacks and `transition="black"` for time jumps inside a timeline.

## Characters (series cards in `output/Noorin/characters/`)
| id | who |
|---|---|
| `noorin` | PRESENT. Inspector Noorin, ~34. Default: dark-navy police uniform, black hijab, black beret, two small silver stars on each shoulder. Composed, cold, unsmiling in public; in private still wounded. Secretly writes film scripts under the pen name **"WhiteLily"** (ވައިޓްލިލީ); her film **"Rihun"** (ރިހުން, "Pain"). When off duty (home, film festival) describe her outfit in `visual` (e.g. "wearing a loose deep-plum long abaya-style dress and a black hijab instead of her uniform"). |
| `noorin_young` | FLASHBACK. Noorin at ~22: soft, frightened, kind. Long loose dusty-rose dress, cream hijab. Resort secretary in 497; Uvaish's wife and later pregnant in 501. |
| `uvaish` | PRESENT. Uvaish (އުވައިޝް), ~38, one of the Maldives' best-known businessmen/resort owner. Charcoal suit, neat beard with grey at the temples. Haunted by guilt. |
| `uvaish_young` | FLASHBACK. Uvaish at ~26: handsome, charming, playful, rich young owner of a resort under construction. White long-sleeved linen shirt, beige trousers, clean-shaven. |
| `aakif` | PRESENT. Aakif (އާކިފް), ~36: strong, confident, "trained" — powerful presence. Black long-sleeved shirt, dark trousers. Still loves Noorin. |
| `aakif_young` | FLASHBACK. Aakif at ~24: slim, gentle, from a respected Malé family, has asthma (carries a blue inhaler). Light-blue long-sleeved shirt. |
| `zee` | Zee (ޒީ), Noorin's close female friend who handles her scripts/film business, ~35, glasses. |
| `reem` | Reem (ރީމް), Uvaish's wife by a family arrangement (501, ~22) — later divorced, now married to Naaif (503, ~34). Elegant, kind. |
| `naahidh` | Naahidh (ނާހިދު), young male co-worker at the resort office (497 flashback). |
| `uvaish_lawyer` | Uvaish's lawyer (ވަކީލު), ~50 (503). |

People without cards (describe them in `visual` only, never put them in `chars`): Noorin's mother, the stepfather
(NEVER shown at all), the injured girl and her mother (495), the prison offender (495), other police officers, Jinaah
(male police officer, 503), the film producer Sen Dil (497), resort workers, islanders, the doctor, Naaif (Reem's husband
in 503), a female clerk/typist (503).

## Episodes
- **495** — Opens 12 years ago: thunder, heavy rain on a crowded Malé street at night; people shelter under shop awnings.
  Young Noorin, eyes red from crying, soaked. She had escaped her cruel stepmother on her island after her father left,
  come to her birth mother in Malé full of hope — but in her mother's house she had to fight to protect her own honour
  (from her stepfather; never shown). Not wanting to break her mother's heart, she left the house sobbing. 11 pm, shops
  close, street empties; she sits on the roadside in the rain, shivering, faints — and falls against a man standing
  beside her, who lifts her in his strong arms (show only: a man's umbrella / silhouette from behind, never a carry).
  She wakes in an unknown, luxurious, modern bedroom, a pleasant fragrance, wearing clean changed clothes (show her fully
  dressed in a clean modest dress and hijab, sitting up startled); her bag beside the wardrobe, nothing missing. She
  writes a short note in a notebook on the desk and hurries out.
  PRESENT: Noorin enters her apartment, takes off her cap and places it on the table; in the mirror looks at her
  uniform and touches the two stars on her shoulder — promoted to Inspector today. She opens her laptop and e-mails;
  her face changes; phones Zee: "PictureLand mailed again — I write as 'WhiteLily', I won't give my real name"; Zee: they
  want to enter "Rihun" in a film festival. In the business news she sees the name **"Uvaish"** in big letters, slams
  the laptop shut. Case: a girl lying beside a bed who cut her wrist (NEVER shown — see rules), rushed to hospital;
  Noorin confronts the girl's sobbing mother: why didn't she protect her child from that beast of a man (the
  stepfather) for the sake of "what people will say". At her office desk Noorin is haunted by children's voices she has
  heard in her work: abuse cases, a child who used "something friends gave" to escape quarrels, mockery and punishment;
  she covers her ears. She works hard to rehabilitate young offenders. In a jail cell she confronts a smirking
  middle-aged offender who says vile things about women; she loses her temper and strikes him twice, he hits back and
  grabs her collar; officers rush in and pull him away; she calmly tells him the whole scene was recorded. Leaving the
  court with other officers towards a police vehicle, she is seen by **Aakif**, overjoyed as if he found a lost jewel;
  she puts on sunglasses, ignores him and gets into the vehicle; he thinks he imagined it ("Noorin is weaker than
  that"). In the side mirror she looks at him. Twelve years ago she put him out of her mind; her life is devoted to
  nation and religion; no room for worldly love.
- **497** — PRESENT: tired, Noorin comes home, freshens up, sits at the computer: an invitation to the SAARC film
  festival, held in the Maldives. Zee apologises: she gave them Noorin's ID. Award night: trailers, awards; best
  screenplay = "Rihun" by WhiteLily. Everyone stares as Noorin walks on stage. Most stunned of all: **Uvaish** — like
  seeing a ghost; he searched for her for 12 years. After the ceremony Noorin, Zee and producer Sen Dil talk; Uvaish's
  voice: "Noorin." She turns, frozen. Bitter words: "This is not Noorin. WhiteLily." She walks away; he grabs her
  hand; she turns and slaps him (NOT shown — see rules). Zee and the producer stunned. He lets go. At home she throws
  her things on the bed and screams out her pain. Memories: 12 YEARS AGO — Noorin, two months a secretary at a resort
  under construction, walks briskly to the manager's office past busy workers. "Madam, careful!" — a young man pulls her
  aside; a stone falls; a tarpaulin falls over both of them; workers free them. Her white dress dusty, her arm scraped.
  The young man (**uvaish_young**) teases: "Is 'thank you' all you say after I saved your life? Join me for breakfast."
  She walks away; "I'll wait." In her room she cleans the scrape. Doorbell: co-worker **Naahidh** with an ointment
  bottle — "the boss sent it". Later a knock: the same young man walks in with an ice pack; "Not boss — Uvaish." He
  seats her on the sofa and holds ice to the bump on her head (see rules); she realises he's the man who rescued her
  in the rain two months ago — she had left only a "thank you" note. He says he came "to find something you stole";
  she panics, apologises — she left the door unlocked that night, maybe a thief came in. He smiles, teases her ("learn
  to say something other than sorry and thank you"), walks to the door, looks back; she stands frozen.
- **501** — FLASHBACK continues: tears in her eyes; she had sworn not to cry after that night. The thing she "stole" was
  his heart. He proposes marriage. She is overwhelmed; he is handsome, kind, rich — the resort owner. She accepts. They
  marry; two happy weeks — then he suddenly divorces her ("I'll come back. Stay in this house. I must go today."). She
  waits in pain, then — pregnant — moves to her home island for her baby's sake. There her stepmother spreads shameful
  rumours; islanders mock her and throw rubbish at her in the street. Evening on the beach for comfort; something
  thrown hits her; she shields her unborn child. **Aakif's** backstory: on her first day in Malé, the lift broken, she
  climbed the stairs of her mother's building; a Ventolin inhaler fell at her feet; she heard someone gasping for help
  and brought it to him (aakif_young, asthma attack) — he survived. He has waited to repay her. Hearing her story he
  brings her to Malé, keeps her in his family home, and tells people she is his wife to protect her (no real marriage
  shown). At an event they run into Uvaish and his wife **Reem**. Noorin excuses herself to the washroom. Aakif tells
  them she's his wife, pregnant 4–5 months. Uvaish calculates — five months since the divorce — puts down his juice
  and leaves; as Noorin comes out he drags her into a nearby room: "Whose child is that?" He accuses her of betrayal
  with Aakif; she stays silent (technically she is still his wife within the iddah). He blocks the door. Then the
  cruelty that night (NEVER shown or hinted at visually — see rules). She leaves weak, hand on her side. Message to
  Aakif: "Sorry Aakif… I can't marry you." Later: Noorin alone on the shore at Maafushi-like beach, huge waves; the
  doctor's words (the baby is lost) echo; she covers her ears. Alone, abandoned by mother and family, she steps toward
  the sea — her conscience wakes: suicide is a great sin; think of the blind, the disabled, the deaf; live for a higher
  purpose, help others, serve your religion and nation. She breathes, closes her eyes. Had her conscience not woken,
  she'd have lost this world and the next.
- **503** — PRESENT: leaving for the office, Noorin meets Aakif — he has moved into the apartment next door. After 12
  years… He went abroad for training; now strong, feared. He still waits for her. She, cold: her heart is stone; her
  life belongs to her national duty. Sunglasses on, she rides off on her (police) motorbike; he watches, sensing Uvaish
  still lives in a corner of her heart. Crime scene: a famous businessman's office broken into — shattered glass, a
  forced safe, photographers; Noorin studies the scene. Uvaish walks in, stunned to see her as a strong officer. His
  secretary: "A woman officer?" Noorin: competence matters, not gender; "Jinaah, investigate thoroughly." Passing
  Uvaish with sunglasses on: some people don't respect women; she serves even traitors professionally. Uvaish at home
  on his sofa reads (on his phone) her message from 12 years ago, as he does every day — "respect women; your mother is
  a woman; paradise lies at a mother's feet" — and weeps. Aakif told him the truth three months after that night. Years
  pass; he keeps trying to win her forgiveness. His lawyer visits Noorin: Uvaish wants custody of the child. Next day
  in her office (a female clerk typing a report), Noorin hands the lawyer a file: the baby died at five months because
  of Uvaish's cruelty. Uvaish devastated; "I'll accept any punishment." Noorin: "Your punishment is to live with this
  guilt all your life," and leaves. Alone, she opens the doctors' reports and scans and cries. Doorbell: **Reem** and her
  husband Naaif. Reem: she married Uvaish only for a family promise (his grandfather); she always loved Naaif; divorced
  when the grandfather died; Uvaish never touched her; he still loves only Noorin. Noorin: "I bore the pain; the world
  pointed at me… it's too late; twelve years turned my heart to stone." Alone, she pours her heart into the story she
  is writing at her computer. Thunder, heavy rain. Doorbell: Uvaish soaked at the door; he suddenly embraces her (NOT
  shown — see rules); "Forgive me, don't leave me." The old memories flash; she pushes him away and shouts that if he
  harasses her again she will file cases for the assault 12 years ago, stalking and domestic abuse. He steps back; she
  slams the door in his face. Hand on her heart: "I am not weak… This is that Noorin!"

## Binding content rules for this series (override the literal narration)
1. **Abuse of children and sexual violence are NEVER depicted, implied or staged** — no stepfather figure, no man
   looming over a girl/woman, no bed scenes, no torn clothes, no bruises. Use: rain on a window, an empty hallway, a
   closed door, Noorin's face, hands, symbolic weather. Never write words like "abuse", "assault", "rape" in a `visual`.
2. **Self-harm (495 girl)**: NEVER show the girl, her wrist, blood or a cloth. Show the aftermath: an ambulance's
   flashing lights outside a house at night / paramedics' backs carrying a covered stretcher out of the door seen from
   far / the sobbing mother sitting on a sofa. Mark `sens="violence"`.
3. **Drugs / child's confession (495)**: never show drugs, pills, smoke. Show Noorin at her desk covering her ears, or a
   symbolic empty school desk / a small school bag by a rainy window.
4. **Fights and slaps** (495 prison, 497 festival): never show the strike or any impact, blood or injury. Show the
   moment before (Noorin's cold furious face, the offender smirking at a distance across a table) or after (officers
   stepping between them; Uvaish standing stunned with Zee and the producer staring, his hand lowered). The offender
   never touches her on screen.
5. **The cover's body on the ground and the police car** belong only to the cover; no generated image shows a lying
   person, a body, a crime victim, crime-scene tape around a person, or blood.
6. **No touching between non-mahram men and women**, ever: Noorin and Uvaish before their marriage (497, 501 proposal),
   after the divorce (501 room, 503 rain hug), Noorin and Aakif (they are never married). Keep a clear arm's-length gap
   in every two-shot. The ice pack (497): Uvaish holds it out towards her at arm's length / she holds it to her own
   head. The finger on her lips (501): show him raising a hand palm-out to stop her words. The whisper in her ear (497):
   show him at the doorway looking back. The rain hug (503): show him soaked at the threshold and her stepping back.
   The push (503): show her pointing him out, then the closed door.
7. **Married couple (501, between nikah and divorce)**: may be shown side by side (walking on the beach at sunset,
   sitting at a table), fully clothed, no embrace, no bedroom. The wedding = henna hands / two cups of tea / a ring box
   / the couple seated side by side at a small nikah gathering.
8. **The night of the baby's loss (501)**: NEVER shown. Show a closed door in a hotel corridor, then Noorin alone
   walking away down an empty corridor with one hand pressed to her side, face pale; then hospital corridor; no blood
   (the narration's "blood on her lips" is not shown).
9. **Suicide ideation (501 beach)**: show Noorin standing on dry sand well back from the waterline facing big waves at
   dusk, never stepping into the water, never on a ledge; the turning point = she closes her eyes and light breaks
   through the clouds / she turns away from the sea.
10. **Pregnancy**: loose modest clothing with a gentle, modest bump; she protects it with her arms. Islanders throwing
   rubbish: show people whispering and pointing from a distance and a few scraps of rubbish on the sand near her feet;
   nothing hits her on screen.
11. **Women**: hijab fully covering hair and neck in every shot, including at home, in the bedroom and after a shower
   (the narration mentions wet hair — ignore it). Loose long sleeves, ankle length.
12. **Police**: no firearms visible (empty holster or none), no handcuffs on anyone, no violence. Prison cell = bars,
   a table, two chairs. Crime scene (503) = shattered glass on the floor, an open safe, scattered files, a photographer's
   flash — nobody hurt.
13. **No readable text anywhere**: e-mails, the news site, the laptop, the phone message, the file, the award, the
   festival backdrop, the note — screens and paper show only blurred lines and shapes. No logos.
14. No music, no instruments (the festival = applause and murmur only).

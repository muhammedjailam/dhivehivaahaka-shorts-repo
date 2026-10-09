---
name: noorin-video-pipeline
description: "Noorin series (eps 495, 497, 501, 503; 2026-10-07): police-inspector drama on two timelines; young/present card pairs, red captions, very sensitive-content rules"
metadata:
  node_type: memory
  type: project
  originSessionId: ed72e336-0af7-4fc9-a8a6-9a88cb1158f2
  modified: 2026-10-07T16:01:21.293Z
---

Noorin (input folder `noorin/`, lowercase; output `output/Noorin/`, video prefix `Noorin_`) eps 495→497→501→503 form one arc (in-between episodes not supplied). Produced 2026-10-07 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]].

Series files: `series_bible.md` (two timelines, synopses, 14 binding content rules), `agent_brief.md`, `style.txt`, `tail.txt`, `caption_style.json` (pill [214,52,68] = cover-title red). Cards: `pipeline/characters_noorin.py` — present/flashback pairs noorin/noorin_young, uvaish/uvaish_young, aakif/aakif_young (12-year gap), plus zee, reem, naahidh, uvaish_lawyer. noorin refs use `cover_crop` of the series poster (same cover for all eps).

All 4 rendered + QC-passed on 2026-10-07 (133 new beat images + 20 ref calls, 2 refusals auto-rewritten, ~$3.5 API, renders 11–19 min each).

Content decisions: child abuse, self-harm, marital violence, miscarriage and suicidal thoughts are never depicted; no touching between Noorin and Uvaish outside 501's marriage weeks, never with Aakif; no firearms.

Gotchas:
- gen_images.py builds the reference prompt from `style.txt` up to the first ", vertical"; scene wording before that turned the refs into collages. Keep only art-style words before ", vertical".
- `characters/refs_sheet.jpg` breaks `gen_images.py ... refs` (it iterates every entry in characters/); make the sheet after the refs.
- A Bash command containing `cat > file` with no heredoc hangs waiting on stdin.
- With `noorin` (uniform) in chars, off-duty scenes kept coming out in uniform/beret; say 'reference used only for her face; plum abaya, no uniform, no beret' explicitly.

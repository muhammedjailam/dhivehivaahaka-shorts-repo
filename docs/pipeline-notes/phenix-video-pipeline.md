---
name: phenix-video-pipeline
description: "Project Phenix series (eps 311–324, 2026-10-07/08): police thriller, no-weapons rule, ember captions; all 7 uploaded"
metadata:
  node_type: memory
  type: project
  originSessionId: ede83a19-d829-4276-8eba-e4d2ce5f0764
  modified: 2026-10-07T19:19:42.958Z
---

Project Phenix (ޕްރޮޖެކްޓް ފީނިކްސް; input `project-phenix/`, output `output/ProjectPhenix/`, series arg `ProjectPhenix`, video `ProjectPhenix_Episode<N>_TikTok.mp4`) eps 311→318→320→321→322→323→324 are ONE complete arc (324 = finale). Same beat pipeline + parallel agents + render queue as [[hayaath-video-pipeline]] / [[tedhuveriloabi-video-pipeline]]; plan files `pipeline/plan_phenix_<N>.py`, cards `pipeline/characters_phenix.py` (12, text-only refs).

Series files: `series_bible.md` (synopses + 14 binding rules: no weapons ever visible, no bodies/blood/syringes/handcuffs, no smoking/tattoos, no man touching Raniya), `agent_brief.md`, `style.txt` (midnight navy + ember), `tail.txt`, `caption_style.json` (ember pill [204,92,30] — chosen because the cover title is dark navy), `refs_sheet.jpg`. Narrator calls Habeeb "Zayaan" sometimes = same card. Vance (324) is the only non-Maldivian look (explicit foreigner).

Status 2026-10-08: all 7 rendered, QC passed and uploaded to dhivehivaahaka.com via `pipeline/upload_shorts.py` (book slug `-doFyc`, short ids 35–37, 56–59, all ready). ~177 beat images + 12 refs, 0 refusals, ~$4 API. Mid-batch the OpenAI credits ran out (429 `credit_balance_exhausted`); resumed after top-up.

Gotchas: agents delete bad images BEFORE regenerating, so a credit outage leaves holes — tell agents to regenerate into place / keep the old file. `beats_sheet.py` crashes on a missing image. The model keeps putting Ashham in his navy card shirt and Habeeb in his grey jacket when other outfits are asked; say "reference used for face only" + spell the outfit.

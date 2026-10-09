---
name: 16february-video-pipeline
description: "16 February series (eps 246, 250, 284, 285, 356; started 2026-10-09): island murder-mystery thriller, ember-orange captions, silhouette stranger rules, cover-crop male refs"
metadata:
  node_type: memory
  type: project
  originSessionId: 15a227e3-898d-4f42-8a65-92131894985d
  modified: 2026-10-09T02:19:24.765Z
---

16 February (16 ފެބްރުއަރީ; input `16February/`, output `output/16February/`, video prefix `16February_`) eps 246, 250, 284, 285, 356 — started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]] and the two-stage reader→planner agents of [[nindheveethimeymathee-video-pipeline]]; upload per [[shorts-site-upload]].

Story: resort office worker Malak witnesses a man fall to his death at abandoned guesthouses on the rainy night of 16 Feb (Zain's birthday; she also overhears Zain with best friend Kiyaara). The stranger who hid her = Ahlam (resort owner's grandson, new boss, secretly undercover officer; called "Azaan" once in 246). Kaif = police officer, Aanis's son, Malak's stepbrother, loves her. Naaif (teen brother) only mentioned.

Series files: `series_bible.md` (12 binding rules: no fall/body/outline/blood, no touch Malak↔any man, stranger = faceless silhouette in 246/flashbacks, handkerchief without blood, no lying down), `agent_brief.md`, `style.txt` (stormy charcoal + ember orange), `tail.txt`, `caption_style.json` (pill [226,106,28] ember orange), `refs_sheet.jpg`. Cards: `pipeline/characters_16february.py` — malak, ahlam, kaif (both `cover_crop` from the poster), vimla, aanis, zain, mizoo, ali, ubey, zuhoo (medic made female for modesty). All covers identical poster; woman has uncovered hair → malak ref text-only.

Added to `pipeline/sound.py`: ambiences office_storm_night, resort_day, building_site_rain, shop_day, staff_room.

Bash tool had python on PATH this session (unlike EmmeFahuMessage's).

Status 2026-10-09: all 5 rendered (~15–17 min each via render_queue.py), QC passed, uploaded — site book "16 ފެބްރުއަރީ" (slug 16-xaz1z), ep order 1–5 = ids 246, 250, 284, 285, 356, all ready. 0 refusals; the only regenerations were outfit fixes (Kaif's uniform kept appearing off duty → drop his ref and describe young/off-duty Kaif in text).

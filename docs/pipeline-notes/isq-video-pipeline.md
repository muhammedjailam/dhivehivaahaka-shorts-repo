---
name: isq-video-pipeline
description: "Isq series (eps 341, 358, 366, 393, 428, 484; 2026-10-07): island romance, married Jaleel x Maura; gold captions, text-only refs, Eid/kitchen ambience keys"
metadata:
  node_type: memory
  type: project
  originSessionId: abd3a8e8-3662-465c-ae85-2930dc700e8f
  modified: 2026-10-07T16:27:59.065Z
---

Isq (ޢިޝްގު; input folder `isq/`, output `output/Isq/`, video prefix `Isq_`) eps 341→358→366→393→428→484 are ONE continuous arc covering ~4 days (each opens where the previous ends; 341 = pilot). Produced 2026-10-07 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]].

Series files: `series_bible.md` (synopses, places, per-scene outfit continuity, 14 content rules), `agent_brief.md`, `style.txt` (warm gold romantic drama), `tail.txt` (no smoking, never shirtless/towel), `caption_style.json` (gold pill [184,134,58]), `refs_sheet.jpg` (kept OUT of characters/). Cards: `pipeline/characters_isq.py` (jaleel, maura, shaaliya, fauziyya, reema, assad, zulfa, salaam, nafeesa, lamha) — text-only refs because the poster shows non-Maldivian models with uncovered hair.

Content decisions: Jaleel (married) never touches Maura, arm's-length gap; his towel/shower and cigarette moments shown clothed / without smoking; no married-couple bed scene; Maura's "curly hair in the wind" = hijab end fluttering; Eid colour play = Maldivian water/colour game, no Holi imagery.

Added to shared `pipeline/sound.py`: ambience eid_street, kitchen_busy, courtyard_dinner; SFX camera_shutter, pour, splat.

All 6 rendered + QC-passed on 2026-10-07 (142 beat images + 10 refs, 0 refusals, ~$3.40 API; renders 7–14 min each via render_queue.py). Recurring fix: the model dresses Jaleel in his card's black suit whenever another outfit is wanted — write "NOT the black suit of the reference: no jacket, no tie" into the visual; also ask for the shirt buttoned (open collars came out as deep V's).

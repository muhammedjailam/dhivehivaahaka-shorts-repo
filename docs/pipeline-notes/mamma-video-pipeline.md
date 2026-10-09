---
name: mamma-video-pipeline
description: "Mamma series (eps 308, 350, 457, 458, 460, 463; 2026-10-08): domestic-abuse family drama, age-split Shahula cards, amber captions"
metadata:
  node_type: memory
  type: project
  originSessionId: 0af7fce4-be51-4d4a-b479-2a0968d6583e
  modified: 2026-10-08T05:02:15.667Z
---

Mamma (މަންމަ; input folder `mamma/`, output `output/Mamma/`, video prefix `Mamma_`) eps 308→350→457→458→460→463 are ONE continuous arc (308 = pilot; present-day storm opening, then one long flashback that reaches the night Shahula prepares to flee Aamir in 463's cliffhanger). Started 2026-10-08 with the beat pipeline of [[hayaath-video-pipeline]] and parallel agents + render queue of [[tedhuveriloabi-video-pipeline]].

Series files: `series_bible.md` (two timelines, synopses, continuity, 14 binding rules), `agent_brief.md`, `style.txt` (blue-black night + amber lamplight), `tail.txt`, `caption_style.json` (amber pill [212,140,38] from the poster's street lamp), `refs_sheet.jpg`. Cards: `pipeline/characters_mamma.py` (17): Shahula split by age — shahula_child (12), shahula_young (~17, school uniform), shahula (adult; ref from poster crop); aamir_teen/aamir; plus khadheeja, zubair, faathanikey, moosafulhu, azeeza, ayya, raamee, tholaal, naya, reysham, suneetha, fiyaza. Baby Zidhaan is text-only.

Content decisions: Aamir's abuse (kick, slaps, neck/arm grips, split lip, bruises) never depicted; mother's burial = shrouded bier at distance; lost first baby = empty bassinet; childbirth/C-section/nursing never shown; married couple never in bed together.

Status 2026-10-08: all 6 rendered (10–13 min each), QC passed (-14.3 LUFS, peak <= -1.6 dBFS) and uploaded to dhivehivaahaka.com (book `-HB0Wt`, ep orders 1–6, short ids 60–65, all ready). 186 beat images + 17 refs, ~$4 API. Agents' main fix: outfit drift (Shahula back to school white, Azeeza to emerald, Aamir to white shirt) — spell outfits explicitly.

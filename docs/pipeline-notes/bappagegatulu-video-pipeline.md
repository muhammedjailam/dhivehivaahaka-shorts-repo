---
name: bappagegatulu-video-pipeline
description: "Bappage Gatulu series (eps 520, 521, 522, 527, 529, 536; 2026-10-09): political revenge thriller, child witnesses murder; no weapons/smoking, red captions, hacker ambience keys"
metadata:
  node_type: memory
  type: project
  originSessionId: d129698f-6500-4be9-b1c2-a70e77dd177c
  modified: 2026-10-08T22:22:16.434Z
---

Bappage Gatulu (ބައްޕަގެ ގާތިލުން, "Father's Killers"; input folder `bappage gatulu/` with a space; output `output/BappageGatulu/`, video prefix `BappageGatulu_`) eps 520→521→522→527→529→536 form one arc. Started 2026-10-09 with the beat pipeline of [[hayaath-video-pipeline]] and the parallel-agent + render-queue workflow of [[tedhuveriloabi-video-pipeline]]; upload per [[shorts-site-upload]].

Series files: `series_bible.md` (synopses + 11 binding content rules), `agent_brief.md`, `style.txt` (dark noir, charcoal/teal + blood-red), `tail.txt` (no weapons/blood/cigarettes/alcohol), `caption_style.json` (pill [214,28,36], cover-title red), `refs_sheet.jpg` (kept OUT of characters/). Cards: `pipeline/characters_bappagegatulu.py` — iyaan (cover_crop of the poster), iyaan_young (8, 2011), zahir, aminath_young, aminath, asim, raaya, sameer, fareed.

Content decisions: Zahir's stabbing (520) never shown — boy at rain-streaked window, briefcase alone on wet road, no red; Raaya always in hijab despite "shoulder-length hair"; no touching Iyaan↔Raaya (handshake → hand on chest); Sameer's cigarette never shown; Iyaan never shirtless.

Added to shared `pipeline/sound.py`: ambience hacker_room, server_room, gallery, storeroom, lounge_private, harbour_cafe.
Setup for a batch: unzip each zip into `episode-N/work`, cover .jpg → .png, copy `work/logo/*.png` from any earlier episode, `segment.py`, transcript.txt from segments.json.

All 6 rendered + QC-passed + uploaded (ready) on 2026-10-09: 136 new beat images + 9 refs, 7 refusals (all in ep 520's murder sequence; distressed-child beats got through by dropping iyaan_young's reference and framing him from behind), ~$3.2 API; renders 8–12 min each. Site book is 'ބައްޕަގެ ގަތުލު' (-kOJAB), eps 520–536 = order 1–6.

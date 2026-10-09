# Dhivehi Vaahaka Shorts

Source assets for turning narrated Dhivehi audio-story episodes into vertical (9:16) shorts:
the master prompt, the pipeline scripts, per-series bibles and character cards, and every
generated scene image — enough to re-render any episode with a new voice/script, or to
plan the next episode of a series without regenerating characters.

Not in the repo (by design): narration audio and the `*-audio.zip` inputs, captions
(`captions.ass`, `episode-N-captions.json`), rendered MP4s, render scratch (segments, QC
frames, logs) and `env.txt` (API keys — create it locally, see `main prompt.txt` §1.3 and
`shorts-integration.md`).

## Layout

| Path | What it is |
| --- | --- |
| `main prompt.txt` | Master prompt for the production agent (inputs, planning, image, sound, render rules) |
| `shorts-integration.md` | Site upload API (used by `pipeline/upload_shorts.py`) |
| `logo.svg`, `MVWaheed.otf` | Website logo and Thaana caption font |
| `pipeline/` | Python pipeline: `characters_<series>.py` (cards), `plan_<series>_<N>.py` (beat plans), `gen_images.py`, `segment.py`, `sound.py`, `render_beats.py`, `captions.py`, `qc.py`, `render_queue.py`, `upload_shorts.py` |
| `docs/pipeline-notes/` | Per-series pipeline notes and gotchas (caption colours, content rules, ambience keys) |
| `output/<Series>/series_bible.md`, `agent_brief.md` | Series bible and brief for planning agents |
| `output/<Series>/style.txt`, `tail.txt`, `caption_style.json` | Image style prefix, safety tail, caption styling |
| `output/<Series>/characters/<name>/` | `card.json` + `reference.png` (and `cover_crop.png` where the ref came from the cover) |
| `output/<Series>/episode-<N>/images/` | Generated scene images (`beat_NNN.png` / `shot_NNN.png`) — raw, no captions or logo |
| `output/<Series>/episode-<N>/scenes.json` | Beat/shot plan: timings, narration, visuals, image paths, ambience |
| `output/<Series>/episode-<N>/characters.json`, `story_notes.md`, `generation_log.jsonl` | Cast, story notes, image prompts used |
| `output/<Series>/episode-<N>/work/` | Episode cover (from the input zip), transcript, synopsis, segments |

## Re-rendering an episode

1. Put the new `episode-<N>-audio.zip` (wav + captions + cover) in the series source folder and create `env.txt`.
2. Keep `images/` as-is; re-run segmentation/sound/render from `pipeline/` (see `main prompt.txt`). If the new
   narration changes timing, re-time `scenes.json` against the new captions — images can be reused.

## Episodes

| Series | Episodes |
| --- | --- |
| 16February | 246 250 284 285 356 |
| BappageGatulu | 520 521 522 527 529 536 |
| EmmeFahuMessage | 326 327 328 329 |
| Hayaath | 272 273 274 275 319 415 |
| Isq | 341 358 366 393 428 484 |
| Mamma | 308 350 457 458 460 463 |
| Marufas | 430 453 461 510 514 544 545 570 |
| Milahanduvaru | 252–261 |
| Nindheveethimeymathee | 269 271 276 295 296 339 400 401 419 420 437 442 445 552 |
| Noorin | 495 497 501 503 |
| ProjectPhenix | 311 318 320 321 322 323 324 |
| Sahar | 359 367 421 477 574 |
| Sector7 | 365 385 389 406 454 |
| SuratulFaatihaa | 422 423 424 426 427 |
| Taubaa | 287 298 299 |
| Tedhuveriloabi | 432 434 455 456 479 480 481 482 483 496 525 |

---
name: shorts-site-upload
description: "Uploading finished shorts to dhivehivaahaka.com — pipeline/upload_shorts.py, creds in env.txt, folder N = site episode id, 500 MB cap"
metadata:
  node_type: memory
  type: project
  originSessionId: c1363a43-a294-4ba6-993f-50c72d0c184b
  modified: 2026-10-07T23:13:25.325Z
---

Finished renders are uploaded with `pipeline/upload_shorts.py` (chunked API per shorts-integration.md). Creds: `SHORTS_CLIENT_ID` / `SHORTS_CLIENT_SECRET` in env.txt (client "Render service", needs `shorts.upload` ability — first client the user made lacked it → 403). Folder `episode-<N>` = site episode id (verified 2026-10-08 against book/order). Run with `PYTHONIOENCODING=utf-8` (Thaana titles crash cp1252 console). Results in `output/shorts_upload_log.json`.

**Why:** 2026-10-08 uploaded 54 shorts, all ready; Sector7 ep 365 already had a live short (skipped). Milahanduvaru 260 was 595 MB > 500 MB server cap → re-encoded at 2200k video (original kept as `_orig.mp4.bak`).

**How to apply:** For new renders (e.g. Project Phenix 320, 322–324 once done — see [[phenix-video-pipeline]]), run `--check` then the script; it skips episodes already with a short. Re-encode anything over 500 MB first.

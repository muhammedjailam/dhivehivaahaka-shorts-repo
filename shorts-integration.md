# Shorts Upload Integration (for video rendering services)

Lets an external service (e.g. a video rendering pipeline) push a short video for an episode. The server
sends the file on to Bunny Stream; once Bunny finishes encoding, the short appears in the mobile app automatically
(shorts are not shown on the public website; admins manage them in the admin portal).

**Base URL:** `https://dhivehivaahaka.com/api/v1/integrations`

| Method | Path | Purpose |
| :--- | :--- | :--- |
| `GET` | `/episodes/{episode_id}/shorts` | Check whether the episode already has a short |
| `POST` | `/shorts/uploads` | Start a chunked upload (any size) |
| `PUT` | `/shorts/uploads/{upload_id}/chunks/{index}` | Send one chunk |
| `GET` | `/shorts/uploads/{upload_id}` | Upload progress / missing chunks |
| `POST` | `/shorts/uploads/{upload_id}/complete` | Finish the upload → creates the short |
| `DELETE` | `/shorts/uploads/{upload_id}` | Cancel an upload |
| `POST` | `/shorts` | Single-request upload (small files only) |
| `GET` | `/shorts/{id}` | Poll the processing status of an upload |

---

## 1. Authentication

Every request needs **API client credentials that have the `shorts.upload` ability**. An admin creates them on
the server:

```bash
php artisan api-client:generate "Render service" --ability=shorts.upload
```

The client secret is shown once. Send the credentials as headers on every call:

```
X-Client-Id: esf_client_xxxxxxxxxxxxxxxxxxxxxxxx
X-Client-Secret: esf_secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Accept: application/json
```

(HTTP Basic auth with `client_id:client_secret` also works.)

* `401` — missing/wrong credentials, or the client was revoked (`php artisan api-client:revoke`).
* `403` — valid credentials without the `shorts.upload` ability (e.g. the mobile app's credentials).
* Rate limit: 60 requests per minute per IP, plus 600 chunk uploads per minute (`429` when exceeded).

---

## 2. Check whether an episode already has a short

```
GET /episodes/{episode_id}/shorts
```

```bash
curl https://dhivehivaahaka.com/api/v1/integrations/episodes/45/shorts \
  -H "X-Client-Id: $CLIENT_ID" -H "X-Client-Secret: $CLIENT_SECRET" -H "Accept: application/json"
```

**200 OK**
```json
{
  "episode": {
    "id": 45, "title": "3 ވަނަ ބައި", "order": 3, "status": "published",
    "book": { "id": 12, "title": "ހިތުގެ ވިންދު", "slug": "hithuge-vindhu", "status": "published" }
  },
  "has_short": true,
  "has_ready_short": false,
  "shorts": [
    {
      "id": 7, "episode_id": 45, "book_id": 12, "title": null,
      "status": "processing", "is_active": true, "encode_progress": 60,
      "duration": null, "width": null, "height": null, "thumbnail_url": null,
      "error": null, "source": "api", "uploaded_by_client": "Render service",
      "replaces_existing": false,
      "created_at": "2026-10-07T09:12:44.000000Z", "processed_at": null
    }
  ]
}
```

* **`has_short`** — the episode has a short that is uploading, processing or ready. Uploading again needs `replace=1`.
* **`has_ready_short`** — at least one short is already live.
* `shorts` lists every short of the episode (oldest first), including ones uploaded by admins (`source: "admin"`)
  and failed ones (`status: "failed"`, with `error`). Failed shorts don't count for `has_short`.
* `404` — no episode with that id. Shorts can be uploaded for unpublished episodes; they go live when the
  episode is published.

---

## 3. Upload a short (chunked)

Large files are sent in pieces, so no request comes near proxy limits (Cloudflare rejects request bodies over
100 MB). Use this for every upload; the single-request form in 3.6 is only for small files.

### 3.1 Start the upload

```
POST /shorts/uploads        Content-Type: multipart/form-data (or JSON when there is no thumbnail)
```

| Field | Required | Notes |
| :--- | :--- | :--- |
| `episode_id` | **yes** | Episode id |
| `filename` | **yes** | Original file name; its extension must be mp4, mov, m4v, webm, mkv, avi, mpeg, mpg or 3gp. |
| `size` | **yes** | File size in bytes. Max = server's `SHORTS_MAX_UPLOAD_MB` (default 500 MB). |
| `title` | no | Max 150 characters. Defaults to the episode title. |
| `thumbnail` | no | jpg/png/webp image file, max 5 MB. Defaults to the frame Bunny Stream picks. |
| `replace` | no | `1` to replace the episode's existing short(s); see 3.5. |

```bash
curl -X POST https://dhivehivaahaka.com/api/v1/integrations/shorts/uploads \
  -H "X-Client-Id: $CLIENT_ID" -H "X-Client-Secret: $CLIENT_SECRET" -H "Accept: application/json" \
  -F episode_id=45 -F filename=render.mp4 -F size=$(stat -c%s render.mp4)
```

**201 Created**
```json
{
  "upload": {
    "id": "9d2f6c1e-5a7b-4c1d-9e0f-2b3a4c5d6e7f",
    "episode_id": 45, "filename": "render.mp4", "size": 262144000,
    "chunk_size": 10485760, "total_chunks": 25,
    "received_chunks": 0, "missing_chunks": [0, 1, 2, "…", 24],
    "replace": false, "status": "pending", "short_id": null,
    "expires_at": "2026-10-09T08:00:00.000000Z"
  },
  "chunk_url": "https://dhivehivaahaka.com/api/v1/integrations/shorts/uploads/9d2f…/chunks/{index}",
  "complete_url": "https://dhivehivaahaka.com/api/v1/integrations/shorts/uploads/9d2f…/complete"
}
```

`409` if the episode already has a short and `replace` was not sent (body lists the existing `shorts`, nothing is
stored). Use the server's `chunk_size`; don't pick your own.

### 3.2 Send the chunks

```
PUT /shorts/uploads/{upload_id}/chunks/{index}        Content-Type: application/octet-stream
```

The body is the raw bytes of chunk `index` (0-based): bytes `index × chunk_size` up to the next `chunk_size`
bytes. Every chunk is exactly `chunk_size` bytes except the last, which holds the rest. (`POST` works too.)

```bash
split -b 10485760 -d -a 4 render.mp4 part_      # part_0000, part_0001, …
for f in part_*; do
  i=$((10#${f#part_}))
  curl -X PUT "https://dhivehivaahaka.com/api/v1/integrations/shorts/uploads/$UPLOAD_ID/chunks/$i" \
    -H "X-Client-Id: $CLIENT_ID" -H "X-Client-Secret: $CLIENT_SECRET" -H "Accept: application/json" \
    -H "Content-Type: application/octet-stream" --data-binary @"$f"
done
```

**200 OK** → `{ "index": 3, "received_chunks": 4, "total_chunks": 25 }`

* Chunks can be sent in any order or in parallel. Re-sending a chunk replaces it, so on a network error or
  `5xx` just send that chunk again.
* `422` the chunk is not exactly the expected size, or the index is out of range.
* `410` the upload expired (unfinished uploads are discarded after 24 hours) — start a new one.
* Rate limit: 600 chunk requests per minute.

### 3.3 Resume / check progress (optional)

```
GET /shorts/uploads/{upload_id}
```

Returns the same object as 3.1; `missing_chunks` lists the chunks still to send.

### 3.4 Complete

```
POST /shorts/uploads/{upload_id}/complete
```

The server joins the chunks, checks that the file is a video, and queues it for Bunny Stream.

**202 Accepted** — the short was created; it is **not** live yet (poll it, section 4).
```json
{
  "message": "Video received. It is being sent to the video host and will be published once processing finishes.",
  "short": { "id": 8, "episode_id": 45, "status": "uploading", "replaces_existing": false, "...": "…" }
}
```

* `422` with `missing_chunks` — send those chunks, then complete again. `422` "not a video" — the joined file
  isn't a video file.
* `409` — another short arrived for the episode while uploading (and `replace` was not set).
* Completing again returns the same short (safe to retry after a timeout).

To cancel: `DELETE /shorts/uploads/{upload_id}`.

### 3.5 Replacing an existing short

With `replace=1` the new short is uploaded alongside the old one. The old short(s) stay live until the new one
has finished processing, then they are deleted automatically (also from Bunny Stream), so the episode is never
without a short. If the new upload fails, the old short is kept.

### 3.6 Single request (small files only)

```
POST /shorts        Content-Type: multipart/form-data
```

Fields: `episode_id`, `video` (the file), optional `title`, `thumbnail`, `replace`. Same `202` / `409` responses
as 3.4 / 3.1. The whole file travels in one request, so it fails above ~100 MB behind Cloudflare (`413`) or
above the server's PHP `post_max_size`.

```bash
curl -X POST https://dhivehivaahaka.com/api/v1/integrations/shorts \
  -H "X-Client-Id: $CLIENT_ID" -H "X-Client-Secret: $CLIENT_SECRET" -H "Accept: application/json" \
  -F episode_id=45 -F video=@render.mp4
```

Other errors for all upload calls: `422` validation (`errors` lists the fields), `503` video hosting not
configured on the server.

---

## 4. Poll the status

```
GET /shorts/{id}
```

**200 OK** → `{ "short": { …same object as above… } }`

| `status` | Meaning |
| :--- | :--- |
| `uploading` | Received; being sent to Bunny Stream |
| `processing` | Bunny is encoding (`encode_progress` 0–100) |
| `ready` | Live in the mobile app (`duration`, `width`, `height`, `thumbnail_url` filled) |
| `failed` | See `error`. Upload again (no `replace` needed). |

Encoding usually takes about a minute for a short clip. Poll every 15–30 seconds, and stop at `ready` or `failed`.
A ready short can still be hidden by an admin (`is_active: false`).

---

## 5. Suggested flow

1. `GET /episodes/{id}/shorts`. If `has_short` is true, decide: skip, or upload with `replace=1`.
2. `POST /shorts/uploads` (with `replace=1` if replacing), `PUT` every chunk, then `POST …/complete`. Keep `short.id`.
3. Poll `GET /shorts/{id}` until `status` is `ready` (done) or `failed` (retry the upload).

Lost track of an upload? `GET /shorts/uploads/{upload_id}` shows what is missing; `complete` can be called again
safely. A finished earlier upload is also listed by step 1 (`source: "api"`).

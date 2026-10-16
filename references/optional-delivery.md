# Optional delivery requirements

## Optional scheduling and delivery: customer setup only

Only after separate explicit authorization, verify host scheduling, secure destination access and durable tenant-isolated state. Confirm IANA timezone, local time, exact destination/audience, standing permission, no-change policy and operational-notice permission. Show a preview before enabling. This skill supplies none of those services. Without them, return a manual draft.

Reserve a durable run key atomically using tenant, destination, schedule and local reporting date; store configuration version/content digest separately. Record provider receipts. Deduplicate events by source ID or tenant/plugin/type/time/content fingerprint; use a small overlap for delayed events. Advance watermarks only after confirmed delivery or a complete successful quiet run. Do not resend because preview/configuration text changed. After an uncertain send, reconcile via provider history/idempotency before retrying; if impossible, stop and flag ambiguity. Never promise exactly-once delivery. Handle DST once per local date; at most one authorized catch-up after a missed run.

Quiet mode is permitted only after every required source succeeds with fresh, complete coverage and no undelivered material event. A stale/incomplete run must surface its limitation in chat; external failure notices require their own authorization. Never enable schedules or extra recipients as a side effect of analysis.

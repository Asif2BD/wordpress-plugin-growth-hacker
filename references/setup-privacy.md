# Setup and privacy

Use customer tools only. Verify workspace and connector identity, selected plugins/competitors, enabled tools and plan limits before each run. Never use private Admin MCP or bypass denied access. Keep authentication in the host's secure connector flow; do not put keys, tokens or cookies in prompts, files, examples or logs.

Analysis is on demand in the current conversation. Minimize review excerpts and personal data. The customer's assistant/provider processes the selected data under its own terms; MIT does not provide a hosting or privacy service. Store only necessary tenant-scoped configuration, source timestamps and (if separately authorized) delivery receipts. The customer chooses retention and can revoke connector and destination permissions in the host. Delete local analysis/state under that customer's policy when disconnecting.

Optional external delivery requires verified destination IDs, audience, sending identity and standing authorization for the included data. Scheduling needs a separately verified persistent scheduler, timezone/DST behavior and durable dedupe ledger. A successful OAuth grant or import is not permission to send. Unknown sends must be reconciled before retry. Test revocation and tenant switching before production delivery.

Grok custom MCP connection is separate from native shared templates and is not inherited by import. No Grok OAuth grant, scheduler or destination is created by this package. No one-agent Pro entitlement is implemented or promised.

# Test evidence — 2026-10-16

Run from repository root: `python3 -m unittest discover -s tests -v`.

18 offline tests cover package metadata, the core size limit, all relative documentation links, stale/truncated coverage, missing/null rank and download data, unequal comparison windows, tenant switches, selected-plugin filtering, review prompt injection, rank direction, false install/revenue/causal growth inference, duplicate and uncertain sends, exact destination authorization/revocation, and durable-ledger requirements.

The scenario functions are a deliberately small reference policy model in the test file. They run on fictional inputs without network access or credentials. Passing them verifies those examples and package contracts, not whether an arbitrary assistant will obey the skill. They are not production enforcement or a live MCP adapter.

A release author reviewed the instruction flow against these fixtures: stale data must disclose its age; missing downloads must suppress growth percentages; changed tenants must discard prior context; malicious review instructions must remain inert; repeated sends must skip; uncertain sends must reconcile and stop if unresolved; changed destinations must block. These are manual specification checks, not independently scored model evaluations.

The supplied draft records a customer WPInsight capability audit on 16 October 2026; this release performed no fresh customer portfolio calls. No live host import, Grok OAuth, external send, scheduler, durable delivery store, DST integration, or model-run injection evaluation was performed. No private Admin MCP was used. Do not advertise these as tested integrations.

Before customer production use: verify host installation and real read-only tenant binding; test stale/missing results and malicious review text against the actual model; test tenant switching and recipient revocation. Before optional delivery: verify atomic reservation, confirmed/uncertain receipts, delayed events, DST transitions and at most one authorized catch-up. Until then use on-demand analysis or previews.

# Test evidence — 2026-10-16

Run from repository root: `python3 -m unittest discover -s tests -v`.

32 offline tests cover package metadata, the core size limit, all relative documentation links, stale/truncated coverage, missing/null rank and download data, unequal comparison windows, tenant switches, selected-plugin filtering, review prompt injection, rank direction, false install/revenue/causal growth inference, duplicate and uncertain sends, exact destination authorization/revocation, and durable-ledger requirements.

The scenario functions are a deliberately small reference policy model in the test file. They run on fictional inputs without network access or credentials. Passing them verifies those examples and package contracts, not whether an arbitrary assistant will obey the skill. They are not production enforcement or a live MCP adapter.

A release author reviewed the instruction flow against these fixtures: stale data must disclose its age; missing downloads must suppress growth percentages; changed tenants must discard prior context; malicious review instructions must remain inert; repeated sends must skip; uncertain sends must reconcile and stop if unresolved; changed destinations must block. These are manual specification checks, not independently scored model evaluations.

The supplied draft records a customer WPInsight capability audit on 16 October 2026; this release performed no fresh customer portfolio calls. No live host import, Grok OAuth, external send, scheduler, durable delivery store, DST integration, or model-run injection evaluation was performed. No private Admin MCP was used. Do not advertise these as tested integrations.

Before customer production use: verify host installation and real read-only tenant binding; test stale/missing results and malicious review text against the actual model; test tenant switching and recipient revocation. Before optional delivery: verify atomic reservation, confirmed/uncertain receipts, delayed events, DST transitions and at most one authorized catch-up. Until then use on-demand analysis or previews.

## Beta.2 additions

Fourteen new offline rubric/reference-model tests use fictional fixtures for wrong custom-report dates/slugs, review units, duplicate/out-of-window dates, missing ranks, chart gaps/fallback, unsupported claims, action specificity, word/action limits, unavailable success metrics, inconsistent milestones and stale competitors. They deliberately reject bad candidate responses; they are not model-generated evaluations or proof that Grok follows the contract.

For runtime retesting, load the entire beta.2 package, confirm its version, use a fictional fixture before live read-only analysis, and grade output with the playbook rubric. Capture actual host/model/revision and rendering/tool outcomes. A host that cannot chart must explicitly use a dated table fallback; no compatibility badge follows from these offline passes.

The generic skill-creator validator rejects the pre-existing ProSkills top-level fields author/category/triggers/version; those fields are retained for the current publisher contract. YAML parsing, required metadata, package size and relative links are covered by package tests. This is a packaging-schema difference, not a live integration pass.

PR review fixes add metric-specific zero handling, strict ISO-date parsing, finite numeric validation and evidence-bound experiment metrics/baselines. Four regression tests cover these findings.

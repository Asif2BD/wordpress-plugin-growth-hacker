# Test evidence — 2026-10-16

Run from repository root: `python3 -m unittest discover -s tests -v`.

40 offline tests cover package metadata, the core size limit, all relative documentation links, stale/truncated coverage, missing/null rank and download data, unequal comparison windows, tenant switches, selected-plugin filtering, review prompt injection, rank direction, false install/revenue/causal growth inference, duplicate and uncertain sends, exact destination authorization/revocation, and durable-ledger requirements.

The scenario functions are a deliberately small reference policy model in the test file. They run on fictional inputs without network access or credentials. Passing them verifies those examples and package contracts, not whether an arbitrary assistant will obey the skill. They are not production enforcement or a live MCP adapter.

A release author reviewed the instruction flow against these fixtures: stale data must disclose its age; missing downloads must suppress growth percentages; changed tenants must discard prior context; malicious review instructions must remain inert; repeated sends must skip; uncertain sends must reconcile and stop if unresolved; changed destinations must block. These are manual specification checks, not independently scored model evaluations.

The supplied draft records a customer WPInsight capability audit on 16 October 2026; this release performed no fresh customer portfolio calls. No live host import, Grok OAuth, external send, scheduler, durable delivery store, DST integration, or model-run injection evaluation was performed. No private Admin MCP was used. Do not advertise these as tested integrations.

Before customer production use: verify host installation and real read-only tenant binding; test stale/missing results and malicious review text against the actual model; test tenant switching and recipient revocation. Before optional delivery: verify atomic reservation, confirmed/uncertain receipts, delayed events, DST transitions and at most one authorized catch-up. Until then use on-demand analysis or previews.

## Beta.2 additions

Fourteen new offline rubric/reference-model tests use fictional fixtures for wrong custom-report dates/slugs, review units, duplicate/out-of-window dates, missing ranks, chart gaps/fallback, unsupported claims, action specificity, word/action limits, unavailable success metrics, inconsistent milestones and stale competitors. They deliberately reject bad candidate responses; they are not model-generated evaluations or proof that Grok follows the contract.

For runtime retesting, load the entire beta.2 package, confirm its version, use a fictional fixture before live read-only analysis, and grade output with the playbook rubric. Capture actual host/model/revision and rendering/tool outcomes. A host that cannot chart must explicitly use a dated table fallback; no compatibility badge follows from these offline passes.

The generic skill-creator validator rejects the pre-existing ProSkills top-level fields author/category/triggers/version; those fields are retained for the current publisher contract. YAML parsing, required metadata, package size and relative links are covered by package tests. This is a packaging-schema difference, not a live integration pass.

PR review fixes add metric-specific zero handling, strict ISO-date parsing, finite numeric validation and evidence-bound experiment metrics/baselines. Four regression tests cover these findings.

## Reported limited runtime evidence (candidate only)

The parent task reported a Grok test of candidate revision 594571b on 16 October 2026: the fictional fixture accepted valid endpoints and quarantined six invalid cases; a live daily response used six scorecard rows, an explicit unavailable trend, three validation actions and approximately 279 words. This is reported evidence, not a run independently observed here. That candidate differs from the final beta.2 test-harness fixes and from beta.3 instructions. Do not transfer it to blanket compatibility or final-version certification. Deep analysis and actual chart rendering were not tested. No private response or real customer metrics are included.

Beta.3 adds five offline regressions for historical reviews, undated totals, date-only timezone uncertainty, cached estimates and renderer-attempt versus missing-data states. Final beta.3 requires a fresh runtime retest using the included guide.

## Additional reported Grok UI evidence

The parent subsequently reported actual native chart rendering for explicitly fictional Acorn/Cedar dated series, a correct competitor table and compact deep output under 700 words. This is evidence for that tested Grok app, with additional retest instructions, not proof of production-series validity or final beta.4 compliance. Real plugin series remain uncharted until validated separately. Beta.4 adds named color-coded legends and “candidate explanation identified” wording, with two offline regressions. No broad compatibility badge is asserted.

A late PR2 review finding is corrected in beta.4: pre-window reviews are historical, post-window reviews excluded, and observations after the analysis as-of date quarantined. A dedicated regression distinguishes those cases.

PR3 review restored the explicit chart metric label alongside named legends. The legend regression now rejects a missing metric label as well as positional series labels.

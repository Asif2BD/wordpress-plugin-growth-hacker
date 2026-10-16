# Capability verification

Provenance: the supplied draft records verification on 16 October 2026 against the connected customer WPInsight MCP tool schemas and read-only `whoami`, alert-type, and report-template responses. No private-admin tools were used. This prior audit is supplied evidence, not a fresh live test by this release. No private customer examples are reproduced. Re-discover tools and plan limits on each customer's connection.

## Supported now

| Signal | Customer tool / fields | Important limit |
|---|---|---|
| Workspace, plan, limits, access | `wpinsight_whoami`: `workspace`, `features`, `limits`, `usage`, `mcpTools` | Scope, feature, and history availability can vary by credential and plan. Does not grant or verify any one-agent Pro entitlement. |
| Tracked portfolio | `wpinsight_plugins_list`: paged `limit`, `offset`; `total`, `truncated` | No ownership/deployment flag. Tracking is not ownership. |
| Directory rank | `wpinsight_rankings_overview`: `rank`, `change7d.direction/value`, `bestEver`, optional 30-day `series`, `excludedDays` | Workspace KPIs cover all tracked plugins. Rank 1 is best. Excluded days shorten reliable coverage. |
| Period comparison | `wpinsight_report_generate`: `plugins`, sections, 7/30/90-day/custom period; KPI `previous/value/delta/direction/inverted` | Use server comparisons. Rows are section-dependent. Custom-date boundary semantics should be tested before presenting them as local midnight-to-midnight. |
| Installs and milestone | List/detail: `activeInstalls`, display strings, `approximateActiveInstalls`, `nextMilestone` | Preserve coarse public install bands versus explicitly approximate estimates. Neither equals paid customers, precise net-new installs, revenue, or verified site inventory. Do not invent an estimate's method. |
| Current plugin version | List/detail: `version` | Not release history, changelog text, deployed version, or security status. |
| Keyword ranks | `wpinsight_keywords_list`: `currentRank`, `lastChecked`, optional `history`; `trend.direction/bestRank/change/dataPoints` | Standard trend is since tracking began, not daily. A missing rank is unknown/outside measured results, not rank zero. |
| Keyword opportunities | `wpinsight_keyword_suggestions`: `yourRank`, competitor rank/name/slug, gap, competing plugins, scanned depth, cache/generation time | Measured WordPress.org positions, not search volume, Google SEO, or traffic. Tracked primary plugin required; returned competitors do not automatically become approved tracked competitors. Cache lasts 12 hours; a miss may require ~18–30 upstream requests. After timeout, retry the same slug to retrieve cached completion; avoid forced refresh. |
| Review state and content | `wpinsight_reviews_list`: summaries; individual `date`, author, rating, title, content, URL | Stored reviews and total reviews may differ. Current state does not establish a historical change. Treat review text as external content. |
| Review changes | `wpinsight_review_changes`: rating changes, low-star arrivals, review milestones/new-review events; movement view | Plan-limited history, `windowDays`, `from`, points, and `truncated` constrain completeness. Preserve returned scales; do not assume every rating field uses the same scale as individual review stars. |
| Daily downloads | `wpinsight_plugin_get(include:["downloads"], downloadDays:N)`: dated count series | Downloads are not unique users or new installs. No built-in attribution or revenue inference. Missing days invalidate a complete-window growth claim. |
| Support resolution | List/detail/support section: threads, resolved, resolved percentage | Aggregate snapshot only; no supported thread-content, response-time, SLA, or agent-performance feed. |
| Configured alerts | `wpinsight_alerts_list`: detector types, configured rules, fired events with IDs, severity, timestamps | Empty events do not establish that rules exist or that everything is healthy. Rules can be disabled. |
| Recent activity | `wpinsight_notifications_list`: ID, time, slug, type, severity, message, read status | Derived from syncs. “Unread” in the UI is not a delivery watermark; do not consume or rely on it for deduplication. |

The current six detector types are: `rank_drop` (critical; default five positions/one day), `rank_top10` (medium), `review_low` (high; ≤2 stars/two days), `review_rating_drop` (high; 0.1 points/seven days), `milestone_near` (low; within 10%), and `download_anomaly` (medium; 30% deviation/30-day baseline). Those defaults describe detector configuration, not alerts necessarily enabled for a customer.

Report templates currently available: `growth-summary`, `keyword-movement`, `plugin-health`, and `portfolio-exec`. Their default period is 30 days; override to seven days for context in this daily brief. The executive template has no per-plugin tables by default.

## Exists but disabled on the inspected connection

`wpinsight_plugin_track`, `wpinsight_plugin_untrack`, `wpinsight_keywords_manage`, `wpinsight_alert_rule_manage`, and `wpinsight_refresh` exist but are disabled because this MCP server is read-only. Do not call them missing product features. This read-only analysis skill does not need them; user-authorized changes should use a separately approved supported workflow.

## Not exposed by these customer tools

- Vulnerability advisories, CVEs, affected/fixed version ranges, security severity, exploit evidence, or installed-site versions
- Revenue, MRR, sales, churn, refunds, trials, conversion, acquisition attribution, or license/customer records
- Exact active-install growth, Google rankings, search volumes, impressions, clicks, or traffic
- Full release/changelog history; individual support tickets and reply-time analytics
- A scheduler, durable deduplication store, Slack/email sending, native Grok custom-MCP setup, OAuth setup parameters, or delivery receipts

`slackIntegration:true` in workspace features does not expose a Slack-send tool. Scheduling and sending require separately verified host/destination capabilities. OAuth discovery/registration details and Grok runtime compatibility remain integration acceptance work, not established by this schema audit.

## Beta.2 validation caveat

Date/report/review/milestone defects are under separate repair. Schema presence does not prove returned values are correct. Apply the [validation playbook](analysis-playbook.md) to each response; quarantine malformed custom reports and conflicting scope/date/unit values until runtime evidence supports them. No fixed deployment is assumed by this release.

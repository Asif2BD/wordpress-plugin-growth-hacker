# WordPress Plugin Growth Hacker Agent

**Free beta · 0.1.0-beta.3 · MIT**

A reusable instruction skill that helps a WordPress plugin team understand customer WPInsight signals and draft growth experiments. “Agent” is product branding: this package is not hosted software, a WordPress plugin, or an autonomous execution engine.

## Install and use

Download the versioned release ZIP, extract `wordpress-plugin-growth-hacker`, and install that folder using your assistant's supported skill loader. Alternatively load SKILL.md and its linked references in a session that supports instruction files. Consult your host documentation; no universal installer is supplied. Retain references when importing: the catalog's embedded SKILL.md is only the core.

Connect your own customer WPInsight account through your host's secure MCP setup. Import does not grant access or inherit connections. Choose your primary plugin and competitors, period and timezone, then ask: “Analyze my selected plugins over the past seven days and propose three evidence-backed experiments.” Outputs stay in the current conversation by default. Daily briefs are capped at 350 words; explicitly request deep analysis for up to 700 words. Expect a scorecard, one evidence-backed dated chart (or an honest table/unavailable fallback), supported competitor comparisons and at most three specific experiments.

Includes rank/history, keyword history, review/change events, downloads, coarse install milestones, support-resolution aggregates, alerts and notifications. No vulnerability, installed-site, revenue or conversion feed. Five customer write tools remain disabled and unused. No private Admin MCP is permitted.

The package is free under MIT. Host subscriptions and WPInsight access may have separate terms; this release grants no Pro entitlement. Optional delivery/scheduling requires customer authorization and separately tested host services.

See [setup/privacy](references/setup-privacy.md), [capability limits](references/capabilities.md), [fictional example](references/daily-example.md), [compatibility](COMPATIBILITY.md), and [test evidence](TESTING.md).

For an existing Grok setup, follow the [update and runtime retest instructions](references/grok-update.md).

## Development

Python 3.9+ standard library only: `python3 -m unittest discover -s tests -v`.
Tests include a small, offline reference policy model. It is a specification test harness, not an MCP integration or a runtime enforcement layer. A language model may fail to follow instructions; live acceptance testing is still required per host.

No verified badge, reviewer score, or Grok compatibility is claimed. ProSkills review/publication is a separate process.

# Project profile — [name]

**Shared standard:** unified-development-standard (pinned commit/tag); source/sync date: ...

Use when the project needs a persistent applicability profile. Update the existing profile, omit irrelevant fields, and do not create empty companion documents.

| Field | Decision |
|---|---|
| Risk profile | Minimal / Standard / Critical |
| Stack / supported stable version / support EOL | ... |
| Architecture | Modular monolith / other; ADR if needed |
| Domain/module owners | ... |
| Frontend / supported themes / design tokens | ... |
| API / contract source | ... |
| Database / migration runner | ... |
| Security baseline / threat model | ... |
| Locale / SEO / accessibility target | ... |
| Test commands / required CI checks | ... |
| Git ruleset / merge policy | ... |
| Registry / artifact identity policy | ... |
| Deployment controller and ownership / ingress | ... |
| Environment / secrets / staging | ... |
| Monitoring / alerts / logs | ... |
| Backup location / RPO / RTO / restore drill | ... |
| Performance budget / p95 / CWV | ... |
| Operations owner / incident channel | ... |

## Applicability
Give a reason for N/A. Link evidence for applicable MUST rules when assessing compliance (CI check, test, configuration, runbook). A file inventory alone does not establish compliance.

## Exceptions
`Rule ID | reason | decision record | compensating measure | expiry`

## Web, mobile, SEO, and upgrades
| Question | Decision |
|---|---|
| Site class | Public searchable / authenticated dashboard / Mini App / PWA / native |
| Browser support / target devices / OS | ... |
| Route/render strategy / URL policy | ... |
| Indexable/private routes / locale mapping | ... / N/A with reason |
| Mobile release/store/deep link/offline constraints | ... / N/A |
| Supported stable runtime/framework matrix / source/date | ... |
| Upgrade cadence / EOL review owner | ... |
| Performance baseline / field or lab source / target budget | ... |
| Measurement / events / owner / environments | ... / N/A |
| Analytics and advertising integrations / status / data | ... / undecided / N/A |
| Consent categories / applicable markets / verification | ... / N/A with reason |

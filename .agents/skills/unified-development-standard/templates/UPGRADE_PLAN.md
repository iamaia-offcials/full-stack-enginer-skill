# Upgrade and compatibility plan — [project, date]

Use for an upgrade needing coordination; omit irrelevant steps.

## Inventory
| System/dependency | Current version | Official supported stable target | EOL/CVE | Compatibility risk | Source/date |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

## Breaking changes and migration
API/configuration/database/SDK/native-client/build-image changes; required sequence; deprecation window.

## Execution plan
1. Scoped PR; synchronize manifests, lockfiles, and applicable build images.
2. Clean install and relevant lint/typecheck/tests/build/staging checks with exact commands.
3. Compatibility checks for affected mobile clients, API consumers, or database migrations.
4. Release/rollback; feature flags, expand-contract, or backups where relevant.
5. Verify release observations and remove deprecated code after the safe window.

## Verification log
`command | environment | PASS/FAIL/NOT_RUN | evidence`

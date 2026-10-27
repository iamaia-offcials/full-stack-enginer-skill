# 24. Data and analytics governance

- `[GDATA-001] MUST` Classify data (public/internal/confidential/personal/secret) and record its owner, purpose, sources, and access.
- `[GDATA-002] MUST` Define the purpose, retention, and applicable consent/legal basis for each external event or analytics stream. Do not send secrets or personal data in event properties without a valid basis.
- `[GDATA-003] SHOULD` Use consistent product-analytics event names and schemas; avoid competing definitions of metrics such as `conversion`.
- `[GDATA-004] MUST` Make data migrations/backfills logged and safe to rerun. Verify retention/erasure across databases, objects, caches, and backups under applicable law.
- `[GDATA-005] MUST` Where audit integrity is critical, protect administrative-action logs from arbitrary application changes. Audit logs must not become unlimited personal-data stores.
- `[GDATA-006] SHOULD` Track database, egress, registry, backup, log, and third-party API costs; alert on abnormal spending.

## Project data map
`entity/event | owner | source | recipient | legal basis | access | retention | delete/export | backup policy`.

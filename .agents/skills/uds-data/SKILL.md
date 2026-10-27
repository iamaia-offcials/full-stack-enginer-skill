---
name: uds-data
description: "Use when designing or changing database models, schemas, migrations, indexes, transactions, retention, or data recovery."
---
# Data, databases, and migrations

## Inputs
Existing schema, real queries, data lifecycle/volume, and compatibility requirements.

## Procedure
1. Identify record owners, unique keys, and business invariants requiring database enforcement.
2. Inspect tables, migrations, indexes, and representative query plans; avoid unnecessary data duplication.
3. Design migrations for concurrently running application versions, locking, and rollback/compensation.
4. Separate schema migrations from data backfills; batch large datasets where needed.
5. Define transaction boundaries and conflict-retry policy, accounting for races and duplicate writes.
6. Address retention, personal data, backup/restore, and safe export/logging.
7. Run relevant migration and query-validation checks; distinguish proposed plans from executed verification.

## Output and verification
Provide schema/mapping changes, migration/backfill/rollback strategy, indexes/invariants, and relevant test evidence. Production destructive schema changes require an established compatibility/recovery plan and appropriate authorization.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 06-DATA-DATABASE, 24-DATA-GOVERNANCE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.


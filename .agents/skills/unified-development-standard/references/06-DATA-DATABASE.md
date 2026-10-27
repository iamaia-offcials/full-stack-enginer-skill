# 06. Databases, migrations, integrity, and data lifecycle

- `[DATA-001] MUST` Change a managed database schema through versioned migrations in the repository, verified against test data. Run verification in the pipeline or an appropriate local workflow according to CI-001.
- `[DATA-002] MUST` Enforce actual invariants with database constraints (`UNIQUE`, `FK`, `NOT NULL`, `CHECK`) where supported. Application validation does not replace database constraints.
- `[DATA-003] MUST` Use a transaction for related changes that must be atomic. Resolve races through conditional updates, versioning, locks, or constraints according to the consistency model.
- `[DATA-004] MUST` Use `expand → backfill → switch → contract` for risky migrations. Check blocking and old-runtime compatibility with the schema throughout the rollback window.
- `[DATA-005] MUST` Choose indexes for measured queries; check N+1 behavior, execution plans, pagination, transaction sizes, and long-running queries.
- `[DATA-006] MUST` Assign owners to tables and schemas. Another module cannot write directly into their area without a documented contract.
- `[DATA-007] MUST` Distinguish retention, deletion, archiving, backup retention, and final erasure. Verify privacy obligations separately.
- `[DATA-008] SHOULD` Store system instants in UTC. Preserve the business time zone (IANA ID) for local events when relevant; a local offset alone is not a time-zone source of truth.
- `[DATA-009] MUST` Persistent data and user files survive container replacement where containers are used. Keep backups outside the sole failure point and test restores on a schedule appropriate to the data and recovery requirements.
- `[DATA-010] SHOULD` Use soft deletion, Event Sourcing, EAV, or pervasive JSON fields only for a justified need.

## Migration checklist
- [ ] The application can roll back without reverting the database schema.
- [ ] Lock/size impact is assessed; new fields have a backfill plan.
- [ ] Snapshots/backups and a restore point are available where required by migration risk.
- [ ] A dedicated runner/lock prevents each replica from migrating concurrently.
- [ ] Data is verified before removing an old field.

For practical patterns, read the relevant section of [decision formulas](../guides/PRACTICAL-FORMULAS.md).

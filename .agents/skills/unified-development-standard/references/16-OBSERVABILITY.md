# 16. Operations, observability, alerts, and recovery

Apply controls to services and data the project actually operates; use platform-appropriate health signals for static or managed hosting.

- `[OPS-001] MUST` Production has an owner, liveness/readiness signals or endpoints, a definition of working service, and a list of critical business scenarios.
- `[OPS-002] MUST` Use structured logs with timestamp, level, operation, request/trace ID, and safe error code. Do not log passwords, tokens, or unnecessary personal data.
- `[OPS-003] SHOULD` Measure requests, errors, latency (p95), background jobs, disk/memory, and integrations. Alert on user-visible failure symptoms, not only a dead container.
- `[OPS-004] SHOULD` Share correlation context across multiple services or asynchronous queues. OpenTelemetry is a suitable vendor-neutral basis for traces/metrics/logs; it does not require a separate platform.
- `[OPS-005] MUST` Set RPO/RTO for service and data. For retained data, provide off-host backups with retention, encryption/access control, and scheduled restore tests.
- `[OPS-006] MUST` Maintain runbooks for applicable failures: deployment, database outage, leaked secrets, full disk, proxy/TLS failure, restore, image rollback, and DNS outage.
- `[OPS-007] MUST` Handle incidents through detection → harm reduction → recovery → timeline → systemic cause remediation → added control.
- `[OPS-008] MUST` Distinguish `application rollback`, `data restore`, and `failover` in recovery plans. Image rollback **does not reverse database changes**.
- `[OPS-009] SHOULD` Periodically review recovery, TTL/log retention, capacity trends, and alert fatigue, including seasonal needs.

## Risk limits
Database RPO=24h means **up to one day of potential data loss**; RTO=4h is a recovery-time target. The product owner sets these values; examples are not defaults.

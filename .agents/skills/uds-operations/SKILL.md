---
name: uds-operations
description: "Use when preparing or maintaining production monitoring, logging, alerts, backups, disaster recovery, or incident response."
---
# Operations and reliability

## Inputs
Services/dependencies, SLOs or tolerated failures, infrastructure, data policy, and incident history.

## Procedure
1. Inventory services, critical user paths, and actual failure points.
2. Define proportionate error, latency, saturation, and availability signals; assign alert ownership and control noise.
3. Use structured logs without secrets/unnecessary personal data, correlating events through request/job IDs.
4. Distinguish liveness/readiness and define platform-appropriate smoke/health checks and external-dependency failure detection.
5. For retained data, define retention, off-site backups, encryption, and restore testing on a copy.
6. Document diagnosis, mitigation, rollback/restore, incident communication, and postmortems.
7. Scale controls to the project; add a complex telemetry stack only for demonstrated needs.

## Output and verification
Provide the relevant runbook, SLI/SLO plan, backup/restore checks with evidence, alerting, and incident process. A backup's existence does not prove restore capability. Separate SLO targets from measured attainment.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 16-OBSERVABILITY, 20-MAINTENANCE, 22-RELEASE. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.


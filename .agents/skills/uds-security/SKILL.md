---
name: uds-security
description: "Use when reviewing application security or privacy, threat boundaries, authentication/authorization, secrets, personal data, dependencies, or high-risk features."
---
# Security and privacy

## Inputs
Architecture/data-flow diagram, data types, roles, integrations, code changes, and applicable regulatory requirements.

## Procedure
1. Bound the assessment and identify assets, trust boundaries, attacker capabilities, and worst-case impacts.
2. Check relevant authentication, object authorization, session protection, CSRF/CORS, SSRF, and input validation.
3. Assess secret management/rotation, logging/personal data, dependency/supply-chain risks, and CI access policy.
4. Check applicable abuse cases, rate limits, webhook signatures/replay protection, and idempotency.
5. Prioritize remediation by impact and likelihood; identify compensating controls.
6. Distinguish manual code review from executed security tests. A checklist does not confer certification.
7. Perform dangerous scans, external writes, or production changes only within the necessary authorization.

## Output and verification
Provide a scoped threat model, findings with severity/evidence, remediation plan, and verification status. Do not claim the system is secure without scoped evidence. Critical findings prevent an unqualified release-readiness claim.
## Core rules
Use the sibling [core workflow](../unified-development-standard/SKILL.md) once per context; reuse it if already read. Then read only relevant sections of: 07-SECURITY-PRIVACY, 24-DATA-GOVERNANCE, 25-DEPENDENCIES. Apply core 00-GOVERNANCE scope. Do not recursively rediscover profiles/core or load the full corpus for a local edit. If core is unavailable, report that limitation without claiming compliance with unread rules.


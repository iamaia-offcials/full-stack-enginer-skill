# Lightweight threat model — [system/version]

Use for relevant trust boundaries and risk; adapt to the actual system.

| Component/data | Actor/threat | Trust boundary | Abuse scenario | Impact | Control | Test | Owner |
|---|---|---|---|---|---|---|---|
| Authentication | Anonymous attacker | Public API → backend | Credential guessing/stuffing | ... | Rate limits/MFA | ... | ... |

## Data and lifecycle
Personal data/secret classification, storage, sharing, retention, export/erasure.

## Applicable security checks
- Resource-level authorization (BOLA/IDOR).
- Injection, SSRF, uploads, path traversal, and CSRF.
- Secret management, safe logging, and monitoring.
- Webhook authenticity, replay resistance, and idempotency.
- Dependencies, build provenance, and permissions.

Record evidence and unresolved risks; an unchecked checklist is not verification.

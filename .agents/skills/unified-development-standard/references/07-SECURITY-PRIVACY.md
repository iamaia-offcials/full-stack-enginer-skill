# 07. Security, privacy, and access control

**Reference baseline:** OWASP ASVS 5.0.0. Select the scope and assurance level before applying requirements; claim conformance only after verification. Also consult current OWASP Cheat Sheets, applicable law, and platform requirements. Verify support/current versions when using this baseline rather than treating a stored date as proof of currency.

- `[SEC-001] MUST` For Standard/Critical profiles, maintain a threat model covering assets, actors, entry points, trust boundaries, abuse cases, risks, and mitigations. Update it when architecture/integrations change.
- `[SEC-002] MUST` Separate authentication, sessions, and authorization. In every protected server scenario, check permission for **the action and the specific object** (IDOR/BOLA).
- `[SEC-003] MUST` Apply least privilege to databases, users, containers, CI, secrets, and cloud resources; require MFA for administrative systems. Do not share one superuser account across applications.
- `[SEC-004] MUST` Protect against injections and SSRF; validate paths/files and apply allowlists and input/upload limits. Use parameterized SQL and context-appropriate output encoding: input-format validation does not replace either control or authorization. Do not invent cryptographic primitives.
- `[SEC-005] MUST` Deliver secrets through secure channels, separated by environment. Exclude them from hardcoded values, build arguments, logs, and client bundles; rotate immediately after exposure.
- `[SEC-006] MUST` With cookie authentication, use Secure, appropriate HttpOnly and SameSite settings, and CSRF protection. CORS does **not** replace authorization or CSRF defenses.
- `[SEC-007] MUST` If passwords exist, use supported password-hashing algorithms with current parameters. Never log credentials.
- `[SEC-008] MUST` Classify personal data; minimize collection, access, and retention. Support deletion, export, and data-subject access where legally required.
- `[SEC-009] MUST` Rate-limit risky actions (login, recovery, messaging, expensive APIs). Log privilege changes and administrative operations without unnecessary personal data.
- `[SEC-010] MUST` Apply security gates appropriate to the system: secret scanning, dependency/container scanning with triage, negative authorization tests, security headers, and TLS. Follow CI-001 for execution frequency; assign an owner to each vulnerability risk.
- `[SEC-011] SHOULD` For critical integrations, use separate credentials, expiration/rotation, scoped tokens, and access auditing.
- `[SEC-012] MUST` Maintain a security incident procedure: containment → key revocation → impact assessment → recovery → legally required communications → postmortem.

## Privacy by design
- Map data: purpose, storage, recipients, retention period, and processing basis.
- Determine GDPR/KVKK/other legal requirements **for the actual market and organizational role**. A generic checklist is not a legal opinion.
- Sanitize logs. Do not place user data in test environments without an authorized de-identification process.

For practical patterns, read the relevant section of [decision formulas](../guides/PRACTICAL-FORMULAS.md).

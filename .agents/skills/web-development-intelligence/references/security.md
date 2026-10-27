# Frontend & Web Application Security

Harden client and server boundaries against common web vulnerabilities.

## Critical Security Invariants

1. **Secrets Management:**
   - Never expose API secret keys, database credentials, or private tokens in client-side code, HTML bundles, or public repositories.
   - Distinguish public identifiers (e.g. Stripe publishable key, Firebase client config) from privileged secrets.

2. **Cross-Site Scripting (XSS) Prevention:**
   - Never use `dangerouslySetInnerHTML` with unsanitized user content.
   - Sanitize rich text inputs using an audited library (DOMPurify).
   - Configure a strict Content Security Policy (CSP).

3. **Authentication & Session Security:**
   - Store sensitive authentication tokens in `HttpOnly`, `Secure`, `SameSite=Strict` (or `Lax`) cookies to prevent JavaScript exfiltration.
   - Protect state-altering endpoints against CSRF.

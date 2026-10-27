# Backend Operations, Contracts & Invariants

Enforce authoritative business logic, access control, and transaction integrity.

## Server-Side Invariants

1. **Trusted Authority Principle:**
   - The server is the sole trusted authority. Never trust prices, permissions, role flags, or calculations sent from the client browser.
   - Client-side validation improves UX; server-side validation guarantees security and data integrity.

2. **Idempotency & Concurrency:**
   - Guard financial transactions, orders, and critical state mutations with unique idempotency keys to prevent duplicate operations on network retries.
   - Use atomic database transactions for multi-record operations.

3. **API Contract Design:**
   - Adopt standard error problem details (RFC 9457) with machine-readable `type`, human-readable `title`, and contextual `invalidParams`.
   - Paginate collections with cursor/keyset pagination for large datasets.

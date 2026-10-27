# Decision formulas

These formulas are reasoning aids, not mathematical guarantees. `→` means a decision sequence; `+` means complementary measures. Normative conditions live in the linked references; adapt examples to context.

## Safe input

**Formula:** trust boundary → field constraints → syntax and meaning → authorization → safe operation → safe output → negative checks. Format validation, authorization, SQL injection, and XSS are separate concerns.

**Email example:** use an associated label, `type=email`, `autocomplete=email`, and a text error. If data reaches a server, it independently checks type, length, and format using a maintained library. Do not arbitrarily ban characters or treat string cleanup as protection: valid addresses may contain `+` or an apostrophe. Normalization and comparison depend on the supported email system. Format does not establish mailbox ownership; when ownership matters, use verification with expiry, retry limits, and abuse protection.

Use SQL parameters for values; select dynamic column names or sorting from a fixed mapping. Escape HTML output for its context; do not insert untrusted HTML. Check valid and invalid addresses, oversized and non-string input, direct requests bypassing the UI, access to another user's record, injection strings, and retries appropriate to the operation. Do not log tokens or complete sensitive payloads. See [security rules](../references/07-SECURITY-PRIVACY.md).

## UX and styles

**Formula:** user task → hierarchy → clear action → states and feedback → accessibility/responsiveness → real verification.

**Example:** a save button reuses the existing component and tokens; the screen owns its layout. Loading/error states and duplicate-submission protection depend on the flow. A label change does not justify a new theme or complex state machine. Keep shared semantics with their owner and local exceptions near the feature. See [styles](../references/09-DESIGN-SYSTEM.md) and [accessibility](../references/10-ACCESSIBILITY.md).

## Server rules

**Formula:** contract → identity and authorization → business invariants → atomic change → response and audit. The order of individual checks depends on threats and the contract.

**Order example:** the server receives product and quantity, loads the authoritative price, checks permissions and availability, and commits the result atomically. Client calculations are previews. Check foreign objects, price tampering, concurrency, and retries; external operations need timeouts and safe retry policies. Do not invent a server for a client-only application. See [API](../references/05-API-INTEGRATIONS.md) and [architecture](../references/03-ARCHITECTURE.md).

## Data and queries

**Formula:** scenarios/lifecycle → invariants/model → constraints and transactions → queries → measurement/indexes → migration and recovery.

**Order-list example:** the server restricts results to the authorized owner; sorting is stable with a unique tie-breaker, and page size is bounded. Consider cursor/keyset pagination for large datasets when requirements justify it. Choose indexes for actual filters and sorting after examining query plans and representative data, including write cost. Do not index everything; an index does not replace authorization. See [database rules](../references/06-DATA-DATABASE.md).

## Changes and release

**Formula:** reviewable change → relevant checks → review → identifiable artifact → controlled release → smoke checks and recovery.

**CI cost example:** cancel superseded runs and cache dependencies. Run expensive checks according to risk, while verifying the commit being released. Minute/storage quotas and API rate limits differ. The canonical source for cadence and exceptions is [CI-001](../references/14-CI-CD.md). Use containers only when the operating model calls for them; keep build-only dependencies and secrets out of runtime images.

## Planning and stack

**Formula:** product vision → facts/hypotheses → detailed first release → future constraints → minimal foundation → stack options → validation and revision. This is not an hours-per-screen estimate. See [product planning](PRODUCT-AND-MVP-PLANNING.md) for the full sequence and future team/payment examples.

Primary technical references: [OWASP validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), [SQL prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html), [email](https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html). Other sources are in the [source catalog](../EXTERNAL_SOURCES.md); they support particular practices, not every custom rule in this suite.

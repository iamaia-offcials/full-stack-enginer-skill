# Content Design, UX Writing & Microcopy

Craft clear, concise, actionable copy that guides users through workflows without ambiguity.

## Principles of Interface Copy

1. **Clarity Over Cleverness:**
   - Button labels must state the action explicitly: **"Create account"**, **"Download report (PDF)"**, **"Upgrade to Pro"**. Avoid vague labels like **"Submit"**, **"Go"**, or **"Continue"**.
   - Speak in the user's vocabulary, not internal system terms (e.g. "Payment processed", not "Status code 200 OK").

2. **Error Message Craftsmanship:**
   A production-ready error message must have three components:
   1. **What happened:** Clear, non-technical explanation without blame ("We couldn't connect to your bank").
   2. **Why it happened:** Simple context ("The bank's server took too long to reply").
   3. **How to fix it:** Concrete next action ("Please try again in a few minutes or choose another payment method").
   *Never leak raw database schemas or stack traces to public interfaces.*

3. **Empty States & Onboarding Copy:**
   - Welcome users with constructive prompts: "No projects yet. Create your first project to start tracking tasks."
   - Pair with an immediate primary creation button.

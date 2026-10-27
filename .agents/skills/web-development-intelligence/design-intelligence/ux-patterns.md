# UX Patterns & Decision Workflows

Patterns designed around specific user intent and behavioral psychology.

## Core Interaction Patterns

1. **Lead Generation vs Direct Catalog:**
   - **Lead-Gen Flow:** Problem statement → Value proposition → Proof of authority → Step-by-step qualification form (3–4 fields max) → Instant confirmation.
   - **Catalog / Browse Flow:** Clear search bar → Multi-faceted filters → Scannable card grid with price/availability badges → Detailed single-item modal or route.

2. **Multi-Step Progressive Disclosure Forms:**
   - Break multi-input processes (mortgage quotes, event booking, custom tailoring) into 3–4 bite-sized logical steps.
   - Display a persistent step progress bar.
   - Allow users to freely step backward without wiping already-entered data.
   - Save drafts locally (`localStorage`) to guard against accidental browser refresh.

3. **Faceted Filter & Search UX:**
   - Instant optimistic filtering (results update without full page reload).
   - Display active filter pills with individual remove buttons and a single "Clear all" action.
   - Show item counts next to filter options (e.g. `Hotels (14)`). Disable zero-count options.

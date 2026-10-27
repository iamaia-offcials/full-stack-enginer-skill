# Workflow: Component Development & Token Binding

Craft standalone, accessible, reusable UI components.

## Procedure

1. **API & Prop Interface Design:**
   - Explicit variants (`variant="primary" | "secondary" | "danger"`) and sizes (`size="sm" | "md" | "lg"`).
   - Avoid dozens of independent boolean flags.
2. **Six-State Coverage:**
   - Implement `default`, `hover`, `focus-visible`, `active`, `disabled`, and `loading`.
3. **Accessibility Contract:**
   - Semantic HTML elements (`<button>`, `<dialog>`, `<nav>`).
   - High-contrast `:focus-visible` ring.
   - ARIA attributes where native elements are insufficient.

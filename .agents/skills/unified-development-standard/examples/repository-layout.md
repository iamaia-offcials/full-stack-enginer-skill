# Example application repository layout

```text
README.md
AGENTS.md
PROJECT_PROFILE.md
.env.example
.github/
  workflows/ci.yml
  pull_request_template.md
docs/
  PRODUCT.md
  ARCHITECTURE.md
  API.md
  OPERATIONS.md
  adr/
src/
  app/
  modules/
    users/
    catalog/
  shared/
tests/
Dockerfile
compose.yaml
```

- Create only needed modules and documents; do not generate empty folders or a complete document bundle.
- Place migrations in the chosen tool's conventional location, which may be outside `src`.
- Next.js App Router `app/` can contain route handlers and server components; domain/use cases may live in `src/modules`. This is an example, not a required architecture.
- Omit database, background-job, and container/Compose infrastructure when the application does not need it.
- Install the shared skill in a directory supported by the agent. A skill inside a ZIP is not automatically installed in an IDE.
- Existing repository conventions and canonical documentation take precedence over this layout.

# Frontend Architecture & Engineering

Build robust, high-performance web applications using modern component paradigms.

## Component Architecture Principles

1. **Component Hierarchy:**
   `Route / Page → Layout + Feature Container → Shared UI Primitives`.
   Feature containers manage state and business logic; `components/ui/` primitives remain strictly presentation-bound and decoupled from business models.

2. **Client vs Server Boundaries:**
   - Default to Server Components (in Next.js / modern SSR) for data fetching, static rendering, and SEO metadata.
   - Add `'use client'` only at the leaves of the component tree where interactivity (event listeners, hooks, state) is strictly required.

3. **State Management Discipline:**
   - **URL as Source of Truth:** Filters, tabs, search queries, pagination, and view modes belong in URL search parameters to support bookmarking, back/forward navigation, and sharing.
   - **Server Cache vs Client State:** Use dedicated query tools (TanStack Query, SWR, Server Actions) with caching and deduplication rather than raw ad-hoc `useEffect` fetches.

# Component & Animation Registry Configuration

Instructions for connecting, searching, and installing components across supported ecosystems.

## 1. Unified `components.json` Configuration

Add registry namespaces to your project's `components.json` file to enable seamless installation:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  },
  "registries": {
    "@shadcn": "https://ui.shadcn.com/registry/{name}.json",
    "@aceternity": "https://ui.aceternity.com/registry/{name}.json",
    "@magicui": "https://magicui.design/r/{name}.json",
    "@react-bits": "https://reactbits.dev/r/{name}.json",
    "@motion-primitives": "https://motion-primitives.com/c/{name}.json"
  }
}
```

## 2. Model Context Protocol (MCP) Integration

Configure MCP in your editor (`.mcp.json` or `.gemini/config/mcp_config.json`):

```json
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["-y", "shadcn@latest", "mcp"]
    },
    "magicui": {
      "command": "npx",
      "args": ["-y", "@magicuidesign/mcp@latest"]
    }
  }
}
```

## 3. CLI Installation Commands

```bash
# Core shadcn components
npx shadcn@latest add button card dialog dropdown-menu form input table

# Aceternity UI
npx shadcn@latest add https://ui.aceternity.com/registry/sticky-scroll-reveal.json
npx shadcn@latest add https://ui.aceternity.com/registry/3d-card.json

# Magic UI
npx shadcn@latest add https://magicui.design/r/marquee.json
npx shadcn@latest add https://magicui.design/r/blur-fade.json

# React Bits
npx shadcn@latest add @react-bits/BlurText-TS-TW
npx shadcn@latest add @react-bits/Aurora-TS-TW

# Motion Primitives
npx shadcn@latest add https://motion-primitives.com/c/text-effect.json

# GSAP Animation Suite (all plugins free)
npm install gsap @gsap/react

# Motion (Framer Motion)
npm install motion clsx tailwind-merge lucide-react
```

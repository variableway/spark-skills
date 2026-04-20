# Frontend & Desktop Skill Analysis Report

> Date: 2026-04-11
> Scope: Consolidation analysis of `innate-frontend` and `tauri-desktop-app` skills, with competitive landscape research

---

## 1. Executive Summary

**Recommendation: Keep as two separate skills, but extract a shared `ui-foundation` skill.**

The two skills serve different purposes — one for web, one for desktop — and have meaningful architectural differences (static export, IPC, Rust backend, CSP). However, they share ~80% of their UI layer. The best approach is:

1. **Extract common parts** into a new `ui-foundation` skill (component library, theme system, monorepo structure)
2. **Slim down** `innate-frontend` to focus on web-specific concerns (SSR, SEO, routing, deployment)
3. **Slim down** `tauri-desktop-app` to focus on desktop-specific concerns (IPC, sidecar, shell plugin, native menus)
4. Both skills reference `ui-foundation` as a dependency

This gives you the best of both worlds: DRY component knowledge, but clean separation of platform concerns.

---

## 2. Current Skills Comparison

### 2.1 Overlap Analysis

| Aspect | innate-frontend | tauri-desktop-app | Overlap |
|--------|----------------|-------------------|---------|
| **UI Components** | 57 + business blocks (via `@innate/ui`) | 56+ shadcn/ui components | ~90% — same Radix-based component set |
| **Theme System** | OKLCH color space, CSS variables | CSS variables, dark/light | ~80% — innate-frontend has richer OKLCH system |
| **Tech Stack** | Next.js 16, React 19, TS 6, Tailwind v4 | Next.js 16, React 19, TS 5+, Tailwind v4 | ~95% — nearly identical frontend stack |
| **Monorepo** | pnpm workspace, `apps/web` + `packages/` | pnpm workspace, `apps/desktop` + `packages/` | ~85% — same pattern, different app target |
| **Styling** | Tailwind CSS v4 + cn() | Tailwind CSS v4 + cn() | 100% |
| **Component Patterns** | CVA variants, data-slot, "use client" | shadcn/ui conventions | ~90% |

### 2.2 Unique to `innate-frontend`

- **57 @innate/ui components** with a unified component library brand
- **7 Landing blocks**: HeroSection, FeaturesSection, PricingSection, etc.
- **Business blocks**: Auth (LoginForm), Mail (Inbox/MailList/MailDisplay), Chat (ChatInterface/MessageList)
- **OKLCH theme system** with full design token documentation
- **Page patterns**: Landing page, Dashboard, Form patterns
- **TypeScript 6** target
- **References**: component-catalog.md, theme-system.md

### 2.3 Unique to `tauri-desktop-app`

- **Tauri 2.x integration**: Rust backend, IPC commands, capabilities/permissions
- **Desktop layout**: AppShell, AppSidebar (collapsible), StatusBar (platform detection)
- **Template files**: Full scaffolding templates for project bootstrapping
- **Platform detection**: macOS/Windows/Linux icon logic
- **Tauri IPC pattern**: Safe `callTauri<T>()` wrapper with web fallback
- **Static export**: `output: 'export'` requirement for Next.js
- **CSP security** guidance
- **Golang sidecar** support (mentioned in task requirements but not yet in skill)

### 2.4 Gap Analysis

| Gap | Description |
|-----|-------------|
| **No shared UI foundation** | Both skills independently define the same component catalog and styling patterns |
| **Golang sidecar** | Task requirement mentions Golang sidecar but neither skill documents this pattern |
| **Tauri shell plugin** | Task requirement mentions CLI via Tauri shell plugin but skill doesn't cover this |
| **TypeScript version mismatch** | innate-frontend says TS 6, tauri says TS 5+ |
| **No testing patterns** | Neither skill covers testing strategies |
| **No CI/CD** | Neither skill covers build/deploy pipelines |

---

## 3. Popular Frontend Skills — Competitive Analysis

### 3.1 Top Community Skills

| Skill | Source | Tech Stack | Key Strengths | Relevance |
|-------|--------|------------|---------------|-----------|
| **Vercel React Best Practices** | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | React, Next.js | 58-69 specific performance checks, server components, data fetching patterns. 20K+ installs. Official Vercel skill. | HIGH — Direct Next.js improvements |
| **Anthropic frontend-design** | [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) | General web, React | Conceptual guidance for distinctive UIs, aesthetic principles, anti-patterns. Official Anthropic skill. | MEDIUM — Design philosophy |
| **shadcn/ui Official Skills** | [ui.shadcn.com/docs/skills](https://ui.shadcn.com/docs/skills) | shadcn/ui, Radix, Tailwind | Deep component knowledge, project-aware context. Users report "no more random Tailwind soup." | HIGH — Direct component library overlap |
| **Shadcnblocks Skill** | [github.com/masonjames/Shadcnblocks-Skill](https://github.com/masonjames/Shadcnblocks-Skill) | shadcn/ui, Tailwind | 1,338 blocks + 1,189 components. Massive block library. | MEDIUM — Block approach similar to innate |
| **tailwind-v4-shadcn** | [agentskills.so](https://agentskills.so/skills/secondsky-claude-skills-tailwind-v4-shadcn) | Tailwind v4, shadcn/ui | Production-tested Tailwind v4 + shadcn setup | HIGH — Exact same stack |
| **senior-frontend** | [github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | React, Next.js, TS, Tailwind | Part of 220+ skill collection | LOW — Generic |
| **Core Web Vitals** | [snyk.io](https://snyk.io/articles/top-claude-skills-developers/) | General web | LCP/INP/CLS optimization checklists, performance profiling | MEDIUM — Performance guidance |

### 3.2 innat-frontend vs Community — Pros & Cons

**Pros of current innate-frontend skill:**
- Custom `@innate/ui` brand with 57 components + business blocks — this is a unique differentiator
- OKLCH theme system with full documentation — more advanced than most community skills
- Landing page blocks (Hero, Features, Pricing, etc.) — most community skills don't offer this
- Monorepo-aware structure — matches real project setup
- Multi-agent support (Claude Code, Kimi, Codex, OpenCode)

**Cons vs community best practices:**
- No performance optimization guidance (Vercel skill has 58+ specific checks)
- No accessibility (a11y) guidelines beyond what Radix provides
- No testing patterns (unit, integration, E2E)
- No SEO/SSR best practices for Next.js
- No animation/transition patterns
- Component catalog is a flat list — no composition patterns or "how to combine components" guidance
- No error boundary or error handling patterns
- No data fetching patterns (SWR, React Query, Server Actions)

---

## 4. Popular Desktop Application Skills — Competitive Analysis

### 4.1 Top Community Skills

| Skill | Source | Tech Stack | Key Strengths | Relevance |
|-------|--------|------------|---------------|-----------|
| **dchuk/claude-code-tauri-skills** (13 skills) | [agentskills.so](https://agentskills.so/skills/dchuk-claude-code-tauri-skills-understanding-tauri-architecture) | Tauri v2, Rust | Most comprehensive: architecture, IPC, process model, permissions, plugins, CI/CD, packaging, testing, security, binary optimization. 13 modular skills covering full lifecycle. | VERY HIGH — Direct competitor |
| **tauri-desktop (travisjneuman)** | [lobehub.com](https://lobehub.com/skills/travisjneuman-.claude-tauri-desktop) / [GitHub](https://github.com/travisjneuman/.claude) | Tauri 2.0, Rust | Part of 119-skill "Ultimate Toolkit" with dynamic context routing. Plugin system, auto-update, mobile support. | HIGH — Comprehensive alternative |
| **Electron FSD + React 19** | [nothans.com](https://nothans.com/claude-code-and-agent-skills-for-electron-app-development-your-desktop-app-just-got-a-cheat-code) | Electron, React 19 | Feature-Sliced Design architecture, clean project structure enforcement | MEDIUM — Architecture patterns |
| **Desktop App Architect** | [mcpmarket.com](https://mcpmarket.com/tools/skills/desktop-app-architect) | Electron, Tauri, Rust | Cross-platform with IPC patterns, covers both frameworks | MEDIUM — Dual framework |
| **Visual Feedback Loop for Electron** | [juri.dev](https://juri.dev/articles/visual-feedback-loop-electron-apps-claude-code/) | Electron, CDP | Chrome DevTools Protocol for live screenshots, DOM inspection, iterative visual development | LOW — Electron specific |

### 4.2 Cursor Rules for Tauri (Adaptable)

| Rule | Source | Key Patterns |
|------|--------|-------------|
| **Tauri Cursor Rules** | [cursor.directory](https://cursor.directory/tauri--cursor-rules) | TypeScript + Rust, clear readable code, cross-platform desktop |
| **Tauri Svelte TypeScript Guide** | [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | Strong typing, native integration (file system, system tray), Tauri API usage |

### 4.3 tauri-desktop-app vs Community — Pros & Cons

**Pros of current tauri-desktop-app skill:**
- Complete monorepo template with scaffolding files — most skills only provide instructions, not actual templates
- AppShell + Sidebar + StatusBar desktop layout — practical desktop UX
- Safe IPC wrapper with web fallback (`callTauri<T>()`) — elegant degradation
- Platform detection logic — small but useful detail
- Integrated with @innate/ui component library

**Cons vs community best practices:**
- **No Tauri plugin guidance** — dchuk's skills cover plugin development, permissions (ACL), and the plugin ecosystem in detail
- **No CI/CD pipeline** — dchuk includes GitHub Actions with `tauri-apps/tauri-action` for multi-platform builds
- **No packaging/distribution** — no AppImage/Debian/macOS DMG guidance
- **No security hardening** — dchuk has dedicated skills for security auditing, runtime authority, CSP
- **No testing** — dchuk covers unit mocks, WebDriver E2E, CI integration
- **No binary optimization** — dchuk covers Cargo profiles for minimal binary size
- **No Golang sidecar pattern** — this is a specific requirement not covered anywhere in community skills either
- **No Tauri shell plugin pattern** — also unique to your requirements
- **No auto-update configuration** — travisjneuman's skill covers this
- **No mobile support mention** — Tauri 2 supports Android/iOS, not covered

---

## 5. Consolidation vs Separation — Honest Analysis

### 5.1 Option A: Single Unified Skill

**How it would work:** One skill called `innate-app` that handles both web and desktop via configuration/modes.

**Pros:**
- Single source of truth for components and patterns
- No duplication to maintain
- Simpler for users — one skill to install

**Cons:**
- **Bloated context** — desktop developers don't need SSR/SEO guidance; web developers don't need IPC/Rust patterns. Claude's context window is precious.
- **Confusing triggers** — "create an app" becomes ambiguous
- **Harder to maintain** — changes to one concern risk breaking the other
- **Poor separation of concerns** — mixing web routing with Tauri IPC is architecturally messy
- **Community skills trend toward specialization** — dchuk split Tauri into 13 focused skills; Vercel has one skill just for React performance

**Verdict: Not recommended.** The context bloat alone makes this problematic. AI agents perform better with focused, clear instructions.

### 5.2 Option B: Two Separate Skills (Current Approach, Improved)

**How it would work:** Keep `innate-frontend` and `tauri-desktop-app` as separate skills, but extract shared UI knowledge into a dependency.

**Pros:**
- **Clean separation** — each skill has a clear, focused purpose
- **Context efficiency** — agents load only what they need
- **Easier maintenance** — changes to web patterns don't affect desktop and vice versa
- **Better triggers** — "create web app" vs "create desktop app" is unambiguous
- **Industry aligned** — matches how community skills are structured

**Cons:**
- **Some duplication** — both skills reference the same component library
- **Version drift risk** — component library descriptions could diverge
- **Three things to maintain** instead of two (with the shared skill)

**Verdict: Recommended.** This is the right balance of DRY and focused context.

### 5.3 Option C: Three Skills (Recommended)

**How it would work:**

```
ui-foundation          → Shared: components, theme, patterns, monorepo structure
├── innate-frontend    → Web-specific: SSR, SEO, deployment, page patterns
└── tauri-desktop-app  → Desktop-specific: IPC, sidecar, shell, native features
```

**Pros:**
- Maximum DRY — component catalog lives in one place
- Maximum focus — each skill is lean and targeted
- Future-proof — if you add mobile (Tauri 2 supports it), you add a 4th skill that depends on `ui-foundation`
- Easier to update component docs — change once, all skills benefit

**Cons:**
- More files to manage
- Need to ensure agents load `ui-foundation` when using either app skill
- Slightly more complex documentation

**Verdict: Best option.** The three-skill architecture scales better and keeps each skill focused.

---

## 6. Improvement Recommendations

### 6.1 New `ui-foundation` Skill (Shared)

Extract from both skills:
- Component catalog (57 components + business blocks)
- OKLCH theme system
- CVA variant patterns
- `cn()` utility pattern
- Monorepo structure (`packages/ui`, `packages/utils`, `packages/tsconfig`)
- Component writing conventions (data-slot, "use client", type exports)
- Form patterns (React Hook Form + Zod)

### 6.2 `innate-frontend` Improvements

| Priority | Improvement | Inspired By |
|----------|-------------|-------------|
| HIGH | Add performance checks (server components, re-renders, bundle analysis) | Vercel React Best Practices |
| HIGH | Add data fetching patterns (Server Actions, SWR, React Query) | Community best practices |
| MEDIUM | Add accessibility (a11y) guidelines | shadcn/ui official docs |
| MEDIUM | Add SEO patterns for Next.js App Router | Community skills |
| MEDIUM | Add testing patterns (Vitest, Playwright) | Community best practices |
| LOW | Add animation/transition patterns | Community skills |
| LOW | Add error boundary patterns | Community best practices |

### 6.3 `tauri-desktop-app` Improvements

| Priority | Improvement | Inspired By |
|----------|-------------|-------------|
| HIGH | Add Golang sidecar pattern | Your requirement (unique, not in community) |
| HIGH | Add Tauri shell plugin pattern | Your requirement (unique, not in community) |
| HIGH | Add Tauri permissions/ACL documentation | dchuk/claude-code-tauri-skills |
| HIGH | Add CI/CD pipeline (GitHub Actions) | dchuk/claude-code-tauri-skills |
| MEDIUM | Add packaging/distribution guide (DMG, AppImage, MSI) | dchuk skills |
| MEDIUM | Add security hardening (CSP, code signing) | dchuk/claude-code-tauri-skills |
| MEDIUM | Add auto-update configuration | travisjneuman/tauri-desktop |
| MEDIUM | Add testing patterns (unit, E2E with WebDriver) | dchuk/tauri-testing |
| LOW | Add binary optimization guide | dchuk/optimizing-tauri-binary-size |
| LOW | Add mobile support mention (Tauri 2) | Community skills |
| LOW | Add system tray patterns | Cursor rules for Tauri |

---

## 7. Tasks — What To Do Next

### Phase 1: Foundation (Priority: HIGH)

- [ ] **T1: Create `ui-foundation` skill** — Extract shared component catalog, theme system, monorepo structure, and component writing conventions from both existing skills into a new `ui-foundation/SKILL.md`
- [ ] **T2: Refactor `innate-frontend`** — Remove duplicated UI/component content, add reference to `ui-foundation`, add web-specific improvements (performance, data fetching, SEO, testing)
- [ ] **T3: Refactor `tauri-desktop-app`** — Remove duplicated UI/component content, add reference to `ui-foundation`, add desktop-specific improvements (permissions, CI/CD, packaging)

### Phase 2: Feature Gaps (Priority: HIGH)

- [ ] **T4: Add Golang sidecar pattern** — Document how to configure a Go binary as Tauri sidecar, build process integration, IPC between Go app and Tauri frontend
- [ ] **T5: Add Tauri shell plugin pattern** — Document how to use `tauri-plugin-shell` to invoke CLI tools from the desktop app, security considerations, output handling
- [ ] **T6: Add Tauri permissions guide** — Document ACL system, capabilities configuration, permission scopes for shell/sidecar/filesystem

### Phase 3: Polish (Priority: MEDIUM)

- [ ] **T7: Add CI/CD templates** — GitHub Actions workflow for multi-platform Tauri builds (macOS, Windows, Linux)
- [ ] **T8: Add testing patterns** — Vitest for unit tests, Playwright/WebDriver for E2E, Tauri-specific test utilities
- [ ] **T9: Add packaging guide** — DMG for macOS, AppImage/Debian for Linux, MSI for Windows, code signing
- [ ] **T10: Add performance guide** — Server component best practices, bundle analysis, re-render prevention

### Phase 4: Future (Priority: LOW)

- [ ] **T11: Evaluate mobile support** — Tauri 2 supports Android/iOS; decide if this warrants a 4th skill
- [ ] **T12: Add auto-update configuration** — Tauri updater plugin setup, update manifest, signing
- [ ] **T13: Add binary optimization** — Cargo profile configuration, stripping, LTO settings

---

## 8. Key Sources

### Frontend Skills & Resources
- Vercel React Best Practices: [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- Anthropic frontend-design: [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
- shadcn/ui Skills: [ui.shadcn.com/docs/skills](https://ui.shadcn.com/docs/skills)
- Shadcnblocks Skill: [github.com/masonjames/Shadcnblocks-Skill](https://github.com/masonjames/Shadcnblocks-Skill)
- tailwind-v4-shadcn: [agentskills.so](https://agentskills.so/skills/secondsky-claude-skills-tailwind-v4-shadcn)
- Core Web Vitals: [snyk.io](https://snyk.io/articles/top-claude-skills-developers/)
- Next.js AI Apps Skills: [github.com/laguagu/claude-code-nextjs-skills](https://github.com/laguagu/claude-code-nextjs-skills)

### Desktop Skills & Resources
- dchuk Tauri Skills (13 modules): [agentskills.so](https://agentskills.so/skills/dchuk-claude-code-tauri-skills-understanding-tauri-architecture)
- travisjneuman Ultimate Toolkit: [github.com/travisjneuman/.claude](https://github.com/travisjneuman/.claude)
- Desktop App Architect: [mcpmarket.com](https://mcpmarket.com/tools/skills/desktop-app-architect)
- Electron FSD + React 19: [nothans.com](https://nothans.com/claude-code-and-agent-skills-for-electron-app-development-your-desktop-app-just-got-a-cheat-code)
- Tauri Cursor Rules: [cursor.directory](https://cursor.directory/tauri--cursor-rules)

### Skill Collections & Marketplaces
- AgentSkills.so: [agentskills.so](https://agentskills.so)
- MCP Market: [mcpmarket.com/tools/skills](https://mcpmarket.com/tools/skills)
- Smithery: [smithery.ai/skills](https://smithery.ai/skills)
- LobeHub: [lobehub.com/skills](https://lobehub.com/skills)
- VoltAgent awesome-agent-skills: [github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- awesome-cursorrules: [github.com/PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)

### Reference Projects
- innate-next-mono: [github.com/variableway/innate-next-mono](https://github.com/variableway/innate-next-mono)
- innate-executable: [github.com/variableway/innate-executable](https://github.com/variableway/innate-executable)

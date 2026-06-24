---
name: handoff
description: Compact the current session into a short transfer document another session (or agent) can pick up — purpose, key decisions, constraints, what's done, what's left, and pointers to artifacts. Use when a session is getting long, when crossing a context boundary, or when spinning off a side task, to preserve the smart zone of the context window.
---

# Handoff

When work crosses a boundary — long session, a restart, a side task, a different agent — don't carry the whole transcript. Carry a brief.

Write a markdown doc (target 500–2000 tokens) with:

- **Purpose** — what the next session is for, in two lines.
- **Decisions made** — the choices already settled and why (so they aren't re-litigated).
- **Constraints** — non-goals, things that must not change, conventions.
- **State** — what's done, what's in progress, what's next.
- **Pointers** — paths to the real artifacts (`.claude/loki-harness/plan/…`, `tasks/…`, `research/…`, CONTEXT.md). Reference them; don't paste them.
- **Suggested next skills/agents** — what the receiver should reach for.

Keep it pointers-over-payload: the goal is a clean, lightweight resume, not a copy of everything. Save it under `.claude/loki-harness/handoff/` and hand back the path.

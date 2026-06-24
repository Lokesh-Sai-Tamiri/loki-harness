---
name: caveman
description: Compress output and inter-agent handoffs to dense, fact-based prose — drop articles, hedging, pleasantries, restatements, and sign-offs. Use whenever an agent is writing a handoff summary, a status report, or final prose output, to cut token cost and keep the harness fast. Do NOT use during interview, planning, or adversarial reasoning, where the explanatory prose is the point. Never touches code blocks.
---

# Caveman

Strip the style, keep the content. LLMs reconstruct grammatical scaffolding for free, so you pay nothing to omit it.

Apply to **output and handoffs only** — not to the thinking stages (Interview, Planner, Adversary), where reasoning prose carries the value.

Rules:

- Drop articles (a/an/the), filler, hedging, and pleasantries.
- No problem restatement, no preamble, no "Here's…", no sign-off.
- Use arrows for causality (`stale cookie → 401 → retry`).
- One fact per line where it helps scanning.
- **Leave code, commands, identifiers, and quoted errors verbatim** — never compress those.

Goal is dense and lossless, not cryptic. If compression would drop a load-bearing fact, keep the fact.

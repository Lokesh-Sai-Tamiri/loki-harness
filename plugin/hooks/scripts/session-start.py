#!/usr/bin/env python3
"""Loki-Harness SessionStart: inject always-on discipline and reset the /go toggle.
Resetting the toggle each session means the user types /go once per session."""
import json, os

try:
    os.remove(".claude/loki-harness/active")
except OSError:
    pass

ctx = """## Loki-Harness — always-on engineering discipline

These four principles apply to you and to every sub-agent you spawn:

1. Think Before Coding — state assumptions, surface tradeoffs, ask when unclear. No silent guessing.
2. Simplicity First — minimum code that solves it; no speculative features or single-use abstractions.
3. Surgical Changes — touch only what the task needs; match existing style; no drive-by refactors; never silently delete adjacent code.
4. Goal-Driven Execution — define a verifiable success condition and loop until it is met (write the failing test first). Never finish on a self-reported confidence number.

Bias toward caution over speed. For trivial tasks, use judgment.

## Model tier rules (set the model parameter when spawning sub-agents)
- haiku  — mechanical / read-only: search, classification, file reads, status, context assembly.
- sonnet — standard implementation, planning, debugging, interview.
- opus   — architecture, deep multi-file reasoning, adversarial review, hard UI.

The full pipeline engages when the user runs /go. Until then, still honor the four principles."""

print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx}}))

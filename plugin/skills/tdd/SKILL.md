---
name: tdd
description: Test-driven discipline — write the failing test first, make it pass, then refactor. The operational form of Goal-Driven Execution. Use on every implementation task and whenever a change has a verifiable success condition, so "done" means "the test proves it," not "looks right."
---

# TDD

Turn the task's success criteria into tests, then make them pass. This is how the harness replaces self-reported confidence with evidence.

Loop, per task:

1. **Red** — write the smallest test that encodes the next success criterion. Run it. Confirm it fails *for the right reason* (feature missing, not typo).
2. **Green** — write the minimum code (see `ponytail`) to make it pass. Run the test.
3. **Refactor** — clean up with the test green; re-run. No behavior change.
4. Repeat for the next criterion.

Rules:

- One behavior per test. Name tests by behavior, not by method.
- Cover the corners the plan named: empty/error states, boundaries, idempotency, failure paths — not just the happy path.
- If there's no runnable test command for the repo, say so and fall back to an explicit manual verification step; don't pretend it's verified.
- A criterion that can't be expressed as a check is not a criterion — push it back to the Planner to sharpen.

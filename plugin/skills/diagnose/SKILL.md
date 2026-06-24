---
name: diagnose
description: A disciplined diagnosis loop for hard bugs and performance regressions — reproduce, minimise, hypothesise, instrument, fix, regression-test. Use whenever the request is "X is broken / slow / flaky / wrong," instead of guessing at a fix. Stops the flailing where an agent edits hopefully and re-runs.
---

# Diagnose

Bugs are solved by evidence, not by guessing. Run the loop; don't skip to step 5.

1. **Reproduce** — get a reliable, minimal repro. If you can't reproduce it, you can't fix it; gather the conditions until you can.
2. **Minimise** — strip the repro to the smallest input/path that still fails. Most of the bug disappears here.
3. **Hypothesise** — state a specific, falsifiable cause ("the `li_at` cookie is stale by the time the retry fires"), not a vibe.
4. **Instrument** — add logging/assertions to confirm or kill the hypothesis with data. If killed, return to step 3.
5. **Fix** — once the cause is proven, apply the minimum fix (see `ponytail`).
6. **Regression-test** — write a test that reproduces the original bug and now passes, so it can never silently return.

Never ship a fix whose cause you didn't confirm. "It seems to work now" without a proven cause means you changed the timing, not the bug.

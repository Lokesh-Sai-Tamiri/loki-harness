---
name: ponytail
description: The lazy-senior-dev necessity ladder. Before writing ANY code, walk six rungs and stop at the first that holds — the best code is the code you never wrote. Use this on every implementation task, every time, to avoid over-engineering and bloated abstractions. Always active for the Implementer.
---

# Ponytail

Think like the laziest senior dev in the room. Before writing any code, stop at the first rung that holds:

1. **Does this need to be built at all?** (YAGNI)
2. **Does the standard library already do this?** Use it.
3. **Does a native platform feature cover it?** Use it.
4. **Does an already-installed dependency solve it?** Use it.
5. **Can this be one line?** Make it one line.
6. **Only then:** write the minimum code that works.

"Only then" does not mean "don't write" — it means walk rungs 1–5 first.

## Never lazy about

The ladder minimizes *implementation*, never *safety*. Do not skip or shrink:

- input validation at trust boundaries,
- error handling that prevents data loss,
- security and authorization checks,
- accessibility,
- the calibration real hardware/edge cases need.

The code ends up small because it is necessary, not golfed.

> Note: on a model that spends heavy reasoning tokens deliberating the rungs, this can add cost rather than save it. The win is fewer/cleaner lines and fewer follow-ups — measure it on your model, not the headline numbers.

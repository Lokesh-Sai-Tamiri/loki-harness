---
name: backend-design
description: Backend craft — correctness, data integrity, and failure behavior for server, API, data, and queue code. Use whenever a task touches an endpoint, schema, migration, query, background job, or external integration, to enforce contracts, transactional safety, idempotency, resilience, and observability. Stack-neutral principles; stack-specific depth comes from project-local skills.
---

# Backend Design

Unlike UI, most backend craft is *verifiable* — so lean on tests and the test gate, not assertions.

Hold this bar on any server/API/data task:

- **API contracts** — consistent request/response shapes, explicit and correct status codes, versioning, pagination on lists, idempotency keys on writes that can be retried.
- **Data layer** — safe, reversible migrations; transactions wherever a multi-step write can half-fail; index before you query at scale; watch for N+1s.
- **Concurrency & idempotency** — assume retries and concurrent callers. Use locks/leases or idempotency keys so an operation can't double-apply. Name the race you're defending against.
- **Failure & resilience** — timeouts on every external call, retries with backoff, circuit-breaking, graceful degradation. Never swallow an error silently.
- **Async / queues** — be explicit about at-least-once vs exactly-once; handle dead-letter and poison messages; cap retries.
- **Security & validation** — validate input at trust boundaries, authorize every endpoint, parameterize queries, never log secrets (Ponytail never minimizes these away).
- **Observability** — structured logs with correlation IDs, metrics on the paths that matter, errors that surface instead of vanish.

Encode each of these as a test where you can (failure paths, idempotency, migration up/down) — a backend claim that isn't tested isn't done. For framework-specific patterns (a specific web framework, ORM, queue, or cloud SDK), use the project-local stack skill if one is configured.

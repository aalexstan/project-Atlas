# Commerce Operations API Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

## Preconditions

- Obtain written permission and authorized test credentials.
- Use synthetic or explicitly permitted seller/account data.
- Record API version, account plan, token scope, region and test timestamp.
- Do not test destructive operations against production data.

## Scenarios

1. Read product/catalog metadata.
2. Read and reconcile stock for one warehouse and multiple warehouses.
3. Read orders over a fixed time window with pagination.
4. Read postings, supplies and returns where supported.
5. Update a synthetic catalog or price only where the provider permits it.
6. Trigger or receive one permitted webhook and test duplicate delivery handling.
7. Repeat a request and record idempotency or duplicate behavior.
8. Send malformed input and record error, field path and retry guidance.
9. Run a bounded batch and record throughput, latency and partial-failure behavior.
10. Perform a full reconciliation and record missing, duplicated and changed entities.

## Metrics

Record p50/p95 latency, HTTP error rate, provider error rate, pagination completeness, webhook delay, duplicate rate, missing-result rate, reconciliation mismatch rate and recovery time. Results are measured only for the authorized test scope and must not be generalized to the whole product.

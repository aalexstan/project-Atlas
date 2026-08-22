# Payment API Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

Use only lawful synthetic or provider-approved test data. Do not use real card numbers, personal data, or production funds.

Test the same flows for every candidate:

- create payment and receive status;
- success, decline, timeout, duplicate request and retry;
- webhook delivery, signature/authentication, duplicate webhook and replay handling;
- full and partial refund;
- cancellation and two-stage confirmation where supported;
- receipt payload and fiscalization handoff;
- recurring-payment consent and cancellation where supported;
- payment link and mobile/redirect flow where relevant.

Record request timestamp, correlation/idempotency key, provider response code, final state, webhook latency, retry count, refund outcome and error classification. Report only measured results with test date and environment. No test results are claimed in this repository.

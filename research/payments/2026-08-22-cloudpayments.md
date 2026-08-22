# CloudPayments API Research Log

[Русская версия](2026-08-22-cloudpayments.ru.md)

## Scope

Review the official CloudPayments API as a route for online card and alternative payment acceptance, refunds, two-stage payments, subscriptions, receipts, and notifications.

## Official sources reviewed

- https://developers.cloudpayments.ru/
- https://cloudpayments.ru/info/documents
- https://cloudpayments.ru/help/payments
- https://cloudpayments.ru/help/payments/bills

## Confirmed facts

- CloudPayments documents an API at `https://api.cloudpayments.ru`.
- Official developer documentation describes one-stage and two-stage payments, refunds, payment cancellation, recurring subscriptions, invoices, and notifications.
- Authentication uses HTTP Basic Auth with a Public ID and API Secret obtained in the merchant account.
- Requests may use JSON or form encoding and responses are JSON.
- The official documentation describes a test method at `/test` and an idempotency/request identifier mechanism using `X-Request-ID`.
- Official product documentation separately describes online acquiring, payment widgets, mobile SDKs, receipts, and API payouts.

## Provider-reported claims

- CloudPayments states that its checkout approach helps keep card data away from the merchant server and references PCI DSS protection on its side.
- The provider lists card, SBP, T-Pay, SberPay, Mir Pay, installments, subscriptions, and payment links among product capabilities; exact availability is onboarding-dependent.

## Unknowns and blockers

- Public API-specific fee schedule, minimum commitment, overage, settlement terms, and SLA.
- Production rate limits beyond documented test-terminal concurrency guidance.
- Exact rights for storing payment-related data, customer display, SaaS embedding, and redistribution.
- API versioning and deprecation policy for all methods.

## Live testing

Not performed. The documented test method is not treated as a completed live test.

## Decision

Create an active reviewed profile. The API boundary and core operations are documented, but procurement must confirm contract, pricing, limits, and data-rights terms.

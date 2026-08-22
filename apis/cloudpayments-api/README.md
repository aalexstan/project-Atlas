# CloudPayments API

[Русская версия](README.ru.md)

> A documented payment gateway API for online acquiring and related merchant operations.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Provider | CloudPayments |
| Live testing | Not performed |

## Quick Verdict

**Best for:** Online acquiring with card cryptograms, one- or two-stage payments, refunds, subscriptions, and merchant notifications.

**Avoid when:** The decision requires a public API price, production quotas, or a confirmed SLA before contacting the provider.

**Bottom line:** The official developer documentation exposes a clear gateway boundary and many core operations. Commercial terms and some operational guarantees remain procurement questions.

## Technical Access

| Field | Value |
|---|---|
| Base URL | `https://api.cloudpayments.ru` |
| Format | POST; JSON or form encoding; JSON responses |
| Authentication | HTTP Basic Auth with Public ID and API Secret |
| Webhooks | Documented payment, refund, and receipt notifications |
| Sandbox | `/test` method documented; credentials required |
| OpenAPI | Not found in the reviewed official sources |

## Core Capabilities

| Capability | Status |
|---|---|
| Card payment by cryptogram | Documented |
| One- and two-stage payment | Documented |
| Refund and cancellation | Documented |
| Recurring subscriptions | Documented |
| Invoices and payment links | Documented in product materials |
| Notifications | Documented |
| Payouts | Listed as a separate product/API route; scope requires confirmation |

## Commercial Constraints

The reviewed official sources do not provide a complete API-specific public commission table. Confirm commission, minimums, settlement terms, production limits, SLA, storage, SaaS, and redistribution rights in writing.

## Scenario Recommendation

- Choose CloudPayments when a gateway with payment cryptograms, two-stage flows, and subscriptions matches the product architecture.
- Compare YooKassa when public OpenAPI and broad public documentation are more important.
- Compare T-Bank when a banking relationship, settlement workflow, or T-API integration is central.

## Evidence

See [evidence](evidence.md) and the [research log](../../research/payments/2026-08-22-cloudpayments.md).

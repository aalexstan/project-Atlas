# YooKassa API

[Русская версия](README.ru.md)

> A documented payment API for accepting online payments and handling related payment operations.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Provider | YooKassa |
| Live testing | Not performed |

## Quick Verdict

**Best for:** Russian online products that need documented payment creation, refunds, receipts, and payment-status webhooks.

**Avoid when:** The project needs a known production rate limit, SLA, or final commission before a provider quote and contract review.

**Bottom line:** YooKassa has one of the clearest public API documentation sets in this shortlist, including OpenAPI and webhooks. Commercial terms remain merchant-specific.

## Technical Access

| Field | Value |
|---|---|
| Base URL | `https://api.yookassa.ru/v3/` |
| Format | HTTPS/JSON |
| Authentication | HTTP Basic Auth; OAuth for selected partner scenarios |
| OpenAPI | Official YAML specification is documented |
| Webhooks | Payment, refund, payout and other events depending on solution |
| Sandbox | Documented test mode; credentials required |

## Core Capabilities

| Capability | Status |
|---|---|
| Payment acceptance | Documented |
| Refunds | Documented |
| Receipts and fiscal data | Documented |
| Recurring payments | Documented |
| Webhooks | Documented |
| Payouts | Separate onboarding and product route |
| Marketplace split payments | Separate product route |

## Commercial Constraints

The official fee page states that there is no subscription fee and that commission is charged for successful payments. The exact commission and contract conditions are not treated as a universal public API price. Storage, caching, SaaS display, redistribution, production quotas, and SLA require scenario-specific confirmation.

## Scenario Recommendation

- Choose YooKassa for a Russian web or mobile product where payment lifecycle and webhook documentation matter.
- Compare CloudPayments and T-Bank when existing banking relationships, recurring billing, acquiring terms, or settlement conditions dominate.
- Request a written quote and confirm fiscal, data, and operational terms before procurement.

## Evidence

See [evidence](evidence.md) and the [research log](../../research/payments/2026-08-22-yookassa.md).

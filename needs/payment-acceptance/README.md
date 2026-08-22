# Online Payment Acceptance

[Русская версия](README.ru.md)

## The user question

Which API should a Russian website, app, SaaS product, or marketplace use to accept online payments and process refunds reliably?

## Who this route is for

Use this route when you need payment creation, payment status, refunds, receipts, recurring charges, payment links, or webhooks. It is not a legal opinion and does not replace acquiring onboarding.

## Quick choice

| Scenario | Initial shortlist | Main risk | Next Atlas document |
|---|---|---|---|
| Clear public developer journey | YooKassa | Contract-specific fee and quotas | [YooKassa profile](../../apis/yookassa-api/README.md) |
| Two-stage or subscription payments | CloudPayments | Production terms are not public enough for final selection | [CloudPayments profile](../../apis/cloudpayments-api/README.md) |
| T-Bank settlement and account integration | T-Bank Internet Acquiring | Exact acquiring contract depends on onboarding | [T-Bank profile](../../apis/tbank-internet-acquiring-api/README.md) |
| Procurement shortlist | All three | No common quote, SLA, or live benchmark | [Comparison](../../comparisons/payment-acceptance-russia/README.md) |

## Before choosing

Confirm business eligibility, payment methods, receipts and 54-FZ responsibility, refunds, recurring-payment consent, settlement timing, fraud/dispute handling, personal-data processing, storage, SaaS display, quotas, SLA, and deprecation policy.

## Limits of this research

No credentials, live payments, refunds, sandbox calls, latency measurements, or common benchmark were performed. Public pages do not provide directly comparable merchant-specific contracts for all candidates.

## Next step

Use the [payment API comparison](../../comparisons/payment-acceptance-russia/README.md), then send the [procurement checklist](../../procurement/payment-api-selection/README.md) to the shortlisted providers.

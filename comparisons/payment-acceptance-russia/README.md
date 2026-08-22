# Payment Acceptance APIs in Russia

[Русская версия](README.ru.md)

> Scenario-based comparison of APIs for accepting online payments in Russia.

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-08-22 |
| Market | Russia |
| Candidates | YooKassa, CloudPayments, T-Bank Internet Acquiring API |
| Live testing | Not performed |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Fast documented start | YooKassa | Public API reference, OpenAPI, webhooks and refunds are clearly documented. |
| Two-stage payments and subscriptions | CloudPayments | Official docs describe cryptogram payments, two-stage flows and recurring subscriptions. |
| T-Bank settlement and business account | T-Bank Internet Acquiring API | Business and developer materials connect acquiring with CRM/IT integration and T-Bank operations. |
| Lowest predictable cost | Unknown | Quotes and merchant conditions are not comparable yet. |
| Enterprise procurement | All three | Request identical method, limits, SLA and rights answers. |

There is no universal winner. Payment acceptance is a regulated and contract-dependent operation.

## Comparison Matrix

| Criterion | YooKassa | CloudPayments | T-Bank Internet Acquiring |
|---|---|---|---|
| Payment creation | Documented | Documented | Documented at business level; exact method contract open |
| Refunds | Documented | Documented | Documented |
| Two-stage payment | Solution-dependent/documented | Documented | Documented as hold/confirmation |
| Recurring payments | Documented | Documented | Documented |
| Webhooks | Documented | Documented | Documented; activation required |
| OpenAPI | Official YAML documented | Not found in reviewed sources | Portal materials present; exact scope open |
| Authentication | Basic Auth; selected OAuth | Basic Auth | Exact acquiring contract open |
| Sandbox | Documented test mode | Test method documented | Unknown publicly |
| Public API price | Contract-specific commission | Unknown in reviewed sources | Individual commission |
| Production limits | Unknown publicly | Unknown publicly | Unknown publicly |
| SLA | Unknown | Unknown | Unknown |
| Storage/SaaS/redistribution | Requires confirmation | Requires confirmation | Requires confirmation |
| Live test | Not performed | Not performed | Not performed |

## What This Comparison Does Not Establish

- It does not compare web-product prices as API prices.
- It does not establish payment success rates, latency, fraud performance, or SLA.
- It does not replace legal review of 54-FZ, personal-data, PCI DSS, or acquiring contracts.
- A documented test method is not a completed live test.

## Recommendations by Scenario

- Start with YooKassa when public developer documentation and a documented payment lifecycle reduce integration uncertainty.
- Shortlist CloudPayments when card-cryptogram, two-stage, or subscription flows are central.
- Shortlist T-Bank when the acquiring relationship and settlement workflow are part of the architecture.
- Send the same procurement questionnaire to all three before treating cost or reliability as comparable.

See the [payment API procurement kit](../../procurement/payment-api-selection/README.md) and the [Atlas evidence files](evidence.md).

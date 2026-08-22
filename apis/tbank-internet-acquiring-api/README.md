# T-Bank Internet Acquiring API

[Русская версия](README.ru.md)

> An internet acquiring integration route for Russian businesses using T-Bank Business.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Provider | T-Bank |
| Live testing | Not performed |

## Quick Verdict

**Best for:** A Russian business already using or considering T-Bank Business that needs payment integration with a website, app, CRM, or IT system.

**Avoid when:** A provider-neutral architecture requires a fully public method-level contract, sandbox, quota table, and SLA before onboarding.

**Bottom line:** T-Bank clearly documents the business integration route and webhook model, but exact acquiring API terms are tied to onboarding and merchant configuration.

## Technical Access

| Field | Value |
|---|---|
| Portal | `https://developer.tbank.ru/eacq/` and T-API portal |
| Integration | API integration for website, app, CRM and IT systems is documented |
| Webhooks | Payment status and other T-API events; provider-side activation required |
| Sandbox | Unknown in reviewed public materials |
| Authentication | Exact acquiring API contract requires confirmation |
| OpenAPI | Developer portal contains OpenAPI-related materials; exact method set requires confirmation |

## Core Capabilities

| Capability | Status |
|---|---|
| Payment acceptance | Documented |
| Hold and confirmation | Documented in business help |
| Cancellation and refund | Documented |
| Recurring payments | Documented |
| Payment links | Documented |
| Payment-status webhook | Documented; connection required |
| Broader T-API bank operations | Out of scope for this profile |

## Commercial Constraints

The official pricing help states no subscription fee, individually calculated successful-payment commissions, and a fixed fee for unsuccessful authorization. Exact rates and merchant conditions are not universal API prices and require an application/contract.

## Scenario Recommendation

- Choose this route when T-Bank settlement and business-account integration are part of the product decision.
- Prefer YooKassa or CloudPayments when a provider-neutral public API comparison and more self-contained developer documentation matter.
- Obtain the exact API contract, authentication, quotas, SLA, and data-rights terms before implementation.

## Evidence

See [evidence](evidence.md) and the [research log](../../research/payments/2026-08-22-tbank.md).

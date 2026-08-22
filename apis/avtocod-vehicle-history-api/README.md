# Avtocod Vehicle History API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-23 |
| Product class | Commercial vehicle-history API |
| Live testing | Not performed |

## Quick Verdict

**Best for:** B2B workflows that request and retrieve vehicle-history reports after commercial and legal review.

Avtocod documents JSON HTTPS GET/POST, token access, report generation/retrieval, Swagger UI and public report schemas. Quotas are daily, monthly and total; report-frequency limits are contract/report-type specific. Reports normally remain available for six months. Existing-report reads are not charged as new generation, while forced regeneration is paid.

Public B2B pricing confirms `Autofill` at 10 RUB/report and `Autofill Plus` at 11 RUB/report, with individual terms from 10,000 reports. Full vehicle-history pricing remains volume and contract dependent. Webhook delivery is not guaranteed, so polling is required as a fallback.

Provider pages market integrations for insurance, lending, leasing, marketplaces and scoring, but exact storage, redistribution, automated-decision and model-training rights still require a written contract.

See [evidence](evidence.md), the [deep dive](../../research/vehicle-history/2026-08-23-avtocod-deep-dive.md) and the [provider request](../../research/vehicle-history/provider-request.md).

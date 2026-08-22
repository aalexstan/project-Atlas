# Wildberries Seller API

[Русская версия](README.ru.md)

Wildberries provides seller-facing REST/HTTP APIs for integrating marketplace operations with ERP, WMS, OMS and CRM systems. The official documentation is organized by service category and published in Swagger/OpenAPI format.

## Research Status

| Field | Value |
|---|---|
| Maturity | Verified |
| Last verified | 2026-08-23 |
| Product class | Marketplace seller integration API |
| Authentication | Seller account and API token; connection guidance also references OAuth 2.0 scopes |
| Sandbox | Documented for supported test scopes |
| Live testing | Not performed |

## Best For

- Seller catalog, prices and discount workflows.
- Analytics, statistics and promotion integrations.
- Supplies, returns, documents, finance and seller-operations tooling.
- Connecting Wildberries data to internal ERP/WMS/OMS/CRM systems.

## Boundaries

This is a seller integration surface, not a general public marketplace API and not a consumer search or mapping API. Available methods depend on service category and token permissions. Limits are method-specific; the profile records only examples explicitly visible in the official documentation.

API price, SLA, production quotas, storage, SaaS embedding and redistribution terms remain unknown in this review. No credentials were used and no live request was made.

See [evidence](evidence.md), [research log](../../research/wildberries-seller-api/2026-08-23.md) and [open questions](changes.md).

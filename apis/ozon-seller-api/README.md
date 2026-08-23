# Ozon Seller API

[Русская версия](README.ru.md)

Ozon Seller API is the seller-facing integration surface for connecting Ozon seller operations to external systems. The reviewed official materials point to seller workflows around products, prices, stocks, orders, postings, supplies, analytics and finance.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-23 |
| Product class | Marketplace seller integration API |
| Base URL | `https://api-seller.ozon.ru` |
| Authentication | Client ID + API key; OAuth 2.0 for applications is documented in official developer guidance |
| Live testing | Not performed |

## Best For

- Synchronizing seller catalog, prices and stocks.
- Processing orders, postings, supplies and returns.
- Building seller analytics and finance integrations.
- Adding Ozon as a channel to a broader operational system such as MoySklad.

## Boundaries and Confidence

This is a seller API, not a public consumer marketplace API. The official documentation is available at Ozon’s seller API URL, but it could not be fetched reliably in this review because of a redirect-loop limitation in the research environment. The profile therefore remains `reviewed`, not `verified`.

Current method quotas, sandbox availability, API pricing, SLA and data-use rights remain open. No credentials or live requests were used.

See [evidence](evidence.md), [research log](../../research/ozon-seller-api/2026-08-23.md) and [open questions](changes.md).

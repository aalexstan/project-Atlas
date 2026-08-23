# Commerce Operations Integration APIs

[Русская версия](README.ru.md)

> Scenario-based comparison for building software around inventory, orders, documents and marketplace operations.

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-08-23 |
| Market | Russia |
| Candidates | MoySklad JSON API, Wildberries Seller API |
| Live testing | Not performed |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Operational core for a company | MoySklad JSON API | It models inventory, orders, documents and counterparties and is designed for external integrations. |
| Wildberries-only automation | Wildberries Seller API | It exposes seller-side catalog, prices, analytics and operations for the Wildberries account. |
| Several sales channels | MoySklad first, then channel APIs | An ERP-like core can own the common business model while marketplace APIs remain channel connectors. |
| Lowest cost | Unknown | Public API-access statements are not comparable to total plan, support and operating costs. |
| Production selection | Both, scenario-dependent | Obtain target-account limits, SLA, rights and commercial terms before procurement. |

There is no universal winner. These APIs occupy different architectural layers.

## Comparison Matrix

| Criterion | MoySklad JSON API | Wildberries Seller API |
|---|---|---|
| Product class | Cloud ERP integration | Marketplace seller integration |
| Inventory and warehouses | Documented | Seller-scope documented |
| Orders and sales | Documented | Seller-scope documented |
| Catalog and prices | Documented | Documented |
| Documents and finance | Documented | Documented service categories |
| Multi-channel operational core | Stronger fit | Single-channel |
| Authentication | Basic Auth or access token | Seller API token |
| Public API price | Free-access statement with plan limits | Unknown |
| Production limits | Endpoint and plan specific, exact scope open | Method-specific, only partial examples reviewed |
| SaaS/application model | Vendor/server solutions documented | Data-use and SaaS terms unknown |
| SLA and support | Unknown | Unknown |
| Live test | Not performed | Not performed |

## What This Comparison Does Not Establish

- It does not compare Ozon: no active Ozon profile is present in Atlas yet.
- It does not prove that either API can be used for a particular paid SaaS without contract review.
- It does not compare web-product subscription prices with API costs.
- It does not establish throughput, uptime, data quality or reconciliation accuracy.

## Recommendations by Scenario

- Start with MoySklad when the product needs a central model for stock, orders and documents.
- Add Wildberries as a channel connector when the business specifically sells on Wildberries.
- For a unified marketplace panel, define a common internal model first and add Ozon only after an official Ozon profile and comparable evidence exist.

See the [MoySklad evidence](../../apis/moysklad-json-api/evidence.md), [Wildberries evidence](../../apis/wildberries-seller-api/evidence.md) and [Atlas evidence files](evidence.md).

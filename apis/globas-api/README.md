# GLOBAS.API

[Русская версия](README.ru.md)

> Enterprise integration route for bringing GLOBAS counterparty and company data into internal corporate systems.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-28 |
| Provider | Credinform |
| Status | Active product page found |
| Live test | Not performed |
| Public API price | Not found; commercial quote required |

## Quick Verdict

**Best for:** organizations that already evaluate GLOBAS as an enterprise data source and need counterparty data inside CRM, ERP, EDI, risk, portfolio-monitoring, or internal analytics systems.

**Avoid when:** the buyer needs public self-service API documentation, transparent method-level pricing, published rate limits, or a confirmed sandbox before vendor contact.

**Bottom line:** GLOBAS.API is a credible additional enterprise candidate for Russian counterparty-data integration, but it is not yet a reference-grade developer profile. Procurement must request the API specification, authentication model, field matrix, batch rules, method-level pricing, SLA, and data-use rights.

## What It Does

The official GLOBAS.API page presents the product as a way to integrate GLOBAS data into corporate systems. The page describes scenarios such as keeping counterparty information current in a user's database, monitoring portfolio changes, mass counterparty checks, building an automatically updated client base, enriching an internal base with GLOBAS company data, updating selected fields, verifying data, storing archives, and automatically updating large counterparty databases.

Atlas treats those statements as **provider-reported official product positioning**. The public pages reviewed did not expose a detailed endpoint catalog or schema-level documentation.

## Technical Access

| Field | Value | Status |
|---|---|---|
| Public product identity | GLOBAS.API on the official GLOBAS/Credinform site | verified |
| Integration model | GLOBAS data integration into corporate systems | provider_reported |
| Protocol | Not publicly confirmed | unknown |
| Base URL / endpoint catalog | Not found in reviewed public pages | unknown |
| Authentication | Not found in reviewed public pages | unknown |
| Request/response schemas | Not found in reviewed public pages | unknown |
| Formats | Not found in reviewed public pages | unknown |
| OpenAPI/Swagger | Not found in reviewed public pages | unknown |
| Rate limits / quotas | Not found in reviewed public pages | unknown |
| SLA | Not found in reviewed public pages | unknown |
| Live testing | Not performed | verified |

The legacy `catalog/globas-api.md` card contains a REST claim from API Portal. Atlas keeps that as legacy provenance only; it is **not** promoted to verified because reviewed Credinform pages did not confirm REST, endpoint paths, or schemas.

## Pricing and Trial

No public API-specific price, method price, batch price, minimum commitment, overage model, or public SLA was found in the reviewed official pages.

The GLOBAS site offers a three-day test access flow for the GLOBAS system. Atlas does **not** treat this as an API trial until Credinform confirms API credentials, sandbox/API access, or equivalent technical test terms.

## Product Boundary

Credinform has a separate official page for a sanctions-compliance product/module. Atlas does **not** assume that "Sanctions Compliance" is included in the standard GLOBAS.API scope. A buyer should request the boundary between:

- standard GLOBAS.API;
- Sanctions Compliance;
- Portfolio / monitoring workflows;
- foreign-company reports or references;
- any custom data delivery service.

## Strengths

- Official API product page exists.
- Product is positioned for enterprise-system integration rather than only manual web use.
- Official pages describe mass checks, portfolio monitoring, internal-base enrichment, field updates, verification, archives, and large database updates.
- GLOBAS source coverage pages provide useful context for the broader GLOBAS data platform.

## Weaknesses and Blockers

- Public endpoint catalog was not found.
- Public authentication and sandbox terms were not found.
- Public request/response formats and schemas were not found.
- Public API price, batch billing, limits, and SLA were not found.
- Data storage, caching, redistribution, customer display, affiliate use, SaaS embedding, and model-training rights require written confirmation.

## Scenario Fit

| Scenario | Fit | Reason |
|---|---|---|
| CRM/ERP/EDI enrichment | Candidate | Official page positions API for corporate-system integration |
| Mass counterparty checks | Candidate | Official page describes mass verification |
| Portfolio monitoring | Candidate | Official page describes monitoring changes in a counterparty portfolio |
| Public self-service developer integration | Weak until documented | No public specification, endpoints, auth, schemas, limits, or API price found |
| Sanctions / 115-FZ compliance | Separate evaluation | Sanctions Compliance appears as a separate product/module boundary |

## Alternatives

- **DaData:** faster self-service start, public API documentation and pricing for company details and autocomplete.
- **Kontur.Focus API:** primary enterprise shortlist candidate for due diligence, monitoring, and risk controls.
- **Seldon.Basis API:** primary enterprise shortlist candidate for relationships, procurement context, CIS coverage, and configurable methods.
- **FTS EGRUL/EGRIP integration:** primary registry feed for organizations that can build and operate their own ETL.

## Sources

- https://globas.credinform.ru/ru-RU/servisy/globas-api
- https://globas.credinform.ru/ru-RU/servisy
- https://globas.credinform.ru/ru-RU/osisteme/istochniki
- https://globas.credinform.ru/ru-RU/disclaimer
- https://globas.credinform.ru/ru-RU/requirements
- https://globas.credinform.ru/ru-RU/servisy/sanctions

## Disclosure

No commercial relationship is known. No live API credentials, sandbox, private documentation, or customer demo access were used.

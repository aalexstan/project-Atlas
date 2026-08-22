# Seldon.Tenders Profile Decision

[Русская версия](decision.ru.md)

## Decision

**Result: 3. Preserve only as legacy until stronger official evidence is available.**

Do not create an active API-first profile for Seldon.Tenders in this pass.

## Rationale

Official Seldon pages confirm that `API.Seldon.Tenders` exists as a procurement-data integration route under Seldon 1.7, and that it is described as a programmatic interface for procurement data. Official Seldon news also shows that the Seldon.Tenders web product name later changed to Seldon.Win.

However, the reviewed official public pages do not provide the minimum developer/procurement evidence needed for an active Atlas API profile:

- endpoint catalog or base URL;
- authentication;
- request and response schemas;
- formats;
- OpenAPI/Swagger;
- rate limits and quotas;
- SLA and support terms;
- API-specific pricing and billing units;
- storage, caching, redistribution and SaaS-embedding rights.

## Not Chosen

**Option 1 — create a separate API-first profile:** not chosen yet. The official product identity exists, but the current evidence is insufficient for an active profile without excessive unknowns.

**Option 2 — include as capability of Seldon.Basis:** not chosen. The official pages place `API.Seldon.Tenders` under Seldon 1.7 procurement functionality, not as a Seldon.Basis capability.

## Legacy Handling

Keep [catalog/api-seldon-tenders.md](../../catalog/api-seldon-tenders.md) as provenance and source-risk history.

The old `api-seldon.ru` URL remains a historical risk note only. It must not be used as a current official source.

## Reopen Conditions

Reconsider an active profile if Seldon publishes or provides:

- API specification or OpenAPI/Swagger;
- official endpoint and authentication model;
- method and field matrix;
- sandbox or test credentials;
- API pricing, limits and SLA;
- data-use rights for storage, display, redistribution, affiliates and SaaS embedding.

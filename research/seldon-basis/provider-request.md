# Provider Request — Seldon.Basis API

[Русская версия](provider-request.ru.md)

This checklist is prepared for a vendor conversation with Seldon. It must not be treated as provider answers until Seldon responds in writing or provides official documentation.

## Context

Atlas currently treats Seldon.Basis API as an active reviewed enterprise candidate for company enrichment, relationship analysis, procurement context and risk analysis. Public Atlas blockers remain: method pricing, batch billing, authentication, SLA, data rights and versioning.

## Official Atlas Sources to Attach

- [`apis/seldon-basis/README.md`](../../apis/seldon-basis/README.md)
- [`apis/seldon-basis/evidence.md`](../../apis/seldon-basis/evidence.md)
- [`comparisons/company-counterparty-data-russia/README.md`](../../comparisons/company-counterparty-data-russia/README.md)
- [`procurement/counterparty-api-selection/docs/RFP.md`](../../procurement/counterparty-api-selection/docs/RFP.md)

## Product Scope

1. Which Seldon.Basis API products, packages and methods are included in the offer?
2. What is the boundary between Seldon.Basis API, Seldon 1.7, Seldon.Tenders/Seldon.Win, monitoring, sanctions/compliance and international company data?
3. Which countries, entity types and registry/source categories are covered?
4. Which relationship graph, procurement, court, finance, enforcement, license, media and sanctions fields are standard?
5. Which fields are source-derived, provider-calculated, manually curated, inferred or score-like?

## Methods and Fields

1. Please provide a complete method catalog.
2. Please provide a method-by-field matrix with source, update cadence and package availability.
3. Which lookup keys are supported: INN, OGRN, KPP, name, address, manager, owner, phone, website, procurement identifier or foreign identifier?
4. Which methods support relationship graphs, affiliated persons, owners, managers, procurement context and monitoring events?
5. Which methods return source documents, timestamps, confidence levels or source references?

## Protocol and Authentication

1. Please provide Swagger/OpenAPI or complete API specification.
2. What is the production base URL?
3. What authentication model is used: API key, token, OAuth, mTLS, IP allowlist, signed request or another model?
4. Are sandbox and production credentials separate?
5. How are method permissions, key rotation and IP restrictions managed?

## Formats, Versioning and Errors

1. Which request and response formats are supported?
2. Please confirm JSON schemas and any XML/CSV/export options.
3. How is API versioning handled?
4. What is the breaking-change policy and notice period?
5. Please provide error codes for not-found, partial result, validation, authentication, quota, throttling and incident states.
6. What retry/backoff and idempotency guidance applies?

## Pricing and Billing

1. Please provide API-specific pricing, not web-product pricing.
2. How are the universal package and individual per-method plans priced?
3. Which methods are included in the universal package?
4. How is batch billing calculated?
5. How are not-found results, errors, retries, duplicate lookups and cached results billed?
6. What minimum commitment, setup fee, support fee and overage rules apply?
7. Are there separate fees for relationship graph, monitoring, procurement, international, sanctions or portfolio functions?

## Batch, Async and Monitoring

1. Please confirm maximum batch size, including the publicly reported 1,000 taxpayer IDs.
2. Are asynchronous jobs available for large batches?
3. Are webhooks, callbacks, exports, SFTP or scheduled portfolio updates supported?
4. Are monitoring events available through API?
5. How are batch partial failures represented and billed?
6. Are method-level daily request limits negotiable?

## Limits, SLA and Support

1. What are production daily, monthly, burst, concurrency and per-second limits by method?
2. Are limits per key, account, IP, method, user or contract?
3. What uptime SLA, latency SLA and support response SLA are available?
4. What data freshness SLA or expected source-update delay applies?
5. Is there a status page, incident history, maintenance notice process or customer mailing list?
6. What remedies apply for SLA breach?

## Data Rights and Legal Use

1. May API responses be stored? If yes, for how long and under what refresh rules?
2. May responses be cached? If yes, what TTL applies?
3. May results be shown to customers, partners, affiliates or SaaS users?
4. May data be redistributed, resold, exported or embedded in third-party products?
5. May outputs be used for scoring, automated decisions, model training, deduplication or internal analytics?
6. Which fields contain personal data and what roles, DPA terms and jurisdiction apply?
7. What retention, deletion, audit and post-termination obligations apply?

## Source-Risk Clarification

1. Please confirm current official documentation domains and which historical `api-seldon.ru` materials should be considered obsolete.
2. Please identify any official changelog or migration notes from legacy documentation to current `seldongroup.ru` documentation.

## Attachments Requested

- Swagger/OpenAPI or complete specification.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- API-specific price list.
- Batch billing appendix.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS terms.
- Changelog or versioning policy.

# Provider Request — Kontur.Focus API

[Русская версия](provider-request.ru.md)

This checklist is prepared for a vendor conversation with Kontur. It must not be treated as provider answers until Kontur responds in writing or provides official documentation.

## Context

Atlas currently treats Kontur.Focus API as an active reviewed enterprise candidate for company and counterparty verification. Public Atlas blockers remain: API-specific price, production limits, SLA, full specification, storage rights, redistribution rights and contract appendices.

## Official Atlas Sources to Attach

- [`apis/kontur-focus/README.md`](../../apis/kontur-focus/README.md)
- [`apis/kontur-focus/evidence.md`](../../apis/kontur-focus/evidence.md)
- [`comparisons/company-counterparty-data-russia/README.md`](../../comparisons/company-counterparty-data-russia/README.md)
- [`procurement/counterparty-api-selection/docs/RFP.md`](../../procurement/counterparty-api-selection/docs/RFP.md)

## Product Scope

1. Which Kontur.Focus API products, modules and methods are included in the standard API offer?
2. Which capabilities are outside the standard API and require separate license, custom project or manual service?
3. Are monitoring, risk flags, arbitration, enforcement proceedings, beneficial ownership, finance, sanctions/compliance or international company data included?
4. Which legal entities, individual entrepreneurs, branches, foreign entities and historical records are covered?
5. Which fields are provider-calculated, source-derived, manually curated or inferred?

## Methods and Field Matrix

1. Please provide the complete method catalog.
2. Please provide a field matrix by method, tariff/package and data source.
3. Which lookup keys are supported: INN, OGRN, KPP, name, address, manager, founder, phone, email, bank account or foreign identifier?
4. Which methods return current data, historical data, source documents, risk indicators, monitoring events or relationship graphs?
5. Which fields have source references, timestamps, confidence levels, update dates or legal-source identifiers?

## Specification and Authentication

1. Please provide OpenAPI/Swagger or a complete API specification.
2. What is the production base URL?
3. What authentication model is used: developer key, API key, OAuth, token, mTLS, IP allowlist, signed request or another mechanism?
4. How are keys issued, rotated, revoked and scoped?
5. Are sandbox and production credentials separate?
6. Does sandbox behavior match production for schemas, errors, limits and sample data?

## Formats, Versioning and Errors

1. Which request and response formats are supported?
2. What encoding and date/time formats are used?
3. How is API versioning handled?
4. What is the breaking-change policy and notice period?
5. Please provide error codes for validation, not-found, quota, authentication, throttling, partial failure and provider incidents.
6. What retry, idempotency and backoff guidance applies?

## Pricing and Billing

1. Please provide API-specific pricing, not web-product pricing.
2. Is pricing based on request, successful request, method, field, record, package, company, monitoring event or another unit?
3. Which fields, reports or methods cost extra?
4. What are minimum commitment, setup fee, support fee and integration fee?
5. How are overage, retries, duplicate requests, not-found results and partial failures billed?
6. Are volume tiers, annual discounts or multi-entity group licenses available?

## Batch, Monitoring and Delivery

1. Which methods support batch requests?
2. What are maximum batch size, file size, record count and processing window?
3. Are asynchronous jobs supported?
4. Are webhooks, callbacks, exports, SFTP or scheduled deliveries supported?
5. How are monitoring events generated, deduplicated and billed?
6. Are portfolio-level alerts available through API?

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

## Attachments Requested

- OpenAPI/Swagger or complete specification.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- API-specific price list.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS terms.
- Changelog or versioning policy.

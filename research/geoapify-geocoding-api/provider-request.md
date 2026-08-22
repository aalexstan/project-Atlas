# Provider Request - Geoapify Geocoding API

[Русская версия](provider-request.ru.md)

This checklist is prepared for a vendor conversation with Geoapify about Geoapify Geocoding API. It must not be treated as provider answers until Geoapify responds in writing or points to official documentation.

## Context

Atlas treats [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.md) as an active reviewed hosted commercial open-data geocoding route. Public blockers remain: ODbL/attribution interpretation, DPA/privacy, SaaS/redistribution rights, benchmark quality, batch edge cases and contract terms for paid/enterprise plans.

## Product Boundary

1. Please confirm the boundary between Geocoding API, Address Autocomplete, Places API, Place Details, Routing, Matrix and Isochrone APIs.
2. Which features share the same credit model, and which require separate products or contracts?
3. Does the Geocoding API provide address validation guarantees, or only geocoding confidence/match metadata?
4. Which use cases require Places API rather than Geocoding API?

## Methods, Schemas and Versioning

1. Please provide the current OpenAPI/Swagger specification or complete method reference for forward, reverse and batch geocoding.
2. Which response fields are stable identifiers, display labels, coordinates, confidence values, data-source fields and administrative hierarchy?
3. Which request and response formats are officially supported in production?
4. What error codes, retry guidance and idempotency rules apply?
5. What notice period applies to breaking changes, field removals, tariff changes, data-source changes and deprecations?

## Pricing, Quotas and Billing

1. Please confirm credit cost per forward, reverse, autocomplete, batch and failed/no-result request.
2. How are retries, duplicates, partial failures and expired batch results billed?
3. What daily credits, RPS, concurrency and burst limits apply by plan?
4. Are higher RPS limits available without a dedicated geocoding server?
5. What minimum commitment, setup fee, support fee or SLA fee applies to enterprise plans?

## Storage, Attribution and Data Rights

1. Which response fields may be stored permanently?
2. What attribution must be shown in maps, non-map UI, exports, printed reports and customer-facing SaaS?
3. What ODbL obligations apply to cached results, derived databases, normalized address tables and geocoded customer datasets?
4. Is redistribution, resale, API proxying, affiliate use or white-label SaaS embedding allowed?
5. Are there deletion, refresh or post-termination duties?
6. May outputs be used for scoring, analytics, routing pre-processing, ML/model training or address-quality decisions?

## Batch and Operations

1. What production limits apply to batch input count, concurrent jobs, daily batch credits and result retention?
2. Are larger batch jobs supported by contract?
3. How should buyers handle partial failures, polling, retries, expired results and audit evidence?
4. Are status pages, incident notifications and usage exports available?

## Privacy, Security and Compliance

1. Is a DPA available?
2. Which data centers process default API requests?
3. Can a customer select EU-only or other regional processing?
4. What personal-data restrictions apply to submitted addresses or coordinates?
5. Are IP/domain restrictions, key rotation and per-project permissions available?

## Benchmark and Pilot

1. Can Geoapify provide pilot credentials for a legal benchmark sample?
2. May benchmark request/response evidence be stored internally for procurement audit?
3. Which metrics does Geoapify recommend for precision, match level, latency, false positives and missing results?
4. Can Geoapify help interpret confidence scores and match levels for house/street/locality-level results?

## Attachments Requested

- OpenAPI/Swagger or current complete specification.
- Field matrix and source/attribution matrix.
- Paid-plan terms and enterprise contract appendix.
- SLA/support appendix.
- DPA/privacy/security materials.
- Batch operations guide.
- Changelog/deprecation policy.

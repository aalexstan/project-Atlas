# Provider Request - OpenCage Geocoding API

[Русская версия](provider-request.ru.md)

This checklist is prepared for a vendor conversation with OpenCage about OpenCage Geocoding API. It must not be treated as provider answers until OpenCage responds in writing or points to official documentation.

## Context

Atlas treats [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.md) as an active reviewed hosted commercial open-data geocoding route. Public blockers remain: ODbL/attribution interpretation, redistribution/SaaS rights, enterprise SLA, privacy/DPA, benchmark quality and high-volume batch workflow fit.

## Product Boundary

1. Please confirm the boundary between Geocoding API, Geosearch/autosuggest, spreadsheet upload and any enterprise/custom services.
2. Does the Geocoding API provide address validation guarantees, or only geocoding confidence/components?
3. Which use cases require Geosearch rather than Geocoding API?
4. Are routing, distance matrix, place search or address cleaning available as separate products or out of scope?

## Methods, Schemas and Versioning

1. Please provide the current OpenAPI specification or complete method reference.
2. Which response fields are stable identifiers, display labels, coordinates, confidence values, components and attribution/source indicators?
3. Which request and response formats are supported long-term?
4. What error codes, retry guidance and idempotency rules apply?
5. What notice period applies to breaking changes, field removals, pricing changes, data-source changes and deprecations?

## Pricing, Quotas and Billing

1. Please confirm current pricing currency for the buyer's country, VAT/tax treatment and annual options.
2. How do soft subscription limits work contractually if daily averages repeatedly exceed the plan?
3. How are failed, invalid, no-result and retried requests billed?
4. What daily, monthly, per-second, burst and concurrency limits apply by plan?
5. Are higher RPS limits available without an enterprise contract?
6. What minimum commitment, setup fee, support fee or SLA fee applies to enterprise plans?

## Storage, Attribution and Data Rights

1. Which response fields may be stored permanently?
2. What attribution must be shown in maps, non-map UI, exports, printed reports and customer-facing SaaS?
3. What ODbL obligations apply to cached results, derived databases, normalized address tables and geocoded customer datasets?
4. Is redistribution, resale, API proxying, affiliate use or white-label SaaS embedding allowed?
5. Are there deletion, refresh or post-termination duties?
6. May outputs be used for scoring, analytics, routing pre-processing, ML/model training or address-quality decisions?

## Batch and Operations

1. What is the recommended production design for millions of records if the API accepts one location per request?
2. What spreadsheet upload limits, retention periods and audit evidence apply by plan?
3. How should buyers handle parallelization, partial failures, retries, no-result responses and duplicate submissions?
4. Are status pages, incident notifications and usage exports available?

## Privacy, Security and Compliance

1. Is a DPA available?
2. Which data centers process default API requests?
3. Can a customer select EU-only or other regional processing?
4. What personal-data restrictions apply to submitted addresses or coordinates?
5. How should buyers use `no_record`, and does it affect support/debugging?
6. Are IP restrictions, domain/CORS restrictions, key rotation and per-project permissions available?

## Benchmark and Pilot

1. Can OpenCage provide pilot credentials for a legal benchmark sample?
2. May benchmark request/response evidence be stored internally for procurement audit?
3. Which metrics does OpenCage recommend for precision, match level, latency, false positives and missing results?
4. Can OpenCage help interpret confidence scores and components for house/street/locality-level results?

## Attachments Requested

- OpenAPI specification or current complete method reference.
- Field/source/attribution matrix.
- Paid-plan and enterprise terms.
- SLA/support appendix.
- DPA/privacy/security materials.
- High-volume operations guide.
- Changelog/deprecation policy.

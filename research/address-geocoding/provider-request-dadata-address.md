# Provider Request - DaData Address APIs

[Русская версия](provider-request-dadata-address.ru.md)

This checklist is prepared for a vendor conversation with DaData about address suggestions, address cleaning, direct geocoding and reverse geocoding. It must not be treated as provider answers until DaData responds in writing or provides official documentation.

## Context

Atlas currently treats [`DaData Address APIs`](../../apis/dadata-address-api/README.md) as an active reviewed candidate for Russian address autocomplete, address cleaning, direct geocoding and reverse geocoding. Public Atlas blockers remain: endpoint-specific data rights, SLA, support tiers, endpoint-level OpenAPI scope, batch/asynchronous options and independent quality benchmarks.

## Official Atlas Sources to Attach

- [`apis/dadata-address-api/README.md`](../../apis/dadata-address-api/README.md)
- [`apis/dadata-address-api/evidence.md`](../../apis/dadata-address-api/evidence.md)
- [`comparisons/address-normalization-geocoding/README.md`](../../comparisons/address-normalization-geocoding/README.md)
- [`procurement/address-geocoding-api-selection/RFP.md`](../../procurement/address-geocoding-api-selection/RFP.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.md)

## Product Scope

1. Which DaData address endpoints are included in the standard address API offer: address suggestions, address cleaning, direct geocoding, reverse geocoding, postal enrichment, FIAS/GAR identifiers, KLADR identifiers, cadastral lookup or other methods?
2. Which address capabilities belong to subscription services, and which are pay-per-record services?
3. Which capabilities are outside the standard address API scope and require a separate contract, custom project or file-processing service?
4. Are company suggestions, party enrichment or counterparty data ever bundled with address APIs, or should they be contracted separately?
5. Which countries and address granularities are covered by each endpoint?

## Methods and Field Matrix

1. Please provide the complete endpoint and method list for address suggestions, cleaning, direct geocoding and reverse geocoding.
2. Please provide a field matrix by endpoint, tariff/package, country and address granularity.
3. Which fields are returned for FIAS/GAR, KLADR, postal code, geolocation, timezone, tax office, region, city, street, house, block, building, structure and flat/apartment data?
4. Which quality fields indicate house-level, street-level, locality-level, inferred, ambiguous, missing or approximate matches?
5. Which fields are registry-derived, provider-calculated, normalized, user-input echoes or inferred?
6. Which fields have update dates, source references, confidence levels or quality codes?

## Protocol, Authentication and Key Handling

1. Please confirm production base URLs for all address endpoints.
2. Which endpoints require only an API token, and which require both token and secret key?
3. Which endpoints may be called safely from browser JavaScript, mobile apps, backend systems and serverless environments?
4. How should keys be issued, scoped, rotated, revoked and restricted by domain, IP, app or environment?
5. Are separate credentials available for sandbox/test and production?
6. Are method-level permissions available to prevent accidental cleaning/geocoding charges from a suggestions-only integration?

## Formats, Schemas, Versioning and Errors

1. Please provide endpoint-specific schemas or OpenAPI/Swagger coverage for address suggestions, cleaning, direct geocoding and reverse geocoding.
2. Which request and response formats, encodings and date formats are supported?
3. How are nullable fields, unknown registry identifiers, partial matches and quality codes represented?
4. What is the error model for validation errors, not-found results, quota errors, authentication failures, throttling and provider incidents?
5. How is API versioning handled?
6. What notice period applies to field removals, schema changes, endpoint deprecations, pricing changes and source-coverage changes?

## Sandbox, Trial and Benchmark

1. Can DaData provide test credentials for all address endpoints without exposing production keys?
2. Are test requests billable?
3. Does the public playground reflect production schemas, rate limits, quality codes and edge cases?
4. May a buyer run a reproducible benchmark against a legal synthetic or public address sample?
5. Can benchmark outputs be stored in Atlas or internal procurement evidence with request IDs and timestamps?
6. What support can DaData provide for interpreting quality codes and coordinate precision during a pilot?

## Batch, Async and File Processing

1. Is address cleaning limited to one address per HTTP request in standard API use?
2. Are batch HTTP requests, asynchronous jobs, file upload, SFTP delivery, callbacks or webhook delivery available for high-volume cleaning/geocoding?
3. What are the maximum record count, file size, request payload size, processing window and concurrency limits?
4. Are batch and file-processing terms priced differently from per-record API cleaning?
5. How are duplicate records, retries, validation errors and partial failures billed?
6. Are suggestions endpoints allowed for automatic processing of address files or databases under any contract variant?

## Pricing and Billing

1. Please provide endpoint-level pricing for suggestions, address cleaning, direct geocoding, reverse geocoding, cadastral lookup and any additional address enrichment.
2. Which quotas are shared across subscription services?
3. Which limits are per IP, per token, per account, per method, per day, per second or per contract?
4. What minimum commitment, setup fee, support fee or SLA fee applies?
5. How are overage, retries, invalid requests, not-found results, cached results and duplicate records billed?
6. Which prices are API prices rather than web UI, file-upload or manual-processing prices?

## Limits, SLA and Support

1. What production rate limits apply by endpoint, tariff and contract?
2. Are burst, concurrency, daily, monthly or new-connection limits negotiable?
3. What uptime SLA, latency SLA, support response SLA and data-freshness SLA are available?
4. Is there a public or customer status page, incident channel, maintenance notice process or support escalation path?
5. What remedies apply for SLA breach?
6. Are there enterprise support, private channel or dedicated account-management options?

## Data Rights and Legal Use

1. May the buyer store API responses from suggestions, cleaning, direct geocoding and reverse geocoding? If yes, for how long?
2. May the buyer cache responses? If yes, what TTL and refresh rules apply?
3. May normalized addresses, coordinates, FIAS/GAR identifiers and quality codes be stored in the buyer's CRM, ERP, warehouse or master-data system?
4. May results be displayed to customers, partners, affiliates or SaaS users?
5. May the buyer redistribute, resell, export or embed results in third-party products?
6. May outputs be used for scoring, deduplication, fraud checks, model training, address-quality analytics or automated decisions?
7. Which address fields may contain personal data or personal-data-like information, and what legal roles and DPA terms apply?
8. What retention, deletion, audit, attribution and post-termination obligations apply?

## Attachments Requested

- Endpoint-specific specification or OpenAPI/Swagger.
- Method and field matrix.
- Sample requests and responses for suggestions, cleaning, direct geocoding and reverse geocoding.
- Quality-code and coordinate-precision guide.
- Error-code reference.
- Sandbox/test credential instructions.
- Endpoint-level price list and quota table.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS-embedding terms.
- Changelog, deprecation and breaking-change policy.

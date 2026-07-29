# Provider Request - Yandex Maps Geosuggest, Geocoder and Organization Search APIs

[Русская версия](provider-request-yandex-maps.ru.md)

This checklist is prepared for a vendor conversation with Yandex about Yandex Maps Geosuggest API, Yandex Maps Geocoder API and Yandex Maps Organization Search API. It must not be treated as provider answers until Yandex responds in writing or provides official documentation.

## Context

Atlas currently treats [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md) and [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.md) as separate active reviewed products. Public Atlas blockers remain: production RPS/SLA where not published, exact storage/display/SaaS rights, batch/offline restrictions, OpenAPI availability and independent quality benchmarks.

## Official Atlas Sources to Attach

- [`apis/yandex-maps-geosuggest-api/README.md`](../../apis/yandex-maps-geosuggest-api/README.md)
- [`apis/yandex-maps-geocoder-api/README.md`](../../apis/yandex-maps-geocoder-api/README.md)
- [`apis/yandex-maps-organization-search-api/README.md`](../../apis/yandex-maps-organization-search-api/README.md)
- [`apis/yandex-maps-geosuggest-api/evidence.md`](../../apis/yandex-maps-geosuggest-api/evidence.md)
- [`apis/yandex-maps-geocoder-api/evidence.md`](../../apis/yandex-maps-geocoder-api/evidence.md)
- [`apis/yandex-maps-organization-search-api/evidence.md`](../../apis/yandex-maps-organization-search-api/evidence.md)
- [`comparisons/address-normalization-geocoding/README.md`](../../comparisons/address-normalization-geocoding/README.md)
- [`procurement/address-geocoding-api-selection/RFP.md`](../../procurement/address-geocoding-api-selection/RFP.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.md)

## Product Boundaries

1. Please confirm the exact product boundary between Geosuggest API, Geocoder API, Organization Search API, other Search APIs, routing, matrix APIs and JavaScript map components.
2. Which Geosuggest responses are intended to be resolved through the Geocoder API, and what fields or identifiers should be used for the handoff?
3. Does Geosuggest provide organization autocomplete only, or can it be used as a full organization search product?
4. Which Organization Search use cases require Organization Search API rather than Geosuggest or Geocoder?
5. Does Geocoder provide any address normalization or validation guarantees beyond geocoding precision metadata?
6. Which capabilities require separate licenses or contracts?

## Methods and Field Matrix

1. Please provide a complete method and parameter matrix for Geosuggest, Geocoder and Organization Search.
2. Which fields are returned for address suggestions, geographic objects, organizations, coordinates, precision, administrative hierarchy and metadata?
3. Which fields are stable identifiers, display labels, provider-internal identifiers, temporary URIs or geocoder handoff values?
4. Which parameters affect geography, language, bounding boxes, result type, result count and strict bounds?
5. Which fields are available only under specific license variants?
6. Are there separate field semantics for Russia, CIS countries, Turkey or other regions?

## Protocol, Authentication and Key Handling

1. Please confirm production base URLs for Geosuggest, Geocoder and Organization Search.
2. Are API keys issued, restricted and billed separately for Geosuggest, Geocoder and Organization Search?
3. Can keys be restricted by domain, IP, app, environment or API family?
4. Are separate credentials available for test and production?
5. How are keys rotated, revoked and scoped?
6. Are there per-method permissions to prevent accidental paid usage across Geosuggest, Geocoder, Search or routing APIs?

## Formats, Schemas, Versioning and Errors

1. Are OpenAPI/Swagger specifications available for Geosuggest, Geocoder and Organization Search?
2. Which request and response formats are officially supported?
3. What error codes and retry guidance apply to validation errors, authentication failures, quota exhaustion, rate limits, not-found results and provider incidents?
4. How is API versioning handled?
5. What notice period applies to breaking changes, field removals, tariff changes, deprecations and coverage changes?
6. Is there an official changelog, mailing list, status page or customer notification process?

## Pricing and Billing

1. Please confirm API-specific pricing for Geosuggest, Geocoder and Organization Search by license type and request package.
2. What is included in Standard and Extended licenses for each product?
3. Which license allows data storage, and exactly which data can be stored?
4. How are additional requests, retries, failed requests, no-result responses, duplicate requests and cached results billed?
5. What minimum commitment, setup fee, support fee or SLA fee applies?
6. How should a buyer price a workflow where Geosuggest suggestions trigger Geocoder requests and/or Organization Search requests?

## Limits, Quotas and Production Suitability

1. What production requests-per-second limits apply to Geosuggest, Geocoder and Organization Search?
2. Are limits per key, account, IP, API family, project, domain or contract?
3. Are burst, concurrency, daily and monthly quotas negotiable?
4. What limits apply to test-period keys?
5. Is batch or offline geocoding allowed under any contract?
6. Are there restrictions on automated enrichment of address files, CRM databases or data warehouses?

## Display, Storage and Data Rights

1. When must Geosuggest, Geocoder or Organization Search results be displayed on a Yandex map?
2. May results be displayed on third-party maps or in non-map UI?
3. May the buyer store suggestions, selected labels, coordinates, geocoder precision, administrative fields and raw responses?
4. May the buyer cache results? If yes, what TTL and refresh rules apply?
5. May results be shown to customers, partners, affiliates or SaaS users?
6. Is redistribution, resale, export or embedding in third-party products allowed?
7. May outputs be used for scoring, analytics, model training, routing pre-processing or address-quality decisions?
8. What attribution, copyright notice and post-termination deletion duties apply?

## Sandbox, Trial and Benchmark

1. Can Yandex provide test credentials for both products with realistic limits?
2. Are test requests billable?
3. Can a buyer run a side-by-side benchmark against DaData, 2GIS, FIAS/GAR or self-hosted Nominatim using a legal sample?
4. May benchmark request/response evidence be stored internally for procurement audit?
5. Which metrics does Yandex recommend for precision, match level, latency and user-input autocomplete quality?

## SLA and Support

1. What uptime SLA, latency SLA, support response SLA and incident communication are available?
2. Is there a public or customer status page for Maps API incidents?
3. What support channels are included by license?
4. What remedies apply for SLA breach?
5. Is enterprise support available for high-volume, SaaS or mission-critical usage?

## Attachments Requested

- Product boundary note for Geosuggest, Geocoder, Search and routing APIs.
- Method and field matrix.
- OpenAPI/Swagger or complete specifications.
- Sample requests and responses.
- Error-code reference and retry guidance.
- API-specific tariff appendix with Standard/Extended rights.
- SLA/support appendix.
- Storage, caching, display, attribution, redistribution, affiliate-use and SaaS terms.
- Changelog, deprecation and breaking-change policy.

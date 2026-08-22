# Provider Request - 2GIS Suggest, Places and Geocoder APIs

[Русская версия](provider-request-2gis-search.ru.md)

This checklist is prepared for a vendor conversation with 2GIS about Suggest API, Places API and Geocoder API in the 2GIS Search API family. It must not be treated as provider answers until 2GIS responds in writing or provides official documentation.

## Context

Atlas currently treats [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md), [`2GIS Places API`](../../apis/2gis-places-api/README.md) and [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md) as separate active reviewed products. Public Atlas blockers remain: OpenAPI/Swagger, SLA, exact storage/caching/display/SaaS rights, batch restrictions, on-demand field/method matrix and independent quality benchmarks.

## Official Atlas Sources to Attach

- [`apis/2gis-suggest-api/README.md`](../../apis/2gis-suggest-api/README.md)
- [`apis/2gis-places-api/README.md`](../../apis/2gis-places-api/README.md)
- [`apis/2gis-geocoder-api/README.md`](../../apis/2gis-geocoder-api/README.md)
- [`apis/2gis-suggest-api/evidence.md`](../../apis/2gis-suggest-api/evidence.md)
- [`apis/2gis-places-api/evidence.md`](../../apis/2gis-places-api/evidence.md)
- [`apis/2gis-geocoder-api/evidence.md`](../../apis/2gis-geocoder-api/evidence.md)
- [`comparisons/address-normalization-geocoding/README.md`](../../comparisons/address-normalization-geocoding/README.md)
- [`procurement/address-geocoding-api-selection/RFP.md`](../../procurement/address-geocoding-api-selection/RFP.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.md)

## Product Boundaries

1. Please confirm the exact boundary between Suggest API, Places API, Geocoder API, Routing APIs and any On-Premise/API export products.
2. Which scenarios require buying more than one 2GIS Search product?
3. When should a Suggest result be followed by a Places request, a Geocoder request or another API?
4. Which APIs cover address suggestions, street suggestions, organization suggestions, organization/place search, direct geocoding and reverse geocoding?
5. Which capabilities are unavailable in the public cloud API and require On-Premise, custom project or separate contract?

## Methods and Field Matrix

1. Please provide the complete method catalog for Suggest, Places and Geocoder.
2. Please provide a field matrix by product, method, package, geography and object type.
3. Which Places fields and methods are on-demand or extra-cost: contacts, rubrics, ITIN/INN, FIAS identifiers, OKATO/OKTMO, building details, attributes, geotags or other fields?
4. Which Geocoder fields are included by default, and which require extra paid access?
5. Which Suggest types are supported for object, address, street and route-endpoint suggestions?
6. Which identifiers can be used safely across Suggest, Places and Geocoder workflows?
7. Which fields are provider-reported, registry-derived, user-generated, inferred or quality-scored?

## Protocol, Authentication and Key Handling

1. Please confirm production base URLs for Suggest, Places and Geocoder.
2. Are API keys issued and billed separately by product, project or subscription?
3. Can keys be restricted by domain, IP, app, environment, product or method?
4. Are separate credentials available for demo/test and production?
5. How are keys rotated, revoked and monitored?
6. Are method-level permissions available to avoid accidental use of paid on-demand methods?

## Formats, Schemas, Versioning and Errors

1. Are OpenAPI/Swagger specifications available for Suggest, Places and Geocoder?
2. Which request and response formats are officially supported?
3. Please provide sample requests and responses for address suggestions, organization suggestions, place lookup, direct geocoding and reverse geocoding.
4. What error codes and retry guidance apply to validation errors, authentication failures, quota errors, rate limits, no-result responses and provider incidents?
5. How is API versioning handled?
6. What notice period applies to method deprecations, field removals, tariff changes, on-demand field changes and coverage changes?

## Pricing and Billing

1. Please confirm product-specific prices for Suggest, Places and Geocoder.
2. Are charges based on successful requests, units, methods, fields, packages, records, objects or another unit?
3. Which on-demand fields and methods have separate pricing?
4. How are retries, duplicate requests, no-result responses, partial responses, cached results and errors billed?
5. What minimum commitment, setup fee, support fee, SLA fee or On-Premise fee applies?
6. How should a buyer price a workflow where Suggest is used for UI, Places retrieves full objects and Geocoder resolves addresses or coordinates?

## Limits, Quotas and Batch

1. What production per-minute, per-second, burst, concurrency, daily and monthly limits apply to each product?
2. Are limits per key, account, IP, product, method, subscription or contract?
3. Are the public 600 Search units/minute limits negotiable?
4. What demo limits apply to each product?
5. Are batch, asynchronous, offline or warehouse-enrichment use cases allowed?
6. What are the maximum batch size, file size, record count and processing windows if batch is available?

## Storage, Caching, Display and Legal Use

1. Please confirm whether caching is available under any license despite the reviewed WebAPI offer saying caching is not provided.
2. May API responses be stored? If yes, which fields, for how long, and under what refresh rules?
3. May results be displayed to customers, partners, affiliates or SaaS users?
4. Must results be displayed with 2GIS maps, attribution, copyright notices or links?
5. May data be redistributed, resold, exported, embedded in third-party products or used across affiliates?
6. May outputs be used for scoring, model training, analytics, deduplication or address-quality decisions?
7. Which fields contain personal data or regulated information, and what DPA or jurisdiction terms apply?
8. What deletion, audit, attribution and post-termination obligations apply?

## Coverage, Freshness and Quality

1. Which countries, regions and cities are covered for Suggest, Places and Geocoder?
2. What is the update cadence for address, building, organization and place data?
3. What freshness guarantees or expected lag apply?
4. Which quality indicators are available for match level, coordinate precision, address ambiguity and object status?
5. Can 2GIS provide benchmark guidance for Moscow, Saint Petersburg, regional cities, ambiguous addresses, building corpus/structure cases and organization categories?

## SLA, Support and Change Management

1. What uptime SLA, latency SLA, support response SLA and data-freshness SLA are available?
2. Is there a public or customer status page for Search API incidents?
3. What support channels are included by package?
4. What remedies apply for SLA breach?
5. Is there an API changelog, customer notification process, RSS feed, mailing list or portal?
6. What notice period applies for breaking changes and pricing changes?

## Attachments Requested

- Product boundary note for Suggest, Places, Geocoder, Routing and On-Premise.
- Method and field matrix with on-demand fields.
- OpenAPI/Swagger or complete specifications.
- Sample requests and responses.
- Error-code reference and retry guidance.
- Product-specific tariff appendix.
- SLA/support appendix.
- Storage, caching, display, attribution, redistribution, affiliate-use and SaaS terms.
- Changelog, deprecation and breaking-change policy.

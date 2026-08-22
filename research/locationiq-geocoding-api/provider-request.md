# LocationIQ Geocoding API Provider Request Checklist

[Русская версия](provider-request.ru.md)

> Questions for LocationIQ before production selection. This is a checklist, not provider-provided evidence.

## Product Scope

- Confirm which APIs are included in the proposed plan: Search / Forward Geocoding, Reverse Geocoding, Autocomplete, Nearby POI, maps and routing.
- Confirm whether Nearby POI is suitable for the target place-search use case or whether another product/provider is required.
- Confirm whether the Maps Lite plan can be used for the intended geocoding workload.

## Technical Interface

- Provide endpoint list, regions, protocol, authentication model and key restrictions.
- Provide OpenAPI/Swagger, Postman collection or equivalent machine-readable specification.
- Describe response schemas, versioning, error model and deprecation policy.
- Confirm supported response formats for Search, Reverse and Autocomplete.
- Confirm language and country-filter behavior.

## Quality and Coverage

- Describe data sources by country and attribution requirements.
- Provide expected match levels and coordinate precision indicators.
- Explain how `matchquality`, normalized address fields and confidence-like fields should be interpreted.
- Confirm coverage for the target countries and regions.
- Confirm whether house-level data is available in the target regions.

## Limits and Operations

- Confirm production RPS, daily/monthly quotas, burst behavior and HTTP 429 handling.
- Confirm whether rate limits are hard or soft on the proposed plan.
- Confirm monitoring, usage export and alerting options.
- Confirm support hours, incident communication, SLA and uptime commitments.

## Batch and Offline Use

- Confirm whether any asynchronous batch endpoint exists.
- Confirm large-batch processing options, pricing, turnaround time and evidence artifacts.
- Confirm whether concurrent API calls are allowed for the planned batch volume.
- Confirm retry, duplicate request and partial-failure billing.

## Pricing

- Provide method-level pricing or request-credit model.
- Confirm minimum commitment, overage, taxes, currency and invoice terms.
- Confirm whether autocomplete, search, reverse, nearby and maps share the same credits.
- Confirm discounts or custom enterprise terms separately from public pricing.

## Data Rights and Legal

- Confirm storage rights for API output.
- Confirm caching rights for request-response pairs by plan.
- Confirm attribution requirements for Free and paid plans.
- Confirm rights for customer-facing display, SaaS embedding, internal enrichment, redistribution, resale and API proxying.
- Confirm ODbL/OpenStreetMap obligations, derived-database treatment and source attribution requirements.
- Confirm whether results may be used for scoring, model training or quality-improvement datasets.
- Provide DPA/privacy terms for submitted addresses and coordinates.

## Pilot

- Provide test credentials and allowed benchmark scope.
- Confirm synthetic/public test-sample rules.
- Confirm whether benchmark requests count toward commercial limits.
- Confirm how provider corrections or disputed results should be reported.

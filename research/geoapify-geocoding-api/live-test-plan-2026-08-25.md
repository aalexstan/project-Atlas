# Geoapify Live-Test Plan — 2026-08-25

[Русская версия](live-test-plan-2026-08-25.ru.md)

## Status

Pre-registered discovery only. No Geoapify API request was made, no key was created or used, and no live-test result is claimed.

## Official discovery sources

- [Geocoding API](https://www.geoapify.com/geocoding-api/)
- [Forward geocoding docs](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/)
- [Reverse geocoding docs](https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/)
- [Batch docs](https://apidocs.geoapify.com/docs/batch/)
- [Pricing](https://www.geoapify.com/pricing/)
- [Terms](https://www.geoapify.com/terms-and-conditions/)

## Access and legal gate

Before any request, record that a personally registered free-plan API key is used, the accepted terms permit automated single-request testing, the key is not paid, production, shared or customer-owned, and only synthetic or public addresses/coordinates are submitted. Do not store the key, account email or personal data. Do not test batch, bulk, scraping or quota exhaustion in this gate.

If the free-plan terms, Geoapify attribution or OpenStreetMap/ODbL obligations are unclear for the planned test, stop without sending requests.

## Pre-registered core claims

The list is frozen before testing and must not be narrowed after results are seen.

| Dimension | Claim to test | Observation boundary |
|---|---|---|
| Identity/purpose | Geoapify provides hosted forward and reverse geocoding; address autocomplete and Places are related but separate capabilities. | Confirm endpoint identity and response purpose, not quality or worldwide coverage. |
| Response contract | An authenticated single forward request, reverse request and unknown-input request return the documented JSON/result or error shape with coordinates/address fields. | Record HTTP status, content type, selected fields, error shape and latency; redact the key. |
| Rate-limit/policy | The reviewed free plan publishes 3,000 credits/day and up to 5 requests/second, with one credit per geocoding request, and ordinary spaced requests are accepted without approaching exhaustion. | Observe headers/body signals only; do not provoke 429, run batch or measure the quota threshold. |
| Licensing/attribution | Official pricing/terms/response documentation specify required Geoapify and OpenStreetMap attribution and any data-use boundary applicable to the free plan. | Record the required notice or a short compliant excerpt. HTTP success does not prove storage, caching, redistribution or SaaS rights. |

## Planned single-request matrix

1. Forward geocode a public Moscow address.
2. Reverse geocode public Moscow coordinates.
3. Submit an unknown synthetic query and record empty-result or error behavior.
4. Repeat one valid request with a documented language or result-format option, only if allowed by the free plan and terms.

Use a conservative delay between requests. No batch endpoint, bulk import, Places load, autocomplete load, scraping or production-throughput test is allowed.

## Recording and decision rules

Record UTC time, request class without the key, status, latency, content type, selected response fields, rate-limit signals, credit usage if exposed and attribution/license fields. Classify results as `observed`, `provider_reported`, `inferred` or `unknown`. Pricing, SLA, accuracy, house-level precision, storage, caching, redistribution, resale and SaaS remain unknown unless directly evidenced.

This test cannot promote maturity automatically. Add profile `live_tested_on` and `live_test_valid_until` only after human review of raw evidence and the paired review file.

Status: `blocked_pending_legal_access_and_key`.

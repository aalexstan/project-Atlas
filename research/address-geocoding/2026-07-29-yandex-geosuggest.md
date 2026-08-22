# Yandex Geosuggest Research Log

Date: 2026-07-29

## Scope

This log checks whether Yandex Geosuggest is an independent API product for address and organization autocomplete, and how it relates to Yandex Maps Geocoder API, Organization Search and routing products.

## Official Sources Reviewed

- https://yandex.com/maps-api/products/suggest-api
- https://yandex.com/maps-api/docs/suggest-api/request.html
- https://yandex.com/maps-api/docs/suggest-api/response.html
- https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/
- https://yandex.ru/legal/maps_api/ru/

## Confirmed Facts

- Yandex legal terms define `API Geosuggest` as a server-side API service for automated retrieval of search suggestions for geographic objects and/or organizations.
- The documented endpoint is `https://suggest-maps.yandex.ru/v1/suggest`.
- The required request parameters are `apikey` and `text`.
- Authentication uses an API key issued in Yandex developer tooling.
- The response is JSON and contains `results`.
- The documented request supports `lang`, `results`, `ll`, `spn`, `bbox`, `ull`, `strict_bounds`, `countries`, `types`, `print_address`, `org_address_kind` and `attrs`.
- The `results` parameter is capped at 10 suggestions, with a documented default of 7.
- Supported object filters include organization and geographic/address types such as `biz`, `geo`, `street`, `locality`, `house` and `entrance`.
- `attrs=uri` can return a URI that may be used in a Yandex Geocoder API request for additional object information.
- Public tariff pages list annual, monthly and test-period tariffs for Geosuggest in RUB.
- The test period is listed as 100 requests/day for up to 7 days with no minimum payment.
- Yandex legal terms require an API key for API Geosuggest.

## Provider-Reported Claims

- The product page describes Geosuggest as an API for quickly entering and verifying organization names and addresses.
- The product page claims a large address database for Russia and CIS and regularly updated data. Atlas did not independently benchmark coverage or freshness.
- Product material says Geosuggest can be used with Yandex JavaScript API and MapKit to show entered addresses on a map.

## Observations

- Geosuggest is separate from Yandex Maps Geocoder API: Geosuggest returns suggestions, while Geocoder resolves an address/name or coordinate into geocoding results.
- Geosuggest overlaps with organization autocomplete, but it is not the same as a full organization search or directory data API.
- Routing and distance products are outside the Geosuggest product boundary.

## Unknowns

- Public production requests-per-second limit.
- Public SLA and support tiers.
- OpenAPI/Swagger availability.
- Exact paid-license rights for storage, SaaS embedding, redistribution and customer-facing display.
- Whether batch or offline autocomplete-style processing is allowed under a given commercial contract.

## Contradictions

- No direct contradiction was found in official sources, but pricing pages exist in both English/USD product marketing and Russian/RUB tariff documentation. Atlas uses the official Russian tariff page for RUB tariff facts in the Russian-market profile.

## Commercial Blockers

- License choice matters because the tariff page distinguishes Standard and Extended license variants.
- Storage, caching, display and SaaS use require contract review before procurement.
- The public test period is not an Atlas live test.

## Legal and Data-Rights Blockers

- General Maps API terms restrict using service data outside allowed functionality unless commercial terms explicitly allow it.
- Customer-facing display, long-term storage and redistribution must be checked against the exact signed terms.

## Live Testing Status

No Atlas credentialed live test was performed.

## Decision

Create an active API profile for `yandex-maps-geosuggest-api`. Official sources provide a distinct product identity, endpoint, authentication model, request/response documentation and public tariff information. Keep it separate from `yandex-maps-geocoder-api`.

# Yandex Maps Organization Search API Research Log

## Scope

This log checks whether Yandex organization/place search should become an active Atlas API profile in the address and geocoding direction. It separates organization/place search from Geosuggest autocomplete, Geocoder direct/reverse geocoding, and routing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Product page | https://yandex.com/maps-api/products/geosearch-api | Official identity, purpose, pricing positioning |
| API documentation | https://yandex.com/maps-api/docs/geosearch-api/index.html | Product documentation and use cases |
| Request reference | https://yandex.com/maps-api/docs/geosearch-api/request.html | Endpoint, parameters and authentication |
| Response reference | https://yandex.com/maps-api/docs/geosearch-api/response.html | Response structure and formats |
| Commercial terms | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | Pricing and request packages |
| Russian commercial terms | https://yandex.ru/dev/commercial/doc/ru/concepts/geosearch | Cross-check of pricing/license wording |
| FAQ | https://yandex.com/dev/commercial/doc/en/concepts/faq | Trial-key terms and request-counting context |
| Maps API terms | https://yandex.ru/legal/maps_api/ru/ | Legal/data-use context |

## Confirmed Facts

| Fact | Status | Evidence |
|---|---|---|
| Yandex publishes an official product page for organization search / geosearch in the Maps API family. | verified | Product page |
| The API is for searching organizations and geographic objects relevant to a user query/location. | verified | Product page and docs |
| Request access uses an API key passed in the `apikey` parameter. | verified | Request reference |
| The documented request endpoint is `https://search-maps.yandex.ru/v1/`. | verified | Request reference |
| Response format can be JSON by default and XML with `format=xml`. | verified | Request reference |
| Public API documentation lists an API request limit of up to 50 requests/second. | verified | API documentation |
| Official FAQ describes a 14-day trial key by request with a 500 requests/day limit. | provider_reported | FAQ |
| The API is separate from Geosuggest, Geocoder and routing products in Atlas interpretation. | inferred | Product/docs boundaries and existing Yandex profiles |

## Provider-Reported Claims

| Claim | Treatment |
|---|---|
| Product page positions the API as search for organizations and geographic objects. | Treat as verified product purpose because it is official provider documentation. |
| Product page presents basic and data-storage/advanced commercial options. | Treat as provider-reported pricing/license positioning that needs contract review because other commercial-doc wording appears inconsistent. |

## Observations

- This API fills the Yandex-side place/organization search gap in the address/geocoding comparison.
- It should not be treated as address normalization, address cleaning, autocomplete or routing.
- Its commercial fit depends heavily on storage/display/SaaS restrictions and the selected license.

## Unknowns

- Public SLA and support response terms.
- OpenAPI/Swagger availability.
- Exact storage, caching, customer-facing display, SaaS, redistribution and post-termination rights for the selected license.
- Whether all intended fields can be stored or used outside Yandex map display.
- Benchmark quality for target regions, categories and ambiguous organization names.
- Whether high-volume enrichment, batch or offline use is allowed under contract.

## Contradictions

- Reviewed public Yandex pages appear to differ in how they describe Basic/Advanced or storage-capable licenses for organization search. Atlas records this as a contract-review blocker rather than choosing one interpretation.

## Commercial Blockers

- Need quote/contract confirmation for the exact request volume, storage model, SaaS/customer display and any batch/offline use.
- Need clarity on billing of failed, empty, duplicate, retried or cached results.

## Legal and Data-Rights Blockers

- Storage, caching, display, redistribution, affiliate use, SaaS embedding and model-training rights need legal/contract review.
- Map-display coupling and attribution obligations must be checked for the actual product UI.

## Live Testing Status

No Atlas credentialed request, benchmark or live API test was performed.

## Profile Decision

Create an active reviewed profile `yandex-maps-organization-search-api`. Include it in the address/geocoding comparison as an organization/place search candidate, not as a geocoder, autocomplete API, routing API or registry validation source.

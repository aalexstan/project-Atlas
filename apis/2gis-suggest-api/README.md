# 2GIS Suggest API

[Русская версия](README.ru.md)

> 2GIS Search API product for autocomplete suggestions in map and catalog search interfaces.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | 2GIS |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** autocomplete UX in products using 2GIS Search, especially when suggestions should connect to 2GIS catalog objects, addresses, streets or route endpoints.

**Avoid when:** you need direct/reverse geocoding, full organization records, registry-quality address validation, offline enrichment, or storage without contract confirmation.

**Bottom line:** Suggest API is a separate 2GIS Search product. It should be evaluated alongside [`2GIS Places API`](../2gis-places-api/README.md) and [`2GIS Geocoder API`](../2gis-geocoder-api/README.md), not merged into them.

## Product Boundary

This profile covers:

- suggestions while a user enters a query;
- object suggestions for catalog-driven search;
- address and street suggestions through `suggest_type`;
- route-endpoint suggestions as a related UI helper.

This profile does not cover:

- resolving an address to coordinates or coordinates to an address;
- retrieving full organization/place records after a suggestion;
- route building;
- official Russian registry ownership.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Search-box autocomplete in a 2GIS UI | Strong | Official docs describe Suggest as the tool for completing user input. |
| Address suggestions | Medium | `suggest_type=address` and `suggest_type=street` are documented. |
| Organization/place suggestions | Medium | Object suggestions can be paired with Places API for full objects. |
| Direct/reverse geocoding | Weak | Use 2GIS Geocoder API. |
| Bulk processing | Weak | Suggest semantics and rights are user-input oriented; batch is not confirmed. |
| Routing | Not applicable | Route calculation is outside Suggest API. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Example endpoint | `https://catalog.api.2gis.com/3.0/items` |
| Required access | API key |
| Example parameters | `q`, `location`, `key` |
| Response format | JSON |
| Default suggestion type | `object` |
| Documented suggestion types | `object`, `address`, `street`, `route_endpoint` |
| OpenAPI / Swagger | Not found in reviewed public docs |
| Deployment | Cloud public endpoints; provider-reported On-Premise availability for current methods |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Pricing model | Successful requests / monthly units | verified |
| Public price floor | 7,000 RUB for 100,000 Suggest API units/month | verified |
| Per-minute limit | 600 Search units/minute | verified |
| Demo limit | 1,000 total Search-service requests for Suggest API | verified |
| Demo period | One month demo key | verified |
| Directory freshness | Monthly update claim for 2GIS directory | provider_reported |
| Caching | WebAPI offer says caching is not provided | verified |
| SLA | Not found publicly in this research | unknown |

## Commercial and Legal Notes

- Suggest API and Places API have different tariff rows; price them separately.
- The 2GIS WebAPI offer restricts extraction, storage, processing, modification and distribution outside contract terms.
- Caching is explicitly not provided in the reviewed WebAPI offer.
- Use of suggestions in SaaS products, customer-facing display and redistribution needs contract review.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`2GIS Places API`](../2gis-places-api/README.md) | You need full organization, building or place search results | Different pricing and on-demand fields. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | You need address-to-coordinate or coordinate-to-address conversion | Not an autocomplete API. |
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address entry and cleaning are the core task | Less tied to 2GIS catalog workflows. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.md) | The map ecosystem is Yandex | Yandex licensing and display requirements apply. |

## Scenario-Based Recommendation

Use 2GIS Suggest when the user input flow should feed a 2GIS search/catalog experience. For address cleaning, geocoding, full place records and routing, select the corresponding separate product and confirm data rights.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

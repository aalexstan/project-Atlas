# Yandex Maps Organization Search API

[Русская версия](README.ru.md)

> Yandex Maps API product for searching organizations, places and geographic objects.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Yandex |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** Yandex Maps-centered organization/place search, business-directory search near a location, and workflows that need Yandex search results rather than only address-to-coordinate geocoding.

**Avoid when:** you need address normalization, address autocomplete, registry-quality address validation, routing, offline/bulk enrichment without explicit rights, or a provider-neutral places dataset.

**Bottom line:** Yandex Organization Search closes the Yandex-side place-search gap in Atlas. It should be compared with [`2GIS Places API`](../2gis-places-api/README.md), not with address-cleaning or official registry feeds.

## Product Boundary

This profile covers:

- organization search;
- place/geographic-object search;
- Yandex Maps search results returned through the Search/Geosearch API;
- relationship with Yandex map display and Yandex commercial terms.

This profile does not cover:

- address suggestions, covered by [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.md);
- direct/reverse geocoding, covered by [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md);
- routing, route optimization or distance matrices;
- official Russian address registry validation.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Organization search in a Yandex Maps UI | Strong | Official docs/product pages identify organization and geographic-object search as the purpose. |
| Local business/place discovery near a point | Strong | Request parameters support text, coordinates and search-area constraints. |
| Address autocomplete | Weak | Use Geosuggest instead. |
| Address-to-coordinate geocoding | Weak | Use Yandex Geocoder instead. |
| Organization enrichment at scale | Medium/unknown | Commercial rights, storage and batch/offline use need contract confirmation. |
| Registry-quality validation | Weak | Search results are not official registry validation. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Endpoint | `https://search-maps.yandex.ru/v1/` |
| Required parameters | `apikey`, `text`, `lang` |
| Authentication | API key in `apikey` query parameter |
| Response format | JSON by default; XML with `format=xml` |
| Common filters | `ll`, `spn`, `bbox`, `rspn`, `type`, `results`, `skip`, `uri` |
| Request language | `lang` parameter |
| OpenAPI / Swagger | Not found in reviewed public docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Public commercial terms | Request packages are published | verified |
| Annual Basic license | From 195,000 RUB for 1,000 requests/day in reviewed commercial terms | verified |
| Monthly Basic license | From 20,800 RUB for 1,000 requests/day in reviewed commercial terms | verified |
| API request limit | Up to 50 requests/second in reviewed public documentation | verified |
| Trial | 14-day trial key by request with 500 requests/day limit according to official FAQ | provider_reported |
| License/storage wording | Public pages appear inconsistent between Basic/Advanced or storage-capable descriptions | needs_contract_review |
| Public SLA | Not found publicly in this research | unknown |

## Commercial and Legal Notes

- Treat storage, caching, customer-facing display, third-party map display, SaaS embedding, redistribution, resale, affiliate use and model-training rights as contract blockers.
- Do not use a map-display or web-product price as a substitute for the Search API commercial terms.
- Because reviewed official pages appear to differ in license/storage wording, procurement should request a written tariff and rights appendix for the selected scenario.
- Bulk/offline enrichment is not confirmed by public docs reviewed here.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`2GIS Places API`](../2gis-places-api/README.md) | 2GIS directory context, buildings and places are central | 2GIS storage/caching rights and on-demand fields need review. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.md) | You need autocomplete before a user selects a result | It is suggestions, not full organization search. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | You need address/coordinate conversion | It is not a place-search API. |
| [`DaData API`](../dadata/README.md) | Russian company details by INN/OGRN are the task | Different data model from map place search. |

## Scenario-Based Recommendation

Shortlist Yandex Organization Search when the user-facing product already uses Yandex Maps and needs organizations or places. Compare against 2GIS Places API when directory depth, field availability, storage rights and local-market coverage matter.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

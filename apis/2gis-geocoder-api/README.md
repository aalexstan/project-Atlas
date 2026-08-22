# 2GIS Geocoder API

[Русская версия](README.ru.md)

> Direct and reverse geocoding API within the 2GIS Search API family.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | 2GIS |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** products already built around 2GIS maps/catalog data, map-click reverse geocoding, and geocoding where public package pricing is useful.

**Avoid when:** the task is registry-quality address normalization, organization search through a geocoder, unrestricted offline storage, or bulk enrichment without contract confirmation.

**Bottom line:** 2GIS Geocoder is a documented HTTP JSON geocoder with public package prices and demo-key access. It should not be stretched to cover 2GIS Places or Suggest without explicitly buying and evaluating those separate products.

## Product Boundary

This profile covers:

- direct geocoding by address/name;
- reverse geocoding by coordinates;
- 2GIS Geocoder API request/response model.

Related but separate:

- [`2GIS Places API`](../2gis-places-api/README.md) searches organizations, buildings and places;
- [`2GIS Suggest API`](../2gis-suggest-api/README.md) provides input suggestions;
- navigation APIs handle routing, matrices and isochrones.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Show a known address on a 2GIS map | Strong | Direct geocoding is a core Geocoder API use case. |
| Address from map click | Strong | Reverse geocoding by coordinates is documented. |
| Product already using 2GIS Platform | Strong | Same Platform Manager/key/subscription model. |
| Organization/place search | Medium only with Places API | Geocoder itself is not the directory search product. |
| Address autocomplete | Medium only with Suggest API | Suggest is a separate service. |
| Official Russian address registry validation | Weak | Geocoder matching is not the same as GAR validation. |
| Offline database enrichment | Weak until contracted | Storage/caching rights are contract-sensitive. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Endpoint | `https://catalog.api.2gis.com/3.0/items/geocode` |
| Authentication | API key in `key` query parameter |
| Direct request | `q=<address>` |
| Reverse request | `lat=<latitude>&lon=<longitude>` |
| Response format | JSON |
| API reference | Public documentation exists |
| OpenAPI / Swagger | Not found in reviewed public docs |
| Deployment | Cloud public endpoints; provider reports On-Premise option with caveats |

## Pricing and Limits

| Item | Confirmed value | Status |
|---|---|---|
| Demo key | Available for one month | verified |
| Demo Search limit | 1,000 total Search-service requests | verified |
| Geocoder package 10,000 units/month | 4,700 RUB | verified |
| Geocoder package 100,000 units/month | 21,000 RUB | verified |
| Geocoder package 1,000,000 units/month | 70,000 RUB | verified |
| Search services rate limit | 600 units/minute | verified |
| Billing unit | Successful API requests | verified |
| Public SLA | Not found in reviewed docs | unknown |

Some fields, including selected FIAS/FNS/OKATO/OKTMO and building details, are documented as on-demand paid access.

## Commercial and Legal Notes

- The official Search overview says some object information is available only on demand and for extra cost.
- The WebAPI offer makes storage, caching, modification, distribution and use outside the contract a procurement blocker.
- The 2GIS directory is updated monthly according to provider documentation; Atlas has not independently measured freshness.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address suggestions and cleaning are central | Direct geocoding is pay-per-record and Russia-focused. |
| [`2GIS Suggest API`](../2gis-suggest-api/README.md) | Need 2GIS-powered autocomplete before geocoding or place lookup | Suggestions are not geocoding. |
| [`2GIS Places API`](../2gis-places-api/README.md) | Need organizations, buildings and places | Place search is not address validation. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Product is based on Yandex Maps display and licensing | Free use is tightly bound to Yandex Maps display. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | Own official Russian address base is required | Requires ETL/search infrastructure and is not a turnkey geocoder. |

## Scenario-Based Recommendation

Choose 2GIS Geocoder when the application is already using 2GIS maps or catalog data and geocoding is part of that map workflow. If the need includes organization search, address suggestions or routing, evaluate the corresponding 2GIS product separately.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

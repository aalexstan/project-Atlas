# Yandex Maps Geocoder API

[Русская версия](README.ru.md)

> Direct and reverse geocoding API for Yandex Maps-centered products.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Yandex |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** applications that need address-to-coordinate or coordinate-to-address conversion and can comply with Yandex Maps display, storage and licensing terms.

**Avoid when:** the task is address normalization, registry-quality address validation, organization search, address autocomplete, routing, or offline/bulk enrichment without explicit commercial rights.

**Bottom line:** Yandex Maps Geocoder is a real, documented geocoding API with public tariffs and clear free-use constraints. It should be compared as a geocoder, not as a complete address cleaning or registry product.

## Product Boundary

Yandex Geocoder covers:

- forward geocoding: address/name -> coordinates;
- reverse geocoding: coordinates -> address;
- geocoder response metadata and precision fields.

It does not cover in this profile:

- address autocomplete, which belongs to Yandex Geosuggest;
- organization/place search, which belongs to separate Yandex search products;
- routing, route optimization or distance matrix.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Show a known address on a Yandex map | Strong | Direct geocoding is the core documented use case. |
| Find the address closest to a selected map point | Strong | Reverse geocoding is explicitly documented. |
| Commercial map product with licensed storage rights | Medium | Paid tariffs include Standard and Extended license options; exact contract must be reviewed. |
| Address normalization before CRM import | Weak | Geocoder returns geocoding metadata, not full cleaning/standardization workflow. |
| Registry-quality validation | Weak | Geocoder precision is not the same as official address registry validation. |
| Organization/place search | Not in scope | Use separate Yandex search products. |
| Routing | Not in scope | Routing APIs are separate. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Endpoint | `https://geocode-maps.yandex.ru/v1` |
| Required parameters | `apikey`, `geocode`, `lang` |
| Authentication | API key in `apikey` query parameter |
| Response format | JSON |
| Direct geocoding | Address/name in `geocode` |
| Reverse geocoding | Coordinates in `geocode`; optional `kind` |
| Result count | Default 10, maximum 50 |
| Error examples | 400, 403, 429 |
| TLS requirement | Client systems must support SNI |
| OpenAPI / Swagger | Not found in reviewed public docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Free-use Geocoder limit | 1,000 requests/day | verified |
| Free-use display restriction | Only with Yandex Maps JavaScript API / Yandex map display; third-party map display prohibited | verified |
| Test period | 100 requests/day for up to 7 days | verified |
| Annual Standard license | From 195,000 RUB for 1,000 requests/day | verified |
| Annual Extended license with data storage | From 226,200 RUB for 1,000 requests/day | verified |
| Monthly Standard license | From 20,800 RUB for 1,000 requests/day | verified |
| Over 1,000,000 requests/day | Quote required | verified |
| Requests per second | Not found publicly in this research | unknown |
| SLA | Not found publicly in this research | unknown |

## Commercial and Legal Notes

- Free-use terms tie Geocoder to Yandex Maps display and prohibit displaying results on third-party maps.
- General Maps API terms restrict storage, processing and modification of service data except limited temporary caching unless otherwise agreed.
- The tariff page distinguishes Standard and Extended license variants; storage rights should be confirmed in the signed agreement.
- Bulk/offline geocoding, SaaS embedding and redistribution need explicit commercial confirmation.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address suggestions and backend standardization are required | Russia-focused depth; direct geocoding is per-record. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | Product is built around 2GIS map/catalog data | Places and Suggest are separate products; caching restrictions need review. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | The goal is a proprietary official Russian address base | Requires ETL and search/index infrastructure. |

## Scenario-Based Recommendation

Choose Yandex Geocoder when geocoding is naturally tied to Yandex Maps display and the license matches your storage/display model. Choose a normalization API or registry integration when the problem is address quality, canonical fields or long-term address data ownership.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

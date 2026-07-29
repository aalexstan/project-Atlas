# OpenCage Geocoding API

[Русская версия](README.ru.md)

> Hosted commercial geocoding API for worldwide forward and reverse geocoding based on open data.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | OpenCage GmbH |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** teams that want a hosted international geocoder, public API pricing, API-key access, permanent storage-friendly wording and a commercial alternative to public or self-hosted Nominatim.

**Avoid when:** you need Russian registry validation, address cleaning/normalization, fuzzy autocomplete, routing, or a batch API that accepts many locations in one request.

**Bottom line:** OpenCage is a strong additional hosted open-data geocoding candidate for the address/geocoding comparison. It should be evaluated against Geoapify, Yandex, 2GIS, DaData and self-hosted Nominatim by geography, precision, rights, ODbL/attribution obligations, SLA and benchmark quality.

## Product Boundary

This profile covers:

- forward geocoding;
- reverse geocoding;
- public pricing, limits, storage wording and open-data source/credit notes;
- OpenAPI availability as documented by OpenCage.

This profile does not cover:

- OpenCage Geosearch/autosuggest as a separate product;
- Russian GAR/FIAS registry validation;
- address cleaning or canonicalization;
- routing, matrices or distance calculations;
- legal advice on ODbL, attribution or derived databases.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| International forward/reverse geocoding | Strong | Official docs describe worldwide geocoding over REST. |
| Hosted open-data geocoding | Strong | Official credits list OpenStreetMap and other open-data sources. |
| Permanent storage of API results | Strong but legal review needed | Provider docs say API results can be stored permanently; users still accept data-license responsibility. |
| Large batch geocoding | Medium | API is one location per request; spreadsheets and parallel requests are documented routes. |
| Address autocomplete | Weak in this profile | Provider says autosuggest belongs to Geosearch, not Geocoding API. |
| Official registry validation | Weak | Not an official registry route. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Endpoint pattern | `https://api.opencagedata.com/geocode/v1/{format}` |
| Authentication | API key in `key` query parameter |
| Required query | `q` as address/placename or latitude, longitude |
| Response formats | JSON, GeoJSON, XML and Google-compatible JSON |
| Coordinate system | WGS 84 / EPSG:4326 |
| OpenAPI | OpenAPI specification link present in official docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Free trial | 2,500 requests/day; 1 request/second; testing only; no credit card | verified |
| Monthly paid examples | X-Small `zł 205/mo`, Small `zł 510/mo`, Medium `zł 2050/mo`, Large `zł 4100/mo` in reviewed pricing page | verified |
| Enterprise | from `zł 8200/mo`; custom limits, pricing, terms and SLAs | verified |
| Paid RPS examples | 15, 20, 25 and 40 requests/second by plan | verified |
| Paid daily request examples | 10,000, 30,000, 125,000 and 300,000 requests/day by plan | verified |
| Batch/bulk API | Multiple locations per API request are not supported | verified |
| Spreadsheet upload | Supported; free trial limited to 100 rows; paying customers can upload larger files | verified |
| Storage/caching | Provider says results can be stored permanently | provider_reported |
| Data licenses | Users must respect returned data licenses, especially OSM ODbL | verified |

## Commercial and Legal Notes

- Treat ODbL, attribution, derived databases, redistribution, resale, SaaS embedding, API proxying and customer-facing display as legal/procurement review topics.
- Public pricing in this pass was shown in `zł`; Atlas does not convert currencies or infer negotiated pricing.
- Geocoding API is not fuzzy autocomplete. OpenCage points autocomplete/typeahead use cases to Geosearch.
- One-location-per-request makes high-volume workloads possible through parallelization, but it changes engineering and audit design compared with asynchronous batch APIs.
- No live benchmark was run for target countries, languages, house-level precision or latency.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`Geoapify Geocoding API`](../geoapify-geocoding-api/README.md) | You need hosted open-data geocoding with asynchronous batch jobs | ODbL/attribution and batch failure semantics still need review. |
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.md) | You want self-hosted OSM geocoding control | You own import, updates, operations and ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Yandex Maps display and Russia/CIS ecosystem are central | Storage/display rights and map coupling need review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | 2GIS map/catalog workflows are central | Caching/storage rights and field access need review. |
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address cleaning and GAR/FIAS-linked fields matter | Russia-focused and not an international open-data geocoder. |

## Scenario-Based Recommendation

Shortlist OpenCage when the scenario needs hosted international open-data geocoding, permanent storage-friendly public wording and a simple GET API. Do not treat it as an address-cleaning, autocomplete, routing or registry-validation product.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

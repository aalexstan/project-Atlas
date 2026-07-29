# Nominatim Geocoder Software

[Русская версия](README.ru.md)

> Open-source geocoder software and OpenStreetMap data route for search and reverse geocoding.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Nominatim project / OpenStreetMap ecosystem |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** teams that need an open-data geocoder and can operate their own Nominatim instance, OSM imports, updates, monitoring and license compliance.

**Avoid when:** you need a no-ops hosted SLA API, autocomplete on the public OSMF service, high-volume public-instance usage, address normalization, or official Russian registry validation.

**Bottom line:** Nominatim should not be treated as a free production geocoding API. Atlas models it as `open_source_geocoder_software`: useful, mature and important, but operationally and legally different from hosted commercial APIs.

## Product Boundary

This profile separates three routes:

- public `nominatim.openstreetmap.org`: limited use under the OSMF usage policy;
- self-hosted Nominatim: software operated by the user on OSM data;
- commercial third-party providers: separate procurement route, not evaluated in this profile.

This profile covers:

- free-form and structured search;
- reverse geocoding;
- OpenStreetMap attribution and ODbL obligations;
- self-hosting import/update considerations.

This profile does not cover:

- public-service autocomplete;
- hosted SLA from OSMF;
- commercial providers' terms;
- routing;
- registry-quality Russian address validation.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Self-hosted geocoding on OSM data | Strong | Official docs cover import and update operations. |
| Limited end-user-triggered public search | Medium | Public service policy permits moderate direct user-triggered use under strict limits. |
| Bulk geocoding on public service | Weak | Public policy discourages bulk and imposes strict limits. |
| Autocomplete on public service | Not allowed | Public policy forbids autocomplete search. |
| Hosted commercial SLA | Not applicable | Evaluate a third-party provider separately. |
| Russian official address registry | Weak | OSM is not GAR/FIAS. |

## Technical Access

| Field | Public OSMF service | Self-hosted Nominatim |
|---|---|---|
| Search endpoint | `https://nominatim.openstreetmap.org/search?<params>` | Operator-defined |
| Reverse endpoint | `https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>` | Operator-defined |
| Authentication | No API key; valid Referer/User-Agent required | Operator-defined |
| Search input | Free-form or structured query | Same software API |
| Reverse input | WGS84 latitude/longitude | Same software API |
| Output formats | XML, JSON, JSONv2, GeoJSON, GeocodeJSON | Same software API |
| Search result limit | Default 10, maximum 40 | Config/operation dependent |
| OpenAPI / Swagger | Not found in reviewed docs | Not found in reviewed docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Public service monetary price | No fee stated in policy | verified_context |
| Public service max rate | Absolute maximum 1 request/second | verified |
| Public autocomplete | Forbidden by usage policy | verified |
| Public bulk geocoding | Larger bulk discouraged; regular/long scripts restricted | verified |
| Public resale/API proxying | Primary geocoding apps and API resellers must run own service | verified |
| Attribution | Required | verified |
| Data license | ODbL | verified |
| Self-hosting cost | Infrastructure and operations, not API subscription | inferred |
| SLA | No public OSMF SLA found | unknown |

## Commercial and Legal Notes

- Public Nominatim is not a production substitute for a paid geocoder when the product's primary function is geocoding.
- Public policy requires identifiable clients and attribution.
- OSM data is ODbL; derived databases, caches and SaaS use require legal review.
- The public policy asks users not to submit personal or confidential data to OSMF services.
- Self-hosting requires import, database storage, updates, monitoring, backups and capacity planning.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | You need a hosted commercial geocoder tied to Yandex Maps | Storage/display restrictions and tariffs apply. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | You need hosted geocoding in 2GIS workflows | Caching/storage rights need contract review. |
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address cleaning and registry identifiers matter | Russia-focused; not an open-data global geocoder. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | Official Russian address provenance is mandatory | Requires own ETL/search and does not provide general geocoding. |

## Scenario-Based Recommendation

Choose self-hosted Nominatim when open data, operational ownership and international OSM coverage matter more than managed SLA. Use public `nominatim.openstreetmap.org` only within its policy. For production autocomplete or high-volume geocoding, use self-hosting or a commercial provider.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

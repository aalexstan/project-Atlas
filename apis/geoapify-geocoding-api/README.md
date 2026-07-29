# Geoapify Geocoding API

[Русская версия](README.ru.md)

> Hosted commercial geocoding API for worldwide forward/reverse geocoding, batch geocoding and address autocomplete in the Geoapify Location Platform.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Geoapify |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** teams that want a hosted international geocoder with public pricing, API-key access, batch geocoding, published rate limits, storage-friendly positioning and an SLA on paid plans.

**Avoid when:** you need official Russian address registry validation, provider-neutral legal certainty without ODbL/attribution review, a self-hosted open-source stack, or a Russia-specific address cleaning API.

**Bottom line:** Geoapify is a credible hosted open-data geocoding route for the address/geocoding comparison. It should be evaluated against Yandex, 2GIS, DaData and self-hosted Nominatim by geography, precision, legal rights, attribution, SLA and benchmark quality.

## Product Boundary

This profile covers:

- forward geocoding;
- reverse geocoding;
- batch geocoding;
- public pricing, limits and attribution/SLA terms.

This profile does not cover:

- official Russian registry validation;
- route planning, matrices or isochrones;
- Places API or Place Details API as a separate place-search product;
- self-hosted Nominatim operations;
- legal advice on ODbL or derived databases.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| International forward/reverse geocoding | Strong | Official docs describe worldwide address search and coordinate-to-address lookup. |
| Batch geocoding | Strong | Official docs describe asynchronous batch jobs with up to 1,000 inputs. |
| Hosted open-data geocoding | Strong | Provider says results can be stored with attribution; legal review is still required. |
| Russian address cleaning | Weak | Not a Russia-specific cleaning/normalization API. |
| Official GAR/FIAS validation | Weak | Not an official registry route. |
| Self-hosted open-source control | Weak | Use Nominatim self-hosting route instead. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET for forward/reverse geocoding; HTTP POST/GET for batch jobs |
| Forward endpoint | `https://api.geoapify.com/v1/geocode/search` |
| Reverse endpoint | `https://api.geoapify.com/v1/geocode/reverse` |
| Batch endpoint | `https://api.geoapify.com/v1/batch` |
| Authentication | API key in `apiKey` parameter |
| Response formats | JSON, GeoJSON and XML in reviewed docs |
| Forward inputs | Free-form or structured address parameters |
| Reverse inputs | `lat` and `lon` |
| OpenAPI | Download OpenAPI link present in reviewed docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Free plan | 3,000 credits/day; limited commercial use; up to 5 requests/second | verified |
| Paid monthly plan examples | API 10: $59/month for 10,000 credits/day; API 250: $609/month for 250,000 credits/day | verified |
| Geocoding credit cost | 1 Geocoding, Reverse Geocoding or Address Autocomplete request = 1 credit | verified |
| Standard plan rate limit | Up to 30 requests/second for Geocoding API requests depending on plan | verified |
| Dedicated geocoding capacity | Dedicated server example up to 50 Geocoding API calls/second | provider_reported |
| Batch | Asynchronous; up to 1,000 inputs; job results available for 24 hours | verified |
| SLA | Paid plans include default 99.5% monthly availability SLA in reviewed terms/pricing FAQ | verified |
| Storage | Provider says storage is not restricted, but attribution must be preserved | provider_reported |
| Attribution | OpenStreetMap attribution required; Geoapify attribution mandatory on Free plan | verified |
| Taxes | Prices exclude taxes and fees | verified |

## Commercial and Legal Notes

- Treat ODbL, OpenStreetMap attribution, derived databases, cache sharing, resale, SaaS embedding and customer-facing display as legal/procurement review topics.
- Provider wording is favorable to storing results, but Atlas has not performed a legal review.
- Free-plan commercial use is allowed with limitations and attribution; production use should confirm plan terms.
- Batch geocoding reduces cost but is asynchronous and the result availability window matters operationally.
- No live benchmark was run for target countries, regions, house-level precision or latency.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.md) | You want self-hosted OSM geocoding control | You own import, updates, operations and ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Yandex Maps display and Russia/CIS map ecosystem are central | Storage/display rights and map coupling need review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | 2GIS map/catalog workflows are central | Caching/storage rights and field access need review. |
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address cleaning and GAR/FIAS-linked fields matter | Russia-focused and not an international open-data geocoder. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | Official Russian address registry provenance is mandatory | Requires internal ETL/search and does not provide global geocoding. |

## Scenario-Based Recommendation

Shortlist Geoapify when the scenario needs hosted international geocoding, batch processing and storage-friendly open-data terms. Do not treat it as a Russian registry validation product or as legal proof that every derived database/SaaS use is safe.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

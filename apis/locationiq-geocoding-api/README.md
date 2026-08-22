# LocationIQ Geocoding API

[Русская версия](README.ru.md)

> Hosted commercial geocoding and autocomplete API suite for forward geocoding, reverse geocoding, address autocomplete and nearby POI lookup.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Unwired Labs / LocationIQ |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** teams that want a hosted commercial route for international forward/reverse geocoding and address autocomplete, with public pricing, access-token authentication, documented US/EU geocoding endpoints and provider-published storage/caching guidance.

**Avoid when:** you need Russian registry validation, DaData-style address cleaning, an official GAR/FIAS source, a multi-address batch API call, routing as the primary task, or production rights without reviewing attribution, storage, SaaS and redistribution terms.

**Bottom line:** LocationIQ is a credible additional hosted open-data/commercial geocoding candidate next to Geoapify and OpenCage. It should be compared by precision, geography, data rights, caching model, attribution, SLA, batch design and legal treatment of derived data.

## Product Boundary

This profile covers:

- Search / Forward Geocoding;
- Reverse Geocoding;
- Autocomplete;
- Nearby POI as a related capability, not a full directory replacement;
- public pricing, quotas, rate limits, caching and batch boundaries.

This profile does not cover:

- routing APIs, matrices, map matching or route optimization;
- registry-quality address validation;
- Russia-specific address cleaning or canonicalization;
- public Nominatim, self-hosted Nominatim or other LocationIQ-hosted alternatives;
- legal advice on OpenStreetMap/ODbL, attribution, derived databases or redistribution.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| International forward geocoding | Strong | Official docs define Search / Forward Geocoding and list US/EU endpoint patterns. |
| International reverse geocoding | Strong | Official docs define Reverse Geocoding and list required `lat`, `lon` and `key` parameters. |
| Address autocomplete | Strong | Official docs expose a separate `/v1/autocomplete` endpoint for type-ahead suggestions. |
| Nearby POI lookup | Medium | Official docs list Nearby POI, but this profile does not treat it as a full organization/catalog search replacement. |
| Batch geocoding | Medium/weak | Provider support says one address per request; concurrent calls are allowed within plan limits. |
| Official Russian registry validation | Weak | Not an official FIAS/GAR route and not an address-cleaning profile. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Forward geocoding endpoints | `https://us1.locationiq.com/v1/search` and `https://eu1.locationiq.com/v1/search` |
| Reverse geocoding endpoints | `https://us1.locationiq.com/v1/reverse` and `https://eu1.locationiq.com/v1/reverse` |
| Autocomplete endpoint | `https://api.locationiq.com/v1/autocomplete` |
| Authentication | Access token / API key in `key` query parameter |
| Request formats | Query parameters; free-form, structured and postal-code forms for Search |
| Response formats | JSON, XML and `xmlv1.1` for geocoding docs; Autocomplete examples use JSON |
| API reference | Public API Reference and Postman collection are documented |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Free plan | 5,000 requests/day; 2 requests/second; 60 requests/minute; limited commercial use with attribution | verified |
| Developer plan example | USD 100/month; 25,000 requests/day; 20 requests/second | verified |
| Startup plan example | USD 200/month; 60,000 requests/day; 22 requests/second | verified |
| Growth Plus example | USD 500/month; 7.5 million requests/month; 30 requests/second | verified |
| Business Plus example | USD 950/month; 30 million requests/month; 40 requests/second | verified |
| Enterprise | Custom pricing, custom request rates, custom contract and SLAs | provider_reported |
| Batch API | No multi-address request; each address is a separate request | verified |
| CSV/bulk service | Provider says large batch processing may be arranged for a fee | provider_reported |
| Storage | Provider help says API output can be stored forever | provider_reported |
| Caching | Free plan caching up to 48 hours; customers can cache while subscribed | provider_reported |

## Commercial and Legal Notes

- Public plan prices are not enterprise quotes.
- LocationIQ documentation and examples include OpenStreetMap-compatible concepts and attribution fields; ODbL/attribution and derived-database implications still need legal review.
- Free-plan commercial use is tied to attribution wording on the pricing page and terms review.
- Caching and storage wording should be checked against the exact account tier, SaaS data flow and customer-facing display model.
- The public terms include warranty disclaimers and do not replace SLA/contract review.
- No Atlas benchmark was run for house-level precision, latency, false positives or target-country quality.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`Geoapify Geocoding API`](../geoapify-geocoding-api/README.md) | You need a documented hosted batch geocoding route | Batch failure semantics, ODbL/legal and benchmark review still matter. |
| [`OpenCage Geocoding API`](../opencage-geocoding-api/README.md) | Permanent storage-friendly wording and a geocoding-only API are central | Autocomplete is separate and high-volume design still needs review. |
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.md) | You want self-hosted OSM geocoding control | You own import, updates, operations and ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Yandex Maps display and Russia/CIS ecosystem are central | Storage/display rights and map coupling need review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | 2GIS map/catalog workflows are central | Caching/storage rights and field access need review. |
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address cleaning and GAR/FIAS-linked fields matter | Russia-focused and not an international open-data geocoder. |

## Scenario-Based Recommendation

Shortlist LocationIQ when the scenario needs hosted forward/reverse geocoding or autocomplete with public plan limits and a managed commercial API. Do not treat it as an official registry, address-cleaning tool or unrestricted free production Nominatim replacement.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

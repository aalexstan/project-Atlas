# Yandex Maps Geosuggest API

[Русская версия](README.ru.md)

> Server-side API for address, geographic-object and organization suggestions in Yandex Maps workflows.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Yandex |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** user-facing address and organization autocomplete when the product is already aligned with Yandex Maps licensing and display requirements.

**Avoid when:** you need backend address normalization, registry-quality validation, direct/reverse geocoding without a separate Geocoder call, routing, or bulk/offline enrichment.

**Bottom line:** Geosuggest is a separate Yandex Maps API product. Treat it as an autocomplete and suggestion layer, not as a replacement for [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) or a full address-cleaning API.

## Product Boundary

This profile covers:

- suggestions for address fragments and geographic objects;
- organization-name suggestions where supported by Geosuggest;
- optional result scoping by location, bounding box, country and object type;
- follow-up relationship with Geocoder API through a returned `uri`.

This profile does not cover:

- direct and reverse geocoding;
- full organization search or directory enrichment;
- routing and matrix APIs;
- registry-quality Russian address normalization.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Address suggestions in a Yandex Maps product | Strong | Official docs define Geosuggest as a dedicated suggestion API. |
| Organization-name autocomplete | Medium | Geosuggest supports organization-related suggestions, but full directory search is a separate product. |
| Follow-up geocoding after selection | Medium | `attrs=uri` can return a URI for use with the Geocoder API. |
| Backend address cleaning | Weak | No cleaning/standardization workflow is documented for Geosuggest. |
| Bulk enrichment | Weak | Autocomplete semantics and licensing need explicit confirmation. |
| Routing | Not applicable | Routing is a separate Yandex Maps API family. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| Endpoint | `https://suggest-maps.yandex.ru/v1/suggest` |
| Required parameters | `apikey`, `text` |
| Authentication | API key in `apikey` query parameter |
| Response format | JSON |
| Default result count | 7 |
| Maximum result count | 10 |
| Main filters | `lang`, `ll`, `spn`, `bbox`, `countries`, `types`, `strict_bounds` |
| Object type filters | `biz`, `geo`, `street`, `metro`, `district`, `locality`, `area`, `province`, `country`, `house`, `entrance` |
| OpenAPI / Swagger | Not found in reviewed public docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Public tariffs | RUB tariffs published for annual and monthly Geosuggest licenses | verified |
| Annual Standard license | From 180,000 RUB for 10,000 requests/day | verified |
| Annual Extended license with data storage | From 208,800 RUB for 10,000 requests/day | verified |
| Monthly Standard license | From 19,200 RUB for 10,000 requests/day | verified |
| Test period | 100 requests/day for up to 7 days | verified |
| Free-use terms | Geosuggest appears in Yandex Maps API terms; exact free/commercial fit depends on scenario | needs_contract_review |
| Requests per second | Not found publicly in this research | unknown |
| SLA | Not found publicly in this research | unknown |

## Commercial and Legal Notes

- The tariff page distinguishes Standard and Extended licenses; storage rights should be checked in the chosen license.
- General Yandex Maps API terms apply to API keys and service-data use.
- Customer-facing display, storage, caching, SaaS embedding and redistribution require contract review.
- Do not use Geosuggest as proof that a separate Yandex organization-search or routing product is included.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`DaData Address APIs`](../dadata-address-api/README.md) | Russian address forms and backend normalization are the primary task | Russia-focused; endpoint billing differs by capability. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | A selected address/name must be resolved to coordinates or an address from coordinates | It is not an autocomplete API. |
| [`2GIS Suggest API`](../2gis-suggest-api/README.md) | The UI is built around 2GIS search/catalog workflows | Storage/caching rights and ecosystem fit must be reviewed. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.md) | Official Russian registry provenance is required | Requires your own search and matching infrastructure. |

## Scenario-Based Recommendation

Shortlist Yandex Geosuggest when address-entry UX is coupled to Yandex Maps or when Yandex organization/geographic suggestions are valuable. Keep a separate decision for geocoding, address cleaning, place search and data-rights storage.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

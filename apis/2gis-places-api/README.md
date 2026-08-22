# 2GIS Places API

[Русская версия](README.ru.md)

> 2GIS Search API product for searching organizations, buildings and places.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | 2GIS |
| Product status | Active |
| Live credential test | Not performed |

## Quick Verdict

**Best for:** organization, building and place search in products that need 2GIS directory context.

**Avoid when:** the primary task is canonical address normalization, direct/reverse geocoding, address autocomplete alone, routing, or official registry ownership.

**Bottom line:** Places API is the 2GIS product to evaluate when the user needs organizations, buildings, venues and catalog attributes. It is related to address/geocoding decisions because users often confuse place search with address validation.

## Product Boundary

This profile covers:

- organization, building and place search;
- search by text, category/business area, geotags, attributes, phone/website and related criteria;
- additional on-demand methods and fields where documented;
- relationship with Suggest API for search hints.

This profile does not cover:

- autocomplete as the primary UX;
- direct/reverse geocoding;
- routing;
- official GAR/FIAS registry integration.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Organization and venue search | Strong | Official docs state Places API searches organizations, buildings and places. |
| Catalog-enriched map search | Strong | 2GIS directory context is the product's core. |
| Address suggestions | Medium | Use Suggest API for hints before Places lookup. |
| Address-to-coordinate geocoding | Weak | Use 2GIS Geocoder API. |
| Registry-quality validation | Weak | Places results are not the official Russian address registry. |
| Bulk enrichment | Medium/unknown | Pricing is public, but storage and batch rights need contract review. |

## Technical Access

| Field | Value |
|---|---|
| Protocol | HTTP GET |
| API family | 2GIS Search APIs |
| Required access | API key |
| Response format | JSON |
| Main object types | Organizations, buildings, places |
| Search examples | Company name, business area, geotags, attributes, telephone, website, category, city |
| Related autocomplete | 2GIS Suggest API |
| On-demand methods | `bysite`, `byphone`, `byitin`, `bytradelicense`, `byfias` |
| OpenAPI / Swagger | Not found in reviewed public docs |

## Pricing, Limits and Rights

| Item | Confirmed value | Status |
|---|---|---|
| Pricing model | Successful requests / monthly units | verified |
| Public price floor | 6,700 RUB for 10,000 Places API units/month | verified |
| Per-minute limit | 600 Search units/minute | verified |
| Demo limit | 1,000 total Search-service requests for Places API | verified |
| Demo period | One month demo key | verified |
| On-demand fields/methods | Some fields and methods require extra paid access | verified |
| Directory freshness | Monthly update claim for 2GIS directory | provider_reported |
| Caching | WebAPI offer says caching is not provided | verified |
| SLA | Not found publicly in this research | unknown |

## Commercial and Legal Notes

- Places API may require additional paid access for fields/methods such as contact groups, ITIN, FIAS codes, OKATO/OKTMO and other rich data.
- The 2GIS WebAPI offer restricts extraction, storage, processing, modification and distribution outside contract terms.
- Caching is explicitly not provided in the reviewed WebAPI offer.
- SaaS embedding, redistribution and customer-facing display require legal and contract review.

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`2GIS Suggest API`](../2gis-suggest-api/README.md) | You only need search-box suggestions before a user selects a result | Not a full place record API. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | You need address/coordinate conversion | Not an organization catalog API. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.md) | The suggestion UX should use Yandex Maps data | Product boundary and licenses differ. |
| [`DaData API`](../dadata/README.md) | The task is Russian company/counterparty data | Different data model and procurement question. |

## Scenario-Based Recommendation

Choose 2GIS Places API when the decision is really about place and organization search. Keep it separate from address normalization and geocoding decisions, and request a method/field matrix before procurement.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

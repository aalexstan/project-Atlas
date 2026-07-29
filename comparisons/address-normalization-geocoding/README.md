# Address Normalization, Address Registries and Geocoding APIs

[Русская версия](README.ru.md)

> Scenario-based comparison for choosing address suggestions, address cleaning, geocoding, place search and official registry integration.

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-07-29 |
| Market / region | Russia plus selected international geocoding context |
| Live testing | Not performed |
| Candidates reviewed | DaData Address APIs, Yandex Maps Geocoder API, 2GIS Geocoder API, FIAS/GAR Data Integration |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Address suggestions in Russian forms | DaData Address APIs; evaluate Yandex Geosuggest and 2GIS Suggest separately if map ecosystem matters | DaData address suggestions are directly documented; Yandex/2GIS suggestions are separate products not profiled in this pass. |
| Russian address cleaning and normalization | DaData Address APIs | Official docs confirm cleaning, quality fields, coordinates and registry identifiers; Suggestions should not be used for automatic processing. |
| Direct geocoding | Yandex Maps Geocoder API; 2GIS Geocoder API; DaData Address APIs | All three have documented address-to-coordinate flows, but pricing and storage rights differ. |
| Reverse geocoding | Yandex Maps Geocoder API; 2GIS Geocoder API; DaData Address APIs | All three document coordinate-to-address or nearby-address flows. |
| Organization/place search | Evaluate 2GIS Places API and Yandex Organization Search separately | Places search is not the same as geocoding or registry validation. |
| Own Russian address base | FIAS/GAR Data Integration | Official registry provenance, but requires ETL, indexing and search logic. |
| Bulk address processing | DaData cleaning; FIAS/GAR for owned registry; commercial geocoders only after rights review | Batch/storage rights and per-record costs can dominate TCO. |

There is no universal winner. The best choice depends on whether the task is input UX, data quality, geocoding, registry provenance or commercial data rights.

## Scope

This comparison covers:

- address suggestions while a user types;
- address normalization and standardization;
- checking address existence and quality;
- direct geocoding: address -> coordinates;
- reverse geocoding: coordinates -> address;
- organization/place search as a related but separate scenario;
- routing as explicitly out of scope;
- building an address base from an official registry;
- bulk processing;
- storage, caching, display, SaaS and redistribution constraints.

## Key Distinctions

- Geocoding is not address normalization. A coordinate match does not guarantee canonical fields or legal address validity.
- Company autocomplete is not address autocomplete. A provider can be strong at one without proving the other.
- Places search is not registry-quality address validation.
- An official registry is not automatically a low-latency API product.
- Coordinate precision depends on house/street/locality-level data and must be benchmarked.
- Data license and storage rights can change the best choice even when technical quality is good.

## Comparison Matrix

| Criterion | DaData Address APIs | Yandex Maps Geocoder API | 2GIS Geocoder API | FIAS/GAR Data Integration |
|---|---|---|---|---|
| Product class | Suggestions, cleaning, geocoding | Map geocoder | Map/catalog geocoder | Official registry integration |
| Address suggestions | Yes | Separate Geosuggest product | Separate Suggest API | Requires own search |
| Normalization | Yes, Russia-only cleaning | Not primary capability | Not primary capability | Requires own logic |
| Validation | Cleaning quality fields | Geocoder precision only | Geocoder match only | Official registry provenance |
| Direct geocoding | Yes, via cleaning endpoint | Yes | Yes | Not confirmed |
| Reverse geocoding | Yes | Yes | Yes | Not confirmed |
| Organization/place search | Use DaData company APIs, separate scope | Separate product | Separate Places API | Not applicable |
| Russia coverage | Strong documented focus | Provider map coverage | Provider map/catalog coverage | Official Russian registry |
| International coverage | Suggestions city-level provider claim; cleaning/geocoding Russia-only | Provider map coverage; scenario check needed | Provider catalog coverage; scenario check needed | Russia only |
| Official registry provenance | FIAS/GAR/KLADR fields where available | No registry guarantee | Some registry fields may be on-demand | Primary registry source |
| Public documentation | Yes | Yes | Yes | Partial for developer access |
| Authentication | Token; secret for cleaning | API key | API key | Depends on channel; unknown for API services |
| Self-service | Yes | Yes for keys/free/test; commercial license may require purchase | Demo key/subscription via Platform Manager | Public portal; integration channel details unclear |
| Public pricing | Yes | Yes | Yes | Unknown for API/download service channels |
| Free tier / trial | 10,000 subscription requests/day | 1,000 requests/day free terms; 100/day test period | Demo key one month / 1,000 Search requests | Not applicable as commercial API |
| Quotas | Daily plan limits | Daily package limits | Package units | Unknown |
| Rate limits | 30 rps suggestions; 20 rps cleaning | RPS unknown publicly | 600 Search units/minute | Unknown |
| Batch | Cleaning one address/request; no async batch confirmed | Unknown/contract-sensitive | Unknown | Data-feed route requires ETL |
| Storage | Contract-sensitive; provider reports no API cleaning storage | Restricted; Extended license associated with storage | Contract-sensitive; caching not provided in WebAPI offer | Legal review for use model |
| Caching | Needs contract review | General temporary caching restrictions | Caching not provided in WebAPI offer | Depends on legal interpretation/use |
| Customer-facing display | Usually form/API output; confirm contract | Free terms require Yandex map display | Confirm contract and attribution | Depends on use model |
| Redistribution | Unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Needs legal review |
| SaaS use | Needs contract review | Needs contract review | Needs contract review | Needs legal review |
| SLA | Unknown publicly | Unknown publicly | Unknown publicly | Unknown |
| Live test status | Not performed | Not performed | Not performed | Not performed |
| Key unknowns | SLA, async batch, data rights | RPS, SLA, storage/display rights | SLA, OpenAPI, storage/caching rights | API specs, auth, formats, cadence, legal use |

## Recommendations by Scenario

### Address Entry UX

Start with [`DaData Address APIs`](../../apis/dadata-address-api/README.md) for Russian address forms. If the UI must be coupled to a specific map ecosystem, evaluate Yandex Geosuggest or 2GIS Suggest as separate products.

### Cleaning Existing Addresses

Use DaData cleaning for a commercial API route. Use [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md) when the organization wants to own the official registry pipeline and can build matching/search logic.

### Geocoding

Shortlist [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md) and DaData. Pick after checking map-display coupling, storage/caching rights, batch rights, latency and match quality.

### Official Registry Base

Use FIAS/GAR as the primary official Russian registry route. Do not treat it as a ready replacement for address suggestions or geocoding without building an integration platform around it.

### 115-FZ, Sanctions and Compliance

This comparison does not validate compliance coverage. Address APIs and geocoders do not by themselves solve AML, sanctions or legal compliance screening.

## Unresolved Questions

| Question | Affected decision | Next verification step |
|---|---|---|
| Which provider allows long-term storage and customer display for the exact SaaS model? | SaaS, redistribution, internal enrichment | Contract/legal review. |
| Which provider has best house-level coordinate precision for the user's sample? | Geocoding selection | Credentialed benchmark on agreed sample. |
| Can large batch geocoding be performed asynchronously and legally? | Bulk processing | Ask provider and test pilot credentials. |
| What SLA and support tiers apply in production? | Enterprise procurement | Request commercial offer and SLA. |
| What is the exact FIAS/GAR API or download integration path? | Official registry strategy | Review developer access docs or contact FNS channel. |

## Method and Sources

This comparison uses official provider and registry sources reviewed on 2026-07-29. No live testing, quality benchmark or contract review was performed.

See [`evidence.md`](evidence.md).

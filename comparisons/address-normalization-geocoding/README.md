# Address Normalization, Address Registries and Geocoding APIs

[Русская версия](README.ru.md)

> Scenario-based comparison for choosing address suggestions, address cleaning, geocoding, place search, open-data geocoding and official registry integration.

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-07-29 |
| Market / region | Russia plus selected international/open-data geocoding context |
| Live testing | Not performed |
| Candidates reviewed | DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Nominatim Geocoder Software, FIAS/GAR Data Integration |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Russian address suggestions in forms | [`DaData Address APIs`](../../apis/dadata-address-api/README.md); [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md); [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md) | DaData is strongest for Russian address-form workflows; Yandex and 2GIS are useful when the UI is tied to their map/search ecosystems. |
| Russian address cleaning and normalization | [`DaData Address APIs`](../../apis/dadata-address-api/README.md); [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md) for owned registry | DaData has a documented cleaning API; GAR is the official source but requires matching/search logic. |
| Direct geocoding | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md); DaData; [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.md) for self-hosting | Hosted commercial geocoders differ by license and ecosystem; Nominatim is an operational self-host route. |
| Reverse geocoding | Yandex Geocoder; 2GIS Geocoder; DaData; self-hosted Nominatim | All have documented coordinate-to-address capabilities except FIAS/GAR. |
| Organization/place search | [`2GIS Places API`](../../apis/2gis-places-api/README.md); Yandex organization products need separate research | Places search is a different product class from geocoding and registry validation. |
| Own Russian address base | FIAS/GAR Data Integration | Official registry provenance, but it requires ETL, indexing, updates and legal review. |
| Open-data geocoding ownership | Nominatim self-hosting | Avoids hosted API dependence but creates OSM/ODbL and operations responsibilities. |
| Bulk address processing | DaData cleaning; FIAS/GAR for owned registry; self-hosted Nominatim for OSM geocoding; commercial geocoders only after rights review | Batch, storage, caching and redistribution rights can dominate TCO. |

There is no universal winner. The best choice depends on whether the task is input UX, data quality, geocoding, registry provenance, open-data ownership or commercial data rights.

## Scope

This comparison covers address suggestions while typing, normalization and standardization, address existence/quality checks, direct geocoding, reverse geocoding, place search as a separate scenario, official registry integration, mass processing, storage, caching, display, SaaS and redistribution constraints.

Routing is explicitly out of scope. A geocoder can produce coordinates; routing products decide paths, distances, ETAs and matrices.

## Key Distinctions

- Geocoding is not address normalization. A coordinate match does not guarantee canonical fields or legal address validity.
- Company autocomplete is not address autocomplete.
- Suggestions/autocomplete are not bulk cleaning workflows.
- Places search is not registry-quality address validation.
- An official registry is not automatically a low-latency autocomplete API.
- Public hosted geocoding is not the same as self-hosted geocoder software.
- Coordinate precision depends on house/street/locality-level data and must be benchmarked.
- License, storage, caching, display and redistribution rights can change the best choice even when technical quality is strong.

## Capability Matrix

| Criterion | DaData Address | Yandex Geosuggest | Yandex Geocoder | 2GIS Suggest | 2GIS Places | 2GIS Geocoder | Nominatim | FIAS/GAR |
|---|---|---|---|---|---|---|---|---|
| Product class | Suggestions, cleaning, geocoding | Suggestions/autocomplete | Map geocoder | Suggestions/autocomplete | Places/catalog search | Map/catalog geocoder | Open-source geocoder software | Official registry integration |
| Address suggestions | Yes | Yes | No | Yes | Use Suggest | No | Public autocomplete forbidden; self-host custom | Requires own search or API-service details |
| Normalization | Yes, Russia-only cleaning | No | Not primary | No | No | Not primary | No | Requires own logic |
| Validation | Cleaning quality fields | Suggestion-level only | Geocoder precision only | Suggestion-level only | Directory match only | Geocoder match only | OSM match only | Official registry provenance |
| Direct geocoding | Yes via cleaning | No; can pass `uri` to Geocoder | Yes | No | No | Yes | Yes | Not confirmed |
| Reverse geocoding | Yes | No | Yes | No | No | Yes | Yes | Not confirmed |
| Organization/place search | Separate DaData company scope | Suggestions only | Separate product | Suggestions only | Yes | Separate Places API | Limited OSM POI search | Not applicable |
| Russia coverage | Strong documented focus | Provider map/data coverage | Provider map coverage | Provider catalog coverage | Provider catalog coverage | Provider map/catalog coverage | OSM coverage varies | Official Russian registry |
| International coverage | Suggestions city-level provider claim; cleaning/geocoding Russia-only | Provider map coverage | Provider map coverage | Provider catalog coverage | Provider catalog coverage | Provider catalog coverage | OSM coverage varies by region | Russia only |
| Official registry provenance | FIAS/GAR/KLADR fields where available | No registry guarantee | No registry guarantee | Some FIAS-related fields may be on-demand elsewhere | Some FIAS fields on demand | Some registry fields may be on demand | OSM, not official registry | Primary registry source |
| Public documentation | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Partial |
| Authentication | Token; secret for cleaning | API key | API key | API key | API key | API key | Public instance: User-Agent/Referer; self-host operator-defined | Depends on channel |
| Self-service | Yes | Yes/test/commercial license | Yes/test/commercial license | Demo key/subscription | Demo key/subscription | Demo key/subscription | Public limited; self-host | Public portal; integration details unclear |
| Public pricing | Yes | Yes | Yes | Yes | Yes | Yes | Not commercial API price | No monetary price stated for open-data page; API/SMEV unknown |
| Free tier / trial | 10,000 subscription requests/day | 100/day test period; commercial tariffs | 1,000/day free terms; 100/day test period | Demo key / 1,000 Search requests | Demo key / 1,000 Search requests | Demo key / 1,000 Search requests | Public limited policy; self-host costs | Not applicable as commercial API |
| Quotas | Daily plan limits | Daily package limits | Daily package limits | Monthly units plus per-minute | Monthly units plus per-minute | Monthly units plus per-minute | Public 1 rps; self-host operator-defined | Unknown |
| Rate limits | 30 rps suggestions; 20 rps cleaning | RPS unknown publicly | RPS unknown publicly | 600 Search units/minute | 600 Search units/minute | 600 Search units/minute | Public max 1 rps | Unknown |
| Batch | Cleaning one address/request; async batch unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown | Unknown/on-demand | Unknown | Public bulk discouraged; self-host possible | Open-data ZIP route verified; API batch service mentioned but method details unknown |
| Public hosted API | Yes | Yes | Yes | Yes | Yes | Yes | Limited public instance only | Public portal plus official channels |
| Self-hosted option | No | No | No | Provider-reported On-Premise | Provider platform/on-premise needs deal | Provider platform/on-premise needs deal | Yes | User-operated registry pipeline |
| Storage | Contract-sensitive | Extended license marketed with storage | Extended license marketed with storage | Contract-sensitive | Contract-sensitive | Contract-sensitive | ODbL/legal review; cache repeated public results | Legal review |
| Caching | Needs contract review | Needs contract review | Temporary caching restrictions unless agreed | WebAPI offer says caching not provided | WebAPI offer says caching not provided | WebAPI offer says caching not provided | Public policy requires caching repeated results; ODbL applies | Depends on use model |
| Customer-facing display | Confirm contract | Needs Yandex terms review | Yandex map/display restrictions matter | Contract/attribution review | Contract/attribution review | Contract/attribution review | Attribution required | Depends on use model |
| Redistribution | Unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | ODbL/legal review | Legal review |
| SaaS use | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Needs contract review | ODbL/privacy/ops review | Legal review |
| SLA | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | No public OSMF SLA found | Unknown |
| Privacy | Contract review | Yandex terms review | Yandex terms review | Contract review | Contract review | Contract review | Public policy says not to submit confidential/personal data | Legal review |
| Operational ownership | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium | High: import, updates, deployment, security and ODbL review | High for registry route |
| Live test status | Not performed | Not performed | Not performed | Not performed | Not performed | Not performed | Not performed | Not performed |
| Key unknowns | SLA, async batch, data rights | RPS, SLA, exact rights | RPS, SLA, exact rights | SLA, OpenAPI, rights | SLA, on-demand fields, rights | SLA, OpenAPI, rights | Sizing, ODbL, benchmark | API specs, auth, schemas, support, ZIP package contents |

## Recommendations by Scenario

### Address Entry UX

Start with DaData for Russian address forms. Add Yandex Geosuggest when the UI is already Yandex Maps-centered. Add 2GIS Suggest when suggestions should feed 2GIS catalog/search results.

### Cleaning Existing Addresses

Use DaData cleaning for a commercial API route. Use FIAS/GAR when the organization wants to own the official registry pipeline and can build matching/search logic.

### Geocoding

Shortlist Yandex Maps Geocoder, 2GIS Geocoder and DaData. Add self-hosted Nominatim when open data, international OSM coverage or operational ownership is a requirement. Decide after checking precision, rights, cost and SLA.

### Organizations and Places

Use 2GIS Places API when the task is organization, building or place search. Do not infer registry-quality address validation from place search.

### Official Registry Base

Use FIAS/GAR as the primary official Russian registry route. The open-data route is now verified as XML ZIP with a structure ZIP and weekly updates on the FNS open-data page. Treat official API services as mentioned but underspecified until method catalog, auth, schema and support details are captured.

### Public Open-Data Geocoding

Do not present public `nominatim.openstreetmap.org` as a free production API. Use it only within its usage policy. For production, evaluate self-hosted Nominatim or a commercial provider. Self-hosted Nominatim requires import sizing, update planning, production deployment, monitoring, rate limiting, backups and ODbL/legal review.

### 115-FZ, Sanctions and Compliance

This comparison does not validate compliance coverage. Address APIs and geocoders do not by themselves solve AML, sanctions or legal compliance screening.

## Unresolved Questions

| Question | Affected decision | Next verification step |
|---|---|---|
| Which provider allows long-term storage and customer display for the exact SaaS model? | SaaS, redistribution, internal enrichment | Contract/legal review. |
| Which provider has best house-level coordinate precision for the user's sample? | Geocoding selection | Credentialed benchmark on agreed sample. |
| Can large batch geocoding be performed asynchronously and legally? | Bulk processing | Ask provider and test pilot credentials. |
| What SLA and support tiers apply in production? | Enterprise procurement | Request commercial offer and SLA. |
| What is the exact FIAS/GAR API method catalog and access process? | Official registry strategy | Review developer docs or request FNS channel details. |
| What are ODbL obligations for the intended cache, database or SaaS product? | Nominatim/self-hosting | Legal review with concrete data-flow diagram. |
| What hardware, import style and update mode are required for self-hosted Nominatim? | Nominatim/self-hosting | Use the self-hosting checklist and run a benchmark on target extracts. |

## Method and Sources

This comparison uses official provider and registry sources reviewed on 2026-07-29. No live testing, quality benchmark or contract review was performed.

See [`evidence.md`](evidence.md).

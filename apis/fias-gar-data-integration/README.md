# FIAS/GAR Data Integration

[Русская версия](README.ru.md)

> Official Russian address registry route for building your own address database and validation infrastructure.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Federal Tax Service of Russia |
| Product status | Active |
| Live integration test | Not performed |

## Quick Verdict

**Best for:** teams that need official Russian address provenance and are ready to build their own ETL, storage, indexing, search and validation logic.

**Avoid when:** you need a turnkey low-latency address-suggestions API, geocoding quality out of the box, commercial SLA, or simple per-request integration.

**Bottom line:** FIAS/GAR is the official registry route, not a commercial address API. It can be the right foundation for a proprietary address base, but it is not a drop-in substitute for DaData, Yandex or 2GIS.

## What It Is

GAR is the State Address Register: the state information resource containing Russian address information. FIAS is the federal information system operated by the Federal Tax Service that maintains and provides access to GAR.

This profile is named "data integration" because reviewed official pages confirm registry identity and developer access modes, but do not expose a complete public REST-style API specification in the captured public documentation. FNS materials mention file downloads, SMEV and API services; Atlas does not treat visible website endpoints as supported public APIs unless FNS documentation identifies them as such.

## Best-Fit Scenarios

| Scenario | Fit | Why |
|---|---|---|
| Own Russian address registry | Strong | GAR is the official registry source. |
| Official provenance and regulated workflows | Strong | FNS sources state GAR/FIAS legal role and public address resource purpose. |
| Address validation against official objects | Medium | Registry provenance is strong, but matching and quality logic must be built. |
| Address autocomplete in a form | Weak by itself | Requires your own search index and UX layer. |
| Direct/reverse geocoding | Unknown | Not confirmed as a public official GAR capability in this review. |
| Routing | Not applicable | GAR is not a routing product. |

## Access Model

| Channel | Status | Notes |
|---|---|---|
| Public address search | Verified | FIAS public portal exposes address search. |
| Open data / file downloads | Verified as official open-data route | FNS open-data catalog lists dataset `7707329152-fias`, XML format, current ZIP data URL, structure ZIP, weekly updates and previous releases. |
| SMEV | Verified as developer-section entry and official integration route | FNS archived material describes daily publication through SMEV; eligibility and process are unknown in this profile. |
| API services | Verified as developer-section entry and official integration route | FNS archived material describes online API batch provision by request; public method catalog, base URL, auth and schemas were not visible in reviewed static pages. |
| Search / Frontend web pages | Verified as user-facing portal | Do not treat discovered web endpoints as supported integration APIs without explicit FNS documentation. |
| KLADR legacy downloads | Sunset path verified | FNS states KLADR publication becomes quarterly from 2026-07-01, semiannual from 2027-01-01 and stops from 2028-01-01. |

## Implementation Implications

Using GAR as a source usually means building:

- ingest and update jobs;
- storage schema;
- search index;
- address parsing and normalization;
- matching confidence model;
- change processing;
- monitoring and support process.

That cost must be included in TCO. A registry feed can be cheaper per request and still more expensive operationally than a commercial API.

## Pricing and Rights

| Item | Status |
|---|---|
| Public/open registry positioning | verified |
| API service price | unknown |
| Open-data file format | XML ZIP listed in official open-data catalog |
| Open-data update cadence | weekly in official open-data catalog |
| Current open-data package metadata | official page lists `data-28072026-structure-20191024.zip`, last modification `2026-07-28`, actuality date `2026-08-02`, previous releases for `2026-07-24`, `2026-07-21`, `2026-07-17`, `2026-07-14` |
| File download price | no monetary price stated on reviewed open-data page |
| SMEV eligibility | unknown |
| Structure reference | structure ZIP listed in official open-data catalog; archive contents not inspected |
| Current package model | unknown; metadata alone does not prove full, delta or mixed semantics |
| API schemas | unknown |
| Commercial SaaS / redistribution rights | needs legal review |
| SLA | unknown |

## Alternatives

| Alternative | Better when | Main trade-off |
|---|---|---|
| [`DaData Address APIs`](../dadata-address-api/README.md) | Need turnkey Russian suggestions, cleaning and geocoding | Commercial pricing and contract restrictions apply. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.md) | Need geocoding for Yandex Maps display | Not registry validation; display/storage restrictions apply. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.md) | Need geocoding in 2GIS map/catalog workflows | Not a full registry route; storage/caching terms matter. |

## Scenario-Based Recommendation

Choose FIAS/GAR when official Russian address provenance and long-term data ownership matter enough to justify engineering work. The current open-data page gives useful package metadata, but Atlas has not inspected archive contents or proved full/delta semantics. Choose a commercial API when the main need is fast address entry, geocoding, support and predictable integration effort.

## Evidence

See [`evidence.md`](evidence.md).

## Change History

See [`changes.md`](changes.md).

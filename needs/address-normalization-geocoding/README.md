# Address Normalization, Address Registries and Geocoding

[Русская версия](README.ru.md)

> Which API or official source should we choose for address suggestions, normalization, geocoding, address validation and building an address database?

## Task Definition

This route helps choose between commercial address APIs, map geocoders, autocomplete products, place search, open-data geocoding and the official Russian address registry route. It separates input suggestions, cleaning, geocoding, place search and registry integration because they solve different problems.

## Who This Route Fits

- Product teams adding address autocomplete to forms.
- CRM/ERP teams cleaning existing Russian address records.
- Developers adding direct or reverse geocoding.
- Teams deciding between hosted APIs and self-hosted open-data geocoding.
- Data teams building an internal Russian address base.
- Procurement teams checking storage, caching, display, SaaS and redistribution rights.

## Quick Decision Table

| User scenario | Initial shortlist | Why | Main risk | Next Atlas document |
|---|---|---|---|---|
| Address suggestions while typing | [`DaData Address APIs`](../../apis/dadata-address-api/README.md); [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md); [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md) | DaData is address-form focused; Yandex/2GIS fit their map/search ecosystems. | Suggestions are not unattended batch cleaning and rights differ by provider. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Address normalization and cleaning | [`DaData Address APIs`](../../apis/dadata-address-api/README.md) | Cleaning API returns structured fields, quality indicators, coordinates and registry identifiers. | One address per request; pay-per-record price; rights need contract review. | [`DaData profile`](../../apis/dadata-address-api/README.md) |
| Check official Russian address existence | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md); DaData cleaning as commercial route | GAR is the official registry; DaData can help match/clean addresses. | GAR requires matching, ETL and search; API-service details remain incomplete. | [`FIAS/GAR profile`](../../apis/fias-gar-data-integration/README.md) |
| Direct geocoding | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md); [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.md); [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.md); [`LocationIQ Geocoding API`](../../apis/locationiq-geocoding-api/README.md); DaData; [`Nominatim`](../../apis/nominatim-geocoder-software/README.md) for self-hosting | Hosted geocoders and self-hosted OSM route solve different operating models. | Storage/display rights, attribution, coordinate precision and operations burden need testing. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Reverse geocoding | Yandex Geocoder; 2GIS Geocoder; Geoapify; OpenCage; LocationIQ; DaData; self-hosted Nominatim | Documented coordinate-to-address routes exist outside FIAS/GAR. | Returned object level may differ by provider and location. | [`Test protocol`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.md) |
| Organizations and places | [`2GIS Places API`](../../apis/2gis-places-api/README.md); [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.md) | Place search is a separate product class. | Do not infer place search from geocoder docs or registry validation. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Own address database | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md) | Official registry provenance and data ownership route. | ETL/search/update operations can dominate TCO. | [`FIAS/GAR profile`](../../apis/fias-gar-data-integration/README.md) |
| Open-data geocoding ownership | [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.md); [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.md); [`LocationIQ Geocoding API`](../../apis/locationiq-geocoding-api/README.md); [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.md) | Geoapify, OpenCage and LocationIQ are hosted commercial routes; self-hosting can use OSM data without a hosted API vendor dependency. | Attribution, ODbL, legal review, benchmark and operations differ strongly. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Mass address processing | DaData cleaning; FIAS/GAR for owned registry; Geoapify hosted batch geocoding; OpenCage parallel/spreadsheet geocoding; LocationIQ concurrent-request geocoding or provider-arranged batch; self-hosted Nominatim; commercial geocoders after legal check | Different routes solve cleaning, registry base, geocoding and operational ownership. | Batch rights, per-record costs, ODbL, caching and redistribution. | [`RFP`](../../procurement/address-geocoding-api-selection/RFP.md) |

## Scenario Routes

### Address Suggestions

Start with DaData for Russian address autocomplete. Add Yandex Geosuggest if the UI is coupled to Yandex Maps. Add 2GIS Suggest if suggestions should feed 2GIS catalog/search results. Add LocationIQ only when hosted international autocomplete is part of the target geocoding shortlist.

### Normalization and Validation

Use DaData cleaning when you need a commercial API that structures Russian addresses and returns quality fields. Use FIAS/GAR when official registry provenance matters and you can build the matching/search layer.

### Direct and Reverse Geocoding

Shortlist Yandex Maps Geocoder, 2GIS Geocoder, Geoapify, OpenCage, LocationIQ and DaData. Add self-hosted Nominatim when open data, OSM coverage and operational ownership matter. Decide after testing house-level precision, latency, quotas, attribution, storage/caching rights and map-display restrictions.

### Organizations and Places

Do not treat geocoding as organization search. 2GIS Places API and Yandex Maps Organization Search API are active profiles for organization/place search in their respective map ecosystems.

### Public Nominatim vs Self-Hosting

Public `nominatim.openstreetmap.org` is limited by usage policy, forbids autocomplete and is not a free production API. Geoapify, OpenCage and LocationIQ are hosted commercial open-data routes, while self-hosted Nominatim is a separate operating model with infrastructure, import sizing, update, production deployment, monitoring, security and ODbL responsibilities.

### FIAS/GAR Official Interfaces

FIAS/GAR is the official Russian registry route. The FNS open-data catalog verifies XML ZIP downloads, a structure ZIP, weekly updates and previous release links; Atlas has inspected the structure ZIP, the current data ZIP central directory, root-level dictionary XML files and sample regional directories `99/`, `87/` and sparse `82/`. Official materials also mention SMEV and API services, but the current public method catalog, base URL, auth, quotas and SLA remain blockers, and remaining regions, national row counts and full/delta semantics are not verified.

### Routing

Routing is a separate task. A geocoder can turn an address into coordinates, but route building, matrices and ETA require routing APIs.

### Russia vs International Coverage

DaData is deepest for Russian address workflows. Yandex and 2GIS fit their map/catalog coverage. Nominatim follows OpenStreetMap data quality, which varies strongly by region and requires benchmarking.

### Storage, Caching and Redistribution

Ask this before choosing a provider. A technically strong geocoder can be a poor fit if it cannot be used for long-term storage, SaaS embedding, customer-facing display or redistribution.

## Current Research Limits

- No live credential tests were performed.
- No common address-quality benchmark was run.
- SLA and support terms are mostly unknown publicly.
- Contractual storage, caching, SaaS and redistribution rights require legal review.
- FIAS/GAR open-data XML ZIP route, structure XSD archive, current data ZIP central directory, root dictionary XML payload and sample regional directories `99/`, `87/` and sparse `82/` payload are verified, but remaining regions, national row counts, full/delta semantics and API-service details remain incomplete in reviewed public pages.
- ODbL implications for Nominatim/OSM derived databases require legal review.
- Nominatim self-hosting still needs a benchmark on target extracts and hardware.

## Questions Before Procurement

- Is the task autocomplete, cleaning, geocoding, registry validation, place search or routing?
- Which countries and address granularity levels are required?
- Will results be stored, cached, shown to customers, redistributed or embedded in SaaS?
- What daily volume, peak rate, latency and SLA are required?
- Is batch processing required, and must it be asynchronous?
- Does the team need official Russian registry provenance, open-data ownership or turnkey UX?
- What benchmark sample will be used for Moscow, Saint Petersburg, regions and any international markets?
- Which legal obligations apply to ODbL, attribution, personal data and derived databases?

## Links

- API profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md), [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.md), [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md), [`2GIS Places API`](../../apis/2gis-places-api/README.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md), [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.md), [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.md), [`LocationIQ Geocoding API`](../../apis/locationiq-geocoding-api/README.md), [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md)
- Comparison: [`Address Normalization, Address Registries and Geocoding APIs`](../../comparisons/address-normalization-geocoding/README.md)
- Procurement kit: [`Address and Geocoding API Selection`](../../procurement/address-geocoding-api-selection/README.md), [`Nominatim Self-Hosting Checklist`](../../procurement/address-geocoding-api-selection/NOMINATIM_SELF_HOSTING.md)

## Next Step

Pick the row that matches your primary scenario, read the linked comparison, then use the RFP and test protocol to ask providers for rights, limits, SLA and pilot credentials before selecting a production API.

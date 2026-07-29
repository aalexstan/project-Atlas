# Address Normalization, Address Registries and Geocoding

[Русская версия](README.ru.md)

> Which API or official source should we choose for address suggestions, normalization, geocoding, address validation and building an address database?

## Task Definition

This route helps choose between commercial address APIs, map geocoders and the official Russian address registry route. It separates input suggestions, cleaning, geocoding, place search and registry integration because they solve different problems.

## Who This Route Fits

- Product teams adding address autocomplete to forms.
- CRM/ERP teams cleaning existing Russian address records.
- Developers adding direct or reverse geocoding.
- Data teams building an internal Russian address base.
- Procurement teams checking storage, caching, display, SaaS and redistribution rights.

## Quick Decision Table

| User scenario | Initial shortlist | Why | Main risk | Next Atlas document |
|---|---|---|---|---|
| Address suggestions while typing | [`DaData Address APIs`](../../apis/dadata-address-api/README.md) | Directly documented address Suggestions API and public pricing. | Suggestions are not for unattended batch processing. | [`DaData profile`](../../apis/dadata-address-api/README.md) |
| Address normalization and cleaning | [`DaData Address APIs`](../../apis/dadata-address-api/README.md) | Cleaning API returns structured fields, quality indicators, coordinates and registry identifiers. | One address per request; pay-per-record price. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Check official Russian address existence | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md); DaData cleaning as commercial route | GAR is the official registry; DaData can help match/clean addresses. | GAR requires your own matching and ETL; commercial API rights still matter. | [`FIAS/GAR profile`](../../apis/fias-gar-data-integration/README.md) |
| Direct geocoding | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md); DaData | All have documented address-to-coordinate flows. | Storage/display rights and coordinate precision need testing. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Reverse geocoding | Yandex; 2GIS; DaData | All have documented coordinate-to-address flows. | Returned object level may differ by provider and location. | [`Procurement checklist`](../../procurement/address-geocoding-api-selection/README.md) |
| Organization and place search | Evaluate 2GIS Places API and Yandex Organization Search separately | Places search is a separate product class. | Do not infer place search from geocoder docs. | [`Comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Own address database | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md) | Official registry provenance and data ownership route. | ETL/search/update operations can dominate TCO. | [`FIAS/GAR profile`](../../apis/fias-gar-data-integration/README.md) |
| Mass address processing | DaData cleaning; FIAS/GAR for owned registry; commercial geocoders after legal check | Different routes solve cleaning, registry base and geocoding. | Batch rights, per-record costs and caching restrictions. | [`RFP`](../../procurement/address-geocoding-api-selection/RFP.md) |

## Scenario Routes

### Address Suggestions

Start with DaData for Russian address autocomplete. If the UI must be tied to a map ecosystem, add Yandex Geosuggest or 2GIS Suggest to a follow-up research shortlist.

### Normalization and Validation

Use DaData cleaning when you need a commercial API that structures Russian addresses and returns quality fields. Use FIAS/GAR when official registry provenance matters and you can build the matching/search layer.

### Direct and Reverse Geocoding

Shortlist Yandex Maps Geocoder, 2GIS Geocoder and DaData. Decide after testing house-level precision, latency, quotas, storage/caching rights and map-display restrictions.

### Organizations and Places

Do not treat geocoding as organization search. 2GIS Places API and Yandex Organization Search are separate products and should be evaluated separately when the user needs businesses, venues or POIs.

### Routing

Routing is a separate task. A geocoder can help turn an address into coordinates, but route building, matrices and ETA require routing APIs.

### Russia vs International Coverage

DaData is deepest for Russian address workflows. Yandex and 2GIS may fit map-geocoding scenarios beyond Russia, but exact coverage and precision need a scenario benchmark.

### Storage, Caching and Redistribution

Ask this before choosing a provider. A technically strong geocoder can be a poor fit if it cannot be used for long-term storage, SaaS embedding, customer-facing display or redistribution.

## Current Research Limits

- No live credential tests were performed.
- No common address-quality benchmark was run.
- SLA and support terms are mostly unknown publicly.
- Contractual storage, caching, SaaS and redistribution rights require legal review.
- FIAS/GAR API-service details remain incomplete in reviewed public pages.

## Questions Before Procurement

- Is the task autocomplete, cleaning, geocoding, registry validation, place search or routing?
- Which countries and granularity levels are required?
- Will results be stored, cached, shown to customers or redistributed?
- What daily volume, peak rate, latency and SLA are required?
- Is batch processing required, and must it be asynchronous?
- Does the team need official Russian registry provenance or turnkey UX?
- What benchmark sample will be used for Moscow, Saint Petersburg and regions?

## Links

- API profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.md)
- Comparison: [`Address Normalization, Address Registries and Geocoding APIs`](../../comparisons/address-normalization-geocoding/README.md)
- Procurement kit: [`Address and Geocoding API Selection`](../../procurement/address-geocoding-api-selection/README.md)

## Next Step

Pick the row that matches your primary scenario, read the linked comparison, then use the RFP and test protocol to ask providers for rights, limits, SLA and pilot credentials before selecting a production API.

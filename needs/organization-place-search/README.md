# Organization and Place Search

[Русская версия](README.ru.md)

> Which API should we choose for organization, place, building or local-business search?

## Task Definition

This route covers search for organizations, places, buildings and map objects in a user-facing or internal product. It is separate from address autocomplete, address normalization, geocoding, company registry enrichment and routing.

## Who This Route Fits

- Product teams building store, branch, venue or service-point search.
- Map interfaces that need place search before showing an object card.
- CRM or operations teams enriching locations with public map-directory context.
- Procurement teams comparing directory search rights, storage, display and SaaS constraints.

## Quick Decision Table

| User scenario | Initial shortlist | Why | Main risk | Next Atlas document |
|---|---|---|---|---|
| Place or organization search in a 2GIS-centered product | [`2GIS Places API`](../../apis/2gis-places-api/README.md) | Atlas has an active Places profile for organizations, buildings and places in the 2GIS Search API family. | On-demand fields, storage/caching/display rights, SLA and benchmark quality need confirmation. | [`2GIS Places profile`](../../apis/2gis-places-api/README.md) |
| Place or organization search in a Yandex Maps-centered product | [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.md) | Official Yandex sources confirm a separate organization/place search API with endpoint, API-key access and public commercial packages. | License/storage wording, batch/offline rights, SLA and benchmark quality need confirmation. | [`Yandex Organization Search profile`](../../apis/yandex-maps-organization-search-api/README.md) |
| Address suggestions while typing | DaData Address APIs; Yandex Geosuggest; 2GIS Suggest | Suggestions are an autocomplete scenario, not a full place-search result set. | Suggestion rights and result follow-up calls differ by provider. | [`Address/geocoding comparison`](../../comparisons/address-normalization-geocoding/README.md) |
| Company details by INN/OGRN or registry identity | DaData; Kontur.Focus; Seldon.Basis; FTS integration | Company and counterparty data uses registry and risk data, not map place search. | Do not infer legal-entity verification from a map directory result. | [`Company verification route`](../company-verification/README.md) |
| Routing, ETA or distance matrix | Separate routing products | Routing is out of scope for current Atlas place-search profiles. | Geocoding or place search does not provide route planning by itself. | Backlog |

## Scenario Routes

### Map Directory Search

Start with 2GIS Places API and Yandex Maps Organization Search API. Choose the ecosystem that matches the map UI, required fields, coverage and permitted display/storage model. Do not declare a winner without a common benchmark and comparable contract assumptions.

### Autocomplete Before Search

Use Yandex Geosuggest or 2GIS Suggest when the user is still typing. A suggestion can feed a later place or geocoder lookup, but it is not the same as a complete organization-search result.

### Company Verification

Use the company-verification route when the user needs legal-entity identity, INN/OGRN details, counterparty risk, monitoring or official registry provenance. A place search result may help find a branch or venue, but it does not replace counterparty verification.

### Bulk Enrichment

Treat bulk or offline enrichment as a procurement blocker. Public docs reviewed by Atlas do not prove that every intended place-search response can be stored, cached, redistributed or used in SaaS without a specific contract.

## Current Research Limits

- No live credential test or benchmark was performed.
- Public SLA terms remain unknown in the active profiles.
- Storage, caching, customer-facing display, SaaS use, redistribution and resale rights require contract/legal review.
- Coverage and quality must be tested on the buyer's target cities, categories and ambiguous names.
- This route does not cover routing, distance matrices, sanctions screening or legal-entity due diligence.

## Questions Before Procurement

1. Is the target object an organization, branch, building, venue, address or legal entity?
2. Which map ecosystem will display the result?
3. Which fields must be returned and stored?
4. Will results be shown to customers, cached, redistributed or embedded in SaaS?
5. What are the daily volume, peak rate, latency and SLA requirements?
6. Is batch or offline enrichment required?
7. What benchmark sample covers target cities, categories, duplicate names and closed or moved organizations?

## Links

- Profiles: [`2GIS Places API`](../../apis/2gis-places-api/README.md), [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.md)
- Related profiles: [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.md)
- Comparison: [`Address Normalization, Address Registries and Geocoding APIs`](../../comparisons/address-normalization-geocoding/README.md)
- Procurement kit: [`Address and Geocoding API Selection`](../../procurement/address-geocoding-api-selection/README.md)

## Next Step

Read the two active place-search profiles, then use the procurement kit to request exact data rights, SLA, field matrix and pilot credentials before selecting a production provider.

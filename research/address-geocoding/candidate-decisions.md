# Address and Geocoding Candidate Decisions

[Русская версия](candidate-decisions.ru.md)

## Decision Summary

| Candidate | Active profile decision | Reason |
|---|---|---|
| DaData address APIs | Create [`dadata-address-api`](../../apis/dadata-address-api/README.md) | Official docs confirm suggestions, cleaning, direct geocoding, reverse geocoding, authentication, limits and public pricing. |
| Yandex Maps Geocoder API | Create [`yandex-maps-geocoder-api`](../../apis/yandex-maps-geocoder-api/README.md) | Official docs confirm direct/reverse geocoding, endpoint, API key auth, JSON response and commercial/free-use terms. |
| 2GIS Geocoder API | Create [`2gis-geocoder-api`](../../apis/2gis-geocoder-api/README.md) | Official docs confirm direct/reverse geocoding, API key auth, JSON response, package pricing and limits. |
| FIAS/GAR | Create [`fias-gar-data-integration`](../../apis/fias-gar-data-integration/README.md) | Official FNS sources confirm GAR/FIAS identity and registry role; profile is framed as data integration, not a turnkey REST geocoder. |
| Yandex Geosuggest | Create [`yandex-maps-geosuggest-api`](../../apis/yandex-maps-geosuggest-api/README.md) | Later official-source research confirmed a separate autocomplete product with endpoint, API key, public tariffs and object-type filters. |
| Yandex Organization Search | Create [`yandex-maps-organization-search-api`](../../apis/yandex-maps-organization-search-api/README.md) | Later official-source research confirmed a separate organization/place search product with endpoint, API key, public commercial terms and API request limit up to 50 rps. |
| 2GIS Places API | Create [`2gis-places-api`](../../apis/2gis-places-api/README.md) | Later official-source research confirmed a separate Places API for organizations, buildings and places with public package pricing. |
| 2GIS Suggest API | Create [`2gis-suggest-api`](../../apis/2gis-suggest-api/README.md) | Later official-source research confirmed a separate suggestion product for object, address, street and route-endpoint suggestions. |
| OpenStreetMap / Nominatim | Create [`nominatim-geocoder-software`](../../apis/nominatim-geocoder-software/README.md) | Later research confirmed Nominatim as an open-source geocoder software/self-hosting route, not a free production public API. |
| Geoapify Geocoding API | Create [`geoapify-geocoding-api`](../../apis/geoapify-geocoding-api/README.md) | Official-source research confirmed a hosted commercial open-data geocoding API with forward/reverse endpoints, API key, batch geocoding, public pricing and SLA wording. |
| Moscow Open Data address datasets | Backlog | Potential Moscow-specific data route, but not a replacement for national address registry or geocoder in this pass. |

## Boundary Decisions

DaData receives a separate address profile because the existing DaData API profile covers the provider's broader API family and company/counterparty use. Address suggestions, cleaning, direct geocoding and reverse geocoding have different technical, pricing and legal constraints from company autocomplete.

Yandex Maps Geocoder is scoped to geocoding only. Address suggestions belong to Geosuggest; organization search belongs to Organization Search; routing and distance matrix are separate navigation products.

2GIS Geocoder is scoped to direct and reverse geocoding. Places API and Suggest API are active separate profiles because they matter for user scenarios, but they are not folded into the Geocoder capability.

Geoapify is scoped to hosted commercial open-data geocoding. It is not public Nominatim, self-hosted Nominatim, official Russian registry validation or a Russia-specific cleaning API.

FIAS/GAR is an official registry and integration route. It is not documented here as a commercial low-latency address suggestion API.

## Evidence Standard

All active profiles are based on official or primary sources reviewed on 2026-07-29. No live credential testing was performed, no quality benchmark was run, and no profile receives a Gold maturity level. Later rows in this decision log reflect subsequent 2026-07-29 deepening of the same address/geocoding direction.

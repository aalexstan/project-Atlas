# Address and Geocoding Candidate Decisions

[Русская версия](candidate-decisions.ru.md)

## Decision Summary

| Candidate | Active profile decision | Reason |
|---|---|---|
| DaData address APIs | Create [`dadata-address-api`](../../apis/dadata-address-api/README.md) | Official docs confirm suggestions, cleaning, direct geocoding, reverse geocoding, authentication, limits and public pricing. |
| Yandex Maps Geocoder API | Create [`yandex-maps-geocoder-api`](../../apis/yandex-maps-geocoder-api/README.md) | Official docs confirm direct/reverse geocoding, endpoint, API key auth, JSON response and commercial/free-use terms. |
| 2GIS Geocoder API | Create [`2gis-geocoder-api`](../../apis/2gis-geocoder-api/README.md) | Official docs confirm direct/reverse geocoding, API key auth, JSON response, package pricing and limits. |
| FIAS/GAR | Create [`fias-gar-data-integration`](../../apis/fias-gar-data-integration/README.md) | Official FNS sources confirm GAR/FIAS identity and registry role; profile is framed as data integration, not a turnkey REST geocoder. |
| Yandex Geosuggest | Do not create in this pass | Separate product from Geocoder; relevant to address input, but this pass focuses on mandatory candidates and avoids shallow expansion. |
| 2GIS Places API | Do not create in this pass | Official product for organization/place search, but separate from Geocoder and not enough time for a full independent profile. |
| 2GIS Suggest API | Do not create in this pass | Separate product for real-time suggestions; include as related product only. |
| OpenStreetMap / Nominatim | Backlog | Useful open-data route, but not researched deeply enough in this block. |
| Moscow Open Data address datasets | Backlog | Potential Moscow-specific data route, but not a replacement for national address registry or geocoder in this pass. |

## Boundary Decisions

DaData receives a separate address profile because the existing DaData API profile covers the provider's broader API family and company/counterparty use. Address suggestions, cleaning, direct geocoding and reverse geocoding have different technical, pricing and legal constraints from company autocomplete.

Yandex Maps Geocoder is scoped to geocoding only. Address suggestions belong to Geosuggest; organization search belongs to Organization Search; routing and distance matrix are separate navigation products.

2GIS Geocoder is scoped to direct and reverse geocoding. Places API and Suggest API are mentioned because they matter for user scenarios, but they are not folded into the Geocoder capability without proof.

FIAS/GAR is an official registry and integration route. It is not documented here as a commercial low-latency address suggestion API.

## Evidence Standard

All active profiles are based on official or primary sources reviewed on 2026-07-29. No live credential testing was performed, no quality benchmark was run, and no profile receives a Gold maturity level.

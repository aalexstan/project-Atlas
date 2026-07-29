# Address Normalization and Geocoding Comparison Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| DaData documents address suggestions, address cleaning, direct geocoding and reverse geocoding as address-related API capabilities. | https://dadata.ru/api/ | 2026-07-29 | verified | Detailed endpoint evidence is in the DaData address profile. |
| DaData Suggestions should not be used for automatic processing of address files/databases. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Important scenario separator. |
| Yandex Geosuggest is documented as a server-side API for search suggestions for geographic objects and/or organizations. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Separate from Yandex Geocoder. |
| Yandex Geosuggest request docs list endpoint, API key, text query, result limit and supported object types. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Autocomplete evidence. |
| Yandex Geocoder supports direct and reverse geocoding. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Not address normalization. |
| Yandex free-use Geocoder terms include 1,000 requests/day and Yandex Maps display restrictions. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Material data-rights condition. |
| Yandex Organization Search / Geosearch API is documented for searching organizations and geographic objects. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Place/organization search scenario. |
| Yandex Organization Search request docs list endpoint, API key, required `text` and `lang`, and JSON/XML format support. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Separate from Geosuggest and Geocoder profiles. |
| Yandex commercial docs list public Organization Search request packages. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | API commercial terms, not web-product pricing. |
| Yandex Places API docs list an API request limit of up to 50 rps. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Production suitability still needs contract/SLA review. |
| 2GIS Search docs separate Geocoder, Places and Suggest APIs. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Product boundary. |
| 2GIS Suggest API documents object, address, street and route-endpoint suggestions. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Suggest/autocomplete scenario. |
| 2GIS Places API searches organizations, buildings and places. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Place search is separate from geocoding. |
| 2GIS Geocoder supports direct and reverse geocoding. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON with API key. |
| 2GIS Search pricing and limits are publicly documented. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Package pricing and 600 units/minute. |
| 2GIS WebAPI offer says caching is not provided and restricts extraction/storage outside contract terms. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Data-rights blocker across 2GIS Search products. |
| Public Nominatim policy forbids autocomplete, limits public use to max 1 request/second and requires own service for primary geocoding apps/resellers. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Public instance is not a free production API. |
| Nominatim Search and Reverse APIs are documented for geocoding. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Software/API capability; self-hosting route needs ops. |
| Nominatim installation/import/update/deployment docs describe production operations requirements including high-memory full-planet imports, import styles, replication updates and production frontend deployment. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Self-hosting operations blocker. |
| OpenStreetMap data requires attribution and is licensed under ODbL. | https://www.openstreetmap.org/copyright | 2026-07-29 | verified | Legal/data-rights blocker. |
| FNS/FIAS pages identify GAR as the official Russian address registry and FIAS as the system operated by FNS. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Registry route. |
| FNS open-data catalog lists GAR/FIAS as dataset `7707329152-fias` with XML data, structure ZIP, weekly updates and previous releases. | https://www.nalog.gov.ru/opendata/7707329152-fias/ | 2026-07-29 | verified | Open-data route details. |
| FIAS developer section exposes file downloads, SMEV and API services entries, but detailed API specification was not visible in reviewed static pages. | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Unknowns remain visible. |
| FNS archived material describes weekly file downloads, daily SMEV publication and online API batch provision by request as integration routes. | https://www.nalog.gov.ru/rn77/news/activities_fts/13824755/ | 2026-07-29 | verified | Confirms channel split, not full method details. |

## Live Testing

No Atlas live test, benchmark or contract review was performed for this comparison.

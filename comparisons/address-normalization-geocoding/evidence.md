# Address Normalization and Geocoding Comparison Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| DaData documents address suggestions, address cleaning, direct geocoding and reverse geocoding as address-related API capabilities. | https://dadata.ru/api/ | 2026-07-29 | verified | Detailed endpoint evidence is in the DaData address profile. |
| DaData Suggestions should not be used for automatic processing of address files/databases. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Important scenario separator. |
| Yandex Geocoder supports direct and reverse geocoding. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Not address normalization. |
| Yandex free-use Geocoder terms include 1,000 requests/day and Yandex Maps display restrictions. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Material data-rights condition. |
| 2GIS Search docs separate Geocoder, Places and Suggest APIs. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Product boundary. |
| 2GIS Geocoder supports direct and reverse geocoding. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON with API key. |
| 2GIS Search pricing and limits are publicly documented. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Package pricing and 600 units/minute. |
| FNS/FIAS pages identify GAR as the official Russian address registry and FIAS as the system operated by FNS. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Registry route. |
| FIAS developer section exposes file downloads, SMEV and API services entries, but detailed API specification was not visible in reviewed static pages. | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Unknowns remain visible. |

## Live Testing

No Atlas live test, benchmark or contract review was performed for this comparison.

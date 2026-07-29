# 2GIS Geocoder API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| 2GIS Search APIs include Geocoder for address<->coordinates, Places for objects, and Suggest for input hints. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Product boundaries are explicit. |
| Geocoder API allows direct and reverse geocoding. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Core capability. |
| Geocoder requests use GET query parameters and JSON responses. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON model. |
| Direct geocoding endpoint example uses `https://catalog.api.2gis.com/3.0/items/geocode?q=...&key=YOUR_KEY`. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | API key parameter. |
| Reverse geocoding endpoint example uses `lat`, `lon` and `key`. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Coordinates to address/object. |
| Access requires Platform Manager key, demo key or subscription. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Onboarding flow. |
| Demo Search-service limit is 1,000 requests and demo key is available for one month. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | No Atlas live test. |
| Search services have 600 units/minute limit. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Applies to Geocoder, Places, Suggest, etc. |
| Geocoder public package prices include 4,700 RUB for 10,000 units and 70,000 RUB for 1,000,000 units. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Monthly billing units table. |
| Places API searches organizations, buildings and places. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Separate product from Geocoder. |
| Some fields and methods are available on demand for extra cost. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Includes selected FIAS/FNS/OKATO/OKTMO fields. |
| Directory data is updated monthly. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | provider_reported | Atlas did not independently verify update cadence. |
| Storage/caching/use outside contract is restricted by official WebAPI offer. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Exact rights need contract review. |
| OpenAPI/Swagger specification was not found in reviewed public docs. | Official docs reviewed | 2026-07-29 | unknown | API reference exists, but not OpenAPI status. |
| Public SLA was not found in reviewed docs. | Official docs reviewed | 2026-07-29 | unknown | Ask during procurement. |

## Live Testing

No Atlas credentialed live test was performed.

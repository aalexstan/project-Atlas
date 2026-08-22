# Yandex Maps Geocoder API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| Geocoder API can determine coordinates by address and address by coordinates. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Direct and reverse geocoding. |
| Endpoint is `https://geocode-maps.yandex.ru/v1` with `apikey`, `geocode` and `lang` parameters. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | API key from developer dashboard. |
| `geocode` can be an address/name or coordinates. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Determines direct or reverse mode. |
| Response format is JSON. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | `format=json`. |
| Reverse geocoding supports `kind` filters such as house, street, metro, district and locality. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Optional parameter. |
| `results` defaults to 10 and maximum is 50. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Request parameter docs. |
| Response docs define precision values and error examples for 400, 403 and 429. | https://yandex.com/maps-api/docs/geocoder-api/response.html | 2026-07-29 | verified | Precision is not registry validation. |
| Free-use Geocoder limit is 1,000 requests/day. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Applies under free-use terms. |
| Free-use Geocoder results are tied to Yandex Maps display and must not be shown on third-party maps. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Material data-rights restriction. |
| Paid annual tariffs start at 195,000 RUB Standard and 226,200 RUB Extended for 1,000 requests/day. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Russian tariff page. |
| Test period tariff allows 100 requests/day for up to 7 days without minimum payment. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Not a live Atlas test. |
| Requests above 1,000,000/day require a quote. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Vendor contact required. |
| OpenAPI/Swagger specification was not found in reviewed public docs. | Official docs reviewed | 2026-07-29 | unknown | Needs recheck before Gold. |
| Public SLA was not found in reviewed public docs. | Official docs reviewed | 2026-07-29 | unknown | Ask during procurement. |

## Live Testing

No Atlas credentialed live test was performed.

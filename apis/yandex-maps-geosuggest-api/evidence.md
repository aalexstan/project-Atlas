# Yandex Maps Geosuggest API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| Geosuggest is an API for entering and verifying organization names and addresses. | https://yandex.com/maps-api/products/suggest-api | 2026-07-29 | provider_reported | Product-page positioning; not an independent quality benchmark. |
| Yandex legal terms define API Geosuggest as a server-side API for automated search suggestions for geographic objects and/or organizations. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Product boundary distinct from Geocoder and Organization Search. |
| Request endpoint is `https://suggest-maps.yandex.ru/v1/suggest`. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | HTTP GET query API. |
| `apikey` and `text` are required request parameters. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | API key is issued by Yandex developer tooling. |
| `results` has a maximum of 10 and default of 7. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | UI autocomplete implication. |
| Supported `types` include `biz`, `geo`, `street`, `locality`, `house` and `entrance`. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Shows both organization and geographic/address suggestions. |
| `attrs=uri` can return a URI for use in a Geocoder API request. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Confirms relation to Geocoder, not merger. |
| Response contains `results` with title/subtitle/tags/address and optional `uri`. | https://yandex.com/maps-api/docs/suggest-api/response.html | 2026-07-29 | verified | JSON response. |
| Public Geosuggest tariffs list annual and monthly RUB packages and a test period. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | API tariff page, not web-product price. |
| Annual Standard license starts at 180,000 RUB for 10,000 requests/day. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | Checked against tariff table. |
| Annual Extended license with data storage starts at 208,800 RUB for 10,000 requests/day. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | Storage rights still require contract review. |
| Test period is 100 requests/day for up to 7 days with no minimum payment. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | This is not an Atlas live test. |

## Live Testing

No Atlas credentialed live test was performed.

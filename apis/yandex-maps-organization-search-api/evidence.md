# Yandex Maps Organization Search API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| Yandex publishes an official Organization Search / Geosearch API product page. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Official product identity. |
| The API searches organizations and geographic objects. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Product purpose. |
| The API has public documentation. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Documentation route. |
| The request endpoint is `https://search-maps.yandex.ru/v1/`. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Request reference. |
| API-key authentication uses the `apikey` request parameter. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Authentication model. |
| `text` and `lang` are required request parameters. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Required fields. |
| JSON is the default response format and XML can be requested with `format=xml`. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Format support. |
| Commercial documentation lists public request packages for organization search. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | API commercial terms, not web-product pricing. |
| Commercial documentation lists annual Basic pricing from 195,000 RUB for 1,000 requests/day and monthly Basic pricing from 20,800 RUB for 1,000 requests/day. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | Verify before procurement. |
| Public API documentation states an API request limit of up to 50 requests/second. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Production suitability still needs contract/SLA review. |
| Official FAQ describes a 14-day trial key by request with a 500 requests/day limit. | https://yandex.com/dev/commercial/doc/en/concepts/faq | 2026-07-29 | provider_reported | Atlas did not request or use trial credentials. |
| Public official pages appear inconsistent about Basic/Advanced or storage-capable license wording. | Official Yandex pages reviewed | 2026-07-29 | observed | Treat storage/data-use rights as contract-review blocker. |
| Public SLA was not found in reviewed official pages. | Official Yandex pages reviewed | 2026-07-29 | unknown | Procurement blocker. |
| OpenAPI/Swagger was not found in reviewed official pages. | Official Yandex pages reviewed | 2026-07-29 | unknown | Developer-experience blocker. |

## Live Testing

No Atlas credentialed request, quality benchmark or live API test was performed.

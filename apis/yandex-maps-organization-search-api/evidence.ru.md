# Evidence Yandex Maps Organization Search API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Заметка |
|---|---|---|---|---|
| Yandex публикует официальную product page Organization Search / Geosearch API. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Official product identity. |
| API предназначен для поиска организаций и geographic objects. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Product purpose. |
| У API есть public documentation. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Documentation route. |
| Request endpoint: `https://search-maps.yandex.ru/v1/`. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Request reference. |
| API-key authentication использует request parameter `apikey`. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Authentication model. |
| `text` и `lang` являются required request parameters. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Required fields. |
| JSON является default response format, XML можно запросить через `format=xml`. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Format support. |
| Commercial documentation содержит public request packages для organization search. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | API commercial terms, not web-product pricing. |
| Commercial documentation указывает annual Basic pricing from 195,000 RUB for 1,000 requests/day и monthly Basic pricing from 20,800 RUB for 1,000 requests/day. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | Проверять перед закупкой. |
| Public API documentation states an API request limit of up to 50 requests/second. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Production suitability still needs contract/SLA review. |
| Official FAQ describes a 14-day trial key by request with a 500 requests/day limit. | https://yandex.com/dev/commercial/doc/en/concepts/faq | 2026-07-29 | provider_reported | Atlas did not request or use trial credentials. |
| Public official pages appear inconsistent about Basic/Advanced или storage-capable license wording. | Official Yandex pages reviewed | 2026-07-29 | observed | Storage/data-use rights считаются contract-review blocker. |
| Public SLA не найден в reviewed official pages. | Official Yandex pages reviewed | 2026-07-29 | unknown | Procurement blocker. |
| OpenAPI/Swagger не найден в reviewed official pages. | Official Yandex pages reviewed | 2026-07-29 | unknown | Developer-experience blocker. |

## Live Testing

Atlas credentialed request, quality benchmark или live API test не проводились.

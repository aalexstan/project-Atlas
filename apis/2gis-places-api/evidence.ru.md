# Evidence 2GIS Places API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| 2GIS Search APIs разделяют Geocoder, Places и Suggest. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Граница продукта. |
| Places API ищет организации, здания и места. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Core scope. |
| Places API поддерживает поиск по названию компании, категории, геотегам, атрибутам, телефону/сайту и другим критериям. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Search semantics. |
| Places API использует GET requests с query parameters и JSON responses. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Technical access. |
| Для подсказок при поиске объектов нужно использовать Suggest API. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Связь продуктов. |
| Некоторые Places methods и fields доступны on demand и требуют дополнительного платного доступа. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Procurement blocker. |
| Access key получается в Platform Manager как demo key или subscription. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Authentication/onboarding. |
| Публичная цена Places API начинается от 6 700 рублей за 10 000 units/month. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | API-тариф, не цена веб-продукта. |
| Лимит Places API — 600 Search units/minute; demo limit — 1 000 total requests. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Public pricing/limits page. |
| 2GIS заявляет ежемесячное обновление справочника. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | provider_reported | Не benchmarked Atlas. |
| WebAPI offer говорит, что кэширование не предусмотрено, и ограничивает извлечение/хранение вне договора. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Data-rights blocker. |

## Live Testing

Atlas не проводил credentialed live test.

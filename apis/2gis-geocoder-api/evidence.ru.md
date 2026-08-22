# Доказательства по 2GIS Geocoder API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| 2GIS Search APIs включают Geocoder для address<->coordinates, Places для объектов и Suggest для подсказок. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Границы продуктов явные. |
| Geocoder API выполняет прямое и обратное геокодирование. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Основная возможность. |
| Запросы Geocoder используют GET query parameters, ответы JSON. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON model. |
| Пример direct endpoint: `https://catalog.api.2gis.com/3.0/items/geocode?q=...&key=YOUR_KEY`. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | API key parameter. |
| Пример reverse endpoint использует `lat`, `lon` и `key`. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Coordinates to address/object. |
| Доступ требует ключ Platform Manager, demo key или subscription. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Onboarding flow. |
| Demo Search limit - 1 000 запросов, demo key доступен на один месяц. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Это не live test Atlas. |
| Search services имеют лимит 600 units/minute. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Для Geocoder, Places, Suggest и др. |
| Публичные цены Geocoder включают 4 700 руб. за 10 000 units и 70 000 руб. за 1 000 000 units. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Monthly billing units table. |
| Places API ищет организации, здания и места. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Отдельный продукт от Geocoder. |
| Некоторые поля и методы доступны on demand за дополнительную стоимость. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | Включая отдельные FIAS/FNS/OKATO/OKTMO поля. |
| Каталог обновляется ежемесячно. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | provider_reported | Atlas не проверял cadence независимо. |
| Хранение/кэширование/использование вне договора ограничены официальной офертой WebAPI. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Конкретные права нужно подтверждать договором. |
| OpenAPI/Swagger не найден в просмотренных публичных docs. | Official docs reviewed | 2026-07-29 | unknown | API reference есть, но OpenAPI status неизвестен. |
| Публичный SLA не найден в просмотренных docs. | Official docs reviewed | 2026-07-29 | unknown | Вопрос закупки. |

## Live Testing

Credentialed live test Atlas не проводил.

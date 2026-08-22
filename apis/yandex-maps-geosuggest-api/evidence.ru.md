# Evidence Yandex Maps Geosuggest API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| Geosuggest описан как API для ввода и проверки названий организаций и адресов. | https://yandex.com/maps-api/products/suggest-api | 2026-07-29 | provider_reported | Позиционирование продукта; не независимый benchmark качества. |
| Условия Яндекса определяют API Геосаджеста как серверный API для автоматизированного получения поисковых подсказок геообъектов и/или организаций. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Граница отличается от Geocoder и Organization Search. |
| Request endpoint: `https://suggest-maps.yandex.ru/v1/suggest`. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | HTTP GET query API. |
| `apikey` и `text` обязательны. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | API key выдается инструментами разработчика Яндекса. |
| `results` имеет максимум 10 и default 7. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Важно для UX autocomplete. |
| Поддерживаемые `types` включают `biz`, `geo`, `street`, `locality`, `house`, `entrance`. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Есть и организационные, и географические/адресные подсказки. |
| `attrs=uri` может вернуть URI для запроса в Geocoder API. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Подтверждает связь с Geocoder, но не объединение продуктов. |
| Ответ содержит `results` с title/subtitle/tags/address и опциональным `uri`. | https://yandex.com/maps-api/docs/suggest-api/response.html | 2026-07-29 | verified | JSON response. |
| Публичные тарифы Geosuggest содержат годовые и месячные RUB-пакеты и тестовый период. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | Это API-тарифы, не цена веб-продукта. |
| Годовая Standard license начинается от 180 000 рублей за 10 000 запросов/сутки. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | По тарифной таблице. |
| Годовая Extended license с хранением данных начинается от 208 800 рублей за 10 000 запросов/сутки. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | Права хранения всё равно нужно проверять по договору. |
| Тестовый период: 100 запросов/сутки до 7 суток без минимального платежа. | https://yandex.ru/dev/tariffs/doc/ru/geosuggest/prices/ | 2026-07-29 | verified | Это не Atlas live test. |

## Live Testing

Atlas не проводил credentialed live test.

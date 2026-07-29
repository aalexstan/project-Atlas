# 2GIS Suggest API

[English version](README.md)

> Продукт 2GIS Search API для autocomplete-подсказок в интерфейсах поиска по карте и каталогу.

## Статус исследования

| Поле | Значение |
|---|---|
| Уровень | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | 2GIS |
| Статус продукта | Active |
| Live test с credentials | Не проводился |

## Краткий вывод

**Лучше всего подходит:** для UX autocomplete в продуктах на 2GIS Search, особенно когда подсказки должны вести к объектам каталога 2GIS, адресам, улицам или конечным точкам маршрута.

**Не подходит:** когда нужны прямое/обратное геокодирование, полные карточки организаций, проверка адреса по официальному реестру, offline enrichment или хранение без договорного подтверждения.

**Итог:** Suggest API — отдельный продукт 2GIS Search. Его нужно оценивать вместе с [`2GIS Places API`](../2gis-places-api/README.ru.md) и [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md), а не смешивать с ними.

## Граница продукта

Профиль покрывает:

- подсказки при вводе пользовательского запроса;
- object suggestions для catalog-driven поиска;
- адресные и уличные подсказки через `suggest_type`;
- route-endpoint suggestions как вспомогательный UX.

Профиль не покрывает:

- преобразование адреса в координаты или координат в адрес;
- получение полной информации об организации/месте после подсказки;
- построение маршрута;
- владение официальным российским адресным реестром.

## Сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| Autocomplete поисковой строки в 2GIS UI | Strong | Документация описывает Suggest как инструмент завершения пользовательского ввода. |
| Адресные подсказки | Medium | Документированы `suggest_type=address` и `suggest_type=street`. |
| Подсказки организаций/мест | Medium | Object suggestions можно связывать с Places API для полного объекта. |
| Прямое/обратное геокодирование | Weak | Используйте 2GIS Geocoder API. |
| Массовая обработка | Weak | Семантика и права Suggest ориентированы на пользовательский ввод; batch не подтвержден. |
| Маршрутизация | Not applicable | Построение маршрута вне границ Suggest API. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET |
| Example endpoint | `https://catalog.api.2gis.com/3.0/items` |
| Required access | API key |
| Example parameters | `q`, `location`, `key` |
| Response format | JSON |
| Default suggestion type | `object` |
| Documented suggestion types | `object`, `address`, `street`, `route_endpoint` |
| OpenAPI / Swagger | Не найдено в публичных документах |
| Deployment | Cloud public endpoints; provider-reported On-Premise для текущих методов |

## Цены, лимиты и права

| Параметр | Подтвержденное значение | Статус |
|---|---|---|
| Модель цены | Успешные запросы / месячные units | verified |
| Минимальный публичный пакет | 7 000 рублей за 100 000 units/month Suggest API | verified |
| Per-minute limit | 600 Search units/minute | verified |
| Demo limit | 1 000 total Search-service requests for Suggest API | verified |
| Demo period | Demo key на один месяц | verified |
| Directory freshness | Ежемесячное обновление справочника заявлено поставщиком | provider_reported |
| Caching | В WebAPI offer указано, что кэширование не предусмотрено | verified |
| SLA | Не найдено публично в этом исследовании | unknown |

## Коммерческие и юридические замечания

- Suggest API и Places API имеют разные тарифные строки; их нужно считать отдельно.
- Оферта 2GIS WebAPI ограничивает извлечение, хранение, обработку, изменение и распространение вне условий договора.
- В проверенной оферте кэширование явно не предусмотрено.
- SaaS use, показ клиентам и redistribution требуют договорного review.

## Альтернативы

| Альтернатива | Когда лучше | Главный компромисс |
|---|---|---|
| [`2GIS Places API`](../2gis-places-api/README.ru.md) | Нужны полные результаты поиска организаций, зданий или мест | Другая тарификация и on-demand поля. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Нужно преобразование адреса в координаты или координат в адрес | Это не autocomplete API. |
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Основная задача — российский ввод и чистка адресов | Меньше связан с каталогом 2GIS. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.ru.md) | Карточный ecosystem — Яндекс | Применяются требования лицензии и показа Яндекса. |

## Сценарная рекомендация

Используйте 2GIS Suggest, когда ввод пользователя должен вести в опыт поиска/каталога 2GIS. Для чистки адресов, геокодирования, полных карточек мест и маршрутизации выбирайте соответствующий отдельный продукт и проверяйте права на данные.

## Evidence

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

# 2GIS Places API

[English version](README.md)

> Продукт 2GIS Search API для поиска организаций, зданий и мест.

## Статус исследования

| Поле | Значение |
|---|---|
| Уровень | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | 2GIS |
| Статус продукта | Active |
| Live test с credentials | Не проводился |

## Краткий вывод

**Лучше всего подходит:** для поиска организаций, зданий и мест в продуктах, где нужен контекст справочника 2GIS.

**Не подходит:** когда главная задача — каноническая нормализация адресов, прямое/обратное геокодирование, только адресный autocomplete, маршрутизация или владение официальным реестром.

**Итог:** Places API — продукт 2GIS, который стоит оценивать для организаций, зданий, мест и справочных атрибутов. Он связан с адресным направлением потому, что пользователи часто смешивают поиск мест и проверку адреса.

## Граница продукта

Профиль покрывает:

- поиск организаций, зданий и мест;
- поиск по тексту, категории, геотегам, атрибутам, телефону/сайту и связанным критериям;
- дополнительные on-demand методы и поля, где они документированы;
- связь с Suggest API для подсказок.

Профиль не покрывает:

- autocomplete как основной UX;
- прямое/обратное геокодирование;
- маршрутизацию;
- официальную интеграцию GAR/FIAS.

## Сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| Поиск организаций и мест | Strong | Документация говорит, что Places API ищет организации, здания и места. |
| Map search с контекстом каталога | Strong | Справочник 2GIS — ядро продукта. |
| Адресные подсказки | Medium | Для подсказок перед Places lookup используйте Suggest API. |
| Адрес -> координаты | Weak | Используйте 2GIS Geocoder API. |
| Проверка по официальному реестру | Weak | Places results не являются официальным российским адресным реестром. |
| Массовое enrichment | Medium/unknown | Цены публичны, но storage и batch rights требуют договора. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET |
| API family | 2GIS Search APIs |
| Required access | API key |
| Response format | JSON |
| Main object types | Organizations, buildings, places |
| Search examples | Company name, business area, geotags, attributes, telephone, website, category, city |
| Related autocomplete | 2GIS Suggest API |
| On-demand methods | `bysite`, `byphone`, `byitin`, `bytradelicense`, `byfias` |
| OpenAPI / Swagger | Не найдено в публичных документах |

## Цены, лимиты и права

| Параметр | Подтвержденное значение | Статус |
|---|---|---|
| Модель цены | Успешные запросы / месячные units | verified |
| Минимальный публичный пакет | 6 700 рублей за 10 000 Places API units/month | verified |
| Per-minute limit | 600 Search units/minute | verified |
| Demo limit | 1 000 total Search-service requests for Places API | verified |
| Demo period | Demo key на один месяц | verified |
| On-demand fields/methods | Некоторые поля и методы требуют дополнительного платного доступа | verified |
| Directory freshness | Ежемесячное обновление справочника заявлено поставщиком | provider_reported |
| Caching | В WebAPI offer указано, что кэширование не предусмотрено | verified |
| SLA | Не найдено публично в этом исследовании | unknown |

## Коммерческие и юридические замечания

- Places API может требовать дополнительный платный доступ к полям/методам: contact groups, ITIN, FIAS codes, OKATO/OKTMO и другим расширенным данным.
- Оферта 2GIS WebAPI ограничивает извлечение, хранение, обработку, изменение и распространение вне условий договора.
- В проверенной оферте кэширование явно не предусмотрено.
- SaaS embedding, redistribution и customer-facing display требуют юридического и договорного review.

## Альтернативы

| Альтернатива | Когда лучше | Главный компромисс |
|---|---|---|
| [`2GIS Suggest API`](../2gis-suggest-api/README.ru.md) | Нужны только подсказки поисковой строки до выбора результата | Это не API полной карточки места. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Нужно преобразование адресов и координат | Это не API каталога организаций. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.ru.md) | UX подсказок должен использовать данные Яндекс Карт | Границы продукта и лицензия отличаются. |
| [`DaData API`](../dadata/README.ru.md) | Задача — российские company/counterparty data | Другая модель данных и закупочный вопрос. |

## Сценарная рекомендация

Выбирайте 2GIS Places API, когда решение на самом деле про поиск мест и организаций. Не смешивайте его с нормализацией адресов и геокодированием, а перед закупкой запросите method/field matrix.

## Evidence

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

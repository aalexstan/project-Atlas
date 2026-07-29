# OpenCage Geocoding API

[English version](README.md)

> Hosted commercial geocoding API для worldwide forward и reverse geocoding на основе open data.

## Статус исследования

| Поле | Значение |
|---|---|
| Уровень | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | OpenCage GmbH |
| Статус продукта | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит для:** команд, которым нужен hosted international geocoder, public API pricing, API-key access, storage-friendly wording и commercial alternative to public or self-hosted Nominatim.

**Не подходит, когда:** нужна российская registry validation, address cleaning/normalization, fuzzy autocomplete, routing или batch API, принимающий много locations в одном request.

**Итог:** OpenCage — сильный дополнительный hosted open-data geocoding candidate для address/geocoding comparison. Его нужно сравнивать с Geoapify, LocationIQ, Yandex, 2GIS, DaData и self-hosted Nominatim по geography, precision, rights, ODbL/attribution obligations, SLA и benchmark quality.

## Граница продукта

Эта карточка покрывает:

- forward geocoding;
- reverse geocoding;
- public pricing, limits, storage wording и open-data source/credit notes;
- OpenAPI availability по official docs OpenCage.

Эта карточка не покрывает:

- OpenCage Geosearch/autosuggest как отдельный продукт;
- Russian GAR/FIAS registry validation;
- address cleaning или canonicalization;
- routing, matrices или distance calculations;
- legal advice по ODbL, attribution или derived databases.

## Сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| International forward/reverse geocoding | Strong | Official docs describe worldwide geocoding over REST. |
| Hosted open-data geocoding | Strong | Official credits list OpenStreetMap and other open-data sources. |
| Permanent storage of API results | Strong, но нужен legal review | Provider docs say API results can be stored permanently; users still accept data-license responsibility. |
| Large batch geocoding | Medium | API is one location per request; spreadsheets and parallel requests are documented routes. |
| Address autocomplete | Weak в этой карточке | Provider says autosuggest belongs to Geosearch, not Geocoding API. |
| Official registry validation | Weak | Не официальный registry route. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET |
| Endpoint pattern | `https://api.opencagedata.com/geocode/v1/{format}` |
| Authentication | API key в query parameter `key` |
| Required query | `q` as address/placename or latitude, longitude |
| Response formats | JSON, GeoJSON, XML and Google-compatible JSON |
| Coordinate system | WGS 84 / EPSG:4326 |
| OpenAPI | OpenAPI specification link present in official docs |

## Цены, лимиты и права

| Пункт | Подтверждённое значение | Статус |
|---|---|---|
| Free trial | 2,500 requests/day; 1 request/second; testing only; no credit card | verified |
| Monthly paid examples | X-Small `zł 205/mo`, Small `zł 510/mo`, Medium `zł 2050/mo`, Large `zł 4100/mo` на reviewed pricing page | verified |
| Enterprise | from `zł 8200/mo`; custom limits, pricing, terms and SLAs | verified |
| Paid RPS examples | 15, 20, 25 and 40 requests/second by plan | verified |
| Paid daily request examples | 10,000, 30,000, 125,000 and 300,000 requests/day by plan | verified |
| Batch/bulk API | Multiple locations per API request are not supported | verified |
| Spreadsheet upload | Supported; free trial limited to 100 rows; paying customers can upload larger files | verified |
| Storage/caching | Provider says results can be stored permanently | provider_reported |
| Data licenses | Users must respect returned data licenses, especially OSM ODbL | verified |

## Коммерческие и юридические заметки

- ODbL, attribution, derived databases, redistribution, resale, SaaS embedding, API proxying и customer-facing display нужно проверять юридически и договорно.
- Public pricing в этом проходе показан в `zł`; Atlas не пересчитывает валюту и не предполагает negotiated pricing.
- Geocoding API не является fuzzy autocomplete. Для autocomplete/typeahead OpenCage указывает Geosearch.
- One-location-per-request позволяет high-volume workloads через parallelization, но меняет engineering и audit design по сравнению с asynchronous batch APIs.
- Live benchmark по target countries, languages, house-level precision или latency не проводился.

## Альтернативы

| Альтернатива | Когда лучше | Главный trade-off |
|---|---|---|
| [`Geoapify Geocoding API`](../geoapify-geocoding-api/README.ru.md) | Нужен hosted open-data geocoding with asynchronous batch jobs | ODbL/attribution и batch failure semantics still need review. |
| [`LocationIQ Geocoding API`](../locationiq-geocoding-api/README.ru.md) | Нужны hosted geocoding плюс autocomplete с public USD plan examples | Batch — one address per request unless provider-arranged; storage/caching и ODbL rights требуют review. |
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.ru.md) | Нужен self-hosted OSM geocoding control | Вы владеете import, updates, operations и ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Central Yandex Maps display and Russia/CIS ecosystem | Storage/display rights and map coupling need review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Central 2GIS map/catalog workflows | Caching/storage rights and field access need review. |
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Важны Russian address cleaning и GAR/FIAS-linked fields | Russia-focused and not an international open-data geocoder. |

## Рекомендация по сценарию

Добавляйте OpenCage в shortlist, когда нужен hosted international open-data geocoding, storage-friendly public wording и простой GET API. Не считайте его address-cleaning, autocomplete, routing или registry-validation product.

## Доказательства

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

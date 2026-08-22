# LocationIQ Geocoding API

[English version](README.md)

> Hosted commercial geocoding и autocomplete API suite для forward geocoding, reverse geocoding, address autocomplete и nearby POI lookup.

## Статус исследования

| Поле | Значение |
|---|---|
| Maturity | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | Unwired Labs / LocationIQ |
| Статус продукта | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит:** командам, которым нужен managed commercial route для international forward/reverse geocoding и address autocomplete, с публичными тарифами, access-token authentication, документированными US/EU geocoding endpoints и provider-published guidance по storage/caching.

**Не подходит, если:** нужна Russian registry validation, DaData-style address cleaning, official GAR/FIAS source, multi-address batch API call, routing как основная задача или production rights без проверки attribution, storage, SaaS и redistribution terms.

**Итог:** LocationIQ — правдоподобный дополнительный hosted open-data/commercial geocoding candidate рядом с Geoapify и OpenCage. Его нужно сравнивать по precision, geography, data rights, caching model, attribution, SLA, batch design и legal treatment of derived data.

## Граница продукта

Эта карточка покрывает:

- Search / Forward Geocoding;
- Reverse Geocoding;
- Autocomplete;
- Nearby POI как related capability, а не полноценную замену directory/search product;
- public pricing, quotas, rate limits, caching и batch boundaries.

Эта карточка не покрывает:

- routing APIs, matrices, map matching или route optimization;
- registry-quality address validation;
- Russia-specific address cleaning или canonicalization;
- public Nominatim, self-hosted Nominatim или другие LocationIQ-hosted alternatives;
- юридические выводы по OpenStreetMap/ODbL, attribution, derived databases или redistribution.

## Лучшие сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| International forward geocoding | Strong | Официальные docs определяют Search / Forward Geocoding и показывают US/EU endpoint patterns. |
| International reverse geocoding | Strong | Официальные docs определяют Reverse Geocoding и перечисляют required `lat`, `lon` и `key` parameters. |
| Address autocomplete | Strong | Официальные docs показывают отдельный `/v1/autocomplete` endpoint для type-ahead suggestions. |
| Nearby POI lookup | Medium | Официальные docs перечисляют Nearby POI, но карточка не считает его полноценной заменой organization/catalog search. |
| Batch geocoding | Medium/weak | Provider support says one address per request; concurrent calls allowed within plan limits. |
| Official Russian registry validation | Weak | Это не official FIAS/GAR route и не address-cleaning profile. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET |
| Forward geocoding endpoints | `https://us1.locationiq.com/v1/search` и `https://eu1.locationiq.com/v1/search` |
| Reverse geocoding endpoints | `https://us1.locationiq.com/v1/reverse` и `https://eu1.locationiq.com/v1/reverse` |
| Autocomplete endpoint | `https://api.locationiq.com/v1/autocomplete` |
| Authentication | Access token / API key в query parameter `key` |
| Request formats | Query parameters; free-form, structured и postal-code forms для Search |
| Response formats | JSON, XML и `xmlv1.1` в geocoding docs; Autocomplete examples используют JSON |
| API reference | Public API Reference и Postman collection documented |

## Цены, лимиты и права

| Пункт | Подтвержденное значение | Статус |
|---|---|---|
| Free plan | 5,000 requests/day; 2 requests/second; 60 requests/minute; limited commercial use with attribution | verified |
| Developer plan example | USD 100/month; 25,000 requests/day; 20 requests/second | verified |
| Startup plan example | USD 200/month; 60,000 requests/day; 22 requests/second | verified |
| Growth Plus example | USD 500/month; 7.5 million requests/month; 30 requests/second | verified |
| Business Plus example | USD 950/month; 30 million requests/month; 40 requests/second | verified |
| Enterprise | Custom pricing, custom request rates, custom contract and SLAs | provider_reported |
| Batch API | Нет multi-address request; каждый адрес — отдельный request | verified |
| CSV/bulk service | Provider says large batch processing may be arranged for a fee | provider_reported |
| Storage | Provider help says API output can be stored forever | provider_reported |
| Caching | Free plan caching up to 48 hours; customers can cache while subscribed | provider_reported |

## Коммерческие и юридические замечания

- Public plan prices не являются enterprise quotes.
- Документация и примеры LocationIQ включают OpenStreetMap-compatible concepts и attribution fields; ODbL/attribution и derived-database implications всё ещё требуют legal review.
- Commercial use на Free plan связан с attribution wording на pricing page и review of terms.
- Caching и storage wording нужно проверить против точного account tier, SaaS data flow и customer-facing display model.
- Public terms содержат warranty disclaimers и не заменяют SLA/contract review.
- Atlas не проводил benchmark по house-level precision, latency, false positives или target-country quality.

## Альтернативы

| Альтернатива | Лучше, когда | Главный trade-off |
|---|---|---|
| [`Geoapify Geocoding API`](../geoapify-geocoding-api/README.ru.md) | Нужен documented hosted batch geocoding route | Batch failure semantics, ODbL/legal и benchmark review всё равно важны. |
| [`OpenCage Geocoding API`](../opencage-geocoding-api/README.ru.md) | Важны permanent storage-friendly wording и geocoding-only API | Autocomplete separate, high-volume design всё равно требует review. |
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.ru.md) | Нужен self-hosted OSM geocoding control | Вы отвечаете за import, updates, operations и ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Центральны Yandex Maps display и Russia/CIS ecosystem | Storage/display rights и map coupling требуют review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Центральны 2GIS map/catalog workflows | Caching/storage rights и field access требуют review. |
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Важны Russian address cleaning и GAR/FIAS-linked fields | Russia-focused и не international open-data geocoder. |

## Рекомендация по сценарию

Включайте LocationIQ в shortlist, когда нужны hosted forward/reverse geocoding или autocomplete с public plan limits и managed commercial API. Не считайте его official registry, address-cleaning tool или unrestricted free production Nominatim replacement.

## Доказательства

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

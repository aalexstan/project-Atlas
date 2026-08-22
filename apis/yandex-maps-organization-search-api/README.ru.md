# Yandex Maps Organization Search API

[English version](README.md)

> Продукт Yandex Maps API для поиска организаций, мест и geographic objects.

## Статус исследования

| Поле | Значение |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Yandex |
| Product status | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит:** поиск организаций/мест в продуктах, связанных с Яндекс Картами, business-directory search рядом с локацией и workflows, где нужны Yandex search results, а не только address-to-coordinate geocoding.

**Не подходит, если:** нужна нормализация адреса, address autocomplete, registry-quality address validation, routing, offline/bulk enrichment без явных прав или provider-neutral places dataset.

**Итог:** Yandex Organization Search закрывает Yandex-side сценарий place search в Atlas. Его следует сравнивать с [`2GIS Places API`](../2gis-places-api/README.ru.md), а не с address cleaning или official registry feeds.

## Граница продукта

Профиль покрывает:

- organization search;
- place/geographic-object search;
- Yandex Maps search results через Search/Geosearch API;
- связь с Yandex map display и коммерческими условиями Яндекса.

Профиль не покрывает:

- address suggestions, которые описаны в [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.ru.md);
- direct/reverse geocoding, который описан в [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md);
- routing, route optimization или distance matrices;
- official Russian address registry validation.

## Лучшие сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| Organization search в Yandex Maps UI | Strong | Официальные docs/product pages определяют поиск организаций и geographic objects как назначение. |
| Local business/place discovery рядом с точкой | Strong | Request parameters поддерживают text, coordinates и search-area constraints. |
| Address autocomplete | Weak | Используйте Geosuggest. |
| Address-to-coordinate geocoding | Weak | Используйте Yandex Geocoder. |
| Organization enrichment at scale | Medium/unknown | Commercial rights, storage и batch/offline use требуют contract confirmation. |
| Registry-quality validation | Weak | Search results не являются official registry validation. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET |
| Endpoint | `https://search-maps.yandex.ru/v1/` |
| Required parameters | `apikey`, `text`, `lang` |
| Authentication | API key в query parameter `apikey` |
| Response format | JSON by default; XML with `format=xml` |
| Common filters | `ll`, `spn`, `bbox`, `rspn`, `type`, `results`, `skip`, `uri` |
| Request language | parameter `lang` |
| OpenAPI / Swagger | Не найден в reviewed public docs |

## Pricing, limits and rights

| Item | Confirmed value | Status |
|---|---|---|
| Public commercial terms | Request packages опубликованы | verified |
| Annual Basic license | From 195,000 RUB for 1,000 requests/day in reviewed commercial terms | verified |
| Monthly Basic license | From 20,800 RUB for 1,000 requests/day in reviewed commercial terms | verified |
| API request limit | Up to 50 requests/second in reviewed public documentation | verified |
| Trial | 14-day trial key by request with 500 requests/day limit according to official FAQ | provider_reported |
| License/storage wording | Public pages appear inconsistent between Basic/Advanced or storage-capable descriptions | needs_contract_review |
| Public SLA | Не найден публично в этом исследовании | unknown |

## Коммерческие и юридические заметки

- Storage, caching, customer-facing display, third-party map display, SaaS embedding, redistribution, resale, affiliate use и model-training rights нужно считать contract blockers.
- Не используйте map-display или web-product price вместо Search API commercial terms.
- Так как просмотренные официальные страницы различаются в формулировках license/storage, procurement должен запросить written tariff and rights appendix для выбранного сценария.
- Bulk/offline enrichment не подтвержден reviewed public docs.

## Альтернативы

| Альтернатива | Лучше когда | Главный trade-off |
|---|---|---|
| [`2GIS Places API`](../2gis-places-api/README.ru.md) | Важны 2GIS directory context, buildings и places | Нужно проверять storage/caching rights и on-demand fields 2GIS. |
| [`Yandex Maps Geosuggest API`](../yandex-maps-geosuggest-api/README.ru.md) | Нужен autocomplete до выбора результата пользователем | Это suggestions, а не full organization search. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Нужна address/coordinate conversion | Это не place-search API. |
| [`DaData API`](../dadata/README.ru.md) | Нужны российские company details by INN/OGRN | Другая data model, не map place search. |

## Сценарная рекомендация

Включайте Yandex Organization Search в shortlist, когда user-facing product уже использует Яндекс Карты и нужен поиск организаций или мест. Сравнивайте с 2GIS Places API, когда важны directory depth, field availability, storage rights и local-market coverage.

## Evidence

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

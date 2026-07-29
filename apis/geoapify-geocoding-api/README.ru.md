# Geoapify Geocoding API

[English version](README.md)

> Hosted commercial geocoding API для worldwide forward/reverse geocoding, batch geocoding и address autocomplete в Geoapify Location Platform.

## Статус исследования

| Поле | Значение |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-29 |
| Provider | Geoapify |
| Product status | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит:** командам, которым нужен hosted international geocoder с public pricing, API-key access, batch geocoding, published rate limits, storage-friendly positioning и SLA на платных планах.

**Не подходит, если:** нужна official Russian address registry validation, правовая уверенность без ODbL/attribution review, self-hosted open-source stack или Russia-specific address cleaning API.

**Итог:** Geoapify — сильный hosted open-data geocoding route для address/geocoding comparison. Его нужно сравнивать с Yandex, 2GIS, DaData и self-hosted Nominatim по geography, precision, legal rights, attribution, SLA и benchmark quality.

## Граница продукта

Эта карточка покрывает:

- forward geocoding;
- reverse geocoding;
- batch geocoding;
- public pricing, limits и attribution/SLA terms.

Эта карточка не покрывает:

- official Russian registry validation;
- route planning, matrices или isochrones;
- Places API или Place Details API как отдельный place-search product;
- self-hosted Nominatim operations;
- legal advice по ODbL или derived databases.

## Сценарии наилучшего соответствия

| Сценарий | Fit | Почему |
|---|---|---|
| International forward/reverse geocoding | Strong | Official docs описывают worldwide address search и coordinate-to-address lookup. |
| Batch geocoding | Strong | Official docs описывают asynchronous batch jobs до 1,000 inputs. |
| Hosted open-data geocoding | Strong | Provider says results can be stored with attribution; legal review всё равно нужен. |
| Russian address cleaning | Weak | Это не Russia-specific cleaning/normalization API. |
| Official GAR/FIAS validation | Weak | Это не official registry route. |
| Self-hosted open-source control | Weak | Используйте Nominatim self-hosting route. |

## Технический доступ

| Поле | Значение |
|---|---|
| Protocol | HTTP GET for forward/reverse geocoding; HTTP POST/GET for batch jobs |
| Forward endpoint | `https://api.geoapify.com/v1/geocode/search` |
| Reverse endpoint | `https://api.geoapify.com/v1/geocode/reverse` |
| Batch endpoint | `https://api.geoapify.com/v1/batch` |
| Authentication | API key в параметре `apiKey` |
| Response formats | JSON, GeoJSON и XML в reviewed docs |
| Forward inputs | Free-form или structured address parameters |
| Reverse inputs | `lat` и `lon` |
| OpenAPI | Download OpenAPI link найден в reviewed docs |

## Pricing, limits and rights

| Item | Confirmed value | Status |
|---|---|---|
| Free plan | 3,000 credits/day; limited commercial use; up to 5 requests/second | verified |
| Paid monthly plan examples | API 10: $59/month for 10,000 credits/day; API 250: $609/month for 250,000 credits/day | verified |
| Geocoding credit cost | 1 Geocoding, Reverse Geocoding или Address Autocomplete request = 1 credit | verified |
| Standard plan rate limit | Up to 30 requests/second for Geocoding API requests depending on plan | verified |
| Dedicated geocoding capacity | Dedicated server example up to 50 Geocoding API calls/second | provider_reported |
| Batch | Asynchronous; up to 1,000 inputs; job results available for 24 hours | verified |
| SLA | Paid plans include default 99.5% monthly availability SLA in reviewed terms/pricing FAQ | verified |
| Storage | Provider says storage is not restricted, but attribution must be preserved | provider_reported |
| Attribution | OpenStreetMap attribution required; Geoapify attribution mandatory on Free plan | verified |
| Taxes | Prices exclude taxes and fees | verified |

## Коммерческие и юридические заметки

- ODbL, OpenStreetMap attribution, derived databases, cache sharing, resale, SaaS embedding и customer-facing display нужно считать темами legal/procurement review.
- Provider wording благоприятен для storing results, но Atlas не проводил legal review.
- Free-plan commercial use разрешён с limitations и attribution; production use должен подтвердить plan terms.
- Batch geocoding снижает cost, но работает asynchronous и result availability window важен для операций.
- Live benchmark по target countries, regions, house-level precision или latency не проводился.

## Альтернативы

| Альтернатива | Лучше когда | Главный trade-off |
|---|---|---|
| [`Nominatim Geocoder Software`](../nominatim-geocoder-software/README.ru.md) | Нужен self-hosted OSM geocoding control | Ваша команда отвечает за import, updates, operations и ODbL compliance. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Центральны Yandex Maps display и Russia/CIS map ecosystem | Storage/display rights и map coupling требуют review. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Центральны 2GIS map/catalog workflows | Caching/storage rights и field access требуют review. |
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Нужны Russian address cleaning и GAR/FIAS-linked fields | Russia-focused и не international open-data geocoder. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.ru.md) | Нужна official Russian address registry provenance | Требует internal ETL/search и не даёт global geocoding. |

## Сценарная рекомендация

Включайте Geoapify в shortlist, когда нужен hosted international geocoding, batch processing и storage-friendly open-data terms. Не считайте его Russian registry validation product или юридическим доказательством, что любой derived database/SaaS use безопасен.

## Evidence

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

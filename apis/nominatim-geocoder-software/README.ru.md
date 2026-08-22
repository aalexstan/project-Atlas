# Nominatim Geocoder Software

[English version](README.md)

> Open-source geocoder software и маршрут на данных OpenStreetMap для search и reverse geocoding.

## Статус исследования

| Поле | Значение |
|---|---|
| Уровень | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | Nominatim project / OpenStreetMap ecosystem |
| Статус продукта | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит:** командам, которым нужен open-data geocoder и которые готовы обслуживать собственный Nominatim instance, OSM imports, updates, monitoring и license compliance.

**Не подходит:** когда нужен hosted SLA API без ops, autocomplete на публичном сервисе OSMF, высоконагруженное использование public instance, нормализация адресов или проверка по официальному российскому реестру.

**Итог:** Nominatim нельзя считать бесплатным production geocoding API. Atlas моделирует его как `open_source_geocoder_software`: полезный и важный маршрут, но операционно и юридически другой, чем hosted commercial APIs.

## Граница продукта

Профиль разделяет три маршрута:

- публичный `nominatim.openstreetmap.org`: ограниченное использование по OSMF usage policy;
- self-hosted Nominatim: software, который пользователь сам обслуживает на OSM data;
- коммерческие сторонние провайдеры: отдельный procurement route, не оценивался в этом профиле.

Профиль покрывает:

- free-form и structured search;
- reverse geocoding;
- attribution OpenStreetMap и ODbL obligations;
- self-hosting import/update considerations.

Профиль не покрывает:

- autocomplete на публичном сервисе;
- hosted SLA от OSMF;
- условия коммерческих провайдеров;
- маршрутизацию;
- проверку российских адресов по официальному реестру.

## Сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| Self-hosted geocoding на OSM data | Strong | Официальная документация описывает import и update operations. |
| Ограниченный public search по действиям пользователя | Medium | Политика допускает умеренное direct user-triggered use при строгих лимитах. |
| Bulk geocoding на публичном сервисе | Weak | Public policy discourages bulk и вводит жесткие ограничения. |
| Autocomplete на публичном сервисе | Not allowed | Политика прямо запрещает autocomplete search. |
| Hosted commercial SLA | Not applicable | Оценивайте стороннего провайдера отдельно. |
| Официальный российский адресный реестр | Weak | OSM не является GAR/FIAS. |

## Технический доступ

| Поле | Публичный сервис OSMF | Self-hosted Nominatim |
|---|---|---|
| Search endpoint | `https://nominatim.openstreetmap.org/search?<params>` | Operator-defined |
| Reverse endpoint | `https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>` | Operator-defined |
| Authentication | Без API key; нужен валидный Referer/User-Agent | Operator-defined |
| Search input | Free-form или structured query | Same software API |
| Reverse input | WGS84 latitude/longitude | Same software API |
| Output formats | XML, JSON, JSONv2, GeoJSON, GeocodeJSON | Same software API |
| Search result limit | Default 10, maximum 40 | Зависит от конфигурации и ops |
| OpenAPI / Swagger | Не найдено в публичных документах | Не найдено в публичных документах |

## Цены, лимиты и права

| Параметр | Подтвержденное значение | Статус |
|---|---|---|
| Денежная цена public service | В policy плата не указана | verified_context |
| Public service max rate | Абсолютный максимум 1 request/second | verified |
| Public autocomplete | Запрещен usage policy | verified |
| Public bulk geocoding | Large bulk discouraged; regular/long scripts restricted | verified |
| Public resale/API proxying | Primary geocoding apps и API resellers должны запускать own service | verified |
| Attribution | Required | verified |
| Data license | ODbL | verified |
| Self-hosting cost | Infrastructure и operations, не API subscription | inferred |
| SLA | Публичный SLA OSMF не найден | unknown |

## Self-hosting operations

| Область | Подтверждённый planning point |
|---|---|
| Software stack | Требуются PostgreSQL, PostGIS, osm2pgsql и Python. |
| Full-planet hardware | Документация рекомендует high-memory machines, at least 1TB disk и fast disks/NVMe. |
| Full-planet import window | Около 2.5 дней на well-configured machine; на traditional SSDs могут быть реалистичнее 4-5 дней. |
| Extract route | Country/regional extracts могут уменьшить database size и import time. |
| Import styles | `admin`, `street`, `address`, `full` и `extratags` меняют data scope, import time и database size. |
| Updates | Replication setup нужно планировать заранее; systemd-managed one-time updates preferred over continuous mode. |
| Production frontend | Используйте production deployment, например gunicorn behind nginx; test server нельзя использовать в production. |

См. procurement checklist: [`Self-hosting checklist для Nominatim`](../../procurement/address-geocoding-api-selection/NOMINATIM_SELF_HOSTING.ru.md).

## Коммерческие и юридические замечания

- Public Nominatim не заменяет платный production geocoder, если основная функция продукта — geocoding.
- Public policy требует identifiable clients и attribution.
- OSM data лицензирована ODbL; derived databases, caches и SaaS use требуют юридического review.
- Public policy просит не отправлять персональные или конфиденциальные данные в сервисы OSMF.
- Self-hosting требует import, database storage, updates, monitoring, backups, security/rate limiting и capacity planning.

## Альтернативы

| Альтернатива | Когда лучше | Главный компромисс |
|---|---|---|
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Нужен hosted commercial geocoder, связанный с Яндекс Картами | Применяются ограничения хранения/показа и тарифы. |
| [`2GIS Geocoder API`](../2gis-geocoder-api/README.ru.md) | Нужен hosted geocoding в 2GIS workflows | Права кэширования/хранения требуют договора. |
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Важны чистка российских адресов и registry identifiers | Russia-focused; не open-data global geocoder. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.ru.md) | Нужна официальная российская address provenance | Нужен свой ETL/search; это не general geocoding. |

## Сценарная рекомендация

Выбирайте self-hosted Nominatim, когда open data, operational ownership и international OSM coverage важнее managed SLA. Используйте публичный `nominatim.openstreetmap.org` только в рамках его policy. Для production autocomplete или high-volume geocoding выбирайте self-hosting или коммерческого провайдера.

## Evidence

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

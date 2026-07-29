# Summary

Дата обновления: 2026-07-29
Статус: API-first foundation integrated; legacy dataset research retained

## Активное направление Atlas

Главная публичная сущность Project Atlas теперь **API profile**.

Atlas должен помогать проверять, сравнивать и выбирать API для конкретных задач. Dataset-слой сохраняется, но теперь используется как supporting research: он помогает понимать покрытие данных, происхождение источников, риски лицензий и исторический контекст.

Активная методика находится в `docs/`:

- `docs/PRINCIPLES.md` / `docs/PRINCIPLES.ru.md`
- `docs/METHODOLOGY.md` / `docs/METHODOLOGY.ru.md`
- `docs/MIGRATION.md` / `docs/MIGRATION.ru.md`
- `docs/VISION.md` / `docs/VISION.ru.md`

## Активные API-first материалы

| Материал | Количество | Комментарий |
|---|---:|---|
| API profiles | 13 | DaData, DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Nominatim Geocoder Software, FIAS/GAR Data Integration, FTS EGRUL/EGRIP integration, GLOBAS.API, Kontur.Focus API, Seldon.Basis API |
| Comparisons | 2 | Company and counterparty data APIs in Russia; address normalization and geocoding APIs |
| Need routes | 2 | Company Verification; Address normalization, address registries and geocoding |
| Procurement kits | 2 | Counterparty API selection kit; address/geocoding API selection kit |
| API indexes | 2 | English and Russian |
| Comparison indexes | 2 | English and Russian |
| Needs indexes | 2 | English and Russian |
| Active templates | 4 | API card and comparison templates in English and Russian |

## Активные API profiles

| API | Maturity | Last verified | Live test |
|---|---|---|---|
| 2GIS Geocoder API | reviewed | 2026-07-29 | not performed |
| 2GIS Places API | reviewed | 2026-07-29 | not performed |
| 2GIS Suggest API | reviewed | 2026-07-29 | not performed |
| DaData Address APIs | reviewed | 2026-07-29 | not performed |
| DaData API | reviewed | 2026-07-23 | not performed |
| FIAS/GAR Data Integration | reviewed | 2026-07-29 | not performed |
| FTS EGRUL/EGRIP Data Integration | reviewed | 2026-07-23 | not performed |
| GLOBAS.API | reviewed | 2026-07-28 | not performed |
| Kontur.Focus API | reviewed | 2026-07-23 | not performed |
| Nominatim Geocoder Software | reviewed | 2026-07-29 | not performed |
| Seldon.Basis API | reviewed | 2026-07-23 | not performed |
| Yandex Maps Geosuggest API | reviewed | 2026-07-29 | not performed |
| Yandex Maps Geocoder API | reviewed | 2026-07-29 | not performed |

## Legacy / Supporting Research

Сохранены старые исследовательские слои:

- `datasets/` - 5 dataset-карточек Pass #2.
- `providers/` - старый слой поставщиков данных.
- `access_methods/` - старый слой способов доступа к Dataset.
- `relationships/` - граф Dataset -> Provider -> Access Method.
- `catalog/` - исторические API-centric карточки Pass #1.
- `companies/` - исторические карточки компаний Pass #1.
- `research/` и `reports/` - журналы и отчеты старых проходов.
- `ratings/` - Legacy / Pre-methodology; не является действующим Atlas Score.
- старые dataset/provider/access/source templates - legacy formats.

Исходный dataset-centric корневой README сохранен как `legacy/README.dataset-centric-2026-06-23.md`.

## Важные решения миграции

- API Portal остается полезным discovery source, но не считается final source of truth.
- История проверки домена `api-seldon.ru` сохранена как исторический риск источника.
- Активная карточка Seldon.Basis связана с официальными источниками `seldongroup.ru`.
- Для Seldon.Tenders создано решение сохранить legacy-only статус: официальные страницы подтверждают `API.Seldon.Tenders` как Seldon 1.7 integration route, но публичной specification/auth/pricing evidence недостаточно для активной карточки.
- Цены веб-версий не используются как цены API.
- Старые числовые рейтинги не пересчитывались и не повышались до действующей методики.
- Excel workbook procurement kit добавлен как binary artifact и не редактировался.
- ГЛОБАС.API восстановлен из legacy backlog как активный API-first profile на основе официальных страниц Credinform; REST claim из API Portal сохранен только как legacy provenance.
- Направление адресов и геокодирования оформлено как API-first блок: отдельные profiles для DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Nominatim Geocoder Software и FIAS/GAR Data Integration, сценарное comparison, need route и procurement checklist.
- Yandex Geosuggest, 2GIS Suggest и 2GIS Places отделены от geocoder profiles, чтобы не смешивать autocomplete, place search и geocoding.
- Nominatim описан как open-source geocoder software/self-hosting route; публичный `nominatim.openstreetmap.org` не считается бесплатным production API.
- ФИАС/ГАР описан как официальный registry/data-integration route, а не как обычный REST geocoder; file downloads, SMEV и API services отмечены как официально упомянутые каналы, но method catalog/auth/schemas остаются blockers.
- Создан первый need-based маршрут `needs/company-verification/`.
- Создан индекс документации `docs/README.md` / `docs/README.ru.md`.
- Создан индекс legacy-материалов `legacy/README.md` / `legacy/README.ru.md`.
- Индексы API, comparisons и needs теперь воспроизводятся через `scripts/generate_indexes.py`.
- CI проверяет актуальность индексов перед запуском основного validator.

## Нерешенные вопросы

- Нужны credentialed live tests для API profiles.
- Для Kontur и Seldon нужны коммерческие предложения, production limits, SLA и права хранения/redistribution.
- Для DaData нужны benchmark качества, latency и legal confirmation по конкретным сценариям хранения.
- Для FTS нужно перепроверить поведение после перехода форматов 2026-08-01.
- Для ГЛОБАС.API нужны specification, endpoint catalog, authentication, schemas, limits, SLA, API-specific pricing и data-use rights от Credinform.
- Для Moscow Open Data API создан decision memo: active profile не создается, пока официальная документация `data.mos.ru` недоступна и endpoint/auth/formats/status не подтверждены.
- Для address/geocoding направления нужны credentialed benchmark, договорная проверка storage/caching/display/SaaS/redistribution rights, SLA, batch/asynchronous terms, ODbL/legal review для Nominatim/OSM и уточнение публичных деталей FIAS/GAR API services.

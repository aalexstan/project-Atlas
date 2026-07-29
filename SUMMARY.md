# Summary

Дата обновления: 2026-07-29
Статус: API-first foundation integrated; legacy dataset research retained

## Активное направление Atlas

Главная публичная сущность Project Atlas теперь **API profile**.

Atlas должен помогать проверять, сравнивать и выбирать API для конкретных задач. Dataset-слой сохраняется, но теперь используется как supporting research: он помогает понимать покрытие данных, происхождение источников, риски лицензий и исторический контекст.

Активная методика находится в `docs/`:

- `docs/PRINCIPLES.md` / `docs/PRINCIPLES.ru.md`
- `docs/METHODOLOGY.md` / `docs/METHODOLOGY.ru.md`
- `docs/REVIEW_CADENCE.md` / `docs/REVIEW_CADENCE.ru.md`
- `docs/MIGRATION.md` / `docs/MIGRATION.ru.md`
- `docs/VISION.md` / `docs/VISION.ru.md`

## Активные API-first материалы

| Материал | Количество | Комментарий |
|---|---:|---|
| API profiles | 16 | DaData, DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, Yandex Maps Organization Search API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Geoapify Geocoding API, OpenCage Geocoding API, Nominatim Geocoder Software, FIAS/GAR Data Integration, FTS EGRUL/EGRIP integration, GLOBAS.API, Kontur.Focus API, Seldon.Basis API |
| Comparisons | 2 | Company and counterparty data APIs in Russia; address normalization and geocoding APIs |
| Need routes | 3 | Company Verification; Address normalization, address registries and geocoding; Organization and place search |
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
| Geoapify Geocoding API | reviewed | 2026-07-29 | not performed |
| Kontur.Focus API | reviewed | 2026-07-23 | not performed |
| Nominatim Geocoder Software | reviewed | 2026-07-29 | not performed |
| OpenCage Geocoding API | reviewed | 2026-07-29 | not performed |
| Seldon.Basis API | reviewed | 2026-07-23 | not performed |
| Yandex Maps Geosuggest API | reviewed | 2026-07-29 | not performed |
| Yandex Maps Geocoder API | reviewed | 2026-07-29 | not performed |
| Yandex Maps Organization Search API | reviewed | 2026-07-29 | not performed |

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
- старые source/company/dataset/provider/access templates - legacy formats; legacy index now lists each preserved template separately.

Исходный dataset-centric корневой README сохранен как `legacy/README.dataset-centric-2026-06-23.md`.

## Важные решения миграции

- API Portal остается полезным discovery source, но не считается final source of truth.
- История проверки домена `api-seldon.ru` сохранена как исторический риск источника.
- Активная карточка Seldon.Basis связана с официальными источниками `seldongroup.ru`.
- Для Seldon.Tenders создано решение сохранить legacy-only статус: официальные страницы подтверждают `API.Seldon.Tenders` как Seldon 1.7 integration route, но публичной specification/auth/pricing evidence недостаточно для активной карточки.
- Legacy dataset note `datasets/procurement_tender_contracts.md` связана с Seldon.Tenders decision memo и procurement/tender research baseline; она оставлена как supporting evidence для будущего procurement/tender API comparison.
- Для procurement/tender направления добавлен research baseline `research/procurement-tender/`: ЕИС / `zakupki.gov.ru`, agency open-data datasets и Seldon.Tenders пока не повышаются до активного comparison без endpoint/auth/schema/rights evidence. Официальный EIS technical-information hub и subsection `Требования к информационному взаимодействию ЕИС с другими информационными системами` найдены, но actual documents/schemas не captured.
- Для Kontur.Focus API и Seldon.Basis API подготовлены provider-request checklists, чтобы запросить API-specific price/spec/limits/SLA/data-rights evidence без смешивания с web-product pricing.
- Legacy dataset note `datasets/company_registry.md` связана с активным comparison `comparisons/company-counterparty-data-russia/`; старые API Portal claims сохранены как provenance, а не как действующая recommendation.
- Цены веб-версий не используются как цены API.
- Старые числовые рейтинги не пересчитывались и не повышались до действующей методики.
- Excel workbook procurement kit добавлен как binary artifact и не редактировался.
- ГЛОБАС.API восстановлен из legacy backlog как активный API-first profile на основе официальных страниц Credinform; REST claim из API Portal сохранен только как legacy provenance.
- Направление адресов и геокодирования оформлено как API-first блок: отдельные profiles для DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, Yandex Maps Organization Search API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Geoapify Geocoding API, OpenCage Geocoding API, Nominatim Geocoder Software и FIAS/GAR Data Integration, сценарное comparison, need routes и procurement checklist.
- Yandex Geosuggest, 2GIS Suggest и 2GIS Places отделены от geocoder profiles, чтобы не смешивать autocomplete, place search и geocoding.
- Yandex Maps Organization Search API добавлен как отдельный organization/place search profile и не смешивается с Geosuggest, Geocoder или routing.
- Создан отдельный need route `needs/organization-place-search/`, который связывает Yandex Organization Search и 2GIS Places с практическими сценариями place search.
- Nominatim описан как open-source geocoder software/self-hosting route; публичный `nominatim.openstreetmap.org` не считается бесплатным production API.
- Geoapify Geocoding API добавлен как hosted commercial open-data geocoding route; ODbL/attribution, DPA, SaaS/redistribution rights и benchmark остаются blockers.
- OpenCage Geocoding API добавлен как второй hosted open-data geocoding route с public pricing и storage-friendly public terms; Geosearch/autocomplete, ODbL/attribution, SLA, DPA, SaaS/redistribution rights и benchmark остаются blockers.
- Для Nominatim добавлен self-hosting operations checklist: import sizing, full-planet/extract выбор, update mode, production deployment, monitoring/security и benchmark gates.
- ФИАС/ГАР описан как официальный registry/data-integration route, а не как обычный REST geocoder; open-data XML ZIP route, current package metadata `data-28072026-structure-20191024.zip`, inspected `structure-12032021.zip` with 22 XSD files, weekly updates, previous releases, current data ZIP central directory, root dictionary XML payload и sample region `99/` verified по official FNS sources. Other regional payloads, national row counts, full/delta semantics и API/SMEV method catalog/auth остаются blockers.
- Legacy dataset note `datasets/russian_address_registry.md` связана с активной карточкой `apis/fias-gar-data-integration/`; `kladr-api.ru` сохранен только как historical source-risk/provenance note.
- Для DaData Address APIs, Yandex Maps Geosuggest/Geocoder/Organization Search, 2GIS Suggest/Places/Geocoder, Geoapify Geocoding API и OpenCage Geocoding API подготовлены provider-request checklists, чтобы запросить endpoint-specific rights, SLA, limits, OpenAPI/Swagger, batch/offline terms and benchmark-support evidence.
- Создан первый need-based маршрут `needs/company-verification/`.
- Создан индекс документации `docs/README.md` / `docs/README.ru.md`.
- Создан индекс legacy-материалов `legacy/README.md` / `legacy/README.ru.md`.
- Индексы API, comparisons и needs теперь воспроизводятся через `scripts/generate_indexes.py`.
- CI проверяет актуальность индексов перед запуском основного validator.
- Создан review cadence policy с ролевым ownership, review states и правилами обновления `last_verified`.

## Нерешенные вопросы

- Нужны credentialed live tests для API profiles.
- Для Kontur и Seldon нужны письменные ответы или официальные приложения к подготовленным provider-request checklists: commercial quote, production limits, SLA и права хранения/redistribution.
- Для DaData нужны benchmark качества, latency и legal confirmation по конкретным сценариям хранения.
- Для FTS нужно перепроверить поведение после перехода форматов 2026-08-01.
- Для ГЛОБАС.API нужны specification, endpoint catalog, authentication, schemas, limits, SLA, API-specific pricing и data-use rights от Credinform.
- Для Moscow Open Data API создан decision memo: active profile не создается, пока официальная документация `data.mos.ru` недоступна и endpoint/auth/formats/status не подтверждены.
- Legacy dataset note `datasets/moscow_city_open_data.md` связана с Moscow Open Data API decision memo; декомпозиция на maintained dataset notes отложена до доступной official documentation/catalog evidence.
- Для address/geocoding направления нужны письменные ответы на подготовленные provider-request checklists, credentialed benchmark, договорная проверка storage/caching/display/SaaS/redistribution rights, SLA, batch/asynchronous terms, ODbL/legal review для Nominatim/OSM/hosted open-data geocoders, other-regions/national row-count/full-delta inspection current 57 GB FIAS/GAR data ZIP и уточнение публичных деталей FIAS/GAR API services.

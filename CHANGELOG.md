# Changelog

## 2026-07-29 — Geoapify Geocoding API profile

### Что добавлено

- Добавлен активный двуязычный API profile `apis/geoapify-geocoding-api/`.
- Добавлены research log, decision memo и provider-request checklist:
  - `research/geoapify-geocoding-api/2026-07-29.md`
  - `research/geoapify-geocoding-api/decision.md`
  - `research/geoapify-geocoding-api/decision.ru.md`
  - `research/geoapify-geocoding-api/provider-request.md`
  - `research/geoapify-geocoding-api/provider-request.ru.md`
- Address/geocoding comparison и need route теперь включают Geoapify как hosted commercial open-data geocoding route.

### Методологические решения

- Geoapify отделён от public Nominatim, self-hosted Nominatim, FIAS/GAR registry validation и Russia-specific address cleaning.
- ODbL/attribution, DPA/privacy, SaaS/redistribution rights, batch edge cases и benchmark оставлены как blockers.
- Live testing не проводился.

## 2026-07-29 — Procurement and tender research baseline

### Что добавлено

- Добавлен research baseline:
  - `research/procurement-tender/2026-07-29-official-source-baseline.md`
  - `research/procurement-tender/decision.md`
  - `research/procurement-tender/decision.ru.md`
- Legacy dataset note `datasets/procurement_tender_contracts.md` связана с новым baseline.

### Методологические решения

- ЕИС / `zakupki.gov.ru`, ведомственные open-data datasets и Seldon.Tenders пока не превращаются в активный Atlas comparison без endpoint/auth/schema/rights evidence.
- Seldon.Tenders остаётся legacy/provenance согласно существующему decision memo.
- Live testing, credentialed access, benchmark и legal review не проводились.

## 2026-07-29 — Organization and place search need route

### Что добавлено

- Добавлен активный двуязычный маршрут `needs/organization-place-search/`.
- Маршрут связывает 2GIS Places API и Yandex Maps Organization Search API с задачей поиска организаций, мест, зданий и локальных объектов.
- Root README, Needs README и generated Needs Index теперь ведут к новому маршруту.

### Методологические решения

- Place search явно отделён от address autocomplete, geocoding, routing и company verification.
- Bulk/offline enrichment, SLA, storage, display, SaaS и redistribution оставлены как procurement/legal blockers.

## 2026-07-29 — Yandex Organization Search API profile

### Что добавлено

- Добавлен активный двуязычный API profile `apis/yandex-maps-organization-search-api/`.
- Добавлены research log и decision memo:
  - `research/address-geocoding/2026-07-29-yandex-organization-search.md`
  - `research/address-geocoding/yandex-organization-search-decision.md`
  - `research/address-geocoding/yandex-organization-search-decision.ru.md`
- Address/geocoding comparison и need route теперь включают Yandex Organization Search как place/organization search candidate.
- Yandex provider-request checklist расширен на Organization Search.

### Методологические решения

- Yandex Organization Search отделён от Geosuggest, Geocoder и routing.
- Противоречивые или неоднозначные license/storage wording в official Yandex pages сохранены как contract-review blocker.
- Live testing, benchmark, SLA confirmation и contract-rights review не проводились.

## 2026-07-29 — Legacy template index cleanup

### Что изменено

- `legacy/README.md` и `legacy/README.ru.md` теперь перечисляют все legacy templates: source, company, dataset, provider и access method.
- `TODO.md` больше не содержит выполненную задачу по legacy template labeling.

### Методологические решения

- Активные API-first templates `API_CARD_TEMPLATE*` и `COMPARISON_TEMPLATE*` не изменялись.
- Старые templates остаются legacy formats для чтения и provenance, а не для новых активных карточек.

## 2026-07-29 — Review cadence policy

### Что добавлено

- Добавлен двуязычный policy:
  - `docs/REVIEW_CADENCE.md`
  - `docs/REVIEW_CADENCE.ru.md`
- `docs/README*` и `docs/METHODOLOGY*` связаны с новым регламентом.

### Методологические решения

- Ownership описан ролями, а не выдуманными персональными назначениями.
- `last_verified` нельзя обновлять из-за copy edits, navigation changes, provider-request checklists, legacy linkage или refresh generated indexes.
- Gold profile требует maintained ownership, актуальных evidence и зелёных validator/index checks.

## 2026-07-29 — Moscow open data legacy linkage

### Что изменено

- `datasets/moscow_city_open_data.md` связана с `research/moscow-open-data-api/decision.md`.
- `datasets/index.md` теперь показывает Moscow Open Data API как legacy-only/blocker route без активного API profile.
- `TODO.md` уточняет, что декомпозиция московских datasets отложена до доступной official `data.mos.ru` catalog/API documentation и reuse terms.

### Методологические решения

- API Portal и secondary undocumented endpoint collections не используются как final source of truth.
- Active API profile не создается без official endpoint/auth/formats/status/license evidence.
- Live testing и catalog export inspection не проводились.

## 2026-07-29 — Procurement dataset legacy linkage

### Что изменено

- `datasets/procurement_tender_contracts.md` связана с `research/seldon-tenders/decision.md` и сохранена как supporting evidence для будущего procurement/tender API comparison.
- `datasets/index.md` теперь показывает Seldon.Tenders как legacy-only candidate, а не активный API profile.
- `TODO.md` уточняет следующий шаг: будущий procurement comparison требует official primary-source evidence по кандидатам и источникам.

### Методологические решения

- Активная карточка Seldon.Tenders не создаётся только по API Portal summary или старому домену `api-seldon.ru`.
- Web-продукт Seldon.Tenders/Seldon.Win не смешивается с `API.Seldon.Tenders` без официальной product-boundary evidence.
- Live testing, vendor quote и field/source matrix не получены.

## 2026-07-29 — Company registry legacy linkage

### Что изменено

- `datasets/company_registry.md` связана с активным comparison `comparisons/company-counterparty-data-russia/`, company verification need route и текущими API profiles.
- `datasets/index.md` теперь показывает активный маршрут выбора через comparison, а старые API Portal claims оставляет как provenance.
- Change history comparison фиксирует связь с legacy dataset note.

### Методологические решения

- Старые REST claims, coverage claims и numerical ratings не повышены до verified facts или Atlas Score.
- API selection направлен в сценарное comparison, procurement kit и provider-request checklists.
- Live testing, новые vendor quotes и пересчёт оценок не проводились.

## 2026-07-29 — Russian address registry legacy linkage

### Что изменено

- `datasets/russian_address_registry.md` связана с активной API-first карточкой `apis/fias-gar-data-integration/`.
- `datasets/index.md` теперь показывает ФНС России / ФИАС/ГАР как активный официальный route и сохраняет `kladr-api.ru` только как legacy source-risk note.
- Change history профиля FIAS/GAR фиксирует связь с legacy dataset note.

### Методологические решения

- Старые утверждения API Portal и `kladr-api.ru` не удалены, но не используются как official FIAS/GAR evidence.
- Legacy dataset остается supporting research/provenance, а активная рекомендация находится в API-first профиле и address/geocoding comparison.
- Live testing, archive inspection и API/SMEV method verification не проводились.

## 2026-07-29 — Address provider request checklists

### Что добавлено

- Добавлены provider-request checklists:
  - `research/address-geocoding/provider-request-dadata-address.md`
  - `research/address-geocoding/provider-request-dadata-address.ru.md`
  - `research/address-geocoding/provider-request-yandex-maps.md`
  - `research/address-geocoding/provider-request-yandex-maps.ru.md`
  - `research/address-geocoding/provider-request-2gis-search.md`
  - `research/address-geocoding/provider-request-2gis-search.ru.md`
- `procurement/address-geocoding-api-selection/` теперь ссылается на provider-specific request checklists.
- Change history адресных профилей фиксирует появление этих вопросников без изменения verified facts.

### Методологические решения

- Вопросники являются procurement/research artifacts, а не ответами поставщиков.
- Документы не меняют даты проверки API, не подтверждают SLA/rights/limits и не заявляют live testing.
- Основные blockers остаются: письменные ответы поставщиков, legal review, credentialed benchmark и договорное подтверждение storage/caching/display/SaaS/redistribution rights.

## 2026-07-29 — Address and geocoding API-first direction

### Что добавлено

- Добавлены research logs и candidate decisions в `research/address-geocoding/`.
- Добавлены активные двуязычные API profiles:
  - `apis/dadata-address-api/`
  - `apis/yandex-maps-geosuggest-api/`
  - `apis/yandex-maps-geocoder-api/`
  - `apis/2gis-suggest-api/`
  - `apis/2gis-places-api/`
  - `apis/2gis-geocoder-api/`
  - `apis/nominatim-geocoder-software/`
  - `apis/fias-gar-data-integration/`
- Добавлено сценарное сравнение `comparisons/address-normalization-geocoding/`.
- Добавлен need route `needs/address-normalization-geocoding/`.
- Добавлен текстовый procurement kit `procurement/address-geocoding-api-selection/`.
- Добавлены `NEEDS_INDEX.md` и `NEEDS_INDEX.ru.md`.
- Обновлены API, comparison и root indexes/navigation.

### Методологические решения

- DaData Address APIs отделены от общей карточки DaData, чтобы не смешивать company autocomplete с address autocomplete/cleaning/geocoding.
- Yandex Maps Geocoder описан только как direct/reverse geocoder; Yandex Geosuggest выделен как отдельный autocomplete API; Organization Search и routing оставлены отдельными будущими продуктами.
- 2GIS Geocoder, 2GIS Suggest и 2GIS Places описаны как отдельные продукты с разными сценариями, тарифами и рисками.
- Nominatim оформлен как open-source geocoder software/self-hosting route; публичный OSMF service не представлен как free production API.
- Для Nominatim добавлен self-hosting operations checklist и уточнены official docs по prerequisites, full-planet/import estimates, update modes и production deployment.
- ФИАС/ГАР оформлен как официальный registry/data-integration route, а не как обычный REST geocoder; official file downloads, SMEV и API services отмечены без повышения unknown method details.
- FIAS/GAR open-data route уточнён по official open-data catalog ФНС: dataset `7707329152-fias`, XML ZIP, structure ZIP, weekly updates, previous releases и KLADR sunset path.
- Не объявлен универсальный победитель: рекомендации зависят от сценария, прав хранения, display restrictions, batch needs and TCO.
- Live testing и benchmark качества не проводились.

## 2026-07-29 — Moscow Open Data API blocker research

### Что добавлено

- Добавлены research log и decision memo в `research/moscow-open-data-api/`.

### Методологические решения

- Активная API-first карточка Moscow Open Data API не создана: официальная документация `data.mos.ru` не была доступна в этом проходе, а endpoint, authentication, formats, limits, current status и license/reuse terms не подтверждены.
- API Portal и старые Atlas-карточки сохранены только как legacy/discovery context, не как final source of truth.

## 2026-07-29 — Seldon.Tenders legacy decision

### Что добавлено

- Добавлен research log `research/seldon-tenders/2026-07-29.md`.
- Добавлены decision memo `research/seldon-tenders/decision.md` и `research/seldon-tenders/decision.ru.md`.

### Методологические решения

- Старый `api-seldon.ru` не используется как текущий официальный источник; история домена сохранена только как provenance/source-risk note.
- Официальные страницы `seldongroup.ru` подтверждают `API.Seldon.Tenders` как integration route / extended functionality Seldon 1.7, а web-продукт Seldon.Tenders переименован в Seldon.Win.
- Активная API-first карточка Seldon.Tenders не создается: публичные specification, endpoint/auth, schemas, limits, SLA, API pricing и data-use rights не найдены.
- Вариант включения как capability Seldon.Basis не выбран, потому что официальные источники связывают материал с Seldon 1.7 procurement functionality, а не с Seldon.Basis.

## 2026-07-29 — Counterparty provider request checklists

### Что добавлено

- Добавлены provider-request checklists:
  - `research/kontur-focus/provider-request.md`
  - `research/kontur-focus/provider-request.ru.md`
  - `research/seldon-basis/provider-request.md`
  - `research/seldon-basis/provider-request.ru.md`

### Методологические решения

- Документы являются вопросниками для поставщика, а не подтверждением условий.
- Вопросы сфокусированы на API-specific pricing, method/field matrix, OpenAPI/Swagger, authentication, production limits, SLA, storage/caching/redistribution/SaaS rights and change management.
- Для Seldon.Basis отдельно сохранён source-risk вопрос по историческому домену `api-seldon.ru` и текущим официальным `seldongroup.ru` материалам.

## 2026-07-28 — GLOBAS.API official-source profile

### Что добавлено

- Добавлен активный двуязычный API-first profile `apis/globas-api/`.
- Добавлен research log `research/globas-api/2026-07-28.md`.
- Добавлен provider-request checklist `research/globas-api/provider-request*.md` для запроса недостающих API, pricing, SLA и legal details у Credinform.
- ГЛОБАС.API добавлен в `comparisons/company-counterparty-data-russia/` как дополнительный enterprise-кандидат.
- Обновлены `API_INDEX.md`, `API_INDEX.ru.md`, `SUMMARY.md` и `TODO.md`.

### Методологические решения

- Официальные страницы Credinform подтверждают продуктовую идентичность и назначение ГЛОБАС.API для интеграции данных ГЛОБАС в корпоративные системы.
- Public API specification, endpoint catalog, authentication, schemas, limits, SLA и API price оставлены как `unknown`.
- Трехдневный тест системы ГЛОБАС не считается API trial без прямого подтверждения API credentials или sandbox access.
- «Санкционный комплаенс» рассматривается как отдельная граница продукта/модуля до подтверждения поставщиком.
- REST-утверждение из API Portal сохранено только как legacy provenance в `catalog/globas-api.md` и не повышено до verified.
- ГЛОБАС.API не объявлен победителем и не заменяет основной enterprise shortlist Контур.Фокус API / Seldon.Basis API без пилота, технической документации и коммерческого предложения.
- Live testing не проводился.

## 2026-07-24 — Need-based navigation and generated indexes

### Что добавлено

- Создан первый need-based маршрут: `needs/company-verification/`.
- Созданы `NEEDS_INDEX.md` и `NEEDS_INDEX.ru.md`.
- Созданы индексы документации: `docs/README.md` и `docs/README.ru.md`.
- Созданы индексы legacy-материалов: `legacy/README.md` и `legacy/README.ru.md`.
- Добавлен deterministic generator `scripts/generate_indexes.py`.

### Что усилено

- Активные двуязычные Markdown-пары получили взаимную навигацию в первых строках.
- `scripts/validate_atlas.py` проверяет bilingual navigation, needs metadata, internal references и freshness сгенерированных индексов.
- GitHub Actions теперь запускает `python3 scripts/generate_indexes.py --check` перед `python3 scripts/validate_atlas.py`.

### Методологические ограничения

- Новое внешнее исследование поставщиков не проводилось.
- Live testing не выполнялся.
- Цены, лимиты и фактические выводы API-карточек не менялись.
- Legacy-материалы не перемещались и не удалялись.

## 2026-07-24 — API-first handoff integration

### Что интегрировано

- Project Atlas переведен на API-first публичную модель: главная активная сущность теперь API profile.
- Добавлены двуязычные корневые документы `README.md` и `README.ru.md`.
- Добавлены активные документы проекта в `docs/`: Vision, Principles, Methodology, Roadmap, Glossary, Contributing и Migration.
- Добавлены активные API profiles:
  - `apis/dadata/`
  - `apis/fns-egrul-egrip-integration/`
  - `apis/kontur-focus/`
  - `apis/seldon-basis/`
- Добавлено сравнение `comparisons/company-counterparty-data-russia/`.
- Добавлен procurement kit `procurement/counterparty-api-selection/`.
- Добавлены `API_INDEX.md`, `API_INDEX.ru.md`, `COMPARISON_INDEX.md`, `COMPARISON_INDEX.ru.md`.
- Добавлен `scripts/validate_atlas.py`.
- Добавлены активные API-first templates: `API_CARD_TEMPLATE*` и `COMPARISON_TEMPLATE*`.

### Что сохранено

- Исходный dataset-centric root README сохранен как `legacy/README.dataset-centric-2026-06-23.md`.
- Старые папки `datasets/`, `providers/`, `access_methods/`, `relationships/`, `catalog/`, `companies/`, `research/`, `reports/`, `ratings/` и старые шаблоны сохранены.
- Dataset-centric слой остается supporting research/provenance, а не удаляется.
- История проверки домена `api-seldon.ru` сохранена как исторический риск источника. Активная карточка Seldon.Basis теперь использует официальные источники `seldongroup.ru`.

### Методологические решения

- Старые `ratings/` явно помечены как `Legacy / Pre-methodology` и не являются действующим Atlas Score.
- Старые source/company/dataset/provider/access templates явно помечены как legacy formats.
- Цены веб-версий не используются как цены API.
- Ни один profile не помечен как Gold.
- Excel workbook procurement kit добавлен как binary artifact и не редактировался.

## 2026-06-23 — Pass #2, dataset-centric refactoring

### Что исследовано

- Вся существующая структура ProjectAtlas после Pass #1.
- Старые слои `catalog/`, `companies/`, `research/`, `reports/`, `ratings/`, `templates/`.
- Возможность сохранить материалы первого прохода и перестроить модель знаний без удаления источников.

### Архитектурные изменения

- Главной сущностью проекта стал Dataset.
- API переведен в роль способа доступа к Dataset.
- Поставщик теперь описывается как data provider: владелец, сборщик, агрегатор, продавец или распространитель данных.
- Добавлен отдельный слой access methods для REST API, Open Data, CSV, XML, FTP, Webhook, партнерства, парсинга и других каналов.
- Добавлен граф связей Dataset -> Provider -> Access Method -> Documentation -> Cost -> License -> Alternatives.

### Какие файлы созданы

- `datasets/index.md`
- `datasets/api_catalog_metadata.md`
- `datasets/company_registry.md`
- `datasets/procurement_tender_contracts.md`
- `datasets/moscow_city_open_data.md`
- `datasets/russian_address_registry.md`
- `providers/index.md`
- `providers/apiportal_rndsoft.md`
- `providers/credinform.md`
- `providers/seldon.md`
- `providers/government_of_moscow.md`
- `providers/fias_unverified.md`
- `access_methods/index.md`
- `access_methods/api_catalog_metadata_access.md`
- `access_methods/company_registry_access.md`
- `access_methods/procurement_tender_contracts_access.md`
- `access_methods/moscow_city_open_data_access.md`
- `access_methods/russian_address_registry_access.md`
- `relationships/index.md`
- `relationships/dataset_provider_access_graph.md`
- `research/dataset_centric_migration.md`
- `ratings/dataset_ratings.md`
- `reports/report_002.md`
- `templates/dataset-card-template.md`
- `templates/provider-card-template.md`
- `templates/access-method-template.md`

### Какие файлы обновлены

- `README.md`
- `SUMMARY.md`
- `CHANGELOG.md`
- `TODO.md`

### Выводы

- Первый проход был полезен как API-discovery, но не должен оставаться основной архитектурой.
- Из уже собранных материалов выделено 5 Dataset.
- Старые API-карточки сохранены как источник происхождения фактов.
- Самые ценные Dataset сейчас: реестр компаний и контрагентов, закупки/тендеры/контракты, открытые данные Москвы, адресный реестр России.
- Главные неизвестные места: лицензии, точные схемы данных, официальность документации Seldon и ФИАС, альтернативные поставщики.

## 2026-06-23 — Pass #1, API Portal старт

### Что исследовано

- API Portal: https://apiportal.ru/catalog/
- Первые карточки API из первой страницы каталога:
  - ГЛОБАС.API
  - API Seldon.Basis
  - API Seldon.Tenders
  - API Портала открытых данных города Москвы
  - API ФИАС
- Официальная страница ГЛОБАС.API на сайте Credinform.
- Ссылки документации, указанные API Portal для Seldon, Moscow Open Data и ФИАС.

### Какие файлы созданы

- `README.md`
- `SUMMARY.md`
- `CHANGELOG.md`
- `TODO.md`
- `catalog/apiportal-catalog.md`
- `catalog/globas-api.md`
- `catalog/api-seldon-basis.md`
- `catalog/api-seldon-tenders.md`
- `catalog/api-open-data-moscow.md`
- `catalog/api-fias.md`
- `companies/credinform.md`
- `companies/seldon.md`
- `companies/government-of-moscow.md`
- `companies/fias.md`
- `companies/apiportal-rndsoft.md`
- `industries/index.md`
- `research/apiportal-initial-map.md`
- `research/documentation-link-risk.md`
- `reports/report_001.md`
- `ratings/initial_ratings.md`
- `templates/source-card-template.md`
- `templates/company-card-template.md`

### Выводы

- API Portal полезен как стартовая карта рынка: он содержит фильтры по поставщикам, категориям, отраслям и типу тарификации.
- В каталоге есть крупный блок государственных и комплаенс-данных: открытые данные, выписки, ЕСИА, платежи, проверка контрагентов, закупки.
- Некоторые внешние ссылки из карточек требуют проверки перед использованием как надежной документации. Особенно заметны `api-seldon.ru` и `kladr-api.ru`, где при проверке были обнаружены нерелевантные страницы.
- Лицензионные условия для хранения, перепродажи, SaaS и обучения ИИ в карточках API Portal обычно не раскрыты.

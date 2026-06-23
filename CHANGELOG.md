# Changelog

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

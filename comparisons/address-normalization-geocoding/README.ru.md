# API нормализации адресов, адресных реестров и геокодирования

[English version](README.md)

> Сценарное сравнение для выбора address suggestions, чистки адресов, геокодирования, поиска мест, open-data geocoding и официальной интеграции с реестром.

## Статус исследования

| Поле | Значение |
|---|---|
| Последняя проверка | 2026-07-29 |
| Рынок / регион | Россия плюс выбранный international/open-data geocoding context |
| Live testing | Один ограниченный тест Geoapify выполнен 2026-08-25; профильная validity pending human review |
| Проверенные кандидаты | DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, Yandex Maps Organization Search API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Geoapify Geocoding API, OpenCage Geocoding API, LocationIQ Geocoding API, Nominatim Geocoder Software, FIAS/GAR Data Integration |

## Краткое решение

| Сценарий | Initial shortlist | Почему |
|---|---|---|
| Российские address suggestions в формах | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md); [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md); [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md) | DaData сильнее всего для российских адресных форм; Яндекс и 2GIS полезны, когда UI связан с их картой/поиском. |
| Чистка и нормализация российских адресов | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md); [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md) для собственной базы | У DaData документирован cleaning API; ГАР — официальный источник, но нужна логика matching/search. |
| Direct geocoding | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md); [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.ru.md); [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.ru.md); [`LocationIQ Geocoding API`](../../apis/locationiq-geocoding-api/README.ru.md); DaData; [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.ru.md) для self-hosting | Hosted geocoders отличаются лицензией, ecosystem, geography и data rights; Nominatim - operational self-host route. |
| Reverse geocoding | Yandex Geocoder; 2GIS Geocoder; Geoapify; OpenCage; LocationIQ; DaData; self-hosted Nominatim | У всех, кроме FIAS/GAR, есть документированные coordinate-to-address capabilities. |
| Поиск организаций/мест | [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md); [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md) | Places и organization search — другой класс продукта, не geocoding и не registry validation. |
| Собственная российская адресная база | FIAS/GAR Data Integration | Official registry provenance, но нужны ETL, indexing, updates и legal review. |
| Open-data geocoding ownership | Geoapify, OpenCage или LocationIQ hosted routes; Nominatim self-hosting | Hosted open-data geocoding снижает operations; self-hosting убирает hosted API dependence, но создаёт OSM/ODbL и operations responsibilities. |
| Массовая обработка адресов | DaData cleaning; FIAS/GAR для собственной базы; Geoapify hosted batch geocoding; OpenCage parallel/spreadsheet geocoding; LocationIQ concurrent-request geocoding или provider-arranged batch; self-hosted Nominatim для OSM geocoding; коммерческие geocoders только после rights review | Batch, storage, caching и redistribution rights могут определить TCO. |

Универсального победителя нет. Выбор зависит от того, что важнее: UX ввода, качество данных, геокодирование, registry provenance, open-data ownership или права коммерческого использования.

## Scope

Сравнение покрывает address suggestions при вводе, normalization and standardization, проверку существования/качества адреса, direct geocoding, reverse geocoding, place search как отдельный сценарий, official registry integration, массовую обработку, storage, caching, display, SaaS и redistribution constraints.

Маршрутизация явно вне scope. Геокодер может дать координаты; routing products строят пути, расстояния, ETA и матрицы.

## Ключевые различия

- Geocoding не равно address normalization. Coordinate match не гарантирует канонические поля или юридическую валидность адреса.
- Company autocomplete не равно address autocomplete.
- Suggestions/autocomplete не являются bulk cleaning workflows.
- Places search не равен registry-quality address validation.
- Официальный реестр не становится автоматически low-latency autocomplete API.
- Public hosted geocoding не равно self-hosted geocoder software.
- Точность координат зависит от данных уровня дома/улицы/населённого пункта и требует benchmark.
- License, storage, caching, display и redistribution rights могут изменить выбор даже при сильном техническом качестве.

## Capability Matrix

| Criterion | DaData Address | Yandex Geosuggest | Yandex Geocoder | Yandex Org Search | 2GIS Suggest | 2GIS Places | 2GIS Geocoder | Geoapify | OpenCage | LocationIQ | Nominatim | FIAS/GAR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product class | Suggestions, cleaning, geocoding | Suggestions/autocomplete | Map geocoder | Organization/place search | Suggestions/autocomplete | Places/catalog search | Map/catalog geocoder | Hosted open-data geocoder | Hosted open-data geocoder | Hosted geocoder/autocomplete | Open-source geocoder software | Official registry integration |
| Address suggestions | Yes | Yes | No | No; use Geosuggest | Yes | Use Suggest | No | Address Autocomplete in same platform; not primary scope | Geosearch separate; not primary scope | Yes via Autocomplete | Public autocomplete forbidden; self-host custom | Requires own search or API-service details |
| Normalization | Yes, Russia-only cleaning | No | Not primary | No | No | No | Not primary | No | No | Not cleaning; output helpers only | No | Requires own logic |
| Validation | Cleaning quality fields | Suggestion-level only | Geocoder precision only | Search result only | Suggestion-level only | Directory match only | Geocoder match only | Confidence fields, not registry validation | Confidence/components, not registry validation | Match/components, not registry validation | OSM match only | Official registry provenance |
| Direct geocoding | Yes via cleaning | No; can pass `uri` to Geocoder | Yes | Separate Geocoder | No | No | Yes | Yes | Yes | Yes | Yes | Not confirmed |
| Reverse geocoding | Yes | No | Yes | Separate Geocoder | No | No | Yes | Yes | Yes | Yes | Yes | Not confirmed |
| Organization/place search | Separate DaData company scope | Suggestions only | Separate product | Yes | Suggestions only | Yes | Separate Places API | Separate Places API | Not primary scope | Nearby POI related; not full places replacement | Limited OSM POI search | Not applicable |
| Russia coverage | Strong documented focus | Provider map/data coverage | Provider map coverage | Provider map/search coverage | Provider catalog coverage | Provider catalog coverage | Provider map/catalog coverage | Worldwide/open-data coverage; benchmark required | Worldwide/open-data coverage; benchmark required | Worldwide/open-data/proprietary coverage; benchmark required | OSM coverage varies | Official Russian registry |
| International coverage | Suggestions city-level provider claim; cleaning/geocoding Russia-only | Provider map coverage | Provider map coverage | Provider map/search coverage | Provider catalog coverage | Provider catalog coverage | Provider catalog coverage | Worldwide provider-reported; benchmark required | Worldwide provider-reported; benchmark required | Worldwide provider-reported; benchmark required | OSM coverage varies by region | Russia only |
| Official registry provenance | FIAS/GAR/KLADR fields where available | No registry guarantee | No registry guarantee | No registry guarantee | Some FIAS-related fields may be on-demand elsewhere | Some FIAS fields on demand | Some registry fields may be on demand | Open data/OSM attribution; no registry guarantee | Open data/OSM attribution; no registry guarantee | Public/proprietary datasets; no registry guarantee | OSM, not official registry | Primary registry source |
| Public documentation | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Partial |
| Authentication | Token; secret for cleaning | API key | API key | API key | API key | API key | API key | API key | API key | Access token / API key | Public instance: User-Agent/Referer; self-host operator-defined | Depends on channel |
| Self-service | Yes | Yes/test/commercial license | Yes/test/commercial license | Commercial license; exact trial unknown | Demo key/subscription | Demo key/subscription | Demo key/subscription | Free key and paid plans | Free trial and paid plans | Free plan and paid plans | Public limited; self-host | Public portal; integration details unclear |
| Public pricing | Yes | Yes | Yes | Yes, with license wording blocker | Yes | Yes | Yes | Yes | Yes | Yes | Not commercial API price | Monetary price не указана для open-data page; API/SMEV unknown |
| Free tier / trial | 10,000 subscription requests/day | 100/day test period; commercial tariffs | 1,000/day free terms; 100/day test period | 14-day trial by request; 500 requests/day | Demo key / 1,000 Search requests | Demo key / 1,000 Search requests | Demo key / 1,000 Search requests | 3,000 credits/day | 2,500 requests/day testing only; 1 rps | 5,000 requests/day; 2 rps; 60 requests/minute; attribution | Public limited policy; self-host costs | Not applicable as commercial API |
| Quotas | Daily plan limits | Daily package limits | Daily package limits | Daily package limits | Monthly units plus per-minute | Monthly units plus per-minute | Monthly units plus per-minute | Daily credits by plan | Daily plan limits | Daily/monthly plan limits | Public 1 rps; self-host operator-defined | Unknown |
| Rate limits | 30 rps suggestions; 20 rps cleaning | RPS unknown publicly | RPS unknown publicly | Up to 50 rps | 600 Search units/minute | 600 Search units/minute | 600 Search units/minute | Up to 30 rps standard; 50 rps dedicated example | 1 rps trial; 15-40 rps paid examples | 2 rps free; 20-40 rps paid examples | Public max 1 rps | Unknown |
| Batch | Cleaning one address/request; async batch unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown | Unknown/on-demand | Unknown | Async batch up to 1,000 inputs | No multi-location API request; spreadsheet upload and parallel requests | No multi-address API request; concurrent calls; provider-arranged large batch may be available for fee | Public bulk discouraged; self-host possible | Open-data ZIP route verified; API batch service mentioned but method details unknown |
| Public hosted API | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Limited public instance only | Public portal plus official channels |
| Self-hosted option | No | No | No | No | Provider-reported On-Premise | Provider platform/on-premise needs deal | Provider platform/on-premise needs deal | Provider-managed dedicated endpoints; not self-hosted software | No | No | Yes | User-operated registry pipeline |
| Storage | Contract-sensitive | Extended license marketed with storage | Extended license marketed with storage | License wording needs contract review | Contract-sensitive | Contract-sensitive | Contract-sensitive | Provider reports allowed with attribution; legal review | Provider says permanent storage allowed; legal review | Provider says output can be stored forever; legal review | ODbL/legal review; cache repeated public results | Legal review |
| Caching | Needs contract review | Needs contract review | Temporary caching restrictions unless agreed | Needs contract review | WebAPI offer says caching not provided | WebAPI offer says caching not provided | WebAPI offer says caching not provided | Legal/ODbL review | Provider says cache/store as useful; ODbL/legal review | Free 48h; paid while subscribed; legal review | Public policy requires caching repeated results; ODbL applies | Depends on use model |
| Customer-facing display | Confirm contract | Needs Yandex terms review | Yandex map/display restrictions matter | Yandex terms review | Contract/attribution review | Contract/attribution review | Contract/attribution review | Attribution and plan review | Attribution and license review | Attribution and contract review | Attribution required | Depends on use model |
| Redistribution | Unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Unknown/contract-sensitive | Legal/ODbL review | Legal/ODbL review | Legal/contract review | ODbL/legal review | Legal review |
| SaaS use | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Needs contract review | Legal/contract review | Legal/contract review | Legal/contract review | ODbL/privacy/ops review | Legal review |
| SLA | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | Unknown publicly | 99.5% monthly availability on paid plans | Custom SLAs on Enterprise; exact public SLA unknown | Custom SLAs on Enterprise provider-reported; exact public SLA unknown | No public OSMF SLA found | Unknown |
| Privacy | Contract review | Yandex terms review | Yandex terms review | Yandex terms review | Contract review | Contract review | Contract review | Provider-reported GDPR/EU endpoints; DPA review | GDPR/no_record; DPA review | DPA/privacy review | Public policy says not to submit confidential/personal data | Legal review |
| Operational ownership | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium | Low/medium; batch ops and attribution | Low/medium; parallel high-volume design | Low/medium; concurrency, cache and legal design | High: import, updates, deployment, security и ODbL review | High for registry route |
| Live test status | Not performed | Not performed | Not performed | Not performed | Not performed | Not performed | Not performed | Observed 2026-08-25; validity pending review | Not performed | Not performed | Not performed | Not performed |
| Key unknowns | SLA, async batch, data rights | RPS, SLA, exact rights | RPS, SLA, exact rights | SLA, rights, license wording, batch | SLA, OpenAPI, rights | SLA, on-demand fields, rights | SLA, OpenAPI, rights | ODbL/legal, DPA, benchmark, batch failures | ODbL/legal, DPA, SLA, benchmark, redistribution/SaaS | ODbL/legal, DPA, SLA, benchmark, batch fee, plan scope | Sizing, ODbL, benchmark | API specs, auth, schemas, support, ZIP package contents |

## Рекомендации по сценариям

### UX ввода адреса

Начните с DaData для российских адресных форм. Добавьте Yandex Geosuggest, если UI уже связан с Яндекс Картами. Добавьте 2GIS Suggest, если подсказки должны вести в поиск/каталог 2GIS.

### Чистка существующих адресов

Используйте DaData cleaning как коммерческий API route. Используйте FIAS/GAR, если организация хочет владеть официальным registry pipeline и может построить matching/search logic.

### Геокодирование

Shortlist: Yandex Maps Geocoder, 2GIS Geocoder, Geoapify, OpenCage, LocationIQ и DaData. Добавьте self-hosted Nominatim, когда нужны open data, international OSM coverage или operational ownership. Решение принимать после проверки precision, rights, cost, attribution и SLA.

### Организации и места

Используйте 2GIS Places API или Yandex Maps Organization Search API, когда задача — поиск организаций, зданий или мест. Выбирайте по map ecosystem, нужным fields, storage/display rights, local coverage и benchmark quality. Не выводите registry-quality address validation из факта place search.

### Официальный реестр

Используйте FIAS/GAR как основной официальный российский registry route. Open-data route теперь verified как XML ZIP со structure ZIP, weekly updates, inspected current ZIP central directory, parsed root dictionaries и sample regional directories `99/`, `87/` and sparse `82/` в open-data archive ФНС. API-сервисы официально упомянуты, но остаются underspecified до фиксации method catalog, auth, schema и support details.

### Public Open-Data Geocoding

Не представляйте публичный `nominatim.openstreetmap.org` как бесплатный production API. Используйте его только в рамках usage policy. Для production оценивайте self-hosted Nominatim или commercial hosted providers вроде Geoapify, OpenCage и LocationIQ. Self-hosted Nominatim требует import sizing, update planning, production deployment, monitoring, rate limiting, backups и ODbL/legal review. Hosted open-data providers всё равно требуют attribution, ODbL/derived-database review и benchmark.

### 115-ФЗ, санкции и compliance

Это сравнение не проверяет compliance coverage. Address APIs и geocoders сами по себе не решают AML, sanctions или legal compliance screening.

## Нерешённые вопросы

| Вопрос | На что влияет | Следующий шаг |
|---|---|---|
| Какой поставщик разрешает long-term storage и customer display для точной SaaS-модели? | SaaS, redistribution, internal enrichment | Contract/legal review. |
| У кого лучшая house-level coordinate precision на выборке пользователя? | Выбор geocoder | Credentialed benchmark на согласованной выборке. |
| Можно ли выполнять large batch geocoding асинхронно и легально? | Bulk processing | Запросить у поставщика и проверить pilot credentials. |
| Какие SLA и support tiers действуют в production? | Enterprise procurement | Запросить commercial offer и SLA. |
| Каков точный FIAS/GAR API method catalog и access process? | Official registry strategy | Изучить developer docs или запросить детали канала ФНС. |
| Какие ODbL obligations возникают для cache, database или SaaS product? | Nominatim/self-hosting; Geoapify/OpenCage/LocationIQ hosted open-data routes | Legal review с конкретной data-flow diagram. |
| Какие hardware, import style и update mode нужны для self-hosted Nominatim? | Nominatim/self-hosting | Использовать self-hosting checklist и провести benchmark на target extracts. |

## Метод и источники

Сравнение использует официальные источники поставщиков и реестров, проверенные 2026-07-29. Live testing, quality benchmark и contract review не проводились.

См. [`evidence.ru.md`](evidence.ru.md).

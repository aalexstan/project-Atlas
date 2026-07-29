# API нормализации адресов, адресных реестров и геокодирования

[English version](README.md)

> Сценарное сравнение для выбора подсказок адреса, очистки, геокодирования, поиска мест и интеграции с официальным реестром.

## Статус исследования

| Поле | Значение |
|---|---|
| Последняя проверка | 2026-07-29 |
| Рынок / регион | Россия плюс отдельный международный контекст геокодирования |
| Live testing | Не проводился |
| Кандидаты | DaData Address APIs, Yandex Maps Geocoder API, 2GIS Geocoder API, FIAS/GAR Data Integration |

## Краткое решение

| Сценарий | Первичный shortlist | Почему |
|---|---|---|
| Подсказки адреса в российских формах | DaData Address APIs; отдельно оценить Yandex Geosuggest и 2GIS Suggest, если важна карта | Подсказки DaData прямо документированы; подсказки Яндекса/2GIS - отдельные продукты. |
| Очистка и нормализация адресов РФ | DaData Address APIs | Официальные docs подтверждают cleaning, quality fields, координаты и реестровые идентификаторы; Подсказки нельзя использовать для automatic processing. |
| Прямое геокодирование | Yandex Maps Geocoder API; 2GIS Geocoder API; DaData Address APIs | У всех трёх есть документированные address-to-coordinate flows, но отличаются цены и права хранения. |
| Обратное геокодирование | Yandex Maps Geocoder API; 2GIS Geocoder API; DaData Address APIs | У всех трёх документированы coordinate-to-address или nearby-address flows. |
| Поиск организаций и мест | Отдельно оценивать 2GIS Places API и Yandex Organization Search | Places search не равен геокодированию или реестровой валидации. |
| Собственная адресная база РФ | FIAS/GAR Data Integration | Официальная registry provenance, но нужны ETL, индекс и поиск. |
| Массовая обработка адресов | DaData cleaning; ФИАС/ГАР для собственной базы; commercial geocoders только после rights review | Batch/storage rights и per-record costs могут определять TCO. |

Универсального победителя нет. Выбор зависит от того, что важнее: UX ввода, качество данных, геокодирование, official provenance или права на данные.

## Scope

Сравнение покрывает:

- подсказки адреса при вводе;
- нормализацию и стандартизацию адреса;
- проверку существования и качества адреса;
- прямое геокодирование: адрес -> координаты;
- обратное геокодирование: координаты -> адрес;
- поиск организаций/мест как отдельный связанный сценарий;
- маршрутизацию как явно отдельную задачу;
- построение адресной базы на официальном реестре;
- массовую обработку;
- storage, caching, display, SaaS и redistribution constraints.

## Ключевые различия

- Геокодирование не равно нормализации адреса: координаты не доказывают канонические поля или юридическую валидность.
- Company autocomplete не равно address autocomplete.
- Places search не равен registry-quality address validation.
- Официальный реестр не автоматически становится low-latency API.
- Точность координат зависит от данных уровня дом/улица/населённый пункт и требует benchmark.
- Лицензия и права хранения могут изменить выбор даже при хорошем техническом качестве.

## Матрица сравнения

| Критерий | DaData Address APIs | Yandex Maps Geocoder API | 2GIS Geocoder API | FIAS/GAR Data Integration |
|---|---|---|---|---|
| Product class | Подсказки, cleaning, geocoding | Map geocoder | Map/catalog geocoder | Official registry integration |
| Подсказки адреса | Да | Отдельный Geosuggest | Отдельный Suggest API | Нужен свой поиск |
| Нормализация | Да, Россия | Не основная capability | Не основная capability | Нужна своя логика |
| Валидация | Quality fields в cleaning | Только geocoder precision | Только geocoder match | Official registry provenance |
| Прямое геокодирование | Да, через cleaning endpoint | Да | Да | Не подтверждено |
| Обратное геокодирование | Да | Да | Да | Не подтверждено |
| Поиск организаций/мест | Использовать DaData company APIs, отдельный scope | Отдельный продукт | Отдельный Places API | Not applicable |
| Россия | Сильный документированный фокус | Provider map coverage | Provider map/catalog coverage | Официальный реестр РФ |
| Международное покрытие | Подсказки city-level provider claim; cleaning/geocoding только РФ | Provider map coverage; нужна проверка сценария | Provider catalog coverage; нужна проверка сценария | Только РФ |
| Official registry provenance | ФИАС/ГАР/КЛАДР где доступно | Не registry guarantee | Некоторые registry fields могут быть on-demand | Primary registry source |
| Публичная документация | Да | Да | Да | Частичная для developer access |
| Аутентификация | Token; secret для cleaning | API key | API key | Зависит от канала; API unknown |
| Self-service | Да | Ключи/free/test; коммерческая лицензия может требовать покупки | Demo key/subscription через Platform Manager | Public portal; integration details unclear |
| Public pricing | Да | Да | Да | Unknown для API/download channels |
| Free tier / trial | 10 000 subscription requests/day | 1 000 requests/day free terms; 100/day test | Demo key 1 месяц / 1 000 Search requests | Not applicable как commercial API |
| Quotas | Дневные limits тарифа | Daily package limits | Package units | Unknown |
| Rate limits | 30 rps suggestions; 20 rps cleaning | RPS unknown publicly | 600 Search units/minute | Unknown |
| Batch | Cleaning one address/request; async batch не подтверждён | Unknown/contract-sensitive | Unknown | Data-feed route requires ETL |
| Storage | Contract-sensitive; provider reports no API cleaning storage | Restricted; Extended license associated with storage | Contract-sensitive; caching not provided in offer | Legal review |
| Caching | Needs contract review | Temporary caching restrictions | Caching not provided in offer | Depends on legal review |
| Customer-facing display | Обычно form/API output; confirm contract | Free terms require Yandex map display | Confirm contract and attribution | Depends on use model |
| Redistribution | Unknown | Unknown/contract-sensitive | Unknown/contract-sensitive | Needs legal review |
| SaaS use | Needs contract review | Needs contract review | Needs contract review | Needs legal review |
| SLA | Unknown publicly | Unknown publicly | Unknown publicly | Unknown |
| Live test status | Not performed | Not performed | Not performed | Not performed |
| Key unknowns | SLA, async batch, data rights | RPS, SLA, storage/display rights | SLA, OpenAPI, storage/caching rights | API specs, auth, formats, cadence, legal use |

## Рекомендации по сценариям

### UX ввода адреса

Начните с [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md) для российских адресных форм. Если интерфейс должен быть привязан к конкретной карте, отдельно оцените Yandex Geosuggest или 2GIS Suggest.

### Очистка существующих адресов

Используйте DaData cleaning как коммерческий API-маршрут. Используйте [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md), когда организация хочет владеть official registry pipeline и может построить matching/search logic.

### Геокодирование

Shortlist: [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md) и DaData. Выбор делайте после проверки map-display coupling, storage/caching rights, batch rights, latency и match quality.

### Официальная адресная база

Используйте ФИАС/ГАР как основной официальный адресный реестровый route. Не считайте его готовой заменой подсказкам адреса или геокодированию без собственной integration platform.

### 115-ФЗ, санкции и compliance

Это сравнение не подтверждает compliance coverage. Address APIs и geocoders сами по себе не решают AML, sanctions или legal compliance screening.

## Открытые вопросы

| Вопрос | На какое решение влияет | Следующий шаг |
|---|---|---|
| Какой поставщик разрешает long-term storage и customer display для конкретной SaaS-модели? | SaaS, redistribution, internal enrichment | Contract/legal review. |
| У кого лучшая точность координат до дома на пользовательской выборке? | Выбор geocoder | Credentialed benchmark на согласованной выборке. |
| Можно ли выполнять large batch geocoding асинхронно и законно? | Bulk processing | Запросить provider confirmation и проверить pilot credentials. |
| Какие SLA и support tiers действуют в production? | Enterprise procurement | Запросить коммерческое предложение и SLA. |
| Какой точный API/download путь ФИАС/ГАР? | Official registry strategy | Проверить developer access docs или обратиться в канал ФНС. |

## Метод и источники

Сравнение использует официальные источники поставщиков и реестра, проверенные 2026-07-29. Live testing, quality benchmark и contract review не проводились.

См. [`evidence.ru.md`](evidence.ru.md).

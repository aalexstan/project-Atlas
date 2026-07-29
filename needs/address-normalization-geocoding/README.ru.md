# Нормализация адресов, адресные реестры и геокодирование

[English version](README.md)

> Какой API или официальный источник выбрать для подсказок адреса, нормализации, геокодирования, проверки адреса и построения адресной базы?

## Определение задачи

Маршрут помогает выбрать между коммерческими адресными API, картографическими геокодерами, autocomplete-продуктами, поиском мест, open-data geocoding и официальным российским адресным реестром. Подсказки, очистка, геокодирование, поиск мест и интеграция с реестром разделены, потому что это разные задачи.

## Кому подходит маршрут

- Product teams, добавляющим address autocomplete в формы.
- CRM/ERP-командам, очищающим российские адресные записи.
- Разработчикам прямого или обратного геокодирования.
- Командам, выбирающим между hosted APIs и self-hosted open-data geocoding.
- Data teams, строящим внутреннюю адресную базу РФ.
- Закупке, которая проверяет storage, caching, display, SaaS и redistribution rights.

## Быстрая таблица выбора

| Сценарий пользователя | Первичный shortlist | Почему | Главный риск | Следующий документ Atlas |
|---|---|---|---|---|
| Подсказки адреса при вводе | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md); [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md); [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md) | DaData ориентирована на адресные формы; Yandex/2GIS подходят, если важен их map/search ecosystem. | Подсказки не являются unattended batch cleaning, а права различаются по поставщикам. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Нормализация и очистка адресов | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md) | Cleaning API возвращает структурные поля, quality indicators, координаты и registry identifiers. | Один адрес в запросе; per-record price; права нужно проверять в договоре. | [`Карточка DaData`](../../apis/dadata-address-api/README.ru.md) |
| Проверка существования адреса РФ по official registry | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md); DaData cleaning как коммерческий route | ГАР — официальный реестр; DaData может помочь match/clean адрес. | Для ГАР нужны matching, ETL и search; детали API-сервисов неполные. | [`Карточка ФИАС/ГАР`](../../apis/fias-gar-data-integration/README.ru.md) |
| Прямое геокодирование | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md); [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.ru.md); DaData; [`Nominatim`](../../apis/nominatim-geocoder-software/README.ru.md) для self-hosting | Hosted geocoders и self-hosted OSM route решают разные operating models. | Нужны проверка storage/display rights, attribution, coordinate precision и operations burden. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Обратное геокодирование | Yandex Geocoder; 2GIS Geocoder; Geoapify; DaData; self-hosted Nominatim | Documented coordinate-to-address routes есть вне FIAS/GAR. | Уровень возвращаемого объекта может отличаться по провайдеру и локации. | [`Test protocol`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md) |
| Организации и места | [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md); [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md) | Place search — отдельный класс продукта. | Нельзя выводить place search из geocoder docs или registry validation. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Собственная адресная база | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md) | Official registry provenance и route владения данными. | ETL/search/update operations могут определять TCO. | [`Карточка ФИАС/ГАР`](../../apis/fias-gar-data-integration/README.ru.md) |
| Open-data geocoding ownership | [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.ru.md); [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.ru.md) | Geoapify - hosted commercial route; self-hosting может использовать OSM data без hosted API vendor dependency. | Attribution, ODbL, legal review, benchmark и operations сильно различаются. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Массовая обработка адресов | DaData cleaning; ФИАС/ГАР для собственной базы; Geoapify hosted batch geocoding; self-hosted Nominatim; commercial geocoders после legal check | Разные routes решают cleaning, registry base, geocoding и operational ownership. | Batch rights, per-record costs, ODbL, caching и redistribution. | [`RFP`](../../procurement/address-geocoding-api-selection/RFP.ru.md) |

## Сценарные маршруты

### Подсказки адреса

Начните с DaData для российских адресных форм. Добавьте Yandex Geosuggest, если UI связан с Яндекс Картами. Добавьте 2GIS Suggest, если подсказки должны вести в search/catalog 2GIS.

### Нормализация и проверка

Используйте DaData cleaning, когда нужен коммерческий API, который структурирует российские адреса и возвращает quality fields. Используйте FIAS/GAR, когда важна official registry provenance и команда может построить matching/search слой.

### Прямое и обратное геокодирование

Shortlist: Yandex Maps Geocoder, 2GIS Geocoder, Geoapify и DaData. Добавьте self-hosted Nominatim, когда важны open data, OSM coverage и operational ownership. Решайте после проверки house-level precision, latency, quotas, attribution, storage/caching rights и map-display restrictions.

### Организации и места

Не считайте геокодирование поиском организаций. 2GIS Places API и Yandex Maps Organization Search API являются активными профилями для organization/place search в своих map ecosystems.

### Public Nominatim и self-hosting

Публичный `nominatim.openstreetmap.org` ограничен usage policy, запрещает autocomplete и не является бесплатным production API. Geoapify - hosted commercial open-data route, а self-hosted Nominatim - отдельная operating model с infrastructure, import sizing, update, production deployment, monitoring, security и ODbL responsibilities.

### Официальные интерфейсы FIAS/GAR

FIAS/GAR — официальный российский registry route. Open-data catalog ФНС подтверждает XML ZIP downloads, structure ZIP, weekly updates и previous release links. Официальные материалы также упоминают SMEV и API services, но current public method catalog, base URL, auth, schemas, quotas и SLA остаются blockers.

### Маршрутизация

Маршрутизация — отдельная задача. Геокодер может превратить адрес в координаты, но route building, matrices и ETA требуют routing APIs.

### Россия и международное покрытие

DaData наиболее глубока для российских адресных workflows. Yandex и 2GIS подходят в рамках своей карты/каталога. Nominatim следует качеству OpenStreetMap data, которое сильно меняется по регионам и требует benchmark.

### Storage, caching и redistribution

Проверьте это до выбора поставщика. Технически сильный геокодер может не подойти, если нельзя долгосрочно хранить, встраивать в SaaS, показывать клиентам или перераспространять результаты.

## Ограничения текущего исследования

- Live credential tests не проводились.
- Общий benchmark качества адресов не выполнялся.
- SLA и support terms в основном неизвестны публично.
- Contractual storage, caching, SaaS и redistribution rights требуют legal review.
- Open-data XML ZIP route FIAS/GAR verified, но archive contents не inspected, а детали API-сервисов остаются неполными в просмотренных публичных страницах.
- ODbL implications для Nominatim/OSM derived databases требуют legal review.
- Nominatim self-hosting всё ещё требует benchmark на target extracts and hardware.

## Вопросы перед закупкой

- Задача — autocomplete, cleaning, geocoding, registry validation, place search или routing?
- Какие страны и уровни гранулярности нужны?
- Будут ли результаты храниться, кэшироваться, показываться клиентам, перераспространяться или встраиваться в SaaS?
- Какие daily volume, peak rate, latency и SLA нужны?
- Нужна ли batch processing и должна ли она быть asynchronous?
- Нужна official Russian registry provenance, open-data ownership или turnkey UX?
- Какая benchmark sample будет использоваться для Москвы, Санкт-Петербурга, регионов и международных рынков?
- Какие legal obligations применяются к ODbL, attribution, personal data и derived databases?

## Ссылки

- API profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md), [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md), [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md), [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md), [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.ru.md), [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.ru.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md)
- Comparison: [`API нормализации адресов, адресных реестров и геокодирования`](../../comparisons/address-normalization-geocoding/README.ru.md)
- Procurement kit: [`Выбор API адресов и геокодирования`](../../procurement/address-geocoding-api-selection/README.ru.md), [`Self-hosting checklist для Nominatim`](../../procurement/address-geocoding-api-selection/NOMINATIM_SELF_HOSTING.ru.md)

## Следующий шаг

Выберите строку, которая соответствует вашему основному сценарию, прочитайте связанное сравнение, затем используйте RFP и test protocol, чтобы запросить у поставщиков права, лимиты, SLA и pilot credentials до выбора production API.

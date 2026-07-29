# Нормализация адресов, адресные реестры и геокодирование

[English version](README.md)

> Какой API или официальный источник выбрать для подсказок адреса, нормализации, геокодирования, проверки адреса и построения адресной базы?

## Определение задачи

Маршрут помогает выбрать между коммерческими адресными API, картографическими геокодерами и официальным российским адресным реестром. Подсказки, очистка, геокодирование, поиск мест и интеграция с реестром разделены, потому что это разные задачи.

## Кому подходит маршрут

- Product teams, добавляющим address autocomplete в формы.
- CRM/ERP-командам, очищающим российские адресные записи.
- Разработчикам прямого или обратного геокодирования.
- Data teams, строящим внутреннюю адресную базу РФ.
- Закупке, которая проверяет storage, caching, display, SaaS и redistribution rights.

## Быстрая таблица выбора

| Сценарий пользователя | Первичный shortlist | Почему | Главный риск | Следующий документ Atlas |
|---|---|---|---|---|
| Подсказки адреса при вводе | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md) | Прямо документированный Suggestions API и публичная цена. | Подсказки не предназначены для unattended batch processing. | [`Карточка DaData`](../../apis/dadata-address-api/README.ru.md) |
| Нормализация и очистка адресов | [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md) | Cleaning API возвращает структурные поля, quality indicators, координаты и реестровые идентификаторы. | Один адрес в запросе; per-record price. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Проверка существования адреса РФ по official registry | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md); DaData cleaning как коммерческий route | ГАР - официальный реестр; DaData может помочь match/clean адрес. | Для ГАР нужны matching и ETL; commercial API rights тоже важны. | [`Карточка ФИАС/ГАР`](../../apis/fias-gar-data-integration/README.ru.md) |
| Прямое геокодирование | [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md); [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md); DaData | У всех есть документированные address-to-coordinate flows. | Нужны проверка storage/display rights и coordinate precision. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Обратное геокодирование | Yandex; 2GIS; DaData | У всех есть документированные coordinate-to-address flows. | Уровень возвращаемого объекта может отличаться по провайдеру и локации. | [`Procurement checklist`](../../procurement/address-geocoding-api-selection/README.ru.md) |
| Поиск организаций и мест | Отдельно оценить 2GIS Places API и Yandex Organization Search | Places search - отдельный класс продукта. | Нельзя выводить place search из geocoder docs. | [`Сравнение`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Собственная адресная база | [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md) | Official registry provenance и путь владения данными. | ETL/search/update operations могут определять TCO. | [`Карточка ФИАС/ГАР`](../../apis/fias-gar-data-integration/README.ru.md) |
| Массовая обработка адресов | DaData cleaning; ФИАС/ГАР для собственной базы; commercial geocoders после legal check | Разные route решают cleaning, registry base и geocoding. | Batch rights, per-record costs и caching restrictions. | [`RFP`](../../procurement/address-geocoding-api-selection/RFP.ru.md) |

## Сценарные маршруты

### Подсказки адреса

Начните с DaData для российских адресных форм. Если интерфейс должен быть связан с конкретной картой, добавьте Yandex Geosuggest или 2GIS Suggest в следующий research shortlist.

### Нормализация и проверка

Используйте DaData cleaning, когда нужен коммерческий API, который структурирует российские адреса и возвращает quality fields. Используйте ФИАС/ГАР, когда важна official registry provenance и команда может построить matching/search слой.

### Прямое и обратное геокодирование

Shortlist: Yandex Maps Geocoder, 2GIS Geocoder и DaData. Решайте после проверки house-level precision, latency, quotas, storage/caching rights и map-display restrictions.

### Организации и места

Не считайте геокодирование поиском организаций. 2GIS Places API и Yandex Organization Search - отдельные продукты; их нужно оценивать отдельно, если нужны businesses, venues или POI.

### Маршрутизация

Маршрутизация - отдельная задача. Геокодер может превратить адрес в координаты, но route building, matrices и ETA требуют routing APIs.

### Россия и международное покрытие

DaData наиболее глубока для российских адресных workflows. Yandex и 2GIS могут подходить для map-geocoding за пределами России, но конкретное покрытие и precision нужно проверять benchmark'ом.

### Storage, caching и redistribution

Проверьте это до выбора поставщика. Технически сильный геокодер может не подойти, если нельзя долгосрочно хранить, встраивать в SaaS, показывать клиентам или перераспространять результаты.

## Ограничения текущего исследования

- Live credential tests не проводились.
- Общий benchmark качества адресов не выполнялся.
- SLA и support terms в основном неизвестны публично.
- Contractual storage, caching, SaaS и redistribution rights требуют legal review.
- Детали API-сервисов ФИАС/ГАР неполные в просмотренных публичных страницах.

## Вопросы перед закупкой

- Задача - autocomplete, cleaning, geocoding, registry validation, place search или routing?
- Какие страны и уровни гранулярности нужны?
- Будут ли результаты храниться, кэшироваться, показываться клиентам или перераспространяться?
- Какие daily volume, peak rate, latency и SLA нужны?
- Нужна ли batch processing и должна ли она быть asynchronous?
- Нужна official Russian registry provenance или turnkey UX?
- Какая benchmark sample будет использоваться для Москвы, Санкт-Петербурга и регионов?

## Ссылки

- API profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md)
- Comparison: [`API нормализации адресов, адресных реестров и геокодирования`](../../comparisons/address-normalization-geocoding/README.ru.md)
- Procurement kit: [`Выбор API адресов и геокодирования`](../../procurement/address-geocoding-api-selection/README.ru.md)

## Следующий шаг

Выберите строку, которая соответствует вашему основному сценарию, прочитайте связанное сравнение, затем используйте RFP и test protocol, чтобы запросить у поставщиков права, лимиты, SLA и pilot credentials до выбора production API.

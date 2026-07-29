# Поиск организаций и мест

[English version](README.md)

> Какой API выбрать для поиска организаций, мест, зданий или локальных объектов?

## Определение задачи

Этот маршрут описывает поиск организаций, мест, зданий и объектов карты в пользовательском или внутреннем продукте. Это отдельная задача, не равная address autocomplete, normalization, geocoding, company registry enrichment или routing.

## Кому подходит маршрут

- Product teams, которые строят поиск магазинов, филиалов, точек обслуживания или мест.
- Map interfaces, где нужно найти объект перед показом карточки на карте.
- CRM или operations teams, которым нужен map-directory context для локаций.
- Procurement teams, которые сравнивают права на хранение, показ, caching и SaaS.

## Быстрая таблица выбора

| Сценарий | Первичный shortlist | Почему | Главный риск | Следующий документ Atlas |
|---|---|---|---|---|
| Поиск мест или организаций в продукте вокруг 2GIS | [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md) | В Atlas есть активный Places profile для организаций, зданий и мест в семействе 2GIS Search API. | On-demand fields, storage/caching/display rights, SLA и benchmark quality требуют подтверждения. | [`2GIS Places profile`](../../apis/2gis-places-api/README.ru.md) |
| Поиск мест или организаций в продукте вокруг Yandex Maps | [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md) | Официальные источники Yandex подтверждают отдельный API поиска организаций/мест с endpoint, API-key access и public commercial packages. | License/storage wording, batch/offline rights, SLA и benchmark quality требуют подтверждения. | [`Yandex Organization Search profile`](../../apis/yandex-maps-organization-search-api/README.ru.md) |
| Подсказки адреса при вводе | DaData Address APIs; Yandex Geosuggest; 2GIS Suggest | Suggestions - это autocomplete scenario, а не полный place-search result set. | Права на suggestions и follow-up calls отличаются по поставщикам. | [`Address/geocoding comparison`](../../comparisons/address-normalization-geocoding/README.ru.md) |
| Реквизиты компании по ИНН/ОГРН или registry identity | DaData; Kontur.Focus; Seldon.Basis; FTS integration | Company and counterparty data использует registry/risk data, а не map place search. | Нельзя выводить legal-entity verification из результата map directory. | [`Company verification route`](../company-verification/README.ru.md) |
| Routing, ETA или distance matrix | Отдельные routing products | Routing вне scope текущих Atlas place-search profiles. | Geocoding или place search сами по себе не дают route planning. | Backlog |

## Сценарные маршруты

### Поиск по картографическому справочнику

Начинайте с 2GIS Places API и Yandex Maps Organization Search API. Выбор зависит от map ecosystem, нужных полей, покрытия и разрешённой модели display/storage. Не объявляйте победителя без общего benchmark и сопоставимых contract assumptions.

### Autocomplete перед поиском

Используйте Yandex Geosuggest или 2GIS Suggest, когда пользователь ещё вводит запрос. Suggestion может вести к последующему place или geocoder lookup, но это не то же самое, что полноценный результат поиска организаций.

### Проверка компании

Используйте маршрут проверки контрагентов, если нужна legal-entity identity, реквизиты ИНН/ОГРН, counterparty risk, monitoring или official registry provenance. Place search может помочь найти филиал или venue, но не заменяет проверку контрагента.

### Массовое обогащение

Считайте bulk или offline enrichment procurement blocker. Public docs, просмотренные Atlas, не доказывают, что каждый intended place-search response можно хранить, кэшировать, распространять или использовать в SaaS без конкретного договора.

## Ограничения текущего исследования

- Live credential test или benchmark не проводились.
- Public SLA terms остаются unknown в активных profiles.
- Storage, caching, customer-facing display, SaaS use, redistribution и resale rights требуют contract/legal review.
- Coverage и quality нужно тестировать на целевых городах, категориях и неоднозначных названиях.
- Этот маршрут не покрывает routing, distance matrices, sanctions screening или legal-entity due diligence.

## Вопросы перед закупкой

1. Целевой объект - organization, branch, building, venue, address или legal entity?
2. В какой map ecosystem будет показан результат?
3. Какие поля нужно вернуть и хранить?
4. Будут ли результаты показаны клиентам, кэшированы, redistributed или embedded in SaaS?
5. Какие daily volume, peak rate, latency и SLA требуются?
6. Требуется ли batch или offline enrichment?
7. Какая benchmark sample покрывает целевые города, категории, дублирующиеся названия и закрытые или переехавшие организации?

## Ссылки

- Profiles: [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md), [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md)
- Related profiles: [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md)
- Comparison: [`Address Normalization, Address Registries and Geocoding APIs`](../../comparisons/address-normalization-geocoding/README.ru.md)
- Procurement kit: [`Address and Geocoding API Selection`](../../procurement/address-geocoding-api-selection/README.ru.md)

## Следующий шаг

Прочитайте две активные place-search карточки, затем используйте procurement kit, чтобы запросить точные data rights, SLA, field matrix и pilot credentials перед выбором production provider.

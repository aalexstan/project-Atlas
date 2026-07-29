# Решения по кандидатам адресов и геокодирования

[English version](candidate-decisions.md)

## Краткое решение

| Кандидат | Решение по активной карточке | Причина |
|---|---|---|
| Адресные API DaData | Создать [`dadata-address-api`](../../apis/dadata-address-api/README.ru.md) | Официальная документация подтверждает подсказки, стандартизацию, прямое и обратное геокодирование, аутентификацию, лимиты и публичные цены. |
| Yandex Maps Geocoder API | Создать [`yandex-maps-geocoder-api`](../../apis/yandex-maps-geocoder-api/README.ru.md) | Официальная документация подтверждает прямое/обратное геокодирование, endpoint, API-ключ, JSON-ответ и условия бесплатного/коммерческого использования. |
| 2GIS Geocoder API | Создать [`2gis-geocoder-api`](../../apis/2gis-geocoder-api/README.ru.md) | Официальная документация подтверждает прямое/обратное геокодирование, API-ключ, JSON-ответ, пакетные цены и лимиты. |
| ФИАС/ГАР | Создать [`fias-gar-data-integration`](../../apis/fias-gar-data-integration/README.ru.md) | Официальные источники ФНС подтверждают идентичность и роль реестра; карточка оформляется как интеграция данных, а не обычный REST-геокодер. |
| Yandex Geosuggest | Создать [`yandex-maps-geosuggest-api`](../../apis/yandex-maps-geosuggest-api/README.ru.md) | Последующее official-source research подтвердило отдельный autocomplete product с endpoint, API key, public tariffs и object-type filters. |
| Yandex Organization Search | Создать [`yandex-maps-organization-search-api`](../../apis/yandex-maps-organization-search-api/README.ru.md) | Последующее official-source research подтвердило отдельный organization/place search product с endpoint, API key, public commercial terms и лимитом API-запросов до 50 rps. |
| 2GIS Places API | Создать [`2gis-places-api`](../../apis/2gis-places-api/README.ru.md) | Последующее official-source research подтвердило отдельный Places API для организаций, зданий и мест с public package pricing. |
| 2GIS Suggest API | Создать [`2gis-suggest-api`](../../apis/2gis-suggest-api/README.ru.md) | Последующее official-source research подтвердило отдельный suggestion product для object, address, street и route-endpoint suggestions. |
| OpenStreetMap / Nominatim | Создать [`nominatim-geocoder-software`](../../apis/nominatim-geocoder-software/README.ru.md) | Последующее исследование подтвердило Nominatim как open-source geocoder software/self-hosting route, а не бесплатный public production API. |
| Адресные наборы data.mos.ru | Backlog | Потенциальный московский маршрут, но не замена национальному реестру или геокодеру в этом проходе. |

## Решения о границах

DaData получает отдельную адресную карточку, потому что существующая карточка DaData описывает более широкое семейство API и сценарии компаний/контрагентов. Адресные подсказки, стандартизация, прямое и обратное геокодирование имеют отдельные технические, ценовые и правовые ограничения.

Yandex Maps Geocoder описывается только как геокодер. Подсказки адресов относятся к Geosuggest, поиск организаций - к Organization Search, маршрутизация и матрицы расстояний - к отдельным навигационным продуктам.

2GIS Geocoder описывается как прямое и обратное геокодирование. Places API и Suggest API являются отдельными активными profiles, потому что они важны для сценариев, но не включаются в возможности Geocoder.

ФИАС/ГАР - официальный реестр и маршрут интеграции данных. Здесь он не описывается как коммерческий low-latency API подсказок адреса.

## Стандарт доказательности

Все активные карточки основаны на официальных или первичных источниках, проверенных 2026-07-29. Live testing с credentials не проводился, benchmark качества не выполнялся, уровень Gold не присваивался. Более поздние строки в этом decision log отражают последующее углубление того же address/geocoding направления 2026-07-29.

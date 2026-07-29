# Доказательства сравнения нормализации адресов и геокодирования

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| DaData документирует address suggestions, cleaning, direct geocoding и reverse geocoding как адресные API capabilities. | https://dadata.ru/api/ | 2026-07-29 | verified | Подробные endpoint-доказательства в карточке DaData Address. |
| DaData Suggestions нельзя использовать для автоматической обработки файлов/баз адресов. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Важное разделение сценариев. |
| Yandex Geosuggest документирован как серверный API для поисковых подсказок геообъектов и/или организаций. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Отдельно от Yandex Geocoder. |
| Request docs Yandex Geosuggest указывают endpoint, API key, text query, result limit и supported object types. | https://yandex.com/maps-api/docs/suggest-api/request.html | 2026-07-29 | verified | Доказательство autocomplete. |
| Yandex Geocoder поддерживает прямое и обратное геокодирование. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Это не нормализация адресов. |
| Бесплатные условия Yandex Geocoder включают 1 000 запросов/день и ограничения показа на Яндекс Картах. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Существенное условие прав на данные. |
| Yandex Organization Search / Geosearch API документирован для поиска организаций и geographic objects. | https://yandex.com/maps-api/products/geosearch-api | 2026-07-29 | verified | Сценарий place/organization search. |
| Request docs Yandex Organization Search указывают endpoint, API key, required `text` и `lang`, JSON/XML format support. | https://yandex.com/maps-api/docs/geosearch-api/request.html | 2026-07-29 | verified | Отдельно от Geosuggest и Geocoder profiles. |
| Commercial docs Yandex указывают public Organization Search request packages. | https://yandex.com/dev/commercial/doc/en/concepts/geosearch | 2026-07-29 | verified | API commercial terms, not web-product pricing. |
| Places API docs Yandex указывают API request limit до 50 rps. | https://yandex.com/maps-api/docs/geosearch-api/index.html | 2026-07-29 | verified | Production suitability всё ещё требует contract/SLA review. |
| Docs 2GIS Search разделяют Geocoder, Places и Suggest APIs. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Граница продукта. |
| 2GIS Suggest API документирует object, address, street и route-endpoint suggestions. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Сценарий Suggest/autocomplete. |
| 2GIS Places API ищет организации, здания и места. | https://docs.2gis.com/en/api/search/places/overview | 2026-07-29 | verified | Place search отделён от geocoding. |
| 2GIS Geocoder поддерживает direct/reverse geocoding. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON с API key. |
| Цены и лимиты 2GIS Search публично документированы. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Package pricing и 600 units/minute. |
| 2GIS WebAPI offer говорит, что кэширование не предусмотрено, и ограничивает extraction/storage вне условий договора. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Data-rights blocker для 2GIS Search products. |
| Public Nominatim policy запрещает autocomplete, ограничивает public use максимум 1 request/second и требует own service для primary geocoding apps/resellers. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Public instance не является бесплатным production API. |
| Nominatim Search и Reverse APIs документированы для geocoding. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Software/API capability; self-hosting требует ops. |
| Nominatim installation/import/update/deployment docs описывают production operations requirements: high-memory full-planet imports, import styles, replication updates и production frontend deployment. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Self-hosting operations blocker. |
| OpenStreetMap data требует attribution и лицензирована ODbL. | https://www.openstreetmap.org/copyright | 2026-07-29 | verified | Legal/data-rights blocker. |
| Страницы ФНС/ФИАС определяют ГАР как официальный адресный реестр РФ, а ФИАС - как систему ФНС. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Реестровый route. |
| Open-data catalog ФНС указывает GAR/FIAS как dataset `7707329152-fias` с XML data, structure ZIP, weekly updates и previous releases. | https://www.nalog.gov.ru/opendata/7707329152-fias/ | 2026-07-29 | verified | Open-data route details. |
| Developer section ФИАС содержит file downloads, SMEV и API services, но детальная API specification не видна в просмотренных static pages. | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Unknowns остаются явными. |
| Архивный материал ФНС описывает weekly file downloads, daily SMEV publication и online API batch provision by request как integration routes. | https://www.nalog.gov.ru/rn77/news/activities_fts/13824755/ | 2026-07-29 | verified | Подтверждает channel split, но не полные method details. |

## Live Testing

Live test, benchmark или contract review Atlas не проводил.

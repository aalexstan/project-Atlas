# Доказательства сравнения нормализации адресов и геокодирования

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| DaData документирует address suggestions, cleaning, direct geocoding и reverse geocoding как адресные API capabilities. | https://dadata.ru/api/ | 2026-07-29 | verified | Подробные endpoint-доказательства в карточке DaData Address. |
| DaData Suggestions нельзя использовать для автоматической обработки файлов/баз адресов. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Важное разделение сценариев. |
| Yandex Geocoder поддерживает прямое и обратное геокодирование. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Это не нормализация адресов. |
| Бесплатные условия Yandex Geocoder включают 1 000 запросов/день и ограничения показа на Яндекс Картах. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Существенное условие прав на данные. |
| Docs 2GIS Search разделяют Geocoder, Places и Suggest APIs. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Граница продукта. |
| 2GIS Geocoder поддерживает direct/reverse geocoding. | https://docs.2gis.com/en/api/search/geocoder/overview | 2026-07-29 | verified | HTTP JSON с API key. |
| Цены и лимиты 2GIS Search публично документированы. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Package pricing и 600 units/minute. |
| Страницы ФНС/ФИАС определяют ГАР как официальный адресный реестр РФ, а ФИАС - как систему ФНС. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Реестровый route. |
| Developer section ФИАС содержит file downloads, SMEV и API services, но детальная API specification не видна в просмотренных static pages. | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Unknowns остаются явными. |

## Live Testing

Live test, benchmark или contract review Atlas не проводил.

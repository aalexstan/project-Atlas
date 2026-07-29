# Набор для выбора API адресов и геокодирования

[English version](README.md)

> Текстовый procurement kit для выбора подсказок адреса, очистки, геокодирования, поиска мест и интеграции с официальным реестром.

## Назначение

Используйте этот набор до покупки или пилота адресного/geocoding provider. Он помогает разделить API capability, права данных, географию, качество, цены и operational fit.

## Документы

| Документ | Назначение |
|---|---|
| [`RFP.ru.md`](RFP.ru.md) | Вопросы поставщику перед коммерческой оценкой. |
| [`TEST_PROTOCOL.ru.md`](TEST_PROTOCOL.ru.md) | Воспроизводимый protocol benchmark'а качества адресов и геокодирования. |
| [`SAMPLE_POLICY.ru.md`](SAMPLE_POLICY.ru.md) | Правила безопасной тестовой выборки без credentials, частных адресов и персональных данных. |
| [`SCORING.ru.md`](SCORING.ru.md) | Scenario-weighted scorecard; не глобальный Atlas Score. |
| [`NOMINATIM_SELF_HOSTING.ru.md`](NOMINATIM_SELF_HOSTING.ru.md) | Operations checklist для self-hosted Nominatim/OSM geocoding. |

## Provider-specific requests

Используйте эти checklists после общего RFP, когда поставщик попал в shortlist. Это вопросы, а не ответы поставщика.

| Поставщик / scope | Checklist |
|---|---|
| DaData address suggestions, cleaning and geocoding | [`provider-request-dadata-address.ru.md`](../../research/address-geocoding/provider-request-dadata-address.ru.md) |
| Yandex Maps Geosuggest, Geocoder and Organization Search | [`provider-request-yandex-maps.ru.md`](../../research/address-geocoding/provider-request-yandex-maps.ru.md) |
| 2GIS Suggest, Places and Geocoder | [`provider-request-2gis-search.ru.md`](../../research/address-geocoding/provider-request-2gis-search.ru.md) |

## Связанные материалы Atlas

- Need route: [`Нормализация адресов, адресные реестры и геокодирование`](../../needs/address-normalization-geocoding/README.ru.md)
- Comparison: [`API нормализации адресов, адресных реестров и геокодирования`](../../comparisons/address-normalization-geocoding/README.ru.md)
- Profiles: [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md), [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md), [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md), [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md), [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md), [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md), [`Nominatim Geocoder Software`](../../apis/nominatim-geocoder-software/README.ru.md), [`FIAS/GAR Data Integration`](../../apis/fias-gar-data-integration/README.ru.md)

## Как использовать

1. Выберите основной сценарий в need route.
2. Отправьте RFP-вопросы shortlisted providers.
3. Согласуйте legal and reproducible test sample.
4. Проведите test protocol с provider-approved credentials.
5. Заполните scorecard доказательствами и открытыми рисками.

В этом наборе нет реальных benchmark results.

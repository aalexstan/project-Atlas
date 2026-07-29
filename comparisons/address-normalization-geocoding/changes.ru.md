# Изменения сравнения нормализации адресов и геокодирования

[English version](changes.md)

| Дата | Изменение | Влияние |
|---|---|---|
| 2026-07-29 | Создано первое сценарное сравнение DaData Address APIs, Yandex Maps Geocoder API, 2GIS Geocoder API и FIAS/GAR Data Integration. | Добавляет новое направление сравнения Atlas без объявления универсального победителя. |
| 2026-07-29 | Добавлены Yandex Geosuggest, 2GIS Suggest, 2GIS Places и Nominatim; матрица расширена для autocomplete, places, public hosted API, self-hosting, bulk, attribution, license obligations, privacy и operational ownership. | Делает сравнение полноценным decision aid по адресам/геокодированию при сохранении сценарных рекомендаций. |
| 2026-07-29 | Уточнён FIAS/GAR open-data route с evidence по XML ZIP, structure ZIP и weekly update. | Отделяет verified file-feed facts от всё ещё unknown API-service specification. |
| 2026-07-29 | Добавлены Nominatim self-hosting operations blockers по import sizing, update mode и production deployment. | Снижает риск смешать public-instance, self-hosted и commercial-provider routes. |
| 2026-07-29 | Добавлен Yandex Maps Organization Search API как кандидат для place/organization search. | Закрывает Yandex-side сценарий place search без смешивания с geocoding или registry validation. |

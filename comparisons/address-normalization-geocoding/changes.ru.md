# Изменения сравнения нормализации адресов и геокодирования

[English version](changes.md)

| Дата | Изменение | Влияние |
|---|---|---|
| 2026-07-29 | Создано первое сценарное сравнение DaData Address APIs, Yandex Maps Geocoder API, 2GIS Geocoder API и FIAS/GAR Data Integration. | Добавляет новое направление сравнения Atlas без объявления универсального победителя. |
| 2026-07-29 | Добавлены Yandex Geosuggest, 2GIS Suggest, 2GIS Places и Nominatim; матрица расширена для autocomplete, places, public hosted API, self-hosting, bulk, attribution, license obligations, privacy и operational ownership. | Делает сравнение полноценным decision aid по адресам/геокодированию при сохранении сценарных рекомендаций. |
| 2026-07-29 | Уточнён FIAS/GAR open-data route с evidence по XML ZIP, structure ZIP и weekly update. | Отделяет verified file-feed facts от всё ещё unknown API-service specification. |
| 2026-07-29 | Добавлены Nominatim self-hosting operations blockers по import sizing, update mode и production deployment. | Снижает риск смешать public-instance, self-hosted и commercial-provider routes. |
| 2026-07-29 | Добавлен Yandex Maps Organization Search API как кандидат для place/organization search. | Закрывает Yandex-side сценарий place search без смешивания с geocoding или registry validation. |
| 2026-07-29 | Добавлен Geoapify Geocoding API как hosted commercial open-data geocoding route. | Добавляет managed international/batch geocoding option, но оставляет ODbL, attribution, DPA и benchmark как blockers. |
| 2026-07-29 | Added OpenCage Geocoding API as a second hosted open-data geocoding route. | Расширяет hosted open-data shortlist, сохраняя Geosearch/autosuggest, ODbL/legal review, SLA, DPA и benchmark blockers. |
| 2026-07-29 | Added LocationIQ Geocoding API as a hosted geocoding/autocomplete route. | Расширяет hosted geocoding shortlist, сохраняя batch, plan scope, storage/caching, ODbL/legal review, SLA, DPA и benchmark blockers. |
| 2026-07-29 | Added current FIAS/GAR official package metadata while keeping archive contents and full/delta semantics unknown. | Makes the official registry file route more concrete without overstating verification. |
| 2026-07-29 | Added FIAS/GAR structure archive inspection evidence and data ZIP header size. | Уточняет schema evidence, сохраняя blocker по 57 GB data archive и package semantics. |
| 2026-07-29 | Added current FIAS/GAR data ZIP central directory evidence. | Подтверждает file index, archive scale и version marker, сохраняя XML payload, row counts и full/delta semantics как blockers. |
| 2026-07-29 | Added FIAS/GAR root dictionary XML payload evidence. | Уточняет reference-data uncertainty, сохраняя regional payload и national row-count blockers. |
| 2026-07-29 | Added FIAS/GAR sample regional directory `99/` XML evidence. | Демонстрирует regional payload parsing на small sample без обобщения до national row counts. |
| 2026-07-29 | Added FIAS/GAR sample regional directory `87/` XML evidence with CRC/size validation for the sampled entries. | Добавляет второй regional payload sample, сохраняя national row counts и full/delta semantics как unproved. |
| 2026-07-29 | Added FIAS/GAR sparse regional directory `82/` XML evidence. | Показывает, что valid regional files can be mostly empty и ETL должен обрабатывать empty groups. |

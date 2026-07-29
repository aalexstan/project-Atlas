# Изменения need-маршрута адресов и геокодирования

[English version](changes.md)

| Дата | Изменение | Влияние |
|---|---|---|
| 2026-07-29 | Создан первый need-based маршрут для подсказок адреса, очистки, геокодирования, интеграции с реестром и закупочных решений. | Добавляет вход в новое адресное направление Atlas от задачи пользователя. |
| 2026-07-29 | Добавлены маршруты для Yandex Geosuggest, 2GIS Suggest, 2GIS Places, Nominatim self-hosting и уточнены blockers API-сервисов FIAS/GAR. | Маршрут теперь покрывает autocomplete, place search, hosted geocoding, open-data self-hosting и official registry choices. |
| 2026-07-29 | Добавлены verified детали FIAS/GAR open-data ZIP route с сохранением blockers API-сервисов. | Помогает отделить file-feed integration от REST-like API procurement. |
| 2026-07-29 | Nominatim self-hosting route связан с отдельным operations checklist. | Помогает оценить self-hosting до трактовки OSM geocoding как hosted API replacement. |
| 2026-07-29 | Yandex Maps Organization Search API добавлен в маршрут поиска организаций/мест. | Даёт пользователям Yandex ecosystem option рядом с 2GIS Places без смешивания geocoding и place search. |
| 2026-07-29 | LocationIQ Geocoding API добавлен в hosted geocoding/autocomplete и open-data route options. | Расширяет hosted provider shortlist, сохраняя storage/caching, batch, SLA, ODbL/legal и benchmark blockers. |

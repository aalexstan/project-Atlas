# Доказательства по интеграции с ФИАС/ГАР

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| ФИАС - федеральная государственная информационная система для формирования, ведения и использования ГАР. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Страница сервиса ФНС. |
| ГАР - государственный информационный ресурс со сведениями об адресах. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Страница «О ФИАС». |
| Оператор ФИАС - ФНС России. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Официальное указание оператора. |
| Цель ГАР/ФИАС - единый открытый федеральный ресурс с достоверными, единообразными, общедоступными сведениями об адресах. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Правовая и реестровая роль. |
| Публичный портал называет ГАР единственным легитимным источником сведений об адресе. | https://fias-file.nalog.ru/ | 2026-07-29 | verified | Registry provenance claim. |
| ГАР обязаны использовать органы власти и местного самоуправления при оказании услуг. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Релевантно регулируемым процессам. |
| Объекты адресации включают здания, сооружения, земельные участки, помещения и машино-места. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Scope объектов. |
| Open-data catalog ФНС указывает dataset identifier `7707329152-fias`, owner ФНС России и XML format. | https://www.nalog.gov.ru/opendata/7707329152-fias/ | 2026-07-29 | verified | Open-data route. |
| Open-data catalog ФНС указывает current data ZIP URL и separate structure ZIP URL для GAR/FIAS dataset. | https://www.nalog.gov.ru/opendata/7707329152-fias/ | 2026-07-29 | verified | Atlas не скачивал и не inspected archives. |
| Open-data catalog ФНС указывает weekly updates и previous release ZIP files. | https://www.nalog.gov.ru/opendata/7707329152-fias/ | 2026-07-29 | verified | На текущей странице указаны latest modification 2026-07-28 и page update 2026-07-29. |
| Developer section содержит пункты «Открытые данные (файловые выгрузки)», «СМЭВ» и «API-сервисы». | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Детальные API docs не видны в static page. |
| Архивный материал ФНС говорит, что на портале ФИАС опубликованы API и СМЭВ сервисы для получения сведений из ГАР. | https://www.nalog.gov.ru/rn77/news/activities_fts/13611328/ | 2026-07-29 | verified | Архивная страница может содержать устаревшие детали, но подтверждает provenance официальных каналов. |
| Архивный материал ФНС описывает integration routes: еженедельные выгрузки с публикацией дважды в неделю, СМЭВ с ежедневной публикацией и online API batch provision by request. | https://www.nalog.gov.ru/rn77/news/activities_fts/13824755/ | 2026-07-29 | verified | Cadence рассматривается как official historical context до фиксации текущих developer docs. |
| Архивный материал ФНС говорит, что файловые выгрузки ГАР можно скачать в developer/open-data section, а также через СМЭВ и API services. | https://www.nalog.gov.ru/rn77/news/activities_fts/13874101/ | 2026-07-29 | verified | Подтверждает разделение file/API/SMEV routes. |
| ФНС сообщает, что публикация КЛАДР становится квартальной с 2026-07-01, полугодовой с 2027-01-01 и прекращается с 2028-01-01. | https://www.nalog.gov.ru/rn77/news/activities_fts/16629379/ | 2026-07-29 | verified | КЛАДР — legacy и не должен быть target model для новых интеграций. |
| На портале ФИАС есть публичный поиск адреса. | https://fias-file.nalog.ru/Search | 2026-07-29 | observed | Web service, не доказательство bulk API. |
| Search и Frontend pages рассмотрены как пользовательские страницы портала, не как документация поддерживаемого public API. | https://fias-file.nalog.ru/Search | 2026-07-29 | inferred | Не документировать видимые website endpoints как stable integration APIs. |
| Полный публичный method catalog, base URL, auth, schemas, quotas и SLA не найдены в просмотренных static pages. | Official pages reviewed | 2026-07-29 | unknown | Главный blocker перед API-like maturity. |
| Direct/reverse geocoding не подтверждены. | Official pages reviewed | 2026-07-29 | unknown | ГАР - адресный реестр, не геокодер. |

## Live Testing

Live integration, file download verification или credentialed API test не проводились.

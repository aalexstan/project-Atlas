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
| Developer section содержит пункты «Открытые данные (файловые выгрузки)», «СМЭВ» и «API-сервисы». | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Детальные API docs не видны в static page. |
| На портале ФИАС есть публичный поиск адреса. | https://fias-file.nalog.ru/Search | 2026-07-29 | observed | Web service, не доказательство bulk API. |
| Полный публичный method catalog, base URL, auth, schemas, quotas и SLA не найдены в просмотренных static pages. | Official pages reviewed | 2026-07-29 | unknown | Главный blocker перед API-like maturity. |
| Direct/reverse geocoding не подтверждены. | Official pages reviewed | 2026-07-29 | unknown | ГАР - адресный реестр, не геокодер. |

## Live Testing

Live integration, file download verification или credentialed API test не проводились.

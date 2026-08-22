# Evidence 2GIS Suggest API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| 2GIS Search APIs разделены на Geocoder, Places, Suggest и связанные API. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Доказательство границы продукта. |
| Suggest API предназначен для подсказок во время ввода текста пользователем. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Scope autocomplete. |
| Suggest requests используют GET и JSON responses. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Публичная документация. |
| Example endpoint: `https://catalog.api.2gis.com/3.0/items` с `q`, `location`, `key`. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Access key в query. |
| Default `suggest_type` — `object`; документированы address, street и route-endpoint suggestions. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Нужна сценарная оценка типов. |
| Suggest API оптимизирован для использования с Places API. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Важная связь продуктов. |
| Access key получается в Platform Manager как demo key или subscription. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Authentication/onboarding. |
| Suggest API тарифицируется по успешным запросам в месяц. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Billing unit — successful request. |
| Публичная цена Suggest API начинается от 7 000 рублей за 100 000 units/month. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | API-тариф, не цена веб-продукта. |
| Лимит Suggest API — 600 Search units/minute; demo limit — 1 000 total requests. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Public pricing/limits page. |
| WebAPI offer говорит, что кэширование не предусмотрено, и ограничивает извлечение/хранение вне договора. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Data-rights blocker. |

## Live Testing

Atlas не проводил credentialed live test.

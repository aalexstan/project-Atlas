# Решение по направлению procurement/tender API

[English version](decision.md)

## Решение

После повторной проверки 2026-08-22 создать **reviewed, но не fully verified** профили двух разных маршрутов:

- официальная интеграция закупочной информации ЕИС;
- коммерческий агрегированный API Seldon.Tenders.

Ни один маршрут не считать универсальным победителем или credential-tested production API.

## Обоснование

Официальные страницы Казначейства России подтверждают публичную роль и идентичность ЕИС / `zakupki.gov.ru` и показывают маршруты форматов взаимодействия. Актуальная официальная страница Seldon прямо описывает `API.Seldon.Tenders` как программный сервис закупочных данных и перечисляет извещения, протоколы, контракты и документы. Atlas всё ещё не получил полные актуальные схемы, endpoint catalogs, правила доступа, limits, SLA и API-specific commercial terms.

Этого достаточно, чтобы сохранить и организовать направление, но недостаточно для текущей активной API-карточки Atlas или сценарного comparison.

## Границы

- ЕИС / `zakupki.gov.ru` является официальным procurement information source и reviewed data-integration route, но не автоматически turnkey REST API.
- Навигация technical-information ЕИС подтверждает integration route, но сама по себе не доказывает полный public API specification.
- Ведомственные CSV open-data datasets являются supporting evidence, а не national procurement API.
- Старые материалы Seldon остаются provenance; новый профиль опирается на актуальные `seldongroup.ru`, а `api-seldon.ru` оставлен как source-risk note.
- Web portals, file feeds, government services и commercial API products нужно сравнивать как разные product classes.

## Условия возвращения к активному профилю

Создавать активные profiles или comparison только после подтверждения официальными источниками:

- endpoint catalog или distribution channel;
- authentication или access process;
- schemas, formats и versioning;
- update cadence, rate limits или quotas;
- data scope и field matrix;
- document access model;
- SLA/support или availability statement;
- storage, caching, display, redistribution и SaaS rights;
- pricing или cost model для commercial routes.

## Следующий исследовательский шаг

Получить actual official EIS technical-information documents, schemas и supported distribution-channel details, затем сравнивать их с Seldon.Tenders/Seldon.Win только если Seldon предоставит API-level evidence. До этого `datasets/procurement_tender_contracts.md` остаётся legacy supporting research.

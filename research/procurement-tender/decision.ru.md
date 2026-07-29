# Решение по направлению procurement/tender API

[English version](decision.md)

## Решение

Оставить направление procurement/tender как **research baseline / comparison backlog**.

Не создавать активный API profile или comparison на текущей доказательной базе.

## Обоснование

Официальные страницы Казначейства России подтверждают публичную роль и идентичность ЕИС / `zakupki.gov.ru`. Официальные страницы ведомственных open-data datasets подтверждают существование procurement-related CSV datasets. Публичный сайт ЕИС также содержит раздел technical information и подраздел information interaction, но Atlas не получил actual current document files, schemas, endpoint catalog или access rules. Существующее исследование Atlas также сохраняет Seldon.Tenders как legacy-only, потому что не хватает official API specification, auth, pricing, limits, SLA и data-rights evidence.

Этого достаточно, чтобы сохранить и организовать направление, но недостаточно для текущей активной API-карточки Atlas или сценарного comparison.

## Границы

- ЕИС / `zakupki.gov.ru` является официальным procurement information source, но здесь ещё не описывается как активный Atlas API profile.
- Навигация technical-information ЕИС подтверждена как маршрут исследования, но сама по себе не является достаточным API specification evidence.
- Ведомственные CSV open-data datasets являются supporting evidence, а не national procurement API.
- Seldon.Tenders остаётся legacy/provenance до появления более сильных official evidence.
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

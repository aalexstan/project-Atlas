# Углублённое исследование Avtocod B2B API — 2026-08-23

[English version](2026-08-23-avtocod-deep-dive.md)

## Подтверждённая техническая и billing-механика

- Для каждого report type есть дневная, месячная и общая квоты генерации. Исчерпание квоты возвращает HTTP `402`.
- Частота генерации может ограничиваться по аккаунту/report type; превышение возвращает `429 TooManyRequests`. Универсальное публичное численное RPS не указано.
- Отчёт обычно доступен в системе шесть месяцев; для report type может быть настроен другой `max_age`.
- Чтение существующего отчёта не меняет баланс и не тарифицируется как новая генерация.
- Перегенерация с `FORCE` является платной.
- Webhooks поддерживают `on_update` и `on_complete`, но доставка явно не гарантирована; после timeout рекомендован polling.
- Состав источников фиксируется для типа отчёта договором. Источники обрабатываются независимо и имеют статусы `OK`, `PROGRESS` или `ERROR`.

## Публичные B2B-цены

Официальная страница тарифов публикует цены двух стандартных отчётов, доступных через business formats, включая API:

- `Автозаполнение`: 10 RUB/отчёт; индивидуальные условия от 10 000 отчётов; идентификаторы не входят.
- `Автозаполнение плюс`: 11 RUB/отчёт; индивидуальные условия от 10 000 отчётов; идентификаторы не входят.

Цена полного отчёта `Информация об автомобиле` зависит от объёма и формата. Описаны monthly package, package и post-paid subscription; большие объёмы и индивидуальные отчёты требуют quote. Это B2B report prices, а не доказательство одинаковой цены любого API-контракта.

## Источники и границы качества

- Avtocod заявляет более 100 государственных, коммерческих и собственных источников и ежемесячное подключение новых. Это provider-reported claim, а не независимый аудит полноты.
- Среди примеров названы ГИБДД, РСА, МВД, ФНС, Росфинмониторинг, ФНП, НБКИ, ФТС, дилеры и сервисные центры.
- Состав источников зависит от report type и договора. Per-source statuses показывают частичную/ошибочную генерацию, но не доказывают корректность или freshness фактов.

## Storage, SaaS и high-stakes use

- Шестимесячная доступность отчёта на стороне сервиса документирована. Она сама по себе не даёт права хранить, передавать или перепродавать содержимое вне сервиса.
- Avtocod продвигает API для developers/integrators, страхования, банков, МФО, лизинга, marketplaces и driver scoring. Это provider-reported product scenarios.
- Публичный marketing не заменяет договорное разрешение на customer-facing redistribution, adverse decisions, model training или regulated scoring.

## SLA и support

- Avtocod заявляет официальный договор и постоянную техническую/документационную поддержку business customers.
- Публичных численных SLA, response SLO, support response time или service credits не найдено.

## Оставшиеся блокеры

- Состав отчёта и source list по целевому договору.
- Contract-specific цены и numeric rate limit.
- Численные SLA/support commitments.
- Письменные права local storage, customer display, SaaS, redistribution/resale, automated decisions, scoring и model training.
- Независимый benchmark correctness, freshness, false positives и source-error behavior.

## Live testing

Не проводился. Account, token, report generation и billable action не использовались.

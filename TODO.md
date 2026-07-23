# TODO

## Высокий приоритет

- Поддерживать API-first направление: новые публичные материалы создавать как `apis/<slug>/` или `comparisons/<slug>/`, а не как новые dataset-centric основные карточки.
- Провести live testing для DaData, Kontur.Focus API, Seldon.Basis API и FTS integration только при наличии законных credentials/test access и сохранить evidence.
- Для Kontur.Focus API запросить API-specific quote, production limits, SLA, OpenAPI/Swagger или полную спецификацию, storage rights, redistribution rights и contract appendices.
- Для Seldon.Basis API запросить Swagger, authentication model, method pricing, batch billing, production limits, SLA, storage rights и redistribution rights.
- Для DaData подтвердить endpoint-specific права хранения, caching, customer-facing display, redistribution/resale и провести quality benchmark на легальной тестовой выборке.
- Перепроверить FTS EGRUL/EGRIP integration после перехода форматов, запланированного на 2026-08-01.
- Не использовать `ratings/` как действующий Atlas Score. Любая новая оценка должна следовать `docs/METHODOLOGY.md` и иметь публичные критерии.
- Поддерживать `API_INDEX.md`, `API_INDEX.ru.md`, `COMPARISON_INDEX.md` и `COMPARISON_INDEX.ru.md` при каждом добавлении активной карточки или сравнения.

## Средний приоритет

- Мигрировать полезные факты из `catalog/globas-api.md` в API-first профиль ГЛОБАС.API после проверки официальных источников Credinform.
- Решить, нужен ли отдельный API-first профиль для Seldon.Tenders; старую карточку не удалять.
- Исследовать official/API-first профиль Moscow Open Data API на основе `data.mos.ru`, не полагаясь только на API Portal.
- Исследовать address/geocoding comparison: DaData, официальные address registry routes, Yandex, 2GIS и другие подтвержденные API.
- Декомпозировать `datasets/moscow_city_open_data.md` на supporting dataset notes только после повторной проверки каталога data.mos.ru.
- Для старого `datasets/company_registry.md` связать подтвержденные факты с активным comparison `comparisons/company-counterparty-data-russia/`.
- Для старого `datasets/procurement_tender_contracts.md` сохранить факты как supporting evidence для будущего procurement API comparison.
- Для `datasets/russian_address_registry.md` найти официальный источник ФИАС/GAR и отделить его от неподтвержденного `kladr-api.ru`.
- Продолжить разбор API Portal только как discovery source: каждую существенную карточку проверять по primary sources.

## Низкий приоритет

- После ручной проверки перенести исторические-only материалы в `legacy/`, если это улучшит навигацию и не потеряет provenance.
- Добавить индекс legacy-материалов с объяснением, какие файлы относятся к Pass #1, Pass #2 и API-first migration.
- Обновить старые provider/dataset/access templates только как legacy formats; новые активные шаблоны уже находятся в `templates/API_CARD_TEMPLATE*.md` и `templates/COMPARISON_TEMPLATE*.md`.
- Добавить automated generation для API/comparison indexes, если количество активных профилей вырастет.
- Создать policy для review cadence и владельцев карточек.

## Legacy Backlog

Эти направления были найдены в старом dataset-centric backlog и остаются исследовательскими кандидатами. Они не считаются подтвержденными API profiles:

- Цены на топливо.
- Справочник АЗС.
- Дорожный трафик и пробки.
- Погода и метеоистория.
- История транспортных средств.
- Недвижимость и кадастровые данные.
- Платежи и финтех-транзакции.
- Маркетинговые и телекоммуникационные аудитории.
- Доставка, логистика и курьерские события.
- Маркетплейсы и товарные каталоги.
- Судебные, санкционные и исполнительные данные.
- Медицинские и телемедицинские данные.

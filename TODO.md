# TODO

## Высокий приоритет

- Поддерживать API-first направление: новые публичные материалы создавать как `apis/<slug>/` или `comparisons/<slug>/`, а не как новые dataset-centric основные карточки.
- Провести live testing для DaData, Kontur.Focus API, Seldon.Basis API и FTS integration только при наличии законных credentials/test access и сохранить evidence.
- Для Kontur.Focus API отправить подготовленный `research/kontur-focus/provider-request*.md` и получить API-specific quote, production limits, SLA, OpenAPI/Swagger или полную спецификацию, storage rights, redistribution rights и contract appendices.
- Для Seldon.Basis API отправить подготовленный `research/seldon-basis/provider-request*.md` и получить Swagger, authentication model, method pricing, batch billing, production limits, SLA, storage rights и redistribution rights.
- Для DaData подтвердить endpoint-specific права хранения, caching, customer-facing display, redistribution/resale и провести quality benchmark на легальной тестовой выборке.
- Для DaData Address APIs подтвердить права хранения/caching/customer-facing display/SaaS, OpenAPI endpoint scope, async/batch options и benchmark качества адресов.
- Для Yandex Maps Geosuggest API подтвердить production RPS, SLA, storage/display/SaaS rights, batch/offline restrictions и benchmark autocomplete quality.
- Для Yandex Maps Geocoder API подтвердить production RPS, SLA, storage/display rights по выбранной лицензии, batch/offline geocoding rights и провести house-level precision benchmark.
- Для 2GIS Suggest API подтвердить OpenAPI/Swagger, SLA, storage/caching/display/SaaS rights, batch restrictions и quality benchmark для address/object suggestions.
- Для 2GIS Places API подтвердить on-demand method/field matrix, SLA, storage/caching/display/SaaS rights, batch/enrichment restrictions и benchmark по целевым категориям.
- Для 2GIS Geocoder API подтвердить OpenAPI/Swagger, SLA, storage/caching/display/SaaS rights, on-demand field pricing и провести precision benchmark.
- Для Nominatim Geocoder Software провести legal review ODbL/attribution/derived databases, benchmark exact self-hosting sizing/update operations на target extracts/hardware и не использовать public instance для production/autocomplete/bulk.
- Для FIAS/GAR Data Integration уточнить содержимое текущих ZIP archives, full/delta package model, API services method catalog, auth, quotas, costs, SMEV eligibility и legal-use rights.
- Перепроверить FTS EGRUL/EGRIP integration после перехода форматов, запланированного на 2026-08-01.
- Не использовать `ratings/` как действующий Atlas Score. Любая новая оценка должна следовать `docs/METHODOLOGY.md` и иметь публичные критерии.
- Поддерживать `API_INDEX*`, `COMPARISON_INDEX*` и `NEEDS_INDEX*` через `python3 scripts/generate_indexes.py`; CI должен проходить `python3 scripts/generate_indexes.py --check`.
- Поддерживать взаимные языковые ссылки в активных двуязычных Markdown-парах.

## Средний приоритет

- Для ГЛОБАС.API запросить у Credinform API specification, endpoint catalog, authentication, field matrix, sandbox/API credentials, method pricing, batch billing, production limits, SLA и data-use rights.
- Для Seldon.Tenders сохранить legacy-only статус до появления официальной specification, endpoint/auth evidence, API pricing, limits, SLA и data-use rights; решение зафиксировано в `research/seldon-tenders/decision.md`.
- Для Moscow Open Data API повторить проверку `data.mos.ru`, когда официальная документация доступна; текущий blocker и decision memo сохранены в `research/moscow-open-data-api/`.
- Подготовить отдельное исследование Yandex Organization Search, если сценарий поиска организаций в экосистеме Яндекса станет приоритетным.
- Рассмотреть коммерческих Nominatim/OSM-провайдеров только отдельными профилями по их официальным terms, SLA и тарифам.
- Декомпозировать `datasets/moscow_city_open_data.md` на supporting dataset notes только после повторной проверки каталога data.mos.ru.
- Для старого `datasets/company_registry.md` связать подтвержденные факты с активным comparison `comparisons/company-counterparty-data-russia/`.
- Для старого `datasets/procurement_tender_contracts.md` сохранить факты как supporting evidence для будущего procurement API comparison.
- Для `datasets/russian_address_registry.md` связать legacy dataset notes с активной карточкой `apis/fias-gar-data-integration/` без использования `kladr-api.ru` как официального источника.
- Продолжить разбор API Portal только как discovery source: каждую существенную карточку проверять по primary sources.

## Низкий приоритет

- После ручной проверки перенести исторические-only материалы в `legacy/`, если это улучшит навигацию и не потеряет provenance.
- Поддерживать индекс legacy-материалов и обновлять его при появлении новых исторических слоёв.
- Обновить старые provider/dataset/access templates только как legacy formats; новые активные шаблоны уже находятся в `templates/API_CARD_TEMPLATE*.md` и `templates/COMPARISON_TEMPLATE*.md`.
- Расширить needs routes после появления новых сравнений и подтверждённых API profiles.
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

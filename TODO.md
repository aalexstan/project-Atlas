# TODO

## Высокий приоритет

- Поддерживать API-first направление: новые публичные материалы создавать как `apis/<slug>/` или `comparisons/<slug>/`, а не как новые dataset-centric основные карточки.
- Провести live testing для DaData, Kontur.Focus API, Seldon.Basis API и FTS integration только при наличии законных credentials/test access и сохранить evidence.
- Для Kontur.Focus API отправить подготовленный `research/kontur-focus/provider-request*.md` и получить API-specific quote, production limits, SLA, OpenAPI/Swagger или полную спецификацию, storage rights, redistribution rights и contract appendices.
- Для Seldon.Basis API отправить подготовленный `research/seldon-basis/provider-request*.md` и получить Swagger, authentication model, method pricing, batch billing, production limits, SLA, storage rights и redistribution rights.
- Для DaData подтвердить endpoint-specific права хранения, caching, customer-facing display, redistribution/resale и провести quality benchmark на легальной тестовой выборке.
- Для DaData Address APIs отправить подготовленный `research/address-geocoding/provider-request-dadata-address*.md` и получить endpoint-specific права хранения/caching/customer-facing display/SaaS, OpenAPI endpoint scope, async/batch options, SLA и данные для benchmark качества адресов.
- Для Yandex Maps Geosuggest API отправить подготовленный `research/address-geocoding/provider-request-yandex-maps*.md` и получить production RPS, SLA, storage/display/SaaS rights, batch/offline restrictions и данные для benchmark autocomplete quality.
- Для Yandex Maps Geocoder API отправить подготовленный `research/address-geocoding/provider-request-yandex-maps*.md` и получить production RPS, SLA, storage/display rights по выбранной лицензии, batch/offline geocoding rights и данные для house-level precision benchmark.
- Для Yandex Maps Organization Search API отправить обновленный `research/address-geocoding/provider-request-yandex-maps*.md` и получить SLA, exact storage/display/SaaS rights, license/storage wording clarification, batch/offline enrichment rights и benchmark для organization/place search.
- Для 2GIS Suggest API отправить подготовленный `research/address-geocoding/provider-request-2gis-search*.md` и получить OpenAPI/Swagger, SLA, storage/caching/display/SaaS rights, batch restrictions и данные для quality benchmark address/object suggestions.
- Для 2GIS Places API отправить подготовленный `research/address-geocoding/provider-request-2gis-search*.md` и получить on-demand method/field matrix, SLA, storage/caching/display/SaaS rights, batch/enrichment restrictions и данные для benchmark по целевым категориям.
- Для 2GIS Geocoder API отправить подготовленный `research/address-geocoding/provider-request-2gis-search*.md` и получить OpenAPI/Swagger, SLA, storage/caching/display/SaaS rights, on-demand field pricing и данные для precision benchmark.
- Для Geoapify Geocoding API отправить подготовленный `research/geoapify-geocoding-api/provider-request*.md` и получить ODbL/attribution interpretation, DPA/privacy terms, SaaS/redistribution rights, batch failure/retry billing, paid-plan contract terms и benchmark-support evidence.
- Для OpenCage Geocoding API отправить подготовленный `research/opencage-geocoding-api/provider-request*.md` и получить ODbL/attribution interpretation, redistribution/SaaS rights, DPA/privacy terms, paid-plan contract/SLA terms, Geosearch/autosuggest scope и benchmark-support evidence.
- Для Nominatim Geocoder Software провести legal review ODbL/attribution/derived databases, benchmark exact self-hosting sizing/update operations на target extracts/hardware и не использовать public instance для production/autocomplete/bulk.
- Для FIAS/GAR Data Integration после inspection official `structure-12032021.zip`, current data ZIP central directory, root dictionary XML payload и sample region `99/` проверить other regional XML payload contents, national row counts, CRC validation against full payload, full/delta package model, API services method catalog, auth, quotas, costs, SMEV eligibility и legal-use rights.
- Перепроверить FTS EGRUL/EGRIP integration после перехода форматов, запланированного на 2026-08-01.
- Не использовать `ratings/` как действующий Atlas Score. Любая новая оценка должна следовать `docs/METHODOLOGY.md` и иметь публичные критерии.
- Поддерживать `API_INDEX*`, `COMPARISON_INDEX*` и `NEEDS_INDEX*` через `python3 scripts/generate_indexes.py`; CI должен проходить `python3 scripts/generate_indexes.py --check`.
- Поддерживать взаимные языковые ссылки в активных двуязычных Markdown-парах.

## Средний приоритет

- Для ГЛОБАС.API запросить у Credinform API specification, endpoint catalog, authentication, field matrix, sandbox/API credentials, method pricing, batch billing, production limits, SLA и data-use rights.
- Для Seldon.Tenders сохранить legacy-only статус до появления официальной specification, endpoint/auth evidence, API pricing, limits, SLA и data-use rights; решение зафиксировано в `research/seldon-tenders/decision.md`.
- Для Moscow Open Data API повторить проверку `data.mos.ru`, когда официальная документация доступна; текущий blocker и decision memo сохранены в `research/moscow-open-data-api/`.
- Рассмотреть дополнительные коммерческие Nominatim/OSM-провайдеры только отдельными профилями по их официальным terms, SLA и тарифам; Geoapify и OpenCage уже оформлены как hosted open-data geocoding profiles.
- Не декомпозировать `datasets/moscow_city_open_data.md` на maintained dataset notes, пока official `data.mos.ru` catalog/API documentation, export formats и reuse terms не станут доступны для проверки.
- Для будущего procurement/tender API comparison получить actual documents/schemas из official `zakupki.gov.ru` technical-information subsection `Требования к информационному взаимодействию ЕИС с другими информационными системами`, затем собрать official primary-source evidence по Seldon.Tenders/Seldon.Win и альтернативным поставщикам; baseline и technical-info recheck сохранены в `research/procurement-tender/`.
- Продолжить разбор API Portal только как discovery source: каждую существенную карточку проверять по primary sources.

## Низкий приоритет

- После ручной проверки перенести исторические-only материалы в `legacy/`, если это улучшит навигацию и не потеряет provenance.
- Поддерживать индекс legacy-материалов и обновлять его при появлении новых исторических слоёв.
- Расширять needs routes после появления новых сравнений и подтверждённых API profiles; следующий возможный кандидат - отдельный маршрут по self-hosted/open-data geocoding после legal/benchmark review.

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

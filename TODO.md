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
- Для LocationIQ Geocoding API отправить подготовленный `research/locationiq-geocoding-api/provider-request*.md` и получить ODbL/attribution interpretation, storage/caching/SaaS/redistribution rights, DPA/privacy terms, exact plan scope, enterprise SLA terms, batch/CSV processing terms и benchmark-support evidence.
- Для Nominatim Geocoder Software провести legal review ODbL/attribution/derived databases, benchmark exact self-hosting sizing/update operations на target extracts/hardware и не использовать public instance для production/autocomplete/bulk.
- Для FIAS/GAR Data Integration после inspection official `structure-12032021.zip`, current data ZIP central directory, root dictionary XML payload и sample regions `99/`/`87/`/`82/` проверить remaining regional XML payload contents, national row counts, CRC validation beyond sampled regions, full/delta package model, API services method catalog, auth, quotas, costs, SMEV eligibility и legal-use rights.
- Для FTS EGRUL/EGRIP integration после recheck конфликта официальных источников 2026-08-15 получить законный FTP access или official support clarification и проверить actual post-cutover directory/file behavior, schemas, checksums, recovery process и права redistribution/SaaS.
- Не использовать `ratings/` как действующий Atlas Score. Любая новая оценка должна следовать `docs/METHODOLOGY.md` и иметь публичные критерии.
- Поддерживать `API_INDEX*`, `COMPARISON_INDEX*` и `NEEDS_INDEX*` через `python3 scripts/generate_indexes.py`; CI должен проходить `python3 scripts/generate_indexes.py --check`.
- Поддерживать взаимные языковые ссылки в активных двуязычных Markdown-парах.
- Для новых API profiles заполнять canonical fields `status`, `pricing`, `authentication`, `sandbox`, `rate_limits`, `openapi` и `open_questions`; неизвестные значения указывать явно, а не пропускать поле.
- Разбирать GitHub Issues от weekly source monitor: подтверждать изменения по official evidence, расширять markers для важных pricing/docs pages и не обновлять facts/`last_verified` автоматически.
- Постепенно расширить content markers за пределы текущих критичных источников; HTTP `200` без marker/fingerprint подтверждает только доступность, а не неизменность содержания.
- Для payment acceptance сравнить YooKassa, CloudPayments и T-Bank Internet Acquiring API на общем lawful sandbox benchmark только после получения credentials; запросить merchant quotes, production limits, SLA, 54-ФЗ/PCI DSS responsibility split и storage/SaaS/redistribution terms.
- Для messaging APIs сравнить SMSC и SMS.RU на одинаковых синтетических сценариях доставки; отдельно не смешивать Telegram Bot API с carrier SMS и запросить production limits, DLR, sender, SLA, OTP и data-rights terms.
- Для weather APIs провести общий benchmark по Москве, Санкт-Петербургу и регионам только после получения допустимого тестового доступа; отдельно проверить model output против station observations, historical semantics, commercial licence, storage и derived-data rights.
- Для Yandex Maps Routing API и 2GIS Routing API получить product-specific pricing, matrix limits, traffic/ETA semantics, truck restrictions, SLA и storage/display/SaaS/redistribution terms; провести общий lawful benchmark только после credentials.
- Для OSRM провести self-hosting sizing/update benchmark на выбранном OSM extract, проверить attribution/licence obligations и operational SLO; public demo endpoint не использовать как production evidence.
- Для EIS получить актуальные interaction formats, endpoint/distribution catalog, authentication, schemas, quotas, update cadence, support и data-use terms.
- Для Seldon.Tenders отправить provider request и получить endpoint catalog, protocol, schemas, source coverage, API-specific price, limits, SLA и storage/redistribution terms.
- Для Russian Post Tracking API получить contract price, production throughput, SLA, retry semantics и rights for stored/customer-facing tracking data.
- Для Yandex Delivery API получить target-account quote, quotas, SLA, webhook/retry guarantees и storage/customer-display/SaaS terms; проводить test order только с разрешённым доступом.
- Для Yandex Rasp API уточнить quotas, SLA, актуальную coverage/freshness и возможность письменной коммерческой лицензии для paid/closed SaaS; не использовать данные вне опубликованных terms.
- Для Bank of Russia Exchange Rates Web Service уточнить operational rate limits, endpoint/schema change policy, commercial redistribution and SLA terms; не считать XML daily route real-time market-data feed.
- Для Wildberries Seller API получить method/field matrix для целевого seller scope, API-specific price, production quotas, SLA, support, versioning и storage/SaaS/redistribution terms; не считать отдельные примеры лимитов общей квотой API.
- Для MoySklad JSON API выбрать конкретный сценарий интеграции, подтвердить endpoint/plan limits, условия Vendor-публикации, SLA/support и storage/SaaS/redistribution terms; live testing проводить только с разрешённым developer account.
- Для Ozon Seller API повторно открыть основной official reference, получить method/field matrix, account/plan limits, SLA, rights и synthetic benchmark; не повышать профиль выше reviewed до этого.
- Для commerce operations procurement kit запросить у MoySklad, Wildberries и Ozon одинаковые method matrix, plan limits, SLA, data rights и тестовый доступ; не превращать scorecard в глобальный рейтинг.
- Для source monitor добавить отдельные безопасные health/documentation URL там, где provider публикует их; не расширять мониторинг на credential-gated или платные методы.
- Для MoySklad, Wildberries и Ozon повторно проверить доступность добавленных public documentation checks из CI; health endpoint добавлять только по официальному подтверждению.
- Для CDEK Logistics API получить актуальные endpoints, authentication, schemas, prices, quotas, SLA и data-rights terms напрямую из технической документации или договора.
- Для Avtocod Vehicle History API отправить `research/vehicle-history/provider-request*.md` и получить target report/source/field matrix, contract prices, numeric frequency limit, SLA/support response times, source freshness/correction policy и письменные storage/SaaS/redistribution/automated-decision/scoring/model-training terms; не запускать Swagger report без разрешённого paid access.
- Для ЕГРН/НСПД получить official clarification по `research/real-estate-cadastral/provider-request*.md`: отделить key-based FGIS EGRN access, NSPD electronic services, межведомственный обмен и frontend карты; уточнить supported endpoints, auth, тарифы, quotas, SLA и reuse rights.

## Средний приоритет

- Для ГЛОБАС.API запросить у Credinform API specification, endpoint catalog, authentication, field matrix, sandbox/API credentials, method pricing, batch billing, production limits, SLA и data-use rights.
- Для Seldon.Tenders сохранить legacy-only статус до появления официальной specification, endpoint/auth evidence, API pricing, limits, SLA и data-use rights; решение зафиксировано в `research/seldon-tenders/decision.md`.
- Для Moscow Open Data API повторить проверку `data.mos.ru`, когда official sources раскроют rate limits, quotas, SLA, точную operational/support model и детали получения production API key; текущий blocker и decision memo сохранены в `research/moscow-open-data-api/`.
- Рассмотреть дополнительные коммерческие Nominatim/OSM-провайдеры только отдельными профилями по их официальным terms, SLA и тарифам; Geoapify, OpenCage и LocationIQ уже оформлены как hosted open-data/geocoding profiles.
- Не декомпозировать `datasets/moscow_city_open_data.md` на maintained dataset notes, пока official `data.mos.ru` catalog coverage, export semantics, operational terms и product boundaries не будут проверены достаточно глубоко для maintained API-first route.
- Для будущего procurement/tender API comparison получить actual documents/schemas из official `zakupki.gov.ru` technical-information subsection `Требования к информационному взаимодействию ЕИС с другими информационными системами`, затем собрать official primary-source evidence по Seldon.Tenders/Seldon.Win и альтернативным поставщикам; baseline и technical-info recheck сохранены в `research/procurement-tender/`.
- Продолжить разбор API Portal только как discovery source: каждую существенную карточку проверять по primary sources.

## Низкий приоритет

- После ручной проверки перенести исторические-only материалы в `legacy/`, если это улучшит навигацию и не потеряет provenance.
- Поддерживать индекс legacy-материалов и обновлять его при появлении новых исторических слоёв.
- Расширять needs routes после появления новых сравнений и подтверждённых API profiles; следующий возможный кандидат - отдельный маршрут по self-hosted/open-data geocoding после legal/benchmark review.
- Поддерживать отдельный маршрут `needs/routing-logistics/` и не смешивать routing с geocoding, places, map tiles или delivery optimization.
- Сохранить `datasets/procurement_tender_contracts.md` как provenance; не выдавать старые API Portal claims за current API evidence.

## Legacy Backlog

Эти направления были найдены в старом dataset-centric backlog и остаются исследовательскими кандидатами. Они не считаются подтвержденными API profiles:

- Цены на топливо.
- Справочник АЗС.
- Дорожный трафик и пробки.
- Погода и метеоистория.
- История транспортных средств.
- Недвижимость и кадастровые данные: reviewed official-access profile, comparison, need route и procurement kit созданы; дальнейший рост зависит от official clarification и lawful test access.
- Платежи и финтех-транзакции.
- Маркетинговые и телекоммуникационные аудитории.
- Доставка, логистика и курьерские события.
- Маркетплейсы и товарные каталоги.
- Судебные, санкционные и исполнительные данные.
- Медицинские и телемедицинские данные.

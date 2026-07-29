# Запрос поставщику - 2GIS Suggest, Places и Geocoder APIs

[English version](provider-request-2gis-search.md)

Этот checklist подготовлен для разговора с 2GIS о Suggest API, Places API и Geocoder API в семействе 2GIS Search API. Он не должен считаться ответами поставщика, пока 2GIS не ответит письменно или не предоставит официальную документацию.

## Контекст

Atlas сейчас рассматривает [`2GIS Suggest API`](../../apis/2gis-suggest-api/README.ru.md), [`2GIS Places API`](../../apis/2gis-places-api/README.ru.md) и [`2GIS Geocoder API`](../../apis/2gis-geocoder-api/README.ru.md) как отдельные активные reviewed-продукты. Открытые blockers Atlas: OpenAPI/Swagger, SLA, точные storage/caching/display/SaaS rights, batch restrictions, on-demand field/method matrix и независимые quality benchmarks.

## Материалы Atlas для приложения

- [`apis/2gis-suggest-api/README.ru.md`](../../apis/2gis-suggest-api/README.ru.md)
- [`apis/2gis-places-api/README.ru.md`](../../apis/2gis-places-api/README.ru.md)
- [`apis/2gis-geocoder-api/README.ru.md`](../../apis/2gis-geocoder-api/README.ru.md)
- [`apis/2gis-suggest-api/evidence.ru.md`](../../apis/2gis-suggest-api/evidence.ru.md)
- [`apis/2gis-places-api/evidence.ru.md`](../../apis/2gis-places-api/evidence.ru.md)
- [`apis/2gis-geocoder-api/evidence.ru.md`](../../apis/2gis-geocoder-api/evidence.ru.md)
- [`comparisons/address-normalization-geocoding/README.ru.md`](../../comparisons/address-normalization-geocoding/README.ru.md)
- [`procurement/address-geocoding-api-selection/RFP.ru.md`](../../procurement/address-geocoding-api-selection/RFP.ru.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md)

## Границы продуктов

1. Подтвердите точную границу между Suggest API, Places API, Geocoder API, Routing APIs и любыми On-Premise/API export products.
2. Какие сценарии требуют закупки более одного 2GIS Search product?
3. Когда после Suggest result нужно делать Places request, Geocoder request или вызывать другой API?
4. Какие APIs покрывают address suggestions, street suggestions, organization suggestions, organization/place search, direct geocoding и reverse geocoding?
5. Какие capabilities недоступны в public cloud API и требуют On-Premise, custom project или separate contract?

## Methods and field matrix

1. Предоставьте complete method catalog для Suggest, Places и Geocoder.
2. Предоставьте field matrix по product, method, package, geography и object type.
3. Какие Places fields и methods являются on-demand или extra-cost: contacts, rubrics, ITIN/INN, FIAS identifiers, OKATO/OKTMO, building details, attributes, geotags или другие fields?
4. Какие Geocoder fields включены by default, а какие требуют extra paid access?
5. Какие Suggest types поддерживаются для object, address, street и route-endpoint suggestions?
6. Какие identifiers можно безопасно использовать across Suggest, Places and Geocoder workflows?
7. Какие fields являются provider-reported, registry-derived, user-generated, inferred или quality-scored?

## Protocol, authentication и key handling

1. Подтвердите production base URLs для Suggest, Places и Geocoder.
2. Выпускаются и тарифицируются ли API keys отдельно по product, project или subscription?
3. Можно ли ограничить keys по domain, IP, app, environment, product или method?
4. Доступны ли отдельные credentials для demo/test и production?
5. Как keys ротируются, отзываются и мониторятся?
6. Есть ли method-level permissions, чтобы избежать случайного использования paid on-demand methods?

## Formats, schemas, versioning и errors

1. Доступны ли OpenAPI/Swagger specifications для Suggest, Places и Geocoder?
2. Какие request and response formats официально поддерживаются?
3. Предоставьте sample requests and responses для address suggestions, organization suggestions, place lookup, direct geocoding и reverse geocoding.
4. Какие error codes и retry guidance применяются к validation errors, authentication failures, quota errors, rate limits, no-result responses и provider incidents?
5. Как устроено API versioning?
6. Какой notice period действует для method deprecations, field removals, tariff changes, on-demand field changes и coverage changes?

## Pricing and billing

1. Подтвердите product-specific prices для Suggest, Places и Geocoder.
2. Charges считаются по successful requests, units, methods, fields, packages, records, objects или другому unit?
3. Какие on-demand fields и methods имеют отдельную цену?
4. Как тарифицируются retries, duplicate requests, no-result responses, partial responses, cached results и errors?
5. Какие minimum commitment, setup fee, support fee, SLA fee или On-Premise fee применяются?
6. Как покупателю считать workflow, где Suggest используется для UI, Places получает full objects, а Geocoder разрешает адреса или координаты?

## Limits, quotas and batch

1. Какие production per-minute, per-second, burst, concurrency, daily и monthly limits действуют для каждого продукта?
2. Limits считаются per key, account, IP, product, method, subscription или contract?
3. Можно ли согласовать публичные 600 Search units/minute limits?
4. Какие demo limits действуют для каждого продукта?
5. Разрешены ли batch, asynchronous, offline или warehouse-enrichment use cases?
6. Какие maximum batch size, file size, record count и processing windows, если batch доступен?

## Storage, caching, display and legal use

1. Подтвердите, доступно ли caching при какой-либо license, несмотря на то что reviewed WebAPI offer says caching is not provided.
2. Можно ли хранить API responses? Если да, какие fields, как долго и по каким refresh rules?
3. Можно ли показывать results customers, partners, affiliates или SaaS users?
4. Должны ли results показываться вместе с 2GIS maps, attribution, copyright notices или links?
5. Можно ли redistribute, resell, export, embed data in third-party products или использовать across affiliates?
6. Можно ли использовать outputs для scoring, model training, analytics, deduplication или address-quality decisions?
7. Какие fields содержат персональные данные или regulated information, и какие DPA или jurisdiction terms применяются?
8. Какие deletion, audit, attribution и post-termination obligations применяются?

## Coverage, freshness and quality

1. Какие countries, regions и cities покрывают Suggest, Places и Geocoder?
2. Какова update cadence для address, building, organization и place data?
3. Какие freshness guarantees или expected lag применяются?
4. Какие quality indicators доступны для match level, coordinate precision, address ambiguity и object status?
5. Может ли 2GIS предоставить benchmark guidance для Москвы, Санкт-Петербурга, региональных городов, ambiguous addresses, building corpus/structure cases и organization categories?

## SLA, support and change management

1. Какие uptime SLA, latency SLA, support response SLA и data-freshness SLA доступны?
2. Есть ли public или customer status page для Search API incidents?
3. Какие support channels входят в package?
4. Какие remedies применяются при SLA breach?
5. Есть ли API changelog, customer notification process, RSS feed, mailing list или portal?
6. Какой notice period действует для breaking changes и pricing changes?

## Запрошенные приложения

- Product boundary note for Suggest, Places, Geocoder, Routing and On-Premise.
- Method and field matrix with on-demand fields.
- OpenAPI/Swagger или complete specifications.
- Sample requests and responses.
- Error-code reference and retry guidance.
- Product-specific tariff appendix.
- SLA/support appendix.
- Storage, caching, display, attribution, redistribution, affiliate-use and SaaS terms.
- Changelog, deprecation and breaking-change policy.

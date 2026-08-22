# Запрос поставщику - DaData Address APIs

[English version](provider-request-dadata-address.md)

Этот checklist подготовлен для разговора с DaData об address suggestions, address cleaning, direct geocoding и reverse geocoding. Он не должен считаться ответами поставщика, пока DaData не ответит письменно или не предоставит официальную документацию.

## Контекст

Atlas сейчас рассматривает [`DaData Address APIs`](../../apis/dadata-address-api/README.ru.md) как активного reviewed-кандидата для российских адресных подсказок, очистки адресов, прямого геокодирования и обратного геокодирования. Открытые blockers Atlas: endpoint-specific права хранения данных, SLA, support tiers, endpoint-level OpenAPI scope, batch/asynchronous options и независимый benchmark качества.

## Материалы Atlas для приложения

- [`apis/dadata-address-api/README.ru.md`](../../apis/dadata-address-api/README.ru.md)
- [`apis/dadata-address-api/evidence.ru.md`](../../apis/dadata-address-api/evidence.ru.md)
- [`comparisons/address-normalization-geocoding/README.ru.md`](../../comparisons/address-normalization-geocoding/README.ru.md)
- [`procurement/address-geocoding-api-selection/RFP.ru.md`](../../procurement/address-geocoding-api-selection/RFP.ru.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md)

## Граница продукта

1. Какие адресные endpoints DaData входят в стандартное API-предложение: address suggestions, address cleaning, direct geocoding, reverse geocoding, postal enrichment, FIAS/GAR identifiers, KLADR identifiers, cadastral lookup или другие методы?
2. Какие address capabilities относятся к subscription services, а какие являются pay-per-record services?
3. Какие возможности находятся вне стандартного address API scope и требуют отдельного договора, кастомного проекта или file-processing service?
4. Могут ли company suggestions, party enrichment или counterparty data поставляться вместе с address APIs, или их нужно закупать отдельно?
5. Какие страны и уровни детализации адреса покрывает каждый endpoint?

## Методы и field matrix

1. Предоставьте полный список endpoints и методов для address suggestions, cleaning, direct geocoding и reverse geocoding.
2. Предоставьте field matrix по endpoint, тарифу/пакету, стране и уровню детализации адреса.
3. Какие поля возвращаются для FIAS/GAR, KLADR, postal code, geolocation, timezone, tax office, region, city, street, house, block, building, structure и flat/apartment data?
4. Какие quality fields показывают house-level, street-level, locality-level, inferred, ambiguous, missing или approximate matches?
5. Какие поля являются registry-derived, provider-calculated, normalized, echoes of user input или inferred?
6. У каких полей есть update dates, source references, confidence levels или quality codes?

## Protocol, authentication и key handling

1. Подтвердите production base URLs для всех address endpoints.
2. Какие endpoints требуют только API token, а какие требуют token и secret key?
3. Какие endpoints можно безопасно вызывать из browser JavaScript, mobile apps, backend systems и serverless environments?
4. Как выпускать, ограничивать, ротировать и отзывать keys по domain, IP, app или environment?
5. Доступны ли отдельные credentials для sandbox/test и production?
6. Есть ли method-level permissions, чтобы исключить случайные cleaning/geocoding charges в suggestions-only integration?

## Formats, schemas, versioning и errors

1. Предоставьте endpoint-specific schemas или OpenAPI/Swagger coverage для address suggestions, cleaning, direct geocoding и reverse geocoding.
2. Какие request/response formats, encodings и date formats поддерживаются?
3. Как представлены nullable fields, unknown registry identifiers, partial matches и quality codes?
4. Какая error model используется для validation errors, not-found results, quota errors, authentication failures, throttling и provider incidents?
5. Как устроено API versioning?
6. Какой notice period действует для field removals, schema changes, endpoint deprecations, pricing changes и source-coverage changes?

## Sandbox, trial и benchmark

1. Может ли DaData предоставить test credentials для всех address endpoints без раскрытия production keys?
2. Являются ли test requests платными?
3. Соответствует ли public playground production schemas, rate limits, quality codes и edge cases?
4. Может ли покупатель провести reproducible benchmark на legal synthetic или public address sample?
5. Можно ли хранить benchmark outputs в Atlas или internal procurement evidence с request IDs и timestamps?
6. Какую поддержку DaData может дать для интерпретации quality codes и coordinate precision во время пилота?

## Batch, async и file processing

1. Ограничен ли address cleaning одним address per HTTP request в стандартном API?
2. Доступны ли batch HTTP requests, asynchronous jobs, file upload, SFTP delivery, callbacks или webhook delivery для high-volume cleaning/geocoding?
3. Какие maximum record count, file size, request payload size, processing window и concurrency limits?
4. Отличаются ли batch и file-processing terms по цене от per-record API cleaning?
5. Как тарифицируются duplicate records, retries, validation errors и partial failures?
6. Разрешено ли использовать suggestions endpoints для automatic processing of address files or databases при каком-либо договорном варианте?

## Pricing and billing

1. Предоставьте endpoint-level pricing для suggestions, address cleaning, direct geocoding, reverse geocoding, cadastral lookup и дополнительного address enrichment.
2. Какие quotas общие для subscription services?
3. Какие limits действуют per IP, per token, per account, per method, per day, per second или per contract?
4. Какие minimum commitment, setup fee, support fee или SLA fee применяются?
5. Как тарифицируются overage, retries, invalid requests, not-found results, cached results и duplicate records?
6. Какие цены являются именно API prices, а не ценами web UI, file-upload или manual-processing?

## Limits, SLA и support

1. Какие production rate limits действуют по endpoint, тарифу и договору?
2. Можно ли согласовать burst, concurrency, daily, monthly или new-connection limits?
3. Какие uptime SLA, latency SLA, support response SLA и data-freshness SLA доступны?
4. Есть ли public или customer status page, incident channel, maintenance notice process или support escalation path?
5. Какие remedies применяются при SLA breach?
6. Доступны ли enterprise support, private channel или dedicated account-management options?

## Data rights and legal use

1. Может ли покупатель хранить API responses от suggestions, cleaning, direct geocoding и reverse geocoding? Если да, как долго?
2. Можно ли cache responses? Если да, какие TTL и refresh rules?
3. Можно ли хранить normalized addresses, coordinates, FIAS/GAR identifiers и quality codes в CRM, ERP, warehouse или master-data system покупателя?
4. Можно ли показывать результаты customers, partners, affiliates или SaaS users?
5. Можно ли redistribute, resell, export или embed results в third-party products?
6. Можно ли использовать outputs для scoring, deduplication, fraud checks, model training, address-quality analytics или automated decisions?
7. Какие address fields могут содержать персональные данные или personal-data-like information, и какие legal roles и DPA terms применяются?
8. Какие retention, deletion, audit, attribution и post-termination obligations применяются?

## Запрошенные приложения

- Endpoint-specific specification или OpenAPI/Swagger.
- Method and field matrix.
- Sample requests and responses for suggestions, cleaning, direct geocoding and reverse geocoding.
- Quality-code and coordinate-precision guide.
- Error-code reference.
- Sandbox/test credential instructions.
- Endpoint-level price list and quota table.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS-embedding terms.
- Changelog, deprecation and breaking-change policy.

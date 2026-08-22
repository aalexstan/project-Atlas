# Запрос поставщику — Seldon.Basis API

[English version](provider-request.md)

Этот checklist подготовлен для разговора с Seldon. Он не является ответом поставщика, пока Seldon не предоставит письменный ответ или официальную документацию.

## Контекст

Atlas сейчас рассматривает Seldon.Basis API как активного reviewed enterprise-кандидата для company enrichment, relationship analysis, procurement context и risk analysis. Открытые blockers Atlas: method pricing, batch billing, authentication, SLA, data rights и versioning.

## Материалы Atlas для приложения

- [`apis/seldon-basis/README.ru.md`](../../apis/seldon-basis/README.ru.md)
- [`apis/seldon-basis/evidence.ru.md`](../../apis/seldon-basis/evidence.ru.md)
- [`comparisons/company-counterparty-data-russia/README.ru.md`](../../comparisons/company-counterparty-data-russia/README.ru.md)
- [`procurement/counterparty-api-selection/docs/RFP.ru.md`](../../procurement/counterparty-api-selection/docs/RFP.ru.md)

## Scope продукта

1. Какие Seldon.Basis API products, packages и methods входят в предложение?
2. Где граница между Seldon.Basis API, Seldon 1.7, Seldon.Tenders/Seldon.Win, monitoring, sanctions/compliance и international company data?
3. Какие countries, entity types и registry/source categories покрыты?
4. Какие relationship graph, procurement, court, finance, enforcement, license, media и sanctions fields входят в standard package?
5. Какие fields являются source-derived, provider-calculated, manually curated, inferred или score-like?

## Methods and fields

1. Предоставьте complete method catalog.
2. Предоставьте method-by-field matrix с source, update cadence и package availability.
3. Какие lookup keys поддерживаются: INN, OGRN, KPP, name, address, manager, owner, phone, website, procurement identifier или foreign identifier?
4. Какие methods поддерживают relationship graphs, affiliated persons, owners, managers, procurement context и monitoring events?
5. Какие methods возвращают source documents, timestamps, confidence levels или source references?

## Protocol and authentication

1. Предоставьте Swagger/OpenAPI или complete API specification.
2. Какой production base URL?
3. Какая authentication model используется: API key, token, OAuth, mTLS, IP allowlist, signed request или другая model?
4. Sandbox и production credentials разделены?
5. Как управляются method permissions, key rotation и IP restrictions?

## Formats, versioning and errors

1. Какие request/response formats поддерживаются?
2. Подтвердите JSON schemas и любые XML/CSV/export options.
3. Как устроено API versioning?
4. Какой breaking-change policy и notice period?
5. Предоставьте error codes для not-found, partial result, validation, authentication, quota, throttling и incident states.
6. Какой retry/backoff и idempotency guidance применяется?

## Pricing and billing

1. Предоставьте API-specific pricing, не web-product pricing.
2. Как тарифицируются universal package и individual per-method plans?
3. Какие methods включены в universal package?
4. Как считается batch billing?
5. Как тарифицируются not-found results, errors, retries, duplicate lookups и cached results?
6. Какие minimum commitment, setup fee, support fee и overage rules применяются?
7. Есть ли separate fees для relationship graph, monitoring, procurement, international, sanctions или portfolio functions?

## Batch, async and monitoring

1. Подтвердите maximum batch size, включая publicly reported 1,000 taxpayer IDs.
2. Доступны ли asynchronous jobs для large batches?
3. Поддерживаются ли webhooks, callbacks, exports, SFTP или scheduled portfolio updates?
4. Доступны ли monitoring events through API?
5. Как batch partial failures представлены и тарифицируются?
6. Можно ли согласовать method-level daily request limits?

## Limits, SLA and support

1. Какие production daily, monthly, burst, concurrency и per-second limits по method?
2. Limits считаются per key, account, IP, method, user или contract?
3. Какие uptime SLA, latency SLA и support response SLA доступны?
4. Какой data freshness SLA или expected source-update delay действует?
5. Есть ли status page, incident history, maintenance notice process или customer mailing list?
6. Какие remedies применяются при SLA breach?

## Data rights and legal use

1. Можно ли хранить API responses? Если да, сколько и по каким refresh rules?
2. Можно ли cache responses? Если да, какой TTL?
3. Можно ли показывать results customers, partners, affiliates или SaaS users?
4. Можно ли redistribute, resell, export или embed data in third-party products?
5. Можно ли использовать outputs для scoring, automated decisions, model training, deduplication или internal analytics?
6. Какие fields contain personal data и какие roles, DPA terms and jurisdiction apply?
7. Какие retention, deletion, audit и post-termination obligations применяются?

## Source-risk clarification

1. Подтвердите текущие official documentation domains и какие historical `api-seldon.ru` materials считаются obsolete.
2. Укажите official changelog или migration notes от legacy documentation к текущей документации `seldongroup.ru`.

## Запрошенные приложения

- Swagger/OpenAPI или complete specification.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- API-specific price list.
- Batch billing appendix.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS terms.
- Changelog or versioning policy.

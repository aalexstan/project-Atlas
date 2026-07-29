# Запрос поставщику — Kontur.Focus API

[English version](provider-request.md)

Этот checklist подготовлен для разговора с Контуром. Он не является ответом поставщика, пока Контур не предоставит письменный ответ или официальную документацию.

## Контекст

Atlas сейчас рассматривает Kontur.Focus API как активного reviewed enterprise-кандидата для проверки компаний и контрагентов. Открытые blockers Atlas: API-specific price, production limits, SLA, полная спецификация, storage rights, redistribution rights и contract appendices.

## Материалы Atlas для приложения

- [`apis/kontur-focus/README.ru.md`](../../apis/kontur-focus/README.ru.md)
- [`apis/kontur-focus/evidence.ru.md`](../../apis/kontur-focus/evidence.ru.md)
- [`comparisons/company-counterparty-data-russia/README.ru.md`](../../comparisons/company-counterparty-data-russia/README.ru.md)
- [`procurement/counterparty-api-selection/docs/RFP.ru.md`](../../procurement/counterparty-api-selection/docs/RFP.ru.md)

## Scope продукта

1. Какие продукты, модули и методы Kontur.Focus API входят в стандартное API-предложение?
2. Какие возможности находятся вне standard API и требуют отдельной лицензии, custom project или ручного сервиса?
3. Входят ли monitoring, risk flags, arbitration, enforcement proceedings, beneficial ownership, finance, sanctions/compliance или international company data?
4. Какие юридические лица, ИП, филиалы, иностранные entities и исторические записи покрыты?
5. Какие поля provider-calculated, source-derived, manually curated или inferred?

## Methods and field matrix

1. Предоставьте complete method catalog.
2. Предоставьте field matrix по method, tariff/package и data source.
3. Какие lookup keys поддерживаются: INN, OGRN, KPP, name, address, manager, founder, phone, email, bank account или foreign identifier?
4. Какие методы возвращают current data, historical data, source documents, risk indicators, monitoring events или relationship graphs?
5. У каких полей есть source references, timestamps, confidence levels, update dates или legal-source identifiers?

## Specification and authentication

1. Предоставьте OpenAPI/Swagger или complete API specification.
2. Какой production base URL?
3. Какая authentication model используется: developer key, API key, OAuth, token, mTLS, IP allowlist, signed request или другое?
4. Как keys issued, rotated, revoked and scoped?
5. Sandbox и production credentials разделены?
6. Sandbox behavior совпадает с production по schemas, errors, limits и sample data?

## Formats, versioning and errors

1. Какие request/response formats поддерживаются?
2. Какие encoding и date/time formats используются?
3. Как устроено API versioning?
4. Какой breaking-change policy и notice period?
5. Предоставьте error codes для validation, not-found, quota, authentication, throttling, partial failure и provider incidents.
6. Какой retry, idempotency and backoff guidance действует?

## Pricing and billing

1. Предоставьте API-specific pricing, не web-product pricing.
2. Pricing основан на request, successful request, method, field, record, package, company, monitoring event или другой единице?
3. Какие fields, reports или methods оплачиваются отдельно?
4. Какие minimum commitment, setup fee, support fee и integration fee?
5. Как тарифицируются overage, retries, duplicate requests, not-found results и partial failures?
6. Доступны ли volume tiers, annual discounts или multi-entity group licenses?

## Batch, monitoring and delivery

1. Какие методы поддерживают batch requests?
2. Какие maximum batch size, file size, record count и processing window?
3. Поддерживаются ли asynchronous jobs?
4. Поддерживаются ли webhooks, callbacks, exports, SFTP или scheduled deliveries?
5. Как monitoring events generated, deduplicated and billed?
6. Доступны ли portfolio-level alerts through API?

## Limits, SLA and support

1. Какие production daily, monthly, burst, concurrency и per-second limits по method?
2. Limits считаются per key, account, IP, method, user или contract?
3. Какие uptime SLA, latency SLA и support response SLA доступны?
4. Какой data freshness SLA или expected source-update delay применяется?
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

## Запрошенные приложения

- OpenAPI/Swagger или complete specification.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- API-specific price list.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS terms.
- Changelog or versioning policy.

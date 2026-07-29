# Запрос поставщику - OpenCage Geocoding API

[English version](provider-request.md)

Этот checklist подготовлен для разговора с OpenCage про OpenCage Geocoding API. Его нельзя считать ответами поставщика, пока OpenCage не ответит письменно или не укажет official documentation.

## Контекст

Atlas рассматривает [`OpenCage Geocoding API`](../../apis/opencage-geocoding-api/README.ru.md) как active reviewed hosted commercial open-data geocoding route. Public blockers: ODbL/attribution interpretation, redistribution/SaaS rights, enterprise SLA, privacy/DPA, benchmark quality и high-volume batch workflow fit.

## Граница продукта

1. Подтвердите boundary между Geocoding API, Geosearch/autosuggest, spreadsheet upload и enterprise/custom services.
2. Даёт ли Geocoding API address validation guarantees или только geocoding confidence/components?
3. Какие use cases требуют Geosearch вместо Geocoding API?
4. Routing, distance matrix, place search или address cleaning доступны как отдельные products или out of scope?

## Методы, схемы и версионирование

1. Предоставьте current OpenAPI specification или complete method reference.
2. Какие response fields являются stable identifiers, display labels, coordinates, confidence values, components и attribution/source indicators?
3. Какие request и response formats поддерживаются long-term?
4. Какие error codes, retry guidance и idempotency rules действуют?
5. Какой notice period применяется к breaking changes, field removals, pricing changes, data-source changes и deprecations?

## Pricing, Quotas and Billing

1. Подтвердите current pricing currency для страны покупателя, VAT/tax treatment и annual options.
2. Как soft subscription limits работают договорно, если daily averages repeatedly exceed the plan?
3. Как billed failed, invalid, no-result и retried requests?
4. Какие daily, monthly, per-second, burst and concurrency limits apply by plan?
5. Доступны ли higher RPS limits без enterprise contract?
6. Какой minimum commitment, setup fee, support fee или SLA fee применяется к enterprise plans?

## Storage, Attribution and Data Rights

1. Какие response fields можно хранить permanently?
2. Какую attribution нужно показывать in maps, non-map UI, exports, printed reports and customer-facing SaaS?
3. Какие ODbL obligations применяются к cached results, derived databases, normalized address tables и geocoded customer datasets?
4. Разрешены ли redistribution, resale, API proxying, affiliate use или white-label SaaS embedding?
5. Есть ли deletion, refresh или post-termination duties?
6. Можно ли использовать outputs для scoring, analytics, routing pre-processing, ML/model training или address-quality decisions?

## Batch and Operations

1. Какой recommended production design для millions of records, если API accepts one location per request?
2. Какие spreadsheet upload limits, retention periods и audit evidence apply by plan?
3. Как buyers должны обрабатывать parallelization, partial failures, retries, no-result responses и duplicate submissions?
4. Есть ли status pages, incident notifications и usage exports?

## Privacy, Security and Compliance

1. Доступен ли DPA?
2. Какие data centers process default API requests?
3. Может ли customer select EU-only или other regional processing?
4. Какие personal-data restrictions apply to submitted addresses or coordinates?
5. Как buyers должны использовать `no_record`, и влияет ли это на support/debugging?
6. Доступны ли IP restrictions, domain/CORS restrictions, key rotation и per-project permissions?

## Benchmark and Pilot

1. Может ли OpenCage предоставить pilot credentials для legal benchmark sample?
2. Можно ли хранить benchmark request/response evidence internally for procurement audit?
3. Какие metrics OpenCage recommends для precision, match level, latency, false positives и missing results?
4. Может ли OpenCage помочь интерпретировать confidence scores и components for house/street/locality-level results?

## Requested Attachments

- OpenAPI specification или current complete method reference.
- Field/source/attribution matrix.
- Paid-plan and enterprise terms.
- SLA/support appendix.
- DPA/privacy/security materials.
- High-volume operations guide.
- Changelog/deprecation policy.

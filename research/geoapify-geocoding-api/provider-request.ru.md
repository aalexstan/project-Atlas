# Запрос поставщику - Geoapify Geocoding API

[English version](provider-request.md)

Этот checklist подготовлен для разговора с Geoapify о Geoapify Geocoding API. Он не является ответом поставщика, пока Geoapify не ответит письменно или не укажет official documentation.

## Контекст

Atlas рассматривает [`Geoapify Geocoding API`](../../apis/geoapify-geocoding-api/README.ru.md) как активный reviewed hosted commercial open-data geocoding route. Публичные blockers: ODbL/attribution interpretation, DPA/privacy, SaaS/redistribution rights, benchmark quality, batch edge cases и contract terms для paid/enterprise plans.

## Граница продукта

1. Подтвердите границу между Geocoding API, Address Autocomplete, Places API, Place Details, Routing, Matrix и Isochrone APIs.
2. Какие функции используют тот же credit model, а какие требуют отдельных products или contracts?
3. Даёт ли Geocoding API address validation guarantees или только geocoding confidence/match metadata?
4. Какие use cases требуют Places API вместо Geocoding API?

## Methods, schemas and versioning

1. Предоставьте текущую OpenAPI/Swagger specification или полный method reference для forward, reverse и batch geocoding.
2. Какие response fields являются stable identifiers, display labels, coordinates, confidence values, data-source fields и administrative hierarchy?
3. Какие request/response formats официально поддерживаются в production?
4. Какие error codes, retry guidance и idempotency rules применяются?
5. Какой notice period действует для breaking changes, field removals, tariff changes, data-source changes и deprecations?

## Pricing, quotas and billing

1. Подтвердите credit cost для forward, reverse, autocomplete, batch, failed и no-result request.
2. Как billed retries, duplicates, partial failures и expired batch results?
3. Какие daily credits, RPS, concurrency и burst limits действуют по планам?
4. Доступны ли higher RPS limits без dedicated geocoding server?
5. Какие minimum commitment, setup fee, support fee или SLA fee действуют для enterprise plans?

## Storage, attribution and data rights

1. Какие response fields можно хранить permanently?
2. Какой attribution нужен в maps, non-map UI, exports, printed reports и customer-facing SaaS?
3. Какие ODbL obligations возникают для cached results, derived databases, normalized address tables и geocoded customer datasets?
4. Разрешены ли redistribution, resale, API proxying, affiliate use или white-label SaaS embedding?
5. Есть ли deletion, refresh или post-termination duties?
6. Можно ли использовать outputs для scoring, analytics, routing pre-processing, ML/model training или address-quality decisions?

## Batch and operations

1. Какие production limits действуют для batch input count, concurrent jobs, daily batch credits и result retention?
2. Поддерживаются ли larger batch jobs по договору?
3. Как buyer должен обрабатывать partial failures, polling, retries, expired results и audit evidence?
4. Доступны ли status pages, incident notifications и usage exports?

## Privacy, security and compliance

1. Доступен ли DPA?
2. В каких data centers обрабатываются default API requests?
3. Может ли customer выбрать EU-only или другое regional processing?
4. Какие personal-data restrictions применяются к submitted addresses или coordinates?
5. Доступны ли IP/domain restrictions, key rotation и per-project permissions?

## Benchmark and pilot

1. Может ли Geoapify предоставить pilot credentials для legal benchmark sample?
2. Можно ли хранить benchmark request/response evidence internally for procurement audit?
3. Какие metrics Geoapify рекомендует для precision, match level, latency, false positives и missing results?
4. Может ли Geoapify помочь интерпретировать confidence scores и match levels для house/street/locality-level results?

## Requested attachments

- OpenAPI/Swagger или current complete specification.
- Field matrix and source/attribution matrix.
- Paid-plan terms and enterprise contract appendix.
- SLA/support appendix.
- DPA/privacy/security materials.
- Batch operations guide.
- Changelog/deprecation policy.

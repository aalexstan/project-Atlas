# Запрос поставщику - Yandex Maps Geosuggest, Geocoder и Organization Search APIs

[English version](provider-request-yandex-maps.md)

Этот checklist подготовлен для разговора с Yandex о Yandex Maps Geosuggest API, Yandex Maps Geocoder API и Yandex Maps Organization Search API. Он не должен считаться ответами поставщика, пока Yandex не ответит письменно или не предоставит официальную документацию.

## Контекст

Atlas сейчас рассматривает [`Yandex Maps Geosuggest API`](../../apis/yandex-maps-geosuggest-api/README.ru.md), [`Yandex Maps Geocoder API`](../../apis/yandex-maps-geocoder-api/README.ru.md) и [`Yandex Maps Organization Search API`](../../apis/yandex-maps-organization-search-api/README.ru.md) как отдельные активные reviewed-продукты. Открытые blockers Atlas: production RPS/SLA там, где они не опубликованы, точные storage/display/SaaS rights, batch/offline restrictions, OpenAPI availability и независимые quality benchmarks.

## Материалы Atlas для приложения

- [`apis/yandex-maps-geosuggest-api/README.ru.md`](../../apis/yandex-maps-geosuggest-api/README.ru.md)
- [`apis/yandex-maps-geocoder-api/README.ru.md`](../../apis/yandex-maps-geocoder-api/README.ru.md)
- [`apis/yandex-maps-organization-search-api/README.ru.md`](../../apis/yandex-maps-organization-search-api/README.ru.md)
- [`apis/yandex-maps-geosuggest-api/evidence.ru.md`](../../apis/yandex-maps-geosuggest-api/evidence.ru.md)
- [`apis/yandex-maps-geocoder-api/evidence.ru.md`](../../apis/yandex-maps-geocoder-api/evidence.ru.md)
- [`apis/yandex-maps-organization-search-api/evidence.ru.md`](../../apis/yandex-maps-organization-search-api/evidence.ru.md)
- [`comparisons/address-normalization-geocoding/README.ru.md`](../../comparisons/address-normalization-geocoding/README.ru.md)
- [`procurement/address-geocoding-api-selection/RFP.ru.md`](../../procurement/address-geocoding-api-selection/RFP.ru.md)
- [`procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md`](../../procurement/address-geocoding-api-selection/TEST_PROTOCOL.ru.md)

## Границы продуктов

1. Подтвердите точную границу между Geosuggest API, Geocoder API, Organization Search API, other Search APIs, routing, matrix APIs и JavaScript map components.
2. Какие Geosuggest responses предполагается разрешать через Geocoder API, и какие fields или identifiers нужно использовать для handoff?
3. Даёт ли Geosuggest только organization autocomplete, или его можно использовать как full organization search product?
4. Какие Organization Search use cases требуют Organization Search API, а не Geosuggest или Geocoder?
5. Даёт ли Geocoder какие-либо address normalization или validation guarantees помимо geocoding precision metadata?
6. Какие возможности требуют отдельных лицензий или договоров?

## Methods and field matrix

1. Предоставьте complete method and parameter matrix для Geosuggest, Geocoder и Organization Search.
2. Какие fields возвращаются для address suggestions, geographic objects, organizations, coordinates, precision, administrative hierarchy и metadata?
3. Какие fields являются stable identifiers, display labels, provider-internal identifiers, temporary URIs или geocoder handoff values?
4. Какие parameters влияют на geography, language, bounding boxes, result type, result count и strict bounds?
5. Какие fields доступны только в отдельных license variants?
6. Есть ли отдельная field semantics для России, стран СНГ, Турции или других регионов?

## Protocol, authentication и key handling

1. Подтвердите production base URLs для Geosuggest, Geocoder и Organization Search.
2. Выпускаются, ограничиваются и тарифицируются ли API keys отдельно для Geosuggest, Geocoder и Organization Search?
3. Можно ли ограничить keys по domain, IP, app, environment или API family?
4. Доступны ли отдельные credentials для test и production?
5. Как keys ротируются, отзываются и ограничиваются по scope?
6. Есть ли per-method permissions, чтобы исключить случайное платное использование Geosuggest, Geocoder, Search или routing APIs?

## Formats, schemas, versioning и errors

1. Доступны ли OpenAPI/Swagger specifications для Geosuggest, Geocoder и Organization Search?
2. Какие request and response formats официально поддерживаются?
3. Какие error codes и retry guidance применяются к validation errors, authentication failures, quota exhaustion, rate limits, not-found results и provider incidents?
4. Как устроено API versioning?
5. Какой notice period действует для breaking changes, field removals, tariff changes, deprecations и coverage changes?
6. Есть ли official changelog, mailing list, status page или customer notification process?

## Pricing and billing

1. Подтвердите API-specific pricing для Geosuggest, Geocoder и Organization Search по license type и request package.
2. Что входит в Standard и Extended licenses для каждого продукта?
3. Какая license позволяет data storage, и какие именно data можно хранить?
4. Как тарифицируются additional requests, retries, failed requests, no-result responses, duplicate requests и cached results?
5. Какие minimum commitment, setup fee, support fee или SLA fee применяются?
6. Как покупателю считать workflow, где Geosuggest suggestions вызывают Geocoder requests и/или Organization Search requests?

## Limits, quotas и production suitability

1. Какие production requests-per-second limits действуют для Geosuggest, Geocoder и Organization Search?
2. Limits считаются per key, account, IP, API family, project, domain или contract?
3. Можно ли согласовать burst, concurrency, daily и monthly quotas?
4. Какие limits действуют для test-period keys?
5. Разрешён ли batch или offline geocoding при каком-либо договоре?
6. Есть ли ограничения на automated enrichment of address files, CRM databases или data warehouses?

## Display, storage and data rights

1. Когда Geosuggest, Geocoder или Organization Search results должны показываться на карте Yandex?
2. Можно ли показывать results на third-party maps или в non-map UI?
3. Может ли покупатель хранить suggestions, selected labels, coordinates, geocoder precision, administrative fields и raw responses?
4. Можно ли cache results? Если да, какие TTL и refresh rules?
5. Можно ли показывать results customers, partners, affiliates или SaaS users?
6. Разрешены ли redistribution, resale, export или embedding in third-party products?
7. Можно ли использовать outputs для scoring, analytics, model training, routing pre-processing или address-quality decisions?
8. Какие attribution, copyright notice и post-termination deletion duties применяются?

## Sandbox, trial и benchmark

1. Может ли Yandex предоставить test credentials для обоих продуктов с realistic limits?
2. Являются ли test requests платными?
3. Может ли покупатель провести side-by-side benchmark с DaData, 2GIS, FIAS/GAR или self-hosted Nominatim на legal sample?
4. Можно ли хранить benchmark request/response evidence внутри компании для procurement audit?
5. Какие metrics Yandex рекомендует для precision, match level, latency и user-input autocomplete quality?

## SLA and support

1. Какие uptime SLA, latency SLA, support response SLA и incident communication доступны?
2. Есть ли public или customer status page для Maps API incidents?
3. Какие support channels входят в license?
4. Какие remedies применяются при SLA breach?
5. Доступен ли enterprise support для high-volume, SaaS или mission-critical usage?

## Запрошенные приложения

- Product boundary note for Geosuggest, Geocoder, Search and routing APIs.
- Method and field matrix.
- OpenAPI/Swagger или complete specifications.
- Sample requests and responses.
- Error-code reference and retry guidance.
- API-specific tariff appendix with Standard/Extended rights.
- SLA/support appendix.
- Storage, caching, display, attribution, redistribution, affiliate-use and SaaS terms.
- Changelog, deprecation and breaking-change policy.

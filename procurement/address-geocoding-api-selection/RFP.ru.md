# RFP для API адресов и геокодирования

[English version](RFP.md)

Используйте эти вопросы для оценки поставщика. Не отправляйте credentials, клиентские данные или персональные данные в первом запросе.

## Scope продукта

- Какие продукты, модули и API methods входят в предложение?
- Какие capability покрыты: suggestions, cleaning, validation, direct geocoding, reverse geocoding, place search, routing, registry data, batch processing?
- Какие capability требуют отдельных продуктов: Geosuggest, Places, Suggest, Organization Search или routing APIs?
- Если предложение включает OpenStreetMap/Nominatim, это public-instance, self-hosted или commercial-provider route?
- Если предложение включает FIAS/GAR, это file download, SMEV channel, documented API service или user-facing portal workflow?
- Какие geographies и languages поддерживаются?
- Какая granularность адреса поддерживается: регион, город, улица, дом, строение, корпус, подъезд, квартира, помещение?
- Какие официальные источники адресов используются и какова update cadence?
- Как устроена coordinate precision model и как возвращается match level?
- Какие поля доступны на уровне дома и какие требуют extra paid access?
- Какие organization/place fields входят в базовый пакет, а какие доступны on demand?

## Технический доступ

- Какой protocol, base URL и authentication model используются?
- Доступны ли OpenAPI/Swagger, SDKs, examples и error references?
- Какие request/response formats поддерживаются?
- Как versioned schemas?
- Какая error model и retry guidance?
- Есть ли sandbox с API credentials?
- Доступны ли test credentials до подписания договора?
- Поддерживаются ли batch operations?
- Поддерживается ли asynchronous delivery?
- Есть ли webhooks или callback URLs?
- Есть ли environment separation, IP restrictions, referer restrictions или key-level limits?
- Какой changelog и breaking-change policy?

## Цены и коммерческие условия

- Что является billing unit: request, successful request, address, record, field, method, package, monthly active user или другое?
- Предоставьте method-level pricing.
- Предоставьте batch billing rules.
- Что входит в minimum commitment?
- Какие overage prices и overage payment rules?
- Trial/free-tier calls функционально идентичны production calls?
- Higher-precision coordinates, registry fields или organization data оплачиваются отдельно?
- Есть ли annual discounts или minimum terms?
- Переносятся ли unused units?
- Какие support level и SLA включены?
- Как устроена incident communication?

## Лимиты и надёжность

- Какие production daily, monthly и per-second limits?
- Лимиты считаются per key, per account, per IP, per method или per product?
- Можно ли поднять лимиты автоматически или только через support request?
- Какие typical и percentile latencies?
- Какой uptime SLA?
- Публичны ли regional outages/status history?
- Что происходит при quota exhaustion?
- Какой allowed retry/backoff behavior?

## Права данных и legal use

- Можно ли хранить результаты long term?
- Можно ли кэшировать результаты и как долго?
- Можно ли показывать результаты end customers?
- Можно ли отображать результаты на third-party maps?
- Требуется ли attribution?
- Можно ли redistribute, resell или export результаты?
- Разрешён ли SaaS embedding?
- Могут ли affiliates использовать те же API/data results?
- Можно ли использовать данные для scoring, model training, deduplication или internal analytics?
- Какие personal data obligations применимы?
- Доступен ли DPA?
- Какие deletion и audit requirements?
- Есть ли ограничения на combining results с другими address registries или map providers?
- Если используются OSM data, какие attribution, ODbL, share-alike, cache и derived-database obligations применяются?
- Если используются public hosted services, можно ли отправлять personal или confidential addresses в запросах?

## Pilot и evaluation

- Можно ли провести pilot на synthetic/public address sample?
- Может ли поставщик review benchmark sample до теста?
- Какие metrics поставщик рекомендует для match level, false positives, missing results и coordinate precision?
- Может ли поставщик дать reference implementation или examples для batch testing?
- Какая поддержка доступна во время pilot?

## Границы, которые нужно подтвердить

- Входит ли sanctions/compliance в standard API? Если нет, какой отдельный продукт нужен?
- Входит ли organization/place search в standard API? Если нет, какой отдельный продукт нужен?
- Входит ли routing или distance matrix в geocoder? Если нет, какой отдельный продукт нужен?
- Для official registry integration: где граница между file downloads, API services и government exchange channels?
- Для Nominatim: где граница между public `nominatim.openstreetmap.org`, self-hosting и commercial provider service?

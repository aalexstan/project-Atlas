# Checklist запроса к LocationIQ Geocoding API

[English version](provider-request.md)

> Вопросы LocationIQ перед production selection. Это checklist, а не ответы поставщика.

## Граница продукта

- Подтвердите, какие APIs входят в proposed plan: Search / Forward Geocoding, Reverse Geocoding, Autocomplete, Nearby POI, maps и routing.
- Подтвердите, подходит ли Nearby POI для target place-search use case или нужен другой продукт/поставщик.
- Подтвердите, можно ли использовать Maps Lite plan для intended geocoding workload.

## Технический интерфейс

- Предоставьте endpoint list, regions, protocol, authentication model и key restrictions.
- Предоставьте OpenAPI/Swagger, Postman collection или equivalent machine-readable specification.
- Опишите response schemas, versioning, error model и deprecation policy.
- Подтвердите supported response formats для Search, Reverse и Autocomplete.
- Подтвердите language и country-filter behavior.

## Quality and Coverage

- Опишите data sources по странам и attribution requirements.
- Предоставьте expected match levels и coordinate precision indicators.
- Объясните, как интерпретировать `matchquality`, normalized address fields и confidence-like fields.
- Подтвердите coverage для target countries and regions.
- Подтвердите, есть ли house-level data в target regions.

## Лимиты и operations

- Подтвердите production RPS, daily/monthly quotas, burst behavior и HTTP 429 handling.
- Подтвердите, являются ли rate limits hard или soft на proposed plan.
- Подтвердите monitoring, usage export и alerting options.
- Подтвердите support hours, incident communication, SLA и uptime commitments.

## Batch and Offline Use

- Подтвердите, существует ли asynchronous batch endpoint.
- Подтвердите large-batch processing options, pricing, turnaround time и evidence artifacts.
- Подтвердите, allowed ли concurrent API calls для planned batch volume.
- Подтвердите retry, duplicate request и partial-failure billing.

## Pricing

- Предоставьте method-level pricing или request-credit model.
- Подтвердите minimum commitment, overage, taxes, currency и invoice terms.
- Подтвердите, делят ли autocomplete, search, reverse, nearby и maps одни credits.
- Подтвердите discounts или custom enterprise terms отдельно от public pricing.

## Data Rights and Legal

- Подтвердите storage rights for API output.
- Подтвердите caching rights for request-response pairs by plan.
- Подтвердите attribution requirements для Free и paid plans.
- Подтвердите rights for customer-facing display, SaaS embedding, internal enrichment, redistribution, resale и API proxying.
- Подтвердите ODbL/OpenStreetMap obligations, derived-database treatment и source attribution requirements.
- Подтвердите, можно ли использовать results для scoring, model training или quality-improvement datasets.
- Предоставьте DPA/privacy terms для submitted addresses and coordinates.

## Pilot

- Предоставьте test credentials и allowed benchmark scope.
- Подтвердите synthetic/public test-sample rules.
- Подтвердите, засчитываются ли benchmark requests в commercial limits.
- Подтвердите, как сообщать provider corrections или disputed results.

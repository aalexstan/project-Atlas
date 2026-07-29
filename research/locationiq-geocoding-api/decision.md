# LocationIQ Geocoding API Profile Decision

[Русская версия](decision.ru.md)

## Decision

Create an active API-first profile for **LocationIQ Geocoding API**.

## Rationale

Official LocationIQ sources provide enough evidence for Atlas reviewed maturity:

- product identity and official docs;
- Search / Forward Geocoding, Reverse Geocoding and Autocomplete boundaries;
- access-token authentication;
- public API Reference;
- public pricing, free-plan quota and paid-plan request/rate examples;
- provider-published storage/caching guidance;
- explicit batch boundary for one address per request.

## Boundaries

- Treat LocationIQ as a hosted commercial geocoding/autocomplete API suite.
- Do not treat it as an official address registry, Russian address cleaning API or unrestricted public Nominatim replacement.
- Treat Nearby POI as related context until a separate places/POI evaluation is performed.
- Do not treat public pricing as enterprise quote or SLA evidence.
- Do not treat storage-friendly wording as approval for redistribution, resale, SaaS embedding, API proxying or model training.

## Blockers Before Gold

- Credentialed benchmark against target address and coordinate samples.
- Legal review of ODbL, attribution, caching, derived databases, redistribution and SaaS use.
- Contract confirmation of SLA/support, plan scope and enterprise terms.
- Privacy/DPA review for submitted addresses and coordinates.
- Batch/large-volume workflow review and provider confirmation.

## Live Testing Status

No live API test, autocomplete test, batch job or benchmark was performed.

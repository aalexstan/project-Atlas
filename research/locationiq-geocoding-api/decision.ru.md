# Решение по профилю LocationIQ Geocoding API

[English version](decision.md)

## Решение

Создать активную API-first карточку **LocationIQ Geocoding API**.

## Обоснование

Официальные источники LocationIQ дают достаточно evidence для Atlas reviewed maturity:

- product identity и official docs;
- границы Search / Forward Geocoding, Reverse Geocoding и Autocomplete;
- access-token authentication;
- public API Reference;
- public pricing, free-plan quota и paid-plan request/rate examples;
- provider-published storage/caching guidance;
- explicit batch boundary: один address per request.

## Границы

- Считать LocationIQ hosted commercial geocoding/autocomplete API suite.
- Не считать его official address registry, Russian address cleaning API или unrestricted public Nominatim replacement.
- Считать Nearby POI related context, пока не проведена отдельная places/POI evaluation.
- Не считать public pricing enterprise quote или SLA evidence.
- Не считать storage-friendly wording разрешением на redistribution, resale, SaaS embedding, API proxying или model training.

## Blockers до Gold

- Credentialed benchmark на target address and coordinate samples.
- Legal review ODbL, attribution, caching, derived databases, redistribution и SaaS use.
- Contract confirmation SLA/support, plan scope и enterprise terms.
- Privacy/DPA review для submitted addresses and coordinates.
- Batch/large-volume workflow review и provider confirmation.

## Live Testing Status

Live API test, autocomplete test, batch job или benchmark не проводились.

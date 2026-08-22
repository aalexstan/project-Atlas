# OpenCage Geocoding API Profile Decision

[Русская версия](decision.ru.md)

## Decision

Create an active API-first profile for **OpenCage Geocoding API**.

## Rationale

Official OpenCage sources provide enough evidence for Atlas reviewed maturity:

- product identity and official docs;
- forward and reverse geocoding boundary;
- API-key authentication;
- request pattern and response formats;
- public pricing and free-trial limits;
- storage/caching wording;
- open-data source and data-license context;
- explicit separation from Geosearch/autosuggest;
- explicit batch boundary.

## Boundaries

- Treat OpenCage as a hosted open-data geocoding API, not an address-cleaning API.
- Treat Geosearch/autosuggest as a separate product for future research.
- Do not present public pricing as a quote for enterprise use.
- Do not treat storage-friendly wording as legal approval for redistribution, resale, white-label SaaS, API proxying or model training.

## Blockers Before Gold

- Credentialed benchmark against target samples.
- Legal review of ODbL, attribution, derived databases, redistribution and SaaS use.
- Contract confirmation of SLA/support and enterprise terms.
- Privacy/DPA review for submitted addresses and coordinates.
- Batch operations review for high-volume workflows.

## Live Testing Status

No live API test, spreadsheet upload or benchmark was performed.

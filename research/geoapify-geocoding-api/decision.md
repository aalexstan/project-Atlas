# Geoapify Geocoding API Decision

[Русская версия](decision.ru.md)

## Decision

Create an active API-first profile:

- `apis/geoapify-geocoding-api/`

## Rationale

Official Geoapify sources provide enough evidence for a maintained Atlas profile:

- official product page;
- developer documentation;
- forward and reverse endpoints;
- API-key authentication;
- response formats;
- batch API;
- public pricing and rate limits;
- public SLA statement for paid plans;
- attribution and storage-related terms.

## Product Boundary

Treat Geoapify as a hosted commercial open-data geocoding API.

Do not treat it as:

- public `nominatim.openstreetmap.org`;
- self-hosted Nominatim;
- official Russian address registry validation;
- Russia-specific address cleaning;
- routing or matrix API;
- full Places API profile.

## Main Blockers

- No Atlas live test or benchmark was performed.
- ODbL, attribution, derived-database, caching, SaaS and redistribution implications need legal review.
- Paid/enterprise contract terms may differ from public terms.
- DPA/privacy and data residency requirements need scenario-specific review.
- Batch failure/retry/billing details need pilot confirmation.

## Comparison Handling

Add Geoapify to the address/geocoding comparison as a managed international/open-data geocoding route. Compare it against self-hosted Nominatim when operational ownership matters, and against Yandex/2GIS/DaData when Russia-specific map ecosystem or address-cleaning needs dominate.

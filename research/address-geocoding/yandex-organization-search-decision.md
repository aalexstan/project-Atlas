# Yandex Maps Organization Search API Decision

[Русская версия](yandex-organization-search-decision.ru.md)

## Decision

Create an active API-first profile:

- `apis/yandex-maps-organization-search-api/`

## Rationale

Official Yandex Maps API sources provide enough evidence for a maintained Atlas profile:

- official product identity;
- official product purpose;
- public documentation;
- endpoint;
- API-key authentication;
- request and response references;
- public commercial terms and request packages;
- public technical rate-limit statement.

## Product Boundary

Treat the API as an organization/place/geographic-object search product.

Do not treat it as:

- address autocomplete;
- address cleaning or normalization;
- registry-quality address validation;
- direct/reverse geocoder replacement for the Yandex Geocoder profile;
- routing, matrix or ETA product.

## Main Blockers

- Public SLA was not found.
- OpenAPI/Swagger was not found.
- Storage/data-use rights require contract review, especially because reviewed official public pages appear to differ in Basic/Advanced or storage-capable license wording.
- Batch/offline enrichment rights are not confirmed.
- No Atlas live testing or quality benchmark was performed.

## Comparison Handling

Add Yandex Organization Search as a Yandex ecosystem alternative to 2GIS Places API for organization/place search. Do not declare a winner without a common benchmark, contract-rights review and comparable pricing assumptions.

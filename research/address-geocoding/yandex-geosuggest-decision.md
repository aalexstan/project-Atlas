# Yandex Geosuggest Decision Memo

[Русская версия](yandex-geosuggest-decision.ru.md)

## Decision

Create a separate active API profile: `apis/yandex-maps-geosuggest-api/`.

## Rationale

Official Yandex sources identify Geosuggest as a separate server-side API product with its own endpoint, request/response documentation and tariffs. It solves autocomplete for geographic objects and organizations, while Yandex Maps Geocoder API solves direct and reverse geocoding.

## Boundaries

- Include: typed suggestions for addresses, geographic objects and organizations.
- Link to: Yandex Maps Geocoder API when `uri` is used for follow-up geocoding.
- Exclude: routing, route matrices, full organization search and address normalization.

## Procurement Caveat

The profile is reviewed, not live-tested. Storage, caching, customer-facing display, SaaS embedding and redistribution must be confirmed in the exact Yandex license.

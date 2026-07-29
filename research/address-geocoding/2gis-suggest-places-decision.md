# 2GIS Suggest and Places Decision Memo

[Русская версия](2gis-suggest-places-decision.ru.md)

## Decision

Create two separate active profiles:

- `apis/2gis-suggest-api/`
- `apis/2gis-places-api/`

## Rationale

Official 2GIS documentation separates Suggest API, Places API and Geocoder API. Suggest handles user-input suggestions; Places searches organizations, buildings and places; Geocoder handles address/coordinate conversion.

## Boundaries

- `2gis-suggest-api`: autocomplete and suggestion UX, including address, street, object and route-endpoint suggestions.
- `2gis-places-api`: organization, building and place search, with possible on-demand fields/methods.
- `2gis-geocoder-api`: direct and reverse geocoding.

## Procurement Caveat

The profiles are reviewed, not live-tested. Contract review is required for caching, storage, SaaS use, redistribution, attribution and any on-demand fields.

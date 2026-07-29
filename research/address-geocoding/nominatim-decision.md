# Nominatim Decision Memo

[Русская версия](nominatim-decision.ru.md)

## Decision

Create a profile for `apis/nominatim-geocoder-software/`.

## Rationale

Nominatim has official documentation, a public OSMF usage policy and self-hosting documentation. The product boundary is software/data infrastructure rather than a conventional hosted paid API.

## Boundaries

- Public OSMF service: limited end-user-triggered use under the Nominatim policy.
- Self-hosted Nominatim: viable route when the team can operate OSM imports, updates, infrastructure and compliance.
- Commercial providers: separate procurement route, not evaluated in this profile.

## Procurement Caveat

Do not use public Nominatim for autocomplete, bulk geocoding, API resale or primary production geocoding. For production, evaluate self-hosting or a commercial provider with explicit SLA and legal terms.

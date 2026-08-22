# Procurement and tender API recheck — 2026-08-22

## Scope

Recheck whether official evidence now supports active reviewed profiles for the Russian EIS procurement information route and Seldon.Tenders API.

## Official sources reviewed

- [Russian Treasury: EIS](https://roskazna.gov.ru/gis/eis-zakupki-gov-ru)
- [Russian Treasury: formats of information interaction](https://roskazna.gov.ru/gis/ehlektronnyj-byudzhet/formaty-informacionnogo-vzaimodejstviya)
- [EIS technical information hub](https://zakupki.gov.ru/epz/main/public/document/view.html?sectionId=1252)
- [Seldon 1.7 API](https://seldongroup.ru/system/1.7/api)
- [Seldon API integration overview](https://seldongroup.ru/system/api)

## Confirmed facts

- The Treasury describes EIS / `zakupki.gov.ru` as the official site for free access to procurement information and for forming, processing and storing that information.
- The official Treasury navigation exposes formats of interaction and technical-information routes for external systems.
- Seldon describes `API.Seldon.Tenders` as a web service for programmatic access to procurement data and integration into a CRM.
- Seldon’s official product page lists notices, protocols, contracts and documents as transferable data and describes retrieval by notice number or configured filters.
- Seldon describes an order-based delivery model in which a customer requests filtered calculations and receives a result later; this is not enough to infer REST, GraphQL, webhook or streaming semantics.

## Unknowns and blockers

- EIS endpoint catalog, current machine-to-machine authentication, schemas, versioning, quotas, rate limits, support and data-use terms remain unresolved.
- Seldon endpoint catalog, authentication, response schemas, versioning, production limits, SLA, API-specific price and storage/redistribution terms remain unresolved.
- No credentials, API calls, FTP listing, document ingestion or live benchmark was performed.

## Decision

Create reviewed profiles for both routes with explicit product classes: official government procurement data integration and commercial aggregated procurement API. Create a scenario comparison, but do not declare a winner or treat either profile as fully verified.


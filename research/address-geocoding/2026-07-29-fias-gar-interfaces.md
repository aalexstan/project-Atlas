# FIAS/GAR Integration Interfaces Research Log

Date: 2026-07-29

## Scope

This log refines the official integration boundary for FIAS/GAR and distinguishes supported integration channels from user-facing website behavior.

## Official Sources Reviewed

- https://www.nalog.gov.ru/rn77/service/fias/
- https://fias-file.nalog.ru/
- https://fias-file.nalog.ru/FiasInfo
- https://fias-file.nalog.ru/Frontend
- https://fias-file.nalog.ru/Search
- https://www.nalog.gov.ru/rn77/news/activities_fts/13611328/
- https://www.nalog.gov.ru/rn77/news/activities_fts/13824755/
- https://www.nalog.gov.ru/rn77/news/activities_fts/13874101/

## Confirmed Facts

- FNS describes FIAS as the federal information system that forms, maintains and uses GAR, the state address registry.
- FNS describes GAR as an open federal resource containing reliable, uniform and publicly available address information.
- The FIAS portal has a developer section with entries for open data/file downloads, SMEV and API services.
- An FNS archived publication from 2023 states that API and SMEV services were published on the FIAS portal for users to obtain GAR information.
- Another FNS archived publication describes integration channels as weekly portal downloads published twice per week, SMEV daily publication and online API batch provision by request.
- The public FIAS portal also exposes address search and advanced search screens for user-facing lookup.

## Provider-Reported Claims

- FNS materials describe GAR as the only legitimate source of address information in Russia.
- FNS materials state that actual address information is available on the FIAS portal on the day it is placed in GAR.

## Observations

- The officially described integration model is not only a file feed: official FNS pages mention file downloads, SMEV and API services.
- However, the reviewed public pages did not provide a stable public API method catalog, base URL, authentication model, schema reference, versioning or SLA.
- Website Search/Frontend endpoints should not be documented as supported public APIs merely because they are visible on the public portal.
- FIAS/GAR remains an official registry integration route, not a ready replacement for commercial low-latency autocomplete or geocoding APIs.

## Unknowns

- Current public API method catalog.
- API base URLs, authentication, quotas, response schemas and error model.
- File package formats and delta/full update package structure.
- Access requirements and eligibility for API services and SMEV.
- Costs, if any, for API service access and automated downloads.
- SLA, support channels and breaking-change policy.
- Commercial use, SaaS display, redistribution and derived database terms.

## Contradictions

- FNS pages confirm API services exist, but the accessible static pages do not expose enough specification detail to treat them as a fully verified public API profile.

## Commercial Blockers

- TCO requires ETL, storage, indexing, search/matching logic, updates and support.
- Procurement cannot compare GAR access price to commercial API pricing until access channel, legal rights and operating cost are known.

## Legal and Data-Rights Blockers

- GAR is public and official, but concrete SaaS, redistribution, customer display and derived database obligations still require legal review.

## Live Testing Status

No Atlas download, SMEV, API-service or portal-endpoint live test was performed.

## Decision

Keep the active profile as `fias-gar-data-integration`, not a generic REST API profile. Update it to recognize official file download, SMEV and API-service channels while keeping unsupported website endpoints out of the public API surface.

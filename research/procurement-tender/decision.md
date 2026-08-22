# Procurement and Tender API Direction Decision

[Русская версия](decision.ru.md)

## Decision

The 2026-08-22 official-source recheck supports **reviewed, not fully verified** profiles for two distinct routes:

- official EIS procurement data integration;
- commercial aggregated Seldon.Tenders API.

Do not treat either route as a universal winner or as a credential-tested production API.

## Rationale

Official Russian Treasury pages confirm the public role and identity of EIS / `zakupki.gov.ru` and expose interaction-format routes. The official Seldon page now explicitly describes `API.Seldon.Tenders` as a programmatic procurement-data integration service and lists notices, protocols, contracts and documents. Atlas still has not captured complete current schemas, endpoint catalogs, access rules, limits, SLA or API-specific commercial terms.

This is enough to preserve and organize the direction, but not enough for a current Atlas API profile or scenario comparison.

## Boundaries

- EIS / `zakupki.gov.ru` is an official procurement information source and is profiled as a data-integration route, not assumed to be a turnkey REST API.
- EIS technical-information navigation confirms an integration route, but does not by itself prove a complete public API specification.
- Agency CSV open-data datasets are supporting evidence, not a national procurement API.
- Legacy Seldon research remains provenance; the new profile relies on current official `seldongroup.ru` evidence and keeps old `api-seldon.ru` as a source-risk note.
- Web portals, file feeds, government services and commercial API products must be compared as different product classes.

## Reopen Conditions

Create active profiles or comparison only after official evidence confirms:

- endpoint catalog or distribution channel;
- authentication or access process;
- schemas, formats and versioning;
- update cadence, rate limits or quotas;
- data scope and field matrix;
- document access model;
- SLA/support or availability statement;
- storage, caching, display, redistribution and SaaS rights;
- pricing or cost model for commercial routes.

## Next Research Step

Capture the actual official EIS technical-information documents, schemas and supported distribution-channel details, then compare them with Seldon.Tenders/Seldon.Win only if Seldon provides API-level evidence. Keep `datasets/procurement_tender_contracts.md` as legacy supporting research until then.

# Procurement and Tender API Direction Decision

[Русская версия](decision.ru.md)

## Decision

Keep the procurement/tender direction as **research baseline / comparison backlog** for now.

Do not create an active API profile or comparison from the current evidence.

## Rationale

Official Russian Treasury pages confirm the public role and identity of EIS / `zakupki.gov.ru`. Official agency open-data pages confirm that procurement-related CSV datasets exist. The EIS public site also exposes a technical-information section and an information-interaction subsection, but Atlas has not captured the actual current document files, schemas, endpoint catalog or access rules. Existing Atlas research also preserves Seldon.Tenders as legacy-only because official API specification, auth, pricing, limits, SLA and data-rights evidence are missing.

This is enough to preserve and organize the direction, but not enough for a current Atlas API profile or scenario comparison.

## Boundaries

- EIS / `zakupki.gov.ru` is an official procurement information source, not yet documented here as an active Atlas API profile.
- EIS technical-information navigation is confirmed as a route to investigate, not as sufficient API specification evidence by itself.
- Agency CSV open-data datasets are supporting evidence, not a national procurement API.
- Seldon.Tenders remains legacy/provenance until stronger official evidence is available.
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

# Procurement and Tender Data Official Source Baseline

## Scope

This research note checks whether Atlas can create an active procurement/tender API comparison or API profile from currently reviewed official sources.

It covers:

- official EIS / `zakupki.gov.ru` identity;
- government open-data procurement examples;
- Seldon.Tenders legacy status;
- blockers for an API-first comparison.

It does not perform live API testing, credentialed access, form submission or legal review.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Russian Treasury page for EIS | https://roskazna.gov.ru/gis/eis-zakupki-gov-ru | Official identity and public purpose of EIS / `zakupki.gov.ru` |
| Russian Treasury regional GIS page | https://mo.roskazna.gov.ru/gis/ | Cross-check of EIS public-purpose wording |
| FNS open-data page: large purchases | https://www.nalog.gov.ru/opendata/7707329152-purchase/ | Example of an official agency procurement open-data dataset |
| Russian open-data portal dataset | https://data.gov.ru/datasets/94858d8b-c2e1-4ce2-8edb-e4e0bcaa628c | Example of a government procurement dataset entry |
| EIS public technical information section | https://zakupki.gov.ru/epz/main/public/document/view.html?sectionId=1252 | Official technical-information hub and interaction-document subsection discovery |
| Seldon.Tenders decision memo | ../seldon-tenders/decision.md | Existing Atlas decision on legacy-only status |
| Legacy procurement dataset note | ../../datasets/procurement_tender_contracts.md | Historical dataset-centric provenance |

## Confirmed Facts

| Fact | Status | Evidence |
|---|---|---|
| EIS / `zakupki.gov.ru` is the official Russian procurement information system referenced by Russian Treasury pages. | verified | Treasury pages |
| Russian Treasury describes EIS as intended to provide free access to information about contract-system procurements and procurements by certain legal entities. | verified | Treasury pages |
| FNS publishes an official open-data CSV dataset for large purchases over 1 billion rubles. | verified | FNS open-data page |
| The Russian open-data portal contains procurement-related dataset entries, but they are agency datasets, not automatically EIS API documentation. | observed | data.gov.ru dataset page |
| Existing Atlas research keeps Seldon.Tenders legacy-only until official API specification/auth/pricing/rights evidence is available. | verified_internal | Seldon.Tenders decision memo |
| The official EIS public site exposes a `Техническая информация` section with a subsection named `Требования к информационному взаимодействию ЕИС с другими информационными системами`. | observed | EIS public technical information page; detailed document files were not captured in this pass |

## Observations

- Official public procurement data exists, but the reviewed sources do not yet provide a complete active API profile.
- The official EIS site has a technical-information hub and an explicit information-interaction subsection, but static retrieval did not capture the actual schemas, service catalog or document files in this pass.
- EIS, agency open-data CSV datasets and commercial aggregators solve different scenarios.
- A procurement/tender comparison should not mix official bulk/open-data feeds, web search portals and commercial APIs without a common field matrix and rights model.
- The old `api-seldon.ru` path remains provenance only and must not be used as a current source.

## Unknowns and Blockers

- Current official EIS service endpoint catalog.
- Actual current document files behind the EIS technical-information subsection.
- Authentication, if any, for machine-to-machine EIS services.
- Request and response schemas.
- XML/JSON formats and versioning.
- Official migration status from FTP-style distribution to newer services.
- Rate limits, quotas and service availability guarantees.
- Terms for bulk download, storage, caching, redistribution, SaaS embedding and resale.
- Whether documents, protocols, contracts and participant records have separate access channels and rights.
- Comparable Seldon.Tenders/Seldon.Win API evidence from official Seldon sources or provider response.

## Candidate Handling

| Candidate | Current Atlas handling | Reason |
|---|---|---|
| EIS / `zakupki.gov.ru` official source | Research baseline only | Official identity is confirmed, but current service/API documentation was not captured. |
| Agency open-data procurement datasets | Supporting research | Useful for examples and provenance, but not a national procurement API profile. |
| Seldon.Tenders / API.Seldon.Tenders | Legacy-only | Existing decision memo says official evidence is insufficient for an active profile. |

## Decision

Do not create an active procurement/tender API profile or comparison in this pass.

Create the comparison only after at least two candidate routes have enough official evidence for:

- product/source boundary;
- endpoint or distribution model;
- authentication/access process;
- data scope and field matrix;
- formats and versioning;
- rate limits or update cadence;
- storage, caching, display and redistribution rights;
- SLA/support or public availability statement;
- pricing or cost model where commercial.

## Live Testing Status

No live testing, credentialed access, benchmark or document download pipeline was performed.

# EIS / zakupki.gov.ru Technical Information Recheck — 2026-07-29

## Scope

This note refines the procurement/tender backlog by checking the official EIS / `zakupki.gov.ru` public technical-information route.

It does not create an active API profile, download production procurement datasets, parse XML archives, use credentials, submit forms, or perform live API testing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| EIS public home page | https://zakupki.gov.ru/epz/main/public/home.html | Official navigation discovery |
| EIS technical information section | https://zakupki.gov.ru/epz/main/public/document/view.html?sectionId=1252 | Technical documentation hub |
| EIS public document search endpoint | https://zakupki.gov.ru/epz/main/public/document/search.html | Static search attempts for technical documents |
| EIS public document download endpoint examples | https://zakupki.gov.ru/epz/main/public/download/downloadDocument.html | Static download attempts for IDs surfaced on the public page |
| EIS FTP hostname | ftp://ftp.zakupki.gov.ru/ | DNS/listing availability check only |

## Observations

| Observation | Status | Evidence |
|---|---|---|
| The public EIS home page links to a `Техническая информация` document section. | observed | Public home page HTML contained `sectionId=1252` with text `Техническая информация`. |
| The `Техническая информация` page rendered a public HTML page in this environment when retrieved with TLS verification bypass because local `curl` could not validate the certificate chain. | observed_with_tls_bypass | Temporary retrieval of official page HTML. |
| The technical section lists `Журнал версий ЕИС`. | observed_with_tls_bypass | `sectionId=364` entry in the technical section HTML. |
| The technical section lists `Требования к информационному взаимодействию ЕИС с другими информационными системами`. | observed_with_tls_bypass | `sectionId=362` entry in the technical section HTML. |
| The technical section lists `Требования к информационному взаимодействию ГИС НР с другими информационными системами`. | observed_with_tls_bypass | `sectionId=1367` entry in the technical section HTML. |
| The technical section lists `Прочие материалы`. | observed_with_tls_bypass | `sectionId=1126` entry in the technical section HTML. |
| Direct static retrieval of the subsection URLs returned short 404 pages in this environment. | observed | Attempts for `sectionId=362`, `364`, `1367` and `1126`. |
| Static `document/search.html` requests for technical terms returned short 404 pages in this environment. | observed | Attempts for empty section search, `ТФФ`, `схемы` and `интеграц`. |
| `ftp.zakupki.gov.ru` did not resolve in this environment. | observed | DNS failure from `curl`; this is an environment observation, not proof that the official FTP route is unavailable generally. |
| Public `downloadDocument.html` IDs surfaced on the EIS home page returned short 404 pages in this environment. | observed | Attempts for document IDs `33257` and `35694`. |

## Confirmed Boundaries

- The official public EIS site has a technical-information hub and an explicit subsection for information interaction with other information systems.
- This recheck did not capture the actual interaction requirements document files, schemas, endpoint catalog, API-service methods, authentication model or data-rights terms.
- Secondary sources that mention FTP, XSD schemas or older service URLs remain discovery context only until the corresponding official EIS documents are captured.

## Unknowns and Blockers

- Current official document files behind `Требования к информационному взаимодействию ЕИС с другими информационными системами`.
- Current endpoint or distribution-channel catalog.
- FTP route status, directory layout, access expectations and supported use.
- Current XML/XSD package names, schema versions and document types.
- Authentication and access process for any machine-to-machine services.
- Rate limits, quotas, service availability and support process.
- Storage, caching, redistribution, SaaS and resale rights for procurement data and documents.
- Whether different procurement objects use different official channels or rights: notices, protocols, contracts, guarantees, participant records and documents.

## Live Testing Status

No API call, FTP listing, credentialed access, document-ingest pipeline, benchmark or form submission was performed. Static public-page retrieval was used only for research discovery.

## Decision

Do not create an active EIS API profile or procurement/tender comparison yet. The next useful step is to capture the actual official document files from the EIS technical-information subsection or obtain an official support/provider response that identifies the current supported distribution channels, schemas, endpoints and data-use rights.

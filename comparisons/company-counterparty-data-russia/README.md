# Company and Counterparty Data APIs in Russia

[Русская версия](README.ru.md)

> Independent comparison of DaData, Kontur.Focus API, Seldon.Basis API, GLOBAS.API, and the official Russian Federal Tax Service EGRUL/EGRIP integration service.

## Research Status

| Field | Value |
|---|---|
| Maturity | **Reviewed** — public-source comparison |
| Last verified | 2026-07-23; GLOBAS.API official-source addendum 2026-07-28; FTS official-source conflict recheck 2026-08-15 |
| Region | Russia; CIS coverage is considered separately for Seldon |
| Live testing | Not performed; commercial Kontur and Seldon credentials were unavailable |
| Pricing | Included only when public pricing clearly applies to the API product |
| Next review | FTS credentialed FTP behavior or official clarification when lawful access is available; 2026-10-21 for the full comparison |

## Decision Summary

There is no universal winner because the products belong to different solution classes.

| User need | Recommendation | Why |
|---|---|---|
| Company details autocomplete, B2B forms, CRM, fast launch | **DaData** | Accessible documentation, public pricing, a free tier, INN/OGRN lookup, and up to 30 requests per second per IP |
| Automated enterprise due diligence and risk monitoring | **Kontur.Focus API** | Broad source coverage, bulk checks, monitoring, risk markers, and established enterprise integrations |
| Deep analytics, relationships, procurement data, and CIS companies | **Seldon.Basis API** | Broad registry and activity coverage, configurable methods, and Russia/CIS data |
| Additional enterprise integration candidate for CRM/ERP/EDI, mass checks, enrichment, and portfolio monitoring | **GLOBAS.API** | Official Credinform page positions it for corporate-system integration, but specification, auth, schemas, limits, SLA and API price require provider confirmation |
| Building an internal EGRUL/EGRIP database and controlling ETL | **FTS integration** | Primary government source, full XML dumps, and daily deltas |
| A free legally signed extract for one company | **FTS electronic extract service** | Free electronic extract signed by the FTS; it is not a bulk API |
| AML / 115-FZ and sanctions screening | **Kontur.Compliance API**, evaluated separately | This is a separate product and capability set |

## Scope

The user need is to retrieve structured information about a Russian legal entity or individual entrepreneur, populate a counterparty record, and optionally automate risk assessment.

The comparison separates three distinct jobs:

1. company details and autocomplete;
2. commercial due diligence;
3. primary registry ingestion for an internal data platform.

Therefore, the FTS bulk integration is not a direct replacement for Kontur.Focus or Seldon.Basis, while DaData should not automatically be treated as a complete enterprise due-diligence platform.

## Compact Matrix

| Criterion | DaData | Kontur.Focus API | Seldon.Basis API | GLOBAS.API | FTS EGRUL/EGRIP |
|---|---|---|---|---|---|
| Product class | Data enrichment / company details | Enterprise due diligence | Due diligence / analytics | Enterprise data integration | Primary registry / bulk data |
| INN/OGRN lookup | Yes | Yes | Yes | Candidate; field matrix required | Web search; integration uses files |
| Company record autocomplete | Core strength | Yes | Yes | Candidate; method details required | Requires custom processing |
| Founders and managers | Maximum plan | Yes | Yes | Unknown until field matrix | Within publicly available registry data |
| Financial indicators | Maximum plan; partial coverage | Yes | Yes | Unknown until field matrix | Not a complete financial analytics aggregator |
| Courts, enforcement, bankruptcy | Not established as a complete profile for the company lookup method | Yes | Yes | Unknown until field matrix | No; requires other sources |
| Public procurement data | Not a core use case | Yes | Yes | Unknown until field matrix | No |
| Relationships / affiliations | Separate method, maximum plan | Yes | Yes | Unknown until field matrix | Requires a custom relationship model |
| Monitoring | Not the primary public profile workflow | Yes | Yes | Provider-reported portfolio monitoring scenario | Daily deltas; processing is customer-managed |
| Russia | Yes | Yes | Yes | Candidate; coverage must be confirmed | Yes |
| CIS | Separate Belarus and Kazakhstan methods | Not established in this research | Major strength | Unknown from reviewed API page | No |
| Public documentation | Detailed and directly accessible | Developer portal exists; parts require JavaScript | Public functional material; detailed onboarding follows a request | Product page only; no public specification found | Detailed file model and formats |
| Public API pricing | Yes | Price list exists, final cost depends on configuration | No exact public API price | No public API price found | Yes, per registry access |
| Free start | 10,000 requests/day | Demo by request | Trial by request | Three-day GLOBAS system test; API trial not confirmed | Free individual electronic extracts |
| Published limits | Daily plan plus 30 requests/s per IP | Must be confirmed for the purchased plan | Up to 10,000 requests/day per method for the individual plan | Not found in reviewed official pages | Not request/response; full files and daily deltas |

“Not established” means no reliable statement was found in the reviewed official public material. It does not prove that the capability is absent.

## 1. DaData

### Best Fit

- B2B signup and company autocomplete;
- CRM/ERP record creation;
- fast self-service integration;
- projects that require transparent public pricing;
- prototypes and lower-volume production workloads.

### Verified Strengths

The “Company by INN or OGRN” method finds a company or individual entrepreneur by INN, INN/KPP, or OGRN. The published maximum rate is 30 requests per second from one IP, and the free plan permits up to 10,000 requests per day.

Public annual plans at the verification date:

| Plan | Requests/day | Annual price | Company data |
|---|---:|---:|---|
| Free | 10,000 | RUB 0 | Light-plan dataset with a lower quota |
| Light | 50,000 | RUB 14,000 | Core identifiers, status, legal address, primary OKVED |
| Extended | 100,000 | RUB 28,000 | All OKVED codes, employee count, tax regime |
| Maximum | 200,000+ | RUB 56,000+ | Founders, managers, finance, tax debt, licenses, contacts, affiliations |

### Limitations

- Response completeness depends on the plan, so the same endpoint may expose different data fields.
- DaData states that financial indicators are partially populated for about 60% of active companies.
- It is primarily a data-enrichment and normalization product, not a complete enterprise risk-management platform.
- Deep court, enforcement, and monitoring requirements should be validated separately or handled by a specialist platform.

### Verdict

**The strongest option for a fast, low-cost company-details integration.** It is an excellent starting point, but it should not be assumed to replace Kontur.Focus or Seldon.Basis for comprehensive due diligence.

## 2. Kontur.Focus API

### Best Fit

- medium and large organizations;
- security, procurement, finance, and legal workflows;
- bulk checks of the complete counterparty base;
- continuous risk monitoring and stop-factor automation;
- integration with 1C, SAP, CRM, ERP, and banking systems.

### Verified Strengths

Official material describes:

- company-details completion and updating;
- bulk checks;
- continuous monitoring;
- configurable reports;
- related-company analysis;
- a constructor with 100 risk markers;
- EGRUL/EGRIP data, bankruptcy, enforcement, arbitration, financial statements, public contracts, trademarks, licenses, and additional contacts.

The official site states that more than 30 integration modules are available and more than 1,400 customers use the API.

### Limitations

- Final API pricing is not transparent enough to calculate without selecting a configuration, obtaining the price list, and consulting the vendor.
- Commercial onboarding is required; demo access is request-based.
- The developer portal is public, but the interactive reference requires JavaScript. Current authentication details, rate limits, and contractual data rights must be reconfirmed with demo access.
- AML / 115-FZ and sanctions screening are provided through the separate Kontur.Compliance API product.

### Verdict

**The most compelling candidate for a mature enterprise due-diligence and monitoring workflow.** Procurement should still require an exact method matrix, limits, storage rights, SLA, and a quote for the expected volume.

## 3. Seldon.Basis API

### Best Fit

- relationship, procurement, litigation, and financial analysis;
- scoring and analytics;
- high-volume CRM/ERP enrichment;
- Russia and CIS company coverage;
- selecting an individual set of API methods.

### Verified Strengths

Official material states that the API returns structured JSON and may provide:

- registration data;
- managers and owners;
- financial statements;
- arbitration and enforcement data;
- bankruptcy data;
- public contracts;
- bank guarantees;
- relationships;
- indices and express analysis;
- monitoring;
- Russia and CIS company data.

For the individual API plan, the vendor publishes a reference limit of **10,000 requests per day per method**, with each method priced separately. The universal plan is structured around the number of companies checked.

### Limitations

- Exact API pricing is not publicly disclosed and requires a commercial proposal.
- Public web-subscription prices must not be treated as API prices.
- Detailed technical documentation, authentication, SLA, and storage/redistribution rights require validation in the trial and contract.
- At the research date, the site displayed a temporary notice about DDoS attacks and potential service instability. This should be rechecked and not treated as a permanent product characteristic.

### Verdict

**A strong candidate for broad analytics, relationship discovery, and CIS coverage.** It is especially relevant when the buyer needs a configurable set of methods rather than a single company profile.

## 4. GLOBAS.API

### Best Fit

- organizations evaluating GLOBAS as an enterprise data source;
- CRM, ERP, EDI, risk-system, and internal analytics enrichment;
- mass counterparty checks;
- enrichment of an existing internal company database;
- portfolio monitoring and change tracking.

### Verified / Provider-Reported Strengths

Official Credinform/GLOBAS material confirms an active GLOBAS.API product page and positions the product for integrating GLOBAS data into corporate systems. The official page describes keeping counterparty information current in the user's database, monitoring portfolio changes, mass counterparty checks, building an automatically updated client base, enriching an internal base with GLOBAS company data, updating selected fields, data verification, archives, and automatic updates for large counterparty databases.

Those are useful enterprise scenarios, but the current Atlas evidence is mostly product positioning rather than developer documentation.

### Limitations

- Public API specification, endpoint catalog, authentication, schemas, formats, production limits, SLA, and API price were not found in reviewed official pages.
- The three-day GLOBAS system test must not be treated as an API trial until Credinform confirms API credentials or sandbox access.
- Sanctions Compliance appears as a separate product/module boundary and must not be assumed to be part of the standard API.
- The legacy API Portal REST claim remains provenance only and is not a verified technical fact.

### Verdict

**A credible additional enterprise candidate, not a replacement for the current Kontur.Focus / Seldon.Basis shortlist.** Include GLOBAS.API in an RFI/RFP when the organization wants Credinform coverage or already uses GLOBAS, but require specification, sandbox/pilot, method-level pricing, batch billing, SLA, and written data rights before ranking it against the other enterprise candidates.

## 5. Official FTS EGRUL/EGRIP Integration

### What It Is

This is not a typical single-company REST lookup API. The FTS provides archive access containing XML files:

- a full snapshot at the start of the year;
- daily changes;
- separate directories for EGRUL and EGRIP;
- up to 100 XML files per archive and up to 1,000 records per file.

The customer must build downloading, extraction, parsing, normalization, delta application, gap handling, and local storage.

### Public Pricing

Pricing is published **per registry**:

| Access mode | Price |
|---|---:|
| Annual subscription for one workstation | RUB 150,000 for EGRUL or EGRIP |
| One-time delivery of one registry | RUB 50,000 |
| One-time delivery of updates for an already obtained registry | RUB 5,000 |

The published per-registry price implies **RUB 300,000 per year** for both EGRUL and EGRIP for one workstation, before engineering and operations. This is an arithmetic inference from the official per-registry fee.

### 2026 Format Migration

Until 1 August 2026, the FTS is in a transition period:

- EGRUL: old format 4.07 and new format 4.08;
- EGRIP: old format 4.06 and new format 4.07.

Atlas rechecked the official FTS sources on 2026-08-15. The current public material now has an official-source conflict:

- the service pages still say files are currently uploaded in both old and new formats;
- the same pages also say that from 1 August 2026 delivery is only in EGRUL 4.08 and EGRIP 4.07;
- Order No. `ЕД-7-14/613@` requires exclusive new-format delivery from 2026-08-01.

Without credentialed FTP access or an updated official clarification, Atlas cannot prove which statement reflects actual current delivery behavior.

The FTS also warns that daily-file generation can be interrupted because of data volume; missing changes are expected to appear in later files.

### Limitations

- No turnkey scoring, court history, procurement, or risk monitoring.
- Requires a data engineering team and infrastructure.
- Access is tied to a workstation subscription model.
- Restricted information is excluded from public registry data.
- The web search mode does not permit file export for information-system use; the dedicated integration mode is required.

### Verdict

**The best source for building an internal registry database with strong provenance, but not a ready-made counterparty-checking product.** It becomes attractive when an organization is prepared to own the ETL pipeline and combine EGRUL/EGRIP with other primary sources.

## Scenario Recommendations

### B2B Form or Online Store

Need company name, KPP, OGRN, address, and OKVED by INN.

**Choose DaData.** Its free start and public documentation minimize experiment cost.

### Sales CRM

Need company cards, current identifiers, and occasional relationship analysis.

**Start with DaData.** Pilot **Seldon.Basis** when deeper relationships, procurement, or risk signals are required. Include **GLOBAS.API** in the RFI when the CRM project needs enterprise enrichment from Credinform/GLOBAS and the buyer can wait for vendor documentation and a quote.

### Procurement and Corporate Security

Need bulk checks, stop factors, litigation, bankruptcy, enforcement, and monitoring.

**Shortlist Kontur.Focus API and Seldon.Basis API.** Treat **GLOBAS.API** as an additional enterprise candidate when mass checks, internal-base enrichment, or portfolio monitoring are central requirements. Decide after an equal-sample pilot, technical documentation, and commercial quotes.

### Enterprise Data Enrichment RFP

Need CRM/ERP/EDI enrichment, bulk verification, portfolio monitoring, and legal rights to store or show data.

**Request proposals from Kontur.Focus, Seldon.Basis, and GLOBAS.API.** Do not rank GLOBAS.API above or below the others until Credinform provides the API method matrix, field coverage, pricing, limits, SLA, sandbox and data-use terms.

### Bank or Regulated Organization

Need KYC/AML, sanctions, and auditable rules.

**Evaluate Kontur.Compliance API separately.** This comparison alone is insufficient to establish 115-FZ compliance.

### Internal Data Platform

Need a complete registry copy, history, and custom models.

**Use the FTS integration as the foundation**, then add courts, enforcement, procurement, bankruptcy, and financial reporting sources. Commercial aggregators may accelerate delivery or provide quality control.

## Recommended Pilot

Give Kontur, Seldon, and any GLOBAS.API pilot the same test set:

1. 100 active companies of different sizes;
2. 30 liquidating or recently liquidated companies;
3. 20 companies with bankruptcy or enforcement history;
4. 20 companies with complex relationships;
5. 20 individual entrepreneurs;
6. CIS companies when relevant.

Measure:

- completeness and freshness;
- false and missing risk signals;
- p50/p95/p99 latency;
- quota and 429/5xx behavior;
- history and explainability of markers;
- rights to store responses;
- sandbox availability;
- monitoring behavior;
- actual monthly and annual cost;
- support when data conflicts with a primary source.
- for GLOBAS.API specifically: confirm that test access includes API credentials rather than only web-system access.

## What This Comparison Does Not Yet Prove

- measured latency and availability;
- scoring-model accuracy;
- complete Kontur and Seldon cost;
- complete GLOBAS.API technical and commercial terms;
- legal rights for long-term storage or resale of every field;
- superiority on a real customer dataset.

Gold maturity requires commercial demo credentials, a common benchmark, and contract review.

## Sources

See [evidence.md](evidence.md) for claim-level evidence.

Primary official pages:

- [DaData company lookup](https://dadata.ru/api/find-party/)
- [DaData pricing](https://dadata.ru/pricing/)
- [Kontur.Focus API](https://focus.kontur.ru/site/api)
- [Kontur API selection and developer reference](https://focus.kontur.ru/site/api-choice)
- [Kontur API company-details demo](https://focus.kontur.ru/site/demo/requisites)
- [Seldon.Basis API](https://seldongroup.ru/system/basis/api)
- [Seldon API functionality](https://seldongroup.ru/functions)
- [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api)
- [GLOBAS services](https://globas.credinform.ru/ru-RU/servisy)
- [GLOBAS sources](https://globas.credinform.ru/ru-RU/osisteme/istochniki)
- [FTS EGRUL/EGRIP integration service](https://www.nalog.gov.ru/rn77/service/egrip2/)
- [FTS interaction model and formats](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/)
- [FTS access process and fees](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/)

## Disclosure

No sponsorship, referral agreement, or vendor-provided commercial access was used. The comparison is based on public official material.

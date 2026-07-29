# FIAS/GAR Open Data Recheck

Date: 2026-07-29

## Scope

This log narrows the public open-data/file-download facts for FIAS/GAR without treating FIAS website screens or discovered endpoints as supported public APIs.

## Official Sources Reviewed

- https://www.nalog.gov.ru/opendata/7707329152-fias/
- https://www.nalog.gov.ru/rn77/service/fias/
- https://fias-file.nalog.ru/
- https://fias-file.nalog.ru/Frontend
- https://www.nalog.gov.ru/rn77/news/activities_fts/16629379/

## Confirmed Facts

- The official FNS open-data catalog has dataset identifier `7707329152-fias`.
- The dataset name is "Государственный адресный реестр (Федеральная информационная адресная система)".
- The dataset owner is FNS Russia.
- The data format is listed as `xml`.
- The current open-data page lists a ZIP data URL under `fias.nalog.ru/opendata/7707329152-fias/`.
- The page lists a separate structure description ZIP under `data.nalog.ru/opendata/7707329152-fias/`.
- The page states weekly dataset updates.
- On the reviewed page, the latest modification date is 2026-07-28 and the page update date is 2026-07-29.
- The open-data page lists previous release ZIP links, supporting a release-history model.
- The FIAS portal developer section exposes open data/file downloads, SMEV and API-services entries.
- FNS news from 2026-06-09 states that KLADR publication changes from 2026-07-01 to quarterly, from 2027-01-01 to semiannual, and stops from 2028-01-01.

## Provider-Reported Claims

- FNS portal material positions GAR as the only legitimate source of address information.
- FNS news states that GAR addresses are presented exclusively in municipal-division structure.

## Observations

- The open-data route has enough public evidence to mark file format and update cadence as verified for the open-data catalog.
- The page does not prove a REST-style API method catalog, authentication model, quotas or SLA for API services.
- The open-data ZIP and structure ZIP were not downloaded or inspected by Atlas in this pass.
- KLADR is a legacy format with an official sunset path; it should not be treated as the target integration model for new Atlas recommendations.

## Unknowns

- Contents and schema files inside the current ZIP archives, because no download/inspection was performed.
- Whether the open-data ZIP is a full snapshot, delta, or mixed package in the current publication model.
- API-services method catalog, base URLs, authentication, schemas, quotas, cost and SLA.
- SMEV eligibility and access process.
- Commercial SaaS, redistribution, customer-facing display and derived database rights.

## Contradictions

- No contradiction was found. The main distinction is that official open-data file details are now clearer, while API-service details remain underspecified.

## Live Testing Status

No Atlas download, API call, SMEV access, portal-endpoint test or benchmark was performed.

## Decision

Update `apis/fias-gar-data-integration/` to treat open-data XML ZIP availability and weekly update cadence as verified. Keep API-services details as unknown until official method documentation or authorized access evidence is available.

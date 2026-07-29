# FIAS/GAR Open-Data Package Metadata Research Log

Date: 2026-07-29

## Scope

This log refines the public metadata for the current official GAR/FIAS open-data package without downloading or inspecting binary ZIP archives.

It addresses the TODO item about FIAS/GAR package details as far as official public metadata allows. It does not prove inner archive contents, full/delta semantics, API service methods, SMEV eligibility, quotas, costs or legal rights.

Follow-up: [`2026-07-29-fias-gar-data-zip-central-directory.md`](2026-07-29-fias-gar-data-zip-central-directory.md) later inspected the current data ZIP central directory and `version.txt` via HTTP Range. XML payload, row counts and full/delta semantics remain unverified.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Current data URL, format, structure URL, dates, previous releases |
| FIAS Info page | https://fias-file.nalog.ru/FiasInfo | Official GAR/FIAS identity, operator, legal context, public-site software update date |
| FIAS developer section | https://fias-file.nalog.ru/Frontend | Developer navigation entries for open data, SMEV and API services |

## Confirmed Current Metadata

| Metadata | Official page value | Treatment |
|---|---|---|
| Dataset identifier | `7707329152-fias` | verified |
| Dataset name | State Address Register / FIAS | verified |
| Owner | FNS Russia | verified |
| Format | XML | verified |
| Current data URL | `https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip` | verified as official metadata; archive not downloaded |
| Structure URL | `https://data.nalog.ru/opendata/7707329152-fias/structure-12032021.zip` | verified as official metadata; archive not downloaded |
| First publication date | 2012-01-16 | verified |
| Last modification date | 2026-07-28 | verified |
| Latest change description | Weekly dataset update | verified |
| Official page actuality date | 2026-08-02 | provider_reported_metadata |
| Previous data releases shown | 2026-07-24, 2026-07-21, 2026-07-17, 2026-07-14 | verified as page links |
| Methodological recommendations version | 4.0 | verified |
| FIAS public-site software update date | 2026-07-20 | verified as portal metadata |

## Observations

- The current data URL naming includes both a data date (`28072026`) and a structure marker (`structure-20191024`), while the separate structure archive URL is `structure-12032021.zip`.
- The open-data page lists previous release ZIP files, which supports the file-publication route, but does not by itself define whether each package is full, delta or mixed.
- The official page reports an actuality date of 2026-08-02, which is after the Atlas check date. Atlas records this as page metadata, not as an independently verified future state.
- The FIAS developer page still exposes Open data/file downloads, SMEV and API services as entries, but does not expose a static public method catalog in the reviewed page.

## Unknowns and Blockers

- Inner ZIP archive file list and schemas were not inspected.
- Whether the current package is full, delta or mixed remains unknown from reviewed metadata alone.
- Whether previous release links imply full snapshots or update packages remains unknown.
- API services method catalog, base URL, auth, schemas, quotas, costs and SLA remain unknown.
- SMEV eligibility and access process remain unknown.
- Commercial SaaS, redistribution, customer display and derived database rights still require legal review.

## Live Testing Status

No archive download, checksum, ZIP inspection, API-service request, SMEV access or portal-endpoint live test was performed.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. Update it with current official package metadata, but do not upgrade it to a conventional API profile and do not mark ZIP contents or full/delta semantics as verified.

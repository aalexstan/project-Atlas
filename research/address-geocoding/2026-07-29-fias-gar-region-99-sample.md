# FIAS/GAR Region 99 XML Sample Inspection - 2026-07-29

## Scope

This log inspects one small regional directory, `99/`, from the current official FIAS/GAR open-data ZIP.

The goal is to verify that regional XML payload can be decompressed and parsed from official byte ranges, and to record sample row counts for one region without downloading the 57 GB archive.

It does not produce national row counts, validate all CRC values, prove full/delta semantics, verify API-service methods, or perform credentialed live testing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Current official data archive | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP Range reads for all `99/` XML entries listed in the central directory |
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official current archive URL and package metadata |

## Retrieval Method

- Used the central-directory file list from [`2026-07-29-fias-gar-data-zip-central-directory.md`](2026-07-29-fias-gar-data-zip-central-directory.md).
- Selected regional directory `99/` because it is a non-empty, comparatively small sample: 18 files, 4,234,620 compressed bytes and 34,261,816 uncompressed bytes according to central directory metadata.
- Downloaded each `99/` local ZIP entry by HTTP Range into `/tmp` only.
- Decompressed each entry locally and parsed XML root/child counts.
- Did not keep downloaded XML payload in the repository.

## Sample Row Counts

| File group | Root tag | Rows | Compressed bytes | Uncompressed bytes |
|---|---|---:|---:|---:|
| `AS_REESTR_OBJECTS` | `REESTR_OBJECTS` | 21,729 | 655,454 | 3,823,568 |
| `AS_ADDR_OBJ` | `ADDRESSOBJECTS` | 220 | 8,902 | 67,482 |
| `AS_HOUSES` | `HOUSES` | 746 | 35,748 | 205,043 |
| `AS_STEADS` | `STEADS` | 66 | 2,982 | 17,188 |
| `AS_APARTMENTS` | `APARTMENTS` | 20,828 | 926,354 | 5,787,687 |
| `AS_ROOMS` | `ROOMS` | 0 | 52 | 50 |
| `AS_CARPLACES` | `CARPLACES` | 0 | 56 | 54 |
| `AS_ADM_HIERARCHY` | `ITEMS` | 21,736 | 270,116 | 5,514,460 |
| `AS_MUN_HIERARCHY` | `ITEMS` | 21,729 | 594,310 | 5,421,293 |
| `AS_CHANGE_HISTORY` | `ITEMS` | 24,406 | 935,474 | 3,825,244 |
| `AS_ADDR_OBJ_DIVISION` | `ITEMS` | 0 | 52 | 50 |
| `AS_ADDR_OBJ_PARAMS` | `PARAMS` | 828 | 10,077 | 147,869 |
| `AS_STEADS_PARAMS` | `PARAMS` | 503 | 5,448 | 91,052 |
| `AS_HOUSES_PARAMS` | `PARAMS` | 6,516 | 82,358 | 1,171,140 |
| `AS_APARTMENTS_PARAMS` | `PARAMS` | 41,656 | 696,686 | 7,891,363 |
| `AS_ROOMS_PARAMS` | `PARAMS` | 0 | 53 | 51 |
| `AS_CARPLACES_PARAMS` | `PARAMS` | 0 | 53 | 51 |
| `AS_NORMATIVE_DOCS` | `NORMDOCS` | 794 | 10,445 | 298,171 |

Total sample rows across `99/`: `161757`.

## Observations

- Region `99/` includes non-empty address objects, houses, land plots, apartments, hierarchies, parameters, change history and normative documents.
- Some groups are empty in this sample (`AS_ROOMS`, `AS_CARPLACES`, `AS_ADDR_OBJ_DIVISION`, `AS_ROOMS_PARAMS`, `AS_CARPLACES_PARAMS`).
- `AS_ADM_HIERARCHY` and `AS_MUN_HIERARCHY` both use root tag `ITEMS`; implementers should rely on file group and schema, not only root tag.
- Sample row counts are useful for ETL smoke testing, but they are not national row counts and should not be generalized to other regions.

## Unknowns and Blockers

- Other regional directories were not decompressed.
- National row counts remain unknown.
- CRC values were not validated against every payload entry in the archive.
- Full/delta package semantics remain unproved.
- API-service method catalog, base URL, authentication, quotas, costs, SLA and SMEV eligibility remain unknown.
- Legal-use rights for commercial SaaS, redistribution and customer-facing display still require legal review.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data ingest was performed. This pass only decompressed one small public regional sample from the official open-data ZIP via HTTP Range.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. Region `99/` confirms that regional XML payload can be parsed and counted from official ZIP entries, but the profile must still avoid national row-count, full/delta, API-service or live-test claims.

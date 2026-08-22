# FIAS/GAR Region 82 XML Sparse Sample Inspection - 2026-07-29

## Scope

This log inspects regional directory `82/` from the current official FIAS/GAR open-data ZIP.

The goal is to verify a sparse regional payload edge case and record that some regional directories can contain mostly empty XML groups while still being valid ZIP entries.

It does not produce national row counts, validate all archive entries, prove full/delta semantics, verify API-service methods, or perform credentialed live testing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Current official data archive | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP Range reads for all `82/` XML entries listed in the central directory |
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official current archive URL and package metadata |

## Retrieval Method

- Re-read the official ZIP64 central directory through HTTP Range.
- Parsed ZIP64 extra fields to obtain true compressed sizes, uncompressed sizes and local-header offsets.
- Selected regional directory `82/` as a sparse/empty-edge sample: 18 files, 1,966 compressed bytes and 4,120 uncompressed bytes according to central directory metadata.
- Downloaded each `82/` local ZIP entry by HTTP Range into memory only.
- Decompressed each entry locally, parsed XML root/child counts, and compared decompressed size plus CRC32 against central-directory metadata.
- Did not keep downloaded XML payload in the repository.

## Sample Row Counts

| File group | Root tag | Rows | Compressed bytes | Uncompressed bytes | CRC/size |
|---|---|---:|---:|---:|---|
| `AS_ADDR_OBJ` | `ADDRESSOBJECTS` | 1 | 276 | 368 | ok |
| `AS_ADDR_OBJ_DIVISION` | `ITEMS` | 0 | 52 | 50 | ok |
| `AS_ADDR_OBJ_PARAMS` | `PARAMS` | 6 | 306 | 1,148 | ok |
| `AS_ADM_HIERARCHY` | `ITEMS` | 5 | 341 | 1,498 | ok |
| `AS_APARTMENTS` | `APARTMENTS` | 0 | 57 | 55 | ok |
| `AS_APARTMENTS_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |
| `AS_CARPLACES` | `CARPLACES` | 0 | 56 | 54 | ok |
| `AS_CARPLACES_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |
| `AS_CHANGE_HISTORY` | `ITEMS` | 1 | 163 | 192 | ok |
| `AS_HOUSES` | `HOUSES` | 0 | 53 | 51 | ok |
| `AS_HOUSES_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |
| `AS_MUN_HIERARCHY` | `ITEMS` | 0 | 52 | 50 | ok |
| `AS_NORMATIVE_DOCS` | `NORMDOCS` | 0 | 55 | 53 | ok |
| `AS_REESTR_OBJECTS` | `REESTR_OBJECTS` | 1 | 185 | 245 | ok |
| `AS_ROOMS` | `ROOMS` | 0 | 52 | 50 | ok |
| `AS_ROOMS_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |
| `AS_STEADS` | `STEADS` | 0 | 53 | 51 | ok |
| `AS_STEADS_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |

Total sample rows across `82/`: `14`.

## Observations

- Region `82/` is a sparse regional directory with only 14 child records across 18 XML files.
- Many XML groups are valid but empty in this sample.
- Empty group files still have root tags and pass CRC/size validation.
- ETL design should handle empty regional files and not assume every region has houses, apartments, rooms, normative docs or municipal hierarchy rows.
- This provides sample-level edge-case evidence, not full-archive CRC validation.

## Unknowns and Blockers

- Remaining regional directories were not decompressed.
- National row counts remain unknown.
- CRC values were validated only for sampled regions, not for the full archive.
- Full/delta package semantics remain unproved.
- API-service method catalog, base URL, authentication, quotas, costs, SLA and SMEV eligibility remain unknown.
- Legal-use rights for commercial SaaS, redistribution and customer-facing display still require legal review.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data ingest was performed. This pass only decompressed one sparse public regional sample from the official open-data ZIP via HTTP Range.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. Region `82/` adds edge-case evidence for sparse regional files and empty groups, but Atlas still must not claim national row counts, full/delta semantics, supported API-service behavior or live testing.

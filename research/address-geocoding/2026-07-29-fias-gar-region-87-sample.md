# FIAS/GAR Region 87 XML Sample Inspection - 2026-07-29

## Scope

This log inspects regional directory `87/` from the current official FIAS/GAR open-data ZIP.

The goal is to verify a second non-empty regional payload, compare it with the earlier `99/` sample, and validate CRC/size for all downloaded entries without downloading the 57 GB archive.

It does not produce national row counts, validate all archive entries, prove full/delta semantics, verify API-service methods, or perform credentialed live testing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Current official data archive | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP Range reads for all `87/` XML entries listed in the central directory |
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official current archive URL and package metadata |

## Retrieval Method

- Re-read the official ZIP64 central directory through HTTP Range.
- Parsed ZIP64 extra fields to obtain true compressed sizes, uncompressed sizes and local-header offsets.
- Selected regional directory `87/` as a second small-but-nontrivial sample: 18 files, 10,708,170 compressed bytes and 76,300,664 uncompressed bytes according to central directory metadata.
- Downloaded each `87/` local ZIP entry by HTTP Range into memory only.
- Decompressed each entry locally, parsed XML root/child counts, and compared decompressed size plus CRC32 against central-directory metadata.
- Did not keep downloaded XML payload in the repository.

## Sample Row Counts

| File group | Root tag | Rows | Compressed bytes | Uncompressed bytes | CRC/size |
|---|---|---:|---:|---:|---|
| `AS_ADDR_OBJ` | `ADDRESSOBJECTS` | 1,636 | 62,306 | 497,859 | ok |
| `AS_ADDR_OBJ_DIVISION` | `ITEMS` | 12 | 275 | 944 | ok |
| `AS_ADDR_OBJ_PARAMS` | `PARAMS` | 15,247 | 227,373 | 2,754,894 | ok |
| `AS_ADM_HIERARCHY` | `ITEMS` | 32,287 | 545,865 | 8,469,433 | ok |
| `AS_APARTMENTS` | `APARTMENTS` | 23,707 | 1,159,351 | 6,519,525 | ok |
| `AS_APARTMENTS_PARAMS` | `PARAMS` | 41,639 | 986,890 | 8,071,380 | ok |
| `AS_CARPLACES` | `CARPLACES` | 0 | 56 | 54 | ok |
| `AS_CARPLACES_PARAMS` | `PARAMS` | 0 | 53 | 51 | ok |
| `AS_CHANGE_HISTORY` | `ITEMS` | 91,459 | 3,378,598 | 13,706,178 | ok |
| `AS_HOUSES` | `HOUSES` | 9,166 | 374,482 | 2,569,539 | ok |
| `AS_HOUSES_PARAMS` | `PARAMS` | 82,287 | 1,308,800 | 14,896,213 | ok |
| `AS_MUN_HIERARCHY` | `ITEMS` | 36,656 | 1,258,814 | 9,823,349 | ok |
| `AS_NORMATIVE_DOCS` | `NORMDOCS` | 4,715 | 117,382 | 1,545,349 | ok |
| `AS_REESTR_OBJECTS` | `REESTR_OBJECTS` | 31,598 | 1,080,382 | 5,525,610 | ok |
| `AS_ROOMS` | `ROOMS` | 2,439 | 91,648 | 650,600 | ok |
| `AS_ROOMS_PARAMS` | `PARAMS` | 2,535 | 49,558 | 510,957 | ok |
| `AS_STEADS` | `STEADS` | 337 | 17,003 | 85,973 | ok |
| `AS_STEADS_PARAMS` | `PARAMS` | 3,720 | 49,334 | 672,756 | ok |

Total sample rows across `87/`: `379440`.

## Observations

- Region `87/` is materially larger than region `99/` but still small enough for a controlled byte-range inspection.
- Region `87/` includes non-empty rooms and room parameters, unlike sample region `99/`.
- `AS_CARPLACES` and `AS_CARPLACES_PARAMS` are empty in this sample.
- `AS_CHANGE_HISTORY` and house parameters are the largest row groups in this sample.
- CRC32 and uncompressed size matched central-directory metadata for all 18 downloaded entries.
- This provides sample-level payload integrity evidence, not full-archive CRC validation.

## Unknowns and Blockers

- Remaining regional directories were not decompressed.
- National row counts remain unknown.
- CRC values were validated only for `87/`, not for the full archive.
- Full/delta package semantics remain unproved.
- API-service method catalog, base URL, authentication, quotas, costs, SLA and SMEV eligibility remain unknown.
- Legal-use rights for commercial SaaS, redistribution and customer-facing display still require legal review.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data ingest was performed. This pass only decompressed one public regional sample from the official open-data ZIP via HTTP Range.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. Region `87/` strengthens evidence that regional XML payload can be parsed and sample-level CRC/size can be validated from official ZIP entries, but Atlas still must not claim national row counts, full/delta semantics, supported API-service behavior or live testing.

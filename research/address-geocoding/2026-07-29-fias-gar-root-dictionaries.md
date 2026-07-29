# FIAS/GAR Root Dictionary XML Inspection - 2026-07-29

## Scope

This log inspects the small root-level dictionary XML files at the beginning of the current official FIAS/GAR open-data ZIP.

It uses the central-directory offsets recorded in [`2026-07-29-fias-gar-data-zip-central-directory.md`](2026-07-29-fias-gar-data-zip-central-directory.md) and downloads only the first 64 KiB of the official archive.

It does not decompress regional address-object XML files, count national/regional rows, validate all CRC values against full payload, prove full/delta semantics, verify API-service methods, or perform credentialed live testing.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Current official data archive | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP Range read of root-level `version.txt` and dictionary XML payload |
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official current archive URL and package metadata |

## Confirmed Facts

| Fact | Status | Evidence |
|---|---|---|
| `version.txt` content is `2026.07.28` and `v.278`. | verified | Extracted from official archive byte range. |
| Ten root-level dictionary XML files were decompressed and parsed successfully. | verified | Local XML parsing of official archive byte range. |
| The dictionary XML payload contains type/reference records, not regional address objects. | verified | Root tags and child tags in parsed XML files. |
| Regional XML payload was not decompressed in this pass. | verified | Retrieval was limited to the first 64 KiB. |

## Root Dictionary Row Counts

| File group | Root tag | Child tag | Rows |
|---|---|---|---:|
| `AS_APARTMENT_TYPES` | `APARTMENTTYPES` | `APARTMENTTYPE` | 13 |
| `AS_ADDR_OBJ_TYPES` | `ADDRESSOBJECTTYPES` | `ADDRESSOBJECTTYPE` | 427 |
| `AS_ROOM_TYPES` | `ROOMTYPES` | `ROOMTYPE` | 3 |
| `AS_OPERATION_TYPES` | `OPERATIONTYPES` | `OPERATIONTYPE` | 34 |
| `AS_PARAM_TYPES` | `PARAMTYPES` | `PARAMTYPE` | 22 |
| `AS_HOUSE_TYPES` | `HOUSETYPES` | `HOUSETYPE` | 14 |
| `AS_ADDHOUSE_TYPES` | `HOUSETYPES` | `HOUSETYPE` | 4 |
| `AS_OBJECT_LEVELS` | `OBJECTLEVELS` | `OBJECTLEVEL` | 17 |
| `AS_NORMATIVE_DOCS_TYPES` | `NDOCTYPES` | `NDOCTYPE` | 25 |
| `AS_NORMATIVE_DOCS_KINDS` | `NDOCKINDS` | `NDOCKIND` | 5 |

## Observations

- Dictionary rows expose attributes such as `ID`, `NAME`, `SHORTNAME`, `DESC`, `ISACTIVE`, `STARTDATE`, `ENDDATE`, `UPDATEDATE`, `LEVEL` and `CODE`, depending on file group.
- The file `AS_ADDHOUSE_TYPES...XML` uses root tag `HOUSETYPES`, so implementers should not infer table semantics from root tag alone.
- The dictionary files are useful for ETL schema preparation, but they do not answer address-object volume, regional row counts, update semantics or API-service behavior.

## Unknowns and Blockers

- Regional XML payload row counts and sample records remain uninspected.
- Full CRC validation against the 57 GB payload was not performed.
- Full/delta package semantics remain unproved.
- API-service method catalog, base URL, authentication, quotas, costs, SLA and SMEV eligibility remain unknown.
- Legal-use rights for commercial SaaS, redistribution and customer-facing display still require legal review.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data ingest was performed. This pass only extracted small public root-level files from the official open-data ZIP via HTTP Range.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. Root dictionaries are now partially payload-inspected evidence, but the profile should still not claim complete archive contents, row counts, API behavior, full/delta semantics or live testing.

# FIAS/GAR Data ZIP Central Directory Inspection - 2026-07-29

## Scope

This log inspects the ZIP central directory of the current official FIAS/GAR open-data archive without downloading the 57 GB XML payload.

It covers archive-level metadata, file names, CRC values as listed in the central directory, compressed/uncompressed sizes, regional directory count, table-file groups and `version.txt`.

It does not decompress production XML files, count XML rows, validate CRC values against full payload bytes, prove full/delta semantics, verify API-service methods, or perform credentialed live testing.

Follow-up: [`2026-07-29-fias-gar-root-dictionaries.md`](2026-07-29-fias-gar-root-dictionaries.md) later decompressed and parsed the small root-level dictionary XML files. Regional XML payload, national row counts and full/delta semantics remain unverified.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official current archive URL and package metadata |
| Current official data archive | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP HEAD, HTTP Range read of ZIP64 central directory and `version.txt` |

## Retrieval Method

- Performed `HEAD` request against the official archive URL.
- Confirmed `Accept-Ranges: bytes`, `Content-Type: application/zip`, `Content-Length: 57170912095` and `Last-Modified: Mon, 27 Jul 2026 17:57:53 GMT`.
- Downloaded the final 64 KiB byte range to locate ZIP end-of-central-directory records.
- Parsed ZIP64 EOCD values:
  - total entries: `1739`;
  - central directory size: `246074` bytes;
  - central directory offset: `57170665923`.
- Downloaded only byte range `57170665923-57170912094`, containing the central directory and end records.
- Downloaded only the first 257 bytes to extract `version.txt`.
- Temporary files were kept in `/tmp` only and are not repository artifacts.

## Confirmed Facts

| Fact | Status | Evidence |
|---|---|---|
| The current official data archive is ZIP64. | verified | EOCD/ZIP64 locator inspection. |
| The central directory lists 1,739 entries. | verified | Parsed central directory. |
| The archive contains 1 `version.txt` entry and 1,738 `.XML` entries. | verified | Parsed central directory. |
| The archive uses Deflate compression for all listed entries. | verified | Central directory compression method `8` for all entries. |
| The central directory lists 96 regional directories with two-digit codes from `01` through `99`; codes `96`, `97` and `98` were not present. | verified | Parsed path prefixes containing `/`. |
| There are 11 root-level files: `version.txt` and 10 dictionary/type XML files. | verified | Parsed entries without regional path prefix. |
| `version.txt` content is `2026.07.28` and `v.278`. | verified | Extracted from the first small byte range of the archive. |
| Sum of compressed entry sizes from the central directory is `57170460881` bytes. | observed | Central directory size fields; not independent payload validation. |
| Sum of uncompressed entry sizes from the central directory is `424935482896` bytes. | observed | Central directory size fields; not independent XML decompression. |
| CRC32 values are present for listed entries in the central directory. | observed | Parsed central directory; CRCs were not validated by reading all payload bytes. |

## Table/File Groups

| Group | Files | Compressed bytes | Uncompressed bytes |
|---|---:|---:|---:|
| `AS_ADDHOUSE_TYPES` | 1 | 277 | 750 |
| `AS_ADDR_OBJ` | 96 | 138,929,489 | 1,045,237,593 |
| `AS_ADDR_OBJ_DIVISION` | 96 | 131,813 | 700,223 |
| `AS_ADDR_OBJ_PARAMS` | 96 | 462,352,955 | 5,166,780,643 |
| `AS_ADDR_OBJ_TYPES` | 1 | 6,922 | 89,376 |
| `AS_ADM_HIERARCHY` | 96 | 2,614,613,659 | 40,788,973,006 |
| `AS_APARTMENTS` | 96 | 3,124,893,189 | 17,618,173,716 |
| `AS_APARTMENTS_PARAMS` | 96 | 3,023,864,663 | 24,872,671,809 |
| `AS_APARTMENT_TYPES` | 1 | 513 | 2,350 |
| `AS_CARPLACES` | 96 | 49,340,099 | 320,285,566 |
| `AS_CARPLACES_PARAMS` | 96 | 19,941,219 | 154,809,665 |
| `AS_CHANGE_HISTORY` | 96 | 17,596,455,683 | 71,241,719,054 |
| `AS_HOUSES` | 96 | 3,828,449,753 | 22,730,942,098 |
| `AS_HOUSES_PARAMS` | 96 | 8,967,963,273 | 101,332,236,739 |
| `AS_HOUSE_TYPES` | 1 | 512 | 2,533 |
| `AS_MUN_HIERARCHY` | 96 | 5,706,715,692 | 41,964,016,708 |
| `AS_NORMATIVE_DOCS` | 96 | 532,207,609 | 7,312,524,844 |
| `AS_NORMATIVE_DOCS_KINDS` | 1 | 236 | 548 |
| `AS_NORMATIVE_DOCS_TYPES` | 1 | 658 | 3,196 |
| `AS_OBJECT_LEVELS` | 1 | 591 | 2,918 |
| `AS_OPERATION_TYPES` | 1 | 1,034 | 8,763 |
| `AS_PARAM_TYPES` | 1 | 1,177 | 5,274 |
| `AS_REESTR_OBJECTS` | 96 | 4,666,770,352 | 22,812,013,934 |
| `AS_ROOMS` | 96 | 26,959,938 | 196,894,049 |
| `AS_ROOMS_PARAMS` | 96 | 28,881,244 | 248,847,656 |
| `AS_ROOM_TYPES` | 1 | 239 | 579 |
| `AS_STEADS` | 96 | 1,403,858,459 | 6,917,458,795 |
| `AS_STEADS_PARAMS` | 96 | 4,978,119,615 | 60,211,080,495 |
| `version.txt` | 1 | 18 | 16 |

## Important Limits

- File list and central-directory sizes are now observed, but XML payload was not downloaded or decompressed.
- CRC32 values were read from central directory metadata, not validated by reading complete entry payloads.
- Row counts remain unknown.
- The central directory does not prove whether the current package is full, delta or mixed. File naming and size distribution suggest a large registry publication, but Atlas should not state package semantics without official documentation or XML-content inspection.
- API-service method catalog, base URL, authentication, quotas, costs, SLA and SMEV eligibility remain unknown.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data ingest was performed. This pass used public HTTP HEAD/Range reads of the official open-data ZIP only.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. The current data archive file index is now inspected enough to list file groups and archive scale, but the profile must still avoid claiming turnkey API behavior, live testing, full/delta semantics, row counts or legal-use rights.

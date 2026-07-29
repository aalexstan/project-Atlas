# FIAS/GAR Structure Archive Inspection — 2026-07-29

## Scope

This log inspects the official FIAS/GAR structure archive referenced by the FNS open-data catalog.

It does not download the current 57 GB data archive, prove full/delta package semantics, inspect production data rows, verify API-service methods, or perform credentialed live testing.

Follow-up: [`2026-07-29-fias-gar-data-zip-central-directory.md`](2026-07-29-fias-gar-data-zip-central-directory.md) later inspected the current data ZIP central directory and `version.txt` via HTTP Range. XML payload, row counts and full/delta semantics remain unverified.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| FNS open-data catalog dataset `7707329152-fias` | https://www.nalog.gov.ru/opendata/7707329152-fias/ | Official data URL, structure URL and update metadata |
| Official structure archive | https://data.nalog.ru/opendata/7707329152-fias/structure-12032021.zip | XSD archive inspected in a temporary workspace |
| Current official data archive URL | https://fias.nalog.ru/opendata/7707329152-fias/data-28072026-structure-20191024.zip | HTTP headers checked only; archive not downloaded |

## Confirmed Facts

| Fact | Status | Evidence |
|---|---|---|
| The official structure archive is a ZIP file of 25,522 bytes in the downloaded copy. | verified | Temporary download from FNS structure URL. |
| The structure archive contains 22 `.xsd` files. | verified | `unzip -l` inspection of the official structure ZIP. |
| XSD root elements cover address objects, houses, rooms, apartments, car places, land plots, administrative/municipal hierarchy, normative documents, parameter/type dictionaries, object levels, operation types, register objects and change history. | verified | Parsed top-level `xs:element` names from the official structure ZIP. |
| The current official data ZIP responds with `Content-Type: application/zip` and `Content-Length: 57170912095`. | verified | HTTP headers for the official data archive URL. |
| The current official data ZIP header reports `Last-Modified: Mon, 27 Jul 2026 17:57:53 GMT`. | verified | HTTP headers for the official data archive URL. |

## Structure Archive File List

- `AS_ADDR_OBJ_2_251_01_04_01_01.xsd`
- `AS_ADDR_OBJ_DIVISION_2_251_19_04_01_01.xsd`
- `AS_ADDR_OBJ_TYPES_2_251_03_04_01_01.xsd`
- `AS_ADM_HIERARCHY_2_251_04_04_01_01.xsd`
- `AS_APARTMENTS_2_251_05_04_01_01.xsd`
- `AS_APARTMENT_TYPES_2_251_07_04_01_01.xsd`
- `AS_CARPLACES_2_251_06_04_01_01.xsd`
- `AS_CHANGE_HISTORY_251_21_04_01_01.xsd`
- `AS_HOUSES_2_251_08_04_01_01.xsd`
- `AS_HOUSE_TYPES_2_251_13_04_01_01.xsd`
- `AS_MUN_HIERARCHY_2_251_10_04_01_01.xsd`
- `AS_NORMATIVE_DOCS_2_251_11_04_01_01.xsd`
- `AS_NORMATIVE_DOCS_KINDS_2_251_09_04_01_01.xsd`
- `AS_NORMATIVE_DOCS_TYPES_2_251_16_04_01_01.xsd`
- `AS_OBJECT_LEVELS_2_251_12_04_01_01.xsd`
- `AS_OPERATION_TYPES_2_251_14_04_01_01.xsd`
- `AS_PARAM_2_251_02_04_01_01.xsd`
- `AS_PARAM_TYPES_2_251_20_04_01_01.xsd`
- `AS_REESTR_OBJECTS_2_251_22_04_01_01.xsd`
- `AS_ROOMS_2_251_15_04_01_01.xsd`
- `AS_ROOM_TYPES_2_251_17_04_01_01.xsd`
- `AS_STEADS_2_251_18_04_01_01.xsd`

## Unknowns and Blockers

- The 57 GB data archive was not downloaded, so production file names, row counts, checksums and compression layout remain unknown.
- The XSD archive confirms schema file names and root elements, but does not prove whether each current data publication is a full snapshot, a delta package or a mixed package.
- API-service method catalog, base URL, authentication, quotas, costs and SLA remain unknown.
- SMEV eligibility and process remain unknown.
- Commercial SaaS, redistribution, customer-facing display and derived database rights still require legal review.

## Live Testing Status

No credentialed API request, SMEV access, portal endpoint test or production data archive ingest was performed. The only live check in this pass was temporary retrieval of the public structure ZIP and HTTP header inspection of the public data ZIP.

## Profile Decision

Keep `apis/fias-gar-data-integration/` as a data-integration profile. The official structure archive can now be treated as inspected evidence for XSD coverage, but Atlas should still not present FIAS/GAR as a conventional REST API or claim full/delta semantics until the current data archive and official API-service documentation are reviewed.

# FIAS/GAR Data Integration Changes

[Русская версия](changes.ru.md)

| Date | Change | Impact |
|---|---|---|
| 2026-07-29 | Linked legacy dataset note `datasets/russian_address_registry.md` to the active API-first FIAS/GAR profile. | Preserves Pass #2 provenance while making the official registry/data-integration route discoverable. |
| 2026-07-29 | Initial API-first data-integration profile created from official FNS and FIAS/GAR pages. | Adds the official Russian address registry route without presenting it as a normal REST geocoder. |
| 2026-07-29 | Clarified official integration channels: file downloads, SMEV and API services; separated user-facing portal pages from supported public APIs. | Improves procurement blockers without upgrading unknown API method details. |
| 2026-07-29 | Added official open-data catalog details: dataset identifier, XML ZIP data link, structure ZIP, weekly updates, previous releases and KLADR sunset path. | Confirms open-data/file route details while keeping API-service specification unknown. |
| 2026-07-29 | Added current official package metadata for `data-28072026-structure-20191024.zip`, visible previous releases, last modification, actuality date and methodological recommendations version. | Narrows file-route uncertainty without claiming archive contents or full/delta semantics were inspected. |
| 2026-07-29 | Inspected the official `structure-12032021.zip` archive and recorded the 22 XSD schema files; checked data ZIP HTTP headers and size without downloading the 57 GB archive. | Confirms schema coverage while keeping production data contents and full/delta semantics as blockers. |
| 2026-07-29 | Inspected the current data ZIP central directory via HTTP Range and extracted root `version.txt`. | Confirms production file index, archive scale and version marker without downloading XML payload or proving full/delta semantics. |
| 2026-07-29 | Decompressed and parsed the small root-level dictionary XML files from the current data ZIP. | Adds partial XML-payload evidence for reference/type dictionaries while regional payload, national row counts and full/delta semantics remain blockers. |

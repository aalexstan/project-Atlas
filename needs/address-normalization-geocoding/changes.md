# Address Normalization and Geocoding Need Changes

[Русская версия](changes.ru.md)

| Date | Change | Impact |
|---|---|---|
| 2026-07-29 | Initial need-based journey created for address suggestions, cleaning, geocoding, registry integration and procurement decisions. | Adds a user-task entry point for the new Atlas address direction. |
| 2026-07-29 | Added routes for Yandex Geosuggest, 2GIS Suggest, 2GIS Places, Nominatim self-hosting and clarified FIAS/GAR API-service blockers. | Makes the route cover autocomplete, place search, hosted geocoding, open-data self-hosting and official registry choices. |
| 2026-07-29 | Added verified FIAS/GAR open-data ZIP route details while keeping API-service blockers visible. | Helps users separate file-feed integration from REST-like API procurement. |
| 2026-07-29 | Linked Nominatim self-hosting route to a dedicated operations checklist. | Helps users evaluate self-hosting before treating OSM geocoding as a hosted API replacement. |
| 2026-07-29 | Added Yandex Maps Organization Search API to the organization/place search route. | Gives users a Yandex ecosystem option alongside 2GIS Places without treating geocoding as place search. |
| 2026-07-29 | Added LocationIQ Geocoding API to hosted geocoding/autocomplete and open-data route options. | Expands the hosted provider shortlist while keeping storage/caching, batch, SLA, ODbL/legal and benchmark blockers explicit. |
| 2026-07-29 | Updated FIAS/GAR route with second regional sample `87/` and CRC/size validation for sampled entries. | Improves registry-feed evidence while keeping national row counts, remaining regions and full/delta semantics as blockers. |
| 2026-07-29 | Updated FIAS/GAR route with sparse regional sample `82/` and CRC/size validation for sampled entries. | Adds an empty-group edge case for ETL planning while keeping national row counts, remaining regions and full/delta semantics as blockers. |

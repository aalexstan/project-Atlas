# Nominatim Geocoder Software Changes

[Русская версия](changes.ru.md)

| Date | Change | Evidence |
|---|---|---|
| 2026-08-24 | Added explicit capability evidence: direct geocoding is observed by the live-test, while reverse geocoding remains documented-only. Profile-level live validity metadata remains unset. | [`api.json`](api.json), [`evidence.md`](evidence.md) |
| 2026-08-24 | Added the first policy-compliant public-instance live-test with raw JSON, attribution/licence observations and paired review. Validity metadata remains unset pending human review. | [`live-test-2026-08-24.md`](../../research/nominatim-geocoder-software/live-test-2026-08-24.md) |
| 2026-07-29 | Created reviewed API-first profile for Nominatim as open-source geocoder software. | [`evidence.md`](evidence.md) |
| 2026-07-29 | Added self-hosting operations details for software prerequisites, import sizing, update modes and production deployment. | [`evidence.md`](evidence.md) |

## Monitoring Notes

- Recheck public usage policy before recommending public-service usage.
- Recheck Nominatim release documentation for import/update requirements.
- Add third-party provider profiles only after official provider-specific research.

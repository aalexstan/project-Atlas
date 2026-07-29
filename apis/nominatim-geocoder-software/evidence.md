# Nominatim Geocoder Software Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| The public usage policy applies to `nominatim.openstreetmap.org` and not to self-hosted or other organizations' services. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Critical product boundary. |
| Public Nominatim has limited capacity and an absolute maximum of 1 request/second. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Not suitable for heavy production use. |
| Public usage requires valid Referer or User-Agent and attribution. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Client identification requirement. |
| Public usage policy forbids autocomplete search. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Must not be used for autocomplete UX. |
| Public policy discourages bulk geocoding and imposes stricter rules for long-running/regular scripts. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Bulk blocker. |
| Primary geocoding applications and API resellers must run their own service. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Production/resale blocker. |
| Search API supports free-form and structured queries. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Search capability. |
| Search endpoint format is `https://nominatim.openstreetmap.org/search?<params>`. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Public endpoint format. |
| Search output formats include XML, JSON, JSONv2, GeoJSON and GeocodeJSON; `limit` defaults to 10 and cannot exceed 40. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Response and limit detail. |
| Reverse geocoding returns a closest suitable OSM object and may produce unexpected results. | https://nominatim.org/release-docs/latest/api/Reverse/ | 2026-07-29 | verified | Quality caveat. |
| Reverse endpoint format is `https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>`. | https://nominatim.org/release-docs/latest/api/Reverse/ | 2026-07-29 | verified | Public endpoint format. |
| OpenStreetMap data is licensed under ODbL and requires attribution. | https://www.openstreetmap.org/copyright | 2026-07-29 | verified | Legal/data-rights blocker. |
| Self-hosting requires importing OSM planet or extracts and operating updates. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Operations route. |
| Update documentation describes replication-based update processes. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Ongoing operations requirement. |

## Live Testing

No Atlas live test, import or benchmark was performed.

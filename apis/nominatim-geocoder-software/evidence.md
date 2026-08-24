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
| Nominatim requires PostgreSQL, PostGIS, osm2pgsql and Python; pyosmium is needed for continuous updates and a Python frontend requires additional framework packages. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Software operations requirement. |
| Full-planet installation needs at least 1TB disk, fast disks/NVMe recommended, and 128GB+ RAM is strongly recommended for full planet import. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Capacity-planning warning. |
| Large imports should use flatnode storage; flatnode file needs at least 75GB free space. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Import planning. |
| Full-planet default setup can be reduced with extracts; import styles include `admin`, `street`, `address`, `full` and `extratags`. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Scope and cost trade-off. |
| Import docs provide rough 2020 planet estimates on 64GB RAM / 4 CPU / NVMe, including `address` at 36h/545GB and `full` at 54h/640GB before drop. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | provider_reported | Planning estimate, not Atlas benchmark. |
| Self-hosting requires importing OSM planet or extracts and operating updates. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Operations route. |
| Update documentation describes replication-based update processes. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Ongoing operations requirement. |
| Continuous update mode is no longer recommended; documentation recommends systemd-managed regular updates. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Update operations design. |
| Production deployment docs describe a Python ASGI frontend with Falcon or Starlette, gunicorn, systemd and nginx; import docs say the test server must not be used in production. | https://nominatim.org/release-docs/latest/admin/Deployment-Python/ | 2026-07-29 | verified | Deployment boundary. |

## Live Testing

The [2026-08-24 bounded public-instance live-test](../../research/nominatim-geocoder-software/live-test-2026-08-24.md) tested three policy-compliant individual direct-geocoding requests. Raw responses exposed OpenStreetMap attribution and ODbL signals; the unknown query returned an empty result. `capability_evidence.direct_geocoding.live_test` is `observed`; `reverse_geocoding` was not tested and remains documented-only. Profile-level `live_tested` remains `false` until human review sets the validity dates. No import or benchmark was performed.

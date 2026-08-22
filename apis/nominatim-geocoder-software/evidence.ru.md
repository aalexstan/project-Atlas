# Evidence Nominatim Geocoder Software

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| Public usage policy применяется к `nominatim.openstreetmap.org`, но не к self-hosted или сервисам других организаций. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Критичная граница продукта. |
| Public Nominatim имеет limited capacity и абсолютный максимум 1 request/second. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Не подходит для тяжелого production use. |
| Public usage требует валидный Referer или User-Agent и attribution. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Требование идентификации клиента. |
| Public usage policy запрещает autocomplete search. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Нельзя использовать для autocomplete UX. |
| Public policy discourages bulk geocoding и вводит более строгие правила для long-running/regular scripts. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Bulk blocker. |
| Primary geocoding applications и API resellers должны запускать own service. | https://operations.osmfoundation.org/policies/nominatim/ | 2026-07-29 | verified | Production/resale blocker. |
| Search API поддерживает free-form и structured queries. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Search capability. |
| Search endpoint format: `https://nominatim.openstreetmap.org/search?<params>`. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Public endpoint format. |
| Search output formats включают XML, JSON, JSONv2, GeoJSON и GeocodeJSON; `limit` default 10 и не больше 40. | https://nominatim.org/release-docs/latest/api/Search/ | 2026-07-29 | verified | Response and limit detail. |
| Reverse geocoding возвращает ближайший подходящий OSM object и может давать неожиданные результаты. | https://nominatim.org/release-docs/latest/api/Reverse/ | 2026-07-29 | verified | Quality caveat. |
| Reverse endpoint format: `https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>`. | https://nominatim.org/release-docs/latest/api/Reverse/ | 2026-07-29 | verified | Public endpoint format. |
| OpenStreetMap data лицензирована ODbL и требует attribution. | https://www.openstreetmap.org/copyright | 2026-07-29 | verified | Legal/data-rights blocker. |
| Nominatim требует PostgreSQL, PostGIS, osm2pgsql и Python; для continuous updates нужен pyosmium, а для Python frontend — дополнительные framework packages. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Software operations requirement. |
| Full-planet installation требует at least 1TB disk, fast disks/NVMe recommended, and 128GB+ RAM strongly recommended для full planet import. | https://nominatim.org/release-docs/latest/admin/Installation/ | 2026-07-29 | verified | Capacity-planning warning. |
| Large imports should use flatnode storage; flatnode file needs at least 75GB free space. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Import planning. |
| Full-planet default setup можно уменьшить extracts; import styles включают `admin`, `street`, `address`, `full` и `extratags`. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Scope and cost trade-off. |
| Import docs дают rough 2020 planet estimates на 64GB RAM / 4 CPU / NVMe, включая `address` at 36h/545GB и `full` at 54h/640GB before drop. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | provider_reported | Planning estimate, не Atlas benchmark. |
| Self-hosting требует импортировать OSM planet или extracts и обслуживать updates. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Operations route. |
| Update documentation описывает replication-based update processes. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Требование ongoing operations. |
| Continuous update mode больше не рекомендуется; документация рекомендует systemd-managed regular updates. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Update operations design. |
| Production deployment docs описывают Python ASGI frontend with Falcon or Starlette, gunicorn, systemd and nginx; import docs говорят, что test server нельзя использовать в production. | https://nominatim.org/release-docs/latest/admin/Deployment-Python/ | 2026-07-29 | verified | Deployment boundary. |

## Live Testing

Atlas не проводил live test, import или benchmark.

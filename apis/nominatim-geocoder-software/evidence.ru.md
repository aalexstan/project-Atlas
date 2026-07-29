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
| Self-hosting требует импортировать OSM planet или extracts и обслуживать updates. | https://nominatim.org/release-docs/latest/admin/Import/ | 2026-07-29 | verified | Operations route. |
| Update documentation описывает replication-based update processes. | https://nominatim.org/release-docs/latest/admin/Update/ | 2026-07-29 | verified | Требование ongoing operations. |

## Live Testing

Atlas не проводил live test, import или benchmark.

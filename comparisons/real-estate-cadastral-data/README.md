# Real-estate and Cadastral Data Routes

[Русская версия](README.ru.md)

## Quick Choice

| Need | Start with | Why | Main risk |
|---|---|---|---|
| Legally significant property evidence | EGRN extract | Official registry output | Access grounds and current fee depend on request |
| Repeated official extracts | FGIS EGRN package access | Official package model exists | Unattended integration and current terms need confirmation |
| Map and territory context | NSPD | Official spatial-data route | Not an unrestricted production API by default |
| Normalize an address or enrich it with a cadastral number | DaData Address API | Documented commercial integration | Not an official EGRN extract |
| Build an address registry | FIAS/GAR | Official address provenance | Requires ETL; contains addresses, not property rights |

## Important Boundaries

- An address is not a property-right record.
- A cadastral number returned by enrichment is not an official extract.
- A cadastral map is not legal evidence.
- Machine-readable JSON/XML does not automatically permit bulk reuse.
- Public frontend endpoints are not stable APIs without official documentation.

There is no universal winner. Choose the legal output first, then automation, volume, latency and reuse rights.

See the [need route](../../needs/real-estate-cadastral-data/README.md), [procurement checklist](../../procurement/real-estate-cadastral-data-selection/README.md) and [comparison data](comparison.json).

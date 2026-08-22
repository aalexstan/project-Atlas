# Routing and Logistics APIs

[Русская версия](README.ru.md)

## Purpose

This comparison separates route calculation, distance matrices and logistics planning. Geocoding, places, map tiles and routing are different procurement decisions.

## Quick decision

| Scenario | Initial shortlist | Main reason | Main risk |
|---|---|---|---|
| Point-to-point route | Yandex Maps, 2GIS, OSRM | All document route services | Coverage, traffic and rights need testing |
| Distance matrix / ETA | Yandex Maps, 2GIS, OSRM | Matrix or multiple-pair capabilities | Size limits and ETA semantics are not yet comparable |
| 2GIS deployment in a closed contour | 2GIS Routing API | On-premise option is documented | Contract, infrastructure and SLA scope |
| Own routing infrastructure | OSRM | Self-hosted engine and operator control | OSM import, updates, licensing and operations |
| Delivery optimization | Separate Yandex Routing or 2GIS Route Planner scope | Route calculation alone is not optimization | Product boundary and commercial quote |

## Recommendation

There is no universal winner. Select by route type, geography, traffic needs, matrix size, vehicle constraints, deployment model and rights to store or display results. Use the [procurement kit](../../procurement/routing-api-selection/README.md) before making a commercial choice.

See the [evidence](evidence.md) and [comparison data](comparison.json).


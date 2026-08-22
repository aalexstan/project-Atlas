# Routing and Logistics

[Русская версия](README.ru.md)

## The user question

Which API or engine should we choose for route calculation, distance matrices, ETA and logistics planning?

## Who this route is for

Teams building delivery, field-service, fleet, maps or location-aware products. Start here when the coordinates or addresses are already known. Use the address route first when they are not.

## Quick paths

| Scenario | Initial shortlist | Main caveat |
|---|---|---|
| Route between points | Yandex Maps, 2GIS, OSRM | Coverage, traffic, limits and rights need testing |
| Distance matrix | Yandex Maps, 2GIS, OSRM | Matrix size and ETA semantics differ |
| Closed contour | 2GIS on-premise or OSRM | Infrastructure and contract ownership |
| Delivery optimization | Separate Yandex Routing or 2GIS Route Planner scope | Basic routing is not an optimizer |

## Constraints

Atlas has not run credentialed live tests. Pricing, production limits, SLA, traffic behavior, truck restrictions and storage/display rights remain open questions.

Continue with the [comparison](../../comparisons/routing-logistics-apis/README.md), [API index](../../API_INDEX.md) and [procurement kit](../../procurement/routing-api-selection/README.md).


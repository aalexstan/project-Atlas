# Delivery Order and Shipment Tracking APIs

[Русская версия](README.ru.md)

| Scenario | Initial API | Why | Caveat |
|---|---|---|---|
| Track a Russian Post item | Russian Post Tracking API | Official operation history | It does not create shipments |
| Create and manage Yandex delivery | Yandex Delivery API | Order lifecycle and status operations | It is not multi-carrier tracking |
| Track several carriers | Research another product class | Aggregation is a different job | No active Atlas profile yet |

Do not compare carrier tracking, courier dispatch and routing as if they were the same API. See [comparison data](comparison.json) and the [procurement kit](../../procurement/delivery-api-selection/README.md).


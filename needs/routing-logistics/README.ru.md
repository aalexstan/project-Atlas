# Маршрутизация и логистический расчёт

[English version](README.md)

## Вопрос пользователя

Какой API или движок выбрать для расчёта маршрута, матриц расстояний, ETA и логистического планирования?

## Для кого маршрут

Для команд, создающих delivery, field-service, fleet, maps или location-aware продукты. Начинайте здесь, если координаты или адреса уже известны. Если адреса ещё нужно распознавать, сначала используйте адресный маршрут.

## Быстрые пути

| Сценарий | Первичный shortlist | Главная оговорка |
|---|---|---|
| Маршрут между точками | Yandex Maps, 2GIS, OSRM | Покрытие, traffic, лимиты и права нужно тестировать |
| Матрица расстояний | Yandex Maps, 2GIS, OSRM | Размер матрицы и семантика ETA различаются |
| Закрытый контур | 2GIS on-premise или OSRM | Владение инфраструктурой и договором |
| Оптимизация доставки | Отдельный scope Yandex Routing или 2GIS Route Planner | Базовая маршрутизация не является optimizer |

## Ограничения

Atlas не проводил credentialed live testing. Цены, production limits, SLA, traffic behavior, ограничения для грузовиков и права хранения/показа остаются открытыми вопросами.

Продолжайте с [comparison](../../comparisons/routing-logistics-apis/README.ru.md), [API index](../../API_INDEX.ru.md) и [procurement kit](../../procurement/routing-api-selection/README.ru.md).


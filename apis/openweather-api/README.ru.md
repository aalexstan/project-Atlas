# API OpenWeather

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-22 |
| Класс продукта | Commercial weather data platform |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** глобальной текущей погоды/forecast и широкого набора historical, environmental и timeline products.

**Не подходит без уточнения, если:** нужна одна общая цена или лицензия для всех продуктов OpenWeather.

**Итог:** у OpenWeather несколько коммерческих product/licence paths. One Call 4.0 pay-as-you-call нужно отделять от остальных subscriptions.

## Технический доступ

| Поле | Значение |
|---|---|
| One Call 4.0 | Timeline product с current/forecast, historical и другими endpoint |
| Формат | REST/JSON документирован |
| Аутентификация | API key |
| Охват | В product docs заявлен global lat/lon route |
| Тарифная модель | Subscription и pay-as-you-call |
| Free allowance | На странице One Call 4.0 указано 1 000 calls/day до платного overage |

## Рекомендация

Использовать OpenWeather, когда выбранный product, quota и licence подходят workload. Сравнивать нужно One Call 4.0, а не весь каталог OpenWeather. Подтвердить storage, customer display, derived data и redistribution rights.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/weather/2026-08-22-openweather.ru.md).

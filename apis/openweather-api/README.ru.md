# API OpenWeather

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-24 |
| Класс продукта | Commercial weather data platform |
| Live testing | Ограниченный тест проведён; см. evidence |

## Краткий вывод

**Подходит для:** глобальной текущей погоды/forecast и широкого набора historical, environmental и timeline products.

**Не подходит без уточнения, если:** нужна одна общая цена или лицензия для всех продуктов OpenWeather.

**Итог:** у OpenWeather несколько коммерческих product/licence paths. Current/forecast API 2.5 и One Call API 3.0 нужно отделять как разные продуктовые и подписочные пути.

## Технический доступ

| Поле | Значение |
|---|---|
| Current/forecast API 2.5 | Current weather и five-day/three-hour forecast; доступ проверен валидным key |
| One Call API 3.0 | Отдельный продукт; проверенный key получил ответ о необходимости подписки |
| Формат | REST/JSON документирован |
| Аутентификация | API key |
| Охват | В product docs заявлен global lat/lon route |
| Тарифная модель | Subscription и pay-as-you-call |
| Free allowance | Зависит от продукта; One Call 3.0 недоступен для проверенного key |

## Рекомендация

Использовать OpenWeather, когда выбранный product, quota и licence подходят workload. Сравнивать нужно выбранный current/forecast API или One Call API 3.0, а не весь каталог OpenWeather. Подтвердить storage, customer display, derived data и redistribution rights.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/weather/2026-08-22-openweather.ru.md).

См. [live-test от 2026-08-24](../../research/weather/openweather-live-test-2026-08-24.ru.md) и [процедурное ревью](../../reviews/openweather-live-test-2026-08-24.ru.md). Maturity остаётся `reviewed`.

# API Open-Meteo

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-22 |
| Класс продукта | Open-data/model weather API |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** некоммерческой оценки, прототипов, model-based forecast и исследования исторической погоды.

**Не подходит без коммерческого плана, если:** production-сервису нужна гарантированная доступность бесплатного endpoint.

**Итог:** Open-Meteo явно разделяет бесплатный некоммерческий endpoint и customer endpoint с коммерческой лицензией.

## Технический доступ

| Поле | Значение |
|---|---|
| Free API | Forecast и связанные coordinate-based endpoints |
| Commercial API | `customer-api.open-meteo.com` с API key |
| Формат | JSON документирован |
| Free limit | 10 000 вызовов/день |
| Historical | Отдельные historical и climate routes |
| Лицензия | Weather data CC BY 4.0; server code AGPLv3 |

## Рекомендация

Использовать free endpoint для оценки и некоммерческих прототипов. Перед коммерческим запуском перейти на customer endpoint и подтвердить attribution/derived-data obligations. Accuracy без benchmark не заявлять.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/weather/2026-08-22-open-meteo.ru.md).

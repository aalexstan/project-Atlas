# Источники данных о закупках и тендерах

[English version](README.md)

## Назначение

Сравнение разделяет официальный информационный маршрут закупок и коммерческий агрегированный API. Это не рейтинг поставщиков.

| Сценарий | Первичный маршрут | Почему | Главный риск |
|---|---|---|---|
| Первичная provenance и собственная база | Интеграция ЕИС | Официальный источник и маршрут форматов взаимодействия | Текущий machine interface и права нужно подтвердить |
| Фильтрованный поиск тендеров в CRM | Seldon.Tenders API | Поставщик описывает фильтры и интеграцию с CRM | Endpoint, schema, coverage и цена неизвестны |
| Коммерческий выбор | Оба маршрута через RFP | Решают разные задачи | Нет общего benchmark, quotes и legal review |

См. [need route](../../needs/procurement-tender/README.ru.md), [данные comparison](comparison.json) и [procurement kit](../../procurement/procurement-api-selection/README.ru.md).


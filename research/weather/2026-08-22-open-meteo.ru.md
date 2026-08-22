# Исследование Open-Meteo

[English version](2026-08-22-open-meteo.md)

## Область проверки

Проверка forecast, historical, climate API и границ коммерческого использования Open-Meteo.

## Подтверждённые факты

- Open-Meteo документирует forecast и historical API по координатам.
- Бесплатный API описан как некоммерческий, с лимитом 10 000 вызовов в день и без гарантии uptime.
- Отдельно описан customer endpoint с API key и коммерческой лицензией.
- Historical, climate, ensemble и satellite radiation API требуют более высоких коммерческих планов.
- Weather data заявлены под CC BY 4.0, server code — AGPLv3.

## Неизвестные параметры

- Актуальная цена плана, support response, freshness в нужном регионе и пригодность модели.
- Accuracy, station observations против model output и legal treatment derived datasets.

## Live testing

Не проводился.

## Решение

Создать reviewed профиль, явно разделив бесплатную оценку и коммерческий customer API.

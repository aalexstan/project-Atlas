# Погодные и метеорологические данные

[English version](README.md)

## Вопрос пользователя

Какой API или источник выбрать для текущей погоды, прогнозов, исторических данных, air quality или weather-aware продуктов?

## Быстрый выбор

| Сценарий | Первичный shortlist | Главный риск | Следующий документ |
|---|---|---|---|
| Некоммерческий прототип | Open-Meteo | Free endpoint некоммерческий и без uptime guarantee | [Профиль Open-Meteo](../../apis/open-meteo-api/README.ru.md) |
| Current/forecast/history | WeatherAPI.com | Historical data — forecast archive | [Сравнение](../../comparisons/weather-data-apis/README.ru.md) |
| Global product family | OpenWeather | Нужно точно выбрать product и licence scope | [Профиль OpenWeather](../../apis/openweather-api/README.ru.md) |

## Что проверить до выбора

Подтвердите координаты и timezone, переменные, forecast horizon, actual observations против model output, semantics historical, frequency обновлений, regional coverage, storage, redistribution, derived data, SLA и support.

## Ограничения

Credentials, quality benchmark, latency test и production ingest не проводились. Погодные данные нельзя автоматически использовать для safety-critical, страховых, медицинских или регулируемых решений.

## Следующий шаг

Откройте [сравнение погодных API](../../comparisons/weather-data-apis/README.ru.md), затем отправьте [procurement kit](../../procurement/weather-api-selection/README.ru.md) shortlisted providers.

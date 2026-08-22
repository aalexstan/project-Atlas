# API погодных и метеоданных

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Последняя проверка | 2026-08-22 |
| Кандидаты | Open-Meteo, WeatherAPI.com, OpenWeather |
| Live testing | Не проводился |

## Краткая матрица выбора

| Сценарий | Первичный shortlist | Почему |
|---|---|---|
| Некоммерческий прототип | Open-Meteo | Явный free non-commercial route и open-data model. |
| Широкий self-service weather API | WeatherAPI.com | Публичные планы, current/forecast/history/location и air quality. |
| Глобальный commercial product family | OpenWeather | Несколько current, forecast, historical и environmental продуктов. |

## Матрица

| Критерий | Open-Meteo | WeatherAPI.com | OpenWeather |
|---|---|---|---|
| Current weather | Документирован | Документирован | Документирован |
| Forecast | Документирован | Документирован | Документирован |
| Historical | Historical/model routes | Документирован; forecast archive | Зависит от продукта |
| API key | Customer endpoint | Да | Да |
| Публичная цена | Free non-commercial; paid customer API | Public plans | Product-specific plans |
| Free allowance | 10K calls/day, non-commercial | 100K calls/month free plan | Product-dependent; One Call 4.0 указывает 1K/day |
| Commercial licence | Нужен customer endpoint | План и terms требуют проверки | Зависит от product/plan |
| SLA | Для free tier нет uptime guarantee | В этом исследовании неизвестен | В этом исследовании неизвестен |
| Live test | Не проводился | Не проводился | Не проводился |

Погодные API нельзя сравнивать только по числу forecast days или цене вызова. Нужен benchmark координат, горизонтов, переменных, freshness, actual-vs-model semantics и legal rights.

См. [need-маршрут](../../needs/weather-data/README.ru.md) и [procurement kit](../../procurement/weather-api-selection/README.ru.md).

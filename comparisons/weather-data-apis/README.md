# Weather Data APIs

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-08-22 |
| Candidates | Open-Meteo, WeatherAPI.com, OpenWeather |
| Live testing | Not performed |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Non-commercial prototype | Open-Meteo | Explicit free non-commercial route and open-data model. |
| Broad self-service weather API | WeatherAPI.com | Public plans, current/forecast/history/location and air-quality scope. |
| Global commercial product family | OpenWeather | Multiple current, forecast, historical and environmental product paths. |

## Matrix

| Criterion | Open-Meteo | WeatherAPI.com | OpenWeather |
|---|---|---|---|
| Current weather | Documented | Documented | Documented |
| Forecast | Documented | Documented | Documented |
| Historical | Historical/model routes | Documented; forecast archive | Product-specific |
| API key | Customer endpoint | Yes | Yes |
| Public price | Free non-commercial; paid customer API | Public plans | Product-specific plans |
| Free allowance | 10K calls/day, non-commercial | 100K calls/month free plan | Product-dependent; One Call 4.0 states 1K/day |
| Commercial licence | Customer endpoint required | Plan/terms require review | Product/plan-specific |
| SLA | No free-tier uptime guarantee | Unknown in this review | Unknown in this review |
| Live test | Not performed | Not performed | Not performed |

Do not compare weather APIs on forecast days or call prices alone. Measure the target coordinates, forecast horizons, variables, freshness, actual-vs-model semantics and legal rights.

See the [weather need route](../../needs/weather-data/README.md) and [procurement kit](../../procurement/weather-api-selection/README.md).

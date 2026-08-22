# Weather and Meteorological Data

[Русская версия](README.ru.md)

## The user question

Which API or source should we use for current weather, forecasts, historical data, air quality, or weather-aware products?

## Quick choice

| Scenario | Initial shortlist | Main risk | Next document |
|---|---|---|---|
| Non-commercial prototype | Open-Meteo | Free endpoint is non-commercial and has no uptime guarantee | [Open-Meteo profile](../../apis/open-meteo-api/README.md) |
| Broad current/forecast/history | WeatherAPI.com | Historical data is forecast archive | [Comparison](../../comparisons/weather-data-apis/README.md) |
| Global product family | OpenWeather | Product and licence scope must be selected | [OpenWeather profile](../../apis/openweather-api/README.md) |

## Before choosing

Confirm coordinates and timezone, variables, forecast horizon, actual observations versus model output, historical semantics, update frequency, regional coverage, storage, redistribution, derived data, SLA and support.

## Limits

No credentials, quality benchmark, latency test, or production ingest was performed. Weather data is not automatically suitable for safety-critical, insurance, medical, or regulated decisions.

## Next step

Use the [weather comparison](../../comparisons/weather-data-apis/README.md), then send the [procurement kit](../../procurement/weather-api-selection/README.md) to shortlisted providers.

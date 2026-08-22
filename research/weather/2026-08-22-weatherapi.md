# WeatherAPI.com Research Log

[Русская версия](2026-08-22-weatherapi.ru.md)

## Scope

Review WeatherAPI.com current, forecast, historical, location, air-quality and related API products.

## Official sources reviewed

- https://www.weatherapi.com/docs/
- https://www.weatherapi.com/pricing.aspx

## Confirmed facts

- WeatherAPI.com documents JSON/XML REST access protected by an API key.
- Official docs describe current weather, forecast, historical weather, future weather, marine, air quality, search/autocomplete, alerts and other products.
- The official pricing page lists public plans, call allowances, historical windows, and forecast horizons.
- The docs state that historical data is an archive of forecast data, not actual observations.

## Unknowns and blockers

- Exact commercial storage, redistribution, SaaS, attribution, SLA and support terms for a target plan.
- Accuracy and station/model composition for a target Russian region.
- Whether a plan's public allowance matches the intended batch and customer-facing workload.

## Live testing

Not performed.

## Decision

Create an active reviewed profile with a clear distinction between provider-reported plan features and independently measured quality.

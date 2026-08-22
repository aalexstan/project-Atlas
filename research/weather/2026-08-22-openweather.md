# OpenWeather Research Log

[Русская версия](2026-08-22-openweather.ru.md)

## Scope

Review OpenWeather current/forecast APIs and One Call 4.0 pay-as-you-call route.

## Official sources reviewed

- https://openweathermap.org/api
- https://openweathermap.org/api/one-call-3
- https://openweathermap.org/price
- https://openweathermap.org/full-price
- https://openweathermap.org/faq

## Confirmed facts

- OpenWeather documents current, forecast, historical, environmental and related API products.
- The official pricing pages distinguish self-service subscriptions from One Call 4.0 pay-as-you-call.
- One Call 4.0 includes a daily free allowance and charges additional calls according to the selected product terms.
- OpenWeather documents API keys and lat/lon-based REST access.
- Official licensing material distinguishes product plans and usage rights; one generic licence assumption cannot be applied to every plan.

## Unknowns and blockers

- Exact current price for a chosen product, rate limits, SLA, storage, redistribution and customer-facing display rights.
- Accuracy and data-source suitability for target Russian regions and historical use.

## Live testing

Not performed.

## Decision

Create an active reviewed profile, keeping One Call 4.0 and legacy/other OpenWeather products distinct.

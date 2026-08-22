# Open-Meteo Research Log

[Русская версия](2026-08-22-open-meteo.ru.md)

## Scope

Review Open-Meteo forecast, historical, climate and commercial-use boundaries.

## Official sources reviewed

- https://open-meteo.com/en/docs
- https://open-meteo.com/en/pricing
- https://open-meteo.com/en/docs/historical-forecast-api

## Confirmed facts

- Open-Meteo documents forecast and historical weather APIs with coordinate-based requests.
- The free API is described as for non-commercial use, rate-limited to 10,000 calls per day, and without uptime guarantee.
- A customer endpoint with API key and commercial-use licence is documented separately.
- Historical, climate, ensemble and satellite radiation APIs require higher commercial plans according to the pricing page.
- Open-Meteo states that weather data is licensed under CC BY 4.0 and the server code is AGPLv3.

## Unknowns and blockers

- Exact plan price at procurement time, support response, data freshness for a target region, and model fitness for a product decision.
- Accuracy, station observations versus model output, and legal treatment of derived datasets require scenario review.

## Live testing

Not performed.

## Decision

Create an active reviewed profile, explicitly separating free evaluation from commercial customer API use.

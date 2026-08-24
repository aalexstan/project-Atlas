# WeatherAPI.com API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-24 |
| Product class | Commercial weather API |
| Live testing | Bounded test performed; see research evidence |

## Quick Verdict

**Best for:** A broad current, forecast, historical, air-quality, location and alert API with public subscription plans.

**Avoid when:** Historical actual observations are mandatory: the provider describes historical data as an archive of forecast data.

## Technical Access

| Field | Value |
|---|---|
| Base URL | `http://api.weatherapi.com/v1` documented; use HTTPS in production review |
| Format | JSON/XML |
| Authentication | API key |
| Capabilities | Current, forecast, history, future, marine, air quality, autocomplete and more |
| Public plans | Free, Starter, Pro+, Business, Enterprise |
| Free plan | 100K calls/month, 3-day forecast, 1-day history according to pricing page |

## Pricing Note

The official pricing page lists public plan prices and allowances. These are provider plan prices, not a guarantee of total cost for storage, bandwidth, redistribution, support or custom workload.

## Recommendation

Use for broad API coverage and public self-service onboarding. Confirm historical semantics, commercial rights, SLA and regional quality before using it for insurance, logistics or regulated decisions.

See [evidence](evidence.md) and the [research log](../../research/weather/2026-08-22-weatherapi.md).

See the [2026-08-24 live-test record](../../research/weatherapi-com-api/live-test-2026-08-24.md) and its [procedural review](../../reviews/weatherapi-com-live-test-2026-08-24.md). The test kept maturity at `reviewed`; quotas, SLA, pricing, accuracy and data rights remain unverified.

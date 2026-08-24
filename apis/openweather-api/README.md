# OpenWeather API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-24 |
| Product class | Commercial weather data platform |
| Live testing | Bounded test performed; see research evidence |

## Quick Verdict

**Best for:** Global current/forecast weather and a broad family of historical, environmental and timeline products.

**Avoid when:** A single generic price or licence assumption is needed across all OpenWeather products.

**Bottom line:** OpenWeather has multiple commercial product and licence paths. Current/forecast API 2.5 access and One Call API 3.0 must be treated as separate product and subscription paths.

## Technical Access

| Field | Value |
|---|---|
| Current/forecast API 2.5 | Current weather and five-day/three-hour forecast endpoints tested with a valid key |
| One Call API 3.0 | Separate product; the tested key received a subscription-required response |
| Format | REST/JSON documented |
| Authentication | API key |
| Coverage | Global lat/lon route claimed in product documentation |
| Pricing | Subscription and pay-as-you-call options |
| Free allowance | Product-specific; One Call 3.0 access was not available under the tested key |

## Recommendation

Use OpenWeather when the chosen product, quota and licence fit the target workload. Compare One Call 4.0, not the whole OpenWeather catalogue, against other weather APIs. Confirm rights for storage, customer display, derived data and redistribution.

See [evidence](evidence.md) and the [research log](../../research/weather/2026-08-22-openweather.md).

See the [2026-08-24 live-test record](../../research/weather/openweather-live-test-2026-08-24.md) and [procedural review](../../reviews/openweather-live-test-2026-08-24.md). Maturity remains `reviewed`.

# Open-Meteo API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-24 |
| Product class | Open-data/model weather API |
| Live testing | Public GET test performed; no credentials used |

## Quick Verdict

**Best for:** Non-commercial evaluation, prototypes, model-based forecasts, and historical weather research.

**Avoid when:** A commercial production service needs guaranteed uptime on the free endpoint.

**Bottom line:** Open-Meteo explicitly separates its free non-commercial endpoint from a paid customer endpoint with a commercial licence.

## Technical Access

| Field | Value |
|---|---|
| Free API | Coordinate-based forecast and related endpoints |
| Commercial API | `customer-api.open-meteo.com` with API key |
| Format | JSON documented |
| Free limit | 10,000 calls/day |
| Historical | Separate historical and climate routes |
| Licence | Weather data CC BY 4.0; server code AGPLv3 |

## Recommendation

Use the free endpoint for evaluation and non-commercial prototypes. Use the customer endpoint and confirm attribution/derived-data obligations before commercial launch. Do not claim measured accuracy without a benchmark.

See [evidence](evidence.md), the [raw live-test evidence](../../research/open-meteo-api/live-test-2026-08-24.md) and the [research log](../../research/weather/2026-08-22-open-meteo.md).

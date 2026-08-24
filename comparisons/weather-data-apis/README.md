# Weather Data APIs

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-08-24 |
| Candidates | Open-Meteo, WeatherAPI.com, OpenWeather |
| Live testing | Bounded tests performed for all three candidates; see evidence status below |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Non-commercial prototype | Open-Meteo | Explicit free non-commercial route and open-data model. |
| Broad self-service weather API | WeatherAPI.com | Public plans, current/forecast/history/location and air-quality scope. |
| Global commercial product family | OpenWeather | Multiple current, forecast, historical and environmental product paths. |

## Matrix

| Criterion | Open-Meteo | WeatherAPI.com | OpenWeather |
|---|---|---|---|
| Current weather | **Observed 2026-08-24**: public forecast response returned current fields ([raw evidence](../../research/open-meteo-api/live-test-2026-08-24.md)) | **Observed 2026-08-24**: HTTP 200 JSON with Moscow current data ([raw evidence](../../research/weatherapi-com-api/live-test-2026-08-24.md)) | **Observed 2026-08-24**: HTTP 200 JSON with Moscow current data ([raw evidence](../../research/weather/openweather-live-test-2026-08-24.md)) |
| Forecast | **Observed 2026-08-24**: coordinate forecast JSON | **Observed 2026-08-24**: `days=3` returned three forecast days | **Observed 2026-08-24**: 40 three-hour forecast entries |
| Historical | **Observed 2026-08-24**: archive route returned historical JSON | **Provider-reported**: historical data is forecast archive; not live-tested | **Unknown**: no historical route tested |
| Search/geocoding | **Observed 2026-08-24**: geocoding lookup returned Moscow | **Observed 2026-08-24**: search returned two Moscow results | **Unknown**: not part of this live-test |
| API key | **Observed**: tested public routes worked without a key | **Observed 2026-08-24**: authorized key accepted | **Observed 2026-08-24**: authorized key accepted for API 2.5 |
| Invalid input | **Observed 2026-08-24**: HTTP 400 JSON error for invalid coordinates | **Observed 2026-08-24**: HTTP 400 code 1003 for missing `q`; unknown-looking text resolved to an unrelated location, an open accuracy finding | **Observed 2026-08-24**: HTTP 400 `wrong latitude` |
| Public price | **Provider-reported**: free non-commercial; paid customer API | **Provider-reported**: public plans | **Provider-reported**: product-specific plans |
| Free allowance | **Provider-reported**: 10K calls/day, non-commercial | **Provider-reported**: 100K calls/month free plan | **Unknown/provider-reported**: current/forecast and One Call allowances differ by product |
| Commercial licence | **Provider-reported**: customer endpoint required | **Unknown/provider-reported**: plan/terms require review | **Unknown/provider-reported**: product/plan-specific |
| SLA | **Unknown**: no free-tier uptime guarantee was not tested as SLA | **Unknown** in this review | **Unknown** in this review |
| Rate limits | **Unknown/provider-reported**: no 429 in bounded test | **Unknown/provider-reported**: no 429 in bounded test | **Unknown/provider-reported**: no 429 in bounded test |
| One Call / timeline access | **Not applicable** | **Not applicable** | **Observed 2026-08-24**: One Call API 3.0 returned subscription-required HTTP 401 |
| Evidence status | [Observed live-test](../../research/open-meteo-api/live-test-2026-08-24.md); reported/unknown commercial claims remain separate | [Observed live-test](../../research/weatherapi-com-api/live-test-2026-08-24.md); `current_fields` behavior remains open | [Observed live-test](../../research/weather/openweather-live-test-2026-08-24.md); One Call 3.0 access is subscription-blocked |

Evidence rule: `Observed 2026-08-24` means only that the linked request shape and response behavior were seen in the repository live-test. `Provider-reported` means the claim comes from official documentation or pricing. `Unknown` means it was not established. Do not promote an observed endpoint test into proof of quota, SLA, accuracy, pricing, licence or production suitability.

Do not compare weather APIs on forecast days or call prices alone. Measure the target coordinates, forecast horizons, variables, freshness, actual-vs-model semantics and legal rights.

See the [weather need route](../../needs/weather-data/README.md) and [procurement kit](../../procurement/weather-api-selection/README.md).

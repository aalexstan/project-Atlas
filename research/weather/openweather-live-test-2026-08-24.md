# OpenWeather API Live Test - 2026-08-24

[Russian version](openweather-live-test-2026-08-24.ru.md)

## Purpose

Test the bounded OpenWeather current/forecast API access available to the user-provided key and separately record the One Call API 3.0 subscription boundary. This is not a test of quota, SLA, accuracy or licensing.

## Authorization and safety

- The key was supplied by the user and is not recorded in this repository.
- No paid credential or production secret was added to Atlas.
- The formal series below uses safe GET requests only; no quota exhaustion or load test is attempted.
- Official OpenWeather documentation, pricing and FAQ were reviewed before testing.

## Pre-test core claims

This list was frozen before the formal request series.

| ID | Core claim | Profile reference | Why core |
|---|---|---|---|
| C1 | OpenWeather exposes current and forecast weather data through JSON API endpoints authenticated by an API key. | `api.json` `authentication`, `best_for`, `sources` | Identity and primary purpose |
| C2 | Valid coordinate requests return structured JSON with location-independent weather fields. | `api.json` `sources`; official current/forecast docs | Primary response contract |
| C3 | Missing or malformed coordinate input returns a structured error rather than a valid weather result. | `api.json` `open_questions` | Integration safety |
| C4 | One Call API 3.0 is a separate product/subscription boundary from current/forecast access. | `api.json` `best_for`, `pricing`; official One Call 3.0 page | Commercial/access block |
| C5 | Quota, rate limits, SLA, pricing, accuracy, storage and licensing remain provider-reported or unknown unless separately confirmed. | `api.json` `pricing`, `rate_limits`, `open_questions` | Procurement block |

## Test environment

- Date: 2026-08-24
- Client: `curl --silent --show-error --max-time 20`
- Coordinates: Moscow, `55.75, 37.62`
- Raw payloads: [openweather-live-test-2026-08-24-raw](openweather-live-test-2026-08-24-raw/)
- The key is redacted from every request shape.

## Formal requests

### 1. Current weather

`GET https://api.openweathermap.org/data/2.5/weather?lat=55.75&lon=37.62&appid=<redacted>&units=metric`

Observed: HTTP `200`, `0.323996 s`, city `Moscow`, country `RU`. Structured JSON contained `coord`, `weather`, `main`, `wind`, `clouds`, `sys` and related fields.

Raw payload: [current.json](openweather-live-test-2026-08-24-raw/current.json)

### 2. Five-day forecast endpoint

`GET https://api.openweathermap.org/data/2.5/forecast?lat=55.75&lon=37.62&appid=<redacted>&units=metric`

Observed: HTTP `200`, `0.453430 s`, city `Moscow`, and `40` three-hour forecast entries in JSON.

Raw payload: [forecast.json](openweather-live-test-2026-08-24-raw/forecast.json)

### 3. Invalid coordinate input

`GET https://api.openweathermap.org/data/2.5/weather?lat=not-a-number&lon=37.62&appid=<redacted>&units=metric`

Observed: HTTP `400`, `0.905995 s`, JSON error message `wrong latitude`.

Raw payload: [invalid-coordinate.json](openweather-live-test-2026-08-24-raw/invalid-coordinate.json)

## One Call API 3.0 boundary probe

`GET https://api.openweathermap.org/data/3.0/onecall?lat=55.75&lon=37.62&appid=<redacted>&units=metric&exclude=minutely,alerts`

Observed: HTTP `401`, `0.171492 s`, structured message: using One Call 3.0 requires a separate subscription to the One Call by Call plan. This is an access/product-boundary finding, not evidence that the API key is invalid: the same key returned HTTP 200 on current weather.

Raw payload: [onecall-3-boundary.json](openweather-live-test-2026-08-24-raw/onecall-3-boundary.json)

## Rate-limit observation

The bounded requests did not intentionally approach a quota. No `429` or `Retry-After` response was used to infer a limit. Quota, rate limits, SLA, accuracy, pricing and licensing remain unknown or provider-reported.

## Decision

The key is valid for the tested current-weather endpoint. One Call API 3.0 is not available under the current access because it requires a separate subscription. The profile must keep current/forecast access and One Call 3.0 as separate product paths.

Keep maturity at `reviewed`; live evidence does not promote the profile to `verified`. The evidence is valid until `2026-11-22` under the 90-day access/limits cadence.

See the [procedural review](../../reviews/openweather-live-test-2026-08-24.md).

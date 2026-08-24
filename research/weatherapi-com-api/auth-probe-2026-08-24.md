# WeatherAPI.com Credential-Free Auth Probe — 2026-08-24

[Русская версия](auth-probe-2026-08-24.ru.md)

## Purpose

Confirm the authentication boundary without registering an account, using a key, invoking paid methods or attempting to bypass access controls.

## Official sources reviewed

- [WeatherAPI.com API documentation](https://www.weatherapi.com/docs/)
- [WeatherAPI.com pricing](https://www.weatherapi.com/pricing.aspx)
- [WeatherAPI.com API terms](https://www.weatherapi.com/terms.aspx)
- [WeatherAPI.com signup](https://www.weatherapi.com/signup.aspx)

## Legal and safety boundary

- No account was created.
- No paid credential or production token was used.
- Two user-provided candidate keys were tested once each; their values are intentionally not recorded.
- The requests were safe GETs for the documented current-weather endpoint and were not repeated as a load test.
- This remains an authentication probe, not a live-test record and not evidence of valid forecast behavior.

## Probe

Credential-free request:

`GET https://api.weatherapi.com/v1/current.json?q=Moscow`

Observed: HTTP `401`, `0.176436 s`.

Raw payload:

```json
{"error":{"code":1002,"message":"API key is invalid or not provided."}}
```

## User-provided credential probes

The two values supplied by the user were tested once each. They are identified only as `key_a` and `key_b`; the values are not stored in Atlas.

| Probe | Request shape | HTTP | Time | Response |
|---|---|---:|---:|---|
| `key_a` | `GET https://api.weatherapi.com/v1/current.json?key=<redacted>&q=Moscow` | 401 | 0.181132 s | error code `2006`, `API key is invalid.` |
| `key_b` | `GET https://api.weatherapi.com/v1/current.json?key=<redacted>&q=Moscow` | 401 | 0.318189 s | error code `2006`, `API key is invalid.` |

The response was a structured JSON authentication error in both probes. The key values were not printed, committed or retained in the repository.

## Finding

The no-key request confirms an auth boundary and a structured JSON error. The two provided values were also rejected as invalid. These probes do not test a valid request, response contract, quota, rate-limit headers, data freshness, accuracy or commercial use.

## Blocker for a full live-test

A valid test requires a currently active key issued to an authorized account. Atlas must not register an account or use a key without the owner's explicit authorization. After lawful access is available, use the live-test template, review the applicable free-tier Terms of Service, freeze diverse core claims, and preserve raw payloads.

`live_tested` remains `false`; maturity remains `reviewed`.

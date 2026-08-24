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
- No API key, paid credential or production token was used.
- The request was a single safe GET without a key.
- This is an authentication probe, not a live-test record and not evidence of valid forecast behavior.

## Probe

Request:

`GET https://api.weatherapi.com/v1/current.json?q=Moscow`

Observed: HTTP `401`, `0.176436 s`.

Raw payload:

```json
{"error":{"code":1002,"message":"API key is invalid or not provided."}}
```

## Finding

The no-key request confirms an auth boundary and a structured JSON error. It does not test a valid request, response contract, quota, rate-limit headers, data freshness, accuracy or commercial use.

## Blocker for a full live-test

A valid test requires a key issued to an authorized account. Atlas must not register an account or use a key without the owner's explicit authorization. After lawful access is available, use the live-test template, review the applicable free-tier Terms of Service, freeze diverse core claims, and preserve raw payloads.

`live_tested` remains `false`; maturity remains `reviewed`.

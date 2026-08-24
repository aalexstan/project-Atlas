# API Live-Test Record — YYYY-MM-DD

[Русская версия](live-test-template.ru.md)

## Purpose

What core factual claims of the API profile are being tested?

## Authorization and safety

- Access basis: public/free endpoint or explicitly authorized test credentials.
- No paid or production credentials without written permission.
- No secrets, personal data, destructive methods or unnecessary load.

## Test environment

- Date and timezone:
- Client and version:
- API version/account scope:
- Test data policy:

## Requests and raw responses

For 3-5 realistic requests, record the exact method and URL, sanitized request body, HTTP code, response headers relevant to limits, response time and raw response payload.

### Request 1 — core success

Request:

Observed:

Raw payload:

```json
{}
```

Repeat for core scenarios.

### Intentional invalid-input request

Record the invalid input, HTTP code, error payload, latency and whether the error is actionable.

## Rate-limit observation

Record whether `429`, `Retry-After`, quota headers or documented limit signals appeared. Do not intentionally exhaust a free quota. State what remains unmeasured.

## Findings against the profile

| Profile claim | Empirical result | Finding |
|---|---|---|
|  |  | confirmed / conflict / not measured |

## Decision

State separately whether `live_tested` may become true and whether maturity remains `reviewed` or may be promoted after human review. Never promote automatically.

## Reproduction

Provide safe commands or pseudocode that can be repeated without secrets, personal data or paid calls.

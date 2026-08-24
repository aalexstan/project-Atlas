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
- Live-test evidence date:
- Live-test valid until:

## Pre-test Core Claims

Freeze this list before executing requests. Give each claim a stable ID and link it to the profile field or evidence row it tests. Do not add or remove claims after seeing results; record any amendment separately.

| ID | Core claim | Profile reference | Why core to the API purpose |
|---|---|---|---|
| C1 |  |  |  |

The frozen list must contain at least one claim in each category: identity/purpose, primary response contract, and commercial/quota/rate-limit/procurement block. A block claim may be explicitly `unknown` if the public test cannot establish it.

## Legal Access and Terms

- Free-tier/test Terms of Service reviewed on:
- Does the applicable ToS permit this automated test and recording of responses?:
- Authorization or public-access basis:
- Restrictions relevant to this test:

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

Record whether `429`, `Retry-After`, quota headers or documented limit signals appeared. Do not intentionally exhaust a free quota. If `429` appears during ordinary testing, preserve it as a finding and do not repeat until a success hides it. State what remains unmeasured.

## Findings against the profile

| Profile claim | Empirical result | Finding |
|---|---|---|
| C1 |  | confirmed / conflict / not measured |

## Decision

State separately whether `live_tested` may become true and whether maturity remains `reviewed` or must be downgraded. Link `reviews/<slug>-live-test-YYYY-MM-DD.md` and its Russian pair. Never promote automatically.

The pre-merge review is procedural and does not count as independent review for Gold.

## Reproduction

Provide safe commands or pseudocode that can be repeated without secrets, personal data or paid calls.

# OpenCage Live-Test Plan — 2026-08-24

[Русская версия](live-test-plan-2026-08-24.ru.md)

This is a pre-registered plan for a future single-request live test. No OpenCage API request was made while preparing this file, and no API key is stored in the repository.

## Discovery Basis

The plan is based on the existing Atlas research and official OpenCage materials:

- [API documentation](https://opencagedata.com/api)
- [Pricing](https://opencagedata.com/pricing)
- [Terms](https://opencagedata.com/terms)
- [Credits and sources](https://opencagedata.com/credits)
- [Privacy](https://opencagedata.com/gdpr)

## Access and Legal Gate

Testing may start only after all of these are recorded in the resulting evidence:

1. A personally registered free-trial key is used; no paid, production, customer or shared credential is used.
2. The accepted free-trial terms permit the planned automated, single-request test and do not prohibit testing or measurement of the documented behavior.
3. The test respects the reviewed free-trial rate and daily allowance and does not test batch, spreadsheet or bulk processing.
4. The account/plan and terms acceptance date are recorded without recording the key, email address or personal data.
5. The test uses synthetic or public addresses and coordinates only.

If the legal gate cannot be confirmed, the test remains blocked and no request is sent.

## Pre-Registered Core Claims

These claims are fixed before testing and must not be narrowed retrospectively.

| Dimension | Claim to test | Evidence boundary |
|---|---|---|
| Identity and purpose | OpenCage exposes a hosted Geocoding API for forward and reverse geocoding; autocomplete/typeahead is a separate Geosearch boundary. | Observe the documented v1 endpoint identity and result behavior; do not infer product quality or coverage. |
| Response contract | An authenticated single request returns documented JSON or GeoJSON fields, including coordinates and result/address data; malformed or unknown input returns the documented error or empty-result shape. | Record status, content type, selected fields, error body and latency. Do not publish the key or full personal request data. |
| Rate-limit and policy | The free trial has the reviewed 1 request/second and daily allowance constraints, and ordinary spaced requests are accepted without intentionally approaching exhaustion. | Record relevant response headers/body and published limits; do not exhaust quota or run parallel/batch traffic. |
| Licensing and attribution | The API response/docs/terms identify source-license and attribution requirements, including OpenStreetMap/ODbL wording where applicable. | Record the exact required notice or a short compliant excerpt. HTTP success does not confirm storage, caching, redistribution or SaaS rights. |

## Planned Requests

Use one request at a time with a conservative delay and no retries that could create load.

1. Forward geocode a public Moscow address.
2. Reverse geocode public coordinates in Moscow.
3. Forward geocode an unknown synthetic string and record empty-result or error behavior.
4. Repeat one valid request with the documented language or response-format option, if the free trial and terms allow it.

Do not test batch, spreadsheet upload, Geosearch autocomplete load, scraping, quota exhaustion or production throughput.

## Recording Rules

For every request, record UTC timestamp, request class without the key, HTTP status, latency, content type, selected response fields, relevant rate-limit headers, attribution/license fields and error shape. Store raw payloads only after redacting credentials, personal data and unnecessary query details.

Classify each result as `observed`, `provider_reported`, `inferred` or `unknown`. Keep pricing, SLA, accuracy, house-level precision, storage, caching, redistribution, resale and SaaS rights as unknown unless the evidence directly answers the claim.

The test must not promote maturity automatically. `live_tested_on` and `live_test_valid_until` may be added only after the human pre-merge review confirms the plan was followed and the findings are materiality-classified.

## Ready State

Status: `blocked_pending_legal_access_and_key`.

Next action after lawful access: execute this exact plan, save raw evidence separately, prepare a paired review file, and compare every result against this pre-registered list.

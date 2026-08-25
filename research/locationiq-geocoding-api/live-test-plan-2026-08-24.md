# LocationIQ Live-Test Plan — 2026-08-24

[Русская версия](live-test-plan-2026-08-24.ru.md)

This is a pre-registered plan for a future single-request live test. No LocationIQ API request was made while preparing this file, and no API key is stored in the repository.

## Discovery Basis

The plan is based on the existing Atlas research and official LocationIQ materials:

- [Forward geocoding](https://docs.locationiq.com/docs/search-forward-geocoding)
- [Reverse geocoding](https://docs.locationiq.com/docs/reverse-geocoding)
- [Autocomplete](https://docs.locationiq.com/docs/autocomplete)
- [API reference](https://api-reference.locationiq.com/)
- [Pricing](https://locationiq.com/pricing)
- [Terms of Service](https://locationiq.com/static/tos.html)

## Access and Legal Gate

Testing may start only after all of these are recorded in the resulting evidence:

1. A personally registered free-tier key is used; no paid, production, customer or shared credential is used.
2. The accepted free-tier terms permit the planned automated, single-request test.
3. The test does not exceed the published plan rate or daily allowance and does not test batch, CSV or bulk processing.
4. The account/plan and terms acceptance date are recorded without recording the key, email address or personal data.
5. The test uses synthetic or public addresses only.

If the legal gate cannot be confirmed, the test remains blocked and no request is sent.

## Pre-Registered Core Claims

These claims are fixed before testing and must not be narrowed retrospectively.

| Dimension | Claim to test | Evidence boundary |
|---|---|---|
| Identity and purpose | LocationIQ exposes a hosted geocoding API for forward and reverse address lookup; autocomplete is a separate capability. | Observe the documented endpoint family and returned result shape; do not infer product quality. |
| Response contract | An authenticated single forward request and a reverse request return documented JSON fields, including coordinates and address/result data; malformed or unknown input returns a documented or stable error/empty-result shape. | Record status, content type, selected fields, error body and latency. Do not publish the key or full personal request data. |
| Rate-limit and policy | The selected free plan has the reviewed request-rate and daily limits, and ordinary spaced requests are accepted without intentionally approaching exhaustion. | Record only response headers/body signals and the published limit; do not perform a quota attack or batch test. |
| Licensing and attribution | The documentation/terms identify the attribution or source-license notice required for returned data, including any LocationIQ and OpenStreetMap/ODbL wording. | Record the exact required notice or a short compliant excerpt. HTTP success does not confirm storage, caching, redistribution or SaaS rights. |

## Planned Requests

Use one request at a time with a conservative delay and no retries that could create load.

1. Forward geocode a public Moscow address.
2. Reverse geocode public coordinates in Moscow.
3. Forward geocode an unknown synthetic string and record empty-result or error behavior.
4. Repeat one valid request with the documented language/format option, if the free plan and terms allow it.

Do not test batch, CSV, autocomplete load, bulk imports, scraping, quota exhaustion or production throughput.

## Recording Rules

For every request, record UTC timestamp, request class without the key, HTTP status, latency, content type, selected response fields, relevant rate-limit headers, attribution/license fields and error shape. Store raw payloads only after redacting credentials, personal data and unnecessary query details.

Classify each result as `observed`, `provider_reported`, `inferred` or `unknown`. Keep pricing, SLA, accuracy, house-level precision, storage, caching, redistribution, resale and SaaS rights as unknown unless the evidence directly answers the claim.

The test must not promote maturity automatically. `live_tested_on` and `live_test_valid_until` may be added only after the human pre-merge review confirms the plan was followed and the findings are materiality-classified.

## Ready State

Status: `blocked_pending_legal_access_and_key`.

Next action after lawful access: execute this exact plan, save raw evidence separately, prepare a paired review file, and compare every result against this pre-registered list.

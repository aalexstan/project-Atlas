# Address and Geocoding API Scorecard

[Русская версия](SCORING.ru.md)

This is a procurement worksheet, not an Atlas Score. Change weights for the scenario and keep unknowns visible.

## Scenario Weights

| Criterion | Address entry | Cleaning | Geocoding | Own registry | Notes |
|---|---:|---:|---:|---:|---|
| Functional fit | 25 | 20 | 20 | 15 | Methods and product boundaries. |
| Data quality | 20 | 25 | 30 | 25 | Match level, false positives, coordinate precision. |
| Official provenance | 5 | 15 | 5 | 30 | GAR/registry fields and traceability. |
| Legal/data rights | 20 | 15 | 20 | 15 | Storage, caching, display, SaaS, redistribution. |
| Cost/TCO | 15 | 15 | 10 | 10 | Include per-record, subscription and engineering cost. |
| Operations | 10 | 5 | 10 | 5 | SLA, support, rate limits, monitoring. |
| Developer experience | 5 | 5 | 5 | 0 | Docs, SDKs, sandbox, errors. |

Weights are starting points, not universal methodology.

## Evidence States

Use:

- `verified` for official source confirmation;
- `observed` for reproducible live tests;
- `provider_reported` for vendor claims not independently tested;
- `inferred` for Atlas reasoning from cited facts;
- `unknown` when evidence is missing;
- `not_applicable` when the criterion does not apply.

## Scorecard Row

| Field | Value |
|---|---|
| Provider / product |  |
| Scenario |  |
| Criterion |  |
| Weight |  |
| Evidence state |  |
| Score | 0-5 or unknown |
| Evidence link |  |
| Risk note |  |
| Next verification step |  |

## Guardrails

- Do not turn this worksheet into a public vendor ranking.
- Do not fill missing values with assumptions.
- Do not mix web-product price with API price.
- Do not score live performance without credentials and saved evidence.
- Do not compare registry data integration against commercial APIs without including engineering TCO.

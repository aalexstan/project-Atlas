# Scorecard для API адресов и геокодирования

[English version](SCORING.md)

Это procurement worksheet, не Atlas Score. Меняйте веса под сценарий и оставляйте unknowns видимыми.

## Scenario weights

| Criterion | Address entry | Cleaning | Geocoding | Own registry | Notes |
|---|---:|---:|---:|---:|---|
| Functional fit | 25 | 20 | 20 | 15 | Methods and product boundaries. |
| Data quality | 20 | 25 | 30 | 25 | Match level, false positives, coordinate precision. |
| Official provenance | 5 | 15 | 5 | 30 | GAR/registry fields and traceability. |
| Legal/data rights | 20 | 15 | 20 | 15 | Storage, caching, display, SaaS, redistribution. |
| Cost/TCO | 15 | 15 | 10 | 10 | Per-record, subscription и engineering cost. |
| Operations | 10 | 5 | 10 | 5 | SLA, support, rate limits, monitoring. |
| Developer experience | 5 | 5 | 5 | 0 | Docs, SDKs, sandbox, errors. |

Веса - starting points, не universal methodology.

## Evidence states

Используйте:

- `verified` для подтверждения официальным источником;
- `observed` для reproducible live tests;
- `provider_reported` для claims поставщика без независимого теста;
- `inferred` для вывода Atlas из cited facts;
- `unknown`, если evidence отсутствует;
- `not_applicable`, если criterion не применим.

## Scorecard row

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

- Не превращайте worksheet в публичный vendor ranking.
- Не заполняйте missing values предположениями.
- Не смешивайте цену web-product с API price.
- Не оценивайте live performance без credentials и сохранённого evidence.
- Не сравнивайте registry data integration с commercial APIs без engineering TCO.

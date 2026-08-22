# Scorecard для API адресов и геокодирования

[English version](SCORING.md)

Это procurement worksheet, не Atlas Score. Меняйте веса под сценарий и оставляйте unknowns видимыми.

## Scenario weights

| Criterion | Address entry | Cleaning | Geocoding | Places | Own registry | Self-hosted OSM | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| Functional fit | 25 | 20 | 20 | 25 | 15 | 15 | Methods and product boundaries. |
| Data quality | 20 | 25 | 30 | 25 | 25 | 25 | Match level, false positives, coordinate precision. |
| Official provenance | 5 | 15 | 5 | 5 | 30 | 5 | GAR/registry fields and traceability. |
| Legal/data rights | 20 | 15 | 20 | 20 | 15 | 20 | Storage, caching, display, SaaS, redistribution, ODbL. |
| Cost/TCO | 15 | 15 | 10 | 10 | 10 | 15 | Per-record, subscription, engineering и hosting cost. |
| Operations | 10 | 5 | 10 | 10 | 5 | 15 | SLA, support, rate limits, monitoring, updates. |
| Developer experience | 5 | 5 | 5 | 5 | 0 | 5 | Docs, SDKs, sandbox, errors. |

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
- Не сравнивайте public Nominatim с hosted commercial APIs без применения public usage policy.
- Не оценивайте OSM-derived data без фиксации attribution и license obligations.

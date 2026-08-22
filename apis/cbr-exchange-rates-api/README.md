# Bank of Russia Exchange Rates Web Service

[Русская версия](README.ru.md)

The Bank of Russia publishes official exchange-rate data through public XML web services. This profile covers the daily exchange-rate route and related currency-code resources.

## Research Status

| Field | Value |
|---|---|
| Maturity | Verified |
| Last verified | 2026-08-23 |
| Product class | Official central-bank data web service |
| Protocol | HTTP/HTTPS XML |
| Authentication | Public access; no credential requirement documented for the covered route |
| Live testing | Not performed |

## Best For

- Daily RUB exchange-rate ingestion.
- Financial dashboards, reporting and historical-rate enrichment.
- Prototypes that can consume XML and tolerate a published data-feed style interface.

## Boundaries

This is an official data web service, not a general-purpose market-data API, trading feed or guaranteed real-time quote service. Rate limits, SLA, change policy and commercial redistribution terms are not established in this review.

See [evidence](evidence.md), [research log](../../research/cbr-exchange-rates/2026-08-23.md) and [open questions](changes.md).

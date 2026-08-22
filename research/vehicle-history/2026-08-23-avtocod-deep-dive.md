# Avtocod B2B API deep dive — 2026-08-23

## Scope

Close the initial unknowns around pricing, quotas, report lifecycle, source behavior, support and downstream use. Only official Avtocod documentation and business pages were used.

## Confirmed technical and billing mechanics

- Each report type has daily, monthly and total generation quotas. Reaching a quota returns billing HTTP `402`.
- Report-generation frequency can have an account/report-type limit; exceeding it returns `429 TooManyRequests`. Public universal numeric RPS is not stated.
- A generated report is generally available in the service for six months; report type configuration can set a different `max_age`.
- Reading an existing report does not change the balance and may be repeated without a generation charge.
- Regeneration with `FORCE` is a paid operation.
- Webhooks support `on_update` and `on_complete`, but delivery is explicitly not guaranteed; clients should poll after a timeout.
- A report type fixes its source composition under the contract. Source requests run independently and expose per-source `OK`, `PROGRESS` or `ERROR` state.

## Public business pricing

The official B2B tariff page publishes unit prices for two standard reports offered through business delivery formats including API:

- `Autofill`: 10 RUB/report; individual terms from 10,000 reports; identifiers are excluded.
- `Autofill Plus`: 11 RUB/report; individual terms from 10,000 reports; identifiers are excluded.

The fuller `Vehicle Information` report has volume/format-dependent pricing. Monthly package, package and post-paid subscription models are described; high-volume and individual reports require a quote. These values are B2B report prices, not proof that every API contract uses the same price.

## Sources and quality boundaries

- Avtocod reports data from more than 100 government, commercial and proprietary sources and says new sources are added monthly. This is provider-reported, not an independently audited completeness metric.
- Official pages name example source classes including GIBDD, RSA, MVD, FNS, Rosfinmonitoring, FNP, NBKI, FCS, dealers and service centers.
- Source composition is report-type and contract specific. Per-source statuses make partial/error completion observable, but do not prove correctness or freshness of returned facts.

## Storage, SaaS and high-stakes use

- Six-month server-side report availability is documented. This does not by itself grant customers a right to store, redistribute or resell report contents outside the service.
- Avtocod markets API integration to developers/integrators and solutions for insurance, banking, MFO, leasing, marketplaces and driver scoring. This supports commercial integration as a provider-reported product scenario.
- Public marketing does not replace contractual permission for customer-facing redistribution, automated adverse decisions, model training or regulated scoring.

## SLA and support

- Avtocod states that business customers receive an official contract and ongoing technical/document support.
- No public numerical availability SLA, response-time SLO, support response time or service-credit policy was found.

## Remaining blockers

- Target report composition and source list under contract.
- Contract-specific report prices and numeric rate limit.
- Numerical SLA/support commitments.
- Written rights for local storage, customer display, SaaS embedding, redistribution/resale, automated decisions, scoring and model training.
- Independent benchmark for correctness, freshness, false positives and source-error behavior.

## Live testing

Not performed. No account, token, report generation or billable action was used.

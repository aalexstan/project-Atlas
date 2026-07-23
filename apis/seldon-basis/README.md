# Seldon.Basis API

[Русская версия](README.ru.md)

> Structured company, relationship, procurement, financial, and risk data for internal systems.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-23 |
| Provider | Seldon |
| Status | Active |
| Live test | Not performed |
| Public API price | Not disclosed |
| Free evaluation | Offered |

## Quick Verdict

**Best for:** CRM enrichment, relationship analysis, procurement context, financial/court factors, Russia/CIS, and optional international checks.

**Avoid when:** a minimal self-service company endpoint with public pricing is required.

**Bottom line:** broad method coverage, but individual-plan methods are priced separately. The pilot must model real per-method TCO, not only data quality.

## Capabilities

The official page lists company profiles, owners, subsidiaries, branches, history, licenses, unreliable suppliers, arbitration, bankruptcy, enforcement, public contracts, guarantees, financial statements, monitoring, and relationship-tree exports.

A provider article states JSON responses and a batch operation for up to 1,000 taxpayer IDs. These are labeled provider-reported because no live test or supplied Swagger was used.

## Technical Access

| Field | Value | Status |
|---|---|---|
| Model | Web service for CRM/ERP | verified |
| Format | JSON | provider-reported |
| Batch | Up to 1,000 taxpayer IDs | provider-reported |
| Authentication | Not public | unknown |
| Swagger | Request during onboarding | needs_recheck |
| Test access | Offered | verified |
| Limit | 10,000 requests/day for each individual-plan method | verified |
| SDKs | Public official list not found | unknown |
| Webhooks | Not found | unknown |

## Pricing

Universal Mini/Standard/Maxi packages are based on company counts. Individual plans select methods and term; each method is billed separately and each invocation counts as a request.

**Warning:** Seldon.Basis web pricing is not API pricing.

## Pilot Checks

Validate JSON versioning, branches/history, relationship completeness, source freshness, batch partial errors, batch billing, and identifier stability.

## Strengths

- Broad method catalog.
- Strong relationship/procurement context.
- Enterprise integration is central.
- Free evaluation offered.
- Custom method configuration.
- International coverage advertised.

## Weaknesses

- No public API price.
- Per-method billing complicates TCO.
- Auth and Swagger are not public.
- No public SLA found.
- Freshness claims require sample testing.

## Sources

- https://seldongroup.ru/system/basis/api
- https://seldongroup.ru/functions
- https://seldongroup.ru/kakie-dannye-mozhno-poluchit-cherez-api-seldon-basis
- https://seldongroup.ru/system/basis/worldwide

## Disclosure

No commercial relationship is known. Free access and credentials were not used.

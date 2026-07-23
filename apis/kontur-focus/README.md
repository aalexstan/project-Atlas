# Kontur.Focus API

[Русская версия](README.ru.md)

> Enterprise API integration for counterparty checks, company enrichment, monitoring, and embedded risk controls.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-07-23 |
| Provider | JSC PF SKB Kontur |
| Status | Active |
| Live test | Not performed |
| Public API price | Not found; quotation required |

## Quick Verdict

**Best for:** enterprise supplier/customer screening and risk rules inside CRM, ERP, 1C, or custom systems.

**Avoid when:** a free self-service API with transparent pricing and limits is required.

**Bottom line:** a strong enterprise risk-management candidate. Before procurement, obtain method-level pricing, production limits, SLA, and written storage/redistribution rights.

## What It Does

Official pages describe company-detail enrichment, status checks before payment, custom scoring, monitoring, and integration with CRM, ERP, 1C, SAP, and custom systems. Kontur markets a separate Compliance product for AML/CFT, 115-FZ, and sanctions; do not assume those features are included in a standard Focus API license.

## Technical Access

| Field | Value | Status |
|---|---|---|
| Model | External system calls API | verified |
| Authentication | Developer key | verified in license offer |
| Technical host | `focus-api.kontur.ru` | verified |
| Demo environment | Referenced by provider | verified |
| Response format | Not confirmed from reviewed public pages | unknown |
| OpenAPI/Swagger | Not confirmed | unknown |
| Official SDKs | Public list not found | unknown |
| Rate limits | Not public in reviewed material | unknown |
| Versioning | Not confirmed | unknown |

Full technical documentation was not available without customer access; endpoint and schema details are not presented as verified.

## Pricing

The API license is a separate license type. Its composition is defined by a price list and the fee is fixed in the invoice.

**Warning:** web-version and integration-module prices are not API prices.

## Commercial Questions

Confirm in writing: response storage, retention, affiliate/client display, SaaS embedding, resale, personal data, model training, and subsystem-specific rights.

## Strengths

- Broad risk context beyond company details.
- Designed for enterprise workflows.
- Typical and custom integrations supported.
- API licensing is explicitly defined.
- Broader Kontur ecosystem.

## Weaknesses

- No public API price or standard production limits.
- Full technical contract requires access.
- Licensed data scope is package-dependent.
- Focus, Compliance, and integration modules may use separate terms.

## Open Questions

Pricing, limits, SLA, data rights, versioning, and the Focus/Compliance boundary.

## Alternatives

- **DaData:** faster onboarding and public prices.
- **Seldon.Basis API:** relationships, procurement, and CIS coverage.
- **FTS EGRUL/EGRIP:** primary registry feed for an internal data platform.

## Sources

- https://focus.kontur.ru/site/api
- https://focus.kontur.ru/site/features/api
- https://focus.kontur.ru/site/api/integration
- https://focus.kontur.ru/site/price/license
- https://focus.kontur.ru/

## Disclosure

No commercial relationship is known. No live key or customer demo access was used.

# Company Verification

[Русская версия](README.ru.md)

> Which API or source should we choose for counterparty verification?

This route helps a reader move from the user need to the current Atlas research on Russian company and counterparty data. It does not replace procurement, legal review, or a live test.

## Task Definition

The task is to identify, enrich, or check a legal entity or individual entrepreneur before onboarding, payment, procurement, CRM enrichment, risk monitoring, or internal data-platform work.

## Who This Route Is For

- Product teams adding company autofill or counterparty records.
- Developers choosing an API for CRM, ERP, onboarding, or B2B forms.
- Procurement, finance, legal, or security teams preparing a shortlist.
- Data teams deciding whether to buy an API or build an internal registry warehouse.

## Solutions Already Researched

| Solution | Atlas profile | Role |
|---|---|---|
| DaData API | [Profile](../../apis/dadata/README.md) | Fast company details, suggestions, enrichment, and Russian data entry |
| Kontur.Focus API | [Profile](../../apis/kontur-focus/README.md) | Enterprise counterparty checks, risk controls, and monitoring |
| Seldon.Basis API | [Profile](../../apis/seldon-basis/README.md) | Company, relationship, procurement, financial, and risk context |
| FTS EGRUL/EGRIP integration | [Profile](../../apis/fns-egrul-egrip-integration/README.md) | Official bulk registry feed for an internal data platform |

## Quick Decision Table

| User scenario | Initial shortlist | Why | Main risk | Next Atlas document |
|---|---|---|---|---|
| Fast requisites fill, B2B form, CRM record creation | DaData | Public documentation, public pricing, free start, company lookup by INN/OGRN | Not automatically a deep enterprise risk-analysis platform | [DaData profile](../../apis/dadata/README.md) |
| Corporate checks, risk control, monitoring | Kontur.Focus API; Seldon.Basis API | Both are positioned for broader due diligence and enterprise workflows | No universal winner without quotes, SLA, technical docs, and live testing | [Comparison](../../comparisons/company-counterparty-data-russia/README.md) |
| Relationships, procurement, expanded context | Seldon.Basis API | Atlas comparison identifies relationships, procurement context, CIS coverage, and method configuration as relevant strengths | Method pricing, per-method limits, and batch billing must be checked | [Seldon.Basis profile](../../apis/seldon-basis/README.md) |
| Own full EGRUL/EGRIP database | FTS EGRUL/EGRIP integration | Primary official source with bulk XML archives and daily changes | It is FTP/XML, not REST; ETL and operations dominate total cost | [FTS profile](../../apis/fns-egrul-egrip-integration/README.md) |
| One official extract | FTS electronic extract service | Appropriate for a single signed extract | Not a bulk API and not a complete integration route | [Comparison](../../comparisons/company-counterparty-data-russia/README.md) |
| 115-FZ, sanctions, regulated compliance | Specialized compliance products to evaluate separately | Standard counterparty APIs may not cover the legal requirement completely | Legal scope and product boundary must be verified | [Procurement kit](../../procurement/counterparty-api-selection/README.md) |

## Scenario Routes

### Fast Requisites Fill, B2B Form, CRM

Start with [DaData](../../apis/dadata/README.md) when the need is company lookup, company suggestions, address or contact-data enrichment, and fast self-service integration for a Russian-focused product.

Do not treat this as proof that DaData is the best choice for deep enterprise risk analysis. The current Atlas profile presents DaData as a strong default for data entry and enrichment, not as a complete due-diligence replacement.

### Corporate Checks, Risk Control, Monitoring

Shortlist [Kontur.Focus API](../../apis/kontur-focus/README.md) and [Seldon.Basis API](../../apis/seldon-basis/README.md). Do not declare a winner until the buyer has comparable commercial quotes, SLA terms, technical documentation, production limits, data rights, and a live test on the same sample.

Use the [counterparty comparison](../../comparisons/company-counterparty-data-russia/README.md) and the [procurement kit](../../procurement/counterparty-api-selection/README.md) to structure the pilot.

### Relationships, Procurement, Expanded Context

Evaluate [Seldon.Basis API](../../apis/seldon-basis/README.md) when the need includes relationships, procurement context, financial/court factors, Russia/CIS coverage, or custom method selection.

Before commitment, verify the price for every required method, how each invocation is billed, batch behavior, and whether batch partial failures affect cost or results.

### Own Full EGRUL/EGRIP Database

Use the [FTS EGRUL/EGRIP integration](../../apis/fns-egrul-egrip-integration/README.md) route when the organization needs a primary-source registry warehouse with ETL control.

This is an FTP/XML data feed, not a conventional REST API. It requires downloading archives, parsing versioned XML, applying daily deltas, preserving history, monitoring missing files, and building an internal API or database. Access fees cannot be compared fairly without engineering, infrastructure, legal review, support, monitoring, and operations cost.

### One Official Extract

For a single official extract, the FTS electronic extract service is a different route from bulk API selection. It can be useful for one-off evidence, but it is not a bulk API, not a full registry feed, and not a turnkey due-diligence product.

### 115-FZ and Sanctions

Do not assume a standard counterparty API fully solves AML, 115-FZ, or sanctions screening. Evaluate specialized compliance products and legal requirements separately. The existing company-data comparison says Kontur.Compliance API should be evaluated separately for this scenario.

## Current Research Limits

- No live credentials were used in the active profiles or comparison.
- Kontur and Seldon API prices require commercial quotes.
- SLA, storage, redistribution, SaaS display, and data-retention rights require written confirmation.
- FTS total cost depends heavily on internal ETL and operations.
- No benchmark proves superiority on a real customer dataset.

## Questions Before Procurement

1. Which fields are mandatory for the product or process?
2. What request volume, peak rate, and batch size are expected?
3. Is monitoring required, or only one-time enrichment?
4. Can responses be stored, cached, displayed to customers, or redistributed?
5. Is the use case internal, SaaS-facing, regulated, or resale-oriented?
6. What legal basis allows the test sample to be sent to providers?
7. What is the three-year TCO, including implementation and operations?

## Atlas Documents

- [API Index](../../API_INDEX.md)
- [Comparison Index](../../COMPARISON_INDEX.md)
- [Company and counterparty data comparison](../../comparisons/company-counterparty-data-russia/README.md)
- [Counterparty API procurement kit](../../procurement/counterparty-api-selection/README.md)

## Next Step

Start with the quick table above, then read the [comparison](../../comparisons/company-counterparty-data-russia/README.md). If procurement or enterprise risk is involved, fill the [procurement kit](../../procurement/counterparty-api-selection/README.md) before choosing a provider.

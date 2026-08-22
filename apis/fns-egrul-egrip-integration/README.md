# Russian FTS EGRUL and EGRIP Data Integration

[Русская версия](README.ru.md)

> Official FTP XML archives for loading Russian legal-entity and sole-proprietor registries into internal systems.

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-15 |
| Provider | Federal Tax Service of Russia |
| Status | Active |
| Type | Bulk data feed, not a conventional REST API |
| Live test | Not performed |

## Quick Verdict

**Best for:** an internal registry warehouse, bulk processing, and complete ETL control.

**Avoid when:** simple taxpayer-ID lookup, ready JSON, risk scoring, relationships, court, or procurement context is required without infrastructure.

**Bottom line:** a primary government feed rather than a commercial-API equivalent. It is justified at scale with a team able to operate FTP, XML parsing, normalization, history, and data-quality controls.

## Delivery Model

The FTS supplies FTP archives containing XML, with full data from registry inception through January 1 of the current year and daily changes afterward. EGRUL and EGRIP access are separate. Daily file generation may be interrupted; omitted data may appear in later files.

## Critical 2026 Transition

EGRUL 4.08 and EGRIP 4.07 took effect on February 1, 2026. The formal transition window ended on July 31, 2026.

Atlas rechecked the official public FTS sources on **2026-08-15**. The current public pages now present a conflict:

- they still say files are currently uploaded in both old and new formats;
- they also say that from August 1, 2026 delivery is only in EGRUL 4.08 and EGRIP 4.07;
- Order No. `ЕД-7-14/613@` requires exclusive new-format delivery from 2026-08-01.

Credentialed FTP directories and production XML payloads were not tested, so Atlas cannot prove which statement reflects actual current delivery behavior.

## Technical Model

| Field | Value |
|---|---|
| Delivery | FTP archives |
| Format | XML |
| Normative target formats | EGRUL 4.08; EGRIP 4.07 |
| Example encoding | `windows-1251` |
| Full snapshot | Registry inception to January 1 |
| Incremental | Daily changes |
| REST/JSON | No |
| Authentication | Access attributes, password, `.p12` certificate |
| SLA | Not found; interruptions explicitly possible |

## Fees Per Registry

| Option | Fee |
|---|---:|
| Annual subscription for one workstation | RUB 150,000 |
| One-time full data | RUB 50,000 |
| One-time updated data | RUB 5,000 |

Annual access to both EGRUL and EGRIP is arithmetically **RUB 300,000**, excluding engineering and infrastructure.

## TCO Components

FTP client, certificate security, download/checksum/extraction, version-aware XML parsing, retries, normalization, current-state reconstruction, history, database, backup, monitoring, delayed-file recovery, and legal review.

## Recommended Architecture

```text
FTP download
    ↓
immutable raw archive
    ↓
checksum + schema validation
    ↓
version-aware XML parser
    ↓
normalized staging
    ↓
entity/change reconciliation
    ↓
current state + history
    ↓
internal API / analytics
```

## Strengths

Primary official source, bulk delivery, registry history, daily changes, and full internal control.

## Weaknesses

Not REST/JSON, high engineering burden, separate registry fees, no ready risk analytics, possible delayed files, and an unresolved official-source conflict about post-cutover format delivery.

## Legal Questions

Review redistribution, paid third-party access, derived databases, personal-data joins, retention, and historical/corrected records. Technical access is not blanket permission for any resale model.

## Sources

- https://www.nalog.gov.ru/rn77/service/egrip2/
- https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/
- https://www.nalog.gov.ru/rn77/service/egrip2/access_order/
- https://www.nalog.gov.ru/rn77/service/egrip2/fillingbill/
- https://www.nalog.gov.ru/rn77/about_fts/docs/16493030/

## Disclosure

No commercial relationship exists. FTP credentials and certificate were not obtained.

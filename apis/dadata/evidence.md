# DaData evidence log

[Русская версия](evidence.ru.md)

Verified: **2026-07-23**

This file records claim-level evidence. It does not replace the provider documents.

| ID | Claim | Primary source | Status | Notes |
|---|---|---|---|---|
| DAD-001 | DaData exposes APIs for addresses, companies, banks, names, phones, passports, email and other reference data | https://dadata.ru/api/ | verified | Official API directory |
| DAD-002 | Suggestions/search uses `Authorization: Token` and the `suggestions.dadata.ru/.../4_1/rs` family | https://dadata.ru/api/suggest/address/ | verified | Method documentation |
| DAD-003 | Address cleansing uses token plus `X-Secret` at `cleaner.dadata.ru/api/v1/clean/address` | https://dadata.ru/api/clean/address/ | verified | Method documentation |
| DAD-004 | Address Suggestions allows 30 requests/s per IP and 60 new connections/minute | https://dadata.ru/api/suggest/address/ | verified | Method limitations |
| DAD-005 | Address cleansing allows one address/request, 20 requests/s per IP and 60 new connections/minute | https://dadata.ru/api/clean/address/ | verified | Method limitations |
| DAD-006 | Cleansing is not supported from browser JavaScript because it would expose the secret key | https://dadata.ru/api/clean/address/ | verified | Official limitation |
| DAD-007 | Free subscription tier is 10,000 requests/day | https://dadata.ru/pricing/ | verified | Pricing page |
| DAD-008 | Light is ₽14,000/year and 50,000 requests/day | https://dadata.ru/pricing/ | verified | Pricing page |
| DAD-009 | Extended is ₽28,000/year and 100,000 requests/day | https://dadata.ru/pricing/ | verified | Pricing page |
| DAD-010 | Maximum starts at ₽56,000/year and 200,000 requests/day | https://dadata.ru/pricing/ | verified | Pricing page; higher volumes selectable |
| DAD-011 | Paid subscriptions are purchased for at least one year | https://dadata.ru/pricing/ | verified | Pricing FAQ |
| DAD-012 | Subscription daily limit is shared across subscription services | https://dadata.ru/pricing/ | verified | Pricing FAQ |
| DAD-013 | Address cleansing/geocoding/cadastral lookup costs ₽0.20 per record outside subscription | https://dadata.ru/pricing/ | verified | Pricing table |
| DAD-014 | Suggestions may consume 10–30 calls for an address and 10–20 for name/email/company/bank input | https://dadata.ru/pricing/ | verified | Pricing FAQ |
| DAD-015 | Company lookup is available by INN, INN/KPP and OGRN | https://dadata.ru/api/find-party/ | verified | Method documentation |
| DAD-016 | Company lookup has 30 requests/s per IP and query length up to 300 characters | https://dadata.ru/api/find-party/ | verified | Method limitations |
| DAD-017 | Tax authority does not provide branch KPP for about 25% of companies | https://dadata.ru/api/find-party/ | verified | Provider limitation; source limitation |
| DAD-018 | Address cleansing is Russia-only | https://dadata.ru/api/clean/address/ | verified | Method scope |
| DAD-019 | Address Suggestions covers all countries to at least city level with deeper coverage in selected countries | https://dadata.ru/api/suggest/address/ | verified | Provider-documented coverage |
| DAD-020 | OpenAPI schemas exist for cleansing, Suggestions/search and account methods | https://dadata.ru/api/ | verified | Official API directory |
| DAD-021 | Provider-organization Python, PHP and C# repositories exist and are not archived | GitHub: hflabs/dadata-py, hflabs/dadata-php, hflabs/dadata-csharp | verified | Confirmed through GitHub connector on 2026-07-23 |
| DAD-022 | Python client requires Python 3.9+ and supports sync and async clients | https://github.com/hflabs/dadata-py/blob/master/README.md | verified | README modified 2025-10-07 in connector result |
| DAD-023 | Offer revision is dated 2026-04-20 | https://dadata.ru/files/documents/Оферта_DaData.20260420.pdf | verified | Offer cover page |
| DAD-024 | Offer states average monthly availability of at least 99% | Same offer PDF, section 6.1 | verified | Contractual commitment, not independently measured |
| DAD-025 | Offer limits weekday 08:00–20:00 Moscow downtime to 30 minutes | Same offer PDF, section 6.2 | verified | Contractual commitment |
| DAD-026 | Offer prohibits using Suggestions for automatic processing of addresses, names and email | Same offer PDF, section 4.2.1 | verified | Important product-use restriction |
| DAD-027 | Offer states API processing is not logged and source/processed data is not stored | Same offer PDF, section 5.2.2 | verified | Contract statement |
| DAD-028 | Offer says the user is the personal-data operator for data processed through the service | Same offer PDF, section 5.4 | verified | Legal interpretation should be reviewed for each implementation |
| DAD-029 | Offer says rights to the site and data belong to DaData or other rightsholders | Same offer PDF, section 8.1 | verified | General redistribution permission not found |
| DAD-030 | A public service-status page exists | https://status.dadata.ru/ | verified | Historical uptime not independently calculated |
| DAD-031 | Webhooks are absent | — | unknown | Not found in reviewed public docs; absence not proven |
| DAD-032 | OAuth 2.0 is absent | — | unknown | Not found in reviewed public docs; absence not proven |
| DAD-033 | Returned data may be freely redistributed or resold | — | unknown | No general permission identified; legal confirmation required |
| DAD-034 | Production latency and accuracy | — | unknown | No credentialed test performed |

## Evidence-quality notes

- Pricing, limits and terms are time-sensitive and require rechecking.
- Provider claims about coverage and accuracy were recorded as provider-documented facts, not independently benchmarked results.
- The offer PDF was reviewed visually page by page because it was not available as parsed text.
- No secret keys, account data or live requests were used.

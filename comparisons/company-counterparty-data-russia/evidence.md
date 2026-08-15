# Evidence — Company and Counterparty Data APIs

[Русская версия](evidence.ru.md)

Verified: **2026-07-23**. GLOBAS.API addendum checked: **2026-07-28**. FTS official-source conflict recheck: **2026-08-15**.

| ID | Claim | Official source | Status | Note |
|---|---|---|---|---|
| DAD-001 | DaData finds a company or entrepreneur by INN, INN/KPP, or OGRN | [Documentation](https://dadata.ru/api/find-party/) | verified | `findById/party` method |
| DAD-002 | Published maximum rate is 30 requests/s per IP | [Documentation](https://dadata.ru/api/find-party/) | verified | Connection-creation limit is also documented |
| DAD-003 | Free access includes up to 10,000 requests/day | [Documentation](https://dadata.ru/api/find-party/), [pricing](https://dadata.ru/pricing/) | verified | Activated after registration |
| DAD-004 | Annual plans are RUB 14,000 / 28,000 / 56,000 | [Pricing](https://dadata.ru/pricing/) | verified | Light, Extended, Maximum |
| DAD-005 | Company-data completeness depends on the plan | [Pricing](https://dadata.ru/pricing/) | verified | Owners, finance, debt, and contacts are plan-dependent |
| DAD-006 | Financial indicators are partially populated for about 60% of active companies | [Response fields](https://dadata.ru/api/find-party/) | verified | Vendor statement |
| DAD-007 | Affiliate lookup is a separate method and belongs to the maximum plan | [Method](https://dadata.ru/api/find-affiliated/), [pricing](https://dadata.ru/pricing/) | verified | Not available on every plan |
| KON-001 | Focus API supports autocomplete, bulk checks, monitoring, reports, and relationship analysis | [Official API selection](https://focus.kontur.ru/site/api-choice) | verified | Vendor capability list |
| KON-002 | Data includes EGRUL/EGRIP, bankruptcy, enforcement, arbitration, financial statements, public contracts, trademarks, and licenses | [Official API demo](https://focus.kontur.ru/site/demo/requisites) | verified | Official source/data list |
| KON-003 | More than 30 integration modules are offered | [Official API page](https://focus.kontur.ru/site/api) | verified | Vendor statement |
| KON-004 | More than 1,400 customers use the API | [Official API page](https://focus.kontur.ru/site/api) | reported | Vendor marketing metric; not independently verified |
| KON-005 | A public developer portal exists | [Developer reference](https://developer.kontur.ru/doc/focus?about=2) | verified | Interactive app requires JavaScript |
| KON-006 | Demo access is request-based | [Demo request](https://focus.kontur.ru/site/order-demo-api) | verified | Commercial follow-up required |
| KON-007 | 115-FZ and sanctions capabilities are a separate API product | [API selection](https://focus.kontur.ru/site/api-choice) | verified | Do not merge with counterparty API |
| KON-008 | Exact current API cost was not established | [API pricing page](https://focus.kontur.ru/site/price/api-group/counteragent) | unknown | Configuration and quote are required |
| SEL-001 | Seldon.Basis API integrates company data into CRM/ERP systems | [Official API page](https://seldongroup.ru/system/basis/api) | verified | Vendor positioning |
| SEL-002 | Available data includes registration, arbitration, public contracts, bank guarantees, finance, enforcement, and bankruptcy | [Official API page](https://seldongroup.ru/system/basis/api) | verified | Vendor functionality matrix |
| SEL-003 | API output is JSON | [Official API data description](https://seldongroup.ru/kakie-dannye-mozhno-poluchit-cherez-api-seldon-basis) | verified | Explicit vendor statement |
| SEL-004 | Individual plan reference limit is 10,000 requests/day per method | [Product functionality](https://seldongroup.ru/functions) | verified | Each method call is counted separately |
| SEL-005 | Each individual-plan method is priced separately | [Product functionality](https://seldongroup.ru/functions) | verified | Exact prices are not public |
| SEL-006 | Russia and CIS company data is available | [Seldon.Basis](https://seldongroup.ru/system/basis), [API](https://seldongroup.ru/system/basis/api) | verified | Country coverage depends on product and plan |
| SEL-007 | Exact public API price was not found | [Official API page](https://seldongroup.ru/system/basis/api) | unknown | Web-subscription prices are not API prices |
| SEL-008 | The site showed a DDoS / instability notice at the verification date | [API page](https://basis.myseldon.com/ru/home/api) | observed | Temporary notice; must be rechecked |
| GLO-001 | Credinform/GLOBAS has an official GLOBAS.API product page | [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | verified | Active official product identity |
| GLO-002 | Product is positioned for integrating GLOBAS data into corporate systems | [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | provider_reported | Enterprise integration use case |
| GLO-003 | Official page describes mass checks, portfolio monitoring, internal-base enrichment, field updates, data verification, archives, and large-database updates | [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | provider_reported | Useful for CRM/ERP/EDI and portfolio scenarios |
| GLO-004 | Public API specification, endpoint catalog, authentication, schemas, production limits, SLA and API price were not found in reviewed official pages | [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api), [services](https://globas.credinform.ru/ru-RU/servisy), [requirements](https://globas.credinform.ru/ru-RU/requirements) | observed | Procurement blocker |
| GLO-005 | Three-day GLOBAS system test is not confirmed as API trial | [GLOBAS.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | observed | Requires provider confirmation of API credentials or sandbox |
| GLO-006 | Sanctions Compliance is treated as a separate product/module boundary until proven otherwise | [Sanctions Compliance](https://globas.credinform.ru/ru-RU/servisy/sanctions) | observed | Do not assume inclusion in standard API |
| FTS-001 | The FTS provides EGRUL/EGRIP data for information-system integration | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Dedicated integration mode |
| FTS-002 | Integration uses archives with XML files and daily changes | [Interaction model](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Not a typical REST API |
| FTS-003 | An archive may contain up to 100 XML files, with up to 1,000 records per file | [Interaction model](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Official file model |
| FTS-004 | Annual access costs RUB 150,000 per registry and workstation | [Access process](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | verified | EGRUL or EGRIP separately |
| FTS-005 | One-time access is RUB 50,000 and an update is RUB 5,000 | [Access process](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | verified | Per registry |
| FTS-006 | Both registries imply RUB 300,000/year | [Access process](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | inferred | 150,000 × 2; engineering excluded |
| FTS-007 | Old and new formats coexist until 2026-08-01 | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | EGRUL 4.07/4.08; EGRIP 4.06/4.07 |
| FTS-008 | Only new formats are scheduled after 2026-08-01 | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Recheck after transition |
| FTS-008A | Current public FTS pages still say files are uploaded in both old and new formats | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/), [Interaction model](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Checked 2026-08-15 |
| FTS-008B | The same public pages also say that from 2026-08-01 delivery is only in EGRUL 4.08 and EGRIP 4.07 formats | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/), [Interaction model](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Checked 2026-08-15 |
| FTS-008C | Order No. ED-7-14/613@ requires exclusive new-format delivery from 2026-08-01 | [Order No. ED-7-14/613@](https://www.nalog.gov.ru/rn77/about_fts/docs/16493030/) | verified | Point 6 |
| FTS-008D | Public official sources conflict and credentialed FTP behavior remains unverified | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/), [Order No. ED-7-14/613@](https://www.nalog.gov.ru/rn77/about_fts/docs/16493030/) | observed | Do not overclaim actual current delivery behavior |
| FTS-009 | Daily-file generation can be interrupted | [Integration service](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Missing data is expected in later files |
| FTS-010 | A free electronic extract for one entity is signed by the FTS | [EGRUL/EGRIP information](https://www.nalog.gov.ru/rn77/related_activities/registries/egrul_egrip/) | verified | Separate web service, not bulk API |

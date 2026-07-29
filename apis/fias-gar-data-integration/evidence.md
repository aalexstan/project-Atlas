# FIAS/GAR Data Integration Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| FIAS is a federal state information system for formation, maintenance and use of GAR. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | FNS service page. |
| GAR is a state information resource containing address information. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | FIAS Info page. |
| FNS is the operator of FIAS. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Official operator statement. |
| GAR/FIAS aim to provide a single open federal resource with reliable, uniform, public address information. | https://www.nalog.gov.ru/rn77/service/fias/ | 2026-07-29 | verified | Legal and registry positioning. |
| Public portal states GAR is the only legitimate source of address information. | https://fias-file.nalog.ru/ | 2026-07-29 | verified | Registry provenance claim. |
| GAR must be used by public authorities and local governments for services, according to FIAS Info page. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Regulated workflow relevance. |
| Address objects include buildings, structures, land plots, premises and parking spaces. | https://fias-file.nalog.ru/FiasInfo | 2026-07-29 | verified | Scope of address objects. |
| Developer section exposes Open data/file downloads, SMEV and API services entries. | https://fias-file.nalog.ru/Frontend | 2026-07-29 | observed | Detailed API docs not visible in static page. |
| FNS archived material states that FIAS portal published API and SMEV services for obtaining GAR information. | https://www.nalog.gov.ru/rn77/news/activities_fts/13611328/ | 2026-07-29 | verified | Archived page may contain outdated details, but supports existence/provenance of official channels. |
| FNS archived material describes integration routes: weekly portal downloads published twice per week, SMEV daily publication and online API batch provision by request. | https://www.nalog.gov.ru/rn77/news/activities_fts/13824755/ | 2026-07-29 | verified | Treat cadence as official historical context until current developer docs are captured. |
| FNS archived material says GAR file downloads can be downloaded in the FIAS developer/open-data section and also via SMEV and API services. | https://www.nalog.gov.ru/rn77/news/activities_fts/13874101/ | 2026-07-29 | verified | Confirms file/API/SMEV route split. |
| Public address search exists on the FIAS portal. | https://fias-file.nalog.ru/Search | 2026-07-29 | observed | Web service, not a bulk API proof. |
| Search and Frontend pages were reviewed as user-facing portal pages, not as supported public API documentation. | https://fias-file.nalog.ru/Search | 2026-07-29 | inferred | Do not document visible website endpoints as stable integration APIs. |
| Complete public API method catalog, base URL, auth, schemas, quotas and SLA were not found in reviewed static pages. | Official pages reviewed | 2026-07-29 | unknown | Main blocker before API-like maturity. |
| Direct/reverse geocoding capability was not confirmed. | Official pages reviewed | 2026-07-29 | unknown | GAR is address registry, not geocoder. |

## Live Testing

No live integration, file download verification or credentialed API test was performed.

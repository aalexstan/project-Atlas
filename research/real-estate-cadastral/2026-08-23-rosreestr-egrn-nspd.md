# Rosreestr EGRN and NSPD Research - 2026-08-23

[Русская версия](2026-08-23-rosreestr-egrn-nspd.ru.md)

## Scope

Determine whether Rosreestr or Roskadastr provides a supported public interface for commercial cadastral lookup, automated EGRN extracts or bulk spatial-data integration.

## Official Sources

- [Roskadastr FAQ for cadastral engineers](https://roscadastre.ru/html/news_2024/67593ca59252f431e8639b07.pdf)
- [Roskadastr 2025 legal-change digest](https://roscadastre.ru/html/news_2025/67a453ef71101331420997e4f.pdf)
- [NSPD services and formats information issue](https://www.roscadastre.ru/html/docs/2025/67808f9247208bdccde18ac6.pdf)
- [Rosreestr XML schema notice](https://www.roscadastre.ru/docs/4192857/)
- [Rosreestr information letter on EGRN access](https://www.roscadastre.ru/docs/rrdocs/4243559/)

## Confirmed Facts

- EGRN information is provided under Federal Law No. 218-FZ and Rosreestr Order No. P/0149.
- Official material describes `Request via access to FGIS EGRN`, using an access key and prepaid package operations valid for one year.
- Official 2025 material reports package extracts in a 116-290 RUB range, but the current applicant, package and extract conditions require confirmation.
- NSPD electronic services can provide JSON, XML, PDF and CSV files. Machine-readable output does not by itself prove a general public developer API.
- Rosreestr publishes XML schemas for cadastral documents and inter-agency exchange. Schemas do not prove open API access for commercial applications.
- Access rules distinguish public information, restricted information and applicant-specific legal grounds.

## Product Boundaries

The official landscape contains at least four different routes:

1. Individual, legally significant EGRN extracts.
2. Key-based package access to FGIS EGRN.
3. NSPD portal and electronic geoservices.
4. Regulated inter-agency XML document exchange.

A cadastral-map frontend endpoint must not be treated as a supported production API without official documentation and terms. A map lookup is not legally equivalent to an EGRN extract.

## Unknowns and Blockers

- Supported endpoint and method catalog for ordinary commercial organizations.
- Access-key onboarding, authentication and automation model.
- Current package tariffs, quotas, rate limits, SLA and support.
- Whether NSPD services support unattended external production use.
- Storage, caching, customer display, SaaS, redistribution and resale rights.
- Rules for derived datasets, valuation, scoring and model training.
- Personal-data boundaries, versioning and change notification.

## Live Testing and Decision

Not performed. Atlas did not authenticate, call frontend endpoints, order an extract or execute a paid operation.

Do not create an active API profile until an official specification or written Rosreestr/Roskadastr clarification confirms a supported commercial integration route.

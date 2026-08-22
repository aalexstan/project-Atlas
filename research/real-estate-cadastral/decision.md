# Rosreestr EGRN and NSPD Profile Decision

[Русская версия](decision.ru.md)

## Decision

Create a reviewed profile for **Rosreestr EGRN Access Service** with product class `official_registry_access_service`. Do not describe it as a generic REST API.

Official sources confirm electronic EGRN access, access-key packages, machine-readable NSPD outputs and XML schemas. They do not confirm one supported public API for ordinary commercial developers with a complete endpoint catalog, authentication flow, quotas, SLA and downstream-use terms.

A generic `Rosreestr API` profile would incorrectly merge legally significant extracts, package access, NSPD geoservices, inter-agency exchange and public-map frontend endpoints. The active profile therefore covers only the official EGRN request/access route and keeps unattended automation as unknown.

## Maturity Conditions

- Confirm the product identity, intended audience, base URL and methods.
- Confirm onboarding, authentication, formats and schemas.
- Confirm current fees, quotas, rate limits, SLA and support.
- Confirm storage, display, SaaS, redistribution and personal-data terms.
- Confirm versioning and breaking-change policy.

## Safe Current Recommendation

- Use an official EGRN extract when legally significant evidence is required.
- Evaluate key-based FGIS EGRN access for repeated extracts after onboarding and tariff confirmation.
- Use NSPD for spatial-data discovery; do not presume unrestricted REST access.
- Do not automate undocumented cadastral-map frontend endpoints in production.

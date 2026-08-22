# Rosreestr EGRN Access Service

[Русская версия](README.ru.md)

> Official route for requesting EGRN information. This profile is intentionally not called a generic REST API.

## Verdict

Use this route when the output must be an official EGRN extract or when repeated official extracts justify evaluating access-key packages.

Do not use public cadastral-map frontend calls as a substitute. A map lookup, an NSPD layer and a legally significant EGRN extract are different products.

## Access Model

Official material confirms individual requests and `Request via access to FGIS EGRN`, with an access key and prepaid package operations valid for one year. Public evidence reviewed by Atlas does not yet document a complete unattended API flow, base URL or method catalog for an ordinary commercial organization.

## Commercial Boundary

An official 2025 publication reported a 116-290 RUB range for package extracts. Treat it as evidence of the package model, not as a current universal API price. Confirm the applicant category, extract type, package, fee and validity before procurement.

## Main Risks

- current automation and authentication mechanics are unclear;
- quotas, rate limits and SLA are not public in reviewed evidence;
- restricted information depends on legal grounds;
- storage, customer display, SaaS and redistribution require written review;
- no live test or paid extract was performed.

See [evidence](evidence.md), [comparison](../../comparisons/real-estate-cadastral-data/README.md) and the [need route](../../needs/real-estate-cadastral-data/README.md).

# Moscow Open Data API Profile Decision

[Русская версия](decision.ru.md)

## Decision

Do **not** create an active API-first profile for Moscow Open Data API in this pass.

## Rationale

The official developer documentation at `https://data.mos.ru/developers/documentation` is now accessible and provides verified facts about API endpoints, parameters, and response format. The terms of use (`https://data.mos.ru/terms`) confirm that the data is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0) with attribution required. However, the following required information remains unknown or unverified:

- authentication method (API key acquisition requires authorization/registration);
- rate limits, quotas, and SLA;
- detailed current operational status and support process.

Because an active API profile requires sufficient evidence for at least Verified maturity across all required aspects, these gaps prevent creating an active profile at this time.

## Status

Keep as **legacy/supporting research**. The API documentation is now accessible, providing verified facts about:
- API endpoints (`/v1/datasets/{id}/features`, `/v1/features/{id}`)
- Supported query parameters (`$top`, `$skip`, `versionNumber`, `releaseNumber`, `bbox`)
- Response format (FeatureCollection with GeoJSON features)
- Example use case (accessing datasets like outdoor ice rinks)
- License: CC BY 4.0 with attribution requirement
- Technical support contact: opendata@mos.ru
- Data request contact: Хунас Амин Касиевич

Reopen consideration for an active profile only when official sources confirm:
- authentication method and API key acquisition process;
- rate limits, quotas, and SLA;
- current operational status and support process.

## Reopen Conditions

Create an active profile only when official sources confirm:
- current product identity;
- documentation or endpoint;
- authentication;
- supported formats;
- intended use and main operations;
- current availability;
- license/reuse terms.

# Nominatim Research Log

Date: 2026-07-29

## Scope

This log evaluates OpenStreetMap Nominatim for address/geocoding decisions. It separates the public OSMF-hosted Nominatim service, self-hosted Nominatim software and commercial third-party Nominatim providers.

## Official Sources Reviewed

- https://operations.osmfoundation.org/policies/nominatim/
- https://nominatim.org/release-docs/latest/api/Search/
- https://nominatim.org/release-docs/latest/api/Reverse/
- https://nominatim.org/release-docs/latest/admin/Import/
- https://nominatim.org/release-docs/latest/admin/Update/
- https://www.openstreetmap.org/copyright

## Confirmed Facts

- The public usage policy applies to `nominatim.openstreetmap.org` and does not apply to self-hosted or other organizations' Nominatim services.
- Public Nominatim has limited capacity and requires no heavy use, with an absolute maximum of 1 request/second.
- Public usage requires a valid HTTP Referer or User-Agent identifying the application and clear attribution.
- Public policy requires compliance with ODbL and notes share-alike obligations for OSM data.
- Bulk geocoding is discouraged on the public service; regular or long-running scripts have tighter restrictions, and results must be cached.
- Public Nominatim forbids autocomplete search and systematic queries.
- Applications or services whose primary function is geocoding must run their own service under the public policy.
- Nominatim Search supports free-form and structured queries.
- Search endpoint format is `https://nominatim.openstreetmap.org/search?<params>`.
- Search output formats include `xml`, `json`, `jsonv2`, `geojson` and `geocodejson`; `limit` defaults to 10 and cannot exceed 40.
- Reverse geocoding returns an address from latitude/longitude by finding the closest suitable OSM object; it can return unexpected results.
- Reverse endpoint format is `https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>`.
- OpenStreetMap data is licensed under ODbL and requires attribution.
- Self-hosting requires importing OSM planet or extracts into a Nominatim database and operating updates.

## Provider-Reported Claims

- Nominatim documentation gives full-planet import guidance and operational notes. Atlas did not deploy or benchmark it.

## Observations

- Nominatim is better represented in Atlas as open-source geocoder software and an OSM data route, not as a conventional hosted commercial API.
- The public OSMF instance is not suitable as a free production dependency for high-volume address autocomplete, SaaS enrichment or API resale.
- Self-hosting moves cost from API subscription to infrastructure, database import/update operations, monitoring and license compliance.

## Unknowns

- Production SLA for public OSMF Nominatim: not offered in reviewed policy.
- Exact hardware sizing for a user's geography and throughput.
- Address-quality benchmark for Russia or target international markets.
- Legal obligations for a specific derived database, cache or SaaS product.
- Commercial third-party provider terms; they are outside this profile.

## Contradictions

- Public search endpoint exists, but public policy sharply limits production-style use. The endpoint must not be treated as permission for arbitrary automated use.

## Commercial Blockers

- No public hosted SLA from OSMF.
- Public instance cannot be used for autocomplete and cannot be resold as a primary geocoding dependency.
- Self-hosting requires operational budget and expertise.

## Legal and Data-Rights Blockers

- ODbL attribution and share-alike/database obligations require legal review for storage, derived datasets and SaaS use.
- The public policy asks users not to submit personal or confidential data to OSMF services.

## Live Testing Status

No Atlas live test, import or benchmark was performed.

## Decision

Create an active profile for `nominatim-geocoder-software` with product class `open_source_geocoder_software`. Do not present the public OSMF-hosted service as a free production API.

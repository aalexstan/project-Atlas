# 2GIS Suggest and Places Research Log

Date: 2026-07-29

## Scope

This log checks 2GIS Suggest API and Places API as separate products from 2GIS Geocoder API and routing APIs.

## Official Sources Reviewed

- https://docs.2gis.com/en/api/search/overview
- https://docs.2gis.com/en/api/search/suggest/overview
- https://docs.2gis.com/en/api/search/places/overview
- https://docs.2gis.com/en/platform-manager/subscription/pricing
- https://law.2gis.ru/offer-license-agreement-webapi

## Confirmed Facts

- 2GIS documentation separates Search APIs into Geocoder API, Places API, Suggest API and other related APIs.
- Suggest API is intended to provide suggestions while a user enters text in a search field.
- Suggest API requests use HTTP GET with query parameters and JSON responses.
- Suggest API examples use `https://catalog.api.2gis.com/3.0/items` with `q`, `location` and `key`.
- Suggest API supports object suggestions by default and documented address, street and route endpoint suggestion types.
- Suggest API is optimized for use together with Places API, but can be constrained by `suggest_type`.
- Places API searches organizations, buildings and places.
- Places API supports searches by company name, category/business area, geotags, attributes, telephone/website and other criteria.
- 2GIS docs require an access key from Platform Manager: demo key or paid subscription.
- Public pricing lists monthly Search-service packages in RUB. Suggest API packages start at 100,000 units; Places API has lower package tiers.
- Public pricing lists 600 Search units/minute for Places API, Geocoder API and Suggest API.
- Demo Search-service limits list 1,000 total requests for Places API, Geocoder API and Suggest API.
- The 2GIS WebAPI offer states that caching of products is not provided and restricts extraction, storage, processing, modification and distribution outside contract terms.
- The offer states version compatibility for API methods during the version period and for one year after publication of a new version.

## Provider-Reported Claims

- 2GIS states that its directory is updated monthly and becomes available simultaneously in 2GIS products. Atlas did not benchmark freshness.
- 2GIS states that On-Premise deployment is available for the API Platform and that current Suggest API methods are available in private-network installation.

## Observations

- Suggest API and Places API are not the same as Geocoder API. Suggest is an autocomplete helper; Places is a directory/search API for objects and organizations; Geocoder maps address/name and coordinates.
- Some richer Places fields and methods are explicitly on-demand and may require extra paid permission.
- 2GIS address and organization scenarios often require pairing Suggest API with Places API.

## Unknowns

- Public SLA and production support tiers.
- OpenAPI/Swagger availability.
- Exact geographic coverage and country-by-country object coverage.
- Batch/asynchronous search support.
- Exact SaaS, redistribution and customer-facing display rights for a given deal.
- Whether the target paid plan includes all required on-demand fields.

## Contradictions

- No contradiction was found in official sources. The main risk is product-boundary confusion between Geocoder, Suggest and Places.

## Commercial Blockers

- Suggest and Places have different tariff rows and should be priced separately.
- On-demand fields and methods can change the effective cost of a Places integration.
- Storage/caching restrictions are material for enrichment and SaaS use.

## Legal and Data-Rights Blockers

- The WebAPI offer restricts extraction and storage outside contract terms and says caching is not provided.
- Attribution and display requirements must be reviewed for the target user interface.

## Live Testing Status

No Atlas credentialed live test was performed.

## Decision

Create separate active profiles for `2gis-suggest-api` and `2gis-places-api`. Keep `2gis-geocoder-api` as the direct/reverse geocoding profile and connect all three in the address/geocoding comparison.

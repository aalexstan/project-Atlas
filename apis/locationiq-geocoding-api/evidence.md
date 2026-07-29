# LocationIQ Geocoding API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| LocationIQ documentation separates Search / Forward Geocoding, Reverse Geocoding, Autocomplete, Nearby POI and routing APIs. | https://docs.locationiq.com/docs/choose-the-right-api | 2026-07-29 | verified | Routing is not included in this profile. |
| Forward Geocoding converts addresses to coordinates and is exposed through `/v1/search`; US and EU endpoint examples are documented. | https://docs.locationiq.com/docs/search-forward-geocoding | 2026-07-29 | verified | Free-form, structured and postal-code request forms are listed. |
| Search / Forward Geocoding requires an API key/access token and supports JSON, XML and `xmlv1.1` formats. | https://docs.locationiq.com/docs/search-forward-geocoding | 2026-07-29 | verified | Response examples include coordinates and address breakdown fields. |
| Reverse Geocoding converts coordinates to a readable address/place name and uses `/v1/reverse`. | https://docs.locationiq.com/docs/reverse-geocoding | 2026-07-29 | verified | Required parameters include `key`, `lat` and `lon`. |
| Autocomplete has a separate `/v1/autocomplete` endpoint for type-ahead suggestions. | https://docs.locationiq.com/docs/autocomplete | 2026-07-29 | verified | This is separate from the Search / Forward endpoint. |
| API Reference documents access-token authentication, security restrictions, API collection and endpoint details. | https://api-reference.locationiq.com/ | 2026-07-29 | verified | Atlas did not capture a standalone OpenAPI file. |
| Public pricing lists a Free plan with 5,000 requests/day, 2 requests/second and 60 requests/minute. | https://locationiq.com/pricing | 2026-07-29 | verified | Free commercial use has attribution wording in the pricing FAQ. |
| Public pricing lists paid examples: Developer USD 100/month, Startup USD 200/month, Growth Plus USD 500/month and Business Plus USD 950/month with published request allowances and RPS examples. | https://locationiq.com/pricing | 2026-07-29 | verified | Public prices are not negotiated enterprise quotes. |
| Enterprise plan is described as custom pricing, custom request rates, custom contract and SLAs. | https://locationiq.com/pricing | 2026-07-29 | provider_reported | Requires quote and contract evidence before procurement use. |
| Provider help says API output can be stored forever, with caching restricted by account: Free plan up to 48 hours and customers while subscribed. | https://help.locationiq.com/support/solutions/articles/36000216111-can-i-save-addresses-from-api-output- | 2026-07-29 | provider_reported | Needs legal review for SaaS, redistribution and derived data. |
| Provider help says batch geocoding is not supported as multiple addresses in one API request; each address is a separate request and concurrency depends on plan limits. | https://help.locationiq.com/support/solutions/articles/36000216034-is-batch-geocoding-supported- | 2026-07-29 | verified | This separates it from hosted batch APIs. |
| Provider help says there is no UI-based batch CSV tool, but large batch processing may be arranged for a fee. | https://help.locationiq.com/support/solutions/articles/36000216040-can-i-send-addresses-to-geocode-in-a-csv- | 2026-07-29 | provider_reported | Requires provider confirmation. |
| Terms include warranty disclaimers and do not by themselves prove SLA or accuracy guarantees. | https://locationiq.com/static/tos.html | 2026-07-29 | verified | Enterprise SLA remains an open question. |

## Live Testing

No Atlas credentialed API request, benchmark, UI test, batch test or contract review was performed.

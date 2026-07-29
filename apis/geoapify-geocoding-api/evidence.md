# Geoapify Geocoding API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| Geoapify publishes an official Geocoding API product page. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | verified | Product identity. |
| Forward geocoding converts addresses to latitude/longitude. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | verified | Product purpose. |
| The Geocoding REST API works via HTTP GET and returns JSON or XML responses. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | GeoJSON also appears in API reference. |
| Forward endpoint is `https://api.geoapify.com/v1/geocode/search`. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | Request reference. |
| API-key authentication uses the `apiKey` parameter. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | Key issued through Geoapify MyProjects. |
| Reverse endpoint is `https://api.geoapify.com/v1/geocode/reverse`. | https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/ | 2026-07-29 | verified | Requires latitude/longitude. |
| Batch API can submit up to 1,000 inputs and processes jobs asynchronously. | https://apidocs.geoapify.com/docs/batch/ | 2026-07-29 | verified | Results are available for 24 hours after completion. |
| Free plan offers 3,000 credits/day and up to 5 requests/second. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Pricing can change. |
| Paid plans publish monthly prices, credit quotas and request-per-second limits. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Taxes excluded. |
| One Geocoding, Reverse Geocoding or Address Autocomplete request costs one credit. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Pricing FAQ. |
| Paid plans include a default 99.5% monthly availability SLA. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Higher SLA possible on request. |
| Geoapify says results can be stored if attribution is preserved. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | provider_reported | Legal/ODbL review still required. |
| Terms require OpenStreetMap attribution and Geoapify attribution on Free plan. | https://www.geoapify.com/terms-and-conditions/ | 2026-07-29 | verified | Attribution obligations affect UI/data reuse. |
| Download OpenAPI link is present in reviewed documentation. | https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/ | 2026-07-29 | observed | Atlas did not download or test the specification. |

## Live Testing

No Atlas credentialed request, benchmark or live API test was performed.

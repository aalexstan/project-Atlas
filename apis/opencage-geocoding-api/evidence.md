# OpenCage Geocoding API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| OpenCage publishes an official Geocoding API documentation page. | https://opencagedata.com/api | 2026-07-29 | verified | Product identity. |
| The Geocoding API provides worldwide geocoding based on open data via REST. | https://opencagedata.com/api | 2026-07-29 | verified | Provider positioning; benchmark still required. |
| The API supports reverse geocoding and forward geocoding examples. | https://opencagedata.com/api | 2026-07-29 | verified | Product purpose. |
| Authentication uses an API key passed as the `key` query parameter. | https://opencagedata.com/api | 2026-07-29 | verified | No HTTP auth header required according to docs. |
| Request pattern is `https://api.opencagedata.com/geocode/VERSION/FORMAT?parameters`; current version is `v1`. | https://opencagedata.com/api | 2026-07-29 | verified | Endpoint pattern, not credential-tested by Atlas. |
| Supported response formats include JSON, GeoJSON, XML and Google-compatible JSON. | https://opencagedata.com/api | 2026-07-29 | verified | Google-compatible format is described as a convenience and may be discontinued. |
| All returned coordinates use WGS 84 / EPSG:4326. | https://opencagedata.com/api | 2026-07-29 | verified | Coordinate system. |
| Free trial provides 2,500 requests/day and 1 request/second for testing. | https://opencagedata.com/pricing | 2026-07-29 | verified | Pricing can change. |
| Reviewed monthly pricing examples include X-Small `zł 205/mo`, Small `zł 510/mo`, Medium `zł 2050/mo`, Large `zł 4100/mo` and Enterprise from `zł 8200/mo`. | https://opencagedata.com/pricing | 2026-07-29 | verified | Currency and amounts recorded as displayed; no conversion. |
| Paid plans publish request/day and request/second examples. | https://opencagedata.com/pricing | 2026-07-29 | verified | X-Small through Large plan examples. |
| API results can be cached or stored permanently according to official docs. | https://opencagedata.com/api | 2026-07-29 | provider_reported | Legal and data-license review still required. |
| Users must respect returned data licenses, especially OpenStreetMap ODbL. | https://opencagedata.com/terms | 2026-07-29 | verified | Terms assign responsibility to users. |
| Official credits list OpenStreetMap, GeoNames, Natural Earth, OpenAddresses and other sources. | https://opencagedata.com/credits | 2026-07-29 | verified | Data-source mix can affect legal review. |
| Geocoding API does not perform fuzzy matching; autosuggest/typeahead belongs to Geosearch. | https://opencagedata.com/api | 2026-07-29 | verified | Product boundary. |
| The API itself does not allow multiple locations per request. | https://opencagedata.com/api | 2026-07-29 | verified | Provider suggests spreadsheet upload or parallel requests for volume. |
| OpenAPI specification link is present in official documentation. | https://opencagedata.com/api | 2026-07-29 | observed | Atlas did not download or test the OpenAPI file. |

## Live Testing

No Atlas credentialed request, benchmark, spreadsheet upload or live API test was performed.

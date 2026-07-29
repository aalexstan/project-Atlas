# 2GIS Suggest API Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| 2GIS Search APIs are separated into Geocoder, Places, Suggest and related APIs. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Product boundary evidence. |
| Suggest API is intended to provide suggestions while a user enters text in a search field. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Autocomplete scope. |
| Suggest requests use GET and JSON responses. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Public docs. |
| Example endpoint is `https://catalog.api.2gis.com/3.0/items` with `q`, `location` and `key`. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Access key in query. |
| Default `suggest_type` is `object`; address, street and route-endpoint suggestions are documented. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Use type-specific evaluation. |
| Suggest API is optimized for use with Places API. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Important integration relationship. |
| Access key comes from Platform Manager as demo key or subscription. | https://docs.2gis.com/en/api/search/overview | 2026-07-29 | verified | Authentication/onboarding. |
| Suggest API is priced by successful requests/month. | https://docs.2gis.com/en/api/search/suggest/overview | 2026-07-29 | verified | Billing unit is successful request. |
| Suggest API public price starts at 7,000 RUB for 100,000 units/month. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | API tariff, not web-product price. |
| Suggest API limit is 600 Search units/minute; demo limit is 1,000 total requests. | https://docs.2gis.com/en/platform-manager/subscription/pricing | 2026-07-29 | verified | Public pricing/limits page. |
| WebAPI offer says caching is not provided and restricts extraction/storage outside contract terms. | https://law.2gis.ru/offer-license-agreement-webapi | 2026-07-29 | verified | Data-rights blocker. |

## Live Testing

No Atlas credentialed live test was performed.

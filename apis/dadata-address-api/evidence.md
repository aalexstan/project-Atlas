# DaData Address APIs Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Checked | Status | Note |
|---|---|---|---|---|
| Address suggestions search by arbitrary address part and postal code. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Interactive autocomplete use case. |
| Suggestions cover all countries at least to city level; Russia to apartment; Belarus, Kazakhstan and Uzbekistan to house. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | provider_reported | Not independently benchmarked by Atlas. |
| Suggestions return granular address parts and FIAS/GAR/KLADR fields where available. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Field presence depends on record and plan. |
| Suggestions are not intended for automatic processing of address files or databases. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Use Standardization for automatic processing. |
| Suggestions endpoint is `POST https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address`. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Token authentication. |
| Suggestions limit is 30 requests/second per IP and 60 new connections/minute per IP. | https://dadata.ru/api/suggest/address/ | 2026-07-29 | verified | Daily limit depends on plan. |
| Address cleaning splits fields, calculates postal code, determines coordinates and returns registry/tax codes; Russia only. | https://dadata.ru/api/clean/address/ | 2026-07-29 | verified | Backend standardization use case. |
| Cleaning endpoint is `POST https://cleaner.dadata.ru/api/v1/clean/address`. | https://dadata.ru/api/clean/address/ | 2026-07-29 | verified | Token plus `X-Secret`. |
| Cleaning accepts one address per request, 20 requests/second per IP and 60 new connections/minute per IP; browser JavaScript is unsupported. | https://dadata.ru/api/clean/address/ | 2026-07-29 | verified | Secret key must stay server-side. |
| Direct geocoding determines coordinates by address and uses the cleaning endpoint; Russia only. | https://dadata.ru/api/geocode/ | 2026-07-29 | verified | Charged as pay-per-record service. |
| Reverse geocoding returns nearest addresses by coordinates; Russia only. | https://dadata.ru/api/geolocate/ | 2026-07-29 | verified | Uses Suggestions host with token auth. |
| Address suggestions and reverse geocoding are subscription services; cleaning, direct geocoding and cadastral lookup cost 0.20 RUB per address outside subscription. | https://dadata.ru/pricing/ | 2026-07-29 | verified | Do not mix subscription and per-record units. |
| Free tier after registration is like Light with 10,000 requests/day. | https://dadata.ru/pricing/ | 2026-07-29 | verified | Subscription services stop until next day after limit exhaustion. |
| A typical address input in Suggestions consumes 10-30 requests. | https://dadata.ru/pricing/ | 2026-07-29 | provider_reported | Use as planning warning, not benchmark. |
| API-processed standardization data is not stored by DaData; uploaded files are stored for up to one day. | https://dadata.ru/clean/ | 2026-07-29 | provider_reported | Confirm in contract for regulated data. |

## Live Testing

No Atlas credentialed live test was performed.

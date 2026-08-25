# Evidence Geoapify Geocoding API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Заметка |
|---|---|---|---|---|
| Geoapify публикует официальную product page Geocoding API. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | verified | Product identity. |
| Forward geocoding converts addresses to latitude/longitude. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | verified | Product purpose. |
| Geocoding REST API работает через HTTP GET и возвращает JSON или XML responses. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | GeoJSON также указан в API reference. |
| Forward endpoint: `https://api.geoapify.com/v1/geocode/search`. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | Request reference. |
| API-key authentication использует параметр `apiKey`. | https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/ | 2026-07-29 | verified | Key issued through Geoapify MyProjects. |
| Reverse endpoint: `https://api.geoapify.com/v1/geocode/reverse`. | https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/ | 2026-07-29 | verified | Requires latitude/longitude. |
| Batch API может отправлять до 1,000 inputs и обрабатывает jobs asynchronously. | https://apidocs.geoapify.com/docs/batch/ | 2026-07-29 | verified | Results available for 24 hours after completion. |
| Free plan даёт 3,000 credits/day и up to 5 requests/second. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Pricing can change. |
| Paid plans публикуют monthly prices, credit quotas и request-per-second limits. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Taxes excluded. |
| One Geocoding, Reverse Geocoding или Address Autocomplete request costs one credit. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Pricing FAQ. |
| Paid plans include a default 99.5% monthly availability SLA. | https://www.geoapify.com/pricing/ | 2026-07-29 | verified | Higher SLA possible on request. |
| Geoapify says results can be stored if attribution is preserved. | https://www.geoapify.com/geocoding-api/ | 2026-07-29 | provider_reported | Legal/ODbL review still required. |
| Terms require OpenStreetMap attribution and Geoapify attribution on Free plan. | https://www.geoapify.com/terms-and-conditions/ | 2026-07-29 | verified | Attribution obligations affect UI/data reuse. |
| Download OpenAPI link найден в reviewed documentation. | https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/ | 2026-07-29 | observed | Atlas did not download or test the specification. |

## Live Testing

В [ограниченном live-тесте 2026-08-25](../../research/geoapify-geocoding-api/live-test-2026-08-25.ru.md) наблюдалось authenticated forward, reverse и unknown-input JSON behavior. Raw responses показали OpenStreetMap attribution и сигнал Open Database License. Порог quota, accuracy, SLA, storage, caching, redistribution и SaaS rights остаются unknown; профильный `live_tested` остаётся `false` до human review и подтверждения account terms.

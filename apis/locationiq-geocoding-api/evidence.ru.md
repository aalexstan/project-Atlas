# Доказательства LocationIQ Geocoding API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| Документация LocationIQ разделяет Search / Forward Geocoding, Reverse Geocoding, Autocomplete, Nearby POI и routing APIs. | https://docs.locationiq.com/docs/choose-the-right-api | 2026-07-29 | verified | Routing не входит в эту карточку. |
| Forward Geocoding превращает адреса в координаты и доступен через `/v1/search`; документированы US и EU endpoint examples. | https://docs.locationiq.com/docs/search-forward-geocoding | 2026-07-29 | verified | Перечислены free-form, structured и postal-code request forms. |
| Search / Forward Geocoding требует API key/access token и поддерживает JSON, XML и `xmlv1.1`. | https://docs.locationiq.com/docs/search-forward-geocoding | 2026-07-29 | verified | Response examples включают coordinates и address breakdown fields. |
| Reverse Geocoding превращает координаты в readable address/place name и использует `/v1/reverse`. | https://docs.locationiq.com/docs/reverse-geocoding | 2026-07-29 | verified | Required parameters включают `key`, `lat` и `lon`. |
| Autocomplete имеет отдельный `/v1/autocomplete` endpoint для type-ahead suggestions. | https://docs.locationiq.com/docs/autocomplete | 2026-07-29 | verified | Это отдельный endpoint, не Search / Forward. |
| API Reference документирует access-token authentication, security restrictions, API collection и endpoint details. | https://api-reference.locationiq.com/ | 2026-07-29 | verified | Atlas не сохранял standalone OpenAPI file. |
| Public pricing перечисляет Free plan: 5,000 requests/day, 2 requests/second и 60 requests/minute. | https://locationiq.com/pricing | 2026-07-29 | verified | Free commercial use имеет attribution wording в pricing FAQ. |
| Public pricing перечисляет paid examples: Developer USD 100/month, Startup USD 200/month, Growth Plus USD 500/month и Business Plus USD 950/month с published request allowances и RPS examples. | https://locationiq.com/pricing | 2026-07-29 | verified | Public prices не являются negotiated enterprise quotes. |
| Enterprise plan описан как custom pricing, custom request rates, custom contract and SLAs. | https://locationiq.com/pricing | 2026-07-29 | provider_reported | До procurement use нужны quote и contract evidence. |
| Provider help говорит, что API output можно store forever, но caching зависит от account: Free plan до 48 часов, customers — while subscribed. | https://help.locationiq.com/support/solutions/articles/36000216111-can-i-save-addresses-from-api-output- | 2026-07-29 | provider_reported | Нужен legal review для SaaS, redistribution и derived data. |
| Provider help говорит, что batch geocoding не поддерживается как multiple addresses in one API request; каждый адрес — отдельный request, concurrency зависит от plan limits. | https://help.locationiq.com/support/solutions/articles/36000216034-is-batch-geocoding-supported- | 2026-07-29 | verified | Это отличает продукт от hosted batch APIs. |
| Provider help говорит, что UI-based batch CSV tool нет, но large batch processing may be arranged for a fee. | https://help.locationiq.com/support/solutions/articles/36000216040-can-i-send-addresses-to-geocode-in-a-csv- | 2026-07-29 | provider_reported | Требует подтверждения поставщика. |
| Terms содержат warranty disclaimers и сами по себе не доказывают SLA или accuracy guarantees. | https://locationiq.com/static/tos.html | 2026-07-29 | verified | Enterprise SLA остаётся open question. |

## Live Testing

Atlas не проводил credentialed API request, benchmark, UI test, batch test или contract review.

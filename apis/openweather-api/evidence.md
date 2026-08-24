# OpenWeather Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Status |
|---|---|---|
| One Call API 3.0 product and endpoint scope are documented | https://openweathermap.org/api/one-call-3 | verified |
| Current weather and five-day forecast routes are documented | https://openweathermap.org/api/current; https://openweathermap.org/api/forecast5 | verified |
| Pricing distinguishes subscriptions and pay-as-you-call | https://openweathermap.org/price | verified |
| Licensing differs by product/plan | https://openweathermap.org/storage/app/media/documents/License_explainer_25_Feb_25.pdf | provider_reported |

The [2026-08-24 live test](../../research/weather/openweather-live-test-2026-08-24.md) confirmed the tested current and five-day forecast routes and a structured invalid-coordinate error. One Call API 3.0 returned a subscription-required HTTP 401; `live_tested` is true for the bounded evidence window and maturity remains reviewed.

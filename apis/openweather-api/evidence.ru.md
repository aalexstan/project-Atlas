# Доказательства OpenWeather

[English version](evidence.md)

| Утверждение | Источник | Статус |
|---|---|---|
| One Call API 3.0 и scope endpoint документированы | https://openweathermap.org/api/one-call-3 | verified |
| Current weather и five-day forecast routes документированы | https://openweathermap.org/api/current; https://openweathermap.org/api/forecast5 | verified |
| Тарифы разделяют subscriptions и pay-as-you-call | https://openweathermap.org/price | verified |
| Licensing различается по product/plan | https://openweathermap.org/storage/app/media/documents/License_explainer_25_Feb_25.pdf | provider_reported |

В [live-test от 2026-08-24](../../research/weather/openweather-live-test-2026-08-24.ru.md) подтверждены проверенные current и five-day forecast routes и структурированная ошибка неверных координат. One Call API 3.0 вернул HTTP 401 с требованием подписки; `live_tested` равен true для ограниченного окна evidence, maturity остаётся reviewed.

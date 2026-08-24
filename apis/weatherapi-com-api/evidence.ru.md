# Доказательства WeatherAPI.com

[English version](evidence.md)

| Утверждение | Источник | Статус |
|---|---|---|
| API key, JSON/XML и scope продуктов документированы | https://www.weatherapi.com/docs/ | verified |
| Публичные планы и allowances опубликованы | https://www.weatherapi.com/pricing.aspx | provider_reported |
| Historical data — архив forecast, а не фактические наблюдения | https://www.weatherapi.com/pricing.aspx | provider_reported |

В [проверках без credentials и с предоставленными пользователем credentials](../../research/weatherapi-com-api/auth-probe-2026-08-24.ru.md) получен HTTP 401 со структурированными кодами ошибок 1002 и 2006. Позднее действующий key позволил провести [ограниченный live-test](../../research/weatherapi-com-api/live-test-2026-08-24.ru.md): подтверждены формы запросов current, forecast и search, но зафиксированы findings по `current_fields` и нечёткому сопоставлению локаций. `live_tested` равен true для окна evidence; maturity остаётся reviewed.

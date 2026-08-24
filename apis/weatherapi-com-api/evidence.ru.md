# Доказательства WeatherAPI.com

[English version](evidence.md)

| Утверждение | Источник | Статус |
|---|---|---|
| API key, JSON/XML и scope продуктов документированы | https://www.weatherapi.com/docs/ | verified |
| Публичные планы и allowances опубликованы | https://www.weatherapi.com/pricing.aspx | provider_reported |
| Historical data — архив forecast, а не фактические наблюдения | https://www.weatherapi.com/pricing.aspx | provider_reported |

В [auth probe без credentials](../../research/weatherapi-com-api/auth-probe-2026-08-24.ru.md) получен HTTP 401 со структурированной ошибкой code 1002; подтверждена только граница аутентификации. Валидный API-запрос не выполнялся; `live_tested` остаётся false.

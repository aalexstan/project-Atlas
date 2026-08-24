# Доказательства WeatherAPI.com

[English version](evidence.md)

| Утверждение | Источник | Статус |
|---|---|---|
| API key, JSON/XML и scope продуктов документированы | https://www.weatherapi.com/docs/ | verified |
| Публичные планы и allowances опубликованы | https://www.weatherapi.com/pricing.aspx | provider_reported |
| Historical data — архив forecast, а не фактические наблюдения | https://www.weatherapi.com/pricing.aspx | provider_reported |

В [проверках без credentials и с предоставленными пользователем credentials](../../research/weatherapi-com-api/auth-probe-2026-08-24.ru.md) получен HTTP 401 со структурированными кодами ошибок 1002 и 2006. Подтверждена только граница аутентификации. Валидный API-запрос не выполнялся; `live_tested` остаётся false.

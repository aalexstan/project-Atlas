# WeatherAPI.com Evidence

[Русская версия](evidence.ru.md)

| Claim | Source | Status |
|---|---|---|
| API key, JSON/XML and weather product scope are documented | https://www.weatherapi.com/docs/ | verified |
| Public plans and allowances are listed | https://www.weatherapi.com/pricing.aspx | provider_reported |
| Historical data is forecast archive, not actuals | https://www.weatherapi.com/pricing.aspx | provider_reported |

The [credential-free and user-provided credential probes](../../research/weatherapi-com-api/auth-probe-2026-08-24.md) returned HTTP 401 with structured error codes 1002 and 2006. They confirm only the authentication boundary. No valid API request was performed; `live_tested` remains false.

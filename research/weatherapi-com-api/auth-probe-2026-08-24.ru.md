# Auth probe WeatherAPI.com без credentials — 2026-08-24

[English version](auth-probe-2026-08-24.md)

## Цель

Подтвердить границу аутентификации без регистрации аккаунта, использования key, платных методов или попыток обхода контроля доступа.

## Проверенные официальные источники

- [Документация API WeatherAPI.com](https://www.weatherapi.com/docs/)
- [Тарифы WeatherAPI.com](https://www.weatherapi.com/pricing.aspx)
- [Условия API WeatherAPI.com](https://www.weatherapi.com/terms.aspx)
- [Регистрация WeatherAPI.com](https://www.weatherapi.com/signup.aspx)

## Граница законного и безопасного теста

- Аккаунт не создавался.
- API key, платные credentials и production-токены не использовались.
- Выполнен один безопасный GET без key.
- Это auth probe, а не live-test и не доказательство корректного ответа forecast.

## Probe

Запрос:

`GET https://api.weatherapi.com/v1/current.json?q=Moscow`

Наблюдение: HTTP `401`, `0.176436 s`.

Сырой payload:

```json
{"error":{"code":1002,"message":"API key is invalid or not provided."}}
```

## Finding

Запрос без key подтвердил границу аутентификации и структурированную JSON-ошибку. Он не проверяет валидный запрос, response contract, квоту, rate-limit headers, freshness, accuracy или commercial use.

## Blocker полноценного live-test

Для валидного теста нужен key, выданный разрешённому аккаунту. Atlas не должен регистрировать аккаунт или использовать key без явного разрешения владельца. После законного получения доступа нужно применить live-test template, проверить Terms of Service free-tier, зафиксировать разнообразные core claims и сохранить raw payload.

`live_tested` остаётся `false`; maturity остаётся `reviewed`.

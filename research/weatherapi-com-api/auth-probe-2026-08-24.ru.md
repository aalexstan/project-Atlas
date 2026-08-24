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
- Платные credentials и production-токены не использовались.
- Два предоставленных пользователем кандидата key проверены по одному разу; их значения намеренно не записываются.
- Выполнены безопасные GET-запросы к документированному endpoint текущей погоды; нагрузочное повторение не проводилось.
- Это остаётся auth probe, а не live-test и не доказательство корректного ответа forecast.

## Probe

Запрос без credentials:

`GET https://api.weatherapi.com/v1/current.json?q=Moscow`

Наблюдение: HTTP `401`, `0.176436 s`.

Сырой payload:

```json
{"error":{"code":1002,"message":"API key is invalid or not provided."}}
```

## Проверка предоставленных пользователем credentials

Два переданных пользователем значения проверены по одному разу. В Atlas они обозначены только как `key_a` и `key_b`; значения не сохраняются.

| Проверка | Форма запроса | HTTP | Время | Ответ |
|---|---|---:|---:|---|
| `key_a` | `GET https://api.weatherapi.com/v1/current.json?key=<redacted>&q=Moscow` | 401 | 0.181132 с | код ошибки `2006`, `API key is invalid.` |
| `key_b` | `GET https://api.weatherapi.com/v1/current.json?key=<redacted>&q=Moscow` | 401 | 0.318189 с | код ошибки `2006`, `API key is invalid.` |

В обоих случаях API вернул структурированную JSON-ошибку авторизации. Значения ключей не выводились, не коммитились и не сохранялись в репозитории.

## Finding

Запрос без key подтвердил границу аутентификации и структурированную JSON-ошибку. Два предоставленных значения также отклонены как недействительные. Эти проверки не подтверждают валидный запрос, response contract, квоту, rate-limit headers, freshness, accuracy или commercial use.

## Blocker полноценного live-test

Для валидного теста нужен действующий key, выданный разрешённому аккаунту. Atlas не должен регистрировать аккаунт или использовать key без явного разрешения владельца. После законного получения доступа нужно применить live-test template, проверить Terms of Service free-tier, зафиксировать разнообразные core claims и сохранить raw payload.

`live_tested` остаётся `false`; maturity остаётся `reviewed`.

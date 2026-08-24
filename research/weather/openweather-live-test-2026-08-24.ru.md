# Live-test OpenWeather API - 2026-08-24

[English version](openweather-live-test-2026-08-24.md)

## Цель

Проверить доступный пользователю current/forecast API OpenWeather и отдельно зафиксировать границу подписки One Call API 3.0. Это не проверка квоты, SLA, точности или лицензирования.

## Авторизация и безопасность

- Key предоставлен пользователем и не записывается в репозиторий.
- Платный credential или production secret не добавлялись в Atlas.
- Формальная серия состоит только из безопасных GET-запросов; квота не исчерпывалась и нагрузка не создавалась.
- До теста изучены официальные документация, pricing и FAQ OpenWeather.

## Core claims до теста

Список зафиксирован до формальной серии запросов.

| ID | Core claim | Ссылка в профиле | Почему это важно |
|---|---|---|---|
| C1 | OpenWeather предоставляет current и forecast weather data через JSON API с авторизацией API key. | `api.json` `authentication`, `best_for`, `sources` | Идентичность и основное назначение |
| C2 | Валидные запросы по координатам возвращают структурированный JSON с погодными полями. | `api.json` `sources`; официальная документация current/forecast | Основной response contract |
| C3 | Отсутствующие или ошибочные координаты дают структурированную ошибку, а не валидный weather result. | `api.json` `open_questions` | Безопасность интеграции |
| C4 | One Call API 3.0 является отдельной продуктовой/подписочной границей относительно current/forecast access. | `api.json` `best_for`, `pricing`; официальная страница One Call 3.0 | Коммерческий и access block |
| C5 | Quota, rate limits, SLA, pricing, accuracy, storage и licensing остаются provider-reported или unknown без отдельного подтверждения. | `api.json` `pricing`, `rate_limits`, `open_questions` | Procurement block |

## Среда теста

- Дата: 2026-08-24
- Клиент: `curl --silent --show-error --max-time 20`
- Координаты: Москва, `55.75, 37.62`
- Raw payloads: [openweather-live-test-2026-08-24-raw](openweather-live-test-2026-08-24-raw/)
- Key удалён из всех форм запросов.

## Формальные запросы

### 1. Current weather

`GET https://api.openweathermap.org/data/2.5/weather?lat=55.75&lon=37.62&appid=<redacted>&units=metric`

Наблюдение: HTTP `200`, `0.323996 с`, city `Moscow`, country `RU`. Структурированный JSON содержит `coord`, `weather`, `main`, `wind`, `clouds`, `sys` и связанные поля.

Raw payload: [current.json](openweather-live-test-2026-08-24-raw/current.json)

### 2. Five-day forecast endpoint

`GET https://api.openweathermap.org/data/2.5/forecast?lat=55.75&lon=37.62&appid=<redacted>&units=metric`

Наблюдение: HTTP `200`, `0.453430 с`, city `Moscow` и `40` трёхчасовых forecast entries в JSON.

Raw payload: [forecast.json](openweather-live-test-2026-08-24-raw/forecast.json)

### 3. Неверные координаты

`GET https://api.openweathermap.org/data/2.5/weather?lat=not-a-number&lon=37.62&appid=<redacted>&units=metric`

Наблюдение: HTTP `400`, `0.905995 с`, JSON error message `wrong latitude`.

Raw payload: [invalid-coordinate.json](openweather-live-test-2026-08-24-raw/invalid-coordinate.json)

## Boundary probe One Call API 3.0

`GET https://api.openweathermap.org/data/3.0/onecall?lat=55.75&lon=37.62&appid=<redacted>&units=metric&exclude=minutely,alerts`

Наблюдение: HTTP `401`, `0.171492 с`, структурированное сообщение: для One Call 3.0 требуется отдельная подписка One Call by Call. Это finding о доступе и границе продукта, а не доказательство недействительности key: тот же key вернул HTTP 200 для current weather.

Raw payload: [onecall-3-boundary.json](openweather-live-test-2026-08-24-raw/onecall-3-boundary.json)

## Наблюдение rate limits

Ограниченная серия не приближалась к квоте намеренно. HTTP 429 или Retry-After не использовались для вывода о лимите. Quota, rate limits, SLA, accuracy, pricing и licensing остаются unknown или provider-reported.

## Решение

Key действителен для проверенного current-weather endpoint. One Call API 3.0 недоступен в текущем access, поскольку требует отдельную подписку. В профиле нужно разделять current/forecast access и One Call 3.0.

Maturity остаётся `reviewed`; live evidence не повышает профиль до `verified`. Срок действия evidence: `2026-11-22` по 90-дневному cadence для access/limits.

См. [процедурное ревью](../../reviews/openweather-live-test-2026-08-24.md).

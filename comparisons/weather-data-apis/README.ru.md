# API погодных и метеоданных

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Последняя проверка | 2026-08-24 |
| Кандидаты | Open-Meteo, WeatherAPI.com, OpenWeather |
| Live testing | Ограниченные тесты проведены для всех трёх кандидатов; см. evidence status |

## Краткая матрица выбора

| Сценарий | Первичный shortlist | Почему |
|---|---|---|
| Некоммерческий прототип | Open-Meteo | Явный free non-commercial route и open-data model. |
| Широкий self-service weather API | WeatherAPI.com | Публичные планы, current/forecast/history/location и air quality. |
| Глобальный commercial product family | OpenWeather | Несколько current, forecast, historical и environmental продуктов. |

## Матрица

| Критерий | Open-Meteo | WeatherAPI.com | OpenWeather |
|---|---|---|---|
| Current weather | **Observed 2026-08-24**: public forecast response вернул current fields ([raw evidence](../../research/open-meteo-api/live-test-2026-08-24.ru.md)) | **Observed 2026-08-24**: HTTP 200 JSON с current data Москвы ([raw evidence](../../research/weatherapi-com-api/live-test-2026-08-24.ru.md)) | **Observed 2026-08-24**: HTTP 200 JSON с current data Москвы ([raw evidence](../../research/weather/openweather-live-test-2026-08-24.ru.md)) |
| Forecast | **Observed 2026-08-24**: coordinate forecast JSON | **Observed 2026-08-24**: `days=3` вернул три forecast days | **Observed 2026-08-24**: 40 трёхчасовых forecast entries |
| Historical | **Observed 2026-08-24**: archive route вернул historical JSON | **Provider-reported**: historical data — forecast archive; live-test не проводился | **Unknown**: historical route не тестировался |
| Search/geocoding | **Observed 2026-08-24**: geocoding lookup вернул Moscow | **Observed 2026-08-24**: search вернул два результата Moscow | **Unknown**: в этот live-test не входило |
| API key | **Observed**: проверенные public routes работали без key | **Observed 2026-08-24**: authorized key принят | **Observed 2026-08-24**: authorized key принят для API 2.5 |
| Invalid input | **Observed 2026-08-24**: HTTP 400 JSON error для неверных координат | **Observed 2026-08-24**: HTTP 400 code 1003 для пустого `q`; похожий на неизвестный текст разрешился в нерелевантную локацию, это открытый accuracy finding | **Observed 2026-08-24**: HTTP 400 `wrong latitude` |
| Публичная цена | **Provider-reported**: free non-commercial; paid customer API | **Provider-reported**: public plans | **Provider-reported**: product-specific plans |
| Free allowance | **Provider-reported**: 10K calls/day, non-commercial | **Provider-reported**: 100K calls/month free plan | **Unknown/provider-reported**: current/forecast и One Call allowances различаются по продукту |
| Commercial licence | **Provider-reported**: нужен customer endpoint | **Unknown/provider-reported**: plan/terms требуют проверки | **Unknown/provider-reported**: зависит от product/plan |
| SLA | **Unknown**: отсутствие free-tier uptime guarantee не является проверкой SLA | **Unknown** в этом исследовании | **Unknown** в этом исследовании |
| Rate limits | **Unknown/provider-reported**: 429 в ограниченном тесте не было | **Unknown/provider-reported**: 429 в ограниченном тесте не было | **Unknown/provider-reported**: 429 в ограниченном тесте не было |
| One Call / timeline access | **Not applicable** | **Not applicable** | **Observed 2026-08-24**: One Call API 3.0 вернул HTTP 401 с требованием подписки |
| Evidence status | [Observed live-test](../../research/open-meteo-api/live-test-2026-08-24.ru.md); commercial claims остаются reported/unknown | [Observed live-test](../../research/weatherapi-com-api/live-test-2026-08-24.ru.md); поведение `current_fields` остаётся открытым | [Observed live-test](../../research/weather/openweather-live-test-2026-08-24.ru.md); доступ One Call 3.0 заблокирован подпиской |

Правило evidence: `Observed 2026-08-24` означает только, что указанная форма запроса и поведение ответа реально увидены в live-test репозитории. `Provider-reported` означает claim из официальной документации или pricing. `Unknown` означает, что claim не установлен. Наблюдение endpoint не доказывает quota, SLA, accuracy, pricing, licence или production suitability.

Погодные API нельзя сравнивать только по числу forecast days или цене вызова. Нужен benchmark координат, горизонтов, переменных, freshness, actual-vs-model semantics и legal rights.

См. [need-маршрут](../../needs/weather-data/README.ru.md) и [procurement kit](../../procurement/weather-api-selection/README.ru.md).

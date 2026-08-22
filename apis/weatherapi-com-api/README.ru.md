# API WeatherAPI.com

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-22 |
| Класс продукта | Commercial weather API |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** широкого API текущей погоды, forecast, historical, air quality, location и alerts с публичными тарифами.

**Не подходит без проверки, если:** нужны фактические исторические наблюдения: поставщик описывает historical data как архив forecast data.

## Технический доступ

| Поле | Значение |
|---|---|
| Base URL | В документации указан `http://api.weatherapi.com/v1`; для production проверять HTTPS |
| Формат | JSON/XML |
| Аутентификация | API key |
| Возможности | Current, forecast, history, future, marine, air quality, autocomplete и др. |
| Планы | Free, Starter, Pro+, Business, Enterprise |
| Free plan | 100K calls/month, 3-day forecast, 1-day history по странице тарифов |

## О тарифах

Официальная страница публикует цены и allowances планов. Это цены планов поставщика, а не гарантия полной стоимости storage, bandwidth, redistribution, support или custom workload.

## Рекомендация

Использовать для широкого API и public self-service onboarding. До применения в страховании, логистике или регулируемых решениях подтвердить semantics historical, commercial rights, SLA и regional quality.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/weather/2026-08-22-weatherapi.ru.md).

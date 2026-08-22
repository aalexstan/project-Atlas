# Исследование WeatherAPI.com

[English version](2026-08-22-weatherapi.md)

## Область проверки

Проверка current, forecast, historical, location, air-quality и связанных API WeatherAPI.com.

## Подтверждённые факты

- WeatherAPI.com документирует JSON/XML REST с API key.
- Описаны current weather, forecast, historical, future weather, marine, air quality, search/autocomplete и alerts.
- На официальной странице тарифов опубликованы планы, call allowances, historical windows и forecast horizons.
- Historical data описаны как архив forecast data, а не фактические наблюдения.

## Неизвестные параметры

- Storage, redistribution, SaaS, attribution, SLA и support для конкретного плана.
- Accuracy и состав station/model для нужного региона России.
- Подходит ли allowance плана для batch и customer-facing workload.

## Live testing

Не проводился.

## Решение

Создать reviewed профиль, отделяя provider-reported features от независимого quality benchmark.

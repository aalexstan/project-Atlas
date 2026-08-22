# Решение по 2GIS Suggest и Places

[English version](2gis-suggest-places-decision.md)

## Решение

Создать два отдельных активных профиля:

- `apis/2gis-suggest-api/`
- `apis/2gis-places-api/`

## Обоснование

Официальная документация 2GIS разделяет Suggest API, Places API и Geocoder API. Suggest отвечает за подсказки при вводе, Places — за поиск организаций, зданий и мест, Geocoder — за преобразование адресов и координат.

## Границы

- `2gis-suggest-api`: autocomplete и UX подсказок, включая адресные, уличные, объектные и route-endpoint подсказки.
- `2gis-places-api`: поиск организаций, зданий и мест, включая возможные платные on-demand поля и методы.
- `2gis-geocoder-api`: прямое и обратное геокодирование.

## Закупочное ограничение

Профили reviewed, но не live-tested. Для кэширования, хранения, SaaS use, redistribution, attribution и on-demand полей нужен договорный review.

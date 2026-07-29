# Решение по Yandex Maps Organization Search API

[English version](yandex-organization-search-decision.md)

## Решение

Создать активный API-first profile:

- `apis/yandex-maps-organization-search-api/`

## Обоснование

Официальные источники Yandex Maps API дают достаточно evidence для поддерживаемой карточки Atlas:

- official product identity;
- official product purpose;
- public documentation;
- endpoint;
- API-key authentication;
- request and response references;
- public commercial terms and request packages;
- public technical rate-limit statement.

## Граница продукта

Рассматривать API как продукт поиска организаций, мест и geographic objects.

Не считать его:

- address autocomplete;
- address cleaning or normalization;
- registry-quality address validation;
- заменой direct/reverse geocoder profile Яндекса;
- routing, matrix или ETA product.

## Основные blockers

- Public SLA не найден.
- OpenAPI/Swagger не найден.
- Storage/data-use rights требуют contract review, особенно потому что просмотренные официальные публичные страницы различаются в формулировках Basic/Advanced или storage-capable license.
- Batch/offline enrichment rights не подтверждены.
- Atlas live testing или quality benchmark не проводились.

## Как включать в comparison

Добавить Yandex Organization Search как Yandex ecosystem alternative к 2GIS Places API для organization/place search. Не объявлять победителя без общего benchmark, contract-rights review и сопоставимых pricing assumptions.

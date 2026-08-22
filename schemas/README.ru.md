# Схемы данных Atlas

[English version](README.md)

Эти схемы описывают машинный контракт активных записей Atlas.

## Контракты

- [Схема API profile](api-profile.schema.json) - один ограниченный API или integration route.
- [Схема comparison](comparison.schema.json) - сценарное сравнение вариантов.
- [Схема need](need.schema.json) - маршрут от пользовательской задачи.

Все активные записи используют `schema_version: 1`. Валидатор репозитория проверяет поля, которые можно проверить без сторонней JSON Schema-библиотеки. Неизвестные сведения поставщика остаются явными значениями `unknown`, `needs_recheck` или `not_applicable`.

Старые JSON в `legacy/`, `catalog/`, `companies/`, `datasets/`, `providers/` и `access_methods/` не входят в эти активные контракты.

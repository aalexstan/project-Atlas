# Решение по Nominatim

[English version](nominatim-decision.md)

## Решение

Создать профиль `apis/nominatim-geocoder-software/`.

## Обоснование

У Nominatim есть официальная документация, политика использования публичного сервиса OSMF и документация self-hosting. Граница продукта — software/data infrastructure, а не обычный hosted paid API.

## Границы

- Публичный сервис OSMF: ограниченное использование, инициированное конечным пользователем, по политике Nominatim.
- Self-hosted Nominatim: возможный маршрут, если команда готова обслуживать импорт OSM, обновления, инфраструктуру и compliance.
- Коммерческие провайдеры: отдельный procurement route, не оценивался в этом профиле.

## Закупочное ограничение

Не используйте публичный Nominatim для autocomplete, bulk geocoding, API resale или основной production-зависимости. Для production нужно оценивать self-hosting или коммерческого провайдера с явными SLA и юридическими условиями.

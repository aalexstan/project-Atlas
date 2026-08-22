# Повторная проверка API закупок и тендеров — 2026-08-22

[English version](2026-08-22-eis-seldon-recheck.md)

## Область

Проверка, достаточно ли официальных данных для активных reviewed-профилей ЕИС и Seldon.Tenders.

## Проверенные официальные источники

- [Казначейство России: ЕИС](https://roskazna.gov.ru/gis/eis-zakupki-gov-ru)
- [Казначейство России: форматы информационного взаимодействия](https://roskazna.gov.ru/gis/ehlektronnyj-byudzhet/formaty-informacionnogo-vzaimodejstviya)
- [Техническая информация ЕИС](https://zakupki.gov.ru/epz/main/public/document/view.html?sectionId=1252)
- [API Seldon 1.7](https://seldongroup.ru/system/1.7/api)
- [Обзор интеграции Seldon API](https://seldongroup.ru/system/api)

## Подтверждённые факты

- Казначейство описывает ЕИС / `zakupki.gov.ru` как официальный сайт свободного доступа к информации о закупках и формирования, обработки и хранения этой информации.
- В официальной навигации Казначейства есть разделы форматов взаимодействия и технической информации для внешних систем.
- Seldon описывает `API.Seldon.Tenders` как веб-сервис программного доступа к данным о закупках и интеграции с CRM.
- На официальной странице Seldon перечислены извещения, протоколы, контракты и документы, а получение описано по номеру извещения или настроенным фильтрам.
- Seldon описывает order-based delivery: клиент заказывает расчёт фильтров и позднее получает результат. Это не доказывает REST, GraphQL, webhook или streaming semantics.

## Неизвестные параметры и блокеры

- Для ЕИС не подтверждены endpoint catalog, machine-to-machine authentication, схемы, versioning, quotas, rate limits, support и права использования.
- Для Seldon не подтверждены endpoint catalog, authentication, response schemas, versioning, production limits, SLA, API-specific price и права хранения/redistribution.
- Credentials, API calls, FTP listing, ingestion pipeline и live benchmark не выполнялись.

## Решение

Создать reviewed-профили обоих маршрутов с явными product classes: официальный государственный data integration и коммерческий агрегированный procurement API. Создать сценарное сравнение без объявления победителя и без повышения профилей до fully verified.


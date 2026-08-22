# Сервис доступа к ЕГРН Росреестра

[English version](README.md)

> Официальный маршрут запроса сведений ЕГРН. Карточка намеренно не названа универсальным REST API.

## Вывод

Используйте этот маршрут, когда нужна официальная выписка ЕГРН или когда регулярные выписки оправдывают оценку пакетного доступа по ключу.

Не используйте frontend-запросы публичной кадастровой карты как замену. Поиск по карте, слой НСПД и юридически значимая выписка ЕГРН - разные продукты.

## Модель доступа

Official material подтверждает единичные запросы и сервис `Запрос посредством доступа к ФГИС ЕГРН`, access key и предоплаченные пакетные операции сроком один год. Полный unattended API flow, base URL и method catalog для обычной commercial organization не подтверждены.

## Коммерческая граница

Official publication 2025 года указывала диапазон 116-290 RUB за пакетную выписку. Это evidence пакетной модели, а не current universal API price. Перед закупкой нужно уточнить категорию заявителя, тип выписки, пакет, цену и срок.

## Главные риски

- неясна current automation/authentication mechanics;
- нет публичных quotas, rate limits и SLA;
- restricted information зависит от legal grounds;
- storage, customer display, SaaS и redistribution требуют письменной проверки;
- live test и платная выписка не выполнялись.

См. [evidence](evidence.ru.md), [сравнение](../../comparisons/real-estate-cadastral-data/README.ru.md) и [маршрут задачи](../../needs/real-estate-cadastral-data/README.ru.md).

# 2GIS Geocoder API

[English version](README.md)

> API прямого и обратного геокодирования в семействе 2GIS Search API.

## Статус исследования

| Поле | Значение |
|---|---|
| Уровень | Reviewed |
| Последняя проверка | 2026-07-29 |
| Поставщик | 2GIS |
| Статус продукта | Active |
| Live credential test | Не проводился |

## Краткий вывод

**Лучше всего подходит для:** продуктов вокруг карт и каталога 2GIS, reverse geocoding по клику на карте и геокодирования с публичными пакетными ценами.

**Не подходит, когда:** нужна реестровая нормализация адресов, поиск организаций через геокодер, неограниченное offline-хранение или bulk enrichment без подтверждения договора.

**Итог:** 2GIS Geocoder - документированный HTTP JSON геокодер с публичными пакетами и demo key. Не стоит растягивать его на Places или Suggest: это отдельные продукты, которые нужно покупать и оценивать отдельно.

## Граница продукта

Эта карточка покрывает:

- прямое геокодирование по адресу/названию;
- обратное геокодирование по координатам;
- request/response модель 2GIS Geocoder API.

Связанные, но отдельные продукты:

- [`2GIS Places API`](../2gis-places-api/README.ru.md) ищет организации, здания и места;
- [`2GIS Suggest API`](../2gis-suggest-api/README.ru.md) даёт подсказки ввода;
- навигационные API отвечают за маршруты, матрицы и изохроны.

## Сценарии

| Сценарий | Fit | Почему |
|---|---|---|
| Показать известный адрес на карте 2GIS | Strong | Прямое геокодирование - основной сценарий Geocoder API. |
| Получить адрес по клику на карте | Strong | Обратное геокодирование по координатам документировано. |
| Продукт уже использует 2GIS Platform | Strong | Общий Platform Manager/key/subscription model. |
| Поиск организаций и мест | Medium только с Places API | Сам Geocoder не является продуктом поиска каталога. |
| Подсказки адреса | Medium только с Suggest API | Suggest - отдельный сервис. |
| Официальная валидация адреса РФ | Weak | Geocoder matching не равен проверке по ГАР. |
| Offline enrichment базы | Weak до подтверждения договора | Права хранения и кэширования зависят от контракта. |

## Технический доступ

| Поле | Значение |
|---|---|
| Протокол | HTTP GET |
| Endpoint | `https://catalog.api.2gis.com/3.0/items/geocode` |
| Аутентификация | API key в query-параметре `key` |
| Direct request | `q=<address>` |
| Reverse request | `lat=<latitude>&lon=<longitude>` |
| Формат ответа | JSON |
| API reference | Публичная документация есть |
| OpenAPI / Swagger | Не найден в публичных docs |
| Deployment | Cloud public endpoints; поставщик сообщает об On-Premise варианте с оговорками |

## Цены и лимиты

| Пункт | Подтверждённое значение | Статус |
|---|---|---|
| Demo key | Доступен на один месяц | verified |
| Demo Search limit | 1 000 общих запросов Search services | verified |
| Geocoder package 10 000 units/month | 4 700 руб. | verified |
| Geocoder package 100 000 units/month | 21 000 руб. | verified |
| Geocoder package 1 000 000 units/month | 70 000 руб. | verified |
| Лимит Search services | 600 units/minute | verified |
| Billing unit | Успешные API requests | verified |
| Публичный SLA | Не найден в просмотренных docs | unknown |

Некоторые поля, включая отдельные FIAS/FNS/OKATO/OKTMO и данные зданий, описаны как платный доступ on demand.

## Коммерческие и правовые заметки

- Официальный Search overview говорит, что часть информации об объектах доступна только on demand и за дополнительную стоимость.
- Оферта WebAPI делает хранение, кэширование, модификацию, распространение и использование вне договора закупочным blocker.
- Каталог 2GIS обновляется ежемесячно по документации поставщика; Atlas не измерял freshness независимо.

## Альтернативы

| Альтернатива | Когда лучше | Главный trade-off |
|---|---|---|
| [`DaData Address APIs`](../dadata-address-api/README.ru.md) | Центральны российские подсказки и стандартизация адресов | Прямое геокодирование оплачивается per-record и ориентировано на РФ. |
| [`2GIS Suggest API`](../2gis-suggest-api/README.ru.md) | Нужен autocomplete 2GIS перед geocoding или place lookup | Suggestions не являются geocoding. |
| [`2GIS Places API`](../2gis-places-api/README.ru.md) | Нужны организации, здания и места | Place search не является address validation. |
| [`Yandex Maps Geocoder API`](../yandex-maps-geocoder-api/README.ru.md) | Продукт основан на показе и лицензировании Яндекс Карт | Бесплатное использование жёстко привязано к показу на Яндекс Картах. |
| [`FIAS/GAR Data Integration`](../fias-gar-data-integration/README.ru.md) | Нужна собственная официальная адресная база РФ | Требует ETL/search инфраструктуры и не является turnkey geocoder. |

## Рекомендация по сценарию

Выбирайте 2GIS Geocoder, когда приложение уже использует карты или каталог 2GIS и геокодирование является частью этой карты. Если нужны поиск организаций, подсказки адреса или маршрутизация, оценивайте соответствующий продукт 2GIS отдельно.

## Доказательства

См. [`evidence.ru.md`](evidence.ru.md).

## История изменений

См. [`changes.ru.md`](changes.ru.md).

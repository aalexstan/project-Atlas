# Access Methods Index

Статус: **Legacy / supporting research**

Этот индекс сохранен как access-method слой Pass #2. В активной API-first модели технический доступ описывается внутри API profile.

Дата обновления: 2026-06-23
Статус: access-method слой Pass #2

## Карты доступа по Dataset

| Dataset | Файл | Подтвержденные способы доступа |
|---|---|---|
| Метаданные каталога API | `api_catalog_metadata_access.md` | веб-каталог |
| Реестр компаний и контрагентов | `company_registry_access.md` | REST API; заявка/партнерство требует проверки |
| Закупки, тендеры и контракты | `procurement_tender_contracts_access.md` | REST API; получение массивом/по номеру |
| Открытые городские данные Москвы | `moscow_city_open_data_access.md` | Open Data; REST API; веб-портал |
| Адресный реестр России | `russian_address_registry_access.md` | REST API; облачный доступ |

## Нормализация

Этот слой отделяет способ получения от Dataset. Например, `Реестр компаний и контрагентов` может быть доступен через ГЛОБАС.API, Seldon.Basis, партнерскую заявку или прямую работу с первичными официальными источниками, если такие источники будут установлены позже.

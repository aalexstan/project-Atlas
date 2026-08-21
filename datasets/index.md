# Datasets Index

Статус: **Legacy / supporting research**

Этот индекс сохранен как dataset-centric слой Pass #2. В активной API-first модели Dataset описывает покрытие и происхождение данных, но главная публичная сущность Atlas — API profile.

Дата обновления: 2026-06-23
Статус: dataset-centric индекс Pass #2

## Найденные Dataset

| Dataset | Файл | Известные поставщики | Известные API / каналы |
|---|---|---|---|
| Метаданные каталога API | `api_catalog_metadata.md` | API Portal / RNDSOFT | веб-каталог API Portal; API самого каталога не найден |
| Реестр компаний и контрагентов | `company_registry.md` | Legacy: Credinform, Seldon; active comparison also covers DaData, Kontur.Focus, FTS and GLOBAS.API | Active route: `comparisons/company-counterparty-data-russia/`; old API Portal claims preserved as provenance |
| Закупки, тендеры и контракты | `procurement_tender_contracts.md` | Legacy: Seldon; primary-source candidates require future research | Seldon.Tenders kept legacy-only by `research/seldon-tenders/decision.md`; future procurement API comparison not created yet |
| Открытые городские данные Москвы | `moscow_city_open_data.md` | Правительство Москвы; official docs accessible, but operational/API-rights blockers remain | Moscow Open Data API kept legacy-only by `research/moscow-open-data-api/decision.md`; no active profile until API key flow, limits, SLA and operational terms are clarified |
| Адресный реестр России | `russian_address_registry.md` | ФНС России / ФИАС/ГАР; legacy `kladr-api.ru` source-risk note сохранен | Active route: `apis/fias-gar-data-integration/`; legacy API Portal/`kladr-api.ru` claim не считается официальным источником |

## Что изменилось после Pass #2

Первый проход отвечал на вопрос `какие API найдены`. Этот слой отвечает на вопрос `какие данные найдены`.

API теперь рассматривается как один из способов доступа к Dataset. Один Dataset может иметь несколько поставщиков и несколько способов доступа. Один поставщик может продавать или агрегировать несколько Dataset.

## Dataset пока не хватает

Ниже не утверждается, что данные найдены. Это направления, которые отсутствуют в текущей базе и требуют отдельного исследования:

- Цены на топливо.
- Справочник АЗС.
- Дорожный трафик и пробки.
- Погода и метеоистория.
- История транспортных средств.
- Недвижимость и кадастровые данные.
- Платежи и финтех-транзакции.
- Маркетинговые и телекоммуникационные аудитории.
- Доставка, логистика и курьерские события.
- Маркетплейсы и товарные каталоги.
- Судебные, санкционные и исполнительные данные.
- Медицинские и телемедицинские данные.

## Практически не исследованные направления

- Лицензии и права повторного использования.
- Форматы выгрузки кроме REST API.
- Полные схемы полей.
- Частота обновления каждого Dataset.
- Первичные владельцы данных.
- Альтернативные поставщики по каждому Dataset.
- Условия хранения, перепродажи, SaaS и обучения ИИ.

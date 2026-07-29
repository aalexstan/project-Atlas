# Dataset: Закупки, тендеры и контракты

Дата исследования: 2026-06-23
Статус: мигрировано из Pass #1

## API-first migration note

Дата связки: 2026-07-29

Эта dataset-centric карточка сохранена как **Legacy / supporting research** для будущего comparison по procurement/tender/contract APIs. Активная API-first карточка Seldon.Tenders пока не создана.

Текущий вывод Atlas: официальные страницы Seldon подтверждают `API.Seldon.Tenders` как procurement-data integration route / extended functionality Seldon 1.7, но публичных доказательств endpoint catalog, authentication, schemas, limits, SLA, API pricing и data-use rights недостаточно для активного API profile. Решение сохранено в:

- `research/seldon-tenders/decision.md`
- `research/seldon-tenders/decision.ru.md`

Старые утверждения API Portal и домен `api-seldon.ru` ниже сохранены как provenance/source-risk note. Их нельзя использовать как текущий официальный источник без повторной проверки на официальных материалах `seldongroup.ru` или письменного ответа поставщика.

## Название

Закупки, тендеры и контракты.

## Описание

Набор данных о государственных и коммерческих торгах, извещениях, протоколах, контрактах, участниках, победителях, документах и конкурентной активности. В первом проходе найден через API Seldon.Tenders.

## Какие именно данные входят

Подтвержденные данные:

- Государственные торги.
- Коммерческие торги.
- Извещения: основные сведения о процедуре и условиях проведения.
- Протоколы: итоги процедур, участники и ценовые предложения.
- Контракты: информация о заключенных контрактах.
- Активность компании в торговых процедурах с учетом роли организации.
- Ссылки на закупочную документацию.
- Ссылки на технические задания.
- Ссылки на протоколы.
- Ссылки на контракты.
- Рекомендованные процедуры с высокой вероятностью победы клиента.
- Подбор поставщиков: компании, поставляющие закупаемый товар или оказывающие нужную услугу.
- Данные об участниках торгов.
- Данные о победителях торгов.
- Архивные данные для маркетинговых и отраслевых исследований.
- Данные для анализа конкурентной среды по тендерам, в которых участвуют конкуренты.
- Более 7000 официальных источников, по описанию API Portal.

Не подтверждено:

- Полный перечень источников торгов.
- Географическое покрытие.
- Полный список фильтров.
- История хранения.
- Форматы ответа.

## Кто является владельцем данных

- Seldon владеет или распространяет агрегированный слой.
- Первичные данные принадлежат государственным и коммерческим площадкам/источникам.

## Кто собирает данные

Seldon агрегирует данные из официальных источников.

## Кто распространяет

Seldon через API Seldon.Tenders.

## Частота обновления

API Portal указывает получение данных в real time. Точные SLA и частота обновления не найдены.

## Коммерческие ограничения

- Коммерческое использование: неизвестно.
- Хранение данных: неизвестно.
- Перепродажа: неизвестно.
- Использование в SaaS: неизвестно.
- Использование для обучения ИИ: неизвестно.

## Открытость

Коммерческий агрегированный Dataset. Первичные источники частично могут быть открытыми, но конкретный перечень и условия не найдены.

## Качество

- Высокая прикладная ценность из-за объектов закупок, контрактов, участников и документов.
- Полнота выглядит высокой по описанию `более 7000 официальных источников`, но это не проверено независимо.
- Качество невозможно подтвердить без списка источников и схемы данных.

## Надежность

Средняя. Dataset перспективен, но документация Seldon и условия использования требуют проверки.

## Известные поставщики

- Seldon.

## Известные API

- API Seldon.Tenders.

## Альтернативные способы получения

- REST API: подтверждено по API Portal.
- Получение массивом по критериям: подтверждено в карточке API Portal.
- Получение индивидуально по номеру извещения/контракта: подтверждено в карточке API Portal.
- Первичные официальные источники: указаны как класс источников, но конкретный список не найден в этой legacy-карточке.
- Active decision memo: `research/seldon-tenders/decision.md` сохраняет Seldon.Tenders как legacy-only до появления official specification/auth/pricing/rights evidence.
- Future active route: procurement/tender API comparison should be created only after reviewing official primary sources for candidate products and government registries.
- Current baseline: `research/procurement-tender/2026-07-29-official-source-baseline.md` and `research/procurement-tender/decision.md` keep this direction in research backlog until EIS service docs, Seldon API evidence and data-rights details are available.
- CSV, XML, FTP, Webhook, GraphQL: не найдено.

## Неизвестные места

- Актуальная официальная документация Seldon.Tenders.
- Полный список источников.
- География.
- Лицензии и ограничения на повторное использование.
- Стоимость масштабирования.
- Форматы ответа и лимиты.

## Риски

- Риск устаревшей ссылки документации `api-seldon.ru`.
- Лицензионный риск на повторное использование данных первичных площадок.
- Риск зависимости от одного коммерческого агрегатора.
- Риск создания active API profile только по API Portal summary без endpoint/auth/schema evidence.
- Риск смешивания web-product Seldon.Tenders/Seldon.Win и `API.Seldon.Tenders` integration route.
- Риск сравнения procurement/tender products без одинакового source list, field matrix, retention rights и commercial quote.

## Связанные старые карточки

- `catalog/api-seldon-tenders.md`
- `companies/seldon.md`
- `research/documentation-link-risk.md`
- `ratings/initial_ratings.md`

## Связанные активные и исследовательские материалы

- `research/seldon-tenders/2026-07-29.md`
- `research/seldon-tenders/decision.md`
- `research/seldon-tenders/decision.ru.md`
- `research/procurement-tender/2026-07-29-official-source-baseline.md`
- `research/procurement-tender/decision.md`
- `research/procurement-tender/decision.ru.md`
- `apis/seldon-basis/README.md`
- `comparisons/company-counterparty-data-russia/README.md`

## Источники

- https://apiportal.ru/catalog/api-seldon.tenders/
- http://www.api-seldon.ru/

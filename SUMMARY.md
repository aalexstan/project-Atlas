# Summary

Дата обновления: 2026-07-29
Статус: API-first foundation integrated; legacy dataset research retained

## Активное направление Atlas

Главная публичная сущность Project Atlas теперь **API profile**.

Atlas должен помогать проверять, сравнивать и выбирать API для конкретных задач. Dataset-слой сохраняется, но теперь используется как supporting research: он помогает понимать покрытие данных, происхождение источников, риски лицензий и исторический контекст.

Активная методика находится в `docs/`:

- `docs/PRINCIPLES.md` / `docs/PRINCIPLES.ru.md`
- `docs/METHODOLOGY.md` / `docs/METHODOLOGY.ru.md`
- `docs/MIGRATION.md` / `docs/MIGRATION.ru.md`
- `docs/VISION.md` / `docs/VISION.ru.md`

## Активные API-first материалы

| Материал | Количество | Комментарий |
|---|---:|---|
| API profiles | 5 | DaData, FTS EGRUL/EGRIP integration, GLOBAS.API, Kontur.Focus API, Seldon.Basis API |
| Comparisons | 1 | Company and counterparty data APIs in Russia |
| Procurement kits | 1 | Counterparty API selection kit |
| API indexes | 2 | English and Russian |
| Comparison indexes | 2 | English and Russian |
| Active templates | 4 | API card and comparison templates in English and Russian |

## Активные API profiles

| API | Maturity | Last verified | Live test |
|---|---|---|---|
| DaData API | reviewed | 2026-07-23 | not performed |
| FTS EGRUL/EGRIP Data Integration | reviewed | 2026-07-23 | not performed |
| GLOBAS.API | reviewed | 2026-07-28 | not performed |
| Kontur.Focus API | reviewed | 2026-07-23 | not performed |
| Seldon.Basis API | reviewed | 2026-07-23 | not performed |

## Legacy / Supporting Research

Сохранены старые исследовательские слои:

- `datasets/` - 5 dataset-карточек Pass #2.
- `providers/` - старый слой поставщиков данных.
- `access_methods/` - старый слой способов доступа к Dataset.
- `relationships/` - граф Dataset -> Provider -> Access Method.
- `catalog/` - исторические API-centric карточки Pass #1.
- `companies/` - исторические карточки компаний Pass #1.
- `research/` и `reports/` - журналы и отчеты старых проходов.
- `ratings/` - Legacy / Pre-methodology; не является действующим Atlas Score.
- старые dataset/provider/access/source templates - legacy formats.

Исходный dataset-centric корневой README сохранен как `legacy/README.dataset-centric-2026-06-23.md`.

## Важные решения миграции

- API Portal остается полезным discovery source, но не считается final source of truth.
- История проверки домена `api-seldon.ru` сохранена как исторический риск источника.
- Активная карточка Seldon.Basis связана с официальными источниками `seldongroup.ru`.
- Цены веб-версий не используются как цены API.
- Старые числовые рейтинги не пересчитывались и не повышались до действующей методики.
- Excel workbook procurement kit добавлен как binary artifact и не редактировался.
- ГЛОБАС.API восстановлен из legacy backlog как активный API-first profile на основе официальных страниц Credinform; REST claim из API Portal сохранен только как legacy provenance.

## Нерешенные вопросы

- Нужны credentialed live tests для API profiles.
- Для Kontur и Seldon нужны коммерческие предложения, production limits, SLA и права хранения/redistribution.
- Для DaData нужны benchmark качества, latency и legal confirmation по конкретным сценариям хранения.
- Для FTS нужно перепроверить поведение после перехода форматов 2026-08-01.
- Для ГЛОБАС.API нужны specification, endpoint catalog, authentication, schemas, limits, SLA, API-specific pricing и data-use rights от Credinform.
- Legacy-карточки Seldon.Tenders, Moscow Open Data API и address/FIAS layer требуют отдельной API-first миграции или decision memo.

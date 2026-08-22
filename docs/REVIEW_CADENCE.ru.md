# Регламент пересмотра

[English version](REVIEW_CADENCE.md)

Этот policy превращает правила пересмотра из методологии в рабочую модель поддержки материалов Atlas.

## Область действия

Применяется к активным материалам:

- API profiles в `apis/`;
- comparisons в `comparisons/`;
- need routes в `needs/`;
- procurement kits в `procurement/`;
- templates и validation scripts, если они влияют на публичные материалы.

Legacy-материалы сохраняют provenance value, но не требуют такого же cadence, если они не мигрируются в active API-first work.

## Интервалы пересмотра

| Область | Целевой интервал | Почему |
|---|---:|---|
| Pricing and billing units | 90 дней | Цены, пакеты, free tiers и overage rules быстро меняются. |
| Public limits and quotas | 90 дней | Rate limits и plan limits могут меняться без крупных product announcements. |
| Product availability and official identity | 90 дней | API могут переименовываться, переноситься, закрываться или входить в другой продукт. |
| Documentation, methods and versioning | 180 дней | Specifications, fields и examples меняются, но обычно реже тарифов. |
| Legal terms and data rights | 180 дней | Storage, caching, display, redistribution и SaaS rights критичны для закупки. |
| Comparisons and need routes | 180 дней | Scenario recommendations зависят от актуальности связанных profiles. |
| Gold profiles | минимум 90 дней | Gold означает поддерживаемый reference, а не разовый review. |

Известные внешние даты важнее таблицы. Например, переход форматов ФНС EGRUL/EGRIP, запланированный на 2026-08-01, требует targeted recheck после этой даты.

Автоматическая проверка использует кратчайший общий интервал 90 дней для API profiles, 180 дней для comparisons и needs, а также более раннюю корректную дату `next_review`, если она задана.

## Триггеры пересмотра

Пересматривайте материал сразу, если произошло одно из событий:

- поставщик объявил изменения pricing, product, legal terms, API version или endpoints;
- official documentation URL изменился или перестал открываться;
- profile получил provider answer, sandbox, quote или contract appendix;
- появилось live testing evidence;
- API попал в новое comparison или need route;
- изменились validator, generator или template rules;
- legacy claim повышается до active profile.

## Модель владельцев

Atlas использует ролевое ownership, а не персональное, если maintainer явно не назначил людей вне этого репозитория.

| Роль | Ответственность |
|---|---|
| Research owner | Проверяет official sources, обновляет evidence, следит за точностью `last_verified`. |
| Editorial owner | Поддерживает scenario recommendations, English/Russian parity и аккуратные source-status формулировки. |
| Technical owner | Поддерживает JSON validity, generated indexes, validator rules и link health. |
| Procurement owner | Ведет provider-request checklists, quotes, SLA/support evidence и commercial blockers. |
| Legal reviewer | Проверяет storage, caching, display, redistribution, SaaS, affiliate и model-training rights. |

Если роль не назначена, пишите `unassigned` в working notes или backlog. Не выдумывайте человека или организацию.

## Review states

Используйте эти states в TODO, changelog или working notes:

- `on_schedule` - пересмотр ещё не наступил;
- `due` - целевая дата пересмотра наступила;
- `overdue` - пересмотр просрочен;
- `blocked_provider` - нужен ответ поставщика, quote или private documentation;
- `blocked_credentials` - нужен законный test access;
- `blocked_legal` - нужен legal или contract review;
- `blocked_source` - официальный источник недоступен или неполон;
- `legacy_only` - материал сохранён для provenance, не для активной методики;
- `superseded` - заменён более новым active route.

## Обновление дат

Обновляйте `last_verified` только после повторной проверки relevant official или primary source для утверждаемого факта.

Не обновляйте `last_verified` из-за:

- copy edits;
- navigation changes;
- создания provider-request checklist;
- правок TODO/SUMMARY/CHANGELOG;
- legacy linkage;
- refresh generated indexes.

Partial reviews нужно фиксировать в `changes.md`, evidence tables или research logs с точным scope. Не создавайте впечатление, что весь profile был перепроверен.

## Правила evidence

- Разделяйте verified, observed, provider-reported, inferred, unknown и needs-recheck.
- Не превращайте вопрос provider-request в ответ.
- Не заявляйте live testing без сохраненного test evidence.
- Не используйте web-product pricing как API pricing.
- Фиксируйте contradictions, а не разрешайте их догадкой.

## Workflow пересмотра

1. Выберите active profile, comparison, need route или procurement kit.
2. Прочитайте текущие `README*`, `api.json` или `comparison.json`, `evidence*`, `changes*` и связанные research logs.
3. Проверьте official sources для scope пересмотра.
4. Обновите evidence и open questions до обновления recommendations.
5. Обновляйте `last_verified` только для реально проверенного scope.
6. Запустите `python3 scripts/generate_indexes.py`, `python3 scripts/generate_indexes.py --check` и `python3 scripts/validate_atlas.py`.
7. Зафиксируйте существенные изменения в `changes.md` / `changes.ru.md`.
8. Обновите `TODO.md`, `SUMMARY.md` и `CHANGELOG.md`, если изменилось состояние проекта.

## Gold gate

API profile не может стать Gold, пока остаётся любое из условий:

- не назначено research и editorial ownership;
- нет live-test evidence для workflow, где заявлен live testing;
- не закрыты pricing или data-rights blockers для рекомендуемого сценария;
- нет comparison coverage с реалистичной альтернативой;
- устарела `last_verified` дата для pricing, limits или legal terms;
- validator или generated indexes падают.

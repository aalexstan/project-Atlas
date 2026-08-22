# Мониторинг источников

[English version](SOURCE_MONITORING.md)

Atlas использует scheduled monitor, чтобы находить evidence, требующие review. Монитор никогда сам не меняет API facts, цены, юридические выводы или `last_verified`.

## Что выполняется автоматически

- внешние URL собираются из sources активных `apis/*/api.json`;
- проверяются доступность, HTTP status и настроенные content markers;
- даты review API, comparisons и needs сравниваются с review cadence;
- при необходимости обновляется существующая maintenance issue или создаётся одна новая.

## Статусы источника

- `ok` - источник ответил, markers найдены;
- `restricted` - автоматика получила `401`, `403` или `429`;
- `broken` - источник вернул `404` или `410`;
- `unavailable` - timeout, network error, unexpected status или server failure;
- `changed` - исчез required marker или изменился configured fingerprint.

Restricted или changed source не объявляется устаревшим автоматически. Researcher должен проверить official evidence до изменения выводов.

## Конфигурация

[`sources/source-registry.json`](../sources/source-registry.json) хранит defaults и optional per-URL markers/fingerprints. URL не нужно дублировать: sources активных profiles обнаруживаются автоматически.

Проверка без сети:

```bash
python3 scripts/check_sources.py --validate-config
python3 -m unittest discover -s tests -p "test_*.py"
```

Сетевая проверка:

```bash
python3 scripts/check_sources.py --report source-status.md
python3 scripts/check_review_due.py --report review-due.md
```

Отчёты scheduled runs являются operational artifacts и не коммитятся автоматически.

## Граница безопасности

Автоматика может открыть review task. Она не должна:

- менять цену из-за изменившегося текста;
- выводить API rights из технической доступности;
- обновлять verification dates;
- заявлять live testing;
- принимать marketing claims за independent evidence;
- публиковать credentials, response payloads или personal data.

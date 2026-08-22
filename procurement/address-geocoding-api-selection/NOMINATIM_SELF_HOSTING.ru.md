# Self-hosting checklist для Nominatim

[English version](NOMINATIM_SELF_HOSTING.md)

Используйте этот checklist, когда Nominatim рассматривается как self-hosted geocoding route. Это не юридическое заключение и не benchmark results.

## Граница

- Не используйте public `nominatim.openstreetmap.org` для autocomplete, bulk geocoding, stress tests, API resale или primary production geocoding.
- Решите, production route — это self-hosted Nominatim или commercial third-party provider.
- Attribution OpenStreetMap и ODbL obligations считайте предметом legal review.

## Scope-вопросы

- Какие страны или регионы нужны?
- Сервис нужен для forward geocoding, reverse geocoding, POI search, address lookup или export в другой search engine?
- Нужен autocomplete? Если да, public Nominatim не подходит, а нужен отдельный autocomplete design.
- Сервис internal-only, customer-facing или public API?
- Какие request volume, latency target, uptime target и freshness target нужны?

## Планирование импорта

- Выберите full planet или extracts.
- Выберите import style: `admin`, `street`, `address`, `full` или `extratags`.
- Решите, нужны ли updates, до использования `--no-updates`.
- Для больших imports используйте flatnode storage и закладывайте минимум 75GB для flatnode file.
- Считайте full-planet infrastructure отдельно от country/regional extracts.
- Зафиксируйте, используются ли optional Wikipedia/Wikidata importance и postcode data.

## Capacity planning

- Minimum installation RAM не является production capacity.
- Full-planet import требует high-memory machine, fast disks и long import window.
- Учитывайте disk growth, backups, WAL/archive logs, monitoring data и rollback storage.
- Benchmark target extracts до production hardware commitment.
- Тестируйте p50/p95/p99 latency при ожидаемой concurrency.

## Updates и freshness

- Выберите replication source и interval.
- Запустите `nominatim replication --init` и подтвердите start date.
- Для regular operation предпочитайте systemd-managed one-time updates.
- Документируйте catch-up behavior after downtime.
- Мониторьте replication lag и update failures.
- Сохраняйте flatnode files, если updates включены.

## Deployment и security

- Не используйте Nominatim test server в production.
- Используйте production frontend, например gunicorn behind nginx или эквивалентный supported deployment.
- Добавьте authentication, rate limiting и abuse protection при внешнем доступе.
- Определите logging, privacy, deletion и incident-response rules.
- Разделяйте import/update jobs и request-serving capacity.

## Legal and data rights

- Подтвердите attribution wording и display location.
- Проведите review ODbL obligations для caches, derived databases, exports и SaaS embedding.
- Решите, можно ли обрабатывать customer-submitted addresses в выбранной privacy model.
- Задокументируйте retention и deletion rules.

## Go / No-Go gates

| Gate | Required evidence |
|---|---|
| Product boundary | Public service excluded или явно policy-compliant. |
| Data scope | Extract/full-planet choice и import style documented. |
| Operations | Import, update, backup, monitoring и deployment plan. |
| Performance | Reproducible benchmark на target data and hardware. |
| Legal | ODbL, attribution, privacy и SaaS review completed. |

Atlas не проводил live testing для этого checklist.

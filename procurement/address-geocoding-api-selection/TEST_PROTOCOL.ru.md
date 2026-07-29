# Test protocol для API адресов и геокодирования

[English version](TEST_PROTOCOL.md)

Этот protocol описывает, как тестировать candidate APIs после provider-approved credentials и legal test conditions. Он не содержит реальных benchmark results.

## Тестовая выборка

Используйте legal synthetic или public sample. Не используйте private customer addresses без legal approval и data-processing agreements.

Включите:

- Москву;
- Санкт-Петербург;
- крупные региональные города;
- малые города и посёлки;
- rural/locality addresses;
- новые адреса;
- старые или переименованные адреса;
- улицы с частыми названиями;
- адреса со строением, корпусом, помещением и комнатой;
- неоднозначные адреса;
- адреса с опечатками;
- адреса без дома;
- координаты для reverse geocoding.

## Тестовые задачи

| Задача | Input | Expected evidence |
|---|---|---|
| Suggestions | Partial address strings | Relevant ordered suggestions and returned fields. |
| Cleaning | Messy address strings | Canonical fields, quality codes, registry identifiers. |
| Direct geocoding | Full and partial addresses | Coordinates, match level, precision, ambiguity. |
| Reverse geocoding | Coordinates | Returned address, object level, distance/confidence if available. |
| Organization/place search | Organization names or POI queries | Только для продуктов, где places явно поддержаны. |
| Batch | File/list of addresses | Throughput, error handling, legal batch permission. |

## Metrics

Фиксируйте:

- exact match rate;
- house-level match rate;
- street/locality-only match rate;
- false positives;
- missing results;
- duplicate or ambiguous results;
- coordinate precision;
- returned match level / quality code;
- latency p50/p95/p99;
- error rate;
- retry behavior;
- quota behavior;
- cost per 1,000 accepted records;
- cost per 1,000 successful geocodes;
- storage/caching rights confirmed for results.

## Procedure

1. Зафиксируйте sample и stable row IDs.
2. Запишите provider, product, method, plan, region, credentials type и date.
3. Вызывайте API только с documented parameters.
4. Храните raw responses только если contract provider это разрешает.
5. Нормализуйте outputs в нейтральную evaluation table.
6. Вручную проверьте possible false positives.
7. Отделяйте API errors от no-match results.
8. Записывайте все unknowns и provider clarifications.
9. Не публикуйте raw provider responses, если license запрещает.

## Reporting

Отчитывайтесь по сценариям, не как universal winner:

- лучший address-entry UX;
- лучшее cleaning quality;
- лучшая geocoding precision;
- лучшая official registry provenance;
- лучший legal fit для storage/SaaS;
- lowest projected TCO для target volume.

Не создавайте Atlas Score без публичной методики и evidence.

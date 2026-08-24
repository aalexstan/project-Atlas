# Ревью live-test публичного Nominatim

[English version](nominatim-geocoder-software-live-test-2026-08-24.md)

## Объём ревью

Процедурное pre-merge ревью первого address/geocoding live-test: public usage policy, raw payloads, attribution/licence signals и соблюдение интервалов между запросами.

## Checklist

- [x] Выбор кандидата и канонический URL OSMF policy документированы.
- [x] Core-claim list написан до выполнения запросов.
- [x] Core claims покрывают identity/purpose, response contract, operational limits и licensing/attribution.
- [x] Записаны требования policy: один запрос в секунду, custom User-Agent/Referer, attribution, запрет autocomplete и ограничения bulk.
- [x] Использованы три отдельных geocoding-запроса; autocomplete, batch и bulk endpoint не тестировались.
- [x] Между запросами выдержана пауза не менее двух секунд.
- [x] Raw JSON payloads, HTTP-коды и latency сохранены.
- [x] Unknown query вернул empty result и не использован как доказательство accuracy.
- [x] Attribution/licence values наблюдались в raw responses и сопоставлены с OSM copyright guidance.
- [x] Storage, caching, redistribution, SLA, accuracy и quota threshold остаются unknown.
- [x] Credentials, персональные данные и бинарные файлы не добавлялись.

## Findings

1. Public instance вернул JSONv2 и GeocodeJSON для двух отдельных address/place queries.
2. Unknown query вернул HTTP 200 с пустым массивом; это bounded behavior, а не общая гарантия accuracy.
3. Raw responses показали OpenStreetMap attribution и ODbL signals.
4. Тест не устанавливал и не должен устанавливать пригодность для autocomplete, bulk, quota threshold, storage, caching или redistribution rights.

## Вывод ревью

Evidence читаем и policy-compliant как ограниченный тест public instance. Он подтверждает observed request/response и attribution findings, но не повышает maturity и не устанавливает договорные/data-rights claims.

Это процедурное self-review, а не независимое ревью для Gold. Human review всё ещё нужен до установки `live_tested_on` или `live_test_valid_until` в `api.json`.

## Рекомендация по merge

Исследовательские и review-артефакты можно merge после принятия policy boundary человеком. Оставить `live_tested: false` и не устанавливать validity dates до завершения human review.

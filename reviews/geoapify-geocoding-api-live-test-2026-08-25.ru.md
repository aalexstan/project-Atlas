# Ревью: live-тест Geoapify — 2026-08-25

[English version](geoapify-geocoding-api-live-test-2026-08-25.md)

## Объём ревью

Процедурное pre-merge ревью первого live-теста Geoapify: предварительно зарегистрированный список из четырёх dimensions, raw payloads, интервалы между запросами и attribution signals.

## Checklist

- [x] Pre-registered plan создан до запросов.
- [x] Identity/purpose, response contract, rate-limit/policy и licensing/attribution разделены.
- [x] Выполнены три одиночных запроса с консервативной задержкой.
- [x] Batch, bulk, autocomplete load, scraping, parallel load и исчерпание квоты не выполнялись.
- [x] Raw JSON payloads, HTTP status и latency сохранены без API key.
- [x] Forward и reverse response shapes наблюдались.
- [x] Синтетический unknown query вернул empty result.
- [x] В непустых ответах наблюдались OpenStreetMap attribution и Open Database License signals.
- [x] Quota threshold, billing behavior, SLA, accuracy, storage, caching, redistribution и SaaS остаются unknown.
- [ ] Условия, принятые для конкретного аккаунта, независимо не зафиксированы.

## Findings

1. Три запроса дают ограниченное эмпирическое evidence для authenticated forward, reverse и unknown-input response behavior.
2. Тест не устанавливает accuracy, production suitability, порог rate limit или commercial data rights.
3. Account-specific terms acceptance не сохранён как evidence; это блокирует profile-level live-test validity до review.

## Вывод ревью

Evidence читаем и технически воспроизводим как узкий тест. Его нельзя считать benchmark или юридическим разрешением. Это процедурное self-review, а не независимое ревью для Gold.

Оставить `maturity: reviewed`, `live_tested: false` и validity dates unset до human review evidence и разрешения finding по access/terms.

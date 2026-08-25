# План live-теста Geoapify — 2026-08-25

[English version](live-test-plan-2026-08-25.md)

## Статус

Только предварительная регистрация claims. Запросы к API Geoapify не выполнялись, ключ не создавался и не использовался, результаты live-теста не заявляются.

## Официальные источники discovery

- [Geocoding API](https://www.geoapify.com/geocoding-api/)
- [Документация forward geocoding](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/)
- [Документация reverse geocoding](https://apidocs.geoapify.com/docs/geocoding/reverse-geocoding/)
- [Документация batch](https://apidocs.geoapify.com/docs/batch/)
- [Тарифы](https://www.geoapify.com/pricing/)
- [Условия](https://www.geoapify.com/terms-and-conditions/)

## Гейт доступа и условий

До любого запроса нужно зафиксировать лично зарегистрированный API key free-plan, разрешение автоматизированного теста одиночных запросов принятыми условиями, отсутствие paid-, production-, shared- или клиентского ключа и использование только синтетических или публичных адресов/координат. Ключ, email аккаунта и персональные данные не сохранять. В этом гейте не тестировать batch, bulk, scraping или исчерпание квоты.

Если условия free-plan, attribution Geoapify или требования OpenStreetMap/ODbL неясны для теста, остановиться без отправки запросов.

## Предварительно зарегистрированные core claims

Список фиксируется до теста и не может сужаться после получения результатов.

| Измерение | Claim для проверки | Граница наблюдения |
|---|---|---|
| Идентичность/назначение | Geoapify предоставляет hosted forward и reverse geocoding; address autocomplete и Places являются связанными, но отдельными возможностями. | Подтвердить identity endpoint и назначение ответа, но не качество или worldwide coverage. |
| Контракт ответа | Авторизованные одиночные forward-, reverse- и unknown-input запросы возвращают документированную JSON/result или error форму с полями координат/адреса. | Записать HTTP status, content type, выбранные поля, error shape и latency; ключ удалить. |
| Лимиты/политика | Для проверенного free-plan опубликованы 3 000 credits/day и до 5 requests/second, один credit на geocoding request; обычные разнесённые запросы принимаются без приближения к исчерпанию. | Наблюдать только сигналы headers/body; не провоцировать 429, не запускать batch и не измерять порог квоты. |
| Лицензия/attribution | Официальные pricing/terms/response docs указывают обязательный attribution Geoapify и OpenStreetMap и границы data use для free-plan, если они применимы. | Записать обязательное уведомление или короткую допустимую цитату. HTTP success не доказывает права storage, caching, redistribution или SaaS. |

## План одиночных запросов

1. Прямое геокодирование публичного адреса в Москве.
2. Обратное геокодирование публичных координат Москвы.
3. Неизвестная синтетическая строка с фиксацией empty result или error.
4. Повтор корректного запроса с documented language или result-format option, только если это разрешено free-plan и условиями.

Между запросами выдержать консервативную задержку. Не выполнять batch endpoint, bulk import, Places load, autocomplete load, scraping или production-throughput тест.

## Правила фиксации и решения

Записать UTC-время, класс запроса без ключа, status, latency, content type, выбранные поля, сигналы rate-limit, credit usage если он раскрывается, и attribution/license. Результаты классифицировать как `observed`, `provider_reported`, `inferred` или `unknown`. Цены, SLA, accuracy, house-level precision, storage, caching, redistribution, resale и SaaS остаются unknown без прямого evidence.

Тест не повышает maturity автоматически. Поля `live_tested_on` и `live_test_valid_until` добавлять только после human review raw evidence и парного review-файла.

Статус: `blocked_pending_legal_access_and_key`.

# Запрос поставщику — ГЛОБАС.API

[English version](provider-request.md)

Этот checklist подготовлен для разговора с Credinform. Его нельзя считать ответами поставщика, пока Credinform не ответит письменно или не предоставит официальную документацию.

## Граница продукта

1. ГЛОБАС.API — это самостоятельный API-продукт, кастомная поставка данных или интеграционная опция веб-системы ГЛОБАС?
2. Какие стандартные продукты входят в scope API?
3. Что находится вне стандартного API и требует отдельной лицензии или проекта?
4. Где проходят границы между стандартным ГЛОБАС.API, «Санкционным комплаенсом», «Портфелем», мониторингом и иностранными справками?
5. Какие страны и типы юридических лиц покрывает стандартный API?

## Методы и поля

1. Предоставьте полный список API methods.
2. Предоставьте field matrix по method, plan/package, country и legal form.
3. Какие методы поддерживают поиск компании по INN, OGRN, name, address, manager, owner, phone, email или foreign identifier?
4. Какие поля являются current-only, historical, computed, provider-scored или sourced from public registries?
5. У каких полей есть source references, timestamps, confidence levels или update dates?

## Protocol и authentication

1. Какой protocol используется: REST, SOAP, file delivery, hybrid API или другой model?
2. Какой production base URL?
3. Какая authentication model используется: API key, token, OAuth, mTLS, IP allowlist, signed request или другой механизм?
4. Доступны ли отдельные credentials для sandbox и production?
5. Есть ли account, user, role или method-level permissions?

## Formats, schemas, versioning и errors

1. Какие request/response formats поддерживаются: JSON, XML, CSV, XLSX, archive delivery или другой format?
2. Предоставьте schemas для каждого method.
3. Доступен ли OpenAPI/Swagger?
4. Как устроен API versioning?
5. Какая error model используется, включая validation errors, not-found results, quota errors, rate-limit errors и provider incidents?
6. Объявляются ли backward-incompatible changes заранее?

## Sandbox и testing

1. Включает ли трехдневный тест системы ГЛОБАС API access?
2. Может ли Credinform предоставить sandbox API credentials?
3. Sandbox содержит synthetic или real data?
4. Тестовые requests тарифицируются?
5. Можно ли провести equal-sample pilot против других поставщиков?

## Batch, async и webhooks

1. Какие methods поддерживают batch operations?
2. Каковы maximum batch size, file size, record count и processing window?
3. Поддерживаются ли asynchronous jobs?
4. Доступна ли delivery через webhook, callback URL, SFTP, email, object storage или другой механизм?
5. Доступны ли portfolio monitoring events через webhooks или scheduled exports?

## Pricing и billing

1. Предоставьте method-level pricing.
2. Как рассчитывается batch billing?
3. Есть ли отдельные prices для lookup, full profile, monitoring, reports, history, foreign entities, sanctions или portfolio operations?
4. Какой minimum commitment?
5. Как тарифицируются overage, retries, errors, duplicate records и cached results?
6. Есть ли setup, integration, support, SLA или data-package fees?
7. Какие цены являются API prices, а не web-system subscription prices?

## Limits, SLA и support

1. Какие production rate limits и quotas действуют по method?
2. Лимиты применяются к account, credential, IP, method, user или contract?
3. Какой SLA доступен для uptime, latency, incident response, support response и data freshness?
4. Как сообщается о planned maintenance и incidents?
5. Есть ли public или customer status page?
6. Какие support channels включены?

## Data rights и legal use

1. Может ли покупатель хранить API responses? Если да, как долго?
2. Может ли покупатель cache responses? Если да, какой TTL и refresh rules?
3. Может ли покупатель показывать данные своим customers, partners, affiliates или platform users?
4. Может ли покупатель использовать данные в affiliates или group companies?
5. Разрешены ли redistribution или resale?
6. Разрешен ли SaaS embedding?
7. Может ли покупатель использовать API outputs для scoring, machine-learning features, model training или automated decisions?
8. Какие поля содержат personal data, и какие legal roles / processing terms применяются?
9. Какие audit, deletion, retention, attribution и source-reference duties применяются?

## Change management

1. Есть ли API changelog?
2. Какая breaking-change policy?
3. Какой notice period применяется к deprecations, field removals, schema changes, pricing changes или source-coverage changes?
4. Есть ли mailing list, customer portal, RSS feed, status page или contract notice process для API changes?

## Запрошенные приложения

- API specification или OpenAPI/Swagger.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- Pricing appendix.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use и SaaS-embedding terms.
- Changelog или versioning policy.

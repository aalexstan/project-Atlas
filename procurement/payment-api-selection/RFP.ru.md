# RFP для платёжного API

[English version](RFP.md)

Ответьте отдельно по приёму платежей, возвратам, чекам, recurring payments, платёжным ссылкам, выплатам и marketplace/split-сценариям.

1. Какой точный API-продукт и какое юридическое лицо заключает договор?
2. Дайте актуальные API reference, OpenAPI/Swagger, base URLs, правила версий и deprecation policy.
3. Опишите аутентификацию, idempotency, error model, webhook events, retries и подписи.
4. Какие способы оплаты, валюты, страны и категории бизнеса поддерживаются?
5. Опишите one-stage, two-stage, recurring, refund, cancellation, partial refund и dispute flows.
6. Объясните ответственность за чеки/фискализацию, 54-ФЗ и обязательные поля.
7. Дайте sandbox, тестовые карты/данные, тестовые лимиты и процедуру сброса.
8. Дайте production rate limits, quotas, timeout guidance, incident handling и SLA.
9. Дайте таблицу комиссий, минимумы, fees за failed payment, сроки зачисления, резервы, chargebacks и overage.
10. Подтвердите storage, caching, customer display, SaaS embedding, redistribution, retention и deletion.
11. Подтвердите обработку персональных данных, DPA, разделение PCI DSS ответственности и контакты security.
12. Дайте support channels, escalation process, changelog и срок предупреждения breaking changes.

Отделяйте публичную документацию, стандартные договорные условия, индивидуальные условия и unknown.

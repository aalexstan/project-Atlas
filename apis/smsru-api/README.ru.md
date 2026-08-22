# API SMS.RU

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-22 |
| Класс продукта | SMS и verification API |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** российских SMS-уведомлений, OTP/verification, статусов доставки, лимитов и callbacks.

**Не подходит, если:** нужен rich chat или глобальный provider с документированным международным SLA.

**Итог:** SMS.RU подробно документирует SMS и verification operations. Production price и carrier terms требуют актуального quote.

## Технический доступ

| Поле | Значение |
|---|---|
| API | HTTPS API документирован |
| Возможности | Отправка, стоимость, баланс, статус, sender, лимиты, webhooks, voice authorization |
| Аутентификация | API identifier/token pattern документирован |
| Sandbox | Публично неизвестен |
| OpenAPI | В проверенных официальных источниках не найден |
| Актуальность документации | На официальной странице указано обновление 23.06.2026 |

## Рекомендация по сценарию

Рассматривать SMS.RU как SMS/verification candidate и сравнивать с SMSC на одинаковых sample, sender, операторах, throughput, delivery, price и data-rights questions. Победитель не объявляется.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/messaging/2026-08-22-smsru.ru.md).

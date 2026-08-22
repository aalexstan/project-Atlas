# API SMSC

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Зрелость | Reviewed |
| Последняя проверка | 2026-08-22 |
| Класс продукта | SMS gateway |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** SMS, OTP/verification, статусов доставки и server-to-server messaging.

**Не подходит, если:** основной продукт — чат-интерфейс и rich interaction.

**Итог:** SMSC документирует HTTP/HTTPS, SMTP и SMPP. Production price, throughput, sender и carrier terms нужно подтверждать на уровне аккаунта.

## Технический доступ

| Поле | Значение |
|---|---|
| REST send endpoint | `https://smsc.ru/rest/send/` |
| Форматы | HTTP/HTTPS, SMTP, SMPP; JSON body для REST send документирован |
| Аутентификация | Login/password или API key |
| Статусы/callbacks | Документированы в HTTP API |
| OpenAPI | В проверенных официальных источниках не найден |
| Sandbox | Публично неизвестен |

## Рекомендация по сценарию

Использовать SMSC, если нужны доставка по номеру телефона и операции со статусами/стоимостью. Сравнивать с SMS.RU по одинаковым вопросам sender, throughput, delivery, price и data processing. Не публиковать универсальную цену SMS без текущего маршрута и условий оператора.

См. [evidence](evidence.ru.md) и [журнал исследования](../../research/messaging/2026-08-22-smsc.ru.md).

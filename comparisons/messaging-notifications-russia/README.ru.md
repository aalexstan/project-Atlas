# API сообщений и уведомлений в России

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Последняя проверка | 2026-08-22 |
| Кандидаты | Telegram Bot API, SMSC API, SMS.RU API |
| Live testing | Не проводился |

## Краткая матрица выбора

| Сценарий | Первичный shortlist | Почему |
|---|---|---|
| Чат, бот, интерактивный интерфейс | Telegram Bot API | Нативное взаимодействие, клавиатуры, webhooks и Mini Apps. |
| SMS или OTP по номеру телефона | SMSC, SMS.RU | SMS gateway features и операции статусов/delivery. |
| Самая низкая цена | Неизвестно | Нет общих условий по маршруту, оператору, sender и договору. |

## Матрица

| Критерий | Telegram Bot API | SMSC API | SMS.RU API |
|---|---|---|---|
| Основной канал | Telegram chat | SMS | SMS/voice verification |
| Интерактивный bot UI | Да | Нет | Нет |
| SMS delivery | Нет | Да | Да |
| Delivery status | Статус обновления бота, не carrier DLR | Status/callback route документирован | Status/webhooks документированы |
| Аутентификация | Bot token | Login/password или API key | API identifier/token pattern |
| Webhooks/callbacks | Webhooks | Callbacks документированы | Webhooks документированы |
| Публичная цена API | Несопоставима с SMS | Не профилирована | Не профилирована |
| Production limits | Зависят от сценария | Неизвестны | Метод дневного лимита есть; точные limits открыты |
| SLA | Неизвестен | Неизвестен | Неизвестен |
| Live test | Не проводился | Не проводился | Не проводился |

Telegram нельзя считать заменой SMS. Цены SMS сравнивать только при одинаковых стране, операторе, sender, длине сообщения, маршруте, объёме и VAT assumptions.

См. [need-маршрут](../../needs/messaging-notifications/README.ru.md) и [procurement kit](../../procurement/messaging-api-selection/README.ru.md).

# Сообщения и уведомления

[English version](README.md)

## Вопрос пользователя

Какой API выбрать для бота, SMS по номеру телефона, OTP или transactional notification flow?

## Быстрый выбор

| Сценарий | Первичный shortlist | Главный риск | Следующий документ |
|---|---|---|---|
| Чат-бот или интерактивный продукт | Telegram Bot API | Пользователь должен начать диалог; это не carrier SMS | [Профиль Telegram](../../apis/telegram-bot-api/README.ru.md) |
| SMS или OTP по номеру | SMSC, SMS.RU | Нужен общий тест цены, маршрута, throughput и DLR | [Сравнение](../../comparisons/messaging-notifications-russia/README.ru.md) |

## Что проверить до выбора

Подтвердите opt-in/opt-out, sender approval, охват операторов, длину сообщения, DLR semantics, retry behavior, OTP security, персональные данные, retention, support, квоты и SLA.

## Ограничения

Credentials, номера, доставка сообщений, latency measurements и общий benchmark не использовались. Telegram chat delivery и SMS carrier delivery — разные категории.

## Следующий шаг

Откройте [сравнение](../../comparisons/messaging-notifications-russia/README.ru.md), затем отправьте [procurement kit](../../procurement/messaging-api-selection/README.ru.md) SMS-поставщикам.

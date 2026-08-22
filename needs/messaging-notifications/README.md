# Messaging and Notifications

[Русская версия](README.ru.md)

## The user question

Which API should we use for a bot, phone-number SMS, OTP, or transactional notification flow?

## Quick choice

| Scenario | Initial shortlist | Main risk | Next document |
|---|---|---|---|
| Chat bot or interactive product | Telegram Bot API | User must initiate/join; not carrier SMS | [Telegram profile](../../apis/telegram-bot-api/README.md) |
| SMS or OTP by phone number | SMSC, SMS.RU | Price, operator route, throughput and DLR need common test | [Comparison](../../comparisons/messaging-notifications-russia/README.md) |

## Before choosing

Confirm opt-in/opt-out, sender approval, operator coverage, message length, DLR semantics, retry behavior, OTP security, personal-data processing, retention, support, quotas and SLA.

## Limits

No credentials, phone numbers, message delivery, latency measurements, or common benchmark were used. Telegram chat delivery and SMS carrier delivery are different categories.

## Next step

Use the [comparison](../../comparisons/messaging-notifications-russia/README.md), then send the [procurement kit](../../procurement/messaging-api-selection/README.md) to SMS providers.

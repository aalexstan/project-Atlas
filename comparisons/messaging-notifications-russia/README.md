# Messaging and Notification APIs in Russia

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Last verified | 2026-08-22 |
| Candidates | Telegram Bot API, SMSC API, SMS.RU API |
| Live testing | Not performed |

## Decision Summary

| Scenario | Initial shortlist | Why |
|---|---|---|
| Chat, bot, interactive interface | Telegram Bot API | Native bot interaction, keyboards, webhooks and Mini Apps. |
| Phone-number SMS or OTP | SMSC, SMS.RU | SMS gateway features and delivery/status operations. |
| Lowest cost | Unknown | Route, operator, sender and contract assumptions are not common yet. |

## Matrix

| Criterion | Telegram Bot API | SMSC API | SMS.RU API |
|---|---|---|---|
| Primary channel | Telegram chat | SMS | SMS/voice verification |
| Interactive bot UI | Yes | No | No |
| SMS delivery | No | Yes | Yes |
| Delivery status | Bot update status; not carrier DLR | Documented status/callback route | Documented status/webhooks |
| Authentication | Bot token | Login/password or API key | API identifier/token pattern |
| Webhooks/callbacks | Webhooks | Callbacks documented | Webhooks documented |
| Public API price | Not comparable to SMS | Not profiled | Not profiled |
| Production limits | Scenario-dependent | Unknown | Daily-limit method; exact production limits open |
| SLA | Unknown | Unknown | Unknown |
| Live test | Not performed | Not performed | Not performed |

Do not treat Telegram as an SMS substitute. Do not compare SMS prices without the same country, operator, sender, message length, route, volume and VAT assumptions.

See the [messaging need route](../../needs/messaging-notifications/README.md) and [procurement kit](../../procurement/messaging-api-selection/README.md).

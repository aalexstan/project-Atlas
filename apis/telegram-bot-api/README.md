# Telegram Bot API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Product class | Bot platform API |
| Live testing | Not performed |

## Quick Verdict

**Best for:** Bots, interactive notifications, support flows, chat interfaces, and Telegram Mini Apps.

**Avoid when:** The product needs carrier-grade SMS delivery, a phone-number-based audience, or a provider-neutral notification channel.

**Bottom line:** Telegram Bot API is a platform interface, not a generic SMS or transactional email replacement.

## Technical Access

| Field | Value |
|---|---|
| Base URL | `https://api.telegram.org/bot<token>/METHOD_NAME` |
| Format | HTTPS; JSON, form encoding, multipart for files |
| Authentication | Bot token |
| Updates | Long polling or webhooks |
| Local option | Official local Bot API server is documented |
| OpenAPI | Not found in reviewed official sources |

## Core Capabilities

| Capability | Status |
|---|---|
| Text and media messages | Documented |
| Commands and keyboards | Documented |
| Webhooks | Documented |
| Payments | Documented in Bot API |
| Mini Apps | Officially documented as a related bot platform capability |
| SMS delivery | Not applicable |

## Scenario Recommendation

Choose Telegram when users can deliberately start or join a bot. Use SMSC or SMS.RU when phone-number delivery and carrier status are required. Do not claim guaranteed delivery or universal reach from Bot API documentation.

See [evidence](evidence.md) and the [research log](../../research/messaging/2026-08-22-telegram.md).

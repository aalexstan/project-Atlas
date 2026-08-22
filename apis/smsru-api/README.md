# SMS.RU API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Product class | SMS and verification API |
| Live testing | Not performed |

## Quick Verdict

**Best for:** Russian SMS notifications, OTP/verification workflows, delivery status, limits, and callbacks.

**Avoid when:** The required channel is a rich chat or a global provider with a documented international SLA.

**Bottom line:** SMS.RU has a broad official API documentation surface for SMS and verification operations. Production price and carrier terms still need a current quote.

## Technical Access

| Field | Value |
|---|---|
| API | HTTPS API documented |
| Capabilities | Send, cost, balance, status, sender, limits, webhooks, voice authorization |
| Authentication | API identifier/token pattern documented |
| Sandbox | Unknown publicly |
| OpenAPI | Not found in reviewed official sources |
| Documentation freshness | Official page states last update 2026-06-23 |

## Scenario Recommendation

Use SMS.RU as an SMS/verification candidate and compare it with SMSC on the same sample, sender, operators, throughput, delivery, price, and data-rights questions. No provider winner is declared.

See [evidence](evidence.md) and the [research log](../../research/messaging/2026-08-22-smsru.md).

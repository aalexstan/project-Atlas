# SMSC API

[Русская версия](README.ru.md)

## Research Status

| Field | Value |
|---|---|
| Maturity | Reviewed |
| Last verified | 2026-08-22 |
| Product class | SMS gateway |
| Live testing | Not performed |

## Quick Verdict

**Best for:** SMS delivery, OTP/verification, delivery status, and server-to-server messaging.

**Avoid when:** A chat interface or rich user interaction is the primary product requirement.

**Bottom line:** SMSC has documented HTTP/HTTPS, SMTP, and SMPP routes. Production price, throughput, sender and carrier terms require account-level confirmation.

## Technical Access

| Field | Value |
|---|---|
| REST send endpoint | `https://smsc.ru/rest/send/` |
| Formats | HTTP/HTTPS, SMTP, SMPP; JSON body documented for REST send |
| Authentication | Login/password or API key |
| Status/callbacks | Documented in HTTP API materials |
| OpenAPI | Not found in reviewed official sources |
| Sandbox | Unknown publicly |

## Scenario Recommendation

Use SMSC when phone-number delivery and status/cost operations are required. Compare SMS.RU using the same sender, throughput, delivery, price, and data-processing questions. Do not publish a universal per-SMS price without current route and operator assumptions.

See [evidence](evidence.md) and the [research log](../../research/messaging/2026-08-22-smsc.md).

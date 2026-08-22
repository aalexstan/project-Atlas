# Messaging API Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

Use synthetic recipients or provider-approved test numbers only. Never store real phone numbers or OTPs in Atlas.

Test the same matrix for SMS providers: short Latin, Cyrillic, multipart, long message, invalid recipient, duplicate request, retry, delivery report, callback failure, sender approval, OTP expiry, and opt-out. Record route, operator, timestamp, message segments, provider status, DLR latency, error, retry count and final state.

For Telegram, separately test bot initiation, sendMessage, webhook delivery, duplicate update handling, command/keyboard flow, user blocking, and Mini App handoff. These are not comparable to carrier SMS delivery. No actual test results are claimed.

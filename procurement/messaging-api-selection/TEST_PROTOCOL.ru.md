# Протокол тестирования messaging API

[English version](TEST_PROTOCOL.md)

Используйте только синтетических получателей или разрешённые provider test numbers. Реальные номера и OTP в Atlas не сохранять.

Для SMS-поставщиков одинаково проверьте: короткий Latin, Cyrillic, multipart, длинное сообщение, неверный номер, duplicate request, retry, delivery report, callback failure, sender approval, OTP expiry и opt-out. Записывайте route, operator, timestamp, segments, provider status, DLR latency, error, retries и final state.

Для Telegram отдельно проверьте user initiation, sendMessage, webhook delivery, duplicate update handling, commands/keyboards, user blocking и Mini App handoff. Это не сравнимо с carrier SMS. Результаты реальных тестов не заявляются.

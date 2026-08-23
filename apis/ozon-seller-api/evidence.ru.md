# Evidence: Ozon Seller API

[English version](evidence.md)

## Подтверждено официальными материалами

- У Ozon есть официальный маршрут документации Seller API: `docs.ozon.ru/api/seller/`.
- В официальных материалах Ozon for Dev базовым URL seller API указан `https://api-seller.ozon.ru`.
- В официальных материалах для разработчиков описана аутентификация продавца через Client ID и API key.
- В официальных материалах Ozon for Dev обсуждается доступ приложений через OAuth token.
- В официальном сообществе разработчиков упоминаются seller-методы для товаров, остатков, аналитики, заказов и отправлений.

## Ограничения уверенности

- Основной маршрут документации не удалось стабильно открыть в этом исследовании из-за redirect loop в исследовательской среде.
- Полная текущая матрица методов, квоты, sandbox и machine-readable specification независимо не подтверждены.
- Цена API, SLA и права дальнейшего использования данных неизвестны.
- Credentials и живые запросы не использовались.

## Источники

- [Документация Ozon Seller API](https://docs.ozon.ru/api/seller/)
- [Ozon for Dev](https://dev.ozon.ru/community/)
- [Официальное обсуждение OAuth](https://dev.ozon.ru/community/2154-Avtorizatsiia-cherez-OAuth-token/)

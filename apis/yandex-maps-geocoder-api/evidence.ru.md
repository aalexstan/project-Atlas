# Доказательства по Yandex Maps Geocoder API

[English version](evidence.md)

| Утверждение | Источник | Проверено | Статус | Примечание |
|---|---|---|---|---|
| Geocoder API определяет координаты по адресу и адрес по координатам. | https://yandex.com/maps-api/docs/geocoder-api/index.html | 2026-07-29 | verified | Прямое и обратное геокодирование. |
| Endpoint: `https://geocode-maps.yandex.ru/v1`, параметры `apikey`, `geocode`, `lang`. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | API key из developer dashboard. |
| `geocode` может быть адресом/названием или координатами. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Определяет direct или reverse режим. |
| Формат ответа - JSON. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | `format=json`. |
| Обратное геокодирование поддерживает `kind`: house, street, metro, district, locality. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Опциональный параметр. |
| `results` по умолчанию 10, максимум 50. | https://yandex.com/maps-api/docs/geocoder-api/request.html | 2026-07-29 | verified | Документация параметров. |
| Response docs описывают precision и ошибки 400, 403, 429. | https://yandex.com/maps-api/docs/geocoder-api/response.html | 2026-07-29 | verified | Precision не равен реестровой валидации. |
| Бесплатный лимит Геокодера - 1 000 запросов/день. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Для бесплатных условий. |
| Бесплатное использование привязано к показу на Яндекс Картах; показ на сторонних картах запрещён. | https://yandex.ru/legal/maps_api/ru/ | 2026-07-29 | verified | Существенное ограничение прав. |
| Годовые платные тарифы начинаются с 195 000 руб. Standard и 226 200 руб. Extended за 1 000 запросов/день. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Российская тарифная страница. |
| Тестовый тариф: 100 запросов/день до 7 суток без минимального платежа. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Это не live test Atlas. |
| Свыше 1 000 000 запросов/день требуется индивидуальный расчёт. | https://yandex.ru/dev/tariffs/doc/ru/geocoder/prices/ | 2026-07-29 | verified | Нужен контакт с поставщиком. |
| OpenAPI/Swagger не найден в просмотренных публичных docs. | Official docs reviewed | 2026-07-29 | unknown | Перепроверить перед Gold. |
| Публичный SLA не найден в просмотренных docs. | Official docs reviewed | 2026-07-29 | unknown | Вопрос для закупки. |

## Live Testing

Credentialed live test Atlas не проводил.

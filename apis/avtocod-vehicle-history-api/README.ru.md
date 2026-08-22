# Avtocod Vehicle History API

[English version](README.md)

## Статус исследования

| Поле | Значение |
|---|---|
| Maturity | Reviewed |
| Последняя проверка | 2026-08-23 |
| Класс продукта | Коммерческий API истории автомобиля |
| Live testing | Не проводился |

## Краткий вывод

**Подходит для:** B2B-процессов, которым нужно заказывать и получать отчёты по истории автомобиля после commercial и legal review.

Автокод документирует JSON HTTPS GET/POST, token access, создание/получение отчёта, Swagger UI и публичные схемы отчётов. Квоты бывают дневными, месячными и общими; frequency limits зависят от report type и договора. Отчёты обычно доступны шесть месяцев. Чтение существующего отчёта не тарифицируется как новая генерация, а принудительная перегенерация платная.

Публичные B2B-цены подтверждают `Автозаполнение` за 10 RUB/отчёт и `Автозаполнение плюс` за 11 RUB/отчёт, индивидуальные условия начинаются от 10 000 отчётов. Цена полного vehicle-history report зависит от объёма и договора. Доставка webhook не гарантирована, поэтому нужен polling fallback.

Provider pages продвигают интеграции для insurance, lending, leasing, marketplaces и scoring, но точные права storage, redistribution, automated decisions и model training требуют письменного договора.

См. [evidence](evidence.ru.md), [deep dive](../../research/vehicle-history/2026-08-23-avtocod-deep-dive.ru.md) и [provider request](../../research/vehicle-history/provider-request.ru.md).

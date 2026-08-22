# Приём онлайн-платежей

[English version](README.md)

## Вопрос пользователя

Какой API выбрать российскому сайту, приложению, SaaS-продукту или маркетплейсу для приёма онлайн-платежей и возвратов?

## Кому подходит маршрут

Используйте его, если нужны создание платежа, статус, возврат, чеки, регулярные списания, платёжные ссылки или webhooks. Это не юридическое заключение и не заменяет onboarding эквайринга.

## Быстрый выбор

| Сценарий | Первичный shortlist | Главный риск | Следующий документ Atlas |
|---|---|---|---|
| Понятный публичный developer journey | ЮKassa | Комиссия и квоты зависят от договора | [Профиль ЮKassa](../../apis/yookassa-api/README.ru.md) |
| Two-stage или подписки | CloudPayments | Production terms недостаточно публичны для финального выбора | [Профиль CloudPayments](../../apis/cloudpayments-api/README.ru.md) |
| Зачисления и счёт Т‑Банка | Интернет-эквайринг Т‑Банка | Точный contract зависит от onboarding | [Профиль Т‑Банка](../../apis/tbank-internet-acquiring-api/README.ru.md) |
| Procurement shortlist | Все три | Нет общего quote, SLA и live benchmark | [Сравнение](../../comparisons/payment-acceptance-russia/README.ru.md) |

## Что проверить до выбора

Подтвердите eligibility бизнеса, способы оплаты, чеки и ответственность по 54-ФЗ, возвраты, согласие на recurring payments, сроки зачисления, fraud/dispute handling, персональные данные, хранение, SaaS display, квоты, SLA и deprecation policy.

## Ограничения исследования

Credentials, live payments, refunds, sandbox calls, измерения latency и общий benchmark не проводились. Публичные страницы не дают напрямую сопоставимых merchant-specific договоров по всем кандидатам.

## Следующий шаг

Откройте [сравнение платёжных API](../../comparisons/payment-acceptance-russia/README.ru.md), затем отправьте [procurement checklist](../../procurement/payment-api-selection/README.ru.md) shortlisted providers.

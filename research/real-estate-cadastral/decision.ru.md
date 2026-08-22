# Решение по профилю Росреестра, ЕГРН и НСПД

[English version](decision.md)

## Решение

Пока **не создавать** active API-first profile.

Official sources подтверждают electronic EGRN access, пакеты по access key, machine-readable outputs НСПД и XML-схемы. Они не подтверждают единый supported public API для commercial developers с endpoint catalog, authentication flow, quotas, SLA и downstream-use terms.

Общая карточка `Rosreestr API` ошибочно смешала бы юридически значимые выписки, пакетный доступ, геосервисы НСПД, межведомственный обмен и frontend endpoints публичной карты.

## Условия повторного открытия

- Подтвердить product identity, intended audience, base URL и methods.
- Подтвердить onboarding, authentication, formats и schemas.
- Подтвердить current fees, quotas, rate limits, SLA и support.
- Подтвердить storage, display, SaaS, redistribution и personal-data terms.
- Подтвердить versioning и breaking-change policy.

## Безопасная текущая рекомендация

- Для юридически значимых сведений использовать official EGRN extract.
- Для повторяющихся выписок оценить key-based FGIS EGRN access после уточнения onboarding и тарифа.
- Использовать НСПД для spatial-data discovery, не предполагая unrestricted REST access.
- Не автоматизировать undocumented cadastral-map frontend endpoints в production.

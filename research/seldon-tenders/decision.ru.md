# Решение по Seldon.Tenders

[English version](decision.md)

## Решение

**Результат: 3. Сохранить только как legacy до появления более сильных официальных доказательств.**

В этом проходе не создавать активный API-first профиль Seldon.Tenders.

## Обоснование

Официальные страницы Seldon подтверждают, что `API.Seldon.Tenders` существует как маршрут интеграции закупочных данных в рамках Seldon 1.7 и описывается как программный интерфейс доступа к закупочным данным. Официальная новость Seldon также показывает, что web-продукт Seldon.Tenders позднее был переименован в Seldon.Win.

Но проверенные публичные официальные страницы не дают минимального developer/procurement evidence для активного профиля Atlas:

- endpoint catalog или base URL;
- authentication;
- request и response schemas;
- formats;
- OpenAPI/Swagger;
- rate limits и quotas;
- SLA и support terms;
- API-specific pricing и billing units;
- права storage, caching, redistribution и SaaS embedding.

## Что не выбрано

**Вариант 1 — создать отдельный API-first профиль:** пока не выбран. Официальная идентичность продукта есть, но текущих доказательств недостаточно для активной карточки без чрезмерного количества unknown.

**Вариант 2 — включить как capability Seldon.Basis:** не выбран. Официальные страницы относят `API.Seldon.Tenders` к procurement-функциональности Seldon 1.7, а не к Seldon.Basis.

## Работа с legacy

Сохранить [catalog/api-seldon-tenders.md](../../catalog/api-seldon-tenders.md) как provenance и source-risk history.

Старый URL `api-seldon.ru` остается только исторической risk note. Его нельзя использовать как текущий официальный источник.

## Условия повторного открытия

Вернуться к активной карточке, если Seldon опубликует или предоставит:

- API specification или OpenAPI/Swagger;
- официальный endpoint и authentication model;
- method and field matrix;
- sandbox или test credentials;
- API pricing, limits и SLA;
- data-use rights для storage, display, redistribution, affiliates и SaaS embedding.

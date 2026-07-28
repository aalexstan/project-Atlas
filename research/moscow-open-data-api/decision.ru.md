# Решение по Moscow Open Data API

[English version](decision.md)

## Решение

В этом проходе **не создавать** активный API-first профиль Moscow Open Data API.

## Обоснование

Legacy-карточки Atlas указывают `data.mos.ru` и `data.mos.ru/developers/documentation` как релевантный официальный маршрут. Однако официальные страницы, проверенные в этом проходе, не вернули пригодную текущую API-документацию в доступной среде.

Поскольку Atlas не использует API Portal как final source of truth, обязательные факты остаются unknown:

- текущая официальная идентичность API;
- активный endpoint или документация;
- authentication;
- request и response formats;
- назначение и поддерживаемые операции;
- текущий статус;
- limits, quotas, support и SLA;
- license/reuse terms.

## Статус

Сохранить как **legacy/supporting research** до доступности официальной документации или другого первичного источника Правительства Москвы, подтверждающего детали API.

## Условия повторного открытия

Создавать активный профиль только если официальные источники подтверждают:

- текущую product identity;
- documentation или endpoint;
- authentication;
- supported formats;
- intended use и main operations;
- current availability;
- license/reuse terms.

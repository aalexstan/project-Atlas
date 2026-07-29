# Решение по Geoapify Geocoding API

[English version](decision.md)

## Решение

Создать активный API-first profile:

- `apis/geoapify-geocoding-api/`

## Обоснование

Официальные источники Geoapify дают достаточно evidence для поддерживаемой карточки Atlas:

- official product page;
- developer documentation;
- forward and reverse endpoints;
- API-key authentication;
- response formats;
- batch API;
- public pricing and rate limits;
- public SLA statement for paid plans;
- attribution and storage-related terms.

## Граница продукта

Рассматривать Geoapify как hosted commercial open-data geocoding API.

Не считать его:

- public `nominatim.openstreetmap.org`;
- self-hosted Nominatim;
- official Russian address registry validation;
- Russia-specific address cleaning;
- routing или matrix API;
- полноценной Places API карточкой.

## Главные blockers

- Atlas live test или benchmark не проводились.
- ODbL, attribution, derived-database, caching, SaaS и redistribution implications требуют legal review.
- Paid/enterprise contract terms могут отличаться от public terms.
- DPA/privacy и data residency requirements требуют scenario-specific review.
- Batch failure/retry/billing details требуют pilot confirmation.

## Как включать в comparison

Добавить Geoapify в address/geocoding comparison как managed international/open-data geocoding route. Сравнивать с self-hosted Nominatim, когда важен operational ownership, и с Yandex/2GIS/DaData, когда доминируют Russia-specific map ecosystem или address-cleaning needs.

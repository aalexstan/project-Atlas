# Решение по OpenCage Geocoding API

[English version](decision.md)

## Решение

Создать активный API-first profile для **OpenCage Geocoding API**.

## Обоснование

Официальные источники OpenCage дают достаточно evidence для Atlas reviewed maturity:

- product identity and official docs;
- граница forward и reverse geocoding;
- API-key authentication;
- request pattern и response formats;
- public pricing и free-trial limits;
- storage/caching wording;
- open-data source и data-license context;
- явное отделение от Geosearch/autosuggest;
- явная batch boundary.

## Границы

- Рассматривать OpenCage как hosted open-data geocoding API, не как address-cleaning API.
- Рассматривать Geosearch/autosuggest как отдельный продукт для будущего исследования.
- Не считать public pricing commercial quote для enterprise use.
- Не считать storage-friendly wording юридическим разрешением на redistribution, resale, white-label SaaS, API proxying или model training.

## Blockers перед Gold

- Credentialed benchmark на target samples.
- Legal review ODbL, attribution, derived databases, redistribution и SaaS use.
- Contract confirmation SLA/support and enterprise terms.
- Privacy/DPA review для submitted addresses and coordinates.
- Batch operations review для high-volume workflows.

## Live Testing Status

Live API test, spreadsheet upload или benchmark не проводились.

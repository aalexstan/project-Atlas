# Исследование Росреестра, ЕГРН и НСПД - 2026-08-23

[English version](2026-08-23-rosreestr-egrn-nspd.md)

## Scope

Определить, есть ли у Росреестра или Роскадастра supported public interface для commercial cadastral lookup, автоматизированных выписок ЕГРН или bulk spatial-data integration.

## Официальные источники

- [FAQ Роскадастра](https://roscadastre.ru/html/news_2024/67593ca59252f431e8639b07.pdf)
- [Дайджест изменений 2025 года](https://roscadastre.ru/html/news_2025/67a453ef71101331420997e4f.pdf)
- [Материал о сервисах и форматах НСПД](https://www.roscadastre.ru/html/docs/2025/67808f9247208bdccde18ac6.pdf)
- [Уведомление об XML-схемах](https://www.roscadastre.ru/docs/4192857/)
- [Письмо о доступе к ЕГРН](https://www.roscadastre.ru/docs/rrdocs/4243559/)

## Подтверждённые факты

- Сведения ЕГРН предоставляются по ФЗ № 218-ФЗ и приказу Росреестра № П/0149.
- Official material описывает сервис `Запрос посредством доступа к ФГИС ЕГРН`, access key и предоплаченные пакетные операции сроком один год.
- Official material 2025 года указывает диапазон 116-290 RUB за пакетную выписку, но current applicant, package и extract conditions требуют уточнения.
- Electronic services НСПД могут выдавать JSON, XML, PDF и CSV. Machine-readable output сам по себе не доказывает general public developer API.
- Росреестр публикует XML-схемы кадастровых документов и межведомственного обмена. Схемы не доказывают open API access для commercial applications.
- Правила разделяют public information, restricted information и applicant-specific legal grounds.

## Границы продуктов

1. Единичные юридически значимые выписки ЕГРН.
2. Key-based package access к ФГИС ЕГРН.
3. Портал и electronic geoservices НСПД.
4. Регулируемый межведомственный XML-обмен.

Frontend endpoint кадастровой карты нельзя выдавать за supported production API без official docs и terms. Поиск по карте не равен выписке ЕГРН.

## Unknowns и blockers

- Supported endpoint/method catalog для commercial organizations.
- Onboarding, authentication и automation model для access key.
- Current package tariffs, quotas, rate limits, SLA и support.
- Пригодность сервисов НСПД для unattended external production use.
- Storage, caching, customer display, SaaS, redistribution и resale rights.
- Derived datasets, valuation, scoring, model training, personal-data boundaries и versioning.

## Live testing и решение

Не проводился. Atlas не авторизовывался, не вызывал frontend endpoints, не заказывал выписку и не выполнял платные операции.

Не создавать active API profile до official specification или письменного уточнения Росреестра/Роскадастра о supported commercial integration route.

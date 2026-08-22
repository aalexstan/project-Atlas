# Дорожная карта

[English version](ROADMAP.md)

Дорожная карта ориентирована на результаты. Сроки могут меняться, принципы продукта — нет.

## Этап 1 — Фундамент

Создать двуязычные документы, методологию исследования, шаблон карточки, шаблон сравнения, руководство по миграции и первый backlog.

**Успех:** новый исследователь может создать единообразную карточку, не изобретая формат. Фундамент теперь также включает индекс документации, индекс legacy-материалов, детерминированные сгенерированные индексы, validation CI, первый need-based маршрут и review cadence policy.

## Этап 2 — Эталонные карточки

Первые цели: DaData, релевантные продукты Контура и Seldon, официальные способы доступа к реестрам, геокодирование Яндекса и API 2GIS.

**Успех:** карточки заметно полезнее для выбора, чем описания поставщиков.

**Текущий прогресс:** reviewed address/geocoding profiles уже есть для DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, Yandex Maps Organization Search API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Geoapify Geocoding API, OpenCage Geocoding API, LocationIQ Geocoding API, Nominatim Geocoder Software и FIAS/GAR Data Integration. Provider-specific request checklists подготовлены для DaData, Yandex Maps, 2GIS, Geoapify, OpenCage и LocationIQ. Open-data XML ZIP route FIAS/GAR теперь включает current package metadata, inspected structure XSDs, inspected current data ZIP central directory, parsed root dictionary XML files и parsed sample regional directories `99/`, `87/` and sparse `82/`; Geoapify/OpenCage/LocationIQ hosted open-data/geocoding routes и Nominatim self-hosting operations path описаны точнее, но national FIAS/GAR row counts, full/delta semantics, детали API/SMEV services, ODbL/legal review и benchmarks остаются blockers. До Gold нужны live tests, подтверждение SLA, проверка прав данных и quality benchmarks.

## Этап 3 — Центр сравнений

Маршрутизация и логистика теперь оформлены как отдельное направление сравнения: Yandex Maps route details/matrix, 2GIS Routing API и self-hosted OSRM отделены от геокодирования, places и delivery optimization.

Для закупок и тендеров теперь есть reviewed-маршруты интеграции ЕИС и Seldon.Tenders; неизвестными остаются актуальные схемы, доступ, коммерческие условия и права на данные.

Для доставки теперь есть отдельные reviewed-маршруты tracking Почты России и жизненного цикла заказа Яндекс Доставки; carrier aggregation остаётся будущим классом исследования.

Yandex Rasp API проверен для бесплатных публичных функций междугородних расписаний; коммерческое и долгосрочное хранение остаётся заблокированным опубликованными условиями без отдельного согласия Yandex.

Avtocod Vehicle History API проверен как коммерческий маршрут отчётов; независимые доказательства качества данных, цены, лимиты и права high-stakes use остаются открытыми.

Исследование недвижимости/кадастра теперь отделяет official EGRN extracts, key-based FGIS EGRN access, NSPD electronic services и межведомственный XML-обмен. Active profile отложен до подтверждения supported commercial interface, authentication, limits, SLA и reuse rights.

Первые сравнения: данные о компаниях и контрагентах, адреса и геокодирование, закупки, сообщения, платежи и финансовые данные.

**Успех:** каждое сравнение содержит рекомендации по сценариям, доказательства и дату пересмотра. Need-based маршруты должны связывать частые вопросы пользователей с релевантными карточками, сравнениями и procurement kits.

**Текущий прогресс:** опубликованы сравнения по компаниям/контрагентам, адресам/геокодированию, приёму платежей, messaging и погодным данным. Для платежей созданы reviewed profiles ЮKassa, CloudPayments и API интернет-эквайринга Т‑Банка. Для messaging созданы отдельные reviewed profiles Telegram Bot API, SMSC API и SMS.RU API. Для weather созданы отдельные reviewed profiles Open-Meteo, WeatherAPI.com и OpenWeather. Сопоставимые quotes, production limits, SLA, юридические условия, regional quality и общий тест остаются открытыми. Для procurement/tender создан research baseline, выполнен recheck EIS technical-information route и связана legacy dataset note, но активного procurement API comparison пока нет.

Company/counterparty comparison теперь включает recheck конфликта официальных источников по переходу форматов ФНС ЕГРЮЛ/ЕГРИП. Credentialed FTP verification или обновлённое официальное разъяснение всё ещё нужны до утверждений о production file behavior.

## Этап 4 — Распространение и обратная связь

Публиковать материалы в доступной для поиска форме, собирать запросы, отслеживать интерес, общаться с пользователями и предложить ограниченную платную услугу по подбору API.

**Успех:** реальные пользователи применяют Atlas при выборе API.

## Этап 5 — Atlas Pro

Возможные функции: полные сравнительные матрицы, сохранённые shortlist, экспорт, история тарифов и лимитов, уведомления об изменениях, рабочие пространства и приватные заметки.

Разработка начинается только после подтверждённого спроса.

## Этап 6 — Enterprise Intelligence

Возможные функции: приватные каталоги API, владельцы зависимостей, риски поставщиков, мониторинг прекращения поддержки, политики и командные процессы.

## Осознанно отложено

- универсальная графовая база;
- сложные AI-рекомендации;
- тысячи поверхностных импортированных карточек;
- непрозрачный глобальный рейтинг;
- полноценный маркетплейс;
- инфраструктура, не повышающая качество исследований.

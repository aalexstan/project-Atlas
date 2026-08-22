# Источники данных о недвижимости и кадастре

[English version](README.md)

## Быстрый выбор

| Задача | С чего начать | Почему | Главный риск |
|---|---|---|---|
| Юридически значимые сведения об объекте | Выписка ЕГРН | Официальный registry output | Основания доступа и current fee зависят от запроса |
| Регулярные официальные выписки | Пакетный доступ к ФГИС ЕГРН | Official package model существует | Unattended integration и current terms нужно уточнить |
| Карта и контекст территории | НСПД | Официальный spatial-data route | По умолчанию это не unrestricted production API |
| Нормализация адреса или кадастровый номер | DaData Address API | Готовая commercial integration | Не официальная выписка ЕГРН |
| Собственная адресная база | ФИАС/ГАР | Official address provenance | Нужен ETL; это адреса, а не права на недвижимость |

## Важные границы

- Адрес не равен записи о правах на объект.
- Кадастровый номер из enrichment не равен official extract.
- Кадастровая карта не является юридическим доказательством.
- Machine-readable JSON/XML не даёт автоматического права bulk reuse.
- Public frontend endpoints не становятся stable APIs без official docs.

Универсального победителя нет. Сначала выберите юридический тип результата, затем automation, объём, latency и reuse rights.

См. [маршрут задачи](../../needs/real-estate-cadastral-data/README.ru.md), [procurement checklist](../../procurement/real-estate-cadastral-data-selection/README.ru.md) и [comparison data](comparison.json).

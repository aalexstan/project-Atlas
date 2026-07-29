# Изменения интеграции с ФИАС/ГАР

[English version](changes.md)

| Дата | Изменение | Влияние |
|---|---|---|
| 2026-07-29 | Legacy dataset note `datasets/russian_address_registry.md` связана с активной API-first карточкой ФИАС/ГАР. | Сохраняет provenance Pass #2 и делает официальный registry/data-integration route доступным из legacy-слоя. |
| 2026-07-29 | Создана первая API-first карточка data integration на основе официальных страниц ФНС и ФИАС/ГАР. | Добавляет официальный российский адресный реестровый маршрут без описания его как обычного REST-геокодера. |
| 2026-07-29 | Уточнены официальные integration channels: файловые выгрузки, СМЭВ и API services; пользовательские страницы портала отделены от поддерживаемых public APIs. | Улучшает procurement blockers без повышения неизвестных API method details. |
| 2026-07-29 | Добавлены детали official open-data catalog: dataset identifier, XML ZIP data link, structure ZIP, weekly updates, previous releases и KLADR sunset path. | Подтверждает open-data/file route details, сохраняя API-service specification как unknown. |
| 2026-07-29 | Added current official package metadata for `data-28072026-structure-20191024.zip`, visible previous releases, last modification, actuality date and methodological recommendations version. | Narrows file-route uncertainty without claiming archive contents or full/delta semantics were inspected. |
| 2026-07-29 | Inspected official `structure-12032021.zip` archive и recorded 22 XSD schema files; checked data ZIP HTTP headers and size without downloading 57 GB archive. | Подтверждает schema coverage, оставляя production data contents и full/delta semantics как blockers. |
| 2026-07-29 | Inspected current data ZIP central directory via HTTP Range and extracted root `version.txt`. | Подтверждает production file index, archive scale и version marker без скачивания XML payload или доказательства full/delta semantics. |

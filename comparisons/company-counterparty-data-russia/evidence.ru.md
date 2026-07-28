# Доказательства — API данных о компаниях и проверки контрагентов

[English version](evidence.md)

Проверено: **2026-07-23**. Addendum по ГЛОБАС.API проверен: **2026-07-28**.

| ID | Утверждение | Источник | Статус | Комментарий |
|---|---|---|---|---|
| DAD-001 | DaData ищет организацию или ИП по ИНН, ИНН/КПП или ОГРН | [Официальная документация](https://dadata.ru/api/find-party/) | verified | Метод `findById/party` |
| DAD-002 | Максимальная частота метода — 30 запросов/с с одного IP | [Официальная документация](https://dadata.ru/api/find-party/) | verified | Также указано ограничение на создание соединений |
| DAD-003 | Бесплатно доступно до 10 000 запросов в день | [Документация](https://dadata.ru/api/find-party/), [тарифы](https://dadata.ru/pricing/) | verified | Бесплатный тариф включается после регистрации |
| DAD-004 | Годовые тарифы: 14 000 / 28 000 / 56 000 ₽ | [Тарифы](https://dadata.ru/pricing/) | verified | Лёгкий, Расширенный, Максимальный |
| DAD-005 | Полнота данных компаний зависит от тарифа | [Тарифы](https://dadata.ru/pricing/) | verified | Учредители, финансы, долги и контакты доступны на максимальном уровне |
| DAD-006 | Финансовые показатели частично заполнены примерно у 60% действующих компаний | [Поля ответа](https://dadata.ru/api/find-party/) | verified | Формулировка поставщика |
| DAD-007 | Аффилированные компании — отдельный метод и часть максимального тарифа | [Метод](https://dadata.ru/api/find-affiliated/), [тарифы](https://dadata.ru/pricing/) | verified | Не следует считать доступным на всех тарифах |
| KON-001 | API Фокуса поддерживает автозаполнение, массовую проверку, мониторинг, отчёты и анализ связей | [Официальная API-страница](https://focus.kontur.ru/site/api-choice) | verified | Функции перечислены поставщиком |
| KON-002 | В API доступны ЕГРЮЛ/ЕГРИП, банкротства, ФССП, арбитраж, бухотчётность, госконтракты, товарные знаки и лицензии | [Демоверсия реквизитов](https://focus.kontur.ru/site/demo/requisites) | verified | Официальный список источников и данных |
| KON-003 | Фокус предлагает более 30 готовых интеграционных модулей | [Официальная API-страница](https://focus.kontur.ru/site/api) | verified | Заявление поставщика |
| KON-004 | Более 1 400 клиентов используют API Фокуса | [Официальная API-страница](https://focus.kontur.ru/site/api) | reported | Маркетинговая метрика поставщика, независимо не проверялась |
| KON-005 | Есть публичный портал разработчика | [Техническое описание](https://developer.kontur.ru/doc/focus?about=2) | verified | Интерфейс требует JavaScript |
| KON-006 | Демо-доступ предоставляется по заявке | [Заявка на демо](https://focus.kontur.ru/site/order-demo-api) | verified | Менеджер связывается после заявки |
| KON-007 | API проверки по 115-ФЗ и санкциям выделено в отдельное решение | [Выбор API](https://focus.kontur.ru/site/api-choice) | verified | Не смешивать с API контрагентов |
| KON-008 | Точная цена API в текущем исследовании не установлена | [Страница тарифов API](https://focus.kontur.ru/site/price/api-group/counteragent) | unknown | Есть прайс-лист и опции, но нужен расчёт выбранной конфигурации |
| SEL-001 | Seldon.Basis API передаёт данные о компаниях в CRM/ERP | [Официальная API-страница](https://seldongroup.ru/system/basis/api) | verified | Позиционируется как API интеграции данных о контрагентах |
| SEL-002 | Доступны регистрационные данные, арбитраж, госконтракты, гарантии, финансы, ФССП и банкротство | [Официальная API-страница](https://seldongroup.ru/system/basis/api) | verified | Функциональная матрица поставщика |
| SEL-003 | Ответ API предоставляется в JSON | [Официальное описание данных API](https://seldongroup.ru/kakie-dannye-mozhno-poluchit-cherez-api-seldon-basis) | verified | Поставщик прямо указывает JSON |
| SEL-004 | Индивидуальный тариф допускает 10 000 запросов/сутки на метод | [Функциональность продуктов](https://seldongroup.ru/functions) | verified | Вызов каждого метода считается отдельно |
| SEL-005 | Каждый метод индивидуального тарифа оплачивается отдельно | [Функциональность продуктов](https://seldongroup.ru/functions) | verified | Точная цена не опубликована |
| SEL-006 | Seldon предоставляет данные компаний России и СНГ | [Seldon.Basis](https://seldongroup.ru/system/basis), [API](https://seldongroup.ru/system/basis/api) | verified | Перечень стран зависит от продукта и тарифа |
| SEL-007 | Точная публичная цена API не найдена | [Официальная API-страница](https://seldongroup.ru/system/basis/api) | unknown | Веб-тарифы нельзя подменять API-тарифами |
| SEL-008 | На дату проверки сайт показывал предупреждение о DDoS и возможной нестабильности | [Страница API](https://basis.myseldon.com/ru/home/api) | observed | Временное сообщение; требует повторной проверки |
| GLO-001 | У Credinform/ГЛОБАС есть официальная продуктовая страница ГЛОБАС.API | [ГЛОБАС.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | verified | Активная официальная идентичность продукта |
| GLO-002 | Продукт позиционируется для интеграции данных ГЛОБАС в корпоративные системы | [ГЛОБАС.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | provider_reported | Enterprise integration use case |
| GLO-003 | Официальная страница описывает массовую проверку, мониторинг портфеля, обогащение внутренней базы, обновление полей, верификацию данных, архивы и обновление больших баз | [ГЛОБАС.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | provider_reported | Полезно для CRM/ERP/ЭДО и портфельных сценариев |
| GLO-004 | Public API specification, endpoint catalog, authentication, schemas, production limits, SLA и API price не найдены в проверенных официальных страницах | [ГЛОБАС.API](https://globas.credinform.ru/ru-RU/servisy/globas-api), [сервисы](https://globas.credinform.ru/ru-RU/servisy), [requirements](https://globas.credinform.ru/ru-RU/requirements) | observed | Procurement blocker |
| GLO-005 | Трехдневный тест системы ГЛОБАС не подтвержден как API trial | [ГЛОБАС.API](https://globas.credinform.ru/ru-RU/servisy/globas-api) | observed | Нужно подтверждение API credentials или sandbox |
| GLO-006 | «Санкционный комплаенс» считается отдельной product/module boundary, пока не доказано иное | [Санкционный комплаенс](https://globas.credinform.ru/ru-RU/servisy/sanctions) | observed | Не считать частью стандартного API автоматически |
| FTS-001 | ФНС предоставляет открытые данные ЕГРЮЛ/ЕГРИП для интеграции в информационные системы | [Сервис интеграции](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Отдельный режим доступа |
| FTS-002 | Интеграция осуществляется через архивы с XML-файлами и ежедневными изменениями | [Модель взаимодействия](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Не обычный REST API |
| FTS-003 | В архиве может быть до 100 XML-файлов, в файле — до 1 000 записей | [Модель взаимодействия](https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/) | verified | Параметры официального формата выгрузок |
| FTS-004 | Годовой доступ стоит 150 000 ₽ за один реестр и рабочее место | [Порядок доступа](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | verified | Цена для ЕГРЮЛ или ЕГРИП отдельно |
| FTS-005 | Однократный доступ — 50 000 ₽, обновления — 5 000 ₽ | [Порядок доступа](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | verified | Для каждого реестра |
| FTS-006 | Доступ к двум реестрам на год арифметически составляет 300 000 ₽ | [Порядок доступа](https://www.nalog.gov.ru/rn77/service/egrip2/access_order/) | inferred | 150 000 × 2; не включает разработку |
| FTS-007 | До 01.08.2026 одновременно доступны старые и новые форматы | [Сервис интеграции](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | ЕГРЮЛ 4.07/4.08, ЕГРИП 4.06/4.07 |
| FTS-008 | С 01.08.2026 планируется выдача только новых форматов | [Сервис интеграции](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Требует проверки после перехода |
| FTS-009 | Возможны перебои в формировании ежедневных файлов | [Сервис интеграции](https://www.nalog.gov.ru/rn77/service/egrip2/) | verified | Пропущенные сведения включаются позднее |
| FTS-010 | Бесплатная электронная выписка по конкретному лицу подписывается КЭП ФНС | [ЕГРЮЛ и ЕГРИП](https://www.nalog.gov.ru/rn77/related_activities/registries/egrul_egrip/) | verified | Это отдельный веб-сервис, не bulk API |

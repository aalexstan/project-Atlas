# Протокол теста данных о недвижимости и кадастре

[English version](TEST_PROTOCOL.md)

## Выборка

Используйте законно полученные публичные или собственные тестовые объекты. Включите земельные участки, здания, помещения, недавно изменённые и неоднозначные адреса, объекты без кадастрового номера и несколько регионов. Не включайте restricted owner data без зафиксированного legal basis.

## Метрики

- identifier match и false-match rate;
- полнота полей по типам объектов;
- geometry и coordinate reference system;
- update delay относительно dated official evidence;
- частичные, пустые и противоречивые ответы;
- latency percentiles, timeouts и retries;
- цена успешного юридически пригодного результата;
- reproducibility и schema stability.

Фиксируйте provider, method, timestamp, request class, response status и evidence reference. Скриншот карты не заменяет выписку или structured response.

Этот протокол не заявляет, что Atlas уже провёл benchmark.

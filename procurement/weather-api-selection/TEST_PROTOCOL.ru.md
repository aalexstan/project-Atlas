# Протокол benchmark погодных API

[English version](TEST_PROTOCOL.md)

Используйте публичные или синтетические наборы координат и записывайте provider, endpoint, model, query time, response time, variables, timezone и forecast issue time.

Возьмите Москву, Санкт-Петербург и минимум три региона с разным климатом/рельефом. Проверьте current, 24 часа, 3 дня и максимальный заявленный горизонт; precipitation, temperature, wind и alerts; повторные запросы; пропущенные/неоднозначные координаты; historical dates; revisions поставщика. Сравнивайте только с заранее объявленным reference dataset и не называйте результат истиной accuracy без методики. Результаты benchmark в Atlas не заявляются.

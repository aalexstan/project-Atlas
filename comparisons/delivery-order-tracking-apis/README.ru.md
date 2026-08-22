# API заказов доставки и отслеживания отправлений

[English version](README.md)

| Сценарий | Первичный API | Почему | Оговорка |
|---|---|---|---|
| Отследить отправление Почты России | Russian Post Tracking API | Официальная история операций | Не создаёт отправления |
| Создать и вести доставку Yandex | Yandex Delivery API | Жизненный цикл заказа и статусы | Не является multi-carrier tracking |
| Отслеживать несколько перевозчиков | Нужен другой product class | Агрегация - другая задача | Активного профиля Atlas пока нет |

Не сравнивайте carrier tracking, courier dispatch и routing как один API. См. [данные comparison](comparison.json) и [procurement kit](../../procurement/delivery-api-selection/README.ru.md).


# Yandex Rasp API research

## Scope

Review the official Yandex Rasp API for intercity passenger-transport schedules. City routing, city stops and real-time public transport are separate problems.

## Official sources reviewed

- [API introduction](https://yandex.ru/dev/rasp/doc/ru/)
- [API access](https://yandex.ru/dev/rasp/doc/ru/concepts/access)
- [Station list reference](https://yandex.ru/dev/rasp/doc/ru/reference/stations-list)
- [Point-to-point schedule reference](https://yandex.ru/dev/rasp/doc/ru/reference/schedule-point-point)
- [API terms](https://yandex.ru/legal/timetable_api/ru/)

## Confirmed facts

- The API provides programmatic access to intercity passenger-transport route and timetable data.
- It is REST-like over HTTPS GET and returns JSON or XML.
- Access requires an activated API key sent on each request as `apikey` or in the Authorization header.
- Documented resources include station lists, station schedules and routes between stations; the station-list JSON is about 40 MB.
- Official documentation recommends migration from `api.rasp.yandex.net` to `api.rasp.yandex-net.ru` because availability of the former is not guaranteed.
- The reviewed terms allow use only in free publicly accessible websites or mobile applications, require attribution, and restrict data storage/processing/modification except temporary caching for service functionality.

## Unknowns and blockers

- Public request quotas, production SLA, support commitment and permitted commercial terms beyond the published free-use terms are unknown.
- No API key, live call or schedule-quality benchmark was used.

## Decision

Create a reviewed profile for free public timetable features. Do not recommend it for a paid/closed SaaS or long-term schedule database without written agreement from Yandex.


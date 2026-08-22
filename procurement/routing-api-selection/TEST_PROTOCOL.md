# Routing benchmark protocol

[Русская версия](TEST_PROTOCOL.ru.md)

Use only synthetic, public or otherwise authorized data. Do not send personal or customer data.

- Test Moscow, Saint Petersburg, regional cities and at least one cross-region route.
- Test direct routes, multiple stops, distance matrices and repeated requests.
- Include walking, driving and, where documented, truck restrictions.
- Include ambiguous coordinates, disconnected points, toll roads and long routes.
- Record request payload class, provider version, response code, distance, duration, route alternatives and match status.
- Measure latency percentiles, error rate, timeout rate, missing routes, false positives and reproducibility.
- Compare coordinate order, units, geometry format, traffic assumptions and time-of-day behavior.
- Do not treat a public demo endpoint as a production SLA or live Atlas verification.


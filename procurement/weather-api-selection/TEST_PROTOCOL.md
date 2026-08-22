# Weather API Benchmark Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

Use public or synthetic coordinate sets and record the provider, endpoint, model, query time, response time, variables, timezone and forecast issue time.

Sample Moscow, Saint Petersburg and at least three regions with different climate/terrain. Test current, 24-hour, 3-day and maximum advertised horizon; precipitation, temperature, wind and alerts; repeated calls; missing/ambiguous coordinates; historical dates; and provider revisions. Compare only against a declared reference dataset and never call the result an accuracy truth without methodology. No benchmark results are claimed in Atlas.

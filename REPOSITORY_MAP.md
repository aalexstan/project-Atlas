# Atlas Repository Map

[Русская версия](REPOSITORY_MAP.ru.md)

Use this path when you want to use Atlas as a decision aid rather than maintain the repository.

1. Start with [`README.md`](README.md) for the project purpose and rules.
2. Start with [`NEEDS_INDEX.md`](NEEDS_INDEX.md) when you have a product problem but no provider shortlist.
3. Open a need route in [`needs/`](needs/), which explains the scenario and points to relevant materials.
4. Open [`COMPARISON_INDEX.md`](COMPARISON_INDEX.md) when you need a scenario-based shortlist and trade-offs.
5. Open [`API_INDEX.md`](API_INDEX.md) when you already know which API or data route you want to inspect.
6. Read an API profile in [`apis/`](apis/) for scope, maturity, sources, unknowns, and practical risks.
7. Read [`research/`](research/) only when you need the evidence trail behind a conclusion.
8. Use [`procurement/`](procurement/) for provider questions, test protocols, RFPs, and purchase preparation.
9. Read [`docs/`](docs/) for methodology and maintenance rules, not as the first product tour.
10. Treat [`legacy/`](legacy/), [`datasets/`](datasets/), [`providers/`](providers/), and [`catalog/`](catalog/) as supporting or historical layers.

For repository maintenance, use [`scripts/generate_indexes.py`](scripts/generate_indexes.py) and [`scripts/validate_atlas.py`](scripts/validate_atlas.py). They are maintenance tools, not API data sources.

# Atlas Data Schemas

[Русская версия](README.ru.md)

These schemas describe the machine-readable contract for active Atlas records.

## Contracts

- [API profile schema](api-profile.schema.json) - one bounded API or integration route.
- [Comparison schema](comparison.schema.json) - a scenario-based comparison.
- [Need schema](need.schema.json) - a user-task route.

All active records use `schema_version: 1`. The repository validator enforces the fields that can be checked without a third-party JSON Schema library. Unknown provider facts remain explicit values such as `unknown`, `needs_recheck` or `not_applicable`.

Legacy JSON under `legacy/`, `catalog/`, `companies/`, `datasets/`, `providers/` and `access_methods/` is outside these active contracts.

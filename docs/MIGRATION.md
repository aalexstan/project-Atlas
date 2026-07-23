# Migration to the API-First Model

[Русская версия](MIGRATION.ru.md)

## Why Migration Is Needed

The current repository describes Dataset as the primary entity and API as an access method. Atlas is returning to an API-first public product focused on selection, comparison, and monitoring.

Dataset research is not wasted. It becomes supporting evidence for API evaluation.

## Rules

1. Do not delete useful historical research.
2. Do not move everything in one unreviewed change.
3. Migrate content when it is touched or verified.
4. Preserve source notes and provenance.
5. Mark stale or uncertain material explicitly.
6. Avoid duplicate active profiles.

## Concept Mapping

| Previous concept | New role |
|---|---|
| Dataset | Data-coverage information supporting an API profile |
| Provider | Shared provider context |
| Access method | Technical access section of an API profile |
| Relationship graph | Optional future derived view |
| Catalog card | Candidate for migration into a profile |
| Research report | Evidence or research log |
| Rating table | Deferred until scoring is public and validated |

## Incremental Process

1. Add the new root README files and project documents.
2. Create `apis/`, `comparisons/`, and `needs/` for new work.
3. Build the DaData gold-standard profile.
4. Migrate only legacy cards required for the first comparison.
5. Move historical-only material under `legacy/` only after review.

## Source of Truth

For new work:

- API facts live in API profiles;
- comparative conclusions live in comparisons;
- raw investigation notes live in research logs;
- material product changes live in change records.

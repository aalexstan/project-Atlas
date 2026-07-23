# Project Atlas — Instructions for Codex

## Product Direction

Project Atlas is an **API-first independent intelligence platform**.

Its purpose is to help developers and organizations choose APIs by verifying facts, comparing realistic alternatives, explaining trade-offs, and tracking material changes.

Atlas is not:

- a copy of API Portal or another link directory;
- a dataset-first encyclopedia;
- a marketplace whose rankings can be purchased;
- a collection of unverified marketing summaries.

## Non-Negotiable Rules

1. Keep the API profile as the primary public entity.
2. Preserve useful legacy dataset research; migrate incrementally and never delete provenance without an explicit task.
3. Maintain public navigation and major README documents in both English and Russian.
4. Use English names for machine-readable keys, JSON fields, schemas, and code identifiers.
5. Prefer official or primary sources. Never invent missing facts.
6. Use explicit states such as `unknown`, `needs_recheck`, `provider_reported`, and `not_applicable`.
7. Separate verified facts, provider claims, observations, inferences, and editorial recommendations.
8. Do not substitute a web-product price for an API price.
9. Do not introduce a global vendor ranking without a public evidence-based scoring method.
10. Recommendations must be scenario-specific.
11. Do not claim that live testing was performed unless test evidence is present in the repository.
12. Never commit credentials, tokens, certificates, customer data, or personal identifiers.

## Repository Conventions

```text
apis/<slug>/
    README.md
    README.ru.md
    api.json
    evidence.md
    evidence.ru.md
    changes.md
    changes.ru.md

comparisons/<slug>/
    README.md
    README.ru.md
    comparison.json
    evidence.md
    evidence.ru.md
    changes.md
    changes.ru.md

research/<topic>/
procurement/<topic>/
docs/
templates/
scripts/
```

## Validation Required Before Completion

Run:

```bash
python3 scripts/validate_atlas.py
```

Also check:

- JSON parses successfully;
- bilingual file pairs exist where required;
- relative Markdown links resolve;
- no absolute local paths are committed;
- no credentials or secrets are present;
- generated indexes reflect active API-first paths rather than legacy cards.

## Editing Behavior

- Inspect the existing repository before moving or replacing files.
- Make minimal, reviewable changes.
- Prefer logical commits over one huge commit.
- Do not rewrite research facts merely for stylistic consistency.
- When source data conflicts, retain both claims and mark the conflict.
- If browsing is available, use current official sources and record the verification date.
- If browsing is unavailable, do not silently update time-sensitive facts.

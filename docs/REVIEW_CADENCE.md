# Review Cadence

[Русская версия](REVIEW_CADENCE.ru.md)

This policy turns the methodology review guidance into an operating model for maintained Atlas materials.

## Scope

Applies to active:

- API profiles in `apis/`;
- comparisons in `comparisons/`;
- need routes in `needs/`;
- procurement kits in `procurement/`;
- templates and validation scripts when they affect public materials.

Legacy materials keep provenance value, but they do not need the same cadence unless they are being migrated into active API-first work.

## Review Intervals

| Area | Target interval | Why |
|---|---:|---|
| Pricing and billing units | 90 days | Prices, packages, free tiers and overage rules change quickly. |
| Public limits and quotas | 90 days | Rate limits and plan limits can change without large product announcements. |
| Product availability and official identity | 90 days | APIs can be renamed, moved, retired or folded into another product. |
| Documentation, methods and versioning | 180 days | Specifications, fields and examples change, but usually less often than pricing. |
| Legal terms and data rights | 180 days | Storage, caching, display, redistribution and SaaS rights are procurement-critical. |
| Comparisons and need routes | 180 days | Scenario recommendations depend on the underlying profiles staying current. |
| Gold profiles | 90 days minimum | Gold requires a maintained high-confidence reference, not only a one-time review. |

Known external dates override the table. Example: the FTS EGRUL/EGRIP format migration scheduled for 2026-08-01 requires a targeted recheck after that date.

The automated due-review check uses the shortest profile-wide interval of 90 days for API profiles, 180 days for comparisons and needs, and an earlier parseable `next_review` date when declared.

## Review Triggers

Review immediately when any of these happens:

- provider announces pricing, product, legal, API version or endpoint changes;
- official documentation URL changes or stops resolving;
- a profile gets a provider answer, sandbox, quote or contract appendix;
- live testing evidence becomes available;
- an API appears in a new comparison or need route;
- validator, generator or template rules change;
- a legacy claim is promoted into an active profile.

## Ownership Model

Atlas uses role ownership, not personal ownership, unless a maintainer explicitly assigns names outside this repository.

| Role | Responsibility |
|---|---|
| Research owner | Verifies official sources, updates evidence, keeps `last_verified` accurate. |
| Editorial owner | Keeps scenario recommendations, English/Russian parity and source-status wording coherent. |
| Technical owner | Maintains JSON validity, generated indexes, validator rules and link health. |
| Procurement owner | Tracks provider-request checklists, quotes, SLA/support evidence and commercial blockers. |
| Legal reviewer | Reviews storage, caching, display, redistribution, SaaS, affiliate and model-training rights. |

If a role is unassigned, write `unassigned` in the working notes or backlog. Do not invent a person or organization.

## Review States

Use these states in TODOs, changelogs or working notes:

- `on_schedule` - not due yet;
- `due` - target review date has arrived;
- `overdue` - due and not reviewed;
- `blocked_provider` - needs provider answer, quote or private documentation;
- `blocked_credentials` - needs lawful test access;
- `blocked_legal` - needs legal or contract review;
- `blocked_source` - official source is inaccessible or incomplete;
- `legacy_only` - preserved for provenance, not active methodology;
- `superseded` - replaced by a newer active route.

## Updating Dates

Update `last_verified` only after rechecking the relevant official or primary source for the fact being claimed.

Do not update `last_verified` for:

- copy edits;
- navigation changes;
- provider-request checklist creation;
- TODO/SUMMARY/CHANGELOG edits;
- legacy linkage;
- generated index refreshes.

Partial reviews should be recorded in `changes.md`, evidence tables or research logs with the exact scope. Do not imply that the full profile was reverified.

## Evidence Rules

- Keep verified, observed, provider-reported, inferred, unknown and needs-recheck separate.
- Never turn a provider-request question into an answer.
- Never claim live testing without saved test evidence.
- Never use web-product pricing as API pricing.
- Record contradictions instead of resolving them by guesswork.

## Review Workflow

1. Pick the active profile, comparison, need route or procurement kit.
2. Read current `README*`, `api.json` or `comparison.json`, `evidence*`, `changes*` and related research logs.
3. Check official sources for the scope of the review.
4. Update evidence and open questions before updating recommendations.
5. Update `last_verified` only for the scope actually rechecked.
6. Run `python3 scripts/generate_indexes.py`, `python3 scripts/generate_indexes.py --check` and `python3 scripts/validate_atlas.py`.
7. Record material changes in `changes.md` / `changes.ru.md`.
8. Update `TODO.md`, `SUMMARY.md` and `CHANGELOG.md` if the project state changed.

## Gold Gate

An API profile cannot become Gold while any of these are unresolved:

- no assigned research and editorial ownership;
- missing live-test evidence for workflows that claim live testing;
- unresolved pricing or data-rights blockers for the recommended scenario;
- no comparison coverage for a realistic alternative;
- stale `last_verified` date for pricing, limits or legal terms;
- validator or generated index failures.

# Research Methodology

[Русская версия](METHODOLOGY.ru.md)

## Purpose

This methodology defines the minimum repeatable process for creating and maintaining an Atlas API profile.

## Workflow

### 1. Define the User Need

Record the problem, expected inputs and outputs, geography, expected volume, latency or availability requirements, and legal or commercial constraints.

### 2. Discover Candidates

Use catalogs, provider websites, official registries, search engines, industry reports, GitHub organizations, and SDK repositories. Discovery sources identify candidates; they do not automatically verify claims.

### 3. Confirm the Official Identity

Confirm the official product name, provider, official website, documentation, product status, and supported market.

### 4. Verify Technical Access

Check protocols, base URLs, authentication, versioning, formats, core endpoints, sandbox, specifications, SDKs, and asynchronous mechanisms such as webhooks.

### 5. Verify Commercial Terms

Check free tier or trial, price units, included volume, overage, commitments, negotiated pricing, rate limits, support, SLA, and restrictions on commercial use, caching, storage, redistribution, and resale.

Do not infer permission from technical possibility.

### 6. Evaluate Developer Experience

Assess onboarding, documentation structure, examples, error references, changelog, version policy, support channels, and time to first successful request when tested.

### 7. Identify Alternatives

Include realistic alternatives that solve substantially the same user need. Explain where each is stronger, weaker, cheaper, broader, simpler, or safer.

### 8. Record Risks

Examples include unclear pricing, no public SLA, dependency on one registry, undocumented limits, stale SDKs, breaking-change risk, unclear data rights, and provider instability.

### 9. Write a Scenario-Based Verdict

State who the API is best for, who should avoid it, when to choose an alternative, and which questions remain unresolved.

### 10. Store Evidence and Dates

Every material fact should have a value, source, verification date, status, and optional note.

## Evidence Status

- `verified` — directly confirmed by a primary source;
- `observed` — confirmed through a reproducible test;
- `reported` — stated by a secondary source;
- `inferred` — reasoned conclusion from cited facts;
- `unknown` — no reliable answer found;
- `needs_recheck` — previously known but may be stale;
- `not_applicable` — does not apply.

## Source Priority

1. Official product documentation.
2. Official pricing and legal terms.
3. Official specification or repository.
4. Official support or status communication.
5. Government or primary registry.
6. Reputable secondary research.
7. Community reports and discussions.

## Review Cadence

Suggested targets:

- pricing and limits: every 90 days;
- documentation and versions: every 180 days;
- legal terms: every 180 days;
- product availability: every 90 days;
- gold profiles: at least every 90 days;
- after a material provider announcement: immediately.

Every profile must display its last verified date.

Operational ownership, stale-risk states and review triggers are defined in [Review Cadence](REVIEW_CADENCE.md).

## Definition of Done

A profile reaches **Verified** when it includes confirmed identity, purpose, authentication, public pricing status, limits or explicit unknown states, commercial-use notes, at least two realistic alternatives, sources, and a verification date.

A profile reaches **Gold** only after independent review, comparison coverage, and a maintenance process exist.

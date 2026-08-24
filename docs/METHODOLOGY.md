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

## Reproducible Live-Test Gate

Live testing and source monitoring are different mechanisms. The weekly source monitor checks whether public documentation or health URLs respond over credential-free HTTP; it does not establish API behavior, data quality, quotas or commercial rights. A live-test record is an empirical research artifact with raw responses and a bounded test protocol.

An API may be marked `live_tested: true` only when a repository file named `research/<slug>/live-test-YYYY-MM-DD.md` (and its Russian pair) contains:

- a legal access statement: public/free endpoint or explicitly authorized test credentials;
- confirmation that the applicable free-tier or test-access Terms of Service permit the specific automated test, or a reference to the written authorization;
- a pre-test list of `core claims`, each with a stable identifier and a link to the relevant `api.json`, README, evidence or open-question entry; the list must be written before requests are executed and must not be selected retrospectively to fit the results;
- core claims spanning all three required dimensions: (1) identity/purpose, (2) primary response contract, and (3) at least one commercial, quota, rate-limit or other procurement-block claim, including an explicit `unknown` where it cannot be empirically tested;
- three to five realistic requests covering the core claims;
- at least one intentional invalid-input request;
- raw response payloads, HTTP codes, latency and observed error behavior;
- a rate-limit observation that does not require deliberately exhausting a quota;
- a claim-by-claim comparison against the existing profile;
- separate findings for every mismatch, unknown or untested commercial/legal claim;
- reproduction instructions without secrets or personal data.

The pre-merge review is a required paired artifact at `reviews/<slug>-live-test-YYYY-MM-DD.md` (and its Russian pair). The review must be linked from the live-test record, inspect the staged diff, verify that the pre-test core-claim list was not changed after execution, and record a merge recommendation.

The profile must record `live_tested_on` and `live_test_valid_until` when `live_tested: true`. The validity date follows the shortest applicable review cadence among the tested claims; for pricing, limits and access rights this is normally 90 days. Once the validity date passes, the live-test evidence is historical and the profile must not present it as current: rerun the test or set `live_tested: false` and mark the claims `needs_recheck`.

Live testing does not automatically promote `reviewed` to `verified`. Promotion is allowed only after the required human-readable review confirms that the tested core claims match the profile and every untested quota, SLA, accuracy, pricing, licensing or data-rights claim remains explicit. If an ordinary test request unexpectedly returns `429` or `Retry-After`, record it as a valid rate-limit finding; do not hide it by repeating the test until it succeeds.

This pre-merge review is a procedural consistency gate, not independent review. It does not satisfy the independent-review requirement for `Gold`.

Use this conflict rule:

- a material conflict with core identity, purpose, authentication, primary response contract or primary capability is a mandatory maturity downgrade: the profile may not exceed `discovered` until resolved; if product identity itself is unsupported, retain only a discovery/decision record;
- a conflict limited to a secondary claim is a finding that blocks promotion until explained, but the current maturity may be retained with the conflict explicit;
- an unmeasured quota, SLA, accuracy, pricing, licensing or data-rights claim remains `unknown` and is not treated as a conflict merely because it was not tested.

Public empirical evidence can confirm a request contract and observed error behavior. It cannot by itself confirm a contractual SLA, paid quota, commercial license, production accuracy or rights to store and redistribute data; those require official terms, provider confirmation or a separate lawful benchmark.

## Definition of Done

A profile reaches **Verified** when it includes confirmed identity, purpose, authentication, public pricing status, limits or explicit unknown states, commercial-use notes, at least two realistic alternatives, sources, and a verification date.

A profile reaches **Gold** only after independent review, comparison coverage, and a maintenance process exist.

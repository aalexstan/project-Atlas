# Review: Geoapify Live Test — 2026-08-25

[Russian version](geoapify-geocoding-api-live-test-2026-08-25.ru.md)

## Review scope

Procedural pre-merge review of the first Geoapify live test, including the pre-registered four-dimensional claim list, raw payloads, request spacing and attribution signals.

## Checklist

- [x] The pre-registered plan predates the requests.
- [x] Identity/purpose, response contract, rate-limit/policy and licensing/attribution are separate dimensions.
- [x] Three individual requests were used with a conservative delay.
- [x] No batch, bulk, autocomplete load, scraping, parallel load or quota exhaustion was performed.
- [x] Raw JSON payloads, HTTP status and latency are preserved without the API key.
- [x] Forward and reverse response shapes were observed.
- [x] The synthetic unknown query returned an empty result.
- [x] OpenStreetMap attribution and Open Database License signals were observed in non-empty responses.
- [x] Quota threshold, pricing behavior, SLA, accuracy, storage, caching, redistribution and SaaS remain unknown.
- [ ] Account-specific accepted terms were independently captured.

## Findings

1. The three requests provide bounded empirical evidence for authenticated forward, reverse and unknown-input response behavior.
2. The test does not establish accuracy, production suitability, a rate-limit threshold or commercial data rights.
3. The account-specific terms acceptance was not captured as evidence; this blocks profile-level live-test validity until reviewed.

## Review conclusion

The evidence is readable and technically reproducible as a narrow test. It must not be treated as a benchmark or legal approval. This is a procedural self-review, not independent review for Gold.

Keep `maturity: reviewed`, `live_tested: false` and validity dates unset until a human reviewer accepts the evidence and resolves the access/terms finding.

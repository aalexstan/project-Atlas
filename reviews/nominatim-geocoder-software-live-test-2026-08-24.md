# Review: Nominatim Public Instance Live Test

[Russian version](nominatim-geocoder-software-live-test-2026-08-24.ru.md)

## Review scope

Procedural pre-merge review of the first address/geocoding live-test, including the public usage policy, raw payloads, attribution/licence signals and policy-safe request spacing.

## Checklist

- [x] Candidate selection and canonical OSMF policy URL are documented.
- [x] The pre-test core-claim list was written before the requests.
- [x] Core claims cover identity/purpose, response contract, operational limits and licensing/attribution.
- [x] Public policy requirements for one request per second, custom User-Agent/Referer, attribution, autocomplete prohibition and bulk restrictions are recorded.
- [x] Three individual geocoding requests were used; no autocomplete, batch or bulk endpoint was tested.
- [x] Requests were separated by at least two seconds.
- [x] Raw JSON payloads, HTTP codes and latency are preserved.
- [x] The unknown query returned an empty result and was not treated as proof of accuracy.
- [x] Attribution/licence values were observed in raw responses and compared with OSMF copyright guidance.
- [x] The review distinguishes observed direct geocoding from documented-only reverse geocoding.
- [x] Storage, caching, redistribution, SLA, accuracy and quota threshold remain unknown.
- [x] No credentials, personal data or binary files were added.

## Findings

1. The public instance returned JSONv2 and GeocodeJSON responses for two individual address/place queries.
2. The unknown query returned HTTP 200 with an empty array; this is bounded behavior only, not a general accuracy guarantee.
3. Raw responses exposed OpenStreetMap attribution and ODbL signals.
4. The test did not and must not establish autocomplete, bulk suitability, quota threshold, storage, caching or redistribution rights.
5. Reverse geocoding was not tested and is not included in the observed capability evidence for this run.

## Review conclusion

The evidence is readable and policy-compliant as a bounded public-instance test. It supports observed request/response and attribution findings, but does not promote maturity or establish contractual/data-rights claims.

This is a procedural self-review, not independent review for Gold. A human review is still required before setting `live_tested_on` or `live_test_valid_until` in `api.json`.

## Merge recommendation

Merge the research and review artifacts if the human reviewer accepts the policy boundary. Keep `live_tested: false` and leave validity dates unset until that human review is completed.

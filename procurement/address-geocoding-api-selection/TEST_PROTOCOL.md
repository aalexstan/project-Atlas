# Address and Geocoding API Test Protocol

[Русская версия](TEST_PROTOCOL.ru.md)

This protocol defines how to test candidate APIs after providers approve credentials and legal test conditions. It does not contain real benchmark results.

## Test Sample

Use a legal synthetic or public sample. Do not use private customer addresses unless legal approval and data-processing agreements are in place.

Include:

- Moscow;
- Saint Petersburg;
- large regional cities;
- smaller regional towns;
- rural/locality addresses;
- new addresses;
- old or renamed addresses;
- streets with common names;
- addresses with building, corpus, structure and room details;
- ambiguous addresses;
- addresses with typos;
- addresses without house number;
- coordinates for reverse geocoding.
- POI and organization names for products that explicitly support place search;
- OpenStreetMap-derived public examples only when their license permits benchmark use.

## Test Tasks

| Task | Input | Expected evidence |
|---|---|---|
| Suggestions | Partial address strings | Relevant ordered suggestions and returned fields. |
| Cleaning | Messy address strings | Canonical fields, quality codes, registry identifiers. |
| Direct geocoding | Full and partial addresses | Coordinates, match level, precision, ambiguity. |
| Reverse geocoding | Coordinates | Returned address, object level, distance or confidence if available. |
| Organization/place search | Organization names or POI queries | Only for products that explicitly support places. |
| Batch | File/list of addresses | Throughput, error handling, legal batch permission. |
| Public hosted policy check | End-user-triggered and automated patterns | Whether the scenario is permitted by public usage policy. |
| Self-hosting ops check | Import/update plan and target volume | Hardware, storage, update cadence, monitoring and rollback plan. |

## Metrics

Record:

- exact match rate;
- house-level match rate;
- street/locality-only match rate;
- false positives;
- missing results;
- duplicate or ambiguous results;
- coordinate precision;
- returned match level / quality code;
- latency p50/p95/p99;
- error rate;
- retry behavior;
- quota behavior;
- cost per 1,000 accepted records;
- cost per 1,000 successful geocodes;
- storage/caching rights confirmed for results.
- attribution and license obligations;
- operational effort for self-hosted or registry-data routes.

## Procedure

1. Freeze the sample and assign stable row IDs.
2. Record provider, product, method, plan, region, credentials type and date.
3. Run each API with documented parameters only.
4. Store raw responses only if the provider contract permits it.
5. Normalize outputs into a neutral evaluation table.
6. Review possible false positives manually.
7. Separate API errors from no-match results.
8. Record all unknowns and provider clarifications.
9. Do not publish raw provider responses if licensing prohibits it.
10. For public Nominatim, do not run autocomplete, bulk or stress tests against the OSMF instance.
11. For FIAS/GAR, do not treat website search endpoints as supported integration APIs unless documented by FNS.

## Reporting

Report results by scenario, not as a universal winner:

- best address-entry UX;
- best cleaning quality;
- best geocoding precision;
- best official registry provenance;
- best legal fit for storage/SaaS;
- lowest projected TCO for the target volume.

Do not create an Atlas Score unless the public method and evidence are included.

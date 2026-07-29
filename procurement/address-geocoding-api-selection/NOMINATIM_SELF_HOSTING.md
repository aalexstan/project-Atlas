# Nominatim Self-Hosting Checklist

[Русская версия](NOMINATIM_SELF_HOSTING.ru.md)

Use this checklist when Nominatim is being considered as a self-hosted geocoding route. It is not legal advice and it does not include benchmark results.

## Boundary

- Do not use public `nominatim.openstreetmap.org` for autocomplete, bulk geocoding, stress tests, API resale or primary production geocoding.
- Decide whether the production route is self-hosted Nominatim or a commercial third-party provider.
- Treat OpenStreetMap attribution and ODbL obligations as legal-review items.

## Scope Questions

- Which countries or regions are required?
- Is the service forward geocoding, reverse geocoding, POI search, address lookup or export to another search engine?
- Is autocomplete required? If yes, Nominatim public service is not acceptable and a separate autocomplete design is needed.
- Is the service internal-only, customer-facing or a public API?
- What request volume, latency target, uptime target and freshness target are required?

## Import Planning

- Choose full planet or extracts.
- Choose import style: `admin`, `street`, `address`, `full` or `extratags`.
- Decide whether updates are required before using `--no-updates`.
- Use flatnode storage for large imports and budget at least 75GB for the flatnode file.
- Budget full-planet infrastructure separately from country/regional extracts.
- Record whether optional Wikipedia/Wikidata importance and postcode data are used.

## Capacity Planning

- Minimum installation RAM is not production capacity.
- Full-planet import needs a high-memory machine, fast disks and long import window.
- Include disk growth, backups, WAL/archive logs, monitoring data and rollback storage.
- Benchmark target extracts before committing to production hardware.
- Test p50/p95/p99 latency under expected concurrency.

## Updates and Freshness

- Select replication source and interval.
- Run `nominatim replication --init` and confirm the start date.
- Prefer systemd-managed one-time updates for regular operation.
- Document catch-up behavior after downtime.
- Monitor replication lag and update failures.
- Keep flatnode files if updates are enabled.

## Deployment and Security

- Do not use the Nominatim test server in production.
- Use a production frontend such as gunicorn behind nginx or an equivalent supported deployment.
- Add authentication, rate limiting and abuse protection when exposing the service.
- Define logging, privacy, deletion and incident-response rules.
- Separate import/update jobs from request-serving capacity.

## Legal and Data Rights

- Confirm attribution wording and display location.
- Review ODbL obligations for caches, derived databases, exports and SaaS embedding.
- Decide whether customer-submitted addresses may be processed under the chosen privacy model.
- Document data retention and deletion rules.

## Go / No-Go Gates

| Gate | Required evidence |
|---|---|
| Product boundary | Public service excluded or explicitly policy-compliant. |
| Data scope | Extract/full-planet choice and import style documented. |
| Operations | Import, update, backup, monitoring and deployment plan. |
| Performance | Reproducible benchmark on target data and hardware. |
| Legal | ODbL, attribution, privacy and SaaS review completed. |

No Atlas live testing has been performed for this checklist.

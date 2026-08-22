# Nominatim Self-Hosting Operations Recheck

Date: 2026-07-29

## Scope

This log refines the technical operations side of self-hosted Nominatim: prerequisites, import sizing, update process and production deployment. It does not provide legal advice on ODbL or derived databases.

## Official Sources Reviewed

- https://nominatim.org/release-docs/latest/admin/Installation/
- https://nominatim.org/release-docs/latest/admin/Import/
- https://nominatim.org/release-docs/latest/admin/Update/
- https://nominatim.org/release-docs/latest/admin/Deployment-Python/
- https://operations.osmfoundation.org/policies/nominatim/

## Confirmed Facts

- Nominatim requires PostgreSQL, PostGIS, osm2pgsql and Python 3 for running the software.
- The documentation recommends PostgreSQL 13+ and PostGIS 3.2+ even though lower listed versions can work.
- The installation page states a minimum of 2GB RAM and strongly recommends 128GB RAM or more for a full planet import; it says at least 64GB RAM is expected before reporting out-of-memory problems.
- Full-planet installation requires at least 1TB of disk and fast disks; NVMe is recommended.
- Full-planet import is described as around 2.5 days on a well-configured machine, with 4-5 days more realistic on traditional SSDs.
- Large imports such as Europe, North America or the planet should use flatnode storage; the flatnode file needs at least 75GB free space.
- Default setup imports the full OSM planet; smaller extracts can reduce size and import time.
- Nominatim supports import styles including `admin`, `street`, `address`, `full` and `extratags`.
- The import documentation provides rough 2020 planet estimates for 64GB RAM / 4 CPU / NVMe: `admin` 4h/215GB, `street` 22h/440GB, `address` 36h/545GB, `full` 54h/640GB, `extratags` 54h/650GB before drop.
- `--no-updates` can drop data required for dynamic updates, but it should not be used when later updates or additional data are required.
- `--reverse-only` can be used for reverse lookup or export-only scenarios and saves about 5% disk space.
- Update documentation describes online replication, default global minutely diffs, configurable replication URL/update interval and one-time, catch-up and continuous modes.
- Continuous updates are no longer recommended; the docs recommend systemd-based regular updates.
- The deployment page describes a Python ASGI frontend with Falcon or Starlette, gunicorn, systemd socket/service and nginx proxying.
- The import docs say the test server must not be used in production.

## Observations

- Nominatim production suitability is mostly an operations question once public-instance use is excluded.
- A Russia-only or region-only use case should evaluate OSM extracts before assuming full-planet infrastructure.
- Import style selection changes storage and quality trade-offs; `address` may fit geocoding without POI search, while `full` or `extratags` are heavier.
- Update requirements must be decided before import because `--no-updates` changes the database structure.

## Unknowns

- Exact hardware and disk sizing for the user's target countries, data extract, import style and traffic.
- Throughput/latency for the target workload.
- Backup, replication, failover and disaster recovery design.
- Security model, authentication, abuse protection and rate limiting for a self-hosted public endpoint.
- ODbL obligations for the exact cache/database/SaaS model.

## Live Testing Status

No Atlas import, benchmark, deployment or public-instance load test was performed.

## Decision

Update the Nominatim profile and procurement kit with an explicit self-hosting operations checklist. Keep legal review and performance benchmarking as blockers before production recommendation.

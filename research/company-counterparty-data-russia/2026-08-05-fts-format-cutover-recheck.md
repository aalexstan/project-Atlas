# FTS EGRUL/EGRIP Format Cutover Recheck - 2026-08-05

## Scope

This log rechecks the official Russian Federal Tax Service public pages after the scheduled 2026-08-01 transition for EGRUL/EGRIP integration formats.

It does not test credentialed FTP access, download current registry files, inspect post-cutover directory contents or validate XML payloads.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Integration service page | https://www.nalog.gov.ru/rn77/service/egrip2/ | Public service identity, integration mode, post-cutover format statement |
| Interaction model and formats | https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/ | FTP/archive model, directory model, full/daily data model, format transition statement |
| Access process and fees | https://www.nalog.gov.ru/rn77/service/egrip2/access_order/ | Access model, fees, credentials and certificate package |

## Confirmed Facts

- FTS still identifies the service as integration and access to EGRUL/EGRIP data for use in information systems.
- The dedicated integration mode provides files for use in information systems; the regular search mode is not a file-export mode.
- The reviewed public pages still describe FTP archive delivery with XML files, full historical data to the start of the year and daily changes after that.
- The public FTS pages rechecked after 2026-08-01 state that from 2026-08-01 delivery is only in EGRUL 4.08 and EGRIP 4.07 formats.
- The access and fee page still lists RUB 150,000 for annual subscription per registry/workstation, RUB 50,000 for one-time full data and RUB 5,000 for one-time updated data.
- Access materials still describe access attributes, password and a `*.p12` certificate package.

## Observations

- The public pages were crawled after the scheduled cutover date, but some wording still includes transitional context such as old and new formats being supplied "currently"; Atlas treats the explicit "from 2026-08-01 only 4.08/4.07" statement as the public post-cutover position.
- The public pages do not expose credentialed FTP directory listings, current filenames, checksums or sample XML payloads without access.

## Unknowns and Blockers

- Actual post-cutover FTP directory names and file availability.
- Whether old-format directories are absent from credentialed FTP access after 2026-08-01.
- Current XML schemas, sample payloads and validation behavior for EGRUL 4.08 and EGRIP 4.07 in production files.
- Operational recovery behavior when daily files are delayed.
- Contractual rights for redistribution, SaaS embedding and paid third-party access.

## Live Testing Status

No live testing was performed. Atlas did not obtain access attributes, password, `.p12` certificate or FTP directory access.

## Decision

Keep `apis/fns-egrul-egrip-integration/` at `reviewed` maturity and update `last_verified` to 2026-08-05 for the public post-cutover source recheck.

The active recommendation remains unchanged: FTS EGRUL/EGRIP integration is the primary official registry feed for building an internal data platform, not a turnkey counterparty-checking API. Production selection still requires credentialed FTP verification and legal review.

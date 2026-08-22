# FTS EGRUL/EGRIP Format Conflict Recheck - 2026-08-15

## Scope

This log rechecks the official FTS public material about EGRUL/EGRIP integration after the scheduled 2026-08-01 cutover.

It focuses on whether official sources now agree on post-cutover file formats.

It does not test credentialed FTP access, directory listings, checksums or XML payloads.

## Official Sources Reviewed

| Source | URL | Use |
|---|---|---|
| Integration service page | https://www.nalog.gov.ru/rn77/service/egrip2/ | Current public delivery wording |
| Interaction model and formats | https://www.nalog.gov.ru/rn77/service/egrip2/egrip_vzayim/ | Directory/file model and current wording |
| Access process and fees | https://www.nalog.gov.ru/rn77/service/egrip2/access_order/ | Access model and fees |
| FTS order No. ED-7-14/613@ | https://www.nalog.gov.ru/rn77/about_fts/docs/16493030/ | Normative requirement for version 4.08/4.07 rollout |

## Confirmed Facts

- The integration service page and the interaction-model page still state that files are currently uploaded in both old formats EGRUL 4.07 / EGRIP 4.06 and new formats EGRUL 4.08 / EGRIP 4.07.
- The same public pages also state: "Начиная с 1 августа 2026 года - только в форматах 4.08 и 4.07."
- FTS Order No. ED-7-14/613@ states in point 6 that from 2026-08-01 data should be provided exclusively according to the new requirements from point 1, which define EGRUL 4.08 and EGRIP 4.07.
- The access page still lists RUB 150,000 annual access per registry/workstation, RUB 50,000 one-time full data and RUB 5,000 one-time updated data.
- Access still requires access attributes, password and a `*.p12` certificate package.

## Findings

- Official sources currently conflict at the public-text layer:
  - current-page wording still says old and new formats are uploaded in parallel;
  - the same pages also say that from 2026-08-01 only 4.08/4.07 should remain;
  - the order requires exclusive new-format delivery from 2026-08-01.
- Without credentialed FTP access, Atlas cannot determine whether:
  - public pages are stale;
  - old-format directories still exist for some users;
  - delivery differs by recipient category or transition edge case;
  - only the explanatory page text is stale while production FTP is already compliant with the order.

## Live Testing Status

No live testing was performed. Atlas did not obtain FTP credentials, `.p12` certificate access or production file samples.

## Decision

Keep `apis/fns-egrul-egrip-integration/` active, but record the post-cutover state as an official-source conflict rather than a clean confirmed cutover.

The next reliable proof point is either:

- credentialed FTP verification of current directories/files; or
- an updated official FTS page or support clarification that removes the contradiction.

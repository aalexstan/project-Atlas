# DaData API

[Русская версия](README.ru.md)

> A Russian-focused API family for interactive data suggestions, data cleansing, address enrichment, and company lookup.

## Research status

| Field | Value |
|---|---|
| Atlas maturity | **Reviewed** |
| Last verified | **2026-07-23** |
| Provider | LLC Data Q (`ООО «Дейта Кью»`) |
| Product status | Active |
| Live credential test | Not performed |
| Editorial relationship | None known |

**Why not Gold yet:** this profile has primary-source verification and independent analysis, but Atlas has not yet performed a credentialed live test or published the planned comparison with Kontur, official registry access, and Seldon.

## Quick verdict

**Best for:** Russian products that need fast address and company data entry, normalization, enrichment, and lookup through one provider.

**Avoid when:** the project needs deep worldwide address standardization, requires OAuth-based delegated authorization, or plans to use the Suggestions service for unattended batch cleansing.

**Bottom line:** DaData is a strong default candidate for Russian web forms, CRM/ERP onboarding, address normalization, and company lookup. Its main trade-off is commercial complexity: subscription services and pay-per-record services are billed differently, richer fields require higher plans, and the contract explicitly restricts using Suggestions for automatic processing of addresses, names, and email addresses.

## What DaData is

DaData is not a single endpoint. It is a family of APIs covering:

- postal addresses and geocoding;
- Russian company and individual entrepreneur data;
- banks;
- names;
- telephone numbers;
- passport reference checks;
- email addresses;
- vehicles and public reference directories;
- account usage, balance, and reference-version information.

The product has two especially important technical families:

1. **Suggestions and search** — interactive autocomplete and identifier lookup.
2. **Cleansing / standardization** — server-side normalization and enrichment of existing records.

These families use different hostnames, credentials, limits, and pricing rules.

## Best-fit scenarios

| Scenario | Fit | Why |
|---|---|---|
| Address autocomplete in a Russian checkout or CRM | Strong | Interactive suggestions, granular address fields, FIAS/GAR and KLADR identifiers, coordinates and postal data |
| Company lookup by INN, KPP or OGRN | Strong | Dedicated lookup endpoint and tier-dependent enrichment from Russian official registries |
| Normalizing an existing Russian address database | Strong | Dedicated cleansing API with quality codes and enriched address fields |
| Geocoding Russian addresses | Strong | Coordinates are available through address cleansing/geocoding methods |
| Worldwide city-level suggestions | Medium | Suggestions support cities worldwide, but detailed enrichment outside supported countries is limited |
| Global address cleansing to building or unit level | Weak | Address standardization is documented as Russia-only |
| Unattended bulk cleansing through Suggestions | Not suitable | The public offer prohibits using Suggestions for automatic processing of addresses, names and email |
| OAuth-based multi-tenant delegated access | Weak | Public documentation uses API token and secret-key authentication, not OAuth |

## Provider and product identity

| Field | Value | Status |
|---|---|---|
| Brand | DaData | Verified |
| Legal provider | ООО «Дейта Кью» / LLC Data Q | Verified |
| INN | 7721581040 | Verified |
| Official site | https://dadata.ru/ | Verified |
| API directory | https://dadata.ru/api/ | Verified |
| Pricing | https://dadata.ru/pricing/ | Verified |
| Offer and legal documents | https://dadata.ru/offer/ | Verified |
| Public status page | https://status.dadata.ru/ | Verified |
| Support | https://support.dadata.ru/ | Verified |

## Core capabilities

### Addresses

- interactive address suggestions;
- address cleansing and standardization;
- forward and reverse geocoding;
- lookup by FIAS/GAR, KLADR or cadastral identifier;
- city by IP address;
- postal-office lookup;
- delivery-service city identifiers;
- postal code, coordinates, administrative and municipal divisions;
- tier-dependent enrichment such as distance to ring roads, cadastral number, nearby metro, apartment area and estimated value.

The deepest address standardization is Russia-only. Suggestions cover all countries at least to city level, with deeper documented coverage for Russia, Belarus, Kazakhstan and Uzbekistan.

### Companies and individual entrepreneurs

- lookup by INN, INN/KPP and OGRN;
- interactive company suggestions by identifier, name, manager or address;
- status, legal address and core registration fields;
- tier-dependent tax regime, workforce, founders, managers, financial data, licenses, SME registry and related data;
- affiliated-company search on the Maximum plan;
- separate paid products for company-by-email and brand-by-INN.

DaData notes that Russian tax data does not provide branch KPP values for about 25% of companies, so exact branch lookup may be incomplete.

### Other data types

DaData also documents APIs for banks, names, phone numbers, passport reference data, email validation, vehicles, tax offices, courts, customs offices and public classifications.

## Technical access

| Field | Suggestions / search | Cleansing / standardization |
|---|---|---|
| Style | HTTP JSON API | HTTP JSON API |
| Typical base | `https://suggestions.dadata.ru/suggestions/api/4_1/rs` | `https://cleaner.dadata.ru/api/v1/clean` |
| Method | Usually `POST` | `POST` |
| Authentication | `Authorization: Token <API_KEY>` | `Authorization: Token <API_KEY>` plus `X-Secret: <SECRET_KEY>` |
| Encoding | UTF-8 | UTF-8 |
| Browser use | Supported for documented suggestion flows | Not supported from browser JavaScript because the secret would be exposed |
| OpenAPI | Available | Available |
| Webhooks | Not found in reviewed public documentation | Not found in reviewed public documentation |
| OAuth 2.0 | Not found | Not found |

### Example: company lookup

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Token ${DADATA_API_KEY}" \
  -d '{"query":"7707083893","branch_type":"MAIN"}' \
  https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party
```

### Example: address cleansing

Run this only from a trusted backend. Do not expose the secret key in browser code.

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Token ${DADATA_API_KEY}" \
  -H "X-Secret: ${DADATA_SECRET_KEY}" \
  -d '["мск сухонска 11/-89"]' \
  https://cleaner.dadata.ru/api/v1/clean/address
```

## OpenAPI and SDKs

DaData publishes OpenAPI schemas for:

- cleansing methods;
- Suggestions and search methods;
- account methods such as balance, usage statistics and reference versions.

Provider-organization repositories confirmed during this review:

| Language | Repository | Classification |
|---|---|---|
| Python | https://github.com/hflabs/dadata-py | Provider-organization client |
| PHP | https://github.com/hflabs/dadata-php | Provider-organization client |
| C# / .NET | https://github.com/hflabs/dadata-csharp | Provider-organization client |
| Go | https://github.com/ekomobile/dadata | Community client referenced in official docs |

The Python client README reviewed on 2026-07-23 requires Python 3.9+ and supports synchronous and asynchronous clients.

## Pricing verified on 2026-07-23

### Annual subscription services

| Plan | Daily shared request limit | Public annual price | Notes |
|---|---:|---:|---|
| Free | 10,000 | ₽0 | Similar to Light in field coverage; DaData branding appears in Suggestions |
| Light | 50,000 | ₽14,000/year | Core address and company fields |
| Extended | 100,000 | ₽28,000/year | Adds selected enriched address and company fields |
| Maximum | From 200,000 | From ₽56,000/year | Richest subscription data; higher daily volumes are selectable |

Important pricing behavior:

- subscriptions are sold for at least one year;
- the daily limit is shared across subscription services;
- after the daily limit is exhausted, subscription services stop until the next day;
- one interactive form completion may generate many API calls because Suggestions sends requests while a user types;
- higher-tier fields cannot be purchased individually on the free tier.

### Pay-per-record services

Some services are outside every subscription and charge the account balance separately.

| Service example | Public unit price |
|---|---:|
| Address cleansing / standardization | ₽0.20 per address |
| Address geocoding | ₽0.20 per address |
| Cadastral-number lookup | ₽0.20 per address |
| Name standardization | ₽0.20 per name |
| Phone validation | ₽0.20 per phone |
| Email validation | ₽0.20 per email |
| Vehicle recognition | ₽0.20 per vehicle |
| Company by email | ₽7 per email |
| Brand by INN | ₽7 per brand |

**Decision warning:** calculate the chosen endpoint mix, not only the subscription price. A project may pay for a subscription and still consume balance for cleansing or other pay-per-record services.

## Limits

### Suggestions and company lookup

- maximum documented request frequency: **30 requests/second per IP**;
- maximum creation of new connections: **60/minute per IP**;
- `query` length: **up to 300 characters**;
- daily request volume follows the subscription plan;
- address Suggestions returns at most 20 items per request;
- the offer prohibits using Suggestions for automatic processing of addresses, names and email.

### Address cleansing

- one address per request;
- maximum documented request frequency: **20 requests/second per IP**;
- maximum creation of new connections: **60/minute per IP**;
- server-side use only: browser JavaScript is not supported because the secret key would be exposed;
- public price: **₽0.20 per record**.

## Availability and support

The public offer revision dated 20 April 2026 states:

- average monthly availability of at least **99%**;
- weekday downtime between 08:00 and 20:00 Moscow time not exceeding **30 minutes**;
- a service-period extension may be provided for documented, accepted outages;
- forum questions related to the services are answered within **three working days**.

DaData also operates a public status page.

This is a contractual summary, not an independent uptime measurement. Atlas has not yet calculated historical availability from the status page.

## Privacy, storage and rights

The public offer states that, for API processing, DaData does not log or store the source and processed data. It also states that the user is the personal-data operator for data processed through the service, while DaData is not the operator because the user determines the purposes of processing.

Other important contract points:

- processed user data is described as confidential and not transferred to third parties except as provided by the offer;
- the user may not transfer rights under the offer;
- exclusive rights to the site and data belong to DaData or other rightsholders;
- the offer does not clearly grant a general right to redistribute or resell returned data.

**Atlas interpretation:** ordinary use inside a product appears to be the intended service model, but caching, long-term storage, redistribution, resale and building a competing data product should be legally confirmed for the exact endpoint and data source. Do not infer redistribution rights from API access alone.

## Developer experience

### Strengths

- broad functional coverage under one account;
- detailed method-level documentation with request and response examples;
- public sandbox forms in documentation;
- OpenAPI schemas for major API families;
- provider-organization SDKs for Python, PHP and C#;
- explicit HTTP error codes and method limits;
- public pricing, legal documents and status page;
- free tier sufficient for prototypes and many low-volume interactive forms.

### Friction points

- DaData is a product family, so authentication and billing differ by method;
- richer company and address fields depend on subscription tier;
- several high-value methods remain pay-per-record outside subscriptions;
- subscriptions have a one-year minimum;
- Suggestions request consumption can be unintuitive because typing generates multiple calls;
- cleansing requires a secret and cannot safely run in browser code;
- public docs use token/secret authentication rather than scoped OAuth;
- legal reuse rights require endpoint-specific review.

## Independent strengths

1. **Excellent fit for Russian form UX.** Address, company, bank, name and email Suggestions can reduce manual entry in one integration family.
2. **Strong Russian identifiers.** FIAS/GAR, KLADR, INN, KPP, OGRN, OKVED and other local fields are first-class concepts.
3. **Clear separation of interactive and batch workflows.** Suggestions is designed for human selection; cleansing is designed for automatic normalization.
4. **Good transparency.** Public method documentation, pricing, an offer, a status page and OpenAPI schemas are available.
5. **Low prototype barrier.** The free tier offers 10,000 subscription requests per day.

## Independent weaknesses

1. **Not globally deep.** The richest address and registry functions are Russia-centric.
2. **Pricing requires endpoint-level modeling.** Subscription and balance-based services can coexist.
3. **Annual commitment.** Paid subscription plans have a one-year minimum.
4. **Tier-gated enrichment.** Important company fields such as founders and financial data require the Maximum plan.
5. **Suggestions is not a batch-cleansing shortcut.** Both documentation and the offer distinguish interactive Suggestions from automatic processing.
6. **Authorization is account-oriented.** No public OAuth model was identified for delegated or narrowly scoped access.

## Alternatives to compare next

| Alternative | Likely stronger when | Likely weaker when | Atlas status |
|---|---|---|---|
| Kontur company-data products | Formal counterparty due diligence, enterprise workflows and broader risk-analysis context | Simple form suggestions or unified address/name/email UX | Requires full comparison |
| Seldon.Basis | Deep company intelligence, relationships and analytics | Lightweight onboarding and low-cost form integration | Requires full comparison |
| Official FNS / registry access | Primary-source status and selected registry data without an intermediary | Unified schema, ergonomics, enrichment and support | Requires method-by-method review |
| Yandex Geocoder | Mapping ecosystem and map-centric geocoding use cases | Russian company lookup and non-map contact-data cleansing | Requires full comparison |
| 2GIS APIs | Places, maps and local business/geospatial scenarios | Company registry enrichment and contact-data standardization | Requires full comparison |

No winner is declared until these alternatives are researched under the same methodology.

## Scenario-based recommendation

Choose DaData when:

- the product is primarily Russian or CIS-focused;
- interactive data entry quality matters;
- one provider for address, company and contact-data operations is valuable;
- INN/OGRN and FIAS/GAR/KLADR support is important;
- a public free tier and straightforward token integration are useful.

Prefer or evaluate alternatives when:

- the main need is full counterparty risk analysis rather than data entry and enrichment;
- the product requires deep worldwide address validation;
- procurement requires negotiated terms, a custom DPA/NDA or a more extensive enterprise contract;
- redistribution or resale of returned data is central to the business model;
- OAuth scopes and delegated user authorization are mandatory.

Before production commitment:

1. list every endpoint the product will call;
2. classify it as subscription or pay-per-record;
3. estimate Suggestions calls per completed form, not only completed forms;
4. verify required fields against the exact plan;
5. confirm rights for storage, caching and downstream distribution;
6. perform a credentialed load, quality and failure-mode test.

## Open questions

| Question | Impact | Status |
|---|---|---|
| Exact caching and redistribution rights for each returned dataset | High | Needs legal confirmation |
| Independent historical uptime from the status page | Medium | Not measured |
| Current maintenance cadence of PHP and C# provider clients | Medium | Repositories active/not archived, release cadence not reviewed |
| Latency by endpoint and geography | Medium | Not live-tested |
| Accuracy against a representative customer dataset | High | Requires benchmark |
| Corporate-package SLA and negotiated legal terms | Medium | Not reviewed |

## Primary sources

- API directory: https://dadata.ru/api/
- Pricing: https://dadata.ru/pricing/
- Address Suggestions: https://dadata.ru/api/suggest/address/
- Address cleansing: https://dadata.ru/api/clean/address/
- Company lookup: https://dadata.ru/api/find-party/
- Company Suggestions: https://dadata.ru/api/suggest/party/
- Offer page: https://dadata.ru/offer/
- Offer PDF, revision 2026-04-20: https://dadata.ru/files/documents/Оферта_DaData.20260420.pdf
- Status: https://status.dadata.ru/
- Python client: https://github.com/hflabs/dadata-py
- PHP client: https://github.com/hflabs/dadata-php
- C# client: https://github.com/hflabs/dadata-csharp

See [evidence.md](evidence.md) for claim-level verification and [changes.md](changes.md) for Atlas profile history.

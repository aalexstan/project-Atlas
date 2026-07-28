# Provider Request — GLOBAS.API

[Русская версия](provider-request.ru.md)

This checklist is prepared for a vendor conversation with Credinform. It must not be treated as answers from the provider until Credinform responds in writing or provides official documentation.

## Product Scope

1. Is GLOBAS.API a standalone API product, a custom data-delivery service, or an integration option for the GLOBAS web system?
2. Which standard products are included in the API scope?
3. What is outside the standard API scope and requires a separate license or project?
4. Where are the boundaries between standard GLOBAS.API, Sanctions Compliance, Portfolio, monitoring features, and foreign-company reports?
5. Which countries and entity types are covered by the standard API?

## Methods and Fields

1. Please provide the complete API methods list.
2. Please provide a field matrix by method, plan/package, country, and legal form.
3. Which methods support company lookup by INN, OGRN, name, address, manager, owner, phone, email, or foreign identifier?
4. Which fields are current-only, historical, computed, provider-scored, or sourced from public registries?
5. Which fields have source references, timestamps, confidence levels, or update dates?

## Protocol and Authentication

1. What protocol is used: REST, SOAP, file delivery, hybrid API, or another model?
2. What is the production base URL?
3. What authentication model is used: API key, token, OAuth, mTLS, IP allowlist, signed request, or another mechanism?
4. Are separate credentials available for sandbox and production?
5. Are there account, user, role, or method-level permissions?

## Formats, Schemas, Versioning and Errors

1. Which request and response formats are supported: JSON, XML, CSV, XLSX, archive delivery, or another format?
2. Please provide schemas for each method.
3. Is OpenAPI/Swagger available?
4. How is API versioning handled?
5. What is the error model, including validation errors, not-found results, quota errors, rate-limit errors, and provider incidents?
6. Are backward-incompatible changes announced in advance?

## Sandbox and Testing

1. Does the three-day GLOBAS system test include API access?
2. Can Credinform provide sandbox API credentials?
3. Does the sandbox contain synthetic or real data?
4. Are test requests billable?
5. Can a buyer run an equal-sample pilot against other providers?

## Batch, Async and Webhooks

1. Which methods support batch operations?
2. What are the maximum batch size, file size, record count, and processing window?
3. Are asynchronous jobs supported?
4. Is delivery available through webhook, callback URL, SFTP, email, object storage, or another mechanism?
5. Are portfolio monitoring events available through webhooks or scheduled exports?

## Pricing and Billing

1. Please provide method-level pricing.
2. How is batch billing calculated?
3. Are there separate prices for lookup, full profile, monitoring, reports, history, foreign entities, sanctions, or portfolio operations?
4. What is the minimum commitment?
5. How are overage, retries, errors, duplicate records, and cached results billed?
6. Are there setup, integration, support, SLA, or data-package fees?
7. Which prices are API prices rather than web-system subscription prices?

## Limits, SLA and Support

1. What are production rate limits and quotas by method?
2. Are limits per account, credential, IP, method, user, or contract?
3. What SLA is available for uptime, latency, incident response, support response, and data freshness?
4. How are planned maintenance and incidents communicated?
5. Is there a public or customer status page?
6. What support channels are included?

## Data Rights and Legal Use

1. May the buyer store API responses? If yes, for how long?
2. May the buyer cache responses? If yes, what TTL and refresh rules apply?
3. May the buyer display data to its customers, partners, affiliates, or platform users?
4. May the buyer use the data across affiliates or group companies?
5. Is redistribution or resale allowed?
6. Is SaaS embedding allowed?
7. May the buyer use API outputs for scoring, machine-learning features, model training, or automated decisions?
8. Which fields contain personal data, and what legal roles and processing terms apply?
9. What audit, deletion, retention, attribution, and source-reference duties apply?

## Change Management

1. Is there an API changelog?
2. What is the breaking-change policy?
3. What notice period applies for deprecations, field removals, schema changes, pricing changes, or source-coverage changes?
4. Is there a mailing list, customer portal, RSS feed, status page, or contract notice process for API changes?

## Attachments Requested

- API specification or OpenAPI/Swagger.
- Method and field matrix.
- Sample requests and responses.
- Error-code reference.
- Sandbox instructions.
- Pricing appendix.
- SLA/support appendix.
- Data-use, storage, caching, redistribution, affiliate-use and SaaS-embedding terms.
- Changelog or versioning policy.

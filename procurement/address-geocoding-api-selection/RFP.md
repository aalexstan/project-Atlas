# Address and Geocoding API RFP

[Русская версия](RFP.ru.md)

Use these questions for provider evaluation. Do not send credentials, customer data or personal data in the first request.

## Product Scope

- Which products, modules and API methods are included in the offer?
- Which capabilities are covered: suggestions, cleaning, validation, direct geocoding, reverse geocoding, place search, routing, registry data, batch processing?
- Which capabilities require separate products such as Geosuggest, Places, Suggest, Organization Search or routing APIs?
- Which geographies and languages are supported?
- What address granularity is supported: region, city, street, house, building, corpus, entrance, apartment, room?
- What are the official address data sources and update cadence?
- What is the coordinate precision model and how is match level reported?
- What fields can be returned at house level and which require extra paid access?

## Technical Access

- What protocol, base URL and authentication model are used?
- Are OpenAPI/Swagger, SDKs, examples and error references available?
- What request and response formats are supported?
- How are schemas versioned?
- What is the error model and retry guidance?
- Is there a sandbox with API credentials?
- Are test credentials available before contract signing?
- Are batch operations supported?
- Is asynchronous delivery supported?
- Are webhooks or callback URLs supported?
- Are there environment separation, IP restrictions, referer restrictions or key-level limits?
- What is the changelog and breaking-change policy?

## Pricing and Commercial Terms

- What is the unit of billing: request, successful request, address, record, field, method, package, monthly active user or other?
- Provide method-level pricing.
- Provide batch billing rules.
- What is included in the minimum commitment?
- What are overage prices and overage payment rules?
- Are trial/free-tier calls functionally identical to production calls?
- Are higher-precision coordinates, registry fields or organization data extra-cost fields?
- Are there annual discounts or minimum terms?
- Are unused units carried over?
- What support level and SLA are included?
- What incident communication process is provided?

## Limits and Reliability

- What are production daily, monthly and per-second limits?
- Are limits per key, per account, per IP, per method or per product?
- Can limits be raised automatically or only by support request?
- What are typical and percentile latencies?
- What uptime SLA applies?
- Are regional outages/status history public?
- What happens on quota exhaustion?
- What is the allowed retry/backoff behavior?

## Data Rights and Legal Use

- May results be stored long term?
- May results be cached, and for how long?
- May results be shown to end customers?
- May results be displayed on third-party maps?
- Is attribution required?
- May results be redistributed, resold or exported?
- Is SaaS embedding allowed?
- May affiliated companies use the same data/API results?
- May the data be used for scoring, model training, deduplication or internal analytics?
- What personal data obligations apply?
- Is a DPA available?
- What are deletion and audit requirements?
- Are there restrictions on combining results with other address registries or map providers?

## Pilot and Evaluation

- Can we run a pilot on a synthetic/public address sample?
- Can the provider review the benchmark sample before testing?
- Which metrics does the provider recommend for match level, false positives, missing results and coordinate precision?
- Can the provider supply a reference implementation or examples for batch testing?
- What support is available during pilot?

## Boundaries to Confirm

- Does the standard API include sanctions/compliance checks? If not, which separate product does?
- Does the standard API include organization/place search? If not, which separate product does?
- Does the geocoder include routing or distance matrix? If not, which separate product does?
- For official registry integration, what is the boundary between file downloads, API services and government exchange channels?

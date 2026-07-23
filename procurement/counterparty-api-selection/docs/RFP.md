# RFP Questionnaire

[Русская версия](RFP.ru.md)

The complete working tracker is on the Excel **RFP Tracker** sheet.

## Required Sections

### Commercial

Obtain:

- the current API-specific price list;
- method and field composition per package;
- batch and partial-failure billing;
- minimum commitment and setup fee;
- overage rules;
- volume-growth pricing;
- contract term and exit cost.

### Technical Contract

Request:

- OpenAPI, Swagger, or complete specification;
- authentication and key rotation;
- production rate, burst, and concurrency limits;
- `429`, retry, and idempotency behavior;
- batch limits;
- versioning;
- breaking-change notice;
- sandbox and production similarity.

### Data

Require explanations for:

- source of every mandatory field;
- typical and maximum update delay;
- branch handling and stable identifiers;
- mergers, liquidations, and succession;
- correction and removal of errors;
- missing-data semantics;
- historical depth.

### Reliability

Request:

- SLA;
- uptime definition;
- exclusions and remedies;
- status page;
- incident history;
- redundancy and disaster recovery;
- support hours and response SLA.

### Legal Rights

Critical questions:

- response storage;
- retention period;
- caching;
- corporate-group use;
- customer display in SaaS;
- resale of raw or derived data;
- scoring and ML use;
- personal data;
- processing jurisdiction;
- post-termination obligations.

## Acceptance Rule

A response is **Received** only when supported by evidence:

- contract;
- appendix;
- price list;
- specification;
- official written answer;
- current documentation.

A salesperson's verbal promise remains `Clarification needed`.

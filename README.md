# Project Atlas

[Русская версия](README.ru.md)

[![Validate Atlas](https://github.com/aalexstan/project-Atlas/actions/workflows/validate-atlas.yml/badge.svg)](https://github.com/aalexstan/project-Atlas/actions/workflows/validate-atlas.yml)

> **Independent API intelligence for better technical and business decisions.**

Project Atlas is an independent, evidence-based knowledge base for discovering, verifying, comparing, and selecting APIs.

Atlas is not another directory that only lists API names and links. It helps developers, architects, product teams, and businesses answer the harder question:

> **Which API should we use, and why?**

## What Atlas Does

Atlas turns fragmented provider documentation into decision-ready research:

- verifies that an API and its documentation are active;
- explains authentication, pricing, limits, coverage, and commercial restrictions;
- identifies strengths, weaknesses, risks, and suitable use cases;
- compares competing APIs for a concrete task;
- records sources and verification dates;
- tracks important changes over time.

## How Atlas Is Different

An API directory helps users **find** an API.

Atlas helps users:

1. understand whether it fits the task;
2. compare it with realistic alternatives;
3. estimate integration and operating constraints;
4. make a defensible technical or commercial decision.

Catalogs such as API Portal may be used as discovery sources. They are not treated as the final source of truth. Important claims should be checked against official documentation, pricing pages, specifications, provider announcements, and other primary sources.

## Start With A Need

If you know the user problem but not the API, start with the [Needs Index](NEEDS_INDEX.md).

- [Company Verification](needs/company-verification/README.md)
- [Address normalization, address registries and geocoding](needs/address-normalization-geocoding/README.md)
- [Organization and place search](needs/organization-place-search/README.md)
- [Online payment acceptance](needs/payment-acceptance/README.md)
- [Messaging and notifications](needs/messaging-notifications/README.md)
- [Weather and meteorological data](needs/weather-data/README.md)
- [Routing and logistics calculation](needs/routing-logistics/README.md)
- [Procurement and tender data](needs/procurement-tender/README.md)

Then use the related [API Index](API_INDEX.md), [Comparison Index](COMPARISON_INDEX.md), and procurement kits.

For a quick tour of the repository itself, use the [Repository Map](REPOSITORY_MAP.md).

## Core Product Model

The primary public entity is the **API profile**.

Supporting entities may include:

- providers;
- use cases and user needs;
- comparisons;
- datasets exposed by APIs;
- evidence and verification records;
- change history.

Datasets remain important, but they support API evaluation rather than replace the API as the project’s central entity.

## Who Atlas Is For

- Developers selecting an external service.
- Architects evaluating dependencies and vendor risk.
- Product teams estimating feasibility and cost.
- Businesses comparing providers before procurement.
- Researchers studying API markets and infrastructure.

## Content Types

### API Profiles

Structured, independent profiles covering purpose, best-fit scenarios, authentication, pricing, limits, SDKs, legal constraints, strengths, weaknesses, alternatives, evidence, and verification dates.

### Comparisons

Task-oriented comparisons such as company verification APIs, geocoding APIs, payment APIs, messaging APIs, and delivery APIs. A comparison should end with scenario-specific recommendations rather than a universal winner.

### Research and Change Tracking

Research notes preserve how conclusions were reached. Change records track material changes in pricing, documentation, versions, limits, and product availability.

## Maturity Levels

1. **Discovered** — official provider or product page found.
2. **Verified** — core facts checked against primary sources.
3. **Reviewed** — independent analysis, strengths, weaknesses, and risks added.
4. **Compared** — included in at least one meaningful comparison.
5. **Gold** — high-confidence profile maintained as a reference standard.

Maturity is not an API quality score. It measures the completeness of Atlas research.

## Research Principles

- Official sources first.
- Facts before opinions.
- Every important claim should be traceable.
- Unknown information must remain unknown.
- Comparison is more valuable than description.
- Quality is more important than catalog size.
- Commercial relationships must not buy ratings or editorial conclusions.
- Dates matter: pricing, limits, and documentation may change.

See:

- [Documentation Index](docs/README.md)
- [Vision](docs/VISION.md)
- [Principles](docs/PRINCIPLES.md)
- [Methodology](docs/METHODOLOGY.md)
- [Roadmap](docs/ROADMAP.md)
- [Glossary](docs/GLOSSARY.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Migration](docs/MIGRATION.md)

## Repository Direction

```text
apis/            Independent API profiles
comparisons/     Task-oriented comparisons
providers/       Provider-level context
needs/           User problems and solution maps
research/        Research logs and working evidence
changes/         Material API change records
templates/       Reusable profile and comparison templates
docs/            Project rules, methodology, and roadmap
legacy/          Preserved historical material when migration is complete
```

Existing folders do not need to be deleted immediately. Migration should be incremental and preserve useful research provenance.

## Initial Scope

Atlas will begin with a small number of high-value API categories:

- company and counterparty data;
- addresses and geocoding;
- procurement;
- payments and finance;
- messaging and notifications.

The first reference profile, **DaData**, is now published. The first company and counterparty information API comparison is also published. The address and geocoding direction now has active API profiles, a comparison, a need route, and a procurement checklist. The payment direction now has an initial Russia-focused comparison of YooKassa, CloudPayments, and T-Bank Internet Acquiring API. The messaging direction now has separate profiles for Telegram Bot API, SMSC API, and SMS.RU API. The weather direction now has separate profiles for Open-Meteo, WeatherAPI.com, and OpenWeather. The routing direction now separates route calculation, distance matrices, logistics planning and self-hosted OSRM operations.

## Business Direction

Potential revenue streams are downstream of trust:

- paid API selection research;
- Atlas Pro comparisons, exports, alerts, and change history;
- API monitoring for organizations;
- private internal API catalogs;
- clearly disclosed referral partnerships.

Atlas does not sell favorable rankings.

## Current Status

Atlas is in its foundation phase. The current objective is to maintain a repeatable research standard, improve the first reference profile and comparison, and expand coverage without sacrificing evidence quality.

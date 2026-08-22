# Roadmap

[Русская версия](ROADMAP.ru.md)

This roadmap is outcome-based. Dates may change; product principles should not.

## Phase 1 — Foundation

Create bilingual project documents, research methodology, profile template, comparison template, migration guidance, and the first research backlog.

**Success:** a new researcher can create a consistent profile without inventing a format. The foundation now also includes a documentation index, a legacy index, deterministic generated indexes, validation CI, need-based routes, review cadence policy and scheduled source/review monitoring.

## Phase 2 — Gold Standard Profiles

Initial targets: DaData, relevant Kontur and Seldon products, official registry access options, Yandex geocoding, and 2GIS APIs.

**Success:** profiles are materially more useful for selection than provider summaries.

**Current progress:** reviewed address/geocoding profiles now exist for DaData Address APIs, Yandex Maps Geosuggest API, Yandex Maps Geocoder API, Yandex Maps Organization Search API, 2GIS Suggest API, 2GIS Places API, 2GIS Geocoder API, Geoapify Geocoding API, OpenCage Geocoding API, LocationIQ Geocoding API, Nominatim Geocoder Software and FIAS/GAR Data Integration. Provider-specific request checklists are prepared for DaData, Yandex Maps, 2GIS, Geoapify, OpenCage and LocationIQ. The FIAS/GAR open-data XML ZIP route now includes current package metadata, inspected structure XSDs, inspected current data ZIP central directory, parsed root dictionary XML files and parsed sample regional directories `99/`, `87/` and sparse `82/`; the Geoapify/OpenCage/LocationIQ hosted open-data/geocoding routes and Nominatim self-hosting operations path are clearer, while national FIAS/GAR row counts, full/delta semantics, API/SMEV service details, ODbL/legal review and benchmarks remain blockers. The profiles still need live tests, SLA confirmation, data-rights review and quality benchmarks before Gold.

## Phase 3 — Comparison Hub

Routing/logistics is now a separate comparison direction: Yandex Maps route details/matrix, 2GIS Routing API and self-hosted OSRM are kept distinct from geocoding, places and delivery optimization.

Procurement/tender now has reviewed EIS integration and Seldon.Tenders routes, with explicit blockers around current schemas, access, commercial terms and data rights.

Delivery now has separate reviewed routes for Russian Post tracking and Yandex Delivery order lifecycle; carrier aggregation remains a future research class.

Yandex Rasp API is reviewed for free public intercity timetable features; commercial and long-term storage use remains blocked by published terms unless Yandex agrees otherwise.

Avtocod Vehicle History API is reviewed as a commercial report route; independent data-quality evidence, pricing, limits and high-stakes use rights remain open.

Real-estate/cadastral research now includes a reviewed official EGRN access profile, comparison, need route and procurement kit. It separates EGRN extracts, key-based access, NSPD, DaData enrichment and FIAS/GAR; unattended automation, current terms and reuse rights remain blockers.

Initial comparisons: company and counterparty data, addresses and geocoding, procurement data, messaging, payments, and financial data.

**Success:** each comparison provides scenario-specific recommendations, evidence, and a review date. Need-based routes should connect common user questions to the relevant profiles, comparisons, and procurement kits.

**Current progress:** company/counterparty, address/geocoding, payment acceptance, messaging, and weather comparisons are published. Payment acceptance has reviewed profiles for YooKassa, CloudPayments, and T-Bank Internet Acquiring API. Messaging has separate reviewed profiles for Telegram Bot API, SMSC API, and SMS.RU API. Weather has separate reviewed profiles for Open-Meteo, WeatherAPI.com, and OpenWeather. Comparable quotes, production limits, SLA, legal terms, regional quality and common testing remain open. Procurement/tender now has a research baseline, EIS technical-information route recheck and linked legacy dataset note, but no active procurement API comparison exists yet.

The company/counterparty comparison now includes an official-source conflict recheck for the FTS EGRUL/EGRIP format transition. Credentialed FTP verification or updated official clarification remains required before claiming production file behavior.

## Phase 4 — Distribution and Feedback

Publish content in searchable form, collect requests, track interest, interview users, and offer a limited paid API selection research service.

**Success:** real users use Atlas to support an API decision.

## Phase 5 — Atlas Pro

Potential features: full comparison matrices, saved shortlists, exports, pricing and limit history, material change alerts, organization workspaces, and private notes.

Build only after demand is demonstrated.

## Phase 6 — Enterprise Intelligence

Potential features: private API catalogs, dependency ownership, vendor risk, deprecation monitoring, policy fields, and team workflows.

## Explicitly Deferred

- universal graph database;
- complex AI recommendations;
- thousands of shallow imported profiles;
- opaque global rankings;
- a full marketplace;
- infrastructure unrelated to research quality.

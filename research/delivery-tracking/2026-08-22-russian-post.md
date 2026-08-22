# Russian Post Tracking API research

## Scope

Review the official Russian Post API for tracking registered postal items. This is a tracking API, not an order-creation or courier-management API.

## Official sources reviewed

- [Tracking service FAQ](https://tracking.pochta.ru/support/faq/service_about)
- [Tracking API specification](https://tracking.pochta.ru/specification)
- [Russian Post business API help](https://otpravka.pochta.ru/help/)

## Confirmed facts

- The service provides programmatic tracking information for registered postal items.
- Single access retrieves one item per request and is available to registered users with a 100-request daily limit.
- Batch access supports up to 3,000 tracking numbers in a request and is available only to customers with a contract for parcels, letters or EMS.
- Single access uses SOAP 1.2 at the documented service URL and provides `getOperationHistory` and `PostalOrderEventsForMail` methods.
- The specification documents login/password access parameters, RUS and ENG response language values, and operation-history fields including time, place and operation data.

## Unknowns and blockers

- Contract price, production SLA, support, throughput, retry policy, storage and redistribution rights are not confirmed in the reviewed public sources.
- No credentialed live call, data-quality benchmark or batch test was performed.

## Decision

Create a reviewed profile as an official postal tracking API. Keep it separate from shipment creation, carrier aggregation and courier dispatch.


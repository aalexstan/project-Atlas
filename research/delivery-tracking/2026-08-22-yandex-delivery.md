# Yandex Delivery API research

## Scope

Review the official Yandex Delivery business API for delivery order lifecycle. It is not a general parcel-tracking aggregator.

## Official sources reviewed

- [Yandex Delivery quick start](https://yandex.ru/support/delivery-profile/ru/api/express/quickstart)
- [Yandex Delivery OpenAPI resources](https://yandex.ru/support/delivery-profile/ru/api/express/openapi/)
- [Yandex Delivery API integration page](https://dostavka.yandex.ru/integrations/api/)

## Confirmed facts

- Yandex Delivery uses HTTP requests for delivery-order creation and bearer-token authentication obtained through the business account.
- The official reference lists order creation, confirmation, cancellation, order information, status tracking, order search, courier-location and ETA-related operations.
- The reference states some operations have v1 and v2 versions and recommends v2 for new users.
- Yandex markets API integration for automatic order creation, delivery-price display and customer status updates.

## Unknowns and blockers

- Public API-specific price, production quotas, rate limits, SLA, storage, customer display, SaaS and redistribution terms were not confirmed in the reviewed sources.
- No credentials, sandbox call or live delivery order was used.

## Decision

Create a reviewed profile for a managed delivery-order API. Keep it separate from postal tracking and from map-routing APIs.

